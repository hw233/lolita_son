/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let cards_effect_map = null;
export function cards_effect_map_init(config_obj:Object):void{
	cards_effect_map = config_obj["cards_effect_map"];
}


export class Cards_effect extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = cards_effect_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Cards_effect(key){
		if(Cards_effect.m_static_map.hasOwnProperty(key) == false){
			Cards_effect.m_static_map[key] = Cards_effect.create_Cards_effect(key);
		}
		return Cards_effect.m_static_map[key];	
	}
	public static create_Cards_effect(key){
		if(cards_effect_map.hasOwnProperty(key)){
			return new Cards_effect(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return cards_effect_map;
	}
}
}