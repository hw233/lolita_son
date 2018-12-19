/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let specialskill3_map = null;
export function specialskill3_map_init(config_obj:Object):void{
	specialskill3_map = config_obj["specialskill3_map"];
}


export class Specialskill3 extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = specialskill3_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Specialskill3(key){
		if(Specialskill3.m_static_map.hasOwnProperty(key) == false){
			Specialskill3.m_static_map[key] = Specialskill3.create_Specialskill3(key);
		}
		return Specialskill3.m_static_map[key];	
	}
	public static create_Specialskill3(key){
		if(specialskill3_map.hasOwnProperty(key)){
			return new Specialskill3(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return specialskill3_map;
	}
}
}