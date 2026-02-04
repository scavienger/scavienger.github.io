---
layout: post
title: "Trionic Array II"
date: 2026-02-04 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/trionic-array-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxSumTrionic(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        long long INF = 4e15;\n        vector<long\
        \ long> dp1(n, -INF), dp2(n, -INF), dp3(n, -INF);\n        long long maxSum\
        \ = -INF;\n        for (int i = 1; i < n; ++i) {\n            if (nums[i] >\
        \ nums[i - 1]) {\n                dp1[i] = max((long long)nums[i - 1] + nums[i],\
        \ dp1[i - 1] + nums[i]);\n                dp3[i] = max(dp2[i - 1] + nums[i],\
        \ dp3[i - 1] + nums[i]);\n            } else if (nums[i] < nums[i - 1]) {\n\
        \                dp2[i] = max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i]);\n\
        \            }\n            if (dp3[i] > maxSum) maxSum = dp3[i];\n        }\n\
        \        return maxSum;\n    }\n};"
      java: "class Solution {\n    public long maxSumTrionic(int[] nums) {\n       \
        \ int n = nums.length;\n        long INF = 4000000000000000L;\n        long[]\
        \ dp1 = new long[n];\n        long[] dp2 = new long[n];\n        long[] dp3\
        \ = new long[n];\n        java.util.Arrays.fill(dp1, -INF);\n        java.util.Arrays.fill(dp2,\
        \ -INF);\n        java.util.Arrays.fill(dp3, -INF);\n        long maxSum = -INF;\n\
        \        for (int i = 1; i < n; i++) {\n            if (nums[i] > nums[i - 1])\
        \ {\n                dp1[i] = Math.max((long) nums[i - 1] + nums[i], dp1[i -\
        \ 1] + nums[i]);\n                dp3[i] = Math.max(dp2[i - 1] + nums[i], dp3[i\
        \ - 1] + nums[i]);\n            } else if (nums[i] < nums[i - 1]) {\n      \
        \          dp2[i] = Math.max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i]);\n\
        \            }\n            if (dp3[i] > maxSum) maxSum = dp3[i];\n        }\n\
        \        return maxSum;\n    }\n}"
      python: "class Solution(object):\n    def maxSumTrionic(self, nums):\n       \
        \ \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\
        \n        n = len(nums)\n        inf = float('inf')\n        dp1 = [-inf] *\
        \ n\n        dp2 = [-inf] * n\n        dp3 = [-inf] * n\n        for i in range(1,\
        \ n):\n            if nums[i] > nums[i - 1]:\n                dp1[i] = max(nums[i\
        \ - 1] + nums[i], dp1[i - 1] + nums[i])\n                dp3[i] = max(dp2[i\
        \ - 1] + nums[i], dp3[i - 1] + nums[i])\n            elif nums[i] < nums[i -\
        \ 1]:\n                dp2[i] = max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i])\n\
        \        return int(max(dp3))"
      python3: "class Solution:\n    def maxSumTrionic(self, nums: List[int]) -> int:\n\
        \        n = len(nums)\n        inf = float('inf')\n        dp1 = [-inf] * n\n\
        \        dp2 = [-inf] * n\n        dp3 = [-inf] * n\n        for i in range(1,\
        \ n):\n            if nums[i] > nums[i - 1]:\n                dp1[i] = max(nums[i\
        \ - 1] + nums[i], dp1[i - 1] + nums[i])\n                dp3[i] = max(dp2[i\
        \ - 1] + nums[i], dp3[i - 1] + nums[i])\n            elif nums[i] < nums[i -\
        \ 1]:\n                dp2[i] = max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i])\n\
        \        return int(max(dp3))"
      c: "#include <stdlib.h>\n#include <limits.h>\n\nlong long max_val(long long a,\
        \ long long b) {\n    return a > b ? a : b;\n}\n\nlong long maxSumTrionic(int*\
        \ nums, int numsSize) {\n    if (numsSize < 4) return 0;\n    long long INF\
        \ = 4000000000000000LL;\n    long long* dp1 = (long long*)malloc(numsSize *\
        \ sizeof(long long));\n    long long* dp2 = (long long*)malloc(numsSize * sizeof(long\
        \ long));\n    long long* dp3 = (long long*)malloc(numsSize * sizeof(long long));\n\
        \    for (int i = 0; i < numsSize; i++) {\n        dp1[i] = dp2[i] = dp3[i]\
        \ = -INF;\n    }\n    long long res = -INF;\n    for (int i = 1; i < numsSize;\
        \ i++) {\n        if (nums[i] > nums[i - 1]) {\n            dp1[i] = max_val((long\
        \ long)nums[i - 1] + nums[i], dp1[i - 1] + nums[i]);\n            dp3[i] = max_val(dp2[i\
        \ - 1] + nums[i], dp3[i - 1] + nums[i]);\n        } else if (nums[i] < nums[i\
        \ - 1]) {\n            dp2[i] = max_val(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i]);\n\
        \        }\n        if (dp3[i] > res) res = dp3[i];\n    }\n    free(dp1); free(dp2);\
        \ free(dp3);\n    return res;\n}"
      csharp: "public class Solution {\n    public long MaxSumTrionic(int[] nums) {\n\
        \        int n = nums.Length;\n        long INF = 4000000000000000L;\n     \
        \   long[] dp1 = new long[n];\n        long[] dp2 = new long[n];\n        long[]\
        \ dp3 = new long[n];\n        for (int i = 0; i < n; i++) {\n            dp1[i]\
        \ = dp2[i] = dp3[i] = -INF;\n        }\n        long maxSum = -INF;\n      \
        \  for (int i = 1; i < n; i++) {\n            if (nums[i] > nums[i - 1]) {\n\
        \                dp1[i] = System.Math.Max((long)nums[i - 1] + nums[i], dp1[i\
        \ - 1] + nums[i]);\n                dp3[i] = System.Math.Max(dp2[i - 1] + nums[i],\
        \ dp3[i - 1] + nums[i]);\n            } else if (nums[i] < nums[i - 1]) {\n\
        \                dp2[i] = System.Math.Max(dp1[i - 1] + nums[i], dp2[i - 1] +\
        \ nums[i]);\n            }\n            if (dp3[i] > maxSum) maxSum = dp3[i];\n\
        \        }\n        return maxSum;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maxSumTrionic\
        \ = function(nums) {\n    const n = nums.length;\n    const dp1 = new Array(n).fill(-Infinity);\n\
        \    const dp2 = new Array(n).fill(-Infinity);\n    const dp3 = new Array(n).fill(-Infinity);\n\
        \    let maxSum = -Infinity;\n    for (let i = 1; i < n; i++) {\n        if\
        \ (nums[i] > nums[i - 1]) {\n            dp1[i] = Math.max(nums[i - 1] + nums[i],\
        \ dp1[i - 1] + nums[i]);\n            dp3[i] = Math.max(dp2[i - 1] + nums[i],\
        \ dp3[i - 1] + nums[i]);\n        } else if (nums[i] < nums[i - 1]) {\n    \
        \        dp2[i] = Math.max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i]);\n  \
        \      }\n        if (dp3[i] > maxSum) maxSum = dp3[i];\n    }\n    return maxSum;\n\
        };"
      typescript: "function maxSumTrionic(nums: number[]): number {\n  const n = nums.length;\n\
        \  const INF = 1000000000000000;\n  let dp1 = -INF, dp2 = -INF, dp3 = -INF;\n\
        \  let ans = -INF;\n\n  for (let i = 1; i < n; i++) {\n    const v = nums[i];\n\
        \    const pv = nums[i - 1];\n    let n1 = -INF, n2 = -INF, n3 = -INF;\n\n \
        \   if (v > pv) {\n      n1 = Math.max(pv + v, dp1 + v);\n      n3 = Math.max(dp2\
        \ + v, dp3 + v);\n    } else if (v < pv) {\n      n2 = Math.max(dp1 + v, dp2\
        \ + v);\n    }\n\n    dp1 = n1;\n    dp2 = n2;\n    dp3 = n3;\n    if (dp3 >\
        \ ans) ans = dp3;\n  }\n  return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function maxSumTrionic($nums) {\n        $n = count($nums);\n\
        \        $inf = 1000000000000000;\n        $dp1 = -$inf;\n        $dp2 = -$inf;\n\
        \        $dp3 = -$inf;\n        $ans = -$inf;\n\n        for ($i = 1; $i < $n;\
        \ $i++) {\n            $v = $nums[$i];\n            $pv = $nums[$i - 1];\n \
        \           $n1 = -$inf;\n            $n2 = -$inf;\n            $n3 = -$inf;\n\
        \n            if ($v > $pv) {\n                $n1 = max($pv + $v, $dp1 + $v);\n\
        \                $n3 = max($dp2 + $v, $dp3 + $v);\n            } else if ($v\
        \ < $pv) {\n                $n2 = max($dp1 + $v, $dp2 + $v);\n            }\n\
        \n            $dp1 = $n1;\n            $dp2 = $n2;\n            $dp3 = $n3;\n\
        \            if ($dp3 > $ans) {\n                $ans = $dp3;\n            }\n\
        \        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func maxSumTrionic(_ nums: [Int]) -> Int {\n   \
        \     let n = nums.count\n        let inf = 1_000_000_000_000_000\n        var\
        \ dp1 = -inf, dp2 = -inf, dp3 = -inf\n        var ans = -inf\n\n        for\
        \ i in 1..<n {\n            let v = nums[i]\n            let pv = nums[i - 1]\n\
        \            var n1 = -inf, n2 = -inf, n3 = -inf\n\n            if v > pv {\n\
        \                n1 = max(pv + v, dp1 + v)\n                n3 = max(dp2 + v,\
        \ dp3 + v)\n            } else if v < pv {\n                n2 = max(dp1 + v,\
        \ dp2 + v)\n            }\n\n            dp1 = n1\n            dp2 = n2\n  \
        \          dp3 = n3\n            if dp3 > ans { ans = dp3 }\n        }\n   \
        \     return ans\n    }\n}"
      kotlin: "import kotlin.math.max\n\nclass Solution {\n    fun maxSumTrionic(nums:\
        \ IntArray): Long {\n        val n = nums.size\n        val inf = 1_000_000_000_000_000L\n\
        \        var dp1 = -inf\n        var dp2 = -inf\n        var dp3 = -inf\n  \
        \      var ans = -inf\n\n        for (i in 1 until n) {\n            val v =\
        \ nums[i].toLong()\n            val pv = nums[i - 1].toLong()\n            var\
        \ n1 = -inf\n            var n2 = -inf\n            var n3 = -inf\n\n      \
        \      if (v > pv) {\n                n1 = max(pv + v, dp1 + v)\n          \
        \      n3 = max(dp2 + v, dp3 + v)\n            } else if (v < pv) {\n      \
        \          n2 = max(dp1 + v, dp2 + v)\n            }\n\n            dp1 = n1\n\
        \            dp2 = n2\n            dp3 = n3\n            if (dp3 > ans) {\n\
        \                ans = dp3\n            }\n        }\n        return ans\n \
        \   }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maxSumTrionic(List<int>\
        \ nums) {\n    int n = nums.length;\n    int inf = 1000000000000000;\n    int\
        \ dp1 = -inf, dp2 = -inf, dp3 = -inf;\n    int ans = -inf;\n\n    for (int i\
        \ = 1; i < n; i++) {\n      int v = nums[i];\n      int pv = nums[i - 1];\n\
        \      int n1 = -inf, n2 = -inf, n3 = -inf;\n\n      if (v > pv) {\n       \
        \ n1 = max(pv + v, dp1 + v);\n        n3 = max(dp2 + v, dp3 + v);\n      } else\
        \ if (v < pv) {\n        n2 = max(dp1 + v, dp2 + v);\n      }\n\n      dp1 =\
        \ n1;\n      dp2 = n2;\n      dp3 = n3;\n      if (dp3 > ans) ans = dp3;\n \
        \   }\n    return ans;\n  }\n}"
      go: "func maxSumTrionic(nums []int) int64 {\n\tn := len(nums)\n\tconst INF int64\
        \ = 1000000000000000\n\tdp1, dp2, dp3 := -INF, -INF, -INF\n\tans := -INF\n\t\
        for i := 1; i < n; i++ {\n\t\tvar n1, n2, n3 int64 = -INF, -INF, -INF\n\t\t\
        v := int64(nums[i])\n\t\tpv := int64(nums[i-1])\n\t\tif v > pv {\n\t\t\tn1 =\
        \ pv + v\n\t\t\tif dp1 != -INF && dp1+v > n1 {\n\t\t\t\tn1 = dp1 + v\n\t\t\t\
        }\n\t\t\tif dp2 != -INF {\n\t\t\t\tn3 = dp2 + v\n\t\t\t}\n\t\t\tif dp3 != -INF\
        \ && dp3+v > n3 {\n\t\t\t\tn3 = dp3 + v\n\t\t\t}\n\t\t} else if v < pv {\n\t\
        \t\tif dp1 != -INF {\n\t\t\t\tn2 = dp1 + v\n\t\t\t}\n\t\t\tif dp2 != -INF &&\
        \ dp2+v > n2 {\n\t\t\t\tn2 = dp2 + v\n\t\t\t}\n\t\t}\n\t\tdp1, dp2, dp3 = n1,\
        \ n2, n3\n\t\tif dp3 > ans {\n\t\t\tans = dp3\n\t\t}\n\t}\n\treturn ans\n}"
      ruby: "def max_sum_trionic(nums)\n  inf = 10**17\n  dp0 = nums[0]\n  dp1 = -inf\n\
        \  dp2 = -inf\n  dp3 = -inf\n  max_val = -inf\n  (1...nums.length).each do |i|\n\
        \    cur = nums[i]\n    prev = nums[i-1]\n    if cur > prev\n      n1 = [dp1,\
        \ dp0].max + cur\n      n3 = [dp3, dp2].max + cur\n      dp0 = [dp0 + cur, cur].max\n\
        \      dp1 = n1\n      dp2 = -inf\n      dp3 = n3\n    elsif cur < prev\n  \
        \    dp2 = [dp2, dp1].max + cur\n      dp0 = cur\n      dp1 = -inf\n      dp3\
        \ = -inf\n    else\n      dp0 = cur\n      dp1 = -inf\n      dp2 = -inf\n  \
        \    dp3 = -inf\n    end\n    max_val = dp3 if dp3 > max_val\n  end\n  max_val\n\
        end"
      scala: "object Solution {\n    def maxSumTrionic(nums: Array[Int]): Long = {\n\
        \        val inf = 100000000000000000L\n        var dp0 = nums(0).toLong\n \
        \       var dp1 = -inf\n        var dp2 = -inf\n        var dp3 = -inf\n   \
        \     var maxVal = -inf\n        for (i <- 1 until nums.length) {\n        \
        \    val cur = nums(i).toLong\n            val prev = nums(i - 1).toLong\n \
        \           if (cur > prev) {\n                val n1 = Math.max(dp1, dp0) +\
        \ cur\n                val n3 = Math.max(dp3, dp2) + cur\n                dp0\
        \ = Math.max(dp0 + cur, cur)\n                dp1 = n1\n                dp2\
        \ = -inf\n                dp3 = n3\n            } else if (cur < prev) {\n \
        \               dp2 = Math.max(dp2, dp1) + cur\n                dp0 = cur\n\
        \                dp1 = -inf\n                dp3 = -inf\n            } else\
        \ {\n                dp0 = cur\n                dp1 = -inf\n               \
        \ dp2 = -inf\n                dp3 = -inf\n            }\n            maxVal\
        \ = Math.max(maxVal, dp3)\n        }\n        maxVal\n    }\n}"
      rust: "impl Solution {\n    pub fn max_sum_trionic(nums: Vec<i32>) -> i64 {\n\
        \        let inf: i64 = 100_000_000_000_000_000;\n        let mut dp0: i64 =\
        \ nums[0] as i64;\n        let mut dp1: i64 = -inf;\n        let mut dp2: i64\
        \ = -inf;\n        let mut dp3: i64 = -inf;\n        let mut max_val: i64 =\
        \ -inf;\n        for i in 1..nums.len() {\n            let cur = nums[i] as\
        \ i64;\n            let prev = nums[i-1] as i64;\n            if cur > prev\
        \ {\n                let n1 = dp1.max(dp0) + cur;\n                let n3 =\
        \ dp3.max(dp2) + cur;\n                dp0 = (dp0 + cur).max(cur);\n       \
        \         dp1 = n1;\n                dp2 = -inf;\n                dp3 = n3;\n\
        \            } else if cur < prev {\n                dp2 = dp2.max(dp1) + cur;\n\
        \                dp0 = cur;\n                dp1 = -inf;\n                dp3\
        \ = -inf;\n            } else {\n                dp0 = cur;\n              \
        \  dp1 = -inf;\n                dp2 = -inf;\n                dp3 = -inf;\n \
        \           }\n            max_val = max_val.max(dp3);\n        }\n        max_val\n\
        \    }\n}"
      racket: "(define/contract (max-sum-trionic nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([inf 100000000000000000]\n         [h (car nums)]\n\
        \         [t (cdr nums)])\n    (let loop ([lst t] [prev h] [dp0 h] [dp1 (- inf)]\
        \ [dp2 (- inf)] [dp3 (- inf)] [max-v (- inf)])\n      (if (null? lst)\n    \
        \      max-v\n          (let* ([cur (car lst)]\n                 [n0 (if (>\
        \ cur prev) (max (+ dp0 cur) cur) cur)]\n                 [n1 (if (> cur prev)\
        \ (+ (max dp1 dp0) cur) (- inf))]\n                 [n2 (if (< cur prev) (+\
        \ (max dp2 dp1) cur) (- inf))]\n                 [n3 (if (> cur prev) (+ (max\
        \ dp3 dp2) cur) (- inf))])\n            (loop (cdr lst) cur n0 n1 n2 n3 (max\
        \ max-v n3)))))))"
      erlang: "-spec max_sum_trionic(Nums :: [integer()]) -> integer().\nmax_sum_trionic([H\
        \ | T]) ->\n  Inf = 100000000000000000,\n  {_, _, _, _, _, MaxSum} = lists:foldl(fun(Cur,\
        \ {Prev, Dp0, Dp1, Dp2, Dp3, Acc}) ->\n    {Next0, Next1, Next2, Next3} = if\n\
        \      Cur > Prev ->\n        {max(Dp0 + Cur, Cur), max(Dp1, Dp0) + Cur, -Inf,\
        \ max(Dp3, Dp2) + Cur};\n      Cur < Prev ->\n        {Cur, -Inf, max(Dp2, Dp1)\
        \ + Cur, -Inf};\n      true ->\n        {Cur, -Inf, -Inf, -Inf}\n    end,\n\
        \    {Cur, Next0, Next1, Next2, Next3, max(Acc, Next3)}\n  end, {H, H, -Inf,\
        \ -Inf, -Inf, -Inf}, T),\n  MaxSum."
      elixir: "defmodule Solution do\n  @spec max_sum_trionic(nums :: [integer]) ::\
        \ integer\n  def max_sum_trionic(nums) do\n    inf = 100_000_000_000_000_000\n\
        \    [h | t] = nums\n    {_prev, _dp0, _dp1, _dp2, _dp3, max_val} = \n     \
        \ Enum.reduce(t, {h, h, -inf, -inf, -inf, -inf}, fn cur, {prev, dp0, dp1, dp2,\
        \ dp3, acc} ->\n        {next0, next1, next2, next3} = \n          cond do\n\
        \            cur > prev ->\n              {max(dp0 + cur, cur), max(dp1, dp0)\
        \ + cur, -inf, max(dp3, dp2) + cur}\n            cur < prev ->\n           \
        \   {cur, -inf, max(dp2, dp1) + cur, -inf}\n            true ->\n          \
        \    {cur, -inf, -inf, -inf}\n          end\n        {cur, next0, next1, next2,\
        \ next3, max(acc, next3)}\n      end)\n    max_val\n  end\nend"
    approach: 'We use dynamic programming to find the maximum trionic subarray sum by
      tracking three distinct phases: strictly increasing (Phase 1), strictly decreasing
      (Phase 2), and strictly increasing (Phase 3). For each index $i$ in the array,
      we define $dp1[i]$ as the maximum sum of a strictly increasing subarray ending
      at $i$, $dp2[i]$ as the maximum sum of a subarray consisting of Phase 1 followed
      by Phase 2 ending at $i$, and $dp3[i]$ as the maximum sum of a complete trionic
      subarray ending at $i$. These states transition based on the monotonic relationship
      between $nums[i]$ and $nums[i-1]$.


      Phase 1 ($dp1$) is initiated or extended whenever $nums[i] > nums[i-1]$. Phase
      2 ($dp2$) is transitioned from Phase 1 or extended whenever $nums[i] < nums[i-1]$.
      Phase 3 ($dp3$) is transitioned from Phase 2 or extended whenever $nums[i] > nums[i-1]$.
      This approach ensures the index requirements $l < p < q < r$ because each transition
      requires at least one additional element to be added to the previous valid phase.
      The strictly monotonic conditions ensure that any equality $nums[i] == nums[i-1]$
      or a break in the required direction for a phase resets the corresponding DP states,
      and the final result is the maximum value found in $dp3$ across all indices.'
    time_complexity: O(n) where n is the length of the input array. We iterate through
      the array once, and each update for the three DP states takes constant time.
    space_complexity: O(n) to store three DP arrays of size n. This could be optimized
      to O(1) by only keeping track of the previous state, but $O(n)$ is efficient and
      fits within memory constraints.
    elapsed_time: 356.9959602355957
    model: gemini-3-flash-preview
    generated_at: '2026-02-04 05:24:02 '
