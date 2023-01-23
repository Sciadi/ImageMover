import os
from elapsed_time import time_it
from pathlib import Path
from datetime import datetime
from time import time
from datetime import datetime

pathin = '\\\chstwin.twin-set.it\\plm-img\\99999'

@time_it
def iter():
    directory = pathin
    files = os.listdir(directory)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)))
    last_10_files = files[-10:]
    print(last_10_files)

@time_it
def scan():
    directory = pathin
    files = list(os.scandir(directory))
    files.sort(key=lambda x: x.stat().st_mtime)
    last_10_files = [f.name for f in files[-10:]]
    print(last_10_files)

@time_it
def pythonic():
    directory = Path(pathin)
    files = list(directory.iterdir())
    files.sort(key=lambda x: x.stat().st_mtime)
    #last_10_files = [f.name for f in files[-10:]]
    today_files = files.sort(key=lambda x: x.stat().st_mtime)
    print(today_files)

@time_it
def gettodayf(f):
    directory = f
    today_timestamp = datetime.now().timestamp()//(24*3600)

    # filter the files
    today_added_files = [f.name for f in directory.iterdir() if f.stat().st_mtime//(24*3600) == today_timestamp ]
    print(today_added_files)



# iter()
# scan()
# pythonic()

curr_time = time()
stat_time = os.path.getmtime(pathin)


print(str(datetime.fromtimestamp(curr_time))+' '+ str(datetime.fromtimestamp(stat_time)))

"""if curr_time > stat:
    print('curr_time')
else:
    print('stat')
"""



