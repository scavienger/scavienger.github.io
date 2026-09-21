---
layout: post
title: "Find X Value of Array I"
date: 2026-09-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-x-value-of-array-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<long long> resultArray(vector<int>&\
        \ nums, int k) {\n        int n = nums.size();\n        vector<long long> res(k,\
        \ 0);\n        vector<long long> dp(k, 0);\n\n        for (int i = 0; i < n;\
        \ ++i) {\n            vector<long long> next_dp(k, 0);\n            int v =\
        \ nums[i] % k;\n            for (int r = 0; r < k; ++r) {\n                if\
        \ (dp[r] > 0) {\n                    next_dp[(r * v) % k] += dp[r];\n      \
        \          }\n            }\n            next_dp[v]++;\n\n            for (int\
        \ r = 0; r < k; ++r) {\n                dp[r] = next_dp[r];\n              \
        \  res[r] += dp[r];\n            }\n        }\n\n        return res;\n    }\n\
        };"
      java: "class Solution {\n    public long[] resultArray(int[] nums, int k) {\n\
        \        int n = nums.length;\n        long[] res = new long[k];\n        long[]\
        \ dp = new long[k];\n\n        for (int i = 0; i < n; i++) {\n            long[]\
        \ nextDp = new long[k];\n            int v = nums[i] % k;\n            for (int\
        \ r = 0; r < k; r++) {\n                if (dp[r] > 0) {\n                 \
        \   nextDp[(r * v) % k] += dp[r];\n                }\n            }\n      \
        \      nextDp[v]++;\n\n            for (int r = 0; r < k; r++) {\n         \
        \       dp[r] = nextDp[r];\n                res[r] += dp[r];\n            }\n\
        \        }\n\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def resultArray(self, nums, k):\n      \
        \  \"\"\"\n        :type nums: List[int]\n        :type k: int\n        :rtype:\
        \ List[int]\n        \"\"\"\n        res = [0] * k\n        dp = [0] * k\n\n\
        \        for x in nums:\n            v = x % k\n            next_dp = [0] *\
        \ k\n            for r in range(k):\n                if dp[r] > 0:\n       \
        \             next_dp[(r * v) % k] += dp[r]\n            next_dp[v] += 1\n \
        \           dp = next_dp\n            for r in range(k):\n                res[r]\
        \ += dp[r]\n\n        return res"
      python3: "class Solution:\n    def resultArray(self, nums: List[int], k: int)\
        \ -> List[int]:\n        res = [0] * k\n        dp = [0] * k\n\n        for\
        \ x in nums:\n            v = x % k\n            next_dp = [0] * k\n       \
        \     for r in range(k):\n                if dp[r] > 0:\n                  \
        \  next_dp[(r * v) % k] += dp[r]\n            next_dp[v] += 1\n            dp\
        \ = next_dp\n            for r in range(k):\n                res[r] += dp[r]\n\
        \n        return res"
      c: "#include <stdlib.h>\n#include <string.h>\n\n/**\n * Note: The returned array\
        \ must be malloced, assume caller calls free().\n */\nlong long* resultArray(int*\
        \ nums, int numsSize, int k, int* returnSize) {\n    *returnSize = k;\n    long\
        \ long* res = (long long*)calloc(k, sizeof(long long));\n    long long dp[5]\
        \ = {0};\n    long long next_dp[5] = {0};\n\n    for (int i = 0; i < numsSize;\
        \ i++) {\n        int v = nums[i] % k;\n        memset(next_dp, 0, sizeof(next_dp));\n\
        \n        for (int r = 0; r < k; r++) {\n            if (dp[r] > 0) {\n    \
        \            next_dp[(r * v) % k] += dp[r];\n            }\n        }\n    \
        \    next_dp[v]++;\n\n        for (int r = 0; r < k; r++) {\n            dp[r]\
        \ = next_dp[r];\n            res[r] += dp[r];\n        }\n    }\n\n    return\
        \ res;\n}"
      csharp: "public class Solution {\n    public long[] ResultArray(int[] nums, int\
        \ k) {\n        long[] ans = new long[k];\n        long[] dp = new long[k];\n\
        \n        foreach (int num in nums) {\n            long[] nextDp = new long[k];\n\
        \            int val = num % k;\n\n            for (int r = 0; r < k; r++) {\n\
        \                if (dp[r] > 0) {\n                    nextDp[(r * val) % k]\
        \ += dp[r];\n                }\n            }\n\n            nextDp[val]++;\n\
        \n            for (int r = 0; r < k; r++) {\n                ans[r] += nextDp[r];\n\
        \            }\n            dp = nextDp;\n        }\n\n        return ans;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number[]}\n */\nvar resultArray = function(nums, k) {\n    let ans = new\
        \ Array(k).fill(0);\n    let dp = new Array(k).fill(0);\n\n    for (let i =\
        \ 0; i < nums.length; i++) {\n        let nextDp = new Array(k).fill(0);\n \
        \       let val = nums[i] % k;\n\n        for (let r = 0; r < k; r++) {\n  \
        \          if (dp[r] > 0) {\n                nextDp[(r * val) % k] += dp[r];\n\
        \            }\n        }\n\n        nextDp[val]++;\n\n        for (let r =\
        \ 0; r < k; r++) {\n            ans[r] += nextDp[r];\n        }\n        dp\
        \ = nextDp;\n    }\n\n    return ans;\n};"
      typescript: "function resultArray(nums: number[], k: number): number[] {\n   \
        \ let ans: number[] = new Array(k).fill(0);\n    let dp: number[] = new Array(k).fill(0);\n\
        \n    for (let i = 0; i < nums.length; i++) {\n        let nextDp: number[]\
        \ = new Array(k).fill(0);\n        let val = nums[i] % k;\n\n        for (let\
        \ r = 0; r < k; r++) {\n            if (dp[r] > 0) {\n                nextDp[(r\
        \ * val) % k] += dp[r];\n            }\n        }\n\n        nextDp[val]++;\n\
        \n        for (let r = 0; r < k; r++) {\n            ans[r] += nextDp[r];\n\
        \        }\n        dp = nextDp;\n    }\n\n    return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer[]\n     */\n    function resultArray($nums,\
        \ $k) {\n        $ans = array_fill(0, $k, 0);\n        $dp = array_fill(0, $k,\
        \ 0);\n\n        foreach ($nums as $num) {\n            $nextDp = array_fill(0,\
        \ $k, 0);\n            $val = $num % $k;\n\n            for ($r = 0; $r < $k;\
        \ $r++) {\n                if ($dp[$r] > 0) {\n                    $nextDp[($r\
        \ * $val) % $k] += $dp[$r];\n                }\n            }\n\n          \
        \  $nextDp[$val]++;\n\n            for ($r = 0; $r < $k; $r++) {\n         \
        \       $ans[$r] += $nextDp[$r];\n            }\n            $dp = $nextDp;\n\
        \        }\n\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func resultArray(_ nums: [Int], _ k: Int) -> [Int]\
        \ {\n        var ans = [Int](repeating: 0, count: k)\n        var dp = [Int](repeating:\
        \ 0, count: k)\n\n        for num in nums {\n            var nextDp = [Int](repeating:\
        \ 0, count: k)\n            let val = num % k\n\n            for r in 0..<k\
        \ {\n                if dp[r] > 0 {\n                    nextDp[(r * val) %\
        \ k] += dp[r]\n                }\n            }\n\n            nextDp[val] +=\
        \ 1\n\n            for r in 0..<k {\n                ans[r] += nextDp[r]\n \
        \           }\n            dp = nextDp\n        }\n\n        return ans\n  \
        \  }\n}"
      kotlin: "class Solution {\n    fun resultArray(nums: IntArray, k: Int): LongArray\
        \ {\n        val ans = LongArray(k)\n        var dp = LongArray(k)\n       \
        \ for (num in nums) {\n            val nextDp = LongArray(k)\n            val\
        \ v = num % k\n            nextDp[v] = nextDp[v] + 1L\n            for (r in\
        \ 0 until k) {\n                if (dp[r] > 0) {\n                    val nextR\
        \ = (r * v) % k\n                    nextDp[nextR] = nextDp[nextR] + dp[r]\n\
        \                }\n            }\n            for (r in 0 until k) {\n    \
        \            ans[r] = ans[r] + nextDp[r]\n            }\n            dp = nextDp\n\
        \        }\n        return ans\n    }\n}"
      dart: "class Solution {\n  List<int> resultArray(List<int> nums, int k) {\n  \
        \  List<int> ans = List<int>.filled(k, 0);\n    List<int> dp = List<int>.filled(k,\
        \ 0);\n    for (int num in nums) {\n      List<int> nextDp = List<int>.filled(k,\
        \ 0);\n      int v = num % k;\n      nextDp[v] += 1;\n      for (int r = 0;\
        \ r < k; r++) {\n        if (dp[r] > 0) {\n          nextDp[(r * v) % k] +=\
        \ dp[r];\n        }\n      }\n      for (int r = 0; r < k; r++) {\n        ans[r]\
        \ += nextDp[r];\n      }\n      dp = nextDp;\n    }\n    return ans;\n  }\n}"
      go: "func resultArray(nums []int, k int) []int64 {\n    ans := make([]int64, k)\n\
        \    dp := make([]int64, k)\n    for _, num := range nums {\n        nextDp\
        \ := make([]int64, k)\n        v := num % k\n        nextDp[v]++\n        for\
        \ r := 0; r < k; r++ {\n            if dp[r] > 0 {\n                nextDp[(r*v)%k]\
        \ += dp[r]\n            }\n        }\n        for r := 0; r < k; r++ {\n   \
        \         ans[r] += nextDp[r]\n        }\n        dp = nextDp\n    }\n    return\
        \ ans\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} k\n# @return {Integer[]}\n\
        def result_array(nums, k)\n    ans = Array.new(k, 0)\n    dp = Array.new(k,\
        \ 0)\n    nums.each do |num|\n        next_dp = Array.new(k, 0)\n        v =\
        \ num % k\n        next_dp[v] += 1\n        (0...k).each do |r|\n          \
        \  if dp[r] > 0\n                next_dp[(r * v) % k] += dp[r]\n           \
        \ end\n        end\n        (0...k).each do |r|\n            ans[r] += next_dp[r]\n\
        \        end\n        dp = next_dp\n    end\n    ans\nend"
      scala: "object Solution {\n    def resultArray(nums: Array[Int], k: Int): Array[Long]\
        \ = {\n        val ans = new Array[Long](k)\n        var dp = new Array[Long](k)\n\
        \        for (num <- nums) {\n            val nextDp = new Array[Long](k)\n\
        \            val v = num % k\n            nextDp(v) += 1L\n            for (r\
        \ <- 0 until k) {\n                if (dp(r) > 0) {\n                    nextDp((r\
        \ * v) % k) += dp(r)\n                }\n            }\n            for (r <-\
        \ 0 until k) {\n                ans(r) += nextDp(r)\n            }\n       \
        \     dp = nextDp\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn result_array(nums: Vec<i32>, k: i32) -> Vec<i64>\
        \ {\n        let k_usize = k as usize;\n        let mut dp = vec![0i64; k_usize];\n\
        \        let mut res = vec![0i64; k_usize];\n\n        for &num in &nums {\n\
        \            let mut next_dp = vec![0i64; k_usize];\n            let rem_val\
        \ = (num as i64 % k as i64) as usize;\n\n            next_dp[rem_val] += 1;\n\
        \            for r in 0..k_usize {\n                if dp[r] > 0 {\n       \
        \             next_dp[(r * rem_val) % k_usize] += dp[r];\n                }\n\
        \            }\n\n            dp = next_dp;\n            for r in 0..k_usize\
        \ {\n                res[r] += dp[r];\n            }\n        }\n\n        res\n\
        \    }\n}"
      racket: "(define/contract (result-array nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? (listof exact-integer?))\n  (define (update-at lst idx val)\n\
        \    (if (= idx 0)\n        (cons (+ (car lst) val) (cdr lst))\n        (cons\
        \ (car lst) (update-at (cdr lst) (- idx 1) val))))\n\n  (let* ([initial-dp (build-list\
        \ k (lambda (x) 0))]\n         [initial-res (build-list k (lambda (x) 0))]\n\
        \         [final-data (foldl (lambda (num acc)\n                           \
        \   (let* ([dp (car acc)]\n                                     [res (cdr acc)]\n\
        \                                     [rem-val (modulo num k)]\n           \
        \                          [next-dp1 (update-at (build-list k (lambda (x) 0))\
        \ rem-val 1)]\n                                     [next-dp (let loop ([dp-list\
        \ dp] [idx 0] [acc-dp next-dp1])\n                                         \
        \       (if (null? dp-list)\n                                              \
        \      acc-dp\n                                                    (let* ([count\
        \ (car dp-list)]\n                                                         \
        \  [new-acc (if (> count 0)\n                                              \
        \                          (update-at acc-dp (modulo (* idx rem-val) k) count)\n\
        \                                                                        acc-dp)])\n\
        \                                                      (loop (cdr dp-list) (+\
        \ idx 1) new-acc))))]\n                                     [new-res (map +\
        \ res next-dp)])\n                                (cons next-dp new-res)))\n\
        \                            (cons initial-dp initial-res)\n               \
        \             nums)])\n    (cdr final-data)))"
      erlang: "-spec result_array(Nums :: [integer()], K :: integer()) -> [integer()].\n\
        result_array(Nums, K) ->\n    InitialDp = lists:duplicate(K, 0),\n    InitialRes\
        \ = lists:duplicate(K, 0),\n    {_, FinalRes} = lists:foldl(fun(Num, {Dp, Res})\
        \ ->\n        RemVal = Num rem K,\n        NextDp0 = lists:duplicate(K, 0),\n\
        \        NextDp1 = update_at(NextDp0, RemVal, 1),\n        NextDp = extend_dp(Dp,\
        \ RemVal, K, 0, NextDp1),\n        NewRes = lists:zipwith(fun(R, D) -> R + D\
        \ end, Res, NextDp),\n        {NextDp, NewRes}\n    end, {InitialDp, InitialRes},\
        \ Nums),\n    FinalRes.\n\nupdate_at(List, Index, Add) ->\n    {Left, [Old |\
        \ Right]} = lists:split(Index, List),\n    Left ++ [Old + Add | Right].\n\n\
        extend_dp([], _RemVal, _K, _Idx, Acc) -> Acc;\nextend_dp([Count | Rest], RemVal,\
        \ K, Idx, Acc) ->\n    NewAcc = if Count > 0 ->\n        TargetRem = (Idx *\
        \ RemVal) rem K,\n        update_at(Acc, TargetRem, Count);\n    true -> Acc\n\
        \    end,\n    extend_dp(Rest, RemVal, K, Idx + 1, NewAcc)."
      elixir: "defmodule Solution do\n  @spec result_array(nums :: [integer], k :: integer)\
        \ :: [integer]\n  def result_array(nums, k) do\n    initial_dp = List.duplicate(0,\
        \ k)\n    initial_res = List.duplicate(0, k)\n\n    {_final_dp, final_res} =\
        \ Enum.reduce(nums, {initial_dp, initial_res}, fn num, {dp, res} ->\n      rem_val\
        \ = rem(num, k)\n      next_dp0 = List.duplicate(0, k)\n      next_dp1 = List.update_at(next_dp0,\
        \ rem_val, fn v -> v + 1 end)\n\n      next_dp = Enum.with_index(dp)\n     \
        \ |> Enum.reduce(next_dp1, fn {count, r}, acc ->\n        if count > 0 do\n\
        \          target_rem = rem(r * rem_val, k)\n          List.update_at(acc, target_rem,\
        \ fn v -> v + count end)\n        else\n          acc\n        end\n      end)\n\
        \n      new_res = Enum.zip(res, next_dp)\n      |> Enum.map(fn {r_val, d_val}\
        \ -> r_val + d_val end)\n\n      {next_dp, new_res}\n    end)\n\n    final_res\n\
        \  end\nend"
    approach: The problem asks us to find the number of contiguous subarrays of `nums`
      whose product modulo `k` equals `x` for all $0 \le x < k$. Since the operation
      involves removing non-overlapping prefix and suffix, it is equivalent to choosing
      any non-empty contiguous subarray $nums[i..j]$ where $0 \le i \le j < n$. We can
      solve this using dynamic programming. Let $dp[r]$ be the count of subarrays ending
      at the current index $i$ that have a product congruent to $r \pmod k$.
    time_complexity: O(n * k) because we iterate through the array once and, for each
      element, we perform at most $k$ operations to update the DP states.
    space_complexity: O(k) because we only maintain arrays of size $k$ to store the
      current and next DP states and the final results.
    elapsed_time: 193.8784236907959
    model: gemini-3-flash-preview
    generated_at: '2026-09-21 02:41:58 '
