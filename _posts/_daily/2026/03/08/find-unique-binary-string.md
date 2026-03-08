---
layout: post
title: "Find Unique Binary String"
date: 2026-03-08 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "String", "Backtracking"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-unique-binary-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string findDifferentBinaryString(vector<string>&\
        \ nums) {\n        string res = \"\";\n        for (int i = 0; i < nums.size();\
        \ ++i) {\n            res += (nums[i][i] == '0' ? '1' : '0');\n        }\n \
        \       return res;\n    }\n};"
      java: "class Solution {\n    public String findDifferentBinaryString(String[]\
        \ nums) {\n        StringBuilder sb = new StringBuilder();\n        for (int\
        \ i = 0; i < nums.length; i++) {\n            sb.append(nums[i].charAt(i) ==\
        \ '0' ? '1' : '0');\n        }\n        return sb.toString();\n    }\n}"
      python: "class Solution(object):\n    def findDifferentBinaryString(self, nums):\n\
        \        \"\"\"\n        :type nums: List[str]\n        :rtype: str\n      \
        \  \"\"\"\n        res = []\n        for i in range(len(nums)):\n          \
        \  res.append('1' if nums[i][i] == '0' else '0')\n        return \"\".join(res)"
      python3: "class Solution:\n    def findDifferentBinaryString(self, nums: List[str])\
        \ -> str:\n        return \"\".join('1' if nums[i][i] == '0' else '0' for i\
        \ in range(len(nums)))"
      c: "char* findDifferentBinaryString(char** nums, int numsSize) {\n    char* res\
        \ = (char*)malloc((numsSize + 1) * sizeof(char));\n    for (int i = 0; i < numsSize;\
        \ i++) {\n        res[i] = (nums[i][i] == '0' ? '1' : '0');\n    }\n    res[numsSize]\
        \ = '\\0';\n    return res;\n}"
      csharp: "public class Solution {\n    public string FindDifferentBinaryString(string[]\
        \ nums) {\n        char[] res = new char[nums.Length];\n        for (int i =\
        \ 0; i < nums.Length; i++) {\n            res[i] = nums[i][i] == '0' ? '1' :\
        \ '0';\n        }\n        return new string(res);\n    }\n}"
      javascript: "/**\n * @param {string[]} nums\n * @return {string}\n */\nvar findDifferentBinaryString\
        \ = function(nums) {\n    let res = \"\";\n    for (let i = 0; i < nums.length;\
        \ i++) {\n        res += nums[i][i] === '0' ? '1' : '0';\n    }\n    return\
        \ res;\n};"
      typescript: "function findDifferentBinaryString(nums: string[]): string {\n  \
        \  let result = \"\";\n    for (let i = 0; i < nums.length; i++) {\n       \
        \ result += nums[i][i] === '0' ? '1' : '0';\n    }\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param String[] $nums\n     * @return\
        \ String\n     */\n    function findDifferentBinaryString($nums) {\n       \
        \ $result = \"\";\n        $n = count($nums);\n        for ($i = 0; $i < $n;\
        \ $i++) {\n            $result .= ($nums[$i][$i] === '0' ? '1' : '0');\n   \
        \     }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func findDifferentBinaryString(_ nums: [String])\
        \ -> String {\n        var result = \"\"\n        for i in 0..<nums.count {\n\
        \            let str = nums[i]\n            let char = str[str.index(str.startIndex,\
        \ offsetBy: i)]\n            result += (char == \"0\" ? \"1\" : \"0\")\n   \
        \     }\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun findDifferentBinaryString(nums: Array<String>):\
        \ String {\n        val sb = StringBuilder()\n        for (i in nums.indices)\
        \ {\n            sb.append(if (nums[i][i] == '0') '1' else '0')\n        }\n\
        \        return sb.toString()\n    }\n}"
      dart: "class Solution {\n  String findDifferentBinaryString(List<String> nums)\
        \ {\n    String result = \"\";\n    for (int i = 0; i < nums.length; i++) {\n\
        \      result += (nums[i][i] == '0' ? '1' : '0');\n    }\n    return result;\n\
        \  }\n}"
      go: "func findDifferentBinaryString(nums []string) string {\n    res := make([]byte,\
        \ len(nums))\n    for i := 0; i < len(nums); i++ {\n        if nums[i][i] ==\
        \ '0' {\n            res[i] = '1'\n        } else {\n            res[i] = '0'\n\
        \        }\n    }\n    return string(res)\n}"
      ruby: "def find_different_binary_string(nums)\n  nums.each_with_index.map { |s,\
        \ i| s[i] == '0' ? '1' : '0' }.join\nend"
      scala: "object Solution {\n  def findDifferentBinaryString(nums: Array[String]):\
        \ String = {\n    nums.indices.map(i => if (nums(i)(i) == '0') '1' else '0').mkString\n\
        \  }\n}"
      rust: "impl Solution {\n    pub fn find_different_binary_string(nums: Vec<String>)\
        \ -> String {\n        nums.iter()\n            .enumerate()\n            .map(|(i,\
        \ s)| if s.as_bytes()[i] == b'0' { '1' } else { '0' })\n            .collect()\n\
        \    }\n}"
      racket: "(define/contract (find-different-binary-string nums)\n  (-> (listof string?)\
        \ string?)\n  (list->string\n   (for/list ([s (in-list nums)]\n            \
        \  [i (in-naturals)])\n     (if (char=? (string-ref s i) #\\0) #\\1 #\\0))))"
      erlang: "-spec find_different_binary_string(Nums :: [unicode:unicode_binary()])\
        \ -> unicode:unicode_binary().\nfind_different_binary_string(Nums) ->\n  Helper\
        \ = fun(Self, [], _, Acc) -> lists:reverse(Acc);\n              (Self, [H|T],\
        \ I, Acc) ->\n                Bit = if binary:at(H, I) =:= $0 -> $1; true ->\
        \ $0 end,\n                Self(Self, T, I + 1, [Bit|Acc])\n           end,\n\
        \  list_to_binary(Helper(Helper, Nums, 0, []))."
      elixir: "defmodule Solution do\n  @spec find_different_binary_string(nums :: [String.t])\
        \ :: String.t\n  def find_different_binary_string(nums) do\n    nums\n    |>\
        \ Enum.with_index()\n    |> Enum.map(fn {s, i} ->\n      if String.at(s, i)\
        \ == \"0\", do: \"1\", else: \"0\"\n    end)\n    |> Enum.join()\n  end\nend"
    approach: 'The problem asks for a binary string of length $n$ that is not present
      in a given list of $n$ binary strings. We can solve this elegantly using Cantor''s
      Diagonal Argument. By constructing a new string where the $i$-th character is
      the bitwise inverse of the $i$-th character of the $i$-th string in the input
      array, we ensure that our generated string differs from every string in the list
      by at least one bit.


      Specifically, for each index $i$ from $0$ to $n-1$, we look at the string $nums[i]$
      and its character at index $i$. If $nums[i][i]$ is ''0'', we set the $i$-th character
      of our result to ''1''. If it is ''1'', we set it to ''0''. This construction
      guarantees that the resulting string is unique relative to the input set because
      it is mathematically impossible for it to match the $i$-th string in the set at
      the $i$-th position.'
    time_complexity: O(n), where n is the number of strings (and the length of each
      string). We perform a single pass through the list of strings, performing a constant-time
      character check and assignment at each step.
    space_complexity: O(n) if we consider the space required to store the output string,
      as we construct a string of length n. The auxiliary space used during the computation
      is O(1) or O(n) depending on whether the language allows mutable strings or requires
      a buffer like StringBuilder.
    elapsed_time: 62.97706747055054
    model: gemini-3-flash-preview
    generated_at: '2026-03-08 01:25:10 '
---

## Problem #1980: Find Unique Binary String

**Difficulty:** Medium

**Topics:** Array, Hash Table, String, Backtracking

## Problem Description

<p>Given an array of strings <code>nums</code> containing <code>n</code> <strong>unique</strong> binary strings each of length <code>n</code>, return <em>a binary string of length </em><code>n</code><em> that <strong>does not appear</strong> in </em><code>nums</code><em>. If there are multiple answers, you may return <strong>any</strong> of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;01&quot;,&quot;10&quot;]
<strong>Output:</strong> &quot;11&quot;
<strong>Explanation:</strong> &quot;11&quot; does not appear in nums. &quot;00&quot; would also be correct.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;00&quot;,&quot;01&quot;]
<strong>Output:</strong> &quot;11&quot;
<strong>Explanation:</strong> &quot;11&quot; does not appear in nums. &quot;10&quot; would also be correct.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [&quot;111&quot;,&quot;011&quot;,&quot;001&quot;]
<strong>Output:</strong> &quot;101&quot;
<strong>Explanation:</strong> &quot;101&quot; does not appear in nums. &quot;000&quot;, &quot;010&quot;, &quot;100&quot;, and &quot;110&quot; would also be correct.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 16</code></li>
	<li><code>nums[i].length == n</code></li>
	<li><code>nums[i] </code>is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li>All the strings of <code>nums</code> are <strong>unique</strong>.</li>
