#coding:utf8
import app.combat.buff as buff
import app.combat.skill as skill
import app.combat.skillpassive as skillpassive
buf = buff.buff(1001);
print buf.effect;

print skill.create_skill(1001,1).effect
print skillpassive.skillpassive(2001,1).effect

print 'test'
print skill.create_skill(1001,1).effect

import app.combat.autocombat
import app.combat.warrior
combat_obj = app.combat.autocombat.autocombat();
warrior_1 = app.combat.warrior.warrior(1,1);
warrior_1.set_data(warrior_1.gen_testdata())
warrior_20 = app.combat.warrior.warrior(20,20);
warrior_20.set_data(warrior_20.gen_testdata())
combat_obj.addwarrior(warrior_1);
combat_obj.addwarrior(warrior_20);
combat_obj.start();
turn_num = 0;
while True:
    if combat_obj.is_end():
        break;
    if turn_num >= 50:
        break;
    combat_obj.on_turn();
    turn_num += 1;
    print 'turn_num:%s'%(turn_num);
combat_obj.end();