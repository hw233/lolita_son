# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


cards_exp_map = {};
cards_exp_map[1] = {"lv":1,"exp":300,"atk":1,"hpmax":10,"stamaniamax":10,};
cards_exp_map[2] = {"lv":2,"exp":600,"atk":1,"hpmax":10,"stamaniamax":11,};
cards_exp_map[3] = {"lv":3,"exp":900,"atk":1,"hpmax":10,"stamaniamax":12,};
cards_exp_map[4] = {"lv":4,"exp":1200,"atk":1,"hpmax":10,"stamaniamax":13,};
cards_exp_map[5] = {"lv":5,"exp":1500,"atk":1,"hpmax":10,"stamaniamax":14,};
cards_exp_map[6] = {"lv":6,"exp":1800,"atk":2,"hpmax":12,"stamaniamax":15,};
cards_exp_map[7] = {"lv":7,"exp":2100,"atk":2,"hpmax":12,"stamaniamax":16,};
cards_exp_map[8] = {"lv":8,"exp":2400,"atk":2,"hpmax":12,"stamaniamax":17,};
cards_exp_map[9] = {"lv":9,"exp":2700,"atk":2,"hpmax":12,"stamaniamax":18,};
cards_exp_map[10] = {"lv":10,"exp":3000,"atk":2,"hpmax":12,"stamaniamax":19,};
cards_exp_map[11] = {"lv":11,"exp":3500,"atk":3,"hpmax":14,"stamaniamax":20,};
cards_exp_map[12] = {"lv":12,"exp":4000,"atk":3,"hpmax":14,"stamaniamax":21,};
cards_exp_map[13] = {"lv":13,"exp":4500,"atk":3,"hpmax":14,"stamaniamax":22,};
cards_exp_map[14] = {"lv":14,"exp":5000,"atk":4,"hpmax":14,"stamaniamax":23,};
cards_exp_map[15] = {"lv":15,"exp":5500,"atk":4,"hpmax":14,"stamaniamax":24,};
cards_exp_map[16] = {"lv":16,"exp":6000,"atk":4,"hpmax":16,"stamaniamax":25,};
cards_exp_map[17] = {"lv":17,"exp":7000,"atk":5,"hpmax":16,"stamaniamax":26,};
cards_exp_map[18] = {"lv":18,"exp":8000,"atk":5,"hpmax":16,"stamaniamax":27,};
cards_exp_map[19] = {"lv":19,"exp":9000,"atk":5,"hpmax":16,"stamaniamax":28,};
cards_exp_map[20] = {"lv":20,"exp":10000,"atk":6,"hpmax":20,"stamaniamax":30,};


class Cards_exp:
	def __init__(self, key):
		config = cards_exp_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Cards_exp(key):
		config = cards_exp_map.get(key);
		if not config:
			return
		return Cards_exp(key)

