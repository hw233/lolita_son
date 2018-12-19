/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let buffinfo_map = null;
export function buffinfo_map_init(config_obj:Object):void{
	buffinfo_map = config_obj["buffinfo_map"];
}


export class Buffinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = buffinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Buffinfo(key){
		if(Buffinfo.m_static_map.hasOwnProperty(key) == false){
			Buffinfo.m_static_map[key] = Buffinfo.create_Buffinfo(key);
		}
		return Buffinfo.m_static_map[key];	
	}
	public static create_Buffinfo(key){
		if(buffinfo_map.hasOwnProperty(key)){
			return new Buffinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return buffinfo_map;
	}
}
}