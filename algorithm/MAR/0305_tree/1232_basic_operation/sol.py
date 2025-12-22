import sys
sys.stdin = open('input.txt', 'r')
#####################################


def search(node):
    # node 를 key 로 하는 value 의 길이가 1(= leaf node)
    if len(tree[node]) == 1:
        # 입력을 str 로 했기 때문에 int 로 형변환 후 return
        return int(tree[node][0])
    nums = []
    # 리스트 요소가 숫자일 때만 재귀함수 호출
    for j in tree[node]:
        if j.isnumeric():
            nums.append(search(j))
    # 부호 별 연산
    if tree[node][0] == '+':
        now = nums[0] + nums[1]
    elif tree[node][0] == '-':
        now = nums[0] - nums[1]
    elif tree[node][0] == '*':
        now = nums[0] * nums[1]
    else:
        now = nums[0] / nums[1]
    # 연산 결과를 반환
    return now


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    tree = {}
    for i in range(N):
        # 노드의 번호와 자식노드, root 의 부호를 입력
        idx, *temp = arr[i]
        # 딕셔너리에 저장
        tree[idx] = tree.get(idx, []) + temp
    # 함수의 반환값을 int 변환
    print(f'#{tc}', int(search('1')))

