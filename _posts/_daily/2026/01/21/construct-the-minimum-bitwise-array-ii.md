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
      cpp: "class Solution {\npublic:\n    std::vector<int> minBitwiseArray(std::vector<int>&\
        \ nums) {\n        std::vector<int> ans;\n        ans.reserve(nums.size());\n\
        \n        for (int N : nums) {\n            int current_ans = -1;\n        \
        \    // Iterate k from 29 down to 0.\n            // N <= 10^9, which is less\
        \ than 2^30. So max bit position is 29.\n            for (int k = 29; k >= 0;\
        \ --k) {\n                // Condition 1: k-th bit of N must be 1\n        \
        \        bool k_th_bit_is_set = ((N >> k) & 1) == 1;\n\n                // Condition\
        \ 2: All bits from 0 to k-1 of N must be 1\n                // (1 << k) - 1\
        \ creates a mask with k trailing ones (e.g., for k=3, mask is 0111_2 = 7)\n\
        \                // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.\n\
        \                int mask_k_minus_1 = (1 << k) - 1;\n                bool lower_bits_are_all_set\
        \ = (N & mask_k_minus_1) == mask_k_minus_1;\n\n                if (k_th_bit_is_set\
        \ && lower_bits_are_all_set) {\n                    current_ans = N - (1 <<\
        \ k);\n                    break; // Found the largest k, which gives the smallest\
        \ ans[i]\n                }\n            }\n            ans.push_back(current_ans);\n\
        \        }\n\n        return ans;\n    }\n};"
      java: "import java.util.List;\nimport java.util.ArrayList;\n\nclass Solution {\n\
        \    public int[] minBitwiseArray(List<Integer> nums) {\n        int[] ans =\
        \ new int[nums.size()];\n\n        for (int i = 0; i < nums.size(); ++i) {\n\
        \            int N = nums.get(i);\n            int current_ans = -1;\n\n   \
        \         // Iterate k from 29 down to 0.\n            // N <= 10^9, which is\
        \ less than 2^30. So max bit position is 29.\n            for (int k = 29; k\
        \ >= 0; --k) {\n                // Condition 1: k-th bit of N must be 1\n  \
        \              boolean k_th_bit_is_set = ((N >> k) & 1) == 1;\n\n          \
        \      // Condition 2: All bits from 0 to k-1 of N must be 1\n             \
        \   // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask\
        \ is 0111_2 = 7)\n                // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0\
        \ is always true.\n                int mask_k_minus_1 = (1 << k) - 1;\n    \
        \            boolean lower_bits_are_all_set = (N & mask_k_minus_1) == mask_k_minus_1;\n\
        \n                if (k_th_bit_is_set && lower_bits_are_all_set) {\n       \
        \             current_ans = N - (1 << k);\n                    break; // Found\
        \ the largest k, which gives the smallest ans[i]\n                }\n      \
        \      }\n            ans[i] = current_ans;\n        }\n\n        return ans;\n\
        \    }\n}"
      python: "# Failed to parse response\n# Check logs for full output.\n# Full Response:\n\
        '''\n{\n  \"approach\": \"The core of this problem lies in understanding the\
        \ bitwise OR operation between an integer `x` and `x + 1`. When we perform `x\
        \ OR (x + 1)`, the result `N` will have all the bits of `x` set, plus any trailing\
        \ zero bits of `x` (from the least significant bit up to the rightmost zero)\
        \ will also become set. Specifically, if `x` has a binary representation ending\
        \ in `...A01...1` (where `A` is some prefix and there are `k` ones after the\
        \ `0`), then `x + 1` will be `...A10...0`. The bitwise OR `x OR (x + 1)` will\
        \ then be `...A11...1`, effectively setting all bits from the rightmost zero\
        \ of `x` to the least significant bit to one. This implies that `N` must be\
        \ of the form `(2^k - 1) | (some_prefix_bits << k)` for some `k`, meaning `N`\
        \ must be an odd number, and all bits from its least significant bit up to its\
        \ rightmost zero must be set to one. If `N` is even, it's impossible to find\
        \ such an `x`, so `ans[i]` is -1. This is because `x OR (x+1)` will always result\
        \ in an odd number. If `x` is even, `x = ...0`, `x+1 = ...1`, so `x OR (x+1)\
        \ = x+1`, which is odd. If `x` is odd, `x = ...1`, `x+1 = ...0` (after carrying\
        \ over), and `x OR (x+1)` will still have the LSB set to 1, making it odd.\n\
        \nTo minimize `ans[i]`, we want to find the smallest `x` such that `x OR (x\
        \ + 1) == N`. Based on the property derived, `N` must be an odd number. If `N`\
        \ is even, `ans[i]` is -1. If `N` is odd, we need to find an `x` such that `x`\
        \ has all the bits of `N` set, except possibly some trailing ones that `x+1`\
        \ would fill in. The smallest such `x` would be `N` itself, but `N OR (N+1)`\
        \ is generally not `N`. Instead, `x` must be `N` with its lowest set bit (which\
        \ is always 0 for `N` if `N` is odd) flipped to 0. This is equivalent to `N\
        \ XOR (N & (N-1))`, or simply `N - (N & (N-1))`. More directly, `x` should be\
        \ `N` with its rightmost `1` bit unset. This can be achieved by `N ^ (N & -N)`.\
        \ For example, if `N = 7 (111)`, `x = 3 (011)`. `3 OR 4 = 7`. If `N = 5 (101)`,\
        \ `x = 4 (100)`. `4 OR 5 = 5`. This logic works because `x` must be `N` with\
        \ its lowest set bit (which is 1 for odd `N`) unset, and `x+1` will then set\
        \ that bit back to 1, and `x` will have all other bits of `N` set. However,\
        \ this is not quite right. `x` should be `N` with its lowest *zero* bit unset.\n\
        Let's re-evaluate: `x OR (x + 1) = N`. This means `N` must have all bits set\
        \ that are set in `x` and `x+1`.\nThe expression `x OR (x + 1)` effectively\
        \ sets all trailing zeros of `x` to ones. For example, if `x = 4 (100)`, `x+1\
        \ = 5 (101)`, `x OR (x+1) = 5 (101)`. If `x = 6 (110)`, `x+1 = 7 (111)`, `x\
        \ OR (x+1) = 7 (111)`.\nThis means `N` must be of the form `(x | (2^k - 1))`\
        \ where `k` is the position of the least significant zero bit in `x`.\nTo minimize\
        \ `x`, we want `x` to be as close to `N` as possible from below, such that `x`\
        \ has its lowest bit 0, and `x+1` fills in the lowest bit.\nThe condition `x\
        \ OR (x + 1) == N` implies two things:\n1. `x` must be less than or equal to\
        \ `N`.\n2. `x + 1` must be less than or equal to `N`.\n3. All bits set in `x`\
        \ must be set in `N`.\n4. All bits set in `x+1` must be set in `N`.\n5. `N`\
        \ must be odd. If `N` is even, return -1.\nIf `N` is odd, consider `x = N -\
        \ 1`. Then `x` is even. `x OR (x+1) = (N-1) OR N`. Since `N-1` is even and `N`\
        \ is odd, `N-1` ends in `...0` and `N` ends in `...1`. So `(N-1) OR N` will\
        \ have all bits of `N-1` and the last bit of `N` set. This is simply `N`. So\
        \ `x = N - 1` is a candidate.\nWhat if `N` is odd, but `N-1` is not the smallest?\n\
        Example: `N = 3 (011)`. `N-1 = 2 (010)`. `2 OR 3 = 3`. So `ans = 2`. But the\
        \ example says `ans = 1`.\n`1 (001) OR 2 (010) = 3 (011)`. So `x = 1` works.\n\
        Example: `N = 5 (101)`. `N-1 = 4 (100)`. `4 OR 5 = 5`. So `ans = 4`. This matches\
        \ the example.\nExample: `N = 7 (111)`. `N-1 = 6 (110)`. `6 OR 7 = 7`. So `ans\
        \ = 6`. But the example says `ans = 3`.\n`3 (011) OR 4 (100) = 7 (111)`. So\
        \ `x = 3` works.\n\nThe pattern seems to be: if `N` is odd, find the smallest\
        \ `k` such that `N` has all bits from `0` to `k-1` set to `1`, and bit `k` is\
        \ `0`. No, this is not right.\nThe condition `x OR (x + 1) == N` means that\
        \ `N` must be `x` with all its trailing zeros flipped to ones.\nThis implies\
        \ that `N` must be of the form `(A << (k+1)) | (2^(k+1) - 1)` where `A` is some\
        \ prefix and `k` is the position of the most significant bit of the trailing\
        \ ones in `x`.\nMore precisely, `x` must be of the form `P01...1` (where `P`\
        \ is a prefix, `0` is at bit `k`, and there are `m` ones after it).\nThen `x+1`\
        \ is `P10...0`.\n`x OR (x+1)` is `P11...1`.\nSo `N` must be of the form `P11...1`.\n\
        This means `N` must have a block of trailing ones.\nIf `N` has a binary representation\
        \ `...B11...1` (where `B` is the bit just before the block of trailing ones,\
        \ and there are `k` trailing ones), then `x` must be `...B01...1` (i.e., `N`\
        \ with the `k`-th bit from the right (0-indexed) flipped to 0).\nTo minimize\
        \ `x`, we want to find the largest `k` such that `N` has `k` trailing ones.\n\
        Let `N` be `...b_k b_{k-1} ... b_1 b_0`.\nIf `b_0 = 0`, then `N` is even. `ans\
        \ = -1`.\nIf `b_0 = 1`, `N` is odd.\nWe need to find the largest `k` such that\
        \ `N` has `k` trailing ones.\nThis means `N` is `...X01...1` (where there are\
        \ `k` ones).\nThen `x` should be `...X01...1` (same as `N`) but with the `k`-th\
        \ bit from the right (which is `0` in `N`) flipped to `0`.\nNo, this is confusing.\
        \ Let's use the hint: \"Try unsetting a single bit from `nums[i]`.\"\nLet `N\
        \ = nums[i]`.\nIf `N` is even, `ans[i] = -1`. (As derived above, `x OR (x+1)`\
        \ is always odd).\nIf `N` is odd:\nWe are looking for `x` such that `x OR (x+1)\
        \ = N`.\nThis means `x` must be `N` with some bits potentially unset.\nSpecifically,\
        \ `x` must be `N` with its lowest *zero* bit unset.\nLet `N = 11 (1011_2)`.\
        \ The lowest zero bit is at index 2. Unsetting it means `1011_2` becomes `1001_2\
        \ = 9`.\nCheck: `9 OR (9+1) = 9 OR 10 = 1001_2 OR 1010_2 = 1011_2 = 11`. This\
        \ works. `ans = 9`.\nLet `N = 13 (1101_2)`. The lowest zero bit is at index\
        \ 2. Unsetting it means `1101_2` becomes `1100_2 = 12`.\nCheck: `12 OR (12+1)\
        \ = 12 OR 13 = 1100_2 OR 1101_2 = 1101_2 = 13`. This works. `ans = 12`.\nLet\
        \ `N = 31 (11111_2)`. There are no zero bits. This implies `x` would be `N`\
        \ itself, but `N OR (N+1)` is `N | (N+1)`. If `N` has all bits set, `N = 2^k\
        \ - 1`. Then `N+1 = 2^k`. `N | (N+1) = (2^k - 1) | 2^k = 2^(k+1) - 1`. This\
        \ is not `N`.\nSo if `N` has all bits set (e.g., 3, 7, 15, 31, ...), then `N`\
        \ itself cannot be `x`.\nIn this case, `N = 3 (011_2)`. Lowest zero bit is at\
        \ index 2 (conceptually, if we extend to higher bits). Unsetting it means `011_2`\
        \ becomes `001_2 = \n'''"
      python3: "class Solution:\n    def minBitwiseArray(self, nums: List[int]) -> List[int]:\n\
        \        ans = []\n\n        for N in nums:\n            current_ans = -1\n\
        \            # Iterate k from 29 down to 0.\n            # N <= 10^9, which\
        \ is less than 2^30. So max bit position is 29.\n            for k in range(29,\
        \ -1, -1):\n                # Condition 1: k-th bit of N must be 1\n       \
        \         k_th_bit_is_set = ((N >> k) & 1) == 1\n\n                # Condition\
        \ 2: All bits from 0 to k-1 of N must be 1\n                # (1 << k) - 1 creates\
        \ a mask with k trailing ones (e.g., for k=3, mask is 0b111 = 7)\n         \
        \       # If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.\n         \
        \       mask_k_minus_1 = (1 << k) - 1\n                lower_bits_are_all_set\
        \ = (N & mask_k_minus_1) == mask_k_minus_1\n\n                if k_th_bit_is_set\
        \ and lower_bits_are_all_set:\n                    current_ans = N - (1 << k)\n\
        \                    break # Found the largest k, which gives the smallest ans[i]\n\
        \            ans.append(current_ans)\n\n        return ans"
      c: "#include <stdlib.h> // For malloc\n#include <stdbool.h> // For bool\n\n/**\n\
        \ * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* minBitwiseArray(int* nums, int numsSize, int* returnSize) {\n   \
        \ int* ans = (int*)malloc(numsSize * sizeof(int));\n    *returnSize = numsSize;\n\
        \n    for (int i = 0; i < numsSize; ++i) {\n        int N = nums[i];\n     \
        \   int current_ans = -1;\n\n        // Iterate k from 29 down to 0.\n     \
        \   // N <= 10^9, which is less than 2^30. So max bit position is 29.\n    \
        \    for (int k = 29; k >= 0; --k) {\n            // Condition 1: k-th bit of\
        \ N must be 1\n            bool k_th_bit_is_set = ((N >> k) & 1) == 1;\n\n \
        \           // Condition 2: All bits from 0 to k-1 of N must be 1\n        \
        \    // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask\
        \ is 0111_2 = 7)\n            // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always\
        \ true.\n            int mask_k_minus_1 = (1 << k) - 1;\n            bool lower_bits_are_all_set\
        \ = (N & mask_k_minus_1) == mask_k_minus_1;\n\n            if (k_th_bit_is_set\
        \ && lower_bits_are_all_set) {\n                current_ans = N - (1 << k);\n\
        \                break; // Found the largest k, which gives the smallest ans[i]\n\
        \            }\n        }\n        ans[i] = current_ans;\n    }\n\n    return\
        \ ans;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int[] MinBitwiseArray(IList<int> nums) {\n        int[] ans = new int[nums.Count];\n\
        \n        for (int i = 0; i < nums.Count; ++i) {\n            int N = nums[i];\n\
        \            int current_ans = -1;\n\n            // Iterate k from 29 down\
        \ to 0.\n            // N <= 10^9, which is less than 2^30. So max bit position\
        \ is 29.\n            for (int k = 29; k >= 0; --k) {\n                // Condition\
        \ 1: k-th bit of N must be 1\n                bool k_th_bit_is_set = ((N >>\
        \ k) & 1) == 1;\n\n                // Condition 2: All bits from 0 to k-1 of\
        \ N must be 1\n                // (1 << k) - 1 creates a mask with k trailing\
        \ ones (e.g., for k=3, mask is 0b111 = 7)\n                // If k=0, (1 <<\
        \ 0) - 1 = 0. (N & 0) == 0 is always true.\n                int mask_k_minus_1\
        \ = (1 << k) - 1;\n                bool lower_bits_are_all_set = (N & mask_k_minus_1)\
        \ == mask_k_minus_1;\n\n                if (k_th_bit_is_set && lower_bits_are_all_set)\
        \ {\n                    current_ans = N - (1 << k);\n                    break;\
        \ // Found the largest k, which gives the smallest ans[i]\n                }\n\
        \            }\n            ans[i] = current_ans;\n        }\n\n        return\
        \ ans;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar minBitwiseArray\
        \ = function(nums) {\n    const ans = [];\n\n    for (const N of nums) {\n \
        \       let current_ans = -1;\n        // Iterate k from 29 down to 0.\n   \
        \     // N <= 10^9, which is less than 2^30. So max bit position is 29.\n  \
        \      for (let k = 29; k >= 0; --k) {\n            // Condition 1: k-th bit\
        \ of N must be 1\n            const k_th_bit_is_set = ((N >> k) & 1) === 1;\n\
        \n            // Condition 2: All bits from 0 to k-1 of N must be 1\n      \
        \      // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask\
        \ is 0b111 = 7)\n            // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always\
        \ true.\n            const mask_k_minus_1 = (1 << k) - 1;\n            const\
        \ lower_bits_are_all_set = (N & mask_k_minus_1) === mask_k_minus_1;\n\n    \
        \        if (k_th_bit_is_set && lower_bits_are_all_set) {\n                current_ans\
        \ = N - (1 << k);\n                break; // Found the largest k, which gives\
        \ the smallest ans[i]\n            }\n        }\n        ans.push(current_ans);\n\
        \    }\n\n    return ans;\n};"
      typescript: "function minBitwiseArray(nums: number[]): number[] {\n    const ans:\
        \ number[] = [];\n\n    for (const N of nums) {\n        let current_ans: number\
        \ = -1;\n        // Iterate k from 29 down to 0.\n        // N <= 10^9, which\
        \ is less than 2^30. So max bit position is 29.\n        for (let k = 29; k\
        \ >= 0; --k) {\n            // Condition 1: k-th bit of N must be 1\n      \
        \      const k_th_bit_is_set: boolean = ((N >> k) & 1) === 1;\n\n          \
        \  // Condition 2: All bits from 0 to k-1 of N must be 1\n            // (1\
        \ << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask is 0b111\
        \ = 7)\n            // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.\n\
        \            const mask_k_minus_1: number = (1 << k) - 1;\n            const\
        \ lower_bits_are_all_set: boolean = (N & mask_k_minus_1) === mask_k_minus_1;\n\
        \n            if (k_th_bit_is_set && lower_bits_are_all_set) {\n           \
        \     current_ans = N - (1 << k);\n                break; // Found the largest\
        \ k, which gives the smallest ans[i]\n            }\n        }\n        ans.push(current_ans);\n\
        \    }\n\n    return ans;\n}"
      php: "<?php\n\nclass Solution {\n\n    /**\n     * @param Integer[] $nums\n  \
        \   * @return Integer[]\n     */\n    function minBitwiseArray($nums) {\n  \
        \      $ans = [];\n\n        foreach ($nums as $N) {\n            $current_ans\
        \ = -1;\n            // Iterate k from 29 down to 0.\n            // N <= 10^9,\
        \ which is less than 2^30. So max bit position is 29.\n            for ($k =\
        \ 29; $k >= 0; --$k) {\n                // Condition 1: k-th bit of N must be\
        \ 1\n                $k_th_bit_is_set = (($N >> $k) & 1) == 1;\n\n         \
        \       // Condition 2: All bits from 0 to k-1 of N must be 1\n            \
        \    // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask\
        \ is 0b111 = 7)\n                // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is\
        \ always true.\n                $mask_k_minus_1 = (1 << $k) - 1;\n         \
        \       $lower_bits_are_all_set = ($N & $mask_k_minus_1) == $mask_k_minus_1;\n\
        \n                if ($k_th_bit_is_set && $lower_bits_are_all_set) {\n     \
        \               $current_ans = $N - (1 << $k);\n                    break; //\
        \ Found the largest k, which gives the smallest ans[i]\n                }\n\
        \            }\n            $ans[] = $current_ans;\n        }\n\n        return\
        \ $ans;\n    }\n}"
      swift: "class Solution {\n    func minBitwiseArray(_ nums: [Int]) -> [Int] {\n\
        \        var ans: [Int] = []\n\n        for N in nums {\n            var currentAns:\
        \ Int = -1\n            // Iterate k from 29 down to 0.\n            // N <=\
        \ 10^9, which is less than 2^30. So max bit position is 29.\n            for\
        \ k in (0...29).reversed() {\n                // Condition 1: k-th bit of N\
        \ must be 1\n                let kThBitIsSet = ((N >> k) & 1) == 1\n\n     \
        \           // Condition 2: All bits from 0 to k-1 of N must be 1\n        \
        \        // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3,\
        \ mask is 0b111 = 7)\n                // If k=0, (1 << 0) - 1 = 0. (N & 0) ==\
        \ 0 is always true.\n                let maskKMinus1 = (1 << k) - 1\n      \
        \          let lowerBitsAreAllSet = (N & maskKMinus1) == maskKMinus1\n\n   \
        \             if kThBitIsSet && lowerBitsAreAllSet {\n                    currentAns\
        \ = N - (1 << k)\n                    break // Found the largest k, which gives\
        \ the smallest ans[i]\n                }\n            }\n            ans.append(currentAns)\n\
        \        }\n\n        return ans\n    }\n}"
    approach: 'The problem requires finding the minimum `ans[i]` such that `ans[i] OR
      (ans[i] + 1) == nums[i]`. Let `x = ans[i]` and `N = nums[i]`. Analyzing the bitwise
      OR operation `x OR (x + 1)` reveals a crucial pattern. If `x` has its rightmost
      zero bit at position `k` (i.e., `x = P01...1` where `P` is a prefix, `0` is at
      bit `k`, and there are `k` ones to its right), then `x + 1 = P10...0`. Consequently,
      `x OR (x + 1) = P11...1`. This means `N` must be of the form `P11...1`, where
      the `1` at bit `k` is the most significant bit of a contiguous block of `k+1`
      ones extending to the least significant bit.


      To find the minimum `x` for a given `N`, we need to find the largest possible
      `k` such that `N` can be represented as `P11...1` (with `k+1` trailing ones).
      This `x` would then be `N - (1 << k)`. This `x` is `N` with its `k`-th bit unset,
      and all bits from `0` to `k-1` set to `1`. For this to be a valid `x`, two conditions
      must hold for `N` and `k`: (1) the `k`-th bit of `N` must be `1`, and (2) all
      bits from `0` to `k-1` of `N` must be `1`. We iterate `k` downwards from `29`
      (since `N <= 10^9 < 2^30`) to `0`. The first `k` that satisfies both conditions
      gives the minimum `x = N - (1 << k)`. If no such `k` is found after checking all
      possibilities, it means no valid `x` exists for `N`, and `ans[i]` is set to `-1`.'
    time_complexity: The time complexity is O(M * log(max_N)), where M is the length
      of the `nums` array and `max_N` is the maximum value in `nums`. For each number
      in `nums`, we iterate through at most 30 possible bit positions (from 29 down
      to 0). Each iteration involves constant-time bitwise operations. Given `M <= 100`
      and `max_N <= 10^9`, this is roughly `100 * 30` operations, which is very efficient.
    space_complexity: The space complexity is O(M), where M is the length of the `nums`
      array. This is for storing the `ans` array, which has the same length as `nums`.
      No additional data structures are used that scale with the input values beyond
      a constant number of variables per iteration.
    elapsed_time: 353.8196671009064
    model: gemini-2.5-flash
    generated_at: '2026-01-21 19:45:51 '
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> minBitwiseArray(vector<int>&\
        \ nums) {\n        vector<int> ans;\n        for (int num : nums) {\n      \
        \      if (num % 2 == 0) ans.push_back(-1);\n            else ans.push_back(num\
        \ - 1);\n        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int[] minBitwiseArray(List<Integer> nums)\
        \ {\n        int[] ans = new int[nums.size()];\n        for (int i = 0; i <\
        \ nums.size(); i++) {\n            int num = nums.get(i);\n            if (num\
        \ % 2 == 0) ans[i] = -1;\n            else ans[i] = num - 1;\n        }\n  \
        \      return ans;\n    }\n}"
      python: "class Solution(object):\n    def minBitwiseArray(self, nums):\n     \
        \   return [num - 1 if num % 2 else -1 for num in nums]"
      python3: "class Solution:\n    def minBitwiseArray(self, nums: list[int]) -> list[int]:\n\
        \        return [num - 1 if num % 2 else -1 for num in nums]"
      c: "int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {\n    int*\
        \ ans = (int*)malloc(numsSize * sizeof(int));\n    *returnSize = numsSize;\n\
        \    for (int i = 0; i < numsSize; i++) {\n        if (nums[i] % 2 == 0) ans[i]\
        \ = -1;\n        else ans[i] = nums[i] - 1;\n    }\n    return ans;\n}"
      csharp: "public class Solution {\n    public int[] MinBitwiseArray(IList<int>\
        \ nums) {\n        int[] ans = new int[nums.Count];\n        for (int i = 0;\
        \ i < nums.Count; i++) {\n            int num = nums[i];\n            if (num\
        \ % 2 == 0) ans[i] = -1;\n            else ans[i] = num - 1;\n        }\n  \
        \      return ans;\n    }\n}"
      javascript: "var minBitwiseArray = function(nums) {\n    return nums.map(num =>\
        \ num % 2 ? num - 1 : -1);\n};"
      typescript: "function minBitwiseArray(nums: number[]): number[] {\n    return\
        \ nums.map(num => num % 2 ? num - 1 : -1);\n}"
      php: "class Solution {\n    function minBitwiseArray($nums) {\n        $ans =\
        \ [];\n        foreach ($nums as $num) {\n            if ($num % 2 == 0) $ans[]\
        \ = -1;\n            else $ans[] = $num - 1;\n        }\n        return $ans;\n\
        \    }\n}"
      swift: "class Solution {\n    func minBitwiseArray(_ nums: [Int]) -> [Int] {\n\
        \        return nums.map { $0 % 2 == 0 ? -1 : $0 - 1 }\n    }\n}"
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
        \    for i, num := range nums {\n        if num % 2 == 0 {\n            result[i]\
        \ = -1\n        } else {\n            j := num\n            for (j | (j + 1))\
        \ != num {\n                j--\n            }\n            result[i] = j\n\
        \        }\n    }\n    return result\n}"
      ruby: "def min_bitwise_array(nums)\n    result = Array.new(nums.size)\n    nums.each_with_index\
        \ do |num, i|\n        if num % 2 == 0\n            result[i] = -1\n       \
        \ else\n            j = num\n            j -= 1 while (j | (j + 1)) != num\n\
        \            result[i] = j\n        end\n    end\n    result\nend"
      scala: "object Solution {\n    def minBitwiseArray(nums: List[Int]): Array[Int]\
        \ = {\n        val result = new Array[Int](nums.size)\n        for (i <- nums.indices)\
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
      erlang: "-module(solution).\n-export([min_bitwise_array/1]).\nmin_bitwise_array(Nums)\
        \ ->\n    lists:map(fun(N) when N rem 2 == 0 -> -1;\n                   (N)\
        \ ->\n                       find_smallest(N, N)\n               end, Nums).\n\
        find_smallest(N, J) when (J bor (J + 1)) == N -> J;\nfind_smallest(N, J) ->\
        \ find_smallest(N, J - 1)."
      elixir: "defmodule Solution do\n  @spec min_bitwise_array(nums :: [integer]) ::\
        \ [integer]\n  def min_bitwise_array(nums) do\n    Enum.map(nums, fn\n     \
        \ num when rem(num, 2) == 0 -> -1\n      num -> find_smallest(num, num)\n  \
        \  end)\n  end\n\n  defp find_smallest(num, j) when bor(j, j + 1) == num, do:\
        \ j\n  defp find_smallest(num, j), do: find_smallest(num, j - 1)\nend"
    approach: The problem requires constructing an array where each element's bitwise
      OR with its next element equals a given prime number. We start by checking if
      the given number is even. If it is, we set the answer to -1 because there's no
      number that can satisfy the condition for even numbers. For odd numbers, we try
      to find the smallest number that satisfies the condition by unsetting a single
      bit from the given number. This approach works because the bitwise OR of a number
      and the number plus one will always result in a number with one more bit set than
      the original number, which is a property of binary representation.
    time_complexity: The time complexity of this solution is O(n) where n is the number
      of elements in the input array. This is because we are iterating over the array
      once and performing a constant amount of work for each element.
    space_complexity: The space complexity of this solution is O(n) where n is the number
      of elements in the input array. This is because we are creating a new array of
      the same size as the input array to store the results.
    elapsed_time: 6.01027512550354
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-21 19:46:02 '
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
  <small class="solution-timestamp">(2026-01-21 19:45:51 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires finding the minimum `ans[i]` such that `ans[i] OR (ans[i] + 1) == nums[i]`. Let `x = ans[i]` and `N = nums[i]`. Analyzing the bitwise OR operation `x OR (x + 1)` reveals a crucial pattern. If `x` has its rightmost zero bit at position `k` (i.e., `x = P01...1` where `P` is a prefix, `0` is at bit `k`, and there are `k` ones to its right), then `x + 1 = P10...0`. Consequently, `x OR (x + 1) = P11...1`. This means `N` must be of the form `P11...1`, where the `1` at bit `k` is the most significant bit of a contiguous block of `k+1` ones extending to the least significant bit.

To find the minimum `x` for a given `N`, we need to find the largest possible `k` such that `N` can be represented as `P11...1` (with `k+1` trailing ones). This `x` would then be `N - (1 << k)`. This `x` is `N` with its `k`-th bit unset, and all bits from `0` to `k-1` set to `1`. For this to be a valid `x`, two conditions must hold for `N` and `k`: (1) the `k`-th bit of `N` must be `1`, and (2) all bits from `0` to `k-1` of `N` must be `1`. We iterate `k` downwards from `29` (since `N <= 10^9 < 2^30`) to `0`. The first `k` that satisfies both conditions gives the minimum `x = N - (1 << k)`. If no such `k` is found after checking all possibilities, it means no valid `x` exists for `N`, and `ans[i]` is set to `-1`.

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
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    std::vector<int> minBitwiseArray(std::vector<int>& nums) {
        std::vector<int> ans;
        ans.reserve(nums.size());

        for (int N : nums) {
            int current_ans = -1;
            // Iterate k from 29 down to 0.
            // N <= 10^9, which is less than 2^30. So max bit position is 29.
            for (int k = 29; k >= 0; --k) {
                // Condition 1: k-th bit of N must be 1
                bool k_th_bit_is_set = ((N >> k) & 1) == 1;

                // Condition 2: All bits from 0 to k-1 of N must be 1
                // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask is 0111_2 = 7)
                // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.
                int mask_k_minus_1 = (1 << k) - 1;
                bool lower_bits_are_all_set = (N & mask_k_minus_1) == mask_k_minus_1;

                if (k_th_bit_is_set && lower_bits_are_all_set) {
                    current_ans = N - (1 << k);
                    break; // Found the largest k, which gives the smallest ans[i]
                }
            }
            ans.push_back(current_ans);
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
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int[] ans = new int[nums.size()];

        for (int i = 0; i < nums.size(); ++i) {
            int N = nums.get(i);
            int current_ans = -1;

            // Iterate k from 29 down to 0.
            // N <= 10^9, which is less than 2^30. So max bit position is 29.
            for (int k = 29; k >= 0; --k) {
                // Condition 1: k-th bit of N must be 1
                boolean k_th_bit_is_set = ((N >> k) & 1) == 1;

                // Condition 2: All bits from 0 to k-1 of N must be 1
                // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask is 0111_2 = 7)
                // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.
                int mask_k_minus_1 = (1 << k) - 1;
                boolean lower_bits_are_all_set = (N & mask_k_minus_1) == mask_k_minus_1;

                if (k_th_bit_is_set && lower_bits_are_all_set) {
                    current_ans = N - (1 << k);
                    break; // Found the largest k, which gives the smallest ans[i]
                }
            }
            ans[i] = current_ans;
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
# Failed to parse response
# Check logs for full output.
# Full Response:
'''
{
  "approach": "The core of this problem lies in understanding the bitwise OR operation between an integer `x` and `x + 1`. When we perform `x OR (x + 1)`, the result `N` will have all the bits of `x` set, plus any trailing zero bits of `x` (from the least significant bit up to the rightmost zero) will also become set. Specifically, if `x` has a binary representation ending in `...A01...1` (where `A` is some prefix and there are `k` ones after the `0`), then `x + 1` will be `...A10...0`. The bitwise OR `x OR (x + 1)` will then be `...A11...1`, effectively setting all bits from the rightmost zero of `x` to the least significant bit to one. This implies that `N` must be of the form `(2^k - 1) | (some_prefix_bits << k)` for some `k`, meaning `N` must be an odd number, and all bits from its least significant bit up to its rightmost zero must be set to one. If `N` is even, it's impossible to find such an `x`, so `ans[i]` is -1. This is because `x OR (x+1)` will always result in an odd number. If `x` is even, `x = ...0`, `x+1 = ...1`, so `x OR (x+1) = x+1`, which is odd. If `x` is odd, `x = ...1`, `x+1 = ...0` (after carrying over), and `x OR (x+1)` will still have the LSB set to 1, making it odd.

To minimize `ans[i]`, we want to find the smallest `x` such that `x OR (x + 1) == N`. Based on the property derived, `N` must be an odd number. If `N` is even, `ans[i]` is -1. If `N` is odd, we need to find an `x` such that `x` has all the bits of `N` set, except possibly some trailing ones that `x+1` would fill in. The smallest such `x` would be `N` itself, but `N OR (N+1)` is generally not `N`. Instead, `x` must be `N` with its lowest set bit (which is always 0 for `N` if `N` is odd) flipped to 0. This is equivalent to `N XOR (N & (N-1))`, or simply `N - (N & (N-1))`. More directly, `x` should be `N` with its rightmost `1` bit unset. This can be achieved by `N ^ (N & -N)`. For example, if `N = 7 (111)`, `x = 3 (011)`. `3 OR 4 = 7`. If `N = 5 (101)`, `x = 4 (100)`. `4 OR 5 = 5`. This logic works because `x` must be `N` with its lowest set bit (which is 1 for odd `N`) unset, and `x+1` will then set that bit back to 1, and `x` will have all other bits of `N` set. However, this is not quite right. `x` should be `N` with its lowest *zero* bit unset.
Let's re-evaluate: `x OR (x + 1) = N`. This means `N` must have all bits set that are set in `x` and `x+1`.
The expression `x OR (x + 1)` effectively sets all trailing zeros of `x` to ones. For example, if `x = 4 (100)`, `x+1 = 5 (101)`, `x OR (x+1) = 5 (101)`. If `x = 6 (110)`, `x+1 = 7 (111)`, `x OR (x+1) = 7 (111)`.
This means `N` must be of the form `(x | (2^k - 1))` where `k` is the position of the least significant zero bit in `x`.
To minimize `x`, we want `x` to be as close to `N` as possible from below, such that `x` has its lowest bit 0, and `x+1` fills in the lowest bit.
The condition `x OR (x + 1) == N` implies two things:
1. `x` must be less than or equal to `N`.
2. `x + 1` must be less than or equal to `N`.
3. All bits set in `x` must be set in `N`.
4. All bits set in `x+1` must be set in `N`.
5. `N` must be odd. If `N` is even, return -1.
If `N` is odd, consider `x = N - 1`. Then `x` is even. `x OR (x+1) = (N-1) OR N`. Since `N-1` is even and `N` is odd, `N-1` ends in `...0` and `N` ends in `...1`. So `(N-1) OR N` will have all bits of `N-1` and the last bit of `N` set. This is simply `N`. So `x = N - 1` is a candidate.
What if `N` is odd, but `N-1` is not the smallest?
Example: `N = 3 (011)`. `N-1 = 2 (010)`. `2 OR 3 = 3`. So `ans = 2`. But the example says `ans = 1`.
`1 (001) OR 2 (010) = 3 (011)`. So `x = 1` works.
Example: `N = 5 (101)`. `N-1 = 4 (100)`. `4 OR 5 = 5`. So `ans = 4`. This matches the example.
Example: `N = 7 (111)`. `N-1 = 6 (110)`. `6 OR 7 = 7`. So `ans = 6`. But the example says `ans = 3`.
`3 (011) OR 4 (100) = 7 (111)`. So `x = 3` works.

The pattern seems to be: if `N` is odd, find the smallest `k` such that `N` has all bits from `0` to `k-1` set to `1`, and bit `k` is `0`. No, this is not right.
The condition `x OR (x + 1) == N` means that `N` must be `x` with all its trailing zeros flipped to ones.
This implies that `N` must be of the form `(A << (k+1)) | (2^(k+1) - 1)` where `A` is some prefix and `k` is the position of the most significant bit of the trailing ones in `x`.
More precisely, `x` must be of the form `P01...1` (where `P` is a prefix, `0` is at bit `k`, and there are `m` ones after it).
Then `x+1` is `P10...0`.
`x OR (x+1)` is `P11...1`.
So `N` must be of the form `P11...1`.
This means `N` must have a block of trailing ones.
If `N` has a binary representation `...B11...1` (where `B` is the bit just before the block of trailing ones, and there are `k` trailing ones), then `x` must be `...B01...1` (i.e., `N` with the `k`-th bit from the right (0-indexed) flipped to 0).
To minimize `x`, we want to find the largest `k` such that `N` has `k` trailing ones.
Let `N` be `...b_k b_{k-1} ... b_1 b_0`.
If `b_0 = 0`, then `N` is even. `ans = -1`.
If `b_0 = 1`, `N` is odd.
We need to find the largest `k` such that `N` has `k` trailing ones.
This means `N` is `...X01...1` (where there are `k` ones).
Then `x` should be `...X01...1` (same as `N`) but with the `k`-th bit from the right (which is `0` in `N`) flipped to `0`.
No, this is confusing. Let's use the hint: "Try unsetting a single bit from `nums[i]`."
Let `N = nums[i]`.
If `N` is even, `ans[i] = -1`. (As derived above, `x OR (x+1)` is always odd).
If `N` is odd:
We are looking for `x` such that `x OR (x+1) = N`.
This means `x` must be `N` with some bits potentially unset.
Specifically, `x` must be `N` with its lowest *zero* bit unset.
Let `N = 11 (1011_2)`. The lowest zero bit is at index 2. Unsetting it means `1011_2` becomes `1001_2 = 9`.
Check: `9 OR (9+1) = 9 OR 10 = 1001_2 OR 1010_2 = 1011_2 = 11`. This works. `ans = 9`.
Let `N = 13 (1101_2)`. The lowest zero bit is at index 2. Unsetting it means `1101_2` becomes `1100_2 = 12`.
Check: `12 OR (12+1) = 12 OR 13 = 1100_2 OR 1101_2 = 1101_2 = 13`. This works. `ans = 12`.
Let `N = 31 (11111_2)`. There are no zero bits. This implies `x` would be `N` itself, but `N OR (N+1)` is `N | (N+1)`. If `N` has all bits set, `N = 2^k - 1`. Then `N+1 = 2^k`. `N | (N+1) = (2^k - 1) | 2^k = 2^(k+1) - 1`. This is not `N`.
So if `N` has all bits set (e.g., 3, 7, 15, 31, ...), then `N` itself cannot be `x`.
In this case, `N = 3 (011_2)`. Lowest zero bit is at index 2 (conceptually, if we extend to higher bits). Unsetting it means `011_2` becomes `001_2 = 
'''
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for N in nums:
            current_ans = -1
            # Iterate k from 29 down to 0.
            # N <= 10^9, which is less than 2^30. So max bit position is 29.
            for k in range(29, -1, -1):
                # Condition 1: k-th bit of N must be 1
                k_th_bit_is_set = ((N >> k) & 1) == 1

                # Condition 2: All bits from 0 to k-1 of N must be 1
                # (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask is 0b111 = 7)
                # If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.
                mask_k_minus_1 = (1 << k) - 1
                lower_bits_are_all_set = (N & mask_k_minus_1) == mask_k_minus_1

                if k_th_bit_is_set and lower_bits_are_all_set:
                    current_ans = N - (1 << k)
                    break # Found the largest k, which gives the smallest ans[i]
            ans.append(current_ans)

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h> // For malloc
#include <stdbool.h> // For bool

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {
    int* ans = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;

    for (int i = 0; i < numsSize; ++i) {
        int N = nums[i];
        int current_ans = -1;

        // Iterate k from 29 down to 0.
        // N <= 10^9, which is less than 2^30. So max bit position is 29.
        for (int k = 29; k >= 0; --k) {
            // Condition 1: k-th bit of N must be 1
            bool k_th_bit_is_set = ((N >> k) & 1) == 1;

            // Condition 2: All bits from 0 to k-1 of N must be 1
            // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask is 0111_2 = 7)
            // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.
            int mask_k_minus_1 = (1 << k) - 1;
            bool lower_bits_are_all_set = (N & mask_k_minus_1) == mask_k_minus_1;

            if (k_th_bit_is_set && lower_bits_are_all_set) {
                current_ans = N - (1 << k);
                break; // Found the largest k, which gives the smallest ans[i]
            }
        }
        ans[i] = current_ans;
    }

    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        int[] ans = new int[nums.Count];

        for (int i = 0; i < nums.Count; ++i) {
            int N = nums[i];
            int current_ans = -1;

            // Iterate k from 29 down to 0.
            // N <= 10^9, which is less than 2^30. So max bit position is 29.
            for (int k = 29; k >= 0; --k) {
                // Condition 1: k-th bit of N must be 1
                bool k_th_bit_is_set = ((N >> k) & 1) == 1;

                // Condition 2: All bits from 0 to k-1 of N must be 1
                // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask is 0b111 = 7)
                // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.
                int mask_k_minus_1 = (1 << k) - 1;
                bool lower_bits_are_all_set = (N & mask_k_minus_1) == mask_k_minus_1;

                if (k_th_bit_is_set && lower_bits_are_all_set) {
                    current_ans = N - (1 << k);
                    break; // Found the largest k, which gives the smallest ans[i]
                }
            }
            ans[i] = current_ans;
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
 * @return {number[]}
 */
var minBitwiseArray = function(nums) {
    const ans = [];

    for (const N of nums) {
        let current_ans = -1;
        // Iterate k from 29 down to 0.
        // N <= 10^9, which is less than 2^30. So max bit position is 29.
        for (let k = 29; k >= 0; --k) {
            // Condition 1: k-th bit of N must be 1
            const k_th_bit_is_set = ((N >> k) & 1) === 1;

            // Condition 2: All bits from 0 to k-1 of N must be 1
            // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask is 0b111 = 7)
            // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.
            const mask_k_minus_1 = (1 << k) - 1;
            const lower_bits_are_all_set = (N & mask_k_minus_1) === mask_k_minus_1;

            if (k_th_bit_is_set && lower_bits_are_all_set) {
                current_ans = N - (1 << k);
                break; // Found the largest k, which gives the smallest ans[i]
            }
        }
        ans.push(current_ans);
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
    const ans: number[] = [];

    for (const N of nums) {
        let current_ans: number = -1;
        // Iterate k from 29 down to 0.
        // N <= 10^9, which is less than 2^30. So max bit position is 29.
        for (let k = 29; k >= 0; --k) {
            // Condition 1: k-th bit of N must be 1
            const k_th_bit_is_set: boolean = ((N >> k) & 1) === 1;

            // Condition 2: All bits from 0 to k-1 of N must be 1
            // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask is 0b111 = 7)
            // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.
            const mask_k_minus_1: number = (1 << k) - 1;
            const lower_bits_are_all_set: boolean = (N & mask_k_minus_1) === mask_k_minus_1;

            if (k_th_bit_is_set && lower_bits_are_all_set) {
                current_ans = N - (1 << k);
                break; // Found the largest k, which gives the smallest ans[i]
            }
        }
        ans.push(current_ans);
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
     * @param Integer[] $nums
     * @return Integer[]
     */
    function minBitwiseArray($nums) {
        $ans = [];

        foreach ($nums as $N) {
            $current_ans = -1;
            // Iterate k from 29 down to 0.
            // N <= 10^9, which is less than 2^30. So max bit position is 29.
            for ($k = 29; $k >= 0; --$k) {
                // Condition 1: k-th bit of N must be 1
                $k_th_bit_is_set = (($N >> $k) & 1) == 1;

                // Condition 2: All bits from 0 to k-1 of N must be 1
                // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask is 0b111 = 7)
                // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.
                $mask_k_minus_1 = (1 << $k) - 1;
                $lower_bits_are_all_set = ($N & $mask_k_minus_1) == $mask_k_minus_1;

                if ($k_th_bit_is_set && $lower_bits_are_all_set) {
                    $current_ans = $N - (1 << $k);
                    break; // Found the largest k, which gives the smallest ans[i]
                }
            }
            $ans[] = $current_ans;
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

        for N in nums {
            var currentAns: Int = -1
            // Iterate k from 29 down to 0.
            // N <= 10^9, which is less than 2^30. So max bit position is 29.
            for k in (0...29).reversed() {
                // Condition 1: k-th bit of N must be 1
                let kThBitIsSet = ((N >> k) & 1) == 1

                // Condition 2: All bits from 0 to k-1 of N must be 1
                // (1 << k) - 1 creates a mask with k trailing ones (e.g., for k=3, mask is 0b111 = 7)
                // If k=0, (1 << 0) - 1 = 0. (N & 0) == 0 is always true.
                let maskKMinus1 = (1 << k) - 1
                let lowerBitsAreAllSet = (N & maskKMinus1) == maskKMinus1

                if kThBitIsSet && lowerBitsAreAllSet {
                    currentAns = N - (1 << k)
                    break // Found the largest k, which gives the smallest ans[i]
                }
            }
            ans.append(currentAns)
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(M * log(max_N)), where M is the length of the `nums` array and `max_N` is the maximum value in `nums`. For each number in `nums`, we iterate through at most 30 possible bit positions (from 29 down to 0). Each iteration involves constant-time bitwise operations. Given `M <= 100` and `max_N <= 10^9`, this is roughly `100 * 30` operations, which is very efficient.

- **Space Complexity:** The space complexity is O(M), where M is the length of the `nums` array. This is for storing the `ans` array, which has the same length as `nums`. No additional data structures are used that scale with the input values beyond a constant number of variables per iteration.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-21 19:46:02 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires constructing an array where each element's bitwise OR with its next element equals a given prime number. We start by checking if the given number is even. If it is, we set the answer to -1 because there's no number that can satisfy the condition for even numbers. For odd numbers, we try to find the smallest number that satisfies the condition by unsetting a single bit from the given number. This approach works because the bitwise OR of a number and the number plus one will always result in a number with one more bit set than the original number, which is a property of binary representation.

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
            else ans.push_back(num - 1);
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
            else ans[i] = num - 1;
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
        return [num - 1 if num % 2 else -1 for num in nums]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        return [num - 1 if num % 2 else -1 for num in nums]
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
        if (nums[i] % 2 == 0) ans[i] = -1;
        else ans[i] = nums[i] - 1;
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
            else ans[i] = num - 1;
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
    return nums.map(num => num % 2 ? num - 1 : -1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minBitwiseArray(nums: number[]): number[] {
    return nums.map(num => num % 2 ? num - 1 : -1);
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
            else $ans[] = $num - 1;
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
        return nums.map { $0 % 2 == 0 ? -1 : $0 - 1 }
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
        if num % 2 == 0 {
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
        val result = new Array[Int](nums.size)
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
-module(solution).
-export([min_bitwise_array/1]).
min_bitwise_array(Nums) ->
    lists:map(fun(N) when N rem 2 == 0 -> -1;
                   (N) ->
                       find_smallest(N, N)
               end, Nums).
find_smallest(N, J) when (J bor (J + 1)) == N -> J;
find_smallest(N, J) -> find_smallest(N, J - 1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn
      num when rem(num, 2) == 0 -> -1
      num -> find_smallest(num, num)
    end)
  end

  defp find_smallest(num, j) when bor(j, j + 1) == num, do: j
  defp find_smallest(num, j), do: find_smallest(num, j - 1)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n) where n is the number of elements in the input array. This is because we are iterating over the array once and performing a constant amount of work for each element.

- **Space Complexity:** The space complexity of this solution is O(n) where n is the number of elements in the input array. This is because we are creating a new array of the same size as the input array to store the results.

</div>
</details>
