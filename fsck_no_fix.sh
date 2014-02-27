#!/bin/bash
for i in `cat /tmp/servicejavas`
do
  echo "-----------------"
  echo $i
  echo "-----------------"
  printf "/n"
  ssh root@$i   \
  fsck / -C --n 
done
