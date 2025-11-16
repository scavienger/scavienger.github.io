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

The problem asks us to count substrings where the number of ones is greater than or equal to the square of the number of zeros (`ones >= zeros^2`). Let `N` be the length of the input string `s`. `N` can be up to `4 * 10^4`.

The key observation for solving this problem efficiently is related to the maximum number of zeros a dominant substring can contain. Let `z` be the number of zeros and `o` be the number of ones in a substring. If `o >= z^2` holds, the substring is dominant. Since `o` cannot exceed the total length of the substring (`o <= N`), it implies that `z^2 <= o <= N`. Therefore, `z^2 <= N`, which means `z <= sqrt(N)`. For `N = 4 * 10^4`, `sqrt(N) = 200`. This means any substring with dominant ones can have at most `floor(sqrt(N))` zeros. If a substring has more than `floor(sqrt(N))` zeros, it cannot be dominant because its `zeros^2` would exceed `N`, and thus `ones` (which is at most `N`) cannot be greater than or equal to `zeros^2`.

This observation allows for an optimized `O(N * sqrt(N))` approach:

1.  Initialize `total_dominant_substrings = 0` to store the final count.
2.  Calculate `MAX_ZERO_COUNT_THRESHOLD = floor(sqrt(N))`. This threshold indicates the maximum number of zeros a substring can have and still potentially be dominant. We use `floor(sqrt(N))` because if `current_zeros` exceeds this value (i.e., `current_zeros >= floor(sqrt(N)) + 1`), then `current_zeros^2` will be greater than `N`, making the dominance condition impossible.
3.  Iterate through `r` from `0` to `N-1`. This `r` will represent the rightmost index of the current substring `s[l..r]`.
4.  Inside this loop, for each `r`, initialize `current_zeros = 0` and `current_ones = 0`.
5.  Iterate `l` backwards from `r` down to `0`. This `l` will represent the leftmost index of the current substring `s[l..r]`.
6.  As `l` decreases, update `current_zeros` and `current_ones` based on `s[l]`:
    *   If `s[l] == '0'`, increment `current_zeros`.
    *   If `s[l] == '1'`, increment `current_ones`.
7.  **Optimization/Early Exit**: If `current_zeros` becomes greater than `MAX_ZERO_COUNT_THRESHOLD`, then any further substring `s[l'..r]` (where `l' < l`) will have even more zeros. As explained above, such substrings cannot be dominant. Therefore, we can `break` out of the inner loop (for `l`) and move to the next `r`.
8.  **Check Condition**: If the `l` loop has not broken, check if `current_ones >= current_zeros * current_zeros`. If this condition is true, increment `total_dominant_substrings`.
9.  After both loops complete, `total_dominant_substrings` will hold the final answer.

This approach ensures that for each `r`, the inner loop for `l` runs at most `r+1` times. However, the `break` condition `current_zeros > MAX_ZERO_COUNT_THRESHOLD` significantly limits the number of iterations where `current_zeros` is non-zero. Specifically, for a fixed `r`, the `l` loop will execute at most `MAX_ZERO_COUNT_THRESHOLD + 1` times where `s[l]` is a '0'. The characters '1' between these '0's also contribute to `current_ones` but do not increment `current_zeros`. In the worst case, the inner loop processes roughly `sqrt(N)` '0's and some '1's in between, leading to an overall time complexity of `O(N * sqrt(N))`.

