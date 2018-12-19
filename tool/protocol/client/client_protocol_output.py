# -*- coding: utf-8 -*-

import sys
import xlrd

def _str2int(s):
		try:
			return int(s)
		except ValueError:
			return 0
def _str2float(s):
		try:
			return float(s)
		except ValueError:
			return 0.0
			
def _str2bool(s):
		try:
			return bool(s)
		except ValueError:
			return 0
	
new_file_template = \
"""# -*- coding: utf-8 -*-

"""
import os
import csv
class CSVSheet(object):
	def __init__(self, fname):
		self.m_Lines = []
		fh = file(fname, "rb")
		reader = csv.reader(fh)
		col, row = 0, 0
		for line in reader:
			self.m_Lines.append(line)
			col = max(len(line), col)
			row += 1
		self.ncols = col
		self.nrows = row
	
	def cell_value(self, y, x):
		s = self.m_Lines[y][x]
		if s.isdigit():
			return int(s)
		return s

class CSVWorkbook(object):
	def __init__(self, path_name):
		self.m_Sheets = {}
		_, _, filenames = os.walk(path_name).next()		#只取第一层目录
		for fname in filenames:
			name, dot, ext = fname.rpartition(".")
			if dot == "." and ext == "csv":
				self.m_Sheets[name.decode("GBK")] = CSVSheet(path_name + "/" + fname)
	
	def sheet_by_name(self, sheet_name):
		return self.m_Sheets.get(sheet_name)
def _check_type(tp):
	#if tp == "byte8":
	#	tp = "string8"
	#elif tp == "byte16":
	#	tp = "string16"
	#elif tp == "byte32":
	#	tp = "string32"
	return tp
def ReadBaseTypeFile(path):
	bk = CSVWorkbook(path);
	filename = "扩展类型"
	sh = bk.sheet_by_name(filename.decode("GBK"))
	headers = ["类型名称","备注", ["属性", "类型", "子类型","说明"]];
	fd = LoadSheet(sh, headers)
	s = ""
	for name,note,ndata in fd:
		s += "\t\'%s\':["%name;
		for pro,ty,sty,content in ndata:
			s += "[\'%s\', \'%s\', \'%s\'],"%(pro, _check_type(ty), _check_type(sty));
		s += "],\n"
	return s
def ReadProtocolFile(path,filename):
	bk = CSVWorkbook(path);
	sh = bk.sheet_by_name(filename.decode("GBK"))
	headers = ["协议名称","协议值","备注", ["属性", "类型", "子类型","说明"]];
	fd = LoadSheet(sh, headers)
	s = ""
	pn2v = [];
	s2c_list = [];
	c2s_list = [];
	for n,v,c,ndata in fd:
		s += "\t\'%s\':["%n;
		pn2v.append("%s = %s;\n"%(n,v));
		lown = n.lower();
		if lown.find('c2s_') == 0:
			c2s_list.append(n)
		else:
			s2c_list.append(n)
		for pro,ty,sty,content in ndata:
			s += "[\'%s\', \'%s\', \'%s\'],"%(pro, _check_type(ty), _check_type(sty));
		s += "],\n"
	return s,pn2v,s2c_list,c2s_list
def MakePythonProtocolFileV2(path):
	basetype_s = ReadBaseTypeFile(path);
	cfg_py_path = path + "/协议配置.csv"
	import csv
	csvfile = file(cfg_py_path, 'r')
	file_content = csv.reader(csvfile);
	
	idx = 0;
	protocol_s = ""
	p2v_s = [];
	s2c_l = [];
	c2s_l = [];
	for line in file_content:
		if idx > 0:
			subpath = line[0];
			ps,p2v,s2cl,c2sl = ReadProtocolFile(path,subpath);
			protocol_s += ps;
			p2v_s.extend(p2v);
			s2c_l.extend(s2cl);
			c2s_l.extend(c2sl);
		idx = idx + 1;
	csvfile.close();
	
	output_s = "Protocol_desc = {\n";
	output_s += basetype_s;
	output_s += protocol_s;
	output_s += "}\n"
	
	c2s_p2struct_s = "\nexport const C2S_CMD_2_PROTODESC:{[key:number]:string;} = {}\n";
	for i in c2s_l:
		c2s_p2struct_s += "C2S_CMD_2_PROTODESC[%s]=\'%s\';\n"%(i,i);
	s2c_p2struct_s = "\nexport const S2C_CMD_2_PROTODESC:{[key:number]:string;} = {}\n";
	for i in s2c_l:
		s2c_p2struct_s += "S2C_CMD_2_PROTODESC[%s]=\'%s\';\n"%(i,i);
		
	p2v_s_py = "";
	p2v_s_ts = "";
	for i in p2v_s:
		p2v_s_ts += "export const "+i;
		p2v_s_py += i;
	err = OutputFile("ProtocolDesc.py", output_s+p2v_s_py, "#protocol_desc start\n", "\n#protocol_desc end",False)
	if err:
		return err
	err = OutputFile("ProtocolDesc.ts","export let "+output_s+p2v_s_ts+s2c_p2struct_s+c2s_p2struct_s, "module protocol_def{\n", "\n}",False,False);
	if err:
		return err
	return
