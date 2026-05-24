---
layout: post
title: "Jump Game V"
date: 2026-05-24 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/jump-game-v/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxJumps(vector<int>& arr, int d) {\n\
        \        int n = arr.size();\n        vector<int> dp(n, 1);\n        vector<int>\
        \ indices(n);\n        for (int i = 0; i < n; ++i) {\n            indices[i]\
        \ = i;\n        }\n        sort(indices.begin(), indices.end(), [&](int a, int\
        \ b) {\n            return arr[a] < arr[b];\n        });\n\n        for (int\
        \ i : indices) {\n            for (int j = i + 1; j <= i + d && j < n; ++j)\
        \ {\n                if (arr[j] >= arr[i]) break;\n                dp[i] = max(dp[i],\
        \ 1 + dp[j]);\n            }\n            for (int j = i - 1; j >= i - d &&\
        \ j >= 0; --j) {\n                if (arr[j] >= arr[i]) break;\n           \
        \     dp[i] = max(dp[i], 1 + dp[j]);\n            }\n        }\n\n        int\
        \ result = 0;\n        for (int val : dp) {\n            result = max(result,\
        \ val);\n        }\n        return result;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int maxJumps(int[]\
        \ arr, int d) {\n        int n = arr.length;\n        int[] dp = new int[n];\n\
        \        Arrays.fill(dp, 1);\n\n        Integer[] indices = new Integer[n];\n\
        \        for (int i = 0; i < n; i++) {\n            indices[i] = i;\n      \
        \  }\n\n        Arrays.sort(indices, (a, b) -> Integer.compare(arr[a], arr[b]));\n\
        \n        for (int i : indices) {\n            for (int j = i + 1; j <= i +\
        \ d && j < n; j++) {\n                if (arr[j] >= arr[i]) break;\n       \
        \         dp[i] = Math.max(dp[i], 1 + dp[j]);\n            }\n            for\
        \ (int j = i - 1; j >= i - d && j >= 0; j--) {\n                if (arr[j] >=\
        \ arr[i]) break;\n                dp[i] = Math.max(dp[i], 1 + dp[j]);\n    \
        \        }\n        }\n\n        int maxVisited = 0;\n        for (int val :\
        \ dp) {\n            maxVisited = Math.max(maxVisited, val);\n        }\n  \
        \      return maxVisited;\n    }\n}"
      python: "class Solution(object):\n    def maxJumps(self, arr, d):\n        \"\"\
        \"\n        :type arr: List[int]\n        :type d: int\n        :rtype: int\n\
        \        \"\"\"\n        n = len(arr)\n        dp = [1] * n\n\n        # Sort\
        \ indices by their value in the array to process dependencies bottom-up\n  \
        \      indices = sorted(range(n), key=lambda i: arr[i])\n\n        for i in\
        \ indices:\n            # Try jumping to the right\n            for j in range(i\
        \ + 1, min(i + d + 1, n)):\n                if arr[j] >= arr[i]:\n         \
        \           break\n                dp[i] = max(dp[i], 1 + dp[j])\n\n       \
        \     # Try jumping to the left\n            for j in range(i - 1, max(-1, i\
        \ - d - 1), -1):\n                if arr[j] >= arr[i]:\n                   \
        \ break\n                dp[i] = max(dp[i], 1 + dp[j])\n\n        return max(dp)\
        \ if dp else 0"
      python3: "from functools import lru_cache\nimport sys\nfrom typing import List\n\
        \nclass Solution:\n    def maxJumps(self, arr: List[int], d: int) -> int:\n\
        \        sys.setrecursionlimit(2000)\n        n = len(arr)\n\n        @lru_cache(None)\n\
        \        def solve(i):\n            res = 1\n            for j in range(i +\
        \ 1, min(i + d + 1, n)):\n                if arr[j] >= arr[i]:\n           \
        \         break\n                current = 1 + solve(j)\n                if\
        \ current > res:\n                    res = current\n            for j in range(i\
        \ - 1, max(-1, i - d - 1), -1):\n                if arr[j] >= arr[i]:\n    \
        \                break\n                current = 1 + solve(j)\n           \
        \     if current > res:\n                    res = current\n            return\
        \ res\n\n        return max(solve(i) for i in range(n))"
      c: "#include <stdlib.h>\n\nint solve(int i, int* arr, int n, int d, int* dp) {\n\
        \    if (dp[i] != 0) return dp[i];\n    int res = 1;\n    for (int j = i + 1;\
        \ j <= i + d && j < n; j++) {\n        if (arr[j] >= arr[i]) break;\n      \
        \  int current = 1 + solve(j, arr, n, d, dp);\n        if (current > res) res\
        \ = current;\n    }\n    for (int j = i - 1; j >= i - d && j >= 0; j--) {\n\
        \        if (arr[j] >= arr[i]) break;\n        int current = 1 + solve(j, arr,\
        \ n, d, dp);\n        if (current > res) res = current;\n    }\n    return dp[i]\
        \ = res;\n}\n\nint maxJumps(int* arr, int arrSize, int d) {\n    int* dp = (int*)calloc(arrSize,\
        \ sizeof(int));\n    int max_res = 0;\n    for (int i = 0; i < arrSize; i++)\
        \ {\n        int current = solve(i, arr, arrSize, d, dp);\n        if (current\
        \ > max_res) max_res = current;\n    }\n    free(dp);\n    return max_res;\n\
        }"
      csharp: "using System;\n\npublic class Solution {\n    public int MaxJumps(int[]\
        \ arr, int d) {\n        int n = arr.Length;\n        int[] memo = new int[n];\n\
        \        int maxResult = 0;\n        for (int i = 0; i < n; i++) {\n       \
        \     int current = Solve(i, arr, d, n, memo);\n            if (current > maxResult)\
        \ {\n                maxResult = current;\n            }\n        }\n      \
        \  return maxResult;\n    }\n\n    private int Solve(int i, int[] arr, int d,\
        \ int n, int[] memo) {\n        if (memo[i] != 0) return memo[i];\n        int\
        \ res = 1;\n        for (int j = i + 1; j <= i + d && j < n; j++) {\n      \
        \      if (arr[j] >= arr[i]) break;\n            int val = 1 + Solve(j, arr,\
        \ d, n, memo);\n            if (val > res) res = val;\n        }\n        for\
        \ (int j = i - 1; j >= i - d && j >= 0; j--) {\n            if (arr[j] >= arr[i])\
        \ break;\n            int val = 1 + Solve(j, arr, d, n, memo);\n           \
        \ if (val > res) res = val;\n        }\n        memo[i] = res;\n        return\
        \ res;\n    }\n}"
      javascript: "/**\n * @param {number[]} arr\n * @param {number} d\n * @return {number}\n\
        \ */\nvar maxJumps = function(arr, d) {\n    const n = arr.length;\n    const\
        \ memo = new Int32Array(n);\n\n    function solve(i) {\n        if (memo[i]\
        \ !== 0) return memo[i];\n        let res = 1;\n        for (let j = i + 1;\
        \ j <= i + d && j < n; j++) {\n            if (arr[j] >= arr[i]) break;\n  \
        \          let val = 1 + solve(j);\n            if (val > res) res = val;\n\
        \        }\n        for (let j = i - 1; j >= i - d && j >= 0; j--) {\n     \
        \       if (arr[j] >= arr[i]) break;\n            let val = 1 + solve(j);\n\
        \            if (val > res) res = val;\n        }\n        return memo[i] =\
        \ res;\n    }\n\n    let maxVal = 0;\n    for (let i = 0; i < n; i++) {\n  \
        \      let current = solve(i);\n        if (current > maxVal) maxVal = current;\n\
        \    }\n    return maxVal;\n};"
      typescript: "function maxJumps(arr: number[], d: number): number {\n    const\
        \ n = arr.length;\n    const memo = new Array(n).fill(0);\n\n    function solve(i:\
        \ number): number {\n        if (memo[i] !== 0) return memo[i];\n\n        let\
        \ res = 1;\n\n        for (let j = i + 1; j <= Math.min(i + d, n - 1) && arr[i]\
        \ > arr[j]; j++) {\n            res = Math.max(res, 1 + solve(j));\n       \
        \ }\n\n        for (let j = i - 1; j >= Math.max(0, i - d) && arr[i] > arr[j];\
        \ j--) {\n            res = Math.max(res, 1 + solve(j));\n        }\n\n    \
        \    return memo[i] = res;\n    }\n\n    let maxVisited = 0;\n    for (let i\
        \ = 0; i < n; i++) {\n        maxVisited = Math.max(maxVisited, solve(i));\n\
        \    }\n\n    return maxVisited;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $arr\n     * @param\
        \ Integer $d\n     * @return Integer\n     */\n    private $memo = [];\n   \
        \ private $arr_data;\n    private $jump_d;\n    private $arr_len;\n\n    function\
        \ maxJumps($arr, $d) {\n        $this->arr_data = $arr;\n        $this->jump_d\
        \ = $d;\n        $this->arr_len = count($arr);\n        $this->memo = array_fill(0,\
        \ $this->arr_len, 0);\n\n        $max_steps = 0;\n        for ($i = 0; $i <\
        \ $this->arr_len; $i++) {\n            $max_steps = max($max_steps, $this->solve($i));\n\
        \        }\n\n        return $max_steps;\n    }\n\n    private function solve($i)\
        \ {\n        if ($this->memo[$i] != 0) {\n            return $this->memo[$i];\n\
        \        }\n\n        $res = 1;\n\n        for ($j = $i + 1; $j <= min($i +\
        \ $this->jump_d, $this->arr_len - 1) && $this->arr_data[$i] > $this->arr_data[$j];\
        \ $j++) {\n            $res = max($res, 1 + $this->solve($j));\n        }\n\n\
        \        for ($j = $i - 1; $j >= max(0, $i - $this->jump_d) && $this->arr_data[$i]\
        \ > $this->arr_data[$j]; $j--) {\n            $res = max($res, 1 + $this->solve($j));\n\
        \        }\n\n        $this->memo[$i] = $res;\n        return $res;\n    }\n\
        }"
      swift: "class Solution {\n    private var memo: [Int] = []\n    private var arr:\
        \ [Int] = []\n    private var d: Int = 0\n    private var n: Int = 0\n\n   \
        \ func maxJumps(_ arr: [Int], _ d: Int) -> Int {\n        self.arr = arr\n \
        \       self.d = d\n        self.n = arr.count\n        self.memo = Array(repeating:\
        \ 0, count: n)\n\n        var maxVisited = 0\n        for i in 0..<n {\n   \
        \         maxVisited = max(maxVisited, solve(i))\n        }\n        return\
        \ maxVisited\n    }\n\n    private func solve(_ i: Int) -> Int {\n        if\
        \ memo[i] != 0 {\n            return memo[i]\n        }\n\n        var res =\
        \ 1\n\n        var j = i + 1\n        while j <= min(i + d, n - 1) && arr[i]\
        \ > arr[j] {\n            res = max(res, 1 + solve(j))\n            j += 1\n\
        \        }\n\n        j = i - 1\n        while j >= max(0, i - d) && arr[i]\
        \ > arr[j] {\n            res = max(res, 1 + solve(j))\n            j -= 1\n\
        \        }\n\n        memo[i] = res\n        return res\n    }\n}"
      kotlin: "class Solution {\n    private lateinit var memo: IntArray\n    private\
        \ lateinit var arr: IntArray\n    private var d: Int = 0\n    private var n:\
        \ Int = 0\n\n    fun maxJumps(arr: IntArray, d: Int): Int {\n        this.arr\
        \ = arr\n        this.d = d\n        this.n = arr.size\n        this.memo =\
        \ IntArray(n) { 0 }\n\n        var maxVisited = 0\n        for (i in 0 until\
        \ n) {\n            maxVisited = Math.max(maxVisited, solve(i))\n        }\n\
        \        return maxVisited\n    }\n\n    private fun solve(i: Int): Int {\n\
        \        if (memo[i] != 0) {\n            return memo[i]\n        }\n\n    \
        \    var res = 1\n\n        // Look right\n        var j = i + 1\n        while\
        \ (j <= Math.min(i + d, n - 1) && arr[i] > arr[j]) {\n            res = Math.max(res,\
        \ 1 + solve(j))\n            j++\n        }\n\n        // Look left\n      \
        \  j = i - 1\n        while (j >= Math.max(0, i - d) && arr[i] > arr[j]) {\n\
        \            res = Math.max(res, 1 + solve(j))\n            j--\n        }\n\
        \n        memo[i] = res\n        return res\n    }\n}"
      dart: "class Solution {\n  int maxJumps(List<int> arr, int d) {\n    int n = arr.length;\n\
        \    List<int> memo = List.filled(n, 0);\n\n    int solve(int i) {\n      if\
        \ (memo[i] != 0) return memo[i];\n\n      int res = 1;\n\n      for (int j =\
        \ i + 1; j < n && j <= i + d; j++) {\n        if (arr[i] > arr[j]) {\n     \
        \     int v = 1 + solve(j);\n          if (v > res) res = v;\n        } else\
        \ {\n          break;\n        }\n      }\n\n      for (int j = i - 1; j >=\
        \ 0 && j >= i - d; j--) {\n        if (arr[i] > arr[j]) {\n          int v =\
        \ 1 + solve(j);\n          if (v > res) res = v;\n        } else {\n       \
        \   break;\n        }\n      }\n\n      memo[i] = res;\n      return res;\n\
        \    }\n\n    int ans = 0;\n    for (int i = 0; i < n; i++) {\n      int current\
        \ = solve(i);\n      if (current > ans) ans = current;\n    }\n    return ans;\n\
        \  }\n}"
      go: "func maxJumps(arr []int, d int) int {\n    n := len(arr)\n    memo := make([]int,\
        \ n)\n\n    var solve func(int) int\n    solve = func(i int) int {\n       \
        \ if memo[i] != 0 {\n            return memo[i]\n        }\n\n        res :=\
        \ 1\n\n        for j := i + 1; j < n && j <= i+d; j++ {\n            if arr[i]\
        \ > arr[j] {\n                v := 1 + solve(j)\n                if v > res\
        \ {\n                    res = v\n                }\n            } else {\n\
        \                break\n            }\n        }\n\n        for j := i - 1;\
        \ j >= 0 && j >= i-d; j-- {\n            if arr[i] > arr[j] {\n            \
        \    v := 1 + solve(j)\n                if v > res {\n                    res\
        \ = v\n                }\n            } else {\n                break\n    \
        \        }\n        }\n\n        memo[i] = res\n        return res\n    }\n\n\
        \    ans := 0\n    for i := 0; i < n; i++ {\n        v := solve(i)\n       \
        \ if v > ans {\n            ans = v\n        }\n    }\n    return ans\n}"
      ruby: "def max_jumps(arr, d)\n  n = arr.length\n  memo = Array.new(n, 0)\n\n \
        \ solve = lambda do |i|\n    return memo[i] if memo[i] != 0\n\n    res = 1\n\
        \n    j = i + 1\n    while j < n && j <= i + d\n      if arr[i] > arr[j]\n \
        \       v = 1 + solve.call(j)\n        res = v if v > res\n      else\n    \
        \    break\n      end\n      j += 1\n    end\n\n    j = i - 1\n    while j >=\
        \ 0 && j >= i - d\n      if arr[i] > arr[j]\n        v = 1 + solve.call(j)\n\
        \        res = v if v > res\n      else\n        break\n      end\n      j -=\
        \ 1\n    end\n\n    memo[i] = res\n    res\n  end\n\n  max_ans = 0\n  (0...n).each\
        \ do |i|\n    v = solve.call(i)\n    max_ans = v if v > max_ans\n  end\n  max_ans\n\
        end"
      scala: "object Solution {\n    def maxJumps(arr: Array[Int], d: Int): Int = {\n\
        \        val n = arr.length\n        val memo = Array.fill(n)(0)\n\n       \
        \ def solve(i: Int): Int = {\n            if (memo(i) != 0) return memo(i)\n\
        \n            var res = 1\n\n            var j = i + 1\n            while (j\
        \ < n && j <= i + d && arr(i) > arr(j)) {\n                val v = 1 + solve(j)\n\
        \                if (v > res) res = v\n                j += 1\n            }\n\
        \n            j = i - 1\n            while (j >= 0 && j >= i - d && arr(i) >\
        \ arr(j)) {\n                val v = 1 + solve(j)\n                if (v > res)\
        \ res = v\n                j -= 1\n            }\n\n            memo(i) = res\n\
        \            res\n        }\n\n        var maxAns = 0\n        for (i <- 0 until\
        \ n) {\n            val v = solve(i)\n            if (v > maxAns) maxAns = v\n\
        \        }\n        maxAns\n    }\n}"
      rust: "impl Solution {\n    pub fn max_jumps(arr: Vec<i32>, d: i32) -> i32 {\n\
        \        let n = arr.len();\n        let d = d as usize;\n        let mut dp\
        \ = vec![1; n];\n        let mut indices: Vec<usize> = (0..n).collect();\n \
        \       indices.sort_by_key(|&i| arr[i]);\n\n        for &i in &indices {\n\
        \            let val_i = arr[i];\n            // Jump to the right\n       \
        \     for j in (i + 1)..std::cmp::min(i + d + 1, n) {\n                if arr[j]\
        \ < val_i {\n                    dp[i] = std::cmp::max(dp[i], 1 + dp[j]);\n\
        \                } else {\n                    break;\n                }\n \
        \           }\n            // Jump to the left\n            for j in (0..i).rev().take(d)\
        \ {\n                if arr[j] < val_i {\n                    dp[i] = std::cmp::max(dp[i],\
        \ 1 + dp[j]);\n                } else {\n                    break;\n      \
        \          }\n            }\n        }\n\n        *dp.iter().max().unwrap_or(&1)\n\
        \    }\n}"
      racket: "(define/contract (max-jumps arr d)\n  (-> (listof exact-integer?) exact-integer?\
        \ exact-integer?)\n  (let* ([n (length arr)]\n         [vec-arr (list->vector\
        \ arr)]\n         [dp (make-vector n 1)]\n         [indices (sort (range n)\
        \ < #:key (lambda (i) (vector-ref vec-arr i)))])\n    (for ([i indices])\n \
        \     (let ([val-i (vector-ref vec-arr i)])\n        (let loop-right ([j (+\
        \ i 1)])\n          (when (and (< j n) (<= (- j i) d) (< (vector-ref vec-arr\
        \ j) val-i))\n            (vector-set! dp i (max (vector-ref dp i) (+ 1 (vector-ref\
        \ dp j))))\n            (loop-right (+ j 1))))\n        (let loop-left ([j (-\
        \ i 1)])\n          (when (and (>= j 0) (<= (- i j) d) (< (vector-ref vec-arr\
        \ j) val-i))\n            (vector-set! dp i (max (vector-ref dp i) (+ 1 (vector-ref\
        \ dp j))))\n            (loop-left (- j 1))))))\n    (apply max (vector->list\
        \ dp))))"
      erlang: "-spec max_jumps(Arr :: [integer()], D :: integer()) -> integer().\nmax_jumps(Arr,\
        \ D) ->\n  N = length(Arr),\n  ArrTuple = list_to_tuple(Arr),\n  Indices = lists:sort(fun(I,\
        \ J) ->\n    element(I + 1, ArrTuple) =< element(J + 1, ArrTuple)\n  end, lists:seq(0,\
        \ N - 1)),\n  FinalDP = lists:foldl(fun(I, AccDP) ->\n    ValI = element(I +\
        \ 1, ArrTuple),\n    RMax = check_right(I + 1, erlang:min(I + D, N - 1), ValI,\
        \ ArrTuple, AccDP, 0),\n    LMax = check_left(I - 1, erlang:max(I - D, 0), ValI,\
        \ ArrTuple, AccDP, 0),\n    array:set(I, 1 + erlang:max(RMax, LMax), AccDP)\n\
        \  end, array:new(N, {default, 0}), Indices),\n  lists:max(array:to_list(FinalDP)).\n\
        \ncheck_right(J, MaxJ, ValI, ArrTuple, DP, CurrentMax) when J =< MaxJ ->\n \
        \ ValJ = element(J + 1, ArrTuple),\n  if ValJ < ValI ->\n    NewMax = erlang:max(CurrentMax,\
        \ array:get(J, DP)),\n    check_right(J + 1, MaxJ, ValI, ArrTuple, DP, NewMax);\n\
        \  true -> CurrentMax\n  end;\ncheck_right(_, _, _, _, _, CurrentMax) -> CurrentMax.\n\
        \ncheck_left(J, MinJ, ValI, ArrTuple, DP, CurrentMax) when J >= MinJ ->\n  ValJ\
        \ = element(J + 1, ArrTuple),\n  if ValJ < ValI ->\n    NewMax = erlang:max(CurrentMax,\
        \ array:get(J, DP)),\n    check_left(J - 1, MinJ, ValI, ArrTuple, DP, NewMax);\n\
        \  true -> CurrentMax\n  end;\ncheck_left(_, _, _, _, _, CurrentMax) -> CurrentMax."
      elixir: "defmodule Solution do\n  @spec max_jumps(arr :: [integer], d :: integer)\
        \ :: integer\n  def max_jumps(arr, d) do\n    n = length(arr)\n    arr_tuple\
        \ = List.to_tuple(arr)\n    indices = Enum.sort(0..(n - 1), fn i, j ->\n   \
        \   elem(arr_tuple, i) <= elem(arr_tuple, j)\n    end)\n\n    dp = Enum.reduce(indices,\
        \ %{}, fn i, acc_dp ->\n      val_i = elem(arr_tuple, i)\n      r_max = check_right(i\
        \ + 1, min(i + d, n - 1), val_i, arr_tuple, acc_dp, 0)\n      l_max = check_left(i\
        \ - 1, max(i - d, 0), val_i, arr_tuple, acc_dp, 0)\n      Map.put(acc_dp, i,\
        \ 1 + max(r_max, l_max))\n    end)\n\n    Enum.max(Map.values(dp))\n  end\n\n\
        \  defp check_right(j, max_j, val_i, arr_tuple, dp, current_max) when j <= max_j\
        \ do\n    val_j = elem(arr_tuple, j)\n    if val_j < val_i do\n      check_right(j\
        \ + 1, max_j, val_i, arr_tuple, dp, max(current_max, Map.get(dp, j, 0)))\n \
        \   else\n      current_max\n    end\n  end\n  defp check_right(_j, _max_j,\
        \ _val_i, _arr_tuple, _dp, current_max), do: current_max\n\n  defp check_left(j,\
        \ min_j, val_i, arr_tuple, dp, current_max) when j >= min_j do\n    val_j =\
        \ elem(arr_tuple, j)\n    if val_j < val_i do\n      check_left(j - 1, min_j,\
        \ val_i, arr_tuple, dp, max(current_max, Map.get(dp, j, 0)))\n    else\n   \
        \   current_max\n    end\n  end\n  defp check_left(_j, _min_j, _val_i, _arr_tuple,\
        \ _dp, current_max), do: current_max\nend"
    approach: 'The problem can be modeled as finding the longest path in a Directed
      Acyclic Graph (DAG), where each index in the array is a node and a directed edge
      exists from index i to index j if a jump from i to j is valid. Since jumps are
      only permitted from an index with a higher value to one with a lower value, the
      graph is naturally acyclic. This allows us to use dynamic programming to find
      the maximum number of visited indices. For any index i, the maximum path length
      starting at i is 1 + max(dp[j]) for all indices j reachable from i in a single
      step.


      To implement this efficiently, we process the indices in ascending order of their
      array values. By doing so, when we calculate the result for a taller index, the
      results for all possible destination indices (which must be shorter) have already
      been computed. For each index i, we explore neighbors in both directions up to
      distance d. If we encounter an index j where arr[j] is greater than or equal to
      arr[i], we stop exploring in that direction immediately, as any jump to an index
      beyond j would violate the condition that all intermediate elements must be strictly
      smaller than the starting value.'
    time_complexity: O(N * d) where N is the length of the array and d is the maximum
      jump distance. Sorting the indices takes O(N log N). After sorting, we iterate
      through each of the N indices once, and for each index, we scan at most d elements
      to the left and d elements to the right. This results in an overall complexity
      of O(N * d + N log N), which simplifies to O(N * d) because d is at least 1 and
      up to N.
    space_complexity: O(N) because we store the dynamic programming results in an array
      of size N and maintain an auxiliary array of indices for the sorting process,
      both of which require linear space.
    elapsed_time: 234.75223565101624
    model: gemini-3-flash-preview
    generated_at: '2026-05-24 02:39:02 '
