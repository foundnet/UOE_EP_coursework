echo "************************************************************************"
echo "*                                                                      *"
echo "*                   Task 8          EXC Coursework 2                   *"
echo "*                                                                      *"
echo "************************************************************************"
echo 

if [ -f "/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part4/queriesLarge.txt" ]
then
echo ----Executing task8 with threshold 1% and err rate %1-0.9%=0.1%-----------------------------------------
echo 
echo 'Command: cat /afs/inf.ed.ac.uk/group/teaching/exc/ex2/part4/queriesLarge.txt |    \'
echo '         ./task8.py 2>execute_log.txt 1>output_full.out'
echo
rm -f output.out >/dev/null 2>&1
rm -f output_full.out >/dev/null 2>&1
rm -f execute_log* >/dev/null 2>&1

cat /afs/inf.ed.ac.uk/group/teaching/exc/ex2/part4/queriesLarge.txt | ./task8.py 2>execute_log.txt 1>output_full.out
cat output_full.out | head -20 >output.out
echo ----Done! The summary information saved in execute_log.txt --------------------------------------------
echo ----The output saved in output_full.out, and the top 20 lines in output.out----------------------------
else
echo ----Wrong!Input file does not exist.-------------------------------------------------------------------
fi

exit 0