---

## Problem #3640: Trionic Array II

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming

## Problem Description

<p data-end="191" data-start="0">You are given an integer array <code data-end="61" data-start="55">nums</code> of length <code data-end="75" data-start="72">n</code>.</p>

<p data-end="191" data-start="0">A <strong data-end="99" data-is-only-node="" data-start="79">trionic subarray</strong> is a contiguous subarray <code data-end="136" data-start="125">nums[l...r]</code> (with <code data-end="158" data-start="143">0 &lt;= l &lt; r &lt; n</code>) for which there exist indices <code>l &lt; p &lt; q &lt; r</code> such that:</p>

<ul>
	<li data-end="267" data-start="230"><code data-end="241" data-start="230">nums[l...p]</code> is <strong>strictly</strong> increasing,</li>
	<li data-end="307" data-start="270"><code data-end="281" data-start="270">nums[p...q]</code> is <strong>strictly</strong> decreasing,</li>
	<li data-end="347" data-start="310"><code data-end="321" data-start="310">nums[q...r]</code> is <strong>strictly</strong> increasing.</li>
</ul>

<p data-end="609" data-is-last-node="" data-is-only-node="" data-start="349">Return the <strong>maximum</strong> sum of any trionic subarray in <code data-end="417" data-start="411">nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,-2,-1,-3,0,2,-1]</span></p>

