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

**Example 1:**

**Input:** s = "00011"

**Output:** 5

**Explanation:**

The substrings with dominant ones are shown in the table below.

``` i j s[i..j] Number of Zeros Number of Ones 3 3 1 0 1 4 4 1 0 1 2 3 01 1 1 3 4 11 0 2 2 4 011 1 2 ``` 

**Example 2:**

**Input:** s = "101101"

**Output:** 16

**Explanation:**

The substrings with **non-dominant** ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

``` i j s[i..j] Number of Zeros Number of Ones 1 1 0 1 0 4 4 0 1 0 1 4 0110 2 2 0 4 10110 2 3 1 5 01101 2 3 ``` 

**Constraints:**

  * `1 <= s.length <= 4 * 104`
  * `s` consists only of characters `'0'` and `'1'`.

## Hints

1. Let us fix the starting index <code>l</code> of the substring and count the number of indices <code>r</code> such that <code>l <= r</code> and the substring <code>s[l..r]</code> has dominant ones.

2. A substring with dominant ones has at most <code>sqrt(n)</code> zeros.

3. We cannot iterate over every <code>r</code> and check if the  <code>s[l..r]</code> has dominant ones. Instead, we iterate over the next <code>sqrt(n)</code> zeros to the left of <code>l</code> and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.

## ✨ AI-Generated Solution (GEMINI)

### Approach

The problem asks us to count substrings `s[l..r]` where the number of ones (`ones`) is greater than or equal to the square of the number of zeros (`zeros`). That is, `ones >= zeros^2`. The length of the string `s` can be up to `4 * 10^4`.

A brute-force approach iterating over all `O(N^2)` substrings and counting `ones` and `zeros` for each would be too slow (`O(N^3)` or `O(N^2)` if using prefix sums).

The key observation comes from the constraint `ones >= zeros^2`:
Since `ones <= N` (the total length of the string), it must be that `N >= ones >= zeros^2`. This implies `zeros^2 <= N`, or `zeros <= sqrt(N)`. For `N = 4 * 10^4`, `sqrt(N) = 200`. This means any substring with dominant ones can have at most `sqrt(N)` zeros. Let `K = floor(sqrt(N))`.

This observation allows us to optimize the counting process. We can iterate through all possible starting positions `l` from `0` to `N-1`. For each `l`, we need to efficiently count valid `r`'s.

The strategy is as follows:
1.  **Precompute zero indices**: Create a list `all_zero_indices` containing the 0-indexed positions of all '0's in `s`. Add sentinels to `all_zero_indices`: `-1` at the beginning and `N` at the end. These sentinels simplify boundary conditions.
2.  **Iterate `l` (left pointer)**: For each `l` from `0` to `N-1`:
    a.  **Handle `zeros = 0` case**: Substrings `s[l..r]` with zero zeros consist entirely of '1's. For such substrings, `ones >= 0^2` is always true (since `ones >= 0`). We find the index in `all_zero_indices` corresponding to the first '0' at or after `l` using binary search (`bisect_left` in Python, `lower_bound` in C++, `Collections.binarySearch` in Java, custom `bisectLeft` in JS/TS, `sort.SearchInts` in Go). Let the position of this zero be `first_zero_pos_from_l`. All `r` in `[l, first_zero_pos_from_l - 1]` form substrings with zero zeros. The count of such substrings is `first_zero_pos_from_l - l`. Add this to the total answer.
    b.  **Handle `zeros > 0` cases**: Iterate `k_th_zero` from `1` to `K` (the maximum allowed number of zeros). For each `k_th_zero`:
        i.   Find the actual index of the `k_th_zero`-th '0' character at or after `l`. This is found by taking the index of the first zero at or after `l` (from step 2a) and adding `k_th_zero - 1` to it within `all_zero_indices`. Let this be `pos_of_kth_zero`. If `k_th_zero` zeros do not exist up to `N-1` (e.g., we ran out of zeros in `all_zero_indices`), break this inner loop.
        ii.  Find the actual index of the `(k_th_zero + 1)`-th '0' character at or after `l`. Let this be `pos_of_kplus1th_zero`. This defines the right boundary for `r` (exclusive) such that `s[l..r]` contains exactly `k_th_zero` zeros (i.e., `r` can go up to `pos_of_kplus1th_zero - 1`).
        iii. For `s[l..r]` to be dominant, we need `ones >= k_th_zero^2`. The number of ones in `s[l..r]` is `(r - l + 1) - k_th_zero`. So, we need `(r - l + 1) - k_th_zero >= k_th_zero^2`, which simplifies to `r >= l + k_th_zero^2 + k_th_zero - 1`. Let this minimum required `r` be `min_r_needed`.
        iv. Combine the constraints on `r`: `r` must be at least `pos_of_kth_zero` (to include the `k_th_zero`-th zero) and at least `min_r_needed` (for the dominant condition). So, the actual lower bound for `r` is `valid_r_start = max(pos_of_kth_zero, min_r_needed)`. The upper bound for `r` is `valid_r_end = pos_of_kplus1th_zero - 1`.
        v. If `valid_r_start <= valid_r_end`, then all `r` in this range are valid, and we add `(valid_r_end - valid_r_start + 1)` to the total answer.

