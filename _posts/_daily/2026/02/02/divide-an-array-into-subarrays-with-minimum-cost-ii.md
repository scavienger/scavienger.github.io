---
layout: post
title: "Divide an Array Into Subarrays With Minimum Cost II"
date: 2026-02-02 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Sliding Window", "Heap (Priority Queue)"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long minimumCost(vector<int>& nums,\
        \ int k, int dist) {\n        int n = nums.size();\n        multiset<int> small,\
        \ large;\n        long long small_sum = 0;\n        int k_minus_2 = k - 2;\n\
        \n        auto add = [&](int val) {\n            small.insert(val);\n      \
        \      small_sum += val;\n            if (small.size() > k_minus_2) {\n    \
        \            auto it = prev(small.end());\n                int v = *it;\n  \
        \              small_sum -= v;\n                large.insert(v);\n         \
        \       small.erase(it);\n            }\n        };\n\n        auto remove =\
        \ [&](int val) {\n            auto it = small.find(val);\n            if (it\
        \ != small.end()) {\n                small_sum -= val;\n                small.erase(it);\n\
        \                if (!large.empty()) {\n                    auto it2 = large.begin();\n\
        \                    int v = *it2;\n                    small_sum += v;\n  \
        \                  small.insert(v);\n                    large.erase(it2);\n\
        \                }\n            } else {\n                large.erase(large.find(val));\n\
        \            }\n        };\n\n        for (int i = 2; i <= 1 + dist && i < n;\
        \ i++) add(nums[i]);\n        long long ans = (long long)nums[0] + nums[1] +\
        \ small_sum;\n\n        for (int i1 = 2; i1 <= n - k + 1; i1++) {\n        \
        \    remove(nums[i1]);\n            if (i1 + dist < n) add(nums[i1 + dist]);\n\
        \            ans = min(ans, (long long)nums[0] + nums[i1] + small_sum);\n  \
        \      }\n\n        return ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    private TreeMap<Integer, Integer>\
        \ small = new TreeMap<>();\n    private TreeMap<Integer, Integer> large = new\
        \ TreeMap<>();\n    private int smallCount = 0;\n    private long smallSum =\
        \ 0;\n\n    public long minimumCost(int[] nums, int k, int dist) {\n       \
        \ int n = nums.length;\n        int k2 = k - 2;\n        for (int i = 2; i <=\
        \ 1 + dist && i < n; i++) add(nums[i], k2);\n        long ans = (long) nums[0]\
        \ + nums[1] + smallSum;\n\n        for (int i1 = 2; i1 <= n - k + 1; i1++) {\n\
        \            remove(nums[i1], k2);\n            if (i1 + dist < n) add(nums[i1\
        \ + dist], k2);\n            ans = Math.min(ans, (long) nums[0] + nums[i1] +\
        \ smallSum);\n        }\n        return ans;\n    }\n\n    private void add(int\
        \ val, int k2) {\n        small.put(val, small.getOrDefault(val, 0) + 1);\n\
        \        smallSum += val;\n        smallCount++;\n        if (smallCount > k2)\
        \ {\n            int last = small.lastKey();\n            smallSum -= last;\n\
        \            removeOne(small, last);\n            smallCount--;\n          \
        \  large.put(last, large.getOrDefault(last, 0) + 1);\n        }\n    }\n\n \
        \   private void remove(int val, int k2) {\n        if (small.containsKey(val))\
        \ {\n            removeOne(small, val);\n            smallSum -= val;\n    \
        \        smallCount--;\n            if (!large.isEmpty()) {\n              \
        \  int first = large.firstKey();\n                small.put(first, small.getOrDefault(first,\
        \ 0) + 1);\n                smallSum += first;\n                smallCount++;\n\
        \                removeOne(large, first);\n            }\n        } else {\n\
        \            removeOne(large, val);\n        }\n    }\n\n    private void removeOne(TreeMap<Integer,\
        \ Integer> map, int val) {\n        int count = map.get(val);\n        if (count\
        \ == 1) map.remove(val);\n        else map.put(val, count - 1);\n    }\n}"
      python: "class Solution(object):\n    def minimumCost(self, nums, k, dist):\n\
        \        n = len(nums)\n        k_small = k - 2\n        unique_vals = sorted(list(set(nums[1:])))\n\
        \        val_map = {v: i + 1 for i, v in enumerate(unique_vals)}\n        n_uniq\
        \ = len(unique_vals)\n        bit_cnt = [0] * (n_uniq + 1)\n        bit_sum\
        \ = [0] * (n_uniq + 1)\n\n        def update(val, delta):\n            idx =\
        \ val_map[val]\n            s = val * delta\n            while idx <= n_uniq:\n\
        \                bit_cnt[idx] += delta\n                bit_sum[idx] += s\n\
        \                idx += idx & -idx\n\n        def query(target):\n         \
        \   pos = 0\n            cnt = 0\n            sm = 0\n            for i in range(n_uniq.bit_length(),\
        \ -1, -1):\n                pw = 1 << i\n                if pos + pw <= n_uniq\
        \ and cnt + bit_cnt[pos + pw] < target:\n                    pos += pw\n   \
        \                 cnt += bit_cnt[pos]\n                    sm += bit_sum[pos]\n\
        \            return sm + (target - cnt) * unique_vals[pos]\n\n        for i\
        \ in range(2, min(n, 2 + dist)):\n            update(nums[i], 1)\n        ans\
        \ = nums[0] + nums[1] + query(k_small)\n\n        for i1 in range(2, n - k +\
        \ 2):\n            update(nums[i1], -1)\n            if i1 + dist < n:\n   \
        \             update(nums[i1 + dist], 1)\n            ans = min(ans, nums[0]\
        \ + nums[i1] + query(k_small))\n        return ans"
      python3: "class Solution:\n    def minimumCost(self, nums: List[int], k: int,\
        \ dist: int) -> int:\n        n = len(nums)\n        k_small = k - 2\n     \
        \   unique_vals = sorted(list(set(nums[1:])))\n        val_map = {v: i + 1 for\
        \ i, v in enumerate(unique_vals)}\n        n_uniq = len(unique_vals)\n     \
        \   bit_cnt = [0] * (n_uniq + 1)\n        bit_sum = [0] * (n_uniq + 1)\n\n \
        \       def update(val, delta):\n            idx = val_map[val]\n          \
        \  s = val * delta\n            while idx <= n_uniq:\n                bit_cnt[idx]\
        \ += delta\n                bit_sum[idx] += s\n                idx += idx &\
        \ -idx\n\n        def query(target):\n            pos = 0\n            cnt =\
        \ 0\n            sm = 0\n            for i in range(n_uniq.bit_length(), -1,\
        \ -1):\n                pw = 1 << i\n                if pos + pw <= n_uniq and\
        \ cnt + bit_cnt[pos + pw] < target:\n                    pos += pw\n       \
        \             cnt += bit_cnt[pos]\n                    sm += bit_sum[pos]\n\
        \            return sm + (target - cnt) * unique_vals[pos]\n\n        for i\
        \ in range(2, min(n, 2 + dist)):\n            update(nums[i], 1)\n        ans\
        \ = nums[0] + nums[1] + query(k_small)\n\n        for i1 in range(2, n - k +\
        \ 2):\n            update(nums[i1], -1)\n            if i1 + dist < n:\n   \
        \             update(nums[i1 + dist], 1)\n            ans = min(ans, nums[0]\
        \ + nums[i1] + query(k_small))\n        return ans"
      c: "#include <stdlib.h>\n#include <string.h>\n\nint compare_ints(const void* a,\
        \ const void* b) {\n    int arg1 = *(const int*)a;\n    int arg2 = *(const int*)b;\n\
        \    if (arg1 < arg2) return -1;\n    if (arg1 > arg2) return 1;\n    return\
        \ 0;\n}\n\nlong long bit_cnt[100005], bit_sum[100005];\nint num_uniq;\n\nvoid\
        \ update(int idx, int delta, int val, int n) {\n    long long s = (long long)val\
        \ * delta;\n    for (; idx <= n; idx += idx & -idx) {\n        bit_cnt[idx]\
        \ += delta;\n        bit_sum[idx] += s;\n    }\n}\n\nlong long query(int k,\
        \ int* unique_vals) {\n    int pos = 0;\n    long long cnt = 0, sum = 0;\n \
        \   for (int i = 1 << 17; i > 0; i >>= 1) {\n        if (pos + i <= num_uniq\
        \ && cnt + bit_cnt[pos + i] < k) {\n            pos += i;\n            cnt +=\
        \ bit_cnt[pos];\n            sum += bit_sum[pos];\n        }\n    }\n    return\
        \ sum + (long long)(k - cnt) * unique_vals[pos];\n}\n\nlong long minimumCost(int*\
        \ nums, int n, int k, int dist) {\n    int* sorted_nums = (int*)malloc((n -\
        \ 1) * sizeof(int));\n    for (int i = 0; i < n - 1; i++) sorted_nums[i] = nums[i\
        \ + 1];\n    qsort(sorted_nums, n - 1, sizeof(int), compare_ints);\n\n    int*\
        \ unique_vals = (int*)malloc((n - 1) * sizeof(int));\n    num_uniq = 0;\n  \
        \  if (n > 1) unique_vals[num_uniq++] = sorted_nums[0];\n    for (int i = 1;\
        \ i < n - 1; i++) {\n        if (sorted_nums[i] != sorted_nums[i - 1]) unique_vals[num_uniq++]\
        \ = sorted_nums[i];\n    }\n\n    memset(bit_cnt, 0, sizeof(bit_cnt));\n   \
        \ memset(bit_sum, 0, sizeof(bit_sum));\n\n    int get_rank(int val) {\n    \
        \    int l = 0, r = num_uniq - 1;\n        while (l <= r) {\n            int\
        \ mid = l + (r - l) / 2;\n            if (unique_vals[mid] == val) return mid\
        \ + 1;\n            if (unique_vals[mid] < val) l = mid + 1;\n            else\
        \ r = mid - 1;\n        }\n        return -1;\n    }\n\n    for (int i = 2;\
        \ i <= 1 + dist && i < n; i++) update(get_rank(nums[i]), 1, nums[i], num_uniq);\n\
        \    long long ans = (long long)nums[0] + nums[1] + query(k - 2, unique_vals);\n\
        \n    for (int i1 = 2; i1 <= n - k + 1; i1++) {\n        update(get_rank(nums[i1]),\
        \ -1, nums[i1], num_uniq);\n        if (i1 + dist < n) update(get_rank(nums[i1\
        \ + dist]), 1, nums[i1 + dist], num_uniq);\n        long long cur = (long long)nums[0]\
        \ + nums[i1] + query(k - 2, unique_vals);\n        if (cur < ans) ans = cur;\n\
        \    }\n\n    free(sorted_nums); free(unique_vals);\n    return ans;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public long MinimumCost(int[] nums, int k, int\
        \ dist) {\n        int n = nums.Length;\n        int k2 = k - 2;\n        SortedSet<(int\
        \ val, int idx)> small = new SortedSet<(int val, int idx)>();\n        SortedSet<(int\
        \ val, int idx)> large = new SortedSet<(int val, int idx)>();\n        long\
        \ smallSum = 0;\n\n        void Add(int val, int i) {\n            small.Add((val,\
        \ i));\n            smallSum += val;\n            if (small.Count > k2) {\n\
        \                var last = small.Max;\n                smallSum -= last.val;\n\
        \                small.Remove(last);\n                large.Add(last);\n   \
        \         }\n        }\n\n        void Remove(int val, int i) {\n          \
        \  if (small.Contains((val, i))) {\n                small.Remove((val, i));\n\
        \                smallSum -= val;\n                if (large.Count > 0) {\n\
        \                    var first = large.Min;\n                    smallSum +=\
        \ first.val;\n                    small.Add(first);\n                    large.Remove(first);\n\
        \                }\n            } else {\n                large.Remove((val,\
        \ i));\n            }\n        }\n\n        for (int i = 2; i <= 1 + dist &&\
        \ i < n; i++) Add(nums[i], i);\n        long ans = (long)nums[0] + nums[1] +\
        \ smallSum;\n\n        for (int i1 = 2; i1 <= n - k + 1; i1++) {\n         \
        \   Remove(nums[i1], i1);\n            if (i1 + dist < n) Add(nums[i1 + dist],\
        \ i1 + dist);\n            ans = Math.min(ans, (long)nums[0] + nums[i1] + smallSum);\n\
        \        }\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @param {number}\
        \ dist\n * @return {number}\n */\nvar minimumCost = function(nums, k, dist)\
        \ {\n    const n = nums.length;\n    const k2 = k - 2;\n    const uniqueVals\
        \ = Array.from(new Set(nums.slice(1))).sort((a, b) => a - b);\n    const valMap\
        \ = new Map();\n    uniqueVals.forEach((v, i) => valMap.set(v, i + 1));\n  \
        \  const nUniq = uniqueVals.length;\n    const bitCnt = new Float64Array(nUniq\
        \ + 1);\n    const bitSum = new Float64Array(nUniq + 1);\n\n    function update(val,\
        \ delta) {\n        let idx = valMap.get(val);\n        const s = val * delta;\n\
        \        while (idx <= nUniq) {\n            bitCnt[idx] += delta;\n       \
        \     bitSum[idx] += s;\n            idx += idx & -idx;\n        }\n    }\n\n\
        \    function query(target) {\n        let pos = 0, cnt = 0, sm = 0;\n     \
        \   for (let i = Math.floor(Math.log2(nUniq)); i >= 0; i--) {\n            const\
        \ pw = 1 << i;\n            if (pos + pw <= nUniq && cnt + bitCnt[pos + pw]\
        \ < target) {\n                pos += pw;\n                cnt += bitCnt[pos];\n\
        \                sm += bitSum[pos];\n            }\n        }\n        return\
        \ sm + (target - cnt) * uniqueVals[pos];\n    }\n\n    for (let i = 2; i <=\
        \ 1 + dist && i < n; i++) update(nums[i], 1);\n    let ans = nums[0] + nums[1]\
        \ + query(k2);\n\n    for (let i1 = 2; i1 <= n - k + 1; i1++) {\n        update(nums[i1],\
        \ -1);\n        if (i1 + dist < n) update(nums[i1 + dist], 1);\n        ans\
        \ = Math.min(ans, nums[0] + nums[i1] + query(k2));\n    }\n    return ans;\n\
        };"
      typescript: "class TreapNode {\n  value: number;\n  priority: number;\n  size:\
        \ number;\n  sum: number;\n  left: TreapNode | null = null;\n  right: TreapNode\
        \ | null = null;\n  constructor(value: number) {\n    this.value = value;\n\
        \    this.priority = Math.random();\n    this.size = 1;\n    this.sum = value;\n\
        \  }\n}\n\nfunction getSize(node: TreapNode | null): number {\n  return node\
        \ ? node.size : 0;\n}\n\nfunction getSum(node: TreapNode | null): number {\n\
        \  return node ? node.sum : 0;\n}\n\nfunction update(node: TreapNode | null)\
        \ {\n  if (node) {\n    node.size = 1 + getSize(node.left) + getSize(node.right);\n\
        \    node.sum = node.value + getSum(node.left) + getSum(node.right);\n  }\n\
        }\n\nfunction splitBySize(node: TreapNode | null, k: number): [TreapNode | null,\
        \ TreapNode | null] {\n  if (!node) return [null, null];\n  const leftSize =\
        \ getSize(node.left);\n  if (leftSize >= k) {\n    const [left, right] = splitBySize(node.left,\
        \ k);\n    node.left = right;\n    update(node);\n    return [left, node];\n\
        \  } else {\n    const [left, right] = splitBySize(node.right, k - leftSize\
        \ - 1);\n    node.right = left;\n    update(node);\n    return [node, right];\n\
        \  }\n}\n\nfunction splitByValue(node: TreapNode | null, value: number): [TreapNode\
        \ | null, TreapNode | null] {\n  if (!node) return [null, null];\n  if (node.value\
        \ <= value) {\n    const [l, r] = splitByValue(node.right, value);\n    node.right\
        \ = l;\n    update(node);\n    return [node, r];\n  } else {\n    const [l,\
        \ r] = splitByValue(node.left, value);\n    node.left = r;\n    update(node);\n\
        \    return [l, node];\n  }\n}\n\nfunction merge(left: TreapNode | null, right:\
        \ TreapNode | null): TreapNode | null {\n  if (!left || !right) return left\
        \ || right;\n  if (left.priority > right.priority) {\n    left.right = merge(left.right,\
        \ right);\n    update(left);\n    return left;\n  } else {\n    right.left =\
        \ merge(left, right.left);\n    update(right);\n    return right;\n  }\n}\n\n\
        function minimumCost(nums: number[], k: number, dist: number): number {\n  const\
        \ n = nums.length;\n  const m = k - 2;\n  let root: TreapNode | null = null;\n\
        \  for (let j = 2; j <= Math.min(1 + dist, n - 1); j++) {\n    root = merge(root,\
        \ null);\n    const [l, r] = splitByValue(root, nums[j]);\n    root = merge(merge(l,\
        \ new TreapNode(nums[j])), r);\n  }\n\n  const getSmallestSum = (k: number):\
        \ number => {\n    if (k === 0) return 0;\n    const [l, r] = splitBySize(root,\
        \ k);\n    const res = getSum(l);\n    root = merge(l, r);\n    return res;\n\
        \  };\n\n  let minCost = nums[0] + nums[1] + getSmallestSum(m);\n\n  for (let\
        \ i = 2; i <= n - k + 1; i++) {\n    let [l, r] = splitByValue(root, nums[i]\
        \ - 1);\n    let [mid, rr] = splitByValue(r, nums[i]);\n    let [one, rest]\
        \ = splitBySize(mid, 1);\n    root = merge(l, merge(rest, rr));\n    if (i +\
        \ dist < n) {\n      let [l2, r2] = splitByValue(root, nums[i + dist]);\n  \
        \    root = merge(merge(l2, new TreapNode(nums[i + dist])), r2);\n    }\n  \
        \  minCost = Math.min(minCost, nums[0] + nums[i] + getSmallestSum(m));\n  }\n\
        \n  return minCost;\n}"
      php: "class Solution {\n    function minimumCost($nums, $k, $dist) {\n       \
        \ $n = count($nums);\n        $m = $k - 2;\n        $root = null;\n        for\
        \ ($j = 2; $j <= min(1 + $dist, $n - 1); $j++) {\n            $root = $this->add($root,\
        \ $nums[$j]);\n        }\n        $minCost = $nums[0] + $nums[1] + $this->sumOfSmallest($root,\
        \ $m);\n        for ($i = 2; $i <= $n - $k + 1; $i++) {\n            $root =\
        \ $this->remove($root, $nums[$i]);\n            if ($i + $dist < $n) {\n   \
        \             $root = $this->add($root, $nums[$i + $dist]);\n            }\n\
        \            $currentCost = $nums[0] + $nums[$i] + $this->sumOfSmallest($root,\
        \ $m);\n            if ($currentCost < $minCost) {\n                $minCost\
        \ = $currentCost;\n            }\n        }\n        return $minCost;\n    }\n\
        \n    private function add($root, $val) {\n        [$l, $r] = $this->splitByValue($root,\
        \ $val);\n        return $this->merge($this->merge($l, new TreapNode($val)),\
        \ $r);\n    }\n\n    private function remove($root, $val) {\n        [$l, $r]\
        \ = $this->splitByValue($root, $val - 1);\n        [$mid, $rr] = $this->splitByValue($r,\
        \ $val);\n        [$one, $rest] = $this->splitBySize($mid, 1);\n        return\
        \ $this->merge($this->merge($l, $rest), $rr);\n    }\n\n    private function\
        \ sumOfSmallest(&$root, $k) {\n        if ($k <= 0) return 0;\n        [$l,\
        \ $r] = $this->splitBySize($root, $k);\n        $res = $l ? $l->sum : 0;\n \
        \       $root = $this->merge($l, $r);\n        return $res;\n    }\n\n    private\
        \ function splitByValue($node, $val) {\n        if (!$node) return [null, null];\n\
        \        if ($node->value <= $val) {\n            [$l, $r] = $this->splitByValue($node->right,\
        \ $val);\n            $node->right = $l;\n            $node->update();\n   \
        \         return [$node, $r];\n        } else {\n            [$l, $r] = $this->splitByValue($node->left,\
        \ $val);\n            $node->left = $r;\n            $node->update();\n    \
        \        return [$l, $node];\n        }\n    }\n\n    private function splitBySize($node,\
        \ $k) {\n        if (!$node) return [null, null];\n        $leftSize = $node->left\
        \ ? $node->left->size : 0;\n        if ($leftSize >= $k) {\n            [$l,\
        \ $r] = $this->splitBySize($node->left, $k);\n            $node->left = $r;\n\
        \            $node->update();\n            return [$l, $node];\n        } else\
        \ {\n            [$l, $r] = $this->splitBySize($node->right, $k - $leftSize\
        \ - 1);\n            $node->right = $l;\n            $node->update();\n    \
        \        return [$node, $r];\n        }\n    }\n\n    private function merge($l,\
        \ $r) {\n        if (!$l || !$r) return $l ?: $r;\n        if ($l->priority\
        \ > $r->priority) {\n            $l->right = $this->merge($l->right, $r);\n\
        \            $l->update();\n            return $l;\n        } else {\n     \
        \       $r->left = $this->merge($l, $r->left);\n            $r->update();\n\
        \            return $r;\n        }\n    }\n}\n\nclass TreapNode {\n    public\
        \ $value, $priority, $size, $sum, $left, $right;\n    function __construct($val)\
        \ {\n        $this->value = $val;\n        $this->priority = mt_rand(0, 1000000000);\n\
        \        $this->size = 1;\n        $this->sum = $val;\n    }\n    function update()\
        \ {\n        $this->size = 1 + ($this->left ? $this->left->size : 0) + ($this->right\
        \ ? $this->right->size : 0);\n        $this->sum = $this->value + ($this->left\
        \ ? $this->left->sum : 0) + ($this->right ? $this->right->sum : 0);\n    }\n\
        }"
      swift: "class Solution {\n    class TreapNode {\n        var value: Int\n    \
        \    var priority: Int\n        var size: Int\n        var sum: Int\n      \
        \  var left: TreapNode? = nil\n        var right: TreapNode? = nil\n       \
        \ init(_ val: Int) {\n            self.value = val\n            self.priority\
        \ = Int.random(in: 0...Int.max)\n            self.size = 1\n            self.sum\
        \ = val\n        }\n        func update() {\n            size = 1 + (left?.size\
        \ ?? 0) + (right?.size ?? 0)\n            sum = value + (left?.sum ?? 0) + (right?.sum\
        \ ?? 0)\n        }\n    }\n\n    func splitByValue(_ node: TreapNode?, _ val:\
        \ Int) -> (TreapNode?, TreapNode?) {\n        guard let node = node else { return\
        \ (nil, nil) }\n        if node.value <= val {\n            let (l, r) = splitByValue(node.right,\
        \ val)\n            node.right = l\n            node.update()\n            return\
        \ (node, r)\n        } else {\n            let (l, r) = splitByValue(node.left,\
        \ val)\n            node.left = r\n            node.update()\n            return\
        \ (l, node)\n        }\n    }\n\n    func splitBySize(_ node: TreapNode?, _\
        \ k: Int) -> (TreapNode?, TreapNode?) {\n        guard let node = node else\
        \ { return (nil, nil) }\n        let leftSize = node.left?.size ?? 0\n     \
        \   if leftSize >= k {\n            let (l, r) = splitBySize(node.left, k)\n\
        \            node.left = r\n            node.update()\n            return (l,\
        \ node)\n        } else {\n            let (l, r) = splitBySize(node.right,\
        \ k - leftSize - 1)\n            node.right = l\n            node.update()\n\
        \            return (node, r)\n        }\n    }\n\n    func merge(_ l: TreapNode?,\
        \ _ r: TreapNode?) -> TreapNode? {\n        if l == nil { return r }\n     \
        \   if r == nil { return l }\n        if l!.priority > r!.priority {\n     \
        \       l!.right = merge(l!.right, r)\n            l!.update()\n           \
        \ return l\n        } else {\n            r!.left = merge(l, r!.left)\n    \
        \        r!.update()\n            return r\n        }\n    }\n\n    func minimumCost(_\
        \ nums: [Int], _ k: Int, _ dist: Int) -> Int {\n        let n = nums.count\n\
        \        let m = k - 2\n        var root: TreapNode? = nil\n\n        func add(_\
        \ val: Int) {\n            let (l, r) = splitByValue(root, val)\n          \
        \  root = merge(merge(l, TreapNode(val)), r)\n        }\n\n        func remove(_\
        \ val: Int) {\n            let (l, r) = splitByValue(root, val - 1)\n      \
        \      let (mid, rr) = splitByValue(r, val)\n            let (_, rest) = splitBySize(mid,\
        \ 1)\n            root = merge(merge(l, rest), rr)\n        }\n\n        func\
        \ sumOfSmallest(_ k: Int) -> Int {\n            if k <= 0 { return 0 }\n   \
        \         let (l, r) = splitBySize(root, k)\n            let res = l?.sum ??\
        \ 0\n            root = merge(l, r)\n            return res\n        }\n\n \
        \       for j in 2...min(1 + dist, n - 1) {\n            add(nums[j])\n    \
        \    }\n\n        var minCost = nums[0] + nums[1] + sumOfSmallest(m)\n\n   \
        \     for i in 2...(n - k + 1) {\n            remove(nums[i])\n            if\
        \ i + dist < n {\n                add(nums[i + dist])\n            }\n     \
        \       let currentCost = nums[0] + nums[i] + sumOfSmallest(m)\n           \
        \ if currentCost < minCost { minCost = currentCost }\n        }\n\n        return\
        \ minCost\n    }\n}"
      kotlin: "import kotlin.math.min\nimport kotlin.random.Random\n\nclass Solution\
        \ {\n    class TreapNode(val value: Int) {\n        val priority = Random.nextInt()\n\
        \        var size = 1\n        var sum = value.toLong()\n        var left: TreapNode?\
        \ = null\n        var right: TreapNode? = null\n\n        fun update() {\n \
        \           size = 1 + (left?.size ?: 0) + (right?.size ?: 0)\n            sum\
        \ = value.toLong() + (left?.sum ?: 0L) + (right?.sum ?: 0L)\n        }\n   \
        \ }\n\n    private fun splitByValue(node: TreapNode?, value: Int): Pair<TreapNode?,\
        \ TreapNode?> {\n        if (node == null) return null to null\n        return\
        \ if (node.value <= value) {\n            val (l, r) = splitByValue(node.right,\
        \ value)\n            node.right = l\n            node.update()\n          \
        \  node to r\n        } else {\n            val (l, r) = splitByValue(node.left,\
        \ value)\n            node.left = r\n            node.update()\n           \
        \ l to node\n        }\n    }\n\n    private fun splitBySize(node: TreapNode?,\
        \ k: Int): Pair<TreapNode?, TreapNode?> {\n        if (node == null) return\
        \ null to null\n        val leftSize = node.left?.size ?: 0\n        return\
        \ if (leftSize >= k) {\n            val (l, r) = splitBySize(node.left, k)\n\
        \            node.left = r\n            node.update()\n            l to node\n\
        \        } else {\n            val (l, r) = splitBySize(node.right, k - leftSize\
        \ - 1)\n            node.right = l\n            node.update()\n            node\
        \ to r\n        }\n    }\n\n    private fun merge(l: TreapNode?, r: TreapNode?):\
        \ TreapNode? {\n        if (l == null) return r\n        if (r == null) return\
        \ l\n        return if (l.priority > r.priority) {\n            l.right = merge(l.right,\
        \ r)\n            l.update()\n            l\n        } else {\n            r.left\
        \ = merge(l, r.left)\n            r.update()\n            r\n        }\n   \
        \ }\n\n    fun minimumCost(nums: IntArray, k: Int, dist: Int): Long {\n    \
        \    val n = nums.size\n        val m = k - 2\n        var root: TreapNode?\
        \ = null\n\n        fun add(val0: Int) {\n            val (l, r) = splitByValue(root,\
        \ val0)\n            root = merge(merge(l, TreapNode(val0)), r)\n        }\n\
        \n        fun remove(val0: Int) {\n            val (l, r) = splitByValue(root,\
        \ val0 - 1)\n            val (mid, rr) = splitByValue(r, val0)\n           \
        \ val (_, rest) = splitBySize(mid, 1)\n            root = merge(merge(l, rest),\
        \ rr)\n        }\n\n        fun sumOfSmallest(k0: Int): Long {\n           \
        \ if (k0 <= 0) return 0L\n            val (l, r) = splitBySize(root, k0)\n \
        \           val res = l?.sum ?: 0L\n            root = merge(l, r)\n       \
        \     return res\n        }\n\n        for (j in 2..min(1 + dist, n - 1)) {\n\
        \            add(nums[j])\n        }\n\n        var minCost = nums[0].toLong()\
        \ + nums[1].toLong() + sumOfSmallest(m)\n\n        for (i in 2..n - k + 1) {\n\
        \            remove(nums[i])\n            if (i + dist < n) {\n            \
        \    add(nums[i + dist])\n            }\n            val curr = nums[0].toLong()\
        \ + nums[i].toLong() + sumOfSmallest(m)\n            if (curr < minCost) minCost\
        \ = curr\n        }\n\n        return minCost\n    }\n}"
      dart: "import 'dart:math';\n\nclass TreapNode {\n  int value;\n  int priority;\n\
        \  int size = 1;\n  int sum;\n  TreapNode? left, right;\n\n  TreapNode(this.value)\
        \ : priority = Random().nextInt(1 << 31), sum = value;\n\n  void update() {\n\
        \    size = 1 + (left?.size ?? 0) + (right?.size ?? 0);\n    sum = value + (left?.sum\
        \ ?? 0) + (right?.sum ?? 0);\n  }\n}\n\nclass Solution {\n  TreapNode? merge(TreapNode?\
        \ l, TreapNode? r) {\n    if (l == null) return r;\n    if (r == null) return\
        \ l;\n    if (l.priority > r.priority) {\n      l.right = merge(l.right, r);\n\
        \      l.update();\n      return l;\n    } else {\n      r.left = merge(l, r.left);\n\
        \      r.update();\n      return r;\n    }\n  }\n\n  List<TreapNode?> splitByValue(TreapNode?\
        \ node, int val) {\n    if (node == null) return [null, null];\n    if (node.value\
        \ <= val) {\n      var res = splitByValue(node.right, val);\n      node.right\
        \ = res[0];\n      node.update();\n      return [node, res[1]];\n    } else\
        \ {\n      var res = splitByValue(node.left, val);\n      node.left = res[1];\n\
        \      node.update();\n      return [res[0], node];\n    }\n  }\n\n  List<TreapNode?>\
        \ splitBySize(TreapNode? node, int k) {\n    if (node == null) return [null,\
        \ null];\n    int leftSize = node.left?.size ?? 0;\n    if (leftSize >= k) {\n\
        \      var res = splitBySize(node.left, k);\n      node.left = res[1];\n   \
        \   node.update();\n      return [res[0], node];\n    } else {\n      var res\
        \ = splitBySize(node.right, k - leftSize - 1);\n      node.right = res[0];\n\
        \      node.update();\n      return [node, res[1]];\n    }\n  }\n\n  int minimumCost(List<int>\
        \ nums, int k, int dist) {\n    int n = nums.length;\n    int m = k - 2;\n \
        \   TreapNode? root;\n\n    TreapNode? add(TreapNode? r, int val) {\n      var\
        \ parts = splitByValue(r, val);\n      return merge(merge(parts[0], TreapNode(val)),\
        \ parts[1]);\n    }\n\n    TreapNode? remove(TreapNode? r, int val) {\n    \
        \  var parts1 = splitByValue(r, val - 1);\n      var parts2 = splitByValue(parts1[1],\
        \ val);\n      var parts3 = splitBySize(parts2[0], 1);\n      return merge(merge(parts1[0],\
        \ parts3[1]), parts2[1]);\n    }\n\n    int sumSmallest(int count) {\n     \
        \ if (count <= 0) return 0;\n      var parts = splitBySize(root, count);\n \
        \     int res = parts[0]?.sum ?? 0;\n      root = merge(parts[0], parts[1]);\n\
        \      return res;\n    }\n\n    for (int j = 2; j <= min(1 + dist, n - 1);\
        \ j++) {\n      root = add(root, nums[j]);\n    }\n\n    int minCost = nums[0]\
        \ + nums[1] + sumSmallest(m);\n    for (int i = 2; i <= n - k + 1; i++) {\n\
        \      root = remove(root, nums[i]);\n      if (i + dist < n) {\n        root\
        \ = add(root, nums[i + dist]);\n      }\n      int currentCost = nums[0] + nums[i]\
        \ + sumSmallest(m);\n      if (currentCost < minCost) minCost = currentCost;\n\
        \    }\n    return minCost;\n  }\n}"
      go: "import (\n\t\"math/rand\"\n)\n\ntype TreapNode struct {\n\tvalue, size int\n\
        \tpriority    int64\n\tsum         int64\n\tleft, right *TreapNode\n}\n\nfunc\
        \ newNode(val int) *TreapNode {\n\treturn &TreapNode{value: val, size: 1, priority:\
        \ rand.Int63(), sum: int64(val)}\n}\n\nfunc (n *TreapNode) update() {\n\tn.size\
        \ = 1\n\tn.sum = int64(n.value)\n\tif n.left != nil {\n\t\tn.size += n.left.size\n\
        \t\tn.sum += n.left.sum\n\t}\n\tif n.right != nil {\n\t\tn.size += n.right.size\n\
        \t\tn.sum += n.right.sum\n\t}\n}\n\nfunc splitByValue(node *TreapNode, val int)\
        \ (*TreapNode, *TreapNode) {\n\tif node == nil {\n\t\treturn nil, nil\n\t}\n\
        \tif node.value <= val {\n\t\tl, r := splitByValue(node.right, val)\n\t\tnode.right\
        \ = l\n\t\tnode.update()\n\t\treturn node, r\n\t} else {\n\t\tl, r := splitByValue(node.left,\
        \ val)\n\t\tnode.left = r\n\t\tnode.update()\n\t\treturn l, node\n\t}\n}\n\n\
        func splitBySize(node *TreapNode, k int) (*TreapNode, *TreapNode) {\n\tif node\
        \ == nil {\n\t\treturn nil, nil\n\t}\n\tleftSize := 0\n\tif node.left != nil\
        \ {\n\t\tleftSize = node.left.size\n\t}\n\tif leftSize >= k {\n\t\tl, r := splitBySize(node.left,\
        \ k)\n\t\tnode.left = r\n\t\tnode.update()\n\t\treturn l, node\n\t} else {\n\
        \t\tl, r := splitBySize(node.right, k-leftSize-1)\n\t\tnode.right = l\n\t\t\
        node.update()\n\t\treturn node, r\n\t}\n}\n\nfunc merge(l, r *TreapNode) *TreapNode\
        \ {\n\tif l == nil {\n\t\treturn r\n\t}\n\tif r == nil {\n\t\treturn l\n\t}\n\
        \tif l.priority > r.priority {\n\t\tl.right = merge(l.right, r)\n\t\tl.update()\n\
        \t\treturn l\n\t} else {\n\t\tr.left = merge(l, r.left)\n\t\tr.update()\n\t\t\
        return r\n\t}\n}\n\nfunc minimumCost(nums []int, k int, dist int) int64 {\n\t\
        n := len(nums)\n\tm := k - 2\n\tvar root *TreapNode\n\n\tadd := func(val int)\
        \ {\n\t\tl, r := splitByValue(root, val)\n\t\troot = merge(merge(l, newNode(val)),\
        \ r)\n\t}\n\tremove := func(val int) {\n\t\tl, r := splitByValue(root, val-1)\n\
        \t\tmid, rr := splitByValue(r, val)\n\t\t_, rest := splitBySize(mid, 1)\n\t\t\
        root = merge(merge(l, rest), rr)\n\t}\n\tsumSmallest := func(count int) int64\
        \ {\n\t\tif count <= 0 {\n\t\t\treturn 0\n\t\t}\n\t\tl, r := splitBySize(root,\
        \ count)\n\t\tres := l.sum\n\t\troot = merge(l, r)\n\t\treturn res\n\t}\n\n\t\
        limit := 1 + dist\n\tif n-1 < limit {\n\t\tlimit = n - 1\n\t}\n\tfor j := 2;\
        \ j <= limit; j++ {\n\t\tadd(nums[j])\n\t}\n\n\tminCost := int64(nums[0]) +\
        \ int64(nums[1]) + sumSmallest(m)\n\tfor i := 2; i <= n-k+1; i++ {\n\t\tremove(nums[i])\n\
        \t\tif i+dist < n {\n\t\t\tadd(nums[i+dist])\n\t\t}\n\t\tcurr := int64(nums[0])\
        \ + int64(nums[i]) + sumSmallest(m)\n\t\tif curr < minCost {\n\t\t\tminCost\
        \ = curr\n\t\t}\n\t}\n\treturn minCost\n}"
      ruby: '// Generation failed for Ruby

        // Reason: Parsing failed'
      scala: '// Generation failed for Scala

        // Reason: Parsing failed'
      rust: '// Generation failed for Rust

        // Reason: Parsing failed'
      racket: '// Generation failed for Racket

        // Reason: Parsing failed'
      erlang: '// Generation failed for Erlang

        // Reason: Parsing failed'
      elixir: '// Generation failed for Elixir

        // Reason: Parsing failed'
    approach: 'The problem asks to find the minimum cost to divide an array into $k$
      contiguous subarrays. The cost is the sum of the first elements of these subarrays.
      Given the condition that the difference between the starting index of the second
      and the $k$-th subarray is at most `dist`, the problem reduces to picking $k-1$
      indices $i_1, i_2, \dots, i_{k-1}$ such that $1 \le i_1 < i_2 < \dots < i_{k-1}
      \le n-1$ and $i_{k-1} - i_1 \le dist$. The total cost is $\text{nums}[0] + \text{nums}[i_1]
      + \sum_{j=2}^{k-1} \text{nums}[i_j]$. For a fixed $i_1$, to minimize this sum,
      we must pick the $k-2$ smallest elements from the range of indices $(i_1, i_1
      + dist]$ that are within the bounds of the array.


      We utilize a sliding window approach as $i_1$ moves from $1$ to $n-k+1$. The candidate
      pool for the remaining $k-2$ indices is the window of elements $\text{nums}[i_1+1
      \dots \min(n-1, i_1+dist)]$. To efficiently maintain and query the sum of the
      $k-2$ smallest elements in this sliding window, we use different data structures
      depending on the language''s capabilities. In C++ and Java, we use multisets or
      TreeMaps. In languages like C, Python, and JavaScript, we use coordinate compression
      combined with a Binary Indexed Tree (Fenwick Tree) to perform $O(\log N)$ updates
      and $O(\log N)$ queries using binary lifting to find the $k$-th smallest prefix
      sum. This ensures an overall time complexity of $O(n \log n)$.'
    time_complexity: O(n \log n) where n is the length of the array. Sorting for coordinate
      compression takes $O(n \log n)$, and the sliding window iterates through the array
      once, with each update and query on the Fenwick Tree or Balanced BST taking $O(\log
      n)$.
    space_complexity: O(n) to store the Fenwick tree or other data structures, the coordinate
      compression mapping, and the input array.
    elapsed_time: 422.7920169830322
    model: gemini-3-flash-preview
    generated_at: '2026-02-04 05:34:29 '
