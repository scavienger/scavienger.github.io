---
layout: post
title: "Climbing Stairs II"
date: 2026-11-10 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/climbing-stairs-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int climbStairs(int n, vector<int>& costs)\
        \ {\n        vector<int> dp(n + 1, INT_MAX);\n        dp[0] = 0;\n        for\
        \ (int j = 1; j <= n; ++j) {\n            for (int jump = 1; jump <= 3 && jump\
        \ <= j; ++jump) {\n                int i = j - jump;\n                dp[j]\
        \ = min(dp[j], dp[i] + costs[j - 1] + jump * jump);\n            }\n       \
        \ }\n        return dp[n];\n    }\n};"
      java: "class Solution {\n    public int climbStairs(int n, int[] costs) {\n  \
        \      int[] dp = new int[n + 1];\n        java.util.Arrays.fill(dp, Integer.MAX_VALUE);\n\
        \        dp[0] = 0;\n        for (int j = 1; j <= n; j++) {\n            for\
        \ (int jump = 1; jump <= 3 && jump <= j; jump++) {\n                int i =\
        \ j - jump;\n                dp[j] = Math.min(dp[j], dp[i] + costs[j - 1] +\
        \ jump * jump);\n            }\n        }\n        return dp[n];\n    }\n}"
      python: "class Solution(object):\n    def climbStairs(self, n, costs):\n     \
        \   \"\"\"\n        :type n: int\n        :type costs: List[int]\n        :rtype:\
        \ int\n        \"\"\"\n        dp = [float('inf')] * (n + 1)\n        dp[0]\
        \ = 0\n        for j in range(1, n + 1):\n            for jump in range(1, min(3,\
        \ j) + 1):\n                i = j - jump\n                dp[j] = min(dp[j],\
        \ dp[i] + costs[j - 1] + jump * jump)\n        return dp[n]"
      python3: "class Solution:\n    def climbStairs(self, n: int, costs: List[int])\
        \ -> int:\n        dp = [float('inf')] * (n + 1)\n        dp[0] = 0\n      \
        \  for j in range(1, n + 1):\n            for jump in range(1, min(3, j) + 1):\n\
        \                i = j - jump\n                dp[j] = min(dp[j], dp[i] + costs[j\
        \ - 1] + jump * jump)\n        return dp[n]"
      c: "int climbStairs(int n, int* costs, int costsSize) {\n    int* dp = (int*)malloc((n\
        \ + 1) * sizeof(int));\n    for (int i = 0; i <= n; ++i) {\n        dp[i] =\
        \ INT_MAX;\n    }\n    dp[0] = 0;\n    for (int j = 1; j <= n; ++j) {\n    \
        \    for (int jump = 1; jump <= 3 && jump <= j; ++jump) {\n            int i\
        \ = j - jump;\n            int candidate = dp[i] + costs[j - 1] + jump * jump;\n\
        \            if (candidate < dp[j]) {\n                dp[j] = candidate;\n\
        \            }\n        }\n    }\n    int result = dp[n];\n    free(dp);\n \
        \   return result;\n}"
      csharp: "public class Solution {\n    public int ClimbStairs(int n, int[] costs)\
        \ {\n        int[] dp = new int[n + 1];\n        Array.Fill(dp, int.MaxValue);\n\
        \        dp[0] = 0;\n        for (int j = 1; j <= n; j++) {\n            for\
        \ (int jump = 1; jump <= Math.Min(3, j); jump++) {\n                int i =\
        \ j - jump;\n                dp[j] = Math.Min(dp[j], dp[i] + costs[j - 1] +\
        \ jump * jump);\n            }\n        }\n        return dp[n];\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[]} costs\n * @return\
        \ {number}\n */\nvar climbStairs = function(n, costs) {\n    const dp = new\
        \ Array(n + 1).fill(Infinity);\n    dp[0] = 0;\n    for (let j = 1; j <= n;\
        \ j++) {\n        for (let jump = 1; jump <= Math.min(3, j); jump++) {\n   \
        \         const i = j - jump;\n            dp[j] = Math.min(dp[j], dp[i] + costs[j\
        \ - 1] + jump * jump);\n        }\n    }\n    return dp[n];\n};"
      typescript: "function climbStairs(n: number, costs: number[]): number {\n    const\
        \ dp: number[] = new Array(n + 1).fill(Infinity);\n    dp[0] = 0;\n    for (let\
        \ j = 1; j <= n; j++) {\n        for (let jump = 1; jump <= Math.min(3, j);\
        \ jump++) {\n            const i = j - jump;\n            dp[j] = Math.min(dp[j],\
        \ dp[i] + costs[j - 1] + jump * jump);\n        }\n    }\n    return dp[n];\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[]\
        \ $costs\n     * @return Integer\n     */\n    function climbStairs($n, $costs)\
        \ {\n        $dp = array_fill(0, $n + 1, PHP_INT_MAX);\n        $dp[0] = 0;\n\
        \        for ($j = 1; $j <= $n; $j++) {\n            for ($jump = 1; $jump <=\
        \ min(3, $j); $jump++) {\n                $i = $j - $jump;\n               \
        \ $dp[$j] = min($dp[$j], $dp[$i] + $costs[$j - 1] + $jump * $jump);\n      \
        \      }\n        }\n        return $dp[$n];\n    }\n}"
      swift: "class Solution {\n    func climbStairs(_ n: Int, _ costs: [Int]) -> Int\
        \ {\n        var dp = Array(repeating: Int.max, count: n + 1)\n        dp[0]\
        \ = 0\n        for j in 1...n {\n            for jump in 1...min(3, j) {\n \
        \               let i = j - jump\n                dp[j] = min(dp[j], dp[i] +\
        \ costs[j - 1] + jump * jump)\n            }\n        }\n        return dp[n]\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun climbStairs(n: Int, costs: IntArray): Int {\n\
        \        val dp = IntArray(n + 1) { Int.MAX_VALUE }\n        dp[0] = 0\n   \
        \     for (j in 1..n) {\n            for (jump in 1..minOf(3, j)) {\n      \
        \          val i = j - jump\n                dp[j] = minOf(dp[j], dp[i] + costs[j\
        \ - 1] + jump * jump)\n            }\n        }\n        return dp[n]\n    }\n\
        }"
      dart: "class Solution {\n  int climbStairs(int n, List<int> costs) {\n    final\
        \ dp = List<int>.filled(n + 1, 0x7fffffff);\n    dp[0] = 0;\n    for (var j\
        \ = 1; j <= n; j++) {\n      for (var jump = 1; jump <= (j < 3 ? j : 3); jump++)\
        \ {\n        final i = j - jump;\n        final candidate = dp[i] + costs[j\
        \ - 1] + jump * jump;\n        if (candidate < dp[j]) {\n          dp[j] = candidate;\n\
        \        }\n      }\n    }\n    return dp[n];\n  }\n}"
      go: "func climbStairs(n int, costs []int) int {\n\tdp := make([]int, n+1)\n\t\
        for i := range dp {\n\t\tdp[i] = int(^uint(0) >> 1)\n\t}\n\tdp[0] = 0\n\tfor\
        \ j := 1; j <= n; j++ {\n\t\tfor jump := 1; jump <= 3 && jump <= j; jump++ {\n\
        \t\t\ti := j - jump\n\t\t\tcandidate := dp[i] + costs[j-1] + jump*jump\n\t\t\
        \tif candidate < dp[j] {\n\t\t\t\tdp[j] = candidate\n\t\t\t}\n\t\t}\n\t}\n\t\
        return dp[n]\n}"
      ruby: "# @param {Integer} n\n# @param {Integer[]} costs\n# @return {Integer}\n\
        def climb_stairs(n, costs)\n  dp = Array.new(n + 1, Float::INFINITY)\n  dp[0]\
        \ = 0\n  (1..n).each do |j|\n    1.upto([3, j].min) do |jump|\n      i = j -\
        \ jump\n      candidate = dp[i] + costs[j - 1] + jump * jump\n      dp[j] =\
        \ candidate if candidate < dp[j]\n    end\n  end\n  dp[n]\nend"
      scala: "object Solution {\n    def climbStairs(n: Int, costs: Array[Int]): Int\
        \ = {\n        val dp = Array.fill(n + 1)(Int.MaxValue)\n        dp(0) = 0\n\
        \        for (j <- 1 to n) {\n            for (jump <- 1 to math.min(3, j))\
        \ {\n                val i = j - jump\n                val candidate = dp(i)\
        \ + costs(j - 1) + jump * jump\n                if (candidate < dp(j)) {\n \
        \                   dp(j) = candidate\n                }\n            }\n  \
        \      }\n        dp(n)\n    }\n}"
      rust: "impl Solution {\n    pub fn climb_stairs(n: i32, costs: Vec<i32>) -> i32\
        \ {\n        let n = n as usize;\n        let mut dp = vec![i32::MAX; n + 1];\n\
        \        dp[0] = 0;\n\n        for j in 1..=n {\n            for jump in 1..=3.min(j)\
        \ {\n                let i = j - jump;\n                let candidate = dp[i]\
        \ + costs[j - 1] + (jump * jump) as i32;\n                dp[j] = dp[j].min(candidate);\n\
        \            }\n        }\n\n        dp[n]\n    }\n}"
      racket: "(define/contract (climb-stairs n costs)\n  (-> exact-integer? (listof\
        \ exact-integer?) exact-integer?)\n  (define dp (make-vector (+ n 1) +inf.0))\n\
        \  (vector-set! dp 0 0)\n  (for ([j (in-range 1 (+ n 1))])\n    (for ([jump\
        \ (in-range 1 (+ (min 3 j) 1))])\n      (define i (- j jump))\n      (define\
        \ candidate (+ (vector-ref dp i)\n                           (list-ref costs\
        \ (- j 1))\n                           (* jump jump)))\n      (vector-set! dp\
        \ j (min (vector-ref dp j) candidate)))\n  )\n  (vector-ref dp n))"
      erlang: "-spec climb_stairs(N :: integer(), Costs :: [integer()]) -> integer().\n\
        climb_stairs(N, Costs) ->\n  climb_stairs(N, Costs, [0]).\n\nclimb_stairs(N,\
        \ _Costs, [Result | _] = Dp) when length(Dp) =:= N + 1 ->\n  Result;\nclimb_stairs(N,\
        \ Costs, Dp) ->\n  J = length(Dp),\n  Cost = lists:nth(J, Costs),\n  Candidates\
        \ = [lists:nth(J - Jump + 1, Dp) + Cost + Jump * Jump\n                || Jump\
        \ <- lists:seq(1, min(3, J))],\n  climb_stairs(N, Costs, [lists:min(Candidates)\
        \ | Dp])."
      elixir: "defmodule Solution do\n  @spec climb_stairs(n :: integer, costs :: [integer])\
        \ :: integer\n  def climb_stairs(n, costs) do\n    dp = Enum.reduce(1..n, [0],\
        \ fn j, acc ->\n      best =\n        1..min(3, j)\n        |> Enum.map(fn jump\
        \ ->\n          Enum.at(acc, jump - 1) + Enum.at(costs, j - 1) + jump * jump\n\
        \        end)\n        |> Enum.min()\n\n      [best | acc]\n    end)\n\n   \
        \ hd(dp)\n  end\nend"
    approach: 'Let dp[j] be the minimum cost to reach step j, with dp[0] = 0. For each
      step j from 1 through n, consider jumps from j-1, j-2, and j-3 when those steps
      are nonnegative.


      For each valid predecessor i, the transition cost is dp[i] + costs[j-1] + (j-i)^2,
      since the costs array is zero-indexed in code. Take the minimum of these candidates;
      the result is dp[n].'
    time_complexity: O(n), since each step checks at most three possible predecessors.
    space_complexity: O(n), for the dynamic programming array.
    elapsed_time: 66.00475907325745
    model: gpt-6-luna
    generated_at: '2026-11-12 23:49:12 '
