import sys

# 로컬 테스트용 (제출 시 주석 처리하거나 경로 수정 필요)
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 문제 번호: BOJ/12851
# 작성 코드 시작
max_val = 100010

def bfs():
    if n >= k:
        return n - k, 1

    visited = [-1] * max_val
    q = [n]
    visited[n] = 0
    cnt = 0
    min_time = float("inf")

    idx = 0
    while q:
        curr = q[idx]
        idx += 1

        if visited[curr] > min_time:
            break

        for v in (curr * 2, curr + 1, curr - 1):
            if 0 <= v < max_val:
                if visited[v] == -1 or visited[v] == visited[curr] + 1:
                    if v == k:
                        min_time = visited[curr] + 1
                        cnt += 1

                    visited[v] = visited[curr] + 1
                    q.append(v)
    return min_time, cnt

n, k = map(int, input().split())
time, count = bfs()
print(time, count, sep="\n")