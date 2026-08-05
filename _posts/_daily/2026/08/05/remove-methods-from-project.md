---
layout: post
title: "Remove Methods From Project"
date: 2026-08-05 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Depth-First Search", "Breadth-First Search", "Graph Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/remove-methods-from-project/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> remainingMethods(int n, int k,\
        \ vector<vector<int>>& invocations) {\n        vector<vector<int>> adj(n);\n\
        \        for (const auto& inv : invocations) {\n            adj[inv[0]].push_back(inv[1]);\n\
        \        }\n\n        vector<bool> suspicious(n, false);\n        vector<int>\
        \ q;\n        q.push_back(k);\n        suspicious[k] = true;\n\n        int\
        \ head = 0;\n        while (head < q.size()) {\n            int u = q[head++];\n\
        \            for (int v : adj[u]) {\n                if (!suspicious[v]) {\n\
        \                    suspicious[v] = true;\n                    q.push_back(v);\n\
        \                }\n            }\n        }\n\n        bool canRemove = true;\n\
        \        for (const auto& inv : invocations) {\n            if (!suspicious[inv[0]]\
        \ && suspicious[inv[1]]) {\n                canRemove = false;\n           \
        \     break;\n            }\n        }\n\n        vector<int> result;\n    \
        \    if (canRemove) {\n            for (int i = 0; i < n; ++i) {\n         \
        \       if (!suspicious[i]) result.push_back(i);\n            }\n        } else\
        \ {\n            for (int i = 0; i < n; ++i) {\n                result.push_back(i);\n\
        \            }\n        }\n\n        return result;\n    }\n};"
      java: "class Solution {\n    public List<Integer> remainingMethods(int n, int\
        \ k, int[][] invocations) {\n        List<Integer>[] adj = new ArrayList[n];\n\
        \        for (int i = 0; i < n; i++) {\n            adj[i] = new ArrayList<>();\n\
        \        }\n        for (int[] inv : invocations) {\n            adj[inv[0]].add(inv[1]);\n\
        \        }\n\n        boolean[] suspicious = new boolean[n];\n        Queue<Integer>\
        \ queue = new LinkedList<>();\n        queue.add(k);\n        suspicious[k]\
        \ = true;\n\n        while (!queue.isEmpty()) {\n            int u = queue.poll();\n\
        \            for (int v : adj[u]) {\n                if (!suspicious[v]) {\n\
        \                    suspicious[v] = true;\n                    queue.add(v);\n\
        \                }\n            }\n        }\n\n        boolean canRemove =\
        \ true;\n        for (int[] inv : invocations) {\n            if (!suspicious[inv[0]]\
        \ && suspicious[inv[1]]) {\n                canRemove = false;\n           \
        \     break;\n            }\n        }\n\n        List<Integer> result = new\
        \ ArrayList<>();\n        if (canRemove) {\n            for (int i = 0; i <\
        \ n; i++) {\n                if (!suspicious[i]) {\n                    result.add(i);\n\
        \                }\n            }\n        } else {\n            for (int i\
        \ = 0; i < n; i++) {\n                result.add(i);\n            }\n      \
        \  }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def remainingMethods(self, n, k, invocations):\n\
        \        \"\"\"\n        :type n: int\n        :type k: int\n        :type invocations:\
        \ List[List[int]]\n        :rtype: List[int]\n        \"\"\"\n        adj =\
        \ [[] for _ in range(n)]\n        for u, v in invocations:\n            adj[u].append(v)\n\
        \n        suspicious = [False] * n\n        suspicious[k] = True\n        stack\
        \ = [k]\n\n        while stack:\n            u = stack.pop()\n            for\
        \ v in adj[u]:\n                if not suspicious[v]:\n                    suspicious[v]\
        \ = True\n                    stack.append(v)\n\n        can_remove = True\n\
        \        for u, v in invocations:\n            if not suspicious[u] and suspicious[v]:\n\
        \                can_remove = False\n                break\n\n        if can_remove:\n\
        \            return [i for i in range(n) if not suspicious[i]]\n        else:\n\
        \            return list(range(n))"
      python3: "class Solution:\n    def remainingMethods(self, n: int, k: int, invocations:\
        \ List[List[int]]) -> List[int]:\n        adj = [[] for _ in range(n)]\n   \
        \     for u, v in invocations:\n            adj[u].append(v)\n\n        suspicious\
        \ = [False] * n\n        suspicious[k] = True\n        queue = collections.deque([k])\n\
        \n        while queue:\n            u = queue.popleft()\n            for v in\
        \ adj[u]:\n                if not suspicious[v]:\n                    suspicious[v]\
        \ = True\n                    queue.append(v)\n\n        can_remove = True\n\
        \        for u, v in invocations:\n            if not suspicious[u] and suspicious[v]:\n\
        \                can_remove = False\n                break\n\n        if can_remove:\n\
        \            return [i for i in range(n) if not suspicious[i]]\n        else:\n\
        \            return [i for i in range(n)]"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* remainingMethods(int n, int k, int** invocations, int invocationsSize,\
        \ int* invocationsColSize, int* returnSize) {\n    int* head = (int*)malloc(n\
        \ * sizeof(int));\n    for (int i = 0; i < n; i++) head[i] = -1;\n\n    int*\
        \ next = (int*)malloc(invocationsSize * sizeof(int));\n    int* to = (int*)malloc(invocationsSize\
        \ * sizeof(int));\n    for (int i = 0; i < invocationsSize; i++) {\n       \
        \ to[i] = invocations[i][1];\n        next[i] = head[invocations[i][0]];\n \
        \       head[invocations[i][0]] = i;\n    }\n\n    bool* suspicious = (bool*)calloc(n,\
        \ sizeof(bool));\n    int* queue = (int*)malloc(n * sizeof(int));\n    int front\
        \ = 0, rear = 0;\n\n    suspicious[k] = true;\n    queue[rear++] = k;\n\n  \
        \  while (front < rear) {\n        int u = queue[front++];\n        for (int\
        \ i = head[u]; i != -1; i = next[i]) {\n            int v = to[i];\n       \
        \     if (!suspicious[v]) {\n                suspicious[v] = true;\n       \
        \         queue[rear++] = v;\n            }\n        }\n    }\n\n    bool canRemove\
        \ = true;\n    for (int i = 0; i < invocationsSize; i++) {\n        if (!suspicious[invocations[i][0]]\
        \ && suspicious[invocations[i][1]]) {\n            canRemove = false;\n    \
        \        break;\n        }\n    }\n\n    int* result;\n    if (canRemove) {\n\
        \        int count = 0;\n        for (int i = 0; i < n; i++) {\n           \
        \ if (!suspicious[i]) count++;\n        }\n        *returnSize = count;\n  \
        \      result = (int*)malloc(count * sizeof(int));\n        int idx = 0;\n \
        \       for (int i = 0; i < n; i++) {\n            if (!suspicious[i]) result[idx++]\
        \ = i;\n        }\n    } else {\n        *returnSize = n;\n        result =\
        \ (int*)malloc(n * sizeof(int));\n        for (int i = 0; i < n; i++) result[i]\
        \ = i;\n    }\n\n    free(head);\n    free(next);\n    free(to);\n    free(suspicious);\n\
        \    free(queue);\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public IList<int> RemainingMethods(int n, int k, int[][] invocations)\
        \ {\n        List<int>[] adj = new List<int>[n];\n        for (int i = 0; i\
        \ < n; i++) {\n            adj[i] = new List<int>();\n        }\n\n        foreach\
        \ (var inv in invocations) {\n            adj[inv[0]].Add(inv[1]);\n       \
        \ }\n\n        bool[] isSuspicious = new bool[n];\n        Stack<int> stack\
        \ = new Stack<int>();\n\n        isSuspicious[k] = true;\n        stack.Push(k);\n\
        \n        while (stack.Count > 0) {\n            int u = stack.Pop();\n    \
        \        foreach (int v in adj[u]) {\n                if (!isSuspicious[v])\
        \ {\n                    isSuspicious[v] = true;\n                    stack.Push(v);\n\
        \                }\n            }\n        }\n\n        bool canRemove = true;\n\
        \        foreach (var inv in invocations) {\n            if (!isSuspicious[inv[0]]\
        \ && isSuspicious[inv[1]]) {\n                canRemove = false;\n         \
        \       break;\n            }\n        }\n\n        List<int> result = new List<int>();\n\
        \        if (canRemove) {\n            for (int i = 0; i < n; i++) {\n     \
        \           if (!isSuspicious[i]) {\n                    result.Add(i);\n  \
        \              }\n            }\n        } else {\n            for (int i =\
        \ 0; i < n; i++) {\n                result.Add(i);\n            }\n        }\n\
        \n        return result;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number} k\n * @param {number[][]}\
        \ invocations\n * @return {number[]}\n */\nvar remainingMethods = function(n,\
        \ k, invocations) {\n    const adj = Array.from({ length: n }, () => []);\n\
        \    for (let i = 0; i < invocations.length; i++) {\n        const [u, v] =\
        \ invocations[i];\n        adj[u].push(v);\n    }\n\n    const isSuspicious\
        \ = new Uint8Array(n);\n    isSuspicious[k] = 1;\n    const stack = [k];\n\n\
        \    while (stack.length > 0) {\n        const u = stack.pop();\n        const\
        \ neighbors = adj[u];\n        for (let i = 0; i < neighbors.length; i++) {\n\
        \            const v = neighbors[i];\n            if (!isSuspicious[v]) {\n\
        \                isSuspicious[v] = 1;\n                stack.push(v);\n    \
        \        }\n        }\n    }\n\n    let canRemove = true;\n    for (let i =\
        \ 0; i < invocations.length; i++) {\n        const [u, v] = invocations[i];\n\
        \        if (!isSuspicious[u] && isSuspicious[v]) {\n            canRemove =\
        \ false;\n            break;\n        }\n    }\n\n    const result = [];\n \
        \   if (canRemove) {\n        for (let i = 0; i < n; i++) {\n            if\
        \ (!isSuspicious[i]) {\n                result.push(i);\n            }\n   \
        \     }\n    } else {\n        for (let i = 0; i < n; i++) {\n            result.push(i);\n\
        \        }\n    }\n\n    return result;\n};"
      typescript: "function remainingMethods(n: number, k: number, invocations: number[][]):\
        \ number[] {\n    const adj: number[][] = Array.from({ length: n }, () => []);\n\
        \    for (const [u, v] of invocations) {\n        adj[u].push(v);\n    }\n\n\
        \    const isSuspicious: boolean[] = new Array(n).fill(false);\n    isSuspicious[k]\
        \ = true;\n    const stack: number[] = [k];\n\n    while (stack.length > 0)\
        \ {\n        const u = stack.pop()!;\n        const neighbors = adj[u];\n  \
        \      for (let i = 0; i < neighbors.length; i++) {\n            const v = neighbors[i];\n\
        \            if (!isSuspicious[v]) {\n                isSuspicious[v] = true;\n\
        \                stack.push(v);\n            }\n        }\n    }\n\n    let\
        \ canRemove: boolean = true;\n    for (const [u, v] of invocations) {\n    \
        \    if (!isSuspicious[u] && isSuspicious[v]) {\n            canRemove = false;\n\
        \            break;\n        }\n    }\n\n    const result: number[] = [];\n\
        \    if (canRemove) {\n        for (let i = 0; i < n; i++) {\n            if\
        \ (!isSuspicious[i]) {\n                result.push(i);\n            }\n   \
        \     }\n    } else {\n        for (let i = 0; i < n; i++) {\n            result.push(i);\n\
        \        }\n    }\n\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer\
        \ $k\n     * @param Integer[][] $invocations\n     * @return Integer[]\n   \
        \  */\n    function remainingMethods($n, $k, $invocations) {\n        $adj =\
        \ array_fill(0, $n, []);\n        foreach ($invocations as $inv) {\n       \
        \     $adj[$inv[0]][] = $inv[1];\n        }\n\n        $isSuspicious = array_fill(0,\
        \ $n, false);\n        $isSuspicious[$k] = true;\n        $stack = [$k];\n\n\
        \        while (!empty($stack)) {\n            $u = array_pop($stack);\n   \
        \         foreach ($adj[$u] as $v) {\n                if (!$isSuspicious[$v])\
        \ {\n                    $isSuspicious[$v] = true;\n                    $stack[]\
        \ = $v;\n                }\n            }\n        }\n\n        $canRemove =\
        \ true;\n        foreach ($invocations as $inv) {\n            if (!$isSuspicious[$inv[0]]\
        \ && $isSuspicious[$inv[1]]) {\n                $canRemove = false;\n      \
        \          break;\n            }\n        }\n\n        $result = [];\n     \
        \   if ($canRemove) {\n            for ($i = 0; $i < $n; $i++) {\n         \
        \       if (!$isSuspicious[$i]) {\n                    $result[] = $i;\n   \
        \             }\n            }\n        } else {\n            for ($i = 0; $i\
        \ < $n; $i++) {\n                $result[] = $i;\n            }\n        }\n\
        \n        return $result;\n    }\n}"
      swift: "class Solution {\n    func remainingMethods(_ n: Int, _ k: Int, _ invocations:\
        \ [[Int]]) -> [Int] {\n        var adj = [[Int]](repeating: [], count: n)\n\
        \        for inv in invocations {\n            adj[inv[0]].append(inv[1])\n\
        \        }\n\n        var isSuspicious = [Bool](repeating: false, count: n)\n\
        \        isSuspicious[k] = true\n        var stack = [k]\n\n        while !stack.isEmpty\
        \ {\n            let u = stack.removeLast()\n            for v in adj[u] {\n\
        \                if !isSuspicious[v] {\n                    isSuspicious[v]\
        \ = true\n                    stack.append(v)\n                }\n         \
        \   }\n        }\n\n        var canRemove = true\n        for inv in invocations\
        \ {\n            if !isSuspicious[inv[0]] && isSuspicious[inv[1]] {\n      \
        \          canRemove = false\n                break\n            }\n       \
        \ }\n\n        if canRemove {\n            var result = [Int]()\n          \
        \  for i in 0..<n {\n                if !isSuspicious[i] {\n               \
        \     result.append(i)\n                }\n            }\n            return\
        \ result\n        } else {\n            return Array(0..<n)\n        }\n   \
        \ }\n}"
      kotlin: "class Solution {\n    fun remainingMethods(n: Int, k: Int, invocations:\
        \ Array<IntArray>): List<Int> {\n        val adj = Array(n) { mutableListOf<Int>()\
        \ }\n        for (inv in invocations) {\n            adj[inv[0]].add(inv[1])\n\
        \        }\n\n        val isSuspicious = BooleanArray(n)\n        val queue\
        \ = java.util.ArrayDeque<Int>()\n\n        isSuspicious[k] = true\n        queue.add(k)\n\
        \n        while (queue.isNotEmpty()) {\n            val curr = queue.poll()\n\
        \            for (neighbor in adj[curr]) {\n                if (!isSuspicious[neighbor])\
        \ {\n                    isSuspicious[neighbor] = true\n                   \
        \ queue.add(neighbor)\n                }\n            }\n        }\n\n     \
        \   var canRemove = true\n        for (inv in invocations) {\n            val\
        \ u = inv[0]\n            val v = inv[1]\n            if (!isSuspicious[u] &&\
        \ isSuspicious[v]) {\n                canRemove = false\n                break\n\
        \            }\n        }\n\n        val result = mutableListOf<Int>()\n   \
        \     if (canRemove) {\n            for (i in 0 until n) {\n               \
        \ if (!isSuspicious[i]) {\n                    result.add(i)\n             \
        \   }\n            }\n        } else {\n            for (i in 0 until n) {\n\
        \                result.add(i)\n            }\n        }\n\n        return result\n\
        \    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  List<int> remainingMethods(int\
        \ n, int k, List<List<int>> invocations) {\n    List<List<int>> adj = List.generate(n,\
        \ (_) => []);\n    for (var inv in invocations) {\n      adj[inv[0]].add(inv[1]);\n\
        \    }\n\n    List<bool> isSuspicious = List.filled(n, false);\n    Queue<int>\
        \ queue = Queue<int>();\n\n    isSuspicious[k] = true;\n    queue.add(k);\n\n\
        \    while (queue.isNotEmpty) {\n      int curr = queue.removeFirst();\n   \
        \   for (int neighbor in adj[curr]) {\n        if (!isSuspicious[neighbor])\
        \ {\n          isSuspicious[neighbor] = true;\n          queue.add(neighbor);\n\
        \        }\n      }\n    }\n\n    bool canRemove = true;\n    for (var inv in\
        \ invocations) {\n      int u = inv[0];\n      int v = inv[1];\n      if (!isSuspicious[u]\
        \ && isSuspicious[v]) {\n        canRemove = false;\n        break;\n      }\n\
        \    }\n\n    List<int> result = [];\n    if (canRemove) {\n      for (int i\
        \ = 0; i < n; i++) {\n        if (!isSuspicious[i]) {\n          result.add(i);\n\
        \        }\n      }\n    } else {\n      for (int i = 0; i < n; i++) {\n   \
        \     result.add(i);\n      }\n    }\n\n    return result;\n  }\n}"
      go: "func remainingMethods(n int, k int, invocations [][]int) []int {\n    adj\
        \ := make([][]int, n)\n    for _, inv := range invocations {\n        adj[inv[0]]\
        \ = append(adj[inv[0]], inv[1])\n    }\n\n    isSuspicious := make([]bool, n)\n\
        \    isSuspicious[k] = true\n    queue := []int{k}\n\n    for len(queue) > 0\
        \ {\n        curr := queue[0]\n        queue = queue[1:]\n        for _, neighbor\
        \ := range adj[curr] {\n            if !isSuspicious[neighbor] {\n         \
        \       isSuspicious[neighbor] = true\n                queue = append(queue,\
        \ neighbor)\n            }\n        }\n    }\n\n    canRemove := true\n    for\
        \ _, inv := range invocations {\n        u, v := inv[0], inv[1]\n        if\
        \ !isSuspicious[u] && isSuspicious[v] {\n            canRemove = false\n   \
        \         break\n        }\n    }\n\n    result := []int{}\n    if canRemove\
        \ {\n        for i := 0; i < n; i++ {\n            if !isSuspicious[i] {\n \
        \               result = append(result, i)\n            }\n        }\n    }\
        \ else {\n        for i := 0; i < n; i++ {\n            result = append(result,\
        \ i)\n        }\n    }\n\n    return result\n}"
      ruby: "# @param {Integer} n\n# @param {Integer} k\n# @param {Integer[][]} invocations\n\
        # @return {Integer[]}\ndef remaining_methods(n, k, invocations)\n    adj = Array.new(n)\
        \ { [] }\n    invocations.each do |u, v|\n        adj[u] << v\n    end\n\n \
        \   is_suspicious = Array.new(n, false)\n    is_suspicious[k] = true\n    queue\
        \ = [k]\n\n    while !queue.empty?\n        curr = queue.shift\n        adj[curr].each\
        \ do |neighbor|\n            if !is_suspicious[neighbor]\n                is_suspicious[neighbor]\
        \ = true\n                queue << neighbor\n            end\n        end\n\
        \    end\n\n    can_remove = true\n    invocations.each do |u, v|\n        if\
        \ !is_suspicious[u] && is_suspicious[v]\n            can_remove = false\n  \
        \          break\n        end\n    end\n\n    result = []\n    if can_remove\n\
        \        (0...n).each do |i|\n            result << i if !is_suspicious[i]\n\
        \        end\n    else\n        (0...n).each do |i|\n            result << i\n\
        \        end\n    end\n\n    result\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def remainingMethods(n:\
        \ Int, k: Int, invocations: Array[Array[Int]]): List[Int] = {\n        val adj\
        \ = Array.fill(n)(mutable.ArrayBuffer[Int]())\n        for (inv <- invocations)\
        \ {\n            adj(inv(0)) += inv(1)\n        }\n\n        val isSuspicious\
        \ = Array.fill(n)(false)\n        val queue = mutable.Queue[Int]()\n\n     \
        \   isSuspicious(k) = true\n        queue.enqueue(k)\n\n        while (queue.nonEmpty)\
        \ {\n            val curr = queue.dequeue()\n            for (neighbor <- adj(curr))\
        \ {\n                if (!isSuspicious(neighbor)) {\n                    isSuspicious(neighbor)\
        \ = true\n                    queue.enqueue(neighbor)\n                }\n \
        \           }\n        }\n\n        var canRemove = true\n        var i = 0\n\
        \        while (i < invocations.length && canRemove) {\n            val u =\
        \ invocations(i)(0)\n            val v = invocations(i)(1)\n            if (!isSuspicious(u)\
        \ && isSuspicious(v)) {\n                canRemove = false\n            }\n\
        \            i += 1\n        }\n\n        val result = mutable.ListBuffer[Int]()\n\
        \        if (canRemove) {\n            for (j <- 0 until n) {\n            \
        \    if (!isSuspicious(j)) {\n                    result += j\n            \
        \    }\n            }\n        } else {\n            for (j <- 0 until n) {\n\
        \                result += j\n            }\n        }\n\n        result.toList\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn remaining_methods(n: i32, k: i32, invocations:\
        \ Vec<Vec<i32>>) -> Vec<i32> {\n        let n = n as usize;\n        let k =\
        \ k as usize;\n        let mut adj = vec![vec![]; n];\n        for inv in invocations.iter()\
        \ {\n            adj[inv[0] as usize].push(inv[1] as usize);\n        }\n\n\
        \        let mut suspicious = vec![false; n];\n        let mut stack = vec![k];\n\
        \        suspicious[k] = true;\n\n        while let Some(u) = stack.pop() {\n\
        \            for &v in &adj[u] {\n                if !suspicious[v] {\n    \
        \                suspicious[v] = true;\n                    stack.push(v);\n\
        \                }\n            }\n        }\n\n        let mut possible_to_remove\
        \ = true;\n        for inv in invocations.iter() {\n            let u = inv[0]\
        \ as usize;\n            let v = inv[1] as usize;\n            if !suspicious[u]\
        \ && suspicious[v] {\n                possible_to_remove = false;\n        \
        \        break;\n            }\n        }\n\n        if possible_to_remove {\n\
        \            (0..n as i32)\n                .filter(|&i| !suspicious[i as usize])\n\
        \                .collect()\n        } else {\n            (0..n as i32).collect()\n\
        \        }\n    }\n}"
      racket: "(define/contract (remaining-methods n k invocations)\n  (-> exact-integer?\
        \ exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))\n\
        \  (let* ([adj (make-vector n '())]\n         [suspicious (make-vector n #f)])\n\
        \    (for ([inv invocations])\n      (let ([u (car inv)]\n            [v (cadr\
        \ inv)])\n        (vector-set! adj u (cons v (vector-ref adj u)))))\n\n    (let\
        \ loop ([stack (list k)])\n      (cond\n        [(not (null? stack))\n     \
        \    (let ([u (car stack)]\n               [rest (cdr stack)])\n           (if\
        \ (vector-ref suspicious u)\n               (loop rest)\n               (begin\n\
        \                 (vector-set! suspicious u #t)\n                 (loop (append\
        \ (vector-ref adj u) rest)))))]))\n\n    (let ([possible-to-remove #t])\n  \
        \    (for ([inv invocations])\n        (let ([u (car inv)]\n              [v\
        \ (cadr inv)])\n          (when (and (not (vector-ref suspicious u)) (vector-ref\
        \ suspicious v))\n            (set! possible-to-remove #f))))\n\n      (if possible-to-remove\n\
        \          (let ([result '()])\n            (for ([i (in-range (- n 1) -1 -1)])\n\
        \              (when (not (vector-ref suspicious i))\n                (set!\
        \ result (cons i result))))\n            result)\n          (let ([result '()])\n\
        \            (for ([i (in-range (- n 1) -1 -1)])\n              (set! result\
        \ (cons i result)))\n            result)))))"
      erlang: "-spec remaining_methods(N :: integer(), K :: integer(), Invocations ::\
        \ [[integer()]]) -> [integer()].\nremaining_methods(N, K, Invocations) ->\n\
        \    Adj = lists:foldl(fun([U, V], Acc) ->\n        maps:put(U, [V | maps:get(U,\
        \ Acc, [])], Acc)\n    end, #{}, Invocations),\n\n    Suspicious = find_suspicious([K],\
        \ Adj, #{K => true}),\n\n    CanRemove = lists:all(fun([U, V]) ->\n        IsUSusp\
        \ = maps:is_key(U, Suspicious),\n        IsVSusp = maps:is_key(V, Suspicious),\n\
        \        not (not IsUSusp andalso IsVSusp)\n    end, Invocations),\n\n    if\n\
        \        CanRemove ->\n            [I || I <- lists:seq(0, N - 1), not maps:is_key(I,\
        \ Suspicious)];\n        true ->\n            lists:seq(0, N - 1)\n    end.\n\
        \nfind_suspicious([], _Adj, Visited) -> Visited;\nfind_suspicious([U | Rest],\
        \ Adj, Visited) ->\n    Neighbors = maps:get(U, Adj, []),\n    NewToVisit =\
        \ [V || V <- Neighbors, not maps:is_key(V, Visited)],\n    NewVisited = lists:foldl(fun(V,\
        \ Acc) -> maps:put(V, true, Acc) end, Visited, NewToVisit),\n    find_suspicious(NewToVisit\
        \ ++ Rest, Adj, NewVisited)."
      elixir: "defmodule Solution do\n  @spec remaining_methods(n :: integer, k :: integer,\
        \ invocations :: [[integer]]) :: [integer]\n  def remaining_methods(n, k, invocations)\
        \ do\n    adj = Enum.reduce(invocations, %{}, fn [u, v], acc ->\n      Map.update(acc,\
        \ u, [v], &[v | &1])\n    end)\n\n    suspicious = find_suspicious([k], adj,\
        \ MapSet.new([k]))\n\n    can_remove = Enum.all?(invocations, fn [u, v] ->\n\
        \      is_u_susp = MapSet.member?(suspicious, u)\n      is_v_susp = MapSet.member?(suspicious,\
        \ v)\n      !( !is_u_susp && is_v_susp )\n    end)\n\n    if can_remove do\n\
        \      Enum.filter(0..(n - 1), fn i -> !MapSet.member?(suspicious, i) end)\n\
        \    else\n      Enum.to_list(0..(n - 1))\n    end\n  end\n\n  defp find_suspicious([],\
        \ _adj, visited), do: visited\n  defp find_suspicious([u | rest], adj, visited)\
        \ do\n    neighbors = Map.get(adj, u, [])\n    new_nodes = Enum.filter(neighbors,\
        \ fn v -> !MapSet.member?(visited, v) end)\n    new_visited = Enum.reduce(new_nodes,\
        \ visited, fn v, acc -> MapSet.put(acc, v) end)\n    find_suspicious(new_nodes\
        \ ++ rest, adj, new_visited)\n  end\nend"
    approach: The problem asks to identify a 'suspicious' group of methods starting
      from method k and determine if they can be removed. A method is suspicious if
      it is reachable from k in the invocation graph. We first identify all suspicious
      methods by building an adjacency list and performing a traversal (BFS or DFS)
      starting from node k. This traversal marks every reachable method as suspicious.
      Since n and the number of invocations are up to $10^5$ and $2 \cdot 10^5$ respectively,
      a standard linear time traversal is efficient enough.
    time_complexity: O(n + m) where n is the number of methods and m is the number of
      invocations. We iterate through the invocations twice (once to build the graph
      and once to check the removal condition) and perform a traversal that visits each
      node and edge at most once.
    space_complexity: O(n + m) to store the adjacency list representation of the invocations,
      the suspicious status of each method, and the queue or stack used during traversal.
    elapsed_time: 757.0932745933533
    model: gemini-3-flash-preview
    generated_at: '2026-08-05 02:03:11 '
---

## Problem #3310: Remove Methods From Project

**Difficulty:** Medium

**Topics:** Depth-First Search, Breadth-First Search, Graph Theory

## Problem Description

<p>You are maintaining a project that has <code>n</code> methods numbered from <code>0</code> to <code>n - 1</code>.</p>

<p>You are given two integers <code>n</code> and <code>k</code>, and a 2D integer array <code>invocations</code>, where <code>invocations[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that method <code>a<sub>i</sub></code> invokes method <code>b<sub>i</sub></code>.</p>

<p>There is a known bug in method <code>k</code>. Method <code>k</code>, along with any method invoked by it, either <strong>directly</strong> or <strong>indirectly</strong>, are considered <strong>suspicious</strong> and we aim to remove them.</p>

<p>A group of methods can only be removed if no method <strong>outside</strong> the group invokes any methods <strong>within</strong> it.</p>

<p>Return an array containing all the remaining methods after removing all the <strong>suspicious</strong> methods. You may return the answer in <em>any order</em>. If it is not possible to remove <strong>all</strong> the suspicious methods, <strong>none</strong> should be removed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1,2,3]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/07/18/graph-2.png" style="width: 200px; height: 200px;" /></p>

<p>Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,4]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/07/18/graph-3.png" style="width: 200px; height: 200px;" /></p>

