---
layout: post
title: "Find Smallest Letter Greater Than Target"
date: 2026-01-31 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Binary Search"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    char nextGreatestLetter(vector<char>& letters,\
        \ char target) {\n        int left = 0, right = letters.size() - 1;\n      \
        \  while (left <= right) {\n            int mid = left + (right - left) / 2;\n\
        \            if (letters[mid] <= target) {\n                left = mid + 1;\n\
        \            }\n            else {\n                right = mid - 1;\n     \
        \       }\n        }\n        return letters[left % letters.size()];\n    }\n\
        };"
      java: "class Solution {\n    public char nextGreatestLetter(char[] letters, char\
        \ target) {\n        int left = 0, right = letters.length - 1;\n        while\
        \ (left <= right) {\n            int mid = left + (right - left) / 2;\n    \
        \        if (letters[mid] <= target) {\n                left = mid + 1;\n  \
        \          } else {\n                right = mid - 1;\n            }\n     \
        \   }\n        return letters[left % letters.length];\n    }\n}"
      python: "class Solution(object):\n    def nextGreatestLetter(self, letters, target):\n\
        \        \"\"\"\n        :type letters: List[str]\n        :type target: str\n\
        \        :rtype: str\n        \"\"\"\n        left, right = 0, len(letters)\
        \ - 1\n        while left <= right:\n            mid = left + (right - left)\
        \ // 2\n            if letters[mid] <= target:\n                left = mid +\
        \ 1\n            else:\n                right = mid - 1\n        return letters[left\
        \ % len(letters)]"
      python3: "class Solution:\n    def nextGreatestLetter(self, letters: List[str],\
        \ target: str) -> str:\n        left, right = 0, len(letters) - 1\n        while\
        \ left <= right:\n            mid = left + (right - left) // 2\n           \
        \ if letters[mid] <= target:\n                left = mid + 1\n            else:\n\
        \                right = mid - 1\n        return letters[left % len(letters)]"
      c: "char nextGreatestLetter(char* letters, int lettersSize, char target) {\n \
        \   int left = 0, right = lettersSize - 1;\n    while (left <= right) {\n  \
        \      int mid = left + (right - left) / 2;\n        if (letters[mid] <= target)\
        \ {\n            left = mid + 1;\n        } else {\n            right = mid\
        \ - 1;\n        }\n    }\n    return letters[left % lettersSize];\n}"
      csharp: "public class Solution {\n    public char NextGreatestLetter(char[] letters,\
        \ char target) {\n        int left = 0, right = letters.Length - 1;\n      \
        \  while (left <= right) {\n            int mid = left + (right - left) / 2;\n\
        \            if (letters[mid] <= target) {\n                left = mid + 1;\n\
        \            } else {\n                right = mid - 1;\n            }\n   \
        \     }\n        return letters[left % letters.Length];\n    }\n}"
      javascript: "/**\n * @param {character[]} letters\n * @param {character} target\n\
        \ * @return {character}\n */\nvar nextGreatestLetter = function(letters, target)\
        \ {\n    let left = 0, right = letters.length - 1;\n    while (left <= right)\
        \ {\n        let mid = Math.floor(left + (right - left) / 2);\n        if (letters[mid]\
        \ <= target) {\n            left = mid + 1;\n        } else {\n            right\
        \ = mid - 1;\n        }\n    }\n    return letters[left % letters.length];\n\
        };"
      typescript: "function nextGreatestLetter(letters: string[], target: string): string\
        \ {\n    let low = 0;\n    let high = letters.length - 1;\n    while (low <=\
        \ high) {\n        let mid = Math.floor(low + (high - low) / 2);\n        if\
        \ (letters[mid] > target) {\n            high = mid - 1;\n        } else {\n\
        \            low = mid + 1;\n        }\n    }\n    return letters[low % letters.length];\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param String[] $letters\n     * @param\
        \ String $target\n     * @return String\n     */\n    function nextGreatestLetter($letters,\
        \ $target) {\n        $low = 0;\n        $high = count($letters) - 1;\n    \
        \    while ($low <= $high) {\n            $mid = $low + floor(($high - $low)\
        \ / 2);\n            if ($letters[$mid] > $target) {\n                $high\
        \ = $mid - 1;\n            } else {\n                $low = $mid + 1;\n    \
        \        }\n        }\n        return $letters[$low % count($letters)];\n  \
        \  }\n}"
      swift: "class Solution {\n    func nextGreatestLetter(_ letters: [Character],\
        \ _ target: Character) -> Character {\n        var low = 0\n        var high\
        \ = letters.count - 1\n        while low <= high {\n            let mid = low\
        \ + (high - low) / 2\n            if letters[mid] > target {\n             \
        \   high = mid - 1\n            } else {\n                low = mid + 1\n  \
        \          }\n        }\n        return letters[low % letters.count]\n    }\n\
        }"
      kotlin: "class Solution {\n    fun nextGreatestLetter(letters: CharArray, target:\
        \ Char): Char {\n        var low = 0\n        var high = letters.size - 1\n\
        \        while (low <= high) {\n            val mid = low + (high - low) / 2\n\
        \            if (letters[mid] > target) {\n                high = mid - 1\n\
        \            } else {\n                low = mid + 1\n            }\n      \
        \  }\n        return letters[low % letters.size]\n    }\n}"
      dart: "class Solution {\n  String nextGreatestLetter(List<String> letters, String\
        \ target) {\n    int low = 0;\n    int high = letters.length - 1;\n    while\
        \ (low <= high) {\n      int mid = low + (high - low) ~/ 2;\n      if (letters[mid].compareTo(target)\
        \ > 0) {\n        high = mid - 1;\n      } else {\n        low = mid + 1;\n\
        \      }\n    }\n    return letters[low % letters.length];\n  }\n}"
      go: "func nextGreatestLetter(letters []byte, target byte) byte {\n    low := 0\n\
        \    high := len(letters) - 1\n    for low <= high {\n        mid := low + (high-low)/2\n\
        \        if letters[mid] > target {\n            high = mid - 1\n        } else\
        \ {\n            low = mid + 1\n        }\n    }\n    return letters[low % len(letters)]\n\
        }"
      ruby: "def next_greatest_letter(letters, target)\n  letters.find { |c| c > target\
        \ } || letters[0]\nend"
      scala: "object Solution {\n    def nextGreatestLetter(letters: Array[Char], target:\
        \ Char): Char = {\n        letters.find(_ > target).getOrElse(letters(0))\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn next_greatest_letter(letters: Vec<char>, target:\
        \ char) -> char {\n        *letters.iter().find(|&&c| c > target).unwrap_or(&letters[0])\n\
        \    }\n}"
      racket: "(define/contract (next-greatest-letter letters target)\n  (-> (listof\
        \ char?) char? char?)\n  (let ([found (findf (lambda (c) (char>? c target))\
        \ letters)])\n    (if found found (car letters))))"
      erlang: "next_greatest_letter(Letters, Target) ->\n  case [L || L <- Letters,\
        \ L > Target] of\n    [H | _] -> H;\n    [] -> hd(Letters)\n  end."
      elixir: "defmodule Solution do\n  @spec next_greatest_letter(letters :: [char],\
        \ target :: char) :: char\n  def next_greatest_letter(letters, target) do\n\
        \    Enum.find(letters, hd(letters), fn c -> c > target end)\n  end\nend"
    approach: 'The problem asks for the smallest character strictly greater than the
      target in a sorted array. Since the array is already sorted in non-decreasing
      order, we can efficiently locate the desired character using a binary search algorithm.
      This approach reduces the search space by half in each step. If the middle element
      is less than or equal to the target, we move the search to the right half; otherwise,
      we move to the left, refining our search for the smallest element that exceeds
      the target.


      The wrap-around condition states that if no character in the array is greater
      than the target, we should return the first character. This is elegantly handled
      by the binary search result. If the left boundary index equals the length of the
      array after the loop, it signifies no character was found that is strictly greater
      than the target. Returning the element at index ''left % letters.length'' correctly
      handles both the found case and the wrap-around case.'
    time_complexity: O(log n) where n is the number of characters in the letters array.
      This is because the binary search algorithm divides the search interval in half
      at each step.
    space_complexity: O(1) because the algorithm only requires a few integer variables
      to maintain the search boundaries, regardless of the input size.
    elapsed_time: 84.75881862640381
    model: gemini-3-flash-preview
    generated_at: '2026-01-31 01:18:57 '
