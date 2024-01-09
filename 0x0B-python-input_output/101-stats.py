#!/usr/bin/python3
"""Import and def proc line."""


import sys
from collections import defaultdict

def process_line(line, stats):
    """
    Process a single line of input and update the statistics.

    :param line: The input line.
    :param stats: Dictionary to store the statistics.
    """
    try:
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update total file size
        stats['total_size'] += file_size

        # Update status code count
        stats['status_codes'][status_code] += 1
    except (ValueError, IndexError):
        pass  # Ignore lines with invalid format

def print_statistics(stats):
    """
    Print the computed statistics.

    :param stats: Dictionary containing the statistics.
    """
    print(f"Total file size: {stats['total_size']}")

    # Print status code count in ascending order
    for code in sorted(stats['status_codes']):
        count = stats['status_codes'][code]
        print(f"{code}: {count}")

def main():
    stats = {'total_size': 0, 'status_codes': defaultdict(int)}
    line_count = 0

    try:
        for line in sys.stdin:
            process_line(line.strip(), stats)
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(stats)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_statistics(stats)

if __name__ == "__main__":
    main()
