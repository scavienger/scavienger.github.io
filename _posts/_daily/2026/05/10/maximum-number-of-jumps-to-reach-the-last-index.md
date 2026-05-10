---
layout: post
title: "Maximum Number of Jumps to Reach the Last Index"
date: 2026-05-10 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass\
        \ Solution {\npublic:\n    int maximumJumps(vector<int>& nums, int target) {\n\
        \        int n = nums.size();\n        vector<int> dp(n, -1);\n        dp[0]\
        \ = 0;\n\n        for (int j = 1; j < n; ++j) {\n            for (int i = 0;\
        \ i < j; ++i) {\n                if (dp[i] != -1) {\n                    long\
        \ long diff = (long long)nums[j] - nums[i];\n                    if (diff <\
        \ 0) diff = -diff;\n                    if (diff <= (long long)target) {\n \
        \                       dp[j] = max(dp[j], dp[i] + 1);\n                   \
        \ }\n                }\n            }\n        }\n\n        return dp[n - 1];\n\
        \    }\n};"
      java: "class Solution {\n    public int maximumJumps(int[] nums, int target) {\n\
        \        int n = nums.length;\n        int[] dp = new int[n];\n        for (int\
        \ i = 0; i < n; i++) {\n            dp[i] = -1;\n        }\n        dp[0] =\
        \ 0;\n\n        for (int j = 1; j < n; j++) {\n            for (int i = 0; i\
        \ < j; i++) {\n                if (dp[i] != -1) {\n                    long\
        \ diff = (long) nums[j] - nums[i];\n                    if (Math.abs(diff) <=\
        \ (long) target) {\n                        dp[j] = Math.max(dp[j], dp[i] +\
        \ 1);\n                    }\n                }\n            }\n        }\n\n\
        \        return dp[n - 1];\n    }\n}"
      python: "class Solution(object):\n    def maximumJumps(self, nums, target):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type target: int\n\
        \        :rtype: int\n        \"\"\"\n        n = len(nums)\n        dp = [-1]\
        \ * n\n        dp[0] = 0\n\n        for j in range(1, n):\n            for i\
        \ in range(j):\n                if dp[i] != -1:\n                    if abs(nums[j]\
        \ - nums[i]) <= target:\n                        dp[j] = max(dp[j], dp[i] +\
        \ 1)\n\n        return dp[n - 1]"
      python3: "class Solution:\n    def maximumJumps(self, nums: List[int], target:\
        \ int) -> int:\n        n = len(nums)\n        dp = [-1] * n\n        dp[0]\
        \ = 0\n\n        for j in range(1, n):\n            for i in range(j):\n   \
        \             if dp[i] != -1:\n                    if abs(nums[j] - nums[i])\
        \ <= target:\n                        dp[j] = max(dp[j], dp[i] + 1)\n\n    \
        \    return dp[n - 1]"
      c: "#include <stdlib.h>\n\nint maximumJumps(int* nums, int numsSize, int target)\
        \ {\n    int* dp = (int*)malloc(numsSize * sizeof(int));\n    for (int i = 0;\
        \ i < numsSize; i++) {\n        dp[i] = -1;\n    }\n    dp[0] = 0;\n\n    for\
        \ (int j = 1; j < numsSize; j++) {\n        for (int i = 0; i < j; i++) {\n\
        \            if (dp[i] != -1) {\n                long long diff = (long long)nums[j]\
        \ - (long long)nums[i];\n                if (diff < 0) diff = -diff;\n     \
        \           if (diff <= (long long)target) {\n                    if (dp[i]\
        \ + 1 > dp[j]) {\n                        dp[j] = dp[i] + 1;\n             \
        \       }\n                }\n            }\n        }\n    }\n\n    int result\
        \ = dp[numsSize - 1];\n    free(dp);\n    return result;\n}"
      csharp: "public class Solution {\n    public int MaximumJumps(int[] nums, int\
        \ target) {\n        int n = nums.Length;\n        int[] dp = new int[n];\n\
        \        for (int i = 1; i < n; i++) {\n            dp[i] = -1;\n        }\n\
        \        dp[0] = 0;\n\n        for (int j = 1; j < n; j++) {\n            for\
        \ (int i = 0; i < j; i++) {\n                if (dp[i] != -1) {\n          \
        \          long diff = (long)nums[j] - nums[i];\n                    if (diff\
        \ >= -target && diff <= target) {\n                        dp[j] = Math.Max(dp[j],\
        \ dp[i] + 1);\n                    }\n                }\n            }\n   \
        \     }\n\n        return dp[n - 1];\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} target\n * @return\
        \ {number}\n */\nvar maximumJumps = function(nums, target) {\n    const n =\
        \ nums.length;\n    const dp = new Array(n).fill(-1);\n    dp[0] = 0;\n\n  \
        \  for (let j = 1; j < n; j++) {\n        for (let i = 0; i < j; i++) {\n  \
        \          if (dp[i] !== -1) {\n                const diff = nums[j] - nums[i];\n\
        \                if (diff >= -target && diff <= target) {\n                \
        \    dp[j] = Math.max(dp[j], dp[i] + 1);\n                }\n            }\n\
        \        }\n    }\n\n    return dp[n - 1];\n};"
      typescript: "function maximumJumps(nums: number[], target: number): number {\n\
        \    const n = nums.length;\n    const dp: number[] = new Array(n).fill(-1);\n\
        \    dp[0] = 0;\n\n    for (let j = 1; j < n; j++) {\n        for (let i = 0;\
        \ i < j; i++) {\n            if (dp[i] !== -1) {\n                const diff\
        \ = nums[j] - nums[i];\n                if (diff >= -target && diff <= target)\
        \ {\n                    dp[j] = Math.max(dp[j], dp[i] + 1);\n             \
        \   }\n            }\n        }\n    }\n\n    return dp[n - 1];\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $target\n     * @return Integer\n     */\n    function maximumJumps($nums,\
        \ $target) {\n        $n = count($nums);\n        $dp = array_fill(0, $n, -1);\n\
        \        $dp[0] = 0;\n\n        for ($j = 1; $j < $n; $j++) {\n            for\
        \ ($i = 0; $i < $j; $i++) {\n                if ($dp[$i] !== -1) {\n       \
        \             $diff = $nums[$j] - $nums[$i];\n                    if ($diff\
        \ >= -$target && $diff <= $target) {\n                        $dp[$j] = max($dp[$j],\
        \ $dp[$i] + 1);\n                    }\n                }\n            }\n \
        \       }\n\n        return $dp[$n - 1];\n    }\n}"
      swift: "class Solution {\n    func maximumJumps(_ nums: [Int], _ target: Int)\
        \ -> Int {\n        let n = nums.count\n        var dp = [Int](repeating: -1,\
        \ count: n)\n        dp[0] = 0\n\n        for j in 1..<n {\n            for\
        \ i in 0..<j {\n                if dp[i] != -1 {\n                    let diff\
        \ = nums[j] - nums[i]\n                    if diff >= -target && diff <= target\
        \ {\n                        dp[j] = max(dp[j], dp[i] + 1)\n               \
        \     }\n                }\n            }\n        }\n\n        return dp[n\
        \ - 1]\n    }\n}"
      kotlin: "class Solution {\n    fun maximumJumps(nums: IntArray, target: Int):\
        \ Int {\n        val n = nums.size\n        val dp = IntArray(n) { -1 }\n  \
        \      dp[0] = 0\n        for (j in 1 until n) {\n            for (i in 0 until\
        \ j) {\n                if (dp[i] != -1) {\n                    val diff = nums[j].toLong()\
        \ - nums[i].toLong()\n                    val absDiff = if (diff < 0) -diff\
        \ else diff\n                    if (absDiff <= target.toLong()) {\n       \
        \                 if (dp[i] + 1 > dp[j]) {\n                            dp[j]\
        \ = dp[i] + 1\n                        }\n                    }\n          \
        \      }\n            }\n        }\n        return dp[n - 1]\n    }\n}"
      dart: "class Solution {\n  int maximumJumps(List<int> nums, int target) {\n  \
        \  int n = nums.length;\n    List<int> dp = List.filled(n, -1);\n    dp[0] =\
        \ 0;\n    for (int j = 1; j < n; j++) {\n      for (int i = 0; i < j; i++) {\n\
        \        if (dp[i] != -1) {\n          int diff = nums[j] - nums[i];\n     \
        \     int absDiff = diff < 0 ? -diff : diff;\n          if (absDiff <= target)\
        \ {\n            if (dp[i] + 1 > dp[j]) {\n              dp[j] = dp[i] + 1;\n\
        \            }\n          }\n        }\n      }\n    }\n    return dp[n - 1];\n\
        \  }\n}"
      go: "func maximumJumps(nums []int, target int) int {\n    n := len(nums)\n   \
        \ dp := make([]int, n)\n    for i := 1; i < n; i++ {\n        dp[i] = -1\n \
        \   }\n    dp[0] = 0\n    for j := 1; j < n; j++ {\n        for i := 0; i <\
        \ j; i++ {\n            if dp[i] != -1 {\n                diff := int64(nums[j])\
        \ - int64(nums[i])\n                absDiff := diff\n                if absDiff\
        \ < 0 {\n                    absDiff = -absDiff\n                }\n       \
        \         if absDiff <= int64(target) {\n                    if dp[i]+1 > dp[j]\
        \ {\n                        dp[j] = dp[i] + 1\n                    }\n    \
        \            }\n            }\n        }\n    }\n    return dp[n-1]\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer}\n\
        def maximum_jumps(nums, target)\n    n = nums.length\n    dp = Array.new(n,\
        \ -1)\n    dp[0] = 0\n    (1...n).each do |j|\n        (0...j).each do |i|\n\
        \            if dp[i] != -1\n                diff = nums[j] - nums[i]\n    \
        \            if diff.abs <= target\n                    if dp[i] + 1 > dp[j]\n\
        \                        dp[j] = dp[i] + 1\n                    end\n      \
        \          end\n            end\n        end\n    end\n    dp[n - 1]\nend"
      scala: "object Solution {\n    def maximumJumps(nums: Array[Int], target: Int):\
        \ Int = {\n        val n = nums.length\n        val dp = Array.fill(n)(-1)\n\
        \        dp(0) = 0\n        for (j <- 1 until n) {\n            for (i <- 0\
        \ until j) {\n                if (dp(i) != -1) {\n                    val diff\
        \ = nums(j).toLong - nums(i).toLong\n                    val absDiff = if (diff\
        \ < 0) -diff else diff\n                    if (absDiff <= target.toLong) {\n\
        \                        if (dp(i) + 1 > dp(j)) {\n                        \
        \    dp(j) = dp(i) + 1\n                        }\n                    }\n \
        \               }\n            }\n        }\n        dp(n - 1)\n    }\n}"
      rust: "impl Solution {\n    pub fn maximum_jumps(nums: Vec<i32>, target: i32)\
        \ -> i32 {\n        let n = nums.len();\n        let mut dp = vec![-1; n];\n\
        \        dp[0] = 0;\n        let target = target as i64;\n\n        for j in\
        \ 1..n {\n            for i in 0..j {\n                if dp[i] != -1 {\n  \
        \                  let val_i = nums[i] as i64;\n                    let val_j\
        \ = nums[j] as i64;\n                    if (val_j - val_i).abs() <= target\
        \ {\n                        dp[j] = dp[j].max(dp[i] + 1);\n               \
        \     }\n                }\n            }\n        }\n\n        dp[n - 1]\n\
        \    }\n}"
      racket: "(define/contract (maximum-jumps nums target)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([n (length nums)]\n         [nums-vec\
        \ (list->vector nums)]\n         [dp (make-vector n -1)])\n    (vector-set!\
        \ dp 0 0)\n    (for ([j (in-range 1 n)])\n      (for ([i (in-range 0 j)])\n\
        \        (let ([dp-i (vector-ref dp i)]\n              [val-i (vector-ref nums-vec\
        \ i)]\n              [val-j (vector-ref nums-vec j)])\n          (when (and\
        \ (not (= dp-i -1))\n                     (<= (abs (- val-j val-i)) target))\n\
        \            (vector-set! dp j (max (vector-ref dp j) (+ dp-i 1)))))))\n   \
        \ (vector-ref dp (- n 1))))"
      erlang: "-spec maximum_jumps(Nums :: [integer()], Target :: integer()) -> integer().\n\
        maximum_jumps(Nums, Target) ->\n  NumsVec = list_to_tuple(Nums),\n  N = tuple_size(NumsVec),\n\
        \  InitialDP = #{0 => 0},\n  IndicesJ = lists:seq(1, N - 1),\n  FinalDP = lists:foldl(fun(J,\
        \ AccDP) ->\n    ValJ = element(J + 1, NumsVec),\n    MaxJ = lists:foldl(fun(I,\
        \ CurrentMax) ->\n      DPI = maps:get(I, AccDP, -1),\n      ValI = element(I\
        \ + 1, NumsVec),\n      case (DPI =/= -1) andalso (abs(ValJ - ValI) =< Target)\
        \ of\n        true ->\n          erlang:max(CurrentMax, DPI + 1);\n        false\
        \ ->\n          CurrentMax\n      end\n    end, -1, lists:seq(0, J - 1)),\n\
        \    maps:put(J, MaxJ, AccDP)\n  end, InitialDP, IndicesJ),\n  maps:get(N -\
        \ 1, FinalDP, -1)."
      elixir: "defmodule Solution do\n  @spec maximum_jumps(nums :: [integer], target\
        \ :: integer) :: integer\n  def maximum_jumps(nums, target) do\n    n = length(nums)\n\
        \    nums_tuple = List.to_tuple(nums)\n\n    dp_final =\n      Enum.reduce(1..(n\
        \ - 1), %{0 => 0}, fn j, acc_dp ->\n        val_j = elem(nums_tuple, j)\n\n\
        \        max_j =\n          Enum.reduce(0..(j - 1), -1, fn i, current_max ->\n\
        \            dp_i = Map.get(acc_dp, i, -1)\n            val_i = elem(nums_tuple,\
        \ i)\n\n            if dp_i != -1 and abs(val_j - val_i) <= target do\n    \
        \          max(current_max, dp_i + 1)\n            else\n              current_max\n\
        \            end\n          end)\n\n        Map.put(acc_dp, j, max_j)\n    \
        \  end)\n\n    Map.get(dp_final, n - 1, -1)\n  end\nend"
    approach: The problem can be framed as finding the maximum path length in a Directed
      Acyclic Graph (DAG) where each index from 0 to n-1 is a node. A directed edge
      exists from index i to index j if i < j and the jump condition -target <= nums[j]
      - nums[i] <= target is satisfied. To find the maximum number of jumps to reach
      the last index, we use dynamic programming. We define a dp array where dp[i] represents
      the maximum number of jumps possible to reach index i from the starting position
      at index 0. We initialize dp[0] to 0 and all other positions to -1, which signifies
      that those indices are initially unreachable.
    time_complexity: O(n^2) where n is the number of elements in the nums array. This
      complexity arises from the nested loop structure where, for each index j, we iterate
      through all previous indices i to check for valid jump conditions.
    space_complexity: O(n) where n is the number of elements in the nums array. This
      space is required to store the dp array of size n, which tracks the maximum number
      of jumps to reach each index.
    elapsed_time: 157.4080319404602
    model: gemini-3-flash-preview
    generated_at: '2026-05-10 02:14:11 '
