---
layout: post
title: "Count Subarrays With Majority Element II"
date: 2026-06-26 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Divide and Conquer", "Segment Tree", "Merge Sort", "Prefix Sum"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/count-subarrays-with-majority-element-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long countMajoritySubarrays(vector<int>&\
        \ nums, int target) {\n        int n = nums.size();\n        vector<int> countP(2\
        \ * n + 1, 0);\n        int offset = n;\n        int currP = 0;\n        countP[currP\
        \ + offset] = 1;\n        long long lessCount = 0;\n        long long ans =\
        \ 0;\n        for (int x : nums) {\n            int prevP = currP;\n       \
        \     if (x == target) {\n                currP++;\n                lessCount\
        \ += countP[prevP + offset];\n            } else {\n                currP--;\n\
        \                lessCount -= countP[currP + offset];\n            }\n     \
        \       ans += lessCount;\n            countP[currP + offset]++;\n        }\n\
        \        return ans;\n    }\n};"
      java: "class Solution {\n    public long countMajoritySubarrays(int[] nums, int\
        \ target) {\n        int n = nums.length;\n        int[] countP = new int[2\
        \ * n + 1];\n        int offset = n;\n        int currP = 0;\n        countP[currP\
        \ + offset] = 1;\n        long lessCount = 0;\n        long ans = 0;\n     \
        \   for (int x : nums) {\n            int prevP = currP;\n            if (x\
        \ == target) {\n                currP++;\n                lessCount += countP[prevP\
        \ + offset];\n            } else {\n                currP--;\n             \
        \   lessCount -= countP[currP + offset];\n            }\n            ans +=\
        \ lessCount;\n            countP[currP + offset]++;\n        }\n        return\
        \ ans;\n    }\n}"
      python: "class Solution(object):\n    def countMajoritySubarrays(self, nums, target):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type target: int\n\
        \        :rtype: int\n        \"\"\"\n        n = len(nums)\n        count_p\
        \ = [0] * (2 * n + 1)\n        offset = n\n        curr_p = 0\n        count_p[curr_p\
        \ + offset] = 1\n        less_count = 0\n        ans = 0\n        for x in nums:\n\
        \            prev_p = curr_p\n            if x == target:\n                curr_p\
        \ += 1\n                less_count += count_p[prev_p + offset]\n           \
        \ else:\n                curr_p -= 1\n                less_count -= count_p[curr_p\
        \ + offset]\n            ans += less_count\n            count_p[curr_p + offset]\
        \ += 1\n        return ans"
      python3: "class Solution:\n    def countMajoritySubarrays(self, nums: List[int],\
        \ target: int) -> int:\n        n = len(nums)\n        freq = [0] * (2 * n +\
        \ 1)\n        offset = n\n        curr = 0\n        freq[curr + offset] = 1\n\
        \        total_less = 0\n        ans = 0\n        for x in nums:\n         \
        \   if x == target:\n                total_less += freq[curr + offset]\n   \
        \             curr += 1\n            else:\n                curr -= 1\n    \
        \            total_less -= freq[curr + offset]\n            ans += total_less\n\
        \            freq[curr + offset] += 1\n        return ans"
      c: "#include <stdlib.h>\n\nlong long countMajoritySubarrays(int* nums, int numsSize,\
        \ int target) {\n    int n = numsSize;\n    int* freq = (int*)calloc(2 * n +\
        \ 1, sizeof(int));\n    if (!freq) return 0;\n    int offset = n;\n    int curr\
        \ = 0;\n    freq[curr + offset] = 1;\n    long long total_less = 0;\n    long\
        \ long ans = 0;\n    for (int i = 0; i < n; i++) {\n        if (nums[i] == target)\
        \ {\n            total_less += (long long)freq[curr + offset];\n           \
        \ curr += 1;\n        } else {\n            curr -= 1;\n            total_less\
        \ -= (long long)freq[curr + offset];\n        }\n        ans += total_less;\n\
        \        freq[curr + offset]++;\n    }\n    free(freq);\n    return ans;\n}"
      csharp: "public class Solution {\n    public long CountMajoritySubarrays(int[]\
        \ nums, int target) {\n        int n = nums.Length;\n        int[] freq = new\
        \ int[2 * n + 1];\n        int offset = n;\n        int curr = 0;\n        freq[curr\
        \ + offset] = 1;\n        long totalLess = 0;\n        long ans = 0;\n     \
        \   foreach (int x in nums) {\n            if (x == target) {\n            \
        \    totalLess += freq[curr + offset];\n                curr += 1;\n       \
        \     } else {\n                curr -= 1;\n                totalLess -= freq[curr\
        \ + offset];\n            }\n            ans += totalLess;\n            freq[curr\
        \ + offset]++;\n        }\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} target\n * @return\
        \ {number}\n */\nvar countMajoritySubarrays = function(nums, target) {\n   \
        \ const n = nums.length;\n    const freq = new Int32Array(2 * n + 1);\n    const\
        \ offset = n;\n    let curr = 0;\n    freq[curr + offset] = 1;\n    let totalLess\
        \ = 0;\n    let ans = 0;\n    for (let i = 0; i < n; i++) {\n        if (nums[i]\
        \ === target) {\n            totalLess += freq[curr + offset];\n           \
        \ curr += 1;\n        } else {\n            curr -= 1;\n            totalLess\
        \ -= freq[curr + offset];\n        }\n        ans += totalLess;\n        freq[curr\
        \ + offset]++;\n    }\n    return ans;\n};"
      typescript: "function countMajoritySubarrays(nums: number[], target: number):\
        \ number {\n    const n = nums.length;\n    const counts = new Int32Array(2\
        \ * n + 1);\n    let curP = 0;\n    let curS = 0;\n    let ans = 0;\n    counts[n]\
        \ = 1;\n    for (let i = 0; i < n; i++) {\n        const prevP = curP;\n   \
        \     if (nums[i] === target) {\n            curP++;\n            curS += counts[prevP\
        \ + n];\n        } else {\n            curP--;\n            curS -= counts[curP\
        \ + n];\n        }\n        ans += curS;\n        counts[curP + n]++;\n    }\n\
        \    return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $target\n     * @return Integer\n     */\n    function countMajoritySubarrays($nums,\
        \ $target) {\n        $n = count($nums);\n        $counts = array_fill(0, 2\
        \ * $n + 1, 0);\n        $curP = 0;\n        $curS = 0;\n        $ans = 0;\n\
        \        $counts[$n] = 1;\n        foreach ($nums as $num) {\n            $prevP\
        \ = $curP;\n            if ($num == $target) {\n                $curP++;\n \
        \               $curS += $counts[$prevP + $n];\n            } else {\n     \
        \           $curP--;\n                $curS -= $counts[$curP + $n];\n      \
        \      }\n            $ans += $curS;\n            $counts[$curP + $n]++;\n \
        \       }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func countMajoritySubarrays(_ nums: [Int], _ target:\
        \ Int) -> Int {\n        let n = nums.count\n        var counts = [Int](repeating:\
        \ 0, count: 2 * n + 1)\n        var curP = 0\n        var curS = 0\n       \
        \ var ans = 0\n        counts[n] = 1\n        for num in nums {\n          \
        \  let prevP = curP\n            if num == target {\n                curP +=\
        \ 1\n                curS += counts[prevP + n]\n            } else {\n     \
        \           curP -= 1\n                curS -= counts[curP + n]\n          \
        \  }\n            ans += curS\n            counts[curP + n] += 1\n        }\n\
        \        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun countMajoritySubarrays(nums: IntArray, target:\
        \ Int): Long {\n        val n = nums.size\n        val counts = IntArray(2 *\
        \ n + 1)\n        var curP = 0\n        var curS = 0L\n        var ans = 0L\n\
        \        counts[n] = 1\n        for (num in nums) {\n            val prevP =\
        \ curP\n            if (num == target) {\n                curP++\n         \
        \       curS += counts[prevP + n].toLong()\n            } else {\n         \
        \       curP--\n                curS -= counts[curP + n].toLong()\n        \
        \    }\n            ans += curS\n            counts[curP + n]++\n        }\n\
        \        return ans\n    }\n}"
      dart: "class Solution {\n  int countMajoritySubarrays(List<int> nums, int target)\
        \ {\n    int n = nums.length;\n    List<int> bit = List.filled(2 * n + 2, 0);\n\
        \n    void update(int idx, int val) {\n      while (idx < bit.length) {\n  \
        \      bit[idx] += val;\n        idx += idx & -idx;\n      }\n    }\n\n    int\
        \ query(int idx) {\n      int sum = 0;\n      while (idx > 0) {\n        sum\
        \ += bit[idx];\n        idx -= idx & -idx;\n      }\n      return sum;\n   \
        \ }\n\n    int currentSum = 0;\n    int ans = 0;\n    update(n + 1, 1);\n\n\
        \    for (int num in nums) {\n      if (num == target) {\n        currentSum++;\n\
        \      } else {\n        currentSum--;\n      }\n      ans += query(currentSum\
        \ + n);\n      update(currentSum + n + 1, 1);\n    }\n\n    return ans;\n  }\n\
        }"
      go: "func countMajoritySubarrays(nums []int, target int) int64 {\n    n := len(nums)\n\
        \    bit := make([]int64, 2*n+2)\n\n    update := func(idx int, val int64) {\n\
        \        for idx < len(bit) {\n            bit[idx] += val\n            idx\
        \ += idx & -idx\n        }\n    }\n\n    query := func(idx int) int64 {\n  \
        \      var sum int64\n        for idx > 0 {\n            sum += bit[idx]\n \
        \           idx -= idx & -idx\n        }\n        return sum\n    }\n\n    currentSum\
        \ := 0\n    var ans int64 = 0\n    update(n+1, 1)\n\n    for _, num := range\
        \ nums {\n        if num == target {\n            currentSum++\n        } else\
        \ {\n            currentSum--\n        }\n        ans += query(currentSum +\
        \ n)\n        update(currentSum + n + 1, 1)\n    }\n\n    return ans\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer}\n\
        def count_majority_subarrays(nums, target)\n  n = nums.length\n  bit = Array.new(2\
        \ * n + 2, 0)\n\n  update = lambda do |idx, val|\n    while idx < bit.length\n\
        \      bit[idx] += val\n      idx += idx & -idx\n    end\n  end\n\n  query =\
        \ lambda do |idx|\n    sum = 0\n    while idx > 0\n      sum += bit[idx]\n \
        \     idx -= idx & -idx\n    end\n    sum\n  end\n\n  current_sum = 0\n  ans\
        \ = 0\n  update.call(n + 1, 1)\n\n  nums.each do |num|\n    if num == target\n\
        \      current_sum += 1\n    else\n      current_sum -= 1\n    end\n    ans\
        \ += query.call(current_sum + n)\n    update.call(current_sum + n + 1, 1)\n\
        \  end\n\n  ans\nend"
      scala: "object Solution {\n    def countMajoritySubarrays(nums: Array[Int], target:\
        \ Int): Long = {\n        val n = nums.length\n        val bit = new Array[Long](2\
        \ * n + 2)\n\n        def update(i: Int, delta: Long): Unit = {\n          \
        \  var idx = i\n            while (idx < bit.length) {\n                bit(idx)\
        \ += delta\n                idx += idx & -idx\n            }\n        }\n\n\
        \        def query(i: Int): Long = {\n            var idx = i\n            var\
        \ sum = 0L\n            while (idx > 0) {\n                sum += bit(idx)\n\
        \                idx -= idx & -idx\n            }\n            sum\n       \
        \ }\n\n        var currentSum = 0\n        var ans = 0L\n        update(n +\
        \ 1, 1)\n\n        for (num <- nums) {\n            if (num == target) {\n \
        \               currentSum += 1\n            } else {\n                currentSum\
        \ -= 1\n            }\n            ans += query(currentSum + n)\n          \
        \  update(currentSum + n + 1, 1)\n        }\n\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn count_majority_subarrays(nums: Vec<i32>, target:\
        \ i32) -> i64 {\n        let n = nums.len();\n        let mut c = vec![0i64;\
        \ 2 * n + 1];\n        let offset = n as i32;\n        let mut current_sum:\
        \ i32 = 0;\n        let mut ans: i64 = 0;\n        let mut t: i64 = 0;\n\n \
        \       c[offset as usize] = 1;\n\n        for x in nums {\n            let\
        \ prev_sum = current_sum;\n            if x == target {\n                current_sum\
        \ += 1;\n                t += c[(prev_sum + offset) as usize];\n           \
        \ } else {\n                current_sum -= 1;\n                t -= c[(current_sum\
        \ + offset) as usize];\n            }\n            ans += t;\n            c[(current_sum\
        \ + offset) as usize] += 1;\n        }\n\n        ans\n    }\n}"
      racket: "(define/contract (count-majority-subarrays nums target)\n  (-> (listof\
        \ exact-integer?) exact-integer? exact-integer?)\n  (let* ([n (length nums)]\n\
        \         [c (make-vector (+ (* 2 n) 1) 0)]\n         [offset n])\n    (vector-set!\
        \ c offset 1)\n    (let loop ([lst nums]\n               [curr 0]\n        \
        \       [t 0]\n               [ans 0])\n      (if (null? lst)\n          ans\n\
        \          (let* ([x (car lst)]\n                 [prev curr]\n            \
        \     [next-curr (if (= x target) (+ curr 1) (- curr 1))]\n                \
        \ [next-t (if (> next-curr prev)\n                             (+ t (vector-ref\
        \ c (+ prev offset)))\n                             (- t (vector-ref c (+ next-curr\
        \ offset))))])\n            (begin\n              (vector-set! c (+ next-curr\
        \ offset) (+ (vector-ref c (+ next-curr offset)) 1))\n              (loop (cdr\
        \ lst) next-curr next-t (+ ans next-t))))))))"
      erlang: "-spec count_majority_subarrays(Nums :: [integer()], Target :: integer())\
        \ -> integer().\ncount_majority_subarrays(Nums, Target) ->\n  {_Curr, _T, Ans,\
        \ _C} = lists:foldl(\n    fun(X, {Curr, T, AnsAcc, C}) ->\n      Prev = Curr,\n\
        \      NextCurr = if X =:= Target -> Curr + 1; true -> Curr - 1 end,\n     \
        \ NextT = if NextCurr > Prev ->\n                   T + maps:get(Prev, C, 0);\n\
        \               true ->\n                   T - maps:get(NextCurr, C, 0)\n \
        \             end,\n      NewC = maps:put(NextCurr, maps:get(NextCurr, C, 0)\
        \ + 1, C),\n      {NextCurr, NextT, AnsAcc + NextT, NewC}\n    end,\n    {0,\
        \ 0, 0, #{0 => 1}},\n    Nums\n  ),\n  Ans."
      elixir: "defmodule Solution do\n  @spec count_majority_subarrays(nums :: [integer],\
        \ target :: integer) :: integer\n  def count_majority_subarrays(nums, target)\
        \ do\n    {_curr, _t, ans, _c} = Enum.reduce(nums, {0, 0, 0, %{0 => 1}}, fn\
        \ x, {curr, t, ans_acc, c} ->\n      prev = curr\n      next_curr = if x ==\
        \ target, do: curr + 1, else: curr - 1\n\n      next_t = if next_curr > prev\
        \ do\n        t + Map.get(c, prev, 0)\n      else\n        t - Map.get(c, next_curr,\
        \ 0)\n      end\n\n      new_c = Map.update(c, next_curr, 1, &(&1 + 1))\n  \
        \    {next_curr, next_t, ans_acc + next_t, new_c}\n    end)\n    ans\n  end\n\
        end"
    approach: 'The problem asks us to count subarrays where a target element is the
      majority (appearing strictly more than half of the times). This condition is equivalent
      to saying that if we assign a value of +1 to each occurrence of the target and
      -1 to all other elements, the sum of these values in the subarray must be strictly
      positive. By converting the array into these transformed values and computing
      prefix sums $P$, the problem simplifies to counting pairs of indices $(i, j)$
      such that $0 \le i < j \le n$ and $P[j] > P[i]$.


      To achieve optimal linear time complexity, we leverage the fact that adjacent
      prefix sums always differ by exactly 1. We maintain a frequency array to store
      the counts of prefix sums seen so far and a running variable, `lessCount`, which
      represents the number of previous prefix sums strictly smaller than the current
      one. As we iterate through the array and update the current prefix sum, we can
      update `lessCount` in constant time: when the prefix sum increases, `lessCount`
      increases by the count of the previous sum; when it decreases, `lessCount` decreases
      by the count of the new current sum. This allows us to calculate the total number
      of valid subarrays in a single $O(N)$ pass.'
    time_complexity: O(N), where N is the length of the input array. We iterate through
      the array exactly once, and all operations inside the loop (prefix sum updates,
      frequency array modifications, and running sum updates) are performed in $O(1)$
      time.
    space_complexity: O(N) to store the frequency array of prefix sums. Since the prefix
      sum $P[i]$ can range from $-N$ to $N$, we need an array of size $2N+1$ to accommodate
      all possible values using an offset.
    elapsed_time: 457.3530831336975
    model: gemini-3-flash-preview
    generated_at: '2026-06-26 02:46:53 '
