---
layout: post
title: "Path Existence Queries in a Graph I"
date: 2026-07-09 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Binary Search", "Union-Find", "Graph Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/path-existence-queries-in-a-graph-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<bool> pathExistenceQueries(int n,\
        \ vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {\n        vector<int>\
        \ componentId(n);\n        componentId[0] = 0;\n        int currentId = 0;\n\
        \        for (int i = 1; i < n; ++i) {\n            if (nums[i] - nums[i - 1]\
        \ > maxDiff) {\n                currentId++;\n            }\n            componentId[i]\
        \ = currentId;\n        }\n\n        int q = queries.size();\n        vector<bool>\
        \ result(q);\n        for (int i = 0; i < q; ++i) {\n            result[i] =\
        \ (componentId[queries[i][0]] == componentId[queries[i][1]]);\n        }\n \
        \       return result;\n    }\n};"
      java: "class Solution {\n    public boolean[] pathExistenceQueries(int n, int[]\
        \ nums, int maxDiff, int[][] queries) {\n        int[] componentId = new int[n];\n\
        \        componentId[0] = 0;\n        int currentId = 0;\n        for (int i\
        \ = 1; i < n; i++) {\n            if (nums[i] - nums[i - 1] > maxDiff) {\n \
        \               currentId++;\n            }\n            componentId[i] = currentId;\n\
        \        }\n\n        boolean[] result = new boolean[queries.length];\n    \
        \    for (int i = 0; i < queries.length; i++) {\n            result[i] = (componentId[queries[i][0]]\
        \ == componentId[queries[i][1]]);\n        }\n        return result;\n    }\n\
        }"
      python: "class Solution(object):\n    def pathExistenceQueries(self, n, nums,\
        \ maxDiff, queries):\n        \"\"\"\n        :type n: int\n        :type nums:\
        \ List[int]\n        :type maxDiff: int\n        :type queries: List[List[int]]\n\
        \        :rtype: List[bool]\n        \"\"\"\n        component_id = [0] * n\n\
        \        curr_id = 0\n        for i in range(1, n):\n            if nums[i]\
        \ - nums[i - 1] > maxDiff:\n                curr_id += 1\n            component_id[i]\
        \ = curr_id\n\n        result = []\n        for u, v in queries:\n         \
        \   result.append(component_id[u] == component_id[v])\n        return result"
      python3: "class Solution:\n    def pathExistenceQueries(self, n: int, nums: List[int],\
        \ maxDiff: int, queries: List[List[int]]) -> List[bool]:\n        component_id\
        \ = [0] * n\n        curr_id = 0\n        for i in range(1, n):\n          \
        \  if nums[i] - nums[i - 1] > maxDiff:\n                curr_id += 1\n     \
        \       component_id[i] = curr_id\n\n        return [component_id[u] == component_id[v]\
        \ for u, v in queries]"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nbool* pathExistenceQueries(int n, int* nums, int numsSize, int maxDiff,\
        \ int** queries, int queriesSize, int* queriesColSize, int* returnSize) {\n\
        \    int* componentId = (int*)malloc(n * sizeof(int));\n    componentId[0] =\
        \ 0;\n    int currentId = 0;\n    for (int i = 1; i < n; i++) {\n        if\
        \ (nums[i] - nums[i - 1] > maxDiff) {\n            currentId++;\n        }\n\
        \        componentId[i] = currentId;\n    }\n\n    bool* result = (bool*)malloc(queriesSize\
        \ * sizeof(bool));\n    for (int i = 0; i < queriesSize; i++) {\n        int\
        \ u = queries[i][0];\n        int v = queries[i][1];\n        result[i] = (componentId[u]\
        \ == componentId[v]);\n    }\n\n    free(componentId);\n    *returnSize = queriesSize;\n\
        \    return result;\n}"
      csharp: "public class Solution {\n    public bool[] PathExistenceQueries(int n,\
        \ int[] nums, int maxDiff, int[][] queries) {\n        int[] compId = new int[n];\n\
        \        int curr = 0;\n        compId[0] = 0;\n        for (int i = 1; i <\
        \ n; i++) {\n            if (nums[i] - nums[i - 1] > maxDiff) {\n          \
        \      curr++;\n            }\n            compId[i] = curr;\n        }\n\n\
        \        int m = queries.Length;\n        bool[] result = new bool[m];\n   \
        \     for (int i = 0; i < m; i++) {\n            int u = queries[i][0];\n  \
        \          int v = queries[i][1];\n            result[i] = compId[u] == compId[v];\n\
        \        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[]} nums\n * @param {number}\
        \ maxDiff\n * @param {number[][]} queries\n * @return {boolean[]}\n */\nvar\
        \ pathExistenceQueries = function(n, nums, maxDiff, queries) {\n    const compId\
        \ = new Int32Array(n);\n    let curr = 0;\n    compId[0] = 0;\n    for (let\
        \ i = 1; i < n; i++) {\n        if (nums[i] - nums[i - 1] > maxDiff) {\n   \
        \         curr++;\n        }\n        compId[i] = curr;\n    }\n\n    const\
        \ m = queries.length;\n    const result = new Array(m);\n    for (let i = 0;\
        \ i < m; i++) {\n        const u = queries[i][0];\n        const v = queries[i][1];\n\
        \        result[i] = compId[u] === compId[v];\n    }\n    return result;\n};"
      typescript: "function pathExistenceQueries(n: number, nums: number[], maxDiff:\
        \ number, queries: number[][]): boolean[] {\n    const compId: Int32Array =\
        \ new Int32Array(n);\n    let curr: number = 0;\n    compId[0] = 0;\n    for\
        \ (let i = 1; i < n; i++) {\n        if (nums[i] - nums[i - 1] > maxDiff) {\n\
        \            curr++;\n        }\n        compId[i] = curr;\n    }\n\n    const\
        \ m: number = queries.length;\n    const result: boolean[] = new Array(m);\n\
        \    for (let i = 0; i < m; i++) {\n        const u: number = queries[i][0];\n\
        \        const v: number = queries[i][1];\n        result[i] = compId[u] ===\
        \ compId[v];\n    }\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[]\
        \ $nums\n     * @param Integer $maxDiff\n     * @param Integer[][] $queries\n\
        \     * @return Boolean[]\n     */\n    function pathExistenceQueries($n, $nums,\
        \ $maxDiff, $queries) {\n        $compId = array_fill(0, $n, 0);\n        $curr\
        \ = 0;\n        for ($i = 1; $i < $n; $i++) {\n            if ($nums[$i] - $nums[$i\
        \ - 1] > $maxDiff) {\n                $curr++;\n            }\n            $compId[$i]\
        \ = $curr;\n        }\n\n        $result = [];\n        foreach ($queries as\
        \ $q) {\n            $u = $q[0];\n            $v = $q[1];\n            $result[]\
        \ = $compId[$u] === $compId[$v];\n        }\n        return $result;\n    }\n\
        }"
      swift: "class Solution {\n    func pathExistenceQueries(_ n: Int, _ nums: [Int],\
        \ _ maxDiff: Int, _ queries: [[Int]]) -> [Bool] {\n        var compId = Array(repeating:\
        \ 0, count: n)\n        var curr = 0\n        for i in 1..<n {\n           \
        \ if nums[i] - nums[i - 1] > maxDiff {\n                curr += 1\n        \
        \    }\n            compId[i] = curr\n        }\n\n        return queries.map\
        \ { q in\n            compId[q[0]] == compId[q[1]]\n        }\n    }\n}"
      kotlin: "class Solution {\n    fun pathExistenceQueries(n: Int, nums: IntArray,\
        \ maxDiff: Int, queries: Array<IntArray>): BooleanArray {\n        val comp\
        \ = IntArray(n)\n        comp[0] = 0\n        for (i in 1 until n) {\n     \
        \       if (nums[i] - nums[i - 1] <= maxDiff) {\n                comp[i] = comp[i\
        \ - 1]\n            } else {\n                comp[i] = comp[i - 1] + 1\n  \
        \          }\n        }\n\n        val answer = BooleanArray(queries.size)\n\
        \        for (i in queries.indices) {\n            val u = queries[i][0]\n \
        \           val v = queries[i][1]\n            answer[i] = comp[u] == comp[v]\n\
        \        }\n        return answer\n    }\n}"
      dart: "class Solution {\n  List<bool> pathExistenceQueries(int n, List<int> nums,\
        \ int maxDiff, List<List<int>> queries) {\n    List<int> comp = List<int>.filled(n,\
        \ 0);\n    for (int i = 1; i < n; i++) {\n      if (nums[i] - nums[i - 1] <=\
        \ maxDiff) {\n        comp[i] = comp[i - 1];\n      } else {\n        comp[i]\
        \ = comp[i - 1] + 1;\n      }\n    }\n\n    List<bool> result = List<bool>.filled(queries.length,\
        \ false);\n    for (int i = 0; i < queries.length; i++) {\n      int u = queries[i][0];\n\
        \      int v = queries[i][1];\n      result[i] = comp[u] == comp[v];\n    }\n\
        \    return result;\n  }\n}"
      go: "func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int)\
        \ []bool {\n    comp := make([]int, n)\n    comp[0] = 0\n    for i := 1; i <\
        \ n; i++ {\n        if nums[i]-nums[i-1] <= maxDiff {\n            comp[i] =\
        \ comp[i-1]\n        } else {\n            comp[i] = comp[i-1] + 1\n       \
        \ }\n    }\n\n    answer := make([]bool, len(queries))\n    for i, q := range\
        \ queries {\n        u, v := q[0], q[1]\n        answer[i] = comp[u] == comp[v]\n\
        \    }\n    return answer\n}"
      ruby: "# @param {Integer} n\n# @param {Integer[]} nums\n# @param {Integer} max_diff\n\
        # @param {Integer[][]} queries\n# @return {Boolean[]}\ndef path_existence_queries(n,\
        \ nums, max_diff, queries)\n  comp = Array.new(n, 0)\n  (1...n).each do |i|\n\
        \    if nums[i] - nums[i - 1] <= max_diff\n      comp[i] = comp[i - 1]\n   \
        \ else\n      comp[i] = comp[i - 1] + 1\n    end\n  end\n\n  queries.map do\
        \ |u, v|\n    comp[u] == comp[v]\n  end\nend"
      scala: "object Solution {\n    def pathExistenceQueries(n: Int, nums: Array[Int],\
        \ maxDiff: Int, queries: Array[Array[Int]]): Array[Boolean] = {\n        val\
        \ comp = new Array[Int](n)\n        comp(0) = 0\n        var i = 1\n       \
        \ while (i < n) {\n            if (nums(i) - nums(i - 1) <= maxDiff) {\n   \
        \             comp(i) = comp(i - 1)\n            } else {\n                comp(i)\
        \ = comp(i - 1) + 1\n            }\n            i += 1\n        }\n\n      \
        \  val result = new Array[Boolean](queries.length)\n        var j = 0\n    \
        \    while (j < queries.length) {\n            val u = queries(j)(0)\n     \
        \       val v = queries(j)(1)\n            result(j) = comp(u) == comp(v)\n\
        \            j += 1\n        }\n        result\n    }\n}"
      rust: "impl Solution {\n    pub fn path_existence_queries(n: i32, nums: Vec<i32>,\
        \ max_diff: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {\n        let n = n as\
        \ usize;\n        let mut component_ids = vec![0; n];\n        let mut curr_id\
        \ = 0;\n\n        if n > 1 {\n            for i in 1..n {\n                if\
        \ nums[i] - nums[i - 1] > max_diff {\n                    curr_id += 1;\n  \
        \              }\n                component_ids[i] = curr_id;\n            }\n\
        \        }\n\n        queries\n            .into_iter()\n            .map(|q|\
        \ {\n                let u = q[0] as usize;\n                let v = q[1] as\
        \ usize;\n                component_ids[u] == component_ids[v]\n           \
        \ })\n            .collect()\n    }\n}"
      racket: "(define/contract (path-existence-queries n nums maxDiff queries)\n  (->\
        \ exact-integer? (listof exact-integer?) exact-integer? (listof (listof exact-integer?))\
        \ (listof boolean?))\n  (let* ([nums-vec (list->vector nums)]\n         [comp-ids\
        \ (make-vector n 0)]\n         [curr-id 0])\n    (for ([i (in-range 1 n)])\n\
        \      (when (> (- (vector-ref nums-vec i) (vector-ref nums-vec (- i 1))) maxDiff)\n\
        \        (set! curr-id (+ curr-id 1)))\n      (vector-set! comp-ids i curr-id))\n\
        \    (map (lambda (q)\n           (let ([u (car q)]\n                 [v (cadr\
        \ q)])\n             (= (vector-ref comp-ids u) (vector-ref comp-ids v))))\n\
        \         queries)))"
      erlang: "-spec path_existence_queries(N :: integer(), Nums :: [integer()], MaxDiff\
        \ :: integer(), Queries :: [[integer()]]) -> [boolean()].\npath_existence_queries(N,\
        \ Nums, MaxDiff, Queries) ->\n    CompIds = compute_comp_ids(Nums, MaxDiff),\n\
        \    CompVec = list_to_tuple(CompIds),\n    [element(U + 1, CompVec) =:= element(V\
        \ + 1, CompVec) || [U, V] <- Queries].\n\ncompute_comp_ids([H | T], MaxDiff)\
        \ ->\n    compute_comp_ids(T, H, 0, [0], MaxDiff).\n\ncompute_comp_ids([], _Prev,\
        \ _CurrId, Acc, _MaxDiff) ->\n    lists:reverse(Acc);\ncompute_comp_ids([H |\
        \ T], Prev, CurrId, Acc, MaxDiff) ->\n    NextId = if (H - Prev) > MaxDiff ->\
        \ CurrId + 1; true -> CurrId end,\n    compute_comp_ids(T, H, NextId, [NextId\
        \ | Acc], MaxDiff)."
      elixir: "defmodule Solution do\n  @spec path_existence_queries(n :: integer, nums\
        \ :: [integer], max_diff :: integer, queries :: [[integer]]) :: [boolean]\n\
        \  def path_existence_queries(n, nums, max_diff, queries) do\n    [first | rest]\
        \ = nums\n    {_, comp_ids_rev} = Enum.reduce(rest, {first, [0]}, fn curr, {prev,\
        \ [curr_id | _] = acc} ->\n      new_id = if curr - prev > max_diff, do: curr_id\
        \ + 1, else: curr_id\n      {curr, [new_id | acc]}\n    end)\n\n    comp_vec\
        \ = Enum.reverse(comp_ids_rev) |> List.to_tuple()\n\n    Enum.map(queries, fn\
        \ [u, v] ->\n      elem(comp_vec, u) == elem(comp_vec, v)\n    end)\n  end\n\
        end"
    approach: 'The core observation for this problem is that because the input array
      is sorted in non-decreasing order, the connected components of the graph must
      consist of contiguous segments of indices. If the difference between any two adjacent
      elements in the sorted array, nums[i] and nums[i-1], exceeds maxDiff, no edge
      can exist between any node in the set {0, ..., i-1} and any node in the set {i,
      ..., n-1}. This is because for any a < i and b >= i, the difference nums[b] -
      nums[a] will be at least as large as nums[i] - nums[i-1].


      To solve the problem efficiently, we can pre-calculate the connected components
      in a single O(n) pass. We maintain a component identifier that starts at 0 and
      increments whenever the gap between adjacent elements in the sorted array is greater
      than maxDiff. After storing these identifiers in an array, we can answer each
      query [u, v] in O(1) time by checking if nodes u and v belong to the same component
      (i.e., whether their identifiers are equal).'
    time_complexity: O(n + q) where n is the number of nodes and q is the number of
      queries. We iterate through the sorted array once to compute connected components
      in O(n) and then iterate through the queries to answer each in O(1), leading to
      a total time complexity of O(n + q).
    space_complexity: O(n) where n is the number of nodes. We need an auxiliary array
      of size n to store the component identifier for each node. The space for the result
      array is O(q), which is often considered part of the output rather than auxiliary
      space.
    elapsed_time: 555.1306896209717
    model: gemini-3-flash-preview
    generated_at: '2026-07-09 02:20:12 '