---

## Problem #2770: Maximum Number of Jumps to Reach the Last Index

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming

## Problem Description

<p>You are given a <strong>0-indexed</strong> array <code>nums</code> of <code>n</code> integers and an integer <code>target</code>.</p>

<p>You are initially positioned at index <code>0</code>. In one step, you can jump from index <code>i</code> to any index <code>j</code> such that:</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; n</code></li>
	<li><code>-target &lt;= nums[j] - nums[i] &lt;= target</code></li>
</ul>

<p>Return <em>the <strong>maximum number of jumps</strong> you can make to reach index</em> <code>n - 1</code>.</p>

<p>If there is no way to reach index <code>n - 1</code>, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,6,4,1,2], target = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1. 
- Jump from index 1 to index 3.
- Jump from index 3 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 3 jumps. Hence, the answer is 3. </pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,6,4,1,2], target = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1.
- Jump from index 1 to index 2.
- Jump from index 2 to index 3.
- Jump from index 3 to index 4.
- Jump from index 4 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 5 jumps. Hence, the answer is 5. </pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,6,4,1,2], target = 0
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be proven that there is no jumping sequence that goes from 0 to n - 1. Hence, the answer is -1. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length == n &lt;= 1000</code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= target &lt;= 2 * 10<sup>9</sup></code></li>
</ul>


