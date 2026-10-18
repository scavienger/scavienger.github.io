---
layout: post
title: "Number of Ways to Reorder Array to Get Same BST"
date: 2026-10-18 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Divide and Conquer", "Dynamic Programming", "Tree", "Union-Find", "Binary Search Tree", "Memoization", "Combinatorics", "Binary Tree", "Fermat's Little Theorem"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
ai_solutions:
  - solutions:
      cpp: "class Solution {\n    vector<vector<long long>> comb;\n    const int MOD\
        \ = 1000000007;\n\n    long long solve(const vector<int>& nums) {\n        if\
        \ (nums.size() < 3) return 1;\n        int root = nums[0];\n        vector<int>\
        \ left, right;\n        left.reserve(nums.size());\n        right.reserve(nums.size());\n\
        \        for (size_t i = 1; i < nums.size(); ++i) {\n            if (nums[i]\
        \ < root) left.push_back(nums[i]);\n            else right.push_back(nums[i]);\n\
        \        }\n        long long left_ways = solve(left);\n        long long right_ways\
        \ = solve(right);\n        long long ways = (left_ways * right_ways) % MOD;\n\
        \        return (ways * comb[left.size() + right.size()][left.size()]) % MOD;\n\
        \    }\n\npublic:\n    int numOfWays(vector<int>& nums) {\n        int n = nums.size();\n\
        \        comb.assign(n + 1, vector<long long>(n + 1, 0));\n        for (int\
        \ i = 0; i <= n; ++i) {\n            comb[i][0] = 1;\n            for (int j\
        \ = 1; j <= i; ++j) {\n                comb[i][j] = (comb[i - 1][j - 1] + comb[i\
        \ - 1][j]) % MOD;\n            }\n        }\n        return (int)((solve(nums)\
        \ - 1 + MOD) % MOD);\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    private long[][] comb;\n \
        \   private static final int MOD = 1000000007;\n\n    public int numOfWays(int[]\
        \ nums) {\n        int n = nums.length;\n        comb = new long[n + 1][n +\
        \ 1];\n        for (int i = 0; i <= n; i++) {\n            comb[i][0] = 1;\n\
        \            for (int j = 1; j <= i; j++) {\n                comb[i][j] = (comb[i\
        \ - 1][j - 1] + comb[i - 1][j]) % MOD;\n            }\n        }\n        List<Integer>\
        \ list = new ArrayList<>();\n        for (int x : nums) list.add(x);\n     \
        \   return (int) ((solve(list) - 1 + MOD) % MOD);\n    }\n\n    private long\
        \ solve(List<Integer> nums) {\n        if (nums.size() < 3) return 1;\n    \
        \    int root = nums.get(0);\n        List<Integer> left = new ArrayList<>();\n\
        \        List<Integer> right = new ArrayList<>();\n        for (int i = 1; i\
        \ < nums.size(); i++) {\n            int val = nums.get(i);\n            if\
        \ (val < root) left.add(val);\n            else right.add(val);\n        }\n\
        \        long lWays = solve(left);\n        long rWays = solve(right);\n   \
        \     long combined = (lWays * rWays) % MOD;\n        return (combined * comb[left.size()\
        \ + right.size()][left.size()]) % MOD;\n    }\n}"
      python: "import sys\n\nclass Solution(object):\n    def numOfWays(self, nums):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n      \
        \  \"\"\"\n        sys.setrecursionlimit(2000)\n        MOD = 10**9 + 7\n  \
        \      n = len(nums)\n\n        comb = [[0] * (n + 1) for _ in range(n + 1)]\n\
        \        for i in range(n + 1):\n            comb[i][0] = 1\n            for\
        \ j in range(1, i + 1):\n                comb[i][j] = (comb[i - 1][j - 1] +\
        \ comb[i - 1][j]) % MOD\n\n        def solve(arr):\n            if len(arr)\
        \ < 3:\n                return 1\n            root = arr[0]\n            left\
        \ = [x for x in arr[1:] if x < root]\n            right = [x for x in arr[1:]\
        \ if x > root]\n\n            L, R = len(left), len(right)\n            ways_left\
        \ = solve(left)\n            ways_right = solve(right)\n\n            return\
        \ (((ways_left * ways_right) % MOD) * comb[L + R][L]) % MOD\n\n        return\
        \ (solve(nums) - 1 + MOD) % MOD"
      python3: "import math\nimport sys\n\nclass Solution:\n    def numOfWays(self,\
        \ nums: list[int]) -> int:\n        MOD = 10**9 + 7\n        sys.setrecursionlimit(2000)\n\
        \n        def solve(arr):\n            if len(arr) <= 2:\n                return\
        \ 1\n\n            root = arr[0]\n            left = [x for x in arr if x <\
        \ root]\n            right = [x for x in arr if x > root]\n\n            L =\
        \ len(left)\n            R = len(right)\n\n            # Number of ways to interleave\
        \ left and right subtree sequences \n            # is given by binomial coefficient\
        \ C(L+R, L).\n            # f(nums) = f(left) * f(right) * C(L+R, L)\n     \
        \       res = (math.comb(L + R, L) * solve(left)) % MOD\n            res = (res\
        \ * solve(right)) % MOD\n            return res\n\n        # The answer is the\
        \ total number of ways minus the original ordering.\n        return (solve(nums)\
        \ - 1 + MOD) % MOD"
      c: "#include <stdlib.h>\n\nlong long solve_recursive(int* nums, int numsSize,\
        \ long long** table, int MOD) {\n    if (numsSize <= 2) return 1;\n\n    int*\
        \ left = (int*)malloc(numsSize * sizeof(int));\n    int* right = (int*)malloc(numsSize\
        \ * sizeof(int));\n    int leftSize = 0, rightSize = 0;\n\n    int root = nums[0];\n\
        \    for (int i = 1; i < numsSize; i++) {\n        if (nums[i] < root) {\n \
        \           left[leftSize++] = nums[i];\n        } else {\n            right[rightSize++]\
        \ = nums[i];\n        }\n    }\n\n    long long combinations = table[leftSize\
        \ + rightSize][leftSize];\n    long long leftWays = solve_recursive(left, leftSize,\
        \ table, MOD);\n    long long rightWays = solve_recursive(right, rightSize,\
        \ table, MOD);\n\n    long long res = (combinations * leftWays) % MOD;\n   \
        \ res = (res * rightWays) % MOD;\n\n    free(left);\n    free(right);\n    return\
        \ res;\n}\n\nint numOfWays(int* nums, int numsSize) {\n    int MOD = 1000000007;\n\
        \    long long** table = (long long**)malloc((numsSize + 1) * sizeof(long long*));\n\
        \    for (int i = 0; i <= numsSize; i++) {\n        table[i] = (long long*)malloc((i\
        \ + 1) * sizeof(long long));\n        table[i][0] = 1;\n        table[i][i]\
        \ = 1;\n        for (int j = 1; j < i; j++) {\n            table[i][j] = (table[i\
        \ - 1][j - 1] + table[i - 1][j]) % MOD;\n        }\n    }\n\n    long long totalWays\
        \ = solve_recursive(nums, numsSize, table, MOD);\n    long long result = (totalWays\
        \ - 1 + MOD) % MOD;\n\n    for (int i = 0; i <= numsSize; i++) {\n        free(table[i]);\n\
        \    }\n    free(table);\n\n    return (int)result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    private long[][] table;\n    private const int\
        \ MOD = 1000000007;\n\n    public int NumOfWays(int[] nums) {\n        int n\
        \ = nums.Length;\n        table = new long[n + 1][];\n        for (int i = 0;\
        \ i <= n; i++) {\n            table[i] = new long[i + 1];\n            table[i][0]\
        \ = 1;\n            table[i][i] = 1;\n            for (int j = 1; j < i; j++)\
        \ {\n                table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) %\
        \ MOD;\n            }\n        }\n\n        long totalWays = Calculate(nums.ToList());\n\
        \        return (int)((totalWays - 1 + MOD) % MOD);\n    }\n\n    private long\
        \ Calculate(List<int> nums) {\n        if (nums.Count <= 2) return 1;\n\n  \
        \      int root = nums[0];\n        List<int> left = new List<int>();\n    \
        \    List<int> right = new List<int>();\n\n        for (int i = 1; i < nums.Count;\
        \ i++) {\n            if (nums[i] < root) {\n                left.Add(nums[i]);\n\
        \            }\n            else {\n                right.Add(nums[i]);\n  \
        \          }\n        }\n\n        long combinations = table[left.Count + right.Count][left.Count];\n\
        \        long leftWays = Calculate(left);\n        long rightWays = Calculate(right);\n\
        \n        long res = (combinations * leftWays) % MOD;\n        res = (res *\
        \ rightWays) % MOD;\n\n        return res;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar numOfWays\
        \ = function(nums) {\n    const MOD = 1000000007n;\n    const n = nums.length;\n\
        \    const table = Array.from({ length: n + 1 }, () => new BigUint64Array(n\
        \ + 1));\n\n    for (let i = 0; i <= n; i++) {\n        table[i][0] = 1n;\n\
        \        table[i][i] = 1n;\n        for (let j = 1; j < i; j++) {\n        \
        \    table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % MOD;\n        }\n\
        \    }\n\n    function calculate(arr) {\n        if (arr.length <= 2) return\
        \ 1n;\n\n        const root = arr[0];\n        const left = [];\n        const\
        \ right = [];\n\n        for (let i = 1; i < arr.length; i++) {\n          \
        \  if (arr[i] < root) {\n                left.push(arr[i]);\n            } else\
        \ {\n                right.push(arr[i]);\n            }\n        }\n\n     \
        \   const combinations = table[left.length + right.length][left.length];\n \
        \       const leftWays = calculate(left);\n        const rightWays = calculate(right);\n\
        \n        let res = (combinations * leftWays) % MOD;\n        res = (res * rightWays)\
        \ % MOD;\n\n        return res;\n    }\n\n    const totalWays = calculate(nums);\n\
        \    return Number((totalWays - 1n + MOD) % MOD);\n};"
      typescript: "function numOfWays(nums: number[]): number {\n  const MOD = 1000000007n;\n\
        \  const n = nums.length;\n  const table: BigInt64Array[] = new Array(n + 1);\n\
        \n  for (let i = 0; i <= n; i++) {\n    table[i] = new BigInt64Array(n + 1);\n\
        \    table[i][0] = 1n;\n    table[i][i] = 1n;\n    for (let j = 1; j < i; j++)\
        \ {\n      table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % MOD;\n  \
        \  }\n  }\n\n  const solve = (arr: number[]): bigint => {\n    if (arr.length\
        \ <= 2) return 1n;\n    const left: number[] = [];\n    const right: number[]\
        \ = [];\n    const root = arr[0];\n    for (let i = 1; i < arr.length; i++)\
        \ {\n      if (arr[i] < root) {\n        left.push(arr[i]);\n      } else {\n\
        \        right.push(arr[i]);\n      }\n    }\n    const leftWays = solve(left);\n\
        \    const rightWays = solve(right);\n    const combinations = table[left.length\
        \ + right.length][left.length];\n    return (((combinations * leftWays) % MOD)\
        \ * rightWays) % MOD;\n  };\n\n  return Number((solve(nums) - 1n + MOD) % MOD);\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function numOfWays($nums) {\n        $mod = 1000000007;\n\
        \        $n = count($nums);\n        $table = [];\n\n        for ($i = 0; $i\
        \ <= $n; $i++) {\n            $table[$i] = array_fill(0, $i + 1, 1);\n     \
        \       for ($j = 1; $j < $i; $j++) {\n                $table[$i][$j] = ($table[$i\
        \ - 1][$j - 1] + $table[$i - 1][$j]) % $mod;\n            }\n        }\n\n \
        \       $solve = function($arr) use (&$solve, &$table, $mod) {\n           \
        \ $count = count($arr);\n            if ($count <= 2) {\n                return\
        \ 1;\n            }\n            $left = [];\n            $right = [];\n   \
        \         $root = $arr[0];\n            for ($i = 1; $i < $count; $i++) {\n\
        \                if ($arr[$i] < $root) {\n                    $left[] = $arr[$i];\n\
        \                } else {\n                    $right[] = $arr[$i];\n      \
        \          }\n            }\n\n            $leftWays = $solve($left);\n    \
        \        $rightWays = $solve($right);\n            $leftCount = count($left);\n\
        \            $rightCount = count($right);\n            $combinations = $table[$leftCount\
        \ + $rightCount][$leftCount];\n            $ways = ($combinations * $leftWays)\
        \ % $mod;\n            return ($ways * $rightWays) % $mod;\n        };\n\n \
        \       $totalWays = $solve($nums);\n        return ($totalWays - 1 + $mod)\
        \ % $mod;\n    }\n}"
      swift: "class Solution {\n    func numOfWays(_ nums: [Int]) -> Int {\n       \
        \ let mod = 1_000_000_007\n        let n = nums.count\n        var table = Array(repeating:\
        \ Array(repeating: 1, count: n + 1), count: n + 1)\n\n        if n >= 2 {\n\
        \            for i in 2...n {\n                for j in 1..<i {\n          \
        \          table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod\n   \
        \             }\n            }\n        }\n\n        func solve(_ arr: [Int])\
        \ -> Int {\n            if arr.count <= 2 {\n                return 1\n    \
        \        }\n            var left = [Int]()\n            var right = [Int]()\n\
        \            let root = arr[0]\n            for i in 1..<arr.count {\n     \
        \           if arr[i] < root {\n                    left.append(arr[i])\n  \
        \              } else {\n                    right.append(arr[i])\n        \
        \        }\n            }\n            let leftWays = solve(left)\n        \
        \    let rightWays = solve(right)\n            let combinations = table[left.count\
        \ + right.count][left.count]\n            let ways = (combinations * leftWays)\
        \ % mod\n            return (ways * rightWays) % mod\n        }\n\n        let\
        \ totalWays = solve(nums)\n        return (totalWays - 1 + mod) % mod\n    }\n\
        }"
      kotlin: "class Solution {\n    fun numOfWays(nums: IntArray): Int {\n        val\
        \ mod = 1_000_000_007L\n        val n = nums.size\n        val table = Array(n\
        \ + 1) { LongArray(n + 1) }\n\n        for (i in 0..n) {\n            table[i][0]\
        \ = 1L\n            table[i][i] = 1L\n            for (j in 1 until i) {\n \
        \               table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod\n\
        \            }\n        }\n\n        fun solve(list: List<Int>): Long {\n  \
        \          if (list.size <= 2) {\n                return 1L\n            }\n\
        \            val left = mutableListOf<Int>()\n            val right = mutableListOf<Int>()\n\
        \            val root = list[0]\n            for (i in 1 until list.size) {\n\
        \                if (list[i] < root) {\n                    left.add(list[i])\n\
        \                } else {\n                    right.add(list[i])\n        \
        \        }\n            }\n            val leftWays = solve(left)\n        \
        \    val rightWays = solve(right)\n            val combinations = table[left.size\
        \ + right.size][left.size]\n            val ways = (combinations * leftWays\
        \ % mod) * rightWays % mod\n            return ways\n        }\n\n        val\
        \ totalWays = solve(nums.toList())\n        return ((totalWays - 1 + mod) %\
        \ mod).toInt()\n    }\n}"
      dart: "class Solution {\n  int numOfWays(List<int> nums) {\n    const int mod\
        \ = 1000000007;\n    int n = nums.length;\n    List<List<int>> table = List.generate(n\
        \ + 1, (i) => List.filled(n + 1, 0));\n    for (int i = 0; i <= n; i++) {\n\
        \      table[i][0] = 1;\n      for (int j = 1; j <= i; j++) {\n        table[i][j]\
        \ = (table[i - 1][j - 1] + table[i - 1][j]) % mod;\n      }\n    }\n\n    int\
        \ dfs(List<int> sub) {\n      if (sub.length <= 2) return 1;\n      int root\
        \ = sub[0];\n      List<int> left = [];\n      List<int> right = [];\n     \
        \ for (int i = 1; i < sub.length; i++) {\n        if (sub[i] < root) {\n   \
        \       left.add(sub[i]);\n        } else {\n          right.add(sub[i]);\n\
        \        }\n      }\n      int ways = table[left.length + right.length][left.length];\n\
        \      int leftWays = dfs(left);\n      int rightWays = dfs(right);\n      int\
        \ res = (ways * leftWays) % mod;\n      res = (res * rightWays) % mod;\n   \
        \   return res;\n    }\n\n    return (dfs(nums) - 1 + mod) % mod;\n  }\n}"
      go: "func numOfWays(nums []int) int {\n    const mod int64 = 1000000007\n    n\
        \ := len(nums)\n    table := make([][]int64, n+1)\n    for i := 0; i <= n; i++\
        \ {\n        table[i] = make([]int64, n+1)\n        table[i][0] = 1\n      \
        \  for j := 1; j <= i; j++ {\n            table[i][j] = (table[i-1][j-1] + table[i-1][j])\
        \ % mod\n        }\n    }\n\n    var dfs func([]int) int64\n    dfs = func(sub\
        \ []int) int64 {\n        if len(sub) <= 2 {\n            return 1\n       \
        \ }\n        root := sub[0]\n        left := make([]int, 0, len(sub))\n    \
        \    right := make([]int, 0, len(sub))\n        for i := 1; i < len(sub); i++\
        \ {\n            if sub[i] < root {\n                left = append(left, sub[i])\n\
        \            } else {\n                right = append(right, sub[i])\n     \
        \       }\n        }\n        ways := table[len(left)+len(right)][len(left)]\n\
        \        res := (ways * dfs(left)) % mod\n        res = (res * dfs(right)) %\
        \ mod\n        return res\n    }\n\n    return int((dfs(nums) - 1 + mod) % mod)\n\
        }"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef num_of_ways(nums)\n\
        \  mod = 1_000_000_007\n  n = nums.length\n  table = Array.new(n + 1) { Array.new(n\
        \ + 1, 0) }\n  (0..n).each do |i|\n    table[i][0] = 1\n    (1..i).each do |j|\n\
        \      table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod\n    end\n\
        \  end\n\n  dfs = lambda do |ns|\n    return 1 if ns.length <= 2\n    root =\
        \ ns[0]\n    left = []\n    right = []\n    (1...ns.length).each do |i|\n  \
        \    if ns[i] < root\n        left << ns[i]\n      else\n        right << ns[i]\n\
        \      end\n    end\n    ways = table[left.length + right.length][left.length]\n\
        \    res = (ways * dfs.call(left)) % mod\n    res = (res * dfs.call(right))\
        \ % mod\n    res\n  end\n\n  (dfs.call(nums) - 1 + mod) % mod\nend"
      scala: "object Solution {\n  def numOfWays(nums: Array[Int]): Int = {\n    val\
        \ mod = 1000000007L\n    val n = nums.length\n    val table = Array.ofDim[Long](n\
        \ + 1, n + 1)\n    for (i <- 0 to n) {\n      table(i)(0) = 1L\n      for (j\
        \ <- 1 to i) {\n        table(i)(j) = (table(i - 1)(j - 1) + table(i - 1)(j))\
        \ % mod\n      }\n    }\n\n    def dfs(ns: List[Int]): Long = {\n      if (ns.length\
        \ <= 2) return 1L\n      val root = ns.head\n      val (left, right) = ns.tail.partition(_\
        \ < root)\n      val ways = table(left.length + right.length)(left.length)\n\
        \      val res = (ways * dfs(left)) % mod\n      (res * dfs(right)) % mod\n\
        \    }\n\n    ((dfs(nums.toList) - 1 + mod) % mod).toInt\n  }\n}"
      rust: "impl Solution {\n    pub fn num_of_ways(nums: Vec<i32>) -> i32 {\n    \
        \    let n = nums.len();\n        let m = 1_000_000_007u64;\n        let mut\
        \ comb = vec![vec![0u64; n + 1]; n + 1];\n        for i in 0..=n {\n       \
        \     comb[i][0] = 1;\n            comb[i][i] = 1;\n            for j in 1..i\
        \ {\n                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % m;\n\
        \            }\n        }\n\n        fn solve(nums: &[i32], comb: &Vec<Vec<u64>>,\
        \ m: u64) -> u64 {\n            if nums.len() <= 2 {\n                return\
        \ 1;\n            }\n            let root = nums[0];\n            let mut left\
        \ = Vec::with_capacity(nums.len());\n            let mut right = Vec::with_capacity(nums.len());\n\
        \            for &x in &nums[1..] {\n                if x < root {\n       \
        \             left.push(x);\n                } else {\n                    right.push(x);\n\
        \                }\n            }\n            let left_res = solve(&left, comb,\
        \ m);\n            let right_res = solve(&right, comb, m);\n            let\
        \ n_l = left.len();\n            let n_r = right.len();\n            let ways\
        \ = comb[n_l + n_r][n_l];\n            (((left_res * right_res) % m) * ways)\
        \ % m\n        }\n\n        ((solve(&nums, &comb, m) + m - 1) % m) as i32\n\
        \    }\n}"
      racket: "(define/contract (num-of-ways nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([n (length nums)]\n         [MOD 1000000007]\n         [comb (make-vector\
        \ (+ n 1))])\n    (for ([i (in-range (+ n 1))])\n      (vector-set! comb i (make-vector\
        \ (+ i 1) 1))\n      (for ([j (in-range 1 i)])\n        (let ([v1 (vector-ref\
        \ (vector-ref comb (- i 1)) (- j 1))]\n              [v2 (vector-ref (vector-ref\
        \ comb (- i 1)) j)])\n          (vector-set! (vector-ref comb i) j (modulo (+\
        \ v1 v2) MOD)))))\n    (define (solve items)\n      (if (or (null? items) (null?\
        \ (cdr items)))\n          1\n          (let* ([root (car items)]\n        \
        \         [rest (cdr items)]\n                 [left (filter (lambda (x) (<\
        \ x root)) rest)]\n                 [right (filter (lambda (x) (> x root)) rest)]\n\
        \                 [n-l (length left)]\n                 [n-r (length right)]\n\
        \                 [c (vector-ref (vector-ref comb (+ n-l n-r)) n-l)])\n    \
        \        (modulo (* (modulo (* (solve left) (solve right)) MOD) c) MOD))))\n\
        \    (modulo (- (solve nums) 1) MOD)))"
      erlang: "-spec num_of_ways(Nums :: [integer()]) -> integer().\nnum_of_ways(Nums)\
        \ ->\n  MOD = 1000000007,\n  N = length(Nums),\n  Table = ets:new(comb_table,\
        \ [set, private]),\n  lists:foreach(fun(I) ->\n    ets:insert(Table, {{I, 0},\
        \ 1}),\n    ets:insert(Table, {{I, I}, 1}),\n    if I > 1 ->\n      lists:foreach(fun(J)\
        \ ->\n        V1 = ets:lookup_element(Table, {I-1, J-1}, 2),\n        V2 = ets:lookup_element(Table,\
        \ {I-1, J}, 2),\n        ets:insert(Table, {{I, J}, (V1 + V2) rem MOD})\n  \
        \    end, lists:seq(1, I-1));\n      true -> ok\n    end\n  end, lists:seq(0,\
        \ N)),\n  Result = solve(Nums, Table, MOD),\n  ets:delete(Table),\n  (Result\
        \ + MOD - 1) rem MOD.\n\nsolve([], _, _) -> 1;\nsolve([_], _, _) -> 1;\nsolve([Root\
        \ | Rest], Table, MOD) ->\n  {Left, Right} = lists:partition(fun(X) -> X < Root\
        \ end, Rest),\n  LRes = solve(Left, Table, MOD),\n  RRes = solve(Right, Table,\
        \ MOD),\n  LSize = length(Left),\n  RSize = length(Right),\n  Comb = ets:lookup_element(Table,\
        \ {LSize + RSize, LSize}, 2),\n  (((LRes * RRes) rem MOD) * Comb) rem MOD."
      elixir: "defmodule Solution do\n  @spec num_of_ways(nums :: [integer]) :: integer\n\
        \  def num_of_ways(nums) do\n    mod = 1_000_000_007\n    n = length(nums)\n\
        \    table = :ets.new(:comb_table, [:set, :private])\n\n    Enum.each(0..n,\
        \ fn i ->\n      :ets.insert(table, {{i, 0}, 1})\n      :ets.insert(table, {{i,\
        \ i}, 1})\n      if i > 1 do\n        Enum.each(1..(i - 1), fn j ->\n      \
        \    v1 = :ets.lookup_element(table, {i - 1, j - 1}, 2)\n          v2 = :ets.lookup_element(table,\
        \ {i - 1, j}, 2)\n          :ets.insert(table, {{i, j}, rem(v1 + v2, mod)})\n\
        \        end)\n      end\n    end)\n\n    res = solve(nums, table, mod)\n  \
        \  :ets.delete(table)\n    rem(res + mod - 1, mod)\n  end\n\n  defp solve([],\
        \ _table, _mod), do: 1\n  defp solve([_root], _table, _mod), do: 1\n  defp solve([root\
        \ | rest], table, mod) do\n    {left, right} = Enum.split_with(rest, fn x ->\
        \ x < root end)\n    l_res = solve(left, table, mod)\n    r_res = solve(right,\
        \ table, mod)\n    l_size = length(left)\n    r_size = length(right)\n    comb\
        \ = :ets.lookup_element(table, {l_size + r_size, l_size}, 2)\n    inner = rem(l_res\
        \ * r_res, mod)\n    rem(inner * comb, mod)\n  end\nend"
    approach: 'The core idea is to use a divide and conquer strategy based on the property
      that the first element of any sequence always becomes the root of its corresponding
      Binary Search Tree (BST). For any given sequence, elements smaller than the root
      populate the left subtree and elements larger populate the right subtree. To ensure
      the BST structure remains identical, the relative ordering of elements within
      the left sub-collection and the relative ordering of elements within the right
      sub-collection must be preserved, though their elements can be interleaved in
      any way. The number of such valid interleavings for two sub-collections of sizes
      $L$ and $R$ is calculated using the binomial coefficient $\binom{L+R}{L}$.


      The algorithm recursively calculates the number of ways to form the left and right
      subtrees and multiplies these by the interleaving factor. We precompute a Pascal''s
      Triangle table to store binomial coefficients modulo $10^9 + 7$, ensuring $O(1)$
      lookup for the interleaving combinations. The final result is the total number
      of ways minus one, as the problem asks for the number of reorderings distinct
      from the original sequence.'
    time_complexity: O(N^2) where N is the length of the input array. Precomputing the
      Pascal's Triangle table takes $O(N^2)$ time. The recursive partitioning of the
      array also takes $O(N^2)$ in the worst case (for a skewed BST), as every element
      is processed at each level of its recursion depth. In the case of a balanced BST,
      this step would take $O(N \log N)$.
    space_complexity: O(N^2) because we store a 2D Pascal's Triangle table of size $N
      \times N$. Additionally, the recursive calls store sub-arrays and utilize stack
      space, which in the worst-case (a completely skewed tree) leads to $O(N)$ depth,
      with the total auxiliary space for sub-arrays summing up to $O(N^2)$.
    elapsed_time: 434.7611765861511
    model: gemini-3-flash-preview
    generated_at: '2026-10-18 02:31:27 '
