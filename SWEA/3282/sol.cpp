#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

struct Product { int v, c; };

void solve() {
	int N, K;
	cin >> N >> K;
	vector<Product> arr;
	int v, c;
	for (int n = 0; n < N; n++) {
		cin >> v >> c;
		arr.push_back({ v, c });
	}
	vector<vector<int>> dp(N + 1, vector<int>(K + 1));
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= K; j++) {
			cout << i << j << '\n';
			// 현재 무게(i)에서 물건을 삽입해서 남은 중량이 0 이상이면
			// int w = i - arr[j-1].v
			// if (
			// dp[남은중량][N] + arr[j-1].c
			int w = j - arr[i - 1].v;
			if (arr[i - 1].v <= j) {
				dp[i][j] = max(arr[i - 1].c + dp[i - 1][w], dp[i - 1][j]);
			}
			else {
				dp[i][j] = dp[i - 1][j];
			}
		}
	}
	cout << dp[N][K] << "\n";
	return;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	FILE* fp;
	freopen_s(&fp, "input.txt", "r", stdin);

	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++) {
		cout << "#" << t << " ";
		solve();
	}
	return 0;
}