---
layout: post
title: "Maximum Matrix Sum"
date: 2026-01-05 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-matrix-sum/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxMatrixSum(std::vector<std::vector<int>>&\
        \ matrix) {\n        long long total_abs_sum = 0;\n        int negative_count\
        \ = 0;\n        int min_val_abs = 100001; // Constraints: -10^5 <= matrix[i][j]\
        \ <= 10^5\n\n        for (const auto& row : matrix) {\n            for (int\
        \ x : row) {\n                total_abs_sum += std::abs(x);\n              \
        \  if (x < 0) {\n                    negative_count++;\n                }\n\
        \                min_val_abs = std::min(min_val_abs, std::abs(x));\n       \
        \     }\n        }\n\n        if (negative_count % 2 == 0) {\n            return\
        \ total_abs_sum;\n        } else {\n            return total_abs_sum - 2 * min_val_abs;\n\
        \        }\n    }\n};"
      java: "class Solution {\n    public long maxMatrixSum(int[][] matrix) {\n    \
        \    long totalAbsSum = 0;\n        int negativeCount = 0;\n        int minValAbs\
        \ = 100001; // Constraints: -10^5 <= matrix[i][j] <= 10^5\n\n        for (int[]\
        \ row : matrix) {\n            for (int x : row) {\n                totalAbsSum\
        \ += Math.abs(x);\n                if (x < 0) {\n                    negativeCount++;\n\
        \                }\n                minValAbs = Math.min(minValAbs, Math.abs(x));\n\
        \            }\n        }\n\n        if (negativeCount % 2 == 0) {\n       \
        \     return totalAbsSum;\n        } else {\n            return totalAbsSum\
        \ - 2 * minValAbs;\n        }\n    }\n}"
      python: "# Failed to parse response\n# Check logs for full output.\n# Full Response:\n\
        '''\n{\n  \"approach\": \"The core insight is that the operation of multiplying\
        \ two adjacent elements by -1 allows us to effectively flip the signs of any\
        \ two arbitrary elements in the matrix, while leaving all other elements' signs\
        \ unchanged. This can be achieved by constructing a path between the two desired\
        \ elements and applying the operation sequentially along the path. For example,\
        \ to flip elements A and B, we can find a path A-X1-X2-...-Xk-B. First, flip\
        \ A and X1. Then, flip X1 and X2. Continue this process until Xk and B are flipped.\
        \ After this sequence, A and B will have their signs flipped, while all intermediate\
        \ elements X1 through Xk will have been flipped twice, returning to their original\
        \ signs.\\n\\nWith the ability to flip any two arbitrary elements, the problem\
        \ reduces to maximizing the sum. To maximize the sum, we want to make as many\
        \ elements positive as possible. We iterate through the matrix to calculate\
        \ the sum of absolute values of all elements (\\\"total_sum_abs\\\"), count\
        \ the number of negative elements (\\\"neg_count\\\"), and find the minimum\
        \ absolute value among all elements (\\\"min_abs_val\\\"). If \\\"neg_count\\\
        \" is even, we can pair up all negative numbers and flip their signs to positive,\
        \ resulting in all elements being positive. The maximum sum is \\\"total_sum_abs\\\
        \". If \\\"neg_count\\\" is odd, we can pair up \\\"neg_count - 1\\\" negative\
        \ numbers and flip them to positive, leaving exactly one negative number. To\
        \ maximize the sum in this case, we ensure this remaining negative number is\
        \ the one with the smallest absolute value. Thus, the maximum sum is \\\"total_sum_abs\
        \ - 2 * min_abs_val\\\" (since \\\"min_abs_val\\\" would have been added to\
        \ \\\"total_sum_abs\\\", but now it's negative, so we subtract \\\"2 * min_abs_val\\\
        \").\",\n  \"time_complexity\": \"The time complexity is O(n^2). We iterate\
        \ through each of the n*n elements of the matrix exactly once. For each element,\
        \ we perform constant time operations such as calculating its absolute value,\
        \ adding to a running sum, checking its sign, and comparing its absolute value\
        \ to a minimum. Therefore, the total time taken is directly proportional to\
        \ the number of elements in the matrix.\",\n  \"space_complexity\": \"The space\
        \ complexity is O(1). We only use a few constant-size variables to store the\
        \ total sum of absolute values, the count of negative numbers, and the minimum\
        \ absolute value encountered. These variables do not scale with the input size\
        \ of the matrix, hence the constant space complexity.\",\n  \"solutions\": {\n\
        \    \"rust\": \"impl Solution {\\n    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>)\
        \ -> i64 {\\n        let mut total_sum_abs: i64 = 0;\\n        let mut neg_count:\
        \ i32 = 0;\\n        let mut min_abs_val: i32 = std::i32::MAX;\\n\\n       \
        \ for row in matrix {\\n            for &val in &row {\\n                total_sum_abs\
        \ += val.abs() as i64;\\n                if val < 0 {\\n                   \
        \ neg_count += 1;\\n                }\\n                min_abs_val = min_abs_val.min(val.abs());\\\
        n            }\\n        }\\n\\n        if neg_count % 2 == 0 {\\n         \
        \   total_sum_abs\\n        } else {\\n            total_sum_abs - 2 * (min_abs_val\
        \ as i64)\\n        }\\n    }\\n}\",\n    \"racket\": \"(define/contract (max-matrix-sum\
        \ matrix)\\n  (-> (listof (listof exact-integer?)) exact-integer?)\\n  (let*\
        \ ((initial-state (list 0 0 (add1 (expt 10 5)))) ; (total-sum-abs neg-count\
        \ min-abs-val)\\n         (final-state (foldl (lambda (row acc-state)\\n   \
        \                            (foldl (lambda (val inner-acc-state)\\n       \
        \                                 (let* ((current-total-sum-abs (list-ref inner-acc-state\
        \ 0))\\n                                               (current-neg-count (list-ref\
        \ inner-acc-state 1))\\n                                               (current-min-abs-val\
        \ (list-ref inner-acc-state 2))\\n                                         \
        \      (abs-val (abs val)))\\n                                          (list\
        \ (+ current-total-sum-abs abs-val)\\n                                     \
        \           (if (< val 0) (+ current-neg-count 1) current-neg-count)\\n    \
        \                                            (min current-min-abs-val abs-val))))\\\
        n                                      acc-state\\n                        \
        \              row))\\n                              initial-state\\n      \
        \                        matrix))\\n         (total-sum-abs (list-ref final-state\
        \ 0))\\n         (neg-count (list-ref final-state 1))\\n         (min-abs-val\
        \ (list-ref final-state 2)))\\n    (if (even? neg-count)\\n        total-sum-abs\\\
        n        (- total-sum-abs (* 2 min-abs-val)))))\",\n    \"erlang\": \"-spec\
        \ max_matrix_sum(Matrix :: [[integer()]]) -> integer().\\nmax_matrix_sum(Matrix)\
        \ ->\\n    {TotalSumAbs, NegCount, MinAbsVal} = lists:foldl(\\n        fun(Row,\
        \ {AccSumAbs, AccNegCount, AccMinAbsVal}) ->\\n            lists:foldl(\\n \
        \               fun(Val, {InnerAccSumAbs, InnerAccNegCount, InnerAccMinAbsVal})\
        \ ->\\n                    AbsVal = abs(Val),\\n                    NewNegCount\
        \ = if Val < 0 -> InnerAccNegCount + 1; true -> InnerAccNegCount end,\\n   \
        \                 {InnerAccSumAbs + AbsVal, NewNegCount, min(InnerAccMinAbsVal,\
        \ AbsVal)}\\n                end,\\n                {AccSumAbs, AccNegCount,\
        \ AccMinAbsVal},\\n                Row\\n            )\\n        end,\\n   \
        \     {0, 0, 100001}, % Initial state: {TotalSumAbs, NegCount, MinAbsVal}\\\
        n        Matrix\\n    ),\\n    if\\n        NegCount rem 2 == 0 ->\\n      \
        \      TotalSumAbs;\\n        true ->\\n            TotalSumAbs - 2 * MinAbsVal\\\
        n    end.\",\n    \"elixir\": \"defmodule Solution do\\n  @spec max_matrix_sum(matrix\
        \ :: [[integer]]) :: integer\\n  def max_matrix_sum(matrix) do\\n    {total_sum_abs,\
        \ neg_count, min_abs_val} = \\n      Enum.reduce(matrix, {0, 0, 100_001}, fn\
        \ row, {acc_sum_abs, acc_neg_count, acc_min_abs_val} ->\\n        Enum.reduce(row,\
        \ {acc_sum_abs, acc_neg_count, acc_min_abs_val}, fn val, {inner_acc_sum_abs,\
        \ inner_acc_neg_count, inner_acc_min_abs_val} ->\\n          abs_val = abs(val)\\\
        n          new_neg_count = if val < 0, do: inner_acc_neg_count + 1, else: inner_acc_neg_count\\\
        n          {inner_acc_sum_abs + abs_val, new_neg_count, min(inner_acc_min_abs_val,\
        \ abs_val)}\\n        end)\\n      end)\\n\\n    if rem(neg_count, 2) == 0 do\\\
        n      total_sum_abs\\n    else\\n      total_sum_abs - 2 * min_abs_val\\n \
        \   end\\n  end\\nend\"\n}\n'''"
      python3: "class Solution:\n    def maxMatrixSum(self, matrix: List[List[int]])\
        \ -> int:\n        total_abs_sum = 0\n        negative_count = 0\n        min_val_abs\
        \ = float('inf')\n\n        for row in matrix:\n            for x in row:\n\
        \                total_abs_sum += abs(x)\n                if x < 0:\n      \
        \              negative_count += 1\n                min_val_abs = min(min_val_abs,\
        \ abs(x))\n\n        if negative_count % 2 == 0:\n            return total_abs_sum\n\
        \        else:\n            return total_abs_sum - 2 * min_val_abs"
      c: "long long maxMatrixSum(int** matrix, int matrixSize, int* matrixColSize) {\n\
        \    long long total_abs_sum = 0;\n    int negative_count = 0;\n    int min_val_abs\
        \ = 100001; // Constraints: -10^5 <= matrix[i][j] <= 10^5\n\n    for (int i\
        \ = 0; i < matrixSize; i++) {\n        for (int j = 0; j < matrixColSize[i];\
        \ j++) {\n            int x = matrix[i][j];\n            total_abs_sum += abs(x);\n\
        \            if (x < 0) {\n                negative_count++;\n            }\n\
        \            if (abs(x) < min_val_abs) {\n                min_val_abs = abs(x);\n\
        \            }\n        }\n    }\n\n    if (negative_count % 2 == 0) {\n   \
        \     return total_abs_sum;\n    } else {\n        return total_abs_sum - 2\
        \ * min_val_abs;\n    }\n}"
      csharp: "public class Solution {\n    public long MaxMatrixSum(int[][] matrix)\
        \ {\n        long sumAbs = 0;\n        int negCount = 0;\n        int minAbsVal\
        \ = int.MaxValue;\n\n        foreach (int[] row in matrix) {\n            foreach\
        \ (int val in row) {\n                sumAbs += Math.Abs(val);\n           \
        \     if (val < 0) {\n                    negCount++;\n                }\n \
        \               minAbsVal = Math.Min(minAbsVal, Math.Abs(val));\n          \
        \  }\n        }\n\n        if (negCount % 2 == 0) {\n            return sumAbs;\n\
        \        } else {\n            return sumAbs - 2 * minAbsVal;\n        }\n \
        \   }\n}"
      javascript: "/**\n * @param {number[][]} matrix\n * @return {number}\n */\nvar\
        \ maxMatrixSum = function(matrix) {\n    let sumAbs = 0;\n    let negCount =\
        \ 0;\n    let minAbsVal = Infinity;\n\n    for (let i = 0; i < matrix.length;\
        \ i++) {\n        for (let j = 0; j < matrix[i].length; j++) {\n           \
        \ const val = matrix[i][j];\n            sumAbs += Math.abs(val);\n        \
        \    if (val < 0) {\n                negCount++;\n            }\n          \
        \  minAbsVal = Math.min(minAbsVal, Math.abs(val));\n        }\n    }\n\n   \
        \ if (negCount % 2 === 0) {\n        return sumAbs;\n    } else {\n        return\
        \ sumAbs - 2 * minAbsVal;\n    }\n};"
      typescript: "function maxMatrixSum(matrix: number[][]): number {\n    let sumAbs:\
        \ number = 0;\n    let negCount: number = 0;\n    let minAbsVal: number = Infinity;\n\
        \n    for (let i = 0; i < matrix.length; i++) {\n        for (let j = 0; j <\
        \ matrix[i].length; j++) {\n            const val = matrix[i][j];\n        \
        \    sumAbs += Math.abs(val);\n            if (val < 0) {\n                negCount++;\n\
        \            }\n            minAbsVal = Math.min(minAbsVal, Math.abs(val));\n\
        \        }\n    }\n\n    if (negCount % 2 === 0) {\n        return sumAbs;\n\
        \    } else {\n        return sumAbs - 2 * minAbsVal;\n    }\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $matrix\n     * @return\
        \ Integer\n     */\n    function maxMatrixSum($matrix) {\n        $sumAbs =\
        \ 0;\n        $negCount = 0;\n        $minAbsVal = PHP_INT_MAX;\n\n        foreach\
        \ ($matrix as $row) {\n            foreach ($row as $val) {\n              \
        \  $sumAbs += abs($val);\n                if ($val < 0) {\n                \
        \    $negCount++;\n                }\n                $minAbsVal = min($minAbsVal,\
        \ abs($val));\n            }\n        }\n\n        if ($negCount % 2 === 0)\
        \ {\n            return $sumAbs;\n        } else {\n            return $sumAbs\
        \ - 2 * $minAbsVal;\n        }\n    }\n}"
      swift: "class Solution {\n    func maxMatrixSum(_ matrix: [[Int]]) -> Int {\n\
        \        var sumAbs: Int = 0\n        var negCount: Int = 0\n        var minAbsVal:\
        \ Int = Int.max\n\n        for row in matrix {\n            for val in row {\n\
        \                sumAbs += abs(val)\n                if val < 0 {\n        \
        \            negCount += 1\n                }\n                minAbsVal = min(minAbsVal,\
        \ abs(val))\n            }\n        }\n\n        if negCount % 2 == 0 {\n  \
        \          return sumAbs\n        } else {\n            return sumAbs - 2 *\
        \ minAbsVal\n        }\n    }\n}"
      kotlin: "class Solution {\n    fun maxMatrixSum(matrix: Array<IntArray>): Long\
        \ {\n        var totalSum: Long = 0\n        var negativeCount = 0\n       \
        \ var minAbsValue = Long.MAX_VALUE\n\n        for (row in matrix) {\n      \
        \      for (element in row) {\n                val absElement = Math.abs(element).toLong()\n\
        \                totalSum += absElement\n                if (element < 0) {\n\
        \                    negativeCount++\n                }\n                if\
        \ (absElement < minAbsValue) {\n                    minAbsValue = absElement\n\
        \                }\n            }\n        }\n\n        if (negativeCount %\
        \ 2 == 0) {\n            return totalSum\n        } else {\n            return\
        \ totalSum - 2 * minAbsValue\n        }\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maxMatrixSum(List<List<int>>\
        \ matrix) {\n    int totalSum = 0;\n    int negativeCount = 0;\n    int minAbsValue\
        \ = 100001; // Constraints: -10^5 <= matrix[i][j] <= 10^5\n\n    for (var row\
        \ in matrix) {\n      for (var element in row) {\n        int absElement = element.abs();\n\
        \        totalSum += absElement;\n        if (element < 0) {\n          negativeCount++;\n\
        \        }\n        if (absElement < minAbsValue) {\n          minAbsValue =\
        \ absElement;\n        }\n      }\n    }\n\n    if (negativeCount % 2 == 0)\
        \ {\n      return totalSum;\n    } else {\n      return totalSum - 2 * minAbsValue;\n\
        \    }\n  }\n}"
      go: "import \"math\"\n\nfunc maxMatrixSum(matrix [][]int) int64 {\n    var totalSum\
        \ int64 = 0\n    var negativeCount int = 0\n    var minAbsValue int64 = math.MaxInt64\n\
        \n    for _, row := range matrix {\n        for _, element := range row {\n\
        \            absElement := int64(math.Abs(float64(element)))\n            totalSum\
        \ += absElement\n            if element < 0 {\n                negativeCount++\n\
        \            }\n            if absElement < minAbsValue {\n                minAbsValue\
        \ = absElement\n            }\n        }\n    }\n\n    if negativeCount % 2\
        \ == 0 {\n        return totalSum\n    } else {\n        return totalSum - 2\
        \ * minAbsValue\n    }\n}"
      ruby: "# @param {Integer[][]} matrix\n# @return {Integer}\ndef max_matrix_sum(matrix)\n\
        \    total_sum = 0\n    negative_count = 0\n    min_abs_value = Float::INFINITY\n\
        \n    matrix.each do |row|\n        row.each do |element|\n            abs_element\
        \ = element.abs\n            total_sum += abs_element\n            if element\
        \ < 0\n                negative_count += 1\n            end\n            if\
        \ abs_element < min_abs_value\n                min_abs_value = abs_element\n\
        \            end\n        end\n    end\n\n    if negative_count % 2 == 0\n \
        \       return total_sum\n    else\n        return total_sum - 2 * min_abs_value\n\
        \    end\nend"
      scala: "object Solution {\n    def maxMatrixSum(matrix: Array[Array[Int]]): Long\
        \ = {\n        var totalSum: Long = 0\n        var negativeCount: Int = 0\n\
        \        var minAbsValue: Long = Long.MaxValue\n\n        for (row <- matrix)\
        \ {\n            for (element <- row) {\n                val absElement = Math.abs(element).toLong\n\
        \                totalSum += absElement\n                if (element < 0) {\n\
        \                    negativeCount += 1\n                }\n               \
        \ if (absElement < minAbsValue) {\n                    minAbsValue = absElement\n\
        \                }\n            }\n        }\n\n        if (negativeCount %\
        \ 2 == 0) {\n            totalSum\n        } else {\n            totalSum -\
        \ 2 * minAbsValue\n        }\n    }\n}"
    approach: 'The core insight lies in understanding the effect of the operation: choosing
      two adjacent elements and multiplying each by -1. This operation always flips
      the signs of exactly two elements. Consequently, the parity of the total number
      of negative elements in the matrix remains invariant throughout any sequence of
      operations. For example, if two positive numbers become negative, the count of
      negatives increases by two (even change). If two negative numbers become positive,
      the count decreases by two (even change). If one positive and one negative number
      flip, the count of negatives remains the same (zero change). This means if the
      initial matrix has an even number of negative elements, we can always transform
      it such that all elements are positive. If it has an odd number of negative elements,
      we will always be left with an odd number of negative elements, with the minimum
      possible being one.'
    time_complexity: The algorithm iterates through each element of the n x n matrix
      exactly once. For each element, it performs constant time operations such as calculating
      the absolute value, addition, comparison, and checking the sign. Therefore, the
      total time complexity is O(n^2), where n is the dimension of the square matrix.
    space_complexity: The algorithm uses a fixed number of variables to store the sum
      of absolute values, the count of negative numbers, and the minimum absolute value
      found. These variables consume a constant amount of memory regardless of the input
      matrix size. Thus, the space complexity is O(1).
    elapsed_time: 114.09570360183716
    model: gemini-2.5-flash
    generated_at: '2026-01-05 01:17:05 '
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxMatrixSum(vector<vector<int>>&\
        \ matrix) {\n        long long sum = 0;\n        int count = 0;\n        int\
        \ minVal = INT_MAX;\n        for (int i = 0; i < matrix.size(); i++) {\n   \
        \         for (int j = 0; j < matrix[i].size(); j++) {\n                if (matrix[i][j]\
        \ < 0) {\n                    count++;\n                }\n                sum\
        \ += abs(matrix[i][j]);\n                minVal = min(minVal, abs(matrix[i][j]));\n\
        \            }\n        }\n        if (count % 2 == 1) {\n            sum -=\
        \ 2 * minVal;\n        }\n        return sum;\n    }\n};"
      java: "class Solution {\n    public long maxMatrixSum(int[][] matrix) {\n    \
        \    long sum = 0;\n        int count = 0;\n        int minVal = Integer.MAX_VALUE;\n\
        \        for (int i = 0; i < matrix.length; i++) {\n            for (int j =\
        \ 0; j < matrix[i].length; j++) {\n                if (matrix[i][j] < 0) {\n\
        \                    count++;\n                }\n                sum += Math.abs(matrix[i][j]);\n\
        \                minVal = Math.min(minVal, Math.abs(matrix[i][j]));\n      \
        \      }\n        }\n        if (count % 2 == 1) {\n            sum -= 2 * minVal;\n\
        \        }\n        return sum;\n    }\n}"
      python: "class Solution:\n    def maxMatrixSum(self, matrix):\n        sum_val\
        \ = 0\n        count = 0\n        min_val = float('inf')\n        for row in\
        \ matrix:\n            for num in row:\n                if num < 0:\n      \
        \              count += 1\n                sum_val += abs(num)\n           \
        \     min_val = min(min_val, abs(num))\n        if count % 2 == 1:\n       \
        \     sum_val -= 2 * min_val\n        return sum_val"
      python3: "class Solution:\n    def maxMatrixSum(self, matrix: list[list[int]])\
        \ -> int:\n        sum_val = 0\n        count = 0\n        min_val = float('inf')\n\
        \        for row in matrix:\n            for num in row:\n                if\
        \ num < 0:\n                    count += 1\n                sum_val += abs(num)\n\
        \                min_val = min(min_val, abs(num))\n        if count % 2 == 1:\n\
        \            sum_val -= 2 * min_val\n        return sum_val"
      c: "long long maxMatrixSum(int** matrix, int matrixSize, int* matrixColSize) {\n\
        \    long long sum = 0;\n    int count = 0;\n    int minVal = INT_MAX;\n   \
        \ for (int i = 0; i < matrixSize; i++) {\n        for (int j = 0; j < matrixColSize[i];\
        \ j++) {\n            if (matrix[i][j] < 0) {\n                count++;\n  \
        \          }\n            sum += abs(matrix[i][j]);\n            minVal = (minVal\
        \ < abs(matrix[i][j])) ? minVal : abs(matrix[i][j]);\n        }\n    }\n   \
        \ if (count % 2 == 1) {\n        sum -= 2 * minVal;\n    }\n    return sum;\n\
        }"
      csharp: "public class Solution {\n    public long MaxMatrixSum(int[][] matrix)\
        \ {\n        int n = matrix.Length;\n        int negativeCount = 0;\n      \
        \  long sum = 0;\n        int min = int.MaxValue;\n        for (int i = 0; i\
        \ < n; i++) {\n            for (int j = 0; j < n; j++) {\n                if\
        \ (matrix[i][j] < 0) {\n                    negativeCount++;\n             \
        \   }\n                sum += Math.Abs(matrix[i][j]);\n                min =\
        \ Math.Min(min, Math.Abs(matrix[i][j]));\n            }\n        }\n       \
        \ if (negativeCount % 2 == 1) {\n            sum -= 2 * min;\n        }\n  \
        \      return sum;\n    }\n}"
      javascript: "var maxMatrixSum = function(matrix) {\n    let n = matrix.length;\n\
        \    let negativeCount = 0;\n    let sum = 0;\n    let min = Infinity;\n   \
        \ for (let i = 0; i < n; i++) {\n        for (let j = 0; j < n; j++) {\n   \
        \         if (matrix[i][j] < 0) {\n                negativeCount++;\n      \
        \      }\n            sum += Math.abs(matrix[i][j]);\n            min = Math.min(min,\
        \ Math.abs(matrix[i][j]));\n        }\n    }\n    if (negativeCount % 2 ===\
        \ 1) {\n        sum -= 2 * min;\n    }\n    return sum;\n};"
      typescript: "function maxMatrixSum(matrix: number[][]): number {\n    let n =\
        \ matrix.length;\n    let negativeCount = 0;\n    let sum = 0;\n    let min\
        \ = Infinity;\n    for (let i = 0; i < n; i++) {\n        for (let j = 0; j\
        \ < n; j++) {\n            if (matrix[i][j] < 0) {\n                negativeCount++;\n\
        \            }\n            sum += Math.abs(matrix[i][j]);\n            min\
        \ = Math.min(min, Math.abs(matrix[i][j]));\n        }\n    }\n    if (negativeCount\
        \ % 2 === 1) {\n        sum -= 2 * min;\n    }\n    return sum;\n}"
      php: "class Solution {\n    function maxMatrixSum($matrix) {\n        $n = count($matrix);\n\
        \        $negativeCount = 0;\n        $sum = 0;\n        $min = PHP_INT_MAX;\n\
        \        for ($i = 0; $i < $n; $i++) {\n            for ($j = 0; $j < $n; $j++)\
        \ {\n                if ($matrix[$i][$j] < 0) {\n                    $negativeCount++;\n\
        \                }\n                $sum += abs($matrix[$i][$j]);\n        \
        \        $min = min($min, abs($matrix[$i][$j]));\n            }\n        }\n\
        \        if ($negativeCount % 2 == 1) {\n            $sum -= 2 * $min;\n   \
        \     }\n        return $sum;\n    }\n}"
      swift: "class Solution {\n    func maxMatrixSum(_ matrix: [[Int]]) -> Int {\n\
        \        let n = matrix.count\n        var negativeCount = 0\n        var sum\
        \ = 0\n        var min = Int.max\n        for i in 0..<n {\n            for\
        \ j in 0..<n {\n                if matrix[i][j] < 0 {\n                    negativeCount\
        \ += 1\n                }\n                sum += abs(matrix[i][j])\n      \
        \          min = min(min, abs(matrix[i][j]))\n            }\n        }\n   \
        \     if negativeCount % 2 == 1 {\n            sum -= 2 * min\n        }\n \
        \       return sum\n    }\n}"
      kotlin: "class Solution {\n    fun maxMatrixSum(matrix: Array<IntArray>): Long\
        \ {\n        var count = 0\n        var sum = 0L\n        var min = Long.MAX_VALUE\n\
        \        for (i in matrix.indices) {\n            for (j in matrix[i].indices)\
        \ {\n                val num = matrix[i][j].toLong()\n                if (num\
        \ < 0) count++\n                sum += kotlin.math.abs(num)\n              \
        \  min = kotlin.math.min(min, kotlin.math.abs(num))\n            }\n       \
        \ }\n        return if (count % 2 == 1) sum - 2 * min else sum\n    }\n}"
      dart: "class Solution {\n  int maxMatrixSum(List<List<int>> matrix) {\n    int\
        \ count = 0;\n    int sum = 0;\n    int min = int.maxFinite;\n    for (var row\
        \ in matrix) {\n      for (var num in row) {\n        if (num < 0) count++;\n\
        \        sum += num.abs();\n        min = min < num.abs() ? min : num.abs();\n\
        \      }\n    }\n    return count % 2 == 1 ? sum - 2 * min : sum;\n  }\n}"
      go: "func maxMatrixSum(matrix [][]int) int64 {\n    count := 0\n    sum := int64(0)\n\
        \    min := int64(1e9)\n    for _, row := range matrix {\n        for _, num\
        \ := range row {\n            if num < 0 {\n                count++\n      \
        \      }\n            sum += int64(abs(num))\n            min = minInt64(min,\
        \ int64(abs(num)))\n        }\n    }\n    if count%2 == 1 {\n        return\
        \ sum - 2*min\n    }\n    return sum\n}\n\nfunc abs(x int) int {\n    if x <\
        \ 0 {\n        return -x\n    }\n    return x\n}\n\nfunc minInt64(a, b int64)\
        \ int64 {\n    if a < b {\n        return a\n    }\n    return b\n}"
      ruby: "def max_matrix_sum(matrix)\n    count = 0\n    sum = 0\n    min = Float::INFINITY\n\
        \    matrix.each do |row|\n        row.each do |num|\n            if num < 0\n\
        \                count += 1\n            end\n            sum += num.abs\n \
        \           min = [min, num.abs].min\n        end\n    end\n    if count % 2\
        \ == 1\n        sum - 2 * min\n    else\n        sum\n    end\nend"
      scala: "object Solution {\n    def maxMatrixSum(matrix: Array[Array[Int]]): Long\
        \ = {\n        var count = 0\n        var sum = 0L\n        var min = Long.MaxValue\n\
        \        for (row <- matrix) {\n            for (num <- row) {\n           \
        \     if (num < 0) count += 1\n                sum += num.abs.toLong\n     \
        \           min = min min num.abs.toLong\n            }\n        }\n       \
        \ if (count % 2 == 1) sum - 2 * min else sum\n    }\n}"
      rust: "impl Solution {\n    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64\
        \ {\n        let mut neg_count = 0;\n        let mut sum = 0;\n        let mut\
        \ min_abs = i32::MAX;\n        for row in matrix {\n            for num in row\
        \ {\n                if num < 0 {\n                    neg_count += 1;\n   \
        \             }\n                sum += num.abs() as i64;\n                min_abs\
        \ = min_abs.min(num.abs());\n            }\n        }\n        if neg_count\
        \ % 2 == 0 {\n            sum\n        } else {\n            sum - 2 * min_abs\
        \ as i64\n        }\n    }\n}"
      racket: "(define/contract (max-matrix-sum matrix)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* (\n    [neg-count (foldl (lambda (x y) (+ x (if (<\
        \ y 0) 1 0))) 0 (apply append matrix))]\n    [sum (foldl (lambda (x y) (+ x\
        \ (abs y))) 0 (apply append matrix))]\n    [min-abs (foldl (lambda (x y) (min\
        \ x (abs y))) (expt 2 31) (apply append matrix))]\n    )\n    (if (even? neg-count)\n\
        \        sum\n        (- sum (* 2 min-abs))\n    )\n  )\n)"
      erlang: "max_matrix_sum(Matrix) ->\n  NegCount = lists:foldl(fun(X, Sum) -> Sum\
        \ + case X < 0 of true -> 1; false -> 0 end end, 0, lists:flatten(Matrix)),\n\
        \  Sum = lists:foldl(fun(X, Sum) -> Sum + abs(X) end, 0, lists:flatten(Matrix)),\n\
        \  MinAbs = lists:foldl(fun(X, Min) -> min(Min, abs(X)) end, 100000, lists:flatten(Matrix)),\n\
        \  case NegCount rem 2 of\n    0 -> Sum;\n    _ -> Sum - 2 * MinAbs\n  end."
      elixir: "defmodule Solution do\n  @spec max_matrix_sum(matrix :: [[integer]])\
        \ :: integer\n  def max_matrix_sum(matrix) do\n    neg_count = Enum.reduce(List.flatten(matrix),\
        \ 0, fn x, sum -> if x < 0, do: sum + 1, else: sum end)\n    sum = Enum.reduce(List.flatten(matrix),\
        \ 0, fn x, sum -> sum + abs(x) end)\n    min_abs = Enum.reduce(List.flatten(matrix),\
        \ :infinity, fn x, min -> min(min, abs(x)) end)\n    if rem(neg_count, 2) ==\
        \ 0, do: sum, else: sum - 2 * min_abs\n  end\nend"
    approach: The problem can be solved by first counting the number of negative numbers
      in the matrix and calculating the sum of the absolute values of all numbers. If
      the count of negative numbers is even, the maximum sum is the sum of the absolute
      values. If the count is odd, we need to find the smallest absolute value and subtract
      it twice from the sum of the absolute values to get the maximum sum. This is because
      we can flip all but one negative number to positive, and the smallest absolute
      value will be the one that we cannot flip to positive. The key intuition is that
      flipping two adjacent numbers does not change the parity of the count of negative
      numbers, so we can always flip all but one negative number to positive if the
      count is odd.
    time_complexity: The time complexity is O(n^2) where n is the size of the matrix.
      This is because we need to iterate over the matrix once to count the number of
      negative numbers, calculate the sum of the absolute values, and find the smallest
      absolute value.
    space_complexity: The space complexity is O(1) because we only use a constant amount
      of space to store the count of negative numbers, the sum of the absolute values,
      and the smallest absolute value. We do not use any data structures that scale
      with the size of the input.
    elapsed_time: 9.921552658081055
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-05 01:17:30 '
---

