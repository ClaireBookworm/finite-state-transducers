from module import FiniteStateTranducer
import json

machine = FiniteStateTranducer()

with open('../python-to-cpp/automaton_if.json') as f:
	obj = json.load(f)

print(obj)
machine.build_from_dict(obj)

