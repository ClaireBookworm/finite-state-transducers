
class Point:
	def __init__(self,id_,isFinal_,parrot_,transitions_=None):
		self.id = id_
		self.isFinal = isFinal_
		self.parrot_ = parrot_
		self.transitions = transitions_
		if self.transitions is None:
			self.transitions = []

	def add_transition(self,transition=None):
		if transition is not None:
			self.transitions.append(transition)

	def add_quick_transition(self,words_,target_,output_):
		self.transitions.append(Transition(words_,self.id,target_,output_))

	def get_transition(self,word):
		for transition in self.transitions:
			if transition.contains(word):
				return transition
		if self.parrot_:
			return Transition([], self.id, self.id, word)
		raise SyntaxError('you have fucked up')
		return None

class Transition:
	def __init__(self,words_,start_,target_,output_):
		self.words = words_
		self.start = start_
		self.target = target_
		self.output = output_

	def contains(self,word):
		return (word in self.words)

class FiniteStateTranducer:
	def __init__(self):
		self.start_id = 0
		self.max_id = 0
		self.points = {}
		
	def build(self,start_id_,clear_points,transitions):
		self.start_id = start_id_
		self.points = clear_points # a dict id:point
		for id_ in self.points.keys():
			for transition in transitions:
				if transition.start == id_:
					print(transition.start, transition.target, id_)
					self.points[id_].add_transition(transition)
		self.max_id = max(self.points.keys())

	def add_point(self, isFinal_=False, parrot_=False): # please remember to implement parrot
		self.max_id += 1
		self.points[self.max_id] = Point(self.max_id, isFinal_, parrot_)
		return self.max_id

	def step(self,word):
		#print(self.start_id,word)
		transition = self.points[self.start_id].get_transition(word)
		self.start_id = transition.target
		return self.points[transition.target].isFinal, transition.output

	def run(self,words):
		outputs = []
		end = False
		for word in words:
			end, output = self.step(word)
			outputs.append(output)
		return end, outputs # report if it's successful or not

	def build_from_dict(self,machine):
		clear_points = {}
		for i,point in enumerate(machine['nodes']):
			clear_points[i] = Point(i, point['isAcceptState'])
		transitions = []
		start_id = 0
		for link in machine['links']:
			if link['type']=='StartLink':
				start_id = link['node']
				continue
			text = link['text']
			if '`' in text:
				input_, output_ = text.split('`')[1], text.split('`')[3]
			elif ':' in text:
				input_, output_ = text.split(':')[0], text.split(':')[1]
			else:
				print('you are fucked')
			if link['type']=='SelfLink':
				transitions.append(Transition(input_,link['node'],link['node'],output_))
			elif link['type']=='Link':
				transitions.append(Transition(input_,link['nodeA'],link['nodeB'],output_))
			else:
				pass
		self.build(start_id,clear_points,transitions)





