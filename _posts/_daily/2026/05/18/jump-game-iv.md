---
layout: post
title: "Jump Game IV"
date: 2026-05-18 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Breadth-First Search"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/jump-game-iv/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minJumps(vector<int>& arr) {\n      \
        \  int n = arr.size();\n        if (n <= 1) return 0;\n\n        unordered_map<int,\
        \ vector<int>> adj;\n        for (int i = 0; i < n; i++) {\n            adj[arr[i]].push_back(i);\n\
        \        }\n\n        vector<bool> visited(n, false);\n        queue<int> q;\n\
        \n        q.push(0);\n        visited[0] = true;\n        int steps = 0;\n\n\
        \        while (!q.empty()) {\n            int size = q.size();\n          \
        \  for (int i = 0; i < size; i++) {\n                int curr = q.front();\n\
        \                q.pop();\n\n                if (curr == n - 1) return steps;\n\
        \n                vector<int>& nextIndices = adj[arr[curr]];\n             \
        \   nextIndices.push_back(curr - 1);\n                nextIndices.push_back(curr\
        \ + 1);\n\n                for (int next : nextIndices) {\n                \
        \    if (next >= 0 && next < n && !visited[next]) {\n                      \
        \  visited[next] = true;\n                        q.push(next);\n          \
        \          }\n                }\n                nextIndices.clear();\n    \
        \        }\n            steps++;\n        }\n        return -1;\n    }\n};"
      java: "class Solution {\n    public int minJumps(int[] arr) {\n        int n =\
        \ arr.length;\n        if (n <= 1) return 0;\n\n        Map<Integer, List<Integer>>\
        \ adj = new HashMap<>();\n        for (int i = 0; i < n; i++) {\n          \
        \  adj.computeIfAbsent(arr[i], x -> new ArrayList<>()).add(i);\n        }\n\n\
        \        boolean[] visited = new boolean[n];\n        Queue<Integer> q = new\
        \ LinkedList<>();\n\n        q.offer(0);\n        visited[0] = true;\n     \
        \   int steps = 0;\n\n        while (!q.isEmpty()) {\n            int size =\
        \ q.size();\n            for (int i = 0; i < size; i++) {\n                int\
        \ curr = q.poll();\n\n                if (curr == n - 1) return steps;\n\n \
        \               List<Integer> nextIndices = adj.get(arr[curr]);\n          \
        \      if (nextIndices != null) {\n                    nextIndices.add(curr\
        \ - 1);\n                    nextIndices.add(curr + 1);\n                  \
        \  for (int next : nextIndices) {\n                        if (next >= 0 &&\
        \ next < n && !visited[next]) {\n                            visited[next] =\
        \ true;\n                            q.offer(next);\n                      \
        \  }\n                    }\n                    adj.remove(arr[curr]);\n  \
        \              } else {\n                    int[] simpleNext = {curr - 1, curr\
        \ + 1};\n                    for (int next : simpleNext) {\n               \
        \         if (next >= 0 && next < n && !visited[next]) {\n                 \
        \           visited[next] = true;\n                            q.offer(next);\n\
        \                        }\n                    }\n                }\n     \
        \       }\n            steps++;\n        }\n        return -1;\n    }\n}"
      python: "from collections import deque, defaultdict\n\nclass Solution(object):\n\
        \    def minJumps(self, arr):\n        \"\"\"\n        :type arr: List[int]\n\
        \        :rtype: int\n        \"\"\"\n        n = len(arr)\n        if n <=\
        \ 1:\n            return 0\n\n        adj = defaultdict(list)\n        for i,\
        \ val in enumerate(arr):\n            adj[val].append(i)\n\n        q = deque([0])\n\
        \        visited = {0}\n        steps = 0\n\n        while q:\n            for\
        \ _ in range(len(q)):\n                curr = q.popleft()\n\n              \
        \  if curr == n - 1:\n                    return steps\n\n                for\
        \ next_idx in adj[arr[curr]]:\n                    if next_idx not in visited:\n\
        \                        visited.add(next_idx)\n                        q.append(next_idx)\n\
        \n                adj[arr[curr]] = []\n\n                for next_idx in [curr\
        \ - 1, curr + 1]:\n                    if 0 <= next_idx < n and next_idx not\
        \ in visited:\n                        visited.add(next_idx)\n             \
        \           q.append(next_idx)\n\n            steps += 1\n\n        return -1"
      python3: "import collections\nfrom typing import List\n\nclass Solution:\n   \
        \ def minJumps(self, arr: List[int]) -> int:\n        n = len(arr)\n       \
        \ if n <= 1:\n            return 0\n\n        graph = collections.defaultdict(list)\n\
        \        for i, x in enumerate(arr):\n            graph[x].append(i)\n\n   \
        \     queue = collections.deque([0])\n        visited = [False] * n\n      \
        \  visited[0] = True\n        steps = 0\n\n        while queue:\n          \
        \  size = len(queue)\n            for _ in range(size):\n                curr\
        \ = queue.popleft()\n                if curr == n - 1:\n                   \
        \ return steps\n\n                val = arr[curr]\n                if val in\
        \ graph:\n                    for neighbor in graph[val]:\n                \
        \        if not visited[neighbor]:\n                            visited[neighbor]\
        \ = True\n                            queue.append(neighbor)\n             \
        \       del graph[val]\n\n                if curr + 1 < n and not visited[curr\
        \ + 1]:\n                    visited[curr + 1] = True\n                    queue.append(curr\
        \ + 1)\n\n                if curr - 1 >= 0 and not visited[curr - 1]:\n    \
        \                visited[curr - 1] = True\n                    queue.append(curr\
        \ - 1)\n            steps += 1\n        return -1"
      c: "#include <stdlib.h>\n#include <stdbool.h>\n\ntypedef struct {\n    int val;\n\
        \    int idx;\n} Pair;\n\nint compare(const void* a, const void* b) {\n    Pair*\
        \ p1 = (Pair*)a;\n    Pair* p2 = (Pair*)b;\n    if (p1->val < p2->val) return\
        \ -1;\n    if (p1->val > p2->val) return 1;\n    return 0;\n}\n\nint find_first(Pair*\
        \ pairs, int n, int val) {\n    int l = 0, r = n - 1, ans = -1;\n    while (l\
        \ <= r) {\n        int mid = l + (r - l) / 2;\n        if (pairs[mid].val ==\
        \ val) {\n            ans = mid;\n            r = mid - 1;\n        } else if\
        \ (pairs[mid].val < val) {\n            l = mid + 1;\n        } else {\n   \
        \         r = mid - 1;\n        }\n    }\n    return ans;\n}\n\nint minJumps(int*\
        \ arr, int arrSize) {\n    if (arrSize <= 1) return 0;\n\n    Pair* pairs =\
        \ (Pair*)malloc(arrSize * sizeof(Pair));\n    for (int i = 0; i < arrSize; i++)\
        \ {\n        pairs[i].val = arr[i];\n        pairs[i].idx = i;\n    }\n    qsort(pairs,\
        \ arrSize, sizeof(Pair), compare);\n\n    int* q = (int*)malloc(arrSize * sizeof(int));\n\
        \    int* dist = (int*)malloc(arrSize * sizeof(int));\n    bool* val_processed\
        \ = (bool*)calloc(arrSize, sizeof(bool));\n    int* v_start_map = (int*)malloc(arrSize\
        \ * sizeof(int));\n\n    for (int i = 0; i < arrSize; i++) {\n        dist[i]\
        \ = -1;\n        v_start_map[i] = find_first(pairs, arrSize, arr[i]);\n    }\n\
        \n    int head = 0, tail = 0;\n    dist[0] = 0;\n    q[tail++] = 0;\n\n    while\
        \ (head < tail) {\n        int curr = q[head++];\n        int d = dist[curr];\n\
        \n        if (curr == arrSize - 1) {\n            free(pairs); free(q); free(dist);\
        \ free(val_processed); free(v_start_map);\n            return d;\n        }\n\
        \n        if (curr + 1 < arrSize && dist[curr + 1] == -1) {\n            dist[curr\
        \ + 1] = d + 1;\n            q[tail++] = curr + 1;\n        }\n        if (curr\
        \ - 1 >= 0 && dist[curr - 1] == -1) {\n            dist[curr - 1] = d + 1;\n\
        \            q[tail++] = curr - 1;\n        }\n\n        int v_start = v_start_map[curr];\n\
        \        if (!val_processed[v_start]) {\n            for (int k = v_start; k\
        \ < arrSize && pairs[k].val == arr[curr]; k++) {\n                int neighbor\
        \ = pairs[k].idx;\n                if (dist[neighbor] == -1) {\n           \
        \         dist[neighbor] = d + 1;\n                    q[tail++] = neighbor;\n\
        \                }\n            }\n            val_processed[v_start] = true;\n\
        \        }\n    }\n\n    free(pairs); free(q); free(dist); free(val_processed);\
        \ free(v_start_map);\n    return -1;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int MinJumps(int[] arr) {\n        int n = arr.Length;\n        if (n <= 1)\
        \ return 0;\n\n        Dictionary<int, List<int>> graph = new Dictionary<int,\
        \ List<int>>();\n        for (int i = 0; i < n; i++) {\n            if (!graph.ContainsKey(arr[i]))\
        \ {\n                graph[arr[i]] = new List<int>();\n            }\n     \
        \       graph[arr[i]].Add(i);\n        }\n\n        Queue<int> queue = new Queue<int>();\n\
        \        bool[] visited = new bool[n];\n        queue.Enqueue(0);\n        visited[0]\
        \ = true;\n        int steps = 0;\n\n        while (queue.Count > 0) {\n   \
        \         int size = queue.Count;\n            for (int i = 0; i < size; i++)\
        \ {\n                int curr = queue.Dequeue();\n                if (curr ==\
        \ n - 1) return steps;\n\n                int val = arr[curr];\n           \
        \     if (graph.ContainsKey(val)) {\n                    foreach (int neighbor\
        \ in graph[val]) {\n                        if (!visited[neighbor]) {\n    \
        \                        visited[neighbor] = true;\n                       \
        \     queue.Enqueue(neighbor);\n                        }\n                \
        \    }\n                    graph.Remove(val);\n                }\n\n      \
        \          if (curr + 1 < n && !visited[curr + 1]) {\n                    visited[curr\
        \ + 1] = true;\n                    queue.Enqueue(curr + 1);\n             \
        \   }\n                if (curr - 1 >= 0 && !visited[curr - 1]) {\n        \
        \            visited[curr - 1] = true;\n                    queue.Enqueue(curr\
        \ - 1);\n                }\n            }\n            steps++;\n        }\n\
        \        return -1;\n    }\n}"
      javascript: "/**\n * @param {number[]} arr\n * @return {number}\n */\nvar minJumps\
        \ = function(arr) {\n    const n = arr.length;\n    if (n <= 1) return 0;\n\n\
        \    const graph = new Map();\n    for (let i = 0; i < n; i++) {\n        if\
        \ (!graph.has(arr[i])) {\n            graph.set(arr[i], []);\n        }\n  \
        \      graph.get(arr[i]).push(i);\n    }\n\n    const queue = [0];\n    const\
        \ visited = new Uint8Array(n);\n    visited[0] = 1;\n    let head = 0;\n   \
        \ let steps = 0;\n\n    while (head < queue.length) {\n        let size = queue.length\
        \ - head;\n        for (let i = 0; i < size; i++) {\n            const curr\
        \ = queue[head++];\n            if (curr === n - 1) return steps;\n\n      \
        \      const val = arr[curr];\n            if (graph.has(val)) {\n         \
        \       const neighbors = graph.get(val);\n                for (let j = 0; j\
        \ < neighbors.length; j++) {\n                    const neighbor = neighbors[j];\n\
        \                    if (!visited[neighbor]) {\n                        visited[neighbor]\
        \ = 1;\n                        queue.push(neighbor);\n                    }\n\
        \                }\n                graph.delete(val);\n            }\n\n  \
        \          if (curr + 1 < n && !visited[curr + 1]) {\n                visited[curr\
        \ + 1] = 1;\n                queue.push(curr + 1);\n            }\n        \
        \    if (curr - 1 >= 0 && !visited[curr - 1]) {\n                visited[curr\
        \ - 1] = 1;\n                queue.push(curr - 1);\n            }\n        }\n\
        \        steps++;\n    }\n    return -1;\n};"
      typescript: "function minJumps(arr: number[]): number {\n    const n = arr.length;\n\
        \    if (n <= 1) return 0;\n\n    const map = new Map<number, number[]>();\n\
        \    for (let i = 0; i < n; i++) {\n        if (!map.has(arr[i])) {\n      \
        \      map.set(arr[i], []);\n        }\n        map.get(arr[i])!.push(i);\n\
        \    }\n\n    let steps = 0;\n    let queue = [0];\n    const visited = new\
        \ Uint8Array(n);\n    visited[0] = 1;\n\n    while (queue.length > 0) {\n  \
        \      const nextQueue: number[] = [];\n        for (const node of queue) {\n\
        \            if (node === n - 1) return steps;\n\n            const val = arr[node];\n\
        \            const indices = map.get(val);\n            if (indices) {\n   \
        \             for (const idx of indices) {\n                    if (!visited[idx])\
        \ {\n                        visited[idx] = 1;\n                        nextQueue.push(idx);\n\
        \                    }\n                }\n                map.delete(val);\n\
        \            }\n\n            if (node + 1 < n && !visited[node + 1]) {\n  \
        \              visited[node + 1] = 1;\n                nextQueue.push(node +\
        \ 1);\n            }\n\n            if (node - 1 >= 0 && !visited[node - 1])\
        \ {\n                visited[node - 1] = 1;\n                nextQueue.push(node\
        \ - 1);\n            }\n        }\n        queue = nextQueue;\n        steps++;\n\
        \    }\n\n    return steps;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $arr\n     * @return\
        \ Integer\n     */\n    function minJumps($arr) {\n        $n = count($arr);\n\
        \        if ($n <= 1) return 0;\n\n        $map = [];\n        foreach ($arr\
        \ as $i => $val) {\n            $map[$val][] = $i;\n        }\n\n        $visited\
        \ = array_fill(0, $n, false);\n        $visited[0] = true;\n        $queue =\
        \ new SplQueue();\n        $queue->enqueue(0);\n        $steps = 0;\n\n    \
        \    while (!$queue->isEmpty()) {\n            $size = $queue->count();\n  \
        \          for ($i = 0; $i < $size; $i++) {\n                $curr = $queue->dequeue();\n\
        \n                if ($curr == $n - 1) return $steps;\n\n                $val\
        \ = $arr[$curr];\n                if (isset($map[$val])) {\n               \
        \     foreach ($map[$val] as $next) {\n                        if (!$visited[$next])\
        \ {\n                            $visited[$next] = true;\n                 \
        \           $queue->enqueue($next);\n                        }\n           \
        \         }\n                    unset($map[$val]);\n                }\n\n \
        \               if ($curr + 1 < $n && !$visited[$curr + 1]) {\n            \
        \        $visited[$curr + 1] = true;\n                    $queue->enqueue($curr\
        \ + 1);\n                }\n\n                if ($curr - 1 >= 0 && !$visited[$curr\
        \ - 1]) {\n                    $visited[$curr - 1] = true;\n               \
        \     $queue->enqueue($curr - 1);\n                }\n            }\n      \
        \      $steps++;\n        }\n\n        return $steps;\n    }\n}"
      swift: "class Solution {\n    func minJumps(_ arr: [Int]) -> Int {\n        let\
        \ n = arr.count\n        if n <= 1 { return 0 }\n\n        var map = [Int: [Int]]()\n\
        \        for (i, val) in arr.enumerated() {\n            map[val, default: []].append(i)\n\
        \        }\n\n        var visited = Array(repeating: false, count: n)\n    \
        \    visited[0] = true\n        var queue = [0]\n        var steps = 0\n\n \
        \       while !queue.isEmpty {\n            var nextQueue = [Int]()\n      \
        \      for curr in queue {\n                if curr == n - 1 { return steps\
        \ }\n\n                let val = arr[curr]\n                if let sameValIndices\
        \ = map[val] {\n                    for next in sameValIndices {\n         \
        \               if !visited[next] {\n                            visited[next]\
        \ = true\n                            nextQueue.append(next)\n             \
        \           }\n                    }\n                    map.removeValue(forKey:\
        \ val)\n                }\n\n                if curr + 1 < n && !visited[curr\
        \ + 1] {\n                    visited[curr + 1] = true\n                   \
        \ nextQueue.append(curr + 1)\n                }\n\n                if curr -\
        \ 1 >= 0 && !visited[curr - 1] {\n                    visited[curr - 1] = true\n\
        \                    nextQueue.append(curr - 1)\n                }\n       \
        \     }\n            queue = nextQueue\n            steps += 1\n        }\n\n\
        \        return steps\n    }\n}"
      kotlin: "import java.util.*\n\nclass Solution {\n    fun minJumps(arr: IntArray):\
        \ Int {\n        val n = arr.size\n        if (n <= 1) return 0\n\n        val\
        \ map = HashMap<Int, MutableList<Int>>()\n        for (i in 0 until n) {\n \
        \           map.computeIfAbsent(arr[i]) { mutableListOf<Int>() }.add(i)\n  \
        \      }\n\n        val visited = BooleanArray(n)\n        visited[0] = true\n\
        \        val queue = java.util.ArrayDeque<Int>()\n        queue.add(0)\n   \
        \     var steps = 0\n\n        while (queue.isNotEmpty()) {\n            val\
        \ size = queue.size\n            for (i in 0 until size) {\n               \
        \ val curr = queue.removeFirst()\n\n                if (curr == n - 1) return\
        \ steps\n\n                val valAtCurr = arr[curr]\n                if (map.containsKey(valAtCurr))\
        \ {\n                    val sameValIndices = map[valAtCurr]!!\n           \
        \         for (next in sameValIndices) {\n                        if (!visited[next])\
        \ {\n                            visited[next] = true\n                    \
        \        queue.addLast(next)\n                        }\n                  \
        \  }\n                    map.remove(valAtCurr)\n                }\n\n     \
        \           if (curr + 1 < n && !visited[curr + 1]) {\n                    visited[curr\
        \ + 1] = true\n                    queue.addLast(curr + 1)\n               \
        \ }\n\n                if (curr - 1 >= 0 && !visited[curr - 1]) {\n        \
        \            visited[curr - 1] = true\n                    queue.addLast(curr\
        \ - 1)\n                }\n            }\n            steps++\n        }\n\n\
        \        return steps\n    }\n}"
      dart: "class Solution {\n  int minJumps(List<int> arr) {\n    int n = arr.length;\n\
        \    if (n <= 1) return 0;\n\n    Map<int, List<int>> graph = {};\n    for (int\
        \ i = 0; i < n; i++) {\n      if (!graph.containsKey(arr[i])) {\n        graph[arr[i]]\
        \ = [];\n      }\n      graph[arr[i]]!.add(i);\n    }\n\n    List<int> queue\
        \ = [0];\n    List<bool> visited = List.filled(n, false);\n    visited[0] =\
        \ true;\n    int steps = 0;\n\n    while (queue.isNotEmpty) {\n      List<int>\
        \ nextQueue = [];\n      for (int curr in queue) {\n        if (curr == n -\
        \ 1) return steps;\n\n        int val = arr[curr];\n        if (graph.containsKey(val))\
        \ {\n          for (int nextIdx in graph[val]!) {\n            if (!visited[nextIdx])\
        \ {\n              visited[nextIdx] = true;\n              nextQueue.add(nextIdx);\n\
        \            }\n          }\n          graph.remove(val);\n        }\n\n   \
        \     if (curr + 1 < n && !visited[curr + 1]) {\n          visited[curr + 1]\
        \ = true;\n          nextQueue.add(curr + 1);\n        }\n        if (curr -\
        \ 1 >= 0 && !visited[curr - 1]) {\n          visited[curr - 1] = true;\n   \
        \       nextQueue.add(curr - 1);\n        }\n      }\n      queue = nextQueue;\n\
        \      steps++;\n    }\n\n    return -1;\n  }\n}"
      go: "func minJumps(arr []int) int {\n\tn := len(arr)\n\tif n <= 1 {\n\t\treturn\
        \ 0\n\t}\n\n\tgraph := make(map[int][]int)\n\tfor i, val := range arr {\n\t\t\
        graph[val] = append(graph[val], i)\n\t}\n\n\tqueue := []int{0}\n\tvisited :=\
        \ make([]bool, n)\n\tvisited[0] = true\n\tsteps := 0\n\n\tfor len(queue) > 0\
        \ {\n\t\tsize := len(queue)\n\t\tfor i := 0; i < size; i++ {\n\t\t\tcurr :=\
        \ queue[i]\n\t\t\tif curr == n-1 {\n\t\t\t\treturn steps\n\t\t\t}\n\n\t\t\t\
        val := arr[curr]\n\t\t\tif indices, ok := graph[val]; ok {\n\t\t\t\tfor _, nextIdx\
        \ := range indices {\n\t\t\t\t\tif !visited[nextIdx] {\n\t\t\t\t\t\tvisited[nextIdx]\
        \ = true\n\t\t\t\t\t\tqueue = append(queue, nextIdx)\n\t\t\t\t\t}\n\t\t\t\t\
        }\n\t\t\t\tdelete(graph, val)\n\t\t\t}\n\n\t\t\tif curr+1 < n && !visited[curr+1]\
        \ {\n\t\t\t\tvisited[curr+1] = true\n\t\t\t\tqueue = append(queue, curr+1)\n\
        \t\t\t}\n\t\t\tif curr-1 >= 0 && !visited[curr-1] {\n\t\t\t\tvisited[curr-1]\
        \ = true\n\t\t\t\tqueue = append(queue, curr-1)\n\t\t\t}\n\t\t}\n\t\tqueue =\
        \ queue[size:]\n\t\tsteps++\n\t}\n\n\treturn -1\n}"
      ruby: "# @param {Integer[]} arr\n# @return {Integer}\ndef min_jumps(arr)\n  n\
        \ = arr.length\n  return 0 if n <= 1\n\n  graph = Hash.new { |h, k| h[k] = []\
        \ }\n  arr.each_with_index { |val, i| graph[val] << i }\n\n  queue = [0]\n \
        \ visited = Array.new(n, false)\n  visited[0] = true\n  steps = 0\n\n  while\
        \ !queue.empty?\n    next_queue = []\n    queue.each do |curr|\n      return\
        \ steps if curr == n - 1\n\n      val = arr[curr]\n      if graph.key?(val)\n\
        \        graph[val].each do |next_idx|\n          unless visited[next_idx]\n\
        \            visited[next_idx] = true\n            next_queue << next_idx\n\
        \          end\n        end\n        graph.delete(val)\n      end\n\n      if\
        \ curr + 1 < n && !visited[curr + 1]\n        visited[curr + 1] = true\n   \
        \     next_queue << curr + 1\n      end\n      if curr - 1 >= 0 && !visited[curr\
        \ - 1]\n        visited[curr - 1] = true\n        next_queue << curr - 1\n \
        \     end\n    end\n    queue = next_queue\n    steps += 1\n  end\n\n  steps\n\
        end"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  def minJumps(arr:\
        \ Array[Int]): Int = {\n    val n = arr.length\n    if (n <= 1) return 0\n\n\
        \    val graph = new mutable.HashMap[Int, mutable.ArrayBuffer[Int]]()\n    var\
        \ i = 0\n    while (i < n) {\n      val value = arr(i)\n      if (!graph.contains(value))\
        \ {\n        graph(value) = new mutable.ArrayBuffer[Int]()\n      }\n      graph(value)\
        \ += i\n      i += 1\n    }\n\n    var queue = mutable.ArrayBuffer[Int](0)\n\
        \    val visited = new Array[Boolean](n)\n    visited(0) = true\n    var steps\
        \ = 0\n\n    while (queue.nonEmpty) {\n      val nextQueue = new mutable.ArrayBuffer[Int]()\n\
        \      var qIdx = 0\n      while (qIdx < queue.length) {\n        val curr =\
        \ queue(qIdx)\n        if (curr == n - 1) return steps\n\n        val value\
        \ = arr(curr)\n        if (graph.contains(value)) {\n          val indices =\
        \ graph(value)\n          var j = 0\n          while (j < indices.length) {\n\
        \            val nextIdx = indices(j)\n            if (!visited(nextIdx)) {\n\
        \              visited(nextIdx) = true\n              nextQueue += nextIdx\n\
        \            }\n            j += 1\n          }\n          graph.remove(value)\n\
        \        }\n\n        if (curr + 1 < n && !visited(curr + 1)) {\n          visited(curr\
        \ + 1) = true\n          nextQueue += (curr + 1)\n        }\n        if (curr\
        \ - 1 >= 0 && !visited(curr - 1)) {\n          visited(curr - 1) = true\n  \
        \        nextQueue += (curr - 1)\n        }\n        qIdx += 1\n      }\n  \
        \    queue = nextQueue\n      steps += 1\n    }\n\n    steps\n  }\n}"
      rust: "use std::collections::{HashMap, VecDeque};\n\nimpl Solution {\n    pub\
        \ fn min_jumps(arr: Vec<i32>) -> i32 {\n        let n = arr.len();\n       \
        \ if n <= 1 {\n            return 0;\n        }\n\n        let mut map: HashMap<i32,\
        \ Vec<usize>> = HashMap::new();\n        for (i, &v) in arr.iter().enumerate()\
        \ {\n            map.entry(v).or_default().push(i);\n        }\n\n        let\
        \ mut q = VecDeque::new();\n        let mut visited = vec![false; n];\n    \
        \    q.push_back(0);\n        visited[0] = true;\n\n        let mut steps =\
        \ 0;\n        while !q.is_empty() {\n            let size = q.len();\n     \
        \       for _ in 0..size {\n                let i = q.pop_front().unwrap();\n\
        \                if i == n - 1 {\n                    return steps;\n      \
        \          }\n\n                let val = arr[i];\n                if let Some(indices)\
        \ = map.remove(&val) {\n                    for j in indices {\n           \
        \             if !visited[j] {\n                            visited[j] = true;\n\
        \                            q.push_back(j);\n                        }\n  \
        \                  }\n                }\n\n                if i + 1 < n && !visited[i\
        \ + 1] {\n                    visited[i + 1] = true;\n                    q.push_back(i\
        \ + 1);\n                }\n\n                if i > 0 && !visited[i - 1] {\n\
        \                    visited[i - 1] = true;\n                    q.push_back(i\
        \ - 1);\n                }\n            }\n            steps += 1;\n       \
        \ }\n        steps\n    }\n}"
      racket: "(define/contract (min-jumps arr)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([n (length arr)]\n         [arr-vec (list->vector arr)])\n    (if\
        \ (<= n 1)\n        0\n        (let/ec return\n          (let ([val-map (make-hash)])\n\
        \            (for ([i (in-range n)])\n              (let ([val (vector-ref arr-vec\
        \ i)])\n                (hash-set! val-map val (cons i (hash-ref val-map val\
        \ '())))))\n            (let ([visited (make-vector n #f)])\n              (vector-set!\
        \ visited 0 #t)\n              (let loop ([q (list 0)] [steps 0])\n        \
        \        (let ([next-level '()])\n                  (for ([i q])\n         \
        \           (if (= i (- n 1))\n                        (return steps)\n    \
        \                    (let* ([val (vector-ref arr-vec i)]\n                 \
        \              [indices (hash-ref val-map val '())])\n                     \
        \     (hash-remove! val-map val)\n                          (for ([nxt (list*\
        \ (+ i 1) (- i 1) indices)])\n                            (when (and (>= nxt\
        \ 0) (< nxt n) (not (vector-ref visited nxt)))\n                           \
        \   (vector-set! visited nxt #t)\n                              (set! next-level\
        \ (cons nxt next-level)))))))\n                  (loop (reverse next-level)\
        \ (+ steps 1)))))))))"
      erlang: "-spec min_jumps(Arr :: [integer()]) -> integer().\nmin_jumps(Arr) ->\n\
        \    N = length(Arr),\n    if N =:= 1 -> 0;\n       true ->\n           ArrTuple\
        \ = list_to_tuple(Arr),\n           ValueMap = build_map(Arr, 1, #{}),\n   \
        \        Queue = queue:in({1, 0}, queue:new()),\n           Visited = #{1 =>\
        \ true},\n           bfs(Queue, Visited, ValueMap, ArrTuple, N)\n    end.\n\n\
        build_map([], _, Map) -> Map;\nbuild_map([H|T], I, Map) ->\n    Indices = maps:get(H,\
        \ Map, []),\n    build_map(T, I + 1, Map#{H => [I | Indices]}).\n\nbfs(Queue,\
        \ Visited, ValueMap, ArrTuple, N) ->\n    {{value, {I, Steps}}, Q1} = queue:out(Queue),\n\
        \    if I =:= N -> Steps;\n       true ->\n           Val = element(I, ArrTuple),\n\
        \           {ValueNeighbors, NewValueMap} = case maps:find(Val, ValueMap) of\n\
        \               {ok, List} -> {List, maps:remove(Val, ValueMap)};\n        \
        \       error -> {[], ValueMap}\n           end,\n           Neighbors = [I\
        \ + 1, I - 1 | ValueNeighbors],\n           {NewQ, NewVisited} = add_neighbors(Neighbors,\
        \ Q1, Visited, N, Steps + 1),\n           bfs(NewQ, NewVisited, NewValueMap,\
        \ ArrTuple, N)\n    end.\n\nadd_neighbors([], Q, V, _, _) -> {Q, V};\nadd_neighbors([H|T],\
        \ Q, V, N, S) ->\n    case (H >= 1) and (H =< N) andalso not maps:is_key(H,\
        \ V) of\n        true -> add_neighbors(T, queue:in({H, S}, Q), V#{H => true},\
        \ N, S);\n        false -> add_neighbors(T, Q, V, N, S)\n    end."
      elixir: "defmodule Solution do\n  @spec min_jumps(arr :: [integer]) :: integer\n\
        \  def min_jumps(arr) do\n    n = length(arr)\n    if n <= 1 do\n      0\n \
        \   else\n      arr_tuple = List.to_tuple(arr)\n      value_map = Enum.with_index(arr)\n\
        \      |> Enum.reduce(%{}, fn {val, idx}, acc ->\n        Map.update(acc, val,\
        \ [idx], &[idx | &1])\n      end)\n      bfs(:queue.from_list([{0, 0}]), %{0\
        \ => true}, value_map, arr_tuple, n)\n    end\n  end\n\n  defp bfs(q, visited,\
        \ val_map, arr_tuple, n) do\n    {{:value, {i, steps}}, q} = :queue.out(q)\n\
        \    if i == n - 1 do\n      steps\n    else\n      val = elem(arr_tuple, i)\n\
        \      {indices, val_map} = Map.pop(val_map, val, [])\n      neighbors = [i\
        \ + 1, i - 1 | indices]\n      {q, visited} = Enum.reduce(neighbors, {q, visited},\
        \ fn nxt, {acc_q, acc_v} ->\n        if nxt >= 0 and nxt < n and not Map.has_key?(acc_v,\
        \ nxt) do\n          {:queue.in({nxt, steps + 1}, acc_q), Map.put(acc_v, nxt,\
        \ true)}\n        else\n          {acc_q, acc_v}\n        end\n      end)\n\
        \      bfs(q, visited, val_map, arr_tuple, n)\n    end\n  end\nend"
    approach: 'The problem is modeled as a shortest path search on a graph where each
      index is a node and valid jumps are edges. Since all edge weights are equal (each
      jump costs 1 step), Breadth-First Search (BFS) is the optimal strategy to find
      the minimum distance from the first index to the last. We pre-process the input
      array into a hash map that maps each unique value to a list of its indices. This
      allows us to efficiently find all potential ''jump-to-same-value'' targets for
      any given index during the BFS traversal.


      To ensure the algorithm runs in linear time, we maintain a visited set or boolean
      array to avoid processing the same index multiple times. A crucial optimization
      is clearing the list of indices for a specific value in the hash map immediately
      after it has been explored for the first time. This prevents redundant $O(N)$
      scans of index lists when multiple indices share the same value, ensuring that
      each node and edge in the implicit graph is visited at most once. Without this
      optimization, the complexity could degenerate to $O(N^2)$ in cases where many
      elements have identical values.'
    time_complexity: O(N) where N is the length of the array. Each index is added to
      and removed from the BFS queue exactly once. The same-value list clearing optimization
      ensures that every index in the hash map is also iterated over at most once throughout
      the entire execution.
    space_complexity: O(N) to store the hash map of indices, the boolean visited array,
      and the BFS queue, all of which occupy space proportional to the number of elements
      in the input array.
    elapsed_time: 241.3611171245575
    model: gemini-3-flash-preview
    generated_at: '2026-05-18 02:42:16 '
