import sys
sys.stdin = open('2851.txt', 'r')


m = [int(input()) for _ in range(10)]
s = 0
for i in range(10):
    s += m[i]
    if s == 100:
        break
    if i != 9:
        # 다음 숫자를 더했을 때 100보다 크다면
        # 근데 100 - 현재 숫자의 절대값과 다음 숫자를 더한 값을 100으로 뺀
        # 절대값의 차이가 작은 쪽을 선택한다.
        # 절대값의 차이가 같다면, 큰쪽을 선택한다.
        t = s + m[i+1]
        if t > 100:
            ut, us = abs(100-t), abs(100-s)
            # t를 선택하는 순간: 같거나, ut가 더 작을 때
            if ut == us or ut < us:
                s = t
            break
print(s)


