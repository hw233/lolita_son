/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

let simplebuff_map = null;
export function simplebuff_map_init(config_obj:Object):void{
	simplebuff_map = config_obj["simplebuff_map"];
}


export class Simplebuff extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = simplebuff_map[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_Simplebuff(key){
		if(Simplebuff.m_static_map.hasOwnProperty(key) == false){
			Simplebuff.m_static_map[key] = Simplebuff.create_Simplebuff(key);
		}
		return Simplebuff.m_static_map[key];	
	}
	public static create_Simplebuff(key){
		if(simplebuff_map.hasOwnProperty(key)){
			return new Simplebuff(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return simplebuff_map;
	}
}
}