---
layout: post
title: "Block Placement Queries"
date: 2026-05-30 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search", "Binary Indexed Tree", "Segment Tree"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/block-placement-queries/
ai_solutions:
  - solutions:
      cpp: "class SegmentTree {\n    int n;\n    vector<int> tree;\npublic:\n    SegmentTree(int\
        \ size) {\n        n = 1;\n        while (n < size) n *= 2;\n        tree.assign(2\
        \ * n, 0);\n    }\n    void update(int i, int val) {\n        i += n;\n    \
        \    tree[i] = val;\n        while (i > 1) {\n            i /= 2;\n        \
        \    tree[i] = max(tree[2 * i], tree[2 * i + 1]);\n        }\n    }\n    int\
        \ query(int l, int r) {\n        int res = 0;\n        l += n;\n        r +=\
        \ n;\n        while (l < r) {\n            if (l % 2 == 1) res = max(res, tree[l++]);\n\
        \            if (r % 2 == 1) res = max(res, tree[--r]);\n            l /= 2;\n\
        \            r /= 2;\n        }\n        return res;\n    }\n};\n\nclass Solution\
        \ {\npublic:\n    vector<bool> getResults(vector<vector<int>>& queries) {\n\
        \        int max_x = 0;\n        for (const auto& q : queries) if (q[1] > max_x)\
        \ max_x = q[1];\n        SegmentTree st(max_x + 1);\n        set<int> obstacles;\n\
        \        obstacles.insert(0);\n        vector<bool> results;\n        for (const\
        \ auto& q : queries) {\n            if (q[0] == 1) {\n                int x\
        \ = q[1];\n                auto it = obstacles.lower_bound(x);\n           \
        \     int x_prev = *prev(it);\n                if (it != obstacles.end()) {\n\
        \                    int x_next = *it;\n                    st.update(x_next,\
        \ x_next - x);\n                }\n                st.update(x, x - x_prev);\n\
        \                obstacles.insert(x);\n            } else {\n              \
        \  int x = q[1], sz = q[2];\n                int x_prev = *prev(obstacles.upper_bound(x));\n\
        \                int max_gap = max(st.query(0, x_prev + 1), x - x_prev);\n \
        \               results.push_back(max_gap >= sz);\n            }\n        }\n\
        \        return results;\n    }\n};"
      java: "import java.util.*;\n\nclass SegmentTree {\n    int n;\n    int[] tree;\n\
        \    public SegmentTree(int size) {\n        n = 1;\n        while (n < size)\
        \ n *= 2;\n        tree = new int[2 * n];\n    }\n    public void update(int\
        \ i, int val) {\n        i += n;\n        tree[i] = val;\n        while (i >\
        \ 1) {\n            i /= 2;\n            tree[i] = Math.max(tree[2 * i], tree[2\
        \ * i + 1]);\n        }\n    }\n    public int query(int l, int r) {\n     \
        \   int res = 0;\n        l += n;\n        r += n;\n        while (l < r) {\n\
        \            if (l % 2 == 1) res = Math.max(res, tree[l++]);\n            if\
        \ (r % 2 == 1) res = Math.max(res, tree[--r]);\n            l /= 2;\n      \
        \      r /= 2;\n        }\n        return res;\n    }\n}\n\nclass Solution {\n\
        \    public List<Boolean> getResults(int[][] queries) {\n        int maxX =\
        \ 0;\n        for (int[] q : queries) if (q[1] > maxX) maxX = q[1];\n      \
        \  SegmentTree st = new SegmentTree(maxX + 1);\n        TreeSet<Integer> obstacles\
        \ = new TreeSet<>();\n        obstacles.add(0);\n        List<Boolean> results\
        \ = new ArrayList<>();\n        for (int[] q : queries) {\n            if (q[0]\
        \ == 1) {\n                int x = q[1];\n                Integer xNext = obstacles.higher(x);\n\
        \                int xPrev = obstacles.lower(x);\n                if (xNext\
        \ != null) st.update(xNext, xNext - x);\n                st.update(x, x - xPrev);\n\
        \                obstacles.add(x);\n            } else {\n                int\
        \ x = q[1], sz = q[2];\n                int xPrev = obstacles.floor(x);\n  \
        \              int maxGap = Math.max(st.query(0, xPrev + 1), x - xPrev);\n \
        \               results.add(maxGap >= sz);\n            }\n        }\n     \
        \   return results;\n    }\n}"
      python: "import bisect\n\nclass SegmentTree:\n    def __init__(self, size):\n\
        \        self.n = 1\n        while self.n < size: self.n *= 2\n        self.tree\
        \ = [0] * (2 * self.n)\n\n    def update(self, i, val):\n        i += self.n\n\
        \        self.tree[i] = val\n        while i > 1:\n            i >>= 1\n   \
        \         self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])\n\n   \
        \ def query(self, l, r):\n        res = 0\n        l += self.n\n        r +=\
        \ self.n\n        while l < r:\n            if l & 1:\n                res =\
        \ max(res, self.tree[l])\n                l += 1\n            if r & 1:\n  \
        \              r -= 1\n                res = max(res, self.tree[r])\n      \
        \      l >>= 1\n            r >>= 1\n        return res\n\nclass Solution(object):\n\
        \    def getResults(self, queries):\n        max_x = 0\n        for q in queries:\
        \ \n            if q[1] > max_x: max_x = q[1]\n        st = SegmentTree(max_x\
        \ + 1)\n        obstacles = [0]\n        ans = []\n        for q in queries:\n\
        \            if q[0] == 1:\n                x = q[1]\n                idx =\
        \ bisect.bisect_left(obstacles, x)\n                x_prev = obstacles[idx -\
        \ 1]\n                if idx < len(obstacles):\n                    x_next =\
        \ obstacles[idx]\n                    st.update(x_next, x_next - x)\n      \
        \          st.update(x, x - x_prev)\n                bisect.insort(obstacles,\
        \ x)\n            else:\n                x, sz = q[1], q[2]\n              \
        \  idx = bisect.bisect_right(obstacles, x)\n                x_p = obstacles[idx\
        \ - 1]\n                best = st.query(0, x_p + 1)\n                if x -\
        \ x_p > best: best = x - x_p\n                ans.append(best >= sz)\n     \
        \   return ans"
      python3: "class Solution:\n    def getResults(self, queries: List[List[int]])\
        \ -> List[bool]:\n        M = 50005\n        n = 1 << 16\n        tree = [0]\
        \ * (2 * n)\n        bit = [0] * (M + 1)\n        total_obstacles = 1\n\n  \
        \      def update_tree(i, val):\n            i += n\n            tree[i] = val\n\
        \            while i > 1:\n                left, right = tree[i], tree[i ^ 1]\n\
        \                tree[i >> 1] = left if left > right else right\n          \
        \      i >>= 1\n\n        def query_tree(l, r):\n            res = 0\n     \
        \       l += n\n            r += n\n            while l < r:\n             \
        \   if l & 1:\n                    if tree[l] > res: res = tree[l]\n       \
        \             l += 1\n                if r & 1:\n                    r -= 1\n\
        \                    if tree[r] > res: res = tree[r]\n                l >>=\
        \ 1\n                r >>= 1\n            return res\n\n        def update_bit(i,\
        \ delta):\n            i += 1\n            while i <= M:\n                bit[i]\
        \ += delta\n                i += i & -i\n\n        def query_bit(i):\n     \
        \       i += 1\n            res = 0\n            while i > 0:\n            \
        \    res += bit[i]\n                i -= i & -i\n            return res\n\n\
        \        def find_kth(k):\n            idx = 0\n            for i in [32768,\
        \ 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]:\n \
        \               if idx + i <= M and bit[idx + i] < k:\n                    idx\
        \ += i\n                    k -= bit[idx]\n            return idx\n\n      \
        \  update_bit(0, 1)\n        results = []\n        for q in queries:\n     \
        \       if q[0] == 1:\n                x = q[1]\n                k = query_bit(x\
        \ - 1)\n                p = find_kth(k)\n                next_obs = find_kth(k\
        \ + 1) if k < total_obstacles else -1\n                update_tree(x, x - p)\n\
        \                if next_obs != -1:\n                    update_tree(next_obs,\
        \ next_obs - x)\n                update_bit(x, 1)\n                total_obstacles\
        \ += 1\n            else:\n                x, sz = q[1], q[2]\n            \
        \    k = query_bit(x)\n                p = find_kth(k)\n                max_gap\
        \ = query_tree(0, p + 1)\n                if x - p > max_gap:\n            \
        \        max_gap = x - p\n                results.append(max_gap >= sz)\n  \
        \      return results"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n\nvoid updateTree(int i, int val,\
        \ int* tree, int n) {\n    i += n;\n    tree[i] = val;\n    while (i > 1) {\n\
        \        tree[i >> 1] = (tree[i] > tree[i ^ 1]) ? tree[i] : tree[i ^ 1];\n \
        \       i >>= 1;\n    }\n}\n\nint queryTree(int l, int r, int* tree, int n)\
        \ {\n    int res = 0;\n    l += n;\n    r += n;\n    while (l < r) {\n     \
        \   if (l & 1) {\n            if (tree[l] > res) res = tree[l];\n          \
        \  l++;\n        }\n        if (r & 1) {\n            r--;\n            if (tree[r]\
        \ > res) res = tree[r];\n        }\n        l >>= 1;\n        r >>= 1;\n   \
        \ }\n    return res;\n}\n\nvoid updateBit(int i, int delta, int* bit, int M)\
        \ {\n    i++;\n    while (i <= M) {\n        bit[i] += delta;\n        i +=\
        \ i & -i;\n    }\n}\n\nint queryBit(int i, int* bit) {\n    i++;\n    int res\
        \ = 0;\n    while (i > 0) {\n        res += bit[i];\n        i -= i & -i;\n\
        \    }\n    return res;\n}\n\nint findKth(int k, int* bit, int M) {\n    int\
        \ idx = 0;\n    for (int i = 1 << 15; i > 0; i >>= 1) {\n        if (idx + i\
        \ <= M && bit[idx + i] < k) {\n            idx += i;\n            k -= bit[idx];\n\
        \        }\n    }\n    return idx;\n}\n\nbool* getResults(int** queries, int\
        \ queriesSize, int* queriesColSize, int* returnSize) {\n    int M = 50001;\n\
        \    int n = 1 << 16;\n    int* tree = (int*)calloc(2 * n, sizeof(int));\n \
        \   int* bit = (int*)calloc(M + 1, sizeof(int));\n    int total_obstacles =\
        \ 1;\n    updateBit(0, 1, bit, M);\n\n    bool* results = (bool*)malloc(queriesSize\
        \ * sizeof(bool));\n    int resIdx = 0;\n\n    for (int i = 0; i < queriesSize;\
        \ i++) {\n        if (queries[i][0] == 1) {\n            int x = queries[i][1];\n\
        \            int k = queryBit(x - 1, bit);\n            int p = findKth(k, bit,\
        \ M);\n            int next_obs = (k < total_obstacles) ? findKth(k + 1, bit,\
        \ M) : -1;\n            updateTree(x, x - p, tree, n);\n            if (next_obs\
        \ != -1) updateTree(next_obs, next_obs - x, tree, n);\n            updateBit(x,\
        \ 1, bit, M);\n            total_obstacles++;\n        } else {\n          \
        \  int x = queries[i][1];\n            int sz = queries[i][2];\n           \
        \ int k = queryBit(x, bit);\n            int p = findKth(k, bit, M);\n     \
        \       int maxGap = queryTree(0, p + 1, tree, n);\n            if (x - p >\
        \ maxGap) maxGap = x - p;\n            results[resIdx++] = (maxGap >= sz);\n\
        \        }\n    }\n\n    free(tree);\n    free(bit);\n    *returnSize = resIdx;\n\
        \    return results;\n}"
      csharp: "public class Solution {\n    public IList<bool> GetResults(int[][] queries)\
        \ {\n        int M = 50001;\n        int n = 1 << 16;\n        int[] tree =\
        \ new int[2 * n];\n        int[] bit = new int[M + 1];\n        int total_obstacles\
        \ = 1;\n\n        void UpdateTree(int i, int val) {\n            i += n;\n \
        \           tree[i] = val;\n            while (i > 1) {\n                tree[i\
        \ >> 1] = Math.Max(tree[i], tree[i ^ 1]);\n                i >>= 1;\n      \
        \      }\n        }\n\n        int QueryTree(int l, int r) {\n            int\
        \ res = 0;\n            l += n;\n            r += n;\n            while (l <\
        \ r) {\n                if ((l & 1) == 1) res = Math.Max(res, tree[l++]);\n\
        \                if ((r & 1) == 1) res = Math.Max(res, tree[--r]);\n       \
        \         l >>= 1;\n                r >>= 1;\n            }\n            return\
        \ res;\n        }\n\n        void UpdateBit(int i, int delta) {\n          \
        \  i++;\n            while (i <= M) {\n                bit[i] += delta;\n  \
        \              i += i & -i;\n            }\n        }\n\n        int QueryBit(int\
        \ i) {\n            i++;\n            int res = 0;\n            while (i > 0)\
        \ {\n                res += bit[i];\n                i -= i & -i;\n        \
        \    }\n            return res;\n        }\n\n        int FindKth(int k) {\n\
        \            int idx = 0;\n            for (int i = 1 << 15; i > 0; i >>= 1)\
        \ {\n                if (idx + i <= M && bit[idx + i] < k) {\n             \
        \       idx += i;\n                    k -= bit[idx];\n                }\n \
        \           }\n            return idx;\n        }\n\n        UpdateBit(0, 1);\n\
        \        List<bool> results = new List<bool>();\n        foreach (var q in queries)\
        \ {\n            if (q[0] == 1) {\n                int x = q[1];\n         \
        \       int k = QueryBit(x - 1);\n                int p = FindKth(k);\n    \
        \            int next_obs = (k < total_obstacles) ? FindKth(k + 1) : -1;\n \
        \               UpdateTree(x, x - p);\n                if (next_obs != -1) UpdateTree(next_obs,\
        \ next_obs - x);\n                UpdateBit(x, 1);\n                total_obstacles++;\n\
        \            } else {\n                int x = q[1], sz = q[2];\n          \
        \      int k = QueryBit(x);\n                int p = FindKth(k);\n         \
        \       int maxGap = Math.Max(QueryTree(0, p + 1), x - p);\n               \
        \ results.Add(maxGap >= sz);\n            }\n        }\n        return results;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[][]} queries\n * @return {boolean[]}\n */\n\
        var getResults = function(queries) {\n    const M = 50001;\n    const n = 1\
        \ << 16;\n    const tree = new Int32Array(2 * n);\n    const bit = new Int32Array(M\
        \ + 1);\n    let total_obstacles = 1;\n\n    function updateTree(i, val) {\n\
        \        i += n;\n        tree[i] = val;\n        while (i > 1) {\n        \
        \    tree[i >> 1] = Math.max(tree[i], tree[i ^ 1]);\n            i >>= 1;\n\
        \        }\n    }\n\n    function queryTree(l, r) {\n        let res = 0;\n\
        \        l += n;\n        r += n;\n        while (l < r) {\n            if (l\
        \ & 1) res = Math.max(res, tree[l++]);\n            if (r & 1) res = Math.max(res,\
        \ tree[--r]);\n            l >>= 1;\n            r >>= 1;\n        }\n     \
        \   return res;\n    }\n\n    function updateBit(i, delta) {\n        for (i++;\
        \ i <= M; i += i & -i) bit[i] += delta;\n    }\n\n    function queryBit(i) {\n\
        \        let res = 0;\n        for (i++; i > 0; i -= i & -i) res += bit[i];\n\
        \        return res;\n    }\n\n    function findKth(k) {\n        let idx =\
        \ 0;\n        for (let i = 1 << 15; i > 0; i >>= 1) {\n            if (idx +\
        \ i <= M && bit[idx + i] < k) {\n                idx += i;\n               \
        \ k -= bit[idx];\n            }\n        }\n        return idx;\n    }\n\n \
        \   updateBit(0, 1);\n    const results = [];\n    for (let i = 0; i < queries.length;\
        \ i++) {\n        const q = queries[i];\n        if (q[0] === 1) {\n       \
        \     const x = q[1];\n            const k = queryBit(x - 1);\n            const\
        \ p = findKth(k);\n            const next_obs = k < total_obstacles ? findKth(k\
        \ + 1) : -1;\n            updateTree(x, x - p);\n            if (next_obs !==\
        \ -1) updateTree(next_obs, next_obs - x);\n            updateBit(x, 1);\n  \
        \          total_obstacles++;\n        } else {\n            const x = q[1],\
        \ sz = q[2];\n            const k = queryBit(x);\n            const p = findKth(k);\n\
        \            const maxGap = Math.max(queryTree(0, p + 1), x - p);\n        \
        \    results.push(maxGap >= sz);\n        }\n    }\n    return results;\n};"
      typescript: "class SegmentTree {\n    private size: number;\n    private tree:\
        \ Int32Array;\n\n    constructor(n: number) {\n        this.size = 1;\n    \
        \    while (this.size < n) this.size *= 2;\n        this.tree = new Int32Array(2\
        \ * this.size);\n    }\n\n    update(i: number, val: number): void {\n     \
        \   i += this.size;\n        this.tree[i] = val;\n        while (i > 1) {\n\
        \            i >>= 1;\n            this.tree[i] = Math.max(this.tree[2 * i],\
        \ this.tree[2 * i + 1]);\n        }\n    }\n\n    query(l: number, r: number):\
        \ number {\n        let res = 0;\n        l += this.size;\n        r += this.size;\n\
        \        while (l <= r) {\n            if (l % 2 === 1) res = Math.max(res,\
        \ this.tree[l++]);\n            if (r % 2 === 0) res = Math.max(res, this.tree[r--]);\n\
        \            l >>= 1;\n            r >>= 1;\n        }\n        return res;\n\
        \    }\n}\n\nfunction getResults(queries: number[][]): boolean[] {\n    let\
        \ maxX = 0;\n    for (const q of queries) {\n        if (q[1] > maxX) maxX =\
        \ q[1];\n    }\n\n    const st = new SegmentTree(maxX + 1);\n    const obs =\
        \ [0];\n    const results: boolean[] = [];\n\n    function bisectLeft(arr: number[],\
        \ x: number): number {\n        let low = 0, high = arr.length;\n        while\
        \ (low < high) {\n            let mid = (low + high) >>> 1;\n            if\
        \ (arr[mid] < x) low = mid + 1;\n            else high = mid;\n        }\n \
        \       return low;\n    }\n\n    function bisectRight(arr: number[], x: number):\
        \ number {\n        let low = 0, high = arr.length;\n        while (low < high)\
        \ {\n            let mid = (low + high) >>> 1;\n            if (arr[mid] <=\
        \ x) low = mid + 1;\n            else high = mid;\n        }\n        return\
        \ low;\n    }\n\n    for (const q of queries) {\n        if (q[0] === 1) {\n\
        \            const x = q[1];\n            const idx = bisectLeft(obs, x);\n\
        \            const prevX = obs[idx - 1];\n            const nextX = obs[idx];\n\
        \n            st.update(x, x - prevX);\n            if (nextX !== undefined)\
        \ {\n                st.update(nextX, nextX - x);\n            }\n         \
        \   obs.splice(idx, 0, x);\n        } else {\n            const x = q[1];\n\
        \            const sz = q[2];\n            const idx = bisectRight(obs, x);\n\
        \            const lastObs = obs[idx - 1];\n            const maxGap = Math.max(st.query(0,\
        \ x), x - lastObs);\n            results.push(maxGap >= sz);\n        }\n  \
        \  }\n\n    return results;\n}"
      php: "class SegmentTree {\n    public $size;\n    public $tree;\n\n    public\
        \ function __construct($n) {\n        $this->size = 1;\n        while ($this->size\
        \ < $n) $this->size *= 2;\n        $this->tree = array_fill(0, 2 * $this->size,\
        \ 0);\n    }\n\n    public function update($i, $val) {\n        $i += $this->size;\n\
        \        $this->tree[$i] = $val;\n        while ($i > 1) {\n            $i >>=\
        \ 1;\n            $this->tree[$i] = max($this->tree[2 * $i], $this->tree[2 *\
        \ $i + 1]);\n        }\n    }\n\n    public function query($l, $r) {\n     \
        \   $res = 0;\n        $l += $this->size;\n        $r += $this->size;\n    \
        \    while ($l <= $r) {\n            if ($l % 2 == 1) $res = max($res, $this->tree[$l++]);\n\
        \            if ($r % 2 == 0) $res = max($res, $this->tree[$r--]);\n       \
        \     $l >>= 1;\n            $r >>= 1;\n        }\n        return $res;\n  \
        \  }\n}\n\nclass Solution {\n    function bisect_left($arr, $x) {\n        $l\
        \ = 0; $r = count($arr);\n        while ($l < $r) {\n            $m = (int)(($l\
        \ + $r) / 2);\n            if ($arr[$m] < $x) $l = $m + 1;\n            else\
        \ $r = $m;\n        }\n        return $l;\n    }\n\n    function bisect_right($arr,\
        \ $x) {\n        $l = 0; $r = count($arr);\n        while ($l < $r) {\n    \
        \        $m = (int)(($l + $r) / 2);\n            if ($arr[$m] <= $x) $l = $m\
        \ + 1;\n            else $r = $m;\n        }\n        return $l;\n    }\n\n\
        \    /**\n     * @param Integer[][] $queries\n     * @return Boolean[]\n   \
        \  */\n    function getResults($queries) {\n        $max_x = 0;\n        foreach\
        \ ($queries as $q) {\n            if ($q[1] > $max_x) $max_x = $q[1];\n    \
        \    }\n\n        $st = new SegmentTree($max_x + 1);\n        $obs = [0];\n\
        \        $results = [];\n\n        foreach ($queries as $q) {\n            if\
        \ ($q[0] == 1) {\n                $x = $q[1];\n                $idx = $this->bisect_left($obs,\
        \ $x);\n                $prev_x = $obs[$idx - 1];\n                $next_x =\
        \ isset($obs[$idx]) ? $obs[$idx] : null;\n\n                $st->update($x,\
        \ $x - $prev_x);\n                if ($next_x !== null) {\n                \
        \    $st->update($next_x, $next_x - $x);\n                }\n              \
        \  array_splice($obs, $idx, 0, $x);\n            } else {\n                $x\
        \ = $q[1];\n                $sz = $q[2];\n                $idx = $this->bisect_right($obs,\
        \ $x);\n                $last_obs = $obs[$idx - 1];\n                $max_gap\
        \ = max($st->query(0, $x), $x - $last_obs);\n                $results[] = $max_gap\
        \ >= $sz;\n            }\n        }\n        return $results;\n    }\n}"
      swift: "class SegmentTree {\n    var size: Int\n    var tree: [Int]\n\n    init(_\
        \ n: Int) {\n        self.size = 1\n        while self.size < n { self.size\
        \ *= 2 }\n        self.tree = Array(repeating: 0, count: 2 * self.size)\n  \
        \  }\n\n    func update(_ i: Int, _ val: Int) {\n        var idx = i + size\n\
        \        tree[idx] = val\n        while idx > 1 {\n            idx /= 2\n  \
        \          tree[idx] = max(tree[2 * idx], tree[2 * idx + 1])\n        }\n  \
        \  }\n\n    func query(_ l: Int, _ r: Int) -> Int {\n        var res = 0\n \
        \       var left = l + size\n        var right = r + size\n        while left\
        \ <= right {\n            if left % 2 == 1 {\n                res = max(res,\
        \ tree[left])\n                left += 1\n            }\n            if right\
        \ % 2 == 0 {\n                res = max(res, tree[right])\n                right\
        \ -= 1\n            }\n            left /= 2\n            right /= 2\n     \
        \   }\n        return res\n    }\n}\n\nclass Solution {\n    func getResults(_\
        \ queries: [[Int]]) -> [Bool] {\n        var maxX = 0\n        for q in queries\
        \ {\n            if q[1] > maxX { maxX = q[1] }\n        }\n\n        let st\
        \ = SegmentTree(maxX + 1)\n        var obs = [0]\n        var results = [Bool]()\n\
        \n        func bisectLeft(_ arr: [Int], _ x: Int) -> Int {\n            var\
        \ low = 0, high = arr.count\n            while low < high {\n              \
        \  let mid = (low + high) / 2\n                if arr[mid] < x { low = mid +\
        \ 1 } else { high = mid }\n            }\n            return low\n        }\n\
        \n        func bisectRight(_ arr: [Int], _ x: Int) -> Int {\n            var\
        \ low = 0, high = arr.count\n            while low < high {\n              \
        \  let mid = (low + high) / 2\n                if arr[mid] <= x { low = mid\
        \ + 1 } else { high = mid }\n            }\n            return low\n       \
        \ }\n\n        for q in queries {\n            if q[0] == 1 {\n            \
        \    let x = q[1]\n                let idx = bisectLeft(obs, x)\n          \
        \      let prevX = obs[idx - 1]\n                st.update(x, x - prevX)\n \
        \               if idx < obs.count {\n                    let nextX = obs[idx]\n\
        \                    st.update(nextX, nextX - x)\n                }\n      \
        \          obs.insert(x, at: idx)\n            } else {\n                let\
        \ x = q[1], sz = q[2]\n                let idx = bisectRight(obs, x)\n     \
        \           let lastObs = obs[idx - 1]\n                let maxGap = max(st.query(0,\
        \ x), x - lastObs)\n                results.append(maxGap >= sz)\n         \
        \   }\n        }\n        return results\n    }\n}"
      kotlin: "import java.util.TreeSet\n\nclass SegmentTree(n: Int) {\n    var size\
        \ = 1\n    val tree: IntArray\n\n    init {\n        while (size < n) size *=\
        \ 2\n        tree = IntArray(2 * size)\n    }\n\n    fun update(i: Int, value:\
        \ Int) {\n        var idx = i + size\n        tree[idx] = value\n        while\
        \ (idx > 1) {\n            idx /= 2\n            tree[idx] = maxOf(tree[2 *\
        \ idx], tree[2 * idx + 1])\n        }\n    }\n\n    fun query(l: Int, r: Int):\
        \ Int {\n        var res = 0\n        var left = l + size\n        var right\
        \ = r + size\n        while (left <= right) {\n            if (left % 2 == 1)\
        \ res = maxOf(res, tree[left++])\n            if (right % 2 == 0) res = maxOf(res,\
        \ tree[right--])\n            left /= 2\n            right /= 2\n        }\n\
        \        return res\n    }\n}\n\nclass Solution {\n    fun getResults(queries:\
        \ Array<IntArray>): List<Boolean> {\n        var maxX = 0\n        for (q in\
        \ queries) {\n            if (q[1] > maxX) maxX = q[1]\n        }\n\n      \
        \  val st = SegmentTree(maxX + 1)\n        val obstacles = TreeSet<Int>()\n\
        \        obstacles.add(0)\n        val results = mutableListOf<Boolean>()\n\n\
        \        for (q in queries) {\n            val type = q[0]\n            if (type\
        \ == 1) {\n                val x = q[1]\n                val prevX = obstacles.lower(x)!!\n\
        \                val nextX = obstacles.higher(x)\n\n                st.update(x,\
        \ x - prevX)\n                if (nextX != null) {\n                    st.update(nextX,\
        \ nextX - x)\n                }\n                obstacles.add(x)\n        \
        \    } else {\n                val x = q[1]\n                val sz = q[2]\n\
        \                val lastObs = obstacles.floor(x)!!\n                val maxGap\
        \ = maxOf(st.query(0, x), x - lastObs)\n                results.add(maxGap >=\
        \ sz)\n            }\n        }\n        return results\n    }\n}"
      dart: "import 'dart:typed_data';\n\nclass Solution {\n  List<bool> getResults(List<List<int>>\
        \ queries) {\n    final int n = 50005;\n    final Int32List maxGapTree = Int32List(2\
        \ * n);\n    final Int32List obsMaxTree = Int32List.filled(2 * n, -1);\n   \
        \ final Int32List obsMinTree = Int32List.filled(2 * n, 1000000);\n\n    void\
        \ updateMax(Int32List tree, int i, int v) {\n      int idx = i + n;\n      tree[idx]\
        \ = v;\n      while (idx > 1) {\n        idx >>= 1;\n        int v1 = tree[idx\
        \ * 2];\n        int v2 = tree[idx * 2 + 1];\n        tree[idx] = v1 > v2 ?\
        \ v1 : v2;\n      }\n    }\n\n    void updateMin(Int32List tree, int i, int\
        \ v) {\n      int idx = i + n;\n      tree[idx] = v;\n      while (idx > 1)\
        \ {\n        idx >>= 1;\n        int v1 = tree[idx * 2];\n        int v2 = tree[idx\
        \ * 2 + 1];\n        tree[idx] = v1 < v2 ? v1 : v2;\n      }\n    }\n\n    int\
        \ queryMax(Int32List tree, int l, int r) {\n      int res = -1;\n      int left\
        \ = l + n;\n      int right = r + n;\n      while (left < right) {\n       \
        \ if (left % 2 == 1) {\n          if (tree[left] > res) res = tree[left];\n\
        \          left++;\n        }\n        if (right % 2 == 1) {\n          right--;\n\
        \          if (tree[right] > res) res = tree[right];\n        }\n        left\
        \ >>= 1;\n        right >>= 1;\n      }\n      return res;\n    }\n\n    int\
        \ queryMin(Int32List tree, int l, int r) {\n      int res = 1000000;\n     \
        \ int left = l + n;\n      int right = r + n;\n      while (left < right) {\n\
        \        if (left % 2 == 1) {\n          if (tree[left] < res) res = tree[left];\n\
        \          left++;\n        }\n        if (right % 2 == 1) {\n          right--;\n\
        \          if (tree[right] < res) res = tree[right];\n        }\n        left\
        \ >>= 1;\n        right >>= 1;\n      }\n      return res;\n    }\n\n    updateMax(obsMaxTree,\
        \ 0, 0);\n    updateMin(obsMinTree, 0, 0);\n\n    final List<bool> results =\
        \ [];\n    for (final q in queries) {\n      if (q[0] == 1) {\n        final\
        \ int x = q[1];\n        final int prev = queryMax(obsMaxTree, 0, x);\n    \
        \    final int next = queryMin(obsMinTree, x + 1, n);\n        updateMax(maxGapTree,\
        \ x, x - prev);\n        if (next != 1000000) {\n          updateMax(maxGapTree,\
        \ next, next - x);\n        }\n        updateMax(obsMaxTree, x, x);\n      \
        \  updateMin(obsMinTree, x, x);\n      } else {\n        final int x = q[1];\n\
        \        final int sz = q[2];\n        final int prev = queryMax(obsMaxTree,\
        \ 0, x + 1);\n        int bestGap = queryMax(maxGapTree, 0, prev + 1);\n   \
        \     if (bestGap < 0) bestGap = 0;\n        if (x - prev > bestGap) bestGap\
        \ = x - prev;\n        results.add(bestGap >= sz);\n      }\n    }\n    return\
        \ results;\n  }\n}"
      go: "func getResults(queries [][]int) []bool {\n\tn := 50005\n\tmaxGapTree :=\
        \ make([]int, 2*n)\n\tobsMaxTree := make([]int, 2*n)\n\tfor i := range obsMaxTree\
        \ {\n\t\tobsMaxTree[i] = -1\n\t}\n\tobsMinTree := make([]int, 2*n)\n\tfor i\
        \ := range obsMinTree {\n\t\tobsMinTree[i] = 1000000\n\t}\n\n\tupdate := func(tree\
        \ []int, i, v int, isMax bool) {\n\t\tidx := i + n\n\t\ttree[idx] = v\n\t\t\
        for idx > 1 {\n\t\t\tidx >>= 1\n\t\t\tif isMax {\n\t\t\t\tif tree[idx<<1] >\
        \ tree[idx<<1|1] {\n\t\t\t\t\ttree[idx] = tree[idx<<1]\n\t\t\t\t} else {\n\t\
        \t\t\t\ttree[idx] = tree[idx<<1|1]\n\t\t\t\t}\n\t\t\t} else {\n\t\t\t\tif tree[idx<<1]\
        \ < tree[idx<<1|1] {\n\t\t\t\t\ttree[idx] = tree[idx<<1]\n\t\t\t\t} else {\n\
        \t\t\t\t\ttree[idx] = tree[idx<<1|1]\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\n\tquery\
        \ := func(tree []int, l, r int, isMax bool) int {\n\t\tvar res int\n\t\tif isMax\
        \ {\n\t\t\tres = -1\n\t\t} else {\n\t\t\tres = 1000000\n\t\t}\n\t\tleft, right\
        \ := l+n, r+n\n\t\tfor left < right {\n\t\t\tif left&1 == 1 {\n\t\t\t\tif isMax\
        \ {\n\t\t\t\t\tif tree[left] > res { res = tree[left] }\n\t\t\t\t} else {\n\t\
        \t\t\t\tif tree[left] < res { res = tree[left] }\n\t\t\t\t}\n\t\t\t\tleft++\n\
        \t\t\t}\n\t\t\tif right&1 == 1 {\n\t\t\t\tright--\n\t\t\t\tif isMax {\n\t\t\t\
        \t\tif tree[right] > res { res = tree[right] }\n\t\t\t\t} else {\n\t\t\t\t\t\
        if tree[right] < res { res = tree[right] }\n\t\t\t\t}\n\t\t\t}\n\t\t\tleft >>=\
        \ 1\n\t\t\tright >>= 1\n\t\t}\n\t\treturn res\n\t}\n\n\tupdate(obsMaxTree, 0,\
        \ 0, true)\n\tupdate(obsMinTree, 0, 0, false)\n\n\tresults := make([]bool, 0)\n\
        \tfor _, q := range queries {\n\t\tif q[0] == 1 {\n\t\t\tx := q[1]\n\t\t\tprev\
        \ := query(obsMaxTree, 0, x, true)\n\t\t\tnext := query(obsMinTree, x+1, n,\
        \ false)\n\t\t\tupdate(maxGapTree, x, x-prev, true)\n\t\t\tif next != 1000000\
        \ {\n\t\t\t\tupdate(maxGapTree, next, next-x, true)\n\t\t\t}\n\t\t\tupdate(obsMaxTree,\
        \ x, x, true)\n\t\t\tupdate(obsMinTree, x, x, false)\n\t\t} else {\n\t\t\tx,\
        \ sz := q[1], q[2]\n\t\t\tprev := query(obsMaxTree, 0, x+1, true)\n\t\t\tmaxGapInTree\
        \ := query(maxGapTree, 0, prev+1, true)\n\t\t\tif maxGapInTree < 0 { maxGapInTree\
        \ = 0 }\n\t\t\tbestGap := maxGapInTree\n\t\t\tif x-prev > bestGap {\n\t\t\t\t\
        bestGap = x - prev\n\t\t\t}\n\t\t\tresults = append(results, bestGap >= sz)\n\
        \t\t}\n\t}\n\treturn results\n}"
      ruby: "def get_results(queries)\n  n = 50005\n  max_gap_tree = Array.new(2 * n,\
        \ 0)\n  obs_max_tree = Array.new(2 * n, -1)\n  obs_min_tree = Array.new(2 *\
        \ n, 1_000_000)\n\n  update_max = lambda do |tree, i, v|\n    idx = i + n\n\
        \    tree[idx] = v\n    while idx > 1\n      idx >>= 1\n      v1 = tree[idx\
        \ << 1]\n      v2 = tree[idx << 1 | 1]\n      tree[idx] = v1 > v2 ? v1 : v2\n\
        \    end\n  end\n\n  update_min = lambda do |tree, i, v|\n    idx = i + n\n\
        \    tree[idx] = v\n    while idx > 1\n      idx >>= 1\n      v1 = tree[idx\
        \ << 1]\n      v2 = tree[idx << 1 | 1]\n      tree[idx] = v1 < v2 ? v1 : v2\n\
        \    end\n  end\n\n  query_max = lambda do |tree, l, r|\n    res = -1\n    left\
        \ = l + n\n    right = r + n\n    while left < right\n      if left.odd?\n \
        \       val = tree[left]\n        res = val if val > res\n        left += 1\n\
        \      end\n      if right.odd?\n        right -= 1\n        val = tree[right]\n\
        \        res = val if val > res\n      end\n      left >>= 1\n      right >>=\
        \ 1\n    end\n    res\n  end\n\n  query_min = lambda do |tree, l, r|\n    res\
        \ = 1_000_000\n    left = l + n\n    right = r + n\n    while left < right\n\
        \      if left.odd?\n        val = tree[left]\n        res = val if val < res\n\
        \        left += 1\n      end\n      if right.odd?\n        right -= 1\n   \
        \     val = tree[right]\n        res = val if val < res\n      end\n      left\
        \ >>= 1\n      right >>= 1\n    end\n    res\n  end\n\n  update_max.call(obs_max_tree,\
        \ 0, 0)\n  update_min.call(obs_min_tree, 0, 0)\n\n  results = []\n  queries.each\
        \ do |q|\n    if q[0] == 1\n      x = q[1]\n      prev_obs = query_max.call(obs_max_tree,\
        \ 0, x)\n      next_obs = query_min.call(obs_min_tree, x + 1, n)\n      update_max.call(max_gap_tree,\
        \ x, x - prev_obs)\n      if next_obs != 1_000_000\n        update_max.call(max_gap_tree,\
        \ next_obs, next_obs - x)\n      end\n      update_max.call(obs_max_tree, x,\
        \ x)\n      update_min.call(obs_min_tree, x, x)\n    else\n      x, sz = q[1],\
        \ q[2]\n      prev_obs = query_max.call(obs_max_tree, 0, x + 1)\n      gap_in_tree\
        \ = query_max.call(max_gap_tree, 0, prev_obs + 1)\n      best_gap = gap_in_tree\
        \ > (x - prev_obs) ? gap_in_tree : (x - prev_obs)\n      results << (best_gap\
        \ >= sz)\n    end\n  end\n  results\nend"
      scala: "import scala.collection.mutable.ListBuffer\n\nobject Solution {\n  def\
        \ getResults(queries: Array[Array[Int]]): List[Boolean] = {\n    val n = 50005\n\
        \    val maxGapTree = Array.fill(2 * n)(0)\n    val obsMaxTree = Array.fill(2\
        \ * n)(-1)\n    val obsMinTree = Array.fill(2 * n)(1000000)\n\n    def updateMax(tree:\
        \ Array[Int], i: Int, v: Int): Unit = {\n      var idx = i + n\n      tree(idx)\
        \ = v\n      while (idx > 1) {\n        idx >>= 1\n        tree(idx) = Math.max(tree(2\
        \ * idx), tree(2 * idx + 1))\n      }\n    }\n\n    def updateMin(tree: Array[Int],\
        \ i: Int, v: Int): Unit = {\n      var idx = i + n\n      tree(idx) = v\n  \
        \    while (idx > 1) {\n        idx >>= 1\n        tree(idx) = Math.min(tree(2\
        \ * idx), tree(2 * idx + 1))\n      }\n    }\n\n    def queryMax(tree: Array[Int],\
        \ l: Int, r: Int): Int = {\n      var res = -1\n      var left = l + n\n   \
        \   var right = r + n\n      while (left < right) {\n        if (left % 2 ==\
        \ 1) {\n          res = Math.max(res, tree(left))\n          left += 1\n   \
        \     }\n        if (right % 2 == 1) {\n          right -= 1\n          res\
        \ = Math.max(res, tree(right))\n        }\n        left >>= 1\n        right\
        \ >>= 1\n      }\n      res\n    }\n\n    def queryMin(tree: Array[Int], l:\
        \ Int, r: Int): Int = {\n      var res = 1000000\n      var left = l + n\n \
        \     var right = r + n\n      while (left < right) {\n        if (left % 2\
        \ == 1) {\n          res = Math.min(res, tree(left))\n          left += 1\n\
        \        }\n        if (right % 2 == 1) {\n          right -= 1\n          res\
        \ = Math.min(res, tree(right))\n        }\n        left >>= 1\n        right\
        \ >>= 1\n      }\n      res\n    }\n\n    updateMax(obsMaxTree, 0, 0)\n    updateMin(obsMinTree,\
        \ 0, 0)\n\n    val results = new ListBuffer[Boolean]()\n    for (q <- queries)\
        \ {\n      if (q(0) == 1) {\n        val x = q(1)\n        val prev = queryMax(obsMaxTree,\
        \ 0, x)\n        val next = queryMin(obsMinTree, x + 1, n)\n        updateMax(maxGapTree,\
        \ x, x - prev)\n        if (next != 1000000) {\n          updateMax(maxGapTree,\
        \ next, next - x)\n        }\n        updateMax(obsMaxTree, x, x)\n        updateMin(obsMinTree,\
        \ x, x)\n      } else {\n        val x = q(1)\n        val sz = q(2)\n     \
        \   val prev = queryMax(obsMaxTree, 0, x + 1)\n        val bestGap = Math.max(queryMax(maxGapTree,\
        \ 0, prev + 1), x - prev)\n        results += (bestGap >= sz)\n      }\n   \
        \ }\n    results.toList\n  }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn get_results(queries:\
        \ Vec<Vec<i32>>) -> Vec<bool> {\n        let mut p = vec![0];\n        for q\
        \ in &queries {\n            if q[0] == 1 {\n                p.push(q[1]);\n\
        \            }\n        }\n        p.sort();\n        p.dedup();\n\n       \
        \ let mut pos_to_idx = HashMap::new();\n        for (i, &val) in p.iter().enumerate()\
        \ {\n            pos_to_idx.insert(val, i);\n        }\n\n        let k = p.len();\n\
        \        let mut next = vec![0; k];\n        let mut prev = vec![0; k];\n  \
        \      for i in 0..k {\n            next[i] = i + 1;\n            prev[i] =\
        \ i as i32 - 1;\n        }\n\n        let mut dsu = (0..k).collect::<Vec<usize>>();\n\
        \        fn find(dsu: &mut Vec<usize>, mut i: usize) -> usize {\n          \
        \  let mut root = i;\n            while dsu[root] != root {\n              \
        \  root = dsu[root];\n            }\n            while dsu[i] != root {\n  \
        \              let next_idx = dsu[i];\n                dsu[i] = root;\n    \
        \            i = next_idx;\n            }\n            root\n        }\n\n \
        \       let mut tree = SegmentTree::new(k);\n        for i in 1..k {\n     \
        \       tree.update(i, p[i] - p[i - 1]);\n        }\n\n        let mut results\
        \ = Vec::with_capacity(queries.len());\n        for q in queries.iter().rev()\
        \ {\n            if q[0] == 1 {\n                let x = q[1];\n           \
        \     let j = *pos_to_idx.get(&x).unwrap();\n                let pr = prev[j]\
        \ as usize;\n                let nx = next[j];\n\n                if nx < k\
        \ {\n                    tree.update(nx, p[nx] - p[pr]);\n                 \
        \   prev[nx] = pr as i32;\n                }\n                tree.update(j,\
        \ 0);\n                next[pr] = nx;\n                dsu[j] = find(&mut dsu,\
        \ pr);\n            } else {\n                let x = q[1];\n              \
        \  let sz = q[2];\n                let j = p.partition_point(|&val| val <= x)\
        \ - 1;\n                let idx = find(&mut dsu, j);\n                let ak\
        \ = p[idx];\n                let max_gap = std::cmp::max(tree.query(0, idx),\
        \ x - ak);\n                results.push(max_gap >= sz);\n            }\n  \
        \      }\n        results.reverse();\n        results\n    }\n}\n\nstruct SegmentTree\
        \ {\n    n: usize,\n    tree: Vec<i32>,\n}\n\nimpl SegmentTree {\n    fn new(n:\
        \ usize) -> Self {\n        let mut m = 1;\n        while m < n {\n        \
        \    m *= 2;\n        }\n        Self {\n            n: m,\n            tree:\
        \ vec![0; 2 * m],\n        }\n    }\n    fn update(&mut self, mut i: usize,\
        \ val: i32) {\n        i += self.n;\n        self.tree[i] = val;\n        while\
        \ i > 1 {\n            i /= 2;\n            self.tree[i] = std::cmp::max(self.tree[2\
        \ * i], self.tree[2 * i + 1]);\n        }\n    }\n    fn query(&self, mut l:\
        \ usize, mut r: usize) -> i32 {\n        l += self.n;\n        r += self.n;\n\
        \        let mut res = 0;\n        while l <= r {\n            if l % 2 == 1\
        \ {\n                res = std::cmp::max(res, self.tree[l]);\n             \
        \   l += 1;\n            }\n            if r % 2 == 0 {\n                res\
        \ = std::cmp::max(res, self.tree[r]);\n                r -= 1;\n           \
        \ }\n            l /= 2;\n            r /= 2;\n        }\n        res\n    }\n\
        }"
      racket: "(define/contract (get-results queries)\n  (-> (listof (listof exact-integer?))\
        \ (listof boolean?))\n  (let* ([p-list (sort (remove-duplicates (cons 0 (map\
        \ second (filter (lambda (q) (= (first q) 1)) queries)))) <)]\n         [p (list->vector\
        \ p-list)]\n         [p-len (vector-length p)]\n         [pos-to-idx (make-hash)]\n\
        \         [_ (for ([i (in-range p-len)]) (hash-set! pos-to-idx (vector-ref p\
        \ i) i))]\n         [next (make-vector p-len p-len)]\n         [prev (make-vector\
        \ p-len -1)]\n         [_ (for ([i (in-range p-len)])\n              (when (<\
        \ i (- p-len 1)) (vector-set! next i (+ i 1)))\n              (when (> i 0)\
        \ (vector-set! prev i (- i 1))))]\n         [dsu (make-vector p-len 0)]\n  \
        \       [_ (for ([i (in-range p-len)]) (vector-set! dsu i i))]\n         [dsu-find\
        \ (lambda (dsu i)\n                     (let loop-root ([curr i])\n        \
        \               (let ([parent (vector-ref dsu curr)])\n                    \
        \     (if (= parent curr) curr (loop-root parent)))))]\n         [dsu-compress\
        \ (lambda (dsu i root)\n                         (let loop-compress ([curr i])\n\
        \                           (let ([parent (vector-ref dsu curr)])\n        \
        \                     (if (= parent root) root\n                           \
        \      (begin (vector-set! dsu curr root) (loop-compress parent))))))]\n   \
        \      [find-and-compress (lambda (dsu i)\n                              (let\
        \ ([root (dsu-find dsu i)])\n                                (dsu-compress dsu\
        \ i root) root))]\n         [m (let loop-m ([acc 1]) (if (< acc p-len) (loop-m\
        \ (* acc 2)) acc))]\n         [tree (make-vector (* 2 m) 0)]\n         [tree-update\
        \ (lambda (tree m i val)\n                        (let loop-up ([idx (+ i m)]\
        \ [v val])\n                          (vector-set! tree idx v)\n           \
        \               (when (> idx 1)\n                            (let* ([p-idx (quotient\
        \ idx 2)]\n                                   [new-val (max (vector-ref tree\
        \ (* 2 p-idx)) (vector-ref tree (+ 1 (* 2 p-idx))))])\n                    \
        \          (loop-up p-idx new-val)))))]\n         [tree-query (lambda (tree\
        \ m l r)\n                       (let loop-q ([ql (+ l m)] [qr (+ r m)] [res\
        \ 0])\n                         (if (<= ql qr)\n                           \
        \  (let* ([res1 (if (= (remainder ql 2) 1) (max res (vector-ref tree ql)) res)]\n\
        \                                    [ql1 (if (= (remainder ql 2) 1) (+ ql 1)\
        \ ql)]\n                                    [res2 (if (= (remainder qr 2) 0)\
        \ (max res1 (vector-ref tree qr)) res1)]\n                                 \
        \   [qr2 (if (= (remainder qr 2) 0) (- qr 1) qr)])\n                       \
        \        (loop-q (quotient ql1 2) (quotient qr2 2) res2))\n                \
        \             res))])\n         [_ (for ([i (in-range 1 p-len)]) (tree-update\
        \ tree m i (- (vector-ref p i) (vector-ref p (- i 1)))))]\n         [results\
        \ '()])\n    (for ([q (reverse queries)])\n      (if (= (first q) 1)\n     \
        \     (let* ([x (second q)]\n                 [j (hash-ref pos-to-idx x)]\n\
        \                 [pr (vector-ref prev j)]\n                 [nx (vector-ref\
        \ next j)])\n            (when (< nx p-len)\n              (tree-update tree\
        \ m nx (- (vector-ref p nx) (vector-ref p pr)))\n              (vector-set!\
        \ prev nx pr))\n            (tree-update tree m j 0)\n            (vector-set!\
        \ next pr nx)\n            (vector-set! dsu j (find-and-compress dsu pr)))\n\
        \          (let* ([x (second q)]\n                 [sz (third q)]\n        \
        \         [j (let loop-ub ([low 0] [high p-len])\n                      (if\
        \ (< low high)\n                          (let ([mid (quotient (+ low high)\
        \ 2)])\n                            (if (<= (vector-ref p mid) x) (loop-ub (+\
        \ mid 1) high) (loop-ub low mid)))\n                          (- low 1)))]\n\
        \                 [idx (find-and-compress dsu j)]\n                 [ak (vector-ref\
        \ p idx)]\n                 [max-gap (max (tree-query tree m 0 idx) (- x ak))])\n\
        \            (set! results (cons (>= max-gap sz) results)))))\n    results))"
      erlang: "-spec get_results(Queries :: [[integer()]]) -> [boolean()].\nget_results(Queries)\
        \ ->\n    PList = lists:usort([0 | [X || [Type, X | _] <- Queries, Type =:=\
        \ 1]]),\n    PLen = length(PList),\n    PArray = array:from_list(PList),\n \
        \   PosToIdx = maps:from_list(lists:zip(PList, lists:seq(0, PLen - 1))),\n \
        \   Next = array:from_list(lists:seq(1, PLen)),\n    Prev = array:from_list([-1\
        \ | lists:seq(0, PLen - 2)]),\n    Dsu = array:from_list(lists:seq(0, PLen -\
        \ 1)),\n    M = find_m(PLen, 1),\n    Tree0 = array:new(2 * M, {default, 0}),\n\
        \    Tree = fill_tree(Tree0, PList, M, 1),\n    process_queries(lists:reverse(Queries),\
        \ PArray, PLen, PosToIdx, Next, Prev, Dsu, Tree, M, []).\n\nfind_m(N, M) when\
        \ M < N -> find_m(N, M * 2);\nfind_m(_, M) -> M.\n\nfill_tree(Tree, [_ | []],\
        \ _M, _Idx) -> Tree;\nfill_tree(Tree, [P1 | [P2 | Rest]], M, Idx) ->\n    NewTree\
        \ = update_tree(Tree, Idx, P2 - P1, M),\n    fill_tree(NewTree, [P2 | Rest],\
        \ M, Idx + 1).\n\nupdate_tree(Tree, I, Val, M) ->\n    Idx = I + M,\n    Tree1\
        \ = array:set(Idx, Val, Tree),\n    update_up(Tree1, Idx div 2).\n\nupdate_up(Tree,\
        \ 0) -> Tree;\nupdate_up(Tree, P) ->\n    V1 = array:get(P * 2, Tree),\n   \
        \ V2 = array:get(P * 2 + 1, Tree),\n    Max = erlang:max(V1, V2),\n    case\
        \ array:get(P, Tree) of\n        Max -> Tree;\n        _ -> update_up(array:set(P,\
        \ Max, Tree), P div 2)\n    end.\n\nquery_tree(Tree, L, R, M) ->\n    query_tree_loop(Tree,\
        \ L + M, R + M, 0).\n\nquery_tree_loop(Tree, L, R, Res) when L =< R ->\n   \
        \ {NewL, Res1} = if L rem 2 =:= 1 -> {L + 1, erlang:max(Res, array:get(L, Tree))};\n\
        \                      true -> {L, Res}\n                   end,\n    {NewR,\
        \ Res2} = if R rem 2 =:= 0 -> {R - 1, erlang:max(Res1, array:get(R, Tree))};\n\
        \                      true -> {R, Res1}\n                   end,\n    query_tree_loop(Tree,\
        \ NewL div 2, NewR div 2, Res2);\nquery_tree_loop(_Tree, _L, _R, Res) -> Res.\n\
        \nfind_dsu(Dsu, I) ->\n    Root = find_root(Dsu, I),\n    {Root, compress_dsu(Dsu,\
        \ I, Root)}.\n\nfind_root(Dsu, I) ->\n    case array:get(I, Dsu) of\n      \
        \  I -> I;\n        Next -> find_root(Dsu, Next)\n    end.\n\ncompress_dsu(Dsu,\
        \ I, Root) ->\n    case array:get(I, Dsu) of\n        Root -> Dsu;\n       \
        \ Next -> compress_dsu(array:set(I, Root, Dsu), Next, Root)\n    end.\n\nupper_bound(Arr,\
        \ Val, Low, High) ->\n    if Low >= High -> Low;\n       true ->\n         \
        \  Mid = (Low + High) div 2,\n           MidVal = array:get(Mid, Arr),\n   \
        \        if MidVal =< Val -> upper_bound(Arr, Val, Mid + 1, High);\n       \
        \       true -> upper_bound(Arr, Val, Low, Mid)\n           end\n    end.\n\n\
        process_queries([], _, _, _, _, _, _, _, _, Acc) -> Acc;\nprocess_queries([[1,\
        \ X] | Rest], PArr, PLen, PosToIdx, Next, Prev, Dsu, Tree, M, Acc) ->\n    J\
        \ = maps:get(X, PosToIdx),\n    Pr = array:get(J, Prev),\n    Nx = array:get(J,\
        \ Next),\n    Tree1 = if Nx < PLen ->\n                   Pnx = array:get(Nx,\
        \ PArr),\n                   Ppr = array:get(Pr, PArr),\n                  \
        \ update_tree(Tree, Nx, Pnx - Ppr, M);\n               true -> Tree\n      \
        \      end,\n    Tree2 = update_tree(Tree1, J, 0, M),\n    Next1 = array:set(Pr,\
        \ Nx, Next),\n    Prev1 = if Nx < PLen -> array:set(Nx, Pr, Prev); true -> Prev\
        \ end,\n    {RootPr, Dsu1} = find_dsu(Dsu, Pr),\n    Dsu2 = array:set(J, RootPr,\
        \ Dsu1),\n    process_queries(Rest, PArr, PLen, PosToIdx, Next1, Prev1, Dsu2,\
        \ Tree2, M, Acc);\nprocess_queries([[2, X, Sz] | Rest], PArr, PLen, PosToIdx,\
        \ Next, Prev, Dsu, Tree, M, Acc) ->\n    UB = upper_bound(PArr, X, 0, PLen),\n\
        \    J = UB - 1,\n    {Idx, Dsu1} = find_dsu(Dsu, J),\n    Ak = array:get(Idx,\
        \ PArr),\n    MaxGap = erlang:max(query_tree(Tree, 0, Idx, M), X - Ak),\n  \
        \  process_queries(Rest, PArr, PLen, PosToIdx, Next, Prev, Dsu1, Tree, M, [(MaxGap\
        \ >= Sz) | Acc])."
      elixir: "defmodule Solution do\n  @spec get_results(queries :: [[integer]]) ::\
        \ [boolean]\n  def get_results(queries) do\n    p_list = queries\n    |> Enum.filter(fn\
        \ [type | _] -> type == 1 end)\n    |> Enum.map(fn [_, x] -> x end)\n    |>\
        \ (fn x_list -> [0 | x_list] end).()\n    |> Enum.sort()\n    |> Enum.dedup()\n\
        \n    p_len = length(p_list)\n    p_array = :array.from_list(p_list)\n    pos_to_idx\
        \ = p_list |> Enum.with_index() |> Map.new()\n\n    m = find_m(p_len, 1)\n \
        \   tree = :array.new(2 * m, default: 0)\n    tree = fill_tree(tree, p_list,\
        \ m, 1)\n\n    next_arr = :array.from_list(Enum.to_list(1..p_len))\n    prev_arr\
        \ = :array.from_list([-1 | Enum.to_list(0..(p_len - 2))])\n    dsu = :array.from_list(Enum.to_list(0..(p_len\
        \ - 1)))\n\n    process_queries(Enum.reverse(queries), p_array, p_len, pos_to_idx,\
        \ next_arr, prev_arr, dsu, tree, m, [])\n  end\n\n  defp find_m(n, m) when m\
        \ < n, do: find_m(n, m * 2)\n  defp find_m(_, m), do: m\n\n  defp fill_tree(tree,\
        \ [_], _m, _idx), do: tree\n  defp fill_tree(tree, [p1 | [p2 | rest]], m, idx)\
        \ do\n    tree = update_tree(tree, idx, p2 - p1, m)\n    fill_tree(tree, [p2\
        \ | rest], m, idx + 1)\n  end\n\n  defp update_tree(tree, i, val, m) do\n  \
        \  idx = i + m\n    tree = :array.set(idx, val, tree)\n    update_up(tree, div(idx,\
        \ 2))\n  end\n\n  defp update_up(tree, 0), do: tree\n  defp update_up(tree,\
        \ p) do\n    v1 = :array.get(p * 2, tree)\n    v2 = :array.get(p * 2 + 1, tree)\n\
        \    max_v = max(v1, v2)\n    if :array.get(p, tree) == max_v do\n      tree\n\
        \    else\n      update_up(:array.set(p, max_v, tree), div(p, 2))\n    end\n\
        \  end\n\n  defp query_tree(tree, l, r, m), do: query_tree_loop(tree, l + m,\
        \ r + m, 0)\n  defp query_tree_loop(_, l, r, res) when l > r, do: res\n  defp\
        \ query_tree_loop(tree, l, r, res) do\n    {l, res} = if rem(l, 2) == 1, do:\
        \ {l + 1, max(res, :array.get(l, tree))}, else: {l, res}\n    {r, res} = if\
        \ rem(r, 2) == 0, do: {r - 1, max(res, :array.get(r, tree))}, else: {r, res}\n\
        \    query_tree_loop(tree, div(l, 2), div(r, 2), res)\n  end\n\n  defp find_dsu(dsu,\
        \ i) do\n    root = find_root(dsu, i)\n    {root, compress_dsu(dsu, i, root)}\n\
        \  end\n  defp find_root(dsu, i) do\n    next = :array.get(i, dsu)\n    if next\
        \ == i, do: i, else: find_root(dsu, next)\n  end\n  defp compress_dsu(dsu, i,\
        \ root) do\n    next = :array.get(i, dsu)\n    if next == root, do: dsu, else:\
        \ compress_dsu(:array.set(i, root, dsu), next, root)\n  end\n\n  defp upper_bound(arr,\
        \ val, low, high) do\n    if low >= high do\n      low\n    else\n      mid\
        \ = div(low + high, 2)\n      if :array.get(mid, arr) <= val, do: upper_bound(arr,\
        \ val, mid + 1, high), else: upper_bound(arr, val, low, mid)\n    end\n  end\n\
        \n  defp process_queries([], _, _, _, _, _, _, _, _, acc), do: acc\n  defp process_queries([[1,\
        \ x] | rest], p_arr, p_len, pos_to_idx, next_arr, prev_arr, dsu, tree, m, acc)\
        \ do\n    j = Map.get(pos_to_idx, x)\n    pr = :array.get(j, prev_arr)\n   \
        \ nx = :array.get(j, next_arr)\n    tree = if nx < p_len do\n      update_tree(tree,\
        \ nx, :array.get(nx, p_arr) - :array.get(pr, p_arr), m)\n    else\n      tree\n\
        \    end\n    tree = update_tree(tree, j, 0, m)\n    next_arr = :array.set(pr,\
        \ nx, next_arr)\n    prev_arr = if nx < p_len, do: :array.set(nx, pr, prev_arr),\
        \ else: prev_arr\n    {root_pr, dsu} = find_dsu(dsu, pr)\n    dsu = :array.set(j,\
        \ root_pr, dsu)\n    process_queries(rest, p_arr, p_len, pos_to_idx, next_arr,\
        \ prev_arr, dsu, tree, m, acc)\n  end\n  defp process_queries([[2, x, sz] |\
        \ rest], p_arr, p_len, pos_to_idx, next_arr, prev_arr, dsu, tree, m, acc) do\n\
        \    ub = upper_bound(p_arr, x, 0, p_len)\n    j = ub - 1\n    {idx, dsu} =\
        \ find_dsu(dsu, j)\n    ak = :array.get(idx, p_arr)\n    max_gap = max(query_tree(tree,\
        \ 0, idx, m), x - ak)\n    process_queries(rest, p_arr, p_len, pos_to_idx, next_arr,\
        \ prev_arr, dsu, tree, m, [max_gap >= sz | acc])\n  end\nend"
    approach: The problem asks to find the maximum gap between obstacles within a dynamic
      environment. We maintain a set of obstacle locations, starting with the origin
      {0}. A segment tree is used to store the length of the gap ending at each obstacle
      position $x_i$, specifically $tree[x_i] = x_i - x_{i-1}$, where $x_{i-1}$ is the
      obstacle immediately preceding $x_i$. This setup allows us to handle type 1 queries
      by finding the predecessor and successor of the new obstacle $x$, splitting the
      existing gap into two smaller ones, and updating the segment tree accordingly
      in $O(\log M)$ time.
    time_complexity: O(Q(log M + log Q)) where Q is the number of queries and M is the
      maximum coordinate value (50,000). For each query, we perform a search in a sorted
      container (O(log Q)) and a point update or range maximum query on a segment tree
      (O(log M)).
    space_complexity: O(M + Q) to store the segment tree and the list of obstacles,
      where M is the maximum coordinate on the number line and Q is the number of queries.
    elapsed_time: 922.8368775844574
    model: gemini-3-flash-preview
    generated_at: '2026-05-30 02:43:40 '