---

## Problem #3013: Divide an Array Into Subarrays With Minimum Cost II

**Difficulty:** Hard

**Topics:** Array, Hash Table, Sliding Window, Heap (Priority Queue)

## Problem Description

<p>You are given a <strong>0-indexed</strong> array of integers <code>nums</code> of length <code>n</code>, and two <strong>positive</strong> integers <code>k</code> and <code>dist</code>.</p>

<p>The <strong>cost</strong> of an array is the value of its <strong>first</strong> element. For example, the cost of <code>[1,2,3]</code> is <code>1</code> while the cost of <code>[3,4,1]</code> is <code>3</code>.</p>

<p>You need to divide <code>nums</code> into <code>k</code> <strong>disjoint contiguous </strong><span data-keyword="subarray-nonempty">subarrays</span>, such that the difference between the starting index of the <strong>second</strong> subarray and the starting index of the <code>kth</code> subarray should be <strong>less than or equal to</strong> <code>dist</code>. In other words, if you divide <code>nums</code> into the subarrays <code>nums[0..(i<sub>1</sub> - 1)], nums[i<sub>1</sub>..(i<sub>2</sub> - 1)], ..., nums[i<sub>k-1</sub>..(n - 1)]</code>, then <code>i<sub>k-1</sub> - i<sub>1</sub> &lt;= dist</code>.</p>

