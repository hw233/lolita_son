/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let winginfo_map = null;
export function winginfo_map_init(config_obj:Object):void{
	winginfo_map = config_obj["winginfo_map"];
}


export class Winginfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = winginfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Winginfo(key){
		if(Winginfo.m_static_map.hasOwnProperty(key) == false){
			Winginfo.m_static_map[key] = Winginfo.create_Winginfo(key);
		}
		return Winginfo.m_static_map[key];	
	}
	public static create_Winginfo(key){
		if(winginfo_map.hasOwnProperty(key)){
			return new Winginfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return winginfo_map;
	}
}
}