echo "************************************************************************"
echo "*                                                                      *"
echo "*                   Task 5          EXC Coursework 2                   *"
echo "*                                                                      *"
echo "************************************************************************"


if [ -f "/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt" ]
then
echo ----Executing task5.py with parameter 100 lines
echo 'Command: cat /afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt | ./task5.py 100 >output_full.out'
rm -f output.out >/dev/null 2>&1
rm -f output_full.out >/dev/null 2>&1
cat /afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt | ./task5.py 100 >output_full.out
cat output_full.out | head -20 >output.out
echo ----Done! The output saved in output_full.out, and the top 20 lines in output.out
fi

exit 0

