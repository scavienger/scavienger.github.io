---
layout: post
title: "Minimum Operations to Sort a Permutation"
date: 2026-10-22 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minOperations(vector<int>& nums) {\n\
        \        int n = nums.size();\n        bool is_inc = true, is_dec = true;\n\
        \        for (int i = 0; i < n; ++i) {\n            if (nums[(i + 1) % n] !=\
        \ (nums[i] + 1) % n) is_inc = false;\n            if (nums[(i + 1) % n] != (nums[i]\
        \ - 1 + n) % n) is_dec = false;\n        }\n\n        if (!is_inc && !is_dec)\
        \ return -1;\n\n        vector<int> dist(2 * n, -1);\n        queue<int> q;\n\
        \        dist[0] = 0;\n        q.push(0);\n\n        while (!q.empty()) {\n\
        \            int u = q.front();\n            q.pop();\n            int t = u\
        \ / n;\n            int k = u % n;\n            int d = dist[u];\n\n       \
        \     // Inverse Rotate Left is Rotate Right\n            int v_rot = t * n\
        \ + (k - 1 + n) % n;\n            if (dist[v_rot] == -1) {\n               \
        \ dist[v_rot] = d + 1;\n                q.push(v_rot);\n            }\n\n  \
        \          // Inverse Reverse is Reverse\n            int v_rev = (1 - t) *\
        \ n + (n - k) % n;\n            if (dist[v_rev] == -1) {\n                dist[v_rev]\
        \ = d + 1;\n                q.push(v_rev);\n            }\n        }\n\n   \
        \     int ans = 2e9;\n        if (is_inc) ans = min(ans, dist[0 * n + nums[0]]);\n\
        \        if (is_dec) ans = min(ans, dist[1 * n + (n - 1 - nums[0] + n) % n]);\n\
        \n        return ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int minOperations(int[]\
        \ nums) {\n        int n = nums.length;\n        boolean isInc = true, isDec\
        \ = true;\n        for (int i = 0; i < n; i++) {\n            if (nums[(i +\
        \ 1) % n] != (nums[i] + 1) % n) isInc = false;\n            if (nums[(i + 1)\
        \ % n] != (nums[i] - 1 + n) % n) isDec = false;\n        }\n\n        if (!isInc\
        \ && !isDec) return -1;\n\n        int[] dist = new int[2 * n];\n        Arrays.fill(dist,\
        \ -1);\n        Deque<Integer> q = new ArrayDeque<>();\n        dist[0] = 0;\n\
        \        q.add(0);\n\n        while (!q.isEmpty()) {\n            int u = q.poll();\n\
        \            int t = u / n;\n            int k = u % n;\n            int d =\
        \ dist[u];\n\n            int vRot = t * n + (k - 1 + n) % n;\n            if\
        \ (dist[vRot] == -1) {\n                dist[vRot] = d + 1;\n              \
        \  q.add(vRot);\n            }\n\n            int vRev = (1 - t) * n + (n -\
        \ k) % n;\n            if (dist[vRev] == -1) {\n                dist[vRev] =\
        \ d + 1;\n                q.add(vRev);\n            }\n        }\n\n       \
        \ int ans = Integer.MAX_VALUE;\n        if (isInc) ans = Math.min(ans, dist[nums[0]]);\n\
        \        if (isDec) ans = Math.min(ans, dist[n + (n - 1 - nums[0] + n) % n]);\n\
        \n        return ans;\n    }\n}"
      python: "import collections\n\nclass Solution(object):\n    def minOperations(self,\
        \ nums):\n        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n\
        \        \"\"\"\n        n = len(nums)\n        is_inc = True\n        is_dec\
        \ = True\n        for i in range(n):\n            if nums[(i + 1) % n] != (nums[i]\
        \ + 1) % n:\n                is_inc = False\n            if nums[(i + 1) % n]\
        \ != (nums[i] - 1 + n) % n:\n                is_dec = False\n\n        if not\
        \ is_inc and not is_dec:\n            return -1\n\n        dist = [-1] * (2\
        \ * n)\n        queue = collections.deque([0])\n        dist[0] = 0\n\n    \
        \    while queue:\n            u = queue.popleft()\n            t, k = divmod(u,\
        \ n)\n            d = dist[u]\n\n            v_rot = t * n + (k - 1 + n) % n\n\
        \            if dist[v_rot] == -1:\n                dist[v_rot] = d + 1\n  \
        \              queue.append(v_rot)\n\n            v_rev = (1 - t) * n + (n -\
        \ k) % n\n            if dist[v_rev] == -1:\n                dist[v_rev] = d\
        \ + 1\n                queue.append(v_rev)\n\n        ans = float('inf')\n \
        \       if is_inc:\n            ans = min(ans, dist[nums[0]])\n        if is_dec:\n\
        \            ans = min(ans, dist[n + (n - 1 - nums[0] + n) % n])\n\n       \
        \ return int(ans)"
      python3: "import collections\n\nclass Solution:\n    def minOperations(self, nums:\
        \ List[int]) -> int:\n        n = len(nums)\n        is_inc = True\n       \
        \ is_dec = True\n        for i in range(n):\n            if nums[(i + 1) % n]\
        \ != (nums[i] + 1) % n:\n                is_inc = False\n            if nums[(i\
        \ + 1) % n] != (nums[i] - 1 + n) % n:\n                is_dec = False\n\n  \
        \      if not is_inc and not is_dec:\n            return -1\n\n        dist\
        \ = [-1] * (2 * n)\n        queue = collections.deque([0])\n        dist[0]\
        \ = 0\n\n        while queue:\n            u = queue.popleft()\n           \
        \ t, k = divmod(u, n)\n            d = dist[u]\n\n            v_rot = t * n\
        \ + (k - 1 + n) % n\n            if dist[v_rot] == -1:\n                dist[v_rot]\
        \ = d + 1\n                queue.append(v_rot)\n\n            v_rev = (1 - t)\
        \ * n + (n - k) % n\n            if dist[v_rev] == -1:\n                dist[v_rev]\
        \ = d + 1\n                queue.append(v_rev)\n\n        ans = float('inf')\n\
        \        if is_inc:\n            ans = min(ans, dist[nums[0]])\n        if is_dec:\n\
        \            ans = min(ans, dist[n + (n - 1 - nums[0] + n) % n])\n\n       \
        \ return int(ans)"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n#include <string.h>\n\nint minOperations(int*\
        \ nums, int numsSize) {\n    int n = numsSize;\n    bool is_inc = true, is_dec\
        \ = true;\n    for (int i = 0; i < n; i++) {\n        if (nums[(i + 1) % n]\
        \ != (nums[i] + 1) % n) is_inc = false;\n        if (nums[(i + 1) % n] != (nums[i]\
        \ - 1 + n) % n) is_dec = false;\n    }\n\n    if (!is_inc && !is_dec) return\
        \ -1;\n\n    int* dist = (int*)malloc(2 * n * sizeof(int));\n    for (int i\
        \ = 0; i < 2 * n; i++) dist[i] = -1;\n\n    int* q = (int*)malloc(2 * n * sizeof(int));\n\
        \    int head = 0, tail = 0;\n\n    dist[0] = 0;\n    q[tail++] = 0;\n\n   \
        \ while (head < tail) {\n        int u = q[head++];\n        int t = u / n;\n\
        \        int k = u % n;\n        int d = dist[u];\n\n        int v_rot = t *\
        \ n + (k - 1 + n) % n;\n        if (dist[v_rot] == -1) {\n            dist[v_rot]\
        \ = d + 1;\n            q[tail++] = v_rot;\n        }\n\n        int v_rev =\
        \ (1 - t) * n + (n - k) % n;\n        if (dist[v_rev] == -1) {\n           \
        \ dist[v_rev] = d + 1;\n            q[tail++] = v_rev;\n        }\n    }\n\n\
        \    int ans = 2000000000;\n    if (is_inc) {\n        int d = dist[nums[0]];\n\
        \        if (d < ans) ans = d;\n    }\n    if (is_dec) {\n        int d = dist[n\
        \ + (n - 1 - nums[0] + n) % n];\n        if (d < ans) ans = d;\n    }\n\n  \
        \  free(dist);\n    free(q);\n    return ans;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int MinOperations(int[]\
        \ nums) {\n        int n = nums.Length;\n        if (n == 0) return 0;\n\n \
        \       bool isType0 = true;\n        for (int i = 0; i < n; i++) {\n      \
        \      if (nums[i] != (nums[0] + i) % n) {\n                isType0 = false;\n\
        \                break;\n            }\n        }\n\n        bool isType1 =\
        \ true;\n        for (int i = 0; i < n; i++) {\n            if (nums[i] != (nums[0]\
        \ - i + n) % n) {\n                isType1 = false;\n                break;\n\
        \            }\n        }\n\n        int res = int.MaxValue;\n\n        if (isType0)\
        \ {\n            int k = nums[0];\n            int cost0 = Math.Min(k, (n -\
        \ k) % n + 2);\n            if (cost0 < res) res = cost0;\n        }\n\n   \
        \     if (isType1) {\n            int k = (n - 1 - nums[0] + n) % n;\n     \
        \       int cost1 = Math.Min(k + 1, (n - k) % n + 1);\n            if (cost1\
        \ < res) res = cost1;\n        }\n\n        return res == int.MaxValue ? -1\
        \ : res;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minOperations\
        \ = function(nums) {\n    const n = nums.length;\n    if (n === 0) return 0;\n\
        \n    let isType0 = true;\n    for (let i = 0; i < n; i++) {\n        if (nums[i]\
        \ !== (nums[0] + i) % n) {\n            isType0 = false;\n            break;\n\
        \        }\n    }\n\n    let isType1 = true;\n    for (let i = 0; i < n; i++)\
        \ {\n        if (nums[i] !== (nums[0] - i + n) % n) {\n            isType1 =\
        \ false;\n            break;\n        }\n    }\n\n    let res = Infinity;\n\n\
        \    if (isType0) {\n        const k = nums[0];\n        const cost0 = Math.min(k,\
        \ (n - k) % n + 2);\n        if (cost0 < res) res = cost0;\n    }\n\n    if\
        \ (isType1) {\n        const k = (n - 1 - nums[0] + n) % n;\n        const cost1\
        \ = Math.min(k + 1, (n - k) % n + 1);\n        if (cost1 < res) res = cost1;\n\
        \    }\n\n    return res === Infinity ? -1 : res;\n};"
      typescript: "function minOperations(nums: number[]): number {\n    const n = nums.length;\n\
        \    if (n === 0) return 0;\n\n    let isType0 = true;\n    for (let i = 0;\
        \ i < n; i++) {\n        if (nums[i] !== (nums[0] + i) % n) {\n            isType0\
        \ = false;\n            break;\n        }\n    }\n\n    let isType1 = true;\n\
        \    for (let i = 0; i < n; i++) {\n        if (nums[i] !== (nums[0] - i + n)\
        \ % n) {\n            isType1 = false;\n            break;\n        }\n    }\n\
        \n    let res = Infinity;\n\n    if (isType0) {\n        const k = nums[0];\n\
        \        const cost0 = Math.min(k, (n - k) % n + 2);\n        if (cost0 < res)\
        \ res = cost0;\n    }\n\n    if (isType1) {\n        const k = (n - 1 - nums[0]\
        \ + n) % n;\n        const cost1 = Math.min(k + 1, (n - k) % n + 1);\n     \
        \   if (cost1 < res) res = cost1;\n    }\n\n    return res === Infinity ? -1\
        \ : res;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minOperations($nums) {\n        $n = count($nums);\n\
        \        if ($n === 0) return 0;\n\n        $isType0 = true;\n        for ($i\
        \ = 0; $i < $n; $i++) {\n            if ($nums[$i] != ($nums[0] + $i) % $n)\
        \ {\n                $isType0 = false;\n                break;\n           \
        \ }\n        }\n\n        $isType1 = true;\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            if ($nums[$i] != ($nums[0] - $i + $n) % $n) {\n           \
        \     $isType1 = false;\n                break;\n            }\n        }\n\n\
        \        $res = PHP_INT_MAX;\n\n        if ($isType0) {\n            $k = $nums[0];\n\
        \            $cost0 = min($k, ($n - $k) % $n + 2);\n            if ($cost0 <\
        \ $res) $res = $cost0;\n        }\n\n        if ($isType1) {\n            $k\
        \ = ($n - 1 - $nums[0] + $n) % $n;\n            $cost1 = min($k + 1, ($n - $k)\
        \ % $n + 1);\n            if ($cost1 < $res) $res = $cost1;\n        }\n\n \
        \       return $res === PHP_INT_MAX ? -1 : $res;\n    }\n}"
      swift: "class Solution {\n    func minOperations(_ nums: [Int]) -> Int {\n   \
        \     let n = nums.count\n        if n == 0 { return 0 }\n\n        var isType0\
        \ = true\n        for i in 0..<n {\n            if nums[i] != (nums[0] + i)\
        \ % n {\n                isType0 = false\n                break\n          \
        \  }\n        }\n\n        var isType1 = true\n        for i in 0..<n {\n  \
        \          if nums[i] != (nums[0] - i + n) % n {\n                isType1 =\
        \ false\n                break\n            }\n        }\n\n        var res\
        \ = Int.max\n\n        if isType0 {\n            let k = nums[0]\n         \
        \   let cost0 = min(k, (n - k) % n + 2)\n            if cost0 < res { res =\
        \ cost0 }\n        }\n\n        if isType1 {\n            let k = (n - 1 - nums[0]\
        \ + n) % n\n            let cost1 = min(k + 1, (n - k) % n + 1)\n          \
        \  if cost1 < res { res = cost1 }\n        }\n\n        return res == Int.max\
        \ ? -1 : res\n    }\n}"
      kotlin: "import java.util.ArrayDeque\n\nclass Solution {\n    fun minOperations(nums:\
        \ IntArray): Int {\n        val n = nums.size\n        var idx0 = -1\n     \
        \   for (i in 0 until n) {\n            if (nums[i] == 0) {\n              \
        \  idx0 = i\n                break\n            }\n        }\n\n        val\
        \ isTarget = Array(2) { BooleanArray(n) }\n\n        var isType0 = true\n  \
        \      for (j in 0 until n) {\n            if (nums[(idx0 + j) % n] != j) {\n\
        \                isType0 = false\n                break\n            }\n   \
        \     }\n        if (isType0) isTarget[0][idx0] = true\n\n        val idx0Rev\
        \ = n - 1 - idx0\n        var isType1 = true\n        for (j in 0 until n) {\n\
        \            if (nums[n - 1 - (idx0Rev + j) % n] != j) {\n                isType1\
        \ = false\n                break\n            }\n        }\n        if (isType1)\
        \ isTarget[1][idx0Rev] = true\n\n        val dist = IntArray(2 * n) { -1 }\n\
        \        val queue = ArrayDeque<Int>()\n\n        dist[0] = 0\n        queue.add(0)\n\
        \n        while (queue.isNotEmpty()) {\n            val curr = queue.removeFirst()\n\
        \            val t = curr / n\n            val s = curr % n\n\n            if\
        \ (isTarget[t][s]) return dist[curr]\n\n            val ns = (s + 1) % n\n \
        \           val nextL = t * n + ns\n            if (dist[nextL] == -1) {\n \
        \               dist[nextL] = dist[curr] + 1\n                queue.add(nextL)\n\
        \            }\n\n            val nt = 1 - t\n            val nrs = (n - s)\
        \ % n\n            val nextR = nt * n + nrs\n            if (dist[nextR] ==\
        \ -1) {\n                dist[nextR] = dist[curr] + 1\n                queue.add(nextR)\n\
        \            }\n        }\n\n        return -1\n    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  int minOperations(List<int>\
        \ nums) {\n    int n = nums.length;\n    int idx0 = -1;\n    for (int i = 0;\
        \ i < n; i++) {\n      if (nums[i] == 0) {\n        idx0 = i;\n        break;\n\
        \      }\n    }\n\n    List<List<bool>> isTarget = [\n      List.filled(n, false),\n\
        \      List.filled(n, false)\n    ];\n\n    bool isType0 = true;\n    for (int\
        \ j = 0; j < n; j++) {\n      if (nums[(idx0 + j) % n] != j) {\n        isType0\
        \ = false;\n        break;\n      }\n    }\n    if (isType0) isTarget[0][idx0]\
        \ = true;\n\n    int idx0Rev = n - 1 - idx0;\n    bool isType1 = true;\n   \
        \ for (int j = 0; j < n; j++) {\n      if (nums[n - 1 - (idx0Rev + j) % n] !=\
        \ j) {\n        isType1 = false;\n        break;\n      }\n    }\n    if (isType1)\
        \ isTarget[1][idx0Rev] = true;\n\n    List<int> dist = List.filled(2 * n, -1);\n\
        \    Queue<int> queue = Queue<int>();\n\n    dist[0] = 0;\n    queue.add(0);\n\
        \n    while (queue.isNotEmpty) {\n      int curr = queue.removeFirst();\n  \
        \    int t = curr ~/ n;\n      int s = curr % n;\n\n      if (isTarget[t][s])\
        \ return dist[curr];\n\n      int ns = (s + 1) % n;\n      int nextL = t * n\
        \ + ns;\n      if (dist[nextL] == -1) {\n        dist[nextL] = dist[curr] +\
        \ 1;\n        queue.add(nextL);\n      }\n\n      int nt = 1 - t;\n      int\
        \ nrs = (n - s) % n;\n      int nextR = nt * n + nrs;\n      if (dist[nextR]\
        \ == -1) {\n        dist[nextR] = dist[curr] + 1;\n        queue.add(nextR);\n\
        \      }\n    }\n\n    return -1;\n  }\n}"
      go: "func minOperations(nums []int) int {\n\tn := len(nums)\n\tidx0 := -1\n\t\
        for i, v := range nums {\n\t\tif v == 0 {\n\t\t\tidx0 = i\n\t\t\tbreak\n\t\t\
        }\n\t}\n\n\tisTarget := [2][]bool{make([]bool, n), make([]bool, n)}\n\n\tisType0\
        \ := true\n\tfor j := 0; j < n; j++ {\n\t\tif nums[(idx0+j)%n] != j {\n\t\t\t\
        isType0 = false\n\t\t\tbreak\n\t\t}\n\t}\n\tif isType0 {\n\t\tisTarget[0][idx0]\
        \ = true\n\t}\n\n\tidx0Rev := n - 1 - idx0\n\tisType1 := true\n\tfor j := 0;\
        \ j < n; j++ {\n\t\tif nums[n-1-(idx0Rev+j)%n] != j {\n\t\t\tisType1 = false\n\
        \t\t\tbreak\n\t\t}\n\t}\n\tif isType1 {\n\t\tisTarget[1][idx0Rev] = true\n\t\
        }\n\n\tdist := make([]int, 2*n)\n\tfor i := range dist {\n\t\tdist[i] = -1\n\
        \t}\n\tqueue := make([]int, 0, 2*n)\n\n\tdist[0] = 0\n\tqueue = append(queue,\
        \ 0)\n\n\thead := 0\n\tfor head < len(queue) {\n\t\tcurr := queue[head]\n\t\t\
        head++\n\n\t\tt := curr / n\n\t\ts := curr % n\n\n\t\tif isTarget[t][s] {\n\t\
        \t\treturn dist[curr]\n\t\t}\n\n\t\tns := (s + 1) % n\n\t\tnextL := t*n + ns\n\
        \t\tif dist[nextL] == -1 {\n\t\t\tdist[nextL] = dist[curr] + 1\n\t\t\tqueue\
        \ = append(queue, nextL)\n\t\t}\n\n\t\tnt := 1 - t\n\t\tnrs := (n - s) % n\n\
        \t\tnextR := nt*n + nrs\n\t\tif dist[nextR] == -1 {\n\t\t\tdist[nextR] = dist[curr]\
        \ + 1\n\t\t\tqueue = append(queue, nextR)\n\t\t}\n\t}\n\n\treturn -1\n}"
      ruby: "def min_operations(nums)\n  n = nums.length\n  idx0 = nums.index(0)\n\n\
        \  is_target = Array.new(2) { Array.new(n, false) }\n\n  is_type0 = true\n \
        \ n.times do |j|\n    if nums[(idx0 + j) % n] != j\n      is_type0 = false\n\
        \      break\n    end\n  end\n  is_target[0][idx0] = true if is_type0\n\n  idx0_rev\
        \ = n - 1 - idx0\n  is_type1 = true\n  n.times do |j|\n    if nums[n - 1 - (idx0_rev\
        \ + j) % n] != j\n      is_type1 = false\n      break\n    end\n  end\n  is_target[1][idx0_rev]\
        \ = true if is_type1\n\n  dist = Array.new(2 * n, -1)\n  queue = [0]\n  dist[0]\
        \ = 0\n  head = 0\n\n  while head < queue.length\n    curr = queue[head]\n \
        \   head += 1\n\n    t = curr / n\n    s = curr % n\n\n    return dist[curr]\
        \ if is_target[t][s]\n\n    ns = (s + 1) % n\n    next_l = t * n + ns\n    if\
        \ dist[next_l] == -1\n      dist[next_l] = dist[curr] + 1\n      queue.push(next_l)\n\
        \    end\n\n    nt = 1 - t\n    nrs = (n - s) % n\n    next_r = nt * n + nrs\n\
        \    if dist[next_r] == -1\n      dist[next_r] = dist[curr] + 1\n      queue.push(next_r)\n\
        \    end\n  end\n\n  -1\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def minOperations(nums:\
        \ Array[Int]): Int = {\n        val n = nums.length\n        val idx0 = nums.indexOf(0)\n\
        \n        val isTarget = Array.fill(2, n)(false)\n\n        var isType0 = true\n\
        \        var j0 = 0\n        while (j0 < n) {\n            if (nums((idx0 +\
        \ j0) % n) != j0) {\n                isType0 = false\n                j0 = n\n\
        \            } else {\n                j0 += 1\n            }\n        }\n \
        \       if (isType0) isTarget(0)(idx0) = true\n\n        val idx0Rev = n - 1\
        \ - idx0\n        var isType1 = true\n        var j1 = 0\n        while (j1\
        \ < n) {\n            if (nums(n - 1 - (idx0Rev + j1) % n) != j1) {\n      \
        \          isType1 = false\n                j1 = n\n            } else {\n \
        \               j1 += 1\n            }\n        }\n        if (isType1) isTarget(1)(idx0Rev)\
        \ = true\n\n        val dist = Array.fill(2 * n)(-1)\n        val queue = mutable.Queue[Int]()\n\
        \n        dist(0) = 0\n        queue.enqueue(0)\n\n        while (queue.nonEmpty)\
        \ {\n            val curr = queue.dequeue()\n            val t = curr / n\n\
        \            val s = curr % n\n\n            if (isTarget(t)(s)) return dist(curr)\n\
        \n            val ns = (s + 1) % n\n            val nextL = t * n + ns\n   \
        \         if (dist(nextL) == -1) {\n                dist(nextL) = dist(curr)\
        \ + 1\n                queue.enqueue(nextL)\n            }\n\n            val\
        \ nt = 1 - t\n            val nrs = (n - s) % n\n            val nextR = nt\
        \ * n + nrs\n            if (dist(nextR) == -1) {\n                dist(nextR)\
        \ = dist(curr) + 1\n                queue.enqueue(nextR)\n            }\n  \
        \      }\n\n        -1\n    }\n}"
      rust: "impl Solution {\n    pub fn min_operations(nums: Vec<i32>) -> i32 {\n \
        \       let n = nums.len();\n        let mut idx0 = 0;\n        for (i, &val)\
        \ in nums.iter().enumerate() {\n            if val == 0 {\n                idx0\
        \ = i;\n                break;\n            }\n        }\n\n        let mut\
        \ t1: i32 = -1;\n        let mut ok1 = true;\n        for i in 0..n {\n    \
        \        if nums[(idx0 + i) % n] != i as i32 {\n                ok1 = false;\n\
        \                break;\n            }\n        }\n        if ok1 {\n      \
        \      t1 = idx0 as i32;\n        }\n\n        let mut t2: i32 = -1;\n     \
        \   let mut ok2 = true;\n        for i in 0..n {\n            if nums[(idx0\
        \ + n - i) % n] != i as i32 {\n                ok2 = false;\n              \
        \  break;\n            }\n        }\n        if ok2 {\n            t2 = (n -\
        \ 1 - idx0) as i32;\n        }\n\n        let mut ans = i32::MAX;\n        if\
        \ t1 != -1 {\n            ans = ans.min(t1);\n            ans = ans.min(n as\
        \ i32 - t1 + 2);\n        }\n        if t2 != -1 {\n            ans = ans.min(t2\
        \ + 1);\n            ans = ans.min(n as i32 - t2 + 1);\n        }\n\n      \
        \  if ans == i32::MAX {\n            -1\n        } else {\n            ans\n\
        \        }\n    }\n}"
      racket: "(define/contract (min-operations nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([n (length nums)]\n         [v (list->vector nums)]\n\
        \         [idx0 (for/first ([i (in-range n)] #:when (= (vector-ref v i) 0))\
        \ i)])\n    (let ([t1 (if (for/and ([i (in-range n)])\n                    (=\
        \ (vector-ref v (modulo (+ idx0 i) n)) i))\n                  idx0\n       \
        \           -1)]\n          [t2 (if (for/and ([i (in-range n)])\n          \
        \          (= (vector-ref v (modulo (- idx0 i) n)) i))\n                  (-\
        \ n 1 idx0)\n                  -1)])\n      (let ([ans1 (if (= t1 -1) 1000000000\
        \ (min t1 (+ (- n t1) 2)))]\n            [ans2 (if (= t2 -1) 1000000000 (min\
        \ (+ t2 1) (+ (- n t2) 1)))])\n        (let ([final-ans (min ans1 ans2)])\n\
        \          (if (= final-ans 1000000000)\n              -1\n              final-ans))))))"
      erlang: "-spec min_operations(Nums :: [integer()]) -> integer().\nmin_operations(Nums)\
        \ ->\n    N = length(Nums),\n    Tuple = list_to_tuple(Nums),\n    Idx0 = find_idx0(0,\
        \ Tuple),\n    T1 = case check_t1(0, Idx0, N, Tuple) of\n        true -> Idx0;\n\
        \        false -> -1\n    end,\n    T2 = case check_t2(0, Idx0, N, Tuple) of\n\
        \        true -> (N - 1 - Idx0);\n        false -> -1\n    end,\n    Ans1 =\
        \ if T1 =:= -1 -> 1000000000;\n              true -> min(T1, N - T1 + 2)\n \
        \          end,\n    Ans2 = if T2 =:= -1 -> 1000000000;\n              true\
        \ -> min(T2 + 1, N - T2 + 1)\n           end,\n    FinalAns = min(Ans1, Ans2),\n\
        \    if FinalAns =:= 1000000000 -> -1;\n       true -> FinalAns\n    end.\n\n\
        find_idx0(I, Tuple) ->\n    case element(I + 1, Tuple) of\n        0 -> I;\n\
        \        _ -> find_idx0(I + 1, Tuple)\n    end.\n\ncheck_t1(I, Idx0, N, Tuple)\
        \ when I < N ->\n    Val = element(((Idx0 + I) rem N) + 1, Tuple),\n    if Val\
        \ =:= I -> check_t1(I + 1, Idx0, N, Tuple);\n       true -> false\n    end;\n\
        check_t1(_I, _Idx0, _N, _Tuple) -> true.\n\ncheck_t2(I, Idx0, N, Tuple) when\
        \ I < N ->\n    Val = element(((Idx0 - I + N) rem N) + 1, Tuple),\n    if Val\
        \ =:= I -> check_t2(I + 1, Idx0, N, Tuple);\n       true -> false\n    end;\n\
        check_t2(_I, _Idx0, _N, _Tuple) -> true."
      elixir: "defmodule Solution do\n  @spec min_operations(nums :: [integer]) :: integer\n\
        \  def min_operations(nums) do\n    n = length(nums)\n    tuple = List.to_tuple(nums)\n\
        \    idx0 = Enum.find_index(nums, fn x -> x == 0 end)\n\n    t1 = if check_t1(0,\
        \ idx0, n, tuple), do: idx0, else: -1\n    t2 = if check_t2(0, idx0, n, tuple),\
        \ do: (n - 1 - idx0), else: -1\n\n    ans = 1_000_000_000\n    ans = if t1 !=\
        \ -1 do\n      d1 = t1\n      d2 = n - t1 + 2\n      min(ans, min(d1, d2))\n\
        \    else\n      ans\n    end\n    ans = if t2 != -1 do\n      d1 = t2 + 1\n\
        \      d2 = n - t2 + 1\n      min(ans, min(d1, d2))\n    else\n      ans\n \
        \   end\n\n    if ans == 1_000_000_000, do: -1, else: ans\n  end\n\n  defp check_t1(i,\
        \ idx0, n, tuple) do\n    if i == n do\n      true\n    else\n      if elem(tuple,\
        \ rem(idx0 + i, n)) == i do\n        check_t1(i + 1, idx0, n, tuple)\n     \
        \ else\n        false\n      end\n    end\n  end\n\n  defp check_t2(i, idx0,\
        \ n, tuple) do\n    if i == n do\n      true\n    else\n      if elem(tuple,\
        \ rem(idx0 - i + n, n)) == i do\n        check_t2(i + 1, idx0, n, tuple)\n \
        \     else\n        false\n      end\n    end\n  end\nend"
    approach: 'The problem can be solved by recognizing that the allowed operations
      (Reverse and Rotate Left) generate the Dihedral group $D_n$. Any array reachable
      from the sorted permutation $[0, 1, \dots, n-1]$ must be either a cyclic rotation
      of the sorted array or a cyclic rotation of the reversed sorted array. This results
      in $2n$ possible reachable states: $n$ rotations of the forward sorted array (Type
      0) and $n$ rotations of the backward sorted array (Type 1). A permutation is reachable
      if and only if it is cyclically increasing (Type 0) or cyclically decreasing (Type
      1).


      To find the minimum operations, we model the problem as a shortest-path search
      on a graph with $2n$ states. Each state is $(type, shift)$, where $shift$ is the
      number of left rotations applied to the base sequence. We perform a Breadth-First
      Search (BFS) starting from the sorted state $(0, 0)$. To find the distance to
      the input array, we use the inverse of the allowed operations: Reverse (self-inverse)
      and Rotate Right (inverse of Rotate Left). After computing the shortest distances
      to all $2n$ states, we identify which states the input array represents and return
      the minimum distance. If the input array is neither cyclically increasing nor
      cyclically decreasing, it is unreachable, and we return -1.'
    time_complexity: O(n) with one-paragraph explanation. Identifying whether the array
      is cyclically increasing or decreasing takes $O(n)$ time by iterating through
      the array once. The BFS visits at most $2n$ states and $4n$ edges, leading to
      a total time complexity of $O(n)$.
    space_complexity: O(n) with one-paragraph explanation. We store the distance for
      $2n$ states and a BFS queue which can contain up to $2n$ elements. This results
      in $O(n)$ space complexity.
    elapsed_time: 335.08382534980774
    model: gemini-3-flash-preview
    generated_at: '2026-10-22 02:48:47 '
---

## Problem #3942: Minimum Operations to Sort a Permutation

**Difficulty:** Medium

**Topics:** Array

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code>, where <code>nums</code> is a <span data-keyword="permutation-array">permutation</span> of the integers from 0 to <code>n - 1</code>.</p>

<p>You may perform <strong>only</strong> the following operations:</p>

<ul>
	<li><strong>Reverse</strong> the entire array.</li>
	<li><strong>Rotate Left by One</strong>: Move the first element to the end of the array, and rest elements to left by one position.</li>
</ul>

<p>Return an integer denoting the <strong>minimum</strong> number of operations required to sort the array in <strong>increasing</strong> order. If it is <strong>not possible</strong> to sort the array using only the given operations, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Rotate Left by one: <code>[2, 1, 0]</code></li>
	<li>Reverse the array: <code>[0, 1, 2]</code></li>
</ul>

<p>The array becomes sorted in 2 operations, which is minimal</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Reverse the array: <code>[2, 0, 1]</code></li>
	<li>Rotate Left by one: <code>[0, 1, 2]</code></li>
</ul>

<p>The array becomes sorted in 2 operations, which is minimal.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,0,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>It is impossible to reach <code>[2, 0, 1, 3]</code>. Thus, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n - 1</code></li>
	<li><code>nums</code> is a permutation of integers from 0 to <code>n - 1</code>.</li>
</ul>


## Hints

1. **1a. (Case Analysis)**

The operations generate only rotations of `nums` and rotations of `reverse(nums)`.

2. **1b. (Case Analysis)**

So sorting is possible if and only if `nums` is a rotation of increasing order, or a rotation of decreasing order.

3. **1c. (Case Analysis)**

If `nums` is increasing cyclically and `nums[i] = 0`, then rotating left `i` times sorts the array, or we may reverse, rotate, then reverse again.

Take the minimum between these possibilities.

4. **1d. (Case Analysis)**

If `nums` is decreasing cyclically, try both possibilities: reverse first, or rotate first and then reverse. Take the minimum valid cost.

5. **2a. (Breadth-First Search)**

As follows from Hint 1a and 1b, each reachable array can be represented as a state. Since all reachable arrays belong to one of two families, we can compress a state into `(type, shift)`.

`type = 0`: a rotation of the original array.
`type = 1`: a rotation of the reversed array.

`shift` denotes the number of left rotations applied within that family.

6. **2b. (Breadth-First Search)**

A left rotation changes `shift` to `(shift + 1) % n`.

A reverse toggles `type`, while also changing the corresponding `shift` to `(n - shift) % n`.

7. **2c. (Breadth-First Search)**

Build a graph on these `2n` states using the two allowed operations, then run BFS from `(0, 0)` to the state representing the input array.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved by recognizing that the allowed operations (Reverse and Rotate Left) generate the Dihedral group $D_n$. Any array reachable from the sorted permutation $[0, 1, \dots, n-1]$ must be either a cyclic rotation of the sorted array or a cyclic rotation of the reversed sorted array. This results in $2n$ possible reachable states: $n$ rotations of the forward sorted array (Type 0) and $n$ rotations of the backward sorted array (Type 1). A permutation is reachable if and only if it is cyclically increasing (Type 0) or cyclically decreasing (Type 1).

To find the minimum operations, we model the problem as a shortest-path search on a graph with $2n$ states. Each state is $(type, shift)$, where $shift$ is the number of left rotations applied to the base sequence. We perform a Breadth-First Search (BFS) starting from the sorted state $(0, 0)$. To find the distance to the input array, we use the inverse of the allowed operations: Reverse (self-inverse) and Rotate Right (inverse of Rotate Left). After computing the shortest distances to all $2n$ states, we identify which states the input array represents and return the minimum distance. If the input array is neither cyclically increasing nor cyclically decreasing, it is unreachable, and we return -1.

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
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        bool is_inc = true, is_dec = true;
        for (int i = 0; i < n; ++i) {
            if (nums[(i + 1) % n] != (nums[i] + 1) % n) is_inc = false;
            if (nums[(i + 1) % n] != (nums[i] - 1 + n) % n) is_dec = false;
        }

        if (!is_inc && !is_dec) return -1;

        vector<int> dist(2 * n, -1);
        queue<int> q;
        dist[0] = 0;
        q.push(0);

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            int t = u / n;
            int k = u % n;
            int d = dist[u];

            // Inverse Rotate Left is Rotate Right
            int v_rot = t * n + (k - 1 + n) % n;
            if (dist[v_rot] == -1) {
                dist[v_rot] = d + 1;
                q.push(v_rot);
            }

            // Inverse Reverse is Reverse
            int v_rev = (1 - t) * n + (n - k) % n;
            if (dist[v_rev] == -1) {
                dist[v_rev] = d + 1;
                q.push(v_rev);
            }
        }

        int ans = 2e9;
        if (is_inc) ans = min(ans, dist[0 * n + nums[0]]);
        if (is_dec) ans = min(ans, dist[1 * n + (n - 1 - nums[0] + n) % n]);

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
    public int minOperations(int[] nums) {
        int n = nums.length;
        boolean isInc = true, isDec = true;
        for (int i = 0; i < n; i++) {
            if (nums[(i + 1) % n] != (nums[i] + 1) % n) isInc = false;
            if (nums[(i + 1) % n] != (nums[i] - 1 + n) % n) isDec = false;
        }

        if (!isInc && !isDec) return -1;

        int[] dist = new int[2 * n];
        Arrays.fill(dist, -1);
        Deque<Integer> q = new ArrayDeque<>();
        dist[0] = 0;
        q.add(0);

        while (!q.isEmpty()) {
            int u = q.poll();
            int t = u / n;
            int k = u % n;
            int d = dist[u];

            int vRot = t * n + (k - 1 + n) % n;
            if (dist[vRot] == -1) {
                dist[vRot] = d + 1;
                q.add(vRot);
            }

            int vRev = (1 - t) * n + (n - k) % n;
            if (dist[vRev] == -1) {
                dist[vRev] = d + 1;
                q.add(vRev);
            }
        }

        int ans = Integer.MAX_VALUE;
        if (isInc) ans = Math.min(ans, dist[nums[0]]);
        if (isDec) ans = Math.min(ans, dist[n + (n - 1 - nums[0] + n) % n]);

        return ans;
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
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        is_inc = True
        is_dec = True
        for i in range(n):
            if nums[(i + 1) % n] != (nums[i] + 1) % n:
                is_inc = False
            if nums[(i + 1) % n] != (nums[i] - 1 + n) % n:
                is_dec = False

        if not is_inc and not is_dec:
            return -1

        dist = [-1] * (2 * n)
        queue = collections.deque([0])
        dist[0] = 0

        while queue:
            u = queue.popleft()
            t, k = divmod(u, n)
            d = dist[u]

            v_rot = t * n + (k - 1 + n) % n
            if dist[v_rot] == -1:
                dist[v_rot] = d + 1
                queue.append(v_rot)

            v_rev = (1 - t) * n + (n - k) % n
            if dist[v_rev] == -1:
                dist[v_rev] = d + 1
                queue.append(v_rev)

        ans = float('inf')
        if is_inc:
            ans = min(ans, dist[nums[0]])
        if is_dec:
            ans = min(ans, dist[n + (n - 1 - nums[0] + n) % n])

        return int(ans)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        is_inc = True
        is_dec = True
        for i in range(n):
            if nums[(i + 1) % n] != (nums[i] + 1) % n:
                is_inc = False
            if nums[(i + 1) % n] != (nums[i] - 1 + n) % n:
                is_dec = False

        if not is_inc and not is_dec:
            return -1

        dist = [-1] * (2 * n)
        queue = collections.deque([0])
        dist[0] = 0

        while queue:
            u = queue.popleft()
            t, k = divmod(u, n)
            d = dist[u]

            v_rot = t * n + (k - 1 + n) % n
            if dist[v_rot] == -1:
                dist[v_rot] = d + 1
                queue.append(v_rot)

            v_rev = (1 - t) * n + (n - k) % n
            if dist[v_rev] == -1:
                dist[v_rev] = d + 1
                queue.append(v_rev)

        ans = float('inf')
        if is_inc:
            ans = min(ans, dist[nums[0]])
        if is_dec:
            ans = min(ans, dist[n + (n - 1 - nums[0] + n) % n])

        return int(ans)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int minOperations(int* nums, int numsSize) {
    int n = numsSize;
    bool is_inc = true, is_dec = true;
    for (int i = 0; i < n; i++) {
        if (nums[(i + 1) % n] != (nums[i] + 1) % n) is_inc = false;
        if (nums[(i + 1) % n] != (nums[i] - 1 + n) % n) is_dec = false;
    }

    if (!is_inc && !is_dec) return -1;

    int* dist = (int*)malloc(2 * n * sizeof(int));
    for (int i = 0; i < 2 * n; i++) dist[i] = -1;

    int* q = (int*)malloc(2 * n * sizeof(int));
    int head = 0, tail = 0;

    dist[0] = 0;
    q[tail++] = 0;

    while (head < tail) {
        int u = q[head++];
        int t = u / n;
        int k = u % n;
        int d = dist[u];

        int v_rot = t * n + (k - 1 + n) % n;
        if (dist[v_rot] == -1) {
            dist[v_rot] = d + 1;
            q[tail++] = v_rot;
        }

        int v_rev = (1 - t) * n + (n - k) % n;
        if (dist[v_rev] == -1) {
            dist[v_rev] = d + 1;
            q[tail++] = v_rev;
        }
    }

    int ans = 2000000000;
    if (is_inc) {
        int d = dist[nums[0]];
        if (d < ans) ans = d;
    }
    if (is_dec) {
        int d = dist[n + (n - 1 - nums[0] + n) % n];
        if (d < ans) ans = d;
    }

    free(dist);
    free(q);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MinOperations(int[] nums) {
        int n = nums.Length;
        if (n == 0) return 0;

        bool isType0 = true;
        for (int i = 0; i < n; i++) {
            if (nums[i] != (nums[0] + i) % n) {
                isType0 = false;
                break;
            }
        }

        bool isType1 = true;
        for (int i = 0; i < n; i++) {
            if (nums[i] != (nums[0] - i + n) % n) {
                isType1 = false;
                break;
            }
        }

        int res = int.MaxValue;

        if (isType0) {
            int k = nums[0];
            int cost0 = Math.Min(k, (n - k) % n + 2);
            if (cost0 < res) res = cost0;
        }

        if (isType1) {
            int k = (n - 1 - nums[0] + n) % n;
            int cost1 = Math.Min(k + 1, (n - k) % n + 1);
            if (cost1 < res) res = cost1;
        }

        return res == int.MaxValue ? -1 : res;
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
var minOperations = function(nums) {
    const n = nums.length;
    if (n === 0) return 0;

    let isType0 = true;
    for (let i = 0; i < n; i++) {
        if (nums[i] !== (nums[0] + i) % n) {
            isType0 = false;
            break;
        }
    }

    let isType1 = true;
    for (let i = 0; i < n; i++) {
        if (nums[i] !== (nums[0] - i + n) % n) {
            isType1 = false;
            break;
        }
    }

    let res = Infinity;

    if (isType0) {
        const k = nums[0];
        const cost0 = Math.min(k, (n - k) % n + 2);
        if (cost0 < res) res = cost0;
    }

    if (isType1) {
        const k = (n - 1 - nums[0] + n) % n;
        const cost1 = Math.min(k + 1, (n - k) % n + 1);
        if (cost1 < res) res = cost1;
    }

    return res === Infinity ? -1 : res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;

    let isType0 = true;
    for (let i = 0; i < n; i++) {
        if (nums[i] !== (nums[0] + i) % n) {
            isType0 = false;
            break;
        }
    }

    let isType1 = true;
    for (let i = 0; i < n; i++) {
        if (nums[i] !== (nums[0] - i + n) % n) {
            isType1 = false;
            break;
        }
    }

    let res = Infinity;

    if (isType0) {
        const k = nums[0];
        const cost0 = Math.min(k, (n - k) % n + 2);
        if (cost0 < res) res = cost0;
    }

    if (isType1) {
        const k = (n - 1 - nums[0] + n) % n;
        const cost1 = Math.min(k + 1, (n - k) % n + 1);
        if (cost1 < res) res = cost1;
    }

    return res === Infinity ? -1 : res;
};
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
    function minOperations($nums) {
        $n = count($nums);
        if ($n === 0) return 0;

        $isType0 = true;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] != ($nums[0] + $i) % $n) {
                $isType0 = false;
                break;
            }
        }

        $isType1 = true;
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] != ($nums[0] - $i + $n) % $n) {
                $isType1 = false;
                break;
            }
        }

        $res = PHP_INT_MAX;

        if ($isType0) {
            $k = $nums[0];
            $cost0 = min($k, ($n - $k) % $n + 2);
            if ($cost0 < $res) $res = $cost0;
        }

        if ($isType1) {
            $k = ($n - 1 - $nums[0] + $n) % $n;
            $cost1 = min($k + 1, ($n - $k) % $n + 1);
            if ($cost1 < $res) $res = $cost1;
        }

        return $res === PHP_INT_MAX ? -1 : $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 0 { return 0 }

        var isType0 = true
        for i in 0..<n {
            if nums[i] != (nums[0] + i) % n {
                isType0 = false
                break
            }
        }

        var isType1 = true
        for i in 0..<n {
            if nums[i] != (nums[0] - i + n) % n {
                isType1 = false
                break
            }
        }

        var res = Int.max

        if isType0 {
            let k = nums[0]
            let cost0 = min(k, (n - k) % n + 2)
            if cost0 < res { res = cost0 }
        }

        if isType1 {
            let k = (n - 1 - nums[0] + n) % n
            let cost1 = min(k + 1, (n - k) % n + 1)
            if cost1 < res { res = cost1 }
        }

        return res == Int.max ? -1 : res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.ArrayDeque

