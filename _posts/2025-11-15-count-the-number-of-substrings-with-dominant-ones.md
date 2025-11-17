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

The core idea relies on a key observation: for a substring `s[l..r]` with `Z` zeros and `O` ones, to be "dominant" (i.e., `O >= Z^2`), the number of zeros `Z` must be relatively small. Since `O + Z` is the length of the substring and `O + Z <= N` (total string length), it must be that `N - Z >= O >= Z^2`. This implies `Z^2 + Z - N <= 0`. Solving this quadratic inequality for `Z`, we find that `Z <= (-1 + sqrt(1 + 4N)) / 2`. For `N=4*10^4`, this upper bound for `Z` is approximately `199`. Let `K_MAX_Z` be this maximum possible number of zeros (e.g., 200). Any substring with more than `K_MAX_Z` zeros cannot be dominant.

This constraint on `Z` allows for an optimized counting strategy:

1.  **Prefix Sums**: First, we precompute `pref_zeros` and `pref_ones` arrays. `pref_zeros[i]` stores the count of '0's in the prefix `s[0...i-1]`, and `pref_ones[i]` stores the count of '1's in `s[0...i-1]`. `pref_zeros[0]` and `pref_ones[0]` are 0, representing an empty prefix.

2.  **Iterate Right Endpoints `r`**: We iterate through each possible right endpoint `r` of a substring `s[l..r]` from `0` to `N-1`.

3.  **Iterate Zero Counts `z`**: For each `r`, we iterate through all possible numbers of zeros `z` that `s[l..r]` could contain, from `0` up to `K_MAX_Z`. Note that `z` also cannot exceed `pref_zeros[r+1]` (the total zeros up to `r`).

4.  **Derive `l` conditions**: For a fixed `r` and `z`:
    *   The number of zeros in `s[0...r]` is `pref_zeros[r+1]`. If `s[l..r]` has `z` zeros, then `s[0...l-1]` (where `j=l-1`) must have `pref_zeros[j] = pref_zeros[r+1] - z`. Let this be `target_prev_zeros`.
    *   The number of ones in `s[0...r]` is `pref_ones[r+1]`. The dominant condition `O >= Z^2` becomes `(pref_ones[r+1] - pref_ones[j]) >= z^2`. Rearranging, we need `pref_ones[j] <= pref_ones[r+1] - z^2`. Let this be `required_prev_ones_upper_bound`.

