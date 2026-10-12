---
layout: post
title: "Apply Operations on Array to Maximize Sum of Squares"
date: 2026-10-12 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Greedy", "Bit Manipulation"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxSum(vector<int>& nums, int k) {\n\
        \        vector<int> counts(31, 0);\n        for (int x : nums) {\n        \
        \    for (int j = 0; j < 31; ++j) {\n                if ((x >> j) & 1) {\n \
        \                   counts[j]++;\n                }\n            }\n       \
        \ }\n\n        long long ans = 0;\n        long long MOD = 1000000007;\n\n \
        \       for (int i = 0; i < k; ++i) {\n            long long val = 0;\n    \
        \        for (int j = 0; j < 31; ++j) {\n                if (counts[j] > 0)\
        \ {\n                    val |= (1LL << j);\n                    counts[j]--;\n\
        \                }\n            }\n            ans = (ans + (val * val) % MOD)\
        \ % MOD;\n        }\n\n        return (int)ans;\n    }\n};"
      java: "class Solution {\n    public int maxSum(List<Integer> nums, int k) {\n\
        \        int[] counts = new int[31];\n        for (int x : nums) {\n       \
        \     for (int j = 0; j < 31; j++) {\n                if (((x >> j) & 1) ==\
        \ 1) {\n                    counts[j]++;\n                }\n            }\n\
        \        }\n\n        long ans = 0;\n        long MOD = 1000000007L;\n\n   \
        \     for (int i = 0; i < k; i++) {\n            long val = 0;\n           \
        \ for (int j = 0; j < 31; j++) {\n                if (counts[j] > 0) {\n   \
        \                 val |= (1L << j);\n                    counts[j]--;\n    \
        \            }\n            }\n            ans = (ans + (val * val) % MOD) %\
        \ MOD;\n        }\n\n        return (int) ans;\n    }\n}"
      python: "class Solution(object):\n    def maxSum(self, nums, k):\n        \"\"\
        \"\n        :type nums: List[int]\n        :type k: int\n        :rtype: int\n\
        \        \"\"\"\n        counts = [0] * 31\n        for x in nums:\n       \
        \     for j in range(31):\n                if (x >> j) & 1:\n              \
        \      counts[j] += 1\n\n        ans = 0\n        MOD = 10**9 + 7\n\n      \
        \  for _ in range(k):\n            val = 0\n            for j in range(31):\n\
        \                if counts[j] > 0:\n                    val |= (1 << j)\n  \
        \                  counts[j] -= 1\n            ans = (ans + val * val) % MOD\n\
        \n        return ans"
      python3: "class Solution:\n    def maxSum(self, nums: List[int], k: int) -> int:\n\
        \        bit_counts = [0] * 31\n        for num in nums:\n            for b\
        \ in range(31):\n                if (num >> b) & 1:\n                    bit_counts[b]\
        \ += 1\n\n        MOD = 10**9 + 7\n        total_sum = 0\n        for _ in range(k):\n\
        \            val = 0\n            for b in range(31):\n                if bit_counts[b]\
        \ > 0:\n                    val |= (1 << b)\n                    bit_counts[b]\
        \ -= 1\n            total_sum = (total_sum + val * val) % MOD\n\n        return\
        \ total_sum"
      c: "int maxSum(int* nums, int numsSize, int k) {\n    int bitCounts[31] = {0};\n\
        \    for (int i = 0; i < numsSize; i++) {\n        for (int b = 0; b < 31; b++)\
        \ {\n            if ((nums[i] >> b) & 1) {\n                bitCounts[b]++;\n\
        \            }\n        }\n    }\n\n    long long totalSum = 0;\n    long long\
        \ MOD = 1000000007;\n    for (int i = 0; i < k; i++) {\n        long long val\
        \ = 0;\n        for (int b = 0; b < 31; b++) {\n            if (bitCounts[b]\
        \ > 0) {\n                val |= (1LL << b);\n                bitCounts[b]--;\n\
        \            }\n        }\n        totalSum = (totalSum + (val * val) % MOD)\
        \ % MOD;\n    }\n\n    return (int)totalSum;\n}"
      csharp: "public class Solution {\n    public int MaxSum(IList<int> nums, int k)\
        \ {\n        int[] bitCounts = new int[31];\n        foreach (int num in nums)\
        \ {\n            for (int b = 0; b < 31; b++) {\n                if (((num >>\
        \ b) & 1) == 1) {\n                    bitCounts[b]++;\n                }\n\
        \            }\n        }\n\n        long totalSum = 0;\n        long MOD =\
        \ 1000000007;\n        for (int i = 0; i < k; i++) {\n            long val =\
        \ 0;\n            for (int b = 0; b < 31; b++) {\n                if (bitCounts[b]\
        \ > 0) {\n                    val |= (1L << b);\n                    bitCounts[b]--;\n\
        \                }\n            }\n            totalSum = (totalSum + (val *\
        \ val) % MOD) % MOD;\n        }\n\n        return (int)totalSum;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar maxSum = function(nums, k) {\n    let bitCounts = new Array(31).fill(0);\n\
        \    for (let num of nums) {\n        for (let b = 0; b < 31; b++) {\n     \
        \       if ((num >> b) & 1) {\n                bitCounts[b]++;\n           \
        \ }\n        }\n    }\n\n    let totalSum = 0n;\n    let MOD = 1000000007n;\n\
        \    for (let i = 0; i < k; i++) {\n        let val = 0n;\n        for (let\
        \ b = 0; b < 31; b++) {\n            if (bitCounts[b] > 0) {\n             \
        \   val |= (1n << BigInt(b));\n                bitCounts[b]--;\n           \
        \ }\n        }\n        totalSum = (totalSum + (val * val) % MOD) % MOD;\n \
        \   }\n\n    return Number(totalSum);\n};"
      typescript: "function maxSum(nums: number[], k: number): number {\n    const counts:\
        \ number[] = new Array(31).fill(0);\n    for (const num of nums) {\n       \
        \ for (let i = 0; i < 31; i++) {\n            if ((num & (1 << i)) !== 0) {\n\
        \                counts[i]++;\n            }\n        }\n    }\n\n    const\
        \ MOD: bigint = 1000000007n;\n    let totalSum: bigint = 0n;\n\n    for (let\
        \ i = 0; i < k; i++) {\n        let val: bigint = 0n;\n        for (let j =\
        \ 0; j < 31; j++) {\n            if (counts[j] > 0) {\n                val |=\
        \ (1n << BigInt(j));\n                counts[j]--;\n            }\n        }\n\
        \        totalSum = (totalSum + (val * val)) % MOD;\n    }\n\n    return Number(totalSum);\n\
        }"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function maxSum($nums, $k)\
        \ {\n        $counts = array_fill(0, 31, 0);\n        foreach ($nums as $num)\
        \ {\n            for ($i = 0; $i < 31; $i++) {\n                if (($num >>\
        \ $i) & 1) {\n                    $counts[$i]++;\n                }\n      \
        \      }\n        }\n\n        $ans = 0;\n        $MOD = 1000000007;\n\n   \
        \     for ($i = 0; $i < $k; $i++) {\n            $val = 0;\n            for\
        \ ($j = 0; $j < 31; $j++) {\n                if ($counts[$j] > 0) {\n      \
        \              $val |= (1 << $j);\n                    $counts[$j]--;\n    \
        \            }\n            }\n            $valMod = $val % $MOD;\n        \
        \    $ans = ($ans + ($valMod * $valMod) % $MOD) % $MOD;\n        }\n\n     \
        \   return $ans;\n    }\n}"
      swift: "class Solution {\n    func maxSum(_ nums: [Int], _ k: Int) -> Int {\n\
        \        var counts = [Int](repeating: 0, count: 31)\n        for num in nums\
        \ {\n            for i in 0..<31 {\n                if (num & (1 << i)) != 0\
        \ {\n                    counts[i] += 1\n                }\n            }\n\
        \        }\n\n        var totalSum: Int64 = 0\n        let MOD: Int64 = 1000000007\n\
        \n        for _ in 0..<k {\n            var val: Int64 = 0\n            for\
        \ i in 0..<31 {\n                if counts[i] > 0 {\n                    val\
        \ |= (Int64(1) << i)\n                    counts[i] -= 1\n                }\n\
        \            }\n            let squaredVal = (val * val) % MOD\n           \
        \ totalSum = (totalSum + squaredVal) % MOD\n        }\n\n        return Int(totalSum)\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun maxSum(nums: List<Int>, k: Int): Int {\n  \
        \      val bitCounts = IntArray(31)\n        for (num in nums) {\n         \
        \   for (i in 0 until 31) {\n                if (((num shr i) and 1) == 1) {\n\
        \                    bitCounts[i]++\n                }\n            }\n    \
        \    }\n\n        var totalSum = 0L\n        val MOD = 1000000007L\n\n     \
        \   for (i in 0 until k) {\n            var currentVal = 0L\n            for\
        \ (j in 0 until 31) {\n                if (bitCounts[j] > 0) {\n           \
        \         currentVal = currentVal or (1L shl j)\n                    bitCounts[j]--\n\
        \                }\n            }\n            val squaredVal = (currentVal\
        \ * currentVal) % MOD\n            totalSum = (totalSum + squaredVal) % MOD\n\
        \        }\n\n        return totalSum.toInt()\n    }\n}"
      dart: "class Solution {\n  int maxSum(List<int> nums, int k) {\n    List<int>\
        \ bitCount = List.filled(31, 0);\n    for (var num in nums) {\n      for (var\
        \ i = 0; i < 31; i++) {\n        if (((num >> i) & 1) == 1) {\n          bitCount[i]++;\n\
        \        }\n      }\n    }\n\n    int totalSum = 0;\n    const int mod = 1000000007;\n\
        \n    for (var i = 0; i < k; i++) {\n      int current = 0;\n      for (var\
        \ j = 0; j < 31; j++) {\n        if (bitCount[j] > 0) {\n          current |=\
        \ (1 << j);\n          bitCount[j]--;\n        }\n      }\n      // current\
        \ * current can be up to 1.15e18, which fits in a 64-bit signed int.\n     \
        \ totalSum = (totalSum + (current * current)) % mod;\n    }\n\n    return totalSum;\n\
        \  }\n}"
      go: "func maxSum(nums []int, k int) int {\n    bitCount := make([]int, 31)\n \
        \   for _, num := range nums {\n        for i := 0; i < 31; i++ {\n        \
        \    if (num >> i)&1 == 1 {\n                bitCount[i]++\n            }\n\
        \        }\n    }\n\n    var totalSum int64 = 0\n    const mod int64 = 1000000007\n\
        \n    for i := 0; i < k; i++ {\n        var current int64 = 0\n        for j\
        \ := 0; j < 31; j++ {\n            if bitCount[j] > 0 {\n                current\
        \ |= (int64(1) << j)\n                bitCount[j]--\n            }\n       \
        \ }\n        // current * current fits in int64 because it is at most ~1.15e18.\n\
        \        totalSum = (totalSum + (current * current)) % mod\n    }\n\n    return\
        \ int(totalSum)\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} k\n# @return {Integer}\n\
        def max_sum(nums, k)\n  bit_count = Array.new(31, 0)\n  nums.each do |num|\n\
        \    31.times do |i|\n      bit_count[i] += 1 if (num >> i) & 1 == 1\n    end\n\
        \  end\n\n  total_sum = 0\n  mod = 1_000_000_007\n\n  k.times do\n    current\
        \ = 0\n    31.times do |j|\n      if bit_count[j] > 0\n        current |= (1\
        \ << j)\n        bit_count[j] -= 1\n      end\n    end\n    total_sum = (total_sum\
        \ + current * current) % mod\n  end\n\n  total_sum\nend"
      scala: "object Solution {\n    def maxSum(nums: List[Int], k: Int): Int = {\n\
        \        val bitCount = Array.fill(31)(0)\n        nums.foreach { num =>\n \
        \           var i = 0\n            while (i < 31) {\n                if (((num\
        \ >> i) & 1) == 1) {\n                    bitCount(i) += 1\n               \
        \ }\n                i += 1\n            }\n        }\n\n        var totalSum:\
        \ Long = 0\n        val mod: Long = 1000000007L\n\n        var i = 0\n     \
        \   while (i < k) {\n            var current: Long = 0\n            var j =\
        \ 0\n            while (j < 31) {\n                if (bitCount(j) > 0) {\n\
        \                    current |= (1L << j)\n                    bitCount(j) -=\
        \ 1\n                }\n                j += 1\n            }\n            totalSum\
        \ = (totalSum + (current * current)) % mod\n            i += 1\n        }\n\n\
        \        totalSum.toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn max_sum(nums: Vec<i32>, k: i32) -> i32 {\n\
        \        let mut bit_counts = [0; 31];\n        for &num in &nums {\n      \
        \      for i in 0..31 {\n                if (num & (1 << i)) != 0 {\n      \
        \              bit_counts[i] += 1;\n                }\n            }\n     \
        \   }\n\n        let mut ans: i64 = 0;\n        let mod_val: i64 = 1_000_000_007;\n\
        \n        for i in 1..=k {\n            let mut current_num: i64 = 0;\n    \
        \        for bit in 0..31 {\n                if bit_counts[bit] >= i {\n   \
        \                 current_num |= 1i64 << bit;\n                }\n         \
        \   }\n            ans = (ans + (current_num * current_num)) % mod_val;\n  \
        \      }\n\n        ans as i32\n    }\n}"
      racket: "(define/contract (max-sum nums k)\n  (-> (listof exact-integer?) exact-integer?\
        \ exact-integer?)\n  (let ([bit-counts (make-vector 31 0)]\n        [mod-val\
        \ 1000000007])\n    (for ([num nums])\n      (for ([i (in-range 31)])\n    \
        \    (when (not (zero? (bitwise-and num (arithmetic-shift 1 i))))\n        \
        \  (vector-set! bit-counts i (+ (vector-ref bit-counts i) 1)))))\n    (let loop\
        \ ([i 1] [ans 0])\n      (if (> i k)\n          ans\n          (let* ([final-num\
        \ (for/fold ([val 0])\n                                       ([bit (in-range\
        \ 31)])\n                               (if (>= (vector-ref bit-counts bit)\
        \ i)\n                                   (bitwise-ior val (arithmetic-shift\
        \ 1 bit))\n                                   val))]\n                 [sq (*\
        \ final-num final-num)])\n            (loop (+ i 1) (remainder (+ ans sq) mod-val)))))))"
      erlang: "-spec max_sum(Nums :: [integer()], K :: integer()) -> integer().\nmax_sum(Nums,\
        \ K) ->\n    Counts = count_all_bits(Nums, {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}),\n\
        \    calculate_sum_simple(1, K, 0, Counts, 1000000007).\n\ncount_all_bits([],\
        \ Acc) -> Acc;\ncount_all_bits([H|T], Acc) ->\n    count_all_bits(T, update_counts(H,\
        \ 0, Acc)).\n\nupdate_counts(0, _, Acc) -> Acc;\nupdate_counts(N, Bit, Acc)\
        \ ->\n    NewAcc = if (N band 1) == 1 ->\n        setelement(Bit + 1, Acc, element(Bit\
        \ + 1, Acc) + 1);\n    true ->\n        Acc\n    end,\n    update_counts(N bsr\
        \ 1, Bit + 1, NewAcc).\n\ncalculate_sum_simple(I, K, Ans, Counts, MOD) when\
        \ I =< K ->\n    Num = build_num_simple(I, 0, 0, Counts),\n    NewAns = (Ans\
        \ + (Num * Num)) rem MOD,\n    calculate_sum_simple(I + 1, K, NewAns, Counts,\
        \ MOD);\ncalculate_sum_simple(_, _, Ans, _, _) -> Ans.\n\nbuild_num_simple(_,\
        \ 31, Num, _Counts) -> Num;\nbuild_num_simple(I, Bit, Num, Counts) ->\n    NewNum\
        \ = if element(Bit + 1, Counts) >= I ->\n        Num bor (1 bsl Bit);\n    true\
        \ ->\n        Num\n    end,\n    build_num_simple(I, Bit + 1, NewNum, Counts)."
      elixir: "defmodule Solution do\n  import Bitwise\n\n  @spec max_sum(nums :: [integer],\
        \ k :: integer) :: integer\n  def max_sum(nums, k) do\n    initial_counts =\
        \ {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}\n    counts\
        \ = Enum.reduce(nums, initial_counts, fn num, acc ->\n      count_bits(num,\
        \ 0, acc)\n    end)\n\n    mod_val = 1_000_000_007\n\n    Enum.reduce(1..k,\
        \ 0, fn i, total_sum ->\n      num = build_num_simple(i, 0, 0, counts)\n   \
        \   rem(total_sum + num * num, mod_val)\n    end)\n  end\n\n  defp count_bits(0,\
        \ _, acc), do: acc\n  defp count_bits(num, bit, acc) do\n    new_acc = if (num\
        \ &&& 1) == 1 do\n      put_elem(acc, bit, elem(acc, bit) + 1)\n    else\n \
        \     acc\n    end\n    count_bits(num >>> 1, bit + 1, new_acc)\n  end\n\n \
        \ defp build_num_simple(_i, 31, num, _counts), do: num\n  defp build_num_simple(i,\
        \ bit, num, counts) do\n    if elem(counts, bit) >= i do\n      build_num_simple(i,\
        \ bit + 1, num ||| (1 <<< bit), counts)\n    else\n      build_num_simple(i,\
        \ bit + 1, num, counts)\n    end\n  end\nend"
    approach: 'The core of the problem lies in the bitwise operation $(nums[i] \text{
      AND } nums[j], nums[i] \text{ OR } nums[j])$, which can be interpreted as transferring
      set bits from one number to another at the same bit position. Specifically, if
      one element has a 1 at bit $p$ and another has a 0, the operation moves that 1
      to the second element. This implies that the total count of set bits at each bit
      position across the entire array remains constant regardless of the number of
      operations performed. To maximize the sum of squares, the intuition is to concentrate
      these set bits to make the chosen $k$ elements as large as possible. This is because
      the square function is convex, meaning that increasing the variance of the numbers
      while maintaining the bitwise sum increases the total sum of squares.


      The algorithm first iterates through the entire array to count the frequency of
      set bits at each of the 30 bit positions (since $nums[i] \le 10^9$). To greedily
      construct the $k$ largest possible numbers, we iterate $k$ times. In each iteration,
      we build a number by setting its $j$-th bit if the $j$-th bit position still has
      at least one remaining set bit. After constructing each of these $k$ numbers,
      we calculate its square and add it to the running sum modulo $10^9 + 7$. This
      greedy strategy ensures that we are selecting the $k$ elements with the maximum
      possible bit concentration, achieving the highest possible sum of squares.'
    time_complexity: O(N * log(max(nums))) where N is the length of the array. We iterate
      through the array once to count the bits (O(N * 30)) and then iterate k times
      to construct the k largest numbers (O(k * 30)). Since k is at most N, the complexity
      simplifies to O(N).
    space_complexity: O(log(max(nums))) to store the frequency of set bits at each bit
      position. In this case, it is O(31), which is constant space O(1).
    elapsed_time: 389.8504674434662
    model: gemini-3-flash-preview
    generated_at: '2026-10-12 03:42:11 '
