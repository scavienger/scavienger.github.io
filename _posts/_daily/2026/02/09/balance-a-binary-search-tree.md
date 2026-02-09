---
layout: post
title: "Balance a Binary Search Tree"
date: 2026-02-09 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Divide and Conquer", "Greedy", "Tree", "Depth-First Search", "Binary Search Tree", "Binary Tree"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/balance-a-binary-search-tree/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *   \
        \  int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode()\
        \ : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x),\
        \ left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode\
        \ *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution\
        \ {\npublic:\n    TreeNode* balanceBST(TreeNode* root) {\n        vector<int>\
        \ nodes;\n        inorder(root, nodes);\n        return build(nodes, 0, nodes.size()\
        \ - 1);\n    }\n\nprivate:\n    void inorder(TreeNode* node, vector<int>& nodes)\
        \ {\n        if (!node) return;\n        inorder(node->left, nodes);\n     \
        \   nodes.push_back(node->val);\n        inorder(node->right, nodes);\n    }\n\
        \n    TreeNode* build(const vector<int>& nodes, int start, int end) {\n    \
        \    if (start > end) return nullptr;\n        int mid = start + (end - start)\
        \ / 2;\n        TreeNode* root = new TreeNode(nodes[mid]);\n        root->left\
        \ = build(nodes, start, mid - 1);\n        root->right = build(nodes, mid +\
        \ 1, end);\n        return root;\n    }\n};"
      java: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode()\
        \ {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val,\
        \ TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left\
        \ = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution\
        \ {\n    private List<Integer> nodes = new ArrayList<>();\n\n    public TreeNode\
        \ balanceBST(TreeNode root) {\n        inorder(root);\n        return build(0,\
        \ nodes.size() - 1);\n    }\n\n    private void inorder(TreeNode node) {\n \
        \       if (node == null) return;\n        inorder(node.left);\n        nodes.add(node.val);\n\
        \        inorder(node.right);\n    }\n\n    private TreeNode build(int start,\
        \ int end) {\n        if (start > end) return null;\n        int mid = start\
        \ + (end - start) / 2;\n        TreeNode root = new TreeNode(nodes.get(mid));\n\
        \        root.left = build(start, mid - 1);\n        root.right = build(mid\
        \ + 1, end);\n        return root;\n    }\n}"
      python: "# Definition for a binary tree node.\n# class TreeNode(object):\n#  \
        \   def __init__(self, val=0, left=None, right=None):\n#         self.val =\
        \ val\n#         self.left = left\n#         self.right = right\nclass Solution(object):\n\
        \    def balanceBST(self, root):\n        \"\"\"\n        :type root: Optional[TreeNode]\n\
        \        :rtype: Optional[TreeNode]\n        \"\"\"\n        nodes = []\n  \
        \      def inorder(node):\n            if not node: return\n            inorder(node.left)\n\
        \            nodes.append(node.val)\n            inorder(node.right)\n\n   \
        \     def build(start, end):\n            if start > end: return None\n    \
        \        mid = (start + end) // 2\n            root = TreeNode(nodes[mid])\n\
        \            root.left = build(start, mid - 1)\n            root.right = build(mid\
        \ + 1, end)\n            return root\n\n        inorder(root)\n        return\
        \ build(0, len(nodes) - 1)"
      python3: "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self,\
        \ val=0, left=None, right=None):\n#         self.val = val\n#         self.left\
        \ = left\n#         self.right = right\nclass Solution:\n    def balanceBST(self,\
        \ root: Optional[TreeNode]) -> Optional[TreeNode]:\n        nodes = []\n   \
        \     def inorder(node):\n            if not node: return\n            inorder(node.left)\n\
        \            nodes.append(node.val)\n            inorder(node.right)\n\n   \
        \     def build(start, end):\n            if start > end: return None\n    \
        \        mid = (start + end) // 2\n            root = TreeNode(nodes[mid])\n\
        \            root.left = build(start, mid - 1)\n            root.right = build(mid\
        \ + 1, end)\n            return root\n\n        inorder(root)\n        return\
        \ build(0, len(nodes) - 1)"
      c: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int\
        \ val;\n *     struct TreeNode *left;\n *     struct TreeNode *right;\n * };\n\
        \ */\nvoid inorder(struct TreeNode* root, int* arr, int* size) {\n    if (!root)\
        \ return;\n    inorder(root->left, arr, size);\n    arr[(*size)++] = root->val;\n\
        \    inorder(root->right, arr, size);\n}\n\nstruct TreeNode* build(int* arr,\
        \ int start, int end) {\n    if (start > end) return NULL;\n    int mid = start\
        \ + (end - start) / 2;\n    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct\
        \ TreeNode));\n    root->val = arr[mid];\n    root->left = build(arr, start,\
        \ mid - 1);\n    root->right = build(arr, mid + 1, end);\n    return root;\n\
        }\n\nstruct TreeNode* balanceBST(struct TreeNode* root) {\n    int* arr = (int*)malloc(10001\
        \ * sizeof(int));\n    int size = 0;\n    inorder(root, arr, &size);\n    struct\
        \ TreeNode* result = build(arr, 0, size - 1);\n    free(arr);\n    return result;\n\
        }"
      csharp: "/**\n * Definition for a binary tree node.\n * public class TreeNode\
        \ {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode\
        \ right;\n *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)\
        \ {\n *         this.val = val;\n *         this.left = left;\n *         this.right\
        \ = right;\n *     }\n * }\n */\npublic class Solution {\n    private List<int>\
        \ nodes = new List<int>();\n\n    public TreeNode BalanceBST(TreeNode root)\
        \ {\n        Inorder(root);\n        return Build(0, nodes.Count - 1);\n   \
        \ }\n\n    private void Inorder(TreeNode node) {\n        if (node == null)\
        \ return;\n        Inorder(node.left);\n        nodes.Add(node.val);\n     \
        \   Inorder(node.right);\n    }\n\n    private TreeNode Build(int start, int\
        \ end) {\n        if (start > end) return null;\n        int mid = start + (end\
        \ - start) / 2;\n        TreeNode root = new TreeNode(nodes[mid]);\n       \
        \ root.left = Build(start, mid - 1);\n        root.right = Build(mid + 1, end);\n\
        \        return root;\n    }\n}"
      javascript: "/**\n * Definition for a binary tree node.\n * function TreeNode(val,\
        \ left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left\
        \ = (left===undefined ? null : left)\n *     this.right = (right===undefined\
        \ ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {TreeNode}\n\
        \ */\nvar balanceBST = function(root) {\n    const nodes = [];\n\n    const\
        \ inorder = (node) => {\n        if (!node) return;\n        inorder(node.left);\n\
        \        nodes.push(node.val);\n        inorder(node.right);\n    };\n\n   \
        \ const build = (start, end) => {\n        if (start > end) return null;\n \
        \       const mid = Math.floor((start + end) / 2);\n        const root = new\
        \ TreeNode(nodes[mid]);\n        root.left = build(start, mid - 1);\n      \
        \  root.right = build(mid + 1, end);\n        return root;\n    };\n\n    inorder(root);\n\
        \    return build(0, nodes.length - 1);\n};"
      typescript: "function balanceBST(root: TreeNode | null): TreeNode | null {\n \
        \   const values: number[] = [];\n    function inorder(node: TreeNode | null):\
        \ void {\n        if (!node) return;\n        inorder(node.left);\n        values.push(node.val);\n\
        \        inorder(node.right);\n    }\n    function build(start: number, end:\
        \ number): TreeNode | null {\n        if (start > end) return null;\n      \
        \  const mid = Math.floor((start + end) / 2);\n        const node = new TreeNode(values[mid]);\n\
        \        node.left = build(start, mid - 1);\n        node.right = build(mid\
        \ + 1, end);\n        return node;\n    }\n    inorder(root);\n    return build(0,\
        \ values.length - 1);\n};"
      php: "class Solution {\n    private $values = [];\n    function balanceBST($root)\
        \ {\n        $this->values = [];\n        $this->inorder($root);\n        return\
        \ $this->build(0, count($this->values) - 1);\n    }\n    private function inorder($node)\
        \ {\n        if ($node === null) return;\n        $this->inorder($node->left);\n\
        \        $this->values[] = $node->val;\n        $this->inorder($node->right);\n\
        \    }\n    private function build($start, $end) {\n        if ($start > $end)\
        \ return null;\n        $mid = floor(($start + $end) / 2);\n        $node =\
        \ new TreeNode($this->values[$mid]);\n        $node->left = $this->build($start,\
        \ $mid - 1);\n        $node->right = $this->build($mid + 1, $end);\n       \
        \ return $node;\n    }\n}"
      swift: "class Solution {\n    func balanceBST(_ root: TreeNode?) -> TreeNode?\
        \ {\n        var values = [Int]()\n        func inorder(_ node: TreeNode?) {\n\
        \            guard let node = node else { return }\n            inorder(node.left)\n\
        \            values.append(node.val)\n            inorder(node.right)\n    \
        \    }\n        func build(_ start: Int, _ end: Int) -> TreeNode? {\n      \
        \      if start > end { return nil }\n            let mid = (start + end) /\
        \ 2\n            let node = TreeNode(values[mid])\n            node.left = build(start,\
        \ mid - 1)\n            node.right = build(mid + 1, end)\n            return\
        \ node\n        }\n        inorder(root)\n        return build(0, values.count\
        \ - 1)\n    }\n}"
      kotlin: "class Solution {\n    private val values = mutableListOf<Int>()\n   \
        \ fun balanceBST(root: TreeNode?): TreeNode? {\n        values.clear()\n   \
        \     inorder(root)\n        return build(0, values.size - 1)\n    }\n    private\
        \ fun inorder(node: TreeNode?) {\n        if (node == null) return\n       \
        \ inorder(node.left)\n        values.add(node.`val`)\n        inorder(node.right)\n\
        \    }\n    private fun build(start: Int, end: Int): TreeNode? {\n        if\
        \ (start > end) return null\n        val mid = (start + end) / 2\n        val\
        \ node = TreeNode(values[mid])\n        node.left = build(start, mid - 1)\n\
        \        node.right = build(mid + 1, end)\n        return node\n    }\n}"
      dart: "class Solution {\n  List<int> values = [];\n  TreeNode? balanceBST(TreeNode?\
        \ root) {\n    values = [];\n    _inorder(root);\n    return _build(0, values.length\
        \ - 1);\n  }\n  void _inorder(TreeNode? node) {\n    if (node == null) return;\n\
        \    _inorder(node.left);\n    values.add(node.val);\n    _inorder(node.right);\n\
        \  }\n  TreeNode? _build(int start, int end) {\n    if (start > end) return\
        \ null;\n    int mid = (start + end) ~/ 2;\n    TreeNode node = TreeNode(values[mid]);\n\
        \    node.left = _build(start, mid - 1);\n    node.right = _build(mid + 1, end);\n\
        \    return node;\n  }\n}"
      go: "func balanceBST(root *TreeNode) *TreeNode {\n    var values []int\n    var\
        \ inorder func(*TreeNode)\n    inorder = func(node *TreeNode) {\n        if\
        \ node == nil {\n            return\n        }\n        inorder(node.Left)\n\
        \        values = append(values, node.Val)\n        inorder(node.Right)\n  \
        \  }\n    inorder(root)\n    var build func(int, int) *TreeNode\n    build =\
        \ func(start, end int) *TreeNode {\n        if start > end {\n            return\
        \ nil\n        }\n        mid := (start + end) / 2\n        node := &TreeNode{Val:\
        \ values[mid]}\n        node.Left = build(start, mid-1)\n        node.Right\
        \ = build(mid+1, end)\n        return node\n    }\n    return build(0, len(values)-1)\n\
        }"
      ruby: "def balance_bst(root)\n  vals = []\n  inorder = ->(node) {\n    return\
        \ if node.nil?\n    inorder.call(node.left)\n    vals << node.val\n    inorder.call(node.right)\n\
        \  }\n  inorder.call(root)\n\n  builder = nil\n  builder = ->(l, r) {\n    return\
        \ nil if l > r\n    mid = (l + r) / 2\n    node = TreeNode.new(vals[mid])\n\
        \    node.left = builder.call(l, mid - 1)\n    node.right = builder.call(mid\
        \ + 1, r)\n    node\n  }\n  builder.call(0, vals.length - 1)\nend"
      scala: "object Solution {\n    def balanceBST(root: TreeNode): TreeNode = {\n\
        \        val vals = new scala.collection.mutable.ArrayBuffer[Int]()\n      \
        \  def inorder(node: TreeNode): Unit = {\n            if (node != null) {\n\
        \                inorder(node.left)\n                vals += node.value\n  \
        \              inorder(node.right)\n            }\n        }\n        inorder(root)\n\
        \n        def build(l: Int, r: Int): TreeNode = {\n            if (l > r) return\
        \ null\n            val mid = l + (r - l) / 2\n            val node = new TreeNode(vals(mid))\n\
        \            node.left = build(l, mid - 1)\n            node.right = build(mid\
        \ + 1, r)\n            node\n        }\n        build(0, vals.size - 1)\n  \
        \  }\n}"
      rust: "use std::rc::Rc;\nuse std::cell::RefCell;\n\nimpl Solution {\n    pub fn\
        \ balance_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>>\
        \ {\n        let mut vals = Vec::new();\n        fn inorder(node: &Option<Rc<RefCell<TreeNode>>>,\
        \ vals: &mut Vec<i32>) {\n            if let Some(n) = node {\n            \
        \    let n_borrow = n.borrow();\n                inorder(&n_borrow.left, vals);\n\
        \                vals.push(n_borrow.val);\n                inorder(&n_borrow.right,\
        \ vals);\n            }\n        }\n        inorder(&root, &mut vals);\n\n \
        \       fn build(vals: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {\n        \
        \    if vals.is_empty() {\n                return None;\n            }\n   \
        \         let mid = vals.len() / 2;\n            let node = Rc::new(RefCell::new(TreeNode::new(vals[mid])));\n\
        \            node.borrow_mut().left = build(&vals[..mid]);\n            node.borrow_mut().right\
        \ = build(&vals[mid + 1..]);\n            Some(node)\n        }\n        build(&vals)\n\
        \    }\n}"
      racket: "(define/contract (balance-bst root)\n  (-> (or/c tree-node? #f) (or/c\
        \ tree-node? #f))\n  (letrec ([inorder (lambda (node acc)\n                \
        \      (if (not node)\n                          acc\n                     \
        \     (inorder (tree-node-left node)\n                                   (cons\
        \ (tree-node-val node)\n                                         (inorder (tree-node-right\
        \ node) acc)))))])\n    (let* ([vals (inorder root '())]\n           [vec (list->vector\
        \ vals)]\n           [len (vector-length vec)])\n      (letrec ([build (lambda\
        \ (l r)\n                        (if (> l r)\n                            #f\n\
        \                            (let ([mid (quotient (+ l r) 2)])\n           \
        \                   (tree-node (vector-ref vec mid)\n                      \
        \                   (build l (- mid 1))\n                                  \
        \       (build (+ mid 1) r)))))])\n        (build 0 (- len 1))))))"
      erlang: "balance_bst(Root) ->\n  Vals = inorder(Root, []),\n  Tuple = list_to_tuple(Vals),\n\
        \  build(Tuple, 1, tuple_size(Tuple)).\n\ninorder(null, Acc) -> Acc;\ninorder(#tree_node{val\
        \ = V, left = L, right = R}, Acc) ->\n  inorder(L, [V | inorder(R, Acc)]).\n\
        \nbuild(_Tuple, Start, End) when Start > End -> null;\nbuild(Tuple, Start, End)\
        \ ->\n  Mid = (Start + End) div 2,\n  Val = element(Mid, Tuple),\n  #tree_node{val\
        \ = Val,\n             left = build(Tuple, Start, Mid - 1),\n             right\
        \ = build(Tuple, Mid + 1, End)}."
      elixir: "defmodule Solution do\n  @spec balance_bst(root :: TreeNode.t | nil)\
        \ :: TreeNode.t | nil\n  def balance_bst(root) do\n    vals = inorder(root,\
        \ [])\n    tuple = List.to_tuple(vals)\n    build(tuple, 0, tuple_size(tuple)\
        \ - 1)\n  end\n\n  defp inorder(nil, acc), do: acc\n  defp inorder(%TreeNode{val:\
        \ v, left: l, right: r}, acc) do\n    inorder(l, [v | inorder(r, acc)])\n  end\n\
        \n  defp build(_tuple, start, end_idx) when start > end_idx, do: nil\n  defp\
        \ build(tuple, start, end_idx) do\n    mid = div(start + end_idx, 2)\n    %TreeNode{\n\
        \      val: elem(tuple, mid),\n      left: build(tuple, start, mid - 1),\n \
        \     right: build(tuple, mid + 1, end_idx)\n    }\n  end\nend"
    approach: 'The algorithm follows a two-step process to transform an unbalanced binary
      search tree into a balanced one. First, it performs an in-order traversal of the
      given tree to collect all node values in a sorted list. Since the input is a binary
      search tree, the in-order traversal guarantees that the elements are visited in
      strictly increasing order, providing a linear sequence of the tree''s data.


      In the second step, the algorithm constructs a new balanced BST from the sorted
      list using a recursive divide-and-conquer strategy. By always selecting the middle
      element of the current list segment as the root and recursively building the left
      and right subtrees from the remaining halves, the algorithm ensures that the depth
      of any two subtrees differs by at most one. This approach effectively rebuilds
      the tree with optimal height, achieving the balance property required.'
    time_complexity: O(N), where N is the number of nodes in the tree. The in-order
      traversal visits each node exactly once, and the recursive construction process
      also processes each value in the array exactly once.
    space_complexity: O(N), as an auxiliary array or list is required to store the values
      of all N nodes. Additionally, the recursion stack for the construction process
      consumes O(log N) space, while the traversal stack can consume up to O(N) space
      in the case of a highly unbalanced input tree.
    elapsed_time: 133.15535712242126
    model: gemini-3-flash-preview
    generated_at: '2026-02-09 01:28:56 '
