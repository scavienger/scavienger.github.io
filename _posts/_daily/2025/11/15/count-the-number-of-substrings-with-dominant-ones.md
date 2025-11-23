---
layout: post
title: "Count the Number of Substrings With Dominant Ones"
date: 2025-11-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
---

## Problem #3234: Count the Number of Substrings With Dominant Ones

**Difficulty:** Medium

**Topics:** String, Enumeration

## Problem Description

<p>You are given a binary string <code>s</code>.</p>

<p>Return the number of <span data-keyword="substring-nonempty">substrings</span> with <strong>dominant</strong> ones.</p>

<p>A string has <strong>dominant</strong> ones if the number of ones in the string is <strong>greater than or equal to</strong> the <strong>square</strong> of the number of zeros in the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;00011&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The substrings with dominant ones are shown in the table below.</p>
</div>

<table>
	<thead>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>s[i..j]</th>
			<th>Number of Zeros</th>
			<th>Number of Ones</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>3</td>
			<td>3</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>3</td>
			<td>01</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>4</td>
			<td>11</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>4</td>
			<td>011</td>
			<td>1</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;101101&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>The substrings with <strong>non-dominant</strong> ones are shown in the table below.</p>

<p>Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.</p>
</div>

<table>
	<thead>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>s[i..j]</th>
			<th>Number of Zeros</th>
			<th>Number of Ones</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>1</td>
			<td>4</td>
			<td>0110</td>
			<td>2</td>
			<td>2</td>
		</tr>
		<tr>
			<td>0</td>
			<td>4</td>
			<td>10110</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>1</td>
			<td>5</td>
			<td>01101</td>
			<td>2</td>
			<td>3</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists only of characters <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. Let us fix the starting index `l` of the substring and count the number of indices `r` such that `l <= r` and the substring `s[l..r]` has dominant ones.

2. A substring with dominant ones has at most `sqrt(n)` zeros.

3. We cannot iterate over every `r` and check if the  `s[l..r]` has dominant ones. Instead, we iterate over the next `sqrt(n)` zeros to the left of `l` and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-21 21:46:45 )</small>
</summary>

<div class="ai-solution-content">

### Approach

