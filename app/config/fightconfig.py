# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fightconfig_map = {};
fightconfig_map[1000] = {"id":1000,"lv":0,"data":[{"num":1,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.09)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":80,},{"num":2,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.10)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":80,},{"num":3,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.12)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":80,},{"num":4,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.13)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":80,},{"num":5,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.15)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":80,},],"skill1":0,"slv1":0,"skill2":0,"slv2":0,"skill3":0,"slv3":0,"skill4":0,"slv4":0,"skill5":0,"slv5":0,"skill6":0,"slv6":0,"skill7":0,"slv7":0,"skill8":0,"slv8":0,"skill9":0,"slv9":0,"skill10":0,"slv10":0,};
fightconfig_map[1001] = {"id":1001,"lv":0,"data":[{"num":1,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.09)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":80,},{"num":2,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.10)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":80,},{"num":3,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.12)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":80,},{"num":4,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.13)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":80,},{"num":5,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.15)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":80,},],"skill1":6589,"slv1":0,"skill2":1004,"slv2":0,"skill3":6511,"slv3":0,"skill4":1503,"slv4":0,"skill5":1001,"slv5":0,"skill6":0,"slv6":0,"skill7":0,"slv7":0,"skill8":0,"slv8":0,"skill9":0,"slv9":0,"skill10":0,"slv10":0,};
fightconfig_map[1002] = {"id":1002,"lv":0,"data":[{"num":1,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.09)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":90,},{"num":2,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.10)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":90,},{"num":3,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.12)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":90,},{"num":4,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.13)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":90,},{"num":5,"hp":0,"hpnum":0,"hidehp":0,"enegytp":0,"enegy":999999,"hideenegy":0,"attack":"(lv*12+lv**2*0.15)*0.7","speed":"lv*4","dodge":"85+lv*0.1","hit":"120+lv*0.1","skillrate":90,},],"skill1":6589,"slv1":0,"skill2":2002,"slv2":0,"skill3":2303,"slv3":0,"skill4":6521,"slv4":0,"skill5":2102,"slv5":0,"skill6":6527,"slv6":0,"skill7":0,"slv7":0,"skill8":0,"slv8":0,"skill9":0,"slv9":0,"skill10":0,"slv10":0,};


class Fightconfig:
	def __init__(self, key):
		config = fightconfig_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fightconfig(key):
		config = fightconfig_map.get(key);
		if not config:
			return
		return Fightconfig(key)