---

## Problem #3161: Block Placement Queries

**Difficulty:** Hard

**Topics:** Array, Binary Search, Binary Indexed Tree, Segment Tree

## Problem Description

<p>There exists an infinite number line, with its origin at 0 and extending towards the <strong>positive</strong> x-axis.</p>

<p>You are given a 2D array <code>queries</code>, which contains two types of queries:</p>

<ol>
	<li>For a query of type 1, <code>queries[i] = [1, x]</code>. Build an obstacle at distance <code>x</code> from the origin. It is guaranteed that there is <strong>no</strong> obstacle at distance <code>x</code> when the query is asked.</li>
	<li>For a query of type 2, <code>queries[i] = [2, x, sz]</code>. Check if it is possible to place a block of size <code>sz</code> <em>anywhere</em> in the range <code>[0, x]</code> on the line, such that the block <strong>entirely</strong> lies in the range <code>[0, x]</code>. A block <strong>cannot </strong>be placed if it intersects with any obstacle, but it may touch it. Note that you do<strong> not</strong> actually place the block. Queries are separate.</li>
</ol>

<p>Return a boolean array <code>results</code>, where <code>results[i]</code> is <code>true</code> if you can place the block specified in the <code>i<sup>th</sup></code> query of type 2, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[false,true,true]</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/04/22/example0block.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 309px; height: 129px;" /></strong></p>

