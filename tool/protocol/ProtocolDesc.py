# -*- coding: utf-8 -*-

#protocol_desc start

Protocol_desc = {
	'chat_msg':[['id', 'int32', ''],['channel', 'int8', ''],['content', 'string16', ''],],
	'item':[['id', 'int32', ''],['shape', 'int16', ''],['name', 'string8', ''],['icon', 'string16', ''],['desc', 'string32', ''],],
	'itemlist':[['max', 'int8', ''],['data', 'list8', 'item'],['min', 'int8', ''],],
	'mail':[['id', 'int32', ''],['content', 'string32', ''],],
	'maillist':[['data', 'list16', 'mail'],],
	'bigmaillist':[['data', 'list32', 'mail'],],
	'c2s_login':[['account', 'string8', ''],['pwd', 'string8', ''],['localkey', 'string16', ''],['bpassager', 'int8', ''],],
	's2c_rolelist_info':[['id', 'int32', ''],['shape', 'int16', ''],['class', 'int8', ''],['lv', 'int16', ''],['name', 'string8', ''],],
	's2c_rolelist':[['rolelist', 'list8', 's2c_rolelist_info'],],
	'c2s_createrole':[['shape', 'int16', ''],['class', 'int8', ''],['name', 'string8', ''],],
	'c2s_choserole':[['roleid', 'int32', ''],],
	's2c_enterscene':[['sceneid', 'int32', ''],['x', 'int16', ''],['y', 'int16', ''],],
	'c2s_role_move':[['x', 'int16', ''],['y', 'int16', ''],],
	's2c_role_move':[['id', 'int32', ''],['x', 'int8', ''],['y', 'int8', ''],],
	's2c_role_enter':[['id', 'int32', ''],['x', 'int8', ''],['y', 'int8', ''],['shape', 'int16', ''],['class', 'int8', ''],['lv', 'int16', ''],['name', 'string8', ''],],
	's2c_role_out':[['id', 'int32', ''],],
	's2c_common_rsp':[['cmdid', 'int8', ''],['result', 'int8', ''],],
	's2c_localkey':[['key', 'string16', ''],],
}


#protocol_desc end
