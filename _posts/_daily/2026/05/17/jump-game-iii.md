---
layout: post
title: "Jump Game III"
date: 2026-05-17 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Depth-First Search", "Breadth-First Search"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/jump-game-iii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool canReach(vector<int>& arr, int start)\
        \ {\n        int n = arr.size();\n        vector<bool> visited(n, false);\n\
        \        queue<int> q;\n        q.push(start);\n        visited[start] = true;\n\
        \n        while (!q.empty()) {\n            int curr = q.front();\n        \
        \    q.pop();\n\n            if (arr[curr] == 0) return true;\n\n          \
        \  int jumps[2] = {curr + arr[curr], curr - arr[curr]};\n            for (int\
        \ next : jumps) {\n                if (next >= 0 && next < n && !visited[next])\
        \ {\n                    visited[next] = true;\n                    q.push(next);\n\
        \                }\n            }\n        }\n\n        return false;\n    }\n\
        };"
      java: "class Solution {\n    public boolean canReach(int[] arr, int start) {\n\
        \        int n = arr.length;\n        boolean[] visited = new boolean[n];\n\
        \        Queue<Integer> queue = new LinkedList<>();\n        queue.add(start);\n\
        \        visited[start] = true;\n\n        while (!queue.isEmpty()) {\n    \
        \        int curr = queue.poll();\n\n            if (arr[curr] == 0) return\
        \ true;\n\n            int[] nextIndices = {curr + arr[curr], curr - arr[curr]};\n\
        \            for (int next : nextIndices) {\n                if (next >= 0 &&\
        \ next < n && !visited[next]) {\n                    visited[next] = true;\n\
        \                    queue.add(next);\n                }\n            }\n  \
        \      }\n\n        return false;\n    }\n}"
      python: "class Solution(object):\n    def canReach(self, arr, start):\n      \
        \  \"\"\"\n        :type arr: List[int]\n        :type start: int\n        :rtype:\
        \ bool\n        \"\"\"\n        n = len(arr)\n        visited = [False] * n\n\
        \        queue = [start]\n        visited[start] = True\n        idx = 0\n\n\
        \        while idx < len(queue):\n            curr = queue[idx]\n          \
        \  idx += 1\n\n            if arr[curr] == 0:\n                return True\n\
        \n            for next_idx in [curr + arr[curr], curr - arr[curr]]:\n      \
        \          if 0 <= next_idx < n and not visited[next_idx]:\n               \
        \     visited[next_idx] = True\n                    queue.append(next_idx)\n\
        \n        return False"
      python3: "class Solution:\n    def canReach(self, arr: List[int], start: int)\
        \ -> bool:\n        from collections import deque\n\n        n = len(arr)\n\
        \        visited = [False] * n\n        q = deque([start])\n        visited[start]\
        \ = True\n\n        while q:\n            curr = q.popleft()\n\n           \
        \ if arr[curr] == 0:\n                return True\n\n            for next_idx\
        \ in (curr + arr[curr], curr - arr[curr]):\n                if 0 <= next_idx\
        \ < n and not visited[next_idx]:\n                    visited[next_idx] = True\n\
        \                    q.append(next_idx)\n\n        return False"
      c: "bool dfs(int* arr, int n, int cur, bool* visited) {\n    if (cur < 0 || cur\
        \ >= n || visited[cur]) {\n        return false;\n    }\n    if (arr[cur] ==\
        \ 0) {\n        return true;\n    }\n\n    visited[cur] = true;\n    return\
        \ dfs(arr, n, cur + arr[cur], visited) || dfs(arr, n, cur - arr[cur], visited);\n\
        }\n\nbool canReach(int* arr, int arrSize, int start) {\n    bool* visited =\
        \ (bool*)calloc(arrSize, sizeof(bool));\n    bool result = dfs(arr, arrSize,\
        \ start, visited);\n    free(visited);\n    return result;\n}"
      csharp: "public class Solution {\n    public bool CanReach(int[] arr, int start)\
        \ {\n        int n = arr.Length;\n        bool[] visited = new bool[n];\n  \
        \      System.Collections.Generic.Queue<int> queue = new System.Collections.Generic.Queue<int>();\n\
        \        queue.Enqueue(start);\n        visited[start] = true;\n        while\
        \ (queue.Count > 0) {\n            int curr = queue.Dequeue();\n           \
        \ if (arr[curr] == 0) return true;\n            int next1 = curr + arr[curr];\n\
        \            if (next1 >= 0 && next1 < n && !visited[next1]) {\n           \
        \     visited[next1] = true;\n                queue.Enqueue(next1);\n      \
        \      }\n            int next2 = curr - arr[curr];\n            if (next2 >=\
        \ 0 && next2 < n && !visited[next2]) {\n                visited[next2] = true;\n\
        \                queue.Enqueue(next2);\n            }\n        }\n        return\
        \ false;\n    }\n}"
      javascript: "/**\n * @param {number[]} arr\n * @param {number} start\n * @return\
        \ {boolean}\n */\nvar canReach = function(arr, start) {\n    const n = arr.length;\n\
        \    const visited = new Array(n).fill(false);\n    const queue = [start];\n\
        \    let head = 0;\n    visited[start] = true;\n    while (head < queue.length)\
        \ {\n        const curr = queue[head++];\n        if (arr[curr] === 0) return\
        \ true;\n        const next1 = curr + arr[curr];\n        if (next1 >= 0 &&\
        \ next1 < n && !visited[next1]) {\n            visited[next1] = true;\n    \
        \        queue.push(next1);\n        }\n        const next2 = curr - arr[curr];\n\
        \        if (next2 >= 0 && next2 < n && !visited[next2]) {\n            visited[next2]\
        \ = true;\n            queue.push(next2);\n        }\n    }\n    return false;\n\
        };"
      typescript: "function canReach(arr: number[], start: number): boolean {\n    const\
        \ n: number = arr.length;\n    const visited: boolean[] = new Array(n).fill(false);\n\
        \    const queue: number[] = [start];\n    let head: number = 0;\n    visited[start]\
        \ = true;\n    while (head < queue.length) {\n        const curr: number = queue[head++];\n\
        \        if (arr[curr] === 0) return true;\n        const next1: number = curr\
        \ + arr[curr];\n        if (next1 >= 0 && next1 < n && !visited[next1]) {\n\
        \            visited[next1] = true;\n            queue.push(next1);\n      \
        \  }\n        const next2: number = curr - arr[curr];\n        if (next2 >=\
        \ 0 && next2 < n && !visited[next2]) {\n            visited[next2] = true;\n\
        \            queue.push(next2);\n        }\n    }\n    return false;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $arr\n     * @param\
        \ Integer $start\n     * @return Boolean\n     */\n    function canReach($arr,\
        \ $start) {\n        $n = count($arr);\n        $visited = array_fill(0, $n,\
        \ false);\n        $queue = [$start];\n        $visited[$start] = true;\n  \
        \      $head = 0;\n        while ($head < count($queue)) {\n            $curr\
        \ = $queue[$head++];\n            if ($arr[$curr] == 0) return true;\n     \
        \       $next1 = $curr + $arr[$curr];\n            if ($next1 >= 0 && $next1\
        \ < $n && !$visited[$next1]) {\n                $visited[$next1] = true;\n \
        \               $queue[] = $next1;\n            }\n            $next2 = $curr\
        \ - $arr[$curr];\n            if ($next2 >= 0 && $next2 < $n && !$visited[$next2])\
        \ {\n                $visited[$next2] = true;\n                $queue[] = $next2;\n\
        \            }\n        }\n        return false;\n    }\n}"
      swift: "class Solution {\n    func canReach(_ arr: [Int], _ start: Int) -> Bool\
        \ {\n        let n = arr.count\n        var visited = Array(repeating: false,\
        \ count: n)\n        var queue = [start]\n        var head = 0\n        visited[start]\
        \ = true\n        while head < queue.count {\n            let curr = queue[head]\n\
        \            head += 1\n            if arr[curr] == 0 {\n                return\
        \ true\n            }\n            let next1 = curr + arr[curr]\n          \
        \  if next1 >= 0 && next1 < n && !visited[next1] {\n                visited[next1]\
        \ = true\n                queue.append(next1)\n            }\n            let\
        \ next2 = curr - arr[curr]\n            if next2 >= 0 && next2 < n && !visited[next2]\
        \ {\n                visited[next2] = true\n                queue.append(next2)\n\
        \            }\n        }\n        return false\n    }\n}"
      kotlin: "class Solution {\n    fun canReach(arr: IntArray, start: Int): Boolean\
        \ {\n        val n = arr.size\n        val visited = BooleanArray(n)\n     \
        \   val queue = java.util.ArrayDeque<Int>()\n        queue.add(start)\n    \
        \    visited[start] = true\n        while (queue.isNotEmpty()) {\n         \
        \   val curr = queue.poll()\n            if (arr[curr] == 0) return true\n \
        \           val next1 = curr + arr[curr]\n            val next2 = curr - arr[curr]\n\
        \            if (next1 in 0 until n && !visited[next1]) {\n                visited[next1]\
        \ = true\n                queue.add(next1)\n            }\n            if (next2\
        \ in 0 until n && !visited[next2]) {\n                visited[next2] = true\n\
        \                queue.add(next2)\n            }\n        }\n        return\
        \ false\n    }\n}"
      dart: "class Solution {\n  bool canReach(List<int> arr, int start) {\n    int\
        \ n = arr.length;\n    List<bool> visited = List.filled(n, false);\n    List<int>\
        \ queue = [start];\n    visited[start] = true;\n    int head = 0;\n    while\
        \ (head < queue.length) {\n      int curr = queue[head++];\n      if (arr[curr]\
        \ == 0) return true;\n      int next1 = curr + arr[curr];\n      int next2 =\
        \ curr - arr[curr];\n      if (next1 >= 0 && next1 < n && !visited[next1]) {\n\
        \        visited[next1] = true;\n        queue.add(next1);\n      }\n      if\
        \ (next2 >= 0 && next2 < n && !visited[next2]) {\n        visited[next2] = true;\n\
        \        queue.add(next2);\n      }\n    }\n    return false;\n  }\n}"
      go: "func canReach(arr []int, start int) bool {\n    n := len(arr)\n    visited\
        \ := make([]bool, n)\n    queue := []int{start}\n    visited[start] = true\n\
        \    for len(queue) > 0 {\n        curr := queue[0]\n        queue = queue[1:]\n\
        \        if arr[curr] == 0 {\n            return true\n        }\n        next1\
        \ := curr + arr[curr]\n        next2 := curr - arr[curr]\n        if next1 >=\
        \ 0 && next1 < n && !visited[next1] {\n            visited[next1] = true\n \
        \           queue = append(queue, next1)\n        }\n        if next2 >= 0 &&\
        \ next2 < n && !visited[next2] {\n            visited[next2] = true\n      \
        \      queue = append(queue, next2)\n        }\n    }\n    return false\n}"
      ruby: "# @param {Integer[]} arr\n# @param {Integer} start\n# @return {Boolean}\n\
        def can_reach(arr, start)\n    n = arr.length\n    visited = Array.new(n, false)\n\
        \    queue = [start]\n    visited[start] = true\n    while !queue.empty?\n \
        \       curr = queue.shift\n        return true if arr[curr] == 0\n        [curr\
        \ + arr[curr], curr - arr[curr]].each do |nxt|\n            if nxt >= 0 && nxt\
        \ < n && !visited[nxt]\n                visited[nxt] = true\n              \
        \  queue.push(nxt)\n            end\n        end\n    end\n    false\nend"
      scala: "object Solution {\n    def canReach(arr: Array[Int], start: Int): Boolean\
        \ = {\n        val n = arr.length\n        val visited = new Array[Boolean](n)\n\
        \        val queue = new scala.collection.mutable.Queue[Int]()\n        queue.enqueue(start)\n\
        \        visited(start) = true\n        while (queue.nonEmpty) {\n         \
        \   val curr = queue.dequeue()\n            if (arr(curr) == 0) return true\n\
        \            val next1 = curr + arr(curr)\n            val next2 = curr - arr[curr]\n\
        \            if (next1 >= 0 && next1 < n && !visited(next1)) {\n           \
        \     visited(next1) = true\n                queue.enqueue(next1)\n        \
        \    }\n            if (next2 >= 0 && next2 < n && !visited(next2)) {\n    \
        \            visited(next2) = true\n                queue.enqueue(next2)\n \
        \           }\n        }\n        false\n    }\n}"
      rust: "use std::collections::VecDeque;\n\nimpl Solution {\n    pub fn can_reach(arr:\
        \ Vec<i32>, start: i32) -> bool {\n        let n = arr.len();\n        let mut\
        \ visited = vec![false; n];\n        let mut queue = VecDeque::new();\n\n  \
        \      let start_idx = start as usize;\n        queue.push_back(start_idx);\n\
        \        visited[start_idx] = true;\n\n        while let Some(curr) = queue.pop_front()\
        \ {\n            let val = arr[curr];\n            if val == 0 {\n         \
        \       return true;\n            }\n\n            let val_u = val as usize;\n\
        \n            if curr + val_u < n && !visited[curr + val_u] {\n            \
        \    visited[curr + val_u] = true;\n                queue.push_back(curr + val_u);\n\
        \            }\n\n            if curr >= val_u && !visited[curr - val_u] {\n\
        \                visited[curr - val_u] = true;\n                queue.push_back(curr\
        \ - val_u);\n            }\n        }\n\n        false\n    }\n}"
      racket: "(define/contract (can-reach arr start)\n  (-> (listof exact-integer?)\
        \ exact-integer? boolean?)\n  (let* ([vec (list->vector arr)]\n         [n (vector-length\
        \ vec)]\n         [visited (make-vector n #f)])\n    (let dfs ([i start])\n\
        \      (cond\n        [(or (< i 0) (>= i n) (vector-ref visited i)) #f]\n  \
        \      [(= (vector-ref vec i) 0) #t]\n        [else\n         (begin\n     \
        \      (vector-set! visited i #t)\n           (let ([v (vector-ref vec i)])\n\
        \             (or (dfs (+ i v))\n                 (dfs (- i v)))))]))))"
      erlang: "-spec can_reach(Arr :: [integer()], Start :: integer()) -> boolean().\n\
        can_reach(Arr, Start) ->\n    ArrVec = list_to_tuple(Arr),\n    N = tuple_size(ArrVec),\n\
        \    Queue = queue:in(Start + 1, queue:new()),\n    Visited = sets:add_element(Start\
        \ + 1, sets:new()),\n    can_reach_bfs(ArrVec, N, Queue, Visited).\n\ncan_reach_bfs(ArrVec,\
        \ N, Queue, Visited) ->\n    case queue:out(Queue) of\n        {empty, _} ->\
        \ false;\n        {{value, Curr}, RestQueue} ->\n            Val = element(Curr,\
        \ ArrVec),\n            if\n                Val =:= 0 -> true;\n           \
        \     true ->\n                    NextIdxs = [I || I <- [Curr + Val, Curr -\
        \ Val],\n                                     I >= 1, I =< N,\n            \
        \                         not sets:is_element(I, Visited)],\n              \
        \      {NewQueue, NewVisited} = lists:foldl(\n                        fun(Idx,\
        \ {Q, V}) ->\n                            {queue:in(Idx, Q), sets:add_element(Idx,\
        \ V)}\n                        end, {RestQueue, Visited}, NextIdxs),\n     \
        \               can_reach_bfs(ArrVec, N, NewQueue, NewVisited)\n           \
        \ end\n    end."
      elixir: "defmodule Solution do\n  @spec can_reach(arr :: [integer], start :: integer)\
        \ :: boolean\n  def can_reach(arr, start) do\n    vec = List.to_tuple(arr)\n\
        \    n = tuple_size(vec)\n    q = :queue.in(start, :queue.new())\n    visited\
        \ = MapSet.new([start])\n    bfs(vec, n, q, visited)\n  end\n\n  defp bfs(vec,\
        \ n, q, visited) do\n    case :queue.out(q) do\n      {:empty, _} -> false\n\
        \      {{:value, curr}, rest_q} ->\n        val = elem(vec, curr)\n        if\
        \ val == 0 do\n          true\n        else\n          {new_q, new_v} = \n \
        \           [curr + val, curr - val]\n            |> Enum.filter(fn i -> i >=\
        \ 0 and i < n and not MapSet.member?(visited, i) end)\n            |> Enum.reduce({rest_q,\
        \ visited}, fn i, {acc_q, acc_v} ->\n              {:queue.in(i, acc_q), MapSet.put(acc_v,\
        \ i)}\n            end)\n          bfs(vec, n, new_q, new_v)\n        end\n\
        \    end\n  end\nend"
    approach: 'The problem can be framed as a graph traversal task where each index
      in the array represents a node and the possible jumps from index $i$ to $i + arr[i]$
      or $i - arr[i]$ represent directed edges. Using a Breadth-First Search (BFS) or
      Depth-First Search (DFS), we can explore all reachable nodes starting from the
      given index. The search continues until we either encounter an index whose value
      is zero, signifying a successful path, or we exhaust all reachable nodes without
      finding a zero.


      To ensure the algorithm terminates and avoids redundant computations in the presence
      of cycles, we maintain a visited state for each index. This can be achieved using
      a boolean array or a set to keep track of indices that have already been processed.
      Before attempting a jump, we verify that the destination index remains within
      the array boundaries and has not been visited yet. If a zero-value element is
      found at any point during the exploration, the search returns true; otherwise,
      if the traversal concludes without finding such an index, it returns false.'
    time_complexity: O(N), where N is the number of elements in the array. Each index
      is visited and added to the queue or stack at most once, and each visit involves
      constant-time bounds checking and arithmetic operations.
    space_complexity: O(N), as we require a boolean array or set to track visited indices,
      and the BFS queue or DFS recursion stack can store up to N elements in the worst
      case.
    elapsed_time: 135.5757348537445
    model: gemini-3-flash-preview
    generated_at: '2026-05-17 02:29:56 '
