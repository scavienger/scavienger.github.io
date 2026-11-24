---
layout: post
title: "Maximum Subarray With Equal Products"
date: 2026-11-24 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math", "Sliding Window", "Enumeration", "Number Theory"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-subarray-with-equal-products/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long get_gcd(long long a, long long\
        \ b) {\n        while (b) {\n            a %= b;\n            std::swap(a, b);\n\
        \        }\n        return a;\n    }\n\n    int maxLength(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        int res = 0;\n        for (int i\
        \ = 0; i < n; ++i) {\n            long long p = 1;\n            long long g\
        \ = 0;\n            long long l = 0;\n            for (int j = i; j < n; ++j)\
        \ {\n                p *= nums[j];\n                if (p > 25200) break;\n\n\
        \                if (i == j) {\n                    g = nums[i];\n         \
        \           l = nums[i];\n                } else {\n                    g =\
        \ get_gcd(g, (long long)nums[j]);\n                    l = (l * nums[j]) / get_gcd(l,\
        \ (long long)nums[j]);\n                }\n\n                if (p == g * l)\
        \ {\n                    res = std::max(res, j - i + 1);\n                }\n\
        \            }\n        }\n        return res;\n    }\n};"
      java: "class Solution {\n    private long getGcd(long a, long b) {\n        while\
        \ (b != 0) {\n            long temp = b;\n            b = a % b;\n         \
        \   a = temp;\n        }\n        return a;\n    }\n\n    public int maxLength(int[]\
        \ nums) {\n        int n = nums.length;\n        int res = 0;\n        for (int\
        \ i = 0; i < n; i++) {\n            long p = 1;\n            long g = 0;\n \
        \           long l = 0;\n            for (int j = i; j < n; j++) {\n       \
        \         p *= nums[j];\n                if (p > 25200) break;\n\n         \
        \       if (i == j) {\n                    g = nums[i];\n                  \
        \  l = nums[i];\n                } else {\n                    g = getGcd(g,\
        \ (long) nums[j]);\n                    l = (l * nums[j]) / getGcd(l, (long)\
        \ nums[j]);\n                }\n\n                if (p == g * l) {\n      \
        \              res = Math.max(res, j - i + 1);\n                }\n        \
        \    }\n        }\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def maxLength(self, nums):\n        \"\"\
        \"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n   \
        \     def get_gcd(a, b):\n            while b:\n                a, b = b, a\
        \ % b\n            return a\n\n        n = len(nums)\n        res = 0\n    \
        \    for i in range(n):\n            p, g, l = 1, 0, 0\n            for j in\
        \ range(i, n):\n                p *= nums[j]\n                if p > 25200:\
        \ break\n                if g == 0:\n                    g = l = nums[j]\n \
        \               else:\n                    g = get_gcd(g, nums[j])\n       \
        \             l = (l * nums[j]) // get_gcd(l, nums[j])\n                if p\
        \ == g * l:\n                    res = max(res, j - i + 1)\n        return res"
      python3: "class Solution:\n    def maxLength(self, nums: List[int]) -> int:\n\
        \        def get_gcd(a, b):\n            while b:\n                a, b = b,\
        \ a % b\n            return a\n\n        n = len(nums)\n        res = 0\n  \
        \      for i in range(n):\n            p, g, l = 1, 0, 0\n            for j\
        \ in range(i, n):\n                p *= nums[j]\n                if p > 25200:\
        \ break\n                if g == 0:\n                    g = l = nums[j]\n \
        \               else:\n                    g = get_gcd(g, nums[j])\n       \
        \             l = (l * nums[j]) // get_gcd(l, nums[j])\n                if p\
        \ == g * l:\n                    res = max(res, j - i + 1)\n        return res"
      c: "long long get_gcd(long long a, long long b) {\n    while (b) {\n        long\
        \ long temp = b;\n        b = a % b;\n        a = temp;\n    }\n    return a;\n\
        }\n\nint maxLength(int* nums, int numsSize) {\n    int res = 0;\n    for (int\
        \ i = 0; i < numsSize; i++) {\n        long long p = 1;\n        long long g\
        \ = 0;\n        long long l = 0;\n        for (int j = i; j < numsSize; j++)\
        \ {\n            p *= nums[j];\n            if (p > 25200) break;\n\n      \
        \      if (i == j) {\n                g = nums[i];\n                l = nums[i];\n\
        \            } else {\n                g = get_gcd(g, (long long)nums[j]);\n\
        \                l = (l * nums[j]) / get_gcd(l, (long long)nums[j]);\n     \
        \       }\n\n            if (p == g * l) {\n                if (j - i + 1 >\
        \ res) res = j - i + 1;\n            }\n        }\n    }\n    return res;\n}"
      csharp: "public class Solution {\n    private long GetGcd(long a, long b) {\n\
        \        while (b != 0) {\n            long temp = b;\n            b = a % b;\n\
        \            a = temp;\n        }\n        return a;\n    }\n\n    public int\
        \ MaxLength(int[] nums) {\n        int n = nums.Length;\n        int res = 0;\n\
        \        for (int i = 0; i < n; i++) {\n            long p = 1;\n          \
        \  long g = 0;\n            long l = 0;\n            for (int j = i; j < n;\
        \ j++) {\n                p *= nums[j];\n                if (p > 25200) break;\n\
        \n                if (i == j) {\n                    g = nums[i];\n        \
        \            l = nums[i];\n                } else {\n                    g =\
        \ GetGcd(g, (long)nums[j]);\n                    l = (l * nums[j]) / GetGcd(l,\
        \ (long)nums[j]);\n                }\n\n                if (p == g * l) {\n\
        \                    res = Math.Max(res, j - i + 1);\n                }\n  \
        \          }\n        }\n        return res;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maxLength\
        \ = function(nums) {\n    const getGcd = (a, b) => {\n        while (b) {\n\
        \            a %= b;\n            [a, b] = [b, a];\n        }\n        return\
        \ a;\n    };\n\n    let n = nums.length;\n    let res = 0;\n    for (let i =\
        \ 0; i < n; i++) {\n        let p = 1;\n        let g = 0;\n        let l =\
        \ 0;\n        for (let j = i; j < n; j++) {\n            p *= nums[j];\n   \
        \         if (p > 25200) break;\n\n            if (i === j) {\n            \
        \    g = nums[i];\n                l = nums[i];\n            } else {\n    \
        \            g = getGcd(g, nums[j]);\n                l = (l * nums[j]) / getGcd(l,\
        \ nums[j]);\n            }\n\n            if (p === g * l) {\n             \
        \   res = Math.max(res, j - i + 1);\n            }\n        }\n    }\n    return\
        \ res;\n};"
      typescript: "function maxLength(nums: number[]): number {\n    const getGcd =\
        \ (a: number, b: number): number => {\n        while (b !== 0) {\n         \
        \   const temp = b;\n            b = a % b;\n            a = temp;\n       \
        \ }\n        return a;\n    };\n\n    const n = nums.length;\n    let res =\
        \ 0;\n    for (let i = 0; i < n; i++) {\n        let p = 1;\n        let g =\
        \ 0;\n        let l = 0;\n        for (let j = i; j < n; j++) {\n          \
        \  p *= nums[j];\n            if (p > 25200) break;\n            if (g === 0)\
        \ {\n                g = nums[j];\n                l = nums[j];\n          \
        \  } else {\n                g = getGcd(g, nums[j]);\n                l = (l\
        \ * nums[j]) / getGcd(l, nums[j]);\n            }\n            if (p === g *\
        \ l) {\n                res = Math.max(res, j - i + 1);\n            }\n   \
        \     }\n    }\n    return res;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function maxLength($nums) {\n        $getGcd = function($a,\
        \ $b) {\n            while ($b != 0) {\n                $temp = $b;\n      \
        \          $b = $a % $b;\n                $a = $temp;\n            }\n     \
        \       return $a;\n        };\n\n        $n = count($nums);\n        $res =\
        \ 0;\n        for ($i = 0; $i < $n; $i++) {\n            $p = 1;\n         \
        \   $g = 0;\n            $l = 0;\n            for ($j = $i; $j < $n; $j++) {\n\
        \                $p *= $nums[$j];\n                if ($p > 25200) break;\n\
        \                if ($g == 0) {\n                    $g = $l = $nums[$j];\n\
        \                } else {\n                    $g = $getGcd($g, $nums[$j]);\n\
        \                    $l = (int)(($l * $nums[$j]) / $getGcd($l, $nums[$j]));\n\
        \                }\n                if ($p == $g * $l) {\n                 \
        \   $res = max($res, $j - $i + 1);\n                }\n            }\n     \
        \   }\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func maxLength(_ nums: [Int]) -> Int {\n       \
        \ func getGcd(_ a: Int, _ b: Int) -> Int {\n            var x = a\n        \
        \    var y = b\n            while y != 0 {\n                let temp = y\n \
        \               y = x % y\n                x = temp\n            }\n       \
        \     return x\n        }\n\n        let n = nums.count\n        var res = 0\n\
        \        for i in 0..<n {\n            var p = 1\n            var g = 0\n  \
        \          var l = 0\n            for j in i..<n {\n                p *= nums[j]\n\
        \                if p > 25200 { break }\n                if g == 0 {\n     \
        \               g = nums[j]\n                    l = nums[j]\n             \
        \   } else {\n                    g = getGcd(g, nums[j])\n                 \
        \   l = (l * nums[j]) / getGcd(l, nums[j])\n                }\n            \
        \    if p == g * l {\n                    res = max(res, j - i + 1)\n      \
        \          }\n            }\n        }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun maxLength(nums: IntArray): Int {\n        fun\
        \ getGcd(a: Int, b: Int): Int {\n            var x = a\n            var y =\
        \ b\n            while (y != 0) {\n                val temp = y\n          \
        \      y = x % y\n                x = temp\n            }\n            return\
        \ x\n        }\n\n        val n = nums.size\n        var res = 0\n        for\
        \ (i in 0 until n) {\n            var p = 1\n            var g = 0\n       \
        \     var l = 0\n            for (j in i until n) {\n                p *= nums[j]\n\
        \                if (p > 25200) break\n                if (g == 0) {\n     \
        \               g = nums[j]\n                    l = nums[j]\n             \
        \   } else {\n                    g = getGcd(g, nums[j])\n                 \
        \   l = (l * nums[j]) / getGcd(l, nums[j])\n                }\n            \
        \    if (p == g * l) {\n                    val currentLen = j - i + 1\n   \
        \                 if (currentLen > res) res = currentLen\n                }\n\
        \            }\n        }\n        return res\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maxLength(List<int> nums)\
        \ {\n    int getGcd(int a, int b) {\n      while (b != 0) {\n        int temp\
        \ = b;\n        b = a % b;\n        a = temp;\n      }\n      return a;\n  \
        \  }\n\n    int n = nums.length;\n    int res = 0;\n    for (int i = 0; i <\
        \ n; i++) {\n      int p = 1;\n      int g = 0;\n      int l = 0;\n      for\
        \ (int j = i; j < n; j++) {\n        p *= nums[j];\n        if (p > 25200) break;\n\
        \        if (g == 0) {\n          g = nums[j];\n          l = nums[j];\n   \
        \     } else {\n          g = getGcd(g, nums[j]);\n          l = (l * nums[j])\
        \ ~/ getGcd(l, nums[j]);\n        }\n        if (p == g * l) {\n          res\
        \ = max(res, j - i + 1);\n        }\n      }\n    }\n    return res;\n  }\n}"
      go: "func maxLength(nums []int) int {\n\tgetGcd := func(a, b int) int {\n\t\t\
        for b != 0 {\n\t\t\ta, b = b, a%b\n\t\t}\n\t\treturn a\n\t}\n\n\tn := len(nums)\n\
        \tres := 0\n\tfor i := 0; i < n; i++ {\n\t\tp, g, l := 1, 0, 0\n\t\tfor j :=\
        \ i; j < n; j++ {\n\t\t\tp *= nums[j]\n\t\t\tif p > 25200 {\n\t\t\t\tbreak\n\
        \t\t\t}\n\t\t\tif g == 0 {\n\t\t\t\tg, l = nums[j], nums[j]\n\t\t\t} else {\n\
        \t\t\t\tg = getGcd(g, nums[j])\n\t\t\t\tl = (l * nums[j]) / getGcd(l, nums[j])\n\
        \t\t\t}\n\t\t\tif p == g*l {\n\t\t\t\tif j-i+1 > res {\n\t\t\t\t\tres = j -\
        \ i + 1\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\treturn res\n}"
      ruby: "def max_length(nums)\n  n = nums.length\n  res = 0\n  (0...n).each do |i|\n\
        \    p = 1\n    g = 0\n    l = 0\n    (i...n).each do |j|\n      p *= nums[j]\n\
        \      break if p > 25200\n      if g == 0\n        g = l = nums[j]\n      else\n\
        \        g = g.gcd(nums[j])\n        l = (l * nums[j]) / l.gcd(nums[j])\n  \
        \    end\n      res = [res, j - i + 1].max if p == g * l\n    end\n  end\n \
        \ res\nend"
      scala: "object Solution {\n    def maxLength(nums: Array[Int]): Int = {\n    \
        \    def getGcd(a: Long, b: Long): Long = if (b == 0) a else getGcd(b, a % b)\n\
        \n        val n = nums.length\n        var res = 0\n        var i = 0\n    \
        \    while (i < n) {\n            var p: Long = 1\n            var g: Long =\
        \ 0\n            var l: Long = 0\n            var j = i\n            var loopBreak\
        \ = false\n            while (j < n && !loopBreak) {\n                p *= nums[j]\n\
        \                if (p > 25200) {\n                    loopBreak = true\n  \
        \              } else {\n                    if (g == 0) {\n               \
        \         g = nums[j].toLong\n                        l = nums[j].toLong\n \
        \                   } else {\n                        g = getGcd(g, nums[j].toLong)\n\
        \                        l = (l * nums[j]) / getGcd(l, nums[j].toLong)\n   \
        \                 }\n                    if (p == g * l) {\n               \
        \         res = Math.max(res, j - i + 1)\n                    }\n          \
        \          j += 1\n                }\n            }\n            i += 1\n  \
        \      }\n        res\n    }\n}"
      rust: "impl Solution {\n    pub fn max_length(nums: Vec<i32>) -> i32 {\n     \
        \   fn gcd(a: i64, b: i64) -> i64 {\n            let (mut x, mut y) = (a, b);\n\
        \            while y != 0 {\n                x %= y;\n                std::mem::swap(&mut\
        \ x, &mut y);\n            }\n            x\n        }\n\n        let n = nums.len();\n\
        \        let mut res = 0;\n        for i in 0..n {\n            let mut p: i64\
        \ = 1;\n            let mut g: i64 = 0;\n            let mut l: i64 = 0;\n \
        \           for j in i..n {\n                p *= nums[j] as i64;\n        \
        \        if p > 25200 {\n                    break;\n                }\n   \
        \             if g == 0 {\n                    g = nums[j] as i64;\n       \
        \             l = nums[j] as i64;\n                } else {\n              \
        \      let current_val = nums[j] as i64;\n                    g = gcd(g, current_val);\n\
        \                    l = (l * current_val) / gcd(l, current_val);\n        \
        \        }\n                if p == g * l {\n                    res = res.max((j\
        \ - i + 1) as i32);\n                }\n            }\n        }\n        res\n\
        \    }\n}"
      racket: "(define/contract (max-length nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([n (length nums)]\n         [arr (list->vector nums)]\n         [res\
        \ 0])\n    (for ([i (in-range n)])\n      (let loop ([j i] [p 1] [g 0] [l 0])\n\
        \        (when (and (< j n))\n          (let* ([val (vector-ref arr j)]\n  \
        \               [np (* p val)])\n            (when (<= np 25200)\n         \
        \     (let* ([ng (if (= g 0) val (gcd g val))]\n                     [nl (if\
        \ (= l 0) val (lcm l val))])\n                (when (= np (* ng nl))\n     \
        \             (set! res (max res (+ (- j i) 1))))\n                (loop (+\
        \ j 1) np ng nl)))))))\n    res))"
      erlang: "-spec max_length(Nums :: [integer()]) -> integer().\nmax_length(Nums)\
        \ ->\n  Arr = list_to_tuple(Nums),\n  N = tuple_size(Arr),\n  solve_i(1, N,\
        \ Arr, 0).\n\nsolve_i(I, N, Arr, Res) when I > N -> Res;\nsolve_i(I, N, Arr,\
        \ Res) ->\n  NewRes = solve_j(I, I, N, Arr, 1, 0, 0, Res),\n  solve_i(I + 1,\
        \ N, Arr, NewRes).\n\nsolve_j(I, J, N, Arr, P, G, L, Res) when J > N -> Res;\n\
        solve_j(I, J, N, Arr, P, G, L, Res) ->\n  Val = element(J, Arr),\n  NP = P *\
        \ Val,\n  if\n    NP > 25200 -> Res;\n    true ->\n      {NG, NL} = if\n   \
        \     G == 0 -> {Val, Val};\n        true -> \n          GcdVal = gcd(G, Val),\n\
        \          {GcdVal, (L * Val) div gcd(L, Val)}\n      end,\n      NewRes = if\n\
        \        NP == NG * NL -> max(Res, J - I + 1);\n        true -> Res\n      end,\n\
        \      solve_j(I, J + 1, N, Arr, NP, NG, NL, NewRes)\n  end.\n\ngcd(A, 0) ->\
        \ A;\ngcd(A, B) -> gcd(B, A rem B)."
      elixir: "defmodule Solution do\n  @spec max_length(nums :: [integer]) :: integer\n\
        \  def max_length(nums) do\n    n = length(nums)\n    arr = List.to_tuple(nums)\n\
        \    Enum.reduce(0..(n - 1), 0, fn i, res_outer ->\n      solve_j(i, i, n, arr,\
        \ 1, 0, 0, res_outer)\n    end)\n  end\n\n  defp solve_j(i, j, n, arr, p, g,\
        \ l, res) when j < n do\n    val = elem(arr, j)\n    np = p * val\n    if np\
        \ > 25200 do\n      res\n    else\n      {ng, nl} = if g == 0 do\n        {val,\
        \ val}\n      else\n        gcd_val = Integer.gcd(g, val)\n        lcm_val =\
        \ div(l * val, Integer.gcd(l, val))\n        {gcd_val, lcm_val}\n      end\n\
        \      new_res = if np == ng * nl, do: max(res, j - i + 1), else: res\n    \
        \  solve_j(i, j + 1, n, arr, np, ng, nl, new_res)\n    end\n  end\n  defp solve_j(_i,\
        \ _j, _n, _arr, _p, _g, _l, res), do: res\nend"
    approach: 'The problem asks for the longest subarray where the product of its elements
      equals the product of its Least Common Multiple (LCM) and Greatest Common Divisor
      (GCD). We use a nested loop approach to check all possible subarrays. For each
      starting position $i$, we extend the subarray by incrementing $j$ from $i$ to
      $n-1$, maintaining a running product ($p$), running GCD ($g$), and running LCM
      ($l$). The GCD is updated using the Euclidean algorithm, and the LCM is updated
      using the standard formula $LCM(a, b) = (a \times b) / GCD(a, b)$.


      Given that the elements of the array are positive integers between 1 and 10, the
      maximum possible LCM of any subarray is $LCM(1, 2, ..., 10) = 2520$, and the maximum
      possible GCD is 10. Consequently, the maximum possible value for $LCM \times GCD$
      is 25,200. We can optimize the search by terminating the inner loop if the running
      product exceeds this threshold, as $p$ can never equal $l \times g$ once it surpasses
      25,200. This also protects against integer overflow in fixed-width languages.'
    time_complexity: O(N^2 * log(M)) where N is the length of the array and M is the
      maximum value in the array (10). The nested loops iterate over all subarrays,
      and calculating the GCD takes logarithmic time.
    space_complexity: O(1) because we only use a constant amount of extra space for
      the running product, GCD, LCM, and the result variables.
    elapsed_time: 191.01982712745667
    model: gemini-3-flash-preview
    generated_at: '2026-11-24 07:51:39 '