---

## Problem #1340: Jump Game V

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Sorting

## Problem Description

<p>Given an array of&nbsp;integers <code>arr</code> and an integer <code>d</code>. In one step you can jump from index <code>i</code> to index:</p>

<ul>
	<li><code>i + x</code> where:&nbsp;<code>i + x &lt; arr.length</code> and <code> 0 &lt;&nbsp;x &lt;= d</code>.</li>
	<li><code>i - x</code> where:&nbsp;<code>i - x &gt;= 0</code> and <code> 0 &lt;&nbsp;x &lt;= d</code>.</li>
</ul>

<p>In addition, you can only jump from index <code>i</code> to index <code>j</code>&nbsp;if <code>arr[i] &gt; arr[j]</code> and <code>arr[i] &gt; arr[k]</code> for all indices <code>k</code> between <code>i</code> and <code>j</code> (More formally <code>min(i,&nbsp;j) &lt; k &lt; max(i, j)</code>).</p>

<p>You can choose any index of the array and start jumping. Return <em>the maximum number of indices</em>&nbsp;you can visit.</p>

<p>Notice that you can not jump outside of the array at any time.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/01/23/meta-chart.jpeg" style="width: 633px; height: 419px;" />
<pre>
<strong>Input:</strong> arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can start at index 10. You can jump 10 --&gt; 8 --&gt; 6 --&gt; 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 &gt; 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 &gt; 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,3,3,3,3], d = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> You can start at any index. You always cannot jump to any index.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [7,6,5,4,3,2,1], d = 1
<strong>Output:</strong> 7
<strong>Explanation:</strong> Start at index 0. You can visit all the indicies. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= d &lt;= arr.length</code></li>
</ul>


