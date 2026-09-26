---
layout: post
title: "Evaluate the Bracket Pairs of a String"
date: 2026-09-26 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "String"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string evaluate(string s, vector<vector<string>>&\
        \ knowledge) {\n        unordered_map<string, string> dict;\n        for (const\
        \ auto& entry : knowledge) {\n            dict[entry[0]] = entry[1];\n     \
        \   }\n\n        string res;\n        res.reserve(s.length());\n        for\
        \ (int i = 0; i < s.length(); ++i) {\n            if (s[i] == '(') {\n     \
        \           int start = ++i;\n                while (s[i] != ')') {\n      \
        \              i++;\n                }\n                string key = s.substr(start,\
        \ i - start);\n                if (dict.count(key)) {\n                    res\
        \ += dict[key];\n                } else {\n                    res += '?';\n\
        \                }\n            } else {\n                res += s[i];\n   \
        \         }\n        }\n        return res;\n    }\n};"
      java: "class Solution {\n    public String evaluate(String s, List<List<String>>\
        \ knowledge) {\n        Map<String, String> dict = new HashMap<>();\n      \
        \  for (List<String> pair : knowledge) {\n            dict.put(pair.get(0),\
        \ pair.get(1));\n        }\n\n        StringBuilder sb = new StringBuilder();\n\
        \        int i = 0;\n        int n = s.length();\n        while (i < n) {\n\
        \            char c = s.charAt(i);\n            if (c == '(') {\n          \
        \      int start = ++i;\n                while (s.charAt(i) != ')') {\n    \
        \                i++;\n                }\n                String key = s.substring(start,\
        \ i);\n                sb.append(dict.getOrDefault(key, \"?\"));\n         \
        \   } else {\n                sb.append(c);\n            }\n            i++;\n\
        \        }\n        return sb.toString();\n    }\n}"
      python: "class Solution(object):\n    def evaluate(self, s, knowledge):\n    \
        \    \"\"\"\n        :type s: str\n        :type knowledge: List[List[str]]\n\
        \        :rtype: str\n        \"\"\"\n        d = {k: v for k, v in knowledge}\n\
        \        res = []\n        i = 0\n        n = len(s)\n        while i < n:\n\
        \            if s[i] == '(':\n                start = i + 1\n              \
        \  i = start\n                while s[i] != ')':\n                    i += 1\n\
        \                key = s[start:i]\n                res.append(d.get(key, \"\
        ?\"))\n            else:\n                res.append(s[i])\n            i +=\
        \ 1\n        return \"\".join(res)"
      python3: "class Solution:\n    def evaluate(self, s: str, knowledge: list[list[str]])\
        \ -> str:\n        d = {k: v for k, v in knowledge}\n        res = []\n    \
        \    i = 0\n        n = len(s)\n        while i < n:\n            if s[i] ==\
        \ '(':\n                start = i + 1\n                i = start\n         \
        \       while s[i] != ')':\n                    i += 1\n                key\
        \ = s[start:i]\n                res.append(d.get(key, \"?\"))\n            else:\n\
        \                res.append(s[i])\n            i += 1\n        return \"\".join(res)"
      c: "#include <stdlib.h>\n#include <string.h>\n\ntypedef struct {\n    char* key;\n\
        \    char* val;\n} Pair;\n\nint comparePairs(const void* a, const void* b) {\n\
        \    return strcmp(((Pair*)a)->key, ((Pair*)b)->key);\n}\n\nint searchCompare(const\
        \ void* targetKey, const void* element) {\n    return strcmp((const char*)targetKey,\
        \ ((Pair*)element)->key);\n}\n\nchar* evaluate(char* s, char*** knowledge, int\
        \ knowledgeSize, int* knowledgeColSize) {\n    Pair* pairs = NULL;\n    if (knowledgeSize\
        \ > 0) {\n        pairs = (Pair*)malloc(sizeof(Pair) * knowledgeSize);\n   \
        \     for (int i = 0; i < knowledgeSize; i++) {\n            pairs[i].key =\
        \ knowledge[i][0];\n            pairs[i].val = knowledge[i][1];\n        }\n\
        \        qsort(pairs, knowledgeSize, sizeof(Pair), comparePairs);\n    }\n\n\
        \    int n = strlen(s);\n    char* result = (char*)malloc(sizeof(char) * (n\
        \ * 10 + 1));\n    int resIdx = 0;\n\n    for (int i = 0; s[i] != '\\0'; i++)\
        \ {\n        if (s[i] == '(') {\n            int start = ++i;\n            while\
        \ (s[i] != ')') i++;\n            char original = s[i];\n            s[i] =\
        \ '\\0';\n            Pair* found = NULL;\n            if (knowledgeSize > 0)\
        \ {\n                found = (Pair*)bsearch(s + start, pairs, knowledgeSize,\
        \ sizeof(Pair), searchCompare);\n            }\n            s[i] = original;\n\
        \            if (found) {\n                int vLen = strlen(found->val);\n\
        \                memcpy(result + resIdx, found->val, vLen);\n              \
        \  resIdx += vLen;\n            } else {\n                result[resIdx++] =\
        \ '?';\n            }\n        } else {\n            result[resIdx++] = s[i];\n\
        \        }\n    }\n\n    result[resIdx] = '\\0';\n    if (pairs) free(pairs);\n\
        \    return result;\n}"
      csharp: "using System.Collections.Generic;\nusing System.Text;\n\npublic class\
        \ Solution {\n    public string Evaluate(string s, IList<IList<string>> knowledge)\
        \ {\n        Dictionary<string, string> dict = new Dictionary<string, string>();\n\
        \        foreach (var pair in knowledge) {\n            dict[pair[0]] = pair[1];\n\
        \        }\n\n        StringBuilder sb = new StringBuilder();\n        for (int\
        \ i = 0; i < s.Length; i++) {\n            if (s[i] == '(') {\n            \
        \    int start = ++i;\n                while (i < s.Length && s[i] != ')') {\n\
        \                    i++;\n                }\n                string key = s.Substring(start,\
        \ i - start);\n                if (dict.TryGetValue(key, out string value))\
        \ {\n                    sb.Append(value);\n                } else {\n     \
        \               sb.Append('?');\n                }\n            } else {\n \
        \               sb.Append(s[i]);\n            }\n        }\n\n        return\
        \ sb.ToString();\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {string[][]} knowledge\n * @return\
        \ {string}\n */\nvar evaluate = function(s, knowledge) {\n    const map = new\
        \ Map();\n    for (const [key, value] of knowledge) {\n        map.set(key,\
        \ value);\n    }\n\n    let result = [];\n    let i = 0;\n    const n = s.length;\n\
        \n    while (i < n) {\n        if (s[i] === '(') {\n            let start =\
        \ ++i;\n            while (i < n && s[i] !== ')') {\n                i++;\n\
        \            }\n            let key = s.substring(start, i);\n            result.push(map.has(key)\
        \ ? map.get(key) : '?');\n            i++; \n        } else {\n            result.push(s[i]);\n\
        \            i++;\n        }\n    }\n\n    return result.join('');\n};"
      typescript: "function evaluate(s: string, knowledge: string[][]): string {\n \
        \   const map = new Map<string, string>();\n    for (const [key, value] of knowledge)\
        \ {\n        map.set(key, value);\n    }\n\n    let result: string[] = [];\n\
        \    let i = 0;\n    const n = s.length;\n\n    while (i < n) {\n        if\
        \ (s[i] === '(') {\n            let start = ++i;\n            while (i < n &&\
        \ s[i] !== ')') {\n                i++;\n            }\n            let key\
        \ = s.substring(start, i);\n            result.push(map.has(key) ? map.get(key)\
        \ : '?');\n            i++;\n        } else {\n            result.push(s[i]);\n\
        \            i++;\n        }\n    }\n\n    return result.join('');\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param String[][]\
        \ $knowledge\n     * @return String\n     */\n    function evaluate($s, $knowledge)\
        \ {\n        $map = [];\n        foreach ($knowledge as $pair) {\n         \
        \   $map[$pair[0]] = $pair[1];\n        }\n\n        $res = [];\n        $len\
        \ = strlen($s);\n        for ($i = 0; $i < $len; $i++) {\n            if ($s[$i]\
        \ === '(') {\n                $start = ++$i;\n                while ($i < $len\
        \ && $s[$i] !== ')') {\n                    $i++;\n                }\n     \
        \           $key = substr($s, $start, $i - $start);\n                $res[]\
        \ = isset($map[$key]) ? $map[$key] : '?';\n            } else {\n          \
        \      $res[] = $s[$i];\n            }\n        }\n\n        return implode('',\
        \ $res);\n    }\n}"
      swift: "class Solution {\n    func evaluate(_ s: String, _ knowledge: [[String]])\
        \ -> String {\n        var dict = [String: String]()\n        for pair in knowledge\
        \ {\n            dict[pair[0]] = pair[1]\n        }\n\n        var result =\
        \ \"\"\n        result.reserveCapacity(s.count)\n        let chars = Array(s)\n\
        \        var i = 0\n        let count = chars.count\n\n        while i < count\
        \ {\n            if chars[i] == \"(\" {\n                i += 1\n          \
        \      let start = i\n                while i < count && chars[i] != \")\" {\n\
        \                    i += 1\n                }\n                let key = String(chars[start..<i])\n\
        \                result.append(dict[key] ?? \"?\")\n                i += 1\n\
        \            } else {\n                result.append(chars[i])\n           \
        \     i += 1\n            }\n        }\n\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun evaluate(s: String, knowledge: List<List<String>>):\
        \ String {\n        val dict = knowledge.associate { it[0] to it[1] }\n    \
        \    val sb = StringBuilder()\n        var i = 0\n        val n = s.length\n\
        \        while (i < n) {\n            if (s[i] == '(') {\n                val\
        \ start = i + 1\n                i++\n                while (s[i] != ')') {\n\
        \                    i++\n                }\n                val key = s.substring(start,\
        \ i)\n                sb.append(dict[key] ?: \"?\")\n            } else {\n\
        \                sb.append(s[i])\n            }\n            i++\n        }\n\
        \        return sb.toString()\n    }\n}"
      dart: "class Solution {\n  String evaluate(String s, List<List<String>> knowledge)\
        \ {\n    Map<String, String> dict = {\n      for (var pair in knowledge) pair[0]:\
        \ pair[1]\n    };\n    StringBuffer sb = StringBuffer();\n    int n = s.length;\n\
        \    for (int i = 0; i < n; i++) {\n      if (s[i] == '(') {\n        int start\
        \ = i + 1;\n        i++;\n        while (s[i] != ')') {\n          i++;\n  \
        \      }\n        String key = s.substring(start, i);\n        sb.write(dict[key]\
        \ ?? \"?\");\n      } else {\n        sb.write(s[i]);\n      }\n    }\n    return\
        \ sb.toString();\n  }\n}"
      go: "import \"strings\"\n\nfunc evaluate(s string, knowledge [][]string) string\
        \ {\n    m := make(map[string]string)\n    for _, pair := range knowledge {\n\
        \        m[pair[0]] = pair[1]\n    }\n    var sb strings.Builder\n    n := len(s)\n\
        \    for i := 0; i < n; i++ {\n        if s[i] == '(' {\n            start :=\
        \ i + 1\n            i++\n            for s[i] != ')' {\n                i++\n\
        \            }\n            key := s[start:i]\n            if val, ok := m[key];\
        \ ok {\n                sb.WriteString(val)\n            } else {\n        \
        \        sb.WriteString(\"?\")\n            }\n        } else {\n          \
        \  sb.WriteByte(s[i])\n        }\n    }\n    return sb.String()\n}"
      ruby: "# @param {String} s\n# @param {String[][]} knowledge\n# @return {String}\n\
        def evaluate(s, knowledge)\n  dict = knowledge.to_h\n  res = \"\"\n  i = 0\n\
        \  n = s.length\n  while i < n\n    if s[i] == '('\n      start_idx = i + 1\n\
        \      i += 1\n      while s[i] != ')'\n        i += 1\n      end\n      key\
        \ = s[start_idx...i]\n      res << (dict[key] || \"?\")\n    else\n      res\
        \ << s[i]\n    end\n    i += 1\n  end\n  res\nend"
      scala: "object Solution {\n    def evaluate(s: String, knowledge: List[List[String]]):\
        \ String = {\n        val dict = knowledge.map(kv => kv(0) -> kv(1)).toMap\n\
        \        val sb = new StringBuilder()\n        var i = 0\n        val n = s.length\n\
        \        while (i < n) {\n            if (s(i) == '(') {\n                val\
        \ start = i + 1\n                i += 1\n                while (s(i) != ')')\
        \ {\n                    i += 1\n                }\n                val key\
        \ = s.substring(start, i)\n                sb.append(dict.getOrElse(key, \"\
        ?\"))\n            } else {\n                sb.append(s(i))\n            }\n\
        \            i += 1\n        }\n        sb.toString()\n    }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn evaluate(s:\
        \ String, knowledge: Vec<Vec<String>>) -> String {\n        let mut map = HashMap::with_capacity(knowledge.len());\n\
        \        for mut kv in knowledge {\n            if kv.len() == 2 {\n       \
        \         let value = kv.pop().unwrap();\n                let key = kv.pop().unwrap();\n\
        \                map.insert(key, value);\n            }\n        }\n\n     \
        \   let mut result = String::with_capacity(s.len());\n        let mut key =\
        \ String::new();\n        let mut in_bracket = false;\n\n        for c in s.chars()\
        \ {\n            match c {\n                '(' => in_bracket = true,\n    \
        \            ')' => {\n                    in_bracket = false;\n           \
        \         if let Some(val) = map.get(&key) {\n                        result.push_str(val);\n\
        \                    } else {\n                        result.push('?');\n \
        \                   }\n                    key.clear();\n                }\n\
        \                _ => {\n                    if in_bracket {\n             \
        \           key.push(c);\n                    } else {\n                   \
        \     result.push(c);\n                    }\n                }\n          \
        \  }\n        }\n        result\n    }\n}"
      racket: "(define/contract (evaluate s knowledge)\n  (-> string? (listof (listof\
        \ string?)) string?)\n  (let ([dict (make-hash)])\n    (for ([kv knowledge])\n\
        \      (hash-set! dict (car kv) (cadr kv)))\n    (let ([out (open-output-string)])\n\
        \      (let loop ([chars (string->list s)] [key-acc #f])\n        (cond\n  \
        \        [(null? chars) (get-output-string out)]\n          [else\n        \
        \   (let ([c (car chars)] [rest (cdr chars)])\n             (cond\n        \
        \       [(char=? c #\\() (loop rest '())]\n               [(char=? c #\\))\n\
        \                (display (hash-ref dict (list->string (reverse key-acc)) \"\
        ?\") out)\n                (loop rest #f)]\n               [key-acc (loop rest\
        \ (cons c key-acc))]\n               [else (display c out) (loop rest #f)]))])))))"
      erlang: "-spec evaluate(S :: unicode:unicode_binary(), Knowledge :: [[unicode:unicode_binary()]])\
        \ -> unicode:unicode_binary().\nevaluate(S, Knowledge) ->\n    Map = maps:from_list([{K,\
        \ V} || [K, V] <- Knowledge]),\n    Res = solve(S, Map, []),\n    unicode:characters_to_binary(Res).\n\
        \nsolve(<<>>, _Map, Acc) ->\n    lists:reverse(Acc);\nsolve(<<$(, Rest/binary>>,\
        \ Map, Acc) ->\n    {Key, AfterBracket} = get_key(Rest, []),\n    Val = maps:get(Key,\
        \ Map, <<\"?\">>),\n    solve(AfterBracket, Map, [Val | Acc]);\nsolve(<<C, Rest/binary>>,\
        \ Map, Acc) ->\n    solve(Rest, Map, [C | Acc]).\n\nget_key(<<$), Rest/binary>>,\
        \ KeyAcc) ->\n    {unicode:characters_to_binary(lists:reverse(KeyAcc)), Rest};\n\
        get_key(<<C, Rest/binary>>, KeyAcc) ->\n    get_key(Rest, [C | KeyAcc])."
      elixir: "defmodule Solution do\n  @spec evaluate(s :: String.t, knowledge :: [[String.t]])\
        \ :: String.t\n  def evaluate(s, knowledge) do\n    map = Map.new(knowledge,\
        \ fn [k, v] -> {k, v} end)\n\n    {res, _} = s\n    |> String.to_charlist()\n\
        \    |> Enum.reduce({[], nil}, fn\n      ?(, {acc, _} -> {acc, []}\n      ?),\
        \ {acc, key_acc} ->\n        key = List.to_string(Enum.reverse(key_acc))\n \
        \       val = Map.get(map, key, \"?\")\n        {[val | acc], nil}\n      char,\
        \ {acc, nil} -> {[char | acc], nil}\n      char, {acc, key_acc} -> {acc, [char\
        \ | key_acc]}\n    end)\n\n    res |> Enum.reverse() |> IO.iodata_to_binary()\n\
        \  end\nend"
    approach: The problem asks to substitute bracketed keys in a string with their corresponding
      values from a given list of pairs. To efficiently solve this, we first convert
      the 'knowledge' 2D array into a hash map (dictionary). This allows us to perform
      average-time O(1) lookups for any key encountered during the string processing
      phase. Given the constraints that keys are unique and no nested brackets exist,
      we can process the string in a single linear pass.
    time_complexity: O(N + K) where N is the length of the input string s and K is the
      total number of characters across all keys and values in the knowledge list. Building
      the hash map takes O(K) time, and iterating through the string s while performing
      lookups takes O(N) time.
    space_complexity: O(N + K) because we store the entire knowledge base in a hash
      map and build a result string that can potentially be longer than the original
      input string.
    elapsed_time: 179.49667096138
    model: gemini-3-flash-preview
    generated_at: '2026-09-26 02:53:33 '
