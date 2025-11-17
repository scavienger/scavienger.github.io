---
layout: post
title: "Number of Substrings With Only 1s"
date: 2025-11-16 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "String"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-substrings-with-only-1s/
---

## Problem #1513: Number of Substrings With Only 1s

**Difficulty:** Medium

**Topics:** Math, String

## Problem Description

Given a binary string `s`, return _the number of substrings with all characters_ `1` _'s_. Since the answer may be too large, return it modulo `109 + 7`.

**Example 1:**

``` Input: s = "0110111" Output: 9 Explanation: There are 9 substring in total with only 1's characters. "1" -> 5 times. "11" -> 3 times. "111" -> 1 time. ``` 

**Example 2:**

``` Input: s = "101" Output: 2 Explanation: Substring "1" is shown 2 times in s. ``` 

**Example 3:**

``` Input: s = "111111" Output: 21 Explanation: Each substring contains only 1's characters. ``` 

**Constraints:**

  * `1 <= s.length <= 105`
  * `s[i]` is either `'0'` or `'1'`.

## Hints

1. Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.

## ⚡ AI-Generated Solution (llama-3.3-70b-versatile)

### Approach

The approach to solve this problem is to iterate through the binary string and count the number of consecutive 1s. For each group of consecutive 1s, calculate the total number of substrings that can be formed using the formula (n + 1) * n // 2, where n is the number of consecutive 1s. This formula is derived from the fact that for a group of n consecutive 1s, there are n substrings of length 1, n-1 substrings of length 2, ..., and 1 substring of length n. The total number of substrings is the sum of the first n natural numbers, which is given by the formula n * (n + 1) // 2.

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
class Solution {
       public:
           int numSub(string s) {
               long long res = 0;
               long long count = 0;
               for (char c : s) {
                   if (c == '1') {
                       count++;
                   } else {
                       res += count * (count + 1) / 2;
                       count = 0;
                   }
               }
               res += count * (count + 1) / 2;
               return res % (1e9 + 7);
           }
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {
           public int numSub(String s) {
               long res = 0;
               long count = 0;
               for (char c : s.toCharArray()) {
                   if (c == '1') {
                       count++;
                   } else {
                       res += count * (count + 1) / 2;
                       count = 0;
                   }
               }
               res += count * (count + 1) / 2;
               return (int)(res % (1e9 + 7));
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution:
           def numSub(self, s: str) -> int:
               res = 0
               count = 0
               for c in s:
                   if c == '1':
                       count += 1
                   else:
                       res += count * (count + 1) // 2
                       count = 0
               res += count * (count + 1) // 2
               return res % (10**9 + 7)
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution:
           def numSub(self, s: str) -> int:
               res = 0
               count = 0
               for c in s:
                   if c == '1':
                       count += 1
                   else:
                       res += count * (count + 1) // 2
                       count = 0
               res += count * (count + 1) // 2
               return res % (10**9 + 7)
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
#include <stdio.h>
       #include <string.h>

       int numSub(char * s){
           long long res = 0;
           long long count = 0;
           for (int i = 0; i < strlen(s); i++) {
               if (s[i] == '1') {
                   count++;
               } else {
                   res += count * (count + 1) / 2;
                   count = 0;
               }
           }
           res += count * (count + 1) / 2;
           return res % (1000000007);
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {
           public int NumSub(string s) {
               long res = 0;
               long count = 0;
               foreach (char c in s) {
                   if (c == '1') {
                       count++;
                   } else {
                       res += count * (count + 1) / 2;
                       count = 0;
                   }
               }
               res += count * (count + 1) / 2;
               return (int)(res % (1000000007));
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
var numSub = function(s) {
           let res = 0;
           let count = 0;
           for (let c of s) {
               if (c == '1') {
                   count++;
               } else {
                   res += count * (count + 1) / 2;
                   count = 0;
               }
           }
           res += count * (count + 1) / 2;
           return res % (1000000007);
       };
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function numSub(s: string): number {
           let res: number = 0;
           let count: number = 0;
           for (let c of s) {
               if (c == '1') {
                   count++;
               } else {
                   res += count * (count + 1) / 2;
                   count = 0;
               }
           }
           res += count * (count + 1) / 2;
           return res % (1000000007);
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
class Solution {
           function numSub($s) {
               $res = 0;
               $count = 0;
               for ($i = 0; $i < strlen($s); $i++) {
                   if ($s[$i] == '1') {
                       $count++;
                   } else {
                       $res += $count * ($count + 1) / 2;
                       $count = 0;
                   }
               }
               $res += $count * ($count + 1) / 2;
               return $res % (1000000007);
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {
           func numSub(_ s: String) -> Int {
               var res: Int64 = 0
               var count: Int64 = 0
               for c in s {
                   if c == "1" {
                       count += 1
                   } else {
                       res += count * (count + 1) / 2
                       count = 0
                   }
               }
               res += count * (count + 1) / 2
               return Int(res % 1000000007)
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {
           fun numSub(s: String): Int {
               var res: Long = 0
               var count: Long = 0
               for (c in s) {
                   if (c == '1') {
                       count++
                   } else {
                       res += count * (count + 1) / 2
                       count = 0
                   }
               }
               res += count * (count + 1) / 2
               return (res % 1000000007).toInt()
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {
           int numSub(String s) {
               int res = 0;
               int count = 0;
               for (var c in s.split('')) {
                   if (c == '1') {
                       count++;
                   } else {
                       res += count * (count + 1) ~/ 2;
                       count = 0;
                   }
               }
               res += count * (count + 1) ~/ 2;
               return res % 1000000007;
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
package main

       import (
           "fmt"
       )

       func numSub(s string) int {
           res := 0
           count := 0
           for _, c := range s {
               if c == '1' {
                   count++
               } else {
                   res += count * (count + 1) / 2
                   count = 0
               }
           }
           res += count * (count + 1) / 2
           return res % 1000000007
       }

       func main() {
           fmt.Println(numSub("0110111")) // 9
           fmt.Println(numSub("101")) // 2
           fmt.Println(numSub("111111")) // 21
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
# @param {String} s
       # @return {Integer}
       def num_sub(s)
           res = 0
           count = 0
           s.each_char do |c|
               if c == '1'
                   count += 1
               else
                   res += count * (count + 1) / 2
                   count = 0
               end
           end
           res += count * (count + 1) / 2
           res % 1000000007
       end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {
           def numSub(s: String): Int = {
               var res: Long = 0
               var count: Long = 0
               for (c <- s) {
                   if (c == '1') {
                       count += 1
                   } else {
                       res += count * (count + 1) / 2
                       count = 0
                   }
               }
               res += count * (count + 1) / 2
               (res % 1000000007).toInt
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {
           pub fn num_sub(s: String) -> i32 {
               let mut res: i64 = 0;
               let mut count: i64 = 0;
               for c in s.chars() {
                   if c == '1' {
                       count += 1;
                   } else {
                       res += count * (count + 1) / 2;
                       count = 0;
                   }
               }
               res += count * (count + 1) / 2;
               (res % 1000000007) as i32
           }
       }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
#lang racket

       (define (num-sub s)
           (let loop ((res 0)
                     (count 0)
                     (s s))
             (cond
               ((null? s) (modulo (+ res (* count (add1 count)) / 2) 1000000007))
               ((eq? (car s) #\1) (loop res (add1 count) (cdr s)))
               (else (loop (+ res (* count (add1 count)) / 2) 0 (cdr s))))))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution).
       -export([num_sub/1]).

       num_sub(S) ->
           num_sub(S, 0, 0).

       num_sub([], Res, Count) ->
           (Res + Count * (Count + 1) div 2) rem 1000000007;
       num_sub([C|Cs], Res, Count) ->
           case C of
               $1 -> num_sub(Cs, Res, Count + 1);
               _ -> num_sub(Cs, Res + Count * (Count + 1) div 2, 0)
           end.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do
           def num_sub(s) do
               num_sub(s, 0, 0)
           end

           defp num_sub([], res, count) do
               (res + count * (count + 1) div 2) rem 1_000_000_007
           end

           defp num_sub([c|cs], res, count) do
               case c do
                   ?1 -> num_sub(cs, res, count + 1)
                   _ -> num_sub(cs, res + count * (count + 1) div 2, 0)
               end
           end
       end
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the binary string. This is because we are iterating through the string once.

- **Space Complexity:** O(1), as we are using a constant amount of space to store the count of consecutive 1s and the total number of substrings.
