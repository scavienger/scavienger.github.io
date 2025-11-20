---
layout: post
title: "Find X-Sum of All K-Long Subarrays I"
date: 2025-11-04 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Sliding Window", "Heap (Priority Queue)"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
---

## Problem #3318: Find X-Sum of All K-Long Subarrays I

**Difficulty:** Easy

**Topics:** Array, Hash Table, Sliding Window, Heap (Priority Queue)

## Problem Description

<p>You are given an array <code>nums</code> of <code>n</code> integers and two integers <code>k</code> and <code>x</code>.</p>

<p>The <strong>x-sum</strong> of an array is calculated by the following procedure:</p>

<ul>
	<li>Count the occurrences of all elements in the array.</li>
	<li>Keep only the occurrences of the top <code>x</code> most frequent elements. If two elements have the same number of occurrences, the element with the <strong>bigger</strong> value is considered more frequent.</li>
	<li>Calculate the sum of the resulting array.</li>
</ul>

<p><strong>Note</strong> that if an array has less than <code>x</code> distinct elements, its <strong>x-sum</strong> is the sum of the array.</p>

<p>Return an integer array <code>answer</code> of length <code>n - k + 1</code> where <code>answer[i]</code> is the <strong>x-sum</strong> of the <span data-keyword="subarray-nonempty">subarray</span> <code>nums[i..i + k - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,2,3,4,2,3], k = 6, x = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[6,10,12]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For subarray <code>[1, 1, 2, 2, 3, 4]</code>, only elements 1 and 2 will be kept in the resulting array. Hence, <code>answer[0] = 1 + 1 + 2 + 2</code>.</li>
	<li>For subarray <code>[1, 2, 2, 3, 4, 2]</code>, only elements 2 and 4 will be kept in the resulting array. Hence, <code>answer[1] = 2 + 2 + 2 + 4</code>. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.</li>
	<li>For subarray <code>[2, 2, 3, 4, 2, 3]</code>, only elements 2 and 3 are kept in the resulting array. Hence, <code>answer[2] = 2 + 2 + 2 + 3 + 3</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,8,7,8,7,5], k = 2, x = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[11,15,15,15,12]</span></p>

<p><strong>Explanation:</strong></p>

<p>Since <code>k == x</code>, <code>answer[i]</code> is equal to the sum of the subarray <code>nums[i..i + k - 1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>1 &lt;= x &lt;= k &lt;= nums.length</code></li>
</ul>


## Hints

1. Implement the x-sum function. Then, run x-sum on every subarray of `nums` of size `k`.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-20 00:21:01)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to compute the 'x-sum' for all contiguous subarrays of a given length `k`. The 'x-sum' of an array is defined by a specific procedure: first, count the occurrences of all elements. Then, identify the `x` most frequent elements. If elements have the same frequency, the one with the larger value is considered more frequent. Finally, sum up all occurrences of these top `x` elements. If the array has fewer than `x` distinct elements, the x-sum is simply the sum of all elements in the array.

The constraints on `n` (length of `nums`) are very small, `n <= 50`. This is a crucial observation. With `n` being so small, a straightforward approach of iterating through all subarrays and calculating their x-sum individually will be efficient enough.

Our strategy involves two main parts: a helper function to calculate the x-sum for a single array (subarray) and a main function to iterate through all `k`-length subarrays and apply the helper. 

**Helper Function: `calculateXSum(sub_array, x)`**
1.  **Frequency Counting**: We first need to count the occurrences of each unique element within the `sub_array`. A frequency map (hash map or a simple array if element values are small and non-negative, which they are here, `1 <= nums[i] <= 50`) is suitable for this. Iterate through `sub_array`, and for each element, increment its count in the frequency map.
2.  **Prepare for Sorting**: Collect all distinct elements and their frequencies into a list of pairs (or objects/structs). Each pair will store `(frequency, value)`.
3.  **Custom Sorting**: Sort this list of `(frequency, value)` pairs. The sorting criteria are vital: 
    *   Primary sort key: `frequency` in *descending* order (most frequent first).
    *   Secondary sort key (tie-breaker): `value` in *descending* order (larger value first, as specified by "bigger value is considered more frequent").
4.  **Select Top `x` Elements**: After sorting, take the first `min(x, number_of_distinct_elements)` pairs from the sorted list. These represent the elements whose occurrences contribute to the x-sum. The `min` operation naturally handles the edge case where the subarray has fewer than `x` distinct elements.
5.  **Calculate Sum**: Initialize `total_x_sum` to 0. For each selected `(frequency, value)` pair, add `value * frequency` to `total_x_sum`. This correctly sums up all occurrences of the top `x` most frequent (and tie-broken) elements.

**Main Function: `findXSum(nums, k, x)`**
1.  Initialize an empty list `answer` to store the results.
2.  Iterate `i` from `0` to `n - k`. This loop generates the starting index for each `k`-length subarray.
3.  For each `i`, extract the subarray `nums[i : i + k]`. 
4.  Call the `calculateXSum` helper function with this extracted subarray and `x`. 
5.  Append the returned x-sum to the `answer` list.
6.  After the loop completes, return the `answer` list.

This approach directly implements the problem description. Given `n <= 50`, the `O(N * K log K)` complexity (where `N` is `nums.length` and `K` is `k`) is perfectly acceptable, as `50 * 50 * log(50)` is a small number of operations.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
#include <vector>
#include <map>
#include <algorithm>
#include <numeric>

// Structure to hold frequency and value for sorting
struct ElementInfo {
    int freq;
    int val;

    // Custom comparison for sorting
    // Sort by frequency descending, then by value descending
    bool operator<(const ElementInfo& other) const {
        if (freq != other.freq) {
            return freq > other.freq; // Higher frequency first
        }
        return val > other.val; // Higher value first for tie-breaker
    }
};

class Solution {
public:
    // Helper function to calculate x-sum for a single array
    long long calculateXSum(const std::vector<int>& sub_array, int x) {
        std::map<int, int> freq_map; // Use std::map for clarity, could use std::vector<int> for 1-50 values
        for (int num : sub_array) {
            freq_map[num]++;
        }

        std::vector<ElementInfo> elements_info;
        for (const auto& pair : freq_map) {
            elements_info.push_back({pair.second, pair.first});
        }

        // Sort elements based on custom comparison operator
        std::sort(elements_info.begin(), elements_info.end());

        long long current_x_sum = 0;
        int count = 0;
        for (const auto& info : elements_info) {
            if (count < x) {
                current_x_sum += (long long)info.val * info.freq;
                count++;
            } else {
                break;
            }
        }
        return current_x_sum;
    }

