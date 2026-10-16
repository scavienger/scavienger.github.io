---
layout: post
title: "Subarrays Distinct Element Sum of Squares II"
date: 2026-10-16 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Binary Indexed Tree", "Segment Tree"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\n    long long MOD = 1e9 + 7;\n    vector<long long> s1,\
        \ s2, lazy;\n\n    void apply(int idx, int l, int r, long long v) {\n      \
        \  long long ln = r - l + 1;\n        s2[idx] = (s2[idx] + 2 * v * s1[idx] +\
        \ (v * v % MOD * ln % MOD)) % MOD;\n        s1[idx] = (s1[idx] + v * ln) % MOD;\n\
        \        lazy[idx] = (lazy[idx] + v) % MOD;\n    }\n\n    void pushDown(int\
        \ idx, int l, int r) {\n        if (lazy[idx] != 0) {\n            int mid =\
        \ (l + r) / 2;\n            apply(2 * idx, l, mid, lazy[idx]);\n           \
        \ apply(2 * idx + 1, mid + 1, r, lazy[idx]);\n            lazy[idx] = 0;\n \
        \       }\n    }\n\n    void update(int idx, int l, int r, int ql, int qr, int\
        \ v) {\n        if (ql <= l && r <= qr) {\n            apply(idx, l, r, v);\n\
        \            return;\n        }\n        pushDown(idx, l, r);\n        int mid\
        \ = (l + r) / 2;\n        if (ql <= mid) update(2 * idx, l, mid, ql, qr, v);\n\
        \        if (qr > mid) update(2 * idx + 1, mid + 1, r, ql, qr, v);\n       \
        \ s1[idx] = (s1[2 * idx] + s1[2 * idx + 1]) % MOD;\n        s2[idx] = (s2[2\
        \ * idx] + s2[2 * idx + 1]) % MOD;\n    }\n\npublic:\n    int sumCounts(vector<int>&\
        \ nums) {\n        int n = nums.size();\n        s1.assign(4 * n, 0);\n    \
        \    s2.assign(4 * n, 0);\n        lazy.assign(4 * n, 0);\n        vector<int>\
        \ last_pos(100001, -1);\n        long long total_ans = 0;\n\n        for (int\
        \ i = 0; i < n; ++i) {\n            int prev = last_pos[nums[i]];\n        \
        \    update(1, 0, n - 1, prev + 1, i, 1);\n            total_ans = (total_ans\
        \ + s2[1]) % MOD;\n            last_pos[nums[i]] = i;\n        }\n\n       \
        \ return (int)total_ans;\n    }\n};"
      java: "class Solution {\n    private static final int MOD = 1000000007;\n    private\
        \ long[] s1, s2, lazy;\n\n    private void apply(int idx, int l, int r, long\
        \ v) {\n        long ln = r - l + 1;\n        s2[idx] = (s2[idx] + 2 * v * s1[idx]\
        \ + (v * v % MOD) * ln) % MOD;\n        s1[idx] = (s1[idx] + v * ln) % MOD;\n\
        \        lazy[idx] = (lazy[idx] + v) % MOD;\n    }\n\n    private void pushDown(int\
        \ idx, int l, int r) {\n        if (lazy[idx] != 0) {\n            int mid =\
        \ l + (r - l) / 2;\n            apply(2 * idx, l, mid, lazy[idx]);\n       \
        \     apply(2 * idx + 1, mid + 1, r, lazy[idx]);\n            lazy[idx] = 0;\n\
        \        }\n    }\n\n    private void update(int idx, int l, int r, int ql,\
        \ int qr, int v) {\n        if (ql <= l && r <= qr) {\n            apply(idx,\
        \ l, r, v);\n            return;\n        }\n        pushDown(idx, l, r);\n\
        \        int mid = l + (r - l) / 2;\n        if (ql <= mid) update(2 * idx,\
        \ l, mid, ql, qr, v);\n        if (qr > mid) update(2 * idx + 1, mid + 1, r,\
        \ ql, qr, v);\n        s1[idx] = (s1[2 * idx] + s1[2 * idx + 1]) % MOD;\n  \
        \      s2[idx] = (s2[2 * idx] + s2[2 * idx + 1]) % MOD;\n    }\n\n    public\
        \ int sumCounts(int[] nums) {\n        int n = nums.length;\n        s1 = new\
        \ long[4 * n];\n        s2 = new long[4 * n];\n        lazy = new long[4 * n];\n\
        \        int[] lastPos = new int[100001];\n        java.util.Arrays.fill(lastPos,\
        \ -1);\n        long totalAns = 0;\n\n        for (int i = 0; i < n; i++) {\n\
        \            int prev = lastPos[nums[i]];\n            update(1, 0, n - 1, prev\
        \ + 1, i, 1);\n            totalAns = (totalAns + s2[1]) % MOD;\n          \
        \  lastPos[nums[i]] = i;\n        }\n\n        return (int) totalAns;\n    }\n\
        }"
      python: "import sys\n\nsys.setrecursionlimit(200000)\n\nclass Solution(object):\n\
        \    def sumCounts(self, nums):\n        \"\"\"\n        :type nums: List[int]\n\
        \        :rtype: int\n        \"\"\"\n        n = len(nums)\n        MOD = 10**9\
        \ + 7\n        s1 = [0] * (4 * n)\n        s2 = [0] * (4 * n)\n        lazy\
        \ = [0] * (4 * n)\n\n        def update(idx, l, r, ql, qr):\n            if\
        \ ql <= l and r <= qr:\n                ln = r - l + 1\n                s2[idx]\
        \ = (s2[idx] + (s1[idx] << 1) + ln) % MOD\n                s1[idx] = (s1[idx]\
        \ + ln) % MOD\n                lazy[idx] = (lazy[idx] + 1) % MOD\n         \
        \       return\n\n            mid = (l + r) >> 1\n            lz = lazy[idx]\n\
        \            if lz:\n                left, right = idx << 1, (idx << 1) | 1\n\
        \                ln_l = mid - l + 1\n                ln_r = r - mid\n      \
        \          lz_sq_l = (lz * lz * ln_l) % MOD\n                lz_sq_r = (lz *\
        \ lz * ln_r) % MOD\n                s2[left] = (s2[left] + (lz << 1) * s1[left]\
        \ + lz_sq_l) % MOD\n                s1[left] = (s1[left] + lz * ln_l) % MOD\n\
        \                lazy[left] = (lazy[left] + lz) % MOD\n                s2[right]\
        \ = (s2[right] + (lz << 1) * s1[right] + lz_sq_r) % MOD\n                s1[right]\
        \ = (s1[right] + lz * ln_r) % MOD\n                lazy[right] = (lazy[right]\
        \ + lz) % MOD\n                lazy[idx] = 0\n\n            if ql <= mid:\n\
        \                update(idx << 1, l, mid, ql, qr)\n            if qr > mid:\n\
        \                update((idx << 1) | 1, mid + 1, r, ql, qr)\n\n            left,\
        \ right = idx << 1, (idx << 1) | 1\n            s1[idx] = (s1[left] + s1[right])\
        \ % MOD\n            s2[idx] = (s2[left] + s2[right]) % MOD\n\n        ans =\
        \ 0\n        last_pos = [-1] * 100001\n        for i, val in enumerate(nums):\n\
        \            prev = last_pos[val]\n            update(1, 0, n - 1, prev + 1,\
        \ i)\n            ans = (ans + s2[1]) % MOD\n            last_pos[val] = i\n\
        \n        return ans"
      python3: "import sys\n\nsys.setrecursionlimit(200000)\n\nclass Solution:\n   \
        \ def sumCounts(self, nums: list[int]) -> int:\n        n = len(nums)\n    \
        \    MOD = 1000000007\n        sum_sq = [0] * (4 * n + 1)\n        sum_val =\
        \ [0] * (4 * n + 1)\n        lazy = [0] * (4 * n + 1)\n\n        def update(node,\
        \ l, r, ql, qr):\n            if ql <= l and r <= qr:\n                cnt =\
        \ r - l + 1\n                sum_sq[node] = (sum_sq[node] + (sum_val[node] <<\
        \ 1) + cnt) % MOD\n                sum_val[node] = (sum_val[node] + cnt) % MOD\n\
        \                lazy[node] += 1\n                return\n\n            mid\
        \ = (l + r) >> 1\n            lz = lazy[node]\n            lc = node << 1\n\
        \            rc = lc | 1\n            if lz:\n                cl, cr = mid -\
        \ l + 1, r - mid\n                lz_sq_mod = (lz * lz) % MOD\n            \
        \    sum_sq[lc] = (sum_sq[lc] + 2 * lz * sum_val[lc] + lz_sq_mod * cl) % MOD\n\
        \                sum_val[lc] = (sum_val[lc] + lz * cl) % MOD\n             \
        \   lazy[lc] += lz\n                sum_sq[rc] = (sum_sq[rc] + 2 * lz * sum_val[rc]\
        \ + lz_sq_mod * cr) % MOD\n                sum_val[rc] = (sum_val[rc] + lz *\
        \ cr) % MOD\n                lazy[rc] += lz\n                lazy[node] = 0\n\
        \n            if ql <= mid:\n                update(lc, l, mid, ql, qr)\n  \
        \          if qr > mid:\n                update(rc, mid + 1, r, ql, qr)\n\n\
        \            sum_sq[node] = (sum_sq[lc] + sum_sq[rc]) % MOD\n            sum_val[node]\
        \ = (sum_val[lc] + sum_val[rc]) % MOD\n\n        ans = 0\n        last_pos =\
        \ [-1] * 100001\n        for i, x in enumerate(nums):\n            update(1,\
        \ 0, n - 1, last_pos[x] + 1, i)\n            ans = (ans + sum_sq[1]) % MOD\n\
        \            last_pos[x] = i\n        return ans"
      c: "#include <string.h>\n\n#define MOD 1000000007\n\nlong long sum_sq[400005];\n\
        long long sum_val[400005];\nlong long lazy[400005];\nint last_pos[100001];\n\
        \nvoid apply(int node, int l, int r, long long v) {\n    long long cnt = r -\
        \ l + 1;\n    sum_sq[node] = (sum_sq[node] + 2 * v * sum_val[node] + (v * v\
        \ % MOD) * cnt) % MOD;\n    sum_val[node] = (sum_val[node] + v * cnt) % MOD;\n\
        \    lazy[node] = (lazy[node] + v) % MOD;\n}\n\nvoid update(int node, int l,\
        \ int r, int ql, int qr) {\n    if (ql <= l && r <= qr) {\n        apply(node,\
        \ l, r, 1);\n        return;\n    }\n    int mid = (l + r) >> 1;\n    if (lazy[node]\
        \ != 0) {\n        apply(node << 1, l, mid, lazy[node]);\n        apply((node\
        \ << 1) | 1, mid + 1, r, lazy[node]);\n        lazy[node] = 0;\n    }\n    if\
        \ (ql <= mid) update(node << 1, l, mid, ql, qr);\n    if (qr > mid) update((node\
        \ << 1) | 1, mid + 1, r, ql, qr);\n    sum_sq[node] = (sum_sq[node << 1] + sum_sq[(node\
        \ << 1) | 1]) % MOD;\n    sum_val[node] = (sum_val[node << 1] + sum_val[(node\
        \ << 1) | 1]) % MOD;\n}\n\nint sumCounts(int* nums, int numsSize) {\n    for\
        \ (int i = 0; i <= 4 * numsSize; i++) {\n        sum_sq[i] = 0; sum_val[i] =\
        \ 0; lazy[i] = 0;\n    }\n    for (int i = 0; i < 100001; i++) last_pos[i] =\
        \ -1;\n\n    long long ans = 0;\n    for (int i = 0; i < numsSize; i++) {\n\
        \        update(1, 0, numsSize - 1, last_pos[nums[i]] + 1, i);\n        ans\
        \ = (ans + sum_sq[1]) % MOD;\n        last_pos[nums[i]] = i;\n    }\n    return\
        \ (int)ans;\n}"
      csharp: "public class Solution {\n    private const int MOD = 1000000007;\n  \
        \  private long[] sumSq;\n    private long[] sumVal;\n    private long[] lazy;\n\
        \n    public int SumCounts(int[] nums) {\n        int n = nums.Length;\n   \
        \     sumSq = new long[4 * n + 1];\n        sumVal = new long[4 * n + 1];\n\
        \        lazy = new long[4 * n + 1];\n        int[] lastPos = new int[100001];\n\
        \        for (int i = 0; i < 100001; i++) lastPos[i] = -1;\n\n        long ans\
        \ = 0;\n        for (int i = 0; i < n; i++) {\n            Update(1, 0, n -\
        \ 1, lastPos[nums[i]] + 1, i);\n            ans = (ans + sumSq[1]) % MOD;\n\
        \            lastPos[nums[i]] = i;\n        }\n        return (int)ans;\n  \
        \  }\n\n    private void Update(int node, int l, int r, int ql, int qr) {\n\
        \        if (ql <= l && r <= qr) {\n            Apply(node, l, r, 1);\n    \
        \        return;\n        }\n        int mid = (l + r) / 2;\n        if (lazy[node]\
        \ != 0) {\n            Apply(2 * node, l, mid, lazy[node]);\n            Apply(2\
        \ * node + 1, mid + 1, r, lazy[node]);\n            lazy[node] = 0;\n      \
        \  }\n        if (ql <= mid) Update(2 * node, l, mid, ql, qr);\n        if (qr\
        \ > mid) Update(2 * node + 1, mid + 1, r, ql, qr);\n        sumSq[node] = (sumSq[2\
        \ * node] + sumSq[2 * node + 1]) % MOD;\n        sumVal[node] = (sumVal[2 *\
        \ node] + sumVal[2 * node + 1]) % MOD;\n    }\n\n    private void Apply(int\
        \ node, int l, int r, long v) {\n        long cnt = r - l + 1;\n        sumSq[node]\
        \ = (sumSq[node] + 2 * v * sumVal[node] + (v * v % MOD) * cnt) % MOD;\n    \
        \    sumVal[node] = (sumVal[node] + v * cnt) % MOD;\n        lazy[node] = (lazy[node]\
        \ + v) % MOD;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar sumCounts\
        \ = function(nums) {\n    const n = nums.length;\n    const MOD = 1000000007;\n\
        \    const sumSq = new Float64Array(4 * n + 1);\n    const sumVal = new Float64Array(4\
        \ * n + 1);\n    const lazy = new Float64Array(4 * n + 1);\n    const lastPos\
        \ = new Int32Array(100001).fill(-1);\n\n    function apply(node, l, r, v) {\n\
        \        const cnt = r - l + 1;\n        sumSq[node] = (sumSq[node] + 2 * v\
        \ * sumVal[node] + (v * v % MOD) * cnt) % MOD;\n        sumVal[node] = (sumVal[node]\
        \ + v * cnt) % MOD;\n        lazy[node] = (lazy[node] + v) % MOD;\n    }\n\n\
        \    function update(node, l, r, ql, qr) {\n        if (ql <= l && r <= qr)\
        \ {\n            apply(node, l, r, 1);\n            return;\n        }\n   \
        \     const mid = (l + r) >> 1;\n        if (lazy[node] !== 0) {\n         \
        \   apply(node << 1, l, mid, lazy[node]);\n            apply((node << 1) | 1,\
        \ mid + 1, r, lazy[node]);\n            lazy[node] = 0;\n        }\n       \
        \ if (ql <= mid) update(node << 1, l, mid, ql, qr);\n        if (qr > mid) update((node\
        \ << 1) | 1, mid + 1, r, ql, qr);\n        sumSq[node] = (sumSq[node << 1] +\
        \ sumSq[(node << 1) | 1]) % MOD;\n        sumVal[node] = (sumVal[node << 1]\
        \ + sumVal[(node << 1) | 1]) % MOD;\n    }\n\n    let ans = 0;\n    for (let\
        \ i = 0; i < n; i++) {\n        update(1, 0, n - 1, lastPos[nums[i]] + 1, i);\n\
        \        ans = (ans + sumSq[1]) % MOD;\n        lastPos[nums[i]] = i;\n    }\n\
        \    return ans;\n};"
      typescript: "function sumCounts(nums: number[]): number {\n    const n = nums.length;\n\
        \    const MOD = 1000000007;\n\n    const sum1 = new Float64Array(4 * n + 1);\n\
        \    const sum2 = new Float64Array(4 * n + 1);\n    const lazy = new Float64Array(4\
        \ * n + 1);\n\n    function apply(node: number, start: number, end: number,\
        \ v: number): void {\n        const len = end - start + 1;\n        sum2[node]\
        \ = (sum2[node] + 2 * v * sum1[node] + v * v * len) % MOD;\n        sum1[node]\
        \ = (sum1[node] + v * len) % MOD;\n        lazy[node] = (lazy[node] + v) % MOD;\n\
        \    }\n\n    function pushDown(node: number, start: number, end: number): void\
        \ {\n        if (lazy[node] !== 0) {\n            const mid = Math.floor((start\
        \ + end) / 2);\n            apply(2 * node, start, mid, lazy[node]);\n     \
        \       apply(2 * node + 1, mid + 1, end, lazy[node]);\n            lazy[node]\
        \ = 0;\n        }\n    }\n\n    function pushUp(node: number): void {\n    \
        \    sum1[node] = (sum1[2 * node] + sum1[2 * node + 1]) % MOD;\n        sum2[node]\
        \ = (sum2[2 * node] + sum2[2 * node + 1]) % MOD;\n    }\n\n    function update(node:\
        \ number, start: number, end: number, L: number, R: number, v: number): void\
        \ {\n        if (L <= start && end <= R) {\n            apply(node, start, end,\
        \ v);\n            return;\n        }\n        pushDown(node, start, end);\n\
        \        const mid = Math.floor((start + end) / 2);\n        if (L <= mid) update(2\
        \ * node, start, mid, L, R, v);\n        if (R > mid) update(2 * node + 1, mid\
        \ + 1, end, L, R, v);\n        pushUp(node);\n    }\n\n    const lastPos = new\
        \ Int32Array(100001).fill(-1);\n    let totalSumSq = 0;\n\n    for (let j =\
        \ 0; j < n; j++) {\n        const val = nums[j];\n        const prevIdx = lastPos[val];\n\
        \        update(1, 0, n - 1, prevIdx + 1, j, 1);\n        totalSumSq = (totalSumSq\
        \ + sum2[1]) % MOD;\n        lastPos[val] = j;\n    }\n\n    return totalSumSq;\n\
        }"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    private $sum1, $sum2, $lazy, $MOD = 1000000007;\n\n\
        \    function apply($node, $start, $end, $v) {\n        $len = $end - $start\
        \ + 1;\n        $this->sum2[$node] = ($this->sum2[$node] + 2 * $v * $this->sum1[$node]\
        \ + $v * $v * $len) % $this->MOD;\n        $this->sum1[$node] = ($this->sum1[$node]\
        \ + $v * $len) % $this->MOD;\n        $this->lazy[$node] = ($this->lazy[$node]\
        \ + $v) % $this->MOD;\n    }\n\n    function pushDown($node, $start, $end) {\n\
        \        if ($this->lazy[$node] != 0) {\n            $mid = (int)(($start +\
        \ $end) / 2);\n            $this->apply(2 * $node, $start, $mid, $this->lazy[$node]);\n\
        \            $this->apply(2 * $node + 1, $mid + 1, $end, $this->lazy[$node]);\n\
        \            $this->lazy[$node] = 0;\n        }\n    }\n\n    function pushUp($node)\
        \ {\n        $this->sum1[$node] = ($this->sum1[2 * $node] + $this->sum1[2 *\
        \ $node + 1]) % $this->MOD;\n        $this->sum2[$node] = ($this->sum2[2 * $node]\
        \ + $this->sum2[2 * $node + 1]) % $this->MOD;\n    }\n\n    function update($node,\
        \ $start, $end, $L, $R, $v) {\n        if ($L <= $start && $end <= $R) {\n \
        \           $this->apply($node, $start, $end, $v);\n            return;\n  \
        \      }\n        $this->pushDown($node, $start, $end);\n        $mid = (int)(($start\
        \ + $end) / 2);\n        if ($L <= $mid) {\n            $this->update(2 * $node,\
        \ $start, $mid, $L, $R, $v);\n        }\n        if ($R > $mid) {\n        \
        \    $this->update(2 * $node + 1, $mid + 1, $end, $L, $R, $v);\n        }\n\
        \        $this->pushUp($node);\n    }\n\n    function sumCounts($nums) {\n \
        \       $n = count($nums);\n        $this->sum1 = array_fill(0, 4 * $n + 1,\
        \ 0);\n        $this->sum2 = array_fill(0, 4 * $n + 1, 0);\n        $this->lazy\
        \ = array_fill(0, 4 * $n + 1, 0);\n        $lastPos = array_fill(0, 100001,\
        \ -1);\n        $totalSumSq = 0;\n\n        for ($j = 0; $j < $n; $j++) {\n\
        \            $val = $nums[$j];\n            $prevIdx = $lastPos[$val];\n   \
        \         $this->update(1, 0, $n - 1, $prevIdx + 1, $j, 1);\n            $totalSumSq\
        \ = ($totalSumSq + $this->sum2[1]) % $this->MOD;\n            $lastPos[$val]\
        \ = $j;\n        }\n\n        return $totalSumSq;\n    }\n}"
      swift: "class Solution {\n    func sumCounts(_ nums: [Int]) -> Int {\n       \
        \ let n = nums.count\n        let MOD = 1_000_000_007\n        var sum1 = [Int](repeating:\
        \ 0, count: 4 * n + 1)\n        var sum2 = [Int](repeating: 0, count: 4 * n\
        \ + 1)\n        var lazy = [Int](repeating: 0, count: 4 * n + 1)\n\n       \
        \ func apply(_ node: Int, _ start: Int, _ end: Int, _ v: Int) {\n          \
        \  let len = end - start + 1\n            sum2[node] = (sum2[node] + 2 * v *\
        \ sum1[node] + v * v * len) % MOD\n            sum1[node] = (sum1[node] + v\
        \ * len) % MOD\n            lazy[node] = (lazy[node] + v) % MOD\n        }\n\
        \n        func pushDown(_ node: Int, _ start: Int, _ end: Int) {\n         \
        \   if lazy[node] != 0 {\n                let mid = (start + end) / 2\n    \
        \            apply(2 * node, start, mid, lazy[node])\n                apply(2\
        \ * node + 1, mid + 1, end, lazy[node])\n                lazy[node] = 0\n  \
        \          }\n        }\n\n        func pushUp(_ node: Int) {\n            sum1[node]\
        \ = (sum1[2 * node] + sum1[2 * node + 1]) % MOD\n            sum2[node] = (sum2[2\
        \ * node] + sum2[2 * node + 1]) % MOD\n        }\n\n        func update(_ node:\
        \ Int, _ start: Int, _ end: Int, _ L: Int, _ R: Int, _ v: Int) {\n         \
        \   if L <= start && end <= R {\n                apply(node, start, end, v)\n\
        \                return\n            }\n            pushDown(node, start, end)\n\
        \            let mid = (start + end) / 2\n            if L <= mid {\n      \
        \          update(2 * node, start, mid, L, R, v)\n            }\n          \
        \  if R > mid {\n                update(2 * node + 1, mid + 1, end, L, R, v)\n\
        \            }\n            pushUp(node)\n        }\n\n        var lastPos =\
        \ [Int](repeating: -1, count: 100001)\n        var totalSumSq = 0\n        for\
        \ j in 0..<n {\n            let val = nums[j]\n            let prevIdx = lastPos[val]\n\
        \            update(1, 0, n - 1, prevIdx + 1, j, 1)\n            totalSumSq\
        \ = (totalSumSq + sum2[1]) % MOD\n            lastPos[val] = j\n        }\n\n\
        \        return totalSumSq\n    }\n}"
      kotlin: "class Solution {\n    fun sumCounts(nums: IntArray): Int {\n        val\
        \ n = nums.size\n        val MOD = 1000000007L\n\n        val sum1 = LongArray(4\
        \ * n + 1)\n        val sum2 = LongArray(4 * n + 1)\n        val lazy = LongArray(4\
        \ * n + 1)\n\n        fun apply(node: Int, start: Int, end: Int, v: Long) {\n\
        \            val len = (end - start + 1).toLong()\n            sum2[node] =\
        \ (sum2[node] + 2 * v * sum1[node] + v * v * len) % MOD\n            sum1[node]\
        \ = (sum1[node] + v * len) % MOD\n            lazy[node] = (lazy[node] + v)\
        \ % MOD\n        }\n\n        fun pushDown(node: Int, start: Int, end: Int)\
        \ {\n            if (lazy[node] != 0L) {\n                val mid = (start +\
        \ end) / 2\n                apply(2 * node, start, mid, lazy[node])\n      \
        \          apply(2 * node + 1, mid + 1, end, lazy[node])\n                lazy[node]\
        \ = 0\n            }\n        }\n\n        fun pushUp(node: Int) {\n       \
        \     sum1[node] = (sum1[2 * node] + sum1[2 * node + 1]) % MOD\n           \
        \ sum2[node] = (sum2[2 * node] + sum2[2 * node + 1]) % MOD\n        }\n\n  \
        \      fun update(node: Int, start: Int, end: Int, L: Int, R: Int, v: Long)\
        \ {\n            if (L <= start && end <= R) {\n                apply(node,\
        \ start, end, v)\n                return\n            }\n            pushDown(node,\
        \ start, end)\n            val mid = (start + end) / 2\n            if (L <=\
        \ mid) update(2 * node, start, mid, L, R, v)\n            if (R > mid) update(2\
        \ * node + 1, mid + 1, end, L, R, v)\n            pushUp(node)\n        }\n\n\
        \        val lastPos = IntArray(100001) { -1 }\n        var totalSumSq = 0L\n\
        \n        for (j in 0 until n) {\n            val valAtJ = nums[j]\n       \
        \     val prevIdx = lastPos[valAtJ]\n            update(1, 0, n - 1, prevIdx\
        \ + 1, j, 1L)\n            totalSumSq = (totalSumSq + sum2[1]) % MOD\n     \
        \       lastPos[valAtJ] = j\n        }\n\n        return totalSumSq.toInt()\n\
        \    }\n}"
      dart: "class Solution {\n  int sumCounts(List<int> nums) {\n    int n = nums.length;\n\
        \    int MOD = 1000000007;\n    List<int> sumSq = List<int>.filled(4 * n, 0);\n\
        \    List<int> sumVal = List<int>.filled(4 * n, 0);\n    List<int> lazyAdd =\
        \ List<int>.filled(4 * n, 0);\n\n    void apply(int v, int tl, int tr, int add)\
        \ {\n      int num = tr - tl + 1;\n      int term1 = (2 * add * sumVal[v]) %\
        \ MOD;\n      int term2 = (((add * add) % MOD) * num) % MOD;\n      sumSq[v]\
        \ = (sumSq[v] + term1 + term2) % MOD;\n      sumVal[v] = (sumVal[v] + (add *\
        \ num)) % MOD;\n      lazyAdd[v] = (lazyAdd[v] + add) % MOD;\n    }\n\n    void\
        \ push(int v, int tl, int tr) {\n      if (lazyAdd[v] != 0) {\n        int tm\
        \ = (tl + tr) ~/ 2;\n        apply(2 * v, tl, tm, lazyAdd[v]);\n        apply(2\
        \ * v + 1, tm + 1, tr, lazyAdd[v]);\n        lazyAdd[v] = 0;\n      }\n    }\n\
        \n    void update(int v, int tl, int tr, int l, int r, int add) {\n      if\
        \ (l > r) return;\n      if (l == tl && r == tr) {\n        apply(v, tl, tr,\
        \ add);\n      } else {\n        push(v, tl, tr);\n        int tm = (tl + tr)\
        \ ~/ 2;\n        if (r <= tm) {\n          update(2 * v, tl, tm, l, r, add);\n\
        \        } else if (l > tm) {\n          update(2 * v + 1, tm + 1, tr, l, r,\
        \ add);\n        } else {\n          update(2 * v, tl, tm, l, tm, add);\n  \
        \        update(2 * v + 1, tm + 1, tr, tm + 1, r, add);\n        }\n       \
        \ sumSq[v] = (sumSq[2 * v] + sumSq[2 * v + 1]) % MOD;\n        sumVal[v] = (sumVal[2\
        \ * v] + sumVal[2 * v + 1]) % MOD;\n      }\n    }\n\n    int totalAns = 0;\n\
        \    List<int> lastPos = List<int>.filled(100001, -1);\n    for (int j = 0;\
        \ j < n; j++) {\n      int prev = lastPos[nums[j]];\n      update(1, 0, n -\
        \ 1, prev + 1, j, 1);\n      totalAns = (totalAns + sumSq[1]) % MOD;\n     \
        \ lastPos[nums[j]] = j;\n    }\n    return totalAns;\n  }\n}"
      go: "func sumCounts(nums []int) int {\n\tn := len(nums)\n\tMOD := int64(1000000007)\n\
        \tsumSq := make([]int64, 4*n)\n\tsumVal := make([]int64, 4*n)\n\tlazyAdd :=\
        \ make([]int64, 4*n)\n\n\tvar apply func(v, tl, tr int, add int64)\n\tapply\
        \ = func(v, tl, tr int, add int64) {\n\t\tnum := int64(tr - tl + 1)\n\t\tterm1\
        \ := (2 * add * sumVal[v]) % MOD\n\t\tterm2 := (add * add % MOD * num) % MOD\n\
        \t\tsumSq[v] = (sumSq[v] + term1 + term2) % MOD\n\t\tsumVal[v] = (sumVal[v]\
        \ + add*num) % MOD\n\t\tlazyAdd[v] = (lazyAdd[v] + add) % MOD\n\t}\n\n\tvar\
        \ push func(v, tl, tr int)\n\tpush = func(v, tl, tr int) {\n\t\tif lazyAdd[v]\
        \ != 0 {\n\t\t\ttm := (tl + tr) / 2\n\t\t\tapply(2*v, tl, tm, lazyAdd[v])\n\t\
        \t\tapply(2*v+1, tm+1, tr, lazyAdd[v])\n\t\t\tlazyAdd[v] = 0\n\t\t}\n\t}\n\n\
        \tvar update func(v, tl, tr, l, r int, add int64)\n\tupdate = func(v, tl, tr,\
        \ l, r int, add int64) {\n\t\tif l > r {\n\t\t\treturn\n\t\t}\n\t\tif l == tl\
        \ && r == tr {\n\t\t\tapply(v, tl, tr, add)\n\t\t} else {\n\t\t\tpush(v, tl,\
        \ tr)\n\t\t\ttm := (tl + tr) / 2\n\t\t\tif r <= tm {\n\t\t\t\tupdate(2*v, tl,\
        \ tm, l, r, add)\n\t\t\t} else if l > tm {\n\t\t\t\tupdate(2*v+1, tm+1, tr,\
        \ l, r, add)\n\t\t\t} else {\n\t\t\t\tupdate(2*v, tl, tm, l, tm, add)\n\t\t\t\
        \tupdate(2*v+1, tm+1, tr, tm+1, r, add)\n\t\t\t}\n\t\t\tsumSq[v] = (sumSq[2*v]\
        \ + sumSq[2*v+1]) % MOD\n\t\t\tsumVal[v] = (sumVal[2*v] + sumVal[2*v+1]) % MOD\n\
        \t\t}\n\t}\n\n\ttotalAns := int64(0)\n\tlastPos := make([]int, 100001)\n\tfor\
        \ i := range lastPos {\n\t\tlastPos[i] = -1\n\t}\n\tfor j := 0; j < n; j++ {\n\
        \t\tprev := lastPos[nums[j]]\n\t\tupdate(1, 0, n-1, prev+1, j, 1)\n\t\ttotalAns\
        \ = (totalAns + sumSq[1]) % MOD\n\t\tlastPos[nums[j]] = j\n\t}\n\n\treturn int(totalAns)\n\
        }"
      ruby: "class SegmentTree\n  def initialize(n)\n    @n = n\n    @sum_sq = Array.new(4\
        \ * n, 0)\n    @sum_val = Array.new(4 * n, 0)\n    @lazy = Array.new(4 * n,\
        \ 0)\n    @mod = 1_000_000_007\n  end\n\n  def apply(v, tl, tr, add)\n    num\
        \ = tr - tl + 1\n    term1 = (2 * add * @sum_val[v]) % @mod\n    term2 = (add\
        \ * add % @mod * num) % @mod\n    @sum_sq[v] = (@sum_sq[v] + term1 + term2)\
        \ % @mod\n    @sum_val[v] = (@sum_val[v] + add * num) % @mod\n    @lazy[v] =\
        \ (@lazy[v] + add) % @mod\n  end\n\n  def push(v, tl, tr)\n    if @lazy[v] !=\
        \ 0\n      tm = (tl + tr) / 2\n      apply(2 * v, tl, tm, @lazy[v])\n      apply(2\
        \ * v + 1, tm + 1, tr, @lazy[v])\n      @lazy[v] = 0\n    end\n  end\n\n  def\
        \ update(v, tl, tr, l, r, add)\n    return if l > r\n    if l == tl && r ==\
        \ tr\n      apply(v, tl, tr, add)\n      return\n    end\n    push(v, tl, tr)\n\
        \    tm = (tl + tr) / 2\n    if r <= tm\n      update(2 * v, tl, tm, l, r, add)\n\
        \    elsif l > tm\n      update(2 * v + 1, tm + 1, tr, l, r, add)\n    else\n\
        \      update(2 * v, tl, tm, l, tm, add)\n      update(2 * v + 1, tm + 1, tr,\
        \ tm + 1, r, add)\n    end\n    @sum_sq[v] = (@sum_sq[2 * v] + @sum_sq[2 * v\
        \ + 1]) % @mod\n    @sum_val[v] = (@sum_val[2 * v] + @sum_val[2 * v + 1]) %\
        \ @mod\n  end\n\n  def total_sum_sq\n    @sum_sq[1]\n  end\nend\n\n# @param\
        \ {Integer[]} nums\n# @return {Integer}\ndef sum_counts(nums)\n  n = nums.length\n\
        \  st = SegmentTree.new(n)\n  last_pos = Array.new(100001, -1)\n  total_ans\
        \ = 0\n  mod = 1_000_000_007\n\n  nums.each_with_index do |num, j|\n    prev\
        \ = last_pos[num]\n    st.update(1, 0, n - 1, prev + 1, j, 1)\n    total_ans\
        \ = (total_ans + st.total_sum_sq) % mod\n    last_pos[num] = j\n  end\n\n  total_ans\n\
        end"
      scala: "object Solution {\n  def sumCounts(nums: Array[Int]): Int = {\n    val\
        \ n = nums.length\n    val sumSq = new Array[Long](4 * n)\n    val sumVal =\
        \ new Array[Long](4 * n)\n    val lazyAdd = new Array[Long](4 * n)\n    val\
        \ MOD = 1000000007L\n\n    def apply(v: Int, tl: Int, tr: Int, add: Long): Unit\
        \ = {\n      val num = (tr - tl + 1).toLong\n      val term1 = (2 * add * sumVal(v))\
        \ % MOD\n      val term2 = (add * add % MOD * num) % MOD\n      sumSq(v) = (sumSq(v)\
        \ + term1 + term2) % MOD\n      sumVal(v) = (sumVal(v) + add * num) % MOD\n\
        \      lazyAdd(v) = (lazyAdd(v) + add) % MOD\n    }\n\n    def push(v: Int,\
        \ tl: Int, tr: Int): Unit = {\n      if (lazyAdd(v) != 0) {\n        val tm\
        \ = (tl + tr) / 2\n        apply(2 * v, tl, tm, lazyAdd(v))\n        apply(2\
        \ * v + 1, tm + 1, tr, lazyAdd(v))\n        lazyAdd(v) = 0\n      }\n    }\n\
        \n    def update(v: Int, tl: Int, tr: Int, l: Int, r: Int, add: Long): Unit\
        \ = {\n      if (l > r) return\n      if (l == tl && r == tr) {\n        apply(v,\
        \ tl, tr, add)\n      } else {\n        push(v, tl, tr)\n        val tm = (tl\
        \ + tr) / 2\n        if (r <= tm) update(2 * v, tl, tm, l, r, add)\n       \
        \ else if (l > tm) update(2 * v + 1, tm + 1, tr, l, r, add)\n        else {\n\
        \          update(2 * v, tl, tm, l, tm, add)\n          update(2 * v + 1, tm\
        \ + 1, tr, tm + 1, r, add)\n        }\n        sumSq(v) = (sumSq(2 * v) + sumSq(2\
        \ * v + 1)) % MOD\n        sumVal(v) = (sumVal(2 * v) + sumVal(2 * v + 1)) %\
        \ MOD\n      }\n    }\n\n    var totalAns = 0L\n    val lastPos = Array.fill(100001)(-1)\n\
        \    var j = 0\n    while (j < n) {\n      val num = nums(j)\n      val prev\
        \ = lastPos(num)\n      update(1, 0, n - 1, prev + 1, j, 1L)\n      totalAns\
        \ = (totalAns + sumSq(1)) % MOD\n      lastPos(num) = j\n      j += 1\n    }\n\
        \    totalAns.toInt\n  }\n}"
      rust: "impl Solution {\n    pub fn sum_counts(nums: Vec<i32>) -> i32 {\n     \
        \   let n = nums.len();\n        let mut sum = vec![0i64; 4 * n + 1];\n    \
        \    let mut sq_sum = vec![0i64; 4 * n + 1];\n        let mut lazy = vec![0i64;\
        \ 4 * n + 1];\n        let mut last_pos = vec![-1i32; 100001];\n        let\
        \ mut total_ans = 0i64;\n        let mod_val = 1_000_000_007i64;\n\n       \
        \ fn apply_lazy(idx: usize, l: usize, r: usize, v: i64, sum: &mut [i64], sq_sum:\
        \ &mut [i64], lazy: &mut [i64], mod_val: i64) {\n            let len = (r -\
        \ l + 1) as i64;\n            sq_sum[idx] = (sq_sum[idx] + 2 * v * sum[idx]\
        \ + v * v % mod_val * len) % mod_val;\n            sum[idx] = (sum[idx] + v\
        \ * len) % mod_val;\n            lazy[idx] = (lazy[idx] + v) % mod_val;\n  \
        \      }\n\n        fn push_down(idx: usize, l: usize, mid: usize, r: usize,\
        \ sum: &mut [i64], sq_sum: &mut [i64], lazy: &mut [i64], mod_val: i64) {\n \
        \           if lazy[idx] != 0 {\n                let v = lazy[idx];\n      \
        \          apply_lazy(2 * idx, l, mid, v, sum, sq_sum, lazy, mod_val);\n   \
        \             apply_lazy(2 * idx + 1, mid + 1, r, v, sum, sq_sum, lazy, mod_val);\n\
        \                lazy[idx] = 0;\n            }\n        }\n\n        fn update(idx:\
        \ usize, l: usize, r: usize, ql: usize, qr: usize, v: i64, sum: &mut [i64],\
        \ sq_sum: &mut [i64], lazy: &mut [i64], mod_val: i64) {\n            if ql <=\
        \ l && r <= qr {\n                apply_lazy(idx, l, r, v, sum, sq_sum, lazy,\
        \ mod_val);\n                return;\n            }\n            let mid = (l\
        \ + r) / 2;\n            push_down(idx, l, mid, r, sum, sq_sum, lazy, mod_val);\n\
        \            if ql <= mid {\n                update(2 * idx, l, mid, ql, qr,\
        \ v, sum, sq_sum, lazy, mod_val);\n            }\n            if qr > mid {\n\
        \                update(2 * idx + 1, mid + 1, r, ql, qr, v, sum, sq_sum, lazy,\
        \ mod_val);\n            }\n            sum[idx] = (sum[2 * idx] + sum[2 * idx\
        \ + 1]) % mod_val;\n            sq_sum[idx] = (sq_sum[2 * idx] + sq_sum[2 *\
        \ idx + 1]) % mod_val;\n        }\n\n        for i in 0..n {\n            let\
        \ p = last_pos[nums[i] as usize];\n            update(1, 0, n - 1, (p + 1) as\
        \ usize, i, 1, &mut sum, &mut sq_sum, &mut lazy, mod_val);\n            total_ans\
        \ = (total_ans + sq_sum[1]) % mod_val;\n            last_pos[nums[i] as usize]\
        \ = i as i32;\n        }\n        total_ans as i32\n    }\n}"
      racket: "(define/contract (sum-counts nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([n (length nums)]\n         [MOD 1000000007]\n         [sum (make-vector\
        \ (+ (* 4 n) 1) 0)]\n         [sq-sum (make-vector (+ (* 4 n) 1) 0)]\n     \
        \    [lazy (make-vector (+ (* 4 n) 1) 0)]\n         [last-pos (make-vector 100001\
        \ -1)]\n         [nums-vec (list->vector nums)])\n\n    (define (apply-lazy-node\
        \ idx l r v)\n      (let ([len (+ (- r l) 1)])\n        (vector-set! sq-sum\
        \ idx (modulo (+ (vector-ref sq-sum idx)\n                                 \
        \          (* 2 v (vector-ref sum idx))\n                                  \
        \         (* v v len)) MOD))\n        (vector-set! sum idx (modulo (+ (vector-ref\
        \ sum idx) (* v len)) MOD))\n        (vector-set! lazy idx (modulo (+ (vector-ref\
        \ lazy idx) v) MOD))))\n\n    (define (push-down idx l mid r)\n      (let ([lz\
        \ (vector-ref lazy idx)])\n        (when (and (not (zero? lz)) (< l r))\n  \
        \        (apply-lazy-node (* 2 idx) l mid lz)\n          (apply-lazy-node (+\
        \ (* 2 idx) 1) (+ mid 1) r lz)\n          (vector-set! lazy idx 0))))\n\n  \
        \  (define (update idx l r ql qr v)\n      (if (and (<= ql l) (<= r qr))\n \
        \         (apply-lazy-node idx l r v)\n          (let* ([mid (quotient (+ l\
        \ r) 2)])\n            (push-down idx l mid r)\n            (when (<= ql mid)\n\
        \              (update (* 2 idx) l mid ql qr v))\n            (when (> qr mid)\n\
        \              (update (+ (* 2 idx) 1) (+ mid 1) r ql qr v))\n            (vector-set!\
        \ sum idx (modulo (+ (vector-ref sum (* 2 idx)) (vector-ref sum (+ (* 2 idx)\
        \ 1))) MOD))\n            (vector-set! sq-sum idx (modulo (+ (vector-ref sq-sum\
        \ (* 2 idx)) (vector-ref sq-sum (+ (* 2 idx) 1))) MOD)))))\n\n    (let loop\
        \ ([i 0] [total-ans 0])\n      (if (< i n)\n          (let* ([val (vector-ref\
        \ nums-vec i)]\n                 [p (vector-ref last-pos val)])\n          \
        \  (update 1 0 (- n 1) (+ p 1) i 1)\n            (vector-set! last-pos val i)\n\
        \            (loop (+ i 1) (modulo (+ total-ans (vector-ref sq-sum 1)) MOD)))\n\
        \          total-ans))))"
      erlang: "-spec sum_counts(Nums :: [integer()]) -> integer().\nsum_counts(Nums)\
        \ ->\n    N = length(Nums),\n    Mod = 1000000007,\n    InitialTree = build(0,\
        \ N - 1),\n    {TotalAns, _, _, _} = lists:foldl(fun(X, {Acc, T, LP, I}) ->\n\
        \        P = maps:get(X, LP, -1),\n        NewT = update(T, 0, N - 1, P + 1,\
        \ I, 1),\n        {{SqSum, _, _}, _, _} = NewT,\n        NewAcc = (Acc + SqSum)\
        \ rem Mod,\n        {NewAcc, NewT, maps:put(X, I, LP), I + 1}\n    end, {0,\
        \ InitialTree, #{}, 0}, Nums),\n    TotalAns.\n\nbuild(L, R) ->\n    if L =:=\
        \ R -> {{0, 0, 0}, nil, nil};\n    true ->\n        Mid = (L + R) div 2,\n \
        \       {{0, 0, 0}, build(L, Mid), build(Mid + 1, R)}\n    end.\n\nupdate({{SqSum,\
        \ Sum, Lazy}, Left, Right}, L, R, QL, QR, V) ->\n    if (QL =< L) and (R =<\
        \ QR) ->\n        apply_lazy({{SqSum, Sum, Lazy}, Left, Right}, L, R, V);\n\
        \    true ->\n        Mid = (L + R) div 2,\n        {L1, R1} = push({{SqSum,\
        \ Sum, Lazy}, Left, Right}, L, Mid, R),\n        {L2, R2} = if\n           \
        \ QR =< Mid -> {update(L1, L, Mid, QL, QR, V), R1};\n            QL > Mid ->\
        \ {L1, update(R1, Mid + 1, R, QL, QR, V)};\n            true -> {update(L1,\
        \ L, Mid, QL, Mid, V), update(R1, Mid + 1, R, Mid + 1, QR, V)}\n        end,\n\
        \        {{SqSumL, SumL, _}, _, _} = L2,\n        {{SqSumR, SumR, _}, _, _}\
        \ = R2,\n        {{(SqSumL + SqSumR) rem 1000000007, (SumL + SumR) rem 1000000007,\
        \ 0}, L2, R2}\n    end.\n\npush({{_, _, 0}, Left, Right}, _, _, _) -> {Left,\
        \ Right};\npush({{_, _, Lazy}, Left, Right}, L, Mid, R) ->\n    {apply_lazy(Left,\
        \ L, Mid, Lazy), apply_lazy(Right, Mid + 1, R, Lazy)}.\n\napply_lazy({{SqSum,\
        \ Sum, Lazy}, Left, Right}, L, R, V) ->\n    Len = R - L + 1,\n    Mod = 1000000007,\n\
        \    NewSqSum = (SqSum + 2 * V * Sum + V * V * Len) rem Mod,\n    NewSum = (Sum\
        \ + V * Len) rem Mod,\n    NewLazy = (Lazy + V) rem Mod,\n    {{NewSqSum, NewSum,\
        \ NewLazy}, Left, Right}."
      elixir: "defmodule Solution do\n  @mod_val 1_000_000_007\n\n  @spec sum_counts(nums\
        \ :: [integer]) :: integer\n  def sum_counts(nums) do\n    n = length(nums)\n\
        \    tree = build(0, n - 1)\n    {total_ans, _, _, _} = Enum.reduce(nums, {0,\
        \ tree, %{}, 0}, fn x, {acc, t, lp, i} ->\n      p = Map.get(lp, x, -1)\n  \
        \    new_t = update(t, 0, n - 1, p + 1, i, 1)\n      {{sq_sum, _sum, _lazy},\
        \ _left, _right} = new_t\n      new_acc = rem(acc + sq_sum, @mod_val)\n    \
        \  {new_acc, new_t, Map.put(lp, x, i), i + 1}\n    end)\n    total_ans\n  end\n\
        \n  defp build(l, r) do\n    if l == r do\n      {{0, 0, 0}, nil, nil}\n   \
        \ else\n      mid = div(l + r, 2)\n      {{0, 0, 0}, build(l, mid), build(mid\
        \ + 1, r)}\n    end\n  end\n\n  defp update({{sq_sum, sum, lazy}, left, right},\
        \ l, r, ql, qr, v) do\n    if ql <= l and r <= qr do\n      apply_lazy({{sq_sum,\
        \ sum, lazy}, left, right}, l, r, v)\n    else\n      mid = div(l + r, 2)\n\
        \      {left, right} = push({{sq_sum, sum, lazy}, left, right}, l, mid, r)\n\
        \n      {new_left, new_right} = cond do\n        qr <= mid -> {update(left,\
        \ l, mid, ql, qr, v), right}\n        ql > mid -> {left, update(right, mid +\
        \ 1, r, ql, qr, v)}\n        true -> {update(left, l, mid, ql, mid, v), update(right,\
        \ mid + 1, r, mid + 1, qr, v)}\n      end\n\n      {{l_sq, l_s, _}, _, _} =\
        \ new_left\n      {{r_sq, r_s, _}, _, _} = new_right\n      {{rem(l_sq + r_sq,\
        \ @mod_val), rem(l_s + r_s, @mod_val), 0}, new_left, new_right}\n    end\n \
        \ end\n\n  defp push({{_sq, _s, 0}, left, right}, _l, _mid, _r), do: {left,\
        \ right}\n  defp push({{_sq, _s, lazy}, left, right}, l, mid, r) do\n    {apply_lazy(left,\
        \ l, mid, lazy), apply_lazy(right, mid + 1, r, lazy)}\n  end\n\n  defp apply_lazy({{sq_sum,\
        \ sum, l_lazy}, left, right}, l, r, v) do\n    len = r - l + 1\n    new_sq_sum\
        \ = rem(sq_sum + 2 * v * sum + v * v * len, @mod_val)\n    new_sum = rem(sum\
        \ + v * len, @mod_val)\n    new_lazy = rem(l_lazy + v, @mod_val)\n    {{new_sq_sum,\
        \ new_sum, new_lazy}, left, right}\n  end\nend"
    approach: 'We can compute the sum of squares of distinct counts for all subarrays
      by iterating through the array and updating the contribution of each element to
      the total sum. Let $f(i, j)$ be the number of distinct elements in the subarray
      $nums[i..j]$. We want to compute $\sum_{j=0}^{n-1} \sum_{i=0}^{j} (f(i, j))^2$.
      As we move from index $j$ to $j+1$, the distinct count $f(i, j+1)$ increases by
      1 for all $i \in (\text{prev\_pos}[nums[j+1]], j+1]$, where $\text{prev\_pos}[x]$
      is the last index before $j+1$ where $x$ appeared. For $i \le \text{prev\_pos}[nums[j+1]]$,
      the distinct count remains the same because the current element $nums[j+1]$ was
      already present in those subarrays.


      To efficiently update and query the sum of squares, we use a Segment Tree with
      lazy propagation. The tree maintains two values for each node: $\sum f(i, j)$
      (denoted as $s_1$) and $\sum (f(i, j))^2$ (denoted as $s_2$). When we perform
      a range increment of $v$ on $f(i, j)$, the new sum of squares is $\sum (f(i, j)
      + v)^2 = \sum (f(i, j)^2 + 2v f(i, j) + v^2) = s_2 + 2v s_1 + \text{len} \cdot
      v^2$. This relationship allows us to update both $s_1$ and $s_2$ in $O(\log n)$
      time. The total complexity is $O(n \log n)$, making it optimal for $n = 10^5$.'
    time_complexity: O(N log N), where N is the length of the array. The algorithm iterates
      through the array once (N iterations), and for each element, it performs a range
      update on the Segment Tree, which takes O(log N) time.
    space_complexity: O(N), as we store the Segment Tree arrays (size 4N) and an array
      to track the last seen positions of each element (size 10^5).
    elapsed_time: 631.7724452018738
    model: gemini-3-flash-preview
    generated_at: '2026-10-16 02:41:54 '
