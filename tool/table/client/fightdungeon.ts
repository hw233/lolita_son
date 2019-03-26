/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let fightdungeon_map = null;
export function fightdungeon_map_init(config_obj:Object):void{
	fightdungeon_map = config_obj["fightdungeon_map"];
}


export class Fightdungeon extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = fightdungeon_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Fightdungeon(key){
		if(Fightdungeon.m_static_map.hasOwnProperty(key) == false){
			Fightdungeon.m_static_map[key] = Fightdungeon.create_Fightdungeon(key);
		}
		return Fightdungeon.m_static_map[key];	
	}
	public static create_Fightdungeon(key){
		if(fightdungeon_map.hasOwnProperty(key)){
			return new Fightdungeon(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return fightdungeon_map;
	}
}
}