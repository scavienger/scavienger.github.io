---
layout: post
title: "Count the Number of Computer Unlocking Permutations"
date: 2025-12-10 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Brainteaser", "Combinatorics"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countPermutations(vector<int>& complexity)\
        \ {\n        const long long mod = 1000000007;\n        int n = complexity.size();\n\
        \        for (int i = 1; i < n; ++i) {\n            if (complexity[i] <= complexity[0])\
        \ {\n                return 0;\n            }\n        }\n        long long\
        \ result = 1;\n        for (int i = 2; i < n; ++i) {\n            result = result\
        \ * i % mod;\n        }\n        return static_cast<int>(result);\n    }\n};"
      java: "class Solution {\n    public int countPermutations(int[] complexity) {\n\
        \        final long mod = 1000000007L;\n        int n = complexity.length;\n\
        \        for (int i = 1; i < n; i++) {\n            if (complexity[i] <= complexity[0])\
        \ {\n                return 0;\n            }\n        }\n        long result\
        \ = 1;\n        for (int i = 2; i < n; i++) {\n            result = result *\
        \ i % mod;\n        }\n        return (int) result;\n    }\n}"
      python: "class Solution(object):\n    def countPermutations(self, complexity):\n\
        \        \"\"\"\n        :type complexity: List[int]\n        :rtype: int\n\
        \        \"\"\"\n        mod = 10**9 + 7\n        n = len(complexity)\n    \
        \    for i in range(1, n):\n            if complexity[i] <= complexity[0]:\n\
        \                return 0\n        result = 1\n        for i in range(2, n):\n\
        \            result = result * i % mod\n        return result"
      python3: "class Solution:\n    def countPermutations(self, complexity: List[int])\
        \ -> int:\n        mod = 10**9 + 7\n        n = len(complexity)\n        for\
        \ i in range(1, n):\n            if complexity[i] <= complexity[0]:\n      \
        \          return 0\n        result = 1\n        for i in range(2, n):\n   \
        \         result = result * i % mod\n        return result"
      c: "int countPermutations(int* complexity, int complexitySize) {\n    const long\
        \ long mod = 1000000007;\n    for (int i = 1; i < complexitySize; ++i) {\n \
        \       if (complexity[i] <= complexity[0]) {\n            return 0;\n     \
        \   }\n    }\n    long long result = 1;\n    for (int i = 2; i < complexitySize;\
        \ ++i) {\n        result = result * i % mod;\n    }\n    return (int) result;\n\
        }"
      csharp: "public class Solution {\n    public int CountPermutations(int[] complexity)\
        \ {\n        const long mod = 1000000007;\n        int n = complexity.Length;\n\
        \        for (int i = 1; i < n; i++) {\n            if (complexity[i] <= complexity[0])\
        \ {\n                return 0;\n            }\n        }\n        long result\
        \ = 1;\n        for (int i = 2; i < n; i++) {\n            result = result *\
        \ i % mod;\n        }\n        return (int)result;\n    }\n}"
      javascript: "/**\n * @param {number[]} complexity\n * @return {number}\n */\n\
        var countPermutations = function(complexity) {\n    const mod = 1000000007;\n\
        \    const n = complexity.length;\n    for (let i = 1; i < n; i++) {\n     \
        \   if (complexity[i] <= complexity[0]) {\n            return 0;\n        }\n\
        \    }\n    let result = 1;\n    for (let i = 2; i < n; i++) {\n        result\
        \ = (result * i) % mod;\n    }\n    return result;\n};"
      typescript: "function countPermutations(complexity: number[]): number {\n    const\
        \ mod = 1000000007;\n    const n = complexity.length;\n    for (let i = 1; i\
        \ < n; i++) {\n        if (complexity[i] <= complexity[0]) {\n            return\
        \ 0;\n        }\n    }\n    let result = 1;\n    for (let i = 2; i < n; i++)\
        \ {\n        result = (result * i) % mod;\n    }\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $complexity\n     *\
        \ @return Integer\n     */\n    function countPermutations($complexity) {\n\
        \        $mod = 1000000007;\n        $n = count($complexity);\n        for ($i\
        \ = 1; $i < $n; $i++) {\n            if ($complexity[$i] <= $complexity[0])\
        \ {\n                return 0;\n            }\n        }\n        $result =\
        \ 1;\n        for ($i = 2; $i < $n; $i++) {\n            $result = ($result\
        \ * $i) % $mod;\n        }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func countPermutations(_ complexity: [Int]) -> Int\
        \ {\n        let mod = 1_000_000_007\n        let n = complexity.count\n   \
        \     for i in 1..<n {\n            if complexity[i] <= complexity[0] {\n  \
        \              return 0\n            }\n        }\n        var result = 1\n\
        \        if n > 2 {\n            for i in 2..<n {\n                result =\
        \ (result * i) % mod\n            }\n        }\n        return result\n    }\n\
        }"
      kotlin: "class Solution {\n    fun countPermutations(complexity: IntArray): Int\
        \ {\n        val n = complexity.size\n        for (i in 1 until n) {\n     \
        \       if (complexity[i] <= complexity[0]) return 0\n        }\n        val\
        \ mod = 1_000_000_007L\n        var result = 1L\n        for (i in 2 until n)\
        \ {\n            result = result * i % mod\n        }\n        return result.toInt()\n\
        \    }\n}"
      dart: "class Solution {\n  int countPermutations(List<int> complexity) {\n   \
        \ final n = complexity.length;\n    for (var i = 1; i < n; i++) {\n      if\
        \ (complexity[i] <= complexity[0]) return 0;\n    }\n    const mod = 1000000007;\n\
        \    var result = 1;\n    for (var i = 2; i < n; i++) {\n      result = result\
        \ * i % mod;\n    }\n    return result;\n  }\n}"
      go: "func countPermutations(complexity []int) int {\n\tn := len(complexity)\n\t\
        for i := 1; i < n; i++ {\n\t\tif complexity[i] <= complexity[0] {\n\t\t\treturn\
        \ 0\n\t\t}\n\t}\n\tconst mod = 1000000007\n\tresult := 1\n\tfor i := 2; i <\
        \ n; i++ {\n\t\tresult = result * i % mod\n\t}\n\treturn result\n}"
      ruby: "# @param {Integer[]} complexity\n# @return {Integer}\ndef count_permutations(complexity)\n\
        \  n = complexity.length\n  (1...n).each do |i|\n    return 0 if complexity[i]\
        \ <= complexity[0]\n  end\n  mod = 1_000_000_007\n  result = 1\n  (2...n).each\
        \ do |i|\n    result = result * i % mod\n  end\n  result\nend"
      scala: "object Solution {\n    def countPermutations(complexity: Array[Int]):\
        \ Int = {\n        val n = complexity.length\n        for (i <- 1 until n) {\n\
        \            if (complexity(i) <= complexity(0)) return 0\n        }\n     \
        \   val mod = 1000000007L\n        var result = 1L\n        for (i <- 2 until\
        \ n) {\n            result = result * i % mod\n        }\n        result.toInt\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn count_permutations(complexity: Vec<i32>) ->\
        \ i32 {\n        let n = complexity.len();\n        for i in 1..n {\n      \
        \      if complexity[i] <= complexity[0] {\n                return 0;\n    \
        \        }\n        }\n        let modulus = 1_000_000_007i64;\n        let\
        \ mut result = 1i64;\n        for i in 2..n {\n            result = result *\
        \ i as i64 % modulus;\n        }\n        result as i32\n    }\n}"
      racket: "(define/contract (count-permutations complexity)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let ([first (car complexity)])\n    (if (ormap (lambda\
        \ (value) (<= value first)) (cdr complexity))\n        0\n        (let loop\
        \ ([i 2] [result 1])\n          (if (>= i (length complexity))\n           \
        \   result\n              (loop (add1 i) (modulo (* result i) 1000000007)))))))"
      erlang: "-spec count_permutations(Complexity :: [integer()]) -> integer().\ncount_permutations(Complexity)\
        \ ->\n  [First | Rest] = Complexity,\n  case lists:any(fun(Value) -> Value =<\
        \ First end, Rest) of\n    true -> 0;\n    false -> factorial_mod(2, length(Complexity),\
        \ 1)\n  end.\n\nfactorial_mod(I, N, Result) when I >= N -> Result;\nfactorial_mod(I,\
        \ N, Result) ->\n  factorial_mod(I + 1, N, (Result * I) rem 1000000007)."
      elixir: "defmodule Solution do\n  @spec count_permutations(complexity :: [integer])\
        \ :: integer\n  def count_permutations(complexity) do\n    [first | rest] =\
        \ complexity\n\n    if Enum.any?(rest, &(&1 <= first)) do\n      0\n    else\n\
        \      Enum.reduce(2..(length(complexity) - 1), 1, fn i, result ->\n       \
        \ rem(result * i, 1_000_000_007)\n      end)\n    end\n  end\nend"
    approach: 'Computer 0 must be first in every valid unlocking order, because it is
      the only computer initially unlocked. If any later computer has complexity less
      than or equal to complexity[0], it cannot be unlocked: every computer that could
      unlock it has a smaller index and therefore has complexity at least complexity[0].
      In that case, return 0.


      Otherwise, computer 0 has strictly lower complexity than every other computer,
      so it can unlock every computer directly. The remaining n - 1 computers can appear
      in any order, giving (n - 1)! permutations modulo 10^9 + 7.'
    time_complexity: O(n), to check all complexities and calculate the factorial.
    space_complexity: O(1), using only a constant amount of extra space.
    elapsed_time: 58.908283948898315
    model: gpt-6-luna
    generated_at: '2026-11-12 23:58:11 '
