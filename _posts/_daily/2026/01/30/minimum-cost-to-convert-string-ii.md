---
layout: post
title: "Minimum Cost to Convert String II"
date: 2026-01-30 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "String", "Dynamic Programming", "Graph Theory", "Trie", "Shortest Path"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-cost-to-convert-string-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long minimumCost(string source, string\
        \ target, vector<string>& original, vector<string>& changed, vector<int>& cost)\
        \ {\n        unordered_map<string, int> id_map;\n        int id_cnt = 0;\n \
        \       auto get_id = [&](const string& s) {\n            if (id_map.find(s)\
        \ == id_map.end()) id_map[s] = id_cnt++;\n            return id_map[s];\n  \
        \      };\n        for (const string& s : original) get_id(s);\n        for\
        \ (const string& s : changed) get_id(s);\n\n        long long INF = 1e15;\n\
        \        vector<vector<long long>> dist(id_cnt, vector<long long>(id_cnt, INF));\n\
        \        for (int i = 0; i < id_cnt; ++i) dist[i][i] = 0;\n        for (int\
        \ i = 0; i < original.size(); ++i) {\n            int u = id_map[original[i]],\
        \ v = id_map[changed[i]];\n            dist[u][v] = min(dist[u][v], (long long)cost[i]);\n\
        \        }\n\n        for (int k = 0; k < id_cnt; ++k) {\n            for (int\
        \ i = 0; i < id_cnt; ++i) {\n                if (dist[i][k] == INF) continue;\n\
        \                for (int j = 0; j < id_cnt; ++j) {\n                    dist[i][j]\
        \ = min(dist[i][j], dist[i][k] + dist[k][j]);\n                }\n         \
        \   }\n        }\n\n        int n = source.length();\n        set<int> unique_lengths;\n\
        \        for (const string& s : original) unique_lengths.insert(s.length());\n\
        \n        vector<long long> dp(n + 1, INF);\n        dp[0] = 0;\n        for\
        \ (int i = 0; i < n; ++i) {\n            if (dp[i] == INF) continue;\n     \
        \       if (source[i] == target[i]) dp[i + 1] = min(dp[i + 1], dp[i]);\n   \
        \         for (int L : unique_lengths) {\n                if (i + L <= n) {\n\
        \                    string sub_s = source.substr(i, L);\n                 \
        \   string sub_t = target.substr(i, L);\n                    if (id_map.count(sub_s)\
        \ && id_map.count(sub_t)) {\n                        int u = id_map[sub_s],\
        \ v = id_map[sub_t];\n                        if (dist[u][v] < INF) dp[i + L]\
        \ = min(dp[i + L], dp[i] + dist[u][v]);\n                    }\n           \
        \     }\n            }\n        }\n        return dp[n] >= INF ? -1 : dp[n];\n\
        \    }\n};"
      java: "class Solution {\n    public long minimumCost(String source, String target,\
        \ String[] original, String[] changed, int[] cost) {\n        Map<String, Integer>\
        \ idMap = new HashMap<>();\n        int idCnt = 0;\n        for (String s :\
        \ original) if (!idMap.containsKey(s)) idMap.put(s, idCnt++);\n        for (String\
        \ s : changed) if (!idMap.containsKey(s)) idMap.put(s, idCnt++);\n\n       \
        \ long INF = 1_000_000_000_000_000L;\n        long[][] dist = new long[idCnt][idCnt];\n\
        \        for (int i = 0; i < idCnt; i++) {\n            Arrays.fill(dist[i],\
        \ INF);\n            dist[i][i] = 0;\n        }\n\n        for (int i = 0; i\
        \ < original.length; i++) {\n            int u = idMap.get(original[i]), v =\
        \ idMap.get(changed[i]);\n            dist[u][v] = Math.min(dist[u][v], (long)\
        \ cost[i]);\n        }\n\n        for (int k = 0; k < idCnt; k++) {\n      \
        \      for (int i = 0; i < idCnt; i++) {\n                if (dist[i][k] ==\
        \ INF) continue;\n                for (int j = 0; j < idCnt; j++) {\n      \
        \              dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);\n\
        \                }\n            }\n        }\n\n        int n = source.length();\n\
        \        Set<Integer> uniqueLengths = new HashSet<>();\n        for (String\
        \ s : original) uniqueLengths.add(s.length());\n\n        long[] dp = new long[n\
        \ + 1];\n        Arrays.fill(dp, INF);\n        dp[0] = 0;\n\n        for (int\
        \ i = 0; i < n; i++) {\n            if (dp[i] == INF) continue;\n          \
        \  if (source.charAt(i) == target.charAt(i)) dp[i + 1] = Math.min(dp[i + 1],\
        \ dp[i]);\n            for (int L : uniqueLengths) {\n                if (i\
        \ + L <= n) {\n                    String subS = source.substring(i, i + L);\n\
        \                    String subT = target.substring(i, i + L);\n           \
        \         if (idMap.containsKey(subS) && idMap.containsKey(subT)) {\n      \
        \                  int u = idMap.get(subS), v = idMap.get(subT);\n         \
        \               if (dist[u][v] < INF) dp[i + L] = Math.min(dp[i + L], dp[i]\
        \ + dist[u][v]);\n                    }\n                }\n            }\n\
        \        }\n        return dp[n] >= INF ? -1 : dp[n];\n    }\n}"
      python: "class Solution(object):\n    def minimumCost(self, source, target, original,\
        \ changed, cost):\n        id_map = {}\n        id_cnt = 0\n        for s in\
        \ original + changed:\n            if s not in id_map:\n                id_map[s]\
        \ = id_cnt\n                id_cnt += 1\n\n        INF = float('inf')\n    \
        \    dist = [[INF] * id_cnt for _ in range(id_cnt)]\n        for i in range(id_cnt):\
        \ dist[i][i] = 0\n\n        for i in range(len(original)):\n            u, v\
        \ = id_map[original[i]], id_map[changed[i]]\n            dist[u][v] = min(dist[u][v],\
        \ cost[i])\n\n        for k in range(id_cnt):\n            for i in range(id_cnt):\n\
        \                if dist[i][k] == INF: continue\n                for j in range(id_cnt):\n\
        \                    if dist[i][k] + dist[k][j] < dist[i][j]:\n            \
        \            dist[i][j] = dist[i][k] + dist[k][j]\n\n        n = len(source)\n\
        \        unique_lengths = sorted(list(set(len(s) for s in original)))\n    \
        \    dp = [INF] * (n + 1)\n        dp[0] = 0\n\n        for i in range(n):\n\
        \            if dp[i] == INF: continue\n            if source[i] == target[i]:\n\
        \                dp[i+1] = min(dp[i+1], dp[i])\n            for L in unique_lengths:\n\
        \                if i + L <= n:\n                    sub_s = source[i:i+L]\n\
        \                    sub_t = target[i:i+L]\n                    if sub_s in\
        \ id_map and sub_t in id_map:\n                        u, v = id_map[sub_s],\
        \ id_map[sub_t]\n                        if dist[u][v] < INF:\n            \
        \                dp[i+L] = min(dp[i+L], dp[i] + dist[u][v])\n\n        return\
        \ int(dp[n]) if dp[n] < INF else -1"
      python3: "class Solution:\n    def minimumCost(self, source: str, target: str,\
        \ original: List[str], changed: List[str], cost: List[int]) -> int:\n      \
        \  id_map = {}\n        id_cnt = 0\n        for s in original + changed:\n \
        \           if s not in id_map:\n                id_map[s] = id_cnt\n      \
        \          id_cnt += 1\n\n        INF = float('inf')\n        dist = [[INF]\
        \ * id_cnt for _ in range(id_cnt)]\n        for i in range(id_cnt): dist[i][i]\
        \ = 0\n\n        for i in range(len(original)):\n            u, v = id_map[original[i]],\
        \ id_map[changed[i]]\n            dist[u][v] = min(dist[u][v], cost[i])\n\n\
        \        for k in range(id_cnt):\n            for i in range(id_cnt):\n    \
        \            if dist[i][k] == INF: continue\n                for j in range(id_cnt):\n\
        \                    if dist[i][k] + dist[k][j] < dist[i][j]:\n            \
        \            dist[i][j] = dist[i][k] + dist[k][j]\n\n        n = len(source)\n\
        \        unique_lengths = sorted(list(set(len(s) for s in original)))\n    \
        \    dp = [INF] * (n + 1)\n        dp[0] = 0\n\n        for i in range(n):\n\
        \            if dp[i] == INF: continue\n            if source[i] == target[i]:\n\
        \                dp[i+1] = min(dp[i+1], dp[i])\n            for L in unique_lengths:\n\
        \                if i + L <= n:\n                    sub_s = source[i:i+L]\n\
        \                    sub_t = target[i:i+L]\n                    if sub_s in\
        \ id_map and sub_t in id_map:\n                        u, v = id_map[sub_s],\
        \ id_map[sub_t]\n                        if dist[u][v] < INF:\n            \
        \                dp[i+L] = min(dp[i+L], dp[i] + dist[u][v])\n\n        return\
        \ int(dp[n]) if dp[n] < INF else -1"
      c: "#include <string.h>\n#include <stdlib.h>\n#include <stdio.h>\n\n#define INF\
        \ 1e15\n\ntypedef struct {\n    int children[26];\n    int id;\n} TrieNode;\n\
        \nstatic TrieNode trie[200005];\nstatic int nodes_cnt;\n\nvoid reset_trie()\
        \ {\n    for (int i = 0; i < nodes_cnt; ++i) {\n        for (int j = 0; j <\
        \ 26; ++j) trie[i].children[j] = 0;\n        trie[i].id = -1;\n    }\n    nodes_cnt\
        \ = 1;\n    trie[0].id = -1;\n}\n\nint insert_trie(const char* s, int* id_gen)\
        \ {\n    int curr = 0;\n    for (int i = 0; s[i]; ++i) {\n        int c = s[i]\
        \ - 'a';\n        if (!trie[curr].children[c]) {\n            for (int j = 0;\
        \ j < 26; j++) trie[nodes_cnt].children[j] = 0;\n            trie[nodes_cnt].id\
        \ = -1;\n            trie[curr].children[c] = nodes_cnt++;\n        }\n    \
        \    curr = trie[curr].children[c];\n    }\n    if (trie[curr].id == -1) trie[curr].id\
        \ = (*id_gen)++;\n    return trie[curr].id;\n}\n\nlong long minimumCost(char*\
        \ source, char* target, char** original, int originalSize, char** changed, int\
        \ changedSize, int* cost, int costSize) {\n    reset_trie();\n    int id_gen\
        \ = 0;\n    long long dist[205][205];\n    for (int i = 0; i < 205; i++) {\n\
        \        for (int j = 0; j < 205; j++) dist[i][j] = (i == j ? 0 : INF);\n  \
        \  }\n    for (int i = 0; i < originalSize; i++) {\n        int u = insert_trie(original[i],\
        \ &id_gen);\n        int v = insert_trie(changed[i], &id_gen);\n        if (cost[i]\
        \ < dist[u][v]) dist[u][v] = cost[i];\n    }\n    for (int k = 0; k < id_gen;\
        \ k++) {\n        for (int i = 0; i < id_gen; i++) {\n            if (dist[i][k]\
        \ == INF) continue;\n            for (int j = 0; j < id_gen; j++) {\n      \
        \          if (dist[k][j] < INF && dist[i][k] + dist[k][j] < dist[i][j])\n \
        \                   dist[i][j] = dist[i][k] + dist[k][j];\n            }\n \
        \       }\n    }\n    int n = strlen(source);\n    long long* dp = malloc(sizeof(long\
        \ long) * (n + 1));\n    for (int i = 0; i <= n; i++) dp[i] = INF;\n    dp[0]\
        \ = 0;\n    for (int i = 0; i < n; i++) {\n        if (dp[i] == INF) continue;\n\
        \        if (source[i] == target[i]) if (dp[i] < dp[i+1]) dp[i+1] = dp[i];\n\
        \        int s_node = 0, t_node = 0;\n        for (int L = 1; i + L <= n; L++)\
        \ {\n            int cs = source[i+L-1] - 'a', ct = target[i+L-1] - 'a';\n \
        \           s_node = (s_node != -1 && trie[s_node].children[cs]) ? trie[s_node].children[cs]\
        \ : -1;\n            t_node = (t_node != -1 && trie[t_node].children[ct]) ?\
        \ trie[t_node].children[ct] : -1;\n            if (s_node == -1 && t_node ==\
        \ -1) break;\n            if (s_node != -1 && t_node != -1 && trie[s_node].id\
        \ != -1 && trie[t_node].id != -1) {\n                int u = trie[s_node].id,\
        \ v = trie[t_node].id;\n                if (dist[u][v] < INF && dp[i] + dist[u][v]\
        \ < dp[i+L]) dp[i+L] = dp[i] + dist[u][v];\n            }\n        }\n    }\n\
        \    long long res = (dp[n] >= INF ? -1 : dp[n]);\n    free(dp);\n    return\
        \ res;\n}"
      csharp: "public class Solution {\n    public long MinimumCost(string source, string\
        \ target, string[] original, string[] changed, int[] cost) {\n        var idMap\
        \ = new Dictionary<string, int>();\n        int idCnt = 0;\n        int GetId(string\
        \ s) {\n            if (!idMap.ContainsKey(s)) idMap[s] = idCnt++;\n       \
        \     return idMap[s];\n        }\n        for (int i = 0; i < original.Length;\
        \ i++) {\n            GetId(original[i]);\n            GetId(changed[i]);\n\
        \        }\n        long INF = 1_000_000_000_000_000L;\n        long[,] dist\
        \ = new long[idCnt, idCnt];\n        for (int i = 0; i < idCnt; i++) {\n   \
        \         for (int j = 0; j < idCnt; j++) dist[i, j] = (i == j ? 0 : INF);\n\
        \        }\n        for (int i = 0; i < original.Length; i++) {\n          \
        \  int u = idMap[original[i]], v = idMap[changed[i]];\n            dist[u, v]\
        \ = Math.Min(dist[u, v], (long)cost[i]);\n        }\n        for (int k = 0;\
        \ k < idCnt; k++) {\n            for (int i = 0; i < idCnt; i++) {\n       \
        \         if (dist[i, k] == INF) continue;\n                for (int j = 0;\
        \ j < idCnt; j++) {\n                    dist[i, j] = Math.Min(dist[i, j], dist[i,\
        \ k] + dist[k, j]);\n                }\n            }\n        }\n        int\
        \ n = source.Length;\n        var uniqueLengths = original.Select(s => s.Length).Distinct().ToList();\n\
        \        long[] dp = new long[n + 1];\n        for (int i = 0; i <= n; i++)\
        \ dp[i] = INF;\n        dp[0] = 0;\n        for (int i = 0; i < n; i++) {\n\
        \            if (dp[i] == INF) continue;\n            if (source[i] == target[i])\
        \ dp[i + 1] = Math.Min(dp[i + 1], dp[i]);\n            foreach (int L in uniqueLengths)\
        \ {\n                if (i + L <= n) {\n                    string subS = source.Substring(i,\
        \ L);\n                    string subT = target.Substring(i, L);\n         \
        \           if (idMap.ContainsKey(subS) && idMap.ContainsKey(subT)) {\n    \
        \                    int u = idMap[subS], v = idMap[subT];\n               \
        \         if (dist[u, v] < INF) dp[i + L] = Math.Min(dp[i + L], dp[i] + dist[u,\
        \ v]);\n                    }\n                }\n            }\n        }\n\
        \        return dp[n] >= INF ? -1 : dp[n];\n    }\n}"
      javascript: "/**\n * @param {string} source\n * @param {string} target\n * @param\
        \ {string[]} original\n * @param {string[]} changed\n * @param {number[]} cost\n\
        \ * @return {number}\n */\nvar minimumCost = function(source, target, original,\
        \ changed, cost) {\n    const idMap = new Map();\n    let idCnt = 0;\n    const\
        \ getId = (s) => {\n        if (!idMap.has(s)) idMap.set(s, idCnt++);\n    \
        \    return idMap.get(s);\n    };\n    for (const s of original) getId(s);\n\
        \    for (const s of changed) getId(s);\n\n    const INF = 1e15;\n    const\
        \ dist = Array.from({ length: idCnt }, () => Array(idCnt).fill(INF));\n    for\
        \ (let i = 0; i < idCnt; i++) dist[i][i] = 0;\n    for (let i = 0; i < original.length;\
        \ i++) {\n        const u = idMap.get(original[i]), v = idMap.get(changed[i]);\n\
        \        dist[u][v] = Math.min(dist[u][v], cost[i]);\n    }\n\n    for (let\
        \ k = 0; k < idCnt; k++) {\n        for (let i = 0; i < idCnt; i++) {\n    \
        \        if (dist[i][k] === INF) continue;\n            for (let j = 0; j <\
        \ idCnt; j++) {\n                dist[i][j] = Math.min(dist[i][j], dist[i][k]\
        \ + dist[k][j]);\n            }\n        }\n    }\n\n    const n = source.length;\n\
        \    const uniqueLengths = [...new Set(original.map(s => s.length))];\n    const\
        \ dp = new Array(n + 1).fill(INF);\n    dp[0] = 0;\n\n    for (let i = 0; i\
        \ < n; i++) {\n        if (dp[i] === INF) continue;\n        if (source[i] ===\
        \ target[i]) dp[i + 1] = Math.min(dp[i + 1], dp[i]);\n        for (const L of\
        \ uniqueLengths) {\n            if (i + L <= n) {\n                const subS\
        \ = source.substring(i, i + L);\n                const subT = target.substring(i,\
        \ i + L);\n                if (idMap.has(subS) && idMap.has(subT)) {\n     \
        \               const u = idMap.get(subS), v = idMap.get(subT);\n          \
        \          if (dist[u][v] < INF) dp[i + L] = Math.min(dp[i + L], dp[i] + dist[u][v]);\n\
        \                }\n            }\n        }\n    }\n\n    return dp[n] >= INF\
        \ ? -1 : dp[n];\n};"
      typescript: "function minimumCost(source: string, target: string, original: string[],\
        \ changed: string[], cost: number[]): number {\n    const n = source.length;\n\
        \    const m = original.length;\n    const INF = 1e15;\n\n    const idMap =\
        \ new Map<string, number>();\n    let idCounter = 0;\n    const getID = (s:\
        \ string) => {\n        if (!idMap.has(s)) idMap.set(s, idCounter++);\n    \
        \    return idMap.get(s)!;\n    };\n\n    for (let i = 0; i < m; i++) {\n  \
        \      getID(original[i]);\n        getID(changed[i]);\n    }\n\n    const M\
        \ = idCounter;\n    const dist = Array.from({ length: M }, () => new Float64Array(M).fill(INF));\n\
        \    for (let i = 0; i < M; i++) dist[i][i] = 0;\n\n    for (let i = 0; i <\
        \ m; i++) {\n        const u = getID(original[i]);\n        const v = getID(changed[i]);\n\
        \        dist[u][v] = Math.min(dist[u][v], cost[i]);\n    }\n\n    for (let\
        \ k = 0; k < M; k++) {\n        for (let i = 0; i < M; i++) {\n            for\
        \ (let j = 0; j < M; j++) {\n                if (dist[i][k] + dist[k][j] < dist[i][j])\
        \ {\n                    dist[i][j] = dist[i][k] + dist[k][j];\n           \
        \     }\n            }\n        }\n    }\n\n    class TrieNode {\n        children:\
        \ { [key: string]: TrieNode } = {};\n        id: number = -1;\n    }\n\n   \
        \ const root = new TrieNode();\n    for (const [s, id] of idMap.entries()) {\n\
        \        let curr = root;\n        for (const char of s) {\n            if (!curr.children[char])\
        \ curr.children[char] = new TrieNode();\n            curr = curr.children[char];\n\
        \        }\n        curr.id = id;\n    }\n\n    const sourceIds = Array.from({\
        \ length: n }, () => new Int32Array(n + 1).fill(-1));\n    const targetIds =\
        \ Array.from({ length: n }, () => new Int32Array(n + 1).fill(-1));\n\n    const\
        \ fillIds = (str: string, targetArr: Int32Array[]) => {\n        for (let i\
        \ = 0; i < n; i++) {\n            let curr = root;\n            for (let j =\
        \ i; j < n; j++) {\n                if (!curr.children[str[j]]) break;\n   \
        \             curr = curr.children[str[j]];\n                if (curr.id !==\
        \ -1) targetArr[i][j - i + 1] = curr.id;\n            }\n        }\n    };\n\
        \n    fillIds(source, sourceIds);\n    fillIds(target, targetIds);\n\n    const\
        \ uniqueLens = Array.from(new Set(original.map(s => s.length)));\n    const\
        \ dp = new Float64Array(n + 1).fill(INF);\n    dp[0] = 0;\n\n    for (let i\
        \ = 0; i < n; i++) {\n        if (dp[i] === INF) continue;\n        if (source[i]\
        \ === target[i]) dp[i + 1] = Math.min(dp[i + 1], dp[i]);\n        for (const\
        \ len of uniqueLens) {\n            if (i + len <= n) {\n                const\
        \ u = sourceIds[i][len];\n                const v = targetIds[i][len];\n   \
        \             if (u !== -1 && v !== -1 && dist[u][v] < INF) {\n            \
        \        dp[i + len] = Math.min(dp[i + len], dp[i] + dist[u][v]);\n        \
        \        }\n            }\n        }\n    }\n\n    return dp[n] >= INF ? -1\
        \ : dp[n];\n};"
      php: "class Solution {\n    function minimumCost($source, $target, $original,\
        \ $changed, $cost) {\n        $n = strlen($source);\n        $m = count($original);\n\
        \        $INF = 1e15;\n        $idMap = [];\n        $idCounter = 0;\n     \
        \   $uniqueLens = [];\n\n        for ($i = 0; $i < $m; $i++) {\n           \
        \ if (!isset($idMap[$original[$i]])) $idMap[$original[$i]] = $idCounter++;\n\
        \            if (!isset($idMap[$changed[$i]])) $idMap[$changed[$i]] = $idCounter++;\n\
        \            $uniqueLens[strlen($original[$i])] = true;\n        }\n\n     \
        \   $M = $idCounter;\n        $dist = array_fill(0, $M, array_fill(0, $M, $INF));\n\
        \        for ($i = 0; $i < $M; $i++) $dist[$i][$i] = 0;\n\n        for ($i =\
        \ 0; $i < $m; $i++) {\n            $u = $idMap[$original[$i]];\n           \
        \ $v = $idMap[$changed[$i]];\n            $dist[$u][$v] = min($dist[$u][$v],\
        \ $cost[$i]);\n        }\n\n        for ($k = 0; $k < $M; $k++) {\n        \
        \    for ($i = 0; $i < $M; $i++) {\n                for ($j = 0; $j < $M; $j++)\
        \ {\n                    if ($dist[$i][$k] + $dist[$k][$j] < $dist[$i][$j])\
        \ {\n                        $dist[$i][$j] = $dist[$i][$k] + $dist[$k][$j];\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    $root = ['children' => [], 'id' => -1];\n        foreach ($idMap as $s\
        \ => $id) {\n            $curr = &$root;\n            for ($j = 0; $j < strlen($s);\
        \ $j++) {\n                if (!isset($curr['children'][$s[$j]])) $curr['children'][$s[$j]]\
        \ = ['children' => [], 'id' => -1];\n                $curr = &$curr['children'][$s[$j]];\n\
        \            }\n            $curr['id'] = $id;\n        }\n\n        $sourceIds\
        \ = array_fill(0, $n, []);\n        $targetIds = array_fill(0, $n, []);\n\n\
        \        $fillIds = function($str, &$targetArr, $n, $root) {\n            for\
        \ ($i = 0; $i < $n; $i++) {\n                $curr = $root;\n              \
        \  for ($j = $i; $j < $n; $j++) {\n                    if (!isset($curr['children'][$str[$j]]))\
        \ break;\n                    $curr = $curr['children'][$str[$j]];\n       \
        \             if ($curr['id'] !== -1) $targetArr[$i][$j - $i + 1] = $curr['id'];\n\
        \                }\n            }\n        };\n\n        $fillIds($source, $sourceIds,\
        \ $n, $root);\n        $fillIds($target, $targetIds, $n, $root);\n\n       \
        \ $dp = array_fill(0, $n + 1, $INF);\n        $dp[0] = 0;\n        $lens = array_keys($uniqueLens);\n\
        \n        for ($i = 0; $i < $n; $i++) {\n            if ($dp[$i] >= $INF) continue;\n\
        \            if ($source[$i] === $target[$i]) $dp[$i+1] = min($dp[$i+1], $dp[$i]);\n\
        \            foreach ($lens as $len) {\n                if ($i + $len <= $n)\
        \ {\n                    if (isset($sourceIds[$i][$len]) && isset($targetIds[$i][$len]))\
        \ {\n                        $u = $sourceIds[$i][$len];\n                  \
        \      $v = $targetIds[$i][$len];\n                        if ($dist[$u][$v]\
        \ < $INF) {\n                            $dp[$i + $len] = min($dp[$i + $len],\
        \ $dp[$i] + $dist[$u][$v]);\n                        }\n                   \
        \ }\n                }\n            }\n        }\n\n        return $dp[$n] >=\
        \ $INF ? -1 : $dp[$n];\n    }\n}"
      swift: "class Solution {\n    class TrieNode {\n        var children = [Character:\
        \ TrieNode]()\n        var id: Int = -1\n    }\n\n    func minimumCost(_ source:\
        \ String, _ target: String, _ original: [String], _ changed: [String], _ cost:\
        \ [Int]) -> Int {\n        let n = source.count\n        let m = original.count\n\
        \        let INF = 1_000_000_000_000_000\n\n        var idMap = [String: Int]()\n\
        \        var idCounter = 0\n        var uniqueLens = Set<Int>()\n\n        let\
        \ sArr = Array(source)\n        let tArr = Array(target)\n\n        for i in\
        \ 0..<m {\n            if idMap[original[i]] == nil { idMap[original[i]] = idCounter;\
        \ idCounter += 1 }\n            if idMap[changed[i]] == nil { idMap[changed[i]]\
        \ = idCounter; idCounter += 1 }\n            uniqueLens.insert(original[i].count)\n\
        \        }\n\n        let M = idCounter\n        var dist = [[Int]](repeating:\
        \ [Int](repeating: INF, count: M), count: M)\n        for i in 0..<M { dist[i][i]\
        \ = 0 }\n\n        for i in 0..<m {\n            let u = idMap[original[i]]!\n\
        \            let v = idMap[changed[i]]!\n            dist[u][v] = min(dist[u][v],\
        \ cost[i])\n        }\n\n        for k in 0..<M {\n            for i in 0..<M\
        \ {\n                for j in 0..<M {\n                    if dist[i][k] + dist[k][j]\
        \ < dist[i][j] {\n                        dist[i][j] = dist[i][k] + dist[k][j]\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    let root = TrieNode()\n        for (s, id) in idMap {\n            var\
        \ curr = root\n            for char in s {\n                if curr.children[char]\
        \ == nil { curr.children[char] = TrieNode() }\n                curr = curr.children[char]!\n\
        \            }\n            curr.id = id\n        }\n\n        var sourceIds\
        \ = [[Int: Int]](repeating: [:], count: n)\n        var targetIds = [[Int: Int]](repeating:\
        \ [:], count: n)\n\n        for i in 0..<n {\n            var curr = root\n\
        \            for j in i..<n {\n                if let next = curr.children[sArr[j]]\
        \ {\n                    curr = next\n                    if curr.id != -1 {\
        \ sourceIds[i][j - i + 1] = curr.id }\n                } else { break }\n  \
        \          }\n            curr = root\n            for j in i..<n {\n      \
        \          if let next = curr.children[tArr[j]] {\n                    curr\
        \ = next\n                    if curr.id != -1 { targetIds[i][j - i + 1] = curr.id\
        \ }\n                } else { break }\n            }\n        }\n\n        var\
        \ dp = [Int](repeating: INF, count: n + 1)\n        dp[0] = 0\n        let lens\
        \ = Array(uniqueLens)\n\n        for i in 0..<n {\n            if dp[i] == INF\
        \ { continue }\n            if sArr[i] == tArr[i] { dp[i + 1] = min(dp[i + 1],\
        \ dp[i]) }\n            for len in lens {\n                if i + len <= n,\
        \ let u = sourceIds[i][len], let v = targetIds[i][len] {\n                 \
        \   if dist[u][v] < INF {\n                        dp[i + len] = min(dp[i +\
        \ len], dp[i] + dist[u][v])\n                    }\n                }\n    \
        \        }\n        }\n\n        return dp[n] >= INF ? -1 : dp[n]\n    }\n}"
      kotlin: "class Solution {\n    class TrieNode {\n        val children = arrayOfNulls<TrieNode>(26)\n\
        \        var id = -1\n    }\n\n    fun minimumCost(source: String, target: String,\
        \ original: Array<String>, changed: Array<String>, cost: IntArray): Long {\n\
        \        val n = source.length\n        val m = original.size\n        val INF\
        \ = 1e15.toLong()\n        val idMap = mutableMapOf<String, Int>()\n       \
        \ var idCounter = 0\n        val uniqueLens = mutableSetOf<Int>()\n\n      \
        \  for (i in 0 until m) {\n            if (!idMap.containsKey(original[i]))\
        \ idMap[original[i]] = idCounter++\n            if (!idMap.containsKey(changed[i]))\
        \ idMap[changed[i]] = idCounter++\n            uniqueLens.add(original[i].length)\n\
        \        }\n\n        val M = idCounter\n        val dist = Array(M) { LongArray(M)\
        \ { INF } }\n        for (i in 0 until M) dist[i][i] = 0\n\n        for (i in\
        \ 0 until m) {\n            val u = idMap[original[i]]!!\n            val v\
        \ = idMap[changed[i]]!!\n            dist[u][v] = minOf(dist[u][v], cost[i].toLong())\n\
        \        }\n\n        for (k in 0 until M) {\n            for (i in 0 until\
        \ M) {\n                for (j in 0 until M) {\n                    if (dist[i][k]\
        \ + dist[k][j] < dist[i][j]) {\n                        dist[i][j] = dist[i][k]\
        \ + dist[k][j]\n                    }\n                }\n            }\n  \
        \      }\n\n        val root = TrieNode()\n        for ((s, id) in idMap) {\n\
        \            var curr = root\n            for (c in s) {\n                val\
        \ idx = c - 'a'\n                if (curr.children[idx] == null) curr.children[idx]\
        \ = TrieNode()\n                curr = curr.children[idx]!!\n            }\n\
        \            curr.id = id\n        }\n\n        val sourceIds = Array(n) { mutableMapOf<Int,\
        \ Int>() }\n        val targetIds = Array(n) { mutableMapOf<Int, Int>() }\n\n\
        \        fun fillIds(str: String, targetArr: Array<MutableMap<Int, Int>>) {\n\
        \            for (i in 0 until n) {\n                var curr = root\n     \
        \           for (j in i until n) {\n                    val idx = str[j] - 'a'\n\
        \                    if (curr.children[idx] == null) break\n               \
        \     curr = curr.children[idx]!!\n                    if (curr.id != -1) targetArr[i][j\
        \ - i + 1] = curr.id\n                }\n            }\n        }\n\n      \
        \  fillIds(source, sourceIds)\n        fillIds(target, targetIds)\n\n      \
        \  val dp = LongArray(n + 1) { INF }\n        dp[0] = 0\n        val lens =\
        \ uniqueLens.toIntArray()\n\n        for (i in 0 until n) {\n            if\
        \ (dp[i] == INF) continue\n            if (source[i] == target[i]) dp[i + 1]\
        \ = minOf(dp[i + 1], dp[i])\n            for (len in lens) {\n             \
        \   if (i + len <= n) {\n                    val u = sourceIds[i][len] ?: -1\n\
        \                    val v = targetIds[i][len] ?: -1\n                    if\
        \ (u != -1 && v != -1 && dist[u][v] < INF) {\n                        dp[i +\
        \ len] = minOf(dp[i + len], dp[i] + dist[u][v])\n                    }\n   \
        \             }\n            }\n        }\n\n        return if (dp[n] >= INF)\
        \ -1 else dp[n]\n    }\n}"
      dart: "class TrieNode {\n  Map<int, TrieNode> children = {};\n  int id = -1;\n\
        }\n\nclass Solution {\n  int minimumCost(String source, String target, List<String>\
        \ original, List<String> changed, List<int> cost) {\n    final int n = source.length;\n\
        \    final int m = original.length;\n    final int INF = 1000000000000000;\n\
        \n    Map<String, int> idMap = {};\n    int idCounter = 0;\n    Set<int> uniqueLens\
        \ = {};\n\n    for (int i = 0; i < m; i++) {\n      if (!idMap.containsKey(original[i]))\
        \ idMap[original[i]] = idCounter++;\n      if (!idMap.containsKey(changed[i]))\
        \ idMap[changed[i]] = idCounter++;\n      uniqueLens.add(original[i].length);\n\
        \    }\n\n    int M = idCounter;\n    List<List<int>> dist = List.generate(M,\
        \ (_) => List.filled(M, INF));\n    for (int i = 0; i < M; i++) dist[i][i] =\
        \ 0;\n\n    for (int i = 0; i < m; i++) {\n      int u = idMap[original[i]]!;\n\
        \      int v = idMap[changed[i]]!;\n      if (cost[i] < dist[u][v]) dist[u][v]\
        \ = cost[i];\n    }\n\n    for (int k = 0; k < M; k++) {\n      for (int i =\
        \ 0; i < M; i++) {\n        for (int j = 0; j < M; j++) {\n          if (dist[i][k]\
        \ + dist[k][j] < dist[i][j]) {\n            dist[i][j] = dist[i][k] + dist[k][j];\n\
        \          }\n        }\n      }\n    }\n\n    TrieNode root = TrieNode();\n\
        \    idMap.forEach((s, id) {\n      TrieNode curr = root;\n      for (int j\
        \ = 0; j < s.length; j++) {\n        int charCode = s.codeUnitAt(j);\n     \
        \   if (!curr.children.containsKey(charCode)) curr.children[charCode] = TrieNode();\n\
        \        curr = curr.children[charCode]!;\n      }\n      curr.id = id;\n  \
        \  });\n\n    List<Map<int, int>> sourceIds = List.generate(n, (_) => {});\n\
        \    List<Map<int, int>> targetIds = List.generate(n, (_) => {});\n\n    void\
        \ fillIds(String str, List<Map<int, int>> targetArr) {\n      for (int i = 0;\
        \ i < n; i++) {\n        TrieNode curr = root;\n        for (int j = i; j <\
        \ n; j++) {\n          int charCode = str.codeUnitAt(j);\n          if (!curr.children.containsKey(charCode))\
        \ break;\n          curr = curr.children[charCode]!;\n          if (curr.id\
        \ != -1) targetArr[i][j - i + 1] = curr.id;\n        }\n      }\n    }\n\n \
        \   fillIds(source, sourceIds);\n    fillIds(target, targetIds);\n\n    List<int>\
        \ dp = List.filled(n + 1, INF);\n    dp[0] = 0;\n    List<int> lens = uniqueLens.toList();\n\
        \n    for (int i = 0; i < n; i++) {\n      if (dp[i] == INF) continue;\n   \
        \   if (source[i] == target[i]) dp[i + 1] = (dp[i + 1] < dp[i]) ? dp[i + 1]\
        \ : dp[i];\n      for (int len in lens) {\n        if (i + len <= n) {\n   \
        \       int? u = sourceIds[i][len];\n          int? v = targetIds[i][len];\n\
        \          if (u != null && v != null && dist[u][v] < INF) {\n            int\
        \ newCost = dp[i] + dist[u][v];\n            if (newCost < dp[i + len]) dp[i\
        \ + len] = newCost;\n          }\n        }\n      }\n    }\n\n    return dp[n]\
        \ >= INF ? -1 : dp[n];\n  }\n}"
      go: "func minimumCost(source string, target string, original []string, changed\
        \ []string, cost []int) int64 {\n    n := len(source)\n    m := len(original)\n\
        \    const INF int64 = 1e15\n\n    idMap := make(map[string]int)\n    idCounter\
        \ := 0\n    uniqueLensMap := make(map[int]bool)\n    for i := 0; i < m; i++\
        \ {\n        if _, ok := idMap[original[i]]; !ok { idMap[original[i]] = idCounter;\
        \ idCounter++ }\n        if _, ok := idMap[changed[i]]; !ok { idMap[changed[i]]\
        \ = idCounter; idCounter++ }\n        uniqueLensMap[len(original[i])] = true\n\
        \    }\n\n    M := idCounter\n    dist := make([][]int64, M)\n    for i := range\
        \ dist {\n        dist[i] = make([]int64, M)\n        for j := range dist[i]\
        \ { dist[i][j] = INF }\n        dist[i][i] = 0\n    }\n\n    for i := 0; i <\
        \ m; i++ {\n        u := idMap[original[i]]\n        v := idMap[changed[i]]\n\
        \        if int64(cost[i]) < dist[u][v] { dist[u][v] = int64(cost[i]) }\n  \
        \  }\n\n    for k := 0; k < M; k++ {\n        for i := 0; i < M; i++ {\n   \
        \         for j := 0; j < M; j++ {\n                if dist[i][k]+dist[k][j]\
        \ < dist[i][j] {\n                    dist[i][j] = dist[i][k] + dist[k][j]\n\
        \                }\n            }\n        }\n    }\n\n    type TrieNode struct\
        \ {\n        children [26]*TrieNode\n        id       int\n    }\n    root :=\
        \ &TrieNode{id: -1}\n    for s, id := range idMap {\n        curr := root\n\
        \        for i := 0; i < len(s); i++ {\n            idx := s[i] - 'a'\n    \
        \        if curr.children[idx] == nil { curr.children[idx] = &TrieNode{id: -1}\
        \ }\n            curr = curr.children[idx]\n        }\n        curr.id = id\n\
        \    }\n\n    sourceIds := make([]map[int]int, n)\n    targetIds := make([]map[int]int,\
        \ n)\n    for i := 0; i < n; i++ {\n        sourceIds[i] = make(map[int]int)\n\
        \        targetIds[i] = make(map[int]int)\n    }\n\n    fillIds := func(str\
        \ string, idsArr []map[int]int) {\n        for i := 0; i < n; i++ {\n      \
        \      curr := root\n            for j := i; j < n; j++ {\n                idx\
        \ := str[j] - 'a'\n                if curr.children[idx] == nil { break }\n\
        \                curr = curr.children[idx]\n                if curr.id != -1\
        \ { idsArr[i][j-i+1] = curr.id }\n            }\n        }\n    }\n    fillIds(source,\
        \ sourceIds)\n    fillIds(target, targetIds)\n\n    dp := make([]int64, n+1)\n\
        \    for i := range dp { dp[i] = INF }\n    dp[0] = 0\n    uniqueLens := make([]int,\
        \ 0, len(uniqueLensMap))\n    for l := range uniqueLensMap { uniqueLens = append(uniqueLens,\
        \ l) }\n\n    for i := 0; i < n; i++ {\n        if dp[i] == INF { continue }\n\
        \        if source[i] == target[i] {\n            if dp[i] < dp[i+1] { dp[i+1]\
        \ = dp[i] }\n        }\n        for _, l := range uniqueLens {\n           \
        \ if i+l <= n {\n                if u, okU := sourceIds[i][l]; okU {\n     \
        \               if v, okV := targetIds[i][l]; okV {\n                      \
        \  if dist[u][v] < INF {\n                            if dp[i]+dist[u][v] <\
        \ dp[i+l] { dp[i+l] = dp[i] + dist[u][v] }\n                        }\n    \
        \                }\n                }\n            }\n        }\n    }\n\n \
        \   if dp[n] >= INF { return -1 }\n    return dp[n]\n}"
      ruby: "def minimum_cost(source, target, original, changed, cost)\n  id_map = {}\n\
        \  id_count = 0\n  (original + changed).each do |s|\n    unless id_map.key?(s)\n\
        \      id_map[s] = id_count\n      id_count += 1\n    end\n  end\n\n  inf =\
        \ 10**15\n  dist = Array.new(id_count) { Array.new(id_count, inf) }\n  id_count.times\
        \ { |i| dist[i][i] = 0 }\n  original.each_with_index do |s, i|\n    u = id_map[s]\n\
        \    v = id_map[changed[i]]\n    dist[u][v] = [dist[u][v], cost[i]].min\n  end\n\
        \n  (0...id_count).each do |k|\n    (0...id_count).each do |i|\n      next if\
        \ dist[i][k] == inf\n      (0...id_count).each do |j|\n        next if dist[k][j]\
        \ == inf\n        if dist[i][k] + dist[k][j] < dist[i][j]\n          dist[i][j]\
        \ = dist[i][k] + dist[k][j]\n        end\n      end\n    end\n  end\n\n  n =\
        \ source.length\n  dp = Array.new(n + 1, inf)\n  dp[0] = 0\n  lengths = original.map(&:length).uniq\n\
        \n  (1..n).each do |i|\n    dp[i] = [dp[i], dp[i - 1]].min if source[i - 1]\
        \ == target[i - 1]\n    lengths.each do |len|\n      if i >= len\n        j\
        \ = i - len\n        if dp[j] < inf\n          u = id_map[source[j, len]]\n\
        \          v = id_map[target[j, len]]\n          if u && v && dist[u][v] < inf\n\
        \            dp[i] = [dp[i], dp[j] + dist[u][v]].min\n          end\n      \
        \  end\n      end\n    end\n  end\n\n  dp[n] >= inf ? -1 : dp[n]\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def minimumCost(source:\
        \ String, target: String, original: Array[String], changed: Array[String], cost:\
        \ Array[Int]): Long = {\n        val idMap = mutable.HashMap[String, Int]()\n\
        \        var idCount = 0\n        for (s <- original ++ changed) {\n       \
        \     if (!idMap.contains(s)) {\n                idMap(s) = idCount\n      \
        \          idCount += 1\n            }\n        }\n\n        val inf = 1000000000000000L\n\
        \        val dist = Array.fill(idCount, idCount)(inf)\n        for (i <- 0 until\
        \ idCount) dist(i)(i) = 0\n        for (i <- original.indices) {\n         \
        \   val u = idMap(original(i))\n            val v = idMap(changed(i))\n    \
        \        dist(u)(v) = Math.min(dist(u)(v), cost(i).toLong)\n        }\n\n  \
        \      for (k <- 0 until idCount; i <- 0 until idCount; j <- 0 until idCount)\
        \ {\n            if (dist(i)(k) != inf && dist(k)(j) != inf) {\n           \
        \     if (dist(i)(k) + dist(k)(j) < dist(i)(j)) {\n                    dist(i)(j)\
        \ = dist(i)(k) + dist(k)(j)\n                }\n            }\n        }\n\n\
        \        val n = source.length\n        val dp = Array.fill(n + 1)(inf)\n  \
        \      dp(0) = 0\n        val uniqueLengths = original.map(_.length).distinct\n\
        \n        for (i <- 1 to n) {\n            if (source(i - 1) == target(i - 1))\
        \ {\n                dp(i) = Math.min(dp(i), dp(i - 1))\n            }\n   \
        \         for (len <- uniqueLengths) {\n                if (i >= len) {\n  \
        \                  val j = i - len\n                    if (dp(j) < inf) {\n\
        \                        val srcSub = source.substring(j, i)\n             \
        \           val tgtSub = target.substring(j, i)\n                        (idMap.get(srcSub),\
        \ idMap.get(tgtSub)) match {\n                            case (Some(u), Some(v))\
        \ =>\n                                if (dist(u)(v) < inf) {\n            \
        \                        dp(i) = Math.min(dp(i), dp(j) + dist(u)(v))\n     \
        \                           }\n                            case _ =>\n     \
        \                   }\n                    }\n                }\n          \
        \  }\n        }\n\n        if (dp(n) >= inf) -1 else dp(n)\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_cost(source: String, target: String,\
        \ original: Vec<String>, changed: Vec<String>, cost: Vec<i32>) -> i64 {\n  \
        \      use std::collections::HashMap;\n        let mut id_map = HashMap::new();\n\
        \        let mut id_count = 0;\n        for s in original.iter().chain(changed.iter())\
        \ {\n            if !id_map.contains_key(s) {\n                id_map.insert(s.clone(),\
        \ id_count);\n                id_count += 1;\n            }\n        }\n\n \
        \       let inf: i64 = 1_000_000_000_000_000;\n        let mut dist = vec![vec![inf;\
        \ id_count]; id_count];\n        for i in 0..id_count { dist[i][i] = 0; }\n\
        \        for i in 0..original.len() {\n            let u = *id_map.get(&original[i]).unwrap();\n\
        \            let v = *id_map.get(&changed[i]).unwrap();\n            dist[u][v]\
        \ = dist[u][v].min(cost[i] as i64);\n        }\n\n        for k in 0..id_count\
        \ {\n            for i in 0..id_count {\n                if dist[i][k] == inf\
        \ { continue; }\n                for j in 0..id_count {\n                  \
        \  if dist[k][j] == inf { continue; }\n                    if dist[i][k] + dist[k][j]\
        \ < dist[i][j] {\n                        dist[i][j] = dist[i][k] + dist[k][j];\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    let n = source.len();\n        let mut dp = vec![inf; n + 1];\n       \
        \ dp[0] = 0;\n        let mut lengths: Vec<usize> = original.iter().map(|s|\
        \ s.len()).collect();\n        lengths.sort_unstable();\n        lengths.dedup();\n\
        \n        let s_bytes = source.as_bytes();\n        let t_bytes = target.as_bytes();\n\
        \n        for i in 1..=n {\n            if s_bytes[i - 1] == t_bytes[i - 1]\
        \ {\n                dp[i] = dp[i].min(dp[i - 1]);\n            }\n        \
        \    for &len in &lengths {\n                if i >= len {\n               \
        \     let j = i - len;\n                    if dp[j] != inf {\n            \
        \            let src_sub = &source[j..i];\n                        let tgt_sub\
        \ = &target[j..i];\n                        if let (Some(&u), Some(&v)) = (id_map.get(src_sub),\
        \ id_map.get(tgt_sub)) {\n                            if dist[u][v] != inf {\n\
        \                                dp[i] = dp[i].min(dp[j] + dist[u][v]);\n  \
        \                          }\n                        }\n                  \
        \  }\n                }\n            }\n        }\n\n        if dp[n] >= inf\
        \ { -1 } else { dp[n] }\n    }\n}"
      racket: "(require racket/list)\n\n(define/contract (minimum-cost source target\
        \ original changed cost)\n  (-> string? string? (listof string?) (listof string?)\
        \ (listof exact-integer?) exact-integer?)\n  (let* ([id-map (make-hash)]\n \
        \        [id-count 0])\n    (for ([s (append original changed)])\n      (unless\
        \ (hash-has-key? id-map s)\n        (hash-set! id-map s id-count)\n        (set!\
        \ id-count (+ id-count 1))))\n    (let ([inf 1000000000000000]\n          [dist\
        \ (make-vector id-count)])\n      (for ([i id-count])\n        (vector-set!\
        \ dist i (make-vector id-count inf))\n        (vector-set! (vector-ref dist\
        \ i) i 0))\n      (for ([s original] [c changed] [co cost])\n        (let ([u\
        \ (hash-ref id-map s)]\n              [v (hash-ref id-map c)])\n          (vector-set!\
        \ (vector-ref dist u) v (min (vector-ref (vector-ref dist u) v) co))))\n   \
        \   (for ([k id-count])\n        (for ([i id-count])\n          (let ([dik (vector-ref\
        \ (vector-ref dist i) k)])\n            (when (< dik inf)\n              (for\
        \ ([j id-count])\n                (let ([dkj (vector-ref (vector-ref dist k)\
        \ j)])\n                  (when (< dkj inf)\n                    (let ([dij\
        \ (vector-ref (vector-ref dist i) j)])\n                      (when (> dij (+\
        \ dik dkj))\n                        (vector-set! (vector-ref dist i) j (+ dik\
        \ dkj)))))))))))\n      (let* ([n (string-length source)]\n             [dp\
        \ (make-vector (+ n 1) inf)]\n             [lengths (remove-duplicates (map\
        \ string-length original))])\n        (vector-set! dp 0 0)\n        (for ([i\
        \ (in-range 1 (+ n 1))])\n          (when (char=? (string-ref source (- i 1))\
        \ (string-ref target (- i 1)))\n            (vector-set! dp i (min (vector-ref\
        \ dp i) (vector-ref dp (- i 1)))))\n          (for ([len lengths])\n       \
        \     (when (>= i len)\n              (let* ([j (- i len)]\n               \
        \      [dpj (vector-ref dp j)])\n                (when (< dpj inf)\n       \
        \           (let* ([src-sub (substring source j i)]\n                      \
        \   [tgt-sub (substring target j i)]\n                         [u (hash-ref\
        \ id-map src-sub #f)]\n                         [v (hash-ref id-map tgt-sub\
        \ #f)])\n                    (when (and u v)\n                      (let ([duv\
        \ (vector-ref (vector-ref dist u) v)])\n                        (when (< duv\
        \ inf)\n                          (vector-set! dp i (min (vector-ref dp i) (+\
        \ dpj duv))))))))))))\n        (let ([ans (vector-ref dp n)])\n          (if\
        \ (>= ans inf) -1 ans))))))"
      erlang: "minimum_cost(Source, Target, Original, Changed, Cost) ->\n    AllStrings\
        \ = lists:usort(Original ++ Changed),\n    IDMap = maps:from_list(lists:zip(AllStrings,\
        \ lists:seq(0, length(AllStrings) - 1))),\n    IDCount = maps:size(IDMap),\n\
        \    INF = 1000000000000000,\n    Dist0 = maps:from_list([{{I, I}, 0} || I <-\
        \ lists:seq(0, IDCount - 1)]),\n    Zip1 = lists:zip(Original, Changed),\n \
        \   Zip2 = lists:zip(Zip1, Cost),\n    Dist1 = lists:foldl(fun({{S, C}, Co},\
        \ Acc) ->\n        U = maps:get(S, IDMap),\n        V = maps:get(C, IDMap),\n\
        \        Old = maps:get({U, V}, Acc, INF),\n        Acc#{{U, V} => min(Old,\
        \ Co)}\n    end, Dist0, Zip2),\n    FinalDist = lists:foldl(fun(K, Dk) ->\n\
        \        IList = [{I, maps:get({I, K}, Dk)} || I <- lists:seq(0, IDCount - 1),\
        \ maps:is_key({I, K}, Dk)],\n        JList = [{J, maps:get({K, J}, Dk)} || J\
        \ <- lists:seq(0, IDCount - 1), maps:is_key({K, J}, Dk)],\n        lists:foldl(fun({I,\
        \ DIK}, AccI) ->\n            lists:foldl(fun({J, DKJ}, AccJ) ->\n         \
        \       NewVal = DIK + DKJ,\n                Existing = maps:get({I, J}, AccJ,\
        \ INF),\n                if NewVal < Existing -> AccJ#{{I, J} => NewVal}; true\
        \ -> AccJ end\n            end, AccI, JList)\n        end, Dk, IList)\n    end,\
        \ Dist1, lists:seq(0, IDCount - 1)),\n    N = byte_size(Source),\n    Lengths\
        \ = lists:usort([byte_size(S) || S <- Original]),\n    DP = lists:foldl(fun(I,\
        \ AccDP) ->\n        CharMatch = (binary_part(Source, I - 1, 1) == binary_part(Target,\
        \ I - 1, 1)),\n        Res0 = if CharMatch -> maps:get(I - 1, AccDP, INF); true\
        \ -> INF end,\n        ResFinal = lists:foldl(fun(Len, MinCost) ->\n       \
        \     if I >= Len ->\n                J = I - Len,\n                case maps:get(J,\
        \ AccDP, INF) of\n                    DPJ when DPJ < INF ->\n              \
        \          SrcSub = binary_part(Source, J, Len),\n                        TgtSub\
        \ = binary_part(Target, J, Len),\n                        case {maps:find(SrcSub,\
        \ IDMap), maps:find(TgtSub, IDMap)} of\n                            {{ok, U},\
        \ {ok, V}} ->\n                                case maps:find({U, V}, FinalDist)\
        \ of\n                                    {ok, DUV} -> min(MinCost, DPJ + DUV);\n\
        \                                    error -> MinCost\n                    \
        \            end;\n                            _ -> MinCost\n              \
        \          end;\n                    _ -> MinCost\n                end;\n  \
        \          true -> MinCost\n            end\n        end, Res0, Lengths),\n\
        \        AccDP#{I => ResFinal}\n    end, #{0 => 0}, lists:seq(1, N)),\n    Ans\
        \ = maps:get(N, DP, INF),\n    if Ans >= INF -> -1; true -> Ans end."
      elixir: "defmodule Solution do\n  @spec minimum_cost(source :: String.t, target\
        \ :: String.t, original :: [String.t], changed :: [String.t], cost :: [integer])\
        \ :: integer\n  def minimum_cost(source, target, original, changed, cost) do\n\
        \    id_list = Enum.uniq(original ++ changed)\n    id_map = Enum.with_index(id_list)\
        \ |> Enum.into(%{})\n    id_count = map_size(id_map)\n    inf = 1_000_000_000_000_000\n\
        \    dist0 = Enum.reduce(0..id_count-1, %{}, fn i, acc -> Map.put(acc, {i, i},\
        \ 0) end)\n    dist1 = Enum.zip([original, changed, cost])\n      |> Enum.reduce(dist0,\
        \ fn {s, c, co}, acc ->\n        u = Map.get(id_map, s)\n        v = Map.get(id_map,\
        \ c)\n        Map.put(acc, {u, v}, min(Map.get(acc, {u, v}, inf), co))\n   \
        \   end)\n    final_dist = Enum.reduce(0..id_count-1, dist1, fn k, dk ->\n \
        \     i_list = for i <- 0..id_count-1, dik = Map.get(dk, {i, k}, inf), dik <\
        \ inf, do: {i, dik}\n      j_list = for j <- 0..id_count-1, dkj = Map.get(dk,\
        \ {k, j}, inf), dkj < inf, do: {j, dkj}\n      Enum.reduce(i_list, dk, fn {i,\
        \ dik}, acc_i ->\n        Enum.reduce(j_list, acc_i, fn {j, dkj}, acc_j ->\n\
        \          new_val = dik + dkj\n          if new_val < Map.get(acc_j, {i, j},\
        \ inf) do\n            Map.put(acc_j, {i, j}, new_val)\n          else\n   \
        \         acc_j\n          end\n        end)\n      end)\n    end)\n    n =\
        \ byte_size(source)\n    unique_lengths = Enum.map(original, &byte_size/1) |>\
        \ Enum.uniq()\n    dp = Enum.reduce(1..n, %{0 => 0}, fn i, acc_dp ->\n     \
        \ res0 = if binary_part(source, i - 1, 1) == binary_part(target, i - 1, 1),\
        \ do: Map.get(acc_dp, i - 1, inf), else: inf\n      res_final = Enum.reduce(unique_lengths,\
        \ res0, fn len, min_val ->\n        if i >= len do\n          j = i - len\n\
        \          dp_j = Map.get(acc_dp, j, inf)\n          if dp_j < inf do\n    \
        \        src_sub = binary_part(source, j, len)\n            tgt_sub = binary_part(target,\
        \ j, len)\n            u = Map.get(id_map, src_sub)\n            v = Map.get(id_map,\
        \ tgt_sub)\n            if u != nil and v != nil do\n              duv = Map.get(final_dist,\
        \ {u, v}, inf)\n              min(min_val, dp_j + duv)\n            else\n \
        \             min_val\n            end\n          else\n            min_val\n\
        \          end\n        else\n          min_val\n        end\n      end)\n \
        \     Map.put(acc_dp, i, res_final)\n    end)\n    ans = Map.get(dp, n, inf)\n\
        \    if ans >= inf, do: -1, else: ans\n  end\nend"
    approach: The algorithm combines the Floyd-Warshall algorithm with dynamic programming.
      First, we identify all unique strings in the `original` and `changed` arrays and
      map them to integer IDs. We then initialize a distance matrix with the given costs
      and use Floyd-Warshall to compute the minimum cost to transform any string in
      our set to any other string. This step handles the 'identical indices' constraint
      by effectively combining any sequence of operations that act on the same substring
      index range into a single minimal cost.
    time_complexity: O(M^3 + N^2) or O(M^3 + N \cdot M \cdot L), where M is the number
      of transformation rules, N is the length of the source string, and L is the max
      rule length. Floyd-Warshall takes O(M^3) for M up to 200, and the DP with Trie
      traversal or hash lookup takes O(N^2) or O(N \cdot M \cdot L).
    space_complexity: O(M^2 + M \cdot L + N), where M^2 is for the distance matrix,
      M \cdot L is for the Trie or string hash map, and N is for the DP array. This
      fits within the 256MB limit easily.
    elapsed_time: 513.3863697052002
    model: gemini-3-flash-preview
    generated_at: '2026-01-30 01:28:49 '
