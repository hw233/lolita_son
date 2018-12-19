/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let pet_exp_map = null;
export function pet_exp_map_init(config_obj:Object):void{
	pet_exp_map = config_obj["pet_exp_map"];
}


export class Pet_exp extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = pet_exp_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Pet_exp(key){
		if(Pet_exp.m_static_map.hasOwnProperty(key) == false){
			Pet_exp.m_static_map[key] = Pet_exp.create_Pet_exp(key);
		}
		return Pet_exp.m_static_map[key];	
	}
	public static create_Pet_exp(key){
		if(pet_exp_map.hasOwnProperty(key)){
			return new Pet_exp(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return pet_exp_map;
	}
}
}