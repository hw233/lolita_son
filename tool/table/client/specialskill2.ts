/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let specialskill2_map = null;
export function specialskill2_map_init(config_obj:Object):void{
	specialskill2_map = config_obj["specialskill2_map"];
}


export class Specialskill2 extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = specialskill2_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Specialskill2(key){
		if(Specialskill2.m_static_map.hasOwnProperty(key) == false){
			Specialskill2.m_static_map[key] = Specialskill2.create_Specialskill2(key);
		}
		return Specialskill2.m_static_map[key];	
	}
	public static create_Specialskill2(key){
		if(specialskill2_map.hasOwnProperty(key)){
			return new Specialskill2(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return specialskill2_map;
	}
}
}