for tc in range(1, int(input())+1):
    ans_price, ans_name = -float('inf'), ''
    for i in range(int(input())):
        price, name = input().split()
        price = int(price)
        if ans_price < price:
            ans_price = price
            ans_name = name
    print(ans_name)


