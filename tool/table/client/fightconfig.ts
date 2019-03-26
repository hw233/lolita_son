/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightconfig_map = null;
export function fightconfig_map_init(config_obj:Object):void{
	fightconfig_map = config_obj["fightconfig_map"];
}


export class Fightconfig extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightconfig_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightconfig(key){
		if(Fightconfig.m_static_map.hasOwnProperty(key) == false){
			Fightconfig.m_static_map[key] = Fightconfig.create_Fightconfig(key);
		}
		return Fightconfig.m_static_map[key];	
	}
	public static create_Fightconfig(key){
		if(fightconfig_map.hasOwnProperty(key)){
			return new Fightconfig(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightconfig_map;
	}
}
}