import shutil
tup=shutil.disk_usage("c:/")
print(tup)
print(tup[0]/(1024*1024*1024))
