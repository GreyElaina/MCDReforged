# -*- coding: utf-8 -*-

import random

counter = 0
secret = random.random()


def add_help_message(server):
	server.add_help_message('!!start', 'Start the server')
	server.add_help_message('!!stop', 'Stop the server')
	server.add_help_message('!!restart', 'Restart the server')
	server.add_help_message('!!rcon', 'Rcon test')
	server.add_help_message('!!permission', 'Get permission level')
	server.add_help_message('!!error', 'What is 1/0?')
	server.add_help_message('!!status', 'Get server status')
	server.add_help_message('!!secret', 'get_plugin_instance() test')


def on_load(server, old_module):
	global counter
	counter = old_module.counter + 1 if old_module is not None else 1
	msg = f'This is the {counter} time to load the plugin'
	if server.is_server_running():
		server.say(msg)
	server.logger.info(msg)
	add_help_message(server)


def on_unload(server):
	server.logger.info('bye')


def on_info(server, info):
	if not info.is_user:
		return
	if info.content == 'ping':
		server.reply(info, 'pong')
	if server.get_permission_level(info) == 3:
		if info.content == '!!start':
			server.start()
		if info.content == '!!stop':
			server.stop_exit()
		if info.content == '!!restart':
			server.restart()
	if info.source == 1 and info.content.startswith('!!say '):
		server.say(info.content[6:])
	if info.content == '!!rcon':
		server.reply(info, f'rcon is running? {str(server.is_rcon_running())}')
		if server.is_rcon_running():
			server.reply(info, '"time query gametime" command result: ' + server.rcon_query('time query gametime'))
	if info.content == '!!permission':
		server.reply(
		    info, f'Your permission level is {server.get_permission_level(info)}')
	if info.content == '!!error':
		x = 1 / 0
	if info.content == '!!status':
		server.reply(info, '''
is_server_running: {}
is_server_startup: {}
is_rcon_running: {}
			'''.strip().format(
			server.is_server_running(),
			server.is_server_startup(),
			server.is_rcon_running(),
		))
	if info.content == '!!secret':
		global secret
		server.reply(info, 'My secret number is {}\nAnd You know it too {}'.format(
			secret, server.get_plugin_instance('sample_plugin').secret)
		)


def on_player_joined(server, player):
	server.tell(player, 'Welcome!')
	server.say(f'Hi {player}')


def on_player_left(server, player):
	server.say(f'Bye {player}')


def on_death_message(server, message):
	server.say(f"RIP {message.split(' ')[0]}")


def on_player_made_advancement(server, player, advancement):
	server.say(f'Good job {player} u have got "{advancement}"')


def on_server_startup(server):
	server.logger.info('Server has started')


def on_server_stop(server, return_code):
	server.logger.info(f'Server has stopped and its return code is {return_code}')


def on_mcdr_stop(server):
	server.logger.info('See you next time~')
