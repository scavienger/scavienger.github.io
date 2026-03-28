---
layout: post
title: "Find the String with LCP"
date: 2026-03-28 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "String", "Dynamic Programming", "Greedy", "Union-Find", "Matrix"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/find-the-string-with-lcp/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string findTheString(vector<vector<int>>&\
        \ lcp) {\n        int n = lcp.size();\n        string s(n, '\\0');\n       \
        \ char cur = 'a';\n        for (int i = 0; i < n; ++i) {\n            if (s[i]\
        \ == '\\0') {\n                if (cur > 'z') return \"\";\n               \
        \ for (int j = i; j < n; ++j) {\n                    if (lcp[i][j] > 0) s[j]\
        \ = cur;\n                }\n                cur++;\n            }\n       \
        \ }\n\n        for (int i = 0; i < n; ++i) if (s[i] == '\\0') return \"\";\n\
        \n        for (int i = n - 1; i >= 0; --i) {\n            for (int j = n - 1;\
        \ j >= 0; --j) {\n                int expected = (s[i] == s[j]) ? ((i + 1 <\
        \ n && j + 1 < n) ? lcp[i + 1][j + 1] + 1 : 1) : 0;\n                if (lcp[i][j]\
        \ != expected) return \"\";\n            }\n        }\n        return s;\n \
        \   }\n};"
      java: "class Solution {\n    public String findTheString(int[][] lcp) {\n    \
        \    int n = lcp.length;\n        char[] s = new char[n];\n        char cur\
        \ = 'a';\n        for (int i = 0; i < n; i++) {\n            if (s[i] == 0)\
        \ {\n                if (cur > 'z') return \"\";\n                for (int j\
        \ = i; j < n; j++) {\n                    if (lcp[i][j] > 0) s[j] = cur;\n \
        \               }\n                cur++;\n            }\n        }\n\n    \
        \    for (int i = 0; i < n; i++) if (s[i] == 0) return \"\";\n\n        for\
        \ (int i = n - 1; i >= 0; i--) {\n            for (int j = n - 1; j >= 0; j--)\
        \ {\n                int expected = (s[i] == s[j]) ? ((i + 1 < n && j + 1 <\
        \ n) ? lcp[i + 1][j + 1] + 1 : 1) : 0;\n                if (lcp[i][j] != expected)\
        \ return \"\";\n            }\n        }\n        return new String(s);\n  \
        \  }\n}"
      python: "class Solution(object):\n    def findTheString(self, lcp):\n        \"\
        \"\"\n        :type lcp: List[List[int]]\n        :rtype: str\n        \"\"\"\
        \n        n = len(lcp)\n        res = [None] * n\n        c = 0\n        for\
        \ i in range(n):\n            if res[i] is None:\n                if c >= 26:\
        \ return \"\"\n                char = chr(ord('a') + c)\n                c +=\
        \ 1\n                for j in range(i, n):\n                    if lcp[i][j]\
        \ > 0:\n                        res[j] = char\n\n        if None in res: return\
        \ \"\"\n        word = \"\".join(res)\n        for i in range(n - 1, -1, -1):\n\
        \            for j in range(n - 1, -1, -1):\n                expected = 0\n\
        \                if word[i] == word[j]:\n                    expected = (lcp[i\
        \ + 1][j + 1] if i + 1 < n and j + 1 < n else 0) + 1\n                if lcp[i][j]\
        \ != expected:\n                    return \"\"\n        return word"
      python3: "class Solution:\n    def findTheString(self, lcp: List[List[int]]) ->\
        \ str:\n        n = len(lcp)\n        res = [None] * n\n        c = 0\n    \
        \    for i in range(n):\n            if res[i] is None:\n                if\
        \ c >= 26: return \"\"\n                char = chr(ord('a') + c)\n         \
        \       c += 1\n                for j in range(i, n):\n                    if\
        \ lcp[i][j] > 0:\n                        res[j] = char\n\n        if None in\
        \ res: return \"\"\n        word = \"\".join(res)\n        for i in range(n\
        \ - 1, -1, -1):\n            for j in range(n - 1, -1, -1):\n              \
        \  expected = 0\n                if word[i] == word[j]:\n                  \
        \  expected = (lcp[i + 1][j + 1] if (i + 1 < n and j + 1 < n) else 0) + 1\n\
        \                if lcp[i][j] != expected:\n                    return \"\"\n\
        \        return word"
      c: "char* findTheString(int** lcp, int n, int* lcpColSize) {\n    char* s = (char*)calloc(n\
        \ + 1, sizeof(char));\n    char cur = 'a';\n    for (int i = 0; i < n; i++)\
        \ {\n        if (s[i] == 0) {\n            if (cur > 'z') {\n              \
        \  free(s);\n                char* empty = (char*)calloc(1, 1);\n          \
        \      return empty;\n            }\n            for (int j = i; j < n; j++)\
        \ {\n                if (lcp[i][j] > 0) s[j] = cur;\n            }\n       \
        \     cur++;\n        }\n    }\n    for (int i = 0; i < n; i++) {\n        if\
        \ (s[i] == 0) {\n            free(s);\n            char* empty = (char*)calloc(1,\
        \ 1);\n            return empty;\n        }\n    }\n    for (int i = n - 1;\
        \ i >= 0; i--) {\n        for (int j = n - 1; j >= 0; j--) {\n            int\
        \ expected = (s[i] == s[j]) ? ((i + 1 < n && j + 1 < n) ? lcp[i + 1][j + 1]\
        \ + 1 : 1) : 0;\n            if (lcp[i][j] != expected) {\n                free(s);\n\
        \                char* empty = (char*)calloc(1, 1);\n                return\
        \ empty;\n            }\n        }\n    }\n    return s;\n}"
      csharp: "public class Solution {\n    public string FindTheString(int[][] lcp)\
        \ {\n        int n = lcp.Length;\n        char[] s = new char[n];\n        char\
        \ cur = 'a';\n        for (int i = 0; i < n; i++) {\n            if (s[i] ==\
        \ '\\0') {\n                if (cur > 'z') return \"\";\n                for\
        \ (int j = i; j < n; j++) {\n                    if (lcp[i][j] > 0) s[j] = cur;\n\
        \                }\n                cur++;\n            }\n        }\n\n   \
        \     for (int i = 0; i < n; i++) if (s[i] == '\\0') return \"\";\n\n      \
        \  for (int i = n - 1; i >= 0; i--) {\n            for (int j = n - 1; j >=\
        \ 0; j--) {\n                int expected = (s[i] == s[j]) ? ((i + 1 < n &&\
        \ j + 1 < n) ? lcp[i + 1][j + 1] + 1 : 1) : 0;\n                if (lcp[i][j]\
        \ != expected) return \"\";\n            }\n        }\n        return new string(s);\n\
        \    }\n}"
      javascript: "/**\n * @param {number[][]} lcp\n * @return {string}\n */\nvar findTheString\
        \ = function(lcp) {\n    let n = lcp.length;\n    let s = new Array(n).fill(null);\n\
        \    let charCode = 97;\n    for (let i = 0; i < n; i++) {\n        if (s[i]\
        \ === null) {\n            if (charCode > 122) return \"\";\n            let\
        \ char = String.fromCharCode(charCode++);\n            for (let j = i; j < n;\
        \ j++) {\n                if (lcp[i][j] > 0) s[j] = char;\n            }\n \
        \       }\n    }\n    for (let i = 0; i < n; i++) if (s[i] === null) return\
        \ \"\";\n    let word = s.join('');\n    for (let i = n - 1; i >= 0; i--) {\n\
        \        for (let j = n - 1; j >= 0; j--) {\n            let expected = 0;\n\
        \            if (word[i] === word[j]) {\n                expected = (i + 1 <\
        \ n && j + 1 < n) ? lcp[i + 1][j + 1] + 1 : 1;\n            }\n            if\
        \ (lcp[i][j] !== expected) return \"\";\n        }\n    }\n    return word;\n\
        };"
      typescript: "function findTheString(lcp: number[][]): string {\n    const n =\
        \ lcp.length;\n    const s: string[] = new Array(n).fill(\"\");\n    let charCode\
        \ = 97;\n    for (let i = 0; i < n; i++) {\n        if (s[i] === \"\") {\n \
        \           if (charCode > 122) return \"\";\n            const char = String.fromCharCode(charCode++);\n\
        \            for (let j = i; j < n; j++) {\n                if (lcp[i][j] >\
        \ 0) {\n                    s[j] = char;\n                }\n            }\n\
        \        }\n    }\n    for (let i = 0; i < n; i++) {\n        for (let j = 0;\
        \ j < n; j++) {\n            let expected = 0;\n            if (s[i] === s[j])\
        \ {\n                expected = 1;\n                if (i + 1 < n && j + 1 <\
        \ n) {\n                    expected += lcp[i + 1][j + 1];\n               \
        \ }\n            }\n            if (lcp[i][j] !== expected) return \"\";\n \
        \       }\n    }\n    return s.join(\"\");\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $lcp\n     * @return\
        \ String\n     */\n    function findTheString($lcp) {\n        $n = count($lcp);\n\
        \        $s = array_fill(0, $n, '');\n        $charCode = 97;\n        for ($i\
        \ = 0; $i < $n; $i++) {\n            if ($s[$i] === '') {\n                if\
        \ ($charCode > 122) return \"\";\n                $char = chr($charCode++);\n\
        \                for ($j = $i; $j < $n; $j++) {\n                    if ($lcp[$i][$j]\
        \ > 0) {\n                        $s[$j] = $char;\n                    }\n \
        \               }\n            }\n        }\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            for ($j = 0; $j < $n; $j++) {\n                $expected =\
        \ 0;\n                if ($s[$i] === $s[$j]) {\n                    $expected\
        \ = 1;\n                    if ($i + 1 < $n && $j + 1 < $n) {\n            \
        \            $expected += $lcp[$i + 1][$j + 1];\n                    }\n   \
        \             }\n                if ($lcp[$i][$j] !== $expected) return \"\"\
        ;\n            }\n        }\n        return implode('', $s);\n    }\n}"
      swift: "class Solution {\n    func findTheString(_ lcp: [[Int]]) -> String {\n\
        \        let n = lcp.count\n        var s = Array(repeating: Character(\" \"\
        ), count: n)\n        var charCode: UInt8 = 97\n        for i in 0..<n {\n \
        \           if s[i] == \" \" {\n                if charCode > 122 { return \"\
        \" }\n                let char = Character(UnicodeScalar(charCode))\n      \
        \          charCode += 1\n                for j in i..<n {\n               \
        \     if lcp[i][j] > 0 {\n                        s[j] = char\n            \
        \        }\n                }\n            }\n        }\n        for i in 0..<n\
        \ {\n            for j in 0..<n {\n                var expected = 0\n      \
        \          if s[i] == s[j] {\n                    expected = 1\n           \
        \         if i + 1 < n && j + 1 < n {\n                        expected += lcp[i\
        \ + 1][j + 1]\n                    }\n                }\n                if\
        \ lcp[i][j] != expected {\n                    return \"\"\n               \
        \ }\n            }\n        }\n        return String(s)\n    }\n}"
      kotlin: "class Solution {\n    fun findTheString(lcp: Array<IntArray>): String\
        \ {\n        val n = lcp.size\n        val s = CharArray(n)\n        var char\
        \ = 'a'\n        for (i in 0 until n) {\n            if (s[i] == '\\u0000')\
        \ {\n                if (char > 'z') return \"\"\n                for (j in\
        \ i until n) {\n                    if (lcp[i][j] > 0) {\n                 \
        \       s[j] = char\n                    }\n                }\n            \
        \    char++\n            }\n        }\n        for (i in 0 until n) {\n    \
        \        for (j in 0 until n) {\n                var expected = 0\n        \
        \        if (s[i] == s[j]) {\n                    expected = 1\n           \
        \         if (i + 1 < n && j + 1 < n) {\n                        expected +=\
        \ lcp[i + 1][j + 1]\n                    }\n                }\n            \
        \    if (lcp[i][j] != expected) return \"\"\n            }\n        }\n    \
        \    return String(s)\n    }\n}"
      dart: "class Solution {\n  String findTheString(List<List<int>> lcp) {\n    int\
        \ n = lcp.length;\n    List<String> s = List.filled(n, \"\");\n    int charCode\
        \ = 97;\n    for (int i = 0; i < n; i++) {\n      if (s[i] == \"\") {\n    \
        \    if (charCode > 122) return \"\";\n        String char = String.fromCharCode(charCode++);\n\
        \        for (int j = i; j < n; j++) {\n          if (lcp[i][j] > 0) {\n   \
        \         s[j] = char;\n          }\n        }\n      }\n    }\n    for (int\
        \ i = 0; i < n; i++) {\n      for (int j = 0; j < n; j++) {\n        int expected\
        \ = 0;\n        if (s[i] == s[j]) {\n          expected = 1;\n          if (i\
        \ + 1 < n && j + 1 < n) {\n            expected += lcp[i + 1][j + 1];\n    \
        \      }\n        }\n        if (lcp[i][j] != expected) return \"\";\n     \
        \ }\n    }\n    return s.join(\"\");\n  }\n}"
      go: "func findTheString(lcp [][]int) string {\n\tn := len(lcp)\n\ts := make([]byte,\
        \ n)\n\tcurChar := byte('a')\n\tfor i := 0; i < n; i++ {\n\t\tif s[i] == 0 {\n\
        \t\t\tif curChar > 'z' {\n\t\t\t\treturn \"\"\n\t\t\t}\n\t\t\tfor j := i; j\
        \ < n; j++ {\n\t\t\t\tif lcp[i][j] > 0 {\n\t\t\t\t\ts[j] = curChar\n\t\t\t\t\
        }\n\t\t\t}\n\t\t\tcurChar++\n\t\t}\n\t}\n\tfor i := 0; i < n; i++ {\n\t\tfor\
        \ j := 0; j < n; j++ {\n\t\texpected := 0\n\t\tif s[i] == s[j] {\n\t\t\texpected\
        \ = 1\n\t\t\tif i+1 < n && j+1 < n {\n\t\t\t\texpected += lcp[i+1][j+1]\n\t\t\
        \t}\n\t\t}\n\t\tif lcp[i][j] != expected {\n\t\t\treturn \"\"\n\t\t}\n\t\t}\n\
        \t}\n\treturn string(s)\n}"
      ruby: "def find_the_string(lcp)\n  n = lcp.length\n  word = Array.new(n)\n  curr_char_code\
        \ = 'a'.ord\n  (0...n).each do |i|\n    if word[i].nil?\n      return \"\" if\
        \ curr_char_code > 'z'.ord\n      char = curr_char_code.chr\n      (i...n).each\
        \ do |j|\n        if lcp[i][j] > 0\n          word[j] = char if word[j].nil?\n\
        \        end\n      end\n      curr_char_code += 1\n    end\n  end\n  return\
        \ \"\" if word.any?(&:nil?)\n  dp = Array.new(n + 1) { Array.new(n + 1, 0) }\n\
        \  (n - 1).downto(0) do |i|\n    (n - 1).downto(0) do |j|\n      if word[i]\
        \ == word[j]\n        dp[i][j] = dp[i + 1][j + 1] + 1\n      else\n        dp[i][j]\
        \ = 0\n      end\n      return \"\" if dp[i][j] != lcp[i][j]\n    end\n  end\n\
        \  word.join\nend"
      scala: "object Solution {\n  def findTheString(lcp: Array[Array[Int]]): String\
        \ = {\n    val n = lcp.length\n    val word = new Array[Char](n)\n    var currChar\
        \ = 'a'\n    for (i <- 0 until n) {\n      if (word(i) == '\\u0000') {\n   \
        \     if (currChar > 'z') return \"\"\n        for (j <- i until n) {\n    \
        \      if (lcp(i)(j) > 0) {\n            if (word(j) == '\\u0000') word(j) =\
        \ currChar\n          }\n        }\n        currChar = (currChar.toInt + 1).toChar\n\
        \      }\n    }\n    if (word.contains('\\u0000')) return \"\"\n    val dp =\
        \ Array.ofDim[Int](n + 1, n + 1)\n    for (i <- n - 1 to 0 by -1) {\n      for\
        \ (j <- n - 1 to 0 by -1) {\n        dp(i)(j) = if (word(i) == word(j)) dp(i\
        \ + 1)(j + 1) + 1 else 0\n        if (dp(i)(j) != lcp(i)(j)) return \"\"\n \
        \     }\n    }\n    new String(word)\n  }\n}"
      rust: "impl Solution {\n    pub fn find_the_string(lcp: Vec<Vec<i32>>) -> String\
        \ {\n        let n = lcp.len();\n        let mut word = vec![0u8; n];\n    \
        \    let mut curr_char = b'a';\n        for i in 0..n {\n            if word[i]\
        \ == 0 {\n                if curr_char > b'z' {\n                    return\
        \ \"\".to_string();\n                }\n                for j in i..n {\n  \
        \                  if lcp[i][j] > 0 {\n                        if word[j] ==\
        \ 0 {\n                            word[j] = curr_char;\n                  \
        \      }\n                    }\n                }\n                curr_char\
        \ += 1;\n            }\n        }\n        if word.iter().any(|&c| c == 0) {\n\
        \            return \"\".to_string();\n        }\n        let mut dp = vec![vec![0;\
        \ n + 1]; n + 1];\n        for i in (0..n).rev() {\n            for j in (0..n).rev()\
        \ {\n                dp[i][j] = if word[i] == word[j] {\n                  \
        \  dp[i + 1][j + 1] + 1\n                } else {\n                    0\n \
        \               };\n                if dp[i][j] != lcp[i][j] {\n           \
        \         return \"\".to_string();\n                }\n            }\n     \
        \   }\n        String::from_utf8(word).unwrap_or_else(|_| \"\".to_string())\n\
        \    }\n}"
      racket: "(define/contract (find-the-string lcp-list)\n  (-> (listof (listof exact-integer?))\
        \ string?)\n  (let* ([n (length lcp-list)]\n         [lcp (apply vector (map\
        \ (lambda (row) (apply vector row)) lcp-list))]\n         [word (make-vector\
        \ n #f)])\n    (define (assign-chars)\n      (let loop ([i 0] [code (char->integer\
        \ #\\a)])\n        (cond\n          [(= i n) #t]\n          [(vector-ref word\
        \ i) (loop (+ i 1) code)]\n          [(> code (char->integer #\\z)) #f]\n  \
        \        [else\n           (for ([j (in-range i n)])\n             (when (>\
        \ (vector-ref (vector-ref lcp i) j) 0)\n               (unless (vector-ref word\
        \ j)\n                 (vector-set! word j (integer->char code)))))\n      \
        \     (loop (+ i 1) (+ code 1))]))) \n    (if (and (assign-chars) (for/and ([i\
        \ (in-range n)]) (vector-ref word i)))\n        (let ([check-lcp (make-vector\
        \ (+ n 1))])\n          (for ([i (in-range (+ n 1))]) (vector-set! check-lcp\
        \ i (make-vector (+ n 1) 0)))\n          (let/ec return\n            (for ([i\
        \ (in-range (- n 1) -1 -1)])\n              (for ([j (in-range (- n 1) -1 -1)])\n\
        \                (let* ([v (if (char=? (vector-ref word i) (vector-ref word\
        \ j))\n                              (+ 1 (vector-ref (vector-ref check-lcp\
        \ (+ i 1)) (+ j 1)))\n                              0)])\n                 \
        \ (if (not (= v (vector-ref (vector-ref lcp i) j)))\n                      (return\
        \ \"\")\n                      (vector-set! (vector-ref check-lcp i) j v)))))\n\
        \            (list->string (vector->list word))))\n        \"\")))"
      erlang: "-spec find_the_string(Lcp :: [[integer()]]) -> unicode:unicode_binary().\n\
        find_the_string(LcpList) ->\n  N = length(LcpList),\n  Lcp = list_to_tuple([list_to_tuple(Row)\
        \ || Row <- LcpList]),\n  case assign_word(N, Lcp, 0, $a, #{}) of\n    error\
        \ -> <<>>;\n    WordMap ->\n      WordList = [maps:get(I, WordMap, undefined)\
        \ || I <- lists:seq(0, N - 1)],\n      case lists:any(fun(X) -> X == undefined\
        \ end, WordList) of\n        true -> <<>>;\n        false ->\n          WordTuple\
        \ = list_to_tuple(WordList),\n          case verify(N, Lcp, WordTuple) of\n\
        \            true -> list_to_binary(WordList);\n            false -> <<>>\n\
        \          end\n      end\n  end.\n\nassign_word(N, _Lcp, I, _Char, Acc) when\
        \ I == N -> Acc;\nassign_word(N, Lcp, I, Char, Acc) ->\n  case maps:is_key(I,\
        \ Acc) of\n    true -> assign_word(N, Lcp, I + 1, Char, Acc);\n    false ->\n\
        \      if Char > $z -> error;\n         true ->\n           NewAcc = lists:foldl(fun(J,\
        \ A) ->\n             case element(J + 1, element(I + 1, Lcp)) > 0 of\n    \
        \           true -> maps:put_new(J, Char, A);\n               false -> A\n \
        \            end\n           end, Acc, lists:seq(I, N - 1)),\n           assign_word(N,\
        \ Lcp, I + 1, Char + 1, NewAcc)\n      end\n  end.\n\nverify(N, Lcp, WordTuple)\
        \ ->\n  try\n    lists:foldl(fun(I, NextRowTuple) ->\n      {RowI, _} = lists:foldr(fun(J,\
        \ {AccRow, _}) ->\n        Val = case element(I + 1, WordTuple) == element(J\
        \ + 1, WordTuple) of\n                true -> element(J + 2, NextRowTuple) +\
        \ 1;\n                false -> 0\n              end,\n        case Val == element(J\
        \ + 1, element(I + 1, Lcp)) of\n          true -> {[Val | AccRow], ok};\n  \
        \        false -> throw(error)\n        end\n      end, {[], ok}, lists:seq(0,\
        \ N - 1)),\n      list_to_tuple(RowI ++ [0])\n    end, list_to_tuple(lists:duplicate(N\
        \ + 1, 0)), lists:reverse(lists:seq(0, N - 1))),\n    true\n  catch\n    error\
        \ -> false\n  end."
      elixir: "defmodule Solution do\n  @spec find_the_string(lcp :: [[integer]]) ::\
        \ String.t\n  def find_the_string(lcp_list) do\n    n = length(lcp_list)\n \
        \   lcp = lcp_list |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n    word_map\
        \ = assign_word(n, lcp, 0, ?a, %{})\n    if word_map == :error do\n      \"\"\
        \n    else\n      word_list = for i <- 0..(n-1), do: Map.get(word_map, i)\n\
        \      if Enum.any?(word_list, &is_nil/1) do\n        \"\"\n      else\n   \
        \     word_t = List.to_tuple(word_list)\n        if verify(n, lcp, word_t) do\n\
        \          List.to_string(word_list)\n        else\n          \"\"\n       \
        \ end\n      end\n    end\n  end\n\n  defp assign_word(n, _lcp, i, _char, acc)\
        \ when i == n, do: acc\n  defp assign_word(n, lcp, i, char, acc) do\n    if\
        \ Map.has_key?(acc, i) do\n      assign_word(n, lcp, i + 1, char, acc)\n   \
        \ else\n      if char > ?z do\n        :error\n      else\n        new_acc =\
        \ Enum.reduce(i..(n-1), acc, fn j, a ->\n          if elem(elem(lcp, i), j)\
        \ > 0, do: Map.put_new(a, j, char), else: a\n        end)\n        assign_word(n,\
        \ lcp, i + 1, char + 1, new_acc)\n      end\n    end\n  end\n\n  defp verify(n,\
        \ lcp, word_t) do\n    try do\n      Enum.reduce((n-1)..0, List.to_tuple(List.duplicate(0,\
        \ n + 1)), fn i, next_dp_row ->\n        {curr_dp_list, _} = Enum.reduce((n-1)..0,\
        \ {[], next_dp_row}, fn j, {acc, next_dp} ->\n          val = if elem(word_t,\
        \ i) == elem(word_t, j), do: elem(next_dp, j + 1) + 1, else: 0\n          if\
        \ val != elem(elem(lcp, i), j), do: throw(:error)\n          {[val | acc], next_dp}\n\
        \        end)\n        List.to_tuple(curr_dp_list ++ [0])\n      end)\n    \
        \  true\n    catch\n      :error -> false\n    end\n  end\nend"
    approach: 'The problem asks us to reconstruct a string from its LCP (Longest Common
      Prefix) matrix. The key observation is that $LCP[i][j] > 0$ if and only if the
      characters at indices $i$ and $j$ are identical ($word[i] = word[j]$). We can
      use this greedy property to build a candidate string: iterate through the indices
      from $0$ to $n-1$, and whenever we encounter an unassigned index, assign it the
      next available character from ''a'' to ''z''. For each newly assigned index $i$,
      we also assign the same character to all indices $j > i$ where $LCP[i][j] > 0$.
      If we need more than 26 distinct characters, no such string exists, and we return
      an empty string.


      After constructing a candidate string, we must verify if it actually produces
      the given LCP matrix. We use the dynamic programming relation for LCP: if $word[i]
      == word[j]$, then $LCP[i][j] = 1 + LCP[i+1][j+1]$ (with boundary $LCP[n][n] =
      0$); otherwise, $LCP[i][j] = 0$. By iterating backwards and comparing the calculated
      LCP values with the input matrix, we ensure that every constraint, including symmetry,
      diagonal values ($LCP[i][i] = n-i$), and internal consistency, is satisfied. If
      the constructed string fails this check, we return an empty string.'
    time_complexity: O(n^2) where n is the length of the string. We iterate through
      the $n \times n$ matrix once for greedy character assignment and once more to
      validate the DP relationship of the LCP values.
    space_complexity: O(n) additional space to store the constructed candidate string
      of length n. The input matrix is $O(n^2)$, but it is provided by the problem and
      not counted as extra space.
    elapsed_time: 288.0401403903961
    model: gemini-3-flash-preview
    generated_at: '2026-03-28 01:30:12 '
---

## Problem #2573: Find the String with LCP

**Difficulty:** Hard

**Topics:** Array, String, Dynamic Programming, Greedy, Union-Find, Matrix

## Problem Description

<p>We define the <code>lcp</code> matrix of any <strong>0-indexed</strong> string <code>word</code> of <code>n</code> lowercase English letters as an <code>n x n</code> grid such that:</p>

<ul>
	<li><code>lcp[i][j]</code> is equal to the length of the <strong>longest common prefix</strong> between the substrings <code>word[i,n-1]</code> and <code>word[j,n-1]</code>.</li>
</ul>

<p>Given an&nbsp;<code>n x n</code> matrix <code>lcp</code>, return the alphabetically smallest string <code>word</code> that corresponds to <code>lcp</code>. If there is no such string, return an empty string.</p>

<p>A string <code>a</code> is lexicographically smaller than a string <code>b</code> (of the same length) if in the first position where <code>a</code> and <code>b</code> differ, string <code>a</code> has a letter that appears earlier in the alphabet than the corresponding letter in <code>b</code>. For example, <code>&quot;aabd&quot;</code> is lexicographically smaller than <code>&quot;aaca&quot;</code> because the first position they differ is at the third letter, and <code>&#39;b&#39;</code> comes before <code>&#39;c&#39;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
<strong>Output:</strong> &quot;abab&quot;
<strong>Explanation:</strong> lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is &quot;abab&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
<strong>Output:</strong> &quot;aaaa&quot;
<strong>Explanation:</strong> lcp corresponds to any 4 letter string with a single distinct letter. The lexicographically smallest of them is &quot;aaaa&quot;. 
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> lcp[3][3] cannot be equal to 3 since word[3,...,3] consists of only a single letter; Thus, no answer exists.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n ==&nbsp;</code><code>lcp.length == </code><code>lcp[i].length</code>&nbsp;<code>&lt;= 1000</code></li>
	<li><code><font face="monospace">0 &lt;= lcp[i][j] &lt;= n</font></code></li>
</ul>


## Hints

1. Use the LCP array to determine which groups of elements must be equal.

2. Match the smallest letter to the group that contains the smallest unassigned index.

3. Build the LCP matrix of the resulting string then check if it is equal to the target LCP.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks us to reconstruct a string from its LCP (Longest Common Prefix) matrix. The key observation is that $LCP[i][j] > 0$ if and only if the characters at indices $i$ and $j$ are identical ($word[i] = word[j]$). We can use this greedy property to build a candidate string: iterate through the indices from $0$ to $n-1$, and whenever we encounter an unassigned index, assign it the next available character from 'a' to 'z'. For each newly assigned index $i$, we also assign the same character to all indices $j > i$ where $LCP[i][j] > 0$. If we need more than 26 distinct characters, no such string exists, and we return an empty string.

After constructing a candidate string, we must verify if it actually produces the given LCP matrix. We use the dynamic programming relation for LCP: if $word[i] == word[j]$, then $LCP[i][j] = 1 + LCP[i+1][j+1]$ (with boundary $LCP[n][n] = 0$); otherwise, $LCP[i][j] = 0$. By iterating backwards and comparing the calculated LCP values with the input matrix, we ensure that every constraint, including symmetry, diagonal values ($LCP[i][i] = n-i$), and internal consistency, is satisfied. If the constructed string fails this check, we return an empty string.

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
    string findTheString(vector<vector<int>>& lcp) {
        int n = lcp.size();
        string s(n, '\0');
        char cur = 'a';
        for (int i = 0; i < n; ++i) {
            if (s[i] == '\0') {
                if (cur > 'z') return "";
                for (int j = i; j < n; ++j) {
                    if (lcp[i][j] > 0) s[j] = cur;
                }
                cur++;
            }
        }

        for (int i = 0; i < n; ++i) if (s[i] == '\0') return "";

        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                int expected = (s[i] == s[j]) ? ((i + 1 < n && j + 1 < n) ? lcp[i + 1][j + 1] + 1 : 1) : 0;
                if (lcp[i][j] != expected) return "";
            }
        }
        return s;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String findTheString(int[][] lcp) {
        int n = lcp.length;
        char[] s = new char[n];
        char cur = 'a';
        for (int i = 0; i < n; i++) {
            if (s[i] == 0) {
                if (cur > 'z') return "";
                for (int j = i; j < n; j++) {
                    if (lcp[i][j] > 0) s[j] = cur;
                }
                cur++;
            }
        }

        for (int i = 0; i < n; i++) if (s[i] == 0) return "";

        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int expected = (s[i] == s[j]) ? ((i + 1 < n && j + 1 < n) ? lcp[i + 1][j + 1] + 1 : 1) : 0;
                if (lcp[i][j] != expected) return "";
            }
        }
        return new String(s);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def findTheString(self, lcp):
        """
        :type lcp: List[List[int]]
        :rtype: str
        """
        n = len(lcp)
        res = [None] * n
        c = 0
        for i in range(n):
            if res[i] is None:
                if c >= 26: return ""
                char = chr(ord('a') + c)
                c += 1
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = char

        if None in res: return ""
        word = "".join(res)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if word[i] == word[j]:
                    expected = (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0) + 1
                if lcp[i][j] != expected:
                    return ""
        return word
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [None] * n
        c = 0
        for i in range(n):
            if res[i] is None:
                if c >= 26: return ""
                char = chr(ord('a') + c)
                c += 1
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = char

        if None in res: return ""
        word = "".join(res)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if word[i] == word[j]:
                    expected = (lcp[i + 1][j + 1] if (i + 1 < n and j + 1 < n) else 0) + 1
                if lcp[i][j] != expected:
                    return ""
        return word
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
char* findTheString(int** lcp, int n, int* lcpColSize) {
    char* s = (char*)calloc(n + 1, sizeof(char));
    char cur = 'a';
    for (int i = 0; i < n; i++) {
        if (s[i] == 0) {
            if (cur > 'z') {
                free(s);
                char* empty = (char*)calloc(1, 1);
                return empty;
            }
            for (int j = i; j < n; j++) {
                if (lcp[i][j] > 0) s[j] = cur;
            }
            cur++;
        }
    }
    for (int i = 0; i < n; i++) {
        if (s[i] == 0) {
            free(s);
            char* empty = (char*)calloc(1, 1);
            return empty;
        }
    }
    for (int i = n - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            int expected = (s[i] == s[j]) ? ((i + 1 < n && j + 1 < n) ? lcp[i + 1][j + 1] + 1 : 1) : 0;
            if (lcp[i][j] != expected) {
                free(s);
                char* empty = (char*)calloc(1, 1);
                return empty;
            }
        }
    }
    return s;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public string FindTheString(int[][] lcp) {
        int n = lcp.Length;
        char[] s = new char[n];
        char cur = 'a';
        for (int i = 0; i < n; i++) {
            if (s[i] == '\0') {
                if (cur > 'z') return "";
                for (int j = i; j < n; j++) {
                    if (lcp[i][j] > 0) s[j] = cur;
                }
                cur++;
            }
        }

        for (int i = 0; i < n; i++) if (s[i] == '\0') return "";

        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int expected = (s[i] == s[j]) ? ((i + 1 < n && j + 1 < n) ? lcp[i + 1][j + 1] + 1 : 1) : 0;
                if (lcp[i][j] != expected) return "";
            }
        }
        return new string(s);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} lcp
 * @return {string}
 */
