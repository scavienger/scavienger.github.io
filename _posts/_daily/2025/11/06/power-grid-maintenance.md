---
layout: post
title: "Power Grid Maintenance"
date: 2025-11-06 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Depth-First Search", "Breadth-First Search", "Union-Find", "Graph Theory", "Heap (Priority Queue)", "Ordered Set"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/power-grid-maintenance/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <queue>\nusing namespace std;\n\nclass Solution\
        \ {\npublic:\n    vector<int> processQueries(int c, vector<vector<int>>& connections,\
        \ vector<vector<int>>& queries) {\n        vector<vector<int>> graph(c + 1);\n\
        \        for (const auto& edge : connections) {\n            graph[edge[0]].push_back(edge[1]);\n\
        \            graph[edge[1]].push_back(edge[0]);\n        }\n\n        vector<int>\
        \ component(c + 1, -1);\n        vector<priority_queue<int, vector<int>, greater<int>>>\
        \ heaps;\n        for (int station = 1; station <= c; ++station) {\n       \
        \     if (component[station] != -1) continue;\n            int id = static_cast<int>(heaps.size());\n\
        \            heaps.emplace_back();\n            vector<int> stack = {station};\n\
        \            component[station] = id;\n            while (!stack.empty()) {\n\
        \                int node = stack.back();\n                stack.pop_back();\n\
        \                heaps[id].push(node);\n                for (int next : graph[node])\
        \ {\n                    if (component[next] == -1) {\n                    \
        \    component[next] = id;\n                        stack.push_back(next);\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    vector<char> online(c + 1, true);\n        vector<int> result;\n      \
        \  for (const auto& query : queries) {\n            int type = query[0];\n \
        \           int station = query[1];\n            if (type == 2) {\n        \
        \        online[station] = false;\n            } else if (online[station]) {\n\
        \                result.push_back(station);\n            } else {\n        \
        \        auto& heap = heaps[component[station]];\n                while (!heap.empty()\
        \ && !online[heap.top()]) heap.pop();\n                result.push_back(heap.empty()\
        \ ? -1 : heap.top());\n            }\n        }\n        return result;\n  \
        \  }\n};"
      java: "import java.util.ArrayDeque;\nimport java.util.ArrayList;\nimport java.util.List;\n\
        import java.util.PriorityQueue;\n\nclass Solution {\n    public int[] processQueries(int\
        \ c, int[][] connections, int[][] queries) {\n        List<Integer>[] graph\
        \ = new ArrayList[c + 1];\n        for (int i = 1; i <= c; i++) graph[i] = new\
        \ ArrayList<>();\n        for (int[] edge : connections) {\n            graph[edge[0]].add(edge[1]);\n\
        \            graph[edge[1]].add(edge[0]);\n        }\n\n        int[] component\
        \ = new int[c + 1];\n        java.util.Arrays.fill(component, -1);\n       \
        \ List<PriorityQueue<Integer>> heaps = new ArrayList<>();\n        for (int\
        \ station = 1; station <= c; station++) {\n            if (component[station]\
        \ != -1) continue;\n            int id = heaps.size();\n            PriorityQueue<Integer>\
        \ heap = new PriorityQueue<>();\n            heaps.add(heap);\n            ArrayDeque<Integer>\
        \ stack = new ArrayDeque<>();\n            stack.push(station);\n          \
        \  component[station] = id;\n            while (!stack.isEmpty()) {\n      \
        \          int node = stack.pop();\n                heap.offer(node);\n    \
        \            for (int next : graph[node]) {\n                    if (component[next]\
        \ == -1) {\n                        component[next] = id;\n                \
        \        stack.push(next);\n                    }\n                }\n     \
        \       }\n        }\n\n        boolean[] online = new boolean[c + 1];\n   \
        \     java.util.Arrays.fill(online, true);\n        int[] result = new int[queries.length];\n\
        \        int size = 0;\n        for (int[] query : queries) {\n            int\
        \ type = query[0];\n            int station = query[1];\n            if (type\
        \ == 2) {\n                online[station] = false;\n            } else if (online[station])\
        \ {\n                result[size++] = station;\n            } else {\n     \
        \           PriorityQueue<Integer> heap = heaps.get(component[station]);\n \
        \               while (!heap.isEmpty() && !online[heap.peek()]) heap.poll();\n\
        \                result[size++] = heap.isEmpty() ? -1 : heap.peek();\n     \
        \       }\n        }\n        return java.util.Arrays.copyOf(result, size);\n\
        \    }\n}"
      python: "class Solution(object):\n    def processQueries(self, c, connections,\
        \ queries):\n        \"\"\"\n        :type c: int\n        :type connections:\
        \ List[List[int]]\n        :type queries: List[List[int]]\n        :rtype: List[int]\n\
        \        \"\"\"\n        import heapq\n\n        graph = [[] for _ in range(c\
        \ + 1)]\n        for u, v in connections:\n            graph[u].append(v)\n\
        \            graph[v].append(u)\n\n        component = [-1] * (c + 1)\n    \
        \    heaps = []\n        for station in range(1, c + 1):\n            if component[station]\
        \ != -1:\n                continue\n            component_id = len(heaps)\n\
        \            heap = []\n            heaps.append(heap)\n            stack =\
        \ [station]\n            component[station] = component_id\n            while\
        \ stack:\n                node = stack.pop()\n                heapq.heappush(heap,\
        \ node)\n                for neighbor in graph[node]:\n                    if\
        \ component[neighbor] == -1:\n                        component[neighbor] =\
        \ component_id\n                        stack.append(neighbor)\n\n        online\
        \ = [True] * (c + 1)\n        result = []\n        for query_type, station in\
        \ queries:\n            if query_type == 2:\n                online[station]\
        \ = False\n            elif online[station]:\n                result.append(station)\n\
        \            else:\n                heap = heaps[component[station]]\n     \
        \           while heap and not online[heap[0]]:\n                    heapq.heappop(heap)\n\
        \                result.append(heap[0] if heap else -1)\n        return result"
      python3: "from typing import List\nimport heapq\n\nclass Solution:\n    def processQueries(self,\
        \ c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:\n\
        \        graph = [[] for _ in range(c + 1)]\n        for u, v in connections:\n\
        \            graph[u].append(v)\n            graph[v].append(u)\n\n        component\
        \ = [-1] * (c + 1)\n        heaps = []\n        for station in range(1, c +\
        \ 1):\n            if component[station] != -1:\n                continue\n\
        \            component_id = len(heaps)\n            heap = []\n            heaps.append(heap)\n\
        \            stack = [station]\n            component[station] = component_id\n\
        \            while stack:\n                node = stack.pop()\n            \
        \    heapq.heappush(heap, node)\n                for neighbor in graph[node]:\n\
        \                    if component[neighbor] == -1:\n                       \
        \ component[neighbor] = component_id\n                        stack.append(neighbor)\n\
        \n        online = [True] * (c + 1)\n        result = []\n        for query_type,\
        \ station in queries:\n            if query_type == 2:\n                online[station]\
        \ = False\n            elif online[station]:\n                result.append(station)\n\
        \            else:\n                heap = heaps[component[station]]\n     \
        \           while heap and not online[heap[0]]:\n                    heapq.heappop(heap)\n\
        \                result.append(heap[0] if heap else -1)\n        return result"
      c: "#include <stdlib.h>\n\nint* processQueries(int c, int** connections, int connectionsSize,\
        \ int* connectionsColSize, int** queries, int queriesSize, int* queriesColSize,\
        \ int* returnSize) {\n    int* degree = (int*)calloc(c + 1, sizeof(int));\n\
        \    for (int i = 0; i < connectionsSize; i++) {\n        degree[connections[i][0]]++;\n\
        \        degree[connections[i][1]]++;\n    }\n\n    int** graph = (int**)malloc((c\
        \ + 1) * sizeof(int*));\n    int* position = (int*)calloc(c + 1, sizeof(int));\n\
        \    for (int i = 0; i <= c; i++) graph[i] = (int*)malloc((degree[i] ? degree[i]\
        \ : 1) * sizeof(int));\n    for (int i = 0; i < connectionsSize; i++) {\n  \
        \      int u = connections[i][0];\n        int v = connections[i][1];\n    \
        \    graph[u][position[u]++] = v;\n        graph[v][position[v]++] = u;\n  \
        \  }\n\n    int* component = (int*)malloc((c + 1) * sizeof(int));\n    for (int\
        \ i = 0; i <= c; i++) component[i] = -1;\n    int** heaps = (int**)malloc((c\
        \ + 1) * sizeof(int*));\n    int* heapSize = (int*)calloc(c + 1, sizeof(int));\n\
        \    int* stack = (int*)malloc((c + 1) * sizeof(int));\n    int componentCount\
        \ = 0;\n\n    for (int station = 1; station <= c; station++) {\n        if (component[station]\
        \ != -1) continue;\n        int id = componentCount++;\n        heaps[id] =\
        \ (int*)malloc((c + 1) * sizeof(int));\n        int top = 0;\n        stack[top++]\
        \ = station;\n        component[station] = id;\n        while (top > 0) {\n\
        \            int node = stack[--top];\n            int size = ++heapSize[id];\n\
        \            int index = size;\n            while (index > 1 && node < heaps[id][index\
        \ / 2]) {\n                heaps[id][index] = heaps[id][index / 2];\n      \
        \          index /= 2;\n            }\n            heaps[id][index] = node;\n\
        \            for (int j = 0; j < degree[node]; j++) {\n                int next\
        \ = graph[node][j];\n                if (component[next] == -1) {\n        \
        \            component[next] = id;\n                    stack[top++] = next;\n\
        \                }\n            }\n        }\n    }\n\n    char* online = (char*)malloc((c\
        \ + 1) * sizeof(char));\n    for (int i = 0; i <= c; i++) online[i] = 1;\n \
        \   int* result = (int*)malloc(queriesSize * sizeof(int));\n    int resultCount\
        \ = 0;\n\n    for (int i = 0; i < queriesSize; i++) {\n        int type = queries[i][0];\n\
        \        int station = queries[i][1];\n        if (type == 2) {\n          \
        \  online[station] = 0;\n        } else if (online[station]) {\n           \
        \ result[resultCount++] = station;\n        } else {\n            int id = component[station];\n\
        \            while (heapSize[id] > 0 && !online[heaps[id][1]]) {\n         \
        \       int last = heaps[id][heapSize[id]--];\n                if (heapSize[id]\
        \ == 0) continue;\n                int index = 1;\n                while (index\
        \ * 2 <= heapSize[id]) {\n                    int child = index * 2;\n     \
        \               if (child + 1 <= heapSize[id] && heaps[id][child + 1] < heaps[id][child])\
        \ child++;\n                    if (heaps[id][child] >= last) break;\n     \
        \               heaps[id][index] = heaps[id][child];\n                    index\
        \ = child;\n                }\n                heaps[id][index] = last;\n  \
        \          }\n            result[resultCount++] = heapSize[id] == 0 ? -1 : heaps[id][1];\n\
        \        }\n    }\n\n    *returnSize = resultCount;\n    return result;\n}"
      csharp: "public class Solution {\n    public int[] ProcessQueries(int c, int[][]\
        \ connections, int[][] queries) {\n        var graph = new List<int>[c + 1];\n\
        \        for (int i = 0; i <= c; i++) graph[i] = new List<int>();\n        foreach\
        \ (var edge in connections) {\n            graph[edge[0]].Add(edge[1]);\n  \
        \          graph[edge[1]].Add(edge[0]);\n        }\n\n        int[] component\
        \ = new int[c + 1];\n        Array.Fill(component, -1);\n        var heaps =\
        \ new List<PriorityQueue<int, int>>();\n        for (int station = 1; station\
        \ <= c; station++) {\n            if (component[station] != -1) continue;\n\
        \            int componentId = heaps.Count;\n            var heap = new PriorityQueue<int,\
        \ int>();\n            heaps.Add(heap);\n            var stack = new Stack<int>();\n\
        \            stack.Push(station);\n            component[station] = componentId;\n\
        \            while (stack.Count > 0) {\n                int node = stack.Pop();\n\
        \                heap.Enqueue(node, node);\n                foreach (int neighbor\
        \ in graph[node]) {\n                    if (component[neighbor] == -1) {\n\
        \                        component[neighbor] = componentId;\n              \
        \          stack.Push(neighbor);\n                    }\n                }\n\
        \            }\n        }\n\n        bool[] online = new bool[c + 1];\n    \
        \    Array.Fill(online, true);\n        var result = new List<int>();\n    \
        \    foreach (var query in queries) {\n            int type = query[0];\n  \
        \          int station = query[1];\n            if (type == 2) {\n         \
        \       online[station] = false;\n            } else if (online[station]) {\n\
        \                result.Add(station);\n            } else {\n              \
        \  var heap = heaps[component[station]];\n                while (heap.Count\
        \ > 0 && !online[heap.Peek()) {\n                    heap.Dequeue();\n     \
        \           }\n                result.Add(heap.Count > 0 ? heap.Peek() : -1);\n\
        \            }\n        }\n        return result.ToArray();\n    }\n}"
      javascript: "/**\n * @param {number} c\n * @param {number[][]} connections\n *\
        \ @param {number[][]} queries\n * @return {number[]}\n */\nvar processQueries\
        \ = function(c, connections, queries) {\n    const graph = Array.from({ length:\
        \ c + 1 }, () => []);\n    for (const [u, v] of connections) {\n        graph[u].push(v);\n\
        \        graph[v].push(u);\n    }\n\n    const component = Array(c + 1).fill(-1);\n\
        \    const heaps = [];\n    for (let station = 1; station <= c; station++) {\n\
        \        if (component[station] !== -1) continue;\n        const componentId\
        \ = heaps.length;\n        const heap = [];\n        heaps.push(heap);\n   \
        \     const stack = [station];\n        component[station] = componentId;\n\
        \        while (stack.length > 0) {\n            const node = stack.pop();\n\
        \            heap.push(node);\n            for (const neighbor of graph[node])\
        \ {\n                if (component[neighbor] === -1) {\n                   \
        \ component[neighbor] = componentId;\n                    stack.push(neighbor);\n\
        \                }\n            }\n        }\n        heap.sort((a, b) => a\
        \ - b);\n    }\n\n    const online = Array(c + 1).fill(true);\n    const result\
        \ = [];\n    for (const [type, station] of queries) {\n        if (type ===\
        \ 2) {\n            online[station] = false;\n        } else if (online[station])\
        \ {\n            result.push(station);\n        } else {\n            const\
        \ heap = heaps[component[station]];\n            while (heap.length > 0 && !online[heap[0]])\
        \ heap.shift();\n            result.push(heap.length > 0 ? heap[0] : -1);\n\
        \        }\n    }\n    return result;\n};"
      typescript: "function processQueries(c: number, connections: number[][], queries:\
        \ number[][]): number[] {\n    const graph: number[][] = Array.from({ length:\
        \ c + 1 }, () => []);\n    for (const [u, v] of connections) {\n        graph[u].push(v);\n\
        \        graph[v].push(u);\n    }\n\n    const component: number[] = Array(c\
        \ + 1).fill(-1);\n    const heaps: number[][] = [];\n    for (let station =\
        \ 1; station <= c; station++) {\n        if (component[station] !== -1) continue;\n\
        \        const componentId = heaps.length;\n        const heap: number[] = [];\n\
        \        heaps.push(heap);\n        const stack = [station];\n        component[station]\
        \ = componentId;\n        while (stack.length > 0) {\n            const node\
        \ = stack.pop()!;\n            heap.push(node);\n            for (const neighbor\
        \ of graph[node]) {\n                if (component[neighbor] === -1) {\n   \
        \                 component[neighbor] = componentId;\n                    stack.push(neighbor);\n\
        \                }\n            }\n        }\n        heap.sort((a, b) => a\
        \ - b);\n    }\n\n    const online: boolean[] = Array(c + 1).fill(true);\n \
        \   const result: number[] = [];\n    for (const [type, station] of queries)\
        \ {\n        if (type === 2) {\n            online[station] = false;\n     \
        \   } else if (online[station]) {\n            result.push(station);\n     \
        \   } else {\n            const heap = heaps[component[station]];\n        \
        \    while (heap.length > 0 && !online[heap[0]]) heap.shift();\n           \
        \ result.push(heap.length > 0 ? heap[0] : -1);\n        }\n    }\n    return\
        \ result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $c\n     * @param Integer[][]\
        \ $connections\n     * @param Integer[][] $queries\n     * @return Integer[]\n\
        \     */\n    function processQueries($c, $connections, $queries) {\n      \
        \  $graph = array_fill(0, $c + 1, []);\n        foreach ($connections as $edge)\
        \ {\n            [$u, $v] = $edge;\n            $graph[$u][] = $v;\n       \
        \     $graph[$v][] = $u;\n        }\n\n        $component = array_fill(0, $c\
        \ + 1, -1);\n        $heaps = [];\n        for ($station = 1; $station <= $c;\
        \ $station++) {\n            if ($component[$station] !== -1) {\n          \
        \      continue;\n            }\n            $componentId = count($heaps);\n\
        \            $heap = new SplMinHeap();\n            $heaps[] = $heap;\n    \
        \        $stack = [$station];\n            $component[$station] = $componentId;\n\
        \            while (!empty($stack)) {\n                $node = array_pop($stack);\n\
        \                $heaps[$componentId]->insert($node);\n                foreach\
        \ ($graph[$node] as $neighbor) {\n                    if ($component[$neighbor]\
        \ === -1) {\n                        $component[$neighbor] = $componentId;\n\
        \                        $stack[] = $neighbor;\n                    }\n    \
        \            }\n            }\n        }\n\n        $online = array_fill(0,\
        \ $c + 1, true);\n        $result = [];\n        foreach ($queries as $query)\
        \ {\n            [$type, $station] = $query;\n            if ($type === 2) {\n\
        \                $online[$station] = false;\n            } elseif ($online[$station])\
        \ {\n                $result[] = $station;\n            } else {\n         \
        \       $componentId = $component[$station];\n                while (!$heaps[$componentId]->isEmpty()\
        \ && !$online[$heaps[$componentId]->top()]) {\n                    $heaps[$componentId]->extract();\n\
        \                }\n                $result[] = $heaps[$componentId]->isEmpty()\
        \ ? -1 : $heaps[$componentId]->top();\n            }\n        }\n        return\
        \ $result;\n    }\n}"
      swift: "class Solution {\n    func processQueries(_ c: Int, _ connections: [[Int]],\
        \ _ queries: [[Int]]) -> [Int] {\n        var graph = Array(repeating: [Int](),\
        \ count: c + 1)\n        for edge in connections {\n            let u = edge[0]\n\
        \            let v = edge[1]\n            graph[u].append(v)\n            graph[v].append(u)\n\
        \        }\n\n        var component = Array(repeating: -1, count: c + 1)\n \
        \       var heaps = [[Int]]()\n        for station in 1...c {\n            if\
        \ component[station] != -1 { continue }\n            let componentId = heaps.count\n\
        \            var stations = [Int]()\n            var stack = [station]\n   \
        \         component[station] = componentId\n            while let node = stack.popLast()\
        \ {\n                stations.append(node)\n                for neighbor in\
        \ graph[node] {\n                    if component[neighbor] == -1 {\n      \
        \                  component[neighbor] = componentId\n                     \
        \   stack.append(neighbor)\n                    }\n                }\n     \
        \       }\n            stations.sort()\n            heaps.append(stations)\n\
        \        }\n\n        var online = Array(repeating: true, count: c + 1)\n  \
        \      var result = [Int]()\n        for query in queries {\n            let\
        \ type = query[0]\n            let station = query[1]\n            if type ==\
        \ 2 {\n                online[station] = false\n            } else if online[station]\
        \ {\n                result.append(station)\n            } else {\n        \
        \        let componentId = component[station]\n                while !heaps[componentId].isEmpty\
        \ && !online[heaps[componentId][0]] {\n                    heaps[componentId].removeFirst()\n\
        \                }\n                result.append(heaps[componentId].isEmpty\
        \ ? -1 : heaps[componentId][0])\n            }\n        }\n        return result\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun processQueries(c: Int, connections: Array<IntArray>,\
        \ queries: Array<IntArray>): IntArray {\n        val graph = Array(c + 1) {\
        \ mutableListOf<Int>() }\n        for (edge in connections) {\n            graph[edge[0]].add(edge[1])\n\
        \            graph[edge[1]].add(edge[0])\n        }\n\n        val component\
        \ = IntArray(c + 1) { -1 }\n        val heaps = mutableListOf<java.util.PriorityQueue<Int>>()\n\
        \        for (station in 1..c) {\n            if (component[station] != -1)\
        \ continue\n            val componentId = heaps.size\n            val heap =\
        \ java.util.PriorityQueue<Int>()\n            heaps.add(heap)\n            val\
        \ stack = mutableListOf(station)\n            component[station] = componentId\n\
        \            while (stack.isNotEmpty()) {\n                val node = stack.removeAt(stack.lastIndex)\n\
        \                heap.add(node)\n                for (neighbor in graph[node])\
        \ {\n                    if (component[neighbor] == -1) {\n                \
        \        component[neighbor] = componentId\n                        stack.add(neighbor)\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    val online = BooleanArray(c + 1) { true }\n        val result = mutableListOf<Int>()\n\
        \        for (query in queries) {\n            val type = query[0]\n       \
        \     val station = query[1]\n            if (type == 2) {\n               \
        \ online[station] = false\n            } else if (online[station]) {\n     \
        \           result.add(station)\n            } else {\n                val heap\
        \ = heaps[component[station]]\n                while (heap.isNotEmpty() && !online[heap.peek()])\
        \ heap.poll()\n                result.add(if (heap.isNotEmpty()) heap.peek()\
        \ else -1)\n            }\n        }\n        return result.toIntArray()\n \
        \   }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  List<int> processQueries(int\
        \ c, List<List<int>> connections, List<List<int>> queries) {\n    final graph\
        \ = List.generate(c + 1, (_) => <int>[]);\n    for (final edge in connections)\
        \ {\n      graph[edge[0]].add(edge[1]);\n      graph[edge[1]].add(edge[0]);\n\
        \    }\n\n    final component = List<int>.filled(c + 1, -1);\n    final heaps\
        \ = <PriorityQueue<int>>[];\n    for (var station = 1; station <= c; station++)\
        \ {\n      if (component[station] != -1) continue;\n      final componentId\
        \ = heaps.length;\n      final heap = PriorityQueue<int>((a, b) => a.compareTo(b));\n\
        \      heaps.add(heap);\n      final stack = <int>[station];\n      component[station]\
        \ = componentId;\n      while (stack.isNotEmpty) {\n        final node = stack.removeLast();\n\
        \        heap.add(node);\n        for (final neighbor in graph[node]) {\n  \
        \        if (component[neighbor] == -1) {\n            component[neighbor] =\
        \ componentId;\n            stack.add(neighbor);\n          }\n        }\n \
        \     }\n    }\n\n    final online = List<bool>.filled(c + 1, true);\n    final\
        \ result = <int>[];\n    for (final query in queries) {\n      final type =\
        \ query[0];\n      final station = query[1];\n      if (type == 2) {\n     \
        \   online[station] = false;\n      } else if (online[station]) {\n        result.add(station);\n\
        \      } else {\n        final heap = heaps[component[station]];\n        while\
        \ (heap.isNotEmpty && !online[heap.first]) {\n          heap.removeFirst();\n\
        \        }\n        result.add(heap.isNotEmpty ? heap.first : -1);\n      }\n\
        \    }\n    return result;\n  }\n}"
      go: "import \"container/heap\"\n\ntype minHeap []int\n\nfunc (h minHeap) Len()\
        \ int           { return len(h) }\nfunc (h minHeap) Less(i, j int) bool { return\
        \ h[i] < h[j] }\nfunc (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i]\
        \ }\nfunc (h *minHeap) Push(x any)        { *h = append(*h, x.(int)) }\nfunc\
        \ (h *minHeap) Pop() any {\n\told := *h\n\tn := len(old)\n\tx := old[n-1]\n\t\
        *h = old[:n-1]\n\treturn x\n}\n\nfunc processQueries(c int, connections [][]int,\
        \ queries [][]int) []int {\n\tgraph := make([][]int, c+1)\n\tfor _, edge :=\
        \ range connections {\n\t\tu, v := edge[0], edge[1]\n\t\tgraph[u] = append(graph[u],\
        \ v)\n\t\tgraph[v] = append(graph[v], u)\n\t}\n\n\tcomponent := make([]int,\
        \ c+1)\n\tfor i := range component {\n\t\tcomponent[i] = -1\n\t}\n\theaps :=\
        \ make([]*minHeap, 0)\n\tfor station := 1; station <= c; station++ {\n\t\tif\
        \ component[station] != -1 {\n\t\t\tcontinue\n\t\t}\n\t\tcomponentID := len(heaps)\n\
        \t\th := &minHeap{}\n\t\theaps = append(heaps, h)\n\t\tstack := []int{station}\n\
        \t\tcomponent[station] = componentID\n\t\tfor len(stack) > 0 {\n\t\t\tn := len(stack)\
        \ - 1\n\t\t\tnode := stack[n]\n\t\t\tstack = stack[:n]\n\t\t\theap.Push(h, node)\n\
        \t\t\tfor _, neighbor := range graph[node] {\n\t\t\t\tif component[neighbor]\
        \ == -1 {\n\t\t\t\t\tcomponent[neighbor] = componentID\n\t\t\t\t\tstack = append(stack,\
        \ neighbor)\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\n\tonline := make([]bool, c+1)\n\
        \tfor i := range online {\n\t\tonline[i] = true\n\t}\n\tresult := make([]int,\
        \ 0)\n\tfor _, query := range queries {\n\t\ttypeID, station := query[0], query[1]\n\
        \t\tif typeID == 2 {\n\t\t\tonline[station] = false\n\t\t} else if online[station]\
        \ {\n\t\t\tresult = append(result, station)\n\t\t} else {\n\t\t\th := heaps[component[station]]\n\
        \t\t\tfor h.Len() > 0 && !online[(*h)[0]] {\n\t\t\t\theap.Pop(h)\n\t\t\t}\n\t\
        \t\tif h.Len() == 0 {\n\t\t\t\tresult = append(result, -1)\n\t\t\t} else {\n\
        \t\t\t\tresult = append(result, (*h)[0])\n\t\t\t}\n\t\t}\n\t}\n\treturn result\n\
        }"
      ruby: "# @param {Integer} c\n# @param {Integer[][]} connections\n# @param {Integer[][]}\
        \ queries\n# @return {Integer[]}\ndef process_queries(c, connections, queries)\n\
        \  graph = Array.new(c + 1) { [] }\n  connections.each do |u, v|\n    graph[u]\
        \ << v\n    graph[v] << u\n  end\n\n  component = Array.new(c + 1, -1)\n  heaps\
        \ = []\n  (1..c).each do |station|\n    next unless component[station] == -1\n\
        \n    component_id = heaps.length\n    heap = []\n    heaps << heap\n    stack\
        \ = [station]\n    component[station] = component_id\n    until stack.empty?\n\
        \      node = stack.pop\n      heap << node\n      graph[node].each do |neighbor|\n\
        \        if component[neighbor] == -1\n          component[neighbor] = component_id\n\
        \          stack << neighbor\n        end\n      end\n    end\n    heap.sort!\n\
        \  end\n\n  online = Array.new(c + 1, true)\n  result = []\n  queries.each do\
        \ |type, station|\n    if type == 2\n      online[station] = false\n    elsif\
        \ online[station]\n      result << station\n    else\n      heap = heaps[component[station]]\n\
        \      heap.shift while !heap.empty? && !online[heap[0]]\n      result << (heap.empty?\
        \ ? -1 : heap[0])\n    end\n  end\n  result\nend"
      scala: "object Solution {\n    def processQueries(c: Int, connections: Array[Array[Int]],\
        \ queries: Array[Array[Int]]): Array[Int] = {\n        val graph = Array.fill(c\
        \ + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])\n        for (edge <-\
        \ connections) {\n            graph(edge(0)) += edge(1)\n            graph(edge(1))\
        \ += edge(0)\n        }\n\n        val component = Array.fill(c + 1)(-1)\n \
        \       val heaps = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.PriorityQueue[Int]]\n\
        \        for (station <- 1 to c) {\n            if (component(station) == -1)\
        \ {\n                val componentId = heaps.length\n                val heap\
        \ = scala.collection.mutable.PriorityQueue.empty[Int](Ordering.Int.reverse)\n\
        \                heaps += heap\n                val stack = scala.collection.mutable.ArrayBuffer(station)\n\
        \                component(station) = componentId\n                while (stack.nonEmpty)\
        \ {\n                    val node = stack.remove(stack.length - 1)\n       \
        \             heap.enqueue(node)\n                    for (neighbor <- graph(node))\
        \ {\n                        if (component(neighbor) == -1) {\n            \
        \                component(neighbor) = componentId\n                       \
        \     stack += neighbor\n                        }\n                    }\n\
        \                }\n            }\n        }\n\n        val online = Array.fill(c\
        \ + 1)(true)\n        val result = scala.collection.mutable.ArrayBuffer.empty[Int]\n\
        \        for (query <- queries) {\n            val queryType = query(0)\n  \
        \          val station = query(1)\n            if (queryType == 2) {\n     \
        \           online(station) = false\n            } else if (online(station))\
        \ {\n                result += station\n            } else {\n             \
        \   val heap = heaps(component(station))\n                while (heap.nonEmpty\
        \ && !online(heap.head)) heap.dequeue()\n                result += (if (heap.nonEmpty)\
        \ heap.head else -1)\n            }\n        }\n        result.toArray\n   \
        \ }\n}"
      rust: "impl Solution {\n    pub fn process_queries(c: i32, connections: Vec<Vec<i32>>,\
        \ queries: Vec<Vec<i32>>) -> Vec<i32> {\n        let n = c as usize;\n     \
        \   let mut graph = vec![Vec::new(); n + 1];\n        for edge in connections\
        \ {\n            let u = edge[0] as usize;\n            let v = edge[1] as usize;\n\
        \            graph[u].push(v);\n            graph[v].push(u);\n        }\n\n\
        \        let mut component = vec![usize::MAX; n + 1];\n        let mut heaps:\
        \ Vec<std::collections::BinaryHeap<std::cmp::Reverse<i32>>> = Vec::new();\n\
        \        for station in 1..=n {\n            if component[station] != usize::MAX\
        \ {\n                continue;\n            }\n            let component_id\
        \ = heaps.len();\n            let mut heap = std::collections::BinaryHeap::new();\n\
        \            let mut stack = vec![station];\n            component[station]\
        \ = component_id;\n            while let Some(node) = stack.pop() {\n      \
        \          heap.push(std::cmp::Reverse(node as i32));\n                for &neighbor\
        \ in &graph[node] {\n                    if component[neighbor] == usize::MAX\
        \ {\n                        component[neighbor] = component_id;\n         \
        \               stack.push(neighbor);\n                    }\n             \
        \   }\n            }\n            heaps.push(heap);\n        }\n\n        let\
        \ mut online = vec![true; n + 1];\n        let mut result = Vec::new();\n  \
        \      for query in queries {\n            let query_type = query[0];\n    \
        \        let station = query[1] as usize;\n            if query_type == 2 {\n\
        \                online[station] = false;\n            } else if online[station]\
        \ {\n                result.push(station as i32);\n            } else {\n  \
        \              let heap = &mut heaps[component[station]];\n                while\
        \ let Some(&std::cmp::Reverse(top)) = heap.peek() {\n                    if\
        \ online[top as usize] {\n                        break;\n                 \
        \   }\n                    heap.pop();\n                }\n                result.push(heap.peek().map_or(-1,\
        \ |x| x.0));\n            }\n        }\n        result\n    }\n}"
      racket: "(define/contract (process-queries c connections queries)\n  (-> exact-integer?\
        \ (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof\
        \ exact-integer?))\n  (let* ([graph (make-vector (add1 c) '())]\n         [component\
        \ (make-vector (add1 c) -1)])\n    (for ([edge connections])\n      (define\
        \ u (first edge))\n      (define v (second edge))\n      (vector-set! graph\
        \ u (cons v (vector-ref graph u)))\n      (vector-set! graph v (cons u (vector-ref\
        \ graph v))))\n    (define heaps '())\n    (for ([station (in-range 1 (add1\
        \ c))])\n      (when (= (vector-ref component station) -1)\n        (define\
        \ component-id (length heaps))\n        (define members '())\n        (define\
        \ stack (list station))\n        (vector-set! component station component-id)\n\
        \        (let loop ()\n          (unless (null? stack)\n            (define\
        \ node (car stack))\n            (set! stack (cdr stack))\n            (set!\
        \ members (cons node members))\n            (for ([neighbor (vector-ref graph\
        \ node)])\n              (when (= (vector-ref component neighbor) -1)\n    \
        \            (vector-set! component neighbor component-id)\n               \
        \ (set! stack (cons neighbor stack))))\n            (loop)))\n        (set!\
        \ heaps (append heaps (list (list->vector (sort members <)))))))\n    (define\
        \ heap-positions (make-vector (length heaps) 0))\n    (define online (make-vector\
        \ (add1 c) #t))\n    (define result '())\n    (for ([query queries])\n     \
        \ (define query-type (first query))\n      (define station (second query))\n\
        \      (cond\n        [(= query-type 2) (vector-set! online station #f)]\n \
        \       [(vector-ref online station) (set! result (cons station result))]\n\
        \        [else\n         (define component-id (vector-ref component station))\n\
        \         (define heap (list-ref heaps component-id))\n         (define position\
        \ (vector-ref heap-positions component-id))\n         (let loop ()\n       \
        \    (when (and (< position (vector-length heap))\n                      (not\
        \ (vector-ref online (vector-ref heap position))))\n             (set! position\
        \ (add1 position))\n             (loop)))\n         (vector-set! heap-positions\
        \ component-id position)\n         (set! result\n               (cons (if (<\
        \ position (vector-length heap))\n                         (vector-ref heap\
        \ position)\n                         -1)\n                     result))]))\n\
        \    (reverse result)))"
      erlang: "-spec process_queries(C :: integer(), Connections :: [[integer()]], Queries\
        \ :: [[integer()]]) -> [integer()].\nprocess_queries(C, Connections, Queries)\
        \ ->\n  Graph0 = maps:from_list([{I, []} || I <- lists:seq(1, C)]),\n  Graph\
        \ = lists:foldl(\n    fun([U, V], Acc) ->\n      Acc1 = maps:update_with(U,\
        \ fun(Neighbors) -> [V | Neighbors] end, Acc),\n      maps:update_with(V, fun(Neighbors)\
        \ -> [U | Neighbors] end, Acc1)\n    end,\n    Graph0,\n    Connections\n  ),\n\
        \  {Components, Heaps} = build_components(lists:seq(1, C), Graph, #{}, []),\n\
        \  Online = maps:from_list([{I, true} || I <- lists:seq(1, C)]),\n  {_, _, Reversed}\
        \ = lists:foldl(\n    fun([2, Station], {CompMap, HeapList, Acc}) ->\n     \
        \     {CompMap, HeapList, Acc, maps:put(Station, false, Online)};\n       ([1,\
        \ Station], {CompMap, HeapList, Acc}) ->\n          case maps:get(Station, Online)\
        \ of\n            true -> {CompMap, HeapList, [Station | Acc], Online};\n  \
        \          false ->\n              ComponentId = maps:get(Station, CompMap),\n\
        \              Heap = lists:nth(ComponentId, HeapList),\n              {Answer,\
        \ UpdatedHeap} = find_online(Heap, Online),\n              {CompMap, replace_nth(ComponentId,\
        \ UpdatedHeap, HeapList), [Answer | Acc], Online}\n          end\n    end,\n\
        \    {Components, Heaps, [], Online},\n    Queries\n  ),\n  lists:reverse(Reversed).\n\
        \nbuild_components([], _Graph, Components, Heaps) -> {Components, Heaps};\n\
        build_components([Station | Rest], Graph, Components, Heaps) ->\n  case maps:is_key(Station,\
        \ Components) of\n    true -> build_components(Rest, Graph, Components, Heaps);\n\
        \    false ->\n      ComponentId = length(Heaps) + 1,\n      {NewComponents,\
        \ Members} = visit([Station], Graph, Components, ComponentId, []),\n      build_components(Rest,\
        \ Graph, NewComponents, Heaps ++ [lists:sort(Members)])\n  end.\n\nvisit([],\
        \ _Graph, Components, _ComponentId, Members) -> {Components, Members};\nvisit([Node\
        \ | Stack], Graph, Components, ComponentId, Members) ->\n  case maps:is_key(Node,\
        \ Components) of\n    true -> visit(Stack, Graph, Components, ComponentId, Members);\n\
        \    false ->\n      NewComponents = maps:put(Node, ComponentId, Components),\n\
        \      Neighbors = maps:get(Node, Graph),\n      visit(Neighbors ++ Stack, Graph,\
        \ NewComponents, ComponentId, [Node | Members])\n  end.\n\nfind_online([], _Online)\
        \ -> {-1, []};\nfind_online([Station | Rest] = Heap, Online) ->\n  case maps:get(Station,\
        \ Online) of\n    true -> {Station, Heap};\n    false -> find_online(Rest, Online)\n\
        \  end.\n\nreplace_nth(1, Value, [_ | Rest]) -> [Value | Rest];\nreplace_nth(N,\
        \ Value, [Head | Rest]) -> [Head | replace_nth(N - 1, Value, Rest)]."
      elixir: "defmodule Solution do\n  @spec process_queries(c :: integer, connections\
        \ :: [[integer]], queries :: [[integer]]) :: [integer]\n  def process_queries(c,\
        \ connections, queries) do\n    graph =\n      Enum.reduce(1..c, %{}, fn station,\
        \ acc ->\n        Map.put(acc, station, [])\n      end)\n      |> then(fn initial\
        \ ->\n        Enum.reduce(connections, initial, fn [u, v], acc ->\n        \
        \  acc\n          |> Map.update!(u, &[v | &1])\n          |> Map.update!(v,\
        \ &[u | &1])\n        end)\n      end)\n\n    {components, heaps} = build_components(1..c,\
        \ graph, %{}, [])\n    online = Map.new(1..c, &{&1, true})\n    positions =\
        \ Map.new(0..(length(heaps) - 1), &{&1, 0})\n\n    {_, _, _, result} =\n   \
        \   Enum.reduce(queries, {components, heaps, {online, positions}, []}, fn\n\
        \        [2, station], {component_map, heap_list, {status, pos}, acc} ->\n \
        \         {component_map, heap_list, {Map.put(status, station, false), pos},\
        \ acc}\n\n        [1, station], {component_map, heap_list, {status, pos}, acc}\
        \ ->\n          if Map.fetch!(status, station) do\n            {component_map,\
        \ heap_list, {status, pos}, [station | acc]}\n          else\n            component_id\
        \ = Map.fetch!(component_map, station)\n            heap = Enum.at(heap_list,\
        \ component_id)\n            start = Map.fetch!(pos, component_id)\n       \
        \     {answer, next_position} = first_online(heap, start, status)\n        \
        \    updated_positions = Map.put(pos, component_id, next_position)\n       \
        \     {component_map, heap_list, {status, updated_positions}, [answer | acc]}\n\
        \          end\n      end)\n\n    Enum.reverse(result)\n  end\n\n  defp build_components(stations,\
        \ graph, components, heaps) do\n    Enum.reduce(stations, {components, heaps},\
        \ fn station, {component_map, heap_list} ->\n      if Map.has_key?(component_map,\
        \ station) do\n        {component_map, heap_list}\n      else\n        component_id\
        \ = length(heap_list)\n        {updated_components, members} = visit([station],\
        \ graph, component_map, component_id, [])\n        {updated_components, heap_list\
        \ ++ [Enum.sort(members)]}\n      end\n    end)\n  end\n\n  defp visit([], _graph,\
        \ components, _component_id, members), do: {components, members}\n\n  defp visit([node\
        \ | stack], graph, components, component_id, members) do\n    if Map.has_key?(components,\
        \ node) do\n      visit(stack, graph, components, component_id, members)\n \
        \   else\n      updated_components = Map.put(components, node, component_id)\n\
        \      neighbors = Map.fetch!(graph, node)\n      visit(neighbors ++ stack,\
        \ graph, updated_components, component_id, [node | members])\n    end\n  end\n\
        \n  defp first_online(heap, position, online) do\n    if position >= length(heap)\
        \ do\n      {-1, position}\n    else\n      station = Enum.at(heap, position)\n\
        \      if Map.fetch!(online, station) do\n        {station, position}\n    \
        \  else\n        first_online(heap, position + 1, online)\n      end\n    end\n\
        \  end\nend"
    approach: 'First, use DFS to assign every station a component ID based on the fixed
      cable connections. Then maintain a min-heap for each component, initially containing
      all its station IDs, and an online flag for each station.


      For a type 2 query, mark the station offline; it remains in the heap and is discarded
      lazily when it reaches the top. For a type 1 query, return the station itself
      if it is online. Otherwise, discard offline IDs from its component''s heap and
      return the smallest remaining ID, or -1 if the heap is empty.'
    time_complexity: O(c + n + q log c), where c is the number of stations, n is the
      number of connections, and q is the number of queries. Each station is pushed
      once and removed from a heap at most once.
    space_complexity: O(c + n), for the adjacency lists, component IDs, online flags,
      and component heaps.
    elapsed_time: 199.22010397911072
    model: gpt-6-luna
    generated_at: '2026-11-13 00:28:29 '
