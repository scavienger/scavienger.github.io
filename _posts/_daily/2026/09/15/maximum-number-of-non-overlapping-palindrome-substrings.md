---
layout: post
title: "Maximum Number of Non-overlapping Palindrome Substrings"
date: 2026-09-15 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Two Pointers", "String", "Dynamic Programming", "Greedy"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxPalindromes(string s, int k) {\n \
        \       int n = s.length();\n        if (k == 1) return n;\n        vector<int>\
        \ dp(n + 1, 0);\n        for (int i = 1; i <= n; ++i) {\n            dp[i] =\
        \ dp[i - 1];\n            if (i >= k) {\n                if (isPal(s, i - k,\
        \ i - 1)) {\n                    dp[i] = max(dp[i], dp[i - k] + 1);\n      \
        \          }\n            }\n            if (i >= k + 1) {\n               \
        \ if (isPal(s, i - k - 1, i - 1)) {\n                    dp[i] = max(dp[i],\
        \ dp[i - k - 1] + 1);\n                }\n            }\n        }\n       \
        \ return dp[n];\n    }\n\nprivate:\n    bool isPal(const string& s, int l, int\
        \ r) {\n        while (l < r) {\n            if (s[l++] != s[r--]) return false;\n\
        \        }\n        return true;\n    }\n};"
      java: "class Solution {\n    public int maxPalindromes(String s, int k) {\n  \
        \      int n = s.length();\n        if (k == 1) return n;\n        int[] dp\
        \ = new int[n + 1];\n        for (int i = 1; i <= n; i++) {\n            dp[i]\
        \ = dp[i - 1];\n            if (i >= k) {\n                if (isPal(s, i -\
        \ k, i - 1)) {\n                    dp[i] = Math.max(dp[i], dp[i - k] + 1);\n\
        \                }\n            }\n            if (i >= k + 1) {\n         \
        \       if (isPal(s, i - k - 1, i - 1)) {\n                    dp[i] = Math.max(dp[i],\
        \ dp[i - k - 1] + 1);\n                }\n            }\n        }\n       \
        \ return dp[n];\n    }\n\n    private boolean isPal(String s, int l, int r)\
        \ {\n        while (l < r) {\n            if (s.charAt(l++) != s.charAt(r--))\
        \ return false;\n        }\n        return true;\n    }\n}"
      python: "class Solution(object):\n    def maxPalindromes(self, s, k):\n      \
        \  \"\"\"\n        :type s: str\n        :type k: int\n        :rtype: int\n\
        \        \"\"\"\n        n = len(s)\n        if k == 1:\n            return\
        \ n\n\n        dp = [0] * (n + 1)\n        for i in range(1, n + 1):\n     \
        \       dp[i] = dp[i - 1]\n            if i >= k:\n                if s[i -\
        \ k] == s[i - 1]:\n                    sub = s[i - k:i]\n                  \
        \  if sub == sub[::-1]:\n                        dp[i] = max(dp[i], dp[i - k]\
        \ + 1)\n            if i >= k + 1:\n                if s[i - k - 1] == s[i -\
        \ 1]:\n                    sub = s[i - k - 1:i]\n                    if sub\
        \ == sub[::-1]:\n                        dp[i] = max(dp[i], dp[i - k - 1] +\
        \ 1)\n        return dp[n]"
      python3: "class Solution:\n    def maxPalindromes(self, s: str, k: int) -> int:\n\
        \        n = len(s)\n        ans = 0\n        last_end = -1\n        for i in\
        \ range(n):\n            l1 = i - k + 1\n            if l1 > last_end and l1\
        \ >= 0:\n                sub = s[l1 : i + 1]\n                if sub == sub[::-1]:\n\
        \                    ans += 1\n                    last_end = i\n          \
        \          continue\n            l2 = i - k\n            if l2 > last_end and\
        \ l2 >= 0:\n                sub = s[l2 : i + 1]\n                if sub == sub[::-1]:\n\
        \                    ans += 1\n                    last_end = i\n        return\
        \ ans"
      c: "#include <string.h>\n\nint maxPalindromes(char* s, int k) {\n    int n = strlen(s);\n\
        \    int ans = 0;\n    int last_end = -1;\n    for (int i = 0; i < n; i++) {\n\
        \        int l1 = i - k + 1;\n        if (l1 > last_end && l1 >= 0) {\n    \
        \        int l = l1, r = i;\n            int is_pal = 1;\n            while\
        \ (l < r) {\n                if (s[l] != s[r]) {\n                    is_pal\
        \ = 0;\n                    break;\n                }\n                l++;\n\
        \                r--;\n            }\n            if (is_pal) {\n          \
        \      ans++;\n                last_end = i;\n                continue;\n  \
        \          }\n        }\n        int l2 = i - k;\n        if (l2 > last_end\
        \ && l2 >= 0) {\n            int l = l2, r = i;\n            int is_pal = 1;\n\
        \            while (l < r) {\n                if (s[l] != s[r]) {\n        \
        \            is_pal = 0;\n                    break;\n                }\n  \
        \              l++;\n                r--;\n            }\n            if (is_pal)\
        \ {\n                ans++;\n                last_end = i;\n            }\n\
        \        }\n    }\n    return ans;\n}"
      csharp: "public class Solution {\n    public int MaxPalindromes(string s, int\
        \ k) {\n        int n = s.Length;\n        int ans = 0;\n        int lastEnd\
        \ = -1;\n        for (int i = 0; i < n; i++) {\n            int l1 = i - k +\
        \ 1;\n            if (l1 > lastEnd && l1 >= 0) {\n                int l = l1,\
        \ r = i;\n                bool isPal = true;\n                while (l < r)\
        \ {\n                    if (s[l] != s[r]) {\n                        isPal\
        \ = false;\n                        break;\n                    }\n        \
        \            l++;\n                    r--;\n                }\n           \
        \     if (isPal) {\n                    ans++;\n                    lastEnd\
        \ = i;\n                    continue;\n                }\n            }\n  \
        \          int l2 = i - k;\n            if (l2 > lastEnd && l2 >= 0) {\n   \
        \             int l = l2, r = i;\n                bool isPal = true;\n     \
        \           while (l < r) {\n                    if (s[l] != s[r]) {\n     \
        \                   isPal = false;\n                        break;\n       \
        \             }\n                    l++;\n                    r--;\n      \
        \          }\n                if (isPal) {\n                    ans++;\n   \
        \                 lastEnd = i;\n                }\n            }\n        }\n\
        \        return ans;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {number} k\n * @return {number}\n\
        \ */\nvar maxPalindromes = function(s, k) {\n    let n = s.length;\n    let\
        \ ans = 0;\n    let lastEnd = -1;\n    for (let i = 0; i < n; i++) {\n     \
        \   let l1 = i - k + 1;\n        if (l1 > lastEnd && l1 >= 0) {\n          \
        \  let l = l1, r = i;\n            let isPal = true;\n            while (l <\
        \ r) {\n                if (s[l] !== s[r]) {\n                    isPal = false;\n\
        \                    break;\n                }\n                l++;\n     \
        \           r--;\n            }\n            if (isPal) {\n                ans++;\n\
        \                lastEnd = i;\n                continue;\n            }\n  \
        \      }\n        let l2 = i - k;\n        if (l2 > lastEnd && l2 >= 0) {\n\
        \            let l = l2, r = i;\n            let isPal = true;\n           \
        \ while (l < r) {\n                if (s[l] !== s[r]) {\n                  \
        \  isPal = false;\n                    break;\n                }\n         \
        \       l++;\n                r--;\n            }\n            if (isPal) {\n\
        \                ans++;\n                lastEnd = i;\n            }\n     \
        \   }\n    }\n    return ans;\n};"
      typescript: "function maxPalindromes(s: string, k: number): number {\n    const\
        \ n = s.length;\n    const dp = new Array(n + 1).fill(0);\n\n    const isPal\
        \ = (l: number, r: number): boolean => {\n        while (l < r) {\n        \
        \    if (s[l] !== s[r]) return false;\n            l++;\n            r--;\n\
        \        }\n        return true;\n    };\n\n    for (let i = 1; i <= n; i++)\
        \ {\n        dp[i] = dp[i - 1];\n        if (i >= k && isPal(i - k, i - 1))\
        \ {\n            dp[i] = Math.max(dp[i], dp[i - k] + 1);\n        }\n      \
        \  if (i >= k + 1 && isPal(i - k - 1, i - 1)) {\n            dp[i] = Math.max(dp[i],\
        \ dp[i - k - 1] + 1);\n        }\n    }\n    return dp[n];\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param Integer\
        \ $k\n     * @return Integer\n     */\n    function maxPalindromes($s, $k) {\n\
        \        $n = strlen($s);\n        $dp = array_fill(0, $n + 1, 0);\n       \
        \ for ($i = 1; $i <= $n; $i++) {\n            $dp[$i] = $dp[$i - 1];\n     \
        \       if ($i >= $k && $this->isPal($s, $i - $k, $i - 1)) {\n             \
        \   $dp[$i] = max($dp[$i], $dp[$i - $k] + 1);\n            }\n            if\
        \ ($i >= $k + 1 && $this->isPal($s, $i - $k - 1, $i - 1)) {\n              \
        \  $dp[$i] = max($dp[$i], $dp[$i - $k - 1] + 1);\n            }\n        }\n\
        \        return $dp[$n];\n    }\n\n    private function isPal($s, $l, $r) {\n\
        \        while ($l < $r) {\n            if ($s[$l] !== $s[$r]) {\n         \
        \       return false;\n            }\n            $l++;\n            $r--;\n\
        \        }\n        return true;\n    }\n}"
      swift: "class Solution {\n    func maxPalindromes(_ s: String, _ k: Int) -> Int\
        \ {\n        let chars = Array(s)\n        let n = chars.count\n        var\
        \ dp = [Int](repeating: 0, count: n + 1)\n\n        for i in 1...n {\n     \
        \       dp[i] = dp[i - 1]\n            if i >= k && isPal(chars, i - k, i -\
        \ 1) {\n                dp[i] = max(dp[i], dp[i - k] + 1)\n            }\n \
        \           if i >= k + 1 && isPal(chars, i - k - 1, i - 1) {\n            \
        \    dp[i] = max(dp[i], dp[i - k - 1] + 1)\n            }\n        }\n     \
        \   return dp[n]\n    }\n\n    private func isPal(_ chars: [Character], _ l:\
        \ Int, _ r: Int) -> Bool {\n        var left = l\n        var right = r\n  \
        \      while left < right {\n            if chars[left] != chars[right] {\n\
        \                return false\n            }\n            left += 1\n      \
        \      right -= 1\n        }\n        return true\n    }\n}"
      kotlin: "class Solution {\n    fun maxPalindromes(s: String, k: Int): Int {\n\
        \        val n = s.length\n        val dp = IntArray(n + 1)\n\n        for (i\
        \ in 1..n) {\n            dp[i] = dp[i - 1]\n            if (i >= k && isPal(s,\
        \ i - k, i - 1)) {\n                dp[i] = maxOf(dp[i], dp[i - k] + 1)\n  \
        \          }\n            if (i >= k + 1 && isPal(s, i - k - 1, i - 1)) {\n\
        \                dp[i] = maxOf(dp[i], dp[i - (k + 1)] + 1)\n            }\n\
        \        }\n        return dp[n]\n    }\n\n    private fun isPal(s: String,\
        \ l: Int, r: Int): Boolean {\n        var left = l\n        var right = r\n\
        \        while (left < right) {\n            if (s[left] != s[right]) return\
        \ false\n            left++\n            right--\n        }\n        return\
        \ true\n    }\n}"
      dart: "class Solution {\n  int maxPalindromes(String s, int k) {\n    int n =\
        \ s.length;\n    List<int> dp = List.filled(n + 1, 0);\n\n    for (int i = 0;\
        \ i < n; i++) {\n      if (dp[i] > dp[i + 1]) {\n        dp[i + 1] = dp[i];\n\
        \      }\n\n      // Check for palindrome of length k ending at i\n      if\
        \ (i >= k - 1) {\n        bool isPal = true;\n        int left = i - k + 1;\n\
        \        int right = i;\n        while (left < right) {\n          if (s[left]\
        \ != s[right]) {\n            isPal = false;\n            break;\n         \
        \ }\n          left++;\n          right--;\n        }\n        if (isPal) {\n\
        \          int res = dp[i - k + 1] + 1;\n          if (res > dp[i + 1]) {\n\
        \            dp[i + 1] = res;\n          }\n        }\n      }\n\n      // Check\
        \ for palindrome of length k + 1 ending at i\n      if (i >= k) {\n        bool\
        \ isPal = true;\n        int left = i - k;\n        int right = i;\n       \
        \ while (left < right) {\n          if (s[left] != s[right]) {\n           \
        \ isPal = false;\n            break;\n          }\n          left++;\n     \
        \     right--;\n        }\n        if (isPal) {\n          int res = dp[i -\
        \ k] + 1;\n          if (res > dp[i + 1]) {\n            dp[i + 1] = res;\n\
        \          }\n        }\n      }\n    }\n\n    return dp[n];\n  }\n}"
      go: "func maxPalindromes(s string, k int) int {\n\tn := len(s)\n\tdp := make([]int,\
        \ n+1)\n\n\tfor i := 0; i < n; i++ {\n\t\tif dp[i] > dp[i+1] {\n\t\t\tdp[i+1]\
        \ = dp[i]\n\t\t}\n\n\t\t// Check for palindrome of length k ending at i\n\t\t\
        if i >= k-1 {\n\t\t\tisPal := true\n\t\t\tleft, right := i-k+1, i\n\t\t\tfor\
        \ left < right {\n\t\t\t\tif s[left] != s[right] {\n\t\t\t\t\tisPal = false\n\
        \t\t\t\t\tbreak\n\t\t\t\t}\n\t\t\t\tleft++\n\t\t\t\tright--\n\t\t\t}\n\t\t\t\
        if isPal {\n\t\t\t\tres := dp[i-k+1] + 1\n\t\t\t\tif res > dp[i+1] {\n\t\t\t\
        \t\tdp[i+1] = res\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\n\t\t// Check for palindrome\
        \ of length k + 1 ending at i\n\t\tif i >= k {\n\t\t\tisPal := true\n\t\t\t\
        left, right := i-k, i\n\t\t\tfor left < right {\n\t\t\t\tif s[left] != s[right]\
        \ {\n\t\t\t\t\tisPal = false\n\t\t\t\t\tbreak\n\t\t\t\t}\n\t\t\t\tleft++\n\t\
        \t\t\tright--\n\t\t\t}\n\t\t\tif isPal {\n\t\t\t\tres := dp[i-k] + 1\n\t\t\t\
        \tif res > dp[i+1] {\n\t\t\t\t\tdp[i+1] = res\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\
        }\n\n\treturn dp[n]\n}"
      ruby: "# @param {String} s\n# @param {Integer} k\n# @return {Integer}\ndef max_palindromes(s,\
        \ k)\n  n = s.length\n  dp = Array.new(n + 1, 0)\n\n  (0...n).each do |i|\n\
        \    dp[i + 1] = dp[i] if dp[i] > dp[i + 1]\n\n    # Check for palindrome of\
        \ length k ending at index i\n    if i >= k - 1\n      is_pal = true\n     \
        \ left = i - k + 1\n      right = i\n      while left < right\n        if s[left]\
        \ != s[right]\n          is_pal = false\n          break\n        end\n    \
        \    left += 1\n        right -= 1\n      end\n      if is_pal\n        res\
        \ = dp[i - k + 1] + 1\n        dp[i + 1] = res if res > dp[i + 1]\n      end\n\
        \    end\n\n    # Check for palindrome of length k + 1 ending at index i\n \
        \   if i >= k\n      is_pal = true\n      left = i - k\n      right = i\n  \
        \    while left < right\n        if s[left] != s[right]\n          is_pal =\
        \ false\n          break\n        end\n        left += 1\n        right -= 1\n\
        \      end\n      if is_pal\n        res = dp[i - k] + 1\n        dp[i + 1]\
        \ = res if res > dp[i + 1]\n      end\n    end\n  end\n\n  dp[n]\nend"
      scala: "object Solution {\n  def maxPalindromes(s: String, k: Int): Int = {\n\
        \    val n = s.length\n    val dp = new Array[Int](n + 1)\n\n    for (i <- 0\
        \ until n) {\n      if (dp(i) > dp(i + 1)) {\n        dp(i + 1) = dp(i)\n  \
        \    }\n\n      // Check for palindrome of length k ending at i\n      if (i\
        \ >= k - 1) {\n        var isPal = true\n        var left = i - k + 1\n    \
        \    var right = i\n        while (left < right && isPal) {\n          if (s(left)\
        \ != s(right)) {\n            isPal = false\n          } else {\n          \
        \  left += 1\n            right -= 1\n          }\n        }\n        if (isPal)\
        \ {\n          val res = dp(i - k + 1) + 1\n          if (res > dp(i + 1)) {\n\
        \            dp(i + 1) = res\n          }\n        }\n      }\n\n      // Check\
        \ for palindrome of length k + 1 ending at i\n      if (i >= k) {\n        var\
        \ isPal = true\n        var left = i - k\n        var right = i\n        while\
        \ (left < right && isPal) {\n          if (s(left) != s(right)) {\n        \
        \    isPal = false\n          } else {\n            left += 1\n            right\
        \ -= 1\n          }\n        }\n        if (isPal) {\n          val res = dp(i\
        \ - k) + 1\n          if (res > dp(i + 1)) {\n            dp(i + 1) = res\n\
        \          }\n        }\n      }\n    }\n\n    dp(n)\n  }\n}"
      rust: "impl Solution {\n    pub fn max_palindromes(s: String, k: i32) -> i32 {\n\
        \        let n = s.len();\n        let k = k as usize;\n        let s_bytes\
        \ = s.as_bytes();\n        let mut dp = vec![0; n + 1];\n\n        for i in\
        \ 1..=n {\n            dp[i] = dp[i - 1];\n\n            if i >= k && Self::is_palindrome(s_bytes,\
        \ i - k, i - 1) {\n                dp[i] = dp[i].max(dp[i - k] + 1);\n     \
        \       }\n\n            if i >= k + 1 && Self::is_palindrome(s_bytes, i - (k\
        \ + 1), i - 1) {\n                dp[i] = dp[i].max(dp[i - (k + 1)] + 1);\n\
        \            }\n        }\n        dp[n]\n    }\n\n    fn is_palindrome(s: &[u8],\
        \ mut l: usize, mut r: usize) -> bool {\n        while l < r {\n           \
        \ if s[l] != s[r] {\n                return false;\n            }\n        \
        \    l += 1;\n            r -= 1;\n        }\n        true\n    }\n}"
      racket: "(define/contract (max-palindromes s k)\n  (-> string? exact-integer?\
        \ exact-integer?)\n  (let* ([n (string-length s)]\n         [dp (make-vector\
        \ (+ n 1) 0)]\n         [is-palindrome? (lambda (l r)\n                    \
        \       (let loop ([l l] [r r])\n                             (if (>= l r)\n\
        \                                 #t\n                                 (if (char=?\
        \ (string-ref s l) (string-ref s r))\n                                     (loop\
        \ (+ l 1) (- r 1))\n                                     #f))))])\n    (for\
        \ ([i (in-range 1 (+ n 1))])\n      (vector-set! dp i (vector-ref dp (- i 1)))\n\
        \      (when (and (>= i k)\n                 (is-palindrome? (- i k) (- i 1)))\n\
        \        (vector-set! dp i (max (vector-ref dp i)\n                        \
        \      (+ (vector-ref dp (- i k)) 1))))\n      (when (and (>= i (+ k 1))\n \
        \                (is-palindrome? (- i (+ k 1)) (- i 1)))\n        (vector-set!\
        \ dp i (max (vector-ref dp i)\n                              (+ (vector-ref\
        \ dp (- i (+ k 1))) 1)))))\n    (vector-ref dp n)))"
      erlang: "-spec max_palindromes(S :: unicode:unicode_binary(), K :: integer())\
        \ -> integer().\nmax_palindromes(S, K) ->\n    N = byte_size(S),\n    Dp = array:new([{size,\
        \ N + 1}, {fixed, true}, {default, 0}]),\n    FinalDp = final_solve(1, N, K,\
        \ S, Dp),\n    array:get(N, FinalDp).\n\nfinal_solve(I, N, K, S, Dp) when I\
        \ =< N ->\n    V_prev = array:get(I - 1, Dp),\n    Dp1 = array:set(I, V_prev,\
        \ Dp),\n\n    Dp2 = case (I >= K) andalso is_palindrome(S, I - K, I - 1) of\n\
        \        true ->\n            Cur1 = array:get(I, Dp1),\n            New1 =\
        \ array:get(I - K, Dp1) + 1,\n            array:set(I, max(Cur1, New1), Dp1);\n\
        \        false -> Dp1\n    end,\n\n    Dp3 = case (I >= K + 1) andalso is_palindrome(S,\
        \ I - (K + 1), I - 1) of\n        true ->\n            Cur2 = array:get(I, Dp2),\n\
        \            New2 = array:get(I - (K + 1), Dp2) + 1,\n            array:set(I,\
        \ max(Cur2, New2), Dp2);\n        false -> Dp2\n    end,\n    final_solve(I\
        \ + 1, N, K, S, Dp3);\nfinal_solve(_I, _N, _K, _S, Dp) ->\n    Dp.\n\nis_palindrome(S,\
        \ L, R) ->\n    is_palindrome_rec(S, L, R).\n\nis_palindrome_rec(_S, L, R) when\
        \ L >= R -> true;\nis_palindrome_rec(S, L, R) ->\n    case binary:at(S, L) ==\
        \ binary:at(S, R) of\n        true -> is_palindrome_rec(S, L + 1, R - 1);\n\
        \        false -> false\n    end."
      elixir: "defmodule Solution do\n  @spec max_palindromes(s :: String.t, k :: integer)\
        \ :: integer\n  def max_palindromes(s, k) do\n    n = byte_size(s)\n    dp =\
        \ :array.new([size: n + 1, fixed: true, default: 0])\n\n    final_dp = Enum.reduce(1..n,\
        \ dp, fn i, acc ->\n      v_prev = :array.get(i - 1, acc)\n      acc = :array.set(i,\
        \ v_prev, acc)\n\n      acc = if i >= k and is_palindrome?(s, i - k, i - 1)\
        \ do\n        cur1 = :array.get(i, acc)\n        new1 = :array.get(i - k, acc)\
        \ + 1\n        :array.set(i, max(cur1, new1), acc)\n      else\n        acc\n\
        \      end\n\n      acc = if i >= k + 1 and is_palindrome?(s, i - (k + 1), i\
        \ - 1) do\n        cur2 = :array.get(i, acc)\n        new2 = :array.get(i -\
        \ (k + 1), acc) + 1\n        :array.set(i, max(cur2, new2), acc)\n      else\n\
        \        acc\n      end\n      acc\n    end)\n\n    :array.get(n, final_dp)\n\
        \  end\n\n  defp is_palindrome?(s, l, r) do\n    is_palindrome_rec(s, l, r)\n\
        \  end\n\n  defp is_palindrome_rec(_s, l, r) when l >= r, do: true\n  defp is_palindrome_rec(s,\
        \ l, r) do\n    if :binary.at(s, l) == :binary.at(s, r) do\n      is_palindrome_rec(s,\
        \ l + 1, r - 1)\n    else\n      false\n    end\n  end\nend"
    approach: 'The problem can be solved by combining dynamic programming with a greedy
      observation about palindromes. We define $dp[i]$ as the maximum number of non-overlapping
      palindromic substrings of length at least $k$ in the prefix $s[0...i-1]$. For
      each index $i$, we either skip the character $s[i-1]$ (setting $dp[i] = dp[i-1]$)
      or attempt to find a palindrome of length at least $k$ that ends at $s[i-1]$.
      A key insight is that any palindrome of length $L \ge k$ contains a ''minimal''
      palindrome of length either $k$ or $k+1$ that ends at or before the same position.
      Because our goal is to maximize the total number of non-overlapping segments,
      picking the earliest possible ending palindrome is always optimal.


      By focusing only on palindromes of length $k$ and $k+1$ ending at each position
      $i$, we can efficiently update our DP state. For each $i$, we check if $s[i-k...i-1]$
      is a palindrome or if $s[i-k-1...i-1]$ is a palindrome. If either condition is
      met, we update $dp[i]$ by incrementing the count from the corresponding previous
      DP state ($dp[i-k]$ or $dp[i-k-1]$). This greedy DP approach ensures we find the
      maximum number of non-overlapping segments while keeping the time complexity efficient.'
    time_complexity: O(nk) with one-paragraph explanation. The algorithm iterates through
      the string of length $n$ once. For each position, it performs at most two palindrome
      checks of length $k$ and $k+1$. Since each palindrome check takes $O(k)$ time,
      the total complexity is $O(n \cdot k)$. Given $n \le 2000$, this results in at
      most $4 \times 10^6$ operations, which easily fits within the execution time limits
      for C++, Java, and Python.
    space_complexity: O(n) with one-paragraph explanation. The algorithm uses a one-dimensional
      dynamic programming array of size $n+1$ to store the maximum count of non-overlapping
      palindromes for each prefix of the input string. This results in $O(n)$ space
      complexity, which is well within memory constraints.
    elapsed_time: 323.06756067276
    model: gemini-3-flash-preview
    generated_at: '2026-09-15 02:50:35 '
