---
layout: post
title: "Predict the Winner"
date: 2026-08-01 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Dynamic Programming", "Recursion", "Game Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/predict-the-winner/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool predictTheWinner(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        vector<vector<int>> dp(n, vector<int>(n));\n\
        \        for (int i = 0; i < n; ++i) {\n            dp[i][i] = nums[i];\n  \
        \      }\n        for (int len = 2; len <= n; ++len) {\n            for (int\
        \ i = 0; i <= n - len; ++i) {\n                int j = i + len - 1;\n      \
        \          dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);\n\
        \            }\n        }\n        return dp[0][n - 1] >= 0;\n    }\n};"
      java: "class Solution {\n    public boolean predictTheWinner(int[] nums) {\n \
        \       int n = nums.length;\n        int[][] dp = new int[n][n];\n        for\
        \ (int i = 0; i < n; i++) {\n            dp[i][i] = nums[i];\n        }\n  \
        \      for (int len = 2; len <= n; len++) {\n            for (int i = 0; i <=\
        \ n - len; i++) {\n                int j = i + len - 1;\n                dp[i][j]\
        \ = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);\n            }\n\
        \        }\n        return dp[0][n - 1] >= 0;\n    }\n}"
      python: "class Solution(object):\n    def predictTheWinner(self, nums):\n    \
        \    \"\"\"\n        :type nums: List[int]\n        :rtype: bool\n        \"\
        \"\"\n        n = len(nums)\n        dp = [[0] * n for _ in range(n)]\n    \
        \    for i in range(n):\n            dp[i][i] = nums[i]\n        for length\
        \ in range(2, n + 1):\n            for i in range(n - length + 1):\n       \
        \         j = i + length - 1\n                dp[i][j] = max(nums[i] - dp[i\
        \ + 1][j], nums[j] - dp[i][j - 1])\n        return dp[0][n - 1] >= 0"
      python3: "class Solution:\n    def predictTheWinner(self, nums: List[int]) ->\
        \ bool:\n        n = len(nums)\n        dp = [[0] * n for _ in range(n)]\n \
        \       for i in range(n):\n            dp[i][i] = nums[i]\n        for length\
        \ in range(2, n + 1):\n            for i in range(n - length + 1):\n       \
        \         j = i + length - 1\n                dp[i][j] = max(nums[i] - dp[i\
        \ + 1][j], nums[j] - dp[i][j - 1])\n        return dp[0][n - 1] >= 0"
      c: "#include <stdbool.h>\n#include <math.h>\n\nbool predictTheWinner(int* nums,\
        \ int numsSize) {\n    int dp[20][20];\n    for (int i = 0; i < numsSize; i++)\
        \ {\n        dp[i][i] = nums[i];\n    }\n    for (int len = 2; len <= numsSize;\
        \ len++) {\n        for (int i = 0; i <= numsSize - len; i++) {\n          \
        \  int j = i + len - 1;\n            int pickLeft = nums[i] - dp[i + 1][j];\n\
        \            int pickRight = nums[j] - dp[i][j - 1];\n            dp[i][j] =\
        \ (pickLeft > pickRight) ? pickLeft : pickRight;\n        }\n    }\n    return\
        \ dp[0][numsSize - 1] >= 0;\n}"
      csharp: "public class Solution {\n    public bool PredictTheWinner(int[] nums)\
        \ {\n        int n = nums.Length;\n        int[,] dp = new int[n, n];\n    \
        \    for (int i = 0; i < n; i++) {\n            dp[i, i] = nums[i];\n      \
        \  }\n        for (int len = 2; len <= n; len++) {\n            for (int i =\
        \ 0; i <= n - len; i++) {\n                int j = i + len - 1;\n          \
        \      dp[i, j] = Math.Max(nums[i] - dp[i + 1, j], nums[j] - dp[i, j - 1]);\n\
        \            }\n        }\n        return dp[0, n - 1] >= 0;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {boolean}\n */\nvar predictTheWinner\
        \ = function(nums) {\n    const n = nums.length;\n    const dp = Array.from({\
        \ length: n }, () => new Array(n).fill(0));\n    for (let i = 0; i < n; i++)\
        \ {\n        dp[i][i] = nums[i];\n    }\n    for (let len = 2; len <= n; len++)\
        \ {\n        for (let i = 0; i <= n - len; i++) {\n            const j = i +\
        \ len - 1;\n            dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j]\
        \ - dp[i][j - 1]);\n        }\n    }\n    return dp[0][n - 1] >= 0;\n};"
      typescript: "function predictTheWinner(nums: number[]): boolean {\n    const n\
        \ = nums.length;\n    const dp: number[][] = Array.from({ length: n }, () =>\
        \ new Array(n).fill(0));\n    for (let i = 0; i < n; i++) {\n        dp[i][i]\
        \ = nums[i];\n    }\n    for (let len = 2; len <= n; len++) {\n        for (let\
        \ i = 0; i <= n - len; i++) {\n            const j = i + len - 1;\n        \
        \    dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);\n\
        \        }\n    }\n    return dp[0][n - 1] >= 0;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Boolean\n     */\n    function predictTheWinner($nums) {\n        $n = count($nums);\n\
        \        $dp = array_fill(0, $n, array_fill(0, $n, 0));\n        for ($i = 0;\
        \ $i < $n; $i++) {\n            $dp[$i][$i] = $nums[$i];\n        }\n      \
        \  for ($len = 2; $len <= $n; $len++) {\n            for ($i = 0; $i <= $n -\
        \ $len; $i++) {\n                $j = $i + $len - 1;\n                $dp[$i][$j]\
        \ = max($nums[$i] - $dp[$i + 1][$j], $nums[$j] - $dp[$i][$j - 1]);\n       \
        \     }\n        }\n        return $dp[0][$n - 1] >= 0;\n    }\n}"
      swift: "class Solution {\n    func predictTheWinner(_ nums: [Int]) -> Bool {\n\
        \        let n = nums.count\n        var dp = Array(repeating: Array(repeating:\
        \ 0, count: n), count: n)\n        for i in 0..<n {\n            dp[i][i] =\
        \ nums[i]\n        }\n        if n >= 2 {\n            for len in 2...n {\n\
        \                for i in 0...(n - len) {\n                    let j = i + len\
        \ - 1\n                    dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] -\
        \ dp[i][j - 1])\n                }\n            }\n        }\n        return\
        \ dp[0][n - 1] >= 0\n    }\n}"
      kotlin: "class Solution {\n    fun predictTheWinner(nums: IntArray): Boolean {\n\
        \        val n = nums.size\n        val dp = IntArray(n) { nums[it] }\n    \
        \    for (len in 1 until n) {\n            for (i in 0 until n - len) {\n  \
        \              val j = i + len\n                val a = nums[i] - dp[i + 1]\n\
        \                val b = nums[j] - dp[i]\n                dp[i] = if (a > b)\
        \ a else b\n            }\n        }\n        return dp[0] >= 0\n    }\n}"
      dart: "class Solution {\n  bool predictTheWinner(List<int> nums) {\n    int n\
        \ = nums.length;\n    List<int> dp = List<int>.from(nums);\n    for (int len\
        \ = 1; len < n; len++) {\n      for (int i = 0; i < n - len; i++) {\n      \
        \  int j = i + len;\n        int a = nums[i] - dp[i + 1];\n        int b = nums[j]\
        \ - dp[i];\n        dp[i] = a > b ? a : b;\n      }\n    }\n    return dp[0]\
        \ >= 0;\n  }\n}"
      go: "func predictTheWinner(nums []int) bool {\n    n := len(nums)\n    dp := make([]int,\
        \ n)\n    for i, v := range nums {\n        dp[i] = v\n    }\n    for length\
        \ := 1; length < n; length++ {\n        for i := 0; i < n-length; i++ {\n  \
        \          j := i + length\n            a := nums[i] - dp[i+1]\n           \
        \ b := nums[j] - dp[i]\n            if a > b {\n                dp[i] = a\n\
        \            } else {\n                dp[i] = b\n            }\n        }\n\
        \    }\n    return dp[0] >= 0\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Boolean}\ndef predict_the_winner(nums)\n\
        \  n = nums.length\n  dp = Array.new(n) { |i| nums[i] }\n  (1...n).each do |len|\n\
        \    (0...(n - len)).each do |i|\n      j = i + len\n      a = nums[i] - dp[i\
        \ + 1]\n      b = nums[j] - dp[i]\n      dp[i] = a > b ? a : b\n    end\n  end\n\
        \  dp[0] >= 0\nend"
      scala: "object Solution {\n    def predictTheWinner(nums: Array[Int]): Boolean\
        \ = {\n        val n = nums.length\n        val dp = nums.clone()\n        for\
        \ (len <- 1 until n) {\n            for (i <- 0 until (n - len)) {\n       \
        \         val j = i + len\n                val a = nums(i) - dp(i + 1)\n   \
        \             val b = nums(j) - dp(i)\n                dp(i) = if (a > b) a\
        \ else b\n            }\n        }\n        dp(0) >= 0\n    }\n}"
      rust: "impl Solution {\n    pub fn predict_the_winner(nums: Vec<i32>) -> bool\
        \ {\n        let n = nums.len();\n        if n == 0 {\n            return true;\n\
        \        }\n        let mut dp = vec![vec![0; n]; n];\n        for i in 0..n\
        \ {\n            dp[i][i] = nums[i];\n        }\n        for length in 2..=n\
        \ {\n            for i in 0..=n - length {\n                let j = i + length\
        \ - 1;\n                dp[i][j] = std::cmp::max(nums[i] - dp[i + 1][j], nums[j]\
        \ - dp[i][j - 1]);\n            }\n        }\n        dp[0][n - 1] >= 0\n  \
        \  }\n}"
      racket: "(define/contract (predict-the-winner nums)\n  (-> (listof exact-integer?)\
        \ boolean?)\n  (let* ([n (length nums)]\n         [arr (list->vector nums)]\n\
        \         [memo (make-hash)])\n    (define (solve i j)\n      (cond\n      \
        \  [(= i j) (vector-ref arr i)]\n        [(hash-has-key? memo (cons i j)) (hash-ref\
        \ memo (cons i j))]\n        [else\n         (let ([res (max (- (vector-ref\
        \ arr i) (solve (+ i 1) j))\n                         (- (vector-ref arr j)\
        \ (solve i (- j 1))))])\n           (hash-set! memo (cons i j) res)\n      \
        \     res)]))\n    (>= (solve 0 (- n 1)) 0)))"
      erlang: "-spec predict_the_winner(Nums :: [integer()]) -> boolean().\npredict_the_winner(Nums)\
        \ ->\n    N = length(Nums),\n    Arr = list_to_tuple(Nums),\n    {Res, _} =\
        \ solve(1, N, Arr, #{}),\n    Res >= 0.\n\nsolve(I, J, Arr, Memo) ->\n    case\
        \ maps:get({I, J}, Memo, undefined) of\n        undefined ->\n            if\n\
        \                I == J ->\n                    Val = element(I, Arr),\n   \
        \                 {Val, maps:put({I, J}, Val, Memo)};\n                true\
        \ ->\n                    {Val1, Memo1} = solve(I + 1, J, Arr, Memo),\n    \
        \                {Val2, Memo2} = solve(I, J - 1, Arr, Memo1),\n            \
        \        Res = erlang:max(element(I, Arr) - Val1, element(J, Arr) - Val2),\n\
        \                    {Res, maps:put({I, J}, Res, Memo2)}\n            end;\n\
        \        CachedValue ->\n            {CachedValue, Memo}\n    end."
      elixir: "defmodule Solution do\n  @spec predict_the_winner(nums :: [integer])\
        \ :: boolean\n  def predict_the_winner(nums) do\n    n = length(nums)\n    arr\
        \ = List.to_tuple(nums)\n    {res, _} = solve(0, n - 1, arr, %{})\n    res >=\
        \ 0\n  end\n\n  defp solve(i, j, arr, memo) do\n    cond do\n      i == j ->\n\
        \        val = elem(arr, i)\n        {val, Map.put(memo, {i, j}, val)}\n   \
        \   Map.has_key?(memo, {i, j}) ->\n        {Map.get(memo, {i, j}), memo}\n \
        \     true ->\n        {val1, memo1} = solve(i + 1, j, arr, memo)\n        {val2,\
        \ memo2} = solve(i, j - 1, arr, memo1)\n        res = max(elem(arr, i) - val1,\
        \ elem(arr, j) - val2)\n        {res, Map.put(memo2, {i, j}, res)}\n    end\n\
        \  end\nend"
    approach: 'The problem can be solved using dynamic programming by defining $dp[i][j]$
      as the maximum relative score difference a player can achieve when considering
      the subarray $nums[i..j]$. In this zero-sum context, if the current player chooses
      $nums[i]$, their relative lead increases by $nums[i]$ minus whatever the opponent
      can optimally achieve from the remaining subarray $nums[i+1..j]$. Thus, the recurrence
      relation is $dp[i][j] = \max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])$.


      We initialize the base cases where the subarray has only one element ($i=j$),
      meaning $dp[i][i] = nums[i]$. We then iterate through all possible subarray lengths
      from 2 up to $n$. After filling the table, the value $dp[0][n-1]$ represents the
      maximum score difference Player 1 can maintain over Player 2 starting from the
      full array. If this value is greater than or equal to zero, Player 1 wins.'
    time_complexity: O(n^2) where n is the number of elements in the array. This is
      because we compute the values for a 2D DP table of size $n \times n$, and each
      state calculation takes $O(1)$ time.
    space_complexity: O(n^2) for the 2D array used to store the results of the subproblems.
      This can be further optimized to $O(n)$ because each length calculation only requires
      information from the previous length's results, but $O(n^2)$ is well within limits
      for $n=20$.
    elapsed_time: 150.95982766151428
    model: gemini-3-flash-preview
    generated_at: '2026-08-01 02:07:35 '
