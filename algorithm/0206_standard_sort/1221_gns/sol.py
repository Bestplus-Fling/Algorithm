import sys
sys.stdin = open("input.txt")

dict_num = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
dict_str = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

T = int(input())
for tc in range(1, T+1):
    t_num, N = input().split()
    N = int(N)
    arr = input().split()
    num_list = []
    string_list = []
    for token in arr:
        num_list.append(dict_num.get(token))
    for num in sorted(num_list):
        string_list.append(dict_str.get(num))
    print(f'#{tc}', ' '.join(string_list))