---

## Problem #1569: Number of Ways to Reorder Array to Get Same BST

**Difficulty:** Hard

**Topics:** Array, Math, Divide and Conquer, Dynamic Programming, Tree, Union-Find, Binary Search Tree, Memoization, Combinatorics, Binary Tree, Fermat's Little Theorem

## Problem Description

<p>Given an array <code>nums</code> that represents a permutation of integers from <code>1</code> to <code>n</code>. We are going to construct a binary search tree (BST) by inserting the elements of <code>nums</code> in order into an initially empty BST. Find the number of different ways to reorder <code>nums</code> so that the constructed BST is identical to that formed from the original array <code>nums</code>.</p>

<ul>
	<li>For example, given <code>nums = [2,1,3]</code>, we will have 2 as the root, 1 as a left child, and 3 as a right child. The array <code>[2,3,1]</code> also yields the same BST but <code>[3,2,1]</code> yields a different BST.</li>
</ul>

<p>Return <em>the number of ways to reorder</em> <code>nums</code> <em>such that the BST formed is identical to the original BST formed from</em> <code>nums</code>.</p>

<p>Since the answer may be very large, <strong>return it modulo </strong><code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2026/02/23/1569_ex0.png" style="width: 160px; height: 160px;" />
<pre>
<strong>Input:</strong> nums = [2,1,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2026/02/23/1569_ex.png" style="width: 270px; height: 270px;" />
<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2026/02/23/1569_ex2.png" style="width: 205px; height: 205px;" />
<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no other orderings of nums that will yield the same BST.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
	<li>All integers in <code>nums</code> are <strong>distinct</strong>.</li>
</ul>


## Hints

1. Use a divide and conquer strategy.

2. The first number will always be the root. Consider the numbers smaller and larger than the root separately. When merging the results together, how many ways can you order x elements in x+y positions?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core idea is to use a divide and conquer strategy based on the property that the first element of any sequence always becomes the root of its corresponding Binary Search Tree (BST). For any given sequence, elements smaller than the root populate the left subtree and elements larger populate the right subtree. To ensure the BST structure remains identical, the relative ordering of elements within the left sub-collection and the relative ordering of elements within the right sub-collection must be preserved, though their elements can be interleaved in any way. The number of such valid interleavings for two sub-collections of sizes $L$ and $R$ is calculated using the binomial coefficient $\binom{L+R}{L}$.

The algorithm recursively calculates the number of ways to form the left and right subtrees and multiplies these by the interleaving factor. We precompute a Pascal's Triangle table to store binomial coefficients modulo $10^9 + 7$, ensuring $O(1)$ lookup for the interleaving combinations. The final result is the total number of ways minus one, as the problem asks for the number of reorderings distinct from the original sequence.

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
class Solution {
    vector<vector<long long>> comb;
    const int MOD = 1000000007;

    long long solve(const vector<int>& nums) {
        if (nums.size() < 3) return 1;
        int root = nums[0];
        vector<int> left, right;
        left.reserve(nums.size());
        right.reserve(nums.size());
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] < root) left.push_back(nums[i]);
            else right.push_back(nums[i]);
        }
        long long left_ways = solve(left);
        long long right_ways = solve(right);
        long long ways = (left_ways * right_ways) % MOD;
        return (ways * comb[left.size() + right.size()][left.size()]) % MOD;
    }

