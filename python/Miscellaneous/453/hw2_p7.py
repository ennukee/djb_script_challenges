# hw2_py7.py
# Dylan Bowers (28838875)

HEADER_SIZE = 320.0
MESSAGE_SIZE = 1152000.0
TRANSMISSION_RATE = 2000000.0
E2E_cache = {}

def end_to_end_delay(n):
    packet_size = HEADER_SIZE + MESSAGE_SIZE / n
    time_to_send = packet_size / TRANSMISSION_RATE
    total_sending_time = time_to_send * ((n - 1) + 2)

    E2E_cache[n] = total_sending_time
    return total_sending_time


last_time = 500
current_n = 1
while True:
    E2E_delay = end_to_end_delay(current_n)
    print(current_n, E2E_cache[current_n])
    if E2E_delay > last_time:
        # Move back 1 n value since we're on the right value + 1
        current_n -= 1
        last_time = E2E_cache[current_n]
        break
    else:
        last_time = E2E_delay
        current_n += 1

print 'Optimal value found at n={}\ntime taken at {}={}s\ntime taken at {}={}s\ntime taken at {}={}s'.format(
    current_n, current_n - 1, E2E_cache[current_n - 1], current_n,
    E2E_cache[current_n], current_n + 1, end_to_end_delay(current_n + 1)
)
