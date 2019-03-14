/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let combat_skip_cfg_map = null;
export function combat_skip_cfg_map_init(config_obj:Object):void{
	combat_skip_cfg_map = config_obj["combat_skip_cfg_map"];
}


export class Combat_skip_cfg extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = combat_skip_cfg_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Combat_skip_cfg(key){
		if(Combat_skip_cfg.m_static_map.hasOwnProperty(key) == false){
			Combat_skip_cfg.m_static_map[key] = Combat_skip_cfg.create_Combat_skip_cfg(key);
		}
		return Combat_skip_cfg.m_static_map[key];	
	}
	public static create_Combat_skip_cfg(key){
		if(combat_skip_cfg_map.hasOwnProperty(key)){
			return new Combat_skip_cfg(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return combat_skip_cfg_map;
	}
}
}