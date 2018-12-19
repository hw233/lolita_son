/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let player_exp_map = null;
export function player_exp_map_init(config_obj:Object):void{
	player_exp_map = config_obj["player_exp_map"];
}


export class Player_exp extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = player_exp_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Player_exp(key){
		if(Player_exp.m_static_map.hasOwnProperty(key) == false){
			Player_exp.m_static_map[key] = Player_exp.create_Player_exp(key);
		}
		return Player_exp.m_static_map[key];	
	}
	public static create_Player_exp(key){
		if(player_exp_map.hasOwnProperty(key)){
			return new Player_exp(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return player_exp_map;
	}
}
}