Example dry run for `s = "00011"` with `N=5`, `MAX_ZERO_COUNT_THRESHOLD = floor(sqrt(5)) = 2`:
- `r=0 (s[0]='0')`: `l=0, s[0..0]='0'`, `z=1, o=0`. `0 >= 1^2` (False).
- `r=1 (s[1]='0')`: `l=1, s[1..1]='0'`, `z=1, o=0` (False). `l=0, s[0..1]='00'`, `z=2, o=0` (False).
- `r=2 (s[2]='0')`: `l=2, s[2..2]='0'`, `z=1, o=0` (False). `l=1, s[1..2]='00'`, `z=2, o=0` (False). `l=0, s[0..2]='000'`, `z=3, o=0`. `current_zeros` (3) `> MAX_ZERO_COUNT_THRESHOLD` (2), so break for `l` loop.
- `r=3 (s[3]='1')`: 
  - `l=3, s[3..3]='1'`, `z=0, o=1`. `1 >= 0^2` (True). `total=1`.
  - `l=2, s[2..3]='01'`, `z=1, o=1`. `1 >= 1^2` (True). `total=2`.
  - `l=1, s[1..3]='001'`, `z=2, o=1`. `1 >= 2^2` (False).
  - `l=0, s[0..3]='0001'`, `z=3, o=1`. `current_zeros` (3) `> MAX_ZERO_COUNT_THRESHOLD` (2), so break for `l` loop.
- `r=4 (s[4]='1')`: 
  - `l=4, s[4..4]='1'`, `z=0, o=1`. `1 >= 0^2` (True). `total=3`.
  - `l=3, s[3..4]='11'`, `z=0, o=2`. `2 >= 0^2` (True). `total=4`.
  - `l=2, s[2..4]='011'`, `z=1, o=2`. `2 >= 1^2` (True). `total=5`.
  - `l=1, s[1..4]='0011'`, `z=2, o=2`. `2 >= 2^2` (False).
  - `l=0, s[0..4]='00011'`, `z=3, o=2`. `current_zeros` (3) `> MAX_ZERO_COUNT_THRESHOLD` (2), so break for `l` loop.

Final `total_dominant_substrings = 5`, which matches Example 1.

### Code

<div class="code-tabs">
  <input type="radio" name="code-lang" id="lang-python" checked>
  <input type="radio" name="code-lang" id="lang-java">
  <input type="radio" name="code-lang" id="lang-cpp">
  <input type="radio" name="code-lang" id="lang-javascript">
  <input type="radio" name="code-lang" id="lang-typescript">
  <input type="radio" name="code-lang" id="lang-go">
  <div class="tab-labels">
    <label for="lang-python">Python</label>
    <label for="lang-java">Java</label>
    <label for="lang-cpp">C++</label>
    <label for="lang-javascript">JavaScript</label>
    <label for="lang-typescript">TypeScript</label>
    <label for="lang-go">Go</label>
  </div>

  <div class="tab-panel" data-lang="python">

```python
import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        total_dominant_substrings = 0
        
        # A dominant substring can have at most floor(sqrt(N)) zeros.
        # If current_zeros > max_zeros_threshold, then current_zeros^2 > N.
        # Since current_ones <= N, it's impossible for current_ones >= current_zeros^2.
        # So we can break early if current_zeros exceeds this threshold.
        max_zeros_threshold = math.isqrt(n) # math.isqrt is available in Python 3.8+
        # For older Python versions, int(n**0.5) can be used.

        for r in range(n):
            current_zeros = 0
            current_ones = 0
            # Iterate 'l' backwards from 'r' to '0'
            for l in range(r, -1, -1):
                if s[l] == '0':
                    current_zeros += 1
                else: # s[l] == '1'
                    current_ones += 1
                
                # Optimization: if current_zeros exceeds the threshold,
                # any further substring by decreasing l will have even more zeros,
                # making the condition impossible to satisfy.
                if current_zeros > max_zeros_threshold:
                    break
                
                # Check the dominant condition
                if current_ones >= current_zeros * current_zeros:
                    total_dominant_substrings += 1
                    
        return total_dominant_substrings
```

  </div>

  <div class="tab-panel" data-lang="java">

