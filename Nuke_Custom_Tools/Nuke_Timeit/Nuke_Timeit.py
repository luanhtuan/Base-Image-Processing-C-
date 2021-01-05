
# Add Timeit - STEP 1

import random
import  timeit

txt = nuke.getInput('how many objects', 'type value')
list = []
for i in range(int(txt)):
    a = nuke.nodes.Sphere()
    posx = float(float(i) * float(random.uniform(1,3)))
    posy = float(random.uniform(2.5,5))
    rndNum = timeit.timeit('"-".join(str(i) for i in range (100))',
                   number = 10000)
    a['translate'].setValue([posx,posy,0])
    a['translate'].setExpression('sin((frame+1000)/'+str(rndNum)+')'+'*'+str(rndNum*2),2)
    a['uniform_scale'].setValue(0.5)
    a.setSelected(True)
    k = nuke.selectedNodes()
b = nuke.createNode("Scene")
x = 0
for i in k:
  b.setInput(x,i)

# Add Timeit - STEP 2


import random
import  timeit

txt = nuke.getInput('how many objects', 'type value')
list = []
for i in range(int(txt)):
    a = nuke.nodes.Sphere()
    posx = float(float(i) * float(random.uniform(1,3)))
    posy = float(random.uniform(2.5,5))
    rndNum = timeit.timeit('"-".join([str(i) for i in range (100)])',
                            number = 10000)
    a['translate'].setValue([posx,posy,0])
    a['translate'].setExpression('sin((frame+1000)/'+str(rndNum)+')'+'*'+str(rndNum*2),2)
    a['uniform_scale'].setValue(0.5)
    a.setSelected(True)
    k = nuke.selectedNodes()
b = nuke.createNode("Scene")
x = 0
for i in k:
  b.setInput(x,i

# Add Timeit - STEP 3

  import random
  import timeit

  txt = nuke.getInput('how many objects', 'type value')
  list = []
  for i in range(int(txt)):
      a = nuke.nodes.Sphere()
  posx = float(float(i) * float(random.uniform(1, 3)))
  posy = float(random.uniform(2.5, 5))
  rndNum = timeit.timeit('"-".join(map(str, range(100)))',
                         number=10000)
  a['translate'].setValue([posx, posy, 0])
  a['translate'].setExpression('sin((frame+1000)/' + str(rndNum) + ')' + '*' + str(rndNum * 2), 2)
  a['uniform_scale'].setValue(0.5)
  a.setSelected(True)
  k = nuke.selectedNodes()
  b = nuke.createNode("Scene")
  x = 0
  for i in k:
      b.setInput(x, i)
