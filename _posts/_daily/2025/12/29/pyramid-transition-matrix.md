---
layout: post
title: "Pyramid Transition Matrix"
date: 2025-12-29 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String", "Backtracking", "Bit Manipulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/pyramid-transition-matrix/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    std::unordered_map<std::string, std::vector<char>>\
        \ allowed_map;\n    std::unordered_map<std::string, bool> memo;\n\n    bool\
        \ pyramidTransition(std::string bottom, std::vector<std::string>& allowed) {\n\
        \        for (const std::string& pattern : allowed) {\n            allowed_map[pattern.substr(0,\
        \ 2)].push_back(pattern[2]);\n        }\n\n        return can_build(bottom);\n\
        \    }\n\nprivate:\n    bool can_build(const std::string& current_row) {\n \
        \       if (memo.count(current_row)) {\n            return memo[current_row];\n\
        \        }\n\n        if (current_row.length() == 1) {\n            return true;\n\
        \        }\n\n        std::string next_row_builder = \"\";\n        bool result\
        \ = find_next_row(0, next_row_builder, current_row);\n        memo[current_row]\
        \ = result;\n        return result;\n    }\n\n    bool find_next_row(int index,\
        \ std::string& next_row_builder, const std::string& current_row) {\n       \
        \ if (index == current_row.length() - 1) {\n            return can_build(next_row_builder);\n\
        \        }\n\n        char left = current_row[index];\n        char right =\
        \ current_row[index + 1];\n        std::string key = \"\";\n        key += left;\n\
        \        key += right;\n\n        if (allowed_map.find(key) == allowed_map.end())\
        \ {\n            return false;\n        }\n\n        for (char top_char : allowed_map[key])\
        \ {\n            next_row_builder.push_back(top_char);\n            if (find_next_row(index\
        \ + 1, next_row_builder, current_row)) {\n                next_row_builder.pop_back();\
        \ \n                return true;\n            }\n            next_row_builder.pop_back();\
        \ \n        }\n\n        return false;\n    }\n};"
      java: "import java.util.List;\nimport java.util.ArrayList;\nimport java.util.Map;\n\
        import java.util.HashMap;\n\nclass Solution {\n    Map<String, List<Character>>\
        \ allowedMap;\n    Map<String, Boolean> memo;\n\n    public boolean pyramidTransition(String\
        \ bottom, List<String> allowed) {\n        allowedMap = new HashMap<>();\n \
        \       for (String pattern : allowed) {\n            String key = pattern.substring(0,\
        \ 2);\n            char value = pattern.charAt(2);\n            allowedMap.computeIfAbsent(key,\
        \ k -> new ArrayList<>()).add(value);\n        }\n\n        memo = new HashMap<>();\n\
        \n        return canBuild(bottom);\n    }\n\n    private boolean canBuild(String\
        \ currentRow) {\n        if (memo.containsKey(currentRow)) {\n            return\
        \ memo.get(currentRow);\n        }\n\n        if (currentRow.length() == 1)\
        \ {\n            return true;\n        }\n\n        StringBuilder nextRowBuilder\
        \ = new StringBuilder();\n        boolean result = findNextRow(0, nextRowBuilder,\
        \ currentRow);\n        memo.put(currentRow, result);\n        return result;\n\
        \    }\n\n    private boolean findNextRow(int index, StringBuilder nextRowBuilder,\
        \ String currentRow) {\n        if (index == currentRow.length() - 1) {\n  \
        \          return canBuild(nextRowBuilder.toString());\n        }\n\n      \
        \  char left = currentRow.charAt(index);\n        char right = currentRow.charAt(index\
        \ + 1);\n        String key = \"\" + left + right;\n\n        if (!allowedMap.containsKey(key))\
        \ {\n            return false;\n        }\n\n        for (char topChar : allowedMap.get(key))\
        \ {\n            nextRowBuilder.append(topChar);\n            if (findNextRow(index\
        \ + 1, nextRowBuilder, currentRow)) {\n                nextRowBuilder.deleteCharAt(nextRowBuilder.length()\
        \ - 1); \n                return true;\n            }\n            nextRowBuilder.deleteCharAt(nextRowBuilder.length()\
        \ - 1); \n        }\n\n        return false;\n    }\n}"
      python: "import collections\n\nclass Solution:\n    def pyramidTransition(self,\
        \ bottom: str, allowed: List[str]) -> bool:\n        allowed_map = collections.defaultdict(list)\n\
        \        for pattern in allowed:\n            allowed_map[pattern[0:2]].append(pattern[2])\n\
        \n        memo = {}\n\n        def can_build(current_row: str) -> bool:\n  \
        \          if current_row in memo:\n                return memo[current_row]\n\
        \n            if len(current_row) == 1:\n                return True\n\n   \
        \         result = find_next_row(0, [], current_row)\n            memo[current_row]\
        \ = result\n            return result\n\n        def find_next_row(index: int,\
        \ next_row_chars: List[str], current_row: str) -> bool:\n            if index\
        \ == len(current_row) - 1:\n                return can_build(\"\".join(next_row_chars))\n\
        \n            left = current_row[index]\n            right = current_row[index\
        \ + 1]\n            key = left + right\n\n            if key not in allowed_map:\n\
        \                return False \n\n            for top_char in allowed_map[key]:\n\
        \                next_row_chars.append(top_char)\n                if find_next_row(index\
        \ + 1, next_row_chars, current_row):\n                    next_row_chars.pop()\
        \ \n                    return True\n                next_row_chars.pop() \n\
        \n            return False \n\n        return can_build(bottom)"
      python3: "import collections\n\nclass Solution:\n    def pyramidTransition(self,\
        \ bottom: str, allowed: List[str]) -> bool:\n        allowed_map = collections.defaultdict(list)\n\
        \        for pattern in allowed:\n            allowed_map[pattern[0:2]].append(pattern[2])\n\
        \n        memo = {}\n\n        def can_build(current_row: str) -> bool:\n  \
        \          if current_row in memo:\n                return memo[current_row]\n\
        \n            if len(current_row) == 1:\n                return True\n\n   \
        \         result = find_next_row(0, [], current_row)\n            memo[current_row]\
        \ = result\n            return result\n\n        def find_next_row(index: int,\
        \ next_row_chars: List[str], current_row: str) -> bool:\n            if index\
        \ == len(current_row) - 1:\n                return can_build(\"\".join(next_row_chars))\n\
        \n            left = current_row[index]\n            right = current_row[index\
        \ + 1]\n            key = left + right\n\n            if key not in allowed_map:\n\
        \                return False \n\n            for top_char in allowed_map[key]:\n\
        \                next_row_chars.append(top_char)\n                if find_next_row(index\
        \ + 1, next_row_chars, current_row):\n                    next_row_chars.pop()\
        \ \n                    return True\n                next_row_chars.pop() \n\
        \n            return False \n\n        return can_build(bottom)"
      c: "#include <stdbool.h>\n#include <string.h>\n#include <stdlib.h>\n\nchar allowed_tops[6][6][7];\
        \ \nint memo[46656]; \n\nint encodeRow(const char* row) {\n    int hash = 0;\n\
        \    int len = strlen(row);\n    for (int i = 0; i < len; ++i) {\n        hash\
        \ = hash * 6 + (row[i] - 'A');\n    }\n    return hash;\n}\n\nbool canBuild(const\
        \ char* current_row);\nbool findNextRow(int index, char* next_row_builder, int\
        \ builder_len, const char* current_row);\n\nbool canBuild(const char* current_row)\
        \ {\n    int len = strlen(current_row);\n    if (len == 1) {\n        return\
        \ true;\n    }\n\n    int row_hash = encodeRow(current_row);\n    if (memo[row_hash]\
        \ != 0) {\n        return memo[row_hash] == 1;\n    }\n\n    char* next_row_builder\
        \ = (char*)malloc(sizeof(char) * len); \n    next_row_builder[0] = '\\0'; \n\
        \n    bool result = findNextRow(0, next_row_builder, 0, current_row);\n\n  \
        \  free(next_row_builder);\n    memo[row_hash] = result ? 1 : -1;\n    return\
        \ result;\n}\n\nbool findNextRow(int index, char* next_row_builder, int builder_len,\
        \ const char* current_row) {\n    int current_row_len = strlen(current_row);\n\
        \n    if (index == current_row_len - 1) {\n        next_row_builder[builder_len]\
        \ = '\\0'; \n        return canBuild(next_row_builder);\n    }\n\n    char left\
        \ = current_row[index];\n    char right = current_row[index + 1];\n\n    const\
        \ char* possible_tops = allowed_tops[left - 'A'][right - 'A'];\n\n    if (possible_tops[0]\
        \ == '\\0') {\n        return false;\n    }\n\n    for (int i = 0; possible_tops[i]\
        \ != '\\0'; ++i) {\n        char top_char = possible_tops[i];\n        next_row_builder[builder_len]\
        \ = top_char; \n\n        if (findNextRow(index + 1, next_row_builder, builder_len\
        \ + 1, current_row)) {\n            return true;\n        }\n    }\n\n    return\
        \ false;\n}\n\nbool pyramidTransition(char* bottom, char** allowed, int allowedSize)\
        \ {\n    memset(memo, 0, sizeof(memo));\n    for (int i = 0; i < 6; ++i) {\n\
        \        for (int j = 0; j < 6; ++j) {\n            allowed_tops[i][j][0] =\
        \ '\\0';\n        }\n    }\n\n    for (int k = 0; k < allowedSize; ++k) {\n\
        \        char* pattern = allowed[k];\n        char left = pattern[0];\n    \
        \    char right = pattern[1];\n        char top = pattern[2];\n\n        int\
        \ left_idx = left - 'A';\n        int right_idx = right - 'A';\n\n        int\
        \ current_len = strlen(allowed_tops[left_idx][right_idx]);\n        allowed_tops[left_idx][right_idx][current_len]\
        \ = top;\n        allowed_tops[left_idx][right_idx][current_len + 1] = '\\0';\n\
        \    }\n\n    return canBuild(bottom);\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Text;\n\
        \npublic class Solution {\n    private Dictionary<string, List<char>> allowedMap;\n\
        \    private Dictionary<string, bool> memo;\n\n    public bool PyramidTransition(string\
        \ bottom, IList<string> allowed) {\n        allowedMap = new Dictionary<string,\
        \ List<char>>();\n        foreach (string pattern in allowed) {\n          \
        \  string key = pattern.Substring(0, 2);\n            char value = pattern[2];\n\
        \            if (!allowedMap.ContainsKey(key)) {\n                allowedMap[key]\
        \ = new List<char>();\n            }\n            allowedMap[key].Add(value);\n\
        \        }\n\n        memo = new Dictionary<string, bool>();\n\n        return\
        \ CanBuild(bottom);\n    }\n\n    private bool CanBuild(string currentRow) {\n\
        \        if (memo.ContainsKey(currentRow)) {\n            return memo[currentRow];\n\
        \        }\n\n        if (currentRow.Length == 1) {\n            return true;\n\
        \        }\n\n        StringBuilder nextRowBuilder = new StringBuilder();\n\
        \        bool result = FindNextRow(0, nextRowBuilder, currentRow);\n       \
        \ memo[currentRow] = result;\n        return result;\n    }\n\n    private bool\
        \ FindNextRow(int index, StringBuilder nextRowBuilder, string currentRow) {\n\
        \        if (index == currentRow.Length - 1) {\n            return CanBuild(nextRowBuilder.ToString());\n\
        \        }\n\n        char left = currentRow[index];\n        char right = currentRow[index\
        \ + 1];\n        string key = \"\" + left + right;\n\n        if (!allowedMap.ContainsKey(key))\
        \ {\n            return false;\n        }\n\n        foreach (char topChar in\
        \ allowedMap[key]) {\n            nextRowBuilder.Append(topChar);\n        \
        \    if (FindNextRow(index + 1, nextRowBuilder, currentRow)) {\n           \
        \     nextRowBuilder.Remove(nextRowBuilder.Length - 1, 1); \n              \
        \  return true;\n            }\n            nextRowBuilder.Remove(nextRowBuilder.Length\
        \ - 1, 1); \n        }\n\n        return false;\n    }\n}"
      javascript: "/**\n * @param {string} bottom\n * @param {string[]} allowed\n *\
        \ @return {boolean}\n */\nvar pyramidTransition = function(bottom, allowed)\
        \ {\n    const allowedMap = new Map();\n    for (const pattern of allowed) {\n\
        \        const key = pattern.substring(0, 2);\n        const value = pattern[2];\n\
        \        if (!allowedMap.has(key)) {\n            allowedMap.set(key, []);\n\
        \        }\n        allowedMap.get(key).push(value);\n    }\n\n    const memo\
        \ = new Map();\n\n    const canBuild = (currentRow) => {\n        if (memo.has(currentRow))\
        \ {\n            return memo.get(currentRow);\n        }\n\n        if (currentRow.length\
        \ === 1) {\n            return true;\n        }\n\n        const nextRowChars\
        \ = [];\n        const result = findNextRow(0, nextRowChars, currentRow);\n\
        \        memo.set(currentRow, result);\n        return result;\n    };\n\n \
        \   const findNextRow = (index, nextRowChars, currentRow) => {\n        if (index\
        \ === currentRow.length - 1) {\n            return canBuild(nextRowChars.join(''));\n\
        \        }\n\n        const left = currentRow[index];\n        const right =\
        \ currentRow[index + 1];\n        const key = left + right;\n\n        if (!allowedMap.has(key))\
        \ {\n            return false;\n        }\n\n        for (const topChar of allowedMap.get(key))\
        \ {\n            nextRowChars.push(topChar);\n            if (findNextRow(index\
        \ + 1, nextRowChars, currentRow)) {\n                nextRowChars.pop(); \n\
        \                return true;\n            }\n            nextRowChars.pop();\
        \ \n        }\n\n        return false;\n    };\n\n    return canBuild(bottom);\n\
        };"
      typescript: "class Solution {\n    private allowedMap: Map<string, string[]>;\n\
        \    private memo: Map<string, boolean>;\n\n    public pyramidTransition(bottom:\
        \ string, allowed: string[]): boolean {\n        this.allowedMap = new Map<string,\
        \ string[]>();\n        for (const pattern of allowed) {\n            const\
        \ key = pattern.substring(0, 2);\n            const value = pattern[2];\n  \
        \          if (!this.allowedMap.has(key)) {\n                this.allowedMap.set(key,\
        \ []);\n            }\n            this.allowedMap.get(key)!.push(value);\n\
        \        }\n\n        this.memo = new Map<string, boolean>();\n\n        return\
        \ this.canBuild(bottom);\n    }\n\n    private canBuild(currentRow: string):\
        \ boolean {\n        if (this.memo.has(currentRow)) {\n            return this.memo.get(currentRow)!;\n\
        \        }\n\n        if (currentRow.length === 1) {\n            return true;\n\
        \        }\n\n        const nextRowChars: string[] = [];\n        const result\
        \ = this.findNextRow(0, nextRowChars, currentRow);\n        this.memo.set(currentRow,\
        \ result);\n        return result;\n    }\n\n    private findNextRow(index:\
        \ number, nextRowChars: string[], currentRow: string): boolean {\n        if\
        \ (index === currentRow.length - 1) {\n            return this.canBuild(nextRowChars.join(''));\n\
        \        }\n\n        const left = currentRow[index];\n        const right =\
        \ currentRow[index + 1];\n        const key = left + right;\n\n        const\
        \ possibleTops = this.allowedMap.get(key);\n        if (!possibleTops) {\n \
        \           return false;\n        }\n\n        for (const topChar of possibleTops)\
        \ {\n            nextRowChars.push(topChar);\n            if (this.findNextRow(index\
        \ + 1, nextRowChars, currentRow)) {\n                nextRowChars.pop(); \n\
        \                return true;\n            }\n            nextRowChars.pop();\
        \ \n        }\n\n        return false;\n    }\n}"
      php: "<?php\n\nclass Solution {\n    private $allowedMap;\n    private $memo;\n\
        \n    /**\n     * @param String $bottom\n     * @param String[] $allowed\n \
        \    * @return Boolean\n     */\n    function pyramidTransition($bottom, $allowed)\
        \ {\n        $this->allowedMap = [];\n        foreach ($allowed as $pattern)\
        \ {\n            $key = substr($pattern, 0, 2);\n            $value = $pattern[2];\n\
        \            if (!isset($this->allowedMap[$key])) {\n                $this->allowedMap[$key]\
        \ = [];\n            }\n            $this->allowedMap[$key][] = $value;\n  \
        \      }\n\n        $this->memo = [];\n\n        return $this->canBuild($bottom);\n\
        \    }\n\n    private function canBuild($currentRow) {\n        if (isset($this->memo[$currentRow]))\
        \ {\n            return $this->memo[$currentRow];\n        }\n\n        if (strlen($currentRow)\
        \ == 1) {\n            return true;\n        }\n\n        $nextRowChars = [];\n\
        \        $result = $this->findNextRow(0, $nextRowChars, $currentRow);\n    \
        \    $this->memo[$currentRow] = $result;\n        return $result;\n    }\n\n\
        \    private function findNextRow($index, &$nextRowChars, $currentRow) {\n \
        \       if ($index == strlen($currentRow) - 1) {\n            return $this->canBuild(implode('',\
        \ $nextRowChars));\n        }\n\n        $left = $currentRow[$index];\n    \
        \    $right = $currentRow[$index + 1];\n        $key = $left . $right;\n\n \
        \       if (!isset($this->allowedMap[$key])) {\n            return false;\n\
        \        }\n\n        foreach ($this->allowedMap[$key] as $topChar) {\n    \
        \        $nextRowChars[] = $topChar;\n            if ($this->findNextRow($index\
        \ + 1, $nextRowChars, $currentRow)) {\n                array_pop($nextRowChars);\
        \ \n                return true;\n            }\n            array_pop($nextRowChars);\
        \ \n        }\n\n        return false;\n    }\n}"
      swift: "class Solution {\n    private var allowedMap: [String: [Character]] =\
        \ [:]\n    private var memo: [String: Bool] = [:]\n\n    func pyramidTransition(_\
        \ bottom: String, _ allowed: [String]) -> Bool {\n        for pattern in allowed\
        \ {\n            let key = String(pattern.prefix(2))\n            let value\
        \ = pattern.last!\n            allowedMap[key, default: []].append(value)\n\
        \        }\n\n        return canBuild(bottom)\n    }\n\n    private func canBuild(_\
        \ currentRow: String) -> Bool {\n        if let result = memo[currentRow] {\n\
        \            return result\n        }\n\n        if currentRow.count == 1 {\n\
        \            return true\n        }\n\n        var nextRowChars: [Character]\
        \ = []\n        let result = findNextRow(0, &nextRowChars, currentRow)\n   \
        \     memo[currentRow] = result\n        return result\n    }\n\n    private\
        \ func findNextRow(_ index: Int, _ nextRowChars: inout [Character], _ currentRow:\
        \ String) -> Bool {\n        if index == currentRow.count - 1 {\n          \
        \  return canBuild(String(nextRowChars))\n        }\n\n        let currentChars\
        \ = Array(currentRow)\n        let left = currentChars[index]\n        let right\
        \ = currentChars[index + 1]\n        let key = String([left, right])\n\n   \
        \     guard let possibleTops = allowedMap[key] else {\n            return false\n\
        \        }\n\n        for topChar in possibleTops {\n            nextRowChars.append(topChar)\n\
        \            if findNextRow(index + 1, &nextRowChars, currentRow) {\n      \
        \          nextRowChars.removeLast() \n                return true\n       \
        \     }\n            nextRowChars.removeLast() \n        }\n\n        return\
        \ false\n    }\n}"
      kotlin: "class Solution {\n    private lateinit var allowedMap: MutableMap<String,\
        \ MutableList<Char>>\n    private lateinit var memo: MutableMap<String, Boolean>\n\
        \n    fun pyramidTransition(bottom: String, allowed: List<String>): Boolean\
        \ {\n        allowedMap = mutableMapOf()\n        for (pattern in allowed) {\n\
        \            val key = pattern.substring(0, 2)\n            val value = pattern[2]\n\
        \            allowedMap.computeIfAbsent(key) { mutableListOf() }.add(value)\n\
        \        }\n\n        memo = mutableMapOf()\n\n        return canBuild(bottom)\n\
        \    }\n\n    private fun canBuild(currentRow: String): Boolean {\n        if\
        \ (memo.containsKey(currentRow)) {\n            return memo[currentRow]!!\n\
        \        }\n\n        if (currentRow.length == 1) {\n            return true\n\
        \        }\n\n        val nextRowBuilder = StringBuilder()\n        val result\
        \ = findNextRow(0, nextRowBuilder, currentRow)\n        memo[currentRow] = result\n\
        \        return result\n    }\n\n    private fun findNextRow(index: Int, nextRowBuilder:\
        \ StringBuilder, currentRow: String): Boolean {\n        if (index == currentRow.length\
        \ - 1) {\n            return canBuild(nextRowBuilder.toString())\n        }\n\
        \n        val left = currentRow[index]\n        val right = currentRow[index\
        \ + 1]\n        val key = \"$left$right\"\n\n        val possibleTops = allowedMap[key]\n\
        \        if (possibleTops == null) {\n            return false\n        }\n\n\
        \        for (topChar in possibleTops) {\n            nextRowBuilder.append(topChar)\n\
        \            if (findNextRow(index + 1, nextRowBuilder, currentRow)) {\n   \
        \             nextRowBuilder.deleteCharAt(nextRowBuilder.length - 1); \n   \
        \             return true\n            }\n            nextRowBuilder.deleteCharAt(nextRowBuilder.length\
        \ - 1); \n        }\n\n        return false;\n    }\n}"
      dart: "class Solution {\n  late Map<String, List<String>> allowedMap;\n  late\
        \ Map<String, bool> memo;\n\n  bool pyramidTransition(String bottom, List<String>\
        \ allowed) {\n    allowedMap = {};\n    for (final pattern in allowed) {\n \
        \     final key = pattern.substring(0, 2);\n      final value = pattern[2];\n\
        \      allowedMap.putIfAbsent(key, () => []).add(value);\n    }\n\n    memo\
        \ = {};\n\n    return _canBuild(bottom);\n  }\n\n  bool _canBuild(String currentRow)\
        \ {\n    if (memo.containsKey(currentRow)) {\n      return memo[currentRow]!;\n\
        \    }\n\n    if (currentRow.length == 1) {\n      return true;\n    }\n\n \
        \   final nextRowChars = <String>[];\n    final result = _findNextRow(0, nextRowChars,\
        \ currentRow);\n    memo[currentRow] = result;\n    return result;\n  }\n\n\
        \  bool _findNextRow(int index, List<String> nextRowChars, String currentRow)\
        \ {\n    if (index == currentRow.length - 1) {\n      return _canBuild(nextRowChars.join(''));\n\
        \    }\n\n    final left = currentRow[index];\n    final right = currentRow[index\
        \ + 1];\n    final key = left + right;\n\n    final possibleTops = allowedMap[key];\n\
        \    if (possibleTops == null) {\n      return false;\n    }\n\n    for (final\
        \ topChar in possibleTops) {\n      nextRowChars.add(topChar);\n      if (_findNextRow(index\
        \ + 1, nextRowChars, currentRow)) {\n        nextRowChars.removeLast(); \n \
        \       return true;\n      }\n      nextRowChars.removeLast(); \n    }\n\n\
        \    return false;\n  }\n}"
      go: "package main\n\nimport (\n\t\"strings\"\n)\n\ntype PyramidHelper struct {\n\
        \tallowedMap map[string][]rune\n\tmemo       map[string]bool\n}\n\nfunc (s *PyramidHelper)\
        \ canBuild(currentRow string) bool {\n\tif val, ok := s.memo[currentRow]; ok\
        \ {\n\t\treturn val\n\t}\n\n\tif len(currentRow) == 1 {\n\t\treturn true\n\t\
        }\n\n\tnextRowChars := make([]rune, 0, len(currentRow)-1) \n\tresult := s.findNextRow(0,\
        \ nextRowChars, currentRow)\n\ts.memo[currentRow] = result\n\treturn result\n\
        }\n\nfunc (s *PyramidHelper) findNextRow(index int, nextRowChars []rune, currentRow\
        \ string) bool {\n\tif index == len(currentRow)-1 {\n\t\treturn s.canBuild(string(nextRowChars))\n\
        \t}\n\n\tleft := rune(currentRow[index])\n\tright := rune(currentRow[index+1])\n\
        \tkey := string([]rune{left, right})\n\n\tpossibleTops, ok := s.allowedMap[key]\n\
        \tif !ok {\n\t\treturn false\n\t}\n\n\tfor _, topChar := range possibleTops\
        \ {\n\t\tif s.findNextRow(index+1, append(nextRowChars, topChar), currentRow)\
        \ {\n\t\t\treturn true\n\t\t}\n\t}\n\n\treturn false\n}\n\nfunc pyramidTransition(bottom\
        \ string, allowed []string) bool {\n\tallowedMap := make(map[string][]rune)\n\
        \tfor _, pattern := range allowed {\n\t\tkey := pattern[0:2]\n\t\tvalue := rune(pattern[2])\n\
        \t\tallowedMap[key] = append(allowedMap[key], value)\n\t}\n\n\thelper := PyramidHelper{\n\
        \t\tallowedMap: allowedMap,\n\t\tmemo:       make(map[string]bool),\n\t}\n\t\
        return helper.canBuild(bottom)\n}"
      ruby: "class Solution\n    def pyramid_transition(bottom, allowed)\n        @allowed_map\
        \ = Hash.new { |hash, key| hash[key] = [] }\n        allowed.each do |pattern|\n\
        \            @allowed_map[pattern[0..1]] << pattern[2]\n        end\n\n    \
        \    @memo = {}\n\n        can_build(bottom)\n    end\n\n    private\n\n   \
        \ def can_build(current_row)\n        return @memo[current_row] if @memo.key?(current_row)\n\
        \n        return true if current_row.length == 1\n\n        next_row_chars =\
        \ []\n        result = find_next_row(0, next_row_chars, current_row)\n     \
        \   @memo[current_row] = result\n        result\n    end\n\n    def find_next_row(index,\
        \ next_row_chars, current_row)\n        if index == current_row.length - 1\n\
        \            return can_build(next_row_chars.join(''))\n        end\n\n    \
        \    left = current_row[index]\n        right = current_row[index + 1]\n   \
        \     key = left + right\n\n        return false unless @allowed_map.key?(key)\n\
        \n        @allowed_map[key].each do |top_char|\n            next_row_chars <<\
        \ top_char\n            if find_next_row(index + 1, next_row_chars, current_row)\n\
        \                next_row_chars.pop \n                return true\n        \
        \    end\n            next_row_chars.pop \n        end\n\n        false\n  \
        \  end\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def pyramidTransition(bottom:\
        \ String, allowed: List[String]): Boolean = {\n        val allowedMap: mutable.Map[String,\
        \ List[Char]] = mutable.Map.empty\n        for (pattern <- allowed) {\n    \
        \        val key = pattern.substring(0, 2)\n            val value = pattern.charAt(2)\n\
        \            allowedMap.update(key, allowedMap.getOrElse(key, List.empty) :+\
        \ value)\n        }\n\n        val memo: mutable.Map[String, Boolean] = mutable.Map.empty\n\
        \n        def canBuild(currentRow: String): Boolean = {\n            if (memo.contains(currentRow))\
        \ {\n                return memo(currentRow)\n            }\n\n            if\
        \ (currentRow.length == 1) {\n                return true\n            }\n\n\
        \            val nextRowBuilder = new StringBuilder()\n            val result\
        \ = findNextRow(0, nextRowBuilder, currentRow)\n            memo.update(currentRow,\
        \ result)\n            result\n        }\n\n        def findNextRow(index: Int,\
        \ nextRowBuilder: StringBuilder, currentRow: String): Boolean = {\n        \
        \    if (index == currentRow.length - 1) {\n                return canBuild(nextRowBuilder.toString())\n\
        \            }\n\n            val left = currentRow(index)\n            val\
        \ right = currentRow(index + 1)\n            val key = s\"$left$right\"\n\n\
        \            allowedMap.get(key) match {\n                case Some(possibleTops)\
        \ =>\n                    for (topChar <- possibleTops) {\n                \
        \        nextRowBuilder.append(topChar)\n                        if (findNextRow(index\
        \ + 1, nextRowBuilder, currentRow)) {\n                            nextRowBuilder.deleteCharAt(nextRowBuilder.length\
        \ - 1) \n                            return true\n                        }\n\
        \                        nextRowBuilder.deleteCharAt(nextRowBuilder.length -\
        \ 1) \n                    }\n                    false\n                case\
        \ None => false\n            }\n        }\n\n        canBuild(bottom)\n    }\n\
        }"
      rust: "use std::collections::HashMap;\n\nstruct Solution;\n\nimpl Solution {\n\
        \    pub fn pyramid_transition(bottom: String, allowed: Vec<String>) -> bool\
        \ {\n        let mut allowed_map: HashMap<String, Vec<char>> = HashMap::new();\n\
        \        for pattern in allowed {\n            let key = pattern[0..2].to_string();\n\
        \            let value = pattern.chars().nth(2).unwrap();\n            allowed_map.entry(key).or_insert_with(Vec::new).push(value);\n\
        \        }\n\n        let mut helper = PyramidHelper {\n            allowed_map,\n\
        \            memo: HashMap::new(),\n        };\n        helper.can_build(bottom)\n\
        \    }\n}\n\nstruct PyramidHelper {\n    allowed_map: HashMap<String, Vec<char>>,\n\
        \    memo: HashMap<String, bool>,\n}\n\nimpl PyramidHelper {\n    fn can_build(&mut\
        \ self, current_row: String) -> bool {\n        if let Some(&result) = self.memo.get(&current_row)\
        \ {\n            return result;\n        }\n\n        if current_row.len() ==\
        \ 1 {\n            return true;\n        }\n\n        let mut next_row_chars:\
        \ Vec<char> = Vec::new();\n        let result = self.find_next_row(0, &mut next_row_chars,\
        \ &current_row);\n        self.memo.insert(current_row, result);\n        result\n\
        \    }\n\n    fn find_next_row(&mut self, index: usize, next_row_chars: &mut\
        \ Vec<char>, current_row: &str) -> bool {\n        if index == current_row.len()\
        \ - 1 {\n            return self.can_build(next_row_chars.iter().collect());\n\
        \        }\n\n        let current_chars: Vec<char> = current_row.chars().collect();\
        \ \n        let left = current_chars[index];\n        let right = current_chars[index\
        \ + 1];\n        let key = format!(\"{}{}\", left, right);\n\n        if let\
        \ Some(possible_tops) = self.allowed_map.get(&key) {\n            for &top_char\
        \ in possible_tops {\n                next_row_chars.push(top_char);\n     \
        \           if self.find_next_row(index + 1, next_row_chars, current_row) {\n\
        \                    next_row_chars.pop(); \n                    return true;\n\
        \                }\n                next_row_chars.pop(); \n            }\n\
        \        }\n\n        false\n    }\n}"
      racket: "#lang racket\n\n(define (pyramid-transition bottom allowed)\n  (define\
        \ allowed-map (make-hash))\n  (for ([pattern allowed])\n    (define key (substring\
        \ pattern 0 2))\n    (define value (string-ref pattern 2))\n    (hash-update!\
        \ allowed-map key (lambda (lst) (cons value lst)) (list)))\n\n  (define memo\
        \ (make-hash))\n\n  (define (can-build current-row)\n    (cond\n      [(hash-has-key?\
        \ memo current-row)\n       (hash-ref memo current-row)]\n      [(equal? (string-length\
        \ current-row) 1)\n       (hash-set! memo current-row #t)\n       #t]\n    \
        \  [else\n       (define result (find-next-row 0 '() current-row))\n       (hash-set!\
        \ memo current-row result)\n       result]))\n\n  (define (find-next-row index\
        \ next-row-chars current-row)\n    (define current-row-len (string-length current-row))\n\
        \    (cond\n      [(= index (- current-row-len 1))\n       (can-build (list->string\
        \ (reverse next-row-chars)))]\n      [else\n       (define left (string-ref\
        \ current-row index))\n       (define right (string-ref current-row (+ index\
        \ 1)))\n       (define key (string left right))\n\n       (cond\n         [(hash-has-key?\
        \ allowed-map key)\n          (define possible-tops (hash-ref allowed-map key))\n\
        \          (ormap (lambda (top-char)\n                   (find-next-row (+ index\
        \ 1) (cons top-char next-row-chars) current-row))\n                 possible-tops)]\n\
        \         [else #f])]))\n\n  (can-build bottom))\n\n(provide pyramid-transition)"
      erlang: "-module(solution).\n-export([pyramidTransition/2]).\n\npyramidTransition(Bottom,\
        \ Allowed) ->\n    AllowedMap = lists:foldl(\n        fun(Pattern, Acc) ->\n\
        \            Key = string:substr(Pattern, 1, 2),\n            Value = string:substr(Pattern,\
        \ 3, 1),\n            maps:update_with(Key, fun(OldValues) -> OldValues ++ Value\
        \ end, Value, Acc)\n        end,\n        maps:new(),\n        Allowed\n   \
        \ ),\n\n    put(memo, maps:new()),\n\n    Result = can_build(Bottom, AllowedMap),\n\
        \    erase(memo),\n    Result.\n\ncan_build(CurrentRow, AllowedMap) ->\n   \
        \ Memo = get(memo),\n    case maps:find(CurrentRow, Memo) of\n        {ok, Result}\
        \ -> Result;\n        _ ->\n            case length(CurrentRow) of\n       \
        \         1 -> \n                    put(memo, maps:put(CurrentRow, true, Memo)),\n\
        \                    true;\n                _ ->\n                    Result\
        \ = find_next_row(0, [], CurrentRow, AllowedMap),\n                    put(memo,\
        \ maps:put(CurrentRow, Result, Memo)),\n                    Result\n       \
        \     end\n    end.\n\nfind_next_row(Index, NextRowChars, CurrentRow, AllowedMap)\
        \ ->\n    CurrentRowLen = length(CurrentRow),\n    if Index == CurrentRowLen\
        \ - 1 ->\n        can_build(lists:reverse(NextRowChars), AllowedMap);\n    true\
        \ ->\n        Left = lists:nth(Index + 1, CurrentRow),\n        Right = lists:nth(Index\
        \ + 2, CurrentRow),\n        Key = [Left, Right],\n\n        case maps:find(Key,\
        \ AllowedMap) of\n            {ok, PossibleTops} ->\n                find_next_row_loop(PossibleTops,\
        \ Index, NextRowChars, CurrentRow, AllowedMap);\n            _ ->\n        \
        \        false\n        end\n    end.\n\nfind_next_row_loop([], _Index, _NextRowChars,\
        \ _CurrentRow, _AllowedMap) ->\n    false;\nfind_next_row_loop([TopChar | Rest],\
        \ Index, NextRowChars, CurrentRow, AllowedMap) ->\n    case find_next_row(Index\
        \ + 1, [TopChar | NextRowChars], CurrentRow, AllowedMap) of\n        true ->\
        \ true;\n        false -> find_next_row_loop(Rest, Index, NextRowChars, CurrentRow,\
        \ AllowedMap)\n    end."
      elixir: "defmodule Solution do\n  @spec pyramid_transition(bottom :: String.t,\
        \ allowed :: [String.t]) :: boolean\n  def pyramid_transition(bottom, allowed)\
        \ do\n    allowed_map = Enum.reduce(allowed, %{}, fn pattern, acc ->\n     \
        \ key = String.slice(pattern, 0, 2)\n      value = String.at(pattern, 2)\n \
        \     Map.update(acc, key, [value], fn old_values -> old_values ++ [value] end)\n\
        \    end)\n\n    Process.put(:memo, %{})\n\n    result = can_build(bottom, allowed_map)\n\
        \    Process.delete(:memo)\n    result\n  end\n\n  defp can_build(current_row,\
        \ allowed_map) do\n    memo = Process.get(:memo)\n    if Map.has_key?(memo,\
        \ current_row) do\n      Map.get(memo, current_row)\n    else\n      result\
        \ = \n        if String.length(current_row) == 1 do\n          true\n      \
        \  else\n          find_next_row(0, [], current_row, allowed_map)\n        end\n\
        \      Process.put(:memo, Map.put(memo, current_row, result))\n      result\n\
        \    end\n  end\n\n  defp find_next_row(index, next_row_chars, current_row,\
        \ allowed_map) do\n    current_row_len = String.length(current_row)\n    if\
        \ index == current_row_len - 1 do\n      can_build(Enum.reverse(next_row_chars)\
        \ |> List.to_string(), allowed_map)\n    else\n      left = String.at(current_row,\
        \ index)\n      right = String.at(current_row, index + 1)\n      key = left\
        \ <> right\n\n      case Map.get(allowed_map, key) do\n        nil -> false\n\
        \        possible_tops ->\n          Enum.any?(possible_tops, fn top_char ->\n\
        \            find_next_row(index + 1, [top_char | next_row_chars], current_row,\
        \ allowed_map)\n          end)\n      end\n    end\n  end\nend"
    approach: The problem is solved using a recursive backtracking approach with memoization.
      We start from the given `bottom` row and attempt to build the pyramid upwards,
      one row at a time, until a single block remains at the top. The core idea is to
      define a recursive function `can_build(current_row)` that returns `true` if a
      pyramid can be built starting from `current_row`, and `false` otherwise. The base
      case for `can_build` is when `current_row` has only one block, in which case it
      returns `true` as the pyramid is complete.
    time_complexity: Let `N` be the length of the `bottom` string (maximum 6) and `M`
      be the size of the alphabet (maximum 6, for 'A' through 'F'). The recursion depth
      is `N`. The number of unique row strings that can be encountered is `sum_{k=1
      to N} M^k`. For `N=6, M=6`, this is approximately `5.6 * 10^4`. For each unique
      `current_row` of length `L`, we call a helper function `find_next_row` which explores
      possibilities for the next row. `find_next_row` is a backtracking function that
      iterates through `L-1` positions. For each position, it tries up to `M` possible
      top characters. The cost of `find_next_row` for a given `current_row` is `O(L
      * M)` in the worst case (when it has to explore all branches for a single block
      before finding a successful path or failing). Therefore, the total time complexity
      is `O(N * M^(N+1))`. With `N=6` and `M=6`, this is `6 * 6^7 = 6^8 = 1,679,616`
      operations, which is well within typical time limits.
    space_complexity: The space complexity is dominated by the memoization table and
      the recursion stack. The `allowed_map` stores `O(allowed.length)` entries. The
      `memo` table stores results for up to `sum_{k=1 to N} M^k` unique row strings.
      Each string has a maximum length of `N`. Thus, the space for memoization is `O(N
      * M^N)`. The recursion stack depth is `N`, and each frame stores a row string
      of length up to `N` (or a character list/builder). So, the stack space is `O(N^2)`.
      The dominant term is `O(N * M^N)`. With `N=6` and `M=6`, this is `6 * 6^6 = 279,936`
      characters/entries, which is acceptable.
    elapsed_time: 136.06478834152222
    model: gemini-2.5-flash
    generated_at: '2025-12-29 01:15:20 '
  - solutions:
      cpp: "class Solution {\npublic:\n    bool pyramidTransition(string bottom, vector<string>&\
        \ allowed) {\n        unordered_map<string, vector<char>> m;\n        for (auto&\
        \ s : allowed) {\n            m[s.substr(0, 2)].push_back(s[2]);\n        }\n\
        \        unordered_set<string> memo;\n        function<bool(string)> dfs = [&](string\
        \ s) {\n            if (s.size() == 1) return true;\n            if (memo.count(s))\
        \ return false;\n            vector<string> next;\n            get(s, next,\
        \ m);\n            if (next.empty()) {\n                memo.insert(s);\n  \
        \              return false;\n            }\n            for (auto& n : next)\
        \ {\n                if (dfs(n)) return true;\n            }\n            memo.insert(s);\n\
        \            return false;\n        };\n        return dfs(bottom);\n    }\n\
        \n    void get(string s, vector<string>& next, unordered_map<string, vector<char>>&\
        \ m) {\n        vector<string> temp = {\"\"};\n        for (int i = 0; i < s.size()\
        \ - 1; i++) {\n            string key = s.substr(i, 2);\n            vector<string>\
        \ t;\n            for (auto& n : temp) {\n                for (auto& c : m[key])\
        \ {\n                    t.push_back(n + c);\n                }\n          \
        \  }\n            temp = t;\n        }\n        next = temp;\n    }\n};"
      java: "class Solution {\n    public boolean pyramidTransition(String bottom, String[]\
        \ allowed) {\n        Map<String, List<Character>> m = new HashMap<>();\n  \
        \      for (String s : allowed) {\n            m.computeIfAbsent(s.substring(0,\
        \ 2), k -> new ArrayList<>()).add(s.charAt(2));\n        }\n        Set<String>\
        \ memo = new HashSet<>();\n        return dfs(bottom, m, memo);\n    }\n\n \
        \   private boolean dfs(String s, Map<String, List<Character>> m, Set<String>\
        \ memo) {\n        if (s.length() == 1) return true;\n        if (memo.contains(s))\
        \ return false;\n        List<String> next = get(s, m);\n        if (next.isEmpty())\
        \ {\n            memo.add(s);\n            return false;\n        }\n      \
        \  for (String n : next) {\n            if (dfs(n, m, memo)) return true;\n\
        \        }\n        memo.add(s);\n        return false;\n    }\n\n    private\
        \ List<String> get(String s, Map<String, List<Character>> m) {\n        List<String>\
        \ temp = new ArrayList<>();\n        temp.add(\"\");\n        for (int i = 0;\
        \ i < s.length() - 1; i++) {\n            String key = s.substring(i, i + 2);\n\
        \            List<String> t = new ArrayList<>();\n            for (String n\
        \ : temp) {\n                for (char c : m.getOrDefault(key, new ArrayList<>()))\
        \ {\n                    t.add(n + c);\n                }\n            }\n \
        \           temp = t;\n        }\n        return temp;\n    }\n}"
      python: "class Solution:\n    def pyramidTransition(self, bottom: str, allowed:\
        \ List[str]) -> bool:\n        m = {}\n        for s in allowed:\n         \
        \   if s[:2] not in m:\n                m[s[:2]] = []\n            m[s[:2]].append(s[2])\n\
        \        memo = set()\n        def dfs(s):\n            if len(s) == 1:\n  \
        \              return True\n            if s in memo:\n                return\
        \ False\n            next_level = get(s, m)\n            if not next_level:\n\
        \                memo.add(s)\n                return False\n            for\
        \ n in next_level:\n                if dfs(n):\n                    return True\n\
        \            memo.add(s)\n            return False\n        def get(s, m):\n\
        \            temp = [\"\"]\n            for i in range(len(s) - 1):\n      \
        \          key = s[i:i+2]\n                t = []\n                for n in\
        \ temp:\n                    for c in m.get(key, []):\n                    \
        \    t.append(n + c)\n                temp = t\n            return temp\n  \
        \      return dfs(bottom)"
      python3: "class Solution:\n    def pyramidTransition(self, bottom: str, allowed:\
        \ List[str]) -> bool:\n        m = {}\n        for s in allowed:\n         \
        \   if s[:2] not in m:\n                m[s[:2]] = []\n            m[s[:2]].append(s[2])\n\
        \        memo = set()\n        def dfs(s):\n            if len(s) == 1:\n  \
        \              return True\n            if s in memo:\n                return\
        \ False\n            next_level = get(s, m)\n            if not next_level:\n\
        \                memo.add(s)\n                return False\n            for\
        \ n in next_level:\n                if dfs(n):\n                    return True\n\
        \            memo.add(s)\n            return False\n        def get(s, m):\n\
        \            temp = [\"\"]\n            for i in range(len(s) - 1):\n      \
        \          key = s[i:i+2]\n                t = []\n                for n in\
        \ temp:\n                    for c in m.get(key, []):\n                    \
        \    t.append(n + c)\n                temp = t\n            return temp\n  \
        \      return dfs(bottom)"
      c: "typedef struct {\n    char key[3];\n    char value;\n} Pair;\n\nbool pyramidTransition(char\
        \ * bottom, char ** allowed, int allowedSize) {\n    Pair *m = (Pair *)malloc(sizeof(Pair)\
        \ * allowedSize);\n    for (int i = 0; i < allowedSize; i++) {\n        strcpy(m[i].key,\
        \ allowed[i]);\n        m[i].value = allowed[i][2];\n    }\n    bool *memo =\
        \ (bool *)malloc(sizeof(bool) * (1 << 20));\n    return dfs(bottom, m, allowedSize,\
        \ memo);\n}\n\nbool dfs(char *s, Pair *m, int size, bool *memo) {\n    if (strlen(s)\
        \ == 1) return true;\n    if (memo[(unsigned long long)s]) return false;\n \
        \   char **next = get(s, m, size);\n    if (!next) {\n        memo[(unsigned\
        \ long long)s] = true;\n        return false;\n    }\n    for (int i = 0; next[i];\
        \ i++) {\n        if (dfs(next[i], m, size, memo)) return true;\n    }\n   \
        \ memo[(unsigned long long)s] = true;\n    return false;\n}\n\nchar **get(char\
        \ *s, Pair *m, int size) {\n    char **temp = (char **)malloc(sizeof(char *)\
        \ * (1 << 10));\n    temp[0] = (char *)malloc(sizeof(char) * 2);\n    temp[0][0]\
        \ = '\\0';\n    int count = 1;\n    for (int i = 0; i < strlen(s) - 1; i++)\
        \ {\n        char key[3];\n        key[0] = s[i];\n        key[1] = s[i + 1];\n\
        \        key[2] = '\\0';\n        for (int j = 0; j < size; j++) {\n       \
        \     if (strcmp(m[j].key, key) == 0) {\n                for (int k = 0; k <\
        \ count; k++) {\n                    temp[count] = (char *)malloc(sizeof(char)\
        \ * (strlen(temp[k]) + 2));\n                    strcpy(temp[count], temp[k]);\n\
        \                    temp[count][strlen(temp[k])] = m[j].value;\n          \
        \          temp[count][strlen(temp[k]) + 1] = '\\0';\n                    count++;\n\
        \                }\n            }\n        }\n    }\n    temp[count] = NULL;\n\
        \    return temp;\n}"
      csharp: "public class Solution {\n    public bool PyramidTransition(string bottom,\
        \ string[] allowed) {\n        Dictionary<string, List<char>> m = new Dictionary<string,\
        \ List<char>>();\n        foreach (string s in allowed) {\n            if (!m.ContainsKey(s.Substring(0,\
        \ 2))) {\n                m[s.Substring(0, 2)] = new List<char>();\n       \
        \     }\n            m[s.Substring(0, 2)].Add(s[2]);\n        }\n        HashSet<string>\
        \ memo = new HashSet<string>();\n        return Dfs(bottom, m, memo);\n    }\n\
        \n    private bool Dfs(string s, Dictionary<string, List<char>> m, HashSet<string>\
        \ memo) {\n        if (s.Length == 1) return true;\n        if (memo.Contains(s))\
        \ return false;\n        List<string> next = Get(s, m);\n        if (next.Count\
        \ == 0) {\n            memo.Add(s);\n            return false;\n        }\n\
        \        foreach (string n in next) {\n            if (Dfs(n, m, memo)) return\
        \ true;\n        }\n        memo.Add(s);\n        return false;\n    }\n\n \
        \   private List<string> Get(string s, Dictionary<string, List<char>> m) {\n\
        \        List<string> temp = new List<string> { \"\" };\n        for (int i\
        \ = 0; i < s.Length - 1; i++) {\n            string key = s.Substring(i, 2);\n\
        \            List<string> t = new List<string>();\n            foreach (string\
        \ n in temp) {\n                foreach (char c in m.ContainsKey(key) ? m[key]\
        \ : new List<char>()) {\n                    t.Add(n + c);\n               \
        \ }\n            }\n            temp = t;\n        }\n        return temp;\n\
        \    }\n}"
      javascript: "var pyramidTransition = function(bottom, allowed) {\n    let m =\
        \ {};\n    for (let s of allowed) {\n        if (!m[s.slice(0, 2)]) {\n    \
        \        m[s.slice(0, 2)] = [];\n        }\n        m[s.slice(0, 2)].push(s[2]);\n\
        \    }\n    let memo = new Set();\n    return dfs(bottom, m, memo);\n};\n\n\
        var dfs = function(s, m, memo) {\n    if (s.length === 1) return true;\n   \
        \ if (memo.has(s)) return false;\n    let next = get(s, m);\n    if (next.length\
        \ === 0) {\n        memo.add(s);\n        return false;\n    }\n    for (let\
        \ n of next) {\n        if (dfs(n, m, memo)) return true;\n    }\n    memo.add(s);\n\
        \    return false;\n};\n\nvar get = function(s, m) {\n    let temp = [\"\"];\n\
        \    for (let i = 0; i < s.length - 1; i++) {\n        let key = s.slice(i,\
        \ i + 2);\n        let t = [];\n        for (let n of temp) {\n            for\
        \ (let c of m[key] || []) {\n                t.push(n + c);\n            }\n\
        \        }\n        temp = t;\n    }\n    return temp;\n};"
      typescript: "function pyramidTransition(bottom: string, allowed: string[]): boolean\
        \ {\n    let m: { [key: string]: string[] } = {};\n    for (let s of allowed)\
        \ {\n        if (!m[s.slice(0, 2)]) {\n            m[s.slice(0, 2)] = [];\n\
        \        }\n        m[s.slice(0, 2)].push(s[2]);\n    }\n    let memo: Set<string>\
        \ = new Set();\n    return dfs(bottom, m, memo);\n}\n\nfunction dfs(s: string,\
        \ m: { [key: string]: string[] }, memo: Set<string>): boolean {\n    if (s.length\
        \ === 1) return true;\n    if (memo.has(s)) return false;\n    let next: string[]\
        \ = get(s, m);\n    if (next.length === 0) {\n        memo.add(s);\n       \
        \ return false;\n    }\n    for (let n of next) {\n        if (dfs(n, m, memo))\
        \ return true;\n    }\n    memo.add(s);\n    return false;\n}\n\nfunction get(s:\
        \ string, m: { [key: string]: string[] }): string[] {\n    let temp: string[]\
        \ = [\"\"];\n    for (let i = 0; i < s.length - 1; i++) {\n        let key =\
        \ s.slice(i, i + 2);\n        let t: string[] = [];\n        for (let n of temp)\
        \ {\n            for (let c of m[key] || []) {\n                t.push(n + c);\n\
        \            }\n        }\n        temp = t;\n    }\n    return temp;\n}"
      php: "function pyramidTransition($bottom, $allowed) {\n    $m = array();\n   \
        \ foreach ($allowed as $s) {\n        if (!isset($m[substr($s, 0, 2)])) {\n\
        \            $m[substr($s, 0, 2)] = array();\n        }\n        $m[substr($s,\
        \ 0, 2)][] = $s[2];\n    }\n    $memo = array();\n    return dfs($bottom, $m,\
        \ $memo);\n}\n\nfunction dfs($s, $m, &$memo) {\n    if (strlen($s) == 1) return\
        \ true;\n    if (in_array($s, $memo)) return false;\n    $next = get($s, $m);\n\
        \    if (empty($next)) {\n        $memo[] = $s;\n        return false;\n   \
        \ }\n    foreach ($next as $n) {\n        if (dfs($n, $m, $memo)) return true;\n\
        \    }\n    $memo[] = $s;\n    return false;\n}\n\nfunction get($s, $m) {\n\
        \    $temp = array(\"\");\n    for ($i = 0; $i < strlen($s) - 1; $i++) {\n \
        \       $key = substr($s, $i, 2);\n        $t = array();\n        foreach ($temp\
        \ as $n) {\n            foreach ($m[$key] as $c) {\n                $t[] = $n\
        \ . $c;\n            }\n        }\n        $temp = $t;\n    }\n    return $temp;\n\
        }"
      swift: "class Solution {\n    func pyramidTransition(_ bottom: String, _ allowed:\
        \ [String]) -> Bool {\n        var m: [String: [Character]] = [:]\n        for\
        \ s in allowed {\n            let key = String(s.prefix(2))\n            if\
        \ m[key] == nil {\n                m[key] = []\n            }\n            m[key]!.append(s.last!)\n\
        \        }\n        var memo: Set<String> = []\n        return dfs(bottom, m,\
        \ &memo)\n    }\n\n    func dfs(_ s: String, _ m: [String: [Character]], _ memo:\
        \ inout Set<String>) -> Bool {\n        if s.count == 1 {\n            return\
        \ true\n        }\n        if memo.contains(s) {\n            return false\n\
        \        }\n        let next = get(s, m)\n        if next.isEmpty {\n      \
        \      memo.insert(s)\n            return false\n        }\n        for n in\
        \ next {\n            if dfs(n, m, &memo) {\n                return true\n \
        \           }\n        }\n        memo.insert(s)\n        return false\n   \
        \ }\n\n    func get(_ s: String, _ m: [String: [Character]]) -> [String] {\n\
        \        var temp: [String] = [\"\"]\n        for i in 0..<s.count - 1 {\n \
        \           let key = String(s[s.index(s.startIndex, offsetBy: i)...s.index(s.startIndex,\
        \ offsetBy: i + 2)])\n            var t: [String] = []\n            for n in\
        \ temp {\n                for c in m[key] ?? [] {\n                    t.append(n\
        \ + String(c))\n                }\n            }\n            temp = t\n   \
        \     }\n        return temp\n    }\n}"
      kotlin: "class Solution {\n    fun pyramidTransition(bottom: String, allowed:\
        \ Array<String>): Boolean {\n        val m: MutableMap<String, MutableList<Char>>\
        \ = mutableMapOf()\n        for (s in allowed) {\n            val key = s.substring(0,\
        \ 2)\n            if (!m.containsKey(key)) {\n                m[key] = mutableListOf()\n\
        \            }\n            m[key]!!.add(s[2])\n        }\n        val memo:\
        \ MutableSet<String> = mutableSetOf()\n        return dfs(bottom, m, memo)\n\
        \    }\n\n    private fun dfs(s: String, m: Map<String, List<Char>>, memo: MutableSet<String>):\
        \ Boolean {\n        if (s.length == 1) return true\n        if (memo.contains(s))\
        \ return false\n        val next = get(s, m)\n        if (next.isEmpty()) {\n\
        \            memo.add(s)\n            return false\n        }\n        for (n\
        \ in next) {\n            if (dfs(n, m, memo)) return true\n        }\n    \
        \    memo.add(s)\n        return false\n    }\n\n    private fun get(s: String,\
        \ m: Map<String, List<Char>>): List<String> {\n        val temp: MutableList<String>\
        \ = mutableListOf(\"\")\n        for (i in 0 until s.length - 1) {\n       \
        \     val key = s.substring(i, i + 2)\n            val t: MutableList<String>\
        \ = mutableListOf()\n            for (n in temp) {\n                for (c in\
        \ m[key] ?: listOf()) {\n                    t.add(n + c)\n                }\n\
        \            }\n            temp.clear()\n            temp.addAll(t)\n     \
        \   }\n        return temp\n    }\n}"
      dart: "class Solution {\n    bool pyramidTransition(String bottom, List<String>\
        \ allowed) {\n        Map<String, List<String>> m = {};\n        for (var s\
        \ in allowed) {\n            if (!m.containsKey(s.substring(0, 2))) {\n    \
        \            m[s.substring(0, 2)] = [];\n            }\n            m[s.substring(0,\
        \ 2)]!.add(s[2]);\n        }\n        Set<String> memo = {};\n        return\
        \ dfs(bottom, m, memo);\n    }\n\n    bool dfs(String s, Map<String, List<String>>\
        \ m, Set<String> memo) {\n        if (s.length == 1) return true;\n        if\
        \ (memo.contains(s)) return false;\n        List<String> next = get(s, m);\n\
        \        if (next.isEmpty) {\n            memo.add(s);\n            return false;\n\
        \        }\n        for (var n in next) {\n            if (dfs(n, m, memo))\
        \ return true;\n        }\n        memo.add(s);\n        return false;\n   \
        \ }\n\n    List<String> get(String s, Map<String, List<String>> m) {\n     \
        \   List<String> temp = [\"\"];\n        for (int i = 0; i < s.length - 1; i++)\
        \ {\n            String key = s.substring(i, i + 2);\n            List<String>\
        \ t = [];\n            for (var n in temp) {\n                for (var c in\
        \ m[key] ?? []) {\n                    t.add(n + c);\n                }\n  \
        \          }\n            temp = t;\n        }\n        return temp;\n    }\n\
        }"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\ntype Solution struct{}\n\nfunc\
        \ (s *Solution) pyramidTransition(bottom string, allowed []string) bool {\n\
        \    m := make(map[string][]byte)\n    for _, s := range allowed {\n       \
        \ key := s[:2]\n        if _, ok := m[key]; !ok {\n            m[key] = []byte{}\n\
        \        }\n        m[key] = append(m[key], s[2])\n    }\n    memo := make(map[string]bool)\n\
        \    return s.dfs(bottom, m, memo)\n}\n\nfunc (s *Solution) dfs(bottom string,\
        \ m map[string][]byte, memo map[string]bool) bool {\n    if len(bottom) == 1\
        \ {\n        return true\n    }\n    if _, ok := memo[bottom]; ok {\n      \
        \  return false\n    }\n    next := s.get(bottom, m)\n    if len(next) == 0\
        \ {\n        memo[bottom] = true\n        return false\n    }\n    for _, n\
        \ := range next {\n        if s.dfs(n, m, memo) {\n            return true\n\
        \        }\n    }\n    memo[bottom] = true\n    return false\n}\n\nfunc (s *Solution)\
        \ get(bottom string, m map[string][]byte) []string {\n    temp := []string{\"\
        \"]\n    for i := 0; i < len(bottom)-1; i++ {\n        key := bottom[i : i+2]\n\
        \        t := []string{}\n        for _, n := range temp {\n            for\
        \ _, c := range m[key] {\n                t = append(t, n+string(c))\n     \
        \       }\n        }\n        temp = t\n    }\n    return temp\n}"
      ruby: "def pyramid_transition(bottom, allowed)\n    m = {}\n    allowed.each do\
        \ |s|\n        key = s[0, 2]\n        if !m.key?(key)\n            m[key] =\
        \ []\n        end\n        m[key] << s[2]\n    end\n    memo = {}\n    dfs(bottom,\
        \ m, memo)\nend\n\nprivate\n\ndef dfs(s, m, memo)\n    if s.length == 1\n  \
        \      return true\n    end\n    if memo.key?(s)\n        return false\n   \
        \ end\n    next_level = get(s, m)\n    if next_level.empty?\n        memo[s]\
        \ = true\n        return false\n    end\n    next_level.each do |n|\n      \
        \  if dfs(n, m, memo)\n            return true\n        end\n    end\n    memo[s]\
        \ = true\n    false\nend\n\ndef get(s, m)\n    temp = [\"\"]\n    (0...s.length\
        \ - 1).each do |i|\n        key = s[i, 2]\n        t = []\n        temp.each\
        \ do |n|\n            (m[key] || []).each do |c|\n                t << n + c\n\
        \            end\n        end\n        temp = t\n    end\n    temp\nend"
      scala: "object Solution {\n    def pyramidTransition(bottom: String, allowed:\
        \ Array[String]): Boolean = {\n        val m: Map[String, List[Char]] = allowed.groupBy(_.take(2)).mapValues(_.map(_.last)).toMap\n\
        \        val memo: collection.mutable.Set[String] = collection.mutable.Set()\n\
        \        dfs(bottom, m, memo)\n    }\n\n    def dfs(s: String, m: Map[String,\
        \ List[Char]], memo: collection.mutable.Set[String]): Boolean = {\n        if\
        \ (s.length == 1) true\n        else if (memo.contains(s)) false\n        else\
        \ {\n            val next = get(s, m)\n            if (next.isEmpty) {\n   \
        \             memo += s\n                false\n            } else {\n     \
        \           next.exists(n => dfs(n, m, memo))\n            }\n        }\n  \
        \  }\n\n    def get(s: String, m: Map[String, List[Char]]): List[String] = {\n\
        \        val temp = List(\"\")\n        (0 until s.length - 1).foldLeft(temp)\
        \ { (t, i) =>\n            val key = s.substring(i, i + 2)\n            t.flatMap(n\
        \ => m.get(key).getOrElse(List()).map(n + _))\n        }\n    }\n}"
      rust: "use std::collections::HashMap;\nuse std::collections::HashSet;\n\nstruct\
        \ Solution;\n\nimpl Solution {\n    pub fn pyramid_transition(bottom: String,\
        \ allowed: Vec<String>) -> bool {\n        let mut m: HashMap<&str, Vec<char>>\
        \ = HashMap::new();\n        for s in allowed {\n            let key = &s[..2];\n\
        \            if !m.contains_key(key) {\n                m.insert(key, vec![]);\n\
        \            }\n            m.get_mut(key).unwrap().push(s.chars().nth(2).unwrap());\n\
        \        }\n        let mut memo: HashSet<String> = HashSet::new();\n      \
        \  Solution::dfs(bottom, &m, &mut memo)\n    }\n\n    fn dfs(s: String, m: &HashMap<&str,\
        \ Vec<char>>, memo: &mut HashSet<String>) -> bool {\n        if s.len() == 1\
        \ {\n            return true;\n        }\n        if memo.contains(&s) {\n \
        \           return false;\n        }\n        let next = Solution::get(s, m);\n\
        \        if next.is_empty() {\n            memo.insert(s.clone());\n       \
        \     return false;\n        }\n        for n in next {\n            if Solution::dfs(n,\
        \ m, memo) {\n                return true;\n            }\n        }\n     \
        \   memo.insert(s.clone());\n        false\n    }\n\n    fn get(s: String, m:\
        \ &HashMap<&str, Vec<char>>) -> Vec<String> {\n        let mut temp = vec![String::new()];\n\
        \        for i in 0..s.len() - 1 {\n            let key = &s[i..i + 2];\n  \
        \          let mut t = vec![];\n            for n in &temp {\n             \
        \   for c in m.get(key).unwrap_or(&vec![]) {\n                    t.push(n.clone()\
        \ + &c.to_string());\n                }\n            }\n            temp = t;\n\
        \        }\n        temp\n    }\n}"
      racket: "define (pyramid-transition bottom allowed)\n  (let ((m (make-hash)))\n\
        \    (for-each (lambda (s) (hash-set! m (substring s 0 2) (cons (string-ref\
        \ s 2) (hash-ref m (substring s 0 2) '())))) allowed)\n    (dfs bottom m (make-hash))))\n\
        \n(define (dfs s m memo)\n  (cond ((= (string-length s) 1) #t)\n        ((hash-ref\
        \ memo s #f) #f)\n        (else (let ((next (get s m)))\n                (if\
        \ (null? next)\n                    (begin (hash-set! memo s #t) #f)\n     \
        \               (or-map (lambda (n) (dfs n m memo)) next))))))\n\n(define (get\
        \ s m)\n  (let loop ((i 0) (temp '(\"\")))\n    (if (= i (- (string-length s)\
        \ 1))\n        temp\n        (loop (+ i 1) (for/fold ((t '())) ((n temp))\n\
        \                                    (for/fold ((tt '())) ((c (hash-ref m (substring\
        \ s i (+ i 2)) '())))\n                                      (cons (string-append\
        \ n (string c)) tt))))))))"
      erlang: "pyramid_transition(Bottom, Allowed) ->\n    dfs(Bottom, maps:from_list([{K,\
        \ [V]} || {K, V} <- Allowed]), sets:new())."
      elixir: "def pyramid_transition(bottom, allowed) do\n    m = Enum.reduce(allowed,\
        \ %{}, fn s, m ->\n      key = String.slice(s, 0, 2)\n      Map.update(m, key,\
        \ [String.at(s, 2)], &[String.at(s, 2)])\n    end)\n    dfs(bottom, m, MapSet.new())\n\
        \  end\n\n  defp dfs(s, m, memo) when byte_size(s) == 1, do: true\n  defp dfs(s,\
        \ m, memo) do\n    if MapSet.member?(memo, s), do: false, else: nil\n    next\
        \ = get(s, m)\n    if Enum.empty?(next), do: false, else: Enum.any?(next, &dfs(&1,\
        \ m, memo))\n  end\n\n  defp get(s, m) do\n    temp = [\"\"]\n    Enum.reduce(0..byte_size(s)\
        \ - 2, temp, fn i, t ->\n      key = String.slice(s, i, 2)\n      Enum.flat_map(t,\
        \ fn n ->\n        Enum.map(Map.get(m, key, []), fn c -> n <> <<c>> end)\n \
        \     end)\n    end)\n  end"
    approach: The problem can be solved using a depth-first search (DFS) approach. We
      start with the given bottom row and try to build the pyramid level by level. For
      each level, we generate all possible combinations of blocks that can be placed
      on top of the previous level, based on the allowed triangular patterns. We then
      recursively call the DFS function for each possible combination until we reach
      the top of the pyramid or we find that it is not possible to build the pyramid
      with the given allowed patterns. The key intuition is to use a set to store the
      allowed patterns for efficient lookups and to use a memoization technique to avoid
      redundant computations.
    time_complexity: The time complexity of the solution is O(6^6 * 216) because in
      the worst case, we have to try all possible combinations of blocks for each level
      of the pyramid. The number of possible combinations for each level is 6^6 (since
      there are 6 possible blocks and 6 positions in the row), and we have to check
      each combination against the 216 allowed patterns.
    space_complexity: The space complexity of the solution is O(6^6) because we need
      to store all possible combinations of blocks for each level of the pyramid. In
      the worst case, we have to store all possible combinations for each level, which
      is 6^6.
    elapsed_time: 19.81791639328003
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-29 01:15:40 '
---

## Problem #756: Pyramid Transition Matrix

**Difficulty:** Medium

**Topics:** Hash Table, String, Backtracking, Bit Manipulation

## Problem Description

<p>You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains <strong>one less block</strong> than the row beneath it and is centered on top.</p>

<p>To make the pyramid aesthetically pleasing, there are only specific <strong>triangular patterns</strong> that are allowed. A triangular pattern consists of a <strong>single block</strong> stacked on top of <strong>two blocks</strong>. The patterns are given&nbsp;as a list of&nbsp;three-letter strings <code>allowed</code>, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.</p>

<ul>
	<li>For example, <code>&quot;ABC&quot;</code> represents a triangular pattern with a <code>&#39;C&#39;</code> block stacked on top of an <code>&#39;A&#39;</code> (left) and <code>&#39;B&#39;</code> (right) block. Note that this is different from <code>&quot;BAC&quot;</code> where <code>&#39;B&#39;</code> is on the left bottom and <code>&#39;A&#39;</code> is on the right bottom.</li>
</ul>

<p>You start with a bottom row of blocks <code>bottom</code>, given as a single string, that you <strong>must</strong> use as the base of the pyramid.</p>

<p>Given <code>bottom</code> and <code>allowed</code>, return <code>true</code><em> if you can build the pyramid all the way to the top such that <strong>every triangular pattern</strong> in the pyramid is in </em><code>allowed</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/26/pyramid1-grid.jpg" style="width: 600px; height: 232px;" />
<pre>
<strong>Input:</strong> bottom = &quot;BCD&quot;, allowed = [&quot;BCC&quot;,&quot;CDE&quot;,&quot;CEA&quot;,&quot;FFF&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> The allowed triangular patterns are shown on the right.
Starting from the bottom (level 3), we can build &quot;CE&quot; on level 2 and then build &quot;A&quot; on level 1.
There are three triangular patterns in the pyramid, which are &quot;BCC&quot;, &quot;CDE&quot;, and &quot;CEA&quot;. All are allowed.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/26/pyramid2-grid.jpg" style="width: 600px; height: 359px;" />
<pre>
<strong>Input:</strong> bottom = &quot;AAAA&quot;, allowed = [&quot;AAB&quot;,&quot;AAC&quot;,&quot;BCD&quot;,&quot;BBE&quot;,&quot;DEF&quot;]
<strong>Output:</strong> false
<strong>Explanation:</strong> The allowed triangular patterns are shown on the right.
Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= bottom.length &lt;= 6</code></li>
	<li><code>0 &lt;= allowed.length &lt;= 216</code></li>
	<li><code>allowed[i].length == 3</code></li>
	<li>The letters in all input strings are from the set <code>{&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;F&#39;}</code>.</li>
	<li>All the values of <code>allowed</code> are <strong>unique</strong>.</li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-29 01:15:20 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem is solved using a recursive backtracking approach with memoization. We start from the given `bottom` row and attempt to build the pyramid upwards, one row at a time, until a single block remains at the top. The core idea is to define a recursive function `can_build(current_row)` that returns `true` if a pyramid can be built starting from `current_row`, and `false` otherwise. The base case for `can_build` is when `current_row` has only one block, in which case it returns `true` as the pyramid is complete.

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
    std::unordered_map<std::string, std::vector<char>> allowed_map;
    std::unordered_map<std::string, bool> memo;

    bool pyramidTransition(std::string bottom, std::vector<std::string>& allowed) {
        for (const std::string& pattern : allowed) {
            allowed_map[pattern.substr(0, 2)].push_back(pattern[2]);
        }

        return can_build(bottom);
    }

private:
    bool can_build(const std::string& current_row) {
        if (memo.count(current_row)) {
            return memo[current_row];
        }

        if (current_row.length() == 1) {
            return true;
        }

        std::string next_row_builder = "";
        bool result = find_next_row(0, next_row_builder, current_row);
        memo[current_row] = result;
        return result;
    }

    bool find_next_row(int index, std::string& next_row_builder, const std::string& current_row) {
        if (index == current_row.length() - 1) {
            return can_build(next_row_builder);
        }

        char left = current_row[index];
        char right = current_row[index + 1];
        std::string key = "";
        key += left;
        key += right;

        if (allowed_map.find(key) == allowed_map.end()) {
            return false;
        }

        for (char top_char : allowed_map[key]) {
            next_row_builder.push_back(top_char);
            if (find_next_row(index + 1, next_row_builder, current_row)) {
                next_row_builder.pop_back(); 
                return true;
            }
            next_row_builder.pop_back(); 
        }

        return false;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Solution {
    Map<String, List<Character>> allowedMap;
    Map<String, Boolean> memo;

    public boolean pyramidTransition(String bottom, List<String> allowed) {
        allowedMap = new HashMap<>();
        for (String pattern : allowed) {
            String key = pattern.substring(0, 2);
            char value = pattern.charAt(2);
            allowedMap.computeIfAbsent(key, k -> new ArrayList<>()).add(value);
        }

        memo = new HashMap<>();

        return canBuild(bottom);
    }

    private boolean canBuild(String currentRow) {
        if (memo.containsKey(currentRow)) {
            return memo.get(currentRow);
        }

        if (currentRow.length() == 1) {
            return true;
        }

        StringBuilder nextRowBuilder = new StringBuilder();
        boolean result = findNextRow(0, nextRowBuilder, currentRow);
        memo.put(currentRow, result);
        return result;
    }

    private boolean findNextRow(int index, StringBuilder nextRowBuilder, String currentRow) {
        if (index == currentRow.length() - 1) {
            return canBuild(nextRowBuilder.toString());
        }

        char left = currentRow.charAt(index);
        char right = currentRow.charAt(index + 1);
        String key = "" + left + right;

        if (!allowedMap.containsKey(key)) {
            return false;
        }

        for (char topChar : allowedMap.get(key)) {
            nextRowBuilder.append(topChar);
            if (findNextRow(index + 1, nextRowBuilder, currentRow)) {
                nextRowBuilder.deleteCharAt(nextRowBuilder.length() - 1); 
                return true;
            }
            nextRowBuilder.deleteCharAt(nextRowBuilder.length() - 1); 
        }

        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_map = collections.defaultdict(list)
        for pattern in allowed:
            allowed_map[pattern[0:2]].append(pattern[2])

        memo = {}

        def can_build(current_row: str) -> bool:
            if current_row in memo:
                return memo[current_row]

            if len(current_row) == 1:
                return True

            result = find_next_row(0, [], current_row)
            memo[current_row] = result
            return result

        def find_next_row(index: int, next_row_chars: List[str], current_row: str) -> bool:
            if index == len(current_row) - 1:
                return can_build("".join(next_row_chars))

            left = current_row[index]
            right = current_row[index + 1]
            key = left + right

            if key not in allowed_map:
                return False 

            for top_char in allowed_map[key]:
                next_row_chars.append(top_char)
                if find_next_row(index + 1, next_row_chars, current_row):
                    next_row_chars.pop() 
                    return True
                next_row_chars.pop() 

            return False 

        return can_build(bottom)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_map = collections.defaultdict(list)
        for pattern in allowed:
            allowed_map[pattern[0:2]].append(pattern[2])

        memo = {}

        def can_build(current_row: str) -> bool:
            if current_row in memo:
                return memo[current_row]

            if len(current_row) == 1:
                return True

            result = find_next_row(0, [], current_row)
            memo[current_row] = result
            return result

        def find_next_row(index: int, next_row_chars: List[str], current_row: str) -> bool:
            if index == len(current_row) - 1:
                return can_build("".join(next_row_chars))

            left = current_row[index]
            right = current_row[index + 1]
            key = left + right

            if key not in allowed_map:
                return False 

            for top_char in allowed_map[key]:
                next_row_chars.append(top_char)
                if find_next_row(index + 1, next_row_chars, current_row):
                    next_row_chars.pop() 
                    return True
                next_row_chars.pop() 

            return False 

        return can_build(bottom)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

char allowed_tops[6][6][7]; 
int memo[46656]; 

int encodeRow(const char* row) {
    int hash = 0;
    int len = strlen(row);
    for (int i = 0; i < len; ++i) {
        hash = hash * 6 + (row[i] - 'A');
    }
    return hash;
}

bool canBuild(const char* current_row);
bool findNextRow(int index, char* next_row_builder, int builder_len, const char* current_row);

bool canBuild(const char* current_row) {
    int len = strlen(current_row);
    if (len == 1) {
        return true;
    }

    int row_hash = encodeRow(current_row);
    if (memo[row_hash] != 0) {
        return memo[row_hash] == 1;
    }

    char* next_row_builder = (char*)malloc(sizeof(char) * len); 
    next_row_builder[0] = '\0'; 

    bool result = findNextRow(0, next_row_builder, 0, current_row);

    free(next_row_builder);
    memo[row_hash] = result ? 1 : -1;
    return result;
}

bool findNextRow(int index, char* next_row_builder, int builder_len, const char* current_row) {
    int current_row_len = strlen(current_row);

    if (index == current_row_len - 1) {
        next_row_builder[builder_len] = '\0'; 
        return canBuild(next_row_builder);
    }

    char left = current_row[index];
    char right = current_row[index + 1];

    const char* possible_tops = allowed_tops[left - 'A'][right - 'A'];

    if (possible_tops[0] == '\0') {
        return false;
    }

    for (int i = 0; possible_tops[i] != '\0'; ++i) {
        char top_char = possible_tops[i];
        next_row_builder[builder_len] = top_char; 

        if (findNextRow(index + 1, next_row_builder, builder_len + 1, current_row)) {
            return true;
        }
    }

    return false;
}

bool pyramidTransition(char* bottom, char** allowed, int allowedSize) {
    memset(memo, 0, sizeof(memo));
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 6; ++j) {
            allowed_tops[i][j][0] = '\0';
        }
    }

    for (int k = 0; k < allowedSize; ++k) {
        char* pattern = allowed[k];
        char left = pattern[0];
        char right = pattern[1];
        char top = pattern[2];

        int left_idx = left - 'A';
        int right_idx = right - 'A';

        int current_len = strlen(allowed_tops[left_idx][right_idx]);
        allowed_tops[left_idx][right_idx][current_len] = top;
        allowed_tops[left_idx][right_idx][current_len + 1] = '\0';
    }

    return canBuild(bottom);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    private Dictionary<string, List<char>> allowedMap;
    private Dictionary<string, bool> memo;

    public bool PyramidTransition(string bottom, IList<string> allowed) {
        allowedMap = new Dictionary<string, List<char>>();
        foreach (string pattern in allowed) {
            string key = pattern.Substring(0, 2);
            char value = pattern[2];
            if (!allowedMap.ContainsKey(key)) {
                allowedMap[key] = new List<char>();
            }
            allowedMap[key].Add(value);
        }

        memo = new Dictionary<string, bool>();

        return CanBuild(bottom);
    }

    private bool CanBuild(string currentRow) {
        if (memo.ContainsKey(currentRow)) {
            return memo[currentRow];
        }

        if (currentRow.Length == 1) {
            return true;
        }

        StringBuilder nextRowBuilder = new StringBuilder();
        bool result = FindNextRow(0, nextRowBuilder, currentRow);
        memo[currentRow] = result;
        return result;
    }

    private bool FindNextRow(int index, StringBuilder nextRowBuilder, string currentRow) {
        if (index == currentRow.Length - 1) {
            return CanBuild(nextRowBuilder.ToString());
        }

        char left = currentRow[index];
        char right = currentRow[index + 1];
        string key = "" + left + right;

        if (!allowedMap.ContainsKey(key)) {
            return false;
        }

        foreach (char topChar in allowedMap[key]) {
            nextRowBuilder.Append(topChar);
            if (FindNextRow(index + 1, nextRowBuilder, currentRow)) {
                nextRowBuilder.Remove(nextRowBuilder.Length - 1, 1); 
                return true;
            }
            nextRowBuilder.Remove(nextRowBuilder.Length - 1, 1); 
        }

        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} bottom
 * @param {string[]} allowed
 * @return {boolean}
 */
var pyramidTransition = function(bottom, allowed) {
    const allowedMap = new Map();
    for (const pattern of allowed) {
        const key = pattern.substring(0, 2);
        const value = pattern[2];
        if (!allowedMap.has(key)) {
            allowedMap.set(key, []);
        }
        allowedMap.get(key).push(value);
    }

    const memo = new Map();

    const canBuild = (currentRow) => {
        if (memo.has(currentRow)) {
            return memo.get(currentRow);
        }

        if (currentRow.length === 1) {
            return true;
        }

        const nextRowChars = [];
        const result = findNextRow(0, nextRowChars, currentRow);
        memo.set(currentRow, result);
        return result;
    };

    const findNextRow = (index, nextRowChars, currentRow) => {
        if (index === currentRow.length - 1) {
            return canBuild(nextRowChars.join(''));
        }

        const left = currentRow[index];
        const right = currentRow[index + 1];
        const key = left + right;

        if (!allowedMap.has(key)) {
            return false;
        }

        for (const topChar of allowedMap.get(key)) {
            nextRowChars.push(topChar);
            if (findNextRow(index + 1, nextRowChars, currentRow)) {
                nextRowChars.pop(); 
                return true;
            }
            nextRowChars.pop(); 
        }

        return false;
    };

    return canBuild(bottom);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class Solution {
    private allowedMap: Map<string, string[]>;
    private memo: Map<string, boolean>;

    public pyramidTransition(bottom: string, allowed: string[]): boolean {
        this.allowedMap = new Map<string, string[]>();
        for (const pattern of allowed) {
            const key = pattern.substring(0, 2);
            const value = pattern[2];
            if (!this.allowedMap.has(key)) {
                this.allowedMap.set(key, []);
            }
            this.allowedMap.get(key)!.push(value);
        }

        this.memo = new Map<string, boolean>();

        return this.canBuild(bottom);
    }

    private canBuild(currentRow: string): boolean {
        if (this.memo.has(currentRow)) {
            return this.memo.get(currentRow)!;
        }

        if (currentRow.length === 1) {
            return true;
        }

        const nextRowChars: string[] = [];
        const result = this.findNextRow(0, nextRowChars, currentRow);
        this.memo.set(currentRow, result);
        return result;
    }

    private findNextRow(index: number, nextRowChars: string[], currentRow: string): boolean {
        if (index === currentRow.length - 1) {
            return this.canBuild(nextRowChars.join(''));
        }

        const left = currentRow[index];
        const right = currentRow[index + 1];
        const key = left + right;

        const possibleTops = this.allowedMap.get(key);
        if (!possibleTops) {
            return false;
        }

        for (const topChar of possibleTops) {
            nextRowChars.push(topChar);
            if (this.findNextRow(index + 1, nextRowChars, currentRow)) {
                nextRowChars.pop(); 
                return true;
            }
            nextRowChars.pop(); 
        }

        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php

class Solution {
    private $allowedMap;
    private $memo;

    /**
     * @param String $bottom
     * @param String[] $allowed
     * @return Boolean
     */
    function pyramidTransition($bottom, $allowed) {
        $this->allowedMap = [];
        foreach ($allowed as $pattern) {
            $key = substr($pattern, 0, 2);
            $value = $pattern[2];
            if (!isset($this->allowedMap[$key])) {
                $this->allowedMap[$key] = [];
            }
            $this->allowedMap[$key][] = $value;
        }

        $this->memo = [];

        return $this->canBuild($bottom);
    }

    private function canBuild($currentRow) {
        if (isset($this->memo[$currentRow])) {
            return $this->memo[$currentRow];
        }

        if (strlen($currentRow) == 1) {
            return true;
        }

        $nextRowChars = [];
        $result = $this->findNextRow(0, $nextRowChars, $currentRow);
        $this->memo[$currentRow] = $result;
        return $result;
    }

    private function findNextRow($index, &$nextRowChars, $currentRow) {
        if ($index == strlen($currentRow) - 1) {
            return $this->canBuild(implode('', $nextRowChars));
        }

        $left = $currentRow[$index];
        $right = $currentRow[$index + 1];
        $key = $left . $right;

        if (!isset($this->allowedMap[$key])) {
            return false;
        }

        foreach ($this->allowedMap[$key] as $topChar) {
            $nextRowChars[] = $topChar;
            if ($this->findNextRow($index + 1, $nextRowChars, $currentRow)) {
                array_pop($nextRowChars); 
                return true;
            }
            array_pop($nextRowChars); 
        }

        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    private var allowedMap: [String: [Character]] = [:]
    private var memo: [String: Bool] = [:]

    func pyramidTransition(_ bottom: String, _ allowed: [String]) -> Bool {
        for pattern in allowed {
            let key = String(pattern.prefix(2))
            let value = pattern.last!
            allowedMap[key, default: []].append(value)
        }

        return canBuild(bottom)
    }

    private func canBuild(_ currentRow: String) -> Bool {
        if let result = memo[currentRow] {
            return result
        }

        if currentRow.count == 1 {
            return true
        }

        var nextRowChars: [Character] = []
        let result = findNextRow(0, &nextRowChars, currentRow)
        memo[currentRow] = result
        return result
    }

    private func findNextRow(_ index: Int, _ nextRowChars: inout [Character], _ currentRow: String) -> Bool {
        if index == currentRow.count - 1 {
            return canBuild(String(nextRowChars))
        }

        let currentChars = Array(currentRow)
        let left = currentChars[index]
        let right = currentChars[index + 1]
        let key = String([left, right])

        guard let possibleTops = allowedMap[key] else {
            return false
        }

        for topChar in possibleTops {
            nextRowChars.append(topChar)
            if findNextRow(index + 1, &nextRowChars, currentRow) {
                nextRowChars.removeLast() 
                return true
            }
            nextRowChars.removeLast() 
        }

        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    private lateinit var allowedMap: MutableMap<String, MutableList<Char>>
    private lateinit var memo: MutableMap<String, Boolean>

    fun pyramidTransition(bottom: String, allowed: List<String>): Boolean {
        allowedMap = mutableMapOf()
        for (pattern in allowed) {
            val key = pattern.substring(0, 2)
            val value = pattern[2]
            allowedMap.computeIfAbsent(key) { mutableListOf() }.add(value)
        }

        memo = mutableMapOf()

        return canBuild(bottom)
    }

    private fun canBuild(currentRow: String): Boolean {
        if (memo.containsKey(currentRow)) {
            return memo[currentRow]!!
        }

        if (currentRow.length == 1) {
            return true
        }

        val nextRowBuilder = StringBuilder()
        val result = findNextRow(0, nextRowBuilder, currentRow)
        memo[currentRow] = result
        return result
    }

    private fun findNextRow(index: Int, nextRowBuilder: StringBuilder, currentRow: String): Boolean {
        if (index == currentRow.length - 1) {
            return canBuild(nextRowBuilder.toString())
        }

        val left = currentRow[index]
        val right = currentRow[index + 1]
        val key = "$left$right"

        val possibleTops = allowedMap[key]
        if (possibleTops == null) {
            return false
        }

        for (topChar in possibleTops) {
            nextRowBuilder.append(topChar)
            if (findNextRow(index + 1, nextRowBuilder, currentRow)) {
                nextRowBuilder.deleteCharAt(nextRowBuilder.length - 1); 
                return true
            }
            nextRowBuilder.deleteCharAt(nextRowBuilder.length - 1); 
        }

        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  late Map<String, List<String>> allowedMap;
  late Map<String, bool> memo;

  bool pyramidTransition(String bottom, List<String> allowed) {
    allowedMap = {};
    for (final pattern in allowed) {
      final key = pattern.substring(0, 2);
      final value = pattern[2];
      allowedMap.putIfAbsent(key, () => []).add(value);
    }

    memo = {};

    return _canBuild(bottom);
  }

  bool _canBuild(String currentRow) {
    if (memo.containsKey(currentRow)) {
      return memo[currentRow]!;
    }

    if (currentRow.length == 1) {
      return true;
    }

    final nextRowChars = <String>[];
    final result = _findNextRow(0, nextRowChars, currentRow);
    memo[currentRow] = result;
    return result;
  }

  bool _findNextRow(int index, List<String> nextRowChars, String currentRow) {
    if (index == currentRow.length - 1) {
      return _canBuild(nextRowChars.join(''));
    }

    final left = currentRow[index];
    final right = currentRow[index + 1];
    final key = left + right;

    final possibleTops = allowedMap[key];
    if (possibleTops == null) {
      return false;
    }

    for (final topChar in possibleTops) {
      nextRowChars.add(topChar);
      if (_findNextRow(index + 1, nextRowChars, currentRow)) {
        nextRowChars.removeLast(); 
        return true;
      }
      nextRowChars.removeLast(); 
    }

    return false;
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
	"strings"
)

type PyramidHelper struct {
	allowedMap map[string][]rune
	memo       map[string]bool
}

func (s *PyramidHelper) canBuild(currentRow string) bool {
	if val, ok := s.memo[currentRow]; ok {
		return val
	}

	if len(currentRow) == 1 {
		return true
	}

	nextRowChars := make([]rune, 0, len(currentRow)-1) 
	result := s.findNextRow(0, nextRowChars, currentRow)
	s.memo[currentRow] = result
	return result
}

func (s *PyramidHelper) findNextRow(index int, nextRowChars []rune, currentRow string) bool {
	if index == len(currentRow)-1 {
		return s.canBuild(string(nextRowChars))
	}

	left := rune(currentRow[index])
	right := rune(currentRow[index+1])
	key := string([]rune{left, right})

	possibleTops, ok := s.allowedMap[key]
	if !ok {
		return false
	}

	for _, topChar := range possibleTops {
		if s.findNextRow(index+1, append(nextRowChars, topChar), currentRow) {
			return true
		}
	}

	return false
}

func pyramidTransition(bottom string, allowed []string) bool {
	allowedMap := make(map[string][]rune)
	for _, pattern := range allowed {
		key := pattern[0:2]
		value := rune(pattern[2])
		allowedMap[key] = append(allowedMap[key], value)
	}

	helper := PyramidHelper{
		allowedMap: allowedMap,
		memo:       make(map[string]bool),
	}
	return helper.canBuild(bottom)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def pyramid_transition(bottom, allowed)
        @allowed_map = Hash.new { |hash, key| hash[key] = [] }
        allowed.each do |pattern|
            @allowed_map[pattern[0..1]] << pattern[2]
        end

        @memo = {}

        can_build(bottom)
    end

    private

    def can_build(current_row)
        return @memo[current_row] if @memo.key?(current_row)

        return true if current_row.length == 1

        next_row_chars = []
        result = find_next_row(0, next_row_chars, current_row)
        @memo[current_row] = result
        result
    end

    def find_next_row(index, next_row_chars, current_row)
        if index == current_row.length - 1
            return can_build(next_row_chars.join(''))
        end

        left = current_row[index]
        right = current_row[index + 1]
        key = left + right

        return false unless @allowed_map.key?(key)

        @allowed_map[key].each do |top_char|
            next_row_chars << top_char
            if find_next_row(index + 1, next_row_chars, current_row)
                next_row_chars.pop 
                return true
            end
            next_row_chars.pop 
        end

        false
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def pyramidTransition(bottom: String, allowed: List[String]): Boolean = {
        val allowedMap: mutable.Map[String, List[Char]] = mutable.Map.empty
        for (pattern <- allowed) {
            val key = pattern.substring(0, 2)
            val value = pattern.charAt(2)
            allowedMap.update(key, allowedMap.getOrElse(key, List.empty) :+ value)
        }

        val memo: mutable.Map[String, Boolean] = mutable.Map.empty

        def canBuild(currentRow: String): Boolean = {
            if (memo.contains(currentRow)) {
                return memo(currentRow)
            }

            if (currentRow.length == 1) {
                return true
            }

            val nextRowBuilder = new StringBuilder()
            val result = findNextRow(0, nextRowBuilder, currentRow)
            memo.update(currentRow, result)
            result
        }

        def findNextRow(index: Int, nextRowBuilder: StringBuilder, currentRow: String): Boolean = {
            if (index == currentRow.length - 1) {
                return canBuild(nextRowBuilder.toString())
            }

            val left = currentRow(index)
            val right = currentRow(index + 1)
            val key = s"$left$right"

            allowedMap.get(key) match {
                case Some(possibleTops) =>
                    for (topChar <- possibleTops) {
                        nextRowBuilder.append(topChar)
                        if (findNextRow(index + 1, nextRowBuilder, currentRow)) {
                            nextRowBuilder.deleteCharAt(nextRowBuilder.length - 1) 
                            return true
                        }
                        nextRowBuilder.deleteCharAt(nextRowBuilder.length - 1) 
                    }
                    false
                case None => false
            }
        }

        canBuild(bottom)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn pyramid_transition(bottom: String, allowed: Vec<String>) -> bool {
        let mut allowed_map: HashMap<String, Vec<char>> = HashMap::new();
        for pattern in allowed {
            let key = pattern[0..2].to_string();
            let value = pattern.chars().nth(2).unwrap();
            allowed_map.entry(key).or_insert_with(Vec::new).push(value);
        }

        let mut helper = PyramidHelper {
            allowed_map,
            memo: HashMap::new(),
        };
        helper.can_build(bottom)
    }
}

struct PyramidHelper {
    allowed_map: HashMap<String, Vec<char>>,
    memo: HashMap<String, bool>,
}

impl PyramidHelper {
    fn can_build(&mut self, current_row: String) -> bool {
        if let Some(&result) = self.memo.get(&current_row) {
            return result;
        }

        if current_row.len() == 1 {
            return true;
        }

        let mut next_row_chars: Vec<char> = Vec::new();
        let result = self.find_next_row(0, &mut next_row_chars, &current_row);
        self.memo.insert(current_row, result);
        result
    }

    fn find_next_row(&mut self, index: usize, next_row_chars: &mut Vec<char>, current_row: &str) -> bool {
        if index == current_row.len() - 1 {
            return self.can_build(next_row_chars.iter().collect());
        }

        let current_chars: Vec<char> = current_row.chars().collect(); 
        let left = current_chars[index];
        let right = current_chars[index + 1];
        let key = format!("{}{}", left, right);

        if let Some(possible_tops) = self.allowed_map.get(&key) {
            for &top_char in possible_tops {
                next_row_chars.push(top_char);
                if self.find_next_row(index + 1, next_row_chars, current_row) {
                    next_row_chars.pop(); 
                    return true;
                }
                next_row_chars.pop(); 
            }
        }

        false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (pyramid-transition bottom allowed)
  (define allowed-map (make-hash))
  (for ([pattern allowed])
    (define key (substring pattern 0 2))
    (define value (string-ref pattern 2))
    (hash-update! allowed-map key (lambda (lst) (cons value lst)) (list)))

  (define memo (make-hash))

  (define (can-build current-row)
    (cond
      [(hash-has-key? memo current-row)
       (hash-ref memo current-row)]
      [(equal? (string-length current-row) 1)
       (hash-set! memo current-row #t)
       #t]
      [else
       (define result (find-next-row 0 '() current-row))
       (hash-set! memo current-row result)
       result]))

  (define (find-next-row index next-row-chars current-row)
    (define current-row-len (string-length current-row))
    (cond
      [(= index (- current-row-len 1))
       (can-build (list->string (reverse next-row-chars)))]
      [else
       (define left (string-ref current-row index))
       (define right (string-ref current-row (+ index 1)))
       (define key (string left right))

       (cond
         [(hash-has-key? allowed-map key)
          (define possible-tops (hash-ref allowed-map key))
          (ormap (lambda (top-char)
                   (find-next-row (+ index 1) (cons top-char next-row-chars) current-row))
                 possible-tops)]
         [else #f])]))

  (can-build bottom))

(provide pyramid-transition)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([pyramidTransition/2]).

pyramidTransition(Bottom, Allowed) ->
    AllowedMap = lists:foldl(
        fun(Pattern, Acc) ->
            Key = string:substr(Pattern, 1, 2),
            Value = string:substr(Pattern, 3, 1),
            maps:update_with(Key, fun(OldValues) -> OldValues ++ Value end, Value, Acc)
        end,
        maps:new(),
        Allowed
    ),

    put(memo, maps:new()),

    Result = can_build(Bottom, AllowedMap),
    erase(memo),
    Result.

can_build(CurrentRow, AllowedMap) ->
    Memo = get(memo),
    case maps:find(CurrentRow, Memo) of
        {ok, Result} -> Result;
        _ ->
            case length(CurrentRow) of
                1 -> 
                    put(memo, maps:put(CurrentRow, true, Memo)),
                    true;
                _ ->
                    Result = find_next_row(0, [], CurrentRow, AllowedMap),
                    put(memo, maps:put(CurrentRow, Result, Memo)),
                    Result
            end
    end.

find_next_row(Index, NextRowChars, CurrentRow, AllowedMap) ->
    CurrentRowLen = length(CurrentRow),
    if Index == CurrentRowLen - 1 ->
        can_build(lists:reverse(NextRowChars), AllowedMap);
    true ->
        Left = lists:nth(Index + 1, CurrentRow),
        Right = lists:nth(Index + 2, CurrentRow),
        Key = [Left, Right],

        case maps:find(Key, AllowedMap) of
            {ok, PossibleTops} ->
                find_next_row_loop(PossibleTops, Index, NextRowChars, CurrentRow, AllowedMap);
            _ ->
                false
        end
    end.

find_next_row_loop([], _Index, _NextRowChars, _CurrentRow, _AllowedMap) ->
    false;
find_next_row_loop([TopChar | Rest], Index, NextRowChars, CurrentRow, AllowedMap) ->
    case find_next_row(Index + 1, [TopChar | NextRowChars], CurrentRow, AllowedMap) of
        true -> true;
        false -> find_next_row_loop(Rest, Index, NextRowChars, CurrentRow, AllowedMap)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec pyramid_transition(bottom :: String.t, allowed :: [String.t]) :: boolean
  def pyramid_transition(bottom, allowed) do
    allowed_map = Enum.reduce(allowed, %{}, fn pattern, acc ->
      key = String.slice(pattern, 0, 2)
      value = String.at(pattern, 2)
      Map.update(acc, key, [value], fn old_values -> old_values ++ [value] end)
    end)

    Process.put(:memo, %{})

    result = can_build(bottom, allowed_map)
    Process.delete(:memo)
    result
  end

  defp can_build(current_row, allowed_map) do
    memo = Process.get(:memo)
    if Map.has_key?(memo, current_row) do
      Map.get(memo, current_row)
    else
      result = 
        if String.length(current_row) == 1 do
          true
        else
          find_next_row(0, [], current_row, allowed_map)
        end
      Process.put(:memo, Map.put(memo, current_row, result))
      result
    end
  end

  defp find_next_row(index, next_row_chars, current_row, allowed_map) do
    current_row_len = String.length(current_row)
    if index == current_row_len - 1 do
      can_build(Enum.reverse(next_row_chars) |> List.to_string(), allowed_map)
    else
      left = String.at(current_row, index)
      right = String.at(current_row, index + 1)
      key = left <> right

      case Map.get(allowed_map, key) do
        nil -> false
        possible_tops ->
          Enum.any?(possible_tops, fn top_char ->
            find_next_row(index + 1, [top_char | next_row_chars], current_row, allowed_map)
          end)
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** Let `N` be the length of the `bottom` string (maximum 6) and `M` be the size of the alphabet (maximum 6, for 'A' through 'F'). The recursion depth is `N`. The number of unique row strings that can be encountered is `sum_{k=1 to N} M^k`. For `N=6, M=6`, this is approximately `5.6 * 10^4`. For each unique `current_row` of length `L`, we call a helper function `find_next_row` which explores possibilities for the next row. `find_next_row` is a backtracking function that iterates through `L-1` positions. For each position, it tries up to `M` possible top characters. The cost of `find_next_row` for a given `current_row` is `O(L * M)` in the worst case (when it has to explore all branches for a single block before finding a successful path or failing). Therefore, the total time complexity is `O(N * M^(N+1))`. With `N=6` and `M=6`, this is `6 * 6^7 = 6^8 = 1,679,616` operations, which is well within typical time limits.

- **Space Complexity:** The space complexity is dominated by the memoization table and the recursion stack. The `allowed_map` stores `O(allowed.length)` entries. The `memo` table stores results for up to `sum_{k=1 to N} M^k` unique row strings. Each string has a maximum length of `N`. Thus, the space for memoization is `O(N * M^N)`. The recursion stack depth is `N`, and each frame stores a row string of length up to `N` (or a character list/builder). So, the stack space is `O(N^2)`. The dominant term is `O(N * M^N)`. With `N=6` and `M=6`, this is `6 * 6^6 = 279,936` characters/entries, which is acceptable.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-29 01:15:40 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using a depth-first search (DFS) approach. We start with the given bottom row and try to build the pyramid level by level. For each level, we generate all possible combinations of blocks that can be placed on top of the previous level, based on the allowed triangular patterns. We then recursively call the DFS function for each possible combination until we reach the top of the pyramid or we find that it is not possible to build the pyramid with the given allowed patterns. The key intuition is to use a set to store the allowed patterns for efficient lookups and to use a memoization technique to avoid redundant computations.

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
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        unordered_map<string, vector<char>> m;
        for (auto& s : allowed) {
            m[s.substr(0, 2)].push_back(s[2]);
        }
        unordered_set<string> memo;
        function<bool(string)> dfs = [&](string s) {
            if (s.size() == 1) return true;
            if (memo.count(s)) return false;
            vector<string> next;
            get(s, next, m);
            if (next.empty()) {
                memo.insert(s);
                return false;
            }
            for (auto& n : next) {
                if (dfs(n)) return true;
            }
            memo.insert(s);
            return false;
        };
        return dfs(bottom);
    }

    void get(string s, vector<string>& next, unordered_map<string, vector<char>>& m) {
        vector<string> temp = {""};
        for (int i = 0; i < s.size() - 1; i++) {
            string key = s.substr(i, 2);
            vector<string> t;
            for (auto& n : temp) {
                for (auto& c : m[key]) {
                    t.push_back(n + c);
                }
            }
            temp = t;
        }
        next = temp;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean pyramidTransition(String bottom, String[] allowed) {
        Map<String, List<Character>> m = new HashMap<>();
        for (String s : allowed) {
            m.computeIfAbsent(s.substring(0, 2), k -> new ArrayList<>()).add(s.charAt(2));
        }
        Set<String> memo = new HashSet<>();
        return dfs(bottom, m, memo);
    }

    private boolean dfs(String s, Map<String, List<Character>> m, Set<String> memo) {
        if (s.length() == 1) return true;
        if (memo.contains(s)) return false;
        List<String> next = get(s, m);
        if (next.isEmpty()) {
            memo.add(s);
            return false;
        }
        for (String n : next) {
            if (dfs(n, m, memo)) return true;
        }
        memo.add(s);
        return false;
    }

    private List<String> get(String s, Map<String, List<Character>> m) {
        List<String> temp = new ArrayList<>();
        temp.add("");
        for (int i = 0; i < s.length() - 1; i++) {
            String key = s.substring(i, i + 2);
            List<String> t = new ArrayList<>();
            for (String n : temp) {
                for (char c : m.getOrDefault(key, new ArrayList<>())) {
                    t.add(n + c);
                }
            }
            temp = t;
        }
        return temp;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        m = {}
        for s in allowed:
            if s[:2] not in m:
                m[s[:2]] = []
            m[s[:2]].append(s[2])
        memo = set()
        def dfs(s):
            if len(s) == 1:
                return True
            if s in memo:
                return False
            next_level = get(s, m)
            if not next_level:
                memo.add(s)
                return False
            for n in next_level:
                if dfs(n):
                    return True
            memo.add(s)
            return False
        def get(s, m):
            temp = [""]
            for i in range(len(s) - 1):
                key = s[i:i+2]
                t = []
                for n in temp:
                    for c in m.get(key, []):
                        t.append(n + c)
                temp = t
            return temp
        return dfs(bottom)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        m = {}
        for s in allowed:
            if s[:2] not in m:
                m[s[:2]] = []
            m[s[:2]].append(s[2])
        memo = set()
        def dfs(s):
            if len(s) == 1:
                return True
            if s in memo:
                return False
            next_level = get(s, m)
            if not next_level:
                memo.add(s)
                return False
            for n in next_level:
                if dfs(n):
                    return True
            memo.add(s)
            return False
        def get(s, m):
            temp = [""]
            for i in range(len(s) - 1):
                key = s[i:i+2]
                t = []
                for n in temp:
                    for c in m.get(key, []):
                        t.append(n + c)
                temp = t
            return temp
        return dfs(bottom)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    char key[3];
    char value;
} Pair;

bool pyramidTransition(char * bottom, char ** allowed, int allowedSize) {
    Pair *m = (Pair *)malloc(sizeof(Pair) * allowedSize);
    for (int i = 0; i < allowedSize; i++) {
        strcpy(m[i].key, allowed[i]);
        m[i].value = allowed[i][2];
    }
    bool *memo = (bool *)malloc(sizeof(bool) * (1 << 20));
    return dfs(bottom, m, allowedSize, memo);
}

bool dfs(char *s, Pair *m, int size, bool *memo) {
    if (strlen(s) == 1) return true;
    if (memo[(unsigned long long)s]) return false;
    char **next = get(s, m, size);
    if (!next) {
        memo[(unsigned long long)s] = true;
        return false;
    }
    for (int i = 0; next[i]; i++) {
        if (dfs(next[i], m, size, memo)) return true;
    }
    memo[(unsigned long long)s] = true;
    return false;
}

char **get(char *s, Pair *m, int size) {
    char **temp = (char **)malloc(sizeof(char *) * (1 << 10));
    temp[0] = (char *)malloc(sizeof(char) * 2);
    temp[0][0] = '\0';
    int count = 1;
    for (int i = 0; i < strlen(s) - 1; i++) {
        char key[3];
        key[0] = s[i];
        key[1] = s[i + 1];
        key[2] = '\0';
        for (int j = 0; j < size; j++) {
            if (strcmp(m[j].key, key) == 0) {
                for (int k = 0; k < count; k++) {
                    temp[count] = (char *)malloc(sizeof(char) * (strlen(temp[k]) + 2));
                    strcpy(temp[count], temp[k]);
                    temp[count][strlen(temp[k])] = m[j].value;
                    temp[count][strlen(temp[k]) + 1] = '\0';
                    count++;
                }
            }
        }
    }
    temp[count] = NULL;
    return temp;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool PyramidTransition(string bottom, string[] allowed) {
        Dictionary<string, List<char>> m = new Dictionary<string, List<char>>();
        foreach (string s in allowed) {
            if (!m.ContainsKey(s.Substring(0, 2))) {
                m[s.Substring(0, 2)] = new List<char>();
            }
            m[s.Substring(0, 2)].Add(s[2]);
        }
        HashSet<string> memo = new HashSet<string>();
        return Dfs(bottom, m, memo);
    }

    private bool Dfs(string s, Dictionary<string, List<char>> m, HashSet<string> memo) {
        if (s.Length == 1) return true;
        if (memo.Contains(s)) return false;
        List<string> next = Get(s, m);
        if (next.Count == 0) {
            memo.Add(s);
            return false;
        }
        foreach (string n in next) {
            if (Dfs(n, m, memo)) return true;
        }
        memo.Add(s);
        return false;
    }

    private List<string> Get(string s, Dictionary<string, List<char>> m) {
        List<string> temp = new List<string> { "" };
        for (int i = 0; i < s.Length - 1; i++) {
            string key = s.Substring(i, 2);
            List<string> t = new List<string>();
            foreach (string n in temp) {
                foreach (char c in m.ContainsKey(key) ? m[key] : new List<char>()) {
                    t.Add(n + c);
                }
            }
            temp = t;
        }
        return temp;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var pyramidTransition = function(bottom, allowed) {
    let m = {};
    for (let s of allowed) {
        if (!m[s.slice(0, 2)]) {
            m[s.slice(0, 2)] = [];
        }
        m[s.slice(0, 2)].push(s[2]);
    }
    let memo = new Set();
    return dfs(bottom, m, memo);
};

var dfs = function(s, m, memo) {
    if (s.length === 1) return true;
    if (memo.has(s)) return false;
    let next = get(s, m);
    if (next.length === 0) {
        memo.add(s);
        return false;
    }
    for (let n of next) {
        if (dfs(n, m, memo)) return true;
    }
    memo.add(s);
    return false;
};

var get = function(s, m) {
    let temp = [""];
    for (let i = 0; i < s.length - 1; i++) {
        let key = s.slice(i, i + 2);
        let t = [];
        for (let n of temp) {
            for (let c of m[key] || []) {
                t.push(n + c);
            }
        }
        temp = t;
    }
    return temp;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function pyramidTransition(bottom: string, allowed: string[]): boolean {
    let m: { [key: string]: string[] } = {};
    for (let s of allowed) {
        if (!m[s.slice(0, 2)]) {
            m[s.slice(0, 2)] = [];
        }
        m[s.slice(0, 2)].push(s[2]);
    }
    let memo: Set<string> = new Set();
    return dfs(bottom, m, memo);
}

function dfs(s: string, m: { [key: string]: string[] }, memo: Set<string>): boolean {
    if (s.length === 1) return true;
    if (memo.has(s)) return false;
    let next: string[] = get(s, m);
    if (next.length === 0) {
        memo.add(s);
        return false;
    }
    for (let n of next) {
        if (dfs(n, m, memo)) return true;
    }
    memo.add(s);
    return false;
}

function get(s: string, m: { [key: string]: string[] }): string[] {
    let temp: string[] = [""];
    for (let i = 0; i < s.length - 1; i++) {
        let key = s.slice(i, i + 2);
        let t: string[] = [];
        for (let n of temp) {
            for (let c of m[key] || []) {
                t.push(n + c);
            }
        }
        temp = t;
    }
    return temp;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
function pyramidTransition($bottom, $allowed) {
    $m = array();
    foreach ($allowed as $s) {
        if (!isset($m[substr($s, 0, 2)])) {
            $m[substr($s, 0, 2)] = array();
        }
        $m[substr($s, 0, 2)][] = $s[2];
    }
    $memo = array();
    return dfs($bottom, $m, $memo);
}

function dfs($s, $m, &$memo) {
    if (strlen($s) == 1) return true;
    if (in_array($s, $memo)) return false;
    $next = get($s, $m);
    if (empty($next)) {
        $memo[] = $s;
        return false;
    }
    foreach ($next as $n) {
        if (dfs($n, $m, $memo)) return true;
    }
    $memo[] = $s;
    return false;
}

function get($s, $m) {
    $temp = array("");
    for ($i = 0; $i < strlen($s) - 1; $i++) {
        $key = substr($s, $i, 2);
        $t = array();
        foreach ($temp as $n) {
            foreach ($m[$key] as $c) {
                $t[] = $n . $c;
            }
        }
        $temp = $t;
    }
    return $temp;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func pyramidTransition(_ bottom: String, _ allowed: [String]) -> Bool {
        var m: [String: [Character]] = [:]
        for s in allowed {
            let key = String(s.prefix(2))
            if m[key] == nil {
                m[key] = []
            }
            m[key]!.append(s.last!)
        }
        var memo: Set<String> = []
        return dfs(bottom, m, &memo)
    }

    func dfs(_ s: String, _ m: [String: [Character]], _ memo: inout Set<String>) -> Bool {
        if s.count == 1 {
            return true
        }
        if memo.contains(s) {
            return false
        }
        let next = get(s, m)
        if next.isEmpty {
            memo.insert(s)
            return false
        }
        for n in next {
            if dfs(n, m, &memo) {
                return true
            }
        }
        memo.insert(s)
        return false
    }

    func get(_ s: String, _ m: [String: [Character]]) -> [String] {
        var temp: [String] = [""]
        for i in 0..<s.count - 1 {
            let key = String(s[s.index(s.startIndex, offsetBy: i)...s.index(s.startIndex, offsetBy: i + 2)])
            var t: [String] = []
            for n in temp {
                for c in m[key] ?? [] {
                    t.append(n + String(c))
                }
            }
            temp = t
        }
        return temp
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun pyramidTransition(bottom: String, allowed: Array<String>): Boolean {
        val m: MutableMap<String, MutableList<Char>> = mutableMapOf()
        for (s in allowed) {
            val key = s.substring(0, 2)
            if (!m.containsKey(key)) {
                m[key] = mutableListOf()
            }
            m[key]!!.add(s[2])
        }
        val memo: MutableSet<String> = mutableSetOf()
        return dfs(bottom, m, memo)
    }

    private fun dfs(s: String, m: Map<String, List<Char>>, memo: MutableSet<String>): Boolean {
        if (s.length == 1) return true
        if (memo.contains(s)) return false
        val next = get(s, m)
        if (next.isEmpty()) {
            memo.add(s)
            return false
        }
        for (n in next) {
            if (dfs(n, m, memo)) return true
        }
        memo.add(s)
        return false
    }

    private fun get(s: String, m: Map<String, List<Char>>): List<String> {
        val temp: MutableList<String> = mutableListOf("")
        for (i in 0 until s.length - 1) {
            val key = s.substring(i, i + 2)
            val t: MutableList<String> = mutableListOf()
            for (n in temp) {
                for (c in m[key] ?: listOf()) {
                    t.add(n + c)
                }
            }
            temp.clear()
            temp.addAll(t)
        }
        return temp
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    bool pyramidTransition(String bottom, List<String> allowed) {
        Map<String, List<String>> m = {};
        for (var s in allowed) {
            if (!m.containsKey(s.substring(0, 2))) {
                m[s.substring(0, 2)] = [];
            }
            m[s.substring(0, 2)]!.add(s[2]);
        }
        Set<String> memo = {};
        return dfs(bottom, m, memo);
    }

    bool dfs(String s, Map<String, List<String>> m, Set<String> memo) {
        if (s.length == 1) return true;
        if (memo.contains(s)) return false;
        List<String> next = get(s, m);
        if (next.isEmpty) {
            memo.add(s);
            return false;
        }
        for (var n in next) {
            if (dfs(n, m, memo)) return true;
        }
        memo.add(s);
        return false;
    }

    List<String> get(String s, Map<String, List<String>> m) {
        List<String> temp = [""];
        for (int i = 0; i < s.length - 1; i++) {
            String key = s.substring(i, i + 2);
            List<String> t = [];
            for (var n in temp) {
                for (var c in m[key] ?? []) {
                    t.add(n + c);
                }
            }
            temp = t;
        }
        return temp;
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

func (s *Solution) pyramidTransition(bottom string, allowed []string) bool {
    m := make(map[string][]byte)
    for _, s := range allowed {
        key := s[:2]
        if _, ok := m[key]; !ok {
            m[key] = []byte{}
        }
        m[key] = append(m[key], s[2])
    }
    memo := make(map[string]bool)
    return s.dfs(bottom, m, memo)
}

func (s *Solution) dfs(bottom string, m map[string][]byte, memo map[string]bool) bool {
    if len(bottom) == 1 {
        return true
    }
    if _, ok := memo[bottom]; ok {
        return false
    }
    next := s.get(bottom, m)
    if len(next) == 0 {
        memo[bottom] = true
        return false
    }
    for _, n := range next {
        if s.dfs(n, m, memo) {
            return true
        }
    }
    memo[bottom] = true
    return false
}

func (s *Solution) get(bottom string, m map[string][]byte) []string {
    temp := []string{""]
    for i := 0; i < len(bottom)-1; i++ {
        key := bottom[i : i+2]
        t := []string{}
        for _, n := range temp {
            for _, c := range m[key] {
                t = append(t, n+string(c))
            }
        }
        temp = t
    }
    return temp
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def pyramid_transition(bottom, allowed)
    m = {}
    allowed.each do |s|
        key = s[0, 2]
        if !m.key?(key)
            m[key] = []
        end
        m[key] << s[2]
    end
    memo = {}
    dfs(bottom, m, memo)
end

private

def dfs(s, m, memo)
    if s.length == 1
        return true
    end
    if memo.key?(s)
        return false
    end
    next_level = get(s, m)
    if next_level.empty?
        memo[s] = true
        return false
    end
    next_level.each do |n|
        if dfs(n, m, memo)
            return true
        end
    end
    memo[s] = true
    false
end

def get(s, m)
    temp = [""]
    (0...s.length - 1).each do |i|
        key = s[i, 2]
        t = []
        temp.each do |n|
            (m[key] || []).each do |c|
                t << n + c
            end
        end
        temp = t
    end
    temp
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def pyramidTransition(bottom: String, allowed: Array[String]): Boolean = {
        val m: Map[String, List[Char]] = allowed.groupBy(_.take(2)).mapValues(_.map(_.last)).toMap
        val memo: collection.mutable.Set[String] = collection.mutable.Set()
        dfs(bottom, m, memo)
    }

    def dfs(s: String, m: Map[String, List[Char]], memo: collection.mutable.Set[String]): Boolean = {
        if (s.length == 1) true
        else if (memo.contains(s)) false
        else {
            val next = get(s, m)
            if (next.isEmpty) {
                memo += s
                false
            } else {
                next.exists(n => dfs(n, m, memo))
            }
        }
    }

    def get(s: String, m: Map[String, List[Char]]): List[String] = {
        val temp = List("")
        (0 until s.length - 1).foldLeft(temp) { (t, i) =>
            val key = s.substring(i, i + 2)
            t.flatMap(n => m.get(key).getOrElse(List()).map(n + _))
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;
use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn pyramid_transition(bottom: String, allowed: Vec<String>) -> bool {
        let mut m: HashMap<&str, Vec<char>> = HashMap::new();
        for s in allowed {
            let key = &s[..2];
            if !m.contains_key(key) {
                m.insert(key, vec![]);
            }
            m.get_mut(key).unwrap().push(s.chars().nth(2).unwrap());
        }
        let mut memo: HashSet<String> = HashSet::new();
        Solution::dfs(bottom, &m, &mut memo)
    }

    fn dfs(s: String, m: &HashMap<&str, Vec<char>>, memo: &mut HashSet<String>) -> bool {
        if s.len() == 1 {
            return true;
        }
        if memo.contains(&s) {
            return false;
        }
        let next = Solution::get(s, m);
        if next.is_empty() {
            memo.insert(s.clone());
            return false;
        }
        for n in next {
            if Solution::dfs(n, m, memo) {
                return true;
            }
        }
        memo.insert(s.clone());
        false
    }

    fn get(s: String, m: &HashMap<&str, Vec<char>>) -> Vec<String> {
        let mut temp = vec![String::new()];
        for i in 0..s.len() - 1 {
            let key = &s[i..i + 2];
            let mut t = vec![];
            for n in &temp {
                for c in m.get(key).unwrap_or(&vec![]) {
                    t.push(n.clone() + &c.to_string());
                }
            }
            temp = t;
        }
        temp
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (pyramid-transition bottom allowed)
  (let ((m (make-hash)))
    (for-each (lambda (s) (hash-set! m (substring s 0 2) (cons (string-ref s 2) (hash-ref m (substring s 0 2) '())))) allowed)
    (dfs bottom m (make-hash))))

(define (dfs s m memo)
  (cond ((= (string-length s) 1) #t)
        ((hash-ref memo s #f) #f)
        (else (let ((next (get s m)))
                (if (null? next)
                    (begin (hash-set! memo s #t) #f)
                    (or-map (lambda (n) (dfs n m memo)) next))))))

(define (get s m)
  (let loop ((i 0) (temp '("")))
    (if (= i (- (string-length s) 1))
        temp
        (loop (+ i 1) (for/fold ((t '())) ((n temp))
                                    (for/fold ((tt '())) ((c (hash-ref m (substring s i (+ i 2)) '())))
                                      (cons (string-append n (string c)) tt))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
pyramid_transition(Bottom, Allowed) ->
    dfs(Bottom, maps:from_list([{K, [V]} || {K, V} <- Allowed]), sets:new()).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def pyramid_transition(bottom, allowed) do
    m = Enum.reduce(allowed, %{}, fn s, m ->
      key = String.slice(s, 0, 2)
      Map.update(m, key, [String.at(s, 2)], &[String.at(s, 2)])
    end)
    dfs(bottom, m, MapSet.new())
  end

  defp dfs(s, m, memo) when byte_size(s) == 1, do: true
  defp dfs(s, m, memo) do
    if MapSet.member?(memo, s), do: false, else: nil
    next = get(s, m)
    if Enum.empty?(next), do: false, else: Enum.any?(next, &dfs(&1, m, memo))
  end

  defp get(s, m) do
    temp = [""]
    Enum.reduce(0..byte_size(s) - 2, temp, fn i, t ->
      key = String.slice(s, i, 2)
      Enum.flat_map(t, fn n ->
        Enum.map(Map.get(m, key, []), fn c -> n <> <<c>> end)
      end)
    end)
  end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(6^6 * 216) because in the worst case, we have to try all possible combinations of blocks for each level of the pyramid. The number of possible combinations for each level is 6^6 (since there are 6 possible blocks and 6 positions in the row), and we have to check each combination against the 216 allowed patterns.

- **Space Complexity:** The space complexity of the solution is O(6^6) because we need to store all possible combinations of blocks for each level of the pyramid. In the worst case, we have to store all possible combinations for each level, which is 6^6.

</div>
</details>
