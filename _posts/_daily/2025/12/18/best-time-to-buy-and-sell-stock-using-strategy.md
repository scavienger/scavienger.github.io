---
layout: post
title: "Best Time to Buy and Sell Stock using Strategy"
date: 2025-12-18 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Sliding Window", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxProfit(std::vector<int>& prices,\
        \ std::vector<int>& strategy, int k) {\n        int n = prices.size();\n\n \
        \       std::vector<long long> prefixOriginalProfit(n + 1, 0);\n        std::vector<long\
        \ long> prefixPricesSum(n + 1, 0);\n\n        for (int i = 0; i < n; ++i) {\n\
        \            prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + (long long)strategy[i]\
        \ * prices[i];\n            prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i];\n\
        \        }\n\n        long long maxProfitVal = prefixOriginalProfit[n];\n\n\
        \        for (int j = 0; j <= n - k; ++j) {\n            long long originalSegmentProfit\
        \ = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];\n\n            long\
        \ long modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j + k\
        \ / 2];\n\n            long long delta = modifiedSegmentProfit - originalSegmentProfit;\n\
        \n            maxProfitVal = std::max(maxProfitVal, prefixOriginalProfit[n]\
        \ + delta);\n        }\n\n        return maxProfitVal;\n    }\n};"
      java: "import java.util.List;\nimport java.util.ArrayList;\nimport java.util.Arrays;\n\
        \nclass Solution {\n    public long maxProfit(int[] prices, int[] strategy,\
        \ int k) {\n        int n = prices.length;\n\n        long[] prefixOriginalProfit\
        \ = new long[n + 1];\n        long[] prefixPricesSum = new long[n + 1];\n\n\
        \        for (int i = 0; i < n; ++i) {\n            prefixOriginalProfit[i+1]\
        \ = prefixOriginalProfit[i] + (long)strategy[i] * prices[i];\n            prefixPricesSum[i+1]\
        \ = prefixPricesSum[i] + prices[i];\n        }\n\n        long maxProfitVal\
        \ = prefixOriginalProfit[n];\n\n        for (int j = 0; j <= n - k; ++j) {\n\
        \            long originalSegmentProfit = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];\n\
        \n            long modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j\
        \ + k / 2];\n\n            long delta = modifiedSegmentProfit - originalSegmentProfit;\n\
        \n            maxProfitVal = Math.max(maxProfitVal, prefixOriginalProfit[n]\
        \ + delta);\n        }\n\n        return maxProfitVal;\n    }\n}"
      python: "class Solution:\n    def maxProfit(self, prices: List[int], strategy:\
        \ List[int], k: int) -> int:\n        n = len(prices)\n\n        prefix_original_profit\
        \ = [0] * (n + 1)\n        prefix_prices_sum = [0] * (n + 1)\n\n        for\
        \ i in range(n):\n            prefix_original_profit[i+1] = prefix_original_profit[i]\
        \ + strategy[i] * prices[i]\n            prefix_prices_sum[i+1] = prefix_prices_sum[i]\
        \ + prices[i]\n\n        max_profit = prefix_original_profit[n]\n\n        for\
        \ j in range(n - k + 1):\n            original_segment_profit = prefix_original_profit[j+k]\
        \ - prefix_original_profit[j]\n\n            modified_segment_profit = prefix_prices_sum[j+k]\
        \ - prefix_prices_sum[j + k // 2]\n\n            delta = modified_segment_profit\
        \ - original_segment_profit\n\n            max_profit = max(max_profit, prefix_original_profit[n]\
        \ + delta)\n\n        return max_profit"
      python3: "class Solution:\n    def maxProfit(self, prices: List[int], strategy:\
        \ List[int], k: int) -> int:\n        n = len(prices)\n\n        prefix_original_profit\
        \ = [0] * (n + 1)\n        prefix_prices_sum = [0] * (n + 1)\n\n        for\
        \ i in range(n):\n            prefix_original_profit[i+1] = prefix_original_profit[i]\
        \ + strategy[i] * prices[i]\n            prefix_prices_sum[i+1] = prefix_prices_sum[i]\
        \ + prices[i]\n\n        max_profit = prefix_original_profit[n]\n\n        for\
        \ j in range(n - k + 1):\n            original_segment_profit = prefix_original_profit[j+k]\
        \ - prefix_original_profit[j]\n\n            modified_segment_profit = prefix_prices_sum[j+k]\
        \ - prefix_prices_sum[j + k // 2]\n\n            delta = modified_segment_profit\
        \ - original_segment_profit\n\n            max_profit = max(max_profit, prefix_original_profit[n]\
        \ + delta)\n\n        return max_profit"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nlong long\
        \ maxProfit(int* prices, int pricesSize, int* strategy, int strategySize, int\
        \ k) {\n    int n = pricesSize;\n\n    long long* prefixOriginalProfit = (long\
        \ long*)calloc(n + 1, sizeof(long long));\n    long long* prefixPricesSum =\
        \ (long long*)calloc(n + 1, sizeof(long long));\n\n    for (int i = 0; i < n;\
        \ ++i) {\n        prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + (long\
        \ long)strategy[i] * prices[i];\n        prefixPricesSum[i+1] = prefixPricesSum[i]\
        \ + prices[i];\n    }\n\n    long long maxProfitVal = prefixOriginalProfit[n];\n\
        \n    for (int j = 0; j <= n - k; ++j) {\n        long long originalSegmentProfit\
        \ = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];\n\n        long long\
        \ modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2];\n\
        \n        long long delta = modifiedSegmentProfit - originalSegmentProfit;\n\
        \n        if (prefixOriginalProfit[n] + delta > maxProfitVal) {\n          \
        \  maxProfitVal = prefixOriginalProfit[n] + delta;\n        }\n    }\n\n   \
        \ free(prefixOriginalProfit);\n    free(prefixPricesSum);\n\n    return maxProfitVal;\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public long MaxProfit(int[] prices, int[] strategy,\
        \ int k) {\n        int n = prices.Length;\n\n        long[] prefixOriginalProfit\
        \ = new long[n + 1];\n        long[] prefixPricesSum = new long[n + 1];\n\n\
        \        for (int i = 0; i < n; ++i) {\n            prefixOriginalProfit[i+1]\
        \ = prefixOriginalProfit[i] + (long)strategy[i] * prices[i];\n            prefixPricesSum[i+1]\
        \ = prefixPricesSum[i] + prices[i];\n        }\n\n        long maxProfitVal\
        \ = prefixOriginalProfit[n];\n\n        for (int j = 0; j <= n - k; ++j) {\n\
        \            long originalSegmentProfit = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];\n\
        \n            long modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j\
        \ + k / 2];\n\n            long delta = modifiedSegmentProfit - originalSegmentProfit;\n\
        \n            maxProfitVal = Math.Max(maxProfitVal, prefixOriginalProfit[n]\
        \ + delta);\n        }\n\n        return maxProfitVal;\n    }\n}"
      javascript: "/**\n * @param {number[]} prices\n * @param {number[]} strategy\n\
        \ * @param {number} k\n * @return {number}\n */\nvar maxProfit = function(prices,\
        \ strategy, k) {\n    const n = prices.length;\n\n    const prefixOriginalProfit\
        \ = new Array(n + 1).fill(0);\n    const prefixPricesSum = new Array(n + 1).fill(0);\n\
        \n    for (let i = 0; i < n; ++i) {\n        prefixOriginalProfit[i+1] = prefixOriginalProfit[i]\
        \ + strategy[i] * prices[i];\n        prefixPricesSum[i+1] = prefixPricesSum[i]\
        \ + prices[i];\n    }\n\n    let maxProfitVal = prefixOriginalProfit[n];\n\n\
        \    for (let j = 0; j <= n - k; ++j) {\n        const originalSegmentProfit\
        \ = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];\n\n        const modifiedSegmentProfit\
        \ = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2];\n\n        const delta\
        \ = modifiedSegmentProfit - originalSegmentProfit;\n\n        maxProfitVal =\
        \ Math.max(maxProfitVal, prefixOriginalProfit[n] + delta);\n    }\n\n    return\
        \ maxProfitVal;\n};"
      typescript: "function maxProfit(prices: number[], strategy: number[], k: number):\
        \ number {\n    const n = prices.length;\n\n    const prefixOriginalProfit:\
        \ number[] = new Array(n + 1).fill(0);\n    const prefixPricesSum: number[]\
        \ = new Array(n + 1).fill(0);\n\n    for (let i = 0; i < n; ++i) {\n       \
        \ prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + strategy[i] * prices[i];\n\
        \        prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i];\n    }\n\n \
        \   let maxProfitVal: number = prefixOriginalProfit[n];\n\n    for (let j =\
        \ 0; j <= n - k; ++j) {\n        const originalSegmentProfit: number = prefixOriginalProfit[j+k]\
        \ - prefixOriginalProfit[j];\n\n        const modifiedSegmentProfit: number\
        \ = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2];\n\n        const delta:\
        \ number = modifiedSegmentProfit - originalSegmentProfit;\n\n        maxProfitVal\
        \ = Math.max(maxProfitVal, prefixOriginalProfit[n] + delta);\n    }\n\n    return\
        \ maxProfitVal;\n}"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[] $prices\n  \
        \   * @param Integer[] $strategy\n     * @param Integer $k\n     * @return Integer\n\
        \     */\n    function maxProfit($prices, $strategy, $k) {\n        $n = count($prices);\n\
        \n        $prefixOriginalProfit = array_fill(0, $n + 1, 0);\n        $prefixPricesSum\
        \ = array_fill(0, $n + 1, 0);\n\n        for ($i = 0; $i < $n; ++$i) {\n   \
        \         $prefixOriginalProfit[$i+1] = $prefixOriginalProfit[$i] + $strategy[$i]\
        \ * $prices[$i];\n            $prefixPricesSum[$i+1] = $prefixPricesSum[$i]\
        \ + $prices[$i];\n        }\n\n        $maxProfitVal = $prefixOriginalProfit[$n];\n\
        \n        for ($j = 0; $j <= $n - $k; ++$j) {\n            $originalSegmentProfit\
        \ = $prefixOriginalProfit[$j+$k] - $prefixOriginalProfit[$j];\n\n          \
        \  $modifiedSegmentProfit = $prefixPricesSum[$j+$k] - $prefixPricesSum[$j +\
        \ $k / 2];\n\n            $delta = $modifiedSegmentProfit - $originalSegmentProfit;\n\
        \n            $maxProfitVal = max($maxProfitVal, $prefixOriginalProfit[$n] +\
        \ $delta);\n        }\n\n        return $maxProfitVal;\n    }\n}\n?>"
      swift: "import Foundation\n\nclass Solution {\n    func maxProfit(_ prices: [Int],\
        \ _ strategy: [Int], _ k: Int) -> Int {\n        let n = prices.count\n\n  \
        \      var prefixOriginalProfit = Array(repeating: 0, count: n + 1)\n      \
        \  var prefixPricesSum = Array(repeating: 0, count: n + 1)\n\n        for i\
        \ in 0..<n {\n            prefixOriginalProfit[i+1] = prefixOriginalProfit[i]\
        \ + strategy[i] * prices[i]\n            prefixPricesSum[i+1] = prefixPricesSum[i]\
        \ + prices[i]\n        }\n\n        var maxProfitVal = prefixOriginalProfit[n]\n\
        \n        for j in 0...(n - k) {\n            let originalSegmentProfit = prefixOriginalProfit[j+k]\
        \ - prefixOriginalProfit[j]\n\n            let modifiedSegmentProfit = prefixPricesSum[j+k]\
        \ - prefixPricesSum[j + k / 2]\n\n            let delta = modifiedSegmentProfit\
        \ - originalSegmentProfit\n\n            maxProfitVal = max(maxProfitVal, prefixOriginalProfit[n]\
        \ + delta)\n        }\n\n        return maxProfitVal\n    }\n}"
      kotlin: "import kotlin.math.max\n\nclass Solution {\n    fun maxProfit(prices:\
        \ IntArray, strategy: IntArray, k: Int): Long {\n        val n = prices.size\n\
        \n        val prefixOriginalProfit = LongArray(n + 1)\n        val prefixPricesSum\
        \ = LongArray(n + 1)\n\n        for (i in 0 until n) {\n            prefixOriginalProfit[i+1]\
        \ = prefixOriginalProfit[i] + strategy[i].toLong() * prices[i]\n           \
        \ prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i].toLong()\n        }\n\
        \n        var maxProfitVal = prefixOriginalProfit[n]\n\n        for (j in 0..(n\
        \ - k)) {\n            val originalSegmentProfit = prefixOriginalProfit[j+k]\
        \ - prefixOriginalProfit[j]\n\n            val modifiedSegmentProfit = prefixPricesSum[j+k]\
        \ - prefixPricesSum[j + k / 2]\n\n            val delta = modifiedSegmentProfit\
        \ - originalSegmentProfit\n\n            maxProfitVal = max(maxProfitVal, prefixOriginalProfit[n]\
        \ + delta)\n        }\n\n        return maxProfitVal\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maxProfit(List<int> prices,\
        \ List<int> strategy, int k) {\n    int n = prices.length;\n\n    List<int>\
        \ prefixOriginalProfit = List<int>.filled(n + 1, 0);\n    List<int> prefixPricesSum\
        \ = List<int>.filled(n + 1, 0);\n\n    for (int i = 0; i < n; ++i) {\n     \
        \ prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + strategy[i] * prices[i];\n\
        \      prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i];\n    }\n\n   \
        \ int maxProfitVal = prefixOriginalProfit[n];\n\n    for (int j = 0; j <= n\
        \ - k; ++j) {\n      int originalSegmentProfit = prefixOriginalProfit[j+k] -\
        \ prefixOriginalProfit[j];\n\n      int modifiedSegmentProfit = prefixPricesSum[j+k]\
        \ - prefixPricesSum[j + k ~/ 2];\n\n      int delta = modifiedSegmentProfit\
        \ - originalSegmentProfit;\n\n      maxProfitVal = max(maxProfitVal, prefixOriginalProfit[n]\
        \ + delta);\n    }\n\n    return maxProfitVal;\n  }\n}"
      go: "package main\n\nimport (\n\t\"math\"\n)\n\nfunc maxProfit(prices []int, strategy\
        \ []int, k int) int64 {\n    n := len(prices)\n\n    prefixOriginalProfit :=\
        \ make([]int64, n + 1)\n    prefixPricesSum := make([]int64, n + 1)\n\n    for\
        \ i := 0; i < n; i++ {\n        prefixOriginalProfit[i+1] = prefixOriginalProfit[i]\
        \ + int64(strategy[i]) * int64(prices[i])\n        prefixPricesSum[i+1] = prefixPricesSum[i]\
        \ + int64(prices[i])\n    }\n\n    maxProfitVal := prefixOriginalProfit[n]\n\
        \n    for j := 0; j <= n - k; j++ {\n        originalSegmentProfit := prefixOriginalProfit[j+k]\
        \ - prefixOriginalProfit[j]\n\n        modifiedSegmentProfit := prefixPricesSum[j+k]\
        \ - prefixPricesSum[j + k / 2]\n\n        delta := modifiedSegmentProfit - originalSegmentProfit;\n\
        \n        maxProfitVal = int64(math.Max(float64(maxProfitVal), float64(prefixOriginalProfit[n]\
        \ + delta)))\n    }\n\n    return maxProfitVal\n}"
      ruby: "# @param {Integer[]} prices\n# @param {Integer[]} strategy\n# @param {Integer}\
        \ k\n# @return {Integer}\ndef max_profit(prices, strategy, k)\n    n = prices.length\n\
        \n    prefix_original_profit = Array.new(n + 1, 0)\n    prefix_prices_sum =\
        \ Array.new(n + 1, 0)\n\n    (0...n).each do |i|\n        prefix_original_profit[i+1]\
        \ = prefix_original_profit[i] + strategy[i] * prices[i]\n        prefix_prices_sum[i+1]\
        \ = prefix_prices_sum[i] + prices[i]\n    end\n\n    max_profit_val = prefix_original_profit[n]\n\
        \n    (0..n - k).each do |j|\n        original_segment_profit = prefix_original_profit[j+k]\
        \ - prefix_original_profit[j]\n\n        modified_segment_profit = prefix_prices_sum[j+k]\
        \ - prefix_prices_sum[j + k / 2]\n\n        delta = modified_segment_profit\
        \ - original_segment_profit\n\n        max_profit_val = [max_profit_val, prefix_original_profit[n]\
        \ + delta].max\n    end\n\n    return max_profit_val\nend"
      scala: "import scala.collection.mutable.ArrayBuffer\nimport scala.math.max\n\n\
        object Solution {\n    def maxProfit(prices: Array[Int], strategy: Array[Int],\
        \ k: Int): Long = {\n        val n = prices.length\n\n        val prefixOriginalProfit\
        \ = Array.fill[Long](n + 1)(0L)\n        val prefixPricesSum = Array.fill[Long](n\
        \ + 1)(0L)\n\n        for (i <- 0 until n) {\n            prefixOriginalProfit(i+1)\
        \ = prefixOriginalProfit(i) + strategy(i).toLong * prices(i)\n            prefixPricesSum(i+1)\
        \ = prefixPricesSum(i) + prices(i).toLong\n        }\n\n        var maxProfitVal\
        \ = prefixOriginalProfit(n)\n\n        for (j <- 0 to n - k) {\n           \
        \ val originalSegmentProfit = prefixOriginalProfit(j+k) - prefixOriginalProfit(j)\n\
        \n            val modifiedSegmentProfit = prefixPricesSum(j+k) - prefixPricesSum(j\
        \ + k / 2)\n\n            val delta = modifiedSegmentProfit - originalSegmentProfit\n\
        \n            maxProfitVal = max(maxProfitVal, prefixOriginalProfit(n) + delta)\n\
        \        }\n\n        maxProfitVal\n    }\n}"
      rust: "impl Solution {\n    pub fn max_profit(prices: Vec<i32>, strategy: Vec<i32>,\
        \ k: i32) -> i64 {\n        let n = prices.len();\n        let k_usize = k as\
        \ usize;\n\n        let mut prefix_original_profit: Vec<i64> = vec![0; n + 1];\n\
        \        let mut prefix_prices_sum: Vec<i64> = vec![0; n + 1];\n\n        for\
        \ i in 0..n {\n            prefix_original_profit[i+1] = prefix_original_profit[i]\
        \ + (strategy[i] as i64) * (prices[i] as i64);\n            prefix_prices_sum[i+1]\
        \ = prefix_prices_sum[i] + (prices[i] as i64);\n        }\n\n        let mut\
        \ max_profit_val: i64 = prefix_original_profit[n];\n\n        for j in 0..=(n\
        \ - k_usize) {\n            let original_segment_profit = prefix_original_profit[j+k_usize]\
        \ - prefix_original_profit[j];\n\n            let modified_segment_profit =\
        \ prefix_prices_sum[j+k_usize] - prefix_prices_sum[j + k_usize / 2];\n\n   \
        \         let delta = modified_segment_profit - original_segment_profit;\n\n\
        \            max_profit_val = max_profit_val.max(prefix_original_profit[n] +\
        \ delta);\n        }\n\n        max_profit_val\n    }\n}"
      racket: "#lang racket\n\n(define (max-profit prices strategy k)\n  (define n (vector-length\
        \ prices))\n\n  (define prefix-original-profit (make-vector (+ n 1) 0))\n  (define\
        \ prefix-prices-sum (make-vector (+ n 1) 0))\n\n  (for ([i (in-range n)])\n\
        \    (vector-set! prefix-original-profit (+ i 1)\n                 (+ (vector-ref\
        \ prefix-original-profit i)\n                    (* (vector-ref strategy i)\
        \ (vector-ref prices i))))\n    (vector-set! prefix-prices-sum (+ i 1)\n   \
        \              (+ (vector-ref prefix-prices-sum i)\n                    (vector-ref\
        \ prices i))))\n\n  (define max-profit-val (vector-ref prefix-original-profit\
        \ n))\n\n  (for ([j (in-range (- n k) (+ 1 (- n k)))])\n    (define original-segment-profit\
        \ (- (vector-ref prefix-original-profit (+ j k))\n                         \
        \              (vector-ref prefix-original-profit j)))\n\n    (define modified-segment-profit\
        \ (- (vector-ref prefix-prices-sum (+ j k))\n                              \
        \         (vector-ref prefix-prices-sum (+ j (quotient k 2)))))\n\n    (define\
        \ delta (- modified-segment-profit original-segment-profit))\n\n    (set! max-profit-val\
        \ (max max-profit-val (+ (vector-ref prefix-original-profit n) delta))))\n\n\
        \  max-profit-val)"
      erlang: "-module(solution).\n-export([max_profit/3]).\n\nmax_profit(Prices, Strategy,\
        \ K) ->\n    N = length(Prices),\n\n    PricesTuple = list_to_tuple(Prices),\n\
        \    StrategyTuple = list_to_tuple(Strategy),\n\n    {_, PrefixOriginalProfitList}\
        \ = lists:mapaccum(\n        fun(I, AccSum) ->\n            Val = element(I+1,\
        \ StrategyTuple) * element(I+1, PricesTuple),\n            NewSum = AccSum +\
        \ Val,\n            {NewSum, NewSum}\n        end,\n        0,\n        lists:seq(0,\
        \ N-1)\n    ),\n    PrefixOriginalProfitTuple = list_to_tuple([0 | PrefixOriginalProfitList]),\n\
        \n    {_, PrefixPricesSumList} = lists:mapaccum(\n        fun(I, AccSum) ->\n\
        \            Val = element(I+1, PricesTuple),\n            NewSum = AccSum +\
        \ Val,\n            {NewSum, NewSum}\n        end,\n        0,\n        lists:seq(0,\
        \ N-1)\n    ),\n    PrefixPricesSumTuple = list_to_tuple([0 | PrefixPricesSumList]),\n\
        \n    MaxProfitVal = element(N + 1, PrefixOriginalProfitTuple),\n\n    lists:foldl(\n\
        \        fun(J, CurrentMaxProfit) ->\n            J_1_indexed = J + 1,\n   \
        \         K_half = K div 2,\n\n            OriginalSegmentProfit = element(J_1_indexed\
        \ + K, PrefixOriginalProfitTuple) - element(J_1_indexed, PrefixOriginalProfitTuple),\n\
        \n            ModifiedSegmentProfit = element(J_1_indexed + K, PrefixPricesSumTuple)\
        \ - element(J_1_indexed + K_half, PrefixPricesSumTuple),\n\n            Delta\
        \ = ModifiedSegmentProfit - OriginalSegmentProfit,\n\n            max(CurrentMaxProfit,\
        \ element(N + 1, PrefixOriginalProfitTuple) + Delta)\n        end,\n       \
        \ MaxProfitVal,\n        lists:seq(0, N - K)\n    )."
      elixir: "defmodule Solution do\n  @spec max_profit(prices :: [integer], strategy\
        \ :: [integer], k :: integer) :: integer\n  def max_profit(prices, strategy,\
        \ k) do\n    n = length(prices)\n\n    prices_tuple = List.to_tuple(prices)\n\
        \    strategy_tuple = List.to_tuple(strategy)\n\n    {_, prefix_original_profit_list}\
        \ = \n      Enum.map_reduce(0..(n-1), 0, fn i, acc_sum ->\n        val = elem(strategy_tuple,\
        \ i) * elem(prices_tuple, i)\n        new_sum = acc_sum + val\n        {new_sum,\
        \ new_sum}\n      end)\n    prefix_original_profit_tuple = List.to_tuple([0\
        \ | prefix_original_profit_list])\n\n    {_, prefix_prices_sum_list} = \n  \
        \    Enum.map_reduce(0..(n-1), 0, fn i, acc_sum ->\n        val = elem(prices_tuple,\
        \ i)\n        new_sum = acc_sum + val\n        {new_sum, new_sum}\n      end)\n\
        \    prefix_prices_sum_tuple = List.to_tuple([0 | prefix_prices_sum_list])\n\
        \n    max_profit_val = elem(prefix_original_profit_tuple, n)\n\n    Enum.reduce(0..(n\
        \ - k), max_profit_val, fn j, current_max_profit ->\n      original_segment_profit\
        \ = elem(prefix_original_profit_tuple, j + k) - elem(prefix_original_profit_tuple,\
        \ j)\n\n      modified_segment_profit = elem(prefix_prices_sum_tuple, j + k)\
        \ - elem(prefix_prices_sum_tuple, j + div(k, 2))\n\n      delta = modified_segment_profit\
        \ - original_segment_profit\n\n      max(current_max_profit, elem(prefix_original_profit_tuple,\
        \ n) + delta)\n    end)\n  end\nend"
    approach: 'The problem asks us to find the maximum profit achievable by either keeping
      the original trading strategy or applying at most one specific modification to
      a contiguous segment of the strategy. The profit is calculated as the sum of `strategy[i]
      * prices[i]` for all days. A modification involves selecting a `k`-length segment,
      setting its first `k/2` elements to `0` (hold), and its last `k/2` elements to
      `1` (sell).


      The core idea is to first calculate the total profit with the original strategy.
      Then, we iterate through all possible contiguous segments of length `k` where
      a modification could be applied. For each such segment, we calculate the change
      in profit that would result from applying the modification. This change (delta)
      is added to the original total profit, and we keep track of the maximum profit
      found across all these scenarios. To efficiently calculate segment sums and the
      profit delta, we use prefix sum arrays. One prefix sum array stores the cumulative
      sum of `strategy[i] * prices[i]`, and another stores the cumulative sum of `prices[i]`.
      These allow us to query any segment sum in O(1) time.'
    time_complexity: The time complexity is O(N), where N is the length of the `prices`
      and `strategy` arrays. This is because we iterate through the arrays once to build
      the two prefix sum arrays (O(N)), and then we iterate at most N-k+1 times (which
      is O(N)) to consider all possible `k`-length segments for modification. Each calculation
      within the loop takes constant time using the precomputed prefix sums.
    space_complexity: The space complexity is O(N), where N is the length of the `prices`
      and `strategy` arrays. This is due to storing two prefix sum arrays, `prefix_original_profit`
      and `prefix_prices_sum`, each of size N+1. No other data structures grow with
      the input size.
    elapsed_time: 118.66921854019165
    model: gemini-2.5-flash
    generated_at: '2025-12-18 01:06:07 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxProfit(vector<int>& prices, vector<int>&\
        \ strategy, int k) {\n        int n = prices.size();\n        int base = 0;\n\
        \        for (int i = 0; i < n; i++) {\n            base += prices[i] * strategy[i];\n\
        \        }\n        int max_profit = base;\n        for (int i = 0; i <= n -\
        \ k; i++) {\n            int delta = 0;\n            for (int j = i; j < i +\
        \ k / 2; j++) {\n                delta -= prices[j] * strategy[j];\n       \
        \     }\n            for (int j = i + k / 2; j < i + k; j++) {\n           \
        \     delta += prices[j] * strategy[j];\n            }\n            max_profit\
        \ = max(max_profit, base + delta);\n        }\n        return max_profit;\n\
        \    }\n};"
      java: "class Solution {\n    public int maxProfit(int[] prices, int[] strategy,\
        \ int k) {\n        int n = prices.length;\n        int base = 0;\n        for\
        \ (int i = 0; i < n; i++) {\n            base += prices[i] * strategy[i];\n\
        \        }\n        int maxProfit = base;\n        for (int i = 0; i <= n -\
        \ k; i++) {\n            int delta = 0;\n            for (int j = i; j < i +\
        \ k / 2; j++) {\n                delta -= prices[j] * strategy[j];\n       \
        \     }\n            for (int j = i + k / 2; j < i + k; j++) {\n           \
        \     delta += prices[j] * strategy[j];\n            }\n            maxProfit\
        \ = Math.max(maxProfit, base + delta);\n        }\n        return maxProfit;\n\
        \    }\n}"
      python: "class Solution:\n    def maxProfit(self, prices: list[int], strategy:\
        \ list[int], k: int) -> int:\n        n = len(prices)\n        base = sum(p\
        \ * s for p, s in zip(prices, strategy))\n        max_profit = base\n      \
        \  for i in range(n - k + 1):\n            delta = 0\n            for j in range(i,\
        \ i + k // 2):\n                delta -= prices[j] * strategy[j]\n         \
        \   for j in range(i + k // 2, i + k):\n                delta += prices[j] *\
        \ strategy[j]\n            max_profit = max(max_profit, base + delta)\n    \
        \    return max_profit"
      python3: "class Solution:\n    def maxProfit(self, prices: list[int], strategy:\
        \ list[int], k: int) -> int:\n        n = len(prices)\n        base = sum(p\
        \ * s for p, s in zip(prices, strategy))\n        max_profit = base\n      \
        \  for i in range(n - k + 1):\n            delta = 0\n            for j in range(i,\
        \ i + k // 2):\n                delta -= prices[j] * strategy[j]\n         \
        \   for j in range(i + k // 2, i + k):\n                delta += prices[j] *\
        \ strategy[j]\n            max_profit = max(max_profit, base + delta)\n    \
        \    return max_profit"
      c: "typedef struct {\n    int* prices;\n    int pricesSize;\n    int* strategy;\n\
        \    int strategySize;\n    int k;\n} Input;\n\nint maxProfit(Input* input)\
        \ {\n    int n = input->pricesSize;\n    int base = 0;\n    for (int i = 0;\
        \ i < n; i++) {\n        base += input->prices[i] * input->strategy[i];\n  \
        \  }\n    int maxProfit = base;\n    for (int i = 0; i <= n - input->k; i++)\
        \ {\n        int delta = 0;\n        for (int j = i; j < i + input->k / 2; j++)\
        \ {\n            delta -= input->prices[j] * input->strategy[j];\n        }\n\
        \        for (int j = i + input->k / 2; j < i + input->k; j++) {\n         \
        \   delta += input->prices[j] * input->strategy[j];\n        }\n        maxProfit\
        \ = (maxProfit > base + delta) ? maxProfit : base + delta;\n    }\n    return\
        \ maxProfit;\n}"
      csharp: "public class Solution {\n    public int MaxProfit(int[] prices, int[]\
        \ strategy, int k) {\n        int n = prices.Length;\n        int baseProfit\
        \ = 0;\n        for (int i = 0; i < n; i++) {\n            baseProfit += prices[i]\
        \ * strategy[i];\n        }\n        int maxProfit = baseProfit;\n        for\
        \ (int i = 0; i <= n - k; i++) {\n            int delta = 0;\n            for\
        \ (int j = i; j < i + k / 2; j++) {\n                delta -= prices[j] * strategy[j];\n\
        \            }\n            for (int j = i + k / 2; j < i + k; j++) {\n    \
        \            delta += prices[j] * strategy[j];\n            }\n            maxProfit\
        \ = Math.Max(maxProfit, baseProfit + delta);\n        }\n        return maxProfit;\n\
        \    }\n}"
      javascript: "var maxProfit = function(prices, strategy, k) {\n    let n = prices.length;\n\
        \    let base = 0;\n    for (let i = 0; i < n; i++) {\n        base += prices[i]\
        \ * strategy[i];\n    }\n    let maxProfit = base;\n    for (let i = 0; i <=\
        \ n - k; i++) {\n        let delta = 0;\n        for (let j = i; j < i + k /\
        \ 2; j++) {\n            delta -= prices[j] * strategy[j];\n        }\n    \
        \    for (let j = i + k / 2; j < i + k; j++) {\n            delta += prices[j]\
        \ * strategy[j];\n        }\n        maxProfit = Math.max(maxProfit, base +\
        \ delta);\n    }\n    return maxProfit;\n};"
      typescript: "function maxProfit(prices: number[], strategy: number[], k: number):\
        \ number {\n    let n = prices.length;\n    let base = 0;\n    for (let i =\
        \ 0; i < n; i++) {\n        base += prices[i] * strategy[i];\n    }\n    let\
        \ maxProfit = base;\n    for (let i = 0; i <= n - k; i++) {\n        let delta\
        \ = 0;\n        for (let j = i; j < i + k / 2; j++) {\n            delta -=\
        \ prices[j] * strategy[j];\n        }\n        for (let j = i + k / 2; j < i\
        \ + k; j++) {\n            delta += prices[j] * strategy[j];\n        }\n  \
        \      maxProfit = Math.max(maxProfit, base + delta);\n    }\n    return maxProfit;\n\
        }"
      php: "class Solution {\n    function maxProfit($prices, $strategy, $k) {\n   \
        \     $n = count($prices);\n        $base = 0;\n        for ($i = 0; $i < $n;\
        \ $i++) {\n            $base += $prices[$i] * $strategy[$i];\n        }\n  \
        \      $maxProfit = $base;\n        for ($i = 0; $i <= $n - $k; $i++) {\n  \
        \          $delta = 0;\n            for ($j = $i; $j < $i + $k / 2; $j++) {\n\
        \                $delta -= $prices[$j] * $strategy[$j];\n            }\n   \
        \         for ($j = $i + $k / 2; $j < $i + $k; $j++) {\n                $delta\
        \ += $prices[$j] * $strategy[$j];\n            }\n            $maxProfit = max($maxProfit,\
        \ $base + $delta);\n        }\n        return $maxProfit;\n    }\n}"
      swift: "class Solution {\n    func maxProfit(_ prices: [Int], _ strategy: [Int],\
        \ _ k: Int) -> Int {\n        let n = prices.count\n        var base = 0\n \
        \       for i in 0..<n {\n            base += prices[i] * strategy[i]\n    \
        \    }\n        var maxProfit = base\n        for i in 0...n-k {\n         \
        \   var delta = 0\n            for j in i..<i+k/2 {\n                delta -=\
        \ prices[j] * strategy[j]\n            }\n            for j in i+k/2..<i+k {\n\
        \                delta += prices[j] * strategy[j]\n            }\n         \
        \   maxProfit = max(maxProfit, base + delta)\n        }\n        return maxProfit\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun maxProfit(prices: IntArray, strategy: IntArray,\
        \ k: Int): Int {\n        val n = prices.size\n        var base = 0\n      \
        \  for (i in 0 until n) {\n            base += prices[i] * strategy[i]\n   \
        \     }\n        var maxProfit = base\n        for (i in 0 until n - k + 1)\
        \ {\n            var delta = 0\n            for (j in i until i + k / 2) {\n\
        \                delta -= prices[j] * strategy[j]\n            }\n         \
        \   for (j in i + k / 2 until i + k) {\n                delta += prices[j] *\
        \ strategy[j]\n            }\n            maxProfit = maxOf(maxProfit, base\
        \ + delta)\n        }\n        return maxProfit\n    }\n}"
      dart: "class Solution {\n    int maxProfit(List<int> prices, List<int> strategy,\
        \ int k) {\n        int n = prices.length;\n        int base = 0;\n        for\
        \ (int i = 0; i < n; i++) {\n            base += prices[i] * strategy[i];\n\
        \        }\n        int maxProfit = base;\n        for (int i = 0; i <= n -\
        \ k; i++) {\n            int delta = 0;\n            for (int j = i; j < i +\
        \ k ~/ 2; j++) {\n                delta -= prices[j] * strategy[j];\n      \
        \      }\n            for (int j = i + k ~/ 2; j < i + k; j++) {\n         \
        \       delta += prices[j] * strategy[j];\n            }\n            maxProfit\
        \ = max(maxProfit, base + delta);\n        }\n        return maxProfit;\n  \
        \  }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\ntype Solution struct{}\n\nfunc\
        \ (s Solution) maxProfit(prices []int, strategy []int, k int) int {\n    n :=\
        \ len(prices)\n    base := 0\n    for i := 0; i < n; i++ {\n        base +=\
        \ prices[i] * strategy[i]\n    }\n    maxProfit := base\n    for i := 0; i <=\
        \ n-k; i++ {\n        delta := 0\n        for j := i; j < i+k/2; j++ {\n   \
        \         delta -= prices[j] * strategy[j]\n        }\n        for j := i +\
        \ k/2; j < i+k; j++ {\n            delta += prices[j] * strategy[j]\n      \
        \  }\n        if base+delta > maxProfit {\n            maxProfit = base + delta\n\
        \        }\n    }\n    return maxProfit\n}"
      ruby: "class Solution\n    def max_profit(prices, strategy, k)\n        n = prices.size\n\
        \        base = 0\n        n.times do |i|\n            base += prices[i] * strategy[i]\n\
        \        end\n        max_profit = base\n        (0..n-k).each do |i|\n    \
        \        delta = 0\n            (i...i+k/2).each do |j|\n                delta\
        \ -= prices[j] * strategy[j]\n            end\n            (i+k/2...i+k).each\
        \ do |j|\n                delta += prices[j] * strategy[j]\n            end\n\
        \            max_profit = [max_profit, base + delta].max\n        end\n    \
        \    max_profit\n    end\nend"
      scala: "object Solution {\n    def maxProfit(prices: Array[Int], strategy: Array[Int],\
        \ k: Int): Int = {\n        val n = prices.length\n        var base = 0\n  \
        \      for (i <- 0 until n) {\n            base += prices(i) * strategy(i)\n\
        \        }\n        var maxProfit = base\n        for (i <- 0 to n - k) {\n\
        \            var delta = 0\n            for (j <- i until i + k / 2) {\n   \
        \             delta -= prices(j) * strategy(j)\n            }\n            for\
        \ (j <- i + k / 2 until i + k) {\n                delta += prices(j) * strategy(j)\n\
        \            }\n            maxProfit = math.max(maxProfit, base + delta)\n\
        \        }\n        maxProfit\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn max_profit(prices: Vec<i32>,\
        \ strategy: Vec<i32>, k: i32) -> i32 {\n        let n = prices.len() as i32;\n\
        \        let mut base = 0;\n        for i in 0..n {\n            base += prices[i\
        \ as usize] * strategy[i as usize];\n        }\n        let mut max_profit =\
        \ base;\n        for i in 0..=n - k {\n            let mut delta = 0;\n    \
        \        for j in i..i + k / 2 {\n                delta -= prices[j as usize]\
        \ * strategy[j as usize];\n            }\n            for j in i + k / 2..i\
        \ + k {\n                delta += prices[j as usize] * strategy[j as usize];\n\
        \            }\n            max_profit = max_profit.max(base + delta);\n   \
        \     }\n        max_profit\n    }\n}"
      racket: "(define (max-profit prices strategy k)\n    (let ((n (length prices))\n\
        \          (base 0))\n        (do ((i 0 (+ i 1)))\n            ((= i n))\n \
        \           (set! base (+ base (* (list-ref prices i) (list-ref strategy i)))))\n\
        \        (let max-profit ((i 0))\n            (if (> i (- n k))\n          \
        \      base\n                (let ((delta 0))\n                    (do ((j i\
        \ (+ j 1)))\n                        ((= j (+ i (/ k 2))))\n               \
        \         (set! delta (- delta (* (list-ref prices j) (list-ref strategy j)))))\n\
        \                    (do ((j (+ i (/ k 2)) (+ j 1)))\n                     \
        \   ((= j (+ i k)))\n                        (set! delta (+ delta (* (list-ref\
        \ prices j) (list-ref strategy j)))))\n                    (max-profit (+ i\
        \ 1) (max base (+ base delta))))))))"
      erlang: "max_profit(Prices, Strategy, K) ->\n    N = length(Prices),\n    Base\
        \ = lists:foldl(fun({P, S}, Acc) -> Acc + P * S end, 0, lists:zip(Prices, Strategy)),\n\
        \    MaxProfit = lists:foldl(\n        fun(I, Max) ->\n            Delta = lists:foldl(\n\
        \                fun({P, S}, Acc) -> Acc - P * S end,\n                0,\n\
        \                lists:sublist(lists:zip(Prices, Strategy), I, K div 2)\n  \
        \          ) + lists:foldl(\n                fun({P, S}, Acc) -> Acc + P * S\
        \ end,\n                0,\n                lists:sublist(lists:zip(Prices,\
        \ Strategy), I + K div 2, K div 2)\n            ),\n            max(Max, Base\
        \ + Delta)\n        end,\n        Base,\n        lists:seq(0, N - K)\n    ),\n\
        \    MaxProfit."
      elixir: "def max_profit(prices, strategy, k) do\n    n = length(prices)\n    base\
        \ = Enum.reduce(Enum.zip(prices, strategy), 0, fn {p, s}, acc -> acc + p * s\
        \ end)\n    max_profit = Enum.reduce(0..n-k, base, fn i, max ->\n        delta\
        \ = Enum.reduce(Enum.slice(Enum.zip(prices, strategy), i, div(k, 2)), 0, fn\
        \ {p, s}, acc -> acc - p * s end) +\n               Enum.reduce(Enum.slice(Enum.zip(prices,\
        \ strategy), i + div(k, 2), div(k, 2)), 0, fn {p, s}, acc -> acc + p * s end)\n\
        \        max(max, base + delta)\n    end)\n    max_profit\nend"
    approach: The problem can be solved by iterating over all possible segments of length
      k in the strategy array and calculating the profit delta caused by replacing that
      segment. We can use prefix sums to precompute the base profit and to get fast
      range queries. The key intuition is to try every segment of length k and compute
      the profit delta caused by replacing that segment, then take the maximum of base
      + delta. This approach allows us to efficiently explore all possible modifications
      to the strategy array and find the one that results in the maximum profit.
    time_complexity: The time complexity of this solution is O(n*k), where n is the
      length of the prices array. This is because we are iterating over all possible
      segments of length k in the strategy array, and for each segment, we are calculating
      the profit delta caused by replacing that segment. The space complexity is O(n),
      which is used to store the prefix sums.
    space_complexity: The space complexity of this solution is O(n), which is used to
      store the prefix sums. We need to store the prefix sums of the prices array and
      the strategy array, which requires O(n) space. The rest of the space is used to
      store the input arrays and the output, which is also O(n).
    elapsed_time: 8.755109548568726
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-18 01:06:16 '
---

