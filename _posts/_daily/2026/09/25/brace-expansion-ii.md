---
layout: post
title: "Brace Expansion II"
date: 2026-09-25 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Hash Table", "String", "Backtracking", "Stack", "Breadth-First Search", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/brace-expansion-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<string> braceExpansionII(string expression)\
        \ {\n        int i = 0;\n        set<string> result = parseExpression(expression,\
        \ i);\n        return vector<string>(result.begin(), result.end());\n    }\n\
        \nprivate:\n    set<string> parseExpression(const string& s, int& i) {\n   \
        \     set<string> res;\n        while (true) {\n            set<string> term\
        \ = parseTerm(s, i);\n            res.insert(term.begin(), term.end());\n  \
        \          if (i < s.length() && s[i] == ',') {\n                i++;\n    \
        \        } else {\n                break;\n            }\n        }\n      \
        \  return res;\n    }\n\n    set<string> parseTerm(const string& s, int& i)\
        \ {\n        set<string> res = {\"\"};\n        while (i < s.length() && s[i]\
        \ != ',' && s[i] != '}') {\n            set<string> next = parseFactor(s, i);\n\
        \            set<string> combined;\n            for (const string& a : res)\
        \ {\n                for (const string& b : next) {\n                    combined.insert(a\
        \ + b);\n                }\n            }\n            res = std::move(combined);\n\
        \        }\n        return res;\n    }\n\n    set<string> parseFactor(const\
        \ string& s, int& i) {\n        if (s[i] == '{') {\n            i++;\n     \
        \       set<string> res = parseExpression(s, i);\n            i++; // skip '}'\n\
        \            return res;\n        } else {\n            int start = i;\n   \
        \         while (i < s.length() && islower(s[i])) {\n                i++;\n\
        \            }\n            return {s.substr(start, i - start)};\n        }\n\
        \    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    private int i = 0;\n\n   \
        \ public List<String> braceExpansionII(String expression) {\n        TreeSet<String>\
        \ resultSet = parseExpression(expression);\n        return new ArrayList<>(resultSet);\n\
        \    }\n\n    private TreeSet<String> parseExpression(String s) {\n        TreeSet<String>\
        \ res = new TreeSet<>();\n        while (true) {\n            TreeSet<String>\
        \ term = parseTerm(s);\n            res.addAll(term);\n            if (i < s.length()\
        \ && s.charAt(i) == ',') {\n                i++;\n            } else {\n   \
        \             break;\n            }\n        }\n        return res;\n    }\n\
        \n    private TreeSet<String> parseTerm(String s) {\n        TreeSet<String>\
        \ res = new TreeSet<>();\n        res.add(\"\");\n        while (i < s.length()\
        \ && s.charAt(i) != ',' && s.charAt(i) != '}') {\n            TreeSet<String>\
        \ next = parseFactor(s);\n            TreeSet<String> combined = new TreeSet<>();\n\
        \            for (String a : res) {\n                for (String b : next) {\n\
        \                    combined.add(a + b);\n                }\n            }\n\
        \            res = combined;\n        }\n        return res;\n    }\n\n    private\
        \ TreeSet<String> parseFactor(String s) {\n        if (s.charAt(i) == '{') {\n\
        \            i++;\n            TreeSet<String> res = parseExpression(s);\n \
        \           i++;\n            return res;\n        } else {\n            int\
        \ start = i;\n            while (i < s.length() && Character.isLowerCase(s.charAt(i)))\
        \ {\n                i++;\n            }\n            TreeSet<String> res =\
        \ new TreeSet<>();\n            res.add(s.substring(start, i));\n          \
        \  return res;\n        }\n    }\n}"
      python: "class Solution(object):\n    def braceExpansionII(self, expression):\n\
        \        \"\"\"\n        :type expression: str\n        :rtype: List[str]\n\
        \        \"\"\"\n        self.i = 0\n        self.s = expression\n\n       \
        \ def parseExpression():\n            res = set()\n            while True:\n\
        \                term = parseTerm()\n                res.update(term)\n    \
        \            if self.i < len(self.s) and self.s[self.i] == ',':\n          \
        \          self.i += 1\n                else:\n                    break\n \
        \           return res\n\n        def parseTerm():\n            res = {\"\"\
        }\n            while self.i < len(self.s) and self.s[self.i] not in (',', '}'):\n\
        \                next_set = parseFactor()\n                new_res = set()\n\
        \                for a in res:\n                    for b in next_set:\n   \
        \                     new_res.add(a + b)\n                res = new_res\n  \
        \          return res\n\n        def parseFactor():\n            if self.s[self.i]\
        \ == '{':\n                self.i += 1\n                res = parseExpression()\n\
        \                self.i += 1\n                return res\n            else:\n\
        \                start = self.i\n                while self.i < len(self.s)\
        \ and 'a' <= self.s[self.i] <= 'z':\n                    self.i += 1\n     \
        \           return {self.s[start:self.i]}\n\n        final_set = parseExpression()\n\
        \        return sorted(list(final_set))"
      python3: "class Solution:\n    def braceExpansionII(self, expression: str) ->\
        \ list[str]:\n        stack = [[set([\"\"])]]\n        for char in expression:\n\
        \            if char == '{':\n                stack.append([set([\"\"])])\n\
        \            elif char == '}':\n                union_res = set().union(*stack.pop())\n\
        \                prev_union = stack[-1]\n                last_set = prev_union[-1]\n\
        \                prev_union[-1] = {s1 + s2 for s1 in last_set for s2 in union_res}\n\
        \            elif char == ',':\n                stack[-1].append(set([\"\"]))\n\
        \            else:\n                current_union = stack[-1]\n            \
        \    last_set = current_union[-1]\n                current_union[-1] = {s +\
        \ char for s in last_set}\n\n        final_union = set().union(*stack[0])\n\
        \        return sorted(list(final_union))"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <ctype.h>\n\
        \ntypedef struct {\n    char** words;\n    int size;\n    int cap;\n} Set;\n\
        \nchar* my_strdup(const char* s) {\n    char* d = malloc(strlen(s) + 1);\n \
        \   if (d) strcpy(d, s);\n    return d;\n}\n\nint compare_strings(const void*\
        \ a, const void* b) {\n    return strcmp(*(const char**)a, *(const char**)b);\n\
        }\n\nvoid sort_and_unique(Set* s) {\n    if (s->size <= 1) return;\n    qsort(s->words,\
        \ s->size, sizeof(char*), compare_strings);\n    int j = 0;\n    for (int i\
        \ = 1; i < s->size; i++) {\n        if (strcmp(s->words[j], s->words[i]) !=\
        \ 0) {\n            s->words[++j] = s->words[i];\n        } else {\n       \
        \     free(s->words[i]);\n        }\n    }\n    s->size = j + 1;\n}\n\nSet create_empty_set()\
        \ {\n    Set s = {NULL, 0, 0};\n    return s;\n}\n\nSet singleton_set(const\
        \ char* word) {\n    Set s;\n    s.size = 1;\n    s.cap = 1;\n    s.words =\
        \ malloc(sizeof(char*));\n    s.words[0] = my_strdup(word);\n    return s;\n\
        }\n\nvoid free_set(Set s) {\n    for (int i = 0; i < s.size; i++) free(s.words[i]);\n\
        \    if (s.words) free(s.words);\n}\n\nSet union_sets(Set s1, Set s2) {\n  \
        \  Set res;\n    res.size = 0;\n    res.cap = s1.size + s2.size;\n    if (res.cap\
        \ == 0) {\n        if (s1.words) free(s1.words);\n        if (s2.words) free(s2.words);\n\
        \        return create_empty_set();\n    }\n    res.words = malloc(res.cap *\
        \ sizeof(char*));\n    for (int i = 0; i < s1.size; i++) res.words[res.size++]\
        \ = s1.words[i];\n    for (int i = 0; i < s2.size; i++) res.words[res.size++]\
        \ = s2.words[i];\n    if (s1.words) free(s1.words);\n    if (s2.words) free(s2.words);\n\
        \    sort_and_unique(&res);\n    return res;\n}\n\nSet multiply(Set s1, Set\
        \ s2) {\n    if (s1.size == 0 || s2.size == 0) {\n        free_set(s1); free_set(s2);\n\
        \        return create_empty_set();\n    }\n    Set res;\n    res.size = 0;\n\
        \    res.cap = s1.size * s2.size;\n    res.words = malloc(res.cap * sizeof(char*));\n\
        \    for (int i = 0; i < s1.size; i++) {\n        for (int j = 0; j < s2.size;\
        \ j++) {\n            char* s = malloc(strlen(s1.words[i]) + strlen(s2.words[j])\
        \ + 1);\n            strcpy(s, s1.words[i]);\n            strcat(s, s2.words[j]);\n\
        \            res.words[res.size++] = s;\n        }\n    }\n    free_set(s1);\
        \ free_set(s2);\n    sort_and_unique(&res);\n    return res;\n}\n\nSet parse_union(char*\
        \ expr, int* p);\n\nSet parse_concatenation(char* expr, int* p) {\n    Set res\
        \ = singleton_set(\"\");\n    while (expr[*p] != '\\0' && expr[*p] != ',' &&\
        \ expr[*p] != '}') {\n        Set factor;\n        if (expr[*p] == '{') {\n\
        \            (*p)++;\n            factor = parse_union(expr, p);\n         \
        \   if (expr[*p] == '}') (*p)++;\n        } else {\n            char word[2]\
        \ = {expr[(*p)++], '\\0'};\n            factor = singleton_set(word);\n    \
        \    }\n        res = multiply(res, factor);\n    }\n    return res;\n}\n\n\
        Set parse_union(char* expr, int* p) {\n    Set res = create_empty_set();\n \
        \   while (1) {\n        Set term = parse_concatenation(expr, p);\n        res\
        \ = union_sets(res, term);\n        if (expr[*p] == ',') (*p)++;\n        else\
        \ break;\n    }\n    return res;\n}\n\nchar** braceExpansionII(char* expression,\
        \ int* returnSize) {\n    int p = 0;\n    Set res = parse_union(expression,\
        \ &p);\n    *returnSize = res.size;\n    return res.words;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public IList<string> BraceExpansionII(string expression) {\n      \
        \  var stack = new Stack<List<HashSet<string>>>();\n        stack.Push(new List<HashSet<string>>\
        \ { new HashSet<string> { \"\" } });\n\n        for (int i = 0; i < expression.Length;\
        \ i++) {\n            char c = expression[i];\n            if (c == '{') {\n\
        \                stack.Push(new List<HashSet<string>> { new HashSet<string>\
        \ { \"\" } });\n            } else if (c == '}') {\n                var currentUnionList\
        \ = stack.Pop();\n                var unionResult = new HashSet<string>();\n\
        \                foreach (var sSet in currentUnionList) {\n                \
        \    foreach (var s in sSet) unionResult.Add(s);\n                }\n\n    \
        \            var parentUnionList = stack.Peek();\n                var lastParentSet\
        \ = parentUnionList[parentUnionList.Count - 1];\n                var multipliedSet\
        \ = new HashSet<string>();\n                foreach (var s1 in lastParentSet)\
        \ {\n                    foreach (var s2 in unionResult) {\n               \
        \         multipliedSet.Add(s1 + s2);\n                    }\n             \
        \   }\n                parentUnionList[parentUnionList.Count - 1] = multipliedSet;\n\
        \            } else if (c == ',') {\n                stack.Peek().Add(new HashSet<string>\
        \ { \"\" });\n            } else {\n                var currentUnionList = stack.Peek();\n\
        \                var lastSet = currentUnionList[currentUnionList.Count - 1];\n\
        \                var nextSet = new HashSet<string>();\n                foreach\
        \ (var s in lastSet) {\n                    nextSet.Add(s + c);\n          \
        \      }\n                currentUnionList[currentUnionList.Count - 1] = nextSet;\n\
        \            }\n        }\n\n        var finalResultSet = new HashSet<string>();\n\
        \        foreach (var sSet in stack.Peek()) {\n            foreach (var s in\
        \ sSet) finalResultSet.Add(s);\n        }\n\n        var resultList = new List<string>(finalResultSet);\n\
        \        resultList.Sort(StringComparer.Ordinal);\n        return resultList;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} expression\n * @return {string[]}\n */\n\
        var braceExpansionII = function(expression) {\n    let stack = [[new Set([\"\
        \"])]];\n\n    for (let i = 0; i < expression.length; i++) {\n        let char\
        \ = expression[i];\n        if (char === '{') {\n            stack.push([new\
        \ Set([\"\"])]);\n        } else if (char === '}') {\n            let currentUnion\
        \ = stack.pop();\n            let unionRes = new Set();\n            for (let\
        \ sSet of currentUnion) {\n                for (let s of sSet) unionRes.add(s);\n\
        \            }\n            let prevUnion = stack[stack.length - 1];\n     \
        \       let lastSet = prevUnion[prevUnion.length - 1];\n            let nextSet\
        \ = new Set();\n            for (let s1 of lastSet) {\n                for (let\
        \ s2 of unionRes) {\n                    nextSet.add(s1 + s2);\n           \
        \     }\n            }\n            prevUnion[prevUnion.length - 1] = nextSet;\n\
        \        } else if (char === ',') {\n            stack[stack.length - 1].push(new\
        \ Set([\"\"]));\n        } else {\n            let currentUnion = stack[stack.length\
        \ - 1];\n            let lastSet = currentUnion[currentUnion.length - 1];\n\
        \            let nextSet = new Set();\n            for (let s of lastSet) {\n\
        \                nextSet.add(s + char);\n            }\n            currentUnion[currentUnion.length\
        \ - 1] = nextSet;\n        }\n    }\n\n    let finalSet = new Set();\n    for\
        \ (let sSet of stack[0]) {\n        for (let s of sSet) finalSet.add(s);\n \
        \   }\n\n    return Array.from(finalSet).sort();\n};"
      typescript: "function braceExpansionII(expression: string): string[] {\n    function\
        \ evaluate(expr: string): Set<string> {\n        if (expr === \"\") return new\
        \ Set([\"\"]);\n\n        let braceCount = 0;\n        let commaIndices: number[]\
        \ = [];\n        for (let i = 0; i < expr.length; i++) {\n            if (expr[i]\
        \ === \"{\") braceCount++;\n            else if (expr[i] === \"}\") braceCount--;\n\
        \            else if (expr[i] === \",\" && braceCount === 0) {\n           \
        \     commaIndices.push(i);\n            }\n        }\n\n        if (commaIndices.length\
        \ > 0) {\n            let res = new Set<string>();\n            let start =\
        \ 0;\n            for (let idx of commaIndices) {\n                let subRes\
        \ = evaluate(expr.substring(start, idx));\n                for (const s of subRes)\
        \ res.add(s);\n                start = idx + 1;\n            }\n           \
        \ let subRes = evaluate(expr.substring(start));\n            for (const s of\
        \ subRes) res.add(s);\n            return res;\n        }\n\n        let firstUnit:\
        \ Set<string>;\n        let rest: string;\n\n        if (expr[0] === \"{\")\
        \ {\n            let bc = 0;\n            let j = 0;\n            for (let i\
        \ = 0; i < expr.length; i++) {\n                if (expr[i] === \"{\") bc++;\n\
        \                else if (expr[i] === \"}\") {\n                    bc--;\n\
        \                    if (bc === 0) {\n                        j = i;\n     \
        \                   break;\n                    }\n                }\n     \
        \       }\n            firstUnit = evaluate(expr.substring(1, j));\n       \
        \     rest = expr.substring(j + 1);\n        } else {\n            firstUnit\
        \ = new Set([expr[0]]);\n            rest = expr.substring(1);\n        }\n\n\
        \        if (rest === \"\") return firstUnit;\n\n        let restSet = evaluate(rest);\n\
        \        let combined = new Set<string>();\n        for (const s1 of firstUnit)\
        \ {\n            for (const s2 of restSet) {\n                combined.add(s1\
        \ + s2);\n            }\n        }\n        return combined;\n    }\n\n    const\
        \ resultSet = evaluate(expression);\n    return Array.from(resultSet).sort();\n\
        }"
      php: "class Solution {\n\n    /**\n     * @param String $expression\n     * @return\
        \ String[]\n     */\n    function braceExpansionII($expression) {\n        $res\
        \ = $this->evaluate($expression);\n        sort($res);\n        return $res;\n\
        \    }\n\n    private function evaluate($expr) {\n        if ($expr === \"\"\
        ) return [\"\"];\n        $braceCount = 0;\n        $commaIndices = [];\n  \
        \      $len = strlen($expr);\n\n        for ($i = 0; $i < $len; $i++) {\n  \
        \          if ($expr[$i] === '{') $braceCount++;\n            else if ($expr[$i]\
        \ === '}') $braceCount--;\n            else if ($expr[$i] === ',' && $braceCount\
        \ === 0) {\n                $commaIndices[] = $i;\n            }\n        }\n\
        \n        if (!empty($commaIndices)) {\n            $resSet = [];\n        \
        \    $start = 0;\n            foreach ($commaIndices as $idx) {\n          \
        \      $subRes = $this->evaluate(substr($expr, $start, $idx - $start));\n  \
        \              foreach ($subRes as $s) $resSet[$s] = true;\n               \
        \ $start = $idx + 1;\n            }\n            $subRes = $this->evaluate(substr($expr,\
        \ $start));\n            foreach ($subRes as $s) $resSet[$s] = true;\n     \
        \       return array_keys($resSet);\n        }\n\n        if ($expr[0] === '{')\
        \ {\n            $bc = 0;\n            $j = 0;\n            for ($i = 0; $i\
        \ < $len; $i++) {\n                if ($expr[$i] === '{') $bc++;\n         \
        \       else if ($expr[$i] === '}') {\n                    $bc--;\n        \
        \            if ($bc === 0) {\n                        $j = $i;\n          \
        \              break;\n                    }\n                }\n          \
        \  }\n            $firstUnit = $this->evaluate(substr($expr, 1, $j - 1));\n\
        \            $rest = substr($expr, $j + 1);\n            if ($rest === false)\
        \ $rest = \"\";\n        } else {\n            $firstUnit = [$expr[0]];\n  \
        \          $rest = substr($expr, 1);\n            if ($rest === false) $rest\
        \ = \"\";\n        }\n\n        if ($rest === \"\") return $firstUnit;\n\n \
        \       $restSet = $this->evaluate($rest);\n        $combinedSet = [];\n   \
        \     foreach ($firstUnit as $s1) {\n            foreach ($restSet as $s2) {\n\
        \                $combinedSet[$s1 . $s2] = true;\n            }\n        }\n\
        \        return array_keys($combinedSet);\n    }\n}"
      swift: "class Solution {\n    func braceExpansionII(_ expression: String) -> [String]\
        \ {\n        func evaluate(_ expr: String) -> Set<String> {\n            if\
        \ expr.isEmpty { return [\"\"] }\n            let chars = Array(expr)\n    \
        \        var braceCount = 0\n            var commaIndices = [Int]()\n\n    \
        \        for i in 0..<chars.count {\n                if chars[i] == \"{\" {\
        \ braceCount += 1 }\n                else if chars[i] == \"}\" { braceCount\
        \ -= 1 }\n                else if chars[i] == \",\" && braceCount == 0 {\n \
        \                   commaIndices.append(i)\n                }\n            }\n\
        \n            if !commaIndices.isEmpty {\n                var res = Set<String>()\n\
        \                var start = 0\n                for idx in commaIndices {\n\
        \                    res.formUnion(evaluate(String(chars[start..<idx])))\n \
        \                   start = idx + 1\n                }\n                res.formUnion(evaluate(String(chars[start...])))\n\
        \                return res\n            }\n\n            var firstUnit: Set<String>\n\
        \            var rest: String\n\n            if chars[0] == \"{\" {\n      \
        \          var bc = 0\n                var j = 0\n                for i in 0..<chars.count\
        \ {\n                    if chars[i] == \"{\" { bc += 1 }\n                \
        \    else if chars[i] == \"}\" {\n                        bc -= 1\n        \
        \                if bc == 0 {\n                            j = i\n         \
        \                   break\n                        }\n                    }\n\
        \                }\n                firstUnit = evaluate(String(chars[1..<j]))\n\
        \                rest = String(chars[(j + 1)...])\n            } else {\n  \
        \              firstUnit = [String(chars[0])]\n                rest = String(chars[1...])\n\
        \            }\n\n            if rest.isEmpty { return firstUnit }\n\n     \
        \       let restSet = evaluate(rest)\n            var combined = Set<String>()\n\
        \            for s1 in firstUnit {\n                for s2 in restSet {\n  \
        \                  combined.insert(s1 + s2)\n                }\n           \
        \ }\n            return combined\n        }\n\n        let resultSet = evaluate(expression)\n\
        \        return Array(resultSet).sorted()\n    }\n}"
      kotlin: "class Solution {\n    fun braceExpansionII(expression: String): List<String>\
        \ {\n        fun evaluate(expr: String): Set<String> {\n            if (expr.isEmpty())\
        \ return setOf(\"\")\n\n            var braceCount = 0\n            val commaIndices\
        \ = mutableListOf<Int>()\n            for (i in expr.indices) {\n          \
        \      if (expr[i] == '{') braceCount++\n                else if (expr[i] ==\
        \ '}') braceCount--\n                else if (expr[i] == ',' && braceCount ==\
        \ 0) {\n                    commaIndices.add(i)\n                }\n       \
        \     }\n\n            if (commaIndices.isNotEmpty()) {\n                val\
        \ res = mutableSetOf<String>()\n                var start = 0\n            \
        \    for (idx in commaIndices) {\n                    res.addAll(evaluate(expr.substring(start,\
        \ idx)))\n                    start = idx + 1\n                }\n         \
        \       res.addAll(evaluate(expr.substring(start)))\n                return\
        \ res\n            }\n\n            val firstUnit: Set<String>\n           \
        \ val rest: String\n            if (expr[0] == '{') {\n                var bc\
        \ = 0\n                var j = 0\n                for (i in expr.indices) {\n\
        \                    if (expr[i] == '{') bc++\n                    else if (expr[i]\
        \ == '}') {\n                        bc--\n                        if (bc ==\
        \ 0) {\n                            j = i\n                            break\n\
        \                        }\n                    }\n                }\n     \
        \           firstUnit = evaluate(expr.substring(1, j))\n                rest\
        \ = expr.substring(j + 1)\n            } else {\n                firstUnit =\
        \ setOf(expr[0].toString())\n                rest = expr.substring(1)\n    \
        \        }\n\n            if (rest.isEmpty()) return firstUnit\n\n         \
        \   val restSet = evaluate(rest)\n            val combined = mutableSetOf<String>()\n\
        \            for (s1 in firstUnit) {\n                for (s2 in restSet) {\n\
        \                    combined.add(s1 + s2)\n                }\n            }\n\
        \            return combined\n        }\n\n        return evaluate(expression).toList().sorted()\n\
        \    }\n}"
      dart: "class Solution {\n  List<String> braceExpansionII(String expression) {\n\
        \    List<List<Set<String>>> stackGroups = [];\n    List<Set<String>> stackCur\
        \ = [];\n    List<Set<String>> groups = [];\n    Set<String> cur = {\"\"};\n\
        \n    for (int i = 0; i < expression.length; i++) {\n      String char = expression[i];\n\
        \      if (char == '{') {\n        stackGroups.add(groups);\n        stackCur.add(cur);\n\
        \        groups = [];\n        cur = {\"\"};\n      } else if (char == ',')\
        \ {\n        groups.add(cur);\n        cur = {\"\"};\n      } else if (char\
        \ == '}') {\n        groups.add(cur);\n        Set<String> combinedUnion = {};\n\
        \        for (var g in groups) {\n          combinedUnion.addAll(g);\n     \
        \   }\n\n        Set<String> prevCur = stackCur.removeLast();\n        List<Set<String>>\
        \ prevGroups = stackGroups.removeLast();\n\n        Set<String> nextCur = {};\n\
        \        for (var s1 in prevCur) {\n          for (var s2 in combinedUnion)\
        \ {\n            nextCur.add(s1 + s2);\n          }\n        }\n        cur\
        \ = nextCur;\n        groups = prevGroups;\n      } else {\n        Set<String>\
        \ nextCur = {};\n        for (var s in cur) {\n          nextCur.add(s + char);\n\
        \        }\n        cur = nextCur;\n      }\n    }\n\n    groups.add(cur);\n\
        \    Set<String> finalSet = {};\n    for (var g in groups) {\n      finalSet.addAll(g);\n\
        \    }\n\n    List<String> res = finalSet.toList();\n    res.sort();\n    return\
        \ res;\n  }\n}"
      go: "import \"sort\"\n\nfunc braceExpansionII(expression string) []string {\n\
        \    type Set map[string]struct{}\n    stackGroups := [][]Set{}\n    stackCur\
        \ := []Set{}\n    groups := []Set{}\n    cur := make(Set)\n    cur[\"\"] = struct{}{}\n\
        \n    for i := 0; i < len(expression); i++ {\n        char := expression[i]\n\
        \        if char == '{' {\n            stackGroups = append(stackGroups, groups)\n\
        \            stackCur = append(stackCur, cur)\n            groups = []Set{}\n\
        \            cur = make(Set)\n            cur[\"\"] = struct{}{}\n        }\
        \ else if char == ',' {\n            groups = append(groups, cur)\n        \
        \    cur = make(Set)\n            cur[\"\"] = struct{}{}\n        } else if\
        \ char == '}' {\n            groups = append(groups, cur)\n            combinedUnion\
        \ := make(Set)\n            for _, g := range groups {\n                for\
        \ s := range g {\n                    combinedUnion[s] = struct{}{}\n      \
        \          }\n            }\n\n            prevCur := stackCur[len(stackCur)-1]\n\
        \            stackCur = stackCur[:len(stackCur)-1]\n            prevGroups :=\
        \ stackGroups[len(stackGroups)-1]\n            stackGroups = stackGroups[:len(stackGroups)-1]\n\
        \n            nextCur := make(Set)\n            for s1 := range prevCur {\n\
        \                for s2 := range combinedUnion {\n                    nextCur[s1+s2]\
        \ = struct{}{}\n                }\n            }\n            cur = nextCur\n\
        \            groups = prevGroups\n        } else {\n            nextCur := make(Set)\n\
        \            for s := range cur {\n                nextCur[s+string(char)] =\
        \ struct{}{}\n            }\n            cur = nextCur\n        }\n    }\n\n\
        \    groups = append(groups, cur)\n    finalSet := make(Set)\n    for _, g :=\
        \ range groups {\n        for s := range g {\n            finalSet[s] = struct{}{}\n\
        \        }\n    }\n\n    res := make([]string, 0, len(finalSet))\n    for s\
        \ := range finalSet {\n        res = append(res, s)\n    }\n    sort.Strings(res)\n\
        \    return res\n}"
      ruby: "require 'set'\n\ndef brace_expansion_ii(expression)\n  stack_groups = []\n\
        \  stack_cur = []\n  groups = []\n  cur = Set.new([\"\"])\n\n  expression.each_char\
        \ do |char|\n    if char == '{'\n      stack_groups.push(groups)\n      stack_cur.push(cur)\n\
        \      groups = []\n      cur = Set.new([\"\"])\n    elsif char == ','\n   \
        \   groups.push(cur)\n      cur = Set.new([\"\"])\n    elsif char == '}'\n \
        \     groups.push(cur)\n      combined_union = Set.new\n      groups.each {\
        \ |g| combined_union |= g }\n\n      prev_cur = stack_cur.pop\n      prev_groups\
        \ = stack_groups.pop\n\n      next_cur = Set.new\n      prev_cur.each do |s1|\n\
        \        combined_union.each do |s2|\n          next_cur.add(s1 + s2)\n    \
        \    end\n      end\n      cur = next_cur\n      groups = prev_groups\n    else\n\
        \      next_cur = Set.new\n      cur.each { |s| next_cur.add(s + char) }\n \
        \     cur = next_cur\n    end\n  end\n\n  groups.push(cur)\n  final_set = Set.new\n\
        \  groups.each { |g| final_set |= g }\n  final_set.to_a.sort\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def braceExpansionII(expression:\
        \ String): List[String] = {\n        val stackGroups = mutable.Stack[mutable.ListBuffer[mutable.Set[String]]]()\n\
        \        val stackCur = mutable.Stack[mutable.Set[String]]()\n        var groups\
        \ = mutable.ListBuffer[mutable.Set[String]]()\n        var cur = mutable.Set(\"\
        \")\n\n        for (char <- expression) {\n            char match {\n      \
        \          case '{' =>\n                    stackGroups.push(groups)\n     \
        \               stackCur.push(cur)\n                    groups = mutable.ListBuffer[mutable.Set[String]]()\n\
        \                    cur = mutable.Set(\"\")\n                case ',' =>\n\
        \                    groups += cur\n                    cur = mutable.Set(\"\
        \")\n                case '}' =>\n                    groups += cur\n      \
        \              val combinedUnion = mutable.Set[String]()\n                 \
        \   groups.foreach(combinedUnion ++= _)\n                    val prevCur = stackCur.pop()\n\
        \                    val prevGroups = stackGroups.pop()\n\n                \
        \    val nextCur = mutable.Set[String]()\n                    for (s1 <- prevCur;\
        \ s2 <- combinedUnion) {\n                        nextCur += (s1 + s2)\n   \
        \                 }\n                    cur = nextCur\n                   \
        \ groups = prevGroups\n                case _ =>\n                    val nextCur\
        \ = mutable.Set[String]()\n                    for (s <- cur) nextCur += (s\
        \ + char)\n                    cur = nextCur\n            }\n        }\n\n \
        \       groups += cur\n        val finalSet = mutable.Set[String]()\n      \
        \  groups.foreach(finalSet ++= _)\n        finalSet.toList.sorted\n    }\n}"
      rust: "use std::collections::BTreeSet;\n\nimpl Solution {\n    pub fn brace_expansion_ii(expression:\
        \ String) -> Vec<String> {\n        let res = Self::solve(&expression);\n  \
        \      res.into_iter().collect()\n    }\n\n    fn solve(s: &str) -> BTreeSet<String>\
        \ {\n        if s.is_empty() {\n            let mut set = BTreeSet::new();\n\
        \            set.insert(\"\".to_string());\n            return set;\n      \
        \  }\n\n        let mut commas = Vec::new();\n        let mut balance = 0;\n\
        \        let bytes = s.as_bytes();\n        for (i, &b) in bytes.iter().enumerate()\
        \ {\n            match b {\n                b'{' => balance += 1,\n        \
        \        b'}' => balance -= 1,\n                b',' if balance == 0 => commas.push(i),\n\
        \                _ => {}\n            }\n        }\n\n        if !commas.is_empty()\
        \ {\n            let mut res = BTreeSet::new();\n            let mut last =\
        \ 0;\n            for &i in &commas {\n                res.extend(Self::solve(&s[last..i]));\n\
        \                last = i + 1;\n            }\n            res.extend(Self::solve(&s[last..]));\n\
        \            return res;\n        }\n\n        if bytes[0] == b'{' {\n     \
        \       let mut balance = 0;\n            let mut match_idx = 0;\n         \
        \   for (i, &b) in bytes.iter().enumerate() {\n                if b == b'{'\
        \ { balance += 1; }\n                else if b == b'}' { balance -= 1; }\n \
        \               if balance == 0 {\n                    match_idx = i;\n    \
        \                break;\n                }\n            }\n            let first_unit\
        \ = Self::solve(&s[1..match_idx]);\n            let rest = Self::solve(&s[match_idx\
        \ + 1..]);\n            let mut res = BTreeSet::new();\n            for a in\
        \ &first_unit {\n                for b in &rest {\n                    res.insert(format!(\"\
        {}{}\", a, b));\n                }\n            }\n            res\n       \
        \ } else {\n            let mut i = 0;\n            while i < s.len() && bytes[i].is_ascii_lowercase()\
        \ {\n                i += 1;\n            }\n            let first_unit_str\
        \ = &s[..i];\n            let rest = Self::solve(&s[i..]);\n            let\
        \ mut res = BTreeSet::new();\n            for b in &rest {\n               \
        \ res.insert(format!(\"{}{}\", first_unit_str, b));\n            }\n       \
        \     res\n        }\n    }\n}"
      racket: "(require racket/set racket/list)\n\n(define/contract (brace-expansion-ii\
        \ expression)\n  (-> string? (listof string?))\n  (let ([res (solve expression)])\n\
        \    (sort (remove-duplicates res) string<?)))\n\n(define (solve s)\n  (if (string=?\
        \ s \"\")\n      '(\"\")\n      (let ([commas (find-top-level-commas s)])\n\
        \        (if (not (null? commas))\n            (remove-duplicates\n        \
        \     (append-map solve (split-by-indices s commas)))\n            (if (char=?\
        \ (string-ref s 0) #\\{)\n                (let* ([idx (find-matching-brace s)]\n\
        \                       [first-unit (solve (substring s 1 idx))]\n         \
        \              [rest (solve (substring s (+ idx 1)))])\n                  (cartesian-product-lists\
        \ first-unit rest))\n                (let* ([idx (find-first-non-letter s)]\n\
        \                       [first-unit-str (substring s 0 idx)]\n             \
        \          [rest (solve (substring s idx))])\n                  (cartesian-product-lists\
        \ (list first-unit-str) rest)))))))\n\n(define (find-top-level-commas s)\n \
        \ (let loop ([i 0] [balance 0] [acc '()])\n    (if (= i (string-length s))\n\
        \        (reverse acc)\n        (let ([c (string-ref s i)])\n          (cond\n\
        \            [(char=? c #\\{) (loop (+ i 1) (+ balance 1) acc)]\n          \
        \  [(char=? c #\\}) (loop (+ i 1) (- balance 1) acc)]\n            [(and (char=?\
        \ c #\\,) (= balance 0)) (loop (+ i 1) balance (cons i acc))]\n            [else\
        \ (loop (+ i 1) balance acc)])))))\n\n(define (split-by-indices s indices)\n\
        \  (let loop ([last 0] [idx-list indices] [acc '()])\n    (if (null? idx-list)\n\
        \        (reverse (cons (substring s last) acc))\n        (loop (+ (car idx-list)\
        \ 1) (cdr idx-list) (cons (substring s last (car idx-list)) acc)))))\n\n(define\
        \ (find-matching-brace s)\n  (let loop ([i 0] [balance 0])\n    (let ([c (string-ref\
        \ s i)])\n      (cond\n        [(char=? c #\\{) (loop (+ i 1) (+ balance 1))]\n\
        \        [(char=? c #\\}) (let ([new-bal (- balance 1)])\n                 \
        \        (if (= new-bal 0) i (loop (+ i 1) new-bal)))]\n        [else (loop\
        \ (+ i 1) balance)]))))\n\n(define (find-first-non-letter s)\n  (let loop ([i\
        \ 0])\n    (if (or (= i (string-length s)) (not (char-lower-case? (string-ref\
        \ s i))))\n        i\n        (loop (+ i 1)))))\n\n(define (cartesian-product-lists\
        \ list1 list2)\n  (remove-duplicates\n   (for*/list ([a list1] [b list2])\n\
        \     (string-append a b))))"
      erlang: "-spec brace_expansion_ii(Expression :: unicode:unicode_binary()) -> [unicode:unicode_binary()].\n\
        brace_expansion_ii(Expression) ->\n    Set = solve(Expression),\n    SortedList\
        \ = lists:sort(sets:to_list(Set)),\n    SortedList.\n\nsolve(<<>>) ->\n    sets:from_list([<<>>]);\n\
        solve(S) ->\n    Commas = find_top_level_commas(S, 0, 0, []),\n    case Commas\
        \ of\n        [_|_] ->\n            Parts = split_by_indices(S, Commas, 0, []),\n\
        \            lists:foldl(fun(P, Acc) -> sets:union(Acc, solve(P)) end, sets:new(),\
        \ Parts);\n        [] ->\n            case binary:at(S, 0) of\n            \
        \    ${ ->\n                    Idx = find_matching_brace(S, 0, 0),\n      \
        \              FirstUnit = solve(binary:part(S, 1, Idx - 1)),\n            \
        \        Rest = solve(binary:part(S, Idx + 1, byte_size(S) - (Idx + 1))),\n\
        \                    cartesian_product(FirstUnit, Rest);\n                _\
        \ ->\n                    Idx = find_first_non_letter(S, 0),\n             \
        \       FirstUnitStr = binary:part(S, 0, Idx),\n                    Rest = solve(binary:part(S,\
        \ Idx, byte_size(S) - Idx)),\n                    cartesian_product(sets:from_list([FirstUnitStr]),\
        \ Rest)\n            end\n    end.\n\nfind_top_level_commas(S, I, Balance, Acc)\
        \ when I == byte_size(S) ->\n    lists:reverse(Acc);\nfind_top_level_commas(S,\
        \ I, Balance, Acc) ->\n    case binary:at(S, I) of\n        ${ -> find_top_level_commas(S,\
        \ I + 1, Balance + 1, Acc);\n        $} -> find_top_level_commas(S, I + 1, Balance\
        \ - 1, Acc);\n        $, when Balance == 0 -> find_top_level_commas(S, I + 1,\
        \ Balance, [I | Acc]);\n        _ -> find_top_level_commas(S, I + 1, Balance,\
        \ Acc)\n    end.\n\nsplit_by_indices(S, [], Last, Acc) ->\n    lists:reverse([binary:part(S,\
        \ Last, byte_size(S) - Last) | Acc]);\nsplit_by_indices(S, [I | T], Last, Acc)\
        \ ->\n    split_by_indices(S, T, I + 1, [binary:part(S, Last, I - Last) | Acc]).\n\
        \nfind_matching_brace(S, I, Balance) ->\n    case binary:at(S, I) of\n     \
        \   ${ -> find_matching_brace(S, I + 1, Balance + 1);\n        $} -> \n    \
        \        if Balance == 1 -> I;\n               true -> find_matching_brace(S,\
        \ I + 1, Balance - 1)\n            end;\n        _ -> find_matching_brace(S,\
        \ I + 1, Balance)\n    end.\n\nfind_first_non_letter(S, I) when I == byte_size(S)\
        \ -> I;\nfind_first_non_letter(S, I) ->\n    C = binary:at(S, I),\n    if C\
        \ >= $a, C =< $z -> find_first_non_letter(S, I + 1);\n       true -> I\n   \
        \ end.\n\ncartesian_product(Set1, Set2) ->\n    List1 = sets:to_list(Set1),\n\
        \    List2 = sets:to_list(Set2),\n    sets:from_list([<<A/binary, B/binary>>\
        \ || A <- List1, B <- List2])."
      elixir: "defmodule Solution do\n  @spec brace_expansion_ii(expression :: String.t)\
        \ :: [String.t]\n  def brace_expansion_ii(expression) do\n    solve(expression)\n\
        \    |> MapSet.to_list()\n    |> Enum.sort()\n  end\n\n  defp solve(\"\") do\n\
        \    MapSet.new([\"\"])\n  end\n\n  defp solve(s) do\n    commas = find_top_level_commas(s)\n\
        \    if length(commas) > 0 do\n      split_by_indices(s, commas)\n      |> Enum.reduce(MapSet.new(),\
        \ fn p, acc -> MapSet.union(acc, solve(p)) end)\n    else\n      if String.at(s,\
        \ 0) == \"{\" do\n        idx = find_matching_brace(s)\n        first_unit =\
        \ solve(String.slice(s, 1, idx - 1))\n        rest = solve(String.slice(s, idx\
        \ + 1, String.length(s) - idx - 1))\n        cartesian_product(first_unit, rest)\n\
        \      else\n        idx = find_first_non_letter(s)\n        first_unit_str\
        \ = String.slice(s, 0, idx)\n        rest = solve(String.slice(s, idx, String.length(s)\
        \ - idx))\n        cartesian_product(MapSet.new([first_unit_str]), rest)\n \
        \     end\n    end\n  end\n\n  defp find_top_level_commas(s) do\n    s\n   \
        \ |> String.graphemes()\n    |> Enum.with_index()\n    |> Enum.reduce({0, []},\
        \ fn {char, i}, {balance, acc} ->\n      case char do\n        \"{\" -> {balance\
        \ + 1, acc}\n        \"}\" -> {balance - 1, acc}\n        \",\" when balance\
        \ == 0 -> {balance, [i | acc]}\n        _ -> {balance, acc}\n      end\n   \
        \ end)\n    |> elem(1)\n    |> Enum.reverse()\n  end\n\n  defp split_by_indices(s,\
        \ indices) do\n    {last, parts} = Enum.reduce(indices, {0, []}, fn i, {last,\
        \ acc} ->\n      {i + 1, [String.slice(s, last, i - last) | acc]}\n    end)\n\
        \    Enum.reverse([String.slice(s, last, String.length(s) - last) | parts])\n\
        \  end\n\n  defp find_matching_brace(s) do\n    s\n    |> String.graphemes()\n\
        \    |> Enum.with_index()\n    |> Enum.reduce_while(0, fn {char, i}, balance\
        \ ->\n      case char do\n        \"{\" -> {:cont, balance + 1}\n        \"\
        }\" ->\n          new_balance = balance - 1\n          if new_balance == 0,\
        \ do: {:halt, i}, else: {:cont, new_balance}\n        _ -> {:cont, balance}\n\
        \      end\n    end)\n  end\n\n  defp find_first_non_letter(s) do\n    idx =\
        \ Enum.find_index(String.graphemes(s), fn char ->\n      not (char >= \"a\"\
        \ and char <= \"z\")\n    end)\n    idx || String.length(s)\n  end\n\n  defp\
        \ cartesian_product(set1, set2) do\n    for a <- set1, b <- set2, into: MapSet.new(),\
        \ do: a <> b\n  end\nend"
    approach: 'The problem can be solved using a recursive descent parser to handle
      the hierarchical structure of the grammar. We define three levels of precedence:
      ''Expression'' which handles the union of sets (separated by commas), ''Term''
      which handles the Cartesian product (concatenation) of adjacent factors, and ''Factor''
      which handles either a nested expression within braces or a literal lowercase
      string. This structure ensures that concatenation is prioritized over union, correctly
      reflecting the grammar rules where ''{a,b}{c,d}'' is a product of two unions.'
    time_complexity: O(N * M * L) where N is the length of the expression, M is the
      total number of words generated, and L is the average length of the strings. Since
      the input length is capped at 60, the branching factor and string concatenations
      are bounded, though the number of generated strings can still grow significantly
      within those bounds.
    space_complexity: O(M * L) to store the intermediate and final sets of strings.
      The recursion depth is proportional to the nesting level of the braces, which
      is at most O(N).
    elapsed_time: 640.4127376079559
    model: gemini-3-flash-preview
    generated_at: '2026-09-25 02:58:01 '
---

## Problem #1096: Brace Expansion II

**Difficulty:** Hard

**Topics:** Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting

## Problem Description

<p>Under the grammar given below, strings can represent a set of lowercase words. Let&nbsp;<code>R(expr)</code>&nbsp;denote the set of words the expression represents.</p>

<p>The grammar can best be understood through simple examples:</p>

<ul>
	<li>Single letters represent a singleton set containing that word.
	<ul>
		<li><code>R(&quot;a&quot;) = {&quot;a&quot;}</code></li>
		<li><code>R(&quot;w&quot;) = {&quot;w&quot;}</code></li>
	</ul>
	</li>
	<li>When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
	<ul>
		<li><code>R(&quot;{a,b,c}&quot;) = {&quot;a&quot;,&quot;b&quot;,&quot;c&quot;}</code></li>
		<li><code>R(&quot;{{a,b},{b,c}}&quot;) = {&quot;a&quot;,&quot;b&quot;,&quot;c&quot;}</code> (notice the final set only contains each word at most once)</li>
	</ul>
	</li>
	<li>When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
	<ul>
		<li><code>R(&quot;{a,b}{c,d}&quot;) = {&quot;ac&quot;,&quot;ad&quot;,&quot;bc&quot;,&quot;bd&quot;}</code></li>
		<li><code>R(&quot;a{b,c}{d,e}f{g,h}&quot;) = {&quot;abdfg&quot;, &quot;abdfh&quot;, &quot;abefg&quot;, &quot;abefh&quot;, &quot;acdfg&quot;, &quot;acdfh&quot;, &quot;acefg&quot;, &quot;acefh&quot;}</code></li>
	</ul>
	</li>
</ul>

<p>Formally, the three rules for our grammar:</p>

<ul>
	<li>For every lowercase letter <code>x</code>, we have <code>R(x) = {x}</code>.</li>
	<li>For expressions <code>e<sub>1</sub>, e<sub>2</sub>, ... , e<sub>k</sub></code> with <code>k &gt;= 2</code>, we have <code>R({e<sub>1</sub>, e<sub>2</sub>, ...}) = R(e<sub>1</sub>) &cup; R(e<sub>2</sub>) &cup; ...</code></li>
	<li>For expressions <code>e<sub>1</sub></code> and <code>e<sub>2</sub></code>, we have <code>R(e<sub>1</sub> + e<sub>2</sub>) = {a + b for (a, b) in R(e<sub>1</sub>) &times; R(e<sub>2</sub>)}</code>, where <code>+</code> denotes concatenation, and <code>&times;</code> denotes the cartesian product.</li>
</ul>

<p>Given an expression representing a set of words under the given grammar, return <em>the sorted list of words that the expression represents</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;{a,b}{c,{d,e}}&quot;
<strong>Output:</strong> [&quot;ac&quot;,&quot;ad&quot;,&quot;ae&quot;,&quot;bc&quot;,&quot;bd&quot;,&quot;be&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;{{a,z},a{b,c},{ab,z}}&quot;
<strong>Output:</strong> [&quot;a&quot;,&quot;ab&quot;,&quot;ac&quot;,&quot;z&quot;]
<strong>Explanation:</strong> Each distinct word is written only once in the final answer.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 60</code></li>
	<li><code>expression[i]</code> consists of <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;,&#39;</code>or lowercase English letters.</li>
	<li>The given&nbsp;<code>expression</code>&nbsp;represents a set of words based on the grammar given in the description.</li>
</ul>


## Hints

1. You can write helper methods to parse the next "chunk" of the expression.  If you see eg. "a", the answer is just the set {a}.  If you see "{", you parse until you complete the "}" (the number of { and } seen are equal) and that becomes a chunk that you find where the appropriate commas are, and parse each individual expression between the commas.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved using a recursive descent parser to handle the hierarchical structure of the grammar. We define three levels of precedence: 'Expression' which handles the union of sets (separated by commas), 'Term' which handles the Cartesian product (concatenation) of adjacent factors, and 'Factor' which handles either a nested expression within braces or a literal lowercase string. This structure ensures that concatenation is prioritized over union, correctly reflecting the grammar rules where '{a,b}{c,d}' is a product of two unions.

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
    vector<string> braceExpansionII(string expression) {
        int i = 0;
        set<string> result = parseExpression(expression, i);
        return vector<string>(result.begin(), result.end());
    }

private:
    set<string> parseExpression(const string& s, int& i) {
        set<string> res;
        while (true) {
            set<string> term = parseTerm(s, i);
            res.insert(term.begin(), term.end());
            if (i < s.length() && s[i] == ',') {
                i++;
            } else {
                break;
            }
        }
        return res;
    }

    set<string> parseTerm(const string& s, int& i) {
        set<string> res = {""};
        while (i < s.length() && s[i] != ',' && s[i] != '}') {
            set<string> next = parseFactor(s, i);
            set<string> combined;
            for (const string& a : res) {
                for (const string& b : next) {
                    combined.insert(a + b);
                }
            }
            res = std::move(combined);
        }
        return res;
    }

    set<string> parseFactor(const string& s, int& i) {
        if (s[i] == '{') {
            i++;
            set<string> res = parseExpression(s, i);
            i++; // skip '}'
            return res;
        } else {
            int start = i;
            while (i < s.length() && islower(s[i])) {
                i++;
            }
            return {s.substr(start, i - start)};
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
    private int i = 0;

    public List<String> braceExpansionII(String expression) {
        TreeSet<String> resultSet = parseExpression(expression);
        return new ArrayList<>(resultSet);
    }

    private TreeSet<String> parseExpression(String s) {
        TreeSet<String> res = new TreeSet<>();
        while (true) {
            TreeSet<String> term = parseTerm(s);
            res.addAll(term);
            if (i < s.length() && s.charAt(i) == ',') {
                i++;
            } else {
                break;
            }
        }
        return res;
    }

    private TreeSet<String> parseTerm(String s) {
        TreeSet<String> res = new TreeSet<>();
        res.add("");
        while (i < s.length() && s.charAt(i) != ',' && s.charAt(i) != '}') {
            TreeSet<String> next = parseFactor(s);
            TreeSet<String> combined = new TreeSet<>();
            for (String a : res) {
                for (String b : next) {
                    combined.add(a + b);
                }
            }
            res = combined;
        }
        return res;
    }

    private TreeSet<String> parseFactor(String s) {
        if (s.charAt(i) == '{') {
            i++;
            TreeSet<String> res = parseExpression(s);
            i++;
            return res;
        } else {
            int start = i;
            while (i < s.length() && Character.isLowerCase(s.charAt(i))) {
                i++;
            }
            TreeSet<String> res = new TreeSet<>();
            res.add(s.substring(start, i));
            return res;
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
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        self.i = 0
        self.s = expression

        def parseExpression():
            res = set()
            while True:
                term = parseTerm()
                res.update(term)
                if self.i < len(self.s) and self.s[self.i] == ',':
                    self.i += 1
                else:
                    break
            return res

        def parseTerm():
            res = {""}
            while self.i < len(self.s) and self.s[self.i] not in (',', '}'):
                next_set = parseFactor()
                new_res = set()
                for a in res:
                    for b in next_set:
                        new_res.add(a + b)
                res = new_res
            return res

        def parseFactor():
            if self.s[self.i] == '{':
                self.i += 1
                res = parseExpression()
                self.i += 1
                return res
            else:
                start = self.i
                while self.i < len(self.s) and 'a' <= self.s[self.i] <= 'z':
                    self.i += 1
                return {self.s[start:self.i]}

        final_set = parseExpression()
        return sorted(list(final_set))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = [[set([""])]]
        for char in expression:
            if char == '{':
                stack.append([set([""])])
            elif char == '}':
                union_res = set().union(*stack.pop())
                prev_union = stack[-1]
                last_set = prev_union[-1]
                prev_union[-1] = {s1 + s2 for s1 in last_set for s2 in union_res}
            elif char == ',':
                stack[-1].append(set([""]))
            else:
                current_union = stack[-1]
                last_set = current_union[-1]
                current_union[-1] = {s + char for s in last_set}

        final_union = set().union(*stack[0])
        return sorted(list(final_union))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    char** words;
    int size;
    int cap;
} Set;

char* my_strdup(const char* s) {
    char* d = malloc(strlen(s) + 1);
    if (d) strcpy(d, s);
    return d;
}

int compare_strings(const void* a, const void* b) {
    return strcmp(*(const char**)a, *(const char**)b);
}

void sort_and_unique(Set* s) {
    if (s->size <= 1) return;
    qsort(s->words, s->size, sizeof(char*), compare_strings);
    int j = 0;
    for (int i = 1; i < s->size; i++) {
        if (strcmp(s->words[j], s->words[i]) != 0) {
            s->words[++j] = s->words[i];
        } else {
            free(s->words[i]);
        }
    }
    s->size = j + 1;
}

Set create_empty_set() {
    Set s = {NULL, 0, 0};
    return s;
}

Set singleton_set(const char* word) {
    Set s;
    s.size = 1;
    s.cap = 1;
    s.words = malloc(sizeof(char*));
    s.words[0] = my_strdup(word);
    return s;
}

void free_set(Set s) {
    for (int i = 0; i < s.size; i++) free(s.words[i]);
    if (s.words) free(s.words);
}

Set union_sets(Set s1, Set s2) {
    Set res;
    res.size = 0;
    res.cap = s1.size + s2.size;
    if (res.cap == 0) {
        if (s1.words) free(s1.words);
        if (s2.words) free(s2.words);
        return create_empty_set();
    }
    res.words = malloc(res.cap * sizeof(char*));
    for (int i = 0; i < s1.size; i++) res.words[res.size++] = s1.words[i];
    for (int i = 0; i < s2.size; i++) res.words[res.size++] = s2.words[i];
    if (s1.words) free(s1.words);
    if (s2.words) free(s2.words);
    sort_and_unique(&res);
    return res;
}

Set multiply(Set s1, Set s2) {
    if (s1.size == 0 || s2.size == 0) {
        free_set(s1); free_set(s2);
        return create_empty_set();
    }
    Set res;
    res.size = 0;
    res.cap = s1.size * s2.size;
    res.words = malloc(res.cap * sizeof(char*));
    for (int i = 0; i < s1.size; i++) {
        for (int j = 0; j < s2.size; j++) {
            char* s = malloc(strlen(s1.words[i]) + strlen(s2.words[j]) + 1);
            strcpy(s, s1.words[i]);
            strcat(s, s2.words[j]);
            res.words[res.size++] = s;
        }
    }
    free_set(s1); free_set(s2);
    sort_and_unique(&res);
    return res;
}

Set parse_union(char* expr, int* p);

Set parse_concatenation(char* expr, int* p) {
    Set res = singleton_set("");
    while (expr[*p] != '\0' && expr[*p] != ',' && expr[*p] != '}') {
        Set factor;
        if (expr[*p] == '{') {
            (*p)++;
            factor = parse_union(expr, p);
            if (expr[*p] == '}') (*p)++;
        } else {
            char word[2] = {expr[(*p)++], '\0'};
            factor = singleton_set(word);
        }
        res = multiply(res, factor);
    }
    return res;
}

Set parse_union(char* expr, int* p) {
    Set res = create_empty_set();
    while (1) {
        Set term = parse_concatenation(expr, p);
        res = union_sets(res, term);
        if (expr[*p] == ',') (*p)++;
        else break;
    }
    return res;
}

char** braceExpansionII(char* expression, int* returnSize) {
    int p = 0;
    Set res = parse_union(expression, &p);
    *returnSize = res.size;
    return res.words;
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
    public IList<string> BraceExpansionII(string expression) {
        var stack = new Stack<List<HashSet<string>>>();
        stack.Push(new List<HashSet<string>> { new HashSet<string> { "" } });

        for (int i = 0; i < expression.Length; i++) {
            char c = expression[i];
            if (c == '{') {
                stack.Push(new List<HashSet<string>> { new HashSet<string> { "" } });
            } else if (c == '}') {
                var currentUnionList = stack.Pop();
                var unionResult = new HashSet<string>();
                foreach (var sSet in currentUnionList) {
                    foreach (var s in sSet) unionResult.Add(s);
                }

                var parentUnionList = stack.Peek();
                var lastParentSet = parentUnionList[parentUnionList.Count - 1];
                var multipliedSet = new HashSet<string>();
                foreach (var s1 in lastParentSet) {
                    foreach (var s2 in unionResult) {
                        multipliedSet.Add(s1 + s2);
                    }
                }
                parentUnionList[parentUnionList.Count - 1] = multipliedSet;
            } else if (c == ',') {
                stack.Peek().Add(new HashSet<string> { "" });
            } else {
                var currentUnionList = stack.Peek();
                var lastSet = currentUnionList[currentUnionList.Count - 1];
                var nextSet = new HashSet<string>();
                foreach (var s in lastSet) {
                    nextSet.Add(s + c);
                }
                currentUnionList[currentUnionList.Count - 1] = nextSet;
            }
        }

        var finalResultSet = new HashSet<string>();
        foreach (var sSet in stack.Peek()) {
            foreach (var s in sSet) finalResultSet.Add(s);
        }

        var resultList = new List<string>(finalResultSet);
        resultList.Sort(StringComparer.Ordinal);
        return resultList;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} expression
 * @return {string[]}
 */
var braceExpansionII = function(expression) {
    let stack = [[new Set([""])]];

    for (let i = 0; i < expression.length; i++) {
        let char = expression[i];
        if (char === '{') {
            stack.push([new Set([""])]);
        } else if (char === '}') {
            let currentUnion = stack.pop();
            let unionRes = new Set();
            for (let sSet of currentUnion) {
                for (let s of sSet) unionRes.add(s);
            }
            let prevUnion = stack[stack.length - 1];
            let lastSet = prevUnion[prevUnion.length - 1];
            let nextSet = new Set();
            for (let s1 of lastSet) {
                for (let s2 of unionRes) {
                    nextSet.add(s1 + s2);
                }
            }
            prevUnion[prevUnion.length - 1] = nextSet;
        } else if (char === ',') {
            stack[stack.length - 1].push(new Set([""]));
        } else {
            let currentUnion = stack[stack.length - 1];
            let lastSet = currentUnion[currentUnion.length - 1];
            let nextSet = new Set();
            for (let s of lastSet) {
                nextSet.add(s + char);
            }
            currentUnion[currentUnion.length - 1] = nextSet;
        }
    }

    let finalSet = new Set();
    for (let sSet of stack[0]) {
        for (let s of sSet) finalSet.add(s);
    }

    return Array.from(finalSet).sort();
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function braceExpansionII(expression: string): string[] {
    function evaluate(expr: string): Set<string> {
        if (expr === "") return new Set([""]);

        let braceCount = 0;
        let commaIndices: number[] = [];
        for (let i = 0; i < expr.length; i++) {
            if (expr[i] === "{") braceCount++;
            else if (expr[i] === "}") braceCount--;
            else if (expr[i] === "," && braceCount === 0) {
                commaIndices.push(i);
            }
        }

        if (commaIndices.length > 0) {
            let res = new Set<string>();
            let start = 0;
            for (let idx of commaIndices) {
                let subRes = evaluate(expr.substring(start, idx));
                for (const s of subRes) res.add(s);
                start = idx + 1;
            }
            let subRes = evaluate(expr.substring(start));
            for (const s of subRes) res.add(s);
            return res;
        }

        let firstUnit: Set<string>;
        let rest: string;

        if (expr[0] === "{") {
            let bc = 0;
            let j = 0;
            for (let i = 0; i < expr.length; i++) {
                if (expr[i] === "{") bc++;
                else if (expr[i] === "}") {
                    bc--;
                    if (bc === 0) {
                        j = i;
                        break;
                    }
                }
            }
            firstUnit = evaluate(expr.substring(1, j));
            rest = expr.substring(j + 1);
        } else {
            firstUnit = new Set([expr[0]]);
            rest = expr.substring(1);
        }

        if (rest === "") return firstUnit;

        let restSet = evaluate(rest);
        let combined = new Set<string>();
        for (const s1 of firstUnit) {
            for (const s2 of restSet) {
                combined.add(s1 + s2);
            }
        }
        return combined;
    }

    const resultSet = evaluate(expression);
    return Array.from(resultSet).sort();
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $expression
     * @return String[]
     */
    function braceExpansionII($expression) {
        $res = $this->evaluate($expression);
        sort($res);
        return $res;
    }

    private function evaluate($expr) {
        if ($expr === "") return [""];
        $braceCount = 0;
        $commaIndices = [];
        $len = strlen($expr);

        for ($i = 0; $i < $len; $i++) {
            if ($expr[$i] === '{') $braceCount++;
            else if ($expr[$i] === '}') $braceCount--;
            else if ($expr[$i] === ',' && $braceCount === 0) {
                $commaIndices[] = $i;
            }
        }

        if (!empty($commaIndices)) {
            $resSet = [];
            $start = 0;
            foreach ($commaIndices as $idx) {
                $subRes = $this->evaluate(substr($expr, $start, $idx - $start));
                foreach ($subRes as $s) $resSet[$s] = true;
                $start = $idx + 1;
            }
            $subRes = $this->evaluate(substr($expr, $start));
            foreach ($subRes as $s) $resSet[$s] = true;
            return array_keys($resSet);
        }

        if ($expr[0] === '{') {
            $bc = 0;
            $j = 0;
            for ($i = 0; $i < $len; $i++) {
                if ($expr[$i] === '{') $bc++;
                else if ($expr[$i] === '}') {
                    $bc--;
                    if ($bc === 0) {
                        $j = $i;
                        break;
                    }
                }
            }
            $firstUnit = $this->evaluate(substr($expr, 1, $j - 1));
            $rest = substr($expr, $j + 1);
            if ($rest === false) $rest = "";
        } else {
            $firstUnit = [$expr[0]];
            $rest = substr($expr, 1);
            if ($rest === false) $rest = "";
        }

        if ($rest === "") return $firstUnit;

        $restSet = $this->evaluate($rest);
        $combinedSet = [];
        foreach ($firstUnit as $s1) {
            foreach ($restSet as $s2) {
                $combinedSet[$s1 . $s2] = true;
            }
        }
        return array_keys($combinedSet);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func braceExpansionII(_ expression: String) -> [String] {
        func evaluate(_ expr: String) -> Set<String> {
            if expr.isEmpty { return [""] }
            let chars = Array(expr)
            var braceCount = 0
            var commaIndices = [Int]()

            for i in 0..<chars.count {
                if chars[i] == "{" { braceCount += 1 }
                else if chars[i] == "}" { braceCount -= 1 }
                else if chars[i] == "," && braceCount == 0 {
                    commaIndices.append(i)
                }
            }

            if !commaIndices.isEmpty {
                var res = Set<String>()
                var start = 0
                for idx in commaIndices {
                    res.formUnion(evaluate(String(chars[start..<idx])))
                    start = idx + 1
                }
                res.formUnion(evaluate(String(chars[start...])))
                return res
            }

            var firstUnit: Set<String>
            var rest: String

            if chars[0] == "{" {
                var bc = 0
                var j = 0
                for i in 0..<chars.count {
                    if chars[i] == "{" { bc += 1 }
                    else if chars[i] == "}" {
                        bc -= 1
                        if bc == 0 {
                            j = i
                            break
                        }
                    }
                }
                firstUnit = evaluate(String(chars[1..<j]))
                rest = String(chars[(j + 1)...])
            } else {
                firstUnit = [String(chars[0])]
                rest = String(chars[1...])
            }

            if rest.isEmpty { return firstUnit }

            let restSet = evaluate(rest)
            var combined = Set<String>()
            for s1 in firstUnit {
                for s2 in restSet {
                    combined.insert(s1 + s2)
                }
            }
            return combined
        }

        let resultSet = evaluate(expression)
        return Array(resultSet).sorted()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun braceExpansionII(expression: String): List<String> {
        fun evaluate(expr: String): Set<String> {
            if (expr.isEmpty()) return setOf("")

            var braceCount = 0
            val commaIndices = mutableListOf<Int>()
            for (i in expr.indices) {
                if (expr[i] == '{') braceCount++
                else if (expr[i] == '}') braceCount--
                else if (expr[i] == ',' && braceCount == 0) {
                    commaIndices.add(i)
                }
            }

            if (commaIndices.isNotEmpty()) {
                val res = mutableSetOf<String>()
                var start = 0
                for (idx in commaIndices) {
                    res.addAll(evaluate(expr.substring(start, idx)))
                    start = idx + 1
                }
                res.addAll(evaluate(expr.substring(start)))
                return res
            }

            val firstUnit: Set<String>
            val rest: String
            if (expr[0] == '{') {
                var bc = 0
                var j = 0
                for (i in expr.indices) {
                    if (expr[i] == '{') bc++
                    else if (expr[i] == '}') {
                        bc--
                        if (bc == 0) {
                            j = i
                            break
                        }
                    }
                }
                firstUnit = evaluate(expr.substring(1, j))
                rest = expr.substring(j + 1)
            } else {
                firstUnit = setOf(expr[0].toString())
                rest = expr.substring(1)
            }

            if (rest.isEmpty()) return firstUnit

            val restSet = evaluate(rest)
            val combined = mutableSetOf<String>()
            for (s1 in firstUnit) {
                for (s2 in restSet) {
                    combined.add(s1 + s2)
                }
            }
            return combined
        }

        return evaluate(expression).toList().sorted()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<String> braceExpansionII(String expression) {
    List<List<Set<String>>> stackGroups = [];
    List<Set<String>> stackCur = [];
    List<Set<String>> groups = [];
    Set<String> cur = {""};

    for (int i = 0; i < expression.length; i++) {
      String char = expression[i];
      if (char == '{') {
        stackGroups.add(groups);
        stackCur.add(cur);
        groups = [];
        cur = {""};
      } else if (char == ',') {
        groups.add(cur);
        cur = {""};
      } else if (char == '}') {
        groups.add(cur);
        Set<String> combinedUnion = {};
        for (var g in groups) {
          combinedUnion.addAll(g);
        }

        Set<String> prevCur = stackCur.removeLast();
        List<Set<String>> prevGroups = stackGroups.removeLast();

        Set<String> nextCur = {};
        for (var s1 in prevCur) {
          for (var s2 in combinedUnion) {
            nextCur.add(s1 + s2);
          }
        }
        cur = nextCur;
        groups = prevGroups;
      } else {
        Set<String> nextCur = {};
        for (var s in cur) {
          nextCur.add(s + char);
        }
        cur = nextCur;
      }
    }

    groups.add(cur);
    Set<String> finalSet = {};
    for (var g in groups) {
      finalSet.addAll(g);
    }

    List<String> res = finalSet.toList();
    res.sort();
    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func braceExpansionII(expression string) []string {
    type Set map[string]struct{}
    stackGroups := [][]Set{}
    stackCur := []Set{}
    groups := []Set{}
    cur := make(Set)
    cur[""] = struct{}{}

    for i := 0; i < len(expression); i++ {
        char := expression[i]
        if char == '{' {
            stackGroups = append(stackGroups, groups)
            stackCur = append(stackCur, cur)
            groups = []Set{}
            cur = make(Set)
            cur[""] = struct{}{}
        } else if char == ',' {
            groups = append(groups, cur)
            cur = make(Set)
            cur[""] = struct{}{}
        } else if char == '}' {
            groups = append(groups, cur)
            combinedUnion := make(Set)
            for _, g := range groups {
                for s := range g {
                    combinedUnion[s] = struct{}{}
                }
            }

            prevCur := stackCur[len(stackCur)-1]
            stackCur = stackCur[:len(stackCur)-1]
            prevGroups := stackGroups[len(stackGroups)-1]
            stackGroups = stackGroups[:len(stackGroups)-1]

            nextCur := make(Set)
            for s1 := range prevCur {
                for s2 := range combinedUnion {
                    nextCur[s1+s2] = struct{}{}
                }
            }
            cur = nextCur
            groups = prevGroups
        } else {
            nextCur := make(Set)
            for s := range cur {
                nextCur[s+string(char)] = struct{}{}
            }
            cur = nextCur
        }
    }

    groups = append(groups, cur)
    finalSet := make(Set)
    for _, g := range groups {
        for s := range g {
            finalSet[s] = struct{}{}
        }
    }

    res := make([]string, 0, len(finalSet))
    for s := range finalSet {
        res = append(res, s)
    }
    sort.Strings(res)
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
require 'set'

def brace_expansion_ii(expression)
  stack_groups = []
  stack_cur = []
  groups = []
  cur = Set.new([""])

  expression.each_char do |char|
    if char == '{'
      stack_groups.push(groups)
      stack_cur.push(cur)
      groups = []
      cur = Set.new([""])
    elsif char == ','
      groups.push(cur)
      cur = Set.new([""])
    elsif char == '}'
      groups.push(cur)
      combined_union = Set.new
      groups.each { |g| combined_union |= g }

      prev_cur = stack_cur.pop
      prev_groups = stack_groups.pop

      next_cur = Set.new
      prev_cur.each do |s1|
        combined_union.each do |s2|
          next_cur.add(s1 + s2)
        end
      end
      cur = next_cur
      groups = prev_groups
    else
      next_cur = Set.new
      cur.each { |s| next_cur.add(s + char) }
      cur = next_cur
    end
  end

  groups.push(cur)
  final_set = Set.new
  groups.each { |g| final_set |= g }
  final_set.to_a.sort
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def braceExpansionII(expression: String): List[String] = {
        val stackGroups = mutable.Stack[mutable.ListBuffer[mutable.Set[String]]]()
        val stackCur = mutable.Stack[mutable.Set[String]]()
        var groups = mutable.ListBuffer[mutable.Set[String]]()
        var cur = mutable.Set("")

        for (char <- expression) {
            char match {
                case '{' =>
                    stackGroups.push(groups)
                    stackCur.push(cur)
                    groups = mutable.ListBuffer[mutable.Set[String]]()
                    cur = mutable.Set("")
                case ',' =>
                    groups += cur
                    cur = mutable.Set("")
                case '}' =>
                    groups += cur
                    val combinedUnion = mutable.Set[String]()
                    groups.foreach(combinedUnion ++= _)
                    val prevCur = stackCur.pop()
                    val prevGroups = stackGroups.pop()

                    val nextCur = mutable.Set[String]()
                    for (s1 <- prevCur; s2 <- combinedUnion) {
                        nextCur += (s1 + s2)
                    }
                    cur = nextCur
                    groups = prevGroups
                case _ =>
                    val nextCur = mutable.Set[String]()
                    for (s <- cur) nextCur += (s + char)
                    cur = nextCur
            }
        }

        groups += cur
        val finalSet = mutable.Set[String]()
        groups.foreach(finalSet ++= _)
        finalSet.toList.sorted
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::BTreeSet;

impl Solution {
    pub fn brace_expansion_ii(expression: String) -> Vec<String> {
        let res = Self::solve(&expression);
        res.into_iter().collect()
    }

    fn solve(s: &str) -> BTreeSet<String> {
        if s.is_empty() {
            let mut set = BTreeSet::new();
            set.insert("".to_string());
            return set;
        }

        let mut commas = Vec::new();
        let mut balance = 0;
        let bytes = s.as_bytes();
        for (i, &b) in bytes.iter().enumerate() {
            match b {
                b'{' => balance += 1,
                b'}' => balance -= 1,
                b',' if balance == 0 => commas.push(i),
                _ => {}
            }
        }

        if !commas.is_empty() {
            let mut res = BTreeSet::new();
            let mut last = 0;
            for &i in &commas {
                res.extend(Self::solve(&s[last..i]));
                last = i + 1;
            }
            res.extend(Self::solve(&s[last..]));
            return res;
        }

        if bytes[0] == b'{' {
            let mut balance = 0;
            let mut match_idx = 0;
            for (i, &b) in bytes.iter().enumerate() {
                if b == b'{' { balance += 1; }
                else if b == b'}' { balance -= 1; }
                if balance == 0 {
                    match_idx = i;
                    break;
                }
            }
            let first_unit = Self::solve(&s[1..match_idx]);
            let rest = Self::solve(&s[match_idx + 1..]);
            let mut res = BTreeSet::new();
            for a in &first_unit {
                for b in &rest {
                    res.insert(format!("{}{}", a, b));
                }
            }
            res
        } else {
            let mut i = 0;
            while i < s.len() && bytes[i].is_ascii_lowercase() {
                i += 1;
            }
            let first_unit_str = &s[..i];
            let rest = Self::solve(&s[i..]);
            let mut res = BTreeSet::new();
            for b in &rest {
                res.insert(format!("{}{}", first_unit_str, b));
            }
            res
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/set racket/list)

(define/contract (brace-expansion-ii expression)
  (-> string? (listof string?))
  (let ([res (solve expression)])
    (sort (remove-duplicates res) string<?)))

(define (solve s)
  (if (string=? s "")
      '("")
      (let ([commas (find-top-level-commas s)])
        (if (not (null? commas))
            (remove-duplicates
             (append-map solve (split-by-indices s commas)))
            (if (char=? (string-ref s 0) #\{)
                (let* ([idx (find-matching-brace s)]
                       [first-unit (solve (substring s 1 idx))]
                       [rest (solve (substring s (+ idx 1)))])
                  (cartesian-product-lists first-unit rest))
                (let* ([idx (find-first-non-letter s)]
                       [first-unit-str (substring s 0 idx)]
                       [rest (solve (substring s idx))])
                  (cartesian-product-lists (list first-unit-str) rest)))))))

(define (find-top-level-commas s)
  (let loop ([i 0] [balance 0] [acc '()])
    (if (= i (string-length s))
        (reverse acc)
        (let ([c (string-ref s i)])
          (cond
            [(char=? c #\{) (loop (+ i 1) (+ balance 1) acc)]
            [(char=? c #\}) (loop (+ i 1) (- balance 1) acc)]
            [(and (char=? c #\,) (= balance 0)) (loop (+ i 1) balance (cons i acc))]
            [else (loop (+ i 1) balance acc)])))))

(define (split-by-indices s indices)
  (let loop ([last 0] [idx-list indices] [acc '()])
    (if (null? idx-list)
        (reverse (cons (substring s last) acc))
        (loop (+ (car idx-list) 1) (cdr idx-list) (cons (substring s last (car idx-list)) acc)))))

(define (find-matching-brace s)
  (let loop ([i 0] [balance 0])
    (let ([c (string-ref s i)])
      (cond
        [(char=? c #\{) (loop (+ i 1) (+ balance 1))]
        [(char=? c #\}) (let ([new-bal (- balance 1)])
                         (if (= new-bal 0) i (loop (+ i 1) new-bal)))]
        [else (loop (+ i 1) balance)]))))

(define (find-first-non-letter s)
  (let loop ([i 0])
    (if (or (= i (string-length s)) (not (char-lower-case? (string-ref s i))))
        i
        (loop (+ i 1)))))

(define (cartesian-product-lists list1 list2)
  (remove-duplicates
   (for*/list ([a list1] [b list2])
     (string-append a b))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec brace_expansion_ii(Expression :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
brace_expansion_ii(Expression) ->
    Set = solve(Expression),
    SortedList = lists:sort(sets:to_list(Set)),
    SortedList.

solve(<<>>) ->
    sets:from_list([<<>>]);
solve(S) ->
    Commas = find_top_level_commas(S, 0, 0, []),
    case Commas of
        [_|_] ->
            Parts = split_by_indices(S, Commas, 0, []),
            lists:foldl(fun(P, Acc) -> sets:union(Acc, solve(P)) end, sets:new(), Parts);
        [] ->
            case binary:at(S, 0) of
                ${ ->
                    Idx = find_matching_brace(S, 0, 0),
                    FirstUnit = solve(binary:part(S, 1, Idx - 1)),
                    Rest = solve(binary:part(S, Idx + 1, byte_size(S) - (Idx + 1))),
                    cartesian_product(FirstUnit, Rest);
                _ ->
                    Idx = find_first_non_letter(S, 0),
                    FirstUnitStr = binary:part(S, 0, Idx),
                    Rest = solve(binary:part(S, Idx, byte_size(S) - Idx)),
                    cartesian_product(sets:from_list([FirstUnitStr]), Rest)
            end
    end.

find_top_level_commas(S, I, Balance, Acc) when I == byte_size(S) ->
    lists:reverse(Acc);
find_top_level_commas(S, I, Balance, Acc) ->
    case binary:at(S, I) of
        ${ -> find_top_level_commas(S, I + 1, Balance + 1, Acc);
        $} -> find_top_level_commas(S, I + 1, Balance - 1, Acc);
        $, when Balance == 0 -> find_top_level_commas(S, I + 1, Balance, [I | Acc]);
        _ -> find_top_level_commas(S, I + 1, Balance, Acc)
    end.

split_by_indices(S, [], Last, Acc) ->
    lists:reverse([binary:part(S, Last, byte_size(S) - Last) | Acc]);
split_by_indices(S, [I | T], Last, Acc) ->
    split_by_indices(S, T, I + 1, [binary:part(S, Last, I - Last) | Acc]).

find_matching_brace(S, I, Balance) ->
    case binary:at(S, I) of
        ${ -> find_matching_brace(S, I + 1, Balance + 1);
        $} -> 
            if Balance == 1 -> I;
               true -> find_matching_brace(S, I + 1, Balance - 1)
            end;
        _ -> find_matching_brace(S, I + 1, Balance)
    end.

find_first_non_letter(S, I) when I == byte_size(S) -> I;
find_first_non_letter(S, I) ->
    C = binary:at(S, I),
    if C >= $a, C =< $z -> find_first_non_letter(S, I + 1);
       true -> I
    end.

cartesian_product(Set1, Set2) ->
    List1 = sets:to_list(Set1),
    List2 = sets:to_list(Set2),
    sets:from_list([<<A/binary, B/binary>> || A <- List1, B <- List2]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec brace_expansion_ii(expression :: String.t) :: [String.t]
  def brace_expansion_ii(expression) do
    solve(expression)
    |> MapSet.to_list()
    |> Enum.sort()
  end

  defp solve("") do
    MapSet.new([""])
  end

  defp solve(s) do
    commas = find_top_level_commas(s)
    if length(commas) > 0 do
      split_by_indices(s, commas)
      |> Enum.reduce(MapSet.new(), fn p, acc -> MapSet.union(acc, solve(p)) end)
    else
      if String.at(s, 0) == "{" do
        idx = find_matching_brace(s)
        first_unit = solve(String.slice(s, 1, idx - 1))
        rest = solve(String.slice(s, idx + 1, String.length(s) - idx - 1))
        cartesian_product(first_unit, rest)
      else
        idx = find_first_non_letter(s)
        first_unit_str = String.slice(s, 0, idx)
        rest = solve(String.slice(s, idx, String.length(s) - idx))
        cartesian_product(MapSet.new([first_unit_str]), rest)
      end
    end
  end

  defp find_top_level_commas(s) do
    s
    |> String.graphemes()
    |> Enum.with_index()
    |> Enum.reduce({0, []}, fn {char, i}, {balance, acc} ->
      case char do
        "{" -> {balance + 1, acc}
        "}" -> {balance - 1, acc}
        "," when balance == 0 -> {balance, [i | acc]}
        _ -> {balance, acc}
      end
    end)
    |> elem(1)
    |> Enum.reverse()
  end

  defp split_by_indices(s, indices) do
    {last, parts} = Enum.reduce(indices, {0, []}, fn i, {last, acc} ->
      {i + 1, [String.slice(s, last, i - last) | acc]}
    end)
    Enum.reverse([String.slice(s, last, String.length(s) - last) | parts])
  end

  defp find_matching_brace(s) do
    s
    |> String.graphemes()
    |> Enum.with_index()
    |> Enum.reduce_while(0, fn {char, i}, balance ->
      case char do
        "{" -> {:cont, balance + 1}
        "}" ->
          new_balance = balance - 1
          if new_balance == 0, do: {:halt, i}, else: {:cont, new_balance}
        _ -> {:cont, balance}
      end
    end)
  end

  defp find_first_non_letter(s) do
    idx = Enum.find_index(String.graphemes(s), fn char ->
      not (char >= "a" and char <= "z")
    end)
    idx || String.length(s)
  end

  defp cartesian_product(set1, set2) do
    for a <- set1, b <- set2, into: MapSet.new(), do: a <> b
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * M * L) where N is the length of the expression, M is the total number of words generated, and L is the average length of the strings. Since the input length is capped at 60, the branching factor and string concatenations are bounded, though the number of generated strings can still grow significantly within those bounds.
- **Space Complexity:** O(M * L) to store the intermediate and final sets of strings. The recursion depth is proportional to the nesting level of the braces, which is at most O(N).
