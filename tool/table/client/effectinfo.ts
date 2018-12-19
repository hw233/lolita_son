/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let effectinfo_map = null;
export function effectinfo_map_init(config_obj:Object):void{
	effectinfo_map = config_obj["effectinfo_map"];
}


export class Effectinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = effectinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Effectinfo(key){
		if(Effectinfo.m_static_map.hasOwnProperty(key) == false){
			Effectinfo.m_static_map[key] = Effectinfo.create_Effectinfo(key);
		}
		return Effectinfo.m_static_map[key];	
	}
	public static create_Effectinfo(key){
		if(effectinfo_map.hasOwnProperty(key)){
			return new Effectinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return effectinfo_map;
	}
}
}