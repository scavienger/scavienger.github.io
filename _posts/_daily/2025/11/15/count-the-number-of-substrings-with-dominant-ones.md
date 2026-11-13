---
layout: post
title: "Count the Number of Substrings With Dominant Ones"
date: 2025-11-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfSubstrings(string s) {\n    \
        \    int n = static_cast<int>(s.size());\n        vector<int> zeros;\n     \
        \   for (int i = 0; i < n; ++i) {\n            if (s[i] == '0') {\n        \
        \        zeros.push_back(i);\n            }\n        }\n\n        long long\
        \ answer = 0;\n        int zeroCount = static_cast<int>(zeros.size());\n   \
        \     for (int left = 0; left < n; ++left) {\n            int first = lower_bound(zeros.begin(),\
        \ zeros.end(), left) - zeros.begin();\n            int onesBeforeFirstZero =\
        \ (first < zeroCount ? zeros[first] : n) - left;\n            answer += onesBeforeFirstZero;\n\
        \n            for (int k = first; k < zeroCount; ++k) {\n                int\
        \ countZeros = k - first + 1;\n                long long minLength = 1LL * countZeros\
        \ * countZeros + countZeros;\n                int nextZero = (k + 1 < zeroCount\
        \ ? zeros[k + 1] : n);\n                int maxLength = nextZero - left;\n \
        \               if (minLength <= maxLength) {\n                    int minEnd\
        \ = left + static_cast<int>(minLength) - 1;\n                    answer += nextZero\
        \ - max(minEnd, zeros[k]);\n                }\n                if (minLength\
        \ > n - left) break;\n            }\n        }\n        return static_cast<int>(answer);\n\
        \    }\n};"
      java: "class Solution {\n    public int numberOfSubstrings(String s) {\n     \
        \   int n = s.length();\n        int[] zeros = new int[n];\n        int zeroCount\
        \ = 0;\n        for (int i = 0; i < n; i++) {\n            if (s.charAt(i) ==\
        \ '0') {\n                zeros[zeroCount++] = i;\n            }\n        }\n\
        \n        long answer = 0;\n        for (int left = 0; left < n; left++) {\n\
        \            int first = 0;\n            while (first < zeroCount && zeros[first]\
        \ < left) {\n                first++;\n            }\n            int firstZeroPosition\
        \ = first < zeroCount ? zeros[first] : n;\n            answer += firstZeroPosition\
        \ - left;\n\n            for (int k = first; k < zeroCount; k++) {\n       \
        \         int countZeros = k - first + 1;\n                long minLength =\
        \ (long) countZeros * countZeros + countZeros;\n                int nextZero\
        \ = k + 1 < zeroCount ? zeros[k + 1] : n;\n                int maxLength = nextZero\
        \ - left;\n                if (minLength <= maxLength) {\n                 \
        \   int minEnd = left + (int) minLength - 1;\n                    answer +=\
        \ nextZero - Math.max(minEnd, zeros[k]);\n                }\n              \
        \  if (minLength > n - left) {\n                    break;\n               \
        \ }\n            }\n        }\n        return (int) answer;\n    }\n}"
      python: "class Solution(object):\n    def numberOfSubstrings(self, s):\n     \
        \   \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n    \
        \    n = len(s)\n        zeros = [i for i, char in enumerate(s) if char == '0']\n\
        \        answer = 0\n        zero_count = len(zeros)\n\n        for left in\
        \ range(n):\n            first = 0\n            while first < zero_count and\
        \ zeros[first] < left:\n                first += 1\n            first_zero_position\
        \ = zeros[first] if first < zero_count else n\n            answer += first_zero_position\
        \ - left\n\n            for k in range(first, zero_count):\n               \
        \ count_zeros = k - first + 1\n                min_length = count_zeros * count_zeros\
        \ + count_zeros\n                next_zero = zeros[k + 1] if k + 1 < zero_count\
        \ else n\n                max_length = next_zero - left\n                if\
        \ min_length <= max_length:\n                    min_end = left + min_length\
        \ - 1\n                    answer += next_zero - max(min_end, zeros[k])\n  \
        \              if min_length > n - left:\n                    break\n      \
        \  return answer"
      python3: "class Solution:\n    def numberOfSubstrings(self, s: str) -> int:\n\
        \        n = len(s)\n        zeros = [i for i, char in enumerate(s) if char\
        \ == '0']\n        answer = 0\n        zero_count = len(zeros)\n\n        for\
        \ left in range(n):\n            first = 0\n            while first < zero_count\
        \ and zeros[first] < left:\n                first += 1\n            first_zero_position\
        \ = zeros[first] if first < zero_count else n\n            answer += first_zero_position\
        \ - left\n\n            for k in range(first, zero_count):\n               \
        \ count_zeros = k - first + 1\n                min_length = count_zeros * count_zeros\
        \ + count_zeros\n                next_zero = zeros[k + 1] if k + 1 < zero_count\
        \ else n\n                max_length = next_zero - left\n                if\
        \ min_length <= max_length:\n                    min_end = left + min_length\
        \ - 1\n                    answer += next_zero - max(min_end, zeros[k])\n  \
        \              if min_length > n - left:\n                    break\n      \
        \  return answer"
      c: "int numberOfSubstrings(char* s) {\n    int n = 0;\n    while (s[n] != '\\\
        0') {\n        n++;\n    }\n\n    int* zeros = (int*)malloc((size_t)n * sizeof(int));\n\
        \    int zeroCount = 0;\n    for (int i = 0; i < n; i++) {\n        if (s[i]\
        \ == '0') {\n            zeros[zeroCount++] = i;\n        }\n    }\n\n    long\
        \ long answer = 0;\n    for (int left = 0; left < n; left++) {\n        int\
        \ first = 0;\n        while (first < zeroCount && zeros[first] < left) {\n \
        \           first++;\n        }\n        int firstZeroPosition = first < zeroCount\
        \ ? zeros[first] : n;\n        answer += firstZeroPosition - left;\n\n     \
        \   for (int k = first; k < zeroCount; k++) {\n            int countZeros =\
        \ k - first + 1;\n            long long minLength = (long long)countZeros *\
        \ countZeros + countZeros;\n            int nextZero = k + 1 < zeroCount ? zeros[k\
        \ + 1] : n;\n            int maxLength = nextZero - left;\n            if (minLength\
        \ <= maxLength) {\n                int minEnd = left + (int)minLength - 1;\n\
        \                int startEnd = minEnd > zeros[k] ? minEnd : zeros[k];\n   \
        \             answer += nextZero - startEnd;\n            }\n            if\
        \ (minLength > n - left) {\n                break;\n            }\n        }\n\
        \    }\n\n    free(zeros);\n    return (int)answer;\n}"
      csharp: "public class Solution {\n    public int NumberOfSubstrings(string s)\
        \ {\n        int n = s.Length;\n        List<int> zeros = new List<int>();\n\
        \        for (int i = 0; i < n; i++) {\n            if (s[i] == '0') {\n   \
        \             zeros.Add(i);\n            }\n        }\n\n        long answer\
        \ = 0;\n        int zeroCount = zeros.Count;\n        int first = 0;\n\n   \
        \     for (int left = 0; left < n; left++) {\n            while (first < zeroCount\
        \ && zeros[first] < left) {\n                first++;\n            }\n\n   \
        \         int firstZeroPosition = first < zeroCount ? zeros[first] : n;\n  \
        \          answer += firstZeroPosition - left;\n\n            for (int k = first;\
        \ k < zeroCount; k++) {\n                int countZeros = k - first + 1;\n \
        \               int minLength = countZeros * countZeros + countZeros;\n    \
        \            int nextZero = k + 1 < zeroCount ? zeros[k + 1] : n;\n        \
        \        int maxLength = nextZero - left;\n                if (minLength <=\
        \ maxLength) {\n                    int minEnd = left + minLength - 1;\n   \
        \                 answer += nextZero - Math.Max(minEnd, zeros[k]);\n       \
        \         }\n                if (minLength > n - left) {\n                 \
        \   break;\n                }\n            }\n        }\n\n        return (int)answer;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar numberOfSubstrings\
        \ = function(s) {\n    const n = s.length;\n    const zeros = [];\n    for (let\
        \ i = 0; i < n; i++) {\n        if (s[i] === '0') {\n            zeros.push(i);\n\
        \        }\n    }\n\n    let answer = 0;\n    let first = 0;\n\n    for (let\
        \ left = 0; left < n; left++) {\n        while (first < zeros.length && zeros[first]\
        \ < left) {\n            first++;\n        }\n\n        const firstZeroPosition\
        \ = first < zeros.length ? zeros[first] : n;\n        answer += firstZeroPosition\
        \ - left;\n\n        for (let k = first; k < zeros.length; k++) {\n        \
        \    const countZeros = k - first + 1;\n            const minLength = countZeros\
        \ * countZeros + countZeros;\n            const nextZero = k + 1 < zeros.length\
        \ ? zeros[k + 1] : n;\n            const maxLength = nextZero - left;\n    \
        \        if (minLength <= maxLength) {\n                const minEnd = left\
        \ + minLength - 1;\n                answer += nextZero - Math.max(minEnd, zeros[k]);\n\
        \            }\n            if (minLength > n - left) {\n                break;\n\
        \            }\n        }\n    }\n\n    return answer;\n};"
      typescript: "function numberOfSubstrings(s: string): number {\n    const n = s.length;\n\
        \    const zeros: number[] = [];\n    for (let i = 0; i < n; i++) {\n      \
        \  if (s[i] === '0') {\n            zeros.push(i);\n        }\n    }\n\n   \
        \ let answer = 0;\n    let first = 0;\n\n    for (let left = 0; left < n; left++)\
        \ {\n        while (first < zeros.length && zeros[first] < left) {\n       \
        \     first++;\n        }\n\n        const firstZeroPosition = first < zeros.length\
        \ ? zeros[first] : n;\n        answer += firstZeroPosition - left;\n\n     \
        \   for (let k = first; k < zeros.length; k++) {\n            const countZeros\
        \ = k - first + 1;\n            const minLength = countZeros * countZeros +\
        \ countZeros;\n            const nextZero = k + 1 < zeros.length ? zeros[k +\
        \ 1] : n;\n            const maxLength = nextZero - left;\n            if (minLength\
        \ <= maxLength) {\n                const minEnd = left + minLength - 1;\n  \
        \              answer += nextZero - Math.max(minEnd, zeros[k]);\n          \
        \  }\n            if (minLength > n - left) {\n                break;\n    \
        \        }\n        }\n    }\n\n    return answer;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function numberOfSubstrings($s) {\n        $n = strlen($s);\n\
        \        $zeros = [];\n        for ($i = 0; $i < $n; $i++) {\n            if\
        \ ($s[$i] === '0') {\n                $zeros[] = $i;\n            }\n      \
        \  }\n\n        $answer = 0;\n        $zeroCount = count($zeros);\n        $first\
        \ = 0;\n\n        for ($left = 0; $left < $n; $left++) {\n            while\
        \ ($first < $zeroCount && $zeros[$first] < $left) {\n                $first++;\n\
        \            }\n\n            $firstZeroPosition = $first < $zeroCount ? $zeros[$first]\
        \ : $n;\n            $answer += $firstZeroPosition - $left;\n\n            for\
        \ ($k = $first; $k < $zeroCount; $k++) {\n                $countZeros = $k -\
        \ $first + 1;\n                $minLength = $countZeros * $countZeros + $countZeros;\n\
        \                $nextZero = $k + 1 < $zeroCount ? $zeros[$k + 1] : $n;\n  \
        \              $maxLength = $nextZero - $left;\n                if ($minLength\
        \ <= $maxLength) {\n                    $minEnd = $left + $minLength - 1;\n\
        \                    $answer += $nextZero - max($minEnd, $zeros[$k]);\n    \
        \            }\n                if ($minLength > $n - $left) {\n           \
        \         break;\n                }\n            }\n        }\n\n        return\
        \ $answer;\n    }\n}"
      swift: "class Solution {\n    func numberOfSubstrings(_ s: String) -> Int {\n\
        \        let chars = Array(s)\n        let n = chars.count\n        var zeros:\
        \ [Int] = []\n        for i in 0..<n {\n            if chars[i] == \"0\" {\n\
        \                zeros.append(i)\n            }\n        }\n\n        var answer\
        \ = 0\n        var first = 0\n\n        for left in 0..<n {\n            while\
        \ first < zeros.count && zeros[first] < left {\n                first += 1\n\
        \            }\n\n            let firstZeroPosition = first < zeros.count ?\
        \ zeros[first] : n\n            answer += firstZeroPosition - left\n\n     \
        \       for k in first..<zeros.count {\n                let countZeros = k -\
        \ first + 1\n                let minLength = countZeros * countZeros + countZeros\n\
        \                let nextZero = k + 1 < zeros.count ? zeros[k + 1] : n\n   \
        \             let maxLength = nextZero - left\n                if minLength\
        \ <= maxLength {\n                    let minEnd = left + minLength - 1\n  \
        \                  answer += nextZero - max(minEnd, zeros[k])\n            \
        \    }\n                if minLength > n - left {\n                    break\n\
        \                }\n            }\n        }\n\n        return answer\n    }\n\
        }"
      kotlin: "class Solution {\n    fun numberOfSubstrings(s: String): Int {\n    \
        \    val n = s.length\n        val zeros = mutableListOf<Int>()\n        for\
        \ (i in s.indices) {\n            if (s[i] == '0') zeros.add(i)\n        }\n\
        \        var answer = 0\n        var first = 0\n\n        for (left in 0 until\
        \ n) {\n            while (first < zeros.size && zeros[first] < left) first++\n\
        \            val firstZeroPosition = if (first < zeros.size) zeros[first] else\
        \ n\n            answer += firstZeroPosition - left\n\n            for (k in\
        \ first until zeros.size) {\n                val countZeros = k - first + 1\n\
        \                val minLength = countZeros * countZeros + countZeros\n    \
        \            val nextZero = if (k + 1 < zeros.size) zeros[k + 1] else n\n  \
        \              val maxLength = nextZero - left\n                if (minLength\
        \ <= maxLength) {\n                    val minEnd = left + minLength - 1\n \
        \                   answer += nextZero - maxOf(minEnd, zeros[k])\n         \
        \       }\n                if (minLength > n - left) break\n            }\n\
        \        }\n        return answer\n    }\n}"
      dart: "class Solution {\n  int numberOfSubstrings(String s) {\n    final n = s.length;\n\
        \    final zeros = <int>[];\n    for (var i = 0; i < n; i++) {\n      if (s[i]\
        \ == '0') zeros.add(i);\n    }\n\n    var answer = 0;\n    var first = 0;\n\
        \    for (var left = 0; left < n; left++) {\n      while (first < zeros.length\
        \ && zeros[first] < left) {\n        first++;\n      }\n      final firstZeroPosition\
        \ = first < zeros.length ? zeros[first] : n;\n      answer += firstZeroPosition\
        \ - left;\n\n      for (var k = first; k < zeros.length; k++) {\n        final\
        \ countZeros = k - first + 1;\n        final minLength = countZeros * countZeros\
        \ + countZeros;\n        final nextZero = k + 1 < zeros.length ? zeros[k + 1]\
        \ : n;\n        final maxLength = nextZero - left;\n        if (minLength <=\
        \ maxLength) {\n          final minEnd = left + minLength - 1;\n          answer\
        \ += nextZero - (minEnd > zeros[k] ? minEnd : zeros[k]);\n        }\n      \
        \  if (minLength > n - left) break;\n      }\n    }\n    return answer;\n  }\n\
        }"
      go: "func numberOfSubstrings(s string) int {\n\tn := len(s)\n\tzeros := make([]int,\
        \ 0)\n\tfor i := 0; i < n; i++ {\n\t\tif s[i] == '0' {\n\t\t\tzeros = append(zeros,\
        \ i)\n\t\t}\n\t}\n\n\tanswer := 0\n\tfirst := 0\n\tfor left := 0; left < n;\
        \ left++ {\n\t\tfor first < len(zeros) && zeros[first] < left {\n\t\t\tfirst++\n\
        \t\t}\n\t\tfirstZeroPosition := n\n\t\tif first < len(zeros) {\n\t\t\tfirstZeroPosition\
        \ = zeros[first]\n\t\t}\n\t\tanswer += firstZeroPosition - left\n\n\t\tfor k\
        \ := first; k < len(zeros); k++ {\n\t\t\tcountZeros := k - first + 1\n\t\t\t\
        minLength := countZeros*countZeros + countZeros\n\t\t\tnextZero := n\n\t\t\t\
        if k+1 < len(zeros) {\n\t\t\t\tnextZero = zeros[k+1]\n\t\t\t}\n\t\t\tmaxLength\
        \ := nextZero - left\n\t\t\tif minLength <= maxLength {\n\t\t\t\tminEnd := left\
        \ + minLength - 1\n\t\t\t\tif zeros[k] > minEnd {\n\t\t\t\t\tminEnd = zeros[k]\n\
        \t\t\t\t}\n\t\t\t\tanswer += nextZero - minEnd\n\t\t\t}\n\t\t\tif minLength\
        \ > n-left {\n\t\t\t\tbreak\n\t\t\t}\n\t\t}\n\t}\n\treturn answer\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef number_of_substrings(s)\n\
        \  n = s.length\n  zeros = []\n  s.each_char.with_index do |char, i|\n    zeros\
        \ << i if char == '0'\n  end\n\n  answer = 0\n  first = 0\n  (0...n).each do\
        \ |left|\n    first += 1 while first < zeros.length && zeros[first] < left\n\
        \    first_zero_position = first < zeros.length ? zeros[first] : n\n    answer\
        \ += first_zero_position - left\n\n    (first...zeros.length).each do |k|\n\
        \      count_zeros = k - first + 1\n      min_length = count_zeros * count_zeros\
        \ + count_zeros\n      next_zero = k + 1 < zeros.length ? zeros[k + 1] : n\n\
        \      max_length = next_zero - left\n      if min_length <= max_length\n  \
        \      min_end = left + min_length - 1\n        min_end = [min_end, zeros[k]].max\n\
        \        answer += next_zero - min_end\n      end\n      break if min_length\
        \ > n - left\n    end\n  end\n  answer\nend"
      scala: "object Solution {\n    def numberOfSubstrings(s: String): Int = {\n  \
        \      val n = s.length\n        val zeros = s.indices.filter(i => s(i) == '0').toArray\n\
        \        var answer = 0\n        var first = 0\n\n        for (left <- 0 until\
        \ n) {\n            while (first < zeros.length && zeros(first) < left) {\n\
        \                first += 1\n            }\n            val firstZeroPosition\
        \ = if (first < zeros.length) zeros(first) else n\n            answer += firstZeroPosition\
        \ - left\n\n            var k = first\n            while (k < zeros.length)\
        \ {\n                val countZeros = k - first + 1\n                val minLength\
        \ = countZeros * countZeros + countZeros\n                val nextZero = if\
        \ (k + 1 < zeros.length) zeros(k + 1) else n\n                val maxLength\
        \ = nextZero - left\n                if (minLength <= maxLength) {\n       \
        \             val minEnd = left + minLength - 1\n                    answer\
        \ += nextZero - math.max(minEnd, zeros(k))\n                }\n            \
        \    if (minLength > n - left) {\n                    k = zeros.length\n   \
        \             } else {\n                    k += 1\n                }\n    \
        \        }\n        }\n        answer\n    }\n}"
      rust: "impl Solution {\n    pub fn number_of_substrings(s: String) -> i32 {\n\
        \        let bytes = s.as_bytes();\n        let n = bytes.len();\n        let\
        \ zeros: Vec<usize> = bytes\n            .iter()\n            .enumerate()\n\
        \            .filter_map(|(i, &byte)| if byte == b'0' { Some(i) } else { None\
        \ })\n            .collect();\n        let mut answer: i64 = 0;\n\n        for\
        \ left in 0..n {\n            let first = zeros.partition_point(|&position|\
        \ position < left);\n            let first_zero_position = zeros.get(first).copied().unwrap_or(n);\n\
        \            answer += (first_zero_position - left) as i64;\n\n            for\
        \ k in first..zeros.len() {\n                let count_zeros = k - first + 1;\n\
        \                let min_length = count_zeros * count_zeros + count_zeros;\n\
        \                if min_length > n - left {\n                    break;\n  \
        \              }\n                let next_zero = zeros.get(k + 1).copied().unwrap_or(n);\n\
        \                let max_length = next_zero - left;\n                if min_length\
        \ <= max_length {\n                    let min_end = left + min_length - 1;\n\
        \                    answer += (next_zero - min_end.max(zeros[k])) as i64;\n\
        \                }\n            }\n        }\n\n        answer as i32\n    }\n\
        }"
      racket: "(define/contract (number-of-substrings s)\n  (-> string? exact-integer?)\n\
        \  (let* ([n (string-length s)]\n         [zeros (for/list ([i (in-range n)]\
        \ #:when (char=? (string-ref s i) #\\0)) i)]\n         [zero-vector (list->vector\
        \ zeros)]\n         [zero-count (vector-length zero-vector)])\n    (for*/sum\
        \ ([left (in-range n)])\n      (let* ([first (let loop ([lo 0] [hi zero-count])\n\
        \                      (if (< lo hi)\n                          (let ([mid (quotient\
        \ (+ lo hi) 2)])\n                            (if (< (vector-ref zero-vector\
        \ mid) left)\n                                (loop (add1 mid) hi)\n       \
        \                         (loop lo mid)))\n                          lo))]\n\
        \             [first-zero-position (if (< first zero-count)\n              \
        \                        (vector-ref zero-vector first)\n                  \
        \                    n)])\n        (+ (- first-zero-position left)\n       \
        \    (let loop ([k first] [total 0])\n             (if (< k zero-count)\n  \
        \               (let* ([count-zeros (add1 (- k first))]\n                  \
        \      [min-length (+ (* count-zeros count-zeros) count-zeros)])\n         \
        \          (if (> min-length (- n left))\n                       total\n   \
        \                    (let* ([next-zero (if (< (add1 k) zero-count)\n       \
        \                                      (vector-ref zero-vector (add1 k))\n \
        \                                            n)]\n                         \
        \     [min-end (+ left min-length -1)]\n                              [contribution\
        \ (if (<= min-length (- next-zero left))\n                                 \
        \               (- next-zero (max min-end (vector-ref zero-vector k)))\n   \
        \                                             0)])\n                       \
        \  (loop (add1 k) (+ total contribution)))))\n                 total))))))"
      erlang: "-spec number_of_substrings(S :: unicode:unicode_binary()) -> integer().\n\
        number_of_substrings(S) ->\n  N = byte_size(S),\n  Zeros = [I || I <- lists:seq(0,\
        \ N - 1), binary:at(S, I) =:= $0],\n  Count = length(Zeros),\n  ZeroTuple =\
        \ list_to_tuple(Zeros),\n  number_of_substrings_left(0, N, Count, ZeroTuple,\
        \ 0).\n\nnumber_of_substrings_left(Left, N, _Count, _Zeros, Answer) when Left\
        \ >= N ->\n  Answer;\nnumber_of_substrings_left(Left, N, Count, Zeros, Answer)\
        \ ->\n  First = first_zero_at_least(1, Count, Left, Zeros),\n  FirstPosition\
        \ = if First =< Count -> element(First, Zeros); true -> N end,\n  NoZeroCount\
        \ = FirstPosition - Left,\n  Added = count_zero_groups(First, Count, Left, N,\
        \ Zeros, 0),\n  number_of_substrings_left(Left + 1, N, Count, Zeros, Answer\
        \ + NoZeroCount + Added).\n\nfirst_zero_at_least(Index, Count, _Left, _Zeros)\
        \ when Index > Count ->\n  Index;\nfirst_zero_at_least(Index, Count, Left, Zeros)\
        \ ->\n  case element(Index, Zeros) < Left of\n    true -> first_zero_at_least(Index\
        \ + 1, Count, Left, Zeros);\n    false -> Index\n  end.\n\ncount_zero_groups(K,\
        \ Count, _Left, _N, _Zeros, Total) when K > Count ->\n  Total;\ncount_zero_groups(K,\
        \ Count, Left, N, Zeros, Total) ->\n  CountZeros = K - first_zero_at_least(1,\
        \ Count, Left, Zeros) + 1,\n  MinLength = CountZeros * CountZeros + CountZeros,\n\
        \  case MinLength > N - Left of\n    true -> Total;\n    false ->\n      NextZero\
        \ = if K < Count -> element(K + 1, Zeros); true -> N end,\n      MaxLength =\
        \ NextZero - Left,\n      Contribution = if MinLength =< MaxLength ->\n    \
        \                     MinEnd = Left + MinLength - 1,\n                     \
        \    ZeroPosition = element(K, Zeros),\n                         NextZero -\
        \ max(MinEnd, ZeroPosition);\n                     true -> 0\n             \
        \        end,\n      count_zero_groups(K + 1, Count, Left, N, Zeros, Total +\
        \ Contribution)\n  end."
      elixir: "defmodule Solution do\n  @spec number_of_substrings(s :: String.t) ::\
        \ integer\n  def number_of_substrings(s) do\n    n = byte_size(s)\n    zeros\
        \ = for i <- 0..(n - 1), :binary.at(s, i) == ?0, do: i\n    zero_count = length(zeros)\n\
        \    zero_tuple = List.to_tuple(zeros)\n\n    Enum.reduce(0..(n - 1), 0, fn\
        \ left, answer ->\n      first = first_zero_at_least(zero_tuple, zero_count,\
        \ left, 0, zero_count)\n      first_zero_position = if first < zero_count, do:\
        \ elem(zero_tuple, first), else: n\n      no_zero_count = first_zero_position\
        \ - left\n      added = count_zero_groups(first, zero_count, left, n, zero_tuple,\
        \ 0)\n      answer + no_zero_count + added\n    end)\n  end\n\n  defp first_zero_at_least(_zeros,\
        \ _count, _left, lo, hi) when lo >= hi, do: lo\n\n  defp first_zero_at_least(zeros,\
        \ count, left, lo, hi) do\n    mid = div(lo + hi, 2)\n\n    if mid < count and\
        \ elem(zeros, mid) < left do\n      first_zero_at_least(zeros, count, left,\
        \ mid + 1, hi)\n    else\n      first_zero_at_least(zeros, count, left, lo,\
        \ mid)\n    end\n  end\n\n  defp count_zero_groups(k, count, _left, _n, _zeros,\
        \ total) when k >= count, do: total\n\n  defp count_zero_groups(k, count, left,\
        \ n, zeros, total) do\n    count_zeros = k - first_zero_at_least(zeros, count,\
        \ left, 0, count) + 1\n    min_length = count_zeros * count_zeros + count_zeros\n\
        \n    if min_length > n - left do\n      total\n    else\n      next_zero =\
        \ if k + 1 < count, do: elem(zeros, k + 1), else: n\n      max_length = next_zero\
        \ - left\n\n      contribution =\n        if min_length <= max_length do\n \
        \         min_end = left + min_length - 1\n          next_zero - max(min_end,\
        \ elem(zeros, k))\n        else\n          0\n        end\n\n      count_zero_groups(k\
        \ + 1, count, left, n, zeros, total + contribution)\n    end\n  end\nend"
    approach: 'For each starting index, count substrings by their number of zeros. Substrings
      with no zeros are all valid, so count the consecutive ones beginning at that index
      directly. A substring with z zeros can be dominant only if its length is at least
      z squared plus z, which means z is at most about the square root of the string
      length.


      Precompute the positions of all zeros, then for each start, visit each feasible
      number of zeros and use the next zero positions to determine the range of ends
      containing exactly that many zeros. The minimum valid end follows from the condition
      ones >= zeros squared; count the valid ends in the range and add them to the answer.'
    time_complexity: O(n sqrt(n)), where n is the string length; each start considers
      at most O(sqrt(n)) zero counts.
    space_complexity: O(n) for storing zero positions.
    elapsed_time: 138.9407877922058
    model: gpt-6-luna
    generated_at: '2026-11-13 00:02:23 '