---

## Problem #3739: Count Subarrays With Majority Element II

**Difficulty:** Hard

**Topics:** Array, Hash Table, Divide and Conquer, Segment Tree, Merge Sort, Prefix Sum

## Problem Description

<p>You are given an integer array <code>nums</code> and an integer <code>target</code>.</p>

<p>Return the number of <strong><span data-keyword="subarray-nonempty">subarrays</span></strong> of <code>nums</code> in which <code>target</code> is the <strong>majority element</strong>.</p>

<p>The <strong>majority element</strong> of a subarray is the element that appears <strong>strictly more than half</strong> of the times in that subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2,3], target = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>Valid subarrays with <code>target = 2</code> as the majority element:</p>

<ul>
	<li><code>nums[1..1] = [2]</code></li>
	<li><code>nums[2..2] = [2]</code></li>
	<li><code>nums[1..2] = [2,2]</code></li>
	<li><code>nums[0..2] = [1,2,2]</code></li>
	<li><code>nums[1..3] = [2,2,3]</code></li>
</ul>

<p>So there are 5 such subarrays.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1], target = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation: </strong></p>

<p><strong>​​​​​​​</strong>All 10 subarrays have 1 as the majority element.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3], target = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><code>target = 4</code> does not appear in <code>nums</code> at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>​​​​​​​5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>​​​​​​​9</sup></code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Convert to +1/-1: let `arr[i] = 1` if `nums[i] == target` else `-1`.

