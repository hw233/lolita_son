/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let sys_open_activity_map = null;
export function sys_open_activity_map_init(config_obj:Object):void{
	sys_open_activity_map = config_obj["sys_open_activity_map"];
}


export class Sys_open_activity extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = sys_open_activity_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Sys_open_activity(key){
		if(Sys_open_activity.m_static_map.hasOwnProperty(key) == false){
			Sys_open_activity.m_static_map[key] = Sys_open_activity.create_Sys_open_activity(key);
		}
		return Sys_open_activity.m_static_map[key];	
	}
	public static create_Sys_open_activity(key){
		if(sys_open_activity_map.hasOwnProperty(key)){
			return new Sys_open_activity(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return sys_open_activity_map;
	}
}
}