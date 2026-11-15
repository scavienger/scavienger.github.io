---
layout: post
title: "Number of Sub-arrays With Odd Sum"
date: 2026-11-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Dynamic Programming", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numOfSubarrays(vector<int>& arr) {\n\
        \        const int MOD = 1e9 + 7;\n        long long ans = 0;\n        int prefix\
        \ = 0;\n        int even_count = 1;\n        int odd_count = 0;\n\n        for\
        \ (int x : arr) {\n            prefix ^= (x & 1);\n            if (prefix ==\
        \ 1) {\n                ans = (ans + even_count) % MOD;\n                odd_count++;\n\
        \            } else {\n                ans = (ans + odd_count) % MOD;\n    \
        \            even_count++;\n            }\n        }\n\n        return ans;\n\
        \    }\n};"
      java: "class Solution {\n    public int numOfSubarrays(int[] arr) {\n        final\
        \ int MOD = 1_000_000_007;\n        long ans = 0;\n        int prefix = 0;\n\
        \        int evenCount = 1;\n        int oddCount = 0;\n\n        for (int x\
        \ : arr) {\n            prefix ^= (x & 1);\n            if (prefix == 1) {\n\
        \                ans = (ans + evenCount) % MOD;\n                oddCount++;\n\
        \            } else {\n                ans = (ans + oddCount) % MOD;\n     \
        \           evenCount++;\n            }\n        }\n\n        return (int) ans;\n\
        \    }\n}"
      python: "class Solution(object):\n    def numOfSubarrays(self, arr):\n       \
        \ \"\"\"\n        :type arr: List[int]\n        :rtype: int\n        \"\"\"\n\
        \        MOD = 10**9 + 7\n        ans = 0\n        prefix = 0\n        even_count\
        \ = 1\n        odd_count = 0\n\n        for x in arr:\n            prefix ^=\
        \ (x & 1)\n            if prefix == 1:\n                ans = (ans + even_count)\
        \ % MOD\n                odd_count += 1\n            else:\n               \
        \ ans = (ans + odd_count) % MOD\n                even_count += 1\n\n       \
        \ return ans"
      python3: "class Solution:\n    def numOfSubarrays(self, arr: list[int]) -> int:\n\
        \        MOD = 10**9 + 7\n        ans = 0\n        prefix = 0\n        even_count\
        \ = 1\n        odd_count = 0\n\n        for x in arr:\n            prefix ^=\
        \ (x & 1)\n            if prefix == 1:\n                ans = (ans + even_count)\
        \ % MOD\n                odd_count += 1\n            else:\n               \
        \ ans = (ans + odd_count) % MOD\n                even_count += 1\n\n       \
        \ return ans"
      c: "int numOfSubarrays(int* arr, int arrSize) {\n    const int MOD = 1000000007;\n\
        \    long long ans = 0;\n    int prefix = 0;\n    int even_count = 1;\n    int\
        \ odd_count = 0;\n\n    for (int i = 0; i < arrSize; i++) {\n        prefix\
        \ ^= (arr[i] & 1);\n        if (prefix == 1) {\n            ans = (ans + even_count)\
        \ % MOD;\n            odd_count++;\n        } else {\n            ans = (ans\
        \ + odd_count) % MOD;\n            even_count++;\n        }\n    }\n\n    return\
        \ (int)ans;\n}"
      csharp: "public class Solution {\n    public int NumOfSubarrays(int[] arr) {\n\
        \        const int MOD = 1000000007;\n        int ans = 0;\n        int prefix\
        \ = 0;\n        int evenCount = 1;\n        int oddCount = 0;\n\n        foreach\
        \ (int x in arr) {\n            prefix ^= (x & 1);\n            if (prefix ==\
        \ 1) {\n                ans = (ans + evenCount) % MOD;\n                oddCount++;\n\
        \            } else {\n                ans = (ans + oddCount) % MOD;\n     \
        \           evenCount++;\n            }\n        }\n\n        return ans;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} arr\n * @return {number}\n */\nvar numOfSubarrays\
        \ = function(arr) {\n    const MOD = 1000000007;\n    let ans = 0;\n    let\
        \ prefix = 0;\n    let evenCount = 1;\n    let oddCount = 0;\n\n    for (const\
        \ x of arr) {\n        prefix ^= (x & 1);\n        if (prefix === 1) {\n   \
        \         ans = (ans + evenCount) % MOD;\n            oddCount++;\n        }\
        \ else {\n            ans = (ans + oddCount) % MOD;\n            evenCount++;\n\
        \        }\n    }\n\n    return ans;\n};"
      typescript: "function numOfSubarrays(arr: number[]): number {\n    const MOD =\
        \ 1000000007;\n    let ans = 0;\n    let prefix = 0;\n    let evenCount = 1;\n\
        \    let oddCount = 0;\n\n    for (const x of arr) {\n        prefix ^= (x &\
        \ 1);\n        if (prefix === 1) {\n            ans = (ans + evenCount) % MOD;\n\
        \            oddCount++;\n        } else {\n            ans = (ans + oddCount)\
        \ % MOD;\n            evenCount++;\n        }\n    }\n\n    return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $arr\n     * @return\
        \ Integer\n     */\n    function numOfSubarrays($arr) {\n        $MOD = 1000000007;\n\
        \        $ans = 0;\n        $prefix = 0;\n        $evenCount = 1;\n        $oddCount\
        \ = 0;\n\n        foreach ($arr as $x) {\n            $prefix ^= ($x & 1);\n\
        \            if ($prefix === 1) {\n                $ans = ($ans + $evenCount)\
        \ % $MOD;\n                $oddCount++;\n            } else {\n            \
        \    $ans = ($ans + $oddCount) % $MOD;\n                $evenCount++;\n    \
        \        }\n        }\n\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func numOfSubarrays(_ arr: [Int]) -> Int {\n   \
        \     let mod = 1_000_000_007\n        var ans = 0\n        var prefix = 0\n\
        \        var evenCount = 1\n        var oddCount = 0\n\n        for x in arr\
        \ {\n            prefix ^= (x & 1)\n            if prefix == 1 {\n         \
        \       ans = (ans + evenCount) % mod\n                oddCount += 1\n     \
        \       } else {\n                ans = (ans + oddCount) % mod\n           \
        \     evenCount += 1\n            }\n        }\n\n        return ans\n    }\n\
        }"
      kotlin: "class Solution {\n    fun numOfSubarrays(arr: IntArray): Int {\n    \
        \    val mod = 1000000007\n        var ans = 0\n        var prefix = 0\n   \
        \     var evenCount = 1\n        var oddCount = 0\n\n        for (x in arr)\
        \ {\n            prefix = prefix xor (x and 1)\n            if (prefix == 1)\
        \ {\n                ans = (ans + evenCount) % mod\n                oddCount++\n\
        \            } else {\n                ans = (ans + oddCount) % mod\n      \
        \          evenCount++\n            }\n        }\n\n        return ans\n   \
        \ }\n}"
      dart: "class Solution {\n  int numOfSubarrays(List<int> arr) {\n    const int\
        \ mod = 1000000007;\n    int ans = 0;\n    int prefix = 0;\n    int evenCount\
        \ = 1;\n    int oddCount = 0;\n\n    for (final x in arr) {\n      prefix ^=\
        \ (x & 1);\n      if (prefix == 1) {\n        ans = (ans + evenCount) % mod;\n\
        \        oddCount++;\n      } else {\n        ans = (ans + oddCount) % mod;\n\
        \        evenCount++;\n      }\n    }\n\n    return ans;\n  }\n}"
      go: "func numOfSubarrays(arr []int) int {\n    const mod = 1000000007\n    ans\
        \ := 0\n    prefix := 0\n    evenCount := 1\n    oddCount := 0\n\n    for _,\
        \ x := range arr {\n        prefix ^= (x & 1)\n        if prefix == 1 {\n  \
        \          ans = (ans + evenCount) % mod\n            oddCount++\n        }\
        \ else {\n            ans = (ans + oddCount) % mod\n            evenCount++\n\
        \        }\n    }\n\n    return ans\n}"
      ruby: "# @param {Integer[]} arr\n# @return {Integer}\ndef num_of_subarrays(arr)\n\
        \    mod = 1_000_000_007\n    ans = 0\n    prefix = 0\n    even_count = 1\n\
        \    odd_count = 0\n\n    arr.each do |x|\n        prefix ^= (x & 1)\n     \
        \   if prefix == 1\n            ans = (ans + even_count) % mod\n           \
        \ odd_count += 1\n        else\n            ans = (ans + odd_count) % mod\n\
        \            even_count += 1\n        end\n    end\n\n    ans\nend"
      scala: "object Solution {\n    def numOfSubarrays(arr: Array[Int]): Int = {\n\
        \        val mod = 1000000007\n        var ans = 0\n        var prefix = 0\n\
        \        var evenCount = 1\n        var oddCount = 0\n\n        for (x <- arr)\
        \ {\n            prefix ^= (x & 1)\n            if (prefix == 1) {\n       \
        \         ans = (ans + evenCount) % mod\n                oddCount += 1\n   \
        \         } else {\n                ans = (ans + oddCount) % mod\n         \
        \       evenCount += 1\n            }\n        }\n\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {\n\
        \        let modulo = 1_000_000_007;\n        let mut ans = 0;\n        let\
        \ mut prefix = 0;\n        let mut even_count = 1;\n        let mut odd_count\
        \ = 0;\n\n        for x in arr {\n            prefix ^= (x & 1);\n         \
        \   if prefix == 1 {\n                ans = (ans + even_count) % modulo;\n \
        \               odd_count += 1;\n            } else {\n                ans =\
        \ (ans + odd_count) % modulo;\n                even_count += 1;\n          \
        \  }\n        }\n\n        ans\n    }\n}"
      racket: "(define/contract (num-of-subarrays arr)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (define MOD 1000000007)\n  (for/fold ([ans 0]\n       \
        \      [prefix 0]\n             [even-count 1]\n             [odd-count 0]\n\
        \             #:result ans)\n            ([x (in-list arr)])\n    (define new-prefix\
        \ (bitwise-xor prefix (bitwise-and x 1)))\n    (if (= new-prefix 1)\n      \
        \  (values (modulo (+ ans even-count) MOD)\n                new-prefix\n   \
        \             even-count\n                (+ odd-count 1))\n        (values\
        \ (modulo (+ ans odd-count) MOD)\n                new-prefix\n             \
        \   (+ even-count 1)\n                odd-count))))"
      erlang: "-spec num_of_subarrays(Arr :: [integer()]) -> integer().\nnum_of_subarrays(Arr)\
        \ ->\n  Mod = 1000000007,\n  {Ans, _Prefix, _EvenCount, _OddCount} =\n    lists:foldl(\n\
        \      fun(X, {AnsAcc, PrefixAcc, EvenAcc, OddAcc}) ->\n        NewPrefix =\
        \ PrefixAcc bxor (X band 1),\n        case NewPrefix of\n          1 ->\n  \
        \          NewAns = (AnsAcc + EvenAcc) rem Mod,\n            {NewAns, NewPrefix,\
        \ EvenAcc, OddAcc + 1};\n          0 ->\n            NewAns = (AnsAcc + OddAcc)\
        \ rem Mod,\n            {NewAns, NewPrefix, EvenAcc + 1, OddAcc}\n        end\n\
        \      end,\n      {0, 0, 1, 0},\n      Arr\n    ),\n  Ans."
      elixir: "defmodule Solution do\n  @spec num_of_subarrays(arr :: [integer]) ::\
        \ integer\n  def num_of_subarrays(arr) do\n    mod = 1_000_000_007\n    import\
        \ Bitwise\n\n    {ans, _prefix, _even_count, _odd_count} =\n      Enum.reduce(arr,\
        \ {0, 0, 1, 0}, fn x, {ans, prefix, even_count, odd_count} ->\n        new_prefix\
        \ = bxor(prefix, band(x, 1))\n\n        if new_prefix == 1 do\n          {rem(ans\
        \ + even_count, mod), new_prefix, even_count, odd_count + 1}\n        else\n\
        \          {rem(ans + odd_count, mod), new_prefix, even_count + 1, odd_count}\n\
        \        end\n      end)\n\n    ans\n  end\nend"
    approach: 'To find the number of subarrays with an odd sum, we can utilize prefix
      sums and their parities. The sum of a subarray from index j to index i - 1 is
      given by the difference between the prefix sum up to i and the prefix sum up to
      j. A subarray sum is odd if and only if the prefix sums at its boundaries have
      different parities (one even and one odd). Therefore, as we iterate through the
      array and maintain the running prefix sum, the number of valid subarrays ending
      at the current index depends on the number of previously seen prefix sums with
      the opposite parity.


      We initialize a counter for even prefix sums to 1 (representing the initial empty
      prefix with sum 0) and odd prefix sums to 0. As we traverse the array, we update
      the current prefix sum parity by adding the current element. If the updated prefix
      sum is odd, it forms an odd-sum subarray with every previously seen even prefix
      sum, so we add the count of even prefix sums to our answer and increment the odd
      count. Conversely, if the current prefix sum is even, we add the count of odd
      prefix sums to the answer and increment the even count. We maintain the total
      count modulo 10^9 + 7 throughout the traversal.'
    time_complexity: O(N), where N is the length of the array arr. We iterate through
      the array in a single pass, performing constant time operations at each step.
    space_complexity: O(1) auxiliary space, as only a few variables are used to track
      the counts of prefix sum parities and the running total.
    elapsed_time: 1433.93510389328
    model: gemini-3.8-flash
    generated_at: '2026-11-15 04:29:46 '
