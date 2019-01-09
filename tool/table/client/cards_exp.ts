/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let cards_exp_map = null;
export function cards_exp_map_init(config_obj:Object):void{
	cards_exp_map = config_obj["cards_exp_map"];
}


export class Cards_exp extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = cards_exp_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Cards_exp(key){
		if(Cards_exp.m_static_map.hasOwnProperty(key) == false){
			Cards_exp.m_static_map[key] = Cards_exp.create_Cards_exp(key);
		}
		return Cards_exp.m_static_map[key];	
	}
	public static create_Cards_exp(key){
		if(cards_exp_map.hasOwnProperty(key)){
			return new Cards_exp(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return cards_exp_map;
	}
}
}