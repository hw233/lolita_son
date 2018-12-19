/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let specialskill1_map = null;
export function specialskill1_map_init(config_obj:Object):void{
	specialskill1_map = config_obj["specialskill1_map"];
}


export class Specialskill1 extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = specialskill1_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Specialskill1(key){
		if(Specialskill1.m_static_map.hasOwnProperty(key) == false){
			Specialskill1.m_static_map[key] = Specialskill1.create_Specialskill1(key);
		}
		return Specialskill1.m_static_map[key];	
	}
	public static create_Specialskill1(key){
		if(specialskill1_map.hasOwnProperty(key)){
			return new Specialskill1(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return specialskill1_map;
	}
}
}