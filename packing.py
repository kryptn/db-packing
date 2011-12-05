#!/usr/bin/python

class Pack(object):
	def load(self, boxes):
		pass
	
	def rotate(self, box):
		pass
	
	def input(self):
		""" gets input """
		n = int(raw_input())
		boxes = list()

		for x in range(n):
			box = raw_input().split()
			box = [int(x) for x in box]
			boxes.append(tuple(box))

		self.boxes = boxes
		self.optimal = sum(map(lambda x: x[0]*x[1], boxes))

	def __init__(self):
		self.input()

if __name__ == '__main__':
	a = Pack()
	print 'boxes:', a.boxes
	print 'optimal:', a.optimal