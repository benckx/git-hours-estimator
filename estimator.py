import sys

one_hour_in_sec = 60 * 60

timestamps = []

for line in sys.stdin:
    timestamp = int(line.replace('\n', ''))
    timestamps.append(timestamp)


def estimate(timestamps, threshold):
    total_time_sec = 0

    timestamps.sort()
    previous_timestamp = timestamps[0]
    current_session = []

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
        else:
            current_session.append(timestamps[x])

    return total_time_sec


print(estimate(timestamps, one_hour_in_sec) / one_hour_in_sec)
print(estimate(timestamps, 3 * one_hour_in_sec) / one_hour_in_sec)

sys.stdout.flush()
