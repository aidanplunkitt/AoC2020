BP_LEN = 10
min_seat, max_seat, seat_sum = 2**BP_LEN - 1, 0, 0

with open('5.txt') as fp:
    for line in fp:
        seat_id = int(''.join(['1' if i in 'BR' else '0' for i in line[:BP_LEN]]), 2)
        min_seat = min(min_seat, seat_id)
        max_seat = max(max_seat, seat_id)
        seat_sum += seat_id

my_seat = sum(range(min_seat, max_seat + 1)) - seat_sum
print(max_seat, my_seat)