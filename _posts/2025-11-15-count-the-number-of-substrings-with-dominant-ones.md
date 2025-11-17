---
layout: post
title: "Count the Number of Substrings With Dominant Ones"
date: 2025-11-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Sliding Window", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
---

## Problem #3234: Count the Number of Substrings With Dominant Ones

**Difficulty:** Medium

**Topics:** String, Sliding Window, Enumeration

## Problem Description

You are given a binary string `s`.

Return the number of substrings with **dominant** ones.

A string has **dominant** ones if the number of ones in the string is **greater than or equal to** the **square** of the number of zeros in the string.

**Example 1:**

**Input:** s = "00011"

**Output:** 5

**Explanation:**

The substrings with dominant ones are shown in the table below.

``` i j s[i..j] Number of Zeros Number of Ones 3 3 1 0 1 4 4 1 0 1 2 3 01 1 1 3 4 11 0 2 2 4 011 1 2 ``` 

**Example 2:**

**Input:** s = "101101"

**Output:** 16

**Explanation:**

The substrings with **non-dominant** ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

``` i j s[i..j] Number of Zeros Number of Ones 1 1 0 1 0 4 4 0 1 0 1 4 0110 2 2 0 4 10110 2 3 1 5 01101 2 3 ``` 

**Constraints:**

  * `1 <= s.length <= 4 * 104`
  * `s` consists only of characters `'0'` and `'1'`.

## Hints

1. Let us fix the starting index <code>l</code> of the substring and count the number of indices <code>r</code> such that <code>l <= r</code> and the substring <code>s[l..r]</code> has dominant ones.

2. A substring with dominant ones has at most <code>sqrt(n)</code> zeros.

3. We cannot iterate over every <code>r</code> and check if the  <code>s[l..r]</code> has dominant ones. Instead, we iterate over the next <code>sqrt(n)</code> zeros to the left of <code>l</code> and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.

## ⚡ AI-Generated Solution (llama-3.3-70b-versatile)

### Approach

The approach to solve this problem is to iterate over the string and for each character, count the number of substrings that have dominant ones. A substring has dominant ones if the number of ones in the substring is greater than or equal to the square of the number of zeros in the substring. We can use a sliding window approach to efficiently count the number of substrings with dominant ones.

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
#include <iostream>
         #include <string>
         using namespace std;

         class Solution {
         public:
             int numberOfSubstrings(string s) {
                 int n = s.size();
                 int count = 0;
                 for (int i = 0; i < n; i++) {
                     int ones = 0;
                     int zeros = 0;
                     for (int j = i; j < n; j++) {
                         if (s[j] == '1') ones++;
                         else zeros++;
                         if (ones >= zeros * zeros) count++;
                     }
                 }
                 return count;
             }
         };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
