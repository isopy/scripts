#!/bin/bash

#Change ~/puppet-cfg/modules/* to reflect the path to your modules
for a in ~/puppet-cfg/modules/*;
do
   cd $a
   versionmerge-init
   echo -e "The $a directory has been version-merged\n"
done