---

## Problem #1382: Balance a Binary Search Tree

**Difficulty:** Medium

**Topics:** Divide and Conquer, Greedy, Tree, Depth-First Search, Binary Search Tree, Binary Tree

## Problem Description

<p>Given the <code>root</code> of a binary search tree, return <em>a <strong>balanced</strong> binary search tree with the same node values</em>. If there is more than one answer, return <strong>any of them</strong>.</p>

<p>A binary search tree is <strong>balanced</strong> if the depth of the two subtrees of every node never differs by more than <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/10/balance1-tree.jpg" style="width: 500px; height: 319px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,null,3,null,4,null,null]
<strong>Output:</strong> [2,1,3,null,null,null,4]
<b>Explanation:</b> This is not the only correct answer, [3,1,4,null,2] is also correct.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/10/balanced2-tree.jpg" style="width: 224px; height: 145px;" />
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> [2,1,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Convert the tree to a sorted array using an in-order traversal.

2. Construct a new balanced tree from the sorted array recursively.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm follows a two-step process to transform an unbalanced binary search tree into a balanced one. First, it performs an in-order traversal of the given tree to collect all node values in a sorted list. Since the input is a binary search tree, the in-order traversal guarantees that the elements are visited in strictly increasing order, providing a linear sequence of the tree's data.

In the second step, the algorithm constructs a new balanced BST from the sorted list using a recursive divide-and-conquer strategy. By always selecting the middle element of the current list segment as the root and recursively building the left and right subtrees from the remaining halves, the algorithm ensures that the depth of any two subtrees differs by at most one. This approach effectively rebuilds the tree with optimal height, achieving the balance property required.

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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* balanceBST(TreeNode* root) {
        vector<int> nodes;
        inorder(root, nodes);
        return build(nodes, 0, nodes.size() - 1);
    }

private:
    void inorder(TreeNode* node, vector<int>& nodes) {
        if (!node) return;
        inorder(node->left, nodes);
        nodes.push_back(node->val);
        inorder(node->right, nodes);
    }

    TreeNode* build(const vector<int>& nodes, int start, int end) {
        if (start > end) return nullptr;
        int mid = start + (end - start) / 2;
        TreeNode* root = new TreeNode(nodes[mid]);
        root->left = build(nodes, start, mid - 1);
        root->right = build(nodes, mid + 1, end);
        return root;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private List<Integer> nodes = new ArrayList<>();

    public TreeNode balanceBST(TreeNode root) {
        inorder(root);
        return build(0, nodes.size() - 1);
    }

    private void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        nodes.add(node.val);
        inorder(node.right);
    }

    private TreeNode build(int start, int end) {
        if (start > end) return null;
        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(nodes.get(mid));
        root.left = build(start, mid - 1);
        root.right = build(mid + 1, end);
        return root;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        nodes = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)

        def build(start, end):
            if start > end: return None
            mid = (start + end) // 2
            root = TreeNode(nodes[mid])
            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)
            return root

        inorder(root)
        return build(0, len(nodes) - 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)

        def build(start, end):
            if start > end: return None
            mid = (start + end) // 2
            root = TreeNode(nodes[mid])
            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)
            return root

        inorder(root)
        return build(0, len(nodes) - 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void inorder(struct TreeNode* root, int* arr, int* size) {
    if (!root) return;
    inorder(root->left, arr, size);
    arr[(*size)++] = root->val;
    inorder(root->right, arr, size);
}

struct TreeNode* build(int* arr, int start, int end) {
    if (start > end) return NULL;
    int mid = start + (end - start) / 2;
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = arr[mid];
    root->left = build(arr, start, mid - 1);
    root->right = build(arr, mid + 1, end);
    return root;
}

struct TreeNode* balanceBST(struct TreeNode* root) {
    int* arr = (int*)malloc(10001 * sizeof(int));
    int size = 0;
    inorder(root, arr, &size);
    struct TreeNode* result = build(arr, 0, size - 1);
    free(arr);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private List<int> nodes = new List<int>();

    public TreeNode BalanceBST(TreeNode root) {
        Inorder(root);
        return Build(0, nodes.Count - 1);
    }

    private void Inorder(TreeNode node) {
        if (node == null) return;
        Inorder(node.left);
        nodes.Add(node.val);
        Inorder(node.right);
    }

    private TreeNode Build(int start, int end) {
        if (start > end) return null;
        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(nodes[mid]);
        root.left = Build(start, mid - 1);
        root.right = Build(mid + 1, end);
        return root;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var balanceBST = function(root) {
    const nodes = [];

    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        nodes.push(node.val);
        inorder(node.right);
    };

    const build = (start, end) => {
        if (start > end) return null;
        const mid = Math.floor((start + end) / 2);
        const root = new TreeNode(nodes[mid]);
        root.left = build(start, mid - 1);
        root.right = build(mid + 1, end);
        return root;
    };

    inorder(root);
    return build(0, nodes.length - 1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function balanceBST(root: TreeNode | null): TreeNode | null {
    const values: number[] = [];
    function inorder(node: TreeNode | null): void {
        if (!node) return;
        inorder(node.left);
        values.push(node.val);
        inorder(node.right);
    }
    function build(start: number, end: number): TreeNode | null {
        if (start > end) return null;
        const mid = Math.floor((start + end) / 2);
        const node = new TreeNode(values[mid]);
        node.left = build(start, mid - 1);
        node.right = build(mid + 1, end);
        return node;
    }
    inorder(root);
    return build(0, values.length - 1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    private $values = [];
    function balanceBST($root) {
        $this->values = [];
        $this->inorder($root);
        return $this->build(0, count($this->values) - 1);
    }
    private function inorder($node) {
        if ($node === null) return;
        $this->inorder($node->left);
        $this->values[] = $node->val;
        $this->inorder($node->right);
    }
    private function build($start, $end) {
        if ($start > $end) return null;
        $mid = floor(($start + $end) / 2);
        $node = new TreeNode($this->values[$mid]);
        $node->left = $this->build($start, $mid - 1);
        $node->right = $this->build($mid + 1, $end);
        return $node;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func balanceBST(_ root: TreeNode?) -> TreeNode? {
        var values = [Int]()
        func inorder(_ node: TreeNode?) {
            guard let node = node else { return }
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        }
        func build(_ start: Int, _ end: Int) -> TreeNode? {
            if start > end { return nil }
            let mid = (start + end) / 2
            let node = TreeNode(values[mid])
            node.left = build(start, mid - 1)
            node.right = build(mid + 1, end)
            return node
        }
        inorder(root)
        return build(0, values.count - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    private val values = mutableListOf<Int>()
    fun balanceBST(root: TreeNode?): TreeNode? {
        values.clear()
        inorder(root)
        return build(0, values.size - 1)
    }
    private fun inorder(node: TreeNode?) {
        if (node == null) return
        inorder(node.left)
        values.add(node.`val`)
        inorder(node.right)
    }
    private fun build(start: Int, end: Int): TreeNode? {
        if (start > end) return null
        val mid = (start + end) / 2
        val node = TreeNode(values[mid])
        node.left = build(start, mid - 1)
        node.right = build(mid + 1, end)
        return node
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> values = [];
  TreeNode? balanceBST(TreeNode? root) {
    values = [];
    _inorder(root);
    return _build(0, values.length - 1);
  }
  void _inorder(TreeNode? node) {
    if (node == null) return;
    _inorder(node.left);
    values.add(node.val);
    _inorder(node.right);
  }
  TreeNode? _build(int start, int end) {
    if (start > end) return null;
    int mid = (start + end) ~/ 2;
    TreeNode node = TreeNode(values[mid]);
    node.left = _build(start, mid - 1);
    node.right = _build(mid + 1, end);
    return node;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func balanceBST(root *TreeNode) *TreeNode {
    var values []int
    var inorder func(*TreeNode)
    inorder = func(node *TreeNode) {
        if node == nil {
            return
        }
        inorder(node.Left)
        values = append(values, node.Val)
        inorder(node.Right)
    }
    inorder(root)
    var build func(int, int) *TreeNode
    build = func(start, end int) *TreeNode {
        if start > end {
            return nil
        }
        mid := (start + end) / 2
        node := &TreeNode{Val: values[mid]}
        node.Left = build(start, mid-1)
        node.Right = build(mid+1, end)
        return node
    }
    return build(0, len(values)-1)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def balance_bst(root)
  vals = []
  inorder = ->(node) {
    return if node.nil?
    inorder.call(node.left)
    vals << node.val
    inorder.call(node.right)
  }
  inorder.call(root)

  builder = nil
  builder = ->(l, r) {
    return nil if l > r
    mid = (l + r) / 2
    node = TreeNode.new(vals[mid])
    node.left = builder.call(l, mid - 1)
    node.right = builder.call(mid + 1, r)
    node
  }
  builder.call(0, vals.length - 1)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def balanceBST(root: TreeNode): TreeNode = {
        val vals = new scala.collection.mutable.ArrayBuffer[Int]()
        def inorder(node: TreeNode): Unit = {
            if (node != null) {
                inorder(node.left)
                vals += node.value
                inorder(node.right)
            }
        }
        inorder(root)

        def build(l: Int, r: Int): TreeNode = {
            if (l > r) return null
            val mid = l + (r - l) / 2
            val node = new TreeNode(vals(mid))
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            node
        }
        build(0, vals.size - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn balance_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut vals = Vec::new();
        fn inorder(node: &Option<Rc<RefCell<TreeNode>>>, vals: &mut Vec<i32>) {
            if let Some(n) = node {
                let n_borrow = n.borrow();
                inorder(&n_borrow.left, vals);
                vals.push(n_borrow.val);
                inorder(&n_borrow.right, vals);
            }
        }
        inorder(&root, &mut vals);

        fn build(vals: &[i32]) -> Option<Rc<RefCell<TreeNode>>> {
            if vals.is_empty() {
                return None;
            }
            let mid = vals.len() / 2;
            let node = Rc::new(RefCell::new(TreeNode::new(vals[mid])));
            node.borrow_mut().left = build(&vals[..mid]);
            node.borrow_mut().right = build(&vals[mid + 1..]);
            Some(node)
        }
        build(&vals)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (balance-bst root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (letrec ([inorder (lambda (node acc)
                      (if (not node)
                          acc
                          (inorder (tree-node-left node)
                                   (cons (tree-node-val node)
                                         (inorder (tree-node-right node) acc)))))])
    (let* ([vals (inorder root '())]
           [vec (list->vector vals)]
           [len (vector-length vec)])
      (letrec ([build (lambda (l r)
                        (if (> l r)
                            #f
                            (let ([mid (quotient (+ l r) 2)])
                              (tree-node (vector-ref vec mid)
                                         (build l (- mid 1))
                                         (build (+ mid 1) r)))))])
        (build 0 (- len 1))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
balance_bst(Root) ->
  Vals = inorder(Root, []),
  Tuple = list_to_tuple(Vals),
  build(Tuple, 1, tuple_size(Tuple)).

inorder(null, Acc) -> Acc;
inorder(#tree_node{val = V, left = L, right = R}, Acc) ->
  inorder(L, [V | inorder(R, Acc)]).

build(_Tuple, Start, End) when Start > End -> null;
build(Tuple, Start, End) ->
  Mid = (Start + End) div 2,
  Val = element(Mid, Tuple),
  #tree_node{val = Val,
             left = build(Tuple, Start, Mid - 1),
             right = build(Tuple, Mid + 1, End)}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec balance_bst(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def balance_bst(root) do
    vals = inorder(root, [])
    tuple = List.to_tuple(vals)
    build(tuple, 0, tuple_size(tuple) - 1)
  end

  defp inorder(nil, acc), do: acc
  defp inorder(%TreeNode{val: v, left: l, right: r}, acc) do
    inorder(l, [v | inorder(r, acc)])
  end

  defp build(_tuple, start, end_idx) when start > end_idx, do: nil
  defp build(tuple, start, end_idx) do
    mid = div(start + end_idx, 2)
    %TreeNode{
      val: elem(tuple, mid),
      left: build(tuple, start, mid - 1),
      right: build(tuple, mid + 1, end_idx)
    }
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the number of nodes in the tree. The in-order traversal visits each node exactly once, and the recursive construction process also processes each value in the array exactly once.
- **Space Complexity:** O(N), as an auxiliary array or list is required to store the values of all N nodes. Additionally, the recursion stack for the construction process consumes O(log N) space, while the traversal stack can consume up to O(N) space in the case of a highly unbalanced input tree.
