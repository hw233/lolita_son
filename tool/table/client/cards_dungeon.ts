/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let cards_dungeon_map = null;
export function cards_dungeon_map_init(config_obj:Object):void{
	cards_dungeon_map = config_obj["cards_dungeon_map"];
}


export class Cards_dungeon extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = cards_dungeon_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Cards_dungeon(key){
		if(Cards_dungeon.m_static_map.hasOwnProperty(key) == false){
			Cards_dungeon.m_static_map[key] = Cards_dungeon.create_Cards_dungeon(key);
		}
		return Cards_dungeon.m_static_map[key];	
	}
	public static create_Cards_dungeon(key){
		if(cards_dungeon_map.hasOwnProperty(key)){
			return new Cards_dungeon(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return cards_dungeon_map;
	}
}
}