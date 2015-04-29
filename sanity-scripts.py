#!/usr/bin/env python
import subprocess

#Create variables that contain the shell commands
uptime = "uptime >> /root/sanity-checks.log_`date +%F`"
netstat = "netstat -nap >> /root/sanity-checks.log_`date +%F`"
mount = "mount >> /root/sanity-checks.log_`date +%F`"
ps = "ps auxwwf >> /root/sanity-checks.log_`date +%F`"
lsof = "lsof >> /root/sanity-checks.log_`date +%F`"
ifconfig = "ifconfig -a >> /root/sanity-checks.log_`date +%F`"
route = "route -n >> /root/sanity-checks.log_`date +%F`"
env = "env >> /root/sanity-checks.log_`date +%F`"
fstab = "cat /etc/fstab >> /root/sanity-checks.log_`date +%F`"
yum_log = "cat /var/log/yum.log >> /root/sanity-checks.log_`date +%F`"

#Places variables into a list/array
cmds = [uptime, netstat, mount, ps, lsof, ifconfig, route, env, fstab, yum_log]

#Create a function, that takes a list parameter
#Function uses default keyword parameter of cmds
def runCommands(command=cmds):
    #Iterates over list, running statements for each item in the list
    for cmd in cmds:
        subprocess.call('echo -e "####################" >> /root/sanity-checks.log_`date +%F`', shell=True)
        subprocess.call(cmd, shell=True)
        subprocess.call('echo -e "\n" >> /root/sanity-checks.log_`date +%F`', shell=True)

runCommands()
