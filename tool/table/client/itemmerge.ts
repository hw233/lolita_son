/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let itemmerge_map = null;
export function itemmerge_map_init(config_obj:Object):void{
	itemmerge_map = config_obj["itemmerge_map"];
}


export class Itemmerge extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = itemmerge_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Itemmerge(key){
		if(Itemmerge.m_static_map.hasOwnProperty(key) == false){
			Itemmerge.m_static_map[key] = Itemmerge.create_Itemmerge(key);
		}
		return Itemmerge.m_static_map[key];	
	}
	public static create_Itemmerge(key){
		if(itemmerge_map.hasOwnProperty(key)){
			return new Itemmerge(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return itemmerge_map;
	}
}
}