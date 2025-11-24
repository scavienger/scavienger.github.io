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
  <small class="solution-timestamp">(2025-11-24 07:30:19 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count the number of unique palindromic subsequences of length three. A length-three palindrome has the form 'X Y X', where 'X' is the first and last character, and 'Y' is the middle character. Both 'X' and 'Y' must be lowercase English letters. Since there are only 26 possible lowercase English letters, there are at most 26 * 26 = 676 unique length-three palindromes. This small upper bound suggests that we can iterate through all possible 'X' characters and for each 'X', determine the unique 'Y' characters that can form 'X Y X'.

The core idea is to iterate through each possible character 'X' from 'a' to 'z'. For a palindrome 'X Y X' to exist as a subsequence, we need to find at least two occurrences of 'X' in the string 's'. Specifically, we need the first occurrence of 'X' (let's say at index `first_X`) and the last occurrence of 'X' (at index `last_X`). If `first_X < last_X`, then any character 'Y' that appears in the substring `s[first_X + 1 ... last_X - 1]` can serve as the middle character. We collect all unique characters 'Y' from this substring and add their count to our total.

To implement this efficiently, we first precompute the first and last occurrence index for every character ('a' through 'z') in the input string `s`. This can be done by iterating through `s` once. Then, we iterate through each character 'X' from 'a' to 'z'. If 'X' appears at least twice (i.e., `first_X < last_X`), we then iterate through the characters in the substring `s[first_X + 1 ... last_X - 1]`. We use a set (or a boolean array) to keep track of the unique characters encountered in this middle segment. The size of this set is the number of unique 'Y' characters for the current 'X', which is added to our running total. Finally, we return the total count.

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
#include <string>
#include <vector>
#include <set>
#include <algorithm>

class Solution {
public:
    int countPalindromicSubsequence(std::string s) {
        std::vector<int> first_occurrence(26, -1);
        std::vector<int> last_occurrence(26, -1);

        int n = s.length();
        for (int i = 0; i < n; ++i) {
            int char_idx = s[i] - 'a';
            if (first_occurrence[char_idx] == -1) {
                first_occurrence[char_idx] = i;
            }
            last_occurrence[char_idx] = i;
        }

        int total_unique_palindromes = 0;

        for (int i = 0; i < 26; ++i) { // Iterate through all possible outer characters 'a' to 'z'
            int first_idx = first_occurrence[i];
            int last_idx = last_occurrence[i];

            if (first_idx != -1 && first_idx < last_idx) {
                // Found at least two occurrences of the character
                // Now find unique characters between first_idx and last_idx

                std::set<char> unique_middle_chars;
                for (int j = first_idx + 1; j < last_idx; ++j) {
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
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countPalindromicSubsequence(String s) {
        int[] firstOccurrence = new int[26];
        int[] lastOccurrence = new int[26];

        // Initialize with -1 to indicate not found
        for (int i = 0; i < 26; i++) {
            firstOccurrence[i] = -1;
            lastOccurrence[i] = -1;
        }

        int n = s.length();
        for (int i = 0; i < n; i++) {
            int charIdx = s.charAt(i) - 'a';
            if (firstOccurrence[charIdx] == -1) {
                firstOccurrence[charIdx] = i;
            }
            lastOccurrence[charIdx] = i;
        }

        int totalUniquePalindromes = 0;

        for (int i = 0; i < 26; i++) { // Iterate through all possible outer characters 'a' to 'z'
            int firstIdx = firstOccurrence[i];
            int lastIdx = lastOccurrence[i];

            if (firstIdx != -1 && firstIdx < lastIdx) {
                // Found at least two occurrences of the character
                // Now find unique characters between firstIdx and lastIdx

                Set<Character> uniqueMiddleChars = new HashSet<>();
                for (int j = firstIdx + 1; j < lastIdx; j++) {
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

        n = len(s)
        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            if first_occurrence[char_idx] == -1:
                first_occurrence[char_idx] = i
            last_occurrence[char_idx] = i

        total_unique_palindromes = 0

        for i in range(26): # Iterate through all possible outer characters 'a' to 'z'
            first_idx = first_occurrence[i]
            last_idx = last_occurrence[i]

            if first_idx != -1 and first_idx < last_idx:
                # Found at least two occurrences of the character
                # Now find unique characters between first_idx and last_idx

                unique_middle_chars = set()
                for j in range(first_idx + 1, last_idx):
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

        n = len(s)
        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            if first_occurrence[char_idx] == -1:
                first_occurrence[char_idx] = i
            last_occurrence[char_idx] = i

        total_unique_palindromes = 0

        for i in range(26): # Iterate through all possible outer characters 'a' to 'z'
            first_idx = first_occurrence[i]
            last_idx = last_occurrence[i]

            if first_idx != -1 and first_idx < last_idx:
                # Found at least two occurrences of the character
                # Now find unique characters between first_idx and last_idx

                unique_middle_chars = set()
                for j in range(first_idx + 1, last_idx):
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

    for (int i = 0; i < 26; i++) {
        first_occurrence[i] = -1;
        last_occurrence[i] = -1;
    }

    int n = strlen(s);
    for (int i = 0; i < n; i++) {
        int char_idx = s[i] - 'a';
        if (first_occurrence[char_idx] == -1) {
            first_occurrence[char_idx] = i;
        }
        last_occurrence[char_idx] = i;
    }

    int total_unique_palindromes = 0;

    for (int i = 0; i < 26; i++) { // Iterate through all possible outer characters 'a' to 'z'
        int first_idx = first_occurrence[i];
        int last_idx = last_occurrence[i];

        if (first_idx != -1 && first_idx < last_idx) {
            // Found at least two occurrences of the character
            // Now find unique characters between first_idx and last_idx

            bool unique_middle_chars[26] = {false}; // Using a boolean array as a set
            int current_unique_count = 0;

            for (int j = first_idx + 1; j < last_idx; j++) {
                int middle_char_idx = s[j] - 'a';
                if (!unique_middle_chars[middle_char_idx]) {
                    unique_middle_chars[middle_char_idx] = true;
                    current_unique_count++;
                }
            }

            total_unique_palindromes += current_unique_count;
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
        int[] lastOccurrence = new int[26];

        // Initialize with -1 to indicate not found
        for (int i = 0; i < 26; i++) {
            firstOccurrence[i] = -1;
            lastOccurrence[i] = -1;
        }

        int n = s.Length;
        for (int i = 0; i < n; i++) {
            int charIdx = s[i] - 'a';
            if (firstOccurrence[charIdx] == -1) {
                firstOccurrence[charIdx] = i;
            }
            lastOccurrence[charIdx] = i;
        }

        int totalUniquePalindromes = 0;

        for (int i = 0; i < 26; i++) { // Iterate through all possible outer characters 'a' to 'z'
            int firstIdx = firstOccurrence[i];
            int lastIdx = lastOccurrence[i];

            if (firstIdx != -1 && firstIdx < lastIdx) {
                // Found at least two occurrences of the character
                // Now find unique characters between firstIdx and lastIdx

                HashSet<char> uniqueMiddleChars = new HashSet<char>();
                for (int j = firstIdx + 1; j < lastIdx; j++) {
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

    const n = s.length;
    for (let i = 0; i < n; i++) {
        const charCode = s.charCodeAt(i) - 'a'.charCodeAt(0);
        if (firstOccurrence[charCode] === -1) {
            firstOccurrence[charCode] = i;
        }
        lastOccurrence[charCode] = i;
    }

    let totalUniquePalindromes = 0;

    for (let i = 0; i < 26; i++) { // Iterate through all possible outer characters 'a' to 'z'
        const firstIdx = firstOccurrence[i];
        const lastIdx = lastOccurrence[i];

        if (firstIdx !== -1 && firstIdx < lastIdx) {
            // Found at least two occurrences of the character
            // Now find unique characters between firstIdx and lastIdx

            const uniqueMiddleChars = new Set();
            for (let j = firstIdx + 1; j < lastIdx; j++) {
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

    const n: number = s.length;
    for (let i = 0; i < n; i++) {
        const charCode: number = s.charCodeAt(i) - 'a'.charCodeAt(0);
        if (firstOccurrence[charCode] === -1) {
            firstOccurrence[charCode] = i;
        }
        lastOccurrence[charCode] = i;
    }

    let totalUniquePalindromes: number = 0;

    for (let i = 0; i < 26; i++) { // Iterate through all possible outer characters 'a' to 'z'
        const firstIdx: number = firstOccurrence[i];
        const lastIdx: number = lastOccurrence[i];

        if (firstIdx !== -1 && firstIdx < lastIdx) {
            // Found at least two occurrences of the character
            // Now find unique characters between firstIdx and lastIdx

            const uniqueMiddleChars: Set<string> = new Set<string>();
            for (let j = firstIdx + 1; j < lastIdx; j++) {
                uniqueMiddleChars.add(s[j]);
            }

            totalUniquePalindromes += uniqueMiddleChars.size;
        }
    }

    return totalUniquePalindromes;
}
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
        for ($i = 0; $i < $n; $i++) {
            $char_idx = ord($s[$i]) - ord('a');
            if ($firstOccurrence[$char_idx] === -1) {
                $firstOccurrence[$char_idx] = $i;
            }
            $lastOccurrence[$char_idx] = $i;
        }

        $totalUniquePalindromes = 0;

        for ($i = 0; $i < 26; $i++) { // Iterate through all possible outer characters 'a' to 'z'
            $firstIdx = $firstOccurrence[$i];
            $lastIdx = $lastOccurrence[$i];

            if ($firstIdx !== -1 && $firstIdx < $lastIdx) {
                // Found at least two occurrences of the character
                // Now find unique characters between firstIdx and lastIdx

                $uniqueMiddleChars = [];
                for ($j = $firstIdx + 1; $j < $lastIdx; $j++) {
                    $uniqueMiddleChars[$s[$j]] = true; // Using associative array as a set
                }

                $totalUniquePalindromes += count($uniqueMiddleChars);
            }
        }

        return $totalUniquePalindromes;
    }
}
?>
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

        let sChars = Array(s)
        let n = sChars.count
        for i in 0..<n {
            let charIdx = Int(sChars[i].asciiValue! - Character("a").asciiValue!)
            if firstOccurrence[charIdx] == -1 {
                firstOccurrence[charIdx] = i
            }
            lastOccurrence[charIdx] = i
        }

        var totalUniquePalindromes = 0

        for i in 0..<26 { // Iterate through all possible outer characters 'a' to 'z'
            let firstIdx = firstOccurrence[i]
            let lastIdx = lastOccurrence[i]

            if firstIdx != -1 && firstIdx < lastIdx {
                // Found at least two occurrences of the character
                // Now find unique characters between firstIdx and lastIdx

                var uniqueMiddleChars = Set<Character>()
                for j in (firstIdx + 1)..<lastIdx {
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

        val n = s.length
        for (i in 0 until n) {
            val charIdx = s[i] - 'a'
            if (firstOccurrence[charIdx] == -1) {
                firstOccurrence[charIdx] = i
            }
            lastOccurrence[charIdx] = i
        }

        var totalUniquePalindromes = 0

        for (i in 0 until 26) { // Iterate through all possible outer characters 'a' to 'z'
            val firstIdx = firstOccurrence[i]
            val lastIdx = lastOccurrence[i]

            if (firstIdx != -1 && firstIdx < lastIdx) {
                // Found at least two occurrences of the character
                // Now find unique characters between firstIdx and lastIdx

                val uniqueMiddleChars = HashSet<Char>()
                for (j in firstIdx + 1 until lastIdx) {
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
class Solution {
  int countPalindromicSubsequence(String s) {
    List<int> firstOccurrence = List.filled(26, -1);
    List<int> lastOccurrence = List.filled(26, -1);

    int n = s.length;
    for (int i = 0; i < n; i++) {
      int charIdx = s.codeUnitAt(i) - 'a'.codeUnitAt(0);
      if (firstOccurrence[charIdx] == -1) {
        firstOccurrence[charIdx] = i;
      }
      lastOccurrence[charIdx] = i;
    }

    int totalUniquePalindromes = 0;

    for (int i = 0; i < 26; i++) { // Iterate through all possible outer characters 'a' to 'z'
      int firstIdx = firstOccurrence[i];
      int lastIdx = lastOccurrence[i];

      if (firstIdx != -1 && firstIdx < lastIdx) {
        // Found at least two occurrences of the character
        // Now find unique characters between firstIdx and lastIdx

        Set<String> uniqueMiddleChars = <String>{};
        for (int j = firstIdx + 1; j < lastIdx; j++) {
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
package main

import (
	"fmt"
)

func countPalindromicSubsequence(s string) int {
    firstOccurrence := [26]int{}
    lastOccurrence := [26]int{}

    // Initialize with -1 to indicate not found
    for i := 0; i < 26; i++ {
        firstOccurrence[i] = -1
        lastOccurrence[i] = -1
    }

    n := len(s)
    for i := 0; i < n; i++ {
        charIdx := s[i] - 'a'
        if firstOccurrence[charIdx] == -1 {
            firstOccurrence[charIdx] = i
        }
        lastOccurrence[charIdx] = i
    }

    totalUniquePalindromes := 0

    for i := 0; i < 26; i++ { // Iterate through all possible outer characters 'a' to 'z'
        firstIdx := firstOccurrence[i]
        lastIdx := lastOccurrence[i]

        if firstIdx != -1 && firstIdx < lastIdx {
            // Found at least two occurrences of the character
            // Now find unique characters between firstIdx and lastIdx

            uniqueMiddleChars := make(map[byte]bool)
            for j := firstIdx + 1; j < lastIdx; j++ {
                uniqueMiddleChars[s[j]] = true
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

# @param {String} s
# @return {Integer}
def count_palindromic_subsequence(s)
    first_occurrence = Array.new(26, -1)
    last_occurrence = Array.new(26, -1)

    n = s.length
    (0...n).each do |i|
        char_idx = s[i].ord - 'a'.ord
        if first_occurrence[char_idx] == -1
            first_occurrence[char_idx] = i
        end
        last_occurrence[char_idx] = i
    end

    total_unique_palindromes = 0

    (0...26).each do |i| # Iterate through all possible outer characters 'a' to 'z'
        first_idx = first_occurrence[i]
        last_idx = last_occurrence[i]

        if first_idx != -1 && first_idx < last_idx
            # Found at least two occurrences of the character
            # Now find unique characters between first_idx and last_idx

            unique_middle_chars = Set.new
            (first_idx + 1...last_idx).each do |j|
                unique_middle_chars.add(s[j])
            end

            total_unique_palindromes += unique_middle_chars.size
        end
    end

    total_unique_palindromes
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

        val n = s.length
        for (i <- 0 until n) {
            val charIdx = s(i) - 'a'
            if (firstOccurrence(charIdx) == -1) {
                firstOccurrence(charIdx) = i
            }
            lastOccurrence(charIdx) = i
        }

        var totalUniquePalindromes = 0

        for (i <- 0 until 26) { // Iterate through all possible outer characters 'a' to 'z'
            val firstIdx = firstOccurrence(i)
            val lastIdx = lastOccurrence(i)

            if (firstIdx != -1 && firstIdx < lastIdx) {
                // Found at least two occurrences of the character
                // Now find unique characters between firstIdx and lastIdx

                val uniqueMiddleChars = mutable.Set[Char]()
                for (j <- firstIdx + 1 until lastIdx) {
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
        let mut first_occurrence: [i32; 26] = [-1; 26];
        let mut last_occurrence: [i32; 26] = [-1; 26];

        let s_bytes = s.as_bytes(); // Work with bytes for efficiency
        let n = s_bytes.len();
        for i in 0..n {
            let char_idx = (s_bytes[i] - b'a') as usize;
            if first_occurrence[char_idx] == -1 {
                first_occurrence[char_idx] = i as i32;
            }
            last_occurrence[char_idx] = i as i32;
        }

        let mut total_unique_palindromes = 0;

        for i in 0..26 { // Iterate through all possible outer characters 'a' to 'z'
            let first_idx = first_occurrence[i];
            let last_idx = last_occurrence[i];

            if first_idx != -1 && first_idx < last_idx {
                // Found at least two occurrences of the character
                // Now find unique characters between first_idx and last_idx

                let mut unique_middle_chars = HashSet::new();
                for j in (first_idx + 1) as usize .. last_idx as usize {
                    unique_middle_chars.insert(s_bytes[j]); // Insert byte directly
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
  (define first-occurrence (build-vector 26 (lambda (i) -1)))
  (define last-occurrence (build-vector 26 (lambda (i) -1)))

  (define n (string-length s))
  (for ([i (in-range n)])
    (define char-code (- (char->integer (string-ref s i)) (char->integer #\a)))
    (when (= (vector-ref first-occurrence char-code) -1)
      (vector-set! first-occurrence char-code i))
    (vector-set! last-occurrence char-code i))

  (define total-unique-palindromes 0)

  (for ([i (in-range 26)]) ; Iterate through all possible outer characters 'a' to 'z'
    (define first-idx (vector-ref first-occurrence i))
    (define last-idx (vector-ref last-occurrence i)))

    (when (and (!= first-idx -1) (< first-idx last-idx))
      ; Found at least two occurrences of the character
      ; Now find unique characters between first-idx and last-idx

      (define unique-middle-chars (make-hash)) ; Using a hash table as a set
      (for ([j (in-range (+ first-idx 1) last-idx)])
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

count_palindromic_subsequence(S_str) ->
    S_list = S_str, % S_str is already a list of char codes
    N = length(S_list),

    InitialOccurrences = maps:from_list([{C, {-1, -1}} || C <- lists:seq($a, $z)]),

    Occurrences = populate_occurrences_list(S_list, 0, InitialOccurrences),

    TotalUniquePalindromes = count_palindromes_loop($a, $z, S_list, Occurrences, 0),
    TotalUniquePalindromes.

populate_occurrences_list([C | Rest], Index, Acc) ->
    {First, Last} = maps:get(C, Acc),
    NewFirst = if First == -1 -> Index; true -> First end,
    NewLast = Index,
    NewAcc = maps:put(C, {NewFirst, NewLast}, Acc),
    populate_occurrences_list(Rest, Index + 1, NewAcc);
populate_occurrences_list([], _, Acc) ->
    Acc.

count_palindromes_loop(Char, EndChar, S_list, Occurrences, AccTotal) when Char =< EndChar ->
    {FirstIdx, LastIdx} = maps:get(Char, Occurrences),

    CurrentPalindromes = 
        if 
            FirstIdx /= -1 andalso FirstIdx < LastIdx ->
                MiddleChars = get_middle_chars_list(S_list, FirstIdx + 1, LastIdx - 1),
                length(ordsets:from_list(MiddleChars));
            true ->
                0
        end,

    count_palindromes_loop(Char + 1, EndChar, S_list, Occurrences, AccTotal + CurrentPalindromes);
count_palindromes_loop(_, _, _, _, AccTotal) ->
    AccTotal.

get_middle_chars_list(S_list, StartIdx, EndIdx) ->
    % lists:sublist(List, Start, Length) is 1-indexed for Start
    % StartIdx and EndIdx are 0-indexed
    if StartIdx > EndIdx ->
        [];
    true ->
        lists:sublist(S_list, StartIdx + 1, EndIdx - StartIdx + 1)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_palindromic_subsequence(s :: String.t) :: integer
  def count_palindromic_subsequence(s) do
    n = String.length(s)

    # Initialize first_occurrence and last_occurrence maps
    # Keys are char codes, values are {first_idx, last_idx}
    initial_occurrences = 
      Enum.reduce(?a..?z, %{}, fn char_code, acc ->
        Map.put(acc, char_code, {-1, -1})
      end)

    # Populate first and last occurrences
    occurrences = 
      Enum.reduce(0..(n-1), initial_occurrences, fn i, acc ->
        char_code = String.at(s, i) |> String.to_charlist() |> hd()
        {first, last} = Map.fetch!(acc, char_code)
        new_first = if first == -1, do: i, else: first
        new_last = i
        Map.put(acc, char_code, {new_first, new_last})
      end)

    total_unique_palindromes = 
      Enum.reduce(?a..?z, 0, fn char_code, acc_total ->
        {first_idx, last_idx} = Map.fetch!(occurrences, char_code)

        current_palindromes = 
          if first_idx != -1 and first_idx < last_idx do
            middle_chars = 
              for j <- (first_idx + 1)..(last_idx - 1), do: String.at(s, j)

            Enum.uniq(middle_chars) |> length()
          else
            0
          end

        acc_total + current_palindromes
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
  <small class="solution-timestamp">(2025-11-24 07:30:29 )</small>
</summary>

<div class="ai-solution-content">

### Approach

No approach provided

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
// Generation failed for C++
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: HTTP Error 400
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A

</div>
</details>
