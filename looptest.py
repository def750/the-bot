args = ['-u', '<@!613889661793992719>', '-n', '1', '-msg', 'Hello', 'world!']

inp = args
allowed_args = ["-u", "-n", "-msg"] 
dic = {}
current_key = None
for el in inp:
    if el in allowed_args:
        current_key = el
        dic[current_key] = []
    else:
        dic[current_key].append(el)
    
for key, val in dic.items():
    dic[key] = " ".join(val)

print(dic)