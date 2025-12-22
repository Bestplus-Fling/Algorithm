import sys
sys.stdin = open('input.txt', 'r')
#########################################

T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    # print(N, Ai, Bi)
    # Ai의 첫 번째 칸과 Bi의 첫 번째 칸을 비교
    # 다르면 해당 위치의 스위치를 변경 해야 함
    #   스위치를 변경하게 되면 해당 위치부터 N까지의 켜짐 => 꺼짐 /  꺼짐 => 켜짐 변경
    # 같으면 스위치 변경할 필요가 없음
    count = 0
    for i in range(N):
        if Ai[i] == Bi[i]:
            continue
        for j in range(i, N):
            if Ai[j] == 1:
                Ai[j] = 0
            else:
                Ai[j] = 1
        count += 1
    print(f'#{tc} {count}')
