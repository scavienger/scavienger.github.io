---
layout: post
title: "Minimum Jumps to Reach End via Prime Teleportation"
date: 2026-05-08 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Math", "Breadth-First Search", "Number Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minJumps(vector<int>& nums) {\n     \
        \   int n = nums.size();\n        if (n <= 1) return 0;\n        int maxVal\
        \ = 0;\n        for (int x : nums) if (x > maxVal) maxVal = x;\n\n        vector<int>\
        \ spf(maxVal + 1);\n        for (int i = 0; i <= maxVal; ++i) spf[i] = i;\n\
        \        for (int i = 2; i * i <= maxVal; ++i) {\n            if (spf[i] ==\
        \ i) {\n                for (int j = i * i; j <= maxVal; j += i)\n         \
        \           if (spf[j] == j) spf[j] = i;\n            }\n        }\n\n     \
        \   vector<bool> isPrime(maxVal + 1, false);\n        for (int i = 2; i <= maxVal;\
        \ ++i) if (spf[i] == i) isPrime[i] = true;\n\n        vector<int> primeCount(maxVal\
        \ + 1, 0);\n        int totalPairs = 0;\n        for (int x : nums) {\n    \
        \        int temp = x;\n            while (temp > 1) {\n                int\
        \ p = spf[temp];\n                primeCount[p]++;\n                totalPairs++;\n\
        \                while (temp % p == 0) temp /= p;\n            }\n        }\n\
        \n        vector<int> primeOffset(maxVal + 2, 0);\n        for (int i = 0; i\
        \ <= maxVal; ++i) primeOffset[i + 1] = primeOffset[i] + primeCount[i];\n\n \
        \       vector<int> flatBuckets(totalPairs);\n        vector<int> currentOffset\
        \ = primeOffset;\n        for (int i = 0; i < n; ++i) {\n            int temp\
        \ = nums[i];\n            while (temp > 1) {\n                int p = spf[temp];\n\
        \                flatBuckets[currentOffset[p]++] = i;\n                while\
        \ (temp % p == 0) temp /= p;\n            }\n        }\n\n        vector<int>\
        \ dist(n, -1);\n        vector<bool> primeUsed(maxVal + 1, false);\n       \
        \ queue<int> q;\n\n        dist[0] = 0;\n        q.push(0);\n\n        while\
        \ (!q.empty()) {\n            int u = q.front();\n            q.pop();\n   \
        \         if (u == n - 1) return dist[u];\n\n            for (int v : {u - 1,\
        \ u + 1}) {\n                if (v >= 0 && v < n && dist[v] == -1) {\n     \
        \               dist[v] = dist[u] + 1;\n                    if (v == n - 1)\
        \ return dist[v];\n                    q.push(v);\n                }\n     \
        \       }\n\n            int p = nums[u];\n            if (p <= maxVal && isPrime[p]\
        \ && !primeUsed[p]) {\n                for (int k = primeOffset[p]; k < primeOffset[p\
        \ + 1]; ++k) {\n                    int v = flatBuckets[k];\n              \
        \      if (dist[v] == -1) {\n                        dist[v] = dist[u] + 1;\n\
        \                        if (v == n - 1) return dist[v];\n                 \
        \       q.push(v);\n                    }\n                }\n             \
        \   primeUsed[p] = true;\n            }\n        }\n        return -1;\n   \
        \ }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int minJumps(int[]\
        \ nums) {\n        int n = nums.length;\n        if (n <= 1) return 0;\n   \
        \     int maxVal = 0;\n        for (int x : nums) if (x > maxVal) maxVal = x;\n\
        \n        int[] spf = new int[maxVal + 1];\n        for (int i = 0; i <= maxVal;\
        \ i++) spf[i] = i;\n        for (int i = 2; i * i <= maxVal; i++) {\n      \
        \      if (spf[i] == i) {\n                for (int j = i * i; j <= maxVal;\
        \ j += i)\n                    if (spf[j] == j) spf[j] = i;\n            }\n\
        \        }\n\n        boolean[] isPrime = new boolean[maxVal + 1];\n       \
        \ for (int i = 2; i <= maxVal; i++) if (spf[i] == i) isPrime[i] = true;\n\n\
        \        int[] primeCount = new int[maxVal + 1];\n        int totalPairs = 0;\n\
        \        for (int x : nums) {\n            int temp = x;\n            while\
        \ (temp > 1) {\n                int p = spf[temp];\n                primeCount[p]++;\n\
        \                totalPairs++;\n                while (temp % p == 0) temp /=\
        \ p;\n            }\n        }\n\n        int[] primeOffset = new int[maxVal\
        \ + 2];\n        for (int i = 0; i <= maxVal; i++) primeOffset[i + 1] = primeOffset[i]\
        \ + primeCount[i];\n\n        int[] flatBuckets = new int[totalPairs];\n   \
        \     int[] currentOffset = primeOffset.clone();\n        for (int i = 0; i\
        \ < n; i++) {\n            int temp = nums[i];\n            while (temp > 1)\
        \ {\n                int p = spf[temp];\n                flatBuckets[currentOffset[p]++]\
        \ = i;\n                while (temp % p == 0) temp /= p;\n            }\n  \
        \      }\n\n        int[] dist = new int[n];\n        Arrays.fill(dist, -1);\n\
        \        boolean[] primeUsed = new boolean[maxVal + 1];\n        Deque<Integer>\
        \ q = new ArrayDeque<>();\n\n        dist[0] = 0;\n        q.offer(0);\n\n \
        \       while (!q.isEmpty()) {\n            int u = q.poll();\n            if\
        \ (u == n - 1) return dist[u];\n\n            int[] neighbors = {u - 1, u +\
        \ 1};\n            for (int v : neighbors) {\n                if (v >= 0 &&\
        \ v < n && dist[v] == -1) {\n                    dist[v] = dist[u] + 1;\n  \
        \                  if (v == n - 1) return dist[v];\n                    q.offer(v);\n\
        \                }\n            }\n\n            int p = nums[u];\n        \
        \    if (p <= maxVal && isPrime[p] && !primeUsed[p]) {\n                for\
        \ (int k = primeOffset[p]; k < primeOffset[p + 1]; k++) {\n                \
        \    int v = flatBuckets[k];\n                    if (dist[v] == -1) {\n   \
        \                     dist[v] = dist[u] + 1;\n                        if (v\
        \ == n - 1) return dist[v];\n                        q.offer(v);\n         \
        \           }\n                }\n                primeUsed[p] = true;\n   \
        \         }\n        }\n        return -1;\n    }\n}"
      python: "import collections\n\nclass Solution(object):\n    def minJumps(self,\
        \ nums):\n        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n\
        \        \"\"\"\n        n = len(nums)\n        if n <= 1: return 0\n      \
        \  max_val = max(nums)\n\n        spf = list(range(max_val + 1))\n        for\
        \ i in range(2, int(max_val**0.5) + 1):\n            if spf[i] == i:\n     \
        \           for j in range(i*i, max_val + 1, i):\n                    if spf[j]\
        \ == j: spf[j] = i\n\n        is_prime = [False] * (max_val + 1)\n        for\
        \ i in range(2, max_val + 1): \n            if spf[i] == i: is_prime[i] = True\n\
        \n        buckets = collections.defaultdict(list)\n        for i, x in enumerate(nums):\n\
        \            temp = x\n            while temp > 1:\n                p = spf[temp]\n\
        \                buckets[p].append(i)\n                while temp % p == 0:\
        \ temp //= p\n\n        q = collections.deque([0])\n        dist = [-1] * n\n\
        \        dist[0] = 0\n        prime_used = [False] * (max_val + 1)\n\n     \
        \   while q:\n            u = q.popleft()\n            if u == n - 1: return\
        \ dist[u]\n\n            for v in [u - 1, u + 1]:\n                if 0 <= v\
        \ < n and dist[v] == -1:\n                    dist[v] = dist[u] + 1\n      \
        \              if v == n - 1: return dist[v]\n                    q.append(v)\n\
        \n            p = nums[u]\n            if p <= max_val and is_prime[p] and not\
        \ prime_used[p]:\n                for v in buckets[p]:\n                   \
        \ if dist[v] == -1:\n                        dist[v] = dist[u] + 1\n       \
        \                 if v == n - 1: return dist[v]\n                        q.append(v)\n\
        \                prime_used[p] = True\n        return -1"
      python3: "import collections\n\nclass Solution:\n    def minJumps(self, nums:\
        \ List[int]) -> int:\n        n = len(nums)\n        if n <= 1: return 0\n \
        \       max_val = max(nums)\n\n        spf = list(range(max_val + 1))\n    \
        \    for i in range(2, int(max_val**0.5) + 1):\n            if spf[i] == i:\n\
        \                for j in range(i*i, max_val + 1, i):\n                    if\
        \ spf[j] == j: spf[j] = i\n\n        is_prime = [False] * (max_val + 1)\n  \
        \      for i in range(2, max_val + 1):\n            if spf[i] == i: is_prime[i]\
        \ = True\n\n        buckets = collections.defaultdict(list)\n        for i,\
        \ x in enumerate(nums):\n            temp = x\n            while temp > 1:\n\
        \                p = spf[temp]\n                buckets[p].append(i)\n     \
        \           while temp % p == 0: temp //= p\n\n        q = collections.deque([0])\n\
        \        dist = [-1] * n\n        dist[0] = 0\n        prime_used = [False]\
        \ * (max_val + 1)\n\n        while q:\n            u = q.popleft()\n       \
        \     if u == n - 1: return dist[u]\n\n            for v in [u - 1, u + 1]:\n\
        \                if 0 <= v < n and dist[v] == -1:\n                    dist[v]\
        \ = dist[u] + 1\n                    if v == n - 1: return dist[v]\n       \
        \             q.append(v)\n\n            p = nums[u]\n            if p <= max_val\
        \ and is_prime[p] and not prime_used[p]:\n                for v in buckets[p]:\n\
        \                    if dist[v] == -1:\n                        dist[v] = dist[u]\
        \ + 1\n                        if v == n - 1: return dist[v]\n             \
        \           q.append(v)\n                prime_used[p] = True\n        return\
        \ -1"
      c: "#include <stdlib.h>\n#include <stdbool.h>\n#include <string.h>\n\nint minJumps(int*\
        \ nums, int numsSize) {\n    if (numsSize <= 1) return 0;\n    int maxVal =\
        \ 0;\n    for (int i = 0; i < numsSize; i++) if (nums[i] > maxVal) maxVal =\
        \ nums[i];\n\n    int* spf = (int*)malloc((maxVal + 1) * sizeof(int));\n   \
        \ for (int i = 0; i <= maxVal; i++) spf[i] = i;\n    for (int i = 2; i * i <=\
        \ maxVal; i++) {\n        if (spf[i] == i) {\n            for (int j = i * i;\
        \ j <= maxVal; j += i)\n                if (spf[j] == j) spf[j] = i;\n     \
        \   }\n    }\n\n    bool* isPrime = (bool*)calloc((maxVal + 1), sizeof(bool));\n\
        \    for (int i = 2; i <= maxVal; i++) if (spf[i] == i) isPrime[i] = true;\n\
        \n    int* primeCount = (int*)calloc((maxVal + 1), sizeof(int));\n    int totalPairs\
        \ = 0;\n    for (int i = 0; i < numsSize; i++) {\n        int temp = nums[i];\n\
        \        while (temp > 1) {\n            int p = spf[temp];\n            primeCount[p]++;\n\
        \            totalPairs++;\n            while (temp % p == 0) temp /= p;\n \
        \       }\n    }\n\n    int* primeOffset = (int*)malloc((maxVal + 2) * sizeof(int));\n\
        \    primeOffset[0] = 0;\n    for (int i = 0; i <= maxVal; i++) primeOffset[i\
        \ + 1] = primeOffset[i] + primeCount[i];\n\n    int* flatBuckets = (int*)malloc(totalPairs\
        \ * sizeof(int));\n    int* currentOffset = (int*)malloc((maxVal + 1) * sizeof(int));\n\
        \    memcpy(currentOffset, primeOffset, (maxVal + 1) * sizeof(int));\n\n   \
        \ for (int i = 0; i < numsSize; i++) {\n        int temp = nums[i];\n      \
        \  while (temp > 1) {\n            int p = spf[temp];\n            flatBuckets[currentOffset[p]++]\
        \ = i;\n            while (temp % p == 0) temp /= p;\n        }\n    }\n\n \
        \   int* dist = (int*)malloc(numsSize * sizeof(int));\n    for (int i = 0; i\
        \ < numsSize; i++) dist[i] = -1;\n    int* queue = (int*)malloc(numsSize * sizeof(int));\n\
        \    bool* primeUsed = (bool*)calloc((maxVal + 1), sizeof(bool));\n\n    int\
        \ head = 0, tail = 0;\n    dist[0] = 0;\n    queue[tail++] = 0;\n\n    int ans\
        \ = -1;\n    while (head < tail) {\n        int u = queue[head++];\n       \
        \ if (u == numsSize - 1) { ans = dist[u]; break; }\n\n        int neighbors[2]\
        \ = {u - 1, u + 1};\n        for (int k = 0; k < 2; k++) {\n            int\
        \ v = neighbors[k];\n            if (v >= 0 && v < numsSize && dist[v] == -1)\
        \ {\n                dist[v] = dist[u] + 1;\n                if (v == numsSize\
        \ - 1) { ans = dist[v]; goto end_bfs; }\n                queue[tail++] = v;\n\
        \            }\n        }\n\n        int p = nums[u];\n        if (p <= maxVal\
        \ && isPrime[p] && !primeUsed[p]) {\n            for (int k = primeOffset[p];\
        \ k < primeOffset[p + 1]; k++) {\n                int v = flatBuckets[k];\n\
        \                if (dist[v] == -1) {\n                    dist[v] = dist[u]\
        \ + 1;\n                    if (v == numsSize - 1) { ans = dist[v]; goto end_bfs;\
        \ }\n                    queue[tail++] = v;\n                }\n           \
        \ }\n            primeUsed[p] = true;\n        }\n    }\n\nend_bfs:\n    free(spf);\
        \ free(isPrime); free(primeCount); free(primeOffset); \n    free(flatBuckets);\
        \ free(currentOffset); free(dist); free(queue); free(primeUsed);\n    return\
        \ ans;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int MinJumps(int[] nums) {\n        int n = nums.Length;\n \
        \       if (n <= 1) return 0;\n\n        int maxVal = 0;\n        foreach (int\
        \ num in nums) {\n            if (num > maxVal) maxVal = num;\n        }\n\n\
        \        int[] minPrime = new int[maxVal + 1];\n        for (int i = 2; i *\
        \ i <= maxVal; i++) {\n            if (minPrime[i] == 0) {\n               \
        \ for (int j = i * i; j <= maxVal; j += i) {\n                    if (minPrime[j]\
        \ == 0) minPrime[j] = i;\n                }\n            }\n        }\n    \
        \    for (int i = 2; i <= maxVal; i++) {\n            if (minPrime[i] == 0)\
        \ minPrime[i] = i;\n        }\n\n        List<int>[] primeToIndices = new List<int>[maxVal\
        \ + 1];\n        for (int i = 0; i < n; i++) {\n            int temp = nums[i];\n\
        \            while (temp > 1) {\n                int p = minPrime[temp];\n \
        \               if (primeToIndices[p] == null) primeToIndices[p] = new List<int>();\n\
        \                primeToIndices[p].Add(i);\n                while (temp % p\
        \ == 0) temp /= p;\n            }\n        }\n\n        Queue<int> queue = new\
        \ Queue<int>();\n        bool[] visited = new bool[n];\n        queue.Enqueue(0);\n\
        \        visited[0] = true;\n        int steps = 0;\n\n        while (queue.Count\
        \ > 0) {\n            int size = queue.Count;\n            while (size-- > 0)\
        \ {\n                int i = queue.Dequeue();\n                if (i == n -\
        \ 1) return steps;\n\n                if (i + 1 < n && !visited[i + 1]) {\n\
        \                    visited[i + 1] = true;\n                    queue.Enqueue(i\
        \ + 1);\n                }\n                if (i - 1 >= 0 && !visited[i - 1])\
        \ {\n                    visited[i - 1] = true;\n                    queue.Enqueue(i\
        \ - 1);\n                }\n\n                int p = nums[i];\n           \
        \     if (p > 1 && p <= maxVal && minPrime[p] == p) {\n                    if\
        \ (primeToIndices[p] != null) {\n                        foreach (int j in primeToIndices[p])\
        \ {\n                            if (!visited[j]) {\n                      \
        \          visited[j] = true;\n                                queue.Enqueue(j);\n\
        \                            }\n                        }\n                \
        \        primeToIndices[p] = null;\n                    }\n                }\n\
        \            }\n            steps++;\n        }\n\n        return -1;\n    }\n\
        }"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minJumps\
        \ = function(nums) {\n    const n = nums.length;\n    if (n <= 1) return 0;\n\
        \n    let maxVal = 0;\n    for (let i = 0; i < n; i++) {\n        if (nums[i]\
        \ > maxVal) maxVal = nums[i];\n    }\n\n    const minPrime = new Int32Array(maxVal\
        \ + 1);\n    for (let i = 2; i * i <= maxVal; i++) {\n        if (minPrime[i]\
        \ === 0) {\n            for (let j = i * i; j <= maxVal; j += i) {\n       \
        \         if (minPrime[j] === 0) minPrime[j] = i;\n            }\n        }\n\
        \    }\n    for (let i = 2; i <= maxVal; i++) {\n        if (minPrime[i] ===\
        \ 0) minPrime[i] = i;\n    }\n\n    const primeToIndices = new Array(maxVal\
        \ + 1);\n    for (let i = 0; i < n; i++) {\n        let temp = nums[i];\n  \
        \      while (temp > 1) {\n            let p = minPrime[temp];\n           \
        \ if (!primeToIndices[p]) primeToIndices[p] = [];\n            primeToIndices[p].push(i);\n\
        \            while (temp % p === 0) temp /= p;\n        }\n    }\n\n    const\
        \ queue = [0];\n    const visited = new Uint8Array(n);\n    visited[0] = 1;\n\
        \    let steps = 0;\n    let head = 0;\n\n    while (head < queue.length) {\n\
        \        let size = queue.length - head;\n        while (size-- > 0) {\n   \
        \         const i = queue[head++];\n            if (i === n - 1) return steps;\n\
        \n            if (i + 1 < n && !visited[i + 1]) {\n                visited[i\
        \ + 1] = 1;\n                queue.push(i + 1);\n            }\n           \
        \ if (i - 1 >= 0 && !visited[i - 1]) {\n                visited[i - 1] = 1;\n\
        \                queue.push(i - 1);\n            }\n\n            const p =\
        \ nums[i];\n            if (p > 1 && p <= maxVal && minPrime[p] === p) {\n \
        \               if (primeToIndices[p]) {\n                    const indices\
        \ = primeToIndices[p];\n                    for (let k = 0; k < indices.length;\
        \ k++) {\n                        const j = indices[k];\n                  \
        \      if (!visited[j]) {\n                            visited[j] = 1;\n   \
        \                         queue.push(j);\n                        }\n      \
        \              }\n                    primeToIndices[p] = null;\n          \
        \      }\n            }\n        }\n        steps++;\n    }\n\n    return -1;\n\
        };"
      typescript: "function minJumps(nums: number[]): number {\n    const n = nums.length;\n\
        \    if (n <= 1) return 0;\n\n    let maxVal = 0;\n    for (let i = 0; i < n;\
        \ i++) {\n        if (nums[i] > maxVal) maxVal = nums[i];\n    }\n\n    const\
        \ minPrime = new Int32Array(maxVal + 1);\n    for (let i = 2; i * i <= maxVal;\
        \ i++) {\n        if (minPrime[i] === 0) {\n            for (let j = i * i;\
        \ j <= maxVal; j += i) {\n                if (minPrime[j] === 0) minPrime[j]\
        \ = i;\n            }\n        }\n    }\n    for (let i = 2; i <= maxVal; i++)\
        \ {\n        if (minPrime[i] === 0) minPrime[i] = i;\n    }\n\n    const primeToIndices:\
        \ (number[] | null)[] = new Array(maxVal + 1).fill(null);\n    for (let i =\
        \ 0; i < n; i++) {\n        let temp = nums[i];\n        while (temp > 1) {\n\
        \            let p = minPrime[temp];\n            if (!primeToIndices[p]) primeToIndices[p]\
        \ = [];\n            primeToIndices[p]!.push(i);\n            while (temp %\
        \ p === 0) temp /= p;\n        }\n    }\n\n    const queue: number[] = [0];\n\
        \    const visited = new Uint8Array(n);\n    visited[0] = 1;\n    let steps\
        \ = 0;\n    let head = 0;\n\n    while (head < queue.length) {\n        let\
        \ size = queue.length - head;\n        while (size-- > 0) {\n            const\
        \ i = queue[head++];\n            if (i === n - 1) return steps;\n\n       \
        \     if (i + 1 < n && !visited[i + 1]) {\n                visited[i + 1] =\
        \ 1;\n                queue.push(i + 1);\n            }\n            if (i -\
        \ 1 >= 0 && !visited[i - 1]) {\n                visited[i - 1] = 1;\n      \
        \          queue.push(i - 1);\n            }\n\n            const p = nums[i];\n\
        \            if (p > 1 && p <= maxVal && minPrime[p] === p) {\n            \
        \    const indices = primeToIndices[p];\n                if (indices) {\n  \
        \                  for (let k = 0; k < indices.length; k++) {\n            \
        \            const j = indices[k];\n                        if (!visited[j])\
        \ {\n                            visited[j] = 1;\n                         \
        \   queue.push(j);\n                        }\n                    }\n     \
        \               primeToIndices[p] = null;\n                }\n            }\n\
        \        }\n        steps++;\n    }\n\n    return -1;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minJumps($nums) {\n        $n = count($nums);\n\
        \        if ($n <= 1) return 0;\n\n        $maxVal = 0;\n        foreach ($nums\
        \ as $num) {\n            if ($num > $maxVal) $maxVal = $num;\n        }\n\n\
        \        $minPrime = new SplFixedArray($maxVal + 1);\n        for ($i = 0; $i\
        \ <= $maxVal; $i++) $minPrime[$i] = 0;\n\n        for ($i = 2; $i * $i <= $maxVal;\
        \ $i++) {\n            if ($minPrime[$i] === 0) {\n                for ($j =\
        \ $i * $i; $j <= $maxVal; $j += $i) {\n                    if ($minPrime[$j]\
        \ === 0) $minPrime[$j] = $i;\n                }\n            }\n        }\n\
        \        for ($i = 2; $i <= $maxVal; $i++) {\n            if ($minPrime[$i]\
        \ === 0) $minPrime[$i] = $i;\n        }\n\n        $primeToIndices = [];\n \
        \       for ($i = 0; $i < $n; $i++) {\n            $temp = $nums[$i];\n    \
        \        while ($temp > 1) {\n                $p = $minPrime[$temp];\n     \
        \           if (!isset($primeToIndices[$p])) $primeToIndices[$p] = [];\n   \
        \             $primeToIndices[$p][] = $i;\n                while ($temp % $p\
        \ === 0) $temp /= $p;\n            }\n        }\n\n        $queue = new SplQueue();\n\
        \        $visited = new SplFixedArray($n);\n        for ($i = 0; $i < $n; $i++)\
        \ $visited[$i] = false;\n        $queue->enqueue(0);\n        $visited[0] =\
        \ true;\n        $steps = 0;\n\n        while (!$queue->isEmpty()) {\n     \
        \       $size = $queue->count();\n            while ($size-- > 0) {\n      \
        \          $i = $queue->dequeue();\n                if ($i === $n - 1) return\
        \ $steps;\n\n                if ($i + 1 < $n && !$visited[$i + 1]) {\n     \
        \               $visited[$i + 1] = true;\n                    $queue->enqueue($i\
        \ + 1);\n                }\n                if ($i - 1 >= 0 && !$visited[$i\
        \ - 1]) {\n                    $visited[$i - 1] = true;\n                  \
        \  $queue->enqueue($i - 1);\n                }\n\n                $p = $nums[$i];\n\
        \                if ($p > 1 && $p <= $maxVal && $minPrime[$p] === $p) {\n  \
        \                  if (isset($primeToIndices[$p])) {\n                     \
        \   foreach ($primeToIndices[$p] as $j) {\n                            if (!$visited[$j])\
        \ {\n                                $visited[$j] = true;\n                \
        \                $queue->enqueue($j);\n                            }\n     \
        \                   }\n                        unset($primeToIndices[$p]);\n\
        \                    }\n                }\n            }\n            $steps++;\n\
        \        }\n\n        return -1;\n    }\n}"
      swift: "class Solution {\n    func minJumps(_ nums: [Int]) -> Int {\n        let\
        \ n = nums.count\n        if n <= 1 { return 0 }\n\n        var maxVal = 0\n\
        \        for num in nums {\n            if num > maxVal { maxVal = num }\n \
        \       }\n\n        var minPrime = [Int](repeating: 0, count: maxVal + 1)\n\
        \        if maxVal >= 2 {\n            let limit = Int(Double(maxVal).squareRoot())\n\
        \            for i in 2...limit {\n                if minPrime[i] == 0 {\n \
        \                   for j in stride(from: i * i, through: maxVal, by: i) {\n\
        \                        if minPrime[j] == 0 { minPrime[j] = i }\n         \
        \           }\n                }\n            }\n            for i in 2...maxVal\
        \ {\n                if minPrime[i] == 0 { minPrime[i] = i }\n            }\n\
        \        }\n\n        var primeToIndices = [Int: [Int]]()\n        for i in\
        \ 0..<n {\n            var temp = nums[i]\n            while temp > 1 {\n  \
        \              let p = minPrime[temp]\n                if primeToIndices[p]\
        \ == nil {\n                    primeToIndices[p] = [i]\n                } else\
        \ {\n                    primeToIndices[p]!.append(i)\n                }\n \
        \               while temp % p == 0 {\n                    temp /= p\n     \
        \           }\n            }\n        }\n\n        var visited = [Bool](repeating:\
        \ false, count: n)\n        var queue = [Int]()\n        queue.append(0)\n \
        \       visited[0] = true\n        var steps = 0\n        var head = 0\n\n \
        \       while head < queue.count {\n            let size = queue.count - head\n\
        \            for _ in 0..<size {\n                let i = queue[head]\n    \
        \            head += 1\n\n                if i == n - 1 { return steps }\n\n\
        \                if i + 1 < n && !visited[i + 1] {\n                    visited[i\
        \ + 1] = true\n                    queue.append(i + 1)\n                }\n\
        \                if i - 1 >= 0 && !visited[i - 1] {\n                    visited[i\
        \ - 1] = true\n                    queue.append(i - 1)\n                }\n\n\
        \                let p = nums[i]\n                if p > 1 && p <= maxVal &&\
        \ minPrime[p] == p {\n                    if let indices = primeToIndices[p]\
        \ {\n                        for j in indices {\n                          \
        \  if !visited[j] {\n                                visited[j] = true\n   \
        \                             queue.append(j)\n                            }\n\
        \                        }\n                        primeToIndices[p] = nil\n\
        \                    }\n                }\n            }\n            steps\
        \ += 1\n        }\n\n        return -1\n    }\n}"
      kotlin: "import java.util.ArrayDeque\n\nclass Solution {\n    fun minJumps(nums:\
        \ IntArray): Int {\n        val n = nums.size\n        if (n == 1) return 0\n\
        \n        val maxVal = 1000000\n        val spf = IntArray(maxVal + 1) { it\
        \ }\n        var i = 2\n        while (i * i <= maxVal) {\n            if (spf[i]\
        \ == i) {\n                var j = i * i\n                while (j <= maxVal)\
        \ {\n                    if (spf[j] == j) spf[j] = i\n                    j\
        \ += i\n                }\n            }\n            i++\n        }\n\n   \
        \     val existsAsPrime = BooleanArray(maxVal + 1)\n        for (x in nums)\
        \ {\n            if (x > 1 && spf[x] == x) existsAsPrime[x] = true\n       \
        \ }\n\n        val buckets = arrayOfNulls<MutableList<Int>>(maxVal + 1)\n  \
        \      for (idx in 0 until n) {\n            var x = nums[idx]\n           \
        \ while (x > 1) {\n                val p = spf[x]\n                if (existsAsPrime[p])\
        \ {\n                    if (buckets[p] == null) buckets[p] = mutableListOf<Int>()\n\
        \                    buckets[p]!!.add(idx)\n                }\n            \
        \    while (x % p == 0) x /= p\n            }\n        }\n\n        val dist\
        \ = IntArray(n) { -1 }\n        val queue = ArrayDeque<Int>()\n        val visitedPrimes\
        \ = BooleanArray(maxVal + 1)\n\n        dist[0] = 0\n        queue.add(0)\n\n\
        \        while (queue.isNotEmpty()) {\n            val u = queue.removeFirst()\n\
        \            if (u == n - 1) return dist[u]\n\n            val neighbors = intArrayOf(u\
        \ - 1, u + 1)\n            for (v in neighbors) {\n                if (v in\
        \ 0 until n && dist[v] == -1) {\n                    dist[v] = dist[u] + 1\n\
        \                    queue.add(v)\n                }\n            }\n\n    \
        \        val p = nums[u]\n            if (p > 1 && spf[p] == p && !visitedPrimes[p])\
        \ {\n                visitedPrimes[p] = true\n                buckets[p]?.let\
        \ { list ->\n                    for (v in list) {\n                       \
        \ if (dist[v] == -1) {\n                            dist[v] = dist[u] + 1\n\
        \                            queue.add(v)\n                        }\n     \
        \               }\n                }\n            }\n        }\n\n        return\
        \ -1\n    }\n}"
      dart: "import 'dart:collection';\nimport 'dart:typed_data';\n\nclass Solution\
        \ {\n  int minJumps(List<int> nums) {\n    int n = nums.length;\n    if (n ==\
        \ 1) return 0;\n\n    const int maxVal = 1000000;\n    Int32List spf = Int32List(maxVal\
        \ + 1);\n    for (int i = 0; i <= maxVal; i++) spf[i] = i;\n\n    for (int i\
        \ = 2; i * i <= maxVal; i++) {\n      if (spf[i] == i) {\n        for (int j\
        \ = i * i; j <= maxVal; j += i) {\n          if (spf[j] == j) spf[j] = i;\n\
        \        }\n      }\n    }\n\n    Uint8List existsAsPrime = Uint8List(maxVal\
        \ + 1);\n    for (int x in nums) {\n      if (x > 1 && spf[x] == x) existsAsPrime[x]\
        \ = 1;\n    }\n\n    List<List<int>?> buckets = List<List<int>?>.filled(maxVal\
        \ + 1, null);\n    for (int i = 0; i < n; i++) {\n      int x = nums[i];\n \
        \     while (x > 1) {\n        int p = spf[x];\n        if (existsAsPrime[p]\
        \ == 1) {\n          if (buckets[p] == null) buckets[p] = [];\n          buckets[p]!.add(i);\n\
        \        }\n        while (x % p == 0) x ~/= p;\n      }\n    }\n\n    Int32List\
        \ dist = Int32List(n)..fillRange(0, n, -1);\n    Uint8List visitedPrimes = Uint8List(maxVal\
        \ + 1);\n    Queue<int> queue = Queue<int>();\n\n    dist[0] = 0;\n    queue.add(0);\n\
        \n    while (queue.isNotEmpty) {\n      int u = queue.removeFirst();\n     \
        \ if (u == n - 1) return dist[u];\n\n      List<int> neighbors = [u - 1, u +\
        \ 1];\n      for (int v in neighbors) {\n        if (v >= 0 && v < n && dist[v]\
        \ == -1) {\n          dist[v] = dist[u] + 1;\n          queue.add(v);\n    \
        \    }\n      }\n\n      int p = nums[u];\n      if (p > 1 && spf[p] == p &&\
        \ visitedPrimes[p] == 0) {\n        visitedPrimes[p] = 1;\n        List<int>?\
        \ bucket = buckets[p];\n        if (bucket != null) {\n          for (int v\
        \ in bucket) {\n            if (dist[v] == -1) {\n              dist[v] = dist[u]\
        \ + 1;\n              queue.add(v);\n            }\n          }\n        }\n\
        \      }\n    }\n\n    return -1;\n  }\n}"
      go: "func minJumps(nums []int) int {\n    n := len(nums)\n    if n == 1 {\n  \
        \      return 0\n    }\n\n    const maxVal = 1000000\n    spf := make([]int32,\
        \ maxVal+1)\n    for i := 0; i <= maxVal; i++ {\n        spf[i] = int32(i)\n\
        \    }\n\n    for i := 2; i*i <= maxVal; i++ {\n        if spf[i] == int32(i)\
        \ {\n            for j := i * i; j <= maxVal; j += i {\n                if spf[j]\
        \ == int32(j) {\n                    spf[j] = int32(i)\n                }\n\
        \            }\n        }\n    }\n\n    existsAsPrime := make([]bool, maxVal+1)\n\
        \    for _, x := range nums {\n        if x > 1 && int(spf[x]) == x {\n    \
        \        existsAsPrime[x] = true\n        }\n    }\n\n    buckets := make([][]int,\
        \ maxVal+1)\n    for i := 0; i < n; i++ {\n        x := nums[i]\n        for\
        \ x > 1 {\n            p := int(spf[x])\n            if existsAsPrime[p] {\n\
        \                buckets[p] = append(buckets[p], i)\n            }\n       \
        \     for x%p == 0 {\n                x /= p\n            }\n        }\n   \
        \ }\n\n    dist := make([]int, n)\n    for i := range dist {\n        dist[i]\
        \ = -1\n    }\n    visitedPrimes := make([]bool, maxVal+1)\n\n    queue := []int{0}\n\
        \    dist[0] = 0\n    head := 0\n\n    for head < len(queue) {\n        u :=\
        \ queue[head]\n        head++\n\n        if u == n-1 {\n            return dist[u]\n\
        \        }\n\n        for _, v := range []int{u - 1, u + 1} {\n            if\
        \ v >= 0 && v < n && dist[v] == -1 {\n                dist[v] = dist[u] + 1\n\
        \                queue = append(queue, v)\n            }\n        }\n\n    \
        \    p := nums[u]\n        if p > 1 && int(spf[p]) == p && !visitedPrimes[p]\
        \ {\n            visitedPrimes[p] = true\n            for _, v := range buckets[p]\
        \ {\n                if dist[v] == -1 {\n                    dist[v] = dist[u]\
        \ + 1\n                    queue = append(queue, v)\n                }\n   \
        \         }\n        }\n    }\n\n    return -1\n}"
      ruby: "def min_jumps(nums)\n  n = nums.length\n  return 0 if n == 1\n\n  max_val\
        \ = 1000000\n  spf = Array.new(max_val + 1, 0)\n  i = 2\n  while i * i <= max_val\n\
        \    if spf[i] == 0\n      j = i * i\n      while j <= max_val\n        spf[j]\
        \ = i if spf[j] == 0\n        j += i\n      end\n    end\n    i += 1\n  end\n\
        \  (2..max_val).each { |k| spf[k] = k if spf[k] == 0 }\n\n  exists_as_prime\
        \ = Array.new(max_val + 1, false)\n  nums.each do |x|\n    exists_as_prime[x]\
        \ = true if x > 1 && spf[x] == x\n  end\n\n  buckets = {}\n  nums.each_with_index\
        \ do |x, idx|\n    temp = x\n    while temp > 1\n      p = spf[temp]\n     \
        \ if exists_as_prime[p]\n        buckets[p] ||= []\n        buckets[p] << idx\n\
        \      end\n      while temp % p == 0\n        temp /= p\n      end\n    end\n\
        \  end\n\n  dist = Array.new(n, -1)\n  visited_primes = Array.new(max_val +\
        \ 1, false)\n  queue = [0]\n  head = 0\n  dist[0] = 0\n\n  while head < queue.length\n\
        \    u = queue[head]\n    head += 1\n    return dist[u] if u == n - 1\n\n  \
        \  [u - 1, u + 1].each do |v|\n      if v >= 0 && v < n && dist[v] == -1\n \
        \       dist[v] = dist[u] + 1\n        queue << v\n      end\n    end\n\n  \
        \  p = nums[u]\n    if p > 1 && spf[p] == p && !visited_primes[p]\n      visited_primes[p]\
        \ = true\n      if buckets[p]\n        buckets[p].each do |v|\n          if\
        \ dist[v] == -1\n            dist[v] = dist[u] + 1\n            queue << v\n\
        \          end\n        end\n      end\n    end\n  end\n\n  return -1\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  def minJumps(nums:\
        \ Array[Int]): Int = {\n    val n = nums.length\n    if (n == 1) return 0\n\n\
        \    val maxVal = 1000000\n    val spf = Array.tabulate(maxVal + 1)(i => i)\n\
        \    var i = 2\n    while (i * i <= maxVal) {\n      if (spf(i) == i) {\n  \
        \      var j = i * i\n        while (j <= maxVal) {\n          if (spf(j) ==\
        \ j) spf(j) = i\n          j += i\n        }\n      }\n      i += 1\n    }\n\
        \n    val existsAsPrime = new Array[Boolean](maxVal + 1)\n    for (x <- nums)\
        \ {\n      if (x > 1 && spf(x) == x) existsAsPrime(x) = true\n    }\n\n    val\
        \ buckets = new Array[mutable.ListBuffer[Int]](maxVal + 1)\n    for (idx <-\
        \ 0 until n) {\n      var x = nums(idx)\n      while (x > 1) {\n        val\
        \ p = spf(x)\n        if (existsAsPrime(p)) {\n          if (buckets(p) == null)\
        \ buckets(p) = new mutable.ListBuffer[Int]()\n          buckets(p) += idx\n\
        \        }\n        while (x % p == 0) x /= p\n      }\n    }\n\n    val dist\
        \ = Array.fill(n)(-1)\n    val visitedPrimes = new Array[Boolean](maxVal + 1)\n\
        \    val queue = mutable.Queue[Int]()\n\n    dist(0) = 0\n    queue.enqueue(0)\n\
        \n    while (queue.nonEmpty) {\n      val u = queue.dequeue()\n      if (u ==\
        \ n - 1) return dist(u)\n\n      val neighbors = List(u - 1, u + 1)\n      for\
        \ (v <- neighbors) {\n        if (v >= 0 && v < n && dist(v) == -1) {\n    \
        \      dist(v) = dist(u) + 1\n          queue.enqueue(v)\n        }\n      }\n\
        \n      val p = nums(u)\n      if (p > 1 && spf(p) == p && !visitedPrimes(p))\
        \ {\n        visitedPrimes(p) = true\n        if (buckets(p) != null) {\n  \
        \        for (v <- buckets(p)) {\n            if (dist(v) == -1) {\n       \
        \       dist(v) = dist(u) + 1\n              queue.enqueue(v)\n            }\n\
        \          }\n        }\n      }\n    }\n\n    -1\n  }\n}"
      rust: "use std::collections::VecDeque;\n\nimpl Solution {\n    pub fn min_jumps(nums:\
        \ Vec<i32>) -> i32 {\n        let n = nums.len();\n        if n == 1 {\n   \
        \         return 0;\n        }\n\n        let mut max_val = 0;\n        for\
        \ &x in &nums {\n            if x > max_val {\n                max_val = x;\n\
        \            }\n        }\n\n        let mut spf = (0..=max_val).collect::<Vec<i32>>();\n\
        \        let mut i = 2;\n        while i * i <= max_val {\n            if spf[i\
        \ as usize] == i {\n                let mut j = i * i;\n                while\
        \ j <= max_val {\n                    if spf[j as usize] == j {\n          \
        \              spf[j as usize] = i;\n                    }\n               \
        \     j += i;\n                }\n            }\n            i += 1;\n     \
        \   }\n\n        let mut is_prime_in_nums = vec![false; max_val as usize + 1];\n\
        \        for &x in &nums {\n            if x >= 2 && spf[x as usize] == x {\n\
        \                is_prime_in_nums[x as usize] = true;\n            }\n     \
        \   }\n\n        let mut prime_to_indices = vec![vec![]; max_val as usize +\
        \ 1];\n        for (idx, &x) in nums.iter().enumerate() {\n            let mut\
        \ temp = x as usize;\n            while temp > 1 {\n                let p =\
        \ spf[temp] as usize;\n                if is_prime_in_nums[p] {\n          \
        \          prime_to_indices[p].push(idx);\n                }\n             \
        \   while temp % p == 0 {\n                    temp /= p;\n                }\n\
        \            }\n        }\n\n        let mut dist = vec![-1; n];\n        let\
        \ mut q = VecDeque::new();\n        dist[0] = 0;\n        q.push_back(0);\n\n\
        \        let mut prime_visited = vec![false; max_val as usize + 1];\n\n    \
        \    while let Some(u) = q.pop_front() {\n            if u == n - 1 {\n    \
        \            return dist[u];\n            }\n\n            if u + 1 < n && dist[u\
        \ + 1] == -1 {\n                dist[u + 1] = dist[u] + 1;\n               \
        \ q.push_back(u + 1);\n            }\n            if u > 0 && dist[u - 1] ==\
        \ -1 {\n                dist[u - 1] = dist[u] + 1;\n                q.push_back(u\
        \ - 1);\n            }\n\n            let val = nums[u] as usize;\n        \
        \    if val >= 2 && spf[val] == val as i32 && !prime_visited[val] {\n      \
        \          prime_visited[val] = true;\n                for &v in &prime_to_indices[val]\
        \ {\n                    if dist[v] == -1 {\n                        dist[v]\
        \ = dist[u] + 1;\n                        q.push_back(v);\n                \
        \    }\n                }\n            }\n        }\n\n        -1\n    }\n}"
      racket: "(define/contract (min-jumps nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([n (length nums)]\n         [nums-vec (list->vector nums)]\n     \
        \    [max-val (if (null? nums) 0 (apply max nums))])\n    (if (= n 1)\n    \
        \    0\n        (let* ([spf (make-vector (+ max-val 1) 0)])\n          (for\
        \ ([i (in-range 2 (+ max-val 1))])\n            (vector-set! spf i i))\n   \
        \       (for ([i (in-range 2 (+ 1 (integer-sqrt max-val)))])\n            (when\
        \ (= (vector-ref spf i) i)\n              (for ([j (in-range (* i i) (+ max-val\
        \ 1) i)])\n                (when (= (vector-ref spf j) j)\n                \
        \  (vector-set! spf j i)))))\n\n          (define is-prime-in-nums (make-vector\
        \ (+ max-val 1) #f))\n          (for ([x nums])\n            (when (and (>=\
        \ x 2) (= (vector-ref spf x) x))\n              (vector-set! is-prime-in-nums\
        \ x #t)))\n\n          (define prime-to-indices (make-vector (+ max-val 1) '()))\n\
        \          (for ([i (in-range n)])\n            (let ([x (vector-ref nums-vec\
        \ i)])\n              (let loop ([temp x])\n                (when (> temp 1)\n\
        \                  (let ([p (vector-ref spf temp)])\n                    (when\
        \ (vector-ref is-prime-in-nums p)\n                      (vector-set! prime-to-indices\
        \ p (cons i (vector-ref prime-to-indices p))))\n                    (let inner-loop\
        \ ([curr temp])\n                      (if (and (> curr 1) (= (remainder curr\
        \ p) 0))\n                          (inner-loop (quotient curr p))\n       \
        \                   (loop curr))))))))\n\n          (define dist (make-vector\
        \ n -1))\n          (define prime-visited (make-vector (+ max-val 1) #f))\n\
        \          (vector-set! dist 0 0)\n\n          (let bfs ([q-front '(0)] [q-back\
        \ '()])\n            (cond\n              [(and (null? q-front) (null? q-back))\
        \ -1]\n              [(null? q-front) (bfs (reverse q-back) '())]\n        \
        \      [else\n               (let* ([u (car q-front)]\n                    \
        \  [rest-front (cdr q-front)])\n                 (if (= u (- n 1))\n       \
        \              (vector-ref dist u)\n                     (let* ([d-u (vector-ref\
        \ dist u)]\n                            [d-next (+ d-u 1)]\n               \
        \             [val (vector-ref nums-vec u)]\n                            [is-u-prime\
        \ (and (>= val 2) (= (vector-ref spf val) val))]\n                         \
        \   [new-back q-back])\n                       (let* ([after-adj (for/fold ([curr-back\
        \ new-back])\n                                                  ([v (list (+\
        \ u 1) (- u 1))])\n                                           (if (and (>= v\
        \ 0) (< v n) (= (vector-ref dist v) -1))\n                                 \
        \              (begin\n                                                 (vector-set!\
        \ dist v d-next)\n                                                 (cons v curr-back))\n\
        \                                               curr-back))]\n             \
        \                 [after-tele (if (and is-u-prime (not (vector-ref prime-visited\
        \ val)))\n                                              (begin\n           \
        \                                     (vector-set! prime-visited val #t)\n \
        \                                               (for/fold ([curr-back after-adj])\n\
        \                                                          ([v (vector-ref prime-to-indices\
        \ val)])\n                                                  (if (= (vector-ref\
        \ dist v) -1)\n                                                      (begin\n\
        \                                                        (vector-set! dist v\
        \ d-next)\n                                                        (cons v curr-back))\n\
        \                                                      curr-back)))\n      \
        \                                        after-adj)])\n                    \
        \     (bfs rest-front after-tele))))]))))))"
      erlang: "-spec min_jumps(Nums :: [integer()]) -> integer().\nmin_jumps(Nums) ->\n\
        \  N = length(Nums),\n  if N == 1 -> 0;\n     true -> solve(Nums, N)\n  end.\n\
        \nsolve(Nums, N) ->\n  NumsVec = array:from_list(Nums),\n  MaxVal = lists:max(Nums),\n\
        \  SPF = ets:new(spf, [set, public]),\n  [ets:insert(SPF, {I, I}) || I <- lists:seq(2,\
        \ MaxVal)],\n  SqrtMax = round(math:sqrt(MaxVal)),\n  lists:foreach(fun(I) ->\n\
        \    case ets:lookup(SPF, I) of\n      [{I, I}] -> sieve_fill(I * I, I, MaxVal,\
        \ SPF);\n      _ -> ok\n    end\n  end, lists:seq(2, SqrtMax)),\n  IsPrimeInNums\
        \ = ets:new(is_prime_in_nums, [set, public]),\n  lists:foreach(fun(X) ->\n \
        \   case ets:lookup(SPF, X) of\n      [{X, X}] -> ets:insert(IsPrimeInNums,\
        \ {X});\n      _ -> ok\n    end\n  end, Nums),\n  PrimeToIndices = ets:new(prime_to_indices,\
        \ [bag, public]),\n  lists:foreach(fun(I) ->\n    Val = array:get(I, NumsVec),\n\
        \    Factors = get_distinct_prime_factors(Val, SPF),\n    lists:foreach(fun(P)\
        \ ->\n      case ets:member(IsPrimeInNums, P) of\n        true -> ets:insert(PrimeToIndices,\
        \ {P, I});\n        false -> ok\n      end\n    end, Factors)\n  end, lists:seq(0,\
        \ N - 1)),\n  Dist = ets:new(dist, [set, public]),\n  ets:insert(Dist, {0, 0}),\n\
        \  PrimeVisited = ets:new(prime_visited, [set, public]),\n  Queue = queue:from_list([0]),\n\
        \  bfs(Queue, NumsVec, N, SPF, PrimeToIndices, Dist, PrimeVisited).\n\nsieve_fill(J,\
        \ I, MaxVal, SPF) when J =< MaxVal ->\n  case ets:lookup(SPF, J) of\n    [{J,\
        \ J}] -> ets:insert(SPF, {J, I});\n    _ -> ok\n  end,\n  sieve_fill(J + I,\
        \ I, MaxVal, SPF);\nsieve_fill(_, _, _, _) -> ok.\n\nget_distinct_prime_factors(1,\
        \ _) -> [];\nget_distinct_prime_factors(Val, SPF) ->\n  [{Val, P}] = ets:lookup(SPF,\
        \ Val),\n  NewVal = div_repeat(Val, P),\n  [P | get_distinct_prime_factors(NewVal,\
        \ SPF)].\n\ndiv_repeat(Val, P) when Val rem P == 0 -> div_repeat(Val div P,\
        \ P);\ndiv_repeat(Val, _) -> Val.\n\nbfs(Queue, NumsVec, N, SPF, PrimeToIndices,\
        \ Dist, PrimeVisited) ->\n  case queue:out(Queue) of\n    {empty, _} -> -1;\n\
        \    {{value, U}, Q2} ->\n      [{U, DU}] = ets:lookup(Dist, U),\n      if U\
        \ == N - 1 -> DU;\n         true ->\n           {Q3, _} = lists:foldl(fun(V,\
        \ {Qi, Di}) ->\n             if V >= 0, V < N ->\n               case ets:member(Di,\
        \ V) of\n                 false -> ets:insert(Di, {V, DU + 1}), {queue:in(V,\
        \ Qi), Di};\n                 true -> {Qi, Di}\n               end;\n      \
        \         true -> {Qi, Di}\n             end\n           end, {Q2, Dist}, [U\
        \ - 1, U + 1]),\n           Val = array:get(U, NumsVec),\n           IsPrime\
        \ = case ets:lookup(SPF, Val) of [{Val, Val}] -> true; _ -> false end,\n   \
        \        Q4 = if IsPrime ->\n                    case ets:member(PrimeVisited,\
        \ Val) of\n                      false ->\n                        ets:insert(PrimeVisited,\
        \ {Val}),\n                        Indices = ets:lookup(PrimeToIndices, Val),\n\
        \                        lists:foldl(fun({_, V}, Qi2) ->\n                 \
        \         case ets:member(Dist, V) of\n                            false ->\
        \ ets:insert(Dist, {V, DU + 1}), queue:in(V, Qi2);\n                       \
        \     true -> Qi2\n                          end\n                        end,\
        \ Q3, Indices);\n                      true -> Q3\n                    end;\n\
        \                    true -> Q3\n                 end,\n           bfs(Q4, NumsVec,\
        \ N, SPF, PrimeToIndices, Dist, PrimeVisited)\n      end\n  end."
      elixir: "defmodule Solution do\n  @spec min_jumps(nums :: [integer]) :: integer\n\
        \  def min_jumps(nums) do\n    n = length(nums)\n    if n == 1 do\n      0\n\
        \    else\n      solve(nums, n)\n    end\n  end\n\n  defp solve(nums, n) do\n\
        \    nums_vec = :array.from_list(nums)\n    max_val = Enum.max(nums)\n    spf\
        \ = :ets.new(:spf, [:set, :public])\n    for i <- 2..max_val, do: :ets.insert(spf,\
        \ {i, i})\n\n    sqrt_max = round(:math.sqrt(max_val))\n    for i <- 2..sqrt_max\
        \ do\n      case :ets.lookup(spf, i) do\n        [{^i, ^i}] -> sieve_fill(i\
        \ * i, i, max_val, spf)\n        _ -> :ok\n      end\n    end\n\n    is_prime_in_nums\
        \ = :ets.new(:is_prime_in_nums, [:set, :public])\n    for x <- nums do\n   \
        \   case :ets.lookup(spf, x) do\n        [{^x, ^x}] -> :ets.insert(is_prime_in_nums,\
        \ {x})\n        _ -> :ok\n      end\n    end\n\n    prime_to_indices = :ets.new(:prime_to_indices,\
        \ [:bag, :public])\n    for i <- 0..(n - 1) do\n      val = :array.get(i, nums_vec)\n\
        \      factors = get_distinct_factors(val, spf)\n      for p <- factors do\n\
        \        if :ets.member(is_prime_in_nums, p) do\n          :ets.insert(prime_to_indices,\
        \ {p, i})\n        end\n      end\n    end\n\n    dist = :ets.new(:dist, [:set,\
        \ :public])\n    :ets.insert(dist, {0, 0})\n    prime_visited = :ets.new(:prime_visited,\
        \ [:set, :public])\n    queue = :queue.from_list([0])\n    bfs(queue, nums_vec,\
        \ n, spf, prime_to_indices, dist, prime_visited)\n  end\n\n  defp sieve_fill(j,\
        \ i, max_val, spf) when j <= max_val do\n    case :ets.lookup(spf, j) do\n \
        \     [{^j, ^j}] -> :ets.insert(spf, {j, i})\n      _ -> :ok\n    end\n    sieve_fill(j\
        \ + i, i, max_val, spf)\n  end\n  defp sieve_fill(_, _, _, _), do: :ok\n\n \
        \ defp get_distinct_factors(1, _), do: []\n  defp get_distinct_factors(val,\
        \ spf) do\n    [{^val, p}] = :ets.lookup(spf, val)\n    new_val = div_repeat(val,\
        \ p)\n    [p | get_distinct_factors(new_val, spf)]\n  end\n\n  defp div_repeat(val,\
        \ p) when rem(val, p) == 0, do: div_repeat(div(val, p), p)\n  defp div_repeat(val,\
        \ _), do: val\n\n  defp bfs(queue, nums_vec, n, spf, prime_to_indices, dist,\
        \ prime_visited) do\n    case :queue.out(queue) do\n      {:empty, _} -> -1\n\
        \      {{:value, u}, queue2} ->\n        [{^u, d_u}] = :ets.lookup(dist, u)\n\
        \        if u == n - 1 do\n          d_u\n        else\n          queue3 = Enum.reduce([u\
        \ - 1, u + 1], queue2, fn v, q ->\n            if v >= 0 and v < n and not :ets.member(dist,\
        \ v) do\n              :ets.insert(dist, {v, d_u + 1})\n              :queue.in(v,\
        \ q)\n            else\n              q\n            end\n          end)\n\n\
        \          val = :array.get(u, nums_vec)\n          is_prime = case :ets.lookup(spf,\
        \ val) do [{^val, ^val}] -> true; _ -> false end\n          queue4 = if is_prime\
        \ and not :ets.member(prime_visited, val) do\n            :ets.insert(prime_visited,\
        \ {val})\n            indices = :ets.lookup(prime_to_indices, val)\n       \
        \     Enum.reduce(indices, queue3, fn {_, v}, q ->\n              if not :ets.member(dist,\
        \ v) do\n                :ets.insert(dist, {v, d_u + 1})\n                :queue.in(v,\
        \ q)\n              else\n                q\n              end\n           \
        \ end)\n          else\n            queue3\n          end\n          bfs(queue4,\
        \ nums_vec, n, spf, prime_to_indices, dist, prime_visited)\n        end\n  \
        \  end\n  end\nend"
    approach: 'The problem asks for the minimum number of jumps to reach the end of
      an array, suggesting a Breadth-First Search (BFS) approach. We treat each index
      as a node in a graph. There are two types of edges: adjacent edges between $i$
      and $i \pm 1$, and teleportation edges from index $i$ to index $j$ if $nums[i]$
      is a prime $p$ and $nums[j]$ is a multiple of $p$. To handle teleportation efficiently,
      we precompute the unique prime factors of every number in $nums$ using a Sieve
      of Eratosthenes to build ''buckets'' where $bucket[p]$ contains all indices $j$
      such that $nums[j]$ is a multiple of $p$.'
    time_complexity: O(M \log \log M + N \log M) where $M$ is the maximum value in $nums$
      ($10^6$) and $N$ is the length of the array ($10^5$). The sieve takes $O(M \log
      \log M)$, and factoring each $nums[j]$ takes at most $O(\log M)$ time (roughly
      7 unique prime factors). BFS visits each node and each prime factor bucket exactly
      once, ensuring efficient traversal within time limits.
    space_complexity: O(M + N \log M) for storing the sieve's smallest prime factor
      array, the prime buckets (CSR format or list of lists), the BFS distance array,
      and the BFS queue.
    elapsed_time: 361.9068925380707
    model: gemini-3-flash-preview
    generated_at: '2026-05-08 02:31:24 '
