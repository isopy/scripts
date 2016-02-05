#!/bin/bash
puppet_mods=$1

if [ "$1" == "-h" ]; then
  echo -e "Usage:\n\t./versionmerge-the-things.sh </path/to/your/puppet/modules/>\n"
  exit 0
fi

if [ -d $puppet_mods ]; then
    for m in `ls $puppet_mods`; do
        cd $puppet_mods/$m
        versionmerge-init
    done
else
    echo "That directory does not exist.  Check your path and try again."
fi
