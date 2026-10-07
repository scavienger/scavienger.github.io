---
layout: post
title: "Remove Invalid Parentheses"
date: 2026-10-07 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["String", "Backtracking", "Breadth-First Search"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/remove-invalid-parentheses/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <string>\n#include <unordered_set>\n\nusing\
        \ namespace std;\n\nclass Solution {\npublic:\n    vector<string> removeInvalidParentheses(string\
        \ s) {\n        int l = 0, r = 0;\n        for (char c : s) {\n            if\
        \ (c == '(') {\n                l++;\n            } else if (c == ')') {\n \
        \               if (l > 0) l--;\n                else r++;\n            }\n\
        \        }\n\n        unordered_set<string> res;\n        string current = \"\
        \";\n        dfs(0, l, r, 0, s, current, res);\n        return vector<string>(res.begin(),\
        \ res.end());\n    }\n\nprivate:\n    void dfs(int idx, int l, int r, int bal,\
        \ const string& s, string& current, unordered_set<string>& res) {\n        if\
        \ (idx == s.length()) {\n            if (l == 0 && r == 0 && bal == 0) {\n \
        \               res.insert(current);\n            }\n            return;\n \
        \       }\n\n        char c = s[idx];\n        if (c == '(') {\n           \
        \ if (l > 0) dfs(idx + 1, l - 1, r, bal, s, current, res);\n            current.push_back('(');\n\
        \            dfs(idx + 1, l, r, bal + 1, s, current, res);\n            current.pop_back();\n\
        \        } else if (c == ')') {\n            if (r > 0) dfs(idx + 1, l, r -\
        \ 1, bal, s, current, res);\n            if (bal > 0) {\n                current.push_back(')');\n\
        \                dfs(idx + 1, l, r, bal - 1, s, current, res);\n           \
        \     current.pop_back();\n            }\n        } else {\n            current.push_back(c);\n\
        \            dfs(idx + 1, l, r, bal, s, current, res);\n            current.pop_back();\n\
        \        }\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public List<String> removeInvalidParentheses(String\
        \ s) {\n        int l = 0, r = 0;\n        for (int i = 0; i < s.length(); i++)\
        \ {\n            char c = s.charAt(i);\n            if (c == '(') {\n      \
        \          l++;\n            } else if (c == ')') {\n                if (l >\
        \ 0) l--;\n                else r++;\n            }\n        }\n\n        Set<String>\
        \ res = new HashSet<>();\n        dfs(s, 0, l, r, 0, new StringBuilder(), res);\n\
        \        return new ArrayList<>(res);\n    }\n\n    private void dfs(String\
        \ s, int idx, int l, int r, int bal, StringBuilder sb, Set<String> res) {\n\
        \        if (idx == s.length()) {\n            if (l == 0 && r == 0 && bal ==\
        \ 0) {\n                res.add(sb.toString());\n            }\n           \
        \ return;\n        }\n\n        char c = s.charAt(idx);\n        int len = sb.length();\n\
        \n        if (c == '(') {\n            if (l > 0) dfs(s, idx + 1, l - 1, r,\
        \ bal, sb, res);\n            sb.append('(');\n            dfs(s, idx + 1, l,\
        \ r, bal + 1, sb, res);\n            sb.setLength(len);\n        } else if (c\
        \ == ')') {\n            if (r > 0) dfs(s, idx + 1, l, r - 1, bal, sb, res);\n\
        \            if (bal > 0) {\n                sb.append(')');\n             \
        \   dfs(s, idx + 1, l, r, bal - 1, sb, res);\n                sb.setLength(len);\n\
        \            }\n        } else {\n            sb.append(c);\n            dfs(s,\
        \ idx + 1, l, r, bal, sb, res);\n            sb.setLength(len);\n        }\n\
        \    }\n}"
      python: "class Solution(object):\n    def removeInvalidParentheses(self, s):\n\
        \        \"\"\"\n        :type s: str\n        :rtype: List[str]\n        \"\
        \"\"\n        l_rem, r_rem = 0, 0\n        for char in s:\n            if char\
        \ == '(':\n                l_rem += 1\n            elif char == ')':\n     \
        \           if l_rem > 0:\n                    l_rem -= 1\n                else:\n\
        \                    r_rem += 1\n\n        res = set()\n        n = len(s)\n\
        \n        def dfs(idx, l, r, bal, path):\n            if idx == n:\n       \
        \         if l == 0 and r == 0 and bal == 0:\n                    res.add(path)\n\
        \                return\n\n            char = s[idx]\n            if char ==\
        \ '(':\n                if l > 0:\n                    dfs(idx + 1, l - 1, r,\
        \ bal, path)\n                dfs(idx + 1, l, r, bal + 1, path + '(')\n    \
        \        elif char == ')':\n                if r > 0:\n                    dfs(idx\
        \ + 1, l, r - 1, bal, path)\n                if bal > 0:\n                 \
        \   dfs(idx + 1, l, r, bal - 1, path + ')')\n            else:\n           \
        \     dfs(idx + 1, l, r, bal, path + char)\n\n        dfs(0, l_rem, r_rem, 0,\
        \ \"\")\n        return list(res)"
      python3: "class Solution:\n    def removeInvalidParentheses(self, s: str) -> list[str]:\n\
        \        def is_valid(string: str) -> bool:\n            balance = 0\n     \
        \       for char in string:\n                if char == '(':\n             \
        \       balance += 1\n                elif char == ')':\n                  \
        \  balance -= 1\n                if balance < 0:\n                    return\
        \ False\n            return balance == 0\n\n        current_level = {s}\n  \
        \      while current_level:\n            valid_strings = [string for string\
        \ in current_level if is_valid(string)]\n            if valid_strings:\n   \
        \             return valid_strings\n\n            next_level = set()\n     \
        \       for string in current_level:\n                for i in range(len(string)):\n\
        \                    if string[i] in '()':\n                        next_level.add(string[:i]\
        \ + string[i+1:])\n            current_level = next_level\n\n        return\
        \ [\"\"]"
      c: "#include <stdlib.h>\n#include <string.h>\n\nstatic void helper(char* s, int\
        \ last_i, int last_j, char p1, char p2, char*** res, int* resSize) {\n    int\
        \ count = 0;\n    int len = strlen(s);\n    for (int i = last_i; i < len; i++)\
        \ {\n        if (s[i] == p1) count++;\n        else if (s[i] == p2) count--;\n\
        \        if (count >= 0) continue;\n        for (int j = last_j; j <= i; j++)\
        \ {\n            if (s[j] == p2 && (j == last_j || s[j - 1] != p2)) {\n    \
        \            char* next = (char*)malloc(len * sizeof(char));\n             \
        \   int ptr = 0;\n                for (int k = 0; k < len; k++) {\n        \
        \            if (k != j) next[ptr++] = s[k];\n                }\n          \
        \      next[ptr] = '\\0';\n                helper(next, i, j, p1, p2, res, resSize);\n\
        \                free(next);\n            }\n        }\n        return;\n  \
        \  }\n    char* rev = (char*)malloc((len + 1) * sizeof(char));\n    for (int\
        \ i = 0; i < len; i++) {\n        rev[i] = s[len - 1 - i];\n    }\n    rev[len]\
        \ = '\\0';\n    if (p1 == '(') {\n        helper(rev, 0, 0, ')', '(', res, resSize);\n\
        \        free(rev);\n    } else {\n        *res = (char**)realloc(*res, (*resSize\
        \ + 1) * sizeof(char*));\n        (*res)[*resSize] = rev;\n        (*resSize)++;\n\
        \    }\n}\n\n/**\n * Note: The returned array must be malloced, assume caller\
        \ calls free().\n */\nchar** removeInvalidParentheses(char* s, int* returnSize)\
        \ {\n    *returnSize = 0;\n    char** res = NULL;\n    helper(s, 0, 0, '(',\
        \ ')', &res, returnSize);\n    return res;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public IList<string> RemoveInvalidParentheses(string s) {\n       \
        \ List<string> result = new List<string>();\n        HashSet<string> visited\
        \ = new HashSet<string>();\n        Queue<string> queue = new Queue<string>();\n\
        \n        queue.Enqueue(s);\n        visited.Add(s);\n        bool found = false;\n\
        \n        while (queue.Count > 0) {\n            int size = queue.Count;\n \
        \           for (int i = 0; i < size; i++) {\n                string curr =\
        \ queue.Dequeue();\n                if (IsValid(curr)) {\n                 \
        \   result.Add(curr);\n                    found = true;\n                }\n\
        \                if (!found) {\n                    for (int j = 0; j < curr.Length;\
        \ j++) {\n                        if (curr[j] != '(' && curr[j] != ')') continue;\n\
        \                        string next = curr.Remove(j, 1);\n                \
        \        if (visited.Add(next)) {\n                            queue.Enqueue(next);\n\
        \                        }\n                    }\n                }\n     \
        \       }\n            if (found) break;\n        }\n\n        if (result.Count\
        \ == 0) result.Add(\"\");\n        return result;\n    }\n\n    private bool\
        \ IsValid(string s) {\n        int count = 0;\n        foreach (char c in s)\
        \ {\n            if (c == '(') count++;\n            else if (c == ')') {\n\
        \                count--;\n                if (count < 0) return false;\n  \
        \          }\n        }\n        return count == 0;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {string[]}\n */\nvar removeInvalidParentheses\
        \ = function(s) {\n    const isValid = (str) => {\n        let count = 0;\n\
        \        for (let i = 0; i < str.length; i++) {\n            if (str[i] ===\
        \ '(') count++;\n            else if (str[i] === ')') {\n                if\
        \ (count === 0) return false;\n                count--;\n            }\n   \
        \     }\n        return count === 0;\n    };\n\n    let level = new Set([s]);\n\
        \    while (level.size > 0) {\n        let valid = Array.from(level).filter(isValid);\n\
        \        if (valid.length > 0) return valid;\n\n        let nextLevel = new\
        \ Set();\n        for (let str of level) {\n            for (let i = 0; i <\
        \ str.length; i++) {\n                if (str[i] === '(' || str[i] === ')')\
        \ {\n                    nextLevel.add(str.slice(0, i) + str.slice(i + 1));\n\
        \                }\n            }\n        }\n        level = nextLevel;\n \
        \   }\n    return [\"\"];\n};"
      typescript: "function removeInvalidParentheses(s: string): string[] {\n    let\
        \ remL = 0, remR = 0;\n    for (const char of s) {\n        if (char === '(')\
        \ remL++;\n        else if (char === ')') {\n            if (remL > 0) remL--;\n\
        \            else remR++;\n        }\n    }\n\n    const result: string[] =\
        \ [];\n\n    function isValid(str: string): boolean {\n        let count = 0;\n\
        \        for (const char of str) {\n            if (char === '(') count++;\n\
        \            else if (char === ')') {\n                count--;\n          \
        \      if (count < 0) return false;\n            }\n        }\n        return\
        \ count === 0;\n    }\n\n    function dfs(start: number, l: number, r: number,\
        \ current: string) {\n        if (l === 0 && r === 0) {\n            if (isValid(current))\
        \ result.push(current);\n            return;\n        }\n\n        for (let\
        \ i = start; i < current.length; i++) {\n            if (i > start && current[i]\
        \ === current[i - 1]) continue;\n\n            if (current[i] === '(' && l >\
        \ 0) {\n                dfs(i, l - 1, r, current.substring(0, i) + current.substring(i\
        \ + 1));\n            } else if (current[i] === ')' && r > 0) {\n          \
        \      dfs(i, l, r - 1, current.substring(0, i) + current.substring(i + 1));\n\
        \            }\n        }\n    }\n\n    dfs(0, remL, remR, s);\n    return result;\n\
        }"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return String[]\n\
        \     */\n    function removeInvalidParentheses($s) {\n        $remL = 0; $remR\
        \ = 0;\n        $len = strlen($s);\n        for ($i = 0; $i < $len; $i++) {\n\
        \            if ($s[$i] == '(') $remL++;\n            elseif ($s[$i] == ')')\
        \ {\n                if ($remL > 0) $remL--;\n                else $remR++;\n\
        \            }\n        }\n        $result = [];\n        $this->dfs(0, $remL,\
        \ $remR, $s, $result);\n        return $result;\n    }\n\n    private function\
        \ isValid($str) {\n        $count = 0;\n        $len = strlen($str);\n     \
        \   for ($i = 0; $i < $len; $i++) {\n            if ($str[$i] == '(') $count++;\n\
        \            elseif ($str[$i] == ')') {\n                $count--;\n       \
        \         if ($count < 0) return false;\n            }\n        }\n        return\
        \ $count == 0;\n    }\n\n    private function dfs($start, $l, $r, $current,\
        \ &$result) {\n        if ($l == 0 && $r == 0) {\n            if ($this->isValid($current))\
        \ $result[] = $current;\n            return;\n        }\n        $len = strlen($current);\n\
        \        for ($i = $start; $i < $len; $i++) {\n            if ($i > $start &&\
        \ $current[$i] == $current[$i - 1]) continue;\n            if ($current[$i]\
        \ == '(' && $l > 0) {\n                $this->dfs($i, $l - 1, $r, substr($current,\
        \ 0, $i) . substr($current, $i + 1), $result);\n            } elseif ($current[$i]\
        \ == ')' && $r > 0) {\n                $this->dfs($i, $l, $r - 1, substr($current,\
        \ 0, $i) . substr($current, $i + 1), $result);\n            }\n        }\n \
        \   }\n}"
      swift: "class Solution {\n    func removeInvalidParentheses(_ s: String) -> [String]\
        \ {\n        var remL = 0, remR = 0\n        let chars = Array(s)\n        for\
        \ char in chars {\n            if char == \"(\" { remL += 1 }\n            else\
        \ if char == \")\" {\n                if remL > 0 { remL -= 1 }\n          \
        \      else { remR += 1 }\n            }\n        }\n\n        var result =\
        \ [String]()\n\n        func isValid(_ arr: [Character]) -> Bool {\n       \
        \     var count = 0\n            for char in arr {\n                if char\
        \ == \"(\" { count += 1 }\n                else if char == \")\" {\n       \
        \             count -= 1\n                    if count < 0 { return false }\n\
        \                }\n            }\n            return count == 0\n        }\n\
        \n        func dfs(_ start: Int, _ l: Int, _ r: Int, _ current: [Character])\
        \ {\n            if l == 0 && r == 0 {\n                if isValid(current)\
        \ {\n                    result.append(String(current))\n                }\n\
        \                return\n            }\n\n            for i in start..<current.count\
        \ {\n                if i > start && current[i] == current[i-1] { continue }\n\
        \n                if current[i] == \"(\" && l > 0 {\n                    var\
        \ next = current\n                    next.remove(at: i)\n                 \
        \   dfs(i, l - 1, r, next)\n                } else if current[i] == \")\" &&\
        \ r > 0 {\n                    var next = current\n                    next.remove(at:\
        \ i)\n                    dfs(i, l, r - 1, next)\n                }\n      \
        \      }\n        }\n\n        dfs(0, remL, remR, chars)\n        return result\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun removeInvalidParentheses(s: String): List<String>\
        \ {\n        var remL = 0\n        var remR = 0\n        for (char in s) {\n\
        \            if (char == '(') remL++\n            else if (char == ')') {\n\
        \                if (remL > 0) remL--\n                else remR++\n       \
        \     }\n        }\n\n        val result = mutableListOf<String>()\n       \
        \ dfs(0, remL, remR, s, result)\n        return result\n    }\n\n    private\
        \ fun isValid(s: String): Boolean {\n        var count = 0\n        for (char\
        \ in s) {\n            if (char == '(') count++\n            else if (char ==\
        \ ')') {\n                count--\n                if (count < 0) return false\n\
        \            }\n        }\n        return count == 0\n    }\n\n    private fun\
        \ dfs(start: Int, l: Int, r: Int, current: String, result: MutableList<String>)\
        \ {\n        if (l == 0 && r == 0) {\n            if (isValid(current)) result.add(current)\n\
        \            return\n        }\n\n        for (i in start until current.length)\
        \ {\n            if (i > start && current[i] == current[i - 1]) continue\n\n\
        \            if (current[i] == '(' && l > 0) {\n                dfs(i, l - 1,\
        \ r, current.substring(0, i) + current.substring(i + 1), result)\n         \
        \   } else if (current[i] == ')' && r > 0) {\n                dfs(i, l, r -\
        \ 1, current.substring(0, i) + current.substring(i + 1), result)\n         \
        \   }\n        }\n    }\n}"
      dart: "class Solution {\n  List<String> removeInvalidParentheses(String s) {\n\
        \    int l = 0, r = 0;\n    for (int i = 0; i < s.length; i++) {\n      if (s[i]\
        \ == '(') {\n        l++;\n      } else if (s[i] == ')') {\n        if (l >\
        \ 0) {\n          l--;\n        } else {\n          r++;\n        }\n      }\n\
        \    }\n\n    List<String> res = [];\n\n    bool isValid(String str) {\n   \
        \   int count = 0;\n      for (int i = 0; i < str.length; i++) {\n        if\
        \ (str[i] == '(') {\n          count++;\n        } else if (str[i] == ')') {\n\
        \          count--;\n          if (count < 0) return false;\n        }\n   \
        \   }\n      return count == 0;\n    }\n\n    void dfs(String curr, int start,\
        \ int lRem, int rRem) {\n      if (lRem == 0 && rRem == 0) {\n        if (isValid(curr))\
        \ res.add(curr);\n        return;\n      }\n\n      for (int i = start; i <\
        \ curr.length; i++) {\n        if (i > start && curr[i] == curr[i - 1]) continue;\n\
        \        if (curr[i] == '(' && lRem > 0) {\n          dfs(curr.substring(0,\
        \ i) + curr.substring(i + 1), i, lRem - 1, rRem);\n        } else if (curr[i]\
        \ == ')' && rRem > 0) {\n          dfs(curr.substring(0, i) + curr.substring(i\
        \ + 1), i, lRem, rRem - 1);\n        }\n      }\n    }\n\n    dfs(s, 0, l, r);\n\
        \    return res;\n  }\n}"
      go: "func removeInvalidParentheses(s string) []string {\n\tl, r := 0, 0\n\tfor\
        \ _, char := range s {\n\t\tif char == '(' {\n\t\t\tl++\n\t\t} else if char\
        \ == ')' {\n\t\t\tif l > 0 {\n\t\t\t\tl--\n\t\t\t} else {\n\t\t\t\tr++\n\t\t\
        \t}\n\t\t}\n\t}\n\n\tvar res []string\n\tvar dfs func(string, int, int, int)\n\
        \n\tisValid := func(str string) bool {\n\t\tcount := 0\n\t\tfor _, char := range\
        \ str {\n\t\t\tif char == '(' {\n\t\t\t\tcount++\n\t\t\t} else if char == ')'\
        \ {\n\t\t\t\tcount--\n\t\t\t\tif count < 0 {\n\t\t\t\t\treturn false\n\t\t\t\
        \t}\n\t\t\t}\n\t\t}\n\t\treturn count == 0\n\t}\n\n\tdfs = func(curr string,\
        \ start, lRem, rRem int) {\n\t\tif lRem == 0 && rRem == 0 {\n\t\t\tif isValid(curr)\
        \ {\n\t\t\t\tres = append(res, curr)\n\t\t\t}\n\t\t\treturn\n\t\t}\n\n\t\tfor\
        \ i := start; i < len(curr); i++ {\n\t\t\tif i > start && curr[i] == curr[i-1]\
        \ {\n\t\t\t\tcontinue\n\t\t\t}\n\t\t\tif curr[i] == '(' && lRem > 0 {\n\t\t\t\
        \tdfs(curr[:i]+curr[i+1:], i, lRem-1, rRem)\n\t\t\t} else if curr[i] == ')'\
        \ && rRem > 0 {\n\t\t\t\tdfs(curr[:i]+curr[i+1:], i, lRem, rRem-1)\n\t\t\t}\n\
        \t\t}\n\t}\n\n\tdfs(s, 0, l, r)\n\treturn res\n}"
      ruby: "# @param {String} s\n# @return {String[]}\ndef remove_invalid_parentheses(s)\n\
        \  l = 0\n  r = 0\n  s.each_char do |c|\n    if c == '('\n      l += 1\n   \
        \ elsif c == ')'\n      if l > 0\n        l -= 1\n      else\n        r += 1\n\
        \      end\n    end\n  end\n\n  @res = []\n\n  def is_valid?(str)\n    count\
        \ = 0\n    str.each_char do |c|\n      if c == '('\n        count += 1\n   \
        \   elsif c == ')'\n        count -= 1\n        return false if count < 0\n\
        \      end\n    end\n    count == 0\n  end\n\n  def solve(str, start, l_rem,\
        \ r_rem)\n    if l_rem == 0 && r_rem == 0\n      @res << str if is_valid?(str)\n\
        \      return\n    end\n    (start...str.length).each do |i|\n      next if\
        \ i > start && str[i] == str[i - 1]\n      if str[i] == '(' && l_rem > 0\n \
        \       solve(str[0...i] + str[i + 1...str.length], i, l_rem - 1, r_rem)\n \
        \     elsif str[i] == ')' && r_rem > 0\n        solve(str[0...i] + str[i + 1...str.length],\
        \ i, l_rem, r_rem - 1)\n      end\n    end\n  end\n\n  solve(s, 0, l, r)\n \
        \ @res\nend"
      scala: "object Solution {\n    def removeInvalidParentheses(s: String): List[String]\
        \ = {\n        var l = 0\n        var r = 0\n        for (c <- s) {\n      \
        \      if (c == '(') l += 1\n            else if (c == ')') {\n            \
        \    if (l > 0) l -= 1\n                else r += 1\n            }\n       \
        \ }\n\n        val res = scala.collection.mutable.ListBuffer[String]()\n   \
        \     dfs(s, 0, l, r, res)\n        res.toList\n    }\n\n    private def isValid(s:\
        \ String): Boolean = {\n        var count = 0\n        for (c <- s) {\n    \
        \        if (c == '(') count += 1\n            else if (c == ')') {\n      \
        \          count -= 1\n                if (count < 0) return false\n       \
        \     }\n        }\n        count == 0\n    }\n\n    private def dfs(s: String,\
        \ start: Int, l: Int, r: Int, res: scala.collection.mutable.ListBuffer[String]):\
        \ Unit = {\n        if (l == 0 && r == 0) {\n            if (isValid(s)) res\
        \ += s\n            return\n        }\n\n        for (i <- start until s.length)\
        \ {\n            if (i == start || s(i) != s(i - 1)) {\n                if (s(i)\
        \ == '(' && l > 0) {\n                    dfs(s.substring(0, i) + s.substring(i\
        \ + 1), i, l - 1, r, res)\n                } else if (s(i) == ')' && r > 0)\
        \ {\n                    dfs(s.substring(0, i) + s.substring(i + 1), i, l, r\
        \ - 1, res)\n                }\n            }\n        }\n    }\n}"
      rust: "use std::collections::HashSet;\n\nimpl Solution {\n    pub fn remove_invalid_parentheses(s:\
        \ String) -> Vec<String> {\n        let mut current_level = HashSet::new();\n\
        \        current_level.insert(s);\n\n        loop {\n            let mut valid_ones\
        \ = Vec::new();\n            for s_str in &current_level {\n               \
        \ if Self::is_valid(s_str) {\n                    valid_ones.push(s_str.clone());\n\
        \                }\n            }\n\n            if !valid_ones.is_empty() {\n\
        \                return valid_ones;\n            }\n\n            let mut next_level\
        \ = HashSet::new();\n            for s_str in &current_level {\n           \
        \     for (i, c) in s_str.char_indices() {\n                    if c == '('\
        \ || c == ')' {\n                        let mut next_s = String::with_capacity(s_str.len()\
        \ - 1);\n                        next_s.push_str(&s_str[..i]);\n           \
        \             next_s.push_str(&s_str[i + c.len_utf8()..]);\n               \
        \         next_level.insert(next_s);\n                    }\n              \
        \  }\n            }\n\n            if next_level.is_empty() {\n            \
        \    return vec![\"\".to_string()];\n            }\n            current_level\
        \ = next_level;\n        }\n    }\n\n    fn is_valid(s: &str) -> bool {\n  \
        \      let mut count = 0;\n        for c in s.chars() {\n            if c ==\
        \ '(' {\n                count += 1;\n            } else if c == ')' {\n   \
        \             if count == 0 {\n                    return false;\n         \
        \       }\n                count -= 1;\n            }\n        }\n        count\
        \ == 0\n    }\n}"
      racket: "(require racket/set)\n\n(define (is-valid? s)\n  (let loop ([chars (string->list\
        \ s)] [count 0])\n    (cond\n      [(< count 0) #f]\n      [(empty? chars) (=\
        \ count 0)]\n      [(char=? (car chars) #\\() (loop (cdr chars) (+ count 1))]\n\
        \      [(char=? (car chars) #\\)) (loop (cdr chars) (- count 1))]\n      [else\
        \ (loop (cdr chars) count)])))\n\n(define (generate-next current-set)\n  (let\
        \ ([next-set (mutable-set)])\n    (for ([s (in-set current-set)])\n      (let\
        \ ([chars (string->list s)])\n        (let loop ([prefix '()] [suffix chars])\n\
        \          (when (not (empty? suffix))\n            (let ([h (car suffix)]\n\
        \                  [t (cdr suffix)])\n              (when (or (char=? h #\\\
        () (char=? h #\\)))\n                (set-add! next-set (list->string (append\
        \ (reverse prefix) t))))\n              (loop (cons h prefix) t))))))\n    next-set))\n\
        \n(define (bfs current-set)\n  (let ([valid-ones (filter is-valid? (set->list\
        \ current-set))])\n    (if (not (empty? valid-ones))\n        valid-ones\n \
        \       (let ([next-set (generate-next current-set)])\n          (if (set-empty?\
        \ next-set)\n              '(\"\")\n              (bfs next-set))))))\n\n(define/contract\
        \ (remove-invalid-parentheses s)\n  (-> string? (listof string?))\n  (bfs (set\
        \ s)))"
      erlang: "-spec remove_invalid_parentheses(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].\n\
        remove_invalid_parentheses(S) ->\n    bfs(sets:add_element(S, sets:new())).\n\
        \nbfs(Queue) ->\n    List = sets:to_list(Queue),\n    Valid = [X || X <- List,\
        \ is_valid(X)],\n    case Valid of\n        [] ->\n            NextQueue = generate_next(List),\n\
        \            case sets:size(NextQueue) of\n                0 -> [<<\"\">>];\n\
        \                _ -> bfs(NextQueue)\n            end;\n        _ ->\n     \
        \       Valid\n    end.\n\nis_valid(S) ->\n    is_valid_list(binary_to_list(S),\
        \ 0).\n\nis_valid_list([], 0) -> true;\nis_valid_list([], _) -> false;\nis_valid_list([$(\
        \ | T], Acc) -> is_valid_list(T, Acc + 1);\nis_valid_list([$) | T], Acc) ->\n\
        \    if Acc > 0 -> is_valid_list(T, Acc - 1);\n       true -> false\n    end;\n\
        is_valid_list([_ | T], Acc) -> is_valid_list(T, Acc).\n\ngenerate_next(List)\
        \ ->\n    lists:foldl(fun(S, AccSet) ->\n        SList = binary_to_list(S),\n\
        \        generate_removals(SList, [], AccSet)\n    end, sets:new(), List).\n\
        \ngenerate_removals([], _Prefix, AccSet) -> AccSet;\ngenerate_removals([H |\
        \ T], Prefix, AccSet) when H =:= $(; H =:= $) ->\n    NewBinary = list_to_binary(lists:reverse(Prefix)\
        \ ++ T),\n    NewAccSet = sets:add_element(NewBinary, AccSet),\n    generate_removals(T,\
        \ [H | Prefix], NewAccSet);\ngenerate_removals([H | T], Prefix, AccSet) ->\n\
        \    generate_removals(T, [H | Prefix], AccSet)."
      elixir: "defmodule Solution do\n  @spec remove_invalid_parentheses(s :: String.t)\
        \ :: [String.t]\n  def remove_invalid_parentheses(s) do\n    bfs(MapSet.new([s]))\n\
        \  end\n\n  defp bfs(set) do\n    valid = Enum.filter(set, &is_valid?/1)\n \
        \   if !Enum.empty?(valid) do\n      valid\n    else\n      next_set = Enum.reduce(set,\
        \ MapSet.new(), fn str, acc ->\n        generate_next_strings(str, acc)\n  \
        \    end)\n      if MapSet.size(next_set) == 0 do\n        [\"\"]\n      else\n\
        \        bfs(next_set)\n      end\n    end\n  end\n\n  defp generate_next_strings(str,\
        \ acc) do\n    charlist = String.to_charlist(str)\n    generate_removals(charlist,\
        \ [], acc)\n  end\n\n  defp generate_removals([], _prefix, acc), do: acc\n \
        \ defp generate_removals([h | t], prefix, acc) when h == ?( or h == ?) do\n\
        \    new_str = List.to_string(Enum.reverse(prefix) ++ t)\n    generate_removals(t,\
        \ [h | prefix], MapSet.put(acc, new_str))\n  end\n  defp generate_removals([h\
        \ | t], prefix, acc) do\n    generate_removals(t, [h | prefix], acc)\n  end\n\
        \n  defp is_valid?(s) do\n    s\n    |> String.to_charlist()\n    |> Enum.reduce_while(0,\
        \ fn\n      ?(, acc -> {:cont, acc + 1}\n      ?), acc -> if acc > 0, do: {:cont,\
        \ acc - 1}, else: {:halt, -1}\n      _, acc -> {:cont, acc}\n    end) == 0\n\
        \  end\nend"
    approach: 'To find all unique valid parentheses strings with the minimum number
      of removals, we first determine the total number of left and right parentheses
      that must be discarded. This is done by a single pass through the string while
      maintaining a balance: every closing parenthesis that doesn''t have a matching
      opening parenthesis must be removed, and any leftover opening parentheses after
      the pass also require removal. This identifies the exact target removal counts
      $l$ and $r$ for the ''('' and '')'' characters, respectively, which ensures we
      only generate strings with the minimum number of deletions.


      We then employ a depth-first search (DFS) with backtracking to explore all potential
      valid strings formed by removing exactly $l$ open and $r$ close parentheses. During
      the search, we track the current index, the current balance of open parentheses,
      and the remaining removals allowed. We only branch into keeping a closing parenthesis
      if the current balance is positive and only branch into removing a parenthesis
      if the corresponding removal count is still positive. Letters are always kept.
      To handle duplicate results efficiently, we store all valid terminal configurations
      in a set before returning them as a list.'
    time_complexity: O(2^N) where N is the length of the string. In the worst case,
      every character is a parenthesis and the algorithm explores two choices (keep
      or remove) for each. While the target removal counts and balance constraints prune
      the search space significantly, the theoretical upper bound remains exponential.
      Given the constraint of at most 20 parentheses, $2^{20}$ operations are well within
      the time limits.
    space_complexity: O(2^N \cdot N) in the worst case. The recursion stack uses $O(N)$
      space, but the result set can store many unique valid strings, each up to $N$
      characters long. The temporary string construction during recursion also contributes
      to the space complexity.
    elapsed_time: 802.6946721076965
    model: gemini-3-flash-preview
    generated_at: '2026-10-07 03:49:05 '
---

## Problem #301: Remove Invalid Parentheses

**Difficulty:** Hard

**Topics:** String, Backtracking, Breadth-First Search

## Problem Description

<p>Given a string <code>s</code> that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.</p>

<p>Return <em>a list of <strong>unique strings</strong> that are valid with the minimum number of removals</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()())()&quot;
<strong>Output:</strong> [&quot;(())()&quot;,&quot;()()()&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(a)())()&quot;
<strong>Output:</strong> [&quot;(a())()&quot;,&quot;(a)()()&quot;]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;)(&quot;
<strong>Output:</strong> [&quot;&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 25</code></li>
	<li><code>s</code> consists of lowercase English letters and parentheses <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>.</li>
	<li>There will be at most <code>20</code> parentheses in <code>s</code>.</li>
</ul>


## Hints

1. Since we do not know which brackets can be removed, we try all the options! We can use recursion.

2. In the recursion, for each bracket, we can either use it or remove it.

3. Recursion will generate all the valid parentheses strings but we want the ones with the least number of parentheses deleted.

4. We can count the number of invalid brackets to be deleted and only generate the valid strings in the recusrion.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find all unique valid parentheses strings with the minimum number of removals, we first determine the total number of left and right parentheses that must be discarded. This is done by a single pass through the string while maintaining a balance: every closing parenthesis that doesn't have a matching opening parenthesis must be removed, and any leftover opening parentheses after the pass also require removal. This identifies the exact target removal counts $l$ and $r$ for the '(' and ')' characters, respectively, which ensures we only generate strings with the minimum number of deletions.

We then employ a depth-first search (DFS) with backtracking to explore all potential valid strings formed by removing exactly $l$ open and $r$ close parentheses. During the search, we track the current index, the current balance of open parentheses, and the remaining removals allowed. We only branch into keeping a closing parenthesis if the current balance is positive and only branch into removing a parenthesis if the corresponding removal count is still positive. Letters are always kept. To handle duplicate results efficiently, we store all valid terminal configurations in a set before returning them as a list.

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
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        int l = 0, r = 0;
        for (char c : s) {
            if (c == '(') {
                l++;
            } else if (c == ')') {
                if (l > 0) l--;
                else r++;
            }
        }

        unordered_set<string> res;
        string current = "";
        dfs(0, l, r, 0, s, current, res);
        return vector<string>(res.begin(), res.end());
    }

private:
    void dfs(int idx, int l, int r, int bal, const string& s, string& current, unordered_set<string>& res) {
        if (idx == s.length()) {
            if (l == 0 && r == 0 && bal == 0) {
                res.insert(current);
            }
            return;
        }

        char c = s[idx];
        if (c == '(') {
            if (l > 0) dfs(idx + 1, l - 1, r, bal, s, current, res);
            current.push_back('(');
            dfs(idx + 1, l, r, bal + 1, s, current, res);
            current.pop_back();
        } else if (c == ')') {
            if (r > 0) dfs(idx + 1, l, r - 1, bal, s, current, res);
            if (bal > 0) {
                current.push_back(')');
                dfs(idx + 1, l, r, bal - 1, s, current, res);
                current.pop_back();
            }
        } else {
            current.push_back(c);
            dfs(idx + 1, l, r, bal, s, current, res);
            current.pop_back();
        }
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
    public List<String> removeInvalidParentheses(String s) {
        int l = 0, r = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                l++;
            } else if (c == ')') {
                if (l > 0) l--;
                else r++;
            }
        }

        Set<String> res = new HashSet<>();
        dfs(s, 0, l, r, 0, new StringBuilder(), res);
        return new ArrayList<>(res);
    }

    private void dfs(String s, int idx, int l, int r, int bal, StringBuilder sb, Set<String> res) {
        if (idx == s.length()) {
            if (l == 0 && r == 0 && bal == 0) {
                res.add(sb.toString());
            }
            return;
        }

        char c = s.charAt(idx);
        int len = sb.length();

        if (c == '(') {
            if (l > 0) dfs(s, idx + 1, l - 1, r, bal, sb, res);
            sb.append('(');
            dfs(s, idx + 1, l, r, bal + 1, sb, res);
            sb.setLength(len);
        } else if (c == ')') {
            if (r > 0) dfs(s, idx + 1, l, r - 1, bal, sb, res);
            if (bal > 0) {
                sb.append(')');
                dfs(s, idx + 1, l, r, bal - 1, sb, res);
                sb.setLength(len);
            }
        } else {
            sb.append(c);
            dfs(s, idx + 1, l, r, bal, sb, res);
            sb.setLength(len);
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l_rem, r_rem = 0, 0
        for char in s:
            if char == '(':
                l_rem += 1
            elif char == ')':
                if l_rem > 0:
                    l_rem -= 1
                else:
                    r_rem += 1

        res = set()
        n = len(s)

        def dfs(idx, l, r, bal, path):
            if idx == n:
                if l == 0 and r == 0 and bal == 0:
                    res.add(path)
                return

            char = s[idx]
            if char == '(':
                if l > 0:
                    dfs(idx + 1, l - 1, r, bal, path)
                dfs(idx + 1, l, r, bal + 1, path + '(')
            elif char == ')':
                if r > 0:
                    dfs(idx + 1, l, r - 1, bal, path)
                if bal > 0:
                    dfs(idx + 1, l, r, bal - 1, path + ')')
            else:
                dfs(idx + 1, l, r, bal, path + char)

        dfs(0, l_rem, r_rem, 0, "")
        return list(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        current_level = {s}
        while current_level:
            valid_strings = [string for string in current_level if is_valid(string)]
            if valid_strings:
                return valid_strings

            next_level = set()
            for string in current_level:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i+1:])
            current_level = next_level

        return [""]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

static void helper(char* s, int last_i, int last_j, char p1, char p2, char*** res, int* resSize) {
    int count = 0;
    int len = strlen(s);
    for (int i = last_i; i < len; i++) {
        if (s[i] == p1) count++;
        else if (s[i] == p2) count--;
        if (count >= 0) continue;
        for (int j = last_j; j <= i; j++) {
            if (s[j] == p2 && (j == last_j || s[j - 1] != p2)) {
                char* next = (char*)malloc(len * sizeof(char));
                int ptr = 0;
                for (int k = 0; k < len; k++) {
                    if (k != j) next[ptr++] = s[k];
                }
                next[ptr] = '\0';
                helper(next, i, j, p1, p2, res, resSize);
                free(next);
            }
        }
        return;
    }
    char* rev = (char*)malloc((len + 1) * sizeof(char));
    for (int i = 0; i < len; i++) {
        rev[i] = s[len - 1 - i];
    }
    rev[len] = '\0';
    if (p1 == '(') {
        helper(rev, 0, 0, ')', '(', res, resSize);
        free(rev);
    } else {
        *res = (char**)realloc(*res, (*resSize + 1) * sizeof(char*));
        (*res)[*resSize] = rev;
        (*resSize)++;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** removeInvalidParentheses(char* s, int* returnSize) {
    *returnSize = 0;
    char** res = NULL;
    helper(s, 0, 0, '(', ')', &res, returnSize);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> RemoveInvalidParentheses(string s) {
        List<string> result = new List<string>();
        HashSet<string> visited = new HashSet<string>();
        Queue<string> queue = new Queue<string>();

        queue.Enqueue(s);
        visited.Add(s);
        bool found = false;

        while (queue.Count > 0) {
            int size = queue.Count;
            for (int i = 0; i < size; i++) {
                string curr = queue.Dequeue();
                if (IsValid(curr)) {
                    result.Add(curr);
                    found = true;
                }
                if (!found) {
                    for (int j = 0; j < curr.Length; j++) {
                        if (curr[j] != '(' && curr[j] != ')') continue;
                        string next = curr.Remove(j, 1);
                        if (visited.Add(next)) {
                            queue.Enqueue(next);
                        }
                    }
                }
            }
            if (found) break;
        }

        if (result.Count == 0) result.Add("");
        return result;
    }

    private bool IsValid(string s) {
        int count = 0;
        foreach (char c in s) {
            if (c == '(') count++;
            else if (c == ')') {
                count--;
                if (count < 0) return false;
            }
        }
        return count == 0;
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
 * @return {string[]}
 */
var removeInvalidParentheses = function(s) {
    const isValid = (str) => {
        let count = 0;
        for (let i = 0; i < str.length; i++) {
            if (str[i] === '(') count++;
            else if (str[i] === ')') {
                if (count === 0) return false;
                count--;
            }
        }
        return count === 0;
    };

    let level = new Set([s]);
    while (level.size > 0) {
        let valid = Array.from(level).filter(isValid);
        if (valid.length > 0) return valid;

        let nextLevel = new Set();
        for (let str of level) {
            for (let i = 0; i < str.length; i++) {
                if (str[i] === '(' || str[i] === ')') {
                    nextLevel.add(str.slice(0, i) + str.slice(i + 1));
                }
            }
        }
        level = nextLevel;
    }
    return [""];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function removeInvalidParentheses(s: string): string[] {
    let remL = 0, remR = 0;
    for (const char of s) {
        if (char === '(') remL++;
        else if (char === ')') {
            if (remL > 0) remL--;
            else remR++;
        }
    }

    const result: string[] = [];

    function isValid(str: string): boolean {
        let count = 0;
        for (const char of str) {
            if (char === '(') count++;
            else if (char === ')') {
                count--;
                if (count < 0) return false;
            }
        }
        return count === 0;
    }

    function dfs(start: number, l: number, r: number, current: string) {
        if (l === 0 && r === 0) {
            if (isValid(current)) result.push(current);
            return;
        }

        for (let i = start; i < current.length; i++) {
            if (i > start && current[i] === current[i - 1]) continue;

            if (current[i] === '(' && l > 0) {
                dfs(i, l - 1, r, current.substring(0, i) + current.substring(i + 1));
            } else if (current[i] === ')' && r > 0) {
                dfs(i, l, r - 1, current.substring(0, i) + current.substring(i + 1));
            }
        }
    }

    dfs(0, remL, remR, s);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function removeInvalidParentheses($s) {
        $remL = 0; $remR = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] == '(') $remL++;
            elseif ($s[$i] == ')') {
                if ($remL > 0) $remL--;
                else $remR++;
            }
        }
        $result = [];
        $this->dfs(0, $remL, $remR, $s, $result);
        return $result;
    }

    private function isValid($str) {
        $count = 0;
        $len = strlen($str);
        for ($i = 0; $i < $len; $i++) {
            if ($str[$i] == '(') $count++;
            elseif ($str[$i] == ')') {
                $count--;
                if ($count < 0) return false;
            }
        }
        return $count == 0;
    }

    private function dfs($start, $l, $r, $current, &$result) {
        if ($l == 0 && $r == 0) {
            if ($this->isValid($current)) $result[] = $current;
            return;
        }
        $len = strlen($current);
        for ($i = $start; $i < $len; $i++) {
            if ($i > $start && $current[$i] == $current[$i - 1]) continue;
            if ($current[$i] == '(' && $l > 0) {
                $this->dfs($i, $l - 1, $r, substr($current, 0, $i) . substr($current, $i + 1), $result);
            } elseif ($current[$i] == ')' && $r > 0) {
                $this->dfs($i, $l, $r - 1, substr($current, 0, $i) . substr($current, $i + 1), $result);
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func removeInvalidParentheses(_ s: String) -> [String] {
        var remL = 0, remR = 0
        let chars = Array(s)
        for char in chars {
            if char == "(" { remL += 1 }
            else if char == ")" {
                if remL > 0 { remL -= 1 }
                else { remR += 1 }
            }
        }

        var result = [String]()

        func isValid(_ arr: [Character]) -> Bool {
            var count = 0
            for char in arr {
                if char == "(" { count += 1 }
                else if char == ")" {
                    count -= 1
                    if count < 0 { return false }
                }
            }
            return count == 0
        }

        func dfs(_ start: Int, _ l: Int, _ r: Int, _ current: [Character]) {
            if l == 0 && r == 0 {
                if isValid(current) {
                    result.append(String(current))
                }
                return
            }

            for i in start..<current.count {
                if i > start && current[i] == current[i-1] { continue }

                if current[i] == "(" && l > 0 {
                    var next = current
                    next.remove(at: i)
                    dfs(i, l - 1, r, next)
                } else if current[i] == ")" && r > 0 {
                    var next = current
                    next.remove(at: i)
                    dfs(i, l, r - 1, next)
                }
            }
        }

        dfs(0, remL, remR, chars)
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun removeInvalidParentheses(s: String): List<String> {
        var remL = 0
        var remR = 0
        for (char in s) {
            if (char == '(') remL++
            else if (char == ')') {
                if (remL > 0) remL--
                else remR++
            }
        }

        val result = mutableListOf<String>()
        dfs(0, remL, remR, s, result)
        return result
    }

    private fun isValid(s: String): Boolean {
        var count = 0
        for (char in s) {
            if (char == '(') count++
            else if (char == ')') {
                count--
                if (count < 0) return false
            }
        }
        return count == 0
    }

    private fun dfs(start: Int, l: Int, r: Int, current: String, result: MutableList<String>) {
        if (l == 0 && r == 0) {
            if (isValid(current)) result.add(current)
            return
        }

        for (i in start until current.length) {
            if (i > start && current[i] == current[i - 1]) continue

            if (current[i] == '(' && l > 0) {
                dfs(i, l - 1, r, current.substring(0, i) + current.substring(i + 1), result)
            } else if (current[i] == ')' && r > 0) {
                dfs(i, l, r - 1, current.substring(0, i) + current.substring(i + 1), result)
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<String> removeInvalidParentheses(String s) {
    int l = 0, r = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        l++;
      } else if (s[i] == ')') {
        if (l > 0) {
          l--;
        } else {
          r++;
        }
      }
    }

    List<String> res = [];

    bool isValid(String str) {
      int count = 0;
      for (int i = 0; i < str.length; i++) {
        if (str[i] == '(') {
          count++;
        } else if (str[i] == ')') {
          count--;
          if (count < 0) return false;
        }
      }
      return count == 0;
    }

    void dfs(String curr, int start, int lRem, int rRem) {
      if (lRem == 0 && rRem == 0) {
        if (isValid(curr)) res.add(curr);
        return;
      }

      for (int i = start; i < curr.length; i++) {
        if (i > start && curr[i] == curr[i - 1]) continue;
        if (curr[i] == '(' && lRem > 0) {
          dfs(curr.substring(0, i) + curr.substring(i + 1), i, lRem - 1, rRem);
        } else if (curr[i] == ')' && rRem > 0) {
          dfs(curr.substring(0, i) + curr.substring(i + 1), i, lRem, rRem - 1);
        }
      }
    }

    dfs(s, 0, l, r);
    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func removeInvalidParentheses(s string) []string {
	l, r := 0, 0
	for _, char := range s {
		if char == '(' {
			l++
		} else if char == ')' {
			if l > 0 {
				l--
			} else {
				r++
			}
		}
	}

	var res []string
	var dfs func(string, int, int, int)

	isValid := func(str string) bool {
		count := 0
		for _, char := range str {
			if char == '(' {
				count++
			} else if char == ')' {
				count--
				if count < 0 {
					return false
				}
			}
		}
		return count == 0
	}

	dfs = func(curr string, start, lRem, rRem int) {
		if lRem == 0 && rRem == 0 {
			if isValid(curr) {
				res = append(res, curr)
			}
			return
		}

		for i := start; i < len(curr); i++ {
			if i > start && curr[i] == curr[i-1] {
				continue
			}
			if curr[i] == '(' && lRem > 0 {
				dfs(curr[:i]+curr[i+1:], i, lRem-1, rRem)
			} else if curr[i] == ')' && rRem > 0 {
				dfs(curr[:i]+curr[i+1:], i, lRem, rRem-1)
			}
		}
	}

	dfs(s, 0, l, r)
	return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {String[]}
def remove_invalid_parentheses(s)
  l = 0
  r = 0
  s.each_char do |c|
    if c == '('
      l += 1
    elsif c == ')'
      if l > 0
        l -= 1
      else
        r += 1
      end
    end
  end

  @res = []

  def is_valid?(str)
    count = 0
    str.each_char do |c|
      if c == '('
        count += 1
      elsif c == ')'
        count -= 1
        return false if count < 0
      end
    end
    count == 0
  end

  def solve(str, start, l_rem, r_rem)
    if l_rem == 0 && r_rem == 0
      @res << str if is_valid?(str)
      return
    end
    (start...str.length).each do |i|
      next if i > start && str[i] == str[i - 1]
      if str[i] == '(' && l_rem > 0
        solve(str[0...i] + str[i + 1...str.length], i, l_rem - 1, r_rem)
      elsif str[i] == ')' && r_rem > 0
        solve(str[0...i] + str[i + 1...str.length], i, l_rem, r_rem - 1)
      end
    end
  end

  solve(s, 0, l, r)
  @res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def removeInvalidParentheses(s: String): List[String] = {
        var l = 0
        var r = 0
        for (c <- s) {
            if (c == '(') l += 1
            else if (c == ')') {
                if (l > 0) l -= 1
                else r += 1
            }
        }

        val res = scala.collection.mutable.ListBuffer[String]()
        dfs(s, 0, l, r, res)
        res.toList
    }

    private def isValid(s: String): Boolean = {
        var count = 0
        for (c <- s) {
            if (c == '(') count += 1
            else if (c == ')') {
                count -= 1
                if (count < 0) return false
            }
        }
        count == 0
    }

    private def dfs(s: String, start: Int, l: Int, r: Int, res: scala.collection.mutable.ListBuffer[String]): Unit = {
        if (l == 0 && r == 0) {
            if (isValid(s)) res += s
            return
        }

        for (i <- start until s.length) {
            if (i == start || s(i) != s(i - 1)) {
                if (s(i) == '(' && l > 0) {
                    dfs(s.substring(0, i) + s.substring(i + 1), i, l - 1, r, res)
                } else if (s(i) == ')' && r > 0) {
                    dfs(s.substring(0, i) + s.substring(i + 1), i, l, r - 1, res)
                }
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashSet;

impl Solution {
    pub fn remove_invalid_parentheses(s: String) -> Vec<String> {
        let mut current_level = HashSet::new();
        current_level.insert(s);

        loop {
            let mut valid_ones = Vec::new();
            for s_str in &current_level {
                if Self::is_valid(s_str) {
                    valid_ones.push(s_str.clone());
                }
            }

            if !valid_ones.is_empty() {
                return valid_ones;
            }

            let mut next_level = HashSet::new();
            for s_str in &current_level {
                for (i, c) in s_str.char_indices() {
                    if c == '(' || c == ')' {
                        let mut next_s = String::with_capacity(s_str.len() - 1);
                        next_s.push_str(&s_str[..i]);
                        next_s.push_str(&s_str[i + c.len_utf8()..]);
                        next_level.insert(next_s);
                    }
                }
            }

            if next_level.is_empty() {
                return vec!["".to_string()];
            }
            current_level = next_level;
        }
    }

    fn is_valid(s: &str) -> bool {
        let mut count = 0;
        for c in s.chars() {
            if c == '(' {
                count += 1;
            } else if c == ')' {
                if count == 0 {
                    return false;
                }
                count -= 1;
            }
        }
        count == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/set)

(define (is-valid? s)
  (let loop ([chars (string->list s)] [count 0])
    (cond
      [(< count 0) #f]
      [(empty? chars) (= count 0)]
      [(char=? (car chars) #\() (loop (cdr chars) (+ count 1))]
      [(char=? (car chars) #\)) (loop (cdr chars) (- count 1))]
      [else (loop (cdr chars) count)])))

(define (generate-next current-set)
  (let ([next-set (mutable-set)])
    (for ([s (in-set current-set)])
      (let ([chars (string->list s)])
        (let loop ([prefix '()] [suffix chars])
          (when (not (empty? suffix))
            (let ([h (car suffix)]
                  [t (cdr suffix)])
              (when (or (char=? h #\() (char=? h #\)))
                (set-add! next-set (list->string (append (reverse prefix) t))))
              (loop (cons h prefix) t))))))
    next-set))

(define (bfs current-set)
  (let ([valid-ones (filter is-valid? (set->list current-set))])
    (if (not (empty? valid-ones))
        valid-ones
        (let ([next-set (generate-next current-set)])
          (if (set-empty? next-set)
              '("")
              (bfs next-set))))))

(define/contract (remove-invalid-parentheses s)
  (-> string? (listof string?))
  (bfs (set s)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec remove_invalid_parentheses(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
remove_invalid_parentheses(S) ->
    bfs(sets:add_element(S, sets:new())).

bfs(Queue) ->
    List = sets:to_list(Queue),
    Valid = [X || X <- List, is_valid(X)],
    case Valid of
        [] ->
            NextQueue = generate_next(List),
            case sets:size(NextQueue) of
                0 -> [<<"">>];
                _ -> bfs(NextQueue)
            end;
        _ ->
            Valid
    end.

is_valid(S) ->
    is_valid_list(binary_to_list(S), 0).

is_valid_list([], 0) -> true;
is_valid_list([], _) -> false;
is_valid_list([$( | T], Acc) -> is_valid_list(T, Acc + 1);
is_valid_list([$) | T], Acc) ->
    if Acc > 0 -> is_valid_list(T, Acc - 1);
       true -> false
    end;
is_valid_list([_ | T], Acc) -> is_valid_list(T, Acc).

generate_next(List) ->
    lists:foldl(fun(S, AccSet) ->
        SList = binary_to_list(S),
        generate_removals(SList, [], AccSet)
    end, sets:new(), List).

generate_removals([], _Prefix, AccSet) -> AccSet;
generate_removals([H | T], Prefix, AccSet) when H =:= $(; H =:= $) ->
    NewBinary = list_to_binary(lists:reverse(Prefix) ++ T),
    NewAccSet = sets:add_element(NewBinary, AccSet),
    generate_removals(T, [H | Prefix], NewAccSet);
generate_removals([H | T], Prefix, AccSet) ->
    generate_removals(T, [H | Prefix], AccSet).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec remove_invalid_parentheses(s :: String.t) :: [String.t]
  def remove_invalid_parentheses(s) do
    bfs(MapSet.new([s]))
  end

  defp bfs(set) do
    valid = Enum.filter(set, &is_valid?/1)
    if !Enum.empty?(valid) do
      valid
    else
      next_set = Enum.reduce(set, MapSet.new(), fn str, acc ->
        generate_next_strings(str, acc)
      end)
      if MapSet.size(next_set) == 0 do
        [""]
      else
        bfs(next_set)
      end
    end
  end

  defp generate_next_strings(str, acc) do
    charlist = String.to_charlist(str)
    generate_removals(charlist, [], acc)
  end

  defp generate_removals([], _prefix, acc), do: acc
  defp generate_removals([h | t], prefix, acc) when h == ?( or h == ?) do
    new_str = List.to_string(Enum.reverse(prefix) ++ t)
    generate_removals(t, [h | prefix], MapSet.put(acc, new_str))
  end
  defp generate_removals([h | t], prefix, acc) do
    generate_removals(t, [h | prefix], acc)
  end

  defp is_valid?(s) do
    s
    |> String.to_charlist()
    |> Enum.reduce_while(0, fn
      ?(, acc -> {:cont, acc + 1}
      ?), acc -> if acc > 0, do: {:cont, acc - 1}, else: {:halt, -1}
      _, acc -> {:cont, acc}
    end) == 0
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(2^N) where N is the length of the string. In the worst case, every character is a parenthesis and the algorithm explores two choices (keep or remove) for each. While the target removal counts and balance constraints prune the search space significantly, the theoretical upper bound remains exponential. Given the constraint of at most 20 parentheses, $2^{20}$ operations are well within the time limits.
- **Space Complexity:** O(2^N \cdot N) in the worst case. The recursion stack uses $O(N)$ space, but the result set can store many unique valid strings, each up to $N$ characters long. The temporary string construction during recursion also contributes to the space complexity.
