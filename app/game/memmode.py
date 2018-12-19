#-*-coding:utf8-*-
'''
Created on 2013-6-5

@author: lan
'''
from firefly.dbentrust.mmode import MAdmin

tb_character_admin = MAdmin('tb_character','id',incrkey='id')
tb_character_admin.insert()
tb_item_admin = MAdmin('tb_item','id',fk ='characterId',incrkey='id')
tb_item_admin.insert()
tb_itemopen_admin = MAdmin('tb_item_open','id',fk ='characterId',incrkey='id')
tb_itemopen_admin.insert()

tb_skill_admin = MAdmin('tb_skill','id',fk ='characterId',incrkey='id')
tb_skill_admin.insert()

tb_specskill_admin = MAdmin('tb_spec_skill','id',fk ='characterId',incrkey='id')
tb_specskill_admin.insert()

tb_pet_admin = MAdmin('tb_pet','id',fk ='characterId',incrkey='id')
tb_pet_admin.insert()

tb_petskill_admin = MAdmin('tb_pet_skill','id',fk ='characterId',incrkey='id')
tb_petskill_admin.insert()

tb_partner_admin = MAdmin('tb_partner','id',fk ='characterId',incrkey='id')
tb_partner_admin.insert()

tb_partnerskill_admin = MAdmin('tb_partner_skill','id',fk ='characterId',incrkey='id')
tb_partnerskill_admin.insert()