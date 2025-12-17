---
layout: post
title: "Best Time to Buy and Sell Stock V"
date: 2025-12-17 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxProfit(vector<int>& prices, int k)\
        \ {\n        int n = prices.size();\n        if (n < 2) return 0;\n        k\
        \ = min(k, n / 2);\n        vector<vector<int>> buy(n, vector<int>(k + 1, 0));\n\
        \        vector<vector<int>> sell(n, vector<int>(k + 1, 0));\n        for (int\
        \ i = 1; i < n; i++) {\n            for (int j = 1; j <= k; j++) {\n       \
        \         buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i]);\n\
        \                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i]);\n\
        \            }\n        }\n        return sell[n - 1][k];\n    }\n};"
      java: "class Solution {\n    public int maxProfit(int[] prices, int k) {\n   \
        \     int n = prices.length;\n        if (n < 2) return 0;\n        k = Math.min(k,\
        \ n / 2);\n        int[][] buy = new int[n][k + 1];\n        int[][] sell =\
        \ new int[n][k + 1];\n        for (int i = 1; i < n; i++) {\n            for\
        \ (int j = 1; j <= k; j++) {\n                buy[i][j] = Math.max(buy[i - 1][j],\
        \ sell[i - 1][j - 1] - prices[i]);\n                sell[i][j] = Math.max(sell[i\
        \ - 1][j], buy[i - 1][j] + prices[i]);\n            }\n        }\n        return\
        \ sell[n - 1][k];\n    }\n}"
      python: "class Solution:\n    def maxProfit(self, prices: List[int], k: int) ->\
        \ int:\n        n = len(prices)\n        if n < 2: return 0\n        k = min(k,\
        \ n // 2)\n        buy = [[0] * (k + 1) for _ in range(n)]\n        sell = [[0]\
        \ * (k + 1) for _ in range(n)]\n        for i in range(1, n):\n            for\
        \ j in range(1, k + 1):\n                buy[i][j] = max(buy[i - 1][j], sell[i\
        \ - 1][j - 1] - prices[i])\n                sell[i][j] = max(sell[i - 1][j],\
        \ buy[i - 1][j] + prices[i])\n        return sell[n - 1][k]"
      python3: "class Solution:\n    def maxProfit(self, prices: List[int], k: int)\
        \ -> int:\n        n = len(prices)\n        if n < 2: return 0\n        k =\
        \ min(k, n // 2)\n        buy = [[0] * (k + 1) for _ in range(n)]\n        sell\
        \ = [[0] * (k + 1) for _ in range(n)]\n        for i in range(1, n):\n     \
        \       for j in range(1, k + 1):\n                buy[i][j] = max(buy[i - 1][j],\
        \ sell[i - 1][j - 1] - prices[i])\n                sell[i][j] = max(sell[i -\
        \ 1][j], buy[i - 1][j] + prices[i])\n        return sell[n - 1][k]"
      c: "typedef struct {\n    int* arr;\n    int size;\n} Array;\n\nint maxProfit(int*\
        \ prices, int pricesSize, int k) {\n    if (pricesSize < 2) return 0;\n    k\
        \ = k < pricesSize / 2 ? k : pricesSize / 2;\n    int** buy = (int**)malloc(pricesSize\
        \ * sizeof(int*));\n    int** sell = (int**)malloc(pricesSize * sizeof(int*));\n\
        \    for (int i = 0; i < pricesSize; i++) {\n        buy[i] = (int*)malloc((k\
        \ + 1) * sizeof(int));\n        sell[i] = (int*)malloc((k + 1) * sizeof(int));\n\
        \    }\n    for (int i = 1; i < pricesSize; i++) {\n        for (int j = 1;\
        \ j <= k; j++) {\n            buy[i][j] = (buy[i - 1][j] > sell[i - 1][j - 1]\
        \ - prices[i]) ? buy[i - 1][j] : sell[i - 1][j - 1] - prices[i];\n         \
        \   sell[i][j] = (sell[i - 1][j] > buy[i - 1][j] + prices[i]) ? sell[i - 1][j]\
        \ : buy[i - 1][j] + prices[i];\n        }\n    }\n    int result = sell[pricesSize\
        \ - 1][k];\n    for (int i = 0; i < pricesSize; i++) {\n        free(buy[i]);\n\
        \        free(sell[i]);\n    }\n    free(buy);\n    free(sell);\n    return\
        \ result;\n}"
      csharp: "public class Solution {\n    public int MaxProfit(int[] prices, int k)\
        \ {\n        int n = prices.Length;\n        if (n < 2) return 0;\n        k\
        \ = Math.Min(k, n / 2);\n        int[][] buy = new int[n][];\n        int[][]\
        \ sell = new int[n][];\n        for (int i = 0; i < n; i++) {\n            buy[i]\
        \ = new int[k + 1];\n            sell[i] = new int[k + 1];\n        }\n    \
        \    for (int i = 1; i < n; i++) {\n            for (int j = 1; j <= k; j++)\
        \ {\n                buy[i][j] = Math.Max(buy[i - 1][j], sell[i - 1][j - 1]\
        \ - prices[i]);\n                sell[i][j] = Math.Max(sell[i - 1][j], buy[i\
        \ - 1][j] + prices[i]);\n            }\n        }\n        return sell[n - 1][k];\n\
        \    }\n}"
      javascript: "var maxProfit = function(prices, k) {\n    let n = prices.length;\n\
        \    if (n < 2) return 0;\n    k = Math.min(k, Math.floor(n / 2));\n    let\
        \ buy = Array(n).fill(0).map(() => Array(k + 1).fill(0));\n    let sell = Array(n).fill(0).map(()\
        \ => Array(k + 1).fill(0));\n    for (let i = 1; i < n; i++) {\n        for\
        \ (let j = 1; j <= k; j++) {\n            buy[i][j] = Math.max(buy[i - 1][j],\
        \ sell[i - 1][j - 1] - prices[i]);\n            sell[i][j] = Math.max(sell[i\
        \ - 1][j], buy[i - 1][j] + prices[i]);\n        }\n    }\n    return sell[n\
        \ - 1][k];\n};"
      typescript: "function maxProfit(prices: number[], k: number): number {\n    let\
        \ n = prices.length;\n    if (n < 2) return 0;\n    k = Math.min(k, Math.floor(n\
        \ / 2));\n    let buy: number[][] = Array(n).fill(0).map(() => Array(k + 1).fill(0));\n\
        \    let sell: number[][] = Array(n).fill(0).map(() => Array(k + 1).fill(0));\n\
        \    for (let i = 1; i < n; i++) {\n        for (let j = 1; j <= k; j++) {\n\
        \            buy[i][j] = Math.max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i]);\n\
        \            sell[i][j] = Math.max(sell[i - 1][j], buy[i - 1][j] + prices[i]);\n\
        \        }\n    }\n    return sell[n - 1][k];\n}"
      php: "class Solution {\n    function maxProfit($prices, $k) {\n        $n = count($prices);\n\
        \        if ($n < 2) return 0;\n        $k = min($k, floor($n / 2));\n     \
        \   $buy = array_fill(0, $n, array_fill(0, $k + 1, 0));\n        $sell = array_fill(0,\
        \ $n, array_fill(0, $k + 1, 0));\n        for ($i = 1; $i < $n; $i++) {\n  \
        \          for ($j = 1; $j <= $k; $j++) {\n                $buy[$i][$j] = max($buy[$i\
        \ - 1][$j], $sell[$i - 1][$j - 1] - $prices[$i]);\n                $sell[$i][$j]\
        \ = max($sell[$i - 1][$j], $buy[$i - 1][$j] + $prices[$i]);\n            }\n\
        \        }\n        return $sell[$n - 1][$k];\n    }\n}"
      swift: "class Solution {\n    func maxProfit(_ prices: [Int], _ k: Int) -> Int\
        \ {\n        let n = prices.count\n        if n < 2 { return 0 }\n        let\
        \ k = min(k, n / 2)\n        var buy = Array(repeating: Array(repeating: 0,\
        \ count: k + 1), count: n)\n        var sell = Array(repeating: Array(repeating:\
        \ 0, count: k + 1), count: n)\n        for i in 1..<n {\n            for j in\
        \ 1...k {\n                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1]\
        \ - prices[i])\n                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j]\
        \ + prices[i])\n            }\n        }\n        return sell[n - 1][k]\n  \
        \  }\n}"
      kotlin: "class Solution {\n    fun maxProfit(prices: IntArray, k: Int): Int {\n\
        \        val n = prices.size\n        if (n < 2) return 0\n        val k = minOf(k,\
        \ n / 2)\n        val buy = Array(n) { IntArray(k + 1) }\n        val sell =\
        \ Array(n) { IntArray(k + 1) }\n        for (i in 1 until n) {\n           \
        \ for (j in 1..k) {\n                buy[i][j] = maxOf(buy[i - 1][j], sell[i\
        \ - 1][j - 1] - prices[i])\n                sell[i][j] = maxOf(sell[i - 1][j],\
        \ buy[i - 1][j] + prices[i])\n            }\n        }\n        return sell[n\
        \ - 1][k]\n    }\n}"
      dart: "class Solution {\n    int maxProfit(List<int> prices, int k) {\n      \
        \  int n = prices.length;\n        if (n < 2) return 0;\n        k = k < n ~/\
        \ 2 ? k : n ~/ 2;\n        List<List<int>> buy = List.generate(n, (i) => List.generate(k\
        \ + 1, (j) => 0));\n        List<List<int>> sell = List.generate(n, (i) => List.generate(k\
        \ + 1, (j) => 0));\n        for (int i = 1; i < n; i++) {\n            for (int\
        \ j = 1; j <= k; j++) {\n                buy[i][j] = max(buy[i - 1][j], sell[i\
        \ - 1][j - 1] - prices[i]);\n                sell[i][j] = max(sell[i - 1][j],\
        \ buy[i - 1][j] + prices[i]);\n            }\n        }\n        return sell[n\
        \ - 1][k];\n    }\n}"
      go: "func maxProfit(prices []int, k int) int {\n    n := len(prices)\n    if n\
        \ < 2 {\n        return 0\n    }\n    k = min(k, n/2)\n    buy := make([][]int,\
        \ n)\n    sell := make([][]int, n)\n    for i := range buy {\n        buy[i]\
        \ = make([]int, k+1)\n        sell[i] = make([]int, k+1)\n    }\n    for i :=\
        \ 1; i < n; i++ {\n        for j := 1; j <= k; j++ {\n            buy[i][j]\
        \ = max(buy[i-1][j], sell[i-1][j-1]-prices[i])\n            sell[i][j] = max(sell[i-1][j],\
        \ buy[i-1][j]+prices[i])\n        }\n    }\n    return sell[n-1][k]\n}\n\nfunc\
        \ max(a, b int) int {\n    if a > b {\n        return a\n    }\n    return b\n\
        }\n\nfunc min(a, b int) int {\n    if a < b {\n        return a\n    }\n   \
        \ return b\n}"
      ruby: "class Solution\n    def max_profit(prices, k)\n        n = prices.size\n\
        \        return 0 if n < 2\n        k = [k, n / 2].min\n        buy = Array.new(n)\
        \ { Array.new(k + 1, 0) }\n        sell = Array.new(n) { Array.new(k + 1, 0)\
        \ }\n        (1...n).each do |i|\n            (1..k).each do |j|\n         \
        \       buy[i][j] = [buy[i - 1][j], sell[i - 1][j - 1] - prices[i]].max\n  \
        \              sell[i][j] = [sell[i - 1][j], buy[i - 1][j] + prices[i]].max\n\
        \            end\n        end\n        sell[n - 1][k]\n    end\nend"
      scala: "object Solution {\n    def maxProfit(prices: Array[Int], k: Int): Int\
        \ = {\n        val n = prices.length\n        if (n < 2) return 0\n        val\
        \ k = math.min(k, n / 2)\n        val buy = Array.ofDim[Int](n, k + 1)\n   \
        \     val sell = Array.ofDim[Int](n, k + 1)\n        for (i <- 1 until n) {\n\
        \            for (j <- 1 to k) {\n                buy(i)(j) = math.max(buy(i\
        \ - 1)(j), sell(i - 1)(j - 1) - prices(i))\n                sell(i)(j) = math.max(sell(i\
        \ - 1)(j), buy(i - 1)(j) + prices(i))\n            }\n        }\n        sell(n\
        \ - 1)(k)\n    }\n}"
      rust: "struct Solution;\nimpl Solution {\n    pub fn max_profit(prices: Vec<i32>,\
        \ k: i32) -> i32 {\n        let n = prices.len();\n        if n < 2 {\n    \
        \        return 0;\n        }\n        let k = k.min(n as i32 / 2);\n      \
        \  let mut buy = vec![vec![0; k as usize + 1]; n];\n        let mut sell = vec![vec![0;\
        \ k as usize + 1]; n];\n        for i in 1..n {\n            for j in 1..=k\
        \ as usize {\n                buy[i][j] = buy[i - 1][j].max(sell[i - 1][j -\
        \ 1] - prices[i]);\n                sell[i][j] = sell[i - 1][j].max(buy[i -\
        \ 1][j] + prices[i]);\n            }\n        }\n        sell[n - 1][k as usize]\n\
        \    }\n}"
      racket: "define (max-profit prices k)\n    (let* (\n        (n (length prices))\n\
        \        (k (min k (quotient n 2)))\n        (buy (make-list n (make-list (+\
        \ k 1) 0)))\n        (sell (make-list n (make-list (+ k 1) 0))))\n        (for\
        \ (\n            ((i (in-range 1 n)))\n            ((j (in-range 1 (+ k 1))))\n\
        \            (set! (list-ref (list-ref buy i) j) (max (list-ref (list-ref buy\
        \ (- i 1)) j) (- (list-ref (list-ref sell (- i 1)) (- j 1)) (list-ref prices\
        \ i))))\n            (set! (list-ref (list-ref sell i) j) (max (list-ref (list-ref\
        \ sell (- i 1)) j) (+ (list-ref (list-ref buy (- i 1)) j) (list-ref prices i))))))\n\
        \        (list-ref (list-ref sell (- n 1)) k))"
      erlang: "max_profit(Prices, K) ->\n    N = length(Prices),\n    K1 = min(K, N\
        \ div 2),\n    Buy = array:new(N, {default, array:new(K1 + 1, {default, 0})}),\n\
        \    Sell = array:new(N, {default, array:new(K1 + 1, {default, 0})}),\n    lists:foreach(fun(I)\
        \ ->\n        lists:foreach(fun(J) ->\n            Buy1 = array:get(I, Buy),\n\
        \            Sell1 = array:get(I, Sell),\n            Buy2 = array:get(I - 1,\
        \ Buy),\n            Sell2 = array:get(I - 1, Sell),\n            array:set(J,\
        \ max(array:get(J, Buy2), array:get(J - 1, Sell2) - lists:nth(I + 1, Prices),\
        \ Buy1), Buy),\n            array:set(J, max(array:get(J, Sell2), array:get(J,\
        \ Buy2) + lists:nth(I + 1, Prices), Sell1), Sell)\n        end, lists:seq(1,\
        \ K1)),\n        lists:seq(1, N - 1)),\n    array:get(K1, array:get(N - 1, Sell))."
      elixir: "defmodule Solution do\n    def max_profit(prices, k) do\n        n =\
        \ length(prices)\n        if n < 2, do: 0\n        k = min(k, div(n, 2))\n \
        \       buy = for _ <- 1..n, do: for _ <- 1..k + 1, do: 0\n        sell = for\
        \ _ <- 1..n, do: for _ <- 1..k + 1, do: 0\n        for i <- 1..n - 1 do\n  \
        \          for j <- 1..k do\n                buy = update_in(buy, [i, j], fn\
        \ x -> max(x, Enum.at(sell, i - 1) |> Enum.at(j - 1) - Enum.at(prices, i)) end)\n\
        \                sell = update_in(sell, [i, j], fn x -> max(x, Enum.at(buy,\
        \ i - 1) |> Enum.at(j) + Enum.at(prices, i)) end)\n            end\n       \
        \ end\n        Enum.at(Enum.at(sell, n - 1), k)\n    end\nend"
    approach: The problem can be solved using dynamic programming. We need to keep track
      of the maximum profit we can get after a certain number of transactions. We can
      use a 2D array to store the maximum profit after each transaction. The key intuition
      is that we can either choose to make a transaction on the current day or not.
      If we choose to make a transaction, we need to consider whether it's a normal
      transaction or a short selling transaction. We can calculate the maximum profit
      by considering all possible transactions and choosing the one that gives us the
      maximum profit. The dynamic programming approach allows us to avoid redundant
      calculations and solve the problem efficiently.
    time_complexity: The time complexity of the solution is O(n * k), where n is the
      number of days and k is the number of transactions. This is because we need to
      iterate over each day and each transaction to calculate the maximum profit.
    space_complexity: The space complexity of the solution is O(n * k), where n is the
      number of days and k is the number of transactions. This is because we need to
      store the maximum profit after each transaction in a 2D array.
    elapsed_time: 9.699870347976685
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-17 02:03:55 '
---