public:
    int numOfWays(vector<int>& nums) {
        int n = nums.size();
        comb.assign(n + 1, vector<long long>(n + 1, 0));
        for (int i = 0; i <= n; ++i) {
            comb[i][0] = 1;
            for (int j = 1; j <= i; ++j) {
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
            }
        }
        return (int)((solve(nums) - 1 + MOD) % MOD);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    private long[][] comb;
    private static final int MOD = 1000000007;

    public int numOfWays(int[] nums) {
        int n = nums.length;
        comb = new long[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            comb[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
            }
        }
        List<Integer> list = new ArrayList<>();
        for (int x : nums) list.add(x);
        return (int) ((solve(list) - 1 + MOD) % MOD);
    }

    private long solve(List<Integer> nums) {
        if (nums.size() < 3) return 1;
        int root = nums.get(0);
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for (int i = 1; i < nums.size(); i++) {
            int val = nums.get(i);
            if (val < root) left.add(val);
            else right.add(val);
        }
        long lWays = solve(left);
        long rWays = solve(right);
        long combined = (lWays * rWays) % MOD;
        return (combined * comb[left.size() + right.size()][left.size()]) % MOD;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import sys

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sys.setrecursionlimit(2000)
        MOD = 10**9 + 7
        n = len(nums)

        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def solve(arr):
            if len(arr) < 3:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            L, R = len(left), len(right)
            ways_left = solve(left)
            ways_right = solve(right)

            return (((ways_left * ways_right) % MOD) * comb[L + R][L]) % MOD

        return (solve(nums) - 1 + MOD) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math
import sys

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        sys.setrecursionlimit(2000)

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            L = len(left)
            R = len(right)

            # Number of ways to interleave left and right subtree sequences 
            # is given by binomial coefficient C(L+R, L).
            # f(nums) = f(left) * f(right) * C(L+R, L)
            res = (math.comb(L + R, L) * solve(left)) % MOD
            res = (res * solve(right)) % MOD
            return res

        # The answer is the total number of ways minus the original ordering.
        return (solve(nums) - 1 + MOD) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

long long solve_recursive(int* nums, int numsSize, long long** table, int MOD) {
    if (numsSize <= 2) return 1;

    int* left = (int*)malloc(numsSize * sizeof(int));
    int* right = (int*)malloc(numsSize * sizeof(int));
    int leftSize = 0, rightSize = 0;

    int root = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < root) {
            left[leftSize++] = nums[i];
        } else {
            right[rightSize++] = nums[i];
        }
    }

    long long combinations = table[leftSize + rightSize][leftSize];
    long long leftWays = solve_recursive(left, leftSize, table, MOD);
    long long rightWays = solve_recursive(right, rightSize, table, MOD);

    long long res = (combinations * leftWays) % MOD;
    res = (res * rightWays) % MOD;

    free(left);
    free(right);
    return res;
}

