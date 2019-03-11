/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fighteffecttime_map = null;
export function fighteffecttime_map_init(config_obj:Object):void{
	fighteffecttime_map = config_obj["fighteffecttime_map"];
}


export class Fighteffecttime extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fighteffecttime_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fighteffecttime(key){
		if(Fighteffecttime.m_static_map.hasOwnProperty(key) == false){
			Fighteffecttime.m_static_map[key] = Fighteffecttime.create_Fighteffecttime(key);
		}
		return Fighteffecttime.m_static_map[key];	
	}
	public static create_Fighteffecttime(key){
		if(fighteffecttime_map.hasOwnProperty(key)){
			return new Fighteffecttime(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fighteffecttime_map;
	}
}
}