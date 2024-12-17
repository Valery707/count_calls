calls = 0
def count_calls():
    global calls
    calls +=1
    return calls

def string_info(string):
    tuple = len(string),string.upper(),string.lower()
    count_calls()
    return tuple
a = string_info('capibara')
e = string_info('new year')
print(a)
print(e)

def is_contains (string, list_to_search):
    count_calls()
    return string in list_to_search
c = is_contains('aaa',['aaa',1,2])
d = is_contains('bbbb', '1,2,3')
print(c)
print(d)

print (count_calls()-1)