<p><strong>Output:</strong> <span class="example-io">-4</span></p>

<p><strong>Explanation:</strong></p>

<p data-end="129" data-start="72">Pick <code data-end="99" data-start="92">l = 1</code>, <code data-end="108" data-start="101">p = 2</code>, <code data-end="117" data-start="110">q = 3</code>, <code data-end="126" data-start="119">r = 5</code>:</p>

<ul>
	<li data-end="203" data-start="132"><code data-end="166" data-start="132">nums[l...p] = nums[1...2] = [-2, -1]</code> is strictly increasing (<code data-end="200" data-start="191">-2 &lt; -1</code>).</li>
	<li data-end="277" data-start="206"><code data-end="240" data-start="206">nums[p...q] = nums[2...3] = [-1, -3]</code> is strictly decreasing (<code data-end="274" data-start="265">-1 &gt; -3</code>)</li>
	<li data-end="396" data-start="280"><code data-end="316" data-start="280">nums[q...r] = nums[3...5] = [-3, 0, 2]</code> is strictly increasing (<code data-end="353" data-start="341">-3 &lt; 0 &lt; 2</code>).</li>
	<li data-end="396" data-start="280">Sum = <code>(-2) + (-1) + (-3) + 0 + 2 = -4</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,2,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<p data-end="519" data-start="462">Pick <code data-end="489" data-start="482">l = 0</code>, <code data-end="498" data-start="491">p = 1</code>, <code data-end="507" data-start="500">q = 2</code>, <code data-end="516" data-start="509">r = 3</code>:</p>