## Problem #3573: Best Time to Buy and Sell Stock V

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming

## Problem Description

<p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a stock in dollars on the <code>i<sup>th</sup></code> day, and an integer <code>k</code>.</p>

<p>You are allowed to make at most <code>k</code> transactions, where each transaction can be either of the following:</p>

<ul>
	<li>
	<p><strong>Normal transaction</strong>: Buy on day <code>i</code>, then sell on a later day <code>j</code> where <code>i &lt; j</code>. You profit <code>prices[j] - prices[i]</code>.</p>
	</li>
	<li>
	<p><strong>Short selling transaction</strong>: Sell on day <code>i</code>, then buy back on a later day <code>j</code> where <code>i &lt; j</code>. You profit <code>prices[i] - prices[j]</code>.</p>
	</li>
</ul>

<p><strong>Note</strong> that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.</p>

<p>Return the <strong>maximum</strong> total profit you can earn by making <strong>at most</strong> <code>k</code> transactions.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">prices = [1,7,9,8,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>
We can make $14 of profit through 2 transactions:

<ul>
	<li>A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.</li>
	<li>A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">prices = [12,16,19,19,8,1,19,13,9], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">36</span></p>

<p><strong>Explanation:</strong></p>
We can make $36 of profit through 3 transactions:

<ul>
	<li>A normal transaction: buy the stock on day 0 for $12 then sell it on day 2 for $19.</li>
	<li>A short selling transaction: sell the stock on day 3 for $19 then buy back on day 4 for $8.</li>
	<li>A normal transaction: buy the stock on day 5 for $1 then sell it on day 6 for $19.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= prices.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= prices.length / 2</code></li>
