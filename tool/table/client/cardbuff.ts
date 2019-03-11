/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let cardbuff_map = null;
export function cardbuff_map_init(config_obj:Object):void{
	cardbuff_map = config_obj["cardbuff_map"];
}


export class Cardbuff extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = cardbuff_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Cardbuff(key){
		if(Cardbuff.m_static_map.hasOwnProperty(key) == false){
			Cardbuff.m_static_map[key] = Cardbuff.create_Cardbuff(key);
		}
		return Cardbuff.m_static_map[key];	
	}
	public static create_Cardbuff(key){
		if(cardbuff_map.hasOwnProperty(key)){
			return new Cardbuff(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return cardbuff_map;
	}
}
}