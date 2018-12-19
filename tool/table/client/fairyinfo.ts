/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fairyinfo_map = null;
export function fairyinfo_map_init(config_obj:Object):void{
	fairyinfo_map = config_obj["fairyinfo_map"];
}


export class Fairyinfo extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fairyinfo_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fairyinfo(key){
		if(Fairyinfo.m_static_map.hasOwnProperty(key) == false){
			Fairyinfo.m_static_map[key] = Fairyinfo.create_Fairyinfo(key);
		}
		return Fairyinfo.m_static_map[key];	
	}
	public static create_Fairyinfo(key){
		if(fairyinfo_map.hasOwnProperty(key)){
			return new Fairyinfo(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fairyinfo_map;
	}
}
}