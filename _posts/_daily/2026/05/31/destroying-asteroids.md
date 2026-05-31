---
layout: post
title: "Destroying Asteroids"
date: 2026-05-31 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/destroying-asteroids/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass\
        \ Solution {\npublic:\n    bool asteroidsDestroyed(int mass, vector<int>& asteroids)\
        \ {\n        sort(asteroids.begin(), asteroids.end());\n        long long currentMass\
        \ = mass;\n        for (int a : asteroids) {\n            if (currentMass >=\
        \ a) {\n                currentMass += a;\n            } else {\n          \
        \      return false;\n            }\n        }\n        return true;\n    }\n\
        };"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public boolean asteroidsDestroyed(int\
        \ mass, int[] asteroids) {\n        Arrays.sort(asteroids);\n        long currentMass\
        \ = mass;\n        for (int a : asteroids) {\n            if (currentMass >=\
        \ a) {\n                currentMass += a;\n            } else {\n          \
        \      return false;\n            }\n        }\n        return true;\n    }\n\
        }"
      python: "class Solution(object):\n    def asteroidsDestroyed(self, mass, asteroids):\n\
        \        \"\"\"\n        :type mass: int\n        :type asteroids: List[int]\n\
        \        :rtype: bool\n        \"\"\"\n        asteroids.sort()\n        curr_mass\
        \ = mass\n        for asteroid in asteroids:\n            if curr_mass >= asteroid:\n\
        \                curr_mass += asteroid\n            else:\n                return\
        \ False\n        return True"
      python3: "from typing import List\n\nclass Solution:\n    def asteroidsDestroyed(self,\
        \ mass: int, asteroids: List[int]) -> bool:\n        asteroids.sort()\n    \
        \    curr_mass = mass\n        for asteroid in asteroids:\n            if curr_mass\
        \ >= asteroid:\n                curr_mass += asteroid\n            else:\n \
        \               return False\n        return True"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n\nint compareAsteroids(const void*\
        \ a, const void* b) {\n    int val1 = *(const int*)a;\n    int val2 = *(const\
        \ int*)b;\n    if (val1 < val2) return -1;\n    if (val1 > val2) return 1;\n\
        \    return 0;\n}\n\nbool asteroidsDestroyed(int mass, int* asteroids, int asteroidsSize)\
        \ {\n    qsort(asteroids, asteroidsSize, sizeof(int), compareAsteroids);\n \
        \   long long currentMass = mass;\n    for (int i = 0; i < asteroidsSize; i++)\
        \ {\n        if (currentMass >= (long long)asteroids[i]) {\n            currentMass\
        \ += asteroids[i];\n        } else {\n            return false;\n        }\n\
        \    }\n    return true;\n}"
      csharp: "public class Solution {\n    public bool AsteroidsDestroyed(int mass,\
        \ int[] asteroids) {\n        System.Array.Sort(asteroids);\n        long currentMass\
        \ = mass;\n        foreach (int asteroid in asteroids) {\n            if (currentMass\
        \ >= asteroid) {\n                currentMass += asteroid;\n            } else\
        \ {\n                return false;\n            }\n        }\n        return\
        \ true;\n    }\n}"
      javascript: "/**\n * @param {number} mass\n * @param {number[]} asteroids\n *\
        \ @return {boolean}\n */\nvar asteroidsDestroyed = function(mass, asteroids)\
        \ {\n    asteroids.sort((a, b) => a - b);\n    let currentMass = mass;\n   \
        \ for (let i = 0; i < asteroids.length; i++) {\n        if (currentMass >= asteroids[i])\
        \ {\n            currentMass += asteroids[i];\n        } else {\n          \
        \  return false;\n        }\n    }\n    return true;\n};"
      typescript: "function asteroidsDestroyed(mass: number, asteroids: number[]): boolean\
        \ {\n    asteroids.sort((a, b) => a - b);\n    let currentMass: number = mass;\n\
        \    for (const asteroid of asteroids) {\n        if (currentMass >= asteroid)\
        \ {\n            currentMass += asteroid;\n        } else {\n            return\
        \ false;\n        }\n    }\n    return true;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $mass\n     * @param\
        \ Integer[] $asteroids\n     * @return Boolean\n     */\n    function asteroidsDestroyed($mass,\
        \ $asteroids) {\n        sort($asteroids);\n        $currentMass = (float)$mass;\n\
        \        foreach ($asteroids as $asteroid) {\n            if ($currentMass >=\
        \ $asteroid) {\n                $currentMass += (float)$asteroid;\n        \
        \    } else {\n                return false;\n            }\n        }\n   \
        \     return true;\n    }\n}"
      swift: "class Solution {\n    func asteroidsDestroyed(_ mass: Int, _ asteroids:\
        \ [Int]) -> Bool {\n        var sortedAsteroids = asteroids.sorted()\n     \
        \   var currentMass: Int64 = Int64(mass)\n        for asteroid in sortedAsteroids\
        \ {\n            if currentMass >= Int64(asteroid) {\n                currentMass\
        \ += Int64(asteroid)\n            } else {\n                return false\n \
        \           }\n        }\n        return true\n    }\n}"
      kotlin: "class Solution {\n    fun asteroidsDestroyed(mass: Int, asteroids: IntArray):\
        \ Boolean {\n        asteroids.sort()\n        var currentMass: Long = mass.toLong()\n\
        \        for (asteroid in asteroids) {\n            if (currentMass < asteroid)\
        \ {\n                return false\n            }\n            currentMass +=\
        \ asteroid\n        }\n        return true\n    }\n}"
      dart: "class Solution {\n  bool asteroidsDestroyed(int mass, List<int> asteroids)\
        \ {\n    asteroids.sort();\n    int currentMass = mass;\n    for (int asteroid\
        \ in asteroids) {\n      if (currentMass < asteroid) {\n        return false;\n\
        \      }\n      currentMass += asteroid;\n    }\n    return true;\n  }\n}"
      go: "import \"sort\"\n\nfunc asteroidsDestroyed(mass int, asteroids []int) bool\
        \ {\n    sort.Ints(asteroids)\n    currentMass := int64(mass)\n    for _, a\
        \ := range asteroids {\n        if currentMass < int64(a) {\n            return\
        \ false\n        }\n        currentMass += int64(a)\n    }\n    return true\n\
        }"
      ruby: "# @param {Integer} mass\n# @param {Integer[]} asteroids\n# @return {Boolean}\n\
        def asteroids_destroyed(mass, asteroids)\n    asteroids.sort!\n    current_mass\
        \ = mass\n    asteroids.each do |a|\n        if current_mass < a\n         \
        \   return false\n        end\n        current_mass += a\n    end\n    true\n\
        end"
      scala: "object Solution {\n    def asteroidsDestroyed(mass: Int, asteroids: Array[Int]):\
        \ Boolean = {\n        val sortedAsteroids = asteroids.sorted\n        var currentMass:\
        \ Long = mass.toLong\n        for (a <- sortedAsteroids) {\n            if (currentMass\
        \ < a) {\n                return false\n            }\n            currentMass\
        \ += a\n        }\n        true\n    }\n}"
      rust: "impl Solution {\n    pub fn asteroids_destroyed(mass: i32, asteroids: Vec<i32>)\
        \ -> bool {\n        let mut current_mass: i64 = mass as i64;\n        let mut\
        \ sorted_asteroids = asteroids;\n        sorted_asteroids.sort_unstable();\n\
        \n        for &asteroid in sorted_asteroids.iter() {\n            let asteroid_mass\
        \ = asteroid as i64;\n            if current_mass >= asteroid_mass {\n     \
        \           current_mass += asteroid_mass;\n            } else {\n         \
        \       return false;\n            }\n        }\n\n        true\n    }\n}"
      racket: "(define/contract (asteroids-destroyed mass asteroids)\n  (-> exact-integer?\
        \ (listof exact-integer?) boolean?)\n  (let ([sorted-asteroids (sort asteroids\
        \ <)])\n    (let loop ([current-mass mass]\n               [remaining sorted-asteroids])\n\
        \      (cond\n        [(empty? remaining) #t]\n        [(>= current-mass (first\
        \ remaining))\n         (loop (+ current-mass (first remaining)) (rest remaining))]\n\
        \        [else #f]))))"
      erlang: "-spec asteroids_destroyed(Mass :: integer(), Asteroids :: [integer()])\
        \ -> boolean().\nasteroids_destroyed(Mass, Asteroids) ->\n  SortedAsteroids\
        \ = lists:sort(Asteroids),\n  check_asteroids(Mass, SortedAsteroids).\n\ncheck_asteroids(_Mass,\
        \ []) ->\n  true;\ncheck_asteroids(Mass, [H | T]) ->\n  if\n    Mass >= H ->\
        \ check_asteroids(Mass + H, T);\n    true -> false\n  end."
      elixir: "defmodule Solution do\n  @spec asteroids_destroyed(mass :: integer, asteroids\
        \ :: [integer]) :: boolean\n  def asteroids_destroyed(mass, asteroids) do\n\
        \    asteroids\n    |> Enum.sort()\n    |> Enum.reduce_while(mass, fn asteroid,\
        \ current_mass ->\n      if current_mass >= asteroid do\n        {:cont, current_mass\
        \ + asteroid}\n      else\n        {:halt, :destroyed}\n      end\n    end)\
        \ != :destroyed\n  end\nend"
    approach: 'To solve this problem, we use a greedy strategy by prioritizing the destruction
      of smaller asteroids first. Since the planet''s mass increases with each asteroid
      it consumes, destroying smaller ones first maximizes the chance of having enough
      mass to destroy larger ones later. If the planet ever encounters an asteroid that
      is more massive than itself, it will be destroyed immediately. Because the asteroids
      can be handled in any order, sorting them in non-decreasing order ensures we always
      face the smallest possible challenge at each step.


      The algorithm begins by sorting the asteroids array. We then maintain the planet''s
      mass as a 64-bit integer to prevent overflow, as the sum of masses can exceed
      the limits of a 32-bit integer. We iterate through the sorted asteroids, comparing
      the planet''s mass to each asteroid''s mass. If the planet is more massive or
      equal, we add the asteroid''s mass to the planet''s total; otherwise, we return
      false. If we successfully iterate through all asteroids, we return true.'
    time_complexity: O(N log N), where N is the number of asteroids. The most time-consuming
      step is sorting the asteroids array, which takes O(N log N) time. The subsequent
      iteration through the array takes linear O(N) time.
    space_complexity: O(log N) or O(1). This depends on the sorting algorithm's internal
      implementation. Most modern sorting algorithms, such as Timsort or Quicksort,
      use O(log N) auxiliary space for recursive calls during the sorting process.
    elapsed_time: 65.95173287391663
    model: gemini-3-flash-preview
    generated_at: '2026-05-31 02:45:58 '
