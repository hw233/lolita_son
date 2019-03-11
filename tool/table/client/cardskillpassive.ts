/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let cardskillpassive_map = null;
export function cardskillpassive_map_init(config_obj:Object):void{
	cardskillpassive_map = config_obj["cardskillpassive_map"];
}


export class Cardskillpassive extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = cardskillpassive_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Cardskillpassive(key){
		if(Cardskillpassive.m_static_map.hasOwnProperty(key) == false){
			Cardskillpassive.m_static_map[key] = Cardskillpassive.create_Cardskillpassive(key);
		}
		return Cardskillpassive.m_static_map[key];	
	}
	public static create_Cardskillpassive(key){
		if(cardskillpassive_map.hasOwnProperty(key)){
			return new Cardskillpassive(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return cardskillpassive_map;
	}
}
}