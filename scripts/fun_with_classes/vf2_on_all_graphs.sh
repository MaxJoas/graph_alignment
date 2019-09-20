#!/bin/bash

#tries a python script on all graphs in graphs/ and puts the output in test_run.txt

#put the script to test after the bash script like './try_on_all_graphs.sh parser.py'
#maybe the script must be made executable first: 'chmod +x try_on_all_graphs.py'


for file in .
do

  out=VF2_$file.txt

  if [ -a $out ]
    then
      echo "deleting $out"
      rm $out
  fi

  echo "Processing file '$file'..."
  time python $1 "$file" >> $out
  echo >> $out
  echo >> $out
  echo >> $out
done

echo "Done."
