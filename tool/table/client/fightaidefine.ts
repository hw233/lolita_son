/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightaidefine_map = null;
export function fightaidefine_map_init(config_obj:Object):void{
	fightaidefine_map = config_obj["fightaidefine_map"];
}


export class Fightaidefine extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightaidefine_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightaidefine(key){
		if(Fightaidefine.m_static_map.hasOwnProperty(key) == false){
			Fightaidefine.m_static_map[key] = Fightaidefine.create_Fightaidefine(key);
		}
		return Fightaidefine.m_static_map[key];	
	}
	public static create_Fightaidefine(key){
		if(fightaidefine_map.hasOwnProperty(key)){
			return new Fightaidefine(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightaidefine_map;
	}
}
}