## Hints

1. Use a dynamic programming approach.

2. Define a dynamic programming array dp of size n, where dp[i] represents the maximum number of jumps from index 0 to index i.

3. For each j iterate over all i < j. Set dp[j] = max(dp[j], dp[i] + 1) if -target <= nums[j] - nums[i] <= target.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be framed as finding the maximum path length in a Directed Acyclic Graph (DAG) where each index from 0 to n-1 is a node. A directed edge exists from index i to index j if i < j and the jump condition -target <= nums[j] - nums[i] <= target is satisfied. To find the maximum number of jumps to reach the last index, we use dynamic programming. We define a dp array where dp[i] represents the maximum number of jumps possible to reach index i from the starting position at index 0. We initialize dp[0] to 0 and all other positions to -1, which signifies that those indices are initially unreachable.

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
#include <algorithm>

using namespace std;

class Solution {
public:
    int maximumJumps(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> dp(n, -1);
        dp[0] = 0;

        for (int j = 1; j < n; ++j) {
            for (int i = 0; i < j; ++i) {
                if (dp[i] != -1) {
                    long long diff = (long long)nums[j] - nums[i];
                    if (diff < 0) diff = -diff;
                    if (diff <= (long long)target) {
                        dp[j] = max(dp[j], dp[i] + 1);
                    }
                }
            }
        }

        return dp[n - 1];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maximumJumps(int[] nums, int target) {
        int n = nums.length;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = -1;
        }
        dp[0] = 0;

        for (int j = 1; j < n; j++) {
            for (int i = 0; i < j; i++) {
                if (dp[i] != -1) {
                    long diff = (long) nums[j] - nums[i];
                    if (Math.abs(diff) <= (long) target) {
                        dp[j] = Math.max(dp[j], dp[i] + 1);
                    }
                }
            }
        }

        return dp[n - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for j in range(1, n):
            for i in range(j):
                if dp[i] != -1:
                    if abs(nums[j] - nums[i]) <= target:
                        dp[j] = max(dp[j], dp[i] + 1)

        return dp[n - 1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for j in range(1, n):
            for i in range(j):
                if dp[i] != -1:
                    if abs(nums[j] - nums[i]) <= target:
                        dp[j] = max(dp[j], dp[i] + 1)

        return dp[n - 1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int maximumJumps(int* nums, int numsSize, int target) {
    int* dp = (int*)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        dp[i] = -1;
    }
    dp[0] = 0;

    for (int j = 1; j < numsSize; j++) {
        for (int i = 0; i < j; i++) {
            if (dp[i] != -1) {
                long long diff = (long long)nums[j] - (long long)nums[i];
                if (diff < 0) diff = -diff;
                if (diff <= (long long)target) {
                    if (dp[i] + 1 > dp[j]) {
                        dp[j] = dp[i] + 1;
                    }
                }
            }
        }
    }

    int result = dp[numsSize - 1];
    free(dp);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximumJumps(int[] nums, int target) {
        int n = nums.Length;
        int[] dp = new int[n];
        for (int i = 1; i < n; i++) {
            dp[i] = -1;
        }
        dp[0] = 0;

        for (int j = 1; j < n; j++) {
            for (int i = 0; i < j; i++) {
                if (dp[i] != -1) {
                    long diff = (long)nums[j] - nums[i];
                    if (diff >= -target && diff <= target) {
                        dp[j] = Math.Max(dp[j], dp[i] + 1);
                    }
                }
            }
        }

        return dp[n - 1];
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
 * @param {number} target
 * @return {number}
 */
var maximumJumps = function(nums, target) {
    const n = nums.length;
    const dp = new Array(n).fill(-1);
    dp[0] = 0;

    for (let j = 1; j < n; j++) {
        for (let i = 0; i < j; i++) {
            if (dp[i] !== -1) {
                const diff = nums[j] - nums[i];
                if (diff >= -target && diff <= target) {
                    dp[j] = Math.max(dp[j], dp[i] + 1);
                }
            }
        }
    }

    return dp[n - 1];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximumJumps(nums: number[], target: number): number {
    const n = nums.length;
    const dp: number[] = new Array(n).fill(-1);
    dp[0] = 0;

    for (let j = 1; j < n; j++) {
        for (let i = 0; i < j; i++) {
            if (dp[i] !== -1) {
                const diff = nums[j] - nums[i];
                if (diff >= -target && diff <= target) {
                    dp[j] = Math.max(dp[j], dp[i] + 1);
                }
            }
        }
    }

    return dp[n - 1];
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
     * @param Integer $target
     * @return Integer
     */
    function maximumJumps($nums, $target) {
        $n = count($nums);
        $dp = array_fill(0, $n, -1);
        $dp[0] = 0;

        for ($j = 1; $j < $n; $j++) {
            for ($i = 0; $i < $j; $i++) {
                if ($dp[$i] !== -1) {
                    $diff = $nums[$j] - $nums[$i];
                    if ($diff >= -$target && $diff <= $target) {
                        $dp[$j] = max($dp[$j], $dp[$i] + 1);
                    }
                }
            }
        }

        return $dp[$n - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximumJumps(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var dp = [Int](repeating: -1, count: n)
        dp[0] = 0

        for j in 1..<n {
            for i in 0..<j {
                if dp[i] != -1 {
                    let diff = nums[j] - nums[i]
                    if diff >= -target && diff <= target {
                        dp[j] = max(dp[j], dp[i] + 1)
                    }
                }
            }
        }

        return dp[n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximumJumps(nums: IntArray, target: Int): Int {
        val n = nums.size
        val dp = IntArray(n) { -1 }
        dp[0] = 0
        for (j in 1 until n) {
            for (i in 0 until j) {
                if (dp[i] != -1) {
                    val diff = nums[j].toLong() - nums[i].toLong()
                    val absDiff = if (diff < 0) -diff else diff
                    if (absDiff <= target.toLong()) {
                        if (dp[i] + 1 > dp[j]) {
                            dp[j] = dp[i] + 1
                        }
                    }
                }
            }
        }
        return dp[n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maximumJumps(List<int> nums, int target) {
    int n = nums.length;
    List<int> dp = List.filled(n, -1);
    dp[0] = 0;
    for (int j = 1; j < n; j++) {
      for (int i = 0; i < j; i++) {
        if (dp[i] != -1) {
          int diff = nums[j] - nums[i];
          int absDiff = diff < 0 ? -diff : diff;
          if (absDiff <= target) {
            if (dp[i] + 1 > dp[j]) {
              dp[j] = dp[i] + 1;
            }
          }
        }
      }
    }
    return dp[n - 1];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maximumJumps(nums []int, target int) int {
    n := len(nums)
    dp := make([]int, n)
    for i := 1; i < n; i++ {
        dp[i] = -1
    }
    dp[0] = 0
    for j := 1; j < n; j++ {
        for i := 0; i < j; i++ {
            if dp[i] != -1 {
                diff := int64(nums[j]) - int64(nums[i])
                absDiff := diff
                if absDiff < 0 {
                    absDiff = -absDiff
                }
                if absDiff <= int64(target) {
                    if dp[i]+1 > dp[j] {
                        dp[j] = dp[i] + 1
                    }
                }
            }
        }
    }
    return dp[n-1]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def maximum_jumps(nums, target)
    n = nums.length
    dp = Array.new(n, -1)
    dp[0] = 0
    (1...n).each do |j|
        (0...j).each do |i|
            if dp[i] != -1
                diff = nums[j] - nums[i]
                if diff.abs <= target
                    if dp[i] + 1 > dp[j]
                        dp[j] = dp[i] + 1
                    end
                end
            end
        end
    end
    dp[n - 1]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximumJumps(nums: Array[Int], target: Int): Int = {
        val n = nums.length
        val dp = Array.fill(n)(-1)
        dp(0) = 0
        for (j <- 1 until n) {
            for (i <- 0 until j) {
                if (dp(i) != -1) {
                    val diff = nums(j).toLong - nums(i).toLong
                    val absDiff = if (diff < 0) -diff else diff
                    if (absDiff <= target.toLong) {
                        if (dp(i) + 1 > dp(j)) {
                            dp(j) = dp(i) + 1
                        }
                    }
                }
            }
        }
        dp(n - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximum_jumps(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut dp = vec![-1; n];
        dp[0] = 0;
        let target = target as i64;

        for j in 1..n {
            for i in 0..j {
                if dp[i] != -1 {
                    let val_i = nums[i] as i64;
                    let val_j = nums[j] as i64;
                    if (val_j - val_i).abs() <= target {
                        dp[j] = dp[j].max(dp[i] + 1);
                    }
                }
            }
        }

        dp[n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximum-jumps nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [dp (make-vector n -1)])
    (vector-set! dp 0 0)
    (for ([j (in-range 1 n)])
      (for ([i (in-range 0 j)])
        (let ([dp-i (vector-ref dp i)]
              [val-i (vector-ref nums-vec i)]
              [val-j (vector-ref nums-vec j)])
          (when (and (not (= dp-i -1))
                     (<= (abs (- val-j val-i)) target))
            (vector-set! dp j (max (vector-ref dp j) (+ dp-i 1)))))))
    (vector-ref dp (- n 1))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_jumps(Nums :: [integer()], Target :: integer()) -> integer().
maximum_jumps(Nums, Target) ->
  NumsVec = list_to_tuple(Nums),
  N = tuple_size(NumsVec),
  InitialDP = #{0 => 0},
  IndicesJ = lists:seq(1, N - 1),
  FinalDP = lists:foldl(fun(J, AccDP) ->
    ValJ = element(J + 1, NumsVec),
    MaxJ = lists:foldl(fun(I, CurrentMax) ->
      DPI = maps:get(I, AccDP, -1),
      ValI = element(I + 1, NumsVec),
      case (DPI =/= -1) andalso (abs(ValJ - ValI) =< Target) of
        true ->
          erlang:max(CurrentMax, DPI + 1);
        false ->
          CurrentMax
      end
    end, -1, lists:seq(0, J - 1)),
    maps:put(J, MaxJ, AccDP)
  end, InitialDP, IndicesJ),
  maps:get(N - 1, FinalDP, -1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_jumps(nums :: [integer], target :: integer) :: integer
  def maximum_jumps(nums, target) do
    n = length(nums)
    nums_tuple = List.to_tuple(nums)

    dp_final =
      Enum.reduce(1..(n - 1), %{0 => 0}, fn j, acc_dp ->
        val_j = elem(nums_tuple, j)

        max_j =
          Enum.reduce(0..(j - 1), -1, fn i, current_max ->
            dp_i = Map.get(acc_dp, i, -1)
            val_i = elem(nums_tuple, i)

            if dp_i != -1 and abs(val_j - val_i) <= target do
              max(current_max, dp_i + 1)
            else
              current_max
            end
          end)

        Map.put(acc_dp, j, max_j)
      end)

    Map.get(dp_final, n - 1, -1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2) where n is the number of elements in the nums array. This complexity arises from the nested loop structure where, for each index j, we iterate through all previous indices i to check for valid jump conditions.
- **Space Complexity:** O(n) where n is the number of elements in the nums array. This space is required to store the dp array of size n, which tracks the maximum number of jumps to reach each index.
