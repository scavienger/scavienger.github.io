---
layout: post
title: "Minimum Operations to Make a Uni-Value Grid"
date: 2026-04-28 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Sorting", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n#include <cmath>\n\nusing namespace\
        \ std;\n\nclass Solution {\npublic:\n    int minOperations(vector<vector<int>>&\
        \ grid, int x) {\n        int m = grid.size();\n        int n = grid[0].size();\n\
        \        vector<int> nums;\n        nums.reserve(m * n);\n\n        int rem\
        \ = grid[0][0] % x;\n        for (int i = 0; i < m; ++i) {\n            for\
        \ (int j = 0; j < n; ++j) {\n                if (grid[i][j] % x != rem) {\n\
        \                    return -1;\n                }\n                nums.push_back(grid[i][j]);\n\
        \            }\n        }\n\n        sort(nums.begin(), nums.end());\n     \
        \   int median = nums[nums.size() / 2];\n        int operations = 0;\n\n   \
        \     for (int val : nums) {\n            operations += abs(val - median) /\
        \ x;\n        }\n\n        return operations;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int minOperations(int[][]\
        \ grid, int x) {\n        int m = grid.length;\n        int n = grid[0].length;\n\
        \        int[] arr = new int[m * n];\n        int k = 0;\n\n        int rem\
        \ = grid[0][0] % x;\n        for (int i = 0; i < m; i++) {\n            for\
        \ (int j = 0; j < n; j++) {\n                if (grid[i][j] % x != rem) {\n\
        \                    return -1;\n                }\n                arr[k++]\
        \ = grid[i][j];\n            }\n        }\n\n        Arrays.sort(arr);\n   \
        \     int median = arr[arr.length / 2];\n        int operations = 0;\n\n   \
        \     for (int val : arr) {\n            operations += Math.abs(val - median)\
        \ / x;\n        }\n\n        return operations;\n    }\n}"
      python: "class Solution(object):\n    def minOperations(self, grid, x):\n    \
        \    \"\"\"\n        :type grid: List[List[int]]\n        :type x: int\n   \
        \     :rtype: int\n        \"\"\"\n        nums = []\n        for row in grid:\n\
        \            for val in row:\n                nums.append(val)\n\n        rem\
        \ = nums[0] % x\n        for val in nums:\n            if val % x != rem:\n\
        \                return -1\n\n        nums.sort()\n        median = nums[len(nums)\
        \ // 2]\n\n        total_operations = 0\n        for val in nums:\n        \
        \    total_operations += abs(val - median) // x\n\n        return total_operations"
      python3: "class Solution:\n    def minOperations(self, grid: List[List[int]],\
        \ x: int) -> int:\n        nums = []\n        for row in grid:\n           \
        \ nums.extend(row)\n\n        rem = nums[0] % x\n        for val in nums:\n\
        \            if val % x != rem:\n                return -1\n\n        nums.sort()\n\
        \        median = nums[len(nums) // 2]\n\n        return sum(abs(val - median)\
        \ // x for val in nums)"
      c: "#include <stdlib.h>\n#include <stdio.h>\n\nint compare(const void* a, const\
        \ void* b) {\n    return (*(int*)a - *(int*)b);\n}\n\nint minOperations(int**\
        \ grid, int gridSize, int* gridColSize, int x) {\n    int m = gridSize;\n  \
        \  int n = gridColSize[0];\n    int totalElements = 0;\n    for (int i = 0;\
        \ i < m; i++) {\n        totalElements += gridColSize[i];\n    }\n\n    int*\
        \ arr = (int*)malloc(totalElements * sizeof(int));\n    int k = 0;\n    int\
        \ rem = grid[0][0] % x;\n\n    for (int i = 0; i < m; i++) {\n        for (int\
        \ j = 0; j < gridColSize[i]; j++) {\n            if (grid[i][j] % x != rem)\
        \ {\n                free(arr);\n                return -1;\n            }\n\
        \            arr[k++] = grid[i][j];\n        }\n    }\n\n    qsort(arr, totalElements,\
        \ sizeof(int), compare);\n\n    int median = arr[totalElements / 2];\n    int\
        \ operations = 0;\n    for (int i = 0; i < totalElements; i++) {\n        operations\
        \ += abs(arr[i] - median) / x;\n    }\n\n    free(arr);\n    return operations;\n\
        }"
      csharp: "using System;\n\npublic class Solution {\n    public int MinOperations(int[][]\
        \ grid, int x) {\n        int m = grid.Length;\n        int n = grid[0].Length;\n\
        \        int[] nums = new int[m * n];\n        int k = 0;\n        for (int\
        \ i = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n        \
        \        nums[k++] = grid[i][j];\n            }\n        }\n\n        int remainder\
        \ = nums[0] % x;\n        foreach (int num in nums) {\n            if (num %\
        \ x != remainder) {\n                return -1;\n            }\n        }\n\n\
        \        Array.Sort(nums);\n        int median = nums[nums.Length / 2];\n  \
        \      int totalOperations = 0;\n\n        foreach (int num in nums) {\n   \
        \         totalOperations += Math.Abs(num - median) / x;\n        }\n\n    \
        \    return totalOperations;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @param {number} x\n * @return\
        \ {number}\n */\nvar minOperations = function(grid, x) {\n    let nums = [];\n\
        \    for (let i = 0; i < grid.length; i++) {\n        for (let j = 0; j < grid[i].length;\
        \ j++) {\n            nums.push(grid[i][j]);\n        }\n    }\n\n    const\
        \ remainder = nums[0] % x;\n    for (let i = 0; i < nums.length; i++) {\n  \
        \      if (nums[i] % x !== remainder) {\n            return -1;\n        }\n\
        \    }\n\n    nums.sort((a, b) => a - b);\n    const median = nums[Math.floor(nums.length\
        \ / 2)];\n    let totalOperations = 0;\n\n    for (const num of nums) {\n  \
        \      totalOperations += Math.abs(num - median) / x;\n    }\n\n    return totalOperations;\n\
        };"
      typescript: "function minOperations(grid: number[][], x: number): number {\n \
        \   let nums: number[] = [];\n    for (let i = 0; i < grid.length; i++) {\n\
        \        for (let j = 0; j < grid[i].length; j++) {\n            nums.push(grid[i][j]);\n\
        \        }\n    }\n\n    const remainder = nums[0] % x;\n    for (let i = 0;\
        \ i < nums.length; i++) {\n        if (nums[i] % x !== remainder) {\n      \
        \      return -1;\n        }\n    }\n\n    nums.sort((a, b) => a - b);\n   \
        \ const median = nums[Math.floor(nums.length / 2)];\n    let totalOperations\
        \ = 0;\n\n    for (const num of nums) {\n        totalOperations += Math.abs(num\
        \ - median) / x;\n    }\n\n    return totalOperations;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @param\
        \ Integer $x\n     * @return Integer\n     */\n    function minOperations($grid,\
        \ $x) {\n        $nums = [];\n        foreach ($grid as $row) {\n          \
        \  foreach ($row as $val) {\n                $nums[] = $val;\n            }\n\
        \        }\n\n        $remainder = $nums[0] % $x;\n        foreach ($nums as\
        \ $num) {\n            if ($num % $x !== $remainder) {\n                return\
        \ -1;\n            }\n        }\n\n        sort($nums);\n        $n = count($nums);\n\
        \        $median = $nums[(int)($n / 2)];\n        $totalOperations = 0;\n\n\
        \        foreach ($nums as $num) {\n            $totalOperations += intdiv(abs($num\
        \ - $median), $x);\n        }\n\n        return $totalOperations;\n    }\n}"
      swift: "class Solution {\n    func minOperations(_ grid: [[Int]], _ x: Int) ->\
        \ Int {\n        var nums = [Int]()\n        for row in grid {\n           \
        \ for val in row {\n                nums.append(val)\n            }\n      \
        \  }\n\n        let remainder = nums[0] % x\n        for num in nums {\n   \
        \         if num % x != remainder {\n                return -1\n           \
        \ }\n        }\n\n        nums.sort()\n        let median = nums[nums.count\
        \ / 2]\n        var totalOperations = 0\n\n        for num in nums {\n     \
        \       totalOperations += abs(num - median) / x\n        }\n\n        return\
        \ totalOperations\n    }\n}"
      kotlin: "class Solution {\n    fun minOperations(grid: Array<IntArray>, x: Int):\
        \ Int {\n        val m = grid.size\n        val n = grid[0].size\n        val\
        \ nums = IntArray(m * n)\n        val rem = grid[0][0] % x\n        var k =\
        \ 0\n        for (i in 0 until m) {\n            for (j in 0 until n) {\n  \
        \              if (grid[i][j] % x != rem) return -1\n                nums[k++]\
        \ = grid[i][j]\n            }\n        }\n        nums.sort()\n        val median\
        \ = nums[nums.size / 2]\n        var ops = 0\n        for (num in nums) {\n\
        \            ops += Math.abs(num - median) / x\n        }\n        return ops\n\
        \    }\n}"
      dart: "class Solution {\n  int minOperations(List<List<int>> grid, int x) {\n\
        \    int m = grid.length;\n    int n = grid[0].length;\n    List<int> nums =\
        \ List.filled(m * n, 0);\n    int k = 0;\n    int rem = grid[0][0] % x;\n  \
        \  for (int i = 0; i < m; i++) {\n      for (int j = 0; j < n; j++) {\n    \
        \    if (grid[i][j] % x != rem) return -1;\n        nums[k++] = grid[i][j];\n\
        \      }\n    }\n    nums.sort();\n    int median = nums[nums.length ~/ 2];\n\
        \    int ops = 0;\n    for (int num in nums) {\n      ops += (num - median).abs()\
        \ ~/ x;\n    }\n    return ops;\n  }\n}"
      go: "import \"sort\"\n\nfunc minOperations(grid [][]int, x int) int {\n\tm :=\
        \ len(grid)\n\tn := len(grid[0])\n\tnums := make([]int, m*n)\n\tk := 0\n\trem\
        \ := grid[0][0] % x\n\tfor i := 0; i < m; i++ {\n\t\tfor j := 0; j < n; j++\
        \ {\n\t\t\tif grid[i][j]%x != rem {\n\t\t\t\treturn -1\n\t\t\t}\n\t\t\tnums[k]\
        \ = grid[i][j]\n\t\t\tk++\n\t\t}\n\t}\n\tsort.Ints(nums)\n\tmedian := nums[len(nums)/2]\n\
        \tops := 0\n\tfor _, v := range nums {\n\t\tdiff := v - median\n\t\tif diff\
        \ < 0 {\n\t\t\tdiff = -diff\n\t\t}\n\t\tops += diff / x\n\t}\n\treturn ops\n\
        }"
      ruby: "# @param {Integer[][]} grid\n# @param {Integer} x\n# @return {Integer}\n\
        def min_operations(grid, x)\n  nums = grid.flatten\n  rem = nums[0] % x\n  nums.each\
        \ do |num|\n    return -1 if num % x != rem\n  end\n  nums.sort!\n  median =\
        \ nums[nums.length / 2]\n  ops = 0\n  nums.each do |num|\n    ops += (num -\
        \ median).abs / x\n  end\n  ops\nend"
      scala: "object Solution {\n    def minOperations(grid: Array[Array[Int]], x: Int):\
        \ Int = {\n        val m = grid.length\n        val n = grid(0).length\n   \
        \     val nums = grid.flatten\n        val rem = nums(0) % x\n        if (nums.exists(_\
        \ % x != rem)) return -1\n        val sortedNums = nums.sorted\n        val\
        \ median = sortedNums(sortedNums.length / 2)\n        var ops = 0\n        for\
        \ (num <- sortedNums) {\n            ops += Math.abs(num - median) / x\n   \
        \     }\n        ops\n    }\n}"
      rust: "impl Solution {\n    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32)\
        \ -> i32 {\n        let mut flat: Vec<i32> = grid.into_iter().flatten().collect();\n\
        \        let first_rem = flat[0] % x;\n        for &val in &flat {\n       \
        \     if val % x != first_rem {\n                return -1;\n            }\n\
        \        }\n        flat.sort_unstable();\n        let median = flat[flat.len()\
        \ / 2];\n        let mut operations = 0;\n        for &val in &flat {\n    \
        \        operations += (val - median).abs() / x;\n        }\n        operations\n\
        \    }\n}"
      racket: "(define/contract (min-operations grid x)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer? exact-integer?)\n  (let* ([flat (flatten grid)]\n         [first-rem\
        \ (modulo (car flat) x)])\n    (if (not (andmap (lambda (v) (= (modulo v x)\
        \ first-rem)) flat))\n        -1\n        (let* ([sorted (sort flat <)]\n  \
        \             [len (length sorted)]\n               [median (list-ref sorted\
        \ (quotient len 2))])\n          (foldl (lambda (v acc) (+ acc (quotient (abs\
        \ (- v median)) x))) 0 sorted)))))"
      erlang: "-spec min_operations(Grid :: [[integer()]], X :: integer()) -> integer().\n\
        min_operations(Grid, X) ->\n    Flat = lists:flatten(Grid),\n    First = hd(Flat),\n\
        \    Rem = First rem X,\n    AllSameRem = lists:all(fun(Val) -> (Val rem X)\
        \ =:= Rem end, Flat),\n    case AllSameRem of\n        false -> -1;\n      \
        \  true ->\n            Sorted = lists:sort(Flat),\n            Len = length(Sorted),\n\
        \            Median = lists:nth((Len div 2) + 1, Sorted),\n            lists:foldl(fun(Val,\
        \ Acc) -> Acc + abs(Val - Median) div X end, 0, Sorted)\n    end."
      elixir: "defmodule Solution do\n  @spec min_operations(grid :: [[integer]], x\
        \ :: integer) :: integer\n  def min_operations(grid, x) do\n    flat = List.flatten(grid)\n\
        \    first_rem = rem(hd(flat), x)\n\n    if Enum.all?(flat, fn val -> rem(val,\
        \ x) == first_rem end) do\n      sorted = Enum.sort(flat)\n      len = length(sorted)\n\
        \      median = Enum.at(sorted, div(len, 2))\n      Enum.reduce(sorted, 0, fn\
        \ val, acc -> acc + div(abs(val - median), x) end)\n    else\n      -1\n   \
        \ end\n  end\nend"
    approach: 'To transform a grid into a uni-value grid where all elements are equal,
      the first requirement is that every element must have the same remainder when
      divided by x. This is because adding or subtracting x from any number grid[i][j]
      does not change the result of grid[i][j] % x. If any two elements have different
      remainders, it is impossible to make them equal using the given operation, and
      the function should return -1. Therefore, the algorithm begins by calculating
      the remainder of the first element and checking it against all other elements
      in the grid.


      Once the consistency of remainders is verified, the goal is to find a target value
      k that minimizes the total number of operations, where each operation costs x.
      The total operations count is given by the sum of abs(grid[i][j] - k) / x. Mathematically,
      the value k that minimizes the sum of absolute differences for a set of numbers
      is the median of those numbers. The algorithm flattens the 2D grid into a 1D array,
      sorts it to identify the median value, and then calculates the cumulative sum
      of steps needed to move every element to this median.'
    time_complexity: O(MN log(MN)) where M is the number of rows and N is the number
      of columns. This complexity is primarily determined by sorting the MN elements
      of the grid to find the median. Traversing the grid to verify the remainder condition
      takes O(MN) time, and the final calculation of operations also takes O(MN) time.
    space_complexity: O(MN) because all elements from the grid are stored in a one-dimensional
      array (or vector) to facilitate sorting and median selection.
    elapsed_time: 211.37851357460022
    model: gemini-3-flash-preview
    generated_at: '2026-04-28 02:14:20 '
