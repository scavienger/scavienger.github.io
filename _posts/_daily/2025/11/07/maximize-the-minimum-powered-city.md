---
layout: post
title: "Maximize the Minimum Powered City"
date: 2025-11-07 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search", "Greedy", "Queue", "Sliding Window", "Prefix Sum"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximize-the-minimum-powered-city/
---

## Problem #2528: Maximize the Minimum Powered City

**Difficulty:** Hard

**Topics:** Array, Binary Search, Greedy, Queue, Sliding Window, Prefix Sum

## Problem Description

<p>You are given a <strong>0-indexed</strong> integer array <code>stations</code> of length <code>n</code>, where <code>stations[i]</code> represents the number of power stations in the <code>i<sup>th</sup></code> city.</p>

<p>Each power station can provide power to every city in a fixed <strong>range</strong>. In other words, if the range is denoted by <code>r</code>, then a power station at city <code>i</code> can provide power to all cities <code>j</code> such that <code>|i - j| &lt;= r</code> and <code>0 &lt;= i, j &lt;= n - 1</code>.</p>

<ul>
	<li>Note that <code>|x|</code> denotes <strong>absolute</strong> value. For example, <code>|7 - 5| = 2</code> and <code>|3 - 10| = 7</code>.</li>
</ul>

<p>The <strong>power</strong> of a city is the total number of power stations it is being provided power from.</p>

<p>The government has sanctioned building <code>k</code> more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.</p>

<p>Given the two integers <code>r</code> and <code>k</code>, return <em>the <strong>maximum possible minimum power</strong> of a city, if the additional power stations are built optimally.</em></p>

<p><strong>Note</strong> that you can build the <code>k</code> power stations in multiple cities.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stations = [1,2,4,5,0], r = 1, k = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
One of the optimal ways is to install both the power stations at city 1. 
So stations will become [1,4,4,5,0].
- City 0 is provided by 1 + 4 = 5 power stations.
- City 1 is provided by 1 + 4 + 4 = 9 power stations.
- City 2 is provided by 4 + 4 + 5 = 13 power stations.
- City 3 is provided by 5 + 4 = 9 power stations.
- City 4 is provided by 5 + 0 = 5 power stations.
So the minimum power of a city is 5.
Since it is not possible to obtain a larger power, we return 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stations = [4,4,4,4], r = 0, k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
It can be proved that we cannot make the minimum power of a city greater than 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == stations.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= stations[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= r&nbsp;&lt;= n - 1</code></li>
	<li><code>0 &lt;= k&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Pre calculate the number of stations on each city using Line Sweep.

2. Use binary search to maximize the minimum.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-23 00:00:21 )</small>
</summary>

<div class="ai-solution-content">

### Approach