---

## Problem #2977: Minimum Cost to Convert String II

**Difficulty:** Hard

**Topics:** Array, String, Dynamic Programming, Graph Theory, Trie, Shortest Path

## Problem Description

<p>You are given two <strong>0-indexed</strong> strings <code>source</code> and <code>target</code>, both of length <code>n</code> and consisting of <strong>lowercase</strong> English characters. You are also given two <strong>0-indexed</strong> string arrays <code>original</code> and <code>changed</code>, and an integer array <code>cost</code>, where <code>cost[i]</code> represents the cost of converting the string <code>original[i]</code> to the string <code>changed[i]</code>.</p>

<p>You start with the string <code>source</code>. In one operation, you can pick a <strong>substring</strong> <code>x</code> from the string, and change it to <code>y</code> at a cost of <code>z</code> <strong>if</strong> there exists <strong>any</strong> index <code>j</code> such that <code>cost[j] == z</code>, <code>original[j] == x</code>, and <code>changed[j] == y</code>. You are allowed to do <strong>any</strong> number of operations, but any pair of operations must satisfy <strong>either</strong> of these two conditions:</p>

<ul>
	<li>The substrings picked in the operations are <code>source[a..b]</code> and <code>source[c..d]</code> with either <code>b &lt; c</code> <strong>or</strong> <code>d &lt; a</code>. In other words, the indices picked in both operations are <strong>disjoint</strong>.</li>
	<li>The substrings picked in the operations are <code>source[a..b]</code> and <code>source[c..d]</code> with <code>a == c</code> <strong>and</strong> <code>b == d</code>. In other words, the indices picked in both operations are <strong>identical</strong>.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> cost to convert the string </em><code>source</code><em> to the string </em><code>target</code><em> using <strong>any</strong> number of operations</em>. <em>If it is impossible to convert</em> <code>source</code> <em>to</em> <code>target</code>,<em> return</em> <code>-1</code>.</p>

