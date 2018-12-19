/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let rideinfo_map = null;
export function rideinfo_map_init(config_obj:Object):void{
	rideinfo_map = config_obj["rideinfo_map"];
}


export class Rideinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = rideinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Rideinfo(key){
		if(Rideinfo.m_static_map.hasOwnProperty(key) == false){
			Rideinfo.m_static_map[key] = Rideinfo.create_Rideinfo(key);
		}
		return Rideinfo.m_static_map[key];	
	}
	public static create_Rideinfo(key){
		if(rideinfo_map.hasOwnProperty(key)){
			return new Rideinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return rideinfo_map;
	}
}
}