---
layout: post
title: "Number of Smooth Descent Periods of a Stock"
date: 2025-12-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long getDescentPeriods(std::vector<int>&\
        \ prices) {\n        int n = prices.size();\n        long long totalDescentPeriods\
        \ = 0;\n        int currentLength = 0;\n\n        for (int i = 0; i < n; i++)\
        \ {\n            if (i == 0 || prices[i] != prices[i-1] - 1) {\n           \
        \     currentLength = 1;\n            } else {\n                currentLength++;\n\
        \            }\n            totalDescentPeriods += currentLength;\n        }\n\
        \n        return totalDescentPeriods;\n    }\n};"
      java: "class Solution {\n    public long getDescentPeriods(int[] prices) {\n \
        \       int n = prices.length;\n        long totalDescentPeriods = 0;\n    \
        \    int currentLength = 0;\n\n        for (int i = 0; i < n; i++) {\n     \
        \       if (i == 0 || prices[i] != prices[i-1] - 1) {\n                currentLength\
        \ = 1;\n            } else {\n                currentLength++;\n           \
        \ }\n            totalDescentPeriods += currentLength;\n        }\n\n      \
        \  return totalDescentPeriods;\n    }\n}"
      python: "class Solution:\n    def getDescentPeriods(self, prices: List[int]) ->\
        \ int:\n        n = len(prices)\n        total_descent_periods = 0\n       \
        \ current_length = 0\n\n        for i in range(n):\n            if i == 0 or\
        \ prices[i] != prices[i-1] - 1:\n                current_length = 1\n      \
        \      else:\n                current_length += 1\n            total_descent_periods\
        \ += current_length\n\n        return total_descent_periods"
      python3: "class Solution:\n    def getDescentPeriods(self, prices: List[int])\
        \ -> int:\n        n = len(prices)\n        total_descent_periods = 0\n    \
        \    current_length = 0\n\n        for i in range(n):\n            if i == 0\
        \ or prices[i] != prices[i-1] - 1:\n                current_length = 1\n   \
        \         else:\n                current_length += 1\n            total_descent_periods\
        \ += current_length\n\n        return total_descent_periods"
      c: "#include <stddef.h> // For size_t\n\nlong long getDescentPeriods(int* prices,\
        \ int pricesSize) {\n    long long totalDescentPeriods = 0;\n    int currentLength\
        \ = 0;\n\n    for (int i = 0; i < pricesSize; i++) {\n        if (i == 0 ||\
        \ prices[i] != prices[i-1] - 1) {\n            currentLength = 1;\n        }\
        \ else {\n            currentLength++;\n        }\n        totalDescentPeriods\
        \ += currentLength;\n    }\n\n    return totalDescentPeriods;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public long GetDescentPeriods(int[]\
        \ prices) {\n        int n = prices.Length;\n        long totalDescentPeriods\
        \ = 0;\n        int currentLength = 0;\n\n        for (int i = 0; i < n; i++)\
        \ {\n            if (i == 0 || prices[i] != prices[i-1] - 1) {\n           \
        \     currentLength = 1;\n            } else {\n                currentLength++;\n\
        \            }\n            totalDescentPeriods += currentLength;\n        }\n\
        \n        return totalDescentPeriods;\n    }\n}"
      javascript: "/**\n * @param {number[]} prices\n * @return {number}\n */\nvar getDescentPeriods\
        \ = function(prices) {\n    const n = prices.length;\n    let totalDescentPeriods\
        \ = 0;\n    let currentLength = 0;\n\n    for (let i = 0; i < n; i++) {\n  \
        \      if (i === 0 || prices[i] !== prices[i-1] - 1) {\n            currentLength\
        \ = 1;\n        } else {\n            currentLength++;\n        }\n        totalDescentPeriods\
        \ += currentLength;\n    }\n\n    return totalDescentPeriods;\n};"
      typescript: "function getDescentPeriods(prices: number[]): number {\n    const\
        \ n = prices.length;\n    let totalDescentPeriods: number = 0; \n    let currentLength:\
        \ number = 0;\n\n    for (let i = 0; i < n; i++) {\n        if (i === 0 || prices[i]\
        \ !== prices[i-1] - 1) {\n            currentLength = 1;\n        }\n      \
        \  else {\n            currentLength++;\n        }\n        totalDescentPeriods\
        \ += currentLength;\n    }\n\n    return totalDescentPeriods;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $prices\n     * @return\
        \ Integer\n     */\n    function getDescentPeriods($prices) {\n        $n =\
        \ count($prices);\n        $totalDescentPeriods = 0; \n        $currentLength\
        \ = 0;\n\n        for ($i = 0; $i < $n; $i++) {\n            if ($i === 0 ||\
        \ $prices[$i] !== $prices[$i-1] - 1) {\n                $currentLength = 1;\n\
        \            } else {\n                $currentLength++;\n            }\n  \
        \          $totalDescentPeriods += $currentLength;\n        }\n\n        return\
        \ $totalDescentPeriods;\n    }\n}"
      swift: "class Solution {\n    func getDescentPeriods(_ prices: [Int]) -> Int {\n\
        \        let n = prices.count\n        var totalDescentPeriods: Int = 0 \n \
        \       var currentLength: Int = 0\n\n        for i in 0..<n {\n           \
        \ if i == 0 || prices[i] != prices[i-1] - 1 {\n                currentLength\
        \ = 1\n            } else {\n                currentLength += 1\n          \
        \  }\n            totalDescentPeriods += currentLength\n        }\n\n      \
        \  return totalDescentPeriods\n    }\n}"
      kotlin: "class Solution {\n    fun getDescentPeriods(prices: IntArray): Long {\n\
        \        val n = prices.size\n        var totalDescentPeriods: Long = 0\n  \
        \      var currentLength: Int = 0\n\n        for (i in 0 until n) {\n      \
        \      if (i == 0 || prices[i] != prices[i-1] - 1) {\n                currentLength\
        \ = 1\n            } else {\n                currentLength++\n            }\n\
        \            totalDescentPeriods += currentLength\n        }\n\n        return\
        \ totalDescentPeriods\n    }\n}"
      dart: "class Solution {\n  int getDescentPeriods(List<int> prices) {\n    final\
        \ n = prices.length;\n    int totalDescentPeriods = 0; \n    int currentLength\
        \ = 0;\n\n    for (int i = 0; i < n; i++) {\n      if (i == 0 || prices[i] !=\
        \ prices[i-1] - 1) {\n        currentLength = 1;\n      }\n      else {\n  \
        \      currentLength++;\n      }\n      totalDescentPeriods += currentLength;\n\
        \    }\n\n    return totalDescentPeriods;\n  }\n}"
      go: "func getDescentPeriods(prices []int) int64 {\n    n := len(prices)\n    var\
        \ totalDescentPeriods int64 = 0\n    var currentLength int = 0\n\n    for i\
        \ := 0; i < n; i++ {\n        if i == 0 || prices[i] != prices[i-1] - 1 {\n\
        \            currentLength = 1\n        } else {\n            currentLength++\n\
        \        }\n        totalDescentPeriods += int64(currentLength)\n    }\n\n \
        \   return totalDescentPeriods\n}"
      ruby: "# @param {Integer[]} prices\n# @return {Integer}\ndef get_descent_periods(prices)\n\
        \    n = prices.length\n    total_descent_periods = 0 \n    current_length =\
        \ 0\n\n    (0...n).each do |i|\n        if i == 0 || prices[i] != prices[i-1]\
        \ - 1\n            current_length = 1\n        else\n            current_length\
        \ += 1\n        end\n        total_descent_periods += current_length\n    end\n\
        \n    return total_descent_periods\nend"
      scala: "object Solution {\n    def getDescentPeriods(prices: Array[Int]): Long\
        \ = {\n        val n = prices.length\n        var totalDescentPeriods: Long\
        \ = 0\n        var currentLength: Int = 0\n\n        for (i <- 0 until n) {\n\
        \            if (i == 0 || prices(i) != prices(i-1) - 1) {\n               \
        \ currentLength = 1\n            } else {\n                currentLength +=\
        \ 1\n            }\n            totalDescentPeriods += currentLength\n     \
        \   }\n\n        totalDescentPeriods\n    }\n}"
      rust: "impl Solution {\n    pub fn get_descent_periods(prices: Vec<i32>) -> i64\
        \ {\n        let n = prices.len();\n        let mut total_descent_periods: i64\
        \ = 0;\n        let mut current_length: i32 = 0;\n\n        for i in 0..n {\n\
        \            if i == 0 || prices[i] != prices[i-1] - 1 {\n                current_length\
        \ = 1;\n            } else {\n                current_length += 1;\n       \
        \     }\n            total_descent_periods += current_length as i64;\n     \
        \   }\n\n        total_descent_periods\n    }\n}"
      racket: "#lang racket\n\n(define/contract (get-descent-periods prices)\n  (->\
        \ (listof exact-integer?) exact-integer?)\n  (let ([n (length prices)]\n   \
        \     [prices-vec (list->vector prices)])\n    (for/fold ([total-descent-periods\
        \ 0]\n               [current-length 0])\n              ([i (in-range n)])\n\
        \      (let ([new-current-length\n             (if (or (= i 0)\n           \
        \          (not (= (vector-ref prices-vec i) (- (vector-ref prices-vec (- i\
        \ 1)) 1))))\n                 1\n                 (+ current-length 1))])\n\
        \        (values (+ total-descent-periods new-current-length)\n            \
        \    new-current-length)))))"
      erlang: "-module(solution).\n-export([get_descent_periods/1]).\n\nget_descent_periods([])\
        \ -> 0;\nget_descent_periods([H | T]) ->\n    % State: {TotalDescentPeriods,\
        \ CurrentLength, PreviousPrice}\n    % Initial state for foldl: {1, 1, H} because\
        \ [H] is always a period of length 1.\n    {Total, _Current, _Prev} = lists:foldl(\n\
        \        fun(CurrentPrice, {AccTotal, AccLength, PrevPrice}) ->\n          \
        \  NewLength =\n                if CurrentPrice == PrevPrice - 1 ->\n      \
        \              AccLength + 1;\n                true ->\n                   \
        \ 1\n                end,\n            {AccTotal + NewLength, NewLength, CurrentPrice}\n\
        \        end,\n        {1, 1, H}, % Initial state: total=1 (for H), length=1,\
        \ prev_price=H\n        T % Fold over the rest of the list\n    ),\n    Total."
      elixir: "defmodule Solution do\n  @spec get_descent_periods(prices :: [integer])\
        \ :: integer\n  def get_descent_periods(prices) do\n    Enum.reduce(prices,\
        \ {0, 0, nil}, fn current_price, {total_descent_periods, current_length, prev_price}\
        \ ->\n      new_length =\n        if is_nil(prev_price) or current_price !=\
        \ prev_price - 1 do\n          1\n        else\n          current_length + 1\n\
        \        end\n\n      {total_descent_periods + new_length, new_length, current_price}\n\
        \    end)\n    |> elem(0) # Extract the total_descent_periods\n  end\nend"
    approach: The problem asks us to count all 'smooth descent periods' in a given array
      of stock prices. A smooth descent period is a contiguous subarray where each day's
      price (after the first) is exactly 1 less than the preceding day's price. Single-day
      periods are always considered smooth descent periods. The core idea is to iterate
      through the array and keep track of the length of the current smooth descent period
      ending at the current day.
    time_complexity: The time complexity is O(N), where N is the number of days (length
      of the `prices` array). We iterate through the array once, performing constant-time
      operations for each element.
    space_complexity: The space complexity is O(1). We use a few variables to store
      the total count, the current period length, and loop indices, which consume a
      constant amount of extra space regardless of the input size.
    elapsed_time: 38.94169235229492
    model: gemini-2.5-flash
    generated_at: '2025-12-15 01:09:58 '
  - solutions:
      cpp: "class Solution {\npublic:\n    long long getDescentPeriods(vector<int>&\
        \ prices) {\n        long long ans = 0;\n        int i = 0;\n        while (i\
        \ < prices.size()) {\n            int j = i;\n            while (j + 1 < prices.size()\
        \ && prices[j] - prices[j + 1] == 1) j++;\n            int k = j - i + 1;\n\
        \            ans += 1LL * k * (k + 1) / 2;\n            i = j + 1;\n       \
        \ }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public long getDescentPeriods(int[] prices) {\n \
        \       long ans = 0;\n        int i = 0;\n        while (i < prices.length)\
        \ {\n            int j = i;\n            while (j + 1 < prices.length && prices[j]\
        \ - prices[j + 1] == 1) j++;\n            int k = j - i + 1;\n            ans\
        \ += (long) k * (k + 1) / 2;\n            i = j + 1;\n        }\n        return\
        \ ans;\n    }\n}"
      python: "class Solution:\n    def getDescentPeriods(self, prices: list[int]) ->\
        \ int:\n        ans = 0\n        i = 0\n        while i < len(prices):\n   \
        \         j = i\n            while j + 1 < len(prices) and prices[j] - prices[j\
        \ + 1] == 1: j += 1\n            k = j - i + 1\n            ans += k * (k +\
        \ 1) // 2\n            i = j + 1\n        return ans"
      python3: "class Solution:\n    def getDescentPeriods(self, prices: list[int])\
        \ -> int:\n        ans = 0\n        i = 0\n        while i < len(prices):\n\
        \            j = i\n            while j + 1 < len(prices) and prices[j] - prices[j\
        \ + 1] == 1: j += 1\n            k = j - i + 1\n            ans += k * (k +\
        \ 1) // 2\n            i = j + 1\n        return ans"
      c: "long long getDescentPeriods(int* prices, int pricesSize) {\n    long long\
        \ ans = 0;\n    int i = 0;\n    while (i < pricesSize) {\n        int j = i;\n\
        \        while (j + 1 < pricesSize && prices[j] - prices[j + 1] == 1) j++;\n\
        \        int k = j - i + 1;\n        ans += (long long)k * (k + 1) / 2;\n  \
        \      i = j + 1;\n    }\n    return ans;\n}"
      csharp: "public class Solution {\n    public long GetDescentPeriods(int[] prices)\
        \ {\n        long ans = 0;\n        int i = 0;\n        while (i < prices.Length)\
        \ {\n            int j = i;\n            while (j + 1 < prices.Length && prices[j]\
        \ - prices[j + 1] == 1) j++;\n            int k = j - i + 1;\n            ans\
        \ += (long)k * (k + 1) / 2;\n            i = j + 1;\n        }\n        return\
        \ ans;\n    }\n}"
      javascript: "var getDescentPeriods = function(prices) {\n    let ans = 0;\n  \
        \  let i = 0;\n    while (i < prices.length) {\n        let j = i;\n       \
        \ while (j + 1 < prices.length && prices[j] - prices[j + 1] == 1) j++;\n   \
        \     let k = j - i + 1;\n        ans += k * (k + 1) / 2;\n        i = j + 1;\n\
        \    }\n    return ans;\n};"
      typescript: "function getDescentPeriods(prices: number[]): number {\n    let ans:\
        \ number = 0;\n    let i: number = 0;\n    while (i < prices.length) {\n   \
        \     let j: number = i;\n        while (j + 1 < prices.length && prices[j]\
        \ - prices[j + 1] == 1) j++;\n        let k: number = j - i + 1;\n        ans\
        \ += k * (k + 1) / 2;\n        i = j + 1;\n    }\n    return ans;\n}"
      php: "class Solution {\n    function getDescentPeriods($prices) {\n        $ans\
        \ = 0;\n        $i = 0;\n        while ($i < count($prices)) {\n           \
        \ $j = $i;\n            while ($j + 1 < count($prices) && $prices[$j] - $prices[$j\
        \ + 1] == 1) $j++;\n            $k = $j - $i + 1;\n            $ans += $k *\
        \ ($k + 1) / 2;\n            $i = $j + 1;\n        }\n        return $ans;\n\
        \    }\n}"
      swift: "class Solution {\n    func getDescentPeriods(_ prices: [Int]) -> Int64\
        \ {\n        var ans: Int64 = 0\n        var i = 0\n        while i < prices.count\
        \ {\n            var j = i\n            while j + 1 < prices.count && prices[j]\
        \ - prices[j + 1] == 1 {\n                j += 1\n            }\n          \
        \  let k = j - i + 1\n            ans += Int64(k) * Int64(k + 1) / 2\n     \
        \       i = j + 1\n        }\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun getDescentPeriods(prices: IntArray): Long {\n\
        \        var ans: Long = 0\n        var i = 0\n        while (i < prices.size)\
        \ {\n            var j = i\n            while (j + 1 < prices.size && prices[j]\
        \ - prices[j + 1] == 1) j++\n            val k = j - i + 1\n            ans\
        \ += k.toLong() * (k + 1) / 2\n            i = j + 1\n        }\n        return\
        \ ans\n    }\n}"
      dart: "class Solution {\n    int getDescentPeriods(List<int> prices) {\n     \
        \   int ans = 0;\n        int i = 0;\n        while (i < prices.length) {\n\
        \            int j = i;\n            while (j + 1 < prices.length && prices[j]\
        \ - prices[j + 1] == 1) j++;\n            int k = j - i + 1;\n            ans\
        \ += k * (k + 1) ~/ 2;\n            i = j + 1;\n        }\n        return ans;\n\
        \    }\n}"
      go: "func getDescentPeriods(prices []int) int64 {\n    ans := int64(0)\n    i\
        \ := 0\n    for i < len(prices) {\n        j := i\n        for j + 1 < len(prices)\
        \ && prices[j] - prices[j + 1] == 1 {\n            j++\n        }\n        k\
        \ := j - i + 1\n        ans += int64(k) * int64(k + 1) / 2\n        i = j +\
        \ 1\n    }\n    return ans\n}"
      ruby: "def get_descent_periods(prices)\n    ans = 0\n    i = 0\n    while i <\
        \ prices.size\n        j = i\n        while j + 1 < prices.size && prices[j]\
        \ - prices[j + 1] == 1\n            j += 1\n        end\n        k = j - i +\
        \ 1\n        ans += k * (k + 1) / 2\n        i = j + 1\n    end\n    ans\nend"
      scala: "object Solution {\n    def getDescentPeriods(prices: Array[Int]): Long\
        \ = {\n        var ans: Long = 0\n        var i = 0\n        while (i < prices.length)\
        \ {\n            var j = i\n            while (j + 1 < prices.length && prices(j)\
        \ - prices(j + 1) == 1) j += 1\n            val k = j - i + 1\n            ans\
        \ += k.toLong * (k + 1) / 2\n            i = j + 1\n        }\n        ans\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn get_descent_periods(prices: Vec<i32>) -> i64\
        \ {\n        let mut ans: i64 = 0;\n        let mut i: usize = 0;\n        while\
        \ i < prices.len() {\n            let mut j: usize = i;\n            while j\
        \ + 1 < prices.len() && prices[j] - prices[j + 1] == 1 {\n                j\
        \ += 1;\n            }\n            let k: i64 = (j - i + 1) as i64;\n     \
        \       ans += k * (k + 1) / 2;\n            i = j + 1;\n        }\n       \
        \ ans\n    }\n}"
      racket: "define (get-descent-periods prices)\n    (let loop ((i 0) (ans 0))\n\
        \        (if (>= i (length prices))\n            ans\n            (let ((j (let\
        \ loop2 ((j i))\n                            (if (and (< j (sub1 (length prices)))\
        \ (= (- (list-ref prices j) (list-ref prices (add1 j))) 1))\n              \
        \                  (loop2 (add1 j))\n                                j)))))\n\
        \                (loop (add1 j) (+ ans (let ((k (- j i))) (/ (* k (add1 k))\
        \ 2))))))))"
      erlang: "get_descent_periods(Prices) ->\n    get_descent_periods(Prices, 0, 0).\n\
        get_descent_periods([_|_]=Prices, I, Ans) ->\n    get_descent_periods(Prices,\
        \ I, Ans, 0, I);\nget_descent_periods([], _, Ans, _, _) -> Ans;\nget_descent_periods([_|_]=Prices,\
        \ I, Ans, J, Start) ->\n    case length(Prices) of\n        Len when J >= Len\
        \ -> get_descent_periods(Prices, I + 1, Ans, 0, I);\n        _ ->\n        \
        \    case lists:nth(J + 1, Prices) - lists:nth(J, Prices) of\n             \
        \   1 -> get_descent_periods(Prices, I, Ans, J + 1, Start);\n              \
        \  _ -> get_descent_periods(Prices, I + 1, Ans + (J - Start + 1) * (J - Start\
        \ + 2) div 2, 0, I)\n            end."
      elixir: "def get_descent_periods(prices) do\n    get_descent_periods(prices, 0,\
        \ 0)\nend\n\ndefp get_descent_periods([], _, ans), do: ans\n\ndefp get_descent_periods([_|_]=prices,\
        \ i, ans) do\n    get_descent_periods(prices, i, ans, 0, i)\nend\n\ndefp get_descent_periods([],\
        \ _, ans, _, _), do: ans\n\ndefp get_descent_periods([_|_]=prices, i, ans, j,\
        \ start) do\n    case length(prices) do\n        len when j >= len -> get_descent_periods(prices,\
        \ i + 1, ans, 0, i)\n        _ ->\n            case Enum.at(prices, j + 1) -\
        \ Enum.at(prices, j) do\n                1 -> get_descent_periods(prices, i,\
        \ ans, j + 1, start)\n                _ -> get_descent_periods(prices, i + 1,\
        \ ans + (j - start + 1) * (j - start + 2) |> div(2), 0, i)\n            end\n\
        \    end\nend"
    approach: 'The problem can be solved by iterating through the array and finding
      the longest possible smooth descent periods. A smooth descent period is a sequence
      of days where the price on each day is lower than the price on the preceding day
      by exactly 1. The first day of the period is exempted from this rule. We can use
      a two-pointer approach to traverse the array and find each longest possible period.
      Once we find a period, we can calculate the number of smooth descent periods within
      that period using the formula for the sum of an arithmetic series: n * (n + 1)
      / 2, where n is the length of the period.'
    time_complexity: The time complexity of the solution is O(n), where n is the number
      of days in the price history. This is because we are iterating through the array
      once to find the longest possible smooth descent periods.
    space_complexity: The space complexity of the solution is O(1), which means the
      space required does not change with the size of the input array, making it very
      efficient in terms of memory usage.
    elapsed_time: 6.316661834716797
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-15 01:10:04 '
---

