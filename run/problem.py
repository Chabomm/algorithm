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
        


