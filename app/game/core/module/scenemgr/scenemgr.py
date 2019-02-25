# -*- coding: utf-8 -*-

import random

REGION_HNUM = 6;#10 actually diameter
REGION_VNUM = 4;#8 actually diameter

BLOCK_W = 256;
BLOCK_H = 256;
GRID_W = 32;
GRID_H = 32;
class sceneblock:
	def __init__(self,sx,sy,h_idx,v_idx):
		self.x = sx;
		self.y = sy;
		self.h_num = h_idx;
		self.v_num = v_idx;
		self.player_list = [];#cid
		return

	def enter(self,cid):
		if cid not in self.player_list:
			self.player_list.append(cid);
		return

	def quit(self,cid):
		if cid in self.player_list:
			self.player_list.remove(cid);
		return

	def dispose(self):
		return
class sceneobj:
	def __init__(self,sid,w,h):
		self.w = w;
		self.h = h;
		self.sid = sid;
		self.block_list = [];
		global BLOCK_W;
		global BLOCK_H;
		global REGION_HNUM;
		global REGION_VNUM;

		self.b_w = BLOCK_W;
		self.b_h = BLOCK_H;

		self.region_hcount = REGION_HNUM;
		self.region_vcount = REGION_VNUM;

		self.region_left = self.region_hcount/2;
		self.region_right = self.region_hcount/2;
		self.region_top = self.region_vcount/2;
		self.region_bottom = self.region_vcount/2;

		self.HCOUNT = self.w/self.b_w;
		self.VCOUNT = self.h/self.b_h;
		if self.HCOUNT <= 0:
			self.HCOUNT = 1;
		if self.VCOUNT <= 0:
			self.VCOUNT = 1;
		for i in xrange(0,self.VCOUNT):
			v_list = [];
			for j in xrange(self.HCOUNT):
				v_list.append(sceneblock(j*BLOCK_W,i*BLOCK_H,j,i));
			self.block_list.append(v_list);

		self.player_map = {};#cid 2 block
		return
	def print_data(self):
		print "sceneobj %s %s %s print_data start\n"%(self.sid,self.VCOUNT,self.HCOUNT);
		for i in xrange(0,self.VCOUNT):
			for j in xrange(self.HCOUNT):
				b = self.block_list[i][j];
				print "%s,%s:%s,%s,%s,%s,%s\n"%(i,j,b.x,b.y,b.h_num,b.v_num,b.player_list);
		print "sceneobj %s print_data end\n"%(self.sid);
		return
	def _gen_notify_list(self,h_num,v_num):
		ret = [];
		left = h_num - self.region_left;
		right = h_num + self.region_right;
		top = v_num - self.region_top;
		bottom = v_num + self.region_bottom;
		if left < 0:
			left = 0;
		if top < 0:
			top = 0;
		if right >= self.HCOUNT:
			right = self.HCOUNT - 1;
		if bottom >= self.VCOUNT:
			bottom = self.VCOUNT - 1;
		#print "_gen_notify_list %s %s %s %s %s %s %s %s"%(h_num,v_num,left,right,top,bottom,self.HCOUNT,self.VCOUNT);
		for x in xrange(left,right+1):
			for y in xrange(top,bottom+1):
				tb = self.block_list[y][x];
				ret = ret + tb.player_list;
		return ret
	def _gen_move_rect(self,src_h,src_v,dst_h,dst_v):
		if src_h == dst_h and src_v == dst_v:
			print "_gen_move_rect 1";
			return [[src_h,src_v]],[],[]#move,enter,quit
		
		left = src_h - self.region_left;
		right = src_h + self.region_right;
		top = src_v - self.region_top;
		bottom = src_v + self.region_bottom;
		if left < 0:
			left = 0;
		if top < 0:
			top = 0;
		if right >= self.HCOUNT:
			right = self.HCOUNT - 1;
		if bottom >= self.VCOUNT:
			bottom = self.VCOUNT - 1;

		dleft = dst_h - self.region_left;
		dright = dst_h + self.region_right;
		dtop = dst_v - self.region_top;
		dbottom = dst_v + self.region_bottom;
		if dleft < 0:
			dleft = 0;
		if dtop < 0:
			dtop = 0;
		if dright >= self.HCOUNT:
			dright = self.HCOUNT - 1;
		if dbottom >= self.VCOUNT:
			dbottom = self.VCOUNT - 1;
		#check if src rect is not covered by dst rect;
		#4 0 4 1
		dist_h = abs(src_h - dst_h);
		dist_v = abs(src_v - dst_v);
		if dist_h > (self.region_hcount+1) or dist_v > (self.region_vcount+1):
			quit_list = [];
			for i in xrange(left,right+1):
				for j in xrange(top,bottom+1):#
					quit_list.append([i,j])
			enter_list = [];
			for i in xrange(dleft,dright+1):
				for j in xrange(dtop,dbottom+1):#
					enter_list.append([i,j])
			move_list = [];
			print "_gen_move_rect 2 %s %s %s %s %s %s %s %s"%(src_h,src_v,dst_h,dst_v,dist_h,dist_v,self.region_hcount,self.region_vcount);
			return move_list,enter_list,quit_list
		if src_h == dst_h:#vertical
			if src_v < dst_v:#down
				quit_list = [];
				for i in xrange(left,right+1):
					for j in xrange(top,dtop):#exclude dtop
						quit_list.append([i,j])
				enter_list = [];
				for i in xrange(left,right+1):
					for j in xrange(bottom+1,dbottom+1):#exclude bottom
						enter_list.append([i,j])
				move_list = [];
				for i in xrange(left,right+1):
					for j in xrange(dtop,bottom+1):
						move_list.append([i,j]);
				print "_gen_move_rect 3";
				return move_list,enter_list,quit_list;
			else:#up
				quit_list = [];
				for i in xrange(left,right+1):
					for j in xrange(dbottom+1,bottom+1):#exclude dbottom
						quit_list.append([i,j])
				enter_list = [];
				for i in xrange(left,right+1):
					for j in xrange(dtop,top):#exclude top
						enter_list.append([i,j])
				move_list = [];
				for i in xrange(left,right+1):
					for j in xrange(top,dbottom+1):
						move_list.append([i,j]);
				print "_gen_move_rect 4";
				return move_list,enter_list,quit_list;
		if src_v == dst_v:#horizontal
			if src_h < dst_h:#right
				quit_list = [];
				for i in xrange(top,bottom+1):
					for j in xrange(left,dleft):#exclude dleft
						quit_list.append([j,i])
				enter_list = [];
				for i in xrange(top,bottom+1):
					for j in xrange(right+1,dright+1):#exclude right
						enter_list.append([j,i])
				move_list = [];
				for i in xrange(top,bottom+1):
					for j in xrange(dleft,right+1):
						move_list.append([j,i]);
				print "_gen_move_rect 5";
				return move_list,enter_list,quit_list;
			else:#left
				quit_list = [];
				for i in xrange(top,bottom+1):
					for j in xrange(dright+1,right+1):#exclude dright
						quit_list.append([j,i])
				enter_list = [];
				for i in xrange(top,bottom+1):
					for j in xrange(dleft,left):#exclude left
						enter_list.append([j,i])
				move_list = [];
				for i in xrange(top,bottom+1):
					for j in xrange(left,dright+1):
						move_list.append([j,i]);
				print "_gen_move_rect 6";
				return move_list,enter_list,quit_list;
		ov_l = 0;
		ov_r = 0;
		ov_t = 0;
		ov_b = 0;
		if left < dleft:
			ov_l = dleft;
			ov_r = right;
		else:
			ov_l = left;
			ov_r = dright;
		if top < dtop:
			ov_t = dtop;
			ov_b = bottom;
		else:
			ov_t = top;
			ov_b = dbottom;
		quit_list = [];
		
		for i in xrange(left,right+1):
			for j in xrange(top,bottom+1):#
				if not (i >= ov_l and i <= ov_r and j >= ov_t and j <= ov_b):
					quit_list.append([i,j])
		enter_list = [];
		for i in xrange(dleft,dright+1):
			for j in xrange(dtop,dbottom+1):#
				if not (i >= ov_l and i <= ov_r and j >= ov_t and j <= ov_b):
					enter_list.append([i,j])
		move_list = [];
		for i in xrange(ov_l,ov_r+1):
			for j in xrange(ov_t,ov_b+1):#
				move_list.append([i,j]);
		print "_gen_move_rect 7";
		return move_list,enter_list,quit_list
	def enter(self,cid,x,y):
		if self.player_map.has_key(cid):
			return;
		h_idx = x/self.b_w;
		v_idx = y/self.b_h;
		if h_idx < 0:
			h_idx = 0;
		if h_idx >= self.HCOUNT:
			h_idx = self.HCOUNT - 1;
		if v_idx < 0:
			v_idx = 0;
		if v_idx >= self.VCOUNT:
			v_idx = self.VCOUNT - 1;
		ret = self._gen_notify_list(h_idx,v_idx);
		tb = self.block_list[v_idx][h_idx];
		tb.enter(cid);
		self.player_map[cid] = tb;
		return ret
	
	def quit(self,cid):
		if self.player_map.has_key(cid):
			b = self.player_map[cid];
			h_num = b.h_num;
			v_num = b.v_num;
			b.quit(cid);
			ret = self._gen_notify_list(h_num,v_num);
			del self.player_map[cid];
			return ret;
		return
	def move(self,cid,x,y):
		if not self.player_map.has_key(cid):
			return;
		h_idx = x/self.b_w;
		v_idx = y/self.b_h;
		if h_idx < 0:
			h_idx = 0;
		if h_idx >= self.HCOUNT:
			h_idx = self.HCOUNT - 1;
		if v_idx < 0:
			v_idx = 0;
		if v_idx >= self.VCOUNT:
			v_idx = self.VCOUNT - 1;
		print "move %s %s %s %s"%(x,y,h_idx,v_idx);
		tb = self.player_map[cid];
		tb.quit(cid);
		sh_idx = tb.h_num;
		sv_idx = tb.v_num;
		m_list,e_list,q_list = self._gen_move_rect(sh_idx,sv_idx,h_idx,v_idx);
		m_ret = [];
		for i in m_list:
			tb = self.block_list[i[1]][i[0]];
			m_ret = m_ret + tb.player_list;
		e_ret = [];
		for i in e_list:
			tb = self.block_list[i[1]][i[0]];
			e_ret = e_ret + tb.player_list;
		q_ret = [];
		for i in q_list:
			tb = self.block_list[i[1]][i[0]];
			q_ret = q_ret + tb.player_list;
		
		tb = self.block_list[v_idx][h_idx];
		tb.enter(cid);
		self.player_map[cid] = tb;
		return m_ret,e_ret,q_ret;
	def dispose(self):
		return

