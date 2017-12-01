#include <stdio.h>
#include <math.h>
#include <malloc.h>
#include <string.h>

#define N 729
#define reps 1000 
#include <omp.h> 

double a[N][N], b[N][N], c[N];
int jmax[N];  


void init1(void);
void init2(void);
void runloop(int); 
void loop1chunk(int, int);
void loop2chunk(int, int);
void valid1(void);
void valid2(void);


int main(int argc, char *argv[]) { 

  double start1,start2,end1,end2;
  int r;

  init1(); 

  start1 = omp_get_wtime(); 

  for (r=0; r<reps; r++){ 
    runloop(1);
  } 

  end1  = omp_get_wtime();  

  valid1(); 

  printf("Total time for %d reps of loop 1 = %f\n",reps, (float)(end1-start1)); 


  init2(); 

  start2 = omp_get_wtime(); 

  for (r=0; r<reps; r++){ 
    runloop(2);
  } 

  end2  = omp_get_wtime(); 

  valid2(); 

  printf("Total time for %d reps of loop 2 = %f\n",reps, (float)(end2-start2)); 

} 

void init1(void){
  int i,j; 

  for (i=0; i<N; i++){ 
    for (j=0; j<N; j++){ 
      a[i][j] = 0.0; 
      b[i][j] = 3.142*(i+j); 
    }
  }

}

void init2(void){ 
  int i,j, expr; 

  for (i=0; i<N; i++){ 
    expr =  i%( 3*(i/30) + 1); 
    if ( expr == 0) { 
      jmax[i] = N;
    }
    else {
      jmax[i] = 1; 
    }
    c[i] = 0.0;
  }

  for (i=0; i<N; i++){ 
    for (j=0; j<N; j++){ 
      b[i][j] = (double) (i*j+1) / (double) (N*N); 
    }
  }
 
} 



//////////////////////////////////////////////////////////////////////
///////////// New structure's defination /////////////////////////////
typedef struct _TopList {
  int thread_num;
  int avail_size;
} TopList ;


//////////////////////////////////////////////////////////////////////
///////////// New functions's defination /////////////////////////////

//Update the available size of the thread in Top List, while reordering the whole list 
void updatetoplist(TopList *plist , int list_len , int t_num , int avail_size);

//Get a piece of work from a specific thread's local trunk
int gettrunk(int (*pavail)[2] , TopList *plist , int t_num , int t_size , int *plow , int *phigh);

//Assign a new trunk to a specific thread 
int dispatchwork(int (*pavail)[2] , omp_lock_t *plock , TopList *plist , \
             int t_num , int t_size ,  int *plow , int *phigh);


//////////////////////////////////////////////////////////////////////
///////////// New version of runloop function ////////////////////////
void runloop(int loopid)  {
  //Shared values among threads
  int (*pavail)[2];	//The boundary value of each thread's local trunk
  TopList *plist;	//The ordered list of threads number by their available trunk size
  omp_lock_t top_lock;  //Lock for serialize the work assignment actions

//  printf("***********LOOP BEGIN*********************\n");

#pragma omp parallel default(none) shared(loopid,pavail,plist,top_lock) 
  {
    int myid  = omp_get_thread_num();
    int nthreads = omp_get_num_threads();
//    printf("INIT:T_ID-%d TOTAL-%d\n",myid,nthreads);

//    int ipt = (int) ceil((double)N/(double)nthreads); 
//    int lo = myid*ipt;
//    int hi = (myid+1)*ipt;
//    if (hi > N) hi = N; 

#pragma omp single
    {
      //Apply the space to store the trunk's boundary for available loops
      pavail = (int(*)[2])malloc( sizeof(int)*2*nthreads );
      int block_size = N /nthreads ;
      
      //Set the initial trunk bundary for each thread and init the locks.
      for (int i = 0; i < nthreads; i++)
      {
        pavail[i][0] = i * block_size;
        pavail[i][1] = (i+1) * block_size;
        if ( N - (i+1) * block_size < block_size )
          pavail[i][1] = N;
      }
      //Initialize the top list and lock
      omp_init_lock(&top_lock) ;
      plist = (TopList *)malloc(sizeof(TopList)*nthreads);
      memset(plist,-1,sizeof(TopList)*nthreads);
    }

    int result = 1;
    int lo, hi;
    
    while ( dispatchwork(pavail,&top_lock,plist,myid,nthreads,&lo,&hi) )  {
      printf("CALC%d:T_ID-%d   LOW:%d  HIGH:%d \n",loopid,myid,lo,hi-1);
      switch (loopid) {
        case 1: loop1chunk(lo,hi); break;
        case 2: loop2chunk(lo,hi); break;
      }
    }  
  }
}

