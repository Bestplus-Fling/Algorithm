import sys
sys.stdin = open("2869.txt")

a, b, v = map(int, input().split())
t = a-b
ans = (v-a) // t + (1 if (v-a) % t else 0)
print(ans+1)


# i = v // a + (1 if v % a != 0 else 0)
# print(i)
# j = v // b
# print(j)
