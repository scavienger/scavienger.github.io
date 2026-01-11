---
layout: post
title: "Maximal Rectangle"
date: 2026-01-11 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming", "Stack", "Matrix", "Monotonic Stack"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximal-rectangle/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int largestRectangleArea(std::vector<int>&\
        \ heights) {\n        std::stack<int> s;\n        int max_area = 0;\n      \
        \  int n = heights.size();\n\n        for (int i = 0; i <= n; ++i) {\n     \
        \       int current_height = (i == n) ? 0 : heights[i];\n            while (!s.empty()\
        \ && heights[s.top()] >= current_height) {\n                int h = heights[s.top()];\n\
        \                s.pop();\n                int width = s.empty() ? i : i - s.top()\
        \ - 1;\n                max_area = std::max(max_area, h * width);\n        \
        \    }\n            s.push(i);\n        }\n        return max_area;\n    }\n\
        \n    int maximalRectangle(std::vector<std::vector<char>>& matrix) {\n     \
        \   if (matrix.empty() || matrix[0].empty()) {\n            return 0;\n    \
        \    }\n\n        int rows = matrix.size();\n        int cols = matrix[0].size();\n\
        \n        std::vector<int> heights(cols, 0);\n        int max_overall_area =\
        \ 0;\n\n        for (int r = 0; r < rows; ++r) {\n            for (int c = 0;\
        \ c < cols; ++c) {\n                if (matrix[r][c] == '1') {\n           \
        \         heights[c]++;\n                } else {\n                    heights[c]\
        \ = 0;\n                }\n            }\n            max_overall_area = std::max(max_overall_area,\
        \ largestRectangleArea(heights));\n        }\n\n        return max_overall_area;\n\
        \    }\n};"
      java: "import java.util.Stack;\nimport java.util.Arrays;\n\nclass Solution {\n\
        \    public int maximalRectangle(char[][] matrix) {\n        if (matrix == null\
        \ || matrix.length == 0 || matrix[0].length == 0) {\n            return 0;\n\
        \        }\n\n        int rows = matrix.length;\n        int cols = matrix[0].length;\n\
        \n        int[] heights = new int[cols];\n        int maxOverallArea = 0;\n\n\
        \        for (int r = 0; r < rows; r++) {\n            for (int c = 0; c < cols;\
        \ c++) {\n                if (matrix[r][c] == '1') {\n                    heights[c]++;\n\
        \                } else {\n                    heights[c] = 0;\n           \
        \     }\n            }\n            maxOverallArea = Math.max(maxOverallArea,\
        \ largestRectangleArea(heights));\n        }\n\n        return maxOverallArea;\n\
        \    }\n\n    private int largestRectangleArea(int[] heights) {\n        Stack<Integer>\
        \ stack = new Stack<>(); // stores indices\n        int maxArea = 0;\n     \
        \   int n = heights.length;\n\n        for (int i = 0; i <= n; i++) {\n    \
        \        int currentHeight = (i == n) ? 0 : heights[i];\n\n            while\
        \ (!stack.isEmpty() && heights[stack.peek()] >= currentHeight) {\n         \
        \       int h = heights[stack.pop()];\n                int width = stack.isEmpty()\
        \ ? i : i - stack.peek() - 1;\n                maxArea = Math.max(maxArea, h\
        \ * width);\n            }\n            stack.push(i);\n        }\n        return\
        \ maxArea;\n    }\n}"
      python: "class Solution(object):\n    def maximalRectangle(self, matrix):\n  \
        \      \"\"\"\n        :type matrix: List[List[str]]\n        :rtype: int\n\
        \        \"\"\"\n        if not matrix or not matrix[0]:\n            return\
        \ 0\n\n        rows = len(matrix)\n        cols = len(matrix[0])\n\n       \
        \ heights = [0] * cols\n        max_area = 0\n\n        def largestRectangleArea(h):\n\
        \            stack = [] # stores indices\n            current_max_area = 0\n\
        \            n = len(h)\n\n            for i in range(n + 1): # Iterate through\
        \ all bars, and an implicit 0 at the end\n                current_height = h[i]\
        \ if i < n else 0\n\n                while stack and h[stack[-1]] >= current_height:\n\
        \                    height = h[stack.pop()]\n                    width = i\
        \ if not stack else i - stack[-1] - 1\n                    current_max_area\
        \ = max(current_max_area, height * width)\n                stack.append(i)\n\
        \            return current_max_area\n\n        for r in range(rows):\n    \
        \        for c in range(cols):\n                if matrix[r][c] == '1':\n  \
        \                  heights[c] += 1\n                else:\n                \
        \    heights[c] = 0\n            max_area = max(max_area, largestRectangleArea(heights))\n\
        \n        return max_area"
      python3: "class Solution:\n    def maximalRectangle(self, matrix: List[List[str]])\
        \ -> int:\n        if not matrix or not matrix[0]:\n            return 0\n\n\
        \        rows = len(matrix)\n        cols = len(matrix[0])\n\n        heights\
        \ = [0] * cols\n        max_area = 0\n\n        def largestRectangleArea(h:\
        \ List[int]) -> int:\n            stack = [] # stores indices\n            current_max_area\
        \ = 0\n            n = len(h)\n\n            for i in range(n + 1): # Iterate\
        \ through all bars, and an implicit 0 at the end\n                current_height\
        \ = h[i] if i < n else 0\n\n                while stack and h[stack[-1]] >=\
        \ current_height:\n                    height = h[stack.pop()]\n           \
        \         width = i if not stack else i - stack[-1] - 1\n                  \
        \  current_max_area = max(current_max_area, height * width)\n              \
        \  stack.append(i)\n            return current_max_area\n\n        for r in\
        \ range(rows):\n            for c in range(cols):\n                if matrix[r][c]\
        \ == '1':\n                    heights[c] += 1\n                else:\n    \
        \                heights[c] = 0\n            max_area = max(max_area, largestRectangleArea(heights))\n\
        \n        return max_area"
      c: "#include <stdlib.h>\n#include <string.h>\n\n// Helper function for max\nint\
        \ max(int a, int b) {\n    return a > b ? a : b;\n}\n\n// Stack implementation\
        \ for C\ntypedef struct {\n    int* arr;\n    int top;\n    int capacity;\n\
        } Stack;\n\nStack* createStack(int capacity) {\n    Stack* stack = (Stack*)\
        \ malloc(sizeof(Stack));\n    stack->capacity = capacity;\n    stack->top =\
        \ -1;\n    stack->arr = (int*) malloc(stack->capacity * sizeof(int));\n    return\
        \ stack;\n}\n\nvoid push(Stack* stack, int item) {\n    stack->arr[++stack->top]\
        \ = item;\n}\n\nint pop(Stack* stack) {\n    return stack->arr[stack->top--];\n\
        }\n\nint peek(Stack* stack) {\n    return stack->arr[stack->top];\n}\n\nint\
        \ isEmpty(Stack* stack) {\n    return stack->top == -1;\n}\n\nvoid freeStack(Stack*\
        \ stack) {\n    free(stack->arr);\n    free(stack);\n}\n\n// Function to find\
        \ the largest rectangle area in a histogram\nint largestRectangleArea(int* heights,\
        \ int n) {\n    Stack* s = createStack(n + 1); // Stack can hold up to n+1 elements\n\
        \    int max_area = 0;\n\n    for (int i = 0; i <= n; ++i) {\n        int current_height\
        \ = (i == n) ? 0 : heights[i];\n        while (!isEmpty(s) && heights[peek(s)]\
        \ >= current_height) {\n            int h = heights[pop(s)];\n            int\
        \ width = isEmpty(s) ? i : i - peek(s) - 1;\n            max_area = max(max_area,\
        \ h * width);\n        }\n        push(s, i);\n    }\n    freeStack(s);\n  \
        \  return max_area;\n}\n\nint maximalRectangle(char** matrix, int matrixSize,\
        \ int* matrixColSize) {\n    if (matrixSize == 0 || *matrixColSize == 0) {\n\
        \        return 0;\n    }\n\n    int rows = matrixSize;\n    int cols = *matrixColSize;\
        \ // All rows have the same number of columns\n\n    int* heights = (int*) calloc(cols,\
        \ sizeof(int)); // Initialize with zeros\n    int max_overall_area = 0;\n\n\
        \    for (int r = 0; r < rows; ++r) {\n        for (int c = 0; c < cols; ++c)\
        \ {\n            if (matrix[r][c] == '1') {\n                heights[c]++;\n\
        \            } else {\n                heights[c] = 0;\n            }\n    \
        \    }\n        max_overall_area = max(max_overall_area, largestRectangleArea(heights,\
        \ cols));\n    }\n\n    free(heights);\n    return max_overall_area;\n}"
      csharp: "public class Solution {\n    public int MaximalRectangle(char[][] matrix)\
        \ {\n        if (matrix == null || matrix.Length == 0 || matrix[0].Length ==\
        \ 0) {\n            return 0;\n        }\n\n        int rows = matrix.Length;\n\
        \        int cols = matrix[0].Length;\n        int maxArea = 0;\n\n        int[]\
        \ heights = new int[cols];\n\n        for (int i = 0; i < rows; i++) {\n   \
        \         for (int j = 0; j < cols; j++) {\n                if (matrix[i][j]\
        \ == '1') {\n                    heights[j]++;\n                } else {\n \
        \                   heights[j] = 0;\n                }\n            }\n    \
        \        maxArea = Math.Max(maxArea, LargestRectangleArea(heights));\n     \
        \   }\n\n        return maxArea;\n    }\n\n    private int LargestRectangleArea(int[]\
        \ heights) {\n        Stack<int> stack = new Stack<int>();\n        int maxArea\
        \ = 0;\n        int n = heights.Length;\n\n        for (int i = 0; i <= n; i++)\
        \ {\n            int currentHeight = (i == n) ? 0 : heights[i]; // Sentinel\
        \ value 0 at the end\n\n            while (stack.Count > 0 && currentHeight\
        \ < heights[stack.Peek()]) {\n                int h = heights[stack.Pop()];\n\
        \                int w = stack.Count == 0 ? i : i - stack.Peek() - 1;\n    \
        \            maxArea = Math.Max(maxArea, h * w);\n            }\n          \
        \  stack.Push(i);\n        }\n        return maxArea;\n    }\n}"
      javascript: "/**\n * @param {character[][]} matrix\n * @return {number}\n */\n\
        var maximalRectangle = function(matrix) {\n    if (!matrix || matrix.length\
        \ === 0 || matrix[0].length === 0) {\n        return 0;\n    }\n\n    const\
        \ rows = matrix.length;\n    const cols = matrix[0].length;\n    let maxArea\
        \ = 0;\n\n    const heights = new Array(cols).fill(0);\n\n    for (let i = 0;\
        \ i < rows; i++) {\n        for (let j = 0; j < cols; j++) {\n            if\
        \ (matrix[i][j] === '1') {\n                heights[j]++;\n            } else\
        \ {\n                heights[j] = 0;\n            }\n        }\n        maxArea\
        \ = Math.max(maxArea, largestRectangleArea(heights));\n    }\n\n    return maxArea;\n\
        };\n\n// Helper function for Largest Rectangle in Histogram\nvar largestRectangleArea\
        \ = function(heights) {\n    const stack = []; // Stores indices\n    let maxArea\
        \ = 0;\n    const n = heights.length;\n\n    for (let i = 0; i <= n; i++) {\n\
        \        const currentHeight = (i === n) ? 0 : heights[i]; // Sentinel value\
        \ 0 at the end\n\n        while (stack.length > 0 && currentHeight < heights[stack[stack.length\
        \ - 1]]) {\n            const h = heights[stack.pop()];\n            const w\
        \ = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;\n            maxArea\
        \ = Math.max(maxArea, h * w);\n        }\n        stack.push(i);\n    }\n  \
        \  return maxArea;\n};"
      typescript: "function maximalRectangle(matrix: string[][]): number {\n    if (!matrix\
        \ || matrix.length === 0 || matrix[0].length === 0) {\n        return 0;\n \
        \   }\n\n    const rows: number = matrix.length;\n    const cols: number = matrix[0].length;\n\
        \    let maxArea: number = 0;\n\n    const heights: number[] = new Array(cols).fill(0);\n\
        \n    for (let i = 0; i < rows; i++) {\n        for (let j = 0; j < cols; j++)\
        \ {\n            if (matrix[i][j] === '1') {\n                heights[j]++;\n\
        \            } else {\n                heights[j] = 0;\n            }\n    \
        \    }\n        maxArea = Math.max(maxArea, largestRectangleArea(heights));\n\
        \    }\n\n    return maxArea;\n}\n\n// Helper function for Largest Rectangle\
        \ in Histogram\nfunction largestRectangleArea(heights: number[]): number {\n\
        \    const stack: number[] = []; // Stores indices\n    let maxArea: number\
        \ = 0;\n    const n: number = heights.length;\n\n    for (let i = 0; i <= n;\
        \ i++) {\n        const currentHeight: number = (i === n) ? 0 : heights[i];\
        \ // Sentinel value 0 at the end\n\n        while (stack.length > 0 && currentHeight\
        \ < heights[stack[stack.length - 1]]) {\n            const h: number = heights[stack.pop()!];\
        \ // ! asserts that pop() will not return undefined\n            const w: number\
        \ = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;\n            maxArea\
        \ = Math.max(maxArea, h * w);\n        }\n        stack.push(i);\n    }\n  \
        \  return maxArea;\n}"
      php: "class Solution {\n\n    /**\n     * @param String[][] $matrix\n     * @return\
        \ Integer\n     */\n    function maximalRectangle($matrix) {\n        if (empty($matrix)\
        \ || empty($matrix[0])) {\n            return 0;\n        }\n\n        $rows\
        \ = count($matrix);\n        $cols = count($matrix[0]);\n        $maxArea =\
        \ 0;\n\n        $heights = array_fill(0, $cols, 0);\n\n        for ($i = 0;\
        \ $i < $rows; $i++) {\n            for ($j = 0; $j < $cols; $j++) {\n      \
        \          if ($matrix[$i][$j] === '1') {\n                    $heights[$j]++;\n\
        \                } else {\n                    $heights[$j] = 0;\n         \
        \       }\n            }\n            $maxArea = max($maxArea, $this->largestRectangleArea($heights));\n\
        \        }\n\n        return $maxArea;\n    }\n\n    /**\n     * Helper function\
        \ for Largest Rectangle in Histogram\n     * @param Integer[] $heights\n   \
        \  * @return Integer\n     */\n    private function largestRectangleArea($heights)\
        \ {\n        $stack = []; // Stores indices\n        $maxArea = 0;\n       \
        \ $n = count($heights);\n\n        for ($i = 0; $i <= $n; $i++) {\n        \
        \    $currentHeight = ($i === $n) ? 0 : $heights[$i]; // Sentinel value 0 at\
        \ the end\n\n            while (!empty($stack) && $currentHeight < $heights[end($stack)])\
        \ {\n                $h = $heights[array_pop($stack)];\n                $w =\
        \ empty($stack) ? $i : $i - end($stack) - 1;\n                $maxArea = max($maxArea,\
        \ $h * $w);\n            }\n            array_push($stack, $i);\n        }\n\
        \        return $maxArea;\n    }\n}"
      swift: "class Solution {\n    func maximalRectangle(_ matrix: [[Character]]) ->\
        \ Int {\n        if matrix.isEmpty || matrix[0].isEmpty {\n            return\
        \ 0\n        }\n\n        let rows = matrix.count\n        let cols = matrix[0].count\n\
        \        var maxArea = 0\n\n        var heights = Array(repeating: 0, count:\
        \ cols)\n\n        for i in 0..<rows {\n            for j in 0..<cols {\n  \
        \              if matrix[i][j] == \"1\" {\n                    heights[j] +=\
        \ 1\n                } else {\n                    heights[j] = 0\n        \
        \        }\n            }\n            maxArea = max(maxArea, largestRectangleArea(heights))\n\
        \        }\n\n        return maxArea\n    }\n\n    // Helper function for Largest\
        \ Rectangle in Histogram\n    private func largestRectangleArea(_ heights: [Int])\
        \ -> Int {\n        var stack: [Int] = [] // Stores indices\n        var maxArea\
        \ = 0\n        let n = heights.count\n\n        for i in 0...n {\n         \
        \   let currentHeight = (i == n) ? 0 : heights[i] // Sentinel value 0 at the\
        \ end\n\n            while !stack.isEmpty && currentHeight < heights[stack.last!]\
        \ {\n                let h = heights[stack.removeLast()]\n                let\
        \ w = stack.isEmpty ? i : i - stack.last! - 1\n                maxArea = max(maxArea,\
        \ h * w)\n            }\n            stack.append(i)\n        }\n        return\
        \ maxArea\n    }\n}"
      kotlin: "import java.util.ArrayDeque\n\nclass Solution {\n    fun maximalRectangle(matrix:\
        \ Array<CharArray>): Int {\n        if (matrix.isEmpty() || matrix[0].isEmpty())\
        \ {\n            return 0\n        }\n\n        val rows = matrix.size\n   \
        \     val cols = matrix[0].size\n        val heights = IntArray(cols)\n    \
        \    var maxArea = 0\n\n        for (r in 0 until rows) {\n            for (c\
        \ in 0 until cols) {\n                if (matrix[r][c] == '1') {\n         \
        \           heights[c]++\n                } else {\n                    heights[c]\
        \ = 0\n                }\n            }\n            maxArea = Math.max(maxArea,\
        \ largestRectangleArea(heights))\n        }\n\n        return maxArea\n    }\n\
        \n    private fun largestRectangleArea(heights: IntArray): Int {\n        var\
        \ maxArea = 0\n        val stack = ArrayDeque<Int>() // Stores indices\n\n \
        \       for (i in 0..heights.size) {\n            val currentHeight = if (i\
        \ == heights.size) 0 else heights[i]\n\n            while (stack.isNotEmpty()\
        \ && currentHeight < heights[stack.peek()]) {\n                val h = heights[stack.pop()]\n\
        \                val w = if (stack.isEmpty()) i else i - stack.peek() - 1\n\
        \                maxArea = Math.max(maxArea, h * w)\n            }\n       \
        \     stack.push(i)\n        }\n        return maxArea\n    }\n}"
      dart: "class Solution {\n  int maximalRectangle(List<List<String>> matrix) {\n\
        \    if (matrix.isEmpty || matrix[0].isEmpty) {\n      return 0;\n    }\n\n\
        \    int rows = matrix.length;\n    int cols = matrix[0].length;\n    List<int>\
        \ heights = List<int>.filled(cols, 0);\n    int maxArea = 0;\n\n    for (int\
        \ r = 0; r < rows; r++) {\n      for (int c = 0; c < cols; c++) {\n        if\
        \ (matrix[r][c] == '1') {\n          heights[c]++;\n        } else {\n     \
        \     heights[c] = 0;\n        }\n      }\n      maxArea = maxArea > _largestRectangleArea(heights)\
        \ ? maxArea : _largestRectangleArea(heights);\n    }\n\n    return maxArea;\n\
        \  }\n\n  int _largestRectangleArea(List<int> heights) {\n    int maxArea =\
        \ 0;\n    List<int> stack = []; // Stores indices\n\n    for (int i = 0; i <=\
        \ heights.length; i++) {\n      int currentHeight = (i == heights.length) ?\
        \ 0 : heights[i];\n\n      while (stack.isNotEmpty && currentHeight < heights[stack.last])\
        \ {\n        int h = heights[stack.removeLast()];\n        int w = stack.isEmpty\
        \ ? i : i - stack.last - 1;\n        maxArea = maxArea > (h * w) ? maxArea :\
        \ (h * w);\n      }\n      stack.add(i);\n    }\n    return maxArea;\n  }\n}"
      go: "func maximalRectangle(matrix [][]byte) int {\n    if len(matrix) == 0 ||\
        \ len(matrix[0]) == 0 {\n        return 0\n    }\n\n    rows := len(matrix)\n\
        \    cols := len(matrix[0])\n    heights := make([]int, cols)\n    maxArea :=\
        \ 0\n\n    for r := 0; r < rows; r++ {\n        for c := 0; c < cols; c++ {\n\
        \            if matrix[r][c] == '1' {\n                heights[c]++\n      \
        \      } else {\n                heights[c] = 0\n            }\n        }\n\
        \        maxArea = max(maxArea, largestRectangleArea(heights))\n    }\n\n  \
        \  return maxArea\n}\n\nfunc largestRectangleArea(heights []int) int {\n   \
        \ maxArea := 0\n    stack := []int{} // Stores indices\n\n    for i := 0; i\
        \ <= len(heights); i++ {\n        currentHeight := 0\n        if i < len(heights)\
        \ {\n            currentHeight = heights[i]\n        }\n\n        for len(stack)\
        \ > 0 && currentHeight < heights[stack[len(stack)-1]] {\n            h := heights[stack[len(stack)-1]]\n\
        \            stack = stack[:len(stack)-1] // Pop\n\n            w := i\n   \
        \         if len(stack) > 0 {\n                w = i - stack[len(stack)-1] -\
        \ 1\n            }\n            maxArea = max(maxArea, h * w)\n        }\n \
        \       stack = append(stack, i) // Push\n    }\n    return maxArea\n}\n\nfunc\
        \ max(a, b int) int {\n    if a > b {\n        return a\n    }\n    return b\n\
        }"
      ruby: "# @param {Character[][]} matrix\n# @return {Integer}\ndef maximal_rectangle(matrix)\n\
        \    return 0 if matrix.empty? || matrix[0].empty?\n\n    rows = matrix.length\n\
        \    cols = matrix[0].length\n    heights = Array.new(cols, 0)\n    max_area\
        \ = 0\n\n    rows.times do |r|\n        cols.times do |c|\n            if matrix[r][c]\
        \ == '1'\n                heights[c] += 1\n            else\n              \
        \  heights[c] = 0\n            end\n        end\n        max_area = [max_area,\
        \ largest_rectangle_area(heights)].max\n    end\n\n    max_area\nend\n\ndef\
        \ largest_rectangle_area(heights)\n    max_area = 0\n    stack = [] # Stores\
        \ indices\n\n    (0..heights.length).each do |i|\n        current_height = (i\
        \ == heights.length) ? 0 : heights[i]\n\n        while !stack.empty? && current_height\
        \ < heights[stack.last]\n            h = heights[stack.pop()]\n            w\
        \ = stack.empty? ? i : i - stack.last - 1\n            max_area = [max_area,\
        \ h * w].max\n        end\n        stack.push(i)\n    end\n    max_area\nend"
      scala: "import scala.collection.mutable.Stack\n\nobject Solution {\n    def maximalRectangle(matrix:\
        \ Array[Array[Char]]): Int = {\n        if (matrix.isEmpty || matrix(0).isEmpty)\
        \ {\n            return 0\n        }\n\n        val rows = matrix.length\n \
        \       val cols = matrix(0).length\n        val heights = Array.fill(cols)(0)\n\
        \        var maxArea = 0\n\n        for (r <- 0 until rows) {\n            for\
        \ (c <- 0 until cols) {\n                if (matrix(r)(c) == '1') {\n      \
        \              heights(c) += 1\n                } else {\n                 \
        \   heights(c) = 0\n                }\n            }\n            maxArea =\
        \ maxArea.max(largestRectangleArea(heights))\n        }\n\n        maxArea\n\
        \    }\n\n    private def largestRectangleArea(heights: Array[Int]): Int = {\n\
        \        var maxArea = 0\n        val stack = new Stack[Int]() // Stores indices\n\
        \n        for (i <- 0 to heights.length) {\n            val currentHeight =\
        \ if (i == heights.length) 0 else heights(i)\n\n            while (stack.nonEmpty\
        \ && currentHeight < heights(stack.top)) {\n                val h = heights(stack.pop())\n\
        \                val w = if (stack.isEmpty) i else i - stack.top - 1\n     \
        \           maxArea = maxArea.max(h * w)\n            }\n            stack.push(i)\n\
        \        }\n        maxArea\n    }\n}"
      rust: "impl Solution {\n    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) ->\
        \ i32 {\n        if matrix.is_empty() || matrix[0].is_empty() {\n          \
        \  return 0;\n        }\n\n        let rows = matrix.len();\n        let cols\
        \ = matrix[0].len();\n        let mut max_area = 0;\n        let mut heights:\
        \ Vec<i32> = vec![0; cols];\n\n        for i in 0..rows {\n            for j\
        \ in 0..cols {\n                if matrix[i][j] == '1' {\n                 \
        \   heights[j] += 1;\n                } else {\n                    heights[j]\
        \ = 0;\n                }\n            }\n            max_area = max_area.max(Self::largest_rectangle_in_histogram(&heights));\n\
        \        }\n\n        max_area\n    }\n\n    fn largest_rectangle_in_histogram(heights:\
        \ &[i32]) -> i32 {\n        let n = heights.len();\n        let mut max_area\
        \ = 0;\n        let mut stack: Vec<usize> = Vec::new(); // Stores indices\n\n\
        \        for i in 0..=n { // Iterate up to n to process remaining stack elements\n\
        \            let current_height = if i == n { 0 } else { heights[i] };\n\n \
        \           while !stack.is_empty() && current_height < heights[*stack.last().unwrap()]\
        \ {\n                let h_idx = stack.pop().unwrap();\n                let\
        \ h = heights[h_idx];\n                let width = if stack.is_empty() {\n \
        \                   i as i32\n                } else {\n                   \
        \ (i - stack.last().unwrap() - 1) as i32\n                };\n             \
        \   max_area = max_area.max(h * width);\n            }\n            stack.push(i);\n\
        \        }\n        max_area\n    }\n}"
      racket: "(define/contract (maximal-rectangle matrix)\n  (-> (listof (listof char?))\
        \ exact-integer?)\n  (if (or (null? matrix) (null? (car matrix)))\n      0 ;\
        \ Handle empty matrix or empty rows\n      (let* ([rows (length matrix)]\n \
        \            [cols (length (car matrix))])\n\n        (define (largest-rectangle-in-histogram\
        \ heights)\n          (let ([n (length heights)])\n            (define (process-bars\
        \ i stack max-h-area)\n              (if (> i n)\n                  max-h-area\n\
        \                  (let ([current-height (if (= i n) 0 (list-ref heights i))])\n\
        \                    (define (pop-and-calculate current-stack current-max)\n\
        \                      (if (and (not (null? current-stack))\n              \
        \                 (< current-height (list-ref heights (car current-stack))))\n\
        \                          (let* ([h-idx (car current-stack)]\n            \
        \                     [h (list-ref heights h-idx)]\n                       \
        \          [new-stack (cdr current-stack)]\n                               \
        \  [width (if (null? new-stack)\n                                          \
        \  i\n                                            (- i (car new-stack) 1))])\n\
        \                            (pop-and-calculate new-stack (max current-max (*\
        \ h width))))\n                          (process-bars (+ i 1) (cons i current-stack)\
        \ current-max))) ; Push current index\n                    (pop-and-calculate\
        \ stack max-h-area))))) ; Start popping and calculating\n            (process-bars\
        \ 0 '() 0))))\n\n        (define (iterate-rows r current-heights max-overall-area)\n\
        \          (if (= r rows)\n              max-overall-area\n              (let*\
        \ ([row-chars (list-ref matrix r)]\n                     [new-heights (for/list\
        \ ([j (in-range cols)]\n                                             [h current-heights])\n\
        \                                    (if (char=? (list-ref row-chars j) #\\\
        1)\n                                        (+ h 1)\n                      \
        \                  0))] ; Update heights for current row\n                 \
        \    [area-from-row (largest-rectangle-in-histogram new-heights)])\n       \
        \         (iterate-rows (+ r 1) new-heights (max max-overall-area area-from-row)))))\
        \ ; Recurse to next row\n\n        (iterate-rows 0 (make-list cols 0) 0))))"
      erlang: "-spec maximal_rectangle(Matrix :: [[char()]]) -> integer().\nmaximal_rectangle(Matrix)\
        \ ->\nRows = length(Matrix),\nCols = if Rows == 0 -> 0; true -> length(hd(Matrix))\
        \ end,\n\nif Rows == 0 orelse Cols == 0 ->\n0;\ntrue ->\nInitialHeights = lists:duplicate(Cols,\
        \ 0),\nmaximal_rectangle_loop(Matrix, 0, Rows, Cols, InitialHeights, 0)\nend.\n\
        \nmaximal_rectangle_loop(_Matrix, RowIdx, Rows, _Cols, _Heights, MaxArea) when\
        \ RowIdx == Rows ->\nMaxArea;\nmaximal_rectangle_loop(Matrix, RowIdx, Rows,\
        \ Cols, CurrentHeights, MaxArea) ->\nCurrentRow = lists:nth(RowIdx + 1, Matrix),\n\
        NewHeights = update_heights(CurrentRow, CurrentHeights, 0, Cols, []),\nAreaFromRow\
        \ = largest_rectangle_in_histogram(NewHeights),\nNewMaxArea = max(MaxArea, AreaFromRow),\n\
        maximal_rectangle_loop(Matrix, RowIdx + 1, Rows, Cols, NewHeights, NewMaxArea).\n\
        \nupdate_heights(_CurrentRow, _CurrentHeights, J, Cols, Acc) when J == Cols\
        \ ->\nlists:reverse(Acc);\nupdate_heights(CurrentRow, CurrentHeights, J, Cols,\
        \ Acc) ->\nChar = lists:nth(J + 1, CurrentRow),\nH = lists:nth(J + 1, CurrentHeights),\n\
        NewH = if Char == $1 -> H + 1; true -> 0 end,\nupdate_heights(CurrentRow, CurrentHeights,\
        \ J + 1, Cols, [NewH | Acc]).\n\nlargest_rectangle_in_histogram(Heights) ->\n\
        N = length(Heights),\nExtendedHeights = Heights ++ [0],\nlargest_rectangle_in_histogram_loop(0,\
        \ N, ExtendedHeights, [], 0).\n\nlargest_rectangle_in_histogram_loop(I, N, Heights,\
        \ Stack, MaxArea) when I > N ->\nMaxArea;\nlargest_rectangle_in_histogram_loop(I,\
        \ N, Heights, Stack, MaxArea) ->\nCurrentHeight = lists:nth(I + 1, Heights),\n\
        {NewStack, CurrentMaxArea} = pop_and_calculate(I, CurrentHeight, Heights, Stack,\
        \ MaxArea),\nlargest_rectangle_in_histogram_loop(I + 1, N, Heights, [I | NewStack],\
        \ CurrentMaxArea).\n\npop_and_calculate(I, CurrentHeight, Heights, Stack, CurrentMax)\
        \ ->\ncase Stack of\n[] ->\n    {Stack, CurrentMax};\n[H_idx | RestStack] ->\n\
        \    H_at_stack_top = lists:nth(H_idx + 1, Heights),\n    if CurrentHeight <\
        \ H_at_stack_top ->\n        H = H_at_stack_top,\n        Width = case RestStack\
        \ of\n                    [] -> I;\n                    [Prev_H_idx | _] ->\
        \ I - Prev_H_idx - 1\n                end,\n        pop_and_calculate(I, CurrentHeight,\
        \ Heights, RestStack, max(CurrentMax, H * Width));\n    true ->\n        {Stack,\
        \ CurrentMax}\n    end\nend."
      elixir: "defmodule Solution do\n  @spec maximal_rectangle(matrix :: [[char]])\
        \ :: integer\n  def maximal_rectangle(matrix) do\n    rows = length(matrix)\n\
        \    cols = if rows == 0, do: 0, else: length(hd(matrix))\n\n    if rows ==\
        \ 0 || cols == 0 do\n      0\n    else\n      initial_heights = List.duplicate(0,\
        \ cols)\n      maximal_rectangle_loop(matrix, 0, rows, cols, initial_heights,\
        \ 0)\n    end\n  end\n\n  defp maximal_rectangle_loop(_matrix, row_idx, rows,\
        \ _cols, _heights, max_area) when row_idx == rows do\n    max_area\n  end\n\n\
        \  defp maximal_rectangle_loop(matrix, row_idx, rows, cols, current_heights,\
        \ max_area) do\n    current_row = Enum.at(matrix, row_idx)\n    new_heights\
        \ = update_heights(current_row, current_heights, 0, cols, [])\n    area_from_row\
        \ = largest_rectangle_in_histogram(new_heights)\n    new_max_area = max(max_area,\
        \ area_from_row)\n    maximal_rectangle_loop(matrix, row_idx + 1, rows, cols,\
        \ new_heights, new_max_area)\n  end\n\n  defp update_heights(_current_row, _current_heights,\
        \ j, cols, acc) when j == cols do\n    Enum.reverse(acc)\n  end\n\n  defp update_heights(current_row,\
        \ current_heights, j, cols, acc) do\n    char = Enum.at(current_row, j)\n  \
        \  h = Enum.at(current_heights, j)\n    new_h = if char == ?1, do: h + 1, else:\
        \ 0\n    update_heights(current_row, current_heights, j + 1, cols, [new_h |\
        \ acc])\n  end\n\n  defp largest_rectangle_in_histogram(heights) do\n    n =\
        \ length(heights)\n    extended_heights = heights ++ [0] # Append 0 to ensure\
        \ all stack elements are processed\n    largest_rectangle_in_histogram_loop(0,\
        \ n, extended_heights, [], 0)\n  end\n\n  defp largest_rectangle_in_histogram_loop(i,\
        \ n, heights, stack, max_area) when i > n do\n    max_area\n  end\n\n  defp\
        \ largest_rectangle_in_histogram_loop(i, n, heights, stack, max_area) do\n \
        \   current_height = Enum.at(heights, i)\n    {new_stack, current_max_area}\
        \ = pop_and_calculate(i, current_height, heights, stack, max_area)\n    largest_rectangle_in_histogram_loop(i\
        \ + 1, n, heights, [i | new_stack], current_max_area)\n  end\n\n  defp pop_and_calculate(i,\
        \ current_height, heights, stack, current_max) do\n    case stack do\n     \
        \ [] ->\n        {stack, current_max}\n      [h_idx | rest_stack] ->\n     \
        \   h_at_stack_top = Enum.at(heights, h_idx)\n        if current_height < h_at_stack_top\
        \ do\n          h = h_at_stack_top\n          width = case rest_stack do\n \
        \                     [] -> i\n                      [prev_h_idx | _] -> i -\
        \ prev_h_idx - 1\n                    end\n          pop_and_calculate(i, current_height,\
        \ heights, rest_stack, max(current_max, h * width))\n        else\n        \
        \  {stack, current_max}\n        end\n    end\n  end\nend"
    approach: 'This problem can be efficiently solved by reducing it to the "Largest
      Rectangle in Histogram" problem. We iterate through each row of the given binary
      matrix. For each row, we construct a histogram where each bar''s height at column
      j represents the number of consecutive ''1''s extending upwards from matrix[i][j]
      to matrix[0][j]. If matrix[i][j] is ''0'', the height at column j is reset to
      0; otherwise, it''s incremented by one from the height calculated for the cell
      directly above it in the previous row.


      After computing the heights array for the current row, we apply the standard "Largest
      Rectangle in Histogram" algorithm. This algorithm uses a monotonic stack to find,
      for each bar in the histogram, the largest rectangle that can be formed with that
      bar as its height. It efficiently determines the nearest smaller elements to the
      left and right of each bar. We maintain a global maximum area, updating it with
      the largest area found in each row''s histogram. The final maximum area accumulated
      across all rows is the result.'
    time_complexity: The algorithm iterates through each of the `rows`. In each row,
      it processes `cols` elements to update the `heights` array, taking `O(cols)` time.
      Subsequently, the `largestRectangleArea` helper function is called, which processes
      the `heights` array of size `cols` using a monotonic stack. This helper function
      also takes `O(cols)` time as each element is pushed and popped from the stack
      at most once. Therefore, the total time complexity is `O(rows * cols)`.
    space_complexity: The primary space usage comes from the `heights` array, which
      stores `cols` integers, and the monotonic stack used within the `largestRectangleArea`
      function, which can store up to `cols` indices in the worst case. Thus, the total
      space complexity is `O(cols)`.
    elapsed_time: 137.23418736457825
    model: gemini-2.5-flash
    generated_at: '2026-01-11 01:18:39 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maximalRectangle(vector<vector<char>>&\
        \ matrix) {\n        if (matrix.empty() || matrix[0].empty()) return 0;\n  \
        \      int rows = matrix.size(), cols = matrix[0].size();\n        vector<int>\
        \ height(cols + 1, 0);\n        int maxArea = 0;\n        for (int i = 0; i\
        \ < rows; i++) {\n            for (int j = 0; j < cols; j++) {\n           \
        \     height[j] = matrix[i][j] == '1' ? height[j] + 1 : 0;\n            }\n\
        \            stack<int> s;\n            for (int j = 0; j <= cols; j++) {\n\
        \                while (!s.empty() && height[j] < height[s.top()]) {\n     \
        \               int h = height[s.top()]; s.pop();\n                    int w\
        \ = s.empty() ? j : j - s.top() - 1;\n                    maxArea = max(maxArea,\
        \ h * w);\n                }\n                s.push(j);\n            }\n  \
        \      }\n        return maxArea;\n    }\n};"
      java: "class Solution {\n    public int maximalRectangle(char[][] matrix) {\n\
        \        if (matrix.length == 0 || matrix[0].length == 0) return 0;\n      \
        \  int rows = matrix.length, cols = matrix[0].length;\n        int[] height\
        \ = new int[cols + 1];\n        int maxArea = 0;\n        for (int i = 0; i\
        \ < rows; i++) {\n            for (int j = 0; j < cols; j++) {\n           \
        \     height[j] = matrix[i][j] == '1' ? height[j] + 1 : 0;\n            }\n\
        \            java.util.Stack<Integer> s = new java.util.Stack<>();\n       \
        \     for (int j = 0; j <= cols; j++) {\n                while (!s.isEmpty()\
        \ && height[j] < height[s.peek()]) {\n                    int h = height[s.peek()];\
        \ s.pop();\n                    int w = s.isEmpty() ? j : j - s.peek() - 1;\n\
        \                    maxArea = Math.max(maxArea, h * w);\n                }\n\
        \                s.push(j);\n            }\n        }\n        return maxArea;\n\
        \    }\n}"
      python: "class Solution(object):\n    def maximalRectangle(self, matrix):\n  \
        \      if not matrix or not matrix[0]: return 0\n        rows, cols = len(matrix),\
        \ len(matrix[0])\n        height = [0] * (cols + 1)\n        maxArea = 0\n \
        \       for row in matrix:\n            for j in range(cols):\n            \
        \    height[j] = height[j] + 1 if row[j] == '1' else 0\n            stack =\
        \ []\n            for j in range(cols + 1):\n                while stack and\
        \ height[j] < height[stack[-1]]:\n                    h = height[stack.pop()]\n\
        \                    w = j if not stack else j - stack[-1] - 1\n           \
        \         maxArea = max(maxArea, h * w)\n                stack.append(j)\n \
        \       return maxArea"
      python3: "class Solution:\n    def maximalRectangle(self, matrix: list[list[str]])\
        \ -> int:\n        if not matrix or not matrix[0]: return 0\n        rows, cols\
        \ = len(matrix), len(matrix[0])\n        height = [0] * (cols + 1)\n       \
        \ maxArea = 0\n        for row in matrix:\n            for j in range(cols):\n\
        \                height[j] = height[j] + 1 if row[j] == '1' else 0\n       \
        \     stack = []\n            for j in range(cols + 1):\n                while\
        \ stack and height[j] < height[stack[-1]]:\n                    h = height[stack.pop()]\n\
        \                    w = j if not stack else j - stack[-1] - 1\n           \
        \         maxArea = max(maxArea, h * w)\n                stack.append(j)\n \
        \       return maxArea"
      c: "int maximalRectangle(char** matrix, int matrixSize, int* matrixColSize) {\n\
        \    if (matrixSize == 0 || matrixColSize[0] == 0) return 0;\n    int rows =\
        \ matrixSize, cols = matrixColSize[0];\n    int* height = (int*)malloc((cols\
        \ + 1) * sizeof(int));\n    for (int i = 0; i <= cols; i++) height[i] = 0;\n\
        \    int maxArea = 0;\n    for (int i = 0; i < rows; i++) {\n        for (int\
        \ j = 0; j < cols; j++) {\n            height[j] = matrix[i][j] == '1' ? height[j]\
        \ + 1 : 0;\n        }\n        int* stack = (int*)malloc((cols + 1) * sizeof(int));\n\
        \        int top = -1;\n        for (int j = 0; j <= cols; j++) {\n        \
        \    while (top != -1 && height[j] < height[stack[top]]) {\n               \
        \ int h = height[stack[top]];\n                top--;\n                int w\
        \ = top == -1 ? j : j - stack[top] - 1;\n                maxArea = maxArea >\
        \ h * w ? maxArea : h * w;\n            }\n            stack[++top] = j;\n \
        \       }\n        free(stack);\n    }\n    free(height);\n    return maxArea;\n\
        }"
      csharp: "public class Solution {\n    public int MaximalRectangle(char[][] matrix)\
        \ {\n        if (matrix.Length == 0) return 0;\n        int rows = matrix.Length;\n\
        \        int cols = matrix[0].Length;\n        int[] height = new int[cols +\
        \ 1];\n        int maxArea = 0;\n        for (int i = 0; i < rows; i++) {\n\
        \            for (int j = 0; j < cols; j++) {\n                height[j] = matrix[i][j]\
        \ == '1' ? height[j] + 1 : 0;\n            }\n            int[] stack = new\
        \ int[cols + 1];\n            int top = -1;\n            for (int j = 0; j <=\
        \ cols; j++) {\n                if (top == -1 || height[j] >= height[stack[top]])\
        \ {\n                    stack[++top] = j;\n                } else {\n     \
        \               while (top != -1 && height[j] < height[stack[top]]) {\n    \
        \                    int h = height[stack[top--]];\n                       \
        \ int w = top == -1 ? j : j - stack[top] - 1;\n                        maxArea\
        \ = Math.Max(maxArea, h * w);\n                    }\n                    stack[++top]\
        \ = j;\n                }\n            }\n        }\n        return maxArea;\n\
        \    }\n}"
      javascript: "var maximalRectangle = function(matrix) {\n    if (matrix.length\
        \ == 0) return 0;\n    let rows = matrix.length;\n    let cols = matrix[0].length;\n\
        \    let height = new Array(cols + 1).fill(0);\n    let maxArea = 0;\n    for\
        \ (let i = 0; i < rows; i++) {\n        for (let j = 0; j < cols; j++) {\n \
        \           height[j] = matrix[i][j] == '1' ? height[j] + 1 : 0;\n        }\n\
        \        let stack = [];\n        let top = -1;\n        for (let j = 0; j <=\
        \ cols; j++) {\n            if (top == -1 || height[j] >= height[stack[top]])\
        \ {\n                stack.push(j);\n                top++;\n            } else\
        \ {\n                while (top != -1 && height[j] < height[stack[top]]) {\n\
        \                    let h = height[stack.pop()];\n                    top--;\n\
        \                    let w = top == -1 ? j : j - stack[stack.length - 1] - 1;\n\
        \                    maxArea = Math.max(maxArea, h * w);\n                }\n\
        \                stack.push(j);\n                top++;\n            }\n   \
        \     }\n    }\n    return maxArea;\n};"
      typescript: "function maximalRectangle(matrix: string[][]): number {\n    if (matrix.length\
        \ == 0) return 0;\n    let rows = matrix.length;\n    let cols = matrix[0].length;\n\
        \    let height: number[] = new Array(cols + 1).fill(0);\n    let maxArea =\
        \ 0;\n    for (let i = 0; i < rows; i++) {\n        for (let j = 0; j < cols;\
        \ j++) {\n            height[j] = matrix[i][j] == '1' ? height[j] + 1 : 0;\n\
        \        }\n        let stack: number[] = [];\n        let top = -1;\n     \
        \   for (let j = 0; j <= cols; j++) {\n            if (top == -1 || height[j]\
        \ >= height[stack[top]]) {\n                stack.push(j);\n               \
        \ top++;\n            } else {\n                while (top != -1 && height[j]\
        \ < height[stack[top]]) {\n                    let h = height[stack.pop()!];\n\
        \                    top--;\n                    let w = top == -1 ? j : j -\
        \ stack[stack.length - 1] - 1;\n                    maxArea = Math.max(maxArea,\
        \ h * w);\n                }\n                stack.push(j);\n             \
        \   top++;\n            }\n        }\n    }\n    return maxArea;\n}"
      php: "class Solution {\n    function maximalRectangle($matrix) {\n        if (empty($matrix))\
        \ return 0;\n        $rows = count($matrix);\n        $cols = count($matrix[0]);\n\
        \        $height = array_fill(0, $cols + 1, 0);\n        $maxArea = 0;\n   \
        \     for ($i = 0; $i < $rows; $i++) {\n            for ($j = 0; $j < $cols;\
        \ $j++) {\n                $height[$j] = $matrix[$i][$j] == '1' ? $height[$j]\
        \ + 1 : 0;\n            }\n            $stack = [];\n            $top = -1;\n\
        \            for ($j = 0; $j <= $cols; $j++) {\n                if ($top ==\
        \ -1 || $height[$j] >= $height[$stack[$top]]) {\n                    $stack[++$top]\
        \ = $j;\n                } else {\n                    while ($top != -1 &&\
        \ $height[$j] < $height[$stack[$top]]) {\n                        $h = $height[array_pop($stack)];\n\
        \                        $top--;\n                        $w = $top == -1 ?\
        \ $j : $j - $stack[$top] - 1;\n                        $maxArea = max($maxArea,\
        \ $h * $w);\n                    }\n                    $stack[++$top] = $j;\n\
        \                }\n            }\n        }\n        return $maxArea;\n   \
        \ }\n}"
      swift: "class Solution {\n    func maximalRectangle(_ matrix: [[Character]]) ->\
        \ Int {\n        if matrix.isEmpty { return 0 }\n        let rows = matrix.count\n\
        \        let cols = matrix[0].count\n        var height = Array(repeating: 0,\
        \ count: cols + 1)\n        var maxArea = 0\n        for i in 0..<rows {\n \
        \           for j in 0..<cols {\n                height[j] = matrix[i][j] ==\
        \ \"1\" ? height[j] + 1 : 0\n            }\n            var stack: [Int] = []\n\
        \            var top = -1\n            for j in 0...cols {\n               \
        \ if top == -1 || height[j] >= height[stack[top]] {\n                    stack.append(j)\n\
        \                    top += 1\n                } else {\n                  \
        \  while top != -1 && height[j] < height[stack[top]] {\n                   \
        \     let h = height[stack.removeLast()]\n                        top -= 1\n\
        \                        let w = top == -1 ? j : j - stack.last! - 1\n     \
        \                   maxArea = max(maxArea, h * w)\n                    }\n \
        \                   stack.append(j)\n                    top += 1\n        \
        \        }\n            }\n        }\n        return maxArea\n    }\n}"
      kotlin: "class Solution {\n    fun maximalRectangle(matrix: Array<CharArray>):\
        \ Int {\n        if (matrix.isEmpty() || matrix[0].isEmpty()) return 0\n   \
        \     val n = matrix[0].size\n        val height = IntArray(n + 1)\n       \
        \ var maxArea = 0\n        for (row in matrix) {\n            for (i in 0 until\
        \ n) {\n                height[i] = if (row[i] == '1') height[i] + 1 else 0\n\
        \            }\n            val stack = ArrayDeque<Int>()\n            for (i\
        \ in 0..n) {\n                while (!stack.isEmpty() && (i == n || height[i]\
        \ < height[stack.last()])) {\n                    val h = height[stack.removeLast()]\n\
        \                    val w = if (stack.isEmpty()) i else i - stack.last() -\
        \ 1\n                    maxArea = maxOf(maxArea, h * w)\n                }\n\
        \                stack.addLast(i)\n            }\n        }\n        return\
        \ maxArea\n    }\n}"
      dart: "class Solution {\n  int maximalRectangle(List<List<String>> matrix) {\n\
        \    if (matrix.isEmpty || matrix[0].isEmpty) return 0;\n    int n = matrix[0].length;\n\
        \    List<int> height = List<int>.filled(n + 1, 0);\n    int maxArea = 0;\n\
        \    for (var row in matrix) {\n      for (int i = 0; i < n; i++) {\n      \
        \  height[i] = row[i] == '1' ? height[i] + 1 : 0;\n      }\n      List<int>\
        \ stack = [];\n      for (int i = 0; i <= n; i++) {\n        while (stack.isNotEmpty\
        \ && (i == n || height[i] < height[stack.last])) {\n          int h = height[stack.removeLast()];\n\
        \          int w = stack.isEmpty ? i : i - stack.last - 1;\n          maxArea\
        \ = maxArea > h * w ? maxArea : h * w;\n        }\n        stack.add(i);\n \
        \     }\n    }\n    return maxArea;\n  }\n}"
      go: "func maximalRectangle(matrix [][]byte) int {\n    if len(matrix) == 0 ||\
        \ len(matrix[0]) == 0 {\n        return 0\n    }\n    n := len(matrix[0])\n\
        \    height := make([]int, n+1)\n    maxArea := 0\n    for _, row := range matrix\
        \ {\n        for i := 0; i < n; i++ {\n            if row[i] == '1' {\n    \
        \            height[i] += 1\n            } else {\n                height[i]\
        \ = 0\n            }\n        }\n        stack := []int{}\n        for i :=\
        \ 0; i <= n; i++ {\n            for len(stack) > 0 && (i == n || height[i] <\
        \ height[stack[len(stack)-1]]) {\n                h := height[stack[len(stack)-1]]\n\
        \                w := i\n                if len(stack) > 0 {\n             \
        \       w = i - stack[len(stack)-1] - 1\n                }\n               \
        \ if h*w > maxArea {\n                    maxArea = h * w\n                }\n\
        \                stack = stack[:len(stack)-1]\n            }\n            stack\
        \ = append(stack, i)\n        }\n    }\n    return maxArea\n}"
      ruby: "def maximal_rectangle(matrix)\n    return 0 if matrix.empty? || matrix[0].empty?\n\
        \    n = matrix[0].size\n    height = Array.new(n + 1, 0)\n    max_area = 0\n\
        \    matrix.each do |row|\n        (0...n).each do |i|\n            height[i]\
        \ = row[i] == '1' ? height[i] + 1 : 0\n        end\n        stack = []\n   \
        \     (0..n).each do |i|\n            while !stack.empty? && (i == n || height[i]\
        \ < height[stack.last])\n                h = height[stack.pop]\n           \
        \     w = stack.empty? ? i : i - stack.last - 1\n                max_area =\
        \ [max_area, h * w].max\n            end\n            stack.push(i)\n      \
        \  end\n    end\n    max_area\nend"
      scala: "object Solution {\n    def maximalRectangle(matrix: Array[Array[Char]]):\
        \ Int = {\n        if (matrix.isEmpty || matrix(0).isEmpty) return 0\n     \
        \   val n = matrix(0).length\n        val height = Array.ofDim[Int](n + 1)\n\
        \        var maxArea = 0\n        for (row <- matrix) {\n            for (i\
        \ <- 0 until n) {\n                height(i) = if (row(i) == '1') height(i)\
        \ + 1 else 0\n            }\n            val stack = scala.collection.mutable.Stack[Int]()\n\
        \            for (i <- 0 to n) {\n                while (!stack.isEmpty && (i\
        \ == n || height(i) < height(stack.top))) {\n                    val h = height(stack.pop)\n\
        \                    val w = if (stack.isEmpty) i else i - stack.top - 1\n \
        \                   maxArea = math.max(maxArea, h * w)\n                }\n\
        \                stack.push(i)\n            }\n        }\n        maxArea\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) ->\
        \ i32 {\n        let rows = matrix.len();\n        let cols = matrix[0].len();\n\
        \        let mut height = vec![0; cols];\n        let mut max_area = 0;\n  \
        \      for row in 0..rows {\n            for col in 0..cols {\n            \
        \    if matrix[row][col] == '1' {\n                    height[col] += 1;\n \
        \               } else {\n                    height[col] = 0;\n           \
        \     }\n            }\n            let mut stack = Vec::new();\n          \
        \  let mut col = 0;\n            while col < cols {\n                if stack.is_empty()\
        \ || height[col] >= height[*stack.last().unwrap()] {\n                    stack.push(col);\n\
        \                    col += 1;\n                } else {\n                 \
        \   let top = stack.pop().unwrap();\n                    let width = if stack.is_empty()\
        \ { col } else { col - stack.last().unwrap() - 1 };\n                    max_area\
        \ = max_area.max(height[top] * width as i32);\n                }\n         \
        \   }\n            while !stack.is_empty() {\n                let top = stack.pop().unwrap();\n\
        \                let width = if stack.is_empty() { col } else { col - stack.last().unwrap()\
        \ - 1 };\n                max_area = max_area.max(height[top] * width as i32);\n\
        \            }\n        }\n        max_area\n    }\n}"
      racket: "(define/contract (maximal-rectangle matrix)\n  (-> (listof (listof char?))\
        \ exact-integer?)\n  (let* (\n           [rows (length matrix)]\n          \
        \ [cols (length (car matrix))]\n           [height (make-vector cols 0)]\n \
        \          [max-area 0])\n    (for-each\n     (lambda (row)\n       (for-each\n\
        \        (lambda (col val)\n          (if (eq? val #\\1)\n              (vector-set!\
        \ height col (+ (vector-ref height col) 1))\n              (vector-set! height\
        \ col 0)))\n        row\n        (build-list cols values))\n       (let loop\
        \ (\n                 [col 0]\n                 [stack '()])\n         (cond\n\
        \          [(= col cols)\n           (loop2 stack)]\n          [(or (null? stack)\
        \ (>= (vector-ref height col) (vector-ref height (car stack))))\n          \
        \ (loop (+ col 1) (cons col stack))]\n          [else\n           (let* (\n\
        \                    [top (car stack)]\n                    [width (if (null?\
        \ stack) col (- col (car stack) 1))])\n             (set! max-area (max max-area\
        \ (* (vector-ref height top) width)))\n             (loop col (cdr stack)))]))\n\
        \       (define (loop2 stack)\n         (cond\n          [(null? stack) max-area]\n\
        \          [else\n           (let* (\n                    [top (car stack)]\n\
        \                    [width (if (null? stack) cols (- cols (car stack) 1))])\n\
        \             (set! max-area (max max-area (* (vector-ref height top) width)))\n\
        \             (loop2 (cdr stack)))])))\n     matrix)\n    max-area))"
      erlang: "maximal_rectangle(Matrix) ->\n  Rows = length(Matrix),\n  Cols = length(hd(Matrix)),\n\
        \  Height = array:new(Cols, {default, 0}),\n  MaxArea = 0,\n  maximal_rectangle(Matrix,\
        \ Rows, Cols, Height, MaxArea).\n\nmaximal_rectangle([Row|Rows], Rows, Cols,\
        \ Height, MaxArea) ->\n  NewHeight = lists:foldl(fun ({Col, Val}, H) ->\n  \
        \                           if Val =:= $1 ->\n                             \
        \    array:set(Col, array:get(Col, H) + 1, H);\n                           \
        \  true ->\n                                 array:set(Col, 0, H)\n        \
        \                 end\n                     end, Height, Row),\n  {NewMaxArea,\
        \ _} = maximal_rectangle_row(NewHeight, Cols, MaxArea, []),\n  maximal_rectangle(Rows,\
        \ Rows, Cols, Height, NewMaxArea);\nmaximal_rectangle([], _, _, _, MaxArea)\
        \ -> MaxArea.\n\nmaximal_rectangle_row(Height, Cols, MaxArea, Stack) ->\n  maximal_rectangle_row(Height,\
        \ Cols, MaxArea, Stack, 0).\nmaximal_rectangle_row(Height, Cols, MaxArea, Stack,\
        \ Col) when Col < Cols ->\n  case Stack of\n    [] ->\n      maximal_rectangle_row(Height,\
        \ Cols, MaxArea, [Col], Col + 1);\n    [Top|T] ->\n      case array:get(Col,\
        \ Height) >= array:get(Top, Height) of\n        true ->\n          maximal_rectangle_row(Height,\
        \ Cols, MaxArea, [Col|Stack], Col + 1);\n        false ->\n          {NewMaxArea,\
        \ NewStack} =\n            case Stack of\n              [] -> {max(MaxArea,\
        \ array:get(Top, Height) * Col), T};\n              _ -> {max(MaxArea, array:get(Top,\
        \ Height) * (Col - hd(Stack) - 1)), T}\n            end,\n          maximal_rectangle_row(Height,\
        \ Cols, NewMaxArea, NewStack, Col)\n      end\n  end;\nmaximal_rectangle_row(Height,\
        \ Cols, MaxArea, Stack, Col) when Col >= Cols ->\n  lists:foldl(fun (Top, {MaxA,\
        \ Stack1}) ->\n                  {max(MaxA, array:get(Top, Height) * (Col -\
        \ hd(Stack1) - 1)), tl(Stack1)}\n              end, {MaxArea, Stack}, Stack)."
      elixir: "defmodule Solution do\n  @spec maximal_rectangle(matrix :: [[char]])\
        \ :: integer\n  def maximal_rectangle(matrix) do\n    rows = length(matrix)\n\
        \    cols = length(Enum.at(matrix, 0))\n    height = Array.new(cols, 0)\n  \
        \  max_area = 0\n    maximal_rectangle(matrix, rows, cols, height, max_area)\n\
        \  end\n\n  defp maximal_rectangle([row|rows], rows, cols, height, max_area)\
        \ do\n    new_height = Enum.reduce(Enum.with_index(row), height, fn {val, col},\
        \ h ->\n                                if val == ?1 do\n                  \
        \                Array.set(h, col, Array.get(h, col) + 1)\n                \
        \                else\n                                  Array.set(h, col, 0)\n\
        \                                end\n                              end)\n \
        \   {new_max_area, _} = maximal_rectangle_row(new_height, cols, max_area, [])\n\
        \    maximal_rectangle(rows, rows, cols, height, new_max_area)\n  end\n\n  defp\
        \ maximal_rectangle([], _, _, _, max_area) do\n    max_area\n  end\n\n  defp\
        \ maximal_rectangle_row(height, cols, max_area, stack) do\n    maximal_rectangle_row(height,\
        \ cols, max_area, stack, 0)\n  end\n\n  defp maximal_rectangle_row(height, cols,\
        \ max_area, stack, col) when col < cols do\n    case stack do\n      [] ->\n\
        \        maximal_rectangle_row(height, cols, max_area, [col], col + 1)\n   \
        \   [top|t] ->\n        case Array.get(height, col) >= Array.get(height, top)\
        \ do\n          true ->\n            maximal_rectangle_row(height, cols, max_area,\
        \ [col|stack], col + 1)\n          false ->\n            {new_max_area, new_stack}\
        \ =\n              case stack do\n                [] -> {max(max_area, Array.get(height,\
        \ top) * col), t}\n                _ -> {max(max_area, Array.get(height, top)\
        \ * (col - hd(stack) - 1)), t}\n              end,\n            maximal_rectangle_row(height,\
        \ cols, new_max_area, new_stack, col)\n        end\n    end\n  end\n\n  defp\
        \ maximal_rectangle_row(height, cols, max_area, stack, col) when col >= cols\
        \ do\n    Enum.reduce(stack, {max_area, stack}, fn top, {max_a, stack1} ->\n\
        \                             {max(max_a, Array.get(height, top) * (col - hd(stack1)\
        \ - 1)), tl(stack1)}\n                           end)\n  end\nend"
    approach: The algorithm to solve this problem involves using a histogram-based approach.
      For each row in the matrix, we calculate the height of the histogram by adding
      the current cell's value to the height of the cell above it if the current cell
      is 1, and resetting the height to 0 if the current cell is 0. Then, we use a stack-based
      approach to find the maximum area of the histogram. We iterate through the histogram,
      pushing the index of each bar onto the stack if the stack is empty or the current
      bar is higher than the bar at the top of the stack. If the current bar is lower
      than the bar at the top of the stack, we calculate the area of the rectangle with
      the bar at the top of the stack as the smallest bar and update the maximum area
      if necessary. We repeat this process until the stack is empty, at which point
      we have found the maximum area of the histogram for the current row. We repeat
      this process for each row in the matrix to find the maximum area of the rectangle
      containing only 1's. The key intuition behind this approach is that the maximum
      area of the rectangle containing only 1's can be found by considering each row
      as a histogram and finding the maximum area of the histogram for each row.
    time_complexity: The time complexity of this algorithm is O(rows * cols), where
      rows is the number of rows in the matrix and cols is the number of columns in
      the matrix. This is because we are iterating through each cell in the matrix once
      to calculate the height of the histogram, and then iterating through the histogram
      once to find the maximum area. The space complexity is O(cols), which is the maximum
      size of the stack.
    space_complexity: The space complexity of this algorithm is O(cols), which is the
      maximum size of the stack. This is because in the worst-case scenario, we may
      need to push all the indices of the histogram onto the stack, which can happen
      if the histogram is strictly decreasing.
    elapsed_time: 16.43586540222168
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-11 01:19:10 '
---

