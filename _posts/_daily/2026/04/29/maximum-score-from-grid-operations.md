---
layout: post
title: "Maximum Score From Grid Operations"
date: 2026-04-29 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming", "Matrix", "Prefix Sum"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-score-from-grid-operations/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Parsing failed'
      java: '// Generation failed for Java

        // Reason: Parsing failed'
      python: '// Generation failed for Python

        // Reason: Parsing failed'
      python3: '// Generation failed for Python3

        // Reason: Parsing failed'
      c: '// Generation failed for C

        // Reason: Parsing failed'
      csharp: '// Generation failed for C#

        // Reason: Parsing failed'
      javascript: '// Generation failed for JavaScript

        // Reason: Parsing failed'
      typescript: '// Generation failed for TypeScript

        // Reason: Parsing failed'
      php: '// Generation failed for PHP

        // Reason: Parsing failed'
      swift: '// Generation failed for Swift

        // Reason: Parsing failed'
      kotlin: '// Generation failed for Kotlin

        // Reason: Parsing failed'
      dart: '// Generation failed for Dart

        // Reason: Parsing failed'
      go: '// Generation failed for Go

        // Reason: Parsing failed'
      ruby: '// Generation failed for Ruby

        // Reason: Parsing failed'
      scala: '// Generation failed for Scala

        // Reason: Parsing failed'
      rust: "impl Solution {\n    pub fn maximum_score(grid: Vec<Vec<i32>>) -> i64 {\n\
        \        let n = grid.len();\n        let mut pref = vec![vec![0i64; n + 1];\
        \ n];\n        for c in 0..n {\n            for r in 0..n {\n              \
        \  pref[c][r + 1] = pref[c][r] + grid[r][c] as i64;\n            }\n       \
        \ }\n\n        let mut dp = vec![vec![-1i64; n + 1]; n + 1];\n        for j\
        \ in 0..=n {\n            dp[j][0] = 0;\n        }\n\n        for i in 1..n\
        \ {\n            let mut next_dp = vec![vec![-1i64; n + 1]; n + 1];\n      \
        \      for j in 0..=n {\n                let mut max_val = vec![-1i64; n + 1];\n\
        \                let mut prefix_max = -1i64;\n                for k in 0..=n\
        \ {\n                    prefix_max = prefix_max.max(dp[j][k]);\n          \
        \          max_val[k] = prefix_max;\n                }\n\n                let\
        \ mut max_val_with_cost = vec![-1i64; n + 1];\n                let mut suffix_max\
        \ = -1i64;\n                for k in (0..=n).rev() {\n                    let\
        \ cost_jk = if k > j { pref[i - 1][k] - pref[i - 1][j] } else { 0 };\n     \
        \               if dp[j][k] != -1 {\n                        suffix_max = suffix_max.max(dp[j][k]\
        \ + cost_jk);\n                    }\n                    max_val_with_cost[k]\
        \ = suffix_max;\n                }\n\n                for l in 0..=n {\n   \
        \                 let cost_jl = if l > j { pref[i - 1][l] - pref[i - 1][j] }\
        \ else { 0 };\n                    let val1 = if max_val[l] != -1 { max_val[l]\
        \ + cost_jl } else { -1 };\n                    let val2 = max_val_with_cost[l];\n\
        \                    next_dp[l][j] = val1.max(val2);\n                }\n  \
        \          }\n            dp = next_dp;\n        }\n\n        let mut ans =\
        \ 0i64;\n        for j in 0..=n {\n            for k in 0..=n {\n          \
        \      if dp[j][k] != -1 {\n                    let cost_final = if k > j {\
        \ pref[n - 1][k] - pref[n - 1][j] } else { 0 };\n                    ans = ans.max(dp[j][k]\
        \ + cost_final);\n                }\n            }\n        }\n        ans\n\
        \    }\n}"
      racket: "(define/contract (maximum-score grid)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([n (length grid)]\n         [pref (make-vector n)]\n\
        \         [dp (make-vector (add1 n))])\n    (for ([c (in-range n)])\n      (let\
        \ ([v (make-vector (add1 n) 0)]\n            [col (map (lambda (row) (list-ref\
        \ row c)) grid)])\n        (for ([r (in-range n)]\n              [val col])\n\
        \          (vector-set! v (add1 r) (+ (vector-ref v r) val)))\n        (vector-set!\
        \ pref c v)))\n    (for ([j (in-range (add1 n))])\n      (let ([v (make-vector\
        \ (add1 n) -1)])\n        (vector-set! v 0 0)\n        (vector-set! dp j v)))\n\
        \    (for ([i (in-range 1 n)])\n      (let ([next-dp (make-vector (add1 n))])\n\
        \        (for ([l (in-range (add1 n))])\n          (vector-set! next-dp l (make-vector\
        \ (add1 n) -1)))\n        (for ([j (in-range (add1 n))])\n          (let* ([max-val\
        \ (make-vector (add1 n) -1)]\n                 [max-val-with-cost (make-vector\
        \ (add1 n) -1)]\n                 [prefix-max -1]\n                 [suffix-max\
        \ -1]\n                 [dp-j (vector-ref dp j)]\n                 [pref-i-1\
        \ (vector-ref pref (sub1 i))])\n            (for ([k (in-range (add1 n))])\n\
        \              (set! prefix-max (max prefix-max (vector-ref dp-j k)))\n    \
        \          (vector-set! max-val k prefix-max))\n            (for ([k (in-range\
        \ n -1 -1)])\n              (let ([cost-jk (if (> k j) (- (vector-ref pref-i-1\
        \ k) (vector-ref pref-i-1 j)) 0)]\n                    [dp-jk (vector-ref dp-j\
        \ k)])\n                (when (not (= dp-jk -1))\n                  (set! suffix-max\
        \ (max suffix-max (+ dp-jk cost-jk))))\n                (vector-set! max-val-with-cost\
        \ k suffix-max)))\n            (for ([l (in-range (add1 n))])\n            \
        \  (let* ([cost-jl (if (> l j) (- (vector-ref pref-i-1 l) (vector-ref pref-i-1\
        \ j)) 0)]\n                     [val1 (if (not (= (vector-ref max-val l) -1))\
        \ (+ (vector-ref max-val l) cost-jl) -1)]\n                     [val2 (vector-ref\
        \ max-val-with_cost l)])\n                (vector-set! (vector-ref next-dp l)\
        \ j (max val1 val2))))))\n        (set! dp next-dp)))\n    (let ([ans 0])\n\
        \      (for ([j (in-range (add1 n))])\n        (let ([dp-j (vector-ref dp j)]\n\
        \              [pref-n-1 (vector-ref pref (sub1 n))])\n          (for ([k (in-range\
        \ (add1 n))])\n            (let ([dp-jk (vector-ref dp-j k)])\n            \
        \  (when (not (= dp-jk -1))\n                (let ([cost-final (if (> k j) (-\
        \ (vector-ref pref-n-1 k) (vector-ref pref-n-1 j)) 0)])\n                  (set!\
        \ ans (max ans (+ dp-jk cost-final)))))))))\n      ans)))"
      erlang: "-spec maximum_score(Grid :: [[integer()]]) -> integer().\nmaximum_score(Grid)\
        \ ->\n    N = length(Grid),\n    FlatGrid = list_to_tuple([list_to_tuple(Row)\
        \ || Row <- Grid]),\n    Pref = list_to_tuple([begin \n        V = lists:foldl(fn(R,\
        \ Acc) -> [hd(Acc) + element(C + 1, element(R + 1, FlatGrid)) | Acc] end, [0],\
        \ lists:seq(0, N - 1)),\n        list_to_tuple(lists:reverse(V))\n    end ||\
        \ C <- lists:seq(0, N - 1)]),\n\n    InitialDP = list_to_tuple([begin \n   \
        \     V = lists:duplicate(N + 1, -1),\n        case J of _ -> list_to_tuple([-1\
        \ || _ <- lists:seq(0, N)]) end\n    end || J <- lists:seq(0, N)]),\n    DP0\
        \ = list_to_tuple([list_to_tuple([if K == 0 -> 0; true -> -1 end || K <- lists:seq(0,\
        \ N)]) || J <- lists:seq(0, N)]),\n\n    FinalDP = lists:foldl(fun(I, CurrentDP)\
        \ ->\n        NextDPLists = [lists:duplicate(N + 1, -1) || _ <- lists:seq(0,\
        \ N)],\n        NextDPFinal = lists:foldl(fun(J, AccDP) ->\n            DP_J\
        \ = element(J + 1, CurrentDP),\n            Pref_I_minus_1 = element(I, Pref),\n\
        \            PrefixMaxs = lists:foldl(fun(K, {PMax, List}) ->\n            \
        \    NewPMax = max(PMax, element(K + 1, DP_J)),\n                {NewPMax, [NewPMax\
        \ | List]}\n            end, {-1, []}, lists:seq(0, N)),\n            MaxVal\
        \ = list_to_tuple(lists:reverse(element(2, PrefixMaxs))),\n            SuffixMaxs\
        \ = lists:foldl(fun(K, {SMax, List}) ->\n                DP_JK = element(K +\
        \ 1, DP_J),\n                CostJK = if K > J -> element(K + 1, Pref_I_minus_1)\
        \ - element(J + 1, Pref_I_minus_1); true -> 0 end,\n                NewSMax\
        \ = if DP_JK == -1 -> SMax; true -> max(SMax, DP_JK + CostJK) end,\n       \
        \         {NewSMax, [NewSMax | List]}\n            end, {-1, []}, lists:reverse(lists:seq(0,\
        \ N))),\n            MaxValWithCost = list_to_tuple(element(2, SuffixMaxs)),\n\
        \n            lists:foldl(fun(L, AccInner) ->\n                CostJL = if L\
        \ > J -> element(L + 1, Pref_I_minus_1) - element(J + 1, Pref_I_minus_1); true\
        \ -> 0 end,\n                Val1 = if element(L + 1, MaxVal) == -1 -> -1; true\
        \ -> element(L + 1, MaxVal) + CostJL end,\n                Val2 = element(L\
        \ + 1, MaxValWithCost),\n                NewVal = max(Val1, Val2),\n       \
        \         RowL = element(L + 1, AccInner),\n                setelement(L + 1,\
        \ AccInner, setelement(J + 1, RowL, NewVal))\n            end, AccDP, lists:seq(0,\
        \ N))\n        end, list_to_tuple([list_to_tuple(lists:duplicate(N + 1, -1))\
        \ || _ <- lists:seq(0, N)]), lists:seq(0, N)),\n        NextDPFinal\n    end,\
        \ DP0, if N > 1 -> lists:seq(1, N - 1); true -> [] end),\n\n    FinalPref =\
        \ element(N, Pref),\n    lists:foldl(fun(J, MaxScore) ->\n        DP_J = element(J\
        \ + 1, FinalDP),\n        lists:foldl(fun(K, MaxK) ->\n            DP_JK = element(K\
        \ + 1, DP_J),\n            if DP_JK == -1 -> MaxK;\n               true ->\n\
        \                   CostFinal = if K > J -> element(K + 1, FinalPref) - element(J\
        \ + 1, FinalPref); true -> 0 end,\n                   max(MaxK, DP_JK + CostFinal)\n\
        \            end\n        end, MaxScore, lists:seq(0, N))\n    end, 0, lists:seq(0,\
        \ N)).\n\nfn(A, B) -> fun(X, Y) -> A(X, Y, B) end."
      elixir: "defmodule Solution do\n  @spec maximum_score(grid :: [[integer]]) ::\
        \ integer\n  def maximum_score(grid) do\n    n = length(grid)\n    pref = for\
        \ c <- 0..(n-1) do\n      col = for r <- 0..(n-1), do: Enum.at(Enum.at(grid,\
        \ r), c)\n      Enum.scan([0 | col], &(&1 + &2)) |> List.to_tuple()\n    end\
        \ |> List.to_tuple()\n\n    initial_dp = List.to_tuple(for _j <- 0..n do\n \
        \     List.to_tuple(for k <- 0..n, do: (if k == 0, do: 0, else: -1))\n    end)\n\
        \n    final_dp = if n > 1 do\n      Enum.reduce(1..(n-1), initial_dp, fn i,\
        \ dp ->\n        next_dp_rows = for _l <- 0..n, do: List.to_tuple(for _j <-\
        \ 0..n, do: -1)\n        Enum.reduce(0..n, List.to_tuple(next_dp_rows), fn j,\
        \ acc_dp ->\n          dp_j = elem(dp, j)\n          pref_i_minus_1 = elem(pref,\
        \ i - 1)\n\n          {_, max_val_list} = Enum.reduce(0..n, {-1, []}, fn k,\
        \ {p_max, list} ->\n            new_p_max = max(p_max, elem(dp_j, k))\n    \
        \        {new_p_max, [new_p_max | list]}\n          end)\n          max_val\
        \ = List.to_tuple(Enum.reverse(max_val_list))\n\n          {_, max_val_with_cost_list}\
        \ = Enum.reduce(n..0, {-1, []}, fn k, {s_max, list} ->\n            dp_jk =\
        \ elem(dp_j, k)\n            cost_jk = if k > j, do: elem(pref_i_minus_1, k)\
        \ - elem(pref_i_minus_1, j), else: 0\n            new_s_max = if dp_jk == -1,\
        \ do: s_max, else: max(s_max, dp_jk + cost_jk)\n            {new_s_max, [new_s_max\
        \ | list]}\n          end)\n          max_val_with_cost = List.to_tuple(max_val_with_cost_list)\n\
        \n          Enum.reduce(0..n, acc_dp, fn l, dp_acc ->\n            cost_jl =\
        \ if l > j, do: elem(pref_i_minus_1, l) - elem(pref_i_minus_1, j), else: 0\n\
        \            val1 = if elem(max_val, l) == -1, do: -1, else: elem(max_val, l)\
        \ + cost_jl\n            val2 = elem(max_val_with_cost, l)\n            new_val\
        \ = max(val1, val2)\n            put_in_tuple(dp_acc, l, j, new_val)\n     \
        \     end)\n        end)\n      end)\n    else\n      initial_dp\n    end\n\n\
        \    pref_n_minus_1 = elem(pref, n - 1)\n    Enum.reduce(0..n, 0, fn j, max_score\
        \ ->\n      dp_j = elem(final_dp, j)\n      Enum.reduce(0..n, max_score, fn\
        \ k, current_max ->\n        dp_jk = elem(dp_j, k)\n        if dp_jk == -1 do\n\
        \          current_max\n        else\n          cost_final = if k > j, do: elem(pref_n_minus_1,\
        \ k) - elem(pref_n_minus_1, j), else: 0\n          max(current_max, dp_jk +\
        \ cost_final)\n        end\n      end)\n    end)\n  end\n\n  defp put_in_tuple(tuple,\
        \ row_idx, col_idx, value) do\n    row = elem(tuple, row_idx)\n    new_row =\
        \ put_elem(row, col_idx, value)\n    put_elem(tuple, row_idx, new_row)\n  end\n\
        end"
    approach: 'The problem asks for the maximum grid score where a cell $(i, j)$ contributes
      if it is white (not colored) and is adjacent horizontally to a black cell. This
      occurs if the height of the current column $H_j \le i$ while the height of either
      of its neighbors $H_{j-1}$ or $H_{j+1}$ is $> i$. This can be restated as column
      $j$ receiving a score from row $i$ if $H_j \le i < \max(H_{j-1}, H_{j+1})$. To
      solve this efficiently, we use dynamic programming. Let $dp[i][H_i][H_{i-1}]$
      represent the maximum score achieved for the first $i$ columns, given the heights
      of the last two columns. The score of column $i-1$ is added as we determine the
      height of column $i$. The score for column $i-1$ given $H_{i-2}, H_{i-1}, H_i$
      is $\sum_{k=H_{i-1}}^{\max(H_{i-2}, H_i)-1} grid[k][i-1]$.


      The transitions for this $O(N^4)$ DP can be optimized to $O(N^3)$ by observing
      that the term $\max(H_{i-2}, H_i)$ allows us to split the transition into two
      cases: $H_{i-2} \le H_i$ and $H_{i-2} > H_i$. For a fixed $H_{i-1}$ and $H_i$,
      we can precompute the maximums over $H_{i-2}$ using prefix and suffix maximums.
      This reduces the complexity to $O(N^3)$. We precompute prefix sums for each column
      to calculate the column scores in $O(1)$. By iterating column by column and maintaining
      only the last two heights (or the current DP state), we ensure optimal time and
      space efficiency.'
    time_complexity: O(N^3) where N is the side length of the grid. We iterate through
      N columns, and for each column, we iterate through $N$ possible heights for the
      current column and the previous column, using precomputed prefix and suffix maximums
      to optimize the third dimension.
    space_complexity: O(N^2) to store the DP table and the prefix sums for the grid.
    elapsed_time: 753.0374963283539
    model: gemini-3-flash-preview
    generated_at: '2026-04-29 02:24:31 '