---

## Problem #3532: Path Existence Queries in a Graph I

**Difficulty:** Medium

**Topics:** Array, Hash Table, Binary Search, Union-Find, Graph Theory

## Problem Description

<p>You are given an integer <code>n</code> representing the number of nodes in a graph, labeled from 0 to <code>n - 1</code>.</p>

<p>You are also given an integer array <code>nums</code> of length <code>n</code> sorted in <strong>non-decreasing</strong> order, and an integer <code>maxDiff</code>.</p>

<p>An <strong>undirected </strong>edge exists between nodes <code>i</code> and <code>j</code> if the <strong>absolute</strong> difference between <code>nums[i]</code> and <code>nums[j]</code> is <strong>at most</strong> <code>maxDiff</code> (i.e., <code>|nums[i] - nums[j]| &lt;= maxDiff</code>).</p>

<p>You are also given a 2D integer array <code>queries</code>. For each <code>queries[i] = [u<sub>i</sub>, v<sub>i</sub>]</code>, determine whether there exists a path between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>.</p>

<p>Return a boolean array <code>answer</code>, where <code>answer[i]</code> is <code>true</code> if there exists a path between <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code> in the <code>i<sup>th</sup></code> query and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[true,false]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Query <code>[0,0]</code>: Node 0 has a trivial path to itself.</li>
	<li>Query <code>[0,1]</code>: There is no edge between Node 0 and Node 1 because <code>|nums[0] - nums[1]| = |1 - 3| = 2</code>, which is greater than <code>maxDiff</code>.</li>
	<li>Thus, the final answer after processing all the queries is <code>[true, false]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[false,false,true,true]</span></p>

