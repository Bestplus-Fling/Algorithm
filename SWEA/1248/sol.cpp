#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int V, E, s1, s2;
struct Node {
	int left = -1, right = -1, parent = -1;
};
int cnt = 0;

void order(vector<Node>& tree, int vtx) {
	// 전위든 중위든 후위든 상관없음
	Node& cur = tree[vtx];
	//cout << "현재 노드" << vtx << ", 왼쪽: " << cur.left << ", 오른쪽: " << cur.right << ", 부모: " << cur.parent << "\n";
	if (cur.left != -1) order(tree, cur.left);
	cnt++;
	if (cur.right != -1) order(tree, cur.right);
}

int check(vector<Node>& tree) {
	// 자식부터 시작해서 부모를 찾아간다.
	// 어떻게?
	// s1의 부모를 먼저 찾는다
	// s2를 순회하면서 s1과 공통된 부모가 있는지 확인하면서 이동, 부모를 찾으면 부모로 지목된 곳부터 자식의 수를 센다(본인 포함).
	unordered_set<int> set;
	int vtx = s1;
	// 1. s1의 부모 순회
	while (vtx != -1) {
		Node& cur = tree[vtx];
		set.insert(cur.parent);
		vtx = cur.parent;
	}

	// 2. s2의 부모 순회 과정에서 공통 부모를 찾으면 break
	vtx = s2;
	while (vtx != -1) {
		Node& cur = tree[vtx];
		if (set.find(cur.parent) != set.end()) {
			return cur.parent;
		}
		vtx = cur.parent;
	}
	return -1;
}

void solve() {
	cin >> V >> E >> s1 >> s2;
	vector<Node> tree(V+1);
	int p, c;
	for (int e = 0; e < E; e++) {
		cin >> p >> c;
		//cout << "부모: " << p << ", 자식: " << c << "\n";
		Node& cur = tree[p];
		if (cur.left == -1) cur.left = c;
		else cur.right = c;
		tree[c].parent = p;
	}
	int res_p = check(tree);
	cnt = 0;
	order(tree, res_p);
	cout << res_p << " " << cnt << "\n";
	return;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	FILE* fp;
	freopen_s(&fp, "input.txt", "r", stdin);
	/*
		가장 가까운 공통 조상을 찾기
		그 정점을 루트로 하는 서브 트리의 크기를 알아낸다.

		이진트리
	*/
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cout << "#" << tc << " ";
		solve();
	}
	return 0;
}