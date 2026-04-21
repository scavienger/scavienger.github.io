---
layout: post
title: "Minimize Hamming Distance After Swap Operations"
date: 2026-04-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Depth-First Search", "Union-Find"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int find(vector<int>& parent, int i) {\n\
        \        int root = i;\n        while (parent[root] != root) root = parent[root];\n\
        \        while (parent[i] != root) {\n            int next = parent[i];\n  \
        \          parent[i] = root;\n            i = next;\n        }\n        return\
        \ root;\n    }\n\n    int minimumHammingDistance(vector<int>& source, vector<int>&\
        \ target, vector<vector<int>>& allowedSwaps) {\n        int n = source.size();\n\
        \        vector<int> parent(n);\n        for (int i = 0; i < n; i++) parent[i]\
        \ = i;\n\n        for (const auto& sw : allowedSwaps) {\n            int r1\
        \ = find(parent, sw[0]);\n            int r2 = find(parent, sw[1]);\n      \
        \      if (r1 != r2) parent[r1] = r2;\n        }\n\n        unordered_map<int,\
        \ vector<int>> components;\n        for (int i = 0; i < n; i++) {\n        \
        \    components[find(parent, i)].push_back(i);\n        }\n\n        int matches\
        \ = 0;\n        for (auto const& [root, indices] : components) {\n         \
        \   unordered_map<int, int> counts;\n            for (int idx : indices) counts[source[idx]]++;\n\
        \            for (int idx : indices) {\n                if (counts[target[idx]]\
        \ > 0) {\n                    counts[target[idx]]--;\n                    matches++;\n\
        \                }\n            }\n        }\n        return n - matches;\n\
        \    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    private int find(int[] parent,\
        \ int i) {\n        int root = i;\n        while (parent[root] != root) {\n\
        \            root = parent[root];\n        }\n        while (parent[i] != root)\
        \ {\n            int next = parent[i];\n            parent[i] = root;\n    \
        \        i = next;\n        }\n        return root;\n    }\n\n    public int\
        \ minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {\n\
        \        int n = source.length;\n        int[] parent = new int[n];\n      \
        \  for (int i = 0; i < n; i++) parent[i] = i;\n\n        for (int[] sw : allowedSwaps)\
        \ {\n            int r1 = find(parent, sw[0]);\n            int r2 = find(parent,\
        \ sw[1]);\n            if (r1 != r2) parent[r1] = r2;\n        }\n\n       \
        \ Map<Integer, List<Integer>> components = new HashMap<>();\n        for (int\
        \ i = 0; i < n; i++) {\n            int root = find(parent, i);\n          \
        \  components.computeIfAbsent(root, k -> new ArrayList<>()).add(i);\n      \
        \  }\n\n        int matches = 0;\n        for (List<Integer> indices : components.values())\
        \ {\n            Map<Integer, Integer> counts = new HashMap<>();\n         \
        \   for (int idx : indices) {\n                counts.put(source[idx], counts.getOrDefault(source[idx],\
        \ 0) + 1);\n            }\n            for (int idx : indices) {\n         \
        \       int val = target[idx];\n                if (counts.getOrDefault(val,\
        \ 0) > 0) {\n                    counts.put(val, counts.get(val) - 1);\n   \
        \                 matches++;\n                }\n            }\n        }\n\n\
        \        return n - matches;\n    }\n}"
      python: "import collections\n\nclass Solution(object):\n    def minimumHammingDistance(self,\
        \ source, target, allowedSwaps):\n        \"\"\"\n        :type source: List[int]\n\
        \        :type target: List[int]\n        :type allowedSwaps: List[List[int]]\n\
        \        :rtype: int\n        \"\"\"\n        n = len(source)\n        parent\
        \ = list(range(n))\n\n        def find(i):\n            root = i\n         \
        \   while parent[root] != root:\n                root = parent[root]\n     \
        \       while parent[i] != root:\n                nxt = parent[i]\n        \
        \        parent[i] = root\n                i = nxt\n            return root\n\
        \n        for a, b in allowedSwaps:\n            r1, r2 = find(a), find(b)\n\
        \            if r1 != r2:\n                parent[r1] = r2\n\n        components\
        \ = collections.defaultdict(list)\n        for i in range(n):\n            components[find(i)].append(i)\n\
        \n        matches = 0\n        for indices in components.values():\n       \
        \     counts = collections.defaultdict(int)\n            for i in indices:\n\
        \                counts[source[i]] += 1\n            for i in indices:\n   \
        \             if counts[target[i]] > 0:\n                    counts[target[i]]\
        \ -= 1\n                    matches += 1\n\n        return n - matches"
      python3: "import collections\nfrom typing import List\n\nclass Solution:\n   \
        \ def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps:\
        \ List[List[int]]) -> int:\n        n = len(source)\n        parent = list(range(n))\n\
        \n        def find(i):\n            root = i\n            while parent[root]\
        \ != root:\n                root = parent[root]\n            while parent[i]\
        \ != root:\n                nxt = parent[i]\n                parent[i] = root\n\
        \                i = nxt\n            return root\n\n        for a, b in allowedSwaps:\n\
        \            r1, r2 = find(a), find(b)\n            if r1 != r2:\n         \
        \       parent[r1] = r2\n\n        components = collections.defaultdict(list)\n\
        \        for i in range(n):\n            components[find(i)].append(i)\n\n \
        \       matches = 0\n        for indices in components.values():\n         \
        \   counts = collections.Counter()\n            for i in indices:\n        \
        \        counts[source[i]] += 1\n            for i in indices:\n           \
        \     if counts[target[i]] > 0:\n                    counts[target[i]] -= 1\n\
        \                    matches += 1\n\n        return n - matches"
      c: "#include <stdlib.h>\n#include <string.h>\n\nint find(int* parent, int i) {\n\
        \    int root = i;\n    while (parent[root] != root) root = parent[root];\n\
        \    while (parent[i] != root) {\n        int next = parent[i];\n        parent[i]\
        \ = root;\n        i = next;\n    }\n    return root;\n}\n\nint compare(const\
        \ void* a, const void* b) {\n    int arg1 = *(const int*)a;\n    int arg2 =\
        \ *(const int*)b;\n    if (arg1 < arg2) return -1;\n    if (arg1 > arg2) return\
        \ 1;\n    return 0;\n}\n\nint minimumHammingDistance(int* source, int sourceSize,\
        \ int* target, int targetSize, int** allowedSwaps, int allowedSwapsSize, int*\
        \ allowedSwapsColSize) {\n    int n = sourceSize;\n    int* parent = (int*)malloc(n\
        \ * sizeof(int));\n    for (int i = 0; i < n; i++) parent[i] = i;\n\n    for\
        \ (int i = 0; i < allowedSwapsSize; i++) {\n        int r1 = find(parent, allowedSwaps[i][0]);\n\
        \        int r2 = find(parent, allowedSwaps[i][1]);\n        if (r1 != r2) parent[r1]\
        \ = r2;\n    }\n\n    int* heads = (int*)malloc(n * sizeof(int));\n    int*\
        \ nexts = (int*)malloc(n * sizeof(int));\n    for (int i = 0; i < n; i++) heads[i]\
        \ = -1;\n    for (int i = 0; i < n; i++) {\n        int root = find(parent,\
        \ i);\n        nexts[i] = heads[root];\n        heads[root] = i;\n    }\n\n\
        \    int* s_buf = (int*)malloc(n * sizeof(int));\n    int* t_buf = (int*)malloc(n\
        \ * sizeof(int));\n    int total_matches = 0;\n\n    for (int i = 0; i < n;\
        \ i++) {\n        if (heads[i] == -1) continue;\n        int count = 0;\n  \
        \      for (int curr = heads[i]; curr != -1; curr = nexts[curr]) {\n       \
        \     s_buf[count] = source[curr];\n            t_buf[count] = target[curr];\n\
        \            count++;\n        }\n\n        qsort(s_buf, count, sizeof(int),\
        \ compare);\n        qsort(t_buf, count, sizeof(int), compare);\n\n        int\
        \ p1 = 0, p2 = 0;\n        while (p1 < count && p2 < count) {\n            if\
        \ (s_buf[p1] == t_buf[p2]) {\n                total_matches++;\n           \
        \     p1++;\n                p2++;\n            } else if (s_buf[p1] < t_buf[p2])\
        \ {\n                p1++;\n            } else {\n                p2++;\n  \
        \          }\n        }\n    }\n\n    free(parent);\n    free(heads);\n    free(nexts);\n\
        \    free(s_buf);\n    free(t_buf);\n\n    return n - total_matches;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int MinimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps)\
        \ {\n        int n = source.Length;\n        int[] parent = new int[n];\n  \
        \      int[] rank = new int[n];\n        for (int i = 0; i < n; i++) parent[i]\
        \ = i;\n\n        int Find(int i) {\n            int root = i;\n           \
        \ while (parent[root] != root) root = parent[root];\n            int curr =\
        \ i;\n            while (parent[curr] != root) {\n                int next =\
        \ parent[curr];\n                parent[curr] = root;\n                curr\
        \ = next;\n            }\n            return root;\n        }\n\n        void\
        \ Union(int i, int j) {\n            int rootI = Find(i);\n            int rootJ\
        \ = Find(j);\n            if (rootI != rootJ) {\n                if (rank[rootI]\
        \ < rank[rootJ]) parent[rootI] = rootJ;\n                else if (rank[rootI]\
        \ > rank[rootJ]) parent[rootJ] = rootI;\n                else {\n          \
        \          parent[rootI] = rootJ;\n                    rank[rootJ]++;\n    \
        \            }\n            }\n        }\n\n        foreach (var swap in allowedSwaps)\
        \ {\n            Union(swap[0], swap[1]);\n        }\n\n        var groups =\
        \ new Dictionary<int, List<int>>();\n        for (int i = 0; i < n; i++) {\n\
        \            int r = Find(i);\n            if (!groups.ContainsKey(r)) {\n \
        \               groups[r] = new List<int>();\n            }\n            groups[r].Add(i);\n\
        \        }\n\n        int totalMatching = 0;\n        var counts = new Dictionary<int,\
        \ int>();\n        foreach (var indices in groups.Values) {\n            counts.Clear();\n\
        \            foreach (int idx in indices) {\n                int val = source[idx];\n\
        \                if (counts.ContainsKey(val)) counts[val]++;\n             \
        \   else counts[val] = 1;\n            }\n            foreach (int idx in indices)\
        \ {\n                int val = target[idx];\n                if (counts.ContainsKey(val)\
        \ && counts[val] > 0) {\n                    totalMatching++;\n            \
        \        counts[val]--;\n                }\n            }\n        }\n\n   \
        \     return n - totalMatching;\n    }\n}"
      javascript: "/**\n * @param {number[]} source\n * @param {number[]} target\n *\
        \ @param {number[][]} allowedSwaps\n * @return {number}\n */\nvar minimumHammingDistance\
        \ = function(source, target, allowedSwaps) {\n    const n = source.length;\n\
        \    const parent = new Int32Array(n);\n    const rank = new Int32Array(n);\n\
        \    for (let i = 0; i < n; i++) parent[i] = i;\n\n    function find(i) {\n\
        \        let root = i;\n        while (parent[root] !== root) root = parent[root];\n\
        \        let curr = i;\n        while (parent[curr] !== root) {\n          \
        \  let next = parent[curr];\n            parent[curr] = root;\n            curr\
        \ = next;\n        }\n        return root;\n    }\n\n    function union(i, j)\
        \ {\n        const rootI = find(i);\n        const rootJ = find(j);\n      \
        \  if (rootI !== rootJ) {\n            if (rank[rootI] < rank[rootJ]) parent[rootI]\
        \ = rootJ;\n            else if (rank[rootI] > rank[rootJ]) parent[rootJ] =\
        \ rootI;\n            else {\n                parent[rootI] = rootJ;\n     \
        \           rank[rootJ]++;\n            }\n        }\n    }\n\n    for (let\
        \ i = 0; i < allowedSwaps.length; i++) {\n        union(allowedSwaps[i][0],\
        \ allowedSwaps[i][1]);\n    }\n\n    const groups = new Map();\n    for (let\
        \ i = 0; i < n; i++) {\n        const r = find(i);\n        if (!groups.has(r))\
        \ groups.set(r, []);\n        groups.get(r).push(i);\n    }\n\n    let totalMatching\
        \ = 0;\n    for (const indices of groups.values()) {\n        const counts =\
        \ new Map();\n        for (let i = 0; i < indices.length; i++) {\n         \
        \   const idx = indices[i];\n            const val = source[idx];\n        \
        \    counts.set(val, (counts.get(val) || 0) + 1);\n        }\n        for (let\
        \ i = 0; i < indices.length; i++) {\n            const idx = indices[i];\n \
        \           const val = target[idx];\n            const count = counts.get(val);\n\
        \            if (count > 0) {\n                totalMatching++;\n          \
        \      counts.set(val, count - 1);\n            }\n        }\n    }\n\n    return\
        \ n - totalMatching;\n};"
      typescript: "function minimumHammingDistance(source: number[], target: number[],\
        \ allowedSwaps: number[][]): number {\n    const n = source.length;\n    const\
        \ parent = new Int32Array(n);\n    const rank = new Int32Array(n);\n    for\
        \ (let i = 0; i < n; i++) parent[i] = i;\n\n    function find(i: number): number\
        \ {\n        let root = i;\n        while (parent[root] !== root) root = parent[root];\n\
        \        let curr = i;\n        while (parent[curr] !== root) {\n          \
        \  let next = parent[curr];\n            parent[curr] = root;\n            curr\
        \ = next;\n        }\n        return root;\n    }\n\n    function union(i: number,\
        \ j: number): void {\n        const rootI = find(i);\n        const rootJ =\
        \ find(j);\n        if (rootI !== rootJ) {\n            if (rank[rootI] < rank[rootJ])\
        \ parent[rootI] = rootJ;\n            else if (rank[rootI] > rank[rootJ]) parent[rootJ]\
        \ = rootI;\n            else {\n                parent[rootI] = rootJ;\n   \
        \             rank[rootJ]++;\n            }\n        }\n    }\n\n    for (let\
        \ i = 0; i < allowedSwaps.length; i++) {\n        union(allowedSwaps[i][0],\
        \ allowedSwaps[i][1]);\n    }\n\n    const groups = new Map<number, number[]>();\n\
        \    for (let i = 0; i < n; i++) {\n        const r = find(i);\n        if (!groups.has(r))\
        \ groups.set(r, []);\n        groups.get(r)!.push(i);\n    }\n\n    let totalMatching\
        \ = 0;\n    for (const indices of groups.values()) {\n        const counts =\
        \ new Map<number, number>();\n        for (let i = 0; i < indices.length; i++)\
        \ {\n            const idx = indices[i];\n            const val = source[idx];\n\
        \            counts.set(val, (counts.get(val) || 0) + 1);\n        }\n     \
        \   for (let i = 0; i < indices.length; i++) {\n            const idx = indices[i];\n\
        \            const val = target[idx];\n            const count = counts.get(val);\n\
        \            if (count && count > 0) {\n                totalMatching++;\n \
        \               counts.set(val, count - 1);\n            }\n        }\n    }\n\
        \n    return n - totalMatching;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $source\n     * @param\
        \ Integer[] $target\n     * @param Integer[][] $allowedSwaps\n     * @return\
        \ Integer\n     */\n    function minimumHammingDistance($source, $target, $allowedSwaps)\
        \ {\n        $n = count($source);\n        $parent = range(0, $n - 1);\n   \
        \     $rank = array_fill(0, $n, 0);\n\n        $find = function($i) use (&$parent)\
        \ {\n            $root = $i;\n            while ($parent[$root] != $root) {\n\
        \                $root = $parent[$root];\n            }\n            $curr =\
        \ $i;\n            while ($parent[$curr] != $root) {\n                $next\
        \ = $parent[$curr];\n                $parent[$curr] = $root;\n             \
        \   $curr = $next;\n            }\n            return $root;\n        };\n\n\
        \        $union = function($i, $j) use (&$parent, &$rank, $find) {\n       \
        \     $rootI = $find($i);\n            $rootJ = $find($j);\n            if ($rootI\
        \ != $rootJ) {\n                if ($rank[$rootI] < $rank[$rootJ]) {\n     \
        \               $parent[$rootI] = $rootJ;\n                } else if ($rank[$rootI]\
        \ > $rank[$rootJ]) {\n                    $parent[$rootJ] = $rootI;\n      \
        \          } else {\n                    $parent[$rootI] = $rootJ;\n       \
        \             $rank[$rootJ]++;\n                }\n            }\n        };\n\
        \n        foreach ($allowedSwaps as $swap) {\n            $union($swap[0], $swap[1]);\n\
        \        }\n\n        $groups = [];\n        for ($i = 0; $i < $n; $i++) {\n\
        \            $r = $find($i);\n            $groups[$r][] = $i;\n        }\n\n\
        \        $totalMatching = 0;\n        foreach ($groups as $indices) {\n    \
        \        $counts = [];\n            foreach ($indices as $idx) {\n         \
        \       $val = $source[$idx];\n                $counts[$val] = ($counts[$val]\
        \ ?? 0) + 1;\n            }\n            foreach ($indices as $idx) {\n    \
        \            $val = $target[$idx];\n                if (isset($counts[$val])\
        \ && $counts[$val] > 0) {\n                    $totalMatching++;\n         \
        \           $counts[$val]--;\n                }\n            }\n        }\n\n\
        \        return $n - $totalMatching;\n    }\n}"
      swift: "class Solution {\n    func minimumHammingDistance(_ source: [Int], _ target:\
        \ [Int], _ allowedSwaps: [[Int]]) -> Int {\n        let n = source.count\n \
        \       var parent = Array(0..<n)\n        var rank = [Int](repeating: 0, count:\
        \ n)\n\n        func find(_ i: Int) -> Int {\n            var root = i\n   \
        \         while parent[root] != root {\n                root = parent[root]\n\
        \            }\n            var curr = i\n            while parent[curr] !=\
        \ root {\n                let next = parent[curr]\n                parent[curr]\
        \ = root\n                curr = next\n            }\n            return root\n\
        \        }\n\n        func union(_ i: Int, _ j: Int) {\n            let rootI\
        \ = find(i)\n            let rootJ = find(j)\n            if rootI != rootJ\
        \ {\n                if rank[rootI] < rank[rootJ] {\n                    parent[rootI]\
        \ = rootJ\n                } else if rank[rootI] > rank[rootJ] {\n         \
        \           parent[rootJ] = rootI\n                } else {\n              \
        \      parent[rootI] = rootJ\n                    rank[rootJ] += 1\n       \
        \         }\n            }\n        }\n\n        for swap in allowedSwaps {\n\
        \            union(swap[0], swap[1])\n        }\n\n        var groups = [Int:\
        \ [Int]]()\n        for i in 0..<n {\n            let r = find(i)\n        \
        \    groups[r, default: []].append(i)\n        }\n\n        var totalMatching\
        \ = 0\n        for indices in groups.values {\n            var counts = [Int:\
        \ Int]()\n            for idx in indices {\n                let val = source[idx]\n\
        \                counts[val, default: 0] += 1\n            }\n            for\
        \ idx in indices {\n                let val = target[idx]\n                if\
        \ let count = counts[val], count > 0 {\n                    totalMatching +=\
        \ 1\n                    counts[val] = count - 1\n                }\n      \
        \      }\n        }\n\n        return n - totalMatching\n    }\n}"
      kotlin: "class Solution {\n    fun minimumHammingDistance(source: IntArray, target:\
        \ IntArray, allowedSwaps: Array<IntArray>): Int {\n        val n = source.size\n\
        \        val parent = IntArray(n) { it }\n\n        fun find(i: Int): Int {\n\
        \            var root = i\n            while (parent[root] != root) {\n    \
        \            root = parent[root]\n            }\n            var curr = i\n\
        \            while (parent[curr] != root) {\n                val next = parent[curr]\n\
        \                parent[curr] = root\n                curr = next\n        \
        \    }\n            return root\n        }\n\n        fun union(i: Int, j: Int)\
        \ {\n            val rootI = find(i)\n            val rootJ = find(j)\n    \
        \        if (rootI != rootJ) {\n                parent[rootI] = rootJ\n    \
        \        }\n        }\n\n        for (swap in allowedSwaps) {\n            union(swap[0],\
        \ swap[1])\n        }\n\n        val groups = mutableMapOf<Int, MutableList<Int>>()\n\
        \        for (i in 0 until n) {\n            val root = find(i)\n          \
        \  groups.getOrPut(root) { mutableListOf<Int>() }.add(i)\n        }\n\n    \
        \    var matchingCount = 0\n        for (indices in groups.values) {\n     \
        \       val counts = mutableMapOf<Int, Int>()\n            for (idx in indices)\
        \ {\n                val sVal = source[idx]\n                counts[sVal] =\
        \ counts.getOrDefault(sVal, 0) + 1\n            }\n            for (idx in indices)\
        \ {\n                val tVal = target[idx]\n                val c = counts.getOrDefault(tVal,\
        \ 0)\n                if (c > 0) {\n                    matchingCount++\n  \
        \                  counts[tVal] = c - 1\n                }\n            }\n\
        \        }\n\n        return n - matchingCount\n    }\n}"
      dart: "class Solution {\n  int minimumHammingDistance(List<int> source, List<int>\
        \ target, List<List<int>> allowedSwaps) {\n    final n = source.length;\n  \
        \  final parent = List<int>.generate(n, (i) => i);\n\n    int find(int i) {\n\
        \      int root = i;\n      while (parent[root] != root) {\n        root = parent[root];\n\
        \      }\n      int curr = i;\n      while (parent[curr] != root) {\n      \
        \  int next = parent[curr];\n        parent[curr] = root;\n        curr = next;\n\
        \      }\n      return root;\n    }\n\n    void union(int i, int j) {\n    \
        \  final rootI = find(i);\n      final rootJ = find(j);\n      if (rootI !=\
        \ rootJ) {\n        parent[rootI] = rootJ;\n      }\n    }\n\n    for (final\
        \ swap in allowedSwaps) {\n      union(swap[0], swap[1]);\n    }\n\n    final\
        \ groups = <int, List<int>>{};\n    for (int i = 0; i < n; i++) {\n      final\
        \ root = find(i);\n      groups.putIfAbsent(root, () => []).add(i);\n    }\n\
        \n    int matchingCount = 0;\n    for (final indices in groups.values) {\n \
        \     final counts = <int, int>{};\n      for (final idx in indices) {\n   \
        \     counts[source[idx]] = (counts[source[idx]] ?? 0) + 1;\n      }\n     \
        \ for (final idx in indices) {\n        final tVal = target[idx];\n        final\
        \ c = counts[tVal] ?? 0;\n        if (c > 0) {\n          matchingCount++;\n\
        \          counts[tVal] = c - 1;\n        }\n      }\n    }\n\n    return n\
        \ - matchingCount;\n  }\n}"
      go: "func minimumHammingDistance(source []int, target []int, allowedSwaps [][]int)\
        \ int {\n    n := len(source)\n    parent := make([]int, n)\n    for i := range\
        \ parent {\n        parent[i] = i\n    }\n\n    find := func(i int) int {\n\
        \        root := i\n        for parent[root] != root {\n            root = parent[root]\n\
        \        }\n        curr := i\n        for parent[curr] != root {\n        \
        \    next := parent[curr]\n            parent[curr] = root\n            curr\
        \ = next\n        }\n        return root\n    }\n\n    union := func(i, j int)\
        \ {\n        rootI := find(i)\n        rootJ := find(j)\n        if rootI !=\
        \ rootJ {\n            parent[rootI] = rootJ\n        }\n    }\n\n    for _,\
        \ swap := range allowedSwaps {\n        union(swap[0], swap[1])\n    }\n\n \
        \   groups := make(map[int][]int)\n    for i := 0; i < n; i++ {\n        root\
        \ := find(i)\n        groups[root] = append(groups[root], i)\n    }\n\n    matchingCount\
        \ := 0\n    for _, indices := range groups {\n        counts := make(map[int]int)\n\
        \        for _, idx := range indices {\n            counts[source[idx]]++\n\
        \        }\n        for _, idx := range indices {\n            tVal := target[idx]\n\
        \            if counts[tVal] > 0 {\n                matchingCount++\n      \
        \          counts[tVal]--\n            }\n        }\n    }\n\n    return n -\
        \ matchingCount\n}"
      ruby: "def minimum_hamming_distance(source, target, allowed_swaps)\n  n = source.length\n\
        \  parent = (0...n).to_a\n\n  find = lambda do |i|\n    root = i\n    root =\
        \ parent[root] while parent[root] != root\n    curr = i\n    while parent[curr]\
        \ != root\n      nxt = parent[curr]\n      parent[curr] = root\n      curr =\
        \ nxt\n    end\n    root\n  end\n\n  allowed_swaps.each do |a, b|\n    root_a\
        \ = find.call(a)\n    root_b = find.call(b)\n    parent[root_a] = root_b if\
        \ root_a != root_b\n  end\n\n  groups = Hash.new { |h, k| h[k] = [] }\n  (0...n).each\
        \ do |i|\n    groups[find.call(i)] << i\n  end\n\n  matching_count = 0\n  groups.each_value\
        \ do |indices|\n    counts = Hash.new(0)\n    indices.each { |idx| counts[source[idx]]\
        \ += 1 }\n    indices.each do |idx|\n      t_val = target[idx]\n      if counts[t_val]\
        \ > 0\n        matching_count += 1\n        counts[t_val] -= 1\n      \tend\n\
        \    end\n  end\n\n  n - matching_count\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def minimumHammingDistance(source:\
        \ Array[Int], target: Array[Int], allowedSwaps: Array[Array[Int]]): Int = {\n\
        \        val n = source.length\n        val parent = (0 until n).toArray\n\n\
        \        def find(i: Int): Int = {\n            var root = i\n            while\
        \ (parent(root) != root) {\n                root = parent(root)\n          \
        \  }\n            var curr = i\n            while (parent(curr) != root) {\n\
        \                val next = parent(curr)\n                parent(curr) = root\n\
        \                curr = next\n            }\n            root\n        }\n\n\
        \        def union(i: Int, j: Int): Unit = {\n            val rootI = find(i)\n\
        \            val rootJ = find(j)\n            if (rootI != rootJ) {\n      \
        \          parent(rootI) = rootJ\n            }\n        }\n\n        for (swap\
        \ <- allowedSwaps) {\n            union(swap(0), swap(1))\n        }\n\n   \
        \     val groups = mutable.HashMap[Int, mutable.ListBuffer[Int]]()\n       \
        \ for (i <- 0 until n) {\n            val root = find(i)\n            groups.getOrElseUpdate(root,\
        \ mutable.ListBuffer[Int]()) += i\n        }\n\n        var matchingCount =\
        \ 0\n        for (indices <- groups.values) {\n            val counts = mutable.HashMap[Int,\
        \ Int]().withDefaultValue(0)\n            for (idx <- indices) {\n         \
        \       counts(source(idx)) += 1\n            }\n            for (idx <- indices)\
        \ {\n                val tVal = target(idx)\n                if (counts(tVal)\
        \ > 0) {\n                    matchingCount += 1\n                    counts(tVal)\
        \ -= 1\n                }\n            }\n        }\n\n        n - matchingCount\n\
        \    }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn minimum_hamming_distance(source:\
        \ Vec<i32>, target: Vec<i32>, allowed_swaps: Vec<Vec<i32>>) -> i32 {\n     \
        \   let n = source.len();\n        let mut parent: Vec<usize> = (0..n).collect();\n\
        \n        fn find(parent: &mut [usize], mut i: usize) -> usize {\n         \
        \   let mut root = i;\n            while parent[root] != root {\n          \
        \      root = parent[root];\n            }\n            let mut curr = i;\n\
        \            while parent[curr] != root {\n                let next = parent[curr];\n\
        \                parent[curr] = root;\n                curr = next;\n      \
        \      }\n            root\n        }\n\n        for swap in allowed_swaps {\n\
        \            let root_u = find(&mut parent, swap[0] as usize);\n           \
        \ let root_v = find(&mut parent, swap[1] as usize);\n            if root_u !=\
        \ root_v {\n                parent[root_u] = root_v;\n            }\n      \
        \  }\n\n        let mut components: HashMap<usize, Vec<usize>> = HashMap::new();\n\
        \        for i in 0..n {\n            let root = find(&mut parent, i);\n   \
        \         components.entry(root).or_default().push(i);\n        }\n\n      \
        \  let mut matches = 0;\n        for indices in components.values() {\n    \
        \        let mut counts = HashMap::new();\n            for &idx in indices {\n\
        \                *counts.entry(source[idx]).or_insert(0) += 1;\n           \
        \ }\n            for &idx in indices {\n                let target_val = target[idx];\n\
        \                if let Some(count) = counts.get_mut(&target_val) {\n      \
        \              if *count > 0 {\n                        *count -= 1;\n     \
        \                   matches += 1;\n                    }\n                }\n\
        \            }\n        }\n\n        (n - matches) as i32\n    }\n}"
      racket: "(define/contract (minimum-hamming-distance source target allowedSwaps)\n\
        \  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([n (length source)]\n         [parent (make-vector\
        \ n)]\n         [source-vec (list->vector source)]\n         [target-vec (list->vector\
        \ target)]\n         [matches-box (box 0)])\n    (for ([i (in-range n)])\n \
        \     (vector-set! parent i i))\n\n    (define (find i)\n      (let loop ([curr\
        \ i] [path '()])\n        (let ([p (vector-ref parent curr)])\n          (if\
        \ (= p curr)\n              (begin\n                (for ([node path])\n   \
        \               (vector-set! parent node curr))\n                curr)\n   \
        \           (loop p (cons curr path))))))\n\n    (define (union i j)\n     \
        \ (let ([root-i (find i)]\n            [root-j (find j)])\n        (unless (=\
        \ root-i root-j)\n          (vector-set! parent root-i root-j))))\n\n    (for\
        \ ([swap allowedSwaps])\n      (union (car swap) (car (cdr swap))))\n\n    (let\
        \ ([components (make-hasheq)])\n      (for ([i (in-range n)])\n        (let*\
        \ ([root (find i)]\n               [indices (hash-ref components root '())])\n\
        \          (hash-set! components root (cons i indices))))\n\n      (for ([(root\
        \ indices) (in-hash components)])\n        (let ([counts (make-hash)])\n   \
        \       (for ([idx indices])\n            (let ([val (vector-ref source-vec\
        \ idx)])\n              (hash-set! counts val (+ (hash-ref counts val 0) 1))))\n\
        \          (for ([idx indices])\n            (let* ([val (vector-ref target-vec\
        \ idx)]\n                   [count (hash-ref counts val 0)])\n             \
        \ (when (> count 0)\n                (set-box! matches-box (+ (unbox matches-box)\
        \ 1))\n                (hash-set! counts val (- count 1)))))))\n\n      (- n\
        \ (unbox matches-box)))))"
      erlang: "-spec minimum_hamming_distance(Source :: [integer()], Target :: [integer()],\
        \ AllowedSwaps :: [[integer()]]) -> integer().\nminimum_hamming_distance(Source,\
        \ Target, AllowedSwaps) ->\n    N = length(Source),\n    SourceVec = list_to_tuple(Source),\n\
        \    TargetVec = list_to_tuple(Target),\n\n    Adj = lists:foldl(fun([U, V],\
        \ Acc) ->\n        Acc1 = maps:put(U, [V | maps:get(U, Acc, [])], Acc),\n  \
        \      maps:put(V, [U | maps:get(V, Acc1, [])], Acc1)\n    end, #{}, AllowedSwaps),\n\
        \n    {TotalMatches, _} = lists:foldl(fun(I, {MatchesAcc, Visited}) ->\n   \
        \     case maps:is_key(I, Visited) of\n            true -> {MatchesAcc, Visited};\n\
        \            false ->\n                {ComponentIndices, NewVisited} = bfs(I,\
        \ Adj, Visited),\n                Matches = count_matches(ComponentIndices,\
        \ SourceVec, TargetVec),\n                {MatchesAcc + Matches, NewVisited}\n\
        \        end\n    end, {0, #{}}, lists:seq(0, N - 1)),\n\n    N - TotalMatches.\n\
        \nbfs(StartNode, Adj, Visited) ->\n    Queue = queue:from_list([StartNode]),\n\
        \    bfs_loop(Queue, Adj, maps:put(StartNode, true, Visited), [StartNode]).\n\
        \nbfs_loop(Queue, Adj, Visited, ComponentIndices) ->\n    case queue:out(Queue)\
        \ of\n        {{value, Node}, RestQueue} ->\n            Neighbors = maps:get(Node,\
        \ Adj, []),\n            {NewQueue, NewVisited, NewComponentIndices} = \n  \
        \              lists:foldl(fun(Neighbor, {Q, V, CI}) ->\n                  \
        \  case maps:is_key(Neighbor, V) of\n                        true -> {Q, V,\
        \ CI};\n                        false -> {queue:in(Neighbor, Q), maps:put(Neighbor,\
        \ true, V), [Neighbor | CI]}\n                    end\n                end,\
        \ {RestQueue, Visited, ComponentIndices}, Neighbors),\n            bfs_loop(NewQueue,\
        \ Adj, NewVisited, NewComponentIndices);\n        {empty, _} ->\n          \
        \  {ComponentIndices, Visited}\n    end.\n\ncount_matches(Indices, SourceVec,\
        \ TargetVec) ->\n    Counts = lists:foldl(fun(Idx, Acc) ->\n        Val = element(Idx\
        \ + 1, SourceVec),\n        maps:put(Val, maps:get(Val, Acc, 0) + 1, Acc)\n\
        \    end, #{}, Indices),\n\n    {Matches, _} = lists:foldl(fun(Idx, {M, C})\
        \ ->\n        Val = element(Idx + 1, TargetVec),\n        case maps:get(Val,\
        \ C, 0) of\n            Count when Count > 0 ->\n                {M + 1, maps:put(Val,\
        \ Count - 1, C)};\n            _ ->\n                {M, C}\n        end\n \
        \   end, {0, Counts}, Indices),\n    Matches."
      elixir: "defmodule Solution do\n  @spec minimum_hamming_distance(source :: [integer],\
        \ target :: [integer], allowed_swaps :: [[integer]]) :: integer\n  def minimum_hamming_distance(source,\
        \ target, allowed_swaps) do\n    n = length(source)\n    source_vec = List.to_tuple(source)\n\
        \    target_vec = List.to_tuple(target)\n\n    adj = Enum.reduce(allowed_swaps,\
        \ %{}, fn [u, v], acc ->\n      acc\n      |> Map.update(u, [v], &[v | &1])\n\
        \      |> Map.update(v, [u], &[u | &1])\n    end)\n\n    {total_matches, _visited}\
        \ = Enum.reduce(0..(n - 1), {0, %{}}, fn i, {matches_acc, visited} ->\n    \
        \  if Map.has_key?(visited, i) do\n        {matches_acc, visited}\n      else\n\
        \        {component_indices, new_visited} = bfs(i, adj, visited)\n        {matches_acc\
        \ + count_matches(component_indices, source_vec, target_vec), new_visited}\n\
        \      end\n    end)\n\n    n - total_matches\n  end\n\n  defp bfs(start_node,\
        \ adj, visited) do\n    queue = :queue.from_list([start_node])\n    bfs_loop(queue,\
        \ adj, Map.put(visited, start_node, true), [start_node])\n  end\n\n  defp bfs_loop(queue,\
        \ adj, visited, component_indices) do\n    case :queue.out(queue) do\n     \
        \ {{:value, node}, rest_queue} ->\n        neighbors = Map.get(adj, node, [])\n\
        \        {new_queue, new_visited, new_component_indices} = \n          Enum.reduce(neighbors,\
        \ {rest_queue, visited, component_indices}, fn neighbor, {q, v, ci} ->\n   \
        \         if Map.has_key?(v, neighbor) do\n              {q, v, ci}\n      \
        \      else\n              {:queue.in(neighbor, q), Map.put(v, neighbor, true),\
        \ [neighbor | ci]}\n            end\n          end)\n        bfs_loop(new_queue,\
        \ adj, new_visited, new_component_indices)\n      {:empty, _} ->\n        {component_indices,\
        \ visited}\n    end\n  end\n\n  defp count_matches(indices, source_vec, target_vec)\
        \ do\n    counts = Enum.reduce(indices, %{}, fn idx, acc ->\n      val = elem(source_vec,\
        \ idx)\n      Map.update(acc, val, 1, &(&1 + 1))\n    end)\n\n    {matches,\
        \ _} = Enum.reduce(indices, {0, counts}, fn idx, {m, c} ->\n      val = elem(target_vec,\
        \ idx)\n      case Map.get(c, val, 0) do\n        count when count > 0 -> {m\
        \ + 1, Map.put(c, val, count - 1)}\n        _ -> {m, c}\n      end\n    end)\n\
        \    matches\n  end\nend"
    approach: 'The problem can be modeled as a graph where each index is a node and
      each entry in allowedSwaps represents an edge. If two indices are in the same
      connected component, the elements at those positions in the source array can be
      swapped multiple times to achieve any arbitrary permutation of those elements.
      We use the Disjoint Set Union (DSU) algorithm to efficiently identify these connected
      components across the array indices. Each component acts as an independent set
      of values that can be rearranged to match the values at the corresponding indices
      in the target array.


      For each identified component, we extract the values from the source and target
      arrays at those specific indices. We then calculate how many elements in the source
      values can match the elements in the target values within that component. This
      is effectively the intersection of the two multisets. The number of such matches
      across all components represents the maximum number of positions where source[i]
      can equal target[i]. Finally, the minimum Hamming distance is calculated by subtracting
      the total number of matches from the total length of the array.'
    time_complexity: O(N \log N + E \alpha(N)) where N is the length of the arrays and
      E is the number of allowed swaps. Building the components using DSU takes O(E
      \alpha(N)), where \alpha is the inverse Ackermann function. Grouping the indices
      into components takes O(N). For each component, counting the matches takes O(K)
      using a hash map or O(K \log K) using sorting (where K is the component size).
      Across all components, this sums to O(N) or O(N \log N).
    space_complexity: O(N) to store the DSU parent pointers, the component groupings,
      and the frequency counts (or temporary buffers) for each component. All these
      structures scale linearly with the size of the input array.
    elapsed_time: 285.74091506004333
    model: gemini-3-flash-preview
    generated_at: '2026-04-21 02:00:07 '