</ul>


## Hints

1. Use dynamic programming.

2. Keep the following states: `idx`, `transactionsDone`, `transactionType`, `isTransactionRunning`.

3. Transactions transition from completed -> running and from running -> completed.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-17 02:03:55 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. We need to keep track of the maximum profit we can get after a certain number of transactions. We can use a 2D array to store the maximum profit after each transaction. The key intuition is that we can either choose to make a transaction on the current day or not. If we choose to make a transaction, we need to consider whether it's a normal transaction or a short selling transaction. We can calculate the maximum profit by considering all possible transactions and choosing the one that gives us the maximum profit. The dynamic programming approach allows us to avoid redundant calculations and solve the problem efficiently.

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
class Solution {
public:
    int maxProfit(vector<int>& prices, int k) {
        int n = prices.size();
        if (n < 2) return 0;
        k = min(k, n / 2);
        vector<vector<int>> buy(n, vector<int>(k + 1, 0));
        vector<vector<int>> sell(n, vector<int>(k + 1, 0));
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i]);
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i]);
            }
        }
        return sell[n - 1][k];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxProfit(int[] prices, int k) {
        int n = prices.length;
        if (n < 2) return 0;
        k = Math.min(k, n / 2);
        int[][] buy = new int[n][k + 1];
        int[][] sell = new int[n][k + 1];
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                buy[i][j] = Math.max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i]);
                sell[i][j] = Math.max(sell[i - 1][j], buy[i - 1][j] + prices[i]);
            }
        }
        return sell[n - 1][k];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2: return 0
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]
        for i in range(1, n):
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i])
        return sell[n - 1][k]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2: return 0
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]
        for i in range(1, n):
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i])
        return sell[n - 1][k]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int* arr;
    int size;
} Array;

