/*
Author: 
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
*/

module config{

${config_map}

export class ${class_name} extends Object{
	private m_config:any;
	public static m_static_map:Object = new Object();
	constructor(key){
		super();
		this.m_config = ${config_map_name}[key];
		for(let i in this.m_config){
			this[i] = this.m_config[i];
		}
		return;
	}
	public static get_${class_name}(key){
		if(${class_name}.m_static_map.hasOwnProperty(key) == false){
			${class_name}.m_static_map[key] = ${class_name}.create_${class_name}(key);
		}
		return ${class_name}.m_static_map[key];	
	}
	public static create_${class_name}(key){
		if(${config_map_name}.hasOwnProperty(key)){
			return new ${class_name}(key);
		}
		return null;	
	}
	public static get_cfg_object():Object
	{
		return ${config_map_name};
	}
}
}