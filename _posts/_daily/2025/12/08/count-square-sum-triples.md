---
layout: post
title: "Count Square Sum Triples"
date: 2025-12-08 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "Enumeration"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-square-sum-triples/
ai_solutions:
  - solutions:
      cpp: "#include <cmath>\n\nclass Solution {\npublic:\n    int countTriples(int\
        \ n) {\n        int count = 0;\n        for (int a = 1; a <= n; ++a) {\n   \
        \         for (int b = 1; b <= n; ++b) {\n                int c_squared = a*a\
        \ + b*b;\n\n                if (c_squared > n*n) {\n                    break;\n\
        \                }\n\n                double c_float = std::sqrt(static_cast<double>(c_squared));\n\
        \                int c_int = static_cast<int>(c_float);\n\n                if\
        \ (c_int * c_int == c_squared && c_int <= n) {\n                    count++;\n\
        \                }\n            }\n        }\n        return count;\n    }\n\
        };"
      java: "class Solution {\n    public int countTriples(int n) {\n        int count\
        \ = 0;\n        for (int a = 1; a <= n; a++) {\n            for (int b = 1;\
        \ b <= n; b++) {\n                int c_squared = a*a + b*b;\n\n           \
        \     if (c_squared > n*n) {\n                    break;\n                }\n\
        \n                double c_float = Math.sqrt(c_squared);\n                int\
        \ c_int = (int) c_float;\n\n                if (c_int * c_int == c_squared &&\
        \ c_int <= n) {\n                    count++;\n                }\n         \
        \   }\n        }\n        return count;\n    }\n}"
      python: "import math\n\nclass Solution:\n    def countTriples(self, n: int) ->\
        \ int:\n        count = 0\n        for a in range(1, n + 1):\n            for\
        \ b in range(1, n + 1):\n                c_squared = a*a + b*b\n\n         \
        \       if c_squared > n*n:\n                    break\n\n                c_float\
        \ = math.sqrt(c_squared)\n                c_int = int(c_float)\n\n         \
        \       if c_int * c_int == c_squared and c_int <= n:\n                    count\
        \ += 1\n        return count"
      python3: "import math\n\nclass Solution:\n    def countTriples(self, n: int) ->\
        \ int:\n        count = 0\n        for a in range(1, n + 1):\n            for\
        \ b in range(1, n + 1):\n                c_squared = a*a + b*b\n\n         \
        \       if c_squared > n*n:\n                    break\n\n                c_float\
        \ = math.sqrt(c_squared)\n                c_int = int(c_float)\n\n         \
        \       if c_int * c_int == c_squared and c_int <= n:\n                    count\
        \ += 1\n        return count"
      c: "#include <math.h>\n\nint countTriples(int n) {\n    int count = 0;\n    for\
        \ (int a = 1; a <= n; ++a) {\n        for (int b = 1; b <= n; ++b) {\n     \
        \       int c_squared = a*a + b*b;\n\n            if (c_squared > n*n) {\n \
        \               break;\n            }\n\n            double c_float = sqrt((double)c_squared);\n\
        \            int c_int = (int)c_float;\n\n            if (c_int * c_int == c_squared\
        \ && c_int <= n) {\n                count++;\n            }\n        }\n   \
        \ }\n    return count;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int CountTriples(int\
        \ n) {\n        int count = 0;\n        for (int a = 1; a <= n; a++) {\n   \
        \         for (int b = 1; b <= n; b++) {\n                int cSquared = a *\
        \ a + b * b;\n\n                if (cSquared > n * n) {\n                  \
        \  break;\n                }\n\n                double cFloat = Math.Sqrt(cSquared);\n\
        \                int cInt = (int)cFloat;\n\n                if (cInt * cInt\
        \ == cSquared && cInt <= n) {\n                    count++;\n              \
        \  }\n            }\n        }\n        return count;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar countTriples\
        \ = function(n) {\n    let count = 0;\n    for (let a = 1; a <= n; a++) {\n\
        \        for (let b = 1; b <= n; b++) {\n            let cSquared = a * a +\
        \ b * b;\n\n            if (cSquared > n * n) {\n                break;\n  \
        \          }\n\n            let cFloat = Math.sqrt(cSquared);\n            let\
        \ cInt = Math.floor(cFloat);\n\n            if (cInt * cInt === cSquared &&\
        \ cInt <= n) {\n                count++;\n            }\n        }\n    }\n\
        \    return count;\n};"
      typescript: "function countTriples(n: number): number {\n    let count: number\
        \ = 0;\n    for (let a = 1; a <= n; a++) {\n        for (let b = 1; b <= n;\
        \ b++) {\n            let cSquared: number = a * a + b * b;\n\n            if\
        \ (cSquared > n * n) {\n                break;\n            }\n\n          \
        \  let cFloat: number = Math.sqrt(cSquared);\n            let cInt: number =\
        \ Math.floor(cFloat);\n\n            if (cInt * cInt === cSquared && cInt <=\
        \ n) {\n                count++;\n            }\n        }\n    }\n    return\
        \ count;\n}"
      php: "class Solution {\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function countTriples($n) {\n        $count = 0;\n        for\
        \ ($a = 1; $a <= $n; $a++) {\n            for ($b = 1; $b <= $n; $b++) {\n \
        \               $cSquared = $a * $a + $b * $b;\n\n                if ($cSquared\
        \ > $n * $n) {\n                    break;\n                }\n\n          \
        \      $cFloat = sqrt($cSquared);\n                $cInt = (int)$cFloat;\n\n\
        \                if ($cInt * $cInt == $cSquared && $cInt <= $n) {\n        \
        \            $count++;\n                }\n            }\n        }\n      \
        \  return $count;\n    }\n}"
      swift: "import Foundation\n\nclass Solution {\n    func countTriples(_ n: Int)\
        \ -> Int {\n        var count = 0\n        for a in 1...n {\n            for\
        \ b in 1...n {\n                let cSquared = a * a + b * b\n\n           \
        \     if cSquared > n * n {\n                    break\n                }\n\n\
        \                let cFloat = sqrt(Double(cSquared))\n                let cInt\
        \ = Int(cFloat)\n\n                if cInt * cInt == cSquared && cInt <= n {\n\
        \                    count += 1\n                }\n            }\n        }\n\
        \        return count\n    }\n}"
      kotlin: "import kotlin.math.sqrt\n\nclass Solution {\n    fun countTriples(n:\
        \ Int): Int {\n        var count = 0\n        for (a in 1..n) {\n          \
        \  for (b in 1..n) {\n                val cSquared = a * a + b * b\n\n     \
        \           if (cSquared > n * n) {\n                    break\n           \
        \     }\n\n                val cFloat = sqrt(cSquared.toDouble())\n        \
        \        val cInt = cFloat.toInt()\n\n                if (cInt * cInt == cSquared\
        \ && cInt <= n) {\n                    count++\n                }\n        \
        \    }\n        }\n        return count\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int countTriples(int n) {\n\
        \    int count = 0;\n    for (int a = 1; a <= n; a++) {\n      for (int b =\
        \ 1; b <= n; b++) {\n        int cSquared = a * a + b * b;\n\n        if (cSquared\
        \ > n * n) {\n          break;\n        }\n\n        double cFloat = sqrt(cSquared.toDouble());\n\
        \        int cInt = cFloat.toInt();\n\n        if (cInt * cInt == cSquared &&\
        \ cInt <= n) {\n          count++;\n        }\n      }\n    }\n    return count;\n\
        \  }\n}"
      go: "package main\n\nimport \"math\"\n\nfunc countTriples(n int) int {\n    count\
        \ := 0\n    for a := 1; a <= n; a++ {\n        for b := 1; b <= n; b++ {\n \
        \           cSquared := a*a + b*b\n\n            if cSquared > n*n {\n     \
        \           break\n            }\n\n            cFloat := math.Sqrt(float64(cSquared))\n\
        \            cInt := int(cFloat)\n\n            if cInt*cInt == cSquared &&\
        \ cInt <= n {\n                count++\n            }\n        }\n    }\n  \
        \  return count\n}"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef count_triples(n)\n    count\
        \ = 0\n    (1..n).each do |a|\n        (1..n).each do |b|\n            c_squared\
        \ = a * a + b * b\n\n            if c_squared > n * n\n                break\n\
        \            end\n\n            c_float = Math.sqrt(c_squared)\n           \
        \ c_int = c_float.to_i\n\n            if c_int * c_int == c_squared && c_int\
        \ <= n\n                count += 1\n            end\n        end\n    end\n\
        \    count\nend"
      scala: "import scala.math.sqrt\n\nobject Solution {\n    def countTriples(n: Int):\
        \ Int = {\n        var count = 0\n        for (a <- 1 to n) {\n            for\
        \ (b <- 1 to n) {\n                val cSquared = a * a + b * b\n\n        \
        \        val cFloat = sqrt(cSquared.toDouble())\n                val cInt =\
        \ cFloat.toInt\n\n                if (cInt * cInt == cSquared && cInt <= n)\
        \ {\n                    count += 1\n                }\n            }\n    \
        \    }\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn count_triples(n: i32) -> i32 {\n        let\
        \ mut count = 0;\n        for a in 1..=n {\n            for b in 1..=n {\n \
        \               let c_squared = a * a + b * b;\n\n                if c_squared\
        \ > n * n {\n                    break;\n                }\n\n             \
        \   let c_float = (c_squared as f64).sqrt();\n                let c_int = c_float\
        \ as i32;\n\n                if c_int * c_int == c_squared && c_int <= n {\n\
        \                    count += 1;\n                }\n            }\n       \
        \ }\n        count\n    }\n}"
      racket: "#lang racket\n\n(define (count-triples-impl a n count)\n  (if (> a n)\n\
        \      count\n      (let loop-b ((b 1) (current-count count))\n        (if (>\
        \ b n)\n            (count-triples-impl (+ a 1) n current-count)\n         \
        \   (let* ((c-squared (+ (* a a) (* b b)))\n                   (n-squared (*\
        \ n n)))\n              (if (> c-squared n-squared)\n                  (count-triples-impl\
        \ (+ a 1) n current-count)\n                  (let* ((c-float (sqrt (exact->inexact\
        \ c-squared)))\n                         (c-int (floor c-float)))\n        \
        \            (if (and (= (* c-int c-int) c-squared) (<= c-int n))\n        \
        \                (loop-b (+ b 1) (+ current-count 1))\n                    \
        \    (loop-b (+ b 1) current-count))))))))\n\n(define (countTriples n)\n  (count-triples-impl\
        \ 1 n 0))"
      erlang: "-module(solution).\n-export([count_triples/1]).\n\ncount_triples(N) ->\n\
        \    count_triples_a(1, N, 0).\n\ncount_triples_a(A, N, Acc) when A =< N ->\n\
        \    count_triples_b(A, 1, N, Acc).\ncount_triples_a(_, _, Acc) ->\n    Acc.\n\
        \ncount_triples_b(A, B, N, Acc) when B =< N ->\n    CSquared = A*A + B*B,\n\
        \    NSquared = N*N,\n    case CSquared > NSquared of\n        true ->\n   \
        \         count_triples_a(A + 1, N, Acc);\n        false ->\n            CFloat\
        \ = math:sqrt(CSquared),\n            CInt = trunc(CFloat),\n            case\
        \ (CInt * CInt == CSquared) and (CInt =< N) of\n                true ->\n  \
        \                  count_triples_b(A, B + 1, N, Acc + 1);\n                false\
        \ ->\n                    count_triples_b(A, B + 1, N, Acc)\n            end\n\
        \    end;\ncount_triples_b(A, _, N, Acc) ->\n    count_triples_a(A + 1, N, Acc)."
      elixir: "defmodule Solution do\n  @spec count_triples(n :: integer) :: integer\n\
        \  def count_triples(n) do\n    count_triples_a(1, n, 0)\n  end\n\n  defp count_triples_a(a,\
        \ n, acc) when a <= n do\n    count_triples_b(a, 1, n, acc)\n  end\n  defp count_triples_a(_a,\
        \ _n, acc), do: acc\n\n  defp count_triples_b(a, b, n, acc) when b <= n do\n\
        \    c_squared = a*a + b*b\n    n_squared = n*n\n\n    if c_squared > n_squared\
        \ do\n      count_triples_a(a + 1, n, acc)\n    else\n      c_float = :math.sqrt(c_squared)\n\
        \      c_int = trunc(c_float)\n\n      if c_int * c_int == c_squared and c_int\
        \ <= n do\n        count_triples_b(a, b + 1, n, acc + 1)\n      else\n     \
        \   count_triples_b(a, b + 1, n, acc)\n      end\n    end\n  end\n  defp count_triples_b(a,\
        \ _b, n, acc), do: count_triples_a(a + 1, n, acc)\nend"
    approach: The problem requires counting Pythagorean triples (a, b, c) such that
      a^2 + b^2 = c^2 and all a, b, c are integers between 1 and n, inclusive. Given
      the constraint that n is small (up to 250), a brute-force approach is efficient
      enough. The core idea is to iterate through all possible integer values for 'a'
      and 'b' within the range [1, n]. For each pair (a, b), we calculate the sum of
      their squares, `c_squared = a*a + b*b`. Then, we determine if `c_squared` is a
      perfect square and if its square root, `c`, also falls within the range [1, n].
    time_complexity: The time complexity is O(n^2). This is because there are two nested
      loops, each iterating from 1 to n. Inside the loops, operations like multiplication,
      addition, square root, and integer conversion are considered constant time. Although
      an optimization is included to break the inner loop early if `a*a + b*b` exceeds
      `n*n`, which reduces the constant factor, the worst-case asymptotic complexity
      remains O(n^2) as the inner loop can still run up to n times for small values
      of 'a'.
    space_complexity: The space complexity is O(1). The algorithm uses a fixed amount
      of extra space regardless of the input size 'n'. Only a few integer variables
      (for 'a', 'b', 'c_squared', 'c_float', 'c_int', and 'count') are used to store
      intermediate results, which does not scale with 'n'.
    elapsed_time: 52.74893116950989
    model: gemini-2.5-flash
    generated_at: '2025-12-08 01:06:16 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int countTriples(int n) {\n        int count\
        \ = 0;\n        for (int a = 1; a <= n; a++) {\n            for (int b = a;\
        \ b <= n; b++) {\n                double c = sqrt(a * a + b * b);\n        \
        \        if (c <= n && c == (int)c) {\n                    if (a != b) count\
        \ += 2;\n                    else count++;\n                }\n            }\n\
        \        }\n        return count;\n    }\n};"
      java: "class Solution {\n    public int countTriples(int n) {\n        int count\
        \ = 0;\n        for (int a = 1; a <= n; a++) {\n            for (int b = a;\
        \ b <= n; b++) {\n                double c = Math.sqrt(a * a + b * b);\n   \
        \             if (c <= n && c == (int)c) {\n                    if (a != b)\
        \ count += 2;\n                    else count++;\n                }\n      \
        \      }\n        }\n        return count;\n    }\n}"
      python: "class Solution:\n    def countTriples(self, n: int) -> int:\n       \
        \ count = 0\n        for a in range(1, n + 1):\n            for b in range(a,\
        \ n + 1):\n                c = (a ** 2 + b ** 2) ** 0.5\n                if\
        \ c <= n and c == int(c):\n                    if a != b: count += 2\n     \
        \               else: count += 1\n        return count"
      python3: "class Solution:\n    def countTriples(self, n: int) -> int:\n      \
        \  count = 0\n        for a in range(1, n + 1):\n            for b in range(a,\
        \ n + 1):\n                c = (a ** 2 + b ** 2) ** 0.5\n                if\
        \ c <= n and c == int(c):\n                    if a != b: count += 2\n     \
        \               else: count += 1\n        return count"
      c: "int countTriples(int n) {\n    int count = 0;\n    for (int a = 1; a <= n;\
        \ a++) {\n        for (int b = a; b <= n; b++) {\n            double c = sqrt(a\
        \ * a + b * b);\n            if (c <= n && c == (int)c) {\n                if\
        \ (a != b) count += 2;\n                else count++;\n            }\n     \
        \   }\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int CountTriples(int n) {\n     \
        \   int count = 0;\n        for (int a = 1; a <= n; a++) {\n            for\
        \ (int b = a; b <= n; b++) {\n                double c = Math.Sqrt(a * a + b\
        \ * b);\n                if (c <= n && c == (int)c) {\n                    if\
        \ (a != b) count += 2;\n                    else count++;\n                }\n\
        \            }\n        }\n        return count;\n    }\n}"
      javascript: "var countTriples = function(n) {\n    let count = 0;\n    for (let\
        \ a = 1; a <= n; a++) {\n        for (let b = a; b <= n; b++) {\n          \
        \  let c = Math.sqrt(a * a + b * b);\n            if (c <= n && c == Math.floor(c))\
        \ {\n                if (a != b) count += 2;\n                else count++;\n\
        \            }\n        }\n    }\n    return count;\n};"
      typescript: "function countTriples(n: number): number {\n    let count: number\
        \ = 0;\n    for (let a: number = 1; a <= n; a++) {\n        for (let b: number\
        \ = a; b <= n; b++) {\n            let c: number = Math.sqrt(a * a + b * b);\n\
        \            if (c <= n && c == Math.floor(c)) {\n                if (a != b)\
        \ count += 2;\n                else count++;\n            }\n        }\n   \
        \ }\n    return count;\n}"
      php: "class Solution {\n    function countTriples($n) {\n        $count = 0;\n\
        \        for ($a = 1; $a <= $n; $a++) {\n            for ($b = $a; $b <= $n;\
        \ $b++) {\n                $c = sqrt($a * $a + $b * $b);\n                if\
        \ ($c <= $n && $c == (int)$c) {\n                    if ($a != $b) $count +=\
        \ 2;\n                    else $count++;\n                }\n            }\n\
        \        }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func countTriples(_ n: Int) -> Int {\n        var\
        \ count = 0\n        for a in 1...n {\n            for b in a...n {\n      \
        \          let c = sqrt(Double(a * a + b * b))\n                if c <= Double(n)\
        \ && c == Double(Int(c)) {\n                    if a != b { count += 2 }\n \
        \                   else { count += 1 }\n                }\n            }\n\
        \        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun countTriples(n: Int): Int {\n        var count\
        \ = 0\n        for (a in 1..n) {\n            for (b in a..n) {\n          \
        \      val c = Math.sqrt(a * a + b * b)\n                if (c <= n && c ==\
        \ c.toInt().toDouble()) {\n                    if (a != b) count += 2\n    \
        \                else count++\n                }\n            }\n        }\n\
        \        return count\n    }\n}"
      dart: "class Solution {\n    int countTriples(int n) {\n        int count = 0;\n\
        \        for (int a = 1; a <= n; a++) {\n            for (int b = a; b <= n;\
        \ b++) {\n                double c = (a * a + b * b).sqrt();\n             \
        \   if (c <= n && c == c.floor().toDouble()) {\n                    if (a !=\
        \ b) count += 2;\n                    else count++;\n                }\n   \
        \         }\n        }\n        return count;\n    }\n}"
      go: "func countTriples(n int) int {\n    count := 0\n    for a := 1; a <= n; a++\
        \ {\n        for b := a; b <= n; b++ {\n            c := math.Sqrt(float64(a*a\
        \ + b*b))\n            if c <= float64(n) && c == float64(int(c)) {\n      \
        \          if a != b { count += 2 }\n                else { count++ }\n    \
        \        }\n        }\n    }\n    return count\n}"
      ruby: "def count_triples(n)\n    count = 0\n    (1..n).each do |a|\n        (a..n).each\
        \ do |b|\n            c = Math.sqrt(a * a + b * b)\n            if c <= n &&\
        \ c == c.to_i\n                if a != b\n                    count += 2\n \
        \               else\n                    count += 1\n                end\n\
        \            end\n        end\n    end\n    count\nend"
      scala: "object Solution {\n    def countTriples(n: Int): Int = {\n        var\
        \ count = 0\n        for (a <- 1 to n) {\n            for (b <- a to n) {\n\
        \                val c = Math.sqrt(a * a + b * b)\n                if (c <=\
        \ n && c == c.toInt) {\n                    if (a != b) count += 2\n       \
        \             else count += 1\n                }\n            }\n        }\n\
        \        count\n    }\n}"
      rust: "impl Solution {\n    pub fn count_triples(n: i32) -> i32 {\n        let\
        \ mut count = 0;\n        for a in 1..=n {\n            for b in a..=n {\n \
        \               let c = (a * a + b * b) as f64;\n                let c = c.sqrt();\n\
        \                if c <= n as f64 && c == c.floor() {\n                    if\
        \ a != b { count += 2 }\n                    else { count += 1 }\n         \
        \       }\n            }\n        }\n        count\n    }\n}"
      racket: "define (count-triples n)\n    (let loop ((a 1) (count 0))\n        (if\
        \ (> a n)\n            count\n            (loop (add1 a) (loop2 a n count)))))\n\
        (define (loop2 a n count)\n    (let loop ((b a) (count count))\n        (if\
        \ (> b n)\n            count\n            (let ((c (sqrt (+ (* a a) (* b b)))))\n\
        \                (if (and (<= c n) (= c (floor c)))\n                    (if\
        \ (= a b)\n                        (loop (add1 b) (add1 count))\n          \
        \              (loop (add1 b) (+ count 2)))\n                    (loop (add1\
        \ b) count))))))"
      erlang: "count_triples(N) ->\n    F = fun(A, Count) ->\n        if A > N -> Count;\n\
        \        true ->\n            F2 = fun(B, Count) ->\n                if B >\
        \ N -> Count;\n                true ->\n                    C = math:sqrt(A\
        \ * A + B * B),\n                    if C =< N andalso C == trunc(C) ->\n  \
        \                      if A == B -> F2(B + 1, Count + 1);\n                \
        \        true -> F2(B + 1, Count + 2)\n                    else\n          \
        \              F2(B + 1, Count)\n            end,\n            F(A + 1, F2(A,\
        \ Count))\n    end,\n    F(1, 0)."
      elixir: "def count_triples(n) do\n    count = 0\n    Enum.reduce(1..n, count,\
        \ fn a, count ->\n        Enum.reduce(a..n, count, fn b, count ->\n        \
        \    c = :math.sqrt(a * a + b * b),\n            if c <= n and c == trunc(c)\
        \ do\n                if a != b, do: count + 2, else: count + 1\n          \
        \  else\n                count\n            end)\n    end)\nend"
    approach: 'The problem requires counting the number of square triples (a, b, c)
      where a, b, and c are integers and a^2 + b^2 = c^2. The approach involves iterating
      over all possible pairs (a, b) and checking if the square root of a^2 + b^2 is
      an integer less than or equal to n. This can be done using a nested loop to generate
      all pairs (a, b) and then checking if the square root of a^2 + b^2 is an integer.
      The key intuition here is to recognize that a^2 + b^2 = c^2 is a Pythagorean triple,
      and we need to count the number of such triples where a, b, and c are all less
      than or equal to n.


      The algorithm can be optimized by only iterating over pairs (a, b) where a <=
      b, since the pairs (b, a) will also be counted. This reduces the number of iterations
      and improves the efficiency of the algorithm. Additionally, we can use a mathematical
      property that a^2 + b^2 = c^2 can be rewritten as c = sqrt(a^2 + b^2), which allows
      us to easily check if c is an integer.'
    time_complexity: The time complexity of the algorithm is O(n^2) because we are iterating
      over all pairs (a, b) where a and b are less than or equal to n. This results
      in a quadratic number of iterations, which dominates the time complexity of the
      algorithm. The space complexity is O(1) because we are only using a constant amount
      of space to store the count of square triples.
    space_complexity: The space complexity of the algorithm is O(1) because we are only
      using a constant amount of space to store the count of square triples. We do not
      need to store any additional data structures or arrays, which keeps the space
      complexity constant.
    elapsed_time: 5.97140645980835
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-08 01:06:22 '
---

