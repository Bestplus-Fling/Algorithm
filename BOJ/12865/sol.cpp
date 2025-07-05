#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void solve() {
	int N, K;
	cin >> N >> K;
	vector<int> val(N);
	vector<int> wt(N);
	for (int i = 0; i < N; i++) {
		cin >> wt[i] >> val[i];
	}

	vector<vector<int>> dp(N+1, vector<int>(K+1));
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= K; j++) {
			int w = j - wt[i - 1];
			if (w >= 0) dp[i][j] = max(dp[i - 1][j], dp[i-1][w] + val[i - 1]);
			else dp[i][j] = dp[i - 1][j];
		}
	}

	for (int i = 0; i <= N; i++)
		for (int j = 0; j <= K; j++)
			cout << dp[i][j] << (j == K ? "\n" : " ");

	cout << dp[N][K] << "\n";

	return;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	FILE* fp;
	freopen_s(&fp, "input.txt", "r", stdin);
	solve();
	return 0;
}