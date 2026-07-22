---
layout: post
title: "Maximize Active Section with Trade II"
date: 2026-07-22 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "String", "Binary Search", "Segment Tree"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximize-active-section-with-trade-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> maxActiveSectionsAfterTrade(string\
        \ s, vector<vector<int>>& queries) {\n        int n = s.length();\n        vector<int>\
        \ s_list, e_list;\n        int total_ones = 0;\n        for (int i = 0; i <\
        \ n; ++i) {\n            if (s[i] == '1') {\n                int start = i;\n\
        \                while (i < n && s[i] == '1') {\n                    total_ones++;\n\
        \                    i++;\n                }\n                s_list.push_back(start);\n\
        \                e_list.push_back(i - 1);\n            }\n        }\n\n    \
        \    int m = s_list.size();\n        if (m == 0) {\n            return vector<int>(queries.size(),\
        \ 0);\n        }\n\n        vector<int> v(m);\n        for (int i = 0; i < m;\
        \ ++i) {\n            int prev_e = (i > 0) ? e_list[i - 1] : -1;\n         \
        \   int next_s = (i < m - 1) ? s_list[i + 1] : n;\n            v[i] = s_list[i]\
        \ - prev_e + next_s - e_list[i] - 2;\n        }\n\n        int size = 1;\n \
        \       while (size < m) size *= 2;\n        vector<int> tree(2 * size, -1);\n\
        \        for (int i = 0; i < m; ++i) tree[size + i] = v[i];\n        for (int\
        \ i = size - 1; i > 0; --i) tree[i] = max(tree[2 * i], tree[2 * i + 1]);\n\n\
        \        auto query_st = [&](int l, int r) {\n            int res = -1;\n  \
        \          for (l += size, r += size; l <= r; l >>= 1, r >>= 1) {\n        \
        \        if (l & 1) res = max(res, tree[l++]);\n                if (!(r & 1))\
        \ res = max(res, tree[r--]);\n            }\n            return res;\n     \
        \   };\n\n        vector<int> results;\n        for (const auto& q : queries)\
        \ {\n            int l = q[0], r = q[1];\n            int i_min = upper_bound(s_list.begin(),\
        \ s_list.end(), l) - s_list.begin();\n            int i_max = lower_bound(e_list.begin(),\
        \ e_list.end(), r) - e_list.begin() - 1;\n\n            if (i_min > i_max) {\n\
        \                results.push_back(total_ones);\n            } else if (i_min\
        \ == i_max) {\n                int prev_e = (i_min > 0) ? e_list[i_min - 1]\
        \ : -1;\n                int next_s = (i_min < m - 1) ? s_list[i_min + 1] :\
        \ n;\n                int gain = (s_list[i_min] - max(prev_e + 1, l)) + (min(next_s\
        \ - 1, r) - e_list[i_min]);\n                results.push_back(total_ones +\
        \ gain);\n            } else {\n                int gain1 = (s_list[i_min] -\
        \ max((i_min > 0 ? e_list[i_min - 1] : -1) + 1, l)) + (s_list[i_min + 1] - 1\
        \ - e_list[i_min]);\n                int gain2 = (s_list[i_max] - (e_list[i_max\
        \ - 1] + 1)) + (min((i_max < m - 1 ? s_list[i_max + 1] : n) - 1, r) - e_list[i_max]);\n\
        \                int gain3 = (i_min + 1 <= i_max - 1) ? query_st(i_min + 1,\
        \ i_max - 1) : -1;\n                results.push_back(total_ones + max({gain1,\
        \ gain2, gain3}));\n            }\n        }\n        return results;\n    }\n\
        };"
      java: "import java.util.*;\n\nclass Solution {\n    public List<Integer> maxActiveSectionsAfterTrade(String\
        \ s, int[][] queries) {\n        int n = s.length();\n        List<Integer>\
        \ sList = new ArrayList<>();\n        List<Integer> eList = new ArrayList<>();\n\
        \        int totalOnes = 0;\n        for (int i = 0; i < n; i++) {\n       \
        \     if (s.charAt(i) == '1') {\n                int start = i;\n          \
        \      while (i < n && s.charAt(i) == '1') {\n                    totalOnes++;\n\
        \                    i++;\n                }\n                sList.add(start);\n\
        \                eList.add(i - 1);\n            }\n        }\n\n        int\
        \ m = sList.size();\n        if (m == 0) {\n            List<Integer> res =\
        \ new ArrayList<>();\n            for (int i = 0; i < queries.length; i++) res.add(0);\n\
        \            return res;\n        }\n\n        int[] v = new int[m];\n     \
        \   for (int i = 0; i < m; i++) {\n            int prevE = (i > 0) ? eList.get(i\
        \ - 1) : -1;\n            int nextS = (i < m - 1) ? sList.get(i + 1) : n;\n\
        \            v[i] = sList.get(i) - prevE + nextS - eList.get(i) - 2;\n     \
        \   }\n\n        int size = 1;\n        while (size < m) size *= 2;\n      \
        \  int[] tree = new int[2 * size];\n        Arrays.fill(tree, -1);\n       \
        \ for (int i = 0; i < m; i++) tree[size + i] = v[i];\n        for (int i = size\
        \ - 1; i > 0; i--) tree[i] = Math.max(tree[2 * i], tree[2 * i + 1]);\n\n   \
        \     List<Integer> results = new ArrayList<>();\n        for (int[] q : queries)\
        \ {\n            int l = q[0], r = q[1];\n            int iMin = Collections.binarySearch(sList,\
        \ l + 1);\n            if (iMin < 0) iMin = -(iMin + 1);\n            int iMax\
        \ = Collections.binarySearch(eList, r);\n            if (iMax < 0) iMax = -(iMax\
        \ + 1) - 1;\n\n            if (iMin > iMax) {\n                results.add(totalOnes);\n\
        \            } else if (iMin == iMax) {\n                int prevE = (iMin >\
        \ 0) ? eList.get(iMin - 1) : -1;\n                int nextS = (iMin < m - 1)\
        \ ? sList.get(iMin + 1) : n;\n                int gain = (sList.get(iMin) -\
        \ Math.max(prevE + 1, l)) + (Math.min(nextS - 1, r) - eList.get(iMin));\n  \
        \              results.add(totalOnes + gain);\n            } else {\n      \
        \          int gain1 = (sList.get(iMin) - Math.max((iMin > 0 ? eList.get(iMin\
        \ - 1) : -1) + 1, l)) + (sList.get(iMin + 1) - 1 - eList.get(iMin));\n     \
        \           int gain2 = (sList.get(iMax) - (eList.get(iMax - 1) + 1)) + (Math.min((iMax\
        \ < m - 1 ? sList.get(iMax + 1) : n) - 1, r) - eList.get(iMax));\n         \
        \       int gain3 = -1;\n                if (iMin + 1 <= iMax - 1) {\n     \
        \               int qL = iMin + 1 + size, qR = iMax - 1 + size;\n          \
        \          while (qL <= qR) {\n                        if ((qL & 1) == 1) gain3\
        \ = Math.max(gain3, tree[qL++]);\n                        if ((qR & 1) == 0)\
        \ gain3 = Math.max(gain3, tree[qR--]);\n                        qL >>= 1; qR\
        \ >>= 1;\n                    }\n                }\n                results.add(totalOnes\
        \ + Math.max(gain1, Math.max(gain2, gain3)));\n            }\n        }\n  \
        \      return results;\n    }\n}"
      python: "import bisect\n\nclass Solution(object):\n    def maxActiveSectionsAfterTrade(self,\
        \ s, queries):\n        n = len(s)\n        s_list, e_list = [], []\n      \
        \  total_ones = 0\n        i = 0\n        while i < n:\n            if s[i]\
        \ == '1':\n                start = i\n                while i < n and s[i] ==\
        \ '1':\n                    total_ones += 1\n                    i += 1\n  \
        \              s_list.append(start)\n                e_list.append(i - 1)\n\
        \            else:\n                i += 1\n\n        m = len(s_list)\n    \
        \    if m == 0:\n            return [0] * len(queries)\n\n        v = [0] *\
        \ m\n        for i in range(m):\n            prev_e = e_list[i-1] if i > 0 else\
        \ -1\n            next_s = s_list[i+1] if i < m - 1 else n\n            v[i]\
        \ = s_list[i] - prev_e + next_s - e_list[i] - 2\n\n        size = 1\n      \
        \  while size < m: size *= 2\n        tree = [-1] * (2 * size)\n        for\
        \ i in range(m):\n            tree[size + i] = v[i]\n        for i in range(size\
        \ - 1, 0, -1):\n            tree[i] = max(tree[2 * i], tree[2 * i + 1])\n\n\
        \        def query_st(l, r):\n            res = -1\n            l += size\n\
        \            r += size\n            while l <= r:\n                if l % 2\
        \ == 1:\n                    res = max(res, tree[l])\n                    l\
        \ += 1\n                if r % 2 == 0:\n                    res = max(res, tree[r])\n\
        \                    r -= 1\n                l //= 2\n                r //=\
        \ 2\n            return res\n\n        results = []\n        for l, r in queries:\n\
        \            i_min = bisect.bisect_right(s_list, l)\n            i_max = bisect.bisect_left(e_list,\
        \ r) - 1\n\n            if i_min > i_max:\n                results.append(total_ones)\n\
        \            elif i_min == i_max:\n                prev_e = e_list[i_min - 1]\
        \ if i_min > 0 else -1\n                next_s = s_list[i_min + 1] if i_min\
        \ < m - 1 else n\n                gain = (s_list[i_min] - max(prev_e + 1, l))\
        \ + (min(next_s - 1, r) - e_list[i_min])\n                results.append(total_ones\
        \ + gain)\n            else:\n                prev_e_min = e_list[i_min - 1]\
        \ if i_min > 0 else -1\n                next_s_min = s_list[i_min + 1]\n   \
        \             gain1 = (s_list[i_min] - max(prev_e_min + 1, l)) + (next_s_min\
        \ - 1 - e_list[i_min])\n\n                prev_e_max = e_list[i_max - 1]\n \
        \               next_s_max = s_list[i_max + 1] if i_max < m - 1 else n\n   \
        \             gain2 = (s_list[i_max] - (prev_e_max + 1)) + (min(next_s_max -\
        \ 1, r) - e_list[i_max])\n\n                gain3 = query_st(i_min + 1, i_max\
        \ - 1) if i_min + 1 <= i_max - 1 else -1\n                results.append(total_ones\
        \ + max(gain1, gain2, gain3))\n\n        return results"
      python3: '// Generation failed for Python3

        // Reason: Parsing failed'
      c: '// Generation failed for C

        // Reason: Parsing failed'
      csharp: '// Generation failed for C#

        // Reason: Parsing failed'
      javascript: '// Generation failed for JavaScript

        // Reason: Parsing failed'
      typescript: '// Generation failed for TypeScript

        // Reason: Parsing failed'
      php: '// Generation failed for PHP

        // Reason: Parsing failed'
      swift: '// Generation failed for Swift

        // Reason: Parsing failed'
      kotlin: '// Generation failed for Kotlin

        // Reason: Parsing failed'
      dart: '// Generation failed for Dart

        // Reason: Parsing failed'
      go: '// Generation failed for Go

        // Reason: Parsing failed'
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
    approach: "The problem asks to maximize active sections ('1's) after at most one\
      \ trade. A trade is only possible if a block of '1's (an active section $O_i$)\
      \ is surrounded by '0's in the augmented string $t = '1' + s[l \\dots r] + '1'$.\
      \ This happens if $O_i$ is strictly contained within the substring range $[l,\
      \ r]$, i.e., $l < start_i$ and $end_i < r$. When $O_i$ is flipped to '0's, it\
      \ merges the adjacent '0' blocks ($Z_{i-1}$ and $Z_i$). The resulting larger '0'\
      \ block can then be flipped to '1's. The net gain in '1's from choosing segment\
      \ $O_i$ is the number of '0's in the original substring that are part of $Z_{i-1}$\
      \ and $Z_i$ within $[l, r]$. The total count of '1's in the entire string $s$\
      \ becomes $C + \text{length}(Z_{i-1} \\cap [l, r]) + \text{length}(Z_i \\cap [l,\
      \ r])$, where $C$ is the total number of '1's initially in $s$.\n\nTo efficiently\
      \ solve this for many queries, we precalculate the '1'-segments $O_i = [s_i, e_i]$.\
      \ For each query, we identify the range $[i_{min}, i_{max}]$ of '1'-segments that\
      \ are strictly within $[l, r]$ using binary search. If this range is not empty,\
      \ we need to maximize $G_i(l, r) = (s_i - \\max(e_{i-1}+1, l)) + (\\min(s_{i+1}-1,\
      \ r) - e_i)$ over $i \\in [i_{min}, i_{max}]$. For the boundaries $i_{min}$ and\
      \ $i_{max}$, the formula depends on $l$ and $r$; however, for any $i \\in (i_{min},\
      \ i_{max})$, the formula simplifies to $V_i = s_i - e_{i-1} + s_{i+1} - e_i -\
      \ 2$, which is independent of $l$ and $r$. We can build a segment tree on these\
      \ $V_i$ values to perform Range Maximum Queries in logarithmic time."
    time_complexity: O(n + Q log n) where n is the length of string s and Q is the number
      of queries. Decomposing s takes O(n), building the segment tree takes O(n), and
      each query takes O(log n) for binary searches and segment tree lookup.
    space_complexity: O(n) to store the indices of the '1'-segments and the segment
      tree nodes.
    elapsed_time: 528.6127851009369
    model: gemini-3-flash-preview
    generated_at: '2026-07-22 02:04:19 '
