---
layout: post
title: "Minimum One Bit Operations to Make Integers Zero"
date: 2025-11-08 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Dynamic Programming", "Bit Manipulation", "Memoization"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumOneBitOperations(int n) {\n  \
        \      int ans = 0;\n        while (n > 0) {\n            // Find k, the position\
        \ of the most significant bit (MSB) of n.\n            // For n=1, k=0. For\
        \ n=2, k=1. For n=4, k=2.\n            // For 32-bit integers, 31 - __builtin_clz(n)\
        \ gives k.\n            int k = 31 - __builtin_clz(n);\n\n            // If\
        \ n is 1, it's the base case where k=0.\n            // f(1) = 1 operation.\n\
        \            if (k == 0) {\n                ans += 1;\n                n = 0;\
        \ // Done\n            } else {\n                // Add (1 << k) to the total\
        \ operations.\n                // This is derived from the recurrence f(n) =\
        \ f(R ^ (1 << (k-1))) + (1 << k)\n                // where R = n ^ (1 << k).\n\
        \                ans += (1 << k);\n\n                // Update n for the next\
        \ iteration.\n                // n = n ^ (1 << k) ^ (1 << (k-1))\n         \
        \       // This effectively removes the k-th bit and flips the (k-1)-th bit.\n\
        \                n = n ^ (1 << k) ^ (1 << (k-1));\n            }\n        }\n\
        \        return ans;\n    }\n};"
      java: "import java.lang.Integer;\n\nclass Solution {\n    public int minimumOneBitOperations(int\
        \ n) {\n        int ans = 0;\n        while (n > 0) {\n            // Find k,\
        \ the position of the most significant bit (MSB) of n.\n            // For n=1,\
        \ k=0. For n=2, k=1. For n=4, k=2.\n            // Integer.numberOfLeadingZeros(n)\
        \ returns the number of zero bits preceding the highest-set bit.\n         \
        \   // For 32-bit integers, 31 - Integer.numberOfLeadingZeros(n) gives k.\n\
        \            int k = 31 - Integer.numberOfLeadingZeros(n);\n\n            //\
        \ If n is 1, it's the base case where k=0.\n            // f(1) = 1 operation.\n\
        \            if (k == 0) {\n                ans += 1;\n                n = 0;\
        \ // Done\n            } else {\n                // Add (1 << k) to the total\
        \ operations.\n                // This is derived from the recurrence f(n) =\
        \ f(R ^ (1 << (k-1))) + (1 << k)\n                // where R = n ^ (1 << k).\n\
        \                ans += (1 << k);\n\n                // Update n for the next\
        \ iteration.\n                // n = n ^ (1 << k) ^ (1 << (k-1))\n         \
        \       // This effectively removes the k-th bit and flips the (k-1)-th bit.\n\
        \                n = n ^ (1 << k) ^ (1 << (k-1));\n            }\n        }\n\
        \        return ans;\n    }\n}"
      python: "class Solution:\n    def minimumOneBitOperations(self, n: int) -> int:\n\
        \        ans = 0\n        while n > 0:\n            # Find k, the position of\
        \ the most significant bit (MSB) of n.\n            # For example, if n=6 (binary\
        \ 110), k=2.\n            # If n=5 (binary 101), k=2.\n            # n.bit_length()\
        \ returns the number of bits required to represent n in binary,\n          \
        \  # excluding the sign and leading zeros. So k = n.bit_length() - 1.\n    \
        \        k = n.bit_length() - 1 \n\n            # If n is 1, it's the base case\
        \ where k=0.\n            # f(1) = 1 operation.\n            if k == 0:\n  \
        \              ans += 1 # f(1) = 1\n                n = 0    # Done\n      \
        \      else:\n                # Add (1 << k) to the total operations.\n    \
        \            # This is derived from the recurrence f(n) = f(R ^ (1 << (k-1)))\
        \ + (1 << k)\n                # where R = n ^ (1 << k).\n                ans\
        \ += (1 << k)\n\n                # Update n for the next iteration.\n      \
        \          # n = n ^ (1 << k) ^ (1 << (k-1))\n                # This effectively\
        \ removes the k-th bit and flips the (k-1)-th bit.\n                n = n ^\
        \ (1 << k) ^ (1 << (k-1))\n\n        return ans"
      python3: "class Solution:\n    def minimumOneBitOperations(self, n: int) -> int:\n\
        \        ans = 0\n        while n > 0:\n            # Find k, the position of\
        \ the most significant bit (MSB) of n.\n            # For example, if n=6 (binary\
        \ 110), k=2.\n            # If n=5 (binary 101), k=2.\n            # n.bit_length()\
        \ returns the number of bits required to represent n in binary,\n          \
        \  # excluding the sign and leading zeros. So k = n.bit_length() - 1.\n    \
        \        k = n.bit_length() - 1 \n\n            # If n is 1, it's the base case\
        \ where k=0.\n            # f(1) = 1 operation.\n            if k == 0:\n  \
        \              ans += 1 # f(1) = 1\n                n = 0    # Done\n      \
        \      else:\n                # Add (1 << k) to the total operations.\n    \
        \            # This is derived from the recurrence f(n) = f(R ^ (1 << (k-1)))\
        \ + (1 << k)\n                # where R = n ^ (1 << k).\n                ans\
        \ += (1 << k)\n\n                # Update n for the next iteration.\n      \
        \          # n = n ^ (1 << k) ^ (1 << (k-1))\n                # This effectively\
        \ removes the k-th bit and flips the (k-1)-th bit.\n                n = n ^\
        \ (1 << k) ^ (1 << (k-1))\n\n        return ans"
      c: "#include <math.h>\n\n// Function to find MSB position (k) for a positive integer\
        \ n\n// This uses GCC's __builtin_clz. For other compilers, a loop or log2 might\
        \ be needed.\n// Assuming a 32-bit unsigned int for n. __builtin_clz(0) is undefined,\
        \ so n=0 is handled by the loop condition.\nint get_msb_pos(int n) {\n    //\
        \ For 32-bit int, 31 - number of leading zeros\n    return 31 - __builtin_clz(n);\n\
        }\n\nint minimumOneBitOperations(int n) {\n    int ans = 0;\n    while (n >\
        \ 0) {\n        // Find k, the position of the most significant bit (MSB) of\
        \ n.\n        // For n=1, k=0. For n=2, k=1. For n=4, k=2.\n        int k =\
        \ get_msb_pos(n);\n\n        // If n is 1, it's the base case where k=0.\n \
        \       // f(1) = 1 operation.\n        if (k == 0) {\n            ans += 1;\
        \ // f(1) = 1\n            n = 0;    // Done\n        } else {\n           \
        \ // Add (1 << k) to the total operations.\n            // This is derived from\
        \ the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)\n            // where\
        \ R = n ^ (1 << k).\n            ans += (1 << k);\n\n            // Update n\
        \ for the next iteration.\n            // n = n ^ (1 << k) ^ (1 << (k-1))\n\
        \            // This effectively removes the k-th bit and flips the (k-1)-th\
        \ bit.\n            n = n ^ (1 << k) ^ (1 << (k-1));\n        }\n    }\n   \
        \ return ans;\n}"
      csharp: "using System;\nusing System.Numerics;\n\npublic class Solution {\n  \
        \  public int MinimumOneBitOperations(int n) {\n        int ans = 0;\n     \
        \   while (n > 0) {\n            // Find k, the position of the most significant\
        \ bit (MSB) of n.\n            // For n=1, k=0. For n=2, k=1. For n=4, k=2.\n\
        \            // BitOperations.Log2(n) returns floor(log2(n)).\n            int\
        \ k = BitOperations.Log2((uint)n);\n\n            // If n is 1, it's the base\
        \ case where k=0.\n            // f(1) = 1 operation.\n            if (k ==\
        \ 0) {\n                ans += 1; // f(1) = 1\n                n = 0;    //\
        \ Done\n            } else {\n                // Add (1 << k) to the total operations.\n\
        \                // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1)))\
        \ + (1 << k)\n                // where R = n ^ (1 << k).\n                ans\
        \ += (1 << k);\n\n                // Update n for the next iteration.\n    \
        \            // n = n ^ (1 << k) ^ (1 << (k-1))\n                // This effectively\
        \ removes the k-th bit and flips the (k-1)-th bit.\n                n = n ^\
        \ (1 << k) ^ (1 << (k-1));\n            }\n        }\n        return ans;\n\
        \    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar minimumOneBitOperations\
        \ = function(n) {\n    let ans = 0;\n    while (n > 0) {\n        // Find k,\
        \ the position of the most significant bit (MSB) of n.\n        // For n=1,\
        \ k=0. For n=2, k=1. For n=4, k=2.\n        // Math.log2(n) returns log base\
        \ 2 of n. Math.floor() truncates to integer.\n        let k = Math.floor(Math.log2(n));\n\
        \n        // If n is 1, it's the base case where k=0.\n        // f(1) = 1 operation.\n\
        \        if (k === 0) {\n            ans += 1; // f(1) = 1\n            n =\
        \ 0;    // Done\n        } else {\n            // Add (1 << k) to the total\
        \ operations.\n            // This is derived from the recurrence f(n) = f(R\
        \ ^ (1 << (k-1))) + (1 << k)\n            // where R = n ^ (1 << k).\n     \
        \       ans += (1 << k);\n\n            // Update n for the next iteration.\n\
        \            // n = n ^ (1 << k) ^ (1 << (k-1))\n            // This effectively\
        \ removes the k-th bit and flips the (k-1)-th bit.\n            n = n ^ (1 <<\
        \ k) ^ (1 << (k-1));\n        }\n    }\n    return ans;\n};"
      typescript: "function minimumOneBitOperations(n: number): number {\n    let ans\
        \ = 0;\n    while (n > 0) {\n        // Find k, the position of the most significant\
        \ bit (MSB) of n.\n        // For n=1, k=0. For n=2, k=1. For n=4, k=2.\n  \
        \      // Math.log2(n) returns log base 2 of n. Math.floor() truncates to integer.\n\
        \        let k = Math.floor(Math.log2(n));\n\n        // If n is 1, it's the\
        \ base case where k=0.\n        // f(1) = 1 operation.\n        if (k === 0)\
        \ {\n            ans += 1; // f(1) = 1\n            n = 0;    // Done\n    \
        \    } else {\n            // Add (1 << k) to the total operations.\n      \
        \      // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1\
        \ << k)\n            // where R = n ^ (1 << k).\n            ans += (1 << k);\n\
        \n            // Update n for the next iteration.\n            // n = n ^ (1\
        \ << k) ^ (1 << (k-1))\n            // This effectively removes the k-th bit\
        \ and flips the (k-1)-th bit.\n            n = n ^ (1 << k) ^ (1 << (k-1));\n\
        \        }\n    }\n    return ans;\n}"
      php: "<?php\nclass Solution {\n    /**\n     * @param Integer $n\n     * @return\
        \ Integer\n     */\n    function minimumOneBitOperations($n) {\n        $ans\
        \ = 0;\n        while ($n > 0) {\n            // Find k, the position of the\
        \ most significant bit (MSB) of n.\n            // For n=1, k=0. For n=2, k=1.\
        \ For n=4, k=2.\n            // log($n, 2) returns log base 2 of n. floor()\
        \ truncates to integer.\n            $k = floor(log($n, 2));\n\n           \
        \ // If n is 1, it's the base case where k=0.\n            // f(1) = 1 operation.\n\
        \            if ($k === 0) {\n                $ans += 1; // f(1) = 1\n     \
        \           $n = 0;    // Done\n            } else {\n                // Add\
        \ (1 << k) to the total operations.\n                // This is derived from\
        \ the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)\n                // where\
        \ R = n ^ (1 << k).\n                $ans += (1 << $k);\n\n                //\
        \ Update n for the next iteration.\n                // n = n ^ (1 << k) ^ (1\
        \ << (k-1))\n                // This effectively removes the k-th bit and flips\
        \ the (k-1)-th bit.\n                $n = $n ^ (1 << $k) ^ (1 << ($k - 1));\n\
        \            }\n        }\n        return $ans;\n    }\n}"
      swift: "import Foundation\n\nclass Solution {\n    func minimumOneBitOperations(_\
        \ n: Int) -> Int {\n        var currentN = n\n        var ans = 0\n        while\
        \ currentN > 0 {\n            // Find k, the position of the most significant\
        \ bit (MSB) of currentN.\n            // For n=1, k=0. For n=2, k=1. For n=4,\
        \ k=2.\n            // For 32-bit integers, 31 - currentN.leadingZeroBitCount\
        \ gives k.\n            // Since n <= 10^9, it fits in 32 bits.\n          \
        \  let k = 31 - currentN.leadingZeroBitCount\n\n            // If currentN is\
        \ 1, it's the base case where k=0.\n            // f(1) = 1 operation.\n   \
        \         if k == 0 {\n                ans += 1 // f(1) = 1\n              \
        \  currentN = 0 // Done\n            } else {\n                // Add (1 <<\
        \ k) to the total operations.\n                // This is derived from the recurrence\
        \ f(n) = f(R ^ (1 << (k-1))) + (1 << k)\n                // where R = n ^ (1\
        \ << k).\n                ans += (1 << k)\n\n                // Update currentN\
        \ for the next iteration.\n                // currentN = currentN ^ (1 << k)\
        \ ^ (1 << (k-1))\n                // This effectively removes the k-th bit and\
        \ flips the (k-1)-th bit.\n                currentN = currentN ^ (1 << k) ^\
        \ (1 << (k-1))\n            }\n        }\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun minimumOneBitOperations(n: Int): Int {\n  \
        \      var currentN = n\n        var ans = 0\n        while (currentN > 0) {\n\
        \            // Find k, the position of the most significant bit (MSB) of currentN.\n\
        \            // For n=1, k=0. For n=2, k=1. For n=4, k=2.\n            // For\
        \ 32-bit integers, 31 - currentN.countLeadingZeroBits() gives k.\n         \
        \   val k = 31 - currentN.countLeadingZeroBits()\n\n            // If currentN\
        \ is 1, it's the base case where k=0.\n            // f(1) = 1 operation.\n\
        \            if (k == 0) {\n                ans += 1 // f(1) = 1\n         \
        \       currentN = 0 // Done\n            } else {\n                // Add (1\
        \ shl k) to the total operations.\n                // This is derived from the\
        \ recurrence f(n) = f(R ^ (1 shl (k-1))) + (1 shl k)\n                // where\
        \ R = n ^ (1 shl k).\n                ans += (1 shl k)\n\n                //\
        \ Update currentN for the next iteration.\n                // currentN = currentN\
        \ xor (1 shl k) xor (1 shl (k-1))\n                // This effectively removes\
        \ the k-th bit and flips the (k-1)-th bit.\n                currentN = currentN\
        \ xor (1 shl k) xor (1 shl (k - 1))\n            }\n        }\n        return\
        \ ans\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minimumOneBitOperations(int\
        \ n) {\n    int ans = 0;\n    while (n > 0) {\n      // Find k, the position\
        \ of the most significant bit (MSB) of n.\n      // For n=1, k=0. For n=2, k=1.\
        \ For n=4, k=2.\n      // n.bitLength returns the number of bits required to\
        \ represent n in binary.\n      // So k = n.bitLength - 1.\n      int k = n.bitLength\
        \ - 1;\n\n      // If n is 1, it's the base case where k=0.\n      // f(1) =\
        \ 1 operation.\n      if (k == 0) {\n        ans += 1; // f(1) = 1\n       \
        \ n = 0; // Done\n      } else {\n        // Add (1 << k) to the total operations.\n\
        \        // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) +\
        \ (1 << k)\n        // where R = n ^ (1 << k).\n        ans += (1 << k);\n\n\
        \        // Update n for the next iteration.\n        // n = n ^ (1 << k) ^\
        \ (1 << (k-1))\n        // This effectively removes the k-th bit and flips the\
        \ (k-1)-th bit.\n        n = n ^ (1 << k) ^ (1 << (k - 1));\n      }\n    }\n\
        \    return ans;\n  }\n}"
      go: "import (\n\t\"math/bits\"\n)\n\nfunc minimumOneBitOperations(n int) int {\n\
        \    ans := 0\n    for n > 0 {\n        // Find k, the position of the most\
        \ significant bit (MSB) of n.\n        // For n=1, k=0. For n=2, k=1. For n=4,\
        \ k=2.\n        // bits.Len(n) returns the minimum number of bits required to\
        \ represent n.\n        // So k = bits.Len(n) - 1.\n        k := bits.Len(n)\
        \ - 1\n\n        // If n is 1, it's the base case where k=0.\n        // f(1)\
        \ = 1 operation.\n        if k == 0 {\n            ans += 1 // f(1) = 1\n  \
        \          n = 0    // Done\n        } else {\n            // Add (1 << k) to\
        \ the total operations.\n            // This is derived from the recurrence\
        \ f(n) = f(R ^ (1 << (k-1))) + (1 << k)\n            // where R = n ^ (1 <<\
        \ k).\n            ans += (1 << k)\n\n            // Update n for the next iteration.\n\
        \            // n = n ^ (1 << k) ^ (1 << (k-1))\n            // This effectively\
        \ removes the k-th bit and flips the (k-1)-th bit.\n            n = n ^ (1 <<\
        \ k) ^ (1 << (k-1))\n        }\n    }\n    return ans\n}"
      ruby: "class Solution\n    # @param {Integer} n\n    # @return {Integer}\n   \
        \ def minimum_one_bit_operations(n)\n        ans = 0\n        while n > 0\n\
        \            # Find k, the position of the most significant bit (MSB) of n.\n\
        \            # For n=1, k=0. For n=2, k=1. For n=4, k=2.\n            # n.bit_length\
        \ returns the number of bits required to represent n in binary.\n          \
        \  # So k = n.bit_length - 1.\n            k = n.bit_length - 1\n\n        \
        \    # If n is 1, it's the base case where k=0.\n            # f(1) = 1 operation.\n\
        \            if k == 0\n                ans += 1 # f(1) = 1\n              \
        \  n = 0    # Done\n            else\n                # Add (1 << k) to the\
        \ total operations.\n                # This is derived from the recurrence f(n)\
        \ = f(R ^ (1 << (k-1))) + (1 << k)\n                # where R = n ^ (1 << k).\n\
        \                ans += (1 << k)\n\n                # Update n for the next\
        \ iteration.\n                # n = n ^ (1 << k) ^ (1 << (k-1))\n          \
        \      # This effectively removes the k-th bit and flips the (k-1)-th bit.\n\
        \                n = n ^ (1 << k) ^ (1 << (k - 1))\n            end\n      \
        \  end\n        ans\n    end\nend"
      scala: "import scala.annotation.tailrec\n\nobject Solution {\n    def minimumOneBitOperations(n:\
        \ Int): Int = {\n        @tailrec\n        def helper(currentN: Int, ans: Int):\
        \ Int = {\n            if (currentN == 0) {\n                ans\n         \
        \   } else {\n                // Find k, the position of the most significant\
        \ bit (MSB) of currentN.\n                // For n=1, k=0. For n=2, k=1. For\
        \ n=4, k=2.\n                // For 32-bit integers, 31 - Integer.numberOfLeadingZeros(currentN)\
        \ gives k.\n                val k = 31 - Integer.numberOfLeadingZeros(currentN)\n\
        \n                // If currentN is 1, it's the base case where k=0.\n     \
        \           // f(1) = 1 operation.\n                if (k == 0) {\n        \
        \            helper(0, ans + 1)\n                } else {\n                \
        \    // Add (1 << k) to the total operations.\n                    // This is\
        \ derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)\n      \
        \              // where R = n ^ (1 << k).\n                    val newAns =\
        \ ans + (1 << k)\n\n                    // Update currentN for the next iteration.\n\
        \                    // newN = currentN ^ (1 << k) ^ (1 << (k-1))\n        \
        \            // This effectively removes the k-th bit and flips the (k-1)-th\
        \ bit.\n                    val newN = currentN ^ (1 << k) ^ (1 << (k - 1))\n\
        \                    helper(newN, newAns)\n                }\n            }\n\
        \        }\n        helper(n, 0)\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_one_bit_operations(n: i32) -> i32 {\n\
        \        let mut current_n = n;\n        let mut ans = 0;\n\n        while current_n\
        \ > 0 {\n            // Find k, the position of the most significant bit (MSB)\
        \ of current_n.\n            // For n=1, k=0. For n=2, k=1. For n=4, k=2.\n\
        \            // For 32-bit integers, 31 - current_n.leading_zeros() gives k.\n\
        \            let k = 31 - current_n.leading_zeros();\n\n            // If current_n\
        \ is 1, it's the base case where k=0.\n            // f(1) = 1 operation.\n\
        \            if k == 0 {\n                ans += 1; // f(1) = 1\n          \
        \      current_n = 0; // Done\n            } else {\n                // Add\
        \ (1 << k) to the total operations.\n                // This is derived from\
        \ the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)\n                // where\
        \ R = n ^ (1 << k).\n                ans += (1 << k);\n\n                //\
        \ Update current_n for the next iteration.\n                // current_n = current_n\
        \ ^ (1 << k) ^ (1 << (k-1))\n                // This effectively removes the\
        \ k-th bit and flips the (k-1)-th bit.\n                current_n = current_n\
        \ ^ (1 << k) ^ (1 << (k - 1));\n            }\n        }\n        ans\n    }\n\
        }"
      racket: "#lang racket\n\n(define (minimum-one-bit-operations n)\n  (let loop ((current-n\
        \ n) (ans 0))\n    (if (= current-n 0)\n        ans\n        (let* ((k (floor\
        \ (log current-n 2)))) ; Find k, MSB position\n          (if (= k 0) ; Base\
        \ case for n=1 (k=0)\n              (loop 0 (+ ans 1))\n              (loop\
        \ (bitwise-xor current-n (bitwise-xor (arithmetic-shift 1 k) (arithmetic-shift\
        \ 1 (- k 1))))\n                    (+ ans (arithmetic-shift 1 k))))))))"
      erlang: "-module(solution).\n-export([minimum_one_bit_operations/1]).\n\nminimum_one_bit_operations(N)\
        \ ->\n    minimum_one_bit_operations_loop(N, 0).\n\nminimum_one_bit_operations_loop(0,\
        \ Ans) ->\n    Ans;\nminimum_one_bit_operations_loop(N, Ans) ->\n    K = trunc(math:log2(N)),\
        \ % Find k, MSB position\n    if K == 0 -> % Base case for N=1 (k=0)\n     \
        \   minimum_one_bit_operations_loop(0, Ans + 1);\n    true ->\n        NewAns\
        \ = Ans + (1 bsl K),\n        NewN = N bxor ((1 bsl K) bxor (1 bsl (K - 1))),\n\
        \        minimum_one_bit_operations_loop(NewN, NewAns)\n    end."
      elixir: "defmodule Solution do\n  @spec minimum_one_bit_operations(n :: integer)\
        \ :: integer\n  def minimum_one_bit_operations(n) do\n    do_minimum_one_bit_operations(n,\
        \ 0)\n  end\n\n  defp do_minimum_one_bit_operations(0, ans), do: ans\n  defp\
        \ do_minimum_one_bit_operations(n, ans) do\n    k = floor(:math.log2(n)) # Find\
        \ k, MSB position\n\n    if k == 0 do # Base case for n=1 (k=0)\n      do_minimum_one_bit_operations(0,\
        \ ans + 1)\n    else\n      new_ans = ans + (1 <<< k)\n      new_n = Bitwise.bxor(n,\
        \ Bitwise.bxor(1 <<< k, 1 <<< (k - 1)))\n      do_minimum_one_bit_operations(new_n,\
        \ new_ans)\n    end\n  end\nend"
    approach: 'The problem asks for the minimum number of operations to transform an
      integer `n` into `0`. We are given two types of operations: (1) change the rightmost
      (0th) bit, and (2) change the `i`-th bit if the `(i-1)`-th bit is `1` and bits
      `(i-2)` through `0` are `0`.


      Let `f(n)` be the minimum operations to transform `n` to `0`. Observing the pattern
      for small values of `n` reveals a sequence: `f(0)=0, f(1)=1, f(2)=3, f(3)=2, f(4)=7,
      f(5)=6, f(6)=4, f(7)=5`. This sequence is precisely the inverse mapping of a specific
      type of Gray code (often referred to as ''reflected binary code''). The operations
      described are the rules for generating this Gray code sequence. Therefore, `f(n)`
      is the ''rank'' of `n` in this Gray code sequence, meaning if `n` is the `k`-th
      element in this sequence (starting from 0), then `f(n) = k`.


      The solution leverages a recursive structure that can be converted into an iterative
      approach. Let `k` be the position of the most significant bit (MSB) of `n`. For
      example, if `n=6` (binary `110`), `k=2`. If `n=5` (binary `101`), `k=2`. The strategy
      is to iteratively turn off the MSB of the current number. To turn off the `k`-th
      bit, we need to reach a state where the `k`-th bit is `1`, the `(k-1)`-th bit
      is `1`, and all bits from `0` to `(k-2)` are `0`. From this state, operation 2
      can be applied to flip the `k`-th bit. This process leads to the recurrence relation:
      `f(n) = f( (n ^ (1 << k)) ^ (1 << (k-1)) ) + (1 << k)`. Here, `(1 << k)` is the
      cost associated with handling the `k`-th bit and preparing for the next step.
      The term `(n ^ (1 << k))` effectively removes the MSB of `n`, and `^ (1 << (k-1))`
      flips the `(k-1)`-th bit to set up the conditions for the next MSB to be processed.
      The base cases are `f(0) = 0` and `f(1) = 1`. The iterative implementation repeatedly
      finds the MSB `k`, adds `(1 << k)` to the total operations, and updates `n` using
      the transformation `n = n ^ (1 << k) ^ (1 << (k-1))`. A special check is included
      for `k=0` (when `n=1`) to handle the base case and avoid issues with `(1 << -1)`.'
    time_complexity: O(log n)
    space_complexity: O(1)
    elapsed_time: 117.20352983474731
    model: gemini-2.5-flash
    generated_at: '2025-11-24 20:59:43 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumOneBitOperations(int n) {\n  \
        \      if (n == 0) return 0;\n        int res = 1;\n        int cnt = 1;\n \
        \       while (n > 1) {\n            if (n % 2 == 1) {\n                res\
        \ = 2 * cnt - res;\n            }\n            cnt *= 2;\n            n /= 2;\n\
        \        }\n        return res;\n    }\n}"
      java: "class Solution {\n    public int minimumOneBitOperations(int n) {\n   \
        \     if (n == 0) return 0;\n        int res = 1;\n        int cnt = 1;\n  \
        \      while (n > 1) {\n            if (n % 2 == 1) {\n                res =\
        \ 2 * cnt - res;\n            }\n            cnt *= 2;\n            n /= 2;\n\
        \        }\n        return res;\n    }\n}"
      python: "class Solution:\n    def minimumOneBitOperations(self, n: int) -> int:\n\
        \        if n == 0:\n            return 0\n        res = 1\n        cnt = 1\n\
        \        while n > 1:\n            if n % 2 == 1:\n                res = 2 *\
        \ cnt - res\n            cnt *= 2\n            n //= 2\n        return res"
      python3: "class Solution:\n    def minimumOneBitOperations(self, n: int) -> int:\n\
        \        if n == 0:\n            return 0\n        res = 1\n        cnt = 1\n\
        \        while n > 1:\n            if n % 2 == 1:\n                res = 2 *\
        \ cnt - res\n            cnt *= 2\n            n //= 2\n        return res"
      c: "#include <stdio.h>\n\nint minimumOneBitOperations(int n) {\n    if (n == 0)\
        \ return 0;\n    int res = 1;\n    int cnt = 1;\n    while (n > 1) {\n     \
        \   if (n % 2 == 1) {\n            res = 2 * cnt - res;\n        }\n       \
        \ cnt *= 2;\n        n /= 2;\n    }\n    return res;\n}"
      csharp: "public class Solution {\n    public int MinimumOneBitOperations(int n)\
        \ {\n        if (n == 0) return 0;\n        int res = 1;\n        int cnt =\
        \ 1;\n        while (n > 1) {\n            if (n % 2 == 1) {\n             \
        \   res = 2 * cnt - res;\n            }\n            cnt *= 2;\n           \
        \ n /= 2;\n        }\n        return res;\n    }\n}"
      javascript: "var minimumOneBitOperations = function(n) {\n    if (n == 0) return\
        \ 0;\n    let res = 1;\n    let cnt = 1;\n    while (n > 1) {\n        if (n\
        \ % 2 == 1) {\n            res = 2 * cnt - res;\n        }\n        cnt *= 2;\n\
        \        n = Math.floor(n / 2);\n    }\n    return res;\n};"
      typescript: "function minimumOneBitOperations(n: number): number {\n    if (n\
        \ == 0) return 0;\n    let res: number = 1;\n    let cnt: number = 1;\n    while\
        \ (n > 1) {\n        if (n % 2 == 1) {\n            res = 2 * cnt - res;\n \
        \       }\n        cnt *= 2;\n        n = Math.floor(n / 2);\n    }\n    return\
        \ res;\n}"
      php: "class Solution {\n    function minimumOneBitOperations($n) {\n        if\
        \ ($n == 0) return 0;\n        $res = 1;\n        $cnt = 1;\n        while ($n\
        \ > 1) {\n            if ($n % 2 == 1) {\n                $res = 2 * $cnt -\
        \ $res;\n            }\n            $cnt *= 2;\n            $n = floor($n /\
        \ 2);\n        }\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func minimumOneBitOperations(_ n: Int) -> Int {\n\
        \        if n == 0 {\n            return 0\n        }\n        var res = 1\n\
        \        var cnt = 1\n        var n = n\n        while n > 1 {\n           \
        \ if n % 2 == 1 {\n                res = 2 * cnt - res\n            }\n    \
        \        cnt *= 2\n            n /= 2\n        }\n        return res\n    }\n\
        }"
      kotlin: "class Solution {\n    fun minimumOneBitOperations(n: Int): Int {\n  \
        \      if (n == 0) return 0\n        var res = 1\n        var cnt = 1\n    \
        \    var n = n\n        while (n > 1) {\n            if (n % 2 == 1) {\n   \
        \             res = 2 * cnt - res\n            }\n            cnt *= 2\n   \
        \         n /= 2\n        }\n        return res\n    }\n}"
      dart: "class Solution {\n    int minimumOneBitOperations(int n) {\n        if\
        \ (n == 0) return 0;\n        int res = 1;\n        int cnt = 1;\n        while\
        \ (n > 1) {\n            if (n % 2 == 1) {\n                res = 2 * cnt -\
        \ res;\n            }\n            cnt *= 2;\n            n = n ~/ 2;\n    \
        \    }\n        return res;\n    }\n}"
      go: "package main\n\nimport \"fmt\"\n\nfunc minimumOneBitOperations(n int) int\
        \ {\n    if n == 0 {\n        return 0\n    }\n    res := 1\n    cnt := 1\n\
        \    for n > 1 {\n        if n%2 == 1 {\n            res = 2*cnt - res\n   \
        \     }\n        cnt *= 2\n        n /= 2\n    }\n    return res\n}"
      ruby: "def minimum_one_bit_operations(n)\n    if n == 0\n        return 0\n  \
        \  end\n    res = 1\n    cnt = 1\n    while n > 1\n        if n % 2 == 1\n \
        \           res = 2 * cnt - res\n        end\n        cnt *= 2\n        n /=\
        \ 2\n    end\n    res\nend"
      scala: "object Solution {\n    def minimumOneBitOperations(n: Int): Int = {\n\
        \        if (n == 0) return 0\n        var res = 1\n        var cnt = 1\n  \
        \      var nVar = n\n        while (nVar > 1) {\n            if (nVar % 2 ==\
        \ 1) {\n                res = 2 * cnt - res\n            }\n            cnt\
        \ *= 2\n            nVar /= 2\n        }\n        res\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_one_bit_operations(n: i32) -> i32 {\n\
        \        if n == 0 {\n            return 0;\n        }\n        let mut res\
        \ = 1;\n        let mut cnt = 1;\n        let mut n = n;\n        while n >\
        \ 1 {\n            if n % 2 == 1 {\n                res = 2 * cnt - res;\n \
        \           }\n            cnt *= 2;\n            n /= 2;\n        }\n     \
        \   res\n    }\n}"
      racket: "#lang racket\n(define (minimum-one-bit-operations n)\n  (if (= n 0)\n\
        \      0\n      (let loop ((res 1) (cnt 1) (n n))\n        (if (> n 1)\n   \
        \         (if (= (remainder n 2) 1)\n                (loop (- (* 2 cnt) res)\
        \ (* 2 cnt) (quotient n 2))\n                (loop res (* 2 cnt) (quotient n\
        \ 2)))\n            res))))"
      erlang: "-module(solution).\n-export([minimum_one_bit_operations/1]).\n\nminimum_one_bit_operations(0)\
        \ -> 0;\nminimum_one_bit_operations(N) ->\n    minimum_one_bit_operations(N,\
        \ 1, 1).\n\nminimum_one_bit_operations(N, Res, Cnt) when N > 1 ->\n    case\
        \ N rem 2 of\n        1 -> minimum_one_bit_operations(N div 2, 2 * Cnt - Res,\
        \ 2 * Cnt);\n        0 -> minimum_one_bit_operations(N div 2, Res, 2 * Cnt)\n\
        \    end;\nminimum_one_bit_operations(_, Res, _) -> Res."
      elixir: "defmodule Solution do\n  def minimum_one_bit_operations(0), do: 0\n \
        \ def minimum_one_bit_operations(n) do\n    minimum_one_bit_operations(n, 1,\
        \ 1)\n  end\n\n  defp minimum_one_bit_operations(n, res, cnt) when n > 1 do\n\
        \    case rem(n, 2) do\n      1 -> minimum_one_bit_operations(div(n, 2), 2 *\
        \ cnt - res, 2 * cnt)\n      0 -> minimum_one_bit_operations(div(n, 2), res,\
        \ 2 * cnt)\n    end\n  end\n\n  defp minimum_one_bit_operations(_, res, _),\
        \ do: res\nend"
    approach: The problem can be solved by using the properties of binary numbers and
      the given operations. The first operation allows us to change the rightmost bit,
      and the second operation allows us to change any bit if the previous bit is 1
      and all bits to its right are 0. We can use these operations to remove all set
      bits from the binary representation of n, starting from the leftmost set bit.
      The key observation is that the minimum number of operations required to remove
      a set bit is equal to the number of bits to its right plus 1. This is because
      we need to change the rightmost bit and then change all bits to its left that
      are set. We can use this observation to calculate the minimum number of operations
      required to remove all set bits from n.
    time_complexity: O(log n) because we need to iterate over the bits of n, and the
      number of bits in n is proportional to log n.
    space_complexity: O(1) because we only need a constant amount of space to store
      the result and the current bit being processed.
    elapsed_time: 4.993774652481079
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-24 20:59:48 '
---