int numOfWays(int* nums, int numsSize) {
    int MOD = 1000000007;
    long long** table = (long long**)malloc((numsSize + 1) * sizeof(long long*));
    for (int i = 0; i <= numsSize; i++) {
        table[i] = (long long*)malloc((i + 1) * sizeof(long long));
        table[i][0] = 1;
        table[i][i] = 1;
        for (int j = 1; j < i; j++) {
            table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % MOD;
        }
    }

    long long totalWays = solve_recursive(nums, numsSize, table, MOD);
    long long result = (totalWays - 1 + MOD) % MOD;

    for (int i = 0; i <= numsSize; i++) {
        free(table[i]);
    }
    free(table);

    return (int)result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    private long[][] table;
    private const int MOD = 1000000007;

    public int NumOfWays(int[] nums) {
        int n = nums.Length;
        table = new long[n + 1][];
        for (int i = 0; i <= n; i++) {
            table[i] = new long[i + 1];
            table[i][0] = 1;
            table[i][i] = 1;
            for (int j = 1; j < i; j++) {
                table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % MOD;
            }
        }

        long totalWays = Calculate(nums.ToList());
        return (int)((totalWays - 1 + MOD) % MOD);
    }

    private long Calculate(List<int> nums) {
        if (nums.Count <= 2) return 1;

        int root = nums[0];
        List<int> left = new List<int>();
        List<int> right = new List<int>();

        for (int i = 1; i < nums.Count; i++) {
            if (nums[i] < root) {
                left.Add(nums[i]);
            }
            else {
                right.Add(nums[i]);
            }
        }

        long combinations = table[left.Count + right.Count][left.Count];
        long leftWays = Calculate(left);
        long rightWays = Calculate(right);

        long res = (combinations * leftWays) % MOD;
        res = (res * rightWays) % MOD;

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
 * @return {number}
 */
var numOfWays = function(nums) {
    const MOD = 1000000007n;
    const n = nums.length;
    const table = Array.from({ length: n + 1 }, () => new BigUint64Array(n + 1));

    for (let i = 0; i <= n; i++) {
        table[i][0] = 1n;
        table[i][i] = 1n;
        for (let j = 1; j < i; j++) {
            table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % MOD;
        }
    }

    function calculate(arr) {
        if (arr.length <= 2) return 1n;

        const root = arr[0];
        const left = [];
        const right = [];

        for (let i = 1; i < arr.length; i++) {
            if (arr[i] < root) {
                left.push(arr[i]);
            } else {
                right.push(arr[i]);
            }
        }

        const combinations = table[left.length + right.length][left.length];
        const leftWays = calculate(left);
        const rightWays = calculate(right);

        let res = (combinations * leftWays) % MOD;
        res = (res * rightWays) % MOD;

        return res;
    }

    const totalWays = calculate(nums);
    return Number((totalWays - 1n + MOD) % MOD);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numOfWays(nums: number[]): number {
  const MOD = 1000000007n;
  const n = nums.length;
  const table: BigInt64Array[] = new Array(n + 1);

  for (let i = 0; i <= n; i++) {
    table[i] = new BigInt64Array(n + 1);
    table[i][0] = 1n;
    table[i][i] = 1n;
    for (let j = 1; j < i; j++) {
      table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % MOD;
    }
  }

  const solve = (arr: number[]): bigint => {
    if (arr.length <= 2) return 1n;
    const left: number[] = [];
    const right: number[] = [];
    const root = arr[0];
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] < root) {
        left.push(arr[i]);
      } else {
        right.push(arr[i]);
      }
    }
    const leftWays = solve(left);
    const rightWays = solve(right);
    const combinations = table[left.length + right.length][left.length];
    return (((combinations * leftWays) % MOD) * rightWays) % MOD;
  };

  return Number((solve(nums) - 1n + MOD) % MOD);
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
     * @return Integer
     */
    function numOfWays($nums) {
        $mod = 1000000007;
        $n = count($nums);
        $table = [];

        for ($i = 0; $i <= $n; $i++) {
            $table[$i] = array_fill(0, $i + 1, 1);
            for ($j = 1; $j < $i; $j++) {
                $table[$i][$j] = ($table[$i - 1][$j - 1] + $table[$i - 1][$j]) % $mod;
            }
        }

        $solve = function($arr) use (&$solve, &$table, $mod) {
            $count = count($arr);
            if ($count <= 2) {
                return 1;
            }
            $left = [];
            $right = [];
            $root = $arr[0];
            for ($i = 1; $i < $count; $i++) {
                if ($arr[$i] < $root) {
                    $left[] = $arr[$i];
                } else {
                    $right[] = $arr[$i];
                }
            }

            $leftWays = $solve($left);
            $rightWays = $solve($right);
            $leftCount = count($left);
            $rightCount = count($right);
            $combinations = $table[$leftCount + $rightCount][$leftCount];
            $ways = ($combinations * $leftWays) % $mod;
            return ($ways * $rightWays) % $mod;
        };

        $totalWays = $solve($nums);
        return ($totalWays - 1 + $mod) % $mod;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numOfWays(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = nums.count
        var table = Array(repeating: Array(repeating: 1, count: n + 1), count: n + 1)

        if n >= 2 {
            for i in 2...n {
                for j in 1..<i {
                    table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod
                }
            }
        }

        func solve(_ arr: [Int]) -> Int {
            if arr.count <= 2 {
                return 1
            }
            var left = [Int]()
            var right = [Int]()
            let root = arr[0]
            for i in 1..<arr.count {
                if arr[i] < root {
                    left.append(arr[i])
                } else {
                    right.append(arr[i])
                }
            }
            let leftWays = solve(left)
            let rightWays = solve(right)
            let combinations = table[left.count + right.count][left.count]
            let ways = (combinations * leftWays) % mod
            return (ways * rightWays) % mod
        }

        let totalWays = solve(nums)
        return (totalWays - 1 + mod) % mod
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numOfWays(nums: IntArray): Int {
        val mod = 1_000_000_007L
        val n = nums.size
        val table = Array(n + 1) { LongArray(n + 1) }

        for (i in 0..n) {
            table[i][0] = 1L
            table[i][i] = 1L
            for (j in 1 until i) {
                table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod
            }
        }

        fun solve(list: List<Int>): Long {
            if (list.size <= 2) {
                return 1L
            }
            val left = mutableListOf<Int>()
            val right = mutableListOf<Int>()
            val root = list[0]
            for (i in 1 until list.size) {
                if (list[i] < root) {
                    left.add(list[i])
                } else {
                    right.add(list[i])
                }
            }
            val leftWays = solve(left)
            val rightWays = solve(right)
            val combinations = table[left.size + right.size][left.size]
            val ways = (combinations * leftWays % mod) * rightWays % mod
            return ways
        }

        val totalWays = solve(nums.toList())
        return ((totalWays - 1 + mod) % mod).toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numOfWays(List<int> nums) {
    const int mod = 1000000007;
    int n = nums.length;
    List<List<int>> table = List.generate(n + 1, (i) => List.filled(n + 1, 0));
    for (int i = 0; i <= n; i++) {
      table[i][0] = 1;
      for (int j = 1; j <= i; j++) {
        table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod;
      }
    }

    int dfs(List<int> sub) {
      if (sub.length <= 2) return 1;
      int root = sub[0];
      List<int> left = [];
      List<int> right = [];
      for (int i = 1; i < sub.length; i++) {
        if (sub[i] < root) {
          left.add(sub[i]);
        } else {
          right.add(sub[i]);
        }
      }
      int ways = table[left.length + right.length][left.length];
      int leftWays = dfs(left);
      int rightWays = dfs(right);
      int res = (ways * leftWays) % mod;
      res = (res * rightWays) % mod;
      return res;
    }

    return (dfs(nums) - 1 + mod) % mod;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numOfWays(nums []int) int {
    const mod int64 = 1000000007
    n := len(nums)
    table := make([][]int64, n+1)
    for i := 0; i <= n; i++ {
        table[i] = make([]int64, n+1)
        table[i][0] = 1
        for j := 1; j <= i; j++ {
            table[i][j] = (table[i-1][j-1] + table[i-1][j]) % mod
        }
    }

    var dfs func([]int) int64
    dfs = func(sub []int) int64 {
        if len(sub) <= 2 {
            return 1
        }
        root := sub[0]
        left := make([]int, 0, len(sub))
        right := make([]int, 0, len(sub))
        for i := 1; i < len(sub); i++ {
            if sub[i] < root {
                left = append(left, sub[i])
            } else {
                right = append(right, sub[i])
            }
        }
        ways := table[len(left)+len(right)][len(left)]
        res := (ways * dfs(left)) % mod
        res = (res * dfs(right)) % mod
        return res
    }

    return int((dfs(nums) - 1 + mod) % mod)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def num_of_ways(nums)
  mod = 1_000_000_007
  n = nums.length
  table = Array.new(n + 1) { Array.new(n + 1, 0) }
  (0..n).each do |i|
    table[i][0] = 1
    (1..i).each do |j|
      table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod
    end
  end

  dfs = lambda do |ns|
    return 1 if ns.length <= 2
    root = ns[0]
    left = []
    right = []
    (1...ns.length).each do |i|
      if ns[i] < root
        left << ns[i]
      else
        right << ns[i]
      end
    end
    ways = table[left.length + right.length][left.length]
    res = (ways * dfs.call(left)) % mod
    res = (res * dfs.call(right)) % mod
    res
  end

  (dfs.call(nums) - 1 + mod) % mod
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def numOfWays(nums: Array[Int]): Int = {
    val mod = 1000000007L
    val n = nums.length
    val table = Array.ofDim[Long](n + 1, n + 1)
    for (i <- 0 to n) {
      table(i)(0) = 1L
      for (j <- 1 to i) {
        table(i)(j) = (table(i - 1)(j - 1) + table(i - 1)(j)) % mod
      }
    }

    def dfs(ns: List[Int]): Long = {
      if (ns.length <= 2) return 1L
      val root = ns.head
      val (left, right) = ns.tail.partition(_ < root)
      val ways = table(left.length + right.length)(left.length)
      val res = (ways * dfs(left)) % mod
      (res * dfs(right)) % mod
    }

    ((dfs(nums.toList) - 1 + mod) % mod).toInt
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn num_of_ways(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let m = 1_000_000_007u64;
        let mut comb = vec![vec![0u64; n + 1]; n + 1];
        for i in 0..=n {
            comb[i][0] = 1;
            comb[i][i] = 1;
            for j in 1..i {
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % m;
            }
        }

        fn solve(nums: &[i32], comb: &Vec<Vec<u64>>, m: u64) -> u64 {
            if nums.len() <= 2 {
                return 1;
            }
            let root = nums[0];
            let mut left = Vec::with_capacity(nums.len());
            let mut right = Vec::with_capacity(nums.len());
            for &x in &nums[1..] {
                if x < root {
                    left.push(x);
                } else {
                    right.push(x);
                }
            }
            let left_res = solve(&left, comb, m);
            let right_res = solve(&right, comb, m);
            let n_l = left.len();
            let n_r = right.len();
            let ways = comb[n_l + n_r][n_l];
            (((left_res * right_res) % m) * ways) % m
        }

        ((solve(&nums, &comb, m) + m - 1) % m) as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (num-of-ways nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [MOD 1000000007]
         [comb (make-vector (+ n 1))])
    (for ([i (in-range (+ n 1))])
      (vector-set! comb i (make-vector (+ i 1) 1))
      (for ([j (in-range 1 i)])
        (let ([v1 (vector-ref (vector-ref comb (- i 1)) (- j 1))]
              [v2 (vector-ref (vector-ref comb (- i 1)) j)])
          (vector-set! (vector-ref comb i) j (modulo (+ v1 v2) MOD)))))
    (define (solve items)
      (if (or (null? items) (null? (cdr items)))
          1
          (let* ([root (car items)]
                 [rest (cdr items)]
                 [left (filter (lambda (x) (< x root)) rest)]
                 [right (filter (lambda (x) (> x root)) rest)]
                 [n-l (length left)]
                 [n-r (length right)]
                 [c (vector-ref (vector-ref comb (+ n-l n-r)) n-l)])
            (modulo (* (modulo (* (solve left) (solve right)) MOD) c) MOD))))
    (modulo (- (solve nums) 1) MOD)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec num_of_ways(Nums :: [integer()]) -> integer().
num_of_ways(Nums) ->
  MOD = 1000000007,
  N = length(Nums),
  Table = ets:new(comb_table, [set, private]),
  lists:foreach(fun(I) ->
    ets:insert(Table, {{I, 0}, 1}),
    ets:insert(Table, {{I, I}, 1}),
    if I > 1 ->
      lists:foreach(fun(J) ->
        V1 = ets:lookup_element(Table, {I-1, J-1}, 2),
        V2 = ets:lookup_element(Table, {I-1, J}, 2),
        ets:insert(Table, {{I, J}, (V1 + V2) rem MOD})
      end, lists:seq(1, I-1));
      true -> ok
    end
  end, lists:seq(0, N)),
  Result = solve(Nums, Table, MOD),
  ets:delete(Table),
  (Result + MOD - 1) rem MOD.

solve([], _, _) -> 1;
solve([_], _, _) -> 1;
solve([Root | Rest], Table, MOD) ->
  {Left, Right} = lists:partition(fun(X) -> X < Root end, Rest),
  LRes = solve(Left, Table, MOD),
  RRes = solve(Right, Table, MOD),
  LSize = length(Left),
  RSize = length(Right),
  Comb = ets:lookup_element(Table, {LSize + RSize, LSize}, 2),
  (((LRes * RRes) rem MOD) * Comb) rem MOD.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_of_ways(nums :: [integer]) :: integer
  def num_of_ways(nums) do
    mod = 1_000_000_007
    n = length(nums)
    table = :ets.new(:comb_table, [:set, :private])

    Enum.each(0..n, fn i ->
      :ets.insert(table, {{i, 0}, 1})
      :ets.insert(table, {{i, i}, 1})
      if i > 1 do
        Enum.each(1..(i - 1), fn j ->
          v1 = :ets.lookup_element(table, {i - 1, j - 1}, 2)
          v2 = :ets.lookup_element(table, {i - 1, j}, 2)
          :ets.insert(table, {{i, j}, rem(v1 + v2, mod)})
        end)
      end
    end)

    res = solve(nums, table, mod)
    :ets.delete(table)
    rem(res + mod - 1, mod)
  end

  defp solve([], _table, _mod), do: 1
  defp solve([_root], _table, _mod), do: 1
  defp solve([root | rest], table, mod) do
    {left, right} = Enum.split_with(rest, fn x -> x < root end)
    l_res = solve(left, table, mod)
    r_res = solve(right, table, mod)
    l_size = length(left)
    r_size = length(right)
    comb = :ets.lookup_element(table, {l_size + r_size, l_size}, 2)
    inner = rem(l_res * r_res, mod)
    rem(inner * comb, mod)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^2) where N is the length of the input array. Precomputing the Pascal's Triangle table takes $O(N^2)$ time. The recursive partitioning of the array also takes $O(N^2)$ in the worst case (for a skewed BST), as every element is processed at each level of its recursion depth. In the case of a balanced BST, this step would take $O(N \log N)$.
- **Space Complexity:** O(N^2) because we store a 2D Pascal's Triangle table of size $N \times N$. Additionally, the recursive calls store sub-arrays and utilize stack space, which in the worst-case (a completely skewed tree) leads to $O(N)$ depth, with the total auxiliary space for sub-arrays summing up to $O(N^2)$.