<p><strong>Note</strong> that there may exist indices <code>i</code>, <code>j</code> such that <code>original[j] == original[i]</code> and <code>changed[j] == changed[i]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abcd&quot;, target = &quot;acbe&quot;, original = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;e&quot;,&quot;d&quot;], changed = [&quot;b&quot;,&quot;c&quot;,&quot;b&quot;,&quot;e&quot;,&quot;b&quot;,&quot;e&quot;], cost = [2,5,5,1,2,20]
<strong>Output:</strong> 28
<strong>Explanation:</strong> To convert &quot;abcd&quot; to &quot;acbe&quot;, do the following operations:
- Change substring source[1..1] from &quot;b&quot; to &quot;c&quot; at a cost of 5.
- Change substring source[2..2] from &quot;c&quot; to &quot;e&quot; at a cost of 1.
- Change substring source[2..2] from &quot;e&quot; to &quot;b&quot; at a cost of 2.
- Change substring source[3..3] from &quot;d&quot; to &quot;e&quot; at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28. 
It can be shown that this is the minimum possible cost.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abcdefgh&quot;, target = &quot;acdeeghh&quot;, original = [&quot;bcd&quot;,&quot;fgh&quot;,&quot;thh&quot;], changed = [&quot;cde&quot;,&quot;thh&quot;,&quot;ghh&quot;], cost = [1,3,5]
<strong>Output:</strong> 9
<strong>Explanation:</strong> To convert &quot;abcdefgh&quot; to &quot;acdeeghh&quot;, do the following operations:
- Change substring source[1..3] from &quot;bcd&quot; to &quot;cde&quot; at a cost of 1.
- Change substring source[5..7] from &quot;fgh&quot; to &quot;thh&quot; at a cost of 3. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation.
- Change substring source[5..7] from &quot;thh&quot; to &quot;ghh&quot; at a cost of 5. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
The total cost incurred is 1 + 3 + 5 = 9.
It can be shown that this is the minimum possible cost.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abcdefgh&quot;, target = &quot;addddddd&quot;, original = [&quot;bcd&quot;,&quot;defgh&quot;], changed = [&quot;ddd&quot;,&quot;ddddd&quot;], cost = [100,1578]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is impossible to convert &quot;abcdefgh&quot; to &quot;addddddd&quot;.
If you select substring source[1..3] as the first operation to change &quot;abcdefgh&quot; to &quot;adddefgh&quot;, you cannot select substring source[3..7] as the second operation because it has a common index, 3, with the first operation.
If you select substring source[3..7] as the first operation to change &quot;abcdefgh&quot; to &quot;abcddddd&quot;, you cannot select substring source[1..3] as the second operation because it has a common index, 3, with the first operation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= source.length == target.length &lt;= 1000</code></li>
	<li><code>source</code>, <code>target</code> consist only of lowercase English characters.</li>
	<li><code>1 &lt;= cost.length == original.length == changed.length &lt;= 100</code></li>
	<li><code>1 &lt;= original[i].length == changed[i].length &lt;= source.length</code></li>
	<li><code>original[i]</code>, <code>changed[i]</code> consist only of lowercase English characters.</li>
	<li><code>original[i] != changed[i]</code></li>
	<li><code>1 &lt;= cost[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Give each unique string in `original` and `changed` arrays a unique id. There are at most `2 * m` unique strings in total where `m` is the length of the arrays. We can put them into a hash map to assign ids.

2. We can pre-compute the smallest costs between all pairs of unique strings using Floyd Warshall algorithm in `O(m ^ 3)` time complexity.

3. Let `dp[i]` be the smallest cost to change the first `i` characters (prefix) of `source` into `target`, leaving the suffix untouched.
We have `dp[0] = 0`.
dp[i] = min(
dp[i - 1] if (source[i - 1] == target[i - 1]),
dp[j-1] + cost[x][y] where x is the id of source[j..(i - 1)] and y is the id of target e[j..(i - 1)])
).
If neither of the two conditions is satisfied, `dp[i] = infinity`.

4. We can use Trie to check for the second condition in `O(1)`.

5. The answer is `dp[n]` where `n` is `source.length`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm combines the Floyd-Warshall algorithm with dynamic programming. First, we identify all unique strings in the `original` and `changed` arrays and map them to integer IDs. We then initialize a distance matrix with the given costs and use Floyd-Warshall to compute the minimum cost to transform any string in our set to any other string. This step handles the 'identical indices' constraint by effectively combining any sequence of operations that act on the same substring index range into a single minimal cost.

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
    long long minimumCost(string source, string target, vector<string>& original, vector<string>& changed, vector<int>& cost) {
        unordered_map<string, int> id_map;
        int id_cnt = 0;
        auto get_id = [&](const string& s) {
            if (id_map.find(s) == id_map.end()) id_map[s] = id_cnt++;
            return id_map[s];
        };
        for (const string& s : original) get_id(s);
        for (const string& s : changed) get_id(s);

        long long INF = 1e15;
        vector<vector<long long>> dist(id_cnt, vector<long long>(id_cnt, INF));
        for (int i = 0; i < id_cnt; ++i) dist[i][i] = 0;
        for (int i = 0; i < original.size(); ++i) {
            int u = id_map[original[i]], v = id_map[changed[i]];
            dist[u][v] = min(dist[u][v], (long long)cost[i]);
        }

        for (int k = 0; k < id_cnt; ++k) {
            for (int i = 0; i < id_cnt; ++i) {
                if (dist[i][k] == INF) continue;
                for (int j = 0; j < id_cnt; ++j) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        int n = source.length();
        set<int> unique_lengths;
        for (const string& s : original) unique_lengths.insert(s.length());

        vector<long long> dp(n + 1, INF);
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            if (dp[i] == INF) continue;
            if (source[i] == target[i]) dp[i + 1] = min(dp[i + 1], dp[i]);
            for (int L : unique_lengths) {
                if (i + L <= n) {
                    string sub_s = source.substr(i, L);
                    string sub_t = target.substr(i, L);
                    if (id_map.count(sub_s) && id_map.count(sub_t)) {
                        int u = id_map[sub_s], v = id_map[sub_t];
                        if (dist[u][v] < INF) dp[i + L] = min(dp[i + L], dp[i] + dist[u][v]);
                    }
                }
            }
        }
        return dp[n] >= INF ? -1 : dp[n];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long minimumCost(String source, String target, String[] original, String[] changed, int[] cost) {
        Map<String, Integer> idMap = new HashMap<>();
        int idCnt = 0;
        for (String s : original) if (!idMap.containsKey(s)) idMap.put(s, idCnt++);
        for (String s : changed) if (!idMap.containsKey(s)) idMap.put(s, idCnt++);

        long INF = 1_000_000_000_000_000L;
        long[][] dist = new long[idCnt][idCnt];
        for (int i = 0; i < idCnt; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }

        for (int i = 0; i < original.length; i++) {
            int u = idMap.get(original[i]), v = idMap.get(changed[i]);
            dist[u][v] = Math.min(dist[u][v], (long) cost[i]);
        }

        for (int k = 0; k < idCnt; k++) {
            for (int i = 0; i < idCnt; i++) {
                if (dist[i][k] == INF) continue;
                for (int j = 0; j < idCnt; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        int n = source.length();
        Set<Integer> uniqueLengths = new HashSet<>();
        for (String s : original) uniqueLengths.add(s.length());

        long[] dp = new long[n + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            if (dp[i] == INF) continue;
            if (source.charAt(i) == target.charAt(i)) dp[i + 1] = Math.min(dp[i + 1], dp[i]);
            for (int L : uniqueLengths) {
                if (i + L <= n) {
                    String subS = source.substring(i, i + L);
                    String subT = target.substring(i, i + L);
                    if (idMap.containsKey(subS) && idMap.containsKey(subT)) {
                        int u = idMap.get(subS), v = idMap.get(subT);
                        if (dist[u][v] < INF) dp[i + L] = Math.min(dp[i + L], dp[i] + dist[u][v]);
                    }
                }
            }
        }
        return dp[n] >= INF ? -1 : dp[n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        id_map = {}
        id_cnt = 0
        for s in original + changed:
            if s not in id_map:
                id_map[s] = id_cnt
                id_cnt += 1

        INF = float('inf')
        dist = [[INF] * id_cnt for _ in range(id_cnt)]
        for i in range(id_cnt): dist[i][i] = 0

        for i in range(len(original)):
            u, v = id_map[original[i]], id_map[changed[i]]
            dist[u][v] = min(dist[u][v], cost[i])

        for k in range(id_cnt):
            for i in range(id_cnt):
                if dist[i][k] == INF: continue
                for j in range(id_cnt):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        n = len(source)
        unique_lengths = sorted(list(set(len(s) for s in original)))
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF: continue
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            for L in unique_lengths:
                if i + L <= n:
                    sub_s = source[i:i+L]
                    sub_t = target[i:i+L]
                    if sub_s in id_map and sub_t in id_map:
                        u, v = id_map[sub_s], id_map[sub_t]
                        if dist[u][v] < INF:
                            dp[i+L] = min(dp[i+L], dp[i] + dist[u][v])

        return int(dp[n]) if dp[n] < INF else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        id_map = {}
        id_cnt = 0
        for s in original + changed:
            if s not in id_map:
                id_map[s] = id_cnt
                id_cnt += 1

        INF = float('inf')
        dist = [[INF] * id_cnt for _ in range(id_cnt)]
        for i in range(id_cnt): dist[i][i] = 0

        for i in range(len(original)):
            u, v = id_map[original[i]], id_map[changed[i]]
            dist[u][v] = min(dist[u][v], cost[i])

        for k in range(id_cnt):
            for i in range(id_cnt):
                if dist[i][k] == INF: continue
                for j in range(id_cnt):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        n = len(source)
        unique_lengths = sorted(list(set(len(s) for s in original)))
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF: continue
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            for L in unique_lengths:
                if i + L <= n:
                    sub_s = source[i:i+L]
                    sub_t = target[i:i+L]
                    if sub_s in id_map and sub_t in id_map:
                        u, v = id_map[sub_s], id_map[sub_t]
                        if dist[u][v] < INF:
                            dp[i+L] = min(dp[i+L], dp[i] + dist[u][v])

        return int(dp[n]) if dp[n] < INF else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define INF 1e15

typedef struct {
    int children[26];
    int id;
} TrieNode;

static TrieNode trie[200005];
static int nodes_cnt;

void reset_trie() {
    for (int i = 0; i < nodes_cnt; ++i) {
        for (int j = 0; j < 26; ++j) trie[i].children[j] = 0;
        trie[i].id = -1;
    }
    nodes_cnt = 1;
    trie[0].id = -1;
}

int insert_trie(const char* s, int* id_gen) {
    int curr = 0;
    for (int i = 0; s[i]; ++i) {
        int c = s[i] - 'a';
        if (!trie[curr].children[c]) {
            for (int j = 0; j < 26; j++) trie[nodes_cnt].children[j] = 0;
            trie[nodes_cnt].id = -1;
            trie[curr].children[c] = nodes_cnt++;
        }
        curr = trie[curr].children[c];
    }
    if (trie[curr].id == -1) trie[curr].id = (*id_gen)++;
    return trie[curr].id;
}

long long minimumCost(char* source, char* target, char** original, int originalSize, char** changed, int changedSize, int* cost, int costSize) {
    reset_trie();
    int id_gen = 0;
    long long dist[205][205];
    for (int i = 0; i < 205; i++) {
        for (int j = 0; j < 205; j++) dist[i][j] = (i == j ? 0 : INF);
    }
    for (int i = 0; i < originalSize; i++) {
        int u = insert_trie(original[i], &id_gen);
        int v = insert_trie(changed[i], &id_gen);
        if (cost[i] < dist[u][v]) dist[u][v] = cost[i];
    }
    for (int k = 0; k < id_gen; k++) {
        for (int i = 0; i < id_gen; i++) {
            if (dist[i][k] == INF) continue;
            for (int j = 0; j < id_gen; j++) {
                if (dist[k][j] < INF && dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }
    int n = strlen(source);
    long long* dp = malloc(sizeof(long long) * (n + 1));
    for (int i = 0; i <= n; i++) dp[i] = INF;
    dp[0] = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i] == INF) continue;
        if (source[i] == target[i]) if (dp[i] < dp[i+1]) dp[i+1] = dp[i];
        int s_node = 0, t_node = 0;
        for (int L = 1; i + L <= n; L++) {
            int cs = source[i+L-1] - 'a', ct = target[i+L-1] - 'a';
            s_node = (s_node != -1 && trie[s_node].children[cs]) ? trie[s_node].children[cs] : -1;
            t_node = (t_node != -1 && trie[t_node].children[ct]) ? trie[t_node].children[ct] : -1;
            if (s_node == -1 && t_node == -1) break;
            if (s_node != -1 && t_node != -1 && trie[s_node].id != -1 && trie[t_node].id != -1) {
                int u = trie[s_node].id, v = trie[t_node].id;
                if (dist[u][v] < INF && dp[i] + dist[u][v] < dp[i+L]) dp[i+L] = dp[i] + dist[u][v];
            }
        }
    }
    long long res = (dp[n] >= INF ? -1 : dp[n]);
    free(dp);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MinimumCost(string source, string target, string[] original, string[] changed, int[] cost) {
        var idMap = new Dictionary<string, int>();
        int idCnt = 0;
        int GetId(string s) {
            if (!idMap.ContainsKey(s)) idMap[s] = idCnt++;
            return idMap[s];
        }
        for (int i = 0; i < original.Length; i++) {
            GetId(original[i]);
            GetId(changed[i]);
        }
        long INF = 1_000_000_000_000_000L;
        long[,] dist = new long[idCnt, idCnt];
        for (int i = 0; i < idCnt; i++) {
            for (int j = 0; j < idCnt; j++) dist[i, j] = (i == j ? 0 : INF);
        }
        for (int i = 0; i < original.Length; i++) {
            int u = idMap[original[i]], v = idMap[changed[i]];
            dist[u, v] = Math.Min(dist[u, v], (long)cost[i]);
        }
        for (int k = 0; k < idCnt; k++) {
            for (int i = 0; i < idCnt; i++) {
                if (dist[i, k] == INF) continue;
                for (int j = 0; j < idCnt; j++) {
                    dist[i, j] = Math.Min(dist[i, j], dist[i, k] + dist[k, j]);
                }
            }
        }
        int n = source.Length;
        var uniqueLengths = original.Select(s => s.Length).Distinct().ToList();
        long[] dp = new long[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = INF;
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == INF) continue;
            if (source[i] == target[i]) dp[i + 1] = Math.Min(dp[i + 1], dp[i]);
            foreach (int L in uniqueLengths) {
                if (i + L <= n) {
                    string subS = source.Substring(i, L);
                    string subT = target.Substring(i, L);
                    if (idMap.ContainsKey(subS) && idMap.ContainsKey(subT)) {
                        int u = idMap[subS], v = idMap[subT];
                        if (dist[u, v] < INF) dp[i + L] = Math.Min(dp[i + L], dp[i] + dist[u, v]);
                    }
                }
            }
        }
        return dp[n] >= INF ? -1 : dp[n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} source
 * @param {string} target
 * @param {string[]} original
 * @param {string[]} changed
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(source, target, original, changed, cost) {
    const idMap = new Map();
    let idCnt = 0;
    const getId = (s) => {
        if (!idMap.has(s)) idMap.set(s, idCnt++);
        return idMap.get(s);
    };
    for (const s of original) getId(s);
    for (const s of changed) getId(s);

    const INF = 1e15;
    const dist = Array.from({ length: idCnt }, () => Array(idCnt).fill(INF));
    for (let i = 0; i < idCnt; i++) dist[i][i] = 0;
    for (let i = 0; i < original.length; i++) {
        const u = idMap.get(original[i]), v = idMap.get(changed[i]);
        dist[u][v] = Math.min(dist[u][v], cost[i]);
    }

    for (let k = 0; k < idCnt; k++) {
        for (let i = 0; i < idCnt; i++) {
            if (dist[i][k] === INF) continue;
            for (let j = 0; j < idCnt; j++) {
                dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    const n = source.length;
    const uniqueLengths = [...new Set(original.map(s => s.length))];
    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;

    for (let i = 0; i < n; i++) {
        if (dp[i] === INF) continue;
        if (source[i] === target[i]) dp[i + 1] = Math.min(dp[i + 1], dp[i]);
        for (const L of uniqueLengths) {
            if (i + L <= n) {
                const subS = source.substring(i, i + L);
                const subT = target.substring(i, i + L);
                if (idMap.has(subS) && idMap.has(subT)) {
                    const u = idMap.get(subS), v = idMap.get(subT);
                    if (dist[u][v] < INF) dp[i + L] = Math.min(dp[i + L], dp[i] + dist[u][v]);
                }
            }
        }
    }

    return dp[n] >= INF ? -1 : dp[n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumCost(source: string, target: string, original: string[], changed: string[], cost: number[]): number {
    const n = source.length;
    const m = original.length;
    const INF = 1e15;

    const idMap = new Map<string, number>();
    let idCounter = 0;
    const getID = (s: string) => {
        if (!idMap.has(s)) idMap.set(s, idCounter++);
        return idMap.get(s)!;
    };

    for (let i = 0; i < m; i++) {
        getID(original[i]);
        getID(changed[i]);
    }

    const M = idCounter;
    const dist = Array.from({ length: M }, () => new Float64Array(M).fill(INF));
    for (let i = 0; i < M; i++) dist[i][i] = 0;

    for (let i = 0; i < m; i++) {
        const u = getID(original[i]);
        const v = getID(changed[i]);
        dist[u][v] = Math.min(dist[u][v], cost[i]);
    }

    for (let k = 0; k < M; k++) {
        for (let i = 0; i < M; i++) {
            for (let j = 0; j < M; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    class TrieNode {
        children: { [key: string]: TrieNode } = {};
        id: number = -1;
    }

    const root = new TrieNode();
    for (const [s, id] of idMap.entries()) {
        let curr = root;
        for (const char of s) {
            if (!curr.children[char]) curr.children[char] = new TrieNode();
            curr = curr.children[char];
        }
        curr.id = id;
    }

    const sourceIds = Array.from({ length: n }, () => new Int32Array(n + 1).fill(-1));
    const targetIds = Array.from({ length: n }, () => new Int32Array(n + 1).fill(-1));

    const fillIds = (str: string, targetArr: Int32Array[]) => {
        for (let i = 0; i < n; i++) {
            let curr = root;
            for (let j = i; j < n; j++) {
                if (!curr.children[str[j]]) break;
                curr = curr.children[str[j]];
                if (curr.id !== -1) targetArr[i][j - i + 1] = curr.id;
            }
        }
    };

    fillIds(source, sourceIds);
    fillIds(target, targetIds);

    const uniqueLens = Array.from(new Set(original.map(s => s.length)));
    const dp = new Float64Array(n + 1).fill(INF);
    dp[0] = 0;

    for (let i = 0; i < n; i++) {
        if (dp[i] === INF) continue;
        if (source[i] === target[i]) dp[i + 1] = Math.min(dp[i + 1], dp[i]);
        for (const len of uniqueLens) {
            if (i + len <= n) {
                const u = sourceIds[i][len];
                const v = targetIds[i][len];
                if (u !== -1 && v !== -1 && dist[u][v] < INF) {
                    dp[i + len] = Math.min(dp[i + len], dp[i] + dist[u][v]);
                }
            }
        }
    }

    return dp[n] >= INF ? -1 : dp[n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minimumCost($source, $target, $original, $changed, $cost) {
        $n = strlen($source);
        $m = count($original);
        $INF = 1e15;
        $idMap = [];
        $idCounter = 0;
        $uniqueLens = [];

        for ($i = 0; $i < $m; $i++) {
            if (!isset($idMap[$original[$i]])) $idMap[$original[$i]] = $idCounter++;
            if (!isset($idMap[$changed[$i]])) $idMap[$changed[$i]] = $idCounter++;
            $uniqueLens[strlen($original[$i])] = true;
        }

        $M = $idCounter;
        $dist = array_fill(0, $M, array_fill(0, $M, $INF));
        for ($i = 0; $i < $M; $i++) $dist[$i][$i] = 0;

        for ($i = 0; $i < $m; $i++) {
            $u = $idMap[$original[$i]];
            $v = $idMap[$changed[$i]];
            $dist[$u][$v] = min($dist[$u][$v], $cost[$i]);
        }

        for ($k = 0; $k < $M; $k++) {
            for ($i = 0; $i < $M; $i++) {
                for ($j = 0; $j < $M; $j++) {
                    if ($dist[$i][$k] + $dist[$k][$j] < $dist[$i][$j]) {
                        $dist[$i][$j] = $dist[$i][$k] + $dist[$k][$j];
                    }
                }
            }
        }

        $root = ['children' => [], 'id' => -1];
        foreach ($idMap as $s => $id) {
            $curr = &$root;
            for ($j = 0; $j < strlen($s); $j++) {
                if (!isset($curr['children'][$s[$j]])) $curr['children'][$s[$j]] = ['children' => [], 'id' => -1];
                $curr = &$curr['children'][$s[$j]];
            }
            $curr['id'] = $id;
        }

        $sourceIds = array_fill(0, $n, []);
        $targetIds = array_fill(0, $n, []);

        $fillIds = function($str, &$targetArr, $n, $root) {
            for ($i = 0; $i < $n; $i++) {
                $curr = $root;
                for ($j = $i; $j < $n; $j++) {
                    if (!isset($curr['children'][$str[$j]])) break;
                    $curr = $curr['children'][$str[$j]];
                    if ($curr['id'] !== -1) $targetArr[$i][$j - $i + 1] = $curr['id'];
                }
            }
        };

        $fillIds($source, $sourceIds, $n, $root);
        $fillIds($target, $targetIds, $n, $root);

        $dp = array_fill(0, $n + 1, $INF);
        $dp[0] = 0;
        $lens = array_keys($uniqueLens);

        for ($i = 0; $i < $n; $i++) {
            if ($dp[$i] >= $INF) continue;
            if ($source[$i] === $target[$i]) $dp[$i+1] = min($dp[$i+1], $dp[$i]);
            foreach ($lens as $len) {
                if ($i + $len <= $n) {
                    if (isset($sourceIds[$i][$len]) && isset($targetIds[$i][$len])) {
                        $u = $sourceIds[$i][$len];
                        $v = $targetIds[$i][$len];
                        if ($dist[$u][$v] < $INF) {
                            $dp[$i + $len] = min($dp[$i + $len], $dp[$i] + $dist[$u][$v]);
                        }
                    }
                }
            }
        }

        return $dp[$n] >= $INF ? -1 : $dp[$n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    class TrieNode {
        var children = [Character: TrieNode]()
        var id: Int = -1
    }

    func minimumCost(_ source: String, _ target: String, _ original: [String], _ changed: [String], _ cost: [Int]) -> Int {
        let n = source.count
        let m = original.count
        let INF = 1_000_000_000_000_000

        var idMap = [String: Int]()
        var idCounter = 0
        var uniqueLens = Set<Int>()

        let sArr = Array(source)
        let tArr = Array(target)

        for i in 0..<m {
            if idMap[original[i]] == nil { idMap[original[i]] = idCounter; idCounter += 1 }
            if idMap[changed[i]] == nil { idMap[changed[i]] = idCounter; idCounter += 1 }
            uniqueLens.insert(original[i].count)
        }

        let M = idCounter
        var dist = [[Int]](repeating: [Int](repeating: INF, count: M), count: M)
        for i in 0..<M { dist[i][i] = 0 }

        for i in 0..<m {
            let u = idMap[original[i]]!
            let v = idMap[changed[i]]!
            dist[u][v] = min(dist[u][v], cost[i])
        }

        for k in 0..<M {
            for i in 0..<M {
                for j in 0..<M {
                    if dist[i][k] + dist[k][j] < dist[i][j] {
                        dist[i][j] = dist[i][k] + dist[k][j]
                    }
                }
            }
        }

        let root = TrieNode()
        for (s, id) in idMap {
            var curr = root
            for char in s {
                if curr.children[char] == nil { curr.children[char] = TrieNode() }
                curr = curr.children[char]!
            }
            curr.id = id
        }

        var sourceIds = [[Int: Int]](repeating: [:], count: n)
        var targetIds = [[Int: Int]](repeating: [:], count: n)

        for i in 0..<n {
            var curr = root
            for j in i..<n {
                if let next = curr.children[sArr[j]] {
                    curr = next
                    if curr.id != -1 { sourceIds[i][j - i + 1] = curr.id }
                } else { break }
            }
            curr = root
            for j in i..<n {
                if let next = curr.children[tArr[j]] {
                    curr = next
                    if curr.id != -1 { targetIds[i][j - i + 1] = curr.id }
                } else { break }
            }
        }

        var dp = [Int](repeating: INF, count: n + 1)
        dp[0] = 0
        let lens = Array(uniqueLens)

        for i in 0..<n {
            if dp[i] == INF { continue }
            if sArr[i] == tArr[i] { dp[i + 1] = min(dp[i + 1], dp[i]) }
            for len in lens {
                if i + len <= n, let u = sourceIds[i][len], let v = targetIds[i][len] {
                    if dist[u][v] < INF {
                        dp[i + len] = min(dp[i + len], dp[i] + dist[u][v])
                    }
                }
            }
        }

        return dp[n] >= INF ? -1 : dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    class TrieNode {
        val children = arrayOfNulls<TrieNode>(26)
        var id = -1
    }

    fun minimumCost(source: String, target: String, original: Array<String>, changed: Array<String>, cost: IntArray): Long {
        val n = source.length
        val m = original.size
        val INF = 1e15.toLong()
        val idMap = mutableMapOf<String, Int>()
        var idCounter = 0
        val uniqueLens = mutableSetOf<Int>()

        for (i in 0 until m) {
            if (!idMap.containsKey(original[i])) idMap[original[i]] = idCounter++
            if (!idMap.containsKey(changed[i])) idMap[changed[i]] = idCounter++
            uniqueLens.add(original[i].length)
        }

        val M = idCounter
        val dist = Array(M) { LongArray(M) { INF } }
        for (i in 0 until M) dist[i][i] = 0

        for (i in 0 until m) {
            val u = idMap[original[i]]!!
            val v = idMap[changed[i]]!!
            dist[u][v] = minOf(dist[u][v], cost[i].toLong())
        }

        for (k in 0 until M) {
            for (i in 0 until M) {
                for (j in 0 until M) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j]
                    }
                }
            }
        }

        val root = TrieNode()
        for ((s, id) in idMap) {
            var curr = root
            for (c in s) {
                val idx = c - 'a'
                if (curr.children[idx] == null) curr.children[idx] = TrieNode()
                curr = curr.children[idx]!!
            }
            curr.id = id
        }

        val sourceIds = Array(n) { mutableMapOf<Int, Int>() }
        val targetIds = Array(n) { mutableMapOf<Int, Int>() }

        fun fillIds(str: String, targetArr: Array<MutableMap<Int, Int>>) {
            for (i in 0 until n) {
                var curr = root
                for (j in i until n) {
                    val idx = str[j] - 'a'
                    if (curr.children[idx] == null) break
                    curr = curr.children[idx]!!
                    if (curr.id != -1) targetArr[i][j - i + 1] = curr.id
                }
            }
        }

        fillIds(source, sourceIds)
        fillIds(target, targetIds)

        val dp = LongArray(n + 1) { INF }
        dp[0] = 0
        val lens = uniqueLens.toIntArray()

        for (i in 0 until n) {
            if (dp[i] == INF) continue
            if (source[i] == target[i]) dp[i + 1] = minOf(dp[i + 1], dp[i])
            for (len in lens) {
                if (i + len <= n) {
                    val u = sourceIds[i][len] ?: -1
                    val v = targetIds[i][len] ?: -1
                    if (u != -1 && v != -1 && dist[u][v] < INF) {
                        dp[i + len] = minOf(dp[i + len], dp[i] + dist[u][v])
                    }
                }
            }
        }

        return if (dp[n] >= INF) -1 else dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class TrieNode {
  Map<int, TrieNode> children = {};
  int id = -1;
}

class Solution {
  int minimumCost(String source, String target, List<String> original, List<String> changed, List<int> cost) {
    final int n = source.length;
    final int m = original.length;
    final int INF = 1000000000000000;

    Map<String, int> idMap = {};
    int idCounter = 0;
    Set<int> uniqueLens = {};

    for (int i = 0; i < m; i++) {
      if (!idMap.containsKey(original[i])) idMap[original[i]] = idCounter++;
      if (!idMap.containsKey(changed[i])) idMap[changed[i]] = idCounter++;
      uniqueLens.add(original[i].length);
    }

    int M = idCounter;
    List<List<int>> dist = List.generate(M, (_) => List.filled(M, INF));
    for (int i = 0; i < M; i++) dist[i][i] = 0;

    for (int i = 0; i < m; i++) {
      int u = idMap[original[i]]!;
      int v = idMap[changed[i]]!;
      if (cost[i] < dist[u][v]) dist[u][v] = cost[i];
    }

    for (int k = 0; k < M; k++) {
      for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
          if (dist[i][k] + dist[k][j] < dist[i][j]) {
            dist[i][j] = dist[i][k] + dist[k][j];
          }
        }
      }
    }

    TrieNode root = TrieNode();
    idMap.forEach((s, id) {
      TrieNode curr = root;
      for (int j = 0; j < s.length; j++) {
        int charCode = s.codeUnitAt(j);
        if (!curr.children.containsKey(charCode)) curr.children[charCode] = TrieNode();
        curr = curr.children[charCode]!;
      }
      curr.id = id;
    });

    List<Map<int, int>> sourceIds = List.generate(n, (_) => {});
    List<Map<int, int>> targetIds = List.generate(n, (_) => {});

    void fillIds(String str, List<Map<int, int>> targetArr) {
      for (int i = 0; i < n; i++) {
        TrieNode curr = root;
        for (int j = i; j < n; j++) {
          int charCode = str.codeUnitAt(j);
          if (!curr.children.containsKey(charCode)) break;
          curr = curr.children[charCode]!;
          if (curr.id != -1) targetArr[i][j - i + 1] = curr.id;
        }
      }
    }

    fillIds(source, sourceIds);
    fillIds(target, targetIds);

    List<int> dp = List.filled(n + 1, INF);
    dp[0] = 0;
    List<int> lens = uniqueLens.toList();

    for (int i = 0; i < n; i++) {
      if (dp[i] == INF) continue;
      if (source[i] == target[i]) dp[i + 1] = (dp[i + 1] < dp[i]) ? dp[i + 1] : dp[i];
      for (int len in lens) {
        if (i + len <= n) {
          int? u = sourceIds[i][len];
          int? v = targetIds[i][len];
          if (u != null && v != null && dist[u][v] < INF) {
            int newCost = dp[i] + dist[u][v];
            if (newCost < dp[i + len]) dp[i + len] = newCost;
          }
        }
      }
    }

    return dp[n] >= INF ? -1 : dp[n];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumCost(source string, target string, original []string, changed []string, cost []int) int64 {
    n := len(source)
    m := len(original)
    const INF int64 = 1e15

    idMap := make(map[string]int)
    idCounter := 0
    uniqueLensMap := make(map[int]bool)
    for i := 0; i < m; i++ {
        if _, ok := idMap[original[i]]; !ok { idMap[original[i]] = idCounter; idCounter++ }
        if _, ok := idMap[changed[i]]; !ok { idMap[changed[i]] = idCounter; idCounter++ }
        uniqueLensMap[len(original[i])] = true
    }

    M := idCounter
    dist := make([][]int64, M)
    for i := range dist {
        dist[i] = make([]int64, M)
        for j := range dist[i] { dist[i][j] = INF }
        dist[i][i] = 0
    }

    for i := 0; i < m; i++ {
        u := idMap[original[i]]
        v := idMap[changed[i]]
        if int64(cost[i]) < dist[u][v] { dist[u][v] = int64(cost[i]) }
    }

    for k := 0; k < M; k++ {
        for i := 0; i < M; i++ {
            for j := 0; j < M; j++ {
                if dist[i][k]+dist[k][j] < dist[i][j] {
                    dist[i][j] = dist[i][k] + dist[k][j]
                }
            }
        }
    }

    type TrieNode struct {
        children [26]*TrieNode
        id       int
    }
    root := &TrieNode{id: -1}
    for s, id := range idMap {
        curr := root
        for i := 0; i < len(s); i++ {
            idx := s[i] - 'a'
            if curr.children[idx] == nil { curr.children[idx] = &TrieNode{id: -1} }
            curr = curr.children[idx]
        }
        curr.id = id
    }

    sourceIds := make([]map[int]int, n)
    targetIds := make([]map[int]int, n)
    for i := 0; i < n; i++ {
        sourceIds[i] = make(map[int]int)
        targetIds[i] = make(map[int]int)
    }

    fillIds := func(str string, idsArr []map[int]int) {
        for i := 0; i < n; i++ {
            curr := root
            for j := i; j < n; j++ {
                idx := str[j] - 'a'
                if curr.children[idx] == nil { break }
                curr = curr.children[idx]
                if curr.id != -1 { idsArr[i][j-i+1] = curr.id }
            }
        }
    }
    fillIds(source, sourceIds)
    fillIds(target, targetIds)

    dp := make([]int64, n+1)
    for i := range dp { dp[i] = INF }
    dp[0] = 0
    uniqueLens := make([]int, 0, len(uniqueLensMap))
    for l := range uniqueLensMap { uniqueLens = append(uniqueLens, l) }

    for i := 0; i < n; i++ {
        if dp[i] == INF { continue }
        if source[i] == target[i] {
            if dp[i] < dp[i+1] { dp[i+1] = dp[i] }
        }
        for _, l := range uniqueLens {
            if i+l <= n {
                if u, okU := sourceIds[i][l]; okU {
                    if v, okV := targetIds[i][l]; okV {
                        if dist[u][v] < INF {
                            if dp[i]+dist[u][v] < dp[i+l] { dp[i+l] = dp[i] + dist[u][v] }
                        }
                    }
                }
            }
        }
    }

    if dp[n] >= INF { return -1 }
    return dp[n]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_cost(source, target, original, changed, cost)
  id_map = {}
  id_count = 0
  (original + changed).each do |s|
    unless id_map.key?(s)
      id_map[s] = id_count
      id_count += 1
    end
  end

  inf = 10**15
  dist = Array.new(id_count) { Array.new(id_count, inf) }
  id_count.times { |i| dist[i][i] = 0 }
  original.each_with_index do |s, i|
    u = id_map[s]
    v = id_map[changed[i]]
    dist[u][v] = [dist[u][v], cost[i]].min
  end

  (0...id_count).each do |k|
    (0...id_count).each do |i|
      next if dist[i][k] == inf
      (0...id_count).each do |j|
        next if dist[k][j] == inf
        if dist[i][k] + dist[k][j] < dist[i][j]
          dist[i][j] = dist[i][k] + dist[k][j]
        end
      end
    end
  end

  n = source.length
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  lengths = original.map(&:length).uniq

  (1..n).each do |i|
    dp[i] = [dp[i], dp[i - 1]].min if source[i - 1] == target[i - 1]
    lengths.each do |len|
      if i >= len
        j = i - len
        if dp[j] < inf
          u = id_map[source[j, len]]
          v = id_map[target[j, len]]
          if u && v && dist[u][v] < inf
            dp[i] = [dp[i], dp[j] + dist[u][v]].min
          end
        end
      end
    end
  end

  dp[n] >= inf ? -1 : dp[n]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def minimumCost(source: String, target: String, original: Array[String], changed: Array[String], cost: Array[Int]): Long = {
        val idMap = mutable.HashMap[String, Int]()
        var idCount = 0
        for (s <- original ++ changed) {
            if (!idMap.contains(s)) {
                idMap(s) = idCount
                idCount += 1
            }
        }

        val inf = 1000000000000000L
        val dist = Array.fill(idCount, idCount)(inf)
        for (i <- 0 until idCount) dist(i)(i) = 0
        for (i <- original.indices) {
            val u = idMap(original(i))
            val v = idMap(changed(i))
            dist(u)(v) = Math.min(dist(u)(v), cost(i).toLong)
        }

        for (k <- 0 until idCount; i <- 0 until idCount; j <- 0 until idCount) {
            if (dist(i)(k) != inf && dist(k)(j) != inf) {
                if (dist(i)(k) + dist(k)(j) < dist(i)(j)) {
                    dist(i)(j) = dist(i)(k) + dist(k)(j)
                }
            }
        }

        val n = source.length
        val dp = Array.fill(n + 1)(inf)
        dp(0) = 0
        val uniqueLengths = original.map(_.length).distinct

        for (i <- 1 to n) {
            if (source(i - 1) == target(i - 1)) {
                dp(i) = Math.min(dp(i), dp(i - 1))
            }
            for (len <- uniqueLengths) {
                if (i >= len) {
                    val j = i - len
                    if (dp(j) < inf) {
                        val srcSub = source.substring(j, i)
                        val tgtSub = target.substring(j, i)
                        (idMap.get(srcSub), idMap.get(tgtSub)) match {
                            case (Some(u), Some(v)) =>
                                if (dist(u)(v) < inf) {
                                    dp(i) = Math.min(dp(i), dp(j) + dist(u)(v))
                                }
                            case _ =>
                        }
                    }
                }
            }
        }

        if (dp(n) >= inf) -1 else dp(n)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_cost(source: String, target: String, original: Vec<String>, changed: Vec<String>, cost: Vec<i32>) -> i64 {
        use std::collections::HashMap;
        let mut id_map = HashMap::new();
        let mut id_count = 0;
        for s in original.iter().chain(changed.iter()) {
            if !id_map.contains_key(s) {
                id_map.insert(s.clone(), id_count);
                id_count += 1;
            }
        }

        let inf: i64 = 1_000_000_000_000_000;
        let mut dist = vec![vec![inf; id_count]; id_count];
        for i in 0..id_count { dist[i][i] = 0; }
        for i in 0..original.len() {
            let u = *id_map.get(&original[i]).unwrap();
            let v = *id_map.get(&changed[i]).unwrap();
            dist[u][v] = dist[u][v].min(cost[i] as i64);
        }

        for k in 0..id_count {
            for i in 0..id_count {
                if dist[i][k] == inf { continue; }
                for j in 0..id_count {
                    if dist[k][j] == inf { continue; }
                    if dist[i][k] + dist[k][j] < dist[i][j] {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        let n = source.len();
        let mut dp = vec![inf; n + 1];
        dp[0] = 0;
        let mut lengths: Vec<usize> = original.iter().map(|s| s.len()).collect();
        lengths.sort_unstable();
        lengths.dedup();

        let s_bytes = source.as_bytes();
        let t_bytes = target.as_bytes();

        for i in 1..=n {
            if s_bytes[i - 1] == t_bytes[i - 1] {
                dp[i] = dp[i].min(dp[i - 1]);
            }
            for &len in &lengths {
                if i >= len {
                    let j = i - len;
                    if dp[j] != inf {
                        let src_sub = &source[j..i];
                        let tgt_sub = &target[j..i];
                        if let (Some(&u), Some(&v)) = (id_map.get(src_sub), id_map.get(tgt_sub)) {
                            if dist[u][v] != inf {
                                dp[i] = dp[i].min(dp[j] + dist[u][v]);
                            }
                        }
                    }
                }
            }
        }

        if dp[n] >= inf { -1 } else { dp[n] }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/list)

(define/contract (minimum-cost source target original changed cost)
  (-> string? string? (listof string?) (listof string?) (listof exact-integer?) exact-integer?)
  (let* ([id-map (make-hash)]
         [id-count 0])
    (for ([s (append original changed)])
      (unless (hash-has-key? id-map s)
        (hash-set! id-map s id-count)
        (set! id-count (+ id-count 1))))
    (let ([inf 1000000000000000]
          [dist (make-vector id-count)])
      (for ([i id-count])
        (vector-set! dist i (make-vector id-count inf))
        (vector-set! (vector-ref dist i) i 0))
      (for ([s original] [c changed] [co cost])
        (let ([u (hash-ref id-map s)]
              [v (hash-ref id-map c)])
          (vector-set! (vector-ref dist u) v (min (vector-ref (vector-ref dist u) v) co))))
      (for ([k id-count])
        (for ([i id-count])
          (let ([dik (vector-ref (vector-ref dist i) k)])
            (when (< dik inf)
              (for ([j id-count])
                (let ([dkj (vector-ref (vector-ref dist k) j)])
                  (when (< dkj inf)
                    (let ([dij (vector-ref (vector-ref dist i) j)])
                      (when (> dij (+ dik dkj))
                        (vector-set! (vector-ref dist i) j (+ dik dkj)))))))))))
      (let* ([n (string-length source)]
             [dp (make-vector (+ n 1) inf)]
             [lengths (remove-duplicates (map string-length original))])
        (vector-set! dp 0 0)
        (for ([i (in-range 1 (+ n 1))])
          (when (char=? (string-ref source (- i 1)) (string-ref target (- i 1)))
            (vector-set! dp i (min (vector-ref dp i) (vector-ref dp (- i 1)))))
          (for ([len lengths])
            (when (>= i len)
              (let* ([j (- i len)]
                     [dpj (vector-ref dp j)])
                (when (< dpj inf)
                  (let* ([src-sub (substring source j i)]
                         [tgt-sub (substring target j i)]
                         [u (hash-ref id-map src-sub #f)]
                         [v (hash-ref id-map tgt-sub #f)])
                    (when (and u v)
                      (let ([duv (vector-ref (vector-ref dist u) v)])
                        (when (< duv inf)
                          (vector-set! dp i (min (vector-ref dp i) (+ dpj duv))))))))))))
        (let ([ans (vector-ref dp n)])
          (if (>= ans inf) -1 ans))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
minimum_cost(Source, Target, Original, Changed, Cost) ->
    AllStrings = lists:usort(Original ++ Changed),
    IDMap = maps:from_list(lists:zip(AllStrings, lists:seq(0, length(AllStrings) - 1))),
    IDCount = maps:size(IDMap),
    INF = 1000000000000000,
    Dist0 = maps:from_list([{{I, I}, 0} || I <- lists:seq(0, IDCount - 1)]),
    Zip1 = lists:zip(Original, Changed),
    Zip2 = lists:zip(Zip1, Cost),
    Dist1 = lists:foldl(fun({{S, C}, Co}, Acc) ->
        U = maps:get(S, IDMap),
        V = maps:get(C, IDMap),
        Old = maps:get({U, V}, Acc, INF),
        Acc#{{U, V} => min(Old, Co)}
    end, Dist0, Zip2),
    FinalDist = lists:foldl(fun(K, Dk) ->
        IList = [{I, maps:get({I, K}, Dk)} || I <- lists:seq(0, IDCount - 1), maps:is_key({I, K}, Dk)],
        JList = [{J, maps:get({K, J}, Dk)} || J <- lists:seq(0, IDCount - 1), maps:is_key({K, J}, Dk)],
        lists:foldl(fun({I, DIK}, AccI) ->
            lists:foldl(fun({J, DKJ}, AccJ) ->
                NewVal = DIK + DKJ,
                Existing = maps:get({I, J}, AccJ, INF),
                if NewVal < Existing -> AccJ#{{I, J} => NewVal}; true -> AccJ end
            end, AccI, JList)
        end, Dk, IList)
    end, Dist1, lists:seq(0, IDCount - 1)),
    N = byte_size(Source),
    Lengths = lists:usort([byte_size(S) || S <- Original]),
    DP = lists:foldl(fun(I, AccDP) ->
        CharMatch = (binary_part(Source, I - 1, 1) == binary_part(Target, I - 1, 1)),
        Res0 = if CharMatch -> maps:get(I - 1, AccDP, INF); true -> INF end,
        ResFinal = lists:foldl(fun(Len, MinCost) ->
            if I >= Len ->
                J = I - Len,
                case maps:get(J, AccDP, INF) of
                    DPJ when DPJ < INF ->
                        SrcSub = binary_part(Source, J, Len),
                        TgtSub = binary_part(Target, J, Len),
                        case {maps:find(SrcSub, IDMap), maps:find(TgtSub, IDMap)} of
                            {{ok, U}, {ok, V}} ->
                                case maps:find({U, V}, FinalDist) of
                                    {ok, DUV} -> min(MinCost, DPJ + DUV);
                                    error -> MinCost
                                end;
                            _ -> MinCost
                        end;
                    _ -> MinCost
                end;
            true -> MinCost
            end
        end, Res0, Lengths),
        AccDP#{I => ResFinal}
    end, #{0 => 0}, lists:seq(1, N)),
    Ans = maps:get(N, DP, INF),
    if Ans >= INF -> -1; true -> Ans end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_cost(source :: String.t, target :: String.t, original :: [String.t], changed :: [String.t], cost :: [integer]) :: integer
  def minimum_cost(source, target, original, changed, cost) do
    id_list = Enum.uniq(original ++ changed)
    id_map = Enum.with_index(id_list) |> Enum.into(%{})
    id_count = map_size(id_map)
    inf = 1_000_000_000_000_000
    dist0 = Enum.reduce(0..id_count-1, %{}, fn i, acc -> Map.put(acc, {i, i}, 0) end)
    dist1 = Enum.zip([original, changed, cost])
      |> Enum.reduce(dist0, fn {s, c, co}, acc ->
        u = Map.get(id_map, s)
        v = Map.get(id_map, c)
        Map.put(acc, {u, v}, min(Map.get(acc, {u, v}, inf), co))
      end)
    final_dist = Enum.reduce(0..id_count-1, dist1, fn k, dk ->
      i_list = for i <- 0..id_count-1, dik = Map.get(dk, {i, k}, inf), dik < inf, do: {i, dik}
      j_list = for j <- 0..id_count-1, dkj = Map.get(dk, {k, j}, inf), dkj < inf, do: {j, dkj}
      Enum.reduce(i_list, dk, fn {i, dik}, acc_i ->
        Enum.reduce(j_list, acc_i, fn {j, dkj}, acc_j ->
          new_val = dik + dkj
          if new_val < Map.get(acc_j, {i, j}, inf) do
            Map.put(acc_j, {i, j}, new_val)
          else
            acc_j
          end
        end)
      end)
    end)
    n = byte_size(source)
    unique_lengths = Enum.map(original, &byte_size/1) |> Enum.uniq()
    dp = Enum.reduce(1..n, %{0 => 0}, fn i, acc_dp ->
      res0 = if binary_part(source, i - 1, 1) == binary_part(target, i - 1, 1), do: Map.get(acc_dp, i - 1, inf), else: inf
      res_final = Enum.reduce(unique_lengths, res0, fn len, min_val ->
        if i >= len do
          j = i - len
          dp_j = Map.get(acc_dp, j, inf)
          if dp_j < inf do
            src_sub = binary_part(source, j, len)
            tgt_sub = binary_part(target, j, len)
            u = Map.get(id_map, src_sub)
            v = Map.get(id_map, tgt_sub)
            if u != nil and v != nil do
              duv = Map.get(final_dist, {u, v}, inf)
              min(min_val, dp_j + duv)
            else
              min_val
            end
          else
            min_val
          end
        else
          min_val
        end
      end)
      Map.put(acc_dp, i, res_final)
    end)
    ans = Map.get(dp, n, inf)
    if ans >= inf, do: -1, else: ans
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M^3 + N^2) or O(M^3 + N \cdot M \cdot L), where M is the number of transformation rules, N is the length of the source string, and L is the max rule length. Floyd-Warshall takes O(M^3) for M up to 200, and the DP with Trie traversal or hash lookup takes O(N^2) or O(N \cdot M \cdot L).
- **Space Complexity:** O(M^2 + M \cdot L + N), where M^2 is for the distance matrix, M \cdot L is for the Trie or string hash map, and N is for the DP array. This fits within the 256MB limit easily.
