---
layout: post
title: "Unique Length-3 Palindromic Subsequences"
date: 2025-11-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String", "Bit Manipulation", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
---

## Problem #1930: Unique Length-3 Palindromic Subsequences

**Difficulty:** Medium

**Topics:** Hash Table, String, Bit Manipulation, Prefix Sum

## Problem Description

<p>Given a string <code>s</code>, return <em>the number of <strong>unique palindromes of length three</strong> that are a <strong>subsequence</strong> of </em><code>s</code>.</p>

<p>Note that even if there are multiple ways to obtain the same subsequence, it is still only counted <strong>once</strong>.</p>

<p>A <strong>palindrome</strong> is a string that reads the same forwards and backwards.</p>

<p>A <strong>subsequence</strong> of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.</p>

<ul>
	<li>For example, <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;<u>a</u>b<u>c</u>d<u>e</u>&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabca&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The 3 palindromic subsequences of length 3 are:
- &quot;aba&quot; (subsequence of &quot;<u>a</u>a<u>b</u>c<u>a</u>&quot;)
- &quot;aaa&quot; (subsequence of &quot;<u>aa</u>bc<u>a</u>&quot;)
- &quot;aca&quot; (subsequence of &quot;<u>a</u>ab<u>ca</u>&quot;)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;adc&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no palindromic subsequences of length 3 in &quot;adc&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbcbaba&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The 4 palindromic subsequences of length 3 are:
- &quot;bbb&quot; (subsequence of &quot;<u>bb</u>c<u>b</u>aba&quot;)
- &quot;bcb&quot; (subsequence of &quot;<u>b</u>b<u>cb</u>aba&quot;)
- &quot;bab&quot; (subsequence of &quot;<u>b</u>bcb<u>ab</u>a&quot;)
- &quot;aba&quot; (subsequence of &quot;bbcb<u>aba</u>&quot;)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>


## Hints

1. What is the maximum number of length-3 palindromic strings?

2. How can we keep track of the characters that appeared to the left of a given position?

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-24 07:41:33 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count the number of unique palindromic subsequences of length three. A length-3 palindrome has the form 'char1 + char2 + char1'. For example, 'aba', 'aca', 'bbb'. There are 26 possible choices for 'char1' (from 'a' to 'z') and 26 possible choices for 'char2' (also 'a' to 'z'), meaning there are at most 26 * 26 = 676 unique length-3 palindromes. This relatively small upper bound suggests that we can iterate through possible 'char1' values.

The core idea is to iterate through each possible character 'c' from 'a' to 'z' that could serve as 'char1'. For each such 'c', we need to find its first occurrence index (let's call it `first_idx`) and its last occurrence index (let's call it `last_idx`) in the input string `s`. If 'c' does not appear in `s`, or if it appears only once (i.e., `first_idx == last_idx`), then we cannot form a palindrome `c_c` because there's no character to place in the middle. If `first_idx < last_idx`, it means there are at least two occurrences of 'c' with other characters potentially in between them.