<ul>
	<li data-end="589" data-start="522"><code data-end="554" data-start="522">nums[l...p] = nums[0...1] = [1, 4]</code> is strictly increasing (<code data-end="586" data-start="579">1 &lt; 4</code>).</li>
	<li data-end="659" data-start="592"><code data-end="624" data-start="592">nums[p...q] = nums[1...2] = [4, 2]</code> is strictly decreasing (<code data-end="656" data-start="649">4 &gt; 2</code>).</li>
	<li data-end="754" data-is-last-node="" data-start="662"><code data-end="694" data-start="662">nums[q...r] = nums[2...3] = [2, 7]</code> is strictly increasing (<code data-end="726" data-start="719">2 &lt; 7</code>).</li>
	<li data-end="754" data-is-last-node="" data-start="662">Sum = <code>1 + 4 + 2 + 7 = 14</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="883" data-start="851"><code data-end="881" data-start="851">4 &lt;= n = nums.length &lt;= 10<sup>5</sup></code></li>
	<li data-end="914" data-start="886"><code data-end="912" data-start="886">-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li data-end="978" data-is-last-node="" data-start="917">It is guaranteed that at least one trionic subarray exists.</li>
</ul>


## Hints

1. Use dynamic programming

2. Let four arrays `dp0...dp3` where `dpk[i]` is the max sum of a subarray ending at `i` after finishing `k` of the four phases (start -> inc -> dec -> inc)

