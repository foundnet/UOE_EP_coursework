set fileformat = UNIX
export STREAM=/opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar > /dev/null
export RPATH=/user/$USER/data

task=task8
filename=/data/assignments/ex1/uniLarge.txt

echo --Remote folder and file preparation
hdfs dfs -rm -r $RPATH/input/$task > /dev/null 2>&1
hdfs dfs -rm -r $RPATH/output/$task > /dev/null 2>&1
hdfs dfs -mkdir $RPATH/input/$task
hdfs dfs -cp $filename $RPATH/input/$task
echo done!

echo --Run hadoop command
hadoop jar $STREAM -mapper mapper.py -combiner combiner.py -reducer reducer.py -input $RPATH/input/$task -output $RPATH/output/$task -file mapper.py -file combiner.py -file reducer.py -numReduceTasks 1

echo --Output files
rm -r ../Result/$task > /dev/null 2>&1
mkdir ../Result > /dev/null 2>&1
hdfs dfs -copyToLocal $RPATH/output/$task ../Result
mkdir ../Result/$task/composed
cat ../Result/$task/part* > ../Result/$task/composed/output.txt
echo done!

echo --Upload Result
hdfs dfs -mkdir /user/$USER/assignment1/ > /dev/null 2>&1
hdfs dfs -rm -r /user/$USER/assignment1/$task > /dev/null 2>&1
hdfs dfs -mkdir /user/$USER/assignment1/$task
hdfs dfs -cp $RPATH/output/$task/* /user/$USER/assignment1/$task
echo done

exit 0

