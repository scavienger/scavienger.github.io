---
layout: post
title: "Maximum Number of Items From Sale II"
date: 2026-11-28 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy", "Sorting", "Heap (Priority Queue)"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maximumSaleItems(vector<vector<int>>&\
        \ items, int budget) {\n        int n = items.size();\n        vector<int> cnt(n\
        \ + 1, 0);\n        long long min_p = items[0][1];\n        for (const auto&\
        \ it : items) {\n            cnt[it[0]]++;\n            if (it[1] < min_p) {\n\
        \                min_p = it[1];\n            }\n        }\n\n        vector<int>\
        \ mult(n + 1, 0);\n        for (int f = 1; f <= n; ++f) {\n            for (int\
        \ k = f; k <= n; k += f) {\n                mult[f] += cnt[k];\n           \
        \ }\n        }\n\n        vector<pair<long long, int>> candidates;\n       \
        \ for (int i = 0; i < n; ++i) {\n            int gain = mult[items[i][0]] -\
        \ 1;\n            long long price = items[i][1];\n            if (gain > 0 &&\
        \ price < 2 * min_p) {\n                candidates.push_back({price, gain});\n\
        \            }\n        }\n\n        sort(candidates.begin(), candidates.end());\n\
        \n        long long b = budget;\n        long long ans = 0;\n        for (const\
        \ auto& cand : candidates) {\n            long long price = cand.first;\n  \
        \          long long count = cand.second;\n            long long take = min(count,\
        \ b / price);\n            ans += take * 2;\n            b -= take * price;\n\
        \            if (take < count) {\n                break;\n            }\n  \
        \      }\n\n        ans += b / min_p;\n        return (int)ans;\n    }\n};"
      java: "class Solution {\n    public int maximumSaleItems(int[][] items, int budget)\
        \ {\n        int n = items.length;\n        int[] cnt = new int[n + 1];\n  \
        \      long minP = items[0][1];\n        for (int[] it : items) {\n        \
        \    cnt[it[0]]++;\n            if (it[1] < minP) {\n                minP =\
        \ it[1];\n            }\n        }\n\n        int[] mult = new int[n + 1];\n\
        \        for (int f = 1; f <= n; ++f) {\n            for (int k = f; k <= n;\
        \ k += f) {\n                mult[f] += cnt[k];\n            }\n        }\n\n\
        \        long[][] candidates = new long[n][2];\n        int candSize = 0;\n\
        \        for (int i = 0; i < n; ++i) {\n            int gain = mult[items[i][0]]\
        \ - 1;\n            long price = items[i][1];\n            if (gain > 0 && price\
        \ < 2 * minP) {\n                candidates[candSize][0] = price;\n        \
        \        candidates[candSize][1] = gain;\n                candSize++;\n    \
        \        }\n        }\n\n        java.util.Arrays.sort(candidates, 0, candSize,\
        \ (a, b) -> Long.compare(a[0], b[0]));\n\n        long b = budget;\n       \
        \ long ans = 0;\n        for (int i = 0; i < candSize; ++i) {\n            long\
        \ price = candidates[i][0];\n            long count = candidates[i][1];\n  \
        \          long take = Math.min(count, b / price);\n            ans += take\
        \ * 2;\n            b -= take * price;\n            if (take < count) {\n  \
        \              break;\n            }\n        }\n\n        ans += b / minP;\n\
        \        return (int) ans;\n    }\n}"
      python: "class Solution(object):\n    def maximumSaleItems(self, items, budget):\n\
        \        \"\"\"\n        :type items: List[List[int]]\n        :type budget:\
        \ int\n        :rtype: int\n        \"\"\"\n        n = len(items)\n       \
        \ cnt = [0] * (n + 1)\n        min_p = items[0][1]\n        for f, p in items:\n\
        \            cnt[f] += 1\n            if p < min_p:\n                min_p =\
        \ p\n\n        mult = [0] * (n + 1)\n        for f in range(1, n + 1):\n   \
        \         for k in range(f, n + 1, f):\n                mult[f] += cnt[k]\n\n\
        \        threshold = 2 * min_p\n        candidates = []\n        for f, p in\
        \ items:\n            gain = mult[f] - 1\n            if gain > 0 and p < threshold:\n\
        \                candidates.append((p, gain))\n\n        candidates.sort(key=lambda\
        \ x: x[0])\n\n        b = budget\n        ans = 0\n        for price, count\
        \ in candidates:\n            take = min(count, b // price)\n            ans\
        \ += take * 2\n            b -= take * price\n            if take < count:\n\
        \                break\n\n        ans += b // min_p\n        return ans"
      python3: "class Solution:\n    def maximumSaleItems(self, items: List[List[int]],\
        \ budget: int) -> int:\n        n = len(items)\n        cnt = [0] * (n + 1)\n\
        \        min_p = items[0][1]\n        for f, p in items:\n            cnt[f]\
        \ += 1\n            if p < min_p:\n                min_p = p\n\n        mult\
        \ = [0] * (n + 1)\n        for f in range(1, n + 1):\n            for k in range(f,\
        \ n + 1, f):\n                mult[f] += cnt[k]\n\n        threshold = 2 * min_p\n\
        \        candidates = []\n        for f, p in items:\n            gain = mult[f]\
        \ - 1\n            if gain > 0 and p < threshold:\n                candidates.append((p,\
        \ gain))\n\n        candidates.sort(key=lambda x: x[0])\n\n        b = budget\n\
        \        ans = 0\n        for price, count in candidates:\n            take\
        \ = min(count, b // price)\n            ans += take * 2\n            b -= take\
        \ * price\n            if take < count:\n                break\n\n        ans\
        \ += b // min_p\n        return ans"
      c: "typedef struct {\n    long long price;\n    int count;\n} Candidate;\n\nint\
        \ compareCandidates(const void* a, const void* b) {\n    long long pa = ((const\
        \ Candidate*)a)->price;\n    long long pb = ((const Candidate*)b)->price;\n\
        \    if (pa < pb) return -1;\n    if (pa > pb) return 1;\n    return 0;\n}\n\
        \nint maximumSaleItems(int** items, int itemsSize, int* itemsColSize, int budget)\
        \ {\n    int n = itemsSize;\n    int* cnt = (int*)calloc(n + 1, sizeof(int));\n\
        \    long long min_p = items[0][1];\n    for (int i = 0; i < n; ++i) {\n   \
        \     cnt[items[i][0]]++;\n        if (items[i][1] < min_p) {\n            min_p\
        \ = items[i][1];\n        }\n    }\n\n    int* mult = (int*)calloc(n + 1, sizeof(int));\n\
        \    for (int f = 1; f <= n; ++f) {\n        for (int k = f; k <= n; k += f)\
        \ {\n            mult[f] += cnt[k];\n        }\n    }\n\n    Candidate* candidates\
        \ = (Candidate*)malloc(n * sizeof(Candidate));\n    int candSize = 0;\n    for\
        \ (int i = 0; i < n; ++i) {\n        int gain = mult[items[i][0]] - 1;\n   \
        \     long long price = items[i][1];\n        if (gain > 0 && price < 2 * min_p)\
        \ {\n            candidates[candSize].price = price;\n            candidates[candSize].count\
        \ = gain;\n            candSize++;\n        }\n    }\n\n    qsort(candidates,\
        \ candSize, sizeof(Candidate), compareCandidates);\n\n    long long b = budget;\n\
        \    long long ans = 0;\n    for (int i = 0; i < candSize; ++i) {\n        long\
        \ long price = candidates[i].price;\n        long long count = candidates[i].count;\n\
        \        long long take = count < (b / price) ? count : (b / price);\n     \
        \   ans += take * 2;\n        b -= take * price;\n        if (take < count)\
        \ {\n            break;\n        }\n    }\n\n    ans += b / min_p;\n\n    free(cnt);\n\
        \    free(mult);\n    free(candidates);\n\n    return (int)ans;\n}"
      csharp: "public class Solution {\n    public int MaximumSaleItems(int[][] items,\
        \ int budget) {\n        int n = items.Length;\n        int[] cnt = new int[n\
        \ + 1];\n        long minP = items[0][1];\n        foreach (var item in items)\
        \ {\n            cnt[item[0]]++;\n            if (item[1] < minP) {\n      \
        \          minP = item[1];\n            }\n        }\n\n        int[] mult =\
        \ new int[n + 1];\n        for (int f = 1; f <= n; f++) {\n            for (int\
        \ k = f; k <= n; k += f) {\n                mult[f] += cnt[k];\n           \
        \ }\n        }\n\n        long threshold = 2 * minP;\n        List<(long price,\
        \ long count)> candidates = new List<(long, long)>();\n        foreach (var\
        \ item in items) {\n            int gain = mult[item[0]] - 1;\n            if\
        \ (gain > 0 && item[1] < threshold) {\n                candidates.Add((item[1],\
        \ gain));\n            }\n        }\n\n        candidates.Sort((a, b) => a.price.CompareTo(b.price));\n\
        \n        long b = budget;\n        long ans = 0;\n        foreach (var (price,\
        \ count) in candidates) {\n            long take = count < b / price ? count\
        \ : b / price;\n            ans += take * 2;\n            b -= take * price;\n\
        \            if (take < count) {\n                break;\n            }\n  \
        \      }\n\n        ans += b / minP;\n        return (int)ans;\n    }\n}"
      javascript: "/**\n * @param {number[][]} items\n * @param {number} budget\n *\
        \ @return {number}\n */\nvar maximumSaleItems = function(items, budget) {\n\
        \    const n = items.length;\n    const cnt = new Int32Array(n + 1);\n    let\
        \ minP = items[0][1];\n    for (let i = 0; i < n; i++) {\n        cnt[items[i][0]]++;\n\
        \        if (items[i][1] < minP) {\n            minP = items[i][1];\n      \
        \  }\n    }\n\n    const mult = new Int32Array(n + 1);\n    for (let f = 1;\
        \ f <= n; f++) {\n        for (let k = f; k <= n; k += f) {\n            mult[f]\
        \ += cnt[k];\n        }\n    }\n\n    const threshold = 2 * minP;\n    const\
        \ candidates = [];\n    for (let i = 0; i < n; i++) {\n        const gain =\
        \ mult[items[i][0]] - 1;\n        if (gain > 0 && items[i][1] < threshold) {\n\
        \            candidates.push([items[i][1], gain]);\n        }\n    }\n\n   \
        \ candidates.sort((a, b) => a[0] - b[0]);\n\n    let b = budget;\n    let ans\
        \ = 0;\n    for (let i = 0; i < candidates.length; i++) {\n        const price\
        \ = candidates[i][0];\n        const count = candidates[i][1];\n        const\
        \ take = Math.min(count, Math.floor(b / price));\n        ans += take * 2;\n\
        \        b -= take * price;\n        if (take < count) {\n            break;\n\
        \        }\n    }\n\n    ans += Math.floor(b / minP);\n    return ans;\n};"
      typescript: "function maximumSaleItems(items: number[][], budget: number): number\
        \ {\n    const n = items.length;\n    const cnt = new Int32Array(n + 1);\n \
        \   let minP = items[0][1];\n    for (let i = 0; i < n; i++) {\n        cnt[items[i][0]]++;\n\
        \        if (items[i][1] < minP) {\n            minP = items[i][1];\n      \
        \  }\n    }\n\n    const mult = new Int32Array(n + 1);\n    for (let f = 1;\
        \ f <= n; f++) {\n        for (let k = f; k <= n; k += f) {\n            mult[f]\
        \ += cnt[k];\n        }\n    }\n\n    const threshold = 2 * minP;\n    const\
        \ candidates: [number, number][] = [];\n    for (let i = 0; i < n; i++) {\n\
        \        const gain = mult[items[i][0]] - 1;\n        if (gain > 0 && items[i][1]\
        \ < threshold) {\n            candidates.push([items[i][1], gain]);\n      \
        \  }\n    }\n\n    candidates.sort((a, b) => a[0] - b[0]);\n\n    let b = budget;\n\
        \    let ans = 0;\n    for (let i = 0; i < candidates.length; i++) {\n     \
        \   const price = candidates[i][0];\n        const count = candidates[i][1];\n\
        \        const take = Math.min(count, Math.floor(b / price));\n        ans +=\
        \ take * 2;\n        b -= take * price;\n        if (take < count) {\n     \
        \       break;\n        }\n    }\n\n    ans += Math.floor(b / minP);\n    return\
        \ ans;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $items\n     * @param\
        \ Integer $budget\n     * @return Integer\n     */\n    function maximumSaleItems($items,\
        \ $budget) {\n        $n = count($items);\n        $cnt = array_fill(0, $n +\
        \ 1, 0);\n        $minP = $items[0][1];\n        foreach ($items as $item) {\n\
        \            $cnt[$item[0]]++;\n            if ($item[1] < $minP) {\n      \
        \          $minP = $item[1];\n            }\n        }\n\n        $mult = array_fill(0,\
        \ $n + 1, 0);\n        for ($f = 1; $f <= $n; $f++) {\n            for ($k =\
        \ $f; $k <= $n; $k += $f) {\n                $mult[$f] += $cnt[$k];\n      \
        \      }\n        }\n\n        $threshold = 2 * $minP;\n        $candidates\
        \ = [];\n        foreach ($items as $item) {\n            $gain = $mult[$item[0]]\
        \ - 1;\n            if ($gain > 0 && $item[1] < $threshold) {\n            \
        \    $candidates[] = [$item[1], $gain];\n            }\n        }\n\n      \
        \  usort($candidates, function($a, $b) {\n            return $a[0] <=> $b[0];\n\
        \        });\n\n        $b = $budget;\n        $ans = 0;\n        foreach ($candidates\
        \ as $cand) {\n            $price = $cand[0];\n            $count = $cand[1];\n\
        \            $take = min($count, intdiv($b, $price));\n            $ans += $take\
        \ * 2;\n            $b -= $take * $price;\n            if ($take < $count) {\n\
        \                break;\n            }\n        }\n\n        $ans += intdiv($b,\
        \ $minP);\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func maximumSaleItems(_ items: [[Int]], _ budget:\
        \ Int) -> Int {\n        let n = items.count\n        var cnt = [Int](repeating:\
        \ 0, count: n + 1)\n        var minP = items[0][1]\n        for item in items\
        \ {\n            cnt[item[0]] += 1\n            if item[1] < minP {\n      \
        \          minP = item[1]\n            }\n        }\n\n        var mult = [Int](repeating:\
        \ 0, count: n + 1)\n        for f in 1...n {\n            var k = f\n      \
        \      while k <= n {\n                mult[f] += cnt[k]\n                k\
        \ += f\n            }\n        }\n\n        let threshold = 2 * minP\n     \
        \   var candidates = [(price: Int, count: Int)]()\n        for item in items\
        \ {\n            let gain = mult[item[0]] - 1\n            if gain > 0 && item[1]\
        \ < threshold {\n                candidates.append((item[1], gain))\n      \
        \      }\n        }\n\n        candidates.sort { $0.price < $1.price }\n\n \
        \       var b = budget\n        var ans = 0\n        for cand in candidates\
        \ {\n            let take = min(cand.count, b / cand.price)\n            ans\
        \ += take * 2\n            b -= take * cand.price\n            if take < cand.count\
        \ {\n                break\n            }\n        }\n\n        ans += b / minP\n\
        \        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun maximumSaleItems(items: Array<IntArray>, budget:\
        \ Int): Int {\n        val n = items.size\n        val cnt = IntArray(n + 1)\n\
        \        var minP = items[0][1].toLong()\n        for (item in items) {\n  \
        \          cnt[item[0]]++\n            if (item[1].toLong() < minP) {\n    \
        \            minP = item[1].toLong()\n            }\n        }\n\n        val\
        \ mult = IntArray(n + 1)\n        for (f in 1..n) {\n            var k = f\n\
        \            while (k <= n) {\n                mult[f] += cnt[k]\n         \
        \       k += f\n            }\n        }\n\n        val threshold = 2L * minP\n\
        \        val candidates = ArrayList<LongArray>()\n        for (item in items)\
        \ {\n            val f = item[0]\n            val p = item[1].toLong()\n   \
        \         val gain = (mult[f] - 1).toLong()\n            if (gain > 0 && p <\
        \ threshold) {\n                candidates.add(longArrayOf(p, gain))\n     \
        \       }\n        }\n\n        candidates.sortWith(compareBy { it[0] })\n\n\
        \        var b = budget.toLong()\n        var ans = 0L\n        for (cand in\
        \ candidates) {\n            val price = cand[0]\n            val count = cand[1]\n\
        \            val take = minOf(count, b / price)\n            ans += take * 2L\n\
        \            b -= take * price\n            if (take < count) {\n          \
        \      break\n            }\n        }\n\n        ans += b / minP\n        return\
        \ ans.toInt()\n    }\n}"
      dart: "class Solution {\n  int maximumSaleItems(List<List<int>> items, int budget)\
        \ {\n    final n = items.length;\n    final cnt = List<int>.filled(n + 1, 0);\n\
        \    int minP = items[0][1];\n    for (final item in items) {\n      cnt[item[0]]++;\n\
        \      if (item[1] < minP) {\n        minP = item[1];\n      }\n    }\n\n  \
        \  final mult = List<int>.filled(n + 1, 0);\n    for (int f = 1; f <= n; f++)\
        \ {\n      for (int k = f; k <= n; k += f) {\n        mult[f] += cnt[k];\n \
        \     }\n    }\n\n    final threshold = 2 * minP;\n    final candidates = <List<int>>[];\n\
        \    for (final item in items) {\n      final f = item[0];\n      final p =\
        \ item[1];\n      final gain = mult[f] - 1;\n      if (gain > 0 && p < threshold)\
        \ {\n        candidates.add([p, gain]);\n      }\n    }\n\n    candidates.sort((a,\
        \ b) => a[0].compareTo(b[0]));\n\n    int b = budget;\n    int ans = 0;\n  \
        \  for (final cand in candidates) {\n      final price = cand[0];\n      final\
        \ count = cand[1];\n      final take = (b ~/ price < count) ? b ~/ price : count;\n\
        \      ans += take * 2;\n      b -= take * price;\n      if (take < count) {\n\
        \        break;\n      }\n    }\n\n    ans += b ~/ minP;\n    return ans;\n\
        \  }\n}"
      go: "package main\n\nimport \"sort\"\n\nfunc maximumSaleItems(items [][]int, budget\
        \ int) int {\n    n := len(items)\n    cnt := make([]int, n+1)\n    minP :=\
        \ int64(items[0][1])\n    for _, item := range items {\n        cnt[item[0]]++\n\
        \        if int64(item[1]) < minP {\n            minP = int64(item[1])\n   \
        \     }\n    }\n\n    mult := make([]int, n+1)\n    for f := 1; f <= n; f++\
        \ {\n        for k := f; k <= n; k += f {\n            mult[f] += cnt[k]\n \
        \       }\n    }\n\n    threshold := 2 * minP\n    type cand struct {\n    \
        \    price int64\n        count int64\n    }\n    var candidates []cand\n  \
        \  for _, item := range items {\n        f := item[0]\n        p := int64(item[1])\n\
        \        gain := int64(mult[f] - 1)\n        if gain > 0 && p < threshold {\n\
        \            candidates = append(candidates, cand{price: p, count: gain})\n\
        \        }\n    }\n\n    sort.Slice(candidates, func(i, j int) bool {\n    \
        \    return candidates[i].price < candidates[j].price\n    })\n\n    b := int64(budget)\n\
        \    var ans int64 = 0\n    for _, c := range candidates {\n        take :=\
        \ b / c.price\n        if c.count < take {\n            take = c.count\n   \
        \     }\n        ans += take * 2\n        b -= take * c.price\n        if take\
        \ < c.count {\n            break\n        }\n    }\n\n    ans += b / minP\n\
        \    return int(ans)\n}"
      ruby: "# @param {Integer[][]} items\n# @param {Integer} budget\n# @return {Integer}\n\
        def maximum_sale_items(items, budget)\n    n = items.length\n    cnt = Array.new(n\
        \ + 1, 0)\n    min_p = items[0][1]\n    items.each do |f, p|\n        cnt[f]\
        \ += 1\n        min_p = p if p < min_p\n    end\n\n    mult = Array.new(n +\
        \ 1, 0)\n    (1..n).each do |f|\n        k = f\n        while k <= n\n     \
        \       mult[f] += cnt[k]\n            k += f\n        end\n    end\n\n    threshold\
        \ = 2 * min_p\n    candidates = []\n    items.each do |f, p|\n        gain =\
        \ mult[f] - 1\n        if gain > 0 && p < threshold\n            candidates\
        \ << [p, gain]\n        end\n    end\n\n    candidates.sort_by! { |x| x[0] }\n\
        \n    b = budget\n    ans = 0\n    candidates.each do |price, count|\n     \
        \   take = [count, b / price].min\n        ans += take * 2\n        b -= take\
        \ * price\n        break if take < count\n    end\n\n    ans += b / min_p\n\
        \    ans\nend"
      scala: "object Solution {\n    def maximumSaleItems(items: Array[Array[Int]],\
        \ budget: Int): Int = {\n        val n = items.length\n        val cnt = new\
        \ Array[Int](n + 1)\n        var minP = items(0)(1).toLong\n        for (item\
        \ <- items) {\n            cnt(item(0)) += 1\n            if (item(1).toLong\
        \ < minP) {\n                minP = item(1).toLong\n            }\n        }\n\
        \n        val mult = new Array[Int](n + 1)\n        for (f <- 1 to n) {\n  \
        \          var k = f\n            while (k <= n) {\n                mult(f)\
        \ += cnt(k)\n                k += f\n            }\n        }\n\n        val\
        \ threshold = 2L * minP\n        val candidates = scala.collection.mutable.ArrayBuffer[(Long,\
        \ Long)]()\n        for (item <- items) {\n            val f = item(0)\n   \
        \         val p = item(1).toLong\n            val gain = (mult(f) - 1).toLong\n\
        \            if (gain > 0 && p < threshold) {\n                candidates +=\
        \ ((p, gain))\n            }\n        }\n\n        val sortedCandidates = candidates.sortBy(_._1)\n\
        \n        var b = budget.toLong\n        var ans = 0L\n        var i = 0\n \
        \       var stop = false\n        while (i < sortedCandidates.length && !stop)\
        \ {\n            val (price, count) = sortedCandidates(i)\n            val take\
        \ = math.min(count, b / price)\n            ans += take * 2L\n            b\
        \ -= take * price\n            if (take < count) {\n                stop = true\n\
        \            }\n            i += 1\n        }\n\n        ans += b / minP\n \
        \       ans.toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn maximum_sale_items(items: Vec<Vec<i32>>, budget:\
        \ i32) -> i32 {\n        let n = items.len();\n        let mut cnt = vec![0i32;\
        \ n + 1];\n        let mut min_p = items[0][1] as i64;\n        for item in\
        \ &items {\n            let f = item[0] as usize;\n            let p = item[1]\
        \ as i64;\n            cnt[f] += 1;\n            if p < min_p {\n          \
        \      min_p = p;\n            }\n        }\n\n        let mut mult = vec![0i32;\
        \ n + 1];\n        for f in 1..=n {\n            let mut k = f;\n          \
        \  while k <= n {\n                mult[f] += cnt[k];\n                k +=\
        \ f;\n            }\n        }\n\n        let threshold = 2 * min_p;\n     \
        \   let mut candidates = Vec::new();\n        for item in &items {\n       \
        \     let f = item[0] as usize;\n            let p = item[1] as i64;\n     \
        \       let gain = mult[f] - 1;\n            if gain > 0 && p < threshold {\n\
        \                candidates.push((p, gain as i64));\n            }\n       \
        \ }\n\n        candidates.sort_unstable_by_key(|&(p, _)| p);\n\n        let\
        \ mut b = budget as i64;\n        let mut ans = 0i64;\n        for (price, count)\
        \ in candidates {\n            let take = count.min(b / price);\n          \
        \  ans += take * 2;\n            b -= take * price;\n            if take < count\
        \ {\n                break;\n            }\n        }\n\n        ans += b /\
        \ min_p;\n        ans as i32\n    }\n}"
      racket: "(define/contract (maximum-sale-items items budget)\n  (-> (listof (listof\
        \ exact-integer?)) exact-integer? exact-integer?)\n  (let* ([n (length items)]\n\
        \         [cnt (make-vector (+ n 1) 0)]\n         [min-p (second (first items))])\n\
        \    (for ([item (in-list items)])\n      (let ([f (first item)]\n         \
        \   [p (second item)])\n        (vector-set! cnt f (+ (vector-ref cnt f) 1))\n\
        \        (when (< p min-p)\n          (set! min-p p))))\n    (let ([mult (make-vector\
        \ (+ n 1) 0)])\n      (for ([f (in-range 1 (+ n 1))])\n        (let ([sum 0])\n\
        \          (for ([k (in-range f (+ n 1) f)])\n            (set! sum (+ sum (vector-ref\
        \ cnt k))))\n          (vector-set! mult f sum)))\n      (let* ([threshold (*\
        \ 2 min-p)]\n             [candidates '()])\n        (for ([item (in-list items)])\n\
        \          (let* ([f (first item)]\n                 [p (second item)]\n   \
        \              [gain (- (vector-ref mult f) 1)])\n            (when (and (>\
        \ gain 0) (< p threshold))\n              (set! candidates (cons (cons p gain)\
        \ candidates)))))\n        (let ([sorted-cand (sort candidates < #:key car)])\n\
        \          (let loop ([cand sorted-cand] [b budget] [ans 0])\n            (cond\n\
        \              [(null? cand) (+ ans (quotient b min-p))]\n              [else\n\
        \               (let* ([cg (car cand)]\n                      [price (car cg)]\n\
        \                      [count (cdr cg)]\n                      [take (min count\
        \ (quotient b price))]\n                      [new-ans (+ ans (* take 2))]\n\
        \                      [new-b (- b (* take price))])\n                 (if (<\
        \ take count)\n                     (+ new-ans (quotient new-b min-p))\n   \
        \                  (loop (cdr cand) new-b new-ans)))])))))))"
      erlang: "-spec maximum_sale_items(Items :: [[integer()]], Budget :: integer())\
        \ -> integer().\nmaximum_sale_items(Items, Budget) ->\n    N = length(Items),\n\
        \    {Cnt, MinP} = lists:foldl(fun([F, P], {AccCnt, AccMin}) ->\n        NewCnt\
        \ = maps:update_with(F, fun(V) -> V + 1 end, 1, AccCnt),\n        NewMin = case\
        \ AccMin of\n            undefined -> P;\n            _ -> min(AccMin, P)\n\
        \        end,\n        {NewCnt, NewMin}\n    end, {#{}, undefined}, Items),\n\
        \n    DistinctF = maps:keys(Cnt),\n    Mult = lists:foldl(fun(F, Acc) ->\n \
        \       Sum = sum_multiples(F, F, N, Cnt, 0),\n        maps:put(F, Sum, Acc)\n\
        \    end, #{}, DistinctF),\n\n    Threshold = 2 * MinP,\n    Candidates = lists:foldl(fun([F,\
        \ P], Acc) ->\n        Gain = maps:get(F, Mult) - 1,\n        case Gain > 0\
        \ andalso P < Threshold of\n            true -> [{P, Gain} | Acc];\n       \
        \     false -> Acc\n        end\n    end, [], Items),\n\n    Sorted = lists:sort(fun({P1,\
        \ _}, {P2, _}) -> P1 =< P2 end, Candidates),\n\n    {RemB, Ans} = take_items(Sorted,\
        \ Budget, 0),\n    Ans + (RemB div MinP).\n\nsum_multiples(K, _Step, Max, _Cnt,\
        \ Acc) when K > Max ->\n    Acc;\nsum_multiples(K, Step, Max, Cnt, Acc) ->\n\
        \    Val = maps:get(K, Cnt, 0),\n    sum_multiples(K + Step, Step, Max, Cnt,\
        \ Acc + Val).\n\ntake_items([], B, Ans) ->\n    {B, Ans};\ntake_items([{Price,\
        \ Count} | Rest], B, Ans) ->\n    Take = min(Count, B div Price),\n    NewAns\
        \ = Ans + Take * 2,\n    NewB = B - Take * Price,\n    case Take < Count of\n\
        \        true -> {NewB, NewAns};\n        false -> take_items(Rest, NewB, NewAns)\n\
        \    end."
      elixir: "defmodule Solution do\n  @spec maximum_sale_items(items :: [[integer]],\
        \ budget :: integer) :: integer\n  def maximum_sale_items(items, budget) do\n\
        \    n = length(items)\n\n    {cnt, min_p} = \n      Enum.reduce(items, {%{},\
        \ nil}, fn [f, p], {acc_cnt, acc_min} ->\n        new_cnt = Map.update(acc_cnt,\
        \ f, 1, &(&1 + 1))\n        new_min = if is_nil(acc_min) or p < acc_min, do:\
        \ p, else: acc_min\n        {new_cnt, new_min}\n      end)\n\n    mult =\n \
        \     Enum.reduce(Map.keys(cnt), %{}, fn f, acc ->\n        sum = sum_multiples(f,\
        \ f, n, cnt, 0)\n        Map.put(acc, f, sum)\n      end)\n\n    threshold =\
        \ 2 * min_p\n\n    candidates =\n      Enum.reduce(items, [], fn [f, p], acc\
        \ ->\n        gain = Map.get(mult, f, 0) - 1\n        if gain > 0 and p < threshold\
        \ do\n          [{p, gain} | acc]\n        else\n          acc\n        end\n\
        \      end)\n      |> Enum.sort_by(fn {p, _gain} -> p end)\n\n    {rem_b, ans}\
        \ =\n      Enum.reduce_while(candidates, {budget, 0}, fn {price, count}, {b,\
        \ total} ->\n        take = min(count, div(b, price))\n        new_total = total\
        \ + take * 2\n        new_b = b - take * price\n        if take < count do\n\
        \          {:halt, {new_b, new_total}}\n        else\n          {:cont, {new_b,\
        \ new_total}}\n        end\n      end)\n\n    ans + div(rem_b, min_p)\n  end\n\
        \n  defp sum_multiples(k, step, max, cnt, acc) do\n    if k > max do\n     \
        \ acc\n    else\n      val = Map.get(cnt, k, 0)\n      sum_multiples(k + step,\
        \ step, max, cnt, acc + val)\n    end\n  end\nend"
    approach: 'Each purchased copy of an item type $i$ provides one copy directly and
      can yield at most one free copy of another item type $j$ where $factor_i$ divides
      $factor_j$ and $i \ne j$. Since each distinct valid $j$ can be claimed at most
      once by item type $i$, purchasing $c$ copies of item $i$ yields $c + \min(c, gain[i])$
      total items, where $gain[i]$ is the count of other items whose factors are multiples
      of $factor_i$. Because different item types can claim the same item $j$ independently,
      the first $gain[i]$ copies of item $i$ effectively grant 2 item copies each at
      the cost of $price_i$, while all subsequent copies grant 1 item copy each at $price_i$.
      Any value-1 copies should always be purchased from the globally cheapest item
      with minimum price $min\_p$.


      Furthermore, purchasing a value-2 unit at cost $P$ is always preferable to (or
      equal to) buying value-1 items as long as $P < 2 \times min\_p$. This is because
      replacing value-1 items with a value-2 item never decreases the total item count.
      Consequently, we can compute $gain[i]$ for all items using a sieve-like divisor
      counting in $O(n \log n)$ time, collect all item types with $gain[i] > 0$ and
      $price_i < 2 \times min\_p$, sort them in ascending order of price, and greedily
      purchase their value-2 units in batches. Finally, any leftover budget is spent
      on value-1 units of the cheapest item.'
    time_complexity: O(n \log n) where n is the number of items. Computing the count
      of multiples for each factor takes O(n \log n) via harmonic series iteration,
      and sorting the filtered candidate items by price takes O(n \log n). The greedy
      batch processing takes O(n) time.
    space_complexity: O(n) auxiliary space to store factor frequency counts, precomputed
      multiple counts, and the list of value-2 candidate items.
    elapsed_time: 883.7500214576721
    model: gemini-3.8-flash
    generated_at: '2026-11-28 05:59:24 '