---

## Problem #3629: Minimum Jumps to Reach End via Prime Teleportation

**Difficulty:** Medium

**Topics:** Array, Hash Table, Math, Breadth-First Search, Number Theory

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code>.</p>

<p>You start at index 0, and your goal is to reach index <code>n - 1</code>.</p>

<p>From any index <code>i</code>, you may perform one of the following operations:</p>

<ul>
	<li><strong>Adjacent Step</strong>: Jump to index <code>i + 1</code> or <code>i - 1</code>, if the index is within bounds.</li>
	<li><strong>Prime Teleportation</strong>: If <code>nums[i]</code> is a <span data-keyword="prime-number">prime number</span> <code>p</code>, you may instantly jump to any index <code>j != i</code> such that <code>nums[j] % p == 0</code>.</li>
</ul>

<p>Return the <strong>minimum</strong> number of jumps required to reach index <code>n - 1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,4,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal sequence of jumps is:</p>

<ul>
	<li>Start at index <code>i = 0</code>. Take an adjacent step to index 1.</li>
	<li>At index <code>i = 1</code>, <code>nums[1] = 2</code> is a prime number. Therefore, we teleport to index <code>i = 3</code> as <code>nums[3] = 6</code> is divisible by 2.</li>
</ul>

<p>Thus, the answer is 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,4,7,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal sequence of jumps is:</p>