---

## Problem #1345: Jump Game IV

**Difficulty:** Hard

**Topics:** Array, Hash Table, Breadth-First Search

## Problem Description

<p>Given an array of&nbsp;integers <code>arr</code>, you are initially positioned at the first index of the array.</p>

<p>In one step you can jump from index <code>i</code> to index:</p>

<ul>
	<li><code>i + 1</code> where:&nbsp;<code>i + 1 &lt; arr.length</code>.</li>
	<li><code>i - 1</code> where:&nbsp;<code>i - 1 &gt;= 0</code>.</li>
	<li><code>j</code> where: <code>arr[i] == arr[j]</code> and <code>i != j</code>.</li>
</ul>

<p>Return <em>the minimum number of steps</em> to reach the <strong>last index</strong> of the array.</p>

<p>Notice that you can not jump outside of the array at any time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [100,-23,-23,404,100,23,23,23,3,404]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You need three jumps from index 0 --&gt; 4 --&gt; 3 --&gt; 9. Note that index 9 is the last index of the array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [7]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Start index is the last index. You do not need to jump.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [7,6,9,6,9,6,9,7]
<strong>Output:</strong> 1
<strong>Explanation:</strong> You can jump directly from index 0 to index 7 which is last index of the array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>8</sup> &lt;= arr[i] &lt;= 10<sup>8</sup></code></li>
</ul>


