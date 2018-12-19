/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let skininfo_map = null;
export function skininfo_map_init(config_obj:Object):void{
	skininfo_map = config_obj["skininfo_map"];
}


export class Skininfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = skininfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Skininfo(key){
		if(Skininfo.m_static_map.hasOwnProperty(key) == false){
			Skininfo.m_static_map[key] = Skininfo.create_Skininfo(key);
		}
		return Skininfo.m_static_map[key];	
	}
	public static create_Skininfo(key){
		if(skininfo_map.hasOwnProperty(key)){
			return new Skininfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return skininfo_map;
	}
}
}