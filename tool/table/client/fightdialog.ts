/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightdialog_map = null;
export function fightdialog_map_init(config_obj:Object):void{
	fightdialog_map = config_obj["fightdialog_map"];
}


export class Fightdialog extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightdialog_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightdialog(key){
		if(Fightdialog.m_static_map.hasOwnProperty(key) == false){
			Fightdialog.m_static_map[key] = Fightdialog.create_Fightdialog(key);
		}
		return Fightdialog.m_static_map[key];	
	}
	public static create_Fightdialog(key){
		if(fightdialog_map.hasOwnProperty(key)){
			return new Fightdialog(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightdialog_map;
	}
}
}