Iterate through each possible right endpoint `r` of a substring. For each `r`, count substrings `s[l..r]` with dominant ones. This is done by first counting substrings with zero zeros (all ones), then iterating through possible counts of zeros `z` from 1 up to `sqrt(N)`. For each `z`, calculate the valid range for `l` based on the positions of zeros and the dominant ones condition `ones >= zeros^2`, adding the count of valid `l`'s.

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
{% raw %}
class Solution {
public:
    long long numberOfSubstrings(std::string s) {
        int n = s.length();
        long long count = 0;

        int maxZerosLimit = static_cast<int>(std::sqrt(n));

        std::vector<int> zero_indices;

        for (int r = 0; r < n; ++r) {
            // Case 1: Substrings s[l..r] with zero zeros (all '1's)
            // These are substrings s[l..r] where l > last_zero_idx
            if (s[r] == '1') {
                int last_zero_idx = -1;
                if (!zero_indices.empty()) {
                    last_zero_idx = zero_indices.back();
                }
                // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                // have zero zeros and positive ones. They are dominant.
                count += (r - (last_zero_idx + 1) + 1);
            }

            // Case 2: Substrings s[l..r] with one or more zeros
            if (s[r] == '0') {
                zero_indices.push_back(r);
            }

            // Iterate through possible number of zeros (z) in s[l..r]
            // from 1 up to maxZerosLimit
            for (int z = 1; z <= maxZerosLimit; ++z) {
                // If there are not enough zeros in s[0..r] to have 'z' zeros, break
                if (zero_indices.size() < z) {
                    break;
                }

                // p_z is the index of the z-th zero from the right (0-indexed from zero_indices)
                int p_z_idx_in_list = zero_indices.size() - z;
                int p_z = zero_indices[p_z_idx_in_list]; // This is the index of the z-th zero from the right in s

                // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                int left_bound_for_z = -1;
                if (p_z_idx_in_list > 0) {
                    left_bound_for_z = zero_indices[p_z_idx_in_list - 1];
                }

                // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                // The number of ones in s[l..r] is (r - l + 1) - z.
                // We need (r - l + 1) - z >= z*z
                // r - l + 1 - z >= z*z
                // r - z*z - z + 1 >= l

                // So, l must satisfy:
                // 1. l > left_bound_for_z
                // 2. l <= p_z
                // 3. l <= r - z*z - z + 1

                // Combine conditions:
                int l_min = left_bound_for_z + 1;
                int l_max = std::min(p_z, r - z * z - z + 1);

                if (l_max >= l_min) {
                    count += (l_max - l_min + 1);
                }
            }
        }

        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

class Solution {
    public long numberOfSubstrings(String s) {
        int n = s.length();
        long count = 0;

        int maxZerosLimit = (int) Math.sqrt(n);

        List<Integer> zeroIndices = new ArrayList<>(); // Stores indices of '0's

        for (int r = 0; r < n; ++r) {
            // Case 1: Substrings s[l..r] with zero zeros (all '1's)
            // These are substrings s[l..r] where l > last_zero_idx
            if (s.charAt(r) == '1') {
                int last_zero_idx = -1;
                if (!zeroIndices.isEmpty()) {
                    last_zero_idx = zeroIndices.get(zeroIndices.size() - 1);
                }
                // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                // have zero zeros and positive ones. They are dominant.
                count += (r - (last_zero_idx + 1) + 1);
            }

            // Case 2: Substrings s[l..r] with one or more zeros
            if (s.charAt(r) == '0') {
                zeroIndices.add(r);
            }

            // Iterate through possible number of zeros (z) in s[l..r]
            // from 1 up to maxZerosLimit
            for (int z = 1; z <= maxZerosLimit; ++z) {
                // If there are not enough zeros in s[0..r] to have 'z' zeros, break
                if (zeroIndices.size() < z) {
                    break;
                }

                // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
                int p_z_idx_in_list = zeroIndices.size() - z;
                int p_z = zeroIndices.get(p_z_idx_in_list); // This is the index of the z-th zero from the right in s

                // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                int left_bound_for_z = -1;
                if (p_z_idx_in_list > 0) {
                    left_bound_for_z = zeroIndices.get(p_z_idx_in_list - 1);
                }

                // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                // The number of ones in s[l..r] is (r - l + 1) - z.
                // We need (r - l + 1) - z >= z*z
                // r - (long)z * z - z + 1 >= l  (cast z*z to long to prevent overflow, though not strictly needed here)

                // So, l must satisfy:
                // 1. l > left_bound_for_z
                // 2. l <= p_z
                // 3. l <= r - z*z - z + 1

                // Combine conditions:
                int l_min = left_bound_for_z + 1;
                int l_max = Math.min(p_z, r - z * z - z + 1);

                if (l_max >= l_min) {
                    count += (l_max - l_min + 1);
                }
            }
        }

        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        max_zeros_limit = int(math.sqrt(n))

        zero_indices = [] # Stores indices of '0's

        for r in range(n):
            # Case 1: Substrings s[l..r] with zero zeros (all '1's)
            # These are substrings s[l..r] where l > last_zero_idx
            if s[r] == '1':
                last_zero_idx = -1
                if zero_indices:
                    last_zero_idx = zero_indices[-1]
                # All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                # have zero zeros and positive ones. They are dominant.
                count += (r - (last_zero_idx + 1) + 1)

            # Case 2: Substrings s[l..r] with one or more zeros
            if s[r] == '0':
                zero_indices.append(r)

            # Iterate through possible number of zeros (z) in s[l..r]
            # from 1 up to max_zeros_limit
            for z in range(1, max_zeros_limit + 1):
                # If there are not enough zeros in s[0..r] to have 'z' zeros, break
                if len(zero_indices) < z:
                    break

                # p_z is the index of the z-th zero from the right (0-indexed from zero_indices)
                # e.g., if z=1, it's the last zero. If z=2, it's the second to last.
                p_z_idx_in_list = len(zero_indices) - z
                p_z = zero_indices[p_z_idx_in_list] # This is the index of the z-th zero from the right in s

                # left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                # Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                left_bound_for_z = -1
                if p_z_idx_in_list > 0:
                    left_bound_for_z = zero_indices[p_z_idx_in_list - 1]

                # For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                # The number of ones in s[l..r] is (r - l + 1) - z.
                # We need (r - l + 1) - z >= z*z
                # r - l + 1 - z >= z*z
                # r - z*z - z + 1 >= l

                # So, l must satisfy:
                # 1. l > left_bound_for_z
                # 2. l <= p_z
                # 3. l <= r - z*z - z + 1

                # Combine conditions:
                l_min = left_bound_for_z + 1
                l_max = min(p_z, r - z * z - z + 1)

                if l_max >= l_min:
                    count += (l_max - l_min + 1)

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        max_zeros_limit = int(math.sqrt(n))

        zero_indices = [] # Stores indices of '0's

        for r in range(n):
            # Case 1: Substrings s[l..r] with zero zeros (all '1's)
            # These are substrings s[l..r] where l > last_zero_idx
            if s[r] == '1':
                last_zero_idx = -1
                if zero_indices:
                    last_zero_idx = zero_indices[-1]
                # All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                # have zero zeros and positive ones. They are dominant.
                count += (r - (last_zero_idx + 1) + 1)

            # Case 2: Substrings s[l..r] with one or more zeros
            if s[r] == '0':
                zero_indices.append(r)

            # Iterate through possible number of zeros (z) in s[l..r]
            # from 1 up to max_zeros_limit
            for z in range(1, max_zeros_limit + 1):
                # If there are not enough zeros in s[0..r] to have 'z' zeros, break
                if len(zero_indices) < z:
                    break

                # p_z is the index of the z-th zero from the right (0-indexed from zero_indices)
                # e.g., if z=1, it's the last zero. If z=2, it's the second to last.
                p_z_idx_in_list = len(zero_indices) - z
                p_z = zero_indices[p_z_idx_in_list] # This is the index of the z-th zero from the right in s

                # left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                # Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                left_bound_for_z = -1
                if p_z_idx_in_list > 0:
                    left_bound_for_z = zero_indices[p_z_idx_in_list - 1]

                # For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                # The number of ones in s[l..r] is (r - l + 1) - z.
                # We need (r - l + 1) - z >= z*z
                # r - l + 1 - z >= z*z
                # r - z*z - z + 1 >= l

                # So, l must satisfy:
                # 1. l > left_bound_for_z
                # 2. l <= p_z
                # 3. l <= r - z*z - z + 1

                # Combine conditions:
                l_min = left_bound_for_z + 1
                l_max = min(p_z, r - z * z - z + 1)

                if l_max >= l_min:
                    count += (l_max - l_min + 1)

        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <math.h>
#include <stdlib.h> // For malloc, free

// A dynamic array (vector) implementation for zero_indices
typedef struct {
    int* arr;
    int size;
    int capacity;
} IntVector;

void initIntVector(IntVector* vec, int initialCapacity) {
    vec->arr = (int*)malloc(sizeof(int) * initialCapacity);
    vec->size = 0;
    vec->capacity = initialCapacity;
}

void pushBackIntVector(IntVector* vec, int item) {
    if (vec->size == vec->capacity) {
        vec->capacity *= 2;
        vec->arr = (int*)realloc(vec->arr, sizeof(int) * vec->capacity);
    }
    vec->arr[vec->size++] = item;
}

int getIntVector(IntVector* vec, int index) {
    return vec->arr[index];
}

int getLastIntVector(IntVector* vec) {
    return vec->arr[vec->size - 1];
}

void freeIntVector(IntVector* vec) {
    free(vec->arr);
    vec->arr = NULL;
    vec->size = 0;
    vec->capacity = 0;
}

long long numberOfSubstrings(char * s) {
    int n = strlen(s);
    long long count = 0;

    int maxZerosLimit = (int) sqrt(n);

    IntVector zero_indices;
    initIntVector(&zero_indices, n / 2 + 1); // Initial capacity can be N/2

    for (int r = 0; r < n; ++r) {
        // Case 1: Substrings s[l..r] with zero zeros (all '1's)
        // These are substrings s[l..r] where l > last_zero_idx
        if (s[r] == '1') {
            int last_zero_idx = -1;
            if (zero_indices.size > 0) {
                last_zero_idx = getLastIntVector(&zero_indices);
            }
            // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
            // have zero zeros and positive ones. They are dominant.
            count += (r - (last_zero_idx + 1) + 1);
        }

        // Case 2: Substrings s[l..r] with one or more zeros
        if (s[r] == '0') {
            pushBackIntVector(&zero_indices, r);
        }

        // Iterate through possible number of zeros (z) in s[l..r]
        // from 1 up to maxZerosLimit
        for (int z = 1; z <= maxZerosLimit; ++z) {
            // If there are not enough zeros in s[0..r] to have 'z' zeros, break
            if (zero_indices.size < z) {
                break;
            }

            // p_z is the index of the z-th zero from the right (0-indexed from zero_indices)
            int p_z_idx_in_list = zero_indices.size - z;
            int p_z = getIntVector(&zero_indices, p_z_idx_in_list); // This is the index of the z-th zero from the right in s

            // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
            // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
            int left_bound_for_z = -1;
            if (p_z_idx_in_list > 0) {
                left_bound_for_z = getIntVector(&zero_indices, p_z_idx_in_list - 1);
            }

            // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
            // The number of ones in s[l..r] is (r - l + 1) - z.
            // We need (r - l + 1) - z >= z*z
            // r - l + 1 - z >= z*z
            // r - (long long)z * z - z + 1 >= l

            // So, l must satisfy:
            // 1. l > left_bound_for_z
            // 2. l <= p_z
            // 3. l <= r - z*z - z + 1

            // Combine conditions:
            int l_min = left_bound_for_z + 1;
            int l_max = p_z; // Initial upper bound for l
            long long required_ones_sq = (long long)z * z;

            // Adjust l_max based on the dominant ones condition
            // We need (r - l + 1) - z >= z*z
            // r - z*z - z + 1 >= l
            int max_l_from_ones_cond = r - (int)required_ones_sq - z + 1;
            l_max = (l_max < max_l_from_ones_cond) ? l_max : max_l_from_ones_cond;

            if (l_max >= l_min) {
                count += (l_max - l_min + 1);
            }
        }
    }

    freeIntVector(&zero_indices);
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public long NumberOfSubstrings(string s) {
        int n = s.Length;
        long count = 0;

        int maxZerosLimit = (int) Math.Sqrt(n);

        List<int> zeroIndices = new List<int>(); // Stores indices of '0's

        for (int r = 0; r < n; ++r) {
            // Case 1: Substrings s[l..r] with zero zeros (all '1's)
            // These are substrings s[l..r] where l > last_zero_idx
            if (s[r] == '1') {
                int last_zero_idx = -1;
                if (zeroIndices.Count > 0) {
                    last_zero_idx = zeroIndices[zeroIndices.Count - 1];
                }
                // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                // have zero zeros and positive ones. They are dominant.
                count += (r - (last_zero_idx + 1) + 1);
            }

            // Case 2: Substrings s[l..r] with one or more zeros
            if (s[r] == '0') {
                zeroIndices.Add(r);
            }

            // Iterate through possible number of zeros (z) in s[l..r]
            // from 1 up to maxZerosLimit
            for (int z = 1; z <= maxZerosLimit; ++z) {
                // If there are not enough zeros in s[0..r] to have 'z' zeros, break
                if (zeroIndices.Count < z) {
                    break;
                }

                // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
                int p_z_idx_in_list = zeroIndices.Count - z;
                int p_z = zeroIndices[p_z_idx_in_list]; // This is the index of the z-th zero from the right in s

                // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                int left_bound_for_z = -1;
                if (p_z_idx_in_list > 0) {
                    left_bound_for_z = zeroIndices[p_z_idx_in_list - 1];
                }

                // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                // The number of ones in s[l..r] is (r - l + 1) - z.
                // We need (r - l + 1) - z >= z*z
                // r - l + 1 - z >= z*z
                // r - (long)z * z - z + 1 >= l

                // So, l must satisfy:
                // 1. l > left_bound_for_z
                // 2. l <= p_z
                // 3. l <= r - z*z - z + 1

                // Combine conditions:
                int l_min = left_bound_for_z + 1;
                int l_max = Math.Min(p_z, r - z * z - z + 1);

                if (l_max >= l_min) {
                    count += (l_max - l_min + 1);
                }
            }
        }

        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const n = s.length;
    let count = 0;

    const maxZerosLimit = Math.floor(Math.sqrt(n));

    const zeroIndices = []; // Stores indices of '0's

    for (let r = 0; r < n; ++r) {
        // Case 1: Substrings s[l..r] with zero zeros (all '1's)
        // These are substrings s[l..r] where l > last_zero_idx
        if (s[r] === '1') {
            let last_zero_idx = -1;
            if (zeroIndices.length > 0) {
                last_zero_idx = zeroIndices[zeroIndices.length - 1];
            }
            // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
            // have zero zeros and positive ones. They are dominant.
            count += (r - (last_zero_idx + 1) + 1);
        }

        // Case 2: Substrings s[l..r] with one or more zeros
        if (s[r] === '0') {
            zeroIndices.push(r);
        }

        // Iterate through possible number of zeros (z) in s[l..r]
        // from 1 up to maxZerosLimit
        for (let z = 1; z <= maxZerosLimit; ++z) {
            // If there are not enough zeros in s[0..r] to have 'z' zeros, break
            if (zeroIndices.length < z) {
                break;
            }

            // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
            // e.g., if z=1, it's the last zero. If z=2, it's the second to last.
            const p_z_idx_in_list = zeroIndices.length - z;
            const p_z = zeroIndices[p_z_idx_in_list]; // This is the index of the z-th zero from the right in s

            // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
            // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
            let left_bound_for_z = -1;
            if (p_z_idx_in_list > 0) {
                left_bound_for_z = zeroIndices[p_z_idx_in_list - 1];
            }

            // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
            // The number of ones in s[l..r] is (r - l + 1) - z.
            // We need (r - l + 1) - z >= z*z
            // r - l + 1 - z >= z*z
            // r - z*z - z + 1 >= l

            // So, l must satisfy:
            // 1. l > left_bound_for_z
            // 2. l <= p_z
            // 3. l <= r - z*z - z + 1

            // Combine conditions:
            const l_min = left_bound_for_z + 1;
            const l_max = Math.min(p_z, r - z * z - z + 1);

            if (l_max >= l_min) {
                count += (l_max - l_min + 1);
            }
        }
    }

    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfSubstrings(s: string): number {
    const n: number = s.length;
    let count: number = 0;

    const maxZerosLimit: number = Math.floor(Math.sqrt(n));

    const zeroIndices: number[] = []; // Stores indices of '0's

    for (let r = 0; r < n; ++r) {
        // Case 1: Substrings s[l..r] with zero zeros (all '1's)
        // These are substrings s[l..r] where l > last_zero_idx
        if (s[r] === '1') {
            let last_zero_idx: number = -1;
            if (zeroIndices.length > 0) {
                last_zero_idx = zeroIndices[zeroIndices.length - 1];
            }
            // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
            // have zero zeros and positive ones. They are dominant.
            count += (r - (last_zero_idx + 1) + 1);
        }

        // Case 2: Substrings s[l..r] with one or more zeros
        if (s[r] === '0') {
            zeroIndices.push(r);
        }

        // Iterate through possible number of zeros (z) in s[l..r]
        // from 1 up to maxZerosLimit
        for (let z = 1; z <= maxZerosLimit; ++z) {
            // If there are not enough zeros in s[0..r] to have 'z' zeros, break
            if (zeroIndices.length < z) {
                break;
            }

            // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
            // e.g., if z=1, it's the last zero. If z=2, it's the second to last.
            const p_z_idx_in_list: number = zeroIndices.length - z;
            const p_z: number = zeroIndices[p_z_idx_in_list]; // This is the index of the z-th zero from the right in s

            // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
            // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
            let left_bound_for_z: number = -1;
            if (p_z_idx_in_list > 0) {
                left_bound_for_z = zeroIndices[p_z_idx_in_list - 1];
            }

            // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
            // The number of ones in s[l..r] is (r - l + 1) - z.
            // We need (r - l + 1) - z >= z*z
            // r - l + 1 - z >= z*z
            // r - z*z - z + 1 >= l

            // So, l must satisfy:
            // 1. l > left_bound_for_z
            // 2. l <= p_z
            // 3. l <= r - z*z - z + 1

            // Combine conditions:
            const l_min: number = left_bound_for_z + 1;
            const l_max: number = Math.min(p_z, r - z * z - z + 1);

            if (l_max >= l_min) {
                count += (l_max - l_min + 1);
            }
        }
    }

    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numberOfSubstrings($s) {
        $n = strlen($s);
        $count = 0;

        $maxZerosLimit = (int) sqrt($n);

        $zeroIndices = []; // Stores indices of '0's

        for ($r = 0; $r < $n; ++$r) {
            // Case 1: Substrings s[l..r] with zero zeros (all '1's)
            // These are substrings s[l..r] where l > last_zero_idx
            if ($s[$r] === '1') {
                $last_zero_idx = -1;
                if (!empty($zeroIndices)) {
                    $last_zero_idx = end($zeroIndices);
                }
                // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                // have zero zeros and positive ones. They are dominant.
                $count += ($r - ($last_zero_idx + 1) + 1);
            }

            // Case 2: Substrings s[l..r] with one or more zeros
            if ($s[$r] === '0') {
                $zeroIndices[] = $r;
            }

            // Iterate through possible number of zeros (z) in s[l..r]
            // from 1 up to maxZerosLimit
            for ($z = 1; $z <= $maxZerosLimit; ++$z) {
                // If there are not enough zeros in s[0..r] to have 'z' zeros, break
                if (count($zeroIndices) < $z) {
                    break;
                }

                // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
                // e.g., if z=1, it's the last zero. If z=2, it's the second to last.
                $p_z_idx_in_list = count($zeroIndices) - $z;
                $p_z = $zeroIndices[$p_z_idx_in_list]; // This is the index of the z-th zero from the right in s

                // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                $left_bound_for_z = -1;
                if ($p_z_idx_in_list > 0) {
                    $left_bound_for_z = $zeroIndices[$p_z_idx_in_list - 1];
                }

                // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                // The number of ones in s[l..r] is (r - l + 1) - z.
                // We need (r - l + 1) - z >= z*z
                // r - l + 1 - z >= z*z
                // r - $z*$z - z + 1 >= l

                // So, l must satisfy:
                // 1. l > left_bound_for_z
                // 2. l <= p_z
                // 3. l <= r - z*z - z + 1

                // Combine conditions:
                $l_min = $left_bound_for_z + 1;
                $l_max = min($p_z, $r - $z * $z - $z + 1);

                if ($l_max >= $l_min) {
                    $count += ($l_max - $l_min + 1);
                }
            }
        }

        return $count;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func numberOfSubstrings(_ s: String) -> Int {
        let n = s.count
        var count = 0
        let sChars = Array(s) // For O(1) character access

        let maxZerosLimit = Int(sqrt(Double(n)))

        var zeroIndices: [Int] = [] // Stores indices of '0's

        for r in 0..<n {
            // Case 1: Substrings s[l..r] with zero zeros (all '1's)
            // These are substrings s[l..r] where l > last_zero_idx
            if sChars[r] == "1" {
                var last_zero_idx = -1
                if let last = zeroIndices.last {
                    last_zero_idx = last
                }
                // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                // have zero zeros and positive ones. They are dominant.
                count += (r - (last_zero_idx + 1) + 1)
            }

            // Case 2: Substrings s[l..r] with one or more zeros
            if sChars[r] == "0" {
                zeroIndices.append(r)
            }

            // Iterate through possible number of zeros (z) in s[l..r]
            // from 1 up to maxZerosLimit
            for z in 1...maxZerosLimit {
                // If there are not enough zeros in s[0..r] to have 'z' zeros, break
                if zeroIndices.count < z {
                    break
                }

                // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
                // e.g., if z=1, it's the last zero. If z=2, it's the second to last.
                let p_z_idx_in_list = zeroIndices.count - z
                let p_z = zeroIndices[p_z_idx_in_list] // This is the index of the z-th zero from the right in s

                // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                var left_bound_for_z = -1
                if p_z_idx_in_list > 0 {
                    left_bound_for_z = zeroIndices[p_z_idx_in_list - 1]
                }

                // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                // The number of ones in s[l..r] is (r - l + 1) - z.
                // We need (r - l + 1) - z >= z*z
                // r - l + 1 - z >= z*z
                // r - z*z - z + 1 >= l

                // So, l must satisfy:
                // 1. l > left_bound_for_z
                // 2. l <= p_z
                // 3. l <= r - z*z - z + 1

                // Combine conditions:
                let l_min = left_bound_for_z + 1
                let l_max = min(p_z, r - z * z - z + 1)

                if l_max >= l_min {
                    count += (l_max - l_min + 1)
                }
            }
        }

        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.sqrt
import kotlin.math.min

class Solution {
    fun numberOfSubstrings(s: String): Long {
        val n = s.length
        var count: Long = 0

        val maxZerosLimit = sqrt(n.toDouble()).toInt()

        val zeroIndices = mutableListOf<Int>() // Stores indices of '0's

        for (r in 0 until n) {
            // Case 1: Substrings s[l..r] with zero zeros (all '1's)
            // These are substrings s[l..r] where l > last_zero_idx
            if (s[r] == '1') {
                var last_zero_idx = -1
                if (zeroIndices.isNotEmpty()) {
                    last_zero_idx = zeroIndices.last()
                }
                // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                // have zero zeros and positive ones. They are dominant.
                count += (r - (last_zero_idx + 1) + 1)
            }

            // Case 2: Substrings s[l..r] with one or more zeros
            if (s[r] == '0') {
                zeroIndices.add(r)
            }

            // Iterate through possible number of zeros (z) in s[l..r]
            // from 1 up to maxZerosLimit
            for (z in 1..maxZerosLimit) {
                // If there are not enough zeros in s[0..r] to have 'z' zeros, break
                if (zeroIndices.size < z) {
                    break
                }

                // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
                // e.g., if z=1, it's the last zero. If z=2, it's the second to last.
                val p_z_idx_in_list = zeroIndices.size - z
                val p_z = zeroIndices[p_z_idx_in_list] // This is the index of the z-th zero from the right in s

                // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                var left_bound_for_z = -1
                if (p_z_idx_in_list > 0) {
                    left_bound_for_z = zeroIndices[p_z_idx_in_list - 1]
                }

                // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                // The number of ones in s[l..r] is (r - l + 1) - z.
                // We need (r - l + 1) - z >= z*z
                // r - l + 1 - z >= z*z
                // r - z*z - z + 1 >= l

                // So, l must satisfy:
                // 1. l > left_bound_for_z
                // 2. l <= p_z
                // 3. l <= r - z*z - z + 1

                // Combine conditions:
                val l_min = left_bound_for_z + 1
                val l_max = min(p_z, r - z * z - z + 1)

                if (l_max >= l_min) {
                    count += (l_max - l_min + 1)
                }
            }
        }

        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int numberOfSubstrings(String s) {
    final n = s.length;
    int count = 0;

    final maxZerosLimit = sqrt(n).floor();

    final zeroIndices = <int>[]; // Stores indices of '0's

    for (int r = 0; r < n; ++r) {
      // Case 1: Substrings s[l..r] with zero zeros (all '1's)
      // These are substrings s[l..r] where l > last_zero_idx
      if (s[r] == '1') {
        int last_zero_idx = -1;
        if (zeroIndices.isNotEmpty) {
          last_zero_idx = zeroIndices.last;
        }
        // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
        // have zero zeros and positive ones. They are dominant.
        count += (r - (last_zero_idx + 1) + 1);
      }

      // Case 2: Substrings s[l..r] with one or more zeros
      if (s[r] == '0') {
        zeroIndices.add(r);
      }

      // Iterate through possible number of zeros (z) in s[l..r]
      // from 1 up to maxZerosLimit
      for (int z = 1; z <= maxZerosLimit; ++z) {
        // If there are not enough zeros in s[0..r] to have 'z' zeros, break
        if (zeroIndices.length < z) {
          break;
        }

        // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
        // e.g., if z=1, it's the last zero. If z=2, it's the second to last.
        final p_z_idx_in_list = zeroIndices.length - z;
        final p_z = zeroIndices[p_z_idx_in_list]; // This is the index of the z-th zero from the right in s

        // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
        // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
        int left_bound_for_z = -1;
        if (p_z_idx_in_list > 0) {
          left_bound_for_z = zeroIndices[p_z_idx_in_list - 1];
        }

        // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
        // The number of ones in s[l..r] is (r - l + 1) - z.
        // We need (r - l + 1) - z >= z*z
        // r - l + 1 - z >= z*z
        // r - z*z - z + 1 >= l

        // So, l must satisfy:
        // 1. l > left_bound_for_z
        // 2. l <= p_z
        // 3. l <= r - z*z - z + 1

        // Combine conditions:
        final l_min = left_bound_for_z + 1;
        final l_max = min(p_z, r - z * z - z + 1);

        if (l_max >= l_min) {
          count += (l_max - l_min + 1);
        }
      }
    }

    return count;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"math"
	"sort"
)

func numberOfSubstrings(s string) int {
    n := len(s)
    var count int

    maxZerosLimit := int(math.Sqrt(float64(n)))

    zeroIndices := []int{} // Stores indices of '0's

    for r := 0; r < n; r++ {
        // Case 1: Substrings s[l..r] with zero zeros (all '1's)
        // These are substrings s[l..r] where l > last_zero_idx
        if s[r] == '1' {
            last_zero_idx := -1
            if len(zeroIndices) > 0 {
                last_zero_idx = zeroIndices[len(zeroIndices) - 1]
            }
            // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
            // have zero zeros and positive ones. They are dominant.
            count += (r - (last_zero_idx + 1) + 1)
        }

        // Case 2: Substrings s[l..r] with one or more zeros
        if s[r] == '0' {
            zeroIndices = append(zeroIndices, r)
        }

        // Iterate through possible number of zeros (z) in s[l..r]
        // from 1 up to maxZerosLimit
        for z := 1; z <= maxZerosLimit; z++ {
            // If there are not enough zeros in s[0..r] to have 'z' zeros, break
            if len(zeroIndices) < z {
                break
            }

            // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
            // e.g., if z=1, it's the last zero. If z=2, it's the second to last.
            p_z_idx_in_list := len(zeroIndices) - z
            p_z := zeroIndices[p_z_idx_in_list] // This is the index of the z-th zero from the right in s

            // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
            // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
            left_bound_for_z := -1
            if p_z_idx_in_list > 0 {
                left_bound_for_z = zeroIndices[p_z_idx_in_list - 1]
            }

            // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
            // The number of ones in s[l..r] is (r - l + 1) - z.
            // We need (r - l + 1) - z >= z*z
            // r - l + 1 - z >= z*z
            // r - z*z - z + 1 >= l

            // So, l must satisfy:
            // 1. l > left_bound_for_z
            // 2. l <= p_z
            // 3. l <= r - z*z - z + 1

            // Combine conditions:
            l_min := left_bound_for_z + 1
            l_max := min(p_z, r - z * z - z + 1)

            if l_max >= l_min {
                count += (l_max - l_min + 1)
            }
        }
    }

    return count
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def number_of_substrings(s)
        n = s.length
        count = 0

        max_zeros_limit = Math.sqrt(n).to_i

        zero_indices = [] # Stores indices of '0's

        (0...n).each do |r|
            # Case 1: Substrings s[l..r] with zero zeros (all '1's)
            # These are substrings s[l..r] where l > last_zero_idx
            if s[r] == '1'
                last_zero_idx = -1
                if !zero_indices.empty?
                    last_zero_idx = zero_indices.last
                end
                # All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                # have zero zeros and positive ones. They are dominant.
                count += (r - (last_zero_idx + 1) + 1)
            end

            # Case 2: Substrings s[l..r] with one or more zeros
            if s[r] == '0'
                zero_indices.push(r)
            end

            # Iterate through possible number of zeros (z) in s[l..r]
            # from 1 up to max_zeros_limit
            (1..max_zeros_limit).each do |z|
                # If there are not enough zeros in s[0..r] to have 'z' zeros, break
                if zero_indices.length < z
                    break
                end

                # p_z is the index of the z-th zero from the right (0-indexed from zero_indices)
                # e.g., if z=1, it's the last zero. If z=2, it's the second to last.
                p_z_idx_in_list = zero_indices.length - z
                p_z = zero_indices[p_z_idx_in_list] # This is the index of the z-th zero from the right in s

                # left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                # Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                left_bound_for_z = -1
                if p_z_idx_in_list > 0
                    left_bound_for_z = zero_indices[p_z_idx_in_list - 1]
                end

                # For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                # The number of ones in s[l..r] is (r - l + 1) - z.
                # We need (r - l + 1) - z >= z*z
                # r - l + 1 - z >= z*z
                # r - z*z - z + 1 >= l

                # So, l must satisfy:
                # 1. l > left_bound_for_z
                # 2. l <= p_z
                # 3. l <= r - z*z - z + 1

                # Combine conditions:
                l_min = left_bound_for_z + 1
                l_max = [p_z, r - z * z - z + 1].min

                if l_max >= l_min
                    count += (l_max - l_min + 1)
                end
            end
        end

        count
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.math
import scala.collection.mutable.ListBuffer
import scala.util.control.Breaks._

object Solution {
    def numberOfSubstrings(s: String): Long = {
        val n = s.length
        var count: Long = 0

        val maxZerosLimit = math.sqrt(n.toDouble).toInt

        val zeroIndices = ListBuffer[Int]() // Stores indices of '0's

        for (r <- 0 until n) {
            // Case 1: Substrings s[l..r] with zero zeros (all '1's)
            // These are substrings s[l..r] where l > last_zero_idx
            if (s(r) == '1') {
                var last_zero_idx = -1
                if (zeroIndices.nonEmpty) {
                    last_zero_idx = zeroIndices.last
                }
                // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                // have zero zeros and positive ones. They are dominant.
                count += (r - (last_zero_idx + 1) + 1)
            }

            // Case 2: Substrings s[l..r] with one or more zeros
            if (s(r) == '0') {
                zeroIndices.append(r)
            }

            // Iterate through possible number of zeros (z) in s[l..r]
            // from 1 up to maxZerosLimit
            breakable {
                for (z <- 1 to maxZerosLimit) {
                    // If there are not enough zeros in s[0..r] to have 'z' zeros, break
                    if (zeroIndices.size < z) {
                        break
                    }

                    // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
                    // e.g., if z=1, it's the last zero. If z=2, it's the second to last.
                    val p_z_idx_in_list = zeroIndices.size - z
                    val p_z = zeroIndices(p_z_idx_in_list) // This is the index of the z-th zero from the right in s

                    // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                    // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                    var left_bound_for_z = -1
                    if (p_z_idx_in_list > 0) {
                        left_bound_for_z = zeroIndices(p_z_idx_in_list - 1)
                    }

                    // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                    // The number of ones in s[l..r] is (r - l + 1) - z.
                    // We need (r - l + 1) - z >= z*z
                    // r - l + 1 - z >= z*z
                    // r - z*z - z + 1 >= l

                    // So, l must satisfy:
                    // 1. l > left_bound_for_z
                    // 2. l <= p_z
                    // 3. l <= r - z*z - z + 1

                    // Combine conditions:
                    val l_min = left_bound_for_z + 1
                    val l_max = math.min(p_z, r - z * z - z + 1)

                    if (l_max >= l_min) {
                        count += (l_max - l_min + 1)
                    }
                }
            }
        }

        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn number_of_substrings(s: String) -> i64 {
        let n = s.len();
        let s_bytes = s.as_bytes(); // For O(1) character access
        let mut count: i64 = 0;

        let max_zeros_limit = (n as f64).sqrt() as usize;

        let mut zero_indices: Vec<usize> = Vec::new(); // Stores indices of '0's

        for r in 0..n {
            // Case 1: Substrings s[l..r] with zero zeros (all '1's)
            // These are substrings s[l..r] where l > last_zero_idx
            if s_bytes[r] == b'1' {
                let mut last_zero_idx = -1;
                if let Some(&last) = zero_indices.last() {
                    last_zero_idx = last as i32;
                }
                // All substrings s[l..r] where l is in [last_zero_idx + 1, r]
                // have zero zeros and positive ones. They are dominant.
                count += (r as i64 - (last_zero_idx as i64 + 1) + 1);
            }

            // Case 2: Substrings s[l..r] with one or more zeros
            if s_bytes[r] == b'0' {
                zero_indices.push(r);
            }

            // Iterate through possible number of zeros (z) in s[l..r]
            // from 1 up to maxZerosLimit
            for z in 1..=max_zeros_limit {
                // If there are not enough zeros in s[0..r] to have 'z' zeros, break
                if zero_indices.len() < z {
                    break;
                }

                // p_z is the index of the z-th zero from the right (0-indexed from zeroIndices)
                // e.g., if z=1, it's the last zero. If z=2, it's the second to last.
                let p_z_idx_in_list = zero_indices.len() - z;
                let p_z = zero_indices[p_z_idx_in_list]; // This is the index of the z-th zero from the right in s

                // left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                // Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                let mut left_bound_for_z = -1;
                if p_z_idx_in_list > 0 {
                    left_bound_for_z = zero_indices[p_z_idx_in_list - 1] as i32;
                }

                // For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
                // The number of ones in s[l..r] is (r - l + 1) - z.
                // We need (r - l + 1) - z >= z*z
                // r - l + 1 - z >= z*z
                // r - z*z - z + 1 >= l

                // So, l must satisfy:
                // 1. l > left_bound_for_z
                // 2. l <= p_z
                // 3. l <= r - z*z - z + 1

                // Combine conditions:
                let l_min = left_bound_for_z + 1;
                let l_max = std::cmp::min(p_z as i32, r as i32 - (z * z) as i32 - z as i32 + 1);

                if l_max >= l_min {
                    count += (l_max - l_min + 1) as i64;
                }
            }
        }

        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (number-of-substrings s)
  (define n (string-length s))
  (define count 0)

  (define max-zeros-limit (floor (sqrt n)))

  (define zero-indices (make-vector 0)) ; Stores indices of '0's

  (for ([r (in-range n)])
    ;; Case 1: Substrings s[l..r] with zero zeros (all '1's)
    ;; These are substrings s[l..r] where l > last_zero_idx
    (when (char=? (string-ref s r) #\1)
      (define last-zero-idx -1)
      (when (> (vector-length zero-indices) 0)
        (set! last-zero-idx (vector-ref zero-indices (- (vector-length zero-indices) 1))))
      ;; All substrings s[l..r] where l is in [last_zero_idx + 1, r]
      ;; have zero zeros and positive ones. They are dominant.
      (set! count (+ count (- r last-zero-idx))))

    ;; Case 2: Substrings s[l..r] with one or more zeros
    (when (char=? (string-ref s r) #\0)
      (set! zero-indices (vector-append zero-indices (vector r))))

    ;; Iterate through possible number of zeros (z) in s[l..r]
    ;; from 1 up to max-zeros-limit
    (for ([z (in-range 1 (+ max-zeros-limit 1))])
      ;; If there are not enough zeros in s[0..r] to have 'z' zeros, break
      (when (< (vector-length zero-indices) z)
        (break))

      ;; p_z is the index of the z-th zero from the right (0-indexed from zero-indices)
      ;; e.g., if z=1, it's the last zero. If z=2, it's the second to last.
      (define p-z-idx-in-list (- (vector-length zero-indices) z))
      (define p-z (vector-ref zero-indices p-z-idx-in-list)) ; This is the index of the z-th zero from the right in s

      ;; left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
      ;; Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
      (define left-bound-for-z -1)
      (when (> p-z-idx-in-list 0)
        (set! left-bound-for-z (vector-ref zero-indices (- p-z-idx-in-list 1))))

      ;; For a substring s[l..r] to have exactly 'z' zeros, 'l' must be in (left_bound_for_z, p_z].
      ;; The number of ones in s[l..r] is (r - l + 1) - z.
      ;; We need (r - l + 1) - z >= z*z
      ;; r - l + 1 - z >= z*z
      ;; r - z*z - z + 1 >= l

      ;; So, l must satisfy:
      ;; 1. l > left_bound_for_z
      ;; 2. l <= p_z
      ;; 3. l <= r - z*z - z + 1

      ;; Combine conditions:
      (define l-min (+ left-bound-for-z 1))
      (define l-max (min p-z (- r (* z z) z -1)))

      (when (>= l-max l-min)
        (set! count (+ count (- l-max l-min -1))))))
  count)

(provide number-of-substrings)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([number_of_substrings/1]).

number_of_substrings(S) ->
    S_bin = list_to_binary(S),
    N = byte_size(S_bin),
    MaxZerosLimit = trunc(math:sqrt(N)),

    {FinalCount, _} = lists:foldl(fun(R, AccState) ->
        {CurrentCount, ZeroIndices} = AccState,

        % Case 1: Substrings s[l..r] with zero zeros (all '1's)
        CharR = binary:at(S_bin, R),
        CountForZeroZeros = if CharR == $1 ->
                                    LastZeroIdx = if lists:is_empty(ZeroIndices) -> -1; true -> lists:last(ZeroIndices) end,
                                    (R - (LastZeroIdx + 1) + 1);
                                true -> 0
                            end,

        UpdatedCount = CurrentCount + CountForZeroZeros,

        % Case 2: Substrings s[l..r] with one or more zeros
        UpdatedZeroIndices = if CharR == $0 ->
                                     ZeroIndices ++ [R];
                                 true -> ZeroIndices
                             end,

        % Iterate through possible number of zeros (z) in s[l..r]
        % from 1 up to MaxZerosLimit
        InnerLoop = fun
            (Z, LoopAccCount) when Z > MaxZerosLimit -> LoopAccCount;
            (Z, LoopAccCount) ->
                % If there are not enough zeros in S_bin[0..R] to have 'z' zeros, break
                if length(UpdatedZeroIndices) < Z ->
                    LoopAccCount;
                true ->
                    % p_z is the index of the z-th zero from the right (0-indexed from zero_indices)
                    PZIdxInList = length(UpdatedZeroIndices) - Z,
                    PZ = lists:nth(PZIdxInList + 1, UpdatedZeroIndices), % Erlang lists are 1-indexed

                    % left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
                    % Any 'l' must be > left_bound_for_z to ensure exactly 'z' zeros.
                    LeftBoundForZ = if PZIdxInList > 0 ->
                                        lists:nth(PZIdxInList, UpdatedZeroIndices);
                                    true -> -1
                                end,

                    % Combine conditions:
                    LMin = LeftBoundForZ + 1,
                    LMax = min(PZ, R - Z * Z - Z + 1),

                    AddedCount = if LMax >= LMin -> (LMax - LMin + 1); true -> 0 end,
                    InnerLoop(Z + 1, LoopAccCount + AddedCount)
                end
        end,

        FinalCountForR = InnerLoop(1, UpdatedCount),
        {FinalCountForR, UpdatedZeroIndices}
    end, {0, []}, lists:seq(0, N - 1)),

    FinalCount.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec number_of_substrings(s :: String.t) :: integer
  def number_of_substrings(s) do
    n = String.length(s)

    max_zeros_limit = :math.sqrt(n) |> trunc

    {final_count, _} = Enum.reduce(0..(n - 1), {0, []}, fn r, {current_count, zero_indices} ->
      # Case 1: Substrings s[l..r] with zero zeros (all '1's)
      char_r = String.at(s, r)
      count_for_zero_zeros = if char_r == "1" do
        last_zero_idx = if Enum.empty?(zero_indices), do: -1, else: List.last(zero_indices)
        r - (last_zero_idx + 1) + 1
      else
        0
      end

      updated_count = current_count + count_for_zero_zeros

      # Case 2: Substrings s[l..r] with one or more zeros
      updated_zero_indices = if char_r == "0" do
        zero_indices ++ [r]
      else
        zero_indices
      end

      # Iterate through possible number of zeros (z) in s[l..r]
      # from 1 up to max_zeros_limit
      inner_loop = fn
        z, loop_acc_count when z > max_zeros_limit -> loop_acc_count
        z, loop_acc_count ->
          # If there are not enough zeros in s[0..r] to have 'z' zeros, break
          if length(updated_zero_indices) < z do
            loop_acc_count
          else
            # p_z is the index of the z-th zero from the right (0-indexed from zero_indices)
            p_z_idx_in_list = length(updated_zero_indices) - z
            p_z = Enum.at(updated_zero_indices, p_z_idx_in_list)

            # left_bound_for_z is the index of the (z+1)-th zero from the right, or -1 if none.
            left_bound_for_z = if p_z_idx_in_list > 0 do
              Enum.at(updated_zero_indices, p_z_idx_in_list - 1)
            else
              -1
            end

            # Combine conditions:
            l_min = left_bound_for_z + 1
            l_max = min(p_z, r - z * z - z + 1)

            added_count = if l_max >= l_min, do: (l_max - l_min + 1), else: 0

            &1.(z + 1, loop_acc_count + added_count)
          end
      end

      final_count_for_r = inner_loop.(1, updated_count)
      {final_count_for_r, updated_zero_indices}
    end)

    final_count
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * sqrt(N))

- **Space Complexity:** O(N)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-21 21:46:52 )</small>
</summary>

<div class="ai-solution-content">

### Approach

This problem can be solved by iterating over all possible substrings of the given string and checking if the number of ones is greater than or equal to the square of the number of zeros. We can use a simple loop to generate all substrings and then count the ones and zeros in each substring.

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
{% raw %}
#include <iostream>
       #include <string>
       using namespace std;

       class Solution {
       public:
           int numberOfSubstrings(string s) {
               int count = 0;
               for (int i = 0; i < s.length(); i++) {
                   for (int j = i; j < s.length(); j++) {
                       int ones = 0, zeros = 0;
                       for (int k = i; k <= j; k++) {
                           if (s[k] == '1') ones++;
                           else zeros++;
                       }
                       if (ones >= zeros * zeros) count++;
                   }
               }
               return count;
           }
       };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
public class Solution {
           public int numberOfSubstrings(String s) {
               int count = 0;
               for (int i = 0; i < s.length(); i++) {
                   for (int j = i; j < s.length(); j++) {
                       int ones = 0, zeros = 0;
                       for (int k = i; k <= j; k++) {
                           if (s.charAt(k) == '1') ones++;
                           else zeros++;
                       }
                       if (ones >= zeros * zeros) count++;
                   }
               }
               return count;
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
           def numberOfSubstrings(self, s: str) -> int:
               count = 0
               for i in range(len(s)):
                   for j in range(i, len(s)):
                       ones = 0
                       zeros = 0
                       for k in range(i, j + 1):
                           if s[k] == '1':
                               ones += 1
                           else:
                               zeros += 1
                       if ones >= zeros * zeros:
                           count += 1
               return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
           def numberOfSubstrings(self, s: str) -> int:
               count = 0
               for i in range(len(s)):
                   for j in range(i, len(s)):
                       ones = 0
                       zeros = 0
                       for k in range(i, j + 1):
                           if s[k] == '1':
                               ones += 1
                           else:
                               zeros += 1
                       if ones >= zeros * zeros:
                           count += 1
               return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
       #include <string.h>

       int numberOfSubstrings(char * s){
           int count = 0;
           for (int i = 0; i < strlen(s); i++) {
               for (int j = i; j < strlen(s); j++) {
                   int ones = 0, zeros = 0;
                   for (int k = i; k <= j; k++) {
                       if (s[k] == '1') ones++;
                       else zeros++;
                   }
                   if (ones >= zeros * zeros) count++;
               }
           }
           return count;
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
           public int NumberOfSubstrings(string s) {
               int count = 0;
               for (int i = 0; i < s.Length; i++) {
                   for (int j = i; j < s.Length; j++) {
                       int ones = 0, zeros = 0;
                       for (int k = i; k <= j; k++) {
                           if (s[k] == '1') ones++;
                           else zeros++;
                       }
                       if (ones >= zeros * zeros) count++;
                   }
               }
               return count;
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var numberOfSubstrings = function(s) {
           let count = 0;
           for (let i = 0; i < s.length; i++) {
               for (let j = i; j < s.length; j++) {
                   let ones = 0, zeros = 0;
                   for (let k = i; k <= j; k++) {
                       if (s[k] == '1') ones++;
                       else zeros++;
                   }
                   if (ones >= zeros * zeros) count++;
               }
           }
           return count;
       };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfSubstrings(s: string): number {
           let count: number = 0;
           for (let i: number = 0; i < s.length; i++) {
               for (let j: number = i; j < s.length; j++) {
                   let ones: number = 0, zeros: number = 0;
                   for (let k: number = i; k <= j; k++) {
                       if (s[k] == '1') ones++;
                       else zeros++;
                   }
                   if (ones >= zeros * zeros) count++;
               }
           }
           return count;
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
           function numberOfSubstrings($s) {
               $count = 0;
               for ($i = 0; $i < strlen($s); $i++) {
                   for ($j = $i; $j < strlen($s); $j++) {
                       $ones = 0; $zeros = 0;
                       for ($k = $i; $k <= $j; $k++) {
                           if ($s[$k] == '1') $ones++;
                           else $zeros++;
                       }
                       if ($ones >= $zeros * $zeros) $count++;
                   }
               }
               return $count;
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
           func numberOfSubstrings(_ s: String) -> Int {
               var count = 0
               for i in 0..<s.count {
                   for j in i..<s.count {
                       var ones = 0
                       var zeros = 0
                       for k in i...j {
                           if s[s.index(s.startIndex, offsetBy: k)] == "1" {
                               ones += 1
                           } else {
                               zeros += 1
                           }
                       }
                       if ones >= zeros * zeros {
                           count += 1
                       }
                   }
               }
               return count
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
           fun numberOfSubstrings(s: String): Int {
               var count = 0
               for (i in 0 until s.length) {
                   for (j in i until s.length) {
                       var ones = 0
                       var zeros = 0
                       for (k in i..j) {
                           if (s[k] == '1') ones++
                           else zeros++
                       }
                       if (ones >= zeros * zeros) count++
                   }
               }
               return count
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
           int numberOfSubstrings(String s) {
               int count = 0;
               for (int i = 0; i < s.length; i++) {
                   for (int j = i; j < s.length; j++) {
                       int ones = 0, zeros = 0;
                       for (int k = i; k <= j; k++) {
                           if (s[k] == '1') ones++;
                           else zeros++;
                       }
                       if (ones >= zeros * zeros) count++;
                   }
               }
               return count;
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

       import (
           "fmt"
       )

       func numberOfSubstrings(s string) int {
           count := 0
           for i := 0; i < len(s); i++ {
               for j := i; j < len(s); j++ {
                   ones, zeros := 0, 0
                   for k := i; k <= j; k++ {
                       if s[k] == '1' {
                           ones++
                       } else {
                           zeros++
                       }
                   }
                   if ones >= zeros * zeros {
                       count++
                   }
               }
           }
           return count
       }

       func main() {
           fmt.Println(numberOfSubstrings("00011"))
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
       # @return {Integer}
       def number_of_substrings(s)
           count = 0
           (0...s.length).each do |i|
               (i...s.length).each do |j|
                   ones = 0
                   zeros = 0
                   (i..j).each do |k|
                       if s[k] == '1'
                           ones += 1
                       else
                           zeros += 1
                       end
                   end
                   count += 1 if ones >= zeros * zeros
               end
           end
           count
       end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
           def numberOfSubstrings(s: String): Int = {
               var count = 0
               for (i <- 0 until s.length) {
                   for (j <- i until s.length) {
                       var ones = 0
                       var zeros = 0
                       for (k <- i to j) {
                           if (s(k) == '1') ones += 1
                           else zeros += 1
                       }
                       if (ones >= zeros * zeros) count += 1
                   }
               }
               count
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
           pub fn number_of_substrings(s: String) -> i32 {
               let mut count = 0;
               for i in 0..s.len() {
                   for j in i..s.len() {
                       let mut ones = 0;
                       let mut zeros = 0;
                       for k in i..=j {
                           if s.as_bytes()[k] == b'1' {
                               ones += 1;
                           } else {
                               zeros += 1;
                           }
                       }
                       if ones >= zeros * zeros {
                           count += 1;
                       }
                   }
               }
               count
           }
       }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
       (define (number-of-substrings s)
           (let loop ([i 0] [count 0])
             (if (= i (string-length s))
                 count
                 (let loop2 ([j i] [count count])
                   (if (= j (string-length s))
                       (loop (+ i 1) count)
                       (let ([ones 0] [zeros 0])
                         (for ([k (in-range i (+ j 1))])
                           (if (eq? (string-ref s k) #\1)
                               (set! ones (+ ones 1))
                               (set! zeros (+ zeros 1))))
                         (if (>= ones (* zeros zeros))
                             (loop2 (+ j 1) (+ count 1))
                             (loop2 (+ j 1) count))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
       -export([number_of_substrings/1]).

       number_of_substrings(S) ->
           Count = count_substrings(S, 0, 0),
           Count.

       count_substrings(S, I, Count) when I >= length(S) ->
           Count;
       count_substrings(S, I, Count) ->
           Count2 = count_substrings2(S, I, I, Count),
           count_substrings(S, I + 1, Count2).

       count_substrings2(S, I, J, Count) when J >= length(S) ->
           Count;
       count_substrings2(S, I, J, Count) ->
           {Ones, Zeros} = count_ones_zeros(S, I, J),
           Count2 = if Ones >= Zeros * Zeros -> Count + 1;
                       true -> Count
                   end,
           count_substrings2(S, I, J + 1, Count2).

       count_ones_zeros(S, I, J) ->
           count_ones_zeros(S, I, J, 0, 0).

       count_ones_zeros(S, I, J, Ones, Zeros) when I > J ->
           {Ones, Zeros};
       count_ones_zeros(S, I, J, Ones, Zeros) ->
           case lists:nth(I + 1, S) of
               $1 -> count_ones_zeros(S, I + 1, J, Ones + 1, Zeros);
               $0 -> count_ones_zeros(S, I + 1, J, Ones, Zeros + 1)
           end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
           def number_of_substrings(s) do
               count = 0
               for i <- 0..String.length(s) - 1 do
                   for j <- i..String.length(s) - 1 do
                       ones = 0
                       zeros = 0
                       for k <- i..j do
                           if String.at(s, k) == "1" do
                               ones = ones + 1
                           else
                               zeros = zeros + 1
                           end
                       end
                       if ones >= zeros * zeros do
                           count = count + 1
                       end
                   end
               end
               count
           end
       end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^3)

- **Space Complexity:** O(1)

</div>
</details>