---

## Problem #3607: Power Grid Maintenance

**Difficulty:** Medium

**Topics:** Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Heap (Priority Queue), Ordered Set

## Problem Description

<p data-end="401" data-start="120">You are given an integer <code data-end="194" data-start="191">c</code> representing <code data-end="211" data-start="208">c</code> power stations, each with a unique identifier <code>id</code> from 1 to <code>c</code> (1‑based indexing).</p>

<p data-end="401" data-start="120">These stations are interconnected via <code data-end="295" data-start="292">n</code> <strong>bidirectional</strong> cables, represented by a 2D array <code data-end="357" data-start="344">connections</code>, where each element <code data-end="430" data-start="405">connections[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates a connection between station <code>u<sub>i</sub></code> and station <code>v<sub>i</sub></code>. Stations that are directly or indirectly connected form a <strong>power grid</strong>.</p>

<p data-end="626" data-start="586">Initially, <strong>all</strong> stations are online (operational).</p>

<p data-end="720" data-start="628">You are also given a 2D array <code data-end="667" data-start="658">queries</code>, where each query is one of the following <em>two</em> types:</p>

<ul data-end="995" data-start="722">
	<li data-end="921" data-start="722">
	<p data-end="921" data-start="724"><code data-end="732" data-start="724">[1, x]</code>: A maintenance check is requested for station <code data-end="782" data-start="779">x</code>. If station <code>x</code> is online, it resolves the check by itself. If station <code>x</code> is offline, the check is resolved by the operational station with the smallest <code>id</code> in the same <strong>power grid</strong> as <code>x</code>. If <strong>no</strong> <strong>operational</strong> station <em>exists</em> in that grid, return -1.</p>
	</li>
	<li data-end="995" data-start="923">
	<p data-end="995" data-start="925"><code data-end="933" data-start="925">[2, x]</code>: Station <code data-end="946" data-start="943">x</code> goes offline (i.e., it becomes non-operational).</p>
	</li>
</ul>

<p data-end="1106" data-start="997">Return an array of integers representing the results of each query of type <code data-end="1080" data-start="1072">[1, x]</code> in the <strong>order</strong> they appear.</p>

<p data-end="1106" data-start="997"><strong>Note:</strong> The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,2,3]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/04/15/powergrid.jpg" style="width: 361px; height: 42px;" /></p>

