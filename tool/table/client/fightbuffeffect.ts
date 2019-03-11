/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightbuffeffect_map = null;
export function fightbuffeffect_map_init(config_obj:Object):void{
	fightbuffeffect_map = config_obj["fightbuffeffect_map"];
}


export class Fightbuffeffect extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightbuffeffect_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightbuffeffect(key){
		if(Fightbuffeffect.m_static_map.hasOwnProperty(key) == false){
			Fightbuffeffect.m_static_map[key] = Fightbuffeffect.create_Fightbuffeffect(key);
		}
		return Fightbuffeffect.m_static_map[key];	
	}
	public static create_Fightbuffeffect(key){
		if(fightbuffeffect_map.hasOwnProperty(key)){
			return new Fightbuffeffect(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightbuffeffect_map;
	}
}
}