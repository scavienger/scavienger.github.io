---
layout: post
title: "Minimum Moves to Make Array Complementary"
date: 2026-05-13 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nclass Solution {\npublic:\n \
        \   int minMoves(std::vector<int>& nums, int limit) {\n        int n = nums.size();\n\
        \        std::vector<int> diff(2 * limit + 2, 0);\n        for (int i = 0; i\
        \ < n / 2; ++i) {\n            int a = nums[i];\n            int b = nums[n\
        \ - 1 - i];\n            int min_v = std::min(a, b);\n            int max_v\
        \ = std::max(a, b);\n\n            diff[2] += 2;\n            diff[min_v + 1]\
        \ -= 1;\n            diff[a + b] -= 1;\n            diff[a + b + 1] += 1;\n\
        \            diff[max_v + limit + 1] += 1;\n        }\n\n        int res = n;\n\
        \        int curr = 0;\n        for (int x = 2; x <= 2 * limit; ++x) {\n   \
        \         curr += diff[x];\n            if (curr < res) {\n                res\
        \ = curr;\n            }\n        }\n        return res;\n    }\n};"
      java: "class Solution {\n    public int minMoves(int[] nums, int limit) {\n  \
        \      int n = nums.length;\n        int[] diff = new int[2 * limit + 2];\n\
        \        for (int i = 0; i < n / 2; i++) {\n            int a = nums[i];\n \
        \           int b = nums[n - 1 - i];\n            int minV = Math.min(a, b);\n\
        \            int maxV = Math.max(a, b);\n\n            diff[2] += 2;\n     \
        \       diff[minV + 1] -= 1;\n            diff[a + b] -= 1;\n            diff[a\
        \ + b + 1] += 1;\n            diff[maxV + limit + 1] += 1;\n        }\n\n  \
        \      int res = n;\n        int curr = 0;\n        for (int x = 2; x <= 2 *\
        \ limit; x++) {\n            curr += diff[x];\n            if (curr < res) {\n\
        \                res = curr;\n            }\n        }\n        return res;\n\
        \    }\n}"
      python: "class Solution(object):\n    def minMoves(self, nums, limit):\n     \
        \   \"\"\"\n        :type nums: List[int]\n        :type limit: int\n      \
        \  :rtype: int\n        \"\"\"\n        n = len(nums)\n        diff = [0] *\
        \ (2 * limit + 2)\n        for i in range(n // 2):\n            a, b = nums[i],\
        \ nums[n - 1 - i]\n            min_v, max_v = min(a, b), max(a, b)\n\n     \
        \       diff[2] += 2\n            diff[min_v + 1] -= 1\n            diff[a +\
        \ b] -= 1\n            diff[a + b + 1] += 1\n            diff[max_v + limit\
        \ + 1] += 1\n\n        res = n\n        curr = 0\n        for x in range(2,\
        \ 2 * limit + 1):\n            curr += diff[x]\n            if curr < res:\n\
        \                res = curr\n        return res"
      python3: "class Solution:\n    def minMoves(self, nums: List[int], limit: int)\
        \ -> int:\n        n = len(nums)\n        diff = [0] * (2 * limit + 2)\n   \
        \     for i in range(n // 2):\n            a, b = nums[i], nums[n - 1 - i]\n\
        \            min_v, max_v = min(a, b), max(a, b)\n\n            diff[2] += 2\n\
        \            diff[min_v + 1] -= 1\n            diff[a + b] -= 1\n          \
        \  diff[a + b + 1] += 1\n            diff[max_v + limit + 1] += 1\n\n      \
        \  res = n\n        curr = 0\n        for x in range(2, 2 * limit + 1):\n  \
        \          curr += diff[x]\n            if curr < res:\n                res\
        \ = curr\n        return res"
      c: "#include <stdlib.h>\n\nint minMoves(int* nums, int numsSize, int limit) {\n\
        \    int* diff = (int*)calloc(2 * limit + 2, sizeof(int));\n    if (diff ==\
        \ NULL) return 0;\n\n    for (int i = 0; i < numsSize / 2; i++) {\n        int\
        \ a = nums[i];\n        int b = nums[numsSize - 1 - i];\n        int min_v =\
        \ (a < b) ? a : b;\n        int max_v = (a > b) ? a : b;\n\n        diff[2]\
        \ += 2;\n        diff[min_v + 1] -= 1;\n        diff[a + b] -= 1;\n        diff[a\
        \ + b + 1] += 1;\n        diff[max_v + limit + 1] += 1;\n    }\n\n    int res\
        \ = numsSize;\n    int curr = 0;\n    for (int x = 2; x <= 2 * limit; x++) {\n\
        \        curr += diff[x];\n        if (curr < res) {\n            res = curr;\n\
        \        }\n    }\n\n    free(diff);\n    return res;\n}"
      csharp: "public class Solution {\n    public int MinMoves(int[] nums, int limit)\
        \ {\n        int n = nums.Length;\n        int[] diff = new int[2 * limit +\
        \ 2];\n\n        for (int i = 0; i < n / 2; i++) {\n            int a = nums[i];\n\
        \            int b = nums[n - 1 - i];\n            int minVal = Math.Min(a,\
        \ b);\n            int maxVal = Math.Max(a, b);\n\n            // Case 1: 2\
        \ moves for every sum between 2 and 2 * limit\n            diff[2] += 2;\n \
        \           diff[2 * limit + 1] -= 2;\n\n            // Case 2: 1 move instead\
        \ of 2 for sums in [min(a, b) + 1, max(a, b) + limit]\n            diff[minVal\
        \ + 1] -= 1;\n            diff[maxVal + limit + 1] += 1;\n\n            // Case\
        \ 3: 0 moves instead of 1 for the exact current sum a + b\n            diff[a\
        \ + b] -= 1;\n            diff[a + b + 1] += 1;\n        }\n\n        int res\
        \ = n;\n        int currentMoves = 0;\n        for (int x = 2; x <= 2 * limit;\
        \ x++) {\n            currentMoves += diff[x];\n            if (currentMoves\
        \ < res) {\n                res = currentMoves;\n            }\n        }\n\n\
        \        return res;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} limit\n * @return\
        \ {number}\n */\nvar minMoves = function(nums, limit) {\n    const n = nums.length;\n\
        \    const diff = new Int32Array(2 * limit + 2);\n\n    for (let i = 0; i <\
        \ n / 2; i++) {\n        const a = nums[i];\n        const b = nums[n - 1 -\
        \ i];\n        const minVal = Math.min(a, b);\n        const maxVal = Math.max(a,\
        \ b);\n\n        // Default: 2 moves for all target sums\n        diff[2] +=\
        \ 2;\n        diff[2 * limit + 1] -= 2;\n\n        // Range [min+1, max+limit]\
        \ can be done in 1 move\n        diff[minVal + 1] -= 1;\n        diff[maxVal\
        \ + limit + 1] += 1;\n\n        // Target sum a+b can be done in 0 moves\n \
        \       diff[a + b] -= 1;\n        diff[a + b + 1] += 1;\n    }\n\n    let res\
        \ = n;\n    let currentMoves = 0;\n    for (let x = 2; x <= 2 * limit; x++)\
        \ {\n        currentMoves += diff[x];\n        if (currentMoves < res) {\n \
        \           res = currentMoves;\n        }\n    }\n\n    return res;\n};"
      typescript: "function minMoves(nums: number[], limit: number): number {\n    const\
        \ n = nums.length;\n    const diff = new Int32Array(2 * limit + 2);\n\n    for\
        \ (let i = 0; i < n / 2; i++) {\n        const a = nums[i];\n        const b\
        \ = nums[n - 1 - i];\n        const minVal = Math.min(a, b);\n        const\
        \ maxVal = Math.max(a, b);\n\n        // Default: 2 moves for all target sums\n\
        \        diff[2] += 2;\n        diff[2 * limit + 1] -= 2;\n\n        // Range\
        \ [min+1, max+limit] can be done in 1 move\n        diff[minVal + 1] -= 1;\n\
        \        diff[maxVal + limit + 1] += 1;\n\n        // Target sum a+b can be\
        \ done in 0 moves\n        diff[a + b] -= 1;\n        diff[a + b + 1] += 1;\n\
        \    }\n\n    let res = n;\n    let currentMoves = 0;\n    for (let x = 2; x\
        \ <= 2 * limit; x++) {\n        currentMoves += diff[x];\n        if (currentMoves\
        \ < res) {\n            res = currentMoves;\n        }\n    }\n\n    return\
        \ res;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $limit\n     * @return Integer\n     */\n    function minMoves($nums,\
        \ $limit) {\n        $n = count($nums);\n        $diff = array_fill(0, 2 * $limit\
        \ + 2, 0);\n\n        for ($i = 0; $i < $n / 2; $i++) {\n            $a = $nums[$i];\n\
        \            $b = $nums[$n - 1 - $i];\n            $minVal = min($a, $b);\n\
        \            $maxVal = max($a, $b);\n\n            // Initial assumption: 2\
        \ moves for any target sum X in [2, 2 * limit]\n            $diff[2] += 2;\n\
        \            $diff[2 * $limit + 1] -= 2;\n\n            // Correct to 1 move\
        \ for target sum in [min+1, max+limit]\n            $diff[$minVal + 1] -= 1;\n\
        \            $diff[$maxVal + $limit + 1] += 1;\n\n            // Correct to\
        \ 0 moves for target sum exactly equal to a + b\n            $diff[$a + $b]\
        \ -= 1;\n            $diff[$a + $b + 1] += 1;\n        }\n\n        $res = $n;\n\
        \        $currentMoves = 0;\n        for ($x = 2; $x <= 2 * $limit; $x++) {\n\
        \            $currentMoves += $diff[$x];\n            if ($currentMoves < $res)\
        \ {\n                $res = $currentMoves;\n            }\n        }\n\n   \
        \     return $res;\n    }\n}"
      swift: "class Solution {\n    func minMoves(_ nums: [Int], _ limit: Int) -> Int\
        \ {\n        let n = nums.count\n        var diff = [Int](repeating: 0, count:\
        \ 2 * limit + 2)\n\n        for i in 0..<(n / 2) {\n            let a = nums[i]\n\
        \            let b = nums[n - 1 - i]\n            let minVal = min(a, b)\n \
        \           let maxVal = max(a, b)\n\n            // All target sums in [2,\
        \ 2*limit] initially require 2 moves per pair\n            diff[2] += 2\n  \
        \          diff[2 * limit + 1] -= 2\n\n            // Target sums in [min+1,\
        \ max+limit] require only 1 move\n            diff[minVal + 1] -= 1\n      \
        \      diff[maxVal + limit + 1] += 1\n\n            // Target sum equal to a+b\
        \ requires 0 moves\n            diff[a + b] -= 1\n            diff[a + b + 1]\
        \ += 1\n        }\n\n        var res = n\n        var currentMoves = 0\n   \
        \     for x in 2...(2 * limit) {\n            currentMoves += diff[x]\n    \
        \        if currentMoves < res {\n                res = currentMoves\n     \
        \       }\n        }\n\n        return res\n    }\n}"
      kotlin: "import kotlin.math.*\n\nclass Solution {\n    fun minMoves(nums: IntArray,\
        \ limit: Int): Int {\n        val n = nums.size\n        val diff = IntArray(2\
        \ * limit + 2)\n        for (i in 0 until n / 2) {\n            val a = nums[i]\n\
        \            val b = nums[n - 1 - i]\n            val minV = min(a, b)\n   \
        \         val maxV = max(a, b)\n\n            // For each pair, baseline moves\
        \ for all target sums is 2\n            // Range [minV + 1, maxV + limit] requires\
        \ only 1 move\n            // Target sum T = a + b requires 0 moves\n\n    \
        \        diff[minV + 1] -= 1\n            diff[maxV + limit + 1] += 1\n    \
        \        diff[a + b] -= 1\n            diff[a + b + 1] += 1\n        }\n\n \
        \       var minAns = n\n        var currentMoves = n\n        for (i in 2..2\
        \ * limit) {\n            currentMoves += diff[i]\n            minAns = min(minAns,\
        \ currentMoves)\n        }\n        return minAns\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minMoves(List<int> nums,\
        \ int limit) {\n    int n = nums.length;\n    List<int> diff = List<int>.filled(2\
        \ * limit + 2, 0);\n\n    for (int i = 0; i < n ~/ 2; i++) {\n      int a =\
        \ nums[i];\n      int b = nums[n - 1 - i];\n      int minV = min(a, b);\n  \
        \    int maxV = max(a, b);\n\n      diff[minV + 1] -= 1;\n      diff[maxV +\
        \ limit + 1] += 1;\n      diff[a + b] -= 1;\n      diff[a + b + 1] += 1;\n \
        \   }\n\n    int minAns = n;\n    int currentMoves = n;\n    for (int i = 2;\
        \ i <= 2 * limit; i++) {\n      currentMoves += diff[i];\n      minAns = min(minAns,\
        \ currentMoves);\n    }\n    return minAns;\n  }\n}"
      go: "func minMoves(nums []int, limit int) int {\n    n := len(nums)\n    diff\
        \ := make([]int, 2*limit+2)\n\n    for i := 0; i < n/2; i++ {\n        a, b\
        \ := nums[i], nums[n-1-i]\n        minV, maxV := a, b\n        if b < a {\n\
        \            minV, maxV = b, a\n        }\n\n        diff[minV+1]--\n      \
        \  diff[maxV+limit+1]++\n        diff[a+b]--\n        diff[a+b+1]++\n    }\n\
        \n    minAns := n\n    currentMoves := n\n    for i := 2; i <= 2*limit; i++\
        \ {\n        currentMoves += diff[i]\n        if currentMoves < minAns {\n \
        \           minAns = currentMoves\n        }\n    }\n    return minAns\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} limit\n# @return {Integer}\n\
        def min_moves(nums, limit)\n    n = nums.length\n    diff = Array.new(2 * limit\
        \ + 2, 0)\n\n    (0...n/2).each do |i|\n        a = nums[i]\n        b = nums[n\
        \ - 1 - i]\n        min_v = a < b ? a : b\n        max_v = a > b ? a : b\n\n\
        \        diff[min_v + 1] -= 1\n        diff[max_v + limit + 1] += 1\n      \
        \  diff[a + b] -= 1\n        diff[a + b + 1] += 1\n    end\n\n    min_ans =\
        \ n\n    current_moves = n\n    (2..2*limit).each do |i|\n        current_moves\
        \ += diff[i]\n        min_ans = current_moves if current_moves < min_ans\n \
        \   end\n    min_ans\nend"
      scala: "import scala.math._\n\nobject Solution {\n    def minMoves(nums: Array[Int],\
        \ limit: Int): Int = {\n        val n = nums.length\n        val diff = new\
        \ Array[Int](2 * limit + 2)\n\n        var i = 0\n        while (i < n / 2)\
        \ {\n            val a = nums(i)\n            val b = nums(n - 1 - i)\n    \
        \        val minV = min(a, b)\n            val maxV = max(a, b)\n\n        \
        \    diff(minV + 1) -= 1\n            diff(maxV + limit + 1) += 1\n        \
        \    diff(a + b) -= 1\n            diff(a + b + 1) += 1\n            i += 1\n\
        \        }\n\n        var minAns = n\n        var currentMoves = n\n       \
        \ var t = 2\n        while (t <= 2 * limit) {\n            currentMoves += diff(t)\n\
        \            if (currentMoves < minAns) {\n                minAns = currentMoves\n\
        \            }\n            t += 1\n        }\n        minAns\n    }\n}"
      rust: "impl Solution {\n    pub fn min_moves(nums: Vec<i32>, limit: i32) -> i32\
        \ {\n        let n = nums.len();\n        let limit = limit as usize;\n    \
        \    let mut diff = vec![0; 2 * limit + 2];\n\n        for i in 0..n / 2 {\n\
        \            let a = nums[i] as usize;\n            let b = nums[n - 1 - i]\
        \ as usize;\n            let min_val = a.min(b);\n            let max_val =\
        \ a.max(b);\n            let sum = a + b;\n\n            // Case for every pair\
        \ (a, b) and target sum x:\n            // - [2, min_val]: 2 moves\n       \
        \     // - [min_val + 1, a + b - 1]: 1 move\n            // - [a + b]: 0 moves\n\
        \            // - [a + b + 1, max_val + limit]: 1 move\n            // - [max_val\
        \ + limit + 1, 2 * limit]: 2 moves\n\n            diff[2] += 2;\n          \
        \  diff[min_val + 1] -= 1;\n            diff[sum] -= 1;\n            diff[sum\
        \ + 1] += 1;\n            if max_val + limit + 1 <= 2 * limit {\n          \
        \      diff[max_val + limit + 1] += 1;\n            }\n        }\n\n       \
        \ let mut min_res = n as i32;\n        let mut curr = 0;\n        for i in 2..=(2\
        \ * limit) {\n            curr += diff[i];\n            if curr < min_res {\n\
        \                min_res = curr;\n            }\n        }\n        min_res\n\
        \    }\n}"
      racket: "(define/contract (min-moves nums limit)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([n (length nums)]\n         [nums-vec\
        \ (list->vector nums)]\n         [diff (make-vector (+ (* 2 limit) 2) 0)]\n\
        \         [half-n (quotient n 2)])\n    (for ([i (in-range half-n)])\n     \
        \ (let* ([a (vector-ref nums-vec i)]\n             [b (vector-ref nums-vec (-\
        \ n 1 i))]\n             [min-val (min a b)]\n             [max-val (max a b)]\n\
        \             [sum (+ a b)])\n        (vector-set! diff 2 (+ (vector-ref diff\
        \ 2) 2))\n        (vector-set! diff (+ min-val 1) (- (vector-ref diff (+ min-val\
        \ 1)) 1))\n        (vector-set! diff sum (- (vector-ref diff sum) 1))\n    \
        \    (vector-set! diff (+ sum 1) (+ (vector-ref diff (+ sum 1)) 1))\n      \
        \  (when (<= (+ max-val limit 1) (* 2 limit))\n          (vector-set! diff (+\
        \ max-val limit 1) (+ (vector-ref diff (+ max-val limit 1)) 1)))))\n    (let-values\
        \ ([(final-min final-curr)\n                  (for/fold ([min-res n]\n     \
        \                        [curr 0])\n                            ([i (in-range\
        \ 2 (+ (* 2 limit) 1))])\n                    (let ([new-curr (+ curr (vector-ref\
        \ diff i))])\n                      (values (min min-res new-curr) new-curr)))])\n\
        \      final-min)))"
      erlang: "-spec min_moves(Nums :: [integer()], Limit :: integer()) -> integer().\n\
        min_moves(Nums, Limit) ->\n    N = length(Nums),\n    NumsVec = list_to_tuple(Nums),\n\
        \    Diff = atomics:new(2 * Limit + 2, [{signed, true}]),\n    lists:foreach(fun(I)\
        \ ->\n        A = element(I + 1, NumsVec),\n        B = element(N - I, NumsVec),\n\
        \        MinVal = erlang:min(A, B),\n        MaxVal = erlang:max(A, B),\n  \
        \      Sum = A + B,\n        atomics:add(Diff, 2, 2),\n        atomics:add(Diff,\
        \ MinVal + 1, -1),\n        atomics:add(Diff, Sum, -1),\n        atomics:add(Diff,\
        \ Sum + 1, 1),\n        if \n            MaxVal + Limit + 1 =< 2 * Limit ->\
        \ atomics:add(Diff, MaxVal + Limit + 1, 1);\n            true -> ok\n      \
        \  end\n    end, lists:seq(0, (N div 2) - 1)),\n    find_min(Diff, 2, 2 * Limit,\
        \ 0, N).\n\nfind_min(Diff, I, Max, Curr, MinRes) when I =< Max ->\n    Val =\
        \ atomics:get(Diff, I),\n    NewCurr = Curr + Val,\n    NewMin = if NewCurr\
        \ < MinRes -> NewCurr; true -> MinRes end,\n    find_min(Diff, I + 1, Max, NewCurr,\
        \ NewMin);\nfind_min(_Diff, _I, _Max, _Curr, MinRes) ->\n    MinRes."
      elixir: "defmodule Solution do\n  @spec min_moves(nums :: [integer], limit ::\
        \ integer) :: integer\n  def min_moves(nums, limit) do\n    n = length(nums)\n\
        \    nums_vec = List.to_tuple(nums)\n    diff = :atomics.new(2 * limit + 2,\
        \ [{:signed, true}])\n    half_n = div(n, 2)\n\n    Enum.each(0..(half_n - 1),\
        \ fn i ->\n      a = elem(nums_vec, i)\n      b = elem(nums_vec, n - 1 - i)\n\
        \      min_val = min(a, b)\n      max_val = max(a, b)\n      sum = a + b\n\n\
        \      :atomics.add(diff, 2, 2)\n      :atomics.add(diff, min_val + 1, -1)\n\
        \      :atomics.add(diff, sum, -1)\n      :atomics.add(diff, sum + 1, 1)\n \
        \     if max_val + limit + 1 <= 2 * limit do\n        :atomics.add(diff, max_val\
        \ + limit + 1, 1)\n      end\n    end)\n\n    find_min(diff, 2, 2 * limit, 0,\
        \ n)\n  end\n\n  defp find_min(diff, i, max_idx, curr, min_res) when i <= max_idx\
        \ do\n    new_curr = curr + :atomics.get(diff, i)\n    new_min = if new_curr\
        \ < min_res, do: new_curr, else: min_res\n    find_min(diff, i + 1, max_idx,\
        \ new_curr, new_min)\n  end\n\n  defp find_min(_diff, _i, _max_idx, _curr, min_res),\
        \ do: min_res\nend"
    approach: 'To solve this problem efficiently, we evaluate the number of modifications
      required for each pair (nums[i], nums[n-1-i]) to achieve a target sum S in the
      range [2, 2 * limit]. For each pair (a, b), the required moves are categorized
      as follows: zero moves if S = a + b; one move if S is within the range [min(a,
      b) + 1, max(a, b) + limit] excluding the specific point where S = a + b; and two
      moves for any other target sum. This range exists because the smallest possible
      sum achievable with one modification is 1 + min(a, b) and the largest is limit
      + max(a, b).


      By leveraging a difference array of size 2 * limit + 2, we can aggregate the move
      counts across all n/2 pairs in linear time. For each pair, we initially assume
      two moves for every possible target sum, then decrement the move count for the
      range requiring only one move, and further decrement it for the specific target
      sum requiring zero moves. After processing all pairs, we perform a linear scan
      using a prefix sum to calculate the total moves for every possible sum and return
      the overall minimum moves found.'
    time_complexity: 'O(n + limit) with one-paragraph explanation: We iterate through
      n/2 pairs of elements in the array to populate the difference array, which takes
      O(n) time. Subsequently, we traverse the difference array of size 2 * limit to
      compute the prefix sums and find the minimum value, which takes O(limit) time.
      Both operations are linear with respect to the input size.'
    space_complexity: 'O(limit) with one-paragraph explanation: The difference array
      used to store the modification counts requires 2 * limit + 2 integers. This space
      usage is proportional to the maximum possible value of the integers in the array
      and is independent of the total number of elements n.'
    elapsed_time: 531.0134761333466
    model: gemini-3-flash-preview
    generated_at: '2026-05-13 02:38:36 '