## Problem #3652: Best Time to Buy and Sell Stock using Strategy

**Difficulty:** Medium

**Topics:** Array, Sliding Window, Prefix Sum

## Problem Description

<p>You are given two integer arrays <code>prices</code> and <code>strategy</code>, where:</p>

<ul>
	<li><code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</li>
	<li><code>strategy[i]</code> represents a trading action on the <code>i<sup>th</sup></code> day, where:
	<ul>
		<li><code>-1</code> indicates buying one unit of the stock.</li>
		<li><code>0</code> indicates holding the stock.</li>
		<li><code>1</code> indicates selling one unit of the stock.</li>
	</ul>
	</li>
</ul>

<p>You are also given an <strong>even</strong> integer <code>k</code>, and may perform <strong>at most one</strong> modification to <code>strategy</code>. A modification consists of:</p>

<ul>
	<li>Selecting exactly <code>k</code> <strong>consecutive</strong> elements in <code>strategy</code>.</li>
	<li>Set the <strong>first</strong> <code>k / 2</code> elements to <code>0</code> (hold).</li>
	<li>Set the <strong>last</strong> <code>k / 2</code> elements to <code>1</code> (sell).</li>
</ul>

<p>The <strong>profit</strong> is defined as the <strong>sum</strong> of <code>strategy[i] * prices[i]</code> across all days.</p>

