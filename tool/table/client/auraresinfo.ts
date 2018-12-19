/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let auraresinfo_map = null;
export function auraresinfo_map_init(config_obj:Object):void{
	auraresinfo_map = config_obj["auraresinfo_map"];
}


export class Auraresinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = auraresinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Auraresinfo(key){
		if(Auraresinfo.m_static_map.hasOwnProperty(key) == false){
			Auraresinfo.m_static_map[key] = Auraresinfo.create_Auraresinfo(key);
		}
		return Auraresinfo.m_static_map[key];	
	}
	public static create_Auraresinfo(key){
		if(auraresinfo_map.hasOwnProperty(key)){
			return new Auraresinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return auraresinfo_map;
	}
}
}