---

## Problem #744: Find Smallest Letter Greater Than Target

**Difficulty:** Easy

**Topics:** Array, Binary Search

## Problem Description

<p>You are given an array of characters <code>letters</code> that is sorted in <strong>non-decreasing order</strong>, and a character <code>target</code>. There are <strong>at least two different</strong> characters in <code>letters</code>.</p>

<p>Return <em>the smallest character in </em><code>letters</code><em> that is lexicographically greater than </em><code>target</code>. If such a character does not exist, return the first character in <code>letters</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> letters = [&quot;c&quot;,&quot;f&quot;,&quot;j&quot;], target = &quot;a&quot;
<strong>Output:</strong> &quot;c&quot;
<strong>Explanation:</strong> The smallest character that is lexicographically greater than &#39;a&#39; in letters is &#39;c&#39;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> letters = [&quot;c&quot;,&quot;f&quot;,&quot;j&quot;], target = &quot;c&quot;
<strong>Output:</strong> &quot;f&quot;
<strong>Explanation:</strong> The smallest character that is lexicographically greater than &#39;c&#39; in letters is &#39;f&#39;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> letters = [&quot;x&quot;,&quot;x&quot;,&quot;y&quot;,&quot;y&quot;], target = &quot;z&quot;
<strong>Output:</strong> &quot;x&quot;
<strong>Explanation:</strong> There are no characters in letters that is lexicographically greater than &#39;z&#39; so we return letters[0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= letters.length &lt;= 10<sup>4</sup></code></li>
	<li><code>letters[i]</code> is a lowercase English letter.</li>
	<li><code>letters</code> is sorted in <strong>non-decreasing</strong> order.</li>
	<li><code>letters</code> contains at least two different characters.</li>
	<li><code>target</code> is a lowercase English letter.</li>
