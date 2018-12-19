/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let petskill1_map = null;
export function petskill1_map_init(config_obj:Object):void{
	petskill1_map = config_obj["petskill1_map"];
}


export class Petskill1 extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = petskill1_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Petskill1(key){
		if(Petskill1.m_static_map.hasOwnProperty(key) == false){
			Petskill1.m_static_map[key] = Petskill1.create_Petskill1(key);
		}
		return Petskill1.m_static_map[key];	
	}
	public static create_Petskill1(key){
		if(petskill1_map.hasOwnProperty(key)){
			return new Petskill1(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return petskill1_map;
	}
}
}