---

## Problem #2916: Subarrays Distinct Element Sum of Squares II

**Difficulty:** Hard

**Topics:** Array, Hash Table, Binary Indexed Tree, Segment Tree

## Problem Description

<p>You are given a <strong>0-indexed </strong>integer array <code>nums</code>.</p>

<p>The <strong>distinct count</strong> of a subarray of <code>nums</code> is defined as:</p>

<ul>
	<li>Let <code>nums[i..j]</code> be a subarray of <code>nums</code> consisting of all the indices from <code>i</code> to <code>j</code> such that <code>0 &lt;= i &lt;= j &lt; nums.length</code>. Then the number of distinct values in <code>nums[i..j]</code> is called the distinct count of <code>nums[i..j]</code>.</li>
</ul>

<p>Return <em>the sum of the <strong>squares</strong> of <strong>distinct counts</strong> of all subarrays of </em><code>nums</code>.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> 15
<strong>Explanation:</strong> Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> = 15.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> = 3.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Consider the sum of the count of distinct values of subarrays ending with index `i`, let’s call it `sum`. Now if you need the sum of all subarrays ending with index `i + 1` think how it can be related to `sum` and what extra will be needed to add to this.

2. You can find that extra sum using the segment tree.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

We can compute the sum of squares of distinct counts for all subarrays by iterating through the array and updating the contribution of each element to the total sum. Let $f(i, j)$ be the number of distinct elements in the subarray $nums[i..j]$. We want to compute $\sum_{j=0}^{n-1} \sum_{i=0}^{j} (f(i, j))^2$. As we move from index $j$ to $j+1$, the distinct count $f(i, j+1)$ increases by 1 for all $i \in (\text{prev\_pos}[nums[j+1]], j+1]$, where $\text{prev\_pos}[x]$ is the last index before $j+1$ where $x$ appeared. For $i \le \text{prev\_pos}[nums[j+1]]$, the distinct count remains the same because the current element $nums[j+1]$ was already present in those subarrays.

