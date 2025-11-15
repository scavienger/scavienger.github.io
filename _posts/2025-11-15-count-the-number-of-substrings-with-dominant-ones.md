---
layout: post
title: "Count the Number of Substrings With Dominant Ones"
date: 2025-11-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Sliding Window", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
---

## Problem #3234: Count the Number of Substrings With Dominant Ones

**Difficulty:** Medium

**Topics:** String, Sliding Window, Enumeration

## Problem Description

You are given a binary string `s`.



Return the number of substrings with **dominant** ones.



A string has **dominant** ones if the number of ones in the string is **greater than or equal to** the **square** of the number of zeros in the string.



 


Example 1:




**Input:** s = "00011"



**Output:** 5



**Explanation:**



The substrings with dominant ones are shown in the table below.





	
		
			i
			j
			s[i..j]
			Number of Zeros
			Number of Ones
		
	
	
		
			3
			3
			1
			0
			1
		
		
			4
			4
			1
			0
			1
		
		
			2
			3
			01
			1
			1
		
		
			3
			4
			11
			0
			2
		
		
			2
			4
			011
			1
			2
		
	


Example 2:




**Input:** s = "101101"



**Output:** 16



**Explanation:**



The substrings with **non-dominant** ones are shown in the table below.



Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.





	
		
			i
			j
			s[i..j]
			Number of Zeros
			Number of Ones
		
	
	
		
			1
			1
			0
			1
			0
		
		
			4
			4
			0
			1
			0
		
		
			1
			4
			0110
			2
			2
		
		
			0
			4
			10110
			2
			3
		
		
			1
			5
			01101
			2
			3
		
	


 


**Constraints:**





	- `1 <= s.length <= 4 * 10^4`
	- `s` consists only of characters `&#39;0&#39;` and `&#39;1&#39;`.

## Hints

1. Let us fix the starting index `l` of the substring and count the number of indices `r` such that `l <= r` and the substring `s[l..r]` has dominant ones.

2. A substring with dominant ones has at most `sqrt(n)` zeros.

3. We cannot iterate over every `r` and check if the  `s[l..r]` has dominant ones. Instead, we iterate over the next `sqrt(n)` zeros to the left of `l` and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.

## ✨ AI-Generated Solution (GEMINI)

### Approach

The problem requires counting substrings with dominant ones, where `ones_count >= zeros_count^2`. A crucial observation is that if `ones_count <= N` (the total length of the string), then `zeros_count^2 <= N`, implying `zeros_count <= sqrt(N)`. This means any substring satisfying the condition can have at most `sqrt(N)` zeros. For `N = 4 * 10^4`, `sqrt(N) = 200`.

We define `MAX_ZEROS_THRESHOLD = int(sqrt(N)) + 1`. Substrings with more than `MAX_ZEROS_THRESHOLD` zeros cannot be dominant. The solution proceeds in two parts:

1.  **Count substrings with zero zeros:** If `zeros_count = 0`, the condition `ones_count >= 0^2` is always true. All substrings consisting entirely of '1's are dominant. We iterate through the string once. When we encounter a '1', we increment a `current_ones_block_length` counter and add its value to `ans`. If we encounter a '0', we reset `current_ones_block_length` to `0`. This efficiently counts all such substrings in O(N) time.

2.  **Count substrings with 1 to `MAX_ZEROS_THRESHOLD` zeros:** We iterate through all possible right endpoints `j` (from `0` to `N-1`). For each `j`, we iterate leftwards from `j` down to `0` to determine the left endpoint `i` of the substring `s[i..j]`. As `i` decreases, we maintain `zeros_count` and `ones_count` for `s[i..j]`.
    *   If `s[i]` is '0', `zeros_count` increases; if `s[i]` is '1', `ones_count` increases.
    *   **Optimization:** If `zeros_count` for `s[i..j]` exceeds `MAX_ZEROS_THRESHOLD`, we `break` the inner loop. This is because any substring `s[i'..j]` with `i' < i` would have an even higher (or equal) `zeros_count`, thus making it impossible to satisfy the dominant ones condition.
    *   If `zeros_count` is between `1` and `MAX_ZEROS_THRESHOLD` (inclusive), and `ones_count >= zeros_count^2`, we increment `ans`. We specifically check `zeros_count >= 1` to avoid double-counting substrings already handled in Part 1.