2. Build prefix sums: `pref[0]=0`, `pref[k] = pref[k - 1] + arr[k - 1]` for `k=1..n`.

3. Count pairs `(i  pref[i]` (these correspond to subarrays where `target` is majority).

4. Use coordinate compression on all `pref` values and a Fenwick tree / ordered map: iterate `k` from `0..n`, query how many previous `pref` are < current, add to `ans`, then update.

5. If `target` never appears return `0`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks us to count subarrays where a target element is the majority (appearing strictly more than half of the times). This condition is equivalent to saying that if we assign a value of +1 to each occurrence of the target and -1 to all other elements, the sum of these values in the subarray must be strictly positive. By converting the array into these transformed values and computing prefix sums $P$, the problem simplifies to counting pairs of indices $(i, j)$ such that $0 \le i < j \le n$ and $P[j] > P[i]$.

To achieve optimal linear time complexity, we leverage the fact that adjacent prefix sums always differ by exactly 1. We maintain a frequency array to store the counts of prefix sums seen so far and a running variable, `lessCount`, which represents the number of previous prefix sums strictly smaller than the current one. As we iterate through the array and update the current prefix sum, we can update `lessCount` in constant time: when the prefix sum increases, `lessCount` increases by the count of the previous sum; when it decreases, `lessCount` decreases by the count of the new current sum. This allows us to calculate the total number of valid subarrays in a single $O(N)$ pass.

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
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> countP(2 * n + 1, 0);
        int offset = n;
        int currP = 0;
        countP[currP + offset] = 1;
        long long lessCount = 0;
        long long ans = 0;
        for (int x : nums) {
            int prevP = currP;
            if (x == target) {
                currP++;
                lessCount += countP[prevP + offset];
            } else {
                currP--;
                lessCount -= countP[currP + offset];
            }
            ans += lessCount;
            countP[currP + offset]++;
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
    public long countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;
        int[] countP = new int[2 * n + 1];
        int offset = n;
        int currP = 0;
        countP[currP + offset] = 1;
        long lessCount = 0;
        long ans = 0;
        for (int x : nums) {
            int prevP = currP;
            if (x == target) {
                currP++;
                lessCount += countP[prevP + offset];
            } else {
                currP--;
                lessCount -= countP[currP + offset];
            }
            ans += lessCount;
            countP[currP + offset]++;
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
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        count_p = [0] * (2 * n + 1)
        offset = n
        curr_p = 0
        count_p[curr_p + offset] = 1
        less_count = 0
        ans = 0
        for x in nums:
            prev_p = curr_p
            if x == target:
                curr_p += 1
                less_count += count_p[prev_p + offset]
            else:
                curr_p -= 1
                less_count -= count_p[curr_p + offset]
            ans += less_count
            count_p[curr_p + offset] += 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        freq = [0] * (2 * n + 1)
        offset = n
        curr = 0
        freq[curr + offset] = 1
        total_less = 0
        ans = 0
        for x in nums:
            if x == target:
                total_less += freq[curr + offset]
                curr += 1
            else:
                curr -= 1
                total_less -= freq[curr + offset]
            ans += total_less
            freq[curr + offset] += 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

long long countMajoritySubarrays(int* nums, int numsSize, int target) {
    int n = numsSize;
    int* freq = (int*)calloc(2 * n + 1, sizeof(int));
    if (!freq) return 0;
    int offset = n;
    int curr = 0;
    freq[curr + offset] = 1;
    long long total_less = 0;
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] == target) {
            total_less += (long long)freq[curr + offset];
            curr += 1;
        } else {
            curr -= 1;
            total_less -= (long long)freq[curr + offset];
        }
        ans += total_less;
        freq[curr + offset]++;
    }
    free(freq);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long CountMajoritySubarrays(int[] nums, int target) {
        int n = nums.Length;
        int[] freq = new int[2 * n + 1];
        int offset = n;
        int curr = 0;
        freq[curr + offset] = 1;
        long totalLess = 0;
        long ans = 0;
        foreach (int x in nums) {
            if (x == target) {
                totalLess += freq[curr + offset];
                curr += 1;
            } else {
                curr -= 1;
                totalLess -= freq[curr + offset];
            }
            ans += totalLess;
            freq[curr + offset]++;
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
 * @param {number} target
 * @return {number}
 */
var countMajoritySubarrays = function(nums, target) {
    const n = nums.length;
    const freq = new Int32Array(2 * n + 1);
    const offset = n;
    let curr = 0;
    freq[curr + offset] = 1;
    let totalLess = 0;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] === target) {
            totalLess += freq[curr + offset];
            curr += 1;
        } else {
            curr -= 1;
            totalLess -= freq[curr + offset];
        }
        ans += totalLess;
        freq[curr + offset]++;
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countMajoritySubarrays(nums: number[], target: number): number {
    const n = nums.length;
    const counts = new Int32Array(2 * n + 1);
    let curP = 0;
    let curS = 0;
    let ans = 0;
    counts[n] = 1;
    for (let i = 0; i < n; i++) {
        const prevP = curP;
        if (nums[i] === target) {
            curP++;
            curS += counts[prevP + n];
        } else {
            curP--;
            curS -= counts[curP + n];
        }
        ans += curS;
        counts[curP + n]++;
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
     * @param Integer $target
     * @return Integer
     */
    function countMajoritySubarrays($nums, $target) {
        $n = count($nums);
        $counts = array_fill(0, 2 * $n + 1, 0);
        $curP = 0;
        $curS = 0;
        $ans = 0;
        $counts[$n] = 1;
        foreach ($nums as $num) {
            $prevP = $curP;
            if ($num == $target) {
                $curP++;
                $curS += $counts[$prevP + $n];
            } else {
                $curP--;
                $curS -= $counts[$curP + $n];
            }
            $ans += $curS;
            $counts[$curP + $n]++;
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
    func countMajoritySubarrays(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var counts = [Int](repeating: 0, count: 2 * n + 1)
        var curP = 0
        var curS = 0
        var ans = 0
        counts[n] = 1
        for num in nums {
            let prevP = curP
            if num == target {
                curP += 1
                curS += counts[prevP + n]
            } else {
                curP -= 1
                curS -= counts[curP + n]
            }
            ans += curS
            counts[curP + n] += 1
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
    fun countMajoritySubarrays(nums: IntArray, target: Int): Long {
        val n = nums.size
        val counts = IntArray(2 * n + 1)
        var curP = 0
        var curS = 0L
        var ans = 0L
        counts[n] = 1
        for (num in nums) {
            val prevP = curP
            if (num == target) {
                curP++
                curS += counts[prevP + n].toLong()
            } else {
                curP--
                curS -= counts[curP + n].toLong()
            }
            ans += curS
            counts[curP + n]++
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
  int countMajoritySubarrays(List<int> nums, int target) {
    int n = nums.length;
    List<int> bit = List.filled(2 * n + 2, 0);

    void update(int idx, int val) {
      while (idx < bit.length) {
        bit[idx] += val;
        idx += idx & -idx;
      }
    }

    int query(int idx) {
      int sum = 0;
      while (idx > 0) {
        sum += bit[idx];
        idx -= idx & -idx;
      }
      return sum;
    }

    int currentSum = 0;
    int ans = 0;
    update(n + 1, 1);

    for (int num in nums) {
      if (num == target) {
        currentSum++;
      } else {
        currentSum--;
      }
      ans += query(currentSum + n);
      update(currentSum + n + 1, 1);
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
func countMajoritySubarrays(nums []int, target int) int64 {
    n := len(nums)
    bit := make([]int64, 2*n+2)

    update := func(idx int, val int64) {
        for idx < len(bit) {
            bit[idx] += val
            idx += idx & -idx
        }
    }

    query := func(idx int) int64 {
        var sum int64
        for idx > 0 {
            sum += bit[idx]
            idx -= idx & -idx
        }
        return sum
    }

    currentSum := 0
    var ans int64 = 0
    update(n+1, 1)

    for _, num := range nums {
        if num == target {
            currentSum++
        } else {
            currentSum--
        }
        ans += query(currentSum + n)
        update(currentSum + n + 1, 1)
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
# @param {Integer} target
# @return {Integer}
def count_majority_subarrays(nums, target)
  n = nums.length
  bit = Array.new(2 * n + 2, 0)

  update = lambda do |idx, val|
    while idx < bit.length
      bit[idx] += val
      idx += idx & -idx
    end
  end

  query = lambda do |idx|
    sum = 0
    while idx > 0
      sum += bit[idx]
      idx -= idx & -idx
    end
    sum
  end

  current_sum = 0
  ans = 0
  update.call(n + 1, 1)

  nums.each do |num|
    if num == target
      current_sum += 1
    else
      current_sum -= 1
    end
    ans += query.call(current_sum + n)
    update.call(current_sum + n + 1, 1)
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
    def countMajoritySubarrays(nums: Array[Int], target: Int): Long = {
        val n = nums.length
        val bit = new Array[Long](2 * n + 2)

        def update(i: Int, delta: Long): Unit = {
            var idx = i
            while (idx < bit.length) {
                bit(idx) += delta
                idx += idx & -idx
            }
        }

        def query(i: Int): Long = {
            var idx = i
            var sum = 0L
            while (idx > 0) {
                sum += bit(idx)
                idx -= idx & -idx
            }
            sum
        }

        var currentSum = 0
        var ans = 0L
        update(n + 1, 1)

        for (num <- nums) {
            if (num == target) {
                currentSum += 1
            } else {
                currentSum -= 1
            }
            ans += query(currentSum + n)
            update(currentSum + n + 1, 1)
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
    pub fn count_majority_subarrays(nums: Vec<i32>, target: i32) -> i64 {
        let n = nums.len();
        let mut c = vec![0i64; 2 * n + 1];
        let offset = n as i32;
        let mut current_sum: i32 = 0;
        let mut ans: i64 = 0;
        let mut t: i64 = 0;

        c[offset as usize] = 1;

        for x in nums {
            let prev_sum = current_sum;
            if x == target {
                current_sum += 1;
                t += c[(prev_sum + offset) as usize];
            } else {
                current_sum -= 1;
                t -= c[(current_sum + offset) as usize];
            }
            ans += t;
            c[(current_sum + offset) as usize] += 1;
        }

        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-majority-subarrays nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [c (make-vector (+ (* 2 n) 1) 0)]
         [offset n])
    (vector-set! c offset 1)
    (let loop ([lst nums]
               [curr 0]
               [t 0]
               [ans 0])
      (if (null? lst)
          ans
          (let* ([x (car lst)]
                 [prev curr]
                 [next-curr (if (= x target) (+ curr 1) (- curr 1))]
                 [next-t (if (> next-curr prev)
                             (+ t (vector-ref c (+ prev offset)))
                             (- t (vector-ref c (+ next-curr offset))))])
            (begin
              (vector-set! c (+ next-curr offset) (+ (vector-ref c (+ next-curr offset)) 1))
              (loop (cdr lst) next-curr next-t (+ ans next-t))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_majority_subarrays(Nums :: [integer()], Target :: integer()) -> integer().
count_majority_subarrays(Nums, Target) ->
  {_Curr, _T, Ans, _C} = lists:foldl(
    fun(X, {Curr, T, AnsAcc, C}) ->
      Prev = Curr,
      NextCurr = if X =:= Target -> Curr + 1; true -> Curr - 1 end,
      NextT = if NextCurr > Prev ->
                   T + maps:get(Prev, C, 0);
               true ->
                   T - maps:get(NextCurr, C, 0)
              end,
      NewC = maps:put(NextCurr, maps:get(NextCurr, C, 0) + 1, C),
      {NextCurr, NextT, AnsAcc + NextT, NewC}
    end,
    {0, 0, 0, #{0 => 1}},
    Nums
  ),
  Ans.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_majority_subarrays(nums :: [integer], target :: integer) :: integer
  def count_majority_subarrays(nums, target) do
    {_curr, _t, ans, _c} = Enum.reduce(nums, {0, 0, 0, %{0 => 1}}, fn x, {curr, t, ans_acc, c} ->
      prev = curr
      next_curr = if x == target, do: curr + 1, else: curr - 1

      next_t = if next_curr > prev do
        t + Map.get(c, prev, 0)
      else
        t - Map.get(c, next_curr, 0)
      end

      new_c = Map.update(c, next_curr, 1, &(&1 + 1))
      {next_curr, next_t, ans_acc + next_t, new_c}
    end)
    ans
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the input array. We iterate through the array exactly once, and all operations inside the loop (prefix sum updates, frequency array modifications, and running sum updates) are performed in $O(1)$ time.
- **Space Complexity:** O(N) to store the frequency array of prefix sums. Since the prefix sum $P[i]$ can range from $-N$ to $N$, we need an array of size $2N+1$ to accommodate all possible values using an offset.