## Problem #85: Maximal Rectangle

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Stack, Matrix, Monotonic Stack

## Problem Description

<p>Given a <code>rows x cols</code>&nbsp;binary <code>matrix</code> filled with <code>0</code>&#39;s and <code>1</code>&#39;s, find the largest rectangle containing only <code>1</code>&#39;s and return <em>its area</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;" />
<pre>
<strong>Input:</strong> matrix = [[&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],[&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;],[&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;],[&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The maximal rectangle is shown in the above picture.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[&quot;0&quot;]]
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[&quot;1&quot;]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>rows == matrix.length</code></li>
	<li><code>cols == matrix[i].length</code></li>
	<li><code>1 &lt;= rows, cols &lt;= 200</code></li>
	<li><code>matrix[i][j]</code> is <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-11 01:18:39 )</small>
</summary>

<div class="ai-solution-content">

### Approach

This problem can be efficiently solved by reducing it to the "Largest Rectangle in Histogram" problem. We iterate through each row of the given binary matrix. For each row, we construct a histogram where each bar's height at column j represents the number of consecutive '1's extending upwards from matrix[i][j] to matrix[0][j]. If matrix[i][j] is '0', the height at column j is reset to 0; otherwise, it's incremented by one from the height calculated for the cell directly above it in the previous row.

