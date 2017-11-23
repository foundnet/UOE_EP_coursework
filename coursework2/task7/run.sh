echo "************************************************************************"
echo "*                                                                      *"
echo "*                   Task 7          EXC Coursework 2                   *"
echo "*                                                                      *"
echo "************************************************************************"
echo 

if [ -f "/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt" ]
then
echo ----Executing task7 with false positive rate 1% and parallel cmd---------------------------------------------
echo ----**The bloomfilter.py is the same with the one in task6, only ran in parallel.**--------------------------
echo 
echo 'Command: cat webLarge.txt |      \'
echo '         parallel -k --pipe --block 5M ./bloomfilter.py -n 1897987 -m raw -h hash 2>>execute_log_s1.txt |  \'
echo '         ./bloomfilter.py -n 1897987 -m hash -h raw 2>execute_log.txt 1>output_full.txt'
echo
echo '----  You can open a new terminal use:  watch tail -n 1 execute_log.txt   to monitor the progress -----------'
rm -f output.out >/dev/null 2>&1
rm -f output_full.out >/dev/null 2>&1
rm -f execute_log* >/dev/null 2>&1

time cat /afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt | parallel -k --pipe --block 5M ./bloomfilter.py -n 1897987 -m raw -h hash 2>>execute_log_s1.txt | ./bloomfilter.py -n 1897987 -m hash -h raw 1>output_full.out

cat output_full.out | head -20 >output.out
echo ----Done! The summary information saved in execute_log.txt --------------------------------------------------
echo ----The output saved in output_full.out, and the top 20 lines in output.out----------------------------------
else
echo ----Wrong!Input file does not exist.-------------------------------------------------------------------------
fi

exit 0

