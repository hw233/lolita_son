# -*- coding: utf-8 -*-

import sys
import xlrd

cur_dir = "";

# 职业名字与id表
CLASSES_ID_AND_NAME_MAP	 = {0x13: "龙隐寺",
							0x15: "镇国府",
							0x16: "影盟",
							0x23: "重阳宫",
							0x24: "太虚观",
							0x33: "逍遥派",
							0x35: "烟雨阁",
							0x36: "药王谷",
							};

# 打开excel文件 返回一个data
# @param {string} fileName xlsx文件名
# @param {string} sheetName sheet名
# @returns data
def openExcel(fileName, sheetName):
	data = xlrd.open_workbook(fileName)
	if sheetName:
		return data.sheet_by_name(sheetName.decode('GBK'))
	else:
		return data.sheets()[0]
	return

# 解析转表配置文件
# @param {string} excel类型的配置文件
# @returns {map} 返回一个
def parseConfigFile(config_file):
	print("parseConfigFile(\"%s\")" % config_file);
	table = openExcel(config_file, "Sheet1");
	nrows = table.nrows;	# 行数
	ncols = table.ncols;	# 列数
	fileList = [];
	for r in range(2, nrows):
		row = table.row_values(r);
		# print("[%s, %s, %s]" % (row[0], row[1], row[2]));
		# struct:[fileName, sheet, jsName]
		if isinstance(row[0], unicode):
			row[0] = row[0].encode("GBK")
		if isinstance(row[1], unicode):
			row[1] = row[1].encode("GBK")
		if isinstance(row[2], unicode):
			row[2] = row[2].encode("GBK")
					
		fileList.append([row[0], row[1], row[2]]);
	return fileList

# 解析一个指定的excel表
# @param {string} excel文件名(全路径)
# @param {string} sheet_name 表的页名
# @param {string} js_name 输出的js表名
# @returns {string} 可输出的js文件类型字符串
def parseExcelFile(file_name, sheet_name, js_name):
	excel_table = openExcel(file_name, sheet_name);
	nrows = excel_table.nrows; # 行数
	#ncols = excel_table.ncols; # 列数
	row_0 = excel_table.row_values(0);
	ncols = len([i for i in row_0 if i != ""]); # 列数
	table_name = js_name;
	config_map_str = "";
	json_str = "\"%s\":{\n"%table_name;
	b_add_json = False;
	config_map_str = "let %s = {};\n" % table_name;
	config_map_item_str = ""; # 一行的字符串
	head_list = parseExcelHead(excel_table);
	col = 0;
	b_first = True
	for r in range(2, nrows):
		value = excel_table.cell(r, col).value;
		head = head_list[0];
		head_var_type = None;
		if head.find("@") >= 0:
			head_var_type = head[head.find("@") + 1:];
		if value == "":
			continue
		height = getRowHight(excel_table, r, col);
		#print "20150703 %d %d %d %d %s\n"%(r,col,ncols,height,config_map_item_str);
		config_map_item_str = parseExcelTable(excel_table, head_list, r, col, ncols, height, False);
		config_map_str += "%s[%s] = {%s};\n" % (table_name, parseValueToStr(value, head_var_type), config_map_item_str);
		json_key = parseValueToStr(value, head_var_type);
		
		if b_first == False:
			json_str += ",\n"
		if head_var_type == "string" or head_var_type == "str" or type(value) == type("Hannibal"):
			json_str += "\t\t\"%s\":{%s}"%(value, config_map_item_str)
		else:
			json_str += "\t\t\"%s\":{%s}"%(json_key, config_map_item_str)
		b_first = False;
	# print("output_str*****************")
	# print(output_str);
	####
	json_str += "}";
	config_map_str = "let %s = null;\n" % table_name;
	config_map_str += "export function %s_init(config_obj:Object):void{\n"%table_name;
	config_map_str += "\t%s = config_obj[\"%s\"];\n}\n"%(table_name,table_name);
	init_func_str = "\t%s_init(config_obj);\n"%table_name;
	####
	config_map_item = None;
	exec "config_map_item = {%s}" % config_map_item_str
	var_name_list = config_map_item.keys();
	return config_map_str, var_name_list,json_str,init_func_str

# 解析excel表的表头
# @param {excel_table} excel_table
# @params {list} 包含表头的列表 struct:[string,]
def parseExcelHead(excel_table):
	nrows = excel_table.nrows; # 行数
	ncols = excel_table.ncols; # 列数
	head_list = [];
	for i in range(ncols):
		value = excel_table.cell(1, i).value;
		head_list.append(value);
	# print(head_list);
	return head_list

