import sys
sys.stdin = open('input.txt', 'r')
#####################################

# 중위 순회
def search(node):
    # 노드의 value가 글자만 들어있는 경우
    if len(tree[node]) == 1:
        # 출력 변수에 저장
        ans_a.extend(tree.get(node))
        return
    # 노드의 value 길이가 2 이상인 경우 리스트를 순회
    for n in tree[node]:
        # 숫자일 경우만 재귀함수 호출
        if n.isnumeric():
            search(n)
        # 아닐 경우 중위순회로 글자를 추가
        else:
            ans_a.append(n)
    return


T = 10
for tc in range(1, T+1):
    # 노드의 수
    N = int(input())
    tree = {}
    ans_a = []
    for i in range(N):
        # 노드의 번호와 나머지를 입력
        idx, *temp = input().split()
        # 글자 이외에 자식 노드의 번호가 주어질 때
        if len(temp) > 1:
            # 중위 순회를 위해 문자를 숫자 중간에 삽입
            word, *temp = temp
            temp.insert(1, word)
        # 딕셔너리에 노드 번호를 키로 하는 리스트 저장
        tree[idx] = temp
    # 함수 호출
    search('1')
    print(f'#{tc}', ''.join(ans_a))
