/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let mapinfo_map = null;
export function mapinfo_map_init(config_obj:Object):void{
	mapinfo_map = config_obj["mapinfo_map"];
}


export class Mapinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = mapinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Mapinfo(key){
		if(Mapinfo.m_static_map.hasOwnProperty(key) == false){
			Mapinfo.m_static_map[key] = Mapinfo.create_Mapinfo(key);
		}
		return Mapinfo.m_static_map[key];	
	}
	public static create_Mapinfo(key){
		if(mapinfo_map.hasOwnProperty(key)){
			return new Mapinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return mapinfo_map;
	}
}
}