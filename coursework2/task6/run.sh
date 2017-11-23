echo "************************************************************************"
echo "*                                                                      *"
echo "*                   Task 6          EXC Coursework 2                   *"
echo "*                                                                      *"
echo "************************************************************************"
echo 

if [ -f "/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt" ]
then
echo ----Executing task6 with parameter false positive rate 1%-----------------------------------------------
echo ----**The bloomfilter_old.py is a single machine version, but with better GUI**-------------------------
echo ----**The bloomfilter.py can be used both in single machine and in parallel, **-------------------------
echo '----  the same bloomfilter.py will be used in task7 again.                     -------------------------'
echo 
echo 'Command: time cat webLarge.txt | ./bloomfilter.py -n 1897987 -m raw -h raw 2>execute_log.txt 1>output_full.out'
echo
echo '----  You can open a new terminal use:  watch tail -n 1 execute_log.txt   to monitor the progress ------   '
rm -f output.out >/dev/null 2>&1
rm -f output_full.out >/dev/null 2>&1
rm -f execute_log.txt >/dev/null 2>&1
time cat /afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt | ./bloomfilter.py -n 1897987 -m raw -h raw 2>execute_log.txt 1>output_full.out
cat output_full.out | head -20 >output.out
echo ----Done! The summary information saved in execute_log.txt --------------------------------------------
echo ----The output saved in output_full.out, and the top 20 lines in output.out----------------------------
else
echo ----Wrong!Input file does not exist.-------------------------------------------------------------------
fi

exit 0