---

## Problem #3947: Maximum Number of Items From Sale II

**Difficulty:** Medium

**Topics:** Array, Greedy, Sorting, Heap (Priority Queue)

## Problem Description

<p>You are given a 2D integer array <code>items</code>, where <code>items[i] = [factor<sub>i</sub>, price<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> item. You are also given an integer <code>budget</code>.</p>

<p>There are unlimited copies of each item available for purchase. You may buy any number of copies of any items such that the total cost of the purchased copies is at most <code>budget</code>.</p>

<p>After buying items, you may receive free copies according to the following rules:</p>

<ul>
	<li>Each purchased copy of item <code>i</code> can give you <strong>at most one</strong> free copy of another item <code>j</code>.</li>
	<li>The free item must satisfy <code>i != j</code> and <code>factor<sub>i</sub></code> divides <code>factor<sub>j</sub></code>.</li>
	<li>For each ordered pair <code>(i, j)</code>, you can receive a free copy of item <code>j</code> from purchases of item <code>i</code> <strong>at most once</strong>, regardless of how many copies of item <code>i</code> you buy.</li>
	<li>The same item <code>j</code> can be received multiple times for free if it is received from purchases of different item types.</li>
</ul>

<p>Return the <strong>maximum total number of item copies</strong> you can obtain, including both purchased copies and free copies, while spending at most <code>budget</code> on purchased items.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">items = [[1,6],[2,4],[3,5]], budget = 19</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>You can buy 2 copies of item 0 and 1 copy of item 1 for a total cost of <code>2 * 6 + 4 = 16</code>, which is not greater than <code>budget = 19</code>.</li>
	<li>One purchased copy of item 0 gives 1 free copy of item 1, because <code>factor<sub>0</sub> = 1</code> divides <code>factor<sub>1</sub> = 2</code>.</li>
	<li>The other purchased copy of item 0 gives 1 free copy of item 2, because <code>factor<sub>0</sub> = 1</code> divides <code>factor<sub>2</sub> = 3</code>.</li>
	<li>You leave with 3 purchased copies and 2 free copies, for a total of 5 item copies.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">items = [[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]], budget = 35</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>You can buy 2 copies of item 0, 1 copy of item 1, and 1 copy of item 2 for a total cost of <code>2 * 8 + 10 + 6 = 32</code>, which is not greater than <code>budget = 35</code>.</li>
	<li>One purchased copy of item 0 gives 1 free copy of item 2, because <code>factor<sub>0</sub> = 2</code> divides <code>factor<sub>2</sub> = 6</code>.</li>
	<li>The other purchased copy of item 0 gives 1 free copy of item 3, because <code>factor<sub>0</sub> = 2</code> divides <code>factor<sub>3</sub> = 4</code>.</li>
	<li>The purchased copy of item 1 gives 1 free copy of item 2, because <code>factor<sub>1</sub> = 1</code> divides <code>factor<sub>2</sub> = 6</code>.</li>
	<li>Buying item 2 gives no free copy, because <code>factor<sub>2</sub> = 6</code> does not divide the factor of any other item.</li>
	<li>You leave with 4 purchased copies and 3 free copies, for a total of 7 item copies.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= items.length &lt;= 10<sup>5</sup></code></li>
	<li><code>items[i] = [factor<sub>i</sub>, price<sub>i</sub>]</code></li>
	<li><code>1 &lt;= factor<sub>i</sub> &lt;= items.length</code></li>
	<li><code>1 &lt;= price<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= budget &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. For each item `i`, compute `gain[i]` = number of other items `j` such that `factor[i]` divides `factor[j]`. This can be done by counting factors and iterating over multiples.

2. If you buy `c` copies of item `i`, it contributes
`c + min(c, gain[i])` total copies, because only the first `gain[i]` purchased copies can be matched to distinct free items.

3. View purchases as marginal units: for item `i`, the first `gain[i]` copies have value `2` each, and all later copies have value `1` each.

4. Since extra value-1 copies should always be bought from the cheapest item, the main task is to choose the cheapest useful value-2 marginal units. Sort item types by price and process their `gain[i]` boosted copies in batches rather than expanding them one by one.

## ✨ AI-Generated Solution (gemini-3.8-flash)

### Approach

Each purchased copy of an item type $i$ provides one copy directly and can yield at most one free copy of another item type $j$ where $factor_i$ divides $factor_j$ and $i \ne j$. Since each distinct valid $j$ can be claimed at most once by item type $i$, purchasing $c$ copies of item $i$ yields $c + \min(c, gain[i])$ total items, where $gain[i]$ is the count of other items whose factors are multiples of $factor_i$. Because different item types can claim the same item $j$ independently, the first $gain[i]$ copies of item $i$ effectively grant 2 item copies each at the cost of $price_i$, while all subsequent copies grant 1 item copy each at $price_i$. Any value-1 copies should always be purchased from the globally cheapest item with minimum price $min\_p$.

Furthermore, purchasing a value-2 unit at cost $P$ is always preferable to (or equal to) buying value-1 items as long as $P < 2 \times min\_p$. This is because replacing value-1 items with a value-2 item never decreases the total item count. Consequently, we can compute $gain[i]$ for all items using a sieve-like divisor counting in $O(n \log n)$ time, collect all item types with $gain[i] > 0$ and $price_i < 2 \times min\_p$, sort them in ascending order of price, and greedily purchase their value-2 units in batches. Finally, any leftover budget is spent on value-1 units of the cheapest item.

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
        int n = items.size();
        vector<int> cnt(n + 1, 0);
        long long min_p = items[0][1];
        for (const auto& it : items) {
            cnt[it[0]]++;
            if (it[1] < min_p) {
                min_p = it[1];
            }
        }

        vector<int> mult(n + 1, 0);
        for (int f = 1; f <= n; ++f) {
            for (int k = f; k <= n; k += f) {
                mult[f] += cnt[k];
            }
        }

        vector<pair<long long, int>> candidates;
        for (int i = 0; i < n; ++i) {
            int gain = mult[items[i][0]] - 1;
            long long price = items[i][1];
            if (gain > 0 && price < 2 * min_p) {
                candidates.push_back({price, gain});
            }
        }

        sort(candidates.begin(), candidates.end());

        long long b = budget;
        long long ans = 0;
        for (const auto& cand : candidates) {
            long long price = cand.first;
            long long count = cand.second;
            long long take = min(count, b / price);
            ans += take * 2;
            b -= take * price;
            if (take < count) {
                break;
            }
        }

        ans += b / min_p;
        return (int)ans;
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
        int n = items.length;
        int[] cnt = new int[n + 1];
        long minP = items[0][1];
        for (int[] it : items) {
            cnt[it[0]]++;
            if (it[1] < minP) {
                minP = it[1];
            }
        }

        int[] mult = new int[n + 1];
        for (int f = 1; f <= n; ++f) {
            for (int k = f; k <= n; k += f) {
                mult[f] += cnt[k];
            }
        }

        long[][] candidates = new long[n][2];
        int candSize = 0;
        for (int i = 0; i < n; ++i) {
            int gain = mult[items[i][0]] - 1;
            long price = items[i][1];
            if (gain > 0 && price < 2 * minP) {
                candidates[candSize][0] = price;
                candidates[candSize][1] = gain;
                candSize++;
            }
        }

        java.util.Arrays.sort(candidates, 0, candSize, (a, b) -> Long.compare(a[0], b[0]));

        long b = budget;
        long ans = 0;
        for (int i = 0; i < candSize; ++i) {
            long price = candidates[i][0];
            long count = candidates[i][1];
            long take = Math.min(count, b / price);
            ans += take * 2;
            b -= take * price;
            if (take < count) {
                break;
            }
        }

        ans += b / minP;
        return (int) ans;
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
        n = len(items)
        cnt = [0] * (n + 1)
        min_p = items[0][1]
        for f, p in items:
            cnt[f] += 1
            if p < min_p:
                min_p = p

        mult = [0] * (n + 1)
        for f in range(1, n + 1):
            for k in range(f, n + 1, f):
                mult[f] += cnt[k]

        threshold = 2 * min_p
        candidates = []
        for f, p in items:
            gain = mult[f] - 1
            if gain > 0 and p < threshold:
                candidates.append((p, gain))

        candidates.sort(key=lambda x: x[0])

        b = budget
        ans = 0
        for price, count in candidates:
            take = min(count, b // price)
            ans += take * 2
            b -= take * price
            if take < count:
                break

        ans += b // min_p
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cnt = [0] * (n + 1)
        min_p = items[0][1]
        for f, p in items:
            cnt[f] += 1
            if p < min_p:
                min_p = p

        mult = [0] * (n + 1)
        for f in range(1, n + 1):
            for k in range(f, n + 1, f):
                mult[f] += cnt[k]

        threshold = 2 * min_p
        candidates = []
        for f, p in items:
            gain = mult[f] - 1
            if gain > 0 and p < threshold:
                candidates.append((p, gain))

        candidates.sort(key=lambda x: x[0])

        b = budget
        ans = 0
        for price, count in candidates:
            take = min(count, b // price)
            ans += take * 2
            b -= take * price
            if take < count:
                break

        ans += b // min_p
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    long long price;
    int count;
} Candidate;

int compareCandidates(const void* a, const void* b) {
    long long pa = ((const Candidate*)a)->price;
    long long pb = ((const Candidate*)b)->price;
    if (pa < pb) return -1;
    if (pa > pb) return 1;
    return 0;
}

int maximumSaleItems(int** items, int itemsSize, int* itemsColSize, int budget) {
    int n = itemsSize;
    int* cnt = (int*)calloc(n + 1, sizeof(int));
    long long min_p = items[0][1];
    for (int i = 0; i < n; ++i) {
        cnt[items[i][0]]++;
        if (items[i][1] < min_p) {
            min_p = items[i][1];
        }
    }

    int* mult = (int*)calloc(n + 1, sizeof(int));
    for (int f = 1; f <= n; ++f) {
        for (int k = f; k <= n; k += f) {
            mult[f] += cnt[k];
        }
    }

    Candidate* candidates = (Candidate*)malloc(n * sizeof(Candidate));
    int candSize = 0;
    for (int i = 0; i < n; ++i) {
        int gain = mult[items[i][0]] - 1;
        long long price = items[i][1];
        if (gain > 0 && price < 2 * min_p) {
            candidates[candSize].price = price;
            candidates[candSize].count = gain;
            candSize++;
        }
    }

    qsort(candidates, candSize, sizeof(Candidate), compareCandidates);

    long long b = budget;
    long long ans = 0;
    for (int i = 0; i < candSize; ++i) {
        long long price = candidates[i].price;
        long long count = candidates[i].count;
        long long take = count < (b / price) ? count : (b / price);
        ans += take * 2;
        b -= take * price;
        if (take < count) {
            break;
        }
    }

    ans += b / min_p;

    free(cnt);
    free(mult);
    free(candidates);

    return (int)ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximumSaleItems(int[][] items, int budget) {
        int n = items.Length;
        int[] cnt = new int[n + 1];
        long minP = items[0][1];
        foreach (var item in items) {
            cnt[item[0]]++;
            if (item[1] < minP) {
                minP = item[1];
            }
        }

        int[] mult = new int[n + 1];
        for (int f = 1; f <= n; f++) {
            for (int k = f; k <= n; k += f) {
                mult[f] += cnt[k];
            }
        }

        long threshold = 2 * minP;
        List<(long price, long count)> candidates = new List<(long, long)>();
        foreach (var item in items) {
            int gain = mult[item[0]] - 1;
            if (gain > 0 && item[1] < threshold) {
                candidates.Add((item[1], gain));
            }
        }

        candidates.Sort((a, b) => a.price.CompareTo(b.price));

        long b = budget;
        long ans = 0;
        foreach (var (price, count) in candidates) {
            long take = count < b / price ? count : b / price;
            ans += take * 2;
            b -= take * price;
            if (take < count) {
                break;
            }
        }

        ans += b / minP;
        return (int)ans;
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
    const n = items.length;
    const cnt = new Int32Array(n + 1);
    let minP = items[0][1];
    for (let i = 0; i < n; i++) {
        cnt[items[i][0]]++;
        if (items[i][1] < minP) {
            minP = items[i][1];
        }
    }

    const mult = new Int32Array(n + 1);
    for (let f = 1; f <= n; f++) {
        for (let k = f; k <= n; k += f) {
            mult[f] += cnt[k];
        }
    }

    const threshold = 2 * minP;
    const candidates = [];
    for (let i = 0; i < n; i++) {
        const gain = mult[items[i][0]] - 1;
        if (gain > 0 && items[i][1] < threshold) {
            candidates.push([items[i][1], gain]);
        }
    }

    candidates.sort((a, b) => a[0] - b[0]);

    let b = budget;
    let ans = 0;
    for (let i = 0; i < candidates.length; i++) {
        const price = candidates[i][0];
        const count = candidates[i][1];
        const take = Math.min(count, Math.floor(b / price));
        ans += take * 2;
        b -= take * price;
        if (take < count) {
            break;
        }
    }

    ans += Math.floor(b / minP);
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximumSaleItems(items: number[][], budget: number): number {
    const n = items.length;
    const cnt = new Int32Array(n + 1);
    let minP = items[0][1];
    for (let i = 0; i < n; i++) {
        cnt[items[i][0]]++;
        if (items[i][1] < minP) {
            minP = items[i][1];
        }
    }

    const mult = new Int32Array(n + 1);
    for (let f = 1; f <= n; f++) {
        for (let k = f; k <= n; k += f) {
            mult[f] += cnt[k];
        }
    }

    const threshold = 2 * minP;
    const candidates: [number, number][] = [];
    for (let i = 0; i < n; i++) {
        const gain = mult[items[i][0]] - 1;
        if (gain > 0 && items[i][1] < threshold) {
            candidates.push([items[i][1], gain]);
        }
    }

    candidates.sort((a, b) => a[0] - b[0]);

    let b = budget;
    let ans = 0;
    for (let i = 0; i < candidates.length; i++) {
        const price = candidates[i][0];
        const count = candidates[i][1];
        const take = Math.min(count, Math.floor(b / price));
        ans += take * 2;
        b -= take * price;
        if (take < count) {
            break;
        }
    }

    ans += Math.floor(b / minP);
    return ans;
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
        $n = count($items);
        $cnt = array_fill(0, $n + 1, 0);
        $minP = $items[0][1];
        foreach ($items as $item) {
            $cnt[$item[0]]++;
            if ($item[1] < $minP) {
                $minP = $item[1];
            }
        }

        $mult = array_fill(0, $n + 1, 0);
        for ($f = 1; $f <= $n; $f++) {
            for ($k = $f; $k <= $n; $k += $f) {
                $mult[$f] += $cnt[$k];
            }
        }

        $threshold = 2 * $minP;
        $candidates = [];
        foreach ($items as $item) {
            $gain = $mult[$item[0]] - 1;
            if ($gain > 0 && $item[1] < $threshold) {
                $candidates[] = [$item[1], $gain];
            }
        }

        usort($candidates, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        $b = $budget;
        $ans = 0;
        foreach ($candidates as $cand) {
            $price = $cand[0];
            $count = $cand[1];
            $take = min($count, intdiv($b, $price));
            $ans += $take * 2;
            $b -= $take * $price;
            if ($take < $count) {
                break;
            }
        }

        $ans += intdiv($b, $minP);
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
    func maximumSaleItems(_ items: [[Int]], _ budget: Int) -> Int {
        let n = items.count
        var cnt = [Int](repeating: 0, count: n + 1)
        var minP = items[0][1]
        for item in items {
            cnt[item[0]] += 1
            if item[1] < minP {
                minP = item[1]
            }
        }

        var mult = [Int](repeating: 0, count: n + 1)
        for f in 1...n {
            var k = f
            while k <= n {
                mult[f] += cnt[k]
                k += f
            }
        }

        let threshold = 2 * minP
        var candidates = [(price: Int, count: Int)]()
        for item in items {
            let gain = mult[item[0]] - 1
            if gain > 0 && item[1] < threshold {
                candidates.append((item[1], gain))
            }
        }

        candidates.sort { $0.price < $1.price }

        var b = budget
        var ans = 0
        for cand in candidates {
            let take = min(cand.count, b / cand.price)
            ans += take * 2
            b -= take * cand.price
            if take < cand.count {
                break
            }
        }

        ans += b / minP
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
    fun maximumSaleItems(items: Array<IntArray>, budget: Int): Int {
        val n = items.size
        val cnt = IntArray(n + 1)
        var minP = items[0][1].toLong()
        for (item in items) {
            cnt[item[0]]++
            if (item[1].toLong() < minP) {
                minP = item[1].toLong()
            }
        }

        val mult = IntArray(n + 1)
        for (f in 1..n) {
            var k = f
            while (k <= n) {
                mult[f] += cnt[k]
                k += f
            }
        }

        val threshold = 2L * minP
        val candidates = ArrayList<LongArray>()
        for (item in items) {
            val f = item[0]
            val p = item[1].toLong()
            val gain = (mult[f] - 1).toLong()
            if (gain > 0 && p < threshold) {
                candidates.add(longArrayOf(p, gain))
            }
        }

        candidates.sortWith(compareBy { it[0] })

        var b = budget.toLong()
        var ans = 0L
        for (cand in candidates) {
            val price = cand[0]
            val count = cand[1]
            val take = minOf(count, b / price)
            ans += take * 2L
            b -= take * price
            if (take < count) {
                break
            }
        }

        ans += b / minP
        return ans.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maximumSaleItems(List<List<int>> items, int budget) {
    final n = items.length;
    final cnt = List<int>.filled(n + 1, 0);
    int minP = items[0][1];
    for (final item in items) {
      cnt[item[0]]++;
      if (item[1] < minP) {
        minP = item[1];
      }
    }

    final mult = List<int>.filled(n + 1, 0);
    for (int f = 1; f <= n; f++) {
      for (int k = f; k <= n; k += f) {
        mult[f] += cnt[k];
      }
    }

    final threshold = 2 * minP;
    final candidates = <List<int>>[];
    for (final item in items) {
      final f = item[0];
      final p = item[1];
      final gain = mult[f] - 1;
      if (gain > 0 && p < threshold) {
        candidates.add([p, gain]);
      }
    }

    candidates.sort((a, b) => a[0].compareTo(b[0]));

    int b = budget;
    int ans = 0;
    for (final cand in candidates) {
      final price = cand[0];
      final count = cand[1];
      final take = (b ~/ price < count) ? b ~/ price : count;
      ans += take * 2;
      b -= take * price;
      if (take < count) {
        break;
      }
    }

    ans += b ~/ minP;
    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import "sort"

func maximumSaleItems(items [][]int, budget int) int {
    n := len(items)
    cnt := make([]int, n+1)
    minP := int64(items[0][1])
    for _, item := range items {
        cnt[item[0]]++
        if int64(item[1]) < minP {
            minP = int64(item[1])
        }
    }

    mult := make([]int, n+1)
    for f := 1; f <= n; f++ {
        for k := f; k <= n; k += f {
            mult[f] += cnt[k]
        }
    }

    threshold := 2 * minP
    type cand struct {
        price int64
        count int64
    }
    var candidates []cand
    for _, item := range items {
        f := item[0]
        p := int64(item[1])
        gain := int64(mult[f] - 1)
        if gain > 0 && p < threshold {
            candidates = append(candidates, cand{price: p, count: gain})
        }
    }

    sort.Slice(candidates, func(i, j int) bool {
        return candidates[i].price < candidates[j].price
    })

    b := int64(budget)
    var ans int64 = 0
    for _, c := range candidates {
        take := b / c.price
        if c.count < take {
            take = c.count
        }
        ans += take * 2
        b -= take * c.price
        if take < c.count {
            break
        }
    }

    ans += b / minP
    return int(ans)
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
    n = items.length
    cnt = Array.new(n + 1, 0)
    min_p = items[0][1]
    items.each do |f, p|
        cnt[f] += 1
        min_p = p if p < min_p
    end

    mult = Array.new(n + 1, 0)
    (1..n).each do |f|
        k = f
        while k <= n
            mult[f] += cnt[k]
            k += f
        end
    end

    threshold = 2 * min_p
    candidates = []
    items.each do |f, p|
        gain = mult[f] - 1
        if gain > 0 && p < threshold
            candidates << [p, gain]
        end
    end

    candidates.sort_by! { |x| x[0] }

    b = budget
    ans = 0
    candidates.each do |price, count|
        take = [count, b / price].min
        ans += take * 2
        b -= take * price
        break if take < count
    end

    ans += b / min_p
    ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximumSaleItems(items: Array[Array[Int]], budget: Int): Int = {
        val n = items.length
        val cnt = new Array[Int](n + 1)
        var minP = items(0)(1).toLong
        for (item <- items) {
            cnt(item(0)) += 1
            if (item(1).toLong < minP) {
                minP = item(1).toLong
            }
        }

        val mult = new Array[Int](n + 1)
        for (f <- 1 to n) {
            var k = f
            while (k <= n) {
                mult(f) += cnt(k)
                k += f
            }
        }

        val threshold = 2L * minP
        val candidates = scala.collection.mutable.ArrayBuffer[(Long, Long)]()
        for (item <- items) {
            val f = item(0)
            val p = item(1).toLong
            val gain = (mult(f) - 1).toLong
            if (gain > 0 && p < threshold) {
                candidates += ((p, gain))
            }
        }

        val sortedCandidates = candidates.sortBy(_._1)

        var b = budget.toLong
        var ans = 0L
        var i = 0
        var stop = false
        while (i < sortedCandidates.length && !stop) {
            val (price, count) = sortedCandidates(i)
            val take = math.min(count, b / price)
            ans += take * 2L
            b -= take * price
            if (take < count) {
                stop = true
            }
            i += 1
        }

        ans += b / minP
        ans.toInt
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
        let n = items.len();
        let mut cnt = vec![0i32; n + 1];
        let mut min_p = items[0][1] as i64;
        for item in &items {
            let f = item[0] as usize;
            let p = item[1] as i64;
            cnt[f] += 1;
            if p < min_p {
                min_p = p;
            }
        }

        let mut mult = vec![0i32; n + 1];
        for f in 1..=n {
            let mut k = f;
            while k <= n {
                mult[f] += cnt[k];
                k += f;
            }
        }

        let threshold = 2 * min_p;
        let mut candidates = Vec::new();
        for item in &items {
            let f = item[0] as usize;
            let p = item[1] as i64;
            let gain = mult[f] - 1;
            if gain > 0 && p < threshold {
                candidates.push((p, gain as i64));
            }
        }

        candidates.sort_unstable_by_key(|&(p, _)| p);

        let mut b = budget as i64;
        let mut ans = 0i64;
        for (price, count) in candidates {
            let take = count.min(b / price);
            ans += take * 2;
            b -= take * price;
            if take < count {
                break;
            }
        }

        ans += b / min_p;
        ans as i32
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
  (let* ([n (length items)]
         [cnt (make-vector (+ n 1) 0)]
         [min-p (second (first items))])
    (for ([item (in-list items)])
      (let ([f (first item)]
            [p (second item)])
        (vector-set! cnt f (+ (vector-ref cnt f) 1))
        (when (< p min-p)
          (set! min-p p))))
    (let ([mult (make-vector (+ n 1) 0)])
      (for ([f (in-range 1 (+ n 1))])
        (let ([sum 0])
          (for ([k (in-range f (+ n 1) f)])
            (set! sum (+ sum (vector-ref cnt k))))
          (vector-set! mult f sum)))
      (let* ([threshold (* 2 min-p)]
             [candidates '()])
        (for ([item (in-list items)])
          (let* ([f (first item)]
                 [p (second item)]
                 [gain (- (vector-ref mult f) 1)])
            (when (and (> gain 0) (< p threshold))
              (set! candidates (cons (cons p gain) candidates)))))
        (let ([sorted-cand (sort candidates < #:key car)])
          (let loop ([cand sorted-cand] [b budget] [ans 0])
            (cond
              [(null? cand) (+ ans (quotient b min-p))]
              [else
               (let* ([cg (car cand)]
                      [price (car cg)]
                      [count (cdr cg)]
                      [take (min count (quotient b price))]
                      [new-ans (+ ans (* take 2))]
                      [new-b (- b (* take price))])
                 (if (< take count)
                     (+ new-ans (quotient new-b min-p))
                     (loop (cdr cand) new-b new-ans)))])))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_sale_items(Items :: [[integer()]], Budget :: integer()) -> integer().
maximum_sale_items(Items, Budget) ->
    N = length(Items),
    {Cnt, MinP} = lists:foldl(fun([F, P], {AccCnt, AccMin}) ->
        NewCnt = maps:update_with(F, fun(V) -> V + 1 end, 1, AccCnt),
        NewMin = case AccMin of
            undefined -> P;
            _ -> min(AccMin, P)
        end,
        {NewCnt, NewMin}
    end, {#{}, undefined}, Items),

    DistinctF = maps:keys(Cnt),
    Mult = lists:foldl(fun(F, Acc) ->
        Sum = sum_multiples(F, F, N, Cnt, 0),
        maps:put(F, Sum, Acc)
    end, #{}, DistinctF),

    Threshold = 2 * MinP,
    Candidates = lists:foldl(fun([F, P], Acc) ->
        Gain = maps:get(F, Mult) - 1,
        case Gain > 0 andalso P < Threshold of
            true -> [{P, Gain} | Acc];
            false -> Acc
        end
    end, [], Items),

    Sorted = lists:sort(fun({P1, _}, {P2, _}) -> P1 =< P2 end, Candidates),

    {RemB, Ans} = take_items(Sorted, Budget, 0),
    Ans + (RemB div MinP).

sum_multiples(K, _Step, Max, _Cnt, Acc) when K > Max ->
    Acc;
sum_multiples(K, Step, Max, Cnt, Acc) ->
    Val = maps:get(K, Cnt, 0),
    sum_multiples(K + Step, Step, Max, Cnt, Acc + Val).

take_items([], B, Ans) ->
    {B, Ans};
take_items([{Price, Count} | Rest], B, Ans) ->
    Take = min(Count, B div Price),
    NewAns = Ans + Take * 2,
    NewB = B - Take * Price,
    case Take < Count of
        true -> {NewB, NewAns};
        false -> take_items(Rest, NewB, NewAns)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_sale_items(items :: [[integer]], budget :: integer) :: integer
  def maximum_sale_items(items, budget) do
    n = length(items)

    {cnt, min_p} = 
      Enum.reduce(items, {%{}, nil}, fn [f, p], {acc_cnt, acc_min} ->
        new_cnt = Map.update(acc_cnt, f, 1, &(&1 + 1))
        new_min = if is_nil(acc_min) or p < acc_min, do: p, else: acc_min
        {new_cnt, new_min}
      end)

    mult =
      Enum.reduce(Map.keys(cnt), %{}, fn f, acc ->
        sum = sum_multiples(f, f, n, cnt, 0)
        Map.put(acc, f, sum)
      end)

    threshold = 2 * min_p

    candidates =
      Enum.reduce(items, [], fn [f, p], acc ->
        gain = Map.get(mult, f, 0) - 1
        if gain > 0 and p < threshold do
          [{p, gain} | acc]
        else
          acc
        end
      end)
      |> Enum.sort_by(fn {p, _gain} -> p end)

    {rem_b, ans} =
      Enum.reduce_while(candidates, {budget, 0}, fn {price, count}, {b, total} ->
        take = min(count, div(b, price))
        new_total = total + take * 2
        new_b = b - take * price
        if take < count do
          {:halt, {new_b, new_total}}
        else
          {:cont, {new_b, new_total}}
        end
      end)

    ans + div(rem_b, min_p)
  end

  defp sum_multiples(k, step, max, cnt, acc) do
    if k > max do
      acc
    else
      val = Map.get(cnt, k, 0)
      sum_multiples(k + step, step, max, cnt, acc + val)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n \log n) where n is the number of items. Computing the count of multiples for each factor takes O(n \log n) via harmonic series iteration, and sorting the filtered candidate items by price takes O(n \log n). The greedy batch processing takes O(n) time.
- **Space Complexity:** O(n) auxiliary space to store factor frequency counts, precomputed multiple counts, and the list of value-2 candidate items.
