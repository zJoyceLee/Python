import datetime

class timeCalc(object):
	"""docstring for timeCalc"""
	def __init__(self, time1, time2):
		super(timeCalc, self).__init__()
		self.time1 = time1
		self.time2 = time2
	def calc(self):
		return self.time2-self.time1
	def output(self):
		delta = self.calc()
		print('Delta Seconds: {}'.format(delta.seconds))
		print('Delta: {}'.format(delta))


print('Calculate Time2 - Time1, input sample: 2019-01-29 13:40:27.243860')
time_str1 = input('Time1: ')
time_str2 = input('Time2: ')
tmp = timeCalc(datetime.datetime.strptime(time_str1, '%Y-%m-%d %H:%M:%S.%f'), datetime.datetime.strptime(time_str2, '%Y-%m-%d %H:%M:%S.%f'))
tmp.output()
input("Press Enter to continue...")
