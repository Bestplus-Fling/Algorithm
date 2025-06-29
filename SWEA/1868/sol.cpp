#include <iostream>
#include <string>
#include <vector>
#include <deque>
using namespace std;

int N;

int dx[8] = { 0, 1, 0, -1, 1, 1, -1, -1 };
int dy[8] = { 1, 0, -1, 0, 1, -1, 1, -1 };
struct Node { int x, y; };

void push_zero(const vector<vector<char>>& grid, vector<vector<bool>>& visited, int i, int j) {
	deque<Node> dq;
	dq.push_back({ i, j });
	visited[i][j] = true;

	while (!dq.empty()) {
		Node cur = dq.front(); dq.pop_front();
		for (int k = 0; k < 8; k++) {
			int nx = cur.x + dx[k], ny = cur.y + dy[k];
			if (nx >= N || nx < 0 || ny >= N || ny < 0 || visited[nx][ny]) continue;
			// 0은 q에 삽입, 0 주변은 밝히긴 해야 함
			visited[nx][ny] = true;
			if (grid[nx][ny] == '0') dq.push_back({nx, ny});
		}
	}
	return;
}

int solve() {
	cin >> N;
	vector<vector<char>> grid(N, vector<char>(N));

	// 입력
	string input;
	for (int i = 0; i < N; i++) {
		cin >> input;
		for (int j = 0; j < N; j++) {
			grid[i][j] = input[j];
		}

	}

	// 8방향에 존재하는 폭탄 개수 누적
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++) {
			int cnt = 0;
			if (grid[i][j] == '*') continue;
			for (int k = 0; k < 8; k++) {
				int ni = i + dx[k], nj = j + dy[k];
				if (ni >= N || ni < 0 || nj >= N || nj < 0) continue;
				if (grid[ni][nj] == '*') cnt++;
			}
			grid[i][j] = cnt + '0';
		}

	// grid 확인용
	//for (int i = 0; i < N; i++) {
	//	for (int j = 0; j < N; j++) {
	//		cout << grid[i][j];
	//	}
	//	cout << "\n";
	//}

	// 0을 누르는 횟수 + 폭탄을 제외한 행의 개수
	// 0을 누르는 건 bfs로 확인
	int push_count = 0;
	int not_visit = 0;
	vector<vector<bool>> visited(N, vector<bool>(N));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (grid[i][j] == '0' && !visited[i][j]) {
				push_zero(grid, visited, i, j);
				push_count++;
			}
		}
	}
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			if (!visited[i][j] && grid[i][j] != '*') not_visit++;
	
	return push_count + not_visit;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	FILE* fp;
	freopen_s(&fp, "input.txt", "r", stdin);

	/*
	 R * C 크기의 표를 이용
	근처 8방향에 지뢰가 있는지 없는지 확인
	지뢰 개수만큼 grid에 표시
	*/

	int T;

	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cout << "#" << tc << " " <<  solve() << "\n";
	}
	return 0;
}