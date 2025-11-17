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

The problem can be solved by counting the number of consecutive '1's in the string and calculating the total number of substrings that can be formed from each group of consecutive '1's. For a group with n consecutive '1's, the total contribution of it to the final answer is (n + 1) * n // 2. We iterate through the string, counting consecutive '1's and adding the contribution of each group to the total count. The result is then returned modulo 10^9 + 7 to prevent overflow.

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
class Solution {public: int numSub(string s) {const int MOD = 1e9 + 7; int count = 0, total = 0; for (char c : s) {if (c == '1') {count++;} else {total = (total + count * (count + 1) / 2) % MOD; count = 0;}} return (total + count * (count + 1) / 2) % MOD;}}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
class Solution {public int numSub(String s) {final int MOD = (int) 1e9 + 7; int count = 0, total = 0; for (char c : s.toCharArray()) {if (c == '1') {count++;} else {total = (total + (int) ((long) count * (count + 1) / 2)) % MOD; count = 0;}} return (total + (int) ((long) count * (count + 1) / 2)) % MOD;}}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
class Solution: def numSub(self, s: str) -> int: MOD = 10**9 + 7; count, total = 0, 0; for c in s: if c == '1': count += 1; else: total = (total + count * (count + 1) // 2) % MOD; count = 0; return (total + count * (count + 1) // 2) % MOD
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
class Solution: def numSub(self, s: str) -> int: MOD = 10**9 + 7; count, total = 0, 0; for c in s: if c == '1': count += 1; else: total = (total + count * (count + 1) // 2) % MOD; count = 0; return (total + count * (count + 1) // 2) % MOD
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
typedef struct {int val;} Solution; int numSub(char * s){const int MOD = 1000000007; int count = 0, total = 0; while (*s) {if (*s == '1') {count++;} else {total = (total + count * (count + 1) / 2) % MOD; count = 0;} s++;} return (total + count * (count + 1) / 2) % MOD;}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
public class Solution {public int NumSub(string s) {const int MOD = 1000000007; int count = 0, total = 0; foreach (char c in s) {if (c == '1') {count++;} else {total = (total + count * (count + 1) / 2) % MOD; count = 0;}} return (total + count * (count + 1) / 2) % MOD;}}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
var numSub = function(s) {const MOD = 1000000007; let count = 0, total = 0; for (let c of s) {if (c == '1') {count++;} else {total = (total + count * (count + 1) / 2) % MOD; count = 0;}} return (total + count * (count + 1) / 2) % MOD;}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
function numSub(s: string): number {const MOD: number = 1000000007; let count: number = 0, total: number = 0; for (let c of s) {if (c == '1') {count++;} else {total = (total + count * (count + 1) / 2) % MOD; count = 0;}} return (total + count * (count + 1) / 2) % MOD;}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
$MOD = 1000000007; function numSub($s) { $count = 0; $total = 0; for ($i = 0; $i < strlen($s); $i++) { if ($s[$i] == '1') { $count++; } else { $total = ($total + $count * ($count + 1) / 2) % $GLOBALS['MOD']; $count = 0; } } return ($total + $count * ($count + 1) / 2) % $GLOBALS['MOD']; }
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
class Solution {func numSub(_ s: String) -> Int {let MOD = 1000000007; var count = 0; var total = 0; for c in s {if c == "1" {count += 1} else {total = (total + count * (count + 1) / 2) % MOD; count = 0}} return (total + count * (count + 1) / 2) % MOD}}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
class Solution {fun numSub(s: String): Int {val MOD = 1000000007; var count = 0; var total = 0; for (c in s) {if (c == '1') {count++} else {total = (total + count * (count + 1) / 2) % MOD; count = 0}} return (total + count * (count + 1) / 2) % MOD}}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
class Solution {int numSub(String s) {const int MOD = 1000000007; int count = 0, total = 0; for (var c in s.split('')) {if (c == '1') {count++;} else {total = (total + count * (count + 1) ~/ 2) % MOD; count = 0;}} return (total + count * (count + 1) ~/ 2) % MOD;}}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
func numSub(s string) int {const MOD int = 1e9 + 7; count, total := 0, 0; for _, c := range s {if c == '1' {count++} else {total = (total + count*(count+1)/2) % MOD; count = 0}} return (total + count*(count+1)/2) % MOD}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
def num_sub(s); MOD = 10**9 + 7; count, total = 0, 0; s.each_char do |c|; if c == '1'; then count += 1; else; total = (total + count * (count + 1) / 2) % MOD; count = 0; end; end; (total + count * (count + 1) / 2) % MOD; end
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
object Solution {def numSub(s: String): Int = {val MOD = 1000000007; var count = 0; var total = 0; for (c <- s) {if (c == '1') {count += 1} else {total = (total + count * (count + 1) / 2) % MOD; count = 0}} (total + count * (count + 1) / 2) % MOD}}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
impl Solution {pub fn num_sub(s: String) -> i32 {const MOD: i32 = 1000000007; let mut count = 0; let mut total: i64 = 0; for c in s.chars() {if c == '1' {count += 1} else {total = (total + (count as i64) * (count as i64 + 1) / 2) % MOD as i64; count = 0}} (total + (count as i64) * (count as i64 + 1) / 2) as i32 % MOD}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
(define (numSub s) (define MOD 1000000007) (define count 0) (define total 0) (for ([c (string->list s)]) (if (eq? c #\1) (set! count (+ count 1)) (begin (set! total (modulo (+ total (/ (* count (+ count 1)) 2)) MOD)) (set! count 0)))) (modulo (+ total (/ (* count (+ count 1)) 2)) MOD))
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
-module(solution). -export([numSub/1]). numSub(S) -> MOD = 1000000007, numSub(S, 0, 0, MOD). numSub([H|T], Count, Total, MOD) when H =:= $1 -> numSub(T, Count + 1, Total, MOD); numSub([_|T], Count, Total, MOD) -> NewTotal = (Total + Count * (Count + 1) div 2) rem MOD, numSub(T, 0, NewTotal, MOD); numSub([], Count, Total, MOD) -> (Total + Count * (Count + 1) div 2) rem MOD.
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
defmodule Solution do def num_sub(s) do mod = 1_000_000_007; num_sub(s, 0, 0, mod) end defp num_sub([?1|t], count, total, mod) do num_sub(t, count + 1, total, mod) end defp num_sub([_|t], count, total, mod) do new_total = rem(total + count * (count + 1) div 2, mod); num_sub(t, 0, new_total, mod) end defp num_sub([], count, total, mod) do rem(total + count * (count + 1) div 2, mod) end end
{% endhighlight %}

  </div>

</div>


### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input string, because we are iterating through the string once to count consecutive '1's.

- **Space Complexity:** O(1) because we are using a constant amount of space to store the count of consecutive '1's and the total count.
