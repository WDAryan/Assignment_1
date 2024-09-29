arr = list(map(int, input("Enter the elements of the list with space: ").strip().split())) #unable to take user input without .strip()
max_len = 0
max_sum = 0
current_len = 0
current_sum = 0
seq = []

for n in arr:
    if n < 0:
        current_len += 1
        current_sum += n
    else:
        if current_len > 0:
            seq.append((current_len, current_sum))
        current_len = 0
        current_sum = 0

if current_len > 0:
    seq.append((current_len, current_sum))

max_len = 0
for s in seq:
    if s[0] > max_len:
        max_len = s[0]

max_sum = 0
for s in seq:
    if s[0] == max_len:
        max_sum += s[1] #taken little help fot this 

if max_sum==0:
    print(-1)
else:
    print(max_sum)
