# coding: utf-8

import app.game.core.game_module_def as game_module_def
import app.game.core.module.game_main as game_main
import app.base.game_module_mgr
import app.game.core.module.gm as gm
import app.game.core.module.mainplayer as mainplayer
import app.game.core.module.pet as pet
import app.game.core.module.partner as partner
def init_game_module():
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.GAME_MAIN,game_main.game_main);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.GM_MAIN,gm.gm_main);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.MAIN_PLAYER,mainplayer.mainplayer);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.PET,pet.pet);
	app.base.game_module_mgr.game_module_mgr().register_module(game_module_def.PARTNER,partner.partner);
	return