def MakePythonProtocolFile(bk):
	sh = bk.sheet_by_name("Sheet1".decode("GBK"))
	headers = ["name", ["property", "type", "value"]]
	fd = LoadSheet(sh, headers)
	s = "Protocol_desc = {\n"
	for name, rdata in fd:
		s += "\t\'%s\':["%name;
		for p,t,v in rdata:
			s += "[\'%s\', \'%s\', \'%s\'],"%(p, t, v);
		s += "],\n"
	s += "}\n"
	err = OutputFile("ProtocolDesc.py", s, "#protocol_desc start\n", "\n#protocol_desc end",False)
	if err:
		return err
	err = OutputFile("ProtocolDesc.ts","export let "+s, "module protocol_def{\n", "\n}",False,False);
	if err:
		return err
	return
#######################################################
def is_type_str(d):
	return (type(d) is str) or (type(d) is unicode)
def LoadSheet(sh, headers, begin_row = 1):
	blst = []
	#print 'LoadSheet %s'%headers;
	for y in xrange(begin_row, sh.nrows):
		x = 0
		lst = []
		for h in headers:
			#print 'h %s %s'%(h,type(h))
			if type(h) is list:
				lst.append(LoadList(sh, 0, x, y, h))
				x += getcol(h)
			else:
				d = sh.cell_value(y, x)
				#print 'd %s %s %s %s'%(x,d,type(d),len(d));
				if x == 0 and (is_type_str(d)) and len(d) == 0:
					break
				else:
					x += 1
					if isinstance(d, unicode):
						d = d.encode("GBK")
					lst.append(d)
		if len(lst) > 0:
			blst.append(lst)
	return blst
def LoadList(sh, base, xs, ys, headers):
	blst = []
	for y in xrange(ys, sh.nrows):
		bd = sh.cell_value(y, base)
		if y > ys and ((not is_type_str(bd)) or len(bd) > 0):
			return blst
		
		x = xs
		lst = []
		for h in headers:
			if type(h) is list:
				lst.append(LoadList(sh, xs, x, y, h))
				x += getcol(h)
			else:
				d = sh.cell_value(y, x)
				if x == xs and is_type_str(d) and len(d) == 0:
					break
				x += 1
				if isinstance(d, unicode):
					d = d.encode("GBK")
				lst.append(d)
		if len(lst) > 0:
			blst.append(lst)
	return blst

def getcol(h):
	cnt = 0
	for f in h:
		if type(f) is list:
			cnt += getcol(f)
		else:
			cnt += 1
	return cnt

def CheckOutput(headers, output):
	for v in headers:
		if output.find(v[1]) != -1:
			return "output error[%s]"%v[1]

def OutputFile(filename, output, prefix = None, suffix = None,bAdd = False,bAddTemp = True):
	try:
		f = open(filename, "rU")
	except IOError:
		f = open(filename, "wb")
		if bAddTemp:
			f.write(new_file_template)
		f.write(prefix+"\n")
		f.write(suffix+"\n")
		f.close()
		f = open(filename, "rU")
	
	f = open(filename, "wb")
	if bAddTemp:
		f.write(new_file_template)
	f.write(prefix+"\n")
	f.write(output+"\n")
	f.write(suffix+"\n")
	f.close()

def CheckHeader(sh, headers):
	for idx, head in enumerate(headers):
		if sh.cell_value(0,idx).encode("GBK") != head[0]:
			return "file table head error<" + head[0] + ">"
	return None


			
def Sheet2Dict(sh, headers, template, prefix = None, suffix = None):
	err = CheckHeader(sh, headers)
	if err:
		return err
	
	out = ""
	if prefix:
		out = prefix
	try:
		for y in xrange(1, sh.nrows):
			tmp = template
			for x in xrange(min(sh.ncols,len(headers))):
				d = sh.cell_value(y,x)
				if isinstance(d, unicode):
					d = d.encode("GBK")
					d = d.replace("\"","\\\"")
				if isinstance(d, float) and headers[x][2] == "%s" and d%1 == 0:
					d = _str2int(d);
				if headers[x][2] == "%d":
					d = _str2int(d);
				if headers[x][1][0] == '$':
					tmp = tmp.replace(headers[x][1], headers[x][2]%d)
			err = CheckOutput(headers, tmp)
			if err:
				return "data(line:%d)"%y + err
			out += tmp
	except:
		print traceback.print_exc()
		return sh.name
	if suffix:
		out += suffix
	return out

