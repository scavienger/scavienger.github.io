---
layout: post
title: "XOR After Range Multiplication Queries I"
date: 2026-04-08 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Divide and Conquer", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/xor-after-range-multiplication-queries-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int xorAfterQueries(vector<int>& nums, vector<vector<int>>&\
        \ queries) {\n        long long MOD = 1000000007;\n        int n = nums.size();\n\
        \        for (const auto& query : queries) {\n            int l = query[0];\n\
        \            int r = query[1];\n            int k = query[2];\n            long\
        \ long v = query[3];\n            for (int i = l; i <= r; i += k) {\n      \
        \          nums[i] = (1LL * nums[i] * v) % MOD;\n            }\n        }\n\
        \        int result = 0;\n        for (int num : nums) {\n            result\
        \ ^= num;\n        }\n        return result;\n    }\n};"
      java: "class Solution {\n    public int xorAfterQueries(int[] nums, int[][] queries)\
        \ {\n        long MOD = 1000000007L;\n        int n = nums.length;\n       \
        \ for (int[] query : queries) {\n            int l = query[0];\n           \
        \ int r = query[1];\n            int k = query[2];\n            long v = (long)\
        \ query[3];\n            for (int i = l; i <= r; i += k) {\n               \
        \ nums[i] = (int) (((long) nums[i] * v) % MOD);\n            }\n        }\n\
        \        int result = 0;\n        for (int num : nums) {\n            result\
        \ ^= num;\n        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def xorAfterQueries(self, nums, queries):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type queries: List[List[int]]\n\
        \        :rtype: int\n        \"\"\"\n        MOD = 10**9 + 7\n        for l,\
        \ r, k, v in queries:\n            for i in range(l, r + 1, k):\n          \
        \      nums[i] = (nums[i] * v) % MOD\n\n        res = 0\n        for x in nums:\n\
        \            res ^= x\n        return res"
      python3: "class Solution:\n    def xorAfterQueries(self, nums: List[int], queries:\
        \ List[List[int]]) -> int:\n        MOD = 10**9 + 7\n        for l, r, k, v\
        \ in queries:\n            for i in range(l, r + 1, k):\n                nums[i]\
        \ = (nums[i] * v) % MOD\n\n        res = 0\n        for x in nums:\n       \
        \     res ^= x\n        return res"
      c: "int xorAfterQueries(int* nums, int numsSize, int** queries, int queriesSize,\
        \ int* queriesColSize) {\n    long long MOD = 1000000007;\n    for (int i =\
        \ 0; i < queriesSize; i++) {\n        int l = queries[i][0];\n        int r\
        \ = queries[i][1];\n        int k = queries[i][2];\n        long long v = queries[i][3];\n\
        \        for (int j = l; j <= r; j += k) {\n            nums[j] = (int)((1LL\
        \ * nums[j] * v) % MOD);\n        }\n    }\n    int result = 0;\n    for (int\
        \ i = 0; i < numsSize; i++) {\n        result ^= nums[i];\n    }\n    return\
        \ result;\n}"
      csharp: "public class Solution {\n    public int XorAfterQueries(int[] nums, int[][]\
        \ queries) {\n        long mod = 1000000007;\n        for (int i = 0; i < queries.Length;\
        \ i++) {\n            int l = queries[i][0];\n            int r = queries[i][1];\n\
        \            int k = queries[i][2];\n            long v = (long)queries[i][3];\n\
        \            for (int idx = l; idx <= r; idx += k) {\n                long current\
        \ = (long)nums[idx];\n                nums[idx] = (int)((current * v) % mod);\n\
        \            }\n        }\n        int result = 0;\n        for (int i = 0;\
        \ i < nums.Length; i++) {\n            result ^= nums[i];\n        }\n     \
        \   return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number[][]} queries\n\
        \ * @return {number}\n */\nvar xorAfterQueries = function(nums, queries) {\n\
        \    const MOD = 1000000007;\n    for (let i = 0; i < queries.length; i++) {\n\
        \        const l = queries[i][0];\n        const r = queries[i][1];\n      \
        \  const k = queries[i][2];\n        const v = queries[i][3];\n        for (let\
        \ idx = l; idx <= r; idx += k) {\n            nums[idx] = (nums[idx] * v) %\
        \ MOD;\n        }\n    }\n    let result = 0;\n    for (let i = 0; i < nums.length;\
        \ i++) {\n        result ^= nums[i];\n    }\n    return result;\n};"
      typescript: "function xorAfterQueries(nums: number[], queries: number[][]): number\
        \ {\n    const MOD: number = 1000000007;\n    for (let i = 0; i < queries.length;\
        \ i++) {\n        const l = queries[i][0];\n        const r = queries[i][1];\n\
        \        const k = queries[i][2];\n        const v = queries[i][3];\n      \
        \  for (let idx = l; idx <= r; idx += k) {\n            nums[idx] = (nums[idx]\
        \ * v) % MOD;\n        }\n    }\n    let result: number = 0;\n    for (let i\
        \ = 0; i < nums.length; i++) {\n        result ^= nums[i];\n    }\n    return\
        \ result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer[][] $queries\n     * @return Integer\n     */\n    function xorAfterQueries($nums,\
        \ $queries) {\n        $mod = 1000000007;\n        foreach ($queries as $query)\
        \ {\n            $l = $query[0];\n            $r = $query[1];\n            $k\
        \ = $query[2];\n            $v = $query[3];\n            for ($idx = $l; $idx\
        \ <= $r; $idx += $k) {\n                $nums[$idx] = ($nums[$idx] * $v) % $mod;\n\
        \            }\n        }\n        $result = 0;\n        foreach ($nums as $num)\
        \ {\n            $result ^= $num;\n        }\n        return $result;\n    }\n\
        }"
      swift: "class Solution {\n    func xorAfterQueries(_ nums: [Int], _ queries: [[Int]])\
        \ -> Int {\n        var mutableNums = nums\n        let mod = 1000000007\n \
        \       for query in queries {\n            let l = query[0]\n            let\
        \ r = query[1]\n            let k = query[2]\n            let v = query[3]\n\
        \            var idx = l\n            while idx <= r {\n                mutableNums[idx]\
        \ = (mutableNums[idx] * v) % mod\n                idx += k\n            }\n\
        \        }\n        var result = 0\n        for num in mutableNums {\n     \
        \       result ^= num\n        }\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun xorAfterQueries(nums: IntArray, queries: Array<IntArray>):\
        \ Int {\n        val MOD: Long = 1000000007L\n        for (query in queries)\
        \ {\n            val l = query[0]\n            val r = query[1]\n          \
        \  val k = query[2]\n            val v = query[3].toLong()\n            var\
        \ idx = l\n            while (idx <= r) {\n                nums[idx] = ((nums[idx].toLong()\
        \ * v) % MOD).toInt()\n                idx += k\n            }\n        }\n\
        \        var result = 0\n        for (num in nums) {\n            result = result\
        \ xor num\n        }\n        return result\n    }\n}"
      dart: "class Solution {\n  int xorAfterQueries(List<int> nums, List<List<int>>\
        \ queries) {\n    const int mod = 1000000007;\n    for (final query in queries)\
        \ {\n      final int l = query[0];\n      final int r = query[1];\n      final\
        \ int k = query[2];\n      final int v = query[3];\n      for (int i = l; i\
        \ <= r; i += k) {\n        nums[i] = (nums[i] * v) % mod;\n      }\n    }\n\
        \    int result = 0;\n    for (final num in nums) {\n      result ^= num;\n\
        \    }\n    return result;\n  }\n}"
      go: "func xorAfterQueries(nums []int, queries [][]int) int {\n    const MOD int64\
        \ = 1000000007\n    for _, query := range queries {\n        l := query[0]\n\
        \        r := query[1]\n        k := query[2]\n        v := int64(query[3])\n\
        \        for i := l; i <= r; i += k {\n            nums[i] = int((int64(nums[i])\
        \ * v) % MOD)\n        }\n    }\n    result := 0\n    for _, num := range nums\
        \ {\n        result ^= num\n    }\n    return result\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer[][]} queries\n# @return {Integer}\n\
        def xor_after_queries(nums, queries)\n  mod = 1000000007\n  queries.each do\
        \ |query|\n    l = query[0]\n    r = query[1]\n    k = query[2]\n    v = query[3]\n\
        \    idx = l\n    while idx <= r\n      nums[idx] = (nums[idx] * v) % mod\n\
        \      idx += k\n    end\n  end\n  result = 0\n  nums.each do |num|\n    result\
        \ ^= num\n  end\n  result\nend"
      scala: "object Solution {\n    def xorAfterQueries(nums: Array[Int], queries:\
        \ Array[Array[Int]]): Int = {\n        val mod: Long = 1000000007L\n       \
        \ for (query <- queries) {\n            val l = query(0)\n            val r\
        \ = query(1)\n            val k = query(2)\n            val v = query(3).toLong\n\
        \            var idx = l\n            while (idx <= r) {\n                nums(idx)\
        \ = ((nums(idx).toLong * v) % mod).toInt\n                idx += k\n       \
        \     }\n        }\n        var result = 0\n        for (num <- nums) {\n  \
        \          result ^= num\n        }\n        result\n    }\n}"
      rust: "impl Solution {\n    pub fn xor_after_queries(nums: Vec<i32>, queries:\
        \ Vec<Vec<i32>>) -> i32 {\n        let mut nums = nums;\n        let m: i64\
        \ = 1_000_000_007;\n\n        for q in queries {\n            let l = q[0] as\
        \ usize;\n            let r = q[1] as usize;\n            let k = q[2] as usize;\n\
        \            let v = q[3] as i64;\n\n            let mut idx = l;\n        \
        \    while idx <= r {\n                nums[idx] = ((nums[idx] as i64 * v) %\
        \ m) as i32;\n                idx += k;\n            }\n        }\n\n      \
        \  let mut res = 0;\n        for x in nums {\n            res ^= x;\n      \
        \  }\n        res\n    }\n}"
      racket: "(define/contract (xor-after-queries nums queries)\n  (-> (listof exact-integer?)\
        \ (listof (listof exact-integer?)) exact-integer?)\n  (let* ([vec (list->vector\
        \ nums)]\n         [mod 1000000007])\n    (for ([q queries])\n      (let ([l\
        \ (list-ref q 0)]\n            [r (list-ref q 1)]\n            [k (list-ref\
        \ q 2)]\n            [v (list-ref q 3)])\n        (for ([idx (in-range l (+\
        \ r 1) k)])\n          (vector-set! vec idx (remainder (* (vector-ref vec idx)\
        \ v) mod)))))\n    (for/fold ([res 0])\n              ([x (in-vector vec)])\n\
        \      (bitwise-xor res x))))"
      erlang: "-spec xor_after_queries(Nums :: [integer()], Queries :: [[integer()]])\
        \ -> integer().\nxor_after_queries(Nums, Queries) ->\n  Mod = 1000000007,\n\
        \  Array = array:from_list(Nums),\n  FinalArray = lists:foldl(fun(Query, AccArr)\
        \ ->\n    [L, R, K, V] = Query,\n    update_array_helper(L, R, K, V, Mod, AccArr)\n\
        \  end, Array, Queries),\n  lists:foldl(fun(X, AccXor) -> AccXor bxor X end,\
        \ 0, array:to_list(FinalArray)).\n\nupdate_array_helper(Idx, R, K, V, Mod, AccArr)\
        \ when Idx =< R ->\n  Val = array:get(Idx, AccArr),\n  NewVal = (Val * V) rem\
        \ Mod,\n  NewAccArr = array:set(Idx, NewVal, AccArr),\n  update_array_helper(Idx\
        \ + K, R, K, V, Mod, NewAccArr);\nupdate_array_helper(_Idx, _R, _K, _V, _Mod,\
        \ AccArr) ->\n  AccArr."
      elixir: "defmodule Solution do\n  require Bitwise\n\n  @spec xor_after_queries(nums\
        \ :: [integer], queries :: [[integer]]) :: integer\n  def xor_after_queries(nums,\
        \ queries) do\n    mod = 1_000_000_007\n    nums_map = nums\n      |> Enum.with_index()\n\
        \      |> Map.new(fn {v, i} -> {i, v} end)\n\n    final_map = Enum.reduce(queries,\
        \ nums_map, fn [l, r, k, v], acc_map ->\n      update_range(l, r, k, v, mod,\
        \ acc_map)\n    end)\n\n    Enum.reduce(final_map, 0, fn {_idx, val}, acc ->\n\
        \      Bitwise.bxor(acc, val)\n    end)\n  end\n\n  defp update_range(idx, r,\
        \ k, v, mod, acc_map) when idx <= r do\n    new_val = rem(Map.get(acc_map, idx)\
        \ * v, mod)\n    update_range(idx + k, r, k, v, mod, Map.put(acc_map, idx, new_val))\n\
        \  end\n\n  defp update_range(_idx, _r, _k, _v, _mod, acc_map), do: acc_map\n\
        end"
    approach: 'The problem asks to perform a series of range multiplication updates
      on an array and return the final bitwise XOR sum of its elements. Given the constraints
      of $n \le 1000$ and $q \le 1000$, a direct simulation of the queries is efficient
      enough to pass within the time limit. For each query $[l_i, r_i, k_i, v_i]$, we
      iterate through the indices starting from $l_i$ up to $r_i$ with a step size of
      $k_i$, multiplying each visited element by $v_i$ and taking the result modulo
      $10^9 + 7$.


      To handle the multiplication correctly and avoid integer overflow, we perform
      the arithmetic using 64-bit integers (like long long in C++ or long in Java) before
      applying the modulo. Once all queries are processed, we perform a single pass
      through the updated array to compute the cumulative bitwise XOR of all its elements.
      This brute-force approach works effectively because the total number of update
      operations is at most $n \times q$, which is approximately $10^6$.'
    time_complexity: O(q * (n / k) + n) where q is the number of queries and n is the
      size of the array. In the worst case where k=1, this simplifies to O(q * n). With
      n, q <= 1000, the operations are well within the 10^6 range.
    space_complexity: O(1) extra space as we modify the input array in place and only
      use a few variables for iteration and result storage.
    elapsed_time: 550.3704121112823
    model: gemini-3-flash-preview
    generated_at: '2026-04-08 01:57:26 '
