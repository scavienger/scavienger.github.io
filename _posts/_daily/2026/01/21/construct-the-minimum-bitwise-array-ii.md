---
layout: post
title: "Construct the Minimum Bitwise Array II"
date: 2026-01-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Bit Manipulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/
ai_solutions:
  - solutions:
      python: "# Failed to parse response\n# Check logs for full output.\n# Full Response:\n\
        '''\n{\n  \"approach\": \"The core of this problem lies in understanding the\
        \ bitwise OR operation between an integer `x` and `x+1`. Let `N = nums[i]`.\
        \ We are looking for the smallest `x` such that `x OR (x+1) == N`. Analyzing\
        \ the binary representations of `x` and `x+1` reveals a crucial pattern. If\
        \ `x` is even, its least significant bit is 0. Then `x+1` will have its least\
        \ significant bit as 1, and all other bits identical to `x`. In this case, `x\
        \ OR (x+1) = x+1`. Thus, if `x` is even, `x+1 = N`, which means `x = N-1`. However,\
        \ if `N` is even, `N-1` is odd, contradicting our assumption that `x` is even.\
        \ The only even prime number is 2. For `N=2`, `x=1` (odd), so no even `x` works.\
        \ Therefore, if `N` is even, no solution exists, and `ans[i]` should be -1.\"\
        ,\n  \"time_complexity\": \"The time complexity is O(M * log(MAX_NUM)) where\
        \ M is the length of the `nums` array and MAX_NUM is the maximum value of `nums[i]`.\
        \ For each number in `nums`, we iterate up to 30-31 bits (for numbers up to\
        \ 10^9) to find the rightmost zero bit. This is a constant number of operations\
        \ per element.\",\n  \"space_complexity\": \"The space complexity is O(M) to\
        \ store the `ans` array, where M is the length of the `nums` array. No additional\
        \ significant space is used beyond the output array.\",\n  \"solutions\": {\n\
        \    \"cpp\": \"class Solution {\\npublic:\\n    std::vector<int> minBitwiseArray(std::vector<int>&\
        \ nums) {\\n        std::vector<int> ans;\\n        for (int N : nums) {\\n\
        \            if (N % 2 == 0) {\\n                ans.push_back(-1);\\n     \
        \           continue;\\n            }\\n\\n            // Find the rightmost\
        \ '0' bit in N. This is equivalent to finding the lowest bit that is '0'.\\\
        n            // If N is odd, its LSB is 1. So we need to find the rightmost\
        \ '0' bit in N-1.\\n            // Or, more generally, find the rightmost '0'\
        \ bit in N. If N has no '0' bits (i.e., N is all 1s, like 3, 7, 15, 31), then\
        \ N-1 is the answer.\\n            // If N is all 1s (e.g., 3, 7, 15), then\
        \ N-1 is also all 1s up to the highest bit, and 0 at the highest bit. This is\
        \ not correct.\\n            // Let's re-evaluate: x OR (x+1) = N.\\n      \
        \      // If N is odd, then x must be odd. (If x is even, x OR (x+1) = x+1,\
        \ which is odd. If x is odd, x OR (x+1) is odd).\\n            // If x is odd,\
        \ x = ...A01...1 (k ones). x+1 = ...A10...0 (k zeros).\\n            // x OR\
        \ (x+1) = ...A11...1 (k+1 ones).\\n            // This means N must be of the\
        \ form (prefix) followed by all ones.\\n            // To minimize x, we want\
        \ to make x as close to N as possible, but smaller.\\n            // N must\
        \ be of the form (prefix)11...1. If N is not of this form, no solution.\\n \
        \           // If N is of this form, then x should be (prefix)01...1.\\n   \
        \         // To get (prefix)01...1 from N, we need to find the rightmost '1'\
        \ bit in N that is NOT part of the trailing sequence of '1's.\\n           \
        \ // This is equivalent to finding the rightmost '0' bit in N, and flipping\
        \ it to '1', and all bits to its right to '0'.\\n            // No, this is\
        \ not correct. This is for x | (x-1).\\n\\n            // Let's use the property:\
        \ x | (x+1) = N.\\n            // This implies that N must have all bits set\
        \ that are set in x AND all bits set that are set in x+1.\\n            // Also,\
        \ x <= N and x+1 <= N. So x must be N or N-1 or smaller.\\n            // If\
        \ x = N, then N | (N+1) = N. This implies N+1 has no bits set that N doesn't\
        \ have. This is only true if N+1 is a submask of N, which is impossible for\
        \ positive integers.\\n            // So x < N.\\n\\n            // Consider\
        \ N in binary. If N has a '0' bit, say at position k (0-indexed from right).\\\
        n            // N = ...10... (k-th bit is 0)\\n            // If x has a '0'\
        \ at position k, then x | (x+1) will also have a '0' at position k (if x has\
        \ 0 at k, and x+1 has 0 at k, or x has 0 at k and x+1 has 1 at k, then x | (x+1)\
        \ has 1 at k).\\n            // The only way x | (x+1) can have a 0 at bit k\
        \ is if both x and x+1 have 0 at bit k.\\n            // This means x must be\
        \ of the form A01...1 and x+1 must be A10...0.\\n            // Then x | (x+1)\
        \ would be A11...1.\\n            // So, if N has a 0 bit, say at position `k`,\
        \ then `x` must have a `0` at bit `k` and `x+1` must have a `0` at bit `k`.\\\
        n            // This means that `x` must be `N` with some bits unset. Specifically,\
        \ `x` must be `N` with its lowest `1` bit flipped to `0`, and all bits to its\
        \ right flipped to `0`.\\n            // This is `x = N & (~(N & -N))`. This\
        \ is `N` XOR `(N & -N)`. This is `N` with its lowest set bit cleared.\\n   \
        \         // Let `x_candidate = N ^ (N & -N)`. This is `N` with its rightmost\
        \ set bit cleared.\\n            // Example: N=7 (111_2). N&-N = 1 (001_2).\
        \ N ^ (N&-N) = 6 (110_2). 6 | 7 = 7. This is not the minimum. Minimum is 3.\\\
        n            // Example: N=5 (101_2). N&-N = 1 (001_2). N ^ (N&-N) = 4 (100_2).\
        \ 4 | 5 = 5. This is correct.\\n            // Example: N=3 (011_2). N&-N =\
        \ 1 (001_2). N ^ (N&-N) = 2 (010_2). 2 | 3 = 3. This is not the minimum. Minimum\
        \ is 1.\\n\\n            // The hint says: \"Try unsetting a single bit from\
        \ nums[i]\".\\n            // Let's try `x = N - (1 << k)` for some k.\\n  \
        \          // The condition `x OR (x+1) == N` implies that `x` must be `N` with\
        \ some bits unset.\\n            // Specifically, if `x` is `...A01...1` (where\
        \ `0` is the rightmost zero bit of `x`, and there are `k` ones after it),\\\
        n            // then `x+1` is `...A10...0` (where `1` is at the position of\
        \ the original `0`, and there are `k` zeros after it).\\n            // Then\
        \ `x OR (x+1)` is `...A11...1` (all bits from the rightmost zero of `x` onwards\
        \ are `1`).\\n            // This means `N` must be of the form `(prefix)11...1`\
        \ where the `prefix` is `A`.\\n            // To find the smallest `x`, we want\
        \ `A` to be as large as possible, and `k` to be as small as possible.\\n   \
        \         // This means we want `x` to be `N` with its rightmost `1` bit (that\
        \ is part of the trailing sequence of `1`s) flipped to `0`.\\n            //\
        \ More precisely, `N` must be of the form `P11...1` where `P` is some prefix.\
        \ The `x` we are looking for is `P01...1`.\\n            // This means `x =\
        \ N - (1 << k)` where `k` is the position of the lowest `0` bit in `N`'s binary\
        \ representation.\\n            // If `N` is all ones (e.g., 3, 7, 15, 31),\
        \ then `N` has no `0` bit. In this case, `x = N-1` is the answer.\\n       \
        \     // For example, N=3 (011_2). No 0 bit. x = 3-1 = 2. But 2 | 3 = 3. This\
        \ is not the minimum. Minimum is 1.\\n            // For N=7 (111_2). No 0 bit.\
        \ x = 7-1 = 6. But 6 | 7 = 7. Not minimum. Minimum is 3.\\n\\n            //\
        \ Let's re-examine the property: `x | (x+1)`. The bits of `x` and `x+1` are\
        \ identical up to the most significant bit where they differ.\\n           \
        \ // Let `k` be the position of the rightmost `0` bit in `x`. Then `x` has the\
        \ form `...B10...0` (where `0` is at position `k`, and there are `m` ones after\
        \ it).\\n            // No, this is wrong. Let `x = A01...1` (where `0` is the\
        \ rightmost `0` bit, and there are `k` ones after it).\\n            // Then\
        \ `x+1 = A10...0` (where `1` is at the position of the original `0`, and there\
        \ are `k` zeros after it).\\n            // `x OR (x+1) = A11...1` (all bits\
        \ from position `k` downwards are `1`).\\n            // So, `N` must be of\
        \ the form `A11...1` for some `A` and some `k`.\\n            // To find the\
        \ minimum `x`, we need to find the largest `A` and smallest `k` such that `N\
        \ = A11...1`.\\n            // This means `N` must be equal to `(A << (k+1))\
        \ | ((1 << (k+1)) - 1)`.\\n            // The value `A` is `N >> (k+1)`. The\
        \ value `k` is the position of the rightmost `0` bit in `N`.\\n            //\
        \ If `N` is all\n'''"
      kotlin: "class Solution {\n    fun minBitwiseArray(nums: List<Int>): IntArray\
        \ {\n        val ans = IntArray(nums.size)\n        for (i in nums.indices)\
        \ {\n            val num = nums[i]\n            if (num % 2 == 0) {\n      \
        \          ans[i] = -1\n            } else {\n                var m = 0\n  \
        \              var temp = num\n                while (temp > 0 && (temp and\
        \ 1) == 1) {\n                    m++\n                    temp = temp shr 1\n\
        \                }\n                ans[i] = num xor (1 shl (m - 1))\n     \
        \       }\n        }\n        return ans\n    }\n}"
      dart: "class Solution {\n  List<int> minBitwiseArray(List<int> nums) {\n    final\
        \ List<int> ans = List<int>.filled(nums.length, 0);\n    for (int i = 0; i <\
        \ nums.length; i++) {\n      final int num = nums[i];\n      if (num % 2 ==\
        \ 0) {\n        ans[i] = -1;\n      } else {\n        int m = 0;\n        int\
        \ temp = num;\n        while (temp > 0 && (temp & 1) == 1) {\n          m++;\n\
        \          temp >>= 1;\n        }\n        ans[i] = num ^ (1 << (m - 1));\n\
        \      }\n    }\n    return ans;\n  }\n}"
      go: "func minBitwiseArray(nums []int) []int {\n    ans := make([]int, len(nums))\n\
        \    for i, num := range nums {\n        if num%2 == 0 {\n            ans[i]\
        \ = -1\n        } else {\n            m := 0\n            temp := num\n    \
        \        for temp > 0 && (temp&1) == 1 {\n                m++\n            \
        \    temp >>= 1\n            }\n            ans[i] = num ^ (1 << (m - 1))\n\
        \        }\n    }\n    return ans\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer[]}\ndef min_bitwise_array(nums)\n\
        \    ans = []\n    nums.each do |num|\n        if num % 2 == 0\n           \
        \ ans << -1\n        else\n            m = 0\n            temp = num\n     \
        \       while temp > 0 && (temp & 1) == 1\n                m += 1\n        \
        \        temp >>= 1\n            end\n            ans << (num ^ (1 << (m - 1)))\n\
        \        end\n    end\n    ans\nend"
      scala: "object Solution {\n    def minBitwiseArray(nums: List[Int]): Array[Int]\
        \ = {\n        val ans = Array.ofDim[Int](nums.length)\n        for (i <- nums.indices)\
        \ {\n            val num = nums(i)\n            if (num % 2 == 0) {\n      \
        \          ans(i) = -1\n            } else {\n                var m = 0\n  \
        \              var temp = num\n                while (temp > 0 && (temp & 1)\
        \ == 1) {\n                    m += 1\n                    temp = temp >>> 1\n\
        \                }\n                ans(i) = num ^ (1 << (m - 1))\n        \
        \    }\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        let mut ans = Vec::with_capacity(nums.len());\n        for num\
        \ in nums {\n            if num % 2 == 0 {\n                ans.push(-1);\n\
        \            } else {\n                let mut m = 0;\n                let mut\
        \ temp = num;\n                while temp > 0 && (temp & 1) == 1 {\n       \
        \             m += 1;\n                    temp >>= 1;\n                }\n\
        \                ans.push(num ^ (1 << (m - 1)));\n            }\n        }\n\
        \        ans\n    }\n}"
      racket: "(define/contract (min-bitwise-array nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (map (lambda (num)\n         (if (= (remainder\
        \ num 2) 0)\n             -1\n             (let loop ((m 0) (temp num))\n  \
        \             (if (and (> temp 0) (= (bitwise-and temp 1) 1))\n            \
        \       (loop (+ m 1) (arithmetic-shift temp -1))\n                   (bitwise-xor\
        \ num (arithmetic-shift 1 (- m 1)))))))\n       nums))"
      erlang: "-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].\nmin_bitwise_array(Nums)\
        \ ->\n  lists:map(fun(Num) ->\n    if\n      (Num rem 2) == 0 ->\n        -1;\n\
        \      true ->\n        M = count_trailing_ones(Num, 0, Num),\n        Num bxor\
        \ (1 bsl (M - 1))\n    end\n  end, Nums).\n\ncount_trailing_ones(Temp, M, _)\
        \ when Temp =< 0 -> M;\ncount_trailing_ones(Temp, M, _) when (Temp band 1) ==\
        \ 0 -> M;\ncount_trailing_ones(Temp, M, Num) ->\n  count_trailing_ones(Temp\
        \ bsr 1, M + 1, Num)."
      elixir: "defmodule Solution do\n  @spec min_bitwise_array(nums :: [integer]) ::\
        \ [integer]\n  def min_bitwise_array(nums) do\n    Enum.map(nums, fn num ->\n\
        \      if rem(num, 2) == 0 do\n        -1\n      else\n        m = count_trailing_ones(num,\
        \ 0)\n        Bitwise.bxor(num, Bitwise.bsl(1, m - 1))\n      end\n    end)\n\
        \  end\n\n  defp count_trailing_ones(temp, m) when temp <= 0, do: m\n  defp\
        \ count_trailing_ones(temp, m) when Bitwise.band(temp, 1) == 0, do: m\n  defp\
        \ count_trailing_ones(temp, m) do\n    count_trailing_ones(Bitwise.bsr(temp,\
        \ 1), m + 1)\n  end\nend"
    approach: 'The problem asks us to find the minimum `ans[i]` such that `ans[i] OR
      (ans[i] + 1) == nums[i]`. Let `x = ans[i]` and `N = nums[i]`. We analyze the bitwise
      OR operation `x OR (x + 1)`. If `x` has its rightmost zero bit at position `k`
      (0-indexed from the right), then `x` can be represented as `(prefix)0(k ones)`
      in binary. Consequently, `x + 1` will be `(prefix)1(k zeros)`. Performing the
      bitwise OR, `x OR (x + 1)` results in `(prefix)1(k ones)`. This implies that `N`
      must be of the form `(some_prefix)1(k ones)`, meaning `N` must have `k+1` trailing
      ones. If `N` does not fit this pattern (e.g., if `N` is even, it has zero trailing
      ones), then no such `x` exists.


      Based on this observation, for a given `N`, we first check if `N` is even. If
      it is, `ans[i]` is `-1`. Since `nums[i]` are prime, this only happens for `N=2`.
      If `N` is odd, we count `m`, the number of trailing ones in `N`. From the pattern
      `(prefix)1(k ones)`, we deduce that `k+1 = m`, so `k = m-1`. The desired `x` is
      then `N` with its `k`-th bit unset. This can be achieved by `x = N XOR (1 << k)`.
      This construction yields the unique `x` that satisfies the structural properties,
      and thus it is the minimal one. We apply this logic for each number in the input
      array `nums` to construct the `ans` array.'
    time_complexity: The time complexity is O(L * log(max_val)), where L is the length
      of the `nums` array and `max_val` is the maximum value in `nums`. For each number,
      we iterate through its bits to count the trailing ones, which takes at most `log(max_val)`
      operations (approximately 30-31 for 10^9).
    space_complexity: The space complexity is O(L), where L is the length of the `nums`
      array. This is due to storing the `ans` array, which has the same length as the
      input array.
    elapsed_time: 328.89649987220764
    model: gemini-2.5-flash
    generated_at: '2026-01-21 18:37:04 '
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> minBitwiseArray(vector<int>&\
        \ nums) {\n        vector<int> ans;\n        for (int num : nums) {\n      \
        \      if (num % 2 == 0) ans.push_back(-1);\n            else {\n          \
        \      int x = num;\n                while ((x | (x + 1)) != num) x--;\n   \
        \             ans.push_back(x);\n            }\n        }\n        return ans;\n\
        \    }\n};"
      java: "class Solution {\n    public int[] minBitwiseArray(List<Integer> nums)\
        \ {\n        int[] ans = new int[nums.size()];\n        for (int i = 0; i <\
        \ nums.size(); i++) {\n            int num = nums.get(i);\n            if (num\
        \ % 2 == 0) ans[i] = -1;\n            else {\n                int x = num;\n\
        \                while ((x | (x + 1)) != num) x--;\n                ans[i] =\
        \ x;\n            }\n        }\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def minBitwiseArray(self, nums):\n     \
        \   ans = []\n        for num in nums:\n            if num % 2 == 0: ans.append(-1)\n\
        \            else:\n                x = num\n                while (x | (x +\
        \ 1)) != num: x -= 1\n                ans.append(x)\n        return ans"
      python3: "class Solution:\n    def minBitwiseArray(self, nums: list[int]) -> list[int]:\n\
        \        ans = []\n        for num in nums:\n            if num % 2 == 0: ans.append(-1)\n\
        \            else:\n                x = num\n                while (x | (x +\
        \ 1)) != num: x -= 1\n                ans.append(x)\n        return ans"
      c: "int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {\n    int*\
        \ ans = (int*)malloc(numsSize * sizeof(int));\n    *returnSize = numsSize;\n\
        \    for (int i = 0; i < numsSize; i++) {\n        int num = nums[i];\n    \
        \    if (num % 2 == 0) ans[i] = -1;\n        else {\n            int x = num;\n\
        \            while ((x | (x + 1)) != num) x--;\n            ans[i] = x;\n  \
        \      }\n    }\n    return ans;\n}"
      csharp: "public class Solution {\n    public int[] MinBitwiseArray(IList<int>\
        \ nums) {\n        int[] ans = new int[nums.Count];\n        for (int i = 0;\
        \ i < nums.Count; i++) {\n            int num = nums[i];\n            if (num\
        \ % 2 == 0) ans[i] = -1;\n            else {\n                int x = num;\n\
        \                while ((x | (x + 1)) != num) x--;\n                ans[i] =\
        \ x;\n            }\n        }\n        return ans;\n    }\n}"
      javascript: "var minBitwiseArray = function(nums) {\n    let ans = [];\n    for\
        \ (let num of nums) {\n        if (num % 2 == 0) ans.push(-1);\n        else\
        \ {\n            let x = num;\n            while ((x | (x + 1)) != num) x--;\n\
        \            ans.push(x);\n        }\n    }\n    return ans;\n};"
      typescript: "function minBitwiseArray(nums: number[]): number[] {\n    let ans:\
        \ number[] = [];\n    for (let num of nums) {\n        if (num % 2 == 0) ans.push(-1);\n\
        \        else {\n            let x = num;\n            while ((x | (x + 1))\
        \ != num) x--;\n            ans.push(x);\n        }\n    }\n    return ans;\n\
        }"
      php: "class Solution {\n    function minBitwiseArray($nums) {\n        $ans =\
        \ [];\n        foreach ($nums as $num) {\n            if ($num % 2 == 0) $ans[]\
        \ = -1;\n            else {\n                $x = $num;\n                while\
        \ (($x | ($x + 1)) != $num) $x--;\n                $ans[] = $x;\n          \
        \  }\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func minBitwiseArray(_ nums: [Int]) -> [Int] {\n\
        \        var ans: [Int] = []\n        for num in nums {\n            if num\
        \ % 2 == 0 { ans.append(-1) }\n            else {\n                var x = num\n\
        \                while (x | (x + 1)) != num { x -= 1 }\n                ans.append(x)\n\
        \            }\n        }\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun minBitwiseArray(nums: List<Int>): IntArray\
        \ {\n        val result = IntArray(nums.size)\n        for (i in nums.indices)\
        \ {\n            if (nums[i] % 2 == 0) {\n                result[i] = -1\n \
        \           } else {\n                var j = nums[i]\n                while\
        \ ((j or (j + 1)) != nums[i]) {\n                    j--\n                }\n\
        \                result[i] = j\n            }\n        }\n        return result\n\
        \    }\n}"
      dart: "class Solution {\n  List<int> minBitwiseArray(List<int> nums) {\n    List<int>\
        \ result = List<int>.filled(nums.length, 0);\n    for (int i = 0; i < nums.length;\
        \ i++) {\n      if (nums[i] % 2 == 0) {\n        result[i] = -1;\n      } else\
        \ {\n        int j = nums[i];\n        while ((j | (j + 1)) != nums[i]) {\n\
        \          j--;\n        }\n        result[i] = j;\n      }\n    }\n    return\
        \ result;\n  }\n}"
      go: "func minBitwiseArray(nums []int) []int {\n    result := make([]int, len(nums))\n\
        \    for i, num := range nums {\n        if num%2 == 0 {\n            result[i]\
        \ = -1\n        } else {\n            j := num\n            for (j | (j + 1))\
        \ != num {\n                j--\n            }\n            result[i] = j\n\
        \        }\n    }\n    return result\n}"
      ruby: "def min_bitwise_array(nums)\n    result = Array.new(nums.size)\n    nums.each_with_index\
        \ do |num, i|\n        if num % 2 == 0\n            result[i] = -1\n       \
        \ else\n            j = num\n            j -= 1 while (j | (j + 1)) != num\n\
        \            result[i] = j\n        end\n    end\n    result\nend"
      scala: "object Solution {\n    def minBitwiseArray(nums: List[Int]): Array[Int]\
        \ = {\n        val result = Array.ofDim[Int](nums.size)\n        for (i <- nums.indices)\
        \ {\n            if (nums(i) % 2 == 0) {\n                result(i) = -1\n \
        \           } else {\n                var j = nums(i)\n                while\
        \ ((j | (j + 1)) != nums(i)) {\n                    j -= 1\n               \
        \ }\n                result(i) = j\n            }\n        }\n        result\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        let mut result = vec![0; nums.len()];\n        for (i, &num) in\
        \ nums.iter().enumerate() {\n            if num % 2 == 0 {\n               \
        \ result[i] = -1;\n            } else {\n                let mut j = num;\n\
        \                while (j | (j + 1)) != num {\n                    j -= 1;\n\
        \                }\n                result[i] = j;\n            }\n        }\n\
        \        result\n    }\n}"
      racket: "(define/contract (min-bitwise-array nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (let loop ([nums nums] [result '()])\n    (if\
        \ (null? nums)\n        (reverse result)\n        (let ([num (car nums)])\n\
        \          (if (even? num)\n              (loop (cdr nums) (cons -1 result))\n\
        \              (let loop2 ([j num])\n                (if (= (bitwise-ior j (add1\
        \ j)) num)\n                    (loop (cdr nums) (cons j result))\n        \
        \            (loop2 (sub1 j)))))))))"
      erlang: "-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].\nmin_bitwise_array(Nums)\
        \ ->\n    lists:map(fun(N) ->\n        case N rem 2 of\n            0 -> -1;\n\
        \            _ ->\n                J = N,\n                while (bor(J, J +\
        \ 1) =/= N) ->\n                    J - 1;\n                J\n        end\n\
        \    end, Nums)."
      elixir: "defmodule Solution do\n  @spec min_bitwise_array(nums :: [integer]) ::\
        \ [integer]\n  def min_bitwise_array(nums) do\n    Enum.map(nums, fn num ->\n\
        \      if rem(num, 2) == 0 do\n        -1\n      else\n        j = num\n   \
        \     while bor(j, j + 1) != num do\n          j = j - 1\n        end\n    \
        \    j\n      end\n    end)\n  end\nend"
    approach: The problem requires constructing an array where each element's bitwise
      OR with its next element equals a given prime number. The key intuition is to
      analyze the binary representation of the prime numbers. For a number to satisfy
      the condition, it must have a specific bit set to 1, such that when it is ORed
      with the next number (which is essentially the current number plus 1), it results
      in the given prime number. This can be achieved by unsetting a single bit from
      the prime number, which will give us the required number. If the prime number
      is even, it is impossible to find such a number, so we set the answer to -1.
    time_complexity: The time complexity of this solution is O(n), where n is the number
      of elements in the input array. This is because we are iterating over each element
      in the array once and performing a constant amount of work for each element.
    space_complexity: The space complexity of this solution is O(n), where n is the
      number of elements in the input array. This is because we are creating a new array
      of the same size as the input array to store the results.
    elapsed_time: 6.779659986495972
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-21 18:37:16 '
---

## Problem #3315: Construct the Minimum Bitwise Array II

**Difficulty:** Medium

**Topics:** Array, Bit Manipulation

## Problem Description

<p>You are given an array <code>nums</code> consisting of <code>n</code> <span data-keyword="prime-number">prime</span> integers.</p>

<p>You need to construct an array <code>ans</code> of length <code>n</code>, such that, for each index <code>i</code>, the bitwise <code>OR</code> of <code>ans[i]</code> and <code>ans[i] + 1</code> is equal to <code>nums[i]</code>, i.e. <code>ans[i] OR (ans[i] + 1) == nums[i]</code>.</p>

<p>Additionally, you must <strong>minimize</strong> each value of <code>ans[i]</code> in the resulting array.</p>

<p>If it is <em>not possible</em> to find such a value for <code>ans[i]</code> that satisfies the <strong>condition</strong>, then set <code>ans[i] = -1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,5,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,1,4,3]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>i = 0</code>, as there is no value for <code>ans[0]</code> that satisfies <code>ans[0] OR (ans[0] + 1) = 2</code>, so <code>ans[0] = -1</code>.</li>
	<li>For <code>i = 1</code>, the smallest <code>ans[1]</code> that satisfies <code>ans[1] OR (ans[1] + 1) = 3</code> is <code>1</code>, because <code>1 OR (1 + 1) = 3</code>.</li>
	<li>For <code>i = 2</code>, the smallest <code>ans[2]</code> that satisfies <code>ans[2] OR (ans[2] + 1) = 5</code> is <code>4</code>, because <code>4 OR (4 + 1) = 5</code>.</li>
	<li>For <code>i = 3</code>, the smallest <code>ans[3]</code> that satisfies <code>ans[3] OR (ans[3] + 1) = 7</code> is <code>3</code>, because <code>3 OR (3 + 1) = 7</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [11,13,31]</span></p>

<p><strong>Output:</strong> <span class="example-io">[9,12,15]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>i = 0</code>, the smallest <code>ans[0]</code> that satisfies <code>ans[0] OR (ans[0] + 1) = 11</code> is <code>9</code>, because <code>9 OR (9 + 1) = 11</code>.</li>
	<li>For <code>i = 1</code>, the smallest <code>ans[1]</code> that satisfies <code>ans[1] OR (ans[1] + 1) = 13</code> is <code>12</code>, because <code>12 OR (12 + 1) = 13</code>.</li>
	<li>For <code>i = 2</code>, the smallest <code>ans[2]</code> that satisfies <code>ans[2] OR (ans[2] + 1) = 31</code> is <code>15</code>, because <code>15 OR (15 + 1) = 31</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>2 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums[i]</code> is a prime number.</li>
</ul>


## Hints

1. Consider the binary representation of `nums[i]`.

2. Answer is -1 for even `nums[i]`.

3. Try unsetting a single bit from `nums[i]`.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-21 18:37:04 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the minimum `ans[i]` such that `ans[i] OR (ans[i] + 1) == nums[i]`. Let `x = ans[i]` and `N = nums[i]`. We analyze the bitwise OR operation `x OR (x + 1)`. If `x` has its rightmost zero bit at position `k` (0-indexed from the right), then `x` can be represented as `(prefix)0(k ones)` in binary. Consequently, `x + 1` will be `(prefix)1(k zeros)`. Performing the bitwise OR, `x OR (x + 1)` results in `(prefix)1(k ones)`. This implies that `N` must be of the form `(some_prefix)1(k ones)`, meaning `N` must have `k+1` trailing ones. If `N` does not fit this pattern (e.g., if `N` is even, it has zero trailing ones), then no such `x` exists.

Based on this observation, for a given `N`, we first check if `N` is even. If it is, `ans[i]` is `-1`. Since `nums[i]` are prime, this only happens for `N=2`. If `N` is odd, we count `m`, the number of trailing ones in `N`. From the pattern `(prefix)1(k ones)`, we deduce that `k+1 = m`, so `k = m-1`. The desired `x` is then `N` with its `k`-th bit unset. This can be achieved by `x = N XOR (1 << k)`. This construction yields the unique `x` that satisfies the structural properties, and thus it is the minimal one. We apply this logic for each number in the input array `nums` to construct the `ans` array.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash" checked>
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
    <label for="lang-python-gemini-2-5-flash">Python</label>
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

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Failed to parse response
# Check logs for full output.
# Full Response:
'''
{
  "approach": "The core of this problem lies in understanding the bitwise OR operation between an integer `x` and `x+1`. Let `N = nums[i]`. We are looking for the smallest `x` such that `x OR (x+1) == N`. Analyzing the binary representations of `x` and `x+1` reveals a crucial pattern. If `x` is even, its least significant bit is 0. Then `x+1` will have its least significant bit as 1, and all other bits identical to `x`. In this case, `x OR (x+1) = x+1`. Thus, if `x` is even, `x+1 = N`, which means `x = N-1`. However, if `N` is even, `N-1` is odd, contradicting our assumption that `x` is even. The only even prime number is 2. For `N=2`, `x=1` (odd), so no even `x` works. Therefore, if `N` is even, no solution exists, and `ans[i]` should be -1.",
  "time_complexity": "The time complexity is O(M * log(MAX_NUM)) where M is the length of the `nums` array and MAX_NUM is the maximum value of `nums[i]`. For each number in `nums`, we iterate up to 30-31 bits (for numbers up to 10^9) to find the rightmost zero bit. This is a constant number of operations per element.",
  "space_complexity": "The space complexity is O(M) to store the `ans` array, where M is the length of the `nums` array. No additional significant space is used beyond the output array.",
  "solutions": {
    "cpp": "class Solution {\npublic:\n    std::vector<int> minBitwiseArray(std::vector<int>& nums) {\n        std::vector<int> ans;\n        for (int N : nums) {\n            if (N % 2 == 0) {\n                ans.push_back(-1);\n                continue;\n            }\n\n            // Find the rightmost '0' bit in N. This is equivalent to finding the lowest bit that is '0'.\n            // If N is odd, its LSB is 1. So we need to find the rightmost '0' bit in N-1.\n            // Or, more generally, find the rightmost '0' bit in N. If N has no '0' bits (i.e., N is all 1s, like 3, 7, 15, 31), then N-1 is the answer.\n            // If N is all 1s (e.g., 3, 7, 15), then N-1 is also all 1s up to the highest bit, and 0 at the highest bit. This is not correct.\n            // Let's re-evaluate: x OR (x+1) = N.\n            // If N is odd, then x must be odd. (If x is even, x OR (x+1) = x+1, which is odd. If x is odd, x OR (x+1) is odd).\n            // If x is odd, x = ...A01...1 (k ones). x+1 = ...A10...0 (k zeros).\n            // x OR (x+1) = ...A11...1 (k+1 ones).\n            // This means N must be of the form (prefix) followed by all ones.\n            // To minimize x, we want to make x as close to N as possible, but smaller.\n            // N must be of the form (prefix)11...1. If N is not of this form, no solution.\n            // If N is of this form, then x should be (prefix)01...1.\n            // To get (prefix)01...1 from N, we need to find the rightmost '1' bit in N that is NOT part of the trailing sequence of '1's.\n            // This is equivalent to finding the rightmost '0' bit in N, and flipping it to '1', and all bits to its right to '0'.\n            // No, this is not correct. This is for x | (x-1).\n\n            // Let's use the property: x | (x+1) = N.\n            // This implies that N must have all bits set that are set in x AND all bits set that are set in x+1.\n            // Also, x <= N and x+1 <= N. So x must be N or N-1 or smaller.\n            // If x = N, then N | (N+1) = N. This implies N+1 has no bits set that N doesn't have. This is only true if N+1 is a submask of N, which is impossible for positive integers.\n            // So x < N.\n\n            // Consider N in binary. If N has a '0' bit, say at position k (0-indexed from right).\n            // N = ...10... (k-th bit is 0)\n            // If x has a '0' at position k, then x | (x+1) will also have a '0' at position k (if x has 0 at k, and x+1 has 0 at k, or x has 0 at k and x+1 has 1 at k, then x | (x+1) has 1 at k).\n            // The only way x | (x+1) can have a 0 at bit k is if both x and x+1 have 0 at bit k.\n            // This means x must be of the form A01...1 and x+1 must be A10...0.\n            // Then x | (x+1) would be A11...1.\n            // So, if N has a 0 bit, say at position `k`, then `x` must have a `0` at bit `k` and `x+1` must have a `0` at bit `k`.\n            // This means that `x` must be `N` with some bits unset. Specifically, `x` must be `N` with its lowest `1` bit flipped to `0`, and all bits to its right flipped to `0`.\n            // This is `x = N & (~(N & -N))`. This is `N` XOR `(N & -N)`. This is `N` with its lowest set bit cleared.\n            // Let `x_candidate = N ^ (N & -N)`. This is `N` with its rightmost set bit cleared.\n            // Example: N=7 (111_2). N&-N = 1 (001_2). N ^ (N&-N) = 6 (110_2). 6 | 7 = 7. This is not the minimum. Minimum is 3.\n            // Example: N=5 (101_2). N&-N = 1 (001_2). N ^ (N&-N) = 4 (100_2). 4 | 5 = 5. This is correct.\n            // Example: N=3 (011_2). N&-N = 1 (001_2). N ^ (N&-N) = 2 (010_2). 2 | 3 = 3. This is not the minimum. Minimum is 1.\n\n            // The hint says: "Try unsetting a single bit from nums[i]".\n            // Let's try `x = N - (1 << k)` for some k.\n            // The condition `x OR (x+1) == N` implies that `x` must be `N` with some bits unset.\n            // Specifically, if `x` is `...A01...1` (where `0` is the rightmost zero bit of `x`, and there are `k` ones after it),\n            // then `x+1` is `...A10...0` (where `1` is at the position of the original `0`, and there are `k` zeros after it).\n            // Then `x OR (x+1)` is `...A11...1` (all bits from the rightmost zero of `x` onwards are `1`).\n            // This means `N` must be of the form `(prefix)11...1` where the `prefix` is `A`.\n            // To find the smallest `x`, we want `A` to be as large as possible, and `k` to be as small as possible.\n            // This means we want `x` to be `N` with its rightmost `1` bit (that is part of the trailing sequence of `1`s) flipped to `0`.\n            // More precisely, `N` must be of the form `P11...1` where `P` is some prefix. The `x` we are looking for is `P01...1`.\n            // This means `x = N - (1 << k)` where `k` is the position of the lowest `0` bit in `N`'s binary representation.\n            // If `N` is all ones (e.g., 3, 7, 15, 31), then `N` has no `0` bit. In this case, `x = N-1` is the answer.\n            // For example, N=3 (011_2). No 0 bit. x = 3-1 = 2. But 2 | 3 = 3. This is not the minimum. Minimum is 1.\n            // For N=7 (111_2). No 0 bit. x = 7-1 = 6. But 6 | 7 = 7. Not minimum. Minimum is 3.\n\n            // Let's re-examine the property: `x | (x+1)`. The bits of `x` and `x+1` are identical up to the most significant bit where they differ.\n            // Let `k` be the position of the rightmost `0` bit in `x`. Then `x` has the form `...B10...0` (where `0` is at position `k`, and there are `m` ones after it).\n            // No, this is wrong. Let `x = A01...1` (where `0` is the rightmost `0` bit, and there are `k` ones after it).\n            // Then `x+1 = A10...0` (where `1` is at the position of the original `0`, and there are `k` zeros after it).\n            // `x OR (x+1) = A11...1` (all bits from position `k` downwards are `1`).\n            // So, `N` must be of the form `A11...1` for some `A` and some `k`.\n            // To find the minimum `x`, we need to find the largest `A` and smallest `k` such that `N = A11...1`.\n            // This means `N` must be equal to `(A << (k+1)) | ((1 << (k+1)) - 1)`.\n            // The value `A` is `N >> (k+1)`. The value `k` is the position of the rightmost `0` bit in `N`.\n            // If `N` is all
'''
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minBitwiseArray(nums: List<Int>): IntArray {
        val ans = IntArray(nums.size)
        for (i in nums.indices) {
            val num = nums[i]
            if (num % 2 == 0) {
                ans[i] = -1
            } else {
                var m = 0
                var temp = num
                while (temp > 0 && (temp and 1) == 1) {
                    m++
                    temp = temp shr 1
                }
                ans[i] = num xor (1 shl (m - 1))
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
class Solution {
  List<int> minBitwiseArray(List<int> nums) {
    final List<int> ans = List<int>.filled(nums.length, 0);
    for (int i = 0; i < nums.length; i++) {
      final int num = nums[i];
      if (num % 2 == 0) {
        ans[i] = -1;
      } else {
        int m = 0;
        int temp = num;
        while (temp > 0 && (temp & 1) == 1) {
          m++;
          temp >>= 1;
        }
        ans[i] = num ^ (1 << (m - 1));
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
func minBitwiseArray(nums []int) []int {
    ans := make([]int, len(nums))
    for i, num := range nums {
        if num%2 == 0 {
            ans[i] = -1
        } else {
            m := 0
            temp := num
            for temp > 0 && (temp&1) == 1 {
                m++
                temp >>= 1
            }
            ans[i] = num ^ (1 << (m - 1))
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
# @param {Integer[]} nums
# @return {Integer[]}
def min_bitwise_array(nums)
    ans = []
    nums.each do |num|
        if num % 2 == 0
            ans << -1
        else
            m = 0
            temp = num
            while temp > 0 && (temp & 1) == 1
                m += 1
                temp >>= 1
            end
            ans << (num ^ (1 << (m - 1)))
        end
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
    def minBitwiseArray(nums: List[Int]): Array[Int] = {
        val ans = Array.ofDim[Int](nums.length)
        for (i <- nums.indices) {
            val num = nums(i)
            if (num % 2 == 0) {
                ans(i) = -1
            } else {
                var m = 0
                var temp = num
                while (temp > 0 && (temp & 1) == 1) {
                    m += 1
                    temp = temp >>> 1
                }
                ans(i) = num ^ (1 << (m - 1))
            }
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
    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = Vec::with_capacity(nums.len());
        for num in nums {
            if num % 2 == 0 {
                ans.push(-1);
            } else {
                let mut m = 0;
                let mut temp = num;
                while temp > 0 && (temp & 1) == 1 {
                    m += 1;
                    temp >>= 1;
                }
                ans.push(num ^ (1 << (m - 1)));
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
(define/contract (min-bitwise-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (map (lambda (num)
         (if (= (remainder num 2) 0)
             -1
             (let loop ((m 0) (temp num))
               (if (and (> temp 0) (= (bitwise-and temp 1) 1))
                   (loop (+ m 1) (arithmetic-shift temp -1))
                   (bitwise-xor num (arithmetic-shift 1 (- m 1)))))))
       nums))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].
min_bitwise_array(Nums) ->
  lists:map(fun(Num) ->
    if
      (Num rem 2) == 0 ->
        -1;
      true ->
        M = count_trailing_ones(Num, 0, Num),
        Num bxor (1 bsl (M - 1))
    end
  end, Nums).

count_trailing_ones(Temp, M, _) when Temp =< 0 -> M;
count_trailing_ones(Temp, M, _) when (Temp band 1) == 0 -> M;
count_trailing_ones(Temp, M, Num) ->
  count_trailing_ones(Temp bsr 1, M + 1, Num).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn num ->
      if rem(num, 2) == 0 do
        -1
      else
        m = count_trailing_ones(num, 0)
        Bitwise.bxor(num, Bitwise.bsl(1, m - 1))
      end
    end)
  end

  defp count_trailing_ones(temp, m) when temp <= 0, do: m
  defp count_trailing_ones(temp, m) when Bitwise.band(temp, 1) == 0, do: m
  defp count_trailing_ones(temp, m) do
    count_trailing_ones(Bitwise.bsr(temp, 1), m + 1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(L * log(max_val)), where L is the length of the `nums` array and `max_val` is the maximum value in `nums`. For each number, we iterate through its bits to count the trailing ones, which takes at most `log(max_val)` operations (approximately 30-31 for 10^9).

- **Space Complexity:** The space complexity is O(L), where L is the length of the `nums` array. This is due to storing the `ans` array, which has the same length as the input array.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-21 18:37:16 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires constructing an array where each element's bitwise OR with its next element equals a given prime number. The key intuition is to analyze the binary representation of the prime numbers. For a number to satisfy the condition, it must have a specific bit set to 1, such that when it is ORed with the next number (which is essentially the current number plus 1), it results in the given prime number. This can be achieved by unsetting a single bit from the prime number, which will give us the required number. If the prime number is even, it is impossible to find such a number, so we set the answer to -1.

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
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;
        for (int num : nums) {
            if (num % 2 == 0) ans.push_back(-1);
            else {
                int x = num;
                while ((x | (x + 1)) != num) x--;
                ans.push_back(x);
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
class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int[] ans = new int[nums.size()];
        for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            if (num % 2 == 0) ans[i] = -1;
            else {
                int x = num;
                while ((x | (x + 1)) != num) x--;
                ans[i] = x;
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
class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        for num in nums:
            if num % 2 == 0: ans.append(-1)
            else:
                x = num
                while (x | (x + 1)) != num: x -= 1
                ans.append(x)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for num in nums:
            if num % 2 == 0: ans.append(-1)
            else:
                x = num
                while (x | (x + 1)) != num: x -= 1
                ans.append(x)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        if (num % 2 == 0) ans[i] = -1;
        else {
            int x = num;
            while ((x | (x + 1)) != num) x--;
            ans[i] = x;
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
public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        int[] ans = new int[nums.Count];
        for (int i = 0; i < nums.Count; i++) {
            int num = nums[i];
            if (num % 2 == 0) ans[i] = -1;
            else {
                int x = num;
                while ((x | (x + 1)) != num) x--;
                ans[i] = x;
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
var minBitwiseArray = function(nums) {
    let ans = [];
    for (let num of nums) {
        if (num % 2 == 0) ans.push(-1);
        else {
            let x = num;
            while ((x | (x + 1)) != num) x--;
            ans.push(x);
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
function minBitwiseArray(nums: number[]): number[] {
    let ans: number[] = [];
    for (let num of nums) {
        if (num % 2 == 0) ans.push(-1);
        else {
            let x = num;
            while ((x | (x + 1)) != num) x--;
            ans.push(x);
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
class Solution {
    function minBitwiseArray($nums) {
        $ans = [];
        foreach ($nums as $num) {
            if ($num % 2 == 0) $ans[] = -1;
            else {
                $x = $num;
                while (($x | ($x + 1)) != $num) $x--;
                $ans[] = $x;
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
    func minBitwiseArray(_ nums: [Int]) -> [Int] {
        var ans: [Int] = []
        for num in nums {
            if num % 2 == 0 { ans.append(-1) }
            else {
                var x = num
                while (x | (x + 1)) != num { x -= 1 }
                ans.append(x)
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
    fun minBitwiseArray(nums: List<Int>): IntArray {
        val result = IntArray(nums.size)
        for (i in nums.indices) {
            if (nums[i] % 2 == 0) {
                result[i] = -1
            } else {
                var j = nums[i]
                while ((j or (j + 1)) != nums[i]) {
                    j--
                }
                result[i] = j
            }
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
  List<int> minBitwiseArray(List<int> nums) {
    List<int> result = List<int>.filled(nums.length, 0);
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] % 2 == 0) {
        result[i] = -1;
      } else {
        int j = nums[i];
        while ((j | (j + 1)) != nums[i]) {
          j--;
        }
        result[i] = j;
      }
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
func minBitwiseArray(nums []int) []int {
    result := make([]int, len(nums))
    for i, num := range nums {
        if num%2 == 0 {
            result[i] = -1
        } else {
            j := num
            for (j | (j + 1)) != num {
                j--
            }
            result[i] = j
        }
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_bitwise_array(nums)
    result = Array.new(nums.size)
    nums.each_with_index do |num, i|
        if num % 2 == 0
            result[i] = -1
        else
            j = num
            j -= 1 while (j | (j + 1)) != num
            result[i] = j
        end
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
    def minBitwiseArray(nums: List[Int]): Array[Int] = {
        val result = Array.ofDim[Int](nums.size)
        for (i <- nums.indices) {
            if (nums(i) % 2 == 0) {
                result(i) = -1
            } else {
                var j = nums(i)
                while ((j | (j + 1)) != nums(i)) {
                    j -= 1
                }
                result(i) = j
            }
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
    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        let mut result = vec![0; nums.len()];
        for (i, &num) in nums.iter().enumerate() {
            if num % 2 == 0 {
                result[i] = -1;
            } else {
                let mut j = num;
                while (j | (j + 1)) != num {
                    j -= 1;
                }
                result[i] = j;
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-bitwise-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ([nums nums] [result '()])
    (if (null? nums)
        (reverse result)
        (let ([num (car nums)])
          (if (even? num)
              (loop (cdr nums) (cons -1 result))
              (let loop2 ([j num])
                (if (= (bitwise-ior j (add1 j)) num)
                    (loop (cdr nums) (cons j result))
                    (loop2 (sub1 j)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].
min_bitwise_array(Nums) ->
    lists:map(fun(N) ->
        case N rem 2 of
            0 -> -1;
            _ ->
                J = N,
                while (bor(J, J + 1) =/= N) ->
                    J - 1;
                J
        end
    end, Nums).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn num ->
      if rem(num, 2) == 0 do
        -1
      else
        j = num
        while bor(j, j + 1) != num do
          j = j - 1
        end
        j
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n), where n is the number of elements in the input array. This is because we are iterating over each element in the array once and performing a constant amount of work for each element.

- **Space Complexity:** The space complexity of this solution is O(n), where n is the number of elements in the input array. This is because we are creating a new array of the same size as the input array to store the results.

</div>
</details>
