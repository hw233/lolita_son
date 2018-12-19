/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let weaponinfo_map = null;
export function weaponinfo_map_init(config_obj:Object):void{
	weaponinfo_map = config_obj["weaponinfo_map"];
}


export class Weaponinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = weaponinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Weaponinfo(key){
		if(Weaponinfo.m_static_map.hasOwnProperty(key) == false){
			Weaponinfo.m_static_map[key] = Weaponinfo.create_Weaponinfo(key);
		}
		return Weaponinfo.m_static_map[key];	
	}
	public static create_Weaponinfo(key){
		if(weaponinfo_map.hasOwnProperty(key)){
			return new Weaponinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return weaponinfo_map;
	}
}
}