---

## Problem #3577: Count the Number of Computer Unlocking Permutations

**Difficulty:** Medium

**Topics:** Array, Math, Brainteaser, Combinatorics

## Problem Description

<p>You are given an array <code>complexity</code> of length <code>n</code>.</p>

<p>There are <code>n</code> <strong>locked</strong> computers in a room with labels from 0 to <code>n - 1</code>, each with its own <strong>unique</strong> password. The password of the computer <code>i</code> has a complexity <code>complexity[i]</code>.</p>

<p>The password for the computer labeled 0 is <strong>already</strong> decrypted and serves as the root. All other computers must be unlocked using it or another previously unlocked computer, following this information:</p>

<ul>
	<li>You can decrypt the password for the computer <code>i</code> using the password for computer <code>j</code>, where <code>j</code> is <strong>any</strong> integer less than <code>i</code> with a lower complexity. (i.e. <code>j &lt; i</code> and <code>complexity[j] &lt; complexity[i]</code>)</li>
	<li>To decrypt the password for computer <code>i</code>, you must have already unlocked a computer <code>j</code> such that <code>j &lt; i</code> and <code>complexity[j] &lt; complexity[i]</code>.</li>
</ul>

<p>Find the number of <span data-keyword="permutation-array">permutations</span> of <code>[0, 1, 2, ..., (n - 1)]</code> that represent a valid order in which the computers can be unlocked, starting from computer 0 as the only initially unlocked one.</p>

