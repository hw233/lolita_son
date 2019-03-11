# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


sys_open_map = {};
sys_open_map["坐骑"] = {"sys_name":"坐骑","condition":"1.0","value":10,"isshow":1,"tips":"达到10级开启坐骑",};
sys_open_map["羽翼"] = {"sys_name":"羽翼","condition":"1.0","value":70,"isshow":1,"tips":"达到70级开启羽翼",};
sys_open_map["时装"] = {"sys_name":"时装","condition":"1.0","value":40,"isshow":0,"tips":"达到40级开启时装",};
sys_open_map["称号"] = {"sys_name":"称号","condition":"1.0","value":25,"isshow":0,"tips":"达到25级开启称号",};
sys_open_map["经脉"] = {"sys_name":"经脉","condition":"1.0","value":95,"isshow":0,"tips":"达到95级开启经脉",};
sys_open_map["丹药"] = {"sys_name":"丹药","condition":"1.0","value":58,"isshow":0,"tips":"达到58级开启丹药",};
sys_open_map["精灵"] = {"sys_name":"精灵","condition":"1.0","value":50,"isshow":1,"tips":"达到50级开启精灵",};
sys_open_map["光武"] = {"sys_name":"光武","condition":"1.0","value":64,"isshow":1,"tips":"达到64级开启光武",};
sys_open_map["仙侣"] = {"sys_name":"仙侣","condition":"1.0","value":20,"isshow":1,"tips":"达到20级开启仙侣",};
sys_open_map["仙阵"] = {"sys_name":"仙阵","condition":"1.0","value":74,"isshow":1,"tips":"达到74级开启仙阵",};
sys_open_map["境界"] = {"sys_name":"境界","condition":"1.0","value":78,"isshow":1,"tips":"达到78级开启境界",};
sys_open_map["奇缘"] = {"sys_name":"奇缘","condition":"1.0","value":20,"isshow":1,"tips":"达到20级开启奇缘",};
sys_open_map["宠物"] = {"sys_name":"宠物","condition":"1.0","value":1,"isshow":1,"tips":"达到1级开启宠物",};
sys_open_map["光环"] = {"sys_name":"光环","condition":"1.0","value":82,"isshow":1,"tips":"达到82级开启光环",};
sys_open_map["兽魂"] = {"sys_name":"兽魂","condition":"1.0","value":86,"isshow":1,"tips":"达到86级开启兽魂",};
sys_open_map["游历"] = {"sys_name":"游历","condition":"1.0","value":50,"isshow":1,"tips":"达到50级开启游历",};
sys_open_map["通关文牒"] = {"sys_name":"通关文牒","condition":"1.0","value":50,"isshow":1,"tips":"达到50级开启通关文牒",};
sys_open_map["大唐授印"] = {"sys_name":"大唐授印","condition":"1.0","value":50,"isshow":1,"tips":"达到50级开启大唐授印",};
sys_open_map["天仙"] = {"sys_name":"天仙","condition":"1.0","value":90,"isshow":1,"tips":"达到90级开启天仙",};
sys_open_map["仙器"] = {"sys_name":"仙器","condition":"1.0","value":95,"isshow":1,"tips":"达到95级开启仙器",};
sys_open_map["仙云"] = {"sys_name":"仙云","condition":"1.0","value":100,"isshow":1,"tips":"达到100级开启仙云",};
sys_open_map["灵气"] = {"sys_name":"灵气","condition":"1.0","value":105,"isshow":1,"tips":"达到105级开启灵气",};
sys_open_map["器灵"] = {"sys_name":"器灵","condition":"1.0","value":110,"isshow":1,"tips":"达到100级开启器灵",};


class Sys_open:
	def __init__(self, key):
		config = sys_open_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Sys_open(key):
		config = sys_open_map.get(key);
		if not config:
			return
		return Sys_open(key)

