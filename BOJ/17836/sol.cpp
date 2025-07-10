#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int n, m, t, res = 10009;
vector<vector<int>> v;
struct Node { int x, y, t; bool g; };
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

void bfs() {
	queue<Node> q;
	q.push({ 0, 0, 0, 0 });
  // 처음에 3차원 생각해놓고 되겠지 하는 안일함은 없어야 한다.
	vector<vector<vector<bool>>> visited(n, vector<vector<bool>>(m, vector<bool>(2)));
	visited[0][0][0] = true;
	while (!q.empty()) {
		Node cur = q.front(); q.pop();
		if (cur.t > t) continue;
		if (cur.x == n - 1 && cur.y == m - 1) {
			res = min(res, cur.t);
			continue;
		}
		if (v[cur.x][cur.y] == 2) cur.g = true;
		for (int k = 0; k < 4; ++k) {
			int nx = cur.x + dx[k], ny = cur.y + dy[k];
			if (nx >= n || nx < 0 || ny >= m || ny < 0) continue;
			if (visited[nx][ny][cur.g] || (!cur.g && v[nx][ny] == 1)) continue;
			q.push({ nx,ny,cur.t + 1, cur.g });
			visited[nx][ny][cur.g] = true;
		}
	}
	return;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	FILE* fp;
	freopen_s(&fp, "input.txt", "r", stdin);

	cin >> n >> m >> t;
	v = vector<vector<int>>(n, vector<int>(m));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> v[i][j];
		}
	}

	bfs();
	string ans = res == 10009 ? "Fail" : to_string(res);
	cout << ans << "\n";
	return 0;
}