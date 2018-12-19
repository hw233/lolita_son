# coding: utf-8
from singleton import Singleton
import event_dispatcher
class game_module(event_dispatcher.event_receiver):
	def __init__(self):
		event_dispatcher.event_receiver.__init__(self);
		self._efunc_map = {};
		self._cmdfunc_map = {};
		self._broadcmdfunc_map = {};
		return
	def start(self):
		return
	def register_event(self,e,efunc):
		if self._efunc_map.has_key(e) and self._efunc_map[e] != None:
			event_dispatcher.event_dispatcher().unregister_event(e,self._efunc_map[e]);
		event_dispatcher.event_dispatcher().register_event(e,efunc);
		self._efunc_map[e] = efunc;
		return
	def unregister_event(self,e,efunc):
		event_dispatcher.event_dispatcher().unregister_event(e,efunc);
		del self._efunc_map[e];
		return
	def unregister_allevent(self):
		for k,v in self._efunc_map.items():
			event_dispatcher.event_dispatcher().unregister_event(k,v);
		self._efunc_map = {};
		for c,v in self._cmdfunc_map.items():
			event_dispatcher.event_dispatcher().unregister_net_event(c,v);
		self._cmdfunc_map = {};

		for c,v in self._broadcmdfunc_map.items():
			event_dispatcher.event_dispatcher().unregister_broadnet_event(c,v);
		self._broadcmdfunc_map = {};

		return;
	def register_net_event(self,cmd,cfunc):
		if self._cmdfunc_map.has_key(cmd) and self._cmdfunc_map[cmd] != None:
			event_dispatcher.event_dispatcher().unregister_net_event(cmd,self._cmdfunc_map[cmd]);
		event_dispatcher.event_dispatcher().register_net_event(cmd,cfunc);
		self._cmdfunc_map[cmd] = cfunc;
		return
	def unregister_net_event(self,cmd,cfunc):
		event_dispatcher.event_dispatcher().unregister_net_event(cmd,cfunc);
		del self._cmdfunc_map[cmd];
		return
	def register_broadnet_event(self,cmd,cfunc):
		if self._broadcmdfunc_map.has_key(cmd) and self._broadcmdfunc_map[cmd] != None:
			event_dispatcher.event_dispatcher().unregister_broadnet_event(cmd,self._broadcmdfunc_map[cmd]);
		event_dispatcher.event_dispatcher().register_broadnet_event(cmd,cfunc);
		self._broadcmdfunc_map[cmd] = cfunc;
		return
	def unregister_broadnet_event(self,cmd,cfunc):
		event_dispatcher.event_dispatcher().unregister_broadnet_event(cmd,cfunc);
		del self._broadcmdfunc_map[cmd];
		return
	def fire_event(self,e,user_data = None):
		event_dispatcher.event_dispatcher().fire_event(e,user_data);
		return;
	def get_module(self,module_name):
		return game_module_mgr().get_module(module_name);
	def dispose(self):
		event_dispatcher.event_dispatcher().unregister_allevent(self);
		return

class game_module_mgr:
	__metaclass__ = Singleton
	def __init__(self):
		self._module_cls_map = {};
		self._module_ins_map = {};
		return;
	def register_module(self,module_name,module_cls):
		self._module_cls_map[module_name] = module_cls;
		return
	def get_module(self,module_name):
		if not self._module_ins_map.has_key(module_name):
			if not self._module_cls_map.has_key(module_name):
				return None;
			ins = self._module_cls_map[module_name]();
			self._module_ins_map[module_name] = ins;
		return self._module_ins_map[module_name];
	def dispose(self):
		self._module_cls_map = {};
		for k,v in self._module_ins_map.items():
			v.dispose();
		self._module_ins_map = {};
		return