---

## Problem #3501: Maximize Active Section with Trade II

**Difficulty:** Hard

**Topics:** Array, String, Binary Search, Segment Tree

## Problem Description

<p>You are given a binary string <code>s</code> of length <code>n</code>, where:</p>

<ul>
	<li><code>&#39;1&#39;</code> represents an <strong>active</strong> section.</li>
	<li><code>&#39;0&#39;</code> represents an <strong>inactive</strong> section.</li>
</ul>

<p>You can perform <strong>at most one trade</strong> to maximize the number of active sections in <code>s</code>. In a trade, you:</p>

<ul>
	<li>Convert a contiguous block of <code>&#39;1&#39;</code>s that is surrounded by <code>&#39;0&#39;</code>s to all <code>&#39;0&#39;</code>s.</li>
	<li>Afterward, convert a contiguous block of <code>&#39;0&#39;</code>s that is surrounded by <code>&#39;1&#39;</code>s to all <code>&#39;1&#39;</code>s.</li>
</ul>

<p>Additionally, you are given a <strong>2D array</strong> <code>queries</code>, where <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> represents a <span data-keyword="substring-nonempty">substring</span> <code>s[l<sub>i</sub>...r<sub>i</sub>]</code>.</p>

<p>For each query, determine the <strong>maximum</strong> possible number of active sections in <code>s</code> after making the optimal trade on the substring <code>s[l<sub>i</sub>...r<sub>i</sub>]</code>.</p>