---

## Problem #3524: Find X Value of Array I

**Difficulty:** Medium

**Topics:** Array, Math, Dynamic Programming

## Problem Description

<p>You are given an array of <strong>positive</strong> integers <code>nums</code>, and a <strong>positive</strong> integer <code>k</code>.</p>

<p>You are allowed to perform an operation <strong>once</strong> on <code>nums</code>, where in each operation you can remove any <strong>non-overlapping</strong> prefix and suffix from <code>nums</code> such that <code>nums</code> remains <strong>non-empty</strong>.</p>

<p>You need to find the <strong>x-value</strong> of <code>nums</code>, which is the number of ways to perform this operation so that the <strong>product</strong> of the remaining elements leaves a <em>remainder</em> of <code>x</code> when divided by <code>k</code>.</p>

<p>Return an array <code>result</code> of size <code>k</code> where <code>result[x]</code> is the <strong>x-value</strong> of <code>nums</code> for <code>0 &lt;= x &lt;= k - 1</code>.</p>

<p>A <strong>prefix</strong> of an array is a <span data-keyword="subarray">subarray</span> that starts from the beginning of the array and extends to any point within it.</p>

<p>A <strong>suffix</strong> of an array is a <span data-keyword="subarray">subarray</span> that starts at any point within the array and extends to the end of the array.</p>