---

## Problem #1722: Minimize Hamming Distance After Swap Operations

**Difficulty:** Medium

**Topics:** Array, Depth-First Search, Union-Find

## Problem Description

<p>You are given two integer arrays, <code>source</code> and <code>target</code>, both of length <code>n</code>. You are also given an array <code>allowedSwaps</code> where each <code>allowedSwaps[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you are allowed to swap the elements at index <code>a<sub>i</sub></code> and index <code>b<sub>i</sub></code> <strong>(0-indexed)</strong> of array <code>source</code>. Note that you can swap elements at a specific pair of indices <strong>multiple</strong> times and in <strong>any</strong> order.</p>

<p>The <strong>Hamming distance</strong> of two arrays of the same length, <code>source</code> and <code>target</code>, is the number of positions where the elements are different. Formally, it is the number of indices <code>i</code> for <code>0 &lt;= i &lt;= n-1</code> where <code>source[i] != target[i]</code> <strong>(0-indexed)</strong>.</p>

<p>Return <em>the <strong>minimum Hamming distance</strong> of </em><code>source</code><em> and </em><code>target</code><em> after performing <strong>any</strong> amount of swap operations on array </em><code>source</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> source can be transformed the following way:
- Swap indices 0 and 1: source = [<u>2</u>,<u>1</u>,3,4]
- Swap indices 2 and 3: source = [2,1,<u>4</u>,<u>3</u>]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are no allowed swaps.
The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == source.length == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= source[i], target[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= allowedSwaps.length &lt;= 10<sup>5</sup></code></li>
	<li><code>allowedSwaps[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
</ul>


## Hints

1. The source array can be imagined as a graph where each index is a node and each allowedSwaps[i] is an edge.

2. Nodes within the same component can be freely swapped with each other.

3. For each component, find the number of common elements. The elements that are not in common will contribute to the total Hamming distance.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as a graph where each index is a node and each entry in allowedSwaps represents an edge. If two indices are in the same connected component, the elements at those positions in the source array can be swapped multiple times to achieve any arbitrary permutation of those elements. We use the Disjoint Set Union (DSU) algorithm to efficiently identify these connected components across the array indices. Each component acts as an independent set of values that can be rearranged to match the values at the corresponding indices in the target array.

For each identified component, we extract the values from the source and target arrays at those specific indices. We then calculate how many elements in the source values can match the elements in the target values within that component. This is effectively the intersection of the two multisets. The number of such matches across all components represents the maximum number of positions where source[i] can equal target[i]. Finally, the minimum Hamming distance is calculated by subtracting the total number of matches from the total length of the array.

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
    int find(vector<int>& parent, int i) {
        int root = i;
        while (parent[root] != root) root = parent[root];
        while (parent[i] != root) {
            int next = parent[i];
            parent[i] = root;
            i = next;
        }
        return root;
    }

    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        int n = source.size();
        vector<int> parent(n);
        for (int i = 0; i < n; i++) parent[i] = i;

        for (const auto& sw : allowedSwaps) {
            int r1 = find(parent, sw[0]);
            int r2 = find(parent, sw[1]);
            if (r1 != r2) parent[r1] = r2;
        }

        unordered_map<int, vector<int>> components;
        for (int i = 0; i < n; i++) {
            components[find(parent, i)].push_back(i);
        }

        int matches = 0;
        for (auto const& [root, indices] : components) {
            unordered_map<int, int> counts;
            for (int idx : indices) counts[source[idx]]++;
            for (int idx : indices) {
                if (counts[target[idx]] > 0) {
                    counts[target[idx]]--;
                    matches++;
                }
            }
        }
        return n - matches;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    private int find(int[] parent, int i) {
        int root = i;
        while (parent[root] != root) {
            root = parent[root];
        }
        while (parent[i] != root) {
            int next = parent[i];
            parent[i] = root;
            i = next;
        }
        return root;
    }

    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        int n = source.length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        for (int[] sw : allowedSwaps) {
            int r1 = find(parent, sw[0]);
            int r2 = find(parent, sw[1]);
            if (r1 != r2) parent[r1] = r2;
        }

        Map<Integer, List<Integer>> components = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int root = find(parent, i);
            components.computeIfAbsent(root, k -> new ArrayList<>()).add(i);
        }

        int matches = 0;
        for (List<Integer> indices : components.values()) {
            Map<Integer, Integer> counts = new HashMap<>();
            for (int idx : indices) {
                counts.put(source[idx], counts.getOrDefault(source[idx], 0) + 1);
            }
            for (int idx : indices) {
                int val = target[idx];
                if (counts.getOrDefault(val, 0) > 0) {
                    counts.put(val, counts.get(val) - 1);
                    matches++;
                }
            }
        }

        return n - matches;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)
        parent = list(range(n))

        def find(i):
            root = i
            while parent[root] != root:
                root = parent[root]
            while parent[i] != root:
                nxt = parent[i]
                parent[i] = root
                i = nxt
            return root

        for a, b in allowedSwaps:
            r1, r2 = find(a), find(b)
            if r1 != r2:
                parent[r1] = r2

        components = collections.defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)

        matches = 0
        for indices in components.values():
            counts = collections.defaultdict(int)
            for i in indices:
                counts[source[i]] += 1
            for i in indices:
                if counts[target[i]] > 0:
                    counts[target[i]] -= 1
                    matches += 1

        return n - matches
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections
from typing import List

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(i):
            root = i
            while parent[root] != root:
                root = parent[root]
            while parent[i] != root:
                nxt = parent[i]
                parent[i] = root
                i = nxt
            return root

        for a, b in allowedSwaps:
            r1, r2 = find(a), find(b)
            if r1 != r2:
                parent[r1] = r2

        components = collections.defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)

        matches = 0
        for indices in components.values():
            counts = collections.Counter()
            for i in indices:
                counts[source[i]] += 1
            for i in indices:
                if counts[target[i]] > 0:
                    counts[target[i]] -= 1
                    matches += 1

        return n - matches
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