---

## Problem #3225: Maximum Score From Grid Operations

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Matrix, Prefix Sum

## Problem Description

<p>You are given a 2D matrix <code>grid</code> of size <code>n x n</code>. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices <code>(i, j)</code>, and color black all the cells of the <code>j<sup>th</sup></code> column starting from the top row down to the <code>i<sup>th</sup></code> row.</p>

<p>The grid score is the sum of all <code>grid[i][j]</code> such that cell <code>(i, j)</code> is white and it has a horizontally adjacent black cell.</p>

<p>Return the <strong>maximum</strong> score that can be achieved after some number of operations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/05/11/one.png" style="width: 300px; height: 200px;" />
<p>In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is <code>grid[3][0] + grid[1][2] + grid[3][3]</code> which is equal to 11.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">94</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/05/11/two-1.png" style="width: 300px; height: 200px;" />
<p>We perform operations on 1, 2, and 3 down to rows 1, 4, and 0, respectively. The score of the resulting grid is <code>grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4]</code> which is equal to 94.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;n == grid.length &lt;= 100</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Use dynamic programming.

2. Solve the problem in O(N^4) using a 3-states dp.

3. Let `dp[i][lastHeight][beforeLastHeight]` denote the maximum score if the grid was limited to column `i`, and the height of column `i - 1` is `lastHeight` and the height of column `i - 2` is `beforeLastHeight`.