---

## Problem #2897: Apply Operations on Array to Maximize Sum of Squares

**Difficulty:** Hard

**Topics:** Array, Hash Table, Greedy, Bit Manipulation

## Problem Description

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and a <strong>positive</strong> integer <code>k</code>.</p>

<p>You can do the following operation on the array <strong>any</strong> number of times:</p>

<ul>
	<li>Choose any two distinct indices <code>i</code> and <code>j</code> and <strong>simultaneously</strong> update the values of <code>nums[i]</code> to <code>(nums[i] AND nums[j])</code> and <code>nums[j]</code> to <code>(nums[i] OR nums[j])</code>. Here, <code>OR</code> denotes the bitwise <code>OR</code> operation, and <code>AND</code> denotes the bitwise <code>AND</code> operation.</li>
</ul>

<p>You have to choose <code>k</code> elements from the final array and calculate the sum of their <strong>squares</strong>.</p>

<p>Return <em>the <strong>maximum</strong> sum of squares you can achieve</em>.</p>

<p>Since the answer can be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,6,5,8], k = 2
<strong>Output:</strong> 261
<strong>Explanation:</strong> We can do the following operations on the array:
- Choose i = 0 and j = 3, then change nums[0] to (2 AND 8) = 0 and nums[3] to (2 OR 8) = 10. The resulting array is nums = [0,6,5,10].
- Choose i = 2 and j = 3, then change nums[2] to (5 AND 10) = 0 and nums[3] to (5 OR 10) = 15. The resulting array is nums = [0,6,0,15].
We can choose the elements 15 and 6 from the final array. The sum of squares is 15<sup>2</sup> + 6<sup>2</sup> = 261.
It can be shown that this is the maximum value we can get.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,5,4,7], k = 3
<strong>Output:</strong> 90
<strong>Explanation:</strong> We do not need to apply any operations.
We can choose the elements 7, 5, and 4 with a sum of squares: 7<sup>2</sup> + 5<sup>2</sup> + 4<sup>2</sup> = 90.
It can be shown that this is the maximum value we can get.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. The operation described only transfers some bits from one element to another in their binary representation.

