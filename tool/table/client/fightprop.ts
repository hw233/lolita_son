/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightprop_map = null;
export function fightprop_map_init(config_obj:Object):void{
	fightprop_map = config_obj["fightprop_map"];
}


export class Fightprop extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightprop_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightprop(key){
		if(Fightprop.m_static_map.hasOwnProperty(key) == false){
			Fightprop.m_static_map[key] = Fightprop.create_Fightprop(key);
		}
		return Fightprop.m_static_map[key];	
	}
	public static create_Fightprop(key){
		if(fightprop_map.hasOwnProperty(key)){
			return new Fightprop(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightprop_map;
	}
}
}