import time
import random

#data input



#sleep 5 sec before starting first solution time test

time.sleep(5)

#start of first solution time test

print('first solution:')

start = time.time()

#first solution



#end of first solution time test

end1 = time.time() - start

#sleep 5 sec before starting second solution time test

time.sleep(5)

print()

#start of second solution time test

print('second solution:')

start = time.time()

#second solution



#end of first solution time test

end2 = time.time() - start

#results of time tests

print()

#result of first solution time test

print('---time---', end1, '---first---')

#result of second solution time test

print('---time---', end2, '---second---')