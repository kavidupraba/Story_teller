#!/usr/bin/bahs

if [ $# -eq 0 ];then
  echo "please add the file in the end"
  exit 1
fi

python3 story_teller.py $1
