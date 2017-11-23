echo "************************************************************************"
echo "*                                                                      *"
echo "*               Task 3 - Step 1/2      EXC Coursework 2                *"
echo "*                                                                      *"
echo "************************************************************************"   


set fileformat = UNIX
export STREAM=/opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar > /dev/null
export RPATH=/user/$USER/assign2/data

task=task3
filename=/data/assignments/ex2/part2/stackLarge.txt

echo --Remote folder and file preparation
hdfs dfs -rm -r $RPATH/input/$task > /dev/null 2>&1
hdfs dfs -rm -r $RPATH/output/$task > /dev/null 2>&1
hdfs dfs -mkdir $RPATH/input/$task
hdfs dfs -mkdir $RPATH/input/$task/step1
hdfs dfs -mkdir $RPATH/output/$task
hdfs dfs -cp $filename $RPATH/input/$task/step1
echo done!

echo --Run hadoop command
#hadoop jar $STREAM -mapper mapper.py -reducer reducer.py -input $RPATH/input/$task -output $RPATH/output/$task -file mapper.py -file reducer.py -numReduceTasks 1
hadoop jar $STREAM -mapper mapper.py -reducer reducer.py -input $RPATH/input/$task/step1 -output $RPATH/output/$task/step1 -file mapper.py -file reducer.py


echo --Output files
rm -r ../../../Result/$task > /dev/null 2>&1
mkdir ../../../Result > /dev/null 2>&1
hdfs dfs -copyToLocal $RPATH/output/$task ../../../Result
mkdir ../../../Result/$task/step1/composed
cat ../../../Result/$task/step1/part* | sort -t $'\t' -k1,1 -k3n,3  > ../../../Result/$task/step1/composed/output.txt
echo done!

echo --Upload Result
#hdfs dfs -mkdir /user/$USER/assignment2/ > /dev/null 2>&1
#hdfs dfs -rm -r /user/$USER/assignment2/$task > /dev/null 2>&1
#hdfs dfs -mkdir /user/$USER/assignment2/$task
#hdfs dfs -cp $RPATH/output/$task/* /user/$USER/assignment2/$task
echo done
echo "************************************************************************"
echo "*                                                                      *"
echo "*               Task 3 - Step 2/2      EXC Coursework 2                *"
echo "*                                                                      *"
echo "************************************************************************"  

filename=../../../Result/$task/step1/composed/output.txt

echo --Remote folder and file preparation
hdfs dfs -rm -r $RPATH/input/$task > /dev/null 2>&1
hdfs dfs -rm -r $RPATH/output/$task > /dev/null 2>&1
hdfs dfs -mkdir $RPATH/input/$task
hdfs dfs -mkdir $RPATH/input/$task
hdfs dfs -copyFromLocal $filename $RPATH/input/$task
echo done!

echo --Run hadoop command
hadoop jar $STREAM -mapper mapper_2.py -combiner combiner_2.py -reducer reducer_2.py -input $RPATH/input/$task -output $RPATH/output/$task -file mapper_2.py -file reducer_2.py -file combiner_2.py  -numReduceTasks 1

echo --Output files
mkdir ../../../Result > /dev/null 2>&1
rm ../../../Result/$task/* > /dev/null 2>&1
hdfs dfs -copyToLocal $RPATH/output/$task/* ../../../Result/$task/
echo done!

echo --Upload Result
hdfs dfs -mkdir /user/$USER/assignment2/ > /dev/null 2>&1
hdfs dfs -rm -r /user/$USER/assignment2/$task > /dev/null 2>&1
hdfs dfs -mkdir /user/$USER/assignment2/$task
hdfs dfs -cp $RPATH/output/$task/* /user/$USER/assignment2/$task
echo done