## Problem #1925: Count Square Sum Triples

**Difficulty:** Easy

**Topics:** Math, Enumeration

## Problem Description

<p>A <strong>square triple</strong> <code>(a,b,c)</code> is a triple where <code>a</code>, <code>b</code>, and <code>c</code> are <strong>integers</strong> and <code>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></code>.</p>

<p>Given an integer <code>n</code>, return <em>the number of <strong>square triples</strong> such that </em><code>1 &lt;= a, b, c &lt;= n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation</strong>: The square triples are (3,4,5) and (4,3,5).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation</strong>: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 250</code></li>
</ul>


## Hints

1. Iterate over all possible pairs (a,b) and check that the square root of a * a + b * b is an integers less than or equal n

2. You can check that the square root of an integer is an integer using binary seach or a builtin function like sqrt

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-08 01:06:16 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires counting Pythagorean triples (a, b, c) such that a^2 + b^2 = c^2 and all a, b, c are integers between 1 and n, inclusive. Given the constraint that n is small (up to 250), a brute-force approach is efficient enough. The core idea is to iterate through all possible integer values for 'a' and 'b' within the range [1, n]. For each pair (a, b), we calculate the sum of their squares, `c_squared = a*a + b*b`. Then, we determine if `c_squared` is a perfect square and if its square root, `c`, also falls within the range [1, n].

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
#include <cmath>