2. To have a maximum sum of squares, it is optimal to greedily make each number as big as possible.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core of the problem lies in the bitwise operation $(nums[i] \text{ AND } nums[j], nums[i] \text{ OR } nums[j])$, which can be interpreted as transferring set bits from one number to another at the same bit position. Specifically, if one element has a 1 at bit $p$ and another has a 0, the operation moves that 1 to the second element. This implies that the total count of set bits at each bit position across the entire array remains constant regardless of the number of operations performed. To maximize the sum of squares, the intuition is to concentrate these set bits to make the chosen $k$ elements as large as possible. This is because the square function is convex, meaning that increasing the variance of the numbers while maintaining the bitwise sum increases the total sum of squares.

The algorithm first iterates through the entire array to count the frequency of set bits at each of the 30 bit positions (since $nums[i] \le 10^9$). To greedily construct the $k$ largest possible numbers, we iterate $k$ times. In each iteration, we build a number by setting its $j$-th bit if the $j$-th bit position still has at least one remaining set bit. After constructing each of these $k$ numbers, we calculate its square and add it to the running sum modulo $10^9 + 7$. This greedy strategy ensures that we are selecting the $k$ elements with the maximum possible bit concentration, achieving the highest possible sum of squares.

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
    int maxSum(vector<int>& nums, int k) {
        vector<int> counts(31, 0);
        for (int x : nums) {
            for (int j = 0; j < 31; ++j) {
                if ((x >> j) & 1) {
                    counts[j]++;
                }
            }
        }

        long long ans = 0;
        long long MOD = 1000000007;

        for (int i = 0; i < k; ++i) {
            long long val = 0;
            for (int j = 0; j < 31; ++j) {
                if (counts[j] > 0) {
                    val |= (1LL << j);
                    counts[j]--;
                }
            }
            ans = (ans + (val * val) % MOD) % MOD;
        }

        return (int)ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxSum(List<Integer> nums, int k) {
        int[] counts = new int[31];
        for (int x : nums) {
            for (int j = 0; j < 31; j++) {
                if (((x >> j) & 1) == 1) {
                    counts[j]++;
                }
            }
        }

        long ans = 0;
        long MOD = 1000000007L;

        for (int i = 0; i < k; i++) {
            long val = 0;
            for (int j = 0; j < 31; j++) {
                if (counts[j] > 0) {
                    val |= (1L << j);
                    counts[j]--;
                }
            }
            ans = (ans + (val * val) % MOD) % MOD;
        }

        return (int) ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = [0] * 31
        for x in nums:
            for j in range(31):
                if (x >> j) & 1:
                    counts[j] += 1

        ans = 0
        MOD = 10**9 + 7

        for _ in range(k):
            val = 0
            for j in range(31):
                if counts[j] > 0:
                    val |= (1 << j)
                    counts[j] -= 1
            ans = (ans + val * val) % MOD

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bit_counts = [0] * 31
        for num in nums:
            for b in range(31):
                if (num >> b) & 1:
                    bit_counts[b] += 1

        MOD = 10**9 + 7
        total_sum = 0
        for _ in range(k):
            val = 0
            for b in range(31):
                if bit_counts[b] > 0:
                    val |= (1 << b)
                    bit_counts[b] -= 1
            total_sum = (total_sum + val * val) % MOD

        return total_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxSum(int* nums, int numsSize, int k) {
    int bitCounts[31] = {0};
    for (int i = 0; i < numsSize; i++) {
        for (int b = 0; b < 31; b++) {
            if ((nums[i] >> b) & 1) {
                bitCounts[b]++;
            }
        }
    }

    long long totalSum = 0;
    long long MOD = 1000000007;
    for (int i = 0; i < k; i++) {
        long long val = 0;
        for (int b = 0; b < 31; b++) {
            if (bitCounts[b] > 0) {
                val |= (1LL << b);
                bitCounts[b]--;
            }
        }
        totalSum = (totalSum + (val * val) % MOD) % MOD;
    }

    return (int)totalSum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxSum(IList<int> nums, int k) {
        int[] bitCounts = new int[31];
        foreach (int num in nums) {
            for (int b = 0; b < 31; b++) {
                if (((num >> b) & 1) == 1) {
                    bitCounts[b]++;
                }
            }
        }

        long totalSum = 0;
        long MOD = 1000000007;
        for (int i = 0; i < k; i++) {
            long val = 0;
            for (int b = 0; b < 31; b++) {
                if (bitCounts[b] > 0) {
                    val |= (1L << b);
                    bitCounts[b]--;
                }
            }
            totalSum = (totalSum + (val * val) % MOD) % MOD;
        }

        return (int)totalSum;
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
 * @return {number}
 */
var maxSum = function(nums, k) {
    let bitCounts = new Array(31).fill(0);
    for (let num of nums) {
        for (let b = 0; b < 31; b++) {
            if ((num >> b) & 1) {
                bitCounts[b]++;
            }
        }
    }

    let totalSum = 0n;
    let MOD = 1000000007n;
    for (let i = 0; i < k; i++) {
        let val = 0n;
        for (let b = 0; b < 31; b++) {
            if (bitCounts[b] > 0) {
                val |= (1n << BigInt(b));
                bitCounts[b]--;
            }
        }
        totalSum = (totalSum + (val * val) % MOD) % MOD;
    }

    return Number(totalSum);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSum(nums: number[], k: number): number {
    const counts: number[] = new Array(31).fill(0);
    for (const num of nums) {
        for (let i = 0; i < 31; i++) {
            if ((num & (1 << i)) !== 0) {
                counts[i]++;
            }
        }
    }

    const MOD: bigint = 1000000007n;
    let totalSum: bigint = 0n;

    for (let i = 0; i < k; i++) {
        let val: bigint = 0n;
        for (let j = 0; j < 31; j++) {
            if (counts[j] > 0) {
                val |= (1n << BigInt(j));
                counts[j]--;
            }
        }
        totalSum = (totalSum + (val * val)) % MOD;
    }

    return Number(totalSum);
}
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
     * @return Integer
     */
    function maxSum($nums, $k) {
        $counts = array_fill(0, 31, 0);
        foreach ($nums as $num) {
            for ($i = 0; $i < 31; $i++) {
                if (($num >> $i) & 1) {
                    $counts[$i]++;
                }
            }
        }

        $ans = 0;
        $MOD = 1000000007;

        for ($i = 0; $i < $k; $i++) {
            $val = 0;
            for ($j = 0; $j < 31; $j++) {
                if ($counts[$j] > 0) {
                    $val |= (1 << $j);
                    $counts[$j]--;
                }
            }
            $valMod = $val % $MOD;
            $ans = ($ans + ($valMod * $valMod) % $MOD) % $MOD;
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
    func maxSum(_ nums: [Int], _ k: Int) -> Int {
        var counts = [Int](repeating: 0, count: 31)
        for num in nums {
            for i in 0..<31 {
                if (num & (1 << i)) != 0 {
                    counts[i] += 1
                }
            }
        }

        var totalSum: Int64 = 0
        let MOD: Int64 = 1000000007

        for _ in 0..<k {
            var val: Int64 = 0
            for i in 0..<31 {
                if counts[i] > 0 {
                    val |= (Int64(1) << i)
                    counts[i] -= 1
                }
            }
            let squaredVal = (val * val) % MOD
            totalSum = (totalSum + squaredVal) % MOD
        }

        return Int(totalSum)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxSum(nums: List<Int>, k: Int): Int {
        val bitCounts = IntArray(31)
        for (num in nums) {
            for (i in 0 until 31) {
                if (((num shr i) and 1) == 1) {
                    bitCounts[i]++
                }
            }
        }

        var totalSum = 0L
        val MOD = 1000000007L

        for (i in 0 until k) {
            var currentVal = 0L
            for (j in 0 until 31) {
                if (bitCounts[j] > 0) {
                    currentVal = currentVal or (1L shl j)
                    bitCounts[j]--
                }
            }
            val squaredVal = (currentVal * currentVal) % MOD
            totalSum = (totalSum + squaredVal) % MOD
        }

        return totalSum.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxSum(List<int> nums, int k) {
    List<int> bitCount = List.filled(31, 0);
    for (var num in nums) {
      for (var i = 0; i < 31; i++) {
        if (((num >> i) & 1) == 1) {
          bitCount[i]++;
        }
      }
    }

    int totalSum = 0;
    const int mod = 1000000007;

    for (var i = 0; i < k; i++) {
      int current = 0;
      for (var j = 0; j < 31; j++) {
        if (bitCount[j] > 0) {
          current |= (1 << j);
          bitCount[j]--;
        }
      }
      // current * current can be up to 1.15e18, which fits in a 64-bit signed int.
      totalSum = (totalSum + (current * current)) % mod;
    }

    return totalSum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxSum(nums []int, k int) int {
    bitCount := make([]int, 31)
    for _, num := range nums {
        for i := 0; i < 31; i++ {
            if (num >> i)&1 == 1 {
                bitCount[i]++
            }
        }
    }

    var totalSum int64 = 0
    const mod int64 = 1000000007

    for i := 0; i < k; i++ {
        var current int64 = 0
        for j := 0; j < 31; j++ {
            if bitCount[j] > 0 {
                current |= (int64(1) << j)
                bitCount[j]--
            }
        }
        // current * current fits in int64 because it is at most ~1.15e18.
        totalSum = (totalSum + (current * current)) % mod
    }

    return int(totalSum)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_sum(nums, k)
  bit_count = Array.new(31, 0)
  nums.each do |num|
    31.times do |i|
      bit_count[i] += 1 if (num >> i) & 1 == 1
    end
  end

  total_sum = 0
  mod = 1_000_000_007

  k.times do
    current = 0
    31.times do |j|
      if bit_count[j] > 0
        current |= (1 << j)
        bit_count[j] -= 1
      end
    end
    total_sum = (total_sum + current * current) % mod
  end

  total_sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxSum(nums: List[Int], k: Int): Int = {
        val bitCount = Array.fill(31)(0)
        nums.foreach { num =>
            var i = 0
            while (i < 31) {
                if (((num >> i) & 1) == 1) {
                    bitCount(i) += 1
                }
                i += 1
            }
        }

        var totalSum: Long = 0
        val mod: Long = 1000000007L

        var i = 0
        while (i < k) {
            var current: Long = 0
            var j = 0
            while (j < 31) {
                if (bitCount(j) > 0) {
                    current |= (1L << j)
                    bitCount(j) -= 1
                }
                j += 1
            }
            totalSum = (totalSum + (current * current)) % mod
            i += 1
        }

        totalSum.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut bit_counts = [0; 31];
        for &num in &nums {
            for i in 0..31 {
                if (num & (1 << i)) != 0 {
                    bit_counts[i] += 1;
                }
            }
        }

        let mut ans: i64 = 0;
        let mod_val: i64 = 1_000_000_007;

        for i in 1..=k {
            let mut current_num: i64 = 0;
            for bit in 0..31 {
                if bit_counts[bit] >= i {
                    current_num |= 1i64 << bit;
                }
            }
            ans = (ans + (current_num * current_num)) % mod_val;
        }

        ans as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([bit-counts (make-vector 31 0)]
        [mod-val 1000000007])
    (for ([num nums])
      (for ([i (in-range 31)])
        (when (not (zero? (bitwise-and num (arithmetic-shift 1 i))))
          (vector-set! bit-counts i (+ (vector-ref bit-counts i) 1)))))
    (let loop ([i 1] [ans 0])
      (if (> i k)
          ans
          (let* ([final-num (for/fold ([val 0])
                                       ([bit (in-range 31)])
                               (if (>= (vector-ref bit-counts bit) i)
                                   (bitwise-ior val (arithmetic-shift 1 bit))
                                   val))]
                 [sq (* final-num final-num)])
            (loop (+ i 1) (remainder (+ ans sq) mod-val)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_sum(Nums :: [integer()], K :: integer()) -> integer().
max_sum(Nums, K) ->
    Counts = count_all_bits(Nums, {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}),
    calculate_sum_simple(1, K, 0, Counts, 1000000007).

count_all_bits([], Acc) -> Acc;
count_all_bits([H|T], Acc) ->
    count_all_bits(T, update_counts(H, 0, Acc)).

update_counts(0, _, Acc) -> Acc;
update_counts(N, Bit, Acc) ->
    NewAcc = if (N band 1) == 1 ->
        setelement(Bit + 1, Acc, element(Bit + 1, Acc) + 1);
    true ->
        Acc
    end,
    update_counts(N bsr 1, Bit + 1, NewAcc).

calculate_sum_simple(I, K, Ans, Counts, MOD) when I =< K ->
    Num = build_num_simple(I, 0, 0, Counts),
    NewAns = (Ans + (Num * Num)) rem MOD,
    calculate_sum_simple(I + 1, K, NewAns, Counts, MOD);
calculate_sum_simple(_, _, Ans, _, _) -> Ans.

build_num_simple(_, 31, Num, _Counts) -> Num;
build_num_simple(I, Bit, Num, Counts) ->
    NewNum = if element(Bit + 1, Counts) >= I ->
        Num bor (1 bsl Bit);
    true ->
        Num
    end,
    build_num_simple(I, Bit + 1, NewNum, Counts).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  import Bitwise

  @spec max_sum(nums :: [integer], k :: integer) :: integer
  def max_sum(nums, k) do
    initial_counts = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
    counts = Enum.reduce(nums, initial_counts, fn num, acc ->
      count_bits(num, 0, acc)
    end)

    mod_val = 1_000_000_007

    Enum.reduce(1..k, 0, fn i, total_sum ->
      num = build_num_simple(i, 0, 0, counts)
      rem(total_sum + num * num, mod_val)
    end)
  end

  defp count_bits(0, _, acc), do: acc
  defp count_bits(num, bit, acc) do
    new_acc = if (num &&& 1) == 1 do
      put_elem(acc, bit, elem(acc, bit) + 1)
    else
      acc
    end
    count_bits(num >>> 1, bit + 1, new_acc)
  end

  defp build_num_simple(_i, 31, num, _counts), do: num
  defp build_num_simple(i, bit, num, counts) do
    if elem(counts, bit) >= i do
      build_num_simple(i, bit + 1, num ||| (1 <<< bit), counts)
    else
      build_num_simple(i, bit + 1, num, counts)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * log(max(nums))) where N is the length of the array. We iterate through the array once to count the bits (O(N * 30)) and then iterate k times to construct the k largest numbers (O(k * 30)). Since k is at most N, the complexity simplifies to O(N).
- **Space Complexity:** O(log(max(nums))) to store the frequency of set bits at each bit position. In this case, it is O(31), which is constant space O(1).
