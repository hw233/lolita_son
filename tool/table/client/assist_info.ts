/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let assist_info_map = null;
export function assist_info_map_init(config_obj:Object):void{
	assist_info_map = config_obj["assist_info_map"];
}


export class Assist_info extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = assist_info_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Assist_info(key){
		if(Assist_info.m_static_map.hasOwnProperty(key) == false){
			Assist_info.m_static_map[key] = Assist_info.create_Assist_info(key);
		}
		return Assist_info.m_static_map[key];	
	}
	public static create_Assist_info(key){
		if(assist_info_map.hasOwnProperty(key)){
			return new Assist_info(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return assist_info_map;
	}
}
}