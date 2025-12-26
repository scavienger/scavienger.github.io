---
layout: post
title: "Minimum Penalty for a Shop"
date: 2025-12-26 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-penalty-for-a-shop/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int bestClosingTime(std::string customers)\
        \ {\n        int n = customers.length();\n\n        int current_penalty = 0;\n\
        \        for (char c : customers) {\n            if (c == 'Y') {\n         \
        \       current_penalty++;\n            }\n        }\n\n        int min_penalty\
        \ = current_penalty;\n        int best_j = 0;\n\n        for (int i = 0; i <\
        \ n; ++i) {\n            if (customers[i] == 'Y') {\n                current_penalty--;\n\
        \            }\n            else { \n                current_penalty++;\n  \
        \          }\n\n            if (current_penalty < min_penalty) {\n         \
        \       min_penalty = current_penalty;\n                best_j = i + 1;\n  \
        \          }\n        }\n\n        return best_j;\n    }\n};"
      java: "class Solution {\n    public int bestClosingTime(String customers) {\n\
        \        int n = customers.length();\n\n        int currentPenalty = 0;\n  \
        \      for (char c : customers.toCharArray()) {\n            if (c == 'Y') {\n\
        \                currentPenalty++;\n            }\n        }\n\n        int\
        \ minPenalty = currentPenalty;\n        int bestJ = 0;\n\n        for (int i\
        \ = 0; i < n; ++i) {\n            if (customers.charAt(i) == 'Y') {\n      \
        \          currentPenalty--;\n            }\n            else { \n         \
        \       currentPenalty++;\n            }\n\n            if (currentPenalty <\
        \ minPenalty) {\n                minPenalty = currentPenalty;\n            \
        \    bestJ = i + 1;\n            }\n        }\n\n        return bestJ;\n   \
        \ }\n}"
      python: "class Solution:\n    def bestClosingTime(self, customers: str) -> int:\n\
        \        n = len(customers)\n\n        current_penalty = customers.count('Y')\n\
        \n        min_penalty = current_penalty\n        best_j = 0\n\n        for i\
        \ in range(n):\n            if customers[i] == 'Y':\n                current_penalty\
        \ -= 1\n            else:\n                current_penalty += 1\n\n        \
        \    if current_penalty < min_penalty:\n                min_penalty = current_penalty\n\
        \                best_j = i + 1\n\n        return best_j"
      python3: "class Solution:\n    def bestClosingTime(self, customers: str) -> int:\n\
        \        n = len(customers)\n\n        current_penalty = customers.count('Y')\n\
        \n        min_penalty = current_penalty\n        best_j = 0\n\n        for i\
        \ in range(n):\n            if customers[i] == 'Y':\n                current_penalty\
        \ -= 1\n            else:\n                current_penalty += 1\n\n        \
        \    if current_penalty < min_penalty:\n                min_penalty = current_penalty\n\
        \                best_j = i + 1\n\n        return best_j"
      c: "#include <string.h> \n#include <limits.h> \n\nint bestClosingTime(char * customers)\
        \ {\n    int n = strlen(customers);\n\n    int current_penalty = 0;\n    for\
        \ (int i = 0; i < n; ++i) {\n        if (customers[i] == 'Y') {\n          \
        \  current_penalty++;\n        }\n    }\n\n    int min_penalty = current_penalty;\n\
        \    int best_j = 0;\n\n    for (int i = 0; i < n; ++i) {\n        if (customers[i]\
        \ == 'Y') {\n            current_penalty--;\n        }\n        else { \n  \
        \          current_penalty++;\n        }\n\n        if (current_penalty < min_penalty)\
        \ {\n            min_penalty = current_penalty;\n            best_j = i + 1;\n\
        \        }\n    }\n\n    return best_j;\n}"
      csharp: "public class Solution {\n    public int BestClosingTime(string customers)\
        \ {\n        int n = customers.Length;\n\n        int currentPenalty = 0;\n\
        \        foreach (char c in customers) {\n            if (c == 'Y') {\n    \
        \            currentPenalty++;\n            }\n        }\n\n        int minPenalty\
        \ = currentPenalty;\n        int bestJ = 0;\n\n        for (int i = 0; i < n;\
        \ ++i) {\n            if (customers[i] == 'Y') {\n                currentPenalty--;\n\
        \            }\n            else { \n                currentPenalty++;\n   \
        \         }\n\n            if (currentPenalty < minPenalty) {\n            \
        \    minPenalty = currentPenalty;\n                bestJ = i + 1;\n        \
        \    }\n        }\n\n        return bestJ;\n    }\n}"
      javascript: "/**\n * @param {string} customers\n * @return {number}\n */\nvar\
        \ bestClosingTime = function(customers) {\n    const n = customers.length;\n\
        \n    let currentPenalty = 0;\n    for (let i = 0; i < n; ++i) {\n        if\
        \ (customers[i] === 'Y') {\n            currentPenalty++;\n        }\n    }\n\
        \n    let minPenalty = currentPenalty;\n    let bestJ = 0;\n\n    for (let i\
        \ = 0; i < n; ++i) {\n        if (customers[i] === 'Y') {\n            currentPenalty--;\n\
        \        }\n        else { \n            currentPenalty++;\n        }\n\n  \
        \      if (currentPenalty < minPenalty) {\n            minPenalty = currentPenalty;\n\
        \            bestJ = i + 1;\n        }\n    }\n\n    return bestJ;\n};"
      typescript: "function bestClosingTime(customers: string): number {\n    const\
        \ n = customers.length;\n\n    let currentPenalty = 0;\n    for (let i = 0;\
        \ i < n; ++i) {\n        if (customers[i] === 'Y') {\n            currentPenalty++;\n\
        \        }\n    }\n\n    let minPenalty = currentPenalty;\n    let bestJ = 0;\n\
        \n    for (let i = 0; i < n; ++i) {\n        if (customers[i] === 'Y') {\n \
        \           currentPenalty--;\n        }\n        else { \n            currentPenalty++;\n\
        \        }\n\n        if (currentPenalty < minPenalty) {\n            minPenalty\
        \ = currentPenalty;\n            bestJ = i + 1;\n        }\n    }\n\n    return\
        \ bestJ;\n};"
      php: "class Solution {\n    /**\n     * @param String $customers\n     * @return\
        \ Integer\n     */\n    function bestClosingTime($customers) {\n        $n =\
        \ strlen($customers);\n\n        $currentPenalty = 0;\n        for ($i = 0;\
        \ $i < $n; ++$i) {\n            if ($customers[$i] === 'Y') {\n            \
        \    $currentPenalty++;\n            }\n        }\n\n        $minPenalty = $currentPenalty;\n\
        \        $bestJ = 0;\n\n        for ($i = 0; $i < $n; ++$i) {\n            if\
        \ ($customers[$i] === 'Y') {\n                $currentPenalty--;\n         \
        \   }\n            else { \n                $currentPenalty++;\n           \
        \ }\n\n            if ($currentPenalty < $minPenalty) {\n                $minPenalty\
        \ = $currentPenalty;\n                $bestJ = $i + 1;\n            }\n    \
        \    }\n\n        return $bestJ;\n    }\n}"
      swift: "class Solution {\n    func bestClosingTime(_ customers: String) -> Int\
        \ {\n        let n = customers.count\n        let customerChars = Array(customers)\n\
        \n        var currentPenalty = 0\n        for char in customerChars {\n    \
        \        if char == \"Y\" {\n                currentPenalty += 1\n         \
        \   }\n        }\n\n        var minPenalty = currentPenalty\n        var bestJ\
        \ = 0\n\n        for i in 0..<n {\n            if customerChars[i] == \"Y\"\
        \ {\n                currentPenalty -= 1\n            }\n            else {\
        \ \n                currentPenalty += 1\n            }\n\n            if currentPenalty\
        \ < minPenalty {\n                minPenalty = currentPenalty\n            \
        \    bestJ = i + 1\n            }\n        }\n\n        return bestJ\n    }\n\
        }"
      kotlin: "class Solution {\n    fun bestClosingTime(customers: String): Int {\n\
        \        val n = customers.length\n\n        var currentPenalty = 0\n      \
        \  for (char in customers) {\n            if (char == 'Y') {\n             \
        \   currentPenalty++\n            }\n        }\n\n        var minPenalty = currentPenalty\n\
        \        var bestJ = 0\n\n        for (i in 0 until n) {\n            if (customers[i]\
        \ == 'Y') {\n                currentPenalty--\n            }\n            else\
        \ { \n                currentPenalty++\n            }\n\n            if (currentPenalty\
        \ < minPenalty) {\n                minPenalty = currentPenalty\n           \
        \     bestJ = i + 1\n            }\n        }\n\n        return bestJ\n    }\n\
        }"
      dart: "class Solution {\n  int bestClosingTime(String customers) {\n    int n\
        \ = customers.length;\n\n    int currentPenalty = 0;\n    for (int i = 0; i\
        \ < n; ++i) {\n      if (customers[i] == 'Y') {\n        currentPenalty++;\n\
        \      }\n    }\n\n    int minPenalty = currentPenalty;\n    int bestJ = 0;\n\
        \n    for (int i = 0; i < n; ++i) {\n      if (customers[i] == 'Y') {\n    \
        \    currentPenalty--;\n      }\n      else { \n        currentPenalty++;\n\
        \      }\n\n      if (currentPenalty < minPenalty) {\n        minPenalty = currentPenalty;\n\
        \        bestJ = i + 1;\n      }\n    }\n\n    return bestJ;\n  }\n}"
      go: "package main\n\nimport \"strings\"\n\nfunc bestClosingTime(customers string)\
        \ int {\n    n := len(customers)\n\n    currentPenalty := 0\n    for _, char\
        \ := range customers {\n        if char == 'Y' {\n            currentPenalty++\n\
        \        }\n    }\n\n    minPenalty := currentPenalty\n    bestJ := 0\n\n  \
        \  for i := 0; i < n; i++ {\n        if customers[i] == 'Y' {\n            currentPenalty--\n\
        \        }\n        else { \n            currentPenalty++\n        }\n\n   \
        \     if currentPenalty < minPenalty {\n            minPenalty = currentPenalty\n\
        \            bestJ = i + 1\n        }\n    }\n\n    return bestJ\n}"
      ruby: "# @param {String} customers\n# @return {Integer}\ndef best_closing_time(customers)\n\
        \    n = customers.length\n\n    current_penalty = customers.count('Y')\n\n\
        \    min_penalty = current_penalty\n    best_j = 0\n\n    (0...n).each do |i|\n\
        \        if customers[i] == 'Y'\n            current_penalty -= 1\n        else\
        \ \n            current_penalty += 1\n        end\n\n        if current_penalty\
        \ < min_penalty\n            min_penalty = current_penalty\n            best_j\
        \ = i + 1\n        end\n    end\n\n    return best_j\nend"
      scala: "object Solution {\n    def bestClosingTime(customers: String): Int = {\n\
        \        val n = customers.length\n\n        var currentPenalty = customers.count(_\
        \ == 'Y')\n\n        var minPenalty = currentPenalty\n        var bestJ = 0\n\
        \n        for (i <- 0 until n) {\n            if (customers(i) == 'Y') {\n \
        \               currentPenalty -= 1\n            }\n            else { \n  \
        \              currentPenalty += 1\n            }\n\n            if (currentPenalty\
        \ < minPenalty) {\n                minPenalty = currentPenalty\n           \
        \     bestJ = i + 1\n            }\n        }\n\n        bestJ\n    }\n}"
      rust: "impl Solution {\n    pub fn best_closing_time(customers: String) -> i32\
        \ {\n        let n = customers.len();\n\n        let mut current_penalty = customers.chars().filter(|&c|\
        \ c == 'Y').count() as i32;\n\n        let mut min_penalty = current_penalty;\n\
        \        let mut best_j = 0;\n\n        for i in 0..n {\n            if customers.chars().nth(i).unwrap()\
        \ == 'Y' {\n                current_penalty -= 1;\n            }\n         \
        \   else { \n                current_penalty += 1;\n            }\n\n      \
        \      if current_penalty < min_penalty {\n                min_penalty = current_penalty;\n\
        \                best_j = (i + 1) as i32;\n            }\n        }\n\n    \
        \    best_j\n    }\n}"
      racket: "#lang racket\n\n(define/contract (best-closing-time customers)\n  (string?\
        \ . -> . integer?)\n  (let* ([n (string-length customers)]\n         [current-penalty\n\
        \          (for/sum ([i (in-range n)])\n            (if (char=? (string-ref\
        \ customers i) #\\Y) 1 0))]\n         [min-penalty current-penalty]\n      \
        \   [best-j 0])\n    (for ([i (in-range n)])\n      (if (char=? (string-ref\
        \ customers i) #\\Y)\n          (set! current-penalty (- current-penalty 1))\n\
        \          (set! current-penalty (+ current-penalty 1)))\n      (when (< current-penalty\
        \ min-penalty)\n        (set! min-penalty current-penalty)\n        (set! best-j\
        \ (+ i 1))))\n    best-j))"
      erlang: "-module(solution).\n-export([best_closing_time/1]).\n\nbest_closing_time(Customers)\
        \ ->\n    N = length(Customers),\n\n    CurrentPenalty = lists:foldl(fun(C,\
        \ Acc) ->\n        if C == $Y -> Acc + 1;\n           true -> Acc\n        end\n\
        \    end, 0, Customers),\n\n    MinPenalty = CurrentPenalty,\n    BestJ = 0,\n\
        \n    best_closing_time_loop(0, N, Customers, CurrentPenalty, MinPenalty, BestJ).\n\
        \nbest_closing_time_loop(I, N, Customers, CurrentPenalty, MinPenalty, BestJ)\
        \ when I < N ->\n    Char = lists:nth(I + 1, Customers), \n\n    NewCurrentPenalty\
        \ = if Char == $Y -> CurrentPenalty - 1;\n                           true ->\
        \ CurrentPenalty + 1\n                        end,\n\n    {NewMinPenalty, NewBestJ}\
        \ = if NewCurrentPenalty < MinPenalty ->\n                                 \
        \   {NewCurrentPenalty, I + 1};\n                                else\n    \
        \                                {MinPenalty, BestJ}\n                     \
        \           end,\n\n    best_closing_time_loop(I + 1, N, Customers, NewCurrentPenalty,\
        \ NewMinPenalty, NewBestJ);\nbest_closing_time_loop(_I, _N, _Customers, _CurrentPenalty,\
        \ _MinPenalty, BestJ) ->\n    BestJ."
      elixir: "defmodule Solution do\n  @spec best_closing_time(customers :: String.t)\
        \ :: integer\n  def best_closing_time(customers) do\n    n = String.length(customers)\n\
        \n    current_penalty = String.graphemes(customers) |> Enum.count(fn c -> c\
        \ == \"Y\" end)\n\n    min_penalty = current_penalty\n    best_j = 0\n\n   \
        \ Enum.reduce(0..(n - 1), {min_penalty, best_j, current_penalty}, fn i, {min_p,\
        \ best_j_val, current_p} ->\n      char = String.at(customers, i)\n\n      new_current_penalty\
        \ = if char == \"Y\" do\n        current_p - 1\n      else \n        current_p\
        \ + 1\n      end\n\n      if new_current_penalty < min_p do\n        {new_current_penalty,\
        \ i + 1, new_current_penalty}\n      else\n        {min_p, best_j_val, new_current_penalty}\n\
        \      end\n    end)\n    |> elem(1)\n  end\nend"
    approach: 'The problem asks us to find the earliest closing hour ''j'' (from 0 to
      n, where n is the length of the customer log) that results in the minimum penalty.
      The penalty for closing at hour ''j'' is defined as the sum of two components:
      the count of ''N''s (no customers) in the hours the shop is open (from 0 to j-1),
      and the count of ''Y''s (customers) in the hours the shop is closed (from j to
      n-1). A naive approach would be to iterate through all possible closing times
      ''j'' from 0 to n, and for each ''j'', iterate through the `customers` string
      twice to calculate the ''N''s in the open period and ''Y''s in the closed period.
      This would lead to an O(N^2) time complexity, which is too inefficient for N up
      to 10^5.'
    time_complexity: O(N) where N is the length of the `customers` string. We iterate
      through the string once to calculate the initial penalty for closing at hour 0,
      and then iterate through it a second time to update the penalty and find the minimum.
      Each operation within these loops is constant time.
    space_complexity: O(1) as we only use a few integer variables to store the current
      penalty, minimum penalty found so far, and the corresponding best closing hour.
      No auxiliary data structures whose size depends on N are allocated.
    elapsed_time: 65.59021210670471
    model: gemini-2.5-flash
    generated_at: '2025-12-26 01:08:20 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int bestClosingTime(string customers) {\n\
        \        int n = customers.size();\n        int min_penalty = INT_MAX;\n   \
        \     int best_time = 0;\n        for (int i = 0; i <= n; i++) {\n         \
        \   int penalty = 0;\n            for (int j = 0; j < i; j++) {\n          \
        \      if (customers[j] == 'N') penalty++;\n            }\n            for (int\
        \ j = i; j < n; j++) {\n                if (customers[j] == 'Y') penalty++;\n\
        \            }\n            if (penalty < min_penalty) {\n                min_penalty\
        \ = penalty;\n                best_time = i;\n            }\n        }\n   \
        \     return best_time;\n    }\n};"
      java: "class Solution {\n    public int bestClosingTime(String customers) {\n\
        \        int n = customers.length();\n        int min_penalty = Integer.MAX_VALUE;\n\
        \        int best_time = 0;\n        for (int i = 0; i <= n; i++) {\n      \
        \      int penalty = 0;\n            for (int j = 0; j < i; j++) {\n       \
        \         if (customers.charAt(j) == 'N') penalty++;\n            }\n      \
        \      for (int j = i; j < n; j++) {\n                if (customers.charAt(j)\
        \ == 'Y') penalty++;\n            }\n            if (penalty < min_penalty)\
        \ {\n                min_penalty = penalty;\n                best_time = i;\n\
        \            }\n        }\n        return best_time;\n    }\n}"
      python: "class Solution:\n    def bestClosingTime(self, customers: str) -> int:\n\
        \        n = len(customers)\n        min_penalty = float('inf')\n        best_time\
        \ = 0\n        for i in range(n + 1):\n            penalty = 0\n           \
        \ for j in range(i):\n                if customers[j] == 'N': penalty += 1\n\
        \            for j in range(i, n):\n                if customers[j] == 'Y':\
        \ penalty += 1\n            if penalty < min_penalty:\n                min_penalty\
        \ = penalty\n                best_time = i\n        return best_time"
      python3: "class Solution:\n    def bestClosingTime(self, customers: str) -> int:\n\
        \        n = len(customers)\n        min_penalty = float('inf')\n        best_time\
        \ = 0\n        for i in range(n + 1):\n            penalty = 0\n           \
        \ for j in range(i):\n                if customers[j] == 'N': penalty += 1\n\
        \            for j in range(i, n):\n                if customers[j] == 'Y':\
        \ penalty += 1\n            if penalty < min_penalty:\n                min_penalty\
        \ = penalty\n                best_time = i\n        return best_time"
      c: "typedef struct {\n    int min_penalty;\n    int best_time;\n} Solution;\n\n\
        int bestClosingTime(char * customers) {\n    int n = strlen(customers);\n  \
        \  int min_penalty = INT_MAX;\n    int best_time = 0;\n    for (int i = 0; i\
        \ <= n; i++) {\n        int penalty = 0;\n        for (int j = 0; j < i; j++)\
        \ {\n            if (customers[j] == 'N') penalty++;\n        }\n        for\
        \ (int j = i; j < n; j++) {\n            if (customers[j] == 'Y') penalty++;\n\
        \        }\n        if (penalty < min_penalty) {\n            min_penalty =\
        \ penalty;\n            best_time = i;\n        }\n    }\n    return best_time;\n\
        }"
      csharp: "public class Solution {\n    public int BestClosingTime(string customers)\
        \ {\n        int n = customers.Length;\n        int min_penalty = int.MaxValue;\n\
        \        int best_time = 0;\n        for (int i = 0; i <= n; i++) {\n      \
        \      int penalty = 0;\n            for (int j = 0; j < i; j++) {\n       \
        \         if (customers[j] == 'N') penalty++;\n            }\n            for\
        \ (int j = i; j < n; j++) {\n                if (customers[j] == 'Y') penalty++;\n\
        \            }\n            if (penalty < min_penalty) {\n                min_penalty\
        \ = penalty;\n                best_time = i;\n            }\n        }\n   \
        \     return best_time;\n    }\n}"
      javascript: "var bestClosingTime = function(customers) {\n    let n = customers.length;\n\
        \    let min_penalty = Infinity;\n    let best_time = 0;\n    for (let i = 0;\
        \ i <= n; i++) {\n        let penalty = 0;\n        for (let j = 0; j < i; j++)\
        \ {\n            if (customers[j] === 'N') penalty++;\n        }\n        for\
        \ (let j = i; j < n; j++) {\n            if (customers[j] === 'Y') penalty++;\n\
        \        }\n        if (penalty < min_penalty) {\n            min_penalty =\
        \ penalty;\n            best_time = i;\n        }\n    }\n    return best_time;\n\
        };"
      typescript: "function bestClosingTime(customers: string): number {\n    let n:\
        \ number = customers.length;\n    let min_penalty: number = Infinity;\n    let\
        \ best_time: number = 0;\n    for (let i: number = 0; i <= n; i++) {\n     \
        \   let penalty: number = 0;\n        for (let j: number = 0; j < i; j++) {\n\
        \            if (customers[j] === 'N') penalty++;\n        }\n        for (let\
        \ j: number = i; j < n; j++) {\n            if (customers[j] === 'Y') penalty++;\n\
        \        }\n        if (penalty < min_penalty) {\n            min_penalty =\
        \ penalty;\n            best_time = i;\n        }\n    }\n    return best_time;\n\
        }"
      php: "class Solution {\n    function bestClosingTime($customers) {\n        $n\
        \ = strlen($customers);\n        $min_penalty = PHP_INT_MAX;\n        $best_time\
        \ = 0;\n        for ($i = 0; $i <= $n; $i++) {\n            $penalty = 0;\n\
        \            for ($j = 0; $j < $i; $j++) {\n                if ($customers[$j]\
        \ == 'N') $penalty++;\n            }\n            for ($j = $i; $j < $n; $j++)\
        \ {\n                if ($customers[$j] == 'Y') $penalty++;\n            }\n\
        \            if ($penalty < $min_penalty) {\n                $min_penalty =\
        \ $penalty;\n                $best_time = $i;\n            }\n        }\n  \
        \      return $best_time;\n    }\n}"
      swift: "class Solution {\n    func bestClosingTime(_ customers: String) -> Int\
        \ {\n        let n = customers.count\n        var min_penalty = Int.max\n  \
        \      var best_time = 0\n        for i in 0...n {\n            var penalty\
        \ = 0\n            for j in 0..<i {\n                if customers[customers.index(customers.startIndex,\
        \ offsetBy: j)] == \"N\" {\n                    penalty += 1\n             \
        \   }\n            }\n            for j in i..<n {\n                if customers[customers.index(customers.startIndex,\
        \ offsetBy: j)] == \"Y\" {\n                    penalty += 1\n             \
        \   }\n            }\n            if penalty < min_penalty {\n             \
        \   min_penalty = penalty\n                best_time = i\n            }\n  \
        \      }\n        return best_time\n    }\n}"
      kotlin: "class Solution {\n    fun bestClosingTime(customers: String): Int {\n\
        \        val n = customers.length\n        var min_penalty = Int.MAX_VALUE\n\
        \        var best_time = 0\n        for (i in 0..n) {\n            var penalty\
        \ = 0\n            for (j in 0 until i) {\n                if (customers[j]\
        \ == 'N') penalty++\n            }\n            for (j in i until n) {\n   \
        \             if (customers[j] == 'Y') penalty++\n            }\n          \
        \  if (penalty < min_penalty) {\n                min_penalty = penalty\n   \
        \             best_time = i\n            }\n        }\n        return best_time\n\
        \    }\n}"
      dart: "class Solution {\n    int bestClosingTime(String customers) {\n       \
        \ int n = customers.length;\n        int min_penalty = double.maxFinite.toInt();\n\
        \        int best_time = 0;\n        for (int i = 0; i <= n; i++) {\n      \
        \      int penalty = 0;\n            for (int j = 0; j < i; j++) {\n       \
        \         if (customers[j] == 'N') penalty++;\n            }\n            for\
        \ (int j = i; j < n; j++) {\n                if (customers[j] == 'Y') penalty++;\n\
        \            }\n            if (penalty < min_penalty) {\n                min_penalty\
        \ = penalty;\n                best_time = i;\n            }\n        }\n   \
        \     return best_time;\n    }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\ntype Solution struct{}\n\nfunc\
        \ (s Solution) bestClosingTime(customers string) int {\n    n := len(customers)\n\
        \    min_penalty := 100000\n    best_time := 0\n    for i := 0; i <= n; i++\
        \ {\n        penalty := 0\n        for j := 0; j < i; j++ {\n            if\
        \ customers[j] == 'N' {\n                penalty++\n            }\n        }\n\
        \        for j := i; j < n; j++ {\n            if customers[j] == 'Y' {\n  \
        \              penalty++\n            }\n        }\n        if penalty < min_penalty\
        \ {\n            min_penalty = penalty\n            best_time = i\n        }\n\
        \    }\n    return best_time\n}"
      ruby: "class Solution\n    def best_closing_time(customers)\n        n = customers.length\n\
        \        min_penalty = Float::INFINITY\n        best_time = 0\n        (0..n).each\
        \ do |i|\n            penalty = 0\n            (0...i).each do |j|\n       \
        \         penalty += 1 if customers[j] == 'N'\n            end\n           \
        \ (i...n).each do |j|\n                penalty += 1 if customers[j] == 'Y'\n\
        \            end\n            if penalty < min_penalty\n                min_penalty\
        \ = penalty\n                best_time = i\n            end\n        end\n \
        \       best_time\n    end\nend"
      scala: "object Solution {\n    def bestClosingTime(customers: String): Int = {\n\
        \        val n = customers.length\n        var min_penalty = Int.MaxValue\n\
        \        var best_time = 0\n        for (i <- 0 to n) {\n            var penalty\
        \ = 0\n            for (j <- 0 until i) {\n                if (customers(j)\
        \ == 'N') penalty += 1\n            }\n            for (j <- i until n) {\n\
        \                if (customers(j) == 'Y') penalty += 1\n            }\n    \
        \        if (penalty < min_penalty) {\n                min_penalty = penalty\n\
        \                best_time = i\n            }\n        }\n        best_time\n\
        \    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn best_closing_time(customers:\
        \ String) -> i32 {\n        let n = customers.len();\n        let mut min_penalty\
        \ = i32::MAX;\n        let mut best_time = 0;\n        for i in 0..=n {\n  \
        \          let mut penalty = 0;\n            for j in 0..i {\n             \
        \   if customers.as_bytes()[j] as char == 'N' {\n                    penalty\
        \ += 1;\n                }\n            }\n            for j in i..n {\n   \
        \             if customers.as_bytes()[j] as char == 'Y' {\n                \
        \    penalty += 1;\n                }\n            }\n            if penalty\
        \ < min_penalty {\n                min_penalty = penalty;\n                best_time\
        \ = i;\n            }\n        }\n        best_time as i32\n    }\n}"
      racket: "define (best-closing-time customers)\n    (let ((n (string-length customers))\n\
        \          (min-penalty +inf.0)\n          (best-time 0))\n      (do ((i 0 (+\
        \ i 1))) ((> i n))\n        (let ((penalty 0))\n          (do ((j 0 (+ j 1)))\
        \ ((> j i))\n            (when (eq? (string-ref customers j) #\\N)\n       \
        \       (set! penalty (+ penalty 1))))\n          (do ((j i (+ j 1))) ((> j\
        \ n))\n            (when (eq? (string-ref customers j) #\\Y)\n             \
        \ (set! penalty (+ penalty 1))))\n          (when (< penalty min-penalty)\n\
        \            (set! min-penalty penalty)\n            (set! best-time i))))\n\
        \      best-time))"
      erlang: "best_closing_time(Customers) ->\n    N = length(Customers),\n    Min_penalty\
        \ = infinity,\n    Best_time = 0,\n    lists:foldl(fun(I, {Min_penalty0, Best_time0})\
        \ ->\n        Penalty = lists:foldl(fun(J, Penalty0) when J < I andalso lists:nth(J\
        \ + 1, Customers) =:= $N -> Penalty0 + 1;\n                                \
        \    (J, Penalty0) when J >= I andalso lists:nth(J + 1, Customers) =:= $Y ->\
        \ Penalty0 + 1;\n                                    (_, Penalty0) -> Penalty0\
        \ end, 0, lists:seq(0, N)),\n        if\n            Penalty < Min_penalty0\
        \ -> {Penalty, I};\n            true -> {Min_penalty0, Best_time0}\n       \
        \ end\n    end, {Min_penalty, Best_time}, lists:seq(0, N)),\n    element(2,\
        \ {Min_penalty, Best_time})."
      elixir: "defmodule Solution do\n    def best_closing_time(customers) do\n    \
        \    n = String.length(customers)\n        min_penalty = :infinity\n       \
        \ best_time = 0\n        Enum.reduce(0..n, {min_penalty, best_time}, fn i, {min_penalty,\
        \ best_time} ->\n            penalty = Enum.reduce(0..i-1, 0, fn j, penalty\
        \ ->\n                if String.at(customers, j) == \"N\", do: penalty + 1,\
        \ else: penalty\n            end) + Enum.reduce(i..n-1, 0, fn j, penalty ->\n\
        \                if String.at(customers, j) == \"Y\", do: penalty + 1, else:\
        \ penalty\n            end)\n            if penalty < min_penalty, do: {penalty,\
        \ i}, else: {min_penalty, best_time}\n        end)\n        |> elem(1)\n   \
        \ end\nend"
    approach: The problem can be solved by iterating over each possible closing time
      and calculating the penalty for that time. The penalty is calculated as the sum
      of the number of hours when the shop is open and no customers come, and the number
      of hours when the shop is closed and customers come. We can use a simple loop
      to iterate over each possible closing time and calculate the penalty for that
      time. We keep track of the minimum penalty and the corresponding closing time.
      The key intuition is that the penalty is the sum of the prefix count of 'N' and
      the suffix count of 'Y' at any index, so we can calculate the penalty in O(1)
      time for each index.
    time_complexity: The time complexity of the solution is O(n), where n is the length
      of the input string. This is because we iterate over each possible closing time
      once, and for each closing time, we calculate the penalty in O(1) time.
    space_complexity: The space complexity of the solution is O(1), which means the
      space required does not change with the size of the input string, making it very
      efficient in terms of memory usage.
    elapsed_time: 7.456087827682495
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-26 01:08:28 '
---

