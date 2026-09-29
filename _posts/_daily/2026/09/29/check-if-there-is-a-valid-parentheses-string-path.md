---
layout: post
title: " Check if There Is a Valid Parentheses String Path"
date: 2026-09-29 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming", "Matrix", "Bracket Sequences"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <bitset>\n\nusing namespace std;\n\nclass Solution\
        \ {\npublic:\n    bool hasValidPath(vector<vector<char>>& grid) {\n        int\
        \ m = grid.size();\n        int n = grid[0].size();\n\n        if ((m + n) %\
        \ 2 == 0 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') {\n            return\
        \ false;\n        }\n\n        vector<vector<bitset<101>>> dp(m, vector<bitset<101>>(n));\n\
        \        dp[0][0][1] = 1;\n\n        for (int i = 0; i < m; ++i) {\n       \
        \     for (int j = 0; j < n; ++j) {\n                if (i == 0 && j == 0) continue;\n\
        \n                bitset<101> prev;\n                if (i > 0) prev |= dp[i\
        \ - 1][j];\n                if (j > 0) prev |= dp[i][j - 1];\n\n           \
        \     if (grid[i][j] == '(') {\n                    dp[i][j] = prev << 1;\n\
        \                } else {\n                    dp[i][j] = prev >> 1;\n     \
        \           }\n            }\n        }\n\n        return dp[m - 1][n - 1][0];\n\
        \    }\n};"
      java: "class Solution {\n    public boolean hasValidPath(char[][] grid) {\n  \
        \      int m = grid.length;\n        int n = grid[0].length;\n\n        if ((m\
        \ + n) % 2 == 0 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') {\n     \
        \       return false;\n        }\n\n        int maxBal = (m + n) / 2;\n    \
        \    boolean[][][] dp = new boolean[m][n][maxBal + 1];\n\n        dp[0][0][1]\
        \ = true;\n\n        for (int i = 0; i < m; i++) {\n            for (int j =\
        \ 0; j < n; j++) {\n                for (int k = 0; k <= maxBal; k++) {\n  \
        \                  if (!dp[i][j][k]) continue;\n\n                    // Down\
        \ move\n                    if (i + 1 < m) {\n                        int nk\
        \ = k + (grid[i + 1][j] == '(' ? 1 : -1);\n                        if (nk >=\
        \ 0 && nk <= maxBal) {\n                            dp[i + 1][j][nk] = true;\n\
        \                        }\n                    }\n\n                    //\
        \ Right move\n                    if (j + 1 < n) {\n                       \
        \ int nk = k + (grid[i][j + 1] == '(' ? 1 : -1);\n                        if\
        \ (nk >= 0 && nk <= maxBal) {\n                            dp[i][j + 1][nk]\
        \ = true;\n                        }\n                    }\n              \
        \  }\n            }\n        }\n\n        return dp[m - 1][n - 1][0];\n    }\n\
        }"
      python: "class Solution(object):\n    def hasValidPath(self, grid):\n        \"\
        \"\"\n        :type grid: List[List[str]]\n        :rtype: bool\n        \"\"\
        \"\n        m = len(grid)\n        n = len(grid[0])\n\n        # Path length\
        \ is m + n - 1. Valid parentheses strings have even length.\n        # Therefore\
        \ m + n - 1 must be even, so m + n must be odd.\n        if (m + n) % 2 == 0\
        \ or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':\n            return False\n\
        \n        # dp[j] stores the reachable balances at cell (current_row, j) as\
        \ a bitmask.\n        # Bit k is set if balance k is reachable.\n        dp\
        \ = [0] * n\n\n        # Initial state: after processing grid[0][0], which must\
        \ be '(', balance is 1.\n        dp[0] = 1 << 1\n\n        for i in range(m):\n\
        \            for j in range(n):\n                if i == 0 and j == 0:\n   \
        \                 continue\n\n                prev_mask = 0\n              \
        \  if i > 0:\n                    prev_mask |= dp[j]\n                if j >\
        \ 0:\n                    prev_mask |= dp[j - 1]\n\n                if grid[i][j]\
        \ == '(':\n                    dp[j] = prev_mask << 1\n                else:\n\
        \                    # Right shift handles the balance >= 0 constraint automatically,\n\
        \                    # as shifting bit 0 right results in it disappearing.\n\
        \                    dp[j] = prev_mask >> 1\n\n        return bool(dp[n - 1]\
        \ & 1)"
      python3: "class Solution:\n    def hasValidPath(self, grid: list[list[str]]) ->\
        \ bool:\n        m, n = len(grid), len(grid[0])\n        # A valid parentheses\
        \ string path must have an even length (m + n - 1).\n        # So m + n must\
        \ be odd.\n        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n\
        \ - 1] == '(':\n            return False\n\n        # dp[r][c] is a bitmask\
        \ where the i-th bit is set if a balance of i is possible at cell (r, c).\n\
        \        # A balance is the number of '(' minus the number of ')'.\n       \
        \ dp = [[0] * n for _ in range(m)]\n\n        # Initial state: after including\
        \ grid[0][0], the balance is 1.\n        dp[0][0] = 1 << 1\n\n        for r\
        \ in range(m):\n            for c in range(n):\n                if r == 0 and\
        \ c == 0: continue\n\n                prev_masks = 0\n                if r >\
        \ 0:\n                    prev_masks |= dp[r - 1][c]\n                if c >\
        \ 0:\n                    prev_masks |= dp[r][c - 1]\n\n                if grid[r][c]\
        \ == '(':\n                    # Increment balance for all possible states\n\
        \                    dp[r][c] = prev_masks << 1\n                else:\n   \
        \                 # Decrement balance for all possible states. Right-shift effectively\n\
        \                    # removes states with balance 0 (which would become -1).\n\
        \                    dp[r][c] = prev_masks >> 1\n\n                # Pruning:\
        \ at current cell (r, c), the balance cannot exceed the remaining steps.\n \
        \               rem_steps = (m - 1 - r) + (n - 1 - c)\n                mask\
        \ = (1 << (rem_steps + 1)) - 1\n                dp[r][c] &= mask\n\n       \
        \ # Result: can we reach the end with a balance of 0 (the 0-th bit)?\n     \
        \   return bool(dp[m - 1][n - 1] & 1)"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n#include <string.h>\n\nbool hasValidPath(char**\
        \ grid, int gridSize, int* gridColSize) {\n    int m = gridSize;\n    int n\
        \ = gridColSize[0];\n\n    if ((m + n) % 2 == 0 || grid[0][0] == ')' || grid[m\
        \ - 1][n - 1] == '(') {\n        return false;\n    }\n\n    const int max_b\
        \ = 101;\n    bool* dp = (bool*)calloc(m * n * max_b, sizeof(bool));\n    if\
        \ (!dp) return false;\n\n    // dp[(r * n + c) * max_b + b] represents if balance\
        \ b is possible at (r, c)\n    dp[(0 * n + 0) * max_b + 1] = true;\n\n    for\
        \ (int r = 0; r < m; r++) {\n        for (int c = 0; c < n; c++) {\n       \
        \     int rem = (m - 1 - r) + (n - 1 - c);\n            for (int b = 0; b <\
        \ max_b; b++) {\n                if (!dp[(r * n + c) * max_b + b]) continue;\n\
        \n                // Pruning\n                if (b > rem) continue;\n\n   \
        \             // Move Down\n                if (r + 1 < m) {\n             \
        \       int nb = b + (grid[r + 1][c] == '(' ? 1 : -1);\n                   \
        \ if (nb >= 0 && nb < max_b) {\n                        dp[((r + 1) * n + c)\
        \ * max_b + nb] = true;\n                    }\n                }\n\n      \
        \          // Move Right\n                if (c + 1 < n) {\n               \
        \     int nb = b + (grid[r][c + 1] == '(' ? 1 : -1);\n                    if\
        \ (nb >= 0 && nb < max_b) {\n                        dp[(r * n + (c + 1)) *\
        \ max_b + nb] = true;\n                    }\n                }\n          \
        \  }\n        }\n    }\n\n    bool result = dp[((m - 1) * n + (n - 1)) * max_b\
        \ + 0];\n    free(dp);\n    return result;\n}"
      csharp: "public class Solution {\n    public bool HasValidPath(char[][] grid)\
        \ {\n        int m = grid.Length;\n        int n = grid[0].Length;\n\n     \
        \   if ((m + n) % 2 == 0 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(')\
        \ {\n            return false;\n        }\n\n        const int max_b = 101;\n\
        \        bool[,,] dp = new bool[m, n, max_b];\n\n        dp[0, 0, 1] = true;\n\
        \n        for (int r = 0; r < m; r++) {\n            for (int c = 0; c < n;\
        \ c++) {\n                int rem = (m - 1 - r) + (n - 1 - c);\n           \
        \     for (int b = 0; b < max_b; b++) {\n                    if (!dp[r, c, b])\
        \ continue;\n\n                    if (b > rem) continue;\n\n              \
        \      // Move Down\n                    if (r + 1 < m) {\n                \
        \        int nb = b + (grid[r + 1][c] == '(' ? 1 : -1);\n                  \
        \      if (nb >= 0 && nb < max_b) {\n                            dp[r + 1, c,\
        \ nb] = true;\n                        }\n                    }\n\n        \
        \            // Move Right\n                    if (c + 1 < n) {\n         \
        \               int nb = b + (grid[r][c + 1] == '(' ? 1 : -1);\n           \
        \             if (nb >= 0 && nb < max_b) {\n                            dp[r,\
        \ c + 1, nb] = true;\n                        }\n                    }\n   \
        \             }\n            }\n        }\n\n        return dp[m - 1, n - 1,\
        \ 0];\n    }\n}"
      javascript: "/**\n * @param {character[][]} grid\n * @return {boolean}\n */\n\
        var hasValidPath = function(grid) {\n    const m = grid.length, n = grid[0].length;\n\
        \n    if ((m + n) % 2 === 0 || grid[0][0] === ')' || grid[m - 1][n - 1] ===\
        \ '(') {\n        return false;\n    }\n\n    // Using BigInt bitmasks to handle\
        \ balances up to 100 efficiently.\n    let dp = Array.from({ length: m }, ()\
        \ => new BigUint64Array(n).fill(0n));\n    let dpTable = Array.from({ length:\
        \ m }, () => Array(n).fill(0n));\n\n    dpTable[0][0] = 1n << 1n;\n\n    for\
        \ (let r = 0; r < m; r++) {\n        for (let c = 0; c < n; c++) {\n       \
        \     if (r === 0 && c === 0) continue;\n\n            let prevMasks = 0n;\n\
        \            if (r > 0) prevMasks |= dpTable[r - 1][c];\n            if (c >\
        \ 0) prevMasks |= dpTable[r][c - 1];\n\n            if (grid[r][c] === '(')\
        \ {\n                dpTable[r][c] = prevMasks << 1n;\n            } else {\n\
        \                dpTable[r][c] = prevMasks >> 1n;\n            }\n\n       \
        \     // Pruning balance values that are impossible to close.\n            let\
        \ rem = (m - 1 - r) + (n - 1 - c);\n            let mask = (1n << BigInt(rem\
        \ + 1)) - 1n;\n            dpTable[r][c] &= mask;\n        }\n    }\n\n    return\
        \ (dpTable[m - 1][n - 1] & 1n) === 1n;\n};"
      typescript: "function hasValidPath(grid: string[][]): boolean {\n    const m =\
        \ grid.length;\n    const n = grid[0].length;\n    if ((m + n - 1) % 2 !== 0\
        \ || grid[0][0] === ')' || grid[m - 1][n - 1] === '(') {\n        return false;\n\
        \    }\n\n    const dp: bigint[] = new Array(n).fill(0n);\n    dp[0] = 1n <<\
        \ 1n;\n\n    for (let i = 0; i < m; i++) {\n        for (let j = 0; j < n; j++)\
        \ {\n            if (i === 0 && j === 0) continue;\n\n            let combined\
        \ = 0n;\n            if (i > 0) combined |= dp[j];\n            if (j > 0) combined\
        \ |= dp[j - 1];\n\n            if (grid[i][j] === '(') {\n                dp[j]\
        \ = combined << 1n;\n            } else {\n                dp[j] = combined\
        \ >> 1n;\n            }\n        }\n    }\n\n    return (dp[n - 1] & 1n) ===\
        \ 1n;\n}"
      php: "class Solution {\n\n    /**\n     * @param String[][] $grid\n     * @return\
        \ Boolean\n     */\n    function hasValidPath($grid) {\n        $m = count($grid);\n\
        \        $n = count($grid[0]);\n        if (($m + $n - 1) % 2 !== 0 || $grid[0][0]\
        \ === ')' || $grid[$m - 1][$n - 1] === '(') {\n            return false;\n \
        \       }\n\n        $maxK = (int)(($m + $n) / 2);\n        $dp = array_fill(0,\
        \ $n, array_fill(0, $maxK + 1, false));\n        $dp[0][1] = true;\n\n     \
        \   for ($i = 0; $i < $m; $i++) {\n            for ($j = 0; $j < $n; $j++) {\n\
        \                if ($i === 0 && $j === 0) continue;\n\n                $char\
        \ = $grid[$i][$j];\n                $current = array_fill(0, $maxK + 1, false);\n\
        \                $isOpening = ($char === '(');\n\n                for ($k =\
        \ 0; $k <= $maxK; $k++) {\n                    if (($i > 0 && $dp[$j][$k]) ||\
        \ ($j > 0 && $dp[$j - 1][$k])) {\n                        if ($isOpening) {\n\
        \                            if ($k + 1 <= $maxK) {\n                      \
        \          $current[$k + 1] = true;\n                            }\n       \
        \                 } else {\n                            if ($k - 1 >= 0) {\n\
        \                                $current[$k - 1] = true;\n                \
        \            }\n                        }\n                    }\n         \
        \       }\n                $dp[$j] = $current;\n            }\n        }\n\n\
        \        return $dp[$n - 1][0];\n    }\n}"
      swift: "class Solution {\n    func hasValidPath(_ grid: [[Character]]) -> Bool\
        \ {\n        let m = grid.count\n        let n = grid[0].count\n        if (m\
        \ + n - 1) % 2 != 0 || grid[0][0] == \")\" || grid[m - 1][n - 1] == \"(\" {\n\
        \            return false\n        }\n\n        let maxK = (m + n) / 2\n   \
        \     var dp = Array(repeating: Array(repeating: false, count: maxK + 1), count:\
        \ n)\n        dp[0][1] = true\n\n        for i in 0..<m {\n            for j\
        \ in 0..<n {\n                if i == 0 && j == 0 { continue }\n\n         \
        \       let isOpening = grid[i][j] == \"(\"\n                var current = Array(repeating:\
        \ false, count: maxK + 1)\n\n                for k in 0...maxK {\n         \
        \           if (i > 0 && dp[j][k]) || (j > 0 && dp[j - 1][k]) {\n          \
        \              if isOpening {\n                            if k + 1 <= maxK\
        \ {\n                                current[k + 1] = true\n               \
        \             }\n                        } else {\n                        \
        \    if k - 1 >= 0 {\n                                current[k - 1] = true\n\
        \                            }\n                        }\n                \
        \    }\n                }\n                dp[j] = current\n            }\n\
        \        }\n\n        return dp[n - 1][0]\n    }\n}"
      kotlin: "import java.util.BitSet\n\nclass Solution {\n    fun hasValidPath(grid:\
        \ Array<CharArray>): Boolean {\n        val m = grid.size\n        val n = grid[0].size\n\
        \        if ((m + n - 1) % 2 != 0 || grid[0][0] == ')' || grid[m - 1][n - 1]\
        \ == '(') {\n            return false\n        }\n\n        val maxK = (m +\
        \ n) / 2\n        val dp = Array(n) { BitSet(maxK + 1) }\n        dp[0].set(1)\n\
        \n        for (i in 0 until m) {\n            for (j in 0 until n) {\n     \
        \           if (i == 0 && j == 0) continue\n\n                val combined =\
        \ BitSet(maxK + 1)\n                if (i > 0) combined.or(dp[j])\n        \
        \        if (j > 0) combined.or(dp[j - 1])\n\n                val current =\
        \ BitSet(maxK + 1)\n                if (grid[i][j] == '(') {\n             \
        \       for (k in 0 until maxK) {\n                        if (combined.get(k))\
        \ current.set(k + 1)\n                    }\n                } else {\n    \
        \                for (k in 1..maxK) {\n                        if (combined.get(k))\
        \ current.set(k - 1)\n                    }\n                }\n           \
        \     dp[j] = current\n            }\n        }\n\n        return dp[n - 1].get(0)\n\
        \    }\n}"
      dart: "class Solution {\n  bool hasValidPath(List<List<String>> grid) {\n    int\
        \ m = grid.length;\n    int n = grid[0].length;\n    if ((m + n - 1) % 2 !=\
        \ 0) return false;\n    if (grid[0][0] == ')' || grid[m - 1][n - 1] == '(')\
        \ return false;\n\n    List<BigInt> dp = List.filled(n, BigInt.zero);\n\n  \
        \  if (grid[0][0] == '(') {\n      dp[0] = BigInt.one << 1;\n    } else {\n\
        \      return false;\n    }\n\n    for (int c = 1; c < n; c++) {\n      if (grid[0][c]\
        \ == '(') {\n        dp[c] = dp[c - 1] << 1;\n      } else {\n        dp[c]\
        \ = dp[c - 1] >> 1;\n      }\n    }\n\n    for (int r = 1; r < m; r++) {\n \
        \     if (grid[r][0] == '(') {\n        dp[0] = dp[0] << 1;\n      } else {\n\
        \        dp[0] = dp[0] >> 1;\n      }\n      for (int c = 1; c < n; c++) {\n\
        \        BigInt prev = dp[c - 1] | dp[c];\n        if (grid[r][c] == '(') {\n\
        \          dp[c] = prev << 1;\n        } else {\n          dp[c] = prev >> 1;\n\
        \        }\n      }\n    }\n\n    return (dp[n - 1] & BigInt.one) != BigInt.zero;\n\
        \  }\n}"
      go: "import \"math/big\"\n\nfunc hasValidPath(grid [][]byte) bool {\n    m :=\
        \ len(grid)\n    n := len(grid[0])\n    if (m+n-1)%2 != 0 || grid[0][0] == ')'\
        \ || grid[m-1][n-1] == '(' {\n        return false\n    }\n\n    dp := make([]*big.Int,\
        \ n)\n    for i := range dp {\n        dp[i] = big.NewInt(0)\n    }\n\n    dp[0].SetUint64(2)\n\
        \    for c := 1; c < n; c++ {\n        if grid[0][c] == '(' {\n            dp[c].Lsh(dp[c-1],\
        \ 1)\n        } else {\n            dp[c].Rsh(dp[c-1], 1)\n        }\n    }\n\
        \n    prev := new(big.Int)\n    for r := 1; r < m; r++ {\n        if grid[r][0]\
        \ == '(' {\n            dp[0].Lsh(dp[0], 1)\n        } else {\n            dp[0].Rsh(dp[0],\
        \ 1)\n        }\n        for c := 1; c < n; c++ {\n            prev.Or(dp[c-1],\
        \ dp[c])\n            if grid[r][c] == '(' {\n                dp[c].Lsh(prev,\
        \ 1)\n            } else {\n                dp[c].Rsh(prev, 1)\n           \
        \ }\n        }\n    }\n\n    return dp[n-1].Bit(0) == 1\n}"
      ruby: "# @param {Character[][]} grid\n# @return {Boolean}\ndef has_valid_path(grid)\n\
        \  m = grid.length\n  n = grid[0].length\n  return false if (m + n - 1) % 2\
        \ != 0\n  return false if grid[0][0] == ')' || grid[m - 1][n - 1] == '('\n\n\
        \  dp = Array.new(n, 0)\n  dp[0] = 1 << 1\n\n  (1...n).each do |c|\n    if grid[0][c]\
        \ == '('\n      dp[c] = dp[c - 1] << 1\n    else\n      dp[c] = dp[c - 1] >>\
        \ 1\n    end\n  end\n\n  (1...m).each do |r|\n    if grid[r][0] == '('\n   \
        \   dp[0] <<= 1\n    else\n      dp[0] >>= 1\n    end\n\n    (1...n).each do\
        \ |c|\n      prev = dp[c - 1] | dp[c]\n      if grid[r][c] == '('\n        dp[c]\
        \ = prev << 1\n      else\n        dp[c] = prev >> 1\n      end\n    end\n \
        \ end\n\n  (dp[n - 1] & 1) != 0\nend"
      scala: "import scala.math.BigInt\n\nobject Solution {\n    def hasValidPath(grid:\
        \ Array[Array[Char]]): Boolean = {\n        val m = grid.length\n        val\
        \ n = grid(0).length\n        if ((m + n - 1) % 2 != 0) return false\n     \
        \   if (grid(0)(0) == ')' || grid(m - 1)(n - 1) == '(') return false\n\n   \
        \     val dp = Array.fill(n)(BigInt(0))\n\n        dp(0) = BigInt(1) << 1\n\
        \        for (c <- 1 until n) {\n            if (grid(0)(c) == '(') dp(c) =\
        \ dp(c - 1) << 1\n            else dp(c) = dp(c - 1) >> 1\n        }\n\n   \
        \     for (r <- 1 until m) {\n            if (grid(r)(0) == '(') dp(0) = dp(0)\
        \ << 1\n            else dp(0) = dp(0) >> 1\n            for (c <- 1 until n)\
        \ {\n                val prevBalances = dp(c - 1) | dp(c)\n                if\
        \ (grid(r)(c) == '(') dp(c) = prevBalances << 1\n                else dp(c)\
        \ = prevBalances >> 1\n            }\n        }\n\n        dp(n - 1).testBit(0)\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn has_valid_path(grid: Vec<Vec<char>>) -> bool\
        \ {\n        let m = grid.len();\n        let n = grid[0].len();\n        let\
        \ l = m + n - 1;\n        if l % 2 != 0 || grid[0][0] == ')' || grid[m - 1][n\
        \ - 1] == '(' {\n            return false;\n        }\n\n        let mut dp\
        \ = vec![vec![[false; 101]; n]; m];\n        dp[0][0][1] = true;\n\n       \
        \ for r in 0..m {\n            for c in 0..n {\n                for k in 0..101\
        \ {\n                    if !dp[r][c][k] { continue; }\n\n                 \
        \   let rem_steps = m + n - r - c - 2;\n\n                    if c + 1 < n {\n\
        \                        let nk = if grid[r][c + 1] == '(' { k + 1 } else {\
        \ k as i32 - 1 };\n                        if nk >= 0 && nk <= 100 && (nk as\
        \ usize) <= rem_steps {\n                            dp[r][c + 1][nk as usize]\
        \ = true;\n                        }\n                    }\n\n            \
        \        if r + 1 < m {\n                        let nk = if grid[r + 1][c]\
        \ == '(' { k + 1 } else { k as i32 - 1 };\n                        if nk >=\
        \ 0 && nk <= 100 && (nk as usize) <= rem_steps {\n                         \
        \   dp[r + 1][c][nk as usize] = true;\n                        }\n         \
        \           }\n                }\n            }\n        }\n        dp[m - 1][n\
        \ - 1][0]\n    }\n}"
      racket: "(define/contract (has-valid-path grid)\n  (-> (listof (listof char?))\
        \ boolean?)\n  (let* ([m (length grid)]\n         [n (length (car grid))]\n\
        \         [L (+ m n -1)])\n    (if (or (odd? L) (char=? (caar grid) #\\)))\n\
        \        #f\n        (let* ([grid-vec (list->vector (map list->vector grid))]\n\
        \               [dp (make-vector (* m n 101) #f)])\n          (define (get-idx\
        \ r c k) (+ (* r n 101) (* c 101) k))\n          (vector-set! dp (get-idx 0\
        \ 0 1) #t)\n          (for ([r (in-range m)])\n            (for ([c (in-range\
        \ n)])\n              (for ([k (in-range 101)])\n                (when (vector-ref\
        \ dp (get-idx r c k))\n                  (let ([rem-steps (- (+ m n) r c 2)])\n\
        \                    (when (< (+ c 1) n)\n                      (let* ([ch (vector-ref\
        \ (vector-ref grid-vec r) (+ c 1))]\n                             [nk (if (char=?\
        \ ch #\\() (+ k 1) (- k 1))])\n                        (when (and (>= nk 0)\
        \ (<= nk 100) (<= nk rem-steps))\n                          (vector-set! dp\
        \ (get-idx r (+ c 1) nk) #t))))\n                    (when (< (+ r 1) m)\n \
        \                     (let* ([ch (vector-ref (vector-ref grid-vec (+ r 1)) c)]\n\
        \                             [nk (if (char=? ch #\\() (+ k 1) (- k 1))])\n\
        \                        (when (and (>= nk 0) (<= nk 100) (<= nk rem-steps))\n\
        \                          (vector-set! dp (get-idx (+ r 1) c nk) #t)))))))))\n\
        \          (vector-ref dp (get-idx (- m 1) (- n 1) 0))))))"
      erlang: "-spec has_valid_path(Grid :: [[char()]]) -> boolean().\nhas_valid_path(Grid)\
        \ ->\n  M = length(Grid),\n  N = length(hd(Grid)),\n  L = M + N - 1,\n  case\
        \ L rem 2 of\n    1 -> false;\n    0 ->\n      case hd(hd(Grid)) of\n      \
        \  $) -> false;\n        $( ->\n          GridVec = list_to_tuple([list_to_tuple(R)\
        \ || R <- Grid]),\n          Cache = ets:new(memo, [set]),\n          Result\
        \ = solve(0, 0, 0, GridVec, M, N, Cache),\n          ets:delete(Cache),\n  \
        \        Result\n      end\n  end.\n\nsolve(R, C, K, GridVec, M, N, Cache) ->\n\
        \  case ets:lookup(Cache, {R, C, K}) of\n    [{_, Val}] -> Val;\n    [] ->\n\
        \      Char = element(C + 1, element(R + 1, GridVec)),\n      NewK = if Char\
        \ == $( -> K + 1; true -> K - 1 end,\n      Res = if\n        NewK < 0 -> false;\n\
        \        NewK > (M - 1 - R) + (N - 1 - C) -> false;\n        R == M - 1, C ==\
        \ N - 1 -> NewK == 0;\n        true ->\n          (R + 1 < M andalso solve(R\
        \ + 1, C, NewK, GridVec, M, N, Cache))\n          orelse (C + 1 < N andalso\
        \ solve(R, C + 1, NewK, GridVec, M, N, Cache))\n      end,\n      ets:insert(Cache,\
        \ {{R, C, K}, Res}),\n      Res\n  end."
      elixir: "defmodule Solution do\n  @spec has_valid_path(grid :: [[char]]) :: boolean\n\
        \  def has_valid_path(grid) do\n    m = length(grid)\n    n = length(hd(grid))\n\
        \    if rem(m + n, 2) == 0 do\n      false\n    else\n      grid_tuple = grid\
        \ |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n      cache = :ets.new(:memo,\
        \ [:set])\n      result = solve(0, 0, 0, grid_tuple, m, n, cache)\n      :ets.delete(cache)\n\
        \      result\n    end\n  end\n\n  defp solve(r, c, k, grid_tuple, m, n, cache)\
        \ do\n    case :ets.lookup(cache, {r, c, k}) do\n      [{_, val}] -> val\n \
        \     [] ->\n        char = elem(elem(grid_tuple, r), c)\n        new_k = if\
        \ char == ?(, do: k + 1, else: k - 1\n        res = cond do\n          new_k\
        \ < 0 -> false\n          new_k > (m - 1 - r) + (n - 1 - c) -> false\n     \
        \     r == m - 1 and c == n - 1 -> new_k == 0\n          true ->\n         \
        \   (r + 1 < m && solve(r + 1, c, new_k, grid_tuple, m, n, cache)) ||\n    \
        \        (c + 1 < n && solve(r, c + 1, new_k, grid_tuple, m, n, cache))\n  \
        \      end\n        :ets.insert(cache, {{r, c, k}, res})\n        res\n    end\n\
        \  end\nend"
    approach: The problem asks whether a path exists from the top-left to the bottom-right
      of an $m \times n$ grid that forms a valid parentheses string, moving only down
      or right. A parentheses string is valid if its total length is even, it has an
      equal number of open and closed brackets, and no prefix contains more closed brackets
      than open brackets. We utilize dynamic programming where the state at each cell
      $(r, c)$ tracks the possible cumulative 'balances' (open count minus closed count)
      that can be reached at that cell. For each step, if we encounter '(', the balance
      increases by 1; if ')', it decreases by 1. If at any point the balance becomes
      negative, that path is discarded.
    time_complexity: O(m * n * (m + n) / W) with bitset optimization, where W is the
      word size. We iterate through each of the $m \times n$ cells and perform bitwise
      shifts and OR operations of size roughly $(m+n)/2$. For $m, n = 100$, the total
      operations are roughly $10,000 \times 100 / 64$, which is well within limits.
    space_complexity: O(m * n * (m + n) / 8) bits to store the DP table. For a $100
      \times 100$ grid with bitsets of size 100, the memory footprint is approximately
      125 KB. Even with a 3D boolean array, the space is roughly $100 \times 100 \times
      100$ bytes, which is about 1 MB.
    elapsed_time: 1069.224942445755
    model: gemini-3-flash-preview
    generated_at: '2026-09-29 03:50:58 '