## Problem #2110: Number of Smooth Descent Periods of a Stock

**Difficulty:** Medium

**Topics:** Array, Math, Dynamic Programming

## Problem Description

<p>You are given an integer array <code>prices</code> representing the daily price history of a stock, where <code>prices[i]</code> is the stock price on the <code>i<sup>th</sup></code> day.</p>

<p>A <strong>smooth descent period</strong> of a stock consists of <strong>one or more contiguous</strong> days such that the price on each day is <strong>lower</strong> than the price on the <strong>preceding day</strong> by <strong>exactly</strong> <code>1</code>. The first day of the period is exempted from this rule.</p>

<p>Return <em>the number of <strong>smooth descent periods</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [3,2,1,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [8,6,7,7]
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 &ne; 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> prices = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is 1 smooth descent period: [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Any array is a series of adjacent longest possible smooth descent periods. For example, [5,3,2,1,7,6] is [5] + [3,2,1] + [7,6].

2. Think of a 2-pointer approach to traverse the array and find each longest possible period.

3. Suppose you found the longest possible period with a length of k. How many periods are within that period? How can you count them quickly? Think of the formula to calculate the sum of 1, 2, 3, ..., k.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-15 01:09:58 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count all 'smooth descent periods' in a given array of stock prices. A smooth descent period is a contiguous subarray where each day's price (after the first) is exactly 1 less than the preceding day's price. Single-day periods are always considered smooth descent periods. The core idea is to iterate through the array and keep track of the length of the current smooth descent period ending at the current day.

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
    long long getDescentPeriods(std::vector<int>& prices) {
        int n = prices.size();
        long long totalDescentPeriods = 0;
        int currentLength = 0;

        for (int i = 0; i < n; i++) {
            if (i == 0 || prices[i] != prices[i-1] - 1) {
                currentLength = 1;
            } else {
                currentLength++;
            }
            totalDescentPeriods += currentLength;
        }

        return totalDescentPeriods;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long getDescentPeriods(int[] prices) {
        int n = prices.length;
        long totalDescentPeriods = 0;
        int currentLength = 0;

        for (int i = 0; i < n; i++) {
            if (i == 0 || prices[i] != prices[i-1] - 1) {
                currentLength = 1;
            } else {
                currentLength++;
            }
            totalDescentPeriods += currentLength;
        }

        return totalDescentPeriods;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        total_descent_periods = 0
        current_length = 0

        for i in range(n):
            if i == 0 or prices[i] != prices[i-1] - 1:
                current_length = 1
            else:
                current_length += 1
            total_descent_periods += current_length

        return total_descent_periods
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        total_descent_periods = 0
        current_length = 0

        for i in range(n):
            if i == 0 or prices[i] != prices[i-1] - 1:
                current_length = 1
            else:
                current_length += 1
            total_descent_periods += current_length

        return total_descent_periods
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stddef.h> // For size_t

long long getDescentPeriods(int* prices, int pricesSize) {
    long long totalDescentPeriods = 0;
    int currentLength = 0;

    for (int i = 0; i < pricesSize; i++) {
        if (i == 0 || prices[i] != prices[i-1] - 1) {
            currentLength = 1;
        } else {
            currentLength++;
        }
        totalDescentPeriods += currentLength;
    }

    return totalDescentPeriods;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public long GetDescentPeriods(int[] prices) {
        int n = prices.Length;
        long totalDescentPeriods = 0;
        int currentLength = 0;

        for (int i = 0; i < n; i++) {
            if (i == 0 || prices[i] != prices[i-1] - 1) {
                currentLength = 1;
            } else {
                currentLength++;
            }
            totalDescentPeriods += currentLength;
        }

        return totalDescentPeriods;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} prices
 * @return {number}
 */
var getDescentPeriods = function(prices) {
    const n = prices.length;
    let totalDescentPeriods = 0;
    let currentLength = 0;

    for (let i = 0; i < n; i++) {
        if (i === 0 || prices[i] !== prices[i-1] - 1) {
            currentLength = 1;
        } else {
            currentLength++;
        }
        totalDescentPeriods += currentLength;
    }

    return totalDescentPeriods;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function getDescentPeriods(prices: number[]): number {
    const n = prices.length;
    let totalDescentPeriods: number = 0; 
    let currentLength: number = 0;

    for (let i = 0; i < n; i++) {
        if (i === 0 || prices[i] !== prices[i-1] - 1) {
            currentLength = 1;
        }
        else {
            currentLength++;
        }
        totalDescentPeriods += currentLength;
    }

    return totalDescentPeriods;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function getDescentPeriods($prices) {
        $n = count($prices);
        $totalDescentPeriods = 0; 
        $currentLength = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($i === 0 || $prices[$i] !== $prices[$i-1] - 1) {
                $currentLength = 1;
            } else {
                $currentLength++;
            }
            $totalDescentPeriods += $currentLength;
        }

        return $totalDescentPeriods;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func getDescentPeriods(_ prices: [Int]) -> Int {
        let n = prices.count
        var totalDescentPeriods: Int = 0 
        var currentLength: Int = 0

        for i in 0..<n {
            if i == 0 || prices[i] != prices[i-1] - 1 {
                currentLength = 1
            } else {
                currentLength += 1
            }
            totalDescentPeriods += currentLength
        }

        return totalDescentPeriods
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun getDescentPeriods(prices: IntArray): Long {
        val n = prices.size
        var totalDescentPeriods: Long = 0
        var currentLength: Int = 0

        for (i in 0 until n) {
            if (i == 0 || prices[i] != prices[i-1] - 1) {
                currentLength = 1
            } else {
                currentLength++
            }
            totalDescentPeriods += currentLength
        }

        return totalDescentPeriods
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int getDescentPeriods(List<int> prices) {
    final n = prices.length;
    int totalDescentPeriods = 0; 
    int currentLength = 0;

    for (int i = 0; i < n; i++) {
      if (i == 0 || prices[i] != prices[i-1] - 1) {
        currentLength = 1;
      }
      else {
        currentLength++;
      }
      totalDescentPeriods += currentLength;
    }

    return totalDescentPeriods;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func getDescentPeriods(prices []int) int64 {
    n := len(prices)
    var totalDescentPeriods int64 = 0
    var currentLength int = 0

    for i := 0; i < n; i++ {
        if i == 0 || prices[i] != prices[i-1] - 1 {
            currentLength = 1
        } else {
            currentLength++
        }
        totalDescentPeriods += int64(currentLength)
    }

    return totalDescentPeriods
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} prices
# @return {Integer}
def get_descent_periods(prices)
    n = prices.length
    total_descent_periods = 0 
    current_length = 0

    (0...n).each do |i|
        if i == 0 || prices[i] != prices[i-1] - 1
            current_length = 1
        else
            current_length += 1
        end
        total_descent_periods += current_length
    end

    return total_descent_periods
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def getDescentPeriods(prices: Array[Int]): Long = {
        val n = prices.length
        var totalDescentPeriods: Long = 0
        var currentLength: Int = 0

        for (i <- 0 until n) {
            if (i == 0 || prices(i) != prices(i-1) - 1) {
                currentLength = 1
            } else {
                currentLength += 1
            }
            totalDescentPeriods += currentLength
        }

        totalDescentPeriods
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn get_descent_periods(prices: Vec<i32>) -> i64 {
        let n = prices.len();
        let mut total_descent_periods: i64 = 0;
        let mut current_length: i32 = 0;

        for i in 0..n {
            if i == 0 || prices[i] != prices[i-1] - 1 {
                current_length = 1;
            } else {
                current_length += 1;
            }
            total_descent_periods += current_length as i64;
        }

        total_descent_periods
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define/contract (get-descent-periods prices)
  (-> (listof exact-integer?) exact-integer?)
  (let ([n (length prices)]
        [prices-vec (list->vector prices)])
    (for/fold ([total-descent-periods 0]
               [current-length 0])
              ([i (in-range n)])
      (let ([new-current-length
             (if (or (= i 0)
                     (not (= (vector-ref prices-vec i) (- (vector-ref prices-vec (- i 1)) 1))))
                 1
                 (+ current-length 1))])
        (values (+ total-descent-periods new-current-length)
                new-current-length)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([get_descent_periods/1]).

get_descent_periods([]) -> 0;
get_descent_periods([H | T]) ->
    % State: {TotalDescentPeriods, CurrentLength, PreviousPrice}
    % Initial state for foldl: {1, 1, H} because [H] is always a period of length 1.
    {Total, _Current, _Prev} = lists:foldl(
        fun(CurrentPrice, {AccTotal, AccLength, PrevPrice}) ->
            NewLength =
                if CurrentPrice == PrevPrice - 1 ->
                    AccLength + 1;
                true ->
                    1
                end,
            {AccTotal + NewLength, NewLength, CurrentPrice}
        end,
        {1, 1, H}, % Initial state: total=1 (for H), length=1, prev_price=H
        T % Fold over the rest of the list
    ),
    Total.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec get_descent_periods(prices :: [integer]) :: integer
  def get_descent_periods(prices) do
    Enum.reduce(prices, {0, 0, nil}, fn current_price, {total_descent_periods, current_length, prev_price} ->
      new_length =
        if is_nil(prev_price) or current_price != prev_price - 1 do
          1
        else
          current_length + 1
        end

      {total_descent_periods + new_length, new_length, current_price}
    end)
    |> elem(0) # Extract the total_descent_periods
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the number of days (length of the `prices` array). We iterate through the array once, performing constant-time operations for each element.

- **Space Complexity:** The space complexity is O(1). We use a few variables to store the total count, the current period length, and loop indices, which consume a constant amount of extra space regardless of the input size.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-15 01:10:04 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating through the array and finding the longest possible smooth descent periods. A smooth descent period is a sequence of days where the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule. We can use a two-pointer approach to traverse the array and find each longest possible period. Once we find a period, we can calculate the number of smooth descent periods within that period using the formula for the sum of an arithmetic series: n * (n + 1) / 2, where n is the length of the period.

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
    long long getDescentPeriods(vector<int>& prices) {
        long long ans = 0;
        int i = 0;
        while (i < prices.size()) {
            int j = i;
            while (j + 1 < prices.size() && prices[j] - prices[j + 1] == 1) j++;
            int k = j - i + 1;
            ans += 1LL * k * (k + 1) / 2;
            i = j + 1;
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
    public long getDescentPeriods(int[] prices) {
        long ans = 0;
        int i = 0;
        while (i < prices.length) {
            int j = i;
            while (j + 1 < prices.length && prices[j] - prices[j + 1] == 1) j++;
            int k = j - i + 1;
            ans += (long) k * (k + 1) / 2;
            i = j + 1;
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
class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        ans = 0
        i = 0
        while i < len(prices):
            j = i
            while j + 1 < len(prices) and prices[j] - prices[j + 1] == 1: j += 1
            k = j - i + 1
            ans += k * (k + 1) // 2
            i = j + 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        ans = 0
        i = 0
        while i < len(prices):
            j = i
            while j + 1 < len(prices) and prices[j] - prices[j + 1] == 1: j += 1
            k = j - i + 1
            ans += k * (k + 1) // 2
            i = j + 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long getDescentPeriods(int* prices, int pricesSize) {
    long long ans = 0;
    int i = 0;
    while (i < pricesSize) {
        int j = i;
        while (j + 1 < pricesSize && prices[j] - prices[j + 1] == 1) j++;
        int k = j - i + 1;
        ans += (long long)k * (k + 1) / 2;
        i = j + 1;
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long GetDescentPeriods(int[] prices) {
        long ans = 0;
        int i = 0;
        while (i < prices.Length) {
            int j = i;
            while (j + 1 < prices.Length && prices[j] - prices[j + 1] == 1) j++;
            int k = j - i + 1;
            ans += (long)k * (k + 1) / 2;
            i = j + 1;
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
var getDescentPeriods = function(prices) {
    let ans = 0;
    let i = 0;
    while (i < prices.length) {
        let j = i;
        while (j + 1 < prices.length && prices[j] - prices[j + 1] == 1) j++;
        let k = j - i + 1;
        ans += k * (k + 1) / 2;
        i = j + 1;
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function getDescentPeriods(prices: number[]): number {
    let ans: number = 0;
    let i: number = 0;
    while (i < prices.length) {
        let j: number = i;
        while (j + 1 < prices.length && prices[j] - prices[j + 1] == 1) j++;
        let k: number = j - i + 1;
        ans += k * (k + 1) / 2;
        i = j + 1;
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function getDescentPeriods($prices) {
        $ans = 0;
        $i = 0;
        while ($i < count($prices)) {
            $j = $i;
            while ($j + 1 < count($prices) && $prices[$j] - $prices[$j + 1] == 1) $j++;
            $k = $j - $i + 1;
            $ans += $k * ($k + 1) / 2;
            $i = $j + 1;
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
    func getDescentPeriods(_ prices: [Int]) -> Int64 {
        var ans: Int64 = 0
        var i = 0
        while i < prices.count {
            var j = i
            while j + 1 < prices.count && prices[j] - prices[j + 1] == 1 {
                j += 1
            }
            let k = j - i + 1
            ans += Int64(k) * Int64(k + 1) / 2
            i = j + 1
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
    fun getDescentPeriods(prices: IntArray): Long {
        var ans: Long = 0
        var i = 0
        while (i < prices.size) {
            var j = i
            while (j + 1 < prices.size && prices[j] - prices[j + 1] == 1) j++
            val k = j - i + 1
            ans += k.toLong() * (k + 1) / 2
            i = j + 1
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
    int getDescentPeriods(List<int> prices) {
        int ans = 0;
        int i = 0;
        while (i < prices.length) {
            int j = i;
            while (j + 1 < prices.length && prices[j] - prices[j + 1] == 1) j++;
            int k = j - i + 1;
            ans += k * (k + 1) ~/ 2;
            i = j + 1;
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
func getDescentPeriods(prices []int) int64 {
    ans := int64(0)
    i := 0
    for i < len(prices) {
        j := i
        for j + 1 < len(prices) && prices[j] - prices[j + 1] == 1 {
            j++
        }
        k := j - i + 1
        ans += int64(k) * int64(k + 1) / 2
        i = j + 1
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def get_descent_periods(prices)
    ans = 0
    i = 0
    while i < prices.size
        j = i
        while j + 1 < prices.size && prices[j] - prices[j + 1] == 1
            j += 1
        end
        k = j - i + 1
        ans += k * (k + 1) / 2
        i = j + 1
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
    def getDescentPeriods(prices: Array[Int]): Long = {
        var ans: Long = 0
        var i = 0
        while (i < prices.length) {
            var j = i
            while (j + 1 < prices.length && prices(j) - prices(j + 1) == 1) j += 1
            val k = j - i + 1
            ans += k.toLong * (k + 1) / 2
            i = j + 1
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
    pub fn get_descent_periods(prices: Vec<i32>) -> i64 {
        let mut ans: i64 = 0;
        let mut i: usize = 0;
        while i < prices.len() {
            let mut j: usize = i;
            while j + 1 < prices.len() && prices[j] - prices[j + 1] == 1 {
                j += 1;
            }
            let k: i64 = (j - i + 1) as i64;
            ans += k * (k + 1) / 2;
            i = j + 1;
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
define (get-descent-periods prices)
    (let loop ((i 0) (ans 0))
        (if (>= i (length prices))
            ans
            (let ((j (let loop2 ((j i))
                            (if (and (< j (sub1 (length prices))) (= (- (list-ref prices j) (list-ref prices (add1 j))) 1))
                                (loop2 (add1 j))
                                j)))))
                (loop (add1 j) (+ ans (let ((k (- j i))) (/ (* k (add1 k)) 2))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
get_descent_periods(Prices) ->
    get_descent_periods(Prices, 0, 0).
get_descent_periods([_|_]=Prices, I, Ans) ->
    get_descent_periods(Prices, I, Ans, 0, I);
get_descent_periods([], _, Ans, _, _) -> Ans;
get_descent_periods([_|_]=Prices, I, Ans, J, Start) ->
    case length(Prices) of
        Len when J >= Len -> get_descent_periods(Prices, I + 1, Ans, 0, I);
        _ ->
            case lists:nth(J + 1, Prices) - lists:nth(J, Prices) of
                1 -> get_descent_periods(Prices, I, Ans, J + 1, Start);
                _ -> get_descent_periods(Prices, I + 1, Ans + (J - Start + 1) * (J - Start + 2) div 2, 0, I)
            end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def get_descent_periods(prices) do
    get_descent_periods(prices, 0, 0)
end

defp get_descent_periods([], _, ans), do: ans

defp get_descent_periods([_|_]=prices, i, ans) do
    get_descent_periods(prices, i, ans, 0, i)
end

defp get_descent_periods([], _, ans, _, _), do: ans

defp get_descent_periods([_|_]=prices, i, ans, j, start) do
    case length(prices) do
        len when j >= len -> get_descent_periods(prices, i + 1, ans, 0, i)
        _ ->
            case Enum.at(prices, j + 1) - Enum.at(prices, j) do
                1 -> get_descent_periods(prices, i, ans, j + 1, start)
                _ -> get_descent_periods(prices, i + 1, ans + (j - start + 1) * (j - start + 2) |> div(2), 0, i)
            end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n), where n is the number of days in the price history. This is because we are iterating through the array once to find the longest possible smooth descent periods.

- **Space Complexity:** The space complexity of the solution is O(1), which means the space required does not change with the size of the input array, making it very efficient in terms of memory usage.

</div>
</details>
