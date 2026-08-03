---
layout: post
title: "Stone Game III"
date: 2026-08-03 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Dynamic Programming", "Game Theory"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/stone-game-iii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string stoneGameIII(vector<int>& stoneValue)\
        \ {\n        int n = stoneValue.size();\n        vector<int> dp(n + 1, -1e9);\n\
        \        dp[n] = 0;\n\n        for (int i = n - 1; i >= 0; --i) {\n        \
        \    int take = 0;\n            for (int k = 0; k < 3 && i + k < n; ++k) {\n\
        \                take += stoneValue[i + k];\n                dp[i] = max(dp[i],\
        \ take - dp[i + k + 1]);\n            }\n        }\n\n        if (dp[0] > 0)\
        \ return \"Alice\";\n        if (dp[0] < 0) return \"Bob\";\n        return\
        \ \"Tie\";\n    }\n};"
      java: "class Solution {\n    public String stoneGameIII(int[] stoneValue) {\n\
        \        int n = stoneValue.length;\n        int[] dp = new int[n + 1];\n  \
        \      for (int i = 0; i < n; i++) dp[i] = Integer.MIN_VALUE;\n        dp[n]\
        \ = 0;\n\n        for (int i = n - 1; i >= 0; i--) {\n            int take =\
        \ 0;\n            for (int k = 0; k < 3 && i + k < n; k++) {\n             \
        \   take += stoneValue[i + k];\n                dp[i] = Math.max(dp[i], take\
        \ - dp[i + k + 1]);\n            }\n        }\n\n        if (dp[0] > 0) return\
        \ \"Alice\";\n        if (dp[0] < 0) return \"Bob\";\n        return \"Tie\"\
        ;\n    }\n}"
      python: "class Solution(object):\n    def stoneGameIII(self, stoneValue):\n  \
        \      \"\"\"\n        :type stoneValue: List[int]\n        :rtype: str\n  \
        \      \"\"\"\n        n = len(stoneValue)\n        dp = [-float('inf')] * (n\
        \ + 1)\n        dp[n] = 0\n\n        for i in range(n - 1, -1, -1):\n      \
        \      take = 0\n            for k in range(3):\n                if i + k <\
        \ n:\n                    take += stoneValue[i + k]\n                    val\
        \ = take - dp[i + k + 1]\n                    if val > dp[i]:\n            \
        \            dp[i] = val\n\n        if dp[0] > 0:\n            return \"Alice\"\
        \n        elif dp[0] < 0:\n            return \"Bob\"\n        else:\n     \
        \       return \"Tie\""
      python3: "class Solution:\n    def stoneGameIII(self, stoneValue: list[int]) ->\
        \ str:\n        n = len(stoneValue)\n        v1 = v2 = v3 = 0\n        for i\
        \ in range(n - 1, -1, -1):\n            current_sum = stoneValue[i]\n      \
        \      res = current_sum - v1\n            if i + 1 < n:\n                current_sum\
        \ += stoneValue[i + 1]\n                res = max(res, current_sum - v2)\n \
        \           if i + 2 < n:\n                current_sum += stoneValue[i + 2]\n\
        \                res = max(res, current_sum - v3)\n            v3, v2, v1 =\
        \ v2, v1, res\n\n        if v1 > 0:\n            return \"Alice\"\n        elif\
        \ v1 < 0:\n            return \"Bob\"\n        else:\n            return \"\
        Tie\""
      c: "char* stoneGameIII(int* stoneValue, int stoneValueSize) {\n    int v1 = 0,\
        \ v2 = 0, v3 = 0;\n    for (int i = stoneValueSize - 1; i >= 0; i--) {\n   \
        \     int currentSum = stoneValue[i];\n        int res = currentSum - v1;\n\
        \        if (i + 1 < stoneValueSize) {\n            currentSum += stoneValue[i\
        \ + 1];\n            int take2 = currentSum - v2;\n            if (take2 > res)\
        \ res = take2;\n        }\n        if (i + 2 < stoneValueSize) {\n         \
        \   currentSum += stoneValue[i + 2];\n            int take3 = currentSum - v3;\n\
        \            if (take3 > res) res = take3;\n        }\n        v3 = v2;\n  \
        \      v2 = v1;\n        v1 = res;\n    }\n    if (v1 > 0) return \"Alice\"\
        ;\n    if (v1 < 0) return \"Bob\";\n    return \"Tie\";\n}"
      csharp: "using System;\n\npublic class Solution {\n    public string StoneGameIII(int[]\
        \ stoneValue) {\n        int n = stoneValue.Length;\n        int v1 = 0, v2\
        \ = 0, v3 = 0;\n        for (int i = n - 1; i >= 0; i--) {\n            int\
        \ currentSum = stoneValue[i];\n            int res = currentSum - v1;\n    \
        \        if (i + 1 < n) {\n                currentSum += stoneValue[i + 1];\n\
        \                res = Math.Max(res, currentSum - v2);\n            }\n    \
        \        if (i + 2 < n) {\n                currentSum += stoneValue[i + 2];\n\
        \                res = Math.Max(res, currentSum - v3);\n            }\n    \
        \        v3 = v2;\n            v2 = v1;\n            v1 = res;\n        }\n\
        \        if (v1 > 0) return \"Alice\";\n        if (v1 < 0) return \"Bob\";\n\
        \        return \"Tie\";\n    }\n}"
      javascript: "/**\n * @param {number[]} stoneValue\n * @return {string}\n */\n\
        var stoneGameIII = function(stoneValue) {\n    let n = stoneValue.length;\n\
        \    let v1 = 0, v2 = 0, v3 = 0;\n    for (let i = n - 1; i >= 0; i--) {\n \
        \       let currentSum = stoneValue[i];\n        let res = currentSum - v1;\n\
        \        if (i + 1 < n) {\n            currentSum += stoneValue[i + 1];\n  \
        \          res = Math.max(res, currentSum - v2);\n        }\n        if (i +\
        \ 2 < n) {\n            currentSum += stoneValue[i + 2];\n            res =\
        \ Math.max(res, currentSum - v3);\n        }\n        v3 = v2;\n        v2 =\
        \ v1;\n        v1 = res;\n    }\n    if (v1 > 0) return \"Alice\";\n    if (v1\
        \ < 0) return \"Bob\";\n    return \"Tie\";\n};"
      typescript: "function stoneGameIII(stoneValue: number[]): string {\n    const\
        \ n = stoneValue.length;\n    const dp = new Array(n + 1).fill(0);\n    for\
        \ (let i = n - 1; i >= 0; i--) {\n        let maxRelative = -Infinity;\n   \
        \     let currentTake = 0;\n        for (let k = 0; k < 3 && i + k < n; k++)\
        \ {\n            currentTake += stoneValue[i + k];\n            const currentRes\
        \ = currentTake - dp[i + k + 1];\n            if (currentRes > maxRelative)\
        \ {\n                maxRelative = currentRes;\n            }\n        }\n \
        \       dp[i] = maxRelative;\n    }\n    if (dp[0] > 0) return \"Alice\";\n\
        \    if (dp[0] < 0) return \"Bob\";\n    return \"Tie\";\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $stoneValue\n     *\
        \ @return String\n     */\n    function stoneGameIII($stoneValue) {\n      \
        \  $n = count($stoneValue);\n        $dp = array_fill(0, $n + 1, 0);\n     \
        \   for ($i = $n - 1; $i >= 0; $i--) {\n            $maxRelative = -PHP_INT_MAX;\n\
        \            $currentTake = 0;\n            for ($k = 0; $k < 3 && $i + $k <\
        \ $n; $k++) {\n                $currentTake += $stoneValue[$i + $k];\n     \
        \           $currentRes = $currentTake - $dp[$i + $k + 1];\n               \
        \ if ($currentRes > $maxRelative) {\n                    $maxRelative = $currentRes;\n\
        \                }\n            }\n            $dp[$i] = $maxRelative;\n   \
        \     }\n        if ($dp[0] > 0) return \"Alice\";\n        if ($dp[0] < 0)\
        \ return \"Bob\";\n        return \"Tie\";\n    }\n}"
      swift: "class Solution {\n    func stoneGameIII(_ stoneValue: [Int]) -> String\
        \ {\n        let n = stoneValue.count\n        var dp = [Int](repeating: 0,\
        \ count: n + 1)\n        for i in stride(from: n - 1, through: 0, by: -1) {\n\
        \            var maxRelative = Int.min\n            var currentTake = 0\n  \
        \          for k in 0..<3 {\n                if i + k < n {\n              \
        \      currentTake += stoneValue[i + k]\n                    let currentRes\
        \ = currentTake - dp[i + k + 1]\n                    if currentRes > maxRelative\
        \ {\n                        maxRelative = currentRes\n                    }\n\
        \                }\n            }\n            dp[i] = maxRelative\n       \
        \ }\n        if dp[0] > 0 { return \"Alice\" }\n        if dp[0] < 0 { return\
        \ \"Bob\" }\n        return \"Tie\"\n    }\n}"
      kotlin: "class Solution {\n    fun stoneGameIII(stoneValue: IntArray): String\
        \ {\n        val n = stoneValue.size\n        val dp = IntArray(n + 1)\n   \
        \     for (i in n - 1 downTo 0) {\n            var maxRelative = Int.MIN_VALUE\n\
        \            var currentTake = 0\n            for (k in 0..2) {\n          \
        \      if (i + k < n) {\n                    currentTake += stoneValue[i + k]\n\
        \                    val currentRes = currentTake - dp[i + k + 1]\n        \
        \            if (currentRes > maxRelative) {\n                        maxRelative\
        \ = currentRes\n                    }\n                }\n            }\n  \
        \          dp[i] = maxRelative\n        }\n        return when {\n         \
        \   dp[0] > 0 -> \"Alice\"\n            dp[0] < 0 -> \"Bob\"\n            else\
        \ -> \"Tie\"\n        }\n    }\n}"
      dart: "class Solution {\n  String stoneGameIII(List<int> stoneValue) {\n    int\
        \ n = stoneValue.length;\n    List<int> dp = List.filled(n + 1, 0);\n    for\
        \ (int i = n - 1; i >= 0; i--) {\n      int res = stoneValue[i] - dp[i + 1];\n\
        \      if (i + 1 < n) {\n        int take2 = stoneValue[i] + stoneValue[i +\
        \ 1] - dp[i + 2];\n        if (take2 > res) res = take2;\n      }\n      if\
        \ (i + 2 < n) {\n        int take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i\
        \ + 2] - dp[i + 3];\n        if (take3 > res) res = take3;\n      }\n      dp[i]\
        \ = res;\n    }\n    if (dp[0] > 0) return \"Alice\";\n    if (dp[0] < 0) return\
        \ \"Bob\";\n    return \"Tie\";\n  }\n}"
      go: "func stoneGameIII(stoneValue []int) string {\n    n := len(stoneValue)\n\
        \    dp := make([]int, n+1)\n    for i := n - 1; i >= 0; i-- {\n        res\
        \ := stoneValue[i] - dp[i+1]\n        if i+1 < n {\n            sum2 := stoneValue[i]\
        \ + stoneValue[i+1] - dp[i+2]\n            if sum2 > res {\n               \
        \ res = sum2\n            }\n        }\n        if i+2 < n {\n            sum3\
        \ := stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3]\n         \
        \   if sum3 > res {\n                res = sum3\n            }\n        }\n\
        \        dp[i] = res\n    }\n    if dp[0] > 0 {\n        return \"Alice\"\n\
        \    }\n    if dp[0] < 0 {\n        return \"Bob\"\n    }\n    return \"Tie\"\
        \n}"
      ruby: "# @param {Integer[]} stone_value\n# @return {String}\ndef stone_game_iii(stone_value)\n\
        \  n = stone_value.length\n  dp = Array.new(n + 1, 0)\n  (n - 1).downto(0) do\
        \ |i|\n    res = stone_value[i] - dp[i + 1]\n    if i + 1 < n\n      val2 =\
        \ stone_value[i] + stone_value[i + 1] - dp[i + 2]\n      res = val2 if val2\
        \ > res\n    end\n    if i + 2 < n\n      val3 = stone_value[i] + stone_value[i\
        \ + 1] + stone_value[i + 2] - dp[i + 3]\n      res = val3 if val3 > res\n  \
        \  end\n    dp[i] = res\n  end\n  if dp[0] > 0\n    return \"Alice\"\n  elsif\
        \ dp[0] < 0\n    return \"Bob\"\n  else\n    return \"Tie\"\n  end\nend"
      scala: "object Solution {\n    def stoneGameIII(stoneValue: Array[Int]): String\
        \ = {\n        val n = stoneValue.length\n        val dp = new Array[Int](n\
        \ + 1)\n        for (i <- n - 1 to 0 by -1) {\n            var res = stoneValue(i)\
        \ - dp(i + 1)\n            if (i + 1 < n) {\n                val val2 = stoneValue(i)\
        \ + stoneValue(i + 1) - dp(i + 2)\n                if (val2 > res) res = val2\n\
        \            }\n            if (i + 2 < n) {\n                val val3 = stoneValue(i)\
        \ + stoneValue(i + 1) + stoneValue(i + 2) - dp(i + 3)\n                if (val3\
        \ > res) res = val3\n            }\n            dp(i) = res\n        }\n   \
        \     if (dp(0) > 0) \"Alice\"\n        else if (dp(0) < 0) \"Bob\"\n      \
        \  else \"Tie\"\n    }\n}"
      rust: "impl Solution {\n    pub fn stone_game_iii(stone_value: Vec<i32>) -> String\
        \ {\n        let n = stone_value.len();\n        let mut dp = vec![0; n + 3];\n\
        \        for i in (0..n).rev() {\n            let s_i = stone_value[i];\n  \
        \          let res1 = s_i - dp[i + 1];\n            let mut res2 = -1_000_000_000;\n\
        \            if i + 1 < n {\n                res2 = s_i + stone_value[i + 1]\
        \ - dp[i + 2];\n            }\n            let mut res3 = -1_000_000_000;\n\
        \            if i + 2 < n {\n                res3 = s_i + stone_value[i + 1]\
        \ + stone_value[i + 2] - dp[i + 3];\n            }\n            dp[i] = res1.max(res2).max(res3);\n\
        \        }\n\n        if dp[0] > 0 {\n            \"Alice\".to_string()\n  \
        \      } else if dp[0] < 0 {\n            \"Bob\".to_string()\n        } else\
        \ {\n            \"Tie\".to_string()\n        }\n    }\n}"
      racket: "(define/contract (stone-game-iii stoneValue)\n  (-> (listof exact-integer?)\
        \ string?)\n  (let* ([n (length stoneValue)]\n         [arr (list->vector stoneValue)]\n\
        \         [dp (make-vector (+ n 3) 0)])\n    (for ([i (in-range (- n 1) -1 -1)])\n\
        \      (let* ([s-i (vector-ref arr i)]\n             [res1 (- s-i (vector-ref\
        \ dp (+ i 1)))]\n             [res2 (if (< (+ i 1) n)\n                    \
        \   (- (+ s-i (vector-ref arr (+ i 1))) (vector-ref dp (+ i 2)))\n         \
        \              -1000000000)]\n             [res3 (if (< (+ i 2) n)\n       \
        \                (- (+ s-i (vector-ref arr (+ i 1)) (vector-ref arr (+ i 2)))\
        \ (vector-ref dp (+ i 3)))\n                       -1000000000)])\n        (vector-set!\
        \ dp i (max res1 res2 res3))))\n    (let ([final (vector-ref dp 0)])\n     \
        \ (cond\n        [(> final 0) \"Alice\"]\n        [(< final 0) \"Bob\"]\n  \
        \      [else \"Tie\"]))))"
      erlang: "stone_game_iii(StoneValue) ->\n  Stones = list_to_tuple(StoneValue),\n\
        \  N = tuple_size(Stones),\n  FinalDP = solve(N - 1, Stones, N, 0, 0, 0),\n\
        \  if\n    FinalDP > 0 -> <<\"Alice\">>;\n    FinalDP < 0 -> <<\"Bob\">>;\n\
        \    true -> <<\"Tie\">>\n  end.\n\nsolve(I, _Stones, _N, DP1, _DP2, _DP3) when\
        \ I < 0 ->\n  DP1;\nsolve(I, Stones, N, DP1, DP2, DP3) ->\n  SI = element(I\
        \ + 1, Stones),\n  Res1 = SI - DP1,\n  Res2 = case I + 1 < N of\n    true ->\
        \ SI + element(I + 2, Stones) - DP2;\n    false -> -1000000000\n  end,\n  Res3\
        \ = case I + 2 < N of\n    true -> SI + element(I + 2, Stones) + element(I +\
        \ 3, Stones) - DP3;\n    false -> -1000000000\n  end,\n  CurrentDP = max(Res1,\
        \ max(Res2, Res3)),\n  solve(I - 1, Stones, N, CurrentDP, DP1, DP2)."
      elixir: "defmodule Solution do\n  @spec stone_game_iii(stone_value :: [integer])\
        \ :: String.t\n  def stone_game_iii(stone_value) do\n    stones = List.to_tuple(stone_value)\n\
        \    n = tuple_size(stones)\n\n    final_dp = solve(n - 1, stones, n, 0, 0,\
        \ 0)\n\n    cond do\n      final_dp > 0 -> \"Alice\"\n      final_dp < 0 ->\
        \ \"Bob\"\n      true -> \"Tie\"\n    end\n  end\n\n  defp solve(i, stones,\
        \ n, dp1, dp2, dp3) when i < 0 do\n    dp1\n  end\n\n  defp solve(i, stones,\
        \ n, dp1, dp2, dp3) do\n    s_i = elem(stones, i)\n\n    res1 = s_i - dp1\n\n\
        \    res2 = if i + 1 < n do\n      s_i + elem(stones, i + 1) - dp2\n    else\n\
        \      -1000000000\n    end\n\n    res3 = if i + 2 < n do\n      s_i + elem(stones,\
        \ i + 1) + elem(stones, i + 2) - dp3\n    else\n      -1000000000\n    end\n\
        \n    current_dp = max(res1, max(res2, res3))\n    solve(i - 1, stones, n, current_dp,\
        \ dp1, dp2)\n  end\nend"
    approach: The problem is modeled using dynamic programming based on a minimax game
      theory approach. We define dp[i] as the maximum relative score (current player's
      score minus the other player's score) achievable starting from the stone at index
      i. Since each player plays optimally to maximize their own total score, the player
      at turn i will choose to take 1, 2, or 3 stones such that the value of those stones
      minus the optimal relative score the opponent can achieve from the remaining stones
      is maximized.
    time_complexity: O(n) where n is the number of stones. We iterate through the stoneValue
      array exactly once from right to left, performing a constant number of operations
      (up to 3) at each index.
    space_complexity: O(n) to store the dynamic programming array. This can be optimized
      to O(1) space since calculating dp[i] only requires the values of dp[i+1], dp[i+2],
      and dp[i+3].
    elapsed_time: 236.28812384605408
    model: gemini-3-flash-preview
    generated_at: '2026-08-03 02:07:43 '
---

## Problem #1406: Stone Game III

**Difficulty:** Hard

**Topics:** Array, Math, Dynamic Programming, Game Theory

## Problem Description

<p>Alice and Bob continue their games with piles of stones. There are several stones <strong>arranged in a row</strong>, and each stone has an associated value which is an integer given in the array <code>stoneValue</code>.</p>

<p>Alice and Bob take turns, with Alice starting first. On each player&#39;s turn, that player can take <code>1</code>, <code>2</code>, or <code>3</code> stones from the <strong>first</strong> remaining stones in the row.</p>

<p>The score of each player is the sum of the values of the stones taken. The score of each player is <code>0</code> initially.</p>

<p>The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.</p>

<p>Assume Alice and Bob <strong>play optimally</strong>.</p>

<p>Return <code>&quot;Alice&quot;</code><em> if Alice will win, </em><code>&quot;Bob&quot;</code><em> if Bob will win, or </em><code>&quot;Tie&quot;</code><em> if they will end the game with the same score</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [1,2,3,7]
<strong>Output:</strong> &quot;Bob&quot;
<strong>Explanation:</strong> Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [1,2,3,-9]
<strong>Output:</strong> &quot;Alice&quot;
<strong>Explanation:</strong> Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob&#39;s score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob&#39;s score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [1,2,3,6]
<strong>Output:</strong> &quot;Tie&quot;
<strong>Explanation:</strong> Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stoneValue.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= stoneValue[i] &lt;= 1000</code></li>
</ul>


## Hints

1. The game can be mapped to minmax game. Alice tries to maximize the total score and Bob tries to minimize it.

2. Use dynamic programming to simulate the game. If the total score was 0 the game is "Tie", and if it has positive value then "Alice" wins, otherwise "Bob" wins.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is modeled using dynamic programming based on a minimax game theory approach. We define dp[i] as the maximum relative score (current player's score minus the other player's score) achievable starting from the stone at index i. Since each player plays optimally to maximize their own total score, the player at turn i will choose to take 1, 2, or 3 stones such that the value of those stones minus the optimal relative score the opponent can achieve from the remaining stones is maximized.

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
    string stoneGameIII(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<int> dp(n + 1, -1e9);
        dp[n] = 0;

        for (int i = n - 1; i >= 0; --i) {
            int take = 0;
            for (int k = 0; k < 3 && i + k < n; ++k) {
                take += stoneValue[i + k];
                dp[i] = max(dp[i], take - dp[i + k + 1]);
            }
        }

        if (dp[0] > 0) return "Alice";
        if (dp[0] < 0) return "Bob";
        return "Tie";
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        int[] dp = new int[n + 1];
        for (int i = 0; i < n; i++) dp[i] = Integer.MIN_VALUE;
        dp[n] = 0;

        for (int i = n - 1; i >= 0; i--) {
            int take = 0;
            for (int k = 0; k < 3 && i + k < n; k++) {
                take += stoneValue[i + k];
                dp[i] = Math.max(dp[i], take - dp[i + k + 1]);
            }
        }

        if (dp[0] > 0) return "Alice";
        if (dp[0] < 0) return "Bob";
        return "Tie";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        dp = [-float('inf')] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            take = 0
            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    val = take - dp[i + k + 1]
                    if val > dp[i]:
                        dp[i] = val

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        v1 = v2 = v3 = 0
        for i in range(n - 1, -1, -1):
            current_sum = stoneValue[i]
            res = current_sum - v1
            if i + 1 < n:
                current_sum += stoneValue[i + 1]
                res = max(res, current_sum - v2)
            if i + 2 < n:
                current_sum += stoneValue[i + 2]
                res = max(res, current_sum - v3)
            v3, v2, v1 = v2, v1, res

        if v1 > 0:
            return "Alice"
        elif v1 < 0:
            return "Bob"
        else:
            return "Tie"
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
char* stoneGameIII(int* stoneValue, int stoneValueSize) {
    int v1 = 0, v2 = 0, v3 = 0;
    for (int i = stoneValueSize - 1; i >= 0; i--) {
        int currentSum = stoneValue[i];
        int res = currentSum - v1;
        if (i + 1 < stoneValueSize) {
            currentSum += stoneValue[i + 1];
            int take2 = currentSum - v2;
            if (take2 > res) res = take2;
        }
        if (i + 2 < stoneValueSize) {
            currentSum += stoneValue[i + 2];
            int take3 = currentSum - v3;
            if (take3 > res) res = take3;
        }
        v3 = v2;
        v2 = v1;
        v1 = res;
    }
    if (v1 > 0) return "Alice";
    if (v1 < 0) return "Bob";
    return "Tie";
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public string StoneGameIII(int[] stoneValue) {
        int n = stoneValue.Length;
        int v1 = 0, v2 = 0, v3 = 0;
        for (int i = n - 1; i >= 0; i--) {
            int currentSum = stoneValue[i];
            int res = currentSum - v1;
            if (i + 1 < n) {
                currentSum += stoneValue[i + 1];
                res = Math.Max(res, currentSum - v2);
            }
            if (i + 2 < n) {
                currentSum += stoneValue[i + 2];
                res = Math.Max(res, currentSum - v3);
            }
            v3 = v2;
            v2 = v1;
            v1 = res;
        }
        if (v1 > 0) return "Alice";
        if (v1 < 0) return "Bob";
        return "Tie";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} stoneValue
 * @return {string}
 */
var stoneGameIII = function(stoneValue) {
    let n = stoneValue.length;
    let v1 = 0, v2 = 0, v3 = 0;
    for (let i = n - 1; i >= 0; i--) {
        let currentSum = stoneValue[i];
        let res = currentSum - v1;
        if (i + 1 < n) {
            currentSum += stoneValue[i + 1];
            res = Math.max(res, currentSum - v2);
        }
        if (i + 2 < n) {
            currentSum += stoneValue[i + 2];
            res = Math.max(res, currentSum - v3);
        }
        v3 = v2;
        v2 = v1;
        v1 = res;
    }
    if (v1 > 0) return "Alice";
    if (v1 < 0) return "Bob";
    return "Tie";
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function stoneGameIII(stoneValue: number[]): string {
    const n = stoneValue.length;
    const dp = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        let maxRelative = -Infinity;
        let currentTake = 0;
        for (let k = 0; k < 3 && i + k < n; k++) {
            currentTake += stoneValue[i + k];
            const currentRes = currentTake - dp[i + k + 1];
            if (currentRes > maxRelative) {
                maxRelative = currentRes;
            }
        }
        dp[i] = maxRelative;
    }
    if (dp[0] > 0) return "Alice";
    if (dp[0] < 0) return "Bob";
    return "Tie";
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $stoneValue
     * @return String
     */
    function stoneGameIII($stoneValue) {
        $n = count($stoneValue);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $maxRelative = -PHP_INT_MAX;
            $currentTake = 0;
            for ($k = 0; $k < 3 && $i + $k < $n; $k++) {
                $currentTake += $stoneValue[$i + $k];
                $currentRes = $currentTake - $dp[$i + $k + 1];
                if ($currentRes > $maxRelative) {
                    $maxRelative = $currentRes;
                }
            }
            $dp[$i] = $maxRelative;
        }
        if ($dp[0] > 0) return "Alice";
        if ($dp[0] < 0) return "Bob";
        return "Tie";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func stoneGameIII(_ stoneValue: [Int]) -> String {
        let n = stoneValue.count
        var dp = [Int](repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            var maxRelative = Int.min
            var currentTake = 0
            for k in 0..<3 {
                if i + k < n {
                    currentTake += stoneValue[i + k]
                    let currentRes = currentTake - dp[i + k + 1]
                    if currentRes > maxRelative {
                        maxRelative = currentRes
                    }
                }
            }
            dp[i] = maxRelative
        }
        if dp[0] > 0 { return "Alice" }
        if dp[0] < 0 { return "Bob" }
        return "Tie"
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun stoneGameIII(stoneValue: IntArray): String {
        val n = stoneValue.size
        val dp = IntArray(n + 1)
        for (i in n - 1 downTo 0) {
            var maxRelative = Int.MIN_VALUE
            var currentTake = 0
            for (k in 0..2) {
                if (i + k < n) {
                    currentTake += stoneValue[i + k]
                    val currentRes = currentTake - dp[i + k + 1]
                    if (currentRes > maxRelative) {
                        maxRelative = currentRes
                    }
                }
            }
            dp[i] = maxRelative
        }
        return when {
            dp[0] > 0 -> "Alice"
            dp[0] < 0 -> "Bob"
            else -> "Tie"
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String stoneGameIII(List<int> stoneValue) {
    int n = stoneValue.length;
    List<int> dp = List.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
      int res = stoneValue[i] - dp[i + 1];
      if (i + 1 < n) {
        int take2 = stoneValue[i] + stoneValue[i + 1] - dp[i + 2];
        if (take2 > res) res = take2;
      }
      if (i + 2 < n) {
        int take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3];
        if (take3 > res) res = take3;
      }
      dp[i] = res;
    }
    if (dp[0] > 0) return "Alice";
    if (dp[0] < 0) return "Bob";
    return "Tie";
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func stoneGameIII(stoneValue []int) string {
    n := len(stoneValue)
    dp := make([]int, n+1)
    for i := n - 1; i >= 0; i-- {
        res := stoneValue[i] - dp[i+1]
        if i+1 < n {
            sum2 := stoneValue[i] + stoneValue[i+1] - dp[i+2]
            if sum2 > res {
                res = sum2
            }
        }
        if i+2 < n {
            sum3 := stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3]
            if sum3 > res {
                res = sum3
            }
        }
        dp[i] = res
    }
    if dp[0] > 0 {
        return "Alice"
    }
    if dp[0] < 0 {
        return "Bob"
    }
    return "Tie"
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} stone_value
# @return {String}
def stone_game_iii(stone_value)
  n = stone_value.length
  dp = Array.new(n + 1, 0)
  (n - 1).downto(0) do |i|
    res = stone_value[i] - dp[i + 1]
    if i + 1 < n
      val2 = stone_value[i] + stone_value[i + 1] - dp[i + 2]
      res = val2 if val2 > res
    end
    if i + 2 < n
      val3 = stone_value[i] + stone_value[i + 1] + stone_value[i + 2] - dp[i + 3]
      res = val3 if val3 > res
    end
    dp[i] = res
  end
  if dp[0] > 0
    return "Alice"
  elsif dp[0] < 0
    return "Bob"
  else
    return "Tie"
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def stoneGameIII(stoneValue: Array[Int]): String = {
        val n = stoneValue.length
        val dp = new Array[Int](n + 1)
        for (i <- n - 1 to 0 by -1) {
            var res = stoneValue(i) - dp(i + 1)
            if (i + 1 < n) {
                val val2 = stoneValue(i) + stoneValue(i + 1) - dp(i + 2)
                if (val2 > res) res = val2
            }
            if (i + 2 < n) {
                val val3 = stoneValue(i) + stoneValue(i + 1) + stoneValue(i + 2) - dp(i + 3)
                if (val3 > res) res = val3
            }
            dp(i) = res
        }
        if (dp(0) > 0) "Alice"
        else if (dp(0) < 0) "Bob"
        else "Tie"
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
        let n = stone_value.len();
        let mut dp = vec![0; n + 3];
        for i in (0..n).rev() {
            let s_i = stone_value[i];
            let res1 = s_i - dp[i + 1];
            let mut res2 = -1_000_000_000;
            if i + 1 < n {
                res2 = s_i + stone_value[i + 1] - dp[i + 2];
            }
            let mut res3 = -1_000_000_000;
            if i + 2 < n {
                res3 = s_i + stone_value[i + 1] + stone_value[i + 2] - dp[i + 3];
            }
            dp[i] = res1.max(res2).max(res3);
        }

        if dp[0] > 0 {
            "Alice".to_string()
        } else if dp[0] < 0 {
            "Bob".to_string()
        } else {
            "Tie".to_string()
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (stone-game-iii stoneValue)
  (-> (listof exact-integer?) string?)
  (let* ([n (length stoneValue)]
         [arr (list->vector stoneValue)]
         [dp (make-vector (+ n 3) 0)])
    (for ([i (in-range (- n 1) -1 -1)])
      (let* ([s-i (vector-ref arr i)]
             [res1 (- s-i (vector-ref dp (+ i 1)))]
             [res2 (if (< (+ i 1) n)
                       (- (+ s-i (vector-ref arr (+ i 1))) (vector-ref dp (+ i 2)))
                       -1000000000)]
             [res3 (if (< (+ i 2) n)
                       (- (+ s-i (vector-ref arr (+ i 1)) (vector-ref arr (+ i 2))) (vector-ref dp (+ i 3)))
                       -1000000000)])
        (vector-set! dp i (max res1 res2 res3))))
    (let ([final (vector-ref dp 0)])
      (cond
        [(> final 0) "Alice"]
        [(< final 0) "Bob"]
        [else "Tie"]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
stone_game_iii(StoneValue) ->
  Stones = list_to_tuple(StoneValue),
  N = tuple_size(Stones),
  FinalDP = solve(N - 1, Stones, N, 0, 0, 0),
  if
    FinalDP > 0 -> <<"Alice">>;
    FinalDP < 0 -> <<"Bob">>;
    true -> <<"Tie">>
  end.

solve(I, _Stones, _N, DP1, _DP2, _DP3) when I < 0 ->
  DP1;
solve(I, Stones, N, DP1, DP2, DP3) ->
  SI = element(I + 1, Stones),
  Res1 = SI - DP1,
  Res2 = case I + 1 < N of
    true -> SI + element(I + 2, Stones) - DP2;
    false -> -1000000000
  end,
  Res3 = case I + 2 < N of
    true -> SI + element(I + 2, Stones) + element(I + 3, Stones) - DP3;
    false -> -1000000000
  end,
  CurrentDP = max(Res1, max(Res2, Res3)),
  solve(I - 1, Stones, N, CurrentDP, DP1, DP2).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec stone_game_iii(stone_value :: [integer]) :: String.t
  def stone_game_iii(stone_value) do
    stones = List.to_tuple(stone_value)
    n = tuple_size(stones)

    final_dp = solve(n - 1, stones, n, 0, 0, 0)

    cond do
      final_dp > 0 -> "Alice"
      final_dp < 0 -> "Bob"
      true -> "Tie"
    end
  end

  defp solve(i, stones, n, dp1, dp2, dp3) when i < 0 do
    dp1
  end

  defp solve(i, stones, n, dp1, dp2, dp3) do
    s_i = elem(stones, i)

    res1 = s_i - dp1

    res2 = if i + 1 < n do
      s_i + elem(stones, i + 1) - dp2
    else
      -1000000000
    end

    res3 = if i + 2 < n do
      s_i + elem(stones, i + 1) + elem(stones, i + 2) - dp3
    else
      -1000000000
    end

    current_dp = max(res1, max(res2, res3))
    solve(i - 1, stones, n, current_dp, dp1, dp2)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of stones. We iterate through the stoneValue array exactly once from right to left, performing a constant number of operations (up to 3) at each index.
- **Space Complexity:** O(n) to store the dynamic programming array. This can be optimized to O(1) space since calculating dp[i] only requires the values of dp[i+1], dp[i+2], and dp[i+3].
