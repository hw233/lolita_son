# coding: utf-8

import app.core.game_module_def as game_module_def
import app.core.module.game_main as game_main
import app.base.game_module_mgr
import app.core.module.gm as gm
import app.core.module.mainplayer as mainplayer
import app.core.module.pet as pet
import app.core.module.partner as partner
import app.core.module.cards_mgr as cards_mgr
import app.core.module.scene_main as scene_main
import app.core.module.chat_main as chat_main
import app.core.module.combat_main as combat_main
def init_game_module():
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.GAME_MAIN,game_main.game_main);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.SCENE_MAIN,scene_main.scene_main);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.GM_MAIN,gm.gm_main);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.MAIN_PLAYER,mainplayer.mainplayer);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.PET,pet.pet);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.PARTNER,partner.partner);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.CARD_MAIN,cards_mgr.cards_mgr);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.CHAT_MAIN,chat_main.chat_main);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.COMBAT_MAIN,combat_main.combat_main);
	return