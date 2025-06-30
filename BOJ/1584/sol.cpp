#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

const int INF = 1e9;
const int MAX = 501;
const int dx[4] = { 0, 1, 0, -1 };
const int dy[4] = { 1, 0, -1, 0 };
vector<vector<int>> grid(MAX, vector<int>(MAX));
struct Node {
	int d, x, y;
	bool operator<(const Node& other) const {
		return d > other.d;
	}
};

void input(int x1, int x2, int y1, int y2, int num) {
	for (int r = x1; r <= x2; r++) {
		for (int c = y1; c <= y2; c++) {
			grid[r][c] = num;
		}
	}
}

void dijkstra() {
	priority_queue<Node> pq;
	vector<vector<int>> dist(MAX, vector<int>(MAX, INF));
	pq.push({ 0, 0, 0 });
	dist[0][0] = 0;
	while (!pq.empty()) {
		Node cur = pq.top(); pq.pop();
		if (cur.d > dist[cur.x][cur.y]) continue;
		for (int k = 0; k < 4; k++) {
			int nx = cur.x + dx[k], ny = cur.y + dy[k];
			if (nx >= MAX || nx < 0 || ny >= MAX || ny < 0) continue;
			int nd = cur.d + grid[nx][ny];
			if (dist[nx][ny] <= nd) continue;
			//cout << "next" << nx << ", " << ny << '\n';
			pq.push({ nd, nx, ny });
			dist[nx][ny] = nd;
		}
	}
	if (dist[500][500] == INF) cout << -1;
	else cout << dist[500][500];
	cout << "\n";
	return;
}

void solve() {
	int a, b, x1, x2, y1, y2;
	int r1, r2, c1, c2;
	cin >> a;
	for (int i = 0; i < a; i++) {
		cin >> x1 >> y1 >> x2 >> y2;
		r1 = min(x1, x2), r2 = max(x1, x2);
		c1 = min(y1, y2), c2 = max(y1, y2);
		input(r1, r2, c1, c2, 1);
	}
	cin >> b;
	for (int i = 0; i < b; i++) {
		cin >> x1 >> y1 >> x2 >> y2;
		r1 = min(x1, x2), r2 = max(x1, x2);
		c1 = min(y1, y2), c2 = max(y1, y2);
		input(r1, r2, c1, c2, INF);
	}
	dijkstra();
	return;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	FILE* fp;
	freopen_s(&fp, "input.txt", "r", stdin);

	solve();
	return 0;
}