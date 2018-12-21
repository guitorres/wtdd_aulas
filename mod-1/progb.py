print 'Begin', __name__
from proga import fA

print 'Define fB'
def fB():
  print 'Dentro fB'
  #proga.fA()
  fA()

print 'Chama fB'
fB()

print 'End', __name__