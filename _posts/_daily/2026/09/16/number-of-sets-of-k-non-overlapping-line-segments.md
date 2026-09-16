---
layout: post
title: "Number of Sets of K Non-Overlapping Line Segments"
date: 2026-09-16 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "Dynamic Programming", "Combinatorics", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfSets(int n, int k) {\n      \
        \  long long MOD = 1e9 + 7;\n        vector<long long> dp0(k + 1, 0);\n    \
        \    vector<long long> dp1(k + 1, 0);\n        dp0[0] = 1;\n        for (int\
        \ i = 1; i < n; ++i) {\n            vector<long long> next_dp0(k + 1, 0);\n\
        \            vector<long long> next_dp1(k + 1, 0);\n            next_dp0[0]\
        \ = 1;\n            for (int j = 1; j <= k; ++j) {\n                next_dp0[j]\
        \ = (dp0[j] + dp1[j]) % MOD;\n                next_dp1[j] = (dp1[j] + next_dp0[j\
        \ - 1]) % MOD;\n            }\n            dp0 = next_dp0;\n            dp1\
        \ = next_dp1;\n        }\n        return (dp0[k] + dp1[k]) % MOD;\n    }\n};"
      java: "class Solution {\n    public int numberOfSets(int n, int k) {\n       \
        \ long MOD = 1_000_000_007;\n        long[] dp0 = new long[k + 1];\n       \
        \ long[] dp1 = new long[k + 1];\n        dp0[0] = 1;\n        for (int i = 1;\
        \ i < n; i++) {\n            long[] next_dp0 = new long[k + 1];\n          \
        \  long[] next_dp1 = new long[k + 1];\n            next_dp0[0] = 1;\n      \
        \      for (int j = 1; j <= k; j++) {\n                next_dp0[j] = (dp0[j]\
        \ + dp1[j]) % MOD;\n                next_dp1[j] = (dp1[j] + next_dp0[j - 1])\
        \ % MOD;\n            }\n            dp0 = next_dp0;\n            dp1 = next_dp1;\n\
        \        }\n        return (int) ((dp0[k] + dp1[k]) % MOD);\n    }\n}"
      python: "class Solution(object):\n    def numberOfSets(self, n, k):\n        \"\
        \"\"\n        :type n: int\n        :type k: int\n        :rtype: int\n    \
        \    \"\"\"\n        MOD = 10**9 + 7\n        dp0 = [0] * (k + 1)\n        dp1\
        \ = [0] * (k + 1)\n        dp0[0] = 1\n        for i in range(1, n):\n     \
        \       next_dp0 = [0] * (k + 1)\n            next_dp1 = [0] * (k + 1)\n   \
        \         next_dp0[0] = 1\n            for j in range(1, k + 1):\n         \
        \       next_dp0[j] = (dp0[j] + dp1[j]) % MOD\n                next_dp1[j] =\
        \ (dp1[j] + next_dp0[j-1]) % MOD\n            dp0 = next_dp0\n            dp1\
        \ = next_dp1\n        return (dp0[k] + dp1[k]) % MOD"
      python3: "class Solution:\n    def numberOfSets(self, n: int, k: int) -> int:\n\
        \        MOD = 10**9 + 7\n        dp0 = [0] * (k + 1)\n        dp1 = [0] * (k\
        \ + 1)\n        dp0[0] = 1\n        for i in range(1, n):\n            next_dp0\
        \ = [0] * (k + 1)\n            next_dp1 = [0] * (k + 1)\n            next_dp0[0]\
        \ = 1\n            for j in range(1, k + 1):\n                next_dp0[j] =\
        \ (dp0[j] + dp1[j]) % MOD\n                next_dp1[j] = (dp1[j] + next_dp0[j\
        \ - 1]) % MOD\n            dp0, dp1 = next_dp0, next_dp1\n        return (dp0[k]\
        \ + dp1[k]) % MOD"
      c: "int numberOfSets(int n, int k) {\n    long long MOD = 1000000007;\n    long\
        \ long* dp0 = (long long*)calloc(k + 1, sizeof(long long));\n    long long*\
        \ dp1 = (long long*)calloc(k + 1, sizeof(long long));\n    long long* next_dp0\
        \ = (long long*)calloc(k + 1, sizeof(long long));\n    long long* next_dp1 =\
        \ (long long*)calloc(k + 1, sizeof(long long));\n\n    dp0[0] = 1;\n    for\
        \ (int i = 1; i < n; i++) {\n        next_dp0[0] = 1;\n        next_dp1[0] =\
        \ 0;\n        for (int j = 1; j <= k; j++) {\n            next_dp0[j] = (dp0[j]\
        \ + dp1[j]) % MOD;\n            next_dp1[j] = (dp1[j] + next_dp0[j - 1]) % MOD;\n\
        \        }\n        for (int j = 0; j <= k; j++) {\n            dp0[j] = next_dp0[j];\n\
        \            dp1[j] = next_dp1[j];\n        }\n    }\n\n    int ans = (int)((dp0[k]\
        \ + dp1[k]) % MOD);\n    free(dp0); free(dp1); free(next_dp0); free(next_dp1);\n\
        \    return ans;\n}"
      csharp: '// Generation failed for C#

        // Reason: Parsing failed'
      javascript: '// Generation failed for JavaScript

        // Reason: Parsing failed'
      typescript: '// Generation failed for TypeScript

        // Reason: Parsing failed'
      php: '// Generation failed for PHP

        // Reason: Parsing failed'
      swift: '// Generation failed for Swift

        // Reason: Parsing failed'
      kotlin: "class Solution {\n    fun numberOfSets(n: Int, k: Int): Int {\n     \
        \   val mod = 1000000007\n        val targetN = n + k - 1\n        val targetK\
        \ = 2 * k\n\n        val dp = IntArray(targetK + 1)\n        dp[0] = 1\n\n \
        \       for (i in 1..targetN) {\n            val limit = if (i < targetK) i\
        \ else targetK\n            for (j in limit downTo 1) {\n                dp[j]\
        \ = (dp[j] + dp[j - 1]) % mod\n            }\n        }\n\n        return dp[targetK]\n\
        \    }\n}"
      dart: "class Solution {\n  int numberOfSets(int n, int k) {\n    int mod = 1000000007;\n\
        \    int targetN = n + k - 1;\n    int targetK = 2 * k;\n\n    List<int> dp\
        \ = List.filled(targetK + 1, 0);\n    dp[0] = 1;\n\n    for (int i = 1; i <=\
        \ targetN; i++) {\n      int limit = i < targetK ? i : targetK;\n      for (int\
        \ j = limit; j >= 1; j--) {\n        dp[j] = (dp[j] + dp[j - 1]) % mod;\n  \
        \    }\n    }\n\n    return dp[targetK];\n  }\n}"
      go: "func numberOfSets(n int, k int) int {\n    mod := 1000000007\n    targetN\
        \ := n + k - 1\n    targetK := 2 * k\n\n    dp := make([]int, targetK+1)\n \
        \   dp[0] = 1\n\n    for i := 1; i <= targetN; i++ {\n        limit := i\n \
        \       if limit > targetK {\n            limit = targetK\n        }\n     \
        \   for j := limit; j >= 1; j-- {\n            dp[j] = (dp[j] + dp[j-1]) % mod\n\
        \        }\n    }\n\n    return dp[targetK]\n}"
      ruby: "# @param {Integer} n\n# @param {Integer} k\n# @return {Integer}\ndef number_of_sets(n,\
        \ k)\n  mod = 1_000_000_007\n  target_n = n + k - 1\n  target_k = 2 * k\n\n\
        \  dp = Array.new(target_k + 1, 0)\n  dp[0] = 1\n\n  (1..target_n).each do |i|\n\
        \    limit = i < target_k ? i : target_k\n    limit.downto(1) do |j|\n     \
        \ dp[j] = (dp[j] + dp[j - 1]) % mod\n    end\n  end\n\n  dp[target_k]\nend"
      scala: "object Solution {\n    def numberOfSets(n: Int, k: Int): Int = {\n   \
        \     val mod = 1000000007\n        val targetN = n + k - 1\n        val targetK\
        \ = 2 * k\n\n        val dp = new Array[Int](targetK + 1)\n        dp(0) = 1\n\
        \n        for (i <- 1 to targetN) {\n            val limit = if (i < targetK)\
        \ i else targetK\n            for (j <- limit to 1 by -1) {\n              \
        \  dp(j) = (dp(j) + dp(j - 1)) % mod\n            }\n        }\n\n        dp(targetK)\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn number_of_sets(n: i32, k: i32) -> i32 {\n \
        \       let n = n as usize;\n        let k = k as usize;\n        let mod_val\
        \ = 1_000_000_007;\n\n        let mut dp0 = vec![0; k + 1];\n        let mut\
        \ dp1 = vec![0; k + 1];\n        let mut next_dp0 = vec![0; k + 1];\n      \
        \  let mut next_dp1 = vec![0; k + 1];\n\n        dp0[0] = 1;\n\n        for\
        \ _ in 1..n {\n            for j in 0..=k {\n                next_dp0[j] = (dp0[j]\
        \ + dp1[j]) % mod_val;\n                if j > 0 {\n                    next_dp1[j]\
        \ = (dp1[j] + next_dp0[j - 1]) % mod_val;\n                } else {\n      \
        \              next_dp1[j] = 0;\n                }\n            }\n        \
        \    std::mem::swap(&mut dp0, &mut next_dp0);\n            std::mem::swap(&mut\
        \ dp1, &mut next_dp1);\n        }\n\n        (dp0[k] + dp1[k]) % mod_val\n \
        \   }\n}"
      racket: "(define/contract (number-of-sets n k)\n  (-> exact-integer? exact-integer?\
        \ exact-integer?)\n  (let ([mod 1000000007])\n    (let ([dp0 (make-vector (+\
        \ k 1) 0)]\n          [dp1 (make-vector (+ k 1) 0)]\n          [next-dp0 (make-vector\
        \ (+ k 1) 0)]\n          [next-dp1 (make-vector (+ k 1) 0)])\n      (vector-set!\
        \ dp0 0 1)\n      (for ([i (in-range 1 n)])\n        (for ([j (in-range (+ k\
        \ 1))])\n          (vector-set! next-dp0 j (remainder (+ (vector-ref dp0 j)\
        \ (vector-ref dp1 j)) mod))\n          (if (> j 0)\n              (vector-set!\
        \ next-dp1 j (remainder (+ (vector-ref dp1 j) (vector-ref next-dp0 (- j 1)))\
        \ mod))\n              (vector-set! next-dp1 j 0)))\n        (for ([j (in-range\
        \ (+ k 1))])\n          (vector-set! dp0 j (vector-ref next-dp0 j))\n      \
        \    (vector-set! dp1 j (vector-ref next-dp1 j))))\n      (remainder (+ (vector-ref\
        \ dp0 k) (vector-ref dp1 k)) mod))))"
      erlang: "-spec number_of_sets(N :: integer(), K :: integer()) -> integer().\n\
        number_of_sets(N, K) ->\n    MOD = 1000000007,\n    InitialDP0 = list_to_tuple([1\
        \ | lists:duplicate(K, 0)]),\n    InitialDP1 = list_to_tuple(lists:duplicate(K\
        \ + 1, 0)),\n    {FinalDP0, FinalDP1} = lists:foldl(\n        fun(_, {DP0, DP1})\
        \ ->\n            compute_next(DP0, DP1, 0, K, MOD, [], [])\n        end,\n\
        \        {InitialDP0, InitialDP1},\n        lists:seq(1, N - 1)\n    ),\n  \
        \  (element(K + 1, FinalDP0) + element(K + 1, FinalDP1)) rem MOD.\n\ncompute_next(_DP0,\
        \ _DP1, J, K, _MOD, Acc0, Acc1) when J > K ->\n    {list_to_tuple(lists:reverse(Acc0)),\
        \ list_to_tuple(lists:reverse(Acc1))};\ncompute_next(DP0, DP1, J, K, MOD, Acc0,\
        \ Acc1) ->\n    V0 = (element(J + 1, DP0) + element(J + 1, DP1)) rem MOD,\n\
        \    V1 = if\n        J > 0 -> (element(J + 1, DP1) + hd(Acc0)) rem MOD;\n \
        \       true -> 0\n    end,\n    compute_next(DP0, DP1, J + 1, K, MOD, [V0 |\
        \ Acc0], [V1 | Acc1])."
      elixir: "defmodule Solution do\n  @spec number_of_sets(n :: integer, k :: integer)\
        \ :: integer\n  def number_of_sets(n, k) do\n    mod = 1_000_000_007\n    initial_dp0\
        \ = Tuple.duplicate(0, k + 1) |> put_elem(0, 1)\n    initial_dp1 = Tuple.duplicate(0,\
        \ k + 1)\n\n    {final_dp0, final_dp1} = Enum.reduce(1..(n - 1), {initial_dp0,\
        \ initial_dp1}, fn _, {dp0, dp1} ->\n      compute_next(dp0, dp1, 0, k, mod,\
        \ [], [])\n    end)\n\n    rem(elem(final_dp0, k) + elem(final_dp1, k), mod)\n\
        \  end\n\n  defp compute_next(_dp0, _dp1, j, k, _mod, acc0, acc1) when j > k\
        \ do\n    {List.to_tuple(Enum.reverse(acc0)), List.to_tuple(Enum.reverse(acc1))}\n\
        \  end\n\n  defp compute_next(dp0, dp1, j, k, mod, acc0, acc1) do\n    v0 =\
        \ rem(elem(dp0, j) + elem(dp1, j), mod)\n    v1 = if j > 0 do\n      rem(elem(dp1,\
        \ j) + hd(acc0), mod)\n    else\n      0\n    end\n    compute_next(dp0, dp1,\
        \ j + 1, k, mod, [v0 | acc0], [v1 | acc1])\n  end\nend"
    approach: 'This problem can be solved using dynamic programming by considering each
      point one by one and deciding whether it starts, continues, or ends a line segment.
      We define two DP states: ''dp0[j]'' as the number of ways to have ''j'' completed
      segments by the current point, and ''dp1[j]'' as the number of ways where ''j''
      segments have been started, with the ''j''-th segment still open (meaning it must
      cover the current point and may extend further).'
    time_complexity: O(n * k) because we iterate through $n$ points and for each point,
      we update the DP states for $k$ segments in constant time.
    space_complexity: O(k) as we only need to store the DP states for the current and
      previous points to compute the number of sets.
    elapsed_time: 1042.6731910705566
    model: gemini-3-flash-preview
    generated_at: '2026-09-16 02:57:38 '
