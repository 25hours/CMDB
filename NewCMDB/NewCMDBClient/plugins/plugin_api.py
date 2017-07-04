from NewCMDB.NewCMDBClient.plugins.linux import sysinfo
from NewCMDB.NewCMDBClient.plugins.windows import sysinfo as win_sysinfo

def LinuxSysInfo():
    #print __file__
    return  sysinfo.collect()
def WindowsSysInfo():
    return win_sysinfo.collect()