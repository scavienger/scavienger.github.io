---
layout: post
title: "Maximum Number of Items From Sale I"
date: 2026-11-27 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming", "Greedy"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-number-of-items-from-sale-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maximumSaleItems(vector<vector<int>>&\
        \ items, int budget) {\n        int maxFactor = 0;\n        int minPrice = 1e9;\n\
        \        for (const auto& item : items) {\n            maxFactor = max(maxFactor,\
        \ item[0]);\n            minPrice = min(minPrice, item[1]);\n        }\n\n \
        \       vector<int> freq(maxFactor + 1, 0);\n        for (const auto& item :\
        \ items) {\n            freq[item[0]]++;\n        }\n\n        vector<int> count(maxFactor\
        \ + 1, 0);\n        for (int i = 1; i <= maxFactor; ++i) {\n            for\
        \ (int j = i; j <= maxFactor; j += i) {\n                count[i] += freq[j];\n\
        \            }\n        }\n\n        vector<int> dp(budget + 1, -1);\n     \
        \   dp[0] = 0;\n\n        for (const auto& item : items) {\n            int\
        \ f = item[0];\n            int p = item[1];\n            int val = count[f];\n\
        \            for (int w = budget; w >= p; --w) {\n                if (dp[w -\
        \ p] != -1) {\n                    dp[w] = max(dp[w], dp[w - p] + val);\n  \
        \              }\n            }\n        }\n\n        int maxItems = 0;\n  \
        \      for (int w = 0; w <= budget; ++w) {\n            if (dp[w] != -1) {\n\
        \                int total = dp[w] + (budget - w) / minPrice;\n            \
        \    maxItems = max(maxItems, total);\n            }\n        }\n\n        return\
        \ maxItems;\n    }\n};"
      java: "class Solution {\n    public int maximumSaleItems(int[][] items, int budget)\
        \ {\n        int maxFactor = 0;\n        int minPrice = Integer.MAX_VALUE;\n\
        \        for (int[] item : items) {\n            maxFactor = Math.max(maxFactor,\
        \ item[0]);\n            minPrice = Math.min(minPrice, item[1]);\n        }\n\
        \n        int[] freq = new int[maxFactor + 1];\n        for (int[] item : items)\
        \ {\n            freq[item[0]]++;\n        }\n\n        int[] count = new int[maxFactor\
        \ + 1];\n        for (int i = 1; i <= maxFactor; ++i) {\n            for (int\
        \ j = i; j <= maxFactor; j += i) {\n                count[i] += freq[j];\n \
        \           }\n        }\n\n        int[] dp = new int[budget + 1];\n      \
        \  for (int i = 1; i <= budget; ++i) {\n            dp[i] = -1;\n        }\n\
        \        dp[0] = 0;\n\n        for (int[] item : items) {\n            int f\
        \ = item[0];\n            int p = item[1];\n            int val = count[f];\n\
        \            for (int w = budget; w >= p; --w) {\n                if (dp[w -\
        \ p] != -1) {\n                    dp[w] = Math.max(dp[w], dp[w - p] + val);\n\
        \                }\n            }\n        }\n\n        int maxItems = 0;\n\
        \        for (int w = 0; w <= budget; ++w) {\n            if (dp[w] != -1) {\n\
        \                int total = dp[w] + (budget - w) / minPrice;\n            \
        \    maxItems = Math.max(maxItems, total);\n            }\n        }\n\n   \
        \     return maxItems;\n    }\n}"
      python: "class Solution(object):\n    def maximumSaleItems(self, items, budget):\n\
        \        \"\"\"\n        :type items: List[List[int]]\n        :type budget:\
        \ int\n        :rtype: int\n        \"\"\"\n        max_factor = max(item[0]\
        \ for item in items)\n        min_price = min(item[1] for item in items)\n\n\
        \        freq = [0] * (max_factor + 1)\n        for factor, price in items:\n\
        \            freq[factor] += 1\n\n        count = [0] * (max_factor + 1)\n \
        \       for i in range(1, max_factor + 1):\n            for j in range(i, max_factor\
        \ + 1, i):\n                count[i] += freq[j]\n\n        dp = [-1] * (budget\
        \ + 1)\n        dp[0] = 0\n\n        for factor, price in items:\n         \
        \   val = count[factor]\n            for w in range(budget, price - 1, -1):\n\
        \                if dp[w - price] != -1:\n                    if dp[w - price]\
        \ + val > dp[w]:\n                        dp[w] = dp[w - price] + val\n\n  \
        \      max_items = 0\n        for w in range(budget + 1):\n            if dp[w]\
        \ != -1:\n                total = dp[w] + (budget - w) // min_price\n      \
        \          if total > max_items:\n                    max_items = total\n\n\
        \        return max_items"
      python3: "class Solution:\n    def maximumSaleItems(self, items: List[List[int]],\
        \ budget: int) -> int:\n        max_factor = max(item[0] for item in items)\n\
        \        min_price = min(item[1] for item in items)\n\n        freq = [0] *\
        \ (max_factor + 1)\n        for factor, price in items:\n            freq[factor]\
        \ += 1\n\n        count = [0] * (max_factor + 1)\n        for i in range(1,\
        \ max_factor + 1):\n            for j in range(i, max_factor + 1, i):\n    \
        \            count[i] += freq[j]\n\n        dp = [-1] * (budget + 1)\n     \
        \   dp[0] = 0\n\n        for factor, price in items:\n            val = count[factor]\n\
        \            for w in range(budget, price - 1, -1):\n                if dp[w\
        \ - price] != -1:\n                    if dp[w - price] + val > dp[w]:\n   \
        \                     dp[w] = dp[w - price] + val\n\n        max_items = 0\n\
        \        for w in range(budget + 1):\n            if dp[w] != -1:\n        \
        \        total = dp[w] + (budget - w) // min_price\n                if total\
        \ > max_items:\n                    max_items = total\n\n        return max_items"
      c: "int maximumSaleItems(int** items, int itemsSize, int* itemsColSize, int budget)\
        \ {\n    int maxFactor = 0;\n    int minPrice = 1e9;\n    for (int i = 0; i\
        \ < itemsSize; ++i) {\n        if (items[i][0] > maxFactor) {\n            maxFactor\
        \ = items[i][0];\n        }\n        if (items[i][1] < minPrice) {\n       \
        \     minPrice = items[i][1];\n        }\n    }\n\n    int* freq = (int*)calloc(maxFactor\
        \ + 1, sizeof(int));\n    for (int i = 0; i < itemsSize; ++i) {\n        freq[items[i][0]]++;\n\
        \    }\n\n    int* count = (int*)calloc(maxFactor + 1, sizeof(int));\n    for\
        \ (int i = 1; i <= maxFactor; ++i) {\n        for (int j = i; j <= maxFactor;\
        \ j += i) {\n            count[i] += freq[j];\n        }\n    }\n\n    int*\
        \ dp = (int*)malloc((budget + 1) * sizeof(int));\n    for (int i = 0; i <= budget;\
        \ ++i) {\n        dp[i] = -1;\n    }\n    dp[0] = 0;\n\n    for (int i = 0;\
        \ i < itemsSize; ++i) {\n        int f = items[i][0];\n        int p = items[i][1];\n\
        \        int val = count[f];\n        for (int w = budget; w >= p; --w) {\n\
        \            if (dp[w - p] != -1) {\n                if (dp[w - p] + val > dp[w])\
        \ {\n                    dp[w] = dp[w - p] + val;\n                }\n     \
        \       }\n        }\n    }\n\n    int maxItems = 0;\n    for (int w = 0; w\
        \ <= budget; ++w) {\n        if (dp[w] != -1) {\n            int total = dp[w]\
        \ + (budget - w) / minPrice;\n            if (total > maxItems) {\n        \
        \        maxItems = total;\n            }\n        }\n    }\n\n    free(freq);\n\
        \    free(count);\n    free(dp);\n    return maxItems;\n}"
      csharp: "public class Solution {\n    public int MaximumSaleItems(int[][] items,\
        \ int budget) {\n        int maxFactor = 0;\n        int minPrice = int.MaxValue;\n\
        \        foreach (var item in items) {\n            if (item[0] > maxFactor)\
        \ maxFactor = item[0];\n            if (item[1] < minPrice) minPrice = item[1];\n\
        \        }\n\n        int[] freq = new int[maxFactor + 1];\n        foreach\
        \ (var item in items) {\n            freq[item[0]]++;\n        }\n\n       \
        \ int[] count = new int[maxFactor + 1];\n        for (int i = 1; i <= maxFactor;\
        \ i++) {\n            for (int j = i; j <= maxFactor; j += i) {\n          \
        \      count[i] += freq[j];\n            }\n        }\n\n        int[] dp =\
        \ new int[budget + 1];\n        for (int i = 0; i <= budget; i++) {\n      \
        \      dp[i] = -1;\n        }\n        dp[0] = 0;\n\n        foreach (var item\
        \ in items) {\n            int factor = item[0];\n            int price = item[1];\n\
        \            int val = count[factor];\n            for (int w = budget; w >=\
        \ price; w--) {\n                if (dp[w - price] != -1) {\n              \
        \      if (dp[w - price] + val > dp[w]) {\n                        dp[w] = dp[w\
        \ - price] + val;\n                    }\n                }\n            }\n\
        \        }\n\n        int maxItems = 0;\n        for (int w = 0; w <= budget;\
        \ w++) {\n            if (dp[w] != -1) {\n                int total = dp[w]\
        \ + (budget - w) / minPrice;\n                if (total > maxItems) {\n    \
        \                maxItems = total;\n                }\n            }\n     \
        \   }\n\n        return maxItems;\n    }\n}"
      javascript: "/**\n * @param {number[][]} items\n * @param {number} budget\n *\
        \ @return {number}\n */\nvar maximumSaleItems = function(items, budget) {\n\
        \    let maxFactor = 0;\n    let minPrice = Infinity;\n    for (const [factor,\
        \ price] of items) {\n        if (factor > maxFactor) maxFactor = factor;\n\
        \        if (price < minPrice) minPrice = price;\n    }\n\n    const freq =\
        \ new Int32Array(maxFactor + 1);\n    for (const [factor] of items) {\n    \
        \    freq[factor]++;\n    }\n\n    const count = new Int32Array(maxFactor +\
        \ 1);\n    for (let i = 1; i <= maxFactor; i++) {\n        for (let j = i; j\
        \ <= maxFactor; j += i) {\n            count[i] += freq[j];\n        }\n   \
        \ }\n\n    const dp = new Int32Array(budget + 1).fill(-1);\n    dp[0] = 0;\n\
        \n    for (const [factor, price] of items) {\n        const val = count[factor];\n\
        \        for (let w = budget; w >= price; w--) {\n            if (dp[w - price]\
        \ !== -1) {\n                if (dp[w - price] + val > dp[w]) {\n          \
        \          dp[w] = dp[w - price] + val;\n                }\n            }\n\
        \        }\n    }\n\n    let maxItems = 0;\n    for (let w = 0; w <= budget;\
        \ w++) {\n        if (dp[w] !== -1) {\n            const total = dp[w] + Math.floor((budget\
        \ - w) / minPrice);\n            if (total > maxItems) {\n                maxItems\
        \ = total;\n            }\n        }\n    }\n\n    return maxItems;\n};"
      typescript: "function maximumSaleItems(items: number[][], budget: number): number\
        \ {\n    let maxFactor = 0;\n    let minPrice = Infinity;\n    for (const [factor,\
        \ price] of items) {\n        if (factor > maxFactor) maxFactor = factor;\n\
        \        if (price < minPrice) minPrice = price;\n    }\n\n    const freq =\
        \ new Int32Array(maxFactor + 1);\n    for (const [factor] of items) {\n    \
        \    freq[factor]++;\n    }\n\n    const count = new Int32Array(maxFactor +\
        \ 1);\n    for (let i = 1; i <= maxFactor; i++) {\n        for (let j = i; j\
        \ <= maxFactor; j += i) {\n            count[i] += freq[j];\n        }\n   \
        \ }\n\n    const dp = new Int32Array(budget + 1).fill(-1);\n    dp[0] = 0;\n\
        \n    for (const [factor, price] of items) {\n        const val = count[factor];\n\
        \        for (let w = budget; w >= price; w--) {\n            if (dp[w - price]\
        \ !== -1) {\n                if (dp[w - price] + val > dp[w]) {\n          \
        \          dp[w] = dp[w - price] + val;\n                }\n            }\n\
        \        }\n    }\n\n    let maxItems = 0;\n    for (let w = 0; w <= budget;\
        \ w++) {\n        if (dp[w] !== -1) {\n            const total = dp[w] + Math.floor((budget\
        \ - w) / minPrice);\n            if (total > maxItems) {\n                maxItems\
        \ = total;\n            }\n        }\n    }\n\n    return maxItems;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $items\n     * @param\
        \ Integer $budget\n     * @return Integer\n     */\n    function maximumSaleItems($items,\
        \ $budget) {\n        $maxFactor = 0;\n        $minPrice = PHP_INT_MAX;\n  \
        \      foreach ($items as $item) {\n            if ($item[0] > $maxFactor) $maxFactor\
        \ = $item[0];\n            if ($item[1] < $minPrice) $minPrice = $item[1];\n\
        \        }\n\n        $freq = array_fill(0, $maxFactor + 1, 0);\n        foreach\
        \ ($items as $item) {\n            $freq[$item[0]]++;\n        }\n\n       \
        \ $count = array_fill(0, $maxFactor + 1, 0);\n        for ($i = 1; $i <= $maxFactor;\
        \ $i++) {\n            for ($j = $i; $j <= $maxFactor; $j += $i) {\n       \
        \         $count[$i] += $freq[$j];\n            }\n        }\n\n        $dp\
        \ = array_fill(0, $budget + 1, -1);\n        $dp[0] = 0;\n\n        foreach\
        \ ($items as $item) {\n            $factor = $item[0];\n            $price =\
        \ $item[1];\n            $val = $count[$factor];\n            for ($w = $budget;\
        \ $w >= $price; $w--) {\n                if ($dp[$w - $price] != -1) {\n   \
        \                 if ($dp[$w - $price] + $val > $dp[$w]) {\n               \
        \         $dp[$w] = $dp[$w - $price] + $val;\n                    }\n      \
        \          }\n            }\n        }\n\n        $maxItems = 0;\n        for\
        \ ($w = 0; $w <= $budget; $w++) {\n            if ($dp[$w] != -1) {\n      \
        \          $total = $dp[$w] + intdiv($budget - $w, $minPrice);\n           \
        \     if ($total > $maxItems) {\n                    $maxItems = $total;\n \
        \               }\n            }\n        }\n\n        return $maxItems;\n \
        \   }\n}"
      swift: "class Solution {\n    func maximumSaleItems(_ items: [[Int]], _ budget:\
        \ Int) -> Int {\n        var maxFactor = 0\n        var minPrice = Int.max\n\
        \        for item in items {\n            if item[0] > maxFactor { maxFactor\
        \ = item[0] }\n            if item[1] < minPrice { minPrice = item[1] }\n  \
        \      }\n\n        var freq = [Int](repeating: 0, count: maxFactor + 1)\n \
        \       for item in items {\n            freq[item[0]] += 1\n        }\n\n \
        \       var count = [Int](repeating: 0, count: maxFactor + 1)\n        if maxFactor\
        \ >= 1 {\n            for i in 1...maxFactor {\n                for j in stride(from:\
        \ i, through: maxFactor, by: i) {\n                    count[i] += freq[j]\n\
        \                }\n            }\n        }\n\n        var dp = [Int](repeating:\
        \ -1, count: budget + 1)\n        dp[0] = 0\n\n        for item in items {\n\
        \            let factor = item[0]\n            let price = item[1]\n       \
        \     let val = count[factor]\n            if price <= budget {\n          \
        \      for w in stride(from: budget, through: price, by: -1) {\n           \
        \         if dp[w - price] != -1 {\n                        if dp[w - price]\
        \ + val > dp[w] {\n                            dp[w] = dp[w - price] + val\n\
        \                        }\n                    }\n                }\n     \
        \       }\n        }\n\n        var maxItems = 0\n        for w in 0...budget\
        \ {\n            if dp[w] != -1 {\n                let total = dp[w] + (budget\
        \ - w) / minPrice\n                if total > maxItems {\n                 \
        \   maxItems = total\n                }\n            }\n        }\n\n      \
        \  return maxItems\n    }\n}"
      kotlin: "class Solution {\n    fun maximumSaleItems(items: Array<IntArray>, budget:\
        \ Int): Int {\n        var maxFactor = 0\n        var minPrice = Int.MAX_VALUE\n\
        \        for (item in items) {\n            if (item[0] > maxFactor) maxFactor\
        \ = item[0]\n            if (item[1] < minPrice) minPrice = item[1]\n      \
        \  }\n\n        val freq = IntArray(maxFactor + 1)\n        for (item in items)\
        \ {\n            freq[item[0]]++\n        }\n\n        val count = IntArray(maxFactor\
        \ + 1)\n        for (i in 1..maxFactor) {\n            var j = i\n         \
        \   while (j <= maxFactor) {\n                count[i] += freq[j]\n        \
        \        j += i\n            }\n        }\n\n        val dp = IntArray(budget\
        \ + 1) { -1 }\n        dp[0] = 0\n\n        for (item in items) {\n        \
        \    val factor = item[0]\n            val price = item[1]\n            val\
        \ v = count[factor]\n            for (w in budget downTo price) {\n        \
        \        if (dp[w - price] != -1) {\n                    val cand = dp[w - price]\
        \ + v\n                    if (cand > dp[w]) {\n                        dp[w]\
        \ = cand\n                    }\n                }\n            }\n        }\n\
        \n        var maxItems = 0\n        for (w in 0..budget) {\n            if (dp[w]\
        \ != -1) {\n                val total = dp[w] + (budget - w) / minPrice\n  \
        \              if (total > maxItems) {\n                    maxItems = total\n\
        \                }\n            }\n        }\n\n        return maxItems\n  \
        \  }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maximumSaleItems(List<List<int>>\
        \ items, int budget) {\n    int maxFactor = 0;\n    int minPrice = 1000000000;\n\
        \    for (var item in items) {\n      if (item[0] > maxFactor) maxFactor = item[0];\n\
        \      if (item[1] < minPrice) minPrice = item[1];\n    }\n\n    List<int> freq\
        \ = List.filled(maxFactor + 1, 0);\n    for (var item in items) {\n      freq[item[0]]++;\n\
        \    }\n\n    List<int> count = List.filled(maxFactor + 1, 0);\n    for (int\
        \ i = 1; i <= maxFactor; i++) {\n      for (int j = i; j <= maxFactor; j +=\
        \ i) {\n        count[i] += freq[j];\n      }\n    }\n\n    List<int> dp = List.filled(budget\
        \ + 1, -1);\n    dp[0] = 0;\n\n    for (var item in items) {\n      int factor\
        \ = item[0];\n      int price = item[1];\n      int val = count[factor];\n \
        \     for (int w = budget; w >= price; w--) {\n        if (dp[w - price] !=\
        \ -1) {\n          int cand = dp[w - price] + val;\n          if (cand > dp[w])\
        \ {\n            dp[w] = cand;\n          }\n        }\n      }\n    }\n\n \
        \   int maxItems = 0;\n    for (int w = 0; w <= budget; w++) {\n      if (dp[w]\
        \ != -1) {\n        int total = dp[w] + (budget - w) ~/ minPrice;\n        if\
        \ (total > maxItems) {\n          maxItems = total;\n        }\n      }\n  \
        \  }\n\n    return maxItems;\n  }\n}"
      go: "func maximumSaleItems(items [][]int, budget int) int {\n    maxFactor :=\
        \ 0\n    minPrice := int(^uint(0) >> 1)\n    for _, item := range items {\n\
        \        if item[0] > maxFactor {\n            maxFactor = item[0]\n       \
        \ }\n        if item[1] < minPrice {\n            minPrice = item[1]\n     \
        \   }\n    }\n\n    freq := make([]int, maxFactor+1)\n    for _, item := range\
        \ items {\n        freq[item[0]]++\n    }\n\n    count := make([]int, maxFactor+1)\n\
        \    for i := 1; i <= maxFactor; i++ {\n        for j := i; j <= maxFactor;\
        \ j += i {\n            count[i] += freq[j]\n        }\n    }\n\n    dp := make([]int,\
        \ budget+1)\n    for i := range dp {\n        dp[i] = -1\n    }\n    dp[0] =\
        \ 0\n\n    for _, item := range items {\n        factor := item[0]\n       \
        \ price := item[1]\n        val := count[factor]\n        for w := budget; w\
        \ >= price; w-- {\n            if dp[w-price] != -1 {\n                cand\
        \ := dp[w-price] + val\n                if cand > dp[w] {\n                \
        \    dp[w] = cand\n                }\n            }\n        }\n    }\n\n  \
        \  maxItems := 0\n    for w := 0; w <= budget; w++ {\n        if dp[w] != -1\
        \ {\n            total := dp[w] + (budget-w)/minPrice\n            if total\
        \ > maxItems {\n                maxItems = total\n            }\n        }\n\
        \    }\n\n    return maxItems\n}"
      ruby: "# @param {Integer[][]} items\n# @param {Integer} budget\n# @return {Integer}\n\
        def maximum_sale_items(items, budget)\n  max_factor = items.map { |item| item[0]\
        \ }.max\n  min_price = items.map { |item| item[1] }.min\n\n  freq = Array.new(max_factor\
        \ + 1, 0)\n  items.each { |factor, _| freq[factor] += 1 }\n\n  count = Array.new(max_factor\
        \ + 1, 0)\n  (1..max_factor).each do |i|\n    (i..max_factor).step(i) do |j|\n\
        \      count[i] += freq[j]\n    end\n  end\n\n  dp = Array.new(budget + 1, -1)\n\
        \  dp[0] = 0\n\n  items.each do |factor, price|\n    val = count[factor]\n \
        \   budget.downto(price) do |w|\n      if dp[w - price] != -1\n        cand\
        \ = dp[w - price] + val\n        dp[w] = cand if cand > dp[w]\n      end\n \
        \   end\n  end\n\n  max_items = 0\n  (0..budget).each do |w|\n    if dp[w] !=\
        \ -1\n      total = dp[w] + (budget - w) / min_price\n      max_items = total\
        \ if total > max_items\n    end\n  end\n\n  max_items\nend"
      scala: "object Solution {\n    def maximumSaleItems(items: Array[Array[Int]],\
        \ budget: Int): Int = {\n        var maxFactor = 0\n        var minPrice = Int.MaxValue\n\
        \        for (item <- items) {\n            if (item(0) > maxFactor) maxFactor\
        \ = item(0)\n            if (item(1) < minPrice) minPrice = item(1)\n      \
        \  }\n\n        val freq = new Array[Int](maxFactor + 1)\n        for (item\
        \ <- items) {\n            freq(item(0)) += 1\n        }\n\n        val count\
        \ = new Array[Int](maxFactor + 1)\n        for (i <- 1 to maxFactor) {\n   \
        \         var j = i\n            while (j <= maxFactor) {\n                count(i)\
        \ += freq(j)\n                j += i\n            }\n        }\n\n        val\
        \ dp = Array.fill(budget + 1)(-1)\n        dp(0) = 0\n\n        for (item <-\
        \ items) {\n            val factor = item(0)\n            val price = item(1)\n\
        \            val v = count(factor)\n            var w = budget\n           \
        \ while (w >= price) {\n                if (dp(w - price) != -1) {\n       \
        \             val cand = dp(w - price) + v\n                    if (cand > dp(w))\
        \ {\n                        dp(w) = cand\n                    }\n         \
        \       }\n                w -= 1\n            }\n        }\n\n        var maxItems\
        \ = 0\n        for (w <- 0 to budget) {\n            if (dp(w) != -1) {\n  \
        \              val total = dp(w) + (budget - w) / minPrice\n               \
        \ if (total > maxItems) {\n                    maxItems = total\n          \
        \      }\n            }\n        }\n\n        maxItems\n    }\n}"
      rust: "impl Solution {\n    pub fn maximum_sale_items(items: Vec<Vec<i32>>, budget:\
        \ i32) -> i32 {\n        let mut max_factor = 0;\n        let mut min_price\
        \ = i32::MAX;\n        for item in &items {\n            if item[0] > max_factor\
        \ { max_factor = item[0]; }\n            if item[1] < min_price { min_price\
        \ = item[1]; }\n        }\n\n        let mut freq = vec![0; (max_factor + 1)\
        \ as usize];\n        for item in &items {\n            freq[item[0] as usize]\
        \ += 1;\n        }\n\n        let mut count = vec![0; (max_factor + 1) as usize];\n\
        \        for i in 1..=max_factor as usize {\n            for j in (i..=max_factor\
        \ as usize).step_by(i) {\n                count[i] += freq[j];\n           \
        \ }\n        }\n\n        let mut dp = vec![-1; (budget + 1) as usize];\n  \
        \      dp[0] = 0;\n\n        for item in &items {\n            let f = item[0]\
        \ as usize;\n            let p = item[1] as usize;\n            let val = count[f];\n\
        \            for w in (p..=budget as usize).rev() {\n                if dp[w\
        \ - p] != -1 {\n                    let new_val = dp[w - p] + val;\n       \
        \             if new_val > dp[w] {\n                        dp[w] = new_val;\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    let mut max_items = 0;\n        for w in 0..=budget as usize {\n      \
        \      if dp[w] != -1 {\n                let total = dp[w] + (budget - w as\
        \ i32) / min_price;\n                if total > max_items {\n              \
        \      max_items = total;\n                }\n            }\n        }\n\n \
        \       max_items\n    }\n}"
      racket: "(define/contract (maximum-sale-items items budget)\n  (-> (listof (listof\
        \ exact-integer?)) exact-integer? exact-integer?)\n  (let* ([max-factor (apply\
        \ max (map first items))]\n         [min-price (apply min (map second items))]\n\
        \         [freq (make-vector (+ max-factor 1) 0)])\n    (for ([item items])\n\
        \      (let ([f (first item)])\n        (vector-set! freq f (+ (vector-ref freq\
        \ f) 1))))\n    (define count (make-vector (+ max-factor 1) 0))\n    (for ([i\
        \ (in-range 1 (+ max-factor 1))])\n      (for ([j (in-range i (+ max-factor\
        \ 1) i)])\n        (vector-set! count i (+ (vector-ref count i) (vector-ref\
        \ freq j)))))\n    (define dp (make-vector (+ budget 1) -1))\n    (vector-set!\
        \ dp 0 0)\n    (for ([item items])\n      (let* ([f (first item)]\n        \
        \     [p (second item)]\n             [val (vector-ref count f)])\n        (for\
        \ ([w (in-range budget (- p 1) -1)])\n          (let ([prev (vector-ref dp (-\
        \ w p))])\n            (when (not (= prev -1))\n              (vector-set! dp\
        \ w (max (vector-ref dp w) (+ prev val))))))))\n    (let ([max-items 0])\n \
        \     (for ([w (in-range (+ budget 1))])\n        (let ([val (vector-ref dp\
        \ w)])\n          (when (not (= val -1))\n            (let ([total (+ val (quotient\
        \ (- budget w) min-price))])\n              (set! max-items (max max-items total))))))\n\
        \      max-items)))"
      erlang: "-spec maximum_sale_items(Items :: [[integer()]], Budget :: integer())\
        \ -> integer().\nmaximum_sale_items(Items, Budget) ->\n    {MaxFactor, MinPrice}\
        \ = lists:foldl(fun([F, P], {MF, MP}) ->\n        {erlang:max(F, MF), erlang:min(P,\
        \ MP)}\n    end, {0, 1000000}, Items),\n\n    Freq = lists:foldl(fun([F, _],\
        \ Acc) ->\n        Acc#{F => maps:get(F, Acc, 0) + 1}\n    end, #{}, Items),\n\
        \n    CountList = [0 | [lists:sum([maps:get(J, Freq, 0) || J <- lists:seq(I,\
        \ MaxFactor, I)]) || I <- lists:seq(1, MaxFactor)]],\n    Count = list_to_tuple(CountList),\n\
        \n    InitialDP = list_to_tuple([-1 || _ <- lists:seq(0, Budget)]),\n    DP0\
        \ = setelement(1, InitialDP, 0),\n\n    FinalDP = lists:foldl(fun([F, P], AccDP)\
        \ ->\n        Val = element(F + 1, Count),\n        ListForNewDP = [begin\n\
        \            OldVal = element(W + 1, AccDP),\n            if W >= P ->\n   \
        \             PrevVal = element(W - P + 1, AccDP),\n                if PrevVal\
        \ =:= -1 -> OldVal;\n                   true -> erlang:max(OldVal, PrevVal +\
        \ Val)\n                end;\n               true -> OldVal\n            end\n\
        \        end || W <- lists:seq(0, Budget)],\n        list_to_tuple(ListForNewDP)\n\
        \    end, DP0, Items),\n\n    lists:foldl(fun(W, MaxAcc) ->\n        case element(W\
        \ + 1, FinalDP) of\n            -1 -> MaxAcc;\n            V -> erlang:max(MaxAcc,\
        \ V + (Budget - W) div MinPrice)\n        end\n    end, 0, lists:seq(0, Budget))."
      elixir: "defmodule Solution do\n  @spec maximum_sale_items(items :: [[integer]],\
        \ budget :: integer) :: integer\n  def maximum_sale_items(items, budget) do\n\
        \    max_factor = items |> Enum.map(fn [f, _] -> f end) |> Enum.max()\n    min_price\
        \ = items |> Enum.map(fn [_, p] -> p end) |> Enum.min()\n\n    freq = Enum.reduce(items,\
        \ %{}, fn [f, _], acc ->\n      Map.put(acc, f, Map.get(acc, f, 0) + 1)\n  \
        \  end)\n\n    count_list = [0 | for i <- 1..max_factor do\n      Enum.take_every(i..max_factor,\
        \ i)\n      |> Enum.reduce(0, fn j, acc -> acc + Map.get(freq, j, 0) end)\n\
        \    end]\n    count = List.to_tuple(count_list)\n\n    initial_dp = List.to_tuple(for\
        \ _ <- 0..budget, do: -1)\n    dp0 = put_elem(initial_dp, 0, 0)\n\n    final_dp\
        \ = Enum.reduce(items, dp0, fn [f, p], acc_dp ->\n      val = elem(count, f)\n\
        \      new_dp_list = for w <- 0..budget do\n        old_val = elem(acc_dp, w)\n\
        \        if w >= p do\n          prev_val = elem(acc_dp, w - p)\n          if\
        \ prev_val == -1, do: old_val, else: max(old_val, prev_val + val)\n        else\n\
        \          old_val\n        end\n      end\n      List.to_tuple(new_dp_list)\n\
        \    end)\n\n    0..budget\n    |> Enum.reduce(0, fn w, max_acc ->\n      case\
        \ elem(final_dp, w) do\n        -1 -> max_acc\n        v -> max(max_acc, v +\
        \ div(budget - w, min_price))\n      end\n    end)\n  end\nend"
    approach: 'The problem can be modeled as a variation of the 0-1 knapsack problem
      combined with unbounded knapsack for remaining budget. First, we observe that
      purchasing the first copy of any item $i$ costs $\text{price}_i$ and yields 1
      copy of item $i$ plus 1 free copy of every other item $j$ where $\text{factor}_i$
      divides $\text{factor}_j$. This means buying the first copy of item $i$ yields
      exactly $\text{count}[\text{factor}_i]$ items, where $\text{count}[f]$ is the
      total number of items whose factor is a multiple of $f$. We can precompute this
      count for all distinct factors in $O(N \sqrt{M})$ or by iterating over multiples.


      Any additional copy beyond the first for an item provides exactly 1 item and no
      further bonuses. To maximize the number of items obtained from additional purchases,
      we should always purchase additional copies of the globally cheapest item, which
      has cost $\min_P = \min_i \text{price}_i$. If that cheapest item was not among
      the initial items purchased, buying it for the first time gives at least 1 item
      (and potentially more, which would correspond to a valid subset in our DP). Therefore,
      we compute the maximum items obtainable by buying a subset of first copies using
      standard 0-1 knapsack DP up to $\text{budget}$, and then for each reachable spent
      amount $w$, the remaining $\text{budget} - w$ can yield $\lfloor (\text{budget}
      - w) / \min_P \rfloor$ additional items. The overall answer is the maximum over
      all $w \le \text{budget}$ of $dp[w] + \lfloor (\text{budget} - w) / \min_P \rfloor$.'
    time_complexity: O(N \cdot \text{budget} + M \log M) where $N$ is the number of
      items, $\text{budget}$ is the given budget, and $M = \max(\text{factor}_i) \le
      1500$. Precomputing the multiple counts takes $O(M \log M + N)$ time, and the
      0-1 knapsack DP takes $O(N \cdot \text{budget})$ time, which easily runs within
      the time limits.
    space_complexity: O(\text{budget} + M) auxiliary space to store the knapsack DP
      array of size $\text{budget} + 1$ and the factor frequencies array of size up
      to 1501.
    elapsed_time: 1752.7018773555756
    model: gemini-3-flash-preview
    generated_at: '2026-11-27 06:31:14 '
