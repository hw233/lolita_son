/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightdata_map = null;
export function fightdata_map_init(config_obj:Object):void{
	fightdata_map = config_obj["fightdata_map"];
}


export class Fightdata extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightdata_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightdata(key){
		if(Fightdata.m_static_map.hasOwnProperty(key) == false){
			Fightdata.m_static_map[key] = Fightdata.create_Fightdata(key);
		}
		return Fightdata.m_static_map[key];	
	}
	public static create_Fightdata(key){
		if(fightdata_map.hasOwnProperty(key)){
			return new Fightdata(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightdata_map;
	}
}
}