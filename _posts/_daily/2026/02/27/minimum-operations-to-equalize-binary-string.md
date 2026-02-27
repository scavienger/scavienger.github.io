---
layout: post
title: "Minimum Operations to Equalize Binary String"
date: 2026-02-27 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Math", "String", "Breadth-First Search", "Union-Find", "Ordered Set"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int find(int p, int i, int n, vector<vector<int>>&\
        \ dsu) {\n        if (i > n) return n + 2;\n        int root = i;\n        while\
        \ (dsu[p][root] != root) root = dsu[p][root];\n        while (dsu[p][i] != root)\
        \ {\n            int next = dsu[p][i];\n            dsu[p][i] = root;\n    \
        \        i = next;\n        }\n        return root;\n    }\n\n    int minOperations(string\
        \ s, int k) {\n        int n = s.length();\n        int z = 0;\n        for\
        \ (char c : s) if (c == '0') z++;\n        if (z == 0) return 0;\n\n       \
        \ vector<vector<int>> dsu(2, vector<int>(n + 3));\n        for (int i = 0; i\
        \ <= n + 2; i++) {\n            dsu[0][i] = i;\n            dsu[1][i] = i;\n\
        \        }\n\n        vector<int> dist(n + 1, -1);\n        queue<int> q;\n\
        \        q.push(z);\n        dist[z] = 0;\n        dsu[z % 2][z] = find(z %\
        \ 2, z + 2, n, dsu);\n\n        while (!q.empty()) {\n            int curr_z\
        \ = q.front();\n            q.pop();\n            int i_min = max(0, k - (n\
        \ - curr_z));\n            int i_max = min(k, curr_z);\n            int L =\
        \ curr_z + k - 2 * i_max;\n            int R = curr_z + k - 2 * i_min;\n   \
        \         int p = (curr_z + k) % 2;\n\n            for (int next_z = find(p,\
        \ L, n, dsu); next_z <= R; next_z = find(p, next_z, n, dsu)) {\n           \
        \     if (next_z == 0) return dist[curr_z] + 1;\n                dist[next_z]\
        \ = dist[curr_z] + 1;\n                q.push(next_z);\n                dsu[p][next_z]\
        \ = find(p, next_z + 2, n, dsu);\n            }\n        }\n\n        return\
        \ -1;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    private int find(int[] dsu,\
        \ int i, int n) {\n        if (i > n) return n + 2;\n        int root = i;\n\
        \        while (dsu[root] != root) root = dsu[root];\n        while (dsu[i]\
        \ != root) {\n            int next = dsu[i];\n            dsu[i] = root;\n \
        \           i = next;\n        }\n        return root;\n    }\n\n    public\
        \ int minOperations(String s, int k) {\n        int n = s.length();\n      \
        \  int z = 0;\n        for (int i = 0; i < n; i++) if (s.charAt(i) == '0') z++;\n\
        \        if (z == 0) return 0;\n\n        int[] dsu0 = new int[n + 3];\n   \
        \     int[] dsu1 = new int[n + 3];\n        for (int i = 0; i <= n + 2; i++)\
        \ {\n            dsu0[i] = i;\n            dsu1[i] = i;\n        }\n\n     \
        \   int[] dist = new int[n + 1];\n        Arrays.fill(dist, -1);\n        Queue<Integer>\
        \ q = new ArrayDeque<>();\n        q.add(z);\n        dist[z] = 0;\n       \
        \ if (z % 2 == 0) dsu0[z] = find(dsu0, z + 2, n);\n        else dsu1[z] = find(dsu1,\
        \ z + 2, n);\n\n        while (!q.isEmpty()) {\n            int currZ = q.poll();\n\
        \            int iMin = Math.max(0, k - (n - currZ));\n            int iMax\
        \ = Math.min(k, currZ);\n            int L = currZ + k - 2 * iMax;\n       \
        \     int R = currZ + k - 2 * iMin;\n            int p = (currZ + k) % 2;\n\
        \            int[] dsu = (p == 0) ? dsu0 : dsu1;\n\n            for (int nextZ\
        \ = find(dsu, L, n); nextZ <= R; nextZ = find(dsu, nextZ, n)) {\n          \
        \      if (nextZ == 0) return dist[currZ] + 1;\n                dist[nextZ]\
        \ = dist[currZ] + 1;\n                q.add(nextZ);\n                dsu[nextZ]\
        \ = find(dsu, nextZ + 2, n);\n            }\n        }\n        return -1;\n\
        \    }\n}"
      python: "from collections import deque\n\nclass Solution(object):\n    def minOperations(self,\
        \ s, k):\n        n = len(s)\n        z = s.count('0')\n        if z == 0:\n\
        \            return 0\n\n        dsu = [list(range(n + 3)), list(range(n + 3))]\n\
        \n        def find(p, i):\n            if i > n: return n + 2\n            root\
        \ = i\n            while dsu[p][root] != root:\n                root = dsu[p][root]\n\
        \            while dsu[p][i] != root:\n                dsu[p][i], i = root,\
        \ dsu[p][i]\n            return root\n\n        dist = [-1] * (n + 1)\n    \
        \    q = deque([z])\n        dist[z] = 0\n        dsu[z % 2][z] = find(z % 2,\
        \ z + 2)\n\n        while q:\n            curr_z = q.popleft()\n           \
        \ i_min = max(0, k - (n - curr_z))\n            i_max = min(k, curr_z)\n   \
        \         L = curr_z + k - 2 * i_max\n            R = curr_z + k - 2 * i_min\n\
        \            p = (curr_z + k) % 2\n\n            next_z = find(p, L)\n     \
        \       while next_z <= R:\n                if next_z == 0: return dist[curr_z]\
        \ + 1\n                dist[next_z] = dist[curr_z] + 1\n                q.append(next_z)\n\
        \                dsu[p][next_z] = find(p, next_z + 2)\n                next_z\
        \ = find(p, next_z)\n\n        return -1"
      python3: "from collections import deque\n\nclass Solution:\n    def minOperations(self,\
        \ s: str, k: int) -> int:\n        n = len(s)\n        z = s.count('0')\n  \
        \      if z == 0:\n            return 0\n\n        dsu = [list(range(n + 3)),\
        \ list(range(n + 3))]\n\n        def find(p, i):\n            if i > n: return\
        \ n + 2\n            root = i\n            while dsu[p][root] != root:\n   \
        \             root = dsu[p][root]\n            curr = i\n            while dsu[p][curr]\
        \ != root:\n                dsu[p][curr], curr = root, dsu[p][curr]\n      \
        \      return root\n\n        dist = [-1] * (n + 1)\n        q = deque([z])\n\
        \        dist[z] = 0\n        dsu[z % 2][z] = find(z % 2, z + 2)\n\n       \
        \ while q:\n            curr_z = q.popleft()\n            i_min = max(0, k -\
        \ (n - curr_z))\n            i_max = min(k, curr_z)\n            L = curr_z\
        \ + k - 2 * i_max\n            R = curr_z + k - 2 * i_min\n            p = (curr_z\
        \ + k) % 2\n\n            next_z = find(p, L)\n            while next_z <= R:\n\
        \                if next_z == 0: return dist[curr_z] + 1\n                dist[next_z]\
        \ = dist[curr_z] + 1\n                q.append(next_z)\n                dsu[p][next_z]\
        \ = find(p, next_z + 2)\n                next_z = find(p, next_z)\n\n      \
        \  return -1"
      c: "#include <string.h>\n#include <stdlib.h>\n\n#define MAX(a, b) ((a) > (b) ?\
        \ (a) : (b))\n#define MIN(a, b) ((a) < (b) ? (a) : (b))\n\nint find(int* dsu,\
        \ int i, int n) {\n    if (i > n) return n + 2;\n    int root = i;\n    while\
        \ (dsu[root] != root) root = dsu[root];\n    while (dsu[i] != root) {\n    \
        \    int next = dsu[i];\n        dsu[i] = root;\n        i = next;\n    }\n\
        \    return root;\n}\n\nint minOperations(char* s, int k) {\n    int n = strlen(s);\n\
        \    int z = 0;\n    for (int i = 0; i < n; i++) if (s[i] == '0') z++;\n   \
        \ if (z == 0) return 0;\n\n    int* dsu0 = (int*)malloc((n + 3) * sizeof(int));\n\
        \    int* dsu1 = (int*)malloc((n + 3) * sizeof(int));\n    int* dist = (int*)malloc((n\
        \ + 1) * sizeof(int));\n    int* q = (int*)malloc((n + 1) * sizeof(int));\n\
        \    for (int i = 0; i <= n + 2; i++) {\n        dsu0[i] = i; dsu1[i] = i;\n\
        \    }\n    for (int i = 0; i <= n; i++) dist[i] = -1;\n\n    int head = 0,\
        \ tail = 0;\n    q[tail++] = z;\n    dist[z] = 0;\n    if (z % 2 == 0) dsu0[z]\
        \ = find(dsu0, z + 2, n);\n    else dsu1[z] = find(dsu1, z + 2, n);\n\n    int\
        \ res = -1;\n    while (head < tail) {\n        int curr_z = q[head++];\n  \
        \      int i_min = MAX(0, k - (n - curr_z));\n        int i_max = MIN(k, curr_z);\n\
        \        int L = curr_z + k - 2 * i_max;\n        int R = curr_z + k - 2 * i_min;\n\
        \        int p = (curr_z + k) % 2;\n        int* dsu = (p == 0) ? dsu0 : dsu1;\n\
        \n        for (int next_z = find(dsu, L, n); next_z <= R; next_z = find(dsu,\
        \ next_z, n)) {\n            if (next_z == 0) { res = dist[curr_z] + 1; goto\
        \ end; }\n            dist[next_z] = dist[curr_z] + 1;\n            q[tail++]\
        \ = next_z;\n            dsu[next_z] = find(dsu, next_z + 2, n);\n        }\n\
        \    }\n\nend:\n    free(dsu0); free(dsu1); free(dist); free(q);\n    return\
        \ res;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    private int Find(int[] dsu, int i, int n) {\n        if (i > n) return\
        \ n + 2;\n        int root = i;\n        while (dsu[root] != root) root = dsu[root];\n\
        \        while (dsu[i] != root) {\n            int next = dsu[i];\n        \
        \    dsu[i] = root;\n            i = next;\n        }\n        return root;\n\
        \    }\n\n    public int MinOperations(string s, int k) {\n        int n = s.Length;\n\
        \        int z = 0;\n        foreach (char c in s) if (c == '0') z++;\n    \
        \    if (z == 0) return 0;\n\n        int[] dsu0 = new int[n + 3];\n       \
        \ int[] dsu1 = new int[n + 3];\n        for (int i = 0; i <= n + 2; i++) { dsu0[i]\
        \ = i; dsu1[i] = i; }\n\n        int[] dist = new int[n + 1];\n        for (int\
        \ i = 0; i <= n; i++) dist[i] = -1;\n\n        Queue<int> q = new Queue<int>();\n\
        \        q.Enqueue(z);\n        dist[z] = 0;\n        if (z % 2 == 0) dsu0[z]\
        \ = Find(dsu0, z + 2, n);\n        else dsu1[z] = Find(dsu1, z + 2, n);\n\n\
        \        while (q.Count > 0) {\n            int currZ = q.Dequeue();\n     \
        \       int iMin = Math.Max(0, k - (n - currZ));\n            int iMax = Math.Min(k,\
        \ currZ);\n            int L = currZ + k - 2 * iMax;\n            int R = currZ\
        \ + k - 2 * iMin;\n            int p = (currZ + k) % 2;\n            int[] dsu\
        \ = (p == 0) ? dsu0 : dsu1;\n\n            for (int nextZ = Find(dsu, L, n);\
        \ nextZ <= R; nextZ = Find(dsu, nextZ, n)) {\n                if (nextZ == 0)\
        \ return dist[currZ] + 1;\n                dist[nextZ] = dist[currZ] + 1;\n\
        \                q.Enqueue(nextZ);\n                dsu[nextZ] = Find(dsu, nextZ\
        \ + 2, n);\n            }\n        }\n        return -1;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {number} k\n * @return {number}\n\
        \ */\nvar minOperations = function(s, k) {\n    const n = s.length;\n    let\
        \ z = 0;\n    for (let i = 0; i < n; i++) if (s[i] === '0') z++;\n    if (z\
        \ === 0) return 0;\n\n    const dsu0 = new Int32Array(n + 3);\n    const dsu1\
        \ = new Int32Array(n + 3);\n    for (let i = 0; i <= n + 2; i++) {\n       \
        \ dsu0[i] = i;\n        dsu1[i] = i;\n    }\n\n    function find(dsu, i) {\n\
        \        if (i > n) return n + 2;\n        let root = i;\n        while (dsu[root]\
        \ !== root) root = dsu[root];\n        while (dsu[i] !== root) {\n         \
        \   let next = dsu[i];\n            dsu[i] = root;\n            i = next;\n\
        \        }\n        return root;\n    }\n\n    const dist = new Int32Array(n\
        \ + 1).fill(-1);\n    const queue = [z];\n    let head = 0;\n    dist[z] = 0;\n\
        \    if (z % 2 === 0) dsu0[z] = find(dsu0, z + 2);\n    else dsu1[z] = find(dsu1,\
        \ z + 2);\n\n    while (head < queue.length) {\n        const currZ = queue[head++];\n\
        \        const iMin = Math.max(0, k - (n - currZ));\n        const iMax = Math.min(k,\
        \ currZ);\n        const L = currZ + k - 2 * iMax;\n        const R = currZ\
        \ + k - 2 * iMin;\n        const p = (currZ + k) % 2;\n        const dsu = (p\
        \ === 0) ? dsu0 : dsu1;\n\n        for (let nextZ = find(dsu, L); nextZ <= R;\
        \ nextZ = find(dsu, nextZ)) {\n            if (nextZ === 0) return dist[currZ]\
        \ + 1;\n            dist[nextZ] = dist[currZ] + 1;\n            queue.push(nextZ);\n\
        \            dsu[nextZ] = find(dsu, nextZ + 2);\n        }\n    }\n    return\
        \ -1;\n};"
      typescript: "function minOperations(s: string, k: number): number {\n    const\
        \ n = s.length;\n    let z = 0;\n    for (let i = 0; i < n; i++) if (s[i] ===\
        \ '0') z++;\n    if (z === 0) return 0;\n\n    const parent = new Int32Array(n\
        \ + 3);\n    for (let i = 0; i < n + 3; i++) parent[i] = i;\n    const dist\
        \ = new Int32Array(n + 1).fill(-1);\n\n    function find(i: number): number\
        \ {\n        let root = i;\n        while (parent[root] !== root) root = parent[root];\n\
        \        while (parent[i] !== root) {\n            let next = parent[i];\n \
        \           parent[i] = root;\n            i = next;\n        }\n        return\
        \ root;\n    }\n\n    const queue: number[] = [z];\n    let head = 0;\n    dist[z]\
        \ = 0;\n    parent[z] = find(z + 2);\n\n    while (head < queue.length) {\n\
        \        const u = queue[head++];\n        const minI = (k - (n - u) > 0) ?\
        \ k - (n - u) : 0;\n        const maxI = (u < k) ? u : k;\n        const minZ\
        \ = u + k - 2 * maxI;\n        const maxZ = u + k - 2 * minI;\n\n        let\
        \ curr = find(minZ);\n        while (curr <= maxZ) {\n            dist[curr]\
        \ = dist[u] + 1;\n            if (curr === 0) return dist[curr];\n         \
        \   queue.push(curr);\n            parent[curr] = find(curr + 2);\n        \
        \    curr = find(curr);\n        }\n    }\n    return -1;\n}"
      php: "class Solution {\n    /**\n     * @param String $s\n     * @param Integer\
        \ $k\n     * @return Integer\n     */\n    function minOperations($s, $k) {\n\
        \        $n = strlen($s);\n        $z = 0;\n        for ($i = 0; $i < $n; $i++)\
        \ if ($s[$i] === '0') $z++;\n        if ($z === 0) return 0;\n\n        $parent\
        \ = array_fill(0, $n + 3, 0);\n        for ($i = 0; $i <= $n + 2; $i++) $parent[$i]\
        \ = $i;\n        $dist = array_fill(0, $n + 1, -1);\n\n        $find = function($i)\
        \ use (&$parent) {\n            $root = $i;\n            while ($parent[$root]\
        \ !== $root) $root = $parent[$root];\n            $curr = $i;\n            while\
        \ ($parent[$curr] !== $root) {\n                $next = $parent[$curr];\n  \
        \              $parent[$curr] = $root;\n                $curr = $next;\n   \
        \         }\n            return $root;\n        };\n\n        $queue = [$z];\n\
        \        $head = 0;\n        $dist[$z] = 0;\n        $parent[$z] = $find($z\
        \ + 2);\n\n        while ($head < count($queue)) {\n            $u = $queue[$head++];\n\
        \            $minI = max(0, $k - ($n - $u));\n            $maxI = min($u, $k);\n\
        \            $minZ = $u + $k - 2 * $maxI;\n            $maxZ = $u + $k - 2 *\
        \ $minI;\n\n            $curr = $find($minZ);\n            while ($curr <= $maxZ)\
        \ {\n                $dist[$curr] = $dist[$u] + 1;\n                if ($curr\
        \ === 0) return $dist[$curr];\n                $queue[] = $curr;\n         \
        \       $parent[$curr] = $find($curr + 2);\n                $curr = $find($curr);\n\
        \            }\n        }\n        return -1;\n    }\n}"
      swift: "class Solution {\n    func minOperations(_ s: String, _ k: Int) -> Int\
        \ {\n        let n = s.count\n        let sArr = Array(s)\n        var z = 0\n\
        \        for char in sArr { if char == \"0\" { z += 1 } }\n        if z == 0\
        \ { return 0 }\n\n        var parent = Array(0...(n + 2))\n        var dist\
        \ = Array(repeating: -1, count: n + 1)\n\n        func find(_ i: Int) -> Int\
        \ {\n            var root = i\n            while parent[root] != root { root\
        \ = parent[root] }\n            var curr = i\n            while parent[curr]\
        \ != root {\n                let next = parent[curr]\n                parent[curr]\
        \ = root\n                curr = next\n            }\n            return root\n\
        \        }\n\n        var queue = [z]\n        var head = 0\n        dist[z]\
        \ = 0\n        parent[z] = find(z + 2)\n\n        while head < queue.count {\n\
        \            let u = queue[head]\n            head += 1\n            let minI\
        \ = max(0, k - (n - u))\n            let maxI = min(u, k)\n            let minZ\
        \ = u + k - 2 * maxI\n            let maxZ = u + k - 2 * minI\n\n          \
        \  var curr = find(minZ)\n            while curr <= maxZ {\n               \
        \ dist[curr] = dist[u] + 1\n                if curr == 0 { return dist[curr]\
        \ }\n                queue.append(curr)\n                parent[curr] = find(curr\
        \ + 2)\n                curr = find(curr)\n            }\n        }\n      \
        \  return -1\n    }\n}"
      kotlin: "import kotlin.collections.ArrayDeque\n\nclass Solution {\n    fun minOperations(s:\
        \ String, k: Int): Int {\n        val n = s.length\n        var z = 0\n    \
        \    for (char in s) if (char == '0') z++\n        if (z == 0) return 0\n\n\
        \        val parent = IntArray(n + 3) { it }\n        val dist = IntArray(n\
        \ + 1) { -1 }\n\n        fun find(i: Int): Int {\n            var root = i\n\
        \            while (parent[root] != root) root = parent[root]\n            var\
        \ curr = i\n            while (parent[curr] != root) {\n                val\
        \ next = parent[curr]\n                parent[curr] = root\n               \
        \ curr = next\n            }\n            return root\n        }\n\n       \
        \ val queue = ArrayDeque<Int>()\n        queue.add(z)\n        dist[z] = 0\n\
        \        parent[z] = find(z + 2)\n\n        while (queue.isNotEmpty()) {\n \
        \           val u = queue.removeFirst()\n            val minI = if (0 > k -\
        \ (n - u)) 0 else k - (n - u)\n            val maxI = if (u < k) u else k\n\
        \            val minZ = u + k - 2 * maxI\n            val maxZ = u + k - 2 *\
        \ minI\n\n            var curr = find(minZ)\n            while (curr <= maxZ)\
        \ {\n                dist[curr] = dist[u] + 1\n                if (curr == 0)\
        \ return dist[curr]\n                queue.add(curr)\n                parent[curr]\
        \ = find(curr + 2)\n                curr = find(curr)\n            }\n     \
        \   }\n        return -1\n    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  int minOperations(String\
        \ s, int k) {\n    int n = s.length;\n    int z = 0;\n    for (int i = 0; i\
        \ < n; i++) {\n      if (s[i] == '0') z++;\n    }\n    if (z == 0) return 0;\n\
        \n    List<int> parent = List<int>.generate(n + 3, (i) => i);\n    List<int>\
        \ dist = List<int>.filled(n + 1, -1);\n\n    int find(int i) {\n      int root\
        \ = i;\n      while (parent[root] != root) root = parent[root];\n      int curr\
        \ = i;\n      while (parent[curr] != root) {\n        int next = parent[curr];\n\
        \        parent[curr] = root;\n        curr = next;\n      }\n      return root;\n\
        \    }\n\n    Queue<int> queue = Queue<int>();\n    queue.add(z);\n    dist[z]\
        \ = 0;\n    parent[z] = find(z + 2);\n\n    while (queue.isNotEmpty) {\n   \
        \   int u = queue.removeFirst();\n      int minI = (k - (n - u) > 0) ? k - (n\
        \ - u) : 0;\n      int maxI = (u < k) ? u : k;\n      int minZ = u + k - 2 *\
        \ maxI;\n      int maxZ = u + k - 2 * minI;\n\n      int curr = find(minZ);\n\
        \      while (curr <= maxZ) {\n        dist[curr] = dist[u] + 1;\n        if\
        \ (curr == 0) return dist[curr];\n        queue.add(curr);\n        parent[curr]\
        \ = find(curr + 2);\n        curr = find(curr);\n      }\n    }\n    return\
        \ -1;\n  }\n}"
      go: "func minOperations(s string, k int) int {\n    n := len(s)\n    z := 0\n\
        \    for i := 0; i < n; i++ {\n        if s[i] == '0' {\n            z++\n \
        \       }\n    }\n    if z == 0 {\n        return 0\n    }\n\n    parent :=\
        \ make([]int, n+3)\n    for i := range parent {\n        parent[i] = i\n   \
        \ }\n    dist := make([]int, n+1)\n    for i := range dist {\n        dist[i]\
        \ = -1\n    }\n\n    find := func(i int) int {\n        root := i\n        for\
        \ parent[root] != root {\n            root = parent[root]\n        }\n     \
        \   curr := i\n        for parent[curr] != root {\n            next := parent[curr]\n\
        \            parent[curr] = root\n            curr = next\n        }\n     \
        \   return root\n    }\n\n    queue := []int{z}\n    dist[z] = 0\n    parent[z]\
        \ = find(z + 2)\n\n    for len(queue) > 0 {\n        u := queue[0]\n       \
        \ queue = queue[1:]\n\n        minI := 0\n        if k-(n-u) > 0 {\n       \
        \     minI = k - (n - u)\n        }\n        maxI := u\n        if k < u {\n\
        \            maxI = k\n        }\n        minZ := u + k - 2*maxI\n        maxZ\
        \ := u + k - 2*minI\n\n        for curr := find(minZ); curr <= maxZ; curr =\
        \ find(curr) {\n            dist[curr] = dist[u] + 1\n            if curr ==\
        \ 0 {\n                return dist[curr]\n            }\n            queue =\
        \ append(queue, curr)\n            parent[curr] = find(curr + 2)\n        }\n\
        \    }\n    return -1\n}"
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
    approach: "The problem can be modeled as finding the shortest path in a graph where\
      \ each state represents the current number of zeros $z$ in the binary string.\
      \ From a state with $z$ zeros, flipping exactly $k$ indices results in a new number\
      \ of zeros $z' = z + (k-i) - i = z + k - 2i$, where $i$ is the number of zeros\
      \ flipped. The number of flipped zeros $i$ is constrained by the available zeros\
      \ and ones: $\\max(0, k - (n - z)) \\leq i \\leq \\min(k, z)$. This defines a\
      \ contiguous range of reachable states $[z'_{min}, z'_{max}]$ that all share the\
      \ same parity as $z+k$. \n\nTo efficiently solve for the minimum operations, we\
      \ perform a Breadth-First Search (BFS) starting from the initial count of zeros.\
      \ To avoid the $O(n^2)$ complexity of exploring every possible edge in the range,\
      \ we use two Disjoint Set Union (DSU) structures (one for even and one for odd\
      \ counts) to skip states that have already been visited. By jumping directly to\
      \ the next unvisited state in the reachable range using the DSU, each state is\
      \ added to the BFS queue at most once. This ensures the algorithm runs in near-linear\
      \ time, making it efficient for strings up to $10^5$ characters."
    time_complexity: O(n \alpha(n)) where $n$ is the length of the string and $\alpha$
      is the inverse Ackermann function. This is because each state (number of zeros
      from $0$ to $n$) is visited at most once during the BFS, and the DSU operations
      for range skipping take nearly constant time.
    space_complexity: O(n) to store the distance array, the BFS queue, and the two DSU
      arrays, each of which scales linearly with the length of the input string.
    elapsed_time: 421.84007358551025
    model: gemini-3-flash-preview
    generated_at: '2026-02-27 01:27:22 '
