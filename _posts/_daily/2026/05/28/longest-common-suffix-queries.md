---
layout: post
title: "Longest Common Suffix Queries"
date: 2026-05-28 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "String", "Trie"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/longest-common-suffix-queries/
ai_solutions:
  - solutions:
      cpp: "class Solution {\n    struct TrieNode {\n        TrieNode* children[26];\n\
        \        int bestIdx;\n        TrieNode() : bestIdx(-1) {\n            for (int\
        \ i = 0; i < 26; ++i) children[i] = nullptr;\n        }\n    };\n\npublic:\n\
        \    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>&\
        \ wordsQuery) {\n        TrieNode* root = new TrieNode();\n        int globalBestIdx\
        \ = 0;\n        for (int i = 1; i < wordsContainer.size(); ++i) {\n        \
        \    if (wordsContainer[i].length() < wordsContainer[globalBestIdx].length())\
        \ {\n                globalBestIdx = i;\n            }\n        }\n        root->bestIdx\
        \ = globalBestIdx;\n\n        for (int i = 0; i < wordsContainer.size(); ++i)\
        \ {\n            string s = wordsContainer[i];\n            TrieNode* curr =\
        \ root;\n            for (int j = s.length() - 1; j >= 0; --j) {\n         \
        \       int c = s[j] - 'a';\n                if (!curr->children[c]) {\n   \
        \                 curr->children[c] = new TrieNode();\n                }\n \
        \               curr = curr->children[c];\n                if (curr->bestIdx\
        \ == -1 || wordsContainer[i].length() < wordsContainer[curr->bestIdx].length())\
        \ {\n                    curr->bestIdx = i;\n                }\n           \
        \ }\n        }\n\n        vector<int> ans;\n        for (const string& q : wordsQuery)\
        \ {\n            TrieNode* curr = root;\n            int lastBest = root->bestIdx;\n\
        \            for (int j = q.length() - 1; j >= 0; --j) {\n                int\
        \ c = q[j] - 'a';\n                if (!curr->children[c]) break;\n        \
        \        curr = curr->children[c];\n                lastBest = curr->bestIdx;\n\
        \            }\n            ans.push_back(lastBest);\n        }\n        return\
        \ ans;\n    }\n};"
      java: "class Solution {\n    class TrieNode {\n        TrieNode[] children = new\
        \ TrieNode[26];\n        int bestIdx = -1;\n    }\n\n    public int[] stringIndices(String[]\
        \ wordsContainer, String[] wordsQuery) {\n        TrieNode root = new TrieNode();\n\
        \        int globalBestIdx = 0;\n        for (int i = 1; i < wordsContainer.length;\
        \ i++) {\n            if (wordsContainer[i].length() < wordsContainer[globalBestIdx].length())\
        \ {\n                globalBestIdx = i;\n            }\n        }\n        root.bestIdx\
        \ = globalBestIdx;\n\n        for (int i = 0; i < wordsContainer.length; i++)\
        \ {\n            String s = wordsContainer[i];\n            TrieNode curr =\
        \ root;\n            for (int j = s.length() - 1; j >= 0; j--) {\n         \
        \       int c = s.charAt(j) - 'a';\n                if (curr.children[c] ==\
        \ null) {\n                    curr.children[c] = new TrieNode();\n        \
        \        }\n                curr = curr.children[c];\n                if (curr.bestIdx\
        \ == -1 || s.length() < wordsContainer[curr.bestIdx].length()) {\n         \
        \           curr.bestIdx = i;\n                }\n            }\n        }\n\
        \n        int[] ans = new int[wordsQuery.length];\n        for (int i = 0; i\
        \ < wordsQuery.length; i++) {\n            String q = wordsQuery[i];\n     \
        \       TrieNode curr = root;\n            int lastBest = root.bestIdx;\n  \
        \          for (int j = q.length() - 1; j >= 0; j--) {\n                int\
        \ c = q.charAt(j) - 'a';\n                if (curr.children[c] == null) break;\n\
        \                curr = curr.children[c];\n                lastBest = curr.bestIdx;\n\
        \            }\n            ans[i] = lastBest;\n        }\n        return ans;\n\
        \    }\n}"
      python: "class Solution(object):\n    def stringIndices(self, wordsContainer,\
        \ wordsQuery):\n        \"\"\"\n        :type wordsContainer: List[str]\n  \
        \      :type wordsQuery: List[str]\n        :rtype: List[int]\n        \"\"\"\
        \n        trie = {}\n        # Pre-calculate global best index (shortest length,\
        \ then smallest index)\n        global_best_idx = 0\n        for i in range(1,\
        \ len(wordsContainer)):\n            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):\n\
        \                global_best_idx = i\n\n        # Trie nodes store: {char: {next_node},\
        \ \"best\": best_index}\n        # Initialize root with global best\n      \
        \  root = {\"best\": global_best_idx}\n\n        for i, word in enumerate(wordsContainer):\n\
        \            curr = root\n            word_len = len(word)\n            # Traverse\
        \ word backwards (suffix is prefix of reversed string)\n            for char\
        \ in reversed(word):\n                if char not in curr:\n               \
        \     curr[char] = {\"best\": i}\n                curr = curr[char]\n      \
        \          # Update best index if current word is shorter\n                best_idx\
        \ = curr[\"best\"]\n                if word_len < len(wordsContainer[best_idx]):\n\
        \                    curr[\"best\"] = i\n\n        results = []\n        for\
        \ query in wordsQuery:\n            curr = root\n            res_idx = root[\"\
        best\"]\n            for char in reversed(query):\n                if char in\
        \ curr:\n                    curr = curr[char]\n                    res_idx\
        \ = curr[\"best\"]\n                else:\n                    break\n     \
        \       results.append(res_idx)\n\n        return results"
      python3: "class TrieNode:\n    __slots__ = ['children', 'best_idx']\n    def __init__(self,\
        \ best_idx):\n        self.children = [None] * 26\n        self.best_idx = best_idx\n\
        \nclass Solution:\n    def stringIndices(self, wordsContainer: List[str], wordsQuery:\
        \ List[str]) -> List[int]:\n        n = len(wordsContainer)\n        lengths\
        \ = [len(w) for w in wordsContainer]\n\n        best_overall_idx = 0\n     \
        \   for i in range(1, n):\n            if lengths[i] < lengths[best_overall_idx]:\n\
        \                best_overall_idx = i\n\n        root = TrieNode(best_overall_idx)\n\
        \n        for i in range(n):\n            word = wordsContainer[i]\n       \
        \     word_len = lengths[i]\n            curr = root\n            for char in\
        \ reversed(word):\n                idx = ord(char) - 97\n                if\
        \ curr.children[idx] is None:\n                    curr.children[idx] = TrieNode(i)\n\
        \                curr = curr.children[idx]\n                if word_len < lengths[curr.best_idx]:\n\
        \                    curr.best_idx = i\n\n        ans = []\n        for query\
        \ in wordsQuery:\n            curr = root\n            for char in reversed(query):\n\
        \                idx = ord(char) - 97\n                if curr.children[idx]:\n\
        \                    curr = curr.children[idx]\n                else:\n    \
        \                break\n            ans.append(curr.best_idx)\n        return\
        \ ans"
      c: "#include <string.h>\n#include <stdlib.h>\n\nstatic int trie[500005][26];\n\
        static int bestIdxs[500005];\n\nint* stringIndices(char** wordsContainer, int\
        \ wordsContainerSize, char** wordsQuery, int wordsQuerySize, int* returnSize)\
        \ {\n    int* lengths = (int*)malloc(wordsContainerSize * sizeof(int));\n  \
        \  int bestOverallIdx = 0;\n    for (int i = 0; i < wordsContainerSize; i++)\
        \ {\n        lengths[i] = (int)strlen(wordsContainer[i]);\n        if (lengths[i]\
        \ < lengths[bestOverallIdx]) {\n            bestOverallIdx = i;\n        }\n\
        \    }\n\n    for (int j = 0; j < 26; j++) trie[0][j] = -1;\n    bestIdxs[0]\
        \ = bestOverallIdx;\n    int poolIdx = 1;\n\n    for (int i = 0; i < wordsContainerSize;\
        \ i++) {\n        int len = lengths[i];\n        int curr = 0;\n        for\
        \ (int j = len - 1; j >= 0; j--) {\n            int charIdx = wordsContainer[i][j]\
        \ - 'a';\n            if (trie[curr][charIdx] == -1) {\n                for\
        \ (int k = 0; k < 26; k++) trie[poolIdx][k] = -1;\n                bestIdxs[poolIdx]\
        \ = i;\n                trie[curr][charIdx] = poolIdx++;\n            }\n  \
        \          curr = trie[curr][charIdx];\n            if (len < lengths[bestIdxs[curr]])\
        \ {\n                bestIdxs[curr] = i;\n            }\n        }\n    }\n\n\
        \    int* ans = (int*)malloc(wordsQuerySize * sizeof(int));\n    *returnSize\
        \ = wordsQuerySize;\n    for (int i = 0; i < wordsQuerySize; i++) {\n      \
        \  int len = (int)strlen(wordsQuery[i]);\n        int curr = 0;\n        for\
        \ (int j = len - 1; j >= 0; j--) {\n            int charIdx = wordsQuery[i][j]\
        \ - 'a';\n            if (trie[curr][charIdx] == -1) break;\n            curr\
        \ = trie[curr][charIdx];\n        }\n        ans[i] = bestIdxs[curr];\n    }\n\
        \n    free(lengths);\n    return ans;\n}"
      csharp: "using System;\n\npublic class Solution {\n    private int[] trie = new\
        \ int[500005 * 26];\n    private int[] bestIdxs = new int[500005];\n\n    public\
        \ int[] StringIndices(string[] wordsContainer, string[] wordsQuery) {\n    \
        \    int n = wordsContainer.Length;\n        int[] lengths = new int[n];\n \
        \       int bestOverallIdx = 0;\n\n        for (int i = 0; i < n; i++) {\n \
        \           lengths[i] = wordsContainer[i].Length;\n            if (lengths[i]\
        \ < lengths[bestOverallIdx]) {\n                bestOverallIdx = i;\n      \
        \      }\n        }\n\n        for (int j = 0; j < 26; j++) trie[j] = -1;\n\
        \        bestIdxs[0] = bestOverallIdx;\n        int poolIdx = 1;\n\n       \
        \ for (int i = 0; i < n; i++) {\n            string word = wordsContainer[i];\n\
        \            int len = lengths[i];\n            int curr = 0;\n            for\
        \ (int j = len - 1; j >= 0; j--) {\n                int charIdx = word[j] -\
        \ 'a';\n                int trieIdx = curr * 26 + charIdx;\n               \
        \ if (trie[trieIdx] == -1) {\n                    int newNode = poolIdx++;\n\
        \                    for (int k = 0; k < 26; k++) trie[newNode * 26 + k] = -1;\n\
        \                    bestIdxs[newNode] = i;\n                    trie[trieIdx]\
        \ = newNode;\n                }\n                curr = trie[trieIdx];\n   \
        \             if (len < lengths[bestIdxs[curr]]) {\n                    bestIdxs[curr]\
        \ = i;\n                }\n            }\n        }\n\n        int[] result\
        \ = new int[wordsQuery.Length];\n        for (int i = 0; i < wordsQuery.Length;\
        \ i++) {\n            string query = wordsQuery[i];\n            int curr =\
        \ 0;\n            for (int j = query.Length - 1; j >= 0; j--) {\n          \
        \      int charIdx = query[j] - 'a';\n                int trieIdx = curr * 26\
        \ + charIdx;\n                if (trie[trieIdx] == -1) break;\n            \
        \    curr = trie[trieIdx];\n            }\n            result[i] = bestIdxs[curr];\n\
        \        }\n\n        return result;\n    }\n}"
      javascript: "/**\n * @param {string[]} wordsContainer\n * @param {string[]} wordsQuery\n\
        \ * @return {number[]}\n */\nvar stringIndices = function(wordsContainer, wordsQuery)\
        \ {\n    const n = wordsContainer.length;\n    const lengths = new Int32Array(n);\n\
        \    let bestOverallIdx = 0;\n    for (let i = 0; i < n; i++) {\n        lengths[i]\
        \ = wordsContainer[i].length;\n        if (lengths[i] < lengths[bestOverallIdx])\
        \ {\n            bestOverallIdx = i;\n        }\n    }\n\n    const trie = new\
        \ Int32Array(500005 * 26);\n    const bestIdxs = new Int32Array(500005);\n \
        \   trie.fill(-1, 0, 26);\n    bestIdxs[0] = bestOverallIdx;\n    let poolIdx\
        \ = 1;\n\n    for (let i = 0; i < n; i++) {\n        const word = wordsContainer[i];\n\
        \        const len = lengths[i];\n        let curr = 0;\n        for (let j\
        \ = len - 1; j >= 0; j--) {\n            const charIdx = word.charCodeAt(j)\
        \ - 97;\n            const trieIdx = curr * 26 + charIdx;\n            if (trie[trieIdx]\
        \ === -1) {\n                const newNode = poolIdx++;\n                trie.fill(-1,\
        \ newNode * 26, newNode * 26 + 26);\n                bestIdxs[newNode] = i;\n\
        \                trie[trieIdx] = newNode;\n            }\n            curr =\
        \ trie[trieIdx];\n            if (len < lengths[bestIdxs[curr]]) {\n       \
        \         bestIdxs[curr] = i;\n            }\n        }\n    }\n\n    const\
        \ m = wordsQuery.length;\n    const ans = new Int32Array(m);\n    for (let i\
        \ = 0; i < m; i++) {\n        const query = wordsQuery[i];\n        let curr\
        \ = 0;\n        for (let j = query.length - 1; j >= 0; j--) {\n            const\
        \ charIdx = query.charCodeAt(j) - 97;\n            const trieIdx = curr * 26\
        \ + charIdx;\n            if (trie[trieIdx] === -1) break;\n            curr\
        \ = trie[trieIdx];\n        }\n        ans[i] = bestIdxs[curr];\n    }\n\n \
        \   return Array.from(ans);\n};"
      typescript: "function stringIndices(wordsContainer: string[], wordsQuery: string[]):\
        \ number[] {\n    class TrieNode {\n        bestIdx: number;\n        children:\
        \ { [key: string]: TrieNode };\n        constructor(bestIdx: number) {\n   \
        \         this.bestIdx = bestIdx;\n            this.children = {};\n       \
        \ }\n    }\n\n    const n = wordsContainer.length;\n    const lengths = wordsContainer.map(w\
        \ => w.length);\n    let globalBestIdx = 0;\n    for (let i = 1; i < n; i++)\
        \ {\n        if (lengths[i] < lengths[globalBestIdx]) {\n            globalBestIdx\
        \ = i;\n        }\n    }\n\n    const root = new TrieNode(globalBestIdx);\n\n\
        \    for (let i = 0; i < n; i++) {\n        const word = wordsContainer[i];\n\
        \        const wordLen = lengths[i];\n        let curr = root;\n        for\
        \ (let j = wordLen - 1; j >= 0; j--) {\n            const char = word[j];\n\
        \            if (!curr.children[char]) {\n                curr.children[char]\
        \ = new TrieNode(i);\n            } else {\n                const bestNodeIdx\
        \ = curr.children[char].bestIdx;\n                if (wordLen < lengths[bestNodeIdx])\
        \ {\n                    curr.children[char].bestIdx = i;\n                }\n\
        \            }\n            curr = curr.children[char];\n        }\n    }\n\n\
        \    const results: number[] = [];\n    for (const query of wordsQuery) {\n\
        \        let curr = root;\n        for (let j = query.length - 1; j >= 0; j--)\
        \ {\n            const char = query[j];\n            if (!curr.children[char])\
        \ {\n                break;\n            }\n            curr = curr.children[char];\n\
        \        }\n        results.push(curr.bestIdx);\n    }\n\n    return results;\n\
        };"
      php: "class TrieNode {\n    public $bestIdx;\n    public $children = [];\n   \
        \ public function __construct($idx) {\n        $this->bestIdx = $idx;\n    }\n\
        }\n\nclass Solution {\n\n    /**\n     * @param String[] $wordsContainer\n \
        \    * @param String[] $wordsQuery\n     * @return Integer[]\n     */\n    function\
        \ stringIndices($wordsContainer, $wordsQuery) {\n        $n = count($wordsContainer);\n\
        \        $lengths = [];\n        $globalBestIdx = 0;\n\n        for ($i = 0;\
        \ $i < $n; $i++) {\n            $lengths[$i] = strlen($wordsContainer[$i]);\n\
        \            if ($lengths[$i] < $lengths[$globalBestIdx]) {\n              \
        \  $globalBestIdx = $i;\n            }\n        }\n\n        $root = new TrieNode($globalBestIdx);\n\
        \n        for ($i = 0; $i < $n; $i++) {\n            $word = $wordsContainer[$i];\n\
        \            $wordLen = $lengths[$i];\n            $curr = $root;\n        \
        \    for ($j = $wordLen - 1; $j >= 0; $j--) {\n                $char = $word[$j];\n\
        \                if (!isset($curr->children[$char])) {\n                   \
        \ $curr->children[$char] = new TrieNode($i);\n                } else {\n   \
        \                 $best = $curr->children[$char]->bestIdx;\n               \
        \     if ($wordLen < $lengths[$best]) {\n                        $curr->children[$char]->bestIdx\
        \ = $i;\n                    }\n                }\n                $curr = $curr->children[$char];\n\
        \            }\n        }\n\n        $results = [];\n        foreach ($wordsQuery\
        \ as $query) {\n            $qLen = strlen($query);\n            $curr = $root;\n\
        \            for ($j = $qLen - 1; $j >= 0; $j--) {\n                $char =\
        \ $query[$j];\n                if (!isset($curr->children[$char])) {\n     \
        \               break;\n                }\n                $curr = $curr->children[$char];\n\
        \            }\n            $results[] = $curr->bestIdx;\n        }\n\n    \
        \    return $results;\n    }\n}"
      swift: "class Solution {\n    class TrieNode {\n        var bestIdx: Int\n   \
        \     var children: [UInt8: TrieNode] = [:]\n        init(bestIdx: Int) {\n\
        \            self.bestIdx = bestIdx\n        }\n    }\n\n    func stringIndices(_\
        \ wordsContainer: [String], _ wordsQuery: [String]) -> [Int] {\n        let\
        \ n = wordsContainer.count\n        var lengths = [Int](repeating: 0, count:\
        \ n)\n        var globalBestIdx = 0\n\n        for i in 0..<n {\n          \
        \  lengths[i] = wordsContainer[i].utf8.count\n            if lengths[i] < lengths[globalBestIdx]\
        \ {\n                globalBestIdx = i\n            }\n        }\n\n       \
        \ let root = TrieNode(bestIdx: globalBestIdx)\n\n        for i in 0..<n {\n\
        \            let word = Array(wordsContainer[i].utf8)\n            let wordLen\
        \ = lengths[i]\n            var curr = root\n            for j in stride(from:\
        \ wordLen - 1, through: 0, by: -1) {\n                let charCode = word[j]\n\
        \                if let next = curr.children[charCode] {\n                 \
        \   if wordLen < lengths[next.bestIdx] {\n                        next.bestIdx\
        \ = i\n                    }\n                    curr = next\n            \
        \    } else {\n                    let newNode = TrieNode(bestIdx: i)\n    \
        \                curr.children[charCode] = newNode\n                    curr\
        \ = newNode\n                }\n            }\n        }\n\n        var results\
        \ = [Int]()\n        results.reserveCapacity(wordsQuery.count)\n\n        for\
        \ query in wordsQuery {\n            let queryBytes = Array(query.utf8)\n  \
        \          var curr = root\n            for j in stride(from: queryBytes.count\
        \ - 1, through: 0, by: -1) {\n                let charCode = queryBytes[j]\n\
        \                if let next = curr.children[charCode] {\n                 \
        \   curr = next\n                } else {\n                    break\n     \
        \           }\n            }\n            results.append(curr.bestIdx)\n   \
        \     }\n\n        return results\n    }\n}"
      kotlin: "class Solution {\n    class TrieNode(var bestIdx: Int) {\n        val\
        \ children = arrayOfNulls<TrieNode>(26)\n    }\n\n    fun stringIndices(wordsContainer:\
        \ Array<String>, wordsQuery: Array<String>): IntArray {\n        val n = wordsContainer.size\n\
        \        val lengths = IntArray(n)\n        var globalBestIdx = 0\n\n      \
        \  for (i in 0 until n) {\n            lengths[i] = wordsContainer[i].length\n\
        \            if (lengths[i] < lengths[globalBestIdx]) {\n                globalBestIdx\
        \ = i\n            }\n        }\n\n        val root = TrieNode(globalBestIdx)\n\
        \n        for (i in 0 until n) {\n            val word = wordsContainer[i]\n\
        \            val wordLen = lengths[i]\n            var curr = root\n       \
        \     for (j in wordLen - 1 downTo 0) {\n                val charIdx = word[j]\
        \ - 'a'\n                if (curr.children[charIdx] == null) {\n           \
        \         curr.children[charIdx] = TrieNode(i)\n                } else {\n \
        \                   val best = curr.children[charIdx]!!.bestIdx\n          \
        \          if (wordLen < lengths[best]) {\n                        curr.children[charIdx]!!.bestIdx\
        \ = i\n                    }\n                }\n                curr = curr.children[charIdx]!!\n\
        \            }\n        }\n\n        val results = IntArray(wordsQuery.size)\n\
        \        for (i in wordsQuery.indices) {\n            val query = wordsQuery[i]\n\
        \            var curr = root\n            for (j in query.length - 1 downTo\
        \ 0) {\n                val charIdx = query[j] - 'a'\n                if (curr.children[charIdx]\
        \ == null) {\n                    break\n                }\n               \
        \ curr = curr.children[charIdx]!!\n            }\n            results[i] = curr.bestIdx\n\
        \        }\n\n        return results\n    }\n}"
      dart: "class TrieNode {\n  int bestIdx;\n  int bestLen;\n  final List<TrieNode?>\
        \ children = List.filled(26, null);\n  TrieNode(this.bestIdx, this.bestLen);\n\
        }\n\nclass Solution {\n  List<int> stringIndices(List<String> wordsContainer,\
        \ List<String> wordsQuery) {\n    TrieNode root = TrieNode(0, wordsContainer[0].length);\n\
        \n    for (int i = 0; i < wordsContainer.length; i++) {\n      String word =\
        \ wordsContainer[i];\n      if (word.length < root.bestLen) {\n        root.bestIdx\
        \ = i;\n        root.bestLen = word.length;\n      }\n      TrieNode curr =\
        \ root;\n      for (int j = word.length - 1; j >= 0; j--) {\n        int code\
        \ = word.codeUnitAt(j) - 97;\n        if (curr.children[code] == null) {\n \
        \         curr.children[code] = TrieNode(i, word.length);\n        } else if\
        \ (word.length < curr.children[code]!.bestLen) {\n          curr.children[code]!.bestIdx\
        \ = i;\n          curr.children[code]!.bestLen = word.length;\n        }\n \
        \       curr = curr.children[code]!;\n      }\n    }\n\n    List<int> ans =\
        \ List.filled(wordsQuery.length, 0);\n    for (int i = 0; i < wordsQuery.length;\
        \ i++) {\n      String query = wordsQuery[i];\n      TrieNode curr = root;\n\
        \      for (int j = query.length - 1; j >= 0; j--) {\n        int code = query.codeUnitAt(j)\
        \ - 97;\n        if (curr.children[code] == null) {\n          break;\n    \
        \    }\n        curr = curr.children[code]!;\n      }\n      ans[i] = curr.bestIdx;\n\
        \    }\n\n    return ans;\n  }\n}"
      go: "func stringIndices(wordsContainer []string, wordsQuery []string) []int {\n\
        \ttype TrieNode struct {\n\t\tchildren [26]*TrieNode\n\t\tbestIdx  int\n\t\t\
        bestLen  int\n\t}\n\n\troot := &TrieNode{bestIdx: 0, bestLen: len(wordsContainer[0])}\n\
        \n\tfor i, word := range wordsContainer {\n\t\tif len(word) < root.bestLen {\n\
        \t\t\troot.bestIdx = i\n\t\t\troot.bestLen = len(word)\n\t\t}\n\t\tcurr := root\n\
        \t\tfor j := len(word) - 1; j >= 0; j-- {\n\t\t\tc := word[j] - 'a'\n\t\t\t\
        if curr.children[c] == nil {\n\t\t\t\tcurr.children[c] = &TrieNode{bestIdx:\
        \ i, bestLen: len(word)}\n\t\t\t} else if len(word) < curr.children[c].bestLen\
        \ {\n\t\t\t\tcurr.children[c].bestIdx = i\n\t\t\t\tcurr.children[c].bestLen\
        \ = len(word)\n\t\t\t}\n\t\t\tcurr = curr.children[c]\n\t\t}\n\t}\n\n\tans :=\
        \ make([]int, len(wordsQuery))\n\tfor i, query := range wordsQuery {\n\t\tcurr\
        \ := root\n\t\tfor j := len(query) - 1; j >= 0; j-- {\n\t\t\tc := query[j] -\
        \ 'a'\n\t\t\tif curr.children[c] == nil {\n\t\t\t\tbreak\n\t\t\t}\n\t\t\tcurr\
        \ = curr.children[c]\n\t\t}\n\t\tans[i] = curr.bestIdx\n\t}\n\n\treturn ans\n\
        }"
      ruby: "class TrieNode\n  attr_accessor :best_idx, :best_len, :children\n  def\
        \ initialize(idx, len)\n    @best_idx = idx\n    @best_len = len\n    @children\
        \ = Array.new(26)\n  end\nend\n\n# @param {String[]} words_container\n# @param\
        \ {String[]} words_query\n# @return {Integer[]}\ndef string_indices(words_container,\
        \ words_query)\n  root = TrieNode.new(0, words_container[0].length)\n\n  words_container.each_with_index\
        \ do |word, i|\n    w_len = word.length\n    if w_len < root.best_len\n    \
        \  root.best_idx = i\n      root.best_len = w_len\n    end\n\n    curr = root\n\
        \    (w_len - 1).downto(0) do |j|\n      code = word.getbyte(j) - 97\n     \
        \ if curr.children[code].nil?\n        curr.children[code] = TrieNode.new(i,\
        \ w_len)\n      elsif w_len < curr.children[code].best_len\n        curr.children[code].best_idx\
        \ = i\n        curr.children[code].best_len = w_len\n      end\n      curr =\
        \ curr.children[code]\n    end\n  end\n\n  words_query.map do |query|\n    curr\
        \ = root\n    (query.length - 1).downto(0) do |j|\n      code = query.getbyte(j)\
        \ - 97\n      if code < 0 || code >= 26 || curr.children[code].nil?\n      \
        \  break\n      end\n      curr = curr.children[code]\n    end\n    curr.best_idx\n\
        \  end\nend"
      scala: "object Solution {\n    class TrieNode(var bestIdx: Int, var bestLen: Int)\
        \ {\n        val children: Array[TrieNode] = new Array[TrieNode](26)\n    }\n\
        \n    def stringIndices(wordsContainer: Array[String], wordsQuery: Array[String]):\
        \ Array[Int] = {\n        val root = new TrieNode(0, wordsContainer(0).length)\n\
        \n        var i = 0\n        while (i < wordsContainer.length) {\n         \
        \   val word = wordsContainer(i)\n            val wLen = word.length\n     \
        \       if (wLen < root.bestLen) {\n                root.bestIdx = i\n     \
        \           root.bestLen = wLen\n            }\n            var curr = root\n\
        \            var j = wLen - 1\n            while (j >= 0) {\n              \
        \  val c = word(j) - 'a'\n                if (curr.children(c) == null) {\n\
        \                    curr.children(c) = new TrieNode(i, wLen)\n            \
        \    } else if (wLen < curr.children(c).bestLen) {\n                    curr.children(c).bestIdx\
        \ = i\n                    curr.children(c).bestLen = wLen\n               \
        \ }\n                curr = curr.children(c)\n                j -= 1\n     \
        \       }\n            i += 1\n        }\n\n        val ans = new Array[Int](wordsQuery.length)\n\
        \        var qIdx = 0\n        while (qIdx < wordsQuery.length) {\n        \
        \    val query = wordsQuery(qIdx)\n            var curr = root\n           \
        \ var j = query.length - 1\n            while (j >= 0) {\n                val\
        \ c = query(j) - 'a'\n                if (c < 0 || c >= 26 || curr.children(c)\
        \ == null) {\n                    j = -1\n                } else {\n       \
        \             curr = curr.children(c)\n                    j -= 1\n        \
        \        }\n            }\n            ans(qIdx) = curr.bestIdx\n          \
        \  qIdx += 1\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn string_indices(words_container: Vec<String>,\
        \ words_query: Vec<String>) -> Vec<i32> {\n        let n = words_container.len();\n\
        \        let lengths: Vec<usize> = words_container.iter().map(|s| s.len()).collect();\n\
        \n        let mut global_best_idx = 0;\n        for i in 1..n {\n          \
        \  if lengths[i] < lengths[global_best_idx] {\n                global_best_idx\
        \ = i;\n            } else if lengths[i] == lengths[global_best_idx] {\n   \
        \             if i < global_best_idx {\n                    global_best_idx\
        \ = i;\n                }\n            }\n        }\n\n        struct Node {\n\
        \            children: [i32; 26],\n            best_idx: i32,\n        }\n\n\
        \        let mut trie = vec![Node {\n            children: [-1; 26],\n     \
        \       best_idx: global_best_idx as i32,\n        }];\n\n        for (i, word)\
        \ in words_container.iter().enumerate() {\n            let mut curr = 0;\n \
        \           let i_len = lengths[i];\n            let i_val = i as i32;\n\n \
        \           let root_best = trie[0].best_idx as usize;\n            if i_len\
        \ < lengths[root_best] || (i_len == lengths[root_best] && i < root_best) {\n\
        \                trie[0].best_idx = i_val;\n            }\n\n            for\
        \ &b in word.as_bytes().iter().rev() {\n                let c = (b - b'a') as\
        \ usize;\n                if trie[curr].children[c] == -1 {\n              \
        \      let new_node_idx = trie.len() as i32;\n                    trie.push(Node\
        \ {\n                        children: [-1; 26],\n                        best_idx:\
        \ i_val,\n                    });\n                    trie[curr].children[c]\
        \ = new_node_idx;\n                }\n                curr = trie[curr].children[c]\
        \ as usize;\n                let curr_best = trie[curr].best_idx as usize;\n\
        \                if i_len < lengths[curr_best] || (i_len == lengths[curr_best]\
        \ && i < curr_best) {\n                    trie[curr].best_idx = i_val;\n  \
        \              }\n            }\n        }\n\n        words_query\n        \
        \    .into_iter()\n            .map(|query| {\n                let mut curr\
        \ = 0;\n                for &b in query.as_bytes().iter().rev() {\n        \
        \            let c = (b - b'a') as usize;\n                    if trie[curr].children[c]\
        \ == -1 {\n                        break;\n                    }\n         \
        \           curr = trie[curr].children[c] as usize;\n                }\n   \
        \             trie[curr].best_idx\n            })\n            .collect()\n\
        \    }\n}"
      racket: "(struct trie-node ([best-idx #:mutable] [children #:mutable]))\n\n(define/contract\
        \ (string-indices wordsContainer wordsQuery)\n  (-> (listof string?) (listof\
        \ string?) (listof exact-integer?))\n  (let* ([n (length wordsContainer)]\n\
        \         [words-vec (list->vector wordsContainer)]\n         [lengths (vector-map\
        \ string-length words-vec)])\n\n    (define (better? idx1 idx2)\n      (let\
        \ ([len1 (vector-ref lengths idx1)]\n            [len2 (vector-ref lengths idx2)])\n\
        \        (or (< len1 len2)\n            (and (= len1 len2) (< idx1 idx2)))))\n\
        \n    (define global-best-idx\n      (let loop ([i 1] [best 0])\n        (if\
        \ (>= i n)\n            best\n            (if (better? i best)\n           \
        \     (loop (+ i 1) i)\n                (loop (+ i 1) best)))))\n\n    (define\
        \ root (trie-node global-best-idx (make-vector 26 #f)))\n\n    (for ([i (in-range\
        \ n)])\n      (let* ([word (vector-ref words-vec i)]\n             [chars (reverse\
        \ (string->list word))])\n        (let loop ([cs chars] [curr root])\n     \
        \     (when (better? i (trie-node-best-idx curr))\n            (set-trie-node-best-idx!\
        \ curr i))\n          (unless (null? cs)\n            (let* ([c-idx (- (char->integer\
        \ (car cs)) 97)]\n                   [children (trie-node-children curr)])\n\
        \              (unless (vector-ref children c-idx)\n                (vector-set!\
        \ children c-idx (trie-node i (make-vector 26 #f))))\n              (loop (cdr\
        \ cs) (vector-ref children c-idx)))))))\n\n    (map (lambda (query)\n      \
        \     (let* ([chars (reverse (string->list query))])\n             (let loop\
        \ ([cs chars] [curr root])\n               (if (null? cs)\n                \
        \   (trie-node-best-idx curr)\n                   (let* ([c-idx (- (char->integer\
        \ (car cs)) 97)]\n                          [next (vector-ref (trie-node-children\
        \ curr) c-idx)])\n                     (if next\n                         (loop\
        \ (cdr cs) next)\n                         (trie-node-best-idx curr)))))))\n\
        \         wordsQuery)))"
      erlang: "-spec string_indices(WordsContainer :: [unicode:unicode_binary()], WordsQuery\
        \ :: [unicode:unicode_binary()]) -> [integer()].\nstring_indices(WordsContainer,\
        \ WordsQuery) ->\n    LengthsList = [byte_size(W) || W <- WordsContainer],\n\
        \    Lengths = list_to_tuple(LengthsList),\n    N = tuple_size(Lengths),\n \
        \   GlobalBestIdx = find_global_best(1, 0, N, Lengths),\n    Enumerate = lists:zip(WordsContainer,\
        \ lists:seq(0, N - 1)),\n    Trie = lists:foldl(fun({Word, Idx}, T) ->\n   \
        \     insert(list_to_binary(lists:reverse(binary_to_list(Word))), Idx, T, Lengths)\n\
        \    end, {node, GlobalBestIdx, #{}}, Enumerate),\n    [query_trie(list_to_binary(lists:reverse(binary_to_list(Q))),\
        \ Trie) || Q <- WordsQuery].\n\nfind_global_best(I, Best, N, Lengths) when I\
        \ =:= N -> Best;\nfind_global_best(I, Best, N, Lengths) ->\n    case is_better(I,\
        \ Best, Lengths) of\n        true -> find_global_best(I + 1, I, N, Lengths);\n\
        \        false -> find_global_best(I + 1, Best, N, Lengths)\n    end.\n\nis_better(NewIdx,\
        \ CurIdx, Lengths) ->\n    L1 = element(NewIdx + 1, Lengths),\n    L2 = element(CurIdx\
        \ + 1, Lengths),\n    (L1 < L2) orelse (L1 =:= L2 andalso NewIdx < CurIdx).\n\
        \ninsert(<<>>, Idx, {node, BestIdx, Children}, Lengths) ->\n    NewBest = if\
        \ is_better(Idx, BestIdx, Lengths) -> Idx; true -> BestIdx end,\n    {node,\
        \ NewBest, Children};\ninsert(<<C, Rest/binary>>, Idx, {node, BestIdx, Children},\
        \ Lengths) ->\n    NewBestIdx = if is_better(Idx, BestIdx, Lengths) -> Idx;\
        \ true -> BestIdx end,\n    Child = maps:get(C, Children, {node, Idx, #{}}),\n\
        \    NewChild = insert(Rest, Idx, Child, Lengths),\n    {node, NewBestIdx, maps:put(C,\
        \ NewChild, Children)}.\n\nquery_trie(<<C, Rest/binary>>, {node, BestIdx, Children})\
        \ ->\n    case maps:get(C, Children, undefined) of\n        undefined -> BestIdx;\n\
        \        NextNode -> query_trie(Rest, NextNode)\n    end;\nquery_trie(<<>>,\
        \ {node, BestIdx, _}) -> BestIdx."
      elixir: "defmodule Solution do\n  @spec string_indices(words_container :: [String.t],\
        \ words_query :: [String.t]) :: [integer]\n  def string_indices(words_container,\
        \ words_query) do\n    lengths_list = Enum.map(words_container, &byte_size/1)\n\
        \    lengths = List.to_tuple(lengths_list)\n    n = tuple_size(lengths)\n\n\
        \    global_best_idx = \n      Enum.reduce(1..(n - 1)//1, 0, fn i, best ->\n\
        \        if is_better(i, best, lengths), do: i, else: best\n      end)\n\n \
        \   trie = \n      words_container\n      |> Enum.with_index()\n      |> Enum.reduce({global_best_idx,\
        \ %{}}, fn {word, idx}, trie ->\n        insert(String.reverse(word), idx, trie,\
        \ lengths)\n      end)\n\n    Enum.map(words_query, fn query ->\n      query_trie(String.reverse(query),\
        \ trie)\n    end)\n  end\n\n  defp is_better(new_idx, cur_idx, lengths) do\n\
        \    l1 = elem(lengths, new_idx)\n    l2 = elem(lengths, cur_idx)\n    l1 <\
        \ l2 or (l1 == l2 and new_idx < cur_idx)\n  end\n\n  defp insert(<<>>, idx,\
        \ {best_idx, children}, lengths) do\n    new_best = if is_better(idx, best_idx,\
        \ lengths), do: idx, else: best_idx\n    {new_best, children}\n  end\n\n  defp\
        \ insert(<<c, rest::binary>>, idx, {best_idx, children}, lengths) do\n    new_best\
        \ = if is_better(idx, best_idx, lengths), do: idx, else: best_idx\n    child\
        \ = Map.get(children, c, {idx, %{}})\n    new_child = insert(rest, idx, child,\
        \ lengths)\n    {new_best, Map.put(children, c, new_child)}\n  end\n\n  defp\
        \ query_trie(<<c, rest::binary>>, {best_idx, children}) do\n    case Map.get(children,\
        \ c) do\n      nil -> best_idx\n      next_node -> query_trie(rest, next_node)\n\
        \    end\n  end\n\n  defp query_trie(<<>>, {best_idx, _children}) do\n    best_idx\n\
        \  end\nend"
    approach: 'To find the longest common suffix, we reverse all strings in ''wordsContainer''
      and ''wordsQuery'' and transform the problem into finding the longest common prefix.
      We utilize a Trie (Prefix Tree) where each node represents a character in the
      reversed strings. To handle the tie-breaking criteria (shortest length, then earliest
      index), every node in the Trie stores the index of the ''best'' word that passes
      through it. As we iterate through ''wordsContainer'', we update a node''s stored
      index only if the current word''s length is strictly less than the length of the
      word previously recorded at that node. Since we process strings in their original
      order, the earliest index requirement is naturally satisfied when lengths are
      equal.


      During the query phase, each word in ''wordsQuery'' is reversed and traversed
      through the Trie character by character. We follow the path as deep as possible;
      the ''best'' index stored at the final reachable node indicates the word in ''wordsContainer''
      that shares the maximum number of prefix characters (original suffixes) while
      adhering to the tie-breaking rules. If a query word has no common suffix characters,
      the root node provides the index of the shortest (and earliest) word in the entire
      container.'
    time_complexity: O(N + M) where N is the sum of lengths of all strings in 'wordsContainer'
      and M is the sum of lengths of all strings in 'wordsQuery'. Building the Trie
      involves iterating through each character of every word in 'wordsContainer' once,
      and querying involves iterating through each character of every word in 'wordsQuery'
      once.
    space_complexity: O(N × Σ) where N is the sum of lengths of all strings in 'wordsContainer'
      and Σ is the alphabet size (26). Each character in 'wordsContainer' can potentially
      create a new node in the Trie, and each node stores a fixed-size array or map
      for its children and an integer index.
    elapsed_time: 364.98479676246643
    model: gemini-3-flash-preview
    generated_at: '2026-05-28 02:35:48 '