---

## Problem #3653: XOR After Range Multiplication Queries I

**Difficulty:** Medium

**Topics:** Array, Divide and Conquer, Simulation

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code> and a 2D integer array <code>queries</code> of size <code>q</code>, where <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>, k<sub>i</sub>, v<sub>i</sub>]</code>.</p>

<p>For each query, you must apply the following operations in order:</p>

<ul>
	<li>Set <code>idx = l<sub>i</sub></code>.</li>
	<li>While <code>idx &lt;= r<sub>i</sub></code>:
	<ul>
		<li>Update: <code>nums[idx] = (nums[idx] * v<sub>i</sub>) % (10<sup>9</sup> + 7)</code></li>
		<li>Set <code>idx += k<sub>i</sub></code>.</li>
	</ul>
	</li>
</ul>

<p>Return the <strong>bitwise XOR</strong> of all elements in <code>nums</code> after processing all queries.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1], queries = [[0,2,1,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li data-end="106" data-start="18">A single query <code data-end="44" data-start="33">[0, 2, 1, 4]</code> multiplies every element from index 0 through index 2 by 4.</li>
	<li data-end="157" data-start="109">The array changes from <code data-end="141" data-start="132">[1, 1, 1]</code> to <code data-end="154" data-start="145">[4, 4, 4]</code>.</li>
	<li data-end="205" data-start="160">The XOR of all elements is <code data-end="202" data-start="187">4 ^ 4 ^ 4 = 4</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,1,5,4], queries = [[1,4,2,3],[0,2,1,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">31</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li data-end="350" data-start="230">The first query <code data-end="257" data-start="246">[1, 4, 2, 3]</code> multiplies the elements at indices 1 and 3 by 3, transforming the array to <code data-end="347" data-start="333">[2, 9, 1, 15, 4]</code>.</li>
	<li data-end="466" data-start="353">The second query <code data-end="381" data-start="370">[0, 2, 1, 2]</code> multiplies the elements at indices 0, 1, and 2 by 2, resulting in <code data-end="463" data-start="448">[4, 18, 2, 15, 4]</code>.</li>
	<li data-end="532" data-is-last-node="" data-start="469">Finally, the XOR of all elements is <code data-end="531" data-start="505">4 ^ 18 ^ 2 ^ 15 ^ 4 = 31</code>.​​​​​​​<strong>​​​​​​​</strong></li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= q == queries.length &lt;= 10<sup>3</sup></code></li>
	<li><code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>, k<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt; n</code></li>
	<li><code>1 &lt;= k<sub>i</sub> &lt;= n</code></li>
	<li><code>1 &lt;= v<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Use bruteforce

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to perform a series of range multiplication updates on an array and return the final bitwise XOR sum of its elements. Given the constraints of $n \le 1000$ and $q \le 1000$, a direct simulation of the queries is efficient enough to pass within the time limit. For each query $[l_i, r_i, k_i, v_i]$, we iterate through the indices starting from $l_i$ up to $r_i$ with a step size of $k_i$, multiplying each visited element by $v_i$ and taking the result modulo $10^9 + 7$.

To handle the multiplication correctly and avoid integer overflow, we perform the arithmetic using 64-bit integers (like long long in C++ or long in Java) before applying the modulo. Once all queries are processed, we perform a single pass through the updated array to compute the cumulative bitwise XOR of all its elements. This brute-force approach works effectively because the total number of update operations is at most $n \times q$, which is approximately $10^6$.

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
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        long long MOD = 1000000007;
        int n = nums.size();
        for (const auto& query : queries) {
            int l = query[0];
            int r = query[1];
            int k = query[2];
            long long v = query[3];
            for (int i = l; i <= r; i += k) {
                nums[i] = (1LL * nums[i] * v) % MOD;
            }
        }
        int result = 0;
        for (int num : nums) {
            result ^= num;
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
    public int xorAfterQueries(int[] nums, int[][] queries) {
        long MOD = 1000000007L;
        int n = nums.length;
        for (int[] query : queries) {
            int l = query[0];
            int r = query[1];
            int k = query[2];
            long v = (long) query[3];
            for (int i = l; i <= r; i += k) {
                nums[i] = (int) (((long) nums[i] * v) % MOD);
            }
        }
        int result = 0;
        for (int num : nums) {
            result ^= num;
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
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD

        res = 0
        for x in nums:
            res ^= x
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD

        res = 0
        for x in nums:
            res ^= x
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int xorAfterQueries(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    long long MOD = 1000000007;
    for (int i = 0; i < queriesSize; i++) {
        int l = queries[i][0];
        int r = queries[i][1];
        int k = queries[i][2];
        long long v = queries[i][3];
        for (int j = l; j <= r; j += k) {
            nums[j] = (int)((1LL * nums[j] * v) % MOD);
        }
    }
    int result = 0;
    for (int i = 0; i < numsSize; i++) {
        result ^= nums[i];
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int XorAfterQueries(int[] nums, int[][] queries) {
        long mod = 1000000007;
        for (int i = 0; i < queries.Length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            int k = queries[i][2];
            long v = (long)queries[i][3];
            for (int idx = l; idx <= r; idx += k) {
                long current = (long)nums[idx];
                nums[idx] = (int)((current * v) % mod);
            }
        }
        int result = 0;
        for (int i = 0; i < nums.Length; i++) {
            result ^= nums[i];
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
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */
var xorAfterQueries = function(nums, queries) {
    const MOD = 1000000007;
    for (let i = 0; i < queries.length; i++) {
        const l = queries[i][0];
        const r = queries[i][1];
        const k = queries[i][2];
        const v = queries[i][3];
        for (let idx = l; idx <= r; idx += k) {
            nums[idx] = (nums[idx] * v) % MOD;
        }
    }
    let result = 0;
    for (let i = 0; i < nums.length; i++) {
        result ^= nums[i];
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function xorAfterQueries(nums: number[], queries: number[][]): number {
    const MOD: number = 1000000007;
    for (let i = 0; i < queries.length; i++) {
        const l = queries[i][0];
        const r = queries[i][1];
        const k = queries[i][2];
        const v = queries[i][3];
        for (let idx = l; idx <= r; idx += k) {
            nums[idx] = (nums[idx] * v) % MOD;
        }
    }
    let result: number = 0;
    for (let i = 0; i < nums.length; i++) {
        result ^= nums[i];
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
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer
     */
    function xorAfterQueries($nums, $queries) {
        $mod = 1000000007;
        foreach ($queries as $query) {
            $l = $query[0];
            $r = $query[1];
            $k = $query[2];
            $v = $query[3];
            for ($idx = $l; $idx <= $r; $idx += $k) {
                $nums[$idx] = ($nums[$idx] * $v) % $mod;
            }
        }
        $result = 0;
        foreach ($nums as $num) {
            $result ^= $num;
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
    func xorAfterQueries(_ nums: [Int], _ queries: [[Int]]) -> Int {
        var mutableNums = nums
        let mod = 1000000007
        for query in queries {
            let l = query[0]
            let r = query[1]
            let k = query[2]
            let v = query[3]
            var idx = l
            while idx <= r {
                mutableNums[idx] = (mutableNums[idx] * v) % mod
                idx += k
            }
        }
        var result = 0
        for num in mutableNums {
            result ^= num
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
    fun xorAfterQueries(nums: IntArray, queries: Array<IntArray>): Int {
        val MOD: Long = 1000000007L
        for (query in queries) {
            val l = query[0]
            val r = query[1]
            val k = query[2]
            val v = query[3].toLong()
            var idx = l
            while (idx <= r) {
                nums[idx] = ((nums[idx].toLong() * v) % MOD).toInt()
                idx += k
            }
        }
        var result = 0
        for (num in nums) {
            result = result xor num
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
class Solution {
  int xorAfterQueries(List<int> nums, List<List<int>> queries) {
    const int mod = 1000000007;
    for (final query in queries) {
      final int l = query[0];
      final int r = query[1];
      final int k = query[2];
      final int v = query[3];
      for (int i = l; i <= r; i += k) {
        nums[i] = (nums[i] * v) % mod;
      }
    }
    int result = 0;
    for (final num in nums) {
      result ^= num;
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
func xorAfterQueries(nums []int, queries [][]int) int {
    const MOD int64 = 1000000007
    for _, query := range queries {
        l := query[0]
        r := query[1]
        k := query[2]
        v := int64(query[3])
        for i := l; i <= r; i += k {
            nums[i] = int((int64(nums[i]) * v) % MOD)
        }
    }
    result := 0
    for _, num := range nums {
        result ^= num
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def xor_after_queries(nums, queries)
  mod = 1000000007
  queries.each do |query|
    l = query[0]
    r = query[1]
    k = query[2]
    v = query[3]
    idx = l
    while idx <= r
      nums[idx] = (nums[idx] * v) % mod
      idx += k
    end
  end
  result = 0
  nums.each do |num|
    result ^= num
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
    def xorAfterQueries(nums: Array[Int], queries: Array[Array[Int]]): Int = {
        val mod: Long = 1000000007L
        for (query <- queries) {
            val l = query(0)
            val r = query(1)
            val k = query(2)
            val v = query(3).toLong
            var idx = l
            while (idx <= r) {
                nums(idx) = ((nums(idx).toLong * v) % mod).toInt
                idx += k
            }
        }
        var result = 0
        for (num <- nums) {
            result ^= num
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
    pub fn xor_after_queries(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let mut nums = nums;
        let m: i64 = 1_000_000_007;

        for q in queries {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let k = q[2] as usize;
            let v = q[3] as i64;

            let mut idx = l;
            while idx <= r {
                nums[idx] = ((nums[idx] as i64 * v) % m) as i32;
                idx += k;
            }
        }

        let mut res = 0;
        for x in nums {
            res ^= x;
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (xor-after-queries nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ([vec (list->vector nums)]
         [mod 1000000007])
    (for ([q queries])
      (let ([l (list-ref q 0)]
            [r (list-ref q 1)]
            [k (list-ref q 2)]
            [v (list-ref q 3)])
        (for ([idx (in-range l (+ r 1) k)])
          (vector-set! vec idx (remainder (* (vector-ref vec idx) v) mod)))))
    (for/fold ([res 0])
              ([x (in-vector vec)])
      (bitwise-xor res x))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec xor_after_queries(Nums :: [integer()], Queries :: [[integer()]]) -> integer().
xor_after_queries(Nums, Queries) ->
  Mod = 1000000007,
  Array = array:from_list(Nums),
  FinalArray = lists:foldl(fun(Query, AccArr) ->
    [L, R, K, V] = Query,
    update_array_helper(L, R, K, V, Mod, AccArr)
  end, Array, Queries),
  lists:foldl(fun(X, AccXor) -> AccXor bxor X end, 0, array:to_list(FinalArray)).

update_array_helper(Idx, R, K, V, Mod, AccArr) when Idx =< R ->
  Val = array:get(Idx, AccArr),
  NewVal = (Val * V) rem Mod,
  NewAccArr = array:set(Idx, NewVal, AccArr),
  update_array_helper(Idx + K, R, K, V, Mod, NewAccArr);
update_array_helper(_Idx, _R, _K, _V, _Mod, AccArr) ->
  AccArr.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  require Bitwise

  @spec xor_after_queries(nums :: [integer], queries :: [[integer]]) :: integer
  def xor_after_queries(nums, queries) do
    mod = 1_000_000_007
    nums_map = nums
      |> Enum.with_index()
      |> Map.new(fn {v, i} -> {i, v} end)

    final_map = Enum.reduce(queries, nums_map, fn [l, r, k, v], acc_map ->
      update_range(l, r, k, v, mod, acc_map)
    end)

    Enum.reduce(final_map, 0, fn {_idx, val}, acc ->
      Bitwise.bxor(acc, val)
    end)
  end

  defp update_range(idx, r, k, v, mod, acc_map) when idx <= r do
    new_val = rem(Map.get(acc_map, idx) * v, mod)
    update_range(idx + k, r, k, v, mod, Map.put(acc_map, idx, new_val))
  end

  defp update_range(_idx, _r, _k, _v, _mod, acc_map), do: acc_map
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(q * (n / k) + n) where q is the number of queries and n is the size of the array. In the worst case where k=1, this simplifies to O(q * n). With n, q <= 1000, the operations are well within the 10^6 range.
- **Space Complexity:** O(1) extra space as we modify the input array in place and only use a few variables for iteration and result storage.