<p>Return <em>the <strong>minimum</strong> possible sum of the cost of these</em> <em>subarrays</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,6,4,2], k = 3, dist = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because i<sub>k-1</sub> - i<sub>1</sub> is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,1,2,2,2,1], k = 4, dist = 3
<strong>Output:</strong> 15
<strong>Explanation:</strong> The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because i<sub>k-1</sub> - i<sub>1</sub> is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between i<sub>k-1</sub> and i<sub>1</sub> is 5 - 1 = 4, which is greater than dist.
It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,8,18,9], k = 3, dist = 1
<strong>Output:</strong> 36
<strong>Explanation:</strong> The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because i<sub>k-1</sub> - i<sub>1</sub> is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
The division [10], [8,18], and [9] is not valid, because the difference between i<sub>k-1</sub> and i<sub>1</sub> is 3 - 1 = 2, which is greater than dist.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>3 &lt;= k &lt;= n</code></li>
	<li><code>k - 2 &lt;= dist &lt;= n - 2</code></li>
</ul>


## Hints

1. For each `i > 0`, try each `nums[i]` as the first element of the second subarray. We need to find the sum of `k - 2` smallest values in the index range `[i + 1, min(i + dist, n - 1)]`.

2. Typically, we use a max heap to maintain the top `k - 2` smallest values dynamically. Here we also have a sliding window, which is the index range `[i + 1, min(i + dist, n - 1)]`. We can use another min heap to put unselected values for future use.