<p>Return the <strong>maximum</strong> possible profit you can achieve.</p>

<p><strong>Note:</strong> There are no constraints on budget or stock ownership, so all buy and sell operations are feasible regardless of past actions.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">prices = [4,2,8], strategy = [-1,0,1], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Modification</th>
			<th style="border: 1px solid black;">Strategy</th>
			<th style="border: 1px solid black;">Profit Calculation</th>
			<th style="border: 1px solid black;">Profit</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">Original</td>
			<td style="border: 1px solid black;">[-1, 0, 1]</td>
			<td style="border: 1px solid black;">(-1 &times; 4) + (0 &times; 2) + (1 &times; 8) = -4 + 0 + 8</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Modify [0, 1]</td>
			<td style="border: 1px solid black;">[0, 1, 1]</td>
			<td style="border: 1px solid black;">(0 &times; 4) + (1 &times; 2) + (1 &times; 8) = 0 + 2 + 8</td>
			<td style="border: 1px solid black;">10</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Modify [1, 2]</td>
			<td style="border: 1px solid black;">[-1, 0, 1]</td>
			<td style="border: 1px solid black;">(-1 &times; 4) + (0 &times; 2) + (1 &times; 8) = -4 + 0 + 8</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
	</tbody>
</table>

<p>Thus, the maximum possible profit is 10, which is achieved by modifying the subarray <code>[0, 1]</code>​​​​​​​.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">prices = [5,4,3], strategy = [1,1,0], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<div class="example-block">
<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Modification</th>
			<th style="border: 1px solid black;">Strategy</th>
			<th style="border: 1px solid black;">Profit Calculation</th>
			<th style="border: 1px solid black;">Profit</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">Original</td>
			<td style="border: 1px solid black;">[1, 1, 0]</td>
			<td style="border: 1px solid black;">(1 &times; 5) + (1 &times; 4) + (0 &times; 3) = 5 + 4 + 0</td>
			<td style="border: 1px solid black;">9</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Modify [0, 1]</td>
			<td style="border: 1px solid black;">[0, 1, 0]</td>
			<td style="border: 1px solid black;">(0 &times; 5) + (1 &times; 4) + (0 &times; 3) = 0 + 4 + 0</td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">Modify [1, 2]</td>
			<td style="border: 1px solid black;">[1, 0, 1]</td>
			<td style="border: 1px solid black;">(1 &times; 5) + (0 &times; 4) + (1 &times; 3) = 5 + 0 + 3</td>
			<td style="border: 1px solid black;">8</td>
		</tr>
	</tbody>
