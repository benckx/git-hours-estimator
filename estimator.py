import sys

one_hour_in_sec = 60 * 60
threshold = 2 * one_hour_in_sec

timestamps = []

for line in sys.stdin:
    timestamp = int(line.replace('\n', ''))
    timestamps.append(timestamp)

total_time_sec = 0

timestamps.sort()
previous_timestamp = timestamps[0]
current_session = []
nbr_of_sessions = 0

for x in range(1, len(timestamps)):
    delta = timestamps[x] - previous_timestamp
    previous_timestamp = timestamps[x]

    if delta > threshold:
        if len(current_session) >= 2:
            start = current_session[0]
            end = current_session[len(current_session) - 1]
            duration = end - start
            total_time_sec += duration
            current_session = []
        nbr_of_sessions += 1
    else:
        current_session.append(timestamps[x])

print(total_time_sec / one_hour_in_sec)

sys.stdout.flush()