After computing the heights array for the current row, we apply the standard "Largest Rectangle in Histogram" algorithm. This algorithm uses a monotonic stack to find, for each bar in the histogram, the largest rectangle that can be formed with that bar as its height. It efficiently determines the nearest smaller elements to the left and right of each bar. We maintain a global maximum area, updating it with the largest area found in each row's histogram. The final maximum area accumulated across all rows is the result.

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
    int largestRectangleArea(std::vector<int>& heights) {
        std::stack<int> s;
        int max_area = 0;
        int n = heights.size();

        for (int i = 0; i <= n; ++i) {
            int current_height = (i == n) ? 0 : heights[i];
            while (!s.empty() && heights[s.top()] >= current_height) {
                int h = heights[s.top()];
                s.pop();
                int width = s.empty() ? i : i - s.top() - 1;
                max_area = std::max(max_area, h * width);
            }
            s.push(i);
        }
        return max_area;
    }

    int maximalRectangle(std::vector<std::vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return 0;
        }

        int rows = matrix.size();
        int cols = matrix[0].size();

        std::vector<int> heights(cols, 0);
        int max_overall_area = 0;

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (matrix[r][c] == '1') {
                    heights[c]++;
                } else {
                    heights[c] = 0;
                }
            }
            max_overall_area = std::max(max_overall_area, largestRectangleArea(heights));
        }

        return max_overall_area;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Stack;
