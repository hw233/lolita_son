/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let partnerskill1_map = null;
export function partnerskill1_map_init(config_obj:Object):void{
	partnerskill1_map = config_obj["partnerskill1_map"];
}


export class Partnerskill1 extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = partnerskill1_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Partnerskill1(key){
		if(Partnerskill1.m_static_map.hasOwnProperty(key) == false){
			Partnerskill1.m_static_map[key] = Partnerskill1.create_Partnerskill1(key);
		}
		return Partnerskill1.m_static_map[key];	
	}
	public static create_Partnerskill1(key){
		if(partnerskill1_map.hasOwnProperty(key)){
			return new Partnerskill1(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return partnerskill1_map;
	}
}
}