---

## Problem #486: Predict the Winner

**Difficulty:** Medium

**Topics:** Array, Math, Dynamic Programming, Recursion, Game Theory

## Problem Description

<p>You are given an integer array <code>nums</code>. Two players are playing a game with this array: player 1 and player 2.</p>

<p>Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of <code>0</code>. At each turn, the player takes one of the numbers from either end of the array (i.e., <code>nums[0]</code> or <code>nums[nums.length - 1]</code>) which reduces the size of the array by <code>1</code>. The player adds the chosen number to their score. The game ends when there are no more elements in the array.</p>

<p>Return <code>true</code> if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return <code>true</code>. You may assume that both players are playing optimally.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,233,7]
<strong>Output:</strong> true
<strong>Explanation:</strong> Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 20</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved using dynamic programming by defining $dp[i][j]$ as the maximum relative score difference a player can achieve when considering the subarray $nums[i..j]$. In this zero-sum context, if the current player chooses $nums[i]$, their relative lead increases by $nums[i]$ minus whatever the opponent can optimally achieve from the remaining subarray $nums[i+1..j]$. Thus, the recurrence relation is $dp[i][j] = \max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])$.

We initialize the base cases where the subarray has only one element ($i=j$), meaning $dp[i][i] = nums[i]$. We then iterate through all possible subarray lengths from 2 up to $n$. After filling the table, the value $dp[0][n-1]$ represents the maximum score difference Player 1 can maintain over Player 2 starting from the full array. If this value is greater than or equal to zero, Player 1 wins.

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
    bool predictTheWinner(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            dp[i][i] = nums[i];
        }
        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i <= n - len; ++i) {
                int j = i + len - 1;
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
            }
        }
        return dp[0][n - 1] >= 0;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean predictTheWinner(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = nums[i];
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
            }
        }
        return dp[0][n - 1] >= 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <math.h>