---

## Problem #1674: Minimum Moves to Make Array Complementary

**Difficulty:** Medium

**Topics:** Array, Hash Table, Prefix Sum

## Problem Description

<p>You are given an integer array <code>nums</code> of <strong>even</strong> length <code>n</code> and an integer <code>limit</code>. In one move, you can replace any integer from <code>nums</code> with another integer between <code>1</code> and <code>limit</code>, inclusive.</p>

<p>The array <code>nums</code> is <strong>complementary</strong> if for all indices <code>i</code> (<strong>0-indexed</strong>), <code>nums[i] + nums[n - 1 - i]</code> equals the same number. For example, the array <code>[1,2,3,4]</code> is complementary because for all indices <code>i</code>, <code>nums[i] + nums[n - 1 - i] = 5</code>.</p>

<p>Return the <em><strong>minimum</strong> number of moves required to make </em><code>nums</code><em> <strong>complementary</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,4,3], limit = 4
<strong>Output:</strong> 1
<strong>Explanation:</strong> In 1 move, you can change nums to [1,2,<u>2</u>,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2,1], limit = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> In 2 moves, you can change nums to [<u>2</u>,2,2,<u>2</u>]. You cannot change any number to 3 since 3 &gt; limit.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,2], limit = 2
<strong>Output:</strong> 0
<strong>Explanation:</strong> nums is already complementary.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n&nbsp;&lt;=&nbsp;10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i]&nbsp;&lt;= limit &lt;=&nbsp;10<sup>5</sup></code></li>
	<li><code>n</code> is even.</li>