---

## Problem #3666: Minimum Operations to Equalize Binary String

**Difficulty:** Hard

**Topics:** Math, String, Breadth-First Search, Union-Find, Ordered Set

## Problem Description

<p>You are given a binary string <code>s</code>, and an integer <code>k</code>.</p>

<p>In one operation, you must choose <strong>exactly</strong> <code>k</code> <strong>different</strong> indices and <strong>flip</strong> each <code>&#39;0&#39;</code> to <code>&#39;1&#39;</code> and each <code>&#39;1&#39;</code> to <code>&#39;0&#39;</code>.</p>

<p>Return the <strong>minimum</strong> number of operations required to make all characters in the string equal to <code>&#39;1&#39;</code>. If it is not possible, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;110&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There is one <code>&#39;0&#39;</code> in <code>s</code>.</li>
	<li>Since <code>k = 1</code>, we can flip it directly in one operation.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;0101&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal set of operations choosing <code>k = 3</code> indices in each operation is:</p>

<ul>
	<li><strong>Operation 1</strong>: Flip indices <code>[0, 1, 3]</code>. <code>s</code> changes from <code>&quot;0101&quot;</code> to <code>&quot;1000&quot;</code>.</li>
	<li><strong>Operation 2</strong>: Flip indices <code>[1, 2, 3]</code>. <code>s</code> changes from <code>&quot;1000&quot;</code> to <code>&quot;1111&quot;</code>.</li>
