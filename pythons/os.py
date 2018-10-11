#!/usr/bin/python

import os

path=os.getcwd()
print(path)

list=os.listdir(path)
print(list)

#delFile=path+"/test1.log"
#os.remove(delFile)

print(os.path.isfile(path))
print(os.path.isdir(path))

print(os.path.exists(path))

lpath="/home/liqing/test.log"
print(os.path.split(lpath))

print(os.path.splitext(lpath))

print(os.path.dirname(lpath))
print(os.path.basename(lpath))

print(os.name)

#os.makedirs("./li/qing/test")
#os.mkdir("./qing")

#print(os.stat("./test.log"))

#print(os.path.getsize("./test.log"))

fp = open("test.log", "a+")
fp.write("liqingliqing\r\n")
fp.flush()
print(fp.tell())
fp.seek(0)
print(fp.read(3))
print(fp.tell())
fp.seek(0)
print(fp.readline())
fp.close()


print('------------------')
def change_name(path):
	global i
	if not os.path.isdir(path) and not os.path.isfile(path):
		return False
	if os.path.isfile(path):
		path_file = os.path.split(path)
		file_ext = path_file[1].split('.')
		log_ext = ['log', 'txt']
		ext = file_ext[-1]
		if ext in log_ext:
			os.rename(path, path_file[0] + '/' + file_ext[0] + '_fc.' + ext)
	elif os.path.isdir(path):
		for x in os.listdir(path):
			change_name(os.path.join(path, x))




test_path = os.getcwd()
change_name(test_path)

