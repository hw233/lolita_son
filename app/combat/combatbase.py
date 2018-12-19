#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''

class combatbase(dict):
	def __init__(self):
		super(combatbase,self).__init__();
		return
	def print_data(self):
		print "data %s"%(self);
		return
	def set_data(self,data_dict):
		for k,v in data_dict.items():
			self[k] = v;
		return