---
layout: post
title: "Four Divisors"
date: 2026-01-04 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/four-divisors/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int sumFourDivisors(std::vector<int>& nums)\
        \ {\n        int totalSumOfDivisors = 0;\n\n        for (int num : nums) {\n\
        \            int currentDivisorsCount = 0;\n            int currentDivisorsSum\
        \ = 0;\n\n            for (int d = 1; (long long)d * d <= num; ++d) {\n    \
        \            if (num % d == 0) {\n                    currentDivisorsCount++;\n\
        \                    currentDivisorsSum += d;\n\n                    if ((long\
        \ long)d * d != num) {\n                        currentDivisorsCount++;\n  \
        \                      currentDivisorsSum += num / d;\n                    }\n\
        \                }\n            }\n\n            if (currentDivisorsCount ==\
        \ 4) {\n                totalSumOfDivisors += currentDivisorsSum;\n        \
        \    }\n        }\n\n        return totalSumOfDivisors;\n    }\n};"
      java: "class Solution {\n    public int sumFourDivisors(int[] nums) {\n      \
        \  int totalSumOfDivisors = 0;\n\n        for (int num : nums) {\n         \
        \   int currentDivisorsCount = 0;\n            int currentDivisorsSum = 0;\n\
        \n            for (int d = 1; (long)d * d <= num; d++) {\n                if\
        \ (num % d == 0) {\n                    currentDivisorsCount++;\n          \
        \          currentDivisorsSum += d;\n\n                    if ((long)d * d !=\
        \ num) {\n                        currentDivisorsCount++;\n                \
        \        currentDivisorsSum += num / d;\n                    }\n           \
        \     }\n            }\n\n            if (currentDivisorsCount == 4) {\n   \
        \             totalSumOfDivisors += currentDivisorsSum;\n            }\n   \
        \     }\n\n        return totalSumOfDivisors;\n    }\n}"
      python: "class Solution(object):\n    def sumFourDivisors(self, nums):\n     \
        \   \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\
        \"\n        total_sum_of_divisors = 0\n        for num in nums:\n          \
        \  current_divisors_count = 0\n            current_divisors_sum = 0\n\n    \
        \        d = 1\n            while d * d <= num:\n                if num % d\
        \ == 0:\n                    current_divisors_count += 1\n                 \
        \   current_divisors_sum += d\n\n                    if d * d != num:\n    \
        \                    current_divisors_count += 1\n                        current_divisors_sum\
        \ += num // d\n                d += 1\n\n            if current_divisors_count\
        \ == 4:\n                total_sum_of_divisors += current_divisors_sum\n\n \
        \       return total_sum_of_divisors"
      python3: "class Solution:\n    def sumFourDivisors(self, nums: List[int]) -> int:\n\
        \        total_sum_of_divisors = 0\n        for num in nums:\n            current_divisors_count\
        \ = 0\n            current_divisors_sum = 0\n\n            d = 1\n         \
        \   while d * d <= num:\n                if num % d == 0:\n                \
        \    current_divisors_count += 1\n                    current_divisors_sum +=\
        \ d\n\n                    if d * d != num:\n                        current_divisors_count\
        \ += 1\n                        current_divisors_sum += num // d\n         \
        \       d += 1\n\n            if current_divisors_count == 4:\n            \
        \    total_sum_of_divisors += current_divisors_sum\n\n        return total_sum_of_divisors"
      c: "int sumFourDivisors(int* nums, int numsSize) {\n    int totalSumOfDivisors\
        \ = 0;\n\n    for (int i = 0; i < numsSize; i++) {\n        int num = nums[i];\n\
        \        int currentDivisorsCount = 0;\n        int currentDivisorsSum = 0;\n\
        \n        for (int d = 1; (long long)d * d <= num; d++) {\n            if (num\
        \ % d == 0) {\n                currentDivisorsCount++;\n                currentDivisorsSum\
        \ += d;\n\n                if ((long long)d * d != num) {\n                \
        \    currentDivisorsCount++;\n                    currentDivisorsSum += num\
        \ / d;\n                }\n            }\n        }\n\n        if (currentDivisorsCount\
        \ == 4) {\n            totalSumOfDivisors += currentDivisorsSum;\n        }\n\
        \    }\n\n    return totalSumOfDivisors;\n}"
      csharp: "public class Solution {\n    public int SumFourDivisors(int[] nums) {\n\
        \        int totalSumOfDivisors = 0;\n        foreach (int num in nums) {\n\
        \            int countDivisors = 0;\n            int currentSumDivisors = 0;\n\
        \            int limit = (int)Math.Sqrt(num);\n\n            for (int i = 1;\
        \ i <= limit; i++) {\n                if (num % i == 0) {\n                \
        \    countDivisors++;\n                    currentSumDivisors += i;\n\n    \
        \                if (i * i != num) {\n                        countDivisors++;\n\
        \                        currentSumDivisors += num / i;\n                  \
        \  }\n                }\n            }\n\n            if (countDivisors == 4)\
        \ {\n                totalSumOfDivisors += currentSumDivisors;\n           \
        \ }\n        }\n        return totalSumOfDivisors;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar sumFourDivisors\
        \ = function(nums) {\n    let totalSumOfDivisors = 0;\n    for (let num of nums)\
        \ {\n        let countDivisors = 0;\n        let currentSumDivisors = 0;\n \
        \       let limit = Math.floor(Math.sqrt(num));\n\n        for (let i = 1; i\
        \ <= limit; i++) {\n            if (num % i === 0) {\n                countDivisors++;\n\
        \                currentSumDivisors += i;\n\n                if (i * i !== num)\
        \ {\n                    countDivisors++;\n                    currentSumDivisors\
        \ += num / i;\n                }\n            }\n        }\n\n        if (countDivisors\
        \ === 4) {\n            totalSumOfDivisors += currentSumDivisors;\n        }\n\
        \    }\n    return totalSumOfDivisors;\n};"
      typescript: "function sumFourDivisors(nums: number[]): number {\n    let totalSumOfDivisors:\
        \ number = 0;\n    for (const num of nums) {\n        let countDivisors: number\
        \ = 0;\n        let currentSumDivisors: number = 0;\n        let limit: number\
        \ = Math.floor(Math.sqrt(num));\n\n        for (let i: number = 1; i <= limit;\
        \ i++) {\n            if (num % i === 0) {\n                countDivisors++;\n\
        \                currentSumDivisors += i;\n\n                if (i * i !== num)\
        \ {\n                    countDivisors++;\n                    currentSumDivisors\
        \ += num / i;\n                }\n            }\n        }\n\n        if (countDivisors\
        \ === 4) {\n            totalSumOfDivisors += currentSumDivisors;\n        }\n\
        \    }\n    return totalSumOfDivisors;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function sumFourDivisors($nums) {\n        $totalSumOfDivisors\
        \ = 0;\n        foreach ($nums as $num) {\n            $countDivisors = 0;\n\
        \            $currentSumDivisors = 0;\n            $limit = (int)sqrt($num);\n\
        \n            for ($i = 1; $i <= $limit; $i++) {\n                if ($num %\
        \ $i == 0) {\n                    $countDivisors++;\n                    $currentSumDivisors\
        \ += $i;\n\n                    if ($i * $i != $num) {\n                   \
        \     $countDivisors++;\n                        $currentSumDivisors += $num\
        \ / $i;\n                    }\n                }\n            }\n\n       \
        \     if ($countDivisors == 4) {\n                $totalSumOfDivisors += $currentSumDivisors;\n\
        \            }\n        }\n        return $totalSumOfDivisors;\n    }\n}"
      swift: "class Solution {\n    func sumFourDivisors(_ nums: [Int]) -> Int {\n \
        \       var totalSumOfDivisors = 0\n        for num in nums {\n            var\
        \ countDivisors = 0\n            var currentSumDivisors = 0\n            let\
        \ limit = Int(sqrt(Double(num)))\n\n            for i in 1...limit {\n     \
        \           if num % i == 0 {\n                    countDivisors += 1\n    \
        \                currentSumDivisors += i\n\n                    if i * i !=\
        \ num {\n                        countDivisors += 1\n                      \
        \  currentSumDivisors += num / i\n                    }\n                }\n\
        \            }\n\n            if countDivisors == 4 {\n                totalSumOfDivisors\
        \ += currentSumDivisors\n            }\n        }\n        return totalSumOfDivisors\n\
        \    }\n}"
      kotlin: "import kotlin.math.sqrt\n\nclass Solution {\n    fun sumFourDivisors(nums:\
        \ IntArray): Int {\n        var totalSumOfDivisors = 0\n\n        for (num in\
        \ nums) {\n            var count = 0\n            var currentSum = 0\n     \
        \       val limit = sqrt(num.toDouble()).toInt()\n\n            for (i in 1..limit)\
        \ {\n                if (num % i == 0) {\n                    if (i * i == num)\
        \ {\n                        count += 1\n                        currentSum\
        \ += i\n                    } else {\n                        count += 2\n \
        \                       currentSum += i\n                        currentSum\
        \ += num / i\n                    }\n                }\n                if (count\
        \ > 4) {\n                    break\n                }\n            }\n\n  \
        \          if (count == 4) {\n                totalSumOfDivisors += currentSum\n\
        \            }\n        }\n\n        return totalSumOfDivisors\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int sumFourDivisors(List<int>\
        \ nums) {\n    int totalSumOfDivisors = 0;\n\n    for (int num in nums) {\n\
        \      int count = 0;\n      int currentSum = 0;\n      int limit = sqrt(num).toInt();\n\
        \n      for (int i = 1; i <= limit; i++) {\n        if (num % i == 0) {\n  \
        \        if (i * i == num) {\n            count += 1;\n            currentSum\
        \ += i;\n          } else {\n            count += 2;\n            currentSum\
        \ += i;\n            currentSum += num ~/ i;\n          }\n        }\n     \
        \   if (count > 4) {\n          break;\n        }\n      }\n\n      if (count\
        \ == 4) {\n        totalSumOfDivisors += currentSum;\n      }\n    }\n\n   \
        \ return totalSumOfDivisors;\n  }\n}"
      go: "import \"math\"\n\nfunc sumFourDivisors(nums []int) int {\n    totalSumOfDivisors\
        \ := 0\n\n    for _, num := range nums {\n        count := 0\n        currentSum\
        \ := 0\n        limit := int(math.Sqrt(float64(num)))\n\n        for i := 1;\
        \ i <= limit; i++ {\n            if num % i == 0 {\n                if i * i\
        \ == num {\n                    count += 1\n                    currentSum +=\
        \ i\n                } else {\n                    count += 2\n            \
        \        currentSum += i\n                    currentSum += num / i\n      \
        \          }\n            }\n            if count > 4 {\n                break\n\
        \            }\n        }\n\n        if count == 4 {\n            totalSumOfDivisors\
        \ += currentSum\n        }\n    }\n\n    return totalSumOfDivisors\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef sum_four_divisors(nums)\n\
        \    total_sum_of_divisors = 0\n\n    nums.each do |num|\n        count = 0\n\
        \        current_sum = 0\n        limit = Math.sqrt(num).to_i\n\n        (1..limit).each\
        \ do |i|\n            if num % i == 0\n                if i * i == num\n   \
        \                 count += 1\n                    current_sum += i\n       \
        \         else\n                    count += 2\n                    current_sum\
        \ += i\n                    current_sum += num / i\n                end\n  \
        \          end\n            if count > 4\n                break\n          \
        \  end\n        end\n\n        if count == 4\n            total_sum_of_divisors\
        \ += current_sum\n        end\n    end\n\n    total_sum_of_divisors\nend"
      scala: "import scala.math.sqrt\n\nobject Solution {\n    def sumFourDivisors(nums:\
        \ Array[Int]): Int = {\n        var totalSumOfDivisors = 0\n\n        for (num\
        \ <- nums) {\n            var count = 0\n            var currentSum = 0\n  \
        \          val limit = sqrt(num.toDouble).toInt\n            var i = 1\n\n \
        \           while (i <= limit && count <= 4) {\n                if (num % i\
        \ == 0) {\n                    if (i * i == num) {\n                       \
        \ count += 1\n                        currentSum += i\n                    }\
        \ else {\n                        count += 2\n                        currentSum\
        \ += i\n                        currentSum += num / i\n                    }\n\
        \                }\n                i += 1\n            }\n\n            if\
        \ (count == 4) {\n                totalSumOfDivisors += currentSum\n       \
        \     }\n        }\n\n        totalSumOfDivisors\n    }\n}"
      rust: "impl Solution {\n    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {\n\
        \        let mut total_sum = 0;\n\n        for &num in nums.iter() {\n     \
        \       let mut divisor_count = 0;\n            let mut current_divisor_sum\
        \ = 0;\n            let limit = (num as f64).sqrt() as i32;\n\n            for\
        \ i in 1..=limit {\n                if num % i == 0 {\n                    divisor_count\
        \ += 1;\n                    current_divisor_sum += i;\n                   \
        \ if i * i != num {\n                        divisor_count += 1;\n         \
        \               current_divisor_sum += num / i;\n                    }\n   \
        \             }\n                if divisor_count > 4 {\n                  \
        \  break;\n                }\n            }\n\n            if divisor_count\
        \ == 4 {\n                total_sum += current_divisor_sum;\n            }\n\
        \        }\n\n        total_sum\n    }\n}"
      racket: "(define/contract (sum-four-divisors nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (define (get-four-divisor-sum n)\n    (let loop ((i 1)\
        \ (divisor-count 0) (current-sum 0))\n      (cond\n        ((> i (floor (sqrt\
        \ n))) ; Loop finished\n         (if (= divisor-count 4) current-sum 0))\n \
        \       ((> divisor-count 4) ; Optimization: more than 4 divisors, stop early\n\
        \         0)\n        ((zero? (modulo n i)) ; i is a divisor\n         (let*\
        \ ((new-count (+ divisor-count 1))\n                (new-sum (+ current-sum\
        \ i)))\n           (if (= (* i i) n)\n               (loop (+ i 1) new-count\
        \ new-sum)\n               (loop (+ i 1) (+ new-count 1) (+ new-sum (quotient\
        \ n i))))))\n        (else ; i is not a divisor\n         (loop (+ i 1) divisor-count\
        \ current-sum)))))\n\n  (foldl (lambda (num acc) (+ acc (get-four-divisor-sum\
        \ num))) 0 nums))"
      erlang: "-spec sum_four_divisors(Nums :: [integer()]) -> integer().\nsum_four_divisors(Nums)\
        \ ->\n    lists:foldl(fun(Num, Acc) ->\n        case get_four_divisor_sum(Num)\
        \ of\n            0 -> Acc;\n            Sum -> Acc + Sum\n        end\n   \
        \ end, 0, Nums).\n\nget_four_divisor_sum(N) ->\n    Limit = trunc(math:sqrt(N)),\n\
        \    get_four_divisor_sum_loop(1, Limit, N, 0, 0).\n\nget_four_divisor_sum_loop(I,\
        \ Limit, N, DivisorCount, CurrentSum) when I > Limit ->\n    case DivisorCount\
        \ of\n        4 -> CurrentSum;\n        _ -> 0\n    end;\nget_four_divisor_sum_loop(I,\
        \ _Limit, _N, DivisorCount, _CurrentSum) when DivisorCount > 4 ->\n    0;\n\
        get_four_divisor_sum_loop(I, Limit, N, DivisorCount, CurrentSum) ->\n    case\
        \ N rem I of\n        0 -> % I is a divisor\n            NewDivisorCount = DivisorCount\
        \ + 1,\n            NewCurrentSum = CurrentSum + I,\n            if\n      \
        \          I * I == N ->\n                    get_four_divisor_sum_loop(I +\
        \ 1, Limit, N, NewDivisorCount, NewCurrentSum);\n                true ->\n \
        \                   get_four_divisor_sum_loop(I + 1, Limit, N, NewDivisorCount\
        \ + 1, NewCurrentSum + (N div I))\n            end;\n        _ -> % I is not\
        \ a divisor\n            get_four_divisor_sum_loop(I + 1, Limit, N, DivisorCount,\
        \ CurrentSum)\n    end."
      elixir: "defmodule Solution do\n  @spec sum_four_divisors(nums :: [integer]) ::\
        \ integer\n  def sum_four_divisors(nums) do\n    Enum.reduce(nums, 0, fn num,\
        \ acc ->\n      case get_four_divisor_sum(num) do\n        0 -> acc\n      \
        \  sum -> acc + sum\n      end\n    end)\n  end\n\n  defp get_four_divisor_sum(n)\
        \ do\n    limit = trunc(:math.sqrt(n))\n    get_four_divisor_sum_loop(1, limit,\
        \ n, 0, 0)\n  end\n\n  defp get_four_divisor_sum_loop(i, _limit, _n, divisor_count,\
        \ _current_sum) when i > _limit do\n    if divisor_count == 4, do: _current_sum,\
        \ else: 0\n  end\n\n  defp get_four_divisor_sum_loop(_i, _limit, _n, divisor_count,\
        \ _current_sum) when divisor_count > 4 do\n    0\n  end\n\n  defp get_four_divisor_sum_loop(i,\
        \ limit, n, divisor_count, current_sum) do\n    if rem(n, i) == 0 do\n     \
        \ new_divisor_count = divisor_count + 1\n      new_current_sum = current_sum\
        \ + i\n\n      if i * i == n do\n        get_four_divisor_sum_loop(i + 1, limit,\
        \ n, new_divisor_count, new_current_sum)\n      else\n        get_four_divisor_sum_loop(i\
        \ + 1, limit, n, new_divisor_count + 1, new_current_sum + div(n, i))\n     \
        \ end\n    else\n      get_four_divisor_sum_loop(i + 1, limit, n, divisor_count,\
        \ current_sum)\n    end\n  end\nend"
    approach: 'The core idea is to iterate through each number in the input array `nums`
      and determine if it has exactly four divisors. For each such number, we calculate
      the sum of its divisors and add it to a running total. If a number does not have
      exactly four divisors, or if it has more than four divisors (in which case we
      can stop early), it contributes nothing to the total sum.


      To efficiently find divisors for a given number `n`, we iterate from `i = 1` up
      to `sqrt(n)`. If `i` divides `n`, then `i` is a divisor. Additionally, `n/i` is
      also a divisor. We must be careful to count `i` and `n/i` correctly: if `i * i
      == n`, then `i` and `n/i` are the same divisor, so we count it only once. Otherwise,
      they are distinct, and we count both. During this process, we maintain a count
      of divisors and their sum. An optimization is to stop checking divisors for `n`
      as soon as `divisor_count` exceeds 4, as `n` can no longer be a candidate. After
      checking all `i` up to `sqrt(n)`, if `divisor_count` is exactly 4, its `current_divisor_sum`
      is added to the overall result.'
    time_complexity: The time complexity is dominated by iterating through each number
      in `nums` and, for each number, finding its divisors. For a number `n`, finding
      its divisors up to `sqrt(n)` takes `O(sqrt(n))` time. Given `N` as the length
      of `nums` and `M` as the maximum value in `nums`, the total time complexity is
      `O(N * sqrt(M))`. With `N = 10^4` and `M = 10^5`, `sqrt(M)` is approximately `316`,
      leading to roughly `10^4 * 316 = 3.16 * 10^6` operations, which is efficient enough.
    space_complexity: The space complexity is `O(1)` because we only use a few constant-size
      variables to store counts and sums during the computation. No auxiliary data structures
      that scale with the input size are used beyond the input array itself.
    elapsed_time: 107.41080737113953
    model: gemini-2.5-flash
    generated_at: '2026-01-04 06:40:37 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int sumFourDivisors(vector<int>& nums) {\n\
        \        int sum = 0;\n        for (int num : nums) {\n            int count\
        \ = 0;\n            int divisorSum = 0;\n            for (int i = 1; i * i <=\
        \ num; i++) {\n                if (num % i == 0) {\n                    count++;\n\
        \                    divisorSum += i;\n                    if (i * i != num)\
        \ {\n                        count++;\n                        divisorSum +=\
        \ num / i;\n                    }\n                }\n            }\n      \
        \      if (count == 4) {\n                sum += divisorSum;\n            }\n\
        \        }\n        return sum;\n    }\n};"
      java: "class Solution {\n    public int sumFourDivisors(int[] nums) {\n      \
        \  int sum = 0;\n        for (int num : nums) {\n            int count = 0;\n\
        \            int divisorSum = 0;\n            for (int i = 1; i * i <= num;\
        \ i++) {\n                if (num % i == 0) {\n                    count++;\n\
        \                    divisorSum += i;\n                    if (i * i != num)\
        \ {\n                        count++;\n                        divisorSum +=\
        \ num / i;\n                    }\n                }\n            }\n      \
        \      if (count == 4) {\n                sum += divisorSum;\n            }\n\
        \        }\n        return sum;\n    }\n}"
      python: "class Solution(object):\n    def sumFourDivisors(self, nums):\n     \
        \   sum = 0\n        for num in nums:\n            count = 0\n            divisorSum\
        \ = 0\n            for i in range(1, int(num ** 0.5) + 1):\n               \
        \ if num % i == 0:\n                    count += 1\n                    divisorSum\
        \ += i\n                    if i * i != num:\n                        count\
        \ += 1\n                        divisorSum += num // i\n            if count\
        \ == 4:\n                sum += divisorSum\n        return sum"
      python3: "class Solution:\n    def sumFourDivisors(self, nums: list[int]) -> int:\n\
        \        sum = 0\n        for num in nums:\n            count = 0\n        \
        \    divisorSum = 0\n            for i in range(1, int(num ** 0.5) + 1):\n \
        \               if num % i == 0:\n                    count += 1\n         \
        \           divisorSum += i\n                    if i * i != num:\n        \
        \                count += 1\n                        divisorSum += num // i\n\
        \            if count == 4:\n                sum += divisorSum\n        return\
        \ sum"
      c: "int sumFourDivisors(int* nums, int numsSize) {\n    int sum = 0;\n    for\
        \ (int i = 0; i < numsSize; i++) {\n        int count = 0;\n        int divisorSum\
        \ = 0;\n        for (int j = 1; j * j <= nums[i]; j++) {\n            if (nums[i]\
        \ % j == 0) {\n                count++;\n                divisorSum += j;\n\
        \                if (j * j != nums[i]) {\n                    count++;\n   \
        \                 divisorSum += nums[i] / j;\n                }\n          \
        \  }\n        }\n        if (count == 4) {\n            sum += divisorSum;\n\
        \        }\n    }\n    return sum;\n}"
      csharp: "public class Solution {\n    public int SumFourDivisors(int[] nums) {\n\
        \        int sum = 0;\n        foreach (int num in nums) {\n            List<int>\
        \ divisors = new List<int>();\n            for (int i = 1; i <= Math.Sqrt(num);\
        \ i++) {\n                if (num % i == 0) {\n                    divisors.Add(i);\n\
        \                    if (i != num / i) divisors.Add(num / i);\n            \
        \    }\n            }\n            if (divisors.Count == 4) {\n            \
        \    sum += divisors.Sum();\n            }\n        }\n        return sum;\n\
        \    }\n}"
      javascript: "var sumFourDivisors = function(nums) {\n    let sum = 0;\n    for\
        \ (let num of nums) {\n        let divisors = [];\n        for (let i = 1; i\
        \ <= Math.sqrt(num); i++) {\n            if (num % i == 0) {\n             \
        \   divisors.push(i);\n                if (i != num / i) divisors.push(num /\
        \ i);\n            }\n        }\n        if (divisors.length == 4) {\n     \
        \       sum += divisors.reduce((a, b) => a + b, 0);\n        }\n    }\n    return\
        \ sum;\n};"
      typescript: "function sumFourDivisors(nums: number[]): number {\n    let sum =\
        \ 0;\n    for (let num of nums) {\n        let divisors: number[] = [];\n  \
        \      for (let i = 1; i <= Math.sqrt(num); i++) {\n            if (num % i\
        \ == 0) {\n                divisors.push(i);\n                if (i != num /\
        \ i) divisors.push(num / i);\n            }\n        }\n        if (divisors.length\
        \ == 4) {\n            sum += divisors.reduce((a, b) => a + b, 0);\n       \
        \ }\n    }\n    return sum;\n}"
      php: "class Solution {\n    function sumFourDivisors($nums) {\n        $sum =\
        \ 0;\n        foreach ($nums as $num) {\n            $divisors = [];\n     \
        \       for ($i = 1; $i <= sqrt($num); $i++) {\n                if ($num % $i\
        \ == 0) {\n                    $divisors[] = $i;\n                    if ($i\
        \ != $num / $i) $divisors[] = $num / $i;\n                }\n            }\n\
        \            if (count($divisors) == 4) {\n                $sum += array_sum($divisors);\n\
        \            }\n        }\n        return $sum;\n    }\n}"
      swift: "class Solution {\n    func sumFourDivisors(_ nums: [Int]) -> Int {\n \
        \       var sum = 0\n        for num in nums {\n            var divisors: [Int]\
        \ = []\n            for i in 1...Int(sqrt(Double(num))) {\n                if\
        \ num % i == 0 {\n                    divisors.append(i)\n                 \
        \   if i != num / i {\n                        divisors.append(num / i)\n  \
        \                  }\n                }\n            }\n            if divisors.count\
        \ == 4 {\n                sum += divisors.reduce(0, +)\n            }\n    \
        \    }\n        return sum\n    }\n}"
      kotlin: "class Solution {\n    fun sumFourDivisors(nums: IntArray): Int {\n  \
        \      var sum = 0\n        for (num in nums) {\n            var divisors =\
        \ 0\n            var divSum = 0\n            for (i in 1..Math.sqrt(num.toDouble()).toInt())\
        \ {\n                if (num % i == 0) {\n                    if (num / i ==\
        \ i) {\n                        divisors++\n                        divSum +=\
        \ i\n                    } else {\n                        divisors += 2\n \
        \                       divSum += i + num / i\n                    }\n     \
        \           }\n                if (divisors > 4) break\n            }\n    \
        \        if (divisors == 4) sum += divSum\n        }\n        return sum\n \
        \   }\n}"
      dart: "class Solution {\n  int sumFourDivisors(List<int> nums) {\n    int sum\
        \ = 0;\n    for (int num in nums) {\n      int divisors = 0;\n      int divSum\
        \ = 0;\n      for (int i = 1; i <= num.sqrt().floor(); i++) {\n        if (num\
        \ % i == 0) {\n          if (num / i == i) {\n            divisors++;\n    \
        \        divSum += i;\n          } else {\n            divisors += 2;\n    \
        \        divSum += i + num / i;\n          }\n        }\n        if (divisors\
        \ > 4) break;\n      }\n      if (divisors == 4) sum += divSum;\n    }\n   \
        \ return sum;\n  }\n}"
      go: "func sumFourDivisors(nums []int) int {\n    sum := 0\n    for _, num := range\
        \ nums {\n        divisors := 0\n        divSum := 0\n        for i := 1; i\
        \ <= int(math.Sqrt(float64(num))); i++ {\n            if num % i == 0 {\n  \
        \              if num / i == i {\n                    divisors++\n         \
        \           divSum += i\n                } else {\n                    divisors\
        \ += 2\n                    divSum += i + num / i\n                }\n     \
        \       }\n            if divisors > 4 {\n                break\n          \
        \  }\n        }\n        if divisors == 4 {\n            sum += divSum\n   \
        \     }\n    }\n    return sum\n}"
      ruby: "def sum_four_divisors(nums)\n    sum = 0\n    nums.each do |num|\n    \
        \    divisors = 0\n        div_sum = 0\n        (1..Math.sqrt(num).to_i).each\
        \ do |i|\n            if num % i == 0\n                if num / i == i\n   \
        \                 divisors += 1\n                    div_sum += i\n        \
        \        else\n                    divisors += 2\n                    div_sum\
        \ += i + num / i\n                end\n            end\n            break if\
        \ divisors > 4\n        end\n        sum += div_sum if divisors == 4\n    end\n\
        \    sum\nend"
      scala: "object Solution {\n    def sumFourDivisors(nums: Array[Int]): Int = {\n\
        \        var sum = 0\n        for (num <- nums) {\n            var divisors\
        \ = 0\n            var divSum = 0\n            for (i <- 1 to Math.sqrt(num).toInt)\
        \ {\n                if (num % i == 0) {\n                    if (num / i ==\
        \ i) {\n                        divisors += 1\n                        divSum\
        \ += i\n                    } else {\n                        divisors += 2\n\
        \                        divSum += i + num / i\n                    }\n    \
        \            }\n                if (divisors > 4) {\n                    i =\
        \ Int.MaxValue\n                }\n            }\n            if (divisors ==\
        \ 4) sum += divSum\n        }\n        sum\n    }\n}"
      rust: "impl Solution {\n    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {\n\
        \        let mut sum = 0;\n        for num in nums {\n            let mut divisors\
        \ = Vec::new();\n            for i in 1..=(num as f64).sqrt() as i32 {\n   \
        \             if num % i == 0 {\n                    divisors.push(i);\n   \
        \                 if i * i != num {\n                        divisors.push(num\
        \ / i);\n                    }\n                }\n            }\n         \
        \   if divisors.len() == 4 {\n                sum += divisors.iter().sum::<i32>();\n\
        \            }\n        }\n        sum\n    }\n}"
      racket: "(define/contract (sum-four-divisors nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let ([sum 0])\n    (for ([num nums])\n      (let ([divisors\
        \ (for/list ([i (in-range 1 (add1 (sqrt num)))])\n                         (if\
        \ (zero? (remainder num i))\n                             (list i (quotient\
        \ num i))\n                             '()))])\n        (if (= (length (flatten\
        \ divisors)) 4)\n            (set! sum (+ sum (apply + (flatten divisors))))))\n\
        \    sum))"
      erlang: "sum_four_divisors(Nums) ->\n  lists:foldl(fun (Num, Sum) ->\n       \
        \             Divisors = [I || I <- lists:seq(1, trunc(math:sqrt(Num))), Num\
        \ rem I == 0],\n                    case length(Divisors) of\n             \
        \         4 -> Sum + lists:sum([I || I <- Divisors] ++ [Num div I || I <- Divisors,\
        \ I * I /= Num]);\n                      _ -> Sum\n                    end\n\
        \                end, 0, Nums)."
      elixir: "defmodule Solution do\n  @spec sum_four_divisors(nums :: [integer]) ::\
        \ integer\n  def sum_four_divisors(nums) do\n    Enum.reduce(nums, 0, fn num,\
        \ sum ->\n      divisors = Enum.flat_map(1..:math.sqrt(num), fn i ->\n     \
        \   if rem(num, i) == 0 do\n          if i * i == num, do: [i], else: [i, div(num,\
        \ i)]\n        else\n          []\n        end\n      end)\n      if length(divisors)\
        \ == 4, do: sum + Enum.sum(divisors), else: sum\n    end)\n  end\nend"
    approach: The problem can be solved by iterating over each number in the input array
      and finding its divisors. For each number, we can find its divisors by iterating
      up to its square root, as any factor larger than the square root would have a
      corresponding factor smaller than the square root. We then check if the number
      of divisors is exactly four and if so, we add the sum of these divisors to the
      total sum. This approach ensures that we only consider numbers with exactly four
      divisors and sum up their divisors accordingly. The key intuition here is to recognize
      that a number with exactly four divisors can be expressed as either p^3 or p*q,
      where p and q are distinct prime numbers.
    time_complexity: The time complexity of this solution is O(n*sqrt(m)), where n is
      the number of elements in the input array and m is the maximum value in the array.
      This is because for each number in the array, we are iterating up to its square
      root to find its divisors.
    space_complexity: The space complexity of this solution is O(1), as we are only
      using a constant amount of space to store the total sum and the divisors of each
      number. We are not using any data structures that scale with the input size.
    elapsed_time: 9.337400436401367
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-04 06:41:01 '
---

