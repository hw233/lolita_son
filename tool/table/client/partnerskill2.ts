/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let partnerskill2_map = null;
export function partnerskill2_map_init(config_obj:Object):void{
	partnerskill2_map = config_obj["partnerskill2_map"];
}


export class Partnerskill2 extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = partnerskill2_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Partnerskill2(key){
		if(Partnerskill2.m_static_map.hasOwnProperty(key) == false){
			Partnerskill2.m_static_map[key] = Partnerskill2.create_Partnerskill2(key);
		}
		return Partnerskill2.m_static_map[key];	
	}
	public static create_Partnerskill2(key){
		if(partnerskill2_map.hasOwnProperty(key)){
			return new Partnerskill2(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return partnerskill2_map;
	}
}
}