public class Solution {
             public int numberOfSubstrings(String s) {
                 int n = s.length();
                 int count = 0;
                 for (int i = 0; i < n; i++) {
                     int ones = 0;
                     int zeros = 0;
                     for (int j = i; j < n; j++) {
                         if (s.charAt(j) == '1') ones++;
                         else zeros++;
                         if (ones >= zeros * zeros) count++;
                     }
                 }
                 return count;
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
             def numberOfSubstrings(self, s: str) -> int:
                 n = len(s)
                 count = 0
                 for i in range(n):
                     ones = 0
                     zeros = 0
                     for j in range(i, n):
                         if s[j] == '1': ones += 1
                         else: zeros += 1
                         if ones >= zeros * zeros: count += 1
                 return count
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
             def numberOfSubstrings(self, s: str) -> int:
                 n = len(s)
                 count = 0
                 for i in range(n):
                     ones = 0
                     zeros = 0
                     for j in range(i, n):
                         if s[j] == '1': ones += 1
                         else: zeros += 1
                         if ones >= zeros * zeros: count += 1
                 return count
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdio.h>
         #include <string.h>

         int numberOfSubstrings(char * s){
             int n = strlen(s);
             int count = 0;
             for (int i = 0; i < n; i++) {
                 int ones = 0;
                 int zeros = 0;
                 for (int j = i; j < n; j++) {
                     if (s[j] == '1') ones++;
                     else zeros++;
                     if (ones >= zeros * zeros) count++;
                 }
             }
             return count;
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
             public int NumberOfSubstrings(string s) {
                 int n = s.Length;
                 int count = 0;
                 for (int i = 0; i < n; i++) {
                     int ones = 0;
                     int zeros = 0;
                     for (int j = i; j < n; j++) {
                         if (s[j] == '1') ones++;
                         else zeros++;
                         if (ones >= zeros * zeros) count++;
                     }
                 }
                 return count;
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
var numberOfSubstrings = function(s) {
             let n = s.length;
             let count = 0;
             for (let i = 0; i < n; i++) {
                 let ones = 0;
                 let zeros = 0;
                 for (let j = i; j < n; j++) {
                     if (s[j] === '1') ones++;
                     else zeros++;
                     if (ones >= zeros * zeros) count++;
                 }
             }
             return count;
         };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function numberOfSubstrings(s: string): number {
             let n: number = s.length;
             let count: number = 0;
             for (let i: number = 0; i < n; i++) {
                 let ones: number = 0;
                 let zeros: number = 0;
                 for (let j: number = i; j < n; j++) {
                     if (s[j] === '1') ones++;
                     else zeros++;
                     if (ones >= zeros * zeros) count++;
                 }
             }
             return count;
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
             function numberOfSubstrings($s) {
                 $n = strlen($s);
                 $count = 0;
                 for ($i = 0; $i < $n; $i++) {
                     $ones = 0;
                     $zeros = 0;
                     for ($j = $i; $j < $n; $j++) {
                         if ($s[$j] == '1') $ones++;
                         else $zeros++;
                         if ($ones >= $zeros * $zeros) $count++;
                     }
                 }
                 return $count;
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
             func numberOfSubstrings(_ s: String) -> Int {
                 let n = s.count
                 var count = 0
                 for i in 0..<n {
                     var ones = 0
                     var zeros = 0
                     for j in i..<n {
                         if s[s.index(s.startIndex, offsetBy: j)] == "1" {
                             ones += 1
                         } else {
                             zeros += 1
                         }
                         if ones >= zeros * zeros {
                             count += 1
                         }
                     }
                 }
                 return count
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
             fun numberOfSubstrings(s: String): Int {
                 val n = s.length
                 var count = 0
                 for (i in 0 until n) {
                     var ones = 0
                     var zeros = 0
                     for (j in i until n) {
                         if (s[j] == '1') ones++
                         else zeros++
                         if (ones >= zeros * zeros) count++
                     }
                 }
                 return count
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
             int numberOfSubstrings(String s) {
                 int n = s.length;
                 int count = 0;
                 for (int i = 0; i < n; i++) {
                     int ones = 0;
                     int zeros = 0;
                     for (int j = i; j < n; j++) {
                         if (s[j] == '1') ones++;
                         else zeros++;
                         if (ones >= zeros * zeros) count++;
                     }
                 }
                 return count;
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func numberOfSubstrings(s string) int {
             n := len(s)
             count := 0
             for i := 0; i < n; i++ {
                 ones := 0
                 zeros := 0
                 for j := i; j < n; j++ {
                     if s[j] == '1' {
                         ones++
                     } else {
                         zeros++
                     }
                     if ones >= zeros * zeros {
                         count++
                     }
                 }
             }
             return count
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {String} s
         # @return {Integer}
         def number_of_substrings(s)
             n = s.size
             count = 0
             (0...n).each do |i|
                 ones = 0
                 zeros = 0
                 (i...n).each do |j|
                     if s[j] == '1'
                         ones += 1
                     else
                         zeros += 1
                     end
                     count += 1 if ones >= zeros * zeros
                 end
             end
             count
         end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
             def numberOfSubstrings(s: String): Int = {
                 val n = s.length
                 var count = 0
                 for (i <- 0 until n) {
                     var ones = 0
                     var zeros = 0
                     for (j <- i until n) {
                         if (s(j) == '1') ones += 1
                         else zeros += 1
                         if (ones >= zeros * zeros) count += 1
                     }
                 }
                 count
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
             pub fn number_of_substrings(s: String) -> i32 {
                 let n = s.len();
                 let mut count = 0;
                 for i in 0..n {
                     let mut ones = 0;
                     let mut zeros = 0;
                     for j in i..n {
                         if s.as_bytes()[j] == b'1' {
                             ones += 1;
                         } else {
                             zeros += 1;
                         }
                         if ones >= zeros * zeros {
                             count += 1;
                         }
                     }
                 }
                 count
             }
         }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket
         (define (number-of-substrings s)
           (define n (string-length s))
           (define count 0)
           (for ([i (range n)])
             (define ones 0)
             (define zeros 0)
             (for ([j (range i n)])
               (if (eq? (string-ref s j) #\1)
                   (set! ones (add1 ones))
                   (set! zeros (add1 zeros)))
               (if (>= ones (* zeros zeros))
                   (set! count (add1 count)))))
           count)
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
         -export([number_of_substrings/1]).

         number_of_substrings(S) ->
             N = length(S),
             Count = count_substrings(S, N, 0, 0, 0),
             Count.

         count_substrings(_, 0, _, _, Count) ->
             Count;
         count_substrings(S, N, I, Ones, Count) ->
             case lists:nth(I, S) of
                 $1 ->
                     count_substrings(S, N - 1, I + 1, Ones + 1, Count);
                 $0 ->
                     count_substrings(S, N - 1, I + 1, Ones, Count + 1)
             end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
           def number_of_substrings(s) do
             n = String.length(s)
             count = 0
             for i <- 0..n-1 do
               ones = 0
               zeros = 0
               for j <- i..n-1 do
                 if String.at(s, j) == "1" do
                   ones = ones + 1
                 else
                   zeros = zeros + 1
                 end
                 if ones >= zeros * zeros do
                   count = count + 1
                 end
               end
             end
             count
           end
         end
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(n^2) where n is the length of the string, because for each character in the string, we are potentially iterating over the rest of the string to count the number of substrings with dominant ones.

- **Space Complexity:** O(1) because we are not using any additional space that scales with the input size.
