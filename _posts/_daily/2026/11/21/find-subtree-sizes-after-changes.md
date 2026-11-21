---
layout: post
title: "Find Subtree Sizes After Changes"
date: 2026-11-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "String", "Tree", "Depth-First Search"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-subtree-sizes-after-changes/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> findSubtreeSizes(vector<int>&\
        \ parent, string s) {\n        int n = parent.size();\n        vector<vector<int>>\
        \ adj(n);\n        for (int i = 1; i < n; ++i) {\n            adj[parent[i]].push_back(i);\n\
        \        }\n\n        vector<int> last_seen(26, -1);\n        vector<int> prev_val(n,\
        \ -1);\n        vector<int> new_parent(n, -1);\n\n        vector<int> st;\n\
        \        st.push_back(0);\n        int c0 = s[0] - 'a';\n        prev_val[0]\
        \ = last_seen[c0];\n        last_seen[c0] = 0;\n\n        vector<int> edge_idx(n,\
        \ 0);\n\n        while (!st.empty()) {\n            int u = st.back();\n   \
        \         if (edge_idx[u] < adj[u].size()) {\n                int v = adj[u][edge_idx[u]++];\n\
        \                int cv = s[v] - 'a';\n                new_parent[v] = (last_seen[cv]\
        \ != -1) ? last_seen[cv] : parent[v];\n                prev_val[v] = last_seen[cv];\n\
        \                last_seen[cv] = v;\n                st.push_back(v);\n    \
        \        } else {\n                int cu = s[u] - 'a';\n                last_seen[cu]\
        \ = prev_val[u];\n                st.pop_back();\n            }\n        }\n\
        \n        vector<int> deg(n, 0);\n        for (int i = 1; i < n; ++i) {\n  \
        \          deg[new_parent[i]]++;\n        }\n\n        vector<int> ans(n, 1);\n\
        \        queue<int> q;\n        for (int i = 0; i < n; ++i) {\n            if\
        \ (deg[i] == 0) {\n                q.push(i);\n            }\n        }\n\n\
        \        while (!q.empty()) {\n            int u = q.front();\n            q.pop();\n\
        \            int p = new_parent[u];\n            if (p != -1) {\n          \
        \      ans[p] += ans[u];\n                if (--deg[p] == 0) {\n           \
        \         q.push(p);\n                }\n            }\n        }\n\n      \
        \  return ans;\n    }\n};"
      java: "class Solution {\n    public int[] findSubtreeSizes(int[] parent, String\
        \ s) {\n        int n = parent.length;\n        int[] head = new int[n];\n \
        \       Arrays.fill(head, -1);\n        int[] to = new int[n];\n        int[]\
        \ next = new int[n];\n        for (int i = 1; i < n; i++) {\n            to[i]\
        \ = i;\n            next[i] = head[parent[i]];\n            head[parent[i]]\
        \ = i;\n        }\n\n        int[] curEdge = new int[n];\n        System.arraycopy(head,\
        \ 0, curEdge, 0, n);\n\n        int[] st = new int[n];\n        int top = 0;\n\
        \        st[top++] = 0;\n\n        int[] lastSeen = new int[26];\n        Arrays.fill(lastSeen,\
        \ -1);\n        int[] prevVal = new int[n];\n        int c0 = s.charAt(0) -\
        \ 'a';\n        prevVal[0] = lastSeen[c0];\n        lastSeen[c0] = 0;\n\n  \
        \      int[] newParent = new int[n];\n        newParent[0] = -1;\n\n       \
        \ while (top > 0) {\n            int u = st[top - 1];\n            if (curEdge[u]\
        \ != -1) {\n                int e = curEdge[u];\n                curEdge[u]\
        \ = next[e];\n                int v = to[e];\n                int cv = s.charAt(v)\
        \ - 'a';\n                newParent[v] = (lastSeen[cv] != -1) ? lastSeen[cv]\
        \ : parent[v];\n                prevVal[v] = lastSeen[cv];\n               \
        \ lastSeen[cv] = v;\n                st[top++] = v;\n            } else {\n\
        \                int cu = s.charAt(u) - 'a';\n                lastSeen[cu] =\
        \ prevVal[u];\n                top--;\n            }\n        }\n\n        int[]\
        \ deg = new int[n];\n        for (int i = 1; i < n; i++) {\n            deg[newParent[i]]++;\n\
        \        }\n\n        int[] ans = new int[n];\n        Arrays.fill(ans, 1);\n\
        \n        int[] q = new int[n];\n        int qHead = 0, qTail = 0;\n       \
        \ for (int i = 0; i < n; i++) {\n            if (deg[i] == 0) {\n          \
        \      q[qTail++] = i;\n            }\n        }\n\n        while (qHead < qTail)\
        \ {\n            int u = q[qHead++];\n            int p = newParent[u];\n  \
        \          if (p != -1) {\n                ans[p] += ans[u];\n             \
        \   deg[p]--;\n                if (deg[p] == 0) {\n                    q[qTail++]\
        \ = p;\n                }\n            }\n        }\n\n        return ans;\n\
        \    }\n}"
      python: "class Solution(object):\n    def findSubtreeSizes(self, parent, s):\n\
        \        \"\"\"\n        :type parent: List[int]\n        :type s: str\n   \
        \     :rtype: List[int]\n        \"\"\"\n        n = len(parent)\n        adj\
        \ = [[] for _ in range(n)]\n        for i in range(1, n):\n            adj[parent[i]].append(i)\n\
        \n        last_seen = [-1] * 26\n        prev_val = [-1] * n\n        new_parent\
        \ = [-1] * n\n\n        st = [0]\n        c0 = ord(s[0]) - ord('a')\n      \
        \  prev_val[0] = last_seen[c0]\n        last_seen[c0] = 0\n\n        edge_idx\
        \ = [0] * n\n\n        while st:\n            u = st[-1]\n            if edge_idx[u]\
        \ < len(adj[u]):\n                v = adj[u][edge_idx[u]]\n                edge_idx[u]\
        \ += 1\n                cv = ord(s[v]) - ord('a')\n                new_parent[v]\
        \ = last_seen[cv] if last_seen[cv] != -1 else parent[v]\n                prev_val[v]\
        \ = last_seen[cv]\n                last_seen[cv] = v\n                st.append(v)\n\
        \            else:\n                cu = ord(s[u]) - ord('a')\n            \
        \    last_seen[cu] = prev_val[u]\n                st.pop()\n\n        deg =\
        \ [0] * n\n        for i in range(1, n):\n            deg[new_parent[i]] +=\
        \ 1\n\n        ans = [1] * n\n        queue = [i for i in range(n) if deg[i]\
        \ == 0]\n        head = 0\n        while head < len(queue):\n            u =\
        \ queue[head]\n            head += 1\n            p = new_parent[u]\n      \
        \      if p != -1:\n                ans[p] += ans[u]\n                deg[p]\
        \ -= 1\n                if deg[p] == 0:\n                    queue.append(p)\n\
        \n        return ans"
      python3: "class Solution:\n    def findSubtreeSizes(self, parent: List[int], s:\
        \ str) -> List[int]:\n        n = len(parent)\n        adj = [[] for _ in range(n)]\n\
        \        for i in range(1, n):\n            adj[parent[i]].append(i)\n\n   \
        \     last_seen = [-1] * 26\n        prev_val = [-1] * n\n        new_parent\
        \ = [-1] * n\n\n        st = [0]\n        c0 = ord(s[0]) - ord('a')\n      \
        \  prev_val[0] = last_seen[c0]\n        last_seen[c0] = 0\n\n        edge_idx\
        \ = [0] * n\n\n        while st:\n            u = st[-1]\n            if edge_idx[u]\
        \ < len(adj[u]):\n                v = adj[u][edge_idx[u]]\n                edge_idx[u]\
        \ += 1\n                cv = ord(s[v]) - ord('a')\n                new_parent[v]\
        \ = last_seen[cv] if last_seen[cv] != -1 else parent[v]\n                prev_val[v]\
        \ = last_seen[cv]\n                last_seen[cv] = v\n                st.append(v)\n\
        \            else:\n                cu = ord(s[u]) - ord('a')\n            \
        \    last_seen[cu] = prev_val[u]\n                st.pop()\n\n        deg =\
        \ [0] * n\n        for i in range(1, n):\n            deg[new_parent[i]] +=\
        \ 1\n\n        ans = [1] * n\n        queue = [i for i in range(n) if deg[i]\
        \ == 0]\n        head = 0\n        while head < len(queue):\n            u =\
        \ queue[head]\n            head += 1\n            p = new_parent[u]\n      \
        \      if p != -1:\n                ans[p] += ans[u]\n                deg[p]\
        \ -= 1\n                if deg[p] == 0:\n                    queue.append(p)\n\
        \n        return ans"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* findSubtreeSizes(int* parent, int parentSize, char* s, int* returnSize)\
        \ {\n    int n = parentSize;\n    int* head = (int*)malloc(n * sizeof(int));\n\
        \    for (int i = 0; i < n; i++) head[i] = -1;\n    int* to = (int*)malloc(n\
        \ * sizeof(int));\n    int* next = (int*)malloc(n * sizeof(int));\n    for (int\
        \ i = 1; i < n; i++) {\n        to[i] = i;\n        next[i] = head[parent[i]];\n\
        \        head[parent[i]] = i;\n    }\n\n    int* curEdge = (int*)malloc(n *\
        \ sizeof(int));\n    for (int i = 0; i < n; i++) curEdge[i] = head[i];\n\n \
        \   int* st = (int*)malloc(n * sizeof(int));\n    int top = 0;\n    st[top++]\
        \ = 0;\n\n    int lastSeen[26];\n    for (int i = 0; i < 26; i++) lastSeen[i]\
        \ = -1;\n    int* prevVal = (int*)malloc(n * sizeof(int));\n    int c0 = s[0]\
        \ - 'a';\n    prevVal[0] = lastSeen[c0];\n    lastSeen[c0] = 0;\n\n    int*\
        \ newParent = (int*)malloc(n * sizeof(int));\n    newParent[0] = -1;\n\n   \
        \ while (top > 0) {\n        int u = st[top - 1];\n        if (curEdge[u] !=\
        \ -1) {\n            int e = curEdge[u];\n            curEdge[u] = next[e];\n\
        \            int v = to[e];\n            int cv = s[v] - 'a';\n            newParent[v]\
        \ = (lastSeen[cv] != -1) ? lastSeen[cv] : parent[v];\n            prevVal[v]\
        \ = lastSeen[cv];\n            lastSeen[cv] = v;\n            st[top++] = v;\n\
        \        } else {\n            int cu = s[u] - 'a';\n            lastSeen[cu]\
        \ = prevVal[u];\n            top--;\n        }\n    }\n\n    int* deg = (int*)calloc(n,\
        \ sizeof(int));\n    for (int i = 1; i < n; i++) {\n        deg[newParent[i]]++;\n\
        \    }\n\n    int* ans = (int*)malloc(n * sizeof(int));\n    for (int i = 0;\
        \ i < n; i++) ans[i] = 1;\n\n    int* q = (int*)malloc(n * sizeof(int));\n \
        \   int qHead = 0, qTail = 0;\n    for (int i = 0; i < n; i++) {\n        if\
        \ (deg[i] == 0) {\n            q[qTail++] = i;\n        }\n    }\n\n    while\
        \ (qHead < qTail) {\n        int u = q[qHead++];\n        int p = newParent[u];\n\
        \        if (p != -1) {\n            ans[p] += ans[u];\n            if (--deg[p]\
        \ == 0) {\n                q[qTail++] = p;\n            }\n        }\n    }\n\
        \n    free(head);\n    free(to);\n    free(next);\n    free(curEdge);\n    free(st);\n\
        \    free(prevVal);\n    free(newParent);\n    free(deg);\n    free(q);\n\n\
        \    *returnSize = n;\n    return ans;\n}"
      csharp: "public class Solution {\n    public int[] FindSubtreeSizes(int[] parent,\
        \ string s) {\n        int n = parent.Length;\n        List<int>[] adj = new\
        \ List<int>[n];\n        for (int i = 0; i < n; i++) {\n            adj[i] =\
        \ new List<int>();\n        }\n        for (int i = 1; i < n; i++) {\n     \
        \       adj[parent[i]].Add(i);\n        }\n\n        int[] lastSeen = new int[26];\n\
        \        Array.Fill(lastSeen, -1);\n        int[] prevVal = new int[n];\n  \
        \      int[] newParent = new int[n];\n        newParent[0] = -1;\n\n       \
        \ int[] st = new int[n];\n        int stTop = 0;\n        st[stTop] = 0;\n\n\
        \        int c0 = s[0] - 'a';\n        prevVal[0] = lastSeen[c0];\n        lastSeen[c0]\
        \ = 0;\n\n        int[] edgeIdx = new int[n];\n\n        while (stTop >= 0)\
        \ {\n            int u = st[stTop];\n            if (edgeIdx[u] < adj[u].Count)\
        \ {\n                int v = adj[u][edgeIdx[u]++];\n                int cv =\
        \ s[v] - 'a';\n                newParent[v] = lastSeen[cv] != -1 ? lastSeen[cv]\
        \ : parent[v];\n                prevVal[v] = lastSeen[cv];\n               \
        \ lastSeen[cv] = v;\n                stTop++;\n                st[stTop] = v;\n\
        \            } else {\n                int cu = s[u] - 'a';\n              \
        \  lastSeen[cu] = prevVal[u];\n                stTop--;\n            }\n   \
        \     }\n\n        int[] deg = new int[n];\n        for (int i = 1; i < n; i++)\
        \ {\n            deg[newParent[i]]++;\n        }\n\n        int[] ans = new\
        \ int[n];\n        Array.Fill(ans, 1);\n        int[] queue = new int[n];\n\
        \        int head = 0, tail = 0;\n        for (int i = 0; i < n; i++) {\n  \
        \          if (deg[i] == 0) {\n                queue[tail++] = i;\n        \
        \    }\n        }\n\n        while (head < tail) {\n            int u = queue[head++];\n\
        \            int p = newParent[u];\n            if (p != -1) {\n           \
        \     ans[p] += ans[u];\n                deg[p]--;\n                if (deg[p]\
        \ == 0) {\n                    queue[tail++] = p;\n                }\n     \
        \       }\n        }\n\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[]} parent\n * @param {string} s\n * @return\
        \ {number[]}\n */\nvar findSubtreeSizes = function(parent, s) {\n    const n\
        \ = parent.length;\n    const adj = Array.from({ length: n }, () => []);\n \
        \   for (let i = 1; i < n; i++) {\n        adj[parent[i]].push(i);\n    }\n\n\
        \    const lastSeen = new Int32Array(26).fill(-1);\n    const prevVal = new\
        \ Int32Array(n).fill(-1);\n    const newParent = new Int32Array(n).fill(-1);\n\
        \n    const st = new Int32Array(n);\n    let stTop = 0;\n    st[0] = 0;\n\n\
        \    const c0 = s.charCodeAt(0) - 97;\n    prevVal[0] = lastSeen[c0];\n    lastSeen[c0]\
        \ = 0;\n\n    const edgeIdx = new Int32Array(n);\n\n    while (stTop >= 0) {\n\
        \        const u = st[stTop];\n        if (edgeIdx[u] < adj[u].length) {\n \
        \           const v = adj[u][edgeIdx[u]++];\n            const cv = s.charCodeAt(v)\
        \ - 97;\n            newParent[v] = lastSeen[cv] !== -1 ? lastSeen[cv] : parent[v];\n\
        \            prevVal[v] = lastSeen[cv];\n            lastSeen[cv] = v;\n   \
        \         stTop++;\n            st[stTop] = v;\n        } else {\n         \
        \   const cu = s.charCodeAt(u) - 97;\n            lastSeen[cu] = prevVal[u];\n\
        \            stTop--;\n        }\n    }\n\n    const deg = new Int32Array(n);\n\
        \    for (let i = 1; i < n; i++) {\n        deg[newParent[i]]++;\n    }\n\n\
        \    const ans = new Int32Array(n).fill(1);\n    const queue = new Int32Array(n);\n\
        \    let head = 0, tail = 0;\n    for (let i = 0; i < n; i++) {\n        if\
        \ (deg[i] === 0) {\n            queue[tail++] = i;\n        }\n    }\n\n   \
        \ while (head < tail) {\n        const u = queue[head++];\n        const p =\
        \ newParent[u];\n        if (p !== -1) {\n            ans[p] += ans[u];\n  \
        \          deg[p]--;\n            if (deg[p] === 0) {\n                queue[tail++]\
        \ = p;\n            }\n        }\n    }\n\n    return Array.from(ans);\n};"
      typescript: "function findSubtreeSizes(parent: number[], s: string): number[]\
        \ {\n    const n = parent.length;\n    const adj: number[][] = Array.from({\
        \ length: n }, () => []);\n    for (let i = 1; i < n; i++) {\n        adj[parent[i]].push(i);\n\
        \    }\n\n    const lastSeen = new Int32Array(26).fill(-1);\n    const prevVal\
        \ = new Int32Array(n).fill(-1);\n    const newParent = new Int32Array(n).fill(-1);\n\
        \n    const st = new Int32Array(n);\n    let stTop = 0;\n    st[0] = 0;\n\n\
        \    const c0 = s.charCodeAt(0) - 97;\n    prevVal[0] = lastSeen[c0];\n    lastSeen[c0]\
        \ = 0;\n\n    const edgeIdx = new Int32Array(n);\n\n    while (stTop >= 0) {\n\
        \        const u = st[stTop];\n        if (edgeIdx[u] < adj[u].length) {\n \
        \           const v = adj[u][edgeIdx[u]++];\n            const cv = s.charCodeAt(v)\
        \ - 97;\n            newParent[v] = lastSeen[cv] !== -1 ? lastSeen[cv] : parent[v];\n\
        \            prevVal[v] = lastSeen[cv];\n            lastSeen[cv] = v;\n   \
        \         stTop++;\n            st[stTop] = v;\n        } else {\n         \
        \   const cu = s.charCodeAt(u) - 97;\n            lastSeen[cu] = prevVal[u];\n\
        \            stTop--;\n        }\n    }\n\n    const deg = new Int32Array(n);\n\
        \    for (let i = 1; i < n; i++) {\n        deg[newParent[i]]++;\n    }\n\n\
        \    const ans = new Int32Array(n).fill(1);\n    const queue = new Int32Array(n);\n\
        \    let head = 0, tail = 0;\n    for (let i = 0; i < n; i++) {\n        if\
        \ (deg[i] === 0) {\n            queue[tail++] = i;\n        }\n    }\n\n   \
        \ while (head < tail) {\n        const u = queue[head++];\n        const p =\
        \ newParent[u];\n        if (p !== -1) {\n            ans[p] += ans[u];\n  \
        \          deg[p]--;\n            if (deg[p] === 0) {\n                queue[tail++]\
        \ = p;\n            }\n        }\n    }\n\n    return Array.from(ans);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $parent\n     * @param\
        \ String $s\n     * @return Integer[]\n     */\n    function findSubtreeSizes($parent,\
        \ $s) {\n        $n = count($parent);\n        $adj = array_fill(0, $n, []);\n\
        \        for ($i = 1; $i < $n; $i++) {\n            $adj[$parent[$i]][] = $i;\n\
        \        }\n\n        $lastSeen = array_fill(0, 26, -1);\n        $prevVal =\
        \ array_fill(0, $n, -1);\n        $newParent = array_fill(0, $n, -1);\n\n  \
        \      $st = [0];\n        $c0 = ord($s[0]) - 97;\n        $prevVal[0] = $lastSeen[$c0];\n\
        \        $lastSeen[$c0] = 0;\n\n        $edgeIdx = array_fill(0, $n, 0);\n\n\
        \        while (!empty($st)) {\n            $u = end($st);\n            if ($edgeIdx[$u]\
        \ < count($adj[$u])) {\n                $v = $adj[$u][$edgeIdx[$u]];\n     \
        \           $edgeIdx[$u]++;\n                $cv = ord($s[$v]) - 97;\n     \
        \           $newParent[$v] = ($lastSeen[$cv] !== -1) ? $lastSeen[$cv] : $parent[$v];\n\
        \                $prevVal[$v] = $lastSeen[$cv];\n                $lastSeen[$cv]\
        \ = $v;\n                $st[] = $v;\n            } else {\n               \
        \ $cu = ord($s[$u]) - 97;\n                $lastSeen[$cu] = $prevVal[$u];\n\
        \                array_pop($st);\n            }\n        }\n\n        $deg =\
        \ array_fill(0, $n, 0);\n        for ($i = 1; $i < $n; $i++) {\n           \
        \ $deg[$newParent[$i]]++;\n        }\n\n        $ans = array_fill(0, $n, 1);\n\
        \        $queue = [];\n        for ($i = 0; $i < $n; $i++) {\n            if\
        \ ($deg[$i] === 0) {\n                $queue[] = $i;\n            }\n      \
        \  }\n\n        $head = 0;\n        $qLen = count($queue);\n        while ($head\
        \ < $qLen) {\n            $u = $queue[$head++];\n            $p = $newParent[$u];\n\
        \            if ($p !== -1) {\n                $ans[$p] += $ans[$u];\n     \
        \           $deg[$p]--;\n                if ($deg[$p] === 0) {\n           \
        \         $queue[] = $p;\n                    $qLen++;\n                }\n\
        \            }\n        }\n\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func findSubtreeSizes(_ parent: [Int], _ s: String)\
        \ -> [Int] {\n        let n = parent.count\n        var adj = [[Int]](repeating:\
        \ [Int](), count: n)\n        for i in 1..<n {\n            adj[parent[i]].append(i)\n\
        \        }\n\n        let sBytes = Array(s.utf8)\n        var lastSeen = [Int](repeating:\
        \ -1, count: 26)\n        var prevVal = [Int](repeating: -1, count: n)\n   \
        \     var newParent = [Int](repeating: -1, count: n)\n\n        var st = [Int]()\n\
        \        st.reserveCapacity(n)\n        st.append(0)\n\n        let c0 = Int(sBytes[0]\
        \ - 97)\n        prevVal[0] = lastSeen[c0]\n        lastSeen[c0] = 0\n\n   \
        \     var edgeIdx = [Int](repeating: 0, count: n)\n\n        while !st.isEmpty\
        \ {\n            let u = st.last!\n            if edgeIdx[u] < adj[u].count\
        \ {\n                let v = adj[u][edgeIdx[u]]\n                edgeIdx[u]\
        \ += 1\n                let cv = Int(sBytes[v] - 97)\n                newParent[v]\
        \ = lastSeen[cv] != -1 ? lastSeen[cv] : parent[v]\n                prevVal[v]\
        \ = lastSeen[cv]\n                lastSeen[cv] = v\n                st.append(v)\n\
        \            } else {\n                let cu = Int(sBytes[u] - 97)\n      \
        \          lastSeen[cu] = prevVal[u]\n                st.removeLast()\n    \
        \        }\n        }\n\n        var deg = [Int](repeating: 0, count: n)\n \
        \       for i in 1..<n {\n            deg[newParent[i]] += 1\n        }\n\n\
        \        var ans = [Int](repeating: 1, count: n)\n        var queue = [Int]()\n\
        \        queue.reserveCapacity(n)\n        for i in 0..<n {\n            if\
        \ deg[i] == 0 {\n                queue.append(i)\n            }\n        }\n\
        \n        var head = 0\n        while head < queue.count {\n            let\
        \ u = queue[head]\n            head += 1\n            let p = newParent[u]\n\
        \            if p != -1 {\n                ans[p] += ans[u]\n              \
        \  deg[p] -= 1\n                if deg[p] == 0 {\n                    queue.append(p)\n\
        \                }\n            }\n        }\n\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun findSubtreeSizes(parent: IntArray, s: String):\
        \ IntArray {\n        val n = parent.size\n        var head = IntArray(n) {\
        \ -1 }\n        val next = IntArray(n)\n        val to = IntArray(n)\n     \
        \   var edgeCount = 0\n\n        for (i in 1 until n) {\n            val p =\
        \ parent[i]\n            to[edgeCount] = i\n            next[edgeCount] = head[p]\n\
        \            head[p] = edgeCount++\n        }\n\n        val lastSeen = IntArray(26)\
        \ { -1 }\n        val prevVal = IntArray(n) { -1 }\n        val newParent =\
        \ IntArray(n) { -1 }\n        val edgeIdx = IntArray(n)\n        for (i in 0\
        \ until n) {\n            edgeIdx[i] = head[i]\n        }\n\n        val st\
        \ = IntArray(n)\n        var stSize = 0\n        st[stSize++] = 0\n        val\
        \ c0 = s[0] - 'a'\n        prevVal[0] = lastSeen[c0]\n        lastSeen[c0] =\
        \ 0\n\n        while (stSize > 0) {\n            val u = st[stSize - 1]\n  \
        \          val e = edgeIdx[u]\n            if (e != -1) {\n                val\
        \ v = to[e]\n                edgeIdx[u] = next[e]\n                val cv =\
        \ s[v] - 'a'\n                newParent[v] = if (lastSeen[cv] != -1) lastSeen[cv]\
        \ else parent[v]\n                prevVal[v] = lastSeen[cv]\n              \
        \  lastSeen[cv] = v\n                st[stSize++] = v\n            } else {\n\
        \                val cu = s[u] - 'a'\n                lastSeen[cu] = prevVal[u]\n\
        \                stSize--\n            }\n        }\n\n        val deg = IntArray(n)\n\
        \        for (i in 1 until n) {\n            deg[newParent[i]]++\n        }\n\
        \n        val ans = IntArray(n) { 1 }\n        val queue = IntArray(n)\n   \
        \     var qHead = 0\n        var qTail = 0\n        for (i in 0 until n) {\n\
        \            if (deg[i] == 0) {\n                queue[qTail++] = i\n      \
        \      }\n        }\n\n        while (qHead < qTail) {\n            val u =\
        \ queue[qHead++]\n            val p = newParent[u]\n            if (p != -1)\
        \ {\n                ans[p] += ans[u]\n                deg[p]--\n          \
        \      if (deg[p] == 0) {\n                    queue[qTail++] = p\n        \
        \        }\n            }\n        }\n\n        return ans\n    }\n}"
      dart: "class Solution {\n  List<int> findSubtreeSizes(List<int> parent, String\
        \ s) {\n    int n = parent.length;\n    List<List<int>> adj = List.generate(n,\
        \ (_) => <int>[]);\n    for (int i = 1; i < n; i++) {\n      adj[parent[i]].add(i);\n\
        \    }\n\n    List<int> lastSeen = List.filled(26, -1);\n    List<int> prevVal\
        \ = List.filled(n, -1);\n    List<int> newParent = List.filled(n, -1);\n   \
        \ List<int> edgeIdx = List.filled(n, 0);\n\n    List<int> st = [0];\n    int\
        \ c0 = s.codeUnitAt(0) - 97;\n    prevVal[0] = lastSeen[c0];\n    lastSeen[c0]\
        \ = 0;\n\n    while (st.isNotEmpty) {\n      int u = st.last;\n      if (edgeIdx[u]\
        \ < adj[u].length) {\n        int v = adj[u][edgeIdx[u]];\n        edgeIdx[u]++;\n\
        \        int cv = s.codeUnitAt(v) - 97;\n        newParent[v] = lastSeen[cv]\
        \ != -1 ? lastSeen[cv] : parent[v];\n        prevVal[v] = lastSeen[cv];\n  \
        \      lastSeen[cv] = v;\n        st.add(v);\n      } else {\n        int cu\
        \ = s.codeUnitAt(u) - 97;\n        lastSeen[cu] = prevVal[u];\n        st.removeLast();\n\
        \      }\n    }\n\n    List<int> deg = List.filled(n, 0);\n    for (int i =\
        \ 1; i < n; i++) {\n      deg[newParent[i]]++;\n    }\n\n    List<int> ans =\
        \ List.filled(n, 1);\n    List<int> queue = [];\n    for (int i = 0; i < n;\
        \ i++) {\n      if (deg[i] == 0) {\n        queue.add(i);\n      }\n    }\n\n\
        \    int head = 0;\n    while (head < queue.length) {\n      int u = queue[head++];\n\
        \      int p = newParent[u];\n      if (p != -1) {\n        ans[p] += ans[u];\n\
        \        deg[p]--;\n        if (deg[p] == 0) {\n          queue.add(p);\n  \
        \      }\n      }\n    }\n\n    return ans;\n  }\n}"
      go: "func findSubtreeSizes(parent []int, s string) []int {\n    n := len(parent)\n\
        \    adj := make([][]int, n)\n    for i := 1; i < n; i++ {\n        adj[parent[i]]\
        \ = append(adj[parent[i]], i)\n    }\n\n    lastSeen := make([]int, 26)\n  \
        \  for i := range lastSeen {\n        lastSeen[i] = -1\n    }\n    prevVal :=\
        \ make([]int, n)\n    newParent := make([]int, n)\n    for i := range newParent\
        \ {\n        newParent[i] = -1\n    }\n    edgeIdx := make([]int, n)\n\n   \
        \ st := []int{0}\n    c0 := int(s[0] - 'a')\n    prevVal[0] = lastSeen[c0]\n\
        \    lastSeen[c0] = 0\n\n    for len(st) > 0 {\n        u := st[len(st)-1]\n\
        \        if edgeIdx[u] < len(adj[u]) {\n            v := adj[u][edgeIdx[u]]\n\
        \            edgeIdx[u]++\n            cv := int(s[v] - 'a')\n            if\
        \ lastSeen[cv] != -1 {\n                newParent[v] = lastSeen[cv]\n      \
        \      } else {\n                newParent[v] = parent[v]\n            }\n \
        \           prevVal[v] = lastSeen[cv]\n            lastSeen[cv] = v\n      \
        \      st = append(st, v)\n        } else {\n            cu := int(s[u] - 'a')\n\
        \            lastSeen[cu] = prevVal[u]\n            st = st[:len(st)-1]\n  \
        \      }\n    }\n\n    deg := make([]int, n)\n    for i := 1; i < n; i++ {\n\
        \        deg[newParent[i]]++\n    }\n\n    ans := make([]int, n)\n    for i\
        \ := 0; i < n; i++ {\n        ans[i] = 1\n    }\n\n    queue := make([]int,\
        \ 0, n)\n    for i := 0; i < n; i++ {\n        if deg[i] == 0 {\n          \
        \  queue = append(queue, i)\n        }\n    }\n\n    head := 0\n    for head\
        \ < len(queue) {\n        u := queue[head]\n        head++\n        p := newParent[u]\n\
        \        if p != -1 {\n            ans[p] += ans[u]\n            deg[p]--\n\
        \            if deg[p] == 0 {\n                queue = append(queue, p)\n  \
        \          }\n        }\n    }\n\n    return ans\n}"
      ruby: "# @param {Integer[]} parent\n# @param {String} s\n# @return {Integer[]}\n\
        def find_subtree_sizes(parent, s)\n    n = parent.length\n    adj = Array.new(n)\
        \ { [] }\n    (1...n).each do |i|\n        adj[parent[i]] << i\n    end\n\n\
        \    last_seen = Array.new(26, -1)\n    prev_val = Array.new(n, -1)\n    new_parent\
        \ = Array.new(n, -1)\n    edge_idx = Array.new(n, 0)\n\n    st = [0]\n    c0\
        \ = s.getbyte(0) - 97\n    prev_val[0] = last_seen[c0]\n    last_seen[c0] =\
        \ 0\n\n    while !st.empty?\n        u = st.last\n        if edge_idx[u] < adj[u].length\n\
        \            v = adj[u][edge_idx[u]]\n            edge_idx[u] += 1\n       \
        \     cv = s.getbyte(v) - 97\n            new_parent[v] = last_seen[cv] != -1\
        \ ? last_seen[cv] : parent[v]\n            prev_val[v] = last_seen[cv]\n   \
        \         last_seen[cv] = v\n            st << v\n        else\n           \
        \ cu = s.getbyte(u) - 97\n            last_seen[cu] = prev_val[u]\n        \
        \    st.pop\n        end\n    end\n\n    deg = Array.new(n, 0)\n    (1...n).each\
        \ do |i|\n        deg[new_parent[i]] += 1\n    end\n\n    ans = Array.new(n,\
        \ 1)\n    queue = []\n    (0...n).each do |i|\n        queue << i if deg[i]\
        \ == 0\n    end\n\n    head = 0\n    while head < queue.length\n        u =\
        \ queue[head]\n        head += 1\n        p = new_parent[u]\n        if p !=\
        \ -1\n            ans[p] += ans[u]\n            deg[p] -= 1\n            queue\
        \ << p if deg[p] == 0\n        end\n    end\n\n    ans\nend"
      scala: "object Solution {\n    def findSubtreeSizes(parent: Array[Int], s: String):\
        \ Array[Int] = {\n        val n = parent.length\n        val head = Array.fill(n)(-1)\n\
        \        val next = new Array[Int](n)\n        val to = new Array[Int](n)\n\
        \        var edgeCount = 0\n\n        var i = 1\n        while (i < n) {\n \
        \           val p = parent(i)\n            to(edgeCount) = i\n            next(edgeCount)\
        \ = head(p)\n            head(p) = edgeCount\n            edgeCount += 1\n \
        \           i += 1\n        }\n\n        val lastSeen = Array.fill(26)(-1)\n\
        \        val prevVal = Array.fill(n)(-1)\n        val newParent = Array.fill(n)(-1)\n\
        \        val edgeIdx = Array.tabulate(n)(head)\n\n        val st = new Array[Int](n)\n\
        \        var stSize = 0\n        st(stSize) = 0\n        stSize += 1\n     \
        \   val c0 = s.charAt(0) - 'a'\n        prevVal(0) = lastSeen(c0)\n        lastSeen(c0)\
        \ = 0\n\n        while (stSize > 0) {\n            val u = st(stSize - 1)\n\
        \            val e = edgeIdx(u)\n            if (e != -1) {\n              \
        \  val v = to(e)\n                edgeIdx(u) = next(e)\n                val\
        \ cv = s.charAt(v) - 'a'\n                newParent(v) = if (lastSeen(cv) !=\
        \ -1) lastSeen(cv) else parent(v)\n                prevVal(v) = lastSeen(cv)\n\
        \                lastSeen(cv) = v\n                st(stSize) = v\n        \
        \        stSize += 1\n            } else {\n                val cu = s.charAt(u)\
        \ - 'a'\n                lastSeen(cu) = prevVal(u)\n                stSize -=\
        \ 1\n            }\n        }\n\n        val deg = new Array[Int](n)\n     \
        \   i = 1\n        while (i < n) {\n            deg(newParent(i)) += 1\n   \
        \         i += 1\n        }\n\n        val ans = Array.fill(n)(1)\n        val\
        \ queue = new Array[Int](n)\n        var qHead = 0\n        var qTail = 0\n\
        \        i = 0\n        while (i < n) {\n            if (deg(i) == 0) {\n  \
        \              queue(qTail) = i\n                qTail += 1\n            }\n\
        \            i += 1\n        }\n\n        while (qHead < qTail) {\n        \
        \    val u = queue(qHead)\n            qHead += 1\n            val p = newParent(u)\n\
        \            if (p != -1) {\n                ans(p) += ans(u)\n            \
        \    deg(p) -= 1\n                if (deg(p) == 0) {\n                    queue(qTail)\
        \ = p\n                    qTail += 1\n                }\n            }\n  \
        \      }\n\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn find_subtree_sizes(parent: Vec<i32>, s: String)\
        \ -> Vec<i32> {\n        let n = parent.len();\n        let s_bytes = s.as_bytes();\n\
        \        let mut adj = vec![Vec::new(); n];\n        for i in 1..n {\n     \
        \       adj[parent[i] as usize].push(i);\n        }\n\n        let mut last_seen\
        \ = [-1i32; 26];\n        let mut new_parent = vec![-1i32; n];\n        let\
        \ mut post_order = Vec::with_capacity(n);\n\n        let c0 = (s_bytes[0] -\
        \ b'a') as usize;\n        let old0 = last_seen[c0];\n        last_seen[c0]\
        \ = 0;\n        let mut st = vec![(0usize, 0usize, old0)];\n\n        while\
        \ let Some((u, edge_idx, old_val)) = st.pop() {\n            if edge_idx < adj[u].len()\
        \ {\n                let v = adj[u][edge_idx];\n                st.push((u,\
        \ edge_idx + 1, old_val));\n\n                let cv = (s_bytes[v] - b'a') as\
        \ usize;\n                new_parent[v] = if last_seen[cv] != -1 {\n       \
        \             last_seen[cv]\n                } else {\n                    parent[v]\n\
        \                };\n                let old_v = last_seen[cv];\n          \
        \      last_seen[cv] = v as i32;\n                st.push((v, 0, old_v));\n\
        \            } else {\n                let cu = (s_bytes[u] - b'a') as usize;\n\
        \                last_seen[cu] = old_val;\n                post_order.push(u);\n\
        \            }\n        }\n\n        let mut ans = vec![1i32; n];\n        for\
        \ &u in &post_order {\n            let p = new_parent[u];\n            if p\
        \ != -1 {\n                ans[p as usize] += ans[u];\n            }\n     \
        \   }\n\n        ans\n    }\n}"
      racket: "(define/contract (find-subtree-sizes parent s)\n  (-> (listof exact-integer?)\
        \ string? (listof exact-integer?))\n  (let* ([n (length parent)]\n         [p-vec\
        \ (list->vector parent)]\n         [s-bytes (string->bytes/utf-8 s)]\n     \
        \    [adj (make-vector n '())])\n    (for ([i (in-range 1 n)])\n      (let ([p\
        \ (vector-ref p-vec i)])\n        (vector-set! adj p (cons i (vector-ref adj\
        \ p)))))\n    (define last-seen (make-vector 26 -1))\n    (define new-parent\
        \ (make-vector n -1))\n    (define c0 (- (bytes-ref s-bytes 0) 97))\n    (define\
        \ old0 (vector-ref last-seen c0))\n    (vector-set! last-seen c0 0)\n    (define\
        \ st (list (list 0 (vector-ref adj 0) old0)))\n    (define post-order '())\n\
        \    (let loop ([stack st])\n      (when (pair? stack)\n        (let* ([top\
        \ (car stack)]\n               [u (car top)]\n               [children (cadr\
        \ top)]\n               [old-val (caddr top)]\n               [rest-stack (cdr\
        \ stack)])\n          (if (pair? children)\n              (let* ([v (car children)]\n\
        \                     [new-top (list u (cdr children) old-val)]\n          \
        \           [cv (- (bytes-ref s-bytes v) 97)]\n                     [ls (vector-ref\
        \ last-seen cv)]\n                     [np (if (= ls -1) (vector-ref p-vec v)\
        \ ls)]\n                     [old-v ls])\n                (vector-set! new-parent\
        \ v np)\n                (vector-set! last-seen cv v)\n                (loop\
        \ (cons (list v (vector-ref adj v) old-v) (cons new-top rest-stack))))\n   \
        \           (let ([cu (- (bytes-ref s-bytes u) 97)])\n                (vector-set!\
        \ last-seen cu old-val)\n                (set! post-order (cons u post-order))\n\
        \                (loop rest-stack))))))\n    (define ans (make-vector n 1))\n\
        \    (for ([u (in-list (reverse post-order))])\n      (let ([p (vector-ref new-parent\
        \ u)])\n        (when (not (= p -1))\n          (vector-set! ans p (+ (vector-ref\
        \ ans p) (vector-ref ans u))))))\n    (vector->list ans)))"
      erlang: "-spec find_subtree_sizes(Parent :: [integer()], S :: unicode:unicode_binary())\
        \ -> [integer()].\nfind_subtree_sizes(Parent, S) ->\n    N = length(Parent),\n\
        \    PArr = array:from_list(Parent),\n    Adj0 = array:new(N, {default, []}),\n\
        \    Adj = lists:foldl(fun({I, P}, Acc) ->\n        if\n            P >= 0 ->\
        \ array:set(P, [I | array:get(P, Acc)], Acc);\n            true -> Acc\n   \
        \     end\n    end, Adj0, lists:zip(lists:seq(0, N - 1), Parent)),\n\n    C0\
        \ = binary:at(S, 0) - $a,\n    LastSeen0 = erlang:make_tuple(26, -1),\n    Old0\
        \ = element(C0 + 1, LastSeen0),\n    LastSeen1 = setelement(C0 + 1, LastSeen0,\
        \ 0),\n    NewParent0 = array:new(N, {default, -1}),\n\n    Stack0 = [{0, array:get(0,\
        \ Adj), Old0}],\n\n    {NewParent, PostOrder} = dfs(Stack0, LastSeen1, NewParent0,\
        \ [], S, Adj, PArr),\n\n    Ans0 = array:new(N, {default, 1}),\n    Ans = lists:foldl(fun(U,\
        \ AccAns) ->\n        P = array:get(U, NewParent),\n        if\n           \
        \ P >= 0 ->\n                Val = array:get(P, AccAns) + array:get(U, AccAns),\n\
        \                array:set(P, Val, AccAns);\n            true ->\n         \
        \       AccAns\n        end\n    end, Ans0, lists:reverse(PostOrder)),\n\n \
        \   array:to_list(Ans).\n\ndfs([], _LastSeen, NewParent, PostOrder, _S, _Adj,\
        \ _PArr) ->\n    {NewParent, PostOrder};\ndfs([{U, [V | RestChildren], OldVal}\
        \ | RestStack], LastSeen, NewParent, PostOrder, S, Adj, PArr) ->\n    CV = binary:at(S,\
        \ V) - $a,\n    LS = element(CV + 1, LastSeen),\n    NP = if LS =:= -1 -> array:get(V,\
        \ PArr); true -> LS end,\n    NewParent1 = array:set(V, NP, NewParent),\n  \
        \  OldV = LS,\n    LastSeen1 = setelement(CV + 1, LastSeen, V),\n    NewTop\
        \ = {U, RestChildren, OldVal},\n    dfs([{V, array:get(V, Adj), OldV}, NewTop\
        \ | RestStack], LastSeen1, NewParent1, PostOrder, S, Adj, PArr);\ndfs([{U, [],\
        \ OldVal} | RestStack], LastSeen, NewParent, PostOrder, S, Adj, PArr) ->\n \
        \   CU = binary:at(S, U) - $a,\n    LastSeen1 = setelement(CU + 1, LastSeen,\
        \ OldVal),\n    dfs(RestStack, LastSeen1, NewParent, [U | PostOrder], S, Adj,\
        \ PArr)."
      elixir: "defmodule Solution do\n  @spec find_subtree_sizes(parent :: [integer],\
        \ s :: String.t) :: [integer]\n  def find_subtree_sizes(parent, s) do\n    n\
        \ = length(parent)\n    p_arr = :array.from_list(parent)\n\n    adj0 = :array.new(n,\
        \ default: [])\n    adj =\n      parent\n      |> Enum.with_index()\n      |>\
        \ Enum.reduce(adj0, fn {p, i}, acc ->\n        if p >= 0 do\n          :array.set(p,\
        \ [i | :array.get(p, acc)], acc)\n        else\n          acc\n        end\n\
        \      end)\n\n    c0 = :binary.at(s, 0) - ?a\n    last_seen0 = :erlang.make_tuple(26,\
        \ -1)\n    old0 = elem(last_seen0, c0)\n    last_seen1 = put_elem(last_seen0,\
        \ c0, 0)\n    new_parent0 = :array.new(n, default: -1)\n\n    stack0 = [{0,\
        \ :array.get(0, adj), old0}]\n\n    {new_parent, post_order} = dfs(stack0, last_seen1,\
        \ new_parent0, [], s, adj, p_arr)\n\n    ans0 = :array.new(n, default: 1)\n\n\
        \    ans =\n      post_order\n      |> Enum.reverse()\n      |> Enum.reduce(ans0,\
        \ fn u, acc ->\n        p = :array.get(u, new_parent)\n        if p >= 0 do\n\
        \          val = :array.get(p, acc) + :array.get(u, acc)\n          :array.set(p,\
        \ val, acc)\n        else\n          acc\n        end\n      end)\n\n    :array.to_list(ans)\n\
        \  end\n\n  defp dfs([], _last_seen, new_parent, post_order, _s, _adj, _p_arr)\
        \ do\n    {new_parent, post_order}\n  end\n\n  defp dfs([{u, [v | rest_children],\
        \ old_val} | rest_stack], last_seen, new_parent, post_order, s, adj, p_arr)\
        \ do\n    cv = :binary.at(s, v) - ?a\n    ls = elem(last_seen, cv)\n    np =\
        \ if ls == -1, do: :array.get(v, p_arr), else: ls\n    new_parent1 = :array.set(v,\
        \ np, new_parent)\n    old_v = ls\n    last_seen1 = put_elem(last_seen, cv,\
        \ v)\n    new_top = {u, rest_children, old_val}\n    dfs([{v, :array.get(v,\
        \ adj), old_v}, new_top | rest_stack], last_seen1, new_parent1, post_order,\
        \ s, adj, p_arr)\n  end\n\n  defp dfs([{u, [], old_val} | rest_stack], last_seen,\
        \ new_parent, post_order, s, adj, p_arr) do\n    cu = :binary.at(s, u) - ?a\n\
        \    last_seen1 = put_elem(last_seen, cu, old_val)\n    dfs(rest_stack, last_seen1,\
        \ new_parent, [u | post_order], s, adj, p_arr)\n  end\nend"
    approach: 'To solve this problem, we first determine the new parent for each node
      by traversing the original tree using depth-first search (DFS). As we traverse
      from the root to each node, we maintain an array tracking the most recent ancestor
      visited for each of the 26 lowercase English letters. When visiting a node x,
      we look up the character assigned to x; if an ancestor with the same character
      exists, that ancestor becomes the new parent of x, otherwise the parent remains
      unchanged. We then update the most recent ancestor for that character to x, explore
      all children of x, and revert the character state upon backtracking.


      Once the new parent pointers are established, the modified tree remains a valid
      directed acyclic graph rooted at node 0 because every node''s new parent is an
      ancestor in the original tree. We can compute the subtree size for each node bottom-up
      without recursion using Kahn''s algorithm. We calculate the in-degree (number
      of children) for each node in the new tree and initialize each node''s subtree
      size to 1. Starting with all leaf nodes (nodes with 0 children) in a queue, we
      repeatedly remove a node, add its subtree size to its new parent, and push the
      parent to the queue once all of its children have been processed.'
    time_complexity: O(n) where n is the number of nodes. Building the adjacency list,
      performing the DFS traversal with constant-time ancestor updates for 26 characters,
      and aggregating subtree sizes bottom-up with Kahn's algorithm all operate in linear
      time.
    space_complexity: O(n) to store the adjacency lists, new parent array, tracking
      state, queue, and output answers.
    elapsed_time: 1536.4997718334198
    model: gemini-3.8-flash
    generated_at: '2026-11-21 05:25:46 '