---

## Problem #2267:  Check if There Is a Valid Parentheses String Path

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Matrix, Bracket Sequences

## Problem Description

<p>A parentheses string is a <strong>non-empty</strong> string consisting only of <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>. It is <strong>valid</strong> if <strong>any</strong> of the following conditions is <strong>true</strong>:</p>

<ul>
	<li>It is <code>()</code>.</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid parentheses strings.</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid parentheses string.</li>
</ul>

<p>You are given an <code>m x n</code> matrix of parentheses <code>grid</code>. A <strong>valid parentheses string path</strong> in the grid is a path satisfying <strong>all</strong> of the following conditions:</p>

<ul>
	<li>The path starts from the upper left cell <code>(0, 0)</code>.</li>
	<li>The path ends at the bottom-right cell <code>(m - 1, n - 1)</code>.</li>
	<li>The path only ever moves <strong>down</strong> or <strong>right</strong>.</li>
	<li>The resulting parentheses string formed by the path is <strong>valid</strong>.</li>
</ul>

<p>Return <code>true</code> <em>if there exists a <strong>valid parentheses string path</strong> in the grid.</em> Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/15/example1drawio.png" style="width: 521px; height: 300px;" />
<pre>
<strong>Input:</strong> grid = [[&quot;(&quot;,&quot;(&quot;,&quot;(&quot;],[&quot;)&quot;,&quot;(&quot;,&quot;)&quot;],[&quot;(&quot;,&quot;(&quot;,&quot;)&quot;],[&quot;(&quot;,&quot;(&quot;,&quot;)&quot;]]
<strong>Output:</strong> true
<strong>Explanation:</strong> The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string &quot;()(())&quot;.
The second path shown results in the valid parentheses string &quot;((()))&quot;.
Note that there may be other valid parentheses string paths.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/15/example2drawio.png" style="width: 165px; height: 165px;" />
<pre>
<strong>Input:</strong> grid = [[&quot;)&quot;,&quot;)&quot;],[&quot;(&quot;,&quot;(&quot;]]
<strong>Output:</strong> false
<strong>Explanation:</strong> The two possible paths form the parentheses strings &quot;))(&quot; and &quot;)((&quot;. Since neither of them are valid parentheses strings, we return false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>grid[i][j]</code> is either <code>&#39;(&#39;</code> or <code>&#39;)&#39;</code>.</li>
</ul>


## Hints

1. What observations can you make about the number of open brackets and close brackets for any prefix of a valid bracket sequence?

2. The number of open brackets must always be greater than or equal to the number of close brackets.

3. Could you use dynamic programming?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks whether a path exists from the top-left to the bottom-right of an $m \times n$ grid that forms a valid parentheses string, moving only down or right. A parentheses string is valid if its total length is even, it has an equal number of open and closed brackets, and no prefix contains more closed brackets than open brackets. We utilize dynamic programming where the state at each cell $(r, c)$ tracks the possible cumulative 'balances' (open count minus closed count) that can be reached at that cell. For each step, if we encounter '(', the balance increases by 1; if ')', it decreases by 1. If at any point the balance becomes negative, that path is discarded.

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
#include <bitset>

using namespace std;

class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        if ((m + n) % 2 == 0 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') {
            return false;
        }

        vector<vector<bitset<101>>> dp(m, vector<bitset<101>>(n));
        dp[0][0][1] = 1;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0) continue;

                bitset<101> prev;
                if (i > 0) prev |= dp[i - 1][j];
                if (j > 0) prev |= dp[i][j - 1];

                if (grid[i][j] == '(') {
                    dp[i][j] = prev << 1;
                } else {
                    dp[i][j] = prev >> 1;
                }
            }
        }

        return dp[m - 1][n - 1][0];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean hasValidPath(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        if ((m + n) % 2 == 0 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') {
            return false;
        }

        int maxBal = (m + n) / 2;
        boolean[][][] dp = new boolean[m][n][maxBal + 1];

        dp[0][0][1] = true;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k <= maxBal; k++) {
                    if (!dp[i][j][k]) continue;

                    // Down move
                    if (i + 1 < m) {
                        int nk = k + (grid[i + 1][j] == '(' ? 1 : -1);
                        if (nk >= 0 && nk <= maxBal) {
                            dp[i + 1][j][nk] = true;
                        }
                    }

                    // Right move
                    if (j + 1 < n) {
                        int nk = k + (grid[i][j + 1] == '(' ? 1 : -1);
                        if (nk >= 0 && nk <= maxBal) {
                            dp[i][j + 1][nk] = true;
                        }
                    }
                }
            }
        }

        return dp[m - 1][n - 1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])

        # Path length is m + n - 1. Valid parentheses strings have even length.
        # Therefore m + n - 1 must be even, so m + n must be odd.
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # dp[j] stores the reachable balances at cell (current_row, j) as a bitmask.
        # Bit k is set if balance k is reachable.
        dp = [0] * n

        # Initial state: after processing grid[0][0], which must be '(', balance is 1.
        dp[0] = 1 << 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                prev_mask = 0
                if i > 0:
                    prev_mask |= dp[j]
                if j > 0:
                    prev_mask |= dp[j - 1]

                if grid[i][j] == '(':
                    dp[j] = prev_mask << 1
                else:
                    # Right shift handles the balance >= 0 constraint automatically,
                    # as shifting bit 0 right results in it disappearing.
                    dp[j] = prev_mask >> 1

        return bool(dp[n - 1] & 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        # A valid parentheses string path must have an even length (m + n - 1).
        # So m + n must be odd.
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # dp[r][c] is a bitmask where the i-th bit is set if a balance of i is possible at cell (r, c).
        # A balance is the number of '(' minus the number of ')'.
        dp = [[0] * n for _ in range(m)]

        # Initial state: after including grid[0][0], the balance is 1.
        dp[0][0] = 1 << 1

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0: continue

                prev_masks = 0
                if r > 0:
                    prev_masks |= dp[r - 1][c]
                if c > 0:
                    prev_masks |= dp[r][c - 1]

                if grid[r][c] == '(':
                    # Increment balance for all possible states
                    dp[r][c] = prev_masks << 1
                else:
                    # Decrement balance for all possible states. Right-shift effectively
                    # removes states with balance 0 (which would become -1).
                    dp[r][c] = prev_masks >> 1

                # Pruning: at current cell (r, c), the balance cannot exceed the remaining steps.
                rem_steps = (m - 1 - r) + (n - 1 - c)
                mask = (1 << (rem_steps + 1)) - 1
                dp[r][c] &= mask

        # Result: can we reach the end with a balance of 0 (the 0-th bit)?
        return bool(dp[m - 1][n - 1] & 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool hasValidPath(char** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];

    if ((m + n) % 2 == 0 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') {
        return false;
    }

    const int max_b = 101;
    bool* dp = (bool*)calloc(m * n * max_b, sizeof(bool));
    if (!dp) return false;

    // dp[(r * n + c) * max_b + b] represents if balance b is possible at (r, c)
    dp[(0 * n + 0) * max_b + 1] = true;

    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            int rem = (m - 1 - r) + (n - 1 - c);
            for (int b = 0; b < max_b; b++) {
                if (!dp[(r * n + c) * max_b + b]) continue;

                // Pruning
                if (b > rem) continue;

                // Move Down
                if (r + 1 < m) {
                    int nb = b + (grid[r + 1][c] == '(' ? 1 : -1);
                    if (nb >= 0 && nb < max_b) {
                        dp[((r + 1) * n + c) * max_b + nb] = true;
                    }
                }

                // Move Right
                if (c + 1 < n) {
                    int nb = b + (grid[r][c + 1] == '(' ? 1 : -1);
                    if (nb >= 0 && nb < max_b) {
                        dp[(r * n + (c + 1)) * max_b + nb] = true;
                    }
                }
            }
        }
    }

    bool result = dp[((m - 1) * n + (n - 1)) * max_b + 0];
    free(dp);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool HasValidPath(char[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;

        if ((m + n) % 2 == 0 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') {
            return false;
        }

        const int max_b = 101;
        bool[,,] dp = new bool[m, n, max_b];

        dp[0, 0, 1] = true;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                int rem = (m - 1 - r) + (n - 1 - c);
                for (int b = 0; b < max_b; b++) {
                    if (!dp[r, c, b]) continue;

                    if (b > rem) continue;

                    // Move Down
                    if (r + 1 < m) {
                        int nb = b + (grid[r + 1][c] == '(' ? 1 : -1);
                        if (nb >= 0 && nb < max_b) {
                            dp[r + 1, c, nb] = true;
                        }
                    }

                    // Move Right
                    if (c + 1 < n) {
                        int nb = b + (grid[r][c + 1] == '(' ? 1 : -1);
                        if (nb >= 0 && nb < max_b) {
                            dp[r, c + 1, nb] = true;
                        }
                    }
                }
            }
        }

        return dp[m - 1, n - 1, 0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var hasValidPath = function(grid) {
    const m = grid.length, n = grid[0].length;

    if ((m + n) % 2 === 0 || grid[0][0] === ')' || grid[m - 1][n - 1] === '(') {
        return false;
    }

    // Using BigInt bitmasks to handle balances up to 100 efficiently.
    let dp = Array.from({ length: m }, () => new BigUint64Array(n).fill(0n));
    let dpTable = Array.from({ length: m }, () => Array(n).fill(0n));

    dpTable[0][0] = 1n << 1n;

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (r === 0 && c === 0) continue;

            let prevMasks = 0n;
            if (r > 0) prevMasks |= dpTable[r - 1][c];
            if (c > 0) prevMasks |= dpTable[r][c - 1];

            if (grid[r][c] === '(') {
                dpTable[r][c] = prevMasks << 1n;
            } else {
                dpTable[r][c] = prevMasks >> 1n;
            }

            // Pruning balance values that are impossible to close.
            let rem = (m - 1 - r) + (n - 1 - c);
            let mask = (1n << BigInt(rem + 1)) - 1n;
            dpTable[r][c] &= mask;
        }
    }

    return (dpTable[m - 1][n - 1] & 1n) === 1n;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function hasValidPath(grid: string[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;
    if ((m + n - 1) % 2 !== 0 || grid[0][0] === ')' || grid[m - 1][n - 1] === '(') {
        return false;
    }

    const dp: bigint[] = new Array(n).fill(0n);
    dp[0] = 1n << 1n;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;

            let combined = 0n;
            if (i > 0) combined |= dp[j];
            if (j > 0) combined |= dp[j - 1];

            if (grid[i][j] === '(') {
                dp[j] = combined << 1n;
            } else {
                dp[j] = combined >> 1n;
            }
        }
    }

    return (dp[n - 1] & 1n) === 1n;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[][] $grid
     * @return Boolean
     */
    function hasValidPath($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        if (($m + $n - 1) % 2 !== 0 || $grid[0][0] === ')' || $grid[$m - 1][$n - 1] === '(') {
            return false;
        }

        $maxK = (int)(($m + $n) / 2);
        $dp = array_fill(0, $n, array_fill(0, $maxK + 1, false));
        $dp[0][1] = true;

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i === 0 && $j === 0) continue;

                $char = $grid[$i][$j];
                $current = array_fill(0, $maxK + 1, false);
                $isOpening = ($char === '(');

                for ($k = 0; $k <= $maxK; $k++) {
                    if (($i > 0 && $dp[$j][$k]) || ($j > 0 && $dp[$j - 1][$k])) {
                        if ($isOpening) {
                            if ($k + 1 <= $maxK) {
                                $current[$k + 1] = true;
                            }
                        } else {
                            if ($k - 1 >= 0) {
                                $current[$k - 1] = true;
                            }
                        }
                    }
                }
                $dp[$j] = $current;
            }
        }

        return $dp[$n - 1][0];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func hasValidPath(_ grid: [[Character]]) -> Bool {
        let m = grid.count
        let n = grid[0].count
        if (m + n - 1) % 2 != 0 || grid[0][0] == ")" || grid[m - 1][n - 1] == "(" {
            return false
        }

        let maxK = (m + n) / 2
        var dp = Array(repeating: Array(repeating: false, count: maxK + 1), count: n)
        dp[0][1] = true

        for i in 0..<m {
            for j in 0..<n {
                if i == 0 && j == 0 { continue }

                let isOpening = grid[i][j] == "("
                var current = Array(repeating: false, count: maxK + 1)

                for k in 0...maxK {
                    if (i > 0 && dp[j][k]) || (j > 0 && dp[j - 1][k]) {
                        if isOpening {
                            if k + 1 <= maxK {
                                current[k + 1] = true
                            }
                        } else {
                            if k - 1 >= 0 {
                                current[k - 1] = true
                            }
                        }
                    }
                }
                dp[j] = current
            }
        }

        return dp[n - 1][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.BitSet

class Solution {
    fun hasValidPath(grid: Array<CharArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        if ((m + n - 1) % 2 != 0 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(') {
            return false
        }

        val maxK = (m + n) / 2
        val dp = Array(n) { BitSet(maxK + 1) }
        dp[0].set(1)

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i == 0 && j == 0) continue

                val combined = BitSet(maxK + 1)
                if (i > 0) combined.or(dp[j])
                if (j > 0) combined.or(dp[j - 1])

                val current = BitSet(maxK + 1)
                if (grid[i][j] == '(') {
                    for (k in 0 until maxK) {
                        if (combined.get(k)) current.set(k + 1)
                    }
                } else {
                    for (k in 1..maxK) {
                        if (combined.get(k)) current.set(k - 1)
                    }
                }
                dp[j] = current
            }
        }

        return dp[n - 1].get(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool hasValidPath(List<List<String>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    if ((m + n - 1) % 2 != 0) return false;
    if (grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false;

    List<BigInt> dp = List.filled(n, BigInt.zero);

    if (grid[0][0] == '(') {
      dp[0] = BigInt.one << 1;
    } else {
      return false;
    }

    for (int c = 1; c < n; c++) {
      if (grid[0][c] == '(') {
        dp[c] = dp[c - 1] << 1;
      } else {
        dp[c] = dp[c - 1] >> 1;
      }
    }

    for (int r = 1; r < m; r++) {
      if (grid[r][0] == '(') {
        dp[0] = dp[0] << 1;
      } else {
        dp[0] = dp[0] >> 1;
      }
      for (int c = 1; c < n; c++) {
        BigInt prev = dp[c - 1] | dp[c];
        if (grid[r][c] == '(') {
          dp[c] = prev << 1;
        } else {
          dp[c] = prev >> 1;
        }
      }
    }

    return (dp[n - 1] & BigInt.one) != BigInt.zero;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "math/big"

func hasValidPath(grid [][]byte) bool {
    m := len(grid)
    n := len(grid[0])
    if (m+n-1)%2 != 0 || grid[0][0] == ')' || grid[m-1][n-1] == '(' {
        return false
    }

    dp := make([]*big.Int, n)
    for i := range dp {
        dp[i] = big.NewInt(0)
    }

    dp[0].SetUint64(2)
    for c := 1; c < n; c++ {
        if grid[0][c] == '(' {
            dp[c].Lsh(dp[c-1], 1)
        } else {
            dp[c].Rsh(dp[c-1], 1)
        }
    }

    prev := new(big.Int)
    for r := 1; r < m; r++ {
        if grid[r][0] == '(' {
            dp[0].Lsh(dp[0], 1)
        } else {
            dp[0].Rsh(dp[0], 1)
        }
        for c := 1; c < n; c++ {
            prev.Or(dp[c-1], dp[c])
            if grid[r][c] == '(' {
                dp[c].Lsh(prev, 1)
            } else {
                dp[c].Rsh(prev, 1)
            }
        }
    }

    return dp[n-1].Bit(0) == 1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Character[][]} grid
# @return {Boolean}
def has_valid_path(grid)
  m = grid.length
  n = grid[0].length
  return false if (m + n - 1) % 2 != 0
  return false if grid[0][0] == ')' || grid[m - 1][n - 1] == '('

  dp = Array.new(n, 0)
  dp[0] = 1 << 1

  (1...n).each do |c|
    if grid[0][c] == '('
      dp[c] = dp[c - 1] << 1
    else
      dp[c] = dp[c - 1] >> 1
    end
  end

  (1...m).each do |r|
    if grid[r][0] == '('
      dp[0] <<= 1
    else
      dp[0] >>= 1
    end

    (1...n).each do |c|
      prev = dp[c - 1] | dp[c]
      if grid[r][c] == '('
        dp[c] = prev << 1
      else
        dp[c] = prev >> 1
      end
    end
  end

  (dp[n - 1] & 1) != 0
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.math.BigInt

object Solution {
    def hasValidPath(grid: Array[Array[Char]]): Boolean = {
        val m = grid.length
        val n = grid(0).length
        if ((m + n - 1) % 2 != 0) return false
        if (grid(0)(0) == ')' || grid(m - 1)(n - 1) == '(') return false

        val dp = Array.fill(n)(BigInt(0))

        dp(0) = BigInt(1) << 1
        for (c <- 1 until n) {
            if (grid(0)(c) == '(') dp(c) = dp(c - 1) << 1
            else dp(c) = dp(c - 1) >> 1
        }

        for (r <- 1 until m) {
            if (grid(r)(0) == '(') dp(0) = dp(0) << 1
            else dp(0) = dp(0) >> 1
            for (c <- 1 until n) {
                val prevBalances = dp(c - 1) | dp(c)
                if (grid(r)(c) == '(') dp(c) = prevBalances << 1
                else dp(c) = prevBalances >> 1
            }
        }

        dp(n - 1).testBit(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn has_valid_path(grid: Vec<Vec<char>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        let l = m + n - 1;
        if l % 2 != 0 || grid[0][0] == ')' || grid[m - 1][n - 1] == '(' {
            return false;
        }

        let mut dp = vec![vec![[false; 101]; n]; m];
        dp[0][0][1] = true;

        for r in 0..m {
            for c in 0..n {
                for k in 0..101 {
                    if !dp[r][c][k] { continue; }

                    let rem_steps = m + n - r - c - 2;

                    if c + 1 < n {
                        let nk = if grid[r][c + 1] == '(' { k + 1 } else { k as i32 - 1 };
                        if nk >= 0 && nk <= 100 && (nk as usize) <= rem_steps {
                            dp[r][c + 1][nk as usize] = true;
                        }
                    }

                    if r + 1 < m {
                        let nk = if grid[r + 1][c] == '(' { k + 1 } else { k as i32 - 1 };
                        if nk >= 0 && nk <= 100 && (nk as usize) <= rem_steps {
                            dp[r + 1][c][nk as usize] = true;
                        }
                    }
                }
            }
        }
        dp[m - 1][n - 1][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (has-valid-path grid)
  (-> (listof (listof char?)) boolean?)
  (let* ([m (length grid)]
         [n (length (car grid))]
         [L (+ m n -1)])
    (if (or (odd? L) (char=? (caar grid) #\)))
        #f
        (let* ([grid-vec (list->vector (map list->vector grid))]
               [dp (make-vector (* m n 101) #f)])
          (define (get-idx r c k) (+ (* r n 101) (* c 101) k))
          (vector-set! dp (get-idx 0 0 1) #t)
          (for ([r (in-range m)])
            (for ([c (in-range n)])
              (for ([k (in-range 101)])
                (when (vector-ref dp (get-idx r c k))
                  (let ([rem-steps (- (+ m n) r c 2)])
                    (when (< (+ c 1) n)
                      (let* ([ch (vector-ref (vector-ref grid-vec r) (+ c 1))]
                             [nk (if (char=? ch #\() (+ k 1) (- k 1))])
                        (when (and (>= nk 0) (<= nk 100) (<= nk rem-steps))
                          (vector-set! dp (get-idx r (+ c 1) nk) #t))))
                    (when (< (+ r 1) m)
                      (let* ([ch (vector-ref (vector-ref grid-vec (+ r 1)) c)]
                             [nk (if (char=? ch #\() (+ k 1) (- k 1))])
                        (when (and (>= nk 0) (<= nk 100) (<= nk rem-steps))
                          (vector-set! dp (get-idx (+ r 1) c nk) #t)))))))))
          (vector-ref dp (get-idx (- m 1) (- n 1) 0))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec has_valid_path(Grid :: [[char()]]) -> boolean().
has_valid_path(Grid) ->
  M = length(Grid),
  N = length(hd(Grid)),
  L = M + N - 1,
  case L rem 2 of
    1 -> false;
    0 ->
      case hd(hd(Grid)) of
        $) -> false;
        $( ->
          GridVec = list_to_tuple([list_to_tuple(R) || R <- Grid]),
          Cache = ets:new(memo, [set]),
          Result = solve(0, 0, 0, GridVec, M, N, Cache),
          ets:delete(Cache),
          Result
      end
  end.

solve(R, C, K, GridVec, M, N, Cache) ->
  case ets:lookup(Cache, {R, C, K}) of
    [{_, Val}] -> Val;
    [] ->
      Char = element(C + 1, element(R + 1, GridVec)),
      NewK = if Char == $( -> K + 1; true -> K - 1 end,
      Res = if
        NewK < 0 -> false;
        NewK > (M - 1 - R) + (N - 1 - C) -> false;
        R == M - 1, C == N - 1 -> NewK == 0;
        true ->
          (R + 1 < M andalso solve(R + 1, C, NewK, GridVec, M, N, Cache))
          orelse (C + 1 < N andalso solve(R, C + 1, NewK, GridVec, M, N, Cache))
      end,
      ets:insert(Cache, {{R, C, K}, Res}),
      Res
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec has_valid_path(grid :: [[char]]) :: boolean
  def has_valid_path(grid) do
    m = length(grid)
    n = length(hd(grid))
    if rem(m + n, 2) == 0 do
      false
    else
      grid_tuple = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
      cache = :ets.new(:memo, [:set])
      result = solve(0, 0, 0, grid_tuple, m, n, cache)
      :ets.delete(cache)
      result
    end
  end

  defp solve(r, c, k, grid_tuple, m, n, cache) do
    case :ets.lookup(cache, {r, c, k}) do
      [{_, val}] -> val
      [] ->
        char = elem(elem(grid_tuple, r), c)
        new_k = if char == ?(, do: k + 1, else: k - 1
        res = cond do
          new_k < 0 -> false
          new_k > (m - 1 - r) + (n - 1 - c) -> false
          r == m - 1 and c == n - 1 -> new_k == 0
          true ->
            (r + 1 < m && solve(r + 1, c, new_k, grid_tuple, m, n, cache)) ||
            (c + 1 < n && solve(r, c + 1, new_k, grid_tuple, m, n, cache))
        end
        :ets.insert(cache, {{r, c, k}, res})
        res
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n * (m + n) / W) with bitset optimization, where W is the word size. We iterate through each of the $m \times n$ cells and perform bitwise shifts and OR operations of size roughly $(m+n)/2$. For $m, n = 100$, the total operations are roughly $10,000 \times 100 / 64$, which is well within limits.
- **Space Complexity:** O(m * n * (m + n) / 8) bits to store the DP table. For a $100 \times 100$ grid with bitsets of size 100, the memory footprint is approximately 125 KB. Even with a 3D boolean array, the space is roughly $100 \times 100 \times 100$ bytes, which is about 1 MB.