void loop1chunk(int lo, int hi) { 
  int i,j; 
  
  for (i=lo; i<hi; i++){ 
    for (j=N-1; j>i; j--){
      a[i][j] += cos(b[i][j]);
    } 
  }

} 



void loop2chunk(int lo, int hi) {
  int i,j,k; 
  double rN2; 

  rN2 = 1.0 / (double) (N*N);  

  for (i=lo; i<hi; i++){ 
    for (j=0; j < jmax[i]; j++){
      for (k=0; k<j; k++){ 
	c[i] += (k+1) * log (b[i][j]) * rN2;
      } 
    }
  }
}

void valid1(void) { 
  int i,j; 
  double suma; 
  
  suma= 0.0; 
  for (i=0; i<N; i++){ 
    for (j=0; j<N; j++){ 
      suma += a[i][j];
    }
  }
  printf("Loop 1 check: Sum of a is %lf\n", suma);

} 


void valid2(void) { 
  int i; 
  double sumc; 
  
  sumc= 0.0; 
  for (i=0; i<N; i++){ 
    sumc += c[i];
  }
  printf("Loop 2 check: Sum of c is %f\n", sumc);
} 

/////////////////////////////////////////////////////////////////////
/////////////New functions developed in this coursework//////////////

//Update the available size of the thread in Top List, while reordering the whole list 
void updatetoplist(TopList *plist , int list_len , int t_num , int avail_size)  {
  int origin_num = t_num;
  TopList tp_swap,tp_cur;
  tp_cur.thread_num = t_num;
  tp_cur.avail_size = avail_size;
  
  int iter_mode = 0;				
  for (int i=0; i<list_len; i++)  {
    if (iter_mode == 0) {
      if (plist[i].thread_num == -1) {
        plist[i] = tp_cur;
        break;
      }
      else if (plist[i].thread_num ==  origin_num) {
        plist[i] = tp_cur;
        iter_mode = 1;
      } 
      else if (plist[i].avail_size < tp_cur.avail_size )  {
        tp_swap = plist[i] ;
        plist[i] = tp_cur ;
        tp_cur = tp_swap ;
      }
    }
    else if (iter_mode == 1) {
      if (plist[i].thread_num == -1) break;
      else if (plist[i].avail_size > plist[i-1].avail_size) {
        tp_swap = plist[i] ; 
        plist[i] = plist[i-1];
        plist[i-1] = tp_swap;
      }
      else break;  
    }
  }
}

//Get a piece of work from a specific thread's local trunk
int gettrunk(int (*pavail)[2] , TopList *plist ,  int t_num , int t_size , int *plow , int *phigh) {
  int get_size = 0;
  int avail_size = pavail[t_num][1] - pavail[t_num][0];

  if ( avail_size > 0 ) {
    *plow = pavail[t_num][0];
    get_size = avail_size / t_size;

    if (get_size == 0 )  get_size = 1;
    *phigh = *plow + get_size;
    pavail[t_num][0] += get_size;

    avail_size =  pavail[t_num][1] - pavail[t_num][0];
    updatetoplist(plist,t_size,t_num,avail_size);

    return 1;
  }
  else return 0;
}
  

//Assign a new trunk to a specific thread
int dispatchwork(int (*pavail)[2] , omp_lock_t *plock , TopList *plist , \
             int t_num , int t_size ,  int *plow , int *phigh)          {
//  printf("DISPA:T_ID-%d LOW-%d  HIGH-%d  LOW-%d HIGH-%d LIST-%d  AVAIL-%d\n",t_num,pavail[t_num][0],pavail[t_num][1],pavail[t_size-1][0],pavail[t_size-1][1],plist[0].thread_num,plist[0].avail_size);

  int result = 1;
  omp_set_lock(plock);

  if (gettrunk(pavail,plist,t_num,t_size,plow,phigh) == 0) {
    if (plist[0].avail_size > 0) {
      if (gettrunk(pavail,plist,plist[0].thread_num,t_size,plow,phigh) == 0)
        result = 0;
      }
      else result = 0;
  }

  omp_unset_lock(plock);
  return result ;
}