class Solution {
public:
    int countTriples(int n) {
        int count = 0;
        for (int a = 1; a <= n; ++a) {
            for (int b = 1; b <= n; ++b) {
                int c_squared = a*a + b*b;

                if (c_squared > n*n) {
                    break;
                }

                double c_float = std::sqrt(static_cast<double>(c_squared));
                int c_int = static_cast<int>(c_float);

                if (c_int * c_int == c_squared && c_int <= n) {
                    count++;
                }
            }
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countTriples(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                int c_squared = a*a + b*b;

                if (c_squared > n*n) {
                    break;
                }

                double c_float = Math.sqrt(c_squared);
                int c_int = (int) c_float;

                if (c_int * c_int == c_squared && c_int <= n) {
                    count++;
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_squared = a*a + b*b

                if c_squared > n*n:
                    break

                c_float = math.sqrt(c_squared)
                c_int = int(c_float)

                if c_int * c_int == c_squared and c_int <= n:
                    count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c_squared = a*a + b*b

                if c_squared > n*n:
                    break

                c_float = math.sqrt(c_squared)
                c_int = int(c_float)

                if c_int * c_int == c_squared and c_int <= n:
                    count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <math.h>

int countTriples(int n) {
    int count = 0;
    for (int a = 1; a <= n; ++a) {
        for (int b = 1; b <= n; ++b) {
            int c_squared = a*a + b*b;

            if (c_squared > n*n) {
                break;
            }

            double c_float = sqrt((double)c_squared);
            int c_int = (int)c_float;

            if (c_int * c_int == c_squared && c_int <= n) {
                count++;
            }
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int CountTriples(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = 1; b <= n; b++) {
                int cSquared = a * a + b * b;

                if (cSquared > n * n) {
                    break;
                }

                double cFloat = Math.Sqrt(cSquared);
                int cInt = (int)cFloat;

                if (cInt * cInt == cSquared && cInt <= n) {
                    count++;
                }
            }
        }
        return count;
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
 * @return {number}
 */
var countTriples = function(n) {
    let count = 0;
    for (let a = 1; a <= n; a++) {
        for (let b = 1; b <= n; b++) {
            let cSquared = a * a + b * b;

            if (cSquared > n * n) {
                break;
            }

            let cFloat = Math.sqrt(cSquared);
            let cInt = Math.floor(cFloat);

            if (cInt * cInt === cSquared && cInt <= n) {
                count++;
            }
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countTriples(n: number): number {
    let count: number = 0;
    for (let a = 1; a <= n; a++) {
        for (let b = 1; b <= n; b++) {
            let cSquared: number = a * a + b * b;

            if (cSquared > n * n) {
                break;
            }

            let cFloat: number = Math.sqrt(cSquared);
            let cInt: number = Math.floor(cFloat);

            if (cInt * cInt === cSquared && cInt <= n) {
                count++;
            }
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function countTriples($n) {
        $count = 0;
        for ($a = 1; $a <= $n; $a++) {
            for ($b = 1; $b <= $n; $b++) {
                $cSquared = $a * $a + $b * $b;

                if ($cSquared > $n * $n) {
                    break;
                }

                $cFloat = sqrt($cSquared);
                $cInt = (int)$cFloat;

                if ($cInt * $cInt == $cSquared && $cInt <= $n) {
                    $count++;
                }
            }
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func countTriples(_ n: Int) -> Int {
        var count = 0
        for a in 1...n {
            for b in 1...n {
                let cSquared = a * a + b * b

                if cSquared > n * n {
                    break
                }

                let cFloat = sqrt(Double(cSquared))
                let cInt = Int(cFloat)

                if cInt * cInt == cSquared && cInt <= n {
                    count += 1
                }
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.sqrt

class Solution {
    fun countTriples(n: Int): Int {
        var count = 0
        for (a in 1..n) {
            for (b in 1..n) {
                val cSquared = a * a + b * b

                if (cSquared > n * n) {
                    break
                }

                val cFloat = sqrt(cSquared.toDouble())
                val cInt = cFloat.toInt()

                if (cInt * cInt == cSquared && cInt <= n) {
                    count++
                }
            }
        }
        return count
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
  int countTriples(int n) {
    int count = 0;
    for (int a = 1; a <= n; a++) {
      for (int b = 1; b <= n; b++) {
        int cSquared = a * a + b * b;

        if (cSquared > n * n) {
          break;
        }

        double cFloat = sqrt(cSquared.toDouble());
        int cInt = cFloat.toInt();

        if (cInt * cInt == cSquared && cInt <= n) {
          count++;
        }
      }
    }
    return count;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import "math"

func countTriples(n int) int {
    count := 0
    for a := 1; a <= n; a++ {
        for b := 1; b <= n; b++ {
            cSquared := a*a + b*b

            if cSquared > n*n {
                break
            }

            cFloat := math.Sqrt(float64(cSquared))
            cInt := int(cFloat)

            if cInt*cInt == cSquared && cInt <= n {
                count++
            }
        }
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Integer}
def count_triples(n)
    count = 0
    (1..n).each do |a|
        (1..n).each do |b|
            c_squared = a * a + b * b

            if c_squared > n * n
                break
            end

            c_float = Math.sqrt(c_squared)
            c_int = c_float.to_i

            if c_int * c_int == c_squared && c_int <= n
                count += 1
            end
        end
    end
    count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.math.sqrt

object Solution {
    def countTriples(n: Int): Int = {
        var count = 0
        for (a <- 1 to n) {
            for (b <- 1 to n) {
                val cSquared = a * a + b * b

                val cFloat = sqrt(cSquared.toDouble())
                val cInt = cFloat.toInt

                if (cInt * cInt == cSquared && cInt <= n) {
                    count += 1
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        let mut count = 0;
        for a in 1..=n {
            for b in 1..=n {
                let c_squared = a * a + b * b;

                if c_squared > n * n {
                    break;
                }

                let c_float = (c_squared as f64).sqrt();
                let c_int = c_float as i32;

                if c_int * c_int == c_squared && c_int <= n {
                    count += 1;
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (count-triples-impl a n count)
  (if (> a n)
      count
      (let loop-b ((b 1) (current-count count))
        (if (> b n)
            (count-triples-impl (+ a 1) n current-count)
            (let* ((c-squared (+ (* a a) (* b b)))
                   (n-squared (* n n)))
              (if (> c-squared n-squared)
                  (count-triples-impl (+ a 1) n current-count)
                  (let* ((c-float (sqrt (exact->inexact c-squared)))
                         (c-int (floor c-float)))
                    (if (and (= (* c-int c-int) c-squared) (<= c-int n))
                        (loop-b (+ b 1) (+ current-count 1))
                        (loop-b (+ b 1) current-count))))))))

(define (countTriples n)
  (count-triples-impl 1 n 0))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_triples/1]).

count_triples(N) ->
    count_triples_a(1, N, 0).

count_triples_a(A, N, Acc) when A =< N ->
    count_triples_b(A, 1, N, Acc).
count_triples_a(_, _, Acc) ->
    Acc.

count_triples_b(A, B, N, Acc) when B =< N ->
    CSquared = A*A + B*B,
    NSquared = N*N,
    case CSquared > NSquared of
        true ->
            count_triples_a(A + 1, N, Acc);
        false ->
            CFloat = math:sqrt(CSquared),
            CInt = trunc(CFloat),
            case (CInt * CInt == CSquared) and (CInt =< N) of
                true ->
                    count_triples_b(A, B + 1, N, Acc + 1);
                false ->
                    count_triples_b(A, B + 1, N, Acc)
            end
    end;
count_triples_b(A, _, N, Acc) ->
    count_triples_a(A + 1, N, Acc).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_triples(n :: integer) :: integer
  def count_triples(n) do
    count_triples_a(1, n, 0)
  end

  defp count_triples_a(a, n, acc) when a <= n do
    count_triples_b(a, 1, n, acc)
  end
  defp count_triples_a(_a, _n, acc), do: acc

  defp count_triples_b(a, b, n, acc) when b <= n do
    c_squared = a*a + b*b
    n_squared = n*n

    if c_squared > n_squared do
      count_triples_a(a + 1, n, acc)
    else
      c_float = :math.sqrt(c_squared)
      c_int = trunc(c_float)

      if c_int * c_int == c_squared and c_int <= n do
        count_triples_b(a, b + 1, n, acc + 1)
      else
        count_triples_b(a, b + 1, n, acc)
      end
    end
  end
  defp count_triples_b(a, _b, n, acc), do: count_triples_a(a + 1, n, acc)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(n^2). This is because there are two nested loops, each iterating from 1 to n. Inside the loops, operations like multiplication, addition, square root, and integer conversion are considered constant time. Although an optimization is included to break the inner loop early if `a*a + b*b` exceeds `n*n`, which reduces the constant factor, the worst-case asymptotic complexity remains O(n^2) as the inner loop can still run up to n times for small values of 'a'.

- **Space Complexity:** The space complexity is O(1). The algorithm uses a fixed amount of extra space regardless of the input size 'n'. Only a few integer variables (for 'a', 'b', 'c_squared', 'c_float', 'c_int', and 'count') are used to store intermediate results, which does not scale with 'n'.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-08 01:06:22 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires counting the number of square triples (a, b, c) where a, b, and c are integers and a^2 + b^2 = c^2. The approach involves iterating over all possible pairs (a, b) and checking if the square root of a^2 + b^2 is an integer less than or equal to n. This can be done using a nested loop to generate all pairs (a, b) and then checking if the square root of a^2 + b^2 is an integer. The key intuition here is to recognize that a^2 + b^2 = c^2 is a Pythagorean triple, and we need to count the number of such triples where a, b, and c are all less than or equal to n.

The algorithm can be optimized by only iterating over pairs (a, b) where a <= b, since the pairs (b, a) will also be counted. This reduces the number of iterations and improves the efficiency of the algorithm. Additionally, we can use a mathematical property that a^2 + b^2 = c^2 can be rewritten as c = sqrt(a^2 + b^2), which allows us to easily check if c is an integer.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int countTriples(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = a; b <= n; b++) {
                double c = sqrt(a * a + b * b);
                if (c <= n && c == (int)c) {
                    if (a != b) count += 2;
                    else count++;
                }
            }
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countTriples(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = a; b <= n; b++) {
                double c = Math.sqrt(a * a + b * b);
                if (c <= n && c == (int)c) {
                    if (a != b) count += 2;
                    else count++;
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                c = (a ** 2 + b ** 2) ** 0.5
                if c <= n and c == int(c):
                    if a != b: count += 2
                    else: count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(a, n + 1):
                c = (a ** 2 + b ** 2) ** 0.5
                if c <= n and c == int(c):
                    if a != b: count += 2
                    else: count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countTriples(int n) {
    int count = 0;
    for (int a = 1; a <= n; a++) {
        for (int b = a; b <= n; b++) {
            double c = sqrt(a * a + b * b);
            if (c <= n && c == (int)c) {
                if (a != b) count += 2;
                else count++;
            }
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountTriples(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = a; b <= n; b++) {
                double c = Math.Sqrt(a * a + b * b);
                if (c <= n && c == (int)c) {
                    if (a != b) count += 2;
                    else count++;
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countTriples = function(n) {
    let count = 0;
    for (let a = 1; a <= n; a++) {
        for (let b = a; b <= n; b++) {
            let c = Math.sqrt(a * a + b * b);
            if (c <= n && c == Math.floor(c)) {
                if (a != b) count += 2;
                else count++;
            }
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countTriples(n: number): number {
    let count: number = 0;
    for (let a: number = 1; a <= n; a++) {
        for (let b: number = a; b <= n; b++) {
            let c: number = Math.sqrt(a * a + b * b);
            if (c <= n && c == Math.floor(c)) {
                if (a != b) count += 2;
                else count++;
            }
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function countTriples($n) {
        $count = 0;
        for ($a = 1; $a <= $n; $a++) {
            for ($b = $a; $b <= $n; $b++) {
                $c = sqrt($a * $a + $b * $b);
                if ($c <= $n && $c == (int)$c) {
                    if ($a != $b) $count += 2;
                    else $count++;
                }
            }
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countTriples(_ n: Int) -> Int {
        var count = 0
        for a in 1...n {
            for b in a...n {
                let c = sqrt(Double(a * a + b * b))
                if c <= Double(n) && c == Double(Int(c)) {
                    if a != b { count += 2 }
                    else { count += 1 }
                }
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countTriples(n: Int): Int {
        var count = 0
        for (a in 1..n) {
            for (b in a..n) {
                val c = Math.sqrt(a * a + b * b)
                if (c <= n && c == c.toInt().toDouble()) {
                    if (a != b) count += 2
                    else count++
                }
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int countTriples(int n) {
        int count = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = a; b <= n; b++) {
                double c = (a * a + b * b).sqrt();
                if (c <= n && c == c.floor().toDouble()) {
                    if (a != b) count += 2;
                    else count++;
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countTriples(n int) int {
    count := 0
    for a := 1; a <= n; a++ {
        for b := a; b <= n; b++ {
            c := math.Sqrt(float64(a*a + b*b))
            if c <= float64(n) && c == float64(int(c)) {
                if a != b { count += 2 }
                else { count++ }
            }
        }
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_triples(n)
    count = 0
    (1..n).each do |a|
        (a..n).each do |b|
            c = Math.sqrt(a * a + b * b)
            if c <= n && c == c.to_i
                if a != b
                    count += 2
                else
                    count += 1
                end
            end
        end
    end
    count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countTriples(n: Int): Int = {
        var count = 0
        for (a <- 1 to n) {
            for (b <- a to n) {
                val c = Math.sqrt(a * a + b * b)
                if (c <= n && c == c.toInt) {
                    if (a != b) count += 2
                    else count += 1
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        let mut count = 0;
        for a in 1..=n {
            for b in a..=n {
                let c = (a * a + b * b) as f64;
                let c = c.sqrt();
                if c <= n as f64 && c == c.floor() {
                    if a != b { count += 2 }
                    else { count += 1 }
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (count-triples n)
    (let loop ((a 1) (count 0))
        (if (> a n)
            count
            (loop (add1 a) (loop2 a n count)))))
(define (loop2 a n count)
    (let loop ((b a) (count count))
        (if (> b n)
            count
            (let ((c (sqrt (+ (* a a) (* b b)))))
                (if (and (<= c n) (= c (floor c)))
                    (if (= a b)
                        (loop (add1 b) (add1 count))
                        (loop (add1 b) (+ count 2)))
                    (loop (add1 b) count))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
count_triples(N) ->
    F = fun(A, Count) ->
        if A > N -> Count;
        true ->
            F2 = fun(B, Count) ->
                if B > N -> Count;
                true ->
                    C = math:sqrt(A * A + B * B),
                    if C =< N andalso C == trunc(C) ->
                        if A == B -> F2(B + 1, Count + 1);
                        true -> F2(B + 1, Count + 2)
                    else
                        F2(B + 1, Count)
            end,
            F(A + 1, F2(A, Count))
    end,
    F(1, 0).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def count_triples(n) do
    count = 0
    Enum.reduce(1..n, count, fn a, count ->
        Enum.reduce(a..n, count, fn b, count ->
            c = :math.sqrt(a * a + b * b),
            if c <= n and c == trunc(c) do
                if a != b, do: count + 2, else: count + 1
            else
                count
            end)
    end)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the algorithm is O(n^2) because we are iterating over all pairs (a, b) where a and b are less than or equal to n. This results in a quadratic number of iterations, which dominates the time complexity of the algorithm. The space complexity is O(1) because we are only using a constant amount of space to store the count of square triples.

- **Space Complexity:** The space complexity of the algorithm is O(1) because we are only using a constant amount of space to store the count of square triples. We do not need to store any additional data structures or arrays, which keeps the space complexity constant.

</div>
</details>
