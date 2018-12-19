/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let specialskill4_map = null;
export function specialskill4_map_init(config_obj:Object):void{
	specialskill4_map = config_obj["specialskill4_map"];
}


export class Specialskill4 extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = specialskill4_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Specialskill4(key){
		if(Specialskill4.m_static_map.hasOwnProperty(key) == false){
			Specialskill4.m_static_map[key] = Specialskill4.create_Specialskill4(key);
		}
		return Specialskill4.m_static_map[key];	
	}
	public static create_Specialskill4(key){
		if(specialskill4_map.hasOwnProperty(key)){
			return new Specialskill4(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return specialskill4_map;
	}
}
}