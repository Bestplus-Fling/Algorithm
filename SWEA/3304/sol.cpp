#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void solve() {
	string a, b;
	cin >> a >> b;
	int n = a.size() + 1, m = b.size() + 1; 
	vector<vector<int>> dp(n, vector<int>(m));
	for (int i = 1; i < n; i++) {
		for (int j = 1; j < m; j++) {
			if (a[i-1] == b[j-1]) dp[i][j] = dp[i - 1][j - 1] + 1;
			else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
		}
	}
	cout << dp[n-1][m-1] << "\n";
	return;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	FILE* fp;
	freopen_s(&fp, "input.txt", "r", stdin);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cout << "#" << tt << " ";
		solve();
	}
	return 0;
}