int find(int* parent, int i) {
    int root = i;
    while (parent[root] != root) root = parent[root];
    while (parent[i] != root) {
        int next = parent[i];
        parent[i] = root;
        i = next;
    }
    return root;
}

int compare(const void* a, const void* b) {
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int minimumHammingDistance(int* source, int sourceSize, int* target, int targetSize, int** allowedSwaps, int allowedSwapsSize, int* allowedSwapsColSize) {
    int n = sourceSize;
    int* parent = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;

    for (int i = 0; i < allowedSwapsSize; i++) {
        int r1 = find(parent, allowedSwaps[i][0]);
        int r2 = find(parent, allowedSwaps[i][1]);
        if (r1 != r2) parent[r1] = r2;
    }

    int* heads = (int*)malloc(n * sizeof(int));
    int* nexts = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) heads[i] = -1;
    for (int i = 0; i < n; i++) {
        int root = find(parent, i);
        nexts[i] = heads[root];
        heads[root] = i;
    }

    int* s_buf = (int*)malloc(n * sizeof(int));
    int* t_buf = (int*)malloc(n * sizeof(int));
    int total_matches = 0;

    for (int i = 0; i < n; i++) {
        if (heads[i] == -1) continue;
        int count = 0;
        for (int curr = heads[i]; curr != -1; curr = nexts[curr]) {
            s_buf[count] = source[curr];
            t_buf[count] = target[curr];
            count++;
        }

        qsort(s_buf, count, sizeof(int), compare);
        qsort(t_buf, count, sizeof(int), compare);

        int p1 = 0, p2 = 0;
        while (p1 < count && p2 < count) {
            if (s_buf[p1] == t_buf[p2]) {
                total_matches++;
                p1++;
                p2++;
            } else if (s_buf[p1] < t_buf[p2]) {
                p1++;
            } else {
                p2++;
            }
        }
    }

    free(parent);
    free(heads);
    free(nexts);
    free(s_buf);
    free(t_buf);

    return n - total_matches;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int MinimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        int n = source.Length;
        int[] parent = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        int Find(int i) {
            int root = i;
            while (parent[root] != root) root = parent[root];
            int curr = i;
            while (parent[curr] != root) {
                int next = parent[curr];
                parent[curr] = root;
                curr = next;
            }
            return root;
        }

        void Union(int i, int j) {
            int rootI = Find(i);
            int rootJ = Find(j);
            if (rootI != rootJ) {
                if (rank[rootI] < rank[rootJ]) parent[rootI] = rootJ;
                else if (rank[rootI] > rank[rootJ]) parent[rootJ] = rootI;
                else {
                    parent[rootI] = rootJ;
                    rank[rootJ]++;
                }
            }
        }

        foreach (var swap in allowedSwaps) {
            Union(swap[0], swap[1]);
        }

        var groups = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            int r = Find(i);
            if (!groups.ContainsKey(r)) {
                groups[r] = new List<int>();
            }
            groups[r].Add(i);
        }

        int totalMatching = 0;
        var counts = new Dictionary<int, int>();
        foreach (var indices in groups.Values) {
            counts.Clear();
            foreach (int idx in indices) {
                int val = source[idx];
                if (counts.ContainsKey(val)) counts[val]++;
                else counts[val] = 1;
            }
            foreach (int idx in indices) {
                int val = target[idx];
                if (counts.ContainsKey(val) && counts[val] > 0) {
                    totalMatching++;
                    counts[val]--;
                }
            }
        }

        return n - totalMatching;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} source
 * @param {number[]} target
 * @param {number[][]} allowedSwaps
 * @return {number}
 */
