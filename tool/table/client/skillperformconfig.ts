/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let skillperformconfig_map = null;
export function skillperformconfig_map_init(config_obj:Object):void{
	skillperformconfig_map = config_obj["skillperformconfig_map"];
}


export class Skillperformconfig extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = skillperformconfig_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Skillperformconfig(key){
		if(Skillperformconfig.m_static_map.hasOwnProperty(key) == false){
			Skillperformconfig.m_static_map[key] = Skillperformconfig.create_Skillperformconfig(key);
		}
		return Skillperformconfig.m_static_map[key];	
	}
	public static create_Skillperformconfig(key){
		if(skillperformconfig_map.hasOwnProperty(key)){
			return new Skillperformconfig(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return skillperformconfig_map;
	}
}
}