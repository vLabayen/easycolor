import sys
from printer import *

#cprint('cprint : default')
#cprint('cprint : red', color = 'red')
#cprint('cprint : green - bold', color = 'green', mode = 'bold')
#cprint('cprint : yellow - blink - end', color = 'yellow', mode = 'blink', end = '\n')
#cprint('cprint : magenta - inverted+underlined', color = 'magenta', mode = ['inverted', 'underlined'])

#print(cprepare('cprepare : default'))
#print(cprepare('cprepare : red', color = 'red'))
#print(cprepare('cprepare : green - bold', color = 'green', mode = 'bold'))
#print(cprepare('cprepare : yellow - blink - end', color = 'yellow', mode = 'blink'), end = '\n')
#print(cprepare('cprepare : magenta - inverted+underlined', color = 'magenta', mode = ['inverted', 'underlined']))

#customprint('customprint : default')
#customprint('customprint : 24', color = 24)
#customprint('customprint : 99 - bold', color = 99, mode = 'bold')
#customprint('customprint : 202 - blink - end', color = 202, mode = 'blink', end = '\n')
#customprint('customprint : 39 - inverted+underlined', color = 39, mode = ['inverted', 'underlined'])

#print(customprepare('customprepare : default'))
#print(customprepare('customprepare : 24', color = 24))
#print(customprepare('customprepare : 99 - bold', color = 99, mode = 'bold'))
#print(customprepare('customprepare : 202 - blink - end', color = 202, mode = 'blink'), end = '\n')
#print(customprepare('customprepare : 39 - inverted+underlined', color = 39, mode = ['inverted', 'underlined']))

ctable(['id', 'username', 'passwd'], [
	[1, 'vic', '9ad597ad5037333fdf5663fae77b95f3'],
	[2, 'arangu', '5f4dcc3b5aa765d61d8327deb882cf99'],
	[3, 'orbegoso', '25f9e794323b453885f5181f1b624d0b'],
	[4, 'jisus', '6eea9b7ef19179a06954edd0f6c05ceb']
])
#ctable(['id', 'username', 'passwd'], [
#	[1, 'vic', '9ad597ad5037333fdf5663fae77b95f3'],
#	[2, 'arangu', '5f4dcc3b5aa765d61d8327deb882cf99'],
#	[3, 'orbegoso', '25f9e794323b453885f5181f1b624d0b'],
#	[4, 'jisus', '6eea9b7ef19179a06954edd0f6c05ceb']
#], header_color = 'blue', header_mode = 'bold')
#ctable(['id', 'username', 'passwd'], [
#	[1, 'vic', '9ad597ad5037333fdf5663fae77b95f3'],
#	[2, 'arangu', '5f4dcc3b5aa765d61d8327deb882cf99'],
#	[3, 'orbegoso', '25f9e794323b453885f5181f1b624d0b'],
#	[4, 'jisus', '6eea9b7ef19179a06954edd0f6c05ceb']
#], header_color = 'blue', header_mode = 'bold', rows_color = 'lblue', rows_mode = 'dim')
#ctable(['id', 'username', 'passwd'], [
#	[1, 'vic', '9ad597ad5037333fdf5663fae77b95f3'],
#	[2, 'arangu', '5f4dcc3b5aa765d61d8327deb882cf99'],
#	[3, 'orbegoso', '25f9e794323b453885f5181f1b624d0b'],
#	[4, 'jisus', '6eea9b7ef19179a06954edd0f6c05ceb']
#], header_color = 'blue', header_mode = 'bold', rows_color = 'lblue', rows_mode = 'dim', table_color = 'red', table_mode = 'blink')

ctable(['id', 'username', 'passwd'], [
	[1, 'vic', '9ad597ad5037333fdf5663fae77b95f3'],
	[2, 'arangu', '5f4dcc3b5aa765d61d8327deb882cf99'],
	[3, 'orbegoso', '25f9e794323b453885f5181f1b624d0b'],
	[4, 'jisus', '6eea9b7ef19179a06954edd0f6c05ceb']
], side_spacing = 3, horizontal_separator = '~', vertical_separator = '^^')