---

## Problem #2033: Minimum Operations to Make a Uni-Value Grid

**Difficulty:** Medium

**Topics:** Array, Math, Sorting, Matrix

## Problem Description

<p>You are given a 2D integer <code>grid</code> of size <code>m x n</code> and an integer <code>x</code>. In one operation, you can <strong>add</strong> <code>x</code> to or <strong>subtract</strong> <code>x</code> from any element in the <code>grid</code>.</p>

<p>A <strong>uni-value grid</strong> is a grid where all the elements of it are equal.</p>

<p>Return <em>the <strong>minimum</strong> number of operations to make the grid <strong>uni-value</strong></em>. If it is not possible, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/gridtxt.png" style="width: 164px; height: 165px;" />
<pre>
<strong>Input:</strong> grid = [[2,4],[6,8]], x = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/gridtxt-1.png" style="width: 164px; height: 165px;" />
<pre>
<strong>Input:</strong> grid = [[1,5],[2,3]], x = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> We can make every element equal to 3.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/gridtxt-2.png" style="width: 164px; height: 165px;" />
<pre>
<strong>Input:</strong> grid = [[1,2],[3,4]], x = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is impossible to make every element equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= x, grid[i][j] &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. Is it possible to make two integers a and b equal if they have different remainders dividing by x?