## Hints

1. Build a graph of n nodes where nodes are the indices of the array and edges for node i are nodes i+1, i-1, j where arr[i] == arr[j].

2. Start bfs from node 0 and keep distance. The answer is the distance when you reach node n-1.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is modeled as a shortest path search on a graph where each index is a node and valid jumps are edges. Since all edge weights are equal (each jump costs 1 step), Breadth-First Search (BFS) is the optimal strategy to find the minimum distance from the first index to the last. We pre-process the input array into a hash map that maps each unique value to a list of its indices. This allows us to efficiently find all potential 'jump-to-same-value' targets for any given index during the BFS traversal.

To ensure the algorithm runs in linear time, we maintain a visited set or boolean array to avoid processing the same index multiple times. A crucial optimization is clearing the list of indices for a specific value in the hash map immediately after it has been explored for the first time. This prevents redundant $O(N)$ scans of index lists when multiple indices share the same value, ensuring that each node and edge in the implicit graph is visited at most once. Without this optimization, the complexity could degenerate to $O(N^2)$ in cases where many elements have identical values.

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
    int minJumps(vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) return 0;

        unordered_map<int, vector<int>> adj;
        for (int i = 0; i < n; i++) {
            adj[arr[i]].push_back(i);
        }

        vector<bool> visited(n, false);
        queue<int> q;

        q.push(0);
        visited[0] = true;
        int steps = 0;

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int curr = q.front();
                q.pop();

                if (curr == n - 1) return steps;

                vector<int>& nextIndices = adj[arr[curr]];
                nextIndices.push_back(curr - 1);
                nextIndices.push_back(curr + 1);

                for (int next : nextIndices) {
                    if (next >= 0 && next < n && !visited[next]) {
                        visited[next] = true;
                        q.push(next);
                    }
                }
                nextIndices.clear();
            }
            steps++;
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
class Solution {
    public int minJumps(int[] arr) {
        int n = arr.length;
        if (n <= 1) return 0;

        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int i = 0; i < n; i++) {
            adj.computeIfAbsent(arr[i], x -> new ArrayList<>()).add(i);
        }