## Problem #1611: Minimum One Bit Operations to Make Integers Zero

**Difficulty:** Hard

**Topics:** Dynamic Programming, Bit Manipulation, Memoization

## Problem Description

<p>Given an integer <code>n</code>, you must transform it into <code>0</code> using the following operations any number of times:</p>

<ul>
	<li>Change the rightmost (<code>0<sup>th</sup></code>) bit in the binary representation of <code>n</code>.</li>
	<li>Change the <code>i<sup>th</sup></code> bit in the binary representation of <code>n</code> if the <code>(i-1)<sup>th</sup></code> bit is set to <code>1</code> and the <code>(i-2)<sup>th</sup></code> through <code>0<sup>th</sup></code> bits are set to <code>0</code>.</li>
</ul>

<p>Return <em>the minimum number of operations to transform </em><code>n</code><em> into </em><code>0</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> The binary representation of 3 is &quot;11&quot;.
&quot;<u>1</u>1&quot; -&gt; &quot;<u>0</u>1&quot; with the 2<sup>nd</sup> operation since the 0<sup>th</sup> bit is 1.
&quot;0<u>1</u>&quot; -&gt; &quot;0<u>0</u>&quot; with the 1<sup>st</sup> operation.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 4
<strong>Explanation:</strong> The binary representation of 6 is &quot;110&quot;.
&quot;<u>1</u>10&quot; -&gt; &quot;<u>0</u>10&quot; with the 2<sup>nd</sup> operation since the 1<sup>st</sup> bit is 1 and 0<sup>th</sup> through 0<sup>th</sup> bits are 0.
&quot;01<u>0</u>&quot; -&gt; &quot;01<u>1</u>&quot; with the 1<sup>st</sup> operation.
&quot;0<u>1</u>1&quot; -&gt; &quot;0<u>0</u>1&quot; with the 2<sup>nd</sup> operation since the 0<sup>th</sup> bit is 1.
&quot;00<u>1</u>&quot; -&gt; &quot;00<u>0</u>&quot; with the 1<sup>st</sup> operation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. The fastest way to convert n to zero is to remove all set bits starting from the leftmost one. Try some simple examples to learn the rule of how many steps are needed to remove one set bit.