3. Process each `i>0`

4. If `nums[i] > nums[i‑1]`, set `dp1[i]=max(dp1[i‑1]+nums[i], dp0[i‑1]+nums[i])`, `dp3[i]=max(dp3[i‑1]+nums[i], dp2[i‑1]+nums[i])`

5. If `nums[i] < nums[i‑1]`, set `dp2[i]=max(dp2[i‑1]+nums[i], dp1[i‑1]+nums[i])`

6. Always carry over `dp0[i]=dp0[i‑1]+nums[i]` when `nums[i]>nums[i‑1]`

7. Return the maximum value in `dp3`

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

We use dynamic programming to find the maximum trionic subarray sum by tracking three distinct phases: strictly increasing (Phase 1), strictly decreasing (Phase 2), and strictly increasing (Phase 3). For each index $i$ in the array, we define $dp1[i]$ as the maximum sum of a strictly increasing subarray ending at $i$, $dp2[i]$ as the maximum sum of a subarray consisting of Phase 1 followed by Phase 2 ending at $i$, and $dp3[i]$ as the maximum sum of a complete trionic subarray ending at $i$. These states transition based on the monotonic relationship between $nums[i]$ and $nums[i-1]$.

Phase 1 ($dp1$) is initiated or extended whenever $nums[i] > nums[i-1]$. Phase 2 ($dp2$) is transitioned from Phase 1 or extended whenever $nums[i] < nums[i-1]$. Phase 3 ($dp3$) is transitioned from Phase 2 or extended whenever $nums[i] > nums[i-1]$. This approach ensures the index requirements $l < p < q < r$ because each transition requires at least one additional element to be added to the previous valid phase. The strictly monotonic conditions ensure that any equality $nums[i] == nums[i-1]$ or a break in the required direction for a phase resets the corresponding DP states, and the final result is the maximum value found in $dp3$ across all indices.

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
    long long maxSumTrionic(vector<int>& nums) {
        int n = nums.size();
        long long INF = 4e15;
        vector<long long> dp1(n, -INF), dp2(n, -INF), dp3(n, -INF);
        long long maxSum = -INF;
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i - 1]) {
                dp1[i] = max((long long)nums[i - 1] + nums[i], dp1[i - 1] + nums[i]);
                dp3[i] = max(dp2[i - 1] + nums[i], dp3[i - 1] + nums[i]);
            } else if (nums[i] < nums[i - 1]) {
                dp2[i] = max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i]);
            }
            if (dp3[i] > maxSum) maxSum = dp3[i];
        }
        return maxSum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long maxSumTrionic(int[] nums) {
        int n = nums.length;
        long INF = 4000000000000000L;
        long[] dp1 = new long[n];
        long[] dp2 = new long[n];
        long[] dp3 = new long[n];
        java.util.Arrays.fill(dp1, -INF);
        java.util.Arrays.fill(dp2, -INF);
        java.util.Arrays.fill(dp3, -INF);
        long maxSum = -INF;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                dp1[i] = Math.max((long) nums[i - 1] + nums[i], dp1[i - 1] + nums[i]);
                dp3[i] = Math.max(dp2[i - 1] + nums[i], dp3[i - 1] + nums[i]);
            } else if (nums[i] < nums[i - 1]) {
                dp2[i] = Math.max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i]);
            }
            if (dp3[i] > maxSum) maxSum = dp3[i];
        }
        return maxSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        inf = float('inf')
        dp1 = [-inf] * n
        dp2 = [-inf] * n
        dp3 = [-inf] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp1[i] = max(nums[i - 1] + nums[i], dp1[i - 1] + nums[i])
                dp3[i] = max(dp2[i - 1] + nums[i], dp3[i - 1] + nums[i])
            elif nums[i] < nums[i - 1]:
                dp2[i] = max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i])
        return int(max(dp3))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        inf = float('inf')
        dp1 = [-inf] * n
        dp2 = [-inf] * n
        dp3 = [-inf] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp1[i] = max(nums[i - 1] + nums[i], dp1[i - 1] + nums[i])
                dp3[i] = max(dp2[i - 1] + nums[i], dp3[i - 1] + nums[i])
            elif nums[i] < nums[i - 1]:
                dp2[i] = max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i])
        return int(max(dp3))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <limits.h>

