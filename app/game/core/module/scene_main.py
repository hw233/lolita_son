# coding: utf-8
# 
import app.base.game_module_mgr
from app.game.core.game_event_def import *
from app.protocol.ProtocolDesc import *
import app.protocol.netutil as netutil
from twisted.python import log
import app.util.helper as helper
import app.util.lang_config as lang_config
import app.scene.memmode as memmode
from firefly.server.globalobject import GlobalObject
import app.game.core.game_module_def as game_module_def
import app.game.core.module.scene.scenemgr as scenemgr
import app.config.sceneinfo as sceneinfo
import app.config.mapinfo as mapinfo
class scene_main(app.base.game_module_mgr.game_module):
	def __init__(self):
		super(scene_main,self).__init__();
		self.character_map = {};
		self.characterinfo_map = {};
		self.smgr = scenemgr.scenemgr();
		for k,v in sceneinfo.sceneinfo_map.items():
			scene_id = v["scene_id"];
			resid = v["res"]
			name = v["name"];
			minfo = mapinfo.create_Mapinfo(resid);
			w = 2560;
			h = 2560;
			if minfo:
				w = minfo.w;
				h = minfo.h;
			self.smgr.init_scene(k,w,h,resid,name);
		self.smgr.parent = self;
		return
	
	def start(self):
		super(scene_main,self).start();
		self.register_event(EVENT_LOGIN,self.on_login);
		self.register_event(EVENT_LOGOUT,self.on_logout);
		self.register_net_event(C2S_MAP_MOVE,self.on_move)
		self.register_event(EVENT_SEND2CLIENT,self._send2client);
		self.register_event(EVENT_SEND2CLIENTBYCID,self._send2clientbycid)
		return
	def _getdidbycid(self,cId):
		if self.character_map.has_key(cId):
			return self.character_map[cId];
		return
	def _send2clientbycid(self,ud):
		cmd = ud[0]
		cId = ud[1];
		dId = self._getdidbycid(cId);
		if dId == None:
			log.err("_send2clientbycid err:%s %s"%(cId,ud));
			return
		data = ud[2];
		buf = netutil.s2c_data2bufbycmd(cmd,data);
		GlobalObject().remote['gate'].callRemote("pushObject",cmd,buf, [dId])
		return
	def _send2client(self,ud):
		cmd = ud[0]
		dId = ud[1];
		data = ud[2];
		buf = netutil.s2c_data2bufbycmd(cmd,data);
		GlobalObject().remote['gate'].callRemote("pushObject",cmd,buf, [dId])
		return
	
	def _float_msg(self,dId,msg):
		c_data = {};
		c_data['msg'] = msg;
		self.fire_event(EVENT_SEND2CLIENT,[S2C_NOTIFY_FLOAT,dId,c_data]);
		return;
	def _is_cId_valid(self,cId):#其实就是角色是否在线的判定
		return self.character_map.has_key(cId);
	def on_login(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		self.character_map[cId] = dId;
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('scene_main on_login fatal err %d'%(cId));
			return
		c_info = c_data.get('data');
		sid = c_info['town'];
		px = c_info['position_x'];
		py = c_info['position_y'];
		shape = c_info['figure'];
		name = c_info['nickname'];
		scene_obj = self.smgr.get_scene_obj(sid);
		if not scene_obj:
			log.msg('scene_main on_login have not this scene %d,%d'%(cId,sid));
			return
		self.characterinfo_map[cId] = {'sid':sid,'x':px,'y':py,'shape':shape,'name':name};
		self.smgr.enter(cId,sid,px,py);

		data = {};
		data['id'] = cId;
		data['scid'] = sid;
		data['scsid'] = sid;
		data['resid'] = scene_obj.resid;
		data['x'] = px;
		data['y'] = py;
		data['scname'] = scene_obj.name;
		buf = netutil.s2c_data2bufbycmd(S2C_HERO_ENTERSCENE,data);
		GlobalObject().remote['gate'].callRemote("pushObject",S2C_HERO_ENTERSCENE,buf, [dId])
		return
	def on_logout(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		del self.character_map[cId];

		self.smgr.quit(cId);

		return
	def on_move(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		x = data["x"];
		y = data["y"];
		step = data["step"];

		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('scene_main on_move fatal err %d'%(cId));
			return
		for i in step:
			print "on_move %d"%(i);
			if i == 1:
				y += 1;
			elif i == 2:
				y += 1;
				x -= 1;
			elif i == 3:
				x -= 1;
			elif i == 4:
				x -= 1;
				y -= 1;
			elif i == 5:
				y -= 1;
			elif i == 6:
				x += 1;
				y -= 1;
			elif i == 7:
				x += 1;
			elif i == 8:
				x += 1;
				y += 1;
		dx = x;
		dy = y;
		log.msg('scene_main on_move %d %d %d'%(cId,dx,dy));
		c_data.update_multi({"position_x":x,"position_y":y});
		self.characterinfo_map[cId]["x"] = dx;
		self.characterinfo_map[cId]["y"] = dy;

		self.smgr.move(cId,dx,dy);
		
		return
	def notify_region_2_c(self,cid,c_list):
		print "notify_region_2_c %s %s"%(cid,c_list);
		dId = self._getdidbycid(cid);
		if dId == None:
			print "notify_region_2_c fatal error %d"%(cid);
			return
		for i in c_list:
			print "notify_region_2_c %d"%(i);
			if self.characterinfo_map.has_key(i):
				cinfo = self.characterinfo_map[i];
				shape = cinfo["shape"];
				x = cinfo["x"];
				y = cinfo["y"];
				name = cinfo["name"];
				desc = "";
				data = {};
				data['id'] = i;
				data['shape'] = shape;
				data['name'] = name;
				data['desc'] = desc;
				data['x'] = x;
				data['y'] = y;
				buf = netutil.s2c_data2bufbycmd(S2C_MAP_ADDPLAYER,data);
				GlobalObject().remote['gate'].callRemote("pushObject",S2C_MAP_ADDPLAYER,buf, [dId])
		return
	def notify_enter_new_region(self,cid,x,y,rw,rh):
		print "notify_enter_new_region %s,%s,%s,%s,%s"%(cid,x,y,rw,rh);
		dId = self._getdidbycid(cid);
		if dId == None:
			print "notify_region_2_c fatal error %d"%(cid);
			return
		data = {};
		data['rw'] = rw;
		data['rh'] = rh;
		data['x'] = x;
		data['y'] = y;
		buf = netutil.s2c_data2bufbycmd(S2C_MAP_REGIONCHANGE,data);
		GlobalObject().remote['gate'].callRemote("pushObject",S2C_MAP_REGIONCHANGE,buf, [dId])
		
		return
	def notify_enter_list(self,notify_list,cid,x,y):
		print "notify_enter_list %s,%s,%s,%s"%(notify_list,cid,x,y);
		if len(notify_list) <= 0:
			return;
		dId_list = [];
		for i in notify_list:
			dId = self._getdidbycid(cid);
			if dId != None:
				dId_list.append(dId);
		cinfo = self.characterinfo_map[cid];
		shape = cinfo["shape"];
		x = cinfo["x"];
		y = cinfo["y"];
		name = cinfo["name"];
		print "%s %s %s %s %s"%(shape,x,y,name,type(name)); 
		data = {};
		data['id'] = cid;
		data['shape'] = shape;
		data['x'] = x;
		data['y'] = y;
		data['desc'] = "";
		data['name'] = name;
		buf = netutil.s2c_data2bufbycmd(S2C_MAP_ADDPLAYER,data);
		GlobalObject().remote['gate'].callRemote("pushObject",S2C_MAP_ADDPLAYER,buf, dId_list)
		return
	def notify_quit_list(self,notify_list,cid):
		print "notify_quit_list %s,%s"%(notify_list,cid);
		if len(notify_list) <= 0:
			return;
		dId_list = [];
		for i in notify_list:
			dId = self._getdidbycid(cid);
			if dId != None:
				dId_list.append(dId);
		data = {};
		data['id'] = cid;
		buf = netutil.s2c_data2bufbycmd(S2C_MAP_DEL,data);
		GlobalObject().remote['gate'].callRemote("pushObject",S2C_MAP_DEL,buf, dId_list)
		return
	def notify_move_list(self,notify_list,cid,x,y):
		print "notify_move_list %s,%s,%s,%s"%(notify_list,cid,x,y);
		if len(notify_list) <= 0:
			return;
		dId_list = [];
		for i in notify_list:
			dId = self._getdidbycid(cid);
			if dId != None:
				dId_list.append(dId);
		
		data = {};
		data['id'] = cid;
		data['x'] = x;
		data['y'] = y;
		data['dx'] = x;
		data['dy'] = y;
		buf = netutil.s2c_data2bufbycmd(S2C_MAP_TRACK,data);
		GlobalObject().remote['gate'].callRemote("pushObject",S2C_MAP_TRACK,buf, dId_list)
		return

	def dispose(self):
		super(game_main,self).dispose();
		return