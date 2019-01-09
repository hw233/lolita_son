/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let cards_map = null;
export function cards_map_init(config_obj:Object):void{
	cards_map = config_obj["cards_map"];
}


export class Cards extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = cards_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Cards(key){
		if(Cards.m_static_map.hasOwnProperty(key) == false){
			Cards.m_static_map[key] = Cards.create_Cards(key);
		}
		return Cards.m_static_map[key];	
	}
	public static create_Cards(key){
		if(cards_map.hasOwnProperty(key)){
			return new Cards(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return cards_map;
	}
}
}