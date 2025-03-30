import sys
sys.stdin = open("2588.txt")

mul = int(input())
div = int(input())
div100, div1 = div//100, (div%100)%10
div10 = (div - div100*100 - div1)//10

print(mul*div1, (mul*div10), (mul*div100), mul*div, sep='\n')