class Solution {
    fun minOperations(nums: IntArray): Int {
        val n = nums.size
        var idx0 = -1
        for (i in 0 until n) {
            if (nums[i] == 0) {
                idx0 = i
                break
            }
        }

        val isTarget = Array(2) { BooleanArray(n) }

        var isType0 = true
        for (j in 0 until n) {
            if (nums[(idx0 + j) % n] != j) {
                isType0 = false
                break
            }
        }
        if (isType0) isTarget[0][idx0] = true

        val idx0Rev = n - 1 - idx0
        var isType1 = true
        for (j in 0 until n) {
            if (nums[n - 1 - (idx0Rev + j) % n] != j) {
                isType1 = false
                break
            }
        }
        if (isType1) isTarget[1][idx0Rev] = true

        val dist = IntArray(2 * n) { -1 }
        val queue = ArrayDeque<Int>()

        dist[0] = 0
        queue.add(0)

        while (queue.isNotEmpty()) {
            val curr = queue.removeFirst()
            val t = curr / n
            val s = curr % n

            if (isTarget[t][s]) return dist[curr]

            val ns = (s + 1) % n
            val nextL = t * n + ns
            if (dist[nextL] == -1) {
                dist[nextL] = dist[curr] + 1
                queue.add(nextL)
            }

            val nt = 1 - t
            val nrs = (n - s) % n
            val nextR = nt * n + nrs
            if (dist[nextR] == -1) {
                dist[nextR] = dist[curr] + 1
                queue.add(nextR)
            }
        }

        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class Solution {
  int minOperations(List<int> nums) {
    int n = nums.length;
    int idx0 = -1;
    for (int i = 0; i < n; i++) {
      if (nums[i] == 0) {
        idx0 = i;
        break;
      }
    }

    List<List<bool>> isTarget = [
      List.filled(n, false),
      List.filled(n, false)
    ];

    bool isType0 = true;
    for (int j = 0; j < n; j++) {
      if (nums[(idx0 + j) % n] != j) {
        isType0 = false;
        break;
      }
    }
    if (isType0) isTarget[0][idx0] = true;

    int idx0Rev = n - 1 - idx0;
    bool isType1 = true;
    for (int j = 0; j < n; j++) {
      if (nums[n - 1 - (idx0Rev + j) % n] != j) {
        isType1 = false;
        break;
      }
    }
    if (isType1) isTarget[1][idx0Rev] = true;

    List<int> dist = List.filled(2 * n, -1);
    Queue<int> queue = Queue<int>();

    dist[0] = 0;
    queue.add(0);

    while (queue.isNotEmpty) {
      int curr = queue.removeFirst();
      int t = curr ~/ n;
      int s = curr % n;

      if (isTarget[t][s]) return dist[curr];

      int ns = (s + 1) % n;
      int nextL = t * n + ns;
      if (dist[nextL] == -1) {
        dist[nextL] = dist[curr] + 1;
        queue.add(nextL);
      }

      int nt = 1 - t;
      int nrs = (n - s) % n;
      int nextR = nt * n + nrs;
      if (dist[nextR] == -1) {
        dist[nextR] = dist[curr] + 1;
        queue.add(nextR);
      }
    }

    return -1;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minOperations(nums []int) int {
	n := len(nums)
	idx0 := -1
	for i, v := range nums {
		if v == 0 {
			idx0 = i
			break
		}
	}

	isTarget := [2][]bool{make([]bool, n), make([]bool, n)}

	isType0 := true
	for j := 0; j < n; j++ {
		if nums[(idx0+j)%n] != j {
			isType0 = false
			break
		}
	}
	if isType0 {
		isTarget[0][idx0] = true
	}

	idx0Rev := n - 1 - idx0
	isType1 := true
	for j := 0; j < n; j++ {
		if nums[n-1-(idx0Rev+j)%n] != j {
			isType1 = false
			break
		}
	}
	if isType1 {
		isTarget[1][idx0Rev] = true
	}

	dist := make([]int, 2*n)
	for i := range dist {
		dist[i] = -1
	}
	queue := make([]int, 0, 2*n)

	dist[0] = 0
	queue = append(queue, 0)

	head := 0
	for head < len(queue) {
		curr := queue[head]
		head++

		t := curr / n
		s := curr % n

		if isTarget[t][s] {
			return dist[curr]
		}

		ns := (s + 1) % n
		nextL := t*n + ns
		if dist[nextL] == -1 {
			dist[nextL] = dist[curr] + 1
			queue = append(queue, nextL)
		}

		nt := 1 - t
		nrs := (n - s) % n
		nextR := nt*n + nrs
		if dist[nextR] == -1 {
			dist[nextR] = dist[curr] + 1
			queue = append(queue, nextR)
		}
	}

	return -1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_operations(nums)
  n = nums.length
  idx0 = nums.index(0)

  is_target = Array.new(2) { Array.new(n, false) }

  is_type0 = true
  n.times do |j|
    if nums[(idx0 + j) % n] != j
      is_type0 = false
      break
    end
  end
  is_target[0][idx0] = true if is_type0

  idx0_rev = n - 1 - idx0
  is_type1 = true
  n.times do |j|
    if nums[n - 1 - (idx0_rev + j) % n] != j
      is_type1 = false
      break
    end
  end
  is_target[1][idx0_rev] = true if is_type1

  dist = Array.new(2 * n, -1)
  queue = [0]
  dist[0] = 0
  head = 0

  while head < queue.length
    curr = queue[head]
    head += 1

    t = curr / n
    s = curr % n

    return dist[curr] if is_target[t][s]

    ns = (s + 1) % n
    next_l = t * n + ns
    if dist[next_l] == -1
      dist[next_l] = dist[curr] + 1
      queue.push(next_l)
    end

    nt = 1 - t
    nrs = (n - s) % n
    next_r = nt * n + nrs
    if dist[next_r] == -1
      dist[next_r] = dist[curr] + 1
      queue.push(next_r)
    end
  end

  -1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def minOperations(nums: Array[Int]): Int = {
        val n = nums.length
        val idx0 = nums.indexOf(0)

        val isTarget = Array.fill(2, n)(false)

        var isType0 = true
        var j0 = 0
        while (j0 < n) {
            if (nums((idx0 + j0) % n) != j0) {
                isType0 = false
                j0 = n
            } else {
                j0 += 1
            }
        }
        if (isType0) isTarget(0)(idx0) = true

        val idx0Rev = n - 1 - idx0
        var isType1 = true
        var j1 = 0
        while (j1 < n) {
            if (nums(n - 1 - (idx0Rev + j1) % n) != j1) {
                isType1 = false
                j1 = n
            } else {
                j1 += 1
            }
        }
        if (isType1) isTarget(1)(idx0Rev) = true

        val dist = Array.fill(2 * n)(-1)
        val queue = mutable.Queue[Int]()

        dist(0) = 0
        queue.enqueue(0)

        while (queue.nonEmpty) {
            val curr = queue.dequeue()
            val t = curr / n
            val s = curr % n

            if (isTarget(t)(s)) return dist(curr)

            val ns = (s + 1) % n
            val nextL = t * n + ns
            if (dist(nextL) == -1) {
                dist(nextL) = dist(curr) + 1
                queue.enqueue(nextL)
            }

            val nt = 1 - t
            val nrs = (n - s) % n
            val nextR = nt * n + nrs
            if (dist(nextR) == -1) {
                dist(nextR) = dist(curr) + 1
                queue.enqueue(nextR)
            }
        }

        -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut idx0 = 0;
        for (i, &val) in nums.iter().enumerate() {
            if val == 0 {
                idx0 = i;
                break;
            }
        }

        let mut t1: i32 = -1;
        let mut ok1 = true;
        for i in 0..n {
            if nums[(idx0 + i) % n] != i as i32 {
                ok1 = false;
                break;
            }
        }
        if ok1 {
            t1 = idx0 as i32;
        }

        let mut t2: i32 = -1;
        let mut ok2 = true;
        for i in 0..n {
            if nums[(idx0 + n - i) % n] != i as i32 {
                ok2 = false;
                break;
            }
        }
        if ok2 {
            t2 = (n - 1 - idx0) as i32;
        }

        let mut ans = i32::MAX;
        if t1 != -1 {
            ans = ans.min(t1);
            ans = ans.min(n as i32 - t1 + 2);
        }
        if t2 != -1 {
            ans = ans.min(t2 + 1);
            ans = ans.min(n as i32 - t2 + 1);
        }

        if ans == i32::MAX {
            -1
        } else {
            ans
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [v (list->vector nums)]
         [idx0 (for/first ([i (in-range n)] #:when (= (vector-ref v i) 0)) i)])
    (let ([t1 (if (for/and ([i (in-range n)])
                    (= (vector-ref v (modulo (+ idx0 i) n)) i))
                  idx0
                  -1)]
          [t2 (if (for/and ([i (in-range n)])
                    (= (vector-ref v (modulo (- idx0 i) n)) i))
                  (- n 1 idx0)
                  -1)])
      (let ([ans1 (if (= t1 -1) 1000000000 (min t1 (+ (- n t1) 2)))]
            [ans2 (if (= t2 -1) 1000000000 (min (+ t2 1) (+ (- n t2) 1)))])
        (let ([final-ans (min ans1 ans2)])
          (if (= final-ans 1000000000)
              -1
              final-ans))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
    N = length(Nums),
    Tuple = list_to_tuple(Nums),
    Idx0 = find_idx0(0, Tuple),
    T1 = case check_t1(0, Idx0, N, Tuple) of
        true -> Idx0;
        false -> -1
    end,
    T2 = case check_t2(0, Idx0, N, Tuple) of
        true -> (N - 1 - Idx0);
        false -> -1
    end,
    Ans1 = if T1 =:= -1 -> 1000000000;
              true -> min(T1, N - T1 + 2)
           end,
    Ans2 = if T2 =:= -1 -> 1000000000;
              true -> min(T2 + 1, N - T2 + 1)
           end,
    FinalAns = min(Ans1, Ans2),
    if FinalAns =:= 1000000000 -> -1;
       true -> FinalAns
    end.

find_idx0(I, Tuple) ->
    case element(I + 1, Tuple) of
        0 -> I;
        _ -> find_idx0(I + 1, Tuple)
    end.

check_t1(I, Idx0, N, Tuple) when I < N ->
    Val = element(((Idx0 + I) rem N) + 1, Tuple),
    if Val =:= I -> check_t1(I + 1, Idx0, N, Tuple);
       true -> false
    end;
check_t1(_I, _Idx0, _N, _Tuple) -> true.

check_t2(I, Idx0, N, Tuple) when I < N ->
    Val = element(((Idx0 - I + N) rem N) + 1, Tuple),
    if Val =:= I -> check_t2(I + 1, Idx0, N, Tuple);
       true -> false
    end;
check_t2(_I, _Idx0, _N, _Tuple) -> true.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    n = length(nums)
    tuple = List.to_tuple(nums)
    idx0 = Enum.find_index(nums, fn x -> x == 0 end)

    t1 = if check_t1(0, idx0, n, tuple), do: idx0, else: -1
    t2 = if check_t2(0, idx0, n, tuple), do: (n - 1 - idx0), else: -1

    ans = 1_000_000_000
    ans = if t1 != -1 do
      d1 = t1
      d2 = n - t1 + 2
      min(ans, min(d1, d2))
    else
      ans
    end
    ans = if t2 != -1 do
      d1 = t2 + 1
      d2 = n - t2 + 1
      min(ans, min(d1, d2))
    else
      ans
    end

    if ans == 1_000_000_000, do: -1, else: ans
  end

  defp check_t1(i, idx0, n, tuple) do
    if i == n do
      true
    else
      if elem(tuple, rem(idx0 + i, n)) == i do
        check_t1(i + 1, idx0, n, tuple)
      else
        false
      end
    end
  end

  defp check_t2(i, idx0, n, tuple) do
    if i == n do
      true
    else
      if elem(tuple, rem(idx0 - i + n, n)) == i do
        check_t2(i + 1, idx0, n, tuple)
      else
        false
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) with one-paragraph explanation. Identifying whether the array is cyclically increasing or decreasing takes $O(n)$ time by iterating through the array once. The BFS visits at most $2n$ states and $4n$ edges, leading to a total time complexity of $O(n)$.
- **Space Complexity:** O(n) with one-paragraph explanation. We store the distance for $2n$ states and a BFS queue which can contain up to $2n$ elements. This results in $O(n)$ space complexity.