</table>

<p>Thus, the maximum possible profit is 9, which is achieved without any modification.</p>
</div>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= prices.length == strategy.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>-1 &lt;= strategy[i] &lt;= 1</code></li>
	<li><code>2 &lt;= k &lt;= prices.length</code></li>
	<li><code>k</code> is even</li>
</ul>


## Hints

1. Use prefix sums to precompute the base profit and to get fast range queries (sums of `prices` and counts of each `strategy` value over any interval).

2. Try every segment of length `k`: compute the profit delta caused by replacing that segment (using the prefix queries) and take the maximum of `base + delta`.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-18 01:06:07 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the maximum profit achievable by either keeping the original trading strategy or applying at most one specific modification to a contiguous segment of the strategy. The profit is calculated as the sum of `strategy[i] * prices[i]` for all days. A modification involves selecting a `k`-length segment, setting its first `k/2` elements to `0` (hold), and its last `k/2` elements to `1` (sell).

The core idea is to first calculate the total profit with the original strategy. Then, we iterate through all possible contiguous segments of length `k` where a modification could be applied. For each such segment, we calculate the change in profit that would result from applying the modification. This change (delta) is added to the original total profit, and we keep track of the maximum profit found across all these scenarios. To efficiently calculate segment sums and the profit delta, we use prefix sum arrays. One prefix sum array stores the cumulative sum of `strategy[i] * prices[i]`, and another stores the cumulative sum of `prices[i]`. These allow us to query any segment sum in O(1) time.

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
    long long maxProfit(std::vector<int>& prices, std::vector<int>& strategy, int k) {
        int n = prices.size();

        std::vector<long long> prefixOriginalProfit(n + 1, 0);
        std::vector<long long> prefixPricesSum(n + 1, 0);

        for (int i = 0; i < n; ++i) {
            prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + (long long)strategy[i] * prices[i];
            prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i];
        }

        long long maxProfitVal = prefixOriginalProfit[n];

        for (int j = 0; j <= n - k; ++j) {
            long long originalSegmentProfit = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];

            long long modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2];

            long long delta = modifiedSegmentProfit - originalSegmentProfit;

            maxProfitVal = std::max(maxProfitVal, prefixOriginalProfit[n] + delta);
        }

        return maxProfitVal;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public long maxProfit(int[] prices, int[] strategy, int k) {
        int n = prices.length;

        long[] prefixOriginalProfit = new long[n + 1];
        long[] prefixPricesSum = new long[n + 1];

        for (int i = 0; i < n; ++i) {
            prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + (long)strategy[i] * prices[i];
            prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i];
        }

        long maxProfitVal = prefixOriginalProfit[n];

        for (int j = 0; j <= n - k; ++j) {
            long originalSegmentProfit = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];

            long modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2];

            long delta = modifiedSegmentProfit - originalSegmentProfit;

            maxProfitVal = Math.max(maxProfitVal, prefixOriginalProfit[n] + delta);
        }

        return maxProfitVal;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        prefix_original_profit = [0] * (n + 1)
        prefix_prices_sum = [0] * (n + 1)

        for i in range(n):
            prefix_original_profit[i+1] = prefix_original_profit[i] + strategy[i] * prices[i]
            prefix_prices_sum[i+1] = prefix_prices_sum[i] + prices[i]

        max_profit = prefix_original_profit[n]

        for j in range(n - k + 1):
            original_segment_profit = prefix_original_profit[j+k] - prefix_original_profit[j]

            modified_segment_profit = prefix_prices_sum[j+k] - prefix_prices_sum[j + k // 2]

            delta = modified_segment_profit - original_segment_profit

            max_profit = max(max_profit, prefix_original_profit[n] + delta)

        return max_profit
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        prefix_original_profit = [0] * (n + 1)
        prefix_prices_sum = [0] * (n + 1)

        for i in range(n):
            prefix_original_profit[i+1] = prefix_original_profit[i] + strategy[i] * prices[i]
            prefix_prices_sum[i+1] = prefix_prices_sum[i] + prices[i]

        max_profit = prefix_original_profit[n]

        for j in range(n - k + 1):
            original_segment_profit = prefix_original_profit[j+k] - prefix_original_profit[j]

            modified_segment_profit = prefix_prices_sum[j+k] - prefix_prices_sum[j + k // 2]

            delta = modified_segment_profit - original_segment_profit

            max_profit = max(max_profit, prefix_original_profit[n] + delta)

        return max_profit
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long maxProfit(int* prices, int pricesSize, int* strategy, int strategySize, int k) {
    int n = pricesSize;

    long long* prefixOriginalProfit = (long long*)calloc(n + 1, sizeof(long long));
    long long* prefixPricesSum = (long long*)calloc(n + 1, sizeof(long long));

    for (int i = 0; i < n; ++i) {
        prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + (long long)strategy[i] * prices[i];
        prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i];
    }

    long long maxProfitVal = prefixOriginalProfit[n];

    for (int j = 0; j <= n - k; ++j) {
        long long originalSegmentProfit = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];

        long long modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2];

        long long delta = modifiedSegmentProfit - originalSegmentProfit;

        if (prefixOriginalProfit[n] + delta > maxProfitVal) {
            maxProfitVal = prefixOriginalProfit[n] + delta;
        }
    }

    free(prefixOriginalProfit);
    free(prefixPricesSum);

    return maxProfitVal;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public long MaxProfit(int[] prices, int[] strategy, int k) {
        int n = prices.Length;

        long[] prefixOriginalProfit = new long[n + 1];
        long[] prefixPricesSum = new long[n + 1];

        for (int i = 0; i < n; ++i) {
            prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + (long)strategy[i] * prices[i];
            prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i];
        }

        long maxProfitVal = prefixOriginalProfit[n];

        for (int j = 0; j <= n - k; ++j) {
            long originalSegmentProfit = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];

            long modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2];

            long delta = modifiedSegmentProfit - originalSegmentProfit;

            maxProfitVal = Math.Max(maxProfitVal, prefixOriginalProfit[n] + delta);
        }

        return maxProfitVal;
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
 * @param {number[]} strategy
 * @param {number} k
 * @return {number}
 */
