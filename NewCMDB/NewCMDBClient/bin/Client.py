import os,sys,platform
from NewCMDB.NewCMDBClient.core import main
#for linux
if platform.system() == "Windows":
    BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
    print (BASE_DIR)
else:
    BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    main.ArgvHandler(sys.argv)