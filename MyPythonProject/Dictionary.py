friends={
    'tom':'3342',
    'jerry':'432',
    'tom':'7899'

}

print(friends) #{'tom': '3342', 'jerry': '432'}  key must be unique otherwise it will be updated with latest value entry

#retrieving element
print(friends['tom']) #7899

#addmin new element to dictionary
friends['satya']='790580'
print(friends) #{'tom': '7899', 'jerry': '432', 'satya': '790580'}

#modify element in dictionary
friends['satya']='85531'
print(friends) #{'tom': '7899', 'jerry': '432', 'satya': '85531'}

#delete elment from dictionary
del friends['jerry'] #deletes key on basis of key
print(friends) #{'tom': '7899', 'satya': '85531'}

#looping in dictionary
dict={
    'a':'10',
    'b':'20',
    'c':'30',
    'd':'40'
}

print(dict) #{'a': '10', 'b': '20', 'c': '30', 'd': '40'}

for x in dict:
    print(x, ":" ,dict[x])

#size of dictionary or length of dictionary
print(len(dict))  #4

d1={'satya':'123',
    'ankit':'456'}
d2={'ankit':'456',
    'satya':'123'}
print(d1 == d2) #True   order is not important
print(d1 != d2) #False