## Hints

1. Use dynamic programming. dp[i] is max jumps you can do starting from index i. Answer is max(dp[i]).

2. dp[i] = 1 + max (dp[j]) where j is all indices you can reach from i.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as finding the longest path in a Directed Acyclic Graph (DAG), where each index in the array is a node and a directed edge exists from index i to index j if a jump from i to j is valid. Since jumps are only permitted from an index with a higher value to one with a lower value, the graph is naturally acyclic. This allows us to use dynamic programming to find the maximum number of visited indices. For any index i, the maximum path length starting at i is 1 + max(dp[j]) for all indices j reachable from i in a single step.

To implement this efficiently, we process the indices in ascending order of their array values. By doing so, when we calculate the result for a taller index, the results for all possible destination indices (which must be shorter) have already been computed. For each index i, we explore neighbors in both directions up to distance d. If we encounter an index j where arr[j] is greater than or equal to arr[i], we stop exploring in that direction immediately, as any jump to an index beyond j would violate the condition that all intermediate elements must be strictly smaller than the starting value.

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
public:
    int maxJumps(vector<int>& arr, int d) {
        int n = arr.size();
        vector<int> dp(n, 1);
        vector<int> indices(n);
        for (int i = 0; i < n; ++i) {
            indices[i] = i;
        }
        sort(indices.begin(), indices.end(), [&](int a, int b) {
            return arr[a] < arr[b];
        });

        for (int i : indices) {
            for (int j = i + 1; j <= i + d && j < n; ++j) {
                if (arr[j] >= arr[i]) break;
                dp[i] = max(dp[i], 1 + dp[j]);
            }
            for (int j = i - 1; j >= i - d && j >= 0; --j) {
                if (arr[j] >= arr[i]) break;
                dp[i] = max(dp[i], 1 + dp[j]);
            }
        }

        int result = 0;
        for (int val : dp) {
            result = max(result, val);
        }
        return result;
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
    public int maxJumps(int[] arr, int d) {
        int n = arr.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }

        Arrays.sort(indices, (a, b) -> Integer.compare(arr[a], arr[b]));

        for (int i : indices) {
            for (int j = i + 1; j <= i + d && j < n; j++) {
                if (arr[j] >= arr[i]) break;
                dp[i] = Math.max(dp[i], 1 + dp[j]);
            }
            for (int j = i - 1; j >= i - d && j >= 0; j--) {
                if (arr[j] >= arr[i]) break;
                dp[i] = Math.max(dp[i], 1 + dp[j]);
            }
        }

        int maxVisited = 0;
        for (int val : dp) {
            maxVisited = Math.max(maxVisited, val);
        }
        return maxVisited;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        dp = [1] * n

        # Sort indices by their value in the array to process dependencies bottom-up
        indices = sorted(range(n), key=lambda i: arr[i])

        for i in indices:
            # Try jumping to the right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + dp[j])

            # Try jumping to the left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + dp[j])

        return max(dp) if dp else 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from functools import lru_cache
import sys
from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        sys.setrecursionlimit(2000)
        n = len(arr)

        @lru_cache(None)
        def solve(i):
            res = 1
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                current = 1 + solve(j)
                if current > res:
                    res = current
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                current = 1 + solve(j)
                if current > res:
                    res = current
            return res

        return max(solve(i) for i in range(n))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int solve(int i, int* arr, int n, int d, int* dp) {
    if (dp[i] != 0) return dp[i];
    int res = 1;
    for (int j = i + 1; j <= i + d && j < n; j++) {
        if (arr[j] >= arr[i]) break;
        int current = 1 + solve(j, arr, n, d, dp);
        if (current > res) res = current;
    }
    for (int j = i - 1; j >= i - d && j >= 0; j--) {
        if (arr[j] >= arr[i]) break;
        int current = 1 + solve(j, arr, n, d, dp);
        if (current > res) res = current;
    }
    return dp[i] = res;
}

int maxJumps(int* arr, int arrSize, int d) {
    int* dp = (int*)calloc(arrSize, sizeof(int));
    int max_res = 0;
    for (int i = 0; i < arrSize; i++) {
        int current = solve(i, arr, arrSize, d, dp);
        if (current > max_res) max_res = current;
    }
    free(dp);
    return max_res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MaxJumps(int[] arr, int d) {
        int n = arr.Length;
        int[] memo = new int[n];
        int maxResult = 0;
        for (int i = 0; i < n; i++) {
            int current = Solve(i, arr, d, n, memo);
            if (current > maxResult) {
                maxResult = current;
            }
        }
        return maxResult;
    }

    private int Solve(int i, int[] arr, int d, int n, int[] memo) {
        if (memo[i] != 0) return memo[i];
        int res = 1;
        for (int j = i + 1; j <= i + d && j < n; j++) {
            if (arr[j] >= arr[i]) break;
            int val = 1 + Solve(j, arr, d, n, memo);
            if (val > res) res = val;
        }
        for (int j = i - 1; j >= i - d && j >= 0; j--) {
            if (arr[j] >= arr[i]) break;
            int val = 1 + Solve(j, arr, d, n, memo);
            if (val > res) res = val;
        }
        memo[i] = res;
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
 * @param {number[]} arr
 * @param {number} d
 * @return {number}
 */
var maxJumps = function(arr, d) {
    const n = arr.length;
    const memo = new Int32Array(n);

    function solve(i) {
        if (memo[i] !== 0) return memo[i];
        let res = 1;
        for (let j = i + 1; j <= i + d && j < n; j++) {
            if (arr[j] >= arr[i]) break;
            let val = 1 + solve(j);
            if (val > res) res = val;
        }
        for (let j = i - 1; j >= i - d && j >= 0; j--) {
            if (arr[j] >= arr[i]) break;
            let val = 1 + solve(j);
            if (val > res) res = val;
        }
        return memo[i] = res;
    }

    let maxVal = 0;
    for (let i = 0; i < n; i++) {
        let current = solve(i);
        if (current > maxVal) maxVal = current;
    }
    return maxVal;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxJumps(arr: number[], d: number): number {
    const n = arr.length;
    const memo = new Array(n).fill(0);

    function solve(i: number): number {
        if (memo[i] !== 0) return memo[i];

        let res = 1;

        for (let j = i + 1; j <= Math.min(i + d, n - 1) && arr[i] > arr[j]; j++) {
            res = Math.max(res, 1 + solve(j));
        }

        for (let j = i - 1; j >= Math.max(0, i - d) && arr[i] > arr[j]; j--) {
            res = Math.max(res, 1 + solve(j));
        }

        return memo[i] = res;
    }

    let maxVisited = 0;
    for (let i = 0; i < n; i++) {
        maxVisited = Math.max(maxVisited, solve(i));
    }

    return maxVisited;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $d
     * @return Integer
     */
    private $memo = [];
    private $arr_data;
    private $jump_d;
    private $arr_len;

    function maxJumps($arr, $d) {
        $this->arr_data = $arr;
        $this->jump_d = $d;
        $this->arr_len = count($arr);
        $this->memo = array_fill(0, $this->arr_len, 0);

        $max_steps = 0;
        for ($i = 0; $i < $this->arr_len; $i++) {
            $max_steps = max($max_steps, $this->solve($i));
        }

        return $max_steps;
    }

    private function solve($i) {
        if ($this->memo[$i] != 0) {
            return $this->memo[$i];
        }

        $res = 1;

        for ($j = $i + 1; $j <= min($i + $this->jump_d, $this->arr_len - 1) && $this->arr_data[$i] > $this->arr_data[$j]; $j++) {
            $res = max($res, 1 + $this->solve($j));
        }

        for ($j = $i - 1; $j >= max(0, $i - $this->jump_d) && $this->arr_data[$i] > $this->arr_data[$j]; $j--) {
            $res = max($res, 1 + $this->solve($j));
        }

        $this->memo[$i] = $res;
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
    private var memo: [Int] = []
    private var arr: [Int] = []
    private var d: Int = 0
    private var n: Int = 0

    func maxJumps(_ arr: [Int], _ d: Int) -> Int {
        self.arr = arr
        self.d = d
        self.n = arr.count
        self.memo = Array(repeating: 0, count: n)

        var maxVisited = 0
        for i in 0..<n {
            maxVisited = max(maxVisited, solve(i))
        }
        return maxVisited
    }

    private func solve(_ i: Int) -> Int {
        if memo[i] != 0 {
            return memo[i]
        }

        var res = 1

        var j = i + 1
        while j <= min(i + d, n - 1) && arr[i] > arr[j] {
            res = max(res, 1 + solve(j))
            j += 1
        }

        j = i - 1
        while j >= max(0, i - d) && arr[i] > arr[j] {
            res = max(res, 1 + solve(j))
            j -= 1
        }

        memo[i] = res
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
    private lateinit var memo: IntArray
    private lateinit var arr: IntArray
    private var d: Int = 0
    private var n: Int = 0

    fun maxJumps(arr: IntArray, d: Int): Int {
        this.arr = arr
        this.d = d
        this.n = arr.size
        this.memo = IntArray(n) { 0 }

        var maxVisited = 0
        for (i in 0 until n) {
            maxVisited = Math.max(maxVisited, solve(i))
        }
        return maxVisited
    }

    private fun solve(i: Int): Int {
        if (memo[i] != 0) {
            return memo[i]
        }

        var res = 1

        // Look right
        var j = i + 1
        while (j <= Math.min(i + d, n - 1) && arr[i] > arr[j]) {
            res = Math.max(res, 1 + solve(j))
            j++
        }

        // Look left
        j = i - 1
        while (j >= Math.max(0, i - d) && arr[i] > arr[j]) {
            res = Math.max(res, 1 + solve(j))
            j--
        }

        memo[i] = res
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
  int maxJumps(List<int> arr, int d) {
    int n = arr.length;
    List<int> memo = List.filled(n, 0);

    int solve(int i) {
      if (memo[i] != 0) return memo[i];

      int res = 1;

      for (int j = i + 1; j < n && j <= i + d; j++) {
        if (arr[i] > arr[j]) {
          int v = 1 + solve(j);
          if (v > res) res = v;
        } else {
          break;
        }
      }

      for (int j = i - 1; j >= 0 && j >= i - d; j--) {
        if (arr[i] > arr[j]) {
          int v = 1 + solve(j);
          if (v > res) res = v;
        } else {
          break;
        }
      }

      memo[i] = res;
      return res;
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
      int current = solve(i);
      if (current > ans) ans = current;
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
func maxJumps(arr []int, d int) int {
    n := len(arr)
    memo := make([]int, n)

    var solve func(int) int
    solve = func(i int) int {
        if memo[i] != 0 {
            return memo[i]
        }

        res := 1

        for j := i + 1; j < n && j <= i+d; j++ {
            if arr[i] > arr[j] {
                v := 1 + solve(j)
                if v > res {
                    res = v
                }
            } else {
                break
            }
        }

        for j := i - 1; j >= 0 && j >= i-d; j-- {
            if arr[i] > arr[j] {
                v := 1 + solve(j)
                if v > res {
                    res = v
                }
            } else {
                break
            }
        }

        memo[i] = res
        return res
    }

    ans := 0
    for i := 0; i < n; i++ {
        v := solve(i)
        if v > ans {
            ans = v
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
def max_jumps(arr, d)
  n = arr.length
  memo = Array.new(n, 0)

  solve = lambda do |i|
    return memo[i] if memo[i] != 0

    res = 1

    j = i + 1
    while j < n && j <= i + d
      if arr[i] > arr[j]
        v = 1 + solve.call(j)
        res = v if v > res
      else
        break
      end
      j += 1
    end

    j = i - 1
    while j >= 0 && j >= i - d
      if arr[i] > arr[j]
        v = 1 + solve.call(j)
        res = v if v > res
      else
        break
      end
      j -= 1
    end

    memo[i] = res
    res
  end

  max_ans = 0
  (0...n).each do |i|
    v = solve.call(i)
    max_ans = v if v > max_ans
  end
  max_ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxJumps(arr: Array[Int], d: Int): Int = {
        val n = arr.length
        val memo = Array.fill(n)(0)

        def solve(i: Int): Int = {
            if (memo(i) != 0) return memo(i)

            var res = 1

            var j = i + 1
            while (j < n && j <= i + d && arr(i) > arr(j)) {
                val v = 1 + solve(j)
                if (v > res) res = v
                j += 1
            }

            j = i - 1
            while (j >= 0 && j >= i - d && arr(i) > arr(j)) {
                val v = 1 + solve(j)
                if (v > res) res = v
                j -= 1
            }

            memo(i) = res
            res
        }

        var maxAns = 0
        for (i <- 0 until n) {
            val v = solve(i)
            if (v > maxAns) maxAns = v
        }
        maxAns
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_jumps(arr: Vec<i32>, d: i32) -> i32 {
        let n = arr.len();
        let d = d as usize;
        let mut dp = vec![1; n];
        let mut indices: Vec<usize> = (0..n).collect();
        indices.sort_by_key(|&i| arr[i]);

        for &i in &indices {
            let val_i = arr[i];
            // Jump to the right
            for j in (i + 1)..std::cmp::min(i + d + 1, n) {
                if arr[j] < val_i {
                    dp[i] = std::cmp::max(dp[i], 1 + dp[j]);
                } else {
                    break;
                }
            }
            // Jump to the left
            for j in (0..i).rev().take(d) {
                if arr[j] < val_i {
                    dp[i] = std::cmp::max(dp[i], 1 + dp[j]);
                } else {
                    break;
                }
            }
        }

        *dp.iter().max().unwrap_or(&1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-jumps arr d)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length arr)]
         [vec-arr (list->vector arr)]
         [dp (make-vector n 1)]
         [indices (sort (range n) < #:key (lambda (i) (vector-ref vec-arr i)))])
    (for ([i indices])
      (let ([val-i (vector-ref vec-arr i)])
        (let loop-right ([j (+ i 1)])
          (when (and (< j n) (<= (- j i) d) (< (vector-ref vec-arr j) val-i))
            (vector-set! dp i (max (vector-ref dp i) (+ 1 (vector-ref dp j))))
            (loop-right (+ j 1))))
        (let loop-left ([j (- i 1)])
          (when (and (>= j 0) (<= (- i j) d) (< (vector-ref vec-arr j) val-i))
            (vector-set! dp i (max (vector-ref dp i) (+ 1 (vector-ref dp j))))
            (loop-left (- j 1))))))
    (apply max (vector->list dp))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_jumps(Arr :: [integer()], D :: integer()) -> integer().
max_jumps(Arr, D) ->
  N = length(Arr),
  ArrTuple = list_to_tuple(Arr),
  Indices = lists:sort(fun(I, J) ->
    element(I + 1, ArrTuple) =< element(J + 1, ArrTuple)
  end, lists:seq(0, N - 1)),
  FinalDP = lists:foldl(fun(I, AccDP) ->
    ValI = element(I + 1, ArrTuple),
    RMax = check_right(I + 1, erlang:min(I + D, N - 1), ValI, ArrTuple, AccDP, 0),
    LMax = check_left(I - 1, erlang:max(I - D, 0), ValI, ArrTuple, AccDP, 0),
    array:set(I, 1 + erlang:max(RMax, LMax), AccDP)
  end, array:new(N, {default, 0}), Indices),
  lists:max(array:to_list(FinalDP)).

check_right(J, MaxJ, ValI, ArrTuple, DP, CurrentMax) when J =< MaxJ ->
  ValJ = element(J + 1, ArrTuple),
  if ValJ < ValI ->
    NewMax = erlang:max(CurrentMax, array:get(J, DP)),
    check_right(J + 1, MaxJ, ValI, ArrTuple, DP, NewMax);
  true -> CurrentMax
  end;
check_right(_, _, _, _, _, CurrentMax) -> CurrentMax.

check_left(J, MinJ, ValI, ArrTuple, DP, CurrentMax) when J >= MinJ ->
  ValJ = element(J + 1, ArrTuple),
  if ValJ < ValI ->
    NewMax = erlang:max(CurrentMax, array:get(J, DP)),
    check_left(J - 1, MinJ, ValI, ArrTuple, DP, NewMax);
  true -> CurrentMax
  end;
check_left(_, _, _, _, _, CurrentMax) -> CurrentMax.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_jumps(arr :: [integer], d :: integer) :: integer
  def max_jumps(arr, d) do
    n = length(arr)
    arr_tuple = List.to_tuple(arr)
    indices = Enum.sort(0..(n - 1), fn i, j ->
      elem(arr_tuple, i) <= elem(arr_tuple, j)
    end)

    dp = Enum.reduce(indices, %{}, fn i, acc_dp ->
      val_i = elem(arr_tuple, i)
      r_max = check_right(i + 1, min(i + d, n - 1), val_i, arr_tuple, acc_dp, 0)
      l_max = check_left(i - 1, max(i - d, 0), val_i, arr_tuple, acc_dp, 0)
      Map.put(acc_dp, i, 1 + max(r_max, l_max))
    end)

    Enum.max(Map.values(dp))
  end

  defp check_right(j, max_j, val_i, arr_tuple, dp, current_max) when j <= max_j do
    val_j = elem(arr_tuple, j)
    if val_j < val_i do
      check_right(j + 1, max_j, val_i, arr_tuple, dp, max(current_max, Map.get(dp, j, 0)))
    else
      current_max
    end
  end
  defp check_right(_j, _max_j, _val_i, _arr_tuple, _dp, current_max), do: current_max

  defp check_left(j, min_j, val_i, arr_tuple, dp, current_max) when j >= min_j do
    val_j = elem(arr_tuple, j)
    if val_j < val_i do
      check_left(j - 1, min_j, val_i, arr_tuple, dp, max(current_max, Map.get(dp, j, 0)))
    else
      current_max
    end
  end
  defp check_left(_j, _min_j, _val_i, _arr_tuple, _dp, current_max), do: current_max
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * d) where N is the length of the array and d is the maximum jump distance. Sorting the indices takes O(N log N). After sorting, we iterate through each of the N indices once, and for each index, we scan at most d elements to the left and d elements to the right. This results in an overall complexity of O(N * d + N log N), which simplifies to O(N * d) because d is at least 1 and up to N.
- **Space Complexity:** O(N) because we store the dynamic programming results in an array of size N and maintain an auxiliary array of indices for the sorting process, both of which require linear space.