2. If it is possible, which number should you select to minimize the number of operations?

3. What if the elements are sorted?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To transform a grid into a uni-value grid where all elements are equal, the first requirement is that every element must have the same remainder when divided by x. This is because adding or subtracting x from any number grid[i][j] does not change the result of grid[i][j] % x. If any two elements have different remainders, it is impossible to make them equal using the given operation, and the function should return -1. Therefore, the algorithm begins by calculating the remainder of the first element and checking it against all other elements in the grid.

Once the consistency of remainders is verified, the goal is to find a target value k that minimizes the total number of operations, where each operation costs x. The total operations count is given by the sum of abs(grid[i][j] - k) / x. Mathematically, the value k that minimizes the sum of absolute differences for a set of numbers is the median of those numbers. The algorithm flattens the 2D grid into a 1D array, sorts it to identify the median value, and then calculates the cumulative sum of steps needed to move every element to this median.

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
#include <cmath>

using namespace std;

class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> nums;
        nums.reserve(m * n);

        int rem = grid[0][0] % x;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] % x != rem) {
                    return -1;
                }
                nums.push_back(grid[i][j]);
            }
        }

        sort(nums.begin(), nums.end());
        int median = nums[nums.size() / 2];
        int operations = 0;

        for (int val : nums) {
            operations += abs(val - median) / x;
        }

        return operations;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public int minOperations(int[][] grid, int x) {
        int m = grid.length;
        int n = grid[0].length;
        int[] arr = new int[m * n];
        int k = 0;

        int rem = grid[0][0] % x;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] % x != rem) {
                    return -1;
                }
                arr[k++] = grid[i][j];
            }
        }

        Arrays.sort(arr);
        int median = arr[arr.length / 2];
        int operations = 0;

        for (int val : arr) {
            operations += Math.abs(val - median) / x;
        }

        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        nums = []
        for row in grid:
            for val in row:
                nums.append(val)

        rem = nums[0] % x
        for val in nums:
            if val % x != rem:
                return -1

        nums.sort()
        median = nums[len(nums) // 2]

        total_operations = 0
        for val in nums:
            total_operations += abs(val - median) // x

        return total_operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            nums.extend(row)

        rem = nums[0] % x
        for val in nums:
            if val % x != rem:
                return -1

        nums.sort()
        median = nums[len(nums) // 2]

        return sum(abs(val - median) // x for val in nums)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdio.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int minOperations(int** grid, int gridSize, int* gridColSize, int x) {
    int m = gridSize;
    int n = gridColSize[0];
    int totalElements = 0;
    for (int i = 0; i < m; i++) {
        totalElements += gridColSize[i];
    }

    int* arr = (int*)malloc(totalElements * sizeof(int));
    int k = 0;
    int rem = grid[0][0] % x;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j] % x != rem) {
                free(arr);
                return -1;
            }
            arr[k++] = grid[i][j];
        }
    }

    qsort(arr, totalElements, sizeof(int), compare);

    int median = arr[totalElements / 2];
    int operations = 0;
    for (int i = 0; i < totalElements; i++) {
        operations += abs(arr[i] - median) / x;
    }

    free(arr);
    return operations;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MinOperations(int[][] grid, int x) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] nums = new int[m * n];
        int k = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                nums[k++] = grid[i][j];
            }
        }

        int remainder = nums[0] % x;
        foreach (int num in nums) {
            if (num % x != remainder) {
                return -1;
            }
        }

        Array.Sort(nums);
        int median = nums[nums.Length / 2];
        int totalOperations = 0;

        foreach (int num in nums) {
            totalOperations += Math.Abs(num - median) / x;
        }

        return totalOperations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} grid
 * @param {number} x
 * @return {number}
 */
