#!/bin/bash

# Check if the search pattern argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <search_pattern> [output_file]"
    exit 1
fi

# Set the search pattern
pattern="$1"

# Set the output file (optional)
output_file="$2"

# Create a temporary file to store the output
tmp_file=$(mktemp)

# Find all files matching the given pattern recursively
find . -type f -name "$pattern" -print0 | while IFS= read -r -d '' file; do
    # Print the file path
    echo "#!# $file" >> "$tmp_file"
    # Print the file contents
    cat "$file" >> "$tmp_file"
    echo "" >> "$tmp_file" # Add a blank line for separation
done

# Save the output to a file if a filename is provided
if [ -n "$output_file" ]; then
    cat "$tmp_file" > "$output_file"
    echo "Output saved to $output_file"
else
    # Copy the contents of the temporary file to the clipboard
    cat "$tmp_file" | xclip -selection clipboard
    echo "Output copied to clipboard"
fi

# Clean up the temporary file
rm "$tmp_file"