By splitting the processing based on the number of zeros and leveraging the `zeros <= K` bound, this algorithm avoids the `O(N^2)` worst case when there are many '1's.

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
import bisect

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # K is the maximum number of zeros a dominant substring can have.
        # If ones >= zeros^2 and ones <= N, then N >= zeros^2 => zeros <= sqrt(N).
        k_max = int(n**0.5)
        
        # Precompute indices of all zeros, plus sentinels for easier boundary handling.
        # The first sentinel -1 handles cases where l=0 and s[0]='1'.
        # The last sentinel N handles cases where there are no more zeros until the end of string.
        all_zero_indices = [-1]
        for i in range(n):
            if s[i] == '0':
                all_zero_indices.append(i)
        all_zero_indices.append(n)
        
        for l in range(n):
            # Find the index in `all_zero_indices` of the first zero at or after `l`.
            # `bisect_left` returns the insertion point, which is exactly what we need.
            start_idx_in_zero_list = bisect.bisect_left(all_zero_indices, l)
            
            # Case 1: Substrings with 0 zeros (i.e., all '1's)
            # These substrings are s[l..r] where r is from l to (first_zero_pos_from_l - 1).
            first_zero_pos_from_l = all_zero_indices[start_idx_in_zero_list]
            if first_zero_pos_from_l > l: # Means s[l] is '1' and there are ones before the first zero
                # Any substring of only '1's is dominant (ones >= 0^2 always true).
                ans += (first_zero_pos_from_l - l)
            
            # Case 2: Substrings with `k_th_zero` zeros, where 1 <= k_th_zero <= k_max
            for k_th_zero in range(1, k_max + 1):
                # `current_zero_list_idx` points to the `k_th_zero`-th actual zero index relative to `l`'s first zero.
                current_zero_list_idx = start_idx_in_zero_list + k_th_zero - 1
                
                # If we've run out of zeros in the string for this `k_th_zero` count.
                # `len(all_zero_indices) - 1` is the index of the last sentinel (N).
                if current_zero_list_idx >= len(all_zero_indices) - 1:
                    break # No more k_th_zero zeros possible from l
                
                # `pos_of_kth_zero` is the actual index of the k_th zero in `s`.
                # `pos_of_kplus1th_zero` is the actual index of the (k+1)-th zero in `s`.
                # Substrings s[l..r] with exactly `k_th_zero` zeros will have `r` in range
                # [pos_of_kth_zero, pos_of_kplus1th_zero - 1].
                pos_of_kth_zero = all_zero_indices[current_zero_list_idx]
                pos_of_kplus1th_zero = all_zero_indices[current_zero_list_idx + 1]
                
                # Calculate the minimum 'r' required for `s[l..r]` to be dominant for this `k_th_zero`.
                # ones = (r - l + 1) - k_th_zero
                # Condition: (r - l + 1) - k_th_zero >= k_th_zero^2
                # r - l + 1 >= k_th_zero^2 + k_th_zero
                # r >= l + k_th_zero^2 + k_th_zero - 1
                min_r_needed = l + k_th_zero**2 + k_th_zero - 1
                
                # The valid range for `r` is limited by `pos_of_kth_zero` and `pos_of_kplus1th_zero`.
                # `r` must be at least `pos_of_kth_zero` to include the `k_th_zero`-th zero.
                # `r` must be at most `pos_of_kplus1th_zero - 1` to not include the `(k+1)`-th zero.
                valid_r_start = max(pos_of_kth_zero, min_r_needed)
                valid_r_end = pos_of_kplus1th_zero - 1
                
                # If the valid range is non-empty, add the count of `r` values.
                if valid_r_start <= valid_r_end:
                    ans += (valid_r_end - valid_r_start + 1)
                    
        return ans