</ul>


## Hints

1. Try to find whether each of 26 next letters are in the given string array.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the smallest character strictly greater than the target in a sorted array. Since the array is already sorted in non-decreasing order, we can efficiently locate the desired character using a binary search algorithm. This approach reduces the search space by half in each step. If the middle element is less than or equal to the target, we move the search to the right half; otherwise, we move to the left, refining our search for the smallest element that exceeds the target.

The wrap-around condition states that if no character in the array is greater than the target, we should return the first character. This is elegantly handled by the binary search result. If the left boundary index equals the length of the array after the loop, it signifies no character was found that is strictly greater than the target. Returning the element at index 'left % letters.length' correctly handles both the found case and the wrap-around case.

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
    char nextGreatestLetter(vector<char>& letters, char target) {
        int left = 0, right = letters.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (letters[mid] <= target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return letters[left % letters.size()];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int left = 0, right = letters.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (letters[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return letters[left % letters.length];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left % len(letters)]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left % len(letters)]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
char nextGreatestLetter(char* letters, int lettersSize, char target) {
    int left = 0, right = lettersSize - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (letters[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return letters[left % lettersSize];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public char NextGreatestLetter(char[] letters, char target) {
        int left = 0, right = letters.Length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (letters[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return letters[left % letters.Length];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    let left = 0, right = letters.length - 1;
    while (left <= right) {
        let mid = Math.floor(left + (right - left) / 2);
        if (letters[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return letters[left % letters.length];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function nextGreatestLetter(letters: string[], target: string): string {
    let low = 0;
    let high = letters.length - 1;
    while (low <= high) {
        let mid = Math.floor(low + (high - low) / 2);
        if (letters[mid] > target) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return letters[low % letters.length];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[] $letters
     * @param String $target
     * @return String
     */
    function nextGreatestLetter($letters, $target) {
        $low = 0;
        $high = count($letters) - 1;
        while ($low <= $high) {
            $mid = $low + floor(($high - $low) / 2);
            if ($letters[$mid] > $target) {
                $high = $mid - 1;
            } else {
                $low = $mid + 1;
            }
        }
        return $letters[$low % count($letters)];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func nextGreatestLetter(_ letters: [Character], _ target: Character) -> Character {
        var low = 0
        var high = letters.count - 1
        while low <= high {
            let mid = low + (high - low) / 2
            if letters[mid] > target {
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        return letters[low % letters.count]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun nextGreatestLetter(letters: CharArray, target: Char): Char {
        var low = 0
        var high = letters.size - 1
        while (low <= high) {
            val mid = low + (high - low) / 2
            if (letters[mid] > target) {
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        return letters[low % letters.size]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String nextGreatestLetter(List<String> letters, String target) {
    int low = 0;
    int high = letters.length - 1;
    while (low <= high) {
      int mid = low + (high - low) ~/ 2;
      if (letters[mid].compareTo(target) > 0) {
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }
    return letters[low % letters.length];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func nextGreatestLetter(letters []byte, target byte) byte {
    low := 0
    high := len(letters) - 1
    for low <= high {
        mid := low + (high-low)/2
        if letters[mid] > target {
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    return letters[low % len(letters)]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def next_greatest_letter(letters, target)
  letters.find { |c| c > target } || letters[0]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def nextGreatestLetter(letters: Array[Char], target: Char): Char = {
        letters.find(_ > target).getOrElse(letters(0))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        *letters.iter().find(|&&c| c > target).unwrap_or(&letters[0])
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (next-greatest-letter letters target)
  (-> (listof char?) char? char?)
  (let ([found (findf (lambda (c) (char>? c target)) letters)])
    (if found found (car letters))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
next_greatest_letter(Letters, Target) ->
  case [L || L <- Letters, L > Target] of
    [H | _] -> H;
    [] -> hd(Letters)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec next_greatest_letter(letters :: [char], target :: char) :: char
  def next_greatest_letter(letters, target) do
    Enum.find(letters, hd(letters), fn c -> c > target end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n) where n is the number of characters in the letters array. This is because the binary search algorithm divides the search interval in half at each step.
- **Space Complexity:** O(1) because the algorithm only requires a few integer variables to maintain the search boundaries, regardless of the input size.