<ul>
	<li>Start at index <code>i = 0</code>. Take an adjacent step to index <code>i = 1</code>.</li>
	<li>At index <code>i = 1</code>, <code>nums[1] = 3</code> is a prime number. Therefore, we teleport to index <code>i = 4</code> since <code>nums[4] = 9</code> is divisible by 3.</li>
</ul>

<p>Thus, the answer is 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,6,5,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Since no teleportation is possible, we move through <code>0 &rarr; 1 &rarr; 2 &rarr; 3</code>. Thus, the answer is 3.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Use a breadth-first search.

2. Precompute prime factors of each `nums[i]` via a sieve, and build a bucket `bucket[p]` mapping each prime `p` to all indices `j` with `nums[j] % p == 0`.

3. During the BFS, when at index `i`, enqueue its adjacent steps (`i+1` and `i-1`) and all indices in `bucket[p]` for each prime `p` dividing `nums[i]`, then clear `bucket[p]` so each prime's bucket is visited only once.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the minimum number of jumps to reach the end of an array, suggesting a Breadth-First Search (BFS) approach. We treat each index as a node in a graph. There are two types of edges: adjacent edges between $i$ and $i \pm 1$, and teleportation edges from index $i$ to index $j$ if $nums[i]$ is a prime $p$ and $nums[j]$ is a multiple of $p$. To handle teleportation efficiently, we precompute the unique prime factors of every number in $nums$ using a Sieve of Eratosthenes to build 'buckets' where $bucket[p]$ contains all indices $j$ such that $nums[j]$ is a multiple of $p$.

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
    int minJumps(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        int maxVal = 0;
        for (int x : nums) if (x > maxVal) maxVal = x;

        vector<int> spf(maxVal + 1);
        for (int i = 0; i <= maxVal; ++i) spf[i] = i;
        for (int i = 2; i * i <= maxVal; ++i) {
            if (spf[i] == i) {
                for (int j = i * i; j <= maxVal; j += i)
                    if (spf[j] == j) spf[j] = i;
            }
        }

        vector<bool> isPrime(maxVal + 1, false);
        for (int i = 2; i <= maxVal; ++i) if (spf[i] == i) isPrime[i] = true;

        vector<int> primeCount(maxVal + 1, 0);
        int totalPairs = 0;
        for (int x : nums) {
            int temp = x;
            while (temp > 1) {
                int p = spf[temp];
                primeCount[p]++;
                totalPairs++;
                while (temp % p == 0) temp /= p;
            }
        }

        vector<int> primeOffset(maxVal + 2, 0);
        for (int i = 0; i <= maxVal; ++i) primeOffset[i + 1] = primeOffset[i] + primeCount[i];

        vector<int> flatBuckets(totalPairs);
        vector<int> currentOffset = primeOffset;
        for (int i = 0; i < n; ++i) {
            int temp = nums[i];
            while (temp > 1) {
                int p = spf[temp];
                flatBuckets[currentOffset[p]++] = i;
                while (temp % p == 0) temp /= p;
            }
        }

        vector<int> dist(n, -1);
        vector<bool> primeUsed(maxVal + 1, false);
        queue<int> q;

        dist[0] = 0;
        q.push(0);

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            if (u == n - 1) return dist[u];

            for (int v : {u - 1, u + 1}) {
                if (v >= 0 && v < n && dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    if (v == n - 1) return dist[v];
                    q.push(v);
                }
            }

            int p = nums[u];
            if (p <= maxVal && isPrime[p] && !primeUsed[p]) {
                for (int k = primeOffset[p]; k < primeOffset[p + 1]; ++k) {
                    int v = flatBuckets[k];
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        if (v == n - 1) return dist[v];
                        q.push(v);
                    }
                }
                primeUsed[p] = true;
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
    public int minJumps(int[] nums) {
        int n = nums.length;
        if (n <= 1) return 0;
        int maxVal = 0;
        for (int x : nums) if (x > maxVal) maxVal = x;

        int[] spf = new int[maxVal + 1];
        for (int i = 0; i <= maxVal; i++) spf[i] = i;
        for (int i = 2; i * i <= maxVal; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= maxVal; j += i)
                    if (spf[j] == j) spf[j] = i;
            }
        }

        boolean[] isPrime = new boolean[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) if (spf[i] == i) isPrime[i] = true;

        int[] primeCount = new int[maxVal + 1];
        int totalPairs = 0;
        for (int x : nums) {
            int temp = x;
            while (temp > 1) {
                int p = spf[temp];
                primeCount[p]++;
                totalPairs++;
                while (temp % p == 0) temp /= p;
            }
        }

        int[] primeOffset = new int[maxVal + 2];
        for (int i = 0; i <= maxVal; i++) primeOffset[i + 1] = primeOffset[i] + primeCount[i];

        int[] flatBuckets = new int[totalPairs];
        int[] currentOffset = primeOffset.clone();
        for (int i = 0; i < n; i++) {
            int temp = nums[i];
            while (temp > 1) {
                int p = spf[temp];
                flatBuckets[currentOffset[p]++] = i;
                while (temp % p == 0) temp /= p;
            }
        }

        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        boolean[] primeUsed = new boolean[maxVal + 1];
        Deque<Integer> q = new ArrayDeque<>();

        dist[0] = 0;
        q.offer(0);

        while (!q.isEmpty()) {
            int u = q.poll();
            if (u == n - 1) return dist[u];

            int[] neighbors = {u - 1, u + 1};
            for (int v : neighbors) {
                if (v >= 0 && v < n && dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    if (v == n - 1) return dist[v];
                    q.offer(v);
                }
            }

            int p = nums[u];
            if (p <= maxVal && isPrime[p] && !primeUsed[p]) {
                for (int k = primeOffset[p]; k < primeOffset[p + 1]; k++) {
                    int v = flatBuckets[k];
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        if (v == n - 1) return dist[v];
                        q.offer(v);
                    }
                }
                primeUsed[p] = true;
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
import collections

class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1: return 0
        max_val = max(nums)

        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, max_val + 1, i):
                    if spf[j] == j: spf[j] = i

        is_prime = [False] * (max_val + 1)
        for i in range(2, max_val + 1): 
            if spf[i] == i: is_prime[i] = True

        buckets = collections.defaultdict(list)
        for i, x in enumerate(nums):
            temp = x
            while temp > 1:
                p = spf[temp]
                buckets[p].append(i)
                while temp % p == 0: temp //= p

        q = collections.deque([0])
        dist = [-1] * n
        dist[0] = 0
        prime_used = [False] * (max_val + 1)

        while q:
            u = q.popleft()
            if u == n - 1: return dist[u]

            for v in [u - 1, u + 1]:
                if 0 <= v < n and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    if v == n - 1: return dist[v]
                    q.append(v)

            p = nums[u]
            if p <= max_val and is_prime[p] and not prime_used[p]:
                for v in buckets[p]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        if v == n - 1: return dist[v]
                        q.append(v)
                prime_used[p] = True
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        max_val = max(nums)

        spf = list(range(max_val + 1))
        for i in range(2, int(max_val**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, max_val + 1, i):
                    if spf[j] == j: spf[j] = i

        is_prime = [False] * (max_val + 1)
        for i in range(2, max_val + 1):
            if spf[i] == i: is_prime[i] = True

        buckets = collections.defaultdict(list)
        for i, x in enumerate(nums):
            temp = x
            while temp > 1:
                p = spf[temp]
                buckets[p].append(i)
                while temp % p == 0: temp //= p

        q = collections.deque([0])
        dist = [-1] * n
        dist[0] = 0
        prime_used = [False] * (max_val + 1)

        while q:
            u = q.popleft()
            if u == n - 1: return dist[u]

            for v in [u - 1, u + 1]:
                if 0 <= v < n and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    if v == n - 1: return dist[v]
                    q.append(v)

            p = nums[u]
            if p <= max_val and is_prime[p] and not prime_used[p]:
                for v in buckets[p]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        if v == n - 1: return dist[v]
                        q.append(v)
                prime_used[p] = True
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int minJumps(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;
    int maxVal = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxVal) maxVal = nums[i];

    int* spf = (int*)malloc((maxVal + 1) * sizeof(int));
    for (int i = 0; i <= maxVal; i++) spf[i] = i;
    for (int i = 2; i * i <= maxVal; i++) {
        if (spf[i] == i) {
            for (int j = i * i; j <= maxVal; j += i)
                if (spf[j] == j) spf[j] = i;
        }
    }

    bool* isPrime = (bool*)calloc((maxVal + 1), sizeof(bool));
    for (int i = 2; i <= maxVal; i++) if (spf[i] == i) isPrime[i] = true;

    int* primeCount = (int*)calloc((maxVal + 1), sizeof(int));
    int totalPairs = 0;
    for (int i = 0; i < numsSize; i++) {
        int temp = nums[i];
        while (temp > 1) {
            int p = spf[temp];
            primeCount[p]++;
            totalPairs++;
            while (temp % p == 0) temp /= p;
        }
    }

    int* primeOffset = (int*)malloc((maxVal + 2) * sizeof(int));
    primeOffset[0] = 0;
    for (int i = 0; i <= maxVal; i++) primeOffset[i + 1] = primeOffset[i] + primeCount[i];

    int* flatBuckets = (int*)malloc(totalPairs * sizeof(int));
    int* currentOffset = (int*)malloc((maxVal + 1) * sizeof(int));
    memcpy(currentOffset, primeOffset, (maxVal + 1) * sizeof(int));

    for (int i = 0; i < numsSize; i++) {
        int temp = nums[i];
        while (temp > 1) {
            int p = spf[temp];
            flatBuckets[currentOffset[p]++] = i;
            while (temp % p == 0) temp /= p;
        }
    }

    int* dist = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) dist[i] = -1;
    int* queue = (int*)malloc(numsSize * sizeof(int));
    bool* primeUsed = (bool*)calloc((maxVal + 1), sizeof(bool));

    int head = 0, tail = 0;
    dist[0] = 0;
    queue[tail++] = 0;

    int ans = -1;
    while (head < tail) {
        int u = queue[head++];
        if (u == numsSize - 1) { ans = dist[u]; break; }

        int neighbors[2] = {u - 1, u + 1};
        for (int k = 0; k < 2; k++) {
            int v = neighbors[k];
            if (v >= 0 && v < numsSize && dist[v] == -1) {
                dist[v] = dist[u] + 1;
                if (v == numsSize - 1) { ans = dist[v]; goto end_bfs; }
                queue[tail++] = v;
            }
        }

        int p = nums[u];
        if (p <= maxVal && isPrime[p] && !primeUsed[p]) {
            for (int k = primeOffset[p]; k < primeOffset[p + 1]; k++) {
                int v = flatBuckets[k];
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    if (v == numsSize - 1) { ans = dist[v]; goto end_bfs; }
                    queue[tail++] = v;
                }
            }
            primeUsed[p] = true;
        }
    }