long long max_val(long long a, long long b) {
    return a > b ? a : b;
}

long long maxSumTrionic(int* nums, int numsSize) {
    if (numsSize < 4) return 0;
    long long INF = 4000000000000000LL;
    long long* dp1 = (long long*)malloc(numsSize * sizeof(long long));
    long long* dp2 = (long long*)malloc(numsSize * sizeof(long long));
    long long* dp3 = (long long*)malloc(numsSize * sizeof(long long));
    for (int i = 0; i < numsSize; i++) {
        dp1[i] = dp2[i] = dp3[i] = -INF;
    }
    long long res = -INF;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > nums[i - 1]) {
            dp1[i] = max_val((long long)nums[i - 1] + nums[i], dp1[i - 1] + nums[i]);
            dp3[i] = max_val(dp2[i - 1] + nums[i], dp3[i - 1] + nums[i]);
        } else if (nums[i] < nums[i - 1]) {
            dp2[i] = max_val(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i]);
        }
        if (dp3[i] > res) res = dp3[i];
    }
    free(dp1); free(dp2); free(dp3);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MaxSumTrionic(int[] nums) {
        int n = nums.Length;
        long INF = 4000000000000000L;
        long[] dp1 = new long[n];
        long[] dp2 = new long[n];
        long[] dp3 = new long[n];
        for (int i = 0; i < n; i++) {
            dp1[i] = dp2[i] = dp3[i] = -INF;
        }
        long maxSum = -INF;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                dp1[i] = System.Math.Max((long)nums[i - 1] + nums[i], dp1[i - 1] + nums[i]);
                dp3[i] = System.Math.Max(dp2[i - 1] + nums[i], dp3[i - 1] + nums[i]);
            } else if (nums[i] < nums[i - 1]) {
                dp2[i] = System.Math.Max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i]);
            }
            if (dp3[i] > maxSum) maxSum = dp3[i];
        }
        return maxSum;
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
 * @return {number}
 */
