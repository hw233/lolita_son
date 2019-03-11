/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let cardskill_map = null;
export function cardskill_map_init(config_obj:Object):void{
	cardskill_map = config_obj["cardskill_map"];
}


export class Cardskill extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = cardskill_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Cardskill(key){
		if(Cardskill.m_static_map.hasOwnProperty(key) == false){
			Cardskill.m_static_map[key] = Cardskill.create_Cardskill(key);
		}
		return Cardskill.m_static_map[key];	
	}
	public static create_Cardskill(key){
		if(cardskill_map.hasOwnProperty(key)){
			return new Cardskill(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return cardskill_map;
	}
}
}