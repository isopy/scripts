#!/usr/bin/bash
OF=myhome_directory_$(date +%Y%m%d).tar.gz
tar -cvzf $OF /home/mjohnson > /tmp/$OF