---

## Problem #3093: Longest Common Suffix Queries

**Difficulty:** Hard

**Topics:** Array, String, Trie

## Problem Description

<p>You are given two arrays of strings <code>wordsContainer</code> and <code>wordsQuery</code>.</p>

<p>For each <code>wordsQuery[i]</code>, you need to find a string from <code>wordsContainer</code> that has the <strong>longest common suffix</strong> with <code>wordsQuery[i]</code>. If there are two or more strings in <code>wordsContainer</code> that share the longest common suffix, find the string that is the <strong>smallest</strong> in length. If there are two or more such strings that have the <strong>same</strong> smallest length, find the one that occurred <strong>earlier</strong> in <code>wordsContainer</code>.</p>

<p>Return <em>an array of integers </em><code>ans</code><em>, where </em><code>ans[i]</code><em> is the index of the string in </em><code>wordsContainer</code><em> that has the <strong>longest common suffix</strong> with </em><code>wordsQuery[i]</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">wordsContainer = [&quot;abcd&quot;,&quot;bcd&quot;,&quot;xbcd&quot;], wordsQuery = [&quot;cd&quot;,&quot;bcd&quot;,&quot;xyz&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,1,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>Let&#39;s look at each <code>wordsQuery[i]</code> separately:</p>

<ul>
	<li>For <code>wordsQuery[0] = &quot;cd&quot;</code>, strings from <code>wordsContainer</code> that share the longest common suffix <code>&quot;cd&quot;</code> are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.</li>
	<li>For <code>wordsQuery[1] = &quot;bcd&quot;</code>, strings from <code>wordsContainer</code> that share the longest common suffix <code>&quot;bcd&quot;</code> are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.</li>
	<li>For <code>wordsQuery[2] = &quot;xyz&quot;</code>, there is no string from <code>wordsContainer</code> that shares a common suffix. Hence the longest common suffix is <code>&quot;&quot;</code>, that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">wordsContainer = [&quot;abcdefgh&quot;,&quot;poiuygh&quot;,&quot;ghghgh&quot;], wordsQuery = [&quot;gh&quot;,&quot;acbfgh&quot;,&quot;acbfegh&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,0,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>Let&#39;s look at each <code>wordsQuery[i]</code> separately:</p>