---

## Problem #1306: Jump Game III

**Difficulty:** Medium

**Topics:** Array, Depth-First Search, Breadth-First Search

## Problem Description

<p>Given an array of non-negative integers <code>arr</code>, you are initially positioned at <code>start</code>&nbsp;index of the array. When you are at index <code>i</code>, you can jump&nbsp;to <code>i + arr[i]</code> or <code>i - arr[i]</code>, check if you can reach&nbsp;<strong>any</strong> index with value 0.</p>

<p>Notice that you can not jump outside of the array at any time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,2,3,0,3,1,2], start = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> 
All possible ways to reach at index 3 with value 0 are: 
index 5 -&gt; index 4 -&gt; index 1 -&gt; index 3 
index 5 -&gt; index 6 -&gt; index 4 -&gt; index 1 -&gt; index 3 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,2,3,0,3,1,2], start = 0
<strong>Output:</strong> true 
<strong>Explanation: 
</strong>One possible way to reach at index 3 with value 0 is: 
index 0 -&gt; index 4 -&gt; index 1 -&gt; index 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,0,2,1,2], start = 2
<strong>Output:</strong> false
<strong>Explanation: </strong>There is no way to reach at index 1 with value 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;&nbsp;arr.length</code></li>
	<li><code>0 &lt;= start &lt; arr.length</code></li>
