/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let avatarinfo_map = null;
export function avatarinfo_map_init(config_obj:Object):void{
	avatarinfo_map = config_obj["avatarinfo_map"];
}


export class Avatarinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = avatarinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Avatarinfo(key){
		if(Avatarinfo.m_static_map.hasOwnProperty(key) == false){
			Avatarinfo.m_static_map[key] = Avatarinfo.create_Avatarinfo(key);
		}
		return Avatarinfo.m_static_map[key];	
	}
	public static create_Avatarinfo(key){
		if(avatarinfo_map.hasOwnProperty(key)){
			return new Avatarinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return avatarinfo_map;
	}
}
}