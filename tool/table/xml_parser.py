#coding:utf8

import sys
import xlrd

cur_dir = "";


# @param {string} fileName xlsxfilename
# @param {string} sheetName sheet name
# @returns data
def openExcel(fileName, sheetName):
	data = xlrd.open_workbook(fileName)
	if sheetName:
		return data.sheet_by_name(sheetName.decode('GBK'))
	else:
		return data.sheets()[0]
	return

# @returns {map} 
def parseConfigFile(config_file):
	print("parseConfigFile(\"%s\")" % config_file);
	table = openExcel(config_file, "Sheet1");
	nrows = table.nrows;	# 
	ncols = table.ncols;	# 
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

# 
# @param {string} excelfilename
# @param {string} sheet_name 
# @param {string} js_name
# @returns {string} js content
def parseExcelFile(file_name, sheet_name, js_name):
	excel_table = openExcel(file_name, sheet_name);
	nrows = excel_table.nrows; # 
	#ncols = excel_table.ncols; # 
	row_0 = excel_table.row_values(0);
	ncols = len([i for i in row_0 if i != ""]); # 
	table_name = js_name;
	config_map_str = "";
	config_map_str += "%s = {};\n" % table_name;
	config_map_item_str = ""; # 
	head_list = parseExcelHead(excel_table);
	col = 0;
	for r in range(2, nrows):
		value = excel_table.cell(r, col).value;
		head = head_list[0];
		head_var_type = None;
		if head.find("@") >= 0:
			head_var_type = head[head.find("@") + 1:];
		if value == "":
			continue
		height = getRowHight(excel_table, r, col);
		#print "config_map_item_str : %s"%(type(config_map_item_str))
		#print "20150703 %d %d %d %d %s\n"%(r,col,ncols,height,config_map_item_str);
		config_map_item_str = parseExcelTable(excel_table, head_list, r, col, ncols, height, False);
		config_map_str += "%s[%s] = {%s};\n" % (table_name, parseValueToStr(value, head_var_type), config_map_item_str);
	# print("output_str*****************")
	# print(output_str);
	config_map_item = None;
	exec "config_map_item = {%s}" % config_map_item_str
	var_name_list = config_map_item.keys();
	return config_map_str, var_name_list


# @param {excel_table} excel_table
# @params {list} struct:[string,]
def parseExcelHead(excel_table):
	nrows = excel_table.nrows; # 
	ncols = excel_table.ncols; # 
	head_list = [];
	for i in range(ncols):
		value = excel_table.cell(1, i).value;
		head_list.append(value);
	# print(head_list);
	return head_list

# @param {} excel_table
# @param {list} head_list
# @param {int} start_r
# @param {int} start_c
# @param {int} width 
# @param {int} height 
# @param {boolean} is_list 
# @returns {string}
def parseExcelTable(excel_table, head_list, start_r, start_c, width, height, is_list):
	#print("parseExcelTable([%s], %s, %s, %s, %s)\n" % (head_list, start_r, start_c, width, height));
	output_str= "";
	#print "output_str %s"%(type(output_str))
	pass_cell = 0; # 
	for r in range(start_r, start_r + height):
		if excel_table.cell(r, start_c).value == "":
			continue
		if is_list:
			output_str += "{";
		for c in range(start_c, start_c + width):
			if pass_cell > 0: # 
				pass_cell -= 1;
				continue
			head = head_list[c - start_c];
			if isinstance(head, unicode):
				head = head.encode("GBK")
			#print(head);
			if head.find("[") >= 0:	# template: jiangli_list#3[jianli_id
				new_width = int(head[head.find("#") + 1: head.find("[")]);
				if new_width and new_width > 0:
					#print "parseExcelTable getRowHight %d %d"%(r,start_c)
					new_height = getRowHight(excel_table, r, start_c);
					#print("r:[%d] start_c:[%d] new_width:[%s] new_height:[%s]" % (r,start_c,new_width, new_height));
					pass_cell = new_width - 1; # 
					new_head_list = head_list[c - start_c + 1: c - start_c + 1 + new_width];
					new_head_list.insert(0, head[head.find("[") + 1:]);	# 
					str = parseExcelTable(excel_table, new_head_list, r, c, new_width, new_height, True);
					output_str += "\"%s\":[%s]," % (head[:head.find("#")], str);
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
				if isinstance(var_name, unicode):
					var_name = var_name.encode("GBK")
				output_str += "\"%s\":%s," % (var_name, var_str);
		if is_list:
			output_str += "},";
	return output_str