import java.util.Arrays;

class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int rows = matrix.length;
        int cols = matrix[0].length;

        int[] heights = new int[cols];
        int maxOverallArea = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (matrix[r][c] == '1') {
                    heights[c]++;
                } else {
                    heights[c] = 0;
                }
            }
            maxOverallArea = Math.max(maxOverallArea, largestRectangleArea(heights));
        }

        return maxOverallArea;
    }

    private int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>(); // stores indices
        int maxArea = 0;
        int n = heights.length;

        for (int i = 0; i <= n; i++) {
            int currentHeight = (i == n) ? 0 : heights[i];

            while (!stack.isEmpty() && heights[stack.peek()] >= currentHeight) {
                int h = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
                maxArea = Math.max(maxArea, h * width);
            }
            stack.push(i);
        }
        return maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(h):
            stack = [] # stores indices
            current_max_area = 0
            n = len(h)

            for i in range(n + 1): # Iterate through all bars, and an implicit 0 at the end
                current_height = h[i] if i < n else 0

                while stack and h[stack[-1]] >= current_height:
                    height = h[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    current_max_area = max(current_max_area, height * width)
                stack.append(i)
            return current_max_area

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(h: List[int]) -> int:
            stack = [] # stores indices
            current_max_area = 0
            n = len(h)

            for i in range(n + 1): # Iterate through all bars, and an implicit 0 at the end
                current_height = h[i] if i < n else 0

                while stack and h[stack[-1]] >= current_height:
                    height = h[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    current_max_area = max(current_max_area, height * width)
                stack.append(i)
            return current_max_area

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

// Helper function for max
int max(int a, int b) {
    return a > b ? a : b;
}

// Stack implementation for C
typedef struct {
    int* arr;
    int top;
    int capacity;
} Stack;

Stack* createStack(int capacity) {
    Stack* stack = (Stack*) malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->arr = (int*) malloc(stack->capacity * sizeof(int));
    return stack;
}

void push(Stack* stack, int item) {
    stack->arr[++stack->top] = item;
}

int pop(Stack* stack) {
    return stack->arr[stack->top--];
}

int peek(Stack* stack) {
    return stack->arr[stack->top];
}

int isEmpty(Stack* stack) {
    return stack->top == -1;
}

void freeStack(Stack* stack) {
    free(stack->arr);
    free(stack);
}

// Function to find the largest rectangle area in a histogram
int largestRectangleArea(int* heights, int n) {
    Stack* s = createStack(n + 1); // Stack can hold up to n+1 elements
    int max_area = 0;

    for (int i = 0; i <= n; ++i) {
        int current_height = (i == n) ? 0 : heights[i];
        while (!isEmpty(s) && heights[peek(s)] >= current_height) {
            int h = heights[pop(s)];
            int width = isEmpty(s) ? i : i - peek(s) - 1;
            max_area = max(max_area, h * width);
        }
        push(s, i);
    }
    freeStack(s);
    return max_area;
}

int maximalRectangle(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0 || *matrixColSize == 0) {
        return 0;
    }

    int rows = matrixSize;
    int cols = *matrixColSize; // All rows have the same number of columns

    int* heights = (int*) calloc(cols, sizeof(int)); // Initialize with zeros
    int max_overall_area = 0;

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (matrix[r][c] == '1') {
                heights[c]++;
            } else {
                heights[c] = 0;
            }
        }
        max_overall_area = max(max_overall_area, largestRectangleArea(heights, cols));
    }

    free(heights);
    return max_overall_area;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.Length == 0 || matrix[0].Length == 0) {
            return 0;
        }

        int rows = matrix.Length;
        int cols = matrix[0].Length;
        int maxArea = 0;

        int[] heights = new int[cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == '1') {
                    heights[j]++;
                } else {
                    heights[j] = 0;
                }
            }
            maxArea = Math.Max(maxArea, LargestRectangleArea(heights));
        }

        return maxArea;
    }

    private int LargestRectangleArea(int[] heights) {
        Stack<int> stack = new Stack<int>();
        int maxArea = 0;
        int n = heights.Length;

        for (int i = 0; i <= n; i++) {
            int currentHeight = (i == n) ? 0 : heights[i]; // Sentinel value 0 at the end

            while (stack.Count > 0 && currentHeight < heights[stack.Peek()]) {
                int h = heights[stack.Pop()];
                int w = stack.Count == 0 ? i : i - stack.Peek() - 1;
                maxArea = Math.Max(maxArea, h * w);
            }
            stack.Push(i);
        }
        return maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) {
        return 0;
    }

    const rows = matrix.length;
    const cols = matrix[0].length;
    let maxArea = 0;

    const heights = new Array(cols).fill(0);

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (matrix[i][j] === '1') {
                heights[j]++;
            } else {
                heights[j] = 0;
            }
        }
        maxArea = Math.max(maxArea, largestRectangleArea(heights));
    }

    return maxArea;
};

