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
        \ bitwise OR operation `x OR (x + 1)`. Let's analyze the binary representation\
        \ of `x` and `x+1`. If `x` is an even number, its least significant bit (LSB)\
        \ is 0, so `x = ...0_2`. Then `x+1 = ...1_2`. In this case, `x OR (x+1) = (...0_2)\
        \ OR (...1_2) = ...1_2 = x+1`. This means if `ans[i]` is even, `ans[i] OR (ans[i]+1)`\
        \ will be `ans[i]+1`, which must be an odd number. Therefore, if `nums[i]` is\
        \ even, no such `ans[i]` exists, and we should set `ans[i] = -1`. Since `nums[i]`\
        \ are prime numbers, the only even prime is 2. So for `nums[i] = 2`, `ans[i]`\
        \ must be -1. For all other prime numbers, `nums[i]` is odd.\",\n  \"time_complexity\"\
        : \"The time complexity is O(N) where N is the length of the input array `nums`.\
        \ For each number in `nums`, we perform a constant number of bitwise operations\
        \ (finding the rightmost zero bit, shifting, and ORing). These operations take\
        \ logarithmic time with respect to the value of `nums[i]`, but since `nums[i]`\
        \ is bounded by 10^9 (which fits in a 32-bit integer), this is effectively a\
        \ constant number of operations per element.\",\n  \"space_complexity\": \"\
        The space complexity is O(N) to store the result array `ans`. If we were allowed\
        \ to modify the input array in place, the space complexity would be O(1) (excluding\
        \ the input/output storage).\",\n  \"solutions\": {\n    \"cpp\": \"class Solution\
        \ {\\npublic:\\n    std::vector<int> minBitwiseArray(std::vector<int>& nums)\
        \ {\\n        std::vector<int> ans;\\n        for (int num : nums) {\\n    \
        \        if (num % 2 == 0) { // If num is even, ans[i] OR (ans[i]+1) can only\
        \ be odd if ans[i] is even, or odd if ans[i] is odd. If ans[i] is even, result\
        \ is ans[i]+1 (odd). If ans[i] is odd, result is (ans[i] | (ans[i]+1)) which\
        \ is always odd. So an even num[i] cannot be formed.\\n                ans.push_back(-1);\\\
        n            } else {\\n                // num is odd. We need ans | (ans+1)\
        \ = num.\\n                // Let ans = P01...1 (binary, k ones at the end)\\\
        n                // Then ans+1 = P10...0 (binary, k zeros at the end)\\n   \
        \             // ans | (ans+1) = P11...1 (binary, k+1 ones at the end)\\n  \
        \              // This means num must be of the form P11...1\\n            \
        \    // To minimize ans, we want to maximize the number of trailing ones in\
        \ ans.\\n                // This means we want to find the smallest k such that\
        \ num has a 0 at bit k and all bits 0 to k-1 are 1.\\n                // If\
        \ num = P11...1, then ans = P01...1\\n                // This is equivalent\
        \ to ans = num ^ (1 << k) where k is the position of the rightmost 1 in num's\
        \ complement (num ^ (num+1)).\\n                // Or, more simply, ans = num\
        \ - (num & (num-1)) - 1. No, this is not right.\\n                // The pattern\
        \ is: if num = X11...1 (k ones), then ans = X01...1 (k ones).\\n           \
        \     // This means ans = num - (1 << k) where k is the position of the rightmost\
        \ 1 in num.\\n                // No, this is also not right. Example: num =\
        \ 7 (111_2). ans = 3 (011_2). k=2 (position of MSB of 3). ans = 7 - (1<<2) =\
        \ 3.\\n                // Example: num = 5 (101_2). ans = 4 (100_2). k=0 (position\
        \ of LSB of 5). ans = 5 - (1<<0) = 4.\\n                // Example: num = 3\
        \ (011_2). ans = 1 (001_2). k=1 (position of LSB of 3). ans = 3 - (1<<1) = 1.\\\
        n                // The pattern is: ans = num - (1 << (rightmost_zero_bit_position_in_ans)).\\\
        n                // Let's find the position of the rightmost 0 bit in `num`.\\\
        n                // If `num` is `...X11...1` (k ones), then `ans` is `...X01...1`\
        \ (k ones).\\n                // `ans = num - (1 << k)` where `k` is the position\
        \ of the rightmost 1 in `num`.\\n                // This is equivalent to `ans\
        \ = num ^ (num & (num-1))` then `ans = num - (ans & -ans)`.\\n             \
        \   // The hint says \\\"Try unsetting a single bit from nums[i]\\\".\\n   \
        \             // If ans | (ans+1) = num, then num must have all bits set that\
        \ are set in ans AND all bits set that are set in ans+1.\\n                //\
        \ Also, since ans < ans+1, the most significant bit of ans and ans+1 are usually\
        \ the same, or ans+1 has one more bit.\\n                // The key property\
        \ of x | (x+1) is that it sets all trailing zeros of x to one.\\n          \
        \      // E.g., x = 4 (100_2), x+1 = 5 (101_2), x | (x+1) = 101_2 = 5.\\n  \
        \              // E.g., x = 6 (110_2), x+1 = 7 (111_2), x | (x+1) = 111_2 =\
        \ 7.\\n                // E.g., x = 1 (001_2), x+1 = 2 (010_2), x | (x+1) =\
        \ 011_2 = 3.\\n                // E.g., x = 3 (011_2), x+1 = 4 (100_2), x |\
        \ (x+1) = 111_2 = 7.\\n                // The result `num` will always be of\
        \ the form `...11...1` (all ones from LSB up to some point).\\n            \
        \    // Specifically, `num` will be `(x | (x+1))`. The bits of `x` and `x+1`\
        \ are identical until the rightmost `0` bit of `x`.\\n                // Let\
        \ `x = A01...1` (where `k` ones follow the `0`).\\n                // Then `x+1\
        \ = A10...0` (where `k` zeros follow the `1`).\\n                // `x | (x+1)\
        \ = A11...1` (where `k+1` ones follow the `A`).\\n                // So, `num`\
        \ must be of the form `A11...1`.\\n                // To find the minimum `ans`,\
        \ we need to find the largest `k` such that `num` has `k` trailing ones, and\
        \ the `k+1`-th bit is `0` in `ans`.\\n                // This means `ans` should\
        \ be `num` with its rightmost `1` bit unset.\\n                // The rightmost\
        \ `1` bit of `num` is `num & (-num)` (using two's complement).\\n          \
        \      // So, `ans = num - (num & (-num))`.\\n                // Let's test\
        \ this:\\n                // num = 3 (011_2). -3 is (111...1101_2). 3 & (-3)\
        \ = 1 (001_2). ans = 3 - 1 = 2. But example says 1.\\n                // This\
        \ logic is flawed.\\n\\n                // Let's re-evaluate the property: `x\
        \ OR (x+1)`. The bits of `x` and `x+1` are identical until the rightmost `0`\
        \ bit of `x`. Let this position be `k`.\\n                // So `x = (prefix)0(1...1)_2`\
        \ where `k` ones follow the `0` bit.\\n                // `x+1 = (prefix)1(0...0)_2`\
        \ where `k` zeros follow the `1` bit.\\n                // `x OR (x+1) = (prefix)1(1...1)_2`\
        \ where `k` ones follow the `1` bit.\\n                // This means `num` must\
        \ be of the form `(prefix)11...1` (k+1 ones).\\n                // To minimize\
        \ `ans`, we need to find the largest `k` such that `num` has `k+1` trailing\
        \ ones.\\n                // This means `num` must be `(some_value) * 2^(k+1)\
        \ - 1` for some `k`.\\n                // Example: num = 3 (011_2). Here k+1\
        \ = 2. So k=1. ans = 1 (001_2). This is `num` with the bit at position `k+1`\
        \ (2) unset, and all bits below it `0`.\\n                // This is `num -\
        \ (1 << (k+1)) + ( (1 << k) - 1 )`.\\n                // This is `num - (1 <<\
        \ (k+1)) + ( (1 << (k+1)) / 2 - 1 )`.\\n                // This is `num - (1\
        \ << k)`. No, this is not right.\\n\\n                // Let's use the hint:\
        \ \\\"Try unsetting a single bit from nums[i]\\\".\\n                // If `ans\
        \ = nums[i] ^ (1 << k)` for some `k`.\\n                // We want `ans | (ans+1)\
        \ == nums[i]`.\\n                // Consider `nums[i]`. It's odd. So its LSB\
        \ is 1.\\n                // If `ans` is `nums[i] - (1 << k)` for some `k`.\\\
        n                // We need `ans` to be `...01...1` and `ans+1` to be `...10...0`\
        \ such that their OR is `nums[i]`.\\n                // This means `nums[i]`\
        \ must be `...11...1`.\\n                // The value `ans` must be `nums[i]`\
        \ with its rightmost `1` bit unset, and then all bits below that position set\
        \ to `1`.\\n                // For example, `nums[i] = 7 (111_2)`. Rightmost\
        \ `1` is at position 0. Unsetting it gives `6 (110_2)`. This is not `ans=3`.\\\
        n                // The correct logic is: `ans` must be `\n'''"
      kotlin: "class Solution {\n    fun minBitwiseArray(nums: List<Int>): IntArray\
        \ {\n        val ans = IntArray(nums.size)\n        for (i in nums.indices)\
        \ {\n            val nVal = nums[i]\n            if (nVal % 2 == 0) {\n    \
        \            ans[i] = -1\n            } else {\n                // Candidate\
        \ 1: x = N-1. This is always valid if N is odd.\n                // (N-1) is\
        \ even, so (N-1) OR N = N.\n                var currentMinX = nVal - 1\n\n \
        \               // Candidate 2: x = N - (1 << p) for some p >= 1.\n        \
        \        // This is valid if N has its p-th bit set, AND\n                //\
        \ the lower p bits of N are all 1s. In this case,\n                // N's binary\
        \ form is (prefix)1(1...1) (p ones),\n                // and x = (prefix)0(1...1)\
        \ (p ones).\n                // Then x+1 = (prefix)1(0...0) (p zeros),\n   \
        \             // and x OR (x+1) = (prefix)1(1...1) which equals N.\n       \
        \         // We iterate p from 1 up to 30 (since N <= 10^9 < 2^30).\n      \
        \          for (p in 1..30) {\n                    // Check if p-th bit of N\
        \ is set\n                    if ((nVal shr p) and 1 == 1) {\n             \
        \           // Check if lower p bits of N are all 1s\n                     \
        \   val mask = (1 shl p) - 1\n                        if ((nVal and mask) ==\
        \ mask) {\n                            val candidateX = nVal - (1 shl p)\n \
        \                           currentMinX = Math.min(currentMinX, candidateX)\n\
        \                        }\n                    }\n                }\n     \
        \           ans[i] = currentMinX\n            }\n        }\n        return ans\n\
        \    }\n}"
      dart: "class Solution {\n  List<int> minBitwiseArray(List<int> nums) {\n    List<int>\
        \ ans = [];\n    for (int nVal in nums) {\n      if (nVal % 2 == 0) {\n    \
        \    ans.add(-1);\n      } else {\n        // Candidate 1: x = N-1. This is\
        \ always valid if N is odd.\n        // (N-1) is even, so (N-1) OR N = N.\n\
        \        int currentMinX = nVal - 1;\n\n        // Candidate 2: x = N - (1 <<\
        \ p) for some p >= 1.\n        // This is valid if N has its p-th bit set, AND\n\
        \        // the lower p bits of N are all 1s.\n        // We iterate p from\
        \ 1 up to 30 (since N <= 10^9 < 2^30).\n        for (int p = 1; p <= 30; p++)\
        \ {\n          // Check if p-th bit of N is set\n          if (((nVal >> p)\
        \ & 1) == 1) {\n            // Check if lower p bits of N are all 1s\n     \
        \       int mask = (1 << p) - 1;\n            if ((nVal & mask) == mask) {\n\
        \              int candidateX = nVal - (1 << p);\n              currentMinX\
        \ = currentMinX < candidateX ? currentMinX : candidateX;\n            }\n  \
        \        }\n        }\n        ans.add(currentMinX);\n      }\n    }\n    return\
        \ ans;\n  }\n}"
      go: "func minBitwiseArray(nums []int) []int {\n    ans := make([]int, len(nums))\n\
        \    for i, nVal := range nums {\n        if nVal % 2 == 0 {\n            ans[i]\
        \ = -1\n        } else {\n            // Candidate 1: x = N-1. This is always\
        \ valid if N is odd.\n            // (N-1) is even, so (N-1) OR N = N.\n   \
        \         currentMinX := nVal - 1\n\n            // Candidate 2: x = N - (1\
        \ << p) for some p >= 1.\n            // This is valid if N has its p-th bit\
        \ set, AND\n            // the lower p bits of N are all 1s.\n            //\
        \ We iterate p from 1 up to 30 (since N <= 10^9 < 2^30).\n            for p\
        \ := 1; p <= 30; p++ {\n                // Check if p-th bit of N is set\n \
        \               if ((nVal >> p) & 1) == 1 {\n                    // Check if\
        \ lower p bits of N are all 1s\n                    mask := (1 << p) - 1\n \
        \                   if (nVal & mask) == mask {\n                        candidateX\
        \ := nVal - (1 << p)\n                        if candidateX < currentMinX {\n\
        \                            currentMinX = candidateX\n                    \
        \    }\n                    }\n                }\n            }\n          \
        \  ans[i] = currentMinX\n        }\n    }\n    return ans\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer[]}\ndef min_bitwise_array(nums)\n\
        \    ans = []\n    nums.each do |n_val|\n        if n_val % 2 == 0\n       \
        \     ans << -1\n        else\n            # Candidate 1: x = N-1. This is always\
        \ valid if N is odd.\n            # (N-1) is even, so (N-1) OR N = N.\n    \
        \        current_min_x = n_val - 1\n\n            # Candidate 2: x = N - (1\
        \ << p) for some p >= 1.\n            # This is valid if N has its p-th bit\
        \ set, AND\n            # the lower p bits of N are all 1s.\n            # We\
        \ iterate p from 1 up to 30 (since N <= 10^9 < 2^30).\n            (1..30).each\
        \ do |p|\n                # Check if p-th bit of N is set\n                if\
        \ ((n_val >> p) & 1) == 1\n                    # Check if lower p bits of N\
        \ are all 1s\n                    mask = (1 << p) - 1\n                    if\
        \ (n_val & mask) == mask\n                        candidate_x = n_val - (1 <<\
        \ p)\n                        current_min_x = [current_min_x, candidate_x].min\n\
        \                    end\n                end\n            end\n           \
        \ ans << current_min_x\n        end\n    end\n    ans\nend"
      scala: "object Solution {\n    def minBitwiseArray(nums: List[Int]): Array[Int]\
        \ = {\n        val ans = Array.ofDim[Int](nums.length)\n        for (i <- nums.indices)\
        \ {\n            val nVal = nums(i)\n            if (nVal % 2 == 0) {\n    \
        \            ans(i) = -1\n            } else {\n                // Candidate\
        \ 1: x = N-1. This is always valid if N is odd.\n                // (N-1) is\
        \ even, so (N-1) OR N = N.\n                var currentMinX = nVal - 1\n\n \
        \               // Candidate 2: x = N - (1 << p) for some p >= 1.\n        \
        \        // This is valid if N has its p-th bit set, AND\n                //\
        \ the lower p bits of N are all 1s.\n                // We iterate p from 1\
        \ up to 30 (since N <= 10^9 < 2^30).\n                for (p <- 1 to 30) {\n\
        \                    // Check if p-th bit of N is set\n                    if\
        \ (((nVal >> p) & 1) == 1) {\n                        // Check if lower p bits\
        \ of N are all 1s\n                        val mask = (1 << p) - 1\n       \
        \                 if ((nVal & mask) == mask) {\n                           \
        \ val candidateX = nVal - (1 << p)\n                            currentMinX\
        \ = Math.min(currentMinX, candidateX)\n                        }\n         \
        \           }\n                }\n                ans(i) = currentMinX\n   \
        \         }\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        let mut ans = Vec::with_capacity(nums.len());\n        for n_val\
        \ in nums {\n            if n_val % 2 == 0 {\n                ans.push(-1);\n\
        \            } else {\n                // Candidate 1: x = N-1. This is always\
        \ valid if N is odd.\n                // (N-1) is even, so (N-1) OR N = N.\n\
        \                let mut current_min_x = n_val - 1;\n\n                // Candidate\
        \ 2: x = N - (1 << p) for some p >= 1.\n                // This is valid if\
        \ N has its p-th bit set, AND\n                // the lower p bits of N are\
        \ all 1s.\n                // We iterate p from 1 up to 30 (since N <= 10^9\
        \ < 2^30).\n                for p in 1..=30 {\n                    // Check\
        \ if p-th bit of N is set\n                    if ((n_val >> p) & 1) == 1 {\n\
        \                        // Check if lower p bits of N are all 1s\n        \
        \                let mask = (1 << p) - 1;\n                        if (n_val\
        \ & mask) == mask {\n                            let candidate_x = n_val - (1\
        \ << p);\n                            current_min_x = current_min_x.min(candidate_x);\n\
        \                        }\n                    }\n                }\n     \
        \           ans.push(current_min_x);\n            }\n        }\n        ans\n\
        \    }\n}"
      racket: "(define/contract (min-bitwise-array nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (for/list ([n-val nums])\n    (if (even? n-val)\n\
        \        -1\n        (let loop ([p 1]\n                   [current-min-x (-\
        \ n-val 1)]) ; Candidate 1: N-1\n          (if (> p 30)\n              current-min-x\n\
        \              (let* ([p-bit-set? (= (bitwise-and (bitwise-rshift n-val p) 1)\
        \ 1)]\n                     [mask (- (bitwise-lshift 1 p) 1)]\n            \
        \         [lower-bits-all-ones? (= (bitwise-and n-val mask) mask)])\n      \
        \          (if (and p-bit-set? lower-bits-all-ones?)\n                    (let\
        \ ([candidate-x (- n-val (bitwise-lshift 1 p))])\n                      (loop\
        \ (+ p 1) (min current-min-x candidate-x)))\n                    (loop (+ p\
        \ 1) current-min-x))))))))"
      erlang: '-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].

        min_bitwise_array(Nums) ->

        lists:map(fun(NVal) ->

        if

        NVal rem 2 == 0 ->

        -1;

        true ->

        % Candidate 1: x = N-1. This is always valid if N is odd.

        % (N-1) is even, so (N-1) bor N = N.

        CurrentMinX = NVal - 1,

        % Candidate 2: x = N - (1 bsl P) for some P >= 1.

        % This is valid if N has its P-th bit set, AND

        % the lower P bits of N are all 1s.

        % We iterate P from 1 up to 30 (since N =< 10^9 < 2^30).

        min_bitwise_array_loop(1, 30, NVal, CurrentMinX)

        end

        end, Nums).


        min_bitwise_array_loop(P, MaxP, NVal, AccMinX) when P =< MaxP ->

        % Check if P-th bit of N is set

        PBitSet = ((NVal bsr P) band 1) == 1,

        % Check if lower P bits of N are all 1s

        Mask = (1 bsl P) - 1,

        LowerBitsAllOnes = (NVal band Mask) == Mask,


        NewAccMinX = if

        PBitSet and LowerBitsAllOnes ->

        CandidateX = NVal - (1 bsl P),

        min(AccMinX, CandidateX);

        true ->

        AccMinX

        end,

        min_bitwise_array_loop(P + 1, MaxP, NVal, NewAccMinX);

        min_bitwise_array_loop(_P, _MaxP, _NVal, AccMinX) ->

        AccMinX.'
      elixir: "defmodule Solution do\n  @spec min_bitwise_array(nums :: [integer]) ::\
        \ [integer]\n  def min_bitwise_array(nums) do\n    Enum.map(nums, fn n_val ->\n\
        \      if rem(n_val, 2) == 0 do\n        -1\n      else\n        # Candidate\
        \ 1: x = N-1. This is always valid if N is odd.\n        # (N-1) is even, so\
        \ (N-1) ||| N = N.\n        current_min_x = n_val - 1\n\n        # Candidate\
        \ 2: x = N - (1 <<< p) for some p >= 1.\n        # This is valid if N has its\
        \ p-th bit set, AND\n        # the lower p bits of N are all 1s.\n        #\
        \ We iterate p from 1 up to 30 (since N <= 10^9 < 2^30).\n        Enum.reduce(1..30,\
        \ current_min_x, fn p, acc_min_x ->\n          # Check if p-th bit of N is set\n\
        \          p_bit_set = (((n_val >>> p) &&& 1) == 1)\n          # Check if lower\
        \ p bits of N are all 1s\n          mask = (1 <<< p) - 1\n          lower_bits_all_ones\
        \ = ((n_val &&& mask) == mask)\n\n          if p_bit_set and lower_bits_all_ones\
        \ do\n            candidate_x = n_val - (1 <<< p)\n            min(acc_min_x,\
        \ candidate_x)\n          else\n            acc_min_x\n          end\n     \
        \   end)\n      end\n    end)\n  end\nend"
    approach: The problem requires finding the minimum `ans[i]` such that `ans[i] OR
      (ans[i] + 1) == nums[i]`. We first analyze the bitwise OR operation `x OR (x +
      1)`. If `x` is an even number, its binary representation ends in `0`, so `x =
      ...0`. Then `x + 1 = ...1`. The bitwise OR `x OR (x + 1)` will be `...1`, which
      is always an odd number. Therefore, if `nums[i]` is an even number, it's impossible
      to satisfy the condition, and `ans[i]` must be -1. This covers the case `nums[i]
      = 2` (the only even prime).
    time_complexity: The time complexity is O(N * log(max_val)) where N is the length
      of the `nums` array and `max_val` is the maximum value in `nums`. For each number
      in `nums`, we perform a constant number of bitwise operations and a loop that
      iterates up to `log2(max_val)` times (approximately 30 for 10^9). Thus, the total
      time complexity is proportional to `nums.length` multiplied by a small constant
      factor.
    space_complexity: The space complexity is O(N) where N is the length of the `nums`
      array. This is due to storing the `ans` array, which has the same length as the
      input `nums` array.
    elapsed_time: 339.1644480228424
    model: gemini-2.5-flash
    generated_at: '2026-01-21 01:16:48 '
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> minBitwiseArray(vector<int>&\
        \ nums) {\n        vector<int> ans;\n        for (int num : nums) {\n      \
        \      if (num % 2 == 0) {\n                ans.push_back(-1);\n           \
        \ } else {\n                ans.push_back(num - 1);\n            }\n       \
        \ }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int[] minBitwiseArray(List<Integer> nums)\
        \ {\n        int[] ans = new int[nums.size()];\n        for (int i = 0; i <\
        \ nums.size(); i++) {\n            int num = nums.get(i);\n            if (num\
        \ % 2 == 0) {\n                ans[i] = -1;\n            } else {\n        \
        \        ans[i] = num - 1;\n            }\n        }\n        return ans;\n\
        \    }\n}"
      python: "class Solution(object):\n    def minBitwiseArray(self, nums):\n     \
        \   \"\"\"\n        :type nums: List[int]\n        :rtype: List[int]\n     \
        \   \"\"\"\n        ans = []\n        for num in nums:\n            if num %\
        \ 2 == 0:\n                ans.append(-1)\n            else:\n             \
        \   ans.append(num - 1)\n        return ans"
      python3: "class Solution:\n    def minBitwiseArray(self, nums: List[int]) -> List[int]:\n\
        \        ans = []\n        for num in nums:\n            if num % 2 == 0:\n\
        \                ans.append(-1)\n            else:\n                ans.append(num\
        \ - 1)\n        return ans"
      c: "int* minBitwiseArray(int* nums, int numsSize, int* returnSize) {\n    int*\
        \ ans = (int*)malloc(numsSize * sizeof(int));\n    *returnSize = numsSize;\n\
        \    for (int i = 0; i < numsSize; i++) {\n        if (nums[i] % 2 == 0) {\n\
        \            ans[i] = -1;\n        } else {\n            ans[i] = nums[i] -\
        \ 1;\n        }\n    }\n    return ans;\n}"
      csharp: "public class Solution {\n    public int[] MinBitwiseArray(IList<int>\
        \ nums) {\n        int[] ans = new int[nums.Count];\n        for (int i = 0;\
        \ i < nums.Count; i++) {\n            int num = nums[i];\n            if (num\
        \ % 2 == 0) {\n                ans[i] = -1;\n            } else {\n        \
        \        ans[i] = num - 1;\n            }\n        }\n        return ans;\n\
        \    }\n}"
      javascript: "var minBitwiseArray = function(nums) {\n    let ans = [];\n    for\
        \ (let num of nums) {\n        if (num % 2 == 0) {\n            ans.push(-1);\n\
        \        } else {\n            ans.push(num - 1);\n        }\n    }\n    return\
        \ ans;\n};"
      typescript: "function minBitwiseArray(nums: number[]): number[] {\n    let ans:\
        \ number[] = [];\n    for (let num of nums) {\n        if (num % 2 == 0) {\n\
        \            ans.push(-1);\n        } else {\n            ans.push(num - 1);\n\
        \        }\n    }\n    return ans;\n}"
      php: "class Solution {\n    function minBitwiseArray($nums) {\n        $ans =\
        \ [];\n        foreach ($nums as $num) {\n            if ($num % 2 == 0) {\n\
        \                $ans[] = -1;\n            } else {\n                $ans[]\
        \ = $num - 1;\n            }\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func minBitwiseArray(_ nums: [Int]) -> [Int] {\n\
        \        var ans: [Int] = []\n        for num in nums {\n            if num\
        \ % 2 == 0 {\n                ans.append(-1)\n            } else {\n       \
        \         ans.append(num - 1)\n            }\n        }\n        return ans\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minBitwiseArray(nums: List<Int>): IntArray\
        \ {\n        val ans = IntArray(nums.size)\n        for (i in nums.indices)\
        \ {\n            if (nums[i] % 2 == 0) {\n                ans[i] = -1\n    \
        \        } else {\n                ans[i] = nums[i] - 1\n            }\n   \
        \     }\n        return ans\n    }\n}"
      dart: "class Solution {\n  List<int> minBitwiseArray(List<int> nums) {\n    List<int>\
        \ ans = List<int>.filled(nums.length, 0);\n    for (int i = 0; i < nums.length;\
        \ i++) {\n      if (nums[i] % 2 == 0) {\n        ans[i] = -1;\n      } else\
        \ {\n        ans[i] = nums[i] - 1;\n      }\n    }\n    return ans;\n  }\n}"
      go: "func minBitwiseArray(nums []int) []int {\n    ans := make([]int, len(nums))\n\
        \    for i, num := range nums {\n        if num%2 == 0 {\n            ans[i]\
        \ = -1\n        } else {\n            ans[i] = num - 1\n        }\n    }\n \
        \   return ans\n}"
      ruby: "def min_bitwise_array(nums)\n    ans = Array.new(nums.size)\n    nums.each_with_index\
        \ do |num, i|\n        if num % 2 == 0\n            ans[i] = -1\n        else\n\
        \            ans[i] = num - 1\n        end\n    end\n    ans\nend"
      scala: "object Solution {\n    def minBitwiseArray(nums: List[Int]): Array[Int]\
        \ = {\n        val ans = Array.ofDim[Int](nums.size)\n        for (i <- nums.indices)\
        \ {\n            if (nums(i) % 2 == 0) {\n                ans(i) = -1\n    \
        \        } else {\n                ans(i) = nums(i) - 1\n            }\n   \
        \     }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        let mut ans: Vec<i32> = vec![];\n        for num in nums {\n  \
        \          if num % 2 == 0 {\n                ans.push(-1);\n            } else\
        \ {\n                ans.push(num - 1);\n            }\n        }\n        ans\n\
        \    }\n}"
      racket: "(define/contract (min-bitwise-array nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (let loop ([nums nums] [ans '()])\n    (if (null?\
        \ nums)\n        (reverse ans)\n        (let ([num (car nums)])\n          (if\
        \ (even? num)\n              (loop (cdr nums) (cons -1 ans))\n             \
        \ (loop (cdr nums) (cons (- num 1) ans)))))))"
      erlang: "min_bitwise_array(Nums) ->\n    lists:map(fun(N) when N rem 2 == 0 ->\
        \ -1;\n                   (N) -> N - 1 end, Nums)."
      elixir: "defmodule Solution do\n  @spec min_bitwise_array(nums :: [integer]) ::\
        \ [integer]\n  def min_bitwise_array(nums) do\n    Enum.map(nums, fn num when\
        \ rem(num, 2) == 0 -> -1; num -> num - 1 end)\n  end\nend"
    approach: The problem requires constructing an array where each element's bitwise
      OR with its next element equals a given prime number. We can start by checking
      if the given prime number is even, in which case we set the corresponding answer
      to -1 because there's no number that can satisfy the condition. For odd prime
      numbers, we can try unsetting a single bit from the prime number to find the smallest
      possible answer. This approach works because unsetting a bit from an odd number
      will always result in an even number, and the bitwise OR of an even number and
      its next number (which is odd) will be the original odd number.
    time_complexity: The time complexity of this solution is O(n), where n is the number
      of elements in the input array. This is because we are iterating over the input
      array once and performing a constant amount of work for each element.
    space_complexity: The space complexity of this solution is O(n), where n is the
      number of elements in the input array. This is because we are creating an output
      array of the same size as the input array.
    elapsed_time: 5.3005530834198
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-21 01:16:59 '
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
  <small class="solution-timestamp">(2026-01-21 01:16:48 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires finding the minimum `ans[i]` such that `ans[i] OR (ans[i] + 1) == nums[i]`. We first analyze the bitwise OR operation `x OR (x + 1)`. If `x` is an even number, its binary representation ends in `0`, so `x = ...0`. Then `x + 1 = ...1`. The bitwise OR `x OR (x + 1)` will be `...1`, which is always an odd number. Therefore, if `nums[i]` is an even number, it's impossible to satisfy the condition, and `ans[i]` must be -1. This covers the case `nums[i] = 2` (the only even prime).

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
  "approach": "The core of this problem lies in understanding the bitwise OR operation `x OR (x + 1)`. Let's analyze the binary representation of `x` and `x+1`. If `x` is an even number, its least significant bit (LSB) is 0, so `x = ...0_2`. Then `x+1 = ...1_2`. In this case, `x OR (x+1) = (...0_2) OR (...1_2) = ...1_2 = x+1`. This means if `ans[i]` is even, `ans[i] OR (ans[i]+1)` will be `ans[i]+1`, which must be an odd number. Therefore, if `nums[i]` is even, no such `ans[i]` exists, and we should set `ans[i] = -1`. Since `nums[i]` are prime numbers, the only even prime is 2. So for `nums[i] = 2`, `ans[i]` must be -1. For all other prime numbers, `nums[i]` is odd.",
  "time_complexity": "The time complexity is O(N) where N is the length of the input array `nums`. For each number in `nums`, we perform a constant number of bitwise operations (finding the rightmost zero bit, shifting, and ORing). These operations take logarithmic time with respect to the value of `nums[i]`, but since `nums[i]` is bounded by 10^9 (which fits in a 32-bit integer), this is effectively a constant number of operations per element.",
  "space_complexity": "The space complexity is O(N) to store the result array `ans`. If we were allowed to modify the input array in place, the space complexity would be O(1) (excluding the input/output storage).",
  "solutions": {
    "cpp": "class Solution {\npublic:\n    std::vector<int> minBitwiseArray(std::vector<int>& nums) {\n        std::vector<int> ans;\n        for (int num : nums) {\n            if (num % 2 == 0) { // If num is even, ans[i] OR (ans[i]+1) can only be odd if ans[i] is even, or odd if ans[i] is odd. If ans[i] is even, result is ans[i]+1 (odd). If ans[i] is odd, result is (ans[i] | (ans[i]+1)) which is always odd. So an even num[i] cannot be formed.\n                ans.push_back(-1);\n            } else {\n                // num is odd. We need ans | (ans+1) = num.\n                // Let ans = P01...1 (binary, k ones at the end)\n                // Then ans+1 = P10...0 (binary, k zeros at the end)\n                // ans | (ans+1) = P11...1 (binary, k+1 ones at the end)\n                // This means num must be of the form P11...1\n                // To minimize ans, we want to maximize the number of trailing ones in ans.\n                // This means we want to find the smallest k such that num has a 0 at bit k and all bits 0 to k-1 are 1.\n                // If num = P11...1, then ans = P01...1\n                // This is equivalent to ans = num ^ (1 << k) where k is the position of the rightmost 1 in num's complement (num ^ (num+1)).\n                // Or, more simply, ans = num - (num & (num-1)) - 1. No, this is not right.\n                // The pattern is: if num = X11...1 (k ones), then ans = X01...1 (k ones).\n                // This means ans = num - (1 << k) where k is the position of the rightmost 1 in num.\n                // No, this is also not right. Example: num = 7 (111_2). ans = 3 (011_2). k=2 (position of MSB of 3). ans = 7 - (1<<2) = 3.\n                // Example: num = 5 (101_2). ans = 4 (100_2). k=0 (position of LSB of 5). ans = 5 - (1<<0) = 4.\n                // Example: num = 3 (011_2). ans = 1 (001_2). k=1 (position of LSB of 3). ans = 3 - (1<<1) = 1.\n                // The pattern is: ans = num - (1 << (rightmost_zero_bit_position_in_ans)).\n                // Let's find the position of the rightmost 0 bit in `num`.\n                // If `num` is `...X11...1` (k ones), then `ans` is `...X01...1` (k ones).\n                // `ans = num - (1 << k)` where `k` is the position of the rightmost 1 in `num`.\n                // This is equivalent to `ans = num ^ (num & (num-1))` then `ans = num - (ans & -ans)`.\n                // The hint says \"Try unsetting a single bit from nums[i]\".\n                // If ans | (ans+1) = num, then num must have all bits set that are set in ans AND all bits set that are set in ans+1.\n                // Also, since ans < ans+1, the most significant bit of ans and ans+1 are usually the same, or ans+1 has one more bit.\n                // The key property of x | (x+1) is that it sets all trailing zeros of x to one.\n                // E.g., x = 4 (100_2), x+1 = 5 (101_2), x | (x+1) = 101_2 = 5.\n                // E.g., x = 6 (110_2), x+1 = 7 (111_2), x | (x+1) = 111_2 = 7.\n                // E.g., x = 1 (001_2), x+1 = 2 (010_2), x | (x+1) = 011_2 = 3.\n                // E.g., x = 3 (011_2), x+1 = 4 (100_2), x | (x+1) = 111_2 = 7.\n                // The result `num` will always be of the form `...11...1` (all ones from LSB up to some point).\n                // Specifically, `num` will be `(x | (x+1))`. The bits of `x` and `x+1` are identical until the rightmost `0` bit of `x`.\n                // Let `x = A01...1` (where `k` ones follow the `0`).\n                // Then `x+1 = A10...0` (where `k` zeros follow the `1`).\n                // `x | (x+1) = A11...1` (where `k+1` ones follow the `A`).\n                // So, `num` must be of the form `A11...1`.\n                // To find the minimum `ans`, we need to find the largest `k` such that `num` has `k` trailing ones, and the `k+1`-th bit is `0` in `ans`.\n                // This means `ans` should be `num` with its rightmost `1` bit unset.\n                // The rightmost `1` bit of `num` is `num & (-num)` (using two's complement).\n                // So, `ans = num - (num & (-num))`.\n                // Let's test this:\n                // num = 3 (011_2). -3 is (111...1101_2). 3 & (-3) = 1 (001_2). ans = 3 - 1 = 2. But example says 1.\n                // This logic is flawed.\n\n                // Let's re-evaluate the property: `x OR (x+1)`. The bits of `x` and `x+1` are identical until the rightmost `0` bit of `x`. Let this position be `k`.\n                // So `x = (prefix)0(1...1)_2` where `k` ones follow the `0` bit.\n                // `x+1 = (prefix)1(0...0)_2` where `k` zeros follow the `1` bit.\n                // `x OR (x+1) = (prefix)1(1...1)_2` where `k` ones follow the `1` bit.\n                // This means `num` must be of the form `(prefix)11...1` (k+1 ones).\n                // To minimize `ans`, we need to find the largest `k` such that `num` has `k+1` trailing ones.\n                // This means `num` must be `(some_value) * 2^(k+1) - 1` for some `k`.\n                // Example: num = 3 (011_2). Here k+1 = 2. So k=1. ans = 1 (001_2). This is `num` with the bit at position `k+1` (2) unset, and all bits below it `0`.\n                // This is `num - (1 << (k+1)) + ( (1 << k) - 1 )`.\n                // This is `num - (1 << (k+1)) + ( (1 << (k+1)) / 2 - 1 )`.\n                // This is `num - (1 << k)`. No, this is not right.\n\n                // Let's use the hint: \"Try unsetting a single bit from nums[i]\".\n                // If `ans = nums[i] ^ (1 << k)` for some `k`.\n                // We want `ans | (ans+1) == nums[i]`.\n                // Consider `nums[i]`. It's odd. So its LSB is 1.\n                // If `ans` is `nums[i] - (1 << k)` for some `k`.\n                // We need `ans` to be `...01...1` and `ans+1` to be `...10...0` such that their OR is `nums[i]`.\n                // This means `nums[i]` must be `...11...1`.\n                // The value `ans` must be `nums[i]` with its rightmost `1` bit unset, and then all bits below that position set to `1`.\n                // For example, `nums[i] = 7 (111_2)`. Rightmost `1` is at position 0. Unsetting it gives `6 (110_2)`. This is not `ans=3`.\n                // The correct logic is: `ans` must be `
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
            val nVal = nums[i]
            if (nVal % 2 == 0) {
                ans[i] = -1
            } else {
                // Candidate 1: x = N-1. This is always valid if N is odd.
                // (N-1) is even, so (N-1) OR N = N.
                var currentMinX = nVal - 1

                // Candidate 2: x = N - (1 << p) for some p >= 1.
                // This is valid if N has its p-th bit set, AND
                // the lower p bits of N are all 1s. In this case,
                // N's binary form is (prefix)1(1...1) (p ones),
                // and x = (prefix)0(1...1) (p ones).
                // Then x+1 = (prefix)1(0...0) (p zeros),
                // and x OR (x+1) = (prefix)1(1...1) which equals N.
                // We iterate p from 1 up to 30 (since N <= 10^9 < 2^30).
                for (p in 1..30) {
                    // Check if p-th bit of N is set
                    if ((nVal shr p) and 1 == 1) {
                        // Check if lower p bits of N are all 1s
                        val mask = (1 shl p) - 1
                        if ((nVal and mask) == mask) {
                            val candidateX = nVal - (1 shl p)
                            currentMinX = Math.min(currentMinX, candidateX)
                        }
                    }
                }
                ans[i] = currentMinX
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
    List<int> ans = [];
    for (int nVal in nums) {
      if (nVal % 2 == 0) {
        ans.add(-1);
      } else {
        // Candidate 1: x = N-1. This is always valid if N is odd.
        // (N-1) is even, so (N-1) OR N = N.
        int currentMinX = nVal - 1;

        // Candidate 2: x = N - (1 << p) for some p >= 1.
        // This is valid if N has its p-th bit set, AND
        // the lower p bits of N are all 1s.
        // We iterate p from 1 up to 30 (since N <= 10^9 < 2^30).
        for (int p = 1; p <= 30; p++) {
          // Check if p-th bit of N is set
          if (((nVal >> p) & 1) == 1) {
            // Check if lower p bits of N are all 1s
            int mask = (1 << p) - 1;
            if ((nVal & mask) == mask) {
              int candidateX = nVal - (1 << p);
              currentMinX = currentMinX < candidateX ? currentMinX : candidateX;
            }
          }
        }
        ans.add(currentMinX);
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
    for i, nVal := range nums {
        if nVal % 2 == 0 {
            ans[i] = -1
        } else {
            // Candidate 1: x = N-1. This is always valid if N is odd.
            // (N-1) is even, so (N-1) OR N = N.
            currentMinX := nVal - 1

            // Candidate 2: x = N - (1 << p) for some p >= 1.
            // This is valid if N has its p-th bit set, AND
            // the lower p bits of N are all 1s.
            // We iterate p from 1 up to 30 (since N <= 10^9 < 2^30).
            for p := 1; p <= 30; p++ {
                // Check if p-th bit of N is set
                if ((nVal >> p) & 1) == 1 {
                    // Check if lower p bits of N are all 1s
                    mask := (1 << p) - 1
                    if (nVal & mask) == mask {
                        candidateX := nVal - (1 << p)
                        if candidateX < currentMinX {
                            currentMinX = candidateX
                        }
                    }
                }
            }
            ans[i] = currentMinX
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
    nums.each do |n_val|
        if n_val % 2 == 0
            ans << -1
        else
            # Candidate 1: x = N-1. This is always valid if N is odd.
            # (N-1) is even, so (N-1) OR N = N.
            current_min_x = n_val - 1

            # Candidate 2: x = N - (1 << p) for some p >= 1.
            # This is valid if N has its p-th bit set, AND
            # the lower p bits of N are all 1s.
            # We iterate p from 1 up to 30 (since N <= 10^9 < 2^30).
            (1..30).each do |p|
                # Check if p-th bit of N is set
                if ((n_val >> p) & 1) == 1
                    # Check if lower p bits of N are all 1s
                    mask = (1 << p) - 1
                    if (n_val & mask) == mask
                        candidate_x = n_val - (1 << p)
                        current_min_x = [current_min_x, candidate_x].min
                    end
                end
            end
            ans << current_min_x
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
            val nVal = nums(i)
            if (nVal % 2 == 0) {
                ans(i) = -1
            } else {
                // Candidate 1: x = N-1. This is always valid if N is odd.
                // (N-1) is even, so (N-1) OR N = N.
                var currentMinX = nVal - 1

                // Candidate 2: x = N - (1 << p) for some p >= 1.
                // This is valid if N has its p-th bit set, AND
                // the lower p bits of N are all 1s.
                // We iterate p from 1 up to 30 (since N <= 10^9 < 2^30).
                for (p <- 1 to 30) {
                    // Check if p-th bit of N is set
                    if (((nVal >> p) & 1) == 1) {
                        // Check if lower p bits of N are all 1s
                        val mask = (1 << p) - 1
                        if ((nVal & mask) == mask) {
                            val candidateX = nVal - (1 << p)
                            currentMinX = Math.min(currentMinX, candidateX)
                        }
                    }
                }
                ans(i) = currentMinX
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
        for n_val in nums {
            if n_val % 2 == 0 {
                ans.push(-1);
            } else {
                // Candidate 1: x = N-1. This is always valid if N is odd.
                // (N-1) is even, so (N-1) OR N = N.
                let mut current_min_x = n_val - 1;

                // Candidate 2: x = N - (1 << p) for some p >= 1.
                // This is valid if N has its p-th bit set, AND
                // the lower p bits of N are all 1s.
                // We iterate p from 1 up to 30 (since N <= 10^9 < 2^30).
                for p in 1..=30 {
                    // Check if p-th bit of N is set
                    if ((n_val >> p) & 1) == 1 {
                        // Check if lower p bits of N are all 1s
                        let mask = (1 << p) - 1;
                        if (n_val & mask) == mask {
                            let candidate_x = n_val - (1 << p);
                            current_min_x = current_min_x.min(candidate_x);
                        }
                    }
                }
                ans.push(current_min_x);
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
  (for/list ([n-val nums])
    (if (even? n-val)
        -1
        (let loop ([p 1]
                   [current-min-x (- n-val 1)]) ; Candidate 1: N-1
          (if (> p 30)
              current-min-x
              (let* ([p-bit-set? (= (bitwise-and (bitwise-rshift n-val p) 1) 1)]
                     [mask (- (bitwise-lshift 1 p) 1)]
                     [lower-bits-all-ones? (= (bitwise-and n-val mask) mask)])
                (if (and p-bit-set? lower-bits-all-ones?)
                    (let ([candidate-x (- n-val (bitwise-lshift 1 p))])
                      (loop (+ p 1) (min current-min-x candidate-x)))
                    (loop (+ p 1) current-min-x))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_bitwise_array(Nums :: [integer()]) -> [integer()].
min_bitwise_array(Nums) ->
lists:map(fun(NVal) ->
if
NVal rem 2 == 0 ->
-1;
true ->
% Candidate 1: x = N-1. This is always valid if N is odd.
% (N-1) is even, so (N-1) bor N = N.
CurrentMinX = NVal - 1,
% Candidate 2: x = N - (1 bsl P) for some P >= 1.
% This is valid if N has its P-th bit set, AND
% the lower P bits of N are all 1s.
% We iterate P from 1 up to 30 (since N =< 10^9 < 2^30).
min_bitwise_array_loop(1, 30, NVal, CurrentMinX)
end
end, Nums).

min_bitwise_array_loop(P, MaxP, NVal, AccMinX) when P =< MaxP ->
% Check if P-th bit of N is set
PBitSet = ((NVal bsr P) band 1) == 1,
% Check if lower P bits of N are all 1s
Mask = (1 bsl P) - 1,
LowerBitsAllOnes = (NVal band Mask) == Mask,

NewAccMinX = if
PBitSet and LowerBitsAllOnes ->
CandidateX = NVal - (1 bsl P),
min(AccMinX, CandidateX);
true ->
AccMinX
end,
min_bitwise_array_loop(P + 1, MaxP, NVal, NewAccMinX);
min_bitwise_array_loop(_P, _MaxP, _NVal, AccMinX) ->
AccMinX.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn n_val ->
      if rem(n_val, 2) == 0 do
        -1
      else
        # Candidate 1: x = N-1. This is always valid if N is odd.
        # (N-1) is even, so (N-1) ||| N = N.
        current_min_x = n_val - 1

        # Candidate 2: x = N - (1 <<< p) for some p >= 1.
        # This is valid if N has its p-th bit set, AND
        # the lower p bits of N are all 1s.
        # We iterate p from 1 up to 30 (since N <= 10^9 < 2^30).
        Enum.reduce(1..30, current_min_x, fn p, acc_min_x ->
          # Check if p-th bit of N is set
          p_bit_set = (((n_val >>> p) &&& 1) == 1)
          # Check if lower p bits of N are all 1s
          mask = (1 <<< p) - 1
          lower_bits_all_ones = ((n_val &&& mask) == mask)

          if p_bit_set and lower_bits_all_ones do
            candidate_x = n_val - (1 <<< p)
            min(acc_min_x, candidate_x)
          else
            acc_min_x
          end
        end)
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N * log(max_val)) where N is the length of the `nums` array and `max_val` is the maximum value in `nums`. For each number in `nums`, we perform a constant number of bitwise operations and a loop that iterates up to `log2(max_val)` times (approximately 30 for 10^9). Thus, the total time complexity is proportional to `nums.length` multiplied by a small constant factor.

- **Space Complexity:** The space complexity is O(N) where N is the length of the `nums` array. This is due to storing the `ans` array, which has the same length as the input `nums` array.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-21 01:16:59 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires constructing an array where each element's bitwise OR with its next element equals a given prime number. We can start by checking if the given prime number is even, in which case we set the corresponding answer to -1 because there's no number that can satisfy the condition. For odd prime numbers, we can try unsetting a single bit from the prime number to find the smallest possible answer. This approach works because unsetting a bit from an odd number will always result in an even number, and the bitwise OR of an even number and its next number (which is odd) will be the original odd number.

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
            if (num % 2 == 0) {
                ans.push_back(-1);
            } else {
                ans.push_back(num - 1);
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
            if (num % 2 == 0) {
                ans[i] = -1;
            } else {
                ans[i] = num - 1;
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
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                ans.append(num - 1)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                ans.append(num - 1)
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
        if (nums[i] % 2 == 0) {
            ans[i] = -1;
        } else {
            ans[i] = nums[i] - 1;
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
            if (num % 2 == 0) {
                ans[i] = -1;
            } else {
                ans[i] = num - 1;
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
        if (num % 2 == 0) {
            ans.push(-1);
        } else {
            ans.push(num - 1);
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
        if (num % 2 == 0) {
            ans.push(-1);
        } else {
            ans.push(num - 1);
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
            if ($num % 2 == 0) {
                $ans[] = -1;
            } else {
                $ans[] = $num - 1;
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
            if num % 2 == 0 {
                ans.append(-1)
            } else {
                ans.append(num - 1)
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
        val ans = IntArray(nums.size)
        for (i in nums.indices) {
            if (nums[i] % 2 == 0) {
                ans[i] = -1
            } else {
                ans[i] = nums[i] - 1
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
    List<int> ans = List<int>.filled(nums.length, 0);
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] % 2 == 0) {
        ans[i] = -1;
      } else {
        ans[i] = nums[i] - 1;
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
            ans[i] = num - 1
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
def min_bitwise_array(nums)
    ans = Array.new(nums.size)
    nums.each_with_index do |num, i|
        if num % 2 == 0
            ans[i] = -1
        else
            ans[i] = num - 1
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
        val ans = Array.ofDim[Int](nums.size)
        for (i <- nums.indices) {
            if (nums(i) % 2 == 0) {
                ans(i) = -1
            } else {
                ans(i) = nums(i) - 1
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
        let mut ans: Vec<i32> = vec![];
        for num in nums {
            if num % 2 == 0 {
                ans.push(-1);
            } else {
                ans.push(num - 1);
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
  (let loop ([nums nums] [ans '()])
    (if (null? nums)
        (reverse ans)
        (let ([num (car nums)])
          (if (even? num)
              (loop (cdr nums) (cons -1 ans))
              (loop (cdr nums) (cons (- num 1) ans)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
min_bitwise_array(Nums) ->
    lists:map(fun(N) when N rem 2 == 0 -> -1;
                   (N) -> N - 1 end, Nums).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_bitwise_array(nums :: [integer]) :: [integer]
  def min_bitwise_array(nums) do
    Enum.map(nums, fn num when rem(num, 2) == 0 -> -1; num -> num - 1 end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n), where n is the number of elements in the input array. This is because we are iterating over the input array once and performing a constant amount of work for each element.

- **Space Complexity:** The space complexity of this solution is O(n), where n is the number of elements in the input array. This is because we are creating an output array of the same size as the input array.

</div>
</details>
