/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let item_map = null;
export function item_map_init(config_obj:Object):void{
	item_map = config_obj["item_map"];
}


export class Item extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = item_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Item(key){
		if(Item.m_static_map.hasOwnProperty(key) == false){
			Item.m_static_map[key] = Item.create_Item(key);
		}
		return Item.m_static_map[key];	
	}
	public static create_Item(key){
		if(item_map.hasOwnProperty(key)){
			return new Item(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return item_map;
	}
}
}