class scenemgr:
	def __init__(self):
		self._scene_map = {};
		self._cid_2_scene = {};
		global GRID_W
		global GRID_H
		global BLOCK_W
		global BLOCK_H
		self.b_w = BLOCK_W;
		self.b_h = BLOCK_H;
		self.grid_w = GRID_W;
		self.grid_h = GRID_H;
		return
	def dispose(self):
		return
	def init_scene(self,scene_id):
		import app.config.mapinfo as mapinfo
		#import mapinfo
		mapinfo = mapinfo.create_Mapinfo(scene_id);
		w = 2560;
		h = 2560;
		if mapinfo:
			w = mapinfo.w;
			h = mapinfo.h;
		self._scene_map[scene_id] = sceneobj(scene_id,w,h);
		return
	def notify_enter_list(self,notify_list,cid,x,y):
		print "notify_enter_list %s,%s,%s,%s,%s,%s,%s,%s"%(notify_list,cid,x,y,x*self.grid_w,y*self.grid_h,x*self.grid_w/self.b_w,y*self.grid_h/self.b_h);
		return
	def notify_quit_list(self,notify_list,cid):
		print "notify_quit_list %s,%s"%(notify_list,cid);
		return
	def notify_move_list(self,notify_list,cid,x,y):
		print "notify_move_list %s,%s,%s,%s,%s,%s,%s,%s"%(notify_list,cid,x,y,x*self.grid_w,y*self.grid_h,x*self.grid_w/self.b_w,y*self.grid_h/self.b_h);
		return
	def print_data(self,sid):
		sobj = self._scene_map[sid];
		sobj.print_data();
		return
	def enter(self,cid,scene_id,x,y):
		gx = x*self.grid_w;
		gy = y*self.grid_h;
		if not self._scene_map.has_key(scene_id):
			self.init_scene(scene_id);
		if self._cid_2_scene.has_key(cid):
			old_sid = self._cid_2_scene[cid];
			if old_sid == scene_id:
				self.jump(cid,gx,gy);
				return;
			else:
				quit_ret = self.quit(cid);
				self.notify_quit_list(quit_ret,cid,x,y);

		self._cid_2_scene[cid] = scene_id;
		enter_ret = self._scene_map[scene_id].enter(cid,gx,gy);
		self.notify_enter_list(enter_ret,cid,x,y);
		return
	def quit(self,cid):
		if self._cid_2_scene.has_key(cid):
			sid = self._cid_2_scene[cid];
			if not self._scene_map.has_key(sid):
				return;
			quit_ret = self._scene_map[sid].quit(cid);
			self.notify_quit_list(quit_ret,cid);
			del self._cid_2_scene[cid];
		return
	def move(self,cid,x,y):
		gx = x*self.grid_w;
		gy = y*self.grid_h;
		if self._cid_2_scene.has_key(cid):
			sid = self._cid_2_scene[cid];
			if not self._scene_map.has_key(sid):
				return;
			m_ret,e_ret,q_ret = self._scene_map[sid].move(cid,gx,gy);
			self.notify_quit_list(q_ret,cid);
			self.notify_enter_list(e_ret,cid,x,y);
			self.notify_move_list(m_ret,cid,x,y);
		return
	def jump(self,cid,new_sid,x,y):
		gx = x*self.grid_w;
		gy = y*self.grid_h;
		if self._cid_2_scene.has_key(cid):
			sid = self._cid_2_scene[cid];
			if self._scene_map.has_key(sid):
				q_ret = self._scene_map[sid].quit(cid);
				self.notify_quit_list(q_ret,cid);
			if self._scene_map.has_key(new_sid):
				self._cid_2_scene[cid] = new_sid;
				enter_ret = self._scene_map[new_sid].enter(cid,gx,gy);
				self.notify_enter_list(enter_ret,cid,x,y);
		return
	
smgr_ins = scenemgr();
def test_func():
	global smgr_ins
	smgr_ins.enter(1,1001,10,10);
	for i in xrange(20,30):
		x = random.randint(0,40);
		y = random.randint(0,40);
		smgr_ins.enter(i,1001,x,y);
	return
