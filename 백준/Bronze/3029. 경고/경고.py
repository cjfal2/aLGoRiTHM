def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

now = input().strip()
throw = input().strip()

h1, m1, s1 = map(int, now.split(':'))
h2, m2, s2 = map(int, throw.split(':'))

now_seconds = time_to_seconds(h1, m1, s1)
throw_seconds = time_to_seconds(h2, m2, s2)

wait_seconds = throw_seconds - now_seconds
if wait_seconds <= 0:
    wait_seconds += 24 * 3600

print(seconds_to_time(wait_seconds))
