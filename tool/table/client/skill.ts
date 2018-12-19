/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let skill_map = null;
export function skill_map_init(config_obj:Object):void{
	skill_map = config_obj["skill_map"];
}


export class Skill extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = skill_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Skill(key){
		if(Skill.m_static_map.hasOwnProperty(key) == false){
			Skill.m_static_map[key] = Skill.create_Skill(key);
		}
		return Skill.m_static_map[key];	
	}
	public static create_Skill(key){
		if(skill_map.hasOwnProperty(key)){
			return new Skill(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return skill_map;
	}
}
}