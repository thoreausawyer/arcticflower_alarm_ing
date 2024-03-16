# slicing
var = "1234567890"
print("")
print("슬라이싱")
print(var[0:10])
print(var[1:10])

# formatting
return_rate_ago = "5"
return_rate = "10"
message = "수익률 : {}%, 직전 수익률 : {}%".format(return_rate_ago,return_rate)
print("")
print("포맷팅")
print(message)

# split
message2 = "1,2,3,4,5"
message2 = message2.split(",")
print("")
print("스플리트")
print(message2)

# tuple (값, 값, 값, 값..) (squence datatype) (타입 제한 없음) (삽입 / 삭제 불가능)
a = (1, "hello", 1/4, True)
conin_closes_tuple = (40000, 50000, 60000, 61000, 76000, 80000, 82000, 83000)
print("")
print("튜플(삽입 / 삭제 불가능)")
print(a)
print(conin_closes_tuple[7])
# conin_closes_tuple[7] = 9000
print(conin_closes_tuple[7])

# list [값, 값, 값, 값..] (squence datatype) (타입 제한 없음) (삽입 / 삭제 가능)
b = [1, "hello", 1/4, False]
conin_closes_list = [40000, 50000, 60000, 61000, 76000, 80000, 82000, 83000]
print("")
print("리스트(삽입 / 삭제 / 수정(.append) 가능)")
print(b)
print(conin_closes_list[7])
conin_closes_list[7] = 90000
print(conin_closes_list[7])

# list.append(값)
c = [1, 2, 3]
print("")
print("리스트.append(값) (리스트 타입에만 사용가능) (점 찍어 사용)")
print(c)
c.append(4)
print(c)


# list.del(값)
print("")
print("del 변수[인덱스]")
print(c)
del c[1]
print(c)

# packing (4개의 서로 다른 타입의 데이터를 하나의 변수에 저장)
print("")
print("packing")
print("ex) e = [1, 'hello', 1/4, True]")
e = [1, 'hello', 1/4, True]

# unpacking (packing된 값들을 풀어서 새로운 변수에 저장)
print("")
print("unpacking")
print("ex) a, b, c, d = e (unpacking할 데이터 수와 이를 저장할 새로운 변수의 수가 동일 해야 함)")
a, b, c, d = e
print(a ,b ,c ,d)

# 튜플도 packing unpackig 가능

# []을 이용한 새로운 조건에 속하는 리스트 만들기
old_list = [1, 2, 3, 4, 5]
# new_list = [새로운_변수명 for 새로운_변수명 in old_list]
# old_list에 있는 요소 [1, 2, 3, 4, 5]를 반복하겠다는 의미
# 새로운_변수명은 임의로 순서대로 꺼내는 1, 2, 3, 4, 5를 지칭하는 변수 -> 아무거나 사용 가능
print("")
print("[]을 이용한 새로운 조건 for ~ in")
print(d)
new_list = [donghoon for donghoon in old_list]
new_list.append(6)
print(old_list)
print(new_list)
# if 조건문
new_list2 = [donghoon for donghoon in old_list if False]
print(old_list)
print(new_list2)
new_list2 = [donghoon for donghoon in old_list if True]
print(new_list2)

# 딕셔너리 dictionary