# 解析表的一块区域
# @param {} excel_table
# @param {list} head_list 表头
# @param {int} start_r 起始行
# @param {int} start_c 起始列
# @param {int} width 宽
# @param {int} height 高
# @param {boolean} is_list 需要解析的区域是否为一个列表格式
# @returns {string}
def parseExcelTable(excel_table, head_list, start_r, start_c, width, height, is_list):
	#print("parseExcelTable([%s], %s, %s, %s, %s)\n" % (head_list, start_r, start_c, width, height));
	output_str= "";
	pass_cell = 0; # 需要跳过的被子函数解析过的列数
	b_list_firstitem = True;
	for r in range(start_r, start_r + height):
		if excel_table.cell(r, start_c).value == "":
			continue
		line_str = "";
		if is_list:
			if b_list_firstitem:
				line_str += "{";
				b_list_firstitem = False;
			else:
				line_str += ",{";
		for c in range(start_c, start_c + width):
			if pass_cell > 0: # 跳过被子函数解析的列
				pass_cell -= 1;
				continue
			head = head_list[c - start_c];
			#print(head);
			if head.find("[") >= 0:	# template: jiangli_list#3[jianli_id
				new_width = int(head[head.find("#") + 1: head.find("[")]);
				if new_width and new_width > 0:
					#print "parseExcelTable getRowHight %d %d"%(r,start_c)
					new_height = getRowHight(excel_table, r, start_c);
					#print("r:[%d] start_c:[%d] new_width:[%s] new_height:[%s]" % (r,start_c,new_width, new_height));
					pass_cell = new_width - 1; # 这些列需要跳过,避免重复解析
					new_head_list = head_list[c - start_c + 1: c - start_c + 1 + new_width];
					new_head_list.insert(0, head[head.find("[") + 1:]);	# 添加"jianli_id"回列表
					str = parseExcelTable(excel_table, new_head_list, r, c, new_width, new_height, True);
					line_str += "\"%s\":[%s]," % (head[:head.find("#")], str);
			else:
				var_str = "";
				var_name = head;
				var_type = "";
				if head.find("@") >= 0:
					var_name = head[:head.find("@")];
					var_type = head[head.find("@") + 1:];
				var_value = excel_table.cell(r, c).value;
				if var_value == "":
					continue
				#print("var_value:[%s] var_type:[%s]" % (var_value, var_type));
				var_str = parseValueToStr(var_value, var_type);
				line_str += "\"%s\":%s," % (var_name, var_str);
		if is_list:
			if len(line_str) > 1:
				line_str = line_str[0:len(line_str)-1];
			line_str += "}";
		else:
			if len(line_str) > 0:
				line_str = line_str[0:len(line_str)-1];
		output_str += line_str;
	return output_str

# 获取行高
# @param {} excel_table
# @param {int} start_r 起始行
# @param {int} col 指定列
def getRowHight(excel_table, start_r, col):
	# print("getRowHight(%s, %s)" % (start_r, col));
	nrows = excel_table.nrows; # 行数
	ncols = excel_table.ncols; # 列数
	#print "getRowHight %d %d %d %d"%(start_r,col,nrows,ncols)
	height = 1;
	for r in range(start_r + 1, nrows):
		#print "value %d %d %s"%(r,col,excel_table.cell(r, col).value)
		if excel_table.cell(r, col).value != None and excel_table.cell(r, col).value != "":
			break
		else:
			height += 1;
	#print("height=%s" % height);
	return height
	
