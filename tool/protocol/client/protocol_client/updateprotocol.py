# -*- coding: gbk -*-

import os
import csv

def MakeClientProtocol():
	headers = ["��������", "���", "��ע", "����", "����", "������", "˵��"]
	fn = os.path.abspath("../protocol/��չ����.csv")
	fr = open(fn, "rb")
	fn = os.path.abspath("Э��鿴.csv")
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

	headers = ["Э������", "Э��ֵ", "��ע", "����", "����", "������", "˵��"]
	fn = os.path.abspath("../protocol/Э������.csv")
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

	print "�������"

if __name__ == "__main__":
	MakeClientProtocol()