---

## Problem #3331: Find Subtree Sizes After Changes

**Difficulty:** Medium

**Topics:** Array, Hash Table, String, Tree, Depth-First Search

## Problem Description

<p>You are given a tree rooted at node 0 that consists of <code>n</code> nodes numbered from <code>0</code> to <code>n - 1</code>. The tree is represented by an array <code>parent</code> of size <code>n</code>, where <code>parent[i]</code> is the parent of node <code>i</code>. Since node 0 is the root, <code>parent[0] == -1</code>.</p>

<p>You are also given a string <code>s</code> of length <code>n</code>, where <code>s[i]</code> is the character assigned to node <code>i</code>.</p>

<p>We make the following changes on the tree <strong>one</strong> time <strong>simultaneously</strong> for all nodes <code>x</code> from <code>1</code> to <code>n - 1</code>:</p>

<ul>
	<li>Find the <strong>closest</strong> node <code>y</code> to node <code>x</code> such that <code>y</code> is an ancestor of <code>x</code>, and <code>s[x] == s[y]</code>.</li>
	<li>If node <code>y</code> does not exist, do nothing.</li>
	<li>Otherwise, <strong>remove</strong> the edge between <code>x</code> and its current parent and make node <code>y</code> the new parent of <code>x</code> by adding an edge between them.</li>