<p>Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/07/20/graph.png" style="width: 200px; height: 200px;" /></p>

<p>All methods are suspicious. We can remove them.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= n - 1</code></li>
	<li><code>0 &lt;= invocations.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>invocations[i] == [a<sub>i</sub>, b<sub>i</sub>]</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>invocations[i] != invocations[j]</code></li>
</ul>


## Hints

1. Use DFS from node `k`.

2. Mark all the nodes visited from node `k`, and then check if they can be visited from the other nodes.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to identify a 'suspicious' group of methods starting from method k and determine if they can be removed. A method is suspicious if it is reachable from k in the invocation graph. We first identify all suspicious methods by building an adjacency list and performing a traversal (BFS or DFS) starting from node k. This traversal marks every reachable method as suspicious. Since n and the number of invocations are up to $10^5$ and $2 \cdot 10^5$ respectively, a standard linear time traversal is efficient enough.

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
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        vector<vector<int>> adj(n);
        for (const auto& inv : invocations) {
            adj[inv[0]].push_back(inv[1]);
        }

        vector<bool> suspicious(n, false);
        vector<int> q;
        q.push_back(k);
        suspicious[k] = true;

        int head = 0;
        while (head < q.size()) {
            int u = q[head++];
            for (int v : adj[u]) {
                if (!suspicious[v]) {
                    suspicious[v] = true;
                    q.push_back(v);
                }
            }
        }

        bool canRemove = true;
        for (const auto& inv : invocations) {
            if (!suspicious[inv[0]] && suspicious[inv[1]]) {
                canRemove = false;
                break;
            }
        }

        vector<int> result;
        if (canRemove) {
            for (int i = 0; i < n; ++i) {
                if (!suspicious[i]) result.push_back(i);
            }
        } else {
            for (int i = 0; i < n; ++i) {
                result.push_back(i);
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
class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] inv : invocations) {
            adj[inv[0]].add(inv[1]);
        }

        boolean[] suspicious = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(k);
        suspicious[k] = true;

        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : adj[u]) {
                if (!suspicious[v]) {
                    suspicious[v] = true;
                    queue.add(v);
                }
            }
        }

        boolean canRemove = true;
        for (int[] inv : invocations) {
            if (!suspicious[inv[0]] && suspicious[inv[1]]) {
                canRemove = false;
                break;
            }
        }

        List<Integer> result = new ArrayList<>();
        if (canRemove) {
            for (int i = 0; i < n; i++) {
                if (!suspicious[i]) {
                    result.add(i);
                }
            }
        } else {
            for (int i = 0; i < n; i++) {
                result.add(i);
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        suspicious = [False] * n
        suspicious[k] = True
        stack = [k]

        while stack:
            u = stack.pop()
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    stack.append(v)

        can_remove = True
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                can_remove = False
                break

        if can_remove:
            return [i for i in range(n) if not suspicious[i]]
        else:
            return list(range(n))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        suspicious = [False] * n
        suspicious[k] = True
        queue = collections.deque([k])

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    queue.append(v)

        can_remove = True
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                can_remove = False
                break

        if can_remove:
            return [i for i in range(n) if not suspicious[i]]
        else:
            return [i for i in range(n)]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* remainingMethods(int n, int k, int** invocations, int invocationsSize, int* invocationsColSize, int* returnSize) {
    int* head = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) head[i] = -1;

    int* next = (int*)malloc(invocationsSize * sizeof(int));
    int* to = (int*)malloc(invocationsSize * sizeof(int));
    for (int i = 0; i < invocationsSize; i++) {
        to[i] = invocations[i][1];
        next[i] = head[invocations[i][0]];
        head[invocations[i][0]] = i;
    }

    bool* suspicious = (bool*)calloc(n, sizeof(bool));
    int* queue = (int*)malloc(n * sizeof(int));
    int front = 0, rear = 0;

    suspicious[k] = true;
    queue[rear++] = k;

    while (front < rear) {
        int u = queue[front++];
        for (int i = head[u]; i != -1; i = next[i]) {
            int v = to[i];
            if (!suspicious[v]) {
                suspicious[v] = true;
                queue[rear++] = v;
            }
        }
    }

    bool canRemove = true;
    for (int i = 0; i < invocationsSize; i++) {
        if (!suspicious[invocations[i][0]] && suspicious[invocations[i][1]]) {
            canRemove = false;
            break;
        }
    }

    int* result;
    if (canRemove) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!suspicious[i]) count++;
        }
        *returnSize = count;
        result = (int*)malloc(count * sizeof(int));
        int idx = 0;
        for (int i = 0; i < n; i++) {
            if (!suspicious[i]) result[idx++] = i;
        }
    } else {
        *returnSize = n;
        result = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++) result[i] = i;
    }

    free(head);
    free(next);
    free(to);
    free(suspicious);
    free(queue);
    return result;
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
    public IList<int> RemainingMethods(int n, int k, int[][] invocations) {
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new List<int>();
        }

        foreach (var inv in invocations) {
            adj[inv[0]].Add(inv[1]);
        }

        bool[] isSuspicious = new bool[n];
        Stack<int> stack = new Stack<int>();

        isSuspicious[k] = true;
        stack.Push(k);

        while (stack.Count > 0) {
            int u = stack.Pop();
            foreach (int v in adj[u]) {
                if (!isSuspicious[v]) {
                    isSuspicious[v] = true;
                    stack.Push(v);
                }
            }
        }

        bool canRemove = true;
        foreach (var inv in invocations) {
            if (!isSuspicious[inv[0]] && isSuspicious[inv[1]]) {
                canRemove = false;
                break;
            }
        }

        List<int> result = new List<int>();
        if (canRemove) {
            for (int i = 0; i < n; i++) {
                if (!isSuspicious[i]) {
                    result.Add(i);
                }
            }
        } else {
            for (int i = 0; i < n; i++) {
                result.Add(i);
            }
        }

        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @param {number} k
 * @param {number[][]} invocations
 * @return {number[]}
 */