<p>Since the answer may be large, return it <strong>modulo</strong> 10<sup>9</sup> + 7.</p>

<p><strong>Note</strong> that the password for the computer <strong>with label</strong> 0 is decrypted, and <em>not</em> the computer with the first position in the permutation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">complexity = [1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The valid permutations are:</p>

<ul>
	<li>[0, 1, 2]
	<ul>
		<li>Unlock computer 0 first with root password.</li>
		<li>Unlock computer 1 with password of computer 0 since <code>complexity[0] &lt; complexity[1]</code>.</li>
		<li>Unlock computer 2 with password of computer 1 since <code>complexity[1] &lt; complexity[2]</code>.</li>
	</ul>
	</li>
	<li>[0, 2, 1]
	<ul>
		<li>Unlock computer 0 first with root password.</li>
		<li>Unlock computer 2 with password of computer 0 since <code>complexity[0] &lt; complexity[2]</code>.</li>
		<li>Unlock computer 1 with password of computer 0 since <code>complexity[0] &lt; complexity[1]</code>.</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">complexity = [3,3,3,4,4,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no possible permutations which can unlock all computers.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= complexity.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= complexity[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Ensure that the element at index 0 has the unique minimum complexity (no other element can match its value).

2. Fix index 0 as the first in the unlocking order.

3. The remaining indices from `1` to `n - 1` can then be arranged arbitrarily, yielding `factorial(n - 1)` possible orders.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Computer 0 must be first in every valid unlocking order, because it is the only computer initially unlocked. If any later computer has complexity less than or equal to complexity[0], it cannot be unlocked: every computer that could unlock it has a smaller index and therefore has complexity at least complexity[0]. In that case, return 0.

