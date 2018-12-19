# coding: utf-8
from singleton import Singleton
class event_receiver(object):
	def __init__(self):
		self._callback = {};
		return
	def register_event(self,e,func):
		self._callback[e] = func;
		return;
	def unregister_event(self,e):
		del self._callback[e];
		return;
	def unregister_allevent(self):
		self._callback = {};
		return;
	def dispose(self):
		self.unregister_all_event();
		return;
	def on_event(self,e,user_data):
		efunc = self._callback[e];
		if e:
			efunc(user_data);
		return;
class event_dispatcher:
	__metaclass__ = Singleton
	def __init__(self):
		self._recv_map = {};
		return
	def register_event(self,e,efunc):
		if self._recv_map.has_key(e) == False:
			self._recv_map[e] = [];
		r_list = self._recv_map[e];
		if efunc not in r_list:
			r_list.append(efunc);
		return
	def unregister_event(self,e,efunc):
		if self._recv_map.has_key(e):
			r_list = self._recv_map[e];
			if r_list and efunc in r_list:
				r_list.remove(efunc);
		return;
	def _gen_net_cmd_e(self,cmd):
		return "net_cmd_%d_%x"%(cmd,cmd);
	def _gen_broadnet_cmd_e(self,cmd):
		return "broadnet_cmd_%d_%x"%(cmd,cmd);
	def register_net_event(self,cmd,cfunc):
		self.register_event(self._gen_net_cmd_e(cmd),cfunc);
		return
	def unregister_net_event(self,cmd,cfunc):
		self.unregister_event(self._gen_net_cmd_e(cmd),cfunc);
		return
	def register_broadnet_event(self,cmd,cfunc):
		self.register_event(self._gen_broadnet_cmd_e(cmd),cfunc);
		return
	def unregister_broadnet_event(self,cmd,cfunc):
		self.unregister_event(self._gen_broadnet_cmd_e(cmd),cfunc);
		return
	def dispatch_event(self,e,user_data):
		if self._recv_map.has_key(e):
			for v in self._recv_map[e]:
				if v:
					v(user_data);
		return;
	def fire_event(self,e,user_data = None):
		self.dispatch_event(e,user_data);
		return;
	def fire_net_event(self,cmd,user_data = None):
		self.dispatch_event(self._gen_net_cmd_e(cmd),user_data);
		return;
	def fire_broadnet_event(self,cmd,user_data = None):
		self.dispatch_event(self._gen_broadnet_cmd_e(cmd),user_data);
		return;