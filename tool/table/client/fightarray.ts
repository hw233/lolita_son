/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightarray_map = null;
export function fightarray_map_init(config_obj:Object):void{
	fightarray_map = config_obj["fightarray_map"];
}


export class Fightarray extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightarray_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightarray(key){
		if(Fightarray.m_static_map.hasOwnProperty(key) == false){
			Fightarray.m_static_map[key] = Fightarray.create_Fightarray(key);
		}
		return Fightarray.m_static_map[key];	
	}
	public static create_Fightarray(key){
		if(fightarray_map.hasOwnProperty(key)){
			return new Fightarray(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightarray_map;
	}
}
}