var maxProfit = function(prices, strategy, k) {
    const n = prices.length;

    const prefixOriginalProfit = new Array(n + 1).fill(0);
    const prefixPricesSum = new Array(n + 1).fill(0);

    for (let i = 0; i < n; ++i) {
        prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + strategy[i] * prices[i];
        prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i];
    }

    let maxProfitVal = prefixOriginalProfit[n];

    for (let j = 0; j <= n - k; ++j) {
        const originalSegmentProfit = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];

        const modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2];

        const delta = modifiedSegmentProfit - originalSegmentProfit;

        maxProfitVal = Math.max(maxProfitVal, prefixOriginalProfit[n] + delta);
    }

    return maxProfitVal;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxProfit(prices: number[], strategy: number[], k: number): number {
    const n = prices.length;

    const prefixOriginalProfit: number[] = new Array(n + 1).fill(0);
    const prefixPricesSum: number[] = new Array(n + 1).fill(0);

    for (let i = 0; i < n; ++i) {
        prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + strategy[i] * prices[i];
        prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i];
    }

    let maxProfitVal: number = prefixOriginalProfit[n];

    for (let j = 0; j <= n - k; ++j) {
        const originalSegmentProfit: number = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];

        const modifiedSegmentProfit: number = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2];

        const delta: number = modifiedSegmentProfit - originalSegmentProfit;

        maxProfitVal = Math.max(maxProfitVal, prefixOriginalProfit[n] + delta);
    }

    return maxProfitVal;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer[] $prices
     * @param Integer[] $strategy
     * @param Integer $k
     * @return Integer
     */
    function maxProfit($prices, $strategy, $k) {
        $n = count($prices);

        $prefixOriginalProfit = array_fill(0, $n + 1, 0);
        $prefixPricesSum = array_fill(0, $n + 1, 0);

        for ($i = 0; $i < $n; ++$i) {
            $prefixOriginalProfit[$i+1] = $prefixOriginalProfit[$i] + $strategy[$i] * $prices[$i];
            $prefixPricesSum[$i+1] = $prefixPricesSum[$i] + $prices[$i];
        }

        $maxProfitVal = $prefixOriginalProfit[$n];

        for ($j = 0; $j <= $n - $k; ++$j) {
            $originalSegmentProfit = $prefixOriginalProfit[$j+$k] - $prefixOriginalProfit[$j];

            $modifiedSegmentProfit = $prefixPricesSum[$j+$k] - $prefixPricesSum[$j + $k / 2];

            $delta = $modifiedSegmentProfit - $originalSegmentProfit;

            $maxProfitVal = max($maxProfitVal, $prefixOriginalProfit[$n] + $delta);
        }

        return $maxProfitVal;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func maxProfit(_ prices: [Int], _ strategy: [Int], _ k: Int) -> Int {
        let n = prices.count

        var prefixOriginalProfit = Array(repeating: 0, count: n + 1)
        var prefixPricesSum = Array(repeating: 0, count: n + 1)

        for i in 0..<n {
            prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + strategy[i] * prices[i]
            prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i]
        }

        var maxProfitVal = prefixOriginalProfit[n]

        for j in 0...(n - k) {
            let originalSegmentProfit = prefixOriginalProfit[j+k] - prefixOriginalProfit[j]

            let modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2]

            let delta = modifiedSegmentProfit - originalSegmentProfit

            maxProfitVal = max(maxProfitVal, prefixOriginalProfit[n] + delta)
        }

        return maxProfitVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.max