</ul>

<p>Thus, the minimum number of operations is 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;101&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>Since <code>k = 2</code> and <code>s</code> has only one <code>&#39;0&#39;</code>, it is impossible to flip exactly <code>k</code> indices to make all <code>&#39;1&#39;</code>. Hence, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>​​​​​​​5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>


## Hints

1. Model state as `z` = number of zeros; flipping `k` picks `i` zeros (`i` between `max(0, k - (n - z))` and `min(k, z)`) and transforms `z` to `z'` = `z + k - 2 * i`, so `z'` lies in a contiguous range and has parity `(z + k) % 2`.

2. Build a graph on states `0..n` and run `BFS` from initial `z` to reach `0`; each edge from `z` goes to all `z'` in that computed interval.

3. For speed, keep two ordered sets of unvisited states by parity and erase ranges with `lower_bound` while `BFSing` to achieve near `O(n log n)` time.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as finding the shortest path in a graph where each state represents the current number of zeros $z$ in the binary string. From a state with $z$ zeros, flipping exactly $k$ indices results in a new number of zeros $z' = z + (k-i) - i = z + k - 2i$, where $i$ is the number of zeros flipped. The number of flipped zeros $i$ is constrained by the available zeros and ones: $\max(0, k - (n - z)) \leq i \leq \min(k, z)$. This defines a contiguous range of reachable states $[z'_{min}, z'_{max}]$ that all share the same parity as $z+k$. 