---

## Problem #3693: Climbing Stairs II

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming

## Problem Description

<p>You are climbing a staircase with <code>n + 1</code> steps, numbered from 0 to <code>n</code>.</p>

<p>You are also given a <strong>1-indexed</strong> integer array <code>costs</code> of length <code>n</code>, where <code>costs[i]</code> is the cost of step <code>i</code>.</p>

<p>From step <code>i</code>, you can jump <strong>only</strong> to step <code>i + 1</code>, <code>i + 2</code>, or <code>i + 3</code>. The cost of jumping from step <code>i</code> to step <code>j</code> is defined as: <code>costs[j] + (j - i)<sup>2</sup></code></p>

<p>You start from step 0 with <code>cost = 0</code>.</p>

<p>Return the <strong>minimum</strong> total cost to reach step <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, costs = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal path is <code>0 &rarr; 1 &rarr; 2 &rarr; 4</code></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Jump</th>
			<th style="border: 1px solid black;">Cost Calculation</th>
			<th style="border: 1px solid black;">Cost</th>
		</tr>
	</tbody>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0 &rarr; 1</td>
			<td style="border: 1px solid black;"><code>costs[1] + (1 - 0)<sup>2</sup> = 1 + 1</code></td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1 &rarr; 2</td>
			<td style="border: 1px solid black;"><code>costs[2] + (2 - 1)<sup>2</sup> = 2 + 1</code></td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2 &rarr; 4</td>
			<td style="border: 1px solid black;"><code>costs[4] + (4 - 2)<sup>2</sup> = 4 + 4</code></td>
			<td style="border: 1px solid black;">8</td>
		</tr>
	</tbody>
