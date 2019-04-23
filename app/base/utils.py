# coding: utf-8

def _str2int(s):
		try:
			return int(float(s))
		except ValueError:
			return 0
def _str2float(s):
		try:
			return float(s)
		except ValueError:
			return 0.0

def gen_player_atk(lv):
	return lv*100;
def gen_player_def(lv):
	return lv*5;
def gen_player_hpmax(lv):
	return lv*200;
def gen_player_spd(lv):
	return lv*100;