```java
import java.lang.Math;

class Solution {
    public long numberOfSubstrings(String s) {
        int n = s.length();
        long totalDominantSubstrings = 0;
        
        // A dominant substring can have at most floor(sqrt(N)) zeros.
        // If currentZeros > maxZerosThreshold, then currentZeros^2 > N.
        // Since currentOnes <= N, it's impossible for currentOnes >= currentZeros^2.
        // So we can break early if currentZeros exceeds this threshold.
        // Math.sqrt returns a double, cast to int for floor effect.
        int maxZerosThreshold = (int) Math.sqrt(n);

        for (int r = 0; r < n; r++) {
            int currentZeros = 0;
            int currentOnes = 0;
            // Iterate 'l' backwards from 'r' to '0'
            for (int l = r; l >= 0; l--) {
                if (s.charAt(l) == '0') {
                    currentZeros++;
                } else { // s.charAt(l) == '1'
                    currentOnes++;
                }
                
                // Optimization: if currentZeros exceeds the threshold,
                // any further substring by decreasing l will have even more zeros,
                // making the condition impossible to satisfy.
                if (currentZeros > maxZerosThreshold) {
                    break;
                }
                
                // Check the dominant condition
                // totalDominantSubstrings must be long to avoid overflow (max 8*10^8).
                // currentOnes and currentZeros fit in int, but their product (up to 4*10^4*4*10^4 = 1.6*10^9) 
                // could exceed int max (2*10^9). currentZeros*currentZeros is max 200*200=40000. 
                // So int for product is fine here. But casting to long for safety in comparison is good practice.
                if ((long)currentOnes >= (long)currentZeros * currentZeros) {
                    totalDominantSubstrings++;
                }
            }
        }
        
        return totalDominantSubstrings;
    }
}
```

  </div>

  <div class="tab-panel" data-lang="cpp">

```cpp
#include <string>
#include <cmath>
#include <vector>

class Solution {
public:
    long long numberOfSubstrings(std::string s) {
        int n = s.length();
        long long totalDominantSubstrings = 0;
        
        // A dominant substring can have at most floor(sqrt(N)) zeros.
        // If currentZeros > maxZerosThreshold, then currentZeros^2 > N.
        // Since currentOnes <= N, it's impossible for currentOnes >= currentZeros^2.
        // So we can break early if currentZeros exceeds this threshold.
        // std::sqrt returns a double, cast to int for floor effect.
        int maxZerosThreshold = static_cast<int>(std::sqrt(n));

        for (int r = 0; r < n; ++r) {
            int currentZeros = 0;
            int currentOnes = 0;
            // Iterate 'l' backwards from 'r' to '0'
            for (int l = r; l >= 0; --l) {
                if (s[l] == '0') {
                    currentZeros++;
                } else { // s[l] == '1'
                    currentOnes++;
                }
                
                // Optimization: if currentZeros exceeds the threshold,
                // any further substring by decreasing l will have even more zeros,
                // making the condition impossible to satisfy.
                if (currentZeros > maxZerosThreshold) {
                    break;
                }
                
                // Check the dominant condition
                // totalDominantSubstrings must be long long to avoid overflow (max 8*10^8).
                // currentOnes and currentZeros fit in int, but their product could overflow.
                // currentZeros*currentZeros is max 200*200=40000, so int is fine. 
                // But casting to long long for comparison is a safer practice.
                if (static_cast<long long>(currentOnes) >= static_cast<long long>(currentZeros) * currentZeros) {
                    totalDominantSubstrings++;
                }
            }
        }
        
        return totalDominantSubstrings;
    }
};
```

  </div>

  <div class="tab-panel" data-lang="javascript">

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const n = s.length;
    let totalDominantSubstrings = 0;
    
    // A dominant substring can have at most floor(sqrt(N)) zeros.
    // If currentZeros > maxZerosThreshold, then currentZeros^2 > N.
    // Since currentOnes <= N, it's impossible for currentOnes >= currentZeros^2.
    // So we can break early if currentZeros exceeds this threshold.
    const maxZerosThreshold = Math.floor(Math.sqrt(n));

    for (let r = 0; r < n; r++) {
        let currentZeros = 0;
        let currentOnes = 0;
        // Iterate 'l' backwards from 'r' to '0'
        for (let l = r; l >= 0; l--) {
            if (s[l] === '0') {
                currentZeros++;
            } else { // s[l] === '1'
                currentOnes++;
            }
            
            // Optimization: if currentZeros exceeds the threshold,
            // any further substring by decreasing l will have even more zeros,
            // making the condition impossible to satisfy.
            if (currentZeros > maxZerosThreshold) {
                break;
            }
            
            // Check the dominant condition
            // JavaScript numbers are 64-bit floats, which can safely represent
            // integers up to 2^53 - 1. Max totalDominantSubstrings is 8 * 10^8,
            // which fits. currentZeros * currentZeros also fits.
            if (currentOnes >= currentZeros * currentZeros) {
                totalDominantSubstrings++;
            }
        }
    }
    
    return totalDominantSubstrings;
};
```

  </div>

  <div class="tab-panel" data-lang="typescript">

```typescript
function numberOfSubstrings(s: string): number {
    const n: number = s.length;
    let totalDominantSubstrings: number = 0;
    
    // A dominant substring can have at most floor(sqrt(N)) zeros.
    // If currentZeros > maxZerosThreshold, then currentZeros^2 > N.
    // Since currentOnes <= N, it's impossible for currentOnes >= currentZeros^2.
    // So we can break early if currentZeros exceeds this threshold.
    const maxZerosThreshold: number = Math.floor(Math.sqrt(n));

    for (let r: number = 0; r < n; r++) {
        let currentZeros: number = 0;
        let currentOnes: number = 0;
        // Iterate 'l' backwards from 'r' to '0'
        for (let l: number = r; l >= 0; l--) {
            if (s[l] === '0') {
                currentZeros++;
            } else { // s[l] === '1'
                currentOnes++;
            }
            
            // Optimization: if currentZeros exceeds the threshold,
            // any further substring by decreasing l will have even more zeros,
            // making the condition impossible to satisfy.
            if (currentZeros > maxZerosThreshold) {
                break;
            }
            
            // Check the dominant condition
            // TypeScript numbers (like JavaScript) are 64-bit floats.
            // Max totalDominantSubstrings is 8 * 10^8, fits within safe integer limits.
            if (currentOnes >= currentZeros * currentZeros) {
                totalDominantSubstrings++;
            }
        }
    }
    
    return totalDominantSubstrings;
};
```

  </div>

  <div class="tab-panel" data-lang="go">

```go
package main