---

## Problem #1621: Number of Sets of K Non-Overlapping Line Segments

**Difficulty:** Medium

**Topics:** Math, Dynamic Programming, Combinatorics, Prefix Sum

## Problem Description

<p>Given <code>n</code> points on a 1-D plane, where the <code>i<sup>th</sup></code> point (from <code>0</code> to <code>n-1</code>) is at <code>x = i</code>, find the number of ways we can draw <strong>exactly</strong> <code>k</code> <strong>non-overlapping</strong> line segments such that each segment covers two or more points. The endpoints of each segment must have <strong>integral coordinates</strong>. The <code>k</code> line segments <strong>do not</strong> have to cover all <code>n</code> points, and they are <strong>allowed</strong> to share endpoints.</p>

<p>Return <em>the number of ways we can draw </em><code>k</code><em> non-overlapping line segments</em><em>.</em> Since this number can be huge, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/07/ex1.png" style="width: 179px; height: 222px;" />
<pre>
<strong>Input:</strong> n = 4, k = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 30, k = 7
<strong>Output:</strong> 796297179
<strong>Explanation:</strong> The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 10<sup>9</sup> + 7 gives us 796297179.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= n-1</code></li>
</ul>


## Hints

1. Try to use dynamic programming where the current index and remaining number of line segments to form can describe any intermediate state.

