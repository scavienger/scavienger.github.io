---
layout: post
title: "Sum of Root To Leaf Binary Numbers"
date: 2026-02-24 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Tree", "Depth-First Search", "Binary Tree"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *   \
        \  int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode()\
        \ : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x),\
        \ left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode\
        \ *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution\
        \ {\npublic:\n    int calculate(TreeNode* node, int currentSum) {\n        if\
        \ (!node) return 0;\n        currentSum = (currentSum << 1) | node->val;\n \
        \       if (!node->left && !node->right) {\n            return currentSum;\n\
        \        }\n        return calculate(node->left, currentSum) + calculate(node->right,\
        \ currentSum);\n    }\n\n    int sumRootToLeaf(TreeNode* root) {\n        return\
        \ calculate(root, 0);\n    }\n};"
      java: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode()\
        \ {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val,\
        \ TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left\
        \ = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution\
        \ {\n    public int sumRootToLeaf(TreeNode root) {\n        return dfs(root,\
        \ 0);\n    }\n\n    private int dfs(TreeNode node, int currentSum) {\n     \
        \   if (node == null) return 0;\n        currentSum = (currentSum << 1) | node.val;\n\
        \        if (node.left == null && node.right == null) {\n            return\
        \ currentSum;\n        }\n        return dfs(node.left, currentSum) + dfs(node.right,\
        \ currentSum);\n    }\n}"
      python: "# Definition for a binary tree node.\n# class TreeNode(object):\n#  \
        \   def __init__(self, val=0, left=None, right=None):\n#         self.val =\
        \ val\n#         self.left = left\n#         self.right = right\nclass Solution(object):\n\
        \    def sumRootToLeaf(self, root):\n        \"\"\"\n        :type root: Optional[TreeNode]\n\
        \        :rtype: int\n        \"\"\"\n        def dfs(node, current_sum):\n\
        \            if not node:\n                return 0\n            current_sum\
        \ = (current_sum << 1) | node.val\n            if not node.left and not node.right:\n\
        \                return current_sum\n            return dfs(node.left, current_sum)\
        \ + dfs(node.right, current_sum)\n\n        return dfs(root, 0)"
      python3: "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self,\
        \ val=0, left=None, right=None):\n#         self.val = val\n#         self.left\
        \ = left\n#         self.right = right\nclass Solution:\n    def sumRootToLeaf(self,\
        \ root: Optional[TreeNode]) -> int:\n        def dfs(node, current_sum):\n \
        \           if not node:\n                return 0\n            current_sum\
        \ = (current_sum << 1) | node.val\n            if not node.left and not node.right:\n\
        \                return current_sum\n            return dfs(node.left, current_sum)\
        \ + dfs(node.right, current_sum)\n\n        return dfs(root, 0)"
      c: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int\
        \ val;\n *     struct TreeNode *left;\n *     struct TreeNode *right;\n * };\n\
        \ */\nint dfs(struct TreeNode* node, int currentSum) {\n    if (node == NULL)\
        \ return 0;\n    currentSum = (currentSum << 1) | node->val;\n    if (node->left\
        \ == NULL && node->right == NULL) {\n        return currentSum;\n    }\n   \
        \ return dfs(node->left, currentSum) + dfs(node->right, currentSum);\n}\n\n\
        int sumRootToLeaf(struct TreeNode* root) {\n    return dfs(root, 0);\n}"
      csharp: "/**\n * Definition for a binary tree node.\n * public class TreeNode\
        \ {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode\
        \ right;\n *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)\
        \ {\n *         this.val = val;\n *         this.left = left;\n *         this.right\
        \ = right;\n *     }\n * }\n */\npublic class Solution {\n    public int SumRootToLeaf(TreeNode\
        \ root) {\n        return Dfs(root, 0);\n    }\n\n    private int Dfs(TreeNode\
        \ node, int currentSum) {\n        if (node == null) return 0;\n        currentSum\
        \ = (currentSum << 1) | node.val;\n        if (node.left == null && node.right\
        \ == null) {\n            return currentSum;\n        }\n        return Dfs(node.left,\
        \ currentSum) + Dfs(node.right, currentSum);\n    }\n}"
      javascript: "/**\n * Definition for a binary tree node.\n * function TreeNode(val,\
        \ left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left\
        \ = (left===undefined ? null : left)\n *     this.right = (right===undefined\
        \ ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {number}\n\
        \ */\nvar sumRootToLeaf = function(root) {\n    const dfs = (node, currentSum)\
        \ => {\n        if (!node) return 0;\n        currentSum = (currentSum << 1)\
        \ | node.val;\n        if (!node.left && !node.right) {\n            return\
        \ currentSum;\n        }\n        return dfs(node.left, currentSum) + dfs(node.right,\
        \ currentSum);\n    };\n\n    return dfs(root, 0);\n};"
      typescript: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n\
        \ *     val: number\n *     left: TreeNode | null\n *     right: TreeNode |\
        \ null\n *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode\
        \ | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.left\
        \ = (left===undefined ? null : left)\n *         this.right = (right===undefined\
        \ ? null : right)\n *     }\n * }\n */\n\nfunction sumRootToLeaf(root: TreeNode\
        \ | null): number {\n    const dfs = (node: TreeNode | null, current: number):\
        \ number => {\n        if (!node) return 0;\n        const val = (current <<\
        \ 1) | node.val;\n        if (!node.left && !node.right) {\n            return\
        \ val;\n        }\n        return dfs(node.left, val) + dfs(node.right, val);\n\
        \    };\n    return dfs(root, 0);\n};"
      php: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *    \
        \ public $val = null;\n *     public $left = null;\n *     public $right = null;\n\
        \ *     function __construct($val = 0, $left = null, $right = null) {\n *  \
        \       this.val = $val;\n *         this.left = $left;\n *         this.right\
        \ = $right;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param\
        \ TreeNode $root\n     * @return Integer\n     */\n    function sumRootToLeaf($root)\
        \ {\n        return $this->dfs($root, 0);\n    }\n\n    function dfs($node,\
        \ $current) {\n        if ($node === null) {\n            return 0;\n      \
        \  }\n        $current = ($current << 1) | $node->val;\n        if ($node->left\
        \ === null && $node->right === null) {\n            return $current;\n     \
        \   }\n        return $this->dfs($node->left, $current) + $this->dfs($node->right,\
        \ $current);\n    }\n}"
      swift: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     public var val: Int\n *     public var left: TreeNode?\n *     public\
        \ var right: TreeNode?\n *     public init() { self.val = 0; self.left = nil;\
        \ self.right = nil; }\n *     public init(_ val: Int) { self.val = val; self.left\
        \ = nil; self.right = nil; }\n *     public init(_ val: Int, _ left: TreeNode?,\
        \ _ right: TreeNode?) {\n *         self.val = val\n *         self.left = left\n\
        \ *         self.right = right\n *     }\n * }\n */\nclass Solution {\n    func\
        \ sumRootToLeaf(_ root: TreeNode?) -> Int {\n        return dfs(root, 0)\n \
        \   }\n\n    private func dfs(_ node: TreeNode?, _ current: Int) -> Int {\n\
        \        guard let node = node else { return 0 }\n        let nextVal = (current\
        \ << 1) | node.val\n        if node.left == nil && node.right == nil {\n   \
        \         return nextVal\n        }\n        return dfs(node.left, nextVal)\
        \ + dfs(node.right, nextVal)\n    }\n}"
      kotlin: "/**\n * Example:\n * var ti = TreeNode(5)\n * var v = ti.`val`\n * Definition\
        \ for a binary tree node.\n * class TreeNode(var `val`: Int) {\n *     var left:\
        \ TreeNode? = null\n *     var right: TreeNode? = null\n * }\n */\nclass Solution\
        \ {\n    fun sumRootToLeaf(root: TreeNode?): Int {\n        return dfs(root,\
        \ 0)\n    }\n\n    private fun dfs(node: TreeNode?, current: Int): Int {\n \
        \       if (node == null) return 0\n        val nextVal = (current shl 1) or\
        \ node.`val`\n        if (node.left == null && node.right == null) {\n     \
        \       return nextVal\n        }\n        return dfs(node.left, nextVal) +\
        \ dfs(node.right, nextVal)\n    }\n}"
      dart: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *   int\
        \ val;\n *   TreeNode? left;\n *   TreeNode? right;\n *   TreeNode([this.val\
        \ = 0, this.left, this.right]);\n * }\n */\nclass Solution {\n  int sumRootToLeaf(TreeNode?\
        \ root) {\n    return _dfs(root, 0);\n  }\n\n  int _dfs(TreeNode? node, int\
        \ current) {\n    if (node == null) return 0;\n    int nextVal = (current <<\
        \ 1) | node.val;\n    if (node.left == null && node.right == null) {\n     \
        \ return nextVal;\n    }\n    return _dfs(node.left, nextVal) + _dfs(node.right,\
        \ nextVal);\n  }\n}"
      go: "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *\
        \     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc\
        \ sumRootToLeaf(root *TreeNode) int {\n    return dfs(root, 0)\n}\n\nfunc dfs(node\
        \ *TreeNode, current int) int {\n    if node == nil {\n        return 0\n  \
        \  }\n    current = (current << 1) | node.Val\n    if node.Left == nil && node.Right\
        \ == nil {\n        return current\n    }\n    return dfs(node.Left, current)\
        \ + dfs(node.Right, current)\n}"
      ruby: "def sum_root_to_leaf(root)\n  dfs(root, 0)\nend\n\ndef dfs(node, current_val)\n\
        \  return 0 if node.nil?\n  next_val = (current_val << 1) | node.val\n  return\
        \ next_val if node.left.nil? && node.right.nil?\n  dfs(node.left, next_val)\
        \ + dfs(node.right, next_val)\nend"
      scala: "object Solution {\n    def sumRootToLeaf(root: TreeNode): Int = {\n  \
        \      def dfs(node: TreeNode, currentVal: Int): Int = {\n            if (node\
        \ == null) return 0\n            val nextVal = (currentVal << 1) | node.value\n\
        \            if (node.left == null && node.right == null) return nextVal\n \
        \           dfs(node.left, nextVal) + dfs(node.right, nextVal)\n        }\n\
        \        dfs(root, 0)\n    }\n}"
      rust: "use std::rc::Rc;\nuse std::cell::RefCell;\nimpl Solution {\n    pub fn\
        \ sum_root_to_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {\n        fn\
        \ dfs(node: Option<Rc<RefCell<TreeNode>>>, current_val: i32) -> i32 {\n    \
        \        if let Some(n) = node {\n                let n_borrow = n.borrow();\n\
        \                let next_val = (current_val << 1) | n_borrow.val;\n       \
        \         if n_borrow.left.is_none() && n_borrow.right.is_none() {\n       \
        \             next_val\n                } else {\n                    dfs(n_borrow.left.clone(),\
        \ next_val) + dfs(n_borrow.right.clone(), next_val)\n                }\n   \
        \         } else {\n                0\n            }\n        }\n        dfs(root,\
        \ 0)\n    }\n}"
      racket: "(define/contract (sum-root-to-leaf root)\n  (-> (or/c tree-node? #f)\
        \ exact-integer?)\n  (letrec ([dfs (lambda (node current-val)\n            \
        \      (cond\n                    [(not node) 0]\n                    [(and\
        \ (not (tree-node-left node)) (not (tree-node-right node)))\n              \
        \       (+ (arithmetic-shift current-val 1) (tree-node-val node))]\n       \
        \             [else\n                     (let ([next-val (+ (arithmetic-shift\
        \ current-val 1) (tree-node-val node))])\n                       (+ (dfs (tree-node-left\
        \ node) next-val)\n                          (dfs (tree-node-right node) next-val)))]))])\n\
        \    (dfs root 0)))"
      erlang: "sum_root_to_leaf(Root) ->\n  dfs(Root, 0).\n\ndfs(null, _) ->\n  0;\n\
        dfs(#tree_node{val = Val, left = null, right = null}, CurrentSum) ->\n  (CurrentSum\
        \ bsl 1) bor Val;\ndfs(#tree_node{val = Val, left = Left, right = Right}, CurrentSum)\
        \ ->\n  NextSum = (CurrentSum bsl 1) bor Val,\n  dfs(Left, NextSum) + dfs(Right,\
        \ NextSum)."
      elixir: "defmodule Solution do\n  require Bitwise\n  @spec sum_root_to_leaf(root\
        \ :: TreeNode.t | nil) :: integer\n  def sum_root_to_leaf(root) do\n    dfs(root,\
        \ 0)\n  end\n\n  defp dfs(nil, _), do: 0\n  defp dfs(%TreeNode{val: val, left:\
        \ nil, right: nil}, current_val) do\n    Bitwise.bor(Bitwise.bsl(current_val,\
        \ 1), val)\n  end\n  defp dfs(%TreeNode{val: val, left: left, right: right},\
        \ current_val) do\n    next_val = Bitwise.bor(Bitwise.bsl(current_val, 1), val)\n\
        \    dfs(left, next_val) + dfs(right, next_val)\n  end\nend"
    approach: 'To solve this problem, we use a depth-first search (DFS) approach to
      traverse the binary tree from the root to each leaf node. As we traverse down
      a path, we maintain a running integer that represents the binary number formed
      so far. For each node visited, we update the current value by shifting it left
      by one bit (effectively multiplying by 2) and adding the current node''s value
      (0 or 1). This allows us to build the binary number incrementally from the most
      significant bit to the least significant bit.


      When we reach a leaf node, which is defined as a node with no left or right children,
      the accumulated value represents the full binary number for that specific path.
      We add this value to our total sum. If the node is not a leaf, we recursively
      call the helper function on its children, passing the updated current value. The
      final result is the sum of values collected from all paths that terminate at a
      leaf node.'
    time_complexity: O(N), where N is the number of nodes in the tree. This is because
      the algorithm visits each node exactly once during the depth-first search traversal.
    space_complexity: O(H), where H is the height of the tree. This space is consumed
      by the recursion stack. In the worst case of a skewed tree, H can be N, while
      in a balanced tree, H is log(N).
    elapsed_time: 107.43318557739258
    model: gemini-3-flash-preview
    generated_at: '2026-02-24 01:25:28 '