end_bfs:
    free(spf); free(isPrime); free(primeCount); free(primeOffset); 
    free(flatBuckets); free(currentOffset); free(dist); free(queue); free(primeUsed);
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

public class Solution {
    public int MinJumps(int[] nums) {
        int n = nums.Length;
        if (n <= 1) return 0;

        int maxVal = 0;
        foreach (int num in nums) {
            if (num > maxVal) maxVal = num;
        }

        int[] minPrime = new int[maxVal + 1];
        for (int i = 2; i * i <= maxVal; i++) {
            if (minPrime[i] == 0) {
                for (int j = i * i; j <= maxVal; j += i) {
                    if (minPrime[j] == 0) minPrime[j] = i;
                }
            }
        }
        for (int i = 2; i <= maxVal; i++) {
            if (minPrime[i] == 0) minPrime[i] = i;
        }

        List<int>[] primeToIndices = new List<int>[maxVal + 1];
        for (int i = 0; i < n; i++) {
            int temp = nums[i];
            while (temp > 1) {
                int p = minPrime[temp];
                if (primeToIndices[p] == null) primeToIndices[p] = new List<int>();
                primeToIndices[p].Add(i);
                while (temp % p == 0) temp /= p;
            }
        }

        Queue<int> queue = new Queue<int>();
        bool[] visited = new bool[n];
        queue.Enqueue(0);
        visited[0] = true;
        int steps = 0;

        while (queue.Count > 0) {
            int size = queue.Count;
            while (size-- > 0) {
                int i = queue.Dequeue();
                if (i == n - 1) return steps;

                if (i + 1 < n && !visited[i + 1]) {
                    visited[i + 1] = true;
                    queue.Enqueue(i + 1);
                }
                if (i - 1 >= 0 && !visited[i - 1]) {
                    visited[i - 1] = true;
                    queue.Enqueue(i - 1);
                }

                int p = nums[i];
                if (p > 1 && p <= maxVal && minPrime[p] == p) {
                    if (primeToIndices[p] != null) {
                        foreach (int j in primeToIndices[p]) {
                            if (!visited[j]) {
                                visited[j] = true;
                                queue.Enqueue(j);
                            }
                        }
                        primeToIndices[p] = null;
                    }
                }
            }
            steps++;
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
 * @param {number[]} nums
 * @return {number}
 */
var minJumps = function(nums) {
    const n = nums.length;
    if (n <= 1) return 0;

    let maxVal = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    const minPrime = new Int32Array(maxVal + 1);
    for (let i = 2; i * i <= maxVal; i++) {
        if (minPrime[i] === 0) {
            for (let j = i * i; j <= maxVal; j += i) {
                if (minPrime[j] === 0) minPrime[j] = i;
            }
        }
    }
    for (let i = 2; i <= maxVal; i++) {
        if (minPrime[i] === 0) minPrime[i] = i;
    }

    const primeToIndices = new Array(maxVal + 1);
    for (let i = 0; i < n; i++) {
        let temp = nums[i];
        while (temp > 1) {
            let p = minPrime[temp];
            if (!primeToIndices[p]) primeToIndices[p] = [];
            primeToIndices[p].push(i);
            while (temp % p === 0) temp /= p;
        }
    }

    const queue = [0];
    const visited = new Uint8Array(n);
    visited[0] = 1;
    let steps = 0;
    let head = 0;

    while (head < queue.length) {
        let size = queue.length - head;
        while (size-- > 0) {
            const i = queue[head++];
            if (i === n - 1) return steps;

            if (i + 1 < n && !visited[i + 1]) {
                visited[i + 1] = 1;
                queue.push(i + 1);
            }
            if (i - 1 >= 0 && !visited[i - 1]) {
                visited[i - 1] = 1;
                queue.push(i - 1);
            }

            const p = nums[i];
            if (p > 1 && p <= maxVal && minPrime[p] === p) {
                if (primeToIndices[p]) {
                    const indices = primeToIndices[p];
                    for (let k = 0; k < indices.length; k++) {
                        const j = indices[k];
                        if (!visited[j]) {
                            visited[j] = 1;
                            queue.push(j);
                        }
                    }
                    primeToIndices[p] = null;
                }
            }
        }
        steps++;
    }

    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minJumps(nums: number[]): number {
    const n = nums.length;
    if (n <= 1) return 0;

    let maxVal = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    const minPrime = new Int32Array(maxVal + 1);
    for (let i = 2; i * i <= maxVal; i++) {
        if (minPrime[i] === 0) {
            for (let j = i * i; j <= maxVal; j += i) {
                if (minPrime[j] === 0) minPrime[j] = i;
            }
        }
    }
    for (let i = 2; i <= maxVal; i++) {
        if (minPrime[i] === 0) minPrime[i] = i;
    }

    const primeToIndices: (number[] | null)[] = new Array(maxVal + 1).fill(null);
    for (let i = 0; i < n; i++) {
        let temp = nums[i];
        while (temp > 1) {
            let p = minPrime[temp];
            if (!primeToIndices[p]) primeToIndices[p] = [];
            primeToIndices[p]!.push(i);
            while (temp % p === 0) temp /= p;
        }
    }

    const queue: number[] = [0];
    const visited = new Uint8Array(n);
    visited[0] = 1;
    let steps = 0;
    let head = 0;

    while (head < queue.length) {
        let size = queue.length - head;
        while (size-- > 0) {
            const i = queue[head++];
            if (i === n - 1) return steps;

            if (i + 1 < n && !visited[i + 1]) {
                visited[i + 1] = 1;
                queue.push(i + 1);
            }
            if (i - 1 >= 0 && !visited[i - 1]) {
                visited[i - 1] = 1;
                queue.push(i - 1);
            }

            const p = nums[i];
            if (p > 1 && p <= maxVal && minPrime[p] === p) {
                const indices = primeToIndices[p];
                if (indices) {
                    for (let k = 0; k < indices.length; k++) {
                        const j = indices[k];
                        if (!visited[j]) {
                            visited[j] = 1;
                            queue.push(j);
                        }
                    }
                    primeToIndices[p] = null;
                }
            }
        }
        steps++;
    }

    return -1;
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
    function minJumps($nums) {
        $n = count($nums);
        if ($n <= 1) return 0;

        $maxVal = 0;
        foreach ($nums as $num) {
            if ($num > $maxVal) $maxVal = $num;
        }

        $minPrime = new SplFixedArray($maxVal + 1);
        for ($i = 0; $i <= $maxVal; $i++) $minPrime[$i] = 0;

        for ($i = 2; $i * $i <= $maxVal; $i++) {
            if ($minPrime[$i] === 0) {
                for ($j = $i * $i; $j <= $maxVal; $j += $i) {
                    if ($minPrime[$j] === 0) $minPrime[$j] = $i;
                }
            }
        }
        for ($i = 2; $i <= $maxVal; $i++) {
            if ($minPrime[$i] === 0) $minPrime[$i] = $i;
        }

        $primeToIndices = [];
        for ($i = 0; $i < $n; $i++) {
            $temp = $nums[$i];
            while ($temp > 1) {
                $p = $minPrime[$temp];
                if (!isset($primeToIndices[$p])) $primeToIndices[$p] = [];
                $primeToIndices[$p][] = $i;
                while ($temp % $p === 0) $temp /= $p;
            }
        }

        $queue = new SplQueue();
        $visited = new SplFixedArray($n);
        for ($i = 0; $i < $n; $i++) $visited[$i] = false;
        $queue->enqueue(0);
        $visited[0] = true;
        $steps = 0;

        while (!$queue->isEmpty()) {
            $size = $queue->count();
            while ($size-- > 0) {
                $i = $queue->dequeue();
                if ($i === $n - 1) return $steps;

                if ($i + 1 < $n && !$visited[$i + 1]) {
                    $visited[$i + 1] = true;
                    $queue->enqueue($i + 1);
                }
                if ($i - 1 >= 0 && !$visited[$i - 1]) {
                    $visited[$i - 1] = true;
                    $queue->enqueue($i - 1);
                }

                $p = $nums[$i];
                if ($p > 1 && $p <= $maxVal && $minPrime[$p] === $p) {
                    if (isset($primeToIndices[$p])) {
                        foreach ($primeToIndices[$p] as $j) {
                            if (!$visited[$j]) {
                                $visited[$j] = true;
                                $queue->enqueue($j);
                            }
                        }
                        unset($primeToIndices[$p]);
                    }
                }
            }
            $steps++;
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
    func minJumps(_ nums: [Int]) -> Int {
        let n = nums.count
        if n <= 1 { return 0 }

        var maxVal = 0
        for num in nums {
            if num > maxVal { maxVal = num }
        }

        var minPrime = [Int](repeating: 0, count: maxVal + 1)
        if maxVal >= 2 {
            let limit = Int(Double(maxVal).squareRoot())
            for i in 2...limit {
                if minPrime[i] == 0 {
                    for j in stride(from: i * i, through: maxVal, by: i) {
                        if minPrime[j] == 0 { minPrime[j] = i }
                    }
                }
            }
            for i in 2...maxVal {
                if minPrime[i] == 0 { minPrime[i] = i }
            }
        }

        var primeToIndices = [Int: [Int]]()
        for i in 0..<n {
            var temp = nums[i]
            while temp > 1 {
                let p = minPrime[temp]
                if primeToIndices[p] == nil {
                    primeToIndices[p] = [i]
                } else {
                    primeToIndices[p]!.append(i)
                }
                while temp % p == 0 {
                    temp /= p
                }
            }
        }

        var visited = [Bool](repeating: false, count: n)
        var queue = [Int]()
        queue.append(0)
        visited[0] = true
        var steps = 0
        var head = 0

        while head < queue.count {
            let size = queue.count - head
            for _ in 0..<size {
                let i = queue[head]
                head += 1

                if i == n - 1 { return steps }

                if i + 1 < n && !visited[i + 1] {
                    visited[i + 1] = true
                    queue.append(i + 1)
                }
                if i - 1 >= 0 && !visited[i - 1] {
                    visited[i - 1] = true
                    queue.append(i - 1)
                }

                let p = nums[i]
                if p > 1 && p <= maxVal && minPrime[p] == p {
                    if let indices = primeToIndices[p] {
                        for j in indices {
                            if !visited[j] {
                                visited[j] = true
                                queue.append(j)
                            }
                        }
                        primeToIndices[p] = nil
                    }
                }
            }
            steps += 1
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
import java.util.ArrayDeque

class Solution {
    fun minJumps(nums: IntArray): Int {
        val n = nums.size
        if (n == 1) return 0

        val maxVal = 1000000
        val spf = IntArray(maxVal + 1) { it }
        var i = 2
        while (i * i <= maxVal) {
            if (spf[i] == i) {
                var j = i * i
                while (j <= maxVal) {
                    if (spf[j] == j) spf[j] = i
                    j += i
                }
            }
            i++
        }

        val existsAsPrime = BooleanArray(maxVal + 1)
        for (x in nums) {
            if (x > 1 && spf[x] == x) existsAsPrime[x] = true
        }

        val buckets = arrayOfNulls<MutableList<Int>>(maxVal + 1)
        for (idx in 0 until n) {
            var x = nums[idx]
            while (x > 1) {
                val p = spf[x]
                if (existsAsPrime[p]) {
                    if (buckets[p] == null) buckets[p] = mutableListOf<Int>()
                    buckets[p]!!.add(idx)
                }
                while (x % p == 0) x /= p
            }
        }

        val dist = IntArray(n) { -1 }
        val queue = ArrayDeque<Int>()
        val visitedPrimes = BooleanArray(maxVal + 1)

        dist[0] = 0
        queue.add(0)

        while (queue.isNotEmpty()) {
            val u = queue.removeFirst()
            if (u == n - 1) return dist[u]

            val neighbors = intArrayOf(u - 1, u + 1)
            for (v in neighbors) {
                if (v in 0 until n && dist[v] == -1) {
                    dist[v] = dist[u] + 1
                    queue.add(v)
                }
            }

            val p = nums[u]
            if (p > 1 && spf[p] == p && !visitedPrimes[p]) {
                visitedPrimes[p] = true
                buckets[p]?.let { list ->
                    for (v in list) {
                        if (dist[v] == -1) {
                            dist[v] = dist[u] + 1
                            queue.add(v)
                        }
                    }
                }
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
import 'dart:typed_data';

class Solution {
  int minJumps(List<int> nums) {
    int n = nums.length;
    if (n == 1) return 0;

    const int maxVal = 1000000;
    Int32List spf = Int32List(maxVal + 1);
    for (int i = 0; i <= maxVal; i++) spf[i] = i;

    for (int i = 2; i * i <= maxVal; i++) {
      if (spf[i] == i) {
        for (int j = i * i; j <= maxVal; j += i) {
          if (spf[j] == j) spf[j] = i;
        }
      }
    }

    Uint8List existsAsPrime = Uint8List(maxVal + 1);
    for (int x in nums) {
      if (x > 1 && spf[x] == x) existsAsPrime[x] = 1;
    }

    List<List<int>?> buckets = List<List<int>?>.filled(maxVal + 1, null);
    for (int i = 0; i < n; i++) {
      int x = nums[i];
      while (x > 1) {
        int p = spf[x];
        if (existsAsPrime[p] == 1) {
          if (buckets[p] == null) buckets[p] = [];
          buckets[p]!.add(i);
        }
        while (x % p == 0) x ~/= p;
      }
    }

    Int32List dist = Int32List(n)..fillRange(0, n, -1);
    Uint8List visitedPrimes = Uint8List(maxVal + 1);
    Queue<int> queue = Queue<int>();

    dist[0] = 0;
    queue.add(0);

    while (queue.isNotEmpty) {
      int u = queue.removeFirst();
      if (u == n - 1) return dist[u];

      List<int> neighbors = [u - 1, u + 1];
      for (int v in neighbors) {
        if (v >= 0 && v < n && dist[v] == -1) {
          dist[v] = dist[u] + 1;
          queue.add(v);
        }
      }

      int p = nums[u];
      if (p > 1 && spf[p] == p && visitedPrimes[p] == 0) {
        visitedPrimes[p] = 1;
        List<int>? bucket = buckets[p];
        if (bucket != null) {
          for (int v in bucket) {
            if (dist[v] == -1) {
              dist[v] = dist[u] + 1;
              queue.add(v);
            }
          }
        }
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
func minJumps(nums []int) int {
    n := len(nums)
    if n == 1 {
        return 0
    }

    const maxVal = 1000000
    spf := make([]int32, maxVal+1)
    for i := 0; i <= maxVal; i++ {
        spf[i] = int32(i)
    }

    for i := 2; i*i <= maxVal; i++ {
        if spf[i] == int32(i) {
            for j := i * i; j <= maxVal; j += i {
                if spf[j] == int32(j) {
                    spf[j] = int32(i)
                }
            }
        }
    }

    existsAsPrime := make([]bool, maxVal+1)
    for _, x := range nums {
        if x > 1 && int(spf[x]) == x {
            existsAsPrime[x] = true
        }
    }

    buckets := make([][]int, maxVal+1)
    for i := 0; i < n; i++ {
        x := nums[i]
        for x > 1 {
            p := int(spf[x])
            if existsAsPrime[p] {
                buckets[p] = append(buckets[p], i)
            }
            for x%p == 0 {
                x /= p
            }
        }
    }

    dist := make([]int, n)
    for i := range dist {
        dist[i] = -1
    }
    visitedPrimes := make([]bool, maxVal+1)

    queue := []int{0}
    dist[0] = 0
    head := 0

    for head < len(queue) {
        u := queue[head]
        head++

        if u == n-1 {
            return dist[u]
        }

        for _, v := range []int{u - 1, u + 1} {
            if v >= 0 && v < n && dist[v] == -1 {
                dist[v] = dist[u] + 1
                queue = append(queue, v)
            }
        }

        p := nums[u]
        if p > 1 && int(spf[p]) == p && !visitedPrimes[p] {
            visitedPrimes[p] = true
            for _, v := range buckets[p] {
                if dist[v] == -1 {
                    dist[v] = dist[u] + 1
                    queue = append(queue, v)
                }
            }
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
def min_jumps(nums)
  n = nums.length
  return 0 if n == 1

  max_val = 1000000
  spf = Array.new(max_val + 1, 0)
  i = 2
  while i * i <= max_val
    if spf[i] == 0
      j = i * i
      while j <= max_val
        spf[j] = i if spf[j] == 0
        j += i
      end
    end
    i += 1
  end
  (2..max_val).each { |k| spf[k] = k if spf[k] == 0 }

  exists_as_prime = Array.new(max_val + 1, false)
  nums.each do |x|
    exists_as_prime[x] = true if x > 1 && spf[x] == x
  end

  buckets = {}
  nums.each_with_index do |x, idx|
    temp = x
    while temp > 1
      p = spf[temp]
      if exists_as_prime[p]
        buckets[p] ||= []
        buckets[p] << idx
      end
      while temp % p == 0
        temp /= p
      end
    end
  end

  dist = Array.new(n, -1)
  visited_primes = Array.new(max_val + 1, false)
  queue = [0]
  head = 0
  dist[0] = 0

  while head < queue.length
    u = queue[head]
    head += 1
    return dist[u] if u == n - 1

    [u - 1, u + 1].each do |v|
      if v >= 0 && v < n && dist[v] == -1
        dist[v] = dist[u] + 1
        queue << v
      end
    end

    p = nums[u]
    if p > 1 && spf[p] == p && !visited_primes[p]
      visited_primes[p] = true
      if buckets[p]
        buckets[p].each do |v|
          if dist[v] == -1
            dist[v] = dist[u] + 1
            queue << v
          end
        end
      end
    end
  end

  return -1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
  def minJumps(nums: Array[Int]): Int = {
    val n = nums.length
    if (n == 1) return 0

    val maxVal = 1000000
    val spf = Array.tabulate(maxVal + 1)(i => i)
    var i = 2
    while (i * i <= maxVal) {
      if (spf(i) == i) {
        var j = i * i
        while (j <= maxVal) {
          if (spf(j) == j) spf(j) = i
          j += i
        }
      }
      i += 1
    }

    val existsAsPrime = new Array[Boolean](maxVal + 1)
    for (x <- nums) {
      if (x > 1 && spf(x) == x) existsAsPrime(x) = true
    }

    val buckets = new Array[mutable.ListBuffer[Int]](maxVal + 1)
    for (idx <- 0 until n) {
      var x = nums(idx)
      while (x > 1) {
        val p = spf(x)
        if (existsAsPrime(p)) {
          if (buckets(p) == null) buckets(p) = new mutable.ListBuffer[Int]()
          buckets(p) += idx
        }
        while (x % p == 0) x /= p
      }
    }

    val dist = Array.fill(n)(-1)
    val visitedPrimes = new Array[Boolean](maxVal + 1)
    val queue = mutable.Queue[Int]()

    dist(0) = 0
    queue.enqueue(0)

    while (queue.nonEmpty) {
      val u = queue.dequeue()
      if (u == n - 1) return dist(u)

      val neighbors = List(u - 1, u + 1)
      for (v <- neighbors) {
        if (v >= 0 && v < n && dist(v) == -1) {
          dist(v) = dist(u) + 1
          queue.enqueue(v)
        }
      }

      val p = nums(u)
      if (p > 1 && spf(p) == p && !visitedPrimes(p)) {
        visitedPrimes(p) = true
        if (buckets(p) != null) {
          for (v <- buckets(p)) {
            if (dist(v) == -1) {
              dist(v) = dist(u) + 1
              queue.enqueue(v)
            }
          }
        }
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
use std::collections::VecDeque;

impl Solution {
    pub fn min_jumps(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 1 {
            return 0;
        }

        let mut max_val = 0;
        for &x in &nums {
            if x > max_val {
                max_val = x;
            }
        }

        let mut spf = (0..=max_val).collect::<Vec<i32>>();
        let mut i = 2;
        while i * i <= max_val {
            if spf[i as usize] == i {
                let mut j = i * i;
                while j <= max_val {
                    if spf[j as usize] == j {
                        spf[j as usize] = i;
                    }
                    j += i;
                }
            }
            i += 1;
        }

        let mut is_prime_in_nums = vec![false; max_val as usize + 1];
        for &x in &nums {
            if x >= 2 && spf[x as usize] == x {
                is_prime_in_nums[x as usize] = true;
            }
        }

        let mut prime_to_indices = vec![vec![]; max_val as usize + 1];
        for (idx, &x) in nums.iter().enumerate() {
            let mut temp = x as usize;
            while temp > 1 {
                let p = spf[temp] as usize;
                if is_prime_in_nums[p] {
                    prime_to_indices[p].push(idx);
                }
                while temp % p == 0 {
                    temp /= p;
                }
            }
        }

        let mut dist = vec![-1; n];
        let mut q = VecDeque::new();
        dist[0] = 0;
        q.push_back(0);

        let mut prime_visited = vec![false; max_val as usize + 1];

        while let Some(u) = q.pop_front() {
            if u == n - 1 {
                return dist[u];
            }

            if u + 1 < n && dist[u + 1] == -1 {
                dist[u + 1] = dist[u] + 1;
                q.push_back(u + 1);
            }
            if u > 0 && dist[u - 1] == -1 {
                dist[u - 1] = dist[u] + 1;
                q.push_back(u - 1);
            }

            let val = nums[u] as usize;
            if val >= 2 && spf[val] == val as i32 && !prime_visited[val] {
                prime_visited[val] = true;
                for &v in &prime_to_indices[val] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1;
                        q.push_back(v);
                    }
                }
            }
        }

        -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-jumps nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [max-val (if (null? nums) 0 (apply max nums))])
    (if (= n 1)
        0
        (let* ([spf (make-vector (+ max-val 1) 0)])
          (for ([i (in-range 2 (+ max-val 1))])
            (vector-set! spf i i))
          (for ([i (in-range 2 (+ 1 (integer-sqrt max-val)))])
            (when (= (vector-ref spf i) i)
              (for ([j (in-range (* i i) (+ max-val 1) i)])
                (when (= (vector-ref spf j) j)
                  (vector-set! spf j i)))))

          (define is-prime-in-nums (make-vector (+ max-val 1) #f))
          (for ([x nums])
            (when (and (>= x 2) (= (vector-ref spf x) x))
              (vector-set! is-prime-in-nums x #t)))

          (define prime-to-indices (make-vector (+ max-val 1) '()))
          (for ([i (in-range n)])
            (let ([x (vector-ref nums-vec i)])
              (let loop ([temp x])
                (when (> temp 1)
                  (let ([p (vector-ref spf temp)])
                    (when (vector-ref is-prime-in-nums p)
                      (vector-set! prime-to-indices p (cons i (vector-ref prime-to-indices p))))
                    (let inner-loop ([curr temp])
                      (if (and (> curr 1) (= (remainder curr p) 0))
                          (inner-loop (quotient curr p))
                          (loop curr))))))))

          (define dist (make-vector n -1))
          (define prime-visited (make-vector (+ max-val 1) #f))
          (vector-set! dist 0 0)

          (let bfs ([q-front '(0)] [q-back '()])
            (cond
              [(and (null? q-front) (null? q-back)) -1]
              [(null? q-front) (bfs (reverse q-back) '())]
              [else
               (let* ([u (car q-front)]
                      [rest-front (cdr q-front)])
                 (if (= u (- n 1))
                     (vector-ref dist u)
                     (let* ([d-u (vector-ref dist u)]
                            [d-next (+ d-u 1)]
                            [val (vector-ref nums-vec u)]
                            [is-u-prime (and (>= val 2) (= (vector-ref spf val) val))]
                            [new-back q-back])
                       (let* ([after-adj (for/fold ([curr-back new-back])
                                                  ([v (list (+ u 1) (- u 1))])
                                           (if (and (>= v 0) (< v n) (= (vector-ref dist v) -1))
                                               (begin
                                                 (vector-set! dist v d-next)
                                                 (cons v curr-back))
                                               curr-back))]
                              [after-tele (if (and is-u-prime (not (vector-ref prime-visited val)))
                                              (begin
                                                (vector-set! prime-visited val #t)
                                                (for/fold ([curr-back after-adj])
                                                          ([v (vector-ref prime-to-indices val)])
                                                  (if (= (vector-ref dist v) -1)
                                                      (begin
                                                        (vector-set! dist v d-next)
                                                        (cons v curr-back))
                                                      curr-back)))
                                              after-adj)])
                         (bfs rest-front after-tele))))]))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_jumps(Nums :: [integer()]) -> integer().
min_jumps(Nums) ->
  N = length(Nums),
  if N == 1 -> 0;
     true -> solve(Nums, N)
  end.

solve(Nums, N) ->
  NumsVec = array:from_list(Nums),
  MaxVal = lists:max(Nums),
  SPF = ets:new(spf, [set, public]),
  [ets:insert(SPF, {I, I}) || I <- lists:seq(2, MaxVal)],
  SqrtMax = round(math:sqrt(MaxVal)),
  lists:foreach(fun(I) ->
    case ets:lookup(SPF, I) of
      [{I, I}] -> sieve_fill(I * I, I, MaxVal, SPF);
      _ -> ok
    end
  end, lists:seq(2, SqrtMax)),
  IsPrimeInNums = ets:new(is_prime_in_nums, [set, public]),
  lists:foreach(fun(X) ->
    case ets:lookup(SPF, X) of
      [{X, X}] -> ets:insert(IsPrimeInNums, {X});
      _ -> ok
    end
  end, Nums),
  PrimeToIndices = ets:new(prime_to_indices, [bag, public]),
  lists:foreach(fun(I) ->
    Val = array:get(I, NumsVec),
    Factors = get_distinct_prime_factors(Val, SPF),
    lists:foreach(fun(P) ->
      case ets:member(IsPrimeInNums, P) of
        true -> ets:insert(PrimeToIndices, {P, I});
        false -> ok
      end
    end, Factors)
  end, lists:seq(0, N - 1)),
  Dist = ets:new(dist, [set, public]),
  ets:insert(Dist, {0, 0}),
  PrimeVisited = ets:new(prime_visited, [set, public]),
  Queue = queue:from_list([0]),
  bfs(Queue, NumsVec, N, SPF, PrimeToIndices, Dist, PrimeVisited).

sieve_fill(J, I, MaxVal, SPF) when J =< MaxVal ->
  case ets:lookup(SPF, J) of
    [{J, J}] -> ets:insert(SPF, {J, I});
    _ -> ok
  end,
  sieve_fill(J + I, I, MaxVal, SPF);
sieve_fill(_, _, _, _) -> ok.

get_distinct_prime_factors(1, _) -> [];
get_distinct_prime_factors(Val, SPF) ->
  [{Val, P}] = ets:lookup(SPF, Val),
  NewVal = div_repeat(Val, P),
  [P | get_distinct_prime_factors(NewVal, SPF)].

div_repeat(Val, P) when Val rem P == 0 -> div_repeat(Val div P, P);
div_repeat(Val, _) -> Val.

bfs(Queue, NumsVec, N, SPF, PrimeToIndices, Dist, PrimeVisited) ->
  case queue:out(Queue) of
    {empty, _} -> -1;
    {{value, U}, Q2} ->
      [{U, DU}] = ets:lookup(Dist, U),
      if U == N - 1 -> DU;
         true ->
           {Q3, _} = lists:foldl(fun(V, {Qi, Di}) ->
             if V >= 0, V < N ->
               case ets:member(Di, V) of
                 false -> ets:insert(Di, {V, DU + 1}), {queue:in(V, Qi), Di};
                 true -> {Qi, Di}
               end;
               true -> {Qi, Di}
             end
           end, {Q2, Dist}, [U - 1, U + 1]),
           Val = array:get(U, NumsVec),
           IsPrime = case ets:lookup(SPF, Val) of [{Val, Val}] -> true; _ -> false end,
           Q4 = if IsPrime ->
                    case ets:member(PrimeVisited, Val) of
                      false ->
                        ets:insert(PrimeVisited, {Val}),
                        Indices = ets:lookup(PrimeToIndices, Val),
                        lists:foldl(fun({_, V}, Qi2) ->
                          case ets:member(Dist, V) of
                            false -> ets:insert(Dist, {V, DU + 1}), queue:in(V, Qi2);
                            true -> Qi2
                          end
                        end, Q3, Indices);
                      true -> Q3
                    end;
                    true -> Q3
                 end,
           bfs(Q4, NumsVec, N, SPF, PrimeToIndices, Dist, PrimeVisited)
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_jumps(nums :: [integer]) :: integer
  def min_jumps(nums) do
    n = length(nums)
    if n == 1 do
      0
    else
      solve(nums, n)
    end
  end

  defp solve(nums, n) do
    nums_vec = :array.from_list(nums)
    max_val = Enum.max(nums)
    spf = :ets.new(:spf, [:set, :public])
    for i <- 2..max_val, do: :ets.insert(spf, {i, i})

    sqrt_max = round(:math.sqrt(max_val))
    for i <- 2..sqrt_max do
      case :ets.lookup(spf, i) do
        [{^i, ^i}] -> sieve_fill(i * i, i, max_val, spf)
        _ -> :ok
      end
    end

    is_prime_in_nums = :ets.new(:is_prime_in_nums, [:set, :public])
    for x <- nums do
      case :ets.lookup(spf, x) do
        [{^x, ^x}] -> :ets.insert(is_prime_in_nums, {x})
        _ -> :ok
      end
    end

    prime_to_indices = :ets.new(:prime_to_indices, [:bag, :public])
    for i <- 0..(n - 1) do
      val = :array.get(i, nums_vec)
      factors = get_distinct_factors(val, spf)
      for p <- factors do
        if :ets.member(is_prime_in_nums, p) do
          :ets.insert(prime_to_indices, {p, i})
        end
      end
    end

    dist = :ets.new(:dist, [:set, :public])
    :ets.insert(dist, {0, 0})
    prime_visited = :ets.new(:prime_visited, [:set, :public])
    queue = :queue.from_list([0])
    bfs(queue, nums_vec, n, spf, prime_to_indices, dist, prime_visited)
  end

  defp sieve_fill(j, i, max_val, spf) when j <= max_val do
    case :ets.lookup(spf, j) do
      [{^j, ^j}] -> :ets.insert(spf, {j, i})
      _ -> :ok
    end
    sieve_fill(j + i, i, max_val, spf)
  end
  defp sieve_fill(_, _, _, _), do: :ok

  defp get_distinct_factors(1, _), do: []
  defp get_distinct_factors(val, spf) do
    [{^val, p}] = :ets.lookup(spf, val)
    new_val = div_repeat(val, p)
    [p | get_distinct_factors(new_val, spf)]
  end

  defp div_repeat(val, p) when rem(val, p) == 0, do: div_repeat(div(val, p), p)
  defp div_repeat(val, _), do: val

  defp bfs(queue, nums_vec, n, spf, prime_to_indices, dist, prime_visited) do
    case :queue.out(queue) do
      {:empty, _} -> -1
      {{:value, u}, queue2} ->
        [{^u, d_u}] = :ets.lookup(dist, u)
        if u == n - 1 do
          d_u
        else
          queue3 = Enum.reduce([u - 1, u + 1], queue2, fn v, q ->
            if v >= 0 and v < n and not :ets.member(dist, v) do
              :ets.insert(dist, {v, d_u + 1})
              :queue.in(v, q)
            else
              q
            end
          end)

          val = :array.get(u, nums_vec)
          is_prime = case :ets.lookup(spf, val) do [{^val, ^val}] -> true; _ -> false end
          queue4 = if is_prime and not :ets.member(prime_visited, val) do
            :ets.insert(prime_visited, {val})
            indices = :ets.lookup(prime_to_indices, val)
            Enum.reduce(indices, queue3, fn {_, v}, q ->
              if not :ets.member(dist, v) do
                :ets.insert(dist, {v, d_u + 1})
                :queue.in(v, q)
              else
                q
              end
            end)
          else
            queue3
          end
          bfs(queue4, nums_vec, n, spf, prime_to_indices, dist, prime_visited)
        end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M \log \log M + N \log M) where $M$ is the maximum value in $nums$ ($10^6$) and $N$ is the length of the array ($10^5$). The sieve takes $O(M \log \log M)$, and factoring each $nums[j]$ takes at most $O(\log M)$ time (roughly 7 unique prime factors). BFS visits each node and each prime factor bucket exactly once, ensuring efficient traversal within time limits.
- **Space Complexity:** O(M + N \log M) for storing the sieve's smallest prime factor array, the prime buckets (CSR format or list of lists), the BFS distance array, and the BFS queue.