</ul>


## Hints

1. Think of BFS to solve the problem.

2. When you reach a position with a value = 0 then return true.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be framed as a graph traversal task where each index in the array represents a node and the possible jumps from index $i$ to $i + arr[i]$ or $i - arr[i]$ represent directed edges. Using a Breadth-First Search (BFS) or Depth-First Search (DFS), we can explore all reachable nodes starting from the given index. The search continues until we either encounter an index whose value is zero, signifying a successful path, or we exhaust all reachable nodes without finding a zero.

To ensure the algorithm terminates and avoids redundant computations in the presence of cycles, we maintain a visited state for each index. This can be achieved using a boolean array or a set to keep track of indices that have already been processed. Before attempting a jump, we verify that the destination index remains within the array boundaries and has not been visited yet. If a zero-value element is found at any point during the exploration, the search returns true; otherwise, if the traversal concludes without finding such an index, it returns false.

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
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        vector<bool> visited(n, false);
        queue<int> q;
        q.push(start);
        visited[start] = true;

        while (!q.empty()) {
            int curr = q.front();
            q.pop();

            if (arr[curr] == 0) return true;

            int jumps[2] = {curr + arr[curr], curr - arr[curr]};
            for (int next : jumps) {
                if (next >= 0 && next < n && !visited[next]) {
                    visited[next] = true;
                    q.push(next);
                }
            }
        }

        return false;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean canReach(int[] arr, int start) {
        int n = arr.length;
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int curr = queue.poll();

            if (arr[curr] == 0) return true;

            int[] nextIndices = {curr + arr[curr], curr - arr[curr]};
            for (int next : nextIndices) {
                if (next >= 0 && next < n && !visited[next]) {
                    visited[next] = true;
                    queue.add(next);
                }
            }
        }

        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        visited = [False] * n
        queue = [start]
        visited[start] = True
        idx = 0

        while idx < len(queue):
            curr = queue[idx]
            idx += 1

            if arr[curr] == 0:
                return True

            for next_idx in [curr + arr[curr], curr - arr[curr]]:
                if 0 <= next_idx < n and not visited[next_idx]:
                    visited[next_idx] = True
                    queue.append(next_idx)

        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import deque

        n = len(arr)
        visited = [False] * n
        q = deque([start])
        visited[start] = True

        while q:
            curr = q.popleft()

            if arr[curr] == 0:
                return True

            for next_idx in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_idx < n and not visited[next_idx]:
                    visited[next_idx] = True
                    q.append(next_idx)

        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool dfs(int* arr, int n, int cur, bool* visited) {
    if (cur < 0 || cur >= n || visited[cur]) {
        return false;
    }
    if (arr[cur] == 0) {
        return true;
    }

    visited[cur] = true;
    return dfs(arr, n, cur + arr[cur], visited) || dfs(arr, n, cur - arr[cur], visited);
}