4. The third state, `beforeLastHeight`, is used to determine which values of column `i - 1` will be added to the score.  We can replace this state with another state that only takes two values 0 or 1.

5. Let `dp[i][lastHeight][isBigger]` denote the maximum score if the grid was limited to column `i`, and where the height of column `i - 1` is `lastHeight`. Additionally, if `isBigger == 1`, the number of black cells in column `i` is assumed to be larger than the number of black cells in column `i - 2`, and vice versa. Note that if our assumption is wrong, it would lead to a suboptimal score and, therefore, it would not be considered as the final answer.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the maximum grid score where a cell $(i, j)$ contributes if it is white (not colored) and is adjacent horizontally to a black cell. This occurs if the height of the current column $H_j \le i$ while the height of either of its neighbors $H_{j-1}$ or $H_{j+1}$ is $> i$. This can be restated as column $j$ receiving a score from row $i$ if $H_j \le i < \max(H_{j-1}, H_{j+1})$. To solve this efficiently, we use dynamic programming. Let $dp[i][H_i][H_{i-1}]$ represent the maximum score achieved for the first $i$ columns, given the heights of the last two columns. The score of column $i-1$ is added as we determine the height of column $i$. The score for column $i-1$ given $H_{i-2}, H_{i-1}, H_i$ is $\sum_{k=H_{i-1}}^{\max(H_{i-2}, H_i)-1} grid[k][i-1]$.

