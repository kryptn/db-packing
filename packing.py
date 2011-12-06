#!/usr/bin/python

class Box(object):
   """ object for each box. """
   def __init__(self, width, height):
      width, height = int(width), int(height)
      self.width = width
      self.height = height
      self.area = width*height
      self.x = None
      self.y = None
   
   def rotate(self):
      """ switches height and width, essentially rotating. """
      self.width, self.height = self.height, self.width

   @property
   def box(self):
      """ returns appropriate tuple. """
      return (self.width, self.height)
   
   @property
   def coord(self):
      return (self.x, self.y)

   def __repr__(self):
      return str(self.box)

class Storage(object):

   def validate(self, x, y):
      """ checks current box locations """
      valid = False
      for i, box in enumerate(self.boxes):
         cond1 = box.x <= x < box.x+box.width
         cond2 = box.y <= y < box.y+box.height
         if cond1 and cond2:
            return i
      return valid

   def place(self, box, x, y):
      box.x = x
      box.y = y
      self.boxes.append(box)
      if self.width < box.x + box.width:
         self.width = box.x + box.width
      if self.height < box.y + box.height:
         self.height = box.y + box.height
   
   def display(self):
      """ builds 2d list with boxes """
      for x in xrange(self.height):
         for y in xrange(self.width):
            g = self.validate(y, x)
            if g:
               print g,
            else:
               print 'x',
         print


   def __init__(self):
      self.width = 0
      self.height = 0
      self.boxes = list()

class Pack(object):
   def load(self, sample):
      """ loads the sample list as input """
      boxes = list()
      for box in sample:
         boxes.append(Box(*tuple(box)))
      self.boxes = boxes
   
   def input(self):
      """ gets input """
      n = int(raw_input())
      boxes = list()

      for x in range(n):
         box = Box(*tuple(raw_input().split()))
         boxes.append(box)

      self.boxes = boxes
   
   def largest(self, boxes):
      """ finds the largest 'box' in the list """

      l = 0
      for i, x in enumerate(boxes):
         if x.area > boxes[l].area:
            l = i
      return l
   
   def listBoxes(self):
      """ lists the boxes """
      for i, box in enumerate(self.boxes):
         print i, box, box.area
   
   def align(self):
      """ aligns the boxes so they're 'standing' """
      for i, box in enumerate(self.boxes):
         if box.width > box.height:
            self.boxes[i].rotate()

   def build(self):
      boxes = self.boxes
      allocated = list()

      while boxes:
         box = boxes.pop(self.largest(boxes))


      
   def __init__(self, sample=None):
      if sample:
         self.load(sample)
      else:
         self.input()
      
      self.allocated = list()      
      self.optimal = sum([x.area for x in self.boxes])

if __name__ == '__main__':
   sample = [(1, 3), (2, 5), (6, 1), (2, 7), (8, 2), (9, 7), (3, 5)]
   a = Pack(sample)
   #a = Pack()
   s = Storage()
   s.place(Box(2,3),3,4)
   print 'boxes:', a.boxes
   print 'optimal:', a.optimal