# 
# @param {} excel_table
# @param {int} start_r 
# @param {int} col 
def getRowHight(excel_table, start_r, col):
	# print("getRowHight(%s, %s)" % (start_r, col));
	nrows = excel_table.nrows; # 
	ncols = excel_table.ncols; # 
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
	
# 
# @param {string} var_value 
# @param {string} var_type 
# @params {string} 
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
		if isinstance(var_value, unicode):
			var_value = var_value.encode("GBK")
		str = "\"%s\"" % var_value;
	elif var_type == "str":
		if isinstance(var_value, unicode):
			var_value = var_value.encode("GBK")
		str = "\"%s\"" % var_value;
	elif var_type == "bool":
		if var_value in ["", "False", "false", "0"]:
			var_value = "False";
		else:
			var_value = "True";
		str = "%s" % var_value;
	else: # var_type为None或者未定义
		if isinstance(var_value, unicode):
			var_value = var_value.encode("GBK")
		if type(var_value) == type(1) or type(var_value) == type(1.0):
			str = "%s" % var_value;
		elif type(var_value) == type("Hannibal"):
			str = "\"%s\"" % var_value;
		else:
			str = "\"%s\"" % var_value;
	return str

# 
# @param {string} data 
# @param {string} fileName 
def outputToFile(class_name, config_map_name, config_map_str, var_name_str, fileName):
	template_file = open("template.py", "r");
	template_str = template_file.read();
	template_file.close();
	template_str = template_str.replace("${class_name}", class_name.capitalize());
	template_str = template_str.replace("${config_map_name}", config_map_name);
	template_str = template_str.replace("${config_map}", config_map_str);
	template_str = template_str.replace("${var_name}", var_name_str);
	f = open(fileName, "w");
	print "template_str type:%s"%(type(template_str))
	template_str = template_str.decode("GBK");
	print "template_str type1:%s"%(type(template_str));
	template_str = template_str.encode("utf8");
	print "template_str type2:%s,%s"%(type(template_str),fileName);
	f.write(template_str);
	#f.write(template_str.encode("utf8"));
	#f.write(template_str.encode("GBK"));
	f.close();
	# print("out_put_file_name<%s>" % fileName);
	return

#
# @param {string} 
# @param {string} 
def parseAllExcelFiles(excel_file_dir, output_file_dir):
	print("excel_file_dir:[%s]" % excel_file_dir);

	print("output_file_dir:[%s]" % output_file_dir);
	file_list = parseConfigFile("config.xls");
	for file_name, sheet_name, js_name in file_list:
		#print "20150529 %s %s %s"%(file_name,sheet_name,js_name)
		print("file_name<%s> sheet_name<%s>, js_name<%s>" % (file_name, sheet_name, js_name));
		file_path = "%s/%s" % (excel_file_dir, file_name);
		config_map_name = "%s_map" % js_name;
		config_map_str, var_name_list = parseExcelFile(file_path, sheet_name, config_map_name);
		var_name_str = "\n";
		for i in var_name_list:
			var_name_str += "\t\tself.%s = config.get(\"%s\");\n" % (i, i);
		outputToFile(js_name, config_map_name, config_map_str, var_name_str, "%s/%s.py" % (output_file_dir, js_name));
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
	cur_dir = py_file[:py_file.rfind("\\")]
	parseAllExcelFiles("table", "../../app/config");
