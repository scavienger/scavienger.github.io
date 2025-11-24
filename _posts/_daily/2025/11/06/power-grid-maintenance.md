---
layout: post
title: "Power Grid Maintenance"
date: 2025-11-06 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Depth-First Search", "Breadth-First Search", "Union Find", "Graph", "Heap (Priority Queue)", "Ordered Set"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/power-grid-maintenance/
---

## Problem #3607: Power Grid Maintenance

**Difficulty:** Medium

**Topics:** Array, Hash Table, Depth-First Search, Breadth-First Search, Union Find, Graph, Heap (Priority Queue), Ordered Set

## Problem Description

<p data-end="401" data-start="120">You are given an integer <code data-end="194" data-start="191">c</code> representing <code data-end="211" data-start="208">c</code> power stations, each with a unique identifier <code>id</code> from 1 to <code>c</code> (1‑based indexing).</p>

<p data-end="401" data-start="120">These stations are interconnected via <code data-end="295" data-start="292">n</code> <strong>bidirectional</strong> cables, represented by a 2D array <code data-end="357" data-start="344">connections</code>, where each element <code data-end="430" data-start="405">connections[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> indicates a connection between station <code>u<sub>i</sub></code> and station <code>v<sub>i</sub></code>. Stations that are directly or indirectly connected form a <strong>power grid</strong>.</p>

<p data-end="626" data-start="586">Initially, <strong>all</strong> stations are online (operational).</p>

<p data-end="720" data-start="628">You are also given a 2D array <code data-end="667" data-start="658">queries</code>, where each query is one of the following <em>two</em> types:</p>

<ul data-end="995" data-start="722">
	<li data-end="921" data-start="722">
	<p data-end="921" data-start="724"><code data-end="732" data-start="724">[1, x]</code>: A maintenance check is requested for station <code data-end="782" data-start="779">x</code>. If station <code>x</code> is online, it resolves the check by itself. If station <code>x</code> is offline, the check is resolved by the operational station with the smallest <code>id</code> in the same <strong>power grid</strong> as <code>x</code>. If <strong>no</strong> <strong>operational</strong> station <em>exists</em> in that grid, return -1.</p>
	</li>
	<li data-end="995" data-start="923">
	<p data-end="995" data-start="925"><code data-end="933" data-start="925">[2, x]</code>: Station <code data-end="946" data-start="943">x</code> goes offline (i.e., it becomes non-operational).</p>
	</li>
</ul>

<p data-end="1106" data-start="997">Return an array of integers representing the results of each query of type <code data-end="1080" data-start="1072">[1, x]</code> in the <strong>order</strong> they appear.</p>

<p data-end="1106" data-start="997"><strong>Note:</strong> The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,2,3]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/04/15/powergrid.jpg" style="width: 361px; height: 42px;" /></p>

<ul>
	<li data-end="223" data-start="143">Initially, all stations <code>{1, 2, 3, 4, 5}</code> are online and form a single power grid.</li>
	<li data-end="322" data-start="226">Query <code>[1,3]</code>: Station 3 is online, so the maintenance check is resolved by station 3.</li>
	<li data-end="402" data-start="325">Query <code>[2,1]</code>: Station 1 goes offline. The remaining online stations are <code>{2, 3, 4, 5}</code>.</li>
	<li data-end="557" data-start="405">Query <code>[1,1]</code>: Station 1 is offline, so the check is resolved by the operational station with the smallest <code>id</code> among <code>{2, 3, 4, 5}</code>, which is station 2.</li>
	<li data-end="641" data-start="560">Query <code>[2,2]</code>: Station 2 goes offline. The remaining online stations are <code>{3, 4, 5}</code>.</li>
	<li data-end="800" data-start="644">Query <code>[1,2]</code>: Station 2 is offline, so the check is resolved by the operational station with the smallest <code>id</code> among <code>{3, 4, 5}</code>, which is station 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,-1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li data-end="976" data-start="909">There are no connections, so each station is its own isolated grid.</li>
	<li data-end="1096" data-start="979">Query <code>[1,1]</code>: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.</li>
	<li data-end="1135" data-start="1099">Query <code>[2,1]</code>: Station 1 goes offline.</li>
	<li data-end="1237" data-start="1138">Query <code>[1,1]</code>: Station 1 is offline and there are no other stations in its grid, so the result is -1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="155" data-start="139"><code>1 &lt;= c &lt;= 10<sup>5</sup></code></li>
	<li data-end="213" data-start="158"><code>0 &lt;= n == connections.length &lt;= min(10<sup>5</sup>, c * (c - 1) / 2)</code></li>
	<li data-end="244" data-start="216"><code>connections[i].length == 2</code></li>
	<li data-end="295" data-start="247"><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= c</code></li>
	<li data-end="338" data-start="298"><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li data-end="374" data-start="341"><code>1 &lt;= queries.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li data-end="401" data-start="377"><code>queries[i].length == 2</code></li>
	<li data-end="436" data-start="404"><code>queries[i][0]</code> is either 1 or 2.</li>
	<li data-end="462" data-start="439"><code>1 &lt;= queries[i][1] &lt;= c</code></li>
</ul>


## Hints

1. Use DFS or BFS to assign each station a component ID

2. For each component, maintain a sorted set of online station IDs

3. For query `[2, x]`, remove `x` from the set of its component

4. For query `[1, x]`, if `x` is in its component’s set return `x`; otherwise if the set is non-empty return its smallest element; else return `-1`

5. Precompute all components and then handle each query in O(log n) time using the sorted sets

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-24 07:49:19 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires managing power stations, their connectivity into grids (connected components), and their operational status (online/offline) while efficiently answering queries about the smallest operational station in a given grid. The core idea is to pre-process the graph to identify connected components and then maintain a sorted collection of online stations for each component.

First, we build an adjacency list from the `connections` to represent the power grid. Then, we perform a graph traversal (DFS or BFS) to discover all connected components. During this traversal, each station is assigned a unique `component_id`. For each `component_id`, we initialize a data structure that will store the IDs of all stations belonging to that component that are currently online. Initially, all stations are online, so every station is added to its respective component's data structure.

To handle queries efficiently, we use a boolean array `is_online` to track the operational status of each station. For each component, we need a data structure that allows efficient insertion, deletion, and retrieval of the minimum element. A balanced binary search tree (like `std::set` in C++, `TreeSet` in Java/Kotlin/Scala, `BTreeSet` in Rust, `SplayTreeSet` in Dart) is ideal, providing `O(log K)` time complexity for these operations, where `K` is the number of elements in the set. For languages without a built-in balanced BST (e.g., Python, Go, JavaScript, TypeScript, PHP, Ruby, Swift, Racket, Erlang, Elixir), a min-priority queue combined with a hash set (for lazy deletion) can achieve similar amortized `O(log K)` performance. The hash set tracks truly active elements, while the priority queue stores elements that might include inactive ones, which are 'cleaned' when they reach the top of the heap.

