/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let skillpassive_map = null;
export function skillpassive_map_init(config_obj:Object):void{
	skillpassive_map = config_obj["skillpassive_map"];
}


export class Skillpassive extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = skillpassive_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Skillpassive(key){
		if(Skillpassive.m_static_map.hasOwnProperty(key) == false){
			Skillpassive.m_static_map[key] = Skillpassive.create_Skillpassive(key);
		}
		return Skillpassive.m_static_map[key];	
	}
	public static create_Skillpassive(key){
		if(skillpassive_map.hasOwnProperty(key)){
			return new Skillpassive(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return skillpassive_map;
	}
}
}