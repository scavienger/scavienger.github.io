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

Given a string `s`, return _the number of**unique palindromes of length three** that are a **subsequence** of _`s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once**.

A **palindrome** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

  * For example, `"ace"` is a subsequence of `"_a_ b _c_ d _e_ "`.

**Example 1:**

``` Input: s = "aabca" Output: 3 Explanation: The 3 palindromic subsequences of length 3 are: \- "aba" (subsequence of "aabca") \- "aaa" (subsequence of "aabca") \- "aca" (subsequence of "aabca") ``` 

**Example 2:**

``` Input: s = "adc" Output: 0 Explanation: There are no palindromic subsequences of length 3 in "adc". ``` 

**Example 3:**

``` Input: s = "bbcbaba" Output: 4 Explanation: The 4 palindromic subsequences of length 3 are: \- "bbb" (subsequence of "bbcbaba") \- "bcb" (subsequence of "bbcbaba") \- "bab" (subsequence of "bbcbaba") \- "aba" (subsequence of "bbcbaba") ``` 

**Constraints:**

  * `3 <= s.length <= 105`
  * `s` consists of only lowercase English letters.

## Hints

1. What is the maximum number of length-3 palindromic strings?

2. How can we keep track of the characters that appeared to the left of a given position?

## ✨ AI-Generated Solution (gemini-2.5-flash)

### Approach

The problem asks us to count the number of unique palindromic subsequences of length three. A palindrome of length three has the specific form `X Y X`, where `X` and `Y` are single characters. For example, 'aba', 'aca', 'zzz' are length-3 palindromes. The core challenge is to ensure that `X Y X` is a subsequence of the given string `s`, meaning we need to find three characters in `s` at indices `i < j < k` such that `s[i] = X`, `s[j] = Y`, and `s[k] = X`. The 'unique' requirement is crucial: even if a palindrome like 'aba' can be formed in multiple ways (e.g., in "abaca", the first 'a' and last 'a' can form 'aba' with 'b', and also the second 'a' and last 'a' can form 'aba' with 'b'), it should only be counted once.

The most straightforward approach to count unique `X Y X` palindromes is to iterate through all possible choices for the outer character `X` (from 'a' to 'z') and then, for each chosen `X`, determine all unique characters `Y` that can serve as the middle character. Since there are 26 lowercase English letters, there are 26 choices for `X` and 26 choices for `Y`, resulting in a maximum of `26 * 26 = 676` distinct length-3 palindromes. We need to efficiently check which of these can actually be formed as subsequences within `s`.

For a specific outer character `X`, to form `X Y X` as a subsequence, we need to find its first occurrence in `s` (let's say at index `first_X`) and its last occurrence in `s` (at index `last_X`). If `X` does not appear in `s`, or if it appears only once (`first_X == last_X`), then it's impossible to have another `X` later in the string with a character `Y` in between. Therefore, we only proceed if `X` appears at least twice and `first_X < last_X`. If these conditions are met, any character `Y` found at an index `j` such that `first_X < j < last_X` can serve as the middle character. To count the number of *unique* palindromes for the fixed `X`, we simply need to count how many *unique characters* exist in the substring `s[first_X + 1 ... last_X - 1]`. Each unique character in this intermediate segment contributes one unique `X Y X` palindrome to our total count.

To make this process efficient, we first precompute the `first_occurrence` and `last_occurrence` indices for all 26 lowercase English letters. This can be done with a single pass through the input string `s`. We'll use two arrays (or equivalent data structures like maps/dictionaries) of size 26: `first_idx_map` and `last_idx_map`. Initialize all entries in these maps to a sentinel value like -1 to indicate that the character hasn't been found yet. Then, iterate through `s` from `i = 0` to `len(s) - 1`. For each character `c` at `s[i]`, convert `c` to its 0-25 integer index. If `first_idx_map[index_of_c]` is still -1, set `first_idx_map[index_of_c] = i`. Regardless, always update `last_idx_map[index_of_c] = i`. After this preprocessing, we will have the exact first and last indices for every character present in `s`.

Finally, we iterate through each possible character `X` (from 'a' to 'z' by iterating `char_code` from 0 to 25). For each `char_code`, we retrieve `first_idx_map[char_code]` and `last_idx_map[char_code]`. If `first_idx_map[char_code]` is -1 (meaning `X` is not in `s`) or if `first_idx_map[char_code] >= last_idx_map[char_code]` (meaning `X` appears at most once, or its first and last occurrences are the same, leaving no room for a middle character), we skip this `X`. Otherwise, we consider the substring `s` from `first_idx_map[char_code] + 1` up to `last_idx_map[char_code] - 1`. We use a `Set` data structure to collect all unique characters within this substring. The size of this `Set` represents the number of unique `Y` characters that can form `X Y X` for the current `X`. We add this size to our running `total_count`. After checking all 26 possible `X` characters, the `total_count` will hold the final answer.

### Code

<div class="code-tabs">
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
#include <string>
#include <vector>
#include <set>
#include <algorithm>

class Solution {
public:
    int countPalindromicSubsequence(std::string s) {
        std::vector<int> first_idx(26, -1);
        std::vector<int> last_idx(26, -1);

        for (int i = 0; i < s.length(); ++i) {
            int char_code = s[i] - 'a';
            if (first_idx[char_code] == -1) {
                first_idx[char_code] = i;
            }
            last_idx[char_code] = i;
        }

        int total_count = 0;
        for (int char_val = 0; char_val < 26; ++char_val) {
            int f_idx = first_idx[char_val];
            int l_idx = last_idx[char_val];

            if (f_idx != -1 && f_idx < l_idx) {
                std::set<char> unique_middle_chars;
                for (int j = f_idx + 1; j < l_idx; ++j) {
                    unique_middle_chars.insert(s[j]);
                }
                total_count += unique_middle_chars.size();
            }
        }

        return total_count;
    }
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countPalindromicSubsequence(String s) {
        int[] firstIdx = new int[26];
        int[] lastIdx = new int[26];

        // Initialize arrays with -1 (not found)
        for (int i = 0; i < 26; i++) {
            firstIdx[i] = -1;
            lastIdx[i] = -1;
        }

        for (int i = 0; i < s.length(); i++) {
            int charCode = s.charAt(i) - 'a';
            if (firstIdx[charCode] == -1) {
                firstIdx[charCode] = i;
            }
            lastIdx[charCode] = i;
        }

        int totalCount = 0;
        for (int charVal = 0; charVal < 26; charVal++) {
            int fIdx = firstIdx[charVal];
            int lIdx = lastIdx[charVal];

            if (fIdx != -1 && fIdx < lIdx) {
                Set<Character> uniqueMiddleChars = new HashSet<>();
                for (int j = fIdx + 1; j < lIdx; j++) {
                    uniqueMiddleChars.add(s.charAt(j));
                }
                totalCount += uniqueMiddleChars.size();
            }
        }

        return totalCount;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_idx = [-1] * 26
        last_idx = [-1] * 26

        for i, char_val in enumerate(s):
            idx = ord(char_val) - ord('a')
            if first_idx[idx] == -1:
                first_idx[idx] = i
            last_idx[idx] = i
        
        total_count = 0
        for char_code in range(26):
            f_idx = first_idx[char_code]
            l_idx = last_idx[char_code]

            if f_idx != -1 and f_idx < l_idx:
                unique_middle_chars = set()
                for j in range(f_idx + 1, l_idx):
                    unique_middle_chars.add(s[j])
                total_count += len(unique_middle_chars)
        
        return total_count
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_idx = [-1] * 26
        last_idx = [-1] * 26

        for i, char_val in enumerate(s):
            idx = ord(char_val) - ord('a')
            if first_idx[idx] == -1:
                first_idx[idx] = i
            last_idx[idx] = i
        
        total_count = 0
        for char_code in range(26):
            f_idx = first_idx[char_code]
            l_idx = last_idx[char_code]

            if f_idx != -1 and f_idx < l_idx:
                unique_middle_chars = set()
                for j in range(f_idx + 1, l_idx):
                    unique_middle_chars.add(s[j])
                total_count += len(unique_middle_chars)
        
        return total_count
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <string.h>
#include <stdlib.h>

// A simple way to represent a set for 26 lowercase English letters
// Uses a boolean array. true if character is in set, false otherwise.
typedef struct {
    int present[26];
    int size;
} CharSet;

void initCharSet(CharSet* cs) {
    memset(cs->present, 0, sizeof(cs->present));
    cs->size = 0;
}

void addCharSet(CharSet* cs, char c) {
    int idx = c - 'a';
    if (!cs->present[idx]) {
        cs->present[idx] = 1;
        cs->size++;
    }
}

int countPalindromicSubsequence(char* s) {
    int first_idx[26];
    int last_idx[26];

    for (int i = 0; i < 26; ++i) {
        first_idx[i] = -1;
        last_idx[i] = -1;
    }

    int len = strlen(s);
    for (int i = 0; i < len; ++i) {
        int char_code = s[i] - 'a';
        if (first_idx[char_code] == -1) {
            first_idx[char_code] = i;
        }
        last_idx[char_code] = i;
    }

    int total_count = 0;
    for (int char_val = 0; char_val < 26; ++char_val) {
        int f_idx = first_idx[char_val];
        int l_idx = last_idx[char_val];

        if (f_idx != -1 && f_idx < l_idx) {
            CharSet unique_middle_chars;
            initCharSet(&unique_middle_chars);
            for (int j = f_idx + 1; j < l_idx; ++j) {
                addCharSet(&unique_middle_chars, s[j]);
            }
            total_count += unique_middle_chars.size;
        }
    }

    return total_count;
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
using System;
using System.Collections.Generic;

public class Solution {
    public int CountPalindromicSubsequence(string s) {
        int[] firstIdx = new int[26];
        int[] lastIdx = new int[26];

        // Initialize arrays with -1 (not found)
        Array.Fill(firstIdx, -1);
        Array.Fill(lastIdx, -1);

        for (int i = 0; i < s.Length; i++) {
            int charCode = s[i] - 'a';
            if (firstIdx[charCode] == -1) {
                firstIdx[charCode] = i;
            }
            lastIdx[charCode] = i;
        }

        int totalCount = 0;
        for (int charVal = 0; charVal < 26; charVal++) {
            int fIdx = firstIdx[charVal];
            int lIdx = lastIdx[charVal];

            if (fIdx != -1 && fIdx < lIdx) {
                HashSet<char> uniqueMiddleChars = new HashSet<char>();
                for (int j = fIdx + 1; j < lIdx; j++) {
                    uniqueMiddleChars.Add(s[j]);
                }
                totalCount += uniqueMiddleChars.Count;
            }
        }

        return totalCount;
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function(s) {
    const firstIdx = new Array(26).fill(-1);
    const lastIdx = new Array(26).fill(-1);

    for (let i = 0; i < s.length; i++) {
        const charCode = s.charCodeAt(i) - 'a'.charCodeAt(0);
        if (firstIdx[charCode] === -1) {
            firstIdx[charCode] = i;
        }
        lastIdx[charCode] = i;
    }

    let totalCount = 0;
    for (let charVal = 0; charVal < 26; charVal++) {
        const fIdx = firstIdx[charVal];
        const lIdx = lastIdx[charVal];

        if (fIdx !== -1 && fIdx < lIdx) {
            const uniqueMiddleChars = new Set();
            for (let j = fIdx + 1; j < lIdx; j++) {
                uniqueMiddleChars.add(s[j]);
            }
            totalCount += uniqueMiddleChars.size;
        }
    }

    return totalCount;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function countPalindromicSubsequence(s: string): number {
    const firstIdx: number[] = new Array(26).fill(-1);
    const lastIdx: number[] = new Array(26).fill(-1);

    for (let i = 0; i < s.length; i++) {
        const charCode = s.charCodeAt(i) - 'a'.charCodeAt(0);
        if (firstIdx[charCode] === -1) {
            firstIdx[charCode] = i;
        }
        lastIdx[charCode] = i;
    }

    let totalCount = 0;
    for (let charVal = 0; charVal < 26; charVal++) {
        const fIdx = firstIdx[charVal];
        const lIdx = lastIdx[charVal];

        if (fIdx !== -1 && fIdx < lIdx) {
            const uniqueMiddleChars: Set<string> = new Set();
            for (let j = fIdx + 1; j < lIdx; j++) {
                uniqueMiddleChars.add(s[j]);
            }
            totalCount += uniqueMiddleChars.size;
        }
    }

    return totalCount;
};
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
<?php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function countPalindromicSubsequence($s) {
        $firstIdx = array_fill(0, 26, -1);
        $lastIdx = array_fill(0, 26, -1);

        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $charCode = ord($s[$i]) - ord('a');
            if ($firstIdx[$charCode] == -1) {
                $firstIdx[$charCode] = $i;
            }
            $lastIdx[$charCode] = $i;
        }

        $totalCount = 0;
        for ($charVal = 0; $charVal < 26; $charVal++) {
            $fIdx = $firstIdx[$charVal];
            $lIdx = $lastIdx[$charVal];

            if ($fIdx != -1 && $fIdx < $lIdx) {
                $uniqueMiddleChars = [];
                for ($j = $fIdx + 1; $j < $lIdx; $j++) {
                    $uniqueMiddleChars[$s[$j]] = true; // Using associative array as a set
                }
                $totalCount += count($uniqueMiddleChars);
            }
        }

        return $totalCount;
    }
}
?>
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
import Foundation

class Solution {
    func countPalindromicSubsequence(_ s: String) -> Int {
        var firstIdx = Array(repeating: -1, count: 26)
        var lastIdx = Array(repeating: -1, count: 26)

        let sChars = Array(s)
        for i in 0..<sChars.count {
            let charCode = Int(sChars[i].asciiValue! - Character("a").asciiValue!)
            if firstIdx[charCode] == -1 {
                firstIdx[charCode] = i
            }
            lastIdx[charCode] = i
        }

        var totalCount = 0
        for charVal in 0..<26 {
            let fIdx = firstIdx[charVal]
            let lIdx = lastIdx[charVal]

            if fIdx != -1 && fIdx < lIdx {
                var uniqueMiddleChars = Set<Character>()
                for j in (fIdx + 1)..<lIdx {
                    uniqueMiddleChars.insert(sChars[j])
                }
                total_count += uniqueMiddleChars.count
            }
        }

        return totalCount
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
    fun countPalindromicSubsequence(s: String): Int {
        val firstIdx = IntArray(26) { -1 }
        val lastIdx = IntArray(26) { -1 }

        for (i in s.indices) {
            val charCode = s[i] - 'a'
            if (firstIdx[charCode] == -1) {
                firstIdx[charCode] = i
            }
            lastIdx[charCode] = i
        }

        var totalCount = 0
        for (charVal in 0 until 26) {
            val fIdx = firstIdx[charVal]
            val lIdx = lastIdx[charVal]

            if (fIdx != -1 && fIdx < lIdx) {
                val uniqueMiddleChars = HashSet<Char>()
                for (j in (fIdx + 1) until lIdx) {
                    uniqueMiddleChars.add(s[j])
                }
                totalCount += uniqueMiddleChars.size
            }
        }

        return totalCount
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
import 'dart:collection';

class Solution {
  int countPalindromicSubsequence(String s) {
    List<int> firstIdx = List.filled(26, -1);
    List<int> lastIdx = List.filled(26, -1);

    for (int i = 0; i < s.length; i++) {
      int charCode = s.codeUnitAt(i) - 'a'.codeUnitAt(0);
      if (firstIdx[charCode] == -1) {
        firstIdx[charCode] = i;
      }
      lastIdx[charCode] = i;
    }

    int totalCount = 0;
    for (int charVal = 0; charVal < 26; charVal++) {
      int fIdx = firstIdx[charVal];
      int lIdx = lastIdx[charVal];

      if (fIdx != -1 && fIdx < lIdx) {
        Set<String> uniqueMiddleChars = HashSet<String>();
        for (int j = fIdx + 1; j < lIdx; j++) {
          uniqueMiddleChars.add(s[j]);
        }
        totalCount += uniqueMiddleChars.length;
      }
    }

    return totalCount;
  }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

import (
	"strings"
)

// Solution for LeetCode problem
// func countPalindromicSubsequence(s string) int {
func countPalindromicSubsequence(s string) int {
    firstIdx := [26]int{}
    lastIdx := [26]int{}

    // Initialize with -1, Go's array default is 0 for int types
    for i := range firstIdx {
        firstIdx[i] = -1
        lastIdx[i] = -1
    }

    for i, charRune := range s {
        charCode := charRune - 'a'
        if firstIdx[charCode] == -1 {
            firstIdx[charCode] = i
        }
        lastIdx[charCode] = i
    }

    totalCount := 0
    for charVal := 0; charVal < 26; charVal++ {
        fIdx := firstIdx[charVal]
        lIdx := lastIdx[charVal]

        if fIdx != -1 && fIdx < lIdx {
            uniqueMiddleChars := make(map[rune]bool)
            for j := fIdx + 1; j < lIdx; j++ {
                uniqueMiddleChars[rune(s[j])] = true
            }
            totalCount += len(uniqueMiddleChars)
        }
    }

    return totalCount
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
require 'set'

class Solution
  def count_palindromic_subsequence(s)
    first_idx = Array.new(26, -1)
    last_idx = Array.new(26, -1)

    s.each_char.with_index do |char_val, i|
      idx = char_val.ord - 'a'.ord
      if first_idx[idx] == -1
        first_idx[idx] = i
      end
      last_idx[idx] = i
    end

    total_count = 0
    (0...26).each do |char_code|
      f_idx = first_idx[char_code]
      l_idx = last_idx[char_code]

      if f_idx != -1 && f_idx < l_idx
        unique_middle_chars = Set.new
        (f_idx + 1...l_idx).each do |j|
          unique_middle_chars.add(s[j])
        end
        total_count += unique_middle_chars.size
      end
    end

    total_count
  end
end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
import scala.collection.mutable

object Solution {
    def countPalindromicSubsequence(s: String): Int = {
        val firstIdx = Array.fill(26)(-1)
        val lastIdx = Array.fill(26)(-1)

        for (i <- s.indices) {
            val charCode = s(i) - 'a'
            if (firstIdx(charCode) == -1) {
                firstIdx(charCode) = i
            }
            lastIdx(charCode) = i
        }

        var totalCount = 0
        for (charVal <- 0 until 26) {
            val fIdx = firstIdx(charVal)
            val lIdx = lastIdx(charVal)

            if (fIdx != -1 && fIdx < lIdx) {
                val uniqueMiddleChars = mutable.Set[Char]()
                for (j <- (fIdx + 1) until lIdx) {
                    uniqueMiddleChars.add(s(j))
                }
                totalCount += uniqueMiddleChars.size
            }
        }

        totalCount
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
use std::collections::HashSet;

impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let s_bytes = s.as_bytes();
        let mut first_idx = [-1; 26];
        let mut last_idx = [-1; 26];

        for (i, &b) in s_bytes.iter().enumerate() {
            let char_code = (b - b'a') as usize;
            if first_idx[char_code] == -1 {
                first_idx[char_code] = i as i32;
            }
            last_idx[char_code] = i as i32;
        }

        let mut total_count = 0;
        for char_val in 0..26 {
            let f_idx = first_idx[char_val];
            let l_idx = last_idx[char_val];

            if f_idx != -1 && f_idx < l_idx {
                let mut unique_middle_chars = HashSet::new();
                for j in (f_idx + 1) as usize..(l_idx) as usize {
                    unique_middle_chars.insert(s_bytes[j]);
                }
                total_count += unique_middle_chars.len() as i32;
            }
        }

        total_count
    }
}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket
(provide (rename-out [count-palindromic-subsequence-impl countPalindromicSubsequence]))

(define (count-palindromic-subsequence-impl s)
  (define len (string-length s))
  
  (define first-idx (make-vector 26 -1))
  (define last-idx (make-vector 26 -1))

  (for ([i (in-range len)])
    (define char-code (- (char->integer (string-ref s i)) (char->integer #\a)))
    (when (= (vector-ref first-idx char-code) -1)
      (vector-set! first-idx char-code i))
    (vector-set! last-idx char-code i))

  (define total-count 0)
  (for ([char-val (in-range 26)])
    (define f-idx (vector-ref first-idx char-val))
    (define l-idx (vector-ref last-idx char-val))

    (when (and (!= f-idx -1) (< f-idx l-idx))
      (define unique-middle-chars (make-hash))
      (for ([j (in-range (+ f-idx 1) l-idx)])
        (hash-set! unique-middle-chars (string-ref s j) #t))
      (set! total-count (+ total-count (hash-count unique-middle-chars)))))

  total-count)
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
-export([count_palindromic_subsequence/1]).

count_palindromic_subsequence(S) ->
    % Initialize arrays for first and last indices. Erlang's array module is 1-indexed.
    % We map 'a' to 1, 'b' to 2, ..., 'z' to 26 for array access.
    FirstIdx = array:new(26, {default, -1}),
    LastIdx = array:new(26, {default, -1}),

    % Process the string to fill first and last index arrays
    {_,
     _,
     FirstIdxProcessed,
     LastIdxProcessed} = lists:foldl(
            fun(Char, {I, AccFirst, AccLast}) ->
                CharCode = (Char - $a) + 1, % Convert to 1-indexed for array
                
                NewAccFirst = 
                    case array:get(CharCode, AccFirst) of
                        -1 -> array:set(CharCode, I, AccFirst);
                        _ -> AccFirst
                    end,
                NewAccLast = array:set(CharCode, I, AccLast),
                {I + 1, NewAccFirst, NewAccLast}
            end,
            {0, FirstIdx, LastIdx},
            S
        ),

    % Calculate total unique palindromic subsequences
    TotalCount = lists:foldl(
            fun(CharVal0Indexed, AccTotalCount) ->
                CharCode = CharVal0Indexed + 1, % Convert to 1-indexed for array
                FIdx = array:get(CharCode, FirstIdxProcessed),
                LIdx = array:get(CharCode, LastIdxProcessed),

                if 
                    FIdx =/= -1 andalso FIdx < LIdx ->
                        % Extract the substring between fIdx and lIdx
                        % list:sublist is 1-indexed for position and count
                        % FIdx, LIdx are 0-indexed string positions
                        % Substring starts at FIdx + 1, length is (LIdx - 1) - (FIdx + 1) + 1 = LIdx - FIdx - 1
                        Subsegment = lists:sublist(S, FIdx + 1 + 1, LIdx - FIdx - 1),
                        
                        % Use gb_sets for unique middle characters
                        UniqueMiddleChars = lists:foldl(fun(C, Set) -> gb_sets:add_element(C, Set) end, gb_sets:new(), Subsegment),
                        AccTotalCount + gb_sets:size(UniqueMiddleChars);
                    true ->
                        AccTotalCount
                end
            end,
            0,
            lists:seq(0, 25) % Iterate through 'a' to 'z' (0-indexed)
        ),
    
    TotalCount.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
  @spec count_palindromic_subsequence(s :: String.t) :: integer
  def count_palindromic_subsequence(s) do
    # Initialize maps for first and last indices. Keys are 0-25 for 'a'-'z'.
    first_idx = Enum.to_list(0..25) |> Map.new(fn i -> {i, -1} end)
    last_idx = Enum.to_list(0..25) |> Map.new(fn i -> {i, -1} end)

    # Process the string to fill first and last index maps
    {first_idx_processed, last_idx_processed} = 
      s
      |> String.graphemes() # Get list of single-character strings
      |> Enum.with_index()  # Pair each character with its 0-based index
      |> Enum.reduce({first_idx, last_idx}, fn {char_str, i}, {acc_first, acc_last} ->
        char_code = String.to_charlist(char_str) |> hd() - ?a # Convert char to 0-25 code
        
        # Update first_idx if this is the first occurrence
        new_first = 
          case Map.fetch!(acc_first, char_code) do
            -1 -> Map.put(acc_first, char_code, i)
            _ -> acc_first
          end
        
        # Always update last_idx with the current index
        new_last = Map.put(acc_last, char_code, i)
        {new_first, new_last}
      end)

    # Calculate total unique palindromic subsequences
    total_count = 
      Enum.reduce(0..25, 0, fn char_val, acc_total_count ->
        f_idx = Map.fetch!(first_idx_processed, char_val)
        l_idx = Map.fetch!(last_idx_processed, char_val)

        if f_idx != -1 && f_idx < l_idx do
          # Extract the substring between f_idx and l_idx
          # Enum.slice(list, start_index, length)
          # Start index: f_idx + 1
          # Length: l_idx - (f_idx + 1)
          subsegment_chars = s |> String.graphemes() |> Enum.slice(f_idx + 1, l_idx - f_idx - 1)
          
          # Use MapSet for unique middle characters
          unique_middle_chars = MapSet.new(subsegment_chars)
          acc_total_count + MapSet.size(unique_middle_chars)
        else
          acc_total_count
        end
      end)

    total_count
  end
end
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the length of the input string `s`.

1.  **Precomputation of `first_idx_map` and `last_idx_map`**: This step involves a single pass through the input string `s`. For each character, we perform constant-time operations (array/map access and update). Thus, this part takes O(N) time.
2.  **Main Loop for `X`**: The outer loop iterates 26 times, once for each possible lowercase English letter ('a' through 'z'). This is a constant number of iterations.
    *   Inside the outer loop, retrieving `first_idx` and `last_idx` for the current `X` takes O(1) time due to precomputation.
    *   The inner loop iterates from `f_idx + 1` to `l_idx - 1`. In the worst-case scenario (e.g., `s = "azzzza"`), `f_idx` could be 0 and `l_idx` could be `N-1`. This means the inner loop could iterate up to O(N) times. Inside this inner loop, adding a character to a `Set` typically takes O(1) on average (amortized constant time).

Combining these, the total time complexity is O(N) for precomputation plus 26 * O(N) for the main loop. Since 26 is a constant, this simplifies to O(N) + O(N) = O(N).
- **Space Complexity:** The space complexity is O(1).

1.  `first_idx_map` and `last_idx_map`: These arrays each store 26 integer values (one for each character of the alphabet). This constitutes O(26) = O(1) space, as the size is constant regardless of the input string length.
2.  `unique_middle_chars` set: This set stores unique characters found within the middle segment of `s`. In the worst case, it might contain all 26 lowercase English letters. This also constitutes O(26) = O(1) space.

Since the auxiliary space used is bounded by a constant (related to the size of the English alphabet) and does not grow with the input string length N, the overall space complexity is O(1).
