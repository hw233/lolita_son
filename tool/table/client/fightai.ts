/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightai_map = null;
export function fightai_map_init(config_obj:Object):void{
	fightai_map = config_obj["fightai_map"];
}


export class Fightai extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightai_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightai(key){
		if(Fightai.m_static_map.hasOwnProperty(key) == false){
			Fightai.m_static_map[key] = Fightai.create_Fightai(key);
		}
		return Fightai.m_static_map[key];	
	}
	public static create_Fightai(key){
		if(fightai_map.hasOwnProperty(key)){
			return new Fightai(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightai_map;
	}
}
}