var maxSumTrionic = function(nums) {
    const n = nums.length;
    const dp1 = new Array(n).fill(-Infinity);
    const dp2 = new Array(n).fill(-Infinity);
    const dp3 = new Array(n).fill(-Infinity);
    let maxSum = -Infinity;
    for (let i = 1; i < n; i++) {
        if (nums[i] > nums[i - 1]) {
            dp1[i] = Math.max(nums[i - 1] + nums[i], dp1[i - 1] + nums[i]);
            dp3[i] = Math.max(dp2[i - 1] + nums[i], dp3[i - 1] + nums[i]);
        } else if (nums[i] < nums[i - 1]) {
            dp2[i] = Math.max(dp1[i - 1] + nums[i], dp2[i - 1] + nums[i]);
        }
        if (dp3[i] > maxSum) maxSum = dp3[i];
    }
    return maxSum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSumTrionic(nums: number[]): number {
  const n = nums.length;
  const INF = 1000000000000000;
  let dp1 = -INF, dp2 = -INF, dp3 = -INF;
  let ans = -INF;

  for (let i = 1; i < n; i++) {
    const v = nums[i];
    const pv = nums[i - 1];
    let n1 = -INF, n2 = -INF, n3 = -INF;

    if (v > pv) {
      n1 = Math.max(pv + v, dp1 + v);
      n3 = Math.max(dp2 + v, dp3 + v);
    } else if (v < pv) {
      n2 = Math.max(dp1 + v, dp2 + v);
    }

    dp1 = n1;
    dp2 = n2;
    dp3 = n3;
    if (dp3 > ans) ans = dp3;
  }
  return ans;
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
     * @return Integer
     */
    function maxSumTrionic($nums) {
        $n = count($nums);
        $inf = 1000000000000000;
        $dp1 = -$inf;
        $dp2 = -$inf;
        $dp3 = -$inf;
        $ans = -$inf;

        for ($i = 1; $i < $n; $i++) {
            $v = $nums[$i];
            $pv = $nums[$i - 1];
            $n1 = -$inf;
            $n2 = -$inf;
            $n3 = -$inf;

            if ($v > $pv) {
                $n1 = max($pv + $v, $dp1 + $v);
                $n3 = max($dp2 + $v, $dp3 + $v);
            } else if ($v < $pv) {
                $n2 = max($dp1 + $v, $dp2 + $v);
            }

            $dp1 = $n1;
            $dp2 = $n2;
            $dp3 = $n3;
            if ($dp3 > $ans) {
                $ans = $dp3;
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
    func maxSumTrionic(_ nums: [Int]) -> Int {
        let n = nums.count
        let inf = 1_000_000_000_000_000
        var dp1 = -inf, dp2 = -inf, dp3 = -inf
        var ans = -inf

        for i in 1..<n {
            let v = nums[i]
            let pv = nums[i - 1]
            var n1 = -inf, n2 = -inf, n3 = -inf

            if v > pv {
                n1 = max(pv + v, dp1 + v)
                n3 = max(dp2 + v, dp3 + v)
            } else if v < pv {
                n2 = max(dp1 + v, dp2 + v)
            }

            dp1 = n1
            dp2 = n2
            dp3 = n3
            if dp3 > ans { ans = dp3 }
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
import kotlin.math.max

class Solution {
    fun maxSumTrionic(nums: IntArray): Long {
        val n = nums.size
        val inf = 1_000_000_000_000_000L
        var dp1 = -inf
        var dp2 = -inf
        var dp3 = -inf
        var ans = -inf

        for (i in 1 until n) {
            val v = nums[i].toLong()
            val pv = nums[i - 1].toLong()
            var n1 = -inf
            var n2 = -inf
            var n3 = -inf

            if (v > pv) {
                n1 = max(pv + v, dp1 + v)
                n3 = max(dp2 + v, dp3 + v)
            } else if (v < pv) {
                n2 = max(dp1 + v, dp2 + v)
            }

            dp1 = n1
            dp2 = n2
            dp3 = n3
            if (dp3 > ans) {
                ans = dp3
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
import 'dart:math';

class Solution {
  int maxSumTrionic(List<int> nums) {
    int n = nums.length;
    int inf = 1000000000000000;
    int dp1 = -inf, dp2 = -inf, dp3 = -inf;
    int ans = -inf;

    for (int i = 1; i < n; i++) {
      int v = nums[i];
      int pv = nums[i - 1];
      int n1 = -inf, n2 = -inf, n3 = -inf;

      if (v > pv) {
        n1 = max(pv + v, dp1 + v);
        n3 = max(dp2 + v, dp3 + v);
      } else if (v < pv) {
        n2 = max(dp1 + v, dp2 + v);
      }

      dp1 = n1;
      dp2 = n2;
      dp3 = n3;
      if (dp3 > ans) ans = dp3;
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
func maxSumTrionic(nums []int) int64 {
	n := len(nums)
	const INF int64 = 1000000000000000
	dp1, dp2, dp3 := -INF, -INF, -INF
	ans := -INF
	for i := 1; i < n; i++ {
		var n1, n2, n3 int64 = -INF, -INF, -INF
		v := int64(nums[i])
		pv := int64(nums[i-1])
		if v > pv {
			n1 = pv + v
			if dp1 != -INF && dp1+v > n1 {
				n1 = dp1 + v
			}
			if dp2 != -INF {
				n3 = dp2 + v
			}
			if dp3 != -INF && dp3+v > n3 {
				n3 = dp3 + v
			}
		} else if v < pv {
			if dp1 != -INF {
				n2 = dp1 + v
			}
			if dp2 != -INF && dp2+v > n2 {
				n2 = dp2 + v
			}
		}
		dp1, dp2, dp3 = n1, n2, n3
		if dp3 > ans {
			ans = dp3
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
def max_sum_trionic(nums)
  inf = 10**17
  dp0 = nums[0]
  dp1 = -inf
  dp2 = -inf
  dp3 = -inf
  max_val = -inf
  (1...nums.length).each do |i|
    cur = nums[i]
    prev = nums[i-1]
    if cur > prev
      n1 = [dp1, dp0].max + cur
      n3 = [dp3, dp2].max + cur
      dp0 = [dp0 + cur, cur].max
      dp1 = n1
      dp2 = -inf
      dp3 = n3
    elsif cur < prev
      dp2 = [dp2, dp1].max + cur
      dp0 = cur
      dp1 = -inf
      dp3 = -inf
    else
      dp0 = cur
      dp1 = -inf
      dp2 = -inf
      dp3 = -inf
    end
    max_val = dp3 if dp3 > max_val
  end
  max_val
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxSumTrionic(nums: Array[Int]): Long = {
        val inf = 100000000000000000L
        var dp0 = nums(0).toLong
        var dp1 = -inf
        var dp2 = -inf
        var dp3 = -inf
        var maxVal = -inf
        for (i <- 1 until nums.length) {
            val cur = nums(i).toLong
            val prev = nums(i - 1).toLong
            if (cur > prev) {
                val n1 = Math.max(dp1, dp0) + cur
                val n3 = Math.max(dp3, dp2) + cur
                dp0 = Math.max(dp0 + cur, cur)
                dp1 = n1
                dp2 = -inf
                dp3 = n3
            } else if (cur < prev) {
                dp2 = Math.max(dp2, dp1) + cur
                dp0 = cur
                dp1 = -inf
                dp3 = -inf
            } else {
                dp0 = cur
                dp1 = -inf
                dp2 = -inf
                dp3 = -inf
            }
            maxVal = Math.max(maxVal, dp3)
        }
        maxVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_sum_trionic(nums: Vec<i32>) -> i64 {
        let inf: i64 = 100_000_000_000_000_000;
        let mut dp0: i64 = nums[0] as i64;
        let mut dp1: i64 = -inf;
        let mut dp2: i64 = -inf;
        let mut dp3: i64 = -inf;
        let mut max_val: i64 = -inf;
        for i in 1..nums.len() {
            let cur = nums[i] as i64;
            let prev = nums[i-1] as i64;
            if cur > prev {
                let n1 = dp1.max(dp0) + cur;
                let n3 = dp3.max(dp2) + cur;
                dp0 = (dp0 + cur).max(cur);
                dp1 = n1;
                dp2 = -inf;
                dp3 = n3;
            } else if cur < prev {
                dp2 = dp2.max(dp1) + cur;
                dp0 = cur;
                dp1 = -inf;
                dp3 = -inf;
            } else {
                dp0 = cur;
                dp1 = -inf;
                dp2 = -inf;
                dp3 = -inf;
            }
            max_val = max_val.max(dp3);
        }
        max_val
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-sum-trionic nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([inf 100000000000000000]
         [h (car nums)]
         [t (cdr nums)])
    (let loop ([lst t] [prev h] [dp0 h] [dp1 (- inf)] [dp2 (- inf)] [dp3 (- inf)] [max-v (- inf)])
      (if (null? lst)
          max-v
          (let* ([cur (car lst)]
                 [n0 (if (> cur prev) (max (+ dp0 cur) cur) cur)]
                 [n1 (if (> cur prev) (+ (max dp1 dp0) cur) (- inf))]
                 [n2 (if (< cur prev) (+ (max dp2 dp1) cur) (- inf))]
                 [n3 (if (> cur prev) (+ (max dp3 dp2) cur) (- inf))])
            (loop (cdr lst) cur n0 n1 n2 n3 (max max-v n3)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_sum_trionic(Nums :: [integer()]) -> integer().
max_sum_trionic([H | T]) ->
  Inf = 100000000000000000,
  {_, _, _, _, _, MaxSum} = lists:foldl(fun(Cur, {Prev, Dp0, Dp1, Dp2, Dp3, Acc}) ->
    {Next0, Next1, Next2, Next3} = if
      Cur > Prev ->
        {max(Dp0 + Cur, Cur), max(Dp1, Dp0) + Cur, -Inf, max(Dp3, Dp2) + Cur};
      Cur < Prev ->
        {Cur, -Inf, max(Dp2, Dp1) + Cur, -Inf};
      true ->
        {Cur, -Inf, -Inf, -Inf}
    end,
    {Cur, Next0, Next1, Next2, Next3, max(Acc, Next3)}
  end, {H, H, -Inf, -Inf, -Inf, -Inf}, T),
  MaxSum.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_sum_trionic(nums :: [integer]) :: integer
  def max_sum_trionic(nums) do
    inf = 100_000_000_000_000_000
    [h | t] = nums
    {_prev, _dp0, _dp1, _dp2, _dp3, max_val} = 
      Enum.reduce(t, {h, h, -inf, -inf, -inf, -inf}, fn cur, {prev, dp0, dp1, dp2, dp3, acc} ->
        {next0, next1, next2, next3} = 
          cond do
            cur > prev ->
              {max(dp0 + cur, cur), max(dp1, dp0) + cur, -inf, max(dp3, dp2) + cur}
            cur < prev ->
              {cur, -inf, max(dp2, dp1) + cur, -inf}
            true ->
              {cur, -inf, -inf, -inf}
          end
        {cur, next0, next1, next2, next3, max(acc, next3)}
      end)
    max_val
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. We iterate through the array once, and each update for the three DP states takes constant time.
- **Space Complexity:** O(n) to store three DP arrays of size n. This could be optimized to O(1) by only keeping track of the previous state, but $O(n)$ is efficient and fits within memory constraints.
