---
layout: post
title: "Longest Substring of One Repeating Character"
date: 2026-08-13 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "String", "Segment Tree", "Ordered Set"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/longest-substring-of-one-repeating-character/
ai_solutions:
  - solutions:
      cpp: "class Solution {\n    struct Node {\n        int maxLen, prefLen, suffLen,\
        \ sz;\n        char lc, rc;\n    };\n    vector<Node> tree;\n\n    void pull(int\
        \ node) {\n        int l = 2 * node, r = 2 * node + 1;\n        tree[node].sz\
        \ = tree[l].sz + tree[r].sz;\n        tree[node].lc = tree[l].lc;\n        tree[node].rc\
        \ = tree[r].rc;\n        tree[node].maxLen = max(tree[l].maxLen, tree[r].maxLen);\n\
        \        tree[node].prefLen = tree[l].prefLen;\n        tree[node].suffLen =\
        \ tree[r].suffLen;\n        if (tree[l].rc == tree[r].lc) {\n            tree[node].maxLen\
        \ = max(tree[node].maxLen, tree[l].suffLen + tree[r].prefLen);\n           \
        \ if (tree[l].prefLen == tree[l].sz) tree[node].prefLen = tree[l].sz + tree[r].prefLen;\n\
        \            if (tree[r].suffLen == tree[r].sz) tree[node].suffLen = tree[r].sz\
        \ + tree[l].suffLen;\n        }\n    }\n\n    void build(int node, int start,\
        \ int end, const string& s) {\n        if (start == end) {\n            tree[node]\
        \ = {1, 1, 1, 1, s[start], s[start]};\n            return;\n        }\n    \
        \    int mid = (start + end) / 2;\n        build(2 * node, start, mid, s);\n\
        \        build(2 * node + 1, mid + 1, end, s);\n        pull(node);\n    }\n\
        \n    void update(int node, int start, int end, int idx, char c) {\n       \
        \ if (start == end) {\n            tree[node].lc = tree[node].rc = c;\n    \
        \        return;\n        }\n        int mid = (start + end) / 2;\n        if\
        \ (idx <= mid) update(2 * node, start, mid, idx, c);\n        else update(2\
        \ * node + 1, mid + 1, end, idx, c);\n        pull(node);\n    }\n\npublic:\n\
        \    vector<int> longestRepeating(string s, string queryCharacters, vector<int>&\
        \ queryIndices) {\n        int n = s.length();\n        int k = queryIndices.size();\n\
        \        tree.resize(4 * n + 1);\n        build(1, 0, n - 1, s);\n        vector<int>\
        \ result(k);\n        for (int i = 0; i < k; i++) {\n            update(1, 0,\
        \ n - 1, queryIndices[i], queryCharacters[i]);\n            result[i] = tree[1].maxLen;\n\
        \        }\n        return result;\n    }\n};"
      java: "class Solution {\n    int[] maxLen, prefLen, suffLen, sz;\n    char[] lc,\
        \ rc;\n\n    private void pull(int node) {\n        int l = 2 * node, r = 2\
        \ * node + 1;\n        lc[node] = lc[l];\n        rc[node] = rc[r];\n      \
        \  sz[node] = sz[l] + sz[r];\n        maxLen[node] = Math.max(maxLen[l], maxLen[r]);\n\
        \        prefLen[node] = prefLen[l];\n        suffLen[node] = suffLen[r];\n\
        \        if (rc[l] == lc[r]) {\n            maxLen[node] = Math.max(maxLen[node],\
        \ suffLen[l] + prefLen[r]);\n            if (prefLen[l] == sz[l]) prefLen[node]\
        \ = sz[l] + prefLen[r];\n            if (suffLen[r] == sz[r]) suffLen[node]\
        \ = sz[r] + suffLen[l];\n        }\n    }\n\n    private void build(int node,\
        \ int start, int end, char[] s) {\n        if (start == end) {\n           \
        \ maxLen[node] = prefLen[node] = suffLen[node] = sz[node] = 1;\n           \
        \ lc[node] = rc[node] = s[start];\n            return;\n        }\n        int\
        \ mid = (start + end) / 2;\n        build(2 * node, start, mid, s);\n      \
        \  build(2 * node + 1, mid + 1, end, s);\n        pull(node);\n    }\n\n   \
        \ private void update(int node, int start, int end, int idx, char c) {\n   \
        \     if (start == end) {\n            lc[node] = rc[node] = c;\n          \
        \  return;\n        }\n        int mid = (start + end) / 2;\n        if (idx\
        \ <= mid) update(2 * node, start, mid, idx, c);\n        else update(2 * node\
        \ + 1, mid + 1, end, idx, c);\n        pull(node);\n    }\n\n    public int[]\
        \ longestRepeating(String s, String queryCharacters, int[] queryIndices) {\n\
        \        int n = s.length();\n        int k = queryIndices.length;\n       \
        \ maxLen = new int[4 * n];\n        prefLen = new int[4 * n];\n        suffLen\
        \ = new int[4 * n];\n        sz = new int[4 * n];\n        lc = new char[4 *\
        \ n];\n        rc = new char[4 * n];\n\n        char[] sArr = s.toCharArray();\n\
        \        build(1, 0, n - 1, sArr);\n\n        int[] results = new int[k];\n\
        \        char[] qChars = queryCharacters.toCharArray();\n        for (int i\
        \ = 0; i < k; i++) {\n            update(1, 0, n - 1, queryIndices[i], qChars[i]);\n\
        \            results[i] = maxLen[1];\n        }\n        return results;\n \
        \   }\n}"
      python: "class Solution(object):\n    def longestRepeating(self, s, queryCharacters,\
        \ queryIndices):\n        \"\"\"\n        :type s: str\n        :type queryCharacters:\
        \ str\n        :type queryIndices: List[int]\n        :rtype: List[int]\n  \
        \      \"\"\"\n        n = len(s)\n        size = 1\n        while size < n:\
        \ \n            size *= 2\n\n        max_l = [0] * (2 * size)\n        pre_l\
        \ = [0] * (2 * size)\n        suf_l = [0] * (2 * size)\n        lc = [''] *\
        \ (2 * size)\n        rc = [''] * (2 * size)\n        sz = [0] * (2 * size)\n\
        \n        for i in range(n):\n            idx = size + i\n            max_l[idx]\
        \ = pre_l[idx] = suf_l[idx] = 1\n            lc[idx] = rc[idx] = s[i]\n    \
        \        sz[idx] = 1\n\n        for i in range(size - 1, 0, -1):\n         \
        \   l, r = i << 1, i << 1 | 1\n            sz_l, sz_r = sz[l], sz[r]\n     \
        \       sz[i] = sz_l + sz_r\n            if sz[i] == 0: continue\n         \
        \   if sz_r == 0:\n                max_l[i], pre_l[i], suf_l[i], lc[i], rc[i]\
        \ = max_l[l], pre_l[l], suf_l[l], lc[l], rc[l]\n            else:\n        \
        \        lc_l, rc_l = lc[l], rc[l]\n                lc_r, rc_r = lc[r], rc[r]\n\
        \                ml_l, ml_r = max_l[l], max_l[r]\n                pl_l, sl_l\
        \ = pre_l[l], suf_l[l]\n                pl_r, sl_r = pre_l[r], suf_l[r]\n  \
        \              res = ml_l if ml_l > ml_r else ml_r\n                pl, sl =\
        \ pl_l, sl_r\n                if rc_l == lc_r:\n                    comb = sl_l\
        \ + pl_r\n                    if comb > res: res = comb\n                  \
        \  if pl_l == sz_l: pl = sz_l + pl_r\n                    if sl_r == sz_r: sl\
        \ = sz_r + sl_l\n                max_l[i], pre_l[i], suf_l[i], lc[i], rc[i]\
        \ = res, pl, sl, lc_l, rc_r\n\n        ans = []\n        for char, idx_s in\
        \ zip(queryCharacters, queryIndices):\n            idx = size + idx_s\n    \
        \        lc[idx] = rc[idx] = char\n            idx >>= 1\n            while\
        \ idx >= 1:\n                l, r = idx << 1, idx << 1 | 1\n               \
        \ sz_l, sz_r = sz[l], sz[r]\n                if sz_r == 0:\n               \
        \     max_l[idx], pre_l[idx], suf_l[idx], lc[idx], rc[idx] = max_l[l], pre_l[l],\
        \ suf_l[l], lc[l], rc[l]\n                else:\n                    lc_l, rc_l,\
        \ lc_r, rc_r = lc[l], rc[l], lc[r], rc[r]\n                    ml_l, ml_r, pl_l,\
        \ sl_l, pl_r, sl_r = max_l[l], max_l[r], pre_l[l], suf_l[l], pre_l[r], suf_l[r]\n\
        \                    res = ml_l if ml_l > ml_r else ml_r\n                 \
        \   pl, sl = pl_l, sl_r\n                    if rc_l == lc_r:\n            \
        \            comb = sl_l + pl_r\n                        if comb > res: res\
        \ = comb\n                        if pl_l == sz_l: pl = sz_l + pl_r\n      \
        \                  if sl_r == sz_r: sl = sz_r + sl_l\n                    max_l[idx],\
        \ pre_l[idx], suf_l[idx], lc[idx], rc[idx] = res, pl, sl, lc_l, rc_r\n     \
        \           idx >>= 1\n            ans.append(max_l[1])\n        return ans"
      python3: "class Solution:\n    def longestRepeating(self, s: str, queryCharacters:\
        \ str, queryIndices: List[int]) -> List[int]:\n        n = len(s)\n        m\
        \ = 1 << (n - 1).bit_length()\n\n        max_len = [0] * (2 * m)\n        pre_len\
        \ = [0] * (2 * m)\n        suf_len = [0] * (2 * m)\n        pre_char = [0] *\
        \ (2 * m)\n        suf_char = [0] * (2 * m)\n        size = [0] * (2 * m)\n\n\
        \        for i in range(n):\n            idx = m + i\n            max_len[idx]\
        \ = pre_len[idx] = suf_len[idx] = 1\n            pre_char[idx] = suf_char[idx]\
        \ = ord(s[i])\n            size[idx] = 1\n\n        def push_up(idx):\n    \
        \        lc, rc = 2 * idx, 2 * idx + 1\n            slc, src = size[lc], size[rc]\n\
        \n            if slc == 0:\n                max_len[idx], pre_len[idx], suf_len[idx]\
        \ = max_len[rc], pre_len[rc], suf_len[rc]\n                pre_char[idx], suf_char[idx],\
        \ size[idx] = pre_char[rc], suf_char[rc], src\n            elif src == 0:\n\
        \                max_len[idx], pre_len[idx], suf_len[idx] = max_len[lc], pre_len[lc],\
        \ suf_len[lc]\n                pre_char[idx], suf_char[idx], size[idx] = pre_char[lc],\
        \ suf_char[lc], slc\n            else:\n                size[idx] = slc + src\n\
        \                l_pc, r_pc, l_sc, r_sc = pre_char[lc], pre_char[rc], suf_char[lc],\
        \ suf_char[rc]\n                pre_char[idx], suf_char[idx] = l_pc, r_sc\n\n\
        \                p_len = pre_len[lc]\n                if p_len == slc and l_pc\
        \ == r_pc:\n                    p_len += pre_len[rc]\n                pre_len[idx]\
        \ = p_len\n\n                s_len = suf_len[rc]\n                if s_len ==\
        \ src and r_sc == l_sc:\n                    s_len += suf_len[lc]\n        \
        \        suf_len[idx] = s_len\n\n                m_len = max_len[lc] if max_len[lc]\
        \ > max_len[rc] else max_len[rc]\n                if l_sc == r_pc:\n       \
        \             combined = suf_len[lc] + pre_len[rc]\n                    if combined\
        \ > m_len: m_len = combined\n                max_len[idx] = m_len\n\n      \
        \  for i in range(m - 1, 0, -1):\n            push_up(i)\n\n        ans = []\n\
        \        q_chars = [ord(c) for c in queryCharacters]\n        for i, char_code\
        \ in zip(queryIndices, q_chars):\n            idx = m + i\n            pre_char[idx]\
        \ = suf_char[idx] = char_code\n            idx >>= 1\n            while idx\
        \ > 0:\n                push_up(idx)\n                idx >>= 1\n          \
        \  ans.append(max_len[1])\n        return ans"
      c: "#include <stdlib.h>\n#include <string.h>\n#include <math.h>\n\ntypedef struct\
        \ {\n    int maxLen;\n    int preLen;\n    int sufLen;\n    char preChar;\n\
        \    char sufChar;\n    int size;\n} Node;\n\nvoid push_up(Node* tree, int idx)\
        \ {\n    int lc = 2 * idx;\n    int rc = 2 * idx + 1;\n    if (tree[lc].size\
        \ == 0) {\n        tree[idx] = tree[rc];\n    } else if (tree[rc].size == 0)\
        \ {\n        tree[idx] = tree[lc];\n    } else {\n        tree[idx].size = tree[lc].size\
        \ + tree[rc].size;\n        tree[idx].preChar = tree[lc].preChar;\n        tree[idx].sufChar\
        \ = tree[rc].sufChar;\n\n        int pLen = tree[lc].preLen;\n        if (pLen\
        \ == tree[lc].size && tree[lc].preChar == tree[rc].preChar) {\n            pLen\
        \ += tree[rc].preLen;\n        }\n        tree[idx].preLen = pLen;\n\n     \
        \   int sLen = tree[rc].sufLen;\n        if (sLen == tree[rc].size && tree[rc].sufChar\
        \ == tree[lc].sufChar) {\n            sLen += tree[lc].sufLen;\n        }\n\
        \        tree[idx].sufLen = sLen;\n\n        int mLen = tree[lc].maxLen > tree[rc].maxLen\
        \ ? tree[lc].maxLen : tree[rc].maxLen;\n        if (tree[lc].sufChar == tree[rc].preChar)\
        \ {\n            int combined = tree[lc].sufLen + tree[rc].preLen;\n       \
        \     if (combined > mLen) mLen = combined;\n        }\n        tree[idx].maxLen\
        \ = mLen;\n    }\n}\n\nint* longestRepeating(char* s, char* queryCharacters,\
        \ int* queryIndices, int queryIndicesSize, int* returnSize) {\n    int n = strlen(s);\n\
        \    int M = 1;\n    while (M < n) M <<= 1;\n\n    Node* tree = (Node*)calloc(2\
        \ * M, sizeof(Node));\n    for (int i = 0; i < n; i++) {\n        int idx =\
        \ M + i;\n        tree[idx].maxLen = tree[idx].preLen = tree[idx].sufLen = 1;\n\
        \        tree[idx].preChar = tree[idx].sufChar = s[i];\n        tree[idx].size\
        \ = 1;\n    }\n    for (int i = M - 1; i > 0; i--) {\n        push_up(tree,\
        \ i);\n    }\n\n    int* lengths = (int*)malloc(queryIndicesSize * sizeof(int));\n\
        \    for (int i = 0; i < queryIndicesSize; i++) {\n        int idx = M + queryIndices[i];\n\
        \        tree[idx].preChar = tree[idx].sufChar = queryCharacters[i];\n     \
        \   idx >>= 1;\n        while (idx > 0) {\n            push_up(tree, idx);\n\
        \            idx >>= 1;\n        }\n        lengths[i] = tree[1].maxLen;\n \
        \   }\n\n    free(tree);\n    *returnSize = queryIndicesSize;\n    return lengths;\n\
        }"
      csharp: "public class Solution {\n    private struct Node {\n        public int\
        \ maxLen;\n        public int preLen;\n        public int sufLen;\n        public\
        \ int size;\n        public char preChar;\n        public char sufChar;\n  \
        \  }\n\n    private void PushUp(Node[] tree, int idx) {\n        int lc = 2\
        \ * idx;\n        int rc = 2 * idx + 1;\n        if (tree[lc].size == 0) {\n\
        \            tree[idx] = tree[rc];\n        } else if (tree[rc].size == 0) {\n\
        \            tree[idx] = tree[lc];\n        } else {\n            tree[idx].size\
        \ = tree[lc].size + tree[rc].size;\n            tree[idx].preChar = tree[lc].preChar;\n\
        \            tree[idx].sufChar = tree[rc].sufChar;\n\n            int pLen =\
        \ tree[lc].preLen;\n            if (pLen == tree[lc].size && tree[lc].preChar\
        \ == tree[rc].preChar) {\n                pLen += tree[rc].preLen;\n       \
        \     }\n            tree[idx].preLen = pLen;\n\n            int sLen = tree[rc].sufLen;\n\
        \            if (sLen == tree[rc].size && tree[rc].sufChar == tree[lc].sufChar)\
        \ {\n                sLen += tree[lc].sufLen;\n            }\n            tree[idx].sufLen\
        \ = sLen;\n\n            int mLen = tree[lc].maxLen > tree[rc].maxLen ? tree[lc].maxLen\
        \ : tree[rc].maxLen;\n            if (tree[lc].sufChar == tree[rc].preChar)\
        \ {\n                int combined = tree[lc].sufLen + tree[rc].preLen;\n   \
        \             if (combined > mLen) mLen = combined;\n            }\n       \
        \     tree[idx].maxLen = mLen;\n        }\n    }\n\n    public int[] LongestRepeating(string\
        \ s, string queryCharacters, int[] queryIndices) {\n        int n = s.Length;\n\
        \        int M = 1;\n        while (M < n) M <<= 1;\n\n        Node[] tree =\
        \ new Node[2 * M];\n        for (int i = 0; i < n; i++) {\n            int idx\
        \ = M + i;\n            tree[idx].maxLen = tree[idx].preLen = tree[idx].sufLen\
        \ = 1;\n            tree[idx].preChar = tree[idx].sufChar = s[i];\n        \
        \    tree[idx].size = 1;\n        }\n        for (int i = M - 1; i > 0; i--)\
        \ {\n            PushUp(tree, i);\n        }\n\n        int k = queryIndices.Length;\n\
        \        int[] results = new int[k];\n        for (int i = 0; i < k; i++) {\n\
        \            int idx = M + queryIndices[i];\n            tree[idx].preChar =\
        \ tree[idx].sufChar = queryCharacters[i];\n            idx >>= 1;\n        \
        \    while (idx > 0) {\n                PushUp(tree, idx);\n               \
        \ idx >>= 1;\n            }\n            results[i] = tree[1].maxLen;\n    \
        \    }\n\n        return results;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {string} queryCharacters\n *\
        \ @param {number[]} queryIndices\n * @return {number[]}\n */\nvar longestRepeating\
        \ = function(s, queryCharacters, queryIndices) {\n    const n = s.length;\n\
        \    let m = 1;\n    while (m < n) m <<= 1;\n\n    const maxLen = new Int32Array(2\
        \ * m);\n    const preLen = new Int32Array(2 * m);\n    const sufLen = new Int32Array(2\
        \ * m);\n    const preChar = new Uint8Array(2 * m);\n    const sufChar = new\
        \ Uint8Array(2 * m);\n    const size = new Int32Array(2 * m);\n\n    function\
        \ pushUp(idx) {\n        const lc = idx << 1;\n        const rc = lc | 1;\n\
        \        const slc = size[lc];\n        const src = size[rc];\n\n        if\
        \ (slc === 0) {\n            maxLen[idx] = maxLen[rc];\n            preLen[idx]\
        \ = preLen[rc];\n            sufLen[idx] = sufLen[rc];\n            preChar[idx]\
        \ = preChar[rc];\n            sufChar[idx] = sufChar[rc];\n            size[idx]\
        \ = src;\n        } else if (src === 0) {\n            maxLen[idx] = maxLen[lc];\n\
        \            preLen[idx] = preLen[lc];\n            sufLen[idx] = sufLen[lc];\n\
        \            preChar[idx] = preChar[lc];\n            sufChar[idx] = sufChar[lc];\n\
        \            size[idx] = slc;\n        } else {\n            size[idx] = slc\
        \ + src;\n            const lpc = preChar[lc], rpc = preChar[rc], lsc = sufChar[lc],\
        \ rsc = sufChar[rc];\n            preChar[idx] = lpc;\n            sufChar[idx]\
        \ = rsc;\n\n            let pLen = preLen[lc];\n            if (pLen === slc\
        \ && lpc === rpc) pLen += preLen[rc];\n            preLen[idx] = pLen;\n\n \
        \           let sLen = sufLen[rc];\n            if (sLen === src && rsc ===\
        \ lsc) sLen += sufLen[lc];\n            sufLen[idx] = sLen;\n\n            let\
        \ mLen = maxLen[lc] > maxLen[rc] ? maxLen[lc] : maxLen[rc];\n            if\
        \ (lsc === rpc) {\n                const combined = sufLen[lc] + preLen[rc];\n\
        \                if (combined > mLen) mLen = combined;\n            }\n    \
        \        maxLen[idx] = mLen;\n        }\n    }\n\n    for (let i = 0; i < n;\
        \ i++) {\n        const idx = m + i;\n        maxLen[idx] = preLen[idx] = sufLen[idx]\
        \ = 1;\n        preChar[idx] = sufChar[idx] = s.charCodeAt(i);\n        size[idx]\
        \ = 1;\n    }\n    for (let i = m - 1; i > 0; i--) {\n        pushUp(i);\n \
        \   }\n\n    const k = queryIndices.length;\n    const result = new Int32Array(k);\n\
        \    for (let i = 0; i < k; i++) {\n        let idx = m + queryIndices[i];\n\
        \        preChar[idx] = sufChar[idx] = queryCharacters.charCodeAt(i);\n    \
        \    idx >>= 1;\n        while (idx > 0) {\n            pushUp(idx);\n     \
        \       idx >>= 1;\n        }\n        result[i] = maxLen[1];\n    }\n\n   \
        \ return Array.from(result);\n};"
      typescript: "function longestRepeating(s: string, queryCharacters: string, queryIndices:\
        \ number[]): number[] {\n    const n = s.length;\n    const maxLen = new Int32Array(4\
        \ * n + 1);\n    const prefixLen = new Int32Array(4 * n + 1);\n    const suffixLen\
        \ = new Int32Array(4 * n + 1);\n    const leftChar = new Int32Array(4 * n +\
        \ 1);\n    const rightChar = new Int32Array(4 * n + 1);\n\n    function merge(node:\
        \ number, left: number, right: number, lLen: number, rLen: number) {\n     \
        \   maxLen[node] = Math.max(maxLen[left], maxLen[right]);\n        leftChar[node]\
        \ = leftChar[left];\n        rightChar[node] = rightChar[right];\n        prefixLen[node]\
        \ = prefixLen[left];\n        suffixLen[node] = suffixLen[right];\n\n      \
        \  if (rightChar[left] === leftChar[right]) {\n            const combined =\
        \ suffixLen[left] + prefixLen[right];\n            if (combined > maxLen[node])\
        \ maxLen[node] = combined;\n            if (prefixLen[left] === lLen) prefixLen[node]\
        \ = lLen + prefixLen[right];\n            if (suffixLen[right] === rLen) suffixLen[node]\
        \ = rLen + suffixLen[left];\n        }\n    }\n\n    function build(node: number,\
        \ start: number, end: number) {\n        if (start === end) {\n            const\
        \ code = s.charCodeAt(start);\n            maxLen[node] = 1;\n            prefixLen[node]\
        \ = 1;\n            suffixLen[node] = 1;\n            leftChar[node] = code;\n\
        \            rightChar[node] = code;\n            return;\n        }\n     \
        \   const mid = (start + end) >> 1;\n        build(2 * node, start, mid);\n\
        \        build(2 * node + 1, mid + 1, end);\n        merge(node, 2 * node, 2\
        \ * node + 1, mid - start + 1, end - mid);\n    }\n\n    function update(node:\
        \ number, start: number, end: number, idx: number, charCode: number) {\n   \
        \     if (start === end) {\n            leftChar[node] = charCode;\n       \
        \     rightChar[node] = charCode;\n            return;\n        }\n        const\
        \ mid = (start + end) >> 1;\n        if (idx <= mid) update(2 * node, start,\
        \ mid, idx, charCode);\n        else update(2 * node + 1, mid + 1, end, idx,\
        \ charCode);\n        merge(node, 2 * node, 2 * node + 1, mid - start + 1, end\
        \ - mid);\n    }\n\n    build(1, 0, n - 1);\n    const k = queryIndices.length;\n\
        \    const results: number[] = new Array(k);\n    for (let i = 0; i < k; i++)\
        \ {\n        update(1, 0, n - 1, queryIndices[i], queryCharacters.charCodeAt(i));\n\
        \        results[i] = maxLen[1];\n    }\n    return results;\n};"
      php: "class Solution {\n    private $maxLen, $prefixLen, $suffixLen, $leftChar,\
        \ $rightChar;\n\n    function merge($node, $left, $right, $lLen, $rLen) {\n\
        \        $this->maxLen[$node] = max($this->maxLen[$left], $this->maxLen[$right]);\n\
        \        $this->leftChar[$node] = $this->leftChar[$left];\n        $this->rightChar[$node]\
        \ = $this->rightChar[$right];\n        $this->prefixLen[$node] = $this->prefixLen[$left];\n\
        \        $this->suffixLen[$node] = $this->suffixLen[$right];\n\n        if ($this->rightChar[$left]\
        \ === $this->leftChar[$right]) {\n            $combined = $this->suffixLen[$left]\
        \ + $this->prefixLen[$right];\n            if ($combined > $this->maxLen[$node])\
        \ $this->maxLen[$node] = $combined;\n            if ($this->prefixLen[$left]\
        \ === $lLen) $this->prefixLen[$node] = $lLen + $this->prefixLen[$right];\n \
        \           if ($this->suffixLen[$right] === $rLen) $this->suffixLen[$node]\
        \ = $rLen + $this->suffixLen[$left];\n        }\n    }\n\n    function build(&$s,\
        \ $node, $start, $end) {\n        if ($start === $end) {\n            $code\
        \ = ord($s[$start]);\n            $this->maxLen[$node] = 1;\n            $this->prefixLen[$node]\
        \ = 1;\n            $this->suffixLen[$node] = 1;\n            $this->leftChar[$node]\
        \ = $code;\n            $this->rightChar[$node] = $code;\n            return;\n\
        \        }\n        $mid = (int)(($start + $end) / 2);\n        $this->build($s,\
        \ 2 * $node, $start, $mid);\n        $this->build($s, 2 * $node + 1, $mid +\
        \ 1, $end);\n        $this->merge($node, 2 * $node, 2 * $node + 1, $mid - $start\
        \ + 1, $end - $mid);\n    }\n\n    function update($node, $start, $end, $idx,\
        \ $charCode) {\n        if ($start === $end) {\n            $this->leftChar[$node]\
        \ = $charCode;\n            $this->rightChar[$node] = $charCode;\n         \
        \   return;\n        }\n        $mid = (int)(($start + $end) / 2);\n       \
        \ if ($idx <= $mid) $this->update(2 * $node, $start, $mid, $idx, $charCode);\n\
        \        else $this->update(2 * $node + 1, $mid + 1, $end, $idx, $charCode);\n\
        \        $this->merge($node, 2 * $node, 2 * $node + 1, $mid - $start + 1, $end\
        \ - $mid);\n    }\n\n    /**\n     * @param String $s\n     * @param String\
        \ $queryCharacters\n     * @param Integer[] $queryIndices\n     * @return Integer[]\n\
        \     */\n    function longestRepeating($s, $queryCharacters, $queryIndices)\
        \ {\n        $n = strlen($s);\n        $this->maxLen = new SplFixedArray(4 *\
        \ $n + 1);\n        $this->prefixLen = new SplFixedArray(4 * $n + 1);\n    \
        \    $this->suffixLen = new SplFixedArray(4 * $n + 1);\n        $this->leftChar\
        \ = new SplFixedArray(4 * $n + 1);\n        $this->rightChar = new SplFixedArray(4\
        \ * $n + 1);\n\n        $this->build($s, 1, 0, $n - 1);\n\n        $k = count($queryIndices);\n\
        \        $results = [];\n        for ($i = 0; $i < $k; $i++) {\n           \
        \ $this->update(1, 0, $n - 1, $queryIndices[$i], ord($queryCharacters[$i]));\n\
        \            $results[] = $this->maxLen[1];\n        }\n        return $results;\n\
        \    }\n}"
      swift: "class Solution {\n    private var maxLen: [Int] = []\n    private var\
        \ prefixLen: [Int] = []\n    private var suffixLen: [Int] = []\n    private\
        \ var leftChar: [UInt8] = []\n    private var rightChar: [UInt8] = []\n\n  \
        \  private func merge(_ node: Int, _ left: Int, _ right: Int, _ lLen: Int, _\
        \ rLen: Int) {\n        maxLen[node] = max(maxLen[left], maxLen[right])\n  \
        \      leftChar[node] = leftChar[left]\n        rightChar[node] = rightChar[right]\n\
        \        prefixLen[node] = prefixLen[left]\n        suffixLen[node] = suffixLen[right]\n\
        \n        if rightChar[left] == leftChar[right] {\n            let combined\
        \ = suffixLen[left] + prefixLen[right]\n            if combined > maxLen[node]\
        \ { maxLen[node] = combined }\n            if prefixLen[left] == lLen { prefixLen[node]\
        \ = lLen + prefixLen[right] }\n            if suffixLen[right] == rLen { suffixLen[node]\
        \ = rLen + suffixLen[left] }\n        }\n    }\n\n    private func build(_ s:\
        \ [UInt8], _ node: Int, _ start: Int, _ end: Int) {\n        if start == end\
        \ {\n            let code = s[start]\n            maxLen[node] = 1\n       \
        \     prefixLen[node] = 1\n            suffixLen[node] = 1\n            leftChar[node]\
        \ = code\n            rightChar[node] = code\n            return\n        }\n\
        \        let mid = (start + end) / 2\n        build(s, 2 * node, start, mid)\n\
        \        build(s, 2 * node + 1, mid + 1, end)\n        merge(node, 2 * node,\
        \ 2 * node + 1, mid - start + 1, end - mid)\n    }\n\n    private func update(_\
        \ node: Int, _ start: Int, _ end: Int, _ idx: Int, _ charCode: UInt8) {\n  \
        \      if start == end {\n            leftChar[node] = charCode\n          \
        \  rightChar[node] = charCode\n            return\n        }\n        let mid\
        \ = (start + end) / 2\n        if idx <= mid { update(2 * node, start, mid,\
        \ idx, charCode) }\n        else { update(2 * node + 1, mid + 1, end, idx, charCode)\
        \ }\n        merge(node, 2 * node, 2 * node + 1, mid - start + 1, end - mid)\n\
        \    }\n\n    func longestRepeating(_ s: String, _ queryCharacters: String,\
        \ _ queryIndices: [Int]) -> [Int] {\n        let n = s.count\n        let sBytes\
        \ = Array(s.utf8)\n        let qBytes = Array(queryCharacters.utf8)\n\n    \
        \    let size = 4 * n + 1\n        maxLen = [Int](repeating: 0, count: size)\n\
        \        prefixLen = [Int](repeating: 0, count: size)\n        suffixLen = [Int](repeating:\
        \ 0, count: size)\n        leftChar = [UInt8](repeating: 0, count: size)\n \
        \       rightChar = [UInt8](repeating: 0, count: size)\n\n        build(sBytes,\
        \ 1, 0, n - 1)\n\n        var results: [Int] = []\n        for i in 0..<queryIndices.count\
        \ {\n            update(1, 0, n - 1, queryIndices[i], qBytes[i])\n         \
        \   results.append(maxLen[1])\n        }\n        return results\n    }\n}"
      kotlin: "class Solution {\n    private lateinit var maxLen: IntArray\n    private\
        \ lateinit var prefixLen: IntArray\n    private lateinit var suffixLen: IntArray\n\
        \    private lateinit var leftChar: IntArray\n    private lateinit var rightChar:\
        \ IntArray\n\n    private fun merge(node: Int, left: Int, right: Int, lLen:\
        \ Int, rLen: Int) {\n        maxLen[node] = maxOf(maxLen[left], maxLen[right])\n\
        \        leftChar[node] = leftChar[left]\n        rightChar[node] = rightChar[right]\n\
        \        prefixLen[node] = prefixLen[left]\n        suffixLen[node] = suffixLen[right]\n\
        \n        if (rightChar[left] == leftChar[right]) {\n            val combined\
        \ = suffixLen[left] + prefixLen[right]\n            if (combined > maxLen[node])\
        \ maxLen[node] = combined\n            if (prefixLen[left] == lLen) prefixLen[node]\
        \ = lLen + prefixLen[right]\n            if (suffixLen[right] == rLen) suffixLen[node]\
        \ = rLen + suffixLen[left]\n        }\n    }\n\n    private fun build(s: String,\
        \ node: Int, start: Int, end: Int) {\n        if (start == end) {\n        \
        \    val code = s[start].toInt()\n            maxLen[node] = 1\n           \
        \ prefixLen[node] = 1\n            suffixLen[node] = 1\n            leftChar[node]\
        \ = code\n            rightChar[node] = code\n            return\n        }\n\
        \        val mid = (start + end) / 2\n        build(s, 2 * node, start, mid)\n\
        \        build(s, 2 * node + 1, mid + 1, end)\n        merge(node, 2 * node,\
        \ 2 * node + 1, mid - start + 1, end - mid)\n    }\n\n    private fun update(node:\
        \ Int, start: Int, end: Int, idx: Int, charCode: Int) {\n        if (start ==\
        \ end) {\n            leftChar[node] = charCode\n            rightChar[node]\
        \ = charCode\n            return\n        }\n        val mid = (start + end)\
        \ / 2\n        if (idx <= mid) update(2 * node, start, mid, idx, charCode)\n\
        \        else update(2 * node + 1, mid + 1, end, idx, charCode)\n        merge(node,\
        \ 2 * node, 2 * node + 1, mid - start + 1, end - mid)\n    }\n\n    fun longestRepeating(s:\
        \ String, queryCharacters: String, queryIndices: IntArray): IntArray {\n   \
        \     val n = s.length\n        val k = queryIndices.size\n        val size\
        \ = 4 * n + 1\n        maxLen = IntArray(size)\n        prefixLen = IntArray(size)\n\
        \        suffixLen = IntArray(size)\n        leftChar = IntArray(size)\n   \
        \     rightChar = IntArray(size)\n\n        build(s, 1, 0, n - 1)\n\n      \
        \  val results = IntArray(k)\n        for (i in 0 until k) {\n            update(1,\
        \ 0, n - 1, queryIndices[i], queryCharacters[i].toInt())\n            results[i]\
        \ = maxLen[1]\n        }\n        return results\n    }\n}"
      dart: "import 'dart:typed_data';\n\nclass Solution {\n  late Int32List _maxLen;\n\
        \  late Int32List _preLen;\n  late Int32List _sufLen;\n  late Int32List _preChar;\n\
        \  late Int32List _sufChar;\n\n  void _merge(int v, int tl, int tr, int tm)\
        \ {\n    int lc = 2 * v;\n    int rc = 2 * v + 1;\n    int leftSize = tm - tl\
        \ + 1;\n    int rightSize = tr - tm;\n\n    _preChar[v] = _preChar[lc];\n  \
        \  _sufChar[v] = _sufChar[rc];\n    _preLen[v] = _preLen[lc];\n    _sufLen[v]\
        \ = _sufLen[rc];\n\n    int m1 = _maxLen[lc];\n    int m2 = _maxLen[rc];\n \
        \   int resMax = m1 > m2 ? m1 : m2;\n\n    if (_sufChar[lc] == _preChar[rc])\
        \ {\n      int combined = _sufLen[lc] + _preLen[rc];\n      if (combined > resMax)\
        \ resMax = combined;\n      if (_preLen[lc] == leftSize) {\n        _preLen[v]\
        \ = leftSize + _preLen[rc];\n      }\n      if (_sufLen[rc] == rightSize) {\n\
        \        _sufLen[v] = rightSize + _sufLen[lc];\n      }\n    }\n    _maxLen[v]\
        \ = resMax;\n  }\n\n  void _build(int v, int tl, int tr, String s) {\n    if\
        \ (tl == tr) {\n      _maxLen[v] = 1;\n      _preLen[v] = 1;\n      _sufLen[v]\
        \ = 1;\n      _preChar[v] = s.codeUnitAt(tl);\n      _sufChar[v] = s.codeUnitAt(tl);\n\
        \    } else {\n      int tm = (tl + tr) ~/ 2;\n      _build(2 * v, tl, tm, s);\n\
        \      _build(2 * v + 1, tm + 1, tr, s);\n      _merge(v, tl, tr, tm);\n   \
        \ }\n  }\n\n  void _update(int v, int tl, int tr, int pos, int charCode) {\n\
        \    if (tl == tr) {\n      _preChar[v] = charCode;\n      _sufChar[v] = charCode;\n\
        \      _maxLen[v] = 1;\n      _preLen[v] = 1;\n      _sufLen[v] = 1;\n    }\
        \ else {\n      int tm = (tl + tr) ~/ 2;\n      if (pos <= tm) {\n        _update(2\
        \ * v, tl, tm, pos, charCode);\n      } else {\n        _update(2 * v + 1, tm\
        \ + 1, tr, pos, charCode);\n      }\n      _merge(v, tl, tr, tm);\n    }\n \
        \ }\n\n  List<int> longestRepeating(String s, String queryCharacters, List<int>\
        \ queryIndices) {\n    int n = s.length;\n    int treeSize = 4 * n + 1;\n  \
        \  _maxLen = Int32List(treeSize);\n    _preLen = Int32List(treeSize);\n    _sufLen\
        \ = Int32List(treeSize);\n    _preChar = Int32List(treeSize);\n    _sufChar\
        \ = Int32List(treeSize);\n\n    _build(1, 0, n - 1, s);\n\n    int k = queryIndices.length;\n\
        \    List<int> result = List.filled(k, 0);\n    for (int i = 0; i < k; i++)\
        \ {\n      _update(1, 0, n - 1, queryIndices[i], queryCharacters.codeUnitAt(i));\n\
        \      result[i] = _maxLen[1];\n    }\n    return result;\n  }\n}"
      go: "func longestRepeating(s string, queryCharacters string, queryIndices []int)\
        \ []int {\n\ttype node struct {\n\t\tmaxLen, preLen, sufLen int\n\t\tpreChar,\
        \ sufChar       byte\n\t}\n\n\tn := len(s)\n\ttree := make([]node, 4*n+1)\n\n\
        \tvar merge func(v, tl, tr, tm int)\n\tmerge = func(v, tl, tr, tm int) {\n\t\
        \tlc, rc := 2*v, 2*v+1\n\t\ttree[v].preChar = tree[lc].preChar\n\t\ttree[v].sufChar\
        \ = tree[rc].sufChar\n\t\ttree[v].preLen = tree[lc].preLen\n\t\ttree[v].sufLen\
        \ = tree[rc].sufLen\n\n\t\tmx := tree[lc].maxLen\n\t\tif tree[rc].maxLen > mx\
        \ {\n\t\t\tmx = tree[rc].maxLen\n\t\t}\n\n\t\tif tree[lc].sufChar == tree[rc].preChar\
        \ {\n\t\t\tcombined := tree[lc].sufLen + tree[rc].preLen\n\t\t\tif combined\
        \ > mx {\n\t\t\t\tmx = combined\n\t\t\t}\n\t\t\tif tree[lc].preLen == (tm -\
        \ tl + 1) {\n\t\t\t\ttree[v].preLen = (tm - tl + 1) + tree[rc].preLen\n\t\t\t\
        }\n\t\t\tif tree[rc].sufLen == (tr - tm) {\n\t\t\t\ttree[v].sufLen = (tr - tm)\
        \ + tree[lc].sufLen\n\t\t\t}\n\t\t}\n\t\ttree[v].maxLen = mx\n\t}\n\n\tvar build\
        \ func(v, tl, tr int)\n\tbuild = func(v, tl, tr int) {\n\t\tif tl == tr {\n\t\
        \t\ttree[v] = node{1, 1, 1, s[tl], s[tl]}\n\t\t\treturn\n\t\t}\n\t\ttm := (tl\
        \ + tr) / 2\n\t\tbuild(2*v, tl, tm)\n\t\tbuild(2*v+1, tm+1, tr)\n\t\tmerge(v,\
        \ tl, tr, tm)\n\t}\n\n\tvar update func(v, tl, tr, pos int, char byte)\n\tupdate\
        \ = func(v, tl, tr, pos int, char byte) {\n\t\tif tl == tr {\n\t\t\ttree[v]\
        \ = node{1, 1, 1, char, char}\n\t\t\treturn\n\t\t}\n\t\ttm := (tl + tr) / 2\n\
        \t\tif pos <= tm {\n\t\t\tupdate(2*v, tl, tm, pos, char)\n\t\t} else {\n\t\t\
        \tupdate(2*v+1, tm+1, tr, pos, char)\n\t\t}\n\t\tmerge(v, tl, tr, tm)\n\t}\n\
        \n\tbuild(1, 0, n-1)\n\tk := len(queryIndices)\n\tres := make([]int, k)\n\t\
        for i := 0; i < k; i++ {\n\t\tupdate(1, 0, n-1, queryIndices[i], queryCharacters[i])\n\
        \t\tres[i] = tree[1].maxLen\n\t}\n\treturn res\n}"
      ruby: "class Solution\n  def longest_repeating(s, query_characters, query_indices)\n\
        \    n = s.length\n    tree_size = 4 * n + 1\n    @max_len = Array.new(tree_size,\
        \ 0)\n    @pre_len = Array.new(tree_size, 0)\n    @suf_len = Array.new(tree_size,\
        \ 0)\n    @pre_char = Array.new(tree_size, 0)\n    @suf_char = Array.new(tree_size,\
        \ 0)\n\n    s_bytes = s.bytes\n    q_bytes = query_characters.bytes\n    build(1,\
        \ 0, n - 1, s_bytes)\n\n    k = query_indices.length\n    result = Array.new(k)\n\
        \    i = 0\n    while i < k\n      update(1, 0, n - 1, query_indices[i], q_bytes[i])\n\
        \      result[i] = @max_len[1]\n      i += 1\n    end\n    result\n  end\n\n\
        \  def merge(v, tl, tr, tm)\n    lc = 2 * v\n    rc = 2 * v + 1\n    @pre_char[v]\
        \ = @pre_char[lc]\n    @suf_char[v] = @suf_char[rc]\n    @pre_len[v] = @pre_len[lc]\n\
        \    @suf_len[v] = @suf_len[rc]\n\n    lm = @max_len[lc]\n    rm = @max_len[rc]\n\
        \    res_m = lm > rm ? lm : rm\n\n    if @suf_char[lc] == @pre_char[rc]\n  \
        \    combined = @suf_len[lc] + @pre_len[rc]\n      res_m = combined if combined\
        \ > res_m\n      l_size = tm - tl + 1\n      r_size = tr - tm\n      @pre_len[v]\
        \ = l_size + @pre_len[rc] if @pre_len[lc] == l_size\n      @suf_len[v] = r_size\
        \ + @suf_len[lc] if @suf_len[rc] == r_size\n    end\n    @max_len[v] = res_m\n\
        \  end\n\n  def build(v, tl, tr, s_bytes)\n    if tl == tr\n      @max_len[v]\
        \ = @pre_len[v] = @suf_len[v] = 1\n      @pre_char[v] = @suf_char[v] = s_bytes[tl]\n\
        \    else\n      tm = (tl + tr) / 2\n      build(2 * v, tl, tm, s_bytes)\n \
        \     build(2 * v + 1, tm + 1, tr, s_bytes)\n      merge(v, tl, tr, tm)\n  \
        \  end\n  end\n\n  def update(v, tl, tr, pos, char_code)\n    if tl == tr\n\
        \      @pre_char[v] = @suf_char[v] = char_code\n      @max_len[v] = @pre_len[v]\
        \ = @suf_len[v] = 1\n    else\n      tm = (tl + tr) / 2\n      if pos <= tm\n\
        \        update(2 * v, tl, tm, pos, char_code)\n      else\n        update(2\
        \ * v + 1, tm + 1, tr, pos, char_code)\n      end\n      merge(v, tl, tr, tm)\n\
        \    end\n  end\nend"
      scala: "object Solution {\n  def longestRepeating(s: String, queryCharacters:\
        \ String, queryIndices: Array[Int]): Array[Int] = {\n    val n = s.length\n\
        \    val treeSize = 4 * n + 1\n    val maxLen = new Array[Int](treeSize)\n \
        \   val preLen = new Array[Int](treeSize)\n    val sufLen = new Array[Int](treeSize)\n\
        \    val preChar = new Array[Int](treeSize)\n    val sufChar = new Array[Int](treeSize)\n\
        \n    def merge(v: Int, tl: Int, tr: Int, tm: Int): Unit = {\n      val lc =\
        \ 2 * v\n      val rc = 2 * v + 1\n      val leftSize = tm - tl + 1\n      val\
        \ rightSize = tr - tm\n\n      preChar(v) = preChar(lc)\n      sufChar(v) =\
        \ sufChar(rc)\n      preLen(v) = preLen(lc)\n      sufLen(v) = sufLen(rc)\n\n\
        \      val lm = maxLen(lc)\n      val rm = maxLen(rc)\n      var resMax = if\
        \ (lm > rm) lm else rm\n\n      if (sufChar(lc) == preChar(rc)) {\n        val\
        \ combined = sufLen(lc) + preLen(rc)\n        if (combined > resMax) resMax\
        \ = combined\n        if (preLen(lc) == leftSize) {\n          preLen(v) = leftSize\
        \ + preLen(rc)\n        }\n        if (sufLen(rc) == rightSize) {\n        \
        \  sufLen(v) = rightSize + sufLen(lc)\n        }\n      }\n      maxLen(v) =\
        \ resMax\n    }\n\n    def build(v: Int, tl: Int, tr: Int): Unit = {\n     \
        \ if (tl == tr) {\n        maxLen(v) = 1\n        preLen(v) = 1\n        sufLen(v)\
        \ = 1\n        preChar(v) = s.charAt(tl).toInt\n        sufChar(v) = s.charAt(tl).toInt\n\
        \      } else {\n        val tm = (tl + tr) / 2\n        build(2 * v, tl, tm)\n\
        \        build(2 * v + 1, tm + 1, tr)\n        merge(v, tl, tr, tm)\n      }\n\
        \    }\n\n    def update(v: Int, tl: Int, tr: Int, pos: Int, charCode: Int):\
        \ Unit = {\n      if (tl == tr) {\n        preChar(v) = charCode\n        sufChar(v)\
        \ = charCode\n        maxLen(v) = 1\n        preLen(v) = 1\n        sufLen(v)\
        \ = 1\n      } else {\n        val tm = (tl + tr) / 2\n        if (pos <= tm)\
        \ update(2 * v, tl, tm, pos, charCode)\n        else update(2 * v + 1, tm +\
        \ 1, tr, pos, charCode)\n        merge(v, tl, tr, tm)\n      }\n    }\n\n  \
        \  build(1, 0, n - 1)\n\n    val k = queryIndices.length\n    val result = new\
        \ Array[Int](k)\n    var i = 0\n    while (i < k) {\n      update(1, 0, n -\
        \ 1, queryIndices(i), queryCharacters.charAt(i).toInt)\n      result(i) = maxLen(1)\n\
        \      i += 1\n    }\n    result\n  }\n}"
      rust: "impl Solution {\n    pub fn longest_repeating(s: String, query_characters:\
        \ String, query_indices: Vec<i32>) -> Vec<i32> {\n        #[derive(Clone, Copy)]\n\
        \        struct Node {\n            max_len: i32,\n            pref_len: i32,\n\
        \            suff_len: i32,\n            left_char: u8,\n            right_char:\
        \ u8,\n            size: i32,\n        }\n\n        fn merge(l: &Node, r: &Node)\
        \ -> Node {\n            let mut res = Node {\n                max_len: l.max_len.max(r.max_len),\n\
        \                pref_len: l.pref_len,\n                suff_len: r.suff_len,\n\
        \                left_char: l.left_char,\n                right_char: r.right_char,\n\
        \                size: l.size + r.size,\n            };\n            if l.right_char\
        \ == r.left_char {\n                res.max_len = res.max_len.max(l.suff_len\
        \ + r.pref_len);\n                if l.pref_len == l.size {\n              \
        \      res.pref_len = l.size + r.pref_len;\n                }\n            \
        \    if r.suff_len == r.size {\n                    res.suff_len = r.size +\
        \ l.suff_len;\n                }\n            }\n            res\n        }\n\
        \n        fn build(s: &[u8], node: usize, start: usize, end: usize, tree: &mut\
        \ [Node]) {\n            if start == end {\n                tree[node] = Node\
        \ {\n                    max_len: 1,\n                    pref_len: 1,\n   \
        \                 suff_len: 1,\n                    left_char: s[start],\n \
        \                   right_char: s[start],\n                    size: 1,\n  \
        \              };\n                return;\n            }\n            let mid\
        \ = (start + end) / 2;\n            build(s, 2 * node, start, mid, tree);\n\
        \            build(s, 2 * node + 1, mid + 1, end, tree);\n            tree[node]\
        \ = merge(&tree[2 * node], &tree[2 * node + 1]);\n        }\n\n        fn update(node:\
        \ usize, start: usize, end: usize, pos: usize, c: u8, tree: &mut [Node]) {\n\
        \            if start == end {\n                tree[node] = Node {\n      \
        \              max_len: 1,\n                    pref_len: 1,\n             \
        \       suff_len: 1,\n                    left_char: c,\n                  \
        \  right_char: c,\n                    size: 1,\n                };\n      \
        \          return;\n            }\n            let mid = (start + end) / 2;\n\
        \            if pos <= mid {\n                update(2 * node, start, mid, pos,\
        \ c, tree);\n            } else {\n                update(2 * node + 1, mid\
        \ + 1, end, pos, c, tree);\n            }\n            tree[node] = merge(&tree[2\
        \ * node], &tree[2 * node + 1]);\n        }\n\n        let n = s.len();\n  \
        \      let mut tree = vec![Node { max_len: 0, pref_len: 0, suff_len: 0, left_char:\
        \ 0, right_char: 0, size: 0 }; 4 * n + 1];\n        let s_bytes = s.as_bytes();\n\
        \        build(s_bytes, 1, 0, n - 1, &mut tree);\n\n        let q_chars = query_characters.as_bytes();\n\
        \        let mut results = Vec::with_capacity(query_indices.len());\n      \
        \  for i in 0..query_indices.len() {\n            update(1, 0, n - 1, query_indices[i]\
        \ as usize, q_chars[i], &mut tree);\n            results.push(tree[1].max_len);\n\
        \        }\n        results\n    }\n}"
      racket: "(define/contract (longest-repeating s queryCharacters queryIndices)\n\
        \  (-> string? string? (listof exact-integer?) (listof exact-integer?))\n  (struct\
        \ node-item (max-len pref-len suff-len left-char right-char size) #:transparent)\n\
        \n  (define (merge-nodes l r)\n    (let* ([l-max (node-item-max-len l)]\n  \
        \         [l-pref (node-item-pref-len l)]\n           [l-suff (node-item-suff-len\
        \ l)]\n           [l-lchar (node-item-left-char l)]\n           [l-rchar (node-item-right-char\
        \ l)]\n           [l-size (node-item-size l)]\n           [r-max (node-item-max-len\
        \ r)]\n           [r-pref (node-item-pref-len r)]\n           [r-suff (node-item-suff-len\
        \ r)]\n           [r-lchar (node-item-left-char r)]\n           [r-rchar (node-item-right-char\
        \ r)]\n           [r-size (node-item-size r)]\n           [res-max (max l-max\
        \ r-max)]\n           [res-pref l-pref]\n           [res-suff r-suff])\n   \
        \   (if (char=? l-rchar r-lchar)\n          (let* ([m1 (max res-max (+ l-suff\
        \ r-pref))]\n                 [p1 (if (= l-pref l-size) (+ l-size r-pref) l-pref)]\n\
        \                 [s1 (if (= r-suff r-size) (+ r-size l-suff) r-suff)])\n  \
        \          (node-item m1 p1 s1 l-lchar r-rchar (+ l-size r-size)))\n       \
        \   (node-item res-max res-pref res-suff l-lchar r-rchar (+ l-size r-size)))))\n\
        \n  (define n (string-length s))\n  (define s-vec (list->vector (string->list\
        \ s)))\n  (define tree (make-vector (* 4 n)))\n\n  (define (build start end\
        \ node)\n    (if (= start end)\n        (let ([char (vector-ref s-vec start)])\n\
        \          (vector-set! tree node (node-item 1 1 1 char char 1)))\n        (let*\
        \ ([mid (quotient (+ start end) 2)]\n               [lc (* 2 node)]\n      \
        \         [rc (+ (* 2 node) 1)])\n          (build start mid lc)\n         \
        \ (build (+ mid 1) end rc)\n          (vector-set! tree node (merge-nodes (vector-ref\
        \ tree lc) (vector-ref tree rc))))))\n\n  (define (update-tree start end node\
        \ pos char)\n    (if (= start end)\n        (vector-set! tree node (node-item\
        \ 1 1 1 char char 1))\n        (let* ([mid (quotient (+ start end) 2)]\n   \
        \            [lc (* 2 node)]\n               [rc (+ (* 2 node) 1)])\n      \
        \    (if (<= pos mid)\n              (update-tree start mid lc pos char)\n \
        \             (update-tree (+ mid 1) end rc pos char))\n          (vector-set!\
        \ tree node (merge-nodes (vector-ref tree lc) (vector-ref tree rc))))))\n\n\
        \  (if (> n 0)\n      (begin\n        (build 0 (- n 1) 1)\n        (for/list\
        \ ([char (string->list queryCharacters)]\n                   [idx queryIndices])\n\
        \          (update-tree 0 (- n 1) 1 idx char)\n          (node-item-max-len\
        \ (vector-ref tree 1))))\n      '()))"
      erlang: "-spec longest_repeating(S :: unicode:unicode_binary(), QueryCharacters\
        \ :: unicode:unicode_binary(), QueryIndices :: [integer()]) -> [integer()].\n\
        longest_repeating(S, QueryCharacters, QueryIndices) ->\n  SList = unicode:characters_to_list(S),\n\
        \  STuple = list_to_tuple(SList),\n  N = length(SList),\n  Tree = build_tree(0,\
        \ N - 1, STuple),\n  QChars = unicode:characters_to_list(QueryCharacters),\n\
        \  Queries = lists:zip(QueryIndices, QChars),\n  {Results, _} = lists:mapfoldl(fun({Idx,\
        \ Char}, CurrentTree) ->\n    NewTree = update_tree(0, N - 1, Idx, Char, CurrentTree),\n\
        \    {MaxLen, _, _, _, _, _} = get_info(NewTree),\n    {MaxLen, NewTree}\n \
        \ end, Tree, Queries),\n  Results.\n\nbuild_tree(L, R, STuple) when L =:= R\
        \ ->\n  C = element(L + 1, STuple),\n  {1, 1, 1, C, C, 1};\nbuild_tree(L, R,\
        \ STuple) ->\n  Mid = (L + R) div 2,\n  Left = build_tree(L, Mid, STuple),\n\
        \  Right = build_tree(Mid + 1, R, STuple),\n  {merge(get_info(Left), get_info(Right)),\
        \ Left, Right}.\n\nupdate_tree(L, R, Pos, Char, {_, Left, Right}) ->\n  Mid\
        \ = (L + R) div 2,\n  {NewLeft, NewRight} = if\n    Pos =< Mid -> {update_tree(L,\
        \ Mid, Pos, Char, Left), Right};\n    true -> {Left, update_tree(Mid + 1, R,\
        \ Pos, Char, Right)}\n  end,\n  {merge(get_info(NewLeft), get_info(NewRight)),\
        \ NewLeft, NewRight};\nupdate_tree(_L, _R, _Pos, Char, _) ->\n  {1, 1, 1, Char,\
        \ Char, 1}.\n\nget_info({Info, _, _}) -> Info;\nget_info(Info) -> Info.\n\n\
        merge({MaxL, PrefL, SuffL, LCharL, RCharL, SizeL}, {MaxR, PrefR, SuffR, LCharR,\
        \ RCharR, SizeR}) ->\n  NewMax = if MaxL > MaxR -> MaxL; true -> MaxR end,\n\
        \  {UpdatedMax, UpdatedPref, UpdatedSuff} = if RCharL =:= LCharR ->\n    M1\
        \ = if (SuffL + PrefR) > NewMax -> SuffL + PrefR; true -> NewMax end,\n    P1\
        \ = if PrefL =:= SizeL -> SizeL + PrefR; true -> PrefL end,\n    S1 = if SuffR\
        \ =:= SizeR -> SizeR + SuffL; true -> SuffR end,\n    {M1, P1, S1};\n  true\
        \ ->\n    {NewMax, PrefL, SuffR}\n  end,\n  {UpdatedMax, UpdatedPref, UpdatedSuff,\
        \ LCharL, RCharR, SizeL + SizeR}."
      elixir: "defmodule Solution do\n  @spec longest_repeating(s :: String.t, query_characters\
        \ :: String.t, query_indices :: [integer]) :: [integer]\n  def longest_repeating(s,\
        \ query_characters, query_indices) do\n    s_list = String.to_charlist(s)\n\
        \    s_tuple = List.to_tuple(s_list)\n    n = length(s_list)\n    tree = build_tree(0,\
        \ n - 1, s_tuple)\n    q_chars = String.to_charlist(query_characters)\n\n  \
        \  {results, _final_tree} = Enum.zip(query_indices, q_chars)\n    |> Enum.map_reduce(tree,\
        \ fn {idx, char}, current_tree ->\n      new_tree = update_tree(0, n - 1, idx,\
        \ char, current_tree)\n      {max_len, _, _, _, _, _} = get_info(new_tree)\n\
        \      {max_len, new_tree}\n    end)\n    results\n  end\n\n  defp build_tree(l,\
        \ r, s_tuple) when l == r do\n    c = elem(s_tuple, l)\n    {1, 1, 1, c, c,\
        \ 1}\n  end\n  defp build_tree(l, r, s_tuple) do\n    mid = div(l + r, 2)\n\
        \    left = build_tree(l, mid, s_tuple)\n    right = build_tree(mid + 1, r,\
        \ s_tuple)\n    {merge(get_info(left), get_info(right)), left, right}\n  end\n\
        \n  defp update_tree(l, r, pos, char, {_, left, right}) do\n    mid = div(l\
        \ + r, 2)\n    {new_left, new_right} = if pos <= mid do\n      {update_tree(l,\
        \ mid, pos, char, left), right}\n    else\n      {left, update_tree(mid + 1,\
        \ r, pos, char, right)}\n    end\n    {merge(get_info(new_left), get_info(new_right)),\
        \ new_left, new_right}\n  end\n  defp update_tree(_l, _r, _pos, char, _) do\n\
        \    {1, 1, 1, char, char, 1}\n  end\n\n  defp get_info({info, _, _}), do: info\n\
        \  defp get_info(info), do: info\n\n  defp merge({max_l, pref_l, suff_l, lc_l,\
        \ rc_l, size_l}, {max_r, pref_r, suff_r, lc_r, rc_r, size_r}) do\n    new_max\
        \ = max(max_l, max_r)\n    {updated_max, updated_pref, updated_suff} = if rc_l\
        \ == lc_r do\n      m1 = max(new_max, suff_l + pref_r)\n      p1 = if pref_l\
        \ == size_l, do: size_l + pref_r, else: pref_l\n      s1 = if suff_r == size_r,\
        \ do: size_r + suff_l, else: suff_r\n      {m1, p1, s1}\n    else\n      {new_max,\
        \ pref_l, suff_r}\n    end\n    {updated_max, updated_pref, updated_suff, lc_l,\
        \ rc_r, size_l + size_r}\n  end\nend"
    approach: 'To solve this problem efficiently, we utilize a segment tree where each
      node represents a range of the string and stores five key attributes: the length
      of the longest repeating character substring within that range (maxLen), the length
      of the identical character prefix (prefLen), the length of the identical character
      suffix (suffLen), and the characters at its left and right boundaries. For a leaf
      node representing a single character, maxLen, prefLen, and suffLen are all initialized
      to 1, while both boundary characters are set to the given character. This structure
      allows us to perform point updates when a character in the string changes and
      propagate the effects up to the root in O(log n) time.


      When merging two adjacent segment tree nodes, the key intuition is to check if
      the right character of the left child matches the left character of the right
      child. If they match, a new repeating substring is formed by combining the left
      child''s suffix and the right child''s prefix. We update the parent''s maxLen
      to be the maximum of the children''s maxLen or this combined middle length. Furthermore,
      if a child is entirely composed of the same character (prefix length equals total
      size), the parent''s prefix or suffix can extend into the other child. This ensures
      that after every update, the root of the segment tree always contains the length
      of the longest repeating character substring for the entire string.'
    time_complexity: O((n + k) log n) where n is the length of the string and k is the
      number of queries. Building the segment tree initially takes O(n) time, and each
      of the k point updates requires O(log n) time to traverse from the leaf to the
      root.
    space_complexity: O(n) because the segment tree requires approximately 4n nodes
      for a recursive implementation or 2n nodes for an iterative implementation, with
      each node storing a fixed amount of character and integer information.
    elapsed_time: 445.9981846809387
    model: gemini-3-flash-preview
    generated_at: '2026-08-13 01:24:00 '
---

## Problem #2213: Longest Substring of One Repeating Character

**Difficulty:** Hard

**Topics:** Array, String, Segment Tree, Ordered Set

## Problem Description

<p>You are given a <strong>0-indexed</strong> string <code>s</code>. You are also given a <strong>0-indexed</strong> string <code>queryCharacters</code> of length <code>k</code> and a <strong>0-indexed</strong> array of integer <strong>indices</strong> <code>queryIndices</code> of length <code>k</code>, both of which are used to describe <code>k</code> queries.</p>

<p>The <code>i<sup>th</sup></code> query updates the character in <code>s</code> at index <code>queryIndices[i]</code> to the character <code>queryCharacters[i]</code>.</p>

<p>Return <em>an array</em> <code>lengths</code> <em>of length </em><code>k</code><em> where</em> <code>lengths[i]</code> <em>is the <strong>length</strong> of the <strong>longest substring</strong> of </em><code>s</code><em> consisting of <strong>only one repeating</strong> character <strong>after</strong> the</em> <code>i<sup>th</sup></code> <em>query</em><em> is performed.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babacc&quot;, queryCharacters = &quot;bcb&quot;, queryIndices = [1,3,3]
<strong>Output:</strong> [3,3,4]
<strong>Explanation:</strong> 
- 1<sup>st</sup> query updates s = &quot;<u>b<strong>b</strong>b</u>acc&quot;. The longest substring consisting of one repeating character is &quot;bbb&quot; with length 3.
- 2<sup>nd</sup> query updates s = &quot;bbb<u><strong>c</strong>cc</u>&quot;. 
  The longest substring consisting of one repeating character can be &quot;bbb&quot; or &quot;ccc&quot; with length 3.
- 3<sup>rd</sup> query updates s = &quot;<u>bbb<strong>b</strong></u>cc&quot;. The longest substring consisting of one repeating character is &quot;bbbb&quot; with length 4.
Thus, we return [3,3,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abyzz&quot;, queryCharacters = &quot;aa&quot;, queryIndices = [2,1]
<strong>Output:</strong> [2,3]
<strong>Explanation:</strong>
- 1<sup>st</sup> query updates s = &quot;ab<strong>a</strong><u>zz</u>&quot;. The longest substring consisting of one repeating character is &quot;zz&quot; with length 2.
- 2<sup>nd</sup> query updates s = &quot;<u>a<strong>a</strong>a</u>zz&quot;. The longest substring consisting of one repeating character is &quot;aaa&quot; with length 3.
Thus, we return [2,3].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>k == queryCharacters.length == queryIndices.length</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>queryCharacters</code> consists of lowercase English letters.</li>
	<li><code>0 &lt;= queryIndices[i] &lt; s.length</code></li>
</ul>


## Hints

1. Use a segment tree to perform fast point updates and range queries.

2. We need each segment tree node to store the length of the longest substring of that segment consisting of only 1 repeating character.

3. We will also have each segment tree node store the leftmost and rightmost character of the segment, the max length of a prefix substring consisting of only 1 repeating character, and the max length of a suffix substring consisting of only 1 repeating character.

4. Use this information to properly merge the two segment tree nodes together.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently, we utilize a segment tree where each node represents a range of the string and stores five key attributes: the length of the longest repeating character substring within that range (maxLen), the length of the identical character prefix (prefLen), the length of the identical character suffix (suffLen), and the characters at its left and right boundaries. For a leaf node representing a single character, maxLen, prefLen, and suffLen are all initialized to 1, while both boundary characters are set to the given character. This structure allows us to perform point updates when a character in the string changes and propagate the effects up to the root in O(log n) time.

When merging two adjacent segment tree nodes, the key intuition is to check if the right character of the left child matches the left character of the right child. If they match, a new repeating substring is formed by combining the left child's suffix and the right child's prefix. We update the parent's maxLen to be the maximum of the children's maxLen or this combined middle length. Furthermore, if a child is entirely composed of the same character (prefix length equals total size), the parent's prefix or suffix can extend into the other child. This ensures that after every update, the root of the segment tree always contains the length of the longest repeating character substring for the entire string.

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
    struct Node {
        int maxLen, prefLen, suffLen, sz;
        char lc, rc;
    };
    vector<Node> tree;

    void pull(int node) {
        int l = 2 * node, r = 2 * node + 1;
        tree[node].sz = tree[l].sz + tree[r].sz;
        tree[node].lc = tree[l].lc;
        tree[node].rc = tree[r].rc;
        tree[node].maxLen = max(tree[l].maxLen, tree[r].maxLen);
        tree[node].prefLen = tree[l].prefLen;
        tree[node].suffLen = tree[r].suffLen;
        if (tree[l].rc == tree[r].lc) {
            tree[node].maxLen = max(tree[node].maxLen, tree[l].suffLen + tree[r].prefLen);
            if (tree[l].prefLen == tree[l].sz) tree[node].prefLen = tree[l].sz + tree[r].prefLen;
            if (tree[r].suffLen == tree[r].sz) tree[node].suffLen = tree[r].sz + tree[l].suffLen;
        }
    }

    void build(int node, int start, int end, const string& s) {
        if (start == end) {
            tree[node] = {1, 1, 1, 1, s[start], s[start]};
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node, start, mid, s);
        build(2 * node + 1, mid + 1, end, s);
        pull(node);
    }

    void update(int node, int start, int end, int idx, char c) {
        if (start == end) {
            tree[node].lc = tree[node].rc = c;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, c);
        else update(2 * node + 1, mid + 1, end, idx, c);
        pull(node);
    }

public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        int n = s.length();
        int k = queryIndices.size();
        tree.resize(4 * n + 1);
        build(1, 0, n - 1, s);
        vector<int> result(k);
        for (int i = 0; i < k; i++) {
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i]);
            result[i] = tree[1].maxLen;
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
    int[] maxLen, prefLen, suffLen, sz;
    char[] lc, rc;

    private void pull(int node) {
        int l = 2 * node, r = 2 * node + 1;
        lc[node] = lc[l];
        rc[node] = rc[r];
        sz[node] = sz[l] + sz[r];
        maxLen[node] = Math.max(maxLen[l], maxLen[r]);
        prefLen[node] = prefLen[l];
        suffLen[node] = suffLen[r];
        if (rc[l] == lc[r]) {
            maxLen[node] = Math.max(maxLen[node], suffLen[l] + prefLen[r]);
            if (prefLen[l] == sz[l]) prefLen[node] = sz[l] + prefLen[r];
            if (suffLen[r] == sz[r]) suffLen[node] = sz[r] + suffLen[l];
        }
    }

    private void build(int node, int start, int end, char[] s) {
        if (start == end) {
            maxLen[node] = prefLen[node] = suffLen[node] = sz[node] = 1;
            lc[node] = rc[node] = s[start];
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node, start, mid, s);
        build(2 * node + 1, mid + 1, end, s);
        pull(node);
    }

    private void update(int node, int start, int end, int idx, char c) {
        if (start == end) {
            lc[node] = rc[node] = c;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, c);
        else update(2 * node + 1, mid + 1, end, idx, c);
        pull(node);
    }

    public int[] longestRepeating(String s, String queryCharacters, int[] queryIndices) {
        int n = s.length();
        int k = queryIndices.length;
        maxLen = new int[4 * n];
        prefLen = new int[4 * n];
        suffLen = new int[4 * n];
        sz = new int[4 * n];
        lc = new char[4 * n];
        rc = new char[4 * n];

        char[] sArr = s.toCharArray();
        build(1, 0, n - 1, sArr);

        int[] results = new int[k];
        char[] qChars = queryCharacters.toCharArray();
        for (int i = 0; i < k; i++) {
            update(1, 0, n - 1, queryIndices[i], qChars[i]);
            results[i] = maxLen[1];
        }
        return results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        size = 1
        while size < n: 
            size *= 2

        max_l = [0] * (2 * size)
        pre_l = [0] * (2 * size)
        suf_l = [0] * (2 * size)
        lc = [''] * (2 * size)
        rc = [''] * (2 * size)
        sz = [0] * (2 * size)

        for i in range(n):
            idx = size + i
            max_l[idx] = pre_l[idx] = suf_l[idx] = 1
            lc[idx] = rc[idx] = s[i]
            sz[idx] = 1

        for i in range(size - 1, 0, -1):
            l, r = i << 1, i << 1 | 1
            sz_l, sz_r = sz[l], sz[r]
            sz[i] = sz_l + sz_r
            if sz[i] == 0: continue
            if sz_r == 0:
                max_l[i], pre_l[i], suf_l[i], lc[i], rc[i] = max_l[l], pre_l[l], suf_l[l], lc[l], rc[l]
            else:
                lc_l, rc_l = lc[l], rc[l]
                lc_r, rc_r = lc[r], rc[r]
                ml_l, ml_r = max_l[l], max_l[r]
                pl_l, sl_l = pre_l[l], suf_l[l]
                pl_r, sl_r = pre_l[r], suf_l[r]
                res = ml_l if ml_l > ml_r else ml_r
                pl, sl = pl_l, sl_r
                if rc_l == lc_r:
                    comb = sl_l + pl_r
                    if comb > res: res = comb
                    if pl_l == sz_l: pl = sz_l + pl_r
                    if sl_r == sz_r: sl = sz_r + sl_l
                max_l[i], pre_l[i], suf_l[i], lc[i], rc[i] = res, pl, sl, lc_l, rc_r

        ans = []
        for char, idx_s in zip(queryCharacters, queryIndices):
            idx = size + idx_s
            lc[idx] = rc[idx] = char
            idx >>= 1
            while idx >= 1:
                l, r = idx << 1, idx << 1 | 1
                sz_l, sz_r = sz[l], sz[r]
                if sz_r == 0:
                    max_l[idx], pre_l[idx], suf_l[idx], lc[idx], rc[idx] = max_l[l], pre_l[l], suf_l[l], lc[l], rc[l]
                else:
                    lc_l, rc_l, lc_r, rc_r = lc[l], rc[l], lc[r], rc[r]
                    ml_l, ml_r, pl_l, sl_l, pl_r, sl_r = max_l[l], max_l[r], pre_l[l], suf_l[l], pre_l[r], suf_l[r]
                    res = ml_l if ml_l > ml_r else ml_r
                    pl, sl = pl_l, sl_r
                    if rc_l == lc_r:
                        comb = sl_l + pl_r
                        if comb > res: res = comb
                        if pl_l == sz_l: pl = sz_l + pl_r
                        if sl_r == sz_r: sl = sz_r + sl_l
                    max_l[idx], pre_l[idx], suf_l[idx], lc[idx], rc[idx] = res, pl, sl, lc_l, rc_r
                idx >>= 1
            ans.append(max_l[1])
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        m = 1 << (n - 1).bit_length()

        max_len = [0] * (2 * m)
        pre_len = [0] * (2 * m)
        suf_len = [0] * (2 * m)
        pre_char = [0] * (2 * m)
        suf_char = [0] * (2 * m)
        size = [0] * (2 * m)

        for i in range(n):
            idx = m + i
            max_len[idx] = pre_len[idx] = suf_len[idx] = 1
            pre_char[idx] = suf_char[idx] = ord(s[i])
            size[idx] = 1

        def push_up(idx):
            lc, rc = 2 * idx, 2 * idx + 1
            slc, src = size[lc], size[rc]

            if slc == 0:
                max_len[idx], pre_len[idx], suf_len[idx] = max_len[rc], pre_len[rc], suf_len[rc]
                pre_char[idx], suf_char[idx], size[idx] = pre_char[rc], suf_char[rc], src
            elif src == 0:
                max_len[idx], pre_len[idx], suf_len[idx] = max_len[lc], pre_len[lc], suf_len[lc]
                pre_char[idx], suf_char[idx], size[idx] = pre_char[lc], suf_char[lc], slc
            else:
                size[idx] = slc + src
                l_pc, r_pc, l_sc, r_sc = pre_char[lc], pre_char[rc], suf_char[lc], suf_char[rc]
                pre_char[idx], suf_char[idx] = l_pc, r_sc

                p_len = pre_len[lc]
                if p_len == slc and l_pc == r_pc:
                    p_len += pre_len[rc]
                pre_len[idx] = p_len

                s_len = suf_len[rc]
                if s_len == src and r_sc == l_sc:
                    s_len += suf_len[lc]
                suf_len[idx] = s_len

                m_len = max_len[lc] if max_len[lc] > max_len[rc] else max_len[rc]
                if l_sc == r_pc:
                    combined = suf_len[lc] + pre_len[rc]
                    if combined > m_len: m_len = combined
                max_len[idx] = m_len

        for i in range(m - 1, 0, -1):
            push_up(i)

        ans = []
        q_chars = [ord(c) for c in queryCharacters]
        for i, char_code in zip(queryIndices, q_chars):
            idx = m + i
            pre_char[idx] = suf_char[idx] = char_code
            idx >>= 1
            while idx > 0:
                push_up(idx)
                idx >>= 1
            ans.append(max_len[1])
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct {
    int maxLen;
    int preLen;
    int sufLen;
    char preChar;
    char sufChar;
    int size;
} Node;

void push_up(Node* tree, int idx) {
    int lc = 2 * idx;
    int rc = 2 * idx + 1;
    if (tree[lc].size == 0) {
        tree[idx] = tree[rc];
    } else if (tree[rc].size == 0) {
        tree[idx] = tree[lc];
    } else {
        tree[idx].size = tree[lc].size + tree[rc].size;
        tree[idx].preChar = tree[lc].preChar;
        tree[idx].sufChar = tree[rc].sufChar;

        int pLen = tree[lc].preLen;
        if (pLen == tree[lc].size && tree[lc].preChar == tree[rc].preChar) {
            pLen += tree[rc].preLen;
        }
        tree[idx].preLen = pLen;

        int sLen = tree[rc].sufLen;
        if (sLen == tree[rc].size && tree[rc].sufChar == tree[lc].sufChar) {
            sLen += tree[lc].sufLen;
        }
        tree[idx].sufLen = sLen;

        int mLen = tree[lc].maxLen > tree[rc].maxLen ? tree[lc].maxLen : tree[rc].maxLen;
        if (tree[lc].sufChar == tree[rc].preChar) {
            int combined = tree[lc].sufLen + tree[rc].preLen;
            if (combined > mLen) mLen = combined;
        }
        tree[idx].maxLen = mLen;
    }
}

int* longestRepeating(char* s, char* queryCharacters, int* queryIndices, int queryIndicesSize, int* returnSize) {
    int n = strlen(s);
    int M = 1;
    while (M < n) M <<= 1;

    Node* tree = (Node*)calloc(2 * M, sizeof(Node));
    for (int i = 0; i < n; i++) {
        int idx = M + i;
        tree[idx].maxLen = tree[idx].preLen = tree[idx].sufLen = 1;
        tree[idx].preChar = tree[idx].sufChar = s[i];
        tree[idx].size = 1;
    }
    for (int i = M - 1; i > 0; i--) {
        push_up(tree, i);
    }

    int* lengths = (int*)malloc(queryIndicesSize * sizeof(int));
    for (int i = 0; i < queryIndicesSize; i++) {
        int idx = M + queryIndices[i];
        tree[idx].preChar = tree[idx].sufChar = queryCharacters[i];
        idx >>= 1;
        while (idx > 0) {
            push_up(tree, idx);
            idx >>= 1;
        }
        lengths[i] = tree[1].maxLen;
    }

    free(tree);
    *returnSize = queryIndicesSize;
    return lengths;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    private struct Node {
        public int maxLen;
        public int preLen;
        public int sufLen;
        public int size;
        public char preChar;
        public char sufChar;
    }

    private void PushUp(Node[] tree, int idx) {
        int lc = 2 * idx;
        int rc = 2 * idx + 1;
        if (tree[lc].size == 0) {
            tree[idx] = tree[rc];
        } else if (tree[rc].size == 0) {
            tree[idx] = tree[lc];
        } else {
            tree[idx].size = tree[lc].size + tree[rc].size;
            tree[idx].preChar = tree[lc].preChar;
            tree[idx].sufChar = tree[rc].sufChar;

            int pLen = tree[lc].preLen;
            if (pLen == tree[lc].size && tree[lc].preChar == tree[rc].preChar) {
                pLen += tree[rc].preLen;
            }
            tree[idx].preLen = pLen;

            int sLen = tree[rc].sufLen;
            if (sLen == tree[rc].size && tree[rc].sufChar == tree[lc].sufChar) {
                sLen += tree[lc].sufLen;
            }
            tree[idx].sufLen = sLen;

            int mLen = tree[lc].maxLen > tree[rc].maxLen ? tree[lc].maxLen : tree[rc].maxLen;
            if (tree[lc].sufChar == tree[rc].preChar) {
                int combined = tree[lc].sufLen + tree[rc].preLen;
                if (combined > mLen) mLen = combined;
            }
            tree[idx].maxLen = mLen;
        }
    }

    public int[] LongestRepeating(string s, string queryCharacters, int[] queryIndices) {
        int n = s.Length;
        int M = 1;
        while (M < n) M <<= 1;

        Node[] tree = new Node[2 * M];
        for (int i = 0; i < n; i++) {
            int idx = M + i;
            tree[idx].maxLen = tree[idx].preLen = tree[idx].sufLen = 1;
            tree[idx].preChar = tree[idx].sufChar = s[i];
            tree[idx].size = 1;
        }
        for (int i = M - 1; i > 0; i--) {
            PushUp(tree, i);
        }

        int k = queryIndices.Length;
        int[] results = new int[k];
        for (int i = 0; i < k; i++) {
            int idx = M + queryIndices[i];
            tree[idx].preChar = tree[idx].sufChar = queryCharacters[i];
            idx >>= 1;
            while (idx > 0) {
                PushUp(tree, idx);
                idx >>= 1;
            }
            results[i] = tree[1].maxLen;
        }

        return results;
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
 * @param {string} queryCharacters
 * @param {number[]} queryIndices
 * @return {number[]}
 */
var longestRepeating = function(s, queryCharacters, queryIndices) {
    const n = s.length;
    let m = 1;
    while (m < n) m <<= 1;

    const maxLen = new Int32Array(2 * m);
    const preLen = new Int32Array(2 * m);
    const sufLen = new Int32Array(2 * m);
    const preChar = new Uint8Array(2 * m);
    const sufChar = new Uint8Array(2 * m);
    const size = new Int32Array(2 * m);

    function pushUp(idx) {
        const lc = idx << 1;
        const rc = lc | 1;
        const slc = size[lc];
        const src = size[rc];

        if (slc === 0) {
            maxLen[idx] = maxLen[rc];
            preLen[idx] = preLen[rc];
            sufLen[idx] = sufLen[rc];
            preChar[idx] = preChar[rc];
            sufChar[idx] = sufChar[rc];
            size[idx] = src;
        } else if (src === 0) {
            maxLen[idx] = maxLen[lc];
            preLen[idx] = preLen[lc];
            sufLen[idx] = sufLen[lc];
            preChar[idx] = preChar[lc];
            sufChar[idx] = sufChar[lc];
            size[idx] = slc;
        } else {
            size[idx] = slc + src;
            const lpc = preChar[lc], rpc = preChar[rc], lsc = sufChar[lc], rsc = sufChar[rc];
            preChar[idx] = lpc;
            sufChar[idx] = rsc;

            let pLen = preLen[lc];
            if (pLen === slc && lpc === rpc) pLen += preLen[rc];
            preLen[idx] = pLen;

            let sLen = sufLen[rc];
            if (sLen === src && rsc === lsc) sLen += sufLen[lc];
            sufLen[idx] = sLen;

            let mLen = maxLen[lc] > maxLen[rc] ? maxLen[lc] : maxLen[rc];
            if (lsc === rpc) {
                const combined = sufLen[lc] + preLen[rc];
                if (combined > mLen) mLen = combined;
            }
            maxLen[idx] = mLen;
        }
    }

    for (let i = 0; i < n; i++) {
        const idx = m + i;
        maxLen[idx] = preLen[idx] = sufLen[idx] = 1;
        preChar[idx] = sufChar[idx] = s.charCodeAt(i);
        size[idx] = 1;
    }
    for (let i = m - 1; i > 0; i--) {
        pushUp(i);
    }

    const k = queryIndices.length;
    const result = new Int32Array(k);
    for (let i = 0; i < k; i++) {
        let idx = m + queryIndices[i];
        preChar[idx] = sufChar[idx] = queryCharacters.charCodeAt(i);
        idx >>= 1;
        while (idx > 0) {
            pushUp(idx);
            idx >>= 1;
        }
        result[i] = maxLen[1];
    }

    return Array.from(result);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function longestRepeating(s: string, queryCharacters: string, queryIndices: number[]): number[] {
    const n = s.length;
    const maxLen = new Int32Array(4 * n + 1);
    const prefixLen = new Int32Array(4 * n + 1);
    const suffixLen = new Int32Array(4 * n + 1);
    const leftChar = new Int32Array(4 * n + 1);
    const rightChar = new Int32Array(4 * n + 1);

    function merge(node: number, left: number, right: number, lLen: number, rLen: number) {
        maxLen[node] = Math.max(maxLen[left], maxLen[right]);
        leftChar[node] = leftChar[left];
        rightChar[node] = rightChar[right];
        prefixLen[node] = prefixLen[left];
        suffixLen[node] = suffixLen[right];

        if (rightChar[left] === leftChar[right]) {
            const combined = suffixLen[left] + prefixLen[right];
            if (combined > maxLen[node]) maxLen[node] = combined;
            if (prefixLen[left] === lLen) prefixLen[node] = lLen + prefixLen[right];
            if (suffixLen[right] === rLen) suffixLen[node] = rLen + suffixLen[left];
        }
    }

    function build(node: number, start: number, end: number) {
        if (start === end) {
            const code = s.charCodeAt(start);
            maxLen[node] = 1;
            prefixLen[node] = 1;
            suffixLen[node] = 1;
            leftChar[node] = code;
            rightChar[node] = code;
            return;
        }
        const mid = (start + end) >> 1;
        build(2 * node, start, mid);
        build(2 * node + 1, mid + 1, end);
        merge(node, 2 * node, 2 * node + 1, mid - start + 1, end - mid);
    }

    function update(node: number, start: number, end: number, idx: number, charCode: number) {
        if (start === end) {
            leftChar[node] = charCode;
            rightChar[node] = charCode;
            return;
        }
        const mid = (start + end) >> 1;
        if (idx <= mid) update(2 * node, start, mid, idx, charCode);
        else update(2 * node + 1, mid + 1, end, idx, charCode);
        merge(node, 2 * node, 2 * node + 1, mid - start + 1, end - mid);
    }

    build(1, 0, n - 1);
    const k = queryIndices.length;
    const results: number[] = new Array(k);
    for (let i = 0; i < k; i++) {
        update(1, 0, n - 1, queryIndices[i], queryCharacters.charCodeAt(i));
        results[i] = maxLen[1];
    }
    return results;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    private $maxLen, $prefixLen, $suffixLen, $leftChar, $rightChar;

    function merge($node, $left, $right, $lLen, $rLen) {
        $this->maxLen[$node] = max($this->maxLen[$left], $this->maxLen[$right]);
        $this->leftChar[$node] = $this->leftChar[$left];
        $this->rightChar[$node] = $this->rightChar[$right];
        $this->prefixLen[$node] = $this->prefixLen[$left];
        $this->suffixLen[$node] = $this->suffixLen[$right];

        if ($this->rightChar[$left] === $this->leftChar[$right]) {
            $combined = $this->suffixLen[$left] + $this->prefixLen[$right];
            if ($combined > $this->maxLen[$node]) $this->maxLen[$node] = $combined;
            if ($this->prefixLen[$left] === $lLen) $this->prefixLen[$node] = $lLen + $this->prefixLen[$right];
            if ($this->suffixLen[$right] === $rLen) $this->suffixLen[$node] = $rLen + $this->suffixLen[$left];
        }
    }

    function build(&$s, $node, $start, $end) {
        if ($start === $end) {
            $code = ord($s[$start]);
            $this->maxLen[$node] = 1;
            $this->prefixLen[$node] = 1;
            $this->suffixLen[$node] = 1;
            $this->leftChar[$node] = $code;
            $this->rightChar[$node] = $code;
            return;
        }
        $mid = (int)(($start + $end) / 2);
        $this->build($s, 2 * $node, $start, $mid);
        $this->build($s, 2 * $node + 1, $mid + 1, $end);
        $this->merge($node, 2 * $node, 2 * $node + 1, $mid - $start + 1, $end - $mid);
    }

    function update($node, $start, $end, $idx, $charCode) {
        if ($start === $end) {
            $this->leftChar[$node] = $charCode;
            $this->rightChar[$node] = $charCode;
            return;
        }
        $mid = (int)(($start + $end) / 2);
        if ($idx <= $mid) $this->update(2 * $node, $start, $mid, $idx, $charCode);
        else $this->update(2 * $node + 1, $mid + 1, $end, $idx, $charCode);
        $this->merge($node, 2 * $node, 2 * $node + 1, $mid - $start + 1, $end - $mid);
    }

    /**
     * @param String $s
     * @param String $queryCharacters
     * @param Integer[] $queryIndices
     * @return Integer[]
     */
    function longestRepeating($s, $queryCharacters, $queryIndices) {
        $n = strlen($s);
        $this->maxLen = new SplFixedArray(4 * $n + 1);
        $this->prefixLen = new SplFixedArray(4 * $n + 1);
        $this->suffixLen = new SplFixedArray(4 * $n + 1);
        $this->leftChar = new SplFixedArray(4 * $n + 1);
        $this->rightChar = new SplFixedArray(4 * $n + 1);

        $this->build($s, 1, 0, $n - 1);

        $k = count($queryIndices);
        $results = [];
        for ($i = 0; $i < $k; $i++) {
            $this->update(1, 0, $n - 1, $queryIndices[$i], ord($queryCharacters[$i]));
            $results[] = $this->maxLen[1];
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
    private var maxLen: [Int] = []
    private var prefixLen: [Int] = []
    private var suffixLen: [Int] = []
    private var leftChar: [UInt8] = []
    private var rightChar: [UInt8] = []

    private func merge(_ node: Int, _ left: Int, _ right: Int, _ lLen: Int, _ rLen: Int) {
        maxLen[node] = max(maxLen[left], maxLen[right])
        leftChar[node] = leftChar[left]
        rightChar[node] = rightChar[right]
        prefixLen[node] = prefixLen[left]
        suffixLen[node] = suffixLen[right]

        if rightChar[left] == leftChar[right] {
            let combined = suffixLen[left] + prefixLen[right]
            if combined > maxLen[node] { maxLen[node] = combined }
            if prefixLen[left] == lLen { prefixLen[node] = lLen + prefixLen[right] }
            if suffixLen[right] == rLen { suffixLen[node] = rLen + suffixLen[left] }
        }
    }

    private func build(_ s: [UInt8], _ node: Int, _ start: Int, _ end: Int) {
        if start == end {
            let code = s[start]
            maxLen[node] = 1
            prefixLen[node] = 1
            suffixLen[node] = 1
            leftChar[node] = code
            rightChar[node] = code
            return
        }
        let mid = (start + end) / 2
        build(s, 2 * node, start, mid)
        build(s, 2 * node + 1, mid + 1, end)
        merge(node, 2 * node, 2 * node + 1, mid - start + 1, end - mid)
    }

    private func update(_ node: Int, _ start: Int, _ end: Int, _ idx: Int, _ charCode: UInt8) {
        if start == end {
            leftChar[node] = charCode
            rightChar[node] = charCode
            return
        }
        let mid = (start + end) / 2
        if idx <= mid { update(2 * node, start, mid, idx, charCode) }
        else { update(2 * node + 1, mid + 1, end, idx, charCode) }
        merge(node, 2 * node, 2 * node + 1, mid - start + 1, end - mid)
    }

    func longestRepeating(_ s: String, _ queryCharacters: String, _ queryIndices: [Int]) -> [Int] {
        let n = s.count
        let sBytes = Array(s.utf8)
        let qBytes = Array(queryCharacters.utf8)

        let size = 4 * n + 1
        maxLen = [Int](repeating: 0, count: size)
        prefixLen = [Int](repeating: 0, count: size)
        suffixLen = [Int](repeating: 0, count: size)
        leftChar = [UInt8](repeating: 0, count: size)
        rightChar = [UInt8](repeating: 0, count: size)

        build(sBytes, 1, 0, n - 1)

        var results: [Int] = []
        for i in 0..<queryIndices.count {
            update(1, 0, n - 1, queryIndices[i], qBytes[i])
            results.append(maxLen[1])
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
    private lateinit var maxLen: IntArray
    private lateinit var prefixLen: IntArray
    private lateinit var suffixLen: IntArray
    private lateinit var leftChar: IntArray
    private lateinit var rightChar: IntArray

    private fun merge(node: Int, left: Int, right: Int, lLen: Int, rLen: Int) {
        maxLen[node] = maxOf(maxLen[left], maxLen[right])
        leftChar[node] = leftChar[left]
        rightChar[node] = rightChar[right]
        prefixLen[node] = prefixLen[left]
        suffixLen[node] = suffixLen[right]

        if (rightChar[left] == leftChar[right]) {
            val combined = suffixLen[left] + prefixLen[right]
            if (combined > maxLen[node]) maxLen[node] = combined
            if (prefixLen[left] == lLen) prefixLen[node] = lLen + prefixLen[right]
            if (suffixLen[right] == rLen) suffixLen[node] = rLen + suffixLen[left]
        }
    }

    private fun build(s: String, node: Int, start: Int, end: Int) {
        if (start == end) {
            val code = s[start].toInt()
            maxLen[node] = 1
            prefixLen[node] = 1
            suffixLen[node] = 1
            leftChar[node] = code
            rightChar[node] = code
            return
        }
        val mid = (start + end) / 2
        build(s, 2 * node, start, mid)
        build(s, 2 * node + 1, mid + 1, end)
        merge(node, 2 * node, 2 * node + 1, mid - start + 1, end - mid)
    }

    private fun update(node: Int, start: Int, end: Int, idx: Int, charCode: Int) {
        if (start == end) {
            leftChar[node] = charCode
            rightChar[node] = charCode
            return
        }
        val mid = (start + end) / 2
        if (idx <= mid) update(2 * node, start, mid, idx, charCode)
        else update(2 * node + 1, mid + 1, end, idx, charCode)
        merge(node, 2 * node, 2 * node + 1, mid - start + 1, end - mid)
    }

    fun longestRepeating(s: String, queryCharacters: String, queryIndices: IntArray): IntArray {
        val n = s.length
        val k = queryIndices.size
        val size = 4 * n + 1
        maxLen = IntArray(size)
        prefixLen = IntArray(size)
        suffixLen = IntArray(size)
        leftChar = IntArray(size)
        rightChar = IntArray(size)

        build(s, 1, 0, n - 1)

        val results = IntArray(k)
        for (i in 0 until k) {
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i].toInt())
            results[i] = maxLen[1]
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
import 'dart:typed_data';

class Solution {
  late Int32List _maxLen;
  late Int32List _preLen;
  late Int32List _sufLen;
  late Int32List _preChar;
  late Int32List _sufChar;

  void _merge(int v, int tl, int tr, int tm) {
    int lc = 2 * v;
    int rc = 2 * v + 1;
    int leftSize = tm - tl + 1;
    int rightSize = tr - tm;

    _preChar[v] = _preChar[lc];
    _sufChar[v] = _sufChar[rc];
    _preLen[v] = _preLen[lc];
    _sufLen[v] = _sufLen[rc];

    int m1 = _maxLen[lc];
    int m2 = _maxLen[rc];
    int resMax = m1 > m2 ? m1 : m2;

    if (_sufChar[lc] == _preChar[rc]) {
      int combined = _sufLen[lc] + _preLen[rc];
      if (combined > resMax) resMax = combined;
      if (_preLen[lc] == leftSize) {
        _preLen[v] = leftSize + _preLen[rc];
      }
      if (_sufLen[rc] == rightSize) {
        _sufLen[v] = rightSize + _sufLen[lc];
      }
    }
    _maxLen[v] = resMax;
  }

  void _build(int v, int tl, int tr, String s) {
    if (tl == tr) {
      _maxLen[v] = 1;
      _preLen[v] = 1;
      _sufLen[v] = 1;
      _preChar[v] = s.codeUnitAt(tl);
      _sufChar[v] = s.codeUnitAt(tl);
    } else {
      int tm = (tl + tr) ~/ 2;
      _build(2 * v, tl, tm, s);
      _build(2 * v + 1, tm + 1, tr, s);
      _merge(v, tl, tr, tm);
    }
  }

  void _update(int v, int tl, int tr, int pos, int charCode) {
    if (tl == tr) {
      _preChar[v] = charCode;
      _sufChar[v] = charCode;
      _maxLen[v] = 1;
      _preLen[v] = 1;
      _sufLen[v] = 1;
    } else {
      int tm = (tl + tr) ~/ 2;
      if (pos <= tm) {
        _update(2 * v, tl, tm, pos, charCode);
      } else {
        _update(2 * v + 1, tm + 1, tr, pos, charCode);
      }
      _merge(v, tl, tr, tm);
    }
  }

  List<int> longestRepeating(String s, String queryCharacters, List<int> queryIndices) {
    int n = s.length;
    int treeSize = 4 * n + 1;
    _maxLen = Int32List(treeSize);
    _preLen = Int32List(treeSize);
    _sufLen = Int32List(treeSize);
    _preChar = Int32List(treeSize);
    _sufChar = Int32List(treeSize);

    _build(1, 0, n - 1, s);

    int k = queryIndices.length;
    List<int> result = List.filled(k, 0);
    for (int i = 0; i < k; i++) {
      _update(1, 0, n - 1, queryIndices[i], queryCharacters.codeUnitAt(i));
      result[i] = _maxLen[1];
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
func longestRepeating(s string, queryCharacters string, queryIndices []int) []int {
	type node struct {
		maxLen, preLen, sufLen int
		preChar, sufChar       byte
	}

	n := len(s)
	tree := make([]node, 4*n+1)

	var merge func(v, tl, tr, tm int)
	merge = func(v, tl, tr, tm int) {
		lc, rc := 2*v, 2*v+1
		tree[v].preChar = tree[lc].preChar
		tree[v].sufChar = tree[rc].sufChar
		tree[v].preLen = tree[lc].preLen
		tree[v].sufLen = tree[rc].sufLen

		mx := tree[lc].maxLen
		if tree[rc].maxLen > mx {
			mx = tree[rc].maxLen
		}

		if tree[lc].sufChar == tree[rc].preChar {
			combined := tree[lc].sufLen + tree[rc].preLen
			if combined > mx {
				mx = combined
			}
			if tree[lc].preLen == (tm - tl + 1) {
				tree[v].preLen = (tm - tl + 1) + tree[rc].preLen
			}
			if tree[rc].sufLen == (tr - tm) {
				tree[v].sufLen = (tr - tm) + tree[lc].sufLen
			}
		}
		tree[v].maxLen = mx
	}

	var build func(v, tl, tr int)
	build = func(v, tl, tr int) {
		if tl == tr {
			tree[v] = node{1, 1, 1, s[tl], s[tl]}
			return
		}
		tm := (tl + tr) / 2
		build(2*v, tl, tm)
		build(2*v+1, tm+1, tr)
		merge(v, tl, tr, tm)
	}

	var update func(v, tl, tr, pos int, char byte)
	update = func(v, tl, tr, pos int, char byte) {
		if tl == tr {
			tree[v] = node{1, 1, 1, char, char}
			return
		}
		tm := (tl + tr) / 2
		if pos <= tm {
			update(2*v, tl, tm, pos, char)
		} else {
			update(2*v+1, tm+1, tr, pos, char)
		}
		merge(v, tl, tr, tm)
	}

	build(1, 0, n-1)
	k := len(queryIndices)
	res := make([]int, k)
	for i := 0; i < k; i++ {
		update(1, 0, n-1, queryIndices[i], queryCharacters[i])
		res[i] = tree[1].maxLen
	}
	return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
  def longest_repeating(s, query_characters, query_indices)
    n = s.length
    tree_size = 4 * n + 1
    @max_len = Array.new(tree_size, 0)
    @pre_len = Array.new(tree_size, 0)
    @suf_len = Array.new(tree_size, 0)
    @pre_char = Array.new(tree_size, 0)
    @suf_char = Array.new(tree_size, 0)

    s_bytes = s.bytes
    q_bytes = query_characters.bytes
    build(1, 0, n - 1, s_bytes)

    k = query_indices.length
    result = Array.new(k)
    i = 0
    while i < k
      update(1, 0, n - 1, query_indices[i], q_bytes[i])
      result[i] = @max_len[1]
      i += 1
    end
    result
  end

  def merge(v, tl, tr, tm)
    lc = 2 * v
    rc = 2 * v + 1
    @pre_char[v] = @pre_char[lc]
    @suf_char[v] = @suf_char[rc]
    @pre_len[v] = @pre_len[lc]
    @suf_len[v] = @suf_len[rc]

    lm = @max_len[lc]
    rm = @max_len[rc]
    res_m = lm > rm ? lm : rm

    if @suf_char[lc] == @pre_char[rc]
      combined = @suf_len[lc] + @pre_len[rc]
      res_m = combined if combined > res_m
      l_size = tm - tl + 1
      r_size = tr - tm
      @pre_len[v] = l_size + @pre_len[rc] if @pre_len[lc] == l_size
      @suf_len[v] = r_size + @suf_len[lc] if @suf_len[rc] == r_size
    end
    @max_len[v] = res_m
  end

  def build(v, tl, tr, s_bytes)
    if tl == tr
      @max_len[v] = @pre_len[v] = @suf_len[v] = 1
      @pre_char[v] = @suf_char[v] = s_bytes[tl]
    else
      tm = (tl + tr) / 2
      build(2 * v, tl, tm, s_bytes)
      build(2 * v + 1, tm + 1, tr, s_bytes)
      merge(v, tl, tr, tm)
    end
  end

  def update(v, tl, tr, pos, char_code)
    if tl == tr
      @pre_char[v] = @suf_char[v] = char_code
      @max_len[v] = @pre_len[v] = @suf_len[v] = 1
    else
      tm = (tl + tr) / 2
      if pos <= tm
        update(2 * v, tl, tm, pos, char_code)
      else
        update(2 * v + 1, tm + 1, tr, pos, char_code)
      end
      merge(v, tl, tr, tm)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def longestRepeating(s: String, queryCharacters: String, queryIndices: Array[Int]): Array[Int] = {
    val n = s.length
    val treeSize = 4 * n + 1
    val maxLen = new Array[Int](treeSize)
    val preLen = new Array[Int](treeSize)
    val sufLen = new Array[Int](treeSize)
    val preChar = new Array[Int](treeSize)
    val sufChar = new Array[Int](treeSize)

    def merge(v: Int, tl: Int, tr: Int, tm: Int): Unit = {
      val lc = 2 * v
      val rc = 2 * v + 1
      val leftSize = tm - tl + 1
      val rightSize = tr - tm

      preChar(v) = preChar(lc)
      sufChar(v) = sufChar(rc)
      preLen(v) = preLen(lc)
      sufLen(v) = sufLen(rc)

      val lm = maxLen(lc)
      val rm = maxLen(rc)
      var resMax = if (lm > rm) lm else rm

      if (sufChar(lc) == preChar(rc)) {
        val combined = sufLen(lc) + preLen(rc)
        if (combined > resMax) resMax = combined
        if (preLen(lc) == leftSize) {
          preLen(v) = leftSize + preLen(rc)
        }
        if (sufLen(rc) == rightSize) {
          sufLen(v) = rightSize + sufLen(lc)
        }
      }
      maxLen(v) = resMax
    }

    def build(v: Int, tl: Int, tr: Int): Unit = {
      if (tl == tr) {
        maxLen(v) = 1
        preLen(v) = 1
        sufLen(v) = 1
        preChar(v) = s.charAt(tl).toInt
        sufChar(v) = s.charAt(tl).toInt
      } else {
        val tm = (tl + tr) / 2
        build(2 * v, tl, tm)
        build(2 * v + 1, tm + 1, tr)
        merge(v, tl, tr, tm)
      }
    }

    def update(v: Int, tl: Int, tr: Int, pos: Int, charCode: Int): Unit = {
      if (tl == tr) {
        preChar(v) = charCode
        sufChar(v) = charCode
        maxLen(v) = 1
        preLen(v) = 1
        sufLen(v) = 1
      } else {
        val tm = (tl + tr) / 2
        if (pos <= tm) update(2 * v, tl, tm, pos, charCode)
        else update(2 * v + 1, tm + 1, tr, pos, charCode)
        merge(v, tl, tr, tm)
      }
    }

    build(1, 0, n - 1)

    val k = queryIndices.length
    val result = new Array[Int](k)
    var i = 0
    while (i < k) {
      update(1, 0, n - 1, queryIndices(i), queryCharacters.charAt(i).toInt)
      result(i) = maxLen(1)
      i += 1
    }
    result
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn longest_repeating(s: String, query_characters: String, query_indices: Vec<i32>) -> Vec<i32> {
        #[derive(Clone, Copy)]
        struct Node {
            max_len: i32,
            pref_len: i32,
            suff_len: i32,
            left_char: u8,
            right_char: u8,
            size: i32,
        }

        fn merge(l: &Node, r: &Node) -> Node {
            let mut res = Node {
                max_len: l.max_len.max(r.max_len),
                pref_len: l.pref_len,
                suff_len: r.suff_len,
                left_char: l.left_char,
                right_char: r.right_char,
                size: l.size + r.size,
            };
            if l.right_char == r.left_char {
                res.max_len = res.max_len.max(l.suff_len + r.pref_len);
                if l.pref_len == l.size {
                    res.pref_len = l.size + r.pref_len;
                }
                if r.suff_len == r.size {
                    res.suff_len = r.size + l.suff_len;
                }
            }
            res
        }

        fn build(s: &[u8], node: usize, start: usize, end: usize, tree: &mut [Node]) {
            if start == end {
                tree[node] = Node {
                    max_len: 1,
                    pref_len: 1,
                    suff_len: 1,
                    left_char: s[start],
                    right_char: s[start],
                    size: 1,
                };
                return;
            }
            let mid = (start + end) / 2;
            build(s, 2 * node, start, mid, tree);
            build(s, 2 * node + 1, mid + 1, end, tree);
            tree[node] = merge(&tree[2 * node], &tree[2 * node + 1]);
        }

        fn update(node: usize, start: usize, end: usize, pos: usize, c: u8, tree: &mut [Node]) {
            if start == end {
                tree[node] = Node {
                    max_len: 1,
                    pref_len: 1,
                    suff_len: 1,
                    left_char: c,
                    right_char: c,
                    size: 1,
                };
                return;
            }
            let mid = (start + end) / 2;
            if pos <= mid {
                update(2 * node, start, mid, pos, c, tree);
            } else {
                update(2 * node + 1, mid + 1, end, pos, c, tree);
            }
            tree[node] = merge(&tree[2 * node], &tree[2 * node + 1]);
        }

        let n = s.len();
        let mut tree = vec![Node { max_len: 0, pref_len: 0, suff_len: 0, left_char: 0, right_char: 0, size: 0 }; 4 * n + 1];
        let s_bytes = s.as_bytes();
        build(s_bytes, 1, 0, n - 1, &mut tree);

        let q_chars = query_characters.as_bytes();
        let mut results = Vec::with_capacity(query_indices.len());
        for i in 0..query_indices.len() {
            update(1, 0, n - 1, query_indices[i] as usize, q_chars[i], &mut tree);
            results.push(tree[1].max_len);
        }
        results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (longest-repeating s queryCharacters queryIndices)
  (-> string? string? (listof exact-integer?) (listof exact-integer?))
  (struct node-item (max-len pref-len suff-len left-char right-char size) #:transparent)

  (define (merge-nodes l r)
    (let* ([l-max (node-item-max-len l)]
           [l-pref (node-item-pref-len l)]
           [l-suff (node-item-suff-len l)]
           [l-lchar (node-item-left-char l)]
           [l-rchar (node-item-right-char l)]
           [l-size (node-item-size l)]
           [r-max (node-item-max-len r)]
           [r-pref (node-item-pref-len r)]
           [r-suff (node-item-suff-len r)]
           [r-lchar (node-item-left-char r)]
           [r-rchar (node-item-right-char r)]
           [r-size (node-item-size r)]
           [res-max (max l-max r-max)]
           [res-pref l-pref]
           [res-suff r-suff])
      (if (char=? l-rchar r-lchar)
          (let* ([m1 (max res-max (+ l-suff r-pref))]
                 [p1 (if (= l-pref l-size) (+ l-size r-pref) l-pref)]
                 [s1 (if (= r-suff r-size) (+ r-size l-suff) r-suff)])
            (node-item m1 p1 s1 l-lchar r-rchar (+ l-size r-size)))
          (node-item res-max res-pref res-suff l-lchar r-rchar (+ l-size r-size)))))

  (define n (string-length s))
  (define s-vec (list->vector (string->list s)))
  (define tree (make-vector (* 4 n)))

  (define (build start end node)
    (if (= start end)
        (let ([char (vector-ref s-vec start)])
          (vector-set! tree node (node-item 1 1 1 char char 1)))
        (let* ([mid (quotient (+ start end) 2)]
               [lc (* 2 node)]
               [rc (+ (* 2 node) 1)])
          (build start mid lc)
          (build (+ mid 1) end rc)
          (vector-set! tree node (merge-nodes (vector-ref tree lc) (vector-ref tree rc))))))

  (define (update-tree start end node pos char)
    (if (= start end)
        (vector-set! tree node (node-item 1 1 1 char char 1))
        (let* ([mid (quotient (+ start end) 2)]
               [lc (* 2 node)]
               [rc (+ (* 2 node) 1)])
          (if (<= pos mid)
              (update-tree start mid lc pos char)
              (update-tree (+ mid 1) end rc pos char))
          (vector-set! tree node (merge-nodes (vector-ref tree lc) (vector-ref tree rc))))))

  (if (> n 0)
      (begin
        (build 0 (- n 1) 1)
        (for/list ([char (string->list queryCharacters)]
                   [idx queryIndices])
          (update-tree 0 (- n 1) 1 idx char)
          (node-item-max-len (vector-ref tree 1))))
      '()))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec longest_repeating(S :: unicode:unicode_binary(), QueryCharacters :: unicode:unicode_binary(), QueryIndices :: [integer()]) -> [integer()].
longest_repeating(S, QueryCharacters, QueryIndices) ->
  SList = unicode:characters_to_list(S),
  STuple = list_to_tuple(SList),
  N = length(SList),
  Tree = build_tree(0, N - 1, STuple),
  QChars = unicode:characters_to_list(QueryCharacters),
  Queries = lists:zip(QueryIndices, QChars),
  {Results, _} = lists:mapfoldl(fun({Idx, Char}, CurrentTree) ->
    NewTree = update_tree(0, N - 1, Idx, Char, CurrentTree),
    {MaxLen, _, _, _, _, _} = get_info(NewTree),
    {MaxLen, NewTree}
  end, Tree, Queries),
  Results.

build_tree(L, R, STuple) when L =:= R ->
  C = element(L + 1, STuple),
  {1, 1, 1, C, C, 1};
build_tree(L, R, STuple) ->
  Mid = (L + R) div 2,
  Left = build_tree(L, Mid, STuple),
  Right = build_tree(Mid + 1, R, STuple),
  {merge(get_info(Left), get_info(Right)), Left, Right}.

update_tree(L, R, Pos, Char, {_, Left, Right}) ->
  Mid = (L + R) div 2,
  {NewLeft, NewRight} = if
    Pos =< Mid -> {update_tree(L, Mid, Pos, Char, Left), Right};
    true -> {Left, update_tree(Mid + 1, R, Pos, Char, Right)}
  end,
  {merge(get_info(NewLeft), get_info(NewRight)), NewLeft, NewRight};
update_tree(_L, _R, _Pos, Char, _) ->
  {1, 1, 1, Char, Char, 1}.

get_info({Info, _, _}) -> Info;
get_info(Info) -> Info.

merge({MaxL, PrefL, SuffL, LCharL, RCharL, SizeL}, {MaxR, PrefR, SuffR, LCharR, RCharR, SizeR}) ->
  NewMax = if MaxL > MaxR -> MaxL; true -> MaxR end,
  {UpdatedMax, UpdatedPref, UpdatedSuff} = if RCharL =:= LCharR ->
    M1 = if (SuffL + PrefR) > NewMax -> SuffL + PrefR; true -> NewMax end,
    P1 = if PrefL =:= SizeL -> SizeL + PrefR; true -> PrefL end,
    S1 = if SuffR =:= SizeR -> SizeR + SuffL; true -> SuffR end,
    {M1, P1, S1};
  true ->
    {NewMax, PrefL, SuffR}
  end,
  {UpdatedMax, UpdatedPref, UpdatedSuff, LCharL, RCharR, SizeL + SizeR}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec longest_repeating(s :: String.t, query_characters :: String.t, query_indices :: [integer]) :: [integer]
  def longest_repeating(s, query_characters, query_indices) do
    s_list = String.to_charlist(s)
    s_tuple = List.to_tuple(s_list)
    n = length(s_list)
    tree = build_tree(0, n - 1, s_tuple)
    q_chars = String.to_charlist(query_characters)

    {results, _final_tree} = Enum.zip(query_indices, q_chars)
    |> Enum.map_reduce(tree, fn {idx, char}, current_tree ->
      new_tree = update_tree(0, n - 1, idx, char, current_tree)
      {max_len, _, _, _, _, _} = get_info(new_tree)
      {max_len, new_tree}
    end)
    results
  end

  defp build_tree(l, r, s_tuple) when l == r do
    c = elem(s_tuple, l)
    {1, 1, 1, c, c, 1}
  end
  defp build_tree(l, r, s_tuple) do
    mid = div(l + r, 2)
    left = build_tree(l, mid, s_tuple)
    right = build_tree(mid + 1, r, s_tuple)
    {merge(get_info(left), get_info(right)), left, right}
  end

  defp update_tree(l, r, pos, char, {_, left, right}) do
    mid = div(l + r, 2)
    {new_left, new_right} = if pos <= mid do
      {update_tree(l, mid, pos, char, left), right}
    else
      {left, update_tree(mid + 1, r, pos, char, right)}
    end
    {merge(get_info(new_left), get_info(new_right)), new_left, new_right}
  end
  defp update_tree(_l, _r, _pos, char, _) do
    {1, 1, 1, char, char, 1}
  end

  defp get_info({info, _, _}), do: info
  defp get_info(info), do: info

  defp merge({max_l, pref_l, suff_l, lc_l, rc_l, size_l}, {max_r, pref_r, suff_r, lc_r, rc_r, size_r}) do
    new_max = max(max_l, max_r)
    {updated_max, updated_pref, updated_suff} = if rc_l == lc_r do
      m1 = max(new_max, suff_l + pref_r)
      p1 = if pref_l == size_l, do: size_l + pref_r, else: pref_l
      s1 = if suff_r == size_r, do: size_r + suff_l, else: suff_r
      {m1, p1, s1}
    else
      {new_max, pref_l, suff_r}
    end
    {updated_max, updated_pref, updated_suff, lc_l, rc_r, size_l + size_r}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((n + k) log n) where n is the length of the string and k is the number of queries. Building the segment tree initially takes O(n) time, and each of the k point updates requires O(log n) time to traverse from the leaf to the root.
- **Space Complexity:** O(n) because the segment tree requires approximately 4n nodes for a recursive implementation or 2n nodes for an iterative implementation, with each node storing a fixed amount of character and integer information.
