import sys
from printer import *

cprint('cprint : default')
cprint('cprint : red', color = 'red')
cprint('cprint : green - bold', color = 'green', mode = 'bold')
cprint('cprint : yellow - blink - end', color = 'yellow', mode = 'blink', end = '\n')
cprint('cprint : magenta - inverted+underlined', color = 'magenta', mode = ['inverted', 'underlined'])

print()

print(cprepare('cprepare : default'))
print(cprepare('cprepare : red', color = 'red'))
print(cprepare('cprepare : green - bold', color = 'green', mode = 'bold'))
print(cprepare('cprepare : yellow - blink - end', color = 'yellow', mode = 'blink'), end = '\n')
print(cprepare('cprepare : magenta - inverted+underlined', color = 'magenta', mode = ['inverted', 'underlined']))

print()

customprint('customprint : default')
customprint('customprint : 24', color = 24)
customprint('customprint : 99 - bold', color = 99, mode = 'bold')
customprint('customprint : 202 - blink - end', color = 202, mode = 'blink', end = '\n')
customprint('customprint : 39 - inverted+underlined', color = 39, mode = ['inverted', 'underlined'])

print()

print(customprepare('customprepare : default'))
print(customprepare('customprepare : 24', color = 24))
print(customprepare('customprepare : 99 - bold', color = 99, mode = 'bold'))
print(customprepare('customprepare : 202 - blink - end', color = 202, mode = 'blink'), end = '\n')
print(customprepare('customprepare : 39 - inverted+underlined', color = 39, mode = ['inverted', 'underlined']))

print()

ecprint('ecprint : default')
ecprint('ecprint : blue', color = 'blue')
ecprint('ecprint : yellow - bold', color = 'yellow', mode = 'bold')
ecprint('yellow - blink - template', color = 'yellow', mode = 'blink', template = 'ecprint : {}')
ecprint('orange', color = 'orange', mode = ['underlined', 'blink'], template = 'ecprint : {}')
ecprint(['blue', 'blue'], color = 'blue', mode = 'bold', template = 'ecprint : 1:{} 2:{}')
ecprint(['yellow', 'blue'], color = ['yellow', 'blue'], mode = 'bold', template = 'ecprint : 1:{} 2:{}')
ecprint(['blink', 'underlined'], color = 'blue', mode = ['blink', 'underlined'], template = 'ecprint : 1:{} 2:{}')
ecprint(['yellow+blink', 'blue+underlined'], color = ['yellow', 'blue'], mode = ['blink', 'underlined'], template = 'ecprint : 1:{} 2:{}')
ecprint(['default+inverted+underlined', 'default+bold+underlined'], mode = [['inverted', 'underlined'], ['bold', 'underlined']], template = 'ecprint : 1:{} 2:{}')
ecprint(['yellow+blink+underlined', 'blue+blink+underlined'], color = ['yellow', 'blue'], mode = [['blink', 'underlined'], ['blink', 'underlined']], template = 'ecprint : 1:{} 2:{}')

print()

print(ecprepare('ecprepare : default'))
print(ecprepare('ecprepare : blue', color = 'blue'))
print(ecprepare('ecprepare : yellow - bold', color = 'yellow', mode = 'bold'))
print(ecprepare('yellow - blink - template', color = 'yellow', mode = 'blink', template = 'ecprepare : {}'))
print(ecprepare('orange', color = 'orange', mode = ['underlined', 'blink'], template = 'ecprepare : {}'))
print(ecprepare(['blue', 'blue'], color = 'blue', mode = 'bold', template = 'ecprepare : 1:{} 2:{}'))
print(ecprepare(['yellow', 'blue'], color = ['yellow', 'blue'], mode = 'bold', template = 'ecprepare : 1:{} 2:{}'))
print(ecprepare(['blink', 'underlined'], color = 'blue', mode = ['blink', 'underlined'], template = 'ecprepare : 1:{} 2:{}'))
print(ecprepare(['yellow+blink', 'blue+underlined'], color = ['yellow', 'blue'], mode = ['blink', 'underlined'], template = 'ecprepare : 1:{} 2:{}'))
print(ecprepare(['default+inverted+underlined', 'default+bold+underlined'], mode = [['inverted', 'underlined'], ['bold', 'underlined']], template = 'ecprepare : 1:{} 2:{}'))
print(ecprepare(['yellow+blink+underlined', 'blue+blink+underlined'], color = ['yellow', 'blue'], mode = [['blink', 'underlined'], ['blink', 'underlined']], template = 'ecprepare : 1:{} 2:{}'))

print()

data = [[1, 'vic', '9ad597'],[2, 'arangu', '5f4dcc'],[3, 'orbegoso', '25f9e7'],[4, 'jisus', '6eea9b']]
ctable(['id', 'username', 'passwd'], data)
ctable(['id', 'username', 'passwd'], data, header_color = 'blue', header_mode = 'bold')
ctable(['id', 'username', 'passwd'], data, header_color = 'blue', header_mode = 'bold', rows_color = 'lblue', rows_mode = 'dim')
ctable(['id', 'username', 'passwd'], data, header_color = 'blue', header_mode = 'bold', rows_color = 'lblue', rows_mode = 'dim', table_color = 'red', table_mode = 'blink')
ctable(['id', 'username', 'passwd'], data, side_spacing = 3, horizontal_separator = '~', vertical_separator = '^^')
