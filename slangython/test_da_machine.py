import sys
sys.path.append('..')
import re
from transducer.module import *
from slangython.build_da_machine import build_da_machine

machine = build_da_machine()


with open('fibonacci_code.slang', 'r') as f:
	code = f.read()
	print(code)
	words = [word for word in re.split('( |\n|\r|\b|\t)', code) if word != '' and word != ' ']
	#print(words)

end, result = machine.run(words)

if end:
	print('successfully translated to:\n')
else:
	print('you have fucked up')

processed_result = []
for word in result:
	if word == '': continue
	processed_result.append(word)
	if word == '\n' or word == '\r' or word == '\b' or word == '\t':
		continue
	processed_result.append(' ')

#print(processed_result)
print(''.join(processed_result))

with open('output_code.py', 'w') as f:
	f.write(''.join(processed_result))