3. Update the two heaps when iteration over `i`. Ordered/Tree sets are also a good choice since we have to delete elements.

4. If the max heap’s size is less than `k - 2`, use the min heap’s value to fill it. If the maximum value in the max heap is larger than the smallest value in the min heap, swap them in the two heaps.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to find the minimum cost to divide an array into $k$ contiguous subarrays. The cost is the sum of the first elements of these subarrays. Given the condition that the difference between the starting index of the second and the $k$-th subarray is at most `dist`, the problem reduces to picking $k-1$ indices $i_1, i_2, \dots, i_{k-1}$ such that $1 \le i_1 < i_2 < \dots < i_{k-1} \le n-1$ and $i_{k-1} - i_1 \le dist$. The total cost is $\text{nums}[0] + \text{nums}[i_1] + \sum_{j=2}^{k-1} \text{nums}[i_j]$. For a fixed $i_1$, to minimize this sum, we must pick the $k-2$ smallest elements from the range of indices $(i_1, i_1 + dist]$ that are within the bounds of the array.

We utilize a sliding window approach as $i_1$ moves from $1$ to $n-k+1$. The candidate pool for the remaining $k-2$ indices is the window of elements $\text{nums}[i_1+1 \dots \min(n-1, i_1+dist)]$. To efficiently maintain and query the sum of the $k-2$ smallest elements in this sliding window, we use different data structures depending on the language's capabilities. In C++ and Java, we use multisets or TreeMaps. In languages like C, Python, and JavaScript, we use coordinate compression combined with a Binary Indexed Tree (Fenwick Tree) to perform $O(\log N)$ updates and $O(\log N)$ queries using binary lifting to find the $k$-th smallest prefix sum. This ensures an overall time complexity of $O(n \log n)$.

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
    long long minimumCost(vector<int>& nums, int k, int dist) {
        int n = nums.size();
        multiset<int> small, large;
        long long small_sum = 0;
        int k_minus_2 = k - 2;

        auto add = [&](int val) {
            small.insert(val);
            small_sum += val;
            if (small.size() > k_minus_2) {
                auto it = prev(small.end());
                int v = *it;
                small_sum -= v;
                large.insert(v);
                small.erase(it);
            }
        };

        auto remove = [&](int val) {
            auto it = small.find(val);
            if (it != small.end()) {
                small_sum -= val;
                small.erase(it);
                if (!large.empty()) {
                    auto it2 = large.begin();
                    int v = *it2;
                    small_sum += v;
                    small.insert(v);
                    large.erase(it2);
                }
            } else {
                large.erase(large.find(val));
            }
        };

        for (int i = 2; i <= 1 + dist && i < n; i++) add(nums[i]);
        long long ans = (long long)nums[0] + nums[1] + small_sum;

        for (int i1 = 2; i1 <= n - k + 1; i1++) {
            remove(nums[i1]);
            if (i1 + dist < n) add(nums[i1 + dist]);
            ans = min(ans, (long long)nums[0] + nums[i1] + small_sum);
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
import java.util.*;

class Solution {
    private TreeMap<Integer, Integer> small = new TreeMap<>();
    private TreeMap<Integer, Integer> large = new TreeMap<>();
    private int smallCount = 0;
    private long smallSum = 0;

    public long minimumCost(int[] nums, int k, int dist) {
        int n = nums.length;
        int k2 = k - 2;
        for (int i = 2; i <= 1 + dist && i < n; i++) add(nums[i], k2);
        long ans = (long) nums[0] + nums[1] + smallSum;

        for (int i1 = 2; i1 <= n - k + 1; i1++) {
            remove(nums[i1], k2);
            if (i1 + dist < n) add(nums[i1 + dist], k2);
            ans = Math.min(ans, (long) nums[0] + nums[i1] + smallSum);
        }
        return ans;
    }

    private void add(int val, int k2) {
        small.put(val, small.getOrDefault(val, 0) + 1);
        smallSum += val;
        smallCount++;
        if (smallCount > k2) {
            int last = small.lastKey();
            smallSum -= last;
            removeOne(small, last);
            smallCount--;
            large.put(last, large.getOrDefault(last, 0) + 1);
        }
    }

    private void remove(int val, int k2) {
        if (small.containsKey(val)) {
            removeOne(small, val);
            smallSum -= val;
            smallCount--;
            if (!large.isEmpty()) {
                int first = large.firstKey();
                small.put(first, small.getOrDefault(first, 0) + 1);
                smallSum += first;
                smallCount++;
                removeOne(large, first);
            }
        } else {
            removeOne(large, val);
        }
    }

    private void removeOne(TreeMap<Integer, Integer> map, int val) {
        int count = map.get(val);
        if (count == 1) map.remove(val);
        else map.put(val, count - 1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        k_small = k - 2
        unique_vals = sorted(list(set(nums[1:])))
        val_map = {v: i + 1 for i, v in enumerate(unique_vals)}
        n_uniq = len(unique_vals)
        bit_cnt = [0] * (n_uniq + 1)
        bit_sum = [0] * (n_uniq + 1)

        def update(val, delta):
            idx = val_map[val]
            s = val * delta
            while idx <= n_uniq:
                bit_cnt[idx] += delta
                bit_sum[idx] += s
                idx += idx & -idx

        def query(target):
            pos = 0
            cnt = 0
            sm = 0
            for i in range(n_uniq.bit_length(), -1, -1):
                pw = 1 << i
                if pos + pw <= n_uniq and cnt + bit_cnt[pos + pw] < target:
                    pos += pw
                    cnt += bit_cnt[pos]
                    sm += bit_sum[pos]
            return sm + (target - cnt) * unique_vals[pos]

        for i in range(2, min(n, 2 + dist)):
            update(nums[i], 1)
        ans = nums[0] + nums[1] + query(k_small)

        for i1 in range(2, n - k + 2):
            update(nums[i1], -1)
            if i1 + dist < n:
                update(nums[i1 + dist], 1)
            ans = min(ans, nums[0] + nums[i1] + query(k_small))
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        k_small = k - 2
        unique_vals = sorted(list(set(nums[1:])))
        val_map = {v: i + 1 for i, v in enumerate(unique_vals)}
        n_uniq = len(unique_vals)
        bit_cnt = [0] * (n_uniq + 1)
        bit_sum = [0] * (n_uniq + 1)

        def update(val, delta):
            idx = val_map[val]
            s = val * delta
            while idx <= n_uniq:
                bit_cnt[idx] += delta
                bit_sum[idx] += s
                idx += idx & -idx

        def query(target):
            pos = 0
            cnt = 0
            sm = 0
            for i in range(n_uniq.bit_length(), -1, -1):
                pw = 1 << i
                if pos + pw <= n_uniq and cnt + bit_cnt[pos + pw] < target:
                    pos += pw
                    cnt += bit_cnt[pos]
                    sm += bit_sum[pos]
            return sm + (target - cnt) * unique_vals[pos]

        for i in range(2, min(n, 2 + dist)):
            update(nums[i], 1)
        ans = nums[0] + nums[1] + query(k_small)

        for i1 in range(2, n - k + 2):
            update(nums[i1], -1)
            if i1 + dist < n:
                update(nums[i1 + dist], 1)
            ans = min(ans, nums[0] + nums[i1] + query(k_small))
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

int compare_ints(const void* a, const void* b) {
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

long long bit_cnt[100005], bit_sum[100005];
int num_uniq;

void update(int idx, int delta, int val, int n) {
    long long s = (long long)val * delta;
    for (; idx <= n; idx += idx & -idx) {
        bit_cnt[idx] += delta;
        bit_sum[idx] += s;
    }
}

long long query(int k, int* unique_vals) {
    int pos = 0;
    long long cnt = 0, sum = 0;
    for (int i = 1 << 17; i > 0; i >>= 1) {
        if (pos + i <= num_uniq && cnt + bit_cnt[pos + i] < k) {
            pos += i;
            cnt += bit_cnt[pos];
            sum += bit_sum[pos];
        }
    }
    return sum + (long long)(k - cnt) * unique_vals[pos];
}

long long minimumCost(int* nums, int n, int k, int dist) {
    int* sorted_nums = (int*)malloc((n - 1) * sizeof(int));
    for (int i = 0; i < n - 1; i++) sorted_nums[i] = nums[i + 1];
    qsort(sorted_nums, n - 1, sizeof(int), compare_ints);

    int* unique_vals = (int*)malloc((n - 1) * sizeof(int));
    num_uniq = 0;
    if (n > 1) unique_vals[num_uniq++] = sorted_nums[0];
    for (int i = 1; i < n - 1; i++) {
        if (sorted_nums[i] != sorted_nums[i - 1]) unique_vals[num_uniq++] = sorted_nums[i];
    }

    memset(bit_cnt, 0, sizeof(bit_cnt));
    memset(bit_sum, 0, sizeof(bit_sum));

    int get_rank(int val) {
        int l = 0, r = num_uniq - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (unique_vals[mid] == val) return mid + 1;
            if (unique_vals[mid] < val) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }

    for (int i = 2; i <= 1 + dist && i < n; i++) update(get_rank(nums[i]), 1, nums[i], num_uniq);
    long long ans = (long long)nums[0] + nums[1] + query(k - 2, unique_vals);

    for (int i1 = 2; i1 <= n - k + 1; i1++) {
        update(get_rank(nums[i1]), -1, nums[i1], num_uniq);
        if (i1 + dist < n) update(get_rank(nums[i1 + dist]), 1, nums[i1 + dist], num_uniq);
        long long cur = (long long)nums[0] + nums[i1] + query(k - 2, unique_vals);
        if (cur < ans) ans = cur;
    }

    free(sorted_nums); free(unique_vals);
    return ans;
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
    public long MinimumCost(int[] nums, int k, int dist) {
        int n = nums.Length;
        int k2 = k - 2;
        SortedSet<(int val, int idx)> small = new SortedSet<(int val, int idx)>();
        SortedSet<(int val, int idx)> large = new SortedSet<(int val, int idx)>();
        long smallSum = 0;

        void Add(int val, int i) {
            small.Add((val, i));
            smallSum += val;
            if (small.Count > k2) {
                var last = small.Max;
                smallSum -= last.val;
                small.Remove(last);
                large.Add(last);
            }
        }

        void Remove(int val, int i) {
            if (small.Contains((val, i))) {
                small.Remove((val, i));
                smallSum -= val;
                if (large.Count > 0) {
                    var first = large.Min;
                    smallSum += first.val;
                    small.Add(first);
                    large.Remove(first);
                }
            } else {
                large.Remove((val, i));
            }
        }

        for (int i = 2; i <= 1 + dist && i < n; i++) Add(nums[i], i);
        long ans = (long)nums[0] + nums[1] + smallSum;

        for (int i1 = 2; i1 <= n - k + 1; i1++) {
            Remove(nums[i1], i1);
            if (i1 + dist < n) Add(nums[i1 + dist], i1 + dist);
            ans = Math.min(ans, (long)nums[0] + nums[i1] + smallSum);
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
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} dist
 * @return {number}
 */
var minimumCost = function(nums, k, dist) {
    const n = nums.length;
    const k2 = k - 2;
    const uniqueVals = Array.from(new Set(nums.slice(1))).sort((a, b) => a - b);
    const valMap = new Map();
    uniqueVals.forEach((v, i) => valMap.set(v, i + 1));
    const nUniq = uniqueVals.length;
    const bitCnt = new Float64Array(nUniq + 1);
    const bitSum = new Float64Array(nUniq + 1);

    function update(val, delta) {
        let idx = valMap.get(val);
        const s = val * delta;
        while (idx <= nUniq) {
            bitCnt[idx] += delta;
            bitSum[idx] += s;
            idx += idx & -idx;
        }
    }

    function query(target) {
        let pos = 0, cnt = 0, sm = 0;
        for (let i = Math.floor(Math.log2(nUniq)); i >= 0; i--) {
            const pw = 1 << i;
            if (pos + pw <= nUniq && cnt + bitCnt[pos + pw] < target) {
                pos += pw;
                cnt += bitCnt[pos];
                sm += bitSum[pos];
            }
        }
        return sm + (target - cnt) * uniqueVals[pos];
    }

    for (let i = 2; i <= 1 + dist && i < n; i++) update(nums[i], 1);
    let ans = nums[0] + nums[1] + query(k2);

    for (let i1 = 2; i1 <= n - k + 1; i1++) {
        update(nums[i1], -1);
        if (i1 + dist < n) update(nums[i1 + dist], 1);
        ans = Math.min(ans, nums[0] + nums[i1] + query(k2));
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class TreapNode {
  value: number;
  priority: number;
  size: number;
  sum: number;
  left: TreapNode | null = null;
  right: TreapNode | null = null;
  constructor(value: number) {
    this.value = value;
    this.priority = Math.random();
    this.size = 1;
    this.sum = value;
  }
}

function getSize(node: TreapNode | null): number {
  return node ? node.size : 0;
}

function getSum(node: TreapNode | null): number {
  return node ? node.sum : 0;
}

function update(node: TreapNode | null) {
  if (node) {
    node.size = 1 + getSize(node.left) + getSize(node.right);
    node.sum = node.value + getSum(node.left) + getSum(node.right);
  }
}

function splitBySize(node: TreapNode | null, k: number): [TreapNode | null, TreapNode | null] {
  if (!node) return [null, null];
  const leftSize = getSize(node.left);
  if (leftSize >= k) {
    const [left, right] = splitBySize(node.left, k);
    node.left = right;
    update(node);
    return [left, node];
  } else {
    const [left, right] = splitBySize(node.right, k - leftSize - 1);
    node.right = left;
    update(node);
    return [node, right];
  }
}

function splitByValue(node: TreapNode | null, value: number): [TreapNode | null, TreapNode | null] {
  if (!node) return [null, null];
  if (node.value <= value) {
    const [l, r] = splitByValue(node.right, value);
    node.right = l;
    update(node);
    return [node, r];
  } else {
    const [l, r] = splitByValue(node.left, value);
    node.left = r;
    update(node);
    return [l, node];
  }
}

function merge(left: TreapNode | null, right: TreapNode | null): TreapNode | null {
  if (!left || !right) return left || right;
  if (left.priority > right.priority) {
    left.right = merge(left.right, right);
    update(left);
    return left;
  } else {
    right.left = merge(left, right.left);
    update(right);
    return right;
  }
}

function minimumCost(nums: number[], k: number, dist: number): number {
  const n = nums.length;
  const m = k - 2;
  let root: TreapNode | null = null;
  for (let j = 2; j <= Math.min(1 + dist, n - 1); j++) {
    root = merge(root, null);
    const [l, r] = splitByValue(root, nums[j]);
    root = merge(merge(l, new TreapNode(nums[j])), r);
  }

  const getSmallestSum = (k: number): number => {
    if (k === 0) return 0;
    const [l, r] = splitBySize(root, k);
    const res = getSum(l);
    root = merge(l, r);
    return res;
  };

  let minCost = nums[0] + nums[1] + getSmallestSum(m);

  for (let i = 2; i <= n - k + 1; i++) {
    let [l, r] = splitByValue(root, nums[i] - 1);
    let [mid, rr] = splitByValue(r, nums[i]);
    let [one, rest] = splitBySize(mid, 1);
    root = merge(l, merge(rest, rr));
    if (i + dist < n) {
      let [l2, r2] = splitByValue(root, nums[i + dist]);
      root = merge(merge(l2, new TreapNode(nums[i + dist])), r2);
    }
    minCost = Math.min(minCost, nums[0] + nums[i] + getSmallestSum(m));
  }

  return minCost;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minimumCost($nums, $k, $dist) {
        $n = count($nums);
        $m = $k - 2;
        $root = null;
        for ($j = 2; $j <= min(1 + $dist, $n - 1); $j++) {
            $root = $this->add($root, $nums[$j]);
        }
        $minCost = $nums[0] + $nums[1] + $this->sumOfSmallest($root, $m);
        for ($i = 2; $i <= $n - $k + 1; $i++) {
            $root = $this->remove($root, $nums[$i]);
            if ($i + $dist < $n) {
                $root = $this->add($root, $nums[$i + $dist]);
            }
            $currentCost = $nums[0] + $nums[$i] + $this->sumOfSmallest($root, $m);
            if ($currentCost < $minCost) {
                $minCost = $currentCost;
            }
        }
        return $minCost;
    }

    private function add($root, $val) {
        [$l, $r] = $this->splitByValue($root, $val);
        return $this->merge($this->merge($l, new TreapNode($val)), $r);
    }

    private function remove($root, $val) {
        [$l, $r] = $this->splitByValue($root, $val - 1);
        [$mid, $rr] = $this->splitByValue($r, $val);
        [$one, $rest] = $this->splitBySize($mid, 1);
        return $this->merge($this->merge($l, $rest), $rr);
    }

    private function sumOfSmallest(&$root, $k) {
        if ($k <= 0) return 0;
        [$l, $r] = $this->splitBySize($root, $k);
        $res = $l ? $l->sum : 0;
        $root = $this->merge($l, $r);
        return $res;
    }

    private function splitByValue($node, $val) {
        if (!$node) return [null, null];
        if ($node->value <= $val) {
            [$l, $r] = $this->splitByValue($node->right, $val);
            $node->right = $l;
            $node->update();
            return [$node, $r];
        } else {
            [$l, $r] = $this->splitByValue($node->left, $val);
            $node->left = $r;
            $node->update();
            return [$l, $node];
        }
    }

    private function splitBySize($node, $k) {
        if (!$node) return [null, null];
        $leftSize = $node->left ? $node->left->size : 0;
        if ($leftSize >= $k) {
            [$l, $r] = $this->splitBySize($node->left, $k);
            $node->left = $r;
            $node->update();
            return [$l, $node];
        } else {
            [$l, $r] = $this->splitBySize($node->right, $k - $leftSize - 1);
            $node->right = $l;
            $node->update();
            return [$node, $r];
        }
    }

    private function merge($l, $r) {
        if (!$l || !$r) return $l ?: $r;
        if ($l->priority > $r->priority) {
            $l->right = $this->merge($l->right, $r);
            $l->update();
            return $l;
        } else {
            $r->left = $this->merge($l, $r->left);
            $r->update();
            return $r;
        }
    }
}

class TreapNode {
    public $value, $priority, $size, $sum, $left, $right;
    function __construct($val) {
        $this->value = $val;
        $this->priority = mt_rand(0, 1000000000);
        $this->size = 1;
        $this->sum = $val;
    }
    function update() {
        $this->size = 1 + ($this->left ? $this->left->size : 0) + ($this->right ? $this->right->size : 0);
        $this->sum = $this->value + ($this->left ? $this->left->sum : 0) + ($this->right ? $this->right->sum : 0);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    class TreapNode {
        var value: Int
        var priority: Int
        var size: Int
        var sum: Int
        var left: TreapNode? = nil
        var right: TreapNode? = nil
        init(_ val: Int) {
            self.value = val
            self.priority = Int.random(in: 0...Int.max)
            self.size = 1
            self.sum = val
        }
        func update() {
            size = 1 + (left?.size ?? 0) + (right?.size ?? 0)
            sum = value + (left?.sum ?? 0) + (right?.sum ?? 0)
        }
    }

    func splitByValue(_ node: TreapNode?, _ val: Int) -> (TreapNode?, TreapNode?) {
        guard let node = node else { return (nil, nil) }
        if node.value <= val {
            let (l, r) = splitByValue(node.right, val)
            node.right = l
            node.update()
            return (node, r)
        } else {
            let (l, r) = splitByValue(node.left, val)
            node.left = r
            node.update()
            return (l, node)
        }
    }

    func splitBySize(_ node: TreapNode?, _ k: Int) -> (TreapNode?, TreapNode?) {
        guard let node = node else { return (nil, nil) }
        let leftSize = node.left?.size ?? 0
        if leftSize >= k {
            let (l, r) = splitBySize(node.left, k)
            node.left = r
            node.update()
            return (l, node)
        } else {
            let (l, r) = splitBySize(node.right, k - leftSize - 1)
            node.right = l
            node.update()
            return (node, r)
        }
    }

    func merge(_ l: TreapNode?, _ r: TreapNode?) -> TreapNode? {
        if l == nil { return r }
        if r == nil { return l }
        if l!.priority > r!.priority {
            l!.right = merge(l!.right, r)
            l!.update()
            return l
        } else {
            r!.left = merge(l, r!.left)
            r!.update()
            return r
        }
    }

    func minimumCost(_ nums: [Int], _ k: Int, _ dist: Int) -> Int {
        let n = nums.count
        let m = k - 2
        var root: TreapNode? = nil

        func add(_ val: Int) {
            let (l, r) = splitByValue(root, val)
            root = merge(merge(l, TreapNode(val)), r)
        }

        func remove(_ val: Int) {
            let (l, r) = splitByValue(root, val - 1)
            let (mid, rr) = splitByValue(r, val)
            let (_, rest) = splitBySize(mid, 1)
            root = merge(merge(l, rest), rr)
        }

        func sumOfSmallest(_ k: Int) -> Int {
            if k <= 0 { return 0 }
            let (l, r) = splitBySize(root, k)
            let res = l?.sum ?? 0
            root = merge(l, r)
            return res
        }

        for j in 2...min(1 + dist, n - 1) {
            add(nums[j])
        }

        var minCost = nums[0] + nums[1] + sumOfSmallest(m)

        for i in 2...(n - k + 1) {
            remove(nums[i])
            if i + dist < n {
                add(nums[i + dist])
            }
            let currentCost = nums[0] + nums[i] + sumOfSmallest(m)
            if currentCost < minCost { minCost = currentCost }
        }

        return minCost
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.min
import kotlin.random.Random

class Solution {
    class TreapNode(val value: Int) {
        val priority = Random.nextInt()
        var size = 1
        var sum = value.toLong()
        var left: TreapNode? = null
        var right: TreapNode? = null

        fun update() {
            size = 1 + (left?.size ?: 0) + (right?.size ?: 0)
            sum = value.toLong() + (left?.sum ?: 0L) + (right?.sum ?: 0L)
        }
    }

    private fun splitByValue(node: TreapNode?, value: Int): Pair<TreapNode?, TreapNode?> {
        if (node == null) return null to null
        return if (node.value <= value) {
            val (l, r) = splitByValue(node.right, value)
            node.right = l
            node.update()
            node to r
        } else {
            val (l, r) = splitByValue(node.left, value)
            node.left = r
            node.update()
            l to node
        }
    }

    private fun splitBySize(node: TreapNode?, k: Int): Pair<TreapNode?, TreapNode?> {
        if (node == null) return null to null
        val leftSize = node.left?.size ?: 0
        return if (leftSize >= k) {
            val (l, r) = splitBySize(node.left, k)
            node.left = r
            node.update()
            l to node
        } else {
            val (l, r) = splitBySize(node.right, k - leftSize - 1)
            node.right = l
            node.update()
            node to r
        }
    }

    private fun merge(l: TreapNode?, r: TreapNode?): TreapNode? {
        if (l == null) return r
        if (r == null) return l
        return if (l.priority > r.priority) {
            l.right = merge(l.right, r)
            l.update()
            l
        } else {
            r.left = merge(l, r.left)
            r.update()
            r
        }
    }

    fun minimumCost(nums: IntArray, k: Int, dist: Int): Long {
        val n = nums.size
        val m = k - 2
        var root: TreapNode? = null

        fun add(val0: Int) {
            val (l, r) = splitByValue(root, val0)
            root = merge(merge(l, TreapNode(val0)), r)
        }

        fun remove(val0: Int) {
            val (l, r) = splitByValue(root, val0 - 1)
            val (mid, rr) = splitByValue(r, val0)
            val (_, rest) = splitBySize(mid, 1)
            root = merge(merge(l, rest), rr)
        }

        fun sumOfSmallest(k0: Int): Long {
            if (k0 <= 0) return 0L
            val (l, r) = splitBySize(root, k0)
            val res = l?.sum ?: 0L
            root = merge(l, r)
            return res
        }

        for (j in 2..min(1 + dist, n - 1)) {
            add(nums[j])
        }

        var minCost = nums[0].toLong() + nums[1].toLong() + sumOfSmallest(m)

        for (i in 2..n - k + 1) {
            remove(nums[i])
            if (i + dist < n) {
                add(nums[i + dist])
            }
            val curr = nums[0].toLong() + nums[i].toLong() + sumOfSmallest(m)
            if (curr < minCost) minCost = curr
        }

        return minCost
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class TreapNode {
  int value;
  int priority;
  int size = 1;
  int sum;
  TreapNode? left, right;

  TreapNode(this.value) : priority = Random().nextInt(1 << 31), sum = value;

  void update() {
    size = 1 + (left?.size ?? 0) + (right?.size ?? 0);
    sum = value + (left?.sum ?? 0) + (right?.sum ?? 0);
  }
}

class Solution {
  TreapNode? merge(TreapNode? l, TreapNode? r) {
    if (l == null) return r;
    if (r == null) return l;
    if (l.priority > r.priority) {
      l.right = merge(l.right, r);
      l.update();
      return l;
    } else {
      r.left = merge(l, r.left);
      r.update();
      return r;
    }
  }

  List<TreapNode?> splitByValue(TreapNode? node, int val) {
    if (node == null) return [null, null];
    if (node.value <= val) {
      var res = splitByValue(node.right, val);
      node.right = res[0];
      node.update();
      return [node, res[1]];
    } else {
      var res = splitByValue(node.left, val);
      node.left = res[1];
      node.update();
      return [res[0], node];
    }
  }

  List<TreapNode?> splitBySize(TreapNode? node, int k) {
    if (node == null) return [null, null];
    int leftSize = node.left?.size ?? 0;
    if (leftSize >= k) {
      var res = splitBySize(node.left, k);
      node.left = res[1];
      node.update();
      return [res[0], node];
    } else {
      var res = splitBySize(node.right, k - leftSize - 1);
      node.right = res[0];
      node.update();
      return [node, res[1]];
    }
  }

  int minimumCost(List<int> nums, int k, int dist) {
    int n = nums.length;
    int m = k - 2;
    TreapNode? root;

    TreapNode? add(TreapNode? r, int val) {
      var parts = splitByValue(r, val);
      return merge(merge(parts[0], TreapNode(val)), parts[1]);
    }

    TreapNode? remove(TreapNode? r, int val) {
      var parts1 = splitByValue(r, val - 1);
      var parts2 = splitByValue(parts1[1], val);
      var parts3 = splitBySize(parts2[0], 1);
      return merge(merge(parts1[0], parts3[1]), parts2[1]);
    }

    int sumSmallest(int count) {
      if (count <= 0) return 0;
      var parts = splitBySize(root, count);
      int res = parts[0]?.sum ?? 0;
      root = merge(parts[0], parts[1]);
      return res;
    }

    for (int j = 2; j <= min(1 + dist, n - 1); j++) {
      root = add(root, nums[j]);
    }

    int minCost = nums[0] + nums[1] + sumSmallest(m);
    for (int i = 2; i <= n - k + 1; i++) {
      root = remove(root, nums[i]);
      if (i + dist < n) {
        root = add(root, nums[i + dist]);
      }
      int currentCost = nums[0] + nums[i] + sumSmallest(m);
      if (currentCost < minCost) minCost = currentCost;
    }
    return minCost;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"math/rand"
)

type TreapNode struct {
	value, size int
	priority    int64
	sum         int64
	left, right *TreapNode
}

func newNode(val int) *TreapNode {
	return &TreapNode{value: val, size: 1, priority: rand.Int63(), sum: int64(val)}
}

func (n *TreapNode) update() {
	n.size = 1
	n.sum = int64(n.value)
	if n.left != nil {
		n.size += n.left.size
		n.sum += n.left.sum
	}
	if n.right != nil {
		n.size += n.right.size
		n.sum += n.right.sum
	}
}

func splitByValue(node *TreapNode, val int) (*TreapNode, *TreapNode) {
	if node == nil {
		return nil, nil
	}
	if node.value <= val {
		l, r := splitByValue(node.right, val)
		node.right = l
		node.update()
		return node, r
	} else {
		l, r := splitByValue(node.left, val)
		node.left = r
		node.update()
		return l, node
	}
}

func splitBySize(node *TreapNode, k int) (*TreapNode, *TreapNode) {
	if node == nil {
		return nil, nil
	}
	leftSize := 0
	if node.left != nil {
		leftSize = node.left.size
	}
	if leftSize >= k {
		l, r := splitBySize(node.left, k)
		node.left = r
		node.update()
		return l, node
	} else {
		l, r := splitBySize(node.right, k-leftSize-1)
		node.right = l
		node.update()
		return node, r
	}
}

func merge(l, r *TreapNode) *TreapNode {
	if l == nil {
		return r
	}
	if r == nil {
		return l
	}
	if l.priority > r.priority {
		l.right = merge(l.right, r)
		l.update()
		return l
	} else {
		r.left = merge(l, r.left)
		r.update()
		return r
	}
}

func minimumCost(nums []int, k int, dist int) int64 {
	n := len(nums)
	m := k - 2
	var root *TreapNode

	add := func(val int) {
		l, r := splitByValue(root, val)
		root = merge(merge(l, newNode(val)), r)
	}
	remove := func(val int) {
		l, r := splitByValue(root, val-1)
		mid, rr := splitByValue(r, val)
		_, rest := splitBySize(mid, 1)
		root = merge(merge(l, rest), rr)
	}
	sumSmallest := func(count int) int64 {
		if count <= 0 {
			return 0
		}
		l, r := splitBySize(root, count)
		res := l.sum
		root = merge(l, r)
		return res
	}

	limit := 1 + dist
	if n-1 < limit {
		limit = n - 1
	}
	for j := 2; j <= limit; j++ {
		add(nums[j])
	}

	minCost := int64(nums[0]) + int64(nums[1]) + sumSmallest(m)
	for i := 2; i <= n-k+1; i++ {
		remove(nums[i])
		if i+dist < n {
			add(nums[i+dist])
		}
		curr := int64(nums[0]) + int64(nums[i]) + sumSmallest(m)
		if curr < minCost {
			minCost = curr
		}
	}
	return minCost
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n \log n) where n is the length of the array. Sorting for coordinate compression takes $O(n \log n)$, and the sliding window iterates through the array once, with each update and query on the Fenwick Tree or Balanced BST taking $O(\log n)$.
- **Space Complexity:** O(n) to store the Fenwick tree or other data structures, the coordinate compression mapping, and the input array.
