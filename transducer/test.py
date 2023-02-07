from module import FiniteStateTranducer
import json

machine = FiniteStateTranducer()

with open('../python-to-cpp/automaton_test.json') as f:
	obj = json.load(f)

print(obj)
machine.build_from_dict(obj)

fit, outputs = machine.run(['a','b','c'])
print(f'works? : {fit}')
print(outputs)