## Problem #1975: Maximum Matrix Sum

**Difficulty:** Medium

**Topics:** Array, Greedy, Matrix

## Problem Description

<p>You are given an <code>n x n</code> integer <code>matrix</code>. You can do the following operation <strong>any</strong> number of times:</p>

<ul>
	<li>Choose any two <strong>adjacent</strong> elements of <code>matrix</code> and <strong>multiply</strong> each of them by <code>-1</code>.</li>
</ul>

<p>Two elements are considered <strong>adjacent</strong> if and only if they share a <strong>border</strong>.</p>

<p>Your goal is to <strong>maximize</strong> the summation of the matrix&#39;s elements. Return <em>the <strong>maximum</strong> sum of the matrix&#39;s elements using the operation mentioned above.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex1.png" style="width: 401px; height: 81px;" />
<pre>
<strong>Input:</strong> matrix = [[1,-1],[-1,1]]
<strong>Output:</strong> 4
<b>Explanation:</b> We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex2.png" style="width: 321px; height: 121px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
<strong>Output:</strong> 16
<b>Explanation:</b> We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == matrix.length == matrix[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 250</code></li>
	<li><code>-10<sup>5</sup> &lt;= matrix[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Try to use the operation so that each row has only one negative number.

2. If you have only one negative element you cannot convert it to positive.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-05 01:17:05 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The core insight lies in understanding the effect of the operation: choosing two adjacent elements and multiplying each by -1. This operation always flips the signs of exactly two elements. Consequently, the parity of the total number of negative elements in the matrix remains invariant throughout any sequence of operations. For example, if two positive numbers become negative, the count of negatives increases by two (even change). If two negative numbers become positive, the count decreases by two (even change). If one positive and one negative number flip, the count of negatives remains the same (zero change). This means if the initial matrix has an even number of negative elements, we can always transform it such that all elements are positive. If it has an odd number of negative elements, we will always be left with an odd number of negative elements, with the minimum possible being one.

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
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    long long maxMatrixSum(std::vector<std::vector<int>>& matrix) {
        long long total_abs_sum = 0;
        int negative_count = 0;
        int min_val_abs = 100001; // Constraints: -10^5 <= matrix[i][j] <= 10^5

        for (const auto& row : matrix) {
            for (int x : row) {
                total_abs_sum += std::abs(x);
                if (x < 0) {
                    negative_count++;
                }
                min_val_abs = std::min(min_val_abs, std::abs(x));
            }
        }

        if (negative_count % 2 == 0) {
            return total_abs_sum;
        } else {
            return total_abs_sum - 2 * min_val_abs;
        }
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long maxMatrixSum(int[][] matrix) {
        long totalAbsSum = 0;
        int negativeCount = 0;
        int minValAbs = 100001; // Constraints: -10^5 <= matrix[i][j] <= 10^5

        for (int[] row : matrix) {
            for (int x : row) {
                totalAbsSum += Math.abs(x);
                if (x < 0) {
                    negativeCount++;
                }
                minValAbs = Math.min(minValAbs, Math.abs(x));
            }
        }

        if (negativeCount % 2 == 0) {
            return totalAbsSum;
        } else {
            return totalAbsSum - 2 * minValAbs;
        }
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
  "approach": "The core insight is that the operation of multiplying two adjacent elements by -1 allows us to effectively flip the signs of any two arbitrary elements in the matrix, while leaving all other elements' signs unchanged. This can be achieved by constructing a path between the two desired elements and applying the operation sequentially along the path. For example, to flip elements A and B, we can find a path A-X1-X2-...-Xk-B. First, flip A and X1. Then, flip X1 and X2. Continue this process until Xk and B are flipped. After this sequence, A and B will have their signs flipped, while all intermediate elements X1 through Xk will have been flipped twice, returning to their original signs.\n\nWith the ability to flip any two arbitrary elements, the problem reduces to maximizing the sum. To maximize the sum, we want to make as many elements positive as possible. We iterate through the matrix to calculate the sum of absolute values of all elements (\"total_sum_abs\"), count the number of negative elements (\"neg_count\"), and find the minimum absolute value among all elements (\"min_abs_val\"). If \"neg_count\" is even, we can pair up all negative numbers and flip their signs to positive, resulting in all elements being positive. The maximum sum is \"total_sum_abs\". If \"neg_count\" is odd, we can pair up \"neg_count - 1\" negative numbers and flip them to positive, leaving exactly one negative number. To maximize the sum in this case, we ensure this remaining negative number is the one with the smallest absolute value. Thus, the maximum sum is \"total_sum_abs - 2 * min_abs_val\" (since \"min_abs_val\" would have been added to \"total_sum_abs\", but now it's negative, so we subtract \"2 * min_abs_val\").",
  "time_complexity": "The time complexity is O(n^2). We iterate through each of the n*n elements of the matrix exactly once. For each element, we perform constant time operations such as calculating its absolute value, adding to a running sum, checking its sign, and comparing its absolute value to a minimum. Therefore, the total time taken is directly proportional to the number of elements in the matrix.",
  "space_complexity": "The space complexity is O(1). We only use a few constant-size variables to store the total sum of absolute values, the count of negative numbers, and the minimum absolute value encountered. These variables do not scale with the input size of the matrix, hence the constant space complexity.",
  "solutions": {
    "rust": "impl Solution {\n    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {\n        let mut total_sum_abs: i64 = 0;\n        let mut neg_count: i32 = 0;\n        let mut min_abs_val: i32 = std::i32::MAX;\n\n        for row in matrix {\n            for &val in &row {\n                total_sum_abs += val.abs() as i64;\n                if val < 0 {\n                    neg_count += 1;\n                }\n                min_abs_val = min_abs_val.min(val.abs());\n            }\n        }\n\n        if neg_count % 2 == 0 {\n            total_sum_abs\n        } else {\n            total_sum_abs - 2 * (min_abs_val as i64)\n        }\n    }\n}",
    "racket": "(define/contract (max-matrix-sum matrix)\n  (-> (listof (listof exact-integer?)) exact-integer?)\n  (let* ((initial-state (list 0 0 (add1 (expt 10 5)))) ; (total-sum-abs neg-count min-abs-val)\n         (final-state (foldl (lambda (row acc-state)\n                               (foldl (lambda (val inner-acc-state)\n                                        (let* ((current-total-sum-abs (list-ref inner-acc-state 0))\n                                               (current-neg-count (list-ref inner-acc-state 1))\n                                               (current-min-abs-val (list-ref inner-acc-state 2))\n                                               (abs-val (abs val)))\n                                          (list (+ current-total-sum-abs abs-val)\n                                                (if (< val 0) (+ current-neg-count 1) current-neg-count)\n                                                (min current-min-abs-val abs-val))))\n                                      acc-state\n                                      row))\n                              initial-state\n                              matrix))\n         (total-sum-abs (list-ref final-state 0))\n         (neg-count (list-ref final-state 1))\n         (min-abs-val (list-ref final-state 2)))\n    (if (even? neg-count)\n        total-sum-abs\n        (- total-sum-abs (* 2 min-abs-val)))))",
    "erlang": "-spec max_matrix_sum(Matrix :: [[integer()]]) -> integer().\nmax_matrix_sum(Matrix) ->\n    {TotalSumAbs, NegCount, MinAbsVal} = lists:foldl(\n        fun(Row, {AccSumAbs, AccNegCount, AccMinAbsVal}) ->\n            lists:foldl(\n                fun(Val, {InnerAccSumAbs, InnerAccNegCount, InnerAccMinAbsVal}) ->\n                    AbsVal = abs(Val),\n                    NewNegCount = if Val < 0 -> InnerAccNegCount + 1; true -> InnerAccNegCount end,\n                    {InnerAccSumAbs + AbsVal, NewNegCount, min(InnerAccMinAbsVal, AbsVal)}\n                end,\n                {AccSumAbs, AccNegCount, AccMinAbsVal},\n                Row\n            )\n        end,\n        {0, 0, 100001}, % Initial state: {TotalSumAbs, NegCount, MinAbsVal}\n        Matrix\n    ),\n    if\n        NegCount rem 2 == 0 ->\n            TotalSumAbs;\n        true ->\n            TotalSumAbs - 2 * MinAbsVal\n    end.",
    "elixir": "defmodule Solution do\n  @spec max_matrix_sum(matrix :: [[integer]]) :: integer\n  def max_matrix_sum(matrix) do\n    {total_sum_abs, neg_count, min_abs_val} = \n      Enum.reduce(matrix, {0, 0, 100_001}, fn row, {acc_sum_abs, acc_neg_count, acc_min_abs_val} ->\n        Enum.reduce(row, {acc_sum_abs, acc_neg_count, acc_min_abs_val}, fn val, {inner_acc_sum_abs, inner_acc_neg_count, inner_acc_min_abs_val} ->\n          abs_val = abs(val)\n          new_neg_count = if val < 0, do: inner_acc_neg_count + 1, else: inner_acc_neg_count\n          {inner_acc_sum_abs + abs_val, new_neg_count, min(inner_acc_min_abs_val, abs_val)}\n        end)\n      end)\n\n    if rem(neg_count, 2) == 0 do\n      total_sum_abs\n    else\n      total_sum_abs - 2 * min_abs_val\n    end\n  end\nend"
}
'''
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_abs_sum = 0
        negative_count = 0
        min_val_abs = float('inf')

        for row in matrix:
            for x in row:
                total_abs_sum += abs(x)
                if x < 0:
                    negative_count += 1
                min_val_abs = min(min_val_abs, abs(x))

        if negative_count % 2 == 0:
            return total_abs_sum
        else:
            return total_abs_sum - 2 * min_val_abs
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long maxMatrixSum(int** matrix, int matrixSize, int* matrixColSize) {
    long long total_abs_sum = 0;
    int negative_count = 0;
    int min_val_abs = 100001; // Constraints: -10^5 <= matrix[i][j] <= 10^5

    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < matrixColSize[i]; j++) {
            int x = matrix[i][j];
            total_abs_sum += abs(x);
            if (x < 0) {
                negative_count++;
            }
            if (abs(x) < min_val_abs) {
                min_val_abs = abs(x);
            }
        }
    }

    if (negative_count % 2 == 0) {
        return total_abs_sum;
    } else {
        return total_abs_sum - 2 * min_val_abs;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MaxMatrixSum(int[][] matrix) {
        long sumAbs = 0;
        int negCount = 0;
        int minAbsVal = int.MaxValue;

        foreach (int[] row in matrix) {
            foreach (int val in row) {
                sumAbs += Math.Abs(val);
                if (val < 0) {
                    negCount++;
                }
                minAbsVal = Math.Min(minAbsVal, Math.Abs(val));
            }
        }

        if (negCount % 2 == 0) {
            return sumAbs;
        } else {
            return sumAbs - 2 * minAbsVal;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxMatrixSum = function(matrix) {
    let sumAbs = 0;
    let negCount = 0;
    let minAbsVal = Infinity;

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            const val = matrix[i][j];
            sumAbs += Math.abs(val);
            if (val < 0) {
                negCount++;
            }
            minAbsVal = Math.min(minAbsVal, Math.abs(val));
        }
    }

    if (negCount % 2 === 0) {
        return sumAbs;
    } else {
        return sumAbs - 2 * minAbsVal;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxMatrixSum(matrix: number[][]): number {
    let sumAbs: number = 0;
    let negCount: number = 0;
    let minAbsVal: number = Infinity;

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            const val = matrix[i][j];
            sumAbs += Math.abs(val);
            if (val < 0) {
                negCount++;
            }
            minAbsVal = Math.min(minAbsVal, Math.abs(val));
        }
    }

    if (negCount % 2 === 0) {
        return sumAbs;
    } else {
        return sumAbs - 2 * minAbsVal;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer
     */
    function maxMatrixSum($matrix) {
        $sumAbs = 0;
        $negCount = 0;
        $minAbsVal = PHP_INT_MAX;

        foreach ($matrix as $row) {
            foreach ($row as $val) {
                $sumAbs += abs($val);
                if ($val < 0) {
                    $negCount++;
                }
                $minAbsVal = min($minAbsVal, abs($val));
            }
        }

        if ($negCount % 2 === 0) {
            return $sumAbs;
        } else {
            return $sumAbs - 2 * $minAbsVal;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxMatrixSum(_ matrix: [[Int]]) -> Int {
        var sumAbs: Int = 0
        var negCount: Int = 0
        var minAbsVal: Int = Int.max

        for row in matrix {
            for val in row {
                sumAbs += abs(val)
                if val < 0 {
                    negCount += 1
                }
                minAbsVal = min(minAbsVal, abs(val))
            }
        }

        if negCount % 2 == 0 {
            return sumAbs
        } else {
            return sumAbs - 2 * minAbsVal
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxMatrixSum(matrix: Array<IntArray>): Long {
        var totalSum: Long = 0
        var negativeCount = 0
        var minAbsValue = Long.MAX_VALUE

        for (row in matrix) {
            for (element in row) {
                val absElement = Math.abs(element).toLong()
                totalSum += absElement
                if (element < 0) {
                    negativeCount++
                }
                if (absElement < minAbsValue) {
                    minAbsValue = absElement
                }
            }
        }

        if (negativeCount % 2 == 0) {
            return totalSum
        } else {
            return totalSum - 2 * minAbsValue
        }
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
  int maxMatrixSum(List<List<int>> matrix) {
    int totalSum = 0;
    int negativeCount = 0;
    int minAbsValue = 100001; // Constraints: -10^5 <= matrix[i][j] <= 10^5

    for (var row in matrix) {
      for (var element in row) {
        int absElement = element.abs();
        totalSum += absElement;
        if (element < 0) {
          negativeCount++;
        }
        if (absElement < minAbsValue) {
          minAbsValue = absElement;
        }
      }
    }

    if (negativeCount % 2 == 0) {
      return totalSum;
    } else {
      return totalSum - 2 * minAbsValue;
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "math"

func maxMatrixSum(matrix [][]int) int64 {
    var totalSum int64 = 0
    var negativeCount int = 0
    var minAbsValue int64 = math.MaxInt64

    for _, row := range matrix {
        for _, element := range row {
            absElement := int64(math.Abs(float64(element)))
            totalSum += absElement
            if element < 0 {
                negativeCount++
            }
            if absElement < minAbsValue {
                minAbsValue = absElement
            }
        }
    }

    if negativeCount % 2 == 0 {
        return totalSum
    } else {
        return totalSum - 2 * minAbsValue
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} matrix
# @return {Integer}
def max_matrix_sum(matrix)
    total_sum = 0
    negative_count = 0
    min_abs_value = Float::INFINITY

    matrix.each do |row|
        row.each do |element|
            abs_element = element.abs
            total_sum += abs_element
            if element < 0
                negative_count += 1
            end
            if abs_element < min_abs_value
                min_abs_value = abs_element
            end
        end
    end

    if negative_count % 2 == 0
        return total_sum
    else
        return total_sum - 2 * min_abs_value
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxMatrixSum(matrix: Array[Array[Int]]): Long = {
        var totalSum: Long = 0
        var negativeCount: Int = 0
        var minAbsValue: Long = Long.MaxValue

        for (row <- matrix) {
            for (element <- row) {
                val absElement = Math.abs(element).toLong
                totalSum += absElement
                if (element < 0) {
                    negativeCount += 1
                }
                if (absElement < minAbsValue) {
                    minAbsValue = absElement
                }
            }
        }

        if (negativeCount % 2 == 0) {
            totalSum
        } else {
            totalSum - 2 * minAbsValue
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The algorithm iterates through each element of the n x n matrix exactly once. For each element, it performs constant time operations such as calculating the absolute value, addition, comparison, and checking the sign. Therefore, the total time complexity is O(n^2), where n is the dimension of the square matrix.

- **Space Complexity:** The algorithm uses a fixed number of variables to store the sum of absolute values, the count of negative numbers, and the minimum absolute value found. These variables consume a constant amount of memory regardless of the input matrix size. Thus, the space complexity is O(1).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-05 01:17:30 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first counting the number of negative numbers in the matrix and calculating the sum of the absolute values of all numbers. If the count of negative numbers is even, the maximum sum is the sum of the absolute values. If the count is odd, we need to find the smallest absolute value and subtract it twice from the sum of the absolute values to get the maximum sum. This is because we can flip all but one negative number to positive, and the smallest absolute value will be the one that we cannot flip to positive. The key intuition is that flipping two adjacent numbers does not change the parity of the count of negative numbers, so we can always flip all but one negative number to positive if the count is odd.

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
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long sum = 0;
        int count = 0;
        int minVal = INT_MAX;
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                if (matrix[i][j] < 0) {
                    count++;
                }
                sum += abs(matrix[i][j]);
                minVal = min(minVal, abs(matrix[i][j]));
            }
        }
        if (count % 2 == 1) {
            sum -= 2 * minVal;
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
    public long maxMatrixSum(int[][] matrix) {
        long sum = 0;
        int count = 0;
        int minVal = Integer.MAX_VALUE;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] < 0) {
                    count++;
                }
                sum += Math.abs(matrix[i][j]);
                minVal = Math.min(minVal, Math.abs(matrix[i][j]));
            }
        }
        if (count % 2 == 1) {
            sum -= 2 * minVal;
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
class Solution:
    def maxMatrixSum(self, matrix):
        sum_val = 0
        count = 0
        min_val = float('inf')
        for row in matrix:
            for num in row:
                if num < 0:
                    count += 1
                sum_val += abs(num)
                min_val = min(min_val, abs(num))
        if count % 2 == 1:
            sum_val -= 2 * min_val
        return sum_val
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        sum_val = 0
        count = 0
        min_val = float('inf')
        for row in matrix:
            for num in row:
                if num < 0:
                    count += 1
                sum_val += abs(num)
                min_val = min(min_val, abs(num))
        if count % 2 == 1:
            sum_val -= 2 * min_val
        return sum_val
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long maxMatrixSum(int** matrix, int matrixSize, int* matrixColSize) {
    long long sum = 0;
    int count = 0;
    int minVal = INT_MAX;
    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < matrixColSize[i]; j++) {
            if (matrix[i][j] < 0) {
                count++;
            }
            sum += abs(matrix[i][j]);
            minVal = (minVal < abs(matrix[i][j])) ? minVal : abs(matrix[i][j]);
        }
    }
    if (count % 2 == 1) {
        sum -= 2 * minVal;
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
    public long MaxMatrixSum(int[][] matrix) {
        int n = matrix.Length;
        int negativeCount = 0;
        long sum = 0;
        int min = int.MaxValue;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] < 0) {
                    negativeCount++;
                }
                sum += Math.Abs(matrix[i][j]);
                min = Math.Min(min, Math.Abs(matrix[i][j]));
            }
        }
        if (negativeCount % 2 == 1) {
            sum -= 2 * min;
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
var maxMatrixSum = function(matrix) {
    let n = matrix.length;
    let negativeCount = 0;
    let sum = 0;
    let min = Infinity;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] < 0) {
                negativeCount++;
            }
            sum += Math.abs(matrix[i][j]);
            min = Math.min(min, Math.abs(matrix[i][j]));
        }
    }
    if (negativeCount % 2 === 1) {
        sum -= 2 * min;
    }
    return sum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxMatrixSum(matrix: number[][]): number {
    let n = matrix.length;
    let negativeCount = 0;
    let sum = 0;
    let min = Infinity;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (matrix[i][j] < 0) {
                negativeCount++;
            }
            sum += Math.abs(matrix[i][j]);
            min = Math.min(min, Math.abs(matrix[i][j]));
        }
    }
    if (negativeCount % 2 === 1) {
        sum -= 2 * min;
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
    function maxMatrixSum($matrix) {
        $n = count($matrix);
        $negativeCount = 0;
        $sum = 0;
        $min = PHP_INT_MAX;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($matrix[$i][$j] < 0) {
                    $negativeCount++;
                }
                $sum += abs($matrix[$i][$j]);
                $min = min($min, abs($matrix[$i][$j]));
            }
        }
        if ($negativeCount % 2 == 1) {
            $sum -= 2 * $min;
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
    func maxMatrixSum(_ matrix: [[Int]]) -> Int {
        let n = matrix.count
        var negativeCount = 0
        var sum = 0
        var min = Int.max
        for i in 0..<n {
            for j in 0..<n {
                if matrix[i][j] < 0 {
                    negativeCount += 1
                }
                sum += abs(matrix[i][j])
                min = min(min, abs(matrix[i][j]))
            }
        }
        if negativeCount % 2 == 1 {
            sum -= 2 * min
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
    fun maxMatrixSum(matrix: Array<IntArray>): Long {
        var count = 0
        var sum = 0L
        var min = Long.MAX_VALUE
        for (i in matrix.indices) {
            for (j in matrix[i].indices) {
                val num = matrix[i][j].toLong()
                if (num < 0) count++
                sum += kotlin.math.abs(num)
                min = kotlin.math.min(min, kotlin.math.abs(num))
            }
        }
        return if (count % 2 == 1) sum - 2 * min else sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxMatrixSum(List<List<int>> matrix) {
    int count = 0;
    int sum = 0;
    int min = int.maxFinite;
    for (var row in matrix) {
      for (var num in row) {
        if (num < 0) count++;
        sum += num.abs();
        min = min < num.abs() ? min : num.abs();
      }
    }
    return count % 2 == 1 ? sum - 2 * min : sum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxMatrixSum(matrix [][]int) int64 {
    count := 0
    sum := int64(0)
    min := int64(1e9)
    for _, row := range matrix {
        for _, num := range row {
            if num < 0 {
                count++
            }
            sum += int64(abs(num))
            min = minInt64(min, int64(abs(num)))
        }
    }
    if count%2 == 1 {
        return sum - 2*min
    }
    return sum
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func minInt64(a, b int64) int64 {
    if a < b {
        return a
    }
    return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_matrix_sum(matrix)
    count = 0
    sum = 0
    min = Float::INFINITY
    matrix.each do |row|
        row.each do |num|
            if num < 0
                count += 1
            end
            sum += num.abs
            min = [min, num.abs].min
        end
    end
    if count % 2 == 1
        sum - 2 * min
    else
        sum
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxMatrixSum(matrix: Array[Array[Int]]): Long = {
        var count = 0
        var sum = 0L
        var min = Long.MaxValue
        for (row <- matrix) {
            for (num <- row) {
                if (num < 0) count += 1
                sum += num.abs.toLong
                min = min min num.abs.toLong
            }
        }
        if (count % 2 == 1) sum - 2 * min else sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
        let mut neg_count = 0;
        let mut sum = 0;
        let mut min_abs = i32::MAX;
        for row in matrix {
            for num in row {
                if num < 0 {
                    neg_count += 1;
                }
                sum += num.abs() as i64;
                min_abs = min_abs.min(num.abs());
            }
        }
        if neg_count % 2 == 0 {
            sum
        } else {
            sum - 2 * min_abs as i64
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-matrix-sum matrix)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* (
    [neg-count (foldl (lambda (x y) (+ x (if (< y 0) 1 0))) 0 (apply append matrix))]
    [sum (foldl (lambda (x y) (+ x (abs y))) 0 (apply append matrix))]
    [min-abs (foldl (lambda (x y) (min x (abs y))) (expt 2 31) (apply append matrix))]
    )
    (if (even? neg-count)
        sum
        (- sum (* 2 min-abs))
    )
  )
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_matrix_sum(Matrix) ->
  NegCount = lists:foldl(fun(X, Sum) -> Sum + case X < 0 of true -> 1; false -> 0 end end, 0, lists:flatten(Matrix)),
  Sum = lists:foldl(fun(X, Sum) -> Sum + abs(X) end, 0, lists:flatten(Matrix)),
  MinAbs = lists:foldl(fun(X, Min) -> min(Min, abs(X)) end, 100000, lists:flatten(Matrix)),
  case NegCount rem 2 of
    0 -> Sum;
    _ -> Sum - 2 * MinAbs
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_matrix_sum(matrix :: [[integer]]) :: integer
  def max_matrix_sum(matrix) do
    neg_count = Enum.reduce(List.flatten(matrix), 0, fn x, sum -> if x < 0, do: sum + 1, else: sum end)
    sum = Enum.reduce(List.flatten(matrix), 0, fn x, sum -> sum + abs(x) end)
    min_abs = Enum.reduce(List.flatten(matrix), :infinity, fn x, min -> min(min, abs(x)) end)
    if rem(neg_count, 2) == 0, do: sum, else: sum - 2 * min_abs
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(n^2) where n is the size of the matrix. This is because we need to iterate over the matrix once to count the number of negative numbers, calculate the sum of the absolute values, and find the smallest absolute value.

- **Space Complexity:** The space complexity is O(1) because we only use a constant amount of space to store the count of negative numbers, the sum of the absolute values, and the smallest absolute value. We do not use any data structures that scale with the size of the input.

</div>
</details>
