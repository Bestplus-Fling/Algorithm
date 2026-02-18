import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: 17478
# 작성 코드 시작
def dfs(depth):
    s = "____" * depth
    print(f'{s}"재귀함수가 뭔가요?"')
    if n == depth:
        print(f'{"____" * n}"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(f'{"____" * n}라고 답변하였지.')
        return

    print(f'{s}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(f'{s}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(f'{s}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    dfs(depth + 1)
    print(f'{s}라고 답변하였지.')


n = int(input())

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
dfs(0)