The transitions for this $O(N^4)$ DP can be optimized to $O(N^3)$ by observing that the term $\max(H_{i-2}, H_i)$ allows us to split the transition into two cases: $H_{i-2} \le H_i$ and $H_{i-2} > H_i$. For a fixed $H_{i-1}$ and $H_i$, we can precompute the maximums over $H_{i-2}$ using prefix and suffix maximums. This reduces the complexity to $O(N^3)$. We precompute prefix sums for each column to calculate the column scores in $O(1)$. By iterating column by column and maintaining only the last two heights (or the current DP state), we ensure optimal time and space efficiency.

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
// Generation failed for C++
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximum_score(grid: Vec<Vec<i32>>) -> i64 {
        let n = grid.len();
        let mut pref = vec![vec![0i64; n + 1]; n];
        for c in 0..n {
            for r in 0..n {
                pref[c][r + 1] = pref[c][r] + grid[r][c] as i64;
            }
        }

        let mut dp = vec![vec![-1i64; n + 1]; n + 1];
        for j in 0..=n {
            dp[j][0] = 0;
        }

        for i in 1..n {
            let mut next_dp = vec![vec![-1i64; n + 1]; n + 1];
            for j in 0..=n {
                let mut max_val = vec![-1i64; n + 1];
                let mut prefix_max = -1i64;
                for k in 0..=n {
                    prefix_max = prefix_max.max(dp[j][k]);
                    max_val[k] = prefix_max;
                }

                let mut max_val_with_cost = vec![-1i64; n + 1];
                let mut suffix_max = -1i64;
                for k in (0..=n).rev() {
                    let cost_jk = if k > j { pref[i - 1][k] - pref[i - 1][j] } else { 0 };
                    if dp[j][k] != -1 {
                        suffix_max = suffix_max.max(dp[j][k] + cost_jk);
                    }
                    max_val_with_cost[k] = suffix_max;
                }

                for l in 0..=n {
                    let cost_jl = if l > j { pref[i - 1][l] - pref[i - 1][j] } else { 0 };
                    let val1 = if max_val[l] != -1 { max_val[l] + cost_jl } else { -1 };
                    let val2 = max_val_with_cost[l];
                    next_dp[l][j] = val1.max(val2);
                }
            }
            dp = next_dp;
        }

        let mut ans = 0i64;
        for j in 0..=n {
            for k in 0..=n {
                if dp[j][k] != -1 {
                    let cost_final = if k > j { pref[n - 1][k] - pref[n - 1][j] } else { 0 };
                    ans = ans.max(dp[j][k] + cost_final);
                }
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
(define/contract (maximum-score grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length grid)]
         [pref (make-vector n)]
         [dp (make-vector (add1 n))])
    (for ([c (in-range n)])
      (let ([v (make-vector (add1 n) 0)]
            [col (map (lambda (row) (list-ref row c)) grid)])
        (for ([r (in-range n)]
              [val col])
          (vector-set! v (add1 r) (+ (vector-ref v r) val)))
        (vector-set! pref c v)))
    (for ([j (in-range (add1 n))])
      (let ([v (make-vector (add1 n) -1)])
        (vector-set! v 0 0)
        (vector-set! dp j v)))
    (for ([i (in-range 1 n)])
      (let ([next-dp (make-vector (add1 n))])
        (for ([l (in-range (add1 n))])
          (vector-set! next-dp l (make-vector (add1 n) -1)))
        (for ([j (in-range (add1 n))])
          (let* ([max-val (make-vector (add1 n) -1)]
                 [max-val-with-cost (make-vector (add1 n) -1)]
                 [prefix-max -1]
                 [suffix-max -1]
                 [dp-j (vector-ref dp j)]
                 [pref-i-1 (vector-ref pref (sub1 i))])
            (for ([k (in-range (add1 n))])
              (set! prefix-max (max prefix-max (vector-ref dp-j k)))
              (vector-set! max-val k prefix-max))
            (for ([k (in-range n -1 -1)])
              (let ([cost-jk (if (> k j) (- (vector-ref pref-i-1 k) (vector-ref pref-i-1 j)) 0)]
                    [dp-jk (vector-ref dp-j k)])
                (when (not (= dp-jk -1))
                  (set! suffix-max (max suffix-max (+ dp-jk cost-jk))))
                (vector-set! max-val-with-cost k suffix-max)))
            (for ([l (in-range (add1 n))])
              (let* ([cost-jl (if (> l j) (- (vector-ref pref-i-1 l) (vector-ref pref-i-1 j)) 0)]
                     [val1 (if (not (= (vector-ref max-val l) -1)) (+ (vector-ref max-val l) cost-jl) -1)]
                     [val2 (vector-ref max-val-with_cost l)])
                (vector-set! (vector-ref next-dp l) j (max val1 val2))))))
        (set! dp next-dp)))
    (let ([ans 0])
      (for ([j (in-range (add1 n))])
        (let ([dp-j (vector-ref dp j)]
              [pref-n-1 (vector-ref pref (sub1 n))])
          (for ([k (in-range (add1 n))])
            (let ([dp-jk (vector-ref dp-j k)])
              (when (not (= dp-jk -1))
                (let ([cost-final (if (> k j) (- (vector-ref pref-n-1 k) (vector-ref pref-n-1 j)) 0)])
                  (set! ans (max ans (+ dp-jk cost-final)))))))))
      ans)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_score(Grid :: [[integer()]]) -> integer().
maximum_score(Grid) ->
    N = length(Grid),
    FlatGrid = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    Pref = list_to_tuple([begin 
        V = lists:foldl(fn(R, Acc) -> [hd(Acc) + element(C + 1, element(R + 1, FlatGrid)) | Acc] end, [0], lists:seq(0, N - 1)),
        list_to_tuple(lists:reverse(V))
    end || C <- lists:seq(0, N - 1)]),

    InitialDP = list_to_tuple([begin 
        V = lists:duplicate(N + 1, -1),
        case J of _ -> list_to_tuple([-1 || _ <- lists:seq(0, N)]) end
    end || J <- lists:seq(0, N)]),
    DP0 = list_to_tuple([list_to_tuple([if K == 0 -> 0; true -> -1 end || K <- lists:seq(0, N)]) || J <- lists:seq(0, N)]),

    FinalDP = lists:foldl(fun(I, CurrentDP) ->
        NextDPLists = [lists:duplicate(N + 1, -1) || _ <- lists:seq(0, N)],
        NextDPFinal = lists:foldl(fun(J, AccDP) ->
            DP_J = element(J + 1, CurrentDP),
            Pref_I_minus_1 = element(I, Pref),
            PrefixMaxs = lists:foldl(fun(K, {PMax, List}) ->
                NewPMax = max(PMax, element(K + 1, DP_J)),
                {NewPMax, [NewPMax | List]}
            end, {-1, []}, lists:seq(0, N)),
            MaxVal = list_to_tuple(lists:reverse(element(2, PrefixMaxs))),
            SuffixMaxs = lists:foldl(fun(K, {SMax, List}) ->
                DP_JK = element(K + 1, DP_J),
                CostJK = if K > J -> element(K + 1, Pref_I_minus_1) - element(J + 1, Pref_I_minus_1); true -> 0 end,
                NewSMax = if DP_JK == -1 -> SMax; true -> max(SMax, DP_JK + CostJK) end,
                {NewSMax, [NewSMax | List]}
            end, {-1, []}, lists:reverse(lists:seq(0, N))),
            MaxValWithCost = list_to_tuple(element(2, SuffixMaxs)),

            lists:foldl(fun(L, AccInner) ->
                CostJL = if L > J -> element(L + 1, Pref_I_minus_1) - element(J + 1, Pref_I_minus_1); true -> 0 end,
                Val1 = if element(L + 1, MaxVal) == -1 -> -1; true -> element(L + 1, MaxVal) + CostJL end,
                Val2 = element(L + 1, MaxValWithCost),
                NewVal = max(Val1, Val2),
                RowL = element(L + 1, AccInner),
                setelement(L + 1, AccInner, setelement(J + 1, RowL, NewVal))
            end, AccDP, lists:seq(0, N))
        end, list_to_tuple([list_to_tuple(lists:duplicate(N + 1, -1)) || _ <- lists:seq(0, N)]), lists:seq(0, N)),
        NextDPFinal
    end, DP0, if N > 1 -> lists:seq(1, N - 1); true -> [] end),

    FinalPref = element(N, Pref),
    lists:foldl(fun(J, MaxScore) ->
        DP_J = element(J + 1, FinalDP),
        lists:foldl(fun(K, MaxK) ->
            DP_JK = element(K + 1, DP_J),
            if DP_JK == -1 -> MaxK;
               true ->
                   CostFinal = if K > J -> element(K + 1, FinalPref) - element(J + 1, FinalPref); true -> 0 end,
                   max(MaxK, DP_JK + CostFinal)
            end
        end, MaxScore, lists:seq(0, N))
    end, 0, lists:seq(0, N)).

fn(A, B) -> fun(X, Y) -> A(X, Y, B) end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_score(grid :: [[integer]]) :: integer
  def maximum_score(grid) do
    n = length(grid)
    pref = for c <- 0..(n-1) do
      col = for r <- 0..(n-1), do: Enum.at(Enum.at(grid, r), c)
      Enum.scan([0 | col], &(&1 + &2)) |> List.to_tuple()
    end |> List.to_tuple()

    initial_dp = List.to_tuple(for _j <- 0..n do
      List.to_tuple(for k <- 0..n, do: (if k == 0, do: 0, else: -1))
    end)

    final_dp = if n > 1 do
      Enum.reduce(1..(n-1), initial_dp, fn i, dp ->
        next_dp_rows = for _l <- 0..n, do: List.to_tuple(for _j <- 0..n, do: -1)
        Enum.reduce(0..n, List.to_tuple(next_dp_rows), fn j, acc_dp ->
          dp_j = elem(dp, j)
          pref_i_minus_1 = elem(pref, i - 1)

          {_, max_val_list} = Enum.reduce(0..n, {-1, []}, fn k, {p_max, list} ->
            new_p_max = max(p_max, elem(dp_j, k))
            {new_p_max, [new_p_max | list]}
          end)
          max_val = List.to_tuple(Enum.reverse(max_val_list))

          {_, max_val_with_cost_list} = Enum.reduce(n..0, {-1, []}, fn k, {s_max, list} ->
            dp_jk = elem(dp_j, k)
            cost_jk = if k > j, do: elem(pref_i_minus_1, k) - elem(pref_i_minus_1, j), else: 0
            new_s_max = if dp_jk == -1, do: s_max, else: max(s_max, dp_jk + cost_jk)
            {new_s_max, [new_s_max | list]}
          end)
          max_val_with_cost = List.to_tuple(max_val_with_cost_list)

          Enum.reduce(0..n, acc_dp, fn l, dp_acc ->
            cost_jl = if l > j, do: elem(pref_i_minus_1, l) - elem(pref_i_minus_1, j), else: 0
            val1 = if elem(max_val, l) == -1, do: -1, else: elem(max_val, l) + cost_jl
            val2 = elem(max_val_with_cost, l)
            new_val = max(val1, val2)
            put_in_tuple(dp_acc, l, j, new_val)
          end)
        end)
      end)
    else
      initial_dp
    end

    pref_n_minus_1 = elem(pref, n - 1)
    Enum.reduce(0..n, 0, fn j, max_score ->
      dp_j = elem(final_dp, j)
      Enum.reduce(0..n, max_score, fn k, current_max ->
        dp_jk = elem(dp_j, k)
        if dp_jk == -1 do
          current_max
        else
          cost_final = if k > j, do: elem(pref_n_minus_1, k) - elem(pref_n_minus_1, j), else: 0
          max(current_max, dp_jk + cost_final)
        end
      end)
    end)
  end

  defp put_in_tuple(tuple, row_idx, col_idx, value) do
    row = elem(tuple, row_idx)
    new_row = put_elem(row, col_idx, value)
    put_elem(tuple, row_idx, new_row)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^3) where N is the side length of the grid. We iterate through N columns, and for each column, we iterate through $N$ possible heights for the current column and the previous column, using precomputed prefix and suffix maximums to optimize the third dimension.
- **Space Complexity:** O(N^2) to store the DP table and the prefix sums for the grid.