// Helper function for Largest Rectangle in Histogram
var largestRectangleArea = function(heights) {
    const stack = []; // Stores indices
    let maxArea = 0;
    const n = heights.length;

    for (let i = 0; i <= n; i++) {
        const currentHeight = (i === n) ? 0 : heights[i]; // Sentinel value 0 at the end

        while (stack.length > 0 && currentHeight < heights[stack[stack.length - 1]]) {
            const h = heights[stack.pop()];
            const w = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
            maxArea = Math.max(maxArea, h * w);
        }
        stack.push(i);
    }
    return maxArea;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximalRectangle(matrix: string[][]): number {
    if (!matrix || matrix.length === 0 || matrix[0].length === 0) {
        return 0;
    }

    const rows: number = matrix.length;
    const cols: number = matrix[0].length;
    let maxArea: number = 0;

    const heights: number[] = new Array(cols).fill(0);

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (matrix[i][j] === '1') {
                heights[j]++;
            } else {
                heights[j] = 0;
            }
        }
        maxArea = Math.max(maxArea, largestRectangleArea(heights));
    }

    return maxArea;
}

// Helper function for Largest Rectangle in Histogram
function largestRectangleArea(heights: number[]): number {
    const stack: number[] = []; // Stores indices
    let maxArea: number = 0;
    const n: number = heights.length;

    for (let i = 0; i <= n; i++) {
        const currentHeight: number = (i === n) ? 0 : heights[i]; // Sentinel value 0 at the end

        while (stack.length > 0 && currentHeight < heights[stack[stack.length - 1]]) {
            const h: number = heights[stack.pop()!]; // ! asserts that pop() will not return undefined
            const w: number = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
            maxArea = Math.max(maxArea, h * w);
        }
        stack.push(i);
    }
    return maxArea;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[][] $matrix
     * @return Integer
     */
    function maximalRectangle($matrix) {
        if (empty($matrix) || empty($matrix[0])) {
            return 0;
        }

        $rows = count($matrix);
        $cols = count($matrix[0]);
        $maxArea = 0;

        $heights = array_fill(0, $cols, 0);

        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                if ($matrix[$i][$j] === '1') {
                    $heights[$j]++;
                } else {
                    $heights[$j] = 0;
                }
            }
            $maxArea = max($maxArea, $this->largestRectangleArea($heights));
        }

        return $maxArea;
    }

    /**
     * Helper function for Largest Rectangle in Histogram
     * @param Integer[] $heights
     * @return Integer
     */
    private function largestRectangleArea($heights) {
        $stack = []; // Stores indices
        $maxArea = 0;
        $n = count($heights);

        for ($i = 0; $i <= $n; $i++) {
            $currentHeight = ($i === $n) ? 0 : $heights[$i]; // Sentinel value 0 at the end

            while (!empty($stack) && $currentHeight < $heights[end($stack)]) {
                $h = $heights[array_pop($stack)];
                $w = empty($stack) ? $i : $i - end($stack) - 1;
                $maxArea = max($maxArea, $h * $w);
            }
            array_push($stack, $i);
        }
        return $maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximalRectangle(_ matrix: [[Character]]) -> Int {
        if matrix.isEmpty || matrix[0].isEmpty {
            return 0
        }

        let rows = matrix.count
        let cols = matrix[0].count
        var maxArea = 0

        var heights = Array(repeating: 0, count: cols)

        for i in 0..<rows {
            for j in 0..<cols {
                if matrix[i][j] == "1" {
                    heights[j] += 1
                } else {
                    heights[j] = 0
                }
            }
            maxArea = max(maxArea, largestRectangleArea(heights))
        }

        return maxArea
    }

    // Helper function for Largest Rectangle in Histogram
    private func largestRectangleArea(_ heights: [Int]) -> Int {
        var stack: [Int] = [] // Stores indices
        var maxArea = 0
        let n = heights.count

        for i in 0...n {
            let currentHeight = (i == n) ? 0 : heights[i] // Sentinel value 0 at the end

            while !stack.isEmpty && currentHeight < heights[stack.last!] {
                let h = heights[stack.removeLast()]
                let w = stack.isEmpty ? i : i - stack.last! - 1
                maxArea = max(maxArea, h * w)
            }
            stack.append(i)
        }
        return maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.ArrayDeque

class Solution {
    fun maximalRectangle(matrix: Array<CharArray>): Int {
        if (matrix.isEmpty() || matrix[0].isEmpty()) {
            return 0
        }

        val rows = matrix.size
        val cols = matrix[0].size
        val heights = IntArray(cols)
        var maxArea = 0

        for (r in 0 until rows) {
            for (c in 0 until cols) {
                if (matrix[r][c] == '1') {
                    heights[c]++
                } else {
                    heights[c] = 0
                }
            }
            maxArea = Math.max(maxArea, largestRectangleArea(heights))
        }

        return maxArea
    }

    private fun largestRectangleArea(heights: IntArray): Int {
        var maxArea = 0
        val stack = ArrayDeque<Int>() // Stores indices

        for (i in 0..heights.size) {
            val currentHeight = if (i == heights.size) 0 else heights[i]

            while (stack.isNotEmpty() && currentHeight < heights[stack.peek()]) {
                val h = heights[stack.pop()]
                val w = if (stack.isEmpty()) i else i - stack.peek() - 1
                maxArea = Math.max(maxArea, h * w)
            }
            stack.push(i)
        }
        return maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maximalRectangle(List<List<String>> matrix) {
    if (matrix.isEmpty || matrix[0].isEmpty) {
      return 0;
    }

    int rows = matrix.length;
    int cols = matrix[0].length;
    List<int> heights = List<int>.filled(cols, 0);
    int maxArea = 0;

    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        if (matrix[r][c] == '1') {
          heights[c]++;
        } else {
          heights[c] = 0;
        }
      }
      maxArea = maxArea > _largestRectangleArea(heights) ? maxArea : _largestRectangleArea(heights);
    }

    return maxArea;
  }

  int _largestRectangleArea(List<int> heights) {
    int maxArea = 0;
    List<int> stack = []; // Stores indices

    for (int i = 0; i <= heights.length; i++) {
      int currentHeight = (i == heights.length) ? 0 : heights[i];

      while (stack.isNotEmpty && currentHeight < heights[stack.last]) {
        int h = heights[stack.removeLast()];
        int w = stack.isEmpty ? i : i - stack.last - 1;
        maxArea = maxArea > (h * w) ? maxArea : (h * w);
      }
      stack.add(i);
    }
    return maxArea;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maximalRectangle(matrix [][]byte) int {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return 0
    }

    rows := len(matrix)
    cols := len(matrix[0])
    heights := make([]int, cols)
    maxArea := 0

    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if matrix[r][c] == '1' {
                heights[c]++
            } else {
                heights[c] = 0
            }
        }
        maxArea = max(maxArea, largestRectangleArea(heights))
    }

    return maxArea
}