<p><strong>Note</strong> that the prefix and suffix to be chosen for the operation can be <strong>empty</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[9,2,4]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>x = 0</code>, the possible operations include all possible ways to remove non-overlapping prefix/suffix that do not remove <code>nums[2] == 3</code>.</li>
	<li>For <code>x = 1</code>, the possible operations are:
	<ul>
		<li>Remove the empty prefix and the suffix <code>[2, 3, 4, 5]</code>. <code>nums</code> becomes <code>[1]</code>.</li>
		<li>Remove the prefix <code>[1, 2, 3]</code> and the suffix <code>[5]</code>. <code>nums</code> becomes <code>[4]</code>.</li>
	</ul>
	</li>
	<li>For <code>x = 2</code>, the possible operations are:
	<ul>
		<li>Remove the empty prefix and the suffix <code>[3, 4, 5]</code>. <code>nums</code> becomes <code>[1, 2]</code>.</li>
		<li>Remove the prefix <code>[1]</code> and the suffix <code>[3, 4, 5]</code>. <code>nums</code> becomes <code>[2]</code>.</li>
		<li>Remove the prefix <code>[1, 2, 3]</code> and the empty suffix. <code>nums</code> becomes <code>[4, 5]</code>.</li>
		<li>Remove the prefix <code>[1, 2, 3, 4]</code> and the empty suffix. <code>nums</code> becomes <code>[5]</code>.</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,4,8,16,32], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">[18,1,2,0]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>x = 0</code>, the only operations that <strong>do not</strong> result in <code>x = 0</code> are:

	<ul>
		<li>Remove the empty prefix and the suffix <code>[4, 8, 16, 32]</code>. <code>nums</code> becomes <code>[1, 2]</code>.</li>
		<li>Remove the empty prefix and the suffix <code>[2, 4, 8, 16, 32]</code>. <code>nums</code> becomes <code>[1]</code>.</li>
		<li>Remove the prefix <code>[1]</code> and the suffix <code>[4, 8, 16, 32]</code>. <code>nums</code> becomes <code>[2]</code>.</li>
	</ul>
	</li>
	<li>For <code>x = 1</code>, the only possible operation is:
	<ul>
		<li>Remove the empty prefix and the suffix <code>[2, 4, 8, 16, 32]</code>. <code>nums</code> becomes <code>[1]</code>.</li>
	</ul>
	</li>
	<li>For <code>x = 2</code>, the possible operations are:
	<ul>
		<li>Remove the empty prefix and the suffix <code>[4, 8, 16, 32]</code>. <code>nums</code> becomes <code>[1, 2]</code>.</li>
		<li>Remove the prefix <code>[1]</code> and the suffix <code>[4, 8, 16, 32]</code>. <code>nums</code> becomes <code>[2]</code>.</li>
	</ul>
	</li>
	<li>For <code>x = 3</code>, there is no possible way to perform the operation.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,1,1], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[9,6]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 5</code></li>
