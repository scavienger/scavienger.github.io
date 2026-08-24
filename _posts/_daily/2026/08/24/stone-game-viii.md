---
layout: post
title: "Stone Game VIII"
date: 2026-08-24 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Dynamic Programming", "Minimax", "Prefix Sum", "Game Theory", "Zero-Sum Game"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/stone-game-viii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int stoneGameVIII(vector<int>& stones) {\n\
        \        int n = stones.size();\n        long long currentSum = 0;\n       \
        \ for (int s : stones) {\n            currentSum += s;\n        }\n\n      \
        \  long long res = currentSum;\n        for (int i = n - 1; i > 1; --i) {\n\
        \            currentSum -= stones[i];\n            long long diff = currentSum\
        \ - res;\n            if (diff > res) {\n                res = diff;\n     \
        \       }\n        }\n\n        return (int)res;\n    }\n};"
      java: "class Solution {\n    public int stoneGameVIII(int[] stones) {\n      \
        \  int n = stones.length;\n        long currentSum = 0;\n        for (int s\
        \ : stones) {\n            currentSum += s;\n        }\n\n        long res =\
        \ currentSum;\n        for (int i = n - 1; i > 1; i--) {\n            currentSum\
        \ -= stones[i];\n            long diff = currentSum - res;\n            if (diff\
        \ > res) {\n                res = diff;\n            }\n        }\n\n      \
        \  return (int) res;\n    }\n}"
      python: "class Solution(object):\n    def stoneGameVIII(self, stones):\n     \
        \   \"\"\"\n        :type stones: List[int]\n        :rtype: int\n        \"\
        \"\"\n        n = len(stones)\n        current_sum = sum(stones)\n        #\
        \ Base case: Alice picks all stones (index n-1 in prefix sum array)\n      \
        \  res = current_sum\n        # Iterate backwards from index n-2 down to index\
        \ 1\n        for i in range(n - 1, 1, -1):\n            current_sum -= stones[i]\n\
        \            # dp[i] = max(dp[i+1], prefixSum[i] - dp[i+1])\n            # We\
        \ update 'res' in place to represent dp[i]\n            diff = current_sum -\
        \ res\n            if diff > res:\n                res = diff\n        return\
        \ res"
      python3: "class Solution:\n    def stoneGameVIII(self, stones: List[int]) -> int:\n\
        \        n = len(stones)\n        curr_p = sum(stones)\n        dp = curr_p\n\
        \        for i in range(n - 2, 0, -1):\n            curr_p -= stones[i + 1]\n\
        \            diff = curr_p - dp\n            if diff > dp:\n               \
        \ dp = diff\n        return dp"
      c: "int stoneGameVIII(int* stones, int stonesSize) {\n    long long currentP =\
        \ 0;\n    for (int i = 0; i < stonesSize; i++) {\n        currentP += stones[i];\n\
        \    }\n    long long dp = currentP;\n    for (int i = stonesSize - 2; i >=\
        \ 1; i--) {\n        currentP -= (long long)stones[i + 1];\n        long long\
        \ diff = currentP - dp;\n        if (diff > dp) {\n            dp = diff;\n\
        \        }\n    }\n    return (int)dp;\n}"
      csharp: "public class Solution {\n    public int StoneGameVIII(int[] stones) {\n\
        \        int n = stones.Length;\n        long currentP = 0;\n        for (int\
        \ i = 0; i < n; i++) {\n            currentP += (long)stones[i];\n        }\n\
        \        long dp = currentP;\n        for (int i = n - 2; i >= 1; i--) {\n \
        \           currentP -= (long)stones[i + 1];\n            long diff = currentP\
        \ - dp;\n            if (diff > dp) {\n                dp = diff;\n        \
        \    }\n        }\n        return (int)dp;\n    }\n}"
      javascript: "/**\n * @param {number[]} stones\n * @return {number}\n */\nvar stoneGameVIII\
        \ = function(stones) {\n    let n = stones.length;\n    let currentP = 0;\n\
        \    for (let i = 0; i < n; i++) {\n        currentP += stones[i];\n    }\n\
        \    let dp = currentP;\n    for (let i = n - 2; i >= 1; i--) {\n        currentP\
        \ -= stones[i + 1];\n        let diff = currentP - dp;\n        if (diff > dp)\
        \ {\n            dp = diff;\n        }\n    }\n    return dp;\n};"
      typescript: "function stoneGameVIII(stones: number[]): number {\n    const n =\
        \ stones.length;\n    let totalSum = stones.reduce((acc, val) => acc + val,\
        \ 0);\n    let res = totalSum;\n    let currentP = totalSum;\n    for (let i\
        \ = n - 2; i >= 1; i--) {\n        currentP -= stones[i + 1];\n        res =\
        \ Math.max(res, currentP - res);\n    }\n    return res;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $stones\n     * @return\
        \ Integer\n     */\n    function stoneGameVIII($stones) {\n        $n = count($stones);\n\
        \        $totalSum = array_sum($stones);\n        $res = $totalSum;\n      \
        \  $currentP = $totalSum;\n        for ($i = $n - 2; $i >= 1; $i--) {\n    \
        \        $currentP -= $stones[$i + 1];\n            $res = max($res, $currentP\
        \ - $res);\n        }\n        return (int)$res;\n    }\n}"
      swift: "class Solution {\n    func stoneGameVIII(_ stones: [Int]) -> Int {\n \
        \       let n = stones.count\n        let totalSum = stones.reduce(0, +)\n \
        \       var res = totalSum\n        var currentP = totalSum\n        if n >\
        \ 2 {\n            for i in stride(from: n - 2, through: 1, by: -1) {\n    \
        \            currentP -= stones[i + 1]\n                res = max(res, currentP\
        \ - res)\n            }\n        } else if n == 2 {\n            return totalSum\n\
        \        }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun stoneGameVIII(stones: IntArray): Int {\n  \
        \      val n = stones.size\n        var totalSum: Long = 0\n        for (s in\
        \ stones) {\n            totalSum += s\n        }\n        var res: Long = totalSum\n\
        \        var currentP: Long = totalSum\n        for (i in n - 2 downTo 1) {\n\
        \            currentP -= stones[i + 1]\n            res = Math.max(res, currentP\
        \ - res)\n        }\n        return res.toInt()\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int stoneGameVIII(List<int>\
        \ stones) {\n    int n = stones.length;\n    int totalSum = 0;\n    for (int\
        \ i = 0; i < n; i++) {\n      totalSum += stones[i];\n    }\n\n    int dp =\
        \ totalSum;\n    int currSum = totalSum;\n\n    for (int i = n - 1; i >= 2;\
        \ i--) {\n      currSum -= stones[i];\n      int diff = currSum - dp;\n    \
        \  if (diff > dp) {\n        dp = diff;\n      }\n    }\n\n    return dp;\n\
        \  }\n}"
      go: "func stoneGameVIII(stones []int) int {\n    n := len(stones)\n    totalSum\
        \ := 0\n    for _, s := range stones {\n        totalSum += s\n    }\n\n   \
        \ dp := totalSum\n    currentPrefixSum := totalSum\n\n    for i := n - 1; i\
        \ >= 2; i-- {\n        currentPrefixSum -= stones[i]\n        diff := currentPrefixSum\
        \ - dp\n        if diff > dp {\n            dp = diff\n        }\n    }\n\n\
        \    return dp\n}"
      ruby: "# @param {Integer[]} stones\n# @return {Integer}\ndef stone_game_viii(stones)\n\
        \  n = stones.length\n  total_sum = stones.sum\n  dp = total_sum\n  curr_sum\
        \ = total_sum\n\n  (n - 1).downto(2) do |i|\n    curr_sum -= stones[i]\n   \
        \ diff = curr_sum - dp\n    dp = diff if diff > dp\n  end\n\n  dp\nend"
      scala: "object Solution {\n    def stoneGameVIII(stones: Array[Int]): Int = {\n\
        \        val n = stones.length\n        var totalSum: Long = 0L\n        var\
        \ i = 0\n        while (i < n) {\n            totalSum += stones(i).toLong\n\
        \            i += 1\n        }\n\n        var dp: Long = totalSum\n        var\
        \ currSum: Long = totalSum\n        var j = n - 1\n\n        while (j >= 2)\
        \ {\n            currSum -= stones(j).toLong\n            val diff = currSum\
        \ - dp\n            if (diff > dp) {\n                dp = diff\n          \
        \  }\n            j -= 1\n        }\n\n        dp.toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn stone_game_viii(stones: Vec<i32>) -> i32 {\n\
        \        let n = stones.len();\n        let mut p: Vec<i64> = vec![0; n + 1];\n\
        \        for i in 0..n {\n            p[i + 1] = p[i] + stones[i] as i64;\n\
        \        }\n\n        let mut current_f = p[n];\n        for i in (2..n).rev()\
        \ {\n            current_f = std::cmp::max(p[i] - current_f, current_f);\n \
        \       }\n\n        current_f as i32\n    }\n}"
      racket: "(define/contract (stone-game-viii stones)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([n (length stones)]\n         [p (make-vector (+\
        \ n 1) 0)])\n    (for ([i (in-range n)]\n          [s stones])\n      (vector-set!\
        \ p (+ i 1) (+ (vector-ref p i) s)))\n    (let loop ([i (- n 1)]\n         \
        \      [current-f (vector-ref p n)])\n      (if (< i 2)\n          current-f\n\
        \          (loop (- i 1) (max (- (vector-ref p i) current-f) current-f))))))"
      erlang: "-spec stone_game_viii(Stones :: [integer()]) -> integer().\nstone_game_viii(Stones)\
        \ ->\n    [Pn | Rest] = lists:foldl(fun(X, [H | T]) -> [X + H, H | T] end, [0],\
        \ Stones),\n    process(Rest, Pn, length(Stones) - 2).\n\nprocess([Pi | Rest],\
        \ CurrentF, Count) when Count > 0 ->\n    process(Rest, erlang:max(Pi - CurrentF,\
        \ CurrentF), Count - 1);\nprocess(_, CurrentF, _) ->\n    CurrentF."
      elixir: "defmodule Solution do\n  @spec stone_game_viii(stones :: [integer]) ::\
        \ integer\n  def stone_game_viii(stones) do\n    [pn | rest] = Enum.reduce(stones,\
        \ [0], fn x, [h | t] -> [x + h, h | t] end)\n    process(rest, pn, length(stones)\
        \ - 2)\n  end\n\n  defp process([pi | rest], current_f, count) when count >\
        \ 0 do\n    process(rest, max(pi - current_f, current_f), count - 1)\n  end\n\
        \n  defp process(_, current_f, _count) do\n    current_f\n  end\nend"
    approach: The problem can be modeled as a game theory problem solvable with dynamic
      programming. The core observation is that removing the leftmost $x$ stones and
      replacing them with a single stone of value $S$ (the sum of the $x$ removed stones)
      is equivalent to choosing an index $i = x - 1$ in the prefix sum array $P$ of
      the original stones. Because every subsequent removal adds its sum to a single
      leftmost stone, any future move that removes $y$ stones from the current row corresponds
      to choosing a prefix sum $P[j]$ from the original array such that $j > i$. Alice
      aims to maximize the difference between her score and Bob's, while Bob aims to
      minimize it (which is equivalent to Bob maximizing his own score relative to Alice's).
    time_complexity: O(n) where n is the number of stones. The algorithm involves a
      single pass to calculate the total sum of the stones and a second pass from the
      end of the prefix sum array to the second element ($P[1]$) to compute the optimal
      score difference using dynamic programming.
    space_complexity: O(1) extra space. While the input array takes O(n) space, the
      algorithm only requires a few auxiliary variables to keep track of the current
      prefix sum and the maximum score difference found so far, as prefix sums are computed
      on the fly by subtracting elements from the total sum.
    elapsed_time: 295.1564474105835
    model: gemini-3-flash-preview
    generated_at: '2026-08-24 00:54:48 '
---

## Problem #1872: Stone Game VIII

**Difficulty:** Hard

**Topics:** Array, Math, Dynamic Programming, Minimax, Prefix Sum, Game Theory, Zero-Sum Game

## Problem Description

<p>Alice and Bob take turns playing a game, with <strong>Alice starting first</strong>.</p>

<p>There are <code>n</code> stones arranged in a row. On each player&#39;s turn, while the number of stones is <strong>more than one</strong>, they will do the following:</p>

<ol>
	<li>Choose an integer <code>x &gt; 1</code>, and <strong>remove</strong> the leftmost <code>x</code> stones from the row.</li>
	<li>Add the <strong>sum</strong> of the <strong>removed</strong> stones&#39; values to the player&#39;s score.</li>
	<li>Place a <strong>new stone</strong>, whose value is equal to that sum, on the left side of the row.</li>
</ol>

<p>The game stops when <strong>only</strong> <strong>one</strong> stone is left in the row.</p>

<p>The <strong>score difference</strong> between Alice and Bob is <code>(Alice&#39;s score - Bob&#39;s score)</code>. Alice&#39;s goal is to <strong>maximize</strong> the score difference, and Bob&#39;s goal is the <strong>minimize</strong> the score difference.</p>

<p>Given an integer array <code>stones</code> of length <code>n</code> where <code>stones[i]</code> represents the value of the <code>i<sup>th</sup></code> stone <strong>from the left</strong>, return <em>the <strong>score difference</strong> between Alice and Bob if they both play <strong>optimally</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stones = [-1,2,-3,4,-5]
<strong>Output:</strong> 5
<strong>Explanation:</strong>
- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
  value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
  the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stones = [7,-6,5,10,5,-2,-6]
<strong>Output:</strong> 13
<strong>Explanation:</strong>
- Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
  stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> stones = [-10,-12]
<strong>Output:</strong> -22
<strong>Explanation:</strong>
- Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
  score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == stones.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= stones[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. Let's note that the only thing that matters is how many stones were removed so we can maintain dp[numberOfRemovedStones]

2. dp[x] = max(sum of all elements up to y - dp[y]) for all y > x

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as a game theory problem solvable with dynamic programming. The core observation is that removing the leftmost $x$ stones and replacing them with a single stone of value $S$ (the sum of the $x$ removed stones) is equivalent to choosing an index $i = x - 1$ in the prefix sum array $P$ of the original stones. Because every subsequent removal adds its sum to a single leftmost stone, any future move that removes $y$ stones from the current row corresponds to choosing a prefix sum $P[j]$ from the original array such that $j > i$. Alice aims to maximize the difference between her score and Bob's, while Bob aims to minimize it (which is equivalent to Bob maximizing his own score relative to Alice's).

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
    int stoneGameVIII(vector<int>& stones) {
        int n = stones.size();
        long long currentSum = 0;
        for (int s : stones) {
            currentSum += s;
        }

        long long res = currentSum;
        for (int i = n - 1; i > 1; --i) {
            currentSum -= stones[i];
            long long diff = currentSum - res;
            if (diff > res) {
                res = diff;
            }
        }

        return (int)res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int stoneGameVIII(int[] stones) {
        int n = stones.length;
        long currentSum = 0;
        for (int s : stones) {
            currentSum += s;
        }

        long res = currentSum;
        for (int i = n - 1; i > 1; i--) {
            currentSum -= stones[i];
            long diff = currentSum - res;
            if (diff > res) {
                res = diff;
            }
        }

        return (int) res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        current_sum = sum(stones)
        # Base case: Alice picks all stones (index n-1 in prefix sum array)
        res = current_sum
        # Iterate backwards from index n-2 down to index 1
        for i in range(n - 1, 1, -1):
            current_sum -= stones[i]
            # dp[i] = max(dp[i+1], prefixSum[i] - dp[i+1])
            # We update 'res' in place to represent dp[i]
            diff = current_sum - res
            if diff > res:
                res = diff
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        curr_p = sum(stones)
        dp = curr_p
        for i in range(n - 2, 0, -1):
            curr_p -= stones[i + 1]
            diff = curr_p - dp
            if diff > dp:
                dp = diff
        return dp
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int stoneGameVIII(int* stones, int stonesSize) {
    long long currentP = 0;
    for (int i = 0; i < stonesSize; i++) {
        currentP += stones[i];
    }
    long long dp = currentP;
    for (int i = stonesSize - 2; i >= 1; i--) {
        currentP -= (long long)stones[i + 1];
        long long diff = currentP - dp;
        if (diff > dp) {
            dp = diff;
        }
    }
    return (int)dp;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int StoneGameVIII(int[] stones) {
        int n = stones.Length;
        long currentP = 0;
        for (int i = 0; i < n; i++) {
            currentP += (long)stones[i];
        }
        long dp = currentP;
        for (int i = n - 2; i >= 1; i--) {
            currentP -= (long)stones[i + 1];
            long diff = currentP - dp;
            if (diff > dp) {
                dp = diff;
            }
        }
        return (int)dp;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} stones
 * @return {number}
 */
var stoneGameVIII = function(stones) {
    let n = stones.length;
    let currentP = 0;
    for (let i = 0; i < n; i++) {
        currentP += stones[i];
    }
    let dp = currentP;
    for (let i = n - 2; i >= 1; i--) {
        currentP -= stones[i + 1];
        let diff = currentP - dp;
        if (diff > dp) {
            dp = diff;
        }
    }
    return dp;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function stoneGameVIII(stones: number[]): number {
    const n = stones.length;
    let totalSum = stones.reduce((acc, val) => acc + val, 0);
    let res = totalSum;
    let currentP = totalSum;
    for (let i = n - 2; i >= 1; i--) {
        currentP -= stones[i + 1];
        res = Math.max(res, currentP - res);
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function stoneGameVIII($stones) {
        $n = count($stones);
        $totalSum = array_sum($stones);
        $res = $totalSum;
        $currentP = $totalSum;
        for ($i = $n - 2; $i >= 1; $i--) {
            $currentP -= $stones[$i + 1];
            $res = max($res, $currentP - $res);
        }
        return (int)$res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func stoneGameVIII(_ stones: [Int]) -> Int {
        let n = stones.count
        let totalSum = stones.reduce(0, +)
        var res = totalSum
        var currentP = totalSum
        if n > 2 {
            for i in stride(from: n - 2, through: 1, by: -1) {
                currentP -= stones[i + 1]
                res = max(res, currentP - res)
            }
        } else if n == 2 {
            return totalSum
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun stoneGameVIII(stones: IntArray): Int {
        val n = stones.size
        var totalSum: Long = 0
        for (s in stones) {
            totalSum += s
        }
        var res: Long = totalSum
        var currentP: Long = totalSum
        for (i in n - 2 downTo 1) {
            currentP -= stones[i + 1]
            res = Math.max(res, currentP - res)
        }
        return res.toInt()
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
  int stoneGameVIII(List<int> stones) {
    int n = stones.length;
    int totalSum = 0;
    for (int i = 0; i < n; i++) {
      totalSum += stones[i];
    }

    int dp = totalSum;
    int currSum = totalSum;

    for (int i = n - 1; i >= 2; i--) {
      currSum -= stones[i];
      int diff = currSum - dp;
      if (diff > dp) {
        dp = diff;
      }
    }

    return dp;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func stoneGameVIII(stones []int) int {
    n := len(stones)
    totalSum := 0
    for _, s := range stones {
        totalSum += s
    }

    dp := totalSum
    currentPrefixSum := totalSum

    for i := n - 1; i >= 2; i-- {
        currentPrefixSum -= stones[i]
        diff := currentPrefixSum - dp
        if diff > dp {
            dp = diff
        }
    }

    return dp
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} stones
# @return {Integer}
def stone_game_viii(stones)
  n = stones.length
  total_sum = stones.sum
  dp = total_sum
  curr_sum = total_sum

  (n - 1).downto(2) do |i|
    curr_sum -= stones[i]
    diff = curr_sum - dp
    dp = diff if diff > dp
  end

  dp
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def stoneGameVIII(stones: Array[Int]): Int = {
        val n = stones.length
        var totalSum: Long = 0L
        var i = 0
        while (i < n) {
            totalSum += stones(i).toLong
            i += 1
        }

        var dp: Long = totalSum
        var currSum: Long = totalSum
        var j = n - 1

        while (j >= 2) {
            currSum -= stones(j).toLong
            val diff = currSum - dp
            if (diff > dp) {
                dp = diff
            }
            j -= 1
        }

        dp.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn stone_game_viii(stones: Vec<i32>) -> i32 {
        let n = stones.len();
        let mut p: Vec<i64> = vec![0; n + 1];
        for i in 0..n {
            p[i + 1] = p[i] + stones[i] as i64;
        }

        let mut current_f = p[n];
        for i in (2..n).rev() {
            current_f = std::cmp::max(p[i] - current_f, current_f);
        }

        current_f as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (stone-game-viii stones)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length stones)]
         [p (make-vector (+ n 1) 0)])
    (for ([i (in-range n)]
          [s stones])
      (vector-set! p (+ i 1) (+ (vector-ref p i) s)))
    (let loop ([i (- n 1)]
               [current-f (vector-ref p n)])
      (if (< i 2)
          current-f
          (loop (- i 1) (max (- (vector-ref p i) current-f) current-f))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec stone_game_viii(Stones :: [integer()]) -> integer().
stone_game_viii(Stones) ->
    [Pn | Rest] = lists:foldl(fun(X, [H | T]) -> [X + H, H | T] end, [0], Stones),
    process(Rest, Pn, length(Stones) - 2).

process([Pi | Rest], CurrentF, Count) when Count > 0 ->
    process(Rest, erlang:max(Pi - CurrentF, CurrentF), Count - 1);
process(_, CurrentF, _) ->
    CurrentF.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec stone_game_viii(stones :: [integer]) :: integer
  def stone_game_viii(stones) do
    [pn | rest] = Enum.reduce(stones, [0], fn x, [h | t] -> [x + h, h | t] end)
    process(rest, pn, length(stones) - 2)
  end

  defp process([pi | rest], current_f, count) when count > 0 do
    process(rest, max(pi - current_f, current_f), count - 1)
  end

  defp process(_, current_f, _count) do
    current_f
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of stones. The algorithm involves a single pass to calculate the total sum of the stones and a second pass from the end of the prefix sum array to the second element ($P[1]$) to compute the optimal score difference using dynamic programming.
- **Space Complexity:** O(1) extra space. While the input array takes O(n) space, the algorithm only requires a few auxiliary variables to keep track of the current prefix sum and the maximum score difference found so far, as prefix sums are computed on the fly by subtracting elements from the total sum.