```

  </div>

  <div class="tab-panel" data-lang="java">

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public long numberOfSubstrings(String s) {
        int n = s.length();
        long ans = 0;
        
        // K is the maximum number of zeros a dominant substring can have.
        // If ones >= zeros^2 and ones <= N, then N >= zeros^2 => zeros <= sqrt(N).
        int kMax = (int) Math.sqrt(n);
        
        // Precompute indices of all zeros, plus sentinels for easier boundary handling.
        // The first sentinel -1 handles cases where l=0 and s[0]='1'.
        // The last sentinel n handles cases where there are no more zeros until the end of string.
        List<Integer> allZeroIndices = new ArrayList<>();
        allZeroIndices.add(-1);
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') {
                allZeroIndices.add(i);
            }
        }
        allZeroIndices.add(n);
        
        for (int l = 0; l < n; l++) {
            // Find the index in `allZeroIndices` of the first zero at or after `l`.
            // `Collections.binarySearch` returns (-(insertion point) - 1) if not found.
            // The insertion point is the index where the element would be inserted to maintain sorted order.
            int startIdxInZeroList = Collections.binarySearch(allZeroIndices, l);
            if (startIdxInZeroList < 0) {
                startIdxInZeroList = -startIdxInZeroList - 1;
            }
            
            // Case 1: Substrings with 0 zeros (i.e., all '1's)
            // These substrings are s[l..r] where r is from l to (firstZeroPosFromL - 1).
            int firstZeroPosFromL = allZeroIndices.get(startIdxInZeroList);
            if (firstZeroPosFromL > l) { // Means s[l] is '1' and there are ones before the first zero
                // Any substring of only '1's is dominant (ones >= 0^2 always true).
                ans += (firstZeroPosFromL - l);
            }
            
            // Case 2: Substrings with `k_th_zero` zeros, where 1 <= k_th_zero <= kMax
            for (int kThZero = 1; kThZero <= kMax; kThZero++) {
                // `currentZeroListIdx` points to the `k_th_zero`-th actual zero index relative to `l`'s first zero.
                int currentZeroListIdx = startIdxInZeroList + kThZero - 1;
                
                // If we've run out of zeros in the string for this `k_th_zero` count.
                // `allZeroIndices.size() - 1` is the index of the last sentinel (N).
                if (currentZeroListIdx >= allZeroIndices.size() - 1) {
                    break; // No more k_th_zero zeros possible from l
                }
                
                // `posOfKthZero` is the actual index of the k_th zero in `s`.
                // `posOfKplus1thZero` is the actual index of the (k+1)-th zero in `s`.
                // Substrings s[l..r] with exactly `k_th_zero` zeros will have `r` in range
                // [posOfKthZero, posOfKplus1thZero - 1].
                int posOfKthZero = allZeroIndices.get(currentZeroListIdx);
                int posOfKplus1thZero = allZeroIndices.get(currentZeroListIdx + 1);
                
                // Calculate the minimum 'r' required for `s[l..r]` to be dominant for this `k_th_zero`.
                // ones = (r - l + 1) - k_th_zero
                // Condition: (r - l + 1) - k_th_zero >= k_th_zero^2
                // r - l + 1 >= k_th_zero^2 + k_th_zero
                // r >= l + k_th_zero^2 + k_th_zero - 1
                long minRNeeded = (long)l + (long)kThZero * kThZero + kThZero - 1;
                
                // The valid range for `r` is limited by `posOfKthZero` and `posOfKplus1thZero`.
                // `r` must be at least `posOfKthZero` to include the `k_th_zero`-th zero.
                // `r` must be at most `posOfKplus1thZero - 1` to not include the `(k+1)`-th zero.
                long validRStart = Math.max(posOfKthZero, minRNeeded);
                long validREnd = posOfKplus1thZero - 1;
                
                // If the valid range is non-empty, add the count of `r` values.
                if (validRStart <= validREnd) {
                    ans += (validREnd - validRStart + 1);
                }
            }
        }
        
        return ans;
    }
}
```

  </div>

  <div class="tab-panel" data-lang="cpp">