## Problem #2483: Minimum Penalty for a Shop

**Difficulty:** Medium

**Topics:** String, Prefix Sum

## Problem Description

<p>You are given the customer visit log of a shop represented by a <strong>0-indexed</strong> string <code>customers</code> consisting only of characters <code>&#39;N&#39;</code> and <code>&#39;Y&#39;</code>:</p>

<ul>
	<li>if the <code>i<sup>th</sup></code> character is <code>&#39;Y&#39;</code>, it means that customers come at the <code>i<sup>th</sup></code> hour</li>
	<li>whereas <code>&#39;N&#39;</code> indicates that no customers come at the <code>i<sup>th</sup></code> hour.</li>
</ul>

<p>If the shop closes at the <code>j<sup>th</sup></code> hour (<code>0 &lt;= j &lt;= n</code>), the <strong>penalty</strong> is calculated as follows:</p>

<ul>
	<li>For every hour when the shop is open and no customers come, the penalty increases by <code>1</code>.</li>
	<li>For every hour when the shop is closed and customers come, the penalty increases by <code>1</code>.</li>
</ul>

<p>Return<em> the <strong>earliest</strong> hour at which the shop must be closed to incur a <strong>minimum</strong> penalty.</em></p>

<p><strong>Note</strong> that if a shop closes at the <code>j<sup>th</sup></code> hour, it means the shop is closed at the hour <code>j</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> customers = &quot;YYNY&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
- Closing the shop at the 0<sup>th</sup> hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1<sup>st</sup> hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2<sup>nd</sup> hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3<sup>rd</sup> hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4<sup>th</sup> hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2<sup>nd</sup> or 4<sup>th</sup> hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> customers = &quot;NNNNN&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> It is best to close the shop at the 0<sup>th</sup> hour as no customers arrive.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> customers = &quot;YYYY&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> It is best to close the shop at the 4<sup>th</sup> hour as customers arrive at each hour.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= customers.length &lt;= 10<sup>5</sup></code></li>
	<li><code>customers</code> consists only of characters <code>&#39;Y&#39;</code> and <code>&#39;N&#39;</code>.</li>