---

## Problem #1807: Evaluate the Bracket Pairs of a String

**Difficulty:** Medium

**Topics:** Array, Hash Table, String

## Problem Description

<p>You are given a string <code>s</code> that contains some bracket pairs, with each pair containing a <strong>non-empty</strong> key.</p>

<ul>
	<li>For example, in the string <code>&quot;(name)is(age)yearsold&quot;</code>, there are <strong>two</strong> bracket pairs that contain the keys <code>&quot;name&quot;</code> and <code>&quot;age&quot;</code>.</li>
</ul>

<p>You know the values of a wide range of keys. This is represented by a 2D string array <code>knowledge</code> where each <code>knowledge[i] = [key<sub>i</sub>, value<sub>i</sub>]</code> indicates that key <code>key<sub>i</sub></code> has a value of <code>value<sub>i</sub></code>.</p>

<p>You are tasked to evaluate <strong>all</strong> of the bracket pairs. When you evaluate a bracket pair that contains some key <code>key<sub>i</sub></code>, you will:</p>

<ul>
	<li>Replace <code>key<sub>i</sub></code> and the bracket pair with the key&#39;s corresponding <code>value<sub>i</sub></code>.</li>
	<li>If you do not know the value of the key, you will replace <code>key<sub>i</sub></code> and the bracket pair with a question mark <code>&quot;?&quot;</code> (without the quotation marks).</li>