To efficiently solve for the minimum operations, we perform a Breadth-First Search (BFS) starting from the initial count of zeros. To avoid the $O(n^2)$ complexity of exploring every possible edge in the range, we use two Disjoint Set Union (DSU) structures (one for even and one for odd counts) to skip states that have already been visited. By jumping directly to the next unvisited state in the reachable range using the DSU, each state is added to the BFS queue at most once. This ensures the algorithm runs in near-linear time, making it efficient for strings up to $10^5$ characters.

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
    int find(int p, int i, int n, vector<vector<int>>& dsu) {
        if (i > n) return n + 2;
        int root = i;
        while (dsu[p][root] != root) root = dsu[p][root];
        while (dsu[p][i] != root) {
            int next = dsu[p][i];
            dsu[p][i] = root;
            i = next;
        }
        return root;
    }

    int minOperations(string s, int k) {
        int n = s.length();
        int z = 0;
        for (char c : s) if (c == '0') z++;
        if (z == 0) return 0;

        vector<vector<int>> dsu(2, vector<int>(n + 3));
        for (int i = 0; i <= n + 2; i++) {
            dsu[0][i] = i;
            dsu[1][i] = i;
        }

        vector<int> dist(n + 1, -1);
        queue<int> q;
        q.push(z);
        dist[z] = 0;
        dsu[z % 2][z] = find(z % 2, z + 2, n, dsu);

        while (!q.empty()) {
            int curr_z = q.front();
            q.pop();
            int i_min = max(0, k - (n - curr_z));
            int i_max = min(k, curr_z);
            int L = curr_z + k - 2 * i_max;
            int R = curr_z + k - 2 * i_min;
            int p = (curr_z + k) % 2;

            for (int next_z = find(p, L, n, dsu); next_z <= R; next_z = find(p, next_z, n, dsu)) {
                if (next_z == 0) return dist[curr_z] + 1;
                dist[next_z] = dist[curr_z] + 1;
                q.push(next_z);
                dsu[p][next_z] = find(p, next_z + 2, n, dsu);
            }
        }

        return -1;
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
    private int find(int[] dsu, int i, int n) {
        if (i > n) return n + 2;
        int root = i;
        while (dsu[root] != root) root = dsu[root];
        while (dsu[i] != root) {
            int next = dsu[i];
            dsu[i] = root;
            i = next;
        }
        return root;
    }

    public int minOperations(String s, int k) {
        int n = s.length();
        int z = 0;
        for (int i = 0; i < n; i++) if (s.charAt(i) == '0') z++;
        if (z == 0) return 0;

        int[] dsu0 = new int[n + 3];
        int[] dsu1 = new int[n + 3];
        for (int i = 0; i <= n + 2; i++) {
            dsu0[i] = i;
            dsu1[i] = i;
        }

        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        Queue<Integer> q = new ArrayDeque<>();
        q.add(z);
        dist[z] = 0;
        if (z % 2 == 0) dsu0[z] = find(dsu0, z + 2, n);
        else dsu1[z] = find(dsu1, z + 2, n);

        while (!q.isEmpty()) {
            int currZ = q.poll();
            int iMin = Math.max(0, k - (n - currZ));
            int iMax = Math.min(k, currZ);
            int L = currZ + k - 2 * iMax;
            int R = currZ + k - 2 * iMin;
            int p = (currZ + k) % 2;
            int[] dsu = (p == 0) ? dsu0 : dsu1;

            for (int nextZ = find(dsu, L, n); nextZ <= R; nextZ = find(dsu, nextZ, n)) {
                if (nextZ == 0) return dist[currZ] + 1;
                dist[nextZ] = dist[currZ] + 1;
                q.add(nextZ);
                dsu[nextZ] = find(dsu, nextZ + 2, n);
            }
        }
        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
from collections import deque

class Solution(object):
    def minOperations(self, s, k):
        n = len(s)
        z = s.count('0')
        if z == 0:
            return 0

        dsu = [list(range(n + 3)), list(range(n + 3))]

        def find(p, i):
            if i > n: return n + 2
            root = i
            while dsu[p][root] != root:
                root = dsu[p][root]
            while dsu[p][i] != root:
                dsu[p][i], i = root, dsu[p][i]
            return root

        dist = [-1] * (n + 1)
        q = deque([z])
        dist[z] = 0
        dsu[z % 2][z] = find(z % 2, z + 2)

        while q:
            curr_z = q.popleft()
            i_min = max(0, k - (n - curr_z))
            i_max = min(k, curr_z)
            L = curr_z + k - 2 * i_max
            R = curr_z + k - 2 * i_min
            p = (curr_z + k) % 2

            next_z = find(p, L)
            while next_z <= R:
                if next_z == 0: return dist[curr_z] + 1
                dist[next_z] = dist[curr_z] + 1
                q.append(next_z)
                dsu[p][next_z] = find(p, next_z + 2)
                next_z = find(p, next_z)

        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        if z == 0:
            return 0

        dsu = [list(range(n + 3)), list(range(n + 3))]

        def find(p, i):
            if i > n: return n + 2
            root = i
            while dsu[p][root] != root:
                root = dsu[p][root]
            curr = i
            while dsu[p][curr] != root:
                dsu[p][curr], curr = root, dsu[p][curr]
            return root

        dist = [-1] * (n + 1)
        q = deque([z])
        dist[z] = 0
        dsu[z % 2][z] = find(z % 2, z + 2)

        while q:
            curr_z = q.popleft()
            i_min = max(0, k - (n - curr_z))
            i_max = min(k, curr_z)
            L = curr_z + k - 2 * i_max
            R = curr_z + k - 2 * i_min
            p = (curr_z + k) % 2

            next_z = find(p, L)
            while next_z <= R:
                if next_z == 0: return dist[curr_z] + 1
                dist[next_z] = dist[curr_z] + 1
                q.append(next_z)
                dsu[p][next_z] = find(p, next_z + 2)
                next_z = find(p, next_z)

        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int find(int* dsu, int i, int n) {
    if (i > n) return n + 2;
    int root = i;
    while (dsu[root] != root) root = dsu[root];
    while (dsu[i] != root) {
        int next = dsu[i];
        dsu[i] = root;
        i = next;
    }
    return root;
}

int minOperations(char* s, int k) {
    int n = strlen(s);
    int z = 0;
    for (int i = 0; i < n; i++) if (s[i] == '0') z++;
    if (z == 0) return 0;

    int* dsu0 = (int*)malloc((n + 3) * sizeof(int));
    int* dsu1 = (int*)malloc((n + 3) * sizeof(int));
    int* dist = (int*)malloc((n + 1) * sizeof(int));
    int* q = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n + 2; i++) {
        dsu0[i] = i; dsu1[i] = i;
    }
    for (int i = 0; i <= n; i++) dist[i] = -1;

    int head = 0, tail = 0;
    q[tail++] = z;
    dist[z] = 0;
    if (z % 2 == 0) dsu0[z] = find(dsu0, z + 2, n);
    else dsu1[z] = find(dsu1, z + 2, n);

    int res = -1;
    while (head < tail) {
        int curr_z = q[head++];
        int i_min = MAX(0, k - (n - curr_z));
        int i_max = MIN(k, curr_z);
        int L = curr_z + k - 2 * i_max;
        int R = curr_z + k - 2 * i_min;
        int p = (curr_z + k) % 2;
        int* dsu = (p == 0) ? dsu0 : dsu1;

        for (int next_z = find(dsu, L, n); next_z <= R; next_z = find(dsu, next_z, n)) {
            if (next_z == 0) { res = dist[curr_z] + 1; goto end; }
            dist[next_z] = dist[curr_z] + 1;
            q[tail++] = next_z;
            dsu[next_z] = find(dsu, next_z + 2, n);
        }
    }

end:
    free(dsu0); free(dsu1); free(dist); free(q);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    private int Find(int[] dsu, int i, int n) {
        if (i > n) return n + 2;
        int root = i;
        while (dsu[root] != root) root = dsu[root];
        while (dsu[i] != root) {
            int next = dsu[i];
            dsu[i] = root;
            i = next;
        }
        return root;
    }

    public int MinOperations(string s, int k) {
        int n = s.Length;
        int z = 0;
        foreach (char c in s) if (c == '0') z++;
        if (z == 0) return 0;

        int[] dsu0 = new int[n + 3];
        int[] dsu1 = new int[n + 3];
        for (int i = 0; i <= n + 2; i++) { dsu0[i] = i; dsu1[i] = i; }

        int[] dist = new int[n + 1];
        for (int i = 0; i <= n; i++) dist[i] = -1;

        Queue<int> q = new Queue<int>();
        q.Enqueue(z);
        dist[z] = 0;
        if (z % 2 == 0) dsu0[z] = Find(dsu0, z + 2, n);
        else dsu1[z] = Find(dsu1, z + 2, n);

        while (q.Count > 0) {
            int currZ = q.Dequeue();
            int iMin = Math.Max(0, k - (n - currZ));
            int iMax = Math.Min(k, currZ);
            int L = currZ + k - 2 * iMax;
            int R = currZ + k - 2 * iMin;
            int p = (currZ + k) % 2;
            int[] dsu = (p == 0) ? dsu0 : dsu1;

            for (int nextZ = Find(dsu, L, n); nextZ <= R; nextZ = Find(dsu, nextZ, n)) {
                if (nextZ == 0) return dist[currZ] + 1;
                dist[nextZ] = dist[currZ] + 1;
                q.Enqueue(nextZ);
                dsu[nextZ] = Find(dsu, nextZ + 2, n);
            }
        }
        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var minOperations = function(s, k) {
    const n = s.length;
    let z = 0;
    for (let i = 0; i < n; i++) if (s[i] === '0') z++;
    if (z === 0) return 0;

    const dsu0 = new Int32Array(n + 3);
    const dsu1 = new Int32Array(n + 3);
    for (let i = 0; i <= n + 2; i++) {
        dsu0[i] = i;
        dsu1[i] = i;
    }

    function find(dsu, i) {
        if (i > n) return n + 2;
        let root = i;
        while (dsu[root] !== root) root = dsu[root];
        while (dsu[i] !== root) {
            let next = dsu[i];
            dsu[i] = root;
            i = next;
        }
        return root;
    }

    const dist = new Int32Array(n + 1).fill(-1);
    const queue = [z];
    let head = 0;
    dist[z] = 0;
    if (z % 2 === 0) dsu0[z] = find(dsu0, z + 2);
    else dsu1[z] = find(dsu1, z + 2);

    while (head < queue.length) {
        const currZ = queue[head++];
        const iMin = Math.max(0, k - (n - currZ));
        const iMax = Math.min(k, currZ);
        const L = currZ + k - 2 * iMax;
        const R = currZ + k - 2 * iMin;
        const p = (currZ + k) % 2;
        const dsu = (p === 0) ? dsu0 : dsu1;

        for (let nextZ = find(dsu, L); nextZ <= R; nextZ = find(dsu, nextZ)) {
            if (nextZ === 0) return dist[currZ] + 1;
            dist[nextZ] = dist[currZ] + 1;
            queue.push(nextZ);
            dsu[nextZ] = find(dsu, nextZ + 2);
        }
    }
    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(s: string, k: number): number {
    const n = s.length;
    let z = 0;
    for (let i = 0; i < n; i++) if (s[i] === '0') z++;
    if (z === 0) return 0;

    const parent = new Int32Array(n + 3);
    for (let i = 0; i < n + 3; i++) parent[i] = i;
    const dist = new Int32Array(n + 1).fill(-1);

    function find(i: number): number {
        let root = i;
        while (parent[root] !== root) root = parent[root];
        while (parent[i] !== root) {
            let next = parent[i];
            parent[i] = root;
            i = next;
        }
        return root;
    }

    const queue: number[] = [z];
    let head = 0;
    dist[z] = 0;
    parent[z] = find(z + 2);

    while (head < queue.length) {
        const u = queue[head++];
        const minI = (k - (n - u) > 0) ? k - (n - u) : 0;
        const maxI = (u < k) ? u : k;
        const minZ = u + k - 2 * maxI;
        const maxZ = u + k - 2 * minI;

        let curr = find(minZ);
        while (curr <= maxZ) {
            dist[curr] = dist[u] + 1;
            if (curr === 0) return dist[curr];
            queue.push(curr);
            parent[curr] = find(curr + 2);
            curr = find(curr);
        }
    }
    return -1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function minOperations($s, $k) {
        $n = strlen($s);
        $z = 0;
        for ($i = 0; $i < $n; $i++) if ($s[$i] === '0') $z++;
        if ($z === 0) return 0;

        $parent = array_fill(0, $n + 3, 0);
        for ($i = 0; $i <= $n + 2; $i++) $parent[$i] = $i;
        $dist = array_fill(0, $n + 1, -1);

        $find = function($i) use (&$parent) {
            $root = $i;
            while ($parent[$root] !== $root) $root = $parent[$root];
            $curr = $i;
            while ($parent[$curr] !== $root) {
                $next = $parent[$curr];
                $parent[$curr] = $root;
                $curr = $next;
            }
            return $root;
        };

        $queue = [$z];
        $head = 0;
        $dist[$z] = 0;
        $parent[$z] = $find($z + 2);

        while ($head < count($queue)) {
            $u = $queue[$head++];
            $minI = max(0, $k - ($n - $u));
            $maxI = min($u, $k);
            $minZ = $u + $k - 2 * $maxI;
            $maxZ = $u + $k - 2 * $minI;

            $curr = $find($minZ);
            while ($curr <= $maxZ) {
                $dist[$curr] = $dist[$u] + 1;
                if ($curr === 0) return $dist[$curr];
                $queue[] = $curr;
                $parent[$curr] = $find($curr + 2);
                $curr = $find($curr);
            }
        }
        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ s: String, _ k: Int) -> Int {
        let n = s.count
        let sArr = Array(s)
        var z = 0
        for char in sArr { if char == "0" { z += 1 } }
        if z == 0 { return 0 }

        var parent = Array(0...(n + 2))
        var dist = Array(repeating: -1, count: n + 1)

        func find(_ i: Int) -> Int {
            var root = i
            while parent[root] != root { root = parent[root] }
            var curr = i
            while parent[curr] != root {
                let next = parent[curr]
                parent[curr] = root
                curr = next
            }
            return root
        }

        var queue = [z]
        var head = 0
        dist[z] = 0
        parent[z] = find(z + 2)

        while head < queue.count {
            let u = queue[head]
            head += 1
            let minI = max(0, k - (n - u))
            let maxI = min(u, k)
            let minZ = u + k - 2 * maxI
            let maxZ = u + k - 2 * minI

            var curr = find(minZ)
            while curr <= maxZ {
                dist[curr] = dist[u] + 1
                if curr == 0 { return dist[curr] }
                queue.append(curr)
                parent[curr] = find(curr + 2)
                curr = find(curr)
            }
        }
        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.collections.ArrayDeque

class Solution {
    fun minOperations(s: String, k: Int): Int {
        val n = s.length
        var z = 0
        for (char in s) if (char == '0') z++
        if (z == 0) return 0

        val parent = IntArray(n + 3) { it }
        val dist = IntArray(n + 1) { -1 }

        fun find(i: Int): Int {
            var root = i
            while (parent[root] != root) root = parent[root]
            var curr = i
            while (parent[curr] != root) {
                val next = parent[curr]
                parent[curr] = root
                curr = next
            }
            return root
        }

        val queue = ArrayDeque<Int>()
        queue.add(z)
        dist[z] = 0
        parent[z] = find(z + 2)

        while (queue.isNotEmpty()) {
            val u = queue.removeFirst()
            val minI = if (0 > k - (n - u)) 0 else k - (n - u)
            val maxI = if (u < k) u else k
            val minZ = u + k - 2 * maxI
            val maxZ = u + k - 2 * minI

            var curr = find(minZ)
            while (curr <= maxZ) {
                dist[curr] = dist[u] + 1
                if (curr == 0) return dist[curr]
                queue.add(curr)
                parent[curr] = find(curr + 2)
                curr = find(curr)
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
  int minOperations(String s, int k) {
    int n = s.length;
    int z = 0;
    for (int i = 0; i < n; i++) {
      if (s[i] == '0') z++;
    }
    if (z == 0) return 0;

    List<int> parent = List<int>.generate(n + 3, (i) => i);
    List<int> dist = List<int>.filled(n + 1, -1);

    int find(int i) {
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

    Queue<int> queue = Queue<int>();
    queue.add(z);
    dist[z] = 0;
    parent[z] = find(z + 2);

    while (queue.isNotEmpty) {
      int u = queue.removeFirst();
      int minI = (k - (n - u) > 0) ? k - (n - u) : 0;
      int maxI = (u < k) ? u : k;
      int minZ = u + k - 2 * maxI;
      int maxZ = u + k - 2 * minI;

      int curr = find(minZ);
      while (curr <= maxZ) {
        dist[curr] = dist[u] + 1;
        if (curr == 0) return dist[curr];
        queue.add(curr);
        parent[curr] = find(curr + 2);
        curr = find(curr);
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
func minOperations(s string, k int) int {
    n := len(s)
    z := 0
    for i := 0; i < n; i++ {
        if s[i] == '0' {
            z++
        }
    }
    if z == 0 {
        return 0
    }

    parent := make([]int, n+3)
    for i := range parent {
        parent[i] = i
    }
    dist := make([]int, n+1)
    for i := range dist {
        dist[i] = -1
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

    queue := []int{z}
    dist[z] = 0
    parent[z] = find(z + 2)

    for len(queue) > 0 {
        u := queue[0]
        queue = queue[1:]

        minI := 0
        if k-(n-u) > 0 {
            minI = k - (n - u)
        }
        maxI := u
        if k < u {
            maxI = k
        }
        minZ := u + k - 2*maxI
        maxZ := u + k - 2*minI

        for curr := find(minZ); curr <= maxZ; curr = find(curr) {
            dist[curr] = dist[u] + 1
            if curr == 0 {
                return dist[curr]
            }
            queue = append(queue, curr)
            parent[curr] = find(curr + 2)
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

- **Time Complexity:** O(n \alpha(n)) where $n$ is the length of the string and $\alpha$ is the inverse Ackermann function. This is because each state (number of zeros from $0$ to $n$) is visited at most once during the BFS, and the DSU operations for range skipping take nearly constant time.
- **Space Complexity:** O(n) to store the distance array, the BFS queue, and the two DSU arrays, each of which scales linearly with the length of the input string.