class Solution {
    fun maxProfit(prices: IntArray, strategy: IntArray, k: Int): Long {
        val n = prices.size

        val prefixOriginalProfit = LongArray(n + 1)
        val prefixPricesSum = LongArray(n + 1)

        for (i in 0 until n) {
            prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + strategy[i].toLong() * prices[i]
            prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i].toLong()
        }

        var maxProfitVal = prefixOriginalProfit[n]

        for (j in 0..(n - k)) {
            val originalSegmentProfit = prefixOriginalProfit[j+k] - prefixOriginalProfit[j]

            val modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j + k / 2]

            val delta = modifiedSegmentProfit - originalSegmentProfit

            maxProfitVal = max(maxProfitVal, prefixOriginalProfit[n] + delta)
        }

        return maxProfitVal
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
  int maxProfit(List<int> prices, List<int> strategy, int k) {
    int n = prices.length;

    List<int> prefixOriginalProfit = List<int>.filled(n + 1, 0);
    List<int> prefixPricesSum = List<int>.filled(n + 1, 0);

    for (int i = 0; i < n; ++i) {
      prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + strategy[i] * prices[i];
      prefixPricesSum[i+1] = prefixPricesSum[i] + prices[i];
    }

    int maxProfitVal = prefixOriginalProfit[n];

    for (int j = 0; j <= n - k; ++j) {
      int originalSegmentProfit = prefixOriginalProfit[j+k] - prefixOriginalProfit[j];

      int modifiedSegmentProfit = prefixPricesSum[j+k] - prefixPricesSum[j + k ~/ 2];

      int delta = modifiedSegmentProfit - originalSegmentProfit;

      maxProfitVal = max(maxProfitVal, prefixOriginalProfit[n] + delta);
    }

    return maxProfitVal;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
	"math"
)

func maxProfit(prices []int, strategy []int, k int) int64 {
    n := len(prices)

    prefixOriginalProfit := make([]int64, n + 1)
    prefixPricesSum := make([]int64, n + 1)

    for i := 0; i < n; i++ {
        prefixOriginalProfit[i+1] = prefixOriginalProfit[i] + int64(strategy[i]) * int64(prices[i])
        prefixPricesSum[i+1] = prefixPricesSum[i] + int64(prices[i])
    }

    maxProfitVal := prefixOriginalProfit[n]

    for j := 0; j <= n - k; j++ {
        originalSegmentProfit := prefixOriginalProfit[j+k] - prefixOriginalProfit[j]

        modifiedSegmentProfit := prefixPricesSum[j+k] - prefixPricesSum[j + k / 2]

        delta := modifiedSegmentProfit - originalSegmentProfit;

        maxProfitVal = int64(math.Max(float64(maxProfitVal), float64(prefixOriginalProfit[n] + delta)))
    }

    return maxProfitVal
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} prices
# @param {Integer[]} strategy
# @param {Integer} k
# @return {Integer}
def max_profit(prices, strategy, k)
    n = prices.length

    prefix_original_profit = Array.new(n + 1, 0)
    prefix_prices_sum = Array.new(n + 1, 0)

    (0...n).each do |i|
        prefix_original_profit[i+1] = prefix_original_profit[i] + strategy[i] * prices[i]
        prefix_prices_sum[i+1] = prefix_prices_sum[i] + prices[i]
    end

    max_profit_val = prefix_original_profit[n]

    (0..n - k).each do |j|
        original_segment_profit = prefix_original_profit[j+k] - prefix_original_profit[j]

        modified_segment_profit = prefix_prices_sum[j+k] - prefix_prices_sum[j + k / 2]

        delta = modified_segment_profit - original_segment_profit

        max_profit_val = [max_profit_val, prefix_original_profit[n] + delta].max
    end

    return max_profit_val
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer
import scala.math.max

