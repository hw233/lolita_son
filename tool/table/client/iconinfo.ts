/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let iconinfo_map = null;
export function iconinfo_map_init(config_obj:Object):void{
	iconinfo_map = config_obj["iconinfo_map"];
}


export class Iconinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = iconinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Iconinfo(key){
		if(Iconinfo.m_static_map.hasOwnProperty(key) == false){
			Iconinfo.m_static_map[key] = Iconinfo.create_Iconinfo(key);
		}
		return Iconinfo.m_static_map[key];	
	}
	public static create_Iconinfo(key){
		if(iconinfo_map.hasOwnProperty(key)){
			return new Iconinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return iconinfo_map;
	}
}
}