---

## Problem #2472: Maximum Number of Non-overlapping Palindrome Substrings

**Difficulty:** Hard

**Topics:** Two Pointers, String, Dynamic Programming, Greedy

## Problem Description

<p>You are given a string <code>s</code> and a <strong>positive</strong> integer <code>k</code>.</p>

<p>Select a set of <strong>non-overlapping</strong> substrings from the string <code>s</code> that satisfy the following conditions:</p>

<ul>
	<li>The <strong>length</strong> of each substring is <strong>at least</strong> <code>k</code>.</li>
	<li>Each substring is a <strong>palindrome</strong>.</li>
</ul>

<p>Return <em>the <strong>maximum</strong> number of substrings in an optimal selection</em>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abaccdbbd&quot;, k = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can select the substrings underlined in s = &quot;<u><strong>aba</strong></u>cc<u><strong>dbbd</strong></u>&quot;. Both &quot;aba&quot; and &quot;dbbd&quot; are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;adbcda&quot;, k = 2
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no palindrome substring of length at least 2 in the string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>


## Hints

1. Try to use dynamic programming to solve the problem.

2. let dp[i] be the answer for the prefix s[0…i].

3. The final answer to the problem will be dp[n-1]. How do you compute this dp?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved by combining dynamic programming with a greedy observation about palindromes. We define $dp[i]$ as the maximum number of non-overlapping palindromic substrings of length at least $k$ in the prefix $s[0...i-1]$. For each index $i$, we either skip the character $s[i-1]$ (setting $dp[i] = dp[i-1]$) or attempt to find a palindrome of length at least $k$ that ends at $s[i-1]$. A key insight is that any palindrome of length $L \ge k$ contains a 'minimal' palindrome of length either $k$ or $k+1$ that ends at or before the same position. Because our goal is to maximize the total number of non-overlapping segments, picking the earliest possible ending palindrome is always optimal.

