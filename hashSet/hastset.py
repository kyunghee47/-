s = set()
s.add(10)
s.add(20)
s.add(30)

s.remove(20)
print(s)

for num in s:
    print(num)

print(10 in s)
print(20 in s)

# 키와 벨류로 이루어짐 
m = dict()
m['a'] = 100
print(m.get('a'))
#없는 값을 넣을때 get과 []의 차이점
print(m.get('b'))
#print(m['b'])

#해쉬맵은 딕셔너리 
print('a' in m)
print('b' in m)

for k, v in m.items():
    print(k,v)

print(len(m))