</ul>

<p>Each key will appear at most once in your <code>knowledge</code>. There will not be any nested brackets in <code>s</code>.</p>

<p>Return <em>the resulting string after evaluating <strong>all</strong> of the bracket pairs.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(name)is(age)yearsold&quot;, knowledge = [[&quot;name&quot;,&quot;bob&quot;],[&quot;age&quot;,&quot;two&quot;]]
<strong>Output:</strong> &quot;bobistwoyearsold&quot;
<strong>Explanation:</strong>
The key &quot;name&quot; has a value of &quot;bob&quot;, so replace &quot;(name)&quot; with &quot;bob&quot;.
The key &quot;age&quot; has a value of &quot;two&quot;, so replace &quot;(age)&quot; with &quot;two&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;hi(name)&quot;, knowledge = [[&quot;a&quot;,&quot;b&quot;]]
<strong>Output:</strong> &quot;hi?&quot;
<strong>Explanation:</strong> As you do not know the value of the key &quot;name&quot;, replace &quot;(name)&quot; with &quot;?&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(a)(a)(a)aaa&quot;, knowledge = [[&quot;a&quot;,&quot;yes&quot;]]
<strong>Output:</strong> &quot;yesyesyesaaa&quot;
<strong>Explanation:</strong> The same key can appear multiple times.
The key &quot;a&quot; has a value of &quot;yes&quot;, so replace all occurrences of &quot;(a)&quot; with &quot;yes&quot;.
Notice that the &quot;a&quot;s not in a bracket pair are not evaluated.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= knowledge.length &lt;= 10<sup>5</sup></code></li>
	<li><code>knowledge[i].length == 2</code></li>
	<li><code>1 &lt;= key<sub>i</sub>.length, value<sub>i</sub>.length &lt;= 10</code></li>
	<li><code>s</code> consists of lowercase English letters and round brackets <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>.</li>
	<li>Every open bracket <code>&#39;(&#39;</code> in <code>s</code> will have a corresponding close bracket <code>&#39;)&#39;</code>.</li>
	<li>The key in each bracket pair of <code>s</code> will be non-empty.</li>
	<li>There will not be any nested bracket pairs in <code>s</code>.</li>
	<li><code>key<sub>i</sub></code> and <code>value<sub>i</sub></code> consist of lowercase English letters.</li>
	<li>Each <code>key<sub>i</sub></code> in <code>knowledge</code> is unique.</li>
