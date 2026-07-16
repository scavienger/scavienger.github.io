---
layout: post
title: "Sum of GCD of Formed Pairs"
date: 2026-07-16 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Two Pointers", "Sorting", "Simulation", "Number Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass\
        \ Solution {\npublic:\n    long long gcdSum(vector<int>& nums) {\n        int\
        \ n = nums.size();\n        vector<int> prefixGcd(n);\n        int mx = 0;\n\
        \        for (int i = 0; i < n; i++) {\n            if (nums[i] > mx) mx = nums[i];\n\
        \            prefixGcd[i] = (int)calcGcd(nums[i], mx);\n        }\n        sort(prefixGcd.begin(),\
        \ prefixGcd.end());\n        long long totalSum = 0;\n        for (int i = 0;\
        \ i < n / 2; i++) {\n            totalSum += calcGcd(prefixGcd[i], prefixGcd[n\
        \ - 1 - i]);\n        }\n        return totalSum;\n    }\n\nprivate:\n    long\
        \ long calcGcd(long long a, long long b) {\n        while (b != 0) {\n     \
        \       long long temp = b;\n            b = a % b;\n            a = temp;\n\
        \        }\n        return a;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public long gcdSum(int[]\
        \ nums) {\n        int n = nums.length;\n        int[] prefixGcd = new int[n];\n\
        \        int mx = 0;\n        for (int i = 0; i < n; i++) {\n            if\
        \ (nums[i] > mx) mx = nums[i];\n            prefixGcd[i] = (int) getGcd(nums[i],\
        \ mx);\n        }\n        Arrays.sort(prefixGcd);\n        long totalSum =\
        \ 0;\n        for (int i = 0; i < n / 2; i++) {\n            totalSum += getGcd(prefixGcd[i],\
        \ prefixGcd[n - 1 - i]);\n        }\n        return totalSum;\n    }\n\n   \
        \ private long getGcd(long a, long b) {\n        while (b != 0) {\n        \
        \    long temp = b;\n            b = a % b;\n            a = temp;\n       \
        \ }\n        return a;\n    }\n}"
      python: "class Solution(object):\n    def gcdSum(self, nums):\n        \"\"\"\n\
        \        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n      \
        \  def get_gcd(a, b):\n            while b:\n                a, b = b, a % b\n\
        \            return a\n\n        n = len(nums)\n        prefixGcd = []\n   \
        \     mx = 0\n        for x in nums:\n            if x > mx:\n             \
        \   mx = x\n            prefixGcd.append(get_gcd(x, mx))\n\n        prefixGcd.sort()\n\
        \        total_sum = 0\n        for i in range(n // 2):\n            a = prefixGcd[i]\n\
        \            b = prefixGcd[n - 1 - i]\n            total_sum += get_gcd(a, b)\n\
        \n        return total_sum"
      python3: "import math\n\nclass Solution:\n    def gcdSum(self, nums: list[int])\
        \ -> int:\n        n = len(nums)\n        prefixGcd = [0] * n\n        mx =\
        \ 0\n        for i in range(n):\n            if nums[i] > mx:\n            \
        \    mx = nums[i]\n            prefixGcd[i] = math.gcd(nums[i], mx)\n\n    \
        \    prefixGcd.sort()\n        total_sum = 0\n        for i in range(n // 2):\n\
        \            total_sum += math.gcd(prefixGcd[i], prefixGcd[n - 1 - i])\n\n \
        \       return total_sum"
      c: '#include <stdlib.h>


        long long find_gcd(long long a, long long b) {

        while (b != 0) {

        long long temp = b;

        b = a % b;

        a = temp;

        }

        return a;

        }


        int compare_ints(const void* a, const void* b) {

        int arg1 = *(const int*)a;

        int arg2 = *(const int*)b;

        if (arg1 < arg2) return -1;

        if (arg1 > arg2) return 1;

        return 0;

        }


        long long gcdSum(int* nums, int numsSize) {

        if (numsSize == 0) return 0;

        int* prefixGcd = (int*)malloc(numsSize * sizeof(int));

        int mx = 0;

        int i;

        for (i = 0; i < numsSize; i++) {

        if (nums[i] > mx) mx = nums[i];

        prefixGcd[i] = (int)find_gcd((long long)nums[i], (long long)mx);

        }


        qsort(prefixGcd, numsSize, sizeof(int), compare_ints);


        long long totalSum = 0;

        for (i = 0; i < numsSize / 2; i++) {

        totalSum += find_gcd((long long)prefixGcd[i], (long long)prefixGcd[numsSize
        - 1 - i]);

        }


        free(prefixGcd);

        return totalSum;

        }'
      csharp: "public class Solution {\n    public long GcdSum(int[] nums) {\n     \
        \   int n = nums.Length;\n        int[] prefixGcd = new int[n];\n        int\
        \ currentMax = 0;\n        for (int i = 0; i < n; i++) {\n            if (nums[i]\
        \ > currentMax) {\n                currentMax = nums[i];\n            }\n  \
        \          prefixGcd[i] = (int)GetGcd(nums[i], currentMax);\n        }\n\n \
        \       System.Array.Sort(prefixGcd);\n\n        long totalSum = 0;\n      \
        \  int left = 0, right = n - 1;\n        while (left < right) {\n          \
        \  totalSum += GetGcd(prefixGcd[left], prefixGcd[right]);\n            left++;\n\
        \            right--;\n        }\n        return totalSum;\n    }\n\n    private\
        \ long GetGcd(long a, long b) {\n        while (b != 0) {\n            a %=\
        \ b;\n            long temp = a;\n            a = b;\n            b = temp;\n\
        \        }\n        return a;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar gcdSum\
        \ = function(nums) {\n    const gcd = (a, b) => {\n        while (b) {\n   \
        \         a %= b;\n            let temp = a;\n            a = b;\n         \
        \   b = temp;\n        }\n        return a;\n    };\n\n    const n = nums.length;\n\
        \    const prefixGcd = new Int32Array(n);\n    let currentMax = 0;\n\n    for\
        \ (let i = 0; i < n; i++) {\n        if (nums[i] > currentMax) {\n         \
        \   currentMax = nums[i];\n        }\n        prefixGcd[i] = gcd(nums[i], currentMax);\n\
        \    }\n\n    prefixGcd.sort();\n\n    let totalSum = 0;\n    let left = 0;\n\
        \    let right = n - 1;\n\n    while (left < right) {\n        totalSum += gcd(prefixGcd[left],\
        \ prefixGcd[right]);\n        left++;\n        right--;\n    }\n\n    return\
        \ totalSum;\n};"
      typescript: "function gcdSum(nums: number[]): number {\n    const gcd = (a: number,\
        \ b: number): number => {\n        while (b) {\n            a %= b;\n      \
        \      let temp = a;\n            a = b;\n            b = temp;\n        }\n\
        \        return a;\n    };\n\n    const n = nums.length;\n    const prefixGcd:\
        \ number[] = new Array(n);\n    let currentMax = 0;\n\n    for (let i = 0; i\
        \ < n; i++) {\n        if (nums[i] > currentMax) {\n            currentMax =\
        \ nums[i];\n        }\n        prefixGcd[i] = gcd(nums[i], currentMax);\n  \
        \  }\n\n    prefixGcd.sort((a, b) => a - b);\n\n    let totalSum = 0;\n    let\
        \ left = 0;\n    let right = n - 1;\n\n    while (left < right) {\n        totalSum\
        \ += gcd(prefixGcd[left], prefixGcd[right]);\n        left++;\n        right--;\n\
        \    }\n\n    return totalSum;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function gcdSum($nums) {\n        $n = count($nums);\n\
        \        $prefixGcd = [];\n        $currentMax = 0;\n\n        for ($i = 0;\
        \ $i < $n; $i++) {\n            if ($nums[$i] > $currentMax) {\n           \
        \     $currentMax = $nums[$i];\n            }\n            $prefixGcd[] = $this->gcd($nums[$i],\
        \ $currentMax);\n        }\n\n        sort($prefixGcd);\n\n        $totalSum\
        \ = 0;\n        $left = 0;\n        $right = $n - 1;\n\n        while ($left\
        \ < $right) {\n            $totalSum += $this->gcd($prefixGcd[$left], $prefixGcd[$right]);\n\
        \            $left++;\n            $right--;\n        }\n\n        return $totalSum;\n\
        \    }\n\n    private function gcd($a, $b) {\n        while ($b != 0) {\n  \
        \          $a %= $b;\n            $temp = $a;\n            $a = $b;\n      \
        \      $b = $temp;\n        }\n        return $a;\n    }\n}"
      swift: "class Solution {\n    func gcdSum(_ nums: [Int]) -> Int {\n        let\
        \ n = nums.count\n        var prefixGcd = [Int]()\n        var currentMax =\
        \ 0\n\n        for i in 0..<n {\n            if nums[i] > currentMax {\n   \
        \             currentMax = nums[i]\n            }\n            prefixGcd.append(gcd(nums[i],\
        \ currentMax))\n        }\n\n        prefixGcd.sort()\n\n        var totalSum\
        \ = 0\n        var left = 0\n        var right = n - 1\n\n        while left\
        \ < right {\n            totalSum += gcd(prefixGcd[left], prefixGcd[right])\n\
        \            left += 1\n            right -= 1\n        }\n\n        return\
        \ totalSum\n    }\n\n    private func gcd(_ a: Int, _ b: Int) -> Int {\n   \
        \     var x = a\n        var y = b\n        while y != 0 {\n            x %=\
        \ y\n            let temp = x\n            x = y\n            y = temp\n   \
        \     }\n        return x\n    }\n}"
      kotlin: "class Solution {\n    fun gcdSum(nums: IntArray): Long {\n        val\
        \ n = nums.size\n        val pg = IntArray(n)\n        var mx = 0\n        for\
        \ (i in 0 until n) {\n            if (nums[i] > mx) {\n                mx =\
        \ nums[i]\n            }\n            pg[i] = gcd(nums[i], mx)\n        }\n\
        \        pg.sort()\n        var sum = 0L\n        var l = 0\n        var r =\
        \ n - 1\n        while (l < r) {\n            sum += gcd(pg[l], pg[r]).toLong()\n\
        \            l++\n            r--\n        }\n        return sum\n    }\n\n\
        \    private fun gcd(a: Int, b: Int): Int {\n        var x = a\n        var\
        \ y = b\n        while (y != 0) {\n            val t = y\n            y = x\
        \ % y\n            x = t\n        }\n        return x\n    }\n}"
      dart: "class Solution {\n  int gcdSum(List<int> nums) {\n    int n = nums.length;\n\
        \    List<int> pg = List<int>.filled(n, 0);\n    int mx = 0;\n    for (int i\
        \ = 0; i < n; i++) {\n      if (nums[i] > mx) {\n        mx = nums[i];\n   \
        \   }\n      pg[i] = _gcd(nums[i], mx);\n    }\n    pg.sort();\n    int sum\
        \ = 0;\n    int l = 0;\n    int r = n - 1;\n    while (l < r) {\n      sum +=\
        \ _gcd(pg[l], pg[r]);\n      l++;\n      r--;\n    }\n    return sum;\n  }\n\
        \n  int _gcd(int a, int b) {\n    while (b != 0) {\n      int t = b;\n     \
        \ b = a % b;\n      a = t;\n    }\n    return a;\n  }\n}"
      go: "import (\n\t\"sort\"\n)\n\nfunc gcdSum(nums []int) int64 {\n\tn := len(nums)\n\
        \tpg := make([]int, n)\n\tmx := 0\n\tfor i, v := range nums {\n\t\tif v > mx\
        \ {\n\t\t\tmx = v\n\t\t}\n\t\tpg[i] = gcd(v, mx)\n\t}\n\tsort.Ints(pg)\n\tvar\
        \ sum int64 = 0\n\tl, r := 0, n-1\n\tfor l < r {\n\t\tsum += int64(gcd(pg[l],\
        \ pg[r]))\n\t\tl++\n\t\tr--\n\t}\n\treturn sum\n}\n\nfunc gcd(a, b int) int\
        \ {\n\tfor b != 0 {\n\t\ta, b = b, a%b\n\t}\n\treturn a\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef gcd_sum(nums)\n  n\
        \ = nums.length\n  pg = Array.new(n)\n  mx = 0\n  nums.each_with_index do |v,\
        \ i|\n    mx = v if v > mx\n    pg[i] = v.gcd(mx)\n  end\n  pg.sort!\n  sum\
        \ = 0\n  l, r = 0, n - 1\n  while l < r\n    sum += pg[l].gcd(pg[r])\n    l\
        \ += 1\n    r -= 1\n  end\n  sum\nend"
      scala: "object Solution {\n  def gcdSum(nums: Array[Int]): Long = {\n    val n\
        \ = nums.length\n    val pg = new Array[Int](n)\n    var mx = 0\n    for (i\
        \ <- 0 until n) {\n      if (nums(i) > mx) {\n        mx = nums(i)\n      }\n\
        \      pg(i) = gcd(nums(i), mx)\n    }\n    val sortedPg = pg.sorted\n    var\
        \ totalSum: Long = 0L\n    var l = 0\n    var r = n - 1\n    while (l < r) {\n\
        \      totalSum += gcd(sortedPg(l), sortedPg(r)).toLong\n      l += 1\n    \
        \  r -= 1\n    }\n    totalSum\n  }\n\n  private def gcd(a: Int, b: Int): Int\
        \ = {\n    var x = a\n    var y = b\n    while (y != 0) {\n      val t = y\n\
        \      y = x % y\n      x = t\n    }\n    x\n  }\n}"
      rust: "impl Solution {\n    pub fn gcd_sum(nums: Vec<i32>) -> i64 {\n        let\
        \ n = nums.len();\n        let mut prefix_gcd: Vec<i64> = Vec::with_capacity(n);\n\
        \        let mut current_max: i64 = 0;\n\n        fn gcd(mut a: i64, mut b:\
        \ i64) -> i64 {\n            while b != 0 {\n                a %= b;\n     \
        \           std::mem::swap(&mut a, &mut b);\n            }\n            a\n\
        \        }\n\n        for &num in &nums {\n            let num_64 = num as i64;\n\
        \            if num_64 > current_max {\n                current_max = num_64;\n\
        \            }\n            prefix_gcd.push(gcd(num_64, current_max));\n   \
        \     }\n\n        prefix_gcd.sort_unstable();\n\n        let mut total_sum:\
        \ i64 = 0;\n        if n > 1 {\n            let mut left = 0;\n            let\
        \ mut right = n - 1;\n            while left < right {\n                total_sum\
        \ += gcd(prefix_gcd[left], prefix_gcd[right]);\n                left += 1;\n\
        \                right -= 1;\n            }\n        }\n        total_sum\n\
        \    }\n}"
      racket: "(define/contract (gcd-sum nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([n (length nums)]\n         [prefix-gcd (let loop ([lst nums] [cur-max\
        \ -1] [acc '()])\n                       (if (null? lst)\n                 \
        \          (reverse acc)\n                           (let* ([num (car lst)]\n\
        \                                  [new-max (max cur-max num)]\n           \
        \                       [g (gcd num new-max)])\n                           \
        \  (loop (cdr lst) new-max (cons g acc)))))]\n         [sorted-gcd (list->vector\
        \ (sort prefix-gcd <))])\n    (let loop ([left 0] [right (- n 1)] [sum 0])\n\
        \      (if (< left right)\n          (let* ([val-left (vector-ref sorted-gcd\
        \ left)]\n                 [val-right (vector-ref sorted-gcd right)])\n    \
        \        (loop (+ left 1) (- right 1) (+ sum (gcd val-left val-right))))\n \
        \         sum))))"
      erlang: "-spec gcd_sum(Nums :: [integer()]) -> integer().\ngcd_sum(Nums) ->\n\
        \    {PrefixGcd, _} = lists:foldl(fun(Num, {Acc, CurMax}) ->\n        NewMax\
        \ = max(Num, CurMax),\n        {[gcd(Num, NewMax) | Acc], NewMax}\n    end,\
        \ {[], 0}, Nums),\n    SortedGcd = lists:sort(PrefixGcd),\n    Len = length(SortedGcd),\n\
        \    pair_sum(SortedGcd, lists:reverse(SortedGcd), Len div 2, 0).\n\ngcd(A,\
        \ 0) -> A;\ngcd(A, B) -> gcd(B, A rem B).\n\npair_sum(_, _, 0, Acc) -> Acc;\n\
        pair_sum([H1|T1], [H2|T2], Count, Acc) ->\n    pair_sum(T1, T2, Count - 1, Acc\
        \ + gcd(H1, H2))."
      elixir: "defmodule Solution do\n  @spec gcd_sum(nums :: [integer]) :: integer\n\
        \  def gcd_sum(nums) do\n    {prefix_gcd, _} = Enum.reduce(nums, {[], 0}, fn\
        \ num, {acc, cur_max} ->\n      new_max = max(num, cur_max)\n      {[gcd(num,\
        \ new_max) | acc], new_max}\n    end)\n\n    sorted_gcd = Enum.sort(prefix_gcd)\n\
        \    n = length(sorted_gcd)\n    num_pairs = div(n, 2)\n\n    left_part = Enum.take(sorted_gcd,\
        \ num_pairs)\n    right_part = sorted_gcd |> Enum.reverse() |> Enum.take(num_pairs)\n\
        \n    Enum.zip(left_part, right_part)\n    |> Enum.reduce(0, fn {a, b}, acc\
        \ -> acc + gcd(a, b) end)\n  end\n\n  defp gcd(a, 0), do: a\n  defp gcd(a, b),\
        \ do: gcd(b, rem(a, b))\nend"
    approach: 'The algorithm first computes the `prefixGcd` array by iterating through
      the input `nums` and calculating the greatest common divisor of each number with
      the running maximum of all numbers seen so far. This step requires a linear pass
      where `prefixGcd[i] = gcd(nums[i], max(nums[0...i]))`. Since the maximum value
      up to any index $i$ is at most $10^9$, each GCD operation takes logarithmic time
      relative to the magnitude of the numbers. After constructing the `prefixGcd` array,
      it is sorted in non-decreasing order to facilitate the specified pairing process.


      Following the sorting, the algorithm forms pairs by picking the smallest and largest
      remaining elements from the `prefixGcd` array (moving inward from both ends).
      For each pair $(a, b)$, it computes $gcd(a, b)$ and adds the result to a running
      total sum. If the length of the array $n$ is odd, the central element is left
      unpaired and ignored as per the problem requirements. The use of a 64-bit integer
      (e.g., `long long` in C++ or `long` in Java) is necessary for the final sum to
      prevent overflow, as the sum can reach approximately $5 \times 10^{13}$.'
    time_complexity: O(n \log n + n \log M) where $n$ is the length of the input array
      and $M$ is the maximum value in `nums`. Computing the `prefixGcd` array takes
      $O(n \log M)$, sorting it takes $O(n \log n)$, and calculating the GCD of the
      $n/2$ pairs takes another $O(n \log M)$.
    space_complexity: O(n) because we allocate a separate array of size $n$ to store
      the `prefixGcd` values before sorting them. Additional space used for recursion
      or sorting overhead is generally $O(\log n)$ or $O(1)$.
    elapsed_time: 236.86256766319275
    model: gemini-3-flash-preview
    generated_at: '2026-07-16 01:58:14 '
---

## Problem #3867: Sum of GCD of Formed Pairs

**Difficulty:** Medium

**Topics:** Array, Math, Two Pointers, Sorting, Simulation, Number Theory

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code>.</p>

<p>Construct an array <code>prefixGcd</code> where for each index <code>i</code>:</p>

<ul>
	<li>Let <code>mx<sub>i</sub> = max(nums[0], nums[1], ..., nums[i])</code>.</li>
	<li><code>prefixGcd[i] = gcd(nums[i], mx<sub>i</sub>)</code>.</li>
</ul>

<p>After constructing <code>prefixGcd</code>:</p>

<ul>
	<li>Sort <code>prefixGcd</code> in <strong>non-decreasing</strong> order.</li>
	<li>Form pairs by taking the <strong>smallest unpaired</strong> element and the <strong>largest unpaired</strong> element.</li>
	<li>Repeat this process until no more pairs can be formed.</li>
	<li>For each formed pair, <strong>compute</strong> the <code>gcd</code> of the two elements.</li>
	<li>If <code>n</code> is odd, the <strong>middle</strong> element in the <code>prefixGcd</code> array remains <strong>unpaired</strong> and should be ignored.</li>
</ul>

<p>Return an integer denoting the <strong>sum of the GCD</strong> values of all formed pairs.</p>
The term <code>gcd(a, b)</code> denotes the <strong>greatest common divisor</strong> of <code>a</code> and <code>b</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,6,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Construct <code>prefixGcd</code>:</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>nums[i]</code></th>
			<th style="border: 1px solid black;"><code>mx<sub>i</sub></code></th>
			<th style="border: 1px solid black;"><code>prefixGcd[i]</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

<p><code>prefixGcd = [2, 6, 2]</code>. After sorting, it forms <code>[2, 2, 6]</code>.</p>

<p>Pair the smallest and largest elements: <code>gcd(2, 6) = 2</code>. The remaining middle element 2 is ignored. Thus, the sum is 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,6,2,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>Construct <code>prefixGcd</code>:</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>nums[i]</code></th>
			<th style="border: 1px solid black;"><code>mx<sub>i</sub></code></th>
			<th style="border: 1px solid black;"><code>prefixGcd[i]</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">8</td>
			<td style="border: 1px solid black;">8</td>
			<td style="border: 1px solid black;">8</td>
		</tr>
	</tbody>
</table>

<p><code>prefixGcd = [3, 6, 2, 8]</code>. After sorting, it forms <code>[2, 3, 6, 8]</code>.</p>

<p>Form pairs: <code>gcd(2, 8) = 2</code> and <code>gcd(3, 6) = 3</code>. Thus, the sum is <code>2 + 3 = 5</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>​​​​​​​9</sup></code></li>
</ul>


## Hints

1. Maintain a running prefix maximum `mx_i` while iterating nums to compute `prefixGcd[i] = gcd(nums[i], mx_i)`.

2. Sort `prefixGcd` in non-decreasing order.

3. Form pairs by combining smallest unpaired and largest unpaired elements.

4. Compute gcd for each pair and sum them; ignore middle element if `n` is odd.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm first computes the `prefixGcd` array by iterating through the input `nums` and calculating the greatest common divisor of each number with the running maximum of all numbers seen so far. This step requires a linear pass where `prefixGcd[i] = gcd(nums[i], max(nums[0...i]))`. Since the maximum value up to any index $i$ is at most $10^9$, each GCD operation takes logarithmic time relative to the magnitude of the numbers. After constructing the `prefixGcd` array, it is sorted in non-decreasing order to facilitate the specified pairing process.

Following the sorting, the algorithm forms pairs by picking the smallest and largest remaining elements from the `prefixGcd` array (moving inward from both ends). For each pair $(a, b)$, it computes $gcd(a, b)$ and adds the result to a running total sum. If the length of the array $n$ is odd, the central element is left unpaired and ignored as per the problem requirements. The use of a 64-bit integer (e.g., `long long` in C++ or `long` in Java) is necessary for the final sum to prevent overflow, as the sum can reach approximately $5 \times 10^{13}$.

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
    long long gcdSum(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefixGcd(n);
        int mx = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > mx) mx = nums[i];
            prefixGcd[i] = (int)calcGcd(nums[i], mx);
        }
        sort(prefixGcd.begin(), prefixGcd.end());
        long long totalSum = 0;
        for (int i = 0; i < n / 2; i++) {
            totalSum += calcGcd(prefixGcd[i], prefixGcd[n - 1 - i]);
        }
        return totalSum;
    }