</table>

<p>Thus, the minimum total cost is <code>2 + 3 + 8 = 13</code></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, costs = [5,1,6,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal path is <code>0 &rarr; 2 &rarr; 4</code></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Jump</th>
			<th style="border: 1px solid black;">Cost Calculation</th>
			<th style="border: 1px solid black;">Cost</th>
		</tr>
	</tbody>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0 &rarr; 2</td>
			<td style="border: 1px solid black;"><code>costs[2] + (2 - 0)<sup>2</sup> = 1 + 4</code></td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2 &rarr; 4</td>
			<td style="border: 1px solid black;"><code>costs[4] + (4 - 2)<sup>2</sup> = 2 + 4</code></td>
			<td style="border: 1px solid black;">6</td>
		</tr>
	</tbody>
</table>

<p>Thus, the minimum total cost is <code>5 + 6 = 11</code></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, costs = [9,8,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal path is <code>0 &rarr; 3</code> with total cost = <code>costs[3] + (3 - 0)<sup>2</sup> = 3 + 9 = 12</code></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == costs.length &lt;= 10<sup>5</sup>​​​​​​​</code></li>
	<li><code>1 &lt;= costs[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. Use dynamic programming where `dp[j]` represents the minimum cost to reach step `j`.

2. From step `i`, you can jump to `i+1`, `i+2`, or `i+3`. Transition depends only on the previous three states.

3. `dp[j] = min(dp[i] + costs[j] + (j - i)^2)` for all `i` in {`j-1`, `j-2`, `j-3`}.

4. Initialize `dp[0] = 0` and compute up to `dp[n]`; the answer is `dp[n]`.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Let dp[j] be the minimum cost to reach step j, with dp[0] = 0. For each step j from 1 through n, consider jumps from j-1, j-2, and j-3 when those steps are nonnegative.

For each valid predecessor i, the transition cost is dp[i] + costs[j-1] + (j-i)^2, since the costs array is zero-indexed in code. Take the minimum of these candidates; the result is dp[n].

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
    int climbStairs(int n, vector<int>& costs) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (int j = 1; j <= n; ++j) {
            for (int jump = 1; jump <= 3 && jump <= j; ++jump) {
                int i = j - jump;
                dp[j] = min(dp[j], dp[i] + costs[j - 1] + jump * jump);
            }
        }
        return dp[n];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int climbStairs(int n, int[] costs) {
        int[] dp = new int[n + 1];
        java.util.Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int j = 1; j <= n; j++) {
            for (int jump = 1; jump <= 3 && jump <= j; jump++) {
                int i = j - jump;
                dp[j] = Math.min(dp[j], dp[i] + costs[j - 1] + jump * jump);
            }
        }
        return dp[n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            for jump in range(1, min(3, j) + 1):
                i = j - jump
                dp[j] = min(dp[j], dp[i] + costs[j - 1] + jump * jump)
        return dp[n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            for jump in range(1, min(3, j) + 1):
                i = j - jump
                dp[j] = min(dp[j], dp[i] + costs[j - 1] + jump * jump)
        return dp[n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int climbStairs(int n, int* costs, int costsSize) {
    int* dp = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; ++i) {
        dp[i] = INT_MAX;
    }
    dp[0] = 0;
    for (int j = 1; j <= n; ++j) {
        for (int jump = 1; jump <= 3 && jump <= j; ++jump) {
            int i = j - jump;
            int candidate = dp[i] + costs[j - 1] + jump * jump;
            if (candidate < dp[j]) {
                dp[j] = candidate;
            }
        }
    }
    int result = dp[n];
    free(dp);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int ClimbStairs(int n, int[] costs) {
        int[] dp = new int[n + 1];
        Array.Fill(dp, int.MaxValue);
        dp[0] = 0;
        for (int j = 1; j <= n; j++) {
            for (int jump = 1; jump <= Math.Min(3, j); jump++) {
                int i = j - jump;
                dp[j] = Math.Min(dp[j], dp[i] + costs[j - 1] + jump * jump);
            }
        }
        return dp[n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @param {number[]} costs
 * @return {number}
 */
var climbStairs = function(n, costs) {
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;
    for (let j = 1; j <= n; j++) {
        for (let jump = 1; jump <= Math.min(3, j); jump++) {
            const i = j - jump;
            dp[j] = Math.min(dp[j], dp[i] + costs[j - 1] + jump * jump);
        }
    }
    return dp[n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function climbStairs(n: number, costs: number[]): number {
    const dp: number[] = new Array(n + 1).fill(Infinity);
    dp[0] = 0;
    for (let j = 1; j <= n; j++) {
        for (let jump = 1; jump <= Math.min(3, j); jump++) {
            const i = j - jump;
            dp[j] = Math.min(dp[j], dp[i] + costs[j - 1] + jump * jump);
        }
    }
    return dp[n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $costs
     * @return Integer
     */
    function climbStairs($n, $costs) {
        $dp = array_fill(0, $n + 1, PHP_INT_MAX);
        $dp[0] = 0;
        for ($j = 1; $j <= $n; $j++) {
            for ($jump = 1; $jump <= min(3, $j); $jump++) {
                $i = $j - $jump;
                $dp[$j] = min($dp[$j], $dp[$i] + $costs[$j - 1] + $jump * $jump);
            }
        }
        return $dp[$n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func climbStairs(_ n: Int, _ costs: [Int]) -> Int {
        var dp = Array(repeating: Int.max, count: n + 1)
        dp[0] = 0
        for j in 1...n {
            for jump in 1...min(3, j) {
                let i = j - jump
                dp[j] = min(dp[j], dp[i] + costs[j - 1] + jump * jump)
            }
        }
        return dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun climbStairs(n: Int, costs: IntArray): Int {
        val dp = IntArray(n + 1) { Int.MAX_VALUE }
        dp[0] = 0
        for (j in 1..n) {
            for (jump in 1..minOf(3, j)) {
                val i = j - jump
                dp[j] = minOf(dp[j], dp[i] + costs[j - 1] + jump * jump)
            }
        }
        return dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int climbStairs(int n, List<int> costs) {
    final dp = List<int>.filled(n + 1, 0x7fffffff);
    dp[0] = 0;
    for (var j = 1; j <= n; j++) {
      for (var jump = 1; jump <= (j < 3 ? j : 3); jump++) {
        final i = j - jump;
        final candidate = dp[i] + costs[j - 1] + jump * jump;
        if (candidate < dp[j]) {
          dp[j] = candidate;
        }
      }
    }
    return dp[n];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func climbStairs(n int, costs []int) int {
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = int(^uint(0) >> 1)
	}
	dp[0] = 0
	for j := 1; j <= n; j++ {
		for jump := 1; jump <= 3 && jump <= j; jump++ {
			i := j - jump
			candidate := dp[i] + costs[j-1] + jump*jump
			if candidate < dp[j] {
				dp[j] = candidate
			}
		}
	}
	return dp[n]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[]} costs
# @return {Integer}
def climb_stairs(n, costs)
  dp = Array.new(n + 1, Float::INFINITY)
  dp[0] = 0
  (1..n).each do |j|
    1.upto([3, j].min) do |jump|
      i = j - jump
      candidate = dp[i] + costs[j - 1] + jump * jump
      dp[j] = candidate if candidate < dp[j]
    end
  end
  dp[n]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def climbStairs(n: Int, costs: Array[Int]): Int = {
        val dp = Array.fill(n + 1)(Int.MaxValue)
        dp(0) = 0
        for (j <- 1 to n) {
            for (jump <- 1 to math.min(3, j)) {
                val i = j - jump
                val candidate = dp(i) + costs(j - 1) + jump * jump
                if (candidate < dp(j)) {
                    dp(j) = candidate
                }
            }
        }
        dp(n)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn climb_stairs(n: i32, costs: Vec<i32>) -> i32 {
        let n = n as usize;
        let mut dp = vec![i32::MAX; n + 1];
        dp[0] = 0;

        for j in 1..=n {
            for jump in 1..=3.min(j) {
                let i = j - jump;
                let candidate = dp[i] + costs[j - 1] + (jump * jump) as i32;
                dp[j] = dp[j].min(candidate);
            }
        }

        dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (climb-stairs n costs)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (define dp (make-vector (+ n 1) +inf.0))
  (vector-set! dp 0 0)
  (for ([j (in-range 1 (+ n 1))])
    (for ([jump (in-range 1 (+ (min 3 j) 1))])
      (define i (- j jump))
      (define candidate (+ (vector-ref dp i)
                           (list-ref costs (- j 1))
                           (* jump jump)))
      (vector-set! dp j (min (vector-ref dp j) candidate)))
  )
  (vector-ref dp n))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec climb_stairs(N :: integer(), Costs :: [integer()]) -> integer().
climb_stairs(N, Costs) ->
  climb_stairs(N, Costs, [0]).

climb_stairs(N, _Costs, [Result | _] = Dp) when length(Dp) =:= N + 1 ->
  Result;
climb_stairs(N, Costs, Dp) ->
  J = length(Dp),
  Cost = lists:nth(J, Costs),
  Candidates = [lists:nth(J - Jump + 1, Dp) + Cost + Jump * Jump
                || Jump <- lists:seq(1, min(3, J))],
  climb_stairs(N, Costs, [lists:min(Candidates) | Dp]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec climb_stairs(n :: integer, costs :: [integer]) :: integer
  def climb_stairs(n, costs) do
    dp = Enum.reduce(1..n, [0], fn j, acc ->
      best =
        1..min(3, j)
        |> Enum.map(fn jump ->
          Enum.at(acc, jump - 1) + Enum.at(costs, j - 1) + jump * jump
        end)
        |> Enum.min()

      [best | acc]
    end)

    hd(dp)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), since each step checks at most three possible predecessors.
- **Space Complexity:** O(n), for the dynamic programming array.
