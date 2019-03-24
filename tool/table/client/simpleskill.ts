/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let simpleskill_map = null;
export function simpleskill_map_init(config_obj:Object):void{
	simpleskill_map = config_obj["simpleskill_map"];
}


export class Simpleskill extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = simpleskill_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Simpleskill(key){
		if(Simpleskill.m_static_map.hasOwnProperty(key) == false){
			Simpleskill.m_static_map[key] = Simpleskill.create_Simpleskill(key);
		}
		return Simpleskill.m_static_map[key];	
	}
	public static create_Simpleskill(key){
		if(simpleskill_map.hasOwnProperty(key)){
			return new Simpleskill(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return simpleskill_map;
	}
}
}