</ul>


## Hints

1. Process pairs from right to left to handle repeats

2. Keep track of the current enclosed string using another string

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to substitute bracketed keys in a string with their corresponding values from a given list of pairs. To efficiently solve this, we first convert the 'knowledge' 2D array into a hash map (dictionary). This allows us to perform average-time O(1) lookups for any key encountered during the string processing phase. Given the constraints that keys are unique and no nested brackets exist, we can process the string in a single linear pass.

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
    string evaluate(string s, vector<vector<string>>& knowledge) {
        unordered_map<string, string> dict;
        for (const auto& entry : knowledge) {
            dict[entry[0]] = entry[1];
        }

        string res;
        res.reserve(s.length());
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                int start = ++i;
                while (s[i] != ')') {
                    i++;
                }
                string key = s.substr(start, i - start);
                if (dict.count(key)) {
                    res += dict[key];
                } else {
                    res += '?';
                }
            } else {
                res += s[i];
            }
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String evaluate(String s, List<List<String>> knowledge) {
        Map<String, String> dict = new HashMap<>();
        for (List<String> pair : knowledge) {
            dict.put(pair.get(0), pair.get(1));
        }

        StringBuilder sb = new StringBuilder();
        int i = 0;
        int n = s.length();
        while (i < n) {
            char c = s.charAt(i);
            if (c == '(') {
                int start = ++i;
                while (s.charAt(i) != ')') {
                    i++;
                }
                String key = s.substring(start, i);
                sb.append(dict.getOrDefault(key, "?"));
            } else {
                sb.append(c);
            }
            i++;
        }
        return sb.toString();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = {k: v for k, v in knowledge}
        res = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                start = i + 1
                i = start
                while s[i] != ')':
                    i += 1
                key = s[start:i]
                res.append(d.get(key, "?"))
            else:
                res.append(s[i])
            i += 1
        return "".join(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {k: v for k, v in knowledge}
        res = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                start = i + 1
                i = start
                while s[i] != ')':
                    i += 1
                key = s[start:i]
                res.append(d.get(key, "?"))
            else:
                res.append(s[i])
            i += 1
        return "".join(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* key;
    char* val;
} Pair;

int comparePairs(const void* a, const void* b) {
    return strcmp(((Pair*)a)->key, ((Pair*)b)->key);
}

int searchCompare(const void* targetKey, const void* element) {
    return strcmp((const char*)targetKey, ((Pair*)element)->key);
}

char* evaluate(char* s, char*** knowledge, int knowledgeSize, int* knowledgeColSize) {
    Pair* pairs = NULL;
    if (knowledgeSize > 0) {
        pairs = (Pair*)malloc(sizeof(Pair) * knowledgeSize);
        for (int i = 0; i < knowledgeSize; i++) {
            pairs[i].key = knowledge[i][0];
            pairs[i].val = knowledge[i][1];
        }
        qsort(pairs, knowledgeSize, sizeof(Pair), comparePairs);
    }

    int n = strlen(s);
    char* result = (char*)malloc(sizeof(char) * (n * 10 + 1));
    int resIdx = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            int start = ++i;
            while (s[i] != ')') i++;
            char original = s[i];
            s[i] = '\0';
            Pair* found = NULL;
            if (knowledgeSize > 0) {
                found = (Pair*)bsearch(s + start, pairs, knowledgeSize, sizeof(Pair), searchCompare);
            }
            s[i] = original;
            if (found) {
                int vLen = strlen(found->val);
                memcpy(result + resIdx, found->val, vLen);
                resIdx += vLen;
            } else {
                result[resIdx++] = '?';
            }
        } else {
            result[resIdx++] = s[i];
        }
    }

    result[resIdx] = '\0';
    if (pairs) free(pairs);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;
using System.Text;

public class Solution {
    public string Evaluate(string s, IList<IList<string>> knowledge) {
        Dictionary<string, string> dict = new Dictionary<string, string>();
        foreach (var pair in knowledge) {
            dict[pair[0]] = pair[1];
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.Length; i++) {
            if (s[i] == '(') {
                int start = ++i;
                while (i < s.Length && s[i] != ')') {
                    i++;
                }
                string key = s.Substring(start, i - start);
                if (dict.TryGetValue(key, out string value)) {
                    sb.Append(value);
                } else {
                    sb.Append('?');
                }
            } else {
                sb.Append(s[i]);
            }
        }

        return sb.ToString();
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
 * @param {string[][]} knowledge
 * @return {string}
 */
var evaluate = function(s, knowledge) {
    const map = new Map();
    for (const [key, value] of knowledge) {
        map.set(key, value);
    }

    let result = [];
    let i = 0;
    const n = s.length;

    while (i < n) {
        if (s[i] === '(') {
            let start = ++i;
            while (i < n && s[i] !== ')') {
                i++;
            }
            let key = s.substring(start, i);
            result.push(map.has(key) ? map.get(key) : '?');
            i++; 
        } else {
            result.push(s[i]);
            i++;
        }
    }

    return result.join('');
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function evaluate(s: string, knowledge: string[][]): string {
    const map = new Map<string, string>();
    for (const [key, value] of knowledge) {
        map.set(key, value);
    }

    let result: string[] = [];
    let i = 0;
    const n = s.length;

    while (i < n) {
        if (s[i] === '(') {
            let start = ++i;
            while (i < n && s[i] !== ')') {
                i++;
            }
            let key = s.substring(start, i);
            result.push(map.has(key) ? map.get(key) : '?');
            i++;
        } else {
            result.push(s[i]);
            i++;
        }
    }

    return result.join('');
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
     * @param String[][] $knowledge
     * @return String
     */
    function evaluate($s, $knowledge) {
        $map = [];
        foreach ($knowledge as $pair) {
            $map[$pair[0]] = $pair[1];
        }

        $res = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '(') {
                $start = ++$i;
                while ($i < $len && $s[$i] !== ')') {
                    $i++;
                }
                $key = substr($s, $start, $i - $start);
                $res[] = isset($map[$key]) ? $map[$key] : '?';
            } else {
                $res[] = $s[$i];
            }
        }

        return implode('', $res);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func evaluate(_ s: String, _ knowledge: [[String]]) -> String {
        var dict = [String: String]()
        for pair in knowledge {
            dict[pair[0]] = pair[1]
        }

        var result = ""
        result.reserveCapacity(s.count)
        let chars = Array(s)
        var i = 0
        let count = chars.count

        while i < count {
            if chars[i] == "(" {
                i += 1
                let start = i
                while i < count && chars[i] != ")" {
                    i += 1
                }
                let key = String(chars[start..<i])
                result.append(dict[key] ?? "?")
                i += 1
            } else {
                result.append(chars[i])
                i += 1
            }
        }

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
    fun evaluate(s: String, knowledge: List<List<String>>): String {
        val dict = knowledge.associate { it[0] to it[1] }
        val sb = StringBuilder()
        var i = 0
        val n = s.length
        while (i < n) {
            if (s[i] == '(') {
                val start = i + 1
                i++
                while (s[i] != ')') {
                    i++
                }
                val key = s.substring(start, i)
                sb.append(dict[key] ?: "?")
            } else {
                sb.append(s[i])
            }
            i++
        }
        return sb.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String evaluate(String s, List<List<String>> knowledge) {
    Map<String, String> dict = {
      for (var pair in knowledge) pair[0]: pair[1]
    };
    StringBuffer sb = StringBuffer();
    int n = s.length;
    for (int i = 0; i < n; i++) {
      if (s[i] == '(') {
        int start = i + 1;
        i++;
        while (s[i] != ')') {
          i++;
        }
        String key = s.substring(start, i);
        sb.write(dict[key] ?? "?");
      } else {
        sb.write(s[i]);
      }
    }
    return sb.toString();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "strings"

func evaluate(s string, knowledge [][]string) string {
    m := make(map[string]string)
    for _, pair := range knowledge {
        m[pair[0]] = pair[1]
    }
    var sb strings.Builder
    n := len(s)
    for i := 0; i < n; i++ {
        if s[i] == '(' {
            start := i + 1
            i++
            for s[i] != ')' {
                i++
            }
            key := s[start:i]
            if val, ok := m[key]; ok {
                sb.WriteString(val)
            } else {
                sb.WriteString("?")
            }
        } else {
            sb.WriteByte(s[i])
        }
    }
    return sb.String()
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {String[][]} knowledge
# @return {String}
def evaluate(s, knowledge)
  dict = knowledge.to_h
  res = ""
  i = 0
  n = s.length
  while i < n
    if s[i] == '('
      start_idx = i + 1
      i += 1
      while s[i] != ')'
        i += 1
      end
      key = s[start_idx...i]
      res << (dict[key] || "?")
    else
      res << s[i]
    end
    i += 1
  end
  res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def evaluate(s: String, knowledge: List[List[String]]): String = {
        val dict = knowledge.map(kv => kv(0) -> kv(1)).toMap
        val sb = new StringBuilder()
        var i = 0
        val n = s.length
        while (i < n) {
            if (s(i) == '(') {
                val start = i + 1
                i += 1
                while (s(i) != ')') {
                    i += 1
                }
                val key = s.substring(start, i)
                sb.append(dict.getOrElse(key, "?"))
            } else {
                sb.append(s(i))
            }
            i += 1
        }
        sb.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;

impl Solution {
    pub fn evaluate(s: String, knowledge: Vec<Vec<String>>) -> String {
        let mut map = HashMap::with_capacity(knowledge.len());
        for mut kv in knowledge {
            if kv.len() == 2 {
                let value = kv.pop().unwrap();
                let key = kv.pop().unwrap();
                map.insert(key, value);
            }
        }

        let mut result = String::with_capacity(s.len());
        let mut key = String::new();
        let mut in_bracket = false;

        for c in s.chars() {
            match c {
                '(' => in_bracket = true,
                ')' => {
                    in_bracket = false;
                    if let Some(val) = map.get(&key) {
                        result.push_str(val);
                    } else {
                        result.push('?');
                    }
                    key.clear();
                }
                _ => {
                    if in_bracket {
                        key.push(c);
                    } else {
                        result.push(c);
                    }
                }
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (evaluate s knowledge)
  (-> string? (listof (listof string?)) string?)
  (let ([dict (make-hash)])
    (for ([kv knowledge])
      (hash-set! dict (car kv) (cadr kv)))
    (let ([out (open-output-string)])
      (let loop ([chars (string->list s)] [key-acc #f])
        (cond
          [(null? chars) (get-output-string out)]
          [else
           (let ([c (car chars)] [rest (cdr chars)])
             (cond
               [(char=? c #\() (loop rest '())]
               [(char=? c #\))
                (display (hash-ref dict (list->string (reverse key-acc)) "?") out)
                (loop rest #f)]
               [key-acc (loop rest (cons c key-acc))]
               [else (display c out) (loop rest #f)]))])))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec evaluate(S :: unicode:unicode_binary(), Knowledge :: [[unicode:unicode_binary()]]) -> unicode:unicode_binary().
evaluate(S, Knowledge) ->
    Map = maps:from_list([{K, V} || [K, V] <- Knowledge]),
    Res = solve(S, Map, []),
    unicode:characters_to_binary(Res).

solve(<<>>, _Map, Acc) ->
    lists:reverse(Acc);
solve(<<$(, Rest/binary>>, Map, Acc) ->
    {Key, AfterBracket} = get_key(Rest, []),
    Val = maps:get(Key, Map, <<"?">>),
    solve(AfterBracket, Map, [Val | Acc]);
solve(<<C, Rest/binary>>, Map, Acc) ->
    solve(Rest, Map, [C | Acc]).

get_key(<<$), Rest/binary>>, KeyAcc) ->
    {unicode:characters_to_binary(lists:reverse(KeyAcc)), Rest};
get_key(<<C, Rest/binary>>, KeyAcc) ->
    get_key(Rest, [C | KeyAcc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec evaluate(s :: String.t, knowledge :: [[String.t]]) :: String.t
  def evaluate(s, knowledge) do
    map = Map.new(knowledge, fn [k, v] -> {k, v} end)

    {res, _} = s
    |> String.to_charlist()
    |> Enum.reduce({[], nil}, fn
      ?(, {acc, _} -> {acc, []}
      ?), {acc, key_acc} ->
        key = List.to_string(Enum.reverse(key_acc))
        val = Map.get(map, key, "?")
        {[val | acc], nil}
      char, {acc, nil} -> {[char | acc], nil}
      char, {acc, key_acc} -> {acc, [char | key_acc]}
    end)

    res |> Enum.reverse() |> IO.iodata_to_binary()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + K) where N is the length of the input string s and K is the total number of characters across all keys and values in the knowledge list. Building the hash map takes O(K) time, and iterating through the string s while performing lookups takes O(N) time.
- **Space Complexity:** O(N + K) because we store the entire knowledge base in a hash map and build a result string that can potentially be longer than the original input string.