Otherwise, computer 0 has strictly lower complexity than every other computer, so it can unlock every computer directly. The remaining n - 1 computers can appear in any order, giving (n - 1)! permutations modulo 10^9 + 7.

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
    int countPermutations(vector<int>& complexity) {
        const long long mod = 1000000007;
        int n = complexity.size();
        for (int i = 1; i < n; ++i) {
            if (complexity[i] <= complexity[0]) {
                return 0;
            }
        }
        long long result = 1;
        for (int i = 2; i < n; ++i) {
            result = result * i % mod;
        }
        return static_cast<int>(result);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countPermutations(int[] complexity) {
        final long mod = 1000000007L;
        int n = complexity.length;
        for (int i = 1; i < n; i++) {
            if (complexity[i] <= complexity[0]) {
                return 0;
            }
        }
        long result = 1;
        for (int i = 2; i < n; i++) {
            result = result * i % mod;
        }
        return (int) result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
        result = 1
        for i in range(2, n):
            result = result * i % mod
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10**9 + 7
        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
        result = 1
        for i in range(2, n):
            result = result * i % mod
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countPermutations(int* complexity, int complexitySize) {
    const long long mod = 1000000007;
    for (int i = 1; i < complexitySize; ++i) {
        if (complexity[i] <= complexity[0]) {
            return 0;
        }
    }
    long long result = 1;
    for (int i = 2; i < complexitySize; ++i) {
        result = result * i % mod;
    }
    return (int) result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountPermutations(int[] complexity) {
        const long mod = 1000000007;
        int n = complexity.Length;
        for (int i = 1; i < n; i++) {
            if (complexity[i] <= complexity[0]) {
                return 0;
            }
        }
        long result = 1;
        for (int i = 2; i < n; i++) {
            result = result * i % mod;
        }
        return (int)result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} complexity
 * @return {number}
 */
var countPermutations = function(complexity) {
    const mod = 1000000007;
    const n = complexity.length;
    for (let i = 1; i < n; i++) {
        if (complexity[i] <= complexity[0]) {
            return 0;
        }
    }
    let result = 1;
    for (let i = 2; i < n; i++) {
        result = (result * i) % mod;
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countPermutations(complexity: number[]): number {
    const mod = 1000000007;
    const n = complexity.length;
    for (let i = 1; i < n; i++) {
        if (complexity[i] <= complexity[0]) {
            return 0;
        }
    }
    let result = 1;
    for (let i = 2; i < n; i++) {
        result = (result * i) % mod;
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
     * @param Integer[] $complexity
     * @return Integer
     */
    function countPermutations($complexity) {
        $mod = 1000000007;
        $n = count($complexity);
        for ($i = 1; $i < $n; $i++) {
            if ($complexity[$i] <= $complexity[0]) {
                return 0;
            }
        }
        $result = 1;
        for ($i = 2; $i < $n; $i++) {
            $result = ($result * $i) % $mod;
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
    func countPermutations(_ complexity: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = complexity.count
        for i in 1..<n {
            if complexity[i] <= complexity[0] {
                return 0
            }
        }
        var result = 1
        if n > 2 {
            for i in 2..<n {
                result = (result * i) % mod
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
    fun countPermutations(complexity: IntArray): Int {
        val n = complexity.size
        for (i in 1 until n) {
            if (complexity[i] <= complexity[0]) return 0
        }
        val mod = 1_000_000_007L
        var result = 1L
        for (i in 2 until n) {
            result = result * i % mod
        }
        return result.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countPermutations(List<int> complexity) {
    final n = complexity.length;
    for (var i = 1; i < n; i++) {
      if (complexity[i] <= complexity[0]) return 0;
    }
    const mod = 1000000007;
    var result = 1;
    for (var i = 2; i < n; i++) {
      result = result * i % mod;
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
func countPermutations(complexity []int) int {
	n := len(complexity)
	for i := 1; i < n; i++ {
		if complexity[i] <= complexity[0] {
			return 0
		}
	}
	const mod = 1000000007
	result := 1
	for i := 2; i < n; i++ {
		result = result * i % mod
	}
	return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} complexity
# @return {Integer}
def count_permutations(complexity)
  n = complexity.length
  (1...n).each do |i|
    return 0 if complexity[i] <= complexity[0]
  end
  mod = 1_000_000_007
  result = 1
  (2...n).each do |i|
    result = result * i % mod
  end
  result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countPermutations(complexity: Array[Int]): Int = {
        val n = complexity.length
        for (i <- 1 until n) {
            if (complexity(i) <= complexity(0)) return 0
        }
        val mod = 1000000007L
        var result = 1L
        for (i <- 2 until n) {
            result = result * i % mod
        }
        result.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_permutations(complexity: Vec<i32>) -> i32 {
        let n = complexity.len();
        for i in 1..n {
            if complexity[i] <= complexity[0] {
                return 0;
            }
        }
        let modulus = 1_000_000_007i64;
        let mut result = 1i64;
        for i in 2..n {
            result = result * i as i64 % modulus;
        }
        result as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-permutations complexity)
  (-> (listof exact-integer?) exact-integer?)
  (let ([first (car complexity)])
    (if (ormap (lambda (value) (<= value first)) (cdr complexity))
        0
        (let loop ([i 2] [result 1])
          (if (>= i (length complexity))
              result
              (loop (add1 i) (modulo (* result i) 1000000007)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_permutations(Complexity :: [integer()]) -> integer().
count_permutations(Complexity) ->
  [First | Rest] = Complexity,
  case lists:any(fun(Value) -> Value =< First end, Rest) of
    true -> 0;
    false -> factorial_mod(2, length(Complexity), 1)
  end.

factorial_mod(I, N, Result) when I >= N -> Result;
factorial_mod(I, N, Result) ->
  factorial_mod(I + 1, N, (Result * I) rem 1000000007).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_permutations(complexity :: [integer]) :: integer
  def count_permutations(complexity) do
    [first | rest] = complexity

    if Enum.any?(rest, &(&1 <= first)) do
      0
    else
      Enum.reduce(2..(length(complexity) - 1), 1, fn i, result ->
        rem(result * i, 1_000_000_007)
      end)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), to check all complexities and calculate the factorial.
- **Space Complexity:** O(1), using only a constant amount of extra space.