<p>For query 0, place an obstacle at <code>x = 2</code>. A block of size at most 2 can be placed before <code>x = 3</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">queries = </span>[[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]<!-- notionvc: 4a471445-5af1-4d72-b11b-94d351a2c8e9 --></p>

<p><strong>Output:</strong> [true,true,false]</p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/04/22/example1block.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 310px; height: 130px;" /></strong></p>

<ul>
	<li>Place an obstacle at <code>x = 7</code> for query 0. A block of size at most 7 can be placed before <code>x = 7</code>.</li>
	<li>Place an obstacle at <code>x = 2</code> for query 2. Now, a block of size at most 5 can be placed before <code>x = 7</code>, and a block of size at most 2 before <code>x = 2</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= queries.length &lt;= 15 * 10<sup>4</sup></code></li>
	<li><code>2 &lt;= queries[i].length &lt;= 3</code></li>
	<li><code>1 &lt;= queries[i][0] &lt;= 2</code></li>
	<li><code>1 &lt;= x, sz &lt;= min(5 * 10<sup>4</sup>, 3 * queries.length)</code></li>
	<li>The input is generated such that for queries of type 1, no obstacle exists at distance <code>x</code> when the query is asked.</li>
	<li>The input is generated such that there is at least one query of type 2.</li>
