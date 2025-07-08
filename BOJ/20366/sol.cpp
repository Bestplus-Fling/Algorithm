#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;


int N;
vector<int> H;
vector<tuple<int, int, int>> snowman;

bool is_valid(int i, int j, int x, int y) {
	return i != x && i != y && j != x && j != y;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	FILE* fp;
	freopen_s(&fp, "input.txt", "r", stdin);

	cin >> N;
	H.resize(N);
	for (int i = 0; i < N; i++)
		cin >> H[i];

	for (int i = 0; i < N; ++i) 
		for (int j = i + 1; j < N; ++j) 
			snowman.push_back({ H[i] + H[j], i, j });
	sort(snowman.begin(), snowman.end());

	int ans = 1e9, res, j = 0, sz = snowman.size();
	int h1, a1, b1;
	int h2, a2, b2;
	for (int i = 0; i < sz; ++i) {
		tie(h1, a1, b1) = snowman[i];
		tie(h2, a2, b2) = snowman[j];
		while (j < sz && is_valid(a1, b1, a2, b2)) {
			res = abs(h2 - h1);
			if (res > ans) break;
			ans = min(ans, res);
			j++;
			tie(h2, a2, b2) = snowman[j];
		}
	}

	cout << ans << "\n";

	return 0;
}