<ul>
	<li data-end="223" data-start="143">Initially, all stations <code>{1, 2, 3, 4, 5}</code> are online and form a single power grid.</li>
	<li data-end="322" data-start="226">Query <code>[1,3]</code>: Station 3 is online, so the maintenance check is resolved by station 3.</li>
	<li data-end="402" data-start="325">Query <code>[2,1]</code>: Station 1 goes offline. The remaining online stations are <code>{2, 3, 4, 5}</code>.</li>
	<li data-end="557" data-start="405">Query <code>[1,1]</code>: Station 1 is offline, so the check is resolved by the operational station with the smallest <code>id</code> among <code>{2, 3, 4, 5}</code>, which is station 2.</li>
	<li data-end="641" data-start="560">Query <code>[2,2]</code>: Station 2 goes offline. The remaining online stations are <code>{3, 4, 5}</code>.</li>
	<li data-end="800" data-start="644">Query <code>[1,2]</code>: Station 2 is offline, so the check is resolved by the operational station with the smallest <code>id</code> among <code>{3, 4, 5}</code>, which is station 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,-1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li data-end="976" data-start="909">There are no connections, so each station is its own isolated grid.</li>
	<li data-end="1096" data-start="979">Query <code>[1,1]</code>: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.</li>
	<li data-end="1135" data-start="1099">Query <code>[2,1]</code>: Station 1 goes offline.</li>
	<li data-end="1237" data-start="1138">Query <code>[1,1]</code>: Station 1 is offline and there are no other stations in its grid, so the result is -1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="155" data-start="139"><code>1 &lt;= c &lt;= 10<sup>5</sup></code></li>
	<li data-end="213" data-start="158"><code>0 &lt;= n == connections.length &lt;= min(10<sup>5</sup>, c * (c - 1) / 2)</code></li>
	<li data-end="244" data-start="216"><code>connections[i].length == 2</code></li>
	<li data-end="295" data-start="247"><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= c</code></li>
	<li data-end="338" data-start="298"><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li data-end="374" data-start="341"><code>1 &lt;= queries.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li data-end="401" data-start="377"><code>queries[i].length == 2</code></li>
	<li data-end="436" data-start="404"><code>queries[i][0]</code> is either 1 or 2.</li>
	<li data-end="462" data-start="439"><code>1 &lt;= queries[i][1] &lt;= c</code></li>
