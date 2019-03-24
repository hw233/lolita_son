/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let simpleskillpassive_map = null;
export function simpleskillpassive_map_init(config_obj:Object):void{
	simpleskillpassive_map = config_obj["simpleskillpassive_map"];
}


export class Simpleskillpassive extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = simpleskillpassive_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Simpleskillpassive(key){
		if(Simpleskillpassive.m_static_map.hasOwnProperty(key) == false){
			Simpleskillpassive.m_static_map[key] = Simpleskillpassive.create_Simpleskillpassive(key);
		}
		return Simpleskillpassive.m_static_map[key];	
	}
	public static create_Simpleskillpassive(key){
		if(simpleskillpassive_map.hasOwnProperty(key)){
			return new Simpleskillpassive(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return simpleskillpassive_map;
	}
}
}