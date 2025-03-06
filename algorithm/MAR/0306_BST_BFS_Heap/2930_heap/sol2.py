import sys
sys.stdin = open('input.txt', 'r')
#####################################


def sort_tree(idx):
    parent, child = idx // 2, idx


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans, que = [], []
    for i in range(N):
        tpl = tuple(map(int, input().split()))
        # print(que)
        # 삽입 조건
        if len(tpl) > 1:
            if not que:
                que.append(tpl[1])
                continue
            for j in range(len(que)-1, -1, -1):
                if que[j] > tpl[1]:
                    continue
                que.insert(j+1, tpl[1])
                break
            else:
                que.insert(0, tpl[1])
            continue
        # 삭제 조건
        if not que:
            ans.append(-1)
            break
        ans.append(que.pop())
    print(f'#{tc}', *ans)