</ul>


## Hints

1. Use DFS or BFS to assign each station a component ID

2. For each component, maintain a sorted set of online station IDs

3. For query `[2, x]`, remove `x` from the set of its component

4. For query `[1, x]`, if `x` is in its component’s set return `x`; otherwise if the set is non-empty return its smallest element; else return `-1`

5. Precompute all components and then handle each query in O(log n) time using the sorted sets

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

First, use DFS to assign every station a component ID based on the fixed cable connections. Then maintain a min-heap for each component, initially containing all its station IDs, and an online flag for each station.

For a type 2 query, mark the station offline; it remains in the heap and is discarded lazily when it reaches the top. For a type 1 query, return the station itself if it is online. Otherwise, discard offline IDs from its component's heap and return the smallest remaining ID, or -1 if the heap is empty.

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
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        vector<vector<int>> graph(c + 1);
        for (const auto& edge : connections) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        vector<int> component(c + 1, -1);
        vector<priority_queue<int, vector<int>, greater<int>>> heaps;
        for (int station = 1; station <= c; ++station) {
            if (component[station] != -1) continue;
            int id = static_cast<int>(heaps.size());
            heaps.emplace_back();
            vector<int> stack = {station};
            component[station] = id;
            while (!stack.empty()) {
                int node = stack.back();
                stack.pop_back();
                heaps[id].push(node);
                for (int next : graph[node]) {
                    if (component[next] == -1) {
                        component[next] = id;
                        stack.push_back(next);
                    }
                }
            }
        }

        vector<char> online(c + 1, true);
        vector<int> result;
        for (const auto& query : queries) {
            int type = query[0];
            int station = query[1];
            if (type == 2) {
                online[station] = false;
            } else if (online[station]) {
                result.push_back(station);
            } else {
                auto& heap = heaps[component[station]];
                while (!heap.empty() && !online[heap.top()]) heap.pop();
                result.push_back(heap.empty() ? -1 : heap.top());
            }
        }
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public int[] processQueries(int c, int[][] connections, int[][] queries) {
        List<Integer>[] graph = new ArrayList[c + 1];
        for (int i = 1; i <= c; i++) graph[i] = new ArrayList<>();
        for (int[] edge : connections) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        int[] component = new int[c + 1];
        java.util.Arrays.fill(component, -1);
        List<PriorityQueue<Integer>> heaps = new ArrayList<>();
        for (int station = 1; station <= c; station++) {
            if (component[station] != -1) continue;
            int id = heaps.size();
            PriorityQueue<Integer> heap = new PriorityQueue<>();
            heaps.add(heap);
            ArrayDeque<Integer> stack = new ArrayDeque<>();
            stack.push(station);
            component[station] = id;
            while (!stack.isEmpty()) {
                int node = stack.pop();
                heap.offer(node);
                for (int next : graph[node]) {
                    if (component[next] == -1) {
                        component[next] = id;
                        stack.push(next);
                    }
                }
            }
        }

        boolean[] online = new boolean[c + 1];
        java.util.Arrays.fill(online, true);
        int[] result = new int[queries.length];
        int size = 0;
        for (int[] query : queries) {
            int type = query[0];
            int station = query[1];
            if (type == 2) {
                online[station] = false;
            } else if (online[station]) {
                result[size++] = station;
            } else {
                PriorityQueue<Integer> heap = heaps.get(component[station]);
                while (!heap.isEmpty() && !online[heap.peek()]) heap.poll();
                result[size++] = heap.isEmpty() ? -1 : heap.peek();
            }
        }
        return java.util.Arrays.copyOf(result, size);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        import heapq

        graph = [[] for _ in range(c + 1)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        component = [-1] * (c + 1)
        heaps = []
        for station in range(1, c + 1):
            if component[station] != -1:
                continue
            component_id = len(heaps)
            heap = []
            heaps.append(heap)
            stack = [station]
            component[station] = component_id
            while stack:
                node = stack.pop()
                heapq.heappush(heap, node)
                for neighbor in graph[node]:
                    if component[neighbor] == -1:
                        component[neighbor] = component_id
                        stack.append(neighbor)

        online = [True] * (c + 1)
        result = []
        for query_type, station in queries:
            if query_type == 2:
                online[station] = False
            elif online[station]:
                result.append(station)
            else:
                heap = heaps[component[station]]
                while heap and not online[heap[0]]:
                    heapq.heappop(heap)
                result.append(heap[0] if heap else -1)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(c + 1)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        component = [-1] * (c + 1)
        heaps = []
        for station in range(1, c + 1):
            if component[station] != -1:
                continue
            component_id = len(heaps)
            heap = []
            heaps.append(heap)
            stack = [station]
            component[station] = component_id
            while stack:
                node = stack.pop()
                heapq.heappush(heap, node)
                for neighbor in graph[node]:
                    if component[neighbor] == -1:
                        component[neighbor] = component_id
                        stack.append(neighbor)

        online = [True] * (c + 1)
        result = []
        for query_type, station in queries:
            if query_type == 2:
                online[station] = False
            elif online[station]:
                result.append(station)
            else:
                heap = heaps[component[station]]
                while heap and not online[heap[0]]:
                    heapq.heappop(heap)
                result.append(heap[0] if heap else -1)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int* processQueries(int c, int** connections, int connectionsSize, int* connectionsColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int* degree = (int*)calloc(c + 1, sizeof(int));
    for (int i = 0; i < connectionsSize; i++) {
        degree[connections[i][0]]++;
        degree[connections[i][1]]++;
    }

    int** graph = (int**)malloc((c + 1) * sizeof(int*));
    int* position = (int*)calloc(c + 1, sizeof(int));
    for (int i = 0; i <= c; i++) graph[i] = (int*)malloc((degree[i] ? degree[i] : 1) * sizeof(int));
    for (int i = 0; i < connectionsSize; i++) {
        int u = connections[i][0];
        int v = connections[i][1];
        graph[u][position[u]++] = v;
        graph[v][position[v]++] = u;
    }

    int* component = (int*)malloc((c + 1) * sizeof(int));
    for (int i = 0; i <= c; i++) component[i] = -1;
    int** heaps = (int**)malloc((c + 1) * sizeof(int*));
    int* heapSize = (int*)calloc(c + 1, sizeof(int));
    int* stack = (int*)malloc((c + 1) * sizeof(int));
    int componentCount = 0;

    for (int station = 1; station <= c; station++) {
        if (component[station] != -1) continue;
        int id = componentCount++;
        heaps[id] = (int*)malloc((c + 1) * sizeof(int));
        int top = 0;
        stack[top++] = station;
        component[station] = id;
        while (top > 0) {
            int node = stack[--top];
            int size = ++heapSize[id];
            int index = size;
            while (index > 1 && node < heaps[id][index / 2]) {
                heaps[id][index] = heaps[id][index / 2];
                index /= 2;
            }
            heaps[id][index] = node;
            for (int j = 0; j < degree[node]; j++) {
                int next = graph[node][j];
                if (component[next] == -1) {
                    component[next] = id;
                    stack[top++] = next;
                }
            }
        }
    }

    char* online = (char*)malloc((c + 1) * sizeof(char));
    for (int i = 0; i <= c; i++) online[i] = 1;
    int* result = (int*)malloc(queriesSize * sizeof(int));
    int resultCount = 0;

    for (int i = 0; i < queriesSize; i++) {
        int type = queries[i][0];
        int station = queries[i][1];
        if (type == 2) {
            online[station] = 0;
        } else if (online[station]) {
            result[resultCount++] = station;
        } else {
            int id = component[station];
            while (heapSize[id] > 0 && !online[heaps[id][1]]) {
                int last = heaps[id][heapSize[id]--];
                if (heapSize[id] == 0) continue;
                int index = 1;
                while (index * 2 <= heapSize[id]) {
                    int child = index * 2;
                    if (child + 1 <= heapSize[id] && heaps[id][child + 1] < heaps[id][child]) child++;
                    if (heaps[id][child] >= last) break;
                    heaps[id][index] = heaps[id][child];
                    index = child;
                }
                heaps[id][index] = last;
            }
            result[resultCount++] = heapSize[id] == 0 ? -1 : heaps[id][1];
        }
    }

    *returnSize = resultCount;
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] ProcessQueries(int c, int[][] connections, int[][] queries) {
        var graph = new List<int>[c + 1];
        for (int i = 0; i <= c; i++) graph[i] = new List<int>();
        foreach (var edge in connections) {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);
        }

        int[] component = new int[c + 1];
        Array.Fill(component, -1);
        var heaps = new List<PriorityQueue<int, int>>();
        for (int station = 1; station <= c; station++) {
            if (component[station] != -1) continue;
            int componentId = heaps.Count;
            var heap = new PriorityQueue<int, int>();
            heaps.Add(heap);
            var stack = new Stack<int>();
            stack.Push(station);
            component[station] = componentId;
            while (stack.Count > 0) {
                int node = stack.Pop();
                heap.Enqueue(node, node);
                foreach (int neighbor in graph[node]) {
                    if (component[neighbor] == -1) {
                        component[neighbor] = componentId;
                        stack.Push(neighbor);
                    }
                }
            }
        }

        bool[] online = new bool[c + 1];
        Array.Fill(online, true);
        var result = new List<int>();
        foreach (var query in queries) {
            int type = query[0];
            int station = query[1];
            if (type == 2) {
                online[station] = false;
            } else if (online[station]) {
                result.Add(station);
            } else {
                var heap = heaps[component[station]];
                while (heap.Count > 0 && !online[heap.Peek()) {
                    heap.Dequeue();
                }
                result.Add(heap.Count > 0 ? heap.Peek() : -1);
            }
        }
        return result.ToArray();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} c
 * @param {number[][]} connections
 * @param {number[][]} queries
 * @return {number[]}
 */
var processQueries = function(c, connections, queries) {
    const graph = Array.from({ length: c + 1 }, () => []);
    for (const [u, v] of connections) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const component = Array(c + 1).fill(-1);
    const heaps = [];
    for (let station = 1; station <= c; station++) {
        if (component[station] !== -1) continue;
        const componentId = heaps.length;
        const heap = [];
        heaps.push(heap);
        const stack = [station];
        component[station] = componentId;
        while (stack.length > 0) {
            const node = stack.pop();
            heap.push(node);
            for (const neighbor of graph[node]) {
                if (component[neighbor] === -1) {
                    component[neighbor] = componentId;
                    stack.push(neighbor);
                }
            }
        }
        heap.sort((a, b) => a - b);
    }

    const online = Array(c + 1).fill(true);
    const result = [];
    for (const [type, station] of queries) {
        if (type === 2) {
            online[station] = false;
        } else if (online[station]) {
            result.push(station);
        } else {
            const heap = heaps[component[station]];
            while (heap.length > 0 && !online[heap[0]]) heap.shift();
            result.push(heap.length > 0 ? heap[0] : -1);
        }
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function processQueries(c: number, connections: number[][], queries: number[][]): number[] {
    const graph: number[][] = Array.from({ length: c + 1 }, () => []);
    for (const [u, v] of connections) {
        graph[u].push(v);
        graph[v].push(u);
    }

    const component: number[] = Array(c + 1).fill(-1);
    const heaps: number[][] = [];
    for (let station = 1; station <= c; station++) {
        if (component[station] !== -1) continue;
        const componentId = heaps.length;
        const heap: number[] = [];
        heaps.push(heap);
        const stack = [station];
        component[station] = componentId;
        while (stack.length > 0) {
            const node = stack.pop()!;
            heap.push(node);
            for (const neighbor of graph[node]) {
                if (component[neighbor] === -1) {
                    component[neighbor] = componentId;
                    stack.push(neighbor);
                }
            }
        }
        heap.sort((a, b) => a - b);
    }

    const online: boolean[] = Array(c + 1).fill(true);
    const result: number[] = [];
    for (const [type, station] of queries) {
        if (type === 2) {
            online[station] = false;
        } else if (online[station]) {
            result.push(station);
        } else {
            const heap = heaps[component[station]];
            while (heap.length > 0 && !online[heap[0]]) heap.shift();
            result.push(heap.length > 0 ? heap[0] : -1);
        }
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $c
     * @param Integer[][] $connections
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function processQueries($c, $connections, $queries) {
        $graph = array_fill(0, $c + 1, []);
        foreach ($connections as $edge) {
            [$u, $v] = $edge;
            $graph[$u][] = $v;
            $graph[$v][] = $u;
        }

        $component = array_fill(0, $c + 1, -1);
        $heaps = [];
        for ($station = 1; $station <= $c; $station++) {
            if ($component[$station] !== -1) {
                continue;
            }
            $componentId = count($heaps);
            $heap = new SplMinHeap();
            $heaps[] = $heap;
            $stack = [$station];
            $component[$station] = $componentId;
            while (!empty($stack)) {
                $node = array_pop($stack);
                $heaps[$componentId]->insert($node);
                foreach ($graph[$node] as $neighbor) {
                    if ($component[$neighbor] === -1) {
                        $component[$neighbor] = $componentId;
                        $stack[] = $neighbor;
                    }
                }
            }
        }

        $online = array_fill(0, $c + 1, true);
        $result = [];
        foreach ($queries as $query) {
            [$type, $station] = $query;
            if ($type === 2) {
                $online[$station] = false;
            } elseif ($online[$station]) {
                $result[] = $station;
            } else {
                $componentId = $component[$station];
                while (!$heaps[$componentId]->isEmpty() && !$online[$heaps[$componentId]->top()]) {
                    $heaps[$componentId]->extract();
                }
                $result[] = $heaps[$componentId]->isEmpty() ? -1 : $heaps[$componentId]->top();
            }
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func processQueries(_ c: Int, _ connections: [[Int]], _ queries: [[Int]]) -> [Int] {
        var graph = Array(repeating: [Int](), count: c + 1)
        for edge in connections {
            let u = edge[0]
            let v = edge[1]
            graph[u].append(v)
            graph[v].append(u)
        }

        var component = Array(repeating: -1, count: c + 1)
        var heaps = [[Int]]()
        for station in 1...c {
            if component[station] != -1 { continue }
            let componentId = heaps.count
            var stations = [Int]()
            var stack = [station]
            component[station] = componentId
            while let node = stack.popLast() {
                stations.append(node)
                for neighbor in graph[node] {
                    if component[neighbor] == -1 {
                        component[neighbor] = componentId
                        stack.append(neighbor)
                    }
                }
            }
            stations.sort()
            heaps.append(stations)
        }

        var online = Array(repeating: true, count: c + 1)
        var result = [Int]()
        for query in queries {
            let type = query[0]
            let station = query[1]
            if type == 2 {
                online[station] = false
            } else if online[station] {
                result.append(station)
            } else {
                let componentId = component[station]
                while !heaps[componentId].isEmpty && !online[heaps[componentId][0]] {
                    heaps[componentId].removeFirst()
                }
                result.append(heaps[componentId].isEmpty ? -1 : heaps[componentId][0])
            }
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun processQueries(c: Int, connections: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val graph = Array(c + 1) { mutableListOf<Int>() }
        for (edge in connections) {
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        }

        val component = IntArray(c + 1) { -1 }
        val heaps = mutableListOf<java.util.PriorityQueue<Int>>()
        for (station in 1..c) {
            if (component[station] != -1) continue
            val componentId = heaps.size
            val heap = java.util.PriorityQueue<Int>()
            heaps.add(heap)
            val stack = mutableListOf(station)
            component[station] = componentId
            while (stack.isNotEmpty()) {
                val node = stack.removeAt(stack.lastIndex)
                heap.add(node)
                for (neighbor in graph[node]) {
                    if (component[neighbor] == -1) {
                        component[neighbor] = componentId
                        stack.add(neighbor)
                    }
                }
            }
        }

        val online = BooleanArray(c + 1) { true }
        val result = mutableListOf<Int>()
        for (query in queries) {
            val type = query[0]
            val station = query[1]
            if (type == 2) {
                online[station] = false
            } else if (online[station]) {
                result.add(station)
            } else {
                val heap = heaps[component[station]]
                while (heap.isNotEmpty() && !online[heap.peek()]) heap.poll()
                result.add(if (heap.isNotEmpty()) heap.peek() else -1)
            }
        }
        return result.toIntArray()
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
  List<int> processQueries(int c, List<List<int>> connections, List<List<int>> queries) {
    final graph = List.generate(c + 1, (_) => <int>[]);
    for (final edge in connections) {
      graph[edge[0]].add(edge[1]);
      graph[edge[1]].add(edge[0]);
    }

    final component = List<int>.filled(c + 1, -1);
    final heaps = <PriorityQueue<int>>[];
    for (var station = 1; station <= c; station++) {
      if (component[station] != -1) continue;
      final componentId = heaps.length;
      final heap = PriorityQueue<int>((a, b) => a.compareTo(b));
      heaps.add(heap);
      final stack = <int>[station];
      component[station] = componentId;
      while (stack.isNotEmpty) {
        final node = stack.removeLast();
        heap.add(node);
        for (final neighbor in graph[node]) {
          if (component[neighbor] == -1) {
            component[neighbor] = componentId;
            stack.add(neighbor);
          }
        }
      }
    }

    final online = List<bool>.filled(c + 1, true);
    final result = <int>[];
    for (final query in queries) {
      final type = query[0];
      final station = query[1];
      if (type == 2) {
        online[station] = false;
      } else if (online[station]) {
        result.add(station);
      } else {
        final heap = heaps[component[station]];
        while (heap.isNotEmpty && !online[heap.first]) {
          heap.removeFirst();
        }
        result.add(heap.isNotEmpty ? heap.first : -1);
      }
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "container/heap"

type minHeap []int

func (h minHeap) Len() int           { return len(h) }
func (h minHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *minHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func processQueries(c int, connections [][]int, queries [][]int) []int {
	graph := make([][]int, c+1)
	for _, edge := range connections {
		u, v := edge[0], edge[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	component := make([]int, c+1)
	for i := range component {
		component[i] = -1
	}
	heaps := make([]*minHeap, 0)
	for station := 1; station <= c; station++ {
		if component[station] != -1 {
			continue
		}
		componentID := len(heaps)
		h := &minHeap{}
		heaps = append(heaps, h)
		stack := []int{station}
		component[station] = componentID
		for len(stack) > 0 {
			n := len(stack) - 1
			node := stack[n]
			stack = stack[:n]
			heap.Push(h, node)
			for _, neighbor := range graph[node] {
				if component[neighbor] == -1 {
					component[neighbor] = componentID
					stack = append(stack, neighbor)
				}
			}
		}
	}

	online := make([]bool, c+1)
	for i := range online {
		online[i] = true
	}
	result := make([]int, 0)
	for _, query := range queries {
		typeID, station := query[0], query[1]
		if typeID == 2 {
			online[station] = false
		} else if online[station] {
			result = append(result, station)
		} else {
			h := heaps[component[station]]
			for h.Len() > 0 && !online[(*h)[0]] {
				heap.Pop(h)
			}
			if h.Len() == 0 {
				result = append(result, -1)
			} else {
				result = append(result, (*h)[0])
			}
		}
	}
	return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} c
# @param {Integer[][]} connections
# @param {Integer[][]} queries
# @return {Integer[]}
def process_queries(c, connections, queries)
  graph = Array.new(c + 1) { [] }
  connections.each do |u, v|
    graph[u] << v
    graph[v] << u
  end

  component = Array.new(c + 1, -1)
  heaps = []
  (1..c).each do |station|
    next unless component[station] == -1

    component_id = heaps.length
    heap = []
    heaps << heap
    stack = [station]
    component[station] = component_id
    until stack.empty?
      node = stack.pop
      heap << node
      graph[node].each do |neighbor|
        if component[neighbor] == -1
          component[neighbor] = component_id
          stack << neighbor
        end
      end
    end
    heap.sort!
  end

  online = Array.new(c + 1, true)
  result = []
  queries.each do |type, station|
    if type == 2
      online[station] = false
    elsif online[station]
      result << station
    else
      heap = heaps[component[station]]
      heap.shift while !heap.empty? && !online[heap[0]]
      result << (heap.empty? ? -1 : heap[0])
    end
  end
  result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def processQueries(c: Int, connections: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
        val graph = Array.fill(c + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
        for (edge <- connections) {
            graph(edge(0)) += edge(1)
            graph(edge(1)) += edge(0)
        }

        val component = Array.fill(c + 1)(-1)
        val heaps = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.PriorityQueue[Int]]
        for (station <- 1 to c) {
            if (component(station) == -1) {
                val componentId = heaps.length
                val heap = scala.collection.mutable.PriorityQueue.empty[Int](Ordering.Int.reverse)
                heaps += heap
                val stack = scala.collection.mutable.ArrayBuffer(station)
                component(station) = componentId
                while (stack.nonEmpty) {
                    val node = stack.remove(stack.length - 1)
                    heap.enqueue(node)
                    for (neighbor <- graph(node)) {
                        if (component(neighbor) == -1) {
                            component(neighbor) = componentId
                            stack += neighbor
                        }
                    }
                }
            }
        }

        val online = Array.fill(c + 1)(true)
        val result = scala.collection.mutable.ArrayBuffer.empty[Int]
        for (query <- queries) {
            val queryType = query(0)
            val station = query(1)
            if (queryType == 2) {
                online(station) = false
            } else if (online(station)) {
                result += station
            } else {
                val heap = heaps(component(station))
                while (heap.nonEmpty && !online(heap.head)) heap.dequeue()
                result += (if (heap.nonEmpty) heap.head else -1)
            }
        }
        result.toArray
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn process_queries(c: i32, connections: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = c as usize;
        let mut graph = vec![Vec::new(); n + 1];
        for edge in connections {
            let u = edge[0] as usize;
            let v = edge[1] as usize;
            graph[u].push(v);
            graph[v].push(u);
        }

        let mut component = vec![usize::MAX; n + 1];
        let mut heaps: Vec<std::collections::BinaryHeap<std::cmp::Reverse<i32>>> = Vec::new();
        for station in 1..=n {
            if component[station] != usize::MAX {
                continue;
            }
            let component_id = heaps.len();
            let mut heap = std::collections::BinaryHeap::new();
            let mut stack = vec![station];
            component[station] = component_id;
            while let Some(node) = stack.pop() {
                heap.push(std::cmp::Reverse(node as i32));
                for &neighbor in &graph[node] {
                    if component[neighbor] == usize::MAX {
                        component[neighbor] = component_id;
                        stack.push(neighbor);
                    }
                }
            }
            heaps.push(heap);
        }

        let mut online = vec![true; n + 1];
        let mut result = Vec::new();
        for query in queries {
            let query_type = query[0];
            let station = query[1] as usize;
            if query_type == 2 {
                online[station] = false;
            } else if online[station] {
                result.push(station as i32);
            } else {
                let heap = &mut heaps[component[station]];
                while let Some(&std::cmp::Reverse(top)) = heap.peek() {
                    if online[top as usize] {
                        break;
                    }
                    heap.pop();
                }
                result.push(heap.peek().map_or(-1, |x| x.0));
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (process-queries c connections queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([graph (make-vector (add1 c) '())]
         [component (make-vector (add1 c) -1)])
    (for ([edge connections])
      (define u (first edge))
      (define v (second edge))
      (vector-set! graph u (cons v (vector-ref graph u)))
      (vector-set! graph v (cons u (vector-ref graph v))))
    (define heaps '())
    (for ([station (in-range 1 (add1 c))])
      (when (= (vector-ref component station) -1)
        (define component-id (length heaps))
        (define members '())
        (define stack (list station))
        (vector-set! component station component-id)
        (let loop ()
          (unless (null? stack)
            (define node (car stack))
            (set! stack (cdr stack))
            (set! members (cons node members))
            (for ([neighbor (vector-ref graph node)])
              (when (= (vector-ref component neighbor) -1)
                (vector-set! component neighbor component-id)
                (set! stack (cons neighbor stack))))
            (loop)))
        (set! heaps (append heaps (list (list->vector (sort members <)))))))
    (define heap-positions (make-vector (length heaps) 0))
    (define online (make-vector (add1 c) #t))
    (define result '())
    (for ([query queries])
      (define query-type (first query))
      (define station (second query))
      (cond
        [(= query-type 2) (vector-set! online station #f)]
        [(vector-ref online station) (set! result (cons station result))]
        [else
         (define component-id (vector-ref component station))
         (define heap (list-ref heaps component-id))
         (define position (vector-ref heap-positions component-id))
         (let loop ()
           (when (and (< position (vector-length heap))
                      (not (vector-ref online (vector-ref heap position))))
             (set! position (add1 position))
             (loop)))
         (vector-set! heap-positions component-id position)
         (set! result
               (cons (if (< position (vector-length heap))
                         (vector-ref heap position)
                         -1)
                     result))]))
    (reverse result)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec process_queries(C :: integer(), Connections :: [[integer()]], Queries :: [[integer()]]) -> [integer()].
process_queries(C, Connections, Queries) ->
  Graph0 = maps:from_list([{I, []} || I <- lists:seq(1, C)]),
  Graph = lists:foldl(
    fun([U, V], Acc) ->
      Acc1 = maps:update_with(U, fun(Neighbors) -> [V | Neighbors] end, Acc),
      maps:update_with(V, fun(Neighbors) -> [U | Neighbors] end, Acc1)
    end,
    Graph0,
    Connections
  ),
  {Components, Heaps} = build_components(lists:seq(1, C), Graph, #{}, []),
  Online = maps:from_list([{I, true} || I <- lists:seq(1, C)]),
  {_, _, Reversed} = lists:foldl(
    fun([2, Station], {CompMap, HeapList, Acc}) ->
          {CompMap, HeapList, Acc, maps:put(Station, false, Online)};
       ([1, Station], {CompMap, HeapList, Acc}) ->
          case maps:get(Station, Online) of
            true -> {CompMap, HeapList, [Station | Acc], Online};
            false ->
              ComponentId = maps:get(Station, CompMap),
              Heap = lists:nth(ComponentId, HeapList),
              {Answer, UpdatedHeap} = find_online(Heap, Online),
              {CompMap, replace_nth(ComponentId, UpdatedHeap, HeapList), [Answer | Acc], Online}
          end
    end,
    {Components, Heaps, [], Online},
    Queries
  ),
  lists:reverse(Reversed).

build_components([], _Graph, Components, Heaps) -> {Components, Heaps};
build_components([Station | Rest], Graph, Components, Heaps) ->
  case maps:is_key(Station, Components) of
    true -> build_components(Rest, Graph, Components, Heaps);
    false ->
      ComponentId = length(Heaps) + 1,
      {NewComponents, Members} = visit([Station], Graph, Components, ComponentId, []),
      build_components(Rest, Graph, NewComponents, Heaps ++ [lists:sort(Members)])
  end.

visit([], _Graph, Components, _ComponentId, Members) -> {Components, Members};
visit([Node | Stack], Graph, Components, ComponentId, Members) ->
  case maps:is_key(Node, Components) of
    true -> visit(Stack, Graph, Components, ComponentId, Members);
    false ->
      NewComponents = maps:put(Node, ComponentId, Components),
      Neighbors = maps:get(Node, Graph),
      visit(Neighbors ++ Stack, Graph, NewComponents, ComponentId, [Node | Members])
  end.

find_online([], _Online) -> {-1, []};
find_online([Station | Rest] = Heap, Online) ->
  case maps:get(Station, Online) of
    true -> {Station, Heap};
    false -> find_online(Rest, Online)
  end.

replace_nth(1, Value, [_ | Rest]) -> [Value | Rest];
replace_nth(N, Value, [Head | Rest]) -> [Head | replace_nth(N - 1, Value, Rest)].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec process_queries(c :: integer, connections :: [[integer]], queries :: [[integer]]) :: [integer]
  def process_queries(c, connections, queries) do
    graph =
      Enum.reduce(1..c, %{}, fn station, acc ->
        Map.put(acc, station, [])
      end)
      |> then(fn initial ->
        Enum.reduce(connections, initial, fn [u, v], acc ->
          acc
          |> Map.update!(u, &[v | &1])
          |> Map.update!(v, &[u | &1])
        end)
      end)

    {components, heaps} = build_components(1..c, graph, %{}, [])
    online = Map.new(1..c, &{&1, true})
    positions = Map.new(0..(length(heaps) - 1), &{&1, 0})

    {_, _, _, result} =
      Enum.reduce(queries, {components, heaps, {online, positions}, []}, fn
        [2, station], {component_map, heap_list, {status, pos}, acc} ->
          {component_map, heap_list, {Map.put(status, station, false), pos}, acc}

        [1, station], {component_map, heap_list, {status, pos}, acc} ->
          if Map.fetch!(status, station) do
            {component_map, heap_list, {status, pos}, [station | acc]}
          else
            component_id = Map.fetch!(component_map, station)
            heap = Enum.at(heap_list, component_id)
            start = Map.fetch!(pos, component_id)
            {answer, next_position} = first_online(heap, start, status)
            updated_positions = Map.put(pos, component_id, next_position)
            {component_map, heap_list, {status, updated_positions}, [answer | acc]}
          end
      end)

    Enum.reverse(result)
  end

  defp build_components(stations, graph, components, heaps) do
    Enum.reduce(stations, {components, heaps}, fn station, {component_map, heap_list} ->
      if Map.has_key?(component_map, station) do
        {component_map, heap_list}
      else
        component_id = length(heap_list)
        {updated_components, members} = visit([station], graph, component_map, component_id, [])
        {updated_components, heap_list ++ [Enum.sort(members)]}
      end
    end)
  end

  defp visit([], _graph, components, _component_id, members), do: {components, members}

  defp visit([node | stack], graph, components, component_id, members) do
    if Map.has_key?(components, node) do
      visit(stack, graph, components, component_id, members)
    else
      updated_components = Map.put(components, node, component_id)
      neighbors = Map.fetch!(graph, node)
      visit(neighbors ++ stack, graph, updated_components, component_id, [node | members])
    end
  end

  defp first_online(heap, position, online) do
    if position >= length(heap) do
      {-1, position}
    else
      station = Enum.at(heap, position)
      if Map.fetch!(online, station) do
        {station, position}
      else
        first_online(heap, position + 1, online)
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(c + n + q log c), where c is the number of stations, n is the number of connections, and q is the number of queries. Each station is pushed once and removed from a heap at most once.
- **Space Complexity:** O(c + n), for the adjacency lists, component IDs, online flags, and component heaps.