</ul>

<p>Return an array <code>answer</code> of size <code>n</code> where <code>answer[i]</code> is the <strong>size</strong> of the <span data-keyword="subtree">subtree</span> rooted at node <code>i</code> in the <strong>final</strong> tree.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">parent = [-1,0,0,1,1,1], s = &quot;abaabc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[6,3,1,1,1,1]</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/08/15/graphex1drawio.png" style="width: 230px; height: 277px;" />
<p>The parent of node 3 will change from node 1 to node 0.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">parent = [-1,0,4,0,1], s = &quot;abbba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[5,2,1,1,1]</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/08/20/exgraph2drawio.png" style="width: 160px; height: 308px;" />
<p>The following changes will happen at the same time:</p>

<ul>
	<li>The parent of node 4 will change from node 1 to node 0.</li>
	<li>The parent of node 2 will change from node 4 to node 1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == parent.length == s.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= parent[i] &lt;= n - 1</code> for all <code>i &gt;= 1</code>.</li>
	<li><code>parent[0] == -1</code></li>
	<li><code>parent</code> represents a valid tree.</li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>


## Hints

1. Perform a depth-first search on the tree, starting from the root.

2. During the DFS, keep track of the most recent node where each character from 'a' to 'z' has been seen.

## ✨ AI-Generated Solution (gemini-3.8-flash)