```cpp
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

class Solution {
public:
    long long numberOfSubstrings(std::string s) {
        int n = s.length();
        long long ans = 0;
        
        // K is the maximum number of zeros a dominant substring can have.
        // If ones >= zeros^2 and ones <= N, then N >= zeros^2 => zeros <= sqrt(N).
        int k_max = static_cast<int>(std::sqrt(n));
        
        // Precompute indices of all zeros, plus sentinels for easier boundary handling.
        // The first sentinel -1 handles cases where l=0 and s[0]='1'.
        // The last sentinel n handles cases where there are no more zeros until the end of string.
        std::vector<int> all_zero_indices;
        all_zero_indices.push_back(-1);
        for (int i = 0; i < n; ++i) {
            if (s[i] == '0') {
                all_zero_indices.push_back(i);
            }
        }
        all_zero_indices.push_back(n);
        
        for (int l = 0; l < n; ++l) {
            // Find the iterator to the first zero in `all_zero_indices` at or after `l`.
            auto it = std::lower_bound(all_zero_indices.begin(), all_zero_indices.end(), l);
            int start_idx_in_zero_list = std::distance(all_zero_indices.begin(), it);
            
            // Case 1: Substrings with 0 zeros (i.e., all '1's)
            // These substrings are s[l..r] where r is from l to (first_zero_pos_from_l - 1).
            int first_zero_pos_from_l = all_zero_indices[start_idx_in_zero_list];
            if (first_zero_pos_from_l > l) { // Means s[l] is '1' and there are ones before the first zero
                // Any substring of only '1's is dominant (ones >= 0^2 always true).
                ans += (first_zero_pos_from_l - l);
            }
            
            // Case 2: Substrings with `k_th_zero` zeros, where 1 <= k_th_zero <= k_max
            for (int k_th_zero = 1; k_th_zero <= k_max; ++k_th_zero) {
                // `current_zero_list_idx` points to the `k_th_zero`-th actual zero index relative to `l`'s first zero.
                int current_zero_list_idx = start_idx_in_zero_list + k_th_zero - 1;
                
                // If we've run out of zeros in the string for this `k_th_zero` count.
                // `all_zero_indices.size() - 1` is the index of the last sentinel (N).
                if (current_zero_list_idx >= all_zero_indices.size() - 1) {
                    break; // No more k_th_zero zeros possible from l
                }
                
                // `pos_of_kth_zero` is the actual index of the k_th zero in `s`.
                // `pos_of_kplus1th_zero` is the actual index of the (k+1)-th zero in `s`.
                // Substrings s[l..r] with exactly `k_th_zero` zeros will have `r` in range
                // [pos_of_kth_zero, pos_of_kplus1th_zero - 1].
                int pos_of_kth_zero = all_zero_indices[current_zero_list_idx];
                int pos_of_kplus1th_zero = all_zero_indices[current_zero_list_idx + 1];
                
                // Calculate the minimum 'r' required for `s[l..r]` to be dominant for this `k_th_zero`.
                // ones = (r - l + 1) - k_th_zero
                // Condition: (r - l + 1) - k_th_zero >= k_th_zero^2
                // r - l + 1 >= k_th_zero^2 + k_th_zero
                // r >= l + k_th_zero^2 + k_th_zero - 1
                long long min_r_needed = (long long)l + (long long)k_th_zero * k_th_zero + k_th_zero - 1;
                
                // The valid range for `r` is limited by `pos_of_kth_zero` and `pos_of_kplus1th_zero`.
                // `r` must be at least `pos_of_kth_zero` to include the `k_th_zero`-th zero.
                // `r` must be at most `pos_of_kplus1th_zero - 1` to not include the `(k+1)`-th zero.
                long long valid_r_start = std::max((long long)pos_of_kth_zero, min_r_needed);
                long long valid_r_end = pos_of_kplus1th_zero - 1;
                
                // If the valid range is non-empty, add the count of `r` values.
                if (valid_r_start <= valid_r_end) {
                    ans += (valid_r_end - valid_r_start + 1);
                }
            }
        }
        
        return ans;
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
    let ans = 0;
    
    // K is the maximum number of zeros a dominant substring can have.
    // If ones >= zeros^2 and ones <= N, then N >= zeros^2 => zeros <= sqrt(N).
    const kMax = Math.floor(Math.sqrt(n));
    
    // Precompute indices of all zeros, plus sentinels for easier boundary handling.
    // The first sentinel -1 handles cases where l=0 and s[0]='1'.
    // The last sentinel n handles cases where there are no more zeros until the end of string.
    const allZeroIndices = [-1];
    for (let i = 0; i < n; i++) {
        if (s[i] === '0') {
            allZeroIndices.push(i);
        }
    }
    allZeroIndices.push(n);
    
    // Custom binary search equivalent to bisect_left
    const bisectLeft = (arr, x) => {
        let low = 0;
        let high = arr.length;
        while (low < high) {
            const mid = Math.floor((low + high) / 2);
            if (arr[mid] < x) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    };
    
    for (let l = 0; l < n; l++) {
        // Find the index in `allZeroIndices` of the first zero at or after `l`.
        const startIdxInZeroList = bisectLeft(allZeroIndices, l);
        
        // Case 1: Substrings with 0 zeros (i.e., all '1's)
        // These substrings are s[l..r] where r is from l to (firstZeroPosFromL - 1).
        const firstZeroPosFromL = allZeroIndices[startIdxInZeroList];
        if (firstZeroPosFromL > l) { // Means s[l] is '1' and there are ones before the first zero
            // Any substring of only '1's is dominant (ones >= 0^2 always true).
            ans += (firstZeroPosFromL - l);
        }
        
        // Case 2: Substrings with `k_th_zero` zeros, where 1 <= k_th_zero <= kMax
        for (let kThZero = 1; kThZero <= kMax; kThZero++) {
            // `currentZeroListIdx` points to the `k_th_zero`-th actual zero index relative to `l`'s first zero.
            const currentZeroListIdx = startIdxInZeroList + kThZero - 1;
            
            // If we've run out of zeros in the string for this `k_th_zero` count.
            // `allZeroIndices.length - 1` is the index of the last sentinel (N).
            if (currentZeroListIdx >= allZeroIndices.length - 1) {
                break; // No more k_th_zero zeros possible from l
            }
            
            // `posOfKthZero` is the actual index of the k_th zero in `s`.
            // `posOfKplus1thZero` is the actual index of the (k+1)-th zero in `s`.
            // Substrings s[l..r] with exactly `k_th_zero` zeros will have `r` in range
            // [posOfKthZero, posOfKplus1thZero - 1].
            const posOfKthZero = allZeroIndices[currentZeroListIdx];
            const posOfKplus1thZero = allZeroIndices[currentZeroListIdx + 1];
            
            // Calculate the minimum 'r' required for `s[l..r]` to be dominant for this `k_th_zero`.
            // ones = (r - l + 1) - k_th_zero
            // Condition: (r - l + 1) - k_th_zero >= k_th_zero^2
            // r - l + 1 >= k_th_zero^2 + k_th_zero
            // r >= l + k_th_zero^2 + k_th_zero - 1
            const minRNeeded = l + kThZero * kThZero + kThZero - 1;
            
            // The valid range for `r` is limited by `posOfKthZero` and `posOfKplus1thZero`.
            // `r` must be at least `posOfKthZero` to include the `k_th_zero`-th zero.
            // `r` must be at most `posOfKplus1thZero - 1` to not include the `(k+1)`-th zero.
            const validRStart = Math.max(posOfKthZero, minRNeeded);
            const validREnd = posOfKplus1thZero - 1;
            
            // If the valid range is non-empty, add the count of `r` values.
            if (validRStart <= validREnd) {
                ans += (validREnd - validRStart + 1);
            }
        }
    }
    
    return ans;
};
```

  </div>

  <div class="tab-panel" data-lang="typescript">

