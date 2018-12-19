/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let aniinfo_map = null;
export function aniinfo_map_init(config_obj:Object):void{
	aniinfo_map = config_obj["aniinfo_map"];
}


export class Aniinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = aniinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Aniinfo(key){
		if(Aniinfo.m_static_map.hasOwnProperty(key) == false){
			Aniinfo.m_static_map[key] = Aniinfo.create_Aniinfo(key);
		}
		return Aniinfo.m_static_map[key];	
	}
	public static create_Aniinfo(key){
		if(aniinfo_map.hasOwnProperty(key)){
			return new Aniinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return aniinfo_map;
	}
}
}