</ul>


## Hints

1. Use dynamic programming.

2. Define `dp[i][r]` as the count of subarrays ending at index `i` whose product modulo `k` equals `r`.

3. Compute `dp[i][r]` for each index `i` in `nums` and sum over all indices to get the final counts for each remainder.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks us to find the number of contiguous subarrays of `nums` whose product modulo `k` equals `x` for all $0 \le x < k$. Since the operation involves removing non-overlapping prefix and suffix, it is equivalent to choosing any non-empty contiguous subarray $nums[i..j]$ where $0 \le i \le j < n$. We can solve this using dynamic programming. Let $dp[r]$ be the count of subarrays ending at the current index $i$ that have a product congruent to $r \pmod k$.

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
    vector<long long> resultArray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> res(k, 0);
        vector<long long> dp(k, 0);

        for (int i = 0; i < n; ++i) {
            vector<long long> next_dp(k, 0);
            int v = nums[i] % k;
            for (int r = 0; r < k; ++r) {
                if (dp[r] > 0) {
                    next_dp[(r * v) % k] += dp[r];
                }
            }
            next_dp[v]++;

            for (int r = 0; r < k; ++r) {
                dp[r] = next_dp[r];
                res[r] += dp[r];
            }
        }

        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long[] resultArray(int[] nums, int k) {
        int n = nums.length;
        long[] res = new long[k];
        long[] dp = new long[k];

        for (int i = 0; i < n; i++) {
            long[] nextDp = new long[k];
            int v = nums[i] % k;
            for (int r = 0; r < k; r++) {
                if (dp[r] > 0) {
                    nextDp[(r * v) % k] += dp[r];
                }
            }
            nextDp[v]++;

            for (int r = 0; r < k; r++) {
                dp[r] = nextDp[r];
                res[r] += dp[r];
            }
        }

        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0] * k
        dp = [0] * k

        for x in nums:
            v = x % k
            next_dp = [0] * k
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * v) % k] += dp[r]
            next_dp[v] += 1
            dp = next_dp
            for r in range(k):
                res[r] += dp[r]

        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        dp = [0] * k

        for x in nums:
            v = x % k
            next_dp = [0] * k
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * v) % k] += dp[r]
            next_dp[v] += 1
            dp = next_dp
            for r in range(k):
                res[r] += dp[r]

        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* resultArray(int* nums, int numsSize, int k, int* returnSize) {
    *returnSize = k;
    long long* res = (long long*)calloc(k, sizeof(long long));
    long long dp[5] = {0};
    long long next_dp[5] = {0};

    for (int i = 0; i < numsSize; i++) {
        int v = nums[i] % k;
        memset(next_dp, 0, sizeof(next_dp));

        for (int r = 0; r < k; r++) {
            if (dp[r] > 0) {
                next_dp[(r * v) % k] += dp[r];
            }
        }
        next_dp[v]++;

        for (int r = 0; r < k; r++) {
            dp[r] = next_dp[r];
            res[r] += dp[r];
        }
    }

    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long[] ResultArray(int[] nums, int k) {
        long[] ans = new long[k];
        long[] dp = new long[k];

        foreach (int num in nums) {
            long[] nextDp = new long[k];
            int val = num % k;

            for (int r = 0; r < k; r++) {
                if (dp[r] > 0) {
                    nextDp[(r * val) % k] += dp[r];
                }
            }

            nextDp[val]++;

            for (int r = 0; r < k; r++) {
                ans[r] += nextDp[r];
            }
            dp = nextDp;
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
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var resultArray = function(nums, k) {
    let ans = new Array(k).fill(0);
    let dp = new Array(k).fill(0);

    for (let i = 0; i < nums.length; i++) {
        let nextDp = new Array(k).fill(0);
        let val = nums[i] % k;

        for (let r = 0; r < k; r++) {
            if (dp[r] > 0) {
                nextDp[(r * val) % k] += dp[r];
            }
        }

        nextDp[val]++;

        for (let r = 0; r < k; r++) {
            ans[r] += nextDp[r];
        }
        dp = nextDp;
    }

    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function resultArray(nums: number[], k: number): number[] {
    let ans: number[] = new Array(k).fill(0);
    let dp: number[] = new Array(k).fill(0);

    for (let i = 0; i < nums.length; i++) {
        let nextDp: number[] = new Array(k).fill(0);
        let val = nums[i] % k;

        for (let r = 0; r < k; r++) {
            if (dp[r] > 0) {
                nextDp[(r * val) % k] += dp[r];
            }
        }

        nextDp[val]++;

        for (let r = 0; r < k; r++) {
            ans[r] += nextDp[r];
        }
        dp = nextDp;
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
     * @param Integer $k
     * @return Integer[]
     */
    function resultArray($nums, $k) {
        $ans = array_fill(0, $k, 0);
        $dp = array_fill(0, $k, 0);

        foreach ($nums as $num) {
            $nextDp = array_fill(0, $k, 0);
            $val = $num % $k;

            for ($r = 0; $r < $k; $r++) {
                if ($dp[$r] > 0) {
                    $nextDp[($r * $val) % $k] += $dp[$r];
                }
            }

            $nextDp[$val]++;

            for ($r = 0; $r < $k; $r++) {
                $ans[$r] += $nextDp[$r];
            }
            $dp = $nextDp;
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
    func resultArray(_ nums: [Int], _ k: Int) -> [Int] {
        var ans = [Int](repeating: 0, count: k)
        var dp = [Int](repeating: 0, count: k)

        for num in nums {
            var nextDp = [Int](repeating: 0, count: k)
            let val = num % k

            for r in 0..<k {
                if dp[r] > 0 {
                    nextDp[(r * val) % k] += dp[r]
                }
            }

            nextDp[val] += 1

            for r in 0..<k {
                ans[r] += nextDp[r]
            }
            dp = nextDp
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
    fun resultArray(nums: IntArray, k: Int): LongArray {
        val ans = LongArray(k)
        var dp = LongArray(k)
        for (num in nums) {
            val nextDp = LongArray(k)
            val v = num % k
            nextDp[v] = nextDp[v] + 1L
            for (r in 0 until k) {
                if (dp[r] > 0) {
                    val nextR = (r * v) % k
                    nextDp[nextR] = nextDp[nextR] + dp[r]
                }
            }
            for (r in 0 until k) {
                ans[r] = ans[r] + nextDp[r]
            }
            dp = nextDp
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
  List<int> resultArray(List<int> nums, int k) {
    List<int> ans = List<int>.filled(k, 0);
    List<int> dp = List<int>.filled(k, 0);
    for (int num in nums) {
      List<int> nextDp = List<int>.filled(k, 0);
      int v = num % k;
      nextDp[v] += 1;
      for (int r = 0; r < k; r++) {
        if (dp[r] > 0) {
          nextDp[(r * v) % k] += dp[r];
        }
      }
      for (int r = 0; r < k; r++) {
        ans[r] += nextDp[r];
      }
      dp = nextDp;
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
func resultArray(nums []int, k int) []int64 {
    ans := make([]int64, k)
    dp := make([]int64, k)
    for _, num := range nums {
        nextDp := make([]int64, k)
        v := num % k
        nextDp[v]++
        for r := 0; r < k; r++ {
            if dp[r] > 0 {
                nextDp[(r*v)%k] += dp[r]
            }
        }
        for r := 0; r < k; r++ {
            ans[r] += nextDp[r]
        }
        dp = nextDp
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def result_array(nums, k)
    ans = Array.new(k, 0)
    dp = Array.new(k, 0)
    nums.each do |num|
        next_dp = Array.new(k, 0)
        v = num % k
        next_dp[v] += 1
        (0...k).each do |r|
            if dp[r] > 0
                next_dp[(r * v) % k] += dp[r]
            end
        end
        (0...k).each do |r|
            ans[r] += next_dp[r]
        end
        dp = next_dp
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
    def resultArray(nums: Array[Int], k: Int): Array[Long] = {
        val ans = new Array[Long](k)
        var dp = new Array[Long](k)
        for (num <- nums) {
            val nextDp = new Array[Long](k)
            val v = num % k
            nextDp(v) += 1L
            for (r <- 0 until k) {
                if (dp(r) > 0) {
                    nextDp((r * v) % k) += dp(r)
                }
            }
            for (r <- 0 until k) {
                ans(r) += nextDp(r)
            }
            dp = nextDp
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
    pub fn result_array(nums: Vec<i32>, k: i32) -> Vec<i64> {
        let k_usize = k as usize;
        let mut dp = vec![0i64; k_usize];
        let mut res = vec![0i64; k_usize];

        for &num in &nums {
            let mut next_dp = vec![0i64; k_usize];
            let rem_val = (num as i64 % k as i64) as usize;

            next_dp[rem_val] += 1;
            for r in 0..k_usize {
                if dp[r] > 0 {
                    next_dp[(r * rem_val) % k_usize] += dp[r];
                }
            }

            dp = next_dp;
            for r in 0..k_usize {
                res[r] += dp[r];
            }
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
(define/contract (result-array nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (define (update-at lst idx val)
    (if (= idx 0)
        (cons (+ (car lst) val) (cdr lst))
        (cons (car lst) (update-at (cdr lst) (- idx 1) val))))

  (let* ([initial-dp (build-list k (lambda (x) 0))]
         [initial-res (build-list k (lambda (x) 0))]
         [final-data (foldl (lambda (num acc)
                              (let* ([dp (car acc)]
                                     [res (cdr acc)]
                                     [rem-val (modulo num k)]
                                     [next-dp1 (update-at (build-list k (lambda (x) 0)) rem-val 1)]
                                     [next-dp (let loop ([dp-list dp] [idx 0] [acc-dp next-dp1])
                                                (if (null? dp-list)
                                                    acc-dp
                                                    (let* ([count (car dp-list)]
                                                           [new-acc (if (> count 0)
                                                                        (update-at acc-dp (modulo (* idx rem-val) k) count)
                                                                        acc-dp)])
                                                      (loop (cdr dp-list) (+ idx 1) new-acc))))]
                                     [new-res (map + res next-dp)])
                                (cons next-dp new-res)))
                            (cons initial-dp initial-res)
                            nums)])
    (cdr final-data)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec result_array(Nums :: [integer()], K :: integer()) -> [integer()].
result_array(Nums, K) ->
    InitialDp = lists:duplicate(K, 0),
    InitialRes = lists:duplicate(K, 0),
    {_, FinalRes} = lists:foldl(fun(Num, {Dp, Res}) ->
        RemVal = Num rem K,
        NextDp0 = lists:duplicate(K, 0),
        NextDp1 = update_at(NextDp0, RemVal, 1),
        NextDp = extend_dp(Dp, RemVal, K, 0, NextDp1),
        NewRes = lists:zipwith(fun(R, D) -> R + D end, Res, NextDp),
        {NextDp, NewRes}
    end, {InitialDp, InitialRes}, Nums),
    FinalRes.

update_at(List, Index, Add) ->
    {Left, [Old | Right]} = lists:split(Index, List),
    Left ++ [Old + Add | Right].

extend_dp([], _RemVal, _K, _Idx, Acc) -> Acc;
extend_dp([Count | Rest], RemVal, K, Idx, Acc) ->
    NewAcc = if Count > 0 ->
        TargetRem = (Idx * RemVal) rem K,
        update_at(Acc, TargetRem, Count);
    true -> Acc
    end,
    extend_dp(Rest, RemVal, K, Idx + 1, NewAcc).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec result_array(nums :: [integer], k :: integer) :: [integer]
  def result_array(nums, k) do
    initial_dp = List.duplicate(0, k)
    initial_res = List.duplicate(0, k)

    {_final_dp, final_res} = Enum.reduce(nums, {initial_dp, initial_res}, fn num, {dp, res} ->
      rem_val = rem(num, k)
      next_dp0 = List.duplicate(0, k)
      next_dp1 = List.update_at(next_dp0, rem_val, fn v -> v + 1 end)

      next_dp = Enum.with_index(dp)
      |> Enum.reduce(next_dp1, fn {count, r}, acc ->
        if count > 0 do
          target_rem = rem(r * rem_val, k)
          List.update_at(acc, target_rem, fn v -> v + count end)
        else
          acc
        end
      end)

      new_res = Enum.zip(res, next_dp)
      |> Enum.map(fn {r_val, d_val} -> r_val + d_val end)

      {next_dp, new_res}
    end)

    final_res
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * k) because we iterate through the array once and, for each element, we perform at most $k$ operations to update the DP states.
- **Space Complexity:** O(k) because we only maintain arrays of size $k$ to store the current and next DP states and the final results.