To efficiently update and query the sum of squares, we use a Segment Tree with lazy propagation. The tree maintains two values for each node: $\sum f(i, j)$ (denoted as $s_1$) and $\sum (f(i, j))^2$ (denoted as $s_2$). When we perform a range increment of $v$ on $f(i, j)$, the new sum of squares is $\sum (f(i, j) + v)^2 = \sum (f(i, j)^2 + 2v f(i, j) + v^2) = s_2 + 2v s_1 + \text{len} \cdot v^2$. This relationship allows us to update both $s_1$ and $s_2$ in $O(\log n)$ time. The total complexity is $O(n \log n)$, making it optimal for $n = 10^5$.

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
    long long MOD = 1e9 + 7;
    vector<long long> s1, s2, lazy;

    void apply(int idx, int l, int r, long long v) {
        long long ln = r - l + 1;
        s2[idx] = (s2[idx] + 2 * v * s1[idx] + (v * v % MOD * ln % MOD)) % MOD;
        s1[idx] = (s1[idx] + v * ln) % MOD;
        lazy[idx] = (lazy[idx] + v) % MOD;
    }

    void pushDown(int idx, int l, int r) {
        if (lazy[idx] != 0) {
            int mid = (l + r) / 2;
            apply(2 * idx, l, mid, lazy[idx]);
            apply(2 * idx + 1, mid + 1, r, lazy[idx]);
            lazy[idx] = 0;
        }
    }

    void update(int idx, int l, int r, int ql, int qr, int v) {
        if (ql <= l && r <= qr) {
            apply(idx, l, r, v);
            return;
        }
        pushDown(idx, l, r);
        int mid = (l + r) / 2;
        if (ql <= mid) update(2 * idx, l, mid, ql, qr, v);
        if (qr > mid) update(2 * idx + 1, mid + 1, r, ql, qr, v);
        s1[idx] = (s1[2 * idx] + s1[2 * idx + 1]) % MOD;
        s2[idx] = (s2[2 * idx] + s2[2 * idx + 1]) % MOD;
    }