int maxProfit(int* prices, int pricesSize, int k) {
    if (pricesSize < 2) return 0;
    k = k < pricesSize / 2 ? k : pricesSize / 2;
    int** buy = (int**)malloc(pricesSize * sizeof(int*));
    int** sell = (int**)malloc(pricesSize * sizeof(int*));
    for (int i = 0; i < pricesSize; i++) {
        buy[i] = (int*)malloc((k + 1) * sizeof(int));
        sell[i] = (int*)malloc((k + 1) * sizeof(int));
    }
    for (int i = 1; i < pricesSize; i++) {
        for (int j = 1; j <= k; j++) {
            buy[i][j] = (buy[i - 1][j] > sell[i - 1][j - 1] - prices[i]) ? buy[i - 1][j] : sell[i - 1][j - 1] - prices[i];
            sell[i][j] = (sell[i - 1][j] > buy[i - 1][j] + prices[i]) ? sell[i - 1][j] : buy[i - 1][j] + prices[i];
        }
    }
    int result = sell[pricesSize - 1][k];
    for (int i = 0; i < pricesSize; i++) {
        free(buy[i]);
        free(sell[i]);
    }
    free(buy);
    free(sell);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxProfit(int[] prices, int k) {
        int n = prices.Length;
        if (n < 2) return 0;
        k = Math.Min(k, n / 2);
        int[][] buy = new int[n][];
        int[][] sell = new int[n][];
        for (int i = 0; i < n; i++) {
            buy[i] = new int[k + 1];
            sell[i] = new int[k + 1];
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                buy[i][j] = Math.Max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i]);
                sell[i][j] = Math.Max(sell[i - 1][j], buy[i - 1][j] + prices[i]);
            }
        }
        return sell[n - 1][k];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxProfit = function(prices, k) {
    let n = prices.length;
    if (n < 2) return 0;
    k = Math.min(k, Math.floor(n / 2));
    let buy = Array(n).fill(0).map(() => Array(k + 1).fill(0));
    let sell = Array(n).fill(0).map(() => Array(k + 1).fill(0));
    for (let i = 1; i < n; i++) {
        for (let j = 1; j <= k; j++) {
            buy[i][j] = Math.max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i]);
            sell[i][j] = Math.max(sell[i - 1][j], buy[i - 1][j] + prices[i]);
        }
    }
    return sell[n - 1][k];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxProfit(prices: number[], k: number): number {
    let n = prices.length;
    if (n < 2) return 0;
    k = Math.min(k, Math.floor(n / 2));
    let buy: number[][] = Array(n).fill(0).map(() => Array(k + 1).fill(0));
    let sell: number[][] = Array(n).fill(0).map(() => Array(k + 1).fill(0));
    for (let i = 1; i < n; i++) {
        for (let j = 1; j <= k; j++) {
            buy[i][j] = Math.max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i]);
            sell[i][j] = Math.max(sell[i - 1][j], buy[i - 1][j] + prices[i]);
        }
    }
    return sell[n - 1][k];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxProfit($prices, $k) {
        $n = count($prices);
        if ($n < 2) return 0;
        $k = min($k, floor($n / 2));
        $buy = array_fill(0, $n, array_fill(0, $k + 1, 0));
        $sell = array_fill(0, $n, array_fill(0, $k + 1, 0));
        for ($i = 1; $i < $n; $i++) {
            for ($j = 1; $j <= $k; $j++) {
                $buy[$i][$j] = max($buy[$i - 1][$j], $sell[$i - 1][$j - 1] - $prices[$i]);
                $sell[$i][$j] = max($sell[$i - 1][$j], $buy[$i - 1][$j] + $prices[$i]);
            }
        }
        return $sell[$n - 1][$k];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxProfit(_ prices: [Int], _ k: Int) -> Int {
        let n = prices.count
        if n < 2 { return 0 }
        let k = min(k, n / 2)
        var buy = Array(repeating: Array(repeating: 0, count: k + 1), count: n)
        var sell = Array(repeating: Array(repeating: 0, count: k + 1), count: n)
        for i in 1..<n {
            for j in 1...k {
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i])
            }
        }
        return sell[n - 1][k]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxProfit(prices: IntArray, k: Int): Int {
        val n = prices.size
        if (n < 2) return 0
        val k = minOf(k, n / 2)
        val buy = Array(n) { IntArray(k + 1) }
        val sell = Array(n) { IntArray(k + 1) }
        for (i in 1 until n) {
            for (j in 1..k) {
                buy[i][j] = maxOf(buy[i - 1][j], sell[i - 1][j - 1] - prices[i])
                sell[i][j] = maxOf(sell[i - 1][j], buy[i - 1][j] + prices[i])
            }
        }
        return sell[n - 1][k]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int maxProfit(List<int> prices, int k) {
        int n = prices.length;
        if (n < 2) return 0;
        k = k < n ~/ 2 ? k : n ~/ 2;
        List<List<int>> buy = List.generate(n, (i) => List.generate(k + 1, (j) => 0));
        List<List<int>> sell = List.generate(n, (i) => List.generate(k + 1, (j) => 0));
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i]);
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i]);
            }
        }
        return sell[n - 1][k];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxProfit(prices []int, k int) int {
    n := len(prices)
    if n < 2 {
        return 0
    }
    k = min(k, n/2)
    buy := make([][]int, n)
    sell := make([][]int, n)
    for i := range buy {
        buy[i] = make([]int, k+1)
        sell[i] = make([]int, k+1)
    }
    for i := 1; i < n; i++ {
        for j := 1; j <= k; j++ {
            buy[i][j] = max(buy[i-1][j], sell[i-1][j-1]-prices[i])
            sell[i][j] = max(sell[i-1][j], buy[i-1][j]+prices[i])
        }
    }
    return sell[n-1][k]
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
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def max_profit(prices, k)
        n = prices.size
        return 0 if n < 2
        k = [k, n / 2].min
        buy = Array.new(n) { Array.new(k + 1, 0) }
        sell = Array.new(n) { Array.new(k + 1, 0) }
        (1...n).each do |i|
            (1..k).each do |j|
                buy[i][j] = [buy[i - 1][j], sell[i - 1][j - 1] - prices[i]].max
                sell[i][j] = [sell[i - 1][j], buy[i - 1][j] + prices[i]].max
            end
        end
        sell[n - 1][k]
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxProfit(prices: Array[Int], k: Int): Int = {
        val n = prices.length
        if (n < 2) return 0
        val k = math.min(k, n / 2)
        val buy = Array.ofDim[Int](n, k + 1)
        val sell = Array.ofDim[Int](n, k + 1)
        for (i <- 1 until n) {
            for (j <- 1 to k) {
                buy(i)(j) = math.max(buy(i - 1)(j), sell(i - 1)(j - 1) - prices(i))
                sell(i)(j) = math.max(sell(i - 1)(j), buy(i - 1)(j) + prices(i))
            }
        }
        sell(n - 1)(k)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;
impl Solution {
    pub fn max_profit(prices: Vec<i32>, k: i32) -> i32 {
        let n = prices.len();
        if n < 2 {
            return 0;
        }
        let k = k.min(n as i32 / 2);
        let mut buy = vec![vec![0; k as usize + 1]; n];
        let mut sell = vec![vec![0; k as usize + 1]; n];
        for i in 1..n {
            for j in 1..=k as usize {
                buy[i][j] = buy[i - 1][j].max(sell[i - 1][j - 1] - prices[i]);
                sell[i][j] = sell[i - 1][j].max(buy[i - 1][j] + prices[i]);
            }
        }
        sell[n - 1][k as usize]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (max-profit prices k)
    (let* (
        (n (length prices))
        (k (min k (quotient n 2)))
        (buy (make-list n (make-list (+ k 1) 0)))
        (sell (make-list n (make-list (+ k 1) 0))))
        (for (
            ((i (in-range 1 n)))
            ((j (in-range 1 (+ k 1))))
            (set! (list-ref (list-ref buy i) j) (max (list-ref (list-ref buy (- i 1)) j) (- (list-ref (list-ref sell (- i 1)) (- j 1)) (list-ref prices i))))
            (set! (list-ref (list-ref sell i) j) (max (list-ref (list-ref sell (- i 1)) j) (+ (list-ref (list-ref buy (- i 1)) j) (list-ref prices i))))))
        (list-ref (list-ref sell (- n 1)) k))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_profit(Prices, K) ->
    N = length(Prices),
    K1 = min(K, N div 2),
    Buy = array:new(N, {default, array:new(K1 + 1, {default, 0})}),
    Sell = array:new(N, {default, array:new(K1 + 1, {default, 0})}),
    lists:foreach(fun(I) ->
        lists:foreach(fun(J) ->
            Buy1 = array:get(I, Buy),
            Sell1 = array:get(I, Sell),
            Buy2 = array:get(I - 1, Buy),
            Sell2 = array:get(I - 1, Sell),
            array:set(J, max(array:get(J, Buy2), array:get(J - 1, Sell2) - lists:nth(I + 1, Prices), Buy1), Buy),
            array:set(J, max(array:get(J, Sell2), array:get(J, Buy2) + lists:nth(I + 1, Prices), Sell1), Sell)
        end, lists:seq(1, K1)),
        lists:seq(1, N - 1)),
    array:get(K1, array:get(N - 1, Sell)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def max_profit(prices, k) do
        n = length(prices)
        if n < 2, do: 0
        k = min(k, div(n, 2))
        buy = for _ <- 1..n, do: for _ <- 1..k + 1, do: 0
        sell = for _ <- 1..n, do: for _ <- 1..k + 1, do: 0
        for i <- 1..n - 1 do
            for j <- 1..k do
                buy = update_in(buy, [i, j], fn x -> max(x, Enum.at(sell, i - 1) |> Enum.at(j - 1) - Enum.at(prices, i)) end)
                sell = update_in(sell, [i, j], fn x -> max(x, Enum.at(buy, i - 1) |> Enum.at(j) + Enum.at(prices, i)) end)
            end
        end
        Enum.at(Enum.at(sell, n - 1), k)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n * k), where n is the number of days and k is the number of transactions. This is because we need to iterate over each day and each transaction to calculate the maximum profit.

- **Space Complexity:** The space complexity of the solution is O(n * k), where n is the number of days and k is the number of transactions. This is because we need to store the maximum profit after each transaction in a 2D array.

</div>
</details>