func largestRectangleArea(heights []int) int {
    maxArea := 0
    stack := []int{} // Stores indices

    for i := 0; i <= len(heights); i++ {
        currentHeight := 0
        if i < len(heights) {
            currentHeight = heights[i]
        }

        for len(stack) > 0 && currentHeight < heights[stack[len(stack)-1]] {
            h := heights[stack[len(stack)-1]]
            stack = stack[:len(stack)-1] // Pop

            w := i
            if len(stack) > 0 {
                w = i - stack[len(stack)-1] - 1
            }
            maxArea = max(maxArea, h * w)
        }
        stack = append(stack, i) // Push
    }
    return maxArea
}

func max(a, b int) int {
    if a > b {
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
# @param {Character[][]} matrix
# @return {Integer}
def maximal_rectangle(matrix)
    return 0 if matrix.empty? || matrix[0].empty?

    rows = matrix.length
    cols = matrix[0].length
    heights = Array.new(cols, 0)
    max_area = 0

    rows.times do |r|
        cols.times do |c|
            if matrix[r][c] == '1'
                heights[c] += 1
            else
                heights[c] = 0
            end
        end
        max_area = [max_area, largest_rectangle_area(heights)].max
    end

    max_area
end

def largest_rectangle_area(heights)
    max_area = 0
    stack = [] # Stores indices

    (0..heights.length).each do |i|
        current_height = (i == heights.length) ? 0 : heights[i]

        while !stack.empty? && current_height < heights[stack.last]
            h = heights[stack.pop()]
            w = stack.empty? ? i : i - stack.last - 1
            max_area = [max_area, h * w].max
        end
        stack.push(i)
    end
    max_area
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.Stack

object Solution {
    def maximalRectangle(matrix: Array[Array[Char]]): Int = {
        if (matrix.isEmpty || matrix(0).isEmpty) {
            return 0
        }

        val rows = matrix.length
        val cols = matrix(0).length
        val heights = Array.fill(cols)(0)
        var maxArea = 0

        for (r <- 0 until rows) {
            for (c <- 0 until cols) {
                if (matrix(r)(c) == '1') {
                    heights(c) += 1
                } else {
                    heights(c) = 0
                }
            }
            maxArea = maxArea.max(largestRectangleArea(heights))
        }

        maxArea
    }

    private def largestRectangleArea(heights: Array[Int]): Int = {
        var maxArea = 0
        val stack = new Stack[Int]() // Stores indices

        for (i <- 0 to heights.length) {
            val currentHeight = if (i == heights.length) 0 else heights(i)

            while (stack.nonEmpty && currentHeight < heights(stack.top)) {
                val h = heights(stack.pop())
                val w = if (stack.isEmpty) i else i - stack.top - 1
                maxArea = maxArea.max(h * w)
            }
            stack.push(i)
        }
        maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() || matrix[0].is_empty() {
            return 0;
        }

        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut max_area = 0;
        let mut heights: Vec<i32> = vec![0; cols];

        for i in 0..rows {
            for j in 0..cols {
                if matrix[i][j] == '1' {
                    heights[j] += 1;
                } else {
                    heights[j] = 0;
                }
            }
            max_area = max_area.max(Self::largest_rectangle_in_histogram(&heights));
        }

        max_area
    }

    fn largest_rectangle_in_histogram(heights: &[i32]) -> i32 {
        let n = heights.len();
        let mut max_area = 0;
        let mut stack: Vec<usize> = Vec::new(); // Stores indices

        for i in 0..=n { // Iterate up to n to process remaining stack elements
            let current_height = if i == n { 0 } else { heights[i] };

            while !stack.is_empty() && current_height < heights[*stack.last().unwrap()] {
                let h_idx = stack.pop().unwrap();
                let h = heights[h_idx];
                let width = if stack.is_empty() {
                    i as i32
                } else {
                    (i - stack.last().unwrap() - 1) as i32
                };
                max_area = max_area.max(h * width);
            }
            stack.push(i);
        }
        max_area
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximal-rectangle matrix)
  (-> (listof (listof char?)) exact-integer?)
  (if (or (null? matrix) (null? (car matrix)))
      0 ; Handle empty matrix or empty rows
      (let* ([rows (length matrix)]
             [cols (length (car matrix))])

        (define (largest-rectangle-in-histogram heights)
          (let ([n (length heights)])
            (define (process-bars i stack max-h-area)
              (if (> i n)
                  max-h-area
                  (let ([current-height (if (= i n) 0 (list-ref heights i))])
                    (define (pop-and-calculate current-stack current-max)
                      (if (and (not (null? current-stack))
                               (< current-height (list-ref heights (car current-stack))))
                          (let* ([h-idx (car current-stack)]
                                 [h (list-ref heights h-idx)]
                                 [new-stack (cdr current-stack)]
                                 [width (if (null? new-stack)
                                            i
                                            (- i (car new-stack) 1))])
                            (pop-and-calculate new-stack (max current-max (* h width))))
                          (process-bars (+ i 1) (cons i current-stack) current-max))) ; Push current index
                    (pop-and-calculate stack max-h-area))))) ; Start popping and calculating
            (process-bars 0 '() 0))))

        (define (iterate-rows r current-heights max-overall-area)
          (if (= r rows)
              max-overall-area
              (let* ([row-chars (list-ref matrix r)]
                     [new-heights (for/list ([j (in-range cols)]
                                             [h current-heights])
                                    (if (char=? (list-ref row-chars j) #\1)
                                        (+ h 1)
                                        0))] ; Update heights for current row
                     [area-from-row (largest-rectangle-in-histogram new-heights)])
                (iterate-rows (+ r 1) new-heights (max max-overall-area area-from-row))))) ; Recurse to next row

        (iterate-rows 0 (make-list cols 0) 0))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximal_rectangle(Matrix :: [[char()]]) -> integer().
maximal_rectangle(Matrix) ->
Rows = length(Matrix),
Cols = if Rows == 0 -> 0; true -> length(hd(Matrix)) end,

if Rows == 0 orelse Cols == 0 ->
0;
true ->
InitialHeights = lists:duplicate(Cols, 0),
maximal_rectangle_loop(Matrix, 0, Rows, Cols, InitialHeights, 0)
end.

maximal_rectangle_loop(_Matrix, RowIdx, Rows, _Cols, _Heights, MaxArea) when RowIdx == Rows ->
MaxArea;
maximal_rectangle_loop(Matrix, RowIdx, Rows, Cols, CurrentHeights, MaxArea) ->
CurrentRow = lists:nth(RowIdx + 1, Matrix),
NewHeights = update_heights(CurrentRow, CurrentHeights, 0, Cols, []),
AreaFromRow = largest_rectangle_in_histogram(NewHeights),
NewMaxArea = max(MaxArea, AreaFromRow),
maximal_rectangle_loop(Matrix, RowIdx + 1, Rows, Cols, NewHeights, NewMaxArea).

update_heights(_CurrentRow, _CurrentHeights, J, Cols, Acc) when J == Cols ->
lists:reverse(Acc);
update_heights(CurrentRow, CurrentHeights, J, Cols, Acc) ->
Char = lists:nth(J + 1, CurrentRow),
H = lists:nth(J + 1, CurrentHeights),
NewH = if Char == $1 -> H + 1; true -> 0 end,
update_heights(CurrentRow, CurrentHeights, J + 1, Cols, [NewH | Acc]).

largest_rectangle_in_histogram(Heights) ->
N = length(Heights),
ExtendedHeights = Heights ++ [0],
largest_rectangle_in_histogram_loop(0, N, ExtendedHeights, [], 0).

largest_rectangle_in_histogram_loop(I, N, Heights, Stack, MaxArea) when I > N ->
MaxArea;
largest_rectangle_in_histogram_loop(I, N, Heights, Stack, MaxArea) ->
CurrentHeight = lists:nth(I + 1, Heights),
{NewStack, CurrentMaxArea} = pop_and_calculate(I, CurrentHeight, Heights, Stack, MaxArea),
largest_rectangle_in_histogram_loop(I + 1, N, Heights, [I | NewStack], CurrentMaxArea).

pop_and_calculate(I, CurrentHeight, Heights, Stack, CurrentMax) ->
case Stack of
[] ->
    {Stack, CurrentMax};
[H_idx | RestStack] ->
    H_at_stack_top = lists:nth(H_idx + 1, Heights),
    if CurrentHeight < H_at_stack_top ->
        H = H_at_stack_top,
        Width = case RestStack of
                    [] -> I;
                    [Prev_H_idx | _] -> I - Prev_H_idx - 1
                end,
        pop_and_calculate(I, CurrentHeight, Heights, RestStack, max(CurrentMax, H * Width));
    true ->
        {Stack, CurrentMax}
    end
end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximal_rectangle(matrix :: [[char]]) :: integer
  def maximal_rectangle(matrix) do
    rows = length(matrix)
    cols = if rows == 0, do: 0, else: length(hd(matrix))

    if rows == 0 || cols == 0 do
      0
    else
      initial_heights = List.duplicate(0, cols)
      maximal_rectangle_loop(matrix, 0, rows, cols, initial_heights, 0)
    end
  end

  defp maximal_rectangle_loop(_matrix, row_idx, rows, _cols, _heights, max_area) when row_idx == rows do
    max_area
  end

  defp maximal_rectangle_loop(matrix, row_idx, rows, cols, current_heights, max_area) do
    current_row = Enum.at(matrix, row_idx)
    new_heights = update_heights(current_row, current_heights, 0, cols, [])
    area_from_row = largest_rectangle_in_histogram(new_heights)
    new_max_area = max(max_area, area_from_row)
    maximal_rectangle_loop(matrix, row_idx + 1, rows, cols, new_heights, new_max_area)
  end

  defp update_heights(_current_row, _current_heights, j, cols, acc) when j == cols do
    Enum.reverse(acc)
  end

  defp update_heights(current_row, current_heights, j, cols, acc) do
    char = Enum.at(current_row, j)
    h = Enum.at(current_heights, j)
    new_h = if char == ?1, do: h + 1, else: 0
    update_heights(current_row, current_heights, j + 1, cols, [new_h | acc])
  end

  defp largest_rectangle_in_histogram(heights) do
    n = length(heights)
    extended_heights = heights ++ [0] # Append 0 to ensure all stack elements are processed
    largest_rectangle_in_histogram_loop(0, n, extended_heights, [], 0)
  end

  defp largest_rectangle_in_histogram_loop(i, n, heights, stack, max_area) when i > n do
    max_area
  end

  defp largest_rectangle_in_histogram_loop(i, n, heights, stack, max_area) do
    current_height = Enum.at(heights, i)
    {new_stack, current_max_area} = pop_and_calculate(i, current_height, heights, stack, max_area)
    largest_rectangle_in_histogram_loop(i + 1, n, heights, [i | new_stack], current_max_area)
  end

  defp pop_and_calculate(i, current_height, heights, stack, current_max) do
    case stack do
      [] ->
        {stack, current_max}
      [h_idx | rest_stack] ->
        h_at_stack_top = Enum.at(heights, h_idx)
        if current_height < h_at_stack_top do
          h = h_at_stack_top
          width = case rest_stack do
                      [] -> i
                      [prev_h_idx | _] -> i - prev_h_idx - 1
                    end
          pop_and_calculate(i, current_height, heights, rest_stack, max(current_max, h * width))
        else
          {stack, current_max}
        end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The algorithm iterates through each of the `rows`. In each row, it processes `cols` elements to update the `heights` array, taking `O(cols)` time. Subsequently, the `largestRectangleArea` helper function is called, which processes the `heights` array of size `cols` using a monotonic stack. This helper function also takes `O(cols)` time as each element is pushed and popped from the stack at most once. Therefore, the total time complexity is `O(rows * cols)`.

- **Space Complexity:** The primary space usage comes from the `heights` array, which stores `cols` integers, and the monotonic stack used within the `largestRectangleArea` function, which can store up to `cols` indices in the worst case. Thus, the total space complexity is `O(cols)`.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-11 01:19:10 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The algorithm to solve this problem involves using a histogram-based approach. For each row in the matrix, we calculate the height of the histogram by adding the current cell's value to the height of the cell above it if the current cell is 1, and resetting the height to 0 if the current cell is 0. Then, we use a stack-based approach to find the maximum area of the histogram. We iterate through the histogram, pushing the index of each bar onto the stack if the stack is empty or the current bar is higher than the bar at the top of the stack. If the current bar is lower than the bar at the top of the stack, we calculate the area of the rectangle with the bar at the top of the stack as the smallest bar and update the maximum area if necessary. We repeat this process until the stack is empty, at which point we have found the maximum area of the histogram for the current row. We repeat this process for each row in the matrix to find the maximum area of the rectangle containing only 1's. The key intuition behind this approach is that the maximum area of the rectangle containing only 1's can be found by considering each row as a histogram and finding the maximum area of the histogram for each row.

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
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) return 0;
        int rows = matrix.size(), cols = matrix[0].size();
        vector<int> height(cols + 1, 0);
        int maxArea = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                height[j] = matrix[i][j] == '1' ? height[j] + 1 : 0;
            }
            stack<int> s;
            for (int j = 0; j <= cols; j++) {
                while (!s.empty() && height[j] < height[s.top()]) {
                    int h = height[s.top()]; s.pop();
                    int w = s.empty() ? j : j - s.top() - 1;
                    maxArea = max(maxArea, h * w);
                }
                s.push(j);
            }
        }
        return maxArea;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int rows = matrix.length, cols = matrix[0].length;
        int[] height = new int[cols + 1];
        int maxArea = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                height[j] = matrix[i][j] == '1' ? height[j] + 1 : 0;
            }
            java.util.Stack<Integer> s = new java.util.Stack<>();
            for (int j = 0; j <= cols; j++) {
                while (!s.isEmpty() && height[j] < height[s.peek()]) {
                    int h = height[s.peek()]; s.pop();
                    int w = s.isEmpty() ? j : j - s.peek() - 1;
                    maxArea = Math.max(maxArea, h * w);
                }
                s.push(j);
            }
        }
        return maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0
        rows, cols = len(matrix), len(matrix[0])
        height = [0] * (cols + 1)
        maxArea = 0
        for row in matrix:
            for j in range(cols):
                height[j] = height[j] + 1 if row[j] == '1' else 0
            stack = []
            for j in range(cols + 1):
                while stack and height[j] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = j if not stack else j - stack[-1] - 1
                    maxArea = max(maxArea, h * w)
                stack.append(j)
        return maxArea
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        rows, cols = len(matrix), len(matrix[0])
        height = [0] * (cols + 1)
        maxArea = 0
        for row in matrix:
            for j in range(cols):
                height[j] = height[j] + 1 if row[j] == '1' else 0
            stack = []
            for j in range(cols + 1):
                while stack and height[j] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = j if not stack else j - stack[-1] - 1
                    maxArea = max(maxArea, h * w)
                stack.append(j)
        return maxArea
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maximalRectangle(char** matrix, int matrixSize, int* matrixColSize) {
    if (matrixSize == 0 || matrixColSize[0] == 0) return 0;
    int rows = matrixSize, cols = matrixColSize[0];
    int* height = (int*)malloc((cols + 1) * sizeof(int));
    for (int i = 0; i <= cols; i++) height[i] = 0;
    int maxArea = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            height[j] = matrix[i][j] == '1' ? height[j] + 1 : 0;
        }
        int* stack = (int*)malloc((cols + 1) * sizeof(int));
        int top = -1;
        for (int j = 0; j <= cols; j++) {
            while (top != -1 && height[j] < height[stack[top]]) {
                int h = height[stack[top]];
                top--;
                int w = top == -1 ? j : j - stack[top] - 1;
                maxArea = maxArea > h * w ? maxArea : h * w;
            }
            stack[++top] = j;
        }
        free(stack);
    }
    free(height);
    return maxArea;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximalRectangle(char[][] matrix) {
        if (matrix.Length == 0) return 0;
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        int[] height = new int[cols + 1];
        int maxArea = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                height[j] = matrix[i][j] == '1' ? height[j] + 1 : 0;
            }
            int[] stack = new int[cols + 1];
            int top = -1;
            for (int j = 0; j <= cols; j++) {
                if (top == -1 || height[j] >= height[stack[top]]) {
                    stack[++top] = j;
                } else {
                    while (top != -1 && height[j] < height[stack[top]]) {
                        int h = height[stack[top--]];
                        int w = top == -1 ? j : j - stack[top] - 1;
                        maxArea = Math.Max(maxArea, h * w);
                    }
                    stack[++top] = j;
                }
            }
        }
        return maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maximalRectangle = function(matrix) {
    if (matrix.length == 0) return 0;
    let rows = matrix.length;
    let cols = matrix[0].length;
    let height = new Array(cols + 1).fill(0);
    let maxArea = 0;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            height[j] = matrix[i][j] == '1' ? height[j] + 1 : 0;
        }
        let stack = [];
        let top = -1;
        for (let j = 0; j <= cols; j++) {
            if (top == -1 || height[j] >= height[stack[top]]) {
                stack.push(j);
                top++;
            } else {
                while (top != -1 && height[j] < height[stack[top]]) {
                    let h = height[stack.pop()];
                    top--;
                    let w = top == -1 ? j : j - stack[stack.length - 1] - 1;
                    maxArea = Math.max(maxArea, h * w);
                }
                stack.push(j);
                top++;
            }
        }
    }
    return maxArea;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximalRectangle(matrix: string[][]): number {
    if (matrix.length == 0) return 0;
    let rows = matrix.length;
    let cols = matrix[0].length;
    let height: number[] = new Array(cols + 1).fill(0);
    let maxArea = 0;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            height[j] = matrix[i][j] == '1' ? height[j] + 1 : 0;
        }
        let stack: number[] = [];
        let top = -1;
        for (let j = 0; j <= cols; j++) {
            if (top == -1 || height[j] >= height[stack[top]]) {
                stack.push(j);
                top++;
            } else {
                while (top != -1 && height[j] < height[stack[top]]) {
                    let h = height[stack.pop()!];
                    top--;
                    let w = top == -1 ? j : j - stack[stack.length - 1] - 1;
                    maxArea = Math.max(maxArea, h * w);
                }
                stack.push(j);
                top++;
            }
        }
    }
    return maxArea;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maximalRectangle($matrix) {
        if (empty($matrix)) return 0;
        $rows = count($matrix);
        $cols = count($matrix[0]);
        $height = array_fill(0, $cols + 1, 0);
        $maxArea = 0;
        for ($i = 0; $i < $rows; $i++) {
            for ($j = 0; $j < $cols; $j++) {
                $height[$j] = $matrix[$i][$j] == '1' ? $height[$j] + 1 : 0;
            }
            $stack = [];
            $top = -1;
            for ($j = 0; $j <= $cols; $j++) {
                if ($top == -1 || $height[$j] >= $height[$stack[$top]]) {
                    $stack[++$top] = $j;
                } else {
                    while ($top != -1 && $height[$j] < $height[$stack[$top]]) {
                        $h = $height[array_pop($stack)];
                        $top--;
                        $w = $top == -1 ? $j : $j - $stack[$top] - 1;
                        $maxArea = max($maxArea, $h * $w);
                    }
                    $stack[++$top] = $j;
                }
            }
        }
        return $maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximalRectangle(_ matrix: [[Character]]) -> Int {
        if matrix.isEmpty { return 0 }
        let rows = matrix.count
        let cols = matrix[0].count
        var height = Array(repeating: 0, count: cols + 1)
        var maxArea = 0
        for i in 0..<rows {
            for j in 0..<cols {
                height[j] = matrix[i][j] == "1" ? height[j] + 1 : 0
            }
            var stack: [Int] = []
            var top = -1
            for j in 0...cols {
                if top == -1 || height[j] >= height[stack[top]] {
                    stack.append(j)
                    top += 1
                } else {
                    while top != -1 && height[j] < height[stack[top]] {
                        let h = height[stack.removeLast()]
                        top -= 1
                        let w = top == -1 ? j : j - stack.last! - 1
                        maxArea = max(maxArea, h * w)
                    }
                    stack.append(j)
                    top += 1
                }
            }
        }
        return maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximalRectangle(matrix: Array<CharArray>): Int {
        if (matrix.isEmpty() || matrix[0].isEmpty()) return 0
        val n = matrix[0].size
        val height = IntArray(n + 1)
        var maxArea = 0
        for (row in matrix) {
            for (i in 0 until n) {
                height[i] = if (row[i] == '1') height[i] + 1 else 0
            }
            val stack = ArrayDeque<Int>()
            for (i in 0..n) {
                while (!stack.isEmpty() && (i == n || height[i] < height[stack.last()])) {
                    val h = height[stack.removeLast()]
                    val w = if (stack.isEmpty()) i else i - stack.last() - 1
                    maxArea = maxOf(maxArea, h * w)
                }
                stack.addLast(i)
            }
        }
        return maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maximalRectangle(List<List<String>> matrix) {
    if (matrix.isEmpty || matrix[0].isEmpty) return 0;
    int n = matrix[0].length;
    List<int> height = List<int>.filled(n + 1, 0);
    int maxArea = 0;
    for (var row in matrix) {
      for (int i = 0; i < n; i++) {
        height[i] = row[i] == '1' ? height[i] + 1 : 0;
      }
      List<int> stack = [];
      for (int i = 0; i <= n; i++) {
        while (stack.isNotEmpty && (i == n || height[i] < height[stack.last])) {
          int h = height[stack.removeLast()];
          int w = stack.isEmpty ? i : i - stack.last - 1;
          maxArea = maxArea > h * w ? maxArea : h * w;
        }
        stack.add(i);
      }
    }
    return maxArea;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maximalRectangle(matrix [][]byte) int {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return 0
    }
    n := len(matrix[0])
    height := make([]int, n+1)
    maxArea := 0
    for _, row := range matrix {
        for i := 0; i < n; i++ {
            if row[i] == '1' {
                height[i] += 1
            } else {
                height[i] = 0
            }
        }
        stack := []int{}
        for i := 0; i <= n; i++ {
            for len(stack) > 0 && (i == n || height[i] < height[stack[len(stack)-1]]) {
                h := height[stack[len(stack)-1]]
                w := i
                if len(stack) > 0 {
                    w = i - stack[len(stack)-1] - 1
                }
                if h*w > maxArea {
                    maxArea = h * w
                }
                stack = stack[:len(stack)-1]
            }
            stack = append(stack, i)
        }
    }
    return maxArea
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def maximal_rectangle(matrix)
    return 0 if matrix.empty? || matrix[0].empty?
    n = matrix[0].size
    height = Array.new(n + 1, 0)
    max_area = 0
    matrix.each do |row|
        (0...n).each do |i|
            height[i] = row[i] == '1' ? height[i] + 1 : 0
        end
        stack = []
        (0..n).each do |i|
            while !stack.empty? && (i == n || height[i] < height[stack.last])
                h = height[stack.pop]
                w = stack.empty? ? i : i - stack.last - 1
                max_area = [max_area, h * w].max
            end
            stack.push(i)
        end
    end
    max_area
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximalRectangle(matrix: Array[Array[Char]]): Int = {
        if (matrix.isEmpty || matrix(0).isEmpty) return 0
        val n = matrix(0).length
        val height = Array.ofDim[Int](n + 1)
        var maxArea = 0
        for (row <- matrix) {
            for (i <- 0 until n) {
                height(i) = if (row(i) == '1') height(i) + 1 else 0
            }
            val stack = scala.collection.mutable.Stack[Int]()
            for (i <- 0 to n) {
                while (!stack.isEmpty && (i == n || height(i) < height(stack.top))) {
                    val h = height(stack.pop)
                    val w = if (stack.isEmpty) i else i - stack.top - 1
                    maxArea = math.max(maxArea, h * w)
                }
                stack.push(i)
            }
        }
        maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut height = vec![0; cols];
        let mut max_area = 0;
        for row in 0..rows {
            for col in 0..cols {
                if matrix[row][col] == '1' {
                    height[col] += 1;
                } else {
                    height[col] = 0;
                }
            }
            let mut stack = Vec::new();
            let mut col = 0;
            while col < cols {
                if stack.is_empty() || height[col] >= height[*stack.last().unwrap()] {
                    stack.push(col);
                    col += 1;
                } else {
                    let top = stack.pop().unwrap();
                    let width = if stack.is_empty() { col } else { col - stack.last().unwrap() - 1 };
                    max_area = max_area.max(height[top] * width as i32);
                }
            }
            while !stack.is_empty() {
                let top = stack.pop().unwrap();
                let width = if stack.is_empty() { col } else { col - stack.last().unwrap() - 1 };
                max_area = max_area.max(height[top] * width as i32);
            }
        }
        max_area
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximal-rectangle matrix)
  (-> (listof (listof char?)) exact-integer?)
  (let* (
           [rows (length matrix)]
           [cols (length (car matrix))]
           [height (make-vector cols 0)]
           [max-area 0])
    (for-each
     (lambda (row)
       (for-each
        (lambda (col val)
          (if (eq? val #\1)
              (vector-set! height col (+ (vector-ref height col) 1))
              (vector-set! height col 0)))
        row
        (build-list cols values))
       (let loop (
                 [col 0]
                 [stack '()])
         (cond
          [(= col cols)
           (loop2 stack)]
          [(or (null? stack) (>= (vector-ref height col) (vector-ref height (car stack))))
           (loop (+ col 1) (cons col stack))]
          [else
           (let* (
                    [top (car stack)]
                    [width (if (null? stack) col (- col (car stack) 1))])
             (set! max-area (max max-area (* (vector-ref height top) width)))
             (loop col (cdr stack)))]))
       (define (loop2 stack)
         (cond
          [(null? stack) max-area]
          [else
           (let* (
                    [top (car stack)]
                    [width (if (null? stack) cols (- cols (car stack) 1))])
             (set! max-area (max max-area (* (vector-ref height top) width)))
             (loop2 (cdr stack)))])))
     matrix)
    max-area))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
maximal_rectangle(Matrix) ->
  Rows = length(Matrix),
  Cols = length(hd(Matrix)),
  Height = array:new(Cols, {default, 0}),
  MaxArea = 0,
  maximal_rectangle(Matrix, Rows, Cols, Height, MaxArea).

maximal_rectangle([Row|Rows], Rows, Cols, Height, MaxArea) ->
  NewHeight = lists:foldl(fun ({Col, Val}, H) ->
                             if Val =:= $1 ->
                                 array:set(Col, array:get(Col, H) + 1, H);
                             true ->
                                 array:set(Col, 0, H)
                         end
                     end, Height, Row),
  {NewMaxArea, _} = maximal_rectangle_row(NewHeight, Cols, MaxArea, []),
  maximal_rectangle(Rows, Rows, Cols, Height, NewMaxArea);
maximal_rectangle([], _, _, _, MaxArea) -> MaxArea.

maximal_rectangle_row(Height, Cols, MaxArea, Stack) ->
  maximal_rectangle_row(Height, Cols, MaxArea, Stack, 0).
maximal_rectangle_row(Height, Cols, MaxArea, Stack, Col) when Col < Cols ->
  case Stack of
    [] ->
      maximal_rectangle_row(Height, Cols, MaxArea, [Col], Col + 1);
    [Top|T] ->
      case array:get(Col, Height) >= array:get(Top, Height) of
        true ->
          maximal_rectangle_row(Height, Cols, MaxArea, [Col|Stack], Col + 1);
        false ->
          {NewMaxArea, NewStack} =
            case Stack of
              [] -> {max(MaxArea, array:get(Top, Height) * Col), T};
              _ -> {max(MaxArea, array:get(Top, Height) * (Col - hd(Stack) - 1)), T}
            end,
          maximal_rectangle_row(Height, Cols, NewMaxArea, NewStack, Col)
      end
  end;
maximal_rectangle_row(Height, Cols, MaxArea, Stack, Col) when Col >= Cols ->
  lists:foldl(fun (Top, {MaxA, Stack1}) ->
                  {max(MaxA, array:get(Top, Height) * (Col - hd(Stack1) - 1)), tl(Stack1)}
              end, {MaxArea, Stack}, Stack).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximal_rectangle(matrix :: [[char]]) :: integer
  def maximal_rectangle(matrix) do
    rows = length(matrix)
    cols = length(Enum.at(matrix, 0))
    height = Array.new(cols, 0)
    max_area = 0
    maximal_rectangle(matrix, rows, cols, height, max_area)
  end

  defp maximal_rectangle([row|rows], rows, cols, height, max_area) do
    new_height = Enum.reduce(Enum.with_index(row), height, fn {val, col}, h ->
                                if val == ?1 do
                                  Array.set(h, col, Array.get(h, col) + 1)
                                else
                                  Array.set(h, col, 0)
                                end
                              end)
    {new_max_area, _} = maximal_rectangle_row(new_height, cols, max_area, [])
    maximal_rectangle(rows, rows, cols, height, new_max_area)
  end

  defp maximal_rectangle([], _, _, _, max_area) do
    max_area
  end

  defp maximal_rectangle_row(height, cols, max_area, stack) do
    maximal_rectangle_row(height, cols, max_area, stack, 0)
  end

  defp maximal_rectangle_row(height, cols, max_area, stack, col) when col < cols do
    case stack do
      [] ->
        maximal_rectangle_row(height, cols, max_area, [col], col + 1)
      [top|t] ->
        case Array.get(height, col) >= Array.get(height, top) do
          true ->
            maximal_rectangle_row(height, cols, max_area, [col|stack], col + 1)
          false ->
            {new_max_area, new_stack} =
              case stack do
                [] -> {max(max_area, Array.get(height, top) * col), t}
                _ -> {max(max_area, Array.get(height, top) * (col - hd(stack) - 1)), t}
              end,
            maximal_rectangle_row(height, cols, new_max_area, new_stack, col)
        end
    end
  end

  defp maximal_rectangle_row(height, cols, max_area, stack, col) when col >= cols do
    Enum.reduce(stack, {max_area, stack}, fn top, {max_a, stack1} ->
                             {max(max_a, Array.get(height, top) * (col - hd(stack1) - 1)), tl(stack1)}
                           end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this algorithm is O(rows * cols), where rows is the number of rows in the matrix and cols is the number of columns in the matrix. This is because we are iterating through each cell in the matrix once to calculate the height of the histogram, and then iterating through the histogram once to find the maximum area. The space complexity is O(cols), which is the maximum size of the stack.

- **Space Complexity:** The space complexity of this algorithm is O(cols), which is the maximum size of the stack. This is because in the worst-case scenario, we may need to push all the indices of the histogram onto the stack, which can happen if the histogram is strictly decreasing.

</div>
</details>
