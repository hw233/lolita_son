/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightcombatai_map = null;
export function fightcombatai_map_init(config_obj:Object):void{
	fightcombatai_map = config_obj["fightcombatai_map"];
}


export class Fightcombatai extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightcombatai_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightcombatai(key){
		if(Fightcombatai.m_static_map.hasOwnProperty(key) == false){
			Fightcombatai.m_static_map[key] = Fightcombatai.create_Fightcombatai(key);
		}
		return Fightcombatai.m_static_map[key];	
	}
	public static create_Fightcombatai(key){
		if(fightcombatai_map.hasOwnProperty(key)){
			return new Fightcombatai(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightcombatai_map;
	}
}
}