# 将一个值转化为输出格式 字符串类型添加双引号
# @param {string} var_value 需要输出的值
# @param {string} var_type 值得类型  可以为自定义类型
# @params {string} 输出值
def parseValueToStr(var_value, var_type = None):
	str = "";
	#print("[%s] [%s] [%s]" % (var_value, type(var_value), var_type));
	if var_type == "int":
		if var_value == None:
			var_value = 0;
		else:
			try:
				var_value = int(var_value);
			except:
				var_value = 0;
		str = "%d" % var_value;
	elif var_type == "float":
		str = "%f" % float(var_value);
	elif var_type == "string":
		str = "\"%s\"" % var_value;
	elif var_type == "str":
		str = "\"%s\"" % var_value;
	elif var_type == "bool":
		if var_value in ["", "False", "false", "否", "0"]:
			var_value = "False";
		else:
			var_value = "True";
		str = "%s" % var_value;
	elif var_type == "shifou":
		str = "%s" % (var_value == "是");
	elif var_type == "classes_id": # 职业id
		_tmp = [i for i in CLASSES_ID_AND_NAME_MAP.keys() if CLASSES_ID_AND_NAME_MAP[i].decode("gbk") == var_value]; # 因为var_value是unicode 所以要先把前面的decode
		if _tmp:
			str = "%s" % _tmp[0];
		else:
			raise "错误的职业数据配置:[%s]" % var_value
	else: # var_type为None或者未定义
		if type(var_value) == type(1) or type(var_value) == type(1.0):
			str = "%s" % var_value;
		elif type(var_value) == type("Hannibal"):
			str = "\"%s\"" % var_value;
		else:
			str = "\"%s\"" % var_value;
	return str

# 将js内容输出到文件中
# @param {string} data js内容字符串
# @param {string} fileName 文件名
def outputToFile(class_name, config_map_name, config_map_str, var_name_str, fileName):
	template_file = open("template.ts", "r");
	template_str = template_file.read();
	template_file.close();
	template_str = template_str.replace("${class_name}", class_name.capitalize());
	template_str = template_str.replace("${config_map_name}", config_map_name);
	template_str = template_str.replace("${config_map}", config_map_str);
	template_str = template_str.replace("${var_name}", var_name_str);
	f = open(fileName, "w");
	f.write(template_str.encode("utf8"));
	#f.write(template_str.encode("GBK"));
	f.close();
	# print("out_put_file_name<%s>" % fileName);
	return
# 将js内容输出到文件中
# @param {string} data js内容字符串
# @param {string} fileName 文件名
def outputJSONAndInitFile(json_str, json_path, init_str, init_path):
	f = open(json_path, "w");
	f.write(json_str.encode("utf8"));
	f.close();
	f = open(init_path, "w");
	f.write(init_str.encode("utf8"));
	f.close();
	return
# 解析所有config.xlsx中的文件并生成相应的js文件
# @param {string} 存放excel文件的目录
# @param {string} 输出js文件的目录
def parseAllExcelFiles(excel_file_dir, output_file_dir,json_dir):
	print("excel_file_dir:[%s]" % excel_file_dir);

	print("output_file_dir:[%s]" % output_file_dir);
	file_list = parseConfigFile("config.xls");
	output_json = "{\n";
	init_func = "module config{\n";
	init_func += "export function config_init(config_obj:Object):void{\n";
	b_first = True;
	for file_name, sheet_name, js_name in file_list:
		#print "20150529 %s %s %s"%(file_name,sheet_name,js_name)
		print("file_name<%s> sheet_name<%s>, js_name<%s>" % (file_name, sheet_name, js_name));
		
		if excel_file_dir == None or len(excel_file_dir) <= 0:
			file_path = file_name
		else:
			file_path = "%s/%s" % (excel_file_dir, file_name);
			
		config_map_name = "%s_map" % js_name;
		config_map_str, var_name_list,json_str,initfunc_str = parseExcelFile(file_path, sheet_name, config_map_name);
		var_name_str = "\n";
		if b_first == False:
			output_json += ",\n";
		output_json += json_str;
		b_first = False;
		init_func += initfunc_str;
		for i in var_name_list:
			var_name_str += "\t\tthis.%s = config.get(\"%s\");\n" % (i, i);
		outputToFile(js_name, config_map_name, config_map_str, var_name_str, "%s/%s.ts" % (output_file_dir, js_name));
	output_json += "}\n";
	init_func += "}\n";
	init_func += "}\n";
	init_file_path = "%s/config_init.ts"%(output_file_dir);
	json_path = "config.json";
	if json_dir != None and len(json_dir) > 0:
		json_path = "%s/config.json"%json_dir
	outputJSONAndInitFile(output_json,json_path,init_func,init_file_path);
	return


if __name__ == "__main__":
	import sys
	print sys.getdefaultencoding();
	xls_path = None;
	jsPath = None
	print(sys.argv)
	# print sys.getdefaultencoding()
	#global cur_dir
	py_file = sys.argv[0]
	output_dir = sys.argv[1]
	json_dir = "";
	if len(sys.argv) > 2:
		json_dir = sys.argv[2]
	print "json_dir:"+json_dir
	parseAllExcelFiles("table", output_dir,json_dir);