private:
    long long calcGcd(long long a, long long b) {
        while (b != 0) {
            long long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public long gcdSum(int[] nums) {
        int n = nums.length;
        int[] prefixGcd = new int[n];
        int mx = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > mx) mx = nums[i];
            prefixGcd[i] = (int) getGcd(nums[i], mx);
        }
        Arrays.sort(prefixGcd);
        long totalSum = 0;
        for (int i = 0; i < n / 2; i++) {
            totalSum += getGcd(prefixGcd[i], prefixGcd[n - 1 - i]);
        }
        return totalSum;
    }

    private long getGcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        prefixGcd = []
        mx = 0
        for x in nums:
            if x > mx:
                mx = x
            prefixGcd.append(get_gcd(x, mx))

        prefixGcd.sort()
        total_sum = 0
        for i in range(n // 2):
            a = prefixGcd[i]
            b = prefixGcd[n - 1 - i]
            total_sum += get_gcd(a, b)

        return total_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = [0] * n
        mx = 0
        for i in range(n):
            if nums[i] > mx:
                mx = nums[i]
            prefixGcd[i] = math.gcd(nums[i], mx)

        prefixGcd.sort()
        total_sum = 0
        for i in range(n // 2):
            total_sum += math.gcd(prefixGcd[i], prefixGcd[n - 1 - i])

        return total_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

long long find_gcd(long long a, long long b) {
while (b != 0) {
long long temp = b;
b = a % b;
a = temp;
}
return a;
}

int compare_ints(const void* a, const void* b) {
int arg1 = *(const int*)a;
int arg2 = *(const int*)b;
if (arg1 < arg2) return -1;
if (arg1 > arg2) return 1;
return 0;
}

long long gcdSum(int* nums, int numsSize) {
if (numsSize == 0) return 0;
int* prefixGcd = (int*)malloc(numsSize * sizeof(int));
int mx = 0;
int i;
for (i = 0; i < numsSize; i++) {
if (nums[i] > mx) mx = nums[i];
prefixGcd[i] = (int)find_gcd((long long)nums[i], (long long)mx);
}

qsort(prefixGcd, numsSize, sizeof(int), compare_ints);

long long totalSum = 0;
for (i = 0; i < numsSize / 2; i++) {
totalSum += find_gcd((long long)prefixGcd[i], (long long)prefixGcd[numsSize - 1 - i]);
}

free(prefixGcd);
return totalSum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long GcdSum(int[] nums) {
        int n = nums.Length;
        int[] prefixGcd = new int[n];
        int currentMax = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > currentMax) {
                currentMax = nums[i];
            }
            prefixGcd[i] = (int)GetGcd(nums[i], currentMax);
        }

        System.Array.Sort(prefixGcd);

        long totalSum = 0;
        int left = 0, right = n - 1;
        while (left < right) {
            totalSum += GetGcd(prefixGcd[left], prefixGcd[right]);
            left++;
            right--;
        }
        return totalSum;
    }

    private long GetGcd(long a, long b) {
        while (b != 0) {
            a %= b;
            long temp = a;
            a = b;
            b = temp;
        }
        return a;
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
var gcdSum = function(nums) {
    const gcd = (a, b) => {
        while (b) {
            a %= b;
            let temp = a;
            a = b;
            b = temp;
        }
        return a;
    };

    const n = nums.length;
    const prefixGcd = new Int32Array(n);
    let currentMax = 0;

    for (let i = 0; i < n; i++) {
        if (nums[i] > currentMax) {
            currentMax = nums[i];
        }
        prefixGcd[i] = gcd(nums[i], currentMax);
    }

    prefixGcd.sort();

    let totalSum = 0;
    let left = 0;
    let right = n - 1;

    while (left < right) {
        totalSum += gcd(prefixGcd[left], prefixGcd[right]);
        left++;
        right--;
    }

    return totalSum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function gcdSum(nums: number[]): number {
    const gcd = (a: number, b: number): number => {
        while (b) {
            a %= b;
            let temp = a;
            a = b;
            b = temp;
        }
        return a;
    };

    const n = nums.length;
    const prefixGcd: number[] = new Array(n);
    let currentMax = 0;

    for (let i = 0; i < n; i++) {
        if (nums[i] > currentMax) {
            currentMax = nums[i];
        }
        prefixGcd[i] = gcd(nums[i], currentMax);
    }

    prefixGcd.sort((a, b) => a - b);

    let totalSum = 0;
    let left = 0;
    let right = n - 1;

    while (left < right) {
        totalSum += gcd(prefixGcd[left], prefixGcd[right]);
        left++;
        right--;
    }

    return totalSum;
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
    function gcdSum($nums) {
        $n = count($nums);
        $prefixGcd = [];
        $currentMax = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] > $currentMax) {
                $currentMax = $nums[$i];
            }
            $prefixGcd[] = $this->gcd($nums[$i], $currentMax);
        }

        sort($prefixGcd);

        $totalSum = 0;
        $left = 0;
        $right = $n - 1;

        while ($left < $right) {
            $totalSum += $this->gcd($prefixGcd[$left], $prefixGcd[$right]);
            $left++;
            $right--;
        }

        return $totalSum;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $a %= $b;
            $temp = $a;
            $a = $b;
            $b = $temp;
        }
        return $a;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func gcdSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefixGcd = [Int]()
        var currentMax = 0

        for i in 0..<n {
            if nums[i] > currentMax {
                currentMax = nums[i]
            }
            prefixGcd.append(gcd(nums[i], currentMax))
        }

        prefixGcd.sort()

        var totalSum = 0
        var left = 0
        var right = n - 1

        while left < right {
            totalSum += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        }

        return totalSum
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            x %= y
            let temp = x
            x = y
            y = temp
        }
        return x
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun gcdSum(nums: IntArray): Long {
        val n = nums.size
        val pg = IntArray(n)
        var mx = 0
        for (i in 0 until n) {
            if (nums[i] > mx) {
                mx = nums[i]
            }
            pg[i] = gcd(nums[i], mx)
        }
        pg.sort()
        var sum = 0L
        var l = 0
        var r = n - 1
        while (l < r) {
            sum += gcd(pg[l], pg[r]).toLong()
            l++
            r--
        }
        return sum
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val t = y
            y = x % y
            x = t
        }
        return x
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int gcdSum(List<int> nums) {
    int n = nums.length;
    List<int> pg = List<int>.filled(n, 0);
    int mx = 0;
    for (int i = 0; i < n; i++) {
      if (nums[i] > mx) {
        mx = nums[i];
      }
      pg[i] = _gcd(nums[i], mx);
    }
    pg.sort();
    int sum = 0;
    int l = 0;
    int r = n - 1;
    while (l < r) {
      sum += _gcd(pg[l], pg[r]);
      l++;
      r--;
    }
    return sum;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = b;
      b = a % b;
      a = t;
    }
    return a;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"sort"
)