</ul>


## Hints

1. Let `d[x]` be the distance of the next obstacle after `x`.

2. For each query of type 2, we just need to check if `max(d[0], d[1], d[2], …d[x - sz]) > sz`.

3. Use segment tree to maintain `d[x]`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to find the maximum gap between obstacles within a dynamic environment. We maintain a set of obstacle locations, starting with the origin {0}. A segment tree is used to store the length of the gap ending at each obstacle position $x_i$, specifically $tree[x_i] = x_i - x_{i-1}$, where $x_{i-1}$ is the obstacle immediately preceding $x_i$. This setup allows us to handle type 1 queries by finding the predecessor and successor of the new obstacle $x$, splitting the existing gap into two smaller ones, and updating the segment tree accordingly in $O(\log M)$ time.

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
class SegmentTree {
    int n;
    vector<int> tree;
public:
    SegmentTree(int size) {
        n = 1;
        while (n < size) n *= 2;
        tree.assign(2 * n, 0);
    }
    void update(int i, int val) {
        i += n;
        tree[i] = val;
        while (i > 1) {
            i /= 2;
            tree[i] = max(tree[2 * i], tree[2 * i + 1]);
        }
    }
    int query(int l, int r) {
        int res = 0;
        l += n;
        r += n;
        while (l < r) {
            if (l % 2 == 1) res = max(res, tree[l++]);
            if (r % 2 == 1) res = max(res, tree[--r]);
            l /= 2;
            r /= 2;
        }
        return res;
    }
};

