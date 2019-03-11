/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightbuff_map = null;
export function fightbuff_map_init(config_obj:Object):void{
	fightbuff_map = config_obj["fightbuff_map"];
}


export class Fightbuff extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightbuff_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightbuff(key){
		if(Fightbuff.m_static_map.hasOwnProperty(key) == false){
			Fightbuff.m_static_map[key] = Fightbuff.create_Fightbuff(key);
		}
		return Fightbuff.m_static_map[key];	
	}
	public static create_Fightbuff(key){
		if(fightbuff_map.hasOwnProperty(key)){
			return new Fightbuff(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightbuff_map;
	}
}
}