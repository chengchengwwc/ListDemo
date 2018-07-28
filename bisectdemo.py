# -*- coding: utf-8 -*-
# @Time : 18-7-28 下午12:51
# @Author : weicheng.wang# @Site : 
# @File : bisectdemo.py
# @Software: PyCharm

import bisect

#用来维护已经排序的序列
#二分查找


inter_list = []
bisect.insort(inter_list,3)
bisect.insort(inter_list,1)
bisect.insort(inter_list,8)
bisect.insort(inter_list,2)
print (bisect.bisect(inter_list,1))
print (bisect.bisect_left(inter_list,1))


