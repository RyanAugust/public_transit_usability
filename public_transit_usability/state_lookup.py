import pandas as pd

class state_lookup(object):
	def __init__(self):
		self.df = pd.read_csv('shapefile_state_def',sep='|')
	def get_state_num(self, state):
		try:
			stateline = self.df[self.df['STATE_NAME'] == state]
			return stateline['STATE'].tolist()[0]
		except:
			print('State Not Found')
	def get_state_name(self, state):
		try:
			stateline = df[df['STATE'] == state]
			return stateline['STATE_NAME']
		except:
			print('State Num Not Found')

state_lookup = state_lookup()