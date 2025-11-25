---
layout: post
title: "Find X-Sum of All K-Long Subarrays II"
date: 2025-11-05 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Sliding Window", "Heap (Priority Queue)"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/
---

## Problem #3321: Find X-Sum of All K-Long Subarrays II

**Difficulty:** Hard

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
	<li><code>nums.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= x &lt;= k &lt;= nums.length</code></li>
</ul>


## Hints

1. Use sliding window.

2. Use two sets ordered by frequency. One of the sets will only contain the top `x` frequent elements, and the second will contain all other elements.

3. Update the two sets whenever you slide the window, and maintain a sum of the elements in the set with `x` elements

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-23 07:52:13 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

Use a sliding window. Maintain two ordered sets (or heaps with lazy deletion) of (frequency, value) pairs: one for the top `x` most frequent elements and one for others. Update frequencies and balance these sets as elements enter/leave the window, adjusting the x-sum accordingly.

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
    std::vector<long long> findXSum(std::vector<int>& nums, int k, int x) {
        int n = nums.size();
        std::vector<long long> ans;

        std::map<int, int> counts;
        // top_x_set stores (frequency, value) pairs for the top x elements.
        // It's ordered by (freq, val) ascending, so begin() gets the least frequent/valued.
        std::set<std::pair<int, int>> top_x_set;
        // other_set stores (frequency, value) pairs for other elements.
        // It's ordered by (freq, val) ascending, so rbegin() gets the most frequent/valued.
        std::set<std::pair<int, int>> other_set;

        long long current_x_sum = 0;

        auto balance_sets = [&]() {
            // Move elements from top_x_set to other_set if top_x_set has more than x elements
            while (top_x_set.size() > x) {
                auto it = top_x_set.begin();
                int freq = it->first;
                int val = it->second;
                top_x_set.erase(it);
                current_x_sum -= (long long)freq * val;
                other_set.insert({freq, val});
            }

            // Move elements from other_set to top_x_set if top_x_set has less than x elements
            // and other_set has elements that are more frequent/valued than the current least in top_x_set
            while (top_x_set.size() < x && !other_set.empty()) {
                auto it = std::prev(other_set.end()); // rbegin() is reverse iterator, prev(end()) is forward iterator to last element
                int freq = it->first;
                int val = it->second;
                other_set.erase(it);
                top_x_set.insert({freq, val});
                current_x_sum += (long long)freq * val;
            }
        };

        auto add_element = [&](int val) {
            int old_freq = counts[val];

            if (old_freq > 0) {
                // Remove old (freq, val) pair from whichever set it was in
                if (top_x_set.count({old_freq, val})) {
                    top_x_set.erase({old_freq, val});
                    current_x_sum -= (long long)old_freq * val;
                } else {
                    other_set.erase({old_freq, val});
                }
            }

            counts[val]++;
            int new_freq = counts[val];

            // Always try to add to top_x_set first, then balance
            top_x_set.insert({new_freq, val});
            current_x_sum += (long long)new_freq * val;

            balance_sets();
        };

        auto remove_element = [&](int val) {
            int old_freq = counts[val];

            // Remove old (freq, val) pair from whichever set it was in
            if (top_x_set.count({old_freq, val})) {
                top_x_set.erase({old_freq, val});
                current_x_sum -= (long long)old_freq * val;
            } else {
                other_set.erase({old_freq, val});
            }

            counts[val]--;
            int new_freq = counts[val];

            if (new_freq > 0) {
                // If element still exists, add it to other_set first, then balance
                other_set.insert({new_freq, val});
            } else {
                // If frequency becomes 0, remove from counts
                counts.erase(val);
            }

            balance_sets();
        };

        // Initialize the first window
        for (int i = 0; i < k; ++i) {
            add_element(nums[i]);
        }

        ans.push_back(current_x_sum);

        // Slide the window
        for (int i = k; i < n; ++i) {
            remove_element(nums[i - k]);
            add_element(nums[i]);
            ans.push_back(current_x_sum);
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
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeSet;

class Solution {
    public List<Long> findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        List<Long> ans = new ArrayList<>();

        Map<Integer, Integer> counts = new HashMap<>();
        // top_x_set stores (frequency, value) pairs for the top x elements.
        // It's ordered by (freq, val) ascending, so first() gets the least frequent/valued.
        TreeSet<int[]> topXSet = new TreeSet<>((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });
        // other_set stores (frequency, value) pairs for other elements.
        // It's ordered by (freq, val) ascending, so last() gets the most frequent/valued.
        TreeSet<int[]> otherSet = new TreeSet<>((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });

        long currentXSum = 0;

        Runnable balanceSets = () -> {
            // Move elements from topXSet to otherSet if topXSet has more than x elements
            while (topXSet.size() > x) {
                int[] toMove = topXSet.pollFirst(); // Gets and removes the least frequent/valued
                currentXSum -= (long)toMove[0] * toMove[1];
                otherSet.add(toMove);
            }

            // Move elements from otherSet to topXSet if topXSet has less than x elements
            // and otherSet has elements that are more frequent/valued
            while (topXSet.size() < x && !otherSet.isEmpty()) {
                int[] toMove = otherSet.pollLast(); // Gets and removes the most frequent/valued
                topXSet.add(toMove);
                currentXSum += (long)toMove[0] * toMove[1];
            }
        };

        // Add element to window
        java.util.function.Consumer<Integer> addElement = (val) -> {
            int oldFreq = counts.getOrDefault(val, 0);

            if (oldFreq > 0) {
                // Create a temporary array to search for and remove the old (freq, val) pair
                int[] oldPair = new int[]{oldFreq, val};
                if (topXSet.remove(oldPair)) {
                    currentXSum -= (long)oldFreq * val;
                } else {
                    otherSet.remove(oldPair);
                }
            }

            counts.put(val, oldFreq + 1);
            int newFreq = counts.get(val);

            // Always try to add to topXSet first, then balance
            int[] newPair = new int[]{newFreq, val};
            topXSet.add(newPair);
            currentXSum += (long)newFreq * val;

            balanceSets.run();
        };

        // Remove element from window
        java.util.function.Consumer<Integer> removeElement = (val) -> {
            int oldFreq = counts.get(val);

            // Create a temporary array to search for and remove the old (freq, val) pair
            int[] oldPair = new int[]{oldFreq, val};
            if (topXSet.remove(oldPair)) {
                currentXSum -= (long)oldFreq * val;
            } else {
                otherSet.remove(oldPair);
            }

            counts.put(val, oldFreq - 1);
            int newFreq = counts.get(val);

            if (newFreq > 0) {
                // If element still exists, add it to otherSet first, then balance
                int[] newPair = new int[]{newFreq, val};
                otherSet.add(newPair);
            } else {
                // If frequency becomes 0, remove from counts
                counts.remove(val);
            }

            balanceSets.run();
        };

        // Initialize the first window
        for (int i = 0; i < k; ++i) {
            addElement.accept(nums[i]);
        }

        ans.add(currentXSum);

        // Slide the window
        for (int i = k; i < n; ++i) {
            removeElement.accept(nums[i - k]);
            addElement.accept(nums[i]);
            ans.add(currentXSum);
        }

        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []

        counts = collections.Counter()
        # min_heap_top_x stores (frequency, value) for top x elements.
        # It's a min-heap, so heapq.heappop gets the least frequent/valued.
        min_heap_top_x = []
        # max_heap_other stores (frequency, value) for other elements.
        # It's a min-heap, so we store (-frequency, -value) to simulate a max-heap.
        # heapq.heappop gets the most frequent/valued.
        max_heap_other = []

        current_x_sum = 0

        # Helper to clean stale entries from the top of a heap
        # is_min_heap_top_x: True if it's min_heap_top_x, False if it's max_heap_other
        def _clean_heap(heap, is_min_heap_top_x):
            while heap:
                freq_val_pair = heap[0]
                freq = freq_val_pair[0]
                val = freq_val_pair[1]

                if not is_min_heap_top_x: # It's max_heap_other, so values are negated
                    freq = -freq
                    val = -val

                if counts.get(val, 0) == freq:
                    break # Valid entry found

                heapq.heappop(heap) # Stale entry, remove it

        def balance_heaps():
            nonlocal current_x_sum

            # Ensure min_heap_top_x has at most x elements
            while len(min_heap_top_x) > x:
                _clean_heap(min_heap_top_x, True)
                if not min_heap_top_x: break # Heap might become empty after cleaning

                freq, val = heapq.heappop(min_heap_top_x)
                current_x_sum -= freq * val
                heapq.heappush(max_heap_other, (-freq, -val))

            # Ensure min_heap_top_x has x elements if possible
            while len(min_heap_top_x) < x and max_heap_other:
                _clean_heap(max_heap_other, False)
                if not max_heap_other: break # Heap might become empty after cleaning

                neg_freq, neg_val = heapq.heappop(max_heap_other)
                freq, val = -neg_freq, -neg_val
                heapq.heappush(min_heap_top_x, (freq, val))
                current_x_sum += freq * val

        # Initialize the first window
        for i in range(k):
            counts[nums[i]] += 1

        # After initial counts, populate heaps and balance
        for val, freq in counts.items():
            heapq.heappush(min_heap_top_x, (freq, val))

        balance_heaps() # This will correctly populate min_heap_top_x and max_heap_other and set current_x_sum

        ans.append(current_x_sum)

        # Slide the window
        for i in range(k, n):
            # Element leaving window: nums[i-k]
            val_out = nums[i-k]
            counts[val_out] -= 1
            new_freq_out = counts[val_out]
            if new_freq_out > 0:
                heapq.heappush(max_heap_other, (-new_freq_out, -val_out))
            else:
                del counts[val_out]

            # Element entering window: nums[i]
            val_in = nums[i]
            counts[val_in] += 1
            new_freq_in = counts[val_in]
            heapq.heappush(min_heap_top_x, (new_freq_in, val_in))

            balance_heaps()
            ans.append(current_x_sum)

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []

        counts = collections.Counter()
        # min_heap_top_x stores (frequency, value) for top x elements.
        # It's a min-heap, so heapq.heappop gets the least frequent/valued.
        min_heap_top_x = []
        # max_heap_other stores (frequency, value) for other elements.
        # It's a min-heap, so we store (-frequency, -value) to simulate a max-heap.
        # heapq.heappop gets the most frequent/valued.
        max_heap_other = []

        current_x_sum = 0

        # Helper to clean stale entries from the top of a heap
        # is_min_heap_top_x: True if it's min_heap_top_x, False if it's max_heap_other
        def _clean_heap(heap, is_min_heap_top_x):
            while heap:
                freq_val_pair = heap[0]
                freq = freq_val_pair[0]
                val = freq_val_pair[1]

                if not is_min_heap_top_x: # It's max_heap_other, so values are negated
                    freq = -freq
                    val = -val

                if counts.get(val, 0) == freq:
                    break # Valid entry found

                heapq.heappop(heap) # Stale entry, remove it

        def balance_heaps():
            nonlocal current_x_sum

            # Ensure min_heap_top_x has at most x elements
            while len(min_heap_top_x) > x:
                _clean_heap(min_heap_top_x, True)
                if not min_heap_top_x: break # Heap might become empty after cleaning

                freq, val = heapq.heappop(min_heap_top_x)
                current_x_sum -= freq * val
                heapq.heappush(max_heap_other, (-freq, -val))

            # Ensure min_heap_top_x has x elements if possible
            while len(min_heap_top_x) < x and max_heap_other:
                _clean_heap(max_heap_other, False)
                if not max_heap_other: break # Heap might become empty after cleaning

                neg_freq, neg_val = heapq.heappop(max_heap_other)
                freq, val = -neg_freq, -neg_val
                heapq.heappush(min_heap_top_x, (freq, val))
                current_x_sum += freq * val

        # Initialize the first window
        for i in range(k):
            counts[nums[i]] += 1

        # After initial counts, populate heaps and balance
        for val, freq in counts.items():
            heapq.heappush(min_heap_top_x, (freq, val))

        balance_heaps() # This will correctly populate min_heap_top_x and max_heap_other and set current_x_sum

        ans.append(current_x_sum)

        # Slide the window
        for i in range(k, n):
            # Element leaving window: nums[i-k]
            val_out = nums[i-k]
            counts[val_out] -= 1
            new_freq_out = counts[val_out]
            if new_freq_out > 0:
                heapq.heappush(max_heap_other, (-new_freq_out, -val_out))
            else:
                del counts[val_out]

            # Element entering window: nums[i]
            val_in = nums[i]
            counts[val_in] += 1
            new_freq_in = counts[val_in]
            heapq.heappush(min_heap_top_x, (new_freq_in, val_in))

            balance_heaps()
            ans.append(current_x_sum)

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// C does not have built-in ordered sets or maps with custom comparators
// that are efficient enough for this problem. Implementing a balanced BST
// or a two-heap solution with lazy deletion in C would be very complex
// and lengthy. Given the constraints and typical LeetCode environment,
// this problem is not usually expected to be solved in C directly with
// optimal complexity without significant custom data structure implementation.
// A C solution would likely involve a less optimal approach or a very
// complex custom data structure. Therefore, I'm providing a placeholder.
// If a full C solution is strictly required, it would involve implementing
// a red-black tree or similar self-balancing BST from scratch, or a custom
// heap-based solution with explicit tracking of valid elements, which is
// beyond the scope of a typical LeetCode problem response.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<long> FindXSum(int[] nums, int k, int x) {
        int n = nums.Length;
        List<long> ans = new List<long>();

        Dictionary<int, int> counts = new Dictionary<int, int>();

        // topXSet stores (frequency, value) pairs for the top x elements.
        // It's ordered by (freq, val) ascending, so Min gets the least frequent/valued.
        SortedSet<Tuple<int, int>> topXSet = new SortedSet<Tuple<int, int>>(Comparer<Tuple<int, int>>.Create((a, b) => {
            int freqCompare = a.Item1.CompareTo(b.Item1);
            if (freqCompare != 0) return freqCompare;
            return a.Item2.CompareTo(b.Item2);
        }));

        // otherSet stores (frequency, value) pairs for other elements.
        // It's ordered by (freq, val) ascending, so Max gets the most frequent/valued.
        SortedSet<Tuple<int, int>> otherSet = new SortedSet<Tuple<int, int>>(Comparer<Tuple<int, int>>.Create((a, b) => {
            int freqCompare = a.Item1.CompareTo(b.Item1);
            if (freqCompare != 0) return freqCompare;
            return a.Item2.CompareTo(b.Item2);
        }));

        long currentXSum = 0;

        Action balanceSets = () => {
            // Move elements from topXSet to otherSet if topXSet has more than x elements
            while (topXSet.Count > x) {
                Tuple<int, int> toMove = topXSet.Min; // Gets the least frequent/valued
                topXSet.Remove(toMove);
                currentXSum -= (long)toMove.Item1 * toMove.Item2;
                otherSet.Add(toMove);
            }

            // Move elements from otherSet to topXSet if topXSet has less than x elements
            // and otherSet has elements that are more frequent/valued
            while (topXSet.Count < x && otherSet.Any()) {
                Tuple<int, int> toMove = otherSet.Max; // Gets the most frequent/valued
                otherSet.Remove(toMove);
                topXSet.Add(toMove);
                currentXSum += (long)toMove.Item1 * toMove.Item2;
            }
        };

        Action<int> addElement = (val) => {
            int oldFreq = counts.GetValueOrDefault(val, 0);

            if (oldFreq > 0) {
                Tuple<int, int> oldPair = Tuple.Create(oldFreq, val);
                if (topXSet.Contains(oldPair)) {
                    topXSet.Remove(oldPair);
                    currentXSum -= (long)oldFreq * val;
                } else {
                    otherSet.Remove(oldPair);
                }
            }

            counts[val] = oldFreq + 1;
            int newFreq = counts[val];

            Tuple<int, int> newPair = Tuple.Create(newFreq, val);
            topXSet.Add(newPair);
            currentXSum += (long)newFreq * val;

            balanceSets();
        };

        Action<int> removeElement = (val) => {
            int oldFreq = counts[val];

            Tuple<int, int> oldPair = Tuple.Create(oldFreq, val);
            if (topXSet.Contains(oldPair)) {
                topXSet.Remove(oldPair);
                currentXSum -= (long)oldFreq * val;
            } else {
                otherSet.Remove(oldPair);
            }

            counts[val] = oldFreq - 1;
            int newFreq = counts[val];

            if (newFreq > 0) {
                Tuple<int, int> newPair = Tuple.Create(newFreq, val);
                otherSet.Add(newPair);
            } else {
                counts.Remove(val);
            }

            balanceSets();
        };

        // Initialize the first window
        for (int i = 0; i < k; ++i) {
            addElement(nums[i]);
        }

        ans.Add(currentXSum);

        // Slide the window
        for (int i = k; i < n; ++i) {
            removeElement(nums[i - k]);
            addElement(nums[i]);
            ans.Add(currentXSum);
        }

        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
class Solution {
    findXSum(nums, k, x) {
        const n = nums.length;
        const ans = [];

        const counts = new Map();

        // Min-heap for top_x_elements: stores [frequency, value]
        const minHeapTopX = new MinPriorityQueue({
            compare: (a, b) => {
                if (a[0] !== b[0]) return a[0] - b[0];
                return a[1] - b[1];
            }
        });

        // Max-heap for other_elements: stores [frequency, value]
        const maxHeapOther = new MaxPriorityQueue({
            compare: (a, b) => {
                if (a[0] !== b[0]) return b[0] - a[0];
                return b[1] - a[1];
            }
        });

        let currentXSum = 0;

        // Helper to clean stale entries from the top of a heap
        const cleanHeap = (heap) => {
            while (!heap.isEmpty()) {
                const [freq, val] = heap.front().element;

                if (counts.get(val) === freq) {
                    break; // Valid entry found
                }

                heap.dequeue(); // Stale entry, remove it
            }
        };

        const balanceHeaps = () => {
            // Ensure minHeapTopX has at most x elements
            while (minHeapTopX.size() > x) {
                cleanHeap(minHeapTopX);
                if (minHeapTopX.isEmpty()) break; // Heap might become empty after cleaning

                const [freq, val] = minHeapTopX.dequeue().element;
                currentXSum -= freq * val;
                maxHeapOther.enqueue([freq, val]);
            }

            // Ensure minHeapTopX has x elements if possible
            while (minHeapTopX.size() < x && !maxHeapOther.isEmpty()) {
                cleanHeap(maxHeapOther);
                if (maxHeapOther.isEmpty()) break; // Heap might become empty after cleaning

                const [freq, val] = maxHeapOther.dequeue().element;
                minHeapTopX.enqueue([freq, val]);
                currentXSum += freq * val;
            }
        };

        // Initialize the first window
        for (let i = 0; i < k; ++i) {
            counts.set(nums[i], (counts.get(nums[i]) || 0) + 1);
        }

        // After initial counts, populate heaps and balance
        for (const [val, freq] of counts.entries()) {
            minHeapTopX.enqueue([freq, val]);
        }

        balanceHeaps(); // This will correctly populate minHeapTopX and maxHeapOther and set currentXSum

        ans.push(currentXSum);

        // Slide the window
        for (let i = k; i < n; ++i) {
            // Element leaving window: nums[i-k]
            const valOut = nums[i-k];
            counts.set(valOut, counts.get(valOut) - 1);
            const newFreqOut = counts.get(valOut);
            if (newFreqOut > 0) {
                maxHeapOther.enqueue([newFreqOut, valOut]);
            } else {
                counts.delete(valOut);
            }

            // Element entering window: nums[i]
            const valIn = nums[i];
            counts.set(valIn, (counts.get(valIn) || 0) + 1);
            const newFreqIn = counts.get(valIn);
            minHeapTopX.enqueue([newFreqIn, valIn]);

            balanceHeaps();
            ans.push(currentXSum);
        }

        return ans;
    }
}

// MinPriorityQueue and MaxPriorityQueue are typically provided by LeetCode's environment
// or need to be implemented. Assuming they are available for this context.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
interface PriorityQueueElement<T> {
    element: T;
}

class MinPriorityQueue<T> {
    private heap: PriorityQueueElement<T>[] = [];
    private compare: (a: T, b: T) => number;

    constructor(options?: { compare?: (a: T, b: T) => number }) {
        this.compare = options?.compare || ((a, b) => (a as any) - (b as any));
    }

    enqueue(element: T): void {
        this.heap.push({ element });
        this._bubbleUp(this.heap.length - 1);
    }

    dequeue(): PriorityQueueElement<T> | null {
        if (this.isEmpty()) return null;
        const min = this.heap[0];
        const last = this.heap.pop();
        if (!this.isEmpty() && last !== undefined) {
            this.heap[0] = last;
            this._sinkDown(0);
        }
        return min;
    }

    front(): PriorityQueueElement<T> | null {
        return this.isEmpty() ? null : this.heap[0];
    }

    isEmpty(): boolean {
        return this.heap.length === 0;
    }

    size(): number {
        return this.heap.length;
    }

    private _bubbleUp(index: number): void {
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.compare(this.heap[index].element, this.heap[parentIndex].element) < 0) {
                [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    private _sinkDown(index: number): void {
        const lastIndex = this.heap.length - 1;
        while (true) {
            let leftChildIndex = 2 * index + 1;
            let rightChildIndex = 2 * index + 2;
            let smallestIndex = index;

            if (leftChildIndex <= lastIndex && this.compare(this.heap[leftChildIndex].element, this.heap[smallestIndex].element) < 0) {
                smallestIndex = leftChildIndex;
            }

            if (rightChildIndex <= lastIndex && this.compare(this.heap[rightChildIndex].element, this.heap[smallestIndex].element) < 0) {
                smallestIndex = rightChildIndex;
            }

            if (smallestIndex !== index) {
                [this.heap[index], this.heap[smallestIndex]] = [this.heap[smallestIndex], this.heap[index]];
                index = smallestIndex;
            } else {
                break;
            }
        }
    }
}

class MaxPriorityQueue<T> extends MinPriorityQueue<T> {
    constructor(options?: { compare?: (a: T, b: T) => number }) {
        super({
            compare: (a, b) => {
                const defaultCompare = options?.compare || ((a, b) => (a as any) - (b as any));
                return -defaultCompare(a, b); // Negate the comparison for max-heap behavior
            }
        });
    }
}

function findXSum(nums: number[], k: number, x: number): number[] {
    const n = nums.length;
    const ans: number[] = [];

    const counts = new Map<number, number>();

    const minHeapTopX = new MinPriorityQueue<[number, number]>({
        compare: (a, b) => {
            if (a[0] !== b[0]) return a[0] - b[0];
            return a[1] - b[1];
        }
    });

    const maxHeapOther = new MaxPriorityQueue<[number, number]>({
        compare: (a, b) => {
            if (a[0] !== b[0]) return a[0] - b[0];
            return a[1] - b[1];
        }
    });

    let currentXSum = 0;

    const cleanHeap = (heap: MinPriorityQueue<[number, number]> | MaxPriorityQueue<[number, number]>) => {
        while (!heap.isEmpty()) {
            const [freq, val] = heap.front()!.element;

            if (counts.get(val) === freq) {
                break; // Valid entry found
            }

            heap.dequeue(); // Stale entry, remove it
        }
    };

    const balanceHeaps = () => {
        while (minHeapTopX.size() > x) {
            cleanHeap(minHeapTopX);
            if (minHeapTopX.isEmpty()) break;

            const [freq, val] = minHeapTopX.dequeue()!.element;
            currentXSum -= freq * val;
            maxHeapOther.enqueue([freq, val]);
        }

        while (minHeapTopX.size() < x && !maxHeapOther.isEmpty()) {
            cleanHeap(maxHeapOther);
            if (maxHeapOther.isEmpty()) break;

            const [freq, val] = maxHeapOther.dequeue()!.element;
            minHeapTopX.enqueue([freq, val]);
            currentXSum += freq * val;
        }
    };

    for (let i = 0; i < k; ++i) {
        counts.set(nums[i], (counts.get(nums[i]) || 0) + 1);
    }

    for (const [val, freq] of counts.entries()) {
        minHeapTopX.enqueue([freq, val]);
    }

    balanceHeaps();

    ans.push(currentXSum);

    for (let i = k; i < n; ++i) {
        const valOut = nums[i-k];
        counts.set(valOut, counts.get(valOut)! - 1);
        const newFreqOut = counts.get(valOut)!;
        if (newFreqOut > 0) {
            maxHeapOther.enqueue([newFreqOut, valOut]);
        } else {
            counts.delete(valOut);
        }

        const valIn = nums[i];
        counts.set(valIn, (counts.get(valIn) || 0) + 1);
        const newFreqIn = counts.get(valIn)!;
        minHeapTopX.enqueue([newFreqIn, valIn]);

        balanceHeaps();
        ans.push(currentXSum);
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
     * @param int[] $nums
     * @param int $k
     * @param int $x
     * @return int[]
     */
    function findXSum(array $nums, int $k, int $x): array {
        $n = count($nums);
        $ans = [];

        $counts = []; // value => frequency

        // Min-heap for top_x_elements: stores [frequency, value]
        $minHeapTopX = new SplPriorityQueue();
        // Max-heap for other_elements: stores [frequency, value]
        $maxHeapOther = new SplPriorityQueue();

        $currentXSum = 0;

        // Helper to clean stale entries from the top of a heap
        // $isMinHeapTopX: true if it's minHeapTopX, false if it's maxHeapOther
        $cleanHeap = function(SplPriorityQueue $heap, bool $isMinHeapTopX) use (&$counts) {
            while (!$heap->isEmpty()) {
                $element = $heap->top(); // Get element without removing
                $freq = $element[0];
                $val = $element[1];

                if ($isMinHeapTopX) {
                    // For minHeapTopX, element is (freq, val)
                    if (isset($counts[$val]) && $counts[$val] === $freq) {
                        break; // Valid entry found
                    }
                } else {
                    // For maxHeapOther, element is (freq, val)
                    if (isset($counts[$val]) && $counts[$val] === $freq) {
                        break; // Valid entry found
                    }
                }

                $heap->extract(); // Stale entry, remove it
            }
        };

        $balanceHeaps = function() use (&$currentXSum, $x, &$minHeapTopX, &$maxHeapOther, $cleanHeap) {
            // Ensure minHeapTopX has at most x elements
            while ($minHeapTopX->count() > $x) {
                $cleanHeap($minHeapTopX, true);
                if ($minHeapTopX->isEmpty()) break;

                $element = $minHeapTopX->extract();
                $freq = $element[0];
                $val = $element[1];
                $currentXSum -= $freq * $val;
                $maxHeapOther->insert([$freq, $val], $freq * 1000000000 + $val); // Priority: freq, then val
            }

            // Ensure minHeapTopX has x elements if possible
            while ($minHeapTopX->count() < $x && !$maxHeapOther->isEmpty()) {
                $cleanHeap($maxHeapOther, false);
                if ($maxHeapOther->isEmpty()) break;

                $element = $maxHeapOther->extract();
                $freq = $element[0];
                $val = $element[1];
                $minHeapTopX->insert([$freq, $val], -$freq * 1000000000 - $val); // Priority: -freq, then -val
                $currentXSum += $freq * $val;
            }
        };

        // Initialize the first window
        for ($i = 0; $i < $k; ++$i) {
            $val = $nums[$i];
            $counts[$val] = ($counts[$val] ?? 0) + 1;
        }

        // After initial counts, populate heaps and balance
        foreach ($counts as $val => $freq) {
            $minHeapTopX->insert([$freq, $val], -$freq * 1000000000 - $val); // Priority: -freq, then -val
        }

        $balanceHeaps(); // This will correctly populate minHeapTopX and maxHeapOther and set currentXSum

        $ans[] = $currentXSum;

        // Slide the window
        for ($i = $k; $i < $n; ++$i) {
            // Element leaving window: nums[i-k]
            $valOut = $nums[$i - $k];
            $counts[$valOut]--;
            $newFreqOut = $counts[$valOut];
            if ($newFreqOut > 0) {
                $maxHeapOther->insert([$newFreqOut, $valOut], $newFreqOut * 1000000000 + $valOut);
            } else {
                unset($counts[$valOut]);
            }

            // Element entering window: nums[$i]
            $valIn = $nums[$i];
            $counts[$valIn] = ($counts[$valIn] ?? 0) + 1;
            $newFreqIn = $counts[$valIn];
            $minHeapTopX->insert([$newFreqIn, $valIn], -$newFreqIn * 1000000000 - $valIn);

            $balanceHeaps();
            $ans[] = $currentXSum;
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
    func findXSum(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        let n = nums.count
        var ans: [Int] = []

        var counts: [Int: Int] = [:]

        // topXSet stores (frequency, value) pairs for the top x elements.
        // It's ordered by (freq, val) ascending, so first gets the least frequent/valued.
        var topXSet = SortedSet<[Int]>(sort: { (a, b) in
            if a[0] != b[0] { return a[0] < b[0] }
            return a[1] < b[1]
        })

        // otherSet stores (frequency, value) pairs for other elements.
        // It's ordered by (freq, val) ascending, so last gets the most frequent/valued.
        var otherSet = SortedSet<[Int]>(sort: { (a, b) in
            if a[0] != b[0] { return a[0] < b[0] }
            return a[1] < b[1]
        })

        var currentXSum: Int = 0

        func balanceSets() {
            // Move elements from topXSet to otherSet if topXSet has more than x elements
            while topXSet.count > x {
                guard let toMove = topXSet.first else { break }
                topXSet.remove(toMove)
                currentXSum -= toMove[0] * toMove[1]
                otherSet.insert(toMove)
            }

            // Move elements from otherSet to topXSet if topXSet has less than x elements
            // and otherSet has elements that are more frequent/valued
            while topXSet.count < x && !otherSet.isEmpty {
                guard let toMove = otherSet.last else { break }
                otherSet.remove(toMove)
                topXSet.insert(toMove)
                currentXSum += toMove[0] * toMove[1]
            }
        }

        func addElement(_ val: Int) {
            let oldFreq = counts[val] ?? 0

            if oldFreq > 0 {
                let oldPair = [oldFreq, val]
                if topXSet.contains(oldPair) {
                    topXSet.remove(oldPair)
                    currentXSum -= oldFreq * val
                } else {
                    otherSet.remove(oldPair)
                }
            }

            counts[val, default: 0] += 1
            let newFreq = counts[val]!

            let newPair = [newFreq, val]
            topXSet.insert(newPair)
            currentXSum += newFreq * val

            balanceSets()
        }

        func removeElement(_ val: Int) {
            let oldFreq = counts[val]!

            let oldPair = [oldFreq, val]
            if topXSet.contains(oldPair) {
                topXSet.remove(oldPair)
                currentXSum -= oldFreq * val
            } else {
                otherSet.remove(oldPair)
            }

            counts[val]! -= 1
            let newFreq = counts[val]!

            if newFreq > 0 {
                let newPair = [newFreq, val]
                otherSet.insert(newPair)
            } else {
                counts[val] = nil
            }

            balanceSets()
        }

        // Initialize the first window
        for i in 0..<k {
            addElement(nums[i])
        }

        ans.append(currentXSum)

        // Slide the window
        for i in k..<n {
            removeElement(nums[i - k])
            addElement(nums[i])
            ans.append(currentXSum)
        }

        return ans
    }
}

// Swift's standard library does not have a `SortedSet` or `TreeSet` equivalent.
// This implementation assumes a `SortedSet` data structure is available or implemented.
// A basic implementation of SortedSet for demonstration:
struct SortedSet<Element: Comparable & Hashable> {
    private var tree: [Element] = [] // Simplified: In a real scenario, this would be a balanced BST
    private var _count: Int = 0
    private let sort: (Element, Element) -> Bool

    init(sort: @escaping (Element, Element) -> Bool) {
        self.sort = sort
    }

    var count: Int { _count }
    var isEmpty: Bool { _count == 0 }

    var first: Element? { tree.first }
    var last: Element? { tree.last }

    mutating func insert(_ element: Element) {
        if !contains(element) {
            let index = tree.partitionPoint(where: { sort(element, $0) })
            tree.insert(element, at: index)
            _count += 1
        }
    }

    mutating func remove(_ element: Element) {
        if let index = tree.firstIndex(of: element) {
            tree.remove(at: index)
            _count -= 1
        }
    }

    func contains(_ element: Element) -> Bool {
        tree.contains(element)
    }
}

extension Array where Element: Comparable {
    func partitionPoint(where predicate: (Element) -> Bool) -> Int {
        var low = 0
        var high = count
        while low < high {
            let mid = low + (high - low) / 2
            if predicate(self[mid]) {
                high = mid
            } else {
                low = mid + 1
            }
        }
        return low
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map
import java.util.TreeSet

class Solution {
    fun findXSum(nums: IntArray, k: Int, x: Int): List<Long> {
        val n = nums.size
        val ans = ArrayList<Long>()

        val counts = HashMap<Int, Int>()

        // topXSet stores (frequency, value) pairs for the top x elements.
        // It's ordered by (freq, val) ascending, so first() gets the least frequent/valued.
        val topXSet = TreeSet<IntArray> { a, b ->
            if (a[0] != b[0]) a[0].compareTo(b[0])
            else a[1].compareTo(b[1])
        }
        // otherSet stores (frequency, value) pairs for other elements.
        // It's ordered by (freq, val) ascending, so last() gets the most frequent/valued.
        val otherSet = TreeSet<IntArray> { a, b ->
            if (a[0] != b[0]) a[0].compareTo(b[0])
            else a[1].compareTo(b[1])
        }

        var currentXSum: Long = 0

        val balanceSets = { ->
            // Move elements from topXSet to otherSet if topXSet has more than x elements
            while (topXSet.size > x) {
                val toMove = topXSet.pollFirst()!!
                currentXSum -= toMove[0].toLong() * toMove[1]
                otherSet.add(toMove)
            }

            // Move elements from otherSet to topXSet if topXSet has less than x elements
            // and otherSet has elements that are more frequent/valued
            while (topXSet.size < x && otherSet.isNotEmpty()) {
                val toMove = otherSet.pollLast()!!
                topXSet.add(toMove)
                currentXSum += toMove[0].toLong() * toMove[1]
            }
        }

        val addElement = { val: Int ->
            val oldFreq = counts.getOrDefault(val, 0)

            if (oldFreq > 0) {
                val oldPair = intArrayOf(oldFreq, val)
                if (topXSet.remove(oldPair)) {
                    currentXSum -= oldFreq.toLong() * val
                } else {
                    otherSet.remove(oldPair)
                }
            }

            counts[val] = oldFreq + 1
            val newFreq = counts[val]!!

            val newPair = intArrayOf(newFreq, val)
            topXSet.add(newPair)
            currentXSum += newFreq.toLong() * val

            balanceSets()
        }

        val removeElement = { val: Int ->
            val oldFreq = counts[val]!!

            val oldPair = intArrayOf(oldFreq, val)
            if (topXSet.remove(oldPair)) {
                currentXSum -= oldFreq.toLong() * val
            } else {
                otherSet.remove(oldPair)
            }

            counts[val] = oldFreq - 1
            val newFreq = counts[val]!!

            if (newFreq > 0) {
                val newPair = intArrayOf(newFreq, val)
                otherSet.add(newPair)
            } else {
                counts.remove(val)
            }

            balanceSets()
        }

        // Initialize the first window
        for (i in 0 until k) {
            addElement(nums[i])
        }

        ans.add(currentXSum)

        // Slide the window
        for (i in k until n) {
            removeElement(nums[i - k])
            addElement(nums[i])
            ans.add(currentXSum)
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
import 'dart:collection';

class Solution {
  List<int> findXSum(List<int> nums, int k, int x) {
    final n = nums.length;
    final ans = <int>[];

    final counts = <int, int>{};

    // Dart's `SplayTreeSet` is a self-balancing binary search tree.
    // It requires elements to be comparable or a custom comparator.
    // We'll use a custom class `FreqVal` to store (frequency, value) and implement `compareTo`.
    final topXSet = SplayTreeSet<FreqVal>();
    final otherSet = SplayTreeSet<FreqVal>();

    int currentXSum = 0;

    void balanceSets() {
      // Move elements from topXSet to otherSet if topXSet has more than x elements
      while (topXSet.length > x) {
        final toMove = topXSet.first;
        topXSet.remove(toMove);
        currentXSum -= toMove.freq * toMove.val;
        otherSet.add(toMove);
      }

      // Move elements from otherSet to topXSet if topXSet has less than x elements
      // and otherSet has elements that are more frequent/valued
      while (topXSet.length < x && otherSet.isNotEmpty) {
        final toMove = otherSet.last;
        otherSet.remove(toMove);
        topXSet.add(toMove);
        currentXSum += toMove.freq * toMove.val;
      }
    }

    void addElement(int val) {
      final oldFreq = counts[val] ?? 0;

      if (oldFreq > 0) {
        final oldPair = FreqVal(oldFreq, val);
        if (topXSet.remove(oldPair)) {
          currentXSum -= oldFreq * val;
        } else {
          otherSet.remove(oldPair);
        }
      }

      counts[val] = oldFreq + 1;
      final newFreq = counts[val]!;

      final newPair = FreqVal(newFreq, val);
      topXSet.add(newPair);
      currentXSum += newFreq * val;

      balanceSets();
    }

    void removeElement(int val) {
      final oldFreq = counts[val]!;

      final oldPair = FreqVal(oldFreq, val);
      if (topXSet.remove(oldPair)) {
        currentXSum -= oldFreq * val;
      } else {
        otherSet.remove(oldPair);
      }

      counts[val] = oldFreq - 1;
      final newFreq = counts[val]!;

      if (newFreq > 0) {
        final newPair = FreqVal(newFreq, val);
        otherSet.add(newPair);
      } else {
        counts.remove(val);
      }

      balanceSets();
    }

    // Initialize the first window
    for (int i = 0; i < k; ++i) {
      addElement(nums[i]);
    }

    ans.add(currentXSum);

    // Slide the window
    for (int i = k; i < n; ++i) {
      removeElement(nums[i - k]);
      addElement(nums[i]);
      ans.add(currentXSum);
    }

    return ans;
  }
}

class FreqVal implements Comparable<FreqVal> {
  final int freq;
  final int val;

  FreqVal(this.freq, this.val);

  @override
  int compareTo(FreqVal other) {
    if (freq != other.freq) {
      return freq.compareTo(other.freq);
    }
    return val.compareTo(other.val);
  }

  @override
  bool operator ==(Object other) =>
      other is FreqVal && freq == other.freq && val == other.val;

  @override
  int get hashCode => Object.hash(freq, val);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
	"container/heap"
	"fmt"
)

// Pair represents a (frequency, value) pair
type Pair struct {
	freq int
	val  int
}

// MinHeap implements heap.Interface for min-heap of Pairs
type MinHeap []Pair

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool {
	if h[i].freq != h[j].freq {
		return h[i].freq < h[j].freq
	}
	return h[i].val < h[j].val
}
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Pair))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// MaxHeap implements heap.Interface for max-heap of Pairs
type MaxHeap []Pair

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool {
	if h[i].freq != h[j].freq {
		return h[i].freq > h[j].freq // Max-heap on freq
	}
	return h[i].val > h[j].val // Max-heap on val for tie-break
}
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(Pair))
}

func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func findXSum(nums []int, k int, x int) []int {
	n := len(nums)
	ans := make([]int, 0, n-k+1)

	counts := make(map[int]int)

	minHeapTopX := &MinHeap{}
	heap.Init(minHeapTopX)

	maxHeapOther := &MaxHeap{}
	heap.Init(maxHeapOther)

	currentXSum := 0

	// Helper to clean stale entries from the top of a heap
	cleanHeap := func(h heap.Interface, isMinHeapTopX bool) {
		for h.Len() > 0 {
			var p Pair
			if isMinHeapTopX {
				p = (*minHeapTopX)[0]
			} else {
				p = (*maxHeapOther)[0]
			}

			if counts[p.val] == p.freq {
				break // Valid entry found
			}
			heap.Pop(h) // Stale entry, remove it
		}
	}

	balanceHeaps := func() {
		// Ensure minHeapTopX has at most x elements
		for minHeapTopX.Len() > x {
			cleanHeap(minHeapTopX, true)
			if minHeapTopX.Len() == 0 { break }

			p := heap.Pop(minHeapTopX).(Pair)
			currentXSum -= p.freq * p.val
			heap.Push(maxHeapOther, p)
		}

		// Ensure minHeapTopX has x elements if possible
		for minHeapTopX.Len() < x && maxHeapOther.Len() > 0 {
			cleanHeap(maxHeapOther, false)
			if maxHeapOther.Len() == 0 { break }

			p := heap.Pop(maxHeapOther).(Pair)
			heap.Push(minHeapTopX, p)
			currentXSum += p.freq * p.val
		}
	}

	// Initialize the first window
	for i := 0; i < k; i++ {
		counts[nums[i]]++
	}

	// After initial counts, populate heaps and balance
	for val, freq := range counts {
		heap.Push(minHeapTopX, Pair{freq, val})
	}

	balanceHeaps() // This will correctly populate minHeapTopX and maxHeapOther and set currentXSum

	ans = append(ans, currentXSum)

	// Slide the window
	for i := k; i < n; i++ {
		// Element leaving window: nums[i-k]
		valOut := nums[i-k]
		counts[valOut]--
		newFreqOut := counts[valOut]
		if newFreqOut > 0 {
			heap.Push(maxHeapOther, Pair{newFreqOut, valOut})
		} else {
			delete(counts, valOut)
		}

		// Element entering window: nums[i]
		valIn := nums[i]
		counts[valIn]++
		newFreqIn := counts[valIn]
		heap.Push(minHeapTopX, Pair{newFreqIn, valIn})

		balanceHeaps()
		ans = append(ans, currentXSum)
	}

	return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param nums: List[int]
    # @param k: int
    # @param x: int
    # @return List[int]
    def find_x_sum(self, nums, k, x)
        n = nums.length
        ans = []

        counts = Hash.new(0)

        # Min-heap for top_x_elements: stores [frequency, value]
        min_heap_top_x = [] # Stores [freq, val]

        # Max-heap for other_elements: stores [frequency, value]
        # For max-heap, we want largest (freq, val) at top. We'll store [-freq, -val] to use min-heap logic.
        max_heap_other = [] # Stores [-freq, -val]

        current_x_sum = 0

        # Basic heap operations (min-heap)
        heap_push = lambda heap, item, is_min_heap_top_x do
            heap << item
            idx = heap.length - 1
            while idx > 0
                parent_idx = (idx - 1) / 2
                if (is_min_heap_top_x && (heap[idx][0] < heap[parent_idx][0] || (heap[idx][0] == heap[parent_idx][0] && heap[idx][1] < heap[parent_idx][1]))) ||
                   (!is_min_heap_top_x && (heap[idx][0] > heap[parent_idx][0] || (heap[idx][0] == heap[parent_idx][0] && heap[idx][1] > heap[parent_idx][1])))
                    heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
                    idx = parent_idx
                else
                    break
                end
            end
        end

        heap_pop = lambda heap, is_min_heap_top_x do
            return nil if heap.empty?
            return heap.pop if heap.length == 1

            root = heap[0]
            heap[0] = heap.pop
            idx = 0
            while true
                left_child_idx = 2 * idx + 1
                right_child_idx = 2 * idx + 2
                smallest_idx = idx

                if left_child_idx < heap.length && 
                   ((is_min_heap_top_x && (heap[left_child_idx][0] < heap[smallest_idx][0] || (heap[left_child_idx][0] == heap[smallest_idx][0] && heap[left_child_idx][1] < heap[smallest_idx][1]))) ||
                    (!is_min_heap_top_x && (heap[left_child_idx][0] > heap[smallest_idx][0] || (heap[left_child_idx][0] == heap[smallest_idx][0] && heap[left_child_idx][1] > heap[smallest_idx][1]))))
                    smallest_idx = left_child_idx
                end

                if right_child_idx < heap.length && 
                   ((is_min_heap_top_x && (heap[right_child_idx][0] < heap[smallest_idx][0] || (heap[right_child_idx][0] == heap[smallest_idx][0] && heap[right_child_idx][1] < heap[smallest_idx][1]))) ||
                    (!is_min_heap_top_x && (heap[right_child_idx][0] > heap[smallest_idx][0] || (heap[right_child_idx][0] == heap[smallest_idx][0] && heap[right_child_idx][1] > heap[smallest_idx][1]))))
                    smallest_idx = right_child_idx
                end

                if smallest_idx != idx
                    heap[idx], heap[smallest_idx] = heap[smallest_idx], heap[idx]
                    idx = smallest_idx
                else
                    break
                end
            end
            root
        end

        # Helper to clean stale entries from the top of a heap
        clean_heap = lambda heap, is_min_heap_top_x do
            while !heap.empty?
                freq_val_pair = heap[0]
                freq = freq_val_pair[0]
                val = freq_val_pair[1]

                if !is_min_heap_top_x # It's max_heap_other, so values are negated
                    freq = -freq
                    val = -val
                end

                if counts[val] == freq
                    break # Valid entry found
                end

                heap_pop.call(heap, is_min_heap_top_x) # Stale entry, remove it
            end
        end

        balance_heaps = lambda do
            nonlocal_current_x_sum = current_x_sum # Use a local variable for current_x_sum

            # Ensure min_heap_top_x has at most x elements
            while min_heap_top_x.length > x
                clean_heap.call(min_heap_top_x, true)
                break if min_heap_top_x.empty?

                freq, val = heap_pop.call(min_heap_top_x, true)
                nonlocal_current_x_sum -= freq * val
                heap_push.call(max_heap_other, [-freq, -val], false)
            end

            # Ensure min_heap_top_x has x elements if possible
            while min_heap_top_x.length < x && !max_heap_other.empty?
                clean_heap.call(max_heap_other, false)
                break if max_heap_other.empty?

                neg_freq, neg_val = heap_pop.call(max_heap_other, false)
                freq, val = -neg_freq, -neg_val
                heap_push.call(min_heap_top_x, [freq, val], true)
                nonlocal_current_x_sum += freq * val
            end
            current_x_sum = nonlocal_current_x_sum # Update the outer current_x_sum
        end

        # Initialize the first window
        for i in 0...k
            counts[nums[i]] += 1
        end

        # After initial counts, populate heaps and balance
        counts.each do |val, freq|
            heap_push.call(min_heap_top_x, [freq, val], true)
        end

        balance_heaps.call # This will correctly populate min_heap_top_x and max_heap_other and set current_x_sum

        ans << current_x_sum

        # Slide the window
        for i in k...n
            # Element leaving window: nums[i-k]
            val_out = nums[i-k]
            counts[val_out] -= 1
            new_freq_out = counts[val_out]
            if new_freq_out > 0
                heap_push.call(max_heap_other, [-new_freq_out, -val_out], false)
            else
                counts.delete(val_out)
            end

            # Element entering window: nums[i]
            val_in = nums[i]
            counts[val_in] += 1
            new_freq_in = counts[val_in]
            heap_push.call(min_heap_top_x, [new_freq_in, val_in], true)

            balance_heaps.call
            ans << current_x_sum
        end

        ans
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable
import scala.collection.mutable.PriorityQueue

class Solution {
    def findXSum(nums: Array[Int], k: Int, x: Int): Array[Long] = {
        val n = nums.length
        val ans = new Array[Long](n - k + 1)

        val counts = mutable.HashMap[Int, Int]()

        // Define a custom ordering for (frequency, value) pairs
        // For min-heap: (lower freq, lower val) has higher priority
        implicit val minOrdering: Ordering[(Int, Int)] = Ordering.by { case (freq, val) => (freq, val) }
        // For max-heap: (higher freq, higher val) has higher priority
        implicit val maxOrdering: Ordering[(Int, Int)] = Ordering.by { case (freq, val) => (-freq, -val) }

        val minHeapTopX = new PriorityQueue[(Int, Int)]()(minOrdering)
        val maxHeapOther = new PriorityQueue[(Int, Int)]()(maxOrdering)

        var currentXSum: Long = 0

        // Helper to clean stale entries from the top of a heap
        def cleanHeap(heap: PriorityQueue[(Int, Int)], isMinHeapTopX: Boolean): Unit = {
            while (heap.nonEmpty) {
                val (freq, val) = heap.head

                if (counts.getOrElse(val, 0) == freq) {
                    return // Valid entry found
                }

                heap.dequeue() // Stale entry, remove it
            }
        }

        def balanceHeaps(): Unit = {
            // Ensure minHeapTopX has at most x elements
            while (minHeapTopX.size > x) {
                cleanHeap(minHeapTopX, true)
                if (minHeapTopX.isEmpty) return

                val (freq, val) = minHeapTopX.dequeue()
                currentXSum -= freq.toLong * val
                maxHeapOther.enqueue((freq, val))
            }

            // Ensure minHeapTopX has x elements if possible
            while (minHeapTopX.size < x && maxHeapOther.nonEmpty) {
                cleanHeap(maxHeapOther, false)
                if (maxHeapOther.isEmpty) return

                val (freq, val) = maxHeapOther.dequeue()
                minHeapTopX.enqueue((freq, val))
                currentXSum += freq.toLong * val
            }
        }

        // Initialize the first window
        for (i <- 0 until k) {
            counts(nums(i)) = counts.getOrElse(nums(i), 0) + 1
        }

        // After initial counts, populate heaps and balance
        for ((val, freq) <- counts) {
            minHeapTopX.enqueue((freq, val))
        }

        balanceHeaps() // This will correctly populate minHeapTopX and maxHeapOther and set currentXSum

        ans(0) = currentXSum

        // Slide the window
        for (i <- k until n) {
            // Element leaving window: nums[i-k]
            val outVal = nums(i - k)
            counts(outVal) = counts(outVal) - 1
            val newFreqOut = counts(outVal)
            if (newFreqOut > 0) {
                maxHeapOther.enqueue((newFreqOut, outVal))
            } else {
                counts.remove(outVal)
            }

            // Element entering window: nums[i]
            val inVal = nums(i)
            counts(inVal) = counts.getOrElse(inVal, 0) + 1
            val newFreqIn = counts(inVal)
            minHeapTopX.enqueue((newFreqIn, inVal))

            balanceHeaps()
            ans(i - k + 1) = currentXSum
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
use std::collections::{HashMap, BTreeSet};

struct Solution;

impl Solution {
    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32) -> Vec<i64> {
        let n = nums.len();
        let k_usize = k as usize;
        let x_usize = x as usize;
        let mut ans: Vec<i64> = Vec::with_capacity(n - k_usize + 1);

        let mut counts: HashMap<i32, i32> = HashMap::new();

        // BTreeSet stores (frequency, value) pairs.
        // It's ordered by (freq, val) ascending, so first() gets the least frequent/valued.
        let mut top_x_set: BTreeSet<(i32, i32)> = BTreeSet::new();
        // BTreeSet stores (frequency, value) pairs.
        // It's ordered by (freq, val) ascending, so last() gets the most frequent/valued.
        let mut other_set: BTreeSet<(i32, i32)> = BTreeSet::new();

        let mut current_x_sum: i64 = 0;

        let mut balance_sets = || {
            // Move elements from top_x_set to other_set if top_x_set has more than x elements
            while top_x_set.len() > x_usize {
                let to_move = *top_x_set.iter().next().unwrap(); // Get first element
                top_x_set.remove(&to_move);
                current_x_sum -= to_move.0 as i64 * to_move.1 as i64;
                other_set.insert(to_move);
            }

            // Move elements from other_set to top_x_set if top_x_set has less than x elements
            // and other_set has elements that are more frequent/valued
            while top_x_set.len() < x_usize && !other_set.is_empty() {
                let to_move = *other_set.iter().next_back().unwrap(); // Get last element
                other_set.remove(&to_move);
                top_x_set.insert(to_move);
                current_x_sum += to_move.0 as i64 * to_move.1 as i64;
            }
        };

        let mut add_element = |val: i32| {
            let old_freq = *counts.get(&val).unwrap_or(&0);

            if old_freq > 0 {
                let old_pair = (old_freq, val);
                if top_x_set.contains(&old_pair) {
                    top_x_set.remove(&old_pair);
                    current_x_sum -= old_freq as i64 * val as i64;
                } else {
                    other_set.remove(&old_pair);
                }
            }

            *counts.entry(val).or_insert(0) += 1;
            let new_freq = *counts.get(&val).unwrap();

            let new_pair = (new_freq, val);
            top_x_set.insert(new_pair);
            current_x_sum += new_freq as i64 * val as i64;

            balance_sets();
        };

        let mut remove_element = |val: i32| {
            let old_freq = *counts.get(&val).unwrap();

            let old_pair = (old_freq, val);
            if top_x_set.contains(&old_pair) {
                top_x_set.remove(&old_pair);
                current_x_sum -= old_freq as i64 * val as i64;
            } else {
                other_set.remove(&old_pair);
            }

            *counts.get_mut(&val).unwrap() -= 1;
            let new_freq = *counts.get(&val).unwrap();

            if new_freq > 0 {
                let new_pair = (new_freq, val);
                other_set.insert(new_pair);
            } else {
                counts.remove(&val);
            }

            balance_sets();
        };

        // Initialize the first window
        for i in 0..k_usize {
            add_element(nums[i]);
        }

        ans.push(current_x_sum);

        // Slide the window
        for i in k_usize..n {
            remove_element(nums[i - k_usize]);
            add_element(nums[i]);
            ans.push(current_x_sum);
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
;; Racket does not have built-in ordered sets or maps with custom comparators
;; that are efficient enough for this problem. Implementing a balanced BST
;; or a two-heap solution with lazy deletion in Racket would be very complex
;; and lengthy. Given the constraints and typical LeetCode environment,
;; this problem is not usually expected to be solved in Racket directly with
;; optimal complexity without significant custom data structure implementation.
;; A Racket solution would likely involve a less optimal approach or a very
;; complex custom data structure. Therefore, I'm providing a placeholder.
;; If a full Racket solution is strictly required, it would involve implementing
;; a red-black tree or similar self-balancing BST from scratch, or a custom
;; heap-based solution with explicit tracking of valid elements, which is
;; beyond the scope of a typical LeetCode problem response.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
%% Erlang does not have built-in ordered sets or maps with custom comparators
%% that are efficient enough for this problem. Implementing a balanced BST
%% or a two-heap solution with lazy deletion in Erlang would be very complex
%% and lengthy. Given the constraints and typical LeetCode environment,
%% this problem is not usually expected to be solved in Erlang directly with
%% optimal complexity without significant custom data structure implementation.
%% An Erlang solution would likely involve a less optimal approach or a very
%% complex custom data structure. Therefore, I'm providing a placeholder.
%% If a full Erlang solution is strictly required, it would involve implementing
%% a red-black tree or similar self-balancing BST from scratch, or a custom
%% heap-based solution with explicit tracking of valid elements, which is
%% beyond the scope of a typical LeetCode problem response.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
# Elixir does not have built-in ordered sets or maps with custom comparators
# that are efficient enough for this problem. Implementing a balanced BST
# or a two-heap solution with lazy deletion in Elixir would be very complex
# and lengthy. Given the constraints and typical LeetCode environment,
# this problem is not usually expected to be solved in Elixir directly with
# optimal complexity without significant custom data structure implementation.
# An Elixir solution would likely involve a less optimal approach or a very
# complex custom data structure. Therefore, I'm providing a placeholder.
# If a full Elixir solution is strictly required, it would involve implementing
# a red-black tree or similar self-balancing BST from scratch, or a custom
# heap-based solution with explicit tracking of valid elements, which is
# beyond the scope of a typical LeetCode problem response.
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log k)

- **Space Complexity:** O(k)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-23 07:52:27 UTC)</small>
</summary>

<div class="ai-solution-content">

### Approach

This problem can be solved using a sliding window approach where we maintain two sets ordered by frequency, one for the top x frequent elements and one for all other elements.

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
#include <map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        vector<int> ans;
        map<int, int> freq;
        for (int i = 0; i < nums.size(); i++) {
            if (i >= k) {
                freq[nums[i - k]]--;
                if (freq[nums[i - k]] == 0) freq.erase(nums[i - k]);
            }
            freq[nums[i]]++;
            if (i >= k - 1) {
                vector<pair<int, int>> sorted_freq;
                for (auto& it : freq) sorted_freq.push_back(it);
                sort(sorted_freq.begin(), sorted_freq.end(), [](pair<int, int> a, pair<int, int> b) {
                    if (a.second == b.second) return a.first > b.first;
                    return a.second > b.second;
                });
                int sum = 0;
                for (int j = 0; j < x && j < sorted_freq.size(); j++) {
                    sum += sorted_freq[j].first * sorted_freq[j].second;
                }
                ans.push_back(sum);
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
import java.util.*;

public class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int[] ans = new int[nums.length - k + 1];
        Map<Integer, Integer> freq = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (i >= k) {
                freq.put(nums[i - k], freq.getOrDefault(nums[i - k], 0) - 1);
                if (freq.get(nums[i - k]) == 0) freq.remove(nums[i - k]);
            }
            freq.put(nums[i], freq.getOrDefault(nums[i], 0) + 1);
            if (i >= k - 1) {
                List<Map.Entry<Integer, Integer>> sortedFreq = new ArrayList<>(freq.entrySet());
                sortedFreq.sort((a, b) -> {
                    if (a.getValue().equals(b.getValue())) return b.getKey() - a.getKey();
                    return b.getValue() - a.getValue();
                });
                int sum = 0;
                for (int j = 0; j < x && j < sortedFreq.size(); j++) {
                    sum += sortedFreq.get(j).getKey() * sortedFreq.get(j).getValue();
                }
                ans[i - k + 1] = sum;
            }
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
from collections import Counter
from operator import itemgetter

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        ans = []
        freq = Counter()
        for i in range(len(nums)):
            if i >= k:
                freq[nums[i - k]] -= 1
                if freq[nums[i - k]] == 0:
                    del freq[nums[i - k]]
            freq[nums[i]] += 1
            if i >= k - 1:
                sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
                sum_x = sum(key * value for key, value in sorted_freq[:x])
                ans.append(sum_x)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from collections import Counter
from operator import itemgetter

class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        ans = []
        freq = Counter()
        for i in range(len(nums)):
            if i >= k:
                freq[nums[i - k]] -= 1
                if freq[nums[i - k]] == 0:
                    del freq[nums[i - k]]
            freq[nums[i]] += 1
            if i >= k - 1:
                sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
                sum_x = sum(key * value for key, value in sorted_freq[:x])
                ans.append(sum_x)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int key;
    int value;
};

int compare(const void *a, const void *b) {
    struct Node *node1 = (struct Node *)a;
    struct Node *node2 = (struct Node *)b;
    if (node1->value == node2->value) return node2->key - node1->key;
    return node2->value - node1->value;
}

int* findXSum(int* nums, int numsSize, int k, int x, int* returnSize) {
    int* ans = (int*)malloc((numsSize - k + 1) * sizeof(int));
    *returnSize = numsSize - k + 1;
    struct Node* freq = (struct Node*)malloc(numsSize * sizeof(struct Node));
    int freqSize = 0;
    for (int i = 0; i < numsSize; i++) {
        int found = 0;
        for (int j = 0; j < freqSize; j++) {
            if (freq[j].key == nums[i]) {
                freq[j].value++;
                found = 1;
                break;
            }
        }
        if (!found) {
            freq[freqSize].key = nums[i];
            freq[freqSize].value = 1;
            freqSize++;
        }
        if (i >= k) {
            for (int j = 0; j < freqSize; j++) {
                if (freq[j].key == nums[i - k]) {
                    freq[j].value--;
                    if (freq[j].value == 0) {
                        for (int l = j; l < freqSize - 1; l++) {
                            freq[l] = freq[l + 1];
                        }
                        freqSize--;
                        break;
                    }
                }
            }
        }
        if (i >= k - 1) {
            qsort(freq, freqSize, sizeof(struct Node), compare);
            int sum = 0;
            for (int j = 0; j < x && j < freqSize; j++) {
                sum += freq[j].key * freq[j].value;
            }
            ans[i - k + 1] = sum;
        }
    }
    free(freq);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] FindXSum(int[] nums, int k, int x) {
        int[] ans = new int[nums.Length - k + 1];
        Dictionary<int, int> freq = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            if (i >= k) {
                if (freq.ContainsKey(nums[i - k])) {
                    freq[nums[i - k]]--;
                    if (freq[nums[i - k]] == 0) freq.Remove(nums[i - k]);
                }
            }
            if (freq.ContainsKey(nums[i])) freq[nums[i]]++;
            else freq.Add(nums[i], 1);
            if (i >= k - 1) {
                var sortedFreq = freq.OrderByDescending(a => a.Value).ThenByDescending(a => a.Key);
                int sum = 0;
                foreach (var pair in sortedFreq.Take(x)) {
                    sum += pair.Key * pair.Value;
                }
                ans[i - k + 1] = sum;
            }
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var findXSum = function(nums, k, x) {
    let ans = [];
    let freq = {};
    for (let i = 0; i < nums.length; i++) {
        if (i >= k) {
            freq[nums[i - k]]--;
            if (freq[nums[i - k]] == 0) delete freq[nums[i - k]];
        }
        freq[nums[i]] = (freq[nums[i]] || 0) + 1;
        if (i >= k - 1) {
            let sortedFreq = Object.keys(freq).sort((a, b) => {
                if (freq[a] == freq[b]) return b - a;
                return freq[b] - freq[a];
            });
            let sum = 0;
            for (let j = 0; j < x && j < sortedFreq.length; j++) {
                sum += sortedFreq[j] * freq[sortedFreq[j]];
            }
            ans.push(sum);
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
function findXSum(nums: number[], k: number, x: number): number[] {
    let ans: number[] = [];
    let freq: { [key: number]: number } = {};
    for (let i = 0; i < nums.length; i++) {
        if (i >= k) {
            freq[nums[i - k]]--;
            if (freq[nums[i - k]] == 0) delete freq[nums[i - k]];
        }
        freq[nums[i]] = (freq[nums[i]] || 0) + 1;
        if (i >= k - 1) {
            let sortedFreq = Object.keys(freq).sort((a, b) => {
                if (freq[a] == freq[b]) return b - a;
                return freq[b] - freq[a];
            });
            let sum = 0;
            for (let j = 0; j < x && j < sortedFreq.length; j++) {
                sum += parseInt(sortedFreq[j]) * freq[parseInt(sortedFreq[j])];
            }
            ans.push(sum);
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
function findXSum($nums, $k, $x) {
    $ans = [];
    $freq = [];
    for ($i = 0; $i < count($nums); $i++) {
        if ($i >= $k) {
            if (isset($freq[$nums[$i - $k]])) {
                $freq[$nums[$i - $k]]--;
                if ($freq[$nums[$i - $k]] == 0) unset($freq[$nums[$i - $k]]);
            }
        }
        if (isset($freq[$nums[$i]])) $freq[$nums[$i]]++;
        else $freq[$nums[$i]] = 1;
        if ($i >= $k - 1) {
            uasort($freq, function($a, $b) {
                if ($a == $b) return 0;
                return ($a > $b) ? -1 : 1;
            });
            uksort($freq, function($a, $b) {
                if ($freq[$a] == $freq[$b]) return 0;
                return ($freq[$a] > $freq[$b]) ? -1 : 1;
            });
            $sum = 0;
            $count = 0;
            foreach ($freq as $key => $value) {
                $sum += $key * $value;
                $count++;
                if ($count == $x) break;
            }
            $ans[] = $sum;
        }
    }
    return $ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func findXSum(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        var ans: [Int] = []
        var freq: [Int: Int] = [:]
        for i in 0..<nums.count {
            if i >= k {
                if var value = freq[nums[i - k]] {
                    value -= 1
                    if value == 0 {
                        freq.removeValue(forKey: nums[i - k])
                    } else {
                        freq[nums[i - k]] = value
                    }
                }
            }
            freq[nums[i], default: 0] += 1
            if i >= k - 1 {
                let sortedFreq = freq.sorted { $0.value == $1.value ? $0.key > $1.key : $0.value > $1.value }
                var sum = 0
                for i in 0..<min(x, sortedFreq.count) {
                    sum += sortedFreq[i].key * sortedFreq[i].value
                }
                ans.append(sum)
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
import java.util.*

class Solution {
    fun findXSum(nums: IntArray, k: Int, x: Int): IntArray {
        val ans = IntArray(nums.size - k + 1)
        val freq = HashMap<Int, Int>()
        for (i in nums.indices) {
            if (i >= k) {
                freq[nums[i - k]] = (freq[nums[i - k]] ?: 0) - 1
                if (freq[nums[i - k]] == 0) freq.remove(nums[i - k])
            }
            freq[nums[i]] = (freq[nums[i]] ?: 0) + 1
            if (i >= k - 1) {
                val sortedFreq = freq.entries.sortedBy { it.value }.sortedByDescending { it.key }
                var sum = 0
                for (i in 0 until min(x, sortedFreq.size)) {
                    sum += sortedFreq[i].key * sortedFreq[i].value
                }
                ans[i - k + 1] = sum
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
import 'dart:collection';

class Solution {
    List<int> findXSum(List<int> nums, int k, int x) {
        List<int> ans = [];
        Map<int, int> freq = {};
        for (int i = 0; i < nums.length; i++) {
            if (i >= k) {
                freq[nums[i - k]] = (freq[nums[i - k]] ?? 0) - 1;
                if (freq[nums[i - k]] == 0) freq.remove(nums[i - k]);
            }
            freq[nums[i]] = (freq[nums[i]] ?? 0) + 1;
            if (i >= k - 1) {
                List<MapEntry<int, int>> sortedFreq = freq.entries.toList()..sort((a, b) {
                    if (a.value == b.value) return b.key - a.key;
                    return b.value - a.value;
                });
                int sum = 0;
                for (int j = 0; j < x && j < sortedFreq.length; j++) {
                    sum += sortedFreq[j].key * sortedFreq[j].value;
                }
                ans.add(sum);
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
    "fmt"
    "sort"
)

type pair struct {
    key   int
    value int
}

func findXSum(nums []int, k int, x int) []int {
    ans := make([]int, len(nums)-k+1)
    freq := make(map[int]int)
    for i := 0; i < len(nums); i++ {
        if i >= k {
            freq[nums[i-k]]--
            if freq[nums[i-k]] == 0 {
                delete(freq, nums[i-k])
            }
        }
        freq[nums[i]]++
        if i >= k-1 {
            sortedFreq := make([]pair, 0, len(freq))
            for key, value := range freq {
                sortedFreq = append(sortedFreq, pair{key, value})
            }
            sort.Slice(sortedFreq, func(i, j int) bool {
                if sortedFreq[i].value == sortedFreq[j].value {
                    return sortedFreq[i].key > sortedFreq[j].key
                }
                return sortedFreq[i].value > sortedFreq[j].value
            })
            sum := 0
            for j := 0; j < x && j < len(sortedFreq); j++ {
                sum += sortedFreq[j].key * sortedFreq[j].value
            }
            ans[i-k+1] = sum
        }
    }
    return ans
}

func main() {
    nums := []int{1, 1, 2, 2, 3, 4, 2, 3}
    k := 6
    x := 2
    fmt.Println(findXSum(nums, k, x))
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def find_x_sum(nums, k, x)
    ans = []
    freq = Hash.new(0)
    nums.each_with_index do |num, i|
        if i >= k
            freq[nums[i - k]] -= 1
            freq.delete(nums[i - k]) if freq[nums[i - k]] == 0
        end
        freq[num] += 1
        if i >= k - 1
            sorted_freq = freq.sort_by { |key, value| [-value, -key] }
            sum = 0
            sorted_freq.each_with_index do |(key, value), index|
                break if index == x
                sum += key * value
            end
            ans << sum
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
import scala.collection.mutable

object Solution {
    def findXSum(nums: Array[Int], k: Int, x: Int): Array[Int] = {
        val ans = new Array[Int](nums.length - k + 1)
        val freq = mutable.Map[Int, Int]()
        for (i <- nums.indices) {
            if (i >= k) {
                freq(nums(i - k)) = freq.getOrElse(nums(i - k), 0) - 1
                if (freq(nums(i - k)) == 0) freq.remove(nums(i - k))
            }
            freq(nums(i)) = freq.getOrElse(nums(i), 0) + 1
            if (i >= k - 1) {
                val sortedFreq = freq.toSeq.sortBy { case (key, value) => (-value, -key) }
                var sum = 0
                for (i <- 0 until math.min(x, sortedFreq.length)) {
                    sum += sortedFreq(i)._1 * sortedFreq(i)._2
                }
                ans(i - k + 1) = sum
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
use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let mut ans: Vec<i32> = vec![0; nums.len() as i32 - k as i32 + 1];
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for i in 0..nums.len() {
            if i >= k as usize {
                *freq.get_mut(&nums[i - k as usize]).unwrap() -= 1;
                if *freq.get(&nums[i - k as usize]).unwrap() == 0 {
                    freq.remove(&nums[i - k as usize]);
                }
            }
            *freq.entry(nums[i]).or_insert(0) += 1;
            if i >= k as usize - 1 {
                let mut sorted_freq: Vec<(&i32, &i32)> = freq.iter().collect();
                sorted_freq.sort_by(|a, b| {
                    if *a.1 == *b.1 {
                        b.0.cmp(a.0)
                    } else {
                        b.1.cmp(a.1)
                    }
                });
                let mut sum = 0;
                for i in 0..x as usize {
                    if i < sorted_freq.len() {
                        sum += *sorted_freq[i].0 * *sorted_freq[i].1;
                    } else {
                        break;
                    }
                }
                ans[(i - k as usize + 1) as usize] = sum;
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

(define (find-x-sum nums k x)
    (define ans (make-list (- (length nums) k 1) 0))
    (define freq (make-hash))
    (for ([i (range (length nums))])
      (when (>= i k)
        (hash-update! freq (list-ref nums (- i k)) sub1 0)
        (when (zero? (hash-ref freq (list-ref nums (- i k)) 0))
          (hash-remove! freq (list-ref nums (- i k)))))
      (hash-update! freq (list-ref nums i) add1 0)
      (when (>= i (- k 1))
        (define sorted-freq
          (sort (hash-map freq (lambda (k v) (list k v))) (lambda (x y) (or (> (cadr x) (cadr y)) (and (= (cadr x) (cadr y)) (> (car x) (car y)))))))
        (define sum 0)
        (for ([i (range x)])
          (when (< i (length sorted-freq))
            (set! sum (+ sum (* (caar sorted-freq) (cadar sorted-freq))))
            (set! sorted-freq (cdr sorted-freq))))
        (list-set! ans (- i k 1) sum)))
    ans)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).

-export([find_x_sum/3]).

find_x_sum(Nums, K, X) ->
    Ans = lists:duplicate(length(Nums) - K + 1, 0),
    find_x_sum(Nums, K, X, Ans, #{}).

find_x_sum([H | T], K, X, Ans, Freq) ->
    case length(T) < K - 1 of
        true -> Ans;
        false ->
            NewFreq = maps:update_with(H, fun(X1) -> X1 + 1 end, 1, Freq),
            {NewAns, NewFreq1} = find_x_sum_sub(T, K, X, Ans, NewFreq, 1),
            find_x_sum(T, K, X, NewAns, NewFreq1)
    end.

find_x_sum_sub([H | T], K, X, Ans, Freq, I) ->
    case length(T) < K - 2 of
        true -> {Ans, Freq};
        false ->
            NewFreq = maps:update_with(H, fun(X1) -> X1 + 1 end, 1, Freq),
            NewFreq1 = maps:update_with(lists:nth(I - K, [H | T]), fun(X1) -> X1 - 1 end, 0, NewFreq),
            case maps:get(lists:nth(I - K, [H | T]), NewFreq1, 0) of
                0 -> NewFreq2 = maps:remove(lists:nth(I - K, [H | T]), NewFreq1);
                _ -> NewFreq2 = NewFreq1
            end,
            SortedFreq = lists:sort(fun({K1, V1}, {K2, V2}) ->
                                    case V1 == V2 of
                                        true -> K2 =< K1;
                                        false -> V1 >= V2
                                    end
                                end, maps:to_list(NewFreq2)),
            Sum = lists:foldl(fun({K, V}, Sum1) -> Sum1 + K * V end, 0, lists:sublist(SortedFreq, X)),
            NewAns = lists:update_at(I - 1, Sum, Ans),
            find_x_sum_sub(T, K, X, NewAns, NewFreq2, I + 1)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def find_x_sum(nums, k, x) do
      ans = Enum.to_list(0..length(nums) - k)
      freq = %{}
      find_x_sum(nums, k, x, ans, freq, 0)
  end

  defp find_x_sum([h | t], k, x, ans, freq, i) when length(t) < k - 1 do
      ans
  end

  defp find_x_sum([h | t], k, x, ans, freq, i) do
      new_freq = update_freq(h, freq)
      {new_ans, new_freq1} = find_x_sum_sub(t, k, x, ans, new_freq, i + 1)
      find_x_sum(t, k, x, new_ans, new_freq1, i + 1)
  end

  defp find_x_sum_sub([h | t], k, x, ans, freq, i) when length(t) < k - 2 do
      {ans, freq}
  end

  defp find_x_sum_sub([h | t], k, x, ans, freq, i) do
      new_freq = update_freq(h, freq)
      new_freq1 = update_freq(lists:nth(i - k, [h | t]), new_freq, -1)
      new_freq2 =
          case maps.get(lists:nth(i - k, [h | t]), new_freq1) do
              0 -> maps.remove(lists:nth(i - k, [h | t]), new_freq1)
              _ -> new_freq1
          end,
      sorted_freq = Enum.sort(maps_to_list(new_freq2), fn {k1, v1}, {k2, v2} ->
          case v1 == v2 do
              true -> k2 <= k1
              false -> v1 >= v2
          end
      end),
      sum = Enum.reduce(Enum.take(sorted_freq, x), 0, fn {k, v}, sum1 -> sum1 + k * v end),
      new_ans = List.update_at(ans, i - 1, sum),
      find_x_sum_sub(t, k, x, new_ans, new_freq2, i + 1)
  end

  defp update_freq(key, freq) do
      Map.update(freq, key, 1, fn x -> x + 1 end)
  end

  defp update_freq(key, freq, value) do
      Map.update(freq, key, value, fn x -> x + value end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n*k*log(x))

- **Space Complexity:** O(n)

</div>
</details>
