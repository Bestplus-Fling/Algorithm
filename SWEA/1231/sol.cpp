#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Node { int left = 0, right = 0; char str = 0; };

int N;

string res;

void in_order(vector<Node>& tree, int vtx) {
	//cout << "현재 정점: " << vtx << "\n";
	const Node& cur = tree[vtx];
	if (cur.left != 0) in_order(tree, vtx * 2);
	res += cur.str;
	if (cur.right != 0) in_order(tree, (vtx * 2) + 1);
	return;
}

void solve() {
	cin >> N;
	vector<Node> tree(N+1);
	int idx;
	for (int i = 0; i < N; i++) {
		Node input;	
		cin >> idx >> input.str;
		if (idx * 2 <= N) cin >> input.left;
		if ((idx * 2) + 1 <= N) cin >> input.right;
		tree[idx] = input;
	}

	res = "";
	in_order(tree, 1);
	return;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	FILE* fp;
	freopen_s(&fp, "input.txt", "r", stdin);

	for (int tc = 1; tc <= 10; tc++) {
		solve();
		cout << "#" << tc << " " << res << "\n";
	}

	return 0;
}