# -*- coding: utf-8 -*-

#protocol_desc start

Protocol_desc = {
	'version':[['major ', 'int16', ''],['minor', 'int16', ''],['patch', 'int16', ''],],
	'ptyperow':[['tid', 'int16', ''],['name', 'string8', ''],['subtid', 'int16', ''],],
	'protocoltype':[['tid', 'int16', ''],['name', 'string8', ''],['fileds', 'list8', 'ptyperow'],],
	'pdescrow':[['name', 'string8', ''],['tid', 'int16', ''],['subtid', 'int16', ''],],
	'protocoldesc':[['cmd', 'uint16', ''],['fileds', 'list8', 'pdescrow'],],
	'role':[['rid', 'int32', ''],['shape', 'int16', ''],['cls', 'int8', ''],['grade', 'int16', ''],['desc', 'byte8', ''],['flag', 'int8', ''],['newtm', 'int32', ''],['theme', 'int8', ''],['name', 'string8', ''],['offline', 'int32', ''],['logintm', 'int32', ''],['orgsrvid', 'int32', ''],],
	'roleinfo':[['rid', 'int32', ''],['name', 'string8', ''],['shape', 'int16', ''],['desc', 'byte8', ''],['cls', 'int8', ''],['grade', 'int16', ''],['vip', 'int8', ''],['battle', 'int32', ''],],
	'prop8':[['idx', 'uint8', ''],['value', 'int8', ''],],
	'prop16':[['idx', 'uint8', ''],['value', 'int16', ''],],
	'prop32':[['idx', 'uint8', ''],['value', 'int32', ''],],
	'propstr':[['idx', 'uint8', ''],['value', 'string8', ''],],
	'propbyte':[['idx', 'uint8', ''],['value', 'byte8', ''],],
	'battleratio':[['idx', 'uint8', ''],['ratio', 'uint16', ''],],
	'reputedata':[['rtype', 'uint8', ''],['value', 'int32', ''],['total', 'int32', ''],],
	'npctalkopt':[['idx', 'int32', ''],['name', 'string8', ''],],
	'item':[['id', 'int32', ''],['sid', 'int32', ''],['amount', 'int32', ''],['pos', 'int16', ''],['key', 'int8', ''],['quality', 'int8', ''],['extra', 'int8', ''],['battle', 'int32', ''],],
	'reward':[['rtype', 'int8', ''],['value', 'int32', ''],],
	'rewarditem':[['sid', 'int32', ''],['amount', 'int16', ''],['quality', 'int8', ''],],
	'warpropinfo':[['props16', 'list8', 'prop16'],['props32', 'list8', 'prop32'],['battle', 'int32', ''],],
	'equipgrowinfo':[['pos', 'int8', ''],['lvl', 'int16', ''],['props', 'list8', 'warpropinfo'],['nextprops', 'list8', 'warpropinfo'],],
	'skill':[['sid', 'uint16', ''],['lv', 'uint8', ''],],
	'skilllearncost':[['sid', 'uint16', ''],['cost', 'int32', ''],],
	'summon':[['sid', 'int16', ''],['shape', 'int16', ''],['quality', 'int8', ''],['name', 'string8', ''],['grade', 'int16', ''],['exp', 'int16', ''],['props', 'warpropinfo', ''],['skills', 'list8', 'skill'],['battle', 'int32', ''],],
	'summonapt':[['sid', 'int16', ''],['lvl', 'int16', ''],['exp', 'int16', ''],['props', 'warpropinfo', ''],['aptsklv', 'uint8', ''],],
	'mailsimple':[['id', 'int32', ''],['status', 'int8', ''],['title', 'string8', ''],['sendtime', 'int32', ''],['hasattach', 'int8', ''],],
	'mail':[['id', 'int32', ''],['status', 'int8', ''],['rewards', 'list8', 'reward'],['items', 'list8', 'rewarditem'],['content', 'string16', ''],],
	'teammemberinfo':[['pid', 'int32', ''],['name', 'string8', ''],['shape', 'int16', ''],['desc', 'byte8', ''],['cls', 'int8', ''],['grade', 'int16', ''],['vip', 'int8', ''],['battle', 'int32', ''],],
	'teaminfo':[['teamid', 'int32', ''],['leader', 'teammemberinfo', ''],['memcnt', 'int8', ''],],
	'partner':[['sid', 'int16', ''],['shape', 'int16', ''],['quality', 'int8', ''],['name', 'string8', ''],['grade', 'int16', ''],['exp', 'int16', ''],['props', 'warpropinfo', ''],['skills', 'list8', 'skill'],['battle', 'int32', ''],],
	's2c_rolelist_info':[['id', 'int32', ''],['shape', 'int16', ''],['class', 'int8', ''],['lv', 'int16', ''],['name', 'string8', ''],],
	'yaoguai':[['id', 'int32', ''],['index', 'int16', ''],['star', 'int8', ''],],
	'qmbossdesc':[['bossid', 'int16', ''],['status', 'int8', ''],['fighter', 'int8', ''],['hprate', 'int8', ''],['rebirthtime', 'int32', ''],],
	'qmbossdmg':[['id', 'int32', ''],['name', 'string8', ''],['damage', 'int32', ''],],
	'qmbosskill':[['second', 'int32', ''],['name', 'string8', ''],['battlevalue', 'int32', ''],],
	'rank_data':[['data16', 'list8', 'int16'],['data32', 'list8', 'int32'],['datastr', 'list8', 'string8'],],
	'shopitem':[['index', 'int32', ''],['exchanged', 'int32', ''],['validcond', 'int8', ''],],
	'scpasssecrwd':[['sceneid', 'int16', ''],['sectionid', 'int16', ''],],
	'mfbinfo':[['fubenid', 'int16', ''],['fighted', 'int8', ''],['saodang', 'int8', ''],],
	'arena_worrior':[['ranking', 'int16', ''],['name', 'string8', ''],['battle', 'int32', ''],['shape', 'int16', ''],['desc', 'byte8', ''],],
	'arena_record':[['win', 'int8', ''],['rise', 'int16', ''],['challenge', 'int8', ''],['name', 'string8', ''],['second', 'int32', ''],],
	'simplerole':[['roleid', 'int32', ''],['shape', 'int16', ''],['name', 'string8', ''],],
	'friendinfo':[['roleid', 'int32', ''],['name', 'string8', ''],['shape', 'int16', ''],['grade', 'int16', ''],['vip', 'int8', ''],['online', 'int8', ''],['battlevalue', 'int32', ''],['gangid', 'int32', ''],['gangname', 'string8', ''],],
	'wildbossstatus':[['bossid', 'int16', ''],['status', 'int8', ''],['nexttime', 'int32', ''],],
	'treasurestar':[['treasureid', 'int16', ''],['star', 'int8', ''],],
	'treasurerwd':[['mapid', 'int16', ''],['stars', 'int8', ''],],
	'tsumeko_progress':[['kalpa', 'int8', ''],['puzzle', 'int8', ''],],
	'tsumeko_puzzle':[['puzzle', 'int8', ''],['roomid', 'int32', ''],['challenge', 'int8', ''],['box', 'int8', ''],],
	'tsumeko_record':[['names', 'list8', 'string8'],['bout', 'int16', ''],['time', 'int32', ''],],
	'traveltime':[['eid', 'int16', ''],['cnt', 'int8', ''],],
	'gangmember':[['id', 'int32', ''],['name', 'string8', ''],['shape', 'int16', ''],['battlevalue', 'int32', ''],['position', 'int8', ''],['gangcontribution', 'int32', ''],['lastoffline', 'int32', ''],],
	'gangrequest':[['id', 'int32', ''],['name', 'string8', ''],['shape', 'int16', ''],['battlevalue', 'int32', ''],],
	'gangdesc':[['id', 'int32', ''],['name', 'string8', ''],['level', 'int8', ''],['member', 'int8', ''],['leadername', 'string8', ''],['autopass', 'int32', ''],],
	'ganginclog':[['time', 'int32', ''],['name', 'string8', ''],['inctype', 'int8', ''],],
	'escort_car':[['rid', 'uint32', ''],['sid', 'uint32', ''],['start', 'uint32', ''],['end', 'uint32', ''],['left', 'uint32', ''],['quality', 'uint8', ''],['battle', 'int32', ''],['name', 'string8', ''],['gang', 'string8', ''],['shape', 'int16', ''],],
	'escort_records':[['id', 'uint16', ''],['attack', 'int8', ''],['rid', 'uint32', ''],['sid', 'uint32', ''],['name', 'string8', ''],['quality', 'uint8', ''],['time', 'uint32', ''],['result', 'int8', ''],['state', 'int8', ''],],
	'ganglog':[['logtype', 'int8', ''],['time', 'int32', ''],['args', 'list8', 'string8'],],
	'gangskillinfo':[['pos', 'int16', ''],['lvl', 'int16', ''],['prop', 'warpropinfo', ''],],
	'gang_boss_damage':[['name', 'string8', ''],['grade', 'int16', ''],['rate', 'int8', ''],],
	'best_player':[['rid', 'uint32', ''],['name', 'string8', ''],['srvid', 'int32', ''],['state', 'int8', ''],],
	'best_winner':[['rid', 'uint32', ''],['name', 'string8', ''],['srvid', 'int32', ''],['win', 'uint8', ''],['lose', 'uint8', ''],['battle', 'int32', ''],['lvl', 'uint16', ''],['shape', 'int16', ''],['desc', 'byte8', ''],],
	'best_fighter':[['rid', 'uint32', ''],['name', 'string8', ''],['srvid', 'int32', ''],['battle', 'int32', ''],['lvl', 'uint16', ''],['shape', 'int16', ''],['desc', 'byte8', ''],],
	'goldtreasure_rare':[['sid', 'int32', ''],['amount', 'int16', ''],['name', 'string8', ''],],
	'growuprwd':[['rewardtype', 'int8', ''],['rewarded', 'list8', 'int8'],],
	'gcexchange':[['index', 'int8', ''],['exchangeid', 'int8', ''],['times', 'int8', ''],],
	'gangflower':[['index', 'int8', ''],['roleid', 'int32', ''],],
	'hegemony_defender':[['rid', 'int32', ''],['name', 'string8', ''],['shape', 'int16', ''],['desc', 'byte8', ''],['cls', 'int8', ''],['grade', 'int16', ''],['battle', 'int32', ''],['hp', 'int16', ''],],
	'hegemony_mine_info':[['mid', 'int16', ''],['camp', 'int8', ''],['name', 'string8', ''],['shape', 'int16', ''],['num', 'int16', ''],],
	'hegemony_role':[['rid', 'uint32', ''],['camp', 'int8', ''],['x', 'int16', ''],['y', 'int16', ''],['name', 'string8', ''],['shape', 'int16', ''],['team', 'int8', ''],],
	'qmjjcount':[['index', 'int8', ''],['count', 'int16', ''],],
	'hegemony_score':[['camp', 'int8', ''],['score', 'int32', ''],],
	'discsgoods':[['goodsid', 'int8', ''],['bought', 'int16', ''],],
	'groupbuyrw':[['cnt', 'int16', ''],['gold', 'int16', ''],],
	'cookbattle_result':[['result_idx', 'int8', ''],['result', 'int8', ''],['subject_style', 'int8', ''],['recipe', 'int8', ''],['rival_style', 'int8', ''],['rival_level', 'int8', ''],],
	'cookbattle_recipe':[['style', 'int8', ''],['recipe', 'int8', ''],['amount', 'int16', ''],],
	'wulin_rank_info':[['rid', 'uint32', ''],['score', 'uint32', ''],['name', 'string8', ''],['srvid', 'int32', ''],],
	'C2S_WEBSOCKET_HELLO':[['msg', 'string16', ''],],
	'S2C_WEBSOCKET_HELLO':[['msg', 'string16', ''],],
	'S2C_MERGE_PACKET':[['packets', 'list8', 'byte8'],],
	'C2S_LOGIN_ASYN_TIME':[['time', 'uint32', ''],['sign', 'string16', ''],],
	'C2S_LOGIN':[['clientver', 'version', ''],['scriptver', 'version', ''],['productver', 'version', ''],['account', 'string8', ''],['pwd', 'string8', ''],['platform', 'int8', ''],['client_type', 'int32', ''],['device', 'string8', ''],['ret_session', 'int8', ''],['token', 'string16', ''],['hwinfo', 'string8', ''],['idfa', 'string8', ''],],
	'C2S_LOGIN_SESSION':[['pid', 'uint32', ''],['session', 'byte16', ''],],
	'C2S_LOGIN_GM':[['account', 'string8', ''],['pwd', 'string8', ''],],
	'C2S_LOGIN_SELECTROLE':[['rid', 'int32', ''],],
	'C2S_LOGIN_CLIENTREADY':[],
	'C2S_LOGIN_CREATEROLE':[['cls', 'int8', ''],['shape', 'int16', ''],['name', 'string8', ''],['rolenum', 'int8', ''],],
	'C2S_LOGIN_DELETEROLE':[['rid', 'int32', ''],],
	'C2S_LOGIN_RESTOREROLE':[['rid', 'int32', ''],],
	'C2S_ACCOUNT_GUEST':[],
	'S2C_SYSTEM_VERSION':[['testtime', 'int8', ''],['clientver', 'version', ''],['scriptver', 'version', ''],['productver', 'version', ''],],
	'S2C_ASYNTIME':[['time', 'uint32', ''],['srvtime', 'uint32', ''],],
	'S2C_LOGIN':[['errcode', 'int8', ''],['errmsg', 'string16', ''],],
	'S2C_LOGIN_OK':[['flag', 'int8', ''],],
	'S2C_LOGIN_ROLEINFO':[['roles', 'list8', 'role'],],
	'S2C_LOGIN_SELECTROLE':[],
	'S2C_LOGIN_DELETEROLE':[['rid', 'int32', ''],],
	'S2C_LOGIN_RELOGIN':[],
	'S2C_LOGIN_SESSION':[['err', 'uint8', ''],],
	'S2C_LOGIN_UPDATESESSION':[['session', 'string16', ''],],
	'S2C_ACCOUNT_GUEST':[['account', 'string8', ''],['pwd', 'string8', ''],],
	'S2C_OPENTIME':[['opentime', 'uint32', ''],],
	'S2C_SERVER_INFO':[['srvid', 'int16', ''],['srvname', 'string8', ''],['opentime', 'uint32', ''],],
	'S2C_ACCOUNT_INFO':[['aid', 'int32', ''],['qudao', 'string8', ''],],
	'S2C_PROTOCOL_DESC':[['ptypes', 'list8', 'ptyperow'],['cusptypes', 'list16', 'protocoltype'],['c2sprotocols', 'list16', 'protocoldesc'],['s2cprotocols', 'list16', 'protocoldesc'],],
	'S2C_CLIENT_COMMAND':[['msg', 'string16', ''],],
	'C2S_CLIENT_SETTING':[['setting', 'byte8', ''],],
	'S2C_CLIENT_SETTING':[['setting', 'byte8', ''],],
	'C2S_SERVER_SETTING':[['autosmelt', 'int8', ''],],
	'S2C_SERVER_SETTING':[['autosmelt', 'int8', ''],],
	'C2S_ROLE_RENAME':[['name', 'string8', ''],],
	'C2S_CHANGE_SIGN':[['sign', 'string8', ''],],
	'S2C_ROLE_FREERENAME':[['freecnt', 'int8', ''],],
	'S2C_SERVER_ONDAY':[['hour', 'int8', ''],],
	'C2S_MAP_MOVE':[['x', 'int16', ''],['y', 'int16', ''],['step', 'list8', 'uint8'],],
	'C2S_MAP_PICK':[['id', 'int32', ''],],
	'S2C_MAP_TRACK':[['id', 'int32', ''],['x', 'int16', ''],['y', 'int16', ''],['dx', 'int8', ''],['dy', 'int8', ''],],
	'S2C_MAP_DEL':[['id', 'byte', ''],],
	'S2C_MAP_ADDPLAYER':[['id', 'int32', ''],['shape', 'int16', ''],['x', 'int16', ''],['y', 'int16', ''],['desc', 'byte8', ''],['name', 'string8', ''],],
	'S2C_MAP_ADDNPC':[['id', 'int32', ''],['sid', 'int32', ''],['shape', 'int16', ''],['x', 'int16', ''],['y', 'int16', ''],['dir', 'int8', ''],['desc', 'byte8', ''],['name', 'string8', ''],],
	'S2C_MAP_ADDGOODS':[['id', 'int32', ''],['shape', 'int16', ''],['x', 'int16', ''],['y', 'int16', ''],['owners', 'list8', 'int32'],['name', 'string8', ''],],
	'S2C_MAP_ADDSUMMON':[['pid', 'int32', ''],['id', 'int16', ''],['shape', 'int16', ''],['quality', 'int8', ''],['desc', 'byte8', ''],['name', 'string8', ''],],
	'S2C_MAP_DELSUMMON':[['pid', 'int32', ''],['id', 'int16', ''],],
	'S2C_MAP_ADDPARTNER':[['pid', 'int32', ''],['id', 'int16', ''],['shape', 'int16', ''],['quality', 'int8', ''],['desc', 'byte8', ''],['name', 'string8', ''],],
	'S2C_MAP_DELPARTNER':[['pid', 'int32', ''],['id', 'int16', ''],],
	'S2C_MAP_ROLESTATE':[['id', 'int32', ''],['state', 'int8', ''],],
	'S2C_MAP_CHANGESHAPE':[['id', 'int32', ''],['shape', 'int16', ''],['desc', 'byte8', ''],],
	'S2C_MAP_CHANGETITLE':[['id', 'int32', ''],['name', 'string8', ''],],
	'S2C_MAP_PLAYANI':[['id', 'int32', ''],['ani', 'int16', ''],['x', 'int16', ''],['y', 'int16', ''],],
	'S2C_MAP_ROLETITLE':[['id', 'int32', ''],['tid', 'int8', ''],],
	'S2C_HANGMAP_INFO':[['scsid', 'int16', ''],],
	'C2S_NPC_LOOK':[['id', 'int32', ''],],
	'C2S_NPC_RESPOND':[['idx', 'int32', ''],],
	'S2C_NPC_CHAT':[['id', 'int32', ''],['icon', 'int16', ''],['name', 'string8', ''],['text', 'string16', ''],['textid', 'int32', ''],['opts', 'list8', 'npctalkopt'],],
	'C2S_ROLE_INFO':[],
	'S2C_ROLE_INFO':[['lv', 'int16', ''],['shape', 'int16', ''],['gold', 'int32', ''],['exp', 'int32', ''],['goldspd', 'int32', ''],['expspd', 'int32', ''],['stamina', 'int32', ''],['tm', 'int32', ''],],
	'C2S_PET_INFO':[],
	'S2C_PET_INFO':[['lv', 'int16', ''],['shape', 'int16', ''],['exp', 'int32', ''],],
	'C2S_SKILL_INFO':[['id', 'int8', ''],],
	'S2C_SKILL_INFO':[['id', 'int8', ''],['skill1lv', 'int16', ''],['skill2lv', 'int16', ''],],
	'C2S_PARTNER_INFO':[],
	'S2C_PARTNER_INFO':[['lv', 'int16', ''],['shape', 'int16', ''],['exp', 'int32', ''],],
	'C2S_CLICK':[['x', 'int16', ''],['y', 'int16', ''],],
	'S2C_CLICK':[['x', 'int16', ''],['y', 'int16', ''],['gold', 'int32', ''],['exp', 'int32', ''],],
	'C2S_LV_UP':[['id', 'int8', ''],],
	'C2S_SKILL_LVUP':[['id', 'int8', ''],['skillid', 'int8', ''],],
	'C2S_SPEC_SKILLINFO':[],
	'S2C_SPEC_SKILLINFO':[['skill1lv', 'int16', ''],['skill1tm', 'int32', ''],['skill1cd', 'int32', ''],['skill2lv', 'int16', ''],['skill2tm', 'int32', ''],['skill2cd', 'int32', ''],['skill3lv', 'int16', ''],['skill3tm', 'int32', ''],['skill3cd', 'int32', ''],['skill4lv', 'int16', ''],['skill4tm', 'int32', ''],['skill4cd', 'int32', ''],],
	'C2S_SPEC_SKILL_USE':[['id', 'int8', ''],],
	'C2S_SPEC_SKILL_LVUP':[['id', 'int8', ''],],
	'C2S_SKILL_CLICK':[['x', 'int16', ''],['y', 'int16', ''],],
	'C2S_ITEM_GETLIST':[],
	'C2S_ITEM_USE':[['id', 'int32', ''],['amount', 'int32', ''],],
	'C2S_ITEM_MOVE':[['id', 'int32', ''],['dstpos', 'int16', ''],],
	'C2S_ITEM_BAGEXPAND':[['size', 'int16', ''],],
	'S2C_ITEM_LIST':[['items', 'list16', 'item'],],
	'S2C_ITEM_ADD':[['item', 'item', ''],],
	'S2C_ITEM_UPDATE':[['id', 'int32', ''],['amount', 'int32', ''],['pos', 'int16', ''],['key', 'int8', ''],],
	'S2C_ITEM_DEL':[['id', 'int32', ''],],
	'S2C_ITEM_BAGCOUNT':[['size', 'int16', ''],['goldsize', 'int16', ''],],
	'C2S_ITEM_BUY':[['id', 'int32', ''],],
	'C2S_CHAT':[['ch', 'int8', ''],['msg', 'string16', ''],],
	'C2S_CHAT_GM':[['msg', 'string16', ''],],
	'S2C_CHAT':[['ch', 'int8', ''],['srvid', 'uint16', ''],['pid', 'int32', ''],['shape', 'int16', ''],['vip', 'int8', ''],['name', 'string8', ''],['msg', 'string16', ''],],
	'S2C_CHAT_SYSTEM':[['ch', 'int8', ''],['msg', 'string16', ''],],
	'S2C_NOTIFY_MESSAGE':[['boxtype', 'uint8', ''],['msg', 'string8', ''],['opt', 'string8', ''],['timeout', 'uint16', ''],],
	'S2C_NOTIFY_FLOAT':[['msg', 'string16', ''],],
	'S2C_NOTIFY_FLYMESSAGE':[['style', 'int8', ''],['msg', 'string16', ''],],
	'S2C_NOTIFY_FLYHINT':[['warid', 'int32', ''],['hint', 'uint8', ''],['sid', 'int32', ''],['num', 'int32', ''],['qua', 'int8', ''],],
	'S2C_NOTIFY_NOENOUGH':[['ctype', 'int8', ''],['sid', 'int32', ''],],
	'S2C_NOTIFY_REWARD':[['warid', 'int32', ''],['showtype', 'int8', ''],['rewards', 'list8', 'reward'],['items', 'list8', 'rewarditem'],],
	'S2C_NOTIFY_OFFLINEREWARD':[['exp', 'int32', ''],['money', 'int32', ''],['equip', 'int16', ''],['mcexp', 'int32', ''],['mcmoney', 'int32', ''],['mcequip', 'int16', ''],['smeltequip', 'int16', ''],['offtime', 'uint32', ''],],
	'C2S_HERO_LEVELUP':[],
	'S2C_HERO_PROP':[['props8', 'list8', 'prop8'],['props16', 'list8', 'prop16'],['props32', 'list8', 'prop32'],['propsstr', 'list8', 'propstr'],['propsbyte', 'list8', 'propbyte'],],
	'S2C_HERO_ENTERSCENE':[['id', 'int32', ''],['scid', 'int16', ''],['scsid', 'int16', ''],['resid', 'int16', ''],['scname', 'string8', ''],['x', 'int16', ''],['y', 'int16', ''],],
	'S2C_HERO_GOTO':[['x', 'int16', ''],['y', 'int16', ''],],
	'S2C_WAR_START':[['id', 'int32', ''],['type', 'int8', ''],['subtype', 'int8', ''],['lineup', 'int8', ''],['playmode', 'int8', ''],['skip', 'int8', ''],['maxbout', 'int8', ''],],
	'S2C_WAR_ADD':[['warid', 'int8', ''],['type', 'int8', ''],['owner', 'int8', ''],['status', 'int16', ''],['shape', 'int16', ''],['desc', 'byte8', ''],['grade', 'int16', ''],['classes', 'int8', ''],['name', 'string8', ''],['zoomlvl', 'int8', ''],],
	'S2C_WAR_LEAVE':[['warid', 'int8', ''],],
	'S2C_WAR_STATUS':[['warid', 'int8', ''],['hprate', 'int16', ''],],
	'S2C_WAR_NEXT':[['bout', 'int8', ''],],
	'S2C_WAR_TURN':[],
	'S2C_WAR_PREEND':[],
	'S2C_WAR_END':[['force', 'int8', ''],],
	'S2C_WAR_REPLY':[],
	'S2C_WAR_ATTACK_NORMAL':[['att', 'int8', ''],['vic', 'int8', ''],],
	'S2C_WAR_ATTACK_END':[],
	'S2C_WAR_PERFORM':[['att', 'int8', ''],['skillid', 'int16', ''],['lv', 'int8', ''],['round', 'int8', ''],['lsvic', 'list8', 'int8'],],
	'S2C_WAR_PERFORM_END':[],
	'S2C_WAR_PARTNER_ATTACK':[['partner', 'int8', ''],['vic', 'int8', ''],],
	'S2C_WAR_BACKATTACK':[['att', 'int8', ''],['skillid', 'int16', ''],['lv', 'int8', ''],['round', 'int8', ''],['lsvic', 'list8', 'int8'],],
	'S2C_WAR_BACKATTACK_END':[],
	'S2C_WAR_SHAKE':[['att', 'int8', ''],['vic', 'int8', ''],],
	'S2C_WAR_PROTECT':[['protector', 'int8', ''],['vic', 'int8', ''],],
	'S2C_WAR_ATTACK_STATUS':[['target', 'int8', ''],['status', 'int16', ''],['value', 'int32', ''],],
	'S2C_WAR_BUFF_ADD':[['warid', 'int8', ''],['bid', 'int16', ''],['overlay', 'int8', ''],['bout', 'int8', ''],['datas', 'list8', 'int32'],],
	'S2C_WAR_BUFF_DEL':[['warid', 'int8', ''],['bid', 'int16', ''],],
	'C2S_WAR_PLAYEND':[['id', 'int32', ''],],
	'S2C_WAR_DEFEAT':[['idx', 'int8', ''],],
}
C2S_WEBSOCKET_HELLO = 0x100;
S2C_WEBSOCKET_HELLO = 0x100;
S2C_MERGE_PACKET = 0x101;
C2S_LOGIN_ASYN_TIME = 0x111;
C2S_LOGIN = 0x113;
C2S_LOGIN_SESSION = 0x120;
C2S_LOGIN_GM = 0x121;
C2S_LOGIN_SELECTROLE = 0x114;
C2S_LOGIN_CLIENTREADY = 0x115;
C2S_LOGIN_CREATEROLE = 0x116;
C2S_LOGIN_DELETEROLE = 0x117;
C2S_LOGIN_RESTOREROLE = 0x118;
C2S_ACCOUNT_GUEST = 0x11a;
S2C_SYSTEM_VERSION = 0x110;
S2C_ASYNTIME = 0x111;
S2C_LOGIN = 0x112;
S2C_LOGIN_OK = 0x113;
S2C_LOGIN_ROLEINFO = 0x114;
S2C_LOGIN_SELECTROLE = 0x115;
S2C_LOGIN_DELETEROLE = 0x116;
S2C_LOGIN_RELOGIN = 0x117;
S2C_LOGIN_SESSION = 0x118;
S2C_LOGIN_UPDATESESSION = 0x119;
S2C_ACCOUNT_GUEST = 0x11a;
S2C_OPENTIME = 0x120;
S2C_SERVER_INFO = 0x128;
S2C_ACCOUNT_INFO = 0x129;
S2C_PROTOCOL_DESC = 0x121;
S2C_CLIENT_COMMAND = 0x122;
C2S_CLIENT_SETTING = 0x123;
S2C_CLIENT_SETTING = 0x123;
C2S_SERVER_SETTING = 0x124;
S2C_SERVER_SETTING = 0x124;
C2S_ROLE_RENAME = 0x125;
C2S_CHANGE_SIGN = 0x126;
S2C_ROLE_FREERENAME = 0x125;
S2C_SERVER_ONDAY = 0x127;
C2S_MAP_MOVE = 0x140;
C2S_MAP_PICK = 0x141;
S2C_MAP_TRACK = 0x42;
S2C_MAP_DEL = 0x43;
S2C_MAP_ADDPLAYER = 0x140;
S2C_MAP_ADDNPC = 0x141;
S2C_MAP_ADDGOODS = 0x142;
S2C_MAP_ADDSUMMON = 0x143;
S2C_MAP_DELSUMMON = 0x148;
S2C_MAP_ADDPARTNER = 0x149;
S2C_MAP_DELPARTNER = 0x14a;
S2C_MAP_ROLESTATE = 0x144;
S2C_MAP_CHANGESHAPE = 0x145;
S2C_MAP_CHANGETITLE = 0x146;
S2C_MAP_PLAYANI = 0x147;
S2C_MAP_ROLETITLE = 0x14b;
S2C_HANGMAP_INFO = 0x150;
C2S_NPC_LOOK = 0x160;
C2S_NPC_RESPOND = 0x161;
S2C_NPC_CHAT = 0x160;
C2S_ROLE_INFO = 0x400;
S2C_ROLE_INFO = 0x400;
C2S_PET_INFO = 0x430;
S2C_PET_INFO = 0x430;
C2S_SKILL_INFO = 0x432;
S2C_SKILL_INFO = 0x432;
C2S_PARTNER_INFO = 0x431;
S2C_PARTNER_INFO = 0x431;
C2S_CLICK = 0x433;
S2C_CLICK = 0x433;
C2S_LV_UP = 0x434;
C2S_SKILL_LVUP = 0x435;
C2S_SPEC_SKILLINFO = 0x436;
S2C_SPEC_SKILLINFO = 0x436;
C2S_SPEC_SKILL_USE = 0x437;
C2S_SPEC_SKILL_LVUP = 0x438;
C2S_SKILL_CLICK = 0x439;
C2S_ITEM_GETLIST = 0x401;
C2S_ITEM_USE = 0x180;
C2S_ITEM_MOVE = 0X402;
C2S_ITEM_BAGEXPAND = 0x181;
S2C_ITEM_LIST = 0x180;
S2C_ITEM_ADD = 0x181;
S2C_ITEM_UPDATE = 0x182;
S2C_ITEM_DEL = 0x183;
S2C_ITEM_BAGCOUNT = 0x184;
C2S_ITEM_BUY = 0x403;
C2S_CHAT = 0x1a0;
C2S_CHAT_GM = 0x1a1;
S2C_CHAT = 0x1a0;
S2C_CHAT_SYSTEM = 0x1a1;
S2C_NOTIFY_MESSAGE = 0x1b0;
S2C_NOTIFY_FLOAT = 0x1b1;
S2C_NOTIFY_FLYMESSAGE = 0x1b2;
S2C_NOTIFY_FLYHINT = 0x1b3;
S2C_NOTIFY_NOENOUGH = 0x1b4;
S2C_NOTIFY_REWARD = 0x1b5;
S2C_NOTIFY_OFFLINEREWARD = 0x1b6;
C2S_HERO_LEVELUP = 0x201;
S2C_HERO_PROP = 0x201;
S2C_HERO_ENTERSCENE = 0x202;
S2C_HERO_GOTO = 0x203;
S2C_WAR_START = 0x300;
S2C_WAR_ADD = 0x301;
S2C_WAR_LEAVE = 0x302;
S2C_WAR_STATUS = 0x303;
S2C_WAR_NEXT = 0x305;
S2C_WAR_TURN = 0x306;
S2C_WAR_PREEND = 0x30e;
S2C_WAR_END = 0x30f;
S2C_WAR_REPLY = 0x30d;
S2C_WAR_ATTACK_NORMAL = 0x311;
S2C_WAR_ATTACK_END = 0x312;
S2C_WAR_PERFORM = 0x313;
S2C_WAR_PERFORM_END = 0x314;
S2C_WAR_PARTNER_ATTACK = 0x315;
S2C_WAR_BACKATTACK = 0x316;
S2C_WAR_BACKATTACK_END = 0x317;
S2C_WAR_SHAKE = 0x318;
S2C_WAR_PROTECT = 0x319;
S2C_WAR_ATTACK_STATUS = 0x31a;
S2C_WAR_BUFF_ADD = 0x330;
S2C_WAR_BUFF_DEL = 0x331;
C2S_WAR_PLAYEND = 0x340;
S2C_WAR_DEFEAT = 0x340;


#protocol_desc end
