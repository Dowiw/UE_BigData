#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

# Input comes from standard input (STDIN)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Parse the input we got from mapper.py
    try:
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        # If count was not a number, silently ignore/discard this line
        continue

    # Hadoop sorts map output by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word is not None:
            # Write result to standard output (STDOUT)
            print(f'{current_word}\t{current_count}')
        current_word = word
        current_count = count

# Output the last word if needed
if current_word is not None:
    print(f'{current_word}\t{current_count}')