func gcdSum(nums []int) int64 {
	n := len(nums)
	pg := make([]int, n)
	mx := 0
	for i, v := range nums {
		if v > mx {
			mx = v
		}
		pg[i] = gcd(v, mx)
	}
	sort.Ints(pg)
	var sum int64 = 0
	l, r := 0, n-1
	for l < r {
		sum += int64(gcd(pg[l], pg[r]))
		l++
		r--
	}
	return sum
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def gcd_sum(nums)
  n = nums.length
  pg = Array.new(n)
  mx = 0
  nums.each_with_index do |v, i|
    mx = v if v > mx
    pg[i] = v.gcd(mx)
  end
  pg.sort!
  sum = 0
  l, r = 0, n - 1
  while l < r
    sum += pg[l].gcd(pg[r])
    l += 1
    r -= 1
  end
  sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def gcdSum(nums: Array[Int]): Long = {
    val n = nums.length
    val pg = new Array[Int](n)
    var mx = 0
    for (i <- 0 until n) {
      if (nums(i) > mx) {
        mx = nums(i)
      }
      pg(i) = gcd(nums(i), mx)
    }
    val sortedPg = pg.sorted
    var totalSum: Long = 0L
    var l = 0
    var r = n - 1
    while (l < r) {
      totalSum += gcd(sortedPg(l), sortedPg(r)).toLong
      l += 1
      r -= 1
    }
    totalSum
  }

  private def gcd(a: Int, b: Int): Int = {
    var x = a
    var y = b
    while (y != 0) {
      val t = y
      y = x % y
      x = t
    }
    x
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn gcd_sum(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut prefix_gcd: Vec<i64> = Vec::with_capacity(n);
        let mut current_max: i64 = 0;

        fn gcd(mut a: i64, mut b: i64) -> i64 {
            while b != 0 {
                a %= b;
                std::mem::swap(&mut a, &mut b);
            }
            a
        }

        for &num in &nums {
            let num_64 = num as i64;
            if num_64 > current_max {
                current_max = num_64;
            }
            prefix_gcd.push(gcd(num_64, current_max));
        }

        prefix_gcd.sort_unstable();

        let mut total_sum: i64 = 0;
        if n > 1 {
            let mut left = 0;
            let mut right = n - 1;
            while left < right {
                total_sum += gcd(prefix_gcd[left], prefix_gcd[right]);
                left += 1;
                right -= 1;
            }
        }
        total_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (gcd-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [prefix-gcd (let loop ([lst nums] [cur-max -1] [acc '()])
                       (if (null? lst)
                           (reverse acc)
                           (let* ([num (car lst)]
                                  [new-max (max cur-max num)]
                                  [g (gcd num new-max)])
                             (loop (cdr lst) new-max (cons g acc)))))]
         [sorted-gcd (list->vector (sort prefix-gcd <))])
    (let loop ([left 0] [right (- n 1)] [sum 0])
      (if (< left right)
          (let* ([val-left (vector-ref sorted-gcd left)]
                 [val-right (vector-ref sorted-gcd right)])
            (loop (+ left 1) (- right 1) (+ sum (gcd val-left val-right))))
          sum))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec gcd_sum(Nums :: [integer()]) -> integer().
gcd_sum(Nums) ->
    {PrefixGcd, _} = lists:foldl(fun(Num, {Acc, CurMax}) ->
        NewMax = max(Num, CurMax),
        {[gcd(Num, NewMax) | Acc], NewMax}
    end, {[], 0}, Nums),
    SortedGcd = lists:sort(PrefixGcd),
    Len = length(SortedGcd),
    pair_sum(SortedGcd, lists:reverse(SortedGcd), Len div 2, 0).

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).

pair_sum(_, _, 0, Acc) -> Acc;
pair_sum([H1|T1], [H2|T2], Count, Acc) ->
    pair_sum(T1, T2, Count - 1, Acc + gcd(H1, H2)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec gcd_sum(nums :: [integer]) :: integer
  def gcd_sum(nums) do
    {prefix_gcd, _} = Enum.reduce(nums, {[], 0}, fn num, {acc, cur_max} ->
      new_max = max(num, cur_max)
      {[gcd(num, new_max) | acc], new_max}
    end)

    sorted_gcd = Enum.sort(prefix_gcd)
    n = length(sorted_gcd)
    num_pairs = div(n, 2)

    left_part = Enum.take(sorted_gcd, num_pairs)
    right_part = sorted_gcd |> Enum.reverse() |> Enum.take(num_pairs)

    Enum.zip(left_part, right_part)
    |> Enum.reduce(0, fn {a, b}, acc -> acc + gcd(a, b) end)
  end

  defp gcd(a, 0), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n \log n + n \log M) where $n$ is the length of the input array and $M$ is the maximum value in `nums`. Computing the `prefixGcd` array takes $O(n \log M)$, sorting it takes $O(n \log n)$, and calculating the GCD of the $n/2$ pairs takes another $O(n \log M)$.
- **Space Complexity:** O(n) because we allocate a separate array of size $n$ to store the `prefixGcd` values before sorting them. Additional space used for recursion or sorting overhead is generally $O(\log n)$ or $O(1)$.