2. consider n=2^k case first, then solve for all n.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-24 20:59:43 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the minimum number of operations to transform an integer `n` into `0`. We are given two types of operations: (1) change the rightmost (0th) bit, and (2) change the `i`-th bit if the `(i-1)`-th bit is `1` and bits `(i-2)` through `0` are `0`.

Let `f(n)` be the minimum operations to transform `n` to `0`. Observing the pattern for small values of `n` reveals a sequence: `f(0)=0, f(1)=1, f(2)=3, f(3)=2, f(4)=7, f(5)=6, f(6)=4, f(7)=5`. This sequence is precisely the inverse mapping of a specific type of Gray code (often referred to as 'reflected binary code'). The operations described are the rules for generating this Gray code sequence. Therefore, `f(n)` is the 'rank' of `n` in this Gray code sequence, meaning if `n` is the `k`-th element in this sequence (starting from 0), then `f(n) = k`.

The solution leverages a recursive structure that can be converted into an iterative approach. Let `k` be the position of the most significant bit (MSB) of `n`. For example, if `n=6` (binary `110`), `k=2`. If `n=5` (binary `101`), `k=2`. The strategy is to iteratively turn off the MSB of the current number. To turn off the `k`-th bit, we need to reach a state where the `k`-th bit is `1`, the `(k-1)`-th bit is `1`, and all bits from `0` to `(k-2)` are `0`. From this state, operation 2 can be applied to flip the `k`-th bit. This process leads to the recurrence relation: `f(n) = f( (n ^ (1 << k)) ^ (1 << (k-1)) ) + (1 << k)`. Here, `(1 << k)` is the cost associated with handling the `k`-th bit and preparing for the next step. The term `(n ^ (1 << k))` effectively removes the MSB of `n`, and `^ (1 << (k-1))` flips the `(k-1)`-th bit to set up the conditions for the next MSB to be processed. The base cases are `f(0) = 0` and `f(1) = 1`. The iterative implementation repeatedly finds the MSB `k`, adds `(1 << k)` to the total operations, and updates `n` using the transformation `n = n ^ (1 << k) ^ (1 << (k-1))`. A special check is included for `k=0` (when `n=1`) to handle the base case and avoid issues with `(1 << -1)`.

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
class Solution {
public:
    int minimumOneBitOperations(int n) {
        int ans = 0;
        while (n > 0) {
            // Find k, the position of the most significant bit (MSB) of n.
            // For n=1, k=0. For n=2, k=1. For n=4, k=2.
            // For 32-bit integers, 31 - __builtin_clz(n) gives k.
            int k = 31 - __builtin_clz(n);

            // If n is 1, it's the base case where k=0.
            // f(1) = 1 operation.
            if (k == 0) {
                ans += 1;
                n = 0; // Done
            } else {
                // Add (1 << k) to the total operations.
                // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
                // where R = n ^ (1 << k).
                ans += (1 << k);

                // Update n for the next iteration.
                // n = n ^ (1 << k) ^ (1 << (k-1))
                // This effectively removes the k-th bit and flips the (k-1)-th bit.
                n = n ^ (1 << k) ^ (1 << (k-1));
            }
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
import java.lang.Integer;

class Solution {
    public int minimumOneBitOperations(int n) {
        int ans = 0;
        while (n > 0) {
            // Find k, the position of the most significant bit (MSB) of n.
            // For n=1, k=0. For n=2, k=1. For n=4, k=2.
            // Integer.numberOfLeadingZeros(n) returns the number of zero bits preceding the highest-set bit.
            // For 32-bit integers, 31 - Integer.numberOfLeadingZeros(n) gives k.
            int k = 31 - Integer.numberOfLeadingZeros(n);

            // If n is 1, it's the base case where k=0.
            // f(1) = 1 operation.
            if (k == 0) {
                ans += 1;
                n = 0; // Done
            } else {
                // Add (1 << k) to the total operations.
                // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
                // where R = n ^ (1 << k).
                ans += (1 << k);

                // Update n for the next iteration.
                // n = n ^ (1 << k) ^ (1 << (k-1))
                // This effectively removes the k-th bit and flips the (k-1)-th bit.
                n = n ^ (1 << k) ^ (1 << (k-1));
            }
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
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            # Find k, the position of the most significant bit (MSB) of n.
            # For example, if n=6 (binary 110), k=2.
            # If n=5 (binary 101), k=2.
            # n.bit_length() returns the number of bits required to represent n in binary,
            # excluding the sign and leading zeros. So k = n.bit_length() - 1.
            k = n.bit_length() - 1 

            # If n is 1, it's the base case where k=0.
            # f(1) = 1 operation.
            if k == 0:
                ans += 1 # f(1) = 1
                n = 0    # Done
            else:
                # Add (1 << k) to the total operations.
                # This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
                # where R = n ^ (1 << k).
                ans += (1 << k)

                # Update n for the next iteration.
                # n = n ^ (1 << k) ^ (1 << (k-1))
                # This effectively removes the k-th bit and flips the (k-1)-th bit.
                n = n ^ (1 << k) ^ (1 << (k-1))

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            # Find k, the position of the most significant bit (MSB) of n.
            # For example, if n=6 (binary 110), k=2.
            # If n=5 (binary 101), k=2.
            # n.bit_length() returns the number of bits required to represent n in binary,
            # excluding the sign and leading zeros. So k = n.bit_length() - 1.
            k = n.bit_length() - 1 

            # If n is 1, it's the base case where k=0.
            # f(1) = 1 operation.
            if k == 0:
                ans += 1 # f(1) = 1
                n = 0    # Done
            else:
                # Add (1 << k) to the total operations.
                # This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
                # where R = n ^ (1 << k).
                ans += (1 << k)

                # Update n for the next iteration.
                # n = n ^ (1 << k) ^ (1 << (k-1))
                # This effectively removes the k-th bit and flips the (k-1)-th bit.
                n = n ^ (1 << k) ^ (1 << (k-1))

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <math.h>

// Function to find MSB position (k) for a positive integer n
// This uses GCC's __builtin_clz. For other compilers, a loop or log2 might be needed.
// Assuming a 32-bit unsigned int for n. __builtin_clz(0) is undefined, so n=0 is handled by the loop condition.
int get_msb_pos(int n) {
    // For 32-bit int, 31 - number of leading zeros
    return 31 - __builtin_clz(n);
}

int minimumOneBitOperations(int n) {
    int ans = 0;
    while (n > 0) {
        // Find k, the position of the most significant bit (MSB) of n.
        // For n=1, k=0. For n=2, k=1. For n=4, k=2.
        int k = get_msb_pos(n);

        // If n is 1, it's the base case where k=0.
        // f(1) = 1 operation.
        if (k == 0) {
            ans += 1; // f(1) = 1
            n = 0;    // Done
        } else {
            // Add (1 << k) to the total operations.
            // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
            // where R = n ^ (1 << k).
            ans += (1 << k);

            // Update n for the next iteration.
            // n = n ^ (1 << k) ^ (1 << (k-1))
            // This effectively removes the k-th bit and flips the (k-1)-th bit.
            n = n ^ (1 << k) ^ (1 << (k-1));
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Numerics;

public class Solution {
    public int MinimumOneBitOperations(int n) {
        int ans = 0;
        while (n > 0) {
            // Find k, the position of the most significant bit (MSB) of n.
            // For n=1, k=0. For n=2, k=1. For n=4, k=2.
            // BitOperations.Log2(n) returns floor(log2(n)).
            int k = BitOperations.Log2((uint)n);

            // If n is 1, it's the base case where k=0.
            // f(1) = 1 operation.
            if (k == 0) {
                ans += 1; // f(1) = 1
                n = 0;    // Done
            } else {
                // Add (1 << k) to the total operations.
                // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
                // where R = n ^ (1 << k).
                ans += (1 << k);

                // Update n for the next iteration.
                // n = n ^ (1 << k) ^ (1 << (k-1))
                // This effectively removes the k-th bit and flips the (k-1)-th bit.
                n = n ^ (1 << k) ^ (1 << (k-1));
            }
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
 * @param {number} n
 * @return {number}
 */
var minimumOneBitOperations = function(n) {
    let ans = 0;
    while (n > 0) {
        // Find k, the position of the most significant bit (MSB) of n.
        // For n=1, k=0. For n=2, k=1. For n=4, k=2.
        // Math.log2(n) returns log base 2 of n. Math.floor() truncates to integer.
        let k = Math.floor(Math.log2(n));

        // If n is 1, it's the base case where k=0.
        // f(1) = 1 operation.
        if (k === 0) {
            ans += 1; // f(1) = 1
            n = 0;    // Done
        } else {
            // Add (1 << k) to the total operations.
            // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
            // where R = n ^ (1 << k).
            ans += (1 << k);

            // Update n for the next iteration.
            // n = n ^ (1 << k) ^ (1 << (k-1))
            // This effectively removes the k-th bit and flips the (k-1)-th bit.
            n = n ^ (1 << k) ^ (1 << (k-1));
        }
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumOneBitOperations(n: number): number {
    let ans = 0;
    while (n > 0) {
        // Find k, the position of the most significant bit (MSB) of n.
        // For n=1, k=0. For n=2, k=1. For n=4, k=2.
        // Math.log2(n) returns log base 2 of n. Math.floor() truncates to integer.
        let k = Math.floor(Math.log2(n));

        // If n is 1, it's the base case where k=0.
        // f(1) = 1 operation.
        if (k === 0) {
            ans += 1; // f(1) = 1
            n = 0;    // Done
        } else {
            // Add (1 << k) to the total operations.
            // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
            // where R = n ^ (1 << k).
            ans += (1 << k);

            // Update n for the next iteration.
            // n = n ^ (1 << k) ^ (1 << (k-1))
            // This effectively removes the k-th bit and flips the (k-1)-th bit.
            n = n ^ (1 << k) ^ (1 << (k-1));
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function minimumOneBitOperations($n) {
        $ans = 0;
        while ($n > 0) {
            // Find k, the position of the most significant bit (MSB) of n.
            // For n=1, k=0. For n=2, k=1. For n=4, k=2.
            // log($n, 2) returns log base 2 of n. floor() truncates to integer.
            $k = floor(log($n, 2));

            // If n is 1, it's the base case where k=0.
            // f(1) = 1 operation.
            if ($k === 0) {
                $ans += 1; // f(1) = 1
                $n = 0;    // Done
            } else {
                // Add (1 << k) to the total operations.
                // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
                // where R = n ^ (1 << k).
                $ans += (1 << $k);

                // Update n for the next iteration.
                // n = n ^ (1 << k) ^ (1 << (k-1))
                // This effectively removes the k-th bit and flips the (k-1)-th bit.
                $n = $n ^ (1 << $k) ^ (1 << ($k - 1));
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
import Foundation

class Solution {
    func minimumOneBitOperations(_ n: Int) -> Int {
        var currentN = n
        var ans = 0
        while currentN > 0 {
            // Find k, the position of the most significant bit (MSB) of currentN.
            // For n=1, k=0. For n=2, k=1. For n=4, k=2.
            // For 32-bit integers, 31 - currentN.leadingZeroBitCount gives k.
            // Since n <= 10^9, it fits in 32 bits.
            let k = 31 - currentN.leadingZeroBitCount

            // If currentN is 1, it's the base case where k=0.
            // f(1) = 1 operation.
            if k == 0 {
                ans += 1 // f(1) = 1
                currentN = 0 // Done
            } else {
                // Add (1 << k) to the total operations.
                // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
                // where R = n ^ (1 << k).
                ans += (1 << k)

                // Update currentN for the next iteration.
                // currentN = currentN ^ (1 << k) ^ (1 << (k-1))
                // This effectively removes the k-th bit and flips the (k-1)-th bit.
                currentN = currentN ^ (1 << k) ^ (1 << (k-1))
            }
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
    fun minimumOneBitOperations(n: Int): Int {
        var currentN = n
        var ans = 0
        while (currentN > 0) {
            // Find k, the position of the most significant bit (MSB) of currentN.
            // For n=1, k=0. For n=2, k=1. For n=4, k=2.
            // For 32-bit integers, 31 - currentN.countLeadingZeroBits() gives k.
            val k = 31 - currentN.countLeadingZeroBits()

            // If currentN is 1, it's the base case where k=0.
            // f(1) = 1 operation.
            if (k == 0) {
                ans += 1 // f(1) = 1
                currentN = 0 // Done
            } else {
                // Add (1 shl k) to the total operations.
                // This is derived from the recurrence f(n) = f(R ^ (1 shl (k-1))) + (1 shl k)
                // where R = n ^ (1 shl k).
                ans += (1 shl k)

                // Update currentN for the next iteration.
                // currentN = currentN xor (1 shl k) xor (1 shl (k-1))
                // This effectively removes the k-th bit and flips the (k-1)-th bit.
                currentN = currentN xor (1 shl k) xor (1 shl (k - 1))
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
  int minimumOneBitOperations(int n) {
    int ans = 0;
    while (n > 0) {
      // Find k, the position of the most significant bit (MSB) of n.
      // For n=1, k=0. For n=2, k=1. For n=4, k=2.
      // n.bitLength returns the number of bits required to represent n in binary.
      // So k = n.bitLength - 1.
      int k = n.bitLength - 1;

      // If n is 1, it's the base case where k=0.
      // f(1) = 1 operation.
      if (k == 0) {
        ans += 1; // f(1) = 1
        n = 0; // Done
      } else {
        // Add (1 << k) to the total operations.
        // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
        // where R = n ^ (1 << k).
        ans += (1 << k);

        // Update n for the next iteration.
        // n = n ^ (1 << k) ^ (1 << (k-1))
        // This effectively removes the k-th bit and flips the (k-1)-th bit.
        n = n ^ (1 << k) ^ (1 << (k - 1));
      }
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
import (
	"math/bits"
)

func minimumOneBitOperations(n int) int {
    ans := 0
    for n > 0 {
        // Find k, the position of the most significant bit (MSB) of n.
        // For n=1, k=0. For n=2, k=1. For n=4, k=2.
        // bits.Len(n) returns the minimum number of bits required to represent n.
        // So k = bits.Len(n) - 1.
        k := bits.Len(n) - 1

        // If n is 1, it's the base case where k=0.
        // f(1) = 1 operation.
        if k == 0 {
            ans += 1 // f(1) = 1
            n = 0    // Done
        } else {
            // Add (1 << k) to the total operations.
            // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
            // where R = n ^ (1 << k).
            ans += (1 << k)

            // Update n for the next iteration.
            // n = n ^ (1 << k) ^ (1 << (k-1))
            // This effectively removes the k-th bit and flips the (k-1)-th bit.
            n = n ^ (1 << k) ^ (1 << (k-1))
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
class Solution
    # @param {Integer} n
    # @return {Integer}
    def minimum_one_bit_operations(n)
        ans = 0
        while n > 0
            # Find k, the position of the most significant bit (MSB) of n.
            # For n=1, k=0. For n=2, k=1. For n=4, k=2.
            # n.bit_length returns the number of bits required to represent n in binary.
            # So k = n.bit_length - 1.
            k = n.bit_length - 1

            # If n is 1, it's the base case where k=0.
            # f(1) = 1 operation.
            if k == 0
                ans += 1 # f(1) = 1
                n = 0    # Done
            else
                # Add (1 << k) to the total operations.
                # This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
                # where R = n ^ (1 << k).
                ans += (1 << k)

                # Update n for the next iteration.
                # n = n ^ (1 << k) ^ (1 << (k-1))
                # This effectively removes the k-th bit and flips the (k-1)-th bit.
                n = n ^ (1 << k) ^ (1 << (k - 1))
            end
        end
        ans
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.annotation.tailrec

object Solution {
    def minimumOneBitOperations(n: Int): Int = {
        @tailrec
        def helper(currentN: Int, ans: Int): Int = {
            if (currentN == 0) {
                ans
            } else {
                // Find k, the position of the most significant bit (MSB) of currentN.
                // For n=1, k=0. For n=2, k=1. For n=4, k=2.
                // For 32-bit integers, 31 - Integer.numberOfLeadingZeros(currentN) gives k.
                val k = 31 - Integer.numberOfLeadingZeros(currentN)

                // If currentN is 1, it's the base case where k=0.
                // f(1) = 1 operation.
                if (k == 0) {
                    helper(0, ans + 1)
                } else {
                    // Add (1 << k) to the total operations.
                    // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
                    // where R = n ^ (1 << k).
                    val newAns = ans + (1 << k)

                    // Update currentN for the next iteration.
                    // newN = currentN ^ (1 << k) ^ (1 << (k-1))
                    // This effectively removes the k-th bit and flips the (k-1)-th bit.
                    val newN = currentN ^ (1 << k) ^ (1 << (k - 1))
                    helper(newN, newAns)
                }
            }
        }
        helper(n, 0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_one_bit_operations(n: i32) -> i32 {
        let mut current_n = n;
        let mut ans = 0;

        while current_n > 0 {
            // Find k, the position of the most significant bit (MSB) of current_n.
            // For n=1, k=0. For n=2, k=1. For n=4, k=2.
            // For 32-bit integers, 31 - current_n.leading_zeros() gives k.
            let k = 31 - current_n.leading_zeros();

            // If current_n is 1, it's the base case where k=0.
            // f(1) = 1 operation.
            if k == 0 {
                ans += 1; // f(1) = 1
                current_n = 0; // Done
            } else {
                // Add (1 << k) to the total operations.
                // This is derived from the recurrence f(n) = f(R ^ (1 << (k-1))) + (1 << k)
                // where R = n ^ (1 << k).
                ans += (1 << k);

                // Update current_n for the next iteration.
                // current_n = current_n ^ (1 << k) ^ (1 << (k-1))
                // This effectively removes the k-th bit and flips the (k-1)-th bit.
                current_n = current_n ^ (1 << k) ^ (1 << (k - 1));
            }
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
#lang racket

(define (minimum-one-bit-operations n)
  (let loop ((current-n n) (ans 0))
    (if (= current-n 0)
        ans
        (let* ((k (floor (log current-n 2)))) ; Find k, MSB position
          (if (= k 0) ; Base case for n=1 (k=0)
              (loop 0 (+ ans 1))
              (loop (bitwise-xor current-n (bitwise-xor (arithmetic-shift 1 k) (arithmetic-shift 1 (- k 1))))
                    (+ ans (arithmetic-shift 1 k))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([minimum_one_bit_operations/1]).

minimum_one_bit_operations(N) ->
    minimum_one_bit_operations_loop(N, 0).

minimum_one_bit_operations_loop(0, Ans) ->
    Ans;
minimum_one_bit_operations_loop(N, Ans) ->
    K = trunc(math:log2(N)), % Find k, MSB position
    if K == 0 -> % Base case for N=1 (k=0)
        minimum_one_bit_operations_loop(0, Ans + 1);
    true ->
        NewAns = Ans + (1 bsl K),
        NewN = N bxor ((1 bsl K) bxor (1 bsl (K - 1))),
        minimum_one_bit_operations_loop(NewN, NewAns)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_one_bit_operations(n :: integer) :: integer
  def minimum_one_bit_operations(n) do
    do_minimum_one_bit_operations(n, 0)
  end

  defp do_minimum_one_bit_operations(0, ans), do: ans
  defp do_minimum_one_bit_operations(n, ans) do
    k = floor(:math.log2(n)) # Find k, MSB position

    if k == 0 do # Base case for n=1 (k=0)
      do_minimum_one_bit_operations(0, ans + 1)
    else
      new_ans = ans + (1 <<< k)
      new_n = Bitwise.bxor(n, Bitwise.bxor(1 <<< k, 1 <<< (k - 1)))
      do_minimum_one_bit_operations(new_n, new_ans)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n)

- **Space Complexity:** O(1)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-24 20:59:48 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using the properties of binary numbers and the given operations. The first operation allows us to change the rightmost bit, and the second operation allows us to change any bit if the previous bit is 1 and all bits to its right are 0. We can use these operations to remove all set bits from the binary representation of n, starting from the leftmost set bit. The key observation is that the minimum number of operations required to remove a set bit is equal to the number of bits to its right plus 1. This is because we need to change the rightmost bit and then change all bits to its left that are set. We can use this observation to calculate the minimum number of operations required to remove all set bits from n.

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
    int minimumOneBitOperations(int n) {
        if (n == 0) return 0;
        int res = 1;
        int cnt = 1;
        while (n > 1) {
            if (n % 2 == 1) {
                res = 2 * cnt - res;
            }
            cnt *= 2;
            n /= 2;
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumOneBitOperations(int n) {
        if (n == 0) return 0;
        int res = 1;
        int cnt = 1;
        while (n > 1) {
            if (n % 2 == 1) {
                res = 2 * cnt - res;
            }
            cnt *= 2;
            n /= 2;
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
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        res = 1
        cnt = 1
        while n > 1:
            if n % 2 == 1:
                res = 2 * cnt - res
            cnt *= 2
            n //= 2
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        res = 1
        cnt = 1
        while n > 1:
            if n % 2 == 1:
                res = 2 * cnt - res
            cnt *= 2
            n //= 2
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>

int minimumOneBitOperations(int n) {
    if (n == 0) return 0;
    int res = 1;
    int cnt = 1;
    while (n > 1) {
        if (n % 2 == 1) {
            res = 2 * cnt - res;
        }
        cnt *= 2;
        n /= 2;
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
    public int MinimumOneBitOperations(int n) {
        if (n == 0) return 0;
        int res = 1;
        int cnt = 1;
        while (n > 1) {
            if (n % 2 == 1) {
                res = 2 * cnt - res;
            }
            cnt *= 2;
            n /= 2;
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
var minimumOneBitOperations = function(n) {
    if (n == 0) return 0;
    let res = 1;
    let cnt = 1;
    while (n > 1) {
        if (n % 2 == 1) {
            res = 2 * cnt - res;
        }
        cnt *= 2;
        n = Math.floor(n / 2);
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumOneBitOperations(n: number): number {
    if (n == 0) return 0;
    let res: number = 1;
    let cnt: number = 1;
    while (n > 1) {
        if (n % 2 == 1) {
            res = 2 * cnt - res;
        }
        cnt *= 2;
        n = Math.floor(n / 2);
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minimumOneBitOperations($n) {
        if ($n == 0) return 0;
        $res = 1;
        $cnt = 1;
        while ($n > 1) {
            if ($n % 2 == 1) {
                $res = 2 * $cnt - $res;
            }
            $cnt *= 2;
            $n = floor($n / 2);
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
    func minimumOneBitOperations(_ n: Int) -> Int {
        if n == 0 {
            return 0
        }
        var res = 1
        var cnt = 1
        var n = n
        while n > 1 {
            if n % 2 == 1 {
                res = 2 * cnt - res
            }
            cnt *= 2
            n /= 2
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
    fun minimumOneBitOperations(n: Int): Int {
        if (n == 0) return 0
        var res = 1
        var cnt = 1
        var n = n
        while (n > 1) {
            if (n % 2 == 1) {
                res = 2 * cnt - res
            }
            cnt *= 2
            n /= 2
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
class Solution {
    int minimumOneBitOperations(int n) {
        if (n == 0) return 0;
        int res = 1;
        int cnt = 1;
        while (n > 1) {
            if (n % 2 == 1) {
                res = 2 * cnt - res;
            }
            cnt *= 2;
            n = n ~/ 2;
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
package main

import "fmt"

func minimumOneBitOperations(n int) int {
    if n == 0 {
        return 0
    }
    res := 1
    cnt := 1
    for n > 1 {
        if n%2 == 1 {
            res = 2*cnt - res
        }
        cnt *= 2
        n /= 2
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_one_bit_operations(n)
    if n == 0
        return 0
    end
    res = 1
    cnt = 1
    while n > 1
        if n % 2 == 1
            res = 2 * cnt - res
        end
        cnt *= 2
        n /= 2
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
    def minimumOneBitOperations(n: Int): Int = {
        if (n == 0) return 0
        var res = 1
        var cnt = 1
        var nVar = n
        while (nVar > 1) {
            if (nVar % 2 == 1) {
                res = 2 * cnt - res
            }
            cnt *= 2
            nVar /= 2
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
    pub fn minimum_one_bit_operations(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        let mut res = 1;
        let mut cnt = 1;
        let mut n = n;
        while n > 1 {
            if n % 2 == 1 {
                res = 2 * cnt - res;
            }
            cnt *= 2;
            n /= 2;
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
#lang racket
(define (minimum-one-bit-operations n)
  (if (= n 0)
      0
      (let loop ((res 1) (cnt 1) (n n))
        (if (> n 1)
            (if (= (remainder n 2) 1)
                (loop (- (* 2 cnt) res) (* 2 cnt) (quotient n 2))
                (loop res (* 2 cnt) (quotient n 2)))
            res))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([minimum_one_bit_operations/1]).

minimum_one_bit_operations(0) -> 0;
minimum_one_bit_operations(N) ->
    minimum_one_bit_operations(N, 1, 1).

minimum_one_bit_operations(N, Res, Cnt) when N > 1 ->
    case N rem 2 of
        1 -> minimum_one_bit_operations(N div 2, 2 * Cnt - Res, 2 * Cnt);
        0 -> minimum_one_bit_operations(N div 2, Res, 2 * Cnt)
    end;
minimum_one_bit_operations(_, Res, _) -> Res.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def minimum_one_bit_operations(0), do: 0
  def minimum_one_bit_operations(n) do
    minimum_one_bit_operations(n, 1, 1)
  end

  defp minimum_one_bit_operations(n, res, cnt) when n > 1 do
    case rem(n, 2) do
      1 -> minimum_one_bit_operations(div(n, 2), 2 * cnt - res, 2 * cnt)
      0 -> minimum_one_bit_operations(div(n, 2), res, 2 * cnt)
    end
  end

  defp minimum_one_bit_operations(_, res, _), do: res
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n) because we need to iterate over the bits of n, and the number of bits in n is proportional to log n.

- **Space Complexity:** O(1) because we only need a constant amount of space to store the result and the current bit being processed.

</div>
</details>