By focusing only on palindromes of length $k$ and $k+1$ ending at each position $i$, we can efficiently update our DP state. For each $i$, we check if $s[i-k...i-1]$ is a palindrome or if $s[i-k-1...i-1]$ is a palindrome. If either condition is met, we update $dp[i]$ by incrementing the count from the corresponding previous DP state ($dp[i-k]$ or $dp[i-k-1]$). This greedy DP approach ensures we find the maximum number of non-overlapping segments while keeping the time complexity efficient.

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
    int maxPalindromes(string s, int k) {
        int n = s.length();
        if (k == 1) return n;
        vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            dp[i] = dp[i - 1];
            if (i >= k) {
                if (isPal(s, i - k, i - 1)) {
                    dp[i] = max(dp[i], dp[i - k] + 1);
                }
            }
            if (i >= k + 1) {
                if (isPal(s, i - k - 1, i - 1)) {
                    dp[i] = max(dp[i], dp[i - k - 1] + 1);
                }
            }
        }
        return dp[n];
    }

private:
    bool isPal(const string& s, int l, int r) {
        while (l < r) {
            if (s[l++] != s[r--]) return false;
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxPalindromes(String s, int k) {
        int n = s.length();
        if (k == 1) return n;
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1];
            if (i >= k) {
                if (isPal(s, i - k, i - 1)) {
                    dp[i] = Math.max(dp[i], dp[i - k] + 1);
                }
            }
            if (i >= k + 1) {
                if (isPal(s, i - k - 1, i - 1)) {
                    dp[i] = Math.max(dp[i], dp[i - k - 1] + 1);
                }
            }
        }
        return dp[n];
    }

    private boolean isPal(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if k == 1:
            return n

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            if i >= k:
                if s[i - k] == s[i - 1]:
                    sub = s[i - k:i]
                    if sub == sub[::-1]:
                        dp[i] = max(dp[i], dp[i - k] + 1)
            if i >= k + 1:
                if s[i - k - 1] == s[i - 1]:
                    sub = s[i - k - 1:i]
                    if sub == sub[::-1]:
                        dp[i] = max(dp[i], dp[i - k - 1] + 1)
        return dp[n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1
        for i in range(n):
            l1 = i - k + 1
            if l1 > last_end and l1 >= 0:
                sub = s[l1 : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_end = i
                    continue
            l2 = i - k
            if l2 > last_end and l2 >= 0:
                sub = s[l2 : i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    last_end = i
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>

int maxPalindromes(char* s, int k) {
    int n = strlen(s);
    int ans = 0;
    int last_end = -1;
    for (int i = 0; i < n; i++) {
        int l1 = i - k + 1;
        if (l1 > last_end && l1 >= 0) {
            int l = l1, r = i;
            int is_pal = 1;
            while (l < r) {
                if (s[l] != s[r]) {
                    is_pal = 0;
                    break;
                }
                l++;
                r--;
            }
            if (is_pal) {
                ans++;
                last_end = i;
                continue;
            }
        }
        int l2 = i - k;
        if (l2 > last_end && l2 >= 0) {
            int l = l2, r = i;
            int is_pal = 1;
            while (l < r) {
                if (s[l] != s[r]) {
                    is_pal = 0;
                    break;
                }
                l++;
                r--;
            }
            if (is_pal) {
                ans++;
                last_end = i;
            }
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
    public int MaxPalindromes(string s, int k) {
        int n = s.Length;
        int ans = 0;
        int lastEnd = -1;
        for (int i = 0; i < n; i++) {
            int l1 = i - k + 1;
            if (l1 > lastEnd && l1 >= 0) {
                int l = l1, r = i;
                bool isPal = true;
                while (l < r) {
                    if (s[l] != s[r]) {
                        isPal = false;
                        break;
                    }
                    l++;
                    r--;
                }
                if (isPal) {
                    ans++;
                    lastEnd = i;
                    continue;
                }
            }
            int l2 = i - k;
            if (l2 > lastEnd && l2 >= 0) {
                int l = l2, r = i;
                bool isPal = true;
                while (l < r) {
                    if (s[l] != s[r]) {
                        isPal = false;
                        break;
                    }
                    l++;
                    r--;
                }
                if (isPal) {
                    ans++;
                    lastEnd = i;
                }
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
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxPalindromes = function(s, k) {
    let n = s.length;
    let ans = 0;
    let lastEnd = -1;
    for (let i = 0; i < n; i++) {
        let l1 = i - k + 1;
        if (l1 > lastEnd && l1 >= 0) {
            let l = l1, r = i;
            let isPal = true;
            while (l < r) {
                if (s[l] !== s[r]) {
                    isPal = false;
                    break;
                }
                l++;
                r--;
            }
            if (isPal) {
                ans++;
                lastEnd = i;
                continue;
            }
        }
        let l2 = i - k;
        if (l2 > lastEnd && l2 >= 0) {
            let l = l2, r = i;
            let isPal = true;
            while (l < r) {
                if (s[l] !== s[r]) {
                    isPal = false;
                    break;
                }
                l++;
                r--;
            }
            if (isPal) {
                ans++;
                lastEnd = i;
            }
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
function maxPalindromes(s: string, k: number): number {
    const n = s.length;
    const dp = new Array(n + 1).fill(0);

    const isPal = (l: number, r: number): boolean => {
        while (l < r) {
            if (s[l] !== s[r]) return false;
            l++;
            r--;
        }
        return true;
    };

    for (let i = 1; i <= n; i++) {
        dp[i] = dp[i - 1];
        if (i >= k && isPal(i - k, i - 1)) {
            dp[i] = Math.max(dp[i], dp[i - k] + 1);
        }
        if (i >= k + 1 && isPal(i - k - 1, i - 1)) {
            dp[i] = Math.max(dp[i], dp[i - k - 1] + 1);
        }
    }
    return dp[n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function maxPalindromes($s, $k) {
        $n = strlen($s);
        $dp = array_fill(0, $n + 1, 0);
        for ($i = 1; $i <= $n; $i++) {
            $dp[$i] = $dp[$i - 1];
            if ($i >= $k && $this->isPal($s, $i - $k, $i - 1)) {
                $dp[$i] = max($dp[$i], $dp[$i - $k] + 1);
            }
            if ($i >= $k + 1 && $this->isPal($s, $i - $k - 1, $i - 1)) {
                $dp[$i] = max($dp[$i], $dp[$i - $k - 1] + 1);
            }
        }
        return $dp[$n];
    }

    private function isPal($s, $l, $r) {
        while ($l < $r) {
            if ($s[$l] !== $s[$r]) {
                return false;
            }
            $l++;
            $r--;
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxPalindromes(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var dp = [Int](repeating: 0, count: n + 1)

        for i in 1...n {
            dp[i] = dp[i - 1]
            if i >= k && isPal(chars, i - k, i - 1) {
                dp[i] = max(dp[i], dp[i - k] + 1)
            }
            if i >= k + 1 && isPal(chars, i - k - 1, i - 1) {
                dp[i] = max(dp[i], dp[i - k - 1] + 1)
            }
        }
        return dp[n]
    }

    private func isPal(_ chars: [Character], _ l: Int, _ r: Int) -> Bool {
        var left = l
        var right = r
        while left < right {
            if chars[left] != chars[right] {
                return false
            }
            left += 1
            right -= 1
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxPalindromes(s: String, k: Int): Int {
        val n = s.length
        val dp = IntArray(n + 1)

        for (i in 1..n) {
            dp[i] = dp[i - 1]
            if (i >= k && isPal(s, i - k, i - 1)) {
                dp[i] = maxOf(dp[i], dp[i - k] + 1)
            }
            if (i >= k + 1 && isPal(s, i - k - 1, i - 1)) {
                dp[i] = maxOf(dp[i], dp[i - (k + 1)] + 1)
            }
        }
        return dp[n]
    }

    private fun isPal(s: String, l: Int, r: Int): Boolean {
        var left = l
        var right = r
        while (left < right) {
            if (s[left] != s[right]) return false
            left++
            right--
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxPalindromes(String s, int k) {
    int n = s.length;
    List<int> dp = List.filled(n + 1, 0);

    for (int i = 0; i < n; i++) {
      if (dp[i] > dp[i + 1]) {
        dp[i + 1] = dp[i];
      }

      // Check for palindrome of length k ending at i
      if (i >= k - 1) {
        bool isPal = true;
        int left = i - k + 1;
        int right = i;
        while (left < right) {
          if (s[left] != s[right]) {
            isPal = false;
            break;
          }
          left++;
          right--;
        }
        if (isPal) {
          int res = dp[i - k + 1] + 1;
          if (res > dp[i + 1]) {
            dp[i + 1] = res;
          }
        }
      }

      // Check for palindrome of length k + 1 ending at i
      if (i >= k) {
        bool isPal = true;
        int left = i - k;
        int right = i;
        while (left < right) {
          if (s[left] != s[right]) {
            isPal = false;
            break;
          }
          left++;
          right--;
        }
        if (isPal) {
          int res = dp[i - k] + 1;
          if (res > dp[i + 1]) {
            dp[i + 1] = res;
          }
        }
      }
    }

    return dp[n];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxPalindromes(s string, k int) int {
	n := len(s)
	dp := make([]int, n+1)

	for i := 0; i < n; i++ {
		if dp[i] > dp[i+1] {
			dp[i+1] = dp[i]
		}

		// Check for palindrome of length k ending at i
		if i >= k-1 {
			isPal := true
			left, right := i-k+1, i
			for left < right {
				if s[left] != s[right] {
					isPal = false
					break
				}
				left++
				right--
			}
			if isPal {
				res := dp[i-k+1] + 1
				if res > dp[i+1] {
					dp[i+1] = res
				}
			}
		}

		// Check for palindrome of length k + 1 ending at i
		if i >= k {
			isPal := true
			left, right := i-k, i
			for left < right {
				if s[left] != s[right] {
					isPal = false
					break
				}
				left++
				right--
			}
			if isPal {
				res := dp[i-k] + 1
				if res > dp[i+1] {
					dp[i+1] = res
				}
			}
		}
	}

	return dp[n]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_palindromes(s, k)
  n = s.length
  dp = Array.new(n + 1, 0)

  (0...n).each do |i|
    dp[i + 1] = dp[i] if dp[i] > dp[i + 1]

    # Check for palindrome of length k ending at index i
    if i >= k - 1
      is_pal = true
      left = i - k + 1
      right = i
      while left < right
        if s[left] != s[right]
          is_pal = false
          break
        end
        left += 1
        right -= 1
      end
      if is_pal
        res = dp[i - k + 1] + 1
        dp[i + 1] = res if res > dp[i + 1]
      end
    end

    # Check for palindrome of length k + 1 ending at index i
    if i >= k
      is_pal = true
      left = i - k
      right = i
      while left < right
        if s[left] != s[right]
          is_pal = false
          break
        end
        left += 1
        right -= 1
      end
      if is_pal
        res = dp[i - k] + 1
        dp[i + 1] = res if res > dp[i + 1]
      end
    end
  end

  dp[n]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def maxPalindromes(s: String, k: Int): Int = {
    val n = s.length
    val dp = new Array[Int](n + 1)

    for (i <- 0 until n) {
      if (dp(i) > dp(i + 1)) {
        dp(i + 1) = dp(i)
      }

      // Check for palindrome of length k ending at i
      if (i >= k - 1) {
        var isPal = true
        var left = i - k + 1
        var right = i
        while (left < right && isPal) {
          if (s(left) != s(right)) {
            isPal = false
          } else {
            left += 1
            right -= 1
          }
        }
        if (isPal) {
          val res = dp(i - k + 1) + 1
          if (res > dp(i + 1)) {
            dp(i + 1) = res
          }
        }
      }

      // Check for palindrome of length k + 1 ending at i
      if (i >= k) {
        var isPal = true
        var left = i - k
        var right = i
        while (left < right && isPal) {
          if (s(left) != s(right)) {
            isPal = false
          } else {
            left += 1
            right -= 1
          }
        }
        if (isPal) {
          val res = dp(i - k) + 1
          if (res > dp(i + 1)) {
            dp(i + 1) = res
          }
        }
      }
    }

    dp(n)
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_palindromes(s: String, k: i32) -> i32 {
        let n = s.len();
        let k = k as usize;
        let s_bytes = s.as_bytes();
        let mut dp = vec![0; n + 1];

        for i in 1..=n {
            dp[i] = dp[i - 1];

            if i >= k && Self::is_palindrome(s_bytes, i - k, i - 1) {
                dp[i] = dp[i].max(dp[i - k] + 1);
            }

            if i >= k + 1 && Self::is_palindrome(s_bytes, i - (k + 1), i - 1) {
                dp[i] = dp[i].max(dp[i - (k + 1)] + 1);
            }
        }
        dp[n]
    }

    fn is_palindrome(s: &[u8], mut l: usize, mut r: usize) -> bool {
        while l < r {
            if s[l] != s[r] {
                return false;
            }
            l += 1;
            r -= 1;
        }
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-palindromes s k)
  (-> string? exact-integer? exact-integer?)
  (let* ([n (string-length s)]
         [dp (make-vector (+ n 1) 0)]
         [is-palindrome? (lambda (l r)
                           (let loop ([l l] [r r])
                             (if (>= l r)
                                 #t
                                 (if (char=? (string-ref s l) (string-ref s r))
                                     (loop (+ l 1) (- r 1))
                                     #f))))])
    (for ([i (in-range 1 (+ n 1))])
      (vector-set! dp i (vector-ref dp (- i 1)))
      (when (and (>= i k)
                 (is-palindrome? (- i k) (- i 1)))
        (vector-set! dp i (max (vector-ref dp i)
                              (+ (vector-ref dp (- i k)) 1))))
      (when (and (>= i (+ k 1))
                 (is-palindrome? (- i (+ k 1)) (- i 1)))
        (vector-set! dp i (max (vector-ref dp i)
                              (+ (vector-ref dp (- i (+ k 1))) 1)))))
    (vector-ref dp n)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_palindromes(S :: unicode:unicode_binary(), K :: integer()) -> integer().
max_palindromes(S, K) ->
    N = byte_size(S),
    Dp = array:new([{size, N + 1}, {fixed, true}, {default, 0}]),
    FinalDp = final_solve(1, N, K, S, Dp),
    array:get(N, FinalDp).

final_solve(I, N, K, S, Dp) when I =< N ->
    V_prev = array:get(I - 1, Dp),
    Dp1 = array:set(I, V_prev, Dp),

    Dp2 = case (I >= K) andalso is_palindrome(S, I - K, I - 1) of
        true ->
            Cur1 = array:get(I, Dp1),
            New1 = array:get(I - K, Dp1) + 1,
            array:set(I, max(Cur1, New1), Dp1);
        false -> Dp1
    end,

    Dp3 = case (I >= K + 1) andalso is_palindrome(S, I - (K + 1), I - 1) of
        true ->
            Cur2 = array:get(I, Dp2),
            New2 = array:get(I - (K + 1), Dp2) + 1,
            array:set(I, max(Cur2, New2), Dp2);
        false -> Dp2
    end,
    final_solve(I + 1, N, K, S, Dp3);
final_solve(_I, _N, _K, _S, Dp) ->
    Dp.

is_palindrome(S, L, R) ->
    is_palindrome_rec(S, L, R).

is_palindrome_rec(_S, L, R) when L >= R -> true;
is_palindrome_rec(S, L, R) ->
    case binary:at(S, L) == binary:at(S, R) of
        true -> is_palindrome_rec(S, L + 1, R - 1);
        false -> false
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_palindromes(s :: String.t, k :: integer) :: integer
  def max_palindromes(s, k) do
    n = byte_size(s)
    dp = :array.new([size: n + 1, fixed: true, default: 0])

    final_dp = Enum.reduce(1..n, dp, fn i, acc ->
      v_prev = :array.get(i - 1, acc)
      acc = :array.set(i, v_prev, acc)

      acc = if i >= k and is_palindrome?(s, i - k, i - 1) do
        cur1 = :array.get(i, acc)
        new1 = :array.get(i - k, acc) + 1
        :array.set(i, max(cur1, new1), acc)
      else
        acc
      end

      acc = if i >= k + 1 and is_palindrome?(s, i - (k + 1), i - 1) do
        cur2 = :array.get(i, acc)
        new2 = :array.get(i - (k + 1), acc) + 1
        :array.set(i, max(cur2, new2), acc)
      else
        acc
      end
      acc
    end)

    :array.get(n, final_dp)
  end

  defp is_palindrome?(s, l, r) do
    is_palindrome_rec(s, l, r)
  end

  defp is_palindrome_rec(_s, l, r) when l >= r, do: true
  defp is_palindrome_rec(s, l, r) do
    if :binary.at(s, l) == :binary.at(s, r) do
      is_palindrome_rec(s, l + 1, r - 1)
    else
      false
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(nk) with one-paragraph explanation. The algorithm iterates through the string of length $n$ once. For each position, it performs at most two palindrome checks of length $k$ and $k+1$. Since each palindrome check takes $O(k)$ time, the total complexity is $O(n \cdot k)$. Given $n \le 2000$, this results in at most $4 \times 10^6$ operations, which easily fits within the execution time limits for C++, Java, and Python.
- **Space Complexity:** O(n) with one-paragraph explanation. The algorithm uses a one-dimensional dynamic programming array of size $n+1$ to store the maximum count of non-overlapping palindromes for each prefix of the input string. This results in $O(n)$ space complexity, which is well within memory constraints.