---

## Problem #3411: Maximum Subarray With Equal Products

**Difficulty:** Easy

**Topics:** Array, Math, Sliding Window, Enumeration, Number Theory

## Problem Description

<p>You are given an array of <strong>positive</strong> integers <code>nums</code>.</p>

<p>An array <code>arr</code> is called <strong>product equivalent</strong> if <code>prod(arr) == lcm(arr) * gcd(arr)</code>, where:</p>

<ul>
	<li><code>prod(arr)</code> is the product of all elements of <code>arr</code>.</li>
	<li><code>gcd(arr)</code> is the <span data-keyword="gcd-function">GCD</span> of all elements of <code>arr</code>.</li>
	<li><code>lcm(arr)</code> is the <span data-keyword="lcm-function">LCM</span> of all elements of <code>arr</code>.</li>
</ul>

<p>Return the length of the <strong>longest</strong> <strong>product equivalent</strong> <span data-keyword="subarray-nonempty">subarray</span> of <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,2,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong>&nbsp;</p>

<p>The longest product equivalent subarray is <code>[1, 2, 1, 1, 1]</code>, where&nbsp;<code>prod([1, 2, 1, 1, 1]) = 2</code>,&nbsp;<code>gcd([1, 2, 1, 1, 1]) = 1</code>, and&nbsp;<code>lcm([1, 2, 1, 1, 1]) = 2</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,4,5,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong>&nbsp;</p>