</ul>


## Hints

1. Given a target sum x, each pair of nums[i] and nums[n-1-i] would either need 0, 1, or 2 modifications.

2. Can you find the optimal target sum x value such that the sum of modifications is minimized?

3. Create a difference array to efficiently sum all the modifications.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently, we evaluate the number of modifications required for each pair (nums[i], nums[n-1-i]) to achieve a target sum S in the range [2, 2 * limit]. For each pair (a, b), the required moves are categorized as follows: zero moves if S = a + b; one move if S is within the range [min(a, b) + 1, max(a, b) + limit] excluding the specific point where S = a + b; and two moves for any other target sum. This range exists because the smallest possible sum achievable with one modification is 1 + min(a, b) and the largest is limit + max(a, b).

By leveraging a difference array of size 2 * limit + 2, we can aggregate the move counts across all n/2 pairs in linear time. For each pair, we initially assume two moves for every possible target sum, then decrement the move count for the range requiring only one move, and further decrement it for the specific target sum requiring zero moves. After processing all pairs, we perform a linear scan using a prefix sum to calculate the total moves for every possible sum and return the overall minimum moves found.

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

class Solution {
public:
    int minMoves(std::vector<int>& nums, int limit) {
        int n = nums.size();
        std::vector<int> diff(2 * limit + 2, 0);
        for (int i = 0; i < n / 2; ++i) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int min_v = std::min(a, b);
            int max_v = std::max(a, b);

            diff[2] += 2;
            diff[min_v + 1] -= 1;
            diff[a + b] -= 1;
            diff[a + b + 1] += 1;
            diff[max_v + limit + 1] += 1;
        }

