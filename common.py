#coding:utf8

import sys

def get_cur_info(self):
	print sys._getframe().f_code.co_filename
	print sys._getframe().f_code.co_name
	print sys._getframe().f_lineno
