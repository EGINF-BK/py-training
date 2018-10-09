#1 unpacking
list1 = ['David','John','Isick']
p1, p2, p3 = list1
print p1, p2, p3

#2  if statement
fruit_list = ["apple","banana","watermelon","penapple"]
fruit_in_hands = ''
if fruit_in_hands not in fruit_list:
    print "yes, no fruit in our hands"

#3  string operation
color = ['red', 'yellow', 'blue', 'white']
result = ''.join(color)
print result

#4  list: iter list and index
items = 'zero one two three'.split()
for i, item in enumerate(items, start=3):
    print i,item

#5  any/all in if/else
color = ['red', 'yellow', 'blue', 'white']
if any( item == 'blue' for item in color):
    print "we'll buy this %s one" % item,