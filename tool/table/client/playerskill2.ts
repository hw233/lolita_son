/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let playerskill2_map = null;
export function playerskill2_map_init(config_obj:Object):void{
	playerskill2_map = config_obj["playerskill2_map"];
}


export class Playerskill2 extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = playerskill2_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Playerskill2(key){
		if(Playerskill2.m_static_map.hasOwnProperty(key) == false){
			Playerskill2.m_static_map[key] = Playerskill2.create_Playerskill2(key);
		}
		return Playerskill2.m_static_map[key];	
	}
	public static create_Playerskill2(key){
		if(playerskill2_map.hasOwnProperty(key)){
			return new Playerskill2(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return playerskill2_map;
	}
}
}