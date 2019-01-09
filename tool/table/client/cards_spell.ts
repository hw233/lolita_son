/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let cards_spell_map = null;
export function cards_spell_map_init(config_obj:Object):void{
	cards_spell_map = config_obj["cards_spell_map"];
}


export class Cards_spell extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = cards_spell_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Cards_spell(key){
		if(Cards_spell.m_static_map.hasOwnProperty(key) == false){
			Cards_spell.m_static_map[key] = Cards_spell.create_Cards_spell(key);
		}
		return Cards_spell.m_static_map[key];	
	}
	public static create_Cards_spell(key){
		if(cards_spell_map.hasOwnProperty(key)){
			return new Cards_spell(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return cards_spell_map;
	}
}
}