```typescript
function numberOfSubstrings(s: string): number {
    const n: number = s.length;
    let ans: number = 0;
    
    // K is the maximum number of zeros a dominant substring can have.
    // If ones >= zeros^2 and ones <= N, then N >= zeros^2 => zeros <= sqrt(N).
    const kMax: number = Math.floor(Math.sqrt(n));
    
    // Precompute indices of all zeros, plus sentinels for easier boundary handling.
    // The first sentinel -1 handles cases where l=0 and s[0]='1'.
    // The last sentinel n handles cases where there are no more zeros until the end of string.
    const allZeroIndices: number[] = [-1];
    for (let i = 0; i < n; i++) {
        if (s[i] === '0') {
            allZeroIndices.push(i);
        }
    }
    allZeroIndices.push(n);
    
    // Custom binary search equivalent to bisect_left
    const bisectLeft = (arr: number[], x: number): number => {
        let low = 0;
        let high = arr.length;
        while (low < high) {
            const mid = Math.floor((low + high) / 2);
            if (arr[mid] < x) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    };
    
    for (let l = 0; l < n; l++) {
        // Find the index in `allZeroIndices` of the first zero at or after `l`.
        const startIdxInZeroList = bisectLeft(allZeroIndices, l);
        
        // Case 1: Substrings with 0 zeros (i.e., all '1's)
        // These substrings are s[l..r] where r is from l to (firstZeroPosFromL - 1).
        const firstZeroPosFromL = allZeroIndices[startIdxInZeroList];
        if (firstZeroPosFromL > l) { // Means s[l] is '1' and there are ones before the first zero
            // Any substring of only '1's is dominant (ones >= 0^2 always true).
            ans += (firstZeroPosFromL - l);
        }
        
        // Case 2: Substrings with `k_th_zero` zeros, where 1 <= k_th_zero <= kMax
        for (let kThZero = 1; kThZero <= kMax; kThZero++) {
            // `currentZeroListIdx` points to the `k_th_zero`-th actual zero index relative to `l`'s first zero.
            const currentZeroListIdx = startIdxInZeroList + kThZero - 1;
            
            // If we've run out of zeros in the string for this `k_th_zero` count.
            // `allZeroIndices.length - 1` is the index of the last sentinel (N).
            if (currentZeroListIdx >= allZeroIndices.length - 1) {
                break; // No more k_th_zero zeros possible from l
            }
            
            // `posOfKthZero` is the actual index of the k_th zero in `s`.
            // `posOfKplus1thZero` is the actual index of the (k+1)-th zero in `s`.
            // Substrings s[l..r] with exactly `k_th_zero` zeros will have `r` in range
            // [posOfKthZero, posOfKplus1thZero - 1].
            const posOfKthZero = allZeroIndices[currentZeroListIdx];
            const posOfKplus1thZero = allZeroIndices[currentZeroListIdx + 1];
            
            // Calculate the minimum 'r' required for `s[l..r]` to be dominant for this `k_th_zero`.
            // ones = (r - l + 1) - k_th_zero
            // Condition: (r - l + 1) - k_th_zero >= k_th_zero^2
            // r - l + 1 >= k_th_zero^2 + k_th_zero
            // r >= l + k_th_zero^2 + k_th_zero - 1
            const minRNeeded: number = l + kThZero * kThZero + kThZero - 1;
            
            // The valid range for `r` is limited by `posOfKthZero` and `posOfKplus1thZero`.
            // `r` must be at least `posOfKthZero` to include the `k_th_zero`-th zero.
            // `r` must be at most `posOfKplus1thZero - 1` to not include the `(k+1)`-th zero.
            const validRStart: number = Math.max(posOfKthZero, minRNeeded);
            const validREnd: number = posOfKplus1thZero - 1;
            
            // If the valid range is non-empty, add the count of `r` values.
            if (validRStart <= validREnd) {
                ans += (validREnd - validRStart + 1);
            }
        }
    }
    
    return ans;
}
```

  </div>

  <div class="tab-panel" data-lang="go">

