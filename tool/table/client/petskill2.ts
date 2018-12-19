/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let petskill2_map = null;
export function petskill2_map_init(config_obj:Object):void{
	petskill2_map = config_obj["petskill2_map"];
}


export class Petskill2 extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = petskill2_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Petskill2(key){
		if(Petskill2.m_static_map.hasOwnProperty(key) == false){
			Petskill2.m_static_map[key] = Petskill2.create_Petskill2(key);
		}
		return Petskill2.m_static_map[key];	
	}
	public static create_Petskill2(key){
		if(petskill2_map.hasOwnProperty(key)){
			return new Petskill2(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return petskill2_map;
	}
}
}