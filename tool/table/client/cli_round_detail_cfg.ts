/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let cli_round_detail_cfg_map = null;
export function cli_round_detail_cfg_map_init(config_obj:Object):void{
	cli_round_detail_cfg_map = config_obj["cli_round_detail_cfg_map"];
}


export class Cli_round_detail_cfg extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = cli_round_detail_cfg_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Cli_round_detail_cfg(key){
		if(Cli_round_detail_cfg.m_static_map.hasOwnProperty(key) == false){
			Cli_round_detail_cfg.m_static_map[key] = Cli_round_detail_cfg.create_Cli_round_detail_cfg(key);
		}
		return Cli_round_detail_cfg.m_static_map[key];	
	}
	public static create_Cli_round_detail_cfg(key){
		if(cli_round_detail_cfg_map.hasOwnProperty(key)){
			return new Cli_round_detail_cfg(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return cli_round_detail_cfg_map;
	}
}
}