        boolean[] visited = new boolean[n];
        Queue<Integer> q = new LinkedList<>();

        q.offer(0);
        visited[0] = true;
        int steps = 0;

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int curr = q.poll();

                if (curr == n - 1) return steps;

                List<Integer> nextIndices = adj.get(arr[curr]);
                if (nextIndices != null) {
                    nextIndices.add(curr - 1);
                    nextIndices.add(curr + 1);
                    for (int next : nextIndices) {
                        if (next >= 0 && next < n && !visited[next]) {
                            visited[next] = true;
                            q.offer(next);
                        }
                    }
                    adj.remove(arr[curr]);
                } else {
                    int[] simpleNext = {curr - 1, curr + 1};
                    for (int next : simpleNext) {
                        if (next >= 0 && next < n && !visited[next]) {
                            visited[next] = true;
                            q.offer(next);
                        }
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

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
from collections import deque, defaultdict

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n <= 1:
            return 0

        adj = defaultdict(list)
        for i, val in enumerate(arr):
            adj[val].append(i)

        q = deque([0])
        visited = {0}
        steps = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == n - 1:
                    return steps

                for next_idx in adj[arr[curr]]:
                    if next_idx not in visited:
                        visited.add(next_idx)
                        q.append(next_idx)

                adj[arr[curr]] = []

                for next_idx in [curr - 1, curr + 1]:
                    if 0 <= next_idx < n and next_idx not in visited:
                        visited.add(next_idx)
                        q.append(next_idx)

            steps += 1

        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = collections.defaultdict(list)
        for i, x in enumerate(arr):
            graph[x].append(i)

        queue = collections.deque([0])
        visited = [False] * n
        visited[0] = True
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == n - 1:
                    return steps

                val = arr[curr]
                if val in graph:
                    for neighbor in graph[val]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                    del graph[val]

                if curr + 1 < n and not visited[curr + 1]:
                    visited[curr + 1] = True
                    queue.append(curr + 1)

                if curr - 1 >= 0 and not visited[curr - 1]:
                    visited[curr - 1] = True
                    queue.append(curr - 1)
            steps += 1
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    int val;
    int idx;
} Pair;

int compare(const void* a, const void* b) {
    Pair* p1 = (Pair*)a;
    Pair* p2 = (Pair*)b;
    if (p1->val < p2->val) return -1;
    if (p1->val > p2->val) return 1;
    return 0;
}

int find_first(Pair* pairs, int n, int val) {
    int l = 0, r = n - 1, ans = -1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (pairs[mid].val == val) {
            ans = mid;
            r = mid - 1;
        } else if (pairs[mid].val < val) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return ans;
}

int minJumps(int* arr, int arrSize) {
    if (arrSize <= 1) return 0;

    Pair* pairs = (Pair*)malloc(arrSize * sizeof(Pair));
    for (int i = 0; i < arrSize; i++) {
        pairs[i].val = arr[i];
        pairs[i].idx = i;
    }
    qsort(pairs, arrSize, sizeof(Pair), compare);

    int* q = (int*)malloc(arrSize * sizeof(int));
    int* dist = (int*)malloc(arrSize * sizeof(int));
    bool* val_processed = (bool*)calloc(arrSize, sizeof(bool));
    int* v_start_map = (int*)malloc(arrSize * sizeof(int));

    for (int i = 0; i < arrSize; i++) {
        dist[i] = -1;
        v_start_map[i] = find_first(pairs, arrSize, arr[i]);
    }

    int head = 0, tail = 0;
    dist[0] = 0;
    q[tail++] = 0;

    while (head < tail) {
        int curr = q[head++];
        int d = dist[curr];

        if (curr == arrSize - 1) {
            free(pairs); free(q); free(dist); free(val_processed); free(v_start_map);
            return d;
        }

        if (curr + 1 < arrSize && dist[curr + 1] == -1) {
            dist[curr + 1] = d + 1;
            q[tail++] = curr + 1;
        }
        if (curr - 1 >= 0 && dist[curr - 1] == -1) {
            dist[curr - 1] = d + 1;
            q[tail++] = curr - 1;
        }

        int v_start = v_start_map[curr];
        if (!val_processed[v_start]) {
            for (int k = v_start; k < arrSize && pairs[k].val == arr[curr]; k++) {
                int neighbor = pairs[k].idx;
                if (dist[neighbor] == -1) {
                    dist[neighbor] = d + 1;
                    q[tail++] = neighbor;
                }
            }
            val_processed[v_start] = true;
        }
    }

    free(pairs); free(q); free(dist); free(val_processed); free(v_start_map);
    return -1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int MinJumps(int[] arr) {
        int n = arr.Length;
        if (n <= 1) return 0;

        Dictionary<int, List<int>> graph = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!graph.ContainsKey(arr[i])) {
                graph[arr[i]] = new List<int>();
            }
            graph[arr[i]].Add(i);
        }

        Queue<int> queue = new Queue<int>();
        bool[] visited = new bool[n];
        queue.Enqueue(0);
        visited[0] = true;
        int steps = 0;

        while (queue.Count > 0) {
            int size = queue.Count;
            for (int i = 0; i < size; i++) {
                int curr = queue.Dequeue();
                if (curr == n - 1) return steps;

                int val = arr[curr];
                if (graph.ContainsKey(val)) {
                    foreach (int neighbor in graph[val]) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true;
                            queue.Enqueue(neighbor);
                        }
                    }
                    graph.Remove(val);
                }

                if (curr + 1 < n && !visited[curr + 1]) {
                    visited[curr + 1] = true;
                    queue.Enqueue(curr + 1);
                }
                if (curr - 1 >= 0 && !visited[curr - 1]) {
                    visited[curr - 1] = true;
                    queue.Enqueue(curr - 1);
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
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function(arr) {
    const n = arr.length;
    if (n <= 1) return 0;

    const graph = new Map();
    for (let i = 0; i < n; i++) {
        if (!graph.has(arr[i])) {
            graph.set(arr[i], []);
        }
        graph.get(arr[i]).push(i);
    }

    const queue = [0];
    const visited = new Uint8Array(n);
    visited[0] = 1;
    let head = 0;
    let steps = 0;

    while (head < queue.length) {
        let size = queue.length - head;
        for (let i = 0; i < size; i++) {
            const curr = queue[head++];
            if (curr === n - 1) return steps;

            const val = arr[curr];
            if (graph.has(val)) {
                const neighbors = graph.get(val);
                for (let j = 0; j < neighbors.length; j++) {
                    const neighbor = neighbors[j];
                    if (!visited[neighbor]) {
                        visited[neighbor] = 1;
                        queue.push(neighbor);
                    }
                }
                graph.delete(val);
            }

            if (curr + 1 < n && !visited[curr + 1]) {
                visited[curr + 1] = 1;
                queue.push(curr + 1);
            }
            if (curr - 1 >= 0 && !visited[curr - 1]) {
                visited[curr - 1] = 1;
                queue.push(curr - 1);
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
function minJumps(arr: number[]): number {
    const n = arr.length;
    if (n <= 1) return 0;

    const map = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        if (!map.has(arr[i])) {
            map.set(arr[i], []);
        }
        map.get(arr[i])!.push(i);
    }

    let steps = 0;
    let queue = [0];
    const visited = new Uint8Array(n);
    visited[0] = 1;

    while (queue.length > 0) {
        const nextQueue: number[] = [];
        for (const node of queue) {
            if (node === n - 1) return steps;

            const val = arr[node];
            const indices = map.get(val);
            if (indices) {
                for (const idx of indices) {
                    if (!visited[idx]) {
                        visited[idx] = 1;
                        nextQueue.push(idx);
                    }
                }
                map.delete(val);
            }

            if (node + 1 < n && !visited[node + 1]) {
                visited[node + 1] = 1;
                nextQueue.push(node + 1);
            }

            if (node - 1 >= 0 && !visited[node - 1]) {
                visited[node - 1] = 1;
                nextQueue.push(node - 1);
            }
        }
        queue = nextQueue;
        steps++;
    }

    return steps;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function minJumps($arr) {
        $n = count($arr);
        if ($n <= 1) return 0;

        $map = [];
        foreach ($arr as $i => $val) {
            $map[$val][] = $i;
        }

        $visited = array_fill(0, $n, false);
        $visited[0] = true;
        $queue = new SplQueue();
        $queue->enqueue(0);
        $steps = 0;

        while (!$queue->isEmpty()) {
            $size = $queue->count();
            for ($i = 0; $i < $size; $i++) {
                $curr = $queue->dequeue();

                if ($curr == $n - 1) return $steps;

                $val = $arr[$curr];
                if (isset($map[$val])) {
                    foreach ($map[$val] as $next) {
                        if (!$visited[$next]) {
                            $visited[$next] = true;
                            $queue->enqueue($next);
                        }
                    }
                    unset($map[$val]);
                }

                if ($curr + 1 < $n && !$visited[$curr + 1]) {
                    $visited[$curr + 1] = true;
                    $queue->enqueue($curr + 1);
                }

                if ($curr - 1 >= 0 && !$visited[$curr - 1]) {
                    $visited[$curr - 1] = true;
                    $queue->enqueue($curr - 1);
                }
            }
            $steps++;
        }

        return $steps;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minJumps(_ arr: [Int]) -> Int {
        let n = arr.count
        if n <= 1 { return 0 }

        var map = [Int: [Int]]()
        for (i, val) in arr.enumerated() {
            map[val, default: []].append(i)
        }

        var visited = Array(repeating: false, count: n)
        visited[0] = true
        var queue = [0]
        var steps = 0

        while !queue.isEmpty {
            var nextQueue = [Int]()
            for curr in queue {
                if curr == n - 1 { return steps }

                let val = arr[curr]
                if let sameValIndices = map[val] {
                    for next in sameValIndices {
                        if !visited[next] {
                            visited[next] = true
                            nextQueue.append(next)
                        }
                    }
                    map.removeValue(forKey: val)
                }

                if curr + 1 < n && !visited[curr + 1] {
                    visited[curr + 1] = true
                    nextQueue.append(curr + 1)
                }

                if curr - 1 >= 0 && !visited[curr - 1] {
                    visited[curr - 1] = true
                    nextQueue.append(curr - 1)
                }
            }
            queue = nextQueue
            steps += 1
        }

        return steps
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.*

class Solution {
    fun minJumps(arr: IntArray): Int {
        val n = arr.size
        if (n <= 1) return 0

        val map = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            map.computeIfAbsent(arr[i]) { mutableListOf<Int>() }.add(i)
        }

        val visited = BooleanArray(n)
        visited[0] = true
        val queue = java.util.ArrayDeque<Int>()
        queue.add(0)
        var steps = 0

        while (queue.isNotEmpty()) {
            val size = queue.size
            for (i in 0 until size) {
                val curr = queue.removeFirst()

                if (curr == n - 1) return steps

                val valAtCurr = arr[curr]
                if (map.containsKey(valAtCurr)) {
                    val sameValIndices = map[valAtCurr]!!
                    for (next in sameValIndices) {
                        if (!visited[next]) {
                            visited[next] = true
                            queue.addLast(next)
                        }
                    }
                    map.remove(valAtCurr)
                }

                if (curr + 1 < n && !visited[curr + 1]) {
                    visited[curr + 1] = true
                    queue.addLast(curr + 1)
                }

                if (curr - 1 >= 0 && !visited[curr - 1]) {
                    visited[curr - 1] = true
                    queue.addLast(curr - 1)
                }
            }
            steps++
        }

        return steps
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minJumps(List<int> arr) {
    int n = arr.length;
    if (n <= 1) return 0;

    Map<int, List<int>> graph = {};
    for (int i = 0; i < n; i++) {
      if (!graph.containsKey(arr[i])) {
        graph[arr[i]] = [];
      }
      graph[arr[i]]!.add(i);
    }

    List<int> queue = [0];
    List<bool> visited = List.filled(n, false);
    visited[0] = true;
    int steps = 0;

    while (queue.isNotEmpty) {
      List<int> nextQueue = [];
      for (int curr in queue) {
        if (curr == n - 1) return steps;

        int val = arr[curr];
        if (graph.containsKey(val)) {
          for (int nextIdx in graph[val]!) {
            if (!visited[nextIdx]) {
              visited[nextIdx] = true;
              nextQueue.add(nextIdx);
            }
          }
          graph.remove(val);
        }

        if (curr + 1 < n && !visited[curr + 1]) {
          visited[curr + 1] = true;
          nextQueue.add(curr + 1);
        }
        if (curr - 1 >= 0 && !visited[curr - 1]) {
          visited[curr - 1] = true;
          nextQueue.add(curr - 1);
        }
      }
      queue = nextQueue;
      steps++;
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
func minJumps(arr []int) int {
	n := len(arr)
	if n <= 1 {
		return 0
	}

	graph := make(map[int][]int)
	for i, val := range arr {
		graph[val] = append(graph[val], i)
	}

	queue := []int{0}
	visited := make([]bool, n)
	visited[0] = true
	steps := 0

	for len(queue) > 0 {
		size := len(queue)
		for i := 0; i < size; i++ {
			curr := queue[i]
			if curr == n-1 {
				return steps
			}

			val := arr[curr]
			if indices, ok := graph[val]; ok {
				for _, nextIdx := range indices {
					if !visited[nextIdx] {
						visited[nextIdx] = true
						queue = append(queue, nextIdx)
					}
				}
				delete(graph, val)
			}

			if curr+1 < n && !visited[curr+1] {
				visited[curr+1] = true
				queue = append(queue, curr+1)
			}
			if curr-1 >= 0 && !visited[curr-1] {
				visited[curr-1] = true
				queue = append(queue, curr-1)
			}
		}
		queue = queue[size:]
		steps++
	}

	return -1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} arr
# @return {Integer}
def min_jumps(arr)
  n = arr.length
  return 0 if n <= 1

  graph = Hash.new { |h, k| h[k] = [] }
  arr.each_with_index { |val, i| graph[val] << i }

  queue = [0]
  visited = Array.new(n, false)
  visited[0] = true
  steps = 0

  while !queue.empty?
    next_queue = []
    queue.each do |curr|
      return steps if curr == n - 1

      val = arr[curr]
      if graph.key?(val)
        graph[val].each do |next_idx|
          unless visited[next_idx]
            visited[next_idx] = true
            next_queue << next_idx
          end
        end
        graph.delete(val)
      end

      if curr + 1 < n && !visited[curr + 1]
        visited[curr + 1] = true
        next_queue << curr + 1
      end
      if curr - 1 >= 0 && !visited[curr - 1]
        visited[curr - 1] = true
        next_queue << curr - 1
      end
    end
    queue = next_queue
    steps += 1
  end

  steps
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
  def minJumps(arr: Array[Int]): Int = {
    val n = arr.length
    if (n <= 1) return 0

    val graph = new mutable.HashMap[Int, mutable.ArrayBuffer[Int]]()
    var i = 0
    while (i < n) {
      val value = arr(i)
      if (!graph.contains(value)) {
        graph(value) = new mutable.ArrayBuffer[Int]()
      }
      graph(value) += i
      i += 1
    }

    var queue = mutable.ArrayBuffer[Int](0)
    val visited = new Array[Boolean](n)
    visited(0) = true
    var steps = 0

    while (queue.nonEmpty) {
      val nextQueue = new mutable.ArrayBuffer[Int]()
      var qIdx = 0
      while (qIdx < queue.length) {
        val curr = queue(qIdx)
        if (curr == n - 1) return steps

        val value = arr(curr)
        if (graph.contains(value)) {
          val indices = graph(value)
          var j = 0
          while (j < indices.length) {
            val nextIdx = indices(j)
            if (!visited(nextIdx)) {
              visited(nextIdx) = true
              nextQueue += nextIdx
            }
            j += 1
          }
          graph.remove(value)
        }

        if (curr + 1 < n && !visited(curr + 1)) {
          visited(curr + 1) = true
          nextQueue += (curr + 1)
        }
        if (curr - 1 >= 0 && !visited(curr - 1)) {
          visited(curr - 1) = true
          nextQueue += (curr - 1)
        }
        qIdx += 1
      }
      queue = nextQueue
      steps += 1
    }

    steps
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::{HashMap, VecDeque};

impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        if n <= 1 {
            return 0;
        }

        let mut map: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &v) in arr.iter().enumerate() {
            map.entry(v).or_default().push(i);
        }

        let mut q = VecDeque::new();
        let mut visited = vec![false; n];
        q.push_back(0);
        visited[0] = true;

        let mut steps = 0;
        while !q.is_empty() {
            let size = q.len();
            for _ in 0..size {
                let i = q.pop_front().unwrap();
                if i == n - 1 {
                    return steps;
                }

                let val = arr[i];
                if let Some(indices) = map.remove(&val) {
                    for j in indices {
                        if !visited[j] {
                            visited[j] = true;
                            q.push_back(j);
                        }
                    }
                }

                if i + 1 < n && !visited[i + 1] {
                    visited[i + 1] = true;
                    q.push_back(i + 1);
                }

                if i > 0 && !visited[i - 1] {
                    visited[i - 1] = true;
                    q.push_back(i - 1);
                }
            }
            steps += 1;
        }
        steps
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-jumps arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length arr)]
         [arr-vec (list->vector arr)])
    (if (<= n 1)
        0
        (let/ec return
          (let ([val-map (make-hash)])
            (for ([i (in-range n)])
              (let ([val (vector-ref arr-vec i)])
                (hash-set! val-map val (cons i (hash-ref val-map val '())))))
            (let ([visited (make-vector n #f)])
              (vector-set! visited 0 #t)
              (let loop ([q (list 0)] [steps 0])
                (let ([next-level '()])
                  (for ([i q])
                    (if (= i (- n 1))
                        (return steps)
                        (let* ([val (vector-ref arr-vec i)]
                               [indices (hash-ref val-map val '())])
                          (hash-remove! val-map val)
                          (for ([nxt (list* (+ i 1) (- i 1) indices)])
                            (when (and (>= nxt 0) (< nxt n) (not (vector-ref visited nxt)))
                              (vector-set! visited nxt #t)
                              (set! next-level (cons nxt next-level)))))))
                  (loop (reverse next-level) (+ steps 1)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_jumps(Arr :: [integer()]) -> integer().
min_jumps(Arr) ->
    N = length(Arr),
    if N =:= 1 -> 0;
       true ->
           ArrTuple = list_to_tuple(Arr),
           ValueMap = build_map(Arr, 1, #{}),
           Queue = queue:in({1, 0}, queue:new()),
           Visited = #{1 => true},
           bfs(Queue, Visited, ValueMap, ArrTuple, N)
    end.

build_map([], _, Map) -> Map;
build_map([H|T], I, Map) ->
    Indices = maps:get(H, Map, []),
    build_map(T, I + 1, Map#{H => [I | Indices]}).

bfs(Queue, Visited, ValueMap, ArrTuple, N) ->
    {{value, {I, Steps}}, Q1} = queue:out(Queue),
    if I =:= N -> Steps;
       true ->
           Val = element(I, ArrTuple),
           {ValueNeighbors, NewValueMap} = case maps:find(Val, ValueMap) of
               {ok, List} -> {List, maps:remove(Val, ValueMap)};
               error -> {[], ValueMap}
           end,
           Neighbors = [I + 1, I - 1 | ValueNeighbors],
           {NewQ, NewVisited} = add_neighbors(Neighbors, Q1, Visited, N, Steps + 1),
           bfs(NewQ, NewVisited, NewValueMap, ArrTuple, N)
    end.

add_neighbors([], Q, V, _, _) -> {Q, V};
add_neighbors([H|T], Q, V, N, S) ->
    case (H >= 1) and (H =< N) andalso not maps:is_key(H, V) of
        true -> add_neighbors(T, queue:in({H, S}, Q), V#{H => true}, N, S);
        false -> add_neighbors(T, Q, V, N, S)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_jumps(arr :: [integer]) :: integer
  def min_jumps(arr) do
    n = length(arr)
    if n <= 1 do
      0
    else
      arr_tuple = List.to_tuple(arr)
      value_map = Enum.with_index(arr)
      |> Enum.reduce(%{}, fn {val, idx}, acc ->
        Map.update(acc, val, [idx], &[idx | &1])
      end)
      bfs(:queue.from_list([{0, 0}]), %{0 => true}, value_map, arr_tuple, n)
    end
  end

  defp bfs(q, visited, val_map, arr_tuple, n) do
    {{:value, {i, steps}}, q} = :queue.out(q)
    if i == n - 1 do
      steps
    else
      val = elem(arr_tuple, i)
      {indices, val_map} = Map.pop(val_map, val, [])
      neighbors = [i + 1, i - 1 | indices]
      {q, visited} = Enum.reduce(neighbors, {q, visited}, fn nxt, {acc_q, acc_v} ->
        if nxt >= 0 and nxt < n and not Map.has_key?(acc_v, nxt) do
          {:queue.in({nxt, steps + 1}, acc_q), Map.put(acc_v, nxt, true)}
        else
          {acc_q, acc_v}
        end
      end)
      bfs(q, visited, val_map, arr_tuple, n)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the array. Each index is added to and removed from the BFS queue exactly once. The same-value list clearing optimization ensures that every index in the hash map is also iterated over at most once throughout the entire execution.
- **Space Complexity:** O(N) to store the hash map of indices, the boolean visited array, and the BFS queue, all of which occupy space proportional to the number of elements in the input array.