def Sheet2Pyfile(sh, headers, fileprefix, template, moduleprefix, path, outfile, prefix = None, suffix = None, wrappers = None, outprefix = ""):
	import_lst = "\n"
	module = "\n"
	
	err = CheckHeader(sh, headers)
	if err:
		return err
	
	tmp = None
	for y in xrange(1, sh.nrows):
		id = sh.cell_value(y,0)
		if isinstance(id,str) and len(id) == 0:
			pass
		else:
			if tmp != None:
				for k, v in last.items():
					tmp = tmp.replace("$"+k[1:], v)
				err = CheckOutput(headers, tmp)
				if err:
					return "data(%d)"%last_id + err
				err = OutputFile(path + "%s%.4d.py"%(fileprefix, last_id), tmp)
				if err:
					return err
			last_id = id
			import_lst += "import %s%s%.4d\n"%(outprefix, fileprefix, id)
			module += "%s[%d] = %s%s%.4d\n"%(moduleprefix, id, outprefix, fileprefix, id)
			tmp = template
			last = {}
		
		vmap = {}
		wmap = {}
		for x in xrange(min(sh.ncols,len(headers))):
			d = sh.cell_value(y,x)
			if isinstance(d, unicode):
				d = d.encode("GBK")
				d = d.replace("\"","\\\"")
			if headers[x][1][0] == '+' and not vmap.has_key(headers[x][1]):
				vmap[headers[x][1]] = ""
			if headers[x][1][0] == '*' and not last.has_key(headers[x][1]):
				last[headers[x][1]] = ""
			if isinstance(d, str) and len(d) == 0:
				continue
			if headers[x][1][0] == '@' and not wmap.has_key(headers[x][1]):
				wmap[headers[x][1]] = ""
			if headers[x][1][0] == '$':
				tmp = tmp.replace(headers[x][1], headers[x][2]%d)
			elif headers[x][1][0] == '+':
				vmap[headers[x][1]] += headers[x][2]%d
			elif headers[x][1][0] == '*':
				last[headers[x][1]] += headers[x][2]%d
			elif headers[x][1][0] == '@':
				wmap[headers[x][1]] += headers[x][2]%d
		for k, v in vmap.items():
			tmp = tmp.replace("$"+k[1:], v)
		if wrappers:
			for k, v in wrappers.items():
				if not last.has_key(k):
					last[k] = ""
				tv = v
				for sk, sv in wmap.items():
					tv = tv.replace("$"+sk[1:], sv)
				if tv != v:
					last[k] += tv
	
	if tmp != None:
		for k, v in last.items():
			tmp = tmp.replace("$"+k[1:], v)
		err = CheckOutput(headers, tmp)
		if err:
			return "data(%d)"%last_id + err
		err = OutputFile(path + "%s%.4d.py"%(fileprefix, last_id), tmp)
		if err:
			return err
	
	import_lst += "\n"
	module += "\n"
	
	if prefix == None:
		prefix = "#"
	if suffix == None:
		suffix = "#"
	
	if type(outfile) is list:
		outfile.append(import_lst + module)
	else:
		return OutputFile(path + outfile, import_lst + module, prefix, suffix)

def CheckError(prefix, err):
	if err:
		print prefix,err
		pdb.set_trace();
		raise IOError

def MakePyfile(path):
	MakePythonProtocolFileV2(path)
	return;
	bk = xlrd.open_workbook(path+'/protocol.xls')
	err = MakePythonProtocolFile(bk)
	CheckError('protocol_desc error!:',err)


def SearchTable():
	ret = 0;
	tableDict = {
			'buff.xls':['Sheet1'],
		};
	
	for k, v in tableDict.iteritems():
		bk = xlrd.open_workbook(k);
		for i in v:
			fd = [];
			sh = bk.sheet_by_name(i.decode("GBK"));
			fd = getTableData(sh, 1);
			fd.sort(key = lambda x:x[0]);
			reStr = FindRepeatID(fd); 
			if len(reStr) > 0:
				ret = -1;
				print "tablename:%s sheetname:%s"%(k, i);
				print reStr
	return ret;

def getTableData(sh, begin_row = 1):
	blst = [];
	for y in xrange(begin_row, sh.nrows):
		x = 0;
		value = sh.cell_value(y,x);
		tmplist = [];
		if value != None and value != '':
			tmplist.append(value);
			tmplist.append(y+1);
			blst.append(tmplist);
	return blst;

def FindRepeatID(fd):
	lenfd = len(fd);
	repeatStr = '';
	for i in xrange(0, lenfd -1):
		if fd[i][0] == fd[i+1][0]:
			repeatStr += "repeat ID:%d, line no:%d, col no:%s \n"%(int(fd[i][0]), int(fd[i][1]), fd[i+1][1]);
	return repeatStr;

if __name__ == "__main__":
	import sys
	arg = None
	if len(sys.argv) == 2:
		arg = sys.argv[1]
	MakePyfile(arg);
	#SearchTable();
#############################################	