---

## Problem #3234: Count the Number of Substrings With Dominant Ones

**Difficulty:** Medium

**Topics:** String, Enumeration

## Problem Description

<p>You are given a binary string <code>s</code>.</p>

<p>Return the number of <span data-keyword="substring-nonempty">substrings</span> with <strong>dominant</strong> ones.</p>

<p>A string has <strong>dominant</strong> ones if the number of ones in the string is <strong>greater than or equal to</strong> the <strong>square</strong> of the number of zeros in the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;00011&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The substrings with dominant ones are shown in the table below.</p>
</div>

<table>
	<thead>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>s[i..j]</th>
			<th>Number of Zeros</th>
			<th>Number of Ones</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>3</td>
			<td>3</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>3</td>
			<td>01</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>4</td>
			<td>11</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>4</td>
			<td>011</td>
			<td>1</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;101101&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>The substrings with <strong>non-dominant</strong> ones are shown in the table below.</p>

<p>Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.</p>
</div>

<table>
	<thead>
		<tr>
			<th>i</th>
			<th>j</th>
			<th>s[i..j]</th>
			<th>Number of Zeros</th>
			<th>Number of Ones</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>4</td>
			<td>4</td>
			<td>0</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>1</td>
			<td>4</td>
			<td>0110</td>
			<td>2</td>
			<td>2</td>
		</tr>
		<tr>
			<td>0</td>
			<td>4</td>
			<td>10110</td>
			<td>2</td>
			<td>3</td>
		</tr>
		<tr>
			<td>1</td>
			<td>5</td>
			<td>01101</td>
			<td>2</td>
			<td>3</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists only of characters <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. Let us fix the starting index `l` of the substring and count the number of indices `r` such that `l <= r` and the substring `s[l..r]` has dominant ones.

