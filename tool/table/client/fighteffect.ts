/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fighteffect_map = null;
export function fighteffect_map_init(config_obj:Object):void{
	fighteffect_map = config_obj["fighteffect_map"];
}


export class Fighteffect extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fighteffect_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fighteffect(key){
		if(Fighteffect.m_static_map.hasOwnProperty(key) == false){
			Fighteffect.m_static_map[key] = Fighteffect.create_Fighteffect(key);
		}
		return Fighteffect.m_static_map[key];	
	}
	public static create_Fighteffect(key){
		if(fighteffect_map.hasOwnProperty(key)){
			return new Fighteffect(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fighteffect_map;
	}
}
}