```go
package main

import (
	"math"
	"sort"
)

func numberOfSubstrings(s string) int64 {
	n := len(s)
	ans := int64(0)

	// K is the maximum number of zeros a dominant substring can have.
	// If ones >= zeros^2 and ones <= N, then N >= zeros^2 => zeros <= sqrt(N).
	kMax := int(math.Sqrt(float64(n)))

	// Precompute indices of all zeros, plus sentinels for easier boundary handling.
	// The first sentinel -1 handles cases where l=0 and s[0]='1'.
	// The last sentinel n handles cases where there are no more zeros until the end of string.
	allZeroIndices := []int{-1}
	for i := 0; i < n; i++ {
		if s[i] == '0' {
			allZeroIndices = append(allZeroIndices, i)
		}
	}
	allZeroIndices = append(allZeroIndices, n)

	for l := 0; l < n; l++ {
		// Find the index in `allZeroIndices` of the first zero at or after `l`.
		// `sort.SearchInts` returns the index of the first element >= x.
		startIdxInZeroList := sort.SearchInts(allZeroIndices, l)

		// Case 1: Substrings with 0 zeros (i.e., all '1's)
		// These substrings are s[l..r] where r is from l to (firstZeroPosFromL - 1).
		firstZeroPosFromL := allZeroIndices[startIdxInZeroList]
		if firstZeroPosFromL > l { // Means s[l] is '1' and there are ones before the first zero
			// Any substring of only '1's is dominant (ones >= 0^2 always true).
			ans += int64(firstZeroPosFromL - l)
		}

		// Case 2: Substrings with `k_th_zero` zeros, where 1 <= k_th_zero <= kMax
		for kThZero := 1; kThZero <= kMax; kThZero++ {
			// `currentZeroListIdx` points to the `k_th_zero`-th actual zero index relative to `l`'s first zero.
			currentZeroListIdx := startIdxInZeroList + kThZero - 1

			// If we've run out of zeros in the string for this `k_th_zero` count.
			// `len(allZeroIndices) - 1` is the index of the last sentinel (n).
			if currentZeroListIdx >= len(allZeroIndices)-1 {
				break // No more k_th_zero zeros possible from l
			}

			// `posOfKthZero` is the actual index of the k_th zero in `s`.
			// `posOfKplus1thZero` is the actual index of the (k+1)-th zero in `s`.
			// Substrings s[l..r] with exactly `k_th_zero` zeros will have `r` in range
			// [posOfKthZero, posOfKplus1thZero - 1].
			posOfKthZero := allZeroIndices[currentZeroListIdx]
			posOfKplus1thZero := allZeroIndices[currentZeroListIdx+1]

			// Calculate the minimum 'r' required for `s[l..r]` to be dominant for this `k_th_zero`.
			// ones = (r - l + 1) - k_th_zero
			// Condition: (r - l + 1) - k_th_zero >= k_th_zero^2
			// r - l + 1 >= k_th_zero^2 + k_th_zero
			// r >= l + k_th_zero^2 + k_th_zero - 1
			minRNeeded := int64(l) + int64(kThZero)*int64(kThZero) + int64(kThZero) - 1

			// The valid range for `r` is limited by `posOfKthZero` and `posOfKplus1thZero`.
			// `r` must be at least `posOfKthZero` to include the `k_th_zero`-th zero.
			// `r` must be at most `posOfKplus1thZero - 1` to not include the `(k+1)`-th zero.
			validRStart := int64(posOfKthZero)
			if minRNeeded > validRStart {
				validRStart = minRNeeded
			}
			validREnd := int64(posOfKplus1thZero - 1)

			// If the valid range is non-empty, add the count of `r` values.
			if validRStart <= validREnd {
				ans += (validREnd - validRStart + 1)
			}
		}
	}

	return ans
}
```

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(N * sqrt(N))

1.  **Preprocessing**: Building `all_zero_indices` takes `O(N)` time.
2.  **Outer loop (for `l`)**: This loop runs `N` times.
3.  **Inside the outer loop**:
    a.  A binary search operation (like `bisect_left` or `lower_bound`) on `all_zero_indices` takes `O(log M)` time, where `M` is the number of zeros. Since `M <= N`, this is `O(log N)`.
    b.  The `zeros=0` case calculation is `O(1)`.
    c.  The inner loop for `k_th_zero` runs at most `K = floor(sqrt(N))` times.
    d.  Inside the inner loop, all operations (array indexing, arithmetic) are `O(1)`.

Thus, the total time complexity is `N * (log N + K) = N * (log N + sqrt(N))`. Since `sqrt(N)` dominates `log N` for large `N`, the overall time complexity is `O(N * sqrt(N))`. Given `N = 4 * 10^4`, `N * sqrt(N) = 4 * 10^4 * 200 = 8 * 10^6`, which is efficient enough.

- **Space Complexity:** O(N)

The `all_zero_indices` list stores the indices of all '0's in the string `s`. In the worst case (e.g., `s` consists entirely of '0's), this list will contain `N+2` elements (including sentinels). Therefore, the space complexity is `O(N)`.