    std::vector<long long> findXSum(std::vector<int>& nums, int k, int x) {
        int n = nums.size();
        std::vector<long long> answer;

        for (int i = 0; i <= n - k; ++i) {
            std::vector<int> sub_array;
            sub_array.reserve(k);
            for (int j = 0; j < k; ++j) {
                sub_array.push_back(nums[i + j]);
            }
            answer.push_back(calculateXSum(sub_array, x));
        }

        return answer;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class ElementInfo {
    int freq;
    int val;

    public ElementInfo(int freq, int val) {
        this.freq = freq;
        this.val = val;
    }
}

class Solution {
    // Helper function to calculate x-sum for a single array
    private long calculateXSum(List<Integer> subArray, int x) {
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : subArray) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        List<ElementInfo> elementsInfo = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            elementsInfo.add(new ElementInfo(entry.getValue(), entry.getKey()));
        }

        // Sort elements: by frequency descending, then by value descending
        Collections.sort(elementsInfo, new Comparator<ElementInfo>() {
            @Override
            public int compare(ElementInfo a, ElementInfo b) {
                if (a.freq != b.freq) {
                    return b.freq - a.freq; // Higher frequency first
                }
                return b.val - a.val; // Higher value first for tie-breaker
            }
        });

        long currentXSum = 0;
        int count = 0;
        for (ElementInfo info : elementsInfo) {
            if (count < x) {
                currentXSum += (long) info.val * info.freq;
                count++;
            } else {
                break;
            }
        }
        return currentXSum;
    }