## Problem #1390: Four Divisors

**Difficulty:** Medium

**Topics:** Array, Math

## Problem Description

<p>Given an integer array <code>nums</code>, return <em>the sum of divisors of the integers in that array that have exactly four divisors</em>. If there is no such integer in the array, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [21,4,7]
<strong>Output:</strong> 32
<strong>Explanation:</strong> 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [21,21]
<strong>Output:</strong> 64
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Find the divisors of each element in the array.

2. You only need to loop to the square root of a number to find its divisors.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-04 06:40:37 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The core idea is to iterate through each number in the input array `nums` and determine if it has exactly four divisors. For each such number, we calculate the sum of its divisors and add it to a running total. If a number does not have exactly four divisors, or if it has more than four divisors (in which case we can stop early), it contributes nothing to the total sum.

To efficiently find divisors for a given number `n`, we iterate from `i = 1` up to `sqrt(n)`. If `i` divides `n`, then `i` is a divisor. Additionally, `n/i` is also a divisor. We must be careful to count `i` and `n/i` correctly: if `i * i == n`, then `i` and `n/i` are the same divisor, so we count it only once. Otherwise, they are distinct, and we count both. During this process, we maintain a count of divisors and their sum. An optimization is to stop checking divisors for `n` as soon as `divisor_count` exceeds 4, as `n` can no longer be a candidate. After checking all `i` up to `sqrt(n)`, if `divisor_count` is exactly 4, its `current_divisor_sum` is added to the overall result.

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
    int sumFourDivisors(std::vector<int>& nums) {
        int totalSumOfDivisors = 0;

        for (int num : nums) {
            int currentDivisorsCount = 0;
            int currentDivisorsSum = 0;

            for (int d = 1; (long long)d * d <= num; ++d) {
                if (num % d == 0) {
                    currentDivisorsCount++;
                    currentDivisorsSum += d;

                    if ((long long)d * d != num) {
                        currentDivisorsCount++;
                        currentDivisorsSum += num / d;
                    }
                }
            }

            if (currentDivisorsCount == 4) {
                totalSumOfDivisors += currentDivisorsSum;
            }
        }

        return totalSumOfDivisors;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int sumFourDivisors(int[] nums) {
        int totalSumOfDivisors = 0;

        for (int num : nums) {
            int currentDivisorsCount = 0;
            int currentDivisorsSum = 0;

            for (int d = 1; (long)d * d <= num; d++) {
                if (num % d == 0) {
                    currentDivisorsCount++;
                    currentDivisorsSum += d;

                    if ((long)d * d != num) {
                        currentDivisorsCount++;
                        currentDivisorsSum += num / d;
                    }
                }
            }

            if (currentDivisorsCount == 4) {
                totalSumOfDivisors += currentDivisorsSum;
            }
        }

        return totalSumOfDivisors;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum_of_divisors = 0
        for num in nums:
            current_divisors_count = 0
            current_divisors_sum = 0

            d = 1
            while d * d <= num:
                if num % d == 0:
                    current_divisors_count += 1
                    current_divisors_sum += d

                    if d * d != num:
                        current_divisors_count += 1
                        current_divisors_sum += num // d
                d += 1

            if current_divisors_count == 4:
                total_sum_of_divisors += current_divisors_sum

        return total_sum_of_divisors
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum_of_divisors = 0
        for num in nums:
            current_divisors_count = 0
            current_divisors_sum = 0

            d = 1
            while d * d <= num:
                if num % d == 0:
                    current_divisors_count += 1
                    current_divisors_sum += d

                    if d * d != num:
                        current_divisors_count += 1
                        current_divisors_sum += num // d
                d += 1

            if current_divisors_count == 4:
                total_sum_of_divisors += current_divisors_sum

        return total_sum_of_divisors
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int sumFourDivisors(int* nums, int numsSize) {
    int totalSumOfDivisors = 0;

    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        int currentDivisorsCount = 0;
        int currentDivisorsSum = 0;

        for (int d = 1; (long long)d * d <= num; d++) {
            if (num % d == 0) {
                currentDivisorsCount++;
                currentDivisorsSum += d;

                if ((long long)d * d != num) {
                    currentDivisorsCount++;
                    currentDivisorsSum += num / d;
                }
            }
        }

        if (currentDivisorsCount == 4) {
            totalSumOfDivisors += currentDivisorsSum;
        }
    }

    return totalSumOfDivisors;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int SumFourDivisors(int[] nums) {
        int totalSumOfDivisors = 0;
        foreach (int num in nums) {
            int countDivisors = 0;
            int currentSumDivisors = 0;
            int limit = (int)Math.Sqrt(num);

            for (int i = 1; i <= limit; i++) {
                if (num % i == 0) {
                    countDivisors++;
                    currentSumDivisors += i;

                    if (i * i != num) {
                        countDivisors++;
                        currentSumDivisors += num / i;
                    }
                }
            }

            if (countDivisors == 4) {
                totalSumOfDivisors += currentSumDivisors;
            }
        }
        return totalSumOfDivisors;
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
var sumFourDivisors = function(nums) {
    let totalSumOfDivisors = 0;
    for (let num of nums) {
        let countDivisors = 0;
        let currentSumDivisors = 0;
        let limit = Math.floor(Math.sqrt(num));

        for (let i = 1; i <= limit; i++) {
            if (num % i === 0) {
                countDivisors++;
                currentSumDivisors += i;

                if (i * i !== num) {
                    countDivisors++;
                    currentSumDivisors += num / i;
                }
            }
        }

        if (countDivisors === 4) {
            totalSumOfDivisors += currentSumDivisors;
        }
    }
    return totalSumOfDivisors;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sumFourDivisors(nums: number[]): number {
    let totalSumOfDivisors: number = 0;
    for (const num of nums) {
        let countDivisors: number = 0;
        let currentSumDivisors: number = 0;
        let limit: number = Math.floor(Math.sqrt(num));

        for (let i: number = 1; i <= limit; i++) {
            if (num % i === 0) {
                countDivisors++;
                currentSumDivisors += i;

                if (i * i !== num) {
                    countDivisors++;
                    currentSumDivisors += num / i;
                }
            }
        }

        if (countDivisors === 4) {
            totalSumOfDivisors += currentSumDivisors;
        }
    }
    return totalSumOfDivisors;
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
     * @return Integer
     */
    function sumFourDivisors($nums) {
        $totalSumOfDivisors = 0;
        foreach ($nums as $num) {
            $countDivisors = 0;
            $currentSumDivisors = 0;
            $limit = (int)sqrt($num);

            for ($i = 1; $i <= $limit; $i++) {
                if ($num % $i == 0) {
                    $countDivisors++;
                    $currentSumDivisors += $i;

                    if ($i * $i != $num) {
                        $countDivisors++;
                        $currentSumDivisors += $num / $i;
                    }
                }
            }

            if ($countDivisors == 4) {
                $totalSumOfDivisors += $currentSumDivisors;
            }
        }
        return $totalSumOfDivisors;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sumFourDivisors(_ nums: [Int]) -> Int {
        var totalSumOfDivisors = 0
        for num in nums {
            var countDivisors = 0
            var currentSumDivisors = 0
            let limit = Int(sqrt(Double(num)))

            for i in 1...limit {
                if num % i == 0 {
                    countDivisors += 1
                    currentSumDivisors += i

                    if i * i != num {
                        countDivisors += 1
                        currentSumDivisors += num / i
                    }
                }
            }

            if countDivisors == 4 {
                totalSumOfDivisors += currentSumDivisors
            }
        }
        return totalSumOfDivisors
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
    fun sumFourDivisors(nums: IntArray): Int {
        var totalSumOfDivisors = 0

        for (num in nums) {
            var count = 0
            var currentSum = 0
            val limit = sqrt(num.toDouble()).toInt()

            for (i in 1..limit) {
                if (num % i == 0) {
                    if (i * i == num) {
                        count += 1
                        currentSum += i
                    } else {
                        count += 2
                        currentSum += i
                        currentSum += num / i
                    }
                }
                if (count > 4) {
                    break
                }
            }

            if (count == 4) {
                totalSumOfDivisors += currentSum
            }
        }

        return totalSumOfDivisors
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
  int sumFourDivisors(List<int> nums) {
    int totalSumOfDivisors = 0;

    for (int num in nums) {
      int count = 0;
      int currentSum = 0;
      int limit = sqrt(num).toInt();

      for (int i = 1; i <= limit; i++) {
        if (num % i == 0) {
          if (i * i == num) {
            count += 1;
            currentSum += i;
          } else {
            count += 2;
            currentSum += i;
            currentSum += num ~/ i;
          }
        }
        if (count > 4) {
          break;
        }
      }

      if (count == 4) {
        totalSumOfDivisors += currentSum;
      }
    }

    return totalSumOfDivisors;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "math"

func sumFourDivisors(nums []int) int {
    totalSumOfDivisors := 0

    for _, num := range nums {
        count := 0
        currentSum := 0
        limit := int(math.Sqrt(float64(num)))

        for i := 1; i <= limit; i++ {
            if num % i == 0 {
                if i * i == num {
                    count += 1
                    currentSum += i
                } else {
                    count += 2
                    currentSum += i
                    currentSum += num / i
                }
            }
            if count > 4 {
                break
            }
        }

        if count == 4 {
            totalSumOfDivisors += currentSum
        }
    }

    return totalSumOfDivisors
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def sum_four_divisors(nums)
    total_sum_of_divisors = 0

    nums.each do |num|
        count = 0
        current_sum = 0
        limit = Math.sqrt(num).to_i

        (1..limit).each do |i|
            if num % i == 0
                if i * i == num
                    count += 1
                    current_sum += i
                else
                    count += 2
                    current_sum += i
                    current_sum += num / i
                end
            end
            if count > 4
                break
            end
        end

        if count == 4
            total_sum_of_divisors += current_sum
        end
    end

    total_sum_of_divisors
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.math.sqrt

object Solution {
    def sumFourDivisors(nums: Array[Int]): Int = {
        var totalSumOfDivisors = 0

        for (num <- nums) {
            var count = 0
            var currentSum = 0
            val limit = sqrt(num.toDouble).toInt
            var i = 1

            while (i <= limit && count <= 4) {
                if (num % i == 0) {
                    if (i * i == num) {
                        count += 1
                        currentSum += i
                    } else {
                        count += 2
                        currentSum += i
                        currentSum += num / i
                    }
                }
                i += 1
            }

            if (count == 4) {
                totalSumOfDivisors += currentSum
            }
        }

        totalSumOfDivisors
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        let mut total_sum = 0;

        for &num in nums.iter() {
            let mut divisor_count = 0;
            let mut current_divisor_sum = 0;
            let limit = (num as f64).sqrt() as i32;

            for i in 1..=limit {
                if num % i == 0 {
                    divisor_count += 1;
                    current_divisor_sum += i;
                    if i * i != num {
                        divisor_count += 1;
                        current_divisor_sum += num / i;
                    }
                }
                if divisor_count > 4 {
                    break;
                }
            }

            if divisor_count == 4 {
                total_sum += current_divisor_sum;
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
(define/contract (sum-four-divisors nums)
  (-> (listof exact-integer?) exact-integer?)
  (define (get-four-divisor-sum n)
    (let loop ((i 1) (divisor-count 0) (current-sum 0))
      (cond
        ((> i (floor (sqrt n))) ; Loop finished
         (if (= divisor-count 4) current-sum 0))
        ((> divisor-count 4) ; Optimization: more than 4 divisors, stop early
         0)
        ((zero? (modulo n i)) ; i is a divisor
         (let* ((new-count (+ divisor-count 1))
                (new-sum (+ current-sum i)))
           (if (= (* i i) n)
               (loop (+ i 1) new-count new-sum)
               (loop (+ i 1) (+ new-count 1) (+ new-sum (quotient n i))))))
        (else ; i is not a divisor
         (loop (+ i 1) divisor-count current-sum)))))

  (foldl (lambda (num acc) (+ acc (get-four-divisor-sum num))) 0 nums))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sum_four_divisors(Nums :: [integer()]) -> integer().
sum_four_divisors(Nums) ->
    lists:foldl(fun(Num, Acc) ->
        case get_four_divisor_sum(Num) of
            0 -> Acc;
            Sum -> Acc + Sum
        end
    end, 0, Nums).

get_four_divisor_sum(N) ->
    Limit = trunc(math:sqrt(N)),
    get_four_divisor_sum_loop(1, Limit, N, 0, 0).

get_four_divisor_sum_loop(I, Limit, N, DivisorCount, CurrentSum) when I > Limit ->
    case DivisorCount of
        4 -> CurrentSum;
        _ -> 0
    end;
get_four_divisor_sum_loop(I, _Limit, _N, DivisorCount, _CurrentSum) when DivisorCount > 4 ->
    0;
get_four_divisor_sum_loop(I, Limit, N, DivisorCount, CurrentSum) ->
    case N rem I of
        0 -> % I is a divisor
            NewDivisorCount = DivisorCount + 1,
            NewCurrentSum = CurrentSum + I,
            if
                I * I == N ->
                    get_four_divisor_sum_loop(I + 1, Limit, N, NewDivisorCount, NewCurrentSum);
                true ->
                    get_four_divisor_sum_loop(I + 1, Limit, N, NewDivisorCount + 1, NewCurrentSum + (N div I))
            end;
        _ -> % I is not a divisor
            get_four_divisor_sum_loop(I + 1, Limit, N, DivisorCount, CurrentSum)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sum_four_divisors(nums :: [integer]) :: integer
  def sum_four_divisors(nums) do
    Enum.reduce(nums, 0, fn num, acc ->
      case get_four_divisor_sum(num) do
        0 -> acc
        sum -> acc + sum
      end
    end)
  end

  defp get_four_divisor_sum(n) do
    limit = trunc(:math.sqrt(n))
    get_four_divisor_sum_loop(1, limit, n, 0, 0)
  end

  defp get_four_divisor_sum_loop(i, _limit, _n, divisor_count, _current_sum) when i > _limit do
    if divisor_count == 4, do: _current_sum, else: 0
  end

  defp get_four_divisor_sum_loop(_i, _limit, _n, divisor_count, _current_sum) when divisor_count > 4 do
    0
  end

  defp get_four_divisor_sum_loop(i, limit, n, divisor_count, current_sum) do
    if rem(n, i) == 0 do
      new_divisor_count = divisor_count + 1
      new_current_sum = current_sum + i

      if i * i == n do
        get_four_divisor_sum_loop(i + 1, limit, n, new_divisor_count, new_current_sum)
      else
        get_four_divisor_sum_loop(i + 1, limit, n, new_divisor_count + 1, new_current_sum + div(n, i))
      end
    else
      get_four_divisor_sum_loop(i + 1, limit, n, divisor_count, current_sum)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by iterating through each number in `nums` and, for each number, finding its divisors. For a number `n`, finding its divisors up to `sqrt(n)` takes `O(sqrt(n))` time. Given `N` as the length of `nums` and `M` as the maximum value in `nums`, the total time complexity is `O(N * sqrt(M))`. With `N = 10^4` and `M = 10^5`, `sqrt(M)` is approximately `316`, leading to roughly `10^4 * 316 = 3.16 * 10^6` operations, which is efficient enough.

- **Space Complexity:** The space complexity is `O(1)` because we only use a few constant-size variables to store counts and sums during the computation. No auxiliary data structures that scale with the input size are used beyond the input array itself.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-04 06:41:01 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over each number in the input array and finding its divisors. For each number, we can find its divisors by iterating up to its square root, as any factor larger than the square root would have a corresponding factor smaller than the square root. We then check if the number of divisors is exactly four and if so, we add the sum of these divisors to the total sum. This approach ensures that we only consider numbers with exactly four divisors and sum up their divisors accordingly. The key intuition here is to recognize that a number with exactly four divisors can be expressed as either p^3 or p*q, where p and q are distinct prime numbers.

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
    int sumFourDivisors(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) {
            int count = 0;
            int divisorSum = 0;
            for (int i = 1; i * i <= num; i++) {
                if (num % i == 0) {
                    count++;
                    divisorSum += i;
                    if (i * i != num) {
                        count++;
                        divisorSum += num / i;
                    }
                }
            }
            if (count == 4) {
                sum += divisorSum;
            }
        }
        return sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int sumFourDivisors(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            int count = 0;
            int divisorSum = 0;
            for (int i = 1; i * i <= num; i++) {
                if (num % i == 0) {
                    count++;
                    divisorSum += i;
                    if (i * i != num) {
                        count++;
                        divisorSum += num / i;
                    }
                }
            }
            if (count == 4) {
                sum += divisorSum;
            }
        }
        return sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def sumFourDivisors(self, nums):
        sum = 0
        for num in nums:
            count = 0
            divisorSum = 0
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    count += 1
                    divisorSum += i
                    if i * i != num:
                        count += 1
                        divisorSum += num // i
            if count == 4:
                sum += divisorSum
        return sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        sum = 0
        for num in nums:
            count = 0
            divisorSum = 0
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    count += 1
                    divisorSum += i
                    if i * i != num:
                        count += 1
                        divisorSum += num // i
            if count == 4:
                sum += divisorSum
        return sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int sumFourDivisors(int* nums, int numsSize) {
    int sum = 0;
    for (int i = 0; i < numsSize; i++) {
        int count = 0;
        int divisorSum = 0;
        for (int j = 1; j * j <= nums[i]; j++) {
            if (nums[i] % j == 0) {
                count++;
                divisorSum += j;
                if (j * j != nums[i]) {
                    count++;
                    divisorSum += nums[i] / j;
                }
            }
        }
        if (count == 4) {
            sum += divisorSum;
        }
    }
    return sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int SumFourDivisors(int[] nums) {
        int sum = 0;
        foreach (int num in nums) {
            List<int> divisors = new List<int>();
            for (int i = 1; i <= Math.Sqrt(num); i++) {
                if (num % i == 0) {
                    divisors.Add(i);
                    if (i != num / i) divisors.Add(num / i);
                }
            }
            if (divisors.Count == 4) {
                sum += divisors.Sum();
            }
        }
        return sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var sumFourDivisors = function(nums) {
    let sum = 0;
    for (let num of nums) {
        let divisors = [];
        for (let i = 1; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                divisors.push(i);
                if (i != num / i) divisors.push(num / i);
            }
        }
        if (divisors.length == 4) {
            sum += divisors.reduce((a, b) => a + b, 0);
        }
    }
    return sum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sumFourDivisors(nums: number[]): number {
    let sum = 0;
    for (let num of nums) {
        let divisors: number[] = [];
        for (let i = 1; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                divisors.push(i);
                if (i != num / i) divisors.push(num / i);
            }
        }
        if (divisors.length == 4) {
            sum += divisors.reduce((a, b) => a + b, 0);
        }
    }
    return sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function sumFourDivisors($nums) {
        $sum = 0;
        foreach ($nums as $num) {
            $divisors = [];
            for ($i = 1; $i <= sqrt($num); $i++) {
                if ($num % $i == 0) {
                    $divisors[] = $i;
                    if ($i != $num / $i) $divisors[] = $num / $i;
                }
            }
            if (count($divisors) == 4) {
                $sum += array_sum($divisors);
            }
        }
        return $sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sumFourDivisors(_ nums: [Int]) -> Int {
        var sum = 0
        for num in nums {
            var divisors: [Int] = []
            for i in 1...Int(sqrt(Double(num))) {
                if num % i == 0 {
                    divisors.append(i)
                    if i != num / i {
                        divisors.append(num / i)
                    }
                }
            }
            if divisors.count == 4 {
                sum += divisors.reduce(0, +)
            }
        }
        return sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun sumFourDivisors(nums: IntArray): Int {
        var sum = 0
        for (num in nums) {
            var divisors = 0
            var divSum = 0
            for (i in 1..Math.sqrt(num.toDouble()).toInt()) {
                if (num % i == 0) {
                    if (num / i == i) {
                        divisors++
                        divSum += i
                    } else {
                        divisors += 2
                        divSum += i + num / i
                    }
                }
                if (divisors > 4) break
            }
            if (divisors == 4) sum += divSum
        }
        return sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int sumFourDivisors(List<int> nums) {
    int sum = 0;
    for (int num in nums) {
      int divisors = 0;
      int divSum = 0;
      for (int i = 1; i <= num.sqrt().floor(); i++) {
        if (num % i == 0) {
          if (num / i == i) {
            divisors++;
            divSum += i;
          } else {
            divisors += 2;
            divSum += i + num / i;
          }
        }
        if (divisors > 4) break;
      }
      if (divisors == 4) sum += divSum;
    }
    return sum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func sumFourDivisors(nums []int) int {
    sum := 0
    for _, num := range nums {
        divisors := 0
        divSum := 0
        for i := 1; i <= int(math.Sqrt(float64(num))); i++ {
            if num % i == 0 {
                if num / i == i {
                    divisors++
                    divSum += i
                } else {
                    divisors += 2
                    divSum += i + num / i
                }
            }
            if divisors > 4 {
                break
            }
        }
        if divisors == 4 {
            sum += divSum
        }
    }
    return sum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def sum_four_divisors(nums)
    sum = 0
    nums.each do |num|
        divisors = 0
        div_sum = 0
        (1..Math.sqrt(num).to_i).each do |i|
            if num % i == 0
                if num / i == i
                    divisors += 1
                    div_sum += i
                else
                    divisors += 2
                    div_sum += i + num / i
                end
            end
            break if divisors > 4
        end
        sum += div_sum if divisors == 4
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
    def sumFourDivisors(nums: Array[Int]): Int = {
        var sum = 0
        for (num <- nums) {
            var divisors = 0
            var divSum = 0
            for (i <- 1 to Math.sqrt(num).toInt) {
                if (num % i == 0) {
                    if (num / i == i) {
                        divisors += 1
                        divSum += i
                    } else {
                        divisors += 2
                        divSum += i + num / i
                    }
                }
                if (divisors > 4) {
                    i = Int.MaxValue
                }
            }
            if (divisors == 4) sum += divSum
        }
        sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        let mut sum = 0;
        for num in nums {
            let mut divisors = Vec::new();
            for i in 1..=(num as f64).sqrt() as i32 {
                if num % i == 0 {
                    divisors.push(i);
                    if i * i != num {
                        divisors.push(num / i);
                    }
                }
            }
            if divisors.len() == 4 {
                sum += divisors.iter().sum::<i32>();
            }
        }
        sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sum-four-divisors nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([sum 0])
    (for ([num nums])
      (let ([divisors (for/list ([i (in-range 1 (add1 (sqrt num)))])
                         (if (zero? (remainder num i))
                             (list i (quotient num i))
                             '()))])
        (if (= (length (flatten divisors)) 4)
            (set! sum (+ sum (apply + (flatten divisors))))))
    sum))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
sum_four_divisors(Nums) ->
  lists:foldl(fun (Num, Sum) ->
                    Divisors = [I || I <- lists:seq(1, trunc(math:sqrt(Num))), Num rem I == 0],
                    case length(Divisors) of
                      4 -> Sum + lists:sum([I || I <- Divisors] ++ [Num div I || I <- Divisors, I * I /= Num]);
                      _ -> Sum
                    end
                end, 0, Nums).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sum_four_divisors(nums :: [integer]) :: integer
  def sum_four_divisors(nums) do
    Enum.reduce(nums, 0, fn num, sum ->
      divisors = Enum.flat_map(1..:math.sqrt(num), fn i ->
        if rem(num, i) == 0 do
          if i * i == num, do: [i], else: [i, div(num, i)]
        else
          []
        end
      end)
      if length(divisors) == 4, do: sum + Enum.sum(divisors), else: sum
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n*sqrt(m)), where n is the number of elements in the input array and m is the maximum value in the array. This is because for each number in the array, we are iterating up to its square root to find its divisors.

- **Space Complexity:** The space complexity of this solution is O(1), as we are only using a constant amount of space to store the total sum and the divisors of each number. We are not using any data structures that scale with the input size.

</div>
</details>
