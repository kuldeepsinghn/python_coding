""" it is an abstract data structure
    that associates  keys [keys are unique]     to values
    abstrcly we think that it is the collection of (key value) pairs
    sometimes we called it maps and dictionary
      can be implemented in differnt concerte ways
       they support :- adding/removing elements
                    -modify asoociated value
                    lookup value of using key """


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)