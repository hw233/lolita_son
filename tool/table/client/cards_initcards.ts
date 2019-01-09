/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let cards_initcards_map = null;
export function cards_initcards_map_init(config_obj:Object):void{
	cards_initcards_map = config_obj["cards_initcards_map"];
}


export class Cards_initcards extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = cards_initcards_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Cards_initcards(key){
		if(Cards_initcards.m_static_map.hasOwnProperty(key) == false){
			Cards_initcards.m_static_map[key] = Cards_initcards.create_Cards_initcards(key);
		}
		return Cards_initcards.m_static_map[key];	
	}
	public static create_Cards_initcards(key){
		if(cards_initcards_map.hasOwnProperty(key)){
			return new Cards_initcards(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return cards_initcards_map;
	}
}
}