### Approach

To solve this problem, we first determine the new parent for each node by traversing the original tree using depth-first search (DFS). As we traverse from the root to each node, we maintain an array tracking the most recent ancestor visited for each of the 26 lowercase English letters. When visiting a node x, we look up the character assigned to x; if an ancestor with the same character exists, that ancestor becomes the new parent of x, otherwise the parent remains unchanged. We then update the most recent ancestor for that character to x, explore all children of x, and revert the character state upon backtracking.

Once the new parent pointers are established, the modified tree remains a valid directed acyclic graph rooted at node 0 because every node's new parent is an ancestor in the original tree. We can compute the subtree size for each node bottom-up without recursion using Kahn's algorithm. We calculate the in-degree (number of children) for each node in the new tree and initialize each node's subtree size to 1. Starting with all leaf nodes (nodes with 0 children) in a queue, we repeatedly remove a node, add its subtree size to its new parent, and push the parent to the queue once all of its children have been processed.

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
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> adj(n);
        for (int i = 1; i < n; ++i) {
            adj[parent[i]].push_back(i);
        }

        vector<int> last_seen(26, -1);
        vector<int> prev_val(n, -1);
        vector<int> new_parent(n, -1);

        vector<int> st;
        st.push_back(0);
        int c0 = s[0] - 'a';
        prev_val[0] = last_seen[c0];
        last_seen[c0] = 0;

        vector<int> edge_idx(n, 0);

        while (!st.empty()) {
            int u = st.back();
            if (edge_idx[u] < adj[u].size()) {
                int v = adj[u][edge_idx[u]++];
                int cv = s[v] - 'a';
                new_parent[v] = (last_seen[cv] != -1) ? last_seen[cv] : parent[v];
                prev_val[v] = last_seen[cv];
                last_seen[cv] = v;
                st.push_back(v);
            } else {
                int cu = s[u] - 'a';
                last_seen[cu] = prev_val[u];
                st.pop_back();
            }
        }

        vector<int> deg(n, 0);
        for (int i = 1; i < n; ++i) {
            deg[new_parent[i]]++;
        }

        vector<int> ans(n, 1);
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (deg[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            int p = new_parent[u];
            if (p != -1) {
                ans[p] += ans[u];
                if (--deg[p] == 0) {
                    q.push(p);
                }
            }
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
class Solution {
    public int[] findSubtreeSizes(int[] parent, String s) {
        int n = parent.length;
        int[] head = new int[n];
        Arrays.fill(head, -1);
        int[] to = new int[n];
        int[] next = new int[n];
        for (int i = 1; i < n; i++) {
            to[i] = i;
            next[i] = head[parent[i]];
            head[parent[i]] = i;
        }

        int[] curEdge = new int[n];
        System.arraycopy(head, 0, curEdge, 0, n);

        int[] st = new int[n];
        int top = 0;
        st[top++] = 0;

        int[] lastSeen = new int[26];
        Arrays.fill(lastSeen, -1);
        int[] prevVal = new int[n];
        int c0 = s.charAt(0) - 'a';
        prevVal[0] = lastSeen[c0];
        lastSeen[c0] = 0;

        int[] newParent = new int[n];
        newParent[0] = -1;

        while (top > 0) {
            int u = st[top - 1];
            if (curEdge[u] != -1) {
                int e = curEdge[u];
                curEdge[u] = next[e];
                int v = to[e];
                int cv = s.charAt(v) - 'a';
                newParent[v] = (lastSeen[cv] != -1) ? lastSeen[cv] : parent[v];
                prevVal[v] = lastSeen[cv];
                lastSeen[cv] = v;
                st[top++] = v;
            } else {
                int cu = s.charAt(u) - 'a';
                lastSeen[cu] = prevVal[u];
                top--;
            }
        }

        int[] deg = new int[n];
        for (int i = 1; i < n; i++) {
            deg[newParent[i]]++;
        }

        int[] ans = new int[n];
        Arrays.fill(ans, 1);

        int[] q = new int[n];
        int qHead = 0, qTail = 0;
        for (int i = 0; i < n; i++) {
            if (deg[i] == 0) {
                q[qTail++] = i;
            }
        }

        while (qHead < qTail) {
            int u = q[qHead++];
            int p = newParent[u];
            if (p != -1) {
                ans[p] += ans[u];
                deg[p]--;
                if (deg[p] == 0) {
                    q[qTail++] = p;
                }
            }
        }

        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        last_seen = [-1] * 26
        prev_val = [-1] * n
        new_parent = [-1] * n

        st = [0]
        c0 = ord(s[0]) - ord('a')
        prev_val[0] = last_seen[c0]
        last_seen[c0] = 0

        edge_idx = [0] * n

        while st:
            u = st[-1]
            if edge_idx[u] < len(adj[u]):
                v = adj[u][edge_idx[u]]
                edge_idx[u] += 1
                cv = ord(s[v]) - ord('a')
                new_parent[v] = last_seen[cv] if last_seen[cv] != -1 else parent[v]
                prev_val[v] = last_seen[cv]
                last_seen[cv] = v
                st.append(v)
            else:
                cu = ord(s[u]) - ord('a')
                last_seen[cu] = prev_val[u]
                st.pop()

        deg = [0] * n
        for i in range(1, n):
            deg[new_parent[i]] += 1

        ans = [1] * n
        queue = [i for i in range(n) if deg[i] == 0]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            p = new_parent[u]
            if p != -1:
                ans[p] += ans[u]
                deg[p] -= 1
                if deg[p] == 0:
                    queue.append(p)

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        last_seen = [-1] * 26
        prev_val = [-1] * n
        new_parent = [-1] * n

        st = [0]
        c0 = ord(s[0]) - ord('a')
        prev_val[0] = last_seen[c0]
        last_seen[c0] = 0

        edge_idx = [0] * n

        while st:
            u = st[-1]
            if edge_idx[u] < len(adj[u]):
                v = adj[u][edge_idx[u]]
                edge_idx[u] += 1
                cv = ord(s[v]) - ord('a')
                new_parent[v] = last_seen[cv] if last_seen[cv] != -1 else parent[v]
                prev_val[v] = last_seen[cv]
                last_seen[cv] = v
                st.append(v)
            else:
                cu = ord(s[u]) - ord('a')
                last_seen[cu] = prev_val[u]
                st.pop()

        deg = [0] * n
        for i in range(1, n):
            deg[new_parent[i]] += 1

        ans = [1] * n
        queue = [i for i in range(n) if deg[i] == 0]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            p = new_parent[u]
            if p != -1:
                ans[p] += ans[u]
                deg[p] -= 1
                if deg[p] == 0:
                    queue.append(p)

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findSubtreeSizes(int* parent, int parentSize, char* s, int* returnSize) {
    int n = parentSize;
    int* head = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) head[i] = -1;
    int* to = (int*)malloc(n * sizeof(int));
    int* next = (int*)malloc(n * sizeof(int));
    for (int i = 1; i < n; i++) {
        to[i] = i;
        next[i] = head[parent[i]];
        head[parent[i]] = i;
    }

    int* curEdge = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) curEdge[i] = head[i];

    int* st = (int*)malloc(n * sizeof(int));
    int top = 0;
    st[top++] = 0;

    int lastSeen[26];
    for (int i = 0; i < 26; i++) lastSeen[i] = -1;
    int* prevVal = (int*)malloc(n * sizeof(int));
    int c0 = s[0] - 'a';
    prevVal[0] = lastSeen[c0];
    lastSeen[c0] = 0;

    int* newParent = (int*)malloc(n * sizeof(int));
    newParent[0] = -1;

    while (top > 0) {
        int u = st[top - 1];
        if (curEdge[u] != -1) {
            int e = curEdge[u];
            curEdge[u] = next[e];
            int v = to[e];
            int cv = s[v] - 'a';
            newParent[v] = (lastSeen[cv] != -1) ? lastSeen[cv] : parent[v];
            prevVal[v] = lastSeen[cv];
            lastSeen[cv] = v;
            st[top++] = v;
        } else {
            int cu = s[u] - 'a';
            lastSeen[cu] = prevVal[u];
            top--;
        }
    }

    int* deg = (int*)calloc(n, sizeof(int));
    for (int i = 1; i < n; i++) {
        deg[newParent[i]]++;
    }

    int* ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = 1;

    int* q = (int*)malloc(n * sizeof(int));
    int qHead = 0, qTail = 0;
    for (int i = 0; i < n; i++) {
        if (deg[i] == 0) {
            q[qTail++] = i;
        }
    }

    while (qHead < qTail) {
        int u = q[qHead++];
        int p = newParent[u];
        if (p != -1) {
            ans[p] += ans[u];
            if (--deg[p] == 0) {
                q[qTail++] = p;
            }
        }
    }

    free(head);
    free(to);
    free(next);
    free(curEdge);
    free(st);
    free(prevVal);
    free(newParent);
    free(deg);
    free(q);

    *returnSize = n;
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] FindSubtreeSizes(int[] parent, string s) {
        int n = parent.Length;
        List<int>[] adj = new List<int>[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new List<int>();
        }
        for (int i = 1; i < n; i++) {
            adj[parent[i]].Add(i);
        }

        int[] lastSeen = new int[26];
        Array.Fill(lastSeen, -1);
        int[] prevVal = new int[n];
        int[] newParent = new int[n];
        newParent[0] = -1;

        int[] st = new int[n];
        int stTop = 0;
        st[stTop] = 0;

        int c0 = s[0] - 'a';
        prevVal[0] = lastSeen[c0];
        lastSeen[c0] = 0;

        int[] edgeIdx = new int[n];

        while (stTop >= 0) {
            int u = st[stTop];
            if (edgeIdx[u] < adj[u].Count) {
                int v = adj[u][edgeIdx[u]++];
                int cv = s[v] - 'a';
                newParent[v] = lastSeen[cv] != -1 ? lastSeen[cv] : parent[v];
                prevVal[v] = lastSeen[cv];
                lastSeen[cv] = v;
                stTop++;
                st[stTop] = v;
            } else {
                int cu = s[u] - 'a';
                lastSeen[cu] = prevVal[u];
                stTop--;
            }
        }

        int[] deg = new int[n];
        for (int i = 1; i < n; i++) {
            deg[newParent[i]]++;
        }

        int[] ans = new int[n];
        Array.Fill(ans, 1);
        int[] queue = new int[n];
        int head = 0, tail = 0;
        for (int i = 0; i < n; i++) {
            if (deg[i] == 0) {
                queue[tail++] = i;
            }
        }

        while (head < tail) {
            int u = queue[head++];
            int p = newParent[u];
            if (p != -1) {
                ans[p] += ans[u];
                deg[p]--;
                if (deg[p] == 0) {
                    queue[tail++] = p;
                }
            }
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
 * @param {number[]} parent
 * @param {string} s
 * @return {number[]}
 */
var findSubtreeSizes = function(parent, s) {
    const n = parent.length;
    const adj = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        adj[parent[i]].push(i);
    }

    const lastSeen = new Int32Array(26).fill(-1);
    const prevVal = new Int32Array(n).fill(-1);
    const newParent = new Int32Array(n).fill(-1);

    const st = new Int32Array(n);
    let stTop = 0;
    st[0] = 0;

    const c0 = s.charCodeAt(0) - 97;
    prevVal[0] = lastSeen[c0];
    lastSeen[c0] = 0;

    const edgeIdx = new Int32Array(n);

    while (stTop >= 0) {
        const u = st[stTop];
        if (edgeIdx[u] < adj[u].length) {
            const v = adj[u][edgeIdx[u]++];
            const cv = s.charCodeAt(v) - 97;
            newParent[v] = lastSeen[cv] !== -1 ? lastSeen[cv] : parent[v];
            prevVal[v] = lastSeen[cv];
            lastSeen[cv] = v;
            stTop++;
            st[stTop] = v;
        } else {
            const cu = s.charCodeAt(u) - 97;
            lastSeen[cu] = prevVal[u];
            stTop--;
        }
    }

    const deg = new Int32Array(n);
    for (let i = 1; i < n; i++) {
        deg[newParent[i]]++;
    }

    const ans = new Int32Array(n).fill(1);
    const queue = new Int32Array(n);
    let head = 0, tail = 0;
    for (let i = 0; i < n; i++) {
        if (deg[i] === 0) {
            queue[tail++] = i;
        }
    }

    while (head < tail) {
        const u = queue[head++];
        const p = newParent[u];
        if (p !== -1) {
            ans[p] += ans[u];
            deg[p]--;
            if (deg[p] === 0) {
                queue[tail++] = p;
            }
        }
    }

    return Array.from(ans);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findSubtreeSizes(parent: number[], s: string): number[] {
    const n = parent.length;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        adj[parent[i]].push(i);
    }

    const lastSeen = new Int32Array(26).fill(-1);
    const prevVal = new Int32Array(n).fill(-1);
    const newParent = new Int32Array(n).fill(-1);

    const st = new Int32Array(n);
    let stTop = 0;
    st[0] = 0;

    const c0 = s.charCodeAt(0) - 97;
    prevVal[0] = lastSeen[c0];
    lastSeen[c0] = 0;

    const edgeIdx = new Int32Array(n);

    while (stTop >= 0) {
        const u = st[stTop];
        if (edgeIdx[u] < adj[u].length) {
            const v = adj[u][edgeIdx[u]++];
            const cv = s.charCodeAt(v) - 97;
            newParent[v] = lastSeen[cv] !== -1 ? lastSeen[cv] : parent[v];
            prevVal[v] = lastSeen[cv];
            lastSeen[cv] = v;
            stTop++;
            st[stTop] = v;
        } else {
            const cu = s.charCodeAt(u) - 97;
            lastSeen[cu] = prevVal[u];
            stTop--;
        }
    }

    const deg = new Int32Array(n);
    for (let i = 1; i < n; i++) {
        deg[newParent[i]]++;
    }

    const ans = new Int32Array(n).fill(1);
    const queue = new Int32Array(n);
    let head = 0, tail = 0;
    for (let i = 0; i < n; i++) {
        if (deg[i] === 0) {
            queue[tail++] = i;
        }
    }

    while (head < tail) {
        const u = queue[head++];
        const p = newParent[u];
        if (p !== -1) {
            ans[p] += ans[u];
            deg[p]--;
            if (deg[p] === 0) {
                queue[tail++] = p;
            }
        }
    }

    return Array.from(ans);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $parent
     * @param String $s
     * @return Integer[]
     */
    function findSubtreeSizes($parent, $s) {
        $n = count($parent);
        $adj = array_fill(0, $n, []);
        for ($i = 1; $i < $n; $i++) {
            $adj[$parent[$i]][] = $i;
        }

        $lastSeen = array_fill(0, 26, -1);
        $prevVal = array_fill(0, $n, -1);
        $newParent = array_fill(0, $n, -1);

        $st = [0];
        $c0 = ord($s[0]) - 97;
        $prevVal[0] = $lastSeen[$c0];
        $lastSeen[$c0] = 0;

        $edgeIdx = array_fill(0, $n, 0);

        while (!empty($st)) {
            $u = end($st);
            if ($edgeIdx[$u] < count($adj[$u])) {
                $v = $adj[$u][$edgeIdx[$u]];
                $edgeIdx[$u]++;
                $cv = ord($s[$v]) - 97;
                $newParent[$v] = ($lastSeen[$cv] !== -1) ? $lastSeen[$cv] : $parent[$v];
                $prevVal[$v] = $lastSeen[$cv];
                $lastSeen[$cv] = $v;
                $st[] = $v;
            } else {
                $cu = ord($s[$u]) - 97;
                $lastSeen[$cu] = $prevVal[$u];
                array_pop($st);
            }
        }

        $deg = array_fill(0, $n, 0);
        for ($i = 1; $i < $n; $i++) {
            $deg[$newParent[$i]]++;
        }

        $ans = array_fill(0, $n, 1);
        $queue = [];
        for ($i = 0; $i < $n; $i++) {
            if ($deg[$i] === 0) {
                $queue[] = $i;
            }
        }

        $head = 0;
        $qLen = count($queue);
        while ($head < $qLen) {
            $u = $queue[$head++];
            $p = $newParent[$u];
            if ($p !== -1) {
                $ans[$p] += $ans[$u];
                $deg[$p]--;
                if ($deg[$p] === 0) {
                    $queue[] = $p;
                    $qLen++;
                }
            }
        }

        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findSubtreeSizes(_ parent: [Int], _ s: String) -> [Int] {
        let n = parent.count
        var adj = [[Int]](repeating: [Int](), count: n)
        for i in 1..<n {
            adj[parent[i]].append(i)
        }

        let sBytes = Array(s.utf8)
        var lastSeen = [Int](repeating: -1, count: 26)
        var prevVal = [Int](repeating: -1, count: n)
        var newParent = [Int](repeating: -1, count: n)

        var st = [Int]()
        st.reserveCapacity(n)
        st.append(0)

        let c0 = Int(sBytes[0] - 97)
        prevVal[0] = lastSeen[c0]
        lastSeen[c0] = 0

        var edgeIdx = [Int](repeating: 0, count: n)

        while !st.isEmpty {
            let u = st.last!
            if edgeIdx[u] < adj[u].count {
                let v = adj[u][edgeIdx[u]]
                edgeIdx[u] += 1
                let cv = Int(sBytes[v] - 97)
                newParent[v] = lastSeen[cv] != -1 ? lastSeen[cv] : parent[v]
                prevVal[v] = lastSeen[cv]
                lastSeen[cv] = v
                st.append(v)
            } else {
                let cu = Int(sBytes[u] - 97)
                lastSeen[cu] = prevVal[u]
                st.removeLast()
            }
        }

        var deg = [Int](repeating: 0, count: n)
        for i in 1..<n {
            deg[newParent[i]] += 1
        }

        var ans = [Int](repeating: 1, count: n)
        var queue = [Int]()
        queue.reserveCapacity(n)
        for i in 0..<n {
            if deg[i] == 0 {
                queue.append(i)
            }
        }

        var head = 0
        while head < queue.count {
            let u = queue[head]
            head += 1
            let p = newParent[u]
            if p != -1 {
                ans[p] += ans[u]
                deg[p] -= 1
                if deg[p] == 0 {
                    queue.append(p)
                }
            }
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findSubtreeSizes(parent: IntArray, s: String): IntArray {
        val n = parent.size
        var head = IntArray(n) { -1 }
        val next = IntArray(n)
        val to = IntArray(n)
        var edgeCount = 0

        for (i in 1 until n) {
            val p = parent[i]
            to[edgeCount] = i
            next[edgeCount] = head[p]
            head[p] = edgeCount++
        }

        val lastSeen = IntArray(26) { -1 }
        val prevVal = IntArray(n) { -1 }
        val newParent = IntArray(n) { -1 }
        val edgeIdx = IntArray(n)
        for (i in 0 until n) {
            edgeIdx[i] = head[i]
        }

        val st = IntArray(n)
        var stSize = 0
        st[stSize++] = 0
        val c0 = s[0] - 'a'
        prevVal[0] = lastSeen[c0]
        lastSeen[c0] = 0

        while (stSize > 0) {
            val u = st[stSize - 1]
            val e = edgeIdx[u]
            if (e != -1) {
                val v = to[e]
                edgeIdx[u] = next[e]
                val cv = s[v] - 'a'
                newParent[v] = if (lastSeen[cv] != -1) lastSeen[cv] else parent[v]
                prevVal[v] = lastSeen[cv]
                lastSeen[cv] = v
                st[stSize++] = v
            } else {
                val cu = s[u] - 'a'
                lastSeen[cu] = prevVal[u]
                stSize--
            }
        }

        val deg = IntArray(n)
        for (i in 1 until n) {
            deg[newParent[i]]++
        }

        val ans = IntArray(n) { 1 }
        val queue = IntArray(n)
        var qHead = 0
        var qTail = 0
        for (i in 0 until n) {
            if (deg[i] == 0) {
                queue[qTail++] = i
            }
        }

        while (qHead < qTail) {
            val u = queue[qHead++]
            val p = newParent[u]
            if (p != -1) {
                ans[p] += ans[u]
                deg[p]--
                if (deg[p] == 0) {
                    queue[qTail++] = p
                }
            }
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> findSubtreeSizes(List<int> parent, String s) {
    int n = parent.length;
    List<List<int>> adj = List.generate(n, (_) => <int>[]);
    for (int i = 1; i < n; i++) {
      adj[parent[i]].add(i);
    }

    List<int> lastSeen = List.filled(26, -1);
    List<int> prevVal = List.filled(n, -1);
    List<int> newParent = List.filled(n, -1);
    List<int> edgeIdx = List.filled(n, 0);

    List<int> st = [0];
    int c0 = s.codeUnitAt(0) - 97;
    prevVal[0] = lastSeen[c0];
    lastSeen[c0] = 0;

    while (st.isNotEmpty) {
      int u = st.last;
      if (edgeIdx[u] < adj[u].length) {
        int v = adj[u][edgeIdx[u]];
        edgeIdx[u]++;
        int cv = s.codeUnitAt(v) - 97;
        newParent[v] = lastSeen[cv] != -1 ? lastSeen[cv] : parent[v];
        prevVal[v] = lastSeen[cv];
        lastSeen[cv] = v;
        st.add(v);
      } else {
        int cu = s.codeUnitAt(u) - 97;
        lastSeen[cu] = prevVal[u];
        st.removeLast();
      }
    }

    List<int> deg = List.filled(n, 0);
    for (int i = 1; i < n; i++) {
      deg[newParent[i]]++;
    }

    List<int> ans = List.filled(n, 1);
    List<int> queue = [];
    for (int i = 0; i < n; i++) {
      if (deg[i] == 0) {
        queue.add(i);
      }
    }

    int head = 0;
    while (head < queue.length) {
      int u = queue[head++];
      int p = newParent[u];
      if (p != -1) {
        ans[p] += ans[u];
        deg[p]--;
        if (deg[p] == 0) {
          queue.add(p);
        }
      }
    }

    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findSubtreeSizes(parent []int, s string) []int {
    n := len(parent)
    adj := make([][]int, n)
    for i := 1; i < n; i++ {
        adj[parent[i]] = append(adj[parent[i]], i)
    }

    lastSeen := make([]int, 26)
    for i := range lastSeen {
        lastSeen[i] = -1
    }
    prevVal := make([]int, n)
    newParent := make([]int, n)
    for i := range newParent {
        newParent[i] = -1
    }
    edgeIdx := make([]int, n)

    st := []int{0}
    c0 := int(s[0] - 'a')
    prevVal[0] = lastSeen[c0]
    lastSeen[c0] = 0

    for len(st) > 0 {
        u := st[len(st)-1]
        if edgeIdx[u] < len(adj[u]) {
            v := adj[u][edgeIdx[u]]
            edgeIdx[u]++
            cv := int(s[v] - 'a')
            if lastSeen[cv] != -1 {
                newParent[v] = lastSeen[cv]
            } else {
                newParent[v] = parent[v]
            }
            prevVal[v] = lastSeen[cv]
            lastSeen[cv] = v
            st = append(st, v)
        } else {
            cu := int(s[u] - 'a')
            lastSeen[cu] = prevVal[u]
            st = st[:len(st)-1]
        }
    }

    deg := make([]int, n)
    for i := 1; i < n; i++ {
        deg[newParent[i]]++
    }

    ans := make([]int, n)
    for i := 0; i < n; i++ {
        ans[i] = 1
    }

    queue := make([]int, 0, n)
    for i := 0; i < n; i++ {
        if deg[i] == 0 {
            queue = append(queue, i)
        }
    }

    head := 0
    for head < len(queue) {
        u := queue[head]
        head++
        p := newParent[u]
        if p != -1 {
            ans[p] += ans[u]
            deg[p]--
            if deg[p] == 0 {
                queue = append(queue, p)
            }
        }
    }

    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} parent
# @param {String} s
# @return {Integer[]}
def find_subtree_sizes(parent, s)
    n = parent.length
    adj = Array.new(n) { [] }
    (1...n).each do |i|
        adj[parent[i]] << i
    end

    last_seen = Array.new(26, -1)
    prev_val = Array.new(n, -1)
    new_parent = Array.new(n, -1)
    edge_idx = Array.new(n, 0)

    st = [0]
    c0 = s.getbyte(0) - 97
    prev_val[0] = last_seen[c0]
    last_seen[c0] = 0

    while !st.empty?
        u = st.last
        if edge_idx[u] < adj[u].length
            v = adj[u][edge_idx[u]]
            edge_idx[u] += 1
            cv = s.getbyte(v) - 97
            new_parent[v] = last_seen[cv] != -1 ? last_seen[cv] : parent[v]
            prev_val[v] = last_seen[cv]
            last_seen[cv] = v
            st << v
        else
            cu = s.getbyte(u) - 97
            last_seen[cu] = prev_val[u]
            st.pop
        end
    end

    deg = Array.new(n, 0)
    (1...n).each do |i|
        deg[new_parent[i]] += 1
    end

    ans = Array.new(n, 1)
    queue = []
    (0...n).each do |i|
        queue << i if deg[i] == 0
    end

    head = 0
    while head < queue.length
        u = queue[head]
        head += 1
        p = new_parent[u]
        if p != -1
            ans[p] += ans[u]
            deg[p] -= 1
            queue << p if deg[p] == 0
        end
    end

    ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findSubtreeSizes(parent: Array[Int], s: String): Array[Int] = {
        val n = parent.length
        val head = Array.fill(n)(-1)
        val next = new Array[Int](n)
        val to = new Array[Int](n)
        var edgeCount = 0

        var i = 1
        while (i < n) {
            val p = parent(i)
            to(edgeCount) = i
            next(edgeCount) = head(p)
            head(p) = edgeCount
            edgeCount += 1
            i += 1
        }

        val lastSeen = Array.fill(26)(-1)
        val prevVal = Array.fill(n)(-1)
        val newParent = Array.fill(n)(-1)
        val edgeIdx = Array.tabulate(n)(head)

        val st = new Array[Int](n)
        var stSize = 0
        st(stSize) = 0
        stSize += 1
        val c0 = s.charAt(0) - 'a'
        prevVal(0) = lastSeen(c0)
        lastSeen(c0) = 0

        while (stSize > 0) {
            val u = st(stSize - 1)
            val e = edgeIdx(u)
            if (e != -1) {
                val v = to(e)
                edgeIdx(u) = next(e)
                val cv = s.charAt(v) - 'a'
                newParent(v) = if (lastSeen(cv) != -1) lastSeen(cv) else parent(v)
                prevVal(v) = lastSeen(cv)
                lastSeen(cv) = v
                st(stSize) = v
                stSize += 1
            } else {
                val cu = s.charAt(u) - 'a'
                lastSeen(cu) = prevVal(u)
                stSize -= 1
            }
        }

        val deg = new Array[Int](n)
        i = 1
        while (i < n) {
            deg(newParent(i)) += 1
            i += 1
        }

        val ans = Array.fill(n)(1)
        val queue = new Array[Int](n)
        var qHead = 0
        var qTail = 0
        i = 0
        while (i < n) {
            if (deg(i) == 0) {
                queue(qTail) = i
                qTail += 1
            }
            i += 1
        }

        while (qHead < qTail) {
            val u = queue(qHead)
            qHead += 1
            val p = newParent(u)
            if (p != -1) {
                ans(p) += ans(u)
                deg(p) -= 1
                if (deg(p) == 0) {
                    queue(qTail) = p
                    qTail += 1
                }
            }
        }

        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_subtree_sizes(parent: Vec<i32>, s: String) -> Vec<i32> {
        let n = parent.len();
        let s_bytes = s.as_bytes();
        let mut adj = vec![Vec::new(); n];
        for i in 1..n {
            adj[parent[i] as usize].push(i);
        }

        let mut last_seen = [-1i32; 26];
        let mut new_parent = vec![-1i32; n];
        let mut post_order = Vec::with_capacity(n);

        let c0 = (s_bytes[0] - b'a') as usize;
        let old0 = last_seen[c0];
        last_seen[c0] = 0;
        let mut st = vec![(0usize, 0usize, old0)];

        while let Some((u, edge_idx, old_val)) = st.pop() {
            if edge_idx < adj[u].len() {
                let v = adj[u][edge_idx];
                st.push((u, edge_idx + 1, old_val));

                let cv = (s_bytes[v] - b'a') as usize;
                new_parent[v] = if last_seen[cv] != -1 {
                    last_seen[cv]
                } else {
                    parent[v]
                };
                let old_v = last_seen[cv];
                last_seen[cv] = v as i32;
                st.push((v, 0, old_v));
            } else {
                let cu = (s_bytes[u] - b'a') as usize;
                last_seen[cu] = old_val;
                post_order.push(u);
            }
        }

        let mut ans = vec![1i32; n];
        for &u in &post_order {
            let p = new_parent[u];
            if p != -1 {
                ans[p as usize] += ans[u];
            }
        }

        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-subtree-sizes parent s)
  (-> (listof exact-integer?) string? (listof exact-integer?))
  (let* ([n (length parent)]
         [p-vec (list->vector parent)]
         [s-bytes (string->bytes/utf-8 s)]
         [adj (make-vector n '())])
    (for ([i (in-range 1 n)])
      (let ([p (vector-ref p-vec i)])
        (vector-set! adj p (cons i (vector-ref adj p)))))
    (define last-seen (make-vector 26 -1))
    (define new-parent (make-vector n -1))
    (define c0 (- (bytes-ref s-bytes 0) 97))
    (define old0 (vector-ref last-seen c0))
    (vector-set! last-seen c0 0)
    (define st (list (list 0 (vector-ref adj 0) old0)))
    (define post-order '())
    (let loop ([stack st])
      (when (pair? stack)
        (let* ([top (car stack)]
               [u (car top)]
               [children (cadr top)]
               [old-val (caddr top)]
               [rest-stack (cdr stack)])
          (if (pair? children)
              (let* ([v (car children)]
                     [new-top (list u (cdr children) old-val)]
                     [cv (- (bytes-ref s-bytes v) 97)]
                     [ls (vector-ref last-seen cv)]
                     [np (if (= ls -1) (vector-ref p-vec v) ls)]
                     [old-v ls])
                (vector-set! new-parent v np)
                (vector-set! last-seen cv v)
                (loop (cons (list v (vector-ref adj v) old-v) (cons new-top rest-stack))))
              (let ([cu (- (bytes-ref s-bytes u) 97)])
                (vector-set! last-seen cu old-val)
                (set! post-order (cons u post-order))
                (loop rest-stack))))))
    (define ans (make-vector n 1))
    (for ([u (in-list (reverse post-order))])
      (let ([p (vector-ref new-parent u)])
        (when (not (= p -1))
          (vector-set! ans p (+ (vector-ref ans p) (vector-ref ans u))))))
    (vector->list ans)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_subtree_sizes(Parent :: [integer()], S :: unicode:unicode_binary()) -> [integer()].
find_subtree_sizes(Parent, S) ->
    N = length(Parent),
    PArr = array:from_list(Parent),
    Adj0 = array:new(N, {default, []}),
    Adj = lists:foldl(fun({I, P}, Acc) ->
        if
            P >= 0 -> array:set(P, [I | array:get(P, Acc)], Acc);
            true -> Acc
        end
    end, Adj0, lists:zip(lists:seq(0, N - 1), Parent)),

    C0 = binary:at(S, 0) - $a,
    LastSeen0 = erlang:make_tuple(26, -1),
    Old0 = element(C0 + 1, LastSeen0),
    LastSeen1 = setelement(C0 + 1, LastSeen0, 0),
    NewParent0 = array:new(N, {default, -1}),

    Stack0 = [{0, array:get(0, Adj), Old0}],

    {NewParent, PostOrder} = dfs(Stack0, LastSeen1, NewParent0, [], S, Adj, PArr),

    Ans0 = array:new(N, {default, 1}),
    Ans = lists:foldl(fun(U, AccAns) ->
        P = array:get(U, NewParent),
        if
            P >= 0 ->
                Val = array:get(P, AccAns) + array:get(U, AccAns),
                array:set(P, Val, AccAns);
            true ->
                AccAns
        end
    end, Ans0, lists:reverse(PostOrder)),

    array:to_list(Ans).

dfs([], _LastSeen, NewParent, PostOrder, _S, _Adj, _PArr) ->
    {NewParent, PostOrder};
dfs([{U, [V | RestChildren], OldVal} | RestStack], LastSeen, NewParent, PostOrder, S, Adj, PArr) ->
    CV = binary:at(S, V) - $a,
    LS = element(CV + 1, LastSeen),
    NP = if LS =:= -1 -> array:get(V, PArr); true -> LS end,
    NewParent1 = array:set(V, NP, NewParent),
    OldV = LS,
    LastSeen1 = setelement(CV + 1, LastSeen, V),
    NewTop = {U, RestChildren, OldVal},
    dfs([{V, array:get(V, Adj), OldV}, NewTop | RestStack], LastSeen1, NewParent1, PostOrder, S, Adj, PArr);
dfs([{U, [], OldVal} | RestStack], LastSeen, NewParent, PostOrder, S, Adj, PArr) ->
    CU = binary:at(S, U) - $a,
    LastSeen1 = setelement(CU + 1, LastSeen, OldVal),
    dfs(RestStack, LastSeen1, NewParent, [U | PostOrder], S, Adj, PArr).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_subtree_sizes(parent :: [integer], s :: String.t) :: [integer]
  def find_subtree_sizes(parent, s) do
    n = length(parent)
    p_arr = :array.from_list(parent)

    adj0 = :array.new(n, default: [])
    adj =
      parent
      |> Enum.with_index()
      |> Enum.reduce(adj0, fn {p, i}, acc ->
        if p >= 0 do
          :array.set(p, [i | :array.get(p, acc)], acc)
        else
          acc
        end
      end)

    c0 = :binary.at(s, 0) - ?a
    last_seen0 = :erlang.make_tuple(26, -1)
    old0 = elem(last_seen0, c0)
    last_seen1 = put_elem(last_seen0, c0, 0)
    new_parent0 = :array.new(n, default: -1)

    stack0 = [{0, :array.get(0, adj), old0}]

    {new_parent, post_order} = dfs(stack0, last_seen1, new_parent0, [], s, adj, p_arr)

    ans0 = :array.new(n, default: 1)

    ans =
      post_order
      |> Enum.reverse()
      |> Enum.reduce(ans0, fn u, acc ->
        p = :array.get(u, new_parent)
        if p >= 0 do
          val = :array.get(p, acc) + :array.get(u, acc)
          :array.set(p, val, acc)
        else
          acc
        end
      end)

    :array.to_list(ans)
  end

  defp dfs([], _last_seen, new_parent, post_order, _s, _adj, _p_arr) do
    {new_parent, post_order}
  end

  defp dfs([{u, [v | rest_children], old_val} | rest_stack], last_seen, new_parent, post_order, s, adj, p_arr) do
    cv = :binary.at(s, v) - ?a
    ls = elem(last_seen, cv)
    np = if ls == -1, do: :array.get(v, p_arr), else: ls
    new_parent1 = :array.set(v, np, new_parent)
    old_v = ls
    last_seen1 = put_elem(last_seen, cv, v)
    new_top = {u, rest_children, old_val}
    dfs([{v, :array.get(v, adj), old_v}, new_top | rest_stack], last_seen1, new_parent1, post_order, s, adj, p_arr)
  end

  defp dfs([{u, [], old_val} | rest_stack], last_seen, new_parent, post_order, s, adj, p_arr) do
    cu = :binary.at(s, u) - ?a
    last_seen1 = put_elem(last_seen, cu, old_val)
    dfs(rest_stack, last_seen1, new_parent, [u | post_order], s, adj, p_arr)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of nodes. Building the adjacency list, performing the DFS traversal with constant-time ancestor updates for 26 characters, and aggregating subtree sizes bottom-up with Kahn's algorithm all operate in linear time.
- **Space Complexity:** O(n) to store the adjacency lists, new parent array, tracking state, queue, and output answers.
