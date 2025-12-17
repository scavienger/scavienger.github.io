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
      cpp: "class Solution {\n    public:\n        int maxProfit(vector<int>& prices,\
        \ int k) {\n            int n = prices.size();\n            if (n < 2) return\
        \ 0;\n            if (k > n / 2) k = n / 2;\n            vector<vector<int>>\
        \ buy(k + 1, vector<int>(n, 0));\n            vector<vector<int>> sell(k + 1,\
        \ vector<int>(n, 0));\n            for (int i = 1; i <= k; i++) {\n        \
        \        int maxDiff = -prices[0];\n                for (int j = 1; j < n; j++)\
        \ {\n                    buy[i][j] = max(buy[i][j - 1], sell[i - 1][j - 1] -\
        \ prices[j]);\n                    sell[i][j] = max(sell[i][j - 1], buy[i][j\
        \ - 1] + prices[j]);\n                    maxDiff = max(maxDiff, sell[i - 1][j\
        \ - 1] - prices[j]);\n                }\n            }\n            return sell[k][n\
        \ - 1];\n        }\n    };"
      java: "class Solution {\npublic int maxProfit(int[] prices, int k) {\n    int\
        \ n = prices.length;\n    if (n < 2) return 0;\n    if (k > n / 2) k = n / 2;\n\
        \    int[][] buy = new int[k + 1][n];\n    int[][] sell = new int[k + 1][n];\n\
        \    for (int i = 1; i <= k; i++) {\n        int maxDiff = -prices[0];\n   \
        \     for (int j = 1; j < n; j++) {\n            buy[i][j] = Math.max(buy[i][j\
        \ - 1], sell[i - 1][j - 1] - prices[j]);\n            sell[i][j] = Math.max(sell[i][j\
        \ - 1], buy[i][j - 1] + prices[j]);\n            maxDiff = Math.max(maxDiff,\
        \ sell[i - 1][j - 1] - prices[j]);\n        }\n    }\n    return sell[k][n -\
        \ 1];\n}\n};"
      python: "class Solution:\ndef maxProfit(self, prices: List[int], k: int) -> int:\n\
        \    n = len(prices)\n    if n < 2: return 0\n    if k > n // 2: k = n // 2\n\
        \    buy = [[0] * n for _ in range(k + 1)]\n    sell = [[0] * n for _ in range(k\
        \ + 1)]\n    for i in range(1, k + 1):\n        max_diff = -prices[0]\n    \
        \    for j in range(1, n):\n            buy[i][j] = max(buy[i][j - 1], sell[i\
        \ - 1][j - 1] - prices[j])\n            sell[i][j] = max(sell[i][j - 1], buy[i][j\
        \ - 1] + prices[j])\n            max_diff = max(max_diff, sell[i - 1][j - 1]\
        \ - prices[j])\n    return sell[k][n - 1]"
      python3: "class Solution:\ndef maxProfit(self, prices: List[int], k: int) -> int:\n\
        \    n = len(prices)\n    if n < 2: return 0\n    if k > n // 2: k = n // 2\n\
        \    buy = [[0] * n for _ in range(k + 1)]\n    sell = [[0] * n for _ in range(k\
        \ + 1)]\n    for i in range(1, k + 1):\n        max_diff = -prices[0]\n    \
        \    for j in range(1, n):\n            buy[i][j] = max(buy[i][j - 1], sell[i\
        \ - 1][j - 1] - prices[j])\n            sell[i][j] = max(sell[i][j - 1], buy[i][j\
        \ - 1] + prices[j])\n            max_diff = max(max_diff, sell[i - 1][j - 1]\
        \ - prices[j])\n    return sell[k][n - 1]"
      c: "#include <stdio.h>\n    #include <stdlib.h>\n    int maxProfit(int* prices,\
        \ int pricesSize, int k) {\n        if (pricesSize < 2) return 0;\n        if\
        \ (k > pricesSize / 2) k = pricesSize / 2;\n        int** buy = (int**)malloc((k\
        \ + 1) * sizeof(int*));\n        int** sell = (int**)malloc((k + 1) * sizeof(int*));\n\
        \        for (int i = 0; i <= k; i++) {\n            buy[i] = (int*)malloc(pricesSize\
        \ * sizeof(int));\n            sell[i] = (int*)malloc(pricesSize * sizeof(int));\n\
        \        }\n        for (int i = 1; i <= k; i++) {\n            int max_diff\
        \ = -prices[0];\n            for (int j = 1; j < pricesSize; j++) {\n      \
        \          buy[i][j] = (buy[i][j - 1] > sell[i - 1][j - 1] - prices[j]) ? buy[i][j\
        \ - 1] : sell[i - 1][j - 1] - prices[j];\n                sell[i][j] = (sell[i][j\
        \ - 1] > buy[i][j - 1] + prices[j]) ? sell[i][j - 1] : buy[i][j - 1] + prices[j];\n\
        \                max_diff = (max_diff > sell[i - 1][j - 1] - prices[j]) ? max_diff\
        \ : sell[i - 1][j - 1] - prices[j];\n            }\n        }\n        int result\
        \ = sell[k][pricesSize - 1];\n        for (int i = 0; i <= k; i++) {\n     \
        \       free(buy[i]);\n            free(sell[i]);\n        }\n        free(buy);\n\
        \        free(sell);\n        return result;\n    }"
      csharp: "public class Solution {\npublic int MaxProfit(int[] prices, int k) {\n\
        \    int n = prices.Length;\n    if (n < 2) return 0;\n    if (k > n / 2) k\
        \ = n / 2;\n    int[][] buy = new int[k + 1][];\n    int[][] sell = new int[k\
        \ + 1][];\n    for (int i = 0; i <= k; i++) {\n        buy[i] = new int[n];\n\
        \        sell[i] = new int[n];\n    }\n    for (int i = 1; i <= k; i++) {\n\
        \        int maxDiff = -prices[0];\n        for (int j = 1; j < n; j++) {\n\
        \            buy[i][j] = Math.Max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j]);\n\
        \            sell[i][j] = Math.Max(sell[i][j - 1], buy[i][j - 1] + prices[j]);\n\
        \            maxDiff = Math.Max(maxDiff, sell[i - 1][j - 1] - prices[j]);\n\
        \        }\n    }\n    return sell[k][n - 1];\n}\n};"
      javascript: "var maxProfit = function(prices, k) {\nlet n = prices.length;\nif\
        \ (n < 2) return 0;\nif (k > n / 2) k = Math.floor(n / 2);\nlet buy = Array(k\
        \ + 1).fill(0).map(() => Array(n).fill(0));\nlet sell = Array(k + 1).fill(0).map(()\
        \ => Array(n).fill(0));\nfor (let i = 1; i <= k; i++) {\n    let maxDiff = -prices[0];\n\
        \    for (let j = 1; j < n; j++) {\n        buy[i][j] = Math.max(buy[i][j -\
        \ 1], sell[i - 1][j - 1] - prices[j]);\n        sell[i][j] = Math.max(sell[i][j\
        \ - 1], buy[i][j - 1] + prices[j]);\n        maxDiff = Math.max(maxDiff, sell[i\
        \ - 1][j - 1] - prices[j]);\n    }\n}\nreturn sell[k][n - 1];\n};"
      typescript: "function maxProfit(prices: number[], k: number): number {\nlet n\
        \ = prices.length;\nif (n < 2) return 0;\nif (k > n / 2) k = Math.floor(n /\
        \ 2);\nlet buy: number[][] = Array(k + 1).fill(0).map(() => Array(n).fill(0));\n\
        let sell: number[][] = Array(k + 1).fill(0).map(() => Array(n).fill(0));\nfor\
        \ (let i = 1; i <= k; i++) {\n    let maxDiff = -prices[0];\n    for (let j\
        \ = 1; j < n; j++) {\n        buy[i][j] = Math.max(buy[i][j - 1], sell[i - 1][j\
        \ - 1] - prices[j]);\n        sell[i][j] = Math.max(sell[i][j - 1], buy[i][j\
        \ - 1] + prices[j]);\n        maxDiff = Math.max(maxDiff, sell[i - 1][j - 1]\
        \ - prices[j]);\n    }\n}\nreturn sell[k][n - 1];\n};"
      php: "class Solution {\nfunction maxProfit($prices, $k) {\n    $n = count($prices);\n\
        \    if ($n < 2) return 0;\n    if ($k > $n / 2) $k = floor($n / 2);\n    $buy\
        \ = array_fill(0, $k + 1, array_fill(0, $n, 0));\n    $sell = array_fill(0,\
        \ $k + 1, array_fill(0, $n, 0));\n    for ($i = 1; $i <= $k; $i++) {\n     \
        \   $maxDiff = -$prices[0];\n        for ($j = 1; $j < $n; $j++) {\n       \
        \     $buy[$i][$j] = max($buy[$i][$j - 1], $sell[$i - 1][$j - 1] - $prices[$j]);\n\
        \            $sell[$i][$j] = max($sell[$i][$j - 1], $buy[$i][$j - 1] + $prices[$j]);\n\
        \            $maxDiff = max($maxDiff, $sell[$i - 1][$j - 1] - $prices[$j]);\n\
        \        }\n    }\n    return $sell[$k][$n - 1];\n}\n};"
      swift: "class Solution {\nfunc maxProfit(_ prices: [Int], _ k: Int) -> Int {\n\
        \    let n = prices.count\n    if n < 2 { return 0 }\n    if k > n / 2 { return\
        \ maxProfit(prices, k: n / 2) }\n    var buy = Array(repeating: Array(repeating:\
        \ 0, count: n), count: k + 1)\n    var sell = Array(repeating: Array(repeating:\
        \ 0, count: n), count: k + 1)\n    for i in 1...k + 1 {\n        var maxDiff\
        \ = -prices[0]\n        for j in 1..<n {\n            buy[i][j] = max(buy[i][j\
        \ - 1], sell[i - 1][j - 1] - prices[j])\n            sell[i][j] = max(sell[i][j\
        \ - 1], buy[i][j - 1] + prices[j])\n            maxDiff = max(maxDiff, sell[i\
        \ - 1][j - 1] - prices[j])\n        }\n    }\n    return sell[k][n - 1]\n}\n\
        };"
      kotlin: "class Solution {\nfun maxProfit(prices: IntArray, k: Int): Int {\n  \
        \  val n = prices.size\n    if (n < 2) return 0\n    if (k > n / 2) return maxProfit(prices,\
        \ n / 2)\n    val buy = Array(k + 1) { IntArray(n) }\n    val sell = Array(k\
        \ + 1) { IntArray(n) }\n    for (i in 1..k) {\n        var maxDiff = -prices[0]\n\
        \        for (j in 1 until n) {\n            buy[i][j] = maxOf(buy[i][j - 1],\
        \ sell[i - 1][j - 1] - prices[j])\n            sell[i][j] = maxOf(sell[i][j\
        \ - 1], buy[i][j - 1] + prices[j])\n            maxDiff = maxOf(maxDiff, sell[i\
        \ - 1][j - 1] - prices[j])\n        }\n    }\n    return sell[k][n - 1]\n}\n\
        };"
      dart: "class Solution {\nint maxProfit(List<int> prices, int k) {\n    int n =\
        \ prices.length;\n    if (n < 2) return 0;\n    if (k > n / 2) k = (n / 2).floor();\n\
        \    List<List<int>> buy = List.generate(k + 1, (i) => List.generate(n, (j)\
        \ => 0));\n    List<List<int>> sell = List.generate(k + 1, (i) => List.generate(n,\
        \ (j) => 0));\n    for (int i = 1; i <= k; i++) {\n        int maxDiff = -prices[0];\n\
        \        for (int j = 1; j < n; j++) {\n            buy[i][j] = max(buy[i][j\
        \ - 1], sell[i - 1][j - 1] - prices[j]);\n            sell[i][j] = max(sell[i][j\
        \ - 1], buy[i][j - 1] + prices[j]);\n            maxDiff = max(maxDiff, sell[i\
        \ - 1][j - 1] - prices[j]);\n        }\n    }\n    return sell[k][n - 1];\n\
        }\n};"
      go: "func maxProfit(prices []int, k int) int {\nn := len(prices)\nif n < 2 {\n\
        \    return 0\n}\nif k > n/2 {\n    k = n / 2\n}\nbuy := make([][]int, k+1)\n\
        sell := make([][]int, k+1)\nfor i := range buy {\n    buy[i] = make([]int, n)\n\
        \    sell[i] = make([]int, n)\n}\nfor i := 1; i <= k; i++ {\n    maxDiff :=\
        \ -prices[0]\n    for j := 1; j < n; j++ {\n        buy[i][j] = max(buy[i][j-1],\
        \ sell[i-1][j-1]-prices[j])\n        sell[i][j] = max(sell[i][j-1], buy[i][j-1]+prices[j])\n\
        \        maxDiff = max(maxDiff, sell[i-1][j-1]-prices[j])\n    }\n}\nreturn\
        \ sell[k][n-1]\n};\nfunc max(a, b int) int {\nif a > b {\n    return a\n}\n\
        return b\n};"
      ruby: "def max_profit(prices, k)\nn = prices.size\nreturn 0 if n < 2\nk = n /\
        \ 2 if k > n / 2\nbuy = Array.new(k + 1) { Array.new(n, 0) }\nsell = Array.new(k\
        \ + 1) { Array.new(n, 0) }\n(1..k).each do |i|\n    max_diff = -prices[0]\n\
        \    (1...n).each do |j|\n        buy[i][j] = [buy[i][j - 1], sell[i - 1][j\
        \ - 1] - prices[j]].max\n        sell[i][j] = [sell[i][j - 1], buy[i][j - 1]\
        \ + prices[j]].max\n        max_diff = [max_diff, sell[i - 1][j - 1] - prices[j]].max\n\
        \    end\nend\nsell[k][n - 1]\nend;"
      scala: "object Solution {\ndef maxProfit(prices: Array[Int], k: Int): Int = {\n\
        \    val n = prices.length\n    if (n < 2) return 0\n    if (k > n / 2) return\
        \ maxProfit(prices, n / 2)\n    val buy = Array.ofDim[Int](k + 1, n)\n    val\
        \ sell = Array.ofDim[Int](k + 1, n)\n    for (i <- 1 to k) {\n        var maxDiff\
        \ = -prices(0)\n        for (j <- 1 until n) {\n            buy(i)(j) = math.max(buy(i)(j\
        \ - 1), sell(i - 1)(j - 1) - prices(j))\n            sell(i)(j) = math.max(sell(i)(j\
        \ - 1), buy(i)(j - 1) + prices(j))\n            maxDiff = math.max(maxDiff,\
        \ sell(i - 1)(j - 1) - prices(j))\n        }\n    }\n    sell(k)(n - 1)\n}\n\
        };"
      rust: "impl Solution {\npub fn max_profit(prices: Vec<i32>, k: i32) -> i32 {\n\
        \    let n = prices.len();\n    if n < 2 {\n        return 0;\n    }\n    if\
        \ k as usize > n / 2 {\n        return Solution::max_profit(prices, (n as i32)\
        \ / 2);\n    }\n    let mut buy = vec![vec![0; n]; (k + 1) as usize];\n    let\
        \ mut sell = vec![vec![0; n]; (k + 1) as usize];\n    for i in 1..=(k as usize)\
        \ {\n        let mut max_diff = -prices[0];\n        for j in 1..n {\n     \
        \       buy[i][j] = std::cmp::max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j]);\n\
        \            sell[i][j] = std::cmp::max(sell[i][j - 1], buy[i][j - 1] + prices[j]);\n\
        \            max_diff = std::cmp::max(max_diff, sell[i - 1][j - 1] - prices[j]);\n\
        \        }\n    }\n    sell[k as usize][n - 1]\n}\n};"
      racket: "#lang racket\n    (define (max-profit prices k)\n        (let* ((n (length\
        \ prices))\n               (k (if (> k (/ n 2)) (/ n 2) k)))\n             \
        \ (define buy (make-vector (add1 k) (make-vector n 0)))\n              (define\
        \ sell (make-vector (add1 k) (make-vector n 0)))\n              (do ((i 1 (add1\
        \ i)))\n                  ((> i k))\n                (do ((j 1 (add1 j)))\n\
        \                    ((= j n))\n                  (vector-set! buy i j (max\
        \ (vector-ref buy i (sub1 j)) (- (vector-ref sell (sub1 i) (sub1 j)) (list-ref\
        \ prices j))))\n                  (vector-set! sell i j (max (vector-ref sell\
        \ i (sub1 j)) (+ (vector-ref buy i (sub1 j)) (list-ref prices j))))))\n    \
        \          (vector-ref sell k (sub1 n))))"
      erlang: "-module(solution).\n    -export([max_profit/2]).\n    max_profit(Prices,\
        \ K) ->\n        N = length(Prices),\n        if N < 2 -> 0;\n            true\
        \ -> \n                K1 = if K > N div 2 -> N div 2; true -> K end,\n    \
        \            Buy = array:new([{size, K1 + 1}, {default, array:new([{size, N},\
        \ {default, 0}])}]),\n                Sell = array:new([{size, K1 + 1}, {default,\
        \ array:new([{size, N}, {default, 0}])}]),\n                max_profit(Prices,\
        \ K1, Buy, Sell, 1, 1, -hd(Prices)).\n    max_profit([_|_], K, Buy, Sell, K,\
        \ N, _) when K > K1 -> array:get(K, Sell, N - 1);\n    max_profit(Prices, K,\
        \ Buy, Sell, K, N, MaxDiff) ->\n        [P|Ps] = Prices,\n        Buy1 = array:set(K,\
        \ array:set(N - 1, max(array:get(K, Buy, N - 2), array:get(K - 1, Sell, N -\
        \ 2) - P), array:get(K, Buy, N - 1)), Buy),\n        Sell1 = array:set(K, array:set(N\
        \ - 1, max(array:get(K, Sell, N - 2), array:get(K, Buy1, N - 1) + P), array:get(K,\
        \ Sell, N - 1)), Sell),\n        MaxDiff1 = max(MaxDiff, array:get(K - 1, Sell,\
        \ N - 2) - P),\n        max_profit(Ps, K, Buy1, Sell1, K, N - 1, MaxDiff1)."
      elixir: "defmodule Solution do\ndef max_profit(prices, k) do\n    n = length(prices)\n\
        \    if n < 2, do: 0\n    k = if k > div(n, 2), do: div(n, 2), else: k\n   \
        \ buy = Array.new(k + 1, fn -> Array.new(n, 0) end)\n    sell = Array.new(k\
        \ + 1, fn -> Array.new(n, 0) end)\n    max_profit(prices, k, buy, sell, 1, 1,\
        \ -Enum.at(prices, 0))\nend\ndefp max_profit([_|_], k, buy, sell, k, n, _) when\
        \ k > k do\n    Array.get(sell, k, n - 1)\nend\ndefp max_profit(prices, k, buy,\
        \ sell, k, n, max_diff) do\n    [p|ps] = prices\n    buy1 = Array.put(buy, k,\
        \ Array.put(Array.get(buy, k), n - 1, max(Array.get(Array.get(buy, k), n - 2),\
        \ Array.get(Array.get(sell, k - 1), n - 2) - p)))\n    sell1 = Array.put(sell,\
        \ k, Array.put(Array.get(sell, k), n - 1, max(Array.get(Array.get(sell, k),\
        \ n - 2), Array.get(Array.get(buy1, k), n - 1) + p)))\n    max_diff1 = max(max_diff,\
        \ Array.get(Array.get(sell, k - 1), n - 2) - p)\n    max_profit(ps, k, buy1,\
        \ sell1, k, n - 1, max_diff1)\nend\nend"
    approach: The problem can be solved using dynamic programming. We need to keep track
      of the maximum profit that can be achieved with a given number of transactions
      and the current state of the transaction (either running or completed). The key
      intuition is to consider all possible transactions and choose the one that maximizes
      the profit. We can use a 2D array to store the maximum profit for each state and
      transaction count. The transition from one state to another can be done by either
      starting a new transaction or completing the current one. The maximum profit can
      be calculated by considering the maximum profit of the previous state and the
      current price.
    time_complexity: The time complexity of the solution is O(n * k) where n is the
      number of days and k is the number of transactions. This is because we need to
      iterate over the prices array and for each price, we need to consider all possible
      transactions.
    space_complexity: The space complexity of the solution is O(n * k) where n is the
      number of days and k is the number of transactions. This is because we need to
      store the maximum profit for each state and transaction count in a 2D array.
    elapsed_time: 12.324929475784302
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-17 01:07:43 '
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
  <small class="solution-timestamp">(2025-12-17 01:07:43 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. We need to keep track of the maximum profit that can be achieved with a given number of transactions and the current state of the transaction (either running or completed). The key intuition is to consider all possible transactions and choose the one that maximizes the profit. We can use a 2D array to store the maximum profit for each state and transaction count. The transition from one state to another can be done by either starting a new transaction or completing the current one. The maximum profit can be calculated by considering the maximum profit of the previous state and the current price.

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
            if (k > n / 2) k = n / 2;
            vector<vector<int>> buy(k + 1, vector<int>(n, 0));
            vector<vector<int>> sell(k + 1, vector<int>(n, 0));
            for (int i = 1; i <= k; i++) {
                int maxDiff = -prices[0];
                for (int j = 1; j < n; j++) {
                    buy[i][j] = max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j]);
                    sell[i][j] = max(sell[i][j - 1], buy[i][j - 1] + prices[j]);
                    maxDiff = max(maxDiff, sell[i - 1][j - 1] - prices[j]);
                }
            }
            return sell[k][n - 1];
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
    if (k > n / 2) k = n / 2;
    int[][] buy = new int[k + 1][n];
    int[][] sell = new int[k + 1][n];
    for (int i = 1; i <= k; i++) {
        int maxDiff = -prices[0];
        for (int j = 1; j < n; j++) {
            buy[i][j] = Math.max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j]);
            sell[i][j] = Math.max(sell[i][j - 1], buy[i][j - 1] + prices[j]);
            maxDiff = Math.max(maxDiff, sell[i - 1][j - 1] - prices[j]);
        }
    }
    return sell[k][n - 1];
}
};
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
    if k > n // 2: k = n // 2
    buy = [[0] * n for _ in range(k + 1)]
    sell = [[0] * n for _ in range(k + 1)]
    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            buy[i][j] = max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j])
            sell[i][j] = max(sell[i][j - 1], buy[i][j - 1] + prices[j])
            max_diff = max(max_diff, sell[i - 1][j - 1] - prices[j])
    return sell[k][n - 1]
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
    if k > n // 2: k = n // 2
    buy = [[0] * n for _ in range(k + 1)]
    sell = [[0] * n for _ in range(k + 1)]
    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            buy[i][j] = max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j])
            sell[i][j] = max(sell[i][j - 1], buy[i][j - 1] + prices[j])
            max_diff = max(max_diff, sell[i - 1][j - 1] - prices[j])
    return sell[k][n - 1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
    #include <stdlib.h>
    int maxProfit(int* prices, int pricesSize, int k) {
        if (pricesSize < 2) return 0;
        if (k > pricesSize / 2) k = pricesSize / 2;
        int** buy = (int**)malloc((k + 1) * sizeof(int*));
        int** sell = (int**)malloc((k + 1) * sizeof(int*));
        for (int i = 0; i <= k; i++) {
            buy[i] = (int*)malloc(pricesSize * sizeof(int));
            sell[i] = (int*)malloc(pricesSize * sizeof(int));
        }
        for (int i = 1; i <= k; i++) {
            int max_diff = -prices[0];
            for (int j = 1; j < pricesSize; j++) {
                buy[i][j] = (buy[i][j - 1] > sell[i - 1][j - 1] - prices[j]) ? buy[i][j - 1] : sell[i - 1][j - 1] - prices[j];
                sell[i][j] = (sell[i][j - 1] > buy[i][j - 1] + prices[j]) ? sell[i][j - 1] : buy[i][j - 1] + prices[j];
                max_diff = (max_diff > sell[i - 1][j - 1] - prices[j]) ? max_diff : sell[i - 1][j - 1] - prices[j];
            }
        }
        int result = sell[k][pricesSize - 1];
        for (int i = 0; i <= k; i++) {
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
    if (k > n / 2) k = n / 2;
    int[][] buy = new int[k + 1][];
    int[][] sell = new int[k + 1][];
    for (int i = 0; i <= k; i++) {
        buy[i] = new int[n];
        sell[i] = new int[n];
    }
    for (int i = 1; i <= k; i++) {
        int maxDiff = -prices[0];
        for (int j = 1; j < n; j++) {
            buy[i][j] = Math.Max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j]);
            sell[i][j] = Math.Max(sell[i][j - 1], buy[i][j - 1] + prices[j]);
            maxDiff = Math.Max(maxDiff, sell[i - 1][j - 1] - prices[j]);
        }
    }
    return sell[k][n - 1];
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxProfit = function(prices, k) {
let n = prices.length;
if (n < 2) return 0;
if (k > n / 2) k = Math.floor(n / 2);
let buy = Array(k + 1).fill(0).map(() => Array(n).fill(0));
let sell = Array(k + 1).fill(0).map(() => Array(n).fill(0));
for (let i = 1; i <= k; i++) {
    let maxDiff = -prices[0];
    for (let j = 1; j < n; j++) {
        buy[i][j] = Math.max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j]);
        sell[i][j] = Math.max(sell[i][j - 1], buy[i][j - 1] + prices[j]);
        maxDiff = Math.max(maxDiff, sell[i - 1][j - 1] - prices[j]);
    }
}
return sell[k][n - 1];
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
if (k > n / 2) k = Math.floor(n / 2);
let buy: number[][] = Array(k + 1).fill(0).map(() => Array(n).fill(0));
let sell: number[][] = Array(k + 1).fill(0).map(() => Array(n).fill(0));
for (let i = 1; i <= k; i++) {
    let maxDiff = -prices[0];
    for (let j = 1; j < n; j++) {
        buy[i][j] = Math.max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j]);
        sell[i][j] = Math.max(sell[i][j - 1], buy[i][j - 1] + prices[j]);
        maxDiff = Math.max(maxDiff, sell[i - 1][j - 1] - prices[j]);
    }
}
return sell[k][n - 1];
};
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
    if ($k > $n / 2) $k = floor($n / 2);
    $buy = array_fill(0, $k + 1, array_fill(0, $n, 0));
    $sell = array_fill(0, $k + 1, array_fill(0, $n, 0));
    for ($i = 1; $i <= $k; $i++) {
        $maxDiff = -$prices[0];
        for ($j = 1; $j < $n; $j++) {
            $buy[$i][$j] = max($buy[$i][$j - 1], $sell[$i - 1][$j - 1] - $prices[$j]);
            $sell[$i][$j] = max($sell[$i][$j - 1], $buy[$i][$j - 1] + $prices[$j]);
            $maxDiff = max($maxDiff, $sell[$i - 1][$j - 1] - $prices[$j]);
        }
    }
    return $sell[$k][$n - 1];
}
};
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
    if k > n / 2 { return maxProfit(prices, k: n / 2) }
    var buy = Array(repeating: Array(repeating: 0, count: n), count: k + 1)
    var sell = Array(repeating: Array(repeating: 0, count: n), count: k + 1)
    for i in 1...k + 1 {
        var maxDiff = -prices[0]
        for j in 1..<n {
            buy[i][j] = max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j])
            sell[i][j] = max(sell[i][j - 1], buy[i][j - 1] + prices[j])
            maxDiff = max(maxDiff, sell[i - 1][j - 1] - prices[j])
        }
    }
    return sell[k][n - 1]
}
};
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
    if (k > n / 2) return maxProfit(prices, n / 2)
    val buy = Array(k + 1) { IntArray(n) }
    val sell = Array(k + 1) { IntArray(n) }
    for (i in 1..k) {
        var maxDiff = -prices[0]
        for (j in 1 until n) {
            buy[i][j] = maxOf(buy[i][j - 1], sell[i - 1][j - 1] - prices[j])
            sell[i][j] = maxOf(sell[i][j - 1], buy[i][j - 1] + prices[j])
            maxDiff = maxOf(maxDiff, sell[i - 1][j - 1] - prices[j])
        }
    }
    return sell[k][n - 1]
}
};
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
    if (k > n / 2) k = (n / 2).floor();
    List<List<int>> buy = List.generate(k + 1, (i) => List.generate(n, (j) => 0));
    List<List<int>> sell = List.generate(k + 1, (i) => List.generate(n, (j) => 0));
    for (int i = 1; i <= k; i++) {
        int maxDiff = -prices[0];
        for (int j = 1; j < n; j++) {
            buy[i][j] = max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j]);
            sell[i][j] = max(sell[i][j - 1], buy[i][j - 1] + prices[j]);
            maxDiff = max(maxDiff, sell[i - 1][j - 1] - prices[j]);
        }
    }
    return sell[k][n - 1];
}
};
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
if k > n/2 {
    k = n / 2
}
buy := make([][]int, k+1)
sell := make([][]int, k+1)
for i := range buy {
    buy[i] = make([]int, n)
    sell[i] = make([]int, n)
}
for i := 1; i <= k; i++ {
    maxDiff := -prices[0]
    for j := 1; j < n; j++ {
        buy[i][j] = max(buy[i][j-1], sell[i-1][j-1]-prices[j])
        sell[i][j] = max(sell[i][j-1], buy[i][j-1]+prices[j])
        maxDiff = max(maxDiff, sell[i-1][j-1]-prices[j])
    }
}
return sell[k][n-1]
};
func max(a, b int) int {
if a > b {
    return a
}
return b
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_profit(prices, k)
n = prices.size
return 0 if n < 2
k = n / 2 if k > n / 2
buy = Array.new(k + 1) { Array.new(n, 0) }
sell = Array.new(k + 1) { Array.new(n, 0) }
(1..k).each do |i|
    max_diff = -prices[0]
    (1...n).each do |j|
        buy[i][j] = [buy[i][j - 1], sell[i - 1][j - 1] - prices[j]].max
        sell[i][j] = [sell[i][j - 1], buy[i][j - 1] + prices[j]].max
        max_diff = [max_diff, sell[i - 1][j - 1] - prices[j]].max
    end
end
sell[k][n - 1]
end;
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
    if (k > n / 2) return maxProfit(prices, n / 2)
    val buy = Array.ofDim[Int](k + 1, n)
    val sell = Array.ofDim[Int](k + 1, n)
    for (i <- 1 to k) {
        var maxDiff = -prices(0)
        for (j <- 1 until n) {
            buy(i)(j) = math.max(buy(i)(j - 1), sell(i - 1)(j - 1) - prices(j))
            sell(i)(j) = math.max(sell(i)(j - 1), buy(i)(j - 1) + prices(j))
            maxDiff = math.max(maxDiff, sell(i - 1)(j - 1) - prices(j))
        }
    }
    sell(k)(n - 1)
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
pub fn max_profit(prices: Vec<i32>, k: i32) -> i32 {
    let n = prices.len();
    if n < 2 {
        return 0;
    }
    if k as usize > n / 2 {
        return Solution::max_profit(prices, (n as i32) / 2);
    }
    let mut buy = vec![vec![0; n]; (k + 1) as usize];
    let mut sell = vec![vec![0; n]; (k + 1) as usize];
    for i in 1..=(k as usize) {
        let mut max_diff = -prices[0];
        for j in 1..n {
            buy[i][j] = std::cmp::max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j]);
            sell[i][j] = std::cmp::max(sell[i][j - 1], buy[i][j - 1] + prices[j]);
            max_diff = std::cmp::max(max_diff, sell[i - 1][j - 1] - prices[j]);
        }
    }
    sell[k as usize][n - 1]
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
    (define (max-profit prices k)
        (let* ((n (length prices))
               (k (if (> k (/ n 2)) (/ n 2) k)))
              (define buy (make-vector (add1 k) (make-vector n 0)))
              (define sell (make-vector (add1 k) (make-vector n 0)))
              (do ((i 1 (add1 i)))
                  ((> i k))
                (do ((j 1 (add1 j)))
                    ((= j n))
                  (vector-set! buy i j (max (vector-ref buy i (sub1 j)) (- (vector-ref sell (sub1 i) (sub1 j)) (list-ref prices j))))
                  (vector-set! sell i j (max (vector-ref sell i (sub1 j)) (+ (vector-ref buy i (sub1 j)) (list-ref prices j))))))
              (vector-ref sell k (sub1 n))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
    -export([max_profit/2]).
    max_profit(Prices, K) ->
        N = length(Prices),
        if N < 2 -> 0;
            true -> 
                K1 = if K > N div 2 -> N div 2; true -> K end,
                Buy = array:new([{size, K1 + 1}, {default, array:new([{size, N}, {default, 0}])}]),
                Sell = array:new([{size, K1 + 1}, {default, array:new([{size, N}, {default, 0}])}]),
                max_profit(Prices, K1, Buy, Sell, 1, 1, -hd(Prices)).
    max_profit([_|_], K, Buy, Sell, K, N, _) when K > K1 -> array:get(K, Sell, N - 1);
    max_profit(Prices, K, Buy, Sell, K, N, MaxDiff) ->
        [P|Ps] = Prices,
        Buy1 = array:set(K, array:set(N - 1, max(array:get(K, Buy, N - 2), array:get(K - 1, Sell, N - 2) - P), array:get(K, Buy, N - 1)), Buy),
        Sell1 = array:set(K, array:set(N - 1, max(array:get(K, Sell, N - 2), array:get(K, Buy1, N - 1) + P), array:get(K, Sell, N - 1)), Sell),
        MaxDiff1 = max(MaxDiff, array:get(K - 1, Sell, N - 2) - P),
        max_profit(Ps, K, Buy1, Sell1, K, N - 1, MaxDiff1).
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
    k = if k > div(n, 2), do: div(n, 2), else: k
    buy = Array.new(k + 1, fn -> Array.new(n, 0) end)
    sell = Array.new(k + 1, fn -> Array.new(n, 0) end)
    max_profit(prices, k, buy, sell, 1, 1, -Enum.at(prices, 0))
end
defp max_profit([_|_], k, buy, sell, k, n, _) when k > k do
    Array.get(sell, k, n - 1)
end
defp max_profit(prices, k, buy, sell, k, n, max_diff) do
    [p|ps] = prices
    buy1 = Array.put(buy, k, Array.put(Array.get(buy, k), n - 1, max(Array.get(Array.get(buy, k), n - 2), Array.get(Array.get(sell, k - 1), n - 2) - p)))
    sell1 = Array.put(sell, k, Array.put(Array.get(sell, k), n - 1, max(Array.get(Array.get(sell, k), n - 2), Array.get(Array.get(buy1, k), n - 1) + p)))
    max_diff1 = max(max_diff, Array.get(Array.get(sell, k - 1), n - 2) - p)
    max_profit(ps, k, buy1, sell1, k, n - 1, max_diff1)
end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n * k) where n is the number of days and k is the number of transactions. This is because we need to iterate over the prices array and for each price, we need to consider all possible transactions.

- **Space Complexity:** The space complexity of the solution is O(n * k) where n is the number of days and k is the number of transactions. This is because we need to store the maximum profit for each state and transaction count in a 2D array.

</div>
</details>
