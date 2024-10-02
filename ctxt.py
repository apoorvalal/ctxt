#!/usr/bin/env python3
import os
import sys
import glob
import subprocess


def find_files(pattern):
    files = []
    for root, _, _ in os.walk("."):
        matched_files = glob.glob(os.path.join(root, pattern))
        files.extend(matched_files)
    return files


def copy_to_clipboard(text):
    if sys.platform.startswith("linux"):
        try:
            subprocess.run(
                ["xclip", "-selection", "clipboard"],
                input=text,
                encoding="utf-8",
                check=True,
            )
        except FileNotFoundError:
            print("xclip is not installed. Skipping clipboard integration.")
    elif sys.platform == "darwin":  # macOS
        subprocess.run(["pbcopy"], input=text, encoding="utf-8", check=True)
    elif sys.platform == "win32":  # only works on WSL
        subprocess.run(["clip.exe"], input=text, encoding="utf-8", check=True)
    else:
        print("Unsupported operating system. Skipping clipboard integration.")


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"Usage: {sys.argv[0]} <search_pattern> [output_file]")
        sys.exit(1)

    pattern = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) == 3 else None

    print("Search pattern:", pattern)
    files = find_files(pattern)
    print("Selected files:", files)

    output = ""
    for file_path in files:
        # add filename to output
        output += f"#!# file: {file_path}\n"
        with open(file_path, "r") as f:
            # add file contents to output
            output += f.read() + "\n\n"

    if output_file:
        with open(output_file, "w") as f:
            f.write(output)
        print(f"Output saved to {output_file}")
    else:
        copy_to_clipboard(output)
        print("Output copied to clipboard.")