2. To make the computation of each state in constant time, we could add another flag to the state that indicates whether or not we are in the middle of placing a line (placed start point but no endpoint).

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

This problem can be solved using dynamic programming by considering each point one by one and deciding whether it starts, continues, or ends a line segment. We define two DP states: 'dp0[j]' as the number of ways to have 'j' completed segments by the current point, and 'dp1[j]' as the number of ways where 'j' segments have been started, with the 'j'-th segment still open (meaning it must cover the current point and may extend further).

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
    int numberOfSets(int n, int k) {
        long long MOD = 1e9 + 7;
        vector<long long> dp0(k + 1, 0);
        vector<long long> dp1(k + 1, 0);
        dp0[0] = 1;
        for (int i = 1; i < n; ++i) {
            vector<long long> next_dp0(k + 1, 0);
            vector<long long> next_dp1(k + 1, 0);
            next_dp0[0] = 1;
            for (int j = 1; j <= k; ++j) {
                next_dp0[j] = (dp0[j] + dp1[j]) % MOD;
                next_dp1[j] = (dp1[j] + next_dp0[j - 1]) % MOD;
            }
            dp0 = next_dp0;
            dp1 = next_dp1;
        }
        return (dp0[k] + dp1[k]) % MOD;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numberOfSets(int n, int k) {
        long MOD = 1_000_000_007;
        long[] dp0 = new long[k + 1];
        long[] dp1 = new long[k + 1];
        dp0[0] = 1;
        for (int i = 1; i < n; i++) {
            long[] next_dp0 = new long[k + 1];
            long[] next_dp1 = new long[k + 1];
            next_dp0[0] = 1;
            for (int j = 1; j <= k; j++) {
                next_dp0[j] = (dp0[j] + dp1[j]) % MOD;
                next_dp1[j] = (dp1[j] + next_dp0[j - 1]) % MOD;
            }
            dp0 = next_dp0;
            dp1 = next_dp1;
        }
        return (int) ((dp0[k] + dp1[k]) % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp0 = [0] * (k + 1)
        dp1 = [0] * (k + 1)
        dp0[0] = 1
        for i in range(1, n):
            next_dp0 = [0] * (k + 1)
            next_dp1 = [0] * (k + 1)
            next_dp0[0] = 1
            for j in range(1, k + 1):
                next_dp0[j] = (dp0[j] + dp1[j]) % MOD
                next_dp1[j] = (dp1[j] + next_dp0[j-1]) % MOD
            dp0 = next_dp0
            dp1 = next_dp1
        return (dp0[k] + dp1[k]) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp0 = [0] * (k + 1)
        dp1 = [0] * (k + 1)
        dp0[0] = 1
        for i in range(1, n):
            next_dp0 = [0] * (k + 1)
            next_dp1 = [0] * (k + 1)
            next_dp0[0] = 1
            for j in range(1, k + 1):
                next_dp0[j] = (dp0[j] + dp1[j]) % MOD
                next_dp1[j] = (dp1[j] + next_dp0[j - 1]) % MOD
            dp0, dp1 = next_dp0, next_dp1
        return (dp0[k] + dp1[k]) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numberOfSets(int n, int k) {
    long long MOD = 1000000007;
    long long* dp0 = (long long*)calloc(k + 1, sizeof(long long));
    long long* dp1 = (long long*)calloc(k + 1, sizeof(long long));
    long long* next_dp0 = (long long*)calloc(k + 1, sizeof(long long));
    long long* next_dp1 = (long long*)calloc(k + 1, sizeof(long long));

    dp0[0] = 1;
    for (int i = 1; i < n; i++) {
        next_dp0[0] = 1;
        next_dp1[0] = 0;
        for (int j = 1; j <= k; j++) {
            next_dp0[j] = (dp0[j] + dp1[j]) % MOD;
            next_dp1[j] = (dp1[j] + next_dp0[j - 1]) % MOD;
        }
        for (int j = 0; j <= k; j++) {
            dp0[j] = next_dp0[j];
            dp1[j] = next_dp1[j];
        }
    }

    int ans = (int)((dp0[k] + dp1[k]) % MOD);
    free(dp0); free(dp1); free(next_dp0); free(next_dp1);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numberOfSets(n: Int, k: Int): Int {
        val mod = 1000000007
        val targetN = n + k - 1
        val targetK = 2 * k

        val dp = IntArray(targetK + 1)
        dp[0] = 1

        for (i in 1..targetN) {
            val limit = if (i < targetK) i else targetK
            for (j in limit downTo 1) {
                dp[j] = (dp[j] + dp[j - 1]) % mod
            }
        }

        return dp[targetK]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numberOfSets(int n, int k) {
    int mod = 1000000007;
    int targetN = n + k - 1;
    int targetK = 2 * k;

    List<int> dp = List.filled(targetK + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= targetN; i++) {
      int limit = i < targetK ? i : targetK;
      for (int j = limit; j >= 1; j--) {
        dp[j] = (dp[j] + dp[j - 1]) % mod;
      }
    }

    return dp[targetK];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numberOfSets(n int, k int) int {
    mod := 1000000007
    targetN := n + k - 1
    targetK := 2 * k

    dp := make([]int, targetK+1)
    dp[0] = 1

    for i := 1; i <= targetN; i++ {
        limit := i
        if limit > targetK {
            limit = targetK
        }
        for j := limit; j >= 1; j-- {
            dp[j] = (dp[j] + dp[j-1]) % mod
        }
    }

    return dp[targetK]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def number_of_sets(n, k)
  mod = 1_000_000_007
  target_n = n + k - 1
  target_k = 2 * k

  dp = Array.new(target_k + 1, 0)
  dp[0] = 1

  (1..target_n).each do |i|
    limit = i < target_k ? i : target_k
    limit.downto(1) do |j|
      dp[j] = (dp[j] + dp[j - 1]) % mod
    end
  end

  dp[target_k]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numberOfSets(n: Int, k: Int): Int = {
        val mod = 1000000007
        val targetN = n + k - 1
        val targetK = 2 * k

        val dp = new Array[Int](targetK + 1)
        dp(0) = 1

        for (i <- 1 to targetN) {
            val limit = if (i < targetK) i else targetK
            for (j <- limit to 1 by -1) {
                dp(j) = (dp(j) + dp(j - 1)) % mod
            }
        }

        dp(targetK)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn number_of_sets(n: i32, k: i32) -> i32 {
        let n = n as usize;
        let k = k as usize;
        let mod_val = 1_000_000_007;

        let mut dp0 = vec![0; k + 1];
        let mut dp1 = vec![0; k + 1];
        let mut next_dp0 = vec![0; k + 1];
        let mut next_dp1 = vec![0; k + 1];

        dp0[0] = 1;

        for _ in 1..n {
            for j in 0..=k {
                next_dp0[j] = (dp0[j] + dp1[j]) % mod_val;
                if j > 0 {
                    next_dp1[j] = (dp1[j] + next_dp0[j - 1]) % mod_val;
                } else {
                    next_dp1[j] = 0;
                }
            }
            std::mem::swap(&mut dp0, &mut next_dp0);
            std::mem::swap(&mut dp1, &mut next_dp1);
        }

        (dp0[k] + dp1[k]) % mod_val
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (number-of-sets n k)
  (-> exact-integer? exact-integer? exact-integer?)
  (let ([mod 1000000007])
    (let ([dp0 (make-vector (+ k 1) 0)]
          [dp1 (make-vector (+ k 1) 0)]
          [next-dp0 (make-vector (+ k 1) 0)]
          [next-dp1 (make-vector (+ k 1) 0)])
      (vector-set! dp0 0 1)
      (for ([i (in-range 1 n)])
        (for ([j (in-range (+ k 1))])
          (vector-set! next-dp0 j (remainder (+ (vector-ref dp0 j) (vector-ref dp1 j)) mod))
          (if (> j 0)
              (vector-set! next-dp1 j (remainder (+ (vector-ref dp1 j) (vector-ref next-dp0 (- j 1))) mod))
              (vector-set! next-dp1 j 0)))
        (for ([j (in-range (+ k 1))])
          (vector-set! dp0 j (vector-ref next-dp0 j))
          (vector-set! dp1 j (vector-ref next-dp1 j))))
      (remainder (+ (vector-ref dp0 k) (vector-ref dp1 k)) mod))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec number_of_sets(N :: integer(), K :: integer()) -> integer().
number_of_sets(N, K) ->
    MOD = 1000000007,
    InitialDP0 = list_to_tuple([1 | lists:duplicate(K, 0)]),
    InitialDP1 = list_to_tuple(lists:duplicate(K + 1, 0)),
    {FinalDP0, FinalDP1} = lists:foldl(
        fun(_, {DP0, DP1}) ->
            compute_next(DP0, DP1, 0, K, MOD, [], [])
        end,
        {InitialDP0, InitialDP1},
        lists:seq(1, N - 1)
    ),
    (element(K + 1, FinalDP0) + element(K + 1, FinalDP1)) rem MOD.

compute_next(_DP0, _DP1, J, K, _MOD, Acc0, Acc1) when J > K ->
    {list_to_tuple(lists:reverse(Acc0)), list_to_tuple(lists:reverse(Acc1))};
compute_next(DP0, DP1, J, K, MOD, Acc0, Acc1) ->
    V0 = (element(J + 1, DP0) + element(J + 1, DP1)) rem MOD,
    V1 = if
        J > 0 -> (element(J + 1, DP1) + hd(Acc0)) rem MOD;
        true -> 0
    end,
    compute_next(DP0, DP1, J + 1, K, MOD, [V0 | Acc0], [V1 | Acc1]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec number_of_sets(n :: integer, k :: integer) :: integer
  def number_of_sets(n, k) do
    mod = 1_000_000_007
    initial_dp0 = Tuple.duplicate(0, k + 1) |> put_elem(0, 1)
    initial_dp1 = Tuple.duplicate(0, k + 1)

    {final_dp0, final_dp1} = Enum.reduce(1..(n - 1), {initial_dp0, initial_dp1}, fn _, {dp0, dp1} ->
      compute_next(dp0, dp1, 0, k, mod, [], [])
    end)

    rem(elem(final_dp0, k) + elem(final_dp1, k), mod)
  end

  defp compute_next(_dp0, _dp1, j, k, _mod, acc0, acc1) when j > k do
    {List.to_tuple(Enum.reverse(acc0)), List.to_tuple(Enum.reverse(acc1))}
  end

  defp compute_next(dp0, dp1, j, k, mod, acc0, acc1) do
    v0 = rem(elem(dp0, j) + elem(dp1, j), mod)
    v1 = if j > 0 do
      rem(elem(dp1, j) + hd(acc0), mod)
    else
      0
    end
    compute_next(dp0, dp1, j + 1, k, mod, [v0 | acc0], [v1 | acc1])
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * k) because we iterate through $n$ points and for each point, we update the DP states for $k$ segments in constant time.
- **Space Complexity:** O(k) as we only need to store the DP states for the current and previous points to compute the number of sets.