</ul>


## Hints

1. We can convert the given strings into base 10 integers.

2. Can we use recursion to generate all possible strings?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for a binary string of length $n$ that is not present in a given list of $n$ binary strings. We can solve this elegantly using Cantor's Diagonal Argument. By constructing a new string where the $i$-th character is the bitwise inverse of the $i$-th character of the $i$-th string in the input array, we ensure that our generated string differs from every string in the list by at least one bit.

Specifically, for each index $i$ from $0$ to $n-1$, we look at the string $nums[i]$ and its character at index $i$. If $nums[i][i]$ is '0', we set the $i$-th character of our result to '1'. If it is '1', we set it to '0'. This construction guarantees that the resulting string is unique relative to the input set because it is mathematically impossible for it to match the $i$-th string in the set at the $i$-th position.

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
    string findDifferentBinaryString(vector<string>& nums) {
        string res = "";
        for (int i = 0; i < nums.size(); ++i) {
            res += (nums[i][i] == '0' ? '1' : '0');
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
    public String findDifferentBinaryString(String[] nums) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < nums.length; i++) {
            sb.append(nums[i].charAt(i) == '0' ? '1' : '0');
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
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        res = []
        for i in range(len(nums)):
            res.append('1' if nums[i][i] == '0' else '0')
        return "".join(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
char* findDifferentBinaryString(char** nums, int numsSize) {
    char* res = (char*)malloc((numsSize + 1) * sizeof(char));
    for (int i = 0; i < numsSize; i++) {
        res[i] = (nums[i][i] == '0' ? '1' : '0');
    }
    res[numsSize] = '\0';
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public string FindDifferentBinaryString(string[] nums) {
        char[] res = new char[nums.Length];
        for (int i = 0; i < nums.Length; i++) {
            res[i] = nums[i][i] == '0' ? '1' : '0';
        }
        return new string(res);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {
    let res = "";
    for (let i = 0; i < nums.length; i++) {
        res += nums[i][i] === '0' ? '1' : '0';
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findDifferentBinaryString(nums: string[]): string {
    let result = "";
    for (let i = 0; i < nums.length; i++) {
        result += nums[i][i] === '0' ? '1' : '0';
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[] $nums
     * @return String
     */
    function findDifferentBinaryString($nums) {
        $result = "";
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $result .= ($nums[$i][$i] === '0' ? '1' : '0');
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findDifferentBinaryString(_ nums: [String]) -> String {
        var result = ""
        for i in 0..<nums.count {
            let str = nums[i]
            let char = str[str.index(str.startIndex, offsetBy: i)]
            result += (char == "0" ? "1" : "0")
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
    fun findDifferentBinaryString(nums: Array<String>): String {
        val sb = StringBuilder()
        for (i in nums.indices) {
            sb.append(if (nums[i][i] == '0') '1' else '0')
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
  String findDifferentBinaryString(List<String> nums) {
    String result = "";
    for (int i = 0; i < nums.length; i++) {
      result += (nums[i][i] == '0' ? '1' : '0');
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findDifferentBinaryString(nums []string) string {
    res := make([]byte, len(nums))
    for i := 0; i < len(nums); i++ {
        if nums[i][i] == '0' {
            res[i] = '1'
        } else {
            res[i] = '0'
        }
    }
    return string(res)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def find_different_binary_string(nums)
  nums.each_with_index.map { |s, i| s[i] == '0' ? '1' : '0' }.join
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def findDifferentBinaryString(nums: Array[String]): String = {
    nums.indices.map(i => if (nums(i)(i) == '0') '1' else '0').mkString
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        nums.iter()
            .enumerate()
            .map(|(i, s)| if s.as_bytes()[i] == b'0' { '1' } else { '0' })
            .collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-different-binary-string nums)
  (-> (listof string?) string?)
  (list->string
   (for/list ([s (in-list nums)]
              [i (in-naturals)])
     (if (char=? (string-ref s i) #\0) #\1 #\0))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_different_binary_string(Nums :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
find_different_binary_string(Nums) ->
  Helper = fun(Self, [], _, Acc) -> lists:reverse(Acc);
              (Self, [H|T], I, Acc) ->
                Bit = if binary:at(H, I) =:= $0 -> $1; true -> $0 end,
                Self(Self, T, I + 1, [Bit|Acc])
           end,
  list_to_binary(Helper(Helper, Nums, 0, [])).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_different_binary_string(nums :: [String.t]) :: String.t
  def find_different_binary_string(nums) do
    nums
    |> Enum.with_index()
    |> Enum.map(fn {s, i} ->
      if String.at(s, i) == "0", do: "1", else: "0"
    end)
    |> Enum.join()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the number of strings (and the length of each string). We perform a single pass through the list of strings, performing a constant-time character check and assignment at each step.
- **Space Complexity:** O(n) if we consider the space required to store the output string, as we construct a string of length n. The auxiliary space used during the computation is O(1) or O(n) depending on whether the language allows mutable strings or requires a buffer like StringBuilder.