var remainingMethods = function(n, k, invocations) {
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < invocations.length; i++) {
        const [u, v] = invocations[i];
        adj[u].push(v);
    }

    const isSuspicious = new Uint8Array(n);
    isSuspicious[k] = 1;
    const stack = [k];

    while (stack.length > 0) {
        const u = stack.pop();
        const neighbors = adj[u];
        for (let i = 0; i < neighbors.length; i++) {
            const v = neighbors[i];
            if (!isSuspicious[v]) {
                isSuspicious[v] = 1;
                stack.push(v);
            }
        }
    }

    let canRemove = true;
    for (let i = 0; i < invocations.length; i++) {
        const [u, v] = invocations[i];
        if (!isSuspicious[u] && isSuspicious[v]) {
            canRemove = false;
            break;
        }
    }

    const result = [];
    if (canRemove) {
        for (let i = 0; i < n; i++) {
            if (!isSuspicious[i]) {
                result.push(i);
            }
        }
    } else {
        for (let i = 0; i < n; i++) {
            result.push(i);
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
function remainingMethods(n: number, k: number, invocations: number[][]): number[] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of invocations) {
        adj[u].push(v);
    }

    const isSuspicious: boolean[] = new Array(n).fill(false);
    isSuspicious[k] = true;
    const stack: number[] = [k];

    while (stack.length > 0) {
        const u = stack.pop()!;
        const neighbors = adj[u];
        for (let i = 0; i < neighbors.length; i++) {
            const v = neighbors[i];
            if (!isSuspicious[v]) {
                isSuspicious[v] = true;
                stack.push(v);
            }
        }
    }

    let canRemove: boolean = true;
    for (const [u, v] of invocations) {
        if (!isSuspicious[u] && isSuspicious[v]) {
            canRemove = false;
            break;
        }
    }

    const result: number[] = [];
    if (canRemove) {
        for (let i = 0; i < n; i++) {
            if (!isSuspicious[i]) {
                result.push(i);
            }
        }
    } else {
        for (let i = 0; i < n; i++) {
            result.push(i);
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
     * @param Integer $n
     * @param Integer $k
     * @param Integer[][] $invocations
     * @return Integer[]
     */
    function remainingMethods($n, $k, $invocations) {
        $adj = array_fill(0, $n, []);
        foreach ($invocations as $inv) {
            $adj[$inv[0]][] = $inv[1];
        }

        $isSuspicious = array_fill(0, $n, false);
        $isSuspicious[$k] = true;
        $stack = [$k];

        while (!empty($stack)) {
            $u = array_pop($stack);
            foreach ($adj[$u] as $v) {
                if (!$isSuspicious[$v]) {
                    $isSuspicious[$v] = true;
                    $stack[] = $v;
                }
            }
        }

        $canRemove = true;
        foreach ($invocations as $inv) {
            if (!$isSuspicious[$inv[0]] && $isSuspicious[$inv[1]]) {
                $canRemove = false;
                break;
            }
        }

        $result = [];
        if ($canRemove) {
            for ($i = 0; $i < $n; $i++) {
                if (!$isSuspicious[$i]) {
                    $result[] = $i;
                }
            }
        } else {
            for ($i = 0; $i < $n; $i++) {
                $result[] = $i;
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
    func remainingMethods(_ n: Int, _ k: Int, _ invocations: [[Int]]) -> [Int] {
        var adj = [[Int]](repeating: [], count: n)
        for inv in invocations {
            adj[inv[0]].append(inv[1])
        }

        var isSuspicious = [Bool](repeating: false, count: n)
        isSuspicious[k] = true
        var stack = [k]

        while !stack.isEmpty {
            let u = stack.removeLast()
            for v in adj[u] {
                if !isSuspicious[v] {
                    isSuspicious[v] = true
                    stack.append(v)
                }
            }
        }

        var canRemove = true
        for inv in invocations {
            if !isSuspicious[inv[0]] && isSuspicious[inv[1]] {
                canRemove = false
                break
            }
        }

        if canRemove {
            var result = [Int]()
            for i in 0..<n {
                if !isSuspicious[i] {
                    result.append(i)
                }
            }
            return result
        } else {
            return Array(0..<n)
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun remainingMethods(n: Int, k: Int, invocations: Array<IntArray>): List<Int> {
        val adj = Array(n) { mutableListOf<Int>() }
        for (inv in invocations) {
            adj[inv[0]].add(inv[1])
        }

        val isSuspicious = BooleanArray(n)
        val queue = java.util.ArrayDeque<Int>()

        isSuspicious[k] = true
        queue.add(k)

        while (queue.isNotEmpty()) {
            val curr = queue.poll()
            for (neighbor in adj[curr]) {
                if (!isSuspicious[neighbor]) {
                    isSuspicious[neighbor] = true
                    queue.add(neighbor)
                }
            }
        }

        var canRemove = true
        for (inv in invocations) {
            val u = inv[0]
            val v = inv[1]
            if (!isSuspicious[u] && isSuspicious[v]) {
                canRemove = false
                break
            }
        }

        val result = mutableListOf<Int>()
        if (canRemove) {
            for (i in 0 until n) {
                if (!isSuspicious[i]) {
                    result.add(i)
                }
            }
        } else {
            for (i in 0 until n) {
                result.add(i)
            }
        }

        return result
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
  List<int> remainingMethods(int n, int k, List<List<int>> invocations) {
    List<List<int>> adj = List.generate(n, (_) => []);
    for (var inv in invocations) {
      adj[inv[0]].add(inv[1]);
    }

    List<bool> isSuspicious = List.filled(n, false);
    Queue<int> queue = Queue<int>();

    isSuspicious[k] = true;
    queue.add(k);

    while (queue.isNotEmpty) {
      int curr = queue.removeFirst();
      for (int neighbor in adj[curr]) {
        if (!isSuspicious[neighbor]) {
          isSuspicious[neighbor] = true;
          queue.add(neighbor);
        }
      }
    }

    bool canRemove = true;
    for (var inv in invocations) {
      int u = inv[0];
      int v = inv[1];
      if (!isSuspicious[u] && isSuspicious[v]) {
        canRemove = false;
        break;
      }
    }

    List<int> result = [];
    if (canRemove) {
      for (int i = 0; i < n; i++) {
        if (!isSuspicious[i]) {
          result.add(i);
        }
      }
    } else {
      for (int i = 0; i < n; i++) {
        result.add(i);
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
func remainingMethods(n int, k int, invocations [][]int) []int {
    adj := make([][]int, n)
    for _, inv := range invocations {
        adj[inv[0]] = append(adj[inv[0]], inv[1])
    }

    isSuspicious := make([]bool, n)
    isSuspicious[k] = true
    queue := []int{k}

    for len(queue) > 0 {
        curr := queue[0]
        queue = queue[1:]
        for _, neighbor := range adj[curr] {
            if !isSuspicious[neighbor] {
                isSuspicious[neighbor] = true
                queue = append(queue, neighbor)
            }
        }
    }

    canRemove := true
    for _, inv := range invocations {
        u, v := inv[0], inv[1]
        if !isSuspicious[u] && isSuspicious[v] {
            canRemove = false
            break
        }
    }

    result := []int{}
    if canRemove {
        for i := 0; i < n; i++ {
            if !isSuspicious[i] {
                result = append(result, i)
            }
        }
    } else {
        for i := 0; i < n; i++ {
            result = append(result, i)
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
# @param {Integer} n
# @param {Integer} k
# @param {Integer[][]} invocations
# @return {Integer[]}
def remaining_methods(n, k, invocations)
    adj = Array.new(n) { [] }
    invocations.each do |u, v|
        adj[u] << v
    end

    is_suspicious = Array.new(n, false)
    is_suspicious[k] = true
    queue = [k]

    while !queue.empty?
        curr = queue.shift
        adj[curr].each do |neighbor|
            if !is_suspicious[neighbor]
                is_suspicious[neighbor] = true
                queue << neighbor
            end
        end
    end

    can_remove = true
    invocations.each do |u, v|
        if !is_suspicious[u] && is_suspicious[v]
            can_remove = false
            break
        end
    end

    result = []
    if can_remove
        (0...n).each do |i|
            result << i if !is_suspicious[i]
        end
    else
        (0...n).each do |i|
            result << i
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
import scala.collection.mutable

object Solution {
    def remainingMethods(n: Int, k: Int, invocations: Array[Array[Int]]): List[Int] = {
        val adj = Array.fill(n)(mutable.ArrayBuffer[Int]())
        for (inv <- invocations) {
            adj(inv(0)) += inv(1)
        }

        val isSuspicious = Array.fill(n)(false)
        val queue = mutable.Queue[Int]()

        isSuspicious(k) = true
        queue.enqueue(k)

        while (queue.nonEmpty) {
            val curr = queue.dequeue()
            for (neighbor <- adj(curr)) {
                if (!isSuspicious(neighbor)) {
                    isSuspicious(neighbor) = true
                    queue.enqueue(neighbor)
                }
            }
        }

        var canRemove = true
        var i = 0
        while (i < invocations.length && canRemove) {
            val u = invocations(i)(0)
            val v = invocations(i)(1)
            if (!isSuspicious(u) && isSuspicious(v)) {
                canRemove = false
            }
            i += 1
        }

        val result = mutable.ListBuffer[Int]()
        if (canRemove) {
            for (j <- 0 until n) {
                if (!isSuspicious(j)) {
                    result += j
                }
            }
        } else {
            for (j <- 0 until n) {
                result += j
            }
        }

        result.toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn remaining_methods(n: i32, k: i32, invocations: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let k = k as usize;
        let mut adj = vec![vec![]; n];
        for inv in invocations.iter() {
            adj[inv[0] as usize].push(inv[1] as usize);
        }

        let mut suspicious = vec![false; n];
        let mut stack = vec![k];
        suspicious[k] = true;

        while let Some(u) = stack.pop() {
            for &v in &adj[u] {
                if !suspicious[v] {
                    suspicious[v] = true;
                    stack.push(v);
                }
            }
        }

        let mut possible_to_remove = true;
        for inv in invocations.iter() {
            let u = inv[0] as usize;
            let v = inv[1] as usize;
            if !suspicious[u] && suspicious[v] {
                possible_to_remove = false;
                break;
            }
        }

        if possible_to_remove {
            (0..n as i32)
                .filter(|&i| !suspicious[i as usize])
                .collect()
        } else {
            (0..n as i32).collect()
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (remaining-methods n k invocations)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([adj (make-vector n '())]
         [suspicious (make-vector n #f)])
    (for ([inv invocations])
      (let ([u (car inv)]
            [v (cadr inv)])
        (vector-set! adj u (cons v (vector-ref adj u)))))

    (let loop ([stack (list k)])
      (cond
        [(not (null? stack))
         (let ([u (car stack)]
               [rest (cdr stack)])
           (if (vector-ref suspicious u)
               (loop rest)
               (begin
                 (vector-set! suspicious u #t)
                 (loop (append (vector-ref adj u) rest)))))]))

    (let ([possible-to-remove #t])
      (for ([inv invocations])
        (let ([u (car inv)]
              [v (cadr inv)])
          (when (and (not (vector-ref suspicious u)) (vector-ref suspicious v))
            (set! possible-to-remove #f))))

      (if possible-to-remove
          (let ([result '()])
            (for ([i (in-range (- n 1) -1 -1)])
              (when (not (vector-ref suspicious i))
                (set! result (cons i result))))
            result)
          (let ([result '()])
            (for ([i (in-range (- n 1) -1 -1)])
              (set! result (cons i result)))
            result)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec remaining_methods(N :: integer(), K :: integer(), Invocations :: [[integer()]]) -> [integer()].
remaining_methods(N, K, Invocations) ->
    Adj = lists:foldl(fun([U, V], Acc) ->
        maps:put(U, [V | maps:get(U, Acc, [])], Acc)
    end, #{}, Invocations),

    Suspicious = find_suspicious([K], Adj, #{K => true}),

    CanRemove = lists:all(fun([U, V]) ->
        IsUSusp = maps:is_key(U, Suspicious),
        IsVSusp = maps:is_key(V, Suspicious),
        not (not IsUSusp andalso IsVSusp)
    end, Invocations),

    if
        CanRemove ->
            [I || I <- lists:seq(0, N - 1), not maps:is_key(I, Suspicious)];
        true ->
            lists:seq(0, N - 1)
    end.

find_suspicious([], _Adj, Visited) -> Visited;
find_suspicious([U | Rest], Adj, Visited) ->
    Neighbors = maps:get(U, Adj, []),
    NewToVisit = [V || V <- Neighbors, not maps:is_key(V, Visited)],
    NewVisited = lists:foldl(fun(V, Acc) -> maps:put(V, true, Acc) end, Visited, NewToVisit),
    find_suspicious(NewToVisit ++ Rest, Adj, NewVisited).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec remaining_methods(n :: integer, k :: integer, invocations :: [[integer]]) :: [integer]
  def remaining_methods(n, k, invocations) do
    adj = Enum.reduce(invocations, %{}, fn [u, v], acc ->
      Map.update(acc, u, [v], &[v | &1])
    end)

    suspicious = find_suspicious([k], adj, MapSet.new([k]))

    can_remove = Enum.all?(invocations, fn [u, v] ->
      is_u_susp = MapSet.member?(suspicious, u)
      is_v_susp = MapSet.member?(suspicious, v)
      !( !is_u_susp && is_v_susp )
    end)

    if can_remove do
      Enum.filter(0..(n - 1), fn i -> !MapSet.member?(suspicious, i) end)
    else
      Enum.to_list(0..(n - 1))
    end
  end

  defp find_suspicious([], _adj, visited), do: visited
  defp find_suspicious([u | rest], adj, visited) do
    neighbors = Map.get(adj, u, [])
    new_nodes = Enum.filter(neighbors, fn v -> !MapSet.member?(visited, v) end)
    new_visited = Enum.reduce(new_nodes, visited, fn v, acc -> MapSet.put(acc, v) end)
    find_suspicious(new_nodes ++ rest, adj, new_visited)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n + m) where n is the number of methods and m is the number of invocations. We iterate through the invocations twice (once to build the graph and once to check the removal condition) and perform a traversal that visits each node and edge at most once.
- **Space Complexity:** O(n + m) to store the adjacency list representation of the invocations, the suspicious status of each method, and the queue or stack used during traversal.