---

## Problem #2126: Destroying Asteroids

**Difficulty:** Medium

**Topics:** Array, Greedy, Sorting

## Problem Description

<p>You are given an integer <code>mass</code>, which represents the original mass of a planet. You are further given an integer array <code>asteroids</code>, where <code>asteroids[i]</code> is the mass of the <code>i<sup>th</sup></code> asteroid.</p>

<p>You can arrange for the planet to collide with the asteroids in <strong>any arbitrary order</strong>. If the mass of the planet is <b>greater than or equal to</b> the mass of the asteroid, the asteroid is <strong>destroyed</strong> and the planet <strong>gains</strong> the mass of the asteroid. Otherwise, the planet is destroyed.</p>

<p>Return <code>true</code><em> if <strong>all</strong> asteroids can be destroyed. Otherwise, return </em><code>false</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> mass = 10, asteroids = [3,9,19,5,21]
<strong>Output:</strong> true
<strong>Explanation:</strong> One way to order the asteroids is [9,19,5,3,21]:
- The planet collides with the asteroid with a mass of 9. New planet mass: 10 + 9 = 19
- The planet collides with the asteroid with a mass of 19. New planet mass: 19 + 19 = 38
- The planet collides with the asteroid with a mass of 5. New planet mass: 38 + 5 = 43
- The planet collides with the asteroid with a mass of 3. New planet mass: 43 + 3 = 46
- The planet collides with the asteroid with a mass of 21. New planet mass: 46 + 21 = 67
All asteroids are destroyed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mass = 5, asteroids = [4,9,23,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
The planet cannot ever gain enough mass to destroy the asteroid with a mass of 23.
After the planet destroys the other asteroids, it will have a mass of 5 + 4 + 9 + 4 = 22.
This is less than 23, so a collision would not destroy the last asteroid.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= mass &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= asteroids.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= asteroids[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Choosing the asteroid to collide with can be done greedily.

2. If an asteroid will destroy the planet, then every bigger asteroid will also destroy the planet.

3. You only need to check the smallest asteroid at each collision. If it will destroy the planet, then every other asteroid will also destroy the planet.

4. Sort the asteroids in non-decreasing order by mass, then greedily try to collide with the asteroids in that order.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we use a greedy strategy by prioritizing the destruction of smaller asteroids first. Since the planet's mass increases with each asteroid it consumes, destroying smaller ones first maximizes the chance of having enough mass to destroy larger ones later. If the planet ever encounters an asteroid that is more massive than itself, it will be destroyed immediately. Because the asteroids can be handled in any order, sorting them in non-decreasing order ensures we always face the smallest possible challenge at each step.

The algorithm begins by sorting the asteroids array. We then maintain the planet's mass as a 64-bit integer to prevent overflow, as the sum of masses can exceed the limits of a 32-bit integer. We iterate through the sorted asteroids, comparing the planet's mass to each asteroid's mass. If the planet is more massive or equal, we add the asteroid's mass to the planet's total; otherwise, we return false. If we successfully iterate through all asteroids, we return true.

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
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        sort(asteroids.begin(), asteroids.end());
        long long currentMass = mass;
        for (int a : asteroids) {
            if (currentMass >= a) {
                currentMass += a;
            } else {
                return false;
            }
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        Arrays.sort(asteroids);
        long currentMass = mass;
        for (int a : asteroids) {
            if (currentMass >= a) {
                currentMass += a;
            } else {
                return false;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        curr_mass = mass
        for asteroid in asteroids:
            if curr_mass >= asteroid:
                curr_mass += asteroid
            else:
                return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        curr_mass = mass
        for asteroid in asteroids:
            if curr_mass >= asteroid:
                curr_mass += asteroid
            else:
                return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>

int compareAsteroids(const void* a, const void* b) {
    int val1 = *(const int*)a;
    int val2 = *(const int*)b;
    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}

bool asteroidsDestroyed(int mass, int* asteroids, int asteroidsSize) {
    qsort(asteroids, asteroidsSize, sizeof(int), compareAsteroids);
    long long currentMass = mass;
    for (int i = 0; i < asteroidsSize; i++) {
        if (currentMass >= (long long)asteroids[i]) {
            currentMass += asteroids[i];
        } else {
            return false;
        }
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool AsteroidsDestroyed(int mass, int[] asteroids) {
        System.Array.Sort(asteroids);
        long currentMass = mass;
        foreach (int asteroid in asteroids) {
            if (currentMass >= asteroid) {
                currentMass += asteroid;
            } else {
                return false;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} mass
 * @param {number[]} asteroids
 * @return {boolean}
 */
var asteroidsDestroyed = function(mass, asteroids) {
    asteroids.sort((a, b) => a - b);
    let currentMass = mass;
    for (let i = 0; i < asteroids.length; i++) {
        if (currentMass >= asteroids[i]) {
            currentMass += asteroids[i];
        } else {
            return false;
        }
    }
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
    asteroids.sort((a, b) => a - b);
    let currentMass: number = mass;
    for (const asteroid of asteroids) {
        if (currentMass >= asteroid) {
            currentMass += asteroid;
        } else {
            return false;
        }
    }
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $mass
     * @param Integer[] $asteroids
     * @return Boolean
     */
    function asteroidsDestroyed($mass, $asteroids) {
        sort($asteroids);
        $currentMass = (float)$mass;
        foreach ($asteroids as $asteroid) {
            if ($currentMass >= $asteroid) {
                $currentMass += (float)$asteroid;
            } else {
                return false;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func asteroidsDestroyed(_ mass: Int, _ asteroids: [Int]) -> Bool {
        var sortedAsteroids = asteroids.sorted()
        var currentMass: Int64 = Int64(mass)
        for asteroid in sortedAsteroids {
            if currentMass >= Int64(asteroid) {
                currentMass += Int64(asteroid)
            } else {
                return false
            }
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun asteroidsDestroyed(mass: Int, asteroids: IntArray): Boolean {
        asteroids.sort()
        var currentMass: Long = mass.toLong()
        for (asteroid in asteroids) {
            if (currentMass < asteroid) {
                return false
            }
            currentMass += asteroid
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool asteroidsDestroyed(int mass, List<int> asteroids) {
    asteroids.sort();
    int currentMass = mass;
    for (int asteroid in asteroids) {
      if (currentMass < asteroid) {
        return false;
      }
      currentMass += asteroid;
    }
    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func asteroidsDestroyed(mass int, asteroids []int) bool {
    sort.Ints(asteroids)
    currentMass := int64(mass)
    for _, a := range asteroids {
        if currentMass < int64(a) {
            return false
        }
        currentMass += int64(a)
    }
    return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} mass
# @param {Integer[]} asteroids
# @return {Boolean}
def asteroids_destroyed(mass, asteroids)
    asteroids.sort!
    current_mass = mass
    asteroids.each do |a|
        if current_mass < a
            return false
        end
        current_mass += a
    end
    true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def asteroidsDestroyed(mass: Int, asteroids: Array[Int]): Boolean = {
        val sortedAsteroids = asteroids.sorted
        var currentMass: Long = mass.toLong
        for (a <- sortedAsteroids) {
            if (currentMass < a) {
                return false
            }
            currentMass += a
        }
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn asteroids_destroyed(mass: i32, asteroids: Vec<i32>) -> bool {
        let mut current_mass: i64 = mass as i64;
        let mut sorted_asteroids = asteroids;
        sorted_asteroids.sort_unstable();

        for &asteroid in sorted_asteroids.iter() {
            let asteroid_mass = asteroid as i64;
            if current_mass >= asteroid_mass {
                current_mass += asteroid_mass;
            } else {
                return false;
            }
        }

        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (asteroids-destroyed mass asteroids)
  (-> exact-integer? (listof exact-integer?) boolean?)
  (let ([sorted-asteroids (sort asteroids <)])
    (let loop ([current-mass mass]
               [remaining sorted-asteroids])
      (cond
        [(empty? remaining) #t]
        [(>= current-mass (first remaining))
         (loop (+ current-mass (first remaining)) (rest remaining))]
        [else #f]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec asteroids_destroyed(Mass :: integer(), Asteroids :: [integer()]) -> boolean().
asteroids_destroyed(Mass, Asteroids) ->
  SortedAsteroids = lists:sort(Asteroids),
  check_asteroids(Mass, SortedAsteroids).

check_asteroids(_Mass, []) ->
  true;
check_asteroids(Mass, [H | T]) ->
  if
    Mass >= H -> check_asteroids(Mass + H, T);
    true -> false
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec asteroids_destroyed(mass :: integer, asteroids :: [integer]) :: boolean
  def asteroids_destroyed(mass, asteroids) do
    asteroids
    |> Enum.sort()
    |> Enum.reduce_while(mass, fn asteroid, current_mass ->
      if current_mass >= asteroid do
        {:cont, current_mass + asteroid}
      else
        {:halt, :destroyed}
      end
    end) != :destroyed
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N), where N is the number of asteroids. The most time-consuming step is sorting the asteroids array, which takes O(N log N) time. The subsequent iteration through the array takes linear O(N) time.
- **Space Complexity:** O(log N) or O(1). This depends on the sorting algorithm's internal implementation. Most modern sorting algorithms, such as Timsort or Quicksort, use O(log N) auxiliary space for recursive calls during the sorting process.
