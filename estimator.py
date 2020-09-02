import sys

for line in sys.stdin:
    timestamp = int(line.replace('\n', ''))
    print(timestamp)

sys.stdout.flush()