bool predictTheWinner(int* nums, int numsSize) {
    int dp[20][20];
    for (int i = 0; i < numsSize; i++) {
        dp[i][i] = nums[i];
    }
    for (int len = 2; len <= numsSize; len++) {
        for (int i = 0; i <= numsSize - len; i++) {
            int j = i + len - 1;
            int pickLeft = nums[i] - dp[i + 1][j];
            int pickRight = nums[j] - dp[i][j - 1];
            dp[i][j] = (pickLeft > pickRight) ? pickLeft : pickRight;
        }
    }
    return dp[0][numsSize - 1] >= 0;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool PredictTheWinner(int[] nums) {
        int n = nums.Length;
        int[,] dp = new int[n, n];
        for (int i = 0; i < n; i++) {
            dp[i, i] = nums[i];
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                dp[i, j] = Math.Max(nums[i] - dp[i + 1, j], nums[j] - dp[i, j - 1]);
            }
        }
        return dp[0, n - 1] >= 0;
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
 * @return {boolean}
 */
var predictTheWinner = function(nums) {
    const n = nums.length;
    const dp = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        dp[i][i] = nums[i];
    }
    for (let len = 2; len <= n; len++) {
        for (let i = 0; i <= n - len; i++) {
            const j = i + len - 1;
            dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
        }
    }
    return dp[0][n - 1] >= 0;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function predictTheWinner(nums: number[]): boolean {
    const n = nums.length;
    const dp: number[][] = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) {
        dp[i][i] = nums[i];
    }
    for (let len = 2; len <= n; len++) {
        for (let i = 0; i <= n - len; i++) {
            const j = i + len - 1;
            dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
        }
    }
    return dp[0][n - 1] >= 0;
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
     * @return Boolean
     */
    function predictTheWinner($nums) {
        $n = count($nums);
        $dp = array_fill(0, $n, array_fill(0, $n, 0));
        for ($i = 0; $i < $n; $i++) {
            $dp[$i][$i] = $nums[$i];
        }
        for ($len = 2; $len <= $n; $len++) {
            for ($i = 0; $i <= $n - $len; $i++) {
                $j = $i + $len - 1;
                $dp[$i][$j] = max($nums[$i] - $dp[$i + 1][$j], $nums[$j] - $dp[$i][$j - 1]);
            }
        }
        return $dp[0][$n - 1] >= 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func predictTheWinner(_ nums: [Int]) -> Bool {
        let n = nums.count
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            dp[i][i] = nums[i]
        }
        if n >= 2 {
            for len in 2...n {
                for i in 0...(n - len) {
                    let j = i + len - 1
                    dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
                }
            }
        }
        return dp[0][n - 1] >= 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun predictTheWinner(nums: IntArray): Boolean {
        val n = nums.size
        val dp = IntArray(n) { nums[it] }
        for (len in 1 until n) {
            for (i in 0 until n - len) {
                val j = i + len
                val a = nums[i] - dp[i + 1]
                val b = nums[j] - dp[i]
                dp[i] = if (a > b) a else b
            }
        }
        return dp[0] >= 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool predictTheWinner(List<int> nums) {
    int n = nums.length;
    List<int> dp = List<int>.from(nums);
    for (int len = 1; len < n; len++) {
      for (int i = 0; i < n - len; i++) {
        int j = i + len;
        int a = nums[i] - dp[i + 1];
        int b = nums[j] - dp[i];
        dp[i] = a > b ? a : b;
      }
    }
    return dp[0] >= 0;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func predictTheWinner(nums []int) bool {
    n := len(nums)
    dp := make([]int, n)
    for i, v := range nums {
        dp[i] = v
    }
    for length := 1; length < n; length++ {
        for i := 0; i < n-length; i++ {
            j := i + length
            a := nums[i] - dp[i+1]
            b := nums[j] - dp[i]
            if a > b {
                dp[i] = a
            } else {
                dp[i] = b
            }
        }
    }
    return dp[0] >= 0
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Boolean}
def predict_the_winner(nums)
  n = nums.length
  dp = Array.new(n) { |i| nums[i] }
  (1...n).each do |len|
    (0...(n - len)).each do |i|
      j = i + len
      a = nums[i] - dp[i + 1]
      b = nums[j] - dp[i]
      dp[i] = a > b ? a : b
    end
  end
  dp[0] >= 0
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def predictTheWinner(nums: Array[Int]): Boolean = {
        val n = nums.length
        val dp = nums.clone()
        for (len <- 1 until n) {
            for (i <- 0 until (n - len)) {
                val j = i + len
                val a = nums(i) - dp(i + 1)
                val b = nums(j) - dp(i)
                dp(i) = if (a > b) a else b
            }
        }
        dp(0) >= 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n == 0 {
            return true;
        }
        let mut dp = vec![vec![0; n]; n];
        for i in 0..n {
            dp[i][i] = nums[i];
        }
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                dp[i][j] = std::cmp::max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
            }
        }
        dp[0][n - 1] >= 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (predict-the-winner nums)
  (-> (listof exact-integer?) boolean?)
  (let* ([n (length nums)]
         [arr (list->vector nums)]
         [memo (make-hash)])
    (define (solve i j)
      (cond
        [(= i j) (vector-ref arr i)]
        [(hash-has-key? memo (cons i j)) (hash-ref memo (cons i j))]
        [else
         (let ([res (max (- (vector-ref arr i) (solve (+ i 1) j))
                         (- (vector-ref arr j) (solve i (- j 1))))])
           (hash-set! memo (cons i j) res)
           res)]))
    (>= (solve 0 (- n 1)) 0)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec predict_the_winner(Nums :: [integer()]) -> boolean().
predict_the_winner(Nums) ->
    N = length(Nums),
    Arr = list_to_tuple(Nums),
    {Res, _} = solve(1, N, Arr, #{}),
    Res >= 0.

solve(I, J, Arr, Memo) ->
    case maps:get({I, J}, Memo, undefined) of
        undefined ->
            if
                I == J ->
                    Val = element(I, Arr),
                    {Val, maps:put({I, J}, Val, Memo)};
                true ->
                    {Val1, Memo1} = solve(I + 1, J, Arr, Memo),
                    {Val2, Memo2} = solve(I, J - 1, Arr, Memo1),
                    Res = erlang:max(element(I, Arr) - Val1, element(J, Arr) - Val2),
                    {Res, maps:put({I, J}, Res, Memo2)}
            end;
        CachedValue ->
            {CachedValue, Memo}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec predict_the_winner(nums :: [integer]) :: boolean
  def predict_the_winner(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)
    {res, _} = solve(0, n - 1, arr, %{})
    res >= 0
  end

  defp solve(i, j, arr, memo) do
    cond do
      i == j ->
        val = elem(arr, i)
        {val, Map.put(memo, {i, j}, val)}
      Map.has_key?(memo, {i, j}) ->
        {Map.get(memo, {i, j}), memo}
      true ->
        {val1, memo1} = solve(i + 1, j, arr, memo)
        {val2, memo2} = solve(i, j - 1, arr, memo1)
        res = max(elem(arr, i) - val1, elem(arr, j) - val2)
        {res, Map.put(memo2, {i, j}, res)}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2) where n is the number of elements in the array. This is because we compute the values for a 2D DP table of size $n \times n$, and each state calculation takes $O(1)$ time.
- **Space Complexity:** O(n^2) for the 2D array used to store the results of the subproblems. This can be further optimized to $O(n)$ because each length calculation only requires information from the previous length's results, but $O(n^2)$ is well within limits for $n=20$.