This two-part approach correctly handles all cases. The `MAX_ZEROS_THRESHOLD` optimization ensures that the inner loop of Part 2, for any `j`, will examine at most `MAX_ZEROS_THRESHOLD` zeros and the '1's between them. This limits the total work for Part 2 to `O(N * MAX_ZEROS_THRESHOLD)`, which simplifies to `O(N * sqrt(N))`.

### Code

```python
import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # MAX_ZEROS_THRESHOLD is the maximum number of zeros a substring can have
        # to potentially satisfy the dominant ones condition (ones_count >= zeros_count^2).
        # If zeros_count > MAX_ZEROS_THRESHOLD, then zeros_count^2 > n (max possible ones_count),
        # so ones_count >= zeros_count^2 cannot be true.
        # Adding 1 to int(math.sqrt(n)) to handle edge cases where n is a perfect square
        # or for minor floating point inaccuracies, ensuring the threshold is safely inclusive.
        MAX_ZEROS_THRESHOLD = int(math.sqrt(n)) + 1 
        
        # Part 1: Count substrings with zero zeros.
        # These are all substrings composed entirely of '1's.
        # For any such substring, zeros_count = 0, so ones_count >= 0^2 is always true.
        # We iterate through the string, maintaining the length of the current contiguous block of '1's.
        # For a block of k '1's, it forms k, k-1, ..., 1 new dominant substrings ending at the current position,
        # which sums to k*(k+1)/2. This can be accumulated by just adding the current_ones_block_length at each '1'.
        current_ones_block_length = 0
        for char in s:
            if char == '1':
                current_ones_block_length += 1
                ans += current_ones_block_length
            else:
                current_ones_block_length = 0
        
        # Part 2: Count substrings with 1 to MAX_ZEROS_THRESHOLD zeros.
        # We iterate through all possible right endpoints `j`.
        # For each `j`, we iterate leftwards with `i` from `j` down to `0`.
        # We maintain `zeros` and `ones` counts for the current substring `s[i..j]`.
        for j in range(n):
            zeros = 0
            ones = 0
            # Iterate i from j down to 0
            for i in range(j, -1, -1):
                if s[i] == '0':
                    zeros += 1
                else:
                    ones += 1
                
                # Optimization: if current `zeros` count exceeds the threshold,
                # any further decrease in `i` (going left) will only increase or maintain `zeros`,
                # making it impossible for `ones >= zeros^2` to be true. So we break early.
                if zeros > MAX_ZEROS_THRESHOLD:
                    break
                
                # We only count substrings with at least one zero here,
                # as zero-zero substrings were already handled in Part 1.
                # Check the dominant ones condition.
                if zeros >= 1 and ones >= zeros * zeros:
                    ans += 1
                    
        return ans

```

### Complexity Analysis

- **Time Complexity:** O(N * sqrt(N)) concatenating explanations:

*   **Part 1 (Substrings with zero zeros):** This loop iterates through the string `s` once. Each operation inside the loop takes constant time. Thus, this part contributes O(N) to the total time complexity.
*   **Part 2 (Substrings with 1 to `MAX_ZEROS_THRESHOLD` zeros):** The outer loop runs `N` times (for `j` from `0` to `N-1`). The inner loop (for `i` from `j` down to `0`) is optimized by the `break` condition `if zeros > MAX_ZEROS_THRESHOLD`. For any given `j`, the inner loop stops once `zeros` exceeds `MAX_ZEROS_THRESHOLD`. This means that `i` will traverse a segment of `s` that contains at most `MAX_ZEROS_THRESHOLD` zeros. The total number of characters processed across all iterations of the inner loop (summed over all `j`) is proportional to `N * MAX_ZEROS_THRESHOLD`. Since `MAX_ZEROS_THRESHOLD` is `O(sqrt(N))`, the total time complexity for this part is `O(N * sqrt(N))`.

Combining both parts, the overall time complexity is O(N) + O(N * sqrt(N)) = O(N * sqrt(N)).
- **Space Complexity:** O(1) excluding the input string `s`. The solution uses a few integer variables (`n`, `ans`, `MAX_ZEROS_THRESHOLD`, `current_ones_block_length`, `j`, `i`, `zeros`, `ones`) which require a constant amount of memory regardless of the input string's length.
