# -*- coding:utf-8 -*-
import re
import os
import time
import math
import os.path
import datetime

# 提取时间戳，


def time_stamp2time(x):
    time_list = [str(i) for i in x.split(' --> ')]
    time_list1_1 = [x for x in time_list[0].split(':')]
    time_list1_2 = [int(x) for x in time_list1_1[2].split(',')]
    time_list1_1.pop()

    time_list2_1 = [x for x in time_list[1].split(':')]
    time_list2_2 = [int(x) for x in time_list2_1[2].split(',')]
    time_list2_1.pop()

    t1 = [int(time_list1_1[0]), int(time_list1_1[1]),
          (time_list1_2[0]+time_list1_2[1]/1000)]
    t2 = [int(time_list2_1[0]), int(time_list2_1[1]),
          (time_list2_2[0]+time_list2_2[1]/1000)]
    return t1, t2

# 加上指定的时间


def modifying_time(time, s):
    time[2] = time[2]+s
    if time[2] >= 60:
        time[1] = time[1]+int(time[2]//60)
        time[2] = time[2] % 60
        if time[1] >= 60:
            time[0] = time[0]+int(time[1]//60)
            time[1] = time[1] % 60
    return time
# 返回时间戳


def time2time_stamp(x):
    x.append(round((x[2]-math.floor(x[2])), 3))
    x[2] = math.floor(x[2])
    H = str(x[0]).zfill(2)
    M = str(x[1]).zfill(2)
    S = str(x[2]).zfill(2)
    MS = str(int(x[3]*1000)).zfill(3)
    time_stamp = H+':'+M+':'+S+','+MS
    return time_stamp


f = input('请输入文件路径：',)
s = float(input('请输入向后移动时间轴的秒数：',))
starttime = datetime.datetime.now()

# 打开字幕文件
with open(f, 'r') as f1:
    path, name = os.path.split(f)
    f2 = open(os.path.join(path, 'Temporary.txt'), 'a')
    for line in f1:
        if re.match(r'\d{1,2}:\d{1,2}:\d{1,2},\d{1,3} --> \d{1,2}:\d{1,2}:\d{1,2},\d{3}', line):
            line = line.strip()
            time_stamp1 = line

            t1, t2 = time_stamp2time(time_stamp1)

            t1 = modifying_time(t1, s)
            t2 = modifying_time(t2, s)

            time_stamp_1 = time2time_stamp(t1)
            time_stamp_2 = time2time_stamp(t2)
            time_stamp2 = time_stamp_1+' --> '+time_stamp_2+'\n'
            line = time_stamp2
        f2.write(line)
    f2.close()
# 写入完毕后删除原文件
os.remove(name)
os.rename('Temporary.txt', name)
endtime = datetime.datetime.now()
print('转换耗时：', endtime - starttime)