        int res = n;
        int curr = 0;
        for (int x = 2; x <= 2 * limit; ++x) {
            curr += diff[x];
            if (curr < res) {
                res = curr;
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
    public int minMoves(int[] nums, int limit) {
        int n = nums.length;
        int[] diff = new int[2 * limit + 2];
        for (int i = 0; i < n / 2; i++) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int minV = Math.min(a, b);
            int maxV = Math.max(a, b);

            diff[2] += 2;
            diff[minV + 1] -= 1;
            diff[a + b] -= 1;
            diff[a + b + 1] += 1;
            diff[maxV + limit + 1] += 1;
        }

        int res = n;
        int curr = 0;
        for (int x = 2; x <= 2 * limit; x++) {
            curr += diff[x];
            if (curr < res) {
                res = curr;
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
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            min_v, max_v = min(a, b), max(a, b)

            diff[2] += 2
            diff[min_v + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[max_v + limit + 1] += 1

        res = n
        curr = 0
        for x in range(2, 2 * limit + 1):
            curr += diff[x]
            if curr < res:
                res = curr
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            min_v, max_v = min(a, b), max(a, b)

            diff[2] += 2
            diff[min_v + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[max_v + limit + 1] += 1

        res = n
        curr = 0
        for x in range(2, 2 * limit + 1):
            curr += diff[x]
            if curr < res:
                res = curr
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int minMoves(int* nums, int numsSize, int limit) {
    int* diff = (int*)calloc(2 * limit + 2, sizeof(int));
    if (diff == NULL) return 0;

    for (int i = 0; i < numsSize / 2; i++) {
        int a = nums[i];
        int b = nums[numsSize - 1 - i];
        int min_v = (a < b) ? a : b;
        int max_v = (a > b) ? a : b;

        diff[2] += 2;
        diff[min_v + 1] -= 1;
        diff[a + b] -= 1;
        diff[a + b + 1] += 1;
        diff[max_v + limit + 1] += 1;
    }

    int res = numsSize;
    int curr = 0;
    for (int x = 2; x <= 2 * limit; x++) {
        curr += diff[x];
        if (curr < res) {
            res = curr;
        }
    }

    free(diff);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinMoves(int[] nums, int limit) {
        int n = nums.Length;
        int[] diff = new int[2 * limit + 2];

        for (int i = 0; i < n / 2; i++) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int minVal = Math.Min(a, b);
            int maxVal = Math.Max(a, b);

            // Case 1: 2 moves for every sum between 2 and 2 * limit
            diff[2] += 2;
            diff[2 * limit + 1] -= 2;

            // Case 2: 1 move instead of 2 for sums in [min(a, b) + 1, max(a, b) + limit]
            diff[minVal + 1] -= 1;
            diff[maxVal + limit + 1] += 1;

            // Case 3: 0 moves instead of 1 for the exact current sum a + b
            diff[a + b] -= 1;
            diff[a + b + 1] += 1;
        }

        int res = n;
        int currentMoves = 0;
        for (int x = 2; x <= 2 * limit; x++) {
            currentMoves += diff[x];
            if (currentMoves < res) {
                res = currentMoves;
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
 * @param {number} limit
 * @return {number}
 */
var minMoves = function(nums, limit) {
    const n = nums.length;
    const diff = new Int32Array(2 * limit + 2);

    for (let i = 0; i < n / 2; i++) {
        const a = nums[i];
        const b = nums[n - 1 - i];
        const minVal = Math.min(a, b);
        const maxVal = Math.max(a, b);

        // Default: 2 moves for all target sums
        diff[2] += 2;
        diff[2 * limit + 1] -= 2;

        // Range [min+1, max+limit] can be done in 1 move
        diff[minVal + 1] -= 1;
        diff[maxVal + limit + 1] += 1;

        // Target sum a+b can be done in 0 moves
        diff[a + b] -= 1;
        diff[a + b + 1] += 1;
    }

    let res = n;
    let currentMoves = 0;
    for (let x = 2; x <= 2 * limit; x++) {
        currentMoves += diff[x];
        if (currentMoves < res) {
            res = currentMoves;
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
function minMoves(nums: number[], limit: number): number {
    const n = nums.length;
    const diff = new Int32Array(2 * limit + 2);

    for (let i = 0; i < n / 2; i++) {
        const a = nums[i];
        const b = nums[n - 1 - i];
        const minVal = Math.min(a, b);
        const maxVal = Math.max(a, b);

        // Default: 2 moves for all target sums
        diff[2] += 2;
        diff[2 * limit + 1] -= 2;

        // Range [min+1, max+limit] can be done in 1 move
        diff[minVal + 1] -= 1;
        diff[maxVal + limit + 1] += 1;

        // Target sum a+b can be done in 0 moves
        diff[a + b] -= 1;
        diff[a + b + 1] += 1;
    }

    let res = n;
    let currentMoves = 0;
    for (let x = 2; x <= 2 * limit; x++) {
        currentMoves += diff[x];
        if (currentMoves < res) {
            res = currentMoves;
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
     * @param Integer $limit
     * @return Integer
     */
    function minMoves($nums, $limit) {
        $n = count($nums);
        $diff = array_fill(0, 2 * $limit + 2, 0);

        for ($i = 0; $i < $n / 2; $i++) {
            $a = $nums[$i];
            $b = $nums[$n - 1 - $i];
            $minVal = min($a, $b);
            $maxVal = max($a, $b);

            // Initial assumption: 2 moves for any target sum X in [2, 2 * limit]
            $diff[2] += 2;
            $diff[2 * $limit + 1] -= 2;

            // Correct to 1 move for target sum in [min+1, max+limit]
            $diff[$minVal + 1] -= 1;
            $diff[$maxVal + $limit + 1] += 1;

            // Correct to 0 moves for target sum exactly equal to a + b
            $diff[$a + $b] -= 1;
            $diff[$a + $b + 1] += 1;
        }

        $res = $n;
        $currentMoves = 0;
        for ($x = 2; $x <= 2 * $limit; $x++) {
            $currentMoves += $diff[$x];
            if ($currentMoves < $res) {
                $res = $currentMoves;
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
    func minMoves(_ nums: [Int], _ limit: Int) -> Int {
        let n = nums.count
        var diff = [Int](repeating: 0, count: 2 * limit + 2)

        for i in 0..<(n / 2) {
            let a = nums[i]
            let b = nums[n - 1 - i]
            let minVal = min(a, b)
            let maxVal = max(a, b)

            // All target sums in [2, 2*limit] initially require 2 moves per pair
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            // Target sums in [min+1, max+limit] require only 1 move
            diff[minVal + 1] -= 1
            diff[maxVal + limit + 1] += 1

            // Target sum equal to a+b requires 0 moves
            diff[a + b] -= 1
            diff[a + b + 1] += 1
        }

        var res = n
        var currentMoves = 0
        for x in 2...(2 * limit) {
            currentMoves += diff[x]
            if currentMoves < res {
                res = currentMoves
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
import kotlin.math.*

class Solution {
    fun minMoves(nums: IntArray, limit: Int): Int {
        val n = nums.size
        val diff = IntArray(2 * limit + 2)
        for (i in 0 until n / 2) {
            val a = nums[i]
            val b = nums[n - 1 - i]
            val minV = min(a, b)
            val maxV = max(a, b)

            // For each pair, baseline moves for all target sums is 2
            // Range [minV + 1, maxV + limit] requires only 1 move
            // Target sum T = a + b requires 0 moves

            diff[minV + 1] -= 1
            diff[maxV + limit + 1] += 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
        }

        var minAns = n
        var currentMoves = n
        for (i in 2..2 * limit) {
            currentMoves += diff[i]
            minAns = min(minAns, currentMoves)
        }
        return minAns
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
  int minMoves(List<int> nums, int limit) {
    int n = nums.length;
    List<int> diff = List<int>.filled(2 * limit + 2, 0);

    for (int i = 0; i < n ~/ 2; i++) {
      int a = nums[i];
      int b = nums[n - 1 - i];
      int minV = min(a, b);
      int maxV = max(a, b);

      diff[minV + 1] -= 1;
      diff[maxV + limit + 1] += 1;
      diff[a + b] -= 1;
      diff[a + b + 1] += 1;
    }

    int minAns = n;
    int currentMoves = n;
    for (int i = 2; i <= 2 * limit; i++) {
      currentMoves += diff[i];
      minAns = min(minAns, currentMoves);
    }
    return minAns;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minMoves(nums []int, limit int) int {
    n := len(nums)
    diff := make([]int, 2*limit+2)

    for i := 0; i < n/2; i++ {
        a, b := nums[i], nums[n-1-i]
        minV, maxV := a, b
        if b < a {
            minV, maxV = b, a
        }

        diff[minV+1]--
        diff[maxV+limit+1]++
        diff[a+b]--
        diff[a+b+1]++
    }

    minAns := n
    currentMoves := n
    for i := 2; i <= 2*limit; i++ {
        currentMoves += diff[i]
        if currentMoves < minAns {
            minAns = currentMoves
        }
    }
    return minAns
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} limit
# @return {Integer}
def min_moves(nums, limit)
    n = nums.length
    diff = Array.new(2 * limit + 2, 0)

    (0...n/2).each do |i|
        a = nums[i]
        b = nums[n - 1 - i]
        min_v = a < b ? a : b
        max_v = a > b ? a : b

        diff[min_v + 1] -= 1
        diff[max_v + limit + 1] += 1
        diff[a + b] -= 1
        diff[a + b + 1] += 1
    end

    min_ans = n
    current_moves = n
    (2..2*limit).each do |i|
        current_moves += diff[i]
        min_ans = current_moves if current_moves < min_ans
    end
    min_ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.math._

object Solution {
    def minMoves(nums: Array[Int], limit: Int): Int = {
        val n = nums.length
        val diff = new Array[Int](2 * limit + 2)

        var i = 0
        while (i < n / 2) {
            val a = nums(i)
            val b = nums(n - 1 - i)
            val minV = min(a, b)
            val maxV = max(a, b)

            diff(minV + 1) -= 1
            diff(maxV + limit + 1) += 1
            diff(a + b) -= 1
            diff(a + b + 1) += 1
            i += 1
        }

        var minAns = n
        var currentMoves = n
        var t = 2
        while (t <= 2 * limit) {
            currentMoves += diff(t)
            if (currentMoves < minAns) {
                minAns = currentMoves
            }
            t += 1
        }
        minAns
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_moves(nums: Vec<i32>, limit: i32) -> i32 {
        let n = nums.len();
        let limit = limit as usize;
        let mut diff = vec![0; 2 * limit + 2];

        for i in 0..n / 2 {
            let a = nums[i] as usize;
            let b = nums[n - 1 - i] as usize;
            let min_val = a.min(b);
            let max_val = a.max(b);
            let sum = a + b;

            // Case for every pair (a, b) and target sum x:
            // - [2, min_val]: 2 moves
            // - [min_val + 1, a + b - 1]: 1 move
            // - [a + b]: 0 moves
            // - [a + b + 1, max_val + limit]: 1 move
            // - [max_val + limit + 1, 2 * limit]: 2 moves

            diff[2] += 2;
            diff[min_val + 1] -= 1;
            diff[sum] -= 1;
            diff[sum + 1] += 1;
            if max_val + limit + 1 <= 2 * limit {
                diff[max_val + limit + 1] += 1;
            }
        }

        let mut min_res = n as i32;
        let mut curr = 0;
        for i in 2..=(2 * limit) {
            curr += diff[i];
            if curr < min_res {
                min_res = curr;
            }
        }
        min_res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-moves nums limit)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [diff (make-vector (+ (* 2 limit) 2) 0)]
         [half-n (quotient n 2)])
    (for ([i (in-range half-n)])
      (let* ([a (vector-ref nums-vec i)]
             [b (vector-ref nums-vec (- n 1 i))]
             [min-val (min a b)]
             [max-val (max a b)]
             [sum (+ a b)])
        (vector-set! diff 2 (+ (vector-ref diff 2) 2))
        (vector-set! diff (+ min-val 1) (- (vector-ref diff (+ min-val 1)) 1))
        (vector-set! diff sum (- (vector-ref diff sum) 1))
        (vector-set! diff (+ sum 1) (+ (vector-ref diff (+ sum 1)) 1))
        (when (<= (+ max-val limit 1) (* 2 limit))
          (vector-set! diff (+ max-val limit 1) (+ (vector-ref diff (+ max-val limit 1)) 1)))))
    (let-values ([(final-min final-curr)
                  (for/fold ([min-res n]
                             [curr 0])
                            ([i (in-range 2 (+ (* 2 limit) 1))])
                    (let ([new-curr (+ curr (vector-ref diff i))])
                      (values (min min-res new-curr) new-curr)))])
      final-min)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_moves(Nums :: [integer()], Limit :: integer()) -> integer().
min_moves(Nums, Limit) ->
    N = length(Nums),
    NumsVec = list_to_tuple(Nums),
    Diff = atomics:new(2 * Limit + 2, [{signed, true}]),
    lists:foreach(fun(I) ->
        A = element(I + 1, NumsVec),
        B = element(N - I, NumsVec),
        MinVal = erlang:min(A, B),
        MaxVal = erlang:max(A, B),
        Sum = A + B,
        atomics:add(Diff, 2, 2),
        atomics:add(Diff, MinVal + 1, -1),
        atomics:add(Diff, Sum, -1),
        atomics:add(Diff, Sum + 1, 1),
        if 
            MaxVal + Limit + 1 =< 2 * Limit -> atomics:add(Diff, MaxVal + Limit + 1, 1);
            true -> ok
        end
    end, lists:seq(0, (N div 2) - 1)),
    find_min(Diff, 2, 2 * Limit, 0, N).

find_min(Diff, I, Max, Curr, MinRes) when I =< Max ->
    Val = atomics:get(Diff, I),
    NewCurr = Curr + Val,
    NewMin = if NewCurr < MinRes -> NewCurr; true -> MinRes end,
    find_min(Diff, I + 1, Max, NewCurr, NewMin);
find_min(_Diff, _I, _Max, _Curr, MinRes) ->
    MinRes.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_moves(nums :: [integer], limit :: integer) :: integer
  def min_moves(nums, limit) do
    n = length(nums)
    nums_vec = List.to_tuple(nums)
    diff = :atomics.new(2 * limit + 2, [{:signed, true}])
    half_n = div(n, 2)

    Enum.each(0..(half_n - 1), fn i ->
      a = elem(nums_vec, i)
      b = elem(nums_vec, n - 1 - i)
      min_val = min(a, b)
      max_val = max(a, b)
      sum = a + b

      :atomics.add(diff, 2, 2)
      :atomics.add(diff, min_val + 1, -1)
      :atomics.add(diff, sum, -1)
      :atomics.add(diff, sum + 1, 1)
      if max_val + limit + 1 <= 2 * limit do
        :atomics.add(diff, max_val + limit + 1, 1)
      end
    end)

    find_min(diff, 2, 2 * limit, 0, n)
  end

  defp find_min(diff, i, max_idx, curr, min_res) when i <= max_idx do
    new_curr = curr + :atomics.get(diff, i)
    new_min = if new_curr < min_res, do: new_curr, else: min_res
    find_min(diff, i + 1, max_idx, new_curr, new_min)
  end

  defp find_min(_diff, _i, _max_idx, _curr, min_res), do: min_res
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n + limit) with one-paragraph explanation: We iterate through n/2 pairs of elements in the array to populate the difference array, which takes O(n) time. Subsequently, we traverse the difference array of size 2 * limit to compute the prefix sums and find the minimum value, which takes O(limit) time. Both operations are linear with respect to the input size.
- **Space Complexity:** O(limit) with one-paragraph explanation: The difference array used to store the modification counts requires 2 * limit + 2 integers. This space usage is proportional to the maximum possible value of the integers in the array and is independent of the total number of elements n.