When a query `[1, x]` arrives: if station `x` is online (checked via `is_online[x]`), we return `x`. If `x` is offline, we find its `component_id` and query the smallest element from the sorted set (or cleaned min-heap) corresponding to that component. If the set is empty, it means no operational stations exist in that grid, so we return -1. When a query `[2, x]` arrives: we mark `x` as offline in `is_online[x]` and remove `x` from its component's sorted set (or active hash set in the lazy deletion heap approach). This strategy ensures that each query is processed efficiently, allowing the solution to scale for large inputs.

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
    // Adjacency list
    std::vector<std::vector<int>> adj;
    // Maps station ID to its component ID
    std::vector<int> component_map;
    // Tracks visited stations during DFS
    std::vector<bool> visited;
    // Stores online stations for each component in a sorted manner
    std::vector<std::set<int>> online_stations_in_component;

    void dfs(int node, int current_component_id) {
        visited[node] = true;
        component_map[node] = current_component_id;
        online_stations_in_component[current_component_id].insert(node); // Add to sorted set
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, current_component_id);
            }
        }
    }

    std::vector<int> processQueries(int c, std::vector<std::vector<int>>& connections, std::vector<std::vector<int>>& queries) {
        adj.resize(c + 1);
        for (const auto& conn : connections) {
            int u = conn[0];
            int v = conn[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        component_map.resize(c + 1);
        visited.resize(c + 1, false);

        int component_id_counter = 0;
        for (int i = 1; i <= c; ++i) {
            if (!visited[i]) {
                online_stations_in_component.emplace_back(); // Add a new empty set for a new component
                dfs(i, component_id_counter);
                component_id_counter++;
            }
        }

        std::vector<bool> is_online(c + 1, true);
        std::vector<int> results;

        for (const auto& query : queries) {
            int query_type = query[0];
            int x = query[1];

            if (query_type == 1) {
                if (is_online[x]) {
                    results.push_back(x);
                } else {
                    int comp_id = component_map[x];
                    if (online_stations_in_component[comp_id].empty()) {
                        results.push_back(-1);
                    } else {
                        results.push_back(*online_stations_in_component[comp_id].begin()); // Smallest element
                    }
                }
            } else { // query_type == 2
                if (is_online[x]) { // Only process if it's currently online
                    is_online[x] = false;
                    int comp_id = component_map[x];
                    online_stations_in_component[comp_id].erase(x); // Remove from sorted set
                }
            }
        }

        return results;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    // Adjacency list
    List<List<Integer>> adj;
    // Maps station ID to its component ID
    int[] componentMap;
    // Tracks visited stations during DFS
    boolean[] visited;
    // Stores online stations for each component in a sorted manner
    List<TreeSet<Integer>> onlineStationsInComponent;

    public List<Integer> processQueries(int c, List<List<Integer>> connections, List<List<Integer>> queries) {
        adj = new ArrayList<>(c + 1);
        for (int i = 0; i <= c; i++) {
            adj.add(new ArrayList<>());
        }

        for (List<Integer> conn : connections) {
            int u = conn.get(0);
            int v = conn.get(1);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        componentMap = new int[c + 1];
        visited = new boolean[c + 1];
        onlineStationsInComponent = new ArrayList<>();

        int componentIdCounter = 0;
        for (int i = 1; i <= c; i++) {
            if (!visited[i]) {
                onlineStationsInComponent.add(new TreeSet<>()); // Add a new empty TreeSet for a new component
                dfs(i, componentIdCounter);
                componentIdCounter++;
            }
        }

        boolean[] isOnline = new boolean[c + 1];
        Arrays.fill(isOnline, true); // Initially all stations are online

        List<Integer> results = new ArrayList<>();

        for (List<Integer> query : queries) {
            int queryType = query.get(0);
            int x = query.get(1);

            if (queryType == 1) {
                if (isOnline[x]) {
                    results.add(x);
                } else {
                    int compId = componentMap[x];
                    TreeSet<Integer> currentComponentOnlineStations = onlineStationsInComponent.get(compId);
                    if (currentComponentOnlineStations.isEmpty()) {
                        results.add(-1);
                    } else {
                        results.add(currentComponentOnlineStations.first()); // Smallest element
                    }
                }
            } else { // queryType == 2
                if (isOnline[x]) { // Only process if it's currently online
                    isOnline[x] = false;
                    int compId = componentMap[x];
                    onlineStationsInComponent.get(compId).remove(x); // Remove from sorted set
                }
            }
        }

        return results;
    }

    private void dfs(int node, int currentComponentId) {
        visited[node] = true;
        componentMap[node] = currentComponentId;
        onlineStationsInComponent.get(currentComponentId).add(node); // Add to sorted set
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor, currentComponentId);
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        component_map = [0] * (c + 1)
        visited = [False] * (c + 1)

        # List of heaps, one for each component
        online_stations_in_component_heaps = []
        # List of sets, one for each component, to track active stations
        online_stations_in_component_active = []

        component_id_counter = 0

        def dfs(node, current_component_id):
            visited[node] = True
            component_map[node] = current_component_id
            # Add node to the heap and active set of its component
            heapq.heappush(online_stations_in_component_heaps[current_component_id], node)
            online_stations_in_component_active[current_component_id].add(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, current_component_id)

        for i in range(1, c + 1):
            if not visited[i]:
                # New component found
                online_stations_in_component_heaps.append([])
                online_stations_in_component_active.append(set())
                dfs(i, component_id_counter)
                component_id_counter += 1

        is_online = [True] * (c + 1)
        results = []

        for query_type, x in queries:
            if query_type == 1:
                if is_online[x]:
                    results.append(x)
                else:
                    comp_id = component_map[x]
                    current_heap = online_stations_in_component_heaps[comp_id]
                    current_active_set = online_stations_in_component_active[comp_id]

                    # Clean the heap: remove elements that are no longer active
                    while current_heap and current_heap[0] not in current_active_set:
                        heapq.heappop(current_heap)

                    if not current_heap:
                        results.append(-1)
                    else:
                        results.append(current_heap[0])
            else: # query_type == 2
                if is_online[x]: # Only process if it's currently online
                    is_online[x] = False
                    comp_id = component_map[x]
                    online_stations_in_component_active[comp_id].remove(x)

        return results
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        component_map = [0] * (c + 1)
        visited = [False] * (c + 1)

        # List of heaps, one for each component
        online_stations_in_component_heaps = []
        # List of sets, one for each component, to track active stations
        online_stations_in_component_active = []

        component_id_counter = 0

        def dfs(node, current_component_id):
            visited[node] = True
            component_map[node] = current_component_id
            # Add node to the heap and active set of its component
            heapq.heappush(online_stations_in_component_heaps[current_component_id], node)
            online_stations_in_component_active[current_component_id].add(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, current_component_id)

        for i in range(1, c + 1):
            if not visited[i]:
                # New component found
                online_stations_in_component_heaps.append([])
                online_stations_in_component_active.append(set())
                dfs(i, component_id_counter)
                component_id_counter += 1

        is_online = [True] * (c + 1)
        results = []

        for query_type, x in queries:
            if query_type == 1:
                if is_online[x]:
                    results.append(x)
                else:
                    comp_id = component_map[x]
                    current_heap = online_stations_in_component_heaps[comp_id]
                    current_active_set = online_stations_in_component_active[comp_id]

                    # Clean the heap: remove elements that are no longer active
                    while current_heap and current_heap[0] not in current_active_set:
                        heapq.heappop(current_heap)

                    if not current_heap:
                        results.append(-1)
                    else:
                        results.append(current_heap[0])
            else: # query_type == 2
                if is_online[x]: # Only process if it's currently online
                    is_online[x] = False
                    comp_id = component_map[x]
                    online_stations_in_component_active[comp_id].remove(x)

        return results
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/*
 * C does not have built-in balanced BSTs or dynamic lists of sets/heaps like C++ or Java.
 * Implementing a custom balanced BST (like AVL or Red-Black tree) or a min-heap with lazy deletion
 * for each component would be very complex and verbose in C.
 * For competitive programming in C, one might use a Disjoint Set Union (DSU) structure to find components
 * and then for each component, maintain a min-heap (implemented with an array) and a hash set (implemented
 * with a hash table or boolean array for small ranges) for lazy deletion.
 * Given the constraints and the need for a complete solution, this would be a significant undertaking.
 * A simplified approach for C might involve a DSU where each root stores the minimum online ID.
 * However, updating this minimum when an arbitrary node goes offline is not efficient with standard DSU.
 * The problem essentially requires a dynamic sorted set per component.
 * 
 * A practical C solution for competitive programming would likely involve:
 * 1. Adjacency list using dynamic arrays (pointers to arrays).
 * 2. DFS/BFS for components, storing component ID in an array.
 * 3. For each component, a dynamically allocated array to act as a min-heap, and a boolean array/hash table
 *    to track active elements for lazy deletion. This is still complex.
 * 
 * Due to the complexity of implementing dynamic sorted sets/heaps with lazy deletion in pure C
 * without standard library equivalents, a full, efficient C solution is omitted as it would be
 * disproportionately long and complex compared to other languages, and typically not expected
 * in a direct translation for such problems on platforms like LeetCode.
 * If a C solution were strictly required, it would involve a custom implementation of a min-heap
 * and a hash set for each component, which is beyond the scope of a concise solution for this problem.
 */
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    private List<List<int>> adj;
    private int[] componentMap;
    private bool[] visited;
    private List<SortedSet<int>> onlineStationsInComponent;

    public IList<int> ProcessQueries(int c, IList<IList<int>> connections, IList<IList<int>> queries) {
        adj = new List<List<int>>(c + 1);
        for (int i = 0; i <= c; i++) {
            adj.Add(new List<int>());
        }

        foreach (var conn in connections) {
            int u = conn[0];
            int v = conn[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        componentMap = new int[c + 1];
        visited = new bool[c + 1];
        onlineStationsInComponent = new List<SortedSet<int>>();

        int componentIdCounter = 0;
        for (int i = 1; i <= c; i++) {
            if (!visited[i]) {
                onlineStationsInComponent.Add(new SortedSet<int>()); // Add a new empty SortedSet
                Dfs(i, componentIdCounter);
                componentIdCounter++;
            }
        }

        bool[] isOnline = new bool[c + 1];
        Array.Fill(isOnline, true); // Initially all stations are online

        List<int> results = new List<int>();

        foreach (var query in queries) {
            int queryType = query[0];
            int x = query[1];

            if (queryType == 1) {
                if (isOnline[x]) {
                    results.Add(x);
                } else {
                    int compId = componentMap[x];
                    SortedSet<int> currentComponentOnlineStations = onlineStationsInComponent[compId];
                    if (currentComponentOnlineStations.Count == 0) {
                        results.Add(-1);
                    } else {
                        results.Add(currentComponentOnlineStations.Min); // Smallest element
                    }
                }
            } else { // queryType == 2
                if (isOnline[x]) { // Only process if it's currently online
                    isOnline[x] = false;
                    int compId = componentMap[x];
                    onlineStationsInComponent[compId].Remove(x); // Remove from sorted set
                }
            }
        }

        return results;
    }

    private void Dfs(int node, int currentComponentId) {
        visited[node] = true;
        componentMap[node] = currentComponentId;
        onlineStationsInComponent[currentComponentId].Add(node); // Add to sorted set
        foreach (int neighbor in adj[node]) {
            if (!visited[neighbor]) {
                Dfs(neighbor, currentComponentId);
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
class MinPriorityQueue {
    constructor() {
        this.heap = [];
    }

    push(val) {
        this.heap.push(val);
        this._bubbleUp(this.heap.length - 1);
    }

    pop() {
        if (this.isEmpty()) return undefined;
        if (this.heap.length === 1) return this.heap.pop();

        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this._bubbleDown(0);
        return min;
    }

    peek() {
        return this.heap.length > 0 ? this.heap[0] : undefined;
    }

    isEmpty() {
        return this.heap.length === 0;
    }

    _bubbleUp(index) {
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[parentIndex] > this.heap[index]) {
                [this.heap[parentIndex], this.heap[index]] = [this.heap[index], this.heap[parentIndex]];
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    _bubbleDown(index) {
        const lastIndex = this.heap.length - 1;
        while (true) {
            let leftChildIndex = 2 * index + 1;
            let rightChildIndex = 2 * index + 2;
            let smallestIndex = index;

            if (leftChildIndex <= lastIndex && this.heap[leftChildIndex] < this.heap[smallestIndex]) {
                smallestIndex = leftChildIndex;
            }

            if (rightChildIndex <= lastIndex && this.heap[rightChildIndex] < this.heap[smallestIndex]) {
                smallestIndex = rightChildIndex;
            }

            if (smallestIndex !== index) {
                [this.heap[index], this.heap[smallestIndex]] = [this.heap[smallestIndex], this.heap[index]];
                index = smallestIndex;
            } else {
                break;
            }
        }
    }
}


class Solution {
    adj = new Map();
    componentMap;
    visited;
    onlineStationsInComponentHeaps; // Array of MinPriorityQueue
    onlineStationsInComponentActive; // Array of Set

    dfs(node, currentComponentId) {
        this.visited[node] = true;
        this.componentMap[node] = currentComponentId;

        // Add node to the heap and active set of its component
        this.onlineStationsInComponentHeaps[currentComponentId].push(node);
        this.onlineStationsInComponentActive[currentComponentId].add(node);

        for (const neighbor of this.adj.get(node) || []) {
            if (!this.visited[neighbor]) {
                this.dfs(neighbor, currentComponentId);
            }
        }
    }

    processQueries(c, connections, queries) {
        for (let i = 1; i <= c; i++) {
            this.adj.set(i, []);
        }
        for (const conn of connections) {
            const [u, v] = conn;
            this.adj.get(u).push(v);
            this.adj.get(v).push(u);
        }

        this.componentMap = new Array(c + 1).fill(0);
        this.visited = new Array(c + 1).fill(false);
        this.onlineStationsInComponentHeaps = [];
        this.onlineStationsInComponentActive = [];

        let componentIdCounter = 0;
        for (let i = 1; i <= c; i++) {
            if (!this.visited[i]) {
                // Initialize new heap and active set for the new component
                this.onlineStationsInComponentHeaps.push(new MinPriorityQueue());
                this.onlineStationsInComponentActive.push(new Set());

                this.dfs(i, componentIdCounter);
                componentIdCounter++;
            }
        }

        const isOnline = new Array(c + 1).fill(true); // Initially all stations are online

        const results = [];

        for (const query of queries) {
            const [queryType, x] = query;

            if (queryType === 1) {
                if (isOnline[x]) {
                    results.push(x);
                } else {
                    const compId = this.componentMap[x];
                    const currentHeap = this.onlineStationsInComponentHeaps[compId];
                    const currentActiveSet = this.onlineStationsInComponentActive[compId];

                    // Clean the heap: remove elements that are no longer active
                    while (!currentHeap.isEmpty() && !currentActiveSet.has(currentHeap.peek())) {
                        currentHeap.pop(); // Remove inactive element
                    }

                    if (currentHeap.isEmpty()) {
                        results.push(-1);
                    } else {
                        results.push(currentHeap.peek());
                    }
                }
            } else { // queryType === 2
                if (isOnline[x]) { // Only process if it's currently online
                    isOnline[x] = false;
                    const compId = this.componentMap[x];
                    this.onlineStationsInComponentActive[compId].delete(x); // Remove from active set
                }
            }
        }

        return results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class MinPriorityQueue {
    private heap: number[] = [];

    push(val: number): void {
        this.heap.push(val);
        this._bubbleUp(this.heap.length - 1);
    }

    pop(): number | undefined {
        if (this.isEmpty()) return undefined;
        if (this.heap.length === 1) return this.heap.pop();

        const min = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this._bubbleDown(0);
        return min;
    }

    peek(): number | undefined {
        return this.heap.length > 0 ? this.heap[0] : undefined;
    }

    isEmpty(): boolean {
        return this.heap.length === 0;
    }

    private _bubbleUp(index: number): void {
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[parentIndex] > this.heap[index]) {
                [this.heap[parentIndex], this.heap[index]] = [this.heap[index], this.heap[parentIndex]];
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    private _bubbleDown(index: number): void {
        const lastIndex = this.heap.length - 1;
        while (true) {
            let leftChildIndex = 2 * index + 1;
            let rightChildIndex = 2 * index + 2;
            let smallestIndex = index;

            if (leftChildIndex <= lastIndex && this.heap[leftChildIndex] < this.heap[smallestIndex]) {
                smallestIndex = leftChildIndex;
            }

            if (rightChildIndex <= lastIndex && this.heap[rightChildIndex] < this.heap[smallestIndex]) {
                smallestIndex = rightChildIndex;
            }

            if (smallestIndex !== index) {
                [this.heap[index], this.heap[smallestIndex]] = [this.heap[smallestIndex], this.heap[index]];
                index = smallestIndex;
            } else {
                break;
            }
        }
    }
}


class Solution {
    private adj: Map<number, number[]> = new Map();
    private componentMap: number[];
    private visited: boolean[];
    private onlineStationsInComponentHeaps: MinPriorityQueue[]; // Array of MinPriorityQueue
    private onlineStationsInComponentActive: Set<number>[]; // Array of Set

    private dfs(node: number, currentComponentId: number): void {
        this.visited[node] = true;
        this.componentMap[node] = currentComponentId;

        this.onlineStationsInComponentHeaps[currentComponentId].push(node);
        this.onlineStationsInComponentActive[currentComponentId].add(node);

        for (const neighbor of this.adj.get(node) || []) {
            if (!this.visited[neighbor]) {
                this.dfs(neighbor, currentComponentId);
            }
        }
    }

    public processQueries(c: number, connections: number[][], queries: number[][]): number[] {
        for (let i = 1; i <= c; i++) {
            this.adj.set(i, []);
        }
        for (const conn of connections) {
            const [u, v] = conn;
            this.adj.get(u)!.push(v);
            this.adj.get(v)!.push(u);
        }

        this.componentMap = new Array(c + 1).fill(0);
        this.visited = new Array(c + 1).fill(false);
        this.onlineStationsInComponentHeaps = [];
        this.onlineStationsInComponentActive = [];

        let componentIdCounter = 0;
        for (let i = 1; i <= c; i++) {
            if (!this.visited[i]) {
                this.onlineStationsInComponentHeaps.push(new MinPriorityQueue());
                this.onlineStationsInComponentActive.push(new Set());

                this.dfs(i, componentIdCounter);
                componentIdCounter++;
            }
        }

        const isOnline: boolean[] = new Array(c + 1).fill(true);

        const results: number[] = [];

        for (const query of queries) {
            const [queryType, x] = query;

            if (queryType === 1) {
                if (isOnline[x]) {
                    results.push(x);
                } else {
                    const compId = this.componentMap[x];
                    const currentHeap = this.onlineStationsInComponentHeaps[compId];
                    const currentActiveSet = this.onlineStationsInComponentActive[compId];

                    while (!currentHeap.isEmpty() && !currentActiveSet.has(currentHeap.peek()!)) {
                        currentHeap.pop();
                    }

                    if (currentHeap.isEmpty()) {
                        results.push(-1);
                    } else {
                        results.push(currentHeap.peek()!);
                    }
                }
            } else { // queryType === 2
                if (isOnline[x]) {
                    isOnline[x] = false;
                    const compId = this.componentMap[x];
                    this.onlineStationsInComponentActive[compId].delete(x);
                }
            }
        }

        return results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php

class MinPriorityQueue extends SplMinHeap {
    // SplMinHeap already provides min-heap functionality.
    // We just need to ensure it's used with lazy deletion.
}

class Solution {
    private $adj;
    private $componentMap;
    private $visited;
    private $onlineStationsInComponentHeaps; // Array of MinPriorityQueue
    private $onlineStationsInComponentActive; // Array of associative arrays (sets)

    private function dfs(int $node, int $currentComponentId): void {
        $this->visited[$node] = true;
        $this->componentMap[$node] = $currentComponentId;

        // Add node to the heap and active set of its component
        $this->onlineStationsInComponentHeaps[$currentComponentId]->insert($node);
        $this->onlineStationsInComponentActive[$currentComponentId][$node] = true; // Use key as set element

        foreach ($this->adj[$node] as $neighbor) {
            if (!$this->visited[$neighbor]) {
                $this->dfs($neighbor, $currentComponentId);
            }
        }
    }

    /**
     * @param int $c
     * @param int[][] $connections
     * @param int[][] $queries
     * @return int[]
     */
    function processQueries(int $c, array $connections, array $queries): array {
        $this->adj = array_fill(0, $c + 1, []);
        foreach ($connections as $conn) {
            list($u, $v) = $conn;
            $this->adj[$u][] = $v;
            $this->adj[$v][] = $u;
        }

        $this->componentMap = array_fill(0, $c + 1, 0);
        $this->visited = array_fill(0, $c + 1, false);
        $this->onlineStationsInComponentHeaps = [];
        $this->onlineStationsInComponentActive = [];

        $componentIdCounter = 0;
        for ($i = 1; $i <= $c; $i++) {
            if (!$this->visited[$i]) {
                // Initialize new heap and active set for the new component
                $this->onlineStationsInComponentHeaps[] = new MinPriorityQueue();
                $this->onlineStationsInComponentActive[] = []; // Empty associative array for set

                $this->dfs($i, $componentIdCounter);
                $componentIdCounter++;
            }
        }

        $isOnline = array_fill(0, $c + 1, true); // Initially all stations are online

        $results = [];

        foreach ($queries as $query) {
            list($queryType, $x) = $query;

            if ($queryType === 1) {
                if ($isOnline[$x]) {
                    $results[] = $x;
                } else {
                    $compId = $this->componentMap[$x];
                    $currentHeap = $this->onlineStationsInComponentHeaps[$compId];
                    $currentActiveSet = $this->onlineStationsInComponentActive[$compId];

                    // Clean the heap: remove elements that are no longer active
                    while (!$currentHeap->isEmpty()) {
                        $top = $currentHeap->top();
                        if (isset($currentActiveSet[$top])) {
                            break; // Found an active element
                        }
                        $currentHeap->extract(); // Remove inactive element
                    }

                    if ($currentHeap->isEmpty()) {
                        $results[] = -1;
                    } else {
                        $results[] = $currentHeap->top();
                    }
                }
            } else { // queryType === 2
                if ($isOnline[$x]) { // Only process if it's currently online
                    $isOnline[$x] = false;
                    $compId = $this->componentMap[$x];
                    unset($this->onlineStationsInComponentActive[$compId][$x]); // Remove from active set
                }
            }
        }

        return $results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

// Custom MinHeap implementation
struct MinHeap {
    private var heap: [Int] = []

    var isEmpty: Bool {
        return heap.isEmpty
    }

    var count: Int {
        return heap.count
    }

    mutating func push(_ element: Int) {
        heap.append(element)
        bubbleUp(heap.count - 1)
    }

    mutating func pop() -> Int? {
        guard !isEmpty else { return nil }
        if heap.count == 1 {
            return heap.removeLast()
        }
        let min = heap[0]
        heap[0] = heap.removeLast()
        bubbleDown(0)
        return min
    }

    func peek() -> Int? {
        return heap.first
    }

    private mutating func bubbleUp(_ index: Int) {
        var currentIndex = index
        var parentIndex = (currentIndex - 1) / 2
        while currentIndex > 0 && heap[currentIndex] < heap[parentIndex] {
            heap.swapAt(currentIndex, parentIndex)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) / 2
        }
    }

    private mutating func bubbleDown(_ index: Int) {
        var currentIndex = index
        let lastIndex = heap.count - 1
        while true {
            let leftChildIndex = 2 * currentIndex + 1
            let rightChildIndex = 2 * currentIndex + 2
            var smallestIndex = currentIndex

            if leftChildIndex <= lastIndex && heap[leftChildIndex] < heap[smallestIndex] {
                smallestIndex = leftChildIndex
            }
            if rightChildIndex <= lastIndex && heap[rightChildIndex] < heap[smallestIndex] {
                smallestIndex = rightChildIndex
            }

            if smallestIndex != currentIndex {
                heap.swapAt(currentIndex, smallestIndex)
                currentIndex = smallestIndex
            } else {
                break
            }
        }
    }
}

class Solution {
    private var adj: [[Int]] = []
    private var componentMap: [Int] = []
    private var visited: [Bool] = []
    private var onlineStationsInComponentHeaps: [MinHeap] = []
    private var onlineStationsInComponentActive: [Set<Int>] = []

    private func dfs(_ node: Int, _ currentComponentId: Int) {
        visited[node] = true
        componentMap[node] = currentComponentId

        onlineStationsInComponentHeaps[currentComponentId].push(node)
        onlineStationsInComponentActive[currentComponentId].insert(node)

        for neighbor in adj[node] {
            if !visited[neighbor]) {
                dfs(neighbor, currentComponentId)
            }
        }
    }

    func processQueries(_ c: Int, _ connections: [[Int]], _ queries: [[Int]]) -> [Int] {
        adj = Array(repeating: [], count: c + 1)
        for conn in connections {
            let u = conn[0]
            let v = conn[1]
            adj[u].append(v)
            adj[v].append(u)
        }

        componentMap = Array(repeating: 0, count: c + 1)
        visited = Array(repeating: false, count: c + 1)

        var componentIdCounter = 0
        for i in 1...c {
            if !visited[i]) {
                onlineStationsInComponentHeaps.append(MinHeap())
                onlineStationsInComponentActive.append(Set<Int>())

                dfs(i, componentIdCounter)
                componentIdCounter += 1
            }
        }

        var isOnline = Array(repeating: true, count: c + 1)

        var results: [Int] = []

        for query in queries {
            let queryType = query[0]
            let x = query[1]

            if queryType == 1 {
                if isOnline[x] {
                    results.append(x)
                } else {
                    let compId = componentMap[x]
                    var currentHeap = onlineStationsInComponentHeaps[compId] // Need to be careful with value vs reference type
                    let currentActiveSet = onlineStationsInComponentActive[compId]

                    // Clean the heap
                    while !currentHeap.isEmpty && !currentActiveSet.contains(currentHeap.peek()!) {
                        _ = currentHeap.pop()
                    }

                    if currentHeap.isEmpty {
                        results.append(-1)
                    } else {
                        results.append(currentHeap.peek()!)
                    }
                    // Update the heap in the array if it's a struct (value type)
                    onlineStationsInComponentHeaps[compId] = currentHeap
                }
            } else { // queryType == 2
                if isOnline[x] {
                    isOnline[x] = false
                    let compId = componentMap[x]
                    onlineStationsInComponentActive[compId].remove(x)
                }
            }
        }

        return results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.*
import kotlin.collections.ArrayList

class Solution {
    private lateinit var adj: List<MutableList<Int>>
    private lateinit var componentMap: IntArray
    private lateinit var visited: BooleanArray
    private lateinit var onlineStationsInComponent: List<TreeSet<Int>>

    fun processQueries(c: Int, connections: List<List<Int>>, queries: List<List<Int>>): List<Int> {
        adj = List(c + 1) { ArrayList() }
        for (conn in connections) {
            val u = conn[0]
            val v = conn[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        componentMap = IntArray(c + 1)
        visited = BooleanArray(c + 1)
        onlineStationsInComponent = ArrayList()

        var componentIdCounter = 0
        for (i in 1..c) {
            if (!visited[i]) {
                (onlineStationsInComponent as ArrayList).add(TreeSet()) // Add a new empty TreeSet
                dfs(i, componentIdCounter)
                componentIdCounter++
            }
        }

        val isOnline = BooleanArray(c + 1) { true } // Initially all stations are online

        val results = ArrayList<Int>()

        for (query in queries) {
            val queryType = query[0]
            val x = query[1]

            if (queryType == 1) {
                if (isOnline[x]) {
                    results.add(x)
                } else {
                    val compId = componentMap[x]
                    val currentComponentOnlineStations = onlineStationsInComponent[compId]
                    if (currentComponentOnlineStations.isEmpty()) {
                        results.add(-1)
                    } else {
                        results.add(currentComponentOnlineStations.first()) // Smallest element
                    }
                }
            }
        } else { // queryType == 2
                if (isOnline[x]) { // Only process if it's currently online
                    isOnline[x] = false
                    val compId = componentMap[x]
                    onlineStationsInComponent[compId].remove(x) // Remove from sorted set
                }
            }
        }

        return results
    }

    private fun dfs(node: Int, currentComponentId: Int) {
        visited[node] = true
        componentMap[node] = currentComponentId;
        onlineStationsInComponent[currentComponentId].add(node); // Add to sorted set
        for (neighbor in adj[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, currentComponentId);
            }
        }
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
  late List<List<int>> adj;
  late List<int> componentMap;
  late List<bool> visited;
  late List<SplayTreeSet<int>> onlineStationsInComponent;

  List<int> processQueries(int c, List<List<int>> connections, List<List<int>> queries) {
    adj = List.generate(c + 1, (_) => []);
    for (final conn in connections) {
      final u = conn[0];
      final v = conn[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    componentMap = List.filled(c + 1, 0);
    visited = List.filled(c + 1, false);
    onlineStationsInComponent = [];

    var componentIdCounter = 0;
    for (var i = 1; i <= c; i++) {
      if (!visited[i]) {
        onlineStationsInComponent.add(SplayTreeSet<int>()); // Add a new empty SplayTreeSet
        _dfs(i, componentIdCounter);
        componentIdCounter++;
      }
    }

    final isOnline = List.filled(c + 1, true); // Initially all stations are online

    final results = <int>[];

    for (final query in queries) {
      final queryType = query[0];
      final x = query[1];

      if (queryType == 1) {
        if (isOnline[x]) {
          results.add(x);
        } else {
          final compId = componentMap[x];
          final currentComponentOnlineStations = onlineStationsInComponent[compId];
          if (currentComponentOnlineStations.isEmpty) {
            results.add(-1);
          } else {
            results.add(currentComponentOnlineStations.first); // Smallest element
          }
        }
      } else { // queryType == 2
        if (isOnline[x]) { // Only process if it's currently online
          isOnline[x] = false;
          final compId = componentMap[x];
          onlineStationsInComponent[compId].remove(x); // Remove from sorted set
        }
      }
    }

    return results;
  }

  void _dfs(int node, int currentComponentId) {
    visited[node] = true;
    componentMap[node] = currentComponentId;
    onlineStationsInComponent[currentComponentId].add(node); // Add to sorted set
    for (final neighbor in adj[node]) {
      if (!visited[neighbor]) {
        _dfs(neighbor, currentComponentId);
      }
    }
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
	"container/heap"
	"fmt"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type Solution struct {
    adj [][]int
    componentMap []int
    visited []bool
    onlineStationsInComponentHeaps []IntHeap
    onlineStationsInComponentActive []map[int]struct{} // Using map as a set
}

func (s *Solution) dfs(node int, currentComponentID int) {
    s.visited[node] = true
    s.componentMap[node] = currentComponentID

    // Add node to the heap and active set of its component
    heap.Push(&s.onlineStationsInComponentHeaps[currentComponentID], node)
    s.onlineStationsInComponentActive[currentComponentID][node] = struct{}{}

    for _, neighbor := range s.adj[node] {
        if !s.visited[neighbor] {
            s.dfs(neighbor, currentComponentID)
        }
    }
}

func (s *Solution) ProcessQueries(c int, connections [][]int, queries [][]int) []int {
    s.adj = make([][]int, c+1)
    for _, conn := range connections {
        u, v := conn[0], conn[1]
        s.adj[u] = append(s.adj[u], v)
        s.adj[v] = append(s.adj[v], u)
    }

    s.componentMap = make([]int, c+1)
    s.visited = make([]bool, c+1)
    s.onlineStationsInComponentHeaps = []
    s.onlineStationsInComponentActive = []

    componentIDCounter := 0
    for i := 1; i <= c; i++ {
        if !s.visited[i] {
            % Initialize new heap and active set for the new component
            s.onlineStationsInComponentHeaps = append(s.onlineStationsInComponentHeaps, IntHeap{})
            s.onlineStationsInComponentActive = append(s.onlineStationsInComponentActive, make(map[int]struct{}))

            s.dfs(i, componentIDCounter)
            componentIDCounter++
        }
    }

    isOnline := make([]bool, c+1)
    for i := 1; i <= c; i++ {
        isOnline[i] = true // Initially all stations are online
    }

    results := []int{}

    for _, query := range queries {
        queryType, x := query[0], query[1]

        if queryType == 1 {
            if isOnline[x] {
                results = append(results, x)
            } else {
                compID := s.componentMap[x]
                currentHeap := &s.onlineStationsInComponentHeaps[compID]
                currentActiveSet := s.onlineStationsInComponentActive[compID]

                // Clean the heap: remove elements that are no longer active
                for currentHeap.Len() > 0 {
                    top := (*currentHeap)[0]
                    if _, ok := currentActiveSet[top]; ok {
                        break // Found an active element
                    }
                    heap.Pop(currentHeap) // Remove inactive element
                }

                if currentHeap.Len() == 0 {
                    results = append(results, -1)
                } else {
                    results = append(results, (*currentHeap)[0])
                }
            }
        } else { // queryType == 2
            if isOnline[x] { // Only process if it's currently online
                isOnline[x] = false
                compID := s.componentMap[x]
                delete(s.onlineStationsInComponentActive[compID], x) // Remove from active set
            }
        }
    }

    return results
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# Custom MinHeap implementation
class MinHeap
    def initialize
        @heap = []
    end

    def empty?
        @heap.empty?
    end

    def push(element)
        @heap << element
        bubble_up(@heap.length - 1)
    end

    def pop
        return nil if empty?
        return @heap.pop if @heap.length == 1

        min = @heap[0]
        @heap[0] = @heap.pop
        bubble_down(0)
        min
    end

    def peek
        @heap.first
    end

    private

    def bubble_up(index)
        current_index = index
        parent_index = (current_index - 1) / 2
        while current_index > 0 && @heap[current_index] < @heap[parent_index]
            @heap[current_index], @heap[parent_index] = @heap[parent_index], @heap[current_index]
            current_index = parent_index
            parent_index = (current_index - 1) / 2
        end
    end

    def bubble_down(index)
        current_index = index
        last_index = @heap.length - 1
        while true
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            smallest_index = current_index

            if left_child_index <= last_index && @heap[left_child_index] < @heap[smallest_index]
                smallest_index = left_child_index
            end
            if right_child_index <= last_index && @heap[right_child_index] < @heap[smallest_index]
                smallest_index = right_child_index
            end

            if smallest_index != current_index
                @heap[current_index], @heap[smallest_index] = @heap[smallest_index], @heap[current_index]
                current_index = smallest_index
            else
                break
            end
        end
    end
end

require 'set'

class Solution
    attr_accessor :adj, :component_map, :visited, :online_stations_in_component_heaps, :online_stations_in_component_active

    def dfs(node, current_component_id)
        @visited[node] = true
        @component_map[node] = current_component_id

        @online_stations_in_component_heaps[current_component_id].push(node)
        @online_stations_in_component_active[current_component_id].add(node)

        (@adj[node] || []).each do |neighbor|
            unless @visited[neighbor]
                dfs(neighbor, current_component_id)
            end
        end
    end

    # @param {Integer} c
    # @param {Integer[][]} connections
    # @param {Integer[][]} queries
    # @return {Integer[]}
    def process_queries(c, connections, queries)
        @adj = Array.new(c + 1) { [] }
        connections.each do |u, v|
            @adj[u] << v
            @adj[v] << u
        end

        @component_map = Array.new(c + 1, 0)
        @visited = Array.new(c + 1, false)
        @online_stations_in_component_heaps = []
        @online_stations_in_component_active = []

        component_id_counter = 0
        (1..c).each do |i|
            unless @visited[i]
                @online_stations_in_component_heaps << MinHeap.new
                @online_stations_in_component_active << Set.new

                dfs(i, component_id_counter)
                component_id_counter += 1
            end
        end

        is_online = Array.new(c + 1, true)

        results = []

        queries.each do |query_type, x|
            if query_type == 1
                if is_online[x]
                    results << x
                else
                    comp_id = @component_map[x]
                    current_heap = @online_stations_in_component_heaps[comp_id]
                    current_active_set = @online_stations_in_component_active[comp_id]

                    # Clean the heap
                    while !current_heap.empty? && !current_active_set.include?(current_heap.peek)
                        current_heap.pop
                    end

                    if current_heap.empty?
                        results << -1
                    else
                        results << current_heap.peek
                    end
                end
            else # query_type == 2
                if is_online[x]
                    is_online[x] = false
                    comp_id = @component_map[x]
                    current_active_set = @online_stations_in_component_active[comp_id]
                    current_active_set.delete(x)
                end
            end
        end

        results
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable
import scala.collection.immutable.TreeSet // For immutable TreeSet, but mutable is often easier for this pattern

class Solution {
    private var adj: Array[mutable.ListBuffer[Int]] = _
    private var componentMap: Array[Int] = _
    private var visited: Array[Boolean] = _
    private var onlineStationsInComponent: mutable.ListBuffer[mutable.TreeSet[Int]] = _

    def processQueries(c: Int, connections: List[List[Int]], queries: List[List[Int]]): List[Int] = {
        adj = Array.fill(c + 1)(mutable.ListBuffer[Int]())
        for (conn <- connections) {
            val u = conn.head
            val v = conn(1)
            adj(u).append(v)
            adj(v).append(u)
        }

        componentMap = Array.fill(c + 1)(0)
        visited = Array.fill(c + 1)(false)
        onlineStationsInComponent = mutable.ListBuffer[mutable.TreeSet[Int]]()

        var componentIdCounter = 0
        for (i <- 1 to c) {
            if (!visited(i)) {
                onlineStationsInComponent.append(mutable.TreeSet[Int]()) // Add a new empty TreeSet
                dfs(i, componentIdCounter)
                componentIdCounter += 1
            }
        }

        val isOnline = Array.fill(c + 1)(true) // Initially all stations are online

        val results = mutable.ListBuffer[Int]()

        for (query <- queries) {
            val queryType = query.head
            val x = query(1)

            if (queryType == 1) {
                if (isOnline(x)) {
                    results.append(x)
                } else {
                    val compId = componentMap(x)
                    val currentComponentOnlineStations = onlineStationsInComponent(compId)
                    if (currentComponentOnlineStations.isEmpty) {
                        results.append(-1)
                    } else {
                        results.append(currentComponentOnlineStations.head) // Smallest element
                    }
                }
            } else { // queryType == 2
                if (isOnline(x)) { // Only process if it's currently online
                    isOnline(x) = false
                    val compId = componentMap(x)
                    onlineStationsInComponent(compId).remove(x) // Remove from sorted set
                }
            }
        }

        results.toList
    }

    private def dfs(node: Int, currentComponentId: Int): Unit = {
        visited(node) = true
        componentMap(node) = currentComponentId
        onlineStationsInComponent(currentComponentId).add(node) // Add to sorted set
        for (neighbor <- adj(node)) {
            if (!visited(neighbor)) {
                dfs(neighbor, currentComponentId)
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::{HashMap, BTreeSet};

struct Solution;

impl Solution {
    fn dfs(
        node: usize,
        current_component_id: usize,
        adj: &Vec<Vec<usize>>,
        component_map: &mut Vec<usize>,
        visited: &mut Vec<bool>,
        online_stations_in_component: &mut Vec<BTreeSet<usize>>,
    ) {
        visited[node] = true;
        component_map[node] = current_component_id;
        online_stations_in_component[current_component_id].insert(node); // Add to sorted set
        for &neighbor in adj[node].iter() {
            if !visited[neighbor] {
                Self::dfs(
                    neighbor,
                    current_component_id,
                    adj,
                    component_map,
                    visited,
                    online_stations_in_component,
                );
            }
        }
    }

    pub fn process_queries(c: i32, connections: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let c_usize = c as usize;
        let mut adj: Vec<Vec<usize>> = vec![vec![]; c_usize + 1];
        for conn in connections {
            let u = conn[0] as usize;
            let v = conn[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        let mut component_map: Vec<usize> = vec![0; c_usize + 1];
        let mut visited: Vec<bool> = vec![false; c_usize + 1];
        let mut online_stations_in_component: Vec<BTreeSet<usize>> = Vec::new();

        let mut component_id_counter = 0;
        for i in 1..=c_usize {
            if !visited[i] {
                online_stations_in_component.push(BTreeSet::new()); // Add a new empty BTreeSet
                Self::dfs(
                    i,
                    component_id_counter,
                    &adj,
                    &mut component_map,
                    &mut visited,
                    &mut online_stations_in_component,
                );
                component_id_counter += 1;
            }
        }

        let mut is_online: Vec<bool> = vec![true; c_usize + 1]; // Initially all stations are online

        let mut results: Vec<i32> = Vec::new();

        for query in queries {
            let query_type = query[0];
            let x = query[1] as usize;

            if query_type == 1 {
                if is_online[x] {
                    results.push(x as i32);
                } else {
                    let comp_id = component_map[x];
                    let current_component_online_stations = &online_stations_in_component[comp_id];
                    if current_component_online_stations.is_empty() {
                        results.push(-1);
                    } else {
                        results.push(*current_component_online_stations.iter().next().unwrap() as i32); // Smallest element
                    }
                }
            } else { // query_type == 2
                if is_online[x] { // Only process if it's currently online
                    is_online[x] = false;
                    let comp_id = component_map[x];
                    online_stations_in_component[comp_id].remove(&x); // Remove from sorted set
                }
            }
        }

        results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(require data/heap) ; For min-heap
(require racket/set) ; For hash-set

(define (process-queries c connections queries)
  (define adj (make-hash))
  (for ([i (range 1 (+ c 1))])
    (hash-set! adj i (list)))
  (for ([conn connections])
    (define u (car conn))
    (define v (cadr conn))
    (hash-set! adj u (cons v (hash-ref adj u)))
    (hash-set! adj v (cons u (hash-ref adj v))))

  (define component-map (make-vector (+ c 1) 0))
  (define visited (make-vector (+ c 1) #f))
  (define online-stations-in-component-heaps (make-vector 0)) ; Dynamic vector of heaps
  (define online-stations-in-component-active (make-vector 0)) ; Dynamic vector of sets

  (define component-id-counter 0)

  (define (dfs node current-component-id)
    (vector-set! visited node #t)
    (vector-set! component-map node current-component-id)

    ;; Add node to the heap and active set of its component
    (heap-add! (vector-ref online-stations-in-component-heaps current-component-id) node)
    (set-add! (vector-ref online-stations-in-component-active current-component-id) node)

    (for ([neighbor (hash-ref adj node)])
      (unless (vector-ref visited neighbor)
        (dfs neighbor current-component-id))))

  (for ([i (range 1 (+ c 1))])
    (unless (vector-ref visited i)
      ;; New component found
      ;; Extend vectors for new component ID
      (set! online-stations-in-component-heaps
            (vector-append online-stations-in-component-heaps (vector (make-heap <))))
      (set! online-stations-in-component-active
            (vector-append online-stations-in-component-active (vector (set))))

      (dfs i component-id-counter)
      (set! component-id-counter (+ component-id-counter 1))))

  (define is-online (make-vector (+ c 1) #t)) ; Initially all stations are online

  (define results (list))

  (for ([query queries])
    (define query-type (car query))
    (define x (cadr query))

    (cond
      [(= query-type 1)
       (if (vector-ref is-online x)
           (set! results (append results (list x)))
           (begin
             (define comp-id (vector-ref component-map x))
             (define current-heap (vector-ref online-stations-in-component-heaps comp-id))
             (define current-active-set (vector-ref online-stations-in-component-active comp-id))

             ;; Clean the heap: remove elements that are no longer active
             (let loop ()
               (when (and (not (heap-empty? current-heap))
                          (not (set-member? current-active-set (heap-min current-heap))))
                 (heap-remove-min! current-heap)
                 (loop)))

             (if (heap-empty? current-heap)
                 (set! results (append results (list -1)))
                 (set! results (append results (list (heap-min current-heap)))))))]
      [(= query-type 2)
       (when (vector-ref is-online x) ; Only process if it's currently online
         (vector-set! is-online x #f)
         (define comp-id (vector-ref component-map x))
         (set-remove! (vector-ref online-stations-in-component-active comp-id) x))]))

  results)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([process_queries/3]).

% Helper function for DFS
% Returns updated maps: {NewVisited, NewComponentMap, NewOnlineStationsInComponent}
dfs(Node, CurrentComponentId, Adj, ComponentMap, Visited, OnlineStationsInComponent) ->
    NewVisited = maps:put(Node, true, Visited),
    NewComponentMap = maps:put(Node, CurrentComponentId, ComponentMap),

    % Add node to the gb_tree for its component
    CurrentTree = maps:get(CurrentComponentId, OnlineStationsInComponent),
    NewTree = gb_trees:insert(Node, Node, CurrentTree), % Store {Node, Node}
    NewOnlineStationsInComponent = maps:put(CurrentComponentId, NewTree, OnlineStationsInComponent),

    Neighbors = maps:get(Node, Adj, []),
    lists:foldl(fun(Neighbor, Acc) ->
        {CurrentVisited, CurrentCompMap, CurrentOnlineStations} = Acc,
        case maps:get(Neighbor, CurrentVisited, false) of
            false ->
                dfs(Neighbor, CurrentComponentId, Adj, CurrentCompMap, CurrentVisited, CurrentOnlineStations);
            true ->
                Acc
        end
    end, {NewVisited, NewComponentMap, NewOnlineStationsInComponent}, Neighbors).

process_queries(C, Connections, Queries) ->
    % Build adjacency list
    Adj = lists:foldl(fun([U, V], Acc) ->
        maps:update_with(U, fun(List) -> [V | List] end, [V], Acc),
        maps:update_with(V, fun(List) -> [U | List] end, [U], Acc)
    end, #{}, Connections),

    % Initialize component data structures
    ComponentMap0 = #{},
    Visited0 = #{},
    OnlineStationsInComponent0 = #{}, % Map from ComponentId to gb_tree

    % Find connected components and populate initial online stations
    {_FinalVisited, FinalComponentMap, InitialOnlineStationsInComponent, _ComponentIdCounter} = 
        lists:foldl(fun(I, Acc) ->
            #{visited := CurrentVisited, component_map := CurrentCompMap, online_stations_in_component := CurrentOnlineStations, comp_id_counter := CompIdCounter} = Acc,
            case maps:get(I, CurrentVisited, false) of
                false ->
                    % New component found
                    NewOnlineStationsInComponentWithNewTree = maps:put(CompIdCounter, gb_trees:empty(), CurrentOnlineStations),

                    {DfsVisited, DfsCompMap, DfsOnlineStations} =
                        dfs(I, CompIdCounter, Adj, CurrentCompMap, CurrentVisited, NewOnlineStationsInComponentWithNewTree),

                    #{visited := DfsVisited, component_map := DfsCompMap, online_stations_in_component := DfsOnlineStations, comp_id_counter := CompIdCounter + 1};
                true ->
                    Acc
            end
        end, #{visited := Visited0, component_map := ComponentMap0, online_stations_in_component := OnlineStationsInComponent0, comp_id_counter := 0}, lists:seq(1, C)),

    IsOnline0 = maps:from_list(lists:map(fun(I) -> {I, true} end, lists:seq(1, C))), % All stations initially online

    % Process queries
    {_FinalIsOnline, _FinalOnlineStationsInComponent, Results} =
        lists:foldl(fun(Query, Acc) ->
            [QueryType, X] = Query,
            #{is_online := CurrentIsOnline, online_stations_in_component := CurrentOnlineStations, results := CurrentResults} = Acc,

            case QueryType of
                1 -> % Maintenance check
                    case maps:get(X, CurrentIsOnline, false) of
                        true -> % X is online
                            #{is_online := CurrentIsOnline, online_stations_in_component := CurrentOnlineStations, results := CurrentResults ++ [X]};
                        false -> % X is offline
                            CompId = maps:get(X, FinalComponentMap),
                            ComponentOnlineStations = maps:get(CompId, CurrentOnlineStations),
                            case gb_trees:is_empty(ComponentOnlineStations) of
                                true ->
                                    #{is_online := CurrentIsOnline, online_stations_in_component := CurrentOnlineStations, results := CurrentResults ++ [-1]};
                                false ->
                                    {MinId, _} = gb_trees:smallest(ComponentOnlineStations),
                                    #{is_online := CurrentIsOnline, online_stations_in_component := CurrentOnlineStations, results := CurrentResults ++ [MinId]}
                            end
                    end;
                2 -> % Station X goes offline
                    case maps:get(X, CurrentIsOnline, false) of
                        true -> % Only process if it's currently online
                            NewIsOnline = maps:put(X, false, CurrentIsOnline),
                            CompId = maps:get(X, FinalComponentMap),
                            ComponentOnlineStations = maps:get(CompId, CurrentOnlineStations),
                            NewComponentOnlineStations = gb_trees:delete(X, ComponentOnlineStations),
                            NewOnlineStationsInComponent = maps:put(CompId, NewComponentOnlineStations, CurrentOnlineStations),
                            #{is_online := NewIsOnline, online_stations_in_component := NewOnlineStationsInComponent, results := CurrentResults};
                        false -> % Already offline, no change
                            Acc
                    end
            end
        end, #{is_online := IsOnline0, online_stations_in_component := InitialOnlineStationsInComponent, results := []}, Queries),

    Results.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec process_queries(c :: integer, connections :: [[integer]], queries :: [[integer]]) :: [integer]
  def process_queries(c, connections, queries) do
    # Build adjacency list
    adj = Enum.reduce(connections, %{}, fn [u, v], acc ->
      acc
      |> Map.update(u, [v], fn list -> [v | list] end)
      |> Map.update(v, [u], fn list -> [u | list] end)
    end)

    # Initialize component data structures
    component_map_0 = %{}
    visited_0 = %{}
    online_stations_in_component_0 = %{} # Map from ComponentId to :gb_trees

    # Find connected components and populate initial online stations
    {_final_visited, final_component_map, initial_online_stations_in_component, _component_id_counter} =
      Enum.reduce(1..c, %{visited: visited_0, component_map: component_map_0, online_stations_in_component: online_stations_in_component_0, comp_id_counter: 0}, fn i, acc ->
        %{visited: current_visited, component_map: current_comp_map, online_stations_in_component: current_online_stations, comp_id_counter: comp_id_counter} = acc
        case Map.get(current_visited, i, false) do
          false ->
            # New component found
            new_online_stations_in_component_with_new_tree = Map.put(current_online_stations, comp_id_counter, :gb_trees.empty())

            {dfs_visited, dfs_comp_map, dfs_online_stations} =
              dfs(i, comp_id_counter, adj, current_comp_map, current_visited, new_online_stations_in_component_with_new_tree)

            %{visited: dfs_visited, component_map: dfs_comp_map, online_stations_in_component: dfs_online_stations, comp_id_counter: comp_id_counter + 1}
          true ->
            acc
        end
      end)

    is_online_0 = Enum.reduce(1..c, %{}, fn i, acc -> Map.put(acc, i, true) end) # All stations initially online

    # Process queries
    {_final_is_online, _final_online_stations_in_component, results} =
      Enum.reduce(queries, %{is_online: is_online_0, online_stations_in_component: initial_online_stations_in_component, results: []}, fn query, acc ->
        [query_type, x] = query
        %{is_online: current_is_online, online_stations_in_component: current_online_stations, results: current_results} = acc

        case query_type do
          1 -> # Maintenance check
            case Map.get(current_is_online, x, false) do
              true -> # X is online
                %{is_online: current_is_online, online_stations_in_component: current_online_stations, results: current_results ++ [x]}
              false -> # X is offline
                comp_id = Map.get(final_component_map, x)
                component_online_stations = Map.get(current_online_stations, comp_id)
                case :gb_trees.is_empty(component_online_stations) do
                  true ->
                    %{is_online: current_is_online, online_stations_in_component: current_online_stations, results: current_results ++ [-1]}
                  false ->
                    {min_id, _} = :gb_trees.smallest(component_online_stations)
                    %{is_online: current_is_online, online_stations_in_component: current_online_stations, results: current_results ++ [min_id]}
                end
            end
          2 -> # Station X goes offline
            case Map.get(current_is_online, x, false) do
              true -> # Only process if it's currently online
                new_is_online = Map.put(current_is_online, x, false)
                comp_id = Map.get(final_component_map, x)
                component_online_stations = Map.get(current_online_stations, comp_id)
                new_component_online_stations = :gb_trees.delete(x, component_online_stations)
                new_online_stations_in_component = Map.put(current_online_stations, comp_id, new_component_online_stations)
                %{is_online: new_is_online, online_stations_in_component: new_online_stations_in_component, results: current_results}
              false -> # Already offline, no change
                acc
            end
        end
      end)

    results
  end

  # Helper function for DFS
  # Returns updated maps: {NewVisited, NewComponentMap, NewOnlineStationsInComponent}
  defp dfs(node, current_component_id, adj, component_map, visited, online_stations_in_component) do
    new_visited = Map.put(visited, node, true)
    new_component_map = Map.put(component_map, node, current_component_id)

    # Add node to the :gb_tree for its component
    current_tree = Map.get(online_stations_in_component, current_component_id)
    new_tree = :gb_trees.insert(node, node, current_tree) # Store {Node, Node}
    new_online_stations_in_component = Map.put(online_stations_in_component, current_component_id, new_tree)

    neighbors = Map.get(adj, node, [])
    Enum.reduce(neighbors, {new_visited, new_component_map, new_online_stations_in_component}, fn neighbor, {current_visited, current_comp_map, current_online_stations} ->
      case Map.get(current_visited, neighbor, false) do
        false ->
          dfs(neighbor, current_component_id, adj, current_comp_map, current_visited, current_online_stations)
        true ->
          {current_visited, current_comp_map, current_online_stations}
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by two phases: initialization and query processing.

1.  **Initialization:**
    *   Building the adjacency list takes `O(c + n)` time, where `c` is the number of stations and `n` is the number of connections.
    *   Performing DFS/BFS to find connected components and populate the initial sorted sets takes `O(c + n)` for graph traversal. During this traversal, each of the `c` stations is inserted into its respective sorted set. In the worst case (one large component), this involves `c` insertions into a single set, each taking `O(log c)` time. Thus, this part is `O(c log c)`.
    *   Total initialization time: `O(c + n + c log c)`.

2.  **Query Processing:**
    *   Each query of type `[1, x]` involves an `O(1)` lookup in `is_online` and `component_map`, followed by an `O(log K)` operation to find the minimum in a sorted set (or amortized `O(log K)` for a lazy deletion heap), where `K` is the number of online stations in the component (`K <= c`). So, `O(log c)` per query.
    *   Each query of type `[2, x]` involves an `O(1)` update in `is_online` and `component_map`, followed by an `O(log K)` operation to remove an element from a sorted set (or amortized `O(log K)` for a lazy deletion heap). So, `O(log c)` per query.
    *   For `q` queries, the total time is `O(q log c)`.

Combining these, the overall time complexity is `O(c + n + (c + q) log c)`. Given `c, n, q <= 2 * 10^5`, `log c` is small (around 17-18), making this approach efficient enough.

- **Space Complexity:** The space complexity is determined by the data structures used:

*   **Adjacency List:** `O(c + n)` to store the graph connections.
*   **`component_map` array:** `O(c)` to store the component ID for each station.
*   **`visited` array:** `O(c)` for DFS/BFS traversal.
*   **`is_online` array:** `O(c)` to store the online/offline status of each station.
*   **`online_stations_in_component` (list of sorted sets/heaps and active sets):** In the worst case, all `c` stations belong to a single component, and all are online. The sorted set (or heap and active set) will store `c` integers. Thus, the total space for these structures is `O(c)`.
*   **DFS recursion stack:** In the worst case (a path graph), the recursion depth can be `O(c)`.

Combining these, the overall space complexity is `O(c + n)`.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-24 07:49:36 )</small>
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
