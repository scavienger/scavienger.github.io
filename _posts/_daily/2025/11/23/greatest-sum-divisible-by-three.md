---
layout: post
title: "Greatest Sum Divisible by Three"
date: 2025-11-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/greatest-sum-divisible-by-three/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxSumDivThree(vector<int>& nums) {\n\
        \        const int neg = -1000000000;\n        vector<int> dp = {0, neg, neg};\n\
        \        for (int x : nums) {\n            vector<int> next = dp;\n        \
        \    for (int r = 0; r < 3; ++r) {\n                if (dp[r] != neg) {\n  \
        \                  int nr = (r + x) % 3;\n                    next[nr] = max(next[nr],\
        \ dp[r] + x);\n                }\n            }\n            dp = next;\n  \
        \      }\n        return dp[0];\n    }\n};"
      java: "class Solution {\n    public int maxSumDivThree(int[] nums) {\n       \
        \ final int neg = -1000000000;\n        int[] dp = {0, neg, neg};\n        for\
        \ (int x : nums) {\n            int[] next = dp.clone();\n            for (int\
        \ r = 0; r < 3; r++) {\n                if (dp[r] != neg) {\n              \
        \      int nr = (r + x) % 3;\n                    next[nr] = Math.max(next[nr],\
        \ dp[r] + x);\n                }\n            }\n            dp = next;\n  \
        \      }\n        return dp[0];\n    }\n}"
      python: "class Solution(object):\n    def maxSumDivThree(self, nums):\n      \
        \  \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\
        \n        neg = -10**9\n        dp = [0, neg, neg]\n        for x in nums:\n\
        \            next_dp = dp[:]\n            for r in range(3):\n             \
        \   if dp[r] != neg:\n                    nr = (r + x) % 3\n               \
        \     next_dp[nr] = max(next_dp[nr], dp[r] + x)\n            dp = next_dp\n\
        \        return dp[0]"
      python3: "class Solution:\n    def maxSumDivThree(self, nums: list[int]) -> int:\n\
        \        neg = -10**9\n        dp = [0, neg, neg]\n        for x in nums:\n\
        \            next_dp = dp[:]\n            for r in range(3):\n             \
        \   if dp[r] != neg:\n                    nr = (r + x) % 3\n               \
        \     next_dp[nr] = max(next_dp[nr], dp[r] + x)\n            dp = next_dp\n\
        \        return dp[0]"
      c: "int maxSumDivThree(int* nums, int numsSize) {\n    const int neg = -1000000000;\n\
        \    int dp[3] = {0, neg, neg};\n    for (int i = 0; i < numsSize; ++i) {\n\
        \        int next[3] = {dp[0], dp[1], dp[2]};\n        for (int r = 0; r < 3;\
        \ ++r) {\n            if (dp[r] != neg) {\n                int nr = (r + nums[i])\
        \ % 3;\n                int candidate = dp[r] + nums[i];\n                if\
        \ (candidate > next[nr]) {\n                    next[nr] = candidate;\n    \
        \            }\n            }\n        }\n        dp[0] = next[0];\n       \
        \ dp[1] = next[1];\n        dp[2] = next[2];\n    }\n    return dp[0];\n}"
      csharp: "public class Solution {\n    public int MaxSumDivThree(int[] nums) {\n\
        \        int neg = -1000000000;\n        int[] dp = { 0, neg, neg };\n     \
        \   foreach (int x in nums) {\n            int[] nextDp = (int[])dp.Clone();\n\
        \            for (int r = 0; r < 3; r++) {\n                if (dp[r] != neg)\
        \ {\n                    int nr = (r + x) % 3;\n                    nextDp[nr]\
        \ = Math.Max(nextDp[nr], dp[r] + x);\n                }\n            }\n   \
        \         dp = nextDp;\n        }\n        return dp[0];\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maxSumDivThree\
        \ = function(nums) {\n    const neg = -1000000000;\n    let dp = [0, neg, neg];\n\
        \    for (const x of nums) {\n        const nextDp = dp.slice();\n        for\
        \ (let r = 0; r < 3; r++) {\n            if (dp[r] !== neg) {\n            \
        \    const nr = (r + x) % 3;\n                nextDp[nr] = Math.max(nextDp[nr],\
        \ dp[r] + x);\n            }\n        }\n        dp = nextDp;\n    }\n    return\
        \ dp[0];\n};"
      typescript: "function maxSumDivThree(nums: number[]): number {\n    const neg\
        \ = -1000000000;\n    let dp = [0, neg, neg];\n    for (const x of nums) {\n\
        \        const nextDp = dp.slice();\n        for (let r = 0; r < 3; r++) {\n\
        \            if (dp[r] !== neg) {\n                const nr = (r + x) % 3;\n\
        \                nextDp[nr] = Math.max(nextDp[nr], dp[r] + x);\n           \
        \ }\n        }\n        dp = nextDp;\n    }\n    return dp[0];\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function maxSumDivThree($nums) {\n        $neg = -1000000000;\n\
        \        $dp = [0, $neg, $neg];\n        foreach ($nums as $x) {\n         \
        \   $nextDp = $dp;\n            for ($r = 0; $r < 3; $r++) {\n             \
        \   if ($dp[$r] !== $neg) {\n                    $nr = ($r + $x) % 3;\n    \
        \                $nextDp[$nr] = max($nextDp[$nr], $dp[$r] + $x);\n         \
        \       }\n            }\n            $dp = $nextDp;\n        }\n        return\
        \ $dp[0];\n    }\n}"
      swift: "class Solution {\n    func maxSumDivThree(_ nums: [Int]) -> Int {\n  \
        \      let neg = -1000000000\n        var dp = [0, neg, neg]\n        for x\
        \ in nums {\n            var nextDp = dp\n            for r in 0..<3 {\n   \
        \             if dp[r] != neg {\n                    let nr = (r + x) % 3\n\
        \                    nextDp[nr] = max(nextDp[nr], dp[r] + x)\n             \
        \   }\n            }\n            dp = nextDp\n        }\n        return dp[0]\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun maxSumDivThree(nums: IntArray): Int {\n   \
        \     val neg = -1_000_000_000\n        var dp = intArrayOf(0, neg, neg)\n \
        \       for (x in nums) {\n            val nextDp = dp.copyOf()\n          \
        \  for (r in 0..2) {\n                if (dp[r] != neg) {\n                \
        \    val nr = (r + x) % 3\n                    nextDp[nr] = maxOf(nextDp[nr],\
        \ dp[r] + x)\n                }\n            }\n            dp = nextDp\n  \
        \      }\n        return dp[0]\n    }\n}"
      dart: "class Solution {\n  int maxSumDivThree(List<int> nums) {\n    const neg\
        \ = -1000000000;\n    var dp = [0, neg, neg];\n    for (final x in nums) {\n\
        \      final nextDp = List<int>.from(dp);\n      for (var r = 0; r < 3; r++)\
        \ {\n        if (dp[r] != neg) {\n          final nr = (r + x) % 3;\n      \
        \    if (dp[r] + x > nextDp[nr]) {\n            nextDp[nr] = dp[r] + x;\n  \
        \        }\n        }\n      }\n      dp = nextDp;\n    }\n    return dp[0];\n\
        \  }\n}"
      go: "func maxSumDivThree(nums []int) int {\n\tconst neg = -1000000000\n\tdp :=\
        \ [3]int{0, neg, neg}\n\tfor _, x := range nums {\n\t\tnextDp := dp\n\t\tfor\
        \ r := 0; r < 3; r++ {\n\t\t\tif dp[r] != neg {\n\t\t\t\tnr := (r + x) % 3\n\
        \t\t\t\tif dp[r]+x > nextDp[nr] {\n\t\t\t\t\tnextDp[nr] = dp[r] + x\n\t\t\t\t\
        }\n\t\t\t}\n\t\t}\n\t\tdp = nextDp\n\t}\n\treturn dp[0]\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef max_sum_div_three(nums)\n\
        \  neg = -1_000_000_000\n  dp = [0, neg, neg]\n  nums.each do |x|\n    next_dp\
        \ = dp.dup\n    3.times do |r|\n      if dp[r] != neg\n        nr = (r + x)\
        \ % 3\n        next_dp[nr] = [next_dp[nr], dp[r] + x].max\n      end\n    end\n\
        \    dp = next_dp\n  end\n  dp[0]\nend"
      scala: "object Solution {\n    def maxSumDivThree(nums: Array[Int]): Int = {\n\
        \        val neg = -1000000000\n        var dp = Array(0, neg, neg)\n      \
        \  for (x <- nums) {\n            val nextDp = dp.clone()\n            for (r\
        \ <- 0 until 3) {\n                if (dp(r) != neg) {\n                   \
        \ val nr = (r + x) % 3\n                    nextDp(nr) = nextDp(nr).max(dp(r)\
        \ + x)\n                }\n            }\n            dp = nextDp\n        }\n\
        \        dp(0)\n    }\n}"
      rust: "impl Solution {\n    pub fn max_sum_div_three(nums: Vec<i32>) -> i32 {\n\
        \        let neg = i32::MIN / 2;\n        let mut dp = [0, neg, neg];\n    \
        \    for x in nums {\n            let mut next_dp = dp;\n            for r in\
        \ 0..3 {\n                if dp[r] != neg {\n                    let nr = (r\
        \ + x as usize) % 3;\n                    next_dp[nr] = next_dp[nr].max(dp[r]\
        \ + x);\n                }\n            }\n            dp = next_dp;\n     \
        \   }\n        dp[0]\n    }\n}"
      racket: "(define/contract (max-sum-div-three nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let loop ([remaining nums] [dp (vector 0 -1000000000 -1000000000)])\n\
        \    (if (null? remaining)\n        (vector-ref dp 0)\n        (let* ([x (car\
        \ remaining)]\n               [next-dp (vector-copy dp)])\n          (for ([r\
        \ (in-range 3)])\n            (define best (vector-ref dp r))\n            (unless\
        \ (= best -1000000000)\n              (define nr (modulo (+ r x) 3))\n     \
        \         (vector-set! next-dp nr\n                           (max (vector-ref\
        \ next-dp nr) (+ best x))))\n          (loop (cdr remaining) next-dp)))))"
      erlang: "-spec max_sum_div_three(Nums :: [integer()]) -> integer().\nmax_sum_div_three(Nums)\
        \ ->\n  lists:foldl(\n    fun(X, Dp) ->\n      lists:foldl(\n        fun(R,\
        \ NextDp) ->\n          Best = lists:nth(R + 1, Dp),\n          case Best of\n\
        \            -1000000000 -> NextDp;\n            _ ->\n              Nr = (R\
        \ + X) rem 3,\n              Updated = max(lists:nth(Nr + 1, NextDp), Best +\
        \ X),\n              lists:sublist(NextDp, Nr) ++ [Updated] ++ lists:nthtail(Nr\
        \ + 1, NextDp)\n          end\n        end,\n        Dp,\n        [0, 1, 2]\n\
        \      )\n    end,\n    [0, -1000000000, -1000000000],\n    Nums\n  ),\n  element(1,\
        \ list_to_tuple(\n    lists:foldl(\n      fun(X, Dp) ->\n        lists:foldl(\n\
        \          fun(R, NextDp) ->\n            Best = lists:nth(R + 1, Dp),\n   \
        \         case Best of\n              -1000000000 -> NextDp;\n             \
        \ _ ->\n                Nr = (R + X) rem 3,\n                Updated = max(lists:nth(Nr\
        \ + 1, NextDp), Best + X),\n                lists:sublist(NextDp, Nr) ++ [Updated]\
        \ ++ lists:nthtail(Nr + 1, NextDp)\n            end\n          end,\n      \
        \    Dp,\n          [0, 1, 2]\n        )\n      end,\n      [0, -1000000000,\
        \ -1000000000],\n      Nums\n    end\n  ))."
      elixir: "defmodule Solution do\n  @spec max_sum_div_three(nums :: [integer]) ::\
        \ integer\n  def max_sum_div_three(nums) do\n    neg = -1_000_000_000\n    dp\
        \ = Enum.reduce(nums, [0, neg, neg], fn x, dp ->\n      Enum.reduce(0..2, dp,\
        \ fn r, next_dp ->\n        best = Enum.at(dp, r)\n        if best == neg do\n\
        \          next_dp\n        else\n          nr = rem(r + x, 3)\n          List.replace_at(next_dp,\
        \ nr, max(Enum.at(next_dp, nr), best + x))\n        end\n      end)\n    end)\n\
        \    Enum.at(dp, 0)\n  end\nend"
    approach: 'Maintain the best sum found for each remainder modulo 3. Initialize the
      states as [0, -infinity, -infinity], since choosing no elements gives remainder
      0. For each number, create a fresh copy of the states so it can either be skipped
      or added once.


      When adding a number, update the state for the resulting remainder using the previous
      best sum plus that number. After processing every element, the best sum divisible
      by 3 is the state for remainder 0.'
    time_complexity: O(n), where n is the number of elements, with three remainder states
      processed for each element.
    space_complexity: O(1), using a fixed number of states regardless of the array length.
    elapsed_time: 77.30283951759338
    model: gpt-6-luna
    generated_at: '2026-11-13 00:11:11 '