public:
    int sumCounts(vector<int>& nums) {
        int n = nums.size();
        s1.assign(4 * n, 0);
        s2.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
        vector<int> last_pos(100001, -1);
        long long total_ans = 0;

        for (int i = 0; i < n; ++i) {
            int prev = last_pos[nums[i]];
            update(1, 0, n - 1, prev + 1, i, 1);
            total_ans = (total_ans + s2[1]) % MOD;
            last_pos[nums[i]] = i;
        }

        return (int)total_ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    private static final int MOD = 1000000007;
    private long[] s1, s2, lazy;

    private void apply(int idx, int l, int r, long v) {
        long ln = r - l + 1;
        s2[idx] = (s2[idx] + 2 * v * s1[idx] + (v * v % MOD) * ln) % MOD;
        s1[idx] = (s1[idx] + v * ln) % MOD;
        lazy[idx] = (lazy[idx] + v) % MOD;
    }

    private void pushDown(int idx, int l, int r) {
        if (lazy[idx] != 0) {
            int mid = l + (r - l) / 2;
            apply(2 * idx, l, mid, lazy[idx]);
            apply(2 * idx + 1, mid + 1, r, lazy[idx]);
            lazy[idx] = 0;
        }
    }

    private void update(int idx, int l, int r, int ql, int qr, int v) {
        if (ql <= l && r <= qr) {
            apply(idx, l, r, v);
            return;
        }
        pushDown(idx, l, r);
        int mid = l + (r - l) / 2;
        if (ql <= mid) update(2 * idx, l, mid, ql, qr, v);
        if (qr > mid) update(2 * idx + 1, mid + 1, r, ql, qr, v);
        s1[idx] = (s1[2 * idx] + s1[2 * idx + 1]) % MOD;
        s2[idx] = (s2[2 * idx] + s2[2 * idx + 1]) % MOD;
    }

    public int sumCounts(int[] nums) {
        int n = nums.length;
        s1 = new long[4 * n];
        s2 = new long[4 * n];
        lazy = new long[4 * n];
        int[] lastPos = new int[100001];
        java.util.Arrays.fill(lastPos, -1);
        long totalAns = 0;

        for (int i = 0; i < n; i++) {
            int prev = lastPos[nums[i]];
            update(1, 0, n - 1, prev + 1, i, 1);
            totalAns = (totalAns + s2[1]) % MOD;
            lastPos[nums[i]] = i;
        }

        return (int) totalAns;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import sys

sys.setrecursionlimit(200000)

class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        MOD = 10**9 + 7
        s1 = [0] * (4 * n)
        s2 = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(idx, l, r, ql, qr):
            if ql <= l and r <= qr:
                ln = r - l + 1
                s2[idx] = (s2[idx] + (s1[idx] << 1) + ln) % MOD
                s1[idx] = (s1[idx] + ln) % MOD
                lazy[idx] = (lazy[idx] + 1) % MOD
                return

            mid = (l + r) >> 1
            lz = lazy[idx]
            if lz:
                left, right = idx << 1, (idx << 1) | 1
                ln_l = mid - l + 1
                ln_r = r - mid
                lz_sq_l = (lz * lz * ln_l) % MOD
                lz_sq_r = (lz * lz * ln_r) % MOD
                s2[left] = (s2[left] + (lz << 1) * s1[left] + lz_sq_l) % MOD
                s1[left] = (s1[left] + lz * ln_l) % MOD
                lazy[left] = (lazy[left] + lz) % MOD
                s2[right] = (s2[right] + (lz << 1) * s1[right] + lz_sq_r) % MOD
                s1[right] = (s1[right] + lz * ln_r) % MOD
                lazy[right] = (lazy[right] + lz) % MOD
                lazy[idx] = 0

            if ql <= mid:
                update(idx << 1, l, mid, ql, qr)
            if qr > mid:
                update((idx << 1) | 1, mid + 1, r, ql, qr)

            left, right = idx << 1, (idx << 1) | 1
            s1[idx] = (s1[left] + s1[right]) % MOD
            s2[idx] = (s2[left] + s2[right]) % MOD

        ans = 0
        last_pos = [-1] * 100001
        for i, val in enumerate(nums):
            prev = last_pos[val]
            update(1, 0, n - 1, prev + 1, i)
            ans = (ans + s2[1]) % MOD
            last_pos[val] = i

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import sys

sys.setrecursionlimit(200000)

class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 1000000007
        sum_sq = [0] * (4 * n + 1)
        sum_val = [0] * (4 * n + 1)
        lazy = [0] * (4 * n + 1)

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                cnt = r - l + 1
                sum_sq[node] = (sum_sq[node] + (sum_val[node] << 1) + cnt) % MOD
                sum_val[node] = (sum_val[node] + cnt) % MOD
                lazy[node] += 1
                return

            mid = (l + r) >> 1
            lz = lazy[node]
            lc = node << 1
            rc = lc | 1
            if lz:
                cl, cr = mid - l + 1, r - mid
                lz_sq_mod = (lz * lz) % MOD
                sum_sq[lc] = (sum_sq[lc] + 2 * lz * sum_val[lc] + lz_sq_mod * cl) % MOD
                sum_val[lc] = (sum_val[lc] + lz * cl) % MOD
                lazy[lc] += lz
                sum_sq[rc] = (sum_sq[rc] + 2 * lz * sum_val[rc] + lz_sq_mod * cr) % MOD
                sum_val[rc] = (sum_val[rc] + lz * cr) % MOD
                lazy[rc] += lz
                lazy[node] = 0

            if ql <= mid:
                update(lc, l, mid, ql, qr)
            if qr > mid:
                update(rc, mid + 1, r, ql, qr)

            sum_sq[node] = (sum_sq[lc] + sum_sq[rc]) % MOD
            sum_val[node] = (sum_val[lc] + sum_val[rc]) % MOD

        ans = 0
        last_pos = [-1] * 100001
        for i, x in enumerate(nums):
            update(1, 0, n - 1, last_pos[x] + 1, i)
            ans = (ans + sum_sq[1]) % MOD
            last_pos[x] = i
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>

#define MOD 1000000007

long long sum_sq[400005];
long long sum_val[400005];
long long lazy[400005];
int last_pos[100001];

void apply(int node, int l, int r, long long v) {
    long long cnt = r - l + 1;
    sum_sq[node] = (sum_sq[node] + 2 * v * sum_val[node] + (v * v % MOD) * cnt) % MOD;
    sum_val[node] = (sum_val[node] + v * cnt) % MOD;
    lazy[node] = (lazy[node] + v) % MOD;
}

void update(int node, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) {
        apply(node, l, r, 1);
        return;
    }
    int mid = (l + r) >> 1;
    if (lazy[node] != 0) {
        apply(node << 1, l, mid, lazy[node]);
        apply((node << 1) | 1, mid + 1, r, lazy[node]);
        lazy[node] = 0;
    }
    if (ql <= mid) update(node << 1, l, mid, ql, qr);
    if (qr > mid) update((node << 1) | 1, mid + 1, r, ql, qr);
    sum_sq[node] = (sum_sq[node << 1] + sum_sq[(node << 1) | 1]) % MOD;
    sum_val[node] = (sum_val[node << 1] + sum_val[(node << 1) | 1]) % MOD;
}

int sumCounts(int* nums, int numsSize) {
    for (int i = 0; i <= 4 * numsSize; i++) {
        sum_sq[i] = 0; sum_val[i] = 0; lazy[i] = 0;
    }
    for (int i = 0; i < 100001; i++) last_pos[i] = -1;

    long long ans = 0;
    for (int i = 0; i < numsSize; i++) {
        update(1, 0, numsSize - 1, last_pos[nums[i]] + 1, i);
        ans = (ans + sum_sq[1]) % MOD;
        last_pos[nums[i]] = i;
    }
    return (int)ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    private const int MOD = 1000000007;
    private long[] sumSq;
    private long[] sumVal;
    private long[] lazy;

    public int SumCounts(int[] nums) {
        int n = nums.Length;
        sumSq = new long[4 * n + 1];
        sumVal = new long[4 * n + 1];
        lazy = new long[4 * n + 1];
        int[] lastPos = new int[100001];
        for (int i = 0; i < 100001; i++) lastPos[i] = -1;

        long ans = 0;
        for (int i = 0; i < n; i++) {
            Update(1, 0, n - 1, lastPos[nums[i]] + 1, i);
            ans = (ans + sumSq[1]) % MOD;
            lastPos[nums[i]] = i;
        }
        return (int)ans;
    }

    private void Update(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) {
            Apply(node, l, r, 1);
            return;
        }
        int mid = (l + r) / 2;
        if (lazy[node] != 0) {
            Apply(2 * node, l, mid, lazy[node]);
            Apply(2 * node + 1, mid + 1, r, lazy[node]);
            lazy[node] = 0;
        }
        if (ql <= mid) Update(2 * node, l, mid, ql, qr);
        if (qr > mid) Update(2 * node + 1, mid + 1, r, ql, qr);
        sumSq[node] = (sumSq[2 * node] + sumSq[2 * node + 1]) % MOD;
        sumVal[node] = (sumVal[2 * node] + sumVal[2 * node + 1]) % MOD;
    }

    private void Apply(int node, int l, int r, long v) {
        long cnt = r - l + 1;
        sumSq[node] = (sumSq[node] + 2 * v * sumVal[node] + (v * v % MOD) * cnt) % MOD;
        sumVal[node] = (sumVal[node] + v * cnt) % MOD;
        lazy[node] = (lazy[node] + v) % MOD;
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
 * @return {number}
 */
var sumCounts = function(nums) {
    const n = nums.length;
    const MOD = 1000000007;
    const sumSq = new Float64Array(4 * n + 1);
    const sumVal = new Float64Array(4 * n + 1);
    const lazy = new Float64Array(4 * n + 1);
    const lastPos = new Int32Array(100001).fill(-1);

    function apply(node, l, r, v) {
        const cnt = r - l + 1;
        sumSq[node] = (sumSq[node] + 2 * v * sumVal[node] + (v * v % MOD) * cnt) % MOD;
        sumVal[node] = (sumVal[node] + v * cnt) % MOD;
        lazy[node] = (lazy[node] + v) % MOD;
    }

    function update(node, l, r, ql, qr) {
        if (ql <= l && r <= qr) {
            apply(node, l, r, 1);
            return;
        }
        const mid = (l + r) >> 1;
        if (lazy[node] !== 0) {
            apply(node << 1, l, mid, lazy[node]);
            apply((node << 1) | 1, mid + 1, r, lazy[node]);
            lazy[node] = 0;
        }
        if (ql <= mid) update(node << 1, l, mid, ql, qr);
        if (qr > mid) update((node << 1) | 1, mid + 1, r, ql, qr);
        sumSq[node] = (sumSq[node << 1] + sumSq[(node << 1) | 1]) % MOD;
        sumVal[node] = (sumVal[node << 1] + sumVal[(node << 1) | 1]) % MOD;
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        update(1, 0, n - 1, lastPos[nums[i]] + 1, i);
        ans = (ans + sumSq[1]) % MOD;
        lastPos[nums[i]] = i;
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sumCounts(nums: number[]): number {
    const n = nums.length;
    const MOD = 1000000007;

    const sum1 = new Float64Array(4 * n + 1);
    const sum2 = new Float64Array(4 * n + 1);
    const lazy = new Float64Array(4 * n + 1);

    function apply(node: number, start: number, end: number, v: number): void {
        const len = end - start + 1;
        sum2[node] = (sum2[node] + 2 * v * sum1[node] + v * v * len) % MOD;
        sum1[node] = (sum1[node] + v * len) % MOD;
        lazy[node] = (lazy[node] + v) % MOD;
    }

    function pushDown(node: number, start: number, end: number): void {
        if (lazy[node] !== 0) {
            const mid = Math.floor((start + end) / 2);
            apply(2 * node, start, mid, lazy[node]);
            apply(2 * node + 1, mid + 1, end, lazy[node]);
            lazy[node] = 0;
        }
    }

    function pushUp(node: number): void {
        sum1[node] = (sum1[2 * node] + sum1[2 * node + 1]) % MOD;
        sum2[node] = (sum2[2 * node] + sum2[2 * node + 1]) % MOD;
    }

    function update(node: number, start: number, end: number, L: number, R: number, v: number): void {
        if (L <= start && end <= R) {
            apply(node, start, end, v);
            return;
        }
        pushDown(node, start, end);
        const mid = Math.floor((start + end) / 2);
        if (L <= mid) update(2 * node, start, mid, L, R, v);
        if (R > mid) update(2 * node + 1, mid + 1, end, L, R, v);
        pushUp(node);
    }

    const lastPos = new Int32Array(100001).fill(-1);
    let totalSumSq = 0;

    for (let j = 0; j < n; j++) {
        const val = nums[j];
        const prevIdx = lastPos[val];
        update(1, 0, n - 1, prevIdx + 1, j, 1);
        totalSumSq = (totalSumSq + sum2[1]) % MOD;
        lastPos[val] = j;
    }

    return totalSumSq;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    private $sum1, $sum2, $lazy, $MOD = 1000000007;

    function apply($node, $start, $end, $v) {
        $len = $end - $start + 1;
        $this->sum2[$node] = ($this->sum2[$node] + 2 * $v * $this->sum1[$node] + $v * $v * $len) % $this->MOD;
        $this->sum1[$node] = ($this->sum1[$node] + $v * $len) % $this->MOD;
        $this->lazy[$node] = ($this->lazy[$node] + $v) % $this->MOD;
    }

    function pushDown($node, $start, $end) {
        if ($this->lazy[$node] != 0) {
            $mid = (int)(($start + $end) / 2);
            $this->apply(2 * $node, $start, $mid, $this->lazy[$node]);
            $this->apply(2 * $node + 1, $mid + 1, $end, $this->lazy[$node]);
            $this->lazy[$node] = 0;
        }
    }

    function pushUp($node) {
        $this->sum1[$node] = ($this->sum1[2 * $node] + $this->sum1[2 * $node + 1]) % $this->MOD;
        $this->sum2[$node] = ($this->sum2[2 * $node] + $this->sum2[2 * $node + 1]) % $this->MOD;
    }

    function update($node, $start, $end, $L, $R, $v) {
        if ($L <= $start && $end <= $R) {
            $this->apply($node, $start, $end, $v);
            return;
        }
        $this->pushDown($node, $start, $end);
        $mid = (int)(($start + $end) / 2);
        if ($L <= $mid) {
            $this->update(2 * $node, $start, $mid, $L, $R, $v);
        }
        if ($R > $mid) {
            $this->update(2 * $node + 1, $mid + 1, $end, $L, $R, $v);
        }
        $this->pushUp($node);
    }

    function sumCounts($nums) {
        $n = count($nums);
        $this->sum1 = array_fill(0, 4 * $n + 1, 0);
        $this->sum2 = array_fill(0, 4 * $n + 1, 0);
        $this->lazy = array_fill(0, 4 * $n + 1, 0);
        $lastPos = array_fill(0, 100001, -1);
        $totalSumSq = 0;

        for ($j = 0; $j < $n; $j++) {
            $val = $nums[$j];
            $prevIdx = $lastPos[$val];
            $this->update(1, 0, $n - 1, $prevIdx + 1, $j, 1);
            $totalSumSq = ($totalSumSq + $this->sum2[1]) % $this->MOD;
            $lastPos[$val] = $j;
        }

        return $totalSumSq;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sumCounts(_ nums: [Int]) -> Int {
        let n = nums.count
        let MOD = 1_000_000_007
        var sum1 = [Int](repeating: 0, count: 4 * n + 1)
        var sum2 = [Int](repeating: 0, count: 4 * n + 1)
        var lazy = [Int](repeating: 0, count: 4 * n + 1)

        func apply(_ node: Int, _ start: Int, _ end: Int, _ v: Int) {
            let len = end - start + 1
            sum2[node] = (sum2[node] + 2 * v * sum1[node] + v * v * len) % MOD
            sum1[node] = (sum1[node] + v * len) % MOD
            lazy[node] = (lazy[node] + v) % MOD
        }

        func pushDown(_ node: Int, _ start: Int, _ end: Int) {
            if lazy[node] != 0 {
                let mid = (start + end) / 2
                apply(2 * node, start, mid, lazy[node])
                apply(2 * node + 1, mid + 1, end, lazy[node])
                lazy[node] = 0
            }
        }

        func pushUp(_ node: Int) {
            sum1[node] = (sum1[2 * node] + sum1[2 * node + 1]) % MOD
            sum2[node] = (sum2[2 * node] + sum2[2 * node + 1]) % MOD
        }

        func update(_ node: Int, _ start: Int, _ end: Int, _ L: Int, _ R: Int, _ v: Int) {
            if L <= start && end <= R {
                apply(node, start, end, v)
                return
            }
            pushDown(node, start, end)
            let mid = (start + end) / 2
            if L <= mid {
                update(2 * node, start, mid, L, R, v)
            }
            if R > mid {
                update(2 * node + 1, mid + 1, end, L, R, v)
            }
            pushUp(node)
        }

        var lastPos = [Int](repeating: -1, count: 100001)
        var totalSumSq = 0
        for j in 0..<n {
            let val = nums[j]
            let prevIdx = lastPos[val]
            update(1, 0, n - 1, prevIdx + 1, j, 1)
            totalSumSq = (totalSumSq + sum2[1]) % MOD
            lastPos[val] = j
        }

        return totalSumSq
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun sumCounts(nums: IntArray): Int {
        val n = nums.size
        val MOD = 1000000007L

        val sum1 = LongArray(4 * n + 1)
        val sum2 = LongArray(4 * n + 1)
        val lazy = LongArray(4 * n + 1)

        fun apply(node: Int, start: Int, end: Int, v: Long) {
            val len = (end - start + 1).toLong()
            sum2[node] = (sum2[node] + 2 * v * sum1[node] + v * v * len) % MOD
            sum1[node] = (sum1[node] + v * len) % MOD
            lazy[node] = (lazy[node] + v) % MOD
        }

        fun pushDown(node: Int, start: Int, end: Int) {
            if (lazy[node] != 0L) {
                val mid = (start + end) / 2
                apply(2 * node, start, mid, lazy[node])
                apply(2 * node + 1, mid + 1, end, lazy[node])
                lazy[node] = 0
            }
        }

        fun pushUp(node: Int) {
            sum1[node] = (sum1[2 * node] + sum1[2 * node + 1]) % MOD
            sum2[node] = (sum2[2 * node] + sum2[2 * node + 1]) % MOD
        }

        fun update(node: Int, start: Int, end: Int, L: Int, R: Int, v: Long) {
            if (L <= start && end <= R) {
                apply(node, start, end, v)
                return
            }
            pushDown(node, start, end)
            val mid = (start + end) / 2
            if (L <= mid) update(2 * node, start, mid, L, R, v)
            if (R > mid) update(2 * node + 1, mid + 1, end, L, R, v)
            pushUp(node)
        }

        val lastPos = IntArray(100001) { -1 }
        var totalSumSq = 0L

        for (j in 0 until n) {
            val valAtJ = nums[j]
            val prevIdx = lastPos[valAtJ]
            update(1, 0, n - 1, prevIdx + 1, j, 1L)
            totalSumSq = (totalSumSq + sum2[1]) % MOD
            lastPos[valAtJ] = j
        }

        return totalSumSq.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int sumCounts(List<int> nums) {
    int n = nums.length;
    int MOD = 1000000007;
    List<int> sumSq = List<int>.filled(4 * n, 0);
    List<int> sumVal = List<int>.filled(4 * n, 0);
    List<int> lazyAdd = List<int>.filled(4 * n, 0);

    void apply(int v, int tl, int tr, int add) {
      int num = tr - tl + 1;
      int term1 = (2 * add * sumVal[v]) % MOD;
      int term2 = (((add * add) % MOD) * num) % MOD;
      sumSq[v] = (sumSq[v] + term1 + term2) % MOD;
      sumVal[v] = (sumVal[v] + (add * num)) % MOD;
      lazyAdd[v] = (lazyAdd[v] + add) % MOD;
    }

    void push(int v, int tl, int tr) {
      if (lazyAdd[v] != 0) {
        int tm = (tl + tr) ~/ 2;
        apply(2 * v, tl, tm, lazyAdd[v]);
        apply(2 * v + 1, tm + 1, tr, lazyAdd[v]);
        lazyAdd[v] = 0;
      }
    }

    void update(int v, int tl, int tr, int l, int r, int add) {
      if (l > r) return;
      if (l == tl && r == tr) {
        apply(v, tl, tr, add);
      } else {
        push(v, tl, tr);
        int tm = (tl + tr) ~/ 2;
        if (r <= tm) {
          update(2 * v, tl, tm, l, r, add);
        } else if (l > tm) {
          update(2 * v + 1, tm + 1, tr, l, r, add);
        } else {
          update(2 * v, tl, tm, l, tm, add);
          update(2 * v + 1, tm + 1, tr, tm + 1, r, add);
        }
        sumSq[v] = (sumSq[2 * v] + sumSq[2 * v + 1]) % MOD;
        sumVal[v] = (sumVal[2 * v] + sumVal[2 * v + 1]) % MOD;
      }
    }

    int totalAns = 0;
    List<int> lastPos = List<int>.filled(100001, -1);
    for (int j = 0; j < n; j++) {
      int prev = lastPos[nums[j]];
      update(1, 0, n - 1, prev + 1, j, 1);
      totalAns = (totalAns + sumSq[1]) % MOD;
      lastPos[nums[j]] = j;
    }
    return totalAns;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func sumCounts(nums []int) int {
	n := len(nums)
	MOD := int64(1000000007)
	sumSq := make([]int64, 4*n)
	sumVal := make([]int64, 4*n)
	lazyAdd := make([]int64, 4*n)

	var apply func(v, tl, tr int, add int64)
	apply = func(v, tl, tr int, add int64) {
		num := int64(tr - tl + 1)
		term1 := (2 * add * sumVal[v]) % MOD
		term2 := (add * add % MOD * num) % MOD
		sumSq[v] = (sumSq[v] + term1 + term2) % MOD
		sumVal[v] = (sumVal[v] + add*num) % MOD
		lazyAdd[v] = (lazyAdd[v] + add) % MOD
	}

	var push func(v, tl, tr int)
	push = func(v, tl, tr int) {
		if lazyAdd[v] != 0 {
			tm := (tl + tr) / 2
			apply(2*v, tl, tm, lazyAdd[v])
			apply(2*v+1, tm+1, tr, lazyAdd[v])
			lazyAdd[v] = 0
		}
	}

	var update func(v, tl, tr, l, r int, add int64)
	update = func(v, tl, tr, l, r int, add int64) {
		if l > r {
			return
		}
		if l == tl && r == tr {
			apply(v, tl, tr, add)
		} else {
			push(v, tl, tr)
			tm := (tl + tr) / 2
			if r <= tm {
				update(2*v, tl, tm, l, r, add)
			} else if l > tm {
				update(2*v+1, tm+1, tr, l, r, add)
			} else {
				update(2*v, tl, tm, l, tm, add)
				update(2*v+1, tm+1, tr, tm+1, r, add)
			}
			sumSq[v] = (sumSq[2*v] + sumSq[2*v+1]) % MOD
			sumVal[v] = (sumVal[2*v] + sumVal[2*v+1]) % MOD
		}
	}

	totalAns := int64(0)
	lastPos := make([]int, 100001)
	for i := range lastPos {
		lastPos[i] = -1
	}
	for j := 0; j < n; j++ {
		prev := lastPos[nums[j]]
		update(1, 0, n-1, prev+1, j, 1)
		totalAns = (totalAns + sumSq[1]) % MOD
		lastPos[nums[j]] = j
	}

	return int(totalAns)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class SegmentTree
  def initialize(n)
    @n = n
    @sum_sq = Array.new(4 * n, 0)
    @sum_val = Array.new(4 * n, 0)
    @lazy = Array.new(4 * n, 0)
    @mod = 1_000_000_007
  end

  def apply(v, tl, tr, add)
    num = tr - tl + 1
    term1 = (2 * add * @sum_val[v]) % @mod
    term2 = (add * add % @mod * num) % @mod
    @sum_sq[v] = (@sum_sq[v] + term1 + term2) % @mod
    @sum_val[v] = (@sum_val[v] + add * num) % @mod
    @lazy[v] = (@lazy[v] + add) % @mod
  end

  def push(v, tl, tr)
    if @lazy[v] != 0
      tm = (tl + tr) / 2
      apply(2 * v, tl, tm, @lazy[v])
      apply(2 * v + 1, tm + 1, tr, @lazy[v])
      @lazy[v] = 0
    end
  end

  def update(v, tl, tr, l, r, add)
    return if l > r
    if l == tl && r == tr
      apply(v, tl, tr, add)
      return
    end
    push(v, tl, tr)
    tm = (tl + tr) / 2
    if r <= tm
      update(2 * v, tl, tm, l, r, add)
    elsif l > tm
      update(2 * v + 1, tm + 1, tr, l, r, add)
    else
      update(2 * v, tl, tm, l, tm, add)
      update(2 * v + 1, tm + 1, tr, tm + 1, r, add)
    end
    @sum_sq[v] = (@sum_sq[2 * v] + @sum_sq[2 * v + 1]) % @mod
    @sum_val[v] = (@sum_val[2 * v] + @sum_val[2 * v + 1]) % @mod
  end

  def total_sum_sq
    @sum_sq[1]
  end
end

# @param {Integer[]} nums
# @return {Integer}
def sum_counts(nums)
  n = nums.length
  st = SegmentTree.new(n)
  last_pos = Array.new(100001, -1)
  total_ans = 0
  mod = 1_000_000_007

  nums.each_with_index do |num, j|
    prev = last_pos[num]
    st.update(1, 0, n - 1, prev + 1, j, 1)
    total_ans = (total_ans + st.total_sum_sq) % mod
    last_pos[num] = j
  end

  total_ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def sumCounts(nums: Array[Int]): Int = {
    val n = nums.length
    val sumSq = new Array[Long](4 * n)
    val sumVal = new Array[Long](4 * n)
    val lazyAdd = new Array[Long](4 * n)
    val MOD = 1000000007L

    def apply(v: Int, tl: Int, tr: Int, add: Long): Unit = {
      val num = (tr - tl + 1).toLong
      val term1 = (2 * add * sumVal(v)) % MOD
      val term2 = (add * add % MOD * num) % MOD
      sumSq(v) = (sumSq(v) + term1 + term2) % MOD
      sumVal(v) = (sumVal(v) + add * num) % MOD
      lazyAdd(v) = (lazyAdd(v) + add) % MOD
    }

    def push(v: Int, tl: Int, tr: Int): Unit = {
      if (lazyAdd(v) != 0) {
        val tm = (tl + tr) / 2
        apply(2 * v, tl, tm, lazyAdd(v))
        apply(2 * v + 1, tm + 1, tr, lazyAdd(v))
        lazyAdd(v) = 0
      }
    }

    def update(v: Int, tl: Int, tr: Int, l: Int, r: Int, add: Long): Unit = {
      if (l > r) return
      if (l == tl && r == tr) {
        apply(v, tl, tr, add)
      } else {
        push(v, tl, tr)
        val tm = (tl + tr) / 2
        if (r <= tm) update(2 * v, tl, tm, l, r, add)
        else if (l > tm) update(2 * v + 1, tm + 1, tr, l, r, add)
        else {
          update(2 * v, tl, tm, l, tm, add)
          update(2 * v + 1, tm + 1, tr, tm + 1, r, add)
        }
        sumSq(v) = (sumSq(2 * v) + sumSq(2 * v + 1)) % MOD
        sumVal(v) = (sumVal(2 * v) + sumVal(2 * v + 1)) % MOD
      }
    }

    var totalAns = 0L
    val lastPos = Array.fill(100001)(-1)
    var j = 0
    while (j < n) {
      val num = nums(j)
      val prev = lastPos(num)
      update(1, 0, n - 1, prev + 1, j, 1L)
      totalAns = (totalAns + sumSq(1)) % MOD
      lastPos(num) = j
      j += 1
    }
    totalAns.toInt
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut sum = vec![0i64; 4 * n + 1];
        let mut sq_sum = vec![0i64; 4 * n + 1];
        let mut lazy = vec![0i64; 4 * n + 1];
        let mut last_pos = vec![-1i32; 100001];
        let mut total_ans = 0i64;
        let mod_val = 1_000_000_007i64;

        fn apply_lazy(idx: usize, l: usize, r: usize, v: i64, sum: &mut [i64], sq_sum: &mut [i64], lazy: &mut [i64], mod_val: i64) {
            let len = (r - l + 1) as i64;
            sq_sum[idx] = (sq_sum[idx] + 2 * v * sum[idx] + v * v % mod_val * len) % mod_val;
            sum[idx] = (sum[idx] + v * len) % mod_val;
            lazy[idx] = (lazy[idx] + v) % mod_val;
        }

        fn push_down(idx: usize, l: usize, mid: usize, r: usize, sum: &mut [i64], sq_sum: &mut [i64], lazy: &mut [i64], mod_val: i64) {
            if lazy[idx] != 0 {
                let v = lazy[idx];
                apply_lazy(2 * idx, l, mid, v, sum, sq_sum, lazy, mod_val);
                apply_lazy(2 * idx + 1, mid + 1, r, v, sum, sq_sum, lazy, mod_val);
                lazy[idx] = 0;
            }
        }

        fn update(idx: usize, l: usize, r: usize, ql: usize, qr: usize, v: i64, sum: &mut [i64], sq_sum: &mut [i64], lazy: &mut [i64], mod_val: i64) {
            if ql <= l && r <= qr {
                apply_lazy(idx, l, r, v, sum, sq_sum, lazy, mod_val);
                return;
            }
            let mid = (l + r) / 2;
            push_down(idx, l, mid, r, sum, sq_sum, lazy, mod_val);
            if ql <= mid {
                update(2 * idx, l, mid, ql, qr, v, sum, sq_sum, lazy, mod_val);
            }
            if qr > mid {
                update(2 * idx + 1, mid + 1, r, ql, qr, v, sum, sq_sum, lazy, mod_val);
            }
            sum[idx] = (sum[2 * idx] + sum[2 * idx + 1]) % mod_val;
            sq_sum[idx] = (sq_sum[2 * idx] + sq_sum[2 * idx + 1]) % mod_val;
        }

        for i in 0..n {
            let p = last_pos[nums[i] as usize];
            update(1, 0, n - 1, (p + 1) as usize, i, 1, &mut sum, &mut sq_sum, &mut lazy, mod_val);
            total_ans = (total_ans + sq_sum[1]) % mod_val;
            last_pos[nums[i] as usize] = i as i32;
        }
        total_ans as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sum-counts nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [MOD 1000000007]
         [sum (make-vector (+ (* 4 n) 1) 0)]
         [sq-sum (make-vector (+ (* 4 n) 1) 0)]
         [lazy (make-vector (+ (* 4 n) 1) 0)]
         [last-pos (make-vector 100001 -1)]
         [nums-vec (list->vector nums)])

    (define (apply-lazy-node idx l r v)
      (let ([len (+ (- r l) 1)])
        (vector-set! sq-sum idx (modulo (+ (vector-ref sq-sum idx)
                                           (* 2 v (vector-ref sum idx))
                                           (* v v len)) MOD))
        (vector-set! sum idx (modulo (+ (vector-ref sum idx) (* v len)) MOD))
        (vector-set! lazy idx (modulo (+ (vector-ref lazy idx) v) MOD))))

    (define (push-down idx l mid r)
      (let ([lz (vector-ref lazy idx)])
        (when (and (not (zero? lz)) (< l r))
          (apply-lazy-node (* 2 idx) l mid lz)
          (apply-lazy-node (+ (* 2 idx) 1) (+ mid 1) r lz)
          (vector-set! lazy idx 0))))

    (define (update idx l r ql qr v)
      (if (and (<= ql l) (<= r qr))
          (apply-lazy-node idx l r v)
          (let* ([mid (quotient (+ l r) 2)])
            (push-down idx l mid r)
            (when (<= ql mid)
              (update (* 2 idx) l mid ql qr v))
            (when (> qr mid)
              (update (+ (* 2 idx) 1) (+ mid 1) r ql qr v))
            (vector-set! sum idx (modulo (+ (vector-ref sum (* 2 idx)) (vector-ref sum (+ (* 2 idx) 1))) MOD))
            (vector-set! sq-sum idx (modulo (+ (vector-ref sq-sum (* 2 idx)) (vector-ref sq-sum (+ (* 2 idx) 1))) MOD)))))

    (let loop ([i 0] [total-ans 0])
      (if (< i n)
          (let* ([val (vector-ref nums-vec i)]
                 [p (vector-ref last-pos val)])
            (update 1 0 (- n 1) (+ p 1) i 1)
            (vector-set! last-pos val i)
            (loop (+ i 1) (modulo (+ total-ans (vector-ref sq-sum 1)) MOD)))
          total-ans))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sum_counts(Nums :: [integer()]) -> integer().
sum_counts(Nums) ->
    N = length(Nums),
    Mod = 1000000007,
    InitialTree = build(0, N - 1),
    {TotalAns, _, _, _} = lists:foldl(fun(X, {Acc, T, LP, I}) ->
        P = maps:get(X, LP, -1),
        NewT = update(T, 0, N - 1, P + 1, I, 1),
        {{SqSum, _, _}, _, _} = NewT,
        NewAcc = (Acc + SqSum) rem Mod,
        {NewAcc, NewT, maps:put(X, I, LP), I + 1}
    end, {0, InitialTree, #{}, 0}, Nums),
    TotalAns.

build(L, R) ->
    if L =:= R -> {{0, 0, 0}, nil, nil};
    true ->
        Mid = (L + R) div 2,
        {{0, 0, 0}, build(L, Mid), build(Mid + 1, R)}
    end.

update({{SqSum, Sum, Lazy}, Left, Right}, L, R, QL, QR, V) ->
    if (QL =< L) and (R =< QR) ->
        apply_lazy({{SqSum, Sum, Lazy}, Left, Right}, L, R, V);
    true ->
        Mid = (L + R) div 2,
        {L1, R1} = push({{SqSum, Sum, Lazy}, Left, Right}, L, Mid, R),
        {L2, R2} = if
            QR =< Mid -> {update(L1, L, Mid, QL, QR, V), R1};
            QL > Mid -> {L1, update(R1, Mid + 1, R, QL, QR, V)};
            true -> {update(L1, L, Mid, QL, Mid, V), update(R1, Mid + 1, R, Mid + 1, QR, V)}
        end,
        {{SqSumL, SumL, _}, _, _} = L2,
        {{SqSumR, SumR, _}, _, _} = R2,
        {{(SqSumL + SqSumR) rem 1000000007, (SumL + SumR) rem 1000000007, 0}, L2, R2}
    end.

push({{_, _, 0}, Left, Right}, _, _, _) -> {Left, Right};
push({{_, _, Lazy}, Left, Right}, L, Mid, R) ->
    {apply_lazy(Left, L, Mid, Lazy), apply_lazy(Right, Mid + 1, R, Lazy)}.

apply_lazy({{SqSum, Sum, Lazy}, Left, Right}, L, R, V) ->
    Len = R - L + 1,
    Mod = 1000000007,
    NewSqSum = (SqSum + 2 * V * Sum + V * V * Len) rem Mod,
    NewSum = (Sum + V * Len) rem Mod,
    NewLazy = (Lazy + V) rem Mod,
    {{NewSqSum, NewSum, NewLazy}, Left, Right}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @mod_val 1_000_000_007

  @spec sum_counts(nums :: [integer]) :: integer
  def sum_counts(nums) do
    n = length(nums)
    tree = build(0, n - 1)
    {total_ans, _, _, _} = Enum.reduce(nums, {0, tree, %{}, 0}, fn x, {acc, t, lp, i} ->
      p = Map.get(lp, x, -1)
      new_t = update(t, 0, n - 1, p + 1, i, 1)
      {{sq_sum, _sum, _lazy}, _left, _right} = new_t
      new_acc = rem(acc + sq_sum, @mod_val)
      {new_acc, new_t, Map.put(lp, x, i), i + 1}
    end)
    total_ans
  end

  defp build(l, r) do
    if l == r do
      {{0, 0, 0}, nil, nil}
    else
      mid = div(l + r, 2)
      {{0, 0, 0}, build(l, mid), build(mid + 1, r)}
    end
  end

  defp update({{sq_sum, sum, lazy}, left, right}, l, r, ql, qr, v) do
    if ql <= l and r <= qr do
      apply_lazy({{sq_sum, sum, lazy}, left, right}, l, r, v)
    else
      mid = div(l + r, 2)
      {left, right} = push({{sq_sum, sum, lazy}, left, right}, l, mid, r)

      {new_left, new_right} = cond do
        qr <= mid -> {update(left, l, mid, ql, qr, v), right}
        ql > mid -> {left, update(right, mid + 1, r, ql, qr, v)}
        true -> {update(left, l, mid, ql, mid, v), update(right, mid + 1, r, mid + 1, qr, v)}
      end

      {{l_sq, l_s, _}, _, _} = new_left
      {{r_sq, r_s, _}, _, _} = new_right
      {{rem(l_sq + r_sq, @mod_val), rem(l_s + r_s, @mod_val), 0}, new_left, new_right}
    end
  end

  defp push({{_sq, _s, 0}, left, right}, _l, _mid, _r), do: {left, right}
  defp push({{_sq, _s, lazy}, left, right}, l, mid, r) do
    {apply_lazy(left, l, mid, lazy), apply_lazy(right, mid + 1, r, lazy)}
  end

  defp apply_lazy({{sq_sum, sum, l_lazy}, left, right}, l, r, v) do
    len = r - l + 1
    new_sq_sum = rem(sq_sum + 2 * v * sum + v * v * len, @mod_val)
    new_sum = rem(sum + v * len, @mod_val)
    new_lazy = rem(l_lazy + v, @mod_val)
    {{new_sq_sum, new_sum, new_lazy}, left, right}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N), where N is the length of the array. The algorithm iterates through the array once (N iterations), and for each element, it performs a range update on the Segment Tree, which takes O(log N) time.
- **Space Complexity:** O(N), as we store the Segment Tree arrays (size 4N) and an array to track the last seen positions of each element (size 10^5).