<p><strong>Explanation:</strong></p>

<p>The resulting graph is:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/03/25/screenshot-2025-03-26-at-122249.png" style="width: 300px; height: 170px;" /></p>

<ul>
	<li>Query <code>[0,1]</code>: There is no edge between Node 0 and Node 1 because <code>|nums[0] - nums[1]| = |2 - 5| = 3</code>, which is greater than <code>maxDiff</code>.</li>
	<li>Query <code>[0,2]</code>: There is no edge between Node 0 and Node 2 because <code>|nums[0] - nums[2]| = |2 - 6| = 4</code>, which is greater than <code>maxDiff</code>.</li>
	<li>Query <code>[1,3]</code>: There is a path between Node 1 and Node 3 through Node 2 since <code>|nums[1] - nums[2]| = |5 - 6| = 1</code> and <code>|nums[2] - nums[3]| = |6 - 8| = 2</code>, both of which are within <code>maxDiff</code>.</li>
	<li>Query <code>[2,3]</code>: There is an edge between Node 2 and Node 3 because <code>|nums[2] - nums[3]| = |6 - 8| = 2</code>, which is equal to <code>maxDiff</code>.</li>
	<li>Thus, the final answer after processing all the queries is <code>[false, false, true, true]</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
	<li><code>0 &lt;= maxDiff &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i] == [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt; n</code></li>
</ul>


## Hints

1. How do the connected components look? Do they appear in segments (i.e., are they continuous)?

2. Preprocess the connected components.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core observation for this problem is that because the input array is sorted in non-decreasing order, the connected components of the graph must consist of contiguous segments of indices. If the difference between any two adjacent elements in the sorted array, nums[i] and nums[i-1], exceeds maxDiff, no edge can exist between any node in the set {0, ..., i-1} and any node in the set {i, ..., n-1}. This is because for any a < i and b >= i, the difference nums[b] - nums[a] will be at least as large as nums[i] - nums[i-1].

To solve the problem efficiently, we can pre-calculate the connected components in a single O(n) pass. We maintain a component identifier that starts at 0 and increments whenever the gap between adjacent elements in the sorted array is greater than maxDiff. After storing these identifiers in an array, we can answer each query [u, v] in O(1) time by checking if nodes u and v belong to the same component (i.e., whether their identifiers are equal).

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
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<int> componentId(n);
        componentId[0] = 0;
        int currentId = 0;
        for (int i = 1; i < n; ++i) {
            if (nums[i] - nums[i - 1] > maxDiff) {
                currentId++;
            }
            componentId[i] = currentId;
        }

        int q = queries.size();
        vector<bool> result(q);
        for (int i = 0; i < q; ++i) {
            result[i] = (componentId[queries[i][0]] == componentId[queries[i][1]]);
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
    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] componentId = new int[n];
        componentId[0] = 0;
        int currentId = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] > maxDiff) {
                currentId++;
            }
            componentId[i] = currentId;
        }

        boolean[] result = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
            result[i] = (componentId[queries[i][0]] == componentId[queries[i][1]]);
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
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        component_id = [0] * n
        curr_id = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr_id += 1
            component_id[i] = curr_id

        result = []
        for u, v in queries:
            result.append(component_id[u] == component_id[v])
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component_id = [0] * n
        curr_id = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr_id += 1
            component_id[i] = curr_id

        return [component_id[u] == component_id[v] for u, v in queries]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* pathExistenceQueries(int n, int* nums, int numsSize, int maxDiff, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int* componentId = (int*)malloc(n * sizeof(int));
    componentId[0] = 0;
    int currentId = 0;
    for (int i = 1; i < n; i++) {
        if (nums[i] - nums[i - 1] > maxDiff) {
            currentId++;
        }
        componentId[i] = currentId;
    }

    bool* result = (bool*)malloc(queriesSize * sizeof(bool));
    for (int i = 0; i < queriesSize; i++) {
        int u = queries[i][0];
        int v = queries[i][1];
        result[i] = (componentId[u] == componentId[v]);
    }

    free(componentId);
    *returnSize = queriesSize;
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool[] PathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] compId = new int[n];
        int curr = 0;
        compId[0] = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] > maxDiff) {
                curr++;
            }
            compId[i] = curr;
        }

        int m = queries.Length;
        bool[] result = new bool[m];
        for (int i = 0; i < m; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            result[i] = compId[u] == compId[v];
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
 * @param {number[]} nums
 * @param {number} maxDiff
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var pathExistenceQueries = function(n, nums, maxDiff, queries) {
    const compId = new Int32Array(n);
    let curr = 0;
    compId[0] = 0;
    for (let i = 1; i < n; i++) {
        if (nums[i] - nums[i - 1] > maxDiff) {
            curr++;
        }
        compId[i] = curr;
    }

    const m = queries.length;
    const result = new Array(m);
    for (let i = 0; i < m; i++) {
        const u = queries[i][0];
        const v = queries[i][1];
        result[i] = compId[u] === compId[v];
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function pathExistenceQueries(n: number, nums: number[], maxDiff: number, queries: number[][]): boolean[] {
    const compId: Int32Array = new Int32Array(n);
    let curr: number = 0;
    compId[0] = 0;
    for (let i = 1; i < n; i++) {
        if (nums[i] - nums[i - 1] > maxDiff) {
            curr++;
        }
        compId[i] = curr;
    }

    const m: number = queries.length;
    const result: boolean[] = new Array(m);
    for (let i = 0; i < m; i++) {
        const u: number = queries[i][0];
        const v: number = queries[i][1];
        result[i] = compId[u] === compId[v];
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
     * @param Integer[] $nums
     * @param Integer $maxDiff
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function pathExistenceQueries($n, $nums, $maxDiff, $queries) {
        $compId = array_fill(0, $n, 0);
        $curr = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] - $nums[$i - 1] > $maxDiff) {
                $curr++;
            }
            $compId[$i] = $curr;
        }

        $result = [];
        foreach ($queries as $q) {
            $u = $q[0];
            $v = $q[1];
            $result[] = $compId[$u] === $compId[$v];
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
    func pathExistenceQueries(_ n: Int, _ nums: [Int], _ maxDiff: Int, _ queries: [[Int]]) -> [Bool] {
        var compId = Array(repeating: 0, count: n)
        var curr = 0
        for i in 1..<n {
            if nums[i] - nums[i - 1] > maxDiff {
                curr += 1
            }
            compId[i] = curr
        }

        return queries.map { q in
            compId[q[0]] == compId[q[1]]
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
    fun pathExistenceQueries(n: Int, nums: IntArray, maxDiff: Int, queries: Array<IntArray>): BooleanArray {
        val comp = IntArray(n)
        comp[0] = 0
        for (i in 1 until n) {
            if (nums[i] - nums[i - 1] <= maxDiff) {
                comp[i] = comp[i - 1]
            } else {
                comp[i] = comp[i - 1] + 1
            }
        }

        val answer = BooleanArray(queries.size)
        for (i in queries.indices) {
            val u = queries[i][0]
            val v = queries[i][1]
            answer[i] = comp[u] == comp[v]
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<bool> pathExistenceQueries(int n, List<int> nums, int maxDiff, List<List<int>> queries) {
    List<int> comp = List<int>.filled(n, 0);
    for (int i = 1; i < n; i++) {
      if (nums[i] - nums[i - 1] <= maxDiff) {
        comp[i] = comp[i - 1];
      } else {
        comp[i] = comp[i - 1] + 1;
      }
    }

    List<bool> result = List<bool>.filled(queries.length, false);
    for (int i = 0; i < queries.length; i++) {
      int u = queries[i][0];
      int v = queries[i][1];
      result[i] = comp[u] == comp[v];
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
func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []bool {
    comp := make([]int, n)
    comp[0] = 0
    for i := 1; i < n; i++ {
        if nums[i]-nums[i-1] <= maxDiff {
            comp[i] = comp[i-1]
        } else {
            comp[i] = comp[i-1] + 1
        }
    }

    answer := make([]bool, len(queries))
    for i, q := range queries {
        u, v := q[0], q[1]
        answer[i] = comp[u] == comp[v]
    }
    return answer
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[]} nums
# @param {Integer} max_diff
# @param {Integer[][]} queries
# @return {Boolean[]}
def path_existence_queries(n, nums, max_diff, queries)
  comp = Array.new(n, 0)
  (1...n).each do |i|
    if nums[i] - nums[i - 1] <= max_diff
      comp[i] = comp[i - 1]
    else
      comp[i] = comp[i - 1] + 1
    end
  end

  queries.map do |u, v|
    comp[u] == comp[v]
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def pathExistenceQueries(n: Int, nums: Array[Int], maxDiff: Int, queries: Array[Array[Int]]): Array[Boolean] = {
        val comp = new Array[Int](n)
        comp(0) = 0
        var i = 1
        while (i < n) {
            if (nums(i) - nums(i - 1) <= maxDiff) {
                comp(i) = comp(i - 1)
            } else {
                comp(i) = comp(i - 1) + 1
            }
            i += 1
        }

        val result = new Array[Boolean](queries.length)
        var j = 0
        while (j < queries.length) {
            val u = queries(j)(0)
            val v = queries(j)(1)
            result(j) = comp(u) == comp(v)
            j += 1
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
    pub fn path_existence_queries(n: i32, nums: Vec<i32>, max_diff: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = n as usize;
        let mut component_ids = vec![0; n];
        let mut curr_id = 0;

        if n > 1 {
            for i in 1..n {
                if nums[i] - nums[i - 1] > max_diff {
                    curr_id += 1;
                }
                component_ids[i] = curr_id;
            }
        }

        queries
            .into_iter()
            .map(|q| {
                let u = q[0] as usize;
                let v = q[1] as usize;
                component_ids[u] == component_ids[v]
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
(define/contract (path-existence-queries n nums maxDiff queries)
  (-> exact-integer? (listof exact-integer?) exact-integer? (listof (listof exact-integer?)) (listof boolean?))
  (let* ([nums-vec (list->vector nums)]
         [comp-ids (make-vector n 0)]
         [curr-id 0])
    (for ([i (in-range 1 n)])
      (when (> (- (vector-ref nums-vec i) (vector-ref nums-vec (- i 1))) maxDiff)
        (set! curr-id (+ curr-id 1)))
      (vector-set! comp-ids i curr-id))
    (map (lambda (q)
           (let ([u (car q)]
                 [v (cadr q)])
             (= (vector-ref comp-ids u) (vector-ref comp-ids v))))
         queries)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec path_existence_queries(N :: integer(), Nums :: [integer()], MaxDiff :: integer(), Queries :: [[integer()]]) -> [boolean()].
path_existence_queries(N, Nums, MaxDiff, Queries) ->
    CompIds = compute_comp_ids(Nums, MaxDiff),
    CompVec = list_to_tuple(CompIds),
    [element(U + 1, CompVec) =:= element(V + 1, CompVec) || [U, V] <- Queries].

compute_comp_ids([H | T], MaxDiff) ->
    compute_comp_ids(T, H, 0, [0], MaxDiff).

compute_comp_ids([], _Prev, _CurrId, Acc, _MaxDiff) ->
    lists:reverse(Acc);
compute_comp_ids([H | T], Prev, CurrId, Acc, MaxDiff) ->
    NextId = if (H - Prev) > MaxDiff -> CurrId + 1; true -> CurrId end,
    compute_comp_ids(T, H, NextId, [NextId | Acc], MaxDiff).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec path_existence_queries(n :: integer, nums :: [integer], max_diff :: integer, queries :: [[integer]]) :: [boolean]
  def path_existence_queries(n, nums, max_diff, queries) do
    [first | rest] = nums
    {_, comp_ids_rev} = Enum.reduce(rest, {first, [0]}, fn curr, {prev, [curr_id | _] = acc} ->
      new_id = if curr - prev > max_diff, do: curr_id + 1, else: curr_id
      {curr, [new_id | acc]}
    end)

    comp_vec = Enum.reverse(comp_ids_rev) |> List.to_tuple()

    Enum.map(queries, fn [u, v] ->
      elem(comp_vec, u) == elem(comp_vec, v)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n + q) where n is the number of nodes and q is the number of queries. We iterate through the sorted array once to compute connected components in O(n) and then iterate through the queries to answer each in O(1), leading to a total time complexity of O(n + q).
- **Space Complexity:** O(n) where n is the number of nodes. We need an auxiliary array of size n to store the component identifier for each node. The space for the result array is O(q), which is often considered part of the output rather than auxiliary space.