5.  **Efficient Counting**: To count `j`s (and thus `l`s) that satisfy both conditions for current `r` and `z`:
    *   We use a hash map `zeros_to_ones_map`. `zeros_to_ones_map[k]` stores a list of `pref_ones` values for all indices `j` where `pref_zeros[j] = k`. These lists are kept sorted.
    *   For the `target_prev_zeros`, we retrieve its corresponding `ones_list` from the map. Since this list is sorted, we can use binary search (e.g., Python's `bisect_right`) to find how many elements in `ones_list` are less than or equal to `required_prev_ones_upper_bound`. This count is added to our total answer.

6.  **Update Map**: After iterating through all `z` for the current `r`, we add `pref_ones[r+1]` to `zeros_to_ones_map[pref_zeros[r+1]]`. Since `pref_ones` values are non-decreasing as `r` increases, appending new values keeps the lists within `zeros_to_ones_map` sorted, which is essential for `bisect_right`.

7.  **Base Case**: Initialize `zeros_to_ones_map[0].append(0)` to account for the empty prefix `s[0...-1]`, which has 0 zeros and 0 ones (representing `j=-1`).

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
    <label for="lang-javascript">JS</label>
    <label for="lang-typescript">TS</label>
    <label for="lang-go">Go</label>
  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
import collections
import math
import bisect

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        # K_MAX_Z is the maximum possible number of zeros in a dominant substring.
        # If Z zeros, O ones, then O >= Z^2.
        # Also O + Z <= N. So N - Z >= O >= Z^2.
        # This implies Z^2 + Z - N <= 0.
        # The maximum Z is floor((-1 + sqrt(1 + 4N)) / 2).
        # For N = 4 * 10^4, Z_max is 199.
        K_MAX_Z = int((math.sqrt(1 + 4 * n) - 1) / 2)
        
        # Prefixes sums for zeros and ones. pref_zeros[i] is count up to index i-1.
        # So pref_zeros[0] = 0, pref_zeros[i] for s[0...i-1].
        pref_zeros = [0] * (n + 1)
        pref_ones = [0] * (n + 1)
        for i in range(n):
            pref_zeros[i+1] = pref_zeros[i] + (1 if s[i] == '0' else 0)
            pref_ones[i+1] = pref_ones[i] + (1 if s[i] == '1' else 0)

        # zeros_to_ones_map stores lists of pref_ones values for specific pref_zeros counts.
        # zeros_to_ones_map[z_count] = [o1, o2, o3, ...]
        # Each list must be sorted to use bisect_right, which is maintained by appending
        # as pref_ones is non-decreasing with increasing 'r'.
        zeros_to_ones_map = collections.defaultdict(list)
        
        # Initialize for prefix up to index -1 (empty string or for l=0).
        # pref_zeros[-1] = 0, pref_ones[-1] = 0
        zeros_to_ones_map[0].append(0)

        for r in range(n):
            # current_total_zeros and current_total_ones are for prefix s[0...r]
            current_total_zeros = pref_zeros[r+1]
            current_total_ones = pref_ones[r+1]

            # Iterate through all possible number of zeros 'z' in substring s[l...r]
            # 'z' can range from 0 up to K_MAX_Z.
            # 'z' also cannot be more than current_total_zeros.
            for z in range(min(K_MAX_Z, current_total_zeros) + 1):
                # We are looking for an index `j` (which corresponds to `l-1`) such that:
                # 1. Number of zeros in s[0...j] is `target_prev_zeros`.
                #    `target_prev_zeros = current_total_zeros - z`
                # 2. Number of ones in s[0...j] (`pref_ones[j]`) satisfies the dominant condition:
                #    `(current_total_ones - pref_ones[j]) >= z*z`
                #    which rearranges to `pref_ones[j] <= current_total_ones - z*z`
                
                target_prev_zeros = current_total_zeros - z
                
                # `target_prev_zeros` is guaranteed to be non-negative due to loop range of `z`.
                
                required_prev_ones_upper_bound = current_total_ones - z * z

                # Find `j`s in `zeros_to_ones_map[target_prev_zeros]` that satisfy the `pref_ones` condition.
                if target_prev_zeros in zeros_to_ones_map:
                    ones_list = zeros_to_ones_map[target_prev_zeros]
                    # `bisect.bisect_right` returns an insertion point that ensures elements to its left are <= value.
                    count = bisect.bisect_right(ones_list, required_prev_ones_upper_bound)
                    ans += count
            
            # Add current prefix (s[0...r]) sums to the map for future iterations.
            zeros_to_ones_map[current_total_zeros].append(current_total_ones)
        
        return ans
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public long numberOfSubstrings(String s) {
        int n = s.length();
        long ans = 0;

        // K_MAX_Z is the maximum possible number of zeros in a dominant substring.
        // Derived from Z^2 + Z - N <= 0.
        int K_MAX_Z = (int) Math.floor((-1 + Math.sqrt(1 + 4L * n)) / 2);
        
        // Prefix sums for zeros and ones. prefZeros[i] is count up to index i-1.
        int[] prefZeros = new int[n + 1];
        int[] prefOnes = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefZeros[i+1] = prefZeros[i] + (s.charAt(i) == '0' ? 1 : 0);
            prefOnes[i+1] = prefOnes[i] + (s.charAt(i) == '1' ? 1 : 0);
        }

        // zerosToOnesMap stores lists of prefOnes values for specific prefZeros counts.
        // Map<Integer, List<Integer>> zerosToOnesMap = new HashMap<>();
        // Using a custom class to optimize memory as N is large
        // Or just accept that HashMap<Integer, ArrayList<Integer>> is standard.
        Map<Integer, List<Integer>> zerosToOnesMap = new HashMap<>();
        
        // Initialize for prefix up to index -1 (empty string or for l=0).
        // prefZeros[-1] = 0, prefOnes[-1] = 0
        zerosToOnesMap.computeIfAbsent(0, k -> new ArrayList<>()).add(0);

        for (int r = 0; r < n; r++) {
            // currentTotalZeros and currentTotalOnes are for prefix s[0...r]
            int currentTotalZeros = prefZeros[r+1];
            int currentTotalOnes = prefOnes[r+1];

            // Iterate through all possible number of zeros 'z' in substring s[l...r]
            // 'z' can range from 0 up to K_MAX_Z.
            // 'z' also cannot be more than currentTotalZeros.
            for (int z = 0; z <= Math.min(K_MAX_Z, currentTotalZeros); z++) {
                // We are looking for an index `j` (which corresponds to `l-1`) such that:
                // 1. Number of zeros in s[0...j] is `targetPrevZeros`.
                //    `targetPrevZeros = currentTotalZeros - z`
                // 2. Number of ones in s[0...j] (`prefOnes[j]`) satisfies the dominant condition:
                //    `(currentTotalOnes - prefOnes[j]) >= z*z`
                //    which rearranges to `prefOnes[j] <= currentTotalOnes - z*z`
                
                int targetPrevZeros = currentTotalZeros - z;
                
                // `targetPrevZeros` is guaranteed to be non-negative due to loop range of `z`.
                
                long requiredPrevOnesUpperBound = currentTotalOnes - (long)z * z;

                // Find `j`s in `zerosToOnesMap[targetPrevZeros]` that satisfy the `prefOnes` condition.
                if (zerosToOnesMap.containsKey(targetPrevZeros)) {
                    List<Integer> onesList = zerosToOnesMap.get(targetPrevZeros);
                    // `Collections.binarySearch` returns index of key if found, or `(-(insertion point) - 1)` if not found.
                    // `insertion point` is the index at which the key would be inserted so that the list remains sorted.
                    // We need to count elements <= `requiredPrevOnesUpperBound`.
                    int idx = Collections.binarySearch(onesList, (int)requiredPrevOnesUpperBound);
                    if (idx < 0) {
                        idx = -idx - 1; // This is the count of elements <= requiredPrevOnesUpperBound
                    } else {
                        // If found, there might be duplicates. Need to find the first element > requiredPrevOnesUpperBound.
                        // `binarySearch` only guarantees finding *an* index if duplicates exist. Iterate right.
                        while (idx < onesList.size() && onesList.get(idx) <= requiredPrevOnesUpperBound) {
                            idx++;
                        }
                    }
                    ans += idx;
                }
            }
            
            // Add current prefix (s[0...r]) sums to the map for future iterations.
            // Ensure the list for currentTotalZeros is created if it doesn't exist.
            zerosToOnesMap.computeIfAbsent(currentTotalZeros, k -> new ArrayList<>()).add(currentTotalOnes);
        }
        
        return ans;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>

class Solution {
public:
    long long numberOfSubstrings(std::string s) {
        int n = s.length();
        long long ans = 0;

        // K_MAX_Z is the maximum possible number of zeros in a dominant substring.
        // Derived from Z^2 + Z - N <= 0.
        int K_MAX_Z = static_cast<int>(std::floor((-1 + std::sqrt(1 + 4LL * n)) / 2));
        
        // Prefix sums for zeros and ones. prefZeros[i] is count up to index i-1.
        std::vector<int> prefZeros(n + 1, 0);
        std::vector<int> prefOnes(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefZeros[i+1] = prefZeros[i] + (s[i] == '0' ? 1 : 0);
            prefOnes[i+1] = prefOnes[i] + (s[i] == '1' ? 1 : 0);
        }

        // zerosToOnesMap stores vectors of prefOnes values for specific prefZeros counts.
        // std::map<int, std::vector<int>> zerosToOnesMap;
        // For competitive programming, unordered_map might be faster on average,
        // but map is safer for worst-case performance guarantees and doesn't require custom hash.
        std::map<int, std::vector<int>> zerosToOnesMap;
        
        // Initialize for prefix up to index -1 (empty string or for l=0).
        // prefZeros[-1] = 0, prefOnes[-1] = 0
        zerosToOnesMap[0].push_back(0);

        for (int r = 0; r < n; ++r) {
            // currentTotalZeros and currentTotalOnes are for prefix s[0...r]
            int currentTotalZeros = prefZeros[r+1];
            int currentTotalOnes = prefOnes[r+1];

            // Iterate through all possible number of zeros 'z' in substring s[l...r]
            // 'z' can range from 0 up to K_MAX_Z.
            // 'z' also cannot be more than currentTotalZeros.
            for (int z = 0; z <= std::min(K_MAX_Z, currentTotalZeros); ++z) {
                // We are looking for an index `j` (which corresponds to `l-1`) such that:
                // 1. Number of zeros in s[0...j] is `targetPrevZeros`.
                //    `targetPrevZeros = currentTotalZeros - z`
                // 2. Number of ones in s[0...j] (`prefOnes[j]`) satisfies the dominant condition:
                //    `(currentTotalOnes - prefOnes[j]) >= z*z`
                //    which rearranges to `prefOnes[j] <= currentTotalOnes - z*z`
                
                int targetPrevZeros = currentTotalZeros - z;
                
                // `targetPrevZeros` is guaranteed to be non-negative due to loop range of `z`.
                
                long long requiredPrevOnesUpperBound = currentTotalOnes - (long long)z * z;

                // Find `j`s in `zerosToOnesMap[targetPrevZeros]` that satisfy the `prefOnes` condition.
                auto it = zerosToOnesMap.find(targetPrevZeros);
                if (it != zerosToOnesMap.end()) {
                    std::vector<int>& onesList = it->second;
                    // `std::upper_bound` returns an iterator to the first element that is greater than `value`.
                    // The distance from `begin()` to this iterator gives the count of elements <= `value`.
                    auto upper_bound_it = std::upper_bound(onesList.begin(), onesList.end(), requiredPrevOnesUpperBound);
                    ans += std::distance(onesList.begin(), upper_bound_it);
                }
            }
            
            // Add current prefix (s[0...r]) sums to the map for future iterations.
            // The `prefOnes` values within each vector will remain sorted because `prefOnes` is non-decreasing over 'r'.
            zerosToOnesMap[currentTotalZeros].push_back(currentTotalOnes);
        }
        
        return ans;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const n = s.length;
    let ans = 0;

    // K_MAX_Z is the maximum possible number of zeros in a dominant substring.
    // Derived from Z^2 + Z - N <= 0.
    const K_MAX_Z = Math.floor((-1 + Math.sqrt(1 + 4 * n)) / 2);
    
    // Prefix sums for zeros and ones. prefZeros[i] is count up to index i-1.
    const prefZeros = new Array(n + 1).fill(0);
    const prefOnes = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefZeros[i+1] = prefZeros[i] + (s[i] === '0' ? 1 : 0);
        prefOnes[i+1] = prefOnes[i] + (s[i] === '1' ? 1 : 0);
    }

    // zerosToOnesMap stores arrays of prefOnes values for specific prefZeros counts.
    // Map<Integer, Array<Integer>>
    const zerosToOnesMap = new Map();
    
    // Initialize for prefix up to index -1 (empty string or for l=0).
    // prefZeros[-1] = 0, prefOnes[-1] = 0
    zerosToOnesMap.set(0, [0]);

    for (let r = 0; r < n; r++) {
        // currentTotalZeros and currentTotalOnes are for prefix s[0...r]
        const currentTotalZeros = prefZeros[r+1];
        const currentTotalOnes = prefOnes[r+1];

        // Iterate through all possible number of zeros 'z' in substring s[l...r]
        // 'z' can range from 0 up to K_MAX_Z.
        // 'z' also cannot be more than currentTotalZeros.
        for (let z = 0; z <= Math.min(K_MAX_Z, currentTotalZeros); z++) {
            // We are looking for an index `j` (which corresponds to `l-1`) such that:
            // 1. Number of zeros in s[0...j] is `targetPrevZeros`.
            //    `targetPrevZeros = currentTotalZeros - z`
            // 2. Number of ones in s[0...j] (`prefOnes[j]`) satisfies the dominant condition:
            //    `(currentTotalOnes - prefOnes[j]) >= z*z`
            //    which rearranges to `prefOnes[j] <= currentTotalOnes - z*z`
            
            const targetPrevZeros = currentTotalZeros - z;
            
            // `targetPrevZeros` is guaranteed to be non-negative due to loop range of `z`.
            
            const requiredPrevOnesUpperBound = currentTotalOnes - z * z;

            // Find `j`s in `zerosToOnesMap[targetPrevZeros]` that satisfy the `prefOnes` condition.
            if (zerosToOnesMap.has(targetPrevZeros)) {
                const onesList = zerosToOnesMap.get(targetPrevZeros);
                // Custom binary search to find upper_bound (equivalent to bisect_right)
                let low = 0;
                let high = onesList.length;
                let count = 0;
                while (low < high) {
                    let mid = Math.floor((low + high) / 2);
                    if (onesList[mid] <= requiredPrevOnesUpperBound) {
                        count = mid + 1;
                        low = mid + 1;
                    } else {
                        high = mid;
                    }
                }
                ans += count;
            }
        }
        
        // Add current prefix (s[0...r]) sums to the map for future iterations.
        // If the key does not exist, initialize with an empty array.
        if (!zerosToOnesMap.has(currentTotalZeros)) {
            zerosToOnesMap.set(currentTotalZeros, []);
        }
        zerosToOnesMap.get(currentTotalZeros).push(currentTotalOnes);
    }
    
    return ans;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function numberOfSubstrings(s: string): number {
    const n: number = s.length;
    let ans: number = 0;

    // K_MAX_Z is the maximum possible number of zeros in a dominant substring.
    // Derived from Z^2 + Z - N <= 0.
    const K_MAX_Z: number = Math.floor((-1 + Math.sqrt(1 + 4 * n)) / 2);
    
    // Prefix sums for zeros and ones. prefZeros[i] is count up to index i-1.
    const prefZeros: number[] = new Array(n + 1).fill(0);
    const prefOnes: number[] = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        prefZeros[i+1] = prefZeros[i] + (s[i] === '0' ? 1 : 0);
        prefOnes[i+1] = prefOnes[i] + (s[i] === '1' ? 1 : 0);
    }

    // zerosToOnesMap stores arrays of prefOnes values for specific prefZeros counts.
    // Map<number, number[]>
    const zerosToOnesMap: Map<number, number[]> = new Map();
    
    // Initialize for prefix up to index -1 (empty string or for l=0).
    // prefZeros[-1] = 0, prefOnes[-1] = 0
    zerosToOnesMap.set(0, [0]);

    for (let r = 0; r < n; r++) {
        // currentTotalZeros and currentTotalOnes are for prefix s[0...r]
        const currentTotalZeros: number = prefZeros[r+1];
        const currentTotalOnes: number = prefOnes[r+1];

        // Iterate through all possible number of zeros 'z' in substring s[l...r]
        // 'z' can range from 0 up to K_MAX_Z.
        // 'z' also cannot be more than currentTotalZeros.
        for (let z = 0; z <= Math.min(K_MAX_Z, currentTotalZeros); z++) {
            // We are looking for an index `j` (which corresponds to `l-1`) such that:
            // 1. Number of zeros in s[0...j] is `targetPrevZeros`.
            //    `targetPrevZeros = currentTotalZeros - z`
            // 2. Number of ones in s[0...j] (`prefOnes[j]`) satisfies the dominant condition:
            //    `(currentTotalOnes - prefOnes[j]) >= z*z`
            //    which rearranges to `prefOnes[j] <= currentTotalOnes - z*z`
            
            const targetPrevZeros: number = currentTotalZeros - z;
            
            // `targetPrevZeros` is guaranteed to be non-negative due to loop range of `z`.
            
            const requiredPrevOnesUpperBound: number = currentTotalOnes - z * z;

            // Find `j`s in `zerosToOnesMap[targetPrevZeros]` that satisfy the `prefOnes` condition.
            if (zerosToOnesMap.has(targetPrevZeros)) {
                const onesList: number[] = zerosToOnesMap.get(targetPrevZeros)!;
                // Custom binary search to find upper_bound (equivalent to bisect_right)
                let low: number = 0;
                let high: number = onesList.length;
                let count: number = 0;
                while (low < high) {
                    let mid: number = Math.floor((low + high) / 2);
                    if (onesList[mid] <= requiredPrevOnesUpperBound) {
                        count = mid + 1;
                        low = mid + 1;
                    } else {
                        high = mid;
                    }
                }
                ans += count;
            }
        }
        
        // Add current prefix (s[0...r]) sums to the map for future iterations.
        // If the key does not exist, initialize with an empty array.
        if (!zerosToOnesMap.has(currentTotalZeros)) {
            zerosToOnesMap.set(currentTotalZeros, []);
        }
        zerosToOnesMap.get(currentTotalZeros)!.push(currentTotalOnes);
    }
    
    return ans;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package solution

import (
	"math"
	"sort"
)

func numberOfSubstrings(s string) int64 {
    n := len(s)
    var ans int64 = 0

    // K_MAX_Z is the maximum possible number of zeros in a dominant substring.
    // Derived from Z^2 + Z - N <= 0.
    K_MAX_Z := int(math.Floor((-1 + math.Sqrt(1 + 4*float64(n))) / 2))
    
    // Prefix sums for zeros and ones. prefZeros[i] is count up to index i-1.
    prefZeros := make([]int, n + 1)
    prefOnes := make([]int, n + 1)
    for i := 0; i < n; i++ {
        prefZeros[i+1] = prefZeros[i] + (func() int { if s[i] == '0' { return 1 } else { return 0 } }()) 
        prefOnes[i+1] = prefOnes[i] + (func() int { if s[i] == '1' { return 1 } else { return 0 } }()) 
    }

    // zerosToOnesMap stores slices of prefOnes values for specific prefZeros counts.
    zerosToOnesMap := make(map[int][]int)
    
    // Initialize for prefix up to index -1 (empty string or for l=0).
    // prefZeros[-1] = 0, prefOnes[-1] = 0
    zerosToOnesMap[0] = append(zerosToOnesMap[0], 0)

    for r := 0; r < n; r++ {
        // currentTotalZeros and currentTotalOnes are for prefix s[0...r]
        currentTotalZeros := prefZeros[r+1]
        currentTotalOnes := prefOnes[r+1]

        // Iterate through all possible number of zeros 'z' in substring s[l...r]
        // 'z' can range from 0 up to K_MAX_Z.
        // 'z' also cannot be more than currentTotalZeros.
        for z := 0; z <= min(K_MAX_Z, currentTotalZeros); z++ {
            // We are looking for an index `j` (which corresponds to `l-1`) such that:
            // 1. Number of zeros in s[0...j] is `targetPrevZeros`.
            //    `targetPrevZeros = currentTotalZeros - z`
            // 2. Number of ones in s[0...j] (`prefOnes[j]`) satisfies the dominant condition:
            //    `(currentTotalOnes - prefOnes[j]) >= z*z`
            //    which rearranges to `prefOnes[j] <= currentTotalOnes - z*z`
            
            targetPrevZeros := currentTotalZeros - z;
            
            // `targetPrevZeros` is guaranteed to be non-negative due to loop range of `z`.
            
            requiredPrevOnesUpperBound := currentTotalOnes - z * z;

            // Find `j`s in `zerosToOnesMap[targetPrevZeros]` that satisfy the `prefOnes` condition.
            if onesList, ok := zerosToOnesMap[targetPrevZeros]; ok {
                // `sort.SearchInts` finds the smallest index i such that onesList[i] >= requiredPrevOnesUpperBound + 1 (effectively upper_bound).
                // All elements before this index i are <= requiredPrevOnesUpperBound.
                count := sort.SearchInts(onesList, requiredPrevOnesUpperBound + 1)
                ans += int64(count)
            }
        }
        
        // Add current prefix (s[0...r]) sums to the map for future iterations.
        // The `prefOnes` values within each slice will remain sorted because `prefOnes` is non-decreasing over 'r'.
        zerosToOnesMap[currentTotalZeros] = append(zerosToOnesMap[currentTotalZeros], currentTotalOnes)
    }
    
    return ans
}

func min(a, b int) int {
    if a < b { return a }
    return b
}
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** The time complexity is `O(N * K_MAX_Z * logN)`.
- Precomputing prefix sums takes `O(N)`.
- The outer loop iterates `r` from `0` to `N-1`, which is `N` iterations.
- The inner loop iterates `z` from `0` to `K_MAX_Z`. `K_MAX_Z` is `O(sqrt(N))` (specifically, `floor((-1 + sqrt(1+4N))/2)` for the given `N`).
- Inside the inner loop, `bisect_right` (binary search) on a list of `pref_ones` values takes `O(log P)` time, where `P` is the length of the list (at most `N`). So, `O(logN)`.
- Appending to the list is `O(1)`.
Therefore, the total time complexity is `O(N * sqrt(N) * logN)`. For `N=4*10^4`, this is approximately `4*10^4 * 200 * 15 = 1.2 * 10^8` operations, which is feasible within typical time limits.

- **Space Complexity:** The space complexity is `O(N)`.
- `pref_zeros` and `pref_ones` arrays take `O(N)` space.
- `zeros_to_ones_map` stores lists of `pref_ones` values. The keys of the map are `pref_zeros` counts, which range from `0` to `N`. However, we only care about counts up to `K_MAX_Z` (about 200) for active lookups, but the map itself might store up to `N` distinct `pref_zeros` values (e.g., for `s = '00...0'`). The total number of elements across all lists stored in the map is `N+1` (since each `(pref_zeros[j], pref_ones[j])` pair for `j=-1...N-1` is stored once). Thus, the total space is `O(N)`.
