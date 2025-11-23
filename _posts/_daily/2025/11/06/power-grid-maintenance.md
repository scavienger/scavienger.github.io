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
  <small class="solution-timestamp">(2025-11-23 01:58:04 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires managing power stations, their connectivity into grids (connected components), and their operational status (online/offline) while efficiently answering queries about the smallest operational station in a grid. The core challenge is to maintain a dynamic set of online stations for each connected component and quickly find the minimum element within these sets.

Our approach involves two main phases: precomputation and query processing. In the precomputation phase, we first build an adjacency list to represent the power grid connections. Then, we use a graph traversal algorithm (Depth First Search or Breadth First Search) to identify all connected components. During this traversal, each station is assigned a unique `component_id`. For each `component_id`, we initialize a data structure that will store the IDs of all stations belonging to that component. Since all stations are initially online, these data structures will initially contain all stations within their respective components. We also maintain a global boolean array, `is_online`, to track the operational status of each station, initialized to `true` for all stations.

In the query processing phase, we iterate through the given queries. For a `[1, x]` query (maintenance check), we first check `is_online[x]`. If `x` is online, `x` itself is the answer. If `x` is offline, we retrieve its `component_id` and then query the data structure associated with that component for its smallest element. This data structure is designed to efficiently provide the minimum online station ID. For a `[2, x]` query (station `x` goes offline), we simply update `is_online[x]` to `false`. The actual removal of `x` from its component's data structure is handled lazily during subsequent `[1, x]` queries to optimize performance. This lazy deletion strategy ensures that elements are only physically removed from the data structure when they are at the top (minimum) and are found to be offline, preventing costly arbitrary removals.

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
    std::vector<int> processQueries(int c, std::vector<std::vector<int>>& connections, std::vector<std::vector<int>>& queries) {
        std::vector<std::vector<int>> adj(c + 1);
        for (const auto& conn : connections) {
            adj[conn[0]].push_back(conn[1]);
            adj[conn[1]].push_back(conn[0]);
        }

        std::vector<int> component_map(c + 1, 0); // Maps station_id to component_id
        std::vector<bool> visited(c + 1, false);

        // Stores sorted sets of online stations for each component
        std::vector<std::set<int>> online_stations_in_component(c + 1); 

        int current_component_id = 0;

        // Step 1: Identify connected components and populate initial sets
        for (int i = 1; i <= c; ++i) {
            if (!visited[i]) {
                current_component_id++;

                std::vector<int> stack;
                stack.push_back(i);
                visited[i] = true;
                component_map[i] = current_component_id;

                std::vector<int> component_nodes; // Collect all nodes in this component

                while (!stack.empty()) {
                    int node = stack.back();
                    stack.pop_back();
                    component_nodes.push_back(node);

                    for (int neighbor : adj[node]) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true;
                            component_map[neighbor] = current_component_id;
                            stack.push_back(neighbor);
                        }
                    }
                }

                // After finding all nodes in a component, add them to its set
                // All nodes are initially online
                for (int node_id : component_nodes) {
                    online_stations_in_component[current_component_id].insert(node_id);
                }
            }
        }

        std::vector<bool> is_online(c + 1, true); // Tracks if a station is currently online

        std::vector<int> results;
        results.reserve(queries.size()); // Pre-allocate memory for results

        // Step 2: Process queries
        for (const auto& query : queries) {
            int query_type = query[0];
            int x = query[1];

            if (query_type == 1) { // Maintenance check
                if (is_online[x]) {
                    results.push_back(x);
                } else {
                    int comp_id = component_map[x];
                    std::set<int>& current_component_set = online_stations_in_component[comp_id];

                    if (!current_component_set.empty()) {
                        results.push_back(*current_component_set.begin()); // Smallest element
                    } else {
                        results.push_back(-1);
                    }
                }
            } else { // Station x goes offline
                if (is_online[x]) { // Only process if it was online
                    is_online[x] = false;
                    int comp_id = component_map[x];
                    online_stations_in_component[comp_id].erase(x);
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
    public List<Integer> processQueries(int c, List<List<Integer>> connections, List<List<Integer>> queries) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= c; i++) {
            adj.add(new ArrayList<>());
        }
        for (List<Integer> conn : connections) {
            int u = conn.get(0);
            int v = conn.get(1);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        int[] componentMap = new int[c + 1]; // Maps station_id to component_id
        boolean[] visited = new boolean[c + 1];

        // Stores sorted sets (TreeSet) of online stations for each component
        List<TreeSet<Integer>> onlineStationsInComponent = new ArrayList<>();
        for (int i = 0; i <= c; i++) {
            onlineStationsInComponent.add(new TreeSet<>());
        }

        int currentComponentId = 0;

        // Step 1: Identify connected components and populate initial sets
        for (int i = 1; i <= c; i++) {
            if (!visited[i]) {
                currentComponentId++;

                Stack<Integer> stack = new Stack<>();
                stack.push(i);
                visited[i] = true;
                componentMap[i] = currentComponentId;

                List<Integer> componentNodes = new ArrayList<>(); // Collect all nodes in this component

                while (!stack.isEmpty()) {
                    int node = stack.pop();
                    componentNodes.add(node);

                    for (int neighbor : adj.get(node)) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true;
                            componentMap[neighbor] = currentComponentId;
                            stack.push(neighbor);
                        }
                    }
                }

                // After finding all nodes in a component, add them to its set
                // All nodes are initially online
                for (int nodeId : componentNodes) {
                    onlineStationsInComponent.get(currentComponentId).add(nodeId);
                }
            }
        }

        boolean[] isOnline = new boolean[c + 1]; // Tracks if a station is currently online
        Arrays.fill(isOnline, true);

        List<Integer> results = new ArrayList<>();

        // Step 2: Process queries
        for (List<Integer> query : queries) {
            int queryType = query.get(0);
            int x = query.get(1);

            if (queryType == 1) { // Maintenance check
                if (isOnline[x]) {
                    results.add(x);
                } else {
                    int compId = componentMap[x];
                    TreeSet<Integer> currentComponentSet = onlineStationsInComponent.get(compId);

                    if (!currentComponentSet.isEmpty()) {
                        results.add(currentComponentSet.first()); // Smallest element
                    } else {
                        results.add(-1);
                    }
                }
            } else { // Station x goes offline
                if (isOnline[x]) { // Only process if it was online
                    isOnline[x] = false;
                    int compId = componentMap[x];
                    onlineStationsInComponent.get(compId).remove(x);
                }
            }
        }

        return results;
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

        component_map = [0] * (c + 1) # Maps station_id to component_id
        visited = [False] * (c + 1)

        # Stores min-heaps for each component
        online_stations_in_component = [[] for _ in range(c + 1)] 

        current_component_id = 0

        # Step 1: Identify connected components and populate initial heaps
        for i in range(1, c + 1):
            if not visited[i]:
                current_component_id += 1

                stack = [i]
                visited[i] = True
                component_map[i] = current_component_id

                component_nodes = [] # Collect all nodes in this component

                while stack:
                    node = stack.pop()
                    component_nodes.append(node)

                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            component_map[neighbor] = current_component_id
                            stack.append(neighbor)

                # After finding all nodes in a component, add them to its heap
                # All nodes are initially online
                for node_id in component_nodes:
                    heapq.heappush(online_stations_in_component[current_component_id], node_id)

        is_online = [True] * (c + 1) # Tracks if a station is currently online

        results = []

        # Step 2: Process queries
        for query_type, x in queries:
            if query_type == 1: # Maintenance check
                if is_online[x]:
                    results.append(x)
                else:
                    comp_id = component_map[x]
                    heap = online_stations_in_component[comp_id]

                    # Lazily remove elements from heap that are no longer online
                    while heap and not is_online[heap[0]]:
                        heapq.heappop(heap)

                    if heap:
                        results.append(heap[0])
                    else:
                        results.append(-1)
            else: # Station x goes offline
                if is_online[x]: # Only process if it was online
                    is_online[x] = False
                    # No need to explicitly remove from heap here, lazy deletion handles it.
                    # The `is_online` array serves as the "removed_from_heap" check.

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

        component_map = [0] * (c + 1) # Maps station_id to component_id
        visited = [False] * (c + 1)

        # Stores min-heaps for each component
        online_stations_in_component = [[] for _ in range(c + 1)] 

        current_component_id = 0

        # Step 1: Identify connected components and populate initial heaps
        for i in range(1, c + 1):
            if not visited[i]:
                current_component_id += 1

                stack = [i]
                visited[i] = True
                component_map[i] = current_component_id

                component_nodes = [] # Collect all nodes in this component

                while stack:
                    node = stack.pop()
                    component_nodes.append(node)

                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            component_map[neighbor] = current_component_id
                            stack.append(neighbor)

                # After finding all nodes in a component, add them to its heap
                # All nodes are initially online
                for node_id in component_nodes:
                    heapq.heappush(online_stations_in_component[current_component_id], node_id)

        is_online = [True] * (c + 1) # Tracks if a station is currently online

        results = []

        # Step 2: Process queries
        for query_type, x in queries:
            if query_type == 1: # Maintenance check
                if is_online[x]:
                    results.append(x)
                else:
                    comp_id = component_map[x]
                    heap = online_stations_in_component[comp_id]

                    # Lazily remove elements from heap that are no longer online
                    while heap and not is_online[heap[0]]:
                        heapq.heappop(heap)

                    if heap:
                        results.append(heap[0])
                    else:
                        results.append(-1)
            else: # Station x goes offline
                if is_online[x]: # Only process if it was online
                    is_online[x] = False
                    # No need to explicitly remove from heap here, lazy deletion handles it.
                    # The `is_online` array serves as the "removed_from_heap" check.

        return results
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// --- Adjacency List (Graph) Implementation ---
typedef struct AdjNode {
    int dest;
    struct AdjNode* next;
} AdjNode;

typedef struct {
    AdjNode** heads;
    int num_vertices;
} Graph;

Graph* createGraph(int num_vertices) {
    Graph* graph = (Graph*)malloc(sizeof(Graph));
    graph->num_vertices = num_vertices;
    graph->heads = (AdjNode**)calloc(num_vertices + 1, sizeof(AdjNode*));
    return graph;
}

void addEdge(Graph* graph, int src, int dest) {
    AdjNode* newNode = (AdjNode*)malloc(sizeof(AdjNode));
    newNode->dest = dest;
    newNode->next = graph->heads[src];
    graph->heads[src] = newNode;
}

void freeGraph(Graph* graph) {
    for (int i = 0; i <= graph->num_vertices; i++) {
        AdjNode* current = graph->heads[i];
        while (current != NULL) {
            AdjNode* temp = current;
            current = current->next;
            free(temp);
        }
    }
    free(graph->heads);
    free(graph);
}

// --- Min-Heap Implementation (for lazy deletion) ---
typedef struct {
    int* arr;
    int capacity;
    int size;
} MinHeap;

MinHeap* createMinHeap(int capacity) {
    MinHeap* heap = (MinHeap*)malloc(sizeof(MinHeap));
    heap->capacity = capacity;
    heap->size = 0;
    heap->arr = (int*)malloc(sizeof(int) * capacity);
    return heap;
}

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapify(MinHeap* heap, int idx) {
    int smallest = idx;
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;

    if (left < heap->size && heap->arr[left] < heap->arr[smallest])
        smallest = left;

    if (right < heap->size && heap->arr[right] < heap->arr[smallest])
        smallest = right;

    if (smallest != idx) {
        swap(&heap->arr[idx], &heap->arr[smallest]);
        heapify(heap, smallest);
    }
}

void insertMinHeap(MinHeap* heap, int val) {
    if (heap->size == heap->capacity) {
        // Resize if needed, though for this problem, capacity is fixed to c
        return;
    }
    heap->size++;
    int i = heap->size - 1;
    heap->arr[i] = val;

    while (i != 0 && heap->arr[(i - 1) / 2] > heap->arr[i]) {
        swap(&heap->arr[i], &heap->arr[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

int extractMin(MinHeap* heap) {
    if (heap->size <= 0) return -1; // Or some indicator of error
    if (heap->size == 1) {
        heap->size--;
        return heap->arr[0];
    }

    int root = heap->arr[0];
    heap->arr[0] = heap->arr[heap->size - 1];
    heap->size--;
    heapify(heap, 0);

    return root;
}

int getMin(MinHeap* heap) {
    if (heap->size <= 0) return -1;
    return heap->arr[0];
}

bool isEmpty(MinHeap* heap) {
    return heap->size == 0;
}

void freeMinHeap(MinHeap* heap) {
    free(heap->arr);
    free(heap);
}

// --- Solution Function ---
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* processQueries(int c, int** connections, int connectionsSize, int* connectionsColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    Graph* graph = createGraph(c);
    for (int i = 0; i < connectionsSize; i++) {
        addEdge(graph, connections[i][0], connections[i][1]);
        addEdge(graph, connections[i][1], connections[i][0]);
    }

    int* component_map = (int*)calloc(c + 1, sizeof(int)); // Maps station_id to component_id
    bool* visited = (bool*)calloc(c + 1, sizeof(bool));

    // Stores min-heaps for each component
    MinHeap** online_stations_in_component = (MinHeap**)calloc(c + 1, sizeof(MinHeap*));
    for (int i = 0; i <= c; i++) {
        // Max capacity for a heap is 'c' (all stations in one component)
        online_stations_in_component[i] = createMinHeap(c);
    }

    int current_component_id = 0;

    // Step 1: Identify connected components and populate initial heaps
    for (int i = 1; i <= c; i++) {
        if (!visited[i]) {
            current_component_id++;

            // Using a simple array as a stack for DFS
            int* stack = (int*)malloc(sizeof(int) * (c + 1));
            int stack_top = -1;

            stack[++stack_top] = i;
            visited[i] = true;
            component_map[i] = current_component_id;

            // Collect all nodes in this component to add to heap later
            int* component_nodes = (int*)malloc(sizeof(int) * (c + 1));
            int component_nodes_count = 0;

            while (stack_top != -1) {
                int node = stack[stack_top--];
                component_nodes[component_nodes_count++] = node;

                AdjNode* current_adj = graph->heads[node];
                while (current_adj != NULL) {
                    int neighbor = current_adj->dest;
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        component_map[neighbor] = current_component_id;
                        stack[++stack_top] = neighbor;
                    }
                    current_adj = current_adj->next;
                }
            }

            // After finding all nodes in a component, add them to its heap
            // All nodes are initially online
            for (int node_idx = 0; node_idx < component_nodes_count; node_idx++) {
                insertMinHeap(online_stations_in_component[current_component_id], component_nodes[node_idx]);
            }
            free(stack);
            free(component_nodes);
        }
    }

    bool* is_online = (bool*)malloc(sizeof(bool) * (c + 1)); // Tracks if a station is currently online
    for (int i = 0; i <= c; i++) {
        is_online[i] = true;
    }

    int* results = (int*)malloc(sizeof(int) * queriesSize);
    *returnSize = 0;

    // Step 2: Process queries
    for (int q_idx = 0; q_idx < queriesSize; q_idx++) {
        int query_type = queries[q_idx][0];
        int x = queries[q_idx][1];

        if (query_type == 1) { // Maintenance check
            if (is_online[x]) {
                results[(*returnSize)++] = x;
            } else {
                int comp_id = component_map[x];
                MinHeap* heap = online_stations_in_component[comp_id];

                // Lazily remove elements from heap that are no longer online
                while (!isEmpty(heap) && !is_online[getMin(heap)]) {
                    extractMin(heap);
                }

                if (!isEmpty(heap)) {
                    results[(*returnSize)++] = getMin(heap);
                } else {
                    results[(*returnSize)++] = -1;
                }
            }
        } else { // Station x goes offline
            if (is_online[x]) { // Only process if it was online
                is_online[x] = false;
                // No need to explicitly remove from heap here, lazy deletion handles it.
                // The `is_online` array serves as the "removed_from_heap" check.
            }
        }
    }

    // Clean up allocated memory
    freeGraph(graph);
    free(component_map);
    free(visited);
    for (int i = 0; i <= c; i++) {
        freeMinHeap(online_stations_in_component[i]);
    }
    free(online_stations_in_component);
    free(is_online);

    return results;
}
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
    public IList<int> ProcessQueries(int c, IList<IList<int>> connections, IList<IList<int>> queries) {
        List<List<int>> adj = new List<List<int>>();
        for (int i = 0; i <= c; i++) {
            adj.Add(new List<int>());
        }
        foreach (var conn in connections) {
            int u = conn[0];
            int v = conn[1];
            adj[u].Add(v);
            adj[v].Add(u);
        }

        int[] componentMap = new int[c + 1]; // Maps station_id to component_id
        bool[] visited = new bool[c + 1];

        // Stores sorted sets (SortedSet) of online stations for each component
        List<SortedSet<int>> onlineStationsInComponent = new List<SortedSet<int>>();
        for (int i = 0; i <= c; i++) {
            onlineStationsInComponent.Add(new SortedSet<int>());
        }

        int currentComponentId = 0;

        // Step 1: Identify connected components and populate initial sets
        for (int i = 1; i <= c; i++) {
            if (!visited[i]) {
                currentComponentId++;

                Stack<int> stack = new Stack<int>();
                stack.Push(i);
                visited[i] = true;
                componentMap[i] = currentComponentId;

                List<int> componentNodes = new List<int>(); // Collect all nodes in this component

                while (stack.Count > 0) {
                    int node = stack.Pop();
                    componentNodes.Add(node);

                    foreach (int neighbor in adj[node]) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true;
                            componentMap[neighbor] = currentComponentId;
                            stack.Push(neighbor);
                        }
                    }
                }

                // After finding all nodes in a component, add them to its set
                // All nodes are initially online
                foreach (int nodeId in componentNodes) {
                    onlineStationsInComponent[currentComponentId].Add(nodeId);
                }
            }
        }

        bool[] isOnline = new bool[c + 1]; // Tracks if a station is currently online
        Array.Fill(isOnline, true);

        List<int> results = new List<int>();

        // Step 2: Process queries
        foreach (var query in queries) {
            int queryType = query[0];
            int x = query[1];

            if (queryType == 1) { // Maintenance check
                if (isOnline[x]) {
                    results.Add(x);
                } else {
                    int compId = componentMap[x];
                    SortedSet<int> currentComponentSet = onlineStationsInComponent[compId];

                    if (currentComponentSet.Count > 0) {
                        results.Add(currentComponentSet.Min);
                    } else {
                        results.Add(-1);
                    }
                }
            } else { // Station x goes offline
                if (isOnline[x]) { // Only process if it was online
                    isOnline[x] = false;
                    int compId = componentMap[x];
                    onlineStationsInComponent[compId].Remove(x);
                }
            }
        }

        return results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} c
 * @param {number[][]} connections
 * @param {number[][]} queries
 * @return {number[]}
 */
class MinHeap {
    constructor() {
        this.heap = [];
    }

    getParentIndex(i) { return Math.floor((i - 1) / 2); }
    getLeftChildIndex(i) { return 2 * i + 1; }
    getRightChildIndex(i) { return 2 * i + 2; }

    hasParent(i) { return this.getParentIndex(i) >= 0; }
    hasLeftChild(i) { return this.getLeftChildIndex(i) < this.heap.length; }
    hasRightChild(i) { return this.getRightChildIndex(i) < this.heap.length; }

    getParent(i) { return this.heap[this.getParentIndex(i)]; }
    getLeftChild(i) { return this.heap[this.getLeftChildIndex(i)]; }
    getRightChild(i) { return this.heap[this.getRightChildIndex(i)]; }

    peek() {
        if (this.heap.length === 0) return null;
        return this.heap[0];
    }

    insert(item) {
        this.heap.push(item);
        this.heapifyUp();
    }

    extractMin() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const item = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return item;
    }

    heapifyUp() {
        let index = this.heap.length - 1;
        while (this.hasParent(index) && this.getParent(index) > this.heap[index]) {
            this.swap(this.getParentIndex(index), index);
            index = this.getParentIndex(index);
        }
    }

    heapifyDown() {
        let index = 0;
        while (this.hasLeftChild(index)) {
            let smallerChildIndex = this.getLeftChildIndex(index);
            if (this.hasRightChild(index) && this.getRightChild(index) < this.getLeftChild(index)) {
                smallerChildIndex = this.getRightChildIndex(index);
            }

            if (this.heap[index] < this.heap[smallerChildIndex]) {
                break;
            } else {
                this.swap(index, smallerChildIndex);
            }
            index = smallerChildIndex;
        }
    }

    swap(indexOne, indexTwo) {
        [this.heap[indexOne], this.heap[indexTwo]] = [this.heap[indexTwo], this.heap[indexOne]];
    }

    isEmpty() {
        return this.heap.length === 0;
    }
}

var processQueries = function(c, connections, queries) {
    const adj = Array.from({ length: c + 1 }, () => []);
    for (const [u, v] of connections) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const componentMap = new Array(c + 1).fill(0); // Maps station_id to component_id
    const visited = new Array(c + 1).fill(false);

    // Stores min-heaps for each component
    const onlineStationsInComponent = Array.from({ length: c + 1 }, () => new MinHeap()); 

    let currentComponentId = 0;

    // Step 1: Identify connected components and populate initial heaps
    for (let i = 1; i <= c; i++) {
        if (!visited[i]) {
            currentComponentId++;

            const stack = [i];
            visited[i] = true;
            componentMap[i] = currentComponentId;

            const componentNodes = []; // Collect all nodes in this component

            while (stack.length > 0) {
                const node = stack.pop();
                componentNodes.push(node);

                for (const neighbor of adj[node]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        componentMap[neighbor] = currentComponentId;
                        stack.push(neighbor);
                    }
                }
            }

            // After finding all nodes in a component, add them to its heap
            // All nodes are initially online
            for (const nodeId of componentNodes) {
                onlineStationsInComponent[currentComponentId].insert(nodeId);
            }
        }
    }

    const isOnline = new Array(c + 1).fill(true); // Tracks if a station is currently online

    const results = [];

    // Step 2: Process queries
    for (const [queryType, x] of queries) {
        if (queryType === 1) { // Maintenance check
            if (isOnline[x]) {
                results.push(x);
            } else {
                const compId = componentMap[x];
                const heap = onlineStationsInComponent[compId];

                // Lazily remove elements from heap that are no longer online
                while (!heap.isEmpty() && !isOnline[heap.peek()]) {
                    heap.extractMin();
                }

                if (!heap.isEmpty()) {
                    results.push(heap.peek());
                } else {
                    results.push(-1);
                }
            }
        } else { // Station x goes offline
            if (isOnline[x]) { // Only process if it was online
                isOnline[x] = false;
                // No need to explicitly remove from heap here, lazy deletion handles it.
                // The `isOnline` array serves as the "removed_from_heap" check.
            }
        }
    }

    return results;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
/**
 * @param {number} c
 * @param {number[][]} connections
 * @param {number[][]} queries
 * @return {number[]}
 */

class MinHeap {
    private heap: number[];

    constructor() {
        this.heap = [];
    }

    private getParentIndex(i: number): number { return Math.floor((i - 1) / 2); }
    private getLeftChildIndex(i: number): number { return 2 * i + 1; }
    private getRightChildIndex(i: number): number { return 2 * i + 2; }

    private hasParent(i: number): boolean { return this.getParentIndex(i) >= 0; }
    private hasLeftChild(i: number): boolean { return this.getLeftChildIndex(i) < this.heap.length; }
    private hasRightChild(i: number): boolean { return this.getRightChildIndex(i) < this.heap.length; }

    private getParent(i: number): number { return this.heap[this.getParentIndex(i)]; }
    private getLeftChild(i: number): number { return this.heap[this.getLeftChildIndex(i)]; }
    private getRightChild(i: number): number { return this.heap[this.getRightChildIndex(i)]; }

    peek(): number | null {
        if (this.heap.length === 0) return null;
        return this.heap[0];
    }

    insert(item: number): void {
        this.heap.push(item);
        this.heapifyUp();
    }

    extractMin(): number | null {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop()!;

        const item = this.heap[0];
        this.heap[0] = this.heap.pop()!;
        this.heapifyDown();
        return item;
    }

    private heapifyUp(): void {
        let index = this.heap.length - 1;
        while (this.hasParent(index) && this.getParent(index) > this.heap[index]) {
            this.swap(this.getParentIndex(index), index);
            index = this.getParentIndex(index);
        }
    }

    private heapifyDown(): void {
        let index = 0;
        while (this.hasLeftChild(index)) {
            let smallerChildIndex = this.getLeftChildIndex(index);
            if (this.hasRightChild(index) && this.getRightChild(index) < this.getLeftChild(index)) {
                smallerChildIndex = this.getRightChildIndex(index);
            }

            if (this.heap[index] < this.heap[smallerChildIndex]) {
                break;
            } else {
                this.swap(index, smallerChildIndex);
            }
            index = smallerChildIndex;
        }
    }

    private swap(indexOne: number, indexTwo: number): void {
        [this.heap[indexOne], this.heap[indexTwo]] = [this.heap[indexTwo], this.heap[indexOne]];
    }

    isEmpty(): boolean {
        return this.heap.length === 0;
    }
}

function processQueries(c: number, connections: number[][], queries: number[][]): number[] {
    const adj: number[][] = Array.from({ length: c + 1 }, () => []);
    for (const [u, v] of connections) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const componentMap: number[] = new Array(c + 1).fill(0); // Maps station_id to component_id
    const visited: boolean[] = new Array(c + 1).fill(false);

    // Stores min-heaps for each component
    const onlineStationsInComponent: MinHeap[] = Array.from({ length: c + 1 }, () => new MinHeap()); 

    let currentComponentId = 0;

    // Step 1: Identify connected components and populate initial heaps
    for (let i = 1; i <= c; i++) {
        if (!visited[i]) {
            currentComponentId++;

            const stack: number[] = [i];
            visited[i] = true;
            componentMap[i] = currentComponentId;

            const componentNodes: number[] = []; // Collect all nodes in this component

            while (stack.length > 0) {
                const node = stack.pop()!;
                componentNodes.push(node);

                for (const neighbor of adj[node]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        componentMap[neighbor] = currentComponentId;
                        stack.push(neighbor);
                    }
                }
            }

            // After finding all nodes in a component, add them to its heap
            // All nodes are initially online
            for (const nodeId of componentNodes) {
                onlineStationsInComponent[currentComponentId].insert(nodeId);
            }
        }
    }

    const isOnline: boolean[] = new Array(c + 1).fill(true); // Tracks if a station is currently online

    const results: number[] = [];

    // Step 2: Process queries
    for (const [queryType, x] of queries) {
        if (queryType === 1) { // Maintenance check
            if (isOnline[x]) {
                results.push(x);
            } else {
                const compId = componentMap[x];
                const heap = onlineStationsInComponent[compId];

                // Lazily remove elements from heap that are no longer online
                while (!heap.isEmpty() && !isOnline[heap.peek()!]) {
                    heap.extractMin();
                }

                if (!heap.isEmpty()) {
                    results.push(heap.peek()!);
                } else {
                    results.push(-1);
                }
            }
        } else { // Station x goes offline
            if (isOnline[x]) { // Only process if it was online
                isOnline[x] = false;
                // No need to explicitly remove from heap here, lazy deletion handles it.
                // The `isOnline` array serves as the "removed_from_heap" check.
            }
        }
    }

    return results;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php

class MinHeap extends SplMinHeap {
    public function compare($value1, $value2): int {
        return $value1 - $value2;
    }
}

class Solution {
    /**
     * @param int $c
     * @param int[][] $connections
     * @param int[][] $queries
     * @return int[]
     */
    function processQueries(int $c, array $connections, array $queries): array {
        $adj = array_fill(0, $c + 1, []);
        foreach ($connections as $conn) {
            $u = $conn[0];
            $v = $conn[1];
            $adj[$u][] = $v;
            $adj[$v][] = $u;
        }

        $componentMap = array_fill(0, $c + 1, 0); // Maps station_id to component_id
        $visited = array_fill(0, $c + 1, false);

        // Stores min-heaps for each component
        $onlineStationsInComponent = array_fill(0, $c + 1, null);
        for ($i = 0; $i <= $c; $i++) {
            $onlineStationsInComponent[$i] = new MinHeap();
        }

        $currentComponentId = 0;

        // Step 1: Identify connected components and populate initial heaps
        for ($i = 1; $i <= $c; $i++) {
            if (!$visited[$i]) {
                $currentComponentId++;

                $stack = [$i];
                $visited[$i] = true;
                $componentMap[$i] = $currentComponentId;

                $componentNodes = []; // Collect all nodes in this component

                while (!empty($stack)) {
                    $node = array_pop($stack);
                    $componentNodes[] = $node;

                    foreach ($adj[$node] as $neighbor) {
                        if (!$visited[$neighbor]) {
                            $visited[$neighbor] = true;
                            $componentMap[$neighbor] = $currentComponentId;
                            $stack[] = $neighbor;
                        }
                    }
                }

                // After finding all nodes in a component, add them to its heap
                // All nodes are initially online
                foreach ($componentNodes as $nodeId) {
                    $onlineStationsInComponent[$currentComponentId]->insert($nodeId);
                }
            }
        }

        $isOnline = array_fill(0, $c + 1, true); // Tracks if a station is currently online

        $results = [];

        // Step 2: Process queries
        foreach ($queries as $query) {
            $queryType = $query[0];
            $x = $query[1];

            if ($queryType === 1) { // Maintenance check
                if ($isOnline[$x]) {
                    $results[] = $x;
                } else {
                    $compId = $componentMap[$x];
                    /** @var MinHeap $heap */
                    $heap = $onlineStationsInComponent[$compId];

                    // Lazily remove elements from heap that are no longer online
                    while (!$heap->isEmpty() && !$isOnline[$heap->top()]) {
                        $heap->extract();
                    }

                    if (!$heap->isEmpty()) {
                        $results[] = $heap->top();
                    } else {
                        $results[] = -1;
                    }
                }
            } else { // Station x goes offline
                if ($isOnline[$x]) { // Only process if it was online
                    $isOnline[$x] = false;
                    // No need to explicitly remove from heap here, lazy deletion handles it.
                    // The `isOnline` array serves as the "removed_from_heap" check.
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
class MinHeap {
    private var heap: [Int]

    init() {
        heap = []
    }

    private func getParentIndex(_ i: Int) -> Int { return (i - 1) / 2 }
    private func getLeftChildIndex(_ i: Int) -> Int { return 2 * i + 1 }
    private func getRightChildIndex(_ i: Int) -> Int { return 2 * i + 2 }

    private func hasParent(_ i: Int) -> Bool { return getParentIndex(i) >= 0 }
    private func hasLeftChild(_ i: Int) -> Bool { return getLeftChildIndex(i) < heap.count }
    private func hasRightChild(_ i: Int) -> Bool { return getRightChildIndex(i) < heap.count }

    private func getParent(_ i: Int) -> Int { return heap[getParentIndex(i)] }
    private func getLeftChild(_ i: Int) -> Int { return heap[getLeftChildIndex(i)] }
    private func getRightChild(_ i: Int) -> Int { return heap[getRightChildIndex(i)] }

    func peek() -> Int? {
        return heap.first
    }

    func insert(_ item: Int) {
        heap.append(item)
        heapifyUp()
    }

    func extractMin() -> Int? {
        if heap.isEmpty { return nil }
        if heap.count == 1 { return heap.removeLast() }

        let item = heap[0]
        heap[0] = heap.removeLast()
        heapifyDown()
        return item
    }

    private func heapifyUp() {
        var index = heap.count - 1
        while hasParent(index) && getParent(index) > heap[index] {
            swap(getParentIndex(index), index)
            index = getParentIndex(index)
        }
    }

    private func heapifyDown() {
        var index = 0
        while hasLeftChild(index) {
            var smallerChildIndex = getLeftChildIndex(index)
            if hasRightChild(index) && getRightChild(index) < getLeftChild(index) {
                smallerChildIndex = getRightChildIndex(index)
            }

            if heap[index] < heap[smallerChildIndex] {
                break
            } else {
                swap(index, smallerChildIndex)
            }
            index = smallerChildIndex
        }
    }

    private func swap(_ indexOne: Int, _ indexTwo: Int) {
        heap.swapAt(indexOne, indexTwo)
    }

    func isEmpty() -> Bool {
        return heap.isEmpty
    }
}

class Solution {
    func processQueries(_ c: Int, _ connections: [[Int]], _ queries: [[Int]]) -> [Int] {
        var adj: [[Int]] = Array(repeating: [], count: c + 1)
        for conn in connections {
            let u = conn[0]
            let v = conn[1]
            adj[u].append(v)
            adj[v].append(u)
        }

        var componentMap: [Int] = Array(repeating: 0, count: c + 1) // Maps station_id to component_id
        var visited: [Bool] = Array(repeating: false, count: c + 1)

        // Stores min-heaps for each component
        var onlineStationsInComponent: [MinHeap] = Array(repeating: MinHeap(), count: c + 1)

        var currentComponentId = 0

        // Step 1: Identify connected components and populate initial heaps
        for i in 1...c {
            if !visited[i] {
                currentComponentId += 1

                var stack: [Int] = [i]
                visited[i] = true
                componentMap[i] = currentComponentId

                var componentNodes: [Int] = [] // Collect all nodes in this component

                while !stack.isEmpty {
                    let node = stack.removeLast()
                    componentNodes.append(node)

                    for neighbor in adj[node] {
                        if !visited[neighbor] {
                            visited[neighbor] = true
                            componentMap[neighbor] = currentComponentId
                            stack.append(neighbor)
                        }
                    }
                }

                // After finding all nodes in a component, add them to its heap
                // All nodes are initially online
                for nodeId in componentNodes {
                    onlineStationsInComponent[currentComponentId].insert(nodeId)
                }
            }
        }

        var isOnline: [Bool] = Array(repeating: true, count: c + 1) // Tracks if a station is currently online

        var results: [Int] = []

        // Step 2: Process queries
        for query in queries {
            let queryType = query[0]
            let x = query[1]

            if queryType == 1 { // Maintenance check
                if isOnline[x] {
                    results.append(x)
                } else {
                    let compId = componentMap[x]
                    let heap = onlineStationsInComponent[compId]

                    // Lazily remove elements from heap that are no longer online
                    while !heap.isEmpty() && !isOnline[heap.peek()!] {
                        _ = heap.extractMin()
                    }

                    if !heap.isEmpty() {
                        results.append(heap.peek()!)
                    } else {
                        results.append(-1)
                    }
                }
            } else { // Station x goes offline
                if isOnline[x] { // Only process if it was online
                    isOnline[x] = false
                    // No need to explicitly remove from heap here, lazy deletion handles it.
                    // The `isOnline` array serves as the "removed_from_heap" check.
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

class Solution {
    fun processQueries(c: Int, connections: List<List<Int>>, queries: List<List<Int>>): List<Int> {
        val adj = Array(c + 1) { mutableListOf<Int>() }
        for (conn in connections) {
            val u = conn[0]
            val v = conn[1]
            adj[u].add(v)
            adj[v].add(u)
        }

        val componentMap = IntArray(c + 1) { 0 } // Maps station_id to component_id
        val visited = BooleanArray(c + 1) { false }

        // Stores sorted sets (TreeSet) of online stations for each component
        val onlineStationsInComponent = Array(c + 1) { TreeSet<Int>() }

        var currentComponentId = 0

        // Step 1: Identify connected components and populate initial sets
        for (i in 1..c) {
            if (!visited[i]) {
                currentComponentId++

                val stack = Stack<Int>()
                stack.push(i)
                visited[i] = true
                componentMap[i] = currentComponentId

                val componentNodes = mutableListOf<Int>() // Collect all nodes in this component

                while (stack.isNotEmpty()) {
                    val node = stack.pop()
                    componentNodes.add(node)

                    for (neighbor in adj[node]) {
                        if (!visited[neighbor]) {
                            visited[neighbor] = true
                            componentMap[neighbor] = currentComponentId
                            stack.push(neighbor)
                        }
                    }
                }

                // After finding all nodes in a component, add them to its set
                // All nodes are initially online
                for (nodeId in componentNodes) {
                    onlineStationsInComponent[currentComponentId].add(nodeId)
                }
            }
        }

        val isOnline = BooleanArray(c + 1) { true } // Tracks if a station is currently online

        val results = mutableListOf<Int>()

        // Step 2: Process queries
        for (query in queries) {
            val queryType = query[0]
            val x = query[1]

            if (queryType == 1) { // Maintenance check
                if (isOnline[x]) {
                    results.add(x)
                } else {
                    val compId = componentMap[x]
                    val currentComponentSet = onlineStationsInComponent[compId]

                    if (currentComponentSet.isNotEmpty()) {
                        results.add(currentComponentSet.first())
                    } else {
                        results.add(-1)
                    }
                }
            } else { // Station x goes offline
                if (isOnline[x]) { // Only process if it was online
                    isOnline[x] = false
                    val compId = componentMap[x]
                    onlineStationsInComponent[compId].remove(x)
                }
            }
        }

        return results
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
  List<int> processQueries(int c, List<List<int>> connections, List<List<int>> queries) {
    final List<List<int>> adj = List.generate(c + 1, (_) => []);
    for (final conn in connections) {
      final u = conn[0];
      final v = conn[1];
      adj[u].add(v);
      adj[v].add(u);
    }

    final List<int> componentMap = List.filled(c + 1, 0); // Maps station_id to component_id
    final List<bool> visited = List.filled(c + 1, false);

    // Stores sorted sets (SplayTreeSet) of online stations for each component
    final List<SplayTreeSet<int>> onlineStationsInComponent = List.generate(c + 1, (_) => SplayTreeSet<int>());

    int currentComponentId = 0;

    // Step 1: Identify connected components and populate initial sets
    for (int i = 1; i <= c; i++) {
      if (!visited[i]) {
        currentComponentId++;

        final List<int> stack = [i];
        visited[i] = true;
        componentMap[i] = currentComponentId;

        final List<int> componentNodes = []; // Collect all nodes in this component

        while (stack.isNotEmpty) {
          final node = stack.removeLast();
          componentNodes.add(node);

          for (final neighbor in adj[node]) {
            if (!visited[neighbor]) {
              visited[neighbor] = true;
              componentMap[neighbor] = currentComponentId;
              stack.add(neighbor);
            }
          }
        }

        // After finding all nodes in a component, add them to its set
        // All nodes are initially online
        for (final nodeId in componentNodes) {
          onlineStationsInComponent[currentComponentId].add(nodeId);
        }
      }
    }

    final List<bool> isOnline = List.filled(c + 1, true); // Tracks if a station is currently online

    final List<int> results = [];

    // Step 2: Process queries
    for (final query in queries) {
      final queryType = query[0];
      final x = query[1];

      if (queryType == 1) { // Maintenance check
        if (isOnline[x]) {
          results.add(x);
        } else {
          final compId = componentMap[x];
          final SplayTreeSet<int> currentComponentSet = onlineStationsInComponent[compId];

          if (currentComponentSet.isNotEmpty) {
            results.add(currentComponentSet.first);
          } else {
            results.add(-1);
          }
        }
      } else { // Station x goes offline
        if (isOnline[x]) { // Only process if it was online
          isOnline[x] = false;
          final compId = componentMap[x];
          onlineStationsInComponent[compId].remove(x);
        }
      }
    }

    return results;
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

func processQueries(c int, connections [][]int, queries [][]int) []int {
	adj := make([][]int, c+1)
	for _, conn := range connections {
		u, v := conn[0], conn[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	componentMap := make([]int, c+1) // Maps station_id to component_id
	visited := make([]bool, c+1)

	// Stores min-heaps for each component
	onlineStationsInComponent := make([]*IntHeap, c+1)
	for i := 0; i <= c; i++ {
		h := &IntHeap{}
		heap.Init(h)
		onlineStationsInComponent[i] = h
	}

	currentComponentId := 0

	// Step 1: Identify connected components and populate initial heaps
	for i := 1; i <= c; i++ {
		if !visited[i] {
			currentComponentId++

			stack := []int{i}
			visited[i] = true
			componentMap[i] = currentComponentId

			var componentNodes []int // Collect all nodes in this component

			for len(stack) > 0 {
				node := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				componentNodes = append(componentNodes, node)

				for _, neighbor := range adj[node] {
					if !visited[neighbor] {
						visited[neighbor] = true
						componentMap[neighbor] = currentComponentId
						stack = append(stack, neighbor)
					}
				}
			}

			// After finding all nodes in a component, add them to its heap
			// All nodes are initially online
			for _, nodeId := range componentNodes {
				heap.Push(onlineStationsInComponent[currentComponentId], nodeId)
			}
		}
	}

	isOnline := make([]bool, c+1)
	for i := 0; i <= c; i++ {
		isOnline[i] = true
	}

	var results []int

	// Step 2: Process queries
	for _, query := range queries {
		queryType, x := query[0], query[1]

		if queryType == 1 { // Maintenance check
			if isOnline[x] {
				results = append(results, x)
			} else {
				compId := componentMap[x]
				heapRef := onlineStationsInComponent[compId]

				// Lazily remove elements from heap that are no longer online
				for heapRef.Len() > 0 && !isOnline[(*heapRef)[0]] {
					heap.Pop(heapRef)
				}

				if heapRef.Len() > 0 {
					results = append(results, (*heapRef)[0])
				} else {
					results = append(results, -1)
				}
			}
		} else { // Station x goes offline
			if isOnline[x] { // Only process if it was online
				isOnline[x] = false
				// No need to explicitly remove from heap here, lazy deletion handles it.
				// The `isOnline` array serves as the "removed_from_heap" check.
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
require 'set'

class MinHeap
  def initialize
    @heap = []
  end

  def push(item)
    @heap << item
    heapify_up(@heap.length - 1)
  end

  def pop
    return nil if @heap.empty?
    return @heap.pop if @heap.length == 1

    min_item = @heap[0]
    @heap[0] = @heap.pop
    heapify_down(0)
    min_item
  end

  def peek
    @heap[0]
  end

  def empty?
    @heap.empty?
  end

  private

  def heapify_up(index)
    while index > 0
      parent_index = (index - 1) / 2
      if @heap[parent_index] > @heap[index]
        swap(parent_index, index)
        index = parent_index
      else
        break
      end
    end
  end

  def heapify_down(index)
    loop do
      left_child_index = 2 * index + 1
      right_child_index = 2 * index + 2
      smallest_child_index = index

      if left_child_index < @heap.length && @heap[left_child_index] < @heap[smallest_child_index]
        smallest_child_index = left_child_index
      end

      if right_child_index < @heap.length && @heap[right_child_index] < @heap[smallest_child_index]
        smallest_child_index = right_child_index
      end

      if smallest_child_index != index
        swap(index, smallest_child_index)
        index = smallest_child_index
      else
        break
      end
    end
  end

  def swap(i, j)
    @heap[i], @heap[j] = @heap[j], @heap[i]
  end
end

class Solution
  def process_queries(c, connections, queries)
    adj = Array.new(c + 1) { [] }
    connections.each do |u, v|
      adj[u] << v
      adj[v] << u
    end

    component_map = Array.new(c + 1, 0) # Maps station_id to component_id
    visited = Array.new(c + 1, false)

    # Stores min-heaps for each component
    online_stations_in_component = Array.new(c + 1) { MinHeap.new }

    current_component_id = 0

    # Step 1: Identify connected components and populate initial heaps
    (1..c).each do |i|
      unless visited[i]
        current_component_id += 1

        stack = [i]
        visited[i] = true
        component_map[i] = current_component_id

        component_nodes = [] # Collect all nodes in this component

        while !stack.empty?
          node = stack.pop
          component_nodes << node

          adj[node].each do |neighbor|
            unless visited[neighbor]
              visited[neighbor] = true
              component_map[neighbor] = current_component_id
              stack.push(neighbor)
            end
          end
        end

        # After finding all nodes in a component, add them to its heap
        # All nodes are initially online
        component_nodes.each do |node_id|
          online_stations_in_component[current_component_id].push(node_id)
        end
      end
    end

    is_online = Array.new(c + 1, true) # Tracks if a station is currently online

    results = []

    # Step 2: Process queries
    queries.each do |query_type, x|
      if query_type == 1 # Maintenance check
        if is_online[x]
          results << x
        else
          comp_id = component_map[x]
          heap = online_stations_in_component[comp_id]

          # Lazily remove elements from heap that are no longer online
          while !heap.empty? && !is_online[heap.peek]
            heap.pop
          end

          if !heap.empty?
            results << heap.peek
          else
            results << -1
          end
        end
      else # Station x goes offline
        if is_online[x] # Only process if it was online
          is_online[x] = false
          # No need to explicitly remove from heap here, lazy deletion handles it.
          # The `is_online` array serves as the "removed_from_heap" check.
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
import scala.collection.immutable.TreeSet

class Solution {
    def processQueries(c: Int, connections: List[List[Int]], queries: List[List[Int]]): List[Int] = {
        val adj: Array[mutable.ListBuffer[Int]] = Array.fill(c + 1)(mutable.ListBuffer[Int]())
        for (conn <- connections) {
            val u = conn(0)
            val v = conn(1)
            adj(u).append(v)
            adj(v).append(u)
        }

        val componentMap: Array[Int] = Array.fill(c + 1)(0) // Maps station_id to component_id
        val visited: Array[Boolean] = Array.fill(c + 1)(false)

        // Stores sorted sets (TreeSet) of online stations for each component
        val onlineStationsInComponent: Array[TreeSet[Int]] = Array.fill(c + 1)(TreeSet.empty[Int])

        var currentComponentId = 0

        // Step 1: Identify connected components and populate initial sets
        for (i <- 1 to c) {
            if (!visited(i)) {
                currentComponentId += 1

                val stack = mutable.Stack[Int]()
                stack.push(i)
                visited(i) = true
                componentMap(i) = currentComponentId

                val componentNodes = mutable.ListBuffer[Int]() // Collect all nodes in this component

                while (stack.nonEmpty) {
                    val node = stack.pop()
                    componentNodes.append(node)

                    for (neighbor <- adj(node)) {
                        if (!visited(neighbor)) {
                            visited(neighbor) = true
                            componentMap(neighbor) = currentComponentId
                            stack.push(neighbor)
                        }
                    }
                }

                // After finding all nodes in a component, add them to its set
                // All nodes are initially online
                for (nodeId <- componentNodes) {
                    onlineStationsInComponent(currentComponentId) += nodeId
                }
            }
        }

        val isOnline: Array[Boolean] = Array.fill(c + 1)(true) // Tracks if a station is currently online

        val results = mutable.ListBuffer[Int]()

        // Step 2: Process queries
        for (query <- queries) {
            val queryType = query(0)
            val x = query(1)

            if (queryType == 1) { // Maintenance check
                if (isOnline(x)) {
                    results.append(x)
                } else {
                    val compId = componentMap(x)
                    val currentComponentSet = onlineStationsInComponent(compId)

                    if (currentComponentSet.nonEmpty) {
                        results.append(currentComponentSet.head)
                    } else {
                        results.append(-1)
                    }
                }
            } else { // Station x goes offline
                if (isOnline(x)) { // Only process if it was online
                    isOnline(x) = false
                    val compId = componentMap(x)
                    onlineStationsInComponent(compId) -= x
                }
            }
        }

        results.toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::{HashMap, VecDeque, BTreeSet};

impl Solution {
    pub fn process_queries(c: i32, connections: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let c_usize = c as usize;
        let mut adj: Vec<Vec<usize>> = vec![vec![]; c_usize + 1];
        for conn in connections {
            let u = conn[0] as usize;
            let v = conn[1] as usize;
            adj[u].push(v);
            adj[v].push(u);
        }

        let mut component_map: Vec<usize> = vec![0; c_usize + 1]; // Maps station_id to component_id
        let mut visited: Vec<bool> = vec![false; c_usize + 1];

        // Stores sorted sets (BTreeSet) of online stations for each component
        let mut online_stations_in_component: Vec<BTreeSet<usize>> = vec![BTreeSet::new(); c_usize + 1];

        let mut current_component_id = 0;

        // Step 1: Identify connected components and populate initial sets
        for i in 1..=c_usize {
            if !visited[i] {
                current_component_id += 1;

                let mut stack: VecDeque<usize> = VecDeque::new();
                stack.push_back(i);
                visited[i] = true;
                component_map[i] = current_component_id;

                let mut component_nodes: Vec<usize> = Vec::new(); // Collect all nodes in this component

                while let Some(node) = stack.pop_back() {
                    component_nodes.push(node);

                    for &neighbor in adj[node].iter() {
                        if !visited[neighbor] {
                            visited[neighbor] = true;
                            component_map[neighbor] = current_component_id;
                            stack.push_back(neighbor);
                        }
                    }
                }

                // After finding all nodes in a component, add them to its set
                // All nodes are initially online
                for node_id in component_nodes {
                    online_stations_in_component[current_component_id].insert(node_id);
                }
            }
        }

        let mut is_online: Vec<bool> = vec![true; c_usize + 1]; // Tracks if a station is currently online

        let mut results: Vec<i32> = Vec::new();

        // Step 2: Process queries
        for query in queries {
            let query_type = query[0];
            let x = query[1] as usize;

            if query_type == 1 { // Maintenance check
                if is_online[x] {
                    results.push(x as i32);
                } else {
                    let comp_id = component_map[x];
                    let current_component_set = &online_stations_in_component[comp_id];

                    if let Some(&min_val) = current_component_set.iter().next() {
                        results.push(min_val as i32);
                    } else {
                        results.push(-1);
                    }
                }
            } else { // Station x goes offline
                if is_online[x] { // Only process if it was online
                    is_online[x] = false;
                    let comp_id = component_map[x];
                    online_stations_in_component[comp_id].remove(&x);
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

(define (process-queries c connections queries)
  (define adj (make-vector (+ c 1) '()))
  (for-each (lambda (conn)
              (define u (car conn))
              (define v (cadr conn))
              (vector-set! adj u (cons v (vector-ref adj u)))
              (vector-set! adj v (cons u (vector-ref adj v))))
            connections)

  (define component-map (make-vector (+ c 1) 0)) ; Maps station_id to component_id
  (define visited (make-vector (+ c 1) #f))

  ; Stores sorted sets (using red-black-tree from data/red-black-tree) of online stations for each component
  (define online-stations-in-component (make-vector (+ c 1) (rbt-empty <))) ; rbt-empty requires a comparator

  (define current-component-id 0)

  ; Step 1: Identify connected components and populate initial sets
  (for ([i (in-range 1 (+ c 1))])
    (when (not (vector-ref visited i))
      (set! current-component-id (+ current-component-id 1))

      (define stack (list i))
      (vector-set! visited i #t)
      (vector-set! component-map i current-component-id)

      (define component-nodes '()) ; Collect all nodes in this component

      (let loop ([current-stack stack] [nodes component-nodes])
        (if (empty? current-stack)
            (begin
              ; After finding all nodes in a component, add them to its set
              ; All nodes are initially online
              (for-each (lambda (node-id)
                          (vector-set! online-stations-in-component current-component-id
                                       (rbt-add (vector-ref online-stations-in-component current-component-id) node-id)))
                        nodes))
            (let* ([node (car current-stack)]
                   [rest-stack (cdr current-stack)])
              (loop (foldl (lambda (neighbor acc)
                             (if (not (vector-ref visited neighbor))
                                 (begin
                                   (vector-set! visited neighbor #t)
                                   (vector-set! component-map neighbor current-component-id)
                                   (cons neighbor acc))
                                 acc))
                           rest-stack
                           (vector-ref adj node))
                    (cons node nodes))))))

  (define is-online (make-vector (+ c 1) #t)) ; Tracks if a station is currently online

  (define results '())

  ; Step 2: Process queries
  (for-each (lambda (query)
              (define query-type (car query))
              (define x (cadr query))

              (cond
                [(= query-type 1) ; Maintenance check
                 (if (vector-ref is-online x)
                     (set! results (append results (list x)))
                     (let* ([comp-id (vector-ref component-map x)]
                            [current-component-set (vector-ref online-stations-in-component comp-id)])
                       (if (rbt-empty? current-component-set)
                           (set! results (append results (list -1)))
                           (set! results (append results (list (rbt-min current-component-set)))))))]
                [(= query-type 2) ; Station x goes offline
                 (when (vector-ref is-online x) ; Only process if it was online
                   (vector-set! is-online x #f)
                   (define comp-id (vector-ref component-map x))
                   (vector-set! online-stations-in-component comp-id
                                (rbt-remove (vector-ref online-stations-in-component comp-id) x))))]))
            queries)

  results)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([process_queries/3]).

-include_lib("stdlib/include/gb_trees.hrl").

process_queries(C, Connections, Queries) ->
    Adj = build_adj(C, Connections),

    ComponentMap = array:new(C + 1, {default, 0}),
    Visited = array:new(C + 1, {default, false}),

    OnlineStationsInComponent = array:new(C + 1, {default, gb_trees:empty()}),

    {FinalComponentMap, FinalVisited, FinalOnlineStationsInComponent, _} = 
        lists:foldl(fun(I, {AccComponentMap, AccVisited, AccOnlineStationsInComponent, CurrentComponentId}) ->
            case array:get(I, AccVisited) of
                false ->
                    NewComponentId = CurrentComponentId + 1,

                    Stack = [I],
                    NewVisited1 = array:set(I, true, AccVisited),
                    NewComponentMap1 = array:set(I, NewComponentId, AccComponentMap),

                    {ComponentNodes, NewVisited2, NewComponentMap2} = 
                        dfs(Stack, [], NewVisited1, NewComponentMap1, NewComponentId, Adj),

                    InitialComponentSet = lists:foldl(fun(NodeId, AccSet) ->
                        gb_trees:insert(NodeId, true, AccSet)
                    end, gb_trees:empty(), ComponentNodes),

                    NewOnlineStationsInComponent = array:set(NewComponentId, InitialComponentSet, AccOnlineStationsInComponent),

                    {NewComponentMap2, NewVisited2, NewOnlineStationsInComponent, NewComponentId};
                true ->
                    {AccComponentMap, AccVisited, AccOnlineStationsInComponent, CurrentComponentId}
            end
        end, {ComponentMap, Visited, OnlineStationsInComponent, 0}, lists:seq(1, C)),

    IsOnline = array:new(C + 1, {default, true}),

    lists:foldl(fun(Query, {AccResults, AccIsOnline, AccOnlineStationsInComponent}) ->
        QueryType = hd(Query),
        X = hd(tl(Query)),

        case QueryType of
            1 -> % Maintenance check
                case array:get(X, AccIsOnline) of
                    true ->
                        {AccResults ++ [X], AccIsOnline, AccOnlineStationsInComponent};
                    false ->
                        CompId = array:get(X, FinalComponentMap),
                        ComponentSet = array:get(CompId, AccOnlineStationsInComponent),

                        case gb_trees:is_empty(ComponentSet) of
                            true ->
                                {AccResults ++ [-1], AccIsOnline, AccOnlineStationsInComponent};
                            false ->
                                {MinVal, _} = gb_trees:smallest(ComponentSet),
                                {AccResults ++ [MinVal], AccIsOnline, AccOnlineStationsInComponent}
                        end
                end;
            2 -> % Station X goes offline
                case array:get(X, AccIsOnline) of
                    true ->
                        NewIsOnline = array:set(X, false, AccIsOnline),
                        CompId = array:get(X, FinalComponentMap),
                        ComponentSet = array:get(CompId, AccOnlineStationsInComponent),
                        NewComponentSet = gb_trees:delete(X, ComponentSet),
                        NewOnlineStationsInComponent = array:set(CompId, NewComponentSet, AccOnlineStationsInComponent),
                        {AccResults, NewIsOnline, NewOnlineStationsInComponent};
                    false ->
                        {AccResults, AccIsOnline, AccOnlineStationsInComponent}
                end
        end
    end, {[], IsOnline, FinalOnlineStationsInComponent}, Queries) of
        {Results, _, _} -> Results
    end.

build_adj(C, Connections) ->
    lists:foldl(fun([U, V], AccAdj) ->
        maps:update_with(U, fun(List) -> [V | List] end, [V], AccAdj)
            end, maps:new(), Connections).

dfs(Stack, ComponentNodes, Visited, ComponentMap, CurrentComponentId, Adj) ->
    case Stack of
        [] ->
            {ComponentNodes, Visited, ComponentMap};
        [Node | RestStack] ->
            NewComponentNodes = [Node | ComponentNodes],

            Neighbors = maps:get(Node, Adj, []),

            {NewStack, NewVisited, NewComponentMap} = 
                lists:foldl(fun(Neighbor, {AccStack, AccVisited, AccComponentMap}) ->
                    case array:get(Neighbor, AccVisited) of
                        false ->
                            { [Neighbor | AccStack], 
                              array:set(Neighbor, true, AccVisited), 
                              array:set(Neighbor, CurrentComponentId, AccComponentMap) };
                        true ->
                            {AccStack, AccVisited, AccComponentMap}
                    end
                end, {RestStack, Visited, ComponentMap}, Neighbors),

            dfs(NewStack, NewComponentNodes, NewVisited, NewComponentMap, CurrentComponentId, Adj)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec process_queries(c :: integer, connections :: [[integer]], queries :: [[integer]]) :: [integer]
  def process_queries(c, connections, queries) do
    adj = build_adj(c, connections)

    component_map = :array.new(c + 1, default: 0)
    visited = :array.new(c + 1, default: false)

    online_stations_in_component = :array.new(c + 1, default: MapSet.new())

    {final_component_map, final_visited, final_online_stations_in_component, _} = 
      Enum.reduce(1..c, {component_map, visited, online_stations_in_component, 0},
        fn i, {acc_component_map, acc_visited, acc_online_stations_in_component, current_component_id} ->
          case :array.get(i, acc_visited) do
            false ->
              new_component_id = current_component_id + 1

              stack = [i]
              new_visited1 = :array.set(i, true, acc_visited)
              new_component_map1 = :array.set(i, new_component_id, acc_component_map)

              {component_nodes, new_visited2, new_component_map2} = 
                dfs(stack, [], new_visited1, new_component_map1, new_component_id, adj)

              initial_component_set = Enum.reduce(component_nodes, MapSet.new(), fn node_id, acc_set ->
                MapSet.put(acc_set, node_id)
              end)

              new_online_stations_in_component = :array.set(new_component_id, initial_component_set, acc_online_stations_in_component)

              {new_component_map2, new_visited2, new_online_stations_in_component, new_component_id}
            true ->
              {acc_component_map, acc_visited, acc_online_stations_in_component, current_component_id}
          end
        end)

    is_online = :array.new(c + 1, default: true)

    {results, _, _} = Enum.reduce(queries, {[], is_online, final_online_stations_in_component},
      fn query, {acc_results, acc_is_online, acc_online_stations_in_component} ->
        [query_type, x] = query

        case query_type do
          1 -> # Maintenance check
            case :array.get(x, acc_is_online) do
              true ->
                {acc_results ++ [x], acc_is_online, acc_online_stations_in_component}
              false ->
                comp_id = :array.get(x, final_component_map)
                component_set = :array.get(comp_id, acc_online_stations_in_component)

                if MapSet.empty?(component_set) do
                  {acc_results ++ [-1], acc_is_online, acc_online_stations_in_component}
                else
                  min_val = Enum.min(component_set)
                  {acc_results ++ [min_val], acc_is_online, acc_online_stations_in_component}
                end
            end
          2 -> # Station X goes offline
            case :array.get(x, acc_is_online) do
              true ->
                new_is_online = :array.set(x, false, acc_is_online)
                comp_id = :array.get(x, final_component_map)
                component_set = :array.get(comp_id, acc_online_stations_in_component)
                new_component_set = MapSet.delete(component_set, x)
                new_online_stations_in_component = :array.set(comp_id, new_component_set, acc_online_stations_in_component)
                {acc_results, new_is_online, new_online_stations_in_component}
              false ->
                {acc_results, acc_is_online, acc_online_stations_in_component}
            end
        end
      end)
    results
  end

  defp build_adj(c, connections) do
    Enum.reduce(connections, %{}, fn [u, v], acc_adj ->
      acc_adj
      |> Map.update(u, [v], fn list -> [v | list] end)
      |> Map.update(v, [u], fn list -> [u | list] end)
    end)
  end

  defp dfs(stack, component_nodes, visited, component_map, current_component_id, adj) do
    case stack do
      [] ->
        {component_nodes, visited, component_map}
      [node | rest_stack] ->
        new_component_nodes = [node | component_nodes]

        neighbors = Map.get(adj, node, [])

        {new_stack, new_visited, new_component_map} = 
          Enum.reduce(neighbors, {rest_stack, visited, component_map},
            fn neighbor, {acc_stack, acc_visited, acc_component_map} ->
              case :array.get(neighbor, acc_visited) do
                false ->
                  { [neighbor | acc_stack],
                    :array.set(neighbor, true, acc_visited),
                    :array.set(neighbor, current_component_id, acc_component_map) }
                true ->
                  {acc_stack, acc_visited, acc_component_map}
              end
            end)

        dfs(new_stack, new_component_nodes, new_visited, new_component_map, current_component_id, adj)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(c + n + Q log c).

1.  **Graph Construction:** Building the adjacency list takes O(c + n) time, where `c` is the number of stations and `n` is the number of connections.
2.  **Component Identification and Initialization:** A single DFS or BFS pass over the graph takes O(c + n) time. During this traversal, each station is visited once, and its `component_id` is assigned. For each component, all its stations are added to a sorted data structure (e.g., `std::set` in C++, `TreeSet` in Java, or a min-heap in Python with lazy deletion). In the worst case, all `c` stations might be in one component, leading to `c` insertions into a single structure. Each insertion takes O(log k) time, where `k` is the current size of the structure. Thus, the total time for initial population is O(c log c).
3.  **Query Processing:** There are `Q` queries.
    *   Type `[1, x]` (Maintenance Check): Checking `is_online[x]` is O(1). Accessing the component's data structure and retrieving the minimum element takes O(log c) time (for `std::set`/`TreeSet`) or O(log c) amortized time (for min-heap with lazy deletion, as each element is pushed once and popped at most once). The `while` loop for lazy deletion processes elements that are no longer online; each such element is popped from the heap at most once across all queries.
    *   Type `[2, x]` (Station Offline): Updating `is_online[x]` is O(1). With lazy deletion, no immediate operation on the sorted data structure is needed.
    Therefore, each query takes O(log c) time in the worst case.

Combining these, the total time complexity is O(c + n + c log c + Q log c), which simplifies to O(c + n + Q log c).

- **Space Complexity:** The space complexity is O(c + n).

1.  **Adjacency List (`adj`):** Stores graph connections, requiring O(c + n) space.
2.  **Component Map (`component_map`):** An array of size `c+1` to store component IDs for each station, taking O(c) space.
3.  **Visited Array (`visited`):** A boolean array of size `c+1` for DFS/BFS, taking O(c) space.
4.  **`is_online` Array:** A boolean array of size `c+1` to track station status, taking O(c) space.
5.  **Sorted Data Structures (`online_stations_in_component`):** This is an array/list of `c+1` sorted sets or min-heaps. Each station ID is stored exactly once across all these data structures. Therefore, the total space occupied by all these structures is O(c).
6.  **DFS/BFS Stack:** In the worst case (a long path), the recursion stack or explicit stack for DFS/BFS can go up to O(c) depth.

Combining these, the total space complexity is O(c + n).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-23 01:58:05 )</small>
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
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A

</div>
</details>
