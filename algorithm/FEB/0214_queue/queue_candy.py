total_candy = 20 # 총 마이쮸 개수

queue = [] # 사람들을 저장할 큐
cnt_person = 1
queue.append((1, 1))

last_person = None  # 마지막으로 마이쮸를 받은 사람을 저장할 변수

while total_candy > 0:
    # queue에 줄 선 사람들한테 분배해야 한다
    # pop(0)을 이용해 가장 앞에 있는 데이터를 가져온다
    # person : 받을 사람, cnt : 받을 개수
    person, ans = queue.pop(0)

    # 남아 있는 캔디의 수가 줘야 하는 캔디 수보다 적으면, 지금 받은 사람이 마지막으로 받은 사람이다.
    # 남아있는 캔디 - 줘야 하는 캔디 <= 0
    if total_candy - ans <= 0:
        last_person = person
        break

    total_candy -= ans
    queue.append((person, ans + 1))

    cnt_person = max(cnt_person, person + 1)
    # 한 명이 줄을 서면, 새로운 번호의 사람이 와서 다시 줄은 선다
    queue.append((cnt_person + 1, 1))

print(f"마지막 마이쮸는 {last_person}번")