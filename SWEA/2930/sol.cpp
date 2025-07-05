#include <iostream>
#include <queue>
using namespace std;

void solve() {
	int N;
	cin >> N;
	priority_queue<int> pq;
	int c, n;
	for (int i = 0; i < N; i++) {
		cin >> c;
		if (c == 1) {
			cin >> n;
			pq.push(n);
		}
		else {
			if (!pq.empty()) {
				cout << " " << pq.top();
				pq.pop();
			}
			else {
				cout << " " << -1;
			}
		}
	}
	return;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	FILE* fp;
	freopen_s(&fp, "input.txt", "r", stdin);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "#" << t;
		solve();
		cout << "\n";
	}

	return 0;
}