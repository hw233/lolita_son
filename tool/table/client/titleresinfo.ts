/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let titleresinfo_map = null;
export function titleresinfo_map_init(config_obj:Object):void{
	titleresinfo_map = config_obj["titleresinfo_map"];
}


export class Titleresinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = titleresinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Titleresinfo(key){
		if(Titleresinfo.m_static_map.hasOwnProperty(key) == false){
			Titleresinfo.m_static_map[key] = Titleresinfo.create_Titleresinfo(key);
		}
		return Titleresinfo.m_static_map[key];	
	}
	public static create_Titleresinfo(key){
		if(titleresinfo_map.hasOwnProperty(key)){
			return new Titleresinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return titleresinfo_map;
	}
}
}