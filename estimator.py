import sys

one_hour_in_sec = 60 * 60

all_commit_timestamps = []

for line in sys.stdin:
    timestamp = int(line.replace('\n', ''))
    all_commit_timestamps.append(timestamp)

all_commit_timestamps.sort()


def estimate(timestamps, threshold):
    total_time_sec = 0

    previous_timestamp = timestamps[0]
    current_session = []

    for x in range(1, len(timestamps)):
        delta = timestamps[x] - previous_timestamp
        previous_timestamp = timestamps[x]

        if delta >= threshold:
            if len(current_session) >= 2:
                start = current_session[0]
                end = current_session[len(current_session) - 1]
                duration = end - start
                total_time_sec += duration
            current_session = []
        else:
            current_session.append(timestamps[x])

    return total_time_sec


def report_estimate(threshold):
    start = all_commit_timestamps[0]
    end = all_commit_timestamps[len(all_commit_timestamps) - 1]

    nbr_of_days_period = int((end - start) / (one_hour_in_sec * 24))

    nbr_of_work_hours = int(estimate(all_commit_timestamps, threshold) / one_hour_in_sec)
    nbr_of_work_days = int(nbr_of_work_hours / 8)

    print()
    print("threshold of", threshold, "sec.")
    print("amount of work (hours):", nbr_of_work_hours)
    print("amount of work (days):", nbr_of_work_days)
    print("on a period of (days):", nbr_of_days_period)
    try:
        print("nbr of hours/days on this project:", nbr_of_work_hours / nbr_of_days_period)
    except ZeroDivisionError:
        print("nbr of hours/days on this project: *** Divided by zero *** ", 0)

report_estimate(one_hour_in_sec)
report_estimate(2 * one_hour_in_sec)
report_estimate(3 * one_hour_in_sec)

sys.stdout.flush()
