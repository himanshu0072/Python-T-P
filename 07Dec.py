dic1={"mac":'123', 'john':'456', "mary":'789', "joe":'000', "jane":'111', "jill":'222', "jack":'333', "james":'444', "jim":'555', "jenny":'666', "jerry":'777', "julia":'888', "joseph":'999'}
dic2={}
for key, value in dic1.items():
    print(key, value)
    dic2[value]=key
print(dic2)