bool canReach(int* arr, int arrSize, int start) {
    bool* visited = (bool*)calloc(arrSize, sizeof(bool));
    bool result = dfs(arr, arrSize, start, visited);
    free(visited);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CanReach(int[] arr, int start) {
        int n = arr.Length;
        bool[] visited = new bool[n];
        System.Collections.Generic.Queue<int> queue = new System.Collections.Generic.Queue<int>();
        queue.Enqueue(start);
        visited[start] = true;
        while (queue.Count > 0) {
            int curr = queue.Dequeue();
            if (arr[curr] == 0) return true;
            int next1 = curr + arr[curr];
            if (next1 >= 0 && next1 < n && !visited[next1]) {
                visited[next1] = true;
                queue.Enqueue(next1);
            }
            int next2 = curr - arr[curr];
            if (next2 >= 0 && next2 < n && !visited[next2]) {
                visited[next2] = true;
                queue.Enqueue(next2);
            }
        }
        return false;
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
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    const n = arr.length;
    const visited = new Array(n).fill(false);
    const queue = [start];
    let head = 0;
    visited[start] = true;
    while (head < queue.length) {
        const curr = queue[head++];
        if (arr[curr] === 0) return true;
        const next1 = curr + arr[curr];
        if (next1 >= 0 && next1 < n && !visited[next1]) {
            visited[next1] = true;
            queue.push(next1);
        }
        const next2 = curr - arr[curr];
        if (next2 >= 0 && next2 < n && !visited[next2]) {
            visited[next2] = true;
            queue.push(next2);
        }
    }
    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function canReach(arr: number[], start: number): boolean {
    const n: number = arr.length;
    const visited: boolean[] = new Array(n).fill(false);
    const queue: number[] = [start];
    let head: number = 0;
    visited[start] = true;
    while (head < queue.length) {
        const curr: number = queue[head++];
        if (arr[curr] === 0) return true;
        const next1: number = curr + arr[curr];
        if (next1 >= 0 && next1 < n && !visited[next1]) {
            visited[next1] = true;
            queue.push(next1);
        }
        const next2: number = curr - arr[curr];
        if (next2 >= 0 && next2 < n && !visited[next2]) {
            visited[next2] = true;
            queue.push(next2);
        }
    }
    return false;
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
     * @param Integer $start
     * @return Boolean
     */
    function canReach($arr, $start) {
        $n = count($arr);
        $visited = array_fill(0, $n, false);
        $queue = [$start];
        $visited[$start] = true;
        $head = 0;
        while ($head < count($queue)) {
            $curr = $queue[$head++];
            if ($arr[$curr] == 0) return true;
            $next1 = $curr + $arr[$curr];
            if ($next1 >= 0 && $next1 < $n && !$visited[$next1]) {
                $visited[$next1] = true;
                $queue[] = $next1;
            }
            $next2 = $curr - $arr[$curr];
            if ($next2 >= 0 && $next2 < $n && !$visited[$next2]) {
                $visited[$next2] = true;
                $queue[] = $next2;
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func canReach(_ arr: [Int], _ start: Int) -> Bool {
        let n = arr.count
        var visited = Array(repeating: false, count: n)
        var queue = [start]
        var head = 0
        visited[start] = true
        while head < queue.count {
            let curr = queue[head]
            head += 1
            if arr[curr] == 0 {
                return true
            }
            let next1 = curr + arr[curr]
            if next1 >= 0 && next1 < n && !visited[next1] {
                visited[next1] = true
                queue.append(next1)
            }
            let next2 = curr - arr[curr]
            if next2 >= 0 && next2 < n && !visited[next2] {
                visited[next2] = true
                queue.append(next2)
            }
        }
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun canReach(arr: IntArray, start: Int): Boolean {
        val n = arr.size
        val visited = BooleanArray(n)
        val queue = java.util.ArrayDeque<Int>()
        queue.add(start)
        visited[start] = true
        while (queue.isNotEmpty()) {
            val curr = queue.poll()
            if (arr[curr] == 0) return true
            val next1 = curr + arr[curr]
            val next2 = curr - arr[curr]
            if (next1 in 0 until n && !visited[next1]) {
                visited[next1] = true
                queue.add(next1)
            }
            if (next2 in 0 until n && !visited[next2]) {
                visited[next2] = true
                queue.add(next2)
            }
        }
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool canReach(List<int> arr, int start) {
    int n = arr.length;
    List<bool> visited = List.filled(n, false);
    List<int> queue = [start];
    visited[start] = true;
    int head = 0;
    while (head < queue.length) {
      int curr = queue[head++];
      if (arr[curr] == 0) return true;
      int next1 = curr + arr[curr];
      int next2 = curr - arr[curr];
      if (next1 >= 0 && next1 < n && !visited[next1]) {
        visited[next1] = true;
        queue.add(next1);
      }
      if (next2 >= 0 && next2 < n && !visited[next2]) {
        visited[next2] = true;
        queue.add(next2);
      }
    }
    return false;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func canReach(arr []int, start int) bool {
    n := len(arr)
    visited := make([]bool, n)
    queue := []int{start}
    visited[start] = true
    for len(queue) > 0 {
        curr := queue[0]
        queue = queue[1:]
        if arr[curr] == 0 {
            return true
        }
        next1 := curr + arr[curr]
        next2 := curr - arr[curr]
        if next1 >= 0 && next1 < n && !visited[next1] {
            visited[next1] = true
            queue = append(queue, next1)
        }
        if next2 >= 0 && next2 < n && !visited[next2] {
            visited[next2] = true
            queue = append(queue, next2)
        }
    }
    return false
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} arr
# @param {Integer} start
# @return {Boolean}
def can_reach(arr, start)
    n = arr.length
    visited = Array.new(n, false)
    queue = [start]
    visited[start] = true
    while !queue.empty?
        curr = queue.shift
        return true if arr[curr] == 0
        [curr + arr[curr], curr - arr[curr]].each do |nxt|
            if nxt >= 0 && nxt < n && !visited[nxt]
                visited[nxt] = true
                queue.push(nxt)
            end
        end
    end
    false
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def canReach(arr: Array[Int], start: Int): Boolean = {
        val n = arr.length
        val visited = new Array[Boolean](n)
        val queue = new scala.collection.mutable.Queue[Int]()
        queue.enqueue(start)
        visited(start) = true
        while (queue.nonEmpty) {
            val curr = queue.dequeue()
            if (arr(curr) == 0) return true
            val next1 = curr + arr(curr)
            val next2 = curr - arr[curr]
            if (next1 >= 0 && next1 < n && !visited(next1)) {
                visited(next1) = true
                queue.enqueue(next1)
            }
            if (next2 >= 0 && next2 < n && !visited(next2)) {
                visited(next2) = true
                queue.enqueue(next2)
            }
        }
        false
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
    pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
        let n = arr.len();
        let mut visited = vec![false; n];
        let mut queue = VecDeque::new();

        let start_idx = start as usize;
        queue.push_back(start_idx);
        visited[start_idx] = true;

        while let Some(curr) = queue.pop_front() {
            let val = arr[curr];
            if val == 0 {
                return true;
            }

            let val_u = val as usize;

            if curr + val_u < n && !visited[curr + val_u] {
                visited[curr + val_u] = true;
                queue.push_back(curr + val_u);
            }

            if curr >= val_u && !visited[curr - val_u] {
                visited[curr - val_u] = true;
                queue.push_back(curr - val_u);
            }
        }

        false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (can-reach arr start)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let* ([vec (list->vector arr)]
         [n (vector-length vec)]
         [visited (make-vector n #f)])
    (let dfs ([i start])
      (cond
        [(or (< i 0) (>= i n) (vector-ref visited i)) #f]
        [(= (vector-ref vec i) 0) #t]
        [else
         (begin
           (vector-set! visited i #t)
           (let ([v (vector-ref vec i)])
             (or (dfs (+ i v))
                 (dfs (- i v)))))]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec can_reach(Arr :: [integer()], Start :: integer()) -> boolean().
can_reach(Arr, Start) ->
    ArrVec = list_to_tuple(Arr),
    N = tuple_size(ArrVec),
    Queue = queue:in(Start + 1, queue:new()),
    Visited = sets:add_element(Start + 1, sets:new()),
    can_reach_bfs(ArrVec, N, Queue, Visited).

can_reach_bfs(ArrVec, N, Queue, Visited) ->
    case queue:out(Queue) of
        {empty, _} -> false;
        {{value, Curr}, RestQueue} ->
            Val = element(Curr, ArrVec),
            if
                Val =:= 0 -> true;
                true ->
                    NextIdxs = [I || I <- [Curr + Val, Curr - Val],
                                     I >= 1, I =< N,
                                     not sets:is_element(I, Visited)],
                    {NewQueue, NewVisited} = lists:foldl(
                        fun(Idx, {Q, V}) ->
                            {queue:in(Idx, Q), sets:add_element(Idx, V)}
                        end, {RestQueue, Visited}, NextIdxs),
                    can_reach_bfs(ArrVec, N, NewQueue, NewVisited)
            end
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec can_reach(arr :: [integer], start :: integer) :: boolean
  def can_reach(arr, start) do
    vec = List.to_tuple(arr)
    n = tuple_size(vec)
    q = :queue.in(start, :queue.new())
    visited = MapSet.new([start])
    bfs(vec, n, q, visited)
  end

  defp bfs(vec, n, q, visited) do
    case :queue.out(q) do
      {:empty, _} -> false
      {{:value, curr}, rest_q} ->
        val = elem(vec, curr)
        if val == 0 do
          true
        else
          {new_q, new_v} = 
            [curr + val, curr - val]
            |> Enum.filter(fn i -> i >= 0 and i < n and not MapSet.member?(visited, i) end)
            |> Enum.reduce({rest_q, visited}, fn i, {acc_q, acc_v} ->
              {:queue.in(i, acc_q), MapSet.put(acc_v, i)}
            end)
          bfs(vec, n, new_q, new_v)
        end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the number of elements in the array. Each index is visited and added to the queue or stack at most once, and each visit involves constant-time bounds checking and arithmetic operations.
- **Space Complexity:** O(N), as we require a boolean array or set to track visited indices, and the BFS queue or DFS recursion stack can store up to N elements in the worst case.
