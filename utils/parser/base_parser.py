# -*- coding: utf-8 -*-
import os
import re
import time

import utils.info
from utils.info import InfoSource


class BaseParser(object):
	NAME = os.path.basename(__file__).rstrip('.py')

	def __init__(self, parser_manager):
		self.STOP_COMMAND = None
		self.parser_manager = parser_manager

	# base parsing, return a Info instance
	def parse_server_stdout_raw(self, text):
		if type(text) is not str:
			raise TypeError('The text to parse should be a string')
		result = utils.info.Info()
		result.source = InfoSource.SERVER
		result.content = result.raw_content = text
		return result

	def parse_server_stdout(self, text):
		return self.parse_server_stdout_raw(text)

	# base parsing, return a Info instance
	def parse_console_command(self, text):
		if type(text) is not str:
			raise TypeError('The text to parse should be a string')
		result = utils.info.Info()
		result.raw_content = text
		t = time.localtime(time.time())
		result.hour = t.tm_hour
		result.min = t.tm_min
		result.sec = t.tm_sec
		result.content = text
		result.source = InfoSource.CONSOLE
		return result

	# returns 1 str: player_name
	# if not matches return None
	def parse_player_joined(self, info):
		return None

	# returns 1 str: player_name
	# if not matches return None
	def parse_player_left(self, info):
		return None

	# returns 1 bool: if info.content is a death message
	def parse_death_message(self, info):
		if info.is_user:
			return False
		re_list = self.parser_manager.get_death_message_list(type(self))
		return any(re.fullmatch(re_exp, info.content) for re_exp in re_list)

	# returns 2 str: player_name, advancement_name
	# if not matches return None
	def parse_player_made_advancement(self, info):
		return None

	def pre_parse_server_stdout(self, text):
		if text.startswith('\033['):
			text = re.sub(r'\033\[.*?m', '', text)
		return text

	# returns 1 bool: if info is a server startup message
	def parse_server_startup_done(self, info):
		return False


def get_parser(parser_manager):
	return BaseParser(parser_manager)
