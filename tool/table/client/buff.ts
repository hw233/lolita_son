/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let buff_map = null;
export function buff_map_init(config_obj:Object):void{
	buff_map = config_obj["buff_map"];
}


export class Buff extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = buff_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Buff(key){
		if(Buff.m_static_map.hasOwnProperty(key) == false){
			Buff.m_static_map[key] = Buff.create_Buff(key);
		}
		return Buff.m_static_map[key];	
	}
	public static create_Buff(key){
		if(buff_map.hasOwnProperty(key)){
			return new Buff(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return buff_map;
	}
}
}