import (
	"math"
)

func numberOfSubstrings(s string) int64 {
    n := len(s)
    var totalDominantSubstrings int64 = 0
    
    // A dominant substring can have at most floor(sqrt(N)) zeros.
    // If currentZeros > maxZerosThreshold, then currentZeros^2 > N.
    // Since currentOnes <= N, it's impossible for currentOnes >= currentZeros^2.
    // So we can break early if currentZeros exceeds this threshold.
    // math.Sqrt returns a float64, cast to int for floor effect.
    maxZerosThreshold := int(math.Sqrt(float64(n)))

    for r := 0; r < n; r++ {
        currentZeros := 0
        currentOnes := 0
        // Iterate 'l' backwards from 'r' to '0'
        for l := r; l >= 0; l-- {
            if s[l] == '0' {
                currentZeros++
            } else { // s[l] == '1'
                currentOnes++
            }
            
            // Optimization: if currentZeros exceeds the threshold,
            // any further substring by decreasing l will have even more zeros,
            // making the condition impossible to satisfy.
            if currentZeros > maxZerosThreshold {
                break
            }
            
            // Check the dominant condition
            // totalDominantSubstrings must be int64 to avoid overflow (max 8*10^8).
            // currentOnes and currentZeros fit in int, but their product could overflow.
            // currentZeros*currentZeros is max 200*200=40000, so int is fine. 
            // But casting to int64 for comparison is a safer practice.
            if int64(currentOnes) >= int64(currentZeros) * int64(currentZeros) {
                totalDominantSubstrings++
            }
        }
    }
    
    return totalDominantSubstrings
}
```

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(N * sqrt(N))

- **Space Complexity:** O(1)