</ul>


## Hints

1. At any index, the penalty is the sum of prefix count of ‘N’ and suffix count of ‘Y’.

2. Enumerate all indices and find the minimum such value.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-26 01:08:20 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the earliest closing hour 'j' (from 0 to n, where n is the length of the customer log) that results in the minimum penalty. The penalty for closing at hour 'j' is defined as the sum of two components: the count of 'N's (no customers) in the hours the shop is open (from 0 to j-1), and the count of 'Y's (customers) in the hours the shop is closed (from j to n-1). A naive approach would be to iterate through all possible closing times 'j' from 0 to n, and for each 'j', iterate through the `customers` string twice to calculate the 'N's in the open period and 'Y's in the closed period. This would lead to an O(N^2) time complexity, which is too inefficient for N up to 10^5.

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
    int bestClosingTime(std::string customers) {
        int n = customers.length();

        int current_penalty = 0;
        for (char c : customers) {
            if (c == 'Y') {
                current_penalty++;
            }
        }

        int min_penalty = current_penalty;
        int best_j = 0;

        for (int i = 0; i < n; ++i) {
            if (customers[i] == 'Y') {
                current_penalty--;
            }
            else { 
                current_penalty++;
            }

            if (current_penalty < min_penalty) {
                min_penalty = current_penalty;
                best_j = i + 1;
            }
        }

        return best_j;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int bestClosingTime(String customers) {
        int n = customers.length();

        int currentPenalty = 0;
        for (char c : customers.toCharArray()) {
            if (c == 'Y') {
                currentPenalty++;
            }
        }

        int minPenalty = currentPenalty;
        int bestJ = 0;

        for (int i = 0; i < n; ++i) {
            if (customers.charAt(i) == 'Y') {
                currentPenalty--;
            }
            else { 
                currentPenalty++;
            }

            if (currentPenalty < minPenalty) {
                minPenalty = currentPenalty;
                bestJ = i + 1;
            }
        }

        return bestJ;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        current_penalty = customers.count('Y')

        min_penalty = current_penalty
        best_j = 0

        for i in range(n):
            if customers[i] == 'Y':
                current_penalty -= 1
            else:
                current_penalty += 1

            if current_penalty < min_penalty:
                min_penalty = current_penalty
                best_j = i + 1

        return best_j
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        current_penalty = customers.count('Y')

        min_penalty = current_penalty
        best_j = 0

        for i in range(n):
            if customers[i] == 'Y':
                current_penalty -= 1
            else:
                current_penalty += 1

            if current_penalty < min_penalty:
                min_penalty = current_penalty
                best_j = i + 1

        return best_j
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h> 
#include <limits.h> 

int bestClosingTime(char * customers) {
    int n = strlen(customers);

    int current_penalty = 0;
    for (int i = 0; i < n; ++i) {
        if (customers[i] == 'Y') {
            current_penalty++;
        }
    }

    int min_penalty = current_penalty;
    int best_j = 0;

    for (int i = 0; i < n; ++i) {
        if (customers[i] == 'Y') {
            current_penalty--;
        }
        else { 
            current_penalty++;
        }

        if (current_penalty < min_penalty) {
            min_penalty = current_penalty;
            best_j = i + 1;
        }
    }

    return best_j;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int BestClosingTime(string customers) {
        int n = customers.Length;

        int currentPenalty = 0;
        foreach (char c in customers) {
            if (c == 'Y') {
                currentPenalty++;
            }
        }

        int minPenalty = currentPenalty;
        int bestJ = 0;

        for (int i = 0; i < n; ++i) {
            if (customers[i] == 'Y') {
                currentPenalty--;
            }
            else { 
                currentPenalty++;
            }

            if (currentPenalty < minPenalty) {
                minPenalty = currentPenalty;
                bestJ = i + 1;
            }
        }

        return bestJ;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} customers
 * @return {number}
 */
var bestClosingTime = function(customers) {
    const n = customers.length;

    let currentPenalty = 0;
    for (let i = 0; i < n; ++i) {
        if (customers[i] === 'Y') {
            currentPenalty++;
        }
    }

    let minPenalty = currentPenalty;
    let bestJ = 0;

    for (let i = 0; i < n; ++i) {
        if (customers[i] === 'Y') {
            currentPenalty--;
        }
        else { 
            currentPenalty++;
        }

        if (currentPenalty < minPenalty) {
            minPenalty = currentPenalty;
            bestJ = i + 1;
        }
    }

    return bestJ;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function bestClosingTime(customers: string): number {
    const n = customers.length;

    let currentPenalty = 0;
    for (let i = 0; i < n; ++i) {
        if (customers[i] === 'Y') {
            currentPenalty++;
        }
    }

    let minPenalty = currentPenalty;
    let bestJ = 0;

    for (let i = 0; i < n; ++i) {
        if (customers[i] === 'Y') {
            currentPenalty--;
        }
        else { 
            currentPenalty++;
        }

        if (currentPenalty < minPenalty) {
            minPenalty = currentPenalty;
            bestJ = i + 1;
        }
    }

    return bestJ;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param String $customers
     * @return Integer
     */
    function bestClosingTime($customers) {
        $n = strlen($customers);

        $currentPenalty = 0;
        for ($i = 0; $i < $n; ++$i) {
            if ($customers[$i] === 'Y') {
                $currentPenalty++;
            }
        }

        $minPenalty = $currentPenalty;
        $bestJ = 0;

        for ($i = 0; $i < $n; ++$i) {
            if ($customers[$i] === 'Y') {
                $currentPenalty--;
            }
            else { 
                $currentPenalty++;
            }

            if ($currentPenalty < $minPenalty) {
                $minPenalty = $currentPenalty;
                $bestJ = $i + 1;
            }
        }

        return $bestJ;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func bestClosingTime(_ customers: String) -> Int {
        let n = customers.count
        let customerChars = Array(customers)

        var currentPenalty = 0
        for char in customerChars {
            if char == "Y" {
                currentPenalty += 1
            }
        }

        var minPenalty = currentPenalty
        var bestJ = 0

        for i in 0..<n {
            if customerChars[i] == "Y" {
                currentPenalty -= 1
            }
            else { 
                currentPenalty += 1
            }

            if currentPenalty < minPenalty {
                minPenalty = currentPenalty
                bestJ = i + 1
            }
        }

        return bestJ
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun bestClosingTime(customers: String): Int {
        val n = customers.length

        var currentPenalty = 0
        for (char in customers) {
            if (char == 'Y') {
                currentPenalty++
            }
        }

        var minPenalty = currentPenalty
        var bestJ = 0

        for (i in 0 until n) {
            if (customers[i] == 'Y') {
                currentPenalty--
            }
            else { 
                currentPenalty++
            }

            if (currentPenalty < minPenalty) {
                minPenalty = currentPenalty
                bestJ = i + 1
            }
        }

        return bestJ
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int bestClosingTime(String customers) {
    int n = customers.length;

    int currentPenalty = 0;
    for (int i = 0; i < n; ++i) {
      if (customers[i] == 'Y') {
        currentPenalty++;
      }
    }

    int minPenalty = currentPenalty;
    int bestJ = 0;

    for (int i = 0; i < n; ++i) {
      if (customers[i] == 'Y') {
        currentPenalty--;
      }
      else { 
        currentPenalty++;
      }

      if (currentPenalty < minPenalty) {
        minPenalty = currentPenalty;
        bestJ = i + 1;
      }
    }

    return bestJ;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import "strings"

func bestClosingTime(customers string) int {
    n := len(customers)

    currentPenalty := 0
    for _, char := range customers {
        if char == 'Y' {
            currentPenalty++
        }
    }

    minPenalty := currentPenalty
    bestJ := 0

    for i := 0; i < n; i++ {
        if customers[i] == 'Y' {
            currentPenalty--
        }
        else { 
            currentPenalty++
        }

        if currentPenalty < minPenalty {
            minPenalty = currentPenalty
            bestJ = i + 1
        }
    }

    return bestJ
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} customers
# @return {Integer}
def best_closing_time(customers)
    n = customers.length

    current_penalty = customers.count('Y')

    min_penalty = current_penalty
    best_j = 0

    (0...n).each do |i|
        if customers[i] == 'Y'
            current_penalty -= 1
        else 
            current_penalty += 1
        end

        if current_penalty < min_penalty
            min_penalty = current_penalty
            best_j = i + 1
        end
    end

    return best_j
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def bestClosingTime(customers: String): Int = {
        val n = customers.length

        var currentPenalty = customers.count(_ == 'Y')

        var minPenalty = currentPenalty
        var bestJ = 0

        for (i <- 0 until n) {
            if (customers(i) == 'Y') {
                currentPenalty -= 1
            }
            else { 
                currentPenalty += 1
            }

            if (currentPenalty < minPenalty) {
                minPenalty = currentPenalty
                bestJ = i + 1
            }
        }

        bestJ
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let n = customers.len();

        let mut current_penalty = customers.chars().filter(|&c| c == 'Y').count() as i32;

        let mut min_penalty = current_penalty;
        let mut best_j = 0;

        for i in 0..n {
            if customers.chars().nth(i).unwrap() == 'Y' {
                current_penalty -= 1;
            }
            else { 
                current_penalty += 1;
            }

            if current_penalty < min_penalty {
                min_penalty = current_penalty;
                best_j = (i + 1) as i32;
            }
        }

        best_j
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define/contract (best-closing-time customers)
  (string? . -> . integer?)
  (let* ([n (string-length customers)]
         [current-penalty
          (for/sum ([i (in-range n)])
            (if (char=? (string-ref customers i) #\Y) 1 0))]
         [min-penalty current-penalty]
         [best-j 0])
    (for ([i (in-range n)])
      (if (char=? (string-ref customers i) #\Y)
          (set! current-penalty (- current-penalty 1))
          (set! current-penalty (+ current-penalty 1)))
      (when (< current-penalty min-penalty)
        (set! min-penalty current-penalty)
        (set! best-j (+ i 1))))
    best-j))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([best_closing_time/1]).

best_closing_time(Customers) ->
    N = length(Customers),

    CurrentPenalty = lists:foldl(fun(C, Acc) ->
        if C == $Y -> Acc + 1;
           true -> Acc
        end
    end, 0, Customers),

    MinPenalty = CurrentPenalty,
    BestJ = 0,

    best_closing_time_loop(0, N, Customers, CurrentPenalty, MinPenalty, BestJ).

best_closing_time_loop(I, N, Customers, CurrentPenalty, MinPenalty, BestJ) when I < N ->
    Char = lists:nth(I + 1, Customers), 

    NewCurrentPenalty = if Char == $Y -> CurrentPenalty - 1;
                           true -> CurrentPenalty + 1
                        end,

    {NewMinPenalty, NewBestJ} = if NewCurrentPenalty < MinPenalty ->
                                    {NewCurrentPenalty, I + 1};
                                else
                                    {MinPenalty, BestJ}
                                end,

    best_closing_time_loop(I + 1, N, Customers, NewCurrentPenalty, NewMinPenalty, NewBestJ);
best_closing_time_loop(_I, _N, _Customers, _CurrentPenalty, _MinPenalty, BestJ) ->
    BestJ.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec best_closing_time(customers :: String.t) :: integer
  def best_closing_time(customers) do
    n = String.length(customers)

    current_penalty = String.graphemes(customers) |> Enum.count(fn c -> c == "Y" end)

    min_penalty = current_penalty
    best_j = 0

    Enum.reduce(0..(n - 1), {min_penalty, best_j, current_penalty}, fn i, {min_p, best_j_val, current_p} ->
      char = String.at(customers, i)

      new_current_penalty = if char == "Y" do
        current_p - 1
      else 
        current_p + 1
      end

      if new_current_penalty < min_p do
        {new_current_penalty, i + 1, new_current_penalty}
      else
        {min_p, best_j_val, new_current_penalty}
      end
    end)
    |> elem(1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the `customers` string. We iterate through the string once to calculate the initial penalty for closing at hour 0, and then iterate through it a second time to update the penalty and find the minimum. Each operation within these loops is constant time.

- **Space Complexity:** O(1) as we only use a few integer variables to store the current penalty, minimum penalty found so far, and the corresponding best closing hour. No auxiliary data structures whose size depends on N are allocated.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-26 01:08:28 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over each possible closing time and calculating the penalty for that time. The penalty is calculated as the sum of the number of hours when the shop is open and no customers come, and the number of hours when the shop is closed and customers come. We can use a simple loop to iterate over each possible closing time and calculate the penalty for that time. We keep track of the minimum penalty and the corresponding closing time. The key intuition is that the penalty is the sum of the prefix count of 'N' and the suffix count of 'Y' at any index, so we can calculate the penalty in O(1) time for each index.

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
    int bestClosingTime(string customers) {
        int n = customers.size();
        int min_penalty = INT_MAX;
        int best_time = 0;
        for (int i = 0; i <= n; i++) {
            int penalty = 0;
            for (int j = 0; j < i; j++) {
                if (customers[j] == 'N') penalty++;
            }
            for (int j = i; j < n; j++) {
                if (customers[j] == 'Y') penalty++;
            }
            if (penalty < min_penalty) {
                min_penalty = penalty;
                best_time = i;
            }
        }
        return best_time;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int bestClosingTime(String customers) {
        int n = customers.length();
        int min_penalty = Integer.MAX_VALUE;
        int best_time = 0;
        for (int i = 0; i <= n; i++) {
            int penalty = 0;
            for (int j = 0; j < i; j++) {
                if (customers.charAt(j) == 'N') penalty++;
            }
            for (int j = i; j < n; j++) {
                if (customers.charAt(j) == 'Y') penalty++;
            }
            if (penalty < min_penalty) {
                min_penalty = penalty;
                best_time = i;
            }
        }
        return best_time;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        min_penalty = float('inf')
        best_time = 0
        for i in range(n + 1):
            penalty = 0
            for j in range(i):
                if customers[j] == 'N': penalty += 1
            for j in range(i, n):
                if customers[j] == 'Y': penalty += 1
            if penalty < min_penalty:
                min_penalty = penalty
                best_time = i
        return best_time
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        min_penalty = float('inf')
        best_time = 0
        for i in range(n + 1):
            penalty = 0
            for j in range(i):
                if customers[j] == 'N': penalty += 1
            for j in range(i, n):
                if customers[j] == 'Y': penalty += 1
            if penalty < min_penalty:
                min_penalty = penalty
                best_time = i
        return best_time
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int min_penalty;
    int best_time;
} Solution;

int bestClosingTime(char * customers) {
    int n = strlen(customers);
    int min_penalty = INT_MAX;
    int best_time = 0;
    for (int i = 0; i <= n; i++) {
        int penalty = 0;
        for (int j = 0; j < i; j++) {
            if (customers[j] == 'N') penalty++;
        }
        for (int j = i; j < n; j++) {
            if (customers[j] == 'Y') penalty++;
        }
        if (penalty < min_penalty) {
            min_penalty = penalty;
            best_time = i;
        }
    }
    return best_time;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int BestClosingTime(string customers) {
        int n = customers.Length;
        int min_penalty = int.MaxValue;
        int best_time = 0;
        for (int i = 0; i <= n; i++) {
            int penalty = 0;
            for (int j = 0; j < i; j++) {
                if (customers[j] == 'N') penalty++;
            }
            for (int j = i; j < n; j++) {
                if (customers[j] == 'Y') penalty++;
            }
            if (penalty < min_penalty) {
                min_penalty = penalty;
                best_time = i;
            }
        }
        return best_time;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var bestClosingTime = function(customers) {
    let n = customers.length;
    let min_penalty = Infinity;
    let best_time = 0;
    for (let i = 0; i <= n; i++) {
        let penalty = 0;
        for (let j = 0; j < i; j++) {
            if (customers[j] === 'N') penalty++;
        }
        for (let j = i; j < n; j++) {
            if (customers[j] === 'Y') penalty++;
        }
        if (penalty < min_penalty) {
            min_penalty = penalty;
            best_time = i;
        }
    }
    return best_time;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function bestClosingTime(customers: string): number {
    let n: number = customers.length;
    let min_penalty: number = Infinity;
    let best_time: number = 0;
    for (let i: number = 0; i <= n; i++) {
        let penalty: number = 0;
        for (let j: number = 0; j < i; j++) {
            if (customers[j] === 'N') penalty++;
        }
        for (let j: number = i; j < n; j++) {
            if (customers[j] === 'Y') penalty++;
        }
        if (penalty < min_penalty) {
            min_penalty = penalty;
            best_time = i;
        }
    }
    return best_time;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function bestClosingTime($customers) {
        $n = strlen($customers);
        $min_penalty = PHP_INT_MAX;
        $best_time = 0;
        for ($i = 0; $i <= $n; $i++) {
            $penalty = 0;
            for ($j = 0; $j < $i; $j++) {
                if ($customers[$j] == 'N') $penalty++;
            }
            for ($j = $i; $j < $n; $j++) {
                if ($customers[$j] == 'Y') $penalty++;
            }
            if ($penalty < $min_penalty) {
                $min_penalty = $penalty;
                $best_time = $i;
            }
        }
        return $best_time;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func bestClosingTime(_ customers: String) -> Int {
        let n = customers.count
        var min_penalty = Int.max
        var best_time = 0
        for i in 0...n {
            var penalty = 0
            for j in 0..<i {
                if customers[customers.index(customers.startIndex, offsetBy: j)] == "N" {
                    penalty += 1
                }
            }
            for j in i..<n {
                if customers[customers.index(customers.startIndex, offsetBy: j)] == "Y" {
                    penalty += 1
                }
            }
            if penalty < min_penalty {
                min_penalty = penalty
                best_time = i
            }
        }
        return best_time
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun bestClosingTime(customers: String): Int {
        val n = customers.length
        var min_penalty = Int.MAX_VALUE
        var best_time = 0
        for (i in 0..n) {
            var penalty = 0
            for (j in 0 until i) {
                if (customers[j] == 'N') penalty++
            }
            for (j in i until n) {
                if (customers[j] == 'Y') penalty++
            }
            if (penalty < min_penalty) {
                min_penalty = penalty
                best_time = i
            }
        }
        return best_time
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int bestClosingTime(String customers) {
        int n = customers.length;
        int min_penalty = double.maxFinite.toInt();
        int best_time = 0;
        for (int i = 0; i <= n; i++) {
            int penalty = 0;
            for (int j = 0; j < i; j++) {
                if (customers[j] == 'N') penalty++;
            }
            for (int j = i; j < n; j++) {
                if (customers[j] == 'Y') penalty++;
            }
            if (penalty < min_penalty) {
                min_penalty = penalty;
                best_time = i;
            }
        }
        return best_time;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
    "fmt"
)

type Solution struct{}

func (s Solution) bestClosingTime(customers string) int {
    n := len(customers)
    min_penalty := 100000
    best_time := 0
    for i := 0; i <= n; i++ {
        penalty := 0
        for j := 0; j < i; j++ {
            if customers[j] == 'N' {
                penalty++
            }
        }
        for j := i; j < n; j++ {
            if customers[j] == 'Y' {
                penalty++
            }
        }
        if penalty < min_penalty {
            min_penalty = penalty
            best_time = i
        }
    }
    return best_time
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def best_closing_time(customers)
        n = customers.length
        min_penalty = Float::INFINITY
        best_time = 0
        (0..n).each do |i|
            penalty = 0
            (0...i).each do |j|
                penalty += 1 if customers[j] == 'N'
            end
            (i...n).each do |j|
                penalty += 1 if customers[j] == 'Y'
            end
            if penalty < min_penalty
                min_penalty = penalty
                best_time = i
            end
        end
        best_time
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def bestClosingTime(customers: String): Int = {
        val n = customers.length
        var min_penalty = Int.MaxValue
        var best_time = 0
        for (i <- 0 to n) {
            var penalty = 0
            for (j <- 0 until i) {
                if (customers(j) == 'N') penalty += 1
            }
            for (j <- i until n) {
                if (customers(j) == 'Y') penalty += 1
            }
            if (penalty < min_penalty) {
                min_penalty = penalty
                best_time = i
            }
        }
        best_time
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;

impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let n = customers.len();
        let mut min_penalty = i32::MAX;
        let mut best_time = 0;
        for i in 0..=n {
            let mut penalty = 0;
            for j in 0..i {
                if customers.as_bytes()[j] as char == 'N' {
                    penalty += 1;
                }
            }
            for j in i..n {
                if customers.as_bytes()[j] as char == 'Y' {
                    penalty += 1;
                }
            }
            if penalty < min_penalty {
                min_penalty = penalty;
                best_time = i;
            }
        }
        best_time as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (best-closing-time customers)
    (let ((n (string-length customers))
          (min-penalty +inf.0)
          (best-time 0))
      (do ((i 0 (+ i 1))) ((> i n))
        (let ((penalty 0))
          (do ((j 0 (+ j 1))) ((> j i))
            (when (eq? (string-ref customers j) #\N)
              (set! penalty (+ penalty 1))))
          (do ((j i (+ j 1))) ((> j n))
            (when (eq? (string-ref customers j) #\Y)
              (set! penalty (+ penalty 1))))
          (when (< penalty min-penalty)
            (set! min-penalty penalty)
            (set! best-time i))))
      best-time))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
best_closing_time(Customers) ->
    N = length(Customers),
    Min_penalty = infinity,
    Best_time = 0,
    lists:foldl(fun(I, {Min_penalty0, Best_time0}) ->
        Penalty = lists:foldl(fun(J, Penalty0) when J < I andalso lists:nth(J + 1, Customers) =:= $N -> Penalty0 + 1;
                                    (J, Penalty0) when J >= I andalso lists:nth(J + 1, Customers) =:= $Y -> Penalty0 + 1;
                                    (_, Penalty0) -> Penalty0 end, 0, lists:seq(0, N)),
        if
            Penalty < Min_penalty0 -> {Penalty, I};
            true -> {Min_penalty0, Best_time0}
        end
    end, {Min_penalty, Best_time}, lists:seq(0, N)),
    element(2, {Min_penalty, Best_time}).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def best_closing_time(customers) do
        n = String.length(customers)
        min_penalty = :infinity
        best_time = 0
        Enum.reduce(0..n, {min_penalty, best_time}, fn i, {min_penalty, best_time} ->
            penalty = Enum.reduce(0..i-1, 0, fn j, penalty ->
                if String.at(customers, j) == "N", do: penalty + 1, else: penalty
            end) + Enum.reduce(i..n-1, 0, fn j, penalty ->
                if String.at(customers, j) == "Y", do: penalty + 1, else: penalty
            end)
            if penalty < min_penalty, do: {penalty, i}, else: {min_penalty, best_time}
        end)
        |> elem(1)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n), where n is the length of the input string. This is because we iterate over each possible closing time once, and for each closing time, we calculate the penalty in O(1) time.

- **Space Complexity:** The space complexity of the solution is O(1), which means the space required does not change with the size of the input string, making it very efficient in terms of memory usage.

</div>
</details>