var findTheString = function(lcp) {
    let n = lcp.length;
    let s = new Array(n).fill(null);
    let charCode = 97;
    for (let i = 0; i < n; i++) {
        if (s[i] === null) {
            if (charCode > 122) return "";
            let char = String.fromCharCode(charCode++);
            for (let j = i; j < n; j++) {
                if (lcp[i][j] > 0) s[j] = char;
            }
        }
    }
    for (let i = 0; i < n; i++) if (s[i] === null) return "";
    let word = s.join('');
    for (let i = n - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            let expected = 0;
            if (word[i] === word[j]) {
                expected = (i + 1 < n && j + 1 < n) ? lcp[i + 1][j + 1] + 1 : 1;
            }
            if (lcp[i][j] !== expected) return "";
        }
    }
    return word;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findTheString(lcp: number[][]): string {
    const n = lcp.length;
    const s: string[] = new Array(n).fill("");
    let charCode = 97;
    for (let i = 0; i < n; i++) {
        if (s[i] === "") {
            if (charCode > 122) return "";
            const char = String.fromCharCode(charCode++);
            for (let j = i; j < n; j++) {
                if (lcp[i][j] > 0) {
                    s[j] = char;
                }
            }
        }
    }
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            let expected = 0;
            if (s[i] === s[j]) {
                expected = 1;
                if (i + 1 < n && j + 1 < n) {
                    expected += lcp[i + 1][j + 1];
                }
            }
            if (lcp[i][j] !== expected) return "";
        }
    }
    return s.join("");
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $lcp
     * @return String
     */
    function findTheString($lcp) {
        $n = count($lcp);
        $s = array_fill(0, $n, '');
        $charCode = 97;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '') {
                if ($charCode > 122) return "";
                $char = chr($charCode++);
                for ($j = $i; $j < $n; $j++) {
                    if ($lcp[$i][$j] > 0) {
                        $s[$j] = $char;
                    }
                }
            }
        }
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $expected = 0;
                if ($s[$i] === $s[$j]) {
                    $expected = 1;
                    if ($i + 1 < $n && $j + 1 < $n) {
                        $expected += $lcp[$i + 1][$j + 1];
                    }
                }
                if ($lcp[$i][$j] !== $expected) return "";
            }
        }
        return implode('', $s);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findTheString(_ lcp: [[Int]]) -> String {
        let n = lcp.count
        var s = Array(repeating: Character(" "), count: n)
        var charCode: UInt8 = 97
        for i in 0..<n {
            if s[i] == " " {
                if charCode > 122 { return "" }
                let char = Character(UnicodeScalar(charCode))
                charCode += 1
                for j in i..<n {
                    if lcp[i][j] > 0 {
                        s[j] = char
                    }
                }
            }
        }
        for i in 0..<n {
            for j in 0..<n {
                var expected = 0
                if s[i] == s[j] {
                    expected = 1
                    if i + 1 < n && j + 1 < n {
                        expected += lcp[i + 1][j + 1]
                    }
                }
                if lcp[i][j] != expected {
                    return ""
                }
            }
        }
        return String(s)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findTheString(lcp: Array<IntArray>): String {
        val n = lcp.size
        val s = CharArray(n)
        var char = 'a'
        for (i in 0 until n) {
            if (s[i] == '\u0000') {
                if (char > 'z') return ""
                for (j in i until n) {
                    if (lcp[i][j] > 0) {
                        s[j] = char
                    }
                }
                char++
            }
        }
        for (i in 0 until n) {
            for (j in 0 until n) {
                var expected = 0
                if (s[i] == s[j]) {
                    expected = 1
                    if (i + 1 < n && j + 1 < n) {
                        expected += lcp[i + 1][j + 1]
                    }
                }
                if (lcp[i][j] != expected) return ""
            }
        }
        return String(s)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String findTheString(List<List<int>> lcp) {
    int n = lcp.length;
    List<String> s = List.filled(n, "");
    int charCode = 97;
    for (int i = 0; i < n; i++) {
      if (s[i] == "") {
        if (charCode > 122) return "";
        String char = String.fromCharCode(charCode++);
        for (int j = i; j < n; j++) {
          if (lcp[i][j] > 0) {
            s[j] = char;
          }
        }
      }
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int expected = 0;
        if (s[i] == s[j]) {
          expected = 1;
          if (i + 1 < n && j + 1 < n) {
            expected += lcp[i + 1][j + 1];
          }
        }
        if (lcp[i][j] != expected) return "";
      }
    }
    return s.join("");
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findTheString(lcp [][]int) string {
	n := len(lcp)
	s := make([]byte, n)
	curChar := byte('a')
	for i := 0; i < n; i++ {
		if s[i] == 0 {
			if curChar > 'z' {
				return ""
			}
			for j := i; j < n; j++ {
				if lcp[i][j] > 0 {
					s[j] = curChar
				}
			}
			curChar++
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
		expected := 0
		if s[i] == s[j] {
			expected = 1
			if i+1 < n && j+1 < n {
				expected += lcp[i+1][j+1]
			}
		}
		if lcp[i][j] != expected {
			return ""
		}
		}
	}
	return string(s)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def find_the_string(lcp)
  n = lcp.length
  word = Array.new(n)
  curr_char_code = 'a'.ord
  (0...n).each do |i|
    if word[i].nil?
      return "" if curr_char_code > 'z'.ord
      char = curr_char_code.chr
      (i...n).each do |j|
        if lcp[i][j] > 0
          word[j] = char if word[j].nil?
        end
      end
      curr_char_code += 1
    end
  end
  return "" if word.any?(&:nil?)
  dp = Array.new(n + 1) { Array.new(n + 1, 0) }
  (n - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      if word[i] == word[j]
        dp[i][j] = dp[i + 1][j + 1] + 1
      else
        dp[i][j] = 0
      end
      return "" if dp[i][j] != lcp[i][j]
    end
  end
  word.join
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def findTheString(lcp: Array[Array[Int]]): String = {
    val n = lcp.length
    val word = new Array[Char](n)
    var currChar = 'a'
    for (i <- 0 until n) {
      if (word(i) == '\u0000') {
        if (currChar > 'z') return ""
        for (j <- i until n) {
          if (lcp(i)(j) > 0) {
            if (word(j) == '\u0000') word(j) = currChar
          }
        }
        currChar = (currChar.toInt + 1).toChar
      }
    }
    if (word.contains('\u0000')) return ""
    val dp = Array.ofDim[Int](n + 1, n + 1)
    for (i <- n - 1 to 0 by -1) {
      for (j <- n - 1 to 0 by -1) {
        dp(i)(j) = if (word(i) == word(j)) dp(i + 1)(j + 1) + 1 else 0
        if (dp(i)(j) != lcp(i)(j)) return ""
      }
    }
    new String(word)
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_the_string(lcp: Vec<Vec<i32>>) -> String {
        let n = lcp.len();
        let mut word = vec![0u8; n];
        let mut curr_char = b'a';
        for i in 0..n {
            if word[i] == 0 {
                if curr_char > b'z' {
                    return "".to_string();
                }
                for j in i..n {
                    if lcp[i][j] > 0 {
                        if word[j] == 0 {
                            word[j] = curr_char;
                        }
                    }
                }
                curr_char += 1;
            }
        }
        if word.iter().any(|&c| c == 0) {
            return "".to_string();
        }
        let mut dp = vec![vec![0; n + 1]; n + 1];
        for i in (0..n).rev() {
            for j in (0..n).rev() {
                dp[i][j] = if word[i] == word[j] {
                    dp[i + 1][j + 1] + 1
                } else {
                    0
                };
                if dp[i][j] != lcp[i][j] {
                    return "".to_string();
                }
            }
        }
        String::from_utf8(word).unwrap_or_else(|_| "".to_string())
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-the-string lcp-list)
  (-> (listof (listof exact-integer?)) string?)
  (let* ([n (length lcp-list)]
         [lcp (apply vector (map (lambda (row) (apply vector row)) lcp-list))]
         [word (make-vector n #f)])
    (define (assign-chars)
      (let loop ([i 0] [code (char->integer #\a)])
        (cond
          [(= i n) #t]
          [(vector-ref word i) (loop (+ i 1) code)]
          [(> code (char->integer #\z)) #f]
          [else
           (for ([j (in-range i n)])
             (when (> (vector-ref (vector-ref lcp i) j) 0)
               (unless (vector-ref word j)
                 (vector-set! word j (integer->char code)))))
           (loop (+ i 1) (+ code 1))]))) 
    (if (and (assign-chars) (for/and ([i (in-range n)]) (vector-ref word i)))
        (let ([check-lcp (make-vector (+ n 1))])
          (for ([i (in-range (+ n 1))]) (vector-set! check-lcp i (make-vector (+ n 1) 0)))
          (let/ec return
            (for ([i (in-range (- n 1) -1 -1)])
              (for ([j (in-range (- n 1) -1 -1)])
                (let* ([v (if (char=? (vector-ref word i) (vector-ref word j))
                              (+ 1 (vector-ref (vector-ref check-lcp (+ i 1)) (+ j 1)))
                              0)])
                  (if (not (= v (vector-ref (vector-ref lcp i) j)))
                      (return "")
                      (vector-set! (vector-ref check-lcp i) j v)))))
            (list->string (vector->list word))))
        "")))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_the_string(Lcp :: [[integer()]]) -> unicode:unicode_binary().
find_the_string(LcpList) ->
  N = length(LcpList),
  Lcp = list_to_tuple([list_to_tuple(Row) || Row <- LcpList]),
  case assign_word(N, Lcp, 0, $a, #{}) of
    error -> <<>>;
    WordMap ->
      WordList = [maps:get(I, WordMap, undefined) || I <- lists:seq(0, N - 1)],
      case lists:any(fun(X) -> X == undefined end, WordList) of
        true -> <<>>;
        false ->
          WordTuple = list_to_tuple(WordList),
          case verify(N, Lcp, WordTuple) of
            true -> list_to_binary(WordList);
            false -> <<>>
          end
      end
  end.

assign_word(N, _Lcp, I, _Char, Acc) when I == N -> Acc;
assign_word(N, Lcp, I, Char, Acc) ->
  case maps:is_key(I, Acc) of
    true -> assign_word(N, Lcp, I + 1, Char, Acc);
    false ->
      if Char > $z -> error;
         true ->
           NewAcc = lists:foldl(fun(J, A) ->
             case element(J + 1, element(I + 1, Lcp)) > 0 of
               true -> maps:put_new(J, Char, A);
               false -> A
             end
           end, Acc, lists:seq(I, N - 1)),
           assign_word(N, Lcp, I + 1, Char + 1, NewAcc)
      end
  end.

verify(N, Lcp, WordTuple) ->
  try
    lists:foldl(fun(I, NextRowTuple) ->
      {RowI, _} = lists:foldr(fun(J, {AccRow, _}) ->
        Val = case element(I + 1, WordTuple) == element(J + 1, WordTuple) of
                true -> element(J + 2, NextRowTuple) + 1;
                false -> 0
              end,
        case Val == element(J + 1, element(I + 1, Lcp)) of
          true -> {[Val | AccRow], ok};
          false -> throw(error)
        end
      end, {[], ok}, lists:seq(0, N - 1)),
      list_to_tuple(RowI ++ [0])
    end, list_to_tuple(lists:duplicate(N + 1, 0)), lists:reverse(lists:seq(0, N - 1))),
    true
  catch
    error -> false
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_the_string(lcp :: [[integer]]) :: String.t
  def find_the_string(lcp_list) do
    n = length(lcp_list)
    lcp = lcp_list |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
    word_map = assign_word(n, lcp, 0, ?a, %{})
    if word_map == :error do
      ""
    else
      word_list = for i <- 0..(n-1), do: Map.get(word_map, i)
      if Enum.any?(word_list, &is_nil/1) do
        ""
      else
        word_t = List.to_tuple(word_list)
        if verify(n, lcp, word_t) do
          List.to_string(word_list)
        else
          ""
        end
      end
    end
  end

  defp assign_word(n, _lcp, i, _char, acc) when i == n, do: acc
  defp assign_word(n, lcp, i, char, acc) do
    if Map.has_key?(acc, i) do
      assign_word(n, lcp, i + 1, char, acc)
    else
      if char > ?z do
        :error
      else
        new_acc = Enum.reduce(i..(n-1), acc, fn j, a ->
          if elem(elem(lcp, i), j) > 0, do: Map.put_new(a, j, char), else: a
        end)
        assign_word(n, lcp, i + 1, char + 1, new_acc)
      end
    end
  end

  defp verify(n, lcp, word_t) do
    try do
      Enum.reduce((n-1)..0, List.to_tuple(List.duplicate(0, n + 1)), fn i, next_dp_row ->
        {curr_dp_list, _} = Enum.reduce((n-1)..0, {[], next_dp_row}, fn j, {acc, next_dp} ->
          val = if elem(word_t, i) == elem(word_t, j), do: elem(next_dp, j + 1) + 1, else: 0
          if val != elem(elem(lcp, i), j), do: throw(:error)
          {[val | acc], next_dp}
        end)
        List.to_tuple(curr_dp_list ++ [0])
      end)
      true
    catch
      :error -> false
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2) where n is the length of the string. We iterate through the $n \times n$ matrix once for greedy character assignment and once more to validate the DP relationship of the LCP values.
- **Space Complexity:** O(n) additional space to store the constructed candidate string of length n. The input matrix is $O(n^2)$, but it is provided by the problem and not counted as extra space.