    public List<Long> findXSum(List<Integer> nums, int k, int x) {
        int n = nums.size();
        List<Long> answer = new ArrayList<>();

        for (int i = 0; i <= n - k; ++i) {
            List<Integer> subArray = new ArrayList<>();
            for (int j = 0; j < k; ++j) {
                subArray.add(nums.get(i + j));
            }
            answer.add(calculateXSum(subArray, x));
        }

        return answer;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
from collections import Counter
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []

        def calculate_x_sum(sub_array: List[int], x_val: int) -> int:
            freq_map = Counter(sub_array)

            # Create a list of (frequency, value) tuples
            elements_info = []
            for val, freq in freq_map.items():
                elements_info.append((freq, val))

            # Sort: primary by frequency descending, secondary by value descending
            elements_info.sort(key=lambda item: (item[0], item[1]), reverse=True)

            current_x_sum = 0
            # Select top x elements and sum their total occurrences
            for i in range(min(x_val, len(elements_info))):
                freq, val = elements_info[i]
                current_x_sum += val * freq

            return current_x_sum

        for i in range(n - k + 1):
            sub_array = nums[i : i + k]
            answer.append(calculate_x_sum(sub_array, x))

        return answer
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
from collections import Counter
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []

        def calculate_x_sum(sub_array: List[int], x_val: int) -> int:
            freq_map = Counter(sub_array)

            # Create a list of (frequency, value) tuples
            elements_info = []
            for val, freq in freq_map.items():
                elements_info.append((freq, val))

            # Sort: primary by frequency descending, secondary by value descending
            # Using reverse=True means (item[0], item[1]) is sorted descendingly.
            # This works for both freq and val components correctly.
            elements_info.sort(key=lambda item: (item[0], item[1]), reverse=True)

            current_x_sum = 0
            # Select top x elements and sum their total occurrences
            for i in range(min(x_val, len(elements_info))):
                freq, val = elements_info[i]
                current_x_sum += val * freq

            return current_x_sum

        for i in range(n - k + 1):
            sub_array = nums[i : i + k]
            answer.append(calculate_x_sum(sub_array, x))

        return answer
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to hold frequency and value for sorting
typedef struct {
    int freq;
    int val;
} ElementInfo;

// Custom comparison function for qsort
// Sort by frequency descending, then by value descending
int compareElementInfo(const void* a, const void* b) {
    ElementInfo* infoA = (ElementInfo*)a;
    ElementInfo* infoB = (ElementInfo*)b;

    if (infoA->freq != infoB->freq) {
        return infoB->freq - infoA->freq; // Higher frequency first
    }
    return infoB->val - infoA->val; // Higher value first for tie-breaker
}

// Helper function to calculate x-sum for a single array
long long calculateXSum(const int* sub_array, int k_len, int x) {
    // Frequencies: nums[i] are 1 to 50, so use array of size 51 (index 0 unused)
    int freq_map[51] = {0}; 
    int distinct_elements_count = 0;
    for (int i = 0; i < k_len; ++i) {
        if (freq_map[sub_array[i]] == 0) {
            distinct_elements_count++;
        }
        freq_map[sub_array[i]]++;
    }

    ElementInfo* elements_info = (ElementInfo*)malloc(sizeof(ElementInfo) * distinct_elements_count);
    if (elements_info == NULL) {
        // Handle malloc error
        return -1; // Or throw an error, depending on error handling strategy
    }

    int current_distinct_idx = 0;
    for (int i = 1; i <= 50; ++i) { // Iterate possible values 1 to 50
        if (freq_map[i] > 0) {
            elements_info[current_distinct_idx].freq = freq_map[i];
            elements_info[current_distinct_idx].val = i;
            current_distinct_idx++;
        }
    }

    // Sort elements using qsort
    qsort(elements_info, distinct_elements_count, sizeof(ElementInfo), compareElementInfo);

    long long current_x_sum = 0;
    for (int i = 0; i < distinct_elements_count && i < x; ++i) {
        current_x_sum += (long long)elements_info[i].val * elements_info[i].freq;
    }

    free(elements_info);
    return current_x_sum;
}

/**
 * Note: The LeetCode C template might provide a different function signature.
 * This implementation assumes a structure where `findXSum` is called externally.
 * If `nums` is an int* and `returnSize` is an int*, you'd adjust.
 * For typical LeetCode C, it's `int* nums, int numsSize, int k, int x, int* returnSize`
 * and returns `long long*`.
 */
long long* findXSum(int* nums, int numsSize, int k, int x, int* returnSize) {
    int num_subarrays = numsSize - k + 1;
    long long* answer = (long long*)malloc(sizeof(long long) * num_subarrays);
    if (answer == NULL) {
        *returnSize = 0;
        return NULL;
    }

    *returnSize = num_subarrays;

    // Create a temporary array for subarrays (to pass to calculateXSum)
    int* sub_array_temp = (int*)malloc(sizeof(int) * k);
    if (sub_array_temp == NULL) {
        free(answer);
        *returnSize = 0;
        return NULL;
    }

    for (int i = 0; i <= numsSize - k; ++i) {
        for (int j = 0; j < k; ++j) {
            sub_array_temp[j] = nums[i + j];
        }
        answer[i] = calculateXSum(sub_array_temp, k, x);
    }

    free(sub_array_temp);
    return answer;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    // Structure to hold frequency and value for sorting
    private class ElementInfo {
        public int Freq { get; set; }
        public int Val { get; set; }

        public ElementInfo(int freq, int val) {
            Freq = freq;
            Val = val;
        }
    }

    // Helper function to calculate x-sum for a single array
    private long CalculateXSum(IList<int> subArray, int x) {
        Dictionary<int, int> freqMap = new Dictionary<int, int>();
        foreach (int num in subArray) {
            freqMap[num] = freqMap.GetValueOrDefault(num, 0) + 1;
        }

        List<ElementInfo> elementsInfo = new List<ElementInfo>();
        foreach (var entry in freqMap) {
            elementsInfo.Add(new ElementInfo(entry.Value, entry.Key));
        }

        // Sort elements: by frequency descending, then by value descending
        elementsInfo.Sort((a, b) => {
            if (a.Freq != b.Freq) {
                return b.Freq.CompareTo(a.Freq); // Higher frequency first
            }
            return b.Val.CompareTo(a.Val); // Higher value first for tie-breaker
        });

        long currentXSum = 0;
        int count = 0;
        foreach (ElementInfo info in elementsInfo) {
            if (count < x) {
                currentXSum += (long)info.Val * info.Freq;
                count++;
            } else {
                break;
            }
        }
        return currentXSum;
    }

    public IList<long> FindXSum(int[] nums, int k, int x) {
        int n = nums.Length;
        List<long> answer = new List<long>();

        for (int i = 0; i <= n - k; ++i) {
            List<int> subArray = new List<int>();
            for (int j = 0; j < k; ++j) {
                subArray.Add(nums[i + j]);
            }
            answer.Add(CalculateXSum(subArray, x));
        }

        return answer;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findXSum = function(nums, k, x) {
    const n = nums.length;
    const answer = [];

    // Helper function to calculate x-sum for a single array
    const calculateXSum = (subArray, xVal) => {
        const freqMap = new Map();
        for (const num of subArray) {
            freqMap.set(num, (freqMap.get(num) || 0) + 1);
        }

        // Create a list of {freq, val} objects
        const elementsInfo = [];
        for (const [val, freq] of freqMap.entries()) {
            elementsInfo.push({ freq, val });
        }

        // Sort elements: by frequency descending, then by value descending
        elementsInfo.sort((a, b) => {
            if (a.freq !== b.freq) {
                return b.freq - a.freq; // Higher frequency first
            }
            return b.val - a.val; // Higher value first for tie-breaker
        });

        let currentXSum = 0;
        // Select top x elements and sum their total occurrences
        for (let i = 0; i < Math.min(xVal, elementsInfo.length); ++i) {
            const { freq, val } = elementsInfo[i];
            currentXSum += val * freq;
        }
        return currentXSum;
    };

    for (let i = 0; i <= n - k; ++i) {
        const subArray = nums.slice(i, i + k);
        answer.push(calculateXSum(subArray, x));
    }

    return answer;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
interface ElementInfo {
    freq: number;
    val: number;
}

function findXSum(nums: number[], k: number, x: number): number[] {
    const n = nums.length;
    const answer: number[] = [];

    // Helper function to calculate x-sum for a single array
    const calculateXSum = (subArray: number[], xVal: number): number => {
        const freqMap = new Map<number, number>();
        for (const num of subArray) {
            freqMap.set(num, (freqMap.get(num) || 0) + 1);
        }

        // Create a list of {freq, val} objects
        const elementsInfo: ElementInfo[] = [];
        for (const [val, freq] of freqMap.entries()) {
            elementsInfo.push({ freq, val });
        }

        // Sort elements: by frequency descending, then by value descending
        elementsInfo.sort((a, b) => {
            if (a.freq !== b.freq) {
                return b.freq - a.freq; // Higher frequency first
            }
            return b.val - a.val; // Higher value first for tie-breaker
        });

        let currentXSum = 0;
        // Select top x elements and sum their total occurrences
        for (let i = 0; i < Math.min(xVal, elementsInfo.length); ++i) {
            const { freq, val } = elementsInfo[i];
            currentXSum += val * freq;
        }
        return currentXSum;
    };

    for (let i = 0; i <= n - k; ++i) {
        const subArray = nums.slice(i, i + k);
        answer.push(calculateXSum(subArray, x));
    }

    return answer;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
<?php

class Solution {

    /**
     * @param int[] $subArray
     * @param int $x
     * @return int
     */
    private function calculateXSum(array $subArray, int $x): int {
        $freqMap = [];
        foreach ($subArray as $num) {
            $freqMap[$num] = ($freqMap[$num] ?? 0) + 1;
        }

        $elementsInfo = [];
        foreach ($freqMap as $val => $freq) {
            $elementsInfo[] = ['freq' => $freq, 'val' => $val];
        }

        // Sort elements: by frequency descending, then by value descending
        usort($elementsInfo, function($a, $b) {
            if ($a['freq'] !== $b['freq']) {
                return $b['freq'] <=> $a['freq']; // Higher frequency first
            }
            return $b['val'] <=> $a['val']; // Higher value first for tie-breaker
        });

        $currentXSum = 0;
        // Select top x elements and sum their total occurrences
        for ($i = 0; $i < min($x, count($elementsInfo)); ++$i) {
            $currentXSum += $elementsInfo[$i]['val'] * $elementsInfo[$i]['freq'];
        }
        return $currentXSum;
    }

    /**
     * @param int[] $nums
     * @param int $k
     * @param int $x
     * @return int[]
     */
    function findXSum(array $nums, int $k, int $x): array {
        $n = count($nums);
        $answer = [];

        for ($i = 0; $i <= $n - $k; ++$i) {
            $subArray = array_slice($nums, $i, $k);
            $answer[] = $this->calculateXSum($subArray, $x);
        }

        return $answer;
    }
}

?>
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
import Foundation

struct ElementInfo {
    let freq: Int
    let val: Int
}

class Solution {
    // Helper function to calculate x-sum for a single array
    private func calculateXSum(_ subArray: [Int], _ x: Int) -> Int {
        var freqMap: [Int: Int] = [:]
        for num in subArray {
            freqMap[num, default: 0] += 1
        }

        var elementsInfo: [ElementInfo] = []
        for (val, freq) in freqMap {
            elementsInfo.append(ElementInfo(freq: freq, val: val))
        }

        // Sort elements: by frequency descending, then by value descending
        elementsInfo.sort { a, b in
            if a.freq != b.freq {
                return a.freq > b.freq // Higher frequency first
            }
            return a.val > b.val // Higher value first for tie-breaker
        }

        var currentXSum: Int = 0
        // Select top x elements and sum their total occurrences
        for i in 0..<min(x, elementsInfo.count) {
            let info = elementsInfo[i]
            currentXSum += info.val * info.freq
        }
        return currentXSum
    }

    func findXSum(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        let n = nums.count
        var answer: [Int] = []

        for i in 0...(n - k) {
            let subArray = Array(nums[i..<(i + k)])
            answer.append(calculateXSum(subArray, x))
        }

        return answer
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
import java.util.Collections

data class ElementInfo(val freq: Int, val val_prop: Int) // Renamed 'val' to 'val_prop' due to keyword conflict

class Solution {
    // Helper function to calculate x-sum for a single array
    private fun calculateXSum(subArray: List<Int>, x: Int): Long {
        val freqMap = mutableMapOf<Int, Int>()
        for (num in subArray) {
            freqMap[num] = freqMap.getOrDefault(num, 0) + 1
        }

        val elementsInfo = mutableListOf<ElementInfo>()
        for ((value, frequency) in freqMap) {
            elementsInfo.add(ElementInfo(frequency, value))
        }

        // Sort elements: by frequency descending, then by value descending
        elementsInfo.sortWith(Comparator {
            a, b ->
            if (a.freq != b.freq) {
                b.freq.compareTo(a.freq) // Higher frequency first
            } else {
                b.val_prop.compareTo(a.val_prop) // Higher value first for tie-breaker
            }
        })

        var currentXSum: Long = 0
        // Select top x elements and sum their total occurrences
        for (i in 0 until minOf(x, elementsInfo.size)) {
            val info = elementsInfo[i]
            currentXSum += info.val_prop.toLong() * info.freq
        }
        return currentXSum
    }

    fun findXSum(nums: IntArray, k: Int, x: Int): List<Long> {
        val n = nums.size
        val answer = mutableListOf<Long>()

        for (i in 0..(n - k)) {
            val subArray = nums.slice(i until i + k)
            answer.add(calculateXSum(subArray, x))
        }

        return answer
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
import 'dart:collection';
import 'dart:math';

class ElementInfo {
  int freq;
  int val;

  ElementInfo(this.freq, this.val);
}

class Solution {
  // Helper function to calculate x-sum for a single array
  int _calculateXSum(List<int> subArray, int x) {
    final freqMap = HashMap<int, int>();
    for (final num in subArray) {
      freqMap[num] = (freqMap[num] ?? 0) + 1;
    }

    final elementsInfo = <ElementInfo>[];
    freqMap.forEach((val, freq) {
      elementsInfo.add(ElementInfo(freq, val));
    });

    // Sort elements: by frequency descending, then by value descending
    elementsInfo.sort((a, b) {
      if (a.freq != b.freq) {
        return b.freq.compareTo(a.freq); // Higher frequency first
      }
      return b.val.compareTo(a.val); // Higher value first for tie-breaker
    });

    int currentXSum = 0;
    // Select top x elements and sum their total occurrences
    for (int i = 0; i < min(x, elementsInfo.length); ++i) {
      final info = elementsInfo[i];
      currentXSum += info.val * info.freq;
    }
    return currentXSum;
  }

  List<int> findXSum(List<int> nums, int k, int x) {
    final n = nums.length;
    final answer = <int>[];

    for (int i = 0; i <= n - k; ++i) {
      final subArray = nums.sublist(i, i + k);
      answer.add(_calculateXSum(subArray, x));
    }

    return answer;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

import (
	"sort"
)

type ElementInfo struct {
	freq int
	val  int
}

func calculateXSum(subArray []int, x int) int {
	freqMap := make(map[int]int)
	for _, num := range subArray {
		freqMap[num]++
	}

	elementsInfo := make([]ElementInfo, 0, len(freqMap))
	for val, freq := range freqMap {
		elementsInfo = append(elementsInfo, ElementInfo{freq: freq, val: val})
	}

	// Sort elements: by frequency descending, then by value descending
	sort.Slice(elementsInfo, func(i, j int) bool {
		if elementsInfo[i].freq != elementsInfo[j].freq {
			return elementsInfo[i].freq > elementsInfo[j].freq // Higher frequency first
		}
		return elementsInfo[i].val > elementsInfo[j].val // Higher value first for tie-breaker
	})

	currentXSum := 0
	for i := 0; i < len(elementsInfo) && i < x; i++ {
		info := elementsInfo[i]
		currentXSum += info.val * info.freq
	}
	return currentXSum
}

func findXSum(nums []int, k int, x int) []int {
	n := len(nums)
	answer := make([]int, 0, n-k+1)

	for i := 0; i <= n-k; i++ {
		subArray := nums[i : i+k]
		answer = append(answer, calculateXSum(subArray, x))
	}

	return answer
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def find_x_sum(nums, k, x)
    n = nums.length
    answer = []

    # Helper function to calculate x-sum for a single array
    calculate_x_sum = lambda do |sub_array, x_val|
        freq_map = sub_array.tally # `tally` method is available in Ruby 2.7+

        elements_info = []
        freq_map.each do |val, freq|
            elements_info << { freq: freq, val: val }
        end

        # Sort elements: by frequency descending, then by value descending
        elements_info.sort! do |a, b|
            if a[:freq] != b[:freq]
                b[:freq] <=> a[:freq] # Higher frequency first
            else
                b[:val] <=> a[:val] # Higher value first for tie-breaker
            end
        end

        current_x_sum = 0
        # Select top x elements and sum their total occurrences
        (0...([x_val, elements_info.length].min)).each do |i|
            info = elements_info[i]
            current_x_sum += info[:val] * info[:freq]
        end
        current_x_sum
    end

    (0..(n - k)).each do |i|
        sub_array = nums[i, k]
        answer << calculate_x_sum.call(sub_array, x)
    end

    answer
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
import scala.collection.mutable
import scala.math.min

class Solution {

    case class ElementInfo(freq: Int, value: Int)

    // Helper function to calculate x-sum for a single array
    private def calculateXSum(subArray: Array[Int], x: Int): Long = {
        val freqMap = mutable.Map[Int, Int]()
        for (num <- subArray) {
            freqMap(num) = freqMap.getOrElse(num, 0) + 1
        }

        var elementsInfo = freqMap.map { case (value, freq) => ElementInfo(freq, value) }.toList

        // Sort elements: by frequency descending, then by value descending
        elementsInfo = elementsInfo.sortWith {
            (a, b) => 
                if (a.freq != b.freq) {
                    a.freq > b.freq // Higher frequency first
                } else {
                    a.value > b.value // Higher value first for tie-breaker
                }
        }

        var currentXSum: Long = 0
        // Select top x elements and sum their total occurrences
        for (i <- 0 until min(x, elementsInfo.length)) {
            val info = elementsInfo(i)
            currentXSum += info.value.toLong * info.freq
        }
        currentXSum
    }

    def findXSum(nums: Array[Int], k: Int, x: Int): Array[Long] = {
        val n = nums.length
        val answer = new Array[Long](n - k + 1)

        for (i <- 0 to (n - k)) {
            val subArray = nums.slice(i, i + k)
            answer(i) = calculateXSum(subArray, x)
        }

        answer
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
use std::collections::HashMap;

#[derive(Debug, PartialEq, Eq, PartialOrd, Ord)]
struct ElementInfo {
    // Note: Rust's default derived Ord sorts fields in declaration order.
    // To achieve (freq desc, val desc), we need to reverse the values if we use default Ord,
    // or provide a custom comparison logic.
    // A more idiomatic way for desc-desc sort with tuples is (Reverse(freq), Reverse(val)).
    // For struct, custom implementation of PartialOrd/Ord is clearest.
    freq: i32,
    val: i32,
}

impl ElementInfo {
    fn new(freq: i32, val: i32) -> Self {
        ElementInfo { freq, val }
    }
}

// Custom comparison for sorting (freq desc, val desc)
impl PartialOrd for ElementInfo {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for ElementInfo {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        // Compare frequencies descending
        let freq_cmp = other.freq.cmp(&self.freq);
        if freq_cmp != std::cmp::Ordering::Equal {
            return freq_cmp;
        }
        // If frequencies are equal, compare values descending
        other.val.cmp(&self.val)
    }
}

impl Solution {
    // Helper function to calculate x-sum for a single array
    fn calculate_x_sum(sub_array: &[i32], x: i32) -> i32 {
        let mut freq_map: HashMap<i32, i32> = HashMap::new();
        for &num in sub_array {
            *freq_map.entry(num).or_insert(0) += 1;
        }

        let mut elements_info: Vec<ElementInfo> = Vec::new();
        for (val, freq) in freq_map {
            elements_info.push(ElementInfo::new(freq, val));
        }

        // Sort elements using the custom Ord implementation
        elements_info.sort();

        let mut current_x_sum: i32 = 0;
        // Select top x elements and sum their total occurrences
        for i in 0..std::cmp::min(x as usize, elements_info.len()) {
            let info = &elements_info[i];
            current_x_sum += info.val * info.freq;
        }
        current_x_sum
    }

    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let n = nums.len() as i32;
        let mut answer: Vec<i32> = Vec::new();

        for i in 0..=(n - k) as usize {
            let sub_array = &nums[i..(i + k as usize)];
            answer.push(Self::calculate_x_sum(sub_array, x));
        }

        answer
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

(define-struct element-info (freq val) #:transparent)

;; Helper function to calculate x-sum for a single array
(define (calculate-x-sum sub-array x-val)
  (define freq-map (make-hash))
  (for-each (lambda (num)
              (hash-update! freq-map num (lambda (current-freq) (+ current-freq 1)) 0))
            sub-array)

  (define elements-info
    (for/list ([(val freq) (in-hash freq-map)])
      (make-element-info freq val)))

  ;; Sort elements: by frequency descending, then by value descending
  (define sorted-elements-info
    (sort elements-info
          (lambda (a b)
            (cond
              [(not (= (element-info-freq a) (element-info-freq b)))
               (> (element-info-freq a) (element-info-freq b))]
              [else
               (> (element-info-val a) (element-info-val b))]))))

  (define current-x-sum 0)
  ;; Select top x elements and sum their total occurrences
  (for ([i (in-range (min x-val (length sorted-elements-info)))])
    (define info (list-ref sorted-elements-info i))
    (set! current-x-sum (+ current-x-sum (* (element-info-val info) (element-info-freq info)))))

  current-x-sum)

;; Main function to find X-Sum of All K-Long Subarrays
(define (find-x-sum nums k x)
  (define n (length nums))
  (define answer '())

  (for ([i (in-range 0 (- n k -1))])
    (define sub-array (take (drop nums i) k))
    (set! answer (append answer (list (calculate-x-sum sub-array x)))))

  answer)

;; For LeetCode compatibility, typically wrap in a module or class structure as required
;; Example usage (if not in a LeetCode runner):
;; (module solution racket
;;   (provide find-x-sum)
;;
;;   (define-struct element-info (freq val) #:transparent)
;;
;;   (define (calculate-x-sum sub-array x-val)
;;     ;; ... (same as above)
;;   )
;;
;;   (define (find-x-sum nums k x)
;;     ;; ... (same as above)
;;   )
;; )
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([findXSum/3]).

%% Helper function to calculate x-sum for a single array
-spec calculate_x_sum(list(), integer()) -> integer().
calculate_x_sum(SubArray, X) ->
    FreqMap = lists:foldl(fun(Num, Acc) ->
                              maps:update_with(Num, fun(Count) -> Count + 1 end, 1, Acc)
                          end, #{}, SubArray),

    ElementsInfo = lists:map(fun({Val, Freq}) ->
                                 #{freq => Freq, val => Val}
                             end, maps:to_list(FreqMap)),

    %% Sort elements: by frequency descending, then by value descending
    SortedElementsInfo = lists:sort(fun(A, B) ->
                                        FreqA = maps:get(freq, A),
                                        FreqB = maps:get(freq, B),
                                        ValA = maps:get(val, A),
                                        ValB = maps:get(val, B),
                                        if FreqA =/= FreqB ->
                                               FreqA > FreqB; %% Higher frequency first
                                           true ->
                                               ValA > ValB %% Higher value first for tie-breaker
                                        end
                                    end, ElementsInfo),

    %% Select top X elements and sum their total occurrences
    TopXElements = lists:sublist(SortedElementsInfo, min(X, length(SortedElementsInfo))),
    lists:foldl(fun(Info, Acc) ->
                    Acc + (maps:get(val, Info) * maps:get(freq, Info))
                end, 0, TopXElements).


%% Main function to find X-Sum of All K-Long Subarrays
-spec findXSum(list(), integer(), integer()) -> list().
findXSum(Nums, K, X) ->
    N = length(Nums),
    lists:foldl(fun(I, Acc) ->
                    SubArray = lists:sublist(Nums, I + 1, K),
                    [calculate_x_sum(SubArray, X) | Acc]
                end, [], lists:seq(0, N - K)).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec find_x_sum(nums :: [integer], k :: integer, x :: integer) :: [integer]
  def find_x_sum(nums, k, x) do
    n = length(nums)
    Enum.map(0..(n - k), fn i ->
      sub_array = Enum.slice(nums, i, k)
      calculate_x_sum(sub_array, x)
    end)
  end

  defp calculate_x_sum(sub_array, x) do
    # 1. Frequency Counting
    freq_map = Enum.reduce(sub_array, %{}, fn num, acc ->
      Map.update(acc, num, 1, &(&1 + 1))
    end)

    # 2. Prepare for Sorting
    elements_info = Enum.map(freq_map, fn {val, freq} ->
      %{freq: freq, val: val}
    end)

    # 3. Custom Sorting: by frequency descending, then by value descending
    sorted_elements_info = Enum.sort(elements_info, fn a, b ->
      if a.freq != b.freq do
        a.freq > b.freq # Higher frequency first
      else
        a.val > b.val # Higher value first for tie-breaker
      end
    end)

    # 4. Select Top X Elements & 5. Calculate Sum
    Enum.reduce(0..min(x - 1, length(sorted_elements_info) - 1), 0, fn i, acc ->
      info = Enum.at(sorted_elements_info, i)
      acc + info.val * info.freq
    end)
  end

  defp min(a, b) do
    if a < b, do: a, else: b
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** Let `N` be `nums.length` and `K` be `k`.

The main loop iterates `N - K + 1` times to consider all possible subarrays of length `K`. In the worst case, `K=1`, so it iterates `N` times. In the worst case, `K=N`, so it iterates `1` time.

Inside the loop, for each subarray of length `K`:
1.  **Extracting subarray**: This takes `O(K)` time.
2.  **Frequency Counting**: Iterating through the `K` elements of the subarray and updating a frequency map takes `O(K)` time. If using an array for frequencies (since `nums[i]` is small, up to 50), it's `O(K)` operations to populate and `O(max_val)` to initialize, where `max_val` is 50. This is effectively `O(K)`.
3.  **Collecting pairs**: Creating a list of `(frequency, value)` pairs from the frequency map takes `O(D)` time, where `D` is the number of distinct elements in the subarray. `D <= K`.
4.  **Sorting pairs**: Sorting `D` pairs takes `O(D log D)` time. Since `D <= K`, this is at most `O(K log K)` time.
5.  **Selecting and Summing**: Iterating through the top `x` sorted pairs takes `O(x)` time. Since `x <= K`, this is `O(K)` time.

Thus, calculating the x-sum for one subarray takes `O(K log K)` time.

Multiplying by the number of subarrays, the total time complexity is `(N - K + 1) * O(K log K)`. Since `K <= N`, in the worst case where `K` is comparable to `N` (e.g., `K=N/2`), this becomes `O(N * N log N)`. Given `N <= 50`, `50 * 50 * log(50)` is roughly `2500 * 6 = 15000` operations, which is very fast and well within typical time limits.

- **Space Complexity:** Let `N` be `nums.length` and `K` be `k`.

**Space for `calculateXSum` function:**
1.  **Frequency map**: This stores counts for distinct elements. In the worst case, all `K` elements in the subarray are distinct, requiring `O(K)` space. However, since `nums[i]` values are constrained to `1 <= nums[i] <= 50`, we can use an array of fixed size 51 (for indices 0-50) for frequencies, making this `O(max_val_of_nums)` or `O(1)` effectively (constant space relative to `K`).
2.  **List of `(frequency, value)` pairs**: This list will hold up to `D` pairs, where `D` is the number of distinct elements. So, it requires `O(D)` space, which is at most `O(K)` space.

**Space for `findXSum` function:**
1.  **Result array**: The `answer` array stores `N - K + 1` integers. In the worst case (`K=1`), this is `N` integers, so `O(N)` space.

Combining these, the total space complexity is `O(N + K + max_val_of_nums)`. Since `K <= N` and `max_val_of_nums` is a constant (50), the dominant factor is `N`. Therefore, the overall space complexity is `O(N)`. Given `N <= 50`, this is very small, effectively `O(1)` space usage for practical purposes.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-20 00:21:13)</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires us to find the x-sum of all k-long subarrays in a given array of integers. The x-sum is calculated by counting the occurrences of all elements in the subarray, keeping only the occurrences of the top x most frequent elements, and then calculating the sum of the resulting array.

To solve this problem, we can use a sliding window approach to generate all k-long subarrays. For each subarray, we can use a hash map to count the occurrences of each element. Then, we can use a priority queue to keep track of the top x most frequent elements. Finally, we can calculate the sum of the resulting array by iterating over the elements in the priority queue.

The time complexity of this approach is O(n * k * log(x)), where n is the length of the input array, k is the length of the subarray, and x is the number of most frequent elements to keep. This is because we need to iterate over each element in the subarray to count its occurrences, and then we need to iterate over the priority queue to calculate the sum of the resulting array.

The space complexity of this approach is O(k), where k is the length of the subarray. This is because we need to store the occurrences of each element in the subarray in a hash map, and then we need to store the top x most frequent elements in a priority queue.

Here is a step-by-step breakdown of the approach:

1. Initialize an empty list to store the x-sum of each subarray.
2. Iterate over the input array using a sliding window of size k.
3. For each subarray, count the occurrences of each element using a hash map.
4. Use a priority queue to keep track of the top x most frequent elements.
5. Calculate the sum of the resulting array by iterating over the elements in the priority queue.
6. Append the x-sum of the current subarray to the result list.
7. Return the result list.

Examples and edge cases can be used to test the correctness of the approach. For example, we can test the approach with an input array of [1, 1, 2, 2, 3, 4, 2, 3] and k = 6, x = 2. The expected output should be [6, 10, 12].

In terms of algorithm logic, the approach can be described as follows:

- Initialize an empty list to store the x-sum of each subarray.
- Iterate over the input array using a sliding window of size k.
- For each subarray, count the occurrences of each element using a hash map.
- Use a priority queue to keep track of the top x most frequent elements.
- Calculate the sum of the resulting array by iterating over the elements in the priority queue.
- Append the x-sum of the current subarray to the result list.
- Return the result list.

The approach can be implemented in various programming languages, including C++, Java, Python, and JavaScript.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        vector<int> result;
        for (int i = 0; i <= nums.size() - k; i++) {
            unordered_map<int, int> count;
            for (int j = i; j < i + k; j++) {
                count[nums[j]]++;
            }
            priority_queue<pair<int, int>> pq;
            for (auto& it : count) {
                pq.push({it.second, it.first});
            }
            int sum = 0;
            for (int j = 0; j < x; j++) {
                if (pq.empty()) break;
                sum += pq.top().second * pq.top().first;
                pq.pop();
            }
            result.push_back(sum);
        }
        return result;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
import java.util.*;

public class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int[] result = new int[nums.length - k + 1];
        for (int i = 0; i <= nums.length - k; i++) {
            Map<Integer, Integer> count = new HashMap<>();
            for (int j = i; j < i + k; j++) {
                count.put(nums[j], count.getOrDefault(nums[j], 0) + 1);
            }
            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] == b[0] ? b[1] - a[1] : b[0] - a[0]);
            for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
                pq.offer(new int[] {entry.getValue(), entry.getKey()});
            }
            int sum = 0;
            for (int j = 0; j < x; j++) {
                if (pq.isEmpty()) break;
                sum += pq.poll()[0] * pq.poll()[1];
            }
            result[i] = sum;
        }
        return result;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
from collections import Counter
import heapq

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        result = []
        for i in range(len(nums) - k + 1):
            count = Counter(nums[i:i+k])
            pq = [(-freq, num) for num, freq in count.items()]
            heapq.heapify(pq)
            sum = 0
            for _ in range(x):
                if not pq: break
                freq, num = heapq.heappop(pq)
                sum += -freq * num
            result.append(sum)
        return result
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
from collections import Counter
import heapq

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        result = []
        for i in range(len(nums) - k + 1):
            count = Counter(nums[i:i+k])
            pq = [(-freq, num) for num, freq in count.items()]
            heapq.heapify(pq)
            sum = 0
            for _ in range(x):
                if not pq: break
                freq, num = heapq.heappop(pq)
                sum += -freq * num
            result.append(sum)
        return result
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int num;
    int freq;
} Pair;

int compare(const void *a, const void *b) {
    Pair *pa = (Pair *)a;
    Pair *pb = (Pair *)b;
    if (pa->freq == pb->freq) {
        return pb->num - pa->num;
    } else {
        return pb->freq - pa->freq;
    }
}

int* findXSum(int* nums, int numsSize, int k, int x, int* returnSize) {
    int* result = (int*)malloc((numsSize - k + 1) * sizeof(int));
    *returnSize = numsSize - k + 1;
    for (int i = 0; i <= numsSize - k; i++) {
        int* count = (int*)calloc(51, sizeof(int));
        for (int j = i; j < i + k; j++) {
            count[nums[j]]++;
        }
        Pair* pairs = (Pair*)malloc(51 * sizeof(Pair));
        int pairSize = 0;
        for (int j = 1; j <= 50; j++) {
            if (count[j] > 0) {
                pairs[pairSize].num = j;
                pairs[pairSize].freq = count[j];
                pairSize++;
            }
        }
        qsort(pairs, pairSize, sizeof(Pair), compare);
        int sum = 0;
        for (int j = 0; j < x && j < pairSize; j++) {
            sum += pairs[j].num * pairs[j].freq;
        }
        result[i] = sum;
        free(pairs);
        free(count);
    }
    return result;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] FindXSum(int[] nums, int k, int x) {
        int[] result = new int[nums.Length - k + 1];
        for (int i = 0; i <= nums.Length - k; i++) {
            Dictionary<int, int> count = new Dictionary<int, int>();
            for (int j = i; j < i + k; j++) {
                if (count.ContainsKey(nums[j])) {
                    count[nums[j]]++;
                } else {
                    count[nums[j]] = 1;
                }
            }
            var pq = new SortedSet<(int freq, int num)>();
            foreach (var pair in count) {
                pq.Add((-pair.Value, pair.Key));
            }
            int sum = 0;
            for (int j = 0; j < x; j++) {
                if (pq.Count == 0) break;
                var pair = pq.Min;
                pq.Remove(pair);
                sum += -pair.freq * pair.num;
            }
            result[i] = sum;
        }
        return result;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
function findXSum(nums, k, x) {
    let result = [];
    for (let i = 0; i <= nums.length - k; i++) {
        let count = {};
        for (let j = i; j < i + k; j++) {
            if (count[nums[j]]) {
                count[nums[j]]++;
            } else {
                count[nums[j]] = 1;
            }
        }
        let pq = [];
        for (let num in count) {
            pq.push([-count[num], parseInt(num)]);
        }
        pq.sort((a, b) => a[0] - b[0]);
        let sum = 0;
        for (let j = 0; j < x; j++) {
            if (pq.length == 0) break;
            let pair = pq.shift();
            sum += -pair[0] * pair[1];
        }
        result.push(sum);
    }
    return result;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function findXSum(nums: number[], k: number, x: number): number[] {
    let result: number[] = [];
    for (let i = 0; i <= nums.length - k; i++) {
        let count: { [key: number]: number } = {};
        for (let j = i; j < i + k; j++) {
            if (count[nums[j]]) {
                count[nums[j]]++;
            } else {
                count[nums[j]] = 1;
            }
        }
        let pq: [number, number][] = [];
        for (let num in count) {
            pq.push([-count[num], parseInt(num)]);
        }
        pq.sort((a, b) => a[0] - b[0]);
        let sum = 0;
        for (let j = 0; j < x; j++) {
            if (pq.length == 0) break;
            let pair = pq.shift();
            sum += -pair[0] * pair[1];
        }
        result.push(sum);
    }
    return result;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
function findXSum($nums, $k, $x) {
    $result = [];
    for ($i = 0; $i <= count($nums) - $k; $i++) {
        $count = [];
        for ($j = $i; $j < $i + $k; $j++) {
            if (isset($count[$nums[$j]])) {
                $count[$nums[$j]]++;
            } else {
                $count[$nums[$j]] = 1;
            }
        }
        $pq = [];
        foreach ($count as $num => $freq) {
            $pq[] = [-$freq, $num];
        }
        usort($pq, function($a, $b) {
            return $a[0] - $b[0];
        });
        $sum = 0;
        for ($j = 0; $j < $x; $j++) {
            if (empty($pq)) break;
            $pair = array_shift($pq);
            $sum += -$pair[0] * $pair[1];
        }
        $result[] = $sum;
    }
    return $result;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
import Foundation

class Solution {
    func findXSum(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        var result: [Int] = []
        for i in 0...nums.count - k {
            var count: [Int: Int] = [:]
            for j in i..<i + k {
                if count[nums[j]] != nil {
                    count[nums[j]]! += 1
                } else {
                    count[nums[j]] = 1
                }
            }
            var pq: [(Int, Int)] = []
            for (num, freq) in count {
                pq.append((-freq, num))
            }
            pq.sort { $0.0 < $1.0 }
            var sum = 0
            for j in 0..<x {
                if pq.isEmpty { break }
                let pair = pq.removeFirst()
                sum += -pair.0 * pair.1
            }
            result.append(sum)
        }
        return result
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
import java.util.*

class Solution {
    fun findXSum(nums: IntArray, k: Int, x: Int): IntArray {
        val result = IntArray(nums.size - k + 1)
        for (i in 0 until nums.size - k + 1) {
            val count = HashMap<Int, Int>()
            for (j in i until i + k) {
                count[nums[j]] = (count[nums[j]] ?: 0) + 1
            }
            val pq = PriorityQueue<Pair<Int, Int>> { a, b ->
                if (a.first == b.first) b.second - a.second else b.first - a.first
            }
            for ((num, freq) in count) {
                pq.add(Pair(freq, num))
            }
            var sum = 0
            for (j in 0 until x) {
                if (pq.isEmpty()) break
                val pair = pq.poll()
                sum += pair.first * pair.second
            }
            result[i] = sum
        }
        return result
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
import 'dart:collection';

class Solution {
    List<int> findXSum(List<int> nums, int k, int x) {
        List<int> result = [];
        for (int i = 0; i <= nums.length - k; i++) {
            Map<int, int> count = {};
            for (int j = i; j < i + k; j++) {
                if (count.containsKey(nums[j])) {
                    count[nums[j]]++;
                } else {
                    count[nums[j]] = 1;
                }
            }
            List<List<int>> pq = [];
            for (int num in count.keys) {
                pq.add([-count[num]!, num]);
            }
            pq.sort((a, b) => a[0].compareTo(b[0]));
            int sum = 0;
            for (int j = 0; j < x; j++) {
                if (pq.isEmpty) break;
                List<int> pair = pq.removeAt(0);
                sum += -pair[0] * pair[1];
            }
            result.add(sum);
        }
        return result;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

import (
    "fmt"
    "sort"
)

type Pair struct {
    freq int
    num  int
}

func findXSum(nums []int, k int, x int) []int {
    result := make([]int, len(nums)-k+1)
    for i := 0; i <= len(nums)-k; i++ {
        count := make(map[int]int)
        for j := i; j < i+k; j++ {
            count[nums[j]]++
        }
        pq := make([]Pair, 0)
        for num, freq := range count {
            pq = append(pq, Pair{freq, num})
        }
        sort.Slice(pq, func(i, j int) bool {
            if pq[i].freq == pq[j].freq {
                return pq[i].num > pq[j].num
            }
            return pq[i].freq > pq[j].freq
        })
        sum := 0
        for j := 0; j < x; j++ {
            if len(pq) == 0 {
                break
            }
            pair := pq[0]
            pq = pq[1:]
            sum += pair.freq * pair.num
        }
        result[i] = sum
    }
    return result
}

func main() {
    nums := []int{1, 1, 2, 2, 3, 4, 2, 3}
    k := 6
    x := 2
    result := findXSum(nums, k, x)
    fmt.Println(result)
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
def find_x_sum(nums, k, x)
    result = []
    (0...nums.size - k + 1).each do |i|
        count = Hash.new(0)
        (i...i + k).each do |j|
            count[nums[j]] += 1
        end
        pq = []
        count.each do |num, freq|
            pq << [-freq, num]
        end
        pq.sort!
        sum = 0
        x.times do
            break if pq.empty?
            pair = pq.shift
            sum += -pair[0] * pair[1]
        end
        result << sum
    end
    result
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
    def findXSum(nums: Array[Int], k: Int, x: Int): Array[Int] = {
        val result = new Array[Int](nums.length - k + 1)
        for (i <- 0 until nums.length - k + 1) {
            val count = scala.collection.mutable.Map[Int, Int]()
            for (j <- i until i + k) {
                count(nums(j)) = count.getOrElse(nums(j), 0) + 1
            }
            val pq = scala.collection.mutable.PriorityQueue[(Int, Int)]()
            for ((num, freq) <- count) {
                pq += ((-freq, num))
            }
            var sum = 0
            for (j <- 0 until x) {
                if (pq.isEmpty) {
                    break
                }
                val pair = pq.dequeue()
                sum += -pair._1 * pair._2
            }
            result(i) = sum
        }
        result
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();
        for i in 0..(nums.len() as i32 - k + 1) {
            let mut count: HashMap<i32, i32> = HashMap::new();
            for j in i..(i + k) {
                *count.entry(nums[j as usize]).or_insert(0) += 1;
            }
            let mut pq: Vec<(i32, i32)> = Vec::new();
            for (num, freq) in &count {
                pq.push((-freq, *num));
            }
            pq.sort();
            let mut sum = 0;
            for j in 0..x {
                if pq.is_empty() {
                    break;
                }
                let pair = pq.remove(0);
                sum += -pair.0 * pair.1;
            }
            result.push(sum);
        }
        result
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

(define (find-x-sum nums k x)
  (let loop ((i 0) (result '()))
    (if (> i (- (length nums) k))
        (reverse result)
        (let* ((count (make-hash))
               (sum 0))
          (for ((j (range i (+ i k))))
            (hash-update! count (list-ref nums j) add1 0))
          (let ((pq (sort (hash-map count (λ (k v) (list (- v) k))) <)))
            (for ((j (range x)))
              (if (null? pq)
                  (set! sum sum)
                  (let ((pair (car pq)))
                    (set! pq (cdr pq))
                    (set! sum (+ sum (* (cadr pair) (- (car pair))))))))
          (loop (+ i 1) (cons sum result))))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).

-export([find_x_sum/3]).

find_x_sum(Nums, K, X) ->
    Result = lists:map(fun(I) -> x_sum(Nums, I, K, X) end, lists:seq(0, length(Nums) - K)),
    Result.

x_sum(Nums, I, K, X) ->
    Subarray = lists:sublist(Nums, I + 1, K),
    Count = count(Subarray, #{}),
    PQ = pq(Count, []),
    Sum = sum(PQ, X, 0),
    Sum.

count([], Count) -> Count;
count([H|T], Count) ->
    case maps:find(H, Count) of
        {ok, Val} -> count(T, maps:put(H, Val + 1, Count));
        error -> count(T, maps:put(H, 1, Count))
    end.

pq([], PQ) -> PQ;
pq([{Num, Freq}|T], PQ) ->
    pq(T, [{-Freq, Num}|PQ]).

sum([], _, Sum) -> Sum;
sum([{Freq, Num}|T], X, Sum) ->
    if X =:= 0 -> Sum;
    true -> sum(T, X - 1, Sum + (-Freq) * Num).
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  def find_x_sum(nums, k, x) do
    result = []
    for i <- 0..(length(nums) - k) do
      count = Enum.reduce(Enum.slice(nums, i, k), %{}, fn num, acc ->
        Map.update(acc, num, 1, &(&1 + 1))
      end)
      pq = Enum.map(count, fn {num, freq} -> {-freq, num} end)
      pq = Enum.sort(pq)
      sum = Enum.reduce(Enum.take(pq, x), 0, fn {freq, num}, acc ->
        acc + (-freq) * num
      end)
      result ++ [sum]
    end
    result
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** 
The time complexity of the approach is O(n * k * log(x)), where n is the length of the input array, k is the length of the subarray, and x is the number of most frequent elements to keep. This is because we need to iterate over each element in the subarray to count its occurrences, and then we need to iterate over the priority queue to calculate the sum of the resulting array.

The time complexity can be broken down as follows:

- Iterating over the input array using a sliding window of size k: O(n)
- Counting the occurrences of each element in the subarray: O(k)
- Using a priority queue to keep track of the top x most frequent elements: O(k * log(x))
- Calculating the sum of the resulting array: O(x)

Therefore, the overall time complexity is O(n * k * log(x)).



- **Space Complexity:** 
The space complexity of the approach is O(k), where k is the length of the subarray. This is because we need to store the occurrences of each element in the subarray in a hash map, and then we need to store the top x most frequent elements in a priority queue.

The space complexity can be broken down as follows:

- Storing the occurrences of each element in the subarray: O(k)
- Storing the top x most frequent elements in a priority queue: O(x)

Therefore, the overall space complexity is O(k).



</div>
</details>
