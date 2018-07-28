# -*- coding: utf-8 -*-
# @Time : 18-7-28 上午10:39
# @Author : weicheng.wang# @Site : 
# @File : sequence_test.py
# @Software: PyCharm


from collections import abc
import numbers

class Group:

    def __init__(self,group_name,company_name,staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reverse()

    def __getitem__(self, item):

        cls = type(self)
        if isinstance(item,slice):
            return cls(group_name=self.group_name,company_name=self.company_name,staffs=self.staffs[item])
        elif isinstance(item,numbers.Integral):
            return cls(group_name=self.group_name,company_name=self.company_name,staffs=[self.staffs[item]])


    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)


    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


if __name__ == '__main__':
    staffs =["a","b","c","d"]
    group = Group(company_name="DDD",group_name="SSS",staffs=staffs)
    group[:2]

