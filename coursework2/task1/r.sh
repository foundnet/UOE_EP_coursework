set fileformat = UNIX
export STREAM=/opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar > /dev/null
export RPATH=/user/$USER/assign2/data

task=task1
filename=./*.txt

echo --Remote folder and file preparation
hdfs dfs -rm -r $RPATH/input/$task > /dev/null 2>&1
hdfs dfs -rm -r $RPATH/output/$task > /dev/null 2>&1
hdfs dfs -mkdir $RPATH/input/$task
hdfs dfs -copyFromLocal $filename $RPATH/input/$task/
echo done!

echo --Run hadoop command
hadoop jar $STREAM -D stream.num.map.output.key.fields=2 -D num.key.fields.for.partition=1 -mapper mapper.py -combiner combiner.py -reducer "cat" -input $RPATH/input/$task -output $RPATH/output/$task -file mapper.py -file combiner.py -file reducer.py 

echo --Output files
rm -r ../../../Result/$task > /dev/null 2>&1
mkdir ../../../Result > /dev/null 2>&1
hdfs dfs -copyToLocal $RPATH/output/$task ../../../Result
mkdir ../../../Result/$task/composed
cat ../../../Result/$task/part* > ../../../Result/$task/composed/output.txt
echo done!

echo --Upload Result
hdfs dfs -mkdir /user/$USER/assignment2/ > /dev/null 2>&1
hdfs dfs -rm -r /user/$USER/assignment2/$task > /dev/null 2>&1
hdfs dfs -mkdir /user/$USER/assignment2/$task
hdfs dfs -cp $RPATH/output/$task/* /user/$USER/assignment2/$task
echo done

exit 0