Once we have `first_idx` and `last_idx` for a character 'c', any character `s[k]` where `first_idx < k < last_idx` can serve as the middle character ('char2') to form the palindrome `c + s[k] + c`. To count unique palindromes, we need to find all unique characters present in the substring `s[first_idx + 1 : last_idx]`. We collect these unique middle characters into a set. The size of this set gives us the number of unique palindromes that start and end with 'c'. We sum these counts for all possible 'c' to get the final answer.

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
    int countPalindromicSubsequence(std::string s) {
        std::vector<int> first_occurrence(26, -1);
        std::vector<int> last_occurrence(26, -1);

        for (int i = 0; i < s.length(); ++i) {
            int char_idx = s[i] - 'a';
            if (first_occurrence[char_idx] == -1) {
                first_occurrence[char_idx] = i;
            }
            last_occurrence[char_idx] = i;
        }

        int total_unique_palindromes = 0;
        for (int i = 0; i < 26; ++i) {
            int f_idx = first_occurrence[i];
            int l_idx = last_occurrence[i];

            if (f_idx != -1 && f_idx < l_idx) {
                std::set<char> unique_middle_chars;
                for (int j = f_idx + 1; j < l_idx; ++j) {
                    unique_middle_chars.insert(s[j]);
                }
                total_unique_palindromes += unique_middle_chars.size();
            }
        }

        return total_unique_palindromes;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countPalindromicSubsequence(String s) {
        int[] firstOccurrence = new int[26];
        Arrays.fill(firstOccurrence, -1);
        int[] lastOccurrence = new int[26];
        Arrays.fill(lastOccurrence, -1);

        for (int i = 0; i < s.length(); ++i) {
            int charIdx = s.charAt(i) - 'a';
            if (firstOccurrence[charIdx] == -1) {
                firstOccurrence[charIdx] = i;
            }
            lastOccurrence[charIdx] = i;
        }

        int totalUniquePalindromes = 0;
        for (int i = 0; i < 26; ++i) {
            int fIdx = firstOccurrence[i];
            int lIdx = lastOccurrence[i];

            if (fIdx != -1 && fIdx < lIdx) {
                Set<Character> uniqueMiddleChars = new HashSet<>();
                for (int j = fIdx + 1; j < lIdx; ++j) {
                    uniqueMiddleChars.add(s.charAt(j));
                }
                totalUniquePalindromes += uniqueMiddleChars.size();
            }
        }

        return totalUniquePalindromes;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurrence = [-1] * 26
        last_occurrence = [-1] * 26

        for i, char_code in enumerate(s):
            char_idx = ord(char_code) - ord('a')
            if first_occurrence[char_idx] == -1:
                first_occurrence[char_idx] = i
            last_occurrence[char_idx] = i

        total_unique_palindromes = 0
        for i in range(26):
            f_idx = first_occurrence[i]
            l_idx = last_occurrence[i]

            if f_idx != -1 and f_idx < l_idx:
                unique_middle_chars = set()
                for j in range(f_idx + 1, l_idx):
                    unique_middle_chars.add(s[j])
                total_unique_palindromes += len(unique_middle_chars)

        return total_unique_palindromes
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurrence = [-1] * 26
        last_occurrence = [-1] * 26

        for i, char_code in enumerate(s):
            char_idx = ord(char_code) - ord('a')
            if first_occurrence[char_idx] == -1:
                first_occurrence[char_idx] = i
            last_occurrence[char_idx] = i

        total_unique_palindromes = 0
        for i in range(26):
            f_idx = first_occurrence[i]
            l_idx = last_occurrence[i]

            if f_idx != -1 and f_idx < l_idx:
                unique_middle_chars = set()
                for j in range(f_idx + 1, l_idx):
                    unique_middle_chars.add(s[j])
                total_unique_palindromes += len(unique_middle_chars)

        return total_unique_palindromes
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

int countPalindromicSubsequence(char * s) {
    int first_occurrence[26];
    int last_occurrence[26];

    for (int i = 0; i < 26; ++i) {
        first_occurrence[i] = -1;
        last_occurrence[i] = -1;
    }

    int n = strlen(s);
    for (int i = 0; i < n; ++i) {
        int char_idx = s[i] - 'a';
        if (first_occurrence[char_idx] == -1) {
            first_occurrence[char_idx] = i;
        }
        last_occurrence[char_idx] = i;
    }

    int total_unique_palindromes = 0;
    for (int i = 0; i < 26; ++i) {
        int f_idx = first_occurrence[i];
        int l_idx = last_occurrence[i];

        if (f_idx != -1 && f_idx < l_idx) {
            bool unique_middle_chars[26] = {false};
            int count_middle = 0;
            for (int j = f_idx + 1; j < l_idx; ++j) {
                int middle_char_idx = s[j] - 'a';
                if (!unique_middle_chars[middle_char_idx]) {
                    unique_middle_chars[middle_char_idx] = true;
                    count_middle++;
                }
            }
            total_unique_palindromes += count_middle;
        }
    }

    return total_unique_palindromes;
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
    public int CountPalindromicSubsequence(string s) {
        int[] firstOccurrence = new int[26];
        Array.Fill(firstOccurrence, -1);
        int[] lastOccurrence = new int[26];
        Array.Fill(lastOccurrence, -1);

        for (int i = 0; i < s.Length; ++i) {
            int charIdx = s[i] - 'a';
            if (firstOccurrence[charIdx] == -1) {
                firstOccurrence[charIdx] = i;
            }
            lastOccurrence[charIdx] = i;
        }

        int totalUniquePalindromes = 0;
        for (int i = 0; i < 26; ++i) {
            int fIdx = firstOccurrence[i];
            int lIdx = lastOccurrence[i];

            if (fIdx != -1 && fIdx < lIdx) {
                HashSet<char> uniqueMiddleChars = new HashSet<char>();
                for (int j = fIdx + 1; j < lIdx; ++j) {
                    uniqueMiddleChars.Add(s[j]);
                }
                totalUniquePalindromes += uniqueMiddleChars.Count;
            }
        }

        return totalUniquePalindromes;
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
var countPalindromicSubsequence = function(s) {
    const firstOccurrence = new Array(26).fill(-1);
    const lastOccurrence = new Array(26).fill(-1);

    for (let i = 0; i < s.length; ++i) {
        const charIdx = s.charCodeAt(i) - 'a'.charCodeAt(0);
        if (firstOccurrence[charIdx] === -1) {
            firstOccurrence[charIdx] = i;
        }
        lastOccurrence[charIdx] = i;
    }

    let totalUniquePalindromes = 0;
    for (let i = 0; i < 26; ++i) {
        const fIdx = firstOccurrence[i];
        const lIdx = lastOccurrence[i];

        if (fIdx !== -1 && fIdx < lIdx) {
            const uniqueMiddleChars = new Set();
            for (let j = fIdx + 1; j < lIdx; ++j) {
                uniqueMiddleChars.add(s[j]);
            }
            totalUniquePalindromes += uniqueMiddleChars.size;
        }
    }

    return totalUniquePalindromes;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countPalindromicSubsequence(s: string): number {
    const firstOccurrence: number[] = new Array(26).fill(-1);
    const lastOccurrence: number[] = new Array(26).fill(-1);

    for (let i = 0; i < s.length; ++i) {
        const charIdx = s.charCodeAt(i) - 'a'.charCodeAt(0);
        if (firstOccurrence[charIdx] === -1) {
            firstOccurrence[charIdx] = i;
        }
        lastOccurrence[charIdx] = i;
    }

    let totalUniquePalindromes = 0;
    for (let i = 0; i < 26; ++i) {
        const fIdx = firstOccurrence[i];
        const lIdx = lastOccurrence[i];

        if (fIdx !== -1 && fIdx < lIdx) {
            const uniqueMiddleChars: Set<string> = new Set();
            for (let j = fIdx + 1; j < lIdx; ++j) {
                uniqueMiddleChars.add(s[j]);
            }
            totalUniquePalindromes += uniqueMiddleChars.size;
        }
    }

    return totalUniquePalindromes;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function countPalindromicSubsequence($s) {
        $firstOccurrence = array_fill(0, 26, -1);
        $lastOccurrence = array_fill(0, 26, -1);

        $n = strlen($s);
        for ($i = 0; $i < $n; ++$i) {
            $charIdx = ord($s[$i]) - ord('a');
            if ($firstOccurrence[$charIdx] == -1) {
                $firstOccurrence[$charIdx] = $i;
            }
            $lastOccurrence[$charIdx] = $i;
        }

        $totalUniquePalindromes = 0;
        for ($i = 0; $i < 26; ++$i) {
            $fIdx = $firstOccurrence[$i];
            $lIdx = $lastOccurrence[$i];

            if ($fIdx != -1 && $fIdx < $lIdx) {
                $uniqueMiddleChars = [];
                for ($j = $fIdx + 1; $j < $lIdx; ++$j) {
                    $uniqueMiddleChars[$s[$j]] = true;
                }
                $totalUniquePalindromes += count($uniqueMiddleChars);
            }
        }

        return $totalUniquePalindromes;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func countPalindromicSubsequence(_ s: String) -> Int {
        var firstOccurrence = Array(repeating: -1, count: 26)
        var lastOccurrence = Array(repeating: -1, count: 26)

        for (i, char) in s.enumerated() {
            let charIdx = Int(char.asciiValue! - Character("a").asciiValue!)
            if firstOccurrence[charIdx] == -1 {
                firstOccurrence[charIdx] = i
            }
            lastOccurrence[charIdx] = i
        }

        var totalUniquePalindromes = 0
        let sChars = Array(s)
        for i in 0..<26 {
            let fIdx = firstOccurrence[i]
            let lIdx = lastOccurrence[i]

            if fIdx != -1 && fIdx < lIdx {
                var uniqueMiddleChars = Set<Character>()
                for j in (fIdx + 1)..<lIdx {
                    uniqueMiddleChars.insert(sChars[j])
                }
                totalUniquePalindromes += uniqueMiddleChars.count
            }
        }

        return totalUniquePalindromes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countPalindromicSubsequence(s: String): Int {
        val firstOccurrence = IntArray(26) { -1 }
        val lastOccurrence = IntArray(26) { -1 }

        s.forEachIndexed { i, char ->
            val charIdx = char - 'a'
            if (firstOccurrence[charIdx] == -1) {
                firstOccurrence[charIdx] = i
            }
            lastOccurrence[charIdx] = i
        }

        var totalUniquePalindromes = 0
        for (i in 0 until 26) {
            val fIdx = firstOccurrence[i]
            val lIdx = lastOccurrence[i]

            if (fIdx != -1 && fIdx < lIdx) {
                val uniqueMiddleChars = HashSet<Char>()
                for (j in fIdx + 1 until lIdx) {
                    uniqueMiddleChars.add(s[j])
                }
                totalUniquePalindromes += uniqueMiddleChars.size
            }
        }

        return totalUniquePalindromes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class Solution {
  int countPalindromicSubsequence(String s) {
    List<int> firstOccurrence = List.filled(26, -1);
    List<int> lastOccurrence = List.filled(26, -1);

    for (int i = 0; i < s.length; ++i) {
      int charIdx = s.codeUnitAt(i) - 'a'.codeUnitAt(0);
      if (firstOccurrence[charIdx] == -1) {
        firstOccurrence[charIdx] = i;
      }
      lastOccurrence[charIdx] = i;
    }

    int totalUniquePalindromes = 0;
    for (int i = 0; i < 26; ++i) {
      int fIdx = firstOccurrence[i];
      int lIdx = lastOccurrence[i];

      if (fIdx != -1 && fIdx < lIdx) {
        Set<String> uniqueMiddleChars = HashSet<String>();
        for (int j = fIdx + 1; j < lIdx; ++j) {
          uniqueMiddleChars.add(s[j]);
        }
        totalUniquePalindromes += uniqueMiddleChars.length;
      }
    }

    return totalUniquePalindromes;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"strings"
)

func countPalindromicSubsequence(s string) int {
    firstOccurrence := make([]int, 26)
    lastOccurrence := make([]int, 26)

    for i := 0; i < 26; i++ {
        firstOccurrence[i] = -1
        lastOccurrence[i] = -1
    }

    for i, char := range s {
        charIdx := int(char - 'a')
        if firstOccurrence[charIdx] == -1 {
            firstOccurrence[charIdx] = i
        }
        lastOccurrence[charIdx] = i
    }

    totalUniquePalindromes := 0
    for i := 0; i < 26; i++ {
        fIdx := firstOccurrence[i]
        lIdx := lastOccurrence[i]

        if fIdx != -1 && fIdx < lIdx {
            uniqueMiddleChars := make(map[rune]bool)
            for j := fIdx + 1; j < lIdx; j++ {
                uniqueMiddleChars[rune(s[j])] = true
            }
            totalUniquePalindromes += len(uniqueMiddleChars)
        }
    }

    return totalUniquePalindromes
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
require 'set'

class Solution
    def countPalindromicSubsequence(s)
        first_occurrence = Array.new(26, -1)
        last_occurrence = Array.new(26, -1)

        s.each_char.with_index do |char, i|
            char_idx = char.ord - 'a'.ord
            if first_occurrence[char_idx] == -1
                first_occurrence[char_idx] = i
            end
            last_occurrence[char_idx] = i
        end

        total_unique_palindromes = 0
        (0...26).each do |i|
            f_idx = first_occurrence[i]
            l_idx = last_occurrence[i]

            if f_idx != -1 && f_idx < l_idx
                unique_middle_chars = Set.new
                (f_idx + 1...l_idx).each do |j|
                    unique_middle_chars.add(s[j])
                end
                total_unique_palindromes += unique_middle_chars.size
            end
        end

        total_unique_palindromes
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
    def countPalindromicSubsequence(s: String): Int = {
        val firstOccurrence = Array.fill(26)(-1)
        val lastOccurrence = Array.fill(26)(-1)

        s.zipWithIndex.foreach { case (char, i) =>
            val charIdx = char - 'a'
            if (firstOccurrence(charIdx) == -1) {
                firstOccurrence(charIdx) = i
            }
            lastOccurrence(charIdx) = i
        }

        var totalUniquePalindromes = 0
        for (i <- 0 until 26) {
            val fIdx = firstOccurrence(i)
            val lIdx = lastOccurrence(i)

            if (fIdx != -1 && fIdx < lIdx) {
                val uniqueMiddleChars = mutable.Set[Char]()
                for (j <- fIdx + 1 until lIdx) {
                    uniqueMiddleChars.add(s(j))
                }
                totalUniquePalindromes += uniqueMiddleChars.size
            }
        }

        totalUniquePalindromes
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
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let mut first_occurrence = vec![-1; 26];
        let mut last_occurrence = vec![-1; 26];

        for (i, char) in s.chars().enumerate() {
            let char_idx = (char as u8 - b'a') as usize;
            if first_occurrence[char_idx] == -1 {
                first_occurrence[char_idx] = i as i32;
            }
            last_occurrence[char_idx] = i as i32;
        }

        let mut total_unique_palindromes = 0;
        let s_bytes = s.as_bytes();

        for i in 0..26 {
            let f_idx = first_occurrence[i];
            let l_idx = last_occurrence[i];

            if f_idx != -1 && f_idx < l_idx {
                let mut unique_middle_chars = HashSet::new();
                for j in (f_idx + 1) as usize .. l_idx as usize {
                    unique_middle_chars.insert(s_bytes[j]);
                }
                total_unique_palindromes += unique_middle_chars.len() as i32;
            }
        }

        total_unique_palindromes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (count-palindromic-subsequence s)
  (define first-occurrence (make-vector 26 -1))
  (define last-occurrence (make-vector 26 -1))

  (for ([i (in-range (string-length s))])
    (define char-idx (- (char->integer (string-ref s i)) (char->integer #\a)))
    (when (= (vector-ref first-occurrence char-idx) -1)
      (vector-set! first-occurrence char-idx i))
    (vector-set! last-occurrence char-idx i))

  (define total-unique-palindromes 0)
  (for ([i (in-range 26)])
    (define f-idx (vector-ref first-occurrence i))
    (define l-idx (vector-ref last-occurrence i))

    (when (and (!= f-idx -1) (< f-idx l-idx))
      (define unique-middle-chars (make-hash))
      (for ([j (in-range (+ f-idx 1) l-idx)])
        (hash-set! unique-middle-chars (string-ref s j) #t))
      (set! total-unique-palindromes (+ total-unique-palindromes (hash-count unique-middle-chars)))))

  total-unique-palindromes)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_palindromic_subsequence/1]).

count_palindromic_subsequence(S) ->
    N = length(S),
    FirstOccurrence = array:new([{size, 26}, {default, -1}]),
    LastOccurrence = array:new([{size, 26}, {default, -1}]),

    {F_occ, L_occ} = lists:foldl(
        fun({Char, I}, {AccF, AccL}) ->
            CharIdx = Char - $a,
            CurrentF = array:get(CharIdx, AccF),
            NewF = if CurrentF == -1 -> array:set(CharIdx, I, AccF); true -> AccF end,
            NewL = array:set(CharIdx, I, AccL),
            {NewF, NewL}
        end,
        {FirstOccurrence, LastOccurrence},
        lists:zip(string:to_list(S), lists:seq(0, N - 1))
    ),

    TotalUniquePalindromes = lists:foldl(
        fun(I, Acc) ->
            F_idx = array:get(I, F_occ),
            L_idx = array:get(I, L_occ),

            if F_idx /= -1 andalso F_idx < L_idx ->
                UniqueMiddleChars = sets:new(),
                % Erlang sublist is 1-indexed, length based
                % String.to_list converts to charlist
                SubStringList = lists:sublist(string:to_list(S), F_idx + 2, L_idx - F_idx - 1),

                MiddleCount = lists:foldl(
                    fun(MiddleChar, MiddleSet) ->
                        sets:add_element(MiddleChar, MiddleSet)
                    end,
                    UniqueMiddleChars,
                    SubStringList
                ),
                Acc + sets:size(MiddleCount);
            true ->
                Acc
            end
        end,
        0,
        lists:seq(0, 25)
    ),

    TotalUniquePalindromes.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_palindromic_subsequence(s :: String.t) :: integer
  def count_palindromic_subsequence(s) do
    first_occurrence = :array.new(size: 26, default: -1)
    last_occurrence = :array.new(size: 26, default: -1)

    {first_occurrence, last_occurrence} = 
      s
      |> String.to_charlist()
      |> Enum.with_index()
      |> Enum.reduce({first_occurrence, last_occurrence}, fn {char, i}, {acc_f, acc_l} ->
        char_idx = char - ?a
        current_f = :array.get(char_idx, acc_f)
        new_f = if current_f == -1, do: :array.set(char_idx, i, acc_f), else: acc_f
        new_l = :array.set(char_idx, i, acc_l)
        {new_f, new_l}
      end)

    total_unique_palindromes = 
      0..25
      |> Enum.reduce(0, fn i, acc ->
        f_idx = :array.get(i, first_occurrence)
        l_idx = :array.get(i, last_occurrence)

        if f_idx != -1 && f_idx < l_idx do
          unique_middle_chars = MapSet.new()

          # Elixir string slicing is 0-indexed, length based
          # Substring from f_idx + 1 up to (but not including) l_idx
          sub_string = String.slice(s, f_idx + 1, l_idx - (f_idx + 1))

          middle_count = 
            sub_string
            |> String.to_charlist()
            |> Enum.reduce(unique_middle_chars, fn middle_char, middle_set ->
              MapSet.put(middle_set, middle_char)
            end)

          acc + MapSet.size(middle_count)
        else
          acc
        end
      end)

    total_unique_palindromes
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N)

- **Space Complexity:** O(1)

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-24 07:41:41 )</small>
</summary>

<div class="ai-solution-content">

### Approach

To solve this problem, we can use a brute force approach by iterating over all possible subsequences of length 3 in the given string and checking if they are palindromes. However, this approach would be inefficient due to its high time complexity. A more efficient approach is to use a hashmap to store the indices of each character in the string. Then, for each character, we can find all pairs of characters that are equal to the first and last characters of the potential palindrome and are separated by at least one character. This approach ensures that we only consider valid palindromic subsequences of length 3. We can then use a set to keep track of unique palindromic subsequences and return the size of the set as the result.

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
#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int count = 0;
        unordered_set<string> unique;
        for (int i = 0; i < s.size(); i++) {
            for (int j = i + 1; j < s.size(); j++) {
                for (int k = j + 1; k < s.size(); k++) {
                    if (s[i] == s[k]) {
                        string sub = s.substr(i, 1) + s.substr(j, 1) + s.substr(k, 1);
                        if (unique.find(sub) == unique.end()) {
                            unique.insert(sub);
                            count++;
                        }
                    }
                }
            }
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

public class Solution {
    public int countPalindromicSubsequence(String s) {
        int count = 0;
        Set<String> unique = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j < s.length(); j++) {
                for (int k = j + 1; k < s.length(); k++) {
                    if (s.charAt(i) == s.charAt(k)) {
                        String sub = s.substring(i, i + 1) + s.substring(j, j + 1) + s.substring(k, k + 1);
                        if (!unique.contains(sub)) {
                            unique.add(sub);
                            count++;
                        }
                    }
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        unique = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                for k in range(j + 1, len(s)):
                    if s[i] == s[k]:
                        sub = s[i] + s[j] + s[k]
                        if sub not in unique:
                            unique.add(sub)
                            count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        unique = set()
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                for k in range(j + 1, len(s)):
                    if s[i] == s[k]:
                        sub = s[i] + s[j] + s[k]
                        if sub not in unique:
                            unique.add(sub)
                            count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <string.h>

int countPalindromicSubsequence(char * s){
    int count = 0;
    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len; j++) {
            for (int k = j + 1; k < len; k++) {
                if (s[i] == s[k]) {
                    char sub[4];
                    sub[0] = s[i];
                    sub[1] = s[j];
                    sub[2] = s[k];
                    sub[3] = '\0';
                    // check if sub is in unique
                    // for simplicity, we assume we have a function to check if a string is in a set
                    // if (!isInSet(sub)) {
                    //     addToStringSet(sub);
                    //     count++;
                    // }
                }
            }
        }
    }
    return count;
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
    public int CountPalindromicSubsequence(string s) {
        int count = 0;
        HashSet<string> unique = new HashSet<string>();
        for (int i = 0; i < s.Length; i++) {
            for (int j = i + 1; j < s.Length; j++) {
                for (int k = j + 1; k < s.Length; k++) {
                    if (s[i] == s[k]) {
                        string sub = s[i].ToString() + s[j].ToString() + s[k].ToString();
                        if (!unique.Contains(sub)) {
                            unique.Add(sub);
                            count++;
                        }
                    }
                }
            }
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
var countPalindromicSubsequence = function(s) {
    let count = 0;
    let unique = new Set();
    for (let i = 0; i < s.length; i++) {
        for (let j = i + 1; j < s.length; j++) {
            for (let k = j + 1; k < s.length; k++) {
                if (s[i] == s[k]) {
                    let sub = s[i] + s[j] + s[k];
                    if (!unique.has(sub)) {
                        unique.add(sub);
                        count++;
                    }
                }
            }
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countPalindromicSubsequence(s: string): number {
    let count: number = 0;
    let unique: Set<string> = new Set();
    for (let i: number = 0; i < s.length; i++) {
        for (let j: number = i + 1; j < s.length; j++) {
            for (let k: number = j + 1; k < s.length; k++) {
                if (s[i] == s[k]) {
                    let sub: string = s[i] + s[j] + s[k];
                    if (!unique.has(sub)) {
                        unique.add(sub);
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function countPalindromicSubsequence($s) {
        $count = 0;
        $unique = array();
        for ($i = 0; $i < strlen($s); $i++) {
            for ($j = $i + 1; $j < strlen($s); $j++) {
                for ($k = $j + 1; $k < strlen($s); $k++) {
                    if ($s[$i] == $s[$k]) {
                        $sub = $s[$i] . $s[$j] . $s[$k];
                        if (!in_array($sub, $unique)) {
                            $unique[] = $sub;
                            $count++;
                        }
                    }
                }
            }
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countPalindromicSubsequence(_ s: String) -> Int {
        var count = 0
        var unique: Set<String> = []
        for i in s.indices {
            for j in s.indices {
                for k in s.indices {
                    if i < j && j < k && s[i] == s[k] {
                        let sub = String(s[i]) + String(s[j]) + String(s[k])
                        if !unique.contains(sub) {
                            unique.insert(sub)
                            count += 1
                        }
                    }
                }
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countPalindromicSubsequence(s: String): Int {
        var count = 0
        val unique: MutableSet<String> = mutableSetOf()
        for (i in s.indices) {
            for (j in i + 1 until s.length) {
                for (k in j + 1 until s.length) {
                    if (s[i] == s[k]) {
                        val sub = s[i].toString() + s[j].toString() + s[k].toString()
                        if (!unique.contains(sub)) {
                            unique.add(sub)
                            count++
                        }
                    }
                }
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countPalindromicSubsequence(String s) {
      int count = 0;
      Set<String> unique = {};
      for (int i = 0; i < s.length; i++) {
          for (int j = i + 1; j < s.length; j++) {
              for (int k = j + 1; k < s.length; k++) {
                  if (s[i] == s[k]) {
                      String sub = s[i] + s[j] + s[k];
                      if (!unique.contains(sub)) {
                          unique.add(sub);
                          count++;
                      }
                  }
              }
          }
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
package main

import (
    "fmt"
)

func countPalindromicSubsequence(s string) int {
    count := 0
    unique := make(map[string]bool)
    for i := 0; i < len(s); i++ {
        for j := i + 1; j < len(s); j++ {
            for k := j + 1; k < len(s); k++ {
                if s[i] == s[k] {
                    sub := string(s[i]) + string(s[j]) + string(s[k])
                    if !unique[sub] {
                        unique[sub] = true
                        count++
                    }
                }
            }
        }
    }
    return count
}

func main() {
    fmt.Println(countPalindromicSubsequence("aabca"))
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
def count_palindromic_subsequence(s)
    count = 0
    unique = Set.new
    (0...s.length).each do |i|
        (i + 1...s.length).each do |j|
            (j + 1...s.length).each do |k|
                if s[i] == s[k]
                    sub = s[i].to_s + s[j].to_s + s[k].to_s
                    if !unique.include?(sub)
                        unique.add(sub)
                        count += 1
                    end
                end
            end
        end
    end
    count
end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countPalindromicSubsequence(s: String): Int = {
        var count = 0
        val unique = scala.collection.mutable.Set[String]()
        for (i <- 0 until s.length) {
            for (j <- i + 1 until s.length) {
                for (k <- j + 1 until s.length) {
                    if (s(i) == s(k)) {
                        val sub = s(i).toString + s(j).toString + s(k).toString
                        if (!unique.contains(sub)) {
                            unique.add(sub)
                            count += 1
                        }
                    }
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let mut count = 0;
        let mut unique: HashSet<String> = HashSet::new();
        for i in 0..s.len() {
            for j in i + 1..s.len() {
                for k in j + 1..s.len() {
                    if s.as_bytes()[i] == s.as_bytes()[k] {
                        let sub = format!("{}{}{}", s.as_bytes()[i] as char, s.as_bytes()[j] as char, s.as_bytes()[k] as char);
                        if !unique.contains(&sub) {
                            unique.insert(sub);
                            count += 1;
                        }
                    }
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (count-palindromic-subsequence s)
    (let ((count 0)
          (unique (make-hash)))
        (for ((i (range (string-length s))))
          (for ((j (range (+ i 1) (string-length s))))
            (for ((k (range (+ j 1) (string-length s))))
              (if (eq? (string-ref s i) (string-ref s k))
                  (let ((sub (string (string-ref s i) (string-ref s j) (string-ref s k))))
                    (if (not (hash-ref unique sub #f))
                        (begin
                          (hash-set! unique sub #t)
                          (set! count (+ count 1))))))))
        count))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).

-export([count_palindromic_subsequence/1]).

count_palindromic_subsequence(S) ->
    Count = count(S, 0, [], []),
    Count.

count([], Count, _, _) ->
    Count;
count([H|T], Count, Unique, S) ->
    {NewCount, NewUnique} = count_sub(T, H, Count, Unique, S),
    count(T, NewCount, NewUnique, [H|S]).

count_sub([], Count, Unique, _) ->
    {Count, Unique};
count_sub([H|T], C, Unique, [CH|S]) ->
    case C == CH of
        true ->
            Sub = [C, H, CH],
            case lists:member(Sub, Unique) of
                true ->
                    count_sub(T, Count, Unique, [CH|S]);
                false ->
                    NewUnique = [Sub|Unique],
                    count_sub(T, Count + 1, NewUnique, [CH|S])
            end;
        false ->
            count_sub(T, Count, Unique, [CH|S])
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def count_palindromic_subsequence(s) do
      count = 0
      unique = MapSet.new()
      count_palindromic_subsequence(s, count, unique)
  end

  defp count_palindromic_subsequence([], count, _), do: count

  defp count_palindromic_subsequence([h|t], count, unique) do
      {new_count, new_unique} = count_sub(t, h, count, unique, [h])
      count_palindromic_subsequence(t, new_count, new_unique)
  end

  defp count_sub([], count, _, _), do: {count, []}

  defp count_sub([h|t], c, count, unique, [ch|s]) do
      case c == ch do
          true ->
              sub = [c, h, ch]
              case Enum.member?(unique, sub) do
                  true -> count_sub(t, count, unique, [ch|s])
                  false ->
                      new_unique = MapSet.put(unique, sub)
                      count_sub(t, count + 1, new_unique, [ch|s])
              end
          false -> count_sub(t, count, unique, [ch|s])
      end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2) where n is the length of the string, because we are iterating over the string and for each character, we are iterating over the rest of the string to find pairs of equal characters.

- **Space Complexity:** O(n) where n is the length of the string, because in the worst case, we might need to store all characters in the hashmap and the set of unique palindromic subsequences.

</div>
</details>
