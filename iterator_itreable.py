#iterables and iterator

number=[1,2,3,4,5,6] #list,tuple,string-----iterables
squares=map(lambda a:a**2,number) #iterator
print(squares) #iterator is an object
print(iter(number)) #iterables is an object

for i in number:
    print(i)
for i in number:
    print(i)

'''An iterable returns an iterator, and calling next on this iterator returns the next item in the sequence'''

number_iter=iter(number) #iterable is returning iterator //An iterable object calls its __iter__ method to return an iterator
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
# print(next(number_iter))  /// throw error

print(next(squares))
print(next(squares))
print(next(squares))
