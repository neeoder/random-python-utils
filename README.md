# Wordlist Merger

This Python script efficiently merges multiple wordlists into a single, de-duplicated output file. It leverages the rich library for enhanced console output, providing informative messages and error handling.

## Features:

- __Merges multiple wordlists__: Combine several wordlists into a single comprehensive list.
- __De-duplicates entries__: Removes duplicate words, ensuring a clean output.
- __Converts words to lowercase__: Ensures case-insensitive word matching.
- __Rich console output__: Provides clear and visually appealing messages (optional).
- __Error handling__: Validates input file existence and guides users appropriately.

## Installation:

1. Ensure you have Python 3 installed (https://www.python.org/downloads/).
2. Install the `rich` library using pip:
  ```
  pip install rich
  ```

## Usage:

There are two ways to use this script:

### 1. Interactive Mode (Enter wordlists one by one):

  1. Run the script with no arguments:
  ```
  python wordlist_merger.py
  ```
  2. You'll be prompted to enter the path to each wordlist one by one. Press Enter to finish.
  3. Specify the desired output file name.

### 2. Command-line Mode (Specify wordlists and output file):

  1. Run the script with the following arguments:
   ```
   python wordlist_merger.py [output_file] [wordlist1] [wordlist2] ...
   ```

   - `output_file`: The path to the file where the merged wordlist will be saved.
   - `wordlist1`, `wordlist2`, etc.: The paths to the wordlists you want to merge.

## Example (Command-line Mode):

```
python wordlist_merger.py merged_words.txt wordlist1.txt wordlist2.txt
```
This merges `wordlist1.txt` and `wordlist2.txt` into `merged_words.txt`.

## Optional Rich Console Output:

This script attempts to use the `rich` library for colorful and user-friendly output. If your terminal doesn't support "True Color," you'll be notified.

## Additional Notes:

- The script ensures that the output file is not a directory itself. If you provide a directory path, it will create a file named merged_wordlist.txt within that directory.
- The merged wordlist is sorted alphabetically and saved in a clean format.

## Feedback and Contribution:

Feel free to report any issues or suggest improvements. You can also contribute to the project by forking it on GitHub (if applicable).
