# -*- coding: utf-8 -*-
import traceback
from utils.server import Server
from utils import constant


if __name__ == '__main__':
	print(f'{constant.NAME_SHORT} {constant.VERSION} starting up')
	print(
	    f'{constant.NAME_SHORT} is open source, u can find it here: https://github.com/Fallen-Breath/MCDReforged'
	)
	print(f'{constant.NAME_SHORT} is still in development, it may not work well')
	try:
		server = Server()
	except:
		print(f'Fail to initialize {constant.NAME_SHORT}')
		print(traceback.format_exc())
		input('Press Enter to exit')
	else:
		server.start()
