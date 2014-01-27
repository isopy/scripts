import os

print "Full path to puppet modules (i.e. /home/mjohnson/puppet-cfg/modules)"
puppet_mod_loc=raw_input("-->")

print "Full path to versionmerge-init script (i.e. /usr/bin/versionmerge-init)"
versionmerge_loc=raw_input("-->")

print os.listdir(puppet_mod_loc)
print "##"
print os.listdir(versionmerge_loc)
print "##"