---

## Problem #1524: Number of Sub-arrays With Odd Sum

**Difficulty:** Medium

**Topics:** Array, Math, Dynamic Programming, Prefix Sum

## Problem Description

<p>Given an array of integers <code>arr</code>, return <em>the number of subarrays with an <strong>odd</strong> sum</em>.</p>

<p>Since the answer can be very large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,4,6]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5,6,7]
<strong>Output:</strong> 16
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 100</code></li>
</ul>


## Hints

1. Can we use the accumulative sum to keep track of all the odd-sum sub-arrays ?

2. if the current accu sum is odd, we care only about previous even accu sums and vice versa.

## ✨ AI-Generated Solution (gemini-3.8-flash)

### Approach

To find the number of subarrays with an odd sum, we can utilize prefix sums and their parities. The sum of a subarray from index j to index i - 1 is given by the difference between the prefix sum up to i and the prefix sum up to j. A subarray sum is odd if and only if the prefix sums at its boundaries have different parities (one even and one odd). Therefore, as we iterate through the array and maintain the running prefix sum, the number of valid subarrays ending at the current index depends on the number of previously seen prefix sums with the opposite parity.

We initialize a counter for even prefix sums to 1 (representing the initial empty prefix with sum 0) and odd prefix sums to 0. As we traverse the array, we update the current prefix sum parity by adding the current element. If the updated prefix sum is odd, it forms an odd-sum subarray with every previously seen even prefix sum, so we add the count of even prefix sums to our answer and increment the odd count. Conversely, if the current prefix sum is even, we add the count of odd prefix sums to the answer and increment the even count. We maintain the total count modulo 10^9 + 7 throughout the traversal.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang" id="lang-cpp" checked>
  <input type="radio" name="code-lang" id="lang-java">
  <input type="radio" name="code-lang" id="lang-python">
  <input type="radio" name="code-lang" id="lang-python3">
  <input type="radio" name="code-lang" id="lang-c">
  <input type="radio" name="code-lang" id="lang-csharp">
  <input type="radio" name="code-lang" id="lang-javascript">
  <input type="radio" name="code-lang" id="lang-typescript">
  <input type="radio" name="code-lang" id="lang-php">
  <input type="radio" name="code-lang" id="lang-swift">
  <input type="radio" name="code-lang" id="lang-kotlin">
  <input type="radio" name="code-lang" id="lang-dart">
  <input type="radio" name="code-lang" id="lang-go">
  <input type="radio" name="code-lang" id="lang-ruby">
  <input type="radio" name="code-lang" id="lang-scala">
  <input type="radio" name="code-lang" id="lang-rust">
  <input type="radio" name="code-lang" id="lang-racket">
  <input type="radio" name="code-lang" id="lang-erlang">
  <input type="radio" name="code-lang" id="lang-elixir">
  <div class="tab-labels">
    <label for="lang-cpp">C++</label>
    <label for="lang-java">Java</label>
    <label for="lang-python">Python</label>
    <label for="lang-python3">Python3</label>
    <label for="lang-c">C</label>
    <label for="lang-csharp">C#</label>
    <label for="lang-javascript">JavaScript</label>
    <label for="lang-typescript">TypeScript</label>
    <label for="lang-php">PHP</label>
    <label for="lang-swift">Swift</label>
    <label for="lang-kotlin">Kotlin</label>
    <label for="lang-dart">Dart</label>
    <label for="lang-go">Go</label>
    <label for="lang-ruby">Ruby</label>
    <label for="lang-scala">Scala</label>
    <label for="lang-rust">Rust</label>
    <label for="lang-racket">Racket</label>
    <label for="lang-erlang">Erlang</label>
    <label for="lang-elixir">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        const int MOD = 1e9 + 7;
        long long ans = 0;
        int prefix = 0;
        int even_count = 1;
        int odd_count = 0;

        for (int x : arr) {
            prefix ^= (x & 1);
            if (prefix == 1) {
                ans = (ans + even_count) % MOD;
                odd_count++;
            } else {
                ans = (ans + odd_count) % MOD;
                even_count++;
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
class Solution {
    public int numOfSubarrays(int[] arr) {
        final int MOD = 1_000_000_007;
        long ans = 0;
        int prefix = 0;
        int evenCount = 1;
        int oddCount = 0;

        for (int x : arr) {
            prefix ^= (x & 1);
            if (prefix == 1) {
                ans = (ans + evenCount) % MOD;
                oddCount++;
            } else {
                ans = (ans + oddCount) % MOD;
                evenCount++;
            }
        }

        return (int) ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 0
        prefix = 0
        even_count = 1
        odd_count = 0

        for x in arr:
            prefix ^= (x & 1)
            if prefix == 1:
                ans = (ans + even_count) % MOD
                odd_count += 1
            else:
                ans = (ans + odd_count) % MOD
                even_count += 1

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        prefix = 0
        even_count = 1
        odd_count = 0

        for x in arr:
            prefix ^= (x & 1)
            if prefix == 1:
                ans = (ans + even_count) % MOD
                odd_count += 1
            else:
                ans = (ans + odd_count) % MOD
                even_count += 1

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numOfSubarrays(int* arr, int arrSize) {
    const int MOD = 1000000007;
    long long ans = 0;
    int prefix = 0;
    int even_count = 1;
    int odd_count = 0;

    for (int i = 0; i < arrSize; i++) {
        prefix ^= (arr[i] & 1);
        if (prefix == 1) {
            ans = (ans + even_count) % MOD;
            odd_count++;
        } else {
            ans = (ans + odd_count) % MOD;
            even_count++;
        }
    }

    return (int)ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumOfSubarrays(int[] arr) {
        const int MOD = 1000000007;
        int ans = 0;
        int prefix = 0;
        int evenCount = 1;
        int oddCount = 0;

        foreach (int x in arr) {
            prefix ^= (x & 1);
            if (prefix == 1) {
                ans = (ans + evenCount) % MOD;
                oddCount++;
            } else {
                ans = (ans + oddCount) % MOD;
                evenCount++;
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
/**
 * @param {number[]} arr
 * @return {number}
 */
var numOfSubarrays = function(arr) {
    const MOD = 1000000007;
    let ans = 0;
    let prefix = 0;
    let evenCount = 1;
    let oddCount = 0;

    for (const x of arr) {
        prefix ^= (x & 1);
        if (prefix === 1) {
            ans = (ans + evenCount) % MOD;
            oddCount++;
        } else {
            ans = (ans + oddCount) % MOD;
            evenCount++;
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
function numOfSubarrays(arr: number[]): number {
    const MOD = 1000000007;
    let ans = 0;
    let prefix = 0;
    let evenCount = 1;
    let oddCount = 0;

    for (const x of arr) {
        prefix ^= (x & 1);
        if (prefix === 1) {
            ans = (ans + evenCount) % MOD;
            oddCount++;
        } else {
            ans = (ans + oddCount) % MOD;
            evenCount++;
        }
    }

    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function numOfSubarrays($arr) {
        $MOD = 1000000007;
        $ans = 0;
        $prefix = 0;
        $evenCount = 1;
        $oddCount = 0;

        foreach ($arr as $x) {
            $prefix ^= ($x & 1);
            if ($prefix === 1) {
                $ans = ($ans + $evenCount) % $MOD;
                $oddCount++;
            } else {
                $ans = ($ans + $oddCount) % $MOD;
                $evenCount++;
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
class Solution {
    func numOfSubarrays(_ arr: [Int]) -> Int {
        let mod = 1_000_000_007
        var ans = 0
        var prefix = 0
        var evenCount = 1
        var oddCount = 0

        for x in arr {
            prefix ^= (x & 1)
            if prefix == 1 {
                ans = (ans + evenCount) % mod
                oddCount += 1
            } else {
                ans = (ans + oddCount) % mod
                evenCount += 1
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
class Solution {
    fun numOfSubarrays(arr: IntArray): Int {
        val mod = 1000000007
        var ans = 0
        var prefix = 0
        var evenCount = 1
        var oddCount = 0

        for (x in arr) {
            prefix = prefix xor (x and 1)
            if (prefix == 1) {
                ans = (ans + evenCount) % mod
                oddCount++
            } else {
                ans = (ans + oddCount) % mod
                evenCount++
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
class Solution {
  int numOfSubarrays(List<int> arr) {
    const int mod = 1000000007;
    int ans = 0;
    int prefix = 0;
    int evenCount = 1;
    int oddCount = 0;

    for (final x in arr) {
      prefix ^= (x & 1);
      if (prefix == 1) {
        ans = (ans + evenCount) % mod;
        oddCount++;
      } else {
        ans = (ans + oddCount) % mod;
        evenCount++;
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
func numOfSubarrays(arr []int) int {
    const mod = 1000000007
    ans := 0
    prefix := 0
    evenCount := 1
    oddCount := 0

    for _, x := range arr {
        prefix ^= (x & 1)
        if prefix == 1 {
            ans = (ans + evenCount) % mod
            oddCount++
        } else {
            ans = (ans + oddCount) % mod
            evenCount++
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
# @param {Integer[]} arr
# @return {Integer}
def num_of_subarrays(arr)
    mod = 1_000_000_007
    ans = 0
    prefix = 0
    even_count = 1
    odd_count = 0

    arr.each do |x|
        prefix ^= (x & 1)
        if prefix == 1
            ans = (ans + even_count) % mod
            odd_count += 1
        else
            ans = (ans + odd_count) % mod
            even_count += 1
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
object Solution {
    def numOfSubarrays(arr: Array[Int]): Int = {
        val mod = 1000000007
        var ans = 0
        var prefix = 0
        var evenCount = 1
        var oddCount = 0

        for (x <- arr) {
            prefix ^= (x & 1)
            if (prefix == 1) {
                ans = (ans + evenCount) % mod
                oddCount += 1
            } else {
                ans = (ans + oddCount) % mod
                evenCount += 1
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
impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {
        let modulo = 1_000_000_007;
        let mut ans = 0;
        let mut prefix = 0;
        let mut even_count = 1;
        let mut odd_count = 0;

        for x in arr {
            prefix ^= (x & 1);
            if prefix == 1 {
                ans = (ans + even_count) % modulo;
                odd_count += 1;
            } else {
                ans = (ans + odd_count) % modulo;
                even_count += 1;
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
(define/contract (num-of-subarrays arr)
  (-> (listof exact-integer?) exact-integer?)
  (define MOD 1000000007)
  (for/fold ([ans 0]
             [prefix 0]
             [even-count 1]
             [odd-count 0]
             #:result ans)
            ([x (in-list arr)])
    (define new-prefix (bitwise-xor prefix (bitwise-and x 1)))
    (if (= new-prefix 1)
        (values (modulo (+ ans even-count) MOD)
                new-prefix
                even-count
                (+ odd-count 1))
        (values (modulo (+ ans odd-count) MOD)
                new-prefix
                (+ even-count 1)
                odd-count))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec num_of_subarrays(Arr :: [integer()]) -> integer().
num_of_subarrays(Arr) ->
  Mod = 1000000007,
  {Ans, _Prefix, _EvenCount, _OddCount} =
    lists:foldl(
      fun(X, {AnsAcc, PrefixAcc, EvenAcc, OddAcc}) ->
        NewPrefix = PrefixAcc bxor (X band 1),
        case NewPrefix of
          1 ->
            NewAns = (AnsAcc + EvenAcc) rem Mod,
            {NewAns, NewPrefix, EvenAcc, OddAcc + 1};
          0 ->
            NewAns = (AnsAcc + OddAcc) rem Mod,
            {NewAns, NewPrefix, EvenAcc + 1, OddAcc}
        end
      end,
      {0, 0, 1, 0},
      Arr
    ),
  Ans.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_of_subarrays(arr :: [integer]) :: integer
  def num_of_subarrays(arr) do
    mod = 1_000_000_007
    import Bitwise

    {ans, _prefix, _even_count, _odd_count} =
      Enum.reduce(arr, {0, 0, 1, 0}, fn x, {ans, prefix, even_count, odd_count} ->
        new_prefix = bxor(prefix, band(x, 1))

        if new_prefix == 1 do
          {rem(ans + even_count, mod), new_prefix, even_count, odd_count + 1}
        else
          {rem(ans + odd_count, mod), new_prefix, even_count + 1, odd_count}
        end
      end)

    ans
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the array arr. We iterate through the array in a single pass, performing constant time operations at each step.
- **Space Complexity:** O(1) auxiliary space, as only a few variables are used to track the counts of prefix sum parities and the running total.
