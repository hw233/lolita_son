# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


${config_map}

class ${class_name}:
	def __init__(self, key):
		config = ${config_map_name}.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_${class_name}(key):
		config = ${config_map_name}.get(key);
		if not config:
			return
		return ${class_name}(key)

