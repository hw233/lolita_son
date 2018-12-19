/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let playerskill1_map = null;
export function playerskill1_map_init(config_obj:Object):void{
	playerskill1_map = config_obj["playerskill1_map"];
}


export class Playerskill1 extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = playerskill1_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Playerskill1(key){
		if(Playerskill1.m_static_map.hasOwnProperty(key) == false){
			Playerskill1.m_static_map[key] = Playerskill1.create_Playerskill1(key);
		}
		return Playerskill1.m_static_map[key];	
	}
	public static create_Playerskill1(key){
		if(playerskill1_map.hasOwnProperty(key)){
			return new Playerskill1(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return playerskill1_map;
	}
}
}