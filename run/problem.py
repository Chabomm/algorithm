# beakjoon 2525
# a, b = map(int, input().split())
# c = int(input())
# a += c//60
# b += c%60
# if b >= 60 :
#     a += 1
#     b -= 60
# if a > 23 :
#     a -= 24
# print(a, b)

#beakjoon 2480
# a, b, c = map(int, input().split())
# if a == b == c :
#     print(10000+a*1000)
# elif a == c :
#     print(1000+a*100)
# elif b == c :
#     print(1000+b*100)
# elif a == b :
#     print(1000+a*100)
# elif a != b != c :
#     print(max(a,b,c)*100)

# # beakjoon 2739
# A = int(input())
# for i in range(9):
#     print(str(A) + " * " + str(i+1) + " = " + str(A*(i+1)))

# beakjoon 10950
# T = int(input())
# for _ in range(T) :
#     A, B = map(int, input().split())
#     print(A+B)

# # beakjoon 8393
# n = int(input())
# a = int()
# for i in range(n):
#     a += i+1
# print(a)
# # or
# print(sum(range(1, n+1)))

# # beakjoon 25304
# X = int(input())
# N = int(input())
# total = int()
# for _ in range(N):
#     a, b = map(int, input().split())
#     total += a*b
    
# if X == total :
#     print("Yes")
# else :
#     print("No")

# beakjoon 25314
# N = int(input())
# a = N//4
# print("long " * a + "int")
# # for i in range(N//4):
    
# ----- beackjoon 15552 -----
import sys

# T = int(sys.stdin.readline().rstrip())

# for _ in range(T):
#     A, B = map(int, sys.stdin.readline().rstrip().split())
#     print(A+B)

# ----- beakjoon 11021 -----
# T = int(sys.stdin.readline().rstrip())
# for i in range(T):
#     A, B = map(int, sys.stdin.readline().rstrip().split())
#     print("Case #"+str(i+1)+": "+ str(A+B))

#  ----- beakjoon 11022 -----
# T = int(sys.stdin.readline().rstrip())
# for i in range(T):
#     A, B = map(int, sys.stdin.readline().rstrip().split())
#     print("Case #"+str(i+1)+": "+str(A)+" + "+str(B)+ " = "+ str(A+B))

# ----- beakjoon 2438 -----
# A = int(input())
# for i in range(A):
#     print((i+1)*"*")

# ----- beakjoon 2439 -----
# A = int(input())
# for i in range(A):
#     print(" "*(A-(i+1)) + (i+1)*"*")

# ----- beakjoon 10952 -----
# while True:  # True or 1 로 적으면 계속 반복!!
#     A, B = map(int, input().split())
#     if A == 0 and B == 0 :
#         break
#     else:
#         print(A+B)

# ----- beakjoon 10951 -----
# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
        # break

# ----- beakjoon 10807 -----
# N = int(input())
# A = list(map(int, input().split()))
# V = int(input())

# print(A.count(V))
# !!!!!!! count: python 리스트 내장 메소드 count()는 매개변수로 입력된 값이 리스트 안에 몇개 있는지 세어 반환해준다.
# counter = 0

# for i in A:
#     if i == V :
#         counter += 1
# print(counter)

# ----- beakjoon 10871 -----
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# for i in A:
#     if i < X :
#         print(i, end=" ")

# ----- beakjoon 10818 -----
# N = int(input())
# list_a = list(map(int, input().split()))
# print(min(list_a), max(list_a))

# ----- beakjoon 2562 -----
# numbers = []
# for _ in range(9):
#         try:
#                 numbers.append(int(input()))
#         except:
#                 break

# print(max(numbers))
# print(numbers.index(max(numbers))+1)

# ---- beakjoon 10810 -----

# 처음 시작 시 n과 m을 입력받고 길이가 n인 리스트를 만든다.
# n, m  = map(int, input().split()) #n, m 입력받기
# basket = [0]*n # 길이가 n인 리스트 생성

# for _ in range(m): # m번 만큼 공을 넣을꺼니까
#         i, j, k = map(int, input().split())
#         for target in range(i,j+1): # j까지면 j앞까지만 해당되므로 j+1을 해준다
#                 basket[target-1] = k #바구니를 k로 치환, basket(리스트 인덱스)는 0부터 시작하고 target은 1부터 시작하니까 -1로 싱크를 맞춰준다
#                 print(basket)

# basket = map(str,basket) #공백구분을 해주기 위해 str로 만들어준다
# print(" ".join(basket)) #join함수를 이용하여 출력



# N, M = map(int, input().split())
# list_a = [0]*N

# for _ in range(M) :
#         i, j, k = map(int, input().split())
#         for target in range(i, j+1) :
#                 list_a[target-1] = k
        
# list_a = map(str,list_a)
# print(" ".join(list_a))

# ---- beakjoon 10813 -----
# N, M = map(int, input().split())
# basket = [i for i in range(1, N+1)]

# for _ in range(M):
#         i, j = map(int, input().split())
#         basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

# basket = map(str, basket)
# print(" ".join(basket))


# ---- beakjoon 5597 -----

list_a = [i for i in range(1, 31)]  # 학생이 30명이니까 1 ~ 30까지의 리스트를 만들어준다
for i in range(28): # 28명만 과제 제출을 했으니 28번만 돌면 됨
        data = int(input())  #과제를 제출한 28명 입력받음
        list_a.remove(data) # 1~30에서 제출한 28명을 지운다

# list_a = map(str, list_a)
# print("\n".join(list_a))
print(min(list_a))
print(max(list_a))







    
        


