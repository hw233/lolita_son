/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let partner_exp_map = null;
export function partner_exp_map_init(config_obj:Object):void{
	partner_exp_map = config_obj["partner_exp_map"];
}


export class Partner_exp extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = partner_exp_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Partner_exp(key){
		if(Partner_exp.m_static_map.hasOwnProperty(key) == false){
			Partner_exp.m_static_map[key] = Partner_exp.create_Partner_exp(key);
		}
		return Partner_exp.m_static_map[key];	
	}
	public static create_Partner_exp(key){
		if(partner_exp_map.hasOwnProperty(key)){
			return new Partner_exp(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return partner_exp_map;
	}
}
}