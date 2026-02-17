---
layout: post
title: "Binary Watch"
date: 2026-02-17 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Backtracking", "Bit Manipulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-watch/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<string> readBinaryWatch(int turnedOn)\
        \ {\n        vector<string> result;\n        for (int h = 0; h < 12; ++h) {\n\
        \            for (int m = 0; m < 60; ++m) {\n                if (__builtin_popcount(h)\
        \ + __builtin_popcount(m) == turnedOn) {\n                    result.push_back(to_string(h)\
        \ + (m < 10 ? \":0\" : \":\") + to_string(m));\n                }\n        \
        \    }\n        }\n        return result;\n    }\n};"
      java: "class Solution {\n    public List<String> readBinaryWatch(int turnedOn)\
        \ {\n        List<String> result = new ArrayList<>();\n        for (int h =\
        \ 0; h < 12; h++) {\n            for (int m = 0; m < 60; m++) {\n          \
        \      if (Integer.bitCount(h) + Integer.bitCount(m) == turnedOn) {\n      \
        \              result.add(String.format(\"%d:%02d\", h, m));\n             \
        \   }\n            }\n        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def readBinaryWatch(self, turnedOn):\n \
        \       \"\"\"\n        :type turnedOn: int\n        :rtype: List[str]\n   \
        \     \"\"\"\n        res = []\n        for h in range(12):\n            for\
        \ m in range(60):\n                if (bin(h).count('1') + bin(m).count('1'))\
        \ == turnedOn:\n                    res.append(str(h) + \":\" + str(m).zfill(2))\n\
        \        return res"
      python3: "class Solution:\n    def readBinaryWatch(self, turnedOn: int) -> List[str]:\n\
        \        return [f\"{h}:{m:02d}\" for h in range(12) for m in range(60) \n \
        \               if (bin(h).count('1') + bin(m).count('1')) == turnedOn]"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nchar** readBinaryWatch(int turnedOn, int* returnSize) {\n    char** res\
        \ = (char**)malloc(720 * sizeof(char*));\n    *returnSize = 0;\n    for (int\
        \ h = 0; h < 12; h++) {\n        for (int m = 0; m < 60; m++) {\n          \
        \  int count = 0;\n            int n = h;\n            while (n > 0) { count\
        \ += (n & 1); n >>= 1; }\n            n = m;\n            while (n > 0) { count\
        \ += (n & 1); n >>= 1; }\n            if (count == turnedOn) {\n           \
        \     res[*returnSize] = (char*)malloc(6 * sizeof(char));\n                sprintf(res[*returnSize],\
        \ \"%d:%02d\", h, m);\n                (*returnSize)++;\n            }\n   \
        \     }\n    }\n    return res;\n}"
      csharp: "public class Solution {\n    public IList<string> ReadBinaryWatch(int\
        \ turnedOn) {\n        List<string> result = new List<string>();\n        for\
        \ (int h = 0; h < 12; h++) {\n            for (int m = 0; m < 60; m++) {\n \
        \               if (CountSetBits(h) + CountSetBits(m) == turnedOn) {\n     \
        \               result.Add(string.Format(\"{0}:{1:D2}\", h, m));\n         \
        \       }\n            }\n        }\n        return result;\n    }\n\n    private\
        \ int CountSetBits(int n) {\n        int count = 0;\n        while (n > 0) {\n\
        \            n &= (n - 1);\n            count++;\n        }\n        return\
        \ count;\n    }\n}"
      javascript: "/**\n * @param {number} turnedOn\n * @return {string[]}\n */\nvar\
        \ readBinaryWatch = function(turnedOn) {\n    const result = [];\n    const\
        \ countBits = (num) => {\n        let count = 0;\n        while (num > 0) {\n\
        \            count += num & 1;\n            num >>= 1;\n        }\n        return\
        \ count;\n    };\n    for (let h = 0; h < 12; h++) {\n        for (let m = 0;\
        \ m < 60; m++) {\n            if (countBits(h) + countBits(m) === turnedOn)\
        \ {\n                result.push(`${h}:${m < 10 ? '0' + m : m}`);\n        \
        \    }\n        }\n    }\n    return result;\n};"
      typescript: "function readBinaryWatch(turnedOn: number): string[] {\n    const\
        \ countBits = (n: number): number => {\n        let count = 0;\n        while\
        \ (n > 0) {\n            n &= (n - 1);\n            count++;\n        }\n  \
        \      return count;\n    };\n    const res: string[] = [];\n    for (let h\
        \ = 0; h < 12; h++) {\n        for (let m = 0; m < 60; m++) {\n            if\
        \ (countBits(h) + countBits(m) === turnedOn) {\n                res.push(h +\
        \ \":\" + (m < 10 ? \"0\" : \"\") + m);\n            }\n        }\n    }\n \
        \   return res;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $turnedOn\n     * @return\
        \ String[]\n     */\n    function readBinaryWatch($turnedOn) {\n        $res\
        \ = [];\n        for ($h = 0; $h < 12; $h++) {\n            for ($m = 0; $m\
        \ < 60; $m++) {\n                if (substr_count(decbin($h), '1') + substr_count(decbin($m),\
        \ '1') === $turnedOn) {\n                    $res[] = sprintf(\"%d:%02d\", $h,\
        \ $m);\n                }\n            }\n        }\n        return $res;\n\
        \    }\n}"
      swift: "class Solution {\n    func readBinaryWatch(_ turnedOn: Int) -> [String]\
        \ {\n        var res = [String]()\n        for h in 0..<12 {\n            for\
        \ m in 0..<60 {\n                if h.nonzeroBitCount + m.nonzeroBitCount ==\
        \ turnedOn {\n                    let mm = m < 10 ? \"0\" + String(m) : String(m)\n\
        \                    res.append(String(h) + \":\" + mm)\n                }\n\
        \            }\n        }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun readBinaryWatch(turnedOn: Int): List<String>\
        \ {\n        val res = mutableListOf<String>()\n        for (h in 0 until 12)\
        \ {\n            for (m in 0 until 60) {\n                if (Integer.bitCount(h)\
        \ + Integer.bitCount(m) == turnedOn) {\n                    res.add(h.toString()\
        \ + \":\" + (if (m < 10) \"0\" + m else m.toString()))\n                }\n\
        \            }\n        }\n        return res\n    }\n}"
      dart: "class Solution {\n  List<String> readBinaryWatch(int turnedOn) {\n    List<String>\
        \ res = [];\n    for (int h = 0; h < 12; h++) {\n      for (int m = 0; m < 60;\
        \ m++) {\n        if (_countBits(h) + _countBits(m) == turnedOn) {\n       \
        \   res.add(h.toString() + \":\" + (m < 10 ? \"0\" : \"\") + m.toString());\n\
        \        }\n      }\n    }\n    return res;\n  }\n\n  int _countBits(int n)\
        \ {\n    int count = 0;\n    while (n > 0) {\n      n &= (n - 1);\n      count++;\n\
        \    }\n    return count;\n  }\n}"
      go: "import (\n    \"fmt\"\n    \"math/bits\"\n)\n\nfunc readBinaryWatch(turnedOn\
        \ int) []string {\n    res := []string{}\n    for h := 0; h < 12; h++ {\n  \
        \      for m := 0; m < 60; m++ {\n            if bits.OnesCount(uint(h)) + bits.OnesCount(uint(m))\
        \ == turnedOn {\n                res = append(res, fmt.Sprintf(\"%d:%02d\",\
        \ h, m))\n            }\n        }\n    }\n    return res\n}"
      ruby: "def read_binary_watch(turned_on)\n  (0..11).each_with_object([]) do |h,\
        \ res|\n    (0..59).each do |m|\n      if (h.to_s(2).count('1') + m.to_s(2).count('1'))\
        \ == turned_on\n        res << \"%d:%02d\" % [h, m]\n      end\n    end\n  end\n\
        end"
      scala: "object Solution {\n  def readBinaryWatch(turnedOn: Int): List[String]\
        \ = {\n    (for {\n      h <- 0 until 12\n      m <- 0 until 60\n      if Integer.bitCount(h)\
        \ + Integer.bitCount(m) == turnedOn\n    } yield f\"$h%d:$m%02d\").toList\n\
        \  }\n}"
      rust: "impl Solution {\n    pub fn read_binary_watch(turned_on: i32) -> Vec<String>\
        \ {\n        let mut res = Vec::new();\n        for h in 0..12 {\n         \
        \   for m in 0..60 {\n                if (h as u32).count_ones() + (m as u32).count_ones()\
        \ == turned_on as u32 {\n                    res.push(format!(\"{}:{:02}\",\
        \ h, m));\n                }\n            }\n        }\n        res\n    }\n\
        }"
      racket: "(define/contract (read-binary-watch turnedOn)\n  (-> exact-integer? (listof\
        \ string?))\n  (for*/list ([h (in-range 12)]\n              [m (in-range 60)]\n\
        \              #:when (= (+ (bitwise-bit-count h) (bitwise-bit-count m)) turnedOn))\n\
        \    (format \"~a:~a~a\" h (if (< m 10) \"0\" \"\") m)))"
      erlang: "read_binary_watch(TurnedOn) ->\n  CountBits = fun(N) -> length([X ||\
        \ X <- integer_to_list(N, 2), X == $1]) end,\n  [list_to_binary(io_lib:format(\"\
        ~w:~s~w\", [H, if M < 10 -> \"0\"; true -> \"\" end, M])) || \n   H <- lists:seq(0,\
        \ 11), \n   M <- lists:seq(0, 59), \n   CountBits(H) + CountBits(M) =:= TurnedOn]."
      elixir: "defmodule Solution do\n  @spec read_binary_watch(turned_on :: integer)\
        \ :: [String.t]\n  def read_binary_watch(turned_on) do\n    for h <- 0..11,\n\
        \        m <- 0..59,\n        Integer.popcount(h) + Integer.popcount(m) == turned_on\
        \ do\n      \"#{h}:#{String.pad_leading(Integer.to_string(m), 2, \"0\")}\"\n\
        \    end\n  end\nend"
    approach: 'The algorithm employs a brute-force approach by traversing every possible
      valid time on a binary watch. Since there are only 12 hours (0-11) and 60 minutes
      (0-59), a nested loop can efficiently evaluate all 720 combinations. For each
      combination, we calculate the number of set bits (representing turned-on LEDs)
      in both the hour and minute values using built-in bit-counting functions or manual
      bit manipulation.


      If the total number of set bits matches the target value ''turnedOn'', the hour
      and minute are formatted into a string following specific rules: no leading zero
      for hours and a two-digit format with a leading zero for minutes. This exhaustive
      search is feasible because the search space is small and constant, ensuring a
      fast and consistent execution time regardless of the input value.'
    time_complexity: O(1) with one-paragraph explanation. The algorithm iterates through
      a fixed number of combinations (12 hours and 60 minutes), resulting in exactly
      720 iterations. Since the search space is independent of the input size, the time
      complexity is constant.
    space_complexity: O(1) with one-paragraph explanation. The amount of extra space
      used for the logic does not scale with the input. While the output array stores
      valid time strings, the maximum number of such strings is bounded by the fixed
      720 possible time combinations.
    elapsed_time: 200.22509121894836
    model: gemini-3-flash-preview
    generated_at: '2026-02-17 01:28:05 '
---

## Problem #401: Binary Watch

**Difficulty:** Easy

**Topics:** Backtracking, Bit Manipulation

## Problem Description

<p>A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent&nbsp;the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.</p>

<ul>
	<li>For example, the below binary watch reads <code>&quot;4:51&quot;</code>.</li>
</ul>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/binarywatch.jpg" style="width: 500px; height: 500px;" /></p>

<p>Given an integer <code>turnedOn</code> which represents the number of LEDs that are currently on (ignoring the PM), return <em>all possible times the watch could represent</em>. You may return the answer in <strong>any order</strong>.</p>

<p>The hour must not contain a leading zero.</p>

<ul>
	<li>For example, <code>&quot;01:00&quot;</code> is not valid. It should be <code>&quot;1:00&quot;</code>.</li>
</ul>

<p>The minute must&nbsp;consist of two digits and may contain a leading zero.</p>

<ul>
	<li>For example, <code>&quot;10:2&quot;</code> is not valid. It should be <code>&quot;10:02&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> turnedOn = 1
<strong>Output:</strong> ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> turnedOn = 9
<strong>Output:</strong> []
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= turnedOn &lt;= 10</code></li>
</ul>


## Hints

1. Simplify by seeking for solutions that involve comparing bit counts.

2. Consider calculating all possible times for comparison purposes.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a brute-force approach by traversing every possible valid time on a binary watch. Since there are only 12 hours (0-11) and 60 minutes (0-59), a nested loop can efficiently evaluate all 720 combinations. For each combination, we calculate the number of set bits (representing turned-on LEDs) in both the hour and minute values using built-in bit-counting functions or manual bit manipulation.

If the total number of set bits matches the target value 'turnedOn', the hour and minute are formatted into a string following specific rules: no leading zero for hours and a two-digit format with a leading zero for minutes. This exhaustive search is feasible because the search space is small and constant, ensuring a fast and consistent execution time regardless of the input value.

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
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> result;
        for (int h = 0; h < 12; ++h) {
            for (int m = 0; m < 60; ++m) {
                if (__builtin_popcount(h) + __builtin_popcount(m) == turnedOn) {
                    result.push_back(to_string(h) + (m < 10 ? ":0" : ":") + to_string(m));
                }
            }
        }
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public List<String> readBinaryWatch(int turnedOn) {
        List<String> result = new ArrayList<>();
        for (int h = 0; h < 12; h++) {
            for (int m = 0; m < 60; m++) {
                if (Integer.bitCount(h) + Integer.bitCount(m) == turnedOn) {
                    result.add(String.format("%d:%02d", h, m));
                }
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    res.append(str(h) + ":" + str(m).zfill(2))
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return [f"{h}:{m:02d}" for h in range(12) for m in range(60) 
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** readBinaryWatch(int turnedOn, int* returnSize) {
    char** res = (char**)malloc(720 * sizeof(char*));
    *returnSize = 0;
    for (int h = 0; h < 12; h++) {
        for (int m = 0; m < 60; m++) {
            int count = 0;
            int n = h;
            while (n > 0) { count += (n & 1); n >>= 1; }
            n = m;
            while (n > 0) { count += (n & 1); n >>= 1; }
            if (count == turnedOn) {
                res[*returnSize] = (char*)malloc(6 * sizeof(char));
                sprintf(res[*returnSize], "%d:%02d", h, m);
                (*returnSize)++;
            }
        }
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public IList<string> ReadBinaryWatch(int turnedOn) {
        List<string> result = new List<string>();
        for (int h = 0; h < 12; h++) {
            for (int m = 0; m < 60; m++) {
                if (CountSetBits(h) + CountSetBits(m) == turnedOn) {
                    result.Add(string.Format("{0}:{1:D2}", h, m));
                }
            }
        }
        return result;
    }

    private int CountSetBits(int n) {
        int count = 0;
        while (n > 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} turnedOn
 * @return {string[]}
 */
var readBinaryWatch = function(turnedOn) {
    const result = [];
    const countBits = (num) => {
        let count = 0;
        while (num > 0) {
            count += num & 1;
            num >>= 1;
        }
        return count;
    };
    for (let h = 0; h < 12; h++) {
        for (let m = 0; m < 60; m++) {
            if (countBits(h) + countBits(m) === turnedOn) {
                result.push(`${h}:${m < 10 ? '0' + m : m}`);
            }
        }
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function readBinaryWatch(turnedOn: number): string[] {
    const countBits = (n: number): number => {
        let count = 0;
        while (n > 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    };
    const res: string[] = [];
    for (let h = 0; h < 12; h++) {
        for (let m = 0; m < 60; m++) {
            if (countBits(h) + countBits(m) === turnedOn) {
                res.push(h + ":" + (m < 10 ? "0" : "") + m);
            }
        }
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $turnedOn
     * @return String[]
     */
    function readBinaryWatch($turnedOn) {
        $res = [];
        for ($h = 0; $h < 12; $h++) {
            for ($m = 0; $m < 60; $m++) {
                if (substr_count(decbin($h), '1') + substr_count(decbin($m), '1') === $turnedOn) {
                    $res[] = sprintf("%d:%02d", $h, $m);
                }
            }
        }
        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func readBinaryWatch(_ turnedOn: Int) -> [String] {
        var res = [String]()
        for h in 0..<12 {
            for m in 0..<60 {
                if h.nonzeroBitCount + m.nonzeroBitCount == turnedOn {
                    let mm = m < 10 ? "0" + String(m) : String(m)
                    res.append(String(h) + ":" + mm)
                }
            }
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun readBinaryWatch(turnedOn: Int): List<String> {
        val res = mutableListOf<String>()
        for (h in 0 until 12) {
            for (m in 0 until 60) {
                if (Integer.bitCount(h) + Integer.bitCount(m) == turnedOn) {
                    res.add(h.toString() + ":" + (if (m < 10) "0" + m else m.toString()))
                }
            }
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<String> readBinaryWatch(int turnedOn) {
    List<String> res = [];
    for (int h = 0; h < 12; h++) {
      for (int m = 0; m < 60; m++) {
        if (_countBits(h) + _countBits(m) == turnedOn) {
          res.add(h.toString() + ":" + (m < 10 ? "0" : "") + m.toString());
        }
      }
    }
    return res;
  }

  int _countBits(int n) {
    int count = 0;
    while (n > 0) {
      n &= (n - 1);
      count++;
    }
    return count;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
    "fmt"
    "math/bits"
)

func readBinaryWatch(turnedOn int) []string {
    res := []string{}
    for h := 0; h < 12; h++ {
        for m := 0; m < 60; m++ {
            if bits.OnesCount(uint(h)) + bits.OnesCount(uint(m)) == turnedOn {
                res = append(res, fmt.Sprintf("%d:%02d", h, m))
            }
        }
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def read_binary_watch(turned_on)
  (0..11).each_with_object([]) do |h, res|
    (0..59).each do |m|
      if (h.to_s(2).count('1') + m.to_s(2).count('1')) == turned_on
        res << "%d:%02d" % [h, m]
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def readBinaryWatch(turnedOn: Int): List[String] = {
    (for {
      h <- 0 until 12
      m <- 0 until 60
      if Integer.bitCount(h) + Integer.bitCount(m) == turnedOn
    } yield f"$h%d:$m%02d").toList
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        let mut res = Vec::new();
        for h in 0..12 {
            for m in 0..60 {
                if (h as u32).count_ones() + (m as u32).count_ones() == turned_on as u32 {
                    res.push(format!("{}:{:02}", h, m));
                }
            }
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (read-binary-watch turnedOn)
  (-> exact-integer? (listof string?))
  (for*/list ([h (in-range 12)]
              [m (in-range 60)]
              #:when (= (+ (bitwise-bit-count h) (bitwise-bit-count m)) turnedOn))
    (format "~a:~a~a" h (if (< m 10) "0" "") m)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
read_binary_watch(TurnedOn) ->
  CountBits = fun(N) -> length([X || X <- integer_to_list(N, 2), X == $1]) end,
  [list_to_binary(io_lib:format("~w:~s~w", [H, if M < 10 -> "0"; true -> "" end, M])) || 
   H <- lists:seq(0, 11), 
   M <- lists:seq(0, 59), 
   CountBits(H) + CountBits(M) =:= TurnedOn].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec read_binary_watch(turned_on :: integer) :: [String.t]
  def read_binary_watch(turned_on) do
    for h <- 0..11,
        m <- 0..59,
        Integer.popcount(h) + Integer.popcount(m) == turned_on do
      "#{h}:#{String.pad_leading(Integer.to_string(m), 2, "0")}"
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1) with one-paragraph explanation. The algorithm iterates through a fixed number of combinations (12 hours and 60 minutes), resulting in exactly 720 iterations. Since the search space is independent of the input size, the time complexity is constant.
- **Space Complexity:** O(1) with one-paragraph explanation. The amount of extra space used for the logic does not scale with the input. While the output array stores valid time strings, the maximum number of such strings is bounded by the fixed 720 possible time combinations.
