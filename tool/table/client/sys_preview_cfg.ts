/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let sys_preview_cfg_map = null;
export function sys_preview_cfg_map_init(config_obj:Object):void{
	sys_preview_cfg_map = config_obj["sys_preview_cfg_map"];
}


export class Sys_preview_cfg extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = sys_preview_cfg_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Sys_preview_cfg(key){
		if(Sys_preview_cfg.m_static_map.hasOwnProperty(key) == false){
			Sys_preview_cfg.m_static_map[key] = Sys_preview_cfg.create_Sys_preview_cfg(key);
		}
		return Sys_preview_cfg.m_static_map[key];	
	}
	public static create_Sys_preview_cfg(key){
		if(sys_preview_cfg_map.hasOwnProperty(key)){
			return new Sys_preview_cfg(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return sys_preview_cfg_map;
	}
}
}