var minimumHammingDistance = function(source, target, allowedSwaps) {
    const n = source.length;
    const parent = new Int32Array(n);
    const rank = new Int32Array(n);
    for (let i = 0; i < n; i++) parent[i] = i;

    function find(i) {
        let root = i;
        while (parent[root] !== root) root = parent[root];
        let curr = i;
        while (parent[curr] !== root) {
            let next = parent[curr];
            parent[curr] = root;
            curr = next;
        }
        return root;
    }

    function union(i, j) {
        const rootI = find(i);
        const rootJ = find(j);
        if (rootI !== rootJ) {
            if (rank[rootI] < rank[rootJ]) parent[rootI] = rootJ;
            else if (rank[rootI] > rank[rootJ]) parent[rootJ] = rootI;
            else {
                parent[rootI] = rootJ;
                rank[rootJ]++;
            }
        }
    }

    for (let i = 0; i < allowedSwaps.length; i++) {
        union(allowedSwaps[i][0], allowedSwaps[i][1]);
    }

    const groups = new Map();
    for (let i = 0; i < n; i++) {
        const r = find(i);
        if (!groups.has(r)) groups.set(r, []);
        groups.get(r).push(i);
    }

    let totalMatching = 0;
    for (const indices of groups.values()) {
        const counts = new Map();
        for (let i = 0; i < indices.length; i++) {
            const idx = indices[i];
            const val = source[idx];
            counts.set(val, (counts.get(val) || 0) + 1);
        }
        for (let i = 0; i < indices.length; i++) {
            const idx = indices[i];
            const val = target[idx];
            const count = counts.get(val);
            if (count > 0) {
                totalMatching++;
                counts.set(val, count - 1);
            }
        }
    }

    return n - totalMatching;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumHammingDistance(source: number[], target: number[], allowedSwaps: number[][]): number {
    const n = source.length;
    const parent = new Int32Array(n);
    const rank = new Int32Array(n);
    for (let i = 0; i < n; i++) parent[i] = i;

    function find(i: number): number {
        let root = i;
        while (parent[root] !== root) root = parent[root];
        let curr = i;
        while (parent[curr] !== root) {
            let next = parent[curr];
            parent[curr] = root;
            curr = next;
        }
        return root;
    }

    function union(i: number, j: number): void {
        const rootI = find(i);
        const rootJ = find(j);
        if (rootI !== rootJ) {
            if (rank[rootI] < rank[rootJ]) parent[rootI] = rootJ;
            else if (rank[rootI] > rank[rootJ]) parent[rootJ] = rootI;
            else {
                parent[rootI] = rootJ;
                rank[rootJ]++;
            }
        }
    }

    for (let i = 0; i < allowedSwaps.length; i++) {
        union(allowedSwaps[i][0], allowedSwaps[i][1]);
    }

    const groups = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        const r = find(i);
        if (!groups.has(r)) groups.set(r, []);
        groups.get(r)!.push(i);
    }

    let totalMatching = 0;
    for (const indices of groups.values()) {
        const counts = new Map<number, number>();
        for (let i = 0; i < indices.length; i++) {
            const idx = indices[i];
            const val = source[idx];
            counts.set(val, (counts.get(val) || 0) + 1);
        }
        for (let i = 0; i < indices.length; i++) {
            const idx = indices[i];
            const val = target[idx];
            const count = counts.get(val);
            if (count && count > 0) {
                totalMatching++;
                counts.set(val, count - 1);
            }
        }
    }

    return n - totalMatching;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $source
     * @param Integer[] $target
     * @param Integer[][] $allowedSwaps
     * @return Integer
     */
    function minimumHammingDistance($source, $target, $allowedSwaps) {
        $n = count($source);
        $parent = range(0, $n - 1);
        $rank = array_fill(0, $n, 0);

        $find = function($i) use (&$parent) {
            $root = $i;
            while ($parent[$root] != $root) {
                $root = $parent[$root];
            }
            $curr = $i;
            while ($parent[$curr] != $root) {
                $next = $parent[$curr];
                $parent[$curr] = $root;
                $curr = $next;
            }
            return $root;
        };

        $union = function($i, $j) use (&$parent, &$rank, $find) {
            $rootI = $find($i);
            $rootJ = $find($j);
            if ($rootI != $rootJ) {
                if ($rank[$rootI] < $rank[$rootJ]) {
                    $parent[$rootI] = $rootJ;
                } else if ($rank[$rootI] > $rank[$rootJ]) {
                    $parent[$rootJ] = $rootI;
                } else {
                    $parent[$rootI] = $rootJ;
                    $rank[$rootJ]++;
                }
            }
        };

        foreach ($allowedSwaps as $swap) {
            $union($swap[0], $swap[1]);
        }

        $groups = [];
        for ($i = 0; $i < $n; $i++) {
            $r = $find($i);
            $groups[$r][] = $i;
        }

        $totalMatching = 0;
        foreach ($groups as $indices) {
            $counts = [];
            foreach ($indices as $idx) {
                $val = $source[$idx];
                $counts[$val] = ($counts[$val] ?? 0) + 1;
            }
            foreach ($indices as $idx) {
                $val = $target[$idx];
                if (isset($counts[$val]) && $counts[$val] > 0) {
                    $totalMatching++;
                    $counts[$val]--;
                }
            }
        }

        return $n - $totalMatching;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumHammingDistance(_ source: [Int], _ target: [Int], _ allowedSwaps: [[Int]]) -> Int {
        let n = source.count
        var parent = Array(0..<n)
        var rank = [Int](repeating: 0, count: n)

        func find(_ i: Int) -> Int {
            var root = i
            while parent[root] != root {
                root = parent[root]
            }
            var curr = i
            while parent[curr] != root {
                let next = parent[curr]
                parent[curr] = root
                curr = next
            }
            return root
        }

        func union(_ i: Int, _ j: Int) {
            let rootI = find(i)
            let rootJ = find(j)
            if rootI != rootJ {
                if rank[rootI] < rank[rootJ] {
                    parent[rootI] = rootJ
                } else if rank[rootI] > rank[rootJ] {
                    parent[rootJ] = rootI
                } else {
                    parent[rootI] = rootJ
                    rank[rootJ] += 1
                }
            }
        }

        for swap in allowedSwaps {
            union(swap[0], swap[1])
        }

        var groups = [Int: [Int]]()
        for i in 0..<n {
            let r = find(i)
            groups[r, default: []].append(i)
        }

        var totalMatching = 0
        for indices in groups.values {
            var counts = [Int: Int]()
            for idx in indices {
                let val = source[idx]
                counts[val, default: 0] += 1
            }
            for idx in indices {
                let val = target[idx]
                if let count = counts[val], count > 0 {
                    totalMatching += 1
                    counts[val] = count - 1
                }
            }
        }

        return n - totalMatching
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumHammingDistance(source: IntArray, target: IntArray, allowedSwaps: Array<IntArray>): Int {
        val n = source.size
        val parent = IntArray(n) { it }

        fun find(i: Int): Int {
            var root = i
            while (parent[root] != root) {
                root = parent[root]
            }
            var curr = i
            while (parent[curr] != root) {
                val next = parent[curr]
                parent[curr] = root
                curr = next
            }
            return root
        }

        fun union(i: Int, j: Int) {
            val rootI = find(i)
            val rootJ = find(j)
            if (rootI != rootJ) {
                parent[rootI] = rootJ
            }
        }

        for (swap in allowedSwaps) {
            union(swap[0], swap[1])
        }

        val groups = mutableMapOf<Int, MutableList<Int>>()
        for (i in 0 until n) {
            val root = find(i)
            groups.getOrPut(root) { mutableListOf<Int>() }.add(i)
        }

        var matchingCount = 0
        for (indices in groups.values) {
            val counts = mutableMapOf<Int, Int>()
            for (idx in indices) {
                val sVal = source[idx]
                counts[sVal] = counts.getOrDefault(sVal, 0) + 1
            }
            for (idx in indices) {
                val tVal = target[idx]
                val c = counts.getOrDefault(tVal, 0)
                if (c > 0) {
                    matchingCount++
                    counts[tVal] = c - 1
                }
            }
        }

        return n - matchingCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumHammingDistance(List<int> source, List<int> target, List<List<int>> allowedSwaps) {
    final n = source.length;
    final parent = List<int>.generate(n, (i) => i);

    int find(int i) {
      int root = i;
      while (parent[root] != root) {
        root = parent[root];
      }
      int curr = i;
      while (parent[curr] != root) {
        int next = parent[curr];
        parent[curr] = root;
        curr = next;
      }
      return root;
    }

    void union(int i, int j) {
      final rootI = find(i);
      final rootJ = find(j);
      if (rootI != rootJ) {
        parent[rootI] = rootJ;
      }
    }

    for (final swap in allowedSwaps) {
      union(swap[0], swap[1]);
    }

    final groups = <int, List<int>>{};
    for (int i = 0; i < n; i++) {
      final root = find(i);
      groups.putIfAbsent(root, () => []).add(i);
    }

    int matchingCount = 0;
    for (final indices in groups.values) {
      final counts = <int, int>{};
      for (final idx in indices) {
        counts[source[idx]] = (counts[source[idx]] ?? 0) + 1;
      }
      for (final idx in indices) {
        final tVal = target[idx];
        final c = counts[tVal] ?? 0;
        if (c > 0) {
          matchingCount++;
          counts[tVal] = c - 1;
        }
      }
    }

    return n - matchingCount;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumHammingDistance(source []int, target []int, allowedSwaps [][]int) int {
    n := len(source)
    parent := make([]int, n)
    for i := range parent {
        parent[i] = i
    }

    find := func(i int) int {
        root := i
        for parent[root] != root {
            root = parent[root]
        }
        curr := i
        for parent[curr] != root {
            next := parent[curr]
            parent[curr] = root
            curr = next
        }
        return root
    }

    union := func(i, j int) {
        rootI := find(i)
        rootJ := find(j)
        if rootI != rootJ {
            parent[rootI] = rootJ
        }
    }

    for _, swap := range allowedSwaps {
        union(swap[0], swap[1])
    }

    groups := make(map[int][]int)
    for i := 0; i < n; i++ {
        root := find(i)
        groups[root] = append(groups[root], i)
    }

    matchingCount := 0
    for _, indices := range groups {
        counts := make(map[int]int)
        for _, idx := range indices {
            counts[source[idx]]++
        }
        for _, idx := range indices {
            tVal := target[idx]
            if counts[tVal] > 0 {
                matchingCount++
                counts[tVal]--
            }
        }
    }

    return n - matchingCount
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_hamming_distance(source, target, allowed_swaps)
  n = source.length
  parent = (0...n).to_a

  find = lambda do |i|
    root = i
    root = parent[root] while parent[root] != root
    curr = i
    while parent[curr] != root
      nxt = parent[curr]
      parent[curr] = root
      curr = nxt
    end
    root
  end

  allowed_swaps.each do |a, b|
    root_a = find.call(a)
    root_b = find.call(b)
    parent[root_a] = root_b if root_a != root_b
  end

  groups = Hash.new { |h, k| h[k] = [] }
  (0...n).each do |i|
    groups[find.call(i)] << i
  end

  matching_count = 0
  groups.each_value do |indices|
    counts = Hash.new(0)
    indices.each { |idx| counts[source[idx]] += 1 }
    indices.each do |idx|
      t_val = target[idx]
      if counts[t_val] > 0
        matching_count += 1
        counts[t_val] -= 1
      	end
    end
  end

  n - matching_count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def minimumHammingDistance(source: Array[Int], target: Array[Int], allowedSwaps: Array[Array[Int]]): Int = {
        val n = source.length
        val parent = (0 until n).toArray

        def find(i: Int): Int = {
            var root = i
            while (parent(root) != root) {
                root = parent(root)
            }
            var curr = i
            while (parent(curr) != root) {
                val next = parent(curr)
                parent(curr) = root
                curr = next
            }
            root
        }

        def union(i: Int, j: Int): Unit = {
            val rootI = find(i)
            val rootJ = find(j)
            if (rootI != rootJ) {
                parent(rootI) = rootJ
            }
        }

        for (swap <- allowedSwaps) {
            union(swap(0), swap(1))
        }

        val groups = mutable.HashMap[Int, mutable.ListBuffer[Int]]()
        for (i <- 0 until n) {
            val root = find(i)
            groups.getOrElseUpdate(root, mutable.ListBuffer[Int]()) += i
        }

        var matchingCount = 0
        for (indices <- groups.values) {
            val counts = mutable.HashMap[Int, Int]().withDefaultValue(0)
            for (idx <- indices) {
                counts(source(idx)) += 1
            }
            for (idx <- indices) {
                val tVal = target(idx)
                if (counts(tVal) > 0) {
                    matchingCount += 1
                    counts(tVal) -= 1
                }
            }
        }

        n - matchingCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;

impl Solution {
    pub fn minimum_hamming_distance(source: Vec<i32>, target: Vec<i32>, allowed_swaps: Vec<Vec<i32>>) -> i32 {
        let n = source.len();
        let mut parent: Vec<usize> = (0..n).collect();

        fn find(parent: &mut [usize], mut i: usize) -> usize {
            let mut root = i;
            while parent[root] != root {
                root = parent[root];
            }
            let mut curr = i;
            while parent[curr] != root {
                let next = parent[curr];
                parent[curr] = root;
                curr = next;
            }
            root
        }

        for swap in allowed_swaps {
            let root_u = find(&mut parent, swap[0] as usize);
            let root_v = find(&mut parent, swap[1] as usize);
            if root_u != root_v {
                parent[root_u] = root_v;
            }
        }

        let mut components: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 0..n {
            let root = find(&mut parent, i);
            components.entry(root).or_default().push(i);
        }

        let mut matches = 0;
        for indices in components.values() {
            let mut counts = HashMap::new();
            for &idx in indices {
                *counts.entry(source[idx]).or_insert(0) += 1;
            }
            for &idx in indices {
                let target_val = target[idx];
                if let Some(count) = counts.get_mut(&target_val) {
                    if *count > 0 {
                        *count -= 1;
                        matches += 1;
                    }
                }
            }
        }

        (n - matches) as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-hamming-distance source target allowedSwaps)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length source)]
         [parent (make-vector n)]
         [source-vec (list->vector source)]
         [target-vec (list->vector target)]
         [matches-box (box 0)])
    (for ([i (in-range n)])
      (vector-set! parent i i))

    (define (find i)
      (let loop ([curr i] [path '()])
        (let ([p (vector-ref parent curr)])
          (if (= p curr)
              (begin
                (for ([node path])
                  (vector-set! parent node curr))
                curr)
              (loop p (cons curr path))))))

    (define (union i j)
      (let ([root-i (find i)]
            [root-j (find j)])
        (unless (= root-i root-j)
          (vector-set! parent root-i root-j))))

    (for ([swap allowedSwaps])
      (union (car swap) (car (cdr swap))))

    (let ([components (make-hasheq)])
      (for ([i (in-range n)])
        (let* ([root (find i)]
               [indices (hash-ref components root '())])
          (hash-set! components root (cons i indices))))

      (for ([(root indices) (in-hash components)])
        (let ([counts (make-hash)])
          (for ([idx indices])
            (let ([val (vector-ref source-vec idx)])
              (hash-set! counts val (+ (hash-ref counts val 0) 1))))
          (for ([idx indices])
            (let* ([val (vector-ref target-vec idx)]
                   [count (hash-ref counts val 0)])
              (when (> count 0)
                (set-box! matches-box (+ (unbox matches-box) 1))
                (hash-set! counts val (- count 1)))))))

      (- n (unbox matches-box)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_hamming_distance(Source :: [integer()], Target :: [integer()], AllowedSwaps :: [[integer()]]) -> integer().
minimum_hamming_distance(Source, Target, AllowedSwaps) ->
    N = length(Source),
    SourceVec = list_to_tuple(Source),
    TargetVec = list_to_tuple(Target),

    Adj = lists:foldl(fun([U, V], Acc) ->
        Acc1 = maps:put(U, [V | maps:get(U, Acc, [])], Acc),
        maps:put(V, [U | maps:get(V, Acc1, [])], Acc1)
    end, #{}, AllowedSwaps),

    {TotalMatches, _} = lists:foldl(fun(I, {MatchesAcc, Visited}) ->
        case maps:is_key(I, Visited) of
            true -> {MatchesAcc, Visited};
            false ->
                {ComponentIndices, NewVisited} = bfs(I, Adj, Visited),
                Matches = count_matches(ComponentIndices, SourceVec, TargetVec),
                {MatchesAcc + Matches, NewVisited}
        end
    end, {0, #{}}, lists:seq(0, N - 1)),

    N - TotalMatches.

bfs(StartNode, Adj, Visited) ->
    Queue = queue:from_list([StartNode]),
    bfs_loop(Queue, Adj, maps:put(StartNode, true, Visited), [StartNode]).

bfs_loop(Queue, Adj, Visited, ComponentIndices) ->
    case queue:out(Queue) of
        {{value, Node}, RestQueue} ->
            Neighbors = maps:get(Node, Adj, []),
            {NewQueue, NewVisited, NewComponentIndices} = 
                lists:foldl(fun(Neighbor, {Q, V, CI}) ->
                    case maps:is_key(Neighbor, V) of
                        true -> {Q, V, CI};
                        false -> {queue:in(Neighbor, Q), maps:put(Neighbor, true, V), [Neighbor | CI]}
                    end
                end, {RestQueue, Visited, ComponentIndices}, Neighbors),
            bfs_loop(NewQueue, Adj, NewVisited, NewComponentIndices);
        {empty, _} ->
            {ComponentIndices, Visited}
    end.

count_matches(Indices, SourceVec, TargetVec) ->
    Counts = lists:foldl(fun(Idx, Acc) ->
        Val = element(Idx + 1, SourceVec),
        maps:put(Val, maps:get(Val, Acc, 0) + 1, Acc)
    end, #{}, Indices),

    {Matches, _} = lists:foldl(fun(Idx, {M, C}) ->
        Val = element(Idx + 1, TargetVec),
        case maps:get(Val, C, 0) of
            Count when Count > 0 ->
                {M + 1, maps:put(Val, Count - 1, C)};
            _ ->
                {M, C}
        end
    end, {0, Counts}, Indices),
    Matches.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_hamming_distance(source :: [integer], target :: [integer], allowed_swaps :: [[integer]]) :: integer
  def minimum_hamming_distance(source, target, allowed_swaps) do
    n = length(source)
    source_vec = List.to_tuple(source)
    target_vec = List.to_tuple(target)

    adj = Enum.reduce(allowed_swaps, %{}, fn [u, v], acc ->
      acc
      |> Map.update(u, [v], &[v | &1])
      |> Map.update(v, [u], &[u | &1])
    end)

    {total_matches, _visited} = Enum.reduce(0..(n - 1), {0, %{}}, fn i, {matches_acc, visited} ->
      if Map.has_key?(visited, i) do
        {matches_acc, visited}
      else
        {component_indices, new_visited} = bfs(i, adj, visited)
        {matches_acc + count_matches(component_indices, source_vec, target_vec), new_visited}
      end
    end)

    n - total_matches
  end

  defp bfs(start_node, adj, visited) do
    queue = :queue.from_list([start_node])
    bfs_loop(queue, adj, Map.put(visited, start_node, true), [start_node])
  end

  defp bfs_loop(queue, adj, visited, component_indices) do
    case :queue.out(queue) do
      {{:value, node}, rest_queue} ->
        neighbors = Map.get(adj, node, [])
        {new_queue, new_visited, new_component_indices} = 
          Enum.reduce(neighbors, {rest_queue, visited, component_indices}, fn neighbor, {q, v, ci} ->
            if Map.has_key?(v, neighbor) do
              {q, v, ci}
            else
              {:queue.in(neighbor, q), Map.put(v, neighbor, true), [neighbor | ci]}
            end
          end)
        bfs_loop(new_queue, adj, new_visited, new_component_indices)
      {:empty, _} ->
        {component_indices, visited}
    end
  end

  defp count_matches(indices, source_vec, target_vec) do
    counts = Enum.reduce(indices, %{}, fn idx, acc ->
      val = elem(source_vec, idx)
      Map.update(acc, val, 1, &(&1 + 1))
    end)

    {matches, _} = Enum.reduce(indices, {0, counts}, fn idx, {m, c} ->
      val = elem(target_vec, idx)
      case Map.get(c, val, 0) do
        count when count > 0 -> {m + 1, Map.put(c, val, count - 1)}
        _ -> {m, c}
      end
    end)
    matches
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N \log N + E \alpha(N)) where N is the length of the arrays and E is the number of allowed swaps. Building the components using DSU takes O(E \alpha(N)), where \alpha is the inverse Ackermann function. Grouping the indices into components takes O(N). For each component, counting the matches takes O(K) using a hash map or O(K \log K) using sorting (where K is the component size). Across all components, this sums to O(N) or O(N \log N).
- **Space Complexity:** O(N) to store the DSU parent pointers, the component groupings, and the frequency counts (or temporary buffers) for each component. All these structures scale linearly with the size of the input array.