object Solution {
    def maxProfit(prices: Array[Int], strategy: Array[Int], k: Int): Long = {
        val n = prices.length

        val prefixOriginalProfit = Array.fill[Long](n + 1)(0L)
        val prefixPricesSum = Array.fill[Long](n + 1)(0L)

        for (i <- 0 until n) {
            prefixOriginalProfit(i+1) = prefixOriginalProfit(i) + strategy(i).toLong * prices(i)
            prefixPricesSum(i+1) = prefixPricesSum(i) + prices(i).toLong
        }

        var maxProfitVal = prefixOriginalProfit(n)

        for (j <- 0 to n - k) {
            val originalSegmentProfit = prefixOriginalProfit(j+k) - prefixOriginalProfit(j)

            val modifiedSegmentProfit = prefixPricesSum(j+k) - prefixPricesSum(j + k / 2)

            val delta = modifiedSegmentProfit - originalSegmentProfit

            maxProfitVal = max(maxProfitVal, prefixOriginalProfit(n) + delta)
        }

        maxProfitVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_profit(prices: Vec<i32>, strategy: Vec<i32>, k: i32) -> i64 {
        let n = prices.len();
        let k_usize = k as usize;

        let mut prefix_original_profit: Vec<i64> = vec![0; n + 1];
        let mut prefix_prices_sum: Vec<i64> = vec![0; n + 1];

        for i in 0..n {
            prefix_original_profit[i+1] = prefix_original_profit[i] + (strategy[i] as i64) * (prices[i] as i64);
            prefix_prices_sum[i+1] = prefix_prices_sum[i] + (prices[i] as i64);
        }

        let mut max_profit_val: i64 = prefix_original_profit[n];

        for j in 0..=(n - k_usize) {
            let original_segment_profit = prefix_original_profit[j+k_usize] - prefix_original_profit[j];

            let modified_segment_profit = prefix_prices_sum[j+k_usize] - prefix_prices_sum[j + k_usize / 2];

            let delta = modified_segment_profit - original_segment_profit;

            max_profit_val = max_profit_val.max(prefix_original_profit[n] + delta);
        }

        max_profit_val
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (max-profit prices strategy k)
  (define n (vector-length prices))

  (define prefix-original-profit (make-vector (+ n 1) 0))
  (define prefix-prices-sum (make-vector (+ n 1) 0))

  (for ([i (in-range n)])
    (vector-set! prefix-original-profit (+ i 1)
                 (+ (vector-ref prefix-original-profit i)
                    (* (vector-ref strategy i) (vector-ref prices i))))
    (vector-set! prefix-prices-sum (+ i 1)
                 (+ (vector-ref prefix-prices-sum i)
                    (vector-ref prices i))))

  (define max-profit-val (vector-ref prefix-original-profit n))

  (for ([j (in-range (- n k) (+ 1 (- n k)))])
    (define original-segment-profit (- (vector-ref prefix-original-profit (+ j k))
                                       (vector-ref prefix-original-profit j)))

    (define modified-segment-profit (- (vector-ref prefix-prices-sum (+ j k))
                                       (vector-ref prefix-prices-sum (+ j (quotient k 2)))))

    (define delta (- modified-segment-profit original-segment-profit))

    (set! max-profit-val (max max-profit-val (+ (vector-ref prefix-original-profit n) delta))))

  max-profit-val)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([max_profit/3]).

max_profit(Prices, Strategy, K) ->
    N = length(Prices),

    PricesTuple = list_to_tuple(Prices),
    StrategyTuple = list_to_tuple(Strategy),

    {_, PrefixOriginalProfitList} = lists:mapaccum(
        fun(I, AccSum) ->
            Val = element(I+1, StrategyTuple) * element(I+1, PricesTuple),
            NewSum = AccSum + Val,
            {NewSum, NewSum}
        end,
        0,
        lists:seq(0, N-1)
    ),
    PrefixOriginalProfitTuple = list_to_tuple([0 | PrefixOriginalProfitList]),

    {_, PrefixPricesSumList} = lists:mapaccum(
        fun(I, AccSum) ->
            Val = element(I+1, PricesTuple),
            NewSum = AccSum + Val,
            {NewSum, NewSum}
        end,
        0,
        lists:seq(0, N-1)
    ),
    PrefixPricesSumTuple = list_to_tuple([0 | PrefixPricesSumList]),

    MaxProfitVal = element(N + 1, PrefixOriginalProfitTuple),

    lists:foldl(
        fun(J, CurrentMaxProfit) ->
            J_1_indexed = J + 1,
            K_half = K div 2,

            OriginalSegmentProfit = element(J_1_indexed + K, PrefixOriginalProfitTuple) - element(J_1_indexed, PrefixOriginalProfitTuple),

            ModifiedSegmentProfit = element(J_1_indexed + K, PrefixPricesSumTuple) - element(J_1_indexed + K_half, PrefixPricesSumTuple),

            Delta = ModifiedSegmentProfit - OriginalSegmentProfit,

            max(CurrentMaxProfit, element(N + 1, PrefixOriginalProfitTuple) + Delta)
        end,
        MaxProfitVal,
        lists:seq(0, N - K)
    ).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_profit(prices :: [integer], strategy :: [integer], k :: integer) :: integer
  def max_profit(prices, strategy, k) do
    n = length(prices)

    prices_tuple = List.to_tuple(prices)
    strategy_tuple = List.to_tuple(strategy)

    {_, prefix_original_profit_list} = 
      Enum.map_reduce(0..(n-1), 0, fn i, acc_sum ->
        val = elem(strategy_tuple, i) * elem(prices_tuple, i)
        new_sum = acc_sum + val
        {new_sum, new_sum}
      end)
    prefix_original_profit_tuple = List.to_tuple([0 | prefix_original_profit_list])

    {_, prefix_prices_sum_list} = 
      Enum.map_reduce(0..(n-1), 0, fn i, acc_sum ->
        val = elem(prices_tuple, i)
        new_sum = acc_sum + val
        {new_sum, new_sum}
      end)
    prefix_prices_sum_tuple = List.to_tuple([0 | prefix_prices_sum_list])

    max_profit_val = elem(prefix_original_profit_tuple, n)

    Enum.reduce(0..(n - k), max_profit_val, fn j, current_max_profit ->
      original_segment_profit = elem(prefix_original_profit_tuple, j + k) - elem(prefix_original_profit_tuple, j)

      modified_segment_profit = elem(prefix_prices_sum_tuple, j + k) - elem(prefix_prices_sum_tuple, j + div(k, 2))

      delta = modified_segment_profit - original_segment_profit

      max(current_max_profit, elem(prefix_original_profit_tuple, n) + delta)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the length of the `prices` and `strategy` arrays. This is because we iterate through the arrays once to build the two prefix sum arrays (O(N)), and then we iterate at most N-k+1 times (which is O(N)) to consider all possible `k`-length segments for modification. Each calculation within the loop takes constant time using the precomputed prefix sums.

- **Space Complexity:** The space complexity is O(N), where N is the length of the `prices` and `strategy` arrays. This is due to storing two prefix sum arrays, `prefix_original_profit` and `prefix_prices_sum`, each of size N+1. No other data structures grow with the input size.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-18 01:06:16 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over all possible segments of length k in the strategy array and calculating the profit delta caused by replacing that segment. We can use prefix sums to precompute the base profit and to get fast range queries. The key intuition is to try every segment of length k and compute the profit delta caused by replacing that segment, then take the maximum of base + delta. This approach allows us to efficiently explore all possible modifications to the strategy array and find the one that results in the maximum profit.

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
    int maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        int n = prices.size();
        int base = 0;
        for (int i = 0; i < n; i++) {
            base += prices[i] * strategy[i];
        }
        int max_profit = base;
        for (int i = 0; i <= n - k; i++) {
            int delta = 0;
            for (int j = i; j < i + k / 2; j++) {
                delta -= prices[j] * strategy[j];
            }
            for (int j = i + k / 2; j < i + k; j++) {
                delta += prices[j] * strategy[j];
            }
            max_profit = max(max_profit, base + delta);
        }
        return max_profit;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxProfit(int[] prices, int[] strategy, int k) {
        int n = prices.length;
        int base = 0;
        for (int i = 0; i < n; i++) {
            base += prices[i] * strategy[i];
        }
        int maxProfit = base;
        for (int i = 0; i <= n - k; i++) {
            int delta = 0;
            for (int j = i; j < i + k / 2; j++) {
                delta -= prices[j] * strategy[j];
            }
            for (int j = i + k / 2; j < i + k; j++) {
                delta += prices[j] * strategy[j];
            }
            maxProfit = Math.max(maxProfit, base + delta);
        }
        return maxProfit;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        n = len(prices)
        base = sum(p * s for p, s in zip(prices, strategy))
        max_profit = base
        for i in range(n - k + 1):
            delta = 0
            for j in range(i, i + k // 2):
                delta -= prices[j] * strategy[j]
            for j in range(i + k // 2, i + k):
                delta += prices[j] * strategy[j]
            max_profit = max(max_profit, base + delta)
        return max_profit
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxProfit(self, prices: list[int], strategy: list[int], k: int) -> int:
        n = len(prices)
        base = sum(p * s for p, s in zip(prices, strategy))
        max_profit = base
        for i in range(n - k + 1):
            delta = 0
            for j in range(i, i + k // 2):
                delta -= prices[j] * strategy[j]
            for j in range(i + k // 2, i + k):
                delta += prices[j] * strategy[j]
            max_profit = max(max_profit, base + delta)
        return max_profit
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int* prices;
    int pricesSize;
    int* strategy;
    int strategySize;
    int k;
} Input;

int maxProfit(Input* input) {
    int n = input->pricesSize;
    int base = 0;
    for (int i = 0; i < n; i++) {
        base += input->prices[i] * input->strategy[i];
    }
    int maxProfit = base;
    for (int i = 0; i <= n - input->k; i++) {
        int delta = 0;
        for (int j = i; j < i + input->k / 2; j++) {
            delta -= input->prices[j] * input->strategy[j];
        }
        for (int j = i + input->k / 2; j < i + input->k; j++) {
            delta += input->prices[j] * input->strategy[j];
        }
        maxProfit = (maxProfit > base + delta) ? maxProfit : base + delta;
    }
    return maxProfit;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxProfit(int[] prices, int[] strategy, int k) {
        int n = prices.Length;
        int baseProfit = 0;
        for (int i = 0; i < n; i++) {
            baseProfit += prices[i] * strategy[i];
        }
        int maxProfit = baseProfit;
        for (int i = 0; i <= n - k; i++) {
            int delta = 0;
            for (int j = i; j < i + k / 2; j++) {
                delta -= prices[j] * strategy[j];
            }
            for (int j = i + k / 2; j < i + k; j++) {
                delta += prices[j] * strategy[j];
            }
            maxProfit = Math.Max(maxProfit, baseProfit + delta);
        }
        return maxProfit;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxProfit = function(prices, strategy, k) {
    let n = prices.length;
    let base = 0;
    for (let i = 0; i < n; i++) {
        base += prices[i] * strategy[i];
    }
    let maxProfit = base;
    for (let i = 0; i <= n - k; i++) {
        let delta = 0;
        for (let j = i; j < i + k / 2; j++) {
            delta -= prices[j] * strategy[j];
        }
        for (let j = i + k / 2; j < i + k; j++) {
            delta += prices[j] * strategy[j];
        }
        maxProfit = Math.max(maxProfit, base + delta);
    }
    return maxProfit;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxProfit(prices: number[], strategy: number[], k: number): number {
    let n = prices.length;
    let base = 0;
    for (let i = 0; i < n; i++) {
        base += prices[i] * strategy[i];
    }
    let maxProfit = base;
    for (let i = 0; i <= n - k; i++) {
        let delta = 0;
        for (let j = i; j < i + k / 2; j++) {
            delta -= prices[j] * strategy[j];
        }
        for (let j = i + k / 2; j < i + k; j++) {
            delta += prices[j] * strategy[j];
        }
        maxProfit = Math.max(maxProfit, base + delta);
    }
    return maxProfit;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxProfit($prices, $strategy, $k) {
        $n = count($prices);
        $base = 0;
        for ($i = 0; $i < $n; $i++) {
            $base += $prices[$i] * $strategy[$i];
        }
        $maxProfit = $base;
        for ($i = 0; $i <= $n - $k; $i++) {
            $delta = 0;
            for ($j = $i; $j < $i + $k / 2; $j++) {
                $delta -= $prices[$j] * $strategy[$j];
            }
            for ($j = $i + $k / 2; $j < $i + $k; $j++) {
                $delta += $prices[$j] * $strategy[$j];
            }
            $maxProfit = max($maxProfit, $base + $delta);
        }
        return $maxProfit;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxProfit(_ prices: [Int], _ strategy: [Int], _ k: Int) -> Int {
        let n = prices.count
        var base = 0
        for i in 0..<n {
            base += prices[i] * strategy[i]
        }
        var maxProfit = base
        for i in 0...n-k {
            var delta = 0
            for j in i..<i+k/2 {
                delta -= prices[j] * strategy[j]
            }
            for j in i+k/2..<i+k {
                delta += prices[j] * strategy[j]
            }
            maxProfit = max(maxProfit, base + delta)
        }
        return maxProfit
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxProfit(prices: IntArray, strategy: IntArray, k: Int): Int {
        val n = prices.size
        var base = 0
        for (i in 0 until n) {
            base += prices[i] * strategy[i]
        }
        var maxProfit = base
        for (i in 0 until n - k + 1) {
            var delta = 0
            for (j in i until i + k / 2) {
                delta -= prices[j] * strategy[j]
            }
            for (j in i + k / 2 until i + k) {
                delta += prices[j] * strategy[j]
            }
            maxProfit = maxOf(maxProfit, base + delta)
        }
        return maxProfit
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int maxProfit(List<int> prices, List<int> strategy, int k) {
        int n = prices.length;
        int base = 0;
        for (int i = 0; i < n; i++) {
            base += prices[i] * strategy[i];
        }
        int maxProfit = base;
        for (int i = 0; i <= n - k; i++) {
            int delta = 0;
            for (int j = i; j < i + k ~/ 2; j++) {
                delta -= prices[j] * strategy[j];
            }
            for (int j = i + k ~/ 2; j < i + k; j++) {
                delta += prices[j] * strategy[j];
            }
            maxProfit = max(maxProfit, base + delta);
        }
        return maxProfit;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
    "fmt"
)

type Solution struct{}

func (s Solution) maxProfit(prices []int, strategy []int, k int) int {
    n := len(prices)
    base := 0
    for i := 0; i < n; i++ {
        base += prices[i] * strategy[i]
    }
    maxProfit := base
    for i := 0; i <= n-k; i++ {
        delta := 0
        for j := i; j < i+k/2; j++ {
            delta -= prices[j] * strategy[j]
        }
        for j := i + k/2; j < i+k; j++ {
            delta += prices[j] * strategy[j]
        }
        if base+delta > maxProfit {
            maxProfit = base + delta
        }
    }
    return maxProfit
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def max_profit(prices, strategy, k)
        n = prices.size
        base = 0
        n.times do |i|
            base += prices[i] * strategy[i]
        end
        max_profit = base
        (0..n-k).each do |i|
            delta = 0
            (i...i+k/2).each do |j|
                delta -= prices[j] * strategy[j]
            end
            (i+k/2...i+k).each do |j|
                delta += prices[j] * strategy[j]
            end
            max_profit = [max_profit, base + delta].max
        end
        max_profit
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxProfit(prices: Array[Int], strategy: Array[Int], k: Int): Int = {
        val n = prices.length
        var base = 0
        for (i <- 0 until n) {
            base += prices(i) * strategy(i)
        }
        var maxProfit = base
        for (i <- 0 to n - k) {
            var delta = 0
            for (j <- i until i + k / 2) {
                delta -= prices(j) * strategy(j)
            }
            for (j <- i + k / 2 until i + k) {
                delta += prices(j) * strategy(j)
            }
            maxProfit = math.max(maxProfit, base + delta)
        }
        maxProfit
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
    pub fn max_profit(prices: Vec<i32>, strategy: Vec<i32>, k: i32) -> i32 {
        let n = prices.len() as i32;
        let mut base = 0;
        for i in 0..n {
            base += prices[i as usize] * strategy[i as usize];
        }
        let mut max_profit = base;
        for i in 0..=n - k {
            let mut delta = 0;
            for j in i..i + k / 2 {
                delta -= prices[j as usize] * strategy[j as usize];
            }
            for j in i + k / 2..i + k {
                delta += prices[j as usize] * strategy[j as usize];
            }
            max_profit = max_profit.max(base + delta);
        }
        max_profit
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (max-profit prices strategy k)
    (let ((n (length prices))
          (base 0))
        (do ((i 0 (+ i 1)))
            ((= i n))
            (set! base (+ base (* (list-ref prices i) (list-ref strategy i)))))
        (let max-profit ((i 0))
            (if (> i (- n k))
                base
                (let ((delta 0))
                    (do ((j i (+ j 1)))
                        ((= j (+ i (/ k 2))))
                        (set! delta (- delta (* (list-ref prices j) (list-ref strategy j)))))
                    (do ((j (+ i (/ k 2)) (+ j 1)))
                        ((= j (+ i k)))
                        (set! delta (+ delta (* (list-ref prices j) (list-ref strategy j)))))
                    (max-profit (+ i 1) (max base (+ base delta))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_profit(Prices, Strategy, K) ->
    N = length(Prices),
    Base = lists:foldl(fun({P, S}, Acc) -> Acc + P * S end, 0, lists:zip(Prices, Strategy)),
    MaxProfit = lists:foldl(
        fun(I, Max) ->
            Delta = lists:foldl(
                fun({P, S}, Acc) -> Acc - P * S end,
                0,
                lists:sublist(lists:zip(Prices, Strategy), I, K div 2)
            ) + lists:foldl(
                fun({P, S}, Acc) -> Acc + P * S end,
                0,
                lists:sublist(lists:zip(Prices, Strategy), I + K div 2, K div 2)
            ),
            max(Max, Base + Delta)
        end,
        Base,
        lists:seq(0, N - K)
    ),
    MaxProfit.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def max_profit(prices, strategy, k) do
    n = length(prices)
    base = Enum.reduce(Enum.zip(prices, strategy), 0, fn {p, s}, acc -> acc + p * s end)
    max_profit = Enum.reduce(0..n-k, base, fn i, max ->
        delta = Enum.reduce(Enum.slice(Enum.zip(prices, strategy), i, div(k, 2)), 0, fn {p, s}, acc -> acc - p * s end) +
               Enum.reduce(Enum.slice(Enum.zip(prices, strategy), i + div(k, 2), div(k, 2)), 0, fn {p, s}, acc -> acc + p * s end)
        max(max, base + delta)
    end)
    max_profit
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n*k), where n is the length of the prices array. This is because we are iterating over all possible segments of length k in the strategy array, and for each segment, we are calculating the profit delta caused by replacing that segment. The space complexity is O(n), which is used to store the prefix sums.

- **Space Complexity:** The space complexity of this solution is O(n), which is used to store the prefix sums. We need to store the prefix sums of the prices array and the strategy array, which requires O(n) space. The rest of the space is used to store the input arrays and the output, which is also O(n).

</div>
</details>
