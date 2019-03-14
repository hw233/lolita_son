/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let skillperform_map = null;
export function skillperform_map_init(config_obj:Object):void{
	skillperform_map = config_obj["skillperform_map"];
}


export class Skillperform extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = skillperform_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Skillperform(key){
		if(Skillperform.m_static_map.hasOwnProperty(key) == false){
			Skillperform.m_static_map[key] = Skillperform.create_Skillperform(key);
		}
		return Skillperform.m_static_map[key];	
	}
	public static create_Skillperform(key){
		if(skillperform_map.hasOwnProperty(key)){
			return new Skillperform(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return skillperform_map;
	}
}
}