2. A substring with dominant ones has at most `sqrt(n)` zeros.

3. We cannot iterate over every `r` and check if the  `s[l..r]` has dominant ones. Instead, we iterate over the next `sqrt(n)` zeros to the left of `l` and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

For each starting index, count substrings by their number of zeros. Substrings with no zeros are all valid, so count the consecutive ones beginning at that index directly. A substring with z zeros can be dominant only if its length is at least z squared plus z, which means z is at most about the square root of the string length.

Precompute the positions of all zeros, then for each start, visit each feasible number of zeros and use the next zero positions to determine the range of ends containing exactly that many zeros. The minimum valid end follows from the condition ones >= zeros squared; count the valid ends in the range and add them to the answer.

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
    int numberOfSubstrings(string s) {
        int n = static_cast<int>(s.size());
        vector<int> zeros;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '0') {
                zeros.push_back(i);
            }
        }

        long long answer = 0;
        int zeroCount = static_cast<int>(zeros.size());
        for (int left = 0; left < n; ++left) {
            int first = lower_bound(zeros.begin(), zeros.end(), left) - zeros.begin();
            int onesBeforeFirstZero = (first < zeroCount ? zeros[first] : n) - left;
            answer += onesBeforeFirstZero;

            for (int k = first; k < zeroCount; ++k) {
                int countZeros = k - first + 1;
                long long minLength = 1LL * countZeros * countZeros + countZeros;
                int nextZero = (k + 1 < zeroCount ? zeros[k + 1] : n);
                int maxLength = nextZero - left;
                if (minLength <= maxLength) {
                    int minEnd = left + static_cast<int>(minLength) - 1;
                    answer += nextZero - max(minEnd, zeros[k]);
                }
                if (minLength > n - left) break;
            }
        }
        return static_cast<int>(answer);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numberOfSubstrings(String s) {
        int n = s.length();
        int[] zeros = new int[n];
        int zeroCount = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0') {
                zeros[zeroCount++] = i;
            }
        }

        long answer = 0;
        for (int left = 0; left < n; left++) {
            int first = 0;
            while (first < zeroCount && zeros[first] < left) {
                first++;
            }
            int firstZeroPosition = first < zeroCount ? zeros[first] : n;
            answer += firstZeroPosition - left;

            for (int k = first; k < zeroCount; k++) {
                int countZeros = k - first + 1;
                long minLength = (long) countZeros * countZeros + countZeros;
                int nextZero = k + 1 < zeroCount ? zeros[k + 1] : n;
                int maxLength = nextZero - left;
                if (minLength <= maxLength) {
                    int minEnd = left + (int) minLength - 1;
                    answer += nextZero - Math.max(minEnd, zeros[k]);
                }
                if (minLength > n - left) {
                    break;
                }
            }
        }
        return (int) answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        zeros = [i for i, char in enumerate(s) if char == '0']
        answer = 0
        zero_count = len(zeros)

        for left in range(n):
            first = 0
            while first < zero_count and zeros[first] < left:
                first += 1
            first_zero_position = zeros[first] if first < zero_count else n
            answer += first_zero_position - left

            for k in range(first, zero_count):
                count_zeros = k - first + 1
                min_length = count_zeros * count_zeros + count_zeros
                next_zero = zeros[k + 1] if k + 1 < zero_count else n
                max_length = next_zero - left
                if min_length <= max_length:
                    min_end = left + min_length - 1
                    answer += next_zero - max(min_end, zeros[k])
                if min_length > n - left:
                    break
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [i for i, char in enumerate(s) if char == '0']
        answer = 0
        zero_count = len(zeros)

        for left in range(n):
            first = 0
            while first < zero_count and zeros[first] < left:
                first += 1
            first_zero_position = zeros[first] if first < zero_count else n
            answer += first_zero_position - left

            for k in range(first, zero_count):
                count_zeros = k - first + 1
                min_length = count_zeros * count_zeros + count_zeros
                next_zero = zeros[k + 1] if k + 1 < zero_count else n
                max_length = next_zero - left
                if min_length <= max_length:
                    min_end = left + min_length - 1
                    answer += next_zero - max(min_end, zeros[k])
                if min_length > n - left:
                    break
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numberOfSubstrings(char* s) {
    int n = 0;
    while (s[n] != '\0') {
        n++;
    }

    int* zeros = (int*)malloc((size_t)n * sizeof(int));
    int zeroCount = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '0') {
            zeros[zeroCount++] = i;
        }
    }

    long long answer = 0;
    for (int left = 0; left < n; left++) {
        int first = 0;
        while (first < zeroCount && zeros[first] < left) {
            first++;
        }
        int firstZeroPosition = first < zeroCount ? zeros[first] : n;
        answer += firstZeroPosition - left;

        for (int k = first; k < zeroCount; k++) {
            int countZeros = k - first + 1;
            long long minLength = (long long)countZeros * countZeros + countZeros;
            int nextZero = k + 1 < zeroCount ? zeros[k + 1] : n;
            int maxLength = nextZero - left;
            if (minLength <= maxLength) {
                int minEnd = left + (int)minLength - 1;
                int startEnd = minEnd > zeros[k] ? minEnd : zeros[k];
                answer += nextZero - startEnd;
            }
            if (minLength > n - left) {
                break;
            }
        }
    }

    free(zeros);
    return (int)answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumberOfSubstrings(string s) {
        int n = s.Length;
        List<int> zeros = new List<int>();
        for (int i = 0; i < n; i++) {
            if (s[i] == '0') {
                zeros.Add(i);
            }
        }

        long answer = 0;
        int zeroCount = zeros.Count;
        int first = 0;

        for (int left = 0; left < n; left++) {
            while (first < zeroCount && zeros[first] < left) {
                first++;
            }

            int firstZeroPosition = first < zeroCount ? zeros[first] : n;
            answer += firstZeroPosition - left;

            for (int k = first; k < zeroCount; k++) {
                int countZeros = k - first + 1;
                int minLength = countZeros * countZeros + countZeros;
                int nextZero = k + 1 < zeroCount ? zeros[k + 1] : n;
                int maxLength = nextZero - left;
                if (minLength <= maxLength) {
                    int minEnd = left + minLength - 1;
                    answer += nextZero - Math.Max(minEnd, zeros[k]);
                }
                if (minLength > n - left) {
                    break;
                }
            }
        }

        return (int)answer;
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
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const n = s.length;
    const zeros = [];
    for (let i = 0; i < n; i++) {
        if (s[i] === '0') {
            zeros.push(i);
        }
    }

    let answer = 0;
    let first = 0;

    for (let left = 0; left < n; left++) {
        while (first < zeros.length && zeros[first] < left) {
            first++;
        }

        const firstZeroPosition = first < zeros.length ? zeros[first] : n;
        answer += firstZeroPosition - left;

        for (let k = first; k < zeros.length; k++) {
            const countZeros = k - first + 1;
            const minLength = countZeros * countZeros + countZeros;
            const nextZero = k + 1 < zeros.length ? zeros[k + 1] : n;
            const maxLength = nextZero - left;
            if (minLength <= maxLength) {
                const minEnd = left + minLength - 1;
                answer += nextZero - Math.max(minEnd, zeros[k]);
            }
            if (minLength > n - left) {
                break;
            }
        }
    }

    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfSubstrings(s: string): number {
    const n = s.length;
    const zeros: number[] = [];
    for (let i = 0; i < n; i++) {
        if (s[i] === '0') {
            zeros.push(i);
        }
    }

    let answer = 0;
    let first = 0;

    for (let left = 0; left < n; left++) {
        while (first < zeros.length && zeros[first] < left) {
            first++;
        }

        const firstZeroPosition = first < zeros.length ? zeros[first] : n;
        answer += firstZeroPosition - left;

        for (let k = first; k < zeros.length; k++) {
            const countZeros = k - first + 1;
            const minLength = countZeros * countZeros + countZeros;
            const nextZero = k + 1 < zeros.length ? zeros[k + 1] : n;
            const maxLength = nextZero - left;
            if (minLength <= maxLength) {
                const minEnd = left + minLength - 1;
                answer += nextZero - Math.max(minEnd, zeros[k]);
            }
            if (minLength > n - left) {
                break;
            }
        }
    }

    return answer;
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
     * @return Integer
     */
    function numberOfSubstrings($s) {
        $n = strlen($s);
        $zeros = [];
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') {
                $zeros[] = $i;
            }
        }

        $answer = 0;
        $zeroCount = count($zeros);
        $first = 0;

        for ($left = 0; $left < $n; $left++) {
            while ($first < $zeroCount && $zeros[$first] < $left) {
                $first++;
            }

            $firstZeroPosition = $first < $zeroCount ? $zeros[$first] : $n;
            $answer += $firstZeroPosition - $left;

            for ($k = $first; $k < $zeroCount; $k++) {
                $countZeros = $k - $first + 1;
                $minLength = $countZeros * $countZeros + $countZeros;
                $nextZero = $k + 1 < $zeroCount ? $zeros[$k + 1] : $n;
                $maxLength = $nextZero - $left;
                if ($minLength <= $maxLength) {
                    $minEnd = $left + $minLength - 1;
                    $answer += $nextZero - max($minEnd, $zeros[$k]);
                }
                if ($minLength > $n - $left) {
                    break;
                }
            }
        }

        return $answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numberOfSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var zeros: [Int] = []
        for i in 0..<n {
            if chars[i] == "0" {
                zeros.append(i)
            }
        }

        var answer = 0
        var first = 0

        for left in 0..<n {
            while first < zeros.count && zeros[first] < left {
                first += 1
            }

            let firstZeroPosition = first < zeros.count ? zeros[first] : n
            answer += firstZeroPosition - left

            for k in first..<zeros.count {
                let countZeros = k - first + 1
                let minLength = countZeros * countZeros + countZeros
                let nextZero = k + 1 < zeros.count ? zeros[k + 1] : n
                let maxLength = nextZero - left
                if minLength <= maxLength {
                    let minEnd = left + minLength - 1
                    answer += nextZero - max(minEnd, zeros[k])
                }
                if minLength > n - left {
                    break
                }
            }
        }

        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numberOfSubstrings(s: String): Int {
        val n = s.length
        val zeros = mutableListOf<Int>()
        for (i in s.indices) {
            if (s[i] == '0') zeros.add(i)
        }
        var answer = 0
        var first = 0

        for (left in 0 until n) {
            while (first < zeros.size && zeros[first] < left) first++
            val firstZeroPosition = if (first < zeros.size) zeros[first] else n
            answer += firstZeroPosition - left

            for (k in first until zeros.size) {
                val countZeros = k - first + 1
                val minLength = countZeros * countZeros + countZeros
                val nextZero = if (k + 1 < zeros.size) zeros[k + 1] else n
                val maxLength = nextZero - left
                if (minLength <= maxLength) {
                    val minEnd = left + minLength - 1
                    answer += nextZero - maxOf(minEnd, zeros[k])
                }
                if (minLength > n - left) break
            }
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numberOfSubstrings(String s) {
    final n = s.length;
    final zeros = <int>[];
    for (var i = 0; i < n; i++) {
      if (s[i] == '0') zeros.add(i);
    }

    var answer = 0;
    var first = 0;
    for (var left = 0; left < n; left++) {
      while (first < zeros.length && zeros[first] < left) {
        first++;
      }
      final firstZeroPosition = first < zeros.length ? zeros[first] : n;
      answer += firstZeroPosition - left;

      for (var k = first; k < zeros.length; k++) {
        final countZeros = k - first + 1;
        final minLength = countZeros * countZeros + countZeros;
        final nextZero = k + 1 < zeros.length ? zeros[k + 1] : n;
        final maxLength = nextZero - left;
        if (minLength <= maxLength) {
          final minEnd = left + minLength - 1;
          answer += nextZero - (minEnd > zeros[k] ? minEnd : zeros[k]);
        }
        if (minLength > n - left) break;
      }
    }
    return answer;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numberOfSubstrings(s string) int {
	n := len(s)
	zeros := make([]int, 0)
	for i := 0; i < n; i++ {
		if s[i] == '0' {
			zeros = append(zeros, i)
		}
	}

	answer := 0
	first := 0
	for left := 0; left < n; left++ {
		for first < len(zeros) && zeros[first] < left {
			first++
		}
		firstZeroPosition := n
		if first < len(zeros) {
			firstZeroPosition = zeros[first]
		}
		answer += firstZeroPosition - left

		for k := first; k < len(zeros); k++ {
			countZeros := k - first + 1
			minLength := countZeros*countZeros + countZeros
			nextZero := n
			if k+1 < len(zeros) {
				nextZero = zeros[k+1]
			}
			maxLength := nextZero - left
			if minLength <= maxLength {
				minEnd := left + minLength - 1
				if zeros[k] > minEnd {
					minEnd = zeros[k]
				}
				answer += nextZero - minEnd
			}
			if minLength > n-left {
				break
			}
		}
	}
	return answer
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def number_of_substrings(s)
  n = s.length
  zeros = []
  s.each_char.with_index do |char, i|
    zeros << i if char == '0'
  end

  answer = 0
  first = 0
  (0...n).each do |left|
    first += 1 while first < zeros.length && zeros[first] < left
    first_zero_position = first < zeros.length ? zeros[first] : n
    answer += first_zero_position - left

    (first...zeros.length).each do |k|
      count_zeros = k - first + 1
      min_length = count_zeros * count_zeros + count_zeros
      next_zero = k + 1 < zeros.length ? zeros[k + 1] : n
      max_length = next_zero - left
      if min_length <= max_length
        min_end = left + min_length - 1
        min_end = [min_end, zeros[k]].max
        answer += next_zero - min_end
      end
      break if min_length > n - left
    end
  end
  answer
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numberOfSubstrings(s: String): Int = {
        val n = s.length
        val zeros = s.indices.filter(i => s(i) == '0').toArray
        var answer = 0
        var first = 0

        for (left <- 0 until n) {
            while (first < zeros.length && zeros(first) < left) {
                first += 1
            }
            val firstZeroPosition = if (first < zeros.length) zeros(first) else n
            answer += firstZeroPosition - left

            var k = first
            while (k < zeros.length) {
                val countZeros = k - first + 1
                val minLength = countZeros * countZeros + countZeros
                val nextZero = if (k + 1 < zeros.length) zeros(k + 1) else n
                val maxLength = nextZero - left
                if (minLength <= maxLength) {
                    val minEnd = left + minLength - 1
                    answer += nextZero - math.max(minEnd, zeros(k))
                }
                if (minLength > n - left) {
                    k = zeros.length
                } else {
                    k += 1
                }
            }
        }
        answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let zeros: Vec<usize> = bytes
            .iter()
            .enumerate()
            .filter_map(|(i, &byte)| if byte == b'0' { Some(i) } else { None })
            .collect();
        let mut answer: i64 = 0;

        for left in 0..n {
            let first = zeros.partition_point(|&position| position < left);
            let first_zero_position = zeros.get(first).copied().unwrap_or(n);
            answer += (first_zero_position - left) as i64;

            for k in first..zeros.len() {
                let count_zeros = k - first + 1;
                let min_length = count_zeros * count_zeros + count_zeros;
                if min_length > n - left {
                    break;
                }
                let next_zero = zeros.get(k + 1).copied().unwrap_or(n);
                let max_length = next_zero - left;
                if min_length <= max_length {
                    let min_end = left + min_length - 1;
                    answer += (next_zero - min_end.max(zeros[k])) as i64;
                }
            }
        }

        answer as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (number-of-substrings s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [zeros (for/list ([i (in-range n)] #:when (char=? (string-ref s i) #\0)) i)]
         [zero-vector (list->vector zeros)]
         [zero-count (vector-length zero-vector)])
    (for*/sum ([left (in-range n)])
      (let* ([first (let loop ([lo 0] [hi zero-count])
                      (if (< lo hi)
                          (let ([mid (quotient (+ lo hi) 2)])
                            (if (< (vector-ref zero-vector mid) left)
                                (loop (add1 mid) hi)
                                (loop lo mid)))
                          lo))]
             [first-zero-position (if (< first zero-count)
                                      (vector-ref zero-vector first)
                                      n)])
        (+ (- first-zero-position left)
           (let loop ([k first] [total 0])
             (if (< k zero-count)
                 (let* ([count-zeros (add1 (- k first))]
                        [min-length (+ (* count-zeros count-zeros) count-zeros)])
                   (if (> min-length (- n left))
                       total
                       (let* ([next-zero (if (< (add1 k) zero-count)
                                             (vector-ref zero-vector (add1 k))
                                             n)]
                              [min-end (+ left min-length -1)]
                              [contribution (if (<= min-length (- next-zero left))
                                                (- next-zero (max min-end (vector-ref zero-vector k)))
                                                0)])
                         (loop (add1 k) (+ total contribution)))))
                 total))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec number_of_substrings(S :: unicode:unicode_binary()) -> integer().
number_of_substrings(S) ->
  N = byte_size(S),
  Zeros = [I || I <- lists:seq(0, N - 1), binary:at(S, I) =:= $0],
  Count = length(Zeros),
  ZeroTuple = list_to_tuple(Zeros),
  number_of_substrings_left(0, N, Count, ZeroTuple, 0).

number_of_substrings_left(Left, N, _Count, _Zeros, Answer) when Left >= N ->
  Answer;
number_of_substrings_left(Left, N, Count, Zeros, Answer) ->
  First = first_zero_at_least(1, Count, Left, Zeros),
  FirstPosition = if First =< Count -> element(First, Zeros); true -> N end,
  NoZeroCount = FirstPosition - Left,
  Added = count_zero_groups(First, Count, Left, N, Zeros, 0),
  number_of_substrings_left(Left + 1, N, Count, Zeros, Answer + NoZeroCount + Added).

first_zero_at_least(Index, Count, _Left, _Zeros) when Index > Count ->
  Index;
first_zero_at_least(Index, Count, Left, Zeros) ->
  case element(Index, Zeros) < Left of
    true -> first_zero_at_least(Index + 1, Count, Left, Zeros);
    false -> Index
  end.

count_zero_groups(K, Count, _Left, _N, _Zeros, Total) when K > Count ->
  Total;
count_zero_groups(K, Count, Left, N, Zeros, Total) ->
  CountZeros = K - first_zero_at_least(1, Count, Left, Zeros) + 1,
  MinLength = CountZeros * CountZeros + CountZeros,
  case MinLength > N - Left of
    true -> Total;
    false ->
      NextZero = if K < Count -> element(K + 1, Zeros); true -> N end,
      MaxLength = NextZero - Left,
      Contribution = if MinLength =< MaxLength ->
                         MinEnd = Left + MinLength - 1,
                         ZeroPosition = element(K, Zeros),
                         NextZero - max(MinEnd, ZeroPosition);
                     true -> 0
                     end,
      count_zero_groups(K + 1, Count, Left, N, Zeros, Total + Contribution)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec number_of_substrings(s :: String.t) :: integer
  def number_of_substrings(s) do
    n = byte_size(s)
    zeros = for i <- 0..(n - 1), :binary.at(s, i) == ?0, do: i
    zero_count = length(zeros)
    zero_tuple = List.to_tuple(zeros)

    Enum.reduce(0..(n - 1), 0, fn left, answer ->
      first = first_zero_at_least(zero_tuple, zero_count, left, 0, zero_count)
      first_zero_position = if first < zero_count, do: elem(zero_tuple, first), else: n
      no_zero_count = first_zero_position - left
      added = count_zero_groups(first, zero_count, left, n, zero_tuple, 0)
      answer + no_zero_count + added
    end)
  end

  defp first_zero_at_least(_zeros, _count, _left, lo, hi) when lo >= hi, do: lo

  defp first_zero_at_least(zeros, count, left, lo, hi) do
    mid = div(lo + hi, 2)

    if mid < count and elem(zeros, mid) < left do
      first_zero_at_least(zeros, count, left, mid + 1, hi)
    else
      first_zero_at_least(zeros, count, left, lo, mid)
    end
  end

  defp count_zero_groups(k, count, _left, _n, _zeros, total) when k >= count, do: total

  defp count_zero_groups(k, count, left, n, zeros, total) do
    count_zeros = k - first_zero_at_least(zeros, count, left, 0, count) + 1
    min_length = count_zeros * count_zeros + count_zeros

    if min_length > n - left do
      total
    else
      next_zero = if k + 1 < count, do: elem(zeros, k + 1), else: n
      max_length = next_zero - left

      contribution =
        if min_length <= max_length do
          min_end = left + min_length - 1
          next_zero - max(min_end, elem(zeros, k))
        else
          0
        end

      count_zero_groups(k + 1, count, left, n, zeros, total + contribution)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n sqrt(n)), where n is the string length; each start considers at most O(sqrt(n)) zero counts.
- **Space Complexity:** O(n) for storing zero positions.
