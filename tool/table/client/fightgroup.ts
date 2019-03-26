/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightgroup_map = null;
export function fightgroup_map_init(config_obj:Object):void{
	fightgroup_map = config_obj["fightgroup_map"];
}


export class Fightgroup extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightgroup_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightgroup(key){
		if(Fightgroup.m_static_map.hasOwnProperty(key) == false){
			Fightgroup.m_static_map[key] = Fightgroup.create_Fightgroup(key);
		}
		return Fightgroup.m_static_map[key];	
	}
	public static create_Fightgroup(key){
		if(fightgroup_map.hasOwnProperty(key)){
			return new Fightgroup(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightgroup_map;
	}
}
}