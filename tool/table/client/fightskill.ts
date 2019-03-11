/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightskill_map = null;
export function fightskill_map_init(config_obj:Object):void{
	fightskill_map = config_obj["fightskill_map"];
}


export class Fightskill extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightskill_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightskill(key){
		if(Fightskill.m_static_map.hasOwnProperty(key) == false){
			Fightskill.m_static_map[key] = Fightskill.create_Fightskill(key);
		}
		return Fightskill.m_static_map[key];	
	}
	public static create_Fightskill(key){
		if(fightskill_map.hasOwnProperty(key)){
			return new Fightskill(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightskill_map;
	}
}
}