---
layout: post
title: "Process String with Special Operations II"
date: 2026-06-17 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["String", "Simulation"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/process-string-with-special-operations-ii/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      java: '// Generation failed for Java

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      python: '// Generation failed for Python

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      python3: '// Generation failed for Python3

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      c: '// Generation failed for C

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      csharp: '// Generation failed for C#

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      javascript: '// Generation failed for JavaScript

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      typescript: "function processStr(s: string, k: number): string {\n    const n\
        \ = s.length;\n    const L: number[] = new Array(n);\n    let currLen = 0;\n\
        \n    for (let i = 0; i < n; i++) {\n        const char = s[i];\n        if\
        \ (char >= 'a' && char <= 'z') {\n            currLen++;\n        } else if\
        \ (char === '*') {\n            if (currLen > 0) currLen--;\n        } else\
        \ if (char === '#') {\n            currLen *= 2;\n        } else if (char ===\
        \ '%') {\n            // Length remains unchanged\n        }\n        L[i] =\
        \ currLen;\n    }\n\n    if (k < 0 || k >= currLen) {\n        return \".\"\
        ;\n    }\n\n    let currentK = k;\n    for (let i = n - 1; i >= 0; i--) {\n\
        \        const char = s[i];\n        const prevLen = i > 0 ? L[i - 1] : 0;\n\
        \n        if (char >= 'a' && char <= 'z') {\n            if (currentK === prevLen)\
        \ {\n                return char;\n            }\n        } else if (char ===\
        \ '*') {\n            // currentK remains the same; it's within bounds of the\
        \ previous string\n        } else if (char === '#') {\n            if (prevLen\
        \ > 0) {\n                currentK %= prevLen;\n            }\n        } else\
        \ if (char === '%') {\n            if (prevLen > 0) {\n                currentK\
        \ = (prevLen - 1) - currentK;\n            }\n        }\n    }\n\n    return\
        \ \".\";\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param Integer\
        \ $k\n     * @return String\n     */\n    function processStr($s, $k) {\n  \
        \      $n = strlen($s);\n        $L = array_fill(0, $n, 0);\n        $currLen\
        \ = 0;\n\n        for ($i = 0; $i < $n; $i++) {\n            $char = $s[$i];\n\
        \            if ($char >= 'a' && $char <= 'z') {\n                $currLen++;\n\
        \            } else if ($char === '*') {\n                if ($currLen > 0)\
        \ $currLen--;\n            } else if ($char === '#') {\n                $currLen\
        \ *= 2;\n            } else if ($char === '%') {\n                // currLen\
        \ stays same\n            }\n            $L[$i] = $currLen;\n        }\n\n \
        \       if ($k < 0 || $k >= $currLen) {\n            return \".\";\n       \
        \ }\n\n        $currentK = $k;\n        for ($i = $n - 1; $i >= 0; $i--) {\n\
        \            $char = $s[$i];\n            $prevLen = $i > 0 ? $L[$i - 1] : 0;\n\
        \n            if ($char >= 'a' && $char <= 'z') {\n                if ($currentK\
        \ == $prevLen) {\n                    return $char;\n                }\n   \
        \         } else if ($char === '*') {\n                // currentK stays same\n\
        \            } else if ($char === '#') {\n                if ($prevLen > 0)\
        \ {\n                    $currentK %= $prevLen;\n                }\n       \
        \     } else if ($char === '%') {\n                if ($prevLen > 0) {\n   \
        \                 $currentK = ($prevLen - 1) - $currentK;\n                }\n\
        \            }\n        }\n\n        return \".\";\n    }\n}"
      swift: "class Solution {\n    func processStr(_ s: String, _ k: Int) -> Character\
        \ {\n        let n = s.count\n        let chars = Array(s)\n        var L =\
        \ [Int](repeating: 0, count: n)\n        var currLen = 0\n\n        for i in\
        \ 0..<n {\n            let char = chars[i]\n            if char >= \"a\" &&\
        \ char <= \"z\" {\n                currLen += 1\n            } else if char\
        \ == \"*\" {\n                if currLen > 0 {\n                    currLen\
        \ -= 1\n                }\n            } else if char == \"#\" {\n         \
        \       currLen *= 2\n            } else if char == \"%\" {\n              \
        \  // currLen stays same\n            }\n            L[i] = currLen\n      \
        \  }\n\n        if k < 0 || k >= currLen {\n            return \".\"\n     \
        \   }\n\n        var currentK = k\n        for i in stride(from: n - 1, through:\
        \ 0, by: -1) {\n            let char = chars[i]\n            let prevLen = i\
        \ > 0 ? L[i-1] : 0\n\n            if char >= \"a\" && char <= \"z\" {\n    \
        \            if currentK == prevLen {\n                    return char\n   \
        \             }\n            } else if char == \"*\" {\n                // currentK\
        \ stays same\n            } else if char == \"#\" {\n                if prevLen\
        \ > 0 {\n                    currentK %= prevLen\n                }\n      \
        \      } else if char == \"%\" {\n                if prevLen > 0 {\n       \
        \             currentK = (prevLen - 1) - currentK\n                }\n     \
        \       }\n        }\n\n        return \".\"\n    }\n}"
      kotlin: "class Solution {\n    fun processStr(s: String, k: Long): Char {\n  \
        \      val n = s.length\n        val L = LongArray(n)\n        var currLen =\
        \ 0L\n\n        for (i in 0 until n) {\n            val char = s[i]\n      \
        \      if (char in 'a'..'z') {\n                currLen++\n            } else\
        \ if (char == '*') {\n                if (currLen > 0) currLen--\n         \
        \   } else if (char == '#') {\n                currLen *= 2\n            } else\
        \ if (char == '%') {\n                // stays the same\n            }\n   \
        \         L[i] = currLen\n        }\n\n        if (k < 0 || k >= currLen) {\n\
        \            return '.'\n        }\n\n        var currentK = k\n        for\
        \ (i in n - 1 downTo 0) {\n            val char = s[i]\n            val prevLen\
        \ = if (i > 0) L[i - 1] else 0L\n\n            if (char in 'a'..'z') {\n   \
        \             if (currentK == prevLen) {\n                    return char\n\
        \                }\n            } else if (char == '*') {\n                //\
        \ currentK remains unchanged\n            } else if (char == '#') {\n      \
        \          if (prevLen > 0) {\n                    currentK %= prevLen\n   \
        \             }\n            } else if (char == '%') {\n                if (prevLen\
        \ > 0) {\n                    currentK = (prevLen - 1) - currentK\n        \
        \        }\n            }\n        }\n\n        return '.'\n    }\n}"
      dart: "class Solution {\n  String processStr(String s, int k) {\n    int n = s.length;\n\
        \    List<int> lengths = List<int>.filled(n, 0);\n    int currLen = 0;\n   \
        \ int charCodeA = 'a'.codeUnitAt(0);\n    int charCodeZ = 'z'.codeUnitAt(0);\n\
        \n    for (int i = 0; i < n; i++) {\n      int charCode = s.codeUnitAt(i);\n\
        \      if (charCode >= charCodeA && charCode <= charCodeZ) {\n        currLen++;\n\
        \      } else if (s[i] == '*') {\n        if (currLen > 0) {\n          currLen--;\n\
        \        }\n      } else if (s[i] == '#') {\n        currLen *= 2;\n      }\
        \ else if (s[i] == '%') {\n        // Length does not change\n      }\n    \
        \  lengths[i] = currLen;\n    }\n\n    if (k < 0 || k >= currLen) {\n      return\
        \ \".\";\n    }\n\n    int currentK = k;\n    for (int i = n - 1; i >= 0; i--)\
        \ {\n      int charCode = s.codeUnitAt(i);\n      int prevLen = (i > 0) ? lengths[i\
        \ - 1] : 0;\n\n      if (charCode >= charCodeA && charCode <= charCodeZ) {\n\
        \        if (currentK == lengths[i] - 1) {\n          return s[i];\n       \
        \ }\n      } else if (s[i] == '#') {\n        if (currentK >= prevLen) {\n \
        \         currentK -= prevLen;\n        }\n      } else if (s[i] == '%') {\n\
        \        currentK = (lengths[i] - 1) - currentK;\n      } else if (s[i] == '*')\
        \ {\n        // currentK remains currentK\n      }\n    }\n    return \".\"\
        ;\n  }\n}"
      go: "func processStr(s string, k int64) byte {\n\tn := len(s)\n\tlengths := make([]int64,\
        \ n)\n\tvar currLen int64 = 0\n\n\tfor i := 0; i < n; i++ {\n\t\tchar := s[i]\n\
        \t\tif char >= 'a' && char <= 'z' {\n\t\t\tcurrLen++\n\t\t} else if char ==\
        \ '*' {\n\t\t\tif currLen > 0 {\n\t\t\t\tcurrLen--\n\t\t\t}\n\t\t} else if char\
        \ == '#' {\n\t\t\tcurrLen *= 2\n\t\t} else if char == '%' {\n\t\t\t// length\
        \ remains currentLen\n\t\t}\n\t\tlengths[i] = currLen\n\t}\n\n\tif k < 0 ||\
        \ k >= currLen {\n\t\treturn '.'\n\t}\n\n\tcurrentK := k\n\tfor i := n - 1;\
        \ i >= 0; i-- {\n\t\tchar := s[i]\n\t\tvar prevLen int64 = 0\n\t\tif i > 0 {\n\
        \t\t\tprevLen = lengths[i-1]\n\t\t}\n\n\t\tif char >= 'a' && char <= 'z' {\n\
        \t\t\tif currentK == lengths[i]-1 {\n\t\t\t\treturn char\n\t\t\t}\n\t\t} else\
        \ if char == '#' {\n\t\t\tif currentK >= prevLen {\n\t\t\t\tcurrentK -= prevLen\n\
        \t\t\t}\n\t\t} else if char == '%' {\n\t\t\tcurrentK = (lengths[i] - 1) - currentK\n\
        \t\t} else if char == '*' {\n\t\t\t// currentK stays currentK\n\t\t}\n\t}\n\t\
        return '.'\n}"
      ruby: "# @param {String} s\n# @param {Integer} k\n# @return {Character}\ndef process_str(s,\
        \ k)\n  n = s.length\n  lengths = Array.new(n)\n  curr_len = 0\n\n  n.times\
        \ do |i|\n    char = s[i]\n    if char >= 'a' && char <= 'z'\n      curr_len\
        \ += 1\n    elsif char == '*'\n      curr_len -= 1 if curr_len > 0\n    elsif\
        \ char == '#'\n      curr_len *= 2\n    elsif char == '%'\n      # Length stays\
        \ same\n    end\n    lengths[i] = curr_len\n  end\n\n  return '.' if k < 0 ||\
        \ k >= curr_len\n\n  current_k = k\n  (n - 1).downto(0) do |i|\n    char = s[i]\n\
        \    prev_len = i > 0 ? lengths[i - 1] : 0\n\n    if char >= 'a' && char <=\
        \ 'z'\n      return char if current_k == lengths[i] - 1\n    elsif char == '#'\n\
        \      current_k -= prev_len if current_k >= prev_len\n    elsif char == '%'\n\
        \      current_k = (lengths[i] - 1) - current_k\n    elsif char == '*'\n   \
        \   # current_k stays current_k\n    end\n  end\n\n  '.'\nend"
      scala: "object Solution {\n  def processStr(s: String, k: Long): Char = {\n  \
        \  val n = s.length\n    val lengths = new Array[Long](n)\n    var currLen:\
        \ Long = 0\n\n    for (i <- 0 until n) {\n      val char = s(i)\n      if (char\
        \ >= 'a' && char <= 'z') {\n        currLen += 1\n      } else if (char == '*')\
        \ {\n        if (currLen > 0) currLen -= 1\n      } else if (char == '#') {\n\
        \        currLen *= 2\n      } else if (char == '%') {\n        // currLen stays\
        \ same\n      }\n      lengths(i) = currLen\n    }\n\n    if (k < 0 || k >=\
        \ currLen) {\n      return '.'\n    }\n\n    var currentK = k\n    for (i <-\
        \ n - 1 to 0 by -1) {\n      val char = s(i)\n      val prevLen: Long = if (i\
        \ > 0) lengths(i - 1) else 0\n\n      if (char >= 'a' && char <= 'z') {\n  \
        \      if (currentK == lengths(i) - 1) {\n          return char\n        }\n\
        \      } else if (char == '#') {\n        if (currentK >= prevLen) {\n     \
        \     currentK -= prevLen\n        }\n      } else if (char == '%') {\n    \
        \    currentK = (lengths(i) - 1) - currentK\n      } else if (char == '*') {\n\
        \        // currentK stays same\n      }\n    }\n    '.'\n  }\n}"
      rust: "impl Solution {\n    pub fn process_str(s: String, k: i64) -> char {\n\
        \        let n = s.len();\n        let mut lengths = vec![0i64; n];\n      \
        \  let s_chars: Vec<char> = s.chars().collect();\n\n        let mut current_len:\
        \ i64 = 0;\n        for i in 0..n {\n            current_len = match s_chars[i]\
        \ {\n                '*' => if current_len > 0 { current_len - 1 } else { 0\
        \ },\n                '#' => current_len * 2,\n                '%' => current_len,\n\
        \                _ => current_len + 1,\n            };\n            lengths[i]\
        \ = current_len;\n        }\n\n        if k < 0 || k >= current_len {\n    \
        \        return '.';\n        }\n\n        let mut curr_k = k;\n        for\
        \ i in (0..n).rev() {\n            let prev_len = if i == 0 { 0 } else { lengths[i\
        \ - 1] };\n            match s_chars[i] {\n                '*' => {\n      \
        \              // Index curr_k remains the same because '*' removed something\
        \ after it.\n                }\n                '#' => {\n                 \
        \   if curr_k >= prev_len {\n                        curr_k -= prev_len;\n \
        \                   }\n                }\n                '%' => {\n       \
        \             curr_k = (prev_len - 1) - curr_k;\n                }\n       \
        \         _ => {\n                    if curr_k == prev_len {\n            \
        \            return s_chars[i];\n                    }\n                   \
        \ // Otherwise, curr_k < prev_len, so character at curr_k didn't change.\n \
        \               }\n            }\n        }\n        '.'\n    }\n}"
      racket: "(define/contract (process-str s k)\n  (-> string? exact-integer? char?)\n\
        \  (let* ([n (string-length s)]\n         [lengths (make-vector n 0)]\n    \
        \     [final-len (let loop ([i 0] [curr-len 0])\n                      (if (<\
        \ i n)\n                          (let* ([ch (string-ref s i)]\n           \
        \                      [next-len (cond\n                                   \
        \          [(char=? ch #\\*) (if (> curr-len 0) (- curr-len 1) 0)]\n       \
        \                                      [(char=? ch #\\#) (* curr-len 2)]\n \
        \                                            [(char=? ch #\\%) curr-len]\n \
        \                                            [else (+ curr-len 1)])])\n    \
        \                        (vector-set! lengths i next-len)\n                \
        \            (loop (+ i 1) next-len))\n                          curr-len))])\n\
        \    (if (or (< k 0) (>= k final-len))\n        #\\.\n        (let find-k ([i\
        \ (- n 1)] [curr-k k])\n          (if (< i 0)\n              #\\.\n        \
        \      (let* ([ch (string-ref s i)]\n                     [prev-len (if (= i\
        \ 0) 0 (vector-ref lengths (- i 1)))])\n                (cond\n            \
        \      [(char=? ch #\\*) (find-k (- i 1) curr-k)]\n                  [(char=?\
        \ ch #\\#) \n                   (if (>= curr-k prev-len)\n                 \
        \      (find-k (- i 1) (- curr-k prev-len))\n                       (find-k\
        \ (- i 1) curr-k))]\n                  [(char=? ch #\\%) \n                \
        \   (find-k (- i 1) (- (- prev-len 1) curr-k))]\n                  [else\n \
        \                  (if (= curr-k prev-len)\n                       ch\n    \
        \                   (find-k (- i 1) curr-k))])))))))"
      erlang: "-spec process_str(S :: unicode:unicode_binary(), K :: integer()) -> char().\n\
        process_str(S, K) ->\n  SL = binary_to_list(S),\n  LengthsRev = calculate_lengths(SL,\
        \ 0, []),\n  FinalLen = case LengthsRev of\n    [H|_] -> H;\n    [] -> 0\n \
        \ end,\n  if\n    K < 0; K >= FinalLen -> $.;\n    true -> find_k(lists:reverse(SL),\
        \ K, LengthsRev)\n  end.\n\ncalculate_lengths([], _CurrLen, Acc) -> Acc;\ncalculate_lengths([H|T],\
        \ CurrLen, Acc) ->\n  NextLen = case H of\n    $* -> erlang:max(0, CurrLen -\
        \ 1);\n    $# -> CurrLen * 2;\n    $% -> CurrLen;\n    _  -> CurrLen + 1\n \
        \ end,\n  calculate_lengths(T, NextLen, [NextLen|Acc]).\n\nfind_k([H|ST], CurrK,\
        \ [_L|LT]) ->\n  PrevLen = case LT of\n    [PL|_] -> PL;\n    [] -> 0\n  end,\n\
        \  case H of\n    $* -> find_k(ST, CurrK, LT);\n    $# -> \n      if \n    \
        \    CurrK >= PrevLen -> find_k(ST, CurrK - PrevLen, LT);\n        true -> find_k(ST,\
        \ CurrK, LT)\n      end;\n    $% -> find_k(ST, (PrevLen - 1) - CurrK, LT);\n\
        \    _ -> \n      if \n        CurrK == PrevLen -> H;\n        true -> find_k(ST,\
        \ CurrK, LT)\n      end\n  end."
      elixir: "defmodule Solution do\n  @spec process_str(s :: String.t, k :: integer)\
        \ :: char\n  def process_str(s, k) do\n    chars = String.to_charlist(s)\n \
        \   lengths_rev = calculate_lengths(chars, 0, [])\n\n    final_len = case lengths_rev\
        \ do\n      [h | _] -> h\n      [] -> 0\n    end\n\n    if k < 0 or k >= final_len\
        \ do\n      ?.\n    else\n      find_k(Enum.reverse(chars), k, lengths_rev)\n\
        \    end\n  end\n\n  defp calculate_lengths([], _curr_len, acc), do: acc\n \
        \ defp calculate_lengths([h | t], curr_len, acc) do\n    next_len = case h do\n\
        \      ?* -> max(0, curr_len - 1)\n      ?# -> curr_len * 2\n      ?% -> curr_len\n\
        \      _  -> curr_len + 1\n    end\n    calculate_lengths(t, next_len, [next_len\
        \ | acc])\n  end\n\n  defp find_k([h | st], curr_k, [_l | lt]) do\n    prev_len\
        \ = case lt do\n      [pl | _] -> pl\n      [] -> 0\n    end\n\n    case h do\n\
        \      ?* -> find_k(st, curr_k, lt)\n      ?# ->\n        if curr_k >= prev_len\
        \ do\n          find_k(st, curr_k - prev_len, lt)\n        else\n          find_k(st,\
        \ curr_k, lt)\n        end\n      ?% ->\n        find_k(st, (prev_len - 1) -\
        \ curr_k, lt)\n      _ ->\n        if curr_k == prev_len do\n          h\n \
        \       else\n          find_k(st, curr_k, lt)\n        end\n    end\n  end\n\
        end"
    approach: 'The problem can be solved efficiently using a two-pass approach. In the
      first pass, we iterate through the input string forward to compute the length
      of the string after each operation. Since the rules define appending (length increases
      by 1), backspacing (length decreases by 1), duplicating (length doubles), and
      reversing (length remains the same), we can calculate and store these lengths
      in an array $L$. The constraints ensure that no intermediate or final string length
      exceeds $10^{15}$, which fits within standard 64-bit integer types.


      In the second pass, we determine the $k$th character by backtracking through the
      string $s$ from the end. If the operation was a character append and the current
      $k$ equals the length of the string before that append, we have found our character.
      For a duplication operation (#), we map the index $k$ back to the original string
      by taking $k = k \pmod{prev\_len}$. For a reverse operation (%), we mirror $k$
      by calculating its new position as $(prev\_len - 1) - k$. Backspacing (*) does
      not change $k$ because any index $k$ that was valid after a character was removed
      must have been valid at that same position before the removal. This strategy allows
      us to pinpoint the character in linear time without the exponential space and
      time required to actually build the string.'
    time_complexity: O(N) where N is the length of the string s. We perform one forward
      pass and one backward pass through the string, with each operation (arithmetic
      or character comparison) taking constant time.
    space_complexity: O(N) to store the array of lengths L for each operation in the
      string. All other variables used take constant space.
    elapsed_time: 825.0855219364166
    model: gemini-3-flash-preview
    generated_at: '2026-06-17 03:41:05 '
---

## Problem #3614: Process String with Special Operations II

**Difficulty:** Hard

**Topics:** String, Simulation

## Problem Description

<p>You are given a string <code>s</code> consisting of lowercase English letters and the special characters: <code>&#39;*&#39;</code>, <code>&#39;#&#39;</code>, and <code>&#39;%&#39;</code>.</p>

<p>You are also given an integer <code>k</code>.</p>

<p>Build a new string <code>result</code> by processing <code>s</code> according to the following rules from left to right:</p>

<ul>
	<li>If the letter is a <strong>lowercase</strong> English letter append it to <code>result</code>.</li>
	<li>A <code>&#39;*&#39;</code> <strong>removes</strong> the last character from <code>result</code>, if it exists.</li>
	<li>A <code>&#39;#&#39;</code> <strong>duplicates</strong> the current <code>result</code> and <strong>appends</strong> it to itself.</li>
	<li>A <code>&#39;%&#39;</code> <strong>reverses</strong> the current <code>result</code>.</li>
</ul>

<p>Return the <code>k<sup>th</sup></code> character of the final string <code>result</code>. If <code>k</code> is out of the bounds of <code>result</code>, return <code>&#39;.&#39;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;a#b%*&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;a&quot;</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>s[i]</code></th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Current <code>result</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>&#39;a&#39;</code></td>
			<td style="border: 1px solid black;">Append <code>&#39;a&#39;</code></td>
			<td style="border: 1px solid black;"><code>&quot;a&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>&#39;#&#39;</code></td>
			<td style="border: 1px solid black;">Duplicate <code>result</code></td>
			<td style="border: 1px solid black;"><code>&quot;aa&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>&#39;b&#39;</code></td>
			<td style="border: 1px solid black;">Append <code>&#39;b&#39;</code></td>
			<td style="border: 1px solid black;"><code>&quot;aab&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;"><code>&#39;%&#39;</code></td>
			<td style="border: 1px solid black;">Reverse <code>result</code></td>
			<td style="border: 1px solid black;"><code>&quot;baa&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;"><code>&#39;*&#39;</code></td>
			<td style="border: 1px solid black;">Remove the last character</td>
			<td style="border: 1px solid black;"><code>&quot;ba&quot;</code></td>
		</tr>
	</tbody>
</table>

<p>The final <code>result</code> is <code>&quot;ba&quot;</code>. The character at index <code>k = 1</code> is <code>&#39;a&#39;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;cd%#*#&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;d&quot;</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>s[i]</code></th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Current <code>result</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>&#39;c&#39;</code></td>
			<td style="border: 1px solid black;">Append <code>&#39;c&#39;</code></td>
			<td style="border: 1px solid black;"><code>&quot;c&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>&#39;d&#39;</code></td>
			<td style="border: 1px solid black;">Append <code>&#39;d&#39;</code></td>
			<td style="border: 1px solid black;"><code>&quot;cd&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>&#39;%&#39;</code></td>
			<td style="border: 1px solid black;">Reverse <code>result</code></td>
			<td style="border: 1px solid black;"><code>&quot;dc&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;"><code>&#39;#&#39;</code></td>
			<td style="border: 1px solid black;">Duplicate <code>result</code></td>
			<td style="border: 1px solid black;"><code>&quot;dcdc&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;"><code>&#39;*&#39;</code></td>
			<td style="border: 1px solid black;">Remove the last character</td>
			<td style="border: 1px solid black;"><code>&quot;dcd&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;"><code>&#39;#&#39;</code></td>
			<td style="border: 1px solid black;">Duplicate <code>result</code></td>
			<td style="border: 1px solid black;"><code>&quot;dcddcd&quot;</code></td>
		</tr>
	</tbody>
</table>

<p>The final <code>result</code> is <code>&quot;dcddcd&quot;</code>. The character at index <code>k = 3</code> is <code>&#39;d&#39;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;z*#&quot;, k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;.&quot;</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>s[i]</code></th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Current <code>result</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>&#39;z&#39;</code></td>
			<td style="border: 1px solid black;">Append <code>&#39;z&#39;</code></td>
			<td style="border: 1px solid black;"><code>&quot;z&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>&#39;*&#39;</code></td>
			<td style="border: 1px solid black;">Remove the last character</td>
			<td style="border: 1px solid black;"><code>&quot;&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>&#39;#&#39;</code></td>
			<td style="border: 1px solid black;">Duplicate the string</td>
			<td style="border: 1px solid black;"><code>&quot;&quot;</code></td>
		</tr>
	</tbody>
</table>

<p>The final <code>result</code> is <code>&quot;&quot;</code>. Since index <code>k = 0</code> is out of bounds, the output is <code>&#39;.&#39;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters and special characters <code>&#39;*&#39;</code>, <code>&#39;#&#39;</code>, and <code>&#39;%&#39;</code>.</li>
	<li><code>0 &lt;= k &lt;= 10<sup>15</sup></code></li>
	<li>The length of <code>result</code> after processing <code>s</code> will not exceed <code>10<sup>15</sup></code>.</li>
</ul>


## Hints

1. Track the length of the string after each operation on `s`.

2. Walk backwards through `s`, undoing each # by using modulus on the tracked lengths, and undoing each % by mirroring across the midpoint, to pinpoint the `k`th character.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved efficiently using a two-pass approach. In the first pass, we iterate through the input string forward to compute the length of the string after each operation. Since the rules define appending (length increases by 1), backspacing (length decreases by 1), duplicating (length doubles), and reversing (length remains the same), we can calculate and store these lengths in an array $L$. The constraints ensure that no intermediate or final string length exceeds $10^{15}$, which fits within standard 64-bit integer types.

In the second pass, we determine the $k$th character by backtracking through the string $s$ from the end. If the operation was a character append and the current $k$ equals the length of the string before that append, we have found our character. For a duplication operation (#), we map the index $k$ back to the original string by taking $k = k \pmod{prev\_len}$. For a reverse operation (%), we mirror $k$ by calculating its new position as $(prev\_len - 1) - k$. Backspacing (*) does not change $k$ because any index $k$ that was valid after a character was removed must have been valid at that same position before the removal. This strategy allows us to pinpoint the character in linear time without the exponential space and time required to actually build the string.

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
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function processStr(s: string, k: number): string {
    const n = s.length;
    const L: number[] = new Array(n);
    let currLen = 0;

    for (let i = 0; i < n; i++) {
        const char = s[i];
        if (char >= 'a' && char <= 'z') {
            currLen++;
        } else if (char === '*') {
            if (currLen > 0) currLen--;
        } else if (char === '#') {
            currLen *= 2;
        } else if (char === '%') {
            // Length remains unchanged
        }
        L[i] = currLen;
    }

    if (k < 0 || k >= currLen) {
        return ".";
    }

    let currentK = k;
    for (let i = n - 1; i >= 0; i--) {
        const char = s[i];
        const prevLen = i > 0 ? L[i - 1] : 0;

        if (char >= 'a' && char <= 'z') {
            if (currentK === prevLen) {
                return char;
            }
        } else if (char === '*') {
            // currentK remains the same; it's within bounds of the previous string
        } else if (char === '#') {
            if (prevLen > 0) {
                currentK %= prevLen;
            }
        } else if (char === '%') {
            if (prevLen > 0) {
                currentK = (prevLen - 1) - currentK;
            }
        }
    }

    return ".";
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
     * @return String
     */
    function processStr($s, $k) {
        $n = strlen($s);
        $L = array_fill(0, $n, 0);
        $currLen = 0;

        for ($i = 0; $i < $n; $i++) {
            $char = $s[$i];
            if ($char >= 'a' && $char <= 'z') {
                $currLen++;
            } else if ($char === '*') {
                if ($currLen > 0) $currLen--;
            } else if ($char === '#') {
                $currLen *= 2;
            } else if ($char === '%') {
                // currLen stays same
            }
            $L[$i] = $currLen;
        }

        if ($k < 0 || $k >= $currLen) {
            return ".";
        }

        $currentK = $k;
        for ($i = $n - 1; $i >= 0; $i--) {
            $char = $s[$i];
            $prevLen = $i > 0 ? $L[$i - 1] : 0;

            if ($char >= 'a' && $char <= 'z') {
                if ($currentK == $prevLen) {
                    return $char;
                }
            } else if ($char === '*') {
                // currentK stays same
            } else if ($char === '#') {
                if ($prevLen > 0) {
                    $currentK %= $prevLen;
                }
            } else if ($char === '%') {
                if ($prevLen > 0) {
                    $currentK = ($prevLen - 1) - $currentK;
                }
            }
        }

        return ".";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func processStr(_ s: String, _ k: Int) -> Character {
        let n = s.count
        let chars = Array(s)
        var L = [Int](repeating: 0, count: n)
        var currLen = 0

        for i in 0..<n {
            let char = chars[i]
            if char >= "a" && char <= "z" {
                currLen += 1
            } else if char == "*" {
                if currLen > 0 {
                    currLen -= 1
                }
            } else if char == "#" {
                currLen *= 2
            } else if char == "%" {
                // currLen stays same
            }
            L[i] = currLen
        }

        if k < 0 || k >= currLen {
            return "."
        }

        var currentK = k
        for i in stride(from: n - 1, through: 0, by: -1) {
            let char = chars[i]
            let prevLen = i > 0 ? L[i-1] : 0

            if char >= "a" && char <= "z" {
                if currentK == prevLen {
                    return char
                }
            } else if char == "*" {
                // currentK stays same
            } else if char == "#" {
                if prevLen > 0 {
                    currentK %= prevLen
                }
            } else if char == "%" {
                if prevLen > 0 {
                    currentK = (prevLen - 1) - currentK
                }
            }
        }

        return "."
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun processStr(s: String, k: Long): Char {
        val n = s.length
        val L = LongArray(n)
        var currLen = 0L

        for (i in 0 until n) {
            val char = s[i]
            if (char in 'a'..'z') {
                currLen++
            } else if (char == '*') {
                if (currLen > 0) currLen--
            } else if (char == '#') {
                currLen *= 2
            } else if (char == '%') {
                // stays the same
            }
            L[i] = currLen
        }

        if (k < 0 || k >= currLen) {
            return '.'
        }

        var currentK = k
        for (i in n - 1 downTo 0) {
            val char = s[i]
            val prevLen = if (i > 0) L[i - 1] else 0L

            if (char in 'a'..'z') {
                if (currentK == prevLen) {
                    return char
                }
            } else if (char == '*') {
                // currentK remains unchanged
            } else if (char == '#') {
                if (prevLen > 0) {
                    currentK %= prevLen
                }
            } else if (char == '%') {
                if (prevLen > 0) {
                    currentK = (prevLen - 1) - currentK
                }
            }
        }

        return '.'
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String processStr(String s, int k) {
    int n = s.length;
    List<int> lengths = List<int>.filled(n, 0);
    int currLen = 0;
    int charCodeA = 'a'.codeUnitAt(0);
    int charCodeZ = 'z'.codeUnitAt(0);

    for (int i = 0; i < n; i++) {
      int charCode = s.codeUnitAt(i);
      if (charCode >= charCodeA && charCode <= charCodeZ) {
        currLen++;
      } else if (s[i] == '*') {
        if (currLen > 0) {
          currLen--;
        }
      } else if (s[i] == '#') {
        currLen *= 2;
      } else if (s[i] == '%') {
        // Length does not change
      }
      lengths[i] = currLen;
    }

    if (k < 0 || k >= currLen) {
      return ".";
    }

    int currentK = k;
    for (int i = n - 1; i >= 0; i--) {
      int charCode = s.codeUnitAt(i);
      int prevLen = (i > 0) ? lengths[i - 1] : 0;

      if (charCode >= charCodeA && charCode <= charCodeZ) {
        if (currentK == lengths[i] - 1) {
          return s[i];
        }
      } else if (s[i] == '#') {
        if (currentK >= prevLen) {
          currentK -= prevLen;
        }
      } else if (s[i] == '%') {
        currentK = (lengths[i] - 1) - currentK;
      } else if (s[i] == '*') {
        // currentK remains currentK
      }
    }
    return ".";
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func processStr(s string, k int64) byte {
	n := len(s)
	lengths := make([]int64, n)
	var currLen int64 = 0

	for i := 0; i < n; i++ {
		char := s[i]
		if char >= 'a' && char <= 'z' {
			currLen++
		} else if char == '*' {
			if currLen > 0 {
				currLen--
			}
		} else if char == '#' {
			currLen *= 2
		} else if char == '%' {
			// length remains currentLen
		}
		lengths[i] = currLen
	}

	if k < 0 || k >= currLen {
		return '.'
	}

	currentK := k
	for i := n - 1; i >= 0; i-- {
		char := s[i]
		var prevLen int64 = 0
		if i > 0 {
			prevLen = lengths[i-1]
		}

		if char >= 'a' && char <= 'z' {
			if currentK == lengths[i]-1 {
				return char
			}
		} else if char == '#' {
			if currentK >= prevLen {
				currentK -= prevLen
			}
		} else if char == '%' {
			currentK = (lengths[i] - 1) - currentK
		} else if char == '*' {
			// currentK stays currentK
		}
	}
	return '.'
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {Integer} k
# @return {Character}
def process_str(s, k)
  n = s.length
  lengths = Array.new(n)
  curr_len = 0

  n.times do |i|
    char = s[i]
    if char >= 'a' && char <= 'z'
      curr_len += 1
    elsif char == '*'
      curr_len -= 1 if curr_len > 0
    elsif char == '#'
      curr_len *= 2
    elsif char == '%'
      # Length stays same
    end
    lengths[i] = curr_len
  end

  return '.' if k < 0 || k >= curr_len

  current_k = k
  (n - 1).downto(0) do |i|
    char = s[i]
    prev_len = i > 0 ? lengths[i - 1] : 0

    if char >= 'a' && char <= 'z'
      return char if current_k == lengths[i] - 1
    elsif char == '#'
      current_k -= prev_len if current_k >= prev_len
    elsif char == '%'
      current_k = (lengths[i] - 1) - current_k
    elsif char == '*'
      # current_k stays current_k
    end
  end

  '.'
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def processStr(s: String, k: Long): Char = {
    val n = s.length
    val lengths = new Array[Long](n)
    var currLen: Long = 0

    for (i <- 0 until n) {
      val char = s(i)
      if (char >= 'a' && char <= 'z') {
        currLen += 1
      } else if (char == '*') {
        if (currLen > 0) currLen -= 1
      } else if (char == '#') {
        currLen *= 2
      } else if (char == '%') {
        // currLen stays same
      }
      lengths(i) = currLen
    }

    if (k < 0 || k >= currLen) {
      return '.'
    }

    var currentK = k
    for (i <- n - 1 to 0 by -1) {
      val char = s(i)
      val prevLen: Long = if (i > 0) lengths(i - 1) else 0

      if (char >= 'a' && char <= 'z') {
        if (currentK == lengths(i) - 1) {
          return char
        }
      } else if (char == '#') {
        if (currentK >= prevLen) {
          currentK -= prevLen
        }
      } else if (char == '%') {
        currentK = (lengths(i) - 1) - currentK
      } else if (char == '*') {
        // currentK stays same
      }
    }
    '.'
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn process_str(s: String, k: i64) -> char {
        let n = s.len();
        let mut lengths = vec![0i64; n];
        let s_chars: Vec<char> = s.chars().collect();

        let mut current_len: i64 = 0;
        for i in 0..n {
            current_len = match s_chars[i] {
                '*' => if current_len > 0 { current_len - 1 } else { 0 },
                '#' => current_len * 2,
                '%' => current_len,
                _ => current_len + 1,
            };
            lengths[i] = current_len;
        }

        if k < 0 || k >= current_len {
            return '.';
        }

        let mut curr_k = k;
        for i in (0..n).rev() {
            let prev_len = if i == 0 { 0 } else { lengths[i - 1] };
            match s_chars[i] {
                '*' => {
                    // Index curr_k remains the same because '*' removed something after it.
                }
                '#' => {
                    if curr_k >= prev_len {
                        curr_k -= prev_len;
                    }
                }
                '%' => {
                    curr_k = (prev_len - 1) - curr_k;
                }
                _ => {
                    if curr_k == prev_len {
                        return s_chars[i];
                    }
                    // Otherwise, curr_k < prev_len, so character at curr_k didn't change.
                }
            }
        }
        '.'
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (process-str s k)
  (-> string? exact-integer? char?)
  (let* ([n (string-length s)]
         [lengths (make-vector n 0)]
         [final-len (let loop ([i 0] [curr-len 0])
                      (if (< i n)
                          (let* ([ch (string-ref s i)]
                                 [next-len (cond
                                             [(char=? ch #\*) (if (> curr-len 0) (- curr-len 1) 0)]
                                             [(char=? ch #\#) (* curr-len 2)]
                                             [(char=? ch #\%) curr-len]
                                             [else (+ curr-len 1)])])
                            (vector-set! lengths i next-len)
                            (loop (+ i 1) next-len))
                          curr-len))])
    (if (or (< k 0) (>= k final-len))
        #\.
        (let find-k ([i (- n 1)] [curr-k k])
          (if (< i 0)
              #\.
              (let* ([ch (string-ref s i)]
                     [prev-len (if (= i 0) 0 (vector-ref lengths (- i 1)))])
                (cond
                  [(char=? ch #\*) (find-k (- i 1) curr-k)]
                  [(char=? ch #\#) 
                   (if (>= curr-k prev-len)
                       (find-k (- i 1) (- curr-k prev-len))
                       (find-k (- i 1) curr-k))]
                  [(char=? ch #\%) 
                   (find-k (- i 1) (- (- prev-len 1) curr-k))]
                  [else
                   (if (= curr-k prev-len)
                       ch
                       (find-k (- i 1) curr-k))])))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec process_str(S :: unicode:unicode_binary(), K :: integer()) -> char().
process_str(S, K) ->
  SL = binary_to_list(S),
  LengthsRev = calculate_lengths(SL, 0, []),
  FinalLen = case LengthsRev of
    [H|_] -> H;
    [] -> 0
  end,
  if
    K < 0; K >= FinalLen -> $.;
    true -> find_k(lists:reverse(SL), K, LengthsRev)
  end.

calculate_lengths([], _CurrLen, Acc) -> Acc;
calculate_lengths([H|T], CurrLen, Acc) ->
  NextLen = case H of
    $* -> erlang:max(0, CurrLen - 1);
    $# -> CurrLen * 2;
    $% -> CurrLen;
    _  -> CurrLen + 1
  end,
  calculate_lengths(T, NextLen, [NextLen|Acc]).

find_k([H|ST], CurrK, [_L|LT]) ->
  PrevLen = case LT of
    [PL|_] -> PL;
    [] -> 0
  end,
  case H of
    $* -> find_k(ST, CurrK, LT);
    $# -> 
      if 
        CurrK >= PrevLen -> find_k(ST, CurrK - PrevLen, LT);
        true -> find_k(ST, CurrK, LT)
      end;
    $% -> find_k(ST, (PrevLen - 1) - CurrK, LT);
    _ -> 
      if 
        CurrK == PrevLen -> H;
        true -> find_k(ST, CurrK, LT)
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec process_str(s :: String.t, k :: integer) :: char
  def process_str(s, k) do
    chars = String.to_charlist(s)
    lengths_rev = calculate_lengths(chars, 0, [])

    final_len = case lengths_rev do
      [h | _] -> h
      [] -> 0
    end

    if k < 0 or k >= final_len do
      ?.
    else
      find_k(Enum.reverse(chars), k, lengths_rev)
    end
  end

  defp calculate_lengths([], _curr_len, acc), do: acc
  defp calculate_lengths([h | t], curr_len, acc) do
    next_len = case h do
      ?* -> max(0, curr_len - 1)
      ?# -> curr_len * 2
      ?% -> curr_len
      _  -> curr_len + 1
    end
    calculate_lengths(t, next_len, [next_len | acc])
  end

  defp find_k([h | st], curr_k, [_l | lt]) do
    prev_len = case lt do
      [pl | _] -> pl
      [] -> 0
    end

    case h do
      ?* -> find_k(st, curr_k, lt)
      ?# ->
        if curr_k >= prev_len do
          find_k(st, curr_k - prev_len, lt)
        else
          find_k(st, curr_k, lt)
        end
      ?% ->
        find_k(st, (prev_len - 1) - curr_k, lt)
      _ ->
        if curr_k == prev_len do
          h
        else
          find_k(st, curr_k, lt)
        end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the string s. We perform one forward pass and one backward pass through the string, with each operation (arithmetic or character comparison) taking constant time.
- **Space Complexity:** O(N) to store the array of lengths L for each operation in the string. All other variables used take constant space.
