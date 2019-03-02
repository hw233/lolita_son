/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let sceneinfo_map = null;
export function sceneinfo_map_init(config_obj:Object):void{
	sceneinfo_map = config_obj["sceneinfo_map"];
}


export class Sceneinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = sceneinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Sceneinfo(key){
		if(Sceneinfo.m_static_map.hasOwnProperty(key) == false){
			Sceneinfo.m_static_map[key] = Sceneinfo.create_Sceneinfo(key);
		}
		return Sceneinfo.m_static_map[key];	
	}
	public static create_Sceneinfo(key){
		if(sceneinfo_map.hasOwnProperty(key)){
			return new Sceneinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return sceneinfo_map;
	}
}
}