<ul>
	<li>For <code>wordsQuery[0] = &quot;gh&quot;</code>, strings from <code>wordsContainer</code> that share the longest common suffix <code>&quot;gh&quot;</code> are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.</li>
	<li>For <code>wordsQuery[1] = &quot;acbfgh&quot;</code>, only the string at index 0 shares the longest common suffix <code>&quot;fgh&quot;</code>. Hence it is the answer, even though the string at index 2 is shorter.</li>
	<li>For <code>wordsQuery[2] = &quot;acbfegh&quot;</code>, strings from <code>wordsContainer</code> that share the longest common suffix <code>&quot;gh&quot;</code> are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= wordsContainer.length, wordsQuery.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= wordsContainer[i].length &lt;= 5 * 10<sup>3</sup></code></li>
	<li><code>1 &lt;= wordsQuery[i].length &lt;= 5 * 10<sup>3</sup></code></li>
	<li><code>wordsContainer[i]</code> consists only of lowercase English letters.</li>
	<li><code>wordsQuery[i]</code> consists only of lowercase English letters.</li>
	<li>Sum of <code>wordsContainer[i].length</code> is at most <code>5 * 10<sup>5</sup></code>.</li>
	<li>Sum of <code>wordsQuery[i].length</code> is at most <code>5 * 10<sup>5</sup></code>.</li>
</ul>


## Hints

1. If we reverse the strings, the problem changes to finding the longest common prefix.

2. Build a Trie, each node is a letter and only saves the best word’s index in each node, based on the criteria.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the longest common suffix, we reverse all strings in 'wordsContainer' and 'wordsQuery' and transform the problem into finding the longest common prefix. We utilize a Trie (Prefix Tree) where each node represents a character in the reversed strings. To handle the tie-breaking criteria (shortest length, then earliest index), every node in the Trie stores the index of the 'best' word that passes through it. As we iterate through 'wordsContainer', we update a node's stored index only if the current word's length is strictly less than the length of the word previously recorded at that node. Since we process strings in their original order, the earliest index requirement is naturally satisfied when lengths are equal.

During the query phase, each word in 'wordsQuery' is reversed and traversed through the Trie character by character. We follow the path as deep as possible; the 'best' index stored at the final reachable node indicates the word in 'wordsContainer' that shares the maximum number of prefix characters (original suffixes) while adhering to the tie-breaking rules. If a query word has no common suffix characters, the root node provides the index of the shortest (and earliest) word in the entire container.

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
    struct TrieNode {
        TrieNode* children[26];
        int bestIdx;
        TrieNode() : bestIdx(-1) {
            for (int i = 0; i < 26; ++i) children[i] = nullptr;
        }
    };

public:
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        TrieNode* root = new TrieNode();
        int globalBestIdx = 0;
        for (int i = 1; i < wordsContainer.size(); ++i) {
            if (wordsContainer[i].length() < wordsContainer[globalBestIdx].length()) {
                globalBestIdx = i;
            }
        }
        root->bestIdx = globalBestIdx;

        for (int i = 0; i < wordsContainer.size(); ++i) {
            string s = wordsContainer[i];
            TrieNode* curr = root;
            for (int j = s.length() - 1; j >= 0; --j) {
                int c = s[j] - 'a';
                if (!curr->children[c]) {
                    curr->children[c] = new TrieNode();
                }
                curr = curr->children[c];
                if (curr->bestIdx == -1 || wordsContainer[i].length() < wordsContainer[curr->bestIdx].length()) {
                    curr->bestIdx = i;
                }
            }
        }

        vector<int> ans;
        for (const string& q : wordsQuery) {
            TrieNode* curr = root;
            int lastBest = root->bestIdx;
            for (int j = q.length() - 1; j >= 0; --j) {
                int c = q[j] - 'a';
                if (!curr->children[c]) break;
                curr = curr->children[c];
                lastBest = curr->bestIdx;
            }
            ans.push_back(lastBest);
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
    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        int bestIdx = -1;
    }

    public int[] stringIndices(String[] wordsContainer, String[] wordsQuery) {
        TrieNode root = new TrieNode();
        int globalBestIdx = 0;
        for (int i = 1; i < wordsContainer.length; i++) {
            if (wordsContainer[i].length() < wordsContainer[globalBestIdx].length()) {
                globalBestIdx = i;
            }
        }
        root.bestIdx = globalBestIdx;

        for (int i = 0; i < wordsContainer.length; i++) {
            String s = wordsContainer[i];
            TrieNode curr = root;
            for (int j = s.length() - 1; j >= 0; j--) {
                int c = s.charAt(j) - 'a';
                if (curr.children[c] == null) {
                    curr.children[c] = new TrieNode();
                }
                curr = curr.children[c];
                if (curr.bestIdx == -1 || s.length() < wordsContainer[curr.bestIdx].length()) {
                    curr.bestIdx = i;
                }
            }
        }

        int[] ans = new int[wordsQuery.length];
        for (int i = 0; i < wordsQuery.length; i++) {
            String q = wordsQuery[i];
            TrieNode curr = root;
            int lastBest = root.bestIdx;
            for (int j = q.length() - 1; j >= 0; j--) {
                int c = q.charAt(j) - 'a';
                if (curr.children[c] == null) break;
                curr = curr.children[c];
                lastBest = curr.bestIdx;
            }
            ans[i] = lastBest;
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
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        trie = {}
        # Pre-calculate global best index (shortest length, then smallest index)
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):
                global_best_idx = i

        # Trie nodes store: {char: {next_node}, "best": best_index}
        # Initialize root with global best
        root = {"best": global_best_idx}

        for i, word in enumerate(wordsContainer):
            curr = root
            word_len = len(word)
            # Traverse word backwards (suffix is prefix of reversed string)
            for char in reversed(word):
                if char not in curr:
                    curr[char] = {"best": i}
                curr = curr[char]
                # Update best index if current word is shorter
                best_idx = curr["best"]
                if word_len < len(wordsContainer[best_idx]):
                    curr["best"] = i

        results = []
        for query in wordsQuery:
            curr = root
            res_idx = root["best"]
            for char in reversed(query):
                if char in curr:
                    curr = curr[char]
                    res_idx = curr["best"]
                else:
                    break
            results.append(res_idx)

        return results
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class TrieNode:
    __slots__ = ['children', 'best_idx']
    def __init__(self, best_idx):
        self.children = [None] * 26
        self.best_idx = best_idx

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        n = len(wordsContainer)
        lengths = [len(w) for w in wordsContainer]

        best_overall_idx = 0
        for i in range(1, n):
            if lengths[i] < lengths[best_overall_idx]:
                best_overall_idx = i

        root = TrieNode(best_overall_idx)

        for i in range(n):
            word = wordsContainer[i]
            word_len = lengths[i]
            curr = root
            for char in reversed(word):
                idx = ord(char) - 97
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode(i)
                curr = curr.children[idx]
                if word_len < lengths[curr.best_idx]:
                    curr.best_idx = i

        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                idx = ord(char) - 97
                if curr.children[idx]:
                    curr = curr.children[idx]
                else:
                    break
            ans.append(curr.best_idx)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>

static int trie[500005][26];
static int bestIdxs[500005];

int* stringIndices(char** wordsContainer, int wordsContainerSize, char** wordsQuery, int wordsQuerySize, int* returnSize) {
    int* lengths = (int*)malloc(wordsContainerSize * sizeof(int));
    int bestOverallIdx = 0;
    for (int i = 0; i < wordsContainerSize; i++) {
        lengths[i] = (int)strlen(wordsContainer[i]);
        if (lengths[i] < lengths[bestOverallIdx]) {
            bestOverallIdx = i;
        }
    }

    for (int j = 0; j < 26; j++) trie[0][j] = -1;
    bestIdxs[0] = bestOverallIdx;
    int poolIdx = 1;

    for (int i = 0; i < wordsContainerSize; i++) {
        int len = lengths[i];
        int curr = 0;
        for (int j = len - 1; j >= 0; j--) {
            int charIdx = wordsContainer[i][j] - 'a';
            if (trie[curr][charIdx] == -1) {
                for (int k = 0; k < 26; k++) trie[poolIdx][k] = -1;
                bestIdxs[poolIdx] = i;
                trie[curr][charIdx] = poolIdx++;
            }
            curr = trie[curr][charIdx];
            if (len < lengths[bestIdxs[curr]]) {
                bestIdxs[curr] = i;
            }
        }
    }

    int* ans = (int*)malloc(wordsQuerySize * sizeof(int));
    *returnSize = wordsQuerySize;
    for (int i = 0; i < wordsQuerySize; i++) {
        int len = (int)strlen(wordsQuery[i]);
        int curr = 0;
        for (int j = len - 1; j >= 0; j--) {
            int charIdx = wordsQuery[i][j] - 'a';
            if (trie[curr][charIdx] == -1) break;
            curr = trie[curr][charIdx];
        }
        ans[i] = bestIdxs[curr];
    }

    free(lengths);
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
    private int[] trie = new int[500005 * 26];
    private int[] bestIdxs = new int[500005];

    public int[] StringIndices(string[] wordsContainer, string[] wordsQuery) {
        int n = wordsContainer.Length;
        int[] lengths = new int[n];
        int bestOverallIdx = 0;

        for (int i = 0; i < n; i++) {
            lengths[i] = wordsContainer[i].Length;
            if (lengths[i] < lengths[bestOverallIdx]) {
                bestOverallIdx = i;
            }
        }

        for (int j = 0; j < 26; j++) trie[j] = -1;
        bestIdxs[0] = bestOverallIdx;
        int poolIdx = 1;

        for (int i = 0; i < n; i++) {
            string word = wordsContainer[i];
            int len = lengths[i];
            int curr = 0;
            for (int j = len - 1; j >= 0; j--) {
                int charIdx = word[j] - 'a';
                int trieIdx = curr * 26 + charIdx;
                if (trie[trieIdx] == -1) {
                    int newNode = poolIdx++;
                    for (int k = 0; k < 26; k++) trie[newNode * 26 + k] = -1;
                    bestIdxs[newNode] = i;
                    trie[trieIdx] = newNode;
                }
                curr = trie[trieIdx];
                if (len < lengths[bestIdxs[curr]]) {
                    bestIdxs[curr] = i;
                }
            }
        }

        int[] result = new int[wordsQuery.Length];
        for (int i = 0; i < wordsQuery.Length; i++) {
            string query = wordsQuery[i];
            int curr = 0;
            for (int j = query.Length - 1; j >= 0; j--) {
                int charIdx = query[j] - 'a';
                int trieIdx = curr * 26 + charIdx;
                if (trie[trieIdx] == -1) break;
                curr = trie[trieIdx];
            }
            result[i] = bestIdxs[curr];
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
 * @param {string[]} wordsContainer
 * @param {string[]} wordsQuery
 * @return {number[]}
 */
var stringIndices = function(wordsContainer, wordsQuery) {
    const n = wordsContainer.length;
    const lengths = new Int32Array(n);
    let bestOverallIdx = 0;
    for (let i = 0; i < n; i++) {
        lengths[i] = wordsContainer[i].length;
        if (lengths[i] < lengths[bestOverallIdx]) {
            bestOverallIdx = i;
        }
    }

    const trie = new Int32Array(500005 * 26);
    const bestIdxs = new Int32Array(500005);
    trie.fill(-1, 0, 26);
    bestIdxs[0] = bestOverallIdx;
    let poolIdx = 1;

    for (let i = 0; i < n; i++) {
        const word = wordsContainer[i];
        const len = lengths[i];
        let curr = 0;
        for (let j = len - 1; j >= 0; j--) {
            const charIdx = word.charCodeAt(j) - 97;
            const trieIdx = curr * 26 + charIdx;
            if (trie[trieIdx] === -1) {
                const newNode = poolIdx++;
                trie.fill(-1, newNode * 26, newNode * 26 + 26);
                bestIdxs[newNode] = i;
                trie[trieIdx] = newNode;
            }
            curr = trie[trieIdx];
            if (len < lengths[bestIdxs[curr]]) {
                bestIdxs[curr] = i;
            }
        }
    }

    const m = wordsQuery.length;
    const ans = new Int32Array(m);
    for (let i = 0; i < m; i++) {
        const query = wordsQuery[i];
        let curr = 0;
        for (let j = query.length - 1; j >= 0; j--) {
            const charIdx = query.charCodeAt(j) - 97;
            const trieIdx = curr * 26 + charIdx;
            if (trie[trieIdx] === -1) break;
            curr = trie[trieIdx];
        }
        ans[i] = bestIdxs[curr];
    }

    return Array.from(ans);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function stringIndices(wordsContainer: string[], wordsQuery: string[]): number[] {
    class TrieNode {
        bestIdx: number;
        children: { [key: string]: TrieNode };
        constructor(bestIdx: number) {
            this.bestIdx = bestIdx;
            this.children = {};
        }
    }

    const n = wordsContainer.length;
    const lengths = wordsContainer.map(w => w.length);
    let globalBestIdx = 0;
    for (let i = 1; i < n; i++) {
        if (lengths[i] < lengths[globalBestIdx]) {
            globalBestIdx = i;
        }
    }

    const root = new TrieNode(globalBestIdx);

    for (let i = 0; i < n; i++) {
        const word = wordsContainer[i];
        const wordLen = lengths[i];
        let curr = root;
        for (let j = wordLen - 1; j >= 0; j--) {
            const char = word[j];
            if (!curr.children[char]) {
                curr.children[char] = new TrieNode(i);
            } else {
                const bestNodeIdx = curr.children[char].bestIdx;
                if (wordLen < lengths[bestNodeIdx]) {
                    curr.children[char].bestIdx = i;
                }
            }
            curr = curr.children[char];
        }
    }

    const results: number[] = [];
    for (const query of wordsQuery) {
        let curr = root;
        for (let j = query.length - 1; j >= 0; j--) {
            const char = query[j];
            if (!curr.children[char]) {
                break;
            }
            curr = curr.children[char];
        }
        results.push(curr.bestIdx);
    }

    return results;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class TrieNode {
    public $bestIdx;
    public $children = [];
    public function __construct($idx) {
        $this->bestIdx = $idx;
    }
}

class Solution {

    /**
     * @param String[] $wordsContainer
     * @param String[] $wordsQuery
     * @return Integer[]
     */
    function stringIndices($wordsContainer, $wordsQuery) {
        $n = count($wordsContainer);
        $lengths = [];
        $globalBestIdx = 0;

        for ($i = 0; $i < $n; $i++) {
            $lengths[$i] = strlen($wordsContainer[$i]);
            if ($lengths[$i] < $lengths[$globalBestIdx]) {
                $globalBestIdx = $i;
            }
        }

        $root = new TrieNode($globalBestIdx);

        for ($i = 0; $i < $n; $i++) {
            $word = $wordsContainer[$i];
            $wordLen = $lengths[$i];
            $curr = $root;
            for ($j = $wordLen - 1; $j >= 0; $j--) {
                $char = $word[$j];
                if (!isset($curr->children[$char])) {
                    $curr->children[$char] = new TrieNode($i);
                } else {
                    $best = $curr->children[$char]->bestIdx;
                    if ($wordLen < $lengths[$best]) {
                        $curr->children[$char]->bestIdx = $i;
                    }
                }
                $curr = $curr->children[$char];
            }
        }

        $results = [];
        foreach ($wordsQuery as $query) {
            $qLen = strlen($query);
            $curr = $root;
            for ($j = $qLen - 1; $j >= 0; $j--) {
                $char = $query[$j];
                if (!isset($curr->children[$char])) {
                    break;
                }
                $curr = $curr->children[$char];
            }
            $results[] = $curr->bestIdx;
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
class Solution {
    class TrieNode {
        var bestIdx: Int
        var children: [UInt8: TrieNode] = [:]
        init(bestIdx: Int) {
            self.bestIdx = bestIdx
        }
    }

    func stringIndices(_ wordsContainer: [String], _ wordsQuery: [String]) -> [Int] {
        let n = wordsContainer.count
        var lengths = [Int](repeating: 0, count: n)
        var globalBestIdx = 0

        for i in 0..<n {
            lengths[i] = wordsContainer[i].utf8.count
            if lengths[i] < lengths[globalBestIdx] {
                globalBestIdx = i
            }
        }

        let root = TrieNode(bestIdx: globalBestIdx)

        for i in 0..<n {
            let word = Array(wordsContainer[i].utf8)
            let wordLen = lengths[i]
            var curr = root
            for j in stride(from: wordLen - 1, through: 0, by: -1) {
                let charCode = word[j]
                if let next = curr.children[charCode] {
                    if wordLen < lengths[next.bestIdx] {
                        next.bestIdx = i
                    }
                    curr = next
                } else {
                    let newNode = TrieNode(bestIdx: i)
                    curr.children[charCode] = newNode
                    curr = newNode
                }
            }
        }

        var results = [Int]()
        results.reserveCapacity(wordsQuery.count)

        for query in wordsQuery {
            let queryBytes = Array(query.utf8)
            var curr = root
            for j in stride(from: queryBytes.count - 1, through: 0, by: -1) {
                let charCode = queryBytes[j]
                if let next = curr.children[charCode] {
                    curr = next
                } else {
                    break
                }
            }
            results.append(curr.bestIdx)
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
class Solution {
    class TrieNode(var bestIdx: Int) {
        val children = arrayOfNulls<TrieNode>(26)
    }

    fun stringIndices(wordsContainer: Array<String>, wordsQuery: Array<String>): IntArray {
        val n = wordsContainer.size
        val lengths = IntArray(n)
        var globalBestIdx = 0

        for (i in 0 until n) {
            lengths[i] = wordsContainer[i].length
            if (lengths[i] < lengths[globalBestIdx]) {
                globalBestIdx = i
            }
        }

        val root = TrieNode(globalBestIdx)

        for (i in 0 until n) {
            val word = wordsContainer[i]
            val wordLen = lengths[i]
            var curr = root
            for (j in wordLen - 1 downTo 0) {
                val charIdx = word[j] - 'a'
                if (curr.children[charIdx] == null) {
                    curr.children[charIdx] = TrieNode(i)
                } else {
                    val best = curr.children[charIdx]!!.bestIdx
                    if (wordLen < lengths[best]) {
                        curr.children[charIdx]!!.bestIdx = i
                    }
                }
                curr = curr.children[charIdx]!!
            }
        }

        val results = IntArray(wordsQuery.size)
        for (i in wordsQuery.indices) {
            val query = wordsQuery[i]
            var curr = root
            for (j in query.length - 1 downTo 0) {
                val charIdx = query[j] - 'a'
                if (curr.children[charIdx] == null) {
                    break
                }
                curr = curr.children[charIdx]!!
            }
            results[i] = curr.bestIdx
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
class TrieNode {
  int bestIdx;
  int bestLen;
  final List<TrieNode?> children = List.filled(26, null);
  TrieNode(this.bestIdx, this.bestLen);
}

class Solution {
  List<int> stringIndices(List<String> wordsContainer, List<String> wordsQuery) {
    TrieNode root = TrieNode(0, wordsContainer[0].length);

    for (int i = 0; i < wordsContainer.length; i++) {
      String word = wordsContainer[i];
      if (word.length < root.bestLen) {
        root.bestIdx = i;
        root.bestLen = word.length;
      }
      TrieNode curr = root;
      for (int j = word.length - 1; j >= 0; j--) {
        int code = word.codeUnitAt(j) - 97;
        if (curr.children[code] == null) {
          curr.children[code] = TrieNode(i, word.length);
        } else if (word.length < curr.children[code]!.bestLen) {
          curr.children[code]!.bestIdx = i;
          curr.children[code]!.bestLen = word.length;
        }
        curr = curr.children[code]!;
      }
    }

    List<int> ans = List.filled(wordsQuery.length, 0);
    for (int i = 0; i < wordsQuery.length; i++) {
      String query = wordsQuery[i];
      TrieNode curr = root;
      for (int j = query.length - 1; j >= 0; j--) {
        int code = query.codeUnitAt(j) - 97;
        if (curr.children[code] == null) {
          break;
        }
        curr = curr.children[code]!;
      }
      ans[i] = curr.bestIdx;
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
func stringIndices(wordsContainer []string, wordsQuery []string) []int {
	type TrieNode struct {
		children [26]*TrieNode
		bestIdx  int
		bestLen  int
	}

	root := &TrieNode{bestIdx: 0, bestLen: len(wordsContainer[0])}

	for i, word := range wordsContainer {
		if len(word) < root.bestLen {
			root.bestIdx = i
			root.bestLen = len(word)
		}
		curr := root
		for j := len(word) - 1; j >= 0; j-- {
			c := word[j] - 'a'
			if curr.children[c] == nil {
				curr.children[c] = &TrieNode{bestIdx: i, bestLen: len(word)}
			} else if len(word) < curr.children[c].bestLen {
				curr.children[c].bestIdx = i
				curr.children[c].bestLen = len(word)
			}
			curr = curr.children[c]
		}
	}

	ans := make([]int, len(wordsQuery))
	for i, query := range wordsQuery {
		curr := root
		for j := len(query) - 1; j >= 0; j-- {
			c := query[j] - 'a'
			if curr.children[c] == nil {
				break
			}
			curr = curr.children[c]
		}
		ans[i] = curr.bestIdx
	}

	return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class TrieNode
  attr_accessor :best_idx, :best_len, :children
  def initialize(idx, len)
    @best_idx = idx
    @best_len = len
    @children = Array.new(26)
  end
end

# @param {String[]} words_container
# @param {String[]} words_query
# @return {Integer[]}
def string_indices(words_container, words_query)
  root = TrieNode.new(0, words_container[0].length)

  words_container.each_with_index do |word, i|
    w_len = word.length
    if w_len < root.best_len
      root.best_idx = i
      root.best_len = w_len
    end

    curr = root
    (w_len - 1).downto(0) do |j|
      code = word.getbyte(j) - 97
      if curr.children[code].nil?
        curr.children[code] = TrieNode.new(i, w_len)
      elsif w_len < curr.children[code].best_len
        curr.children[code].best_idx = i
        curr.children[code].best_len = w_len
      end
      curr = curr.children[code]
    end
  end

  words_query.map do |query|
    curr = root
    (query.length - 1).downto(0) do |j|
      code = query.getbyte(j) - 97
      if code < 0 || code >= 26 || curr.children[code].nil?
        break
      end
      curr = curr.children[code]
    end
    curr.best_idx
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    class TrieNode(var bestIdx: Int, var bestLen: Int) {
        val children: Array[TrieNode] = new Array[TrieNode](26)
    }

    def stringIndices(wordsContainer: Array[String], wordsQuery: Array[String]): Array[Int] = {
        val root = new TrieNode(0, wordsContainer(0).length)

        var i = 0
        while (i < wordsContainer.length) {
            val word = wordsContainer(i)
            val wLen = word.length
            if (wLen < root.bestLen) {
                root.bestIdx = i
                root.bestLen = wLen
            }
            var curr = root
            var j = wLen - 1
            while (j >= 0) {
                val c = word(j) - 'a'
                if (curr.children(c) == null) {
                    curr.children(c) = new TrieNode(i, wLen)
                } else if (wLen < curr.children(c).bestLen) {
                    curr.children(c).bestIdx = i
                    curr.children(c).bestLen = wLen
                }
                curr = curr.children(c)
                j -= 1
            }
            i += 1
        }

        val ans = new Array[Int](wordsQuery.length)
        var qIdx = 0
        while (qIdx < wordsQuery.length) {
            val query = wordsQuery(qIdx)
            var curr = root
            var j = query.length - 1
            while (j >= 0) {
                val c = query(j) - 'a'
                if (c < 0 || c >= 26 || curr.children(c) == null) {
                    j = -1
                } else {
                    curr = curr.children(c)
                    j -= 1
                }
            }
            ans(qIdx) = curr.bestIdx
            qIdx += 1
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
    pub fn string_indices(words_container: Vec<String>, words_query: Vec<String>) -> Vec<i32> {
        let n = words_container.len();
        let lengths: Vec<usize> = words_container.iter().map(|s| s.len()).collect();

        let mut global_best_idx = 0;
        for i in 1..n {
            if lengths[i] < lengths[global_best_idx] {
                global_best_idx = i;
            } else if lengths[i] == lengths[global_best_idx] {
                if i < global_best_idx {
                    global_best_idx = i;
                }
            }
        }

        struct Node {
            children: [i32; 26],
            best_idx: i32,
        }

        let mut trie = vec![Node {
            children: [-1; 26],
            best_idx: global_best_idx as i32,
        }];

        for (i, word) in words_container.iter().enumerate() {
            let mut curr = 0;
            let i_len = lengths[i];
            let i_val = i as i32;

            let root_best = trie[0].best_idx as usize;
            if i_len < lengths[root_best] || (i_len == lengths[root_best] && i < root_best) {
                trie[0].best_idx = i_val;
            }

            for &b in word.as_bytes().iter().rev() {
                let c = (b - b'a') as usize;
                if trie[curr].children[c] == -1 {
                    let new_node_idx = trie.len() as i32;
                    trie.push(Node {
                        children: [-1; 26],
                        best_idx: i_val,
                    });
                    trie[curr].children[c] = new_node_idx;
                }
                curr = trie[curr].children[c] as usize;
                let curr_best = trie[curr].best_idx as usize;
                if i_len < lengths[curr_best] || (i_len == lengths[curr_best] && i < curr_best) {
                    trie[curr].best_idx = i_val;
                }
            }
        }

        words_query
            .into_iter()
            .map(|query| {
                let mut curr = 0;
                for &b in query.as_bytes().iter().rev() {
                    let c = (b - b'a') as usize;
                    if trie[curr].children[c] == -1 {
                        break;
                    }
                    curr = trie[curr].children[c] as usize;
                }
                trie[curr].best_idx
            })
            .collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(struct trie-node ([best-idx #:mutable] [children #:mutable]))

(define/contract (string-indices wordsContainer wordsQuery)
  (-> (listof string?) (listof string?) (listof exact-integer?))
  (let* ([n (length wordsContainer)]
         [words-vec (list->vector wordsContainer)]
         [lengths (vector-map string-length words-vec)])

    (define (better? idx1 idx2)
      (let ([len1 (vector-ref lengths idx1)]
            [len2 (vector-ref lengths idx2)])
        (or (< len1 len2)
            (and (= len1 len2) (< idx1 idx2)))))

    (define global-best-idx
      (let loop ([i 1] [best 0])
        (if (>= i n)
            best
            (if (better? i best)
                (loop (+ i 1) i)
                (loop (+ i 1) best)))))

    (define root (trie-node global-best-idx (make-vector 26 #f)))

    (for ([i (in-range n)])
      (let* ([word (vector-ref words-vec i)]
             [chars (reverse (string->list word))])
        (let loop ([cs chars] [curr root])
          (when (better? i (trie-node-best-idx curr))
            (set-trie-node-best-idx! curr i))
          (unless (null? cs)
            (let* ([c-idx (- (char->integer (car cs)) 97)]
                   [children (trie-node-children curr)])
              (unless (vector-ref children c-idx)
                (vector-set! children c-idx (trie-node i (make-vector 26 #f))))
              (loop (cdr cs) (vector-ref children c-idx)))))))

    (map (lambda (query)
           (let* ([chars (reverse (string->list query))])
             (let loop ([cs chars] [curr root])
               (if (null? cs)
                   (trie-node-best-idx curr)
                   (let* ([c-idx (- (char->integer (car cs)) 97)]
                          [next (vector-ref (trie-node-children curr) c-idx)])
                     (if next
                         (loop (cdr cs) next)
                         (trie-node-best-idx curr)))))))
         wordsQuery)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec string_indices(WordsContainer :: [unicode:unicode_binary()], WordsQuery :: [unicode:unicode_binary()]) -> [integer()].
string_indices(WordsContainer, WordsQuery) ->
    LengthsList = [byte_size(W) || W <- WordsContainer],
    Lengths = list_to_tuple(LengthsList),
    N = tuple_size(Lengths),
    GlobalBestIdx = find_global_best(1, 0, N, Lengths),
    Enumerate = lists:zip(WordsContainer, lists:seq(0, N - 1)),
    Trie = lists:foldl(fun({Word, Idx}, T) ->
        insert(list_to_binary(lists:reverse(binary_to_list(Word))), Idx, T, Lengths)
    end, {node, GlobalBestIdx, #{}}, Enumerate),
    [query_trie(list_to_binary(lists:reverse(binary_to_list(Q))), Trie) || Q <- WordsQuery].

find_global_best(I, Best, N, Lengths) when I =:= N -> Best;
find_global_best(I, Best, N, Lengths) ->
    case is_better(I, Best, Lengths) of
        true -> find_global_best(I + 1, I, N, Lengths);
        false -> find_global_best(I + 1, Best, N, Lengths)
    end.

is_better(NewIdx, CurIdx, Lengths) ->
    L1 = element(NewIdx + 1, Lengths),
    L2 = element(CurIdx + 1, Lengths),
    (L1 < L2) orelse (L1 =:= L2 andalso NewIdx < CurIdx).

insert(<<>>, Idx, {node, BestIdx, Children}, Lengths) ->
    NewBest = if is_better(Idx, BestIdx, Lengths) -> Idx; true -> BestIdx end,
    {node, NewBest, Children};
insert(<<C, Rest/binary>>, Idx, {node, BestIdx, Children}, Lengths) ->
    NewBestIdx = if is_better(Idx, BestIdx, Lengths) -> Idx; true -> BestIdx end,
    Child = maps:get(C, Children, {node, Idx, #{}}),
    NewChild = insert(Rest, Idx, Child, Lengths),
    {node, NewBestIdx, maps:put(C, NewChild, Children)}.

query_trie(<<C, Rest/binary>>, {node, BestIdx, Children}) ->
    case maps:get(C, Children, undefined) of
        undefined -> BestIdx;
        NextNode -> query_trie(Rest, NextNode)
    end;
query_trie(<<>>, {node, BestIdx, _}) -> BestIdx.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec string_indices(words_container :: [String.t], words_query :: [String.t]) :: [integer]
  def string_indices(words_container, words_query) do
    lengths_list = Enum.map(words_container, &byte_size/1)
    lengths = List.to_tuple(lengths_list)
    n = tuple_size(lengths)

    global_best_idx = 
      Enum.reduce(1..(n - 1)//1, 0, fn i, best ->
        if is_better(i, best, lengths), do: i, else: best
      end)

    trie = 
      words_container
      |> Enum.with_index()
      |> Enum.reduce({global_best_idx, %{}}, fn {word, idx}, trie ->
        insert(String.reverse(word), idx, trie, lengths)
      end)

    Enum.map(words_query, fn query ->
      query_trie(String.reverse(query), trie)
    end)
  end

  defp is_better(new_idx, cur_idx, lengths) do
    l1 = elem(lengths, new_idx)
    l2 = elem(lengths, cur_idx)
    l1 < l2 or (l1 == l2 and new_idx < cur_idx)
  end

  defp insert(<<>>, idx, {best_idx, children}, lengths) do
    new_best = if is_better(idx, best_idx, lengths), do: idx, else: best_idx
    {new_best, children}
  end

  defp insert(<<c, rest::binary>>, idx, {best_idx, children}, lengths) do
    new_best = if is_better(idx, best_idx, lengths), do: idx, else: best_idx
    child = Map.get(children, c, {idx, %{}})
    new_child = insert(rest, idx, child, lengths)
    {new_best, Map.put(children, c, new_child)}
  end

  defp query_trie(<<c, rest::binary>>, {best_idx, children}) do
    case Map.get(children, c) do
      nil -> best_idx
      next_node -> query_trie(rest, next_node)
    end
  end

  defp query_trie(<<>>, {best_idx, _children}) do
    best_idx
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + M) where N is the sum of lengths of all strings in 'wordsContainer' and M is the sum of lengths of all strings in 'wordsQuery'. Building the Trie involves iterating through each character of every word in 'wordsContainer' once, and querying involves iterating through each character of every word in 'wordsQuery' once.
- **Space Complexity:** O(N × Σ) where N is the sum of lengths of all strings in 'wordsContainer' and Σ is the alphabet size (26). Each character in 'wordsContainer' can potentially create a new node in the Trie, and each node stores a fixed-size array or map for its children and an integer index.