This problem is solved using binary search on the answer (the maximum possible minimum power). The `check` function determines if a given `target_min_power` is achievable. Inside `check`, we first calculate the initial power for each city using a difference array (line sweep). Then, we iterate through cities, greedily adding power stations at `i+r` if city `i`'s current power is below `target_min_power`, updating `k` and power contributions using another difference array.

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
#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    bool check(long long target_min_power, int n, int r, long long k, const std::vector<int>& stations) {
        std::vector<long long> initial_power(n);
        std::vector<long long> diff_initial(n + 1, 0);

        for (int idx = 0; idx < n; ++idx) {
            int left_bound = std::max(0, idx - r);
            int right_bound = std::min(n - 1, idx + r);
            diff_initial[left_bound] += stations[idx];
            diff_initial[right_bound + 1] -= stations[idx];
        }

        long long current_sum_initial = 0;
        for (int i = 0; i < n; ++i) {
            current_sum_initial += diff_initial[i];
            initial_power[i] = current_sum_initial;
        }

        long long k_remaining = k;
        std::vector<long long> diff_added_power_contribution(n + 1, 0);
        long long current_added_power_sum = 0;

        for (int i = 0; i < n; ++i) {
            current_added_power_sum += diff_added_power_contribution[i];
            long long total_power_at_i = initial_power[i] + current_added_power_sum;

            if (total_power_at_i < target_min_power) {
                long long needed = target_min_power - total_power_at_i;
                k_remaining -= needed;
                if (k_remaining < 0) {
                    return false;
                }

                diff_added_power_contribution[i] += needed;
                int end_idx_for_contribution = std::min(n - 1, i + 2 * r);
                if (end_idx_for_contribution + 1 < n + 1) {
                    diff_added_power_contribution[end_idx_for_contribution + 1] -= needed;
                }
                current_added_power_sum += needed;
            }
        }
        return true;
    }

    long long maxPower(std::vector<int>& stations, int r, long long k) {
        int n = stations.size();

        long long low = 0;
        long long high = 2e10 + 1e9 + 7; // Max possible power for a city

        long long ans = 0;
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (check(mid, n, r, k, stations)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public long maxPower(int[] stations, int r, long k) {
        int n = stations.length;

        long low = 0;
        long high = 2L * (long)1e10 + (long)1e9 + 7; // Max possible power for a city

        long ans = 0;
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (check(mid, n, r, k, stations)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }

    private boolean check(long target_min_power, int n, int r, long k_initial, int[] stations) {
        long[] initial_power = new long[n];
        long[] diff_initial = new long[n + 1];

        for (int idx = 0; idx < n; ++idx) {
            int left_bound = Math.max(0, idx - r);
            int right_bound = Math.min(n - 1, idx + r);
            diff_initial[left_bound] += stations[idx];
            diff_initial[right_bound + 1] -= stations[idx];
        }

        long current_sum_initial = 0;
        for (int i = 0; i < n; ++i) {
            current_sum_initial += diff_initial[i];
            initial_power[i] = current_sum_initial;
        }

        long k_remaining = k_initial;
        long[] diff_added_power_contribution = new long[n + 1];
        long current_added_power_sum = 0;

        for (int i = 0; i < n; ++i) {
            current_added_power_sum += diff_added_power_contribution[i];
            long total_power_at_i = initial_power[i] + current_added_power_sum;

            if (total_power_at_i < target_min_power) {
                long needed = target_min_power - total_power_at_i;
                k_remaining -= needed;
                if (k_remaining < 0) {
                    return false;
                }

                diff_added_power_contribution[i] += needed;
                int end_idx_for_contribution = Math.min(n - 1, i + 2 * r);
                if (end_idx_for_contribution + 1 < n + 1) {
                    diff_added_power_contribution[end_idx_for_contribution + 1] -= needed;
                }
                current_added_power_sum += needed;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        def check(target_min_power: int) -> bool:
            initial_power = [0] * n
            diff_initial = [0] * (n + 1)
            for idx in range(n):
                left_bound = max(0, idx - r)
                right_bound = min(n - 1, idx + r)
                diff_initial[left_bound] += stations[idx]
                diff_initial[right_bound + 1] -= stations[idx]

            current_sum_initial = 0
            for i in range(n):
                current_sum_initial += diff_initial[i]
                initial_power[i] = current_sum_initial

            k_remaining = k
            diff_added_power_contribution = [0] * (n + 1)
            current_added_power_sum = 0

            for i in range(n):
                current_added_power_sum += diff_added_power_contribution[i]
                total_power_at_i = initial_power[i] + current_added_power_sum

                if total_power_at_i < target_min_power:
                    needed = target_min_power - total_power_at_i
                    k_remaining -= needed
                    if k_remaining < 0:
                        return False

                    diff_added_power_contribution[i] += needed
                    end_idx_for_contribution = min(n - 1, i + 2 * r)
                    if end_idx_for_contribution + 1 < n + 1:
                        diff_added_power_contribution[end_idx_for_contribution + 1] -= needed

                    current_added_power_sum += needed

            return True

        low = 0
        high = 2 * 10**10 + 10**9 + 7 # A safe upper bound for max possible power

        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        def check(target_min_power: int) -> bool:
            initial_power = [0] * n
            diff_initial = [0] * (n + 1)
            for idx in range(n):
                left_bound = max(0, idx - r)
                right_bound = min(n - 1, idx + r)
                diff_initial[left_bound] += stations[idx]
                diff_initial[right_bound + 1] -= stations[idx]

            current_sum_initial = 0
            for i in range(n):
                current_sum_initial += diff_initial[i]
                initial_power[i] = current_sum_initial

            k_remaining = k
            diff_added_power_contribution = [0] * (n + 1)
            current_added_power_sum = 0

            for i in range(n):
                current_added_power_sum += diff_added_power_contribution[i]
                total_power_at_i = initial_power[i] + current_added_power_sum

                if total_power_at_i < target_min_power:
                    needed = target_min_power - total_power_at_i
                    k_remaining -= needed
                    if k_remaining < 0:
                        return False

                    diff_added_power_contribution[i] += needed
                    end_idx_for_contribution = min(n - 1, i + 2 * r)
                    if end_idx_for_contribution + 1 < n + 1:
                        diff_added_power_contribution[end_idx_for_contribution + 1] -= needed

                    current_added_power_sum += needed

            return True

        low = 0
        high = 2 * 10**10 + 10**9 + 7 # A safe upper bound for max possible power

        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>

// Helper function for max and min
long long max_ll(long long a, long long b) { return a > b ? a : b; }
long long min_ll(long long a, long long b) { return a < b ? a : b; }
int max_int(int a, int b) { return a > b ? a : b; }
int min_int(int a, int b) { return a < b ? a : b; }

bool check(long long target_min_power, int n, int r, long long k_initial, int* stations) {
    long long* initial_power = (long long*)calloc(n, sizeof(long long));
    long long* diff_initial = (long long*)calloc(n + 1, sizeof(long long));

    for (int idx = 0; idx < n; ++idx) {
        int left_bound = max_int(0, idx - r);
        int right_bound = min_int(n - 1, idx + r);
        diff_initial[left_bound] += stations[idx];
        diff_initial[right_bound + 1] -= stations[idx];
    }

    long long current_sum_initial = 0;
    for (int i = 0; i < n; ++i) {
        current_sum_initial += diff_initial[i];
        initial_power[i] = current_sum_initial;
    }

    long long k_remaining = k_initial;
    long long* diff_added_power_contribution = (long long*)calloc(n + 1, sizeof(long long));
    long long current_added_power_sum = 0;

    for (int i = 0; i < n; ++i) {
        current_added_power_sum += diff_added_power_contribution[i];
        long long total_power_at_i = initial_power[i] + current_added_power_sum;

        if (total_power_at_i < target_min_power) {
            long long needed = target_min_power - total_power_at_i;
            k_remaining -= needed;
            if (k_remaining < 0) {
                free(initial_power);
                free(diff_initial);
                free(diff_added_power_contribution);
                return false;
            }

            diff_added_power_contribution[i] += needed;
            int end_idx_for_contribution = min_int(n - 1, i + 2 * r);
            if (end_idx_for_contribution + 1 < n + 1) {
                diff_added_power_contribution[end_idx_for_contribution + 1] -= needed;
            }
            current_added_power_sum += needed;
        }
    }
    free(initial_power);
    free(diff_initial);
    free(diff_added_power_contribution);
    return true;
}

long long maxPower(int* stations, int stationsSize, int r, long long k) {
    int n = stationsSize;

    long long low = 0;
    long long high = 20000000000LL + 1000000000LL + 7; // Max possible power for a city

    long long ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, n, r, k, stations)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public long MaxPower(int[] stations, int r, long k) {
        int n = stations.Length;

        long low = 0;
        long high = 2L * (long)1e10 + (long)1e9 + 7; // Max possible power for a city

        long ans = 0;
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (Check(mid, n, r, k, stations)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }

    private bool Check(long target_min_power, int n, int r, long k_initial, int[] stations) {
        long[] initial_power = new long[n];
        long[] diff_initial = new long[n + 1];

        for (int idx = 0; idx < n; ++idx) {
            int left_bound = Math.Max(0, idx - r);
            int right_bound = Math.Min(n - 1, idx + r);
            diff_initial[left_bound] += stations[idx];
            diff_initial[right_bound + 1] -= stations[idx];
        }

        long current_sum_initial = 0;
        for (int i = 0; i < n; ++i) {
            current_sum_initial += diff_initial[i];
            initial_power[i] = current_sum_initial;
        }

        long k_remaining = k_initial;
        long[] diff_added_power_contribution = new long[n + 1];
        long current_added_power_sum = 0;

        for (int i = 0; i < n; ++i) {
            current_added_power_sum += diff_added_power_contribution[i];
            long total_power_at_i = initial_power[i] + current_added_power_sum;

            if (total_power_at_i < target_min_power) {
                long needed = target_min_power - total_power_at_i;
                k_remaining -= needed;
                if (k_remaining < 0) {
                    return false;
                }

                diff_added_power_contribution[i] += needed;
                int end_idx_for_contribution = Math.Min(n - 1, i + 2 * r);
                if (end_idx_for_contribution + 1 < n + 1) {
                    diff_added_power_contribution[end_idx_for_contribution + 1] -= needed;
                }
                current_added_power_sum += needed;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} stations
 * @param {number} r
 * @param {number} k
 * @return {number}
 */
var maxPower = function(stations, r, k) {
    const n = stations.length;

    const check = (target_min_power) => {
        const initial_power = new Array(n).fill(0);
        const diff_initial = new Array(n + 1).fill(0);

        for (let idx = 0; idx < n; ++idx) {
            const left_bound = Math.max(0, idx - r);
            const right_bound = Math.min(n - 1, idx + r);
            diff_initial[left_bound] += stations[idx];
            diff_initial[right_bound + 1] -= stations[idx];
        }

        let current_sum_initial = 0;
        for (let i = 0; i < n; ++i) {
            current_sum_initial += diff_initial[i];
            initial_power[i] = current_sum_initial;
        }

        let k_remaining = k;
        const diff_added_power_contribution = new Array(n + 1).fill(0);
        let current_added_power_sum = 0;

        for (let i = 0; i < n; ++i) {
            current_added_power_sum += diff_added_power_contribution[i];
            let total_power_at_i = initial_power[i] + current_added_power_sum;

            if (total_power_at_i < target_min_power) {
                const needed = target_min_power - total_power_at_i;
                k_remaining -= needed;
                if (k_remaining < 0) {
                    return false;
                }

                diff_added_power_contribution[i] += needed;
                const end_idx_for_contribution = Math.min(n - 1, i + 2 * r);
                if (end_idx_for_contribution + 1 < n + 1) {
                    diff_added_power_contribution[end_idx_for_contribution + 1] -= needed;
                }
                current_added_power_sum += needed;
            }
        }
        return true;
    };

    let low = 0;
    let high = 2 * 10**10 + 10**9 + 7; // Max possible power for a city

    let ans = 0;
    while (low <= high) {
        const mid = Math.floor(low + (high - low) / 2);
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxPower(stations: number[], r: number, k: number): number {
    const n = stations.length;

    const check = (target_min_power: number): boolean => {
        const initial_power: number[] = new Array(n).fill(0);
        const diff_initial: number[] = new Array(n + 1).fill(0);

        for (let idx = 0; idx < n; ++idx) {
            const left_bound = Math.max(0, idx - r);
            const right_bound = Math.min(n - 1, idx + r);
            diff_initial[left_bound] += stations[idx];
            diff_initial[right_bound + 1] -= stations[idx];
        }

        let current_sum_initial = 0;
        for (let i = 0; i < n; ++i) {
            current_sum_initial += diff_initial[i];
            initial_power[i] = current_sum_initial;
        }

        let k_remaining = k;
        const diff_added_power_contribution: number[] = new Array(n + 1).fill(0);
        let current_added_power_sum = 0;

        for (let i = 0; i < n; ++i) {
            current_added_power_sum += diff_added_power_contribution[i];
            let total_power_at_i = initial_power[i] + current_added_power_sum;

            if (total_power_at_i < target_min_power) {
                const needed = target_min_power - total_power_at_i;
                k_remaining -= needed;
                if (k_remaining < 0) {
                    return false;
                }

                diff_added_power_contribution[i] += needed;
                const end_idx_for_contribution = Math.min(n - 1, i + 2 * r);
                if (end_idx_for_contribution + 1 < n + 1) {
                    diff_added_power_contribution[end_idx_for_contribution + 1] -= needed;
                }
                current_added_power_sum += needed;
            }
        }
        return true;
    };

    let low = 0;
    let high = 2 * 10**10 + 10**9 + 7; // Max possible power for a city

    let ans = 0;
    while (low <= high) {
        const mid = Math.floor(low + (high - low) / 2);
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php

class Solution {

    /**
     * @param Integer[] $stations
     * @param Integer $r
     * @param Integer $k
     * @return Integer
     */
    function maxPower(array $stations, int $r, int $k): int {
        $n = count($stations);

        $check = function(int $target_min_power) use ($n, $r, $k, $stations): bool {
            $initial_power = array_fill(0, $n, 0);
            $diff_initial = array_fill(0, $n + 1, 0);

            for ($idx = 0; $idx < $n; ++$idx) {
                $left_bound = max(0, $idx - $r);
                $right_bound = min($n - 1, $idx + $r);
                $diff_initial[$left_bound] += $stations[$idx];
                $diff_initial[$right_bound + 1] -= $stations[$idx];
            }

            $current_sum_initial = 0;
            for ($i = 0; $i < $n; ++$i) {
                $current_sum_initial += $diff_initial[$i];
                $initial_power[$i] = $current_sum_initial;
            }

            $k_remaining = $k;
            $diff_added_power_contribution = array_fill(0, $n + 1, 0);
            $current_added_power_sum = 0;

            for ($i = 0; $i < $n; ++$i) {
                $current_added_power_sum += $diff_added_power_contribution[$i];
                $total_power_at_i = $initial_power[$i] + $current_added_power_sum;

                if ($total_power_at_i < $target_min_power) {
                    $needed = $target_min_power - $total_power_at_i;
                    $k_remaining -= $needed;
                    if ($k_remaining < 0) {
                        return false;
                    }

                    $diff_added_power_contribution[$i] += $needed;
                    $end_idx_for_contribution = min($n - 1, $i + 2 * $r);
                    if ($end_idx_for_contribution + 1 < $n + 1) {
                        $diff_added_power_contribution[$end_idx_for_contribution + 1] -= $needed;
                    }
                    $current_added_power_sum += $needed;
                }
            }
            return true;
        };

        $low = 0;
        $high = 2 * 10**10 + 10**9 + 7; // Max possible power for a city

        $ans = 0;
        while ($low <= $high) {
            $mid = floor($low + ($high - $low) / 2);
            if ($check($mid)) {
                $ans = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }
        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func maxPower(_ stations: [Int], _ r: Int, _ k: Int) -> Int {
        let n = stations.count

        func check(_ target_min_power: Int) -> Bool {
            var initial_power = Array(repeating: 0, count: n)
            var diff_initial = Array(repeating: 0, count: n + 1)

            for idx in 0..<n {
                let left_bound = max(0, idx - r)
                let right_bound = min(n - 1, idx + r)
                diff_initial[left_bound] += stations[idx]
                diff_initial[right_bound + 1] -= stations[idx]
            }

            var current_sum_initial = 0
            for i in 0..<n {
                current_sum_initial += diff_initial[i]
                initial_power[i] = current_sum_initial
            }

            var k_remaining = k
            var diff_added_power_contribution = Array(repeating: 0, count: n + 1)
            var current_added_power_sum = 0

            for i in 0..<n {
                current_added_power_sum += diff_added_power_contribution[i]
                let total_power_at_i = initial_power[i] + current_added_power_sum

                if total_power_at_i < target_min_power {
                    let needed = target_min_power - total_power_at_i
                    k_remaining -= needed
                    if k_remaining < 0 {
                        return false
                    }

                    diff_added_power_contribution[i] += needed
                    let end_idx_for_contribution = min(n - 1, i + 2 * r)
                    if end_idx_for_contribution + 1 < n + 1 {
                        diff_added_power_contribution[end_idx_for_contribution + 1] -= needed
                    }
                    current_added_power_sum += needed
                }
            }
            return true
        }

        var low = 0
        var high = 2 * 10_000_000_000 + 1_000_000_000 + 7 // Max possible power for a city

        var ans = 0
        while low <= high {
            let mid = low + (high - low) / 2
            if check(mid) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.max
import kotlin.math.min

class Solution {
    fun maxPower(stations: IntArray, r: Int, k: Long): Long {
        val n = stations.size

        fun check(target_min_power: Long): Boolean {
            val initial_power = LongArray(n) { 0L }
            val diff_initial = LongArray(n + 1) { 0L }

            for (idx in 0 until n) {
                val left_bound = max(0, idx - r)
                val right_bound = min(n - 1, idx + r)
                diff_initial[left_bound] += stations[idx]
                diff_initial[right_bound + 1] -= stations[idx]
            }

            var current_sum_initial = 0L
            for (i in 0 until n) {
                current_sum_initial += diff_initial[i]
                initial_power[i] = current_sum_initial
            }

            var k_remaining = k
            val diff_added_power_contribution = LongArray(n + 1) { 0L }
            var current_added_power_sum = 0L

            for (i in 0 until n) {
                current_added_power_sum += diff_added_power_contribution[i]
                val total_power_at_i = initial_power[i] + current_added_power_sum

                if (total_power_at_i < target_min_power) {
                    val needed = target_min_power - total_power_at_i
                    k_remaining -= needed
                    if (k_remaining < 0) {
                        return false
                    }

                    diff_added_power_contribution[i] += needed
                    val end_idx_for_contribution = min(n - 1, i + 2 * r)
                    if (end_idx_for_contribution + 1 < n + 1) {
                        diff_added_power_contribution[end_idx_for_contribution + 1] -= needed
                    }
                    current_added_power_sum += needed
                }
            }
            return true
        }

        var low = 0L
        var high = 2L * 10_000_000_000L + 1_000_000_000L + 7L // Max possible power for a city

        var ans = 0L
        while (low <= high) {
            val mid = low + (high - low) / 2
            if (check(mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return ans
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
  int maxPower(List<int> stations, int r, int k) {
    final n = stations.length;

    bool check(int targetMinPower) {
      final initialPower = List<int>.filled(n, 0);
      final diffInitial = List<int>.filled(n + 1, 0);

      for (int idx = 0; idx < n; ++idx) {
        final leftBound = max(0, idx - r);
        final rightBound = min(n - 1, idx + r);
        diffInitial[leftBound] += stations[idx];
        diffInitial[rightBound + 1] -= stations[idx];
      }

      int currentSumInitial = 0;
      for (int i = 0; i < n; ++i) {
        currentSumInitial += diffInitial[i];
        initialPower[i] = currentSumInitial;
      }

      int kRemaining = k;
      final diffAddedPowerContribution = List<int>.filled(n + 1, 0);
      int currentAddedPowerSum = 0;

      for (int i = 0; i < n; ++i) {
        currentAddedPowerSum += diffAddedPowerContribution[i];
        int totalPowerAtI = initialPower[i] + currentAddedPowerSum;

        if (totalPowerAtI < targetMinPower) {
          final needed = targetMinPower - totalPowerAtI;
          kRemaining -= needed;
          if (kRemaining < 0) {
            return false;
          }

          diffAddedPowerContribution[i] += needed;
          final endIdxForContribution = min(n - 1, i + 2 * r);
          if (endIdxForContribution + 1 < n + 1) {
            diffAddedPowerContribution[endIdxForContribution + 1] -= needed;
          }
          currentAddedPowerSum += needed;
        }
      }
      return true;
    }

    int low = 0;
    // Dart's int type can handle large numbers up to 2^63 - 1 on 64-bit platforms.
    // 2 * 10^10 + 10^9 + 7 is within this range.
    int high = 2 * pow(10, 10).toInt() + pow(10, 9).toInt() + 7;

    int ans = 0;
    while (low <= high) {
      final mid = low + (high - low) ~/ 2;
      if (check(mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return ans;
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
	"math"
)

func maxPower(stations []int, r int, k int) int {
    n := len(stations)

    check := func(targetMinPower int) bool {
        initialPower := make([]int, n)
        diffInitial := make([]int, n + 1)

        for idx := 0; idx < n; idx++ {
            leftBound := int(math.Max(float64(0), float64(idx - r)))
            rightBound := int(math.Min(float64(n - 1), float64(idx + r)))
            diffInitial[leftBound] += stations[idx]
            diffInitial[rightBound + 1] -= stations[idx]
        }

        currentSumInitial := 0
        for i := 0; i < n; i++ {
            currentSumInitial += diffInitial[i]
            initialPower[i] = currentSumInitial
        }

        kRemaining := k
        diffAddedPowerContribution := make([]int, n + 1)
        currentAddedPowerSum := 0

        for i := 0; i < n; i++ {
            currentAddedPowerSum += diffAddedPowerContribution[i]
            totalPowerAtI := initialPower[i] + currentAddedPowerSum

            if totalPowerAtI < targetMinPower {
                needed := targetMinPower - totalPowerAtI
                kRemaining -= needed
                if kRemaining < 0 {
                    return false
                }

                diffAddedPowerContribution[i] += needed;
                endIdxForContribution := int(math.Min(float64(n - 1), float64(i + 2 * r)))
                if endIdxForContribution + 1 < n + 1 {
                    diffAddedPowerContribution[endIdxForContribution + 1] -= needed;
                }
                currentAddedPowerSum += needed;
            }
        }
        return true
    }

    low := 0
    // Go's int type is usually 32-bit or 64-bit depending on the system.
    // For competitive programming, it's often 64-bit on typical platforms.
    // However, to be safe with large numbers, we should use int64 for powers and k.
    // The problem statement implies k is int, but it can be 10^9. stations[i] is int.
    // Sums can exceed int32. Let's assume int is 64-bit for now, or use int64 explicitly.
    // LeetCode Go environment typically uses 64-bit int for `int` type.
    high := 2 * int(math.Pow10(10)) + int(math.Pow10(9)) + 7 // Max possible power for a city

    ans := 0
    for low <= high {
        mid := low + (high - low) / 2
        if check(mid) {
            ans = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} stations
# @param {Integer} r
# @param {Integer} k
# @return {Integer}
def max_power(stations, r, k)
    n = stations.length

    check = ->(target_min_power) do
        initial_power = Array.new(n, 0)
        diff_initial = Array.new(n + 1, 0)

        stations.each_with_index do |s_val, idx|
            left_bound = [0, idx - r].max
            right_bound = [n - 1, idx + r].min
            diff_initial[left_bound] += s_val
            diff_initial[right_bound + 1] -= s_val
        end

        current_sum_initial = 0
        n.times do |i|
            current_sum_initial += diff_initial[i]
            initial_power[i] = current_sum_initial
        end

        k_remaining = k
        diff_added_power_contribution = Array.new(n + 1, 0)
        current_added_power_sum = 0

        n.times do |i|
            current_added_power_sum += diff_added_power_contribution[i]
            total_power_at_i = initial_power[i] + current_added_power_sum

            if total_power_at_i < target_min_power
                needed = target_min_power - total_power_at_i
                k_remaining -= needed
                return false if k_remaining < 0

                diff_added_power_contribution[i] += needed
                end_idx_for_contribution = [n - 1, i + 2 * r].min
                if end_idx_for_contribution + 1 < n + 1
                    diff_added_power_contribution[end_idx_for_contribution + 1] -= needed
                end
                current_added_power_sum += needed
            end
        end
        true
    end

    low = 0
    high = 2 * (10**10) + (10**9) + 7 # Max possible power for a city

    ans = 0
    while low <= high
        mid = low + (high - low) / 2
        if check.call(mid)
            ans = mid
            low = mid + 1
        else
            high = mid - 1
        end
    end
    ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer
import scala.math.{max, min}

object Solution {
    def maxPower(stations: Array[Int], r: Int, k: Long): Long = {
        val n = stations.length

        def check(target_min_power: Long): Boolean = {
            val initial_power = Array.ofDim[Long](n)
            val diff_initial = Array.ofDim[Long](n + 1)

            for (idx <- 0 until n) {
                val left_bound = max(0, idx - r)
                val right_bound = min(n - 1, idx + r)
                diff_initial(left_bound) += stations(idx)
                diff_initial(right_bound + 1) -= stations(idx)
            }

            var current_sum_initial = 0L
            for (i <- 0 until n) {
                current_sum_initial += diff_initial(i)
                initial_power(i) = current_sum_initial
            }

            var k_remaining = k
            val diff_added_power_contribution = Array.ofDim[Long](n + 1)
            var current_added_power_sum = 0L

            for (i <- 0 until n) {
                current_added_power_sum += diff_added_power_contribution(i)
                val total_power_at_i = initial_power(i) + current_added_power_sum

                if (total_power_at_i < target_min_power) {
                    val needed = target_min_power - total_power_at_i
                    k_remaining -= needed
                    if (k_remaining < 0) {
                        return false
                    }

                    diff_added_power_contribution(i) += needed
                    val end_idx_for_contribution = min(n - 1, i + 2 * r)
                    if (end_idx_for_contribution + 1 < n + 1) {
                        diff_added_power_contribution(end_idx_for_contribution + 1) -= needed
                    }
                    current_added_power_sum += needed
                }
            }
            true
        }

        var low = 0L
        var high = 2L * 10_000_000_000L + 1_000_000_000L + 7L // Max possible power for a city

        var ans = 0L
        while (low <= high) {
            val mid = low + (high - low) / 2
            if (check(mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::cmp::{max, min};

impl Solution {
    pub fn max_power(stations: Vec<i32>, r: i32, k: i64) -> i64 {
        let n = stations.len();

        let check = |target_min_power: i64| -> bool {
            let mut initial_power = vec![0i64; n];
            let mut diff_initial = vec![0i64; n + 1];

            for (idx, &s_val) in stations.iter().enumerate() {
                let left_bound = max(0, idx as i32 - r) as usize;
                let right_bound = min(n as i32 - 1, idx as i32 + r) as usize;
                diff_initial[left_bound] += s_val as i64;
                diff_initial[right_bound + 1] -= s_val as i64;
            }

            let mut current_sum_initial = 0i64;
            for i in 0..n {
                current_sum_initial += diff_initial[i];
                initial_power[i] = current_sum_initial;
            }

            let mut k_remaining = k;
            let mut diff_added_power_contribution = vec![0i64; n + 1];
            let mut current_added_power_sum = 0i64;

            for i in 0..n {
                current_added_power_sum += diff_added_power_contribution[i];
                let total_power_at_i = initial_power[i] + current_added_power_sum;

                if total_power_at_i < target_min_power {
                    let needed = target_min_power - total_power_at_i;
                    k_remaining -= needed;
                    if k_remaining < 0 {
                        return false;
                    }

                    diff_added_power_contribution[i] += needed;
                    let end_idx_for_contribution = min(n as i32 - 1, i as i32 + 2 * r) as usize;
                    if end_idx_for_contribution + 1 < n + 1 {
                        diff_added_power_contribution[end_idx_for_contribution + 1] -= needed;
                    }
                    current_added_power_sum += needed;
                }
            }
            true
        };

        let mut low = 0i64;
        let mut high = 2 * 10_i64.pow(10) + 10_i64.pow(9) + 7; // Max possible power for a city

        let mut ans = 0i64;
        while low <= high {
            let mid = low + (high - low) / 2;
            if check(mid) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (max-power stations r k)
  (define n (vector-length stations))

  (define (check target-min-power)
    (define initial-power (make-vector n 0))
    (define diff-initial (make-vector (+ n 1) 0))

    (for ([idx (in-range n)])
      (define left-bound (max 0 (- idx r)))
      (define right-bound (min (- n 1) (+ idx r)))
      (vector-set! diff-initial left-bound (+ (vector-ref diff-initial left-bound) (vector-ref stations idx)))
      (vector-set! diff-initial (+ right-bound 1) (- (vector-ref diff-initial (+ right-bound 1)) (vector-ref stations idx))))

    (define current-sum-initial (make-box 0))
    (for ([i (in-range n)])
      (set-box! current-sum-initial (+ (unbox current-sum-initial) (vector-ref diff-initial i)))
      (vector-set! initial-power i (unbox current-sum-initial)))

    (define k-remaining (make-box k))
    (define diff-added-power-contribution (make-vector (+ n 1) 0))
    (define current-added-power-sum (make-box 0))

    (for ([i (in-range n)])
      (set-box! current-added-power-sum (+ (unbox current-added-power-sum) (vector-ref diff-added-power-contribution i)))
      (define total-power-at-i (+ (vector-ref initial-power i) (unbox current-added-power-sum)))

      (when (< total-power-at-i target-min-power)
        (define needed (- target-min-power total-power-at-i))
        (set-box! k-remaining (- (unbox k-remaining) needed))
        (when (< (unbox k-remaining) 0)
          (error 'check "k_remaining became negative")) ; This should be handled by returning #f

        (vector-set! diff-added-power-contribution i (+ (vector-ref diff-added-power-contribution i) needed))
        (define end-idx-for-contribution (min (- n 1) (+ i (* 2 r))))
        (when (< (+ end-idx-for-contribution 1) (+ n 1))
          (vector-set! diff-added-power-contribution (+ end-idx-for-contribution 1) (- (vector-ref diff-added-power-contribution (+ end-idx-for-contribution 1)) needed)))
        (set-box! current-added-power-sum (+ (unbox current-added-power-sum) needed))))

    (>= (unbox k-remaining) 0))

  (define low 0)
  (define high (+ (* 2 (expt 10 10)) (expt 10 9) 7)) ; Max possible power for a city

  (define ans 0)
  (let loop ([l low] [h high] [a ans])
    (if (<= l h)
        (let ([mid (+ l (quotient (- h l) 2))])
          (if (check mid)
              (loop (+ mid 1) h mid)
              (loop l (- mid 1) a)))
        a)))

(provide (rename-out [max-power Solution-maxPower]))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([max_power/3]).

max_power(Stations, R, K) ->
    N = length(Stations),

    Check = fun(TargetMinPower) ->
        InitialPower = array:new(N, {default, 0}),
        DiffInitial = array:new(N + 1, {default, 0}),

        lists:foldl(fun(Idx, AccDiffInitial) ->
            StationVal = lists:nth(Idx + 1, Stations),
            LeftBound = max(0, Idx - R),
            RightBound = min(N - 1, Idx + R),
            AccDiffInitial1 = array:set(LeftBound, array:get(LeftBound, AccDiffInitial) + StationVal, AccDiffInitial),
            array:set(RightBound + 1, array:get(RightBound + 1, AccDiffInitial1) - StationVal, AccDiffInitial1)
        end, DiffInitial, lists:seq(0, N - 1)),

        CurrentSumInitial = {0},
        InitialPowerFinal = lists:foldl(fun(I, AccInitialPower) ->
            CurrentSum = element(1, CurrentSumInitial) + array:get(I, DiffInitial),
            element(1, CurrentSumInitial, CurrentSum),
            array:set(I, CurrentSum, AccInitialPower)
        end, InitialPower, lists:seq(0, N - 1)),

        KRemaining = {K},
        DiffAddedPowerContribution = array:new(N + 1, {default, 0}),
        CurrentAddedPowerSum = {0},

        lists:foldl(fun(I, AccDiffAdded) ->
            CurrentAddedSum = element(1, CurrentAddedPowerSum) + array:get(I, AccDiffAdded),
            element(1, CurrentAddedPowerSum, CurrentAddedSum),
            TotalPowerAtI = array:get(I, InitialPowerFinal) + CurrentAddedSum,

            if TotalPowerAtI < TargetMinPower ->
                Needed = TargetMinPower - TotalPowerAtI,
                KR = element(1, KRemaining) - Needed,
                element(1, KRemaining, KR),
                if KR < 0 ->
                    throw(false) % Use throw to exit early
                else
                    AccDiffAdded1 = array:set(I, array:get(I, AccDiffAdded) + Needed, AccDiffAdded),
                    EndIdxForContribution = min(N - 1, I + 2 * R),
                    if EndIdxForContribution + 1 < N + 1 ->
                        array:set(EndIdxForContribution + 1, array:get(EndIdxForContribution + 1, AccDiffAdded1) - Needed, AccDiffAdded1)
                    else
                        AccDiffAdded1
                    end
                end;
            true ->
                AccDiffAdded
            end
        end, DiffAddedPowerContribution, lists:seq(0, N - 1)),

        element(1, KRemaining) >= 0
    end,

    Low = 0,
    High = 2 * 10000000000 + 1000000000 + 7, % Max possible power for a city

    Ans = 0,
    try
        binary_search(Low, High, Ans, Check)
    catch
        throw:false -> 0 % If check throws false, it means 0 is the answer or something went wrong.
                        % This needs to be handled carefully. The binary search should return the last true.
                        % Re-implementing binary search to handle throw.
    end.

% Helper for binary search
binary_search(Low, High, Ans, Check) when Low =< High ->
    Mid = Low + (High - Low) div 2,
    try
        if Check(Mid) ->
            binary_search(Mid + 1, High, Mid, Check)
        else
            binary_search(Low, Mid - 1, Ans, Check)
        end
    catch
        throw:false -> % If check(Mid) throws false, it means Mid is not achievable.
                       % We need to search in the lower half.
            binary_search(Low, Mid - 1, Ans, Check)
    end;
binary_search(_, _, Ans, _) ->
    Ans.

% Helper functions for min/max (Erlang has built-in min/max, but for clarity)
min(A, B) when A < B -> A;
min(A, B) -> B.

max(A, B) when A > B -> A;
max(A, B) -> B.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_power(stations :: [integer], r :: integer, k :: integer) :: integer
  def max_power(stations, r, k) do
    n = length(stations)

    check = fn target_min_power ->
      initial_power = :array.new(n, [{:default, 0}])
      diff_initial = :array.new(n + 1, [{:default, 0}])

      diff_initial = Enum.reduce(0..(n - 1), diff_initial, fn idx, acc_diff_initial ->
        station_val = Enum.at(stations, idx)
        left_bound = max(0, idx - r)
        right_bound = min(n - 1, idx + r)
        acc_diff_initial
        |> :array.set(left_bound, :array.get(left_bound, acc_diff_initial) + station_val)
        |> :array.set(right_bound + 1, :array.get(right_bound + 1, acc_diff_initial) - station_val)
      end)

      {_current_sum_initial, initial_power_final} = Enum.reduce(0..(n - 1), {0, initial_power}, fn i, {acc_sum, acc_initial_power} ->
        new_sum = acc_sum + :array.get(i, diff_initial)
        {new_sum, :array.set(i, new_sum, acc_initial_power)}
      end)

      {_final_k_remaining, _final_diff_added_power_contribution, _final_current_added_power_sum, possible} = Enum.reduce_while(0..(n - 1), {k, :array.new(n + 1, [{:default, 0}]), 0, true}, fn i, {kr_acc, dac_acc, cas_acc, p_acc} ->
        new_cas_acc = cas_acc + :array.get(i, dac_acc)
        total_power_at_i = :array.get(i, initial_power_final) + new_cas_acc

        if total_power_at_i < target_min_power do
          needed = target_min_power - total_power_at_i
          new_kr = kr_acc - needed
          if new_kr < 0 do
            {:halt, {new_kr, dac_acc, new_cas_acc, false}}
          else
            new_dac = :array.set(i, :array.get(i, dac_acc) + needed, dac_acc)
            end_idx_for_contribution = min(n - 1, i + 2 * r)
            new_dac = if end_idx_for_contribution + 1 < n + 1 do
              :array.set(end_idx_for_contribution + 1, :array.get(end_idx_for_contribution + 1, new_dac) - needed, new_dac)
            else
              new_dac
            end
            {:cont, {new_kr, new_dac, new_cas_acc + needed, true}}
          end
        else
          {:cont, {kr_acc, dac_acc, new_cas_acc, p_acc}}
        end
      end)
      possible
    end

    low = 0
    high = 2 * :math.pow(10, 10) |> round |> trunc + :math.pow(10, 9) |> round |> trunc + 7

    ans = 0
    binary_search(low, high, ans, check)
  end

  defp binary_search(low, high, ans, check) when low <= high do
    mid = low + div(high - low, 2)
    if check.(mid) do
      binary_search(mid + 1, high, mid, check)
    else
      binary_search(low, mid - 1, ans, check)
    end
  end
  defp binary_search(_low, _high, ans, _check), do: ans

  defp min(a, b), do: if a < b, do: a, else: b
  defp max(a, b), do: if a > b, do: a, else: b
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * log(MAX_POWER))

- **Space Complexity:** O(N)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-23 00:00:35 )</small>
</summary>

<div class="ai-solution-content">

### Approach

This problem can be solved by using a binary search approach to find the maximum possible minimum power of a city. The power of each city is calculated by considering the range of the power stations and the additional power stations that can be built.

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
      #include <vector>
      #include <algorithm>
      using namespace std;
      class Solution {
      public:
         int maxPower(vector<int>& stations, int r, int k) {
            int n = stations.size();
            vector<int> power(n);
            for (int i = 0; i < n; i++) {
               for (int j = max(0, i - r); j <= min(n - 1, i + r); j++) {
                  power[j] += stations[i];
               }
            }
            int low = *min_element(power.begin(), power.end());
            int high = *max_element(power.begin(), power.end()) + k;
            while (low < high) {
               int mid = low + (high - low + 1) / 2;
               vector<int> temp = power;
               int count = 0;
               for (int i = 0; i < n; i++) {
                  if (temp[i] < mid) {
                     int add = mid - temp[i];
                     count += add;
                     temp[i] += add;
                     for (int j = max(0, i - r); j <= min(n - 1, i + r); j++) {
                        if (j != i) {
                           temp[j] += add;
                        }
                     }
                  }
               }
               if (count <= k) {
                  low = mid;
               } else {
                  high = mid - 1;
               }
            }
            return low;
         }
      };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;
      public class Solution {
         public int maxPower(int[] stations, int r, int k) {
            int n = stations.length;
            int[] power = new int[n];
            for (int i = 0; i < n; i++) {
               for (int j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
                  power[j] += stations[i];
               }
            }
            int low = Integer.MAX_VALUE;
            int high = Integer.MIN_VALUE;
            for (int i = 0; i < n; i++) {
               low = Math.min(low, power[i]);
               high = Math.max(high, power[i]);
            }
            high += k;
            while (low < high) {
               int mid = low + (high - low + 1) / 2;
               int[] temp = power.clone();
               int count = 0;
               for (int i = 0; i < n; i++) {
                  if (temp[i] < mid) {
                     int add = mid - temp[i];
                     count += add;
                     temp[i] += add;
                     for (int j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
                        if (j != i) {
                           temp[j] += add;
                        }
                     }
                  }
               }
               if (count <= k) {
                  low = mid;
               } else {
                  high = mid - 1;
               }
            }
            return low;
         }
      }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
  def maxPower(self, stations: list[int], r: int, k: int) -> int:
     n = len(stations)
     power = [0] * n
     for i in range(n):
        for j in range(max(0, i - r), min(n, i + r + 1)):
           power[j] += stations[i]
     low = min(power)
     high = max(power) + k
     while low < high:
        mid = low + (high - low + 1) // 2
        temp = power[:]
        count = 0
        for i in range(n):
           if temp[i] < mid:
              add = mid - temp[i]
              count += add
              temp[i] += add
              for j in range(max(0, i - r), min(n, i + r + 1)):
                 if j != i:
                    temp[j] += add
        if count <= k:
           low = mid
        else:
           high = mid - 1
     return low
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
  def maxPower(self, stations: list[int], r: int, k: int) -> int:
     n = len(stations)
     power = [0] * n
     for i in range(n):
        for j in range(max(0, i - r), min(n, i + r + 1)):
           power[j] += stations[i]
     low = min(power)
     high = max(power) + k
     while low < high:
        mid = low + (high - low + 1) // 2
        temp = power[:]
        count = 0
        for i in range(n):
           if temp[i] < mid:
              add = mid - temp[i]
              count += add
              temp[i] += add
              for j in range(max(0, i - r), min(n, i + r + 1)):
                 if j != i:
                    temp[j] += add
        if count <= k:
           low = mid
        else:
           high = mid - 1
     return low
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
      #include <stdlib.h>
      #include <string.h>
      #define MAX(a, b) ((a) > (b) ? (a) : (b))
      #define MIN(a, b) ((a) < (b) ? (a) : (b))
      int maxPower(int* stations, int stationsSize, int r, int k) {
         int* power = (int*)malloc(stationsSize * sizeof(int));
         for (int i = 0; i < stationsSize; i++) {
            power[i] = 0;
         }
         for (int i = 0; i < stationsSize; i++) {
            for (int j = MAX(0, i - r); j <= MIN(stationsSize - 1, i + r); j++) {
               power[j] += stations[i];
            }
         }
         int low = power[0];
         int high = power[0];
         for (int i = 1; i < stationsSize; i++) {
            low = MIN(low, power[i]);
            high = MAX(high, power[i]);
         }
         high += k;
         while (low < high) {
            int mid = low + (high - low + 1) / 2;
            int* temp = (int*)malloc(stationsSize * sizeof(int));
            memcpy(temp, power, stationsSize * sizeof(int));
            int count = 0;
            for (int i = 0; i < stationsSize; i++) {
               if (temp[i] < mid) {
                  int add = mid - temp[i];
                  count += add;
                  temp[i] += add;
                  for (int j = MAX(0, i - r); j <= MIN(stationsSize - 1, i + r); j++) {
                     if (j != i) {
                        temp[j] += add;
                     }
                  }
               }
            }
            if (count <= k) {
               low = mid;
            } else {
               high = mid - 1;
            }
            free(temp);
         }
         free(power);
         return low;
      }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
      public class Solution {
         public int MaxPower(int[] stations, int r, int k) {
            int n = stations.Length;
            int[] power = new int[n];
            for (int i = 0; i < n; i++) {
               for (int j = Math.Max(0, i - r); j <= Math.Min(n - 1, i + r); j++) {
                  power[j] += stations[i];
               }
            }
            int low = power[0];
            int high = power[0];
            for (int i = 1; i < n; i++) {
               low = Math.Min(low, power[i]);
               high = Math.Max(high, power[i]);
            }
            high += k;
            while (low < high) {
               int mid = low + (high - low + 1) / 2;
               int[] temp = (int[])power.Clone();
               int count = 0;
               for (int i = 0; i < n; i++) {
                  if (temp[i] < mid) {
                     int add = mid - temp[i];
                     count += add;
                     temp[i] += add;
                     for (int j = Math.Max(0, i - r); j <= Math.Min(n - 1, i + r); j++) {
                        if (j != i) {
                           temp[j] += add;
                        }
                     }
                  }
               }
               if (count <= k) {
                  low = mid;
               } else {
                  high = mid - 1;
               }
            }
            return low;
         }
      }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxPower = function(stations, r, k) {
  let n = stations.length;
  let power = new Array(n).fill(0);
  for (let i = 0; i < n; i++) {
     for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
        power[j] += stations[i];
     }
  }
  let low = power[0];
  let high = power[0];
  for (let i = 1; i < n; i++) {
     low = Math.min(low, power[i]);
     high = Math.max(high, power[i]);
  }
  high += k;
  while (low < high) {
     let mid = low + Math.floor((high - low + 1) / 2);
     let temp = power.slice();
     let count = 0;
     for (let i = 0; i < n; i++) {
        if (temp[i] < mid) {
           let add = mid - temp[i];
           count += add;
           temp[i] += add;
           for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
              if (j != i) {
                 temp[j] += add;
              }
           }
        }
     }
     if (count <= k) {
        low = mid;
     } else {
        high = mid - 1;
     }
  }
  return low;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxPower(stations: number[], r: number, k: number): number {
  let n = stations.length;
  let power: number[] = new Array(n).fill(0);
  for (let i = 0; i < n; i++) {
     for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
        power[j] += stations[i];
     }
  }
  let low = power[0];
  let high = power[0];
  for (let i = 1; i < n; i++) {
     low = Math.min(low, power[i]);
     high = Math.max(high, power[i]);
  }
  high += k;
  while (low < high) {
     let mid = low + Math.floor((high - low + 1) / 2);
     let temp = power.slice();
     let count = 0;
     for (let i = 0; i < n; i++) {
        if (temp[i] < mid) {
           let add = mid - temp[i];
           count += add;
           temp[i] += add;
           for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
              if (j != i) {
                 temp[j] += add;
              }
           }
        }
     }
     if (count <= k) {
        low = mid;
     } else {
        high = mid - 1;
     }
  }
  return low;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
function maxPower($stations, $r, $k) {
  $n = count($stations);
  $power = array_fill(0, $n, 0);
  for ($i = 0; $i < $n; $i++) {
     for ($j = max(0, $i - $r); $j <= min($n - 1, $i + $r); $j++) {
        $power[$j] += $stations[$i];
     }
  }
  $low = $power[0];
  $high = $power[0];
  for ($i = 1; $i < $n; $i++) {
     $low = min($low, $power[$i]);
     $high = max($high, $power[$i]);
  }
  $high += $k;
  while ($low < $high) {
     $mid = $low + floor(($high - $low + 1) / 2);
     $temp = $power;
     $count = 0;
     for ($i = 0; $i < $n; $i++) {
        if ($temp[$i] < $mid) {
           $add = $mid - $temp[$i];
           $count += $add;
           $temp[$i] += $add;
           for ($j = max(0, $i - $r); $j <= min($n - 1, $i + $r); $j++) {
              if ($j != $i) {
                 $temp[$j] += $add;
              }
           }
        }
     }
     if ($count <= $k) {
        $low = $mid;
     } else {
        $high = $mid - 1;
     }
  }
  return $low;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
func maxPower(_ stations: [Int], _ r: Int, _ k: Int) -> Int {
  let n = stations.count
  var power = [Int](repeating: 0, count: n)
  for i in 0..<n {
     for j in max(0, i - r)...min(n - 1, i + r) {
        power[j] += stations[i]
     }
  }
  var low = power[0]
  var high = power[0]
  for i in 1..<n {
     low = min(low, power[i])
     high = max(high, power[i])
  }
  high += k
  while low < high {
     let mid = low + (high - low + 1) / 2
     var temp = power
     var count = 0
     for i in 0..<n {
        if temp[i] < mid {
           let add = mid - temp[i]
           count += add
           temp[i] += add
           for j in max(0, i - r)...min(n - 1, i + r) {
              if j != i {
                 temp[j] += add
              }
           }
        }
     }
     if count <= k {
        low = mid
     } else {
        high = mid - 1
     }
  }
  return low
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
  fun maxPower(stations: IntArray, r: Int, k: Int): Int {
     val n = stations.size
     val power = IntArray(n)
     for (i in 0 until n) {
        for (j in maxOf(0, i - r)..minOf(n - 1, i + r)) {
           power[j] += stations[i]
        }
     }
     var low = power[0]
     var high = power[0]
     for (i in 1 until n) {
        low = minOf(low, power[i])
        high = maxOf(high, power[i])
     }
     high += k
     while (low < high) {
        val mid = low + (high - low + 1) / 2
        val temp = power.copyOf()
        var count = 0
        for (i in 0 until n) {
           if (temp[i] < mid) {
              val add = mid - temp[i]
              count += add
              temp[i] += add
              for (j in maxOf(0, i - r)..minOf(n - 1, i + r)) {
                 if (j != i) {
                    temp[j] += add
                 }
              }
           }
        }
        if (count <= k) {
           low = mid
        } else {
           high = mid - 1
        }
     }
     return low
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxPower(List<int> stations, int r, int k) {
     int n = stations.length;
     List<int> power = List<int>.filled(n, 0);
     for (int i = 0; i < n; i++) {
        for (int j = max(0, i - r); j <= min(n - 1, i + r); j++) {
           power[j] += stations[i];
        }
     }
     int low = power[0];
     int high = power[0];
     for (int i = 1; i < n; i++) {
        low = min(low, power[i]);
        high = max(high, power[i]);
     }
     high += k;
     while (low < high) {
        int mid = low + (high - low + 1) ~/ 2;
        List<int> temp = List<int>.from(power);
        int count = 0;
        for (int i = 0; i < n; i++) {
           if (temp[i] < mid) {
              int add = mid - temp[i];
              count += add;
              temp[i] += add;
              for (int j = max(0, i - r); j <= min(n - 1, i + r); j++) {
                 if (j != i) {
                    temp[j] += add;
                 }
              }
           }
        }
        if (count <= k) {
           low = mid;
        } else {
           high = mid - 1;
        }
     }
     return low;
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
      func maxPower(stations []int, r int, k int) int {
         n := len(stations)
         power := make([]int, n)
         for i := 0; i < n; i++ {
            for j := max(0, i-r); j <= min(n-1, i+r); j++ {
               power[j] += stations[i]
            }
         }
         low := power[0]
         high := power[0]
         for i := 1; i < n; i++ {
            low = min(low, power[i])
            high = max(high, power[i])
         }
         high += k
         for low < high {
            mid := low + (high-low+1)/2
            temp := make([]int, n)
            copy(temp, power)
            count := 0
            for i := 0; i < n; i++ {
               if temp[i] < mid {
                  add := mid - temp[i]
                  count += add
                  temp[i] += add
                  for j := max(0, i-r); j <= min(n-1, i+r); j++ {
                     if j != i {
                        temp[j] += add
                     }
                  }
               }
            }
            if count <= k {
               low = mid
            } else {
               high = mid - 1
            }
         }
         return low
      }
      func max(a, b int) int {
         if a > b {
            return a
         }
         return b
      }
      func min(a, b int) int {
         if a < b {
            return a
         }
         return b
      }
      func main() {
         stations := []int{1, 2, 4, 5, 0}
         r := 1
         k := 2
         fmt.Println(maxPower(stations, r, k))
      }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_power(stations, r, k)
  n = stations.size
  power = Array.new(n, 0)
  for i in 0...n
     for j in [0, i - r].max..[n - 1, i + r].min
        power[j] += stations[i]
     end
  end
  low = power[0]
  high = power[0]
  for i in 1...n
     low = [low, power[i]].min
     high = [high, power[i]].max
  end
  high += k
  while low < high
     mid = low + (high - low + 1) / 2
     temp = power.dup
     count = 0
     for i in 0...n
        if temp[i] < mid
           add = mid - temp[i]
           count += add
           temp[i] += add
           for j in [0, i - r].max..[n - 1, i + r].min
              if j != i
                 temp[j] += add
              end
           end
        end
     end
     if count <= k
        low = mid
     else
        high = mid - 1
     end
  end
  low
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def maxPower(stations: Array[Int], r: Int, k: Int): Int = {
     val n = stations.length
     val power = new Array[Int](n)
     for (i <- 0 until n) {
        for (j <- math.max(0, i - r) to math.min(n - 1, i + r)) {
           power(j) += stations(i)
        }
     }
     var low = power(0)
     var high = power(0)
     for (i <- 1 until n) {
        low = math.min(low, power(i))
        high = math.max(high, power(i))
     }
     high += k
     while (low < high) {
        val mid = low + (high - low + 1) / 2
        val temp = power.clone()
        var count = 0
        for (i <- 0 until n) {
           if (temp(i) < mid) {
              val add = mid - temp(i)
              count += add
              temp(i) += add
              for (j <- math.max(0, i - r) to math.min(n - 1, i + r)) {
                 if (j != i) {
                    temp(j) += add
                 }
              }
           }
        }
        if (count <= k) {
           low = mid
        } else {
           high = mid - 1
        }
     }
     low
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
fn max_power(stations: Vec<i32>, r: i32, k: i32) -> i32 {
  let n = stations.len();
  let mut power = vec![0; n];
  for i in 0..n {
     for j in (i as i32 - r).max(0)..=(i as i32 + r).min((n - 1) as i32) {
        power[j as usize] += stations[i];
     }
  }
  let mut low = power[0];
  let mut high = power[0];
  for i in 1..n {
     low = low.min(power[i]);
     high = high.max(power[i]);
  }
  high += k;
  while low < high {
     let mid = low + (high - low + 1) / 2;
     let mut temp = power.clone();
     let mut count = 0;
     for i in 0..n {
        if temp[i] < mid {
           let add = mid - temp[i];
           count += add;
           temp[i] += add;
           for j in (i as i32 - r).max(0)..=(i as i32 + r).min((n - 1) as i32) {
              if j as usize != i {
                 temp[j as usize] += add;
              }
           }
        }
     }
     if count <= k {
        low = mid;
     } else {
        high = mid - 1;
     }
  }
  low
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
      (define (max-power stations r k)
        (define n (length stations))
        (define power (make-list n 0))
        (for ([i (range n)])
          (for ([j (range (max 0 (- i r)) (add1 (min (- n 1) (+ i r))))])
            (set! (list-ref power j) (+ (list-ref power j) (list-ref stations i)))))
        (define low (list-ref power 0))
        (define high (list-ref power 0))
        (for ([i (range 1 n)])
          (set! low (min low (list-ref power i)))
          (set! high (max high (list-ref power i))))
        (set! high (+ high k))
        (let loop ([low low] [high high])
          (if (< low high)
              (let* ([mid (+ low (quotient (+ high low) 2))]
                     [temp (map (λ(x) x) power)]
                     [count 0])
                (for ([i (range n)])
                  (when (< (list-ref temp i) mid)
                    (let ([add (- mid (list-ref temp i)))])
                      (set! count (+ count add))
                      (set! (list-ref temp i) (+ (list-ref temp i) add))
                      (for ([j (range (max 0 (- i r)) (add1 (min (- n 1) (+ i r))))])
                        (when (not (= j i))
                          (set! (list-ref temp j) (+ (list-ref temp j) add)))))))
                (if (<= count k)
                    (loop mid high)
                    (loop low (- mid 1))))
              low)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
      -export([max_power/3]).
      max_power(Stations, R, K) ->
         N = length(Stations),
         Power = lists:duplicate(N, 0),
         lists:foldl(
           fun(I, Acc) ->
             lists:foldl(
               fun(J, Acc1) ->
                 lists:update(J, Acc1, Acc1 + lists:nth(I + 1, Stations))
               end, Acc, lists:seq(max(0, I - R), min(N - 1, I + R)))
           end, Power, lists:seq(0, N - 1)),
         Low = lists:nth(1, Power),
         High = lists:nth(1, Power),
         {Low1, High1} = lists:foldl(
           fun(I, {Low0, High0}) ->
             {min(Low0, lists:nth(I + 1, Power)), max(High0, lists:nth(I + 1, Power))}
           end, {Low, High}, lists:seq(0, N - 1)),
         High1 + K,
         loop(Low1, High1 + K).
      loop(Low, High) when Low < High ->
         Mid = Low + (High - Low) div 2,
         Temp = lists:duplicate(length(Power), 0),
         {Count, Temp1} = lists:foldl(
           fun(I, {Count0, Temp0}) ->
             case lists:nth(I + 1, Temp0) < Mid of
               true ->
                 Add = Mid - lists:nth(I + 1, Temp0),
                 {Count0 + Add, lists:update(I, Temp0, lists:nth(I + 1, Temp0) + Add)};
               false ->
                 {Count0, Temp0}
             end
           end, {0, Power}, lists:seq(0, length(Power) - 1)),
         case Count =< K of
           true -> loop(Mid, High);
           false -> loop(Low, Mid - 1)
         end;
      loop(Low, High) -> Low.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
def max_power(stations, r, k) do
  n = length(stations)
  power = Enum.to_list(0..n-1)
  |> Enum.map(fn _ -> 0 end)
  Enum.reduce(0..n-1, power, fn i, acc ->
    Enum.reduce(max(0, i - r)..min(n - 1, i + r), acc, fn j, acc1 ->
      List.update_at(acc1, j, &(&1 + Enum.at(stations, i)))
    end)
  end)
  low = Enum.at(power, 0)
  high = Enum.at(power, 0)
  {low1, high1} = Enum.reduce(1..n-1, {low, high}, fn i, {low0, high0} ->
    {min(low0, Enum.at(power, i)), max(high0, Enum.at(power, i))}
  end)
  high1 + k
  loop(low1, high1 + k)
end
defp loop(low, high) when low < high do
  mid = low + div(high - low + 1, 2)
  temp = Enum.to_list(0..length(power)-1)
  |> Enum.map(fn _ -> 0 end)
  {count, temp1} = Enum.reduce(0..length(power)-1, {0, power}, fn i, {count0, temp0} ->
    if Enum.at(temp0, i) < mid do
      add = mid - Enum.at(temp0, i)
      {count0 + add, List.update_at(temp0, i, &(&1 + add))}
    else
      {count0, temp0}
    end
  end)
  if count <= k do
    loop(mid, high)
  else
    loop(low, mid - 1)
  end
end
defp loop(low, high), do: low
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log m)

- **Space Complexity:** O(n)

</div>
</details>