class Solution {
public:
    vector<bool> getResults(vector<vector<int>>& queries) {
        int max_x = 0;
        for (const auto& q : queries) if (q[1] > max_x) max_x = q[1];
        SegmentTree st(max_x + 1);
        set<int> obstacles;
        obstacles.insert(0);
        vector<bool> results;
        for (const auto& q : queries) {
            if (q[0] == 1) {
                int x = q[1];
                auto it = obstacles.lower_bound(x);
                int x_prev = *prev(it);
                if (it != obstacles.end()) {
                    int x_next = *it;
                    st.update(x_next, x_next - x);
                }
                st.update(x, x - x_prev);
                obstacles.insert(x);
            } else {
                int x = q[1], sz = q[2];
                int x_prev = *prev(obstacles.upper_bound(x));
                int max_gap = max(st.query(0, x_prev + 1), x - x_prev);
                results.push_back(max_gap >= sz);
            }
        }
        return results;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class SegmentTree {
    int n;
    int[] tree;
    public SegmentTree(int size) {
        n = 1;
        while (n < size) n *= 2;
        tree = new int[2 * n];
    }
    public void update(int i, int val) {
        i += n;
        tree[i] = val;
        while (i > 1) {
            i /= 2;
            tree[i] = Math.max(tree[2 * i], tree[2 * i + 1]);
        }
    }
    public int query(int l, int r) {
        int res = 0;
        l += n;
        r += n;
        while (l < r) {
            if (l % 2 == 1) res = Math.max(res, tree[l++]);
            if (r % 2 == 1) res = Math.max(res, tree[--r]);
            l /= 2;
            r /= 2;
        }
        return res;
    }
}

class Solution {
    public List<Boolean> getResults(int[][] queries) {
        int maxX = 0;
        for (int[] q : queries) if (q[1] > maxX) maxX = q[1];
        SegmentTree st = new SegmentTree(maxX + 1);
        TreeSet<Integer> obstacles = new TreeSet<>();
        obstacles.add(0);
        List<Boolean> results = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) {
                int x = q[1];
                Integer xNext = obstacles.higher(x);
                int xPrev = obstacles.lower(x);
                if (xNext != null) st.update(xNext, xNext - x);
                st.update(x, x - xPrev);
                obstacles.add(x);
            } else {
                int x = q[1], sz = q[2];
                int xPrev = obstacles.floor(x);
                int maxGap = Math.max(st.query(0, xPrev + 1), x - xPrev);
                results.add(maxGap >= sz);
            }
        }
        return results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import bisect

class SegmentTree:
    def __init__(self, size):
        self.n = 1
        while self.n < size: self.n *= 2
        self.tree = [0] * (2 * self.n)

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

class Solution(object):
    def getResults(self, queries):
        max_x = 0
        for q in queries: 
            if q[1] > max_x: max_x = q[1]
        st = SegmentTree(max_x + 1)
        obstacles = [0]
        ans = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = bisect.bisect_left(obstacles, x)
                x_prev = obstacles[idx - 1]
                if idx < len(obstacles):
                    x_next = obstacles[idx]
                    st.update(x_next, x_next - x)
                st.update(x, x - x_prev)
                bisect.insort(obstacles, x)
            else:
                x, sz = q[1], q[2]
                idx = bisect.bisect_right(obstacles, x)
                x_p = obstacles[idx - 1]
                best = st.query(0, x_p + 1)
                if x - x_p > best: best = x - x_p
                ans.append(best >= sz)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        M = 50005
        n = 1 << 16
        tree = [0] * (2 * n)
        bit = [0] * (M + 1)
        total_obstacles = 1

        def update_tree(i, val):
            i += n
            tree[i] = val
            while i > 1:
                left, right = tree[i], tree[i ^ 1]
                tree[i >> 1] = left if left > right else right
                i >>= 1

        def query_tree(l, r):
            res = 0
            l += n
            r += n
            while l < r:
                if l & 1:
                    if tree[l] > res: res = tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    if tree[r] > res: res = tree[r]
                l >>= 1
                r >>= 1
            return res

        def update_bit(i, delta):
            i += 1
            while i <= M:
                bit[i] += delta
                i += i & -i

        def query_bit(i):
            i += 1
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def find_kth(k):
            idx = 0
            for i in [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]:
                if idx + i <= M and bit[idx + i] < k:
                    idx += i
                    k -= bit[idx]
            return idx

        update_bit(0, 1)
        results = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                k = query_bit(x - 1)
                p = find_kth(k)
                next_obs = find_kth(k + 1) if k < total_obstacles else -1
                update_tree(x, x - p)
                if next_obs != -1:
                    update_tree(next_obs, next_obs - x)
                update_bit(x, 1)
                total_obstacles += 1
            else:
                x, sz = q[1], q[2]
                k = query_bit(x)
                p = find_kth(k)
                max_gap = query_tree(0, p + 1)
                if x - p > max_gap:
                    max_gap = x - p
                results.append(max_gap >= sz)
        return results
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>

void updateTree(int i, int val, int* tree, int n) {
    i += n;
    tree[i] = val;
    while (i > 1) {
        tree[i >> 1] = (tree[i] > tree[i ^ 1]) ? tree[i] : tree[i ^ 1];
        i >>= 1;
    }
}

int queryTree(int l, int r, int* tree, int n) {
    int res = 0;
    l += n;
    r += n;
    while (l < r) {
        if (l & 1) {
            if (tree[l] > res) res = tree[l];
            l++;
        }
        if (r & 1) {
            r--;
            if (tree[r] > res) res = tree[r];
        }
        l >>= 1;
        r >>= 1;
    }
    return res;
}

void updateBit(int i, int delta, int* bit, int M) {
    i++;
    while (i <= M) {
        bit[i] += delta;
        i += i & -i;
    }
}

int queryBit(int i, int* bit) {
    i++;
    int res = 0;
    while (i > 0) {
        res += bit[i];
        i -= i & -i;
    }
    return res;
}

int findKth(int k, int* bit, int M) {
    int idx = 0;
    for (int i = 1 << 15; i > 0; i >>= 1) {
        if (idx + i <= M && bit[idx + i] < k) {
            idx += i;
            k -= bit[idx];
        }
    }
    return idx;
}

bool* getResults(int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int M = 50001;
    int n = 1 << 16;
    int* tree = (int*)calloc(2 * n, sizeof(int));
    int* bit = (int*)calloc(M + 1, sizeof(int));
    int total_obstacles = 1;
    updateBit(0, 1, bit, M);

    bool* results = (bool*)malloc(queriesSize * sizeof(bool));
    int resIdx = 0;

    for (int i = 0; i < queriesSize; i++) {
        if (queries[i][0] == 1) {
            int x = queries[i][1];
            int k = queryBit(x - 1, bit);
            int p = findKth(k, bit, M);
            int next_obs = (k < total_obstacles) ? findKth(k + 1, bit, M) : -1;
            updateTree(x, x - p, tree, n);
            if (next_obs != -1) updateTree(next_obs, next_obs - x, tree, n);
            updateBit(x, 1, bit, M);
            total_obstacles++;
        } else {
            int x = queries[i][1];
            int sz = queries[i][2];
            int k = queryBit(x, bit);
            int p = findKth(k, bit, M);
            int maxGap = queryTree(0, p + 1, tree, n);
            if (x - p > maxGap) maxGap = x - p;
            results[resIdx++] = (maxGap >= sz);
        }
    }

    free(tree);
    free(bit);
    *returnSize = resIdx;
    return results;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public IList<bool> GetResults(int[][] queries) {
        int M = 50001;
        int n = 1 << 16;
        int[] tree = new int[2 * n];
        int[] bit = new int[M + 1];
        int total_obstacles = 1;

        void UpdateTree(int i, int val) {
            i += n;
            tree[i] = val;
            while (i > 1) {
                tree[i >> 1] = Math.Max(tree[i], tree[i ^ 1]);
                i >>= 1;
            }
        }

        int QueryTree(int l, int r) {
            int res = 0;
            l += n;
            r += n;
            while (l < r) {
                if ((l & 1) == 1) res = Math.Max(res, tree[l++]);
                if ((r & 1) == 1) res = Math.Max(res, tree[--r]);
                l >>= 1;
                r >>= 1;
            }
            return res;
        }

        void UpdateBit(int i, int delta) {
            i++;
            while (i <= M) {
                bit[i] += delta;
                i += i & -i;
            }
        }

        int QueryBit(int i) {
            i++;
            int res = 0;
            while (i > 0) {
                res += bit[i];
                i -= i & -i;
            }
            return res;
        }

        int FindKth(int k) {
            int idx = 0;
            for (int i = 1 << 15; i > 0; i >>= 1) {
                if (idx + i <= M && bit[idx + i] < k) {
                    idx += i;
                    k -= bit[idx];
                }
            }
            return idx;
        }

        UpdateBit(0, 1);
        List<bool> results = new List<bool>();
        foreach (var q in queries) {
            if (q[0] == 1) {
                int x = q[1];
                int k = QueryBit(x - 1);
                int p = FindKth(k);
                int next_obs = (k < total_obstacles) ? FindKth(k + 1) : -1;
                UpdateTree(x, x - p);
                if (next_obs != -1) UpdateTree(next_obs, next_obs - x);
                UpdateBit(x, 1);
                total_obstacles++;
            } else {
                int x = q[1], sz = q[2];
                int k = QueryBit(x);
                int p = FindKth(k);
                int maxGap = Math.Max(QueryTree(0, p + 1), x - p);
                results.Add(maxGap >= sz);
            }
        }
        return results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var getResults = function(queries) {
    const M = 50001;
    const n = 1 << 16;
    const tree = new Int32Array(2 * n);
    const bit = new Int32Array(M + 1);
    let total_obstacles = 1;

    function updateTree(i, val) {
        i += n;
        tree[i] = val;
        while (i > 1) {
            tree[i >> 1] = Math.max(tree[i], tree[i ^ 1]);
            i >>= 1;
        }
    }

    function queryTree(l, r) {
        let res = 0;
        l += n;
        r += n;
        while (l < r) {
            if (l & 1) res = Math.max(res, tree[l++]);
            if (r & 1) res = Math.max(res, tree[--r]);
            l >>= 1;
            r >>= 1;
        }
        return res;
    }

    function updateBit(i, delta) {
        for (i++; i <= M; i += i & -i) bit[i] += delta;
    }

    function queryBit(i) {
        let res = 0;
        for (i++; i > 0; i -= i & -i) res += bit[i];
        return res;
    }

    function findKth(k) {
        let idx = 0;
        for (let i = 1 << 15; i > 0; i >>= 1) {
            if (idx + i <= M && bit[idx + i] < k) {
                idx += i;
                k -= bit[idx];
            }
        }
        return idx;
    }

    updateBit(0, 1);
    const results = [];
    for (let i = 0; i < queries.length; i++) {
        const q = queries[i];
        if (q[0] === 1) {
            const x = q[1];
            const k = queryBit(x - 1);
            const p = findKth(k);
            const next_obs = k < total_obstacles ? findKth(k + 1) : -1;
            updateTree(x, x - p);
            if (next_obs !== -1) updateTree(next_obs, next_obs - x);
            updateBit(x, 1);
            total_obstacles++;
        } else {
            const x = q[1], sz = q[2];
            const k = queryBit(x);
            const p = findKth(k);
            const maxGap = Math.max(queryTree(0, p + 1), x - p);
            results.push(maxGap >= sz);
        }
    }
    return results;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class SegmentTree {
    private size: number;
    private tree: Int32Array;

    constructor(n: number) {
        this.size = 1;
        while (this.size < n) this.size *= 2;
        this.tree = new Int32Array(2 * this.size);
    }

    update(i: number, val: number): void {
        i += this.size;
        this.tree[i] = val;
        while (i > 1) {
            i >>= 1;
            this.tree[i] = Math.max(this.tree[2 * i], this.tree[2 * i + 1]);
        }
    }

    query(l: number, r: number): number {
        let res = 0;
        l += this.size;
        r += this.size;
        while (l <= r) {
            if (l % 2 === 1) res = Math.max(res, this.tree[l++]);
            if (r % 2 === 0) res = Math.max(res, this.tree[r--]);
            l >>= 1;
            r >>= 1;
        }
        return res;
    }
}

function getResults(queries: number[][]): boolean[] {
    let maxX = 0;
    for (const q of queries) {
        if (q[1] > maxX) maxX = q[1];
    }

    const st = new SegmentTree(maxX + 1);
    const obs = [0];
    const results: boolean[] = [];

    function bisectLeft(arr: number[], x: number): number {
        let low = 0, high = arr.length;
        while (low < high) {
            let mid = (low + high) >>> 1;
            if (arr[mid] < x) low = mid + 1;
            else high = mid;
        }
        return low;
    }

    function bisectRight(arr: number[], x: number): number {
        let low = 0, high = arr.length;
        while (low < high) {
            let mid = (low + high) >>> 1;
            if (arr[mid] <= x) low = mid + 1;
            else high = mid;
        }
        return low;
    }

    for (const q of queries) {
        if (q[0] === 1) {
            const x = q[1];
            const idx = bisectLeft(obs, x);
            const prevX = obs[idx - 1];
            const nextX = obs[idx];

            st.update(x, x - prevX);
            if (nextX !== undefined) {
                st.update(nextX, nextX - x);
            }
            obs.splice(idx, 0, x);
        } else {
            const x = q[1];
            const sz = q[2];
            const idx = bisectRight(obs, x);
            const lastObs = obs[idx - 1];
            const maxGap = Math.max(st.query(0, x), x - lastObs);
            results.push(maxGap >= sz);
        }
    }

    return results;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class SegmentTree {
    public $size;
    public $tree;

    public function __construct($n) {
        $this->size = 1;
        while ($this->size < $n) $this->size *= 2;
        $this->tree = array_fill(0, 2 * $this->size, 0);
    }

    public function update($i, $val) {
        $i += $this->size;
        $this->tree[$i] = $val;
        while ($i > 1) {
            $i >>= 1;
            $this->tree[$i] = max($this->tree[2 * $i], $this->tree[2 * $i + 1]);
        }
    }

    public function query($l, $r) {
        $res = 0;
        $l += $this->size;
        $r += $this->size;
        while ($l <= $r) {
            if ($l % 2 == 1) $res = max($res, $this->tree[$l++]);
            if ($r % 2 == 0) $res = max($res, $this->tree[$r--]);
            $l >>= 1;
            $r >>= 1;
        }
        return $res;
    }
}

class Solution {
    function bisect_left($arr, $x) {
        $l = 0; $r = count($arr);
        while ($l < $r) {
            $m = (int)(($l + $r) / 2);
            if ($arr[$m] < $x) $l = $m + 1;
            else $r = $m;
        }
        return $l;
    }

    function bisect_right($arr, $x) {
        $l = 0; $r = count($arr);
        while ($l < $r) {
            $m = (int)(($l + $r) / 2);
            if ($arr[$m] <= $x) $l = $m + 1;
            else $r = $m;
        }
        return $l;
    }

    /**
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function getResults($queries) {
        $max_x = 0;
        foreach ($queries as $q) {
            if ($q[1] > $max_x) $max_x = $q[1];
        }

        $st = new SegmentTree($max_x + 1);
        $obs = [0];
        $results = [];

        foreach ($queries as $q) {
            if ($q[0] == 1) {
                $x = $q[1];
                $idx = $this->bisect_left($obs, $x);
                $prev_x = $obs[$idx - 1];
                $next_x = isset($obs[$idx]) ? $obs[$idx] : null;

                $st->update($x, $x - $prev_x);
                if ($next_x !== null) {
                    $st->update($next_x, $next_x - $x);
                }
                array_splice($obs, $idx, 0, $x);
            } else {
                $x = $q[1];
                $sz = $q[2];
                $idx = $this->bisect_right($obs, $x);
                $last_obs = $obs[$idx - 1];
                $max_gap = max($st->query(0, $x), $x - $last_obs);
                $results[] = $max_gap >= $sz;
            }
        }
        return $results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class SegmentTree {
    var size: Int
    var tree: [Int]

    init(_ n: Int) {
        self.size = 1
        while self.size < n { self.size *= 2 }
        self.tree = Array(repeating: 0, count: 2 * self.size)
    }

    func update(_ i: Int, _ val: Int) {
        var idx = i + size
        tree[idx] = val
        while idx > 1 {
            idx /= 2
            tree[idx] = max(tree[2 * idx], tree[2 * idx + 1])
        }
    }

    func query(_ l: Int, _ r: Int) -> Int {
        var res = 0
        var left = l + size
        var right = r + size
        while left <= right {
            if left % 2 == 1 {
                res = max(res, tree[left])
                left += 1
            }
            if right % 2 == 0 {
                res = max(res, tree[right])
                right -= 1
            }
            left /= 2
            right /= 2
        }
        return res
    }
}

class Solution {
    func getResults(_ queries: [[Int]]) -> [Bool] {
        var maxX = 0
        for q in queries {
            if q[1] > maxX { maxX = q[1] }
        }

        let st = SegmentTree(maxX + 1)
        var obs = [0]
        var results = [Bool]()

        func bisectLeft(_ arr: [Int], _ x: Int) -> Int {
            var low = 0, high = arr.count
            while low < high {
                let mid = (low + high) / 2
                if arr[mid] < x { low = mid + 1 } else { high = mid }
            }
            return low
        }

        func bisectRight(_ arr: [Int], _ x: Int) -> Int {
            var low = 0, high = arr.count
            while low < high {
                let mid = (low + high) / 2
                if arr[mid] <= x { low = mid + 1 } else { high = mid }
            }
            return low
        }

        for q in queries {
            if q[0] == 1 {
                let x = q[1]
                let idx = bisectLeft(obs, x)
                let prevX = obs[idx - 1]
                st.update(x, x - prevX)
                if idx < obs.count {
                    let nextX = obs[idx]
                    st.update(nextX, nextX - x)
                }
                obs.insert(x, at: idx)
            } else {
                let x = q[1], sz = q[2]
                let idx = bisectRight(obs, x)
                let lastObs = obs[idx - 1]
                let maxGap = max(st.query(0, x), x - lastObs)
                results.append(maxGap >= sz)
            }
        }
        return results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.TreeSet

class SegmentTree(n: Int) {
    var size = 1
    val tree: IntArray

    init {
        while (size < n) size *= 2
        tree = IntArray(2 * size)
    }

    fun update(i: Int, value: Int) {
        var idx = i + size
        tree[idx] = value
        while (idx > 1) {
            idx /= 2
            tree[idx] = maxOf(tree[2 * idx], tree[2 * idx + 1])
        }
    }

    fun query(l: Int, r: Int): Int {
        var res = 0
        var left = l + size
        var right = r + size
        while (left <= right) {
            if (left % 2 == 1) res = maxOf(res, tree[left++])
            if (right % 2 == 0) res = maxOf(res, tree[right--])
            left /= 2
            right /= 2
        }
        return res
    }
}

class Solution {
    fun getResults(queries: Array<IntArray>): List<Boolean> {
        var maxX = 0
        for (q in queries) {
            if (q[1] > maxX) maxX = q[1]
        }

        val st = SegmentTree(maxX + 1)
        val obstacles = TreeSet<Int>()
        obstacles.add(0)
        val results = mutableListOf<Boolean>()

        for (q in queries) {
            val type = q[0]
            if (type == 1) {
                val x = q[1]
                val prevX = obstacles.lower(x)!!
                val nextX = obstacles.higher(x)

                st.update(x, x - prevX)
                if (nextX != null) {
                    st.update(nextX, nextX - x)
                }
                obstacles.add(x)
            } else {
                val x = q[1]
                val sz = q[2]
                val lastObs = obstacles.floor(x)!!
                val maxGap = maxOf(st.query(0, x), x - lastObs)
                results.add(maxGap >= sz)
            }
        }
        return results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:typed_data';

class Solution {
  List<bool> getResults(List<List<int>> queries) {
    final int n = 50005;
    final Int32List maxGapTree = Int32List(2 * n);
    final Int32List obsMaxTree = Int32List.filled(2 * n, -1);
    final Int32List obsMinTree = Int32List.filled(2 * n, 1000000);

    void updateMax(Int32List tree, int i, int v) {
      int idx = i + n;
      tree[idx] = v;
      while (idx > 1) {
        idx >>= 1;
        int v1 = tree[idx * 2];
        int v2 = tree[idx * 2 + 1];
        tree[idx] = v1 > v2 ? v1 : v2;
      }
    }

    void updateMin(Int32List tree, int i, int v) {
      int idx = i + n;
      tree[idx] = v;
      while (idx > 1) {
        idx >>= 1;
        int v1 = tree[idx * 2];
        int v2 = tree[idx * 2 + 1];
        tree[idx] = v1 < v2 ? v1 : v2;
      }
    }

    int queryMax(Int32List tree, int l, int r) {
      int res = -1;
      int left = l + n;
      int right = r + n;
      while (left < right) {
        if (left % 2 == 1) {
          if (tree[left] > res) res = tree[left];
          left++;
        }
        if (right % 2 == 1) {
          right--;
          if (tree[right] > res) res = tree[right];
        }
        left >>= 1;
        right >>= 1;
      }
      return res;
    }

    int queryMin(Int32List tree, int l, int r) {
      int res = 1000000;
      int left = l + n;
      int right = r + n;
      while (left < right) {
        if (left % 2 == 1) {
          if (tree[left] < res) res = tree[left];
          left++;
        }
        if (right % 2 == 1) {
          right--;
          if (tree[right] < res) res = tree[right];
        }
        left >>= 1;
        right >>= 1;
      }
      return res;
    }

    updateMax(obsMaxTree, 0, 0);
    updateMin(obsMinTree, 0, 0);

    final List<bool> results = [];
    for (final q in queries) {
      if (q[0] == 1) {
        final int x = q[1];
        final int prev = queryMax(obsMaxTree, 0, x);
        final int next = queryMin(obsMinTree, x + 1, n);
        updateMax(maxGapTree, x, x - prev);
        if (next != 1000000) {
          updateMax(maxGapTree, next, next - x);
        }
        updateMax(obsMaxTree, x, x);
        updateMin(obsMinTree, x, x);
      } else {
        final int x = q[1];
        final int sz = q[2];
        final int prev = queryMax(obsMaxTree, 0, x + 1);
        int bestGap = queryMax(maxGapTree, 0, prev + 1);
        if (bestGap < 0) bestGap = 0;
        if (x - prev > bestGap) bestGap = x - prev;
        results.add(bestGap >= sz);
      }
    }
    return results;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func getResults(queries [][]int) []bool {
	n := 50005
	maxGapTree := make([]int, 2*n)
	obsMaxTree := make([]int, 2*n)
	for i := range obsMaxTree {
		obsMaxTree[i] = -1
	}
	obsMinTree := make([]int, 2*n)
	for i := range obsMinTree {
		obsMinTree[i] = 1000000
	}

	update := func(tree []int, i, v int, isMax bool) {
		idx := i + n
		tree[idx] = v
		for idx > 1 {
			idx >>= 1
			if isMax {
				if tree[idx<<1] > tree[idx<<1|1] {
					tree[idx] = tree[idx<<1]
				} else {
					tree[idx] = tree[idx<<1|1]
				}
			} else {
				if tree[idx<<1] < tree[idx<<1|1] {
					tree[idx] = tree[idx<<1]
				} else {
					tree[idx] = tree[idx<<1|1]
				}
			}
		}
	}

	query := func(tree []int, l, r int, isMax bool) int {
		var res int
		if isMax {
			res = -1
		} else {
			res = 1000000
		}
		left, right := l+n, r+n
		for left < right {
			if left&1 == 1 {
				if isMax {
					if tree[left] > res { res = tree[left] }
				} else {
					if tree[left] < res { res = tree[left] }
				}
				left++
			}
			if right&1 == 1 {
				right--
				if isMax {
					if tree[right] > res { res = tree[right] }
				} else {
					if tree[right] < res { res = tree[right] }
				}
			}
			left >>= 1
			right >>= 1
		}
		return res
	}

	update(obsMaxTree, 0, 0, true)
	update(obsMinTree, 0, 0, false)

	results := make([]bool, 0)
	for _, q := range queries {
		if q[0] == 1 {
			x := q[1]
			prev := query(obsMaxTree, 0, x, true)
			next := query(obsMinTree, x+1, n, false)
			update(maxGapTree, x, x-prev, true)
			if next != 1000000 {
				update(maxGapTree, next, next-x, true)
			}
			update(obsMaxTree, x, x, true)
			update(obsMinTree, x, x, false)
		} else {
			x, sz := q[1], q[2]
			prev := query(obsMaxTree, 0, x+1, true)
			maxGapInTree := query(maxGapTree, 0, prev+1, true)
			if maxGapInTree < 0 { maxGapInTree = 0 }
			bestGap := maxGapInTree
			if x-prev > bestGap {
				bestGap = x - prev
			}
			results = append(results, bestGap >= sz)
		}
	}
	return results
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def get_results(queries)
  n = 50005
  max_gap_tree = Array.new(2 * n, 0)
  obs_max_tree = Array.new(2 * n, -1)
  obs_min_tree = Array.new(2 * n, 1_000_000)

  update_max = lambda do |tree, i, v|
    idx = i + n
    tree[idx] = v
    while idx > 1
      idx >>= 1
      v1 = tree[idx << 1]
      v2 = tree[idx << 1 | 1]
      tree[idx] = v1 > v2 ? v1 : v2
    end
  end

  update_min = lambda do |tree, i, v|
    idx = i + n
    tree[idx] = v
    while idx > 1
      idx >>= 1
      v1 = tree[idx << 1]
      v2 = tree[idx << 1 | 1]
      tree[idx] = v1 < v2 ? v1 : v2
    end
  end

  query_max = lambda do |tree, l, r|
    res = -1
    left = l + n
    right = r + n
    while left < right
      if left.odd?
        val = tree[left]
        res = val if val > res
        left += 1
      end
      if right.odd?
        right -= 1
        val = tree[right]
        res = val if val > res
      end
      left >>= 1
      right >>= 1
    end
    res
  end

  query_min = lambda do |tree, l, r|
    res = 1_000_000
    left = l + n
    right = r + n
    while left < right
      if left.odd?
        val = tree[left]
        res = val if val < res
        left += 1
      end
      if right.odd?
        right -= 1
        val = tree[right]
        res = val if val < res
      end
      left >>= 1
      right >>= 1
    end
    res
  end

  update_max.call(obs_max_tree, 0, 0)
  update_min.call(obs_min_tree, 0, 0)

  results = []
  queries.each do |q|
    if q[0] == 1
      x = q[1]
      prev_obs = query_max.call(obs_max_tree, 0, x)
      next_obs = query_min.call(obs_min_tree, x + 1, n)
      update_max.call(max_gap_tree, x, x - prev_obs)
      if next_obs != 1_000_000
        update_max.call(max_gap_tree, next_obs, next_obs - x)
      end
      update_max.call(obs_max_tree, x, x)
      update_min.call(obs_min_tree, x, x)
    else
      x, sz = q[1], q[2]
      prev_obs = query_max.call(obs_max_tree, 0, x + 1)
      gap_in_tree = query_max.call(max_gap_tree, 0, prev_obs + 1)
      best_gap = gap_in_tree > (x - prev_obs) ? gap_in_tree : (x - prev_obs)
      results << (best_gap >= sz)
    end
  end
  results
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ListBuffer

object Solution {
  def getResults(queries: Array[Array[Int]]): List[Boolean] = {
    val n = 50005
    val maxGapTree = Array.fill(2 * n)(0)
    val obsMaxTree = Array.fill(2 * n)(-1)
    val obsMinTree = Array.fill(2 * n)(1000000)

    def updateMax(tree: Array[Int], i: Int, v: Int): Unit = {
      var idx = i + n
      tree(idx) = v
      while (idx > 1) {
        idx >>= 1
        tree(idx) = Math.max(tree(2 * idx), tree(2 * idx + 1))
      }
    }

    def updateMin(tree: Array[Int], i: Int, v: Int): Unit = {
      var idx = i + n
      tree(idx) = v
      while (idx > 1) {
        idx >>= 1
        tree(idx) = Math.min(tree(2 * idx), tree(2 * idx + 1))
      }
    }

    def queryMax(tree: Array[Int], l: Int, r: Int): Int = {
      var res = -1
      var left = l + n
      var right = r + n
      while (left < right) {
        if (left % 2 == 1) {
          res = Math.max(res, tree(left))
          left += 1
        }
        if (right % 2 == 1) {
          right -= 1
          res = Math.max(res, tree(right))
        }
        left >>= 1
        right >>= 1
      }
      res
    }

    def queryMin(tree: Array[Int], l: Int, r: Int): Int = {
      var res = 1000000
      var left = l + n
      var right = r + n
      while (left < right) {
        if (left % 2 == 1) {
          res = Math.min(res, tree(left))
          left += 1
        }
        if (right % 2 == 1) {
          right -= 1
          res = Math.min(res, tree(right))
        }
        left >>= 1
        right >>= 1
      }
      res
    }

    updateMax(obsMaxTree, 0, 0)
    updateMin(obsMinTree, 0, 0)

    val results = new ListBuffer[Boolean]()
    for (q <- queries) {
      if (q(0) == 1) {
        val x = q(1)
        val prev = queryMax(obsMaxTree, 0, x)
        val next = queryMin(obsMinTree, x + 1, n)
        updateMax(maxGapTree, x, x - prev)
        if (next != 1000000) {
          updateMax(maxGapTree, next, next - x)
        }
        updateMax(obsMaxTree, x, x)
        updateMin(obsMinTree, x, x)
      } else {
        val x = q(1)
        val sz = q(2)
        val prev = queryMax(obsMaxTree, 0, x + 1)
        val bestGap = Math.max(queryMax(maxGapTree, 0, prev + 1), x - prev)
        results += (bestGap >= sz)
      }
    }
    results.toList
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
    pub fn get_results(queries: Vec<Vec<i32>>) -> Vec<bool> {
        let mut p = vec![0];
        for q in &queries {
            if q[0] == 1 {
                p.push(q[1]);
            }
        }
        p.sort();
        p.dedup();

        let mut pos_to_idx = HashMap::new();
        for (i, &val) in p.iter().enumerate() {
            pos_to_idx.insert(val, i);
        }

        let k = p.len();
        let mut next = vec![0; k];
        let mut prev = vec![0; k];
        for i in 0..k {
            next[i] = i + 1;
            prev[i] = i as i32 - 1;
        }

        let mut dsu = (0..k).collect::<Vec<usize>>();
        fn find(dsu: &mut Vec<usize>, mut i: usize) -> usize {
            let mut root = i;
            while dsu[root] != root {
                root = dsu[root];
            }
            while dsu[i] != root {
                let next_idx = dsu[i];
                dsu[i] = root;
                i = next_idx;
            }
            root
        }

        let mut tree = SegmentTree::new(k);
        for i in 1..k {
            tree.update(i, p[i] - p[i - 1]);
        }

        let mut results = Vec::with_capacity(queries.len());
        for q in queries.iter().rev() {
            if q[0] == 1 {
                let x = q[1];
                let j = *pos_to_idx.get(&x).unwrap();
                let pr = prev[j] as usize;
                let nx = next[j];

                if nx < k {
                    tree.update(nx, p[nx] - p[pr]);
                    prev[nx] = pr as i32;
                }
                tree.update(j, 0);
                next[pr] = nx;
                dsu[j] = find(&mut dsu, pr);
            } else {
                let x = q[1];
                let sz = q[2];
                let j = p.partition_point(|&val| val <= x) - 1;
                let idx = find(&mut dsu, j);
                let ak = p[idx];
                let max_gap = std::cmp::max(tree.query(0, idx), x - ak);
                results.push(max_gap >= sz);
            }
        }
        results.reverse();
        results
    }
}

struct SegmentTree {
    n: usize,
    tree: Vec<i32>,
}

impl SegmentTree {
    fn new(n: usize) -> Self {
        let mut m = 1;
        while m < n {
            m *= 2;
        }
        Self {
            n: m,
            tree: vec![0; 2 * m],
        }
    }
    fn update(&mut self, mut i: usize, val: i32) {
        i += self.n;
        self.tree[i] = val;
        while i > 1 {
            i /= 2;
            self.tree[i] = std::cmp::max(self.tree[2 * i], self.tree[2 * i + 1]);
        }
    }
    fn query(&self, mut l: usize, mut r: usize) -> i32 {
        l += self.n;
        r += self.n;
        let mut res = 0;
        while l <= r {
            if l % 2 == 1 {
                res = std::cmp::max(res, self.tree[l]);
                l += 1;
            }
            if r % 2 == 0 {
                res = std::cmp::max(res, self.tree[r]);
                r -= 1;
            }
            l /= 2;
            r /= 2;
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (get-results queries)
  (-> (listof (listof exact-integer?)) (listof boolean?))
  (let* ([p-list (sort (remove-duplicates (cons 0 (map second (filter (lambda (q) (= (first q) 1)) queries)))) <)]
         [p (list->vector p-list)]
         [p-len (vector-length p)]
         [pos-to-idx (make-hash)]
         [_ (for ([i (in-range p-len)]) (hash-set! pos-to-idx (vector-ref p i) i))]
         [next (make-vector p-len p-len)]
         [prev (make-vector p-len -1)]
         [_ (for ([i (in-range p-len)])
              (when (< i (- p-len 1)) (vector-set! next i (+ i 1)))
              (when (> i 0) (vector-set! prev i (- i 1))))]
         [dsu (make-vector p-len 0)]
         [_ (for ([i (in-range p-len)]) (vector-set! dsu i i))]
         [dsu-find (lambda (dsu i)
                     (let loop-root ([curr i])
                       (let ([parent (vector-ref dsu curr)])
                         (if (= parent curr) curr (loop-root parent)))))]
         [dsu-compress (lambda (dsu i root)
                         (let loop-compress ([curr i])
                           (let ([parent (vector-ref dsu curr)])
                             (if (= parent root) root
                                 (begin (vector-set! dsu curr root) (loop-compress parent))))))]
         [find-and-compress (lambda (dsu i)
                              (let ([root (dsu-find dsu i)])
                                (dsu-compress dsu i root) root))]
         [m (let loop-m ([acc 1]) (if (< acc p-len) (loop-m (* acc 2)) acc))]
         [tree (make-vector (* 2 m) 0)]
         [tree-update (lambda (tree m i val)
                        (let loop-up ([idx (+ i m)] [v val])
                          (vector-set! tree idx v)
                          (when (> idx 1)
                            (let* ([p-idx (quotient idx 2)]
                                   [new-val (max (vector-ref tree (* 2 p-idx)) (vector-ref tree (+ 1 (* 2 p-idx))))])
                              (loop-up p-idx new-val)))))]
         [tree-query (lambda (tree m l r)
                       (let loop-q ([ql (+ l m)] [qr (+ r m)] [res 0])
                         (if (<= ql qr)
                             (let* ([res1 (if (= (remainder ql 2) 1) (max res (vector-ref tree ql)) res)]
                                    [ql1 (if (= (remainder ql 2) 1) (+ ql 1) ql)]
                                    [res2 (if (= (remainder qr 2) 0) (max res1 (vector-ref tree qr)) res1)]
                                    [qr2 (if (= (remainder qr 2) 0) (- qr 1) qr)])
                               (loop-q (quotient ql1 2) (quotient qr2 2) res2))
                             res))])
         [_ (for ([i (in-range 1 p-len)]) (tree-update tree m i (- (vector-ref p i) (vector-ref p (- i 1)))))]
         [results '()])
    (for ([q (reverse queries)])
      (if (= (first q) 1)
          (let* ([x (second q)]
                 [j (hash-ref pos-to-idx x)]
                 [pr (vector-ref prev j)]
                 [nx (vector-ref next j)])
            (when (< nx p-len)
              (tree-update tree m nx (- (vector-ref p nx) (vector-ref p pr)))
              (vector-set! prev nx pr))
            (tree-update tree m j 0)
            (vector-set! next pr nx)
            (vector-set! dsu j (find-and-compress dsu pr)))
          (let* ([x (second q)]
                 [sz (third q)]
                 [j (let loop-ub ([low 0] [high p-len])
                      (if (< low high)
                          (let ([mid (quotient (+ low high) 2)])
                            (if (<= (vector-ref p mid) x) (loop-ub (+ mid 1) high) (loop-ub low mid)))
                          (- low 1)))]
                 [idx (find-and-compress dsu j)]
                 [ak (vector-ref p idx)]
                 [max-gap (max (tree-query tree m 0 idx) (- x ak))])
            (set! results (cons (>= max-gap sz) results)))))
    results))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec get_results(Queries :: [[integer()]]) -> [boolean()].
get_results(Queries) ->
    PList = lists:usort([0 | [X || [Type, X | _] <- Queries, Type =:= 1]]),
    PLen = length(PList),
    PArray = array:from_list(PList),
    PosToIdx = maps:from_list(lists:zip(PList, lists:seq(0, PLen - 1))),
    Next = array:from_list(lists:seq(1, PLen)),
    Prev = array:from_list([-1 | lists:seq(0, PLen - 2)]),
    Dsu = array:from_list(lists:seq(0, PLen - 1)),
    M = find_m(PLen, 1),
    Tree0 = array:new(2 * M, {default, 0}),
    Tree = fill_tree(Tree0, PList, M, 1),
    process_queries(lists:reverse(Queries), PArray, PLen, PosToIdx, Next, Prev, Dsu, Tree, M, []).

find_m(N, M) when M < N -> find_m(N, M * 2);
find_m(_, M) -> M.

fill_tree(Tree, [_ | []], _M, _Idx) -> Tree;
fill_tree(Tree, [P1 | [P2 | Rest]], M, Idx) ->
    NewTree = update_tree(Tree, Idx, P2 - P1, M),
    fill_tree(NewTree, [P2 | Rest], M, Idx + 1).

update_tree(Tree, I, Val, M) ->
    Idx = I + M,
    Tree1 = array:set(Idx, Val, Tree),
    update_up(Tree1, Idx div 2).

update_up(Tree, 0) -> Tree;
update_up(Tree, P) ->
    V1 = array:get(P * 2, Tree),
    V2 = array:get(P * 2 + 1, Tree),
    Max = erlang:max(V1, V2),
    case array:get(P, Tree) of
        Max -> Tree;
        _ -> update_up(array:set(P, Max, Tree), P div 2)
    end.

query_tree(Tree, L, R, M) ->
    query_tree_loop(Tree, L + M, R + M, 0).

query_tree_loop(Tree, L, R, Res) when L =< R ->
    {NewL, Res1} = if L rem 2 =:= 1 -> {L + 1, erlang:max(Res, array:get(L, Tree))};
                      true -> {L, Res}
                   end,
    {NewR, Res2} = if R rem 2 =:= 0 -> {R - 1, erlang:max(Res1, array:get(R, Tree))};
                      true -> {R, Res1}
                   end,
    query_tree_loop(Tree, NewL div 2, NewR div 2, Res2);
query_tree_loop(_Tree, _L, _R, Res) -> Res.

find_dsu(Dsu, I) ->
    Root = find_root(Dsu, I),
    {Root, compress_dsu(Dsu, I, Root)}.

find_root(Dsu, I) ->
    case array:get(I, Dsu) of
        I -> I;
        Next -> find_root(Dsu, Next)
    end.

compress_dsu(Dsu, I, Root) ->
    case array:get(I, Dsu) of
        Root -> Dsu;
        Next -> compress_dsu(array:set(I, Root, Dsu), Next, Root)
    end.

upper_bound(Arr, Val, Low, High) ->
    if Low >= High -> Low;
       true ->
           Mid = (Low + High) div 2,
           MidVal = array:get(Mid, Arr),
           if MidVal =< Val -> upper_bound(Arr, Val, Mid + 1, High);
              true -> upper_bound(Arr, Val, Low, Mid)
           end
    end.

process_queries([], _, _, _, _, _, _, _, _, Acc) -> Acc;
process_queries([[1, X] | Rest], PArr, PLen, PosToIdx, Next, Prev, Dsu, Tree, M, Acc) ->
    J = maps:get(X, PosToIdx),
    Pr = array:get(J, Prev),
    Nx = array:get(J, Next),
    Tree1 = if Nx < PLen ->
                   Pnx = array:get(Nx, PArr),
                   Ppr = array:get(Pr, PArr),
                   update_tree(Tree, Nx, Pnx - Ppr, M);
               true -> Tree
            end,
    Tree2 = update_tree(Tree1, J, 0, M),
    Next1 = array:set(Pr, Nx, Next),
    Prev1 = if Nx < PLen -> array:set(Nx, Pr, Prev); true -> Prev end,
    {RootPr, Dsu1} = find_dsu(Dsu, Pr),
    Dsu2 = array:set(J, RootPr, Dsu1),
    process_queries(Rest, PArr, PLen, PosToIdx, Next1, Prev1, Dsu2, Tree2, M, Acc);
process_queries([[2, X, Sz] | Rest], PArr, PLen, PosToIdx, Next, Prev, Dsu, Tree, M, Acc) ->
    UB = upper_bound(PArr, X, 0, PLen),
    J = UB - 1,
    {Idx, Dsu1} = find_dsu(Dsu, J),
    Ak = array:get(Idx, PArr),
    MaxGap = erlang:max(query_tree(Tree, 0, Idx, M), X - Ak),
    process_queries(Rest, PArr, PLen, PosToIdx, Next, Prev, Dsu1, Tree, M, [(MaxGap >= Sz) | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec get_results(queries :: [[integer]]) :: [boolean]
  def get_results(queries) do
    p_list = queries
    |> Enum.filter(fn [type | _] -> type == 1 end)
    |> Enum.map(fn [_, x] -> x end)
    |> (fn x_list -> [0 | x_list] end).()
    |> Enum.sort()
    |> Enum.dedup()

    p_len = length(p_list)
    p_array = :array.from_list(p_list)
    pos_to_idx = p_list |> Enum.with_index() |> Map.new()

    m = find_m(p_len, 1)
    tree = :array.new(2 * m, default: 0)
    tree = fill_tree(tree, p_list, m, 1)

    next_arr = :array.from_list(Enum.to_list(1..p_len))
    prev_arr = :array.from_list([-1 | Enum.to_list(0..(p_len - 2))])
    dsu = :array.from_list(Enum.to_list(0..(p_len - 1)))

    process_queries(Enum.reverse(queries), p_array, p_len, pos_to_idx, next_arr, prev_arr, dsu, tree, m, [])
  end

  defp find_m(n, m) when m < n, do: find_m(n, m * 2)
  defp find_m(_, m), do: m

  defp fill_tree(tree, [_], _m, _idx), do: tree
  defp fill_tree(tree, [p1 | [p2 | rest]], m, idx) do
    tree = update_tree(tree, idx, p2 - p1, m)
    fill_tree(tree, [p2 | rest], m, idx + 1)
  end

  defp update_tree(tree, i, val, m) do
    idx = i + m
    tree = :array.set(idx, val, tree)
    update_up(tree, div(idx, 2))
  end

  defp update_up(tree, 0), do: tree
  defp update_up(tree, p) do
    v1 = :array.get(p * 2, tree)
    v2 = :array.get(p * 2 + 1, tree)
    max_v = max(v1, v2)
    if :array.get(p, tree) == max_v do
      tree
    else
      update_up(:array.set(p, max_v, tree), div(p, 2))
    end
  end

  defp query_tree(tree, l, r, m), do: query_tree_loop(tree, l + m, r + m, 0)
  defp query_tree_loop(_, l, r, res) when l > r, do: res
  defp query_tree_loop(tree, l, r, res) do
    {l, res} = if rem(l, 2) == 1, do: {l + 1, max(res, :array.get(l, tree))}, else: {l, res}
    {r, res} = if rem(r, 2) == 0, do: {r - 1, max(res, :array.get(r, tree))}, else: {r, res}
    query_tree_loop(tree, div(l, 2), div(r, 2), res)
  end

  defp find_dsu(dsu, i) do
    root = find_root(dsu, i)
    {root, compress_dsu(dsu, i, root)}
  end
  defp find_root(dsu, i) do
    next = :array.get(i, dsu)
    if next == i, do: i, else: find_root(dsu, next)
  end
  defp compress_dsu(dsu, i, root) do
    next = :array.get(i, dsu)
    if next == root, do: dsu, else: compress_dsu(:array.set(i, root, dsu), next, root)
  end

  defp upper_bound(arr, val, low, high) do
    if low >= high do
      low
    else
      mid = div(low + high, 2)
      if :array.get(mid, arr) <= val, do: upper_bound(arr, val, mid + 1, high), else: upper_bound(arr, val, low, mid)
    end
  end

  defp process_queries([], _, _, _, _, _, _, _, _, acc), do: acc
  defp process_queries([[1, x] | rest], p_arr, p_len, pos_to_idx, next_arr, prev_arr, dsu, tree, m, acc) do
    j = Map.get(pos_to_idx, x)
    pr = :array.get(j, prev_arr)
    nx = :array.get(j, next_arr)
    tree = if nx < p_len do
      update_tree(tree, nx, :array.get(nx, p_arr) - :array.get(pr, p_arr), m)
    else
      tree
    end
    tree = update_tree(tree, j, 0, m)
    next_arr = :array.set(pr, nx, next_arr)
    prev_arr = if nx < p_len, do: :array.set(nx, pr, prev_arr), else: prev_arr
    {root_pr, dsu} = find_dsu(dsu, pr)
    dsu = :array.set(j, root_pr, dsu)
    process_queries(rest, p_arr, p_len, pos_to_idx, next_arr, prev_arr, dsu, tree, m, acc)
  end
  defp process_queries([[2, x, sz] | rest], p_arr, p_len, pos_to_idx, next_arr, prev_arr, dsu, tree, m, acc) do
    ub = upper_bound(p_arr, x, 0, p_len)
    j = ub - 1
    {idx, dsu} = find_dsu(dsu, j)
    ak = :array.get(idx, p_arr)
    max_gap = max(query_tree(tree, 0, idx, m), x - ak)
    process_queries(rest, p_arr, p_len, pos_to_idx, next_arr, prev_arr, dsu, tree, m, [max_gap >= sz | acc])
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(Q(log M + log Q)) where Q is the number of queries and M is the maximum coordinate value (50,000). For each query, we perform a search in a sorted container (O(log Q)) and a point update or range maximum query on a segment tree (O(log M)).
- **Space Complexity:** O(M + Q) to store the segment tree and the list of obstacles, where M is the maximum coordinate on the number line and Q is the number of queries.