---

## Problem #1022: Sum of Root To Leaf Binary Numbers

**Difficulty:** Easy

**Topics:** Tree, Depth-First Search, Binary Tree

## Problem Description

<p>You are given the <code>root</code> of a binary tree where each node has a value <code>0</code> or <code>1</code>. Each root-to-leaf path represents a binary number starting with the most significant bit.</p>

<ul>
	<li>For example, if the path is <code>0 -&gt; 1 -&gt; 1 -&gt; 0 -&gt; 1</code>, then this could represent <code>01101</code> in binary, which is <code>13</code>.</li>
</ul>

<p>For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return <em>the sum of these numbers</em>.</p>

<p>The test cases are generated so that the answer fits in a <strong>32-bits</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png" style="width: 400px; height: 263px;" />
<pre>
<strong>Input:</strong> root = [1,0,1,0,1,0,1]
<strong>Output:</strong> 22
<strong>Explanation: </strong>(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [0]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>Node.val</code> is <code>0</code> or <code>1</code>.</li>
</ul>


## Hints

1. Find each path, then transform that path to an integer in base 10.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we use a depth-first search (DFS) approach to traverse the binary tree from the root to each leaf node. As we traverse down a path, we maintain a running integer that represents the binary number formed so far. For each node visited, we update the current value by shifting it left by one bit (effectively multiplying by 2) and adding the current node's value (0 or 1). This allows us to build the binary number incrementally from the most significant bit to the least significant bit.

When we reach a leaf node, which is defined as a node with no left or right children, the accumulated value represents the full binary number for that specific path. We add this value to our total sum. If the node is not a leaf, we recursively call the helper function on its children, passing the updated current value. The final result is the sum of values collected from all paths that terminate at a leaf node.

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
    int calculate(TreeNode* node, int currentSum) {
        if (!node) return 0;
        currentSum = (currentSum << 1) | node->val;
        if (!node->left && !node->right) {
            return currentSum;
        }
        return calculate(node->left, currentSum) + calculate(node->right, currentSum);
    }

    int sumRootToLeaf(TreeNode* root) {
        return calculate(root, 0);
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
    public int sumRootToLeaf(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int currentSum) {
        if (node == null) return 0;
        currentSum = (currentSum << 1) | node.val;
        if (node.left == null && node.right == null) {
            return currentSum;
        }
        return dfs(node.left, currentSum) + dfs(node.right, currentSum);
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
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum = (current_sum << 1) | node.val
            if not node.left and not node.right:
                return current_sum
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)
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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum = (current_sum << 1) | node.val
            if not node.left and not node.right:
                return current_sum
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)
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
int dfs(struct TreeNode* node, int currentSum) {
    if (node == NULL) return 0;
    currentSum = (currentSum << 1) | node->val;
    if (node->left == NULL && node->right == NULL) {
        return currentSum;
    }
    return dfs(node->left, currentSum) + dfs(node->right, currentSum);
}

int sumRootToLeaf(struct TreeNode* root) {
    return dfs(root, 0);
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
    public int SumRootToLeaf(TreeNode root) {
        return Dfs(root, 0);
    }

    private int Dfs(TreeNode node, int currentSum) {
        if (node == null) return 0;
        currentSum = (currentSum << 1) | node.val;
        if (node.left == null && node.right == null) {
            return currentSum;
        }
        return Dfs(node.left, currentSum) + Dfs(node.right, currentSum);
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
 * @return {number}
 */
var sumRootToLeaf = function(root) {
    const dfs = (node, currentSum) => {
        if (!node) return 0;
        currentSum = (currentSum << 1) | node.val;
        if (!node.left && !node.right) {
            return currentSum;
        }
        return dfs(node.left, currentSum) + dfs(node.right, currentSum);
    };

    return dfs(root, 0);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function sumRootToLeaf(root: TreeNode | null): number {
    const dfs = (node: TreeNode | null, current: number): number => {
        if (!node) return 0;
        const val = (current << 1) | node.val;
        if (!node.left && !node.right) {
            return val;
        }
        return dfs(node.left, val) + dfs(node.right, val);
    };
    return dfs(root, 0);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         this.val = $val;
 *         this.left = $left;
 *         this.right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function sumRootToLeaf($root) {
        return $this->dfs($root, 0);
    }

    function dfs($node, $current) {
        if ($node === null) {
            return 0;
        }
        $current = ($current << 1) | $node->val;
        if ($node->left === null && $node->right === null) {
            return $current;
        }
        return $this->dfs($node->left, $current) + $this->dfs($node->right, $current);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func sumRootToLeaf(_ root: TreeNode?) -> Int {
        return dfs(root, 0)
    }

    private func dfs(_ node: TreeNode?, _ current: Int) -> Int {
        guard let node = node else { return 0 }
        let nextVal = (current << 1) | node.val
        if node.left == nil && node.right == nil {
            return nextVal
        }
        return dfs(node.left, nextVal) + dfs(node.right, nextVal)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun sumRootToLeaf(root: TreeNode?): Int {
        return dfs(root, 0)
    }

    private fun dfs(node: TreeNode?, current: Int): Int {
        if (node == null) return 0
        val nextVal = (current shl 1) or node.`val`
        if (node.left == null && node.right == null) {
            return nextVal
        }
        return dfs(node.left, nextVal) + dfs(node.right, nextVal)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class Solution {
  int sumRootToLeaf(TreeNode? root) {
    return _dfs(root, 0);
  }

  int _dfs(TreeNode? node, int current) {
    if (node == null) return 0;
    int nextVal = (current << 1) | node.val;
    if (node.left == null && node.right == null) {
      return nextVal;
    }
    return _dfs(node.left, nextVal) + _dfs(node.right, nextVal);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumRootToLeaf(root *TreeNode) int {
    return dfs(root, 0)
}

func dfs(node *TreeNode, current int) int {
    if node == nil {
        return 0
    }
    current = (current << 1) | node.Val
    if node.Left == nil && node.Right == nil {
        return current
    }
    return dfs(node.Left, current) + dfs(node.Right, current)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def sum_root_to_leaf(root)
  dfs(root, 0)
end

def dfs(node, current_val)
  return 0 if node.nil?
  next_val = (current_val << 1) | node.val
  return next_val if node.left.nil? && node.right.nil?
  dfs(node.left, next_val) + dfs(node.right, next_val)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def sumRootToLeaf(root: TreeNode): Int = {
        def dfs(node: TreeNode, currentVal: Int): Int = {
            if (node == null) return 0
            val nextVal = (currentVal << 1) | node.value
            if (node.left == null && node.right == null) return nextVal
            dfs(node.left, nextVal) + dfs(node.right, nextVal)
        }
        dfs(root, 0)
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
    pub fn sum_root_to_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, current_val: i32) -> i32 {
            if let Some(n) = node {
                let n_borrow = n.borrow();
                let next_val = (current_val << 1) | n_borrow.val;
                if n_borrow.left.is_none() && n_borrow.right.is_none() {
                    next_val
                } else {
                    dfs(n_borrow.left.clone(), next_val) + dfs(n_borrow.right.clone(), next_val)
                }
            } else {
                0
            }
        }
        dfs(root, 0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sum-root-to-leaf root)
  (-> (or/c tree-node? #f) exact-integer?)
  (letrec ([dfs (lambda (node current-val)
                  (cond
                    [(not node) 0]
                    [(and (not (tree-node-left node)) (not (tree-node-right node)))
                     (+ (arithmetic-shift current-val 1) (tree-node-val node))]
                    [else
                     (let ([next-val (+ (arithmetic-shift current-val 1) (tree-node-val node))])
                       (+ (dfs (tree-node-left node) next-val)
                          (dfs (tree-node-right node) next-val)))]))])
    (dfs root 0)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
sum_root_to_leaf(Root) ->
  dfs(Root, 0).

dfs(null, _) ->
  0;
dfs(#tree_node{val = Val, left = null, right = null}, CurrentSum) ->
  (CurrentSum bsl 1) bor Val;
dfs(#tree_node{val = Val, left = Left, right = Right}, CurrentSum) ->
  NextSum = (CurrentSum bsl 1) bor Val,
  dfs(Left, NextSum) + dfs(Right, NextSum).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  require Bitwise
  @spec sum_root_to_leaf(root :: TreeNode.t | nil) :: integer
  def sum_root_to_leaf(root) do
    dfs(root, 0)
  end

  defp dfs(nil, _), do: 0
  defp dfs(%TreeNode{val: val, left: nil, right: nil}, current_val) do
    Bitwise.bor(Bitwise.bsl(current_val, 1), val)
  end
  defp dfs(%TreeNode{val: val, left: left, right: right}, current_val) do
    next_val = Bitwise.bor(Bitwise.bsl(current_val, 1), val)
    dfs(left, next_val) + dfs(right, next_val)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the number of nodes in the tree. This is because the algorithm visits each node exactly once during the depth-first search traversal.
- **Space Complexity:** O(H), where H is the height of the tree. This space is consumed by the recursion stack. In the worst case of a skewed tree, H can be N, while in a balanced tree, H is log(N).