var minOperations = function(grid, x) {
    let nums = [];
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            nums.push(grid[i][j]);
        }
    }

    const remainder = nums[0] % x;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % x !== remainder) {
            return -1;
        }
    }

    nums.sort((a, b) => a - b);
    const median = nums[Math.floor(nums.length / 2)];
    let totalOperations = 0;

    for (const num of nums) {
        totalOperations += Math.abs(num - median) / x;
    }

    return totalOperations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(grid: number[][], x: number): number {
    let nums: number[] = [];
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            nums.push(grid[i][j]);
        }
    }

    const remainder = nums[0] % x;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % x !== remainder) {
            return -1;
        }
    }

    nums.sort((a, b) => a - b);
    const median = nums[Math.floor(nums.length / 2)];
    let totalOperations = 0;

    for (const num of nums) {
        totalOperations += Math.abs(num - median) / x;
    }

    return totalOperations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $x
     * @return Integer
     */
    function minOperations($grid, $x) {
        $nums = [];
        foreach ($grid as $row) {
            foreach ($row as $val) {
                $nums[] = $val;
            }
        }

        $remainder = $nums[0] % $x;
        foreach ($nums as $num) {
            if ($num % $x !== $remainder) {
                return -1;
            }
        }

        sort($nums);
        $n = count($nums);
        $median = $nums[(int)($n / 2)];
        $totalOperations = 0;

        foreach ($nums as $num) {
            $totalOperations += intdiv(abs($num - $median), $x);
        }

        return $totalOperations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ grid: [[Int]], _ x: Int) -> Int {
        var nums = [Int]()
        for row in grid {
            for val in row {
                nums.append(val)
            }
        }

        let remainder = nums[0] % x
        for num in nums {
            if num % x != remainder {
                return -1
            }
        }

        nums.sort()
        let median = nums[nums.count / 2]
        var totalOperations = 0

        for num in nums {
            totalOperations += abs(num - median) / x
        }

        return totalOperations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minOperations(grid: Array<IntArray>, x: Int): Int {
        val m = grid.size
        val n = grid[0].size
        val nums = IntArray(m * n)
        val rem = grid[0][0] % x
        var k = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (grid[i][j] % x != rem) return -1
                nums[k++] = grid[i][j]
            }
        }
        nums.sort()
        val median = nums[nums.size / 2]
        var ops = 0
        for (num in nums) {
            ops += Math.abs(num - median) / x
        }
        return ops
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minOperations(List<List<int>> grid, int x) {
    int m = grid.length;
    int n = grid[0].length;
    List<int> nums = List.filled(m * n, 0);
    int k = 0;
    int rem = grid[0][0] % x;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] % x != rem) return -1;
        nums[k++] = grid[i][j];
      }
    }
    nums.sort();
    int median = nums[nums.length ~/ 2];
    int ops = 0;
    for (int num in nums) {
      ops += (num - median).abs() ~/ x;
    }
    return ops;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func minOperations(grid [][]int, x int) int {
	m := len(grid)
	n := len(grid[0])
	nums := make([]int, m*n)
	k := 0
	rem := grid[0][0] % x
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j]%x != rem {
				return -1
			}
			nums[k] = grid[i][j]
			k++
		}
	}
	sort.Ints(nums)
	median := nums[len(nums)/2]
	ops := 0
	for _, v := range nums {
		diff := v - median
		if diff < 0 {
			diff = -diff
		}
		ops += diff / x
	}
	return ops
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} grid
# @param {Integer} x
# @return {Integer}
def min_operations(grid, x)
  nums = grid.flatten
  rem = nums[0] % x
  nums.each do |num|
    return -1 if num % x != rem
  end
  nums.sort!
  median = nums[nums.length / 2]
  ops = 0
  nums.each do |num|
    ops += (num - median).abs / x
  end
  ops
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minOperations(grid: Array[Array[Int]], x: Int): Int = {
        val m = grid.length
        val n = grid(0).length
        val nums = grid.flatten
        val rem = nums(0) % x
        if (nums.exists(_ % x != rem)) return -1
        val sortedNums = nums.sorted
        val median = sortedNums(sortedNums.length / 2)
        var ops = 0
        for (num <- sortedNums) {
            ops += Math.abs(num - median) / x
        }
        ops
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32) -> i32 {
        let mut flat: Vec<i32> = grid.into_iter().flatten().collect();
        let first_rem = flat[0] % x;
        for &val in &flat {
            if val % x != first_rem {
                return -1;
            }
        }
        flat.sort_unstable();
        let median = flat[flat.len() / 2];
        let mut operations = 0;
        for &val in &flat {
            operations += (val - median).abs() / x;
        }
        operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-operations grid x)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([flat (flatten grid)]
         [first-rem (modulo (car flat) x)])
    (if (not (andmap (lambda (v) (= (modulo v x) first-rem)) flat))
        -1
        (let* ([sorted (sort flat <)]
               [len (length sorted)]
               [median (list-ref sorted (quotient len 2))])
          (foldl (lambda (v acc) (+ acc (quotient (abs (- v median)) x))) 0 sorted)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_operations(Grid :: [[integer()]], X :: integer()) -> integer().
min_operations(Grid, X) ->
    Flat = lists:flatten(Grid),
    First = hd(Flat),
    Rem = First rem X,
    AllSameRem = lists:all(fun(Val) -> (Val rem X) =:= Rem end, Flat),
    case AllSameRem of
        false -> -1;
        true ->
            Sorted = lists:sort(Flat),
            Len = length(Sorted),
            Median = lists:nth((Len div 2) + 1, Sorted),
            lists:foldl(fun(Val, Acc) -> Acc + abs(Val - Median) div X end, 0, Sorted)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_operations(grid :: [[integer]], x :: integer) :: integer
  def min_operations(grid, x) do
    flat = List.flatten(grid)
    first_rem = rem(hd(flat), x)

    if Enum.all?(flat, fn val -> rem(val, x) == first_rem end) do
      sorted = Enum.sort(flat)
      len = length(sorted)
      median = Enum.at(sorted, div(len, 2))
      Enum.reduce(sorted, 0, fn val, acc -> acc + div(abs(val - median), x) end)
    else
      -1
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(MN log(MN)) where M is the number of rows and N is the number of columns. This complexity is primarily determined by sorting the MN elements of the grid to find the median. Traversing the grid to verify the remainder condition takes O(MN) time, and the final calculation of operations also takes O(MN) time.
- **Space Complexity:** O(MN) because all elements from the grid are stored in a one-dimensional array (or vector) to facilitate sorting and median selection.