---

## Problem #1262: Greatest Sum Divisible by Three

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Greedy, Sorting

## Problem Description

<p>Given an integer array <code>nums</code>, return <em>the <strong>maximum possible sum </strong>of elements of the array such that it is divisible by three</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,6,5,1,8]
<strong>Output:</strong> 18
<strong>Explanation:</strong> Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since 4 is not divisible by 3, do not pick any number.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,4]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. Represent the state as DP[pos][mod]: maximum possible sum starting in the position "pos" in the array where the current sum modulo 3 is equal to mod.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Maintain the best sum found for each remainder modulo 3. Initialize the states as [0, -infinity, -infinity], since choosing no elements gives remainder 0. For each number, create a fresh copy of the states so it can either be skipped or added once.

When adding a number, update the state for the resulting remainder using the previous best sum plus that number. After processing every element, the best sum divisible by 3 is the state for remainder 0.

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
    int maxSumDivThree(vector<int>& nums) {
        const int neg = -1000000000;
        vector<int> dp = {0, neg, neg};
        for (int x : nums) {
            vector<int> next = dp;
            for (int r = 0; r < 3; ++r) {
                if (dp[r] != neg) {
                    int nr = (r + x) % 3;
                    next[nr] = max(next[nr], dp[r] + x);
                }
            }
            dp = next;
        }
        return dp[0];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxSumDivThree(int[] nums) {
        final int neg = -1000000000;
        int[] dp = {0, neg, neg};
        for (int x : nums) {
            int[] next = dp.clone();
            for (int r = 0; r < 3; r++) {
                if (dp[r] != neg) {
                    int nr = (r + x) % 3;
                    next[nr] = Math.max(next[nr], dp[r] + x);
                }
            }
            dp = next;
        }
        return dp[0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = -10**9
        dp = [0, neg, neg]
        for x in nums:
            next_dp = dp[:]
            for r in range(3):
                if dp[r] != neg:
                    nr = (r + x) % 3
                    next_dp[nr] = max(next_dp[nr], dp[r] + x)
            dp = next_dp
        return dp[0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        neg = -10**9
        dp = [0, neg, neg]
        for x in nums:
            next_dp = dp[:]
            for r in range(3):
                if dp[r] != neg:
                    nr = (r + x) % 3
                    next_dp[nr] = max(next_dp[nr], dp[r] + x)
            dp = next_dp
        return dp[0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxSumDivThree(int* nums, int numsSize) {
    const int neg = -1000000000;
    int dp[3] = {0, neg, neg};
    for (int i = 0; i < numsSize; ++i) {
        int next[3] = {dp[0], dp[1], dp[2]};
        for (int r = 0; r < 3; ++r) {
            if (dp[r] != neg) {
                int nr = (r + nums[i]) % 3;
                int candidate = dp[r] + nums[i];
                if (candidate > next[nr]) {
                    next[nr] = candidate;
                }
            }
        }
        dp[0] = next[0];
        dp[1] = next[1];
        dp[2] = next[2];
    }
    return dp[0];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxSumDivThree(int[] nums) {
        int neg = -1000000000;
        int[] dp = { 0, neg, neg };
        foreach (int x in nums) {
            int[] nextDp = (int[])dp.Clone();
            for (int r = 0; r < 3; r++) {
                if (dp[r] != neg) {
                    int nr = (r + x) % 3;
                    nextDp[nr] = Math.Max(nextDp[nr], dp[r] + x);
                }
            }
            dp = nextDp;
        }
        return dp[0];
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
 * @return {number}
 */
var maxSumDivThree = function(nums) {
    const neg = -1000000000;
    let dp = [0, neg, neg];
    for (const x of nums) {
        const nextDp = dp.slice();
        for (let r = 0; r < 3; r++) {
            if (dp[r] !== neg) {
                const nr = (r + x) % 3;
                nextDp[nr] = Math.max(nextDp[nr], dp[r] + x);
            }
        }
        dp = nextDp;
    }
    return dp[0];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSumDivThree(nums: number[]): number {
    const neg = -1000000000;
    let dp = [0, neg, neg];
    for (const x of nums) {
        const nextDp = dp.slice();
        for (let r = 0; r < 3; r++) {
            if (dp[r] !== neg) {
                const nr = (r + x) % 3;
                nextDp[nr] = Math.max(nextDp[nr], dp[r] + x);
            }
        }
        dp = nextDp;
    }
    return dp[0];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumDivThree($nums) {
        $neg = -1000000000;
        $dp = [0, $neg, $neg];
        foreach ($nums as $x) {
            $nextDp = $dp;
            for ($r = 0; $r < 3; $r++) {
                if ($dp[$r] !== $neg) {
                    $nr = ($r + $x) % 3;
                    $nextDp[$nr] = max($nextDp[$nr], $dp[$r] + $x);
                }
            }
            $dp = $nextDp;
        }
        return $dp[0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxSumDivThree(_ nums: [Int]) -> Int {
        let neg = -1000000000
        var dp = [0, neg, neg]
        for x in nums {
            var nextDp = dp
            for r in 0..<3 {
                if dp[r] != neg {
                    let nr = (r + x) % 3
                    nextDp[nr] = max(nextDp[nr], dp[r] + x)
                }
            }
            dp = nextDp
        }
        return dp[0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxSumDivThree(nums: IntArray): Int {
        val neg = -1_000_000_000
        var dp = intArrayOf(0, neg, neg)
        for (x in nums) {
            val nextDp = dp.copyOf()
            for (r in 0..2) {
                if (dp[r] != neg) {
                    val nr = (r + x) % 3
                    nextDp[nr] = maxOf(nextDp[nr], dp[r] + x)
                }
            }
            dp = nextDp
        }
        return dp[0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxSumDivThree(List<int> nums) {
    const neg = -1000000000;
    var dp = [0, neg, neg];
    for (final x in nums) {
      final nextDp = List<int>.from(dp);
      for (var r = 0; r < 3; r++) {
        if (dp[r] != neg) {
          final nr = (r + x) % 3;
          if (dp[r] + x > nextDp[nr]) {
            nextDp[nr] = dp[r] + x;
          }
        }
      }
      dp = nextDp;
    }
    return dp[0];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxSumDivThree(nums []int) int {
	const neg = -1000000000
	dp := [3]int{0, neg, neg}
	for _, x := range nums {
		nextDp := dp
		for r := 0; r < 3; r++ {
			if dp[r] != neg {
				nr := (r + x) % 3
				if dp[r]+x > nextDp[nr] {
					nextDp[nr] = dp[r] + x
				}
			}
		}
		dp = nextDp
	}
	return dp[0]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def max_sum_div_three(nums)
  neg = -1_000_000_000
  dp = [0, neg, neg]
  nums.each do |x|
    next_dp = dp.dup
    3.times do |r|
      if dp[r] != neg
        nr = (r + x) % 3
        next_dp[nr] = [next_dp[nr], dp[r] + x].max
      end
    end
    dp = next_dp
  end
  dp[0]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxSumDivThree(nums: Array[Int]): Int = {
        val neg = -1000000000
        var dp = Array(0, neg, neg)
        for (x <- nums) {
            val nextDp = dp.clone()
            for (r <- 0 until 3) {
                if (dp(r) != neg) {
                    val nr = (r + x) % 3
                    nextDp(nr) = nextDp(nr).max(dp(r) + x)
                }
            }
            dp = nextDp
        }
        dp(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_sum_div_three(nums: Vec<i32>) -> i32 {
        let neg = i32::MIN / 2;
        let mut dp = [0, neg, neg];
        for x in nums {
            let mut next_dp = dp;
            for r in 0..3 {
                if dp[r] != neg {
                    let nr = (r + x as usize) % 3;
                    next_dp[nr] = next_dp[nr].max(dp[r] + x);
                }
            }
            dp = next_dp;
        }
        dp[0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-sum-div-three nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ([remaining nums] [dp (vector 0 -1000000000 -1000000000)])
    (if (null? remaining)
        (vector-ref dp 0)
        (let* ([x (car remaining)]
               [next-dp (vector-copy dp)])
          (for ([r (in-range 3)])
            (define best (vector-ref dp r))
            (unless (= best -1000000000)
              (define nr (modulo (+ r x) 3))
              (vector-set! next-dp nr
                           (max (vector-ref next-dp nr) (+ best x))))
          (loop (cdr remaining) next-dp)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_sum_div_three(Nums :: [integer()]) -> integer().
max_sum_div_three(Nums) ->
  lists:foldl(
    fun(X, Dp) ->
      lists:foldl(
        fun(R, NextDp) ->
          Best = lists:nth(R + 1, Dp),
          case Best of
            -1000000000 -> NextDp;
            _ ->
              Nr = (R + X) rem 3,
              Updated = max(lists:nth(Nr + 1, NextDp), Best + X),
              lists:sublist(NextDp, Nr) ++ [Updated] ++ lists:nthtail(Nr + 1, NextDp)
          end
        end,
        Dp,
        [0, 1, 2]
      )
    end,
    [0, -1000000000, -1000000000],
    Nums
  ),
  element(1, list_to_tuple(
    lists:foldl(
      fun(X, Dp) ->
        lists:foldl(
          fun(R, NextDp) ->
            Best = lists:nth(R + 1, Dp),
            case Best of
              -1000000000 -> NextDp;
              _ ->
                Nr = (R + X) rem 3,
                Updated = max(lists:nth(Nr + 1, NextDp), Best + X),
                lists:sublist(NextDp, Nr) ++ [Updated] ++ lists:nthtail(Nr + 1, NextDp)
            end
          end,
          Dp,
          [0, 1, 2]
        )
      end,
      [0, -1000000000, -1000000000],
      Nums
    end
  )).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_sum_div_three(nums :: [integer]) :: integer
  def max_sum_div_three(nums) do
    neg = -1_000_000_000
    dp = Enum.reduce(nums, [0, neg, neg], fn x, dp ->
      Enum.reduce(0..2, dp, fn r, next_dp ->
        best = Enum.at(dp, r)
        if best == neg do
          next_dp
        else
          nr = rem(r + x, 3)
          List.replace_at(next_dp, nr, max(Enum.at(next_dp, nr), best + x))
        end
      end)
    end)
    Enum.at(dp, 0)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the number of elements, with three remainder states processed for each element.
- **Space Complexity:** O(1), using a fixed number of states regardless of the array length.