<p>The longest product equivalent subarray is <code>[3, 4, 5].</code></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1,4,5,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10</code></li>
</ul>


## Hints

1. What is the maximum possible lcm?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the longest subarray where the product of its elements equals the product of its Least Common Multiple (LCM) and Greatest Common Divisor (GCD). We use a nested loop approach to check all possible subarrays. For each starting position $i$, we extend the subarray by incrementing $j$ from $i$ to $n-1$, maintaining a running product ($p$), running GCD ($g$), and running LCM ($l$). The GCD is updated using the Euclidean algorithm, and the LCM is updated using the standard formula $LCM(a, b) = (a \times b) / GCD(a, b)$.

Given that the elements of the array are positive integers between 1 and 10, the maximum possible LCM of any subarray is $LCM(1, 2, ..., 10) = 2520$, and the maximum possible GCD is 10. Consequently, the maximum possible value for $LCM \times GCD$ is 25,200. We can optimize the search by terminating the inner loop if the running product exceeds this threshold, as $p$ can never equal $l \times g$ once it surpasses 25,200. This also protects against integer overflow in fixed-width languages.

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
    long long get_gcd(long long a, long long b) {
        while (b) {
            a %= b;
            std::swap(a, b);
        }
        return a;
    }

    int maxLength(vector<int>& nums) {
        int n = nums.size();
        int res = 0;
        for (int i = 0; i < n; ++i) {
            long long p = 1;
            long long g = 0;
            long long l = 0;
            for (int j = i; j < n; ++j) {
                p *= nums[j];
                if (p > 25200) break;

                if (i == j) {
                    g = nums[i];
                    l = nums[i];
                } else {
                    g = get_gcd(g, (long long)nums[j]);
                    l = (l * nums[j]) / get_gcd(l, (long long)nums[j]);
                }

                if (p == g * l) {
                    res = std::max(res, j - i + 1);
                }
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
    private long getGcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int maxLength(int[] nums) {
        int n = nums.length;
        int res = 0;
        for (int i = 0; i < n; i++) {
            long p = 1;
            long g = 0;
            long l = 0;
            for (int j = i; j < n; j++) {
                p *= nums[j];
                if (p > 25200) break;

                if (i == j) {
                    g = nums[i];
                    l = nums[i];
                } else {
                    g = getGcd(g, (long) nums[j]);
                    l = (l * nums[j]) / getGcd(l, (long) nums[j]);
                }

                if (p == g * l) {
                    res = Math.max(res, j - i + 1);
                }
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
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        res = 0
        for i in range(n):
            p, g, l = 1, 0, 0
            for j in range(i, n):
                p *= nums[j]
                if p > 25200: break
                if g == 0:
                    g = l = nums[j]
                else:
                    g = get_gcd(g, nums[j])
                    l = (l * nums[j]) // get_gcd(l, nums[j])
                if p == g * l:
                    res = max(res, j - i + 1)
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        res = 0
        for i in range(n):
            p, g, l = 1, 0, 0
            for j in range(i, n):
                p *= nums[j]
                if p > 25200: break
                if g == 0:
                    g = l = nums[j]
                else:
                    g = get_gcd(g, nums[j])
                    l = (l * nums[j]) // get_gcd(l, nums[j])
                if p == g * l:
                    res = max(res, j - i + 1)
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long get_gcd(long long a, long long b) {
    while (b) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int maxLength(int* nums, int numsSize) {
    int res = 0;
    for (int i = 0; i < numsSize; i++) {
        long long p = 1;
        long long g = 0;
        long long l = 0;
        for (int j = i; j < numsSize; j++) {
            p *= nums[j];
            if (p > 25200) break;

            if (i == j) {
                g = nums[i];
                l = nums[i];
            } else {
                g = get_gcd(g, (long long)nums[j]);
                l = (l * nums[j]) / get_gcd(l, (long long)nums[j]);
            }

            if (p == g * l) {
                if (j - i + 1 > res) res = j - i + 1;
            }
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
    private long GetGcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int MaxLength(int[] nums) {
        int n = nums.Length;
        int res = 0;
        for (int i = 0; i < n; i++) {
            long p = 1;
            long g = 0;
            long l = 0;
            for (int j = i; j < n; j++) {
                p *= nums[j];
                if (p > 25200) break;

                if (i == j) {
                    g = nums[i];
                    l = nums[i];
                } else {
                    g = GetGcd(g, (long)nums[j]);
                    l = (l * nums[j]) / GetGcd(l, (long)nums[j]);
                }

                if (p == g * l) {
                    res = Math.Max(res, j - i + 1);
                }
            }
        }
        return res;
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
var maxLength = function(nums) {
    const getGcd = (a, b) => {
        while (b) {
            a %= b;
            [a, b] = [b, a];
        }
        return a;
    };

    let n = nums.length;
    let res = 0;
    for (let i = 0; i < n; i++) {
        let p = 1;
        let g = 0;
        let l = 0;
        for (let j = i; j < n; j++) {
            p *= nums[j];
            if (p > 25200) break;

            if (i === j) {
                g = nums[i];
                l = nums[i];
            } else {
                g = getGcd(g, nums[j]);
                l = (l * nums[j]) / getGcd(l, nums[j]);
            }

            if (p === g * l) {
                res = Math.max(res, j - i + 1);
            }
        }
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxLength(nums: number[]): number {
    const getGcd = (a: number, b: number): number => {
        while (b !== 0) {
            const temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    const n = nums.length;
    let res = 0;
    for (let i = 0; i < n; i++) {
        let p = 1;
        let g = 0;
        let l = 0;
        for (let j = i; j < n; j++) {
            p *= nums[j];
            if (p > 25200) break;
            if (g === 0) {
                g = nums[j];
                l = nums[j];
            } else {
                g = getGcd(g, nums[j]);
                l = (l * nums[j]) / getGcd(l, nums[j]);
            }
            if (p === g * l) {
                res = Math.max(res, j - i + 1);
            }
        }
    }
    return res;
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
    function maxLength($nums) {
        $getGcd = function($a, $b) {
            while ($b != 0) {
                $temp = $b;
                $b = $a % $b;
                $a = $temp;
            }
            return $a;
        };

        $n = count($nums);
        $res = 0;
        for ($i = 0; $i < $n; $i++) {
            $p = 1;
            $g = 0;
            $l = 0;
            for ($j = $i; $j < $n; $j++) {
                $p *= $nums[$j];
                if ($p > 25200) break;
                if ($g == 0) {
                    $g = $l = $nums[$j];
                } else {
                    $g = $getGcd($g, $nums[$j]);
                    $l = (int)(($l * $nums[$j]) / $getGcd($l, $nums[$j]));
                }
                if ($p == $g * $l) {
                    $res = max($res, $j - $i + 1);
                }
            }
        }
        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxLength(_ nums: [Int]) -> Int {
        func getGcd(_ a: Int, _ b: Int) -> Int {
            var x = a
            var y = b
            while y != 0 {
                let temp = y
                y = x % y
                x = temp
            }
            return x
        }

        let n = nums.count
        var res = 0
        for i in 0..<n {
            var p = 1
            var g = 0
            var l = 0
            for j in i..<n {
                p *= nums[j]
                if p > 25200 { break }
                if g == 0 {
                    g = nums[j]
                    l = nums[j]
                } else {
                    g = getGcd(g, nums[j])
                    l = (l * nums[j]) / getGcd(l, nums[j])
                }
                if p == g * l {
                    res = max(res, j - i + 1)
                }
            }
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxLength(nums: IntArray): Int {
        fun getGcd(a: Int, b: Int): Int {
            var x = a
            var y = b
            while (y != 0) {
                val temp = y
                y = x % y
                x = temp
            }
            return x
        }

        val n = nums.size
        var res = 0
        for (i in 0 until n) {
            var p = 1
            var g = 0
            var l = 0
            for (j in i until n) {
                p *= nums[j]
                if (p > 25200) break
                if (g == 0) {
                    g = nums[j]
                    l = nums[j]
                } else {
                    g = getGcd(g, nums[j])
                    l = (l * nums[j]) / getGcd(l, nums[j])
                }
                if (p == g * l) {
                    val currentLen = j - i + 1
                    if (currentLen > res) res = currentLen
                }
            }
        }
        return res
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
  int maxLength(List<int> nums) {
    int getGcd(int a, int b) {
      while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
      }
      return a;
    }

    int n = nums.length;
    int res = 0;
    for (int i = 0; i < n; i++) {
      int p = 1;
      int g = 0;
      int l = 0;
      for (int j = i; j < n; j++) {
        p *= nums[j];
        if (p > 25200) break;
        if (g == 0) {
          g = nums[j];
          l = nums[j];
        } else {
          g = getGcd(g, nums[j]);
          l = (l * nums[j]) ~/ getGcd(l, nums[j]);
        }
        if (p == g * l) {
          res = max(res, j - i + 1);
        }
      }
    }
    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxLength(nums []int) int {
	getGcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}

	n := len(nums)
	res := 0
	for i := 0; i < n; i++ {
		p, g, l := 1, 0, 0
		for j := i; j < n; j++ {
			p *= nums[j]
			if p > 25200 {
				break
			}
			if g == 0 {
				g, l = nums[j], nums[j]
			} else {
				g = getGcd(g, nums[j])
				l = (l * nums[j]) / getGcd(l, nums[j])
			}
			if p == g*l {
				if j-i+1 > res {
					res = j - i + 1
				}
			}
		}
	}
	return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_length(nums)
  n = nums.length
  res = 0
  (0...n).each do |i|
    p = 1
    g = 0
    l = 0
    (i...n).each do |j|
      p *= nums[j]
      break if p > 25200
      if g == 0
        g = l = nums[j]
      else
        g = g.gcd(nums[j])
        l = (l * nums[j]) / l.gcd(nums[j])
      end
      res = [res, j - i + 1].max if p == g * l
    end
  end
  res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxLength(nums: Array[Int]): Int = {
        def getGcd(a: Long, b: Long): Long = if (b == 0) a else getGcd(b, a % b)

        val n = nums.length
        var res = 0
        var i = 0
        while (i < n) {
            var p: Long = 1
            var g: Long = 0
            var l: Long = 0
            var j = i
            var loopBreak = false
            while (j < n && !loopBreak) {
                p *= nums[j]
                if (p > 25200) {
                    loopBreak = true
                } else {
                    if (g == 0) {
                        g = nums[j].toLong
                        l = nums[j].toLong
                    } else {
                        g = getGcd(g, nums[j].toLong)
                        l = (l * nums[j]) / getGcd(l, nums[j].toLong)
                    }
                    if (p == g * l) {
                        res = Math.max(res, j - i + 1)
                    }
                    j += 1
                }
            }
            i += 1
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_length(nums: Vec<i32>) -> i32 {
        fn gcd(a: i64, b: i64) -> i64 {
            let (mut x, mut y) = (a, b);
            while y != 0 {
                x %= y;
                std::mem::swap(&mut x, &mut y);
            }
            x
        }

        let n = nums.len();
        let mut res = 0;
        for i in 0..n {
            let mut p: i64 = 1;
            let mut g: i64 = 0;
            let mut l: i64 = 0;
            for j in i..n {
                p *= nums[j] as i64;
                if p > 25200 {
                    break;
                }
                if g == 0 {
                    g = nums[j] as i64;
                    l = nums[j] as i64;
                } else {
                    let current_val = nums[j] as i64;
                    g = gcd(g, current_val);
                    l = (l * current_val) / gcd(l, current_val);
                }
                if p == g * l {
                    res = res.max((j - i + 1) as i32);
                }
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
(define/contract (max-length nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [arr (list->vector nums)]
         [res 0])
    (for ([i (in-range n)])
      (let loop ([j i] [p 1] [g 0] [l 0])
        (when (and (< j n))
          (let* ([val (vector-ref arr j)]
                 [np (* p val)])
            (when (<= np 25200)
              (let* ([ng (if (= g 0) val (gcd g val))]
                     [nl (if (= l 0) val (lcm l val))])
                (when (= np (* ng nl))
                  (set! res (max res (+ (- j i) 1))))
                (loop (+ j 1) np ng nl)))))))
    res))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_length(Nums :: [integer()]) -> integer().
max_length(Nums) ->
  Arr = list_to_tuple(Nums),
  N = tuple_size(Arr),
  solve_i(1, N, Arr, 0).

solve_i(I, N, Arr, Res) when I > N -> Res;
solve_i(I, N, Arr, Res) ->
  NewRes = solve_j(I, I, N, Arr, 1, 0, 0, Res),
  solve_i(I + 1, N, Arr, NewRes).

solve_j(I, J, N, Arr, P, G, L, Res) when J > N -> Res;
solve_j(I, J, N, Arr, P, G, L, Res) ->
  Val = element(J, Arr),
  NP = P * Val,
  if
    NP > 25200 -> Res;
    true ->
      {NG, NL} = if
        G == 0 -> {Val, Val};
        true -> 
          GcdVal = gcd(G, Val),
          {GcdVal, (L * Val) div gcd(L, Val)}
      end,
      NewRes = if
        NP == NG * NL -> max(Res, J - I + 1);
        true -> Res
      end,
      solve_j(I, J + 1, N, Arr, NP, NG, NL, NewRes)
  end.

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_length(nums :: [integer]) :: integer
  def max_length(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)
    Enum.reduce(0..(n - 1), 0, fn i, res_outer ->
      solve_j(i, i, n, arr, 1, 0, 0, res_outer)
    end)
  end

  defp solve_j(i, j, n, arr, p, g, l, res) when j < n do
    val = elem(arr, j)
    np = p * val
    if np > 25200 do
      res
    else
      {ng, nl} = if g == 0 do
        {val, val}
      else
        gcd_val = Integer.gcd(g, val)
        lcm_val = div(l * val, Integer.gcd(l, val))
        {gcd_val, lcm_val}
      end
      new_res = if np == ng * nl, do: max(res, j - i + 1), else: res
      solve_j(i, j + 1, n, arr, np, ng, nl, new_res)
    end
  end
  defp solve_j(_i, _j, _n, _arr, _p, _g, _l, res), do: res
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^2 * log(M)) where N is the length of the array and M is the maximum value in the array (10). The nested loops iterate over all subarrays, and calculating the GCD takes logarithmic time.
- **Space Complexity:** O(1) because we only use a constant amount of extra space for the running product, GCD, LCM, and the result variables.
