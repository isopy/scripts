#!/usr/bin/env python
import subprocess

#Create variables that contain the shell commands
uptime = "uptime > /root/sanity-check_uptime.log_`date +%m%d%y-%T`"
netstat = "netstat -nap > /root/sanity-check_netstat.log_`date +%m%d%y-%T`"
mount = "mount > /root/sanity-check_mount.log_`date +%m%d%y-%T`"
ps = "ps auxwwf > /root/sanity-check_ps.log_`date +%m%d%y-%T`"
lsof = "lsof > /root/sanity-check_lsof.log_`date +%m%d%y-%T`"
ifconfig = "ifconfig -a > /root/sanity-check_ifconfig.log_`date +%m%d%y-%T`"
route = "route -n > /root/sanity-check_route.log_`date +%m%d%y-%T`"
env = "env > /root/sanity-check_env.log_`date +%m%d%y-%T`"
fstab = "cat /etc/fstab > /root/sanity-check_fstab.log_`date +%m%d%y-%T`"
yum_log = "cat /var/log/yum.log > /root/sanity-check_yum.log_`date +%m%d%y-%T`"

#Places variables into a list/array
cmds = [uptime, netstat, mount, ps, lsof, ifconfig, route, env, fstab, yum_log]

#Create a function, that takes a list parameter
#Function uses default keyword parameter of cmds
def runCommands(command=cmds):
    #Iterates over list, running statements for each item in the list
    for cmd in cmds:
        subprocess.call(cmd, shell=True)

runCommands()
