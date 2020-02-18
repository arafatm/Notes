# Read a random note
find . -type d \( -name .git  \) -prune -o \( -name "*.mkd" -o -name "*.md" \) |shuf -n 1

find . -type f | shuf -n 1
