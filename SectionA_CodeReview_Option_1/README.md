# Group Anagrams - Python Solution

This repository contains a Python solution for grouping anagrams from a list of strings. It demonstrates data manipulation and algorithmic thinking in Python.

## Problem Description

The task is to write a function that accepts a list of strings and groups the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

For example, the words "eat", "tea", and "ate" are all anagrams of each other because they all contain the same letters.

## Solution

The solution implemented in this repository uses a dictionary to categorize the strings by their sorted character tuples.

For each string in the input list:
1. The string is sorted alphabetically, which provides a unique representation for each set of anagrams.
2. The sorted string is used as a key in a dictionary, and the original string is appended to the list of values for that key.

The function returns a list of lists, with each sublist containing a group of anagrams.

## Usage

The main solution can be found in the `anagram.py` file. To execute the solution, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `anagram.py` file.
3. Run the following command:

```bash
python anagram.py
```

The list of anagram groups will be printed to the console.

## Testing

This solution has been tested with several inputs, including the example input: `["eat", "tea", "tan", "ate", "nat", "bat"]`.

To run the tests, you can use the `anagram_test.py` file. Execute the following command:

```bash
python anagram_test.py
```

This will run the test cases and verify the correctness of the solution.

### Space Complexity Analysis

The space complexity of an algorithm refers to the amount of additional memory or space required by the algorithm to solve a problem. In the case of the Anagram Grouping solution, we will analyze the worst-case space complexity.

The space complexity of the given solution is O(N), where N is the total number of characters in all the input strings combined. This complexity arises from the use of a dictionary to store the anagram groups.

Explanation:
- For each input string, the characters are sorted to generate a unique representation for each set of anagrams.
- The sorted string is used as a key in the dictionary, and the original string is appended to the list of values for that key.
- As the number of input strings increases, the dictionary's size grows proportionally.

In the worst-case scenario, where all the input strings are distinct and do not form any anagram groups, the space complexity can be analyzed as follows:
- Each input string will be stored as a value in the dictionary, resulting in N entries.
- The length of each string can be at most M, where M is the maximum length among all the input strings.
- Therefore, the total space required will be O(N * M).

It's important to note that the space complexity does not depend on the number of anagram groups or their sizes, but rather on the total number of characters in the input strings.

If memory usage is a concern, especially for very large inputs, alternative approaches that trade-off space for time efficiency could be explored.

## Contact

If you have any questions or suggestions regarding this solution, feel free to reach out.

Hein.Engelbrecht2403@gmail.com

Thank you for your consideration!