/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let randomname_map = null;
export function randomname_map_init(config_obj:Object):void{
	randomname_map = config_obj["randomname_map"];
}


export class Randomname extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = randomname_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Randomname(key){
		if(Randomname.m_static_map.hasOwnProperty(key) == false){
			Randomname.m_static_map[key] = Randomname.create_Randomname(key);
		}
		return Randomname.m_static_map[key];	
	}
	public static create_Randomname(key){
		if(randomname_map.hasOwnProperty(key)){
			return new Randomname(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return randomname_map;
	}
}
}