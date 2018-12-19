# -*- coding: gbk -*-

import os
import csv

def MakeClientProtocol():
	headers = ["类型名称", "编号", "备注", "属性", "类型", "子类型", "说明"]
	fn = os.path.abspath("../protocol/扩展类型.csv")
	fr = open(fn, "rb")
	fn = os.path.abspath("协议查看.csv")
	fw = open(fn, "wb")
	fcsv = csv.writer(fw)
	fcsv.writerow(headers)
	for idx, line in enumerate(csv.reader(fr)):
		if idx == 0:
			continue
		fcsv.writerow(line[:1] + [""] + line[1:-1])
	for i in xrange(3):
		fcsv.writerow([""] * 6)
	fr.close()

	headers = ["协议名称", "协议值", "备注", "属性", "类型", "子类型", "说明"]
	fn = os.path.abspath("../protocol/协议配置.csv")
	fcfg = open(fn, "rb")
	fcsv.writerow(headers)
	for line in csv.reader(fcfg):
		fn = os.path.abspath("../protocol/%s.csv"%(line[0]))
		if not os.path.exists(fn):
			continue
		fr = open(fn, "rb")
		for line in csv.reader(fr):
			if line == headers:
				continue
			fcsv.writerow(line)
		fr.close()
	fcfg.close()
	fw.close()

	print "更新完成"

if __name__ == "__main__":
	MakeClientProtocol()