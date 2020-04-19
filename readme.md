# Read a random note
find . -type d \( -name .git  \) -prune -o \( -name "*.mkd" -o -name "*.md" \) |shuf -n 1

# find a random doc to read
find . -type f | shuf -n 1
find . -type f -name "*.md" -not -path "./.git/*" |shuf -n 1