---

## Problem #3946: Maximum Number of Items From Sale I

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Greedy

## Problem Description

<p>You are given a 2D integer array <code>items</code>, where <code>items[i] = [factor<sub>i</sub>, price<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> item. You are also given an integer <code>budget</code>.</p>

<p>There are unlimited copies of each item available for purchase.You may buy any number of copies of any items such that the total cost of the purchased copies is at most <code>budget</code>.</p>

<p>After buying items, you may receive free copies according to the following rules:</p>

<ul>
	<li>For each item <code>i</code> that you bought <strong>at least one copy</strong> of, you receive <strong>one free copy</strong> of every item <code>j</code> such that <code>j != i</code> and <code>factor<sub>i</sub></code> divides <code>factor<sub>j</sub></code>.</li>
	<li>Buying multiple copies of the same item <code>i</code> does <strong>not</strong> give additional free copies through item <code>i</code>.</li>
	<li>The same item <code>j</code> can be received multiple times for free if it is received from purchases of different item types.</li>
</ul>

<p>Return the <strong>maximum total number of item copies</strong> you can obtain, including both purchased copies and free copies, while spending at most <code>budget</code> on purchased items.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">items = [[6,2],[2,6],[3,4]], budget = 9</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>You can buy 2 copies of item 0 and 1 copy of item 2 for a total cost of <code>2 * 2 + 4 = 8</code>, which is not greater than <code>budget = 9</code>.</li>
	<li>Buying item 2 gives 1 free copy of item 0, because <code>factor<sub>2</sub> = 3</code> divides <code>factor<sub>0</sub> = 6</code>.</li>
	<li>You leave with 3 purchased copies and 1 free copy, for a total of 4 item copies.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>You can buy 1 copy of item 0, 1 copy of item 1, and 2 copies of item 2 for a total cost of <code>4 + 2 + 2 * 1 = 8</code>.</li>
	<li>Buying item 0 gives 1 free copy of items 2, 3, and 4.</li>
	<li>Buying item 1 gives 1 free copy of items 3 and 4.</li>
	<li>Buying item 2 gives 1 free copy of item 4.</li>
	<li>Thus, you receive 6 free copies. You leave with 4 purchased copies and 6 free copies, for a total of 10 item copies.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= items.length &lt;= 1000</code></li>
	<li><code>items[i] = [factor<sub>i</sub>, price<sub>i</sub>]</code></li>
	<li><code>1 &lt;= factor<sub>i</sub>, price<sub>i</sub> &lt;= 1500</code></li>
	<li><code>1 &lt;= budget &lt;= 1500</code></li>
</ul>


## Hints

1. Precompute for every possible factor `f`, how many items have a factor divisible by `f`.

2. Buying the first copy of item `i` is special: it gives the purchased copy plus one free copy of every other item whose factor is divisible by `factor_i`.

3. Buying more copies of the same item does not create more free copies, so after the first copy, each extra purchase only adds one item copy.

4. This suggests a knapsack-style DP over item types and remaining budget, where each item can either be skipped, bought for the first time, or bought additional times after it has already been activated.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as a variation of the 0-1 knapsack problem combined with unbounded knapsack for remaining budget. First, we observe that purchasing the first copy of any item $i$ costs $\text{price}_i$ and yields 1 copy of item $i$ plus 1 free copy of every other item $j$ where $\text{factor}_i$ divides $\text{factor}_j$. This means buying the first copy of item $i$ yields exactly $\text{count}[\text{factor}_i]$ items, where $\text{count}[f]$ is the total number of items whose factor is a multiple of $f$. We can precompute this count for all distinct factors in $O(N \sqrt{M})$ or by iterating over multiples.

Any additional copy beyond the first for an item provides exactly 1 item and no further bonuses. To maximize the number of items obtained from additional purchases, we should always purchase additional copies of the globally cheapest item, which has cost $\min_P = \min_i \text{price}_i$. If that cheapest item was not among the initial items purchased, buying it for the first time gives at least 1 item (and potentially more, which would correspond to a valid subset in our DP). Therefore, we compute the maximum items obtainable by buying a subset of first copies using standard 0-1 knapsack DP up to $\text{budget}$, and then for each reachable spent amount $w$, the remaining $\text{budget} - w$ can yield $\lfloor (\text{budget} - w) / \min_P \rfloor$ additional items. The overall answer is the maximum over all $w \le \text{budget}$ of $dp[w] + \lfloor (\text{budget} - w) / \min_P \rfloor$.

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
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int maxFactor = 0;
        int minPrice = 1e9;
        for (const auto& item : items) {
            maxFactor = max(maxFactor, item[0]);
            minPrice = min(minPrice, item[1]);
        }

        vector<int> freq(maxFactor + 1, 0);
        for (const auto& item : items) {
            freq[item[0]]++;
        }

        vector<int> count(maxFactor + 1, 0);
        for (int i = 1; i <= maxFactor; ++i) {
            for (int j = i; j <= maxFactor; j += i) {
                count[i] += freq[j];
            }
        }

        vector<int> dp(budget + 1, -1);
        dp[0] = 0;

        for (const auto& item : items) {
            int f = item[0];
            int p = item[1];
            int val = count[f];
            for (int w = budget; w >= p; --w) {
                if (dp[w - p] != -1) {
                    dp[w] = max(dp[w], dp[w - p] + val);
                }
            }
        }

        int maxItems = 0;
        for (int w = 0; w <= budget; ++w) {
            if (dp[w] != -1) {
                int total = dp[w] + (budget - w) / minPrice;
                maxItems = max(maxItems, total);
            }
        }

        return maxItems;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maximumSaleItems(int[][] items, int budget) {
        int maxFactor = 0;
        int minPrice = Integer.MAX_VALUE;
        for (int[] item : items) {
            maxFactor = Math.max(maxFactor, item[0]);
            minPrice = Math.min(minPrice, item[1]);
        }

        int[] freq = new int[maxFactor + 1];
        for (int[] item : items) {
            freq[item[0]]++;
        }

        int[] count = new int[maxFactor + 1];
        for (int i = 1; i <= maxFactor; ++i) {
            for (int j = i; j <= maxFactor; j += i) {
                count[i] += freq[j];
            }
        }

        int[] dp = new int[budget + 1];
        for (int i = 1; i <= budget; ++i) {
            dp[i] = -1;
        }
        dp[0] = 0;

        for (int[] item : items) {
            int f = item[0];
            int p = item[1];
            int val = count[f];
            for (int w = budget; w >= p; --w) {
                if (dp[w - p] != -1) {
                    dp[w] = Math.max(dp[w], dp[w - p] + val);
                }
            }
        }

        int maxItems = 0;
        for (int w = 0; w <= budget; ++w) {
            if (dp[w] != -1) {
                int total = dp[w] + (budget - w) / minPrice;
                maxItems = Math.max(maxItems, total);
            }
        }

        return maxItems;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        max_factor = max(item[0] for item in items)
        min_price = min(item[1] for item in items)

        freq = [0] * (max_factor + 1)
        for factor, price in items:
            freq[factor] += 1

        count = [0] * (max_factor + 1)
        for i in range(1, max_factor + 1):
            for j in range(i, max_factor + 1, i):
                count[i] += freq[j]

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for factor, price in items:
            val = count[factor]
            for w in range(budget, price - 1, -1):
                if dp[w - price] != -1:
                    if dp[w - price] + val > dp[w]:
                        dp[w] = dp[w - price] + val

        max_items = 0
        for w in range(budget + 1):
            if dp[w] != -1:
                total = dp[w] + (budget - w) // min_price
                if total > max_items:
                    max_items = total

        return max_items
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(item[0] for item in items)
        min_price = min(item[1] for item in items)

        freq = [0] * (max_factor + 1)
        for factor, price in items:
            freq[factor] += 1

        count = [0] * (max_factor + 1)
        for i in range(1, max_factor + 1):
            for j in range(i, max_factor + 1, i):
                count[i] += freq[j]

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for factor, price in items:
            val = count[factor]
            for w in range(budget, price - 1, -1):
                if dp[w - price] != -1:
                    if dp[w - price] + val > dp[w]:
                        dp[w] = dp[w - price] + val

        max_items = 0
        for w in range(budget + 1):
            if dp[w] != -1:
                total = dp[w] + (budget - w) // min_price
                if total > max_items:
                    max_items = total

        return max_items
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maximumSaleItems(int** items, int itemsSize, int* itemsColSize, int budget) {
    int maxFactor = 0;
    int minPrice = 1e9;
    for (int i = 0; i < itemsSize; ++i) {
        if (items[i][0] > maxFactor) {
            maxFactor = items[i][0];
        }
        if (items[i][1] < minPrice) {
            minPrice = items[i][1];
        }
    }

    int* freq = (int*)calloc(maxFactor + 1, sizeof(int));
    for (int i = 0; i < itemsSize; ++i) {
        freq[items[i][0]]++;
    }

    int* count = (int*)calloc(maxFactor + 1, sizeof(int));
    for (int i = 1; i <= maxFactor; ++i) {
        for (int j = i; j <= maxFactor; j += i) {
            count[i] += freq[j];
        }
    }

    int* dp = (int*)malloc((budget + 1) * sizeof(int));
    for (int i = 0; i <= budget; ++i) {
        dp[i] = -1;
    }
    dp[0] = 0;

    for (int i = 0; i < itemsSize; ++i) {
        int f = items[i][0];
        int p = items[i][1];
        int val = count[f];
        for (int w = budget; w >= p; --w) {
            if (dp[w - p] != -1) {
                if (dp[w - p] + val > dp[w]) {
                    dp[w] = dp[w - p] + val;
                }
            }
        }
    }

    int maxItems = 0;
    for (int w = 0; w <= budget; ++w) {
        if (dp[w] != -1) {
            int total = dp[w] + (budget - w) / minPrice;
            if (total > maxItems) {
                maxItems = total;
            }
        }
    }

    free(freq);
    free(count);
    free(dp);
    return maxItems;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximumSaleItems(int[][] items, int budget) {
        int maxFactor = 0;
        int minPrice = int.MaxValue;
        foreach (var item in items) {
            if (item[0] > maxFactor) maxFactor = item[0];
            if (item[1] < minPrice) minPrice = item[1];
        }

        int[] freq = new int[maxFactor + 1];
        foreach (var item in items) {
            freq[item[0]]++;
        }

        int[] count = new int[maxFactor + 1];
        for (int i = 1; i <= maxFactor; i++) {
            for (int j = i; j <= maxFactor; j += i) {
                count[i] += freq[j];
            }
        }

        int[] dp = new int[budget + 1];
        for (int i = 0; i <= budget; i++) {
            dp[i] = -1;
        }
        dp[0] = 0;

        foreach (var item in items) {
            int factor = item[0];
            int price = item[1];
            int val = count[factor];
            for (int w = budget; w >= price; w--) {
                if (dp[w - price] != -1) {
                    if (dp[w - price] + val > dp[w]) {
                        dp[w] = dp[w - price] + val;
                    }
                }
            }
        }

        int maxItems = 0;
        for (int w = 0; w <= budget; w++) {
            if (dp[w] != -1) {
                int total = dp[w] + (budget - w) / minPrice;
                if (total > maxItems) {
                    maxItems = total;
                }
            }
        }

        return maxItems;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} items
 * @param {number} budget
 * @return {number}
 */
var maximumSaleItems = function(items, budget) {
    let maxFactor = 0;
    let minPrice = Infinity;
    for (const [factor, price] of items) {
        if (factor > maxFactor) maxFactor = factor;
        if (price < minPrice) minPrice = price;
    }

    const freq = new Int32Array(maxFactor + 1);
    for (const [factor] of items) {
        freq[factor]++;
    }

    const count = new Int32Array(maxFactor + 1);
    for (let i = 1; i <= maxFactor; i++) {
        for (let j = i; j <= maxFactor; j += i) {
            count[i] += freq[j];
        }
    }

    const dp = new Int32Array(budget + 1).fill(-1);
    dp[0] = 0;

    for (const [factor, price] of items) {
        const val = count[factor];
        for (let w = budget; w >= price; w--) {
            if (dp[w - price] !== -1) {
                if (dp[w - price] + val > dp[w]) {
                    dp[w] = dp[w - price] + val;
                }
            }
        }
    }

    let maxItems = 0;
    for (let w = 0; w <= budget; w++) {
        if (dp[w] !== -1) {
            const total = dp[w] + Math.floor((budget - w) / minPrice);
            if (total > maxItems) {
                maxItems = total;
            }
        }
    }

    return maxItems;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximumSaleItems(items: number[][], budget: number): number {
    let maxFactor = 0;
    let minPrice = Infinity;
    for (const [factor, price] of items) {
        if (factor > maxFactor) maxFactor = factor;
        if (price < minPrice) minPrice = price;
    }

    const freq = new Int32Array(maxFactor + 1);
    for (const [factor] of items) {
        freq[factor]++;
    }

    const count = new Int32Array(maxFactor + 1);
    for (let i = 1; i <= maxFactor; i++) {
        for (let j = i; j <= maxFactor; j += i) {
            count[i] += freq[j];
        }
    }

    const dp = new Int32Array(budget + 1).fill(-1);
    dp[0] = 0;

    for (const [factor, price] of items) {
        const val = count[factor];
        for (let w = budget; w >= price; w--) {
            if (dp[w - price] !== -1) {
                if (dp[w - price] + val > dp[w]) {
                    dp[w] = dp[w - price] + val;
                }
            }
        }
    }

    let maxItems = 0;
    for (let w = 0; w <= budget; w++) {
        if (dp[w] !== -1) {
            const total = dp[w] + Math.floor((budget - w) / minPrice);
            if (total > maxItems) {
                maxItems = total;
            }
        }
    }

    return maxItems;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $items
     * @param Integer $budget
     * @return Integer
     */
    function maximumSaleItems($items, $budget) {
        $maxFactor = 0;
        $minPrice = PHP_INT_MAX;
        foreach ($items as $item) {
            if ($item[0] > $maxFactor) $maxFactor = $item[0];
            if ($item[1] < $minPrice) $minPrice = $item[1];
        }

        $freq = array_fill(0, $maxFactor + 1, 0);
        foreach ($items as $item) {
            $freq[$item[0]]++;
        }

        $count = array_fill(0, $maxFactor + 1, 0);
        for ($i = 1; $i <= $maxFactor; $i++) {
            for ($j = $i; $j <= $maxFactor; $j += $i) {
                $count[$i] += $freq[$j];
            }
        }

        $dp = array_fill(0, $budget + 1, -1);
        $dp[0] = 0;

        foreach ($items as $item) {
            $factor = $item[0];
            $price = $item[1];
            $val = $count[$factor];
            for ($w = $budget; $w >= $price; $w--) {
                if ($dp[$w - $price] != -1) {
                    if ($dp[$w - $price] + $val > $dp[$w]) {
                        $dp[$w] = $dp[$w - $price] + $val;
                    }
                }
            }
        }

        $maxItems = 0;
        for ($w = 0; $w <= $budget; $w++) {
            if ($dp[$w] != -1) {
                $total = $dp[$w] + intdiv($budget - $w, $minPrice);
                if ($total > $maxItems) {
                    $maxItems = $total;
                }
            }
        }

        return $maxItems;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximumSaleItems(_ items: [[Int]], _ budget: Int) -> Int {
        var maxFactor = 0
        var minPrice = Int.max
        for item in items {
            if item[0] > maxFactor { maxFactor = item[0] }
            if item[1] < minPrice { minPrice = item[1] }
        }

        var freq = [Int](repeating: 0, count: maxFactor + 1)
        for item in items {
            freq[item[0]] += 1
        }

        var count = [Int](repeating: 0, count: maxFactor + 1)
        if maxFactor >= 1 {
            for i in 1...maxFactor {
                for j in stride(from: i, through: maxFactor, by: i) {
                    count[i] += freq[j]
                }
            }
        }

        var dp = [Int](repeating: -1, count: budget + 1)
        dp[0] = 0

        for item in items {
            let factor = item[0]
            let price = item[1]
            let val = count[factor]
            if price <= budget {
                for w in stride(from: budget, through: price, by: -1) {
                    if dp[w - price] != -1 {
                        if dp[w - price] + val > dp[w] {
                            dp[w] = dp[w - price] + val
                        }
                    }
                }
            }
        }

        var maxItems = 0
        for w in 0...budget {
            if dp[w] != -1 {
                let total = dp[w] + (budget - w) / minPrice
                if total > maxItems {
                    maxItems = total
                }
            }
        }

        return maxItems
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximumSaleItems(items: Array<IntArray>, budget: Int): Int {
        var maxFactor = 0
        var minPrice = Int.MAX_VALUE
        for (item in items) {
            if (item[0] > maxFactor) maxFactor = item[0]
            if (item[1] < minPrice) minPrice = item[1]
        }

        val freq = IntArray(maxFactor + 1)
        for (item in items) {
            freq[item[0]]++
        }

        val count = IntArray(maxFactor + 1)
        for (i in 1..maxFactor) {
            var j = i
            while (j <= maxFactor) {
                count[i] += freq[j]
                j += i
            }
        }

        val dp = IntArray(budget + 1) { -1 }
        dp[0] = 0

        for (item in items) {
            val factor = item[0]
            val price = item[1]
            val v = count[factor]
            for (w in budget downTo price) {
                if (dp[w - price] != -1) {
                    val cand = dp[w - price] + v
                    if (cand > dp[w]) {
                        dp[w] = cand
                    }
                }
            }
        }

        var maxItems = 0
        for (w in 0..budget) {
            if (dp[w] != -1) {
                val total = dp[w] + (budget - w) / minPrice
                if (total > maxItems) {
                    maxItems = total
                }
            }
        }

        return maxItems
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
  int maximumSaleItems(List<List<int>> items, int budget) {
    int maxFactor = 0;
    int minPrice = 1000000000;
    for (var item in items) {
      if (item[0] > maxFactor) maxFactor = item[0];
      if (item[1] < minPrice) minPrice = item[1];
    }

    List<int> freq = List.filled(maxFactor + 1, 0);
    for (var item in items) {
      freq[item[0]]++;
    }

    List<int> count = List.filled(maxFactor + 1, 0);
    for (int i = 1; i <= maxFactor; i++) {
      for (int j = i; j <= maxFactor; j += i) {
        count[i] += freq[j];
      }
    }

    List<int> dp = List.filled(budget + 1, -1);
    dp[0] = 0;

    for (var item in items) {
      int factor = item[0];
      int price = item[1];
      int val = count[factor];
      for (int w = budget; w >= price; w--) {
        if (dp[w - price] != -1) {
          int cand = dp[w - price] + val;
          if (cand > dp[w]) {
            dp[w] = cand;
          }
        }
      }
    }

    int maxItems = 0;
    for (int w = 0; w <= budget; w++) {
      if (dp[w] != -1) {
        int total = dp[w] + (budget - w) ~/ minPrice;
        if (total > maxItems) {
          maxItems = total;
        }
      }
    }

    return maxItems;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maximumSaleItems(items [][]int, budget int) int {
    maxFactor := 0
    minPrice := int(^uint(0) >> 1)
    for _, item := range items {
        if item[0] > maxFactor {
            maxFactor = item[0]
        }
        if item[1] < minPrice {
            minPrice = item[1]
        }
    }

    freq := make([]int, maxFactor+1)
    for _, item := range items {
        freq[item[0]]++
    }

    count := make([]int, maxFactor+1)
    for i := 1; i <= maxFactor; i++ {
        for j := i; j <= maxFactor; j += i {
            count[i] += freq[j]
        }
    }

    dp := make([]int, budget+1)
    for i := range dp {
        dp[i] = -1
    }
    dp[0] = 0

    for _, item := range items {
        factor := item[0]
        price := item[1]
        val := count[factor]
        for w := budget; w >= price; w-- {
            if dp[w-price] != -1 {
                cand := dp[w-price] + val
                if cand > dp[w] {
                    dp[w] = cand
                }
            }
        }
    }

    maxItems := 0
    for w := 0; w <= budget; w++ {
        if dp[w] != -1 {
            total := dp[w] + (budget-w)/minPrice
            if total > maxItems {
                maxItems = total
            }
        }
    }

    return maxItems
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} items
# @param {Integer} budget
# @return {Integer}
def maximum_sale_items(items, budget)
  max_factor = items.map { |item| item[0] }.max
  min_price = items.map { |item| item[1] }.min

  freq = Array.new(max_factor + 1, 0)
  items.each { |factor, _| freq[factor] += 1 }

  count = Array.new(max_factor + 1, 0)
  (1..max_factor).each do |i|
    (i..max_factor).step(i) do |j|
      count[i] += freq[j]
    end
  end

  dp = Array.new(budget + 1, -1)
  dp[0] = 0

  items.each do |factor, price|
    val = count[factor]
    budget.downto(price) do |w|
      if dp[w - price] != -1
        cand = dp[w - price] + val
        dp[w] = cand if cand > dp[w]
      end
    end
  end

  max_items = 0
  (0..budget).each do |w|
    if dp[w] != -1
      total = dp[w] + (budget - w) / min_price
      max_items = total if total > max_items
    end
  end

  max_items
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximumSaleItems(items: Array[Array[Int]], budget: Int): Int = {
        var maxFactor = 0
        var minPrice = Int.MaxValue
        for (item <- items) {
            if (item(0) > maxFactor) maxFactor = item(0)
            if (item(1) < minPrice) minPrice = item(1)
        }

        val freq = new Array[Int](maxFactor + 1)
        for (item <- items) {
            freq(item(0)) += 1
        }

        val count = new Array[Int](maxFactor + 1)
        for (i <- 1 to maxFactor) {
            var j = i
            while (j <= maxFactor) {
                count(i) += freq(j)
                j += i
            }
        }

        val dp = Array.fill(budget + 1)(-1)
        dp(0) = 0

        for (item <- items) {
            val factor = item(0)
            val price = item(1)
            val v = count(factor)
            var w = budget
            while (w >= price) {
                if (dp(w - price) != -1) {
                    val cand = dp(w - price) + v
                    if (cand > dp(w)) {
                        dp(w) = cand
                    }
                }
                w -= 1
            }
        }

        var maxItems = 0
        for (w <- 0 to budget) {
            if (dp(w) != -1) {
                val total = dp(w) + (budget - w) / minPrice
                if (total > maxItems) {
                    maxItems = total
                }
            }
        }

        maxItems
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximum_sale_items(items: Vec<Vec<i32>>, budget: i32) -> i32 {
        let mut max_factor = 0;
        let mut min_price = i32::MAX;
        for item in &items {
            if item[0] > max_factor { max_factor = item[0]; }
            if item[1] < min_price { min_price = item[1]; }
        }

        let mut freq = vec![0; (max_factor + 1) as usize];
        for item in &items {
            freq[item[0] as usize] += 1;
        }

        let mut count = vec![0; (max_factor + 1) as usize];
        for i in 1..=max_factor as usize {
            for j in (i..=max_factor as usize).step_by(i) {
                count[i] += freq[j];
            }
        }

        let mut dp = vec![-1; (budget + 1) as usize];
        dp[0] = 0;

        for item in &items {
            let f = item[0] as usize;
            let p = item[1] as usize;
            let val = count[f];
            for w in (p..=budget as usize).rev() {
                if dp[w - p] != -1 {
                    let new_val = dp[w - p] + val;
                    if new_val > dp[w] {
                        dp[w] = new_val;
                    }
                }
            }
        }

        let mut max_items = 0;
        for w in 0..=budget as usize {
            if dp[w] != -1 {
                let total = dp[w] + (budget - w as i32) / min_price;
                if total > max_items {
                    max_items = total;
                }
            }
        }

        max_items
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximum-sale-items items budget)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([max-factor (apply max (map first items))]
         [min-price (apply min (map second items))]
         [freq (make-vector (+ max-factor 1) 0)])
    (for ([item items])
      (let ([f (first item)])
        (vector-set! freq f (+ (vector-ref freq f) 1))))
    (define count (make-vector (+ max-factor 1) 0))
    (for ([i (in-range 1 (+ max-factor 1))])
      (for ([j (in-range i (+ max-factor 1) i)])
        (vector-set! count i (+ (vector-ref count i) (vector-ref freq j)))))
    (define dp (make-vector (+ budget 1) -1))
    (vector-set! dp 0 0)
    (for ([item items])
      (let* ([f (first item)]
             [p (second item)]
             [val (vector-ref count f)])
        (for ([w (in-range budget (- p 1) -1)])
          (let ([prev (vector-ref dp (- w p))])
            (when (not (= prev -1))
              (vector-set! dp w (max (vector-ref dp w) (+ prev val))))))))
    (let ([max-items 0])
      (for ([w (in-range (+ budget 1))])
        (let ([val (vector-ref dp w)])
          (when (not (= val -1))
            (let ([total (+ val (quotient (- budget w) min-price))])
              (set! max-items (max max-items total))))))
      max-items)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_sale_items(Items :: [[integer()]], Budget :: integer()) -> integer().
maximum_sale_items(Items, Budget) ->
    {MaxFactor, MinPrice} = lists:foldl(fun([F, P], {MF, MP}) ->
        {erlang:max(F, MF), erlang:min(P, MP)}
    end, {0, 1000000}, Items),

    Freq = lists:foldl(fun([F, _], Acc) ->
        Acc#{F => maps:get(F, Acc, 0) + 1}
    end, #{}, Items),

    CountList = [0 | [lists:sum([maps:get(J, Freq, 0) || J <- lists:seq(I, MaxFactor, I)]) || I <- lists:seq(1, MaxFactor)]],
    Count = list_to_tuple(CountList),

    InitialDP = list_to_tuple([-1 || _ <- lists:seq(0, Budget)]),
    DP0 = setelement(1, InitialDP, 0),

    FinalDP = lists:foldl(fun([F, P], AccDP) ->
        Val = element(F + 1, Count),
        ListForNewDP = [begin
            OldVal = element(W + 1, AccDP),
            if W >= P ->
                PrevVal = element(W - P + 1, AccDP),
                if PrevVal =:= -1 -> OldVal;
                   true -> erlang:max(OldVal, PrevVal + Val)
                end;
               true -> OldVal
            end
        end || W <- lists:seq(0, Budget)],
        list_to_tuple(ListForNewDP)
    end, DP0, Items),

    lists:foldl(fun(W, MaxAcc) ->
        case element(W + 1, FinalDP) of
            -1 -> MaxAcc;
            V -> erlang:max(MaxAcc, V + (Budget - W) div MinPrice)
        end
    end, 0, lists:seq(0, Budget)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_sale_items(items :: [[integer]], budget :: integer) :: integer
  def maximum_sale_items(items, budget) do
    max_factor = items |> Enum.map(fn [f, _] -> f end) |> Enum.max()
    min_price = items |> Enum.map(fn [_, p] -> p end) |> Enum.min()

    freq = Enum.reduce(items, %{}, fn [f, _], acc ->
      Map.put(acc, f, Map.get(acc, f, 0) + 1)
    end)

    count_list = [0 | for i <- 1..max_factor do
      Enum.take_every(i..max_factor, i)
      |> Enum.reduce(0, fn j, acc -> acc + Map.get(freq, j, 0) end)
    end]
    count = List.to_tuple(count_list)

    initial_dp = List.to_tuple(for _ <- 0..budget, do: -1)
    dp0 = put_elem(initial_dp, 0, 0)

    final_dp = Enum.reduce(items, dp0, fn [f, p], acc_dp ->
      val = elem(count, f)
      new_dp_list = for w <- 0..budget do
        old_val = elem(acc_dp, w)
        if w >= p do
          prev_val = elem(acc_dp, w - p)
          if prev_val == -1, do: old_val, else: max(old_val, prev_val + val)
        else
          old_val
        end
      end
      List.to_tuple(new_dp_list)
    end)

    0..budget
    |> Enum.reduce(0, fn w, max_acc ->
      case elem(final_dp, w) do
        -1 -> max_acc
        v -> max(max_acc, v + div(budget - w, min_price))
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N \cdot \text{budget} + M \log M) where $N$ is the number of items, $\text{budget}$ is the given budget, and $M = \max(\text{factor}_i) \le 1500$. Precomputing the multiple counts takes $O(M \log M + N)$ time, and the 0-1 knapsack DP takes $O(N \cdot \text{budget})$ time, which easily runs within the time limits.
- **Space Complexity:** O(\text{budget} + M) auxiliary space to store the knapsack DP array of size $\text{budget} + 1$ and the factor frequencies array of size up to 1501.
