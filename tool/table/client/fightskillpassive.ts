/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightskillpassive_map = null;
export function fightskillpassive_map_init(config_obj:Object):void{
	fightskillpassive_map = config_obj["fightskillpassive_map"];
}


export class Fightskillpassive extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightskillpassive_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightskillpassive(key){
		if(Fightskillpassive.m_static_map.hasOwnProperty(key) == false){
			Fightskillpassive.m_static_map[key] = Fightskillpassive.create_Fightskillpassive(key);
		}
		return Fightskillpassive.m_static_map[key];	
	}
	public static create_Fightskillpassive(key){
		if(fightskillpassive_map.hasOwnProperty(key)){
			return new Fightskillpassive(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightskillpassive_map;
	}
}
}