<p>Return an array <code>answer</code>, where <code>answer[i]</code> is the result for <code>queries[i]</code>.</p>

<p><strong>Note</strong></p>

<ul>
	<li>For each query, treat <code>s[l<sub>i</sub>...r<sub>i</sub>]</code> as if it is <strong>augmented</strong> with a <code>&#39;1&#39;</code> at both ends, forming <code>t = &#39;1&#39; + s[l<sub>i</sub>...r<sub>i</sub>] + &#39;1&#39;</code>. The augmented <code>&#39;1&#39;</code>s <strong>do not</strong> contribute to the final count.</li>
	<li>The queries are independent of each other.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;01&quot;, queries = [[0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1]</span></p>

<p><strong>Explanation:</strong></p>

<p>Because there is no block of <code>&#39;1&#39;</code>s surrounded by <code>&#39;0&#39;</code>s, no valid trade is possible. The maximum number of active sections is 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;0100&quot;, queries = [[0,3],[0,2],[1,3],[2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[4,3,1,1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>
	<p>Query <code>[0, 3]</code> &rarr; Substring <code>&quot;0100&quot;</code> &rarr; Augmented to <code>&quot;101001&quot;</code><br />
	Choose <code>&quot;0100&quot;</code>, convert <code>&quot;0100&quot;</code> &rarr; <code>&quot;0000&quot;</code> &rarr; <code>&quot;1111&quot;</code>.<br />
	The final string without augmentation is <code>&quot;1111&quot;</code>. The maximum number of active sections is 4.</p>
	</li>
	<li>
	<p>Query <code>[0, 2]</code> &rarr; Substring <code>&quot;010&quot;</code> &rarr; Augmented to <code>&quot;10101&quot;</code><br />
	Choose <code>&quot;010&quot;</code>, convert <code>&quot;010&quot;</code> &rarr; <code>&quot;000&quot;</code> &rarr; <code>&quot;111&quot;</code>.<br />
	The final string without augmentation is <code>&quot;1110&quot;</code>. The maximum number of active sections is 3.</p>
	</li>
	<li>
	<p>Query <code>[1, 3]</code> &rarr; Substring <code>&quot;100&quot;</code> &rarr; Augmented to <code>&quot;11001&quot;</code><br />
	Because there is no block of <code>&#39;1&#39;</code>s surrounded by <code>&#39;0&#39;</code>s, no valid trade is possible. The maximum number of active sections is 1.</p>
	</li>
	<li>
	<p>Query <code>[2, 3]</code> &rarr; Substring <code>&quot;00&quot;</code> &rarr; Augmented to <code>&quot;1001&quot;</code><br />
	Because there is no block of <code>&#39;1&#39;</code>s surrounded by <code>&#39;0&#39;</code>s, no valid trade is possible. The maximum number of active sections is 1.</p>
	</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;1000100&quot;, queries = [[1,5],[0,6],[0,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[6,7,2]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li data-end="383" data-start="217">
	<p data-end="383" data-start="219">Query <code>[1, 5]</code> &rarr; Substring <code data-end="255" data-start="246">&quot;00010&quot;</code> &rarr; Augmented to <code data-end="282" data-start="271">&quot;1000101&quot;</code><br data-end="285" data-start="282" />
	Choose <code data-end="303" data-start="294">&quot;00010&quot;</code>, convert <code data-end="322" data-start="313">&quot;00010&quot;</code> &rarr; <code data-end="322" data-start="313">&quot;00000&quot;</code> &rarr; <code data-end="334" data-start="325">&quot;11111&quot;</code>.<br />
	The final string without augmentation is <code data-end="404" data-start="396">&quot;1111110&quot;</code>. The maximum number of active sections is 6.</p>
	</li>
	<li data-end="561" data-start="385">
	<p data-end="561" data-start="387">Query <code>[0, 6]</code> &rarr; Substring <code data-end="425" data-start="414">&quot;1000100&quot;</code> &rarr; Augmented to <code data-end="454" data-start="441">&quot;110001001&quot;</code><br data-end="457" data-start="454" />
	Choose <code data-end="477" data-start="466">&quot;000100&quot;</code>, convert <code data-end="498" data-start="487">&quot;000100&quot;</code> &rarr; <code data-end="498" data-start="487">&quot;000000&quot;</code> &rarr; <code data-end="512" data-start="501">&quot;111111&quot;</code>.<br />
	The final string without augmentation is <code data-end="404" data-start="396">&quot;1111111&quot;</code>. The maximum number of active sections is 7.</p>
	</li>
	<li data-end="741" data-start="563">
	<p data-end="741" data-start="565">Query <code>[0, 4]</code> &rarr; Substring <code data-end="601" data-start="592">&quot;10001&quot;</code> &rarr; Augmented to <code data-end="627" data-start="617">&quot;1100011&quot;</code><br data-end="630" data-start="627" />
	Because there is no block of <code>&#39;1&#39;</code>s surrounded by <code>&#39;0&#39;</code>s, no valid trade is possible. The maximum number of active sections is 2.</p>
	</li>
</ul>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;01010&quot;, queries = [[0,3],[1,4],[1,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[4,4,2]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>
	<p>Query <code>[0, 3]</code> &rarr; Substring <code>&quot;0101&quot;</code> &rarr; Augmented to <code>&quot;101011&quot;</code><br />
	Choose <code>&quot;010&quot;</code>, convert <code>&quot;010&quot;</code> &rarr; <code>&quot;000&quot;</code> &rarr; <code>&quot;111&quot;</code>.<br />
	The final string without augmentation is <code>&quot;11110&quot;</code>. The maximum number of active sections is 4.</p>
	</li>
	<li>
	<p>Query <code>[1, 4]</code> &rarr; Substring <code>&quot;1010&quot;</code> &rarr; Augmented to <code>&quot;110101&quot;</code><br />
	Choose <code>&quot;010&quot;</code>, convert <code>&quot;010&quot;</code> &rarr; <code>&quot;000&quot;</code> &rarr; <code>&quot;111&quot;</code>.<br />
	The final string without augmentation is <code>&quot;01111&quot;</code>. The maximum number of active sections is 4.</p>
	</li>
	<li>
	<p>Query <code>[1, 3]</code> &rarr; Substring <code>&quot;101&quot;</code> &rarr; Augmented to <code>&quot;11011&quot;</code><br />
	Because there is no block of <code>&#39;1&#39;</code>s surrounded by <code>&#39;0&#39;</code>s, no valid trade is possible. The maximum number of active sections is 2.</p>
	</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt; n</code></li>
</ul>


## Hints

1. Split consecutive zeros and ones into segments and give each segment an ID.

2. The answer should be the maximum of `ans[i] = len[i - 1] + len[i + 1]`, where `i` is a one-segment.

3. For a zero-segment, define `ans[i] = 0`.

4. Note that all three segments (`i - 1`, `i`, and `i + 1`) should be fully covered by the substring.

5. Use a segment tree to perform range maximum queries on the answer. The query to the segment tree is not straightforward since we need to ensure the zero-segments are fully covered. Handle the first and last segments separately.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to maximize active sections ('1's) after at most one trade. A trade is only possible if a block of '1's (an active section $O_i$) is surrounded by '0's in the augmented string $t = '1' + s[l \dots r] + '1'$. This happens if $O_i$ is strictly contained within the substring range $[l, r]$, i.e., $l < start_i$ and $end_i < r$. When $O_i$ is flipped to '0's, it merges the adjacent '0' blocks ($Z_{i-1}$ and $Z_i$). The resulting larger '0' block can then be flipped to '1's. The net gain in '1's from choosing segment $O_i$ is the number of '0's in the original substring that are part of $Z_{i-1}$ and $Z_i$ within $[l, r]$. The total count of '1's in the entire string $s$ becomes $C + 	ext{length}(Z_{i-1} \cap [l, r]) + 	ext{length}(Z_i \cap [l, r])$, where $C$ is the total number of '1's initially in $s$.

To efficiently solve this for many queries, we precalculate the '1'-segments $O_i = [s_i, e_i]$. For each query, we identify the range $[i_{min}, i_{max}]$ of '1'-segments that are strictly within $[l, r]$ using binary search. If this range is not empty, we need to maximize $G_i(l, r) = (s_i - \max(e_{i-1}+1, l)) + (\min(s_{i+1}-1, r) - e_i)$ over $i \in [i_{min}, i_{max}]$. For the boundaries $i_{min}$ and $i_{max}$, the formula depends on $l$ and $r$; however, for any $i \in (i_{min}, i_{max})$, the formula simplifies to $V_i = s_i - e_{i-1} + s_{i+1} - e_i - 2$, which is independent of $l$ and $r$. We can build a segment tree on these $V_i$ values to perform Range Maximum Queries in logarithmic time.

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
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.length();
        vector<int> s_list, e_list;
        int total_ones = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '1') {
                int start = i;
                while (i < n && s[i] == '1') {
                    total_ones++;
                    i++;
                }
                s_list.push_back(start);
                e_list.push_back(i - 1);
            }
        }

        int m = s_list.size();
        if (m == 0) {
            return vector<int>(queries.size(), 0);
        }

        vector<int> v(m);
        for (int i = 0; i < m; ++i) {
            int prev_e = (i > 0) ? e_list[i - 1] : -1;
            int next_s = (i < m - 1) ? s_list[i + 1] : n;
            v[i] = s_list[i] - prev_e + next_s - e_list[i] - 2;
        }

        int size = 1;
        while (size < m) size *= 2;
        vector<int> tree(2 * size, -1);
        for (int i = 0; i < m; ++i) tree[size + i] = v[i];
        for (int i = size - 1; i > 0; --i) tree[i] = max(tree[2 * i], tree[2 * i + 1]);

        auto query_st = [&](int l, int r) {
            int res = -1;
            for (l += size, r += size; l <= r; l >>= 1, r >>= 1) {
                if (l & 1) res = max(res, tree[l++]);
                if (!(r & 1)) res = max(res, tree[r--]);
            }
            return res;
        };

        vector<int> results;
        for (const auto& q : queries) {
            int l = q[0], r = q[1];
            int i_min = upper_bound(s_list.begin(), s_list.end(), l) - s_list.begin();
            int i_max = lower_bound(e_list.begin(), e_list.end(), r) - e_list.begin() - 1;

            if (i_min > i_max) {
                results.push_back(total_ones);
            } else if (i_min == i_max) {
                int prev_e = (i_min > 0) ? e_list[i_min - 1] : -1;
                int next_s = (i_min < m - 1) ? s_list[i_min + 1] : n;
                int gain = (s_list[i_min] - max(prev_e + 1, l)) + (min(next_s - 1, r) - e_list[i_min]);
                results.push_back(total_ones + gain);
            } else {
                int gain1 = (s_list[i_min] - max((i_min > 0 ? e_list[i_min - 1] : -1) + 1, l)) + (s_list[i_min + 1] - 1 - e_list[i_min]);
                int gain2 = (s_list[i_max] - (e_list[i_max - 1] + 1)) + (min((i_max < m - 1 ? s_list[i_max + 1] : n) - 1, r) - e_list[i_max]);
                int gain3 = (i_min + 1 <= i_max - 1) ? query_st(i_min + 1, i_max - 1) : -1;
                results.push_back(total_ones + max({gain1, gain2, gain3}));
            }
        }
        return results;
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
    public List<Integer> maxActiveSectionsAfterTrade(String s, int[][] queries) {
        int n = s.length();
        List<Integer> sList = new ArrayList<>();
        List<Integer> eList = new ArrayList<>();
        int totalOnes = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                int start = i;
                while (i < n && s.charAt(i) == '1') {
                    totalOnes++;
                    i++;
                }
                sList.add(start);
                eList.add(i - 1);
            }
        }

        int m = sList.size();
        if (m == 0) {
            List<Integer> res = new ArrayList<>();
            for (int i = 0; i < queries.length; i++) res.add(0);
            return res;
        }

        int[] v = new int[m];
        for (int i = 0; i < m; i++) {
            int prevE = (i > 0) ? eList.get(i - 1) : -1;
            int nextS = (i < m - 1) ? sList.get(i + 1) : n;
            v[i] = sList.get(i) - prevE + nextS - eList.get(i) - 2;
        }

        int size = 1;
        while (size < m) size *= 2;
        int[] tree = new int[2 * size];
        Arrays.fill(tree, -1);
        for (int i = 0; i < m; i++) tree[size + i] = v[i];
        for (int i = size - 1; i > 0; i--) tree[i] = Math.max(tree[2 * i], tree[2 * i + 1]);

        List<Integer> results = new ArrayList<>();
        for (int[] q : queries) {
            int l = q[0], r = q[1];
            int iMin = Collections.binarySearch(sList, l + 1);
            if (iMin < 0) iMin = -(iMin + 1);
            int iMax = Collections.binarySearch(eList, r);
            if (iMax < 0) iMax = -(iMax + 1) - 1;

            if (iMin > iMax) {
                results.add(totalOnes);
            } else if (iMin == iMax) {
                int prevE = (iMin > 0) ? eList.get(iMin - 1) : -1;
                int nextS = (iMin < m - 1) ? sList.get(iMin + 1) : n;
                int gain = (sList.get(iMin) - Math.max(prevE + 1, l)) + (Math.min(nextS - 1, r) - eList.get(iMin));
                results.add(totalOnes + gain);
            } else {
                int gain1 = (sList.get(iMin) - Math.max((iMin > 0 ? eList.get(iMin - 1) : -1) + 1, l)) + (sList.get(iMin + 1) - 1 - eList.get(iMin));
                int gain2 = (sList.get(iMax) - (eList.get(iMax - 1) + 1)) + (Math.min((iMax < m - 1 ? sList.get(iMax + 1) : n) - 1, r) - eList.get(iMax));
                int gain3 = -1;
                if (iMin + 1 <= iMax - 1) {
                    int qL = iMin + 1 + size, qR = iMax - 1 + size;
                    while (qL <= qR) {
                        if ((qL & 1) == 1) gain3 = Math.max(gain3, tree[qL++]);
                        if ((qR & 1) == 0) gain3 = Math.max(gain3, tree[qR--]);
                        qL >>= 1; qR >>= 1;
                    }
                }
                results.add(totalOnes + Math.max(gain1, Math.max(gain2, gain3)));
            }
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
import bisect

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        s_list, e_list = [], []
        total_ones = 0
        i = 0
        while i < n:
            if s[i] == '1':
                start = i
                while i < n and s[i] == '1':
                    total_ones += 1
                    i += 1
                s_list.append(start)
                e_list.append(i - 1)
            else:
                i += 1

        m = len(s_list)
        if m == 0:
            return [0] * len(queries)

        v = [0] * m
        for i in range(m):
            prev_e = e_list[i-1] if i > 0 else -1
            next_s = s_list[i+1] if i < m - 1 else n
            v[i] = s_list[i] - prev_e + next_s - e_list[i] - 2

        size = 1
        while size < m: size *= 2
        tree = [-1] * (2 * size)
        for i in range(m):
            tree[size + i] = v[i]
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def query_st(l, r):
            res = -1
            l += size
            r += size
            while l <= r:
                if l % 2 == 1:
                    res = max(res, tree[l])
                    l += 1
                if r % 2 == 0:
                    res = max(res, tree[r])
                    r -= 1
                l //= 2
                r //= 2
            return res

        results = []
        for l, r in queries:
            i_min = bisect.bisect_right(s_list, l)
            i_max = bisect.bisect_left(e_list, r) - 1

            if i_min > i_max:
                results.append(total_ones)
            elif i_min == i_max:
                prev_e = e_list[i_min - 1] if i_min > 0 else -1
                next_s = s_list[i_min + 1] if i_min < m - 1 else n
                gain = (s_list[i_min] - max(prev_e + 1, l)) + (min(next_s - 1, r) - e_list[i_min])
                results.append(total_ones + gain)
            else:
                prev_e_min = e_list[i_min - 1] if i_min > 0 else -1
                next_s_min = s_list[i_min + 1]
                gain1 = (s_list[i_min] - max(prev_e_min + 1, l)) + (next_s_min - 1 - e_list[i_min])

                prev_e_max = e_list[i_max - 1]
                next_s_max = s_list[i_max + 1] if i_max < m - 1 else n
                gain2 = (s_list[i_max] - (prev_e_max + 1)) + (min(next_s_max - 1, r) - e_list[i_max])

                gain3 = query_st(i_min + 1, i_max - 1) if i_min + 1 <= i_max - 1 else -1
                results.append(total_ones + max(gain1, gain2, gain3))

        return results
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: Parsing failed
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

- **Time Complexity:** O(n + Q log n) where n is the length of string s and Q is the number of queries. Decomposing s takes O(n), building the segment tree takes O(n), and each query takes O(log n) for binary searches and segment tree lookup.
- **Space Complexity:** O(n) to store the indices of the '1'-segments and the segment tree nodes.
