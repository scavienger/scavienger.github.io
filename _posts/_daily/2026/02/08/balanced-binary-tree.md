---
layout: post
title: "Balanced Binary Tree"
date: 2026-02-08 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Tree", "Depth-First Search", "Binary Tree"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/balanced-binary-tree/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *   \
        \  int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode()\
        \ : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x),\
        \ left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode\
        \ *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution\
        \ {\npublic:\n    int check(TreeNode* node) {\n        if (!node) return 0;\n\
        \        int left = check(node->left);\n        if (left == -1) return -1;\n\
        \        int right = check(node->right);\n        if (right == -1) return -1;\n\
        \        if (left - right > 1 || right - left > 1) return -1;\n        return\
        \ (left > right ? left : right) + 1;\n    }\n\n    bool isBalanced(TreeNode*\
        \ root) {\n        return check(root) != -1;\n    }\n};"
      java: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode()\
        \ {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val,\
        \ TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left\
        \ = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution\
        \ {\n    public boolean isBalanced(TreeNode root) {\n        return check(root)\
        \ != -1;\n    }\n\n    private int check(TreeNode node) {\n        if (node\
        \ == null) return 0;\n        int left = check(node.left);\n        if (left\
        \ == -1) return -1;\n        int right = check(node.right);\n        if (right\
        \ == -1) return -1;\n        if (Math.abs(left - right) > 1) return -1;\n  \
        \      return Math.max(left, right) + 1;\n    }\n}"
      python: "# Definition for a binary tree node.\n# class TreeNode(object):\n#  \
        \   def __init__(self, val=0, left=None, right=None):\n#         self.val =\
        \ val\n#         self.left = left\n#         self.right = right\nclass Solution(object):\n\
        \    def isBalanced(self, root):\n        \"\"\"\n        :type root: Optional[TreeNode]\n\
        \        :rtype: bool\n        \"\"\"\n        def check(node):\n          \
        \  if not node:\n                return 0\n            left = check(node.left)\n\
        \            if left == -1:\n                return -1\n            right =\
        \ check(node.right)\n            if right == -1:\n                return -1\n\
        \            if abs(left - right) > 1:\n                return -1\n        \
        \    return max(left, right) + 1\n\n        return check(root) != -1"
      python3: "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self,\
        \ val=0, left=None, right=None):\n#         self.val = val\n#         self.left\
        \ = left\n#         self.right = right\nclass Solution:\n    def isBalanced(self,\
        \ root: Optional[TreeNode]) -> bool:\n        def check(node):\n           \
        \ if not node:\n                return 0\n            left = check(node.left)\n\
        \            if left == -1:\n                return -1\n            right =\
        \ check(node.right)\n            if right == -1:\n                return -1\n\
        \            if abs(left - right) > 1:\n                return -1\n        \
        \    return max(left, right) + 1\n\n        return check(root) != -1"
      c: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int\
        \ val;\n *     struct TreeNode *left;\n *     struct TreeNode *right;\n * };\n\
        \ */\nint check(struct TreeNode* node) {\n    if (!node) return 0;\n    int\
        \ left = check(node->left);\n    if (left == -1) return -1;\n    int right =\
        \ check(node->right);\n    if (right == -1) return -1;\n    int diff = left\
        \ - right;\n    if (diff < 0) diff = -diff;\n    if (diff > 1) return -1;\n\
        \    return (left > right ? left : right) + 1;\n}\n\nbool isBalanced(struct\
        \ TreeNode* root) {\n    return check(root) != -1;\n}"
      csharp: "/**\n * Definition for a binary tree node.\n * public class TreeNode\
        \ {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode\
        \ right;\n *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)\
        \ {\n *         this.val = val;\n *         this.left = left;\n *         this.right\
        \ = right;\n *     } cyclic reference here is intentional\n * }\n */\npublic\
        \ class Solution {\n    public bool IsBalanced(TreeNode root) {\n        return\
        \ Check(root) != -1;\n    }\n\n    private int Check(TreeNode node) {\n    \
        \    if (node == null) return 0;\n        int left = Check(node.left);\n   \
        \     if (left == -1) return -1;\n        int right = Check(node.right);\n \
        \       if (right == -1) return -1;\n        if (Math.Abs(left - right) > 1)\
        \ return -1;\n        return Math.Max(left, right) + 1;\n    }\n}"
      javascript: "/**\n * Definition for a binary tree node.\n * function TreeNode(val,\
        \ left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left\
        \ = (left===undefined ? null : left)\n *     this.right = (right===undefined\
        \ ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {boolean}\n\
        \ */\nvar isBalanced = function(root) {\n    const check = (node) => {\n   \
        \     if (!node) return 0;\n        let left = check(node.left);\n        if\
        \ (left === -1) return -1;\n        let right = check(node.right);\n       \
        \ if (right === -1) return -1;\n        if (Math.abs(left - right) > 1) return\
        \ -1;\n        return Math.max(left, right) + 1;\n    };\n\n    return check(root)\
        \ !== -1;\n};"
      typescript: "function isBalanced(root: TreeNode | null): boolean {\n    const\
        \ checkHeight = (node: TreeNode | null): number => {\n        if (node === null)\
        \ return 0;\n        const leftHeight = checkHeight(node.left);\n        if\
        \ (leftHeight === -1) return -1;\n        const rightHeight = checkHeight(node.right);\n\
        \        if (rightHeight === -1) return -1;\n        if (Math.abs(leftHeight\
        \ - rightHeight) > 1) return -1;\n        return Math.max(leftHeight, rightHeight)\
        \ + 1;\n    };\n    return checkHeight(root) !== -1;\n};"
      php: "class Solution {\n\n    /**\n     * @param TreeNode $root\n     * @return\
        \ Boolean\n     */\n    function isBalanced($root) {\n        return $this->checkHeight($root)\
        \ !== -1;\n    }\n\n    function checkHeight($node) {\n        if ($node ===\
        \ null) return 0;\n        $left = $this->checkHeight($node->left);\n      \
        \  if ($left === -1) return -1;\n        $right = $this->checkHeight($node->right);\n\
        \        if ($right === -1) return -1;\n        if (abs($left - $right) > 1)\
        \ return -1;\n        return max($left, $right) + 1;\n    }\n}"
      swift: "class Solution {\n    func isBalanced(_ root: TreeNode?) -> Bool {\n \
        \       return checkHeight(root) != -1\n    }\n\n    private func checkHeight(_\
        \ node: TreeNode?) -> Int {\n        guard let node = node else { return 0 }\n\
        \        let left = checkHeight(node.left)\n        if left == -1 { return -1\
        \ }\n        let right = checkHeight(node.right)\n        if right == -1 { return\
        \ -1 }\n        if abs(left - right) > 1 { return -1 }\n        return max(left,\
        \ right) + 1\n    }\n}"
      kotlin: "class Solution {\n    fun isBalanced(root: TreeNode?): Boolean {\n  \
        \      return checkHeight(root) != -1\n    }\n\n    private fun checkHeight(node:\
        \ TreeNode?): Int {\n        if (node == null) return 0\n        val left =\
        \ checkHeight(node.left)\n        if (left == -1) return -1\n        val right\
        \ = checkHeight(node.right)\n        if (right == -1) return -1\n        val\
        \ diff = if (left > right) left - right else right - left\n        if (diff\
        \ > 1) return -1\n        return (if (left > right) left else right) + 1\n \
        \   }\n}"
      dart: "class Solution {\n  bool isBalanced(TreeNode? root) {\n    return _checkHeight(root)\
        \ != -1;\n  }\n\n  int _checkHeight(TreeNode? node) {\n    if (node == null)\
        \ return 0;\n    int left = _checkHeight(node.left);\n    if (left == -1) return\
        \ -1;\n    int right = _checkHeight(node.right);\n    if (right == -1) return\
        \ -1;\n    int diff = (left - right).abs();\n    if (diff > 1) return -1;\n\
        \    return (left > right ? left : right) + 1;\n  }\n}"
      go: "func isBalanced(root *TreeNode) bool {\n    return checkHeight(root) != -1\n\
        }\n\nfunc checkHeight(node *TreeNode) int {\n    if node == nil {\n        return\
        \ 0\n    }\n    left := checkHeight(node.Left)\n    if left == -1 {\n      \
        \  return -1\n    }\n    right := checkHeight(node.Right)\n    if right == -1\
        \ {\n        return -1\n    }\n    diff := left - right\n    if diff < 0 {\n\
        \        diff = -diff\n    }\n    if diff > 1 {\n        return -1\n    }\n\
        \    if left > right {\n        return left + 1\n    }\n    return right + 1\n\
        }"
      ruby: "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor\
        \ :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n\
        #         @val = val\n#         @left = left\n#         @right = right\n#  \
        \   end\n# end\n# @param {TreeNode} root\n# @return {Boolean}\ndef is_balanced(root)\n\
        \  check_height(root) != -1\nend\n\ndef check_height(node)\n  return 0 if node.nil?\n\
        \n  left_height = check_height(node.left)\n  return -1 if left_height == -1\n\
        \n  right_height = check_height(node.right)\n  return -1 if right_height ==\
        \ -1\n\n  return -1 if (left_height - right_height).abs > 1\n\n  [left_height,\
        \ right_height].max + 1\nend"
      scala: "/**\n * Definition for a binary tree node.\n * class TreeNode(_value:\
        \ Int = 0, _left: TreeNode = null, _right: TreeNode = null) {\n *   var value:\
        \ Int = _value\n *   var left: TreeNode = _left\n *   var right: TreeNode =\
        \ _right\n * }\n */\nobject Solution {\n    def isBalanced(root: TreeNode):\
        \ Boolean = {\n        def checkHeight(node: TreeNode): Int = {\n          \
        \  if (node == null) return 0\n            val left = checkHeight(node.left)\n\
        \            if (left == -1) return -1\n            val right = checkHeight(node.right)\n\
        \            if (right == -1) return -1\n            if (Math.abs(left - right)\
        \ > 1) return -1\n            Math.max(left, right) + 1\n        }\n       \
        \ checkHeight(root) != -1\n    }\n}"
      rust: "use std::rc::Rc;\nuse std::cell::RefCell;\n\nimpl Solution {\n    pub fn\
        \ is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {\n        fn check_height(node:\
        \ &Option<Rc<RefCell<TreeNode>>>) -> i32 {\n            match node {\n     \
        \           None => 0,\n                Some(node_ref) => {\n              \
        \      let n = node_ref.borrow();\n                    let left = check_height(&n.left);\n\
        \                    if left == -1 { return -1; }\n                    let right\
        \ = check_height(&n.right);\n                    if right == -1 { return -1;\
        \ }\n                    if (left - right).abs() > 1 { return -1; }\n      \
        \              std::cmp::max(left, right) + 1\n                }\n         \
        \   }\n        }\n        check_height(&root) != -1\n    }\n}"
      racket: "(define/contract (is-balanced root)\n  (-> (or/c tree-node? #f) boolean?)\n\
        \  (define (check-height node)\n    (cond\n      [(not node) 0]\n      [else\n\
        \       (let ([left (check-height (tree-node-left node))])\n         (if (=\
        \ left -1)\n             -1\n             (let ([right (check-height (tree-node-right\
        \ node))])\n               (if (or (= right -1) (> (abs (- left right)) 1))\n\
        \                   -1\n                   (+ 1 (max left right))))))]))\n \
        \ (not (= (check-height root) -1)))"
      erlang: "%% Definition for a binary tree node.\n%%\n%% -record(tree_node, {val\
        \ = 0 :: integer(),\n%%                     left = null  :: 'null' | #tree_node{},\n\
        %%                     right = null :: 'null' | #tree_node{}}).\n\n-spec is_balanced(Root\
        \ :: #tree_node{} | null) -> boolean().\nis_balanced(Root) ->\n  check_height(Root)\
        \ =/= -1.\n\ncheck_height(null) -> 0;\ncheck_height(#tree_node{left = Left,\
        \ right = Right}) ->\n  LHeight = check_height(Left),\n  if LHeight =:= -1 ->\
        \ -1;\n     true ->\n       RHeight = check_height(Right),\n       if RHeight\
        \ =:= -1 -> -1;\n          true ->\n            Diff = abs(LHeight - RHeight),\n\
        \            if Diff > 1 -> -1;\n               true -> 1 + max(LHeight, RHeight)\n\
        \            end\n       end\n  end."
      elixir: "# Definition for a binary tree node.\n#\n# defmodule TreeNode do\n# \
        \  @type t :: %__MODULE__{\n#           val: integer,\n#           left: TreeNode.t()\
        \ | nil,\n#           right: TreeNode.t() | nil\n#         }\n#   defstruct\
        \ val: 0, left: nil, right: nil\n# end\n\ndefmodule Solution do\n  @spec is_balanced(root\
        \ :: TreeNode.t | nil) :: boolean\n  def is_balanced(root) do\n    check_height(root)\
        \ != -1\n  end\n\n  defp check_height(nil), do: 0\n  defp check_height(node)\
        \ do\n    left = check_height(node.left)\n    if left == -1 do\n      -1\n \
        \   else\n      right = check_height(node.right)\n      if right == -1 or abs(left\
        \ - right) > 1 do\n        -1\n      else\n        1 + max(left, right)\n  \
        \    end\n    end\n  end\nend"
    approach: 'The height-balanced property is verified using a bottom-up recursion
      strategy. By performing a post-order traversal, the algorithm calculates the height
      of the left and right subtrees for every node. If any subtree is found to be unbalanced,
      or if the height difference between the left and right subtrees exceeds one, a
      sentinel value of -1 is returned to signal the imbalance up the recursion stack.


      This approach is more efficient than a top-down approach because it avoids redundant
      height calculations for the same nodes. Instead of calling a separate height function
      for every node in the tree (which would result in $O(N^2)$ time), this method
      checks the balance condition in a single pass. If the entire tree is balanced,
      the root returns its actual height; otherwise, it returns -1.'
    time_complexity: O(N), where N is the number of nodes in the binary tree. The algorithm
      performs a single post-order traversal, visiting each node exactly once and performing
      constant-time work at each step.
    space_complexity: O(H), where H is the height of the tree. This corresponds to the
      maximum depth of the recursion stack. In the worst case of a skewed tree, H equals
      N, while in a balanced tree, H is log N.
    elapsed_time: 61.851557970047
    model: gemini-3-flash-preview
    generated_at: '2026-02-08 01:57:39 '
---

## Problem #110: Balanced Binary Tree

**Difficulty:** Easy

**Topics:** Tree, Depth-First Search, Binary Tree

## Problem Description

<p>Given a binary tree, determine if it is <span data-keyword="height-balanced"><strong>height-balanced</strong></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [1,2,2,3,3,null,null,4,4]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The height-balanced property is verified using a bottom-up recursion strategy. By performing a post-order traversal, the algorithm calculates the height of the left and right subtrees for every node. If any subtree is found to be unbalanced, or if the height difference between the left and right subtrees exceeds one, a sentinel value of -1 is returned to signal the imbalance up the recursion stack.

This approach is more efficient than a top-down approach because it avoids redundant height calculations for the same nodes. Instead of calling a separate height function for every node in the tree (which would result in $O(N^2)$ time), this method checks the balance condition in a single pass. If the entire tree is balanced, the root returns its actual height; otherwise, it returns -1.

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
    int check(TreeNode* node) {
        if (!node) return 0;
        int left = check(node->left);
        if (left == -1) return -1;
        int right = check(node->right);
        if (right == -1) return -1;
        if (left - right > 1 || right - left > 1) return -1;
        return (left > right ? left : right) + 1;
    }

    bool isBalanced(TreeNode* root) {
        return check(root) != -1;
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
    public boolean isBalanced(TreeNode root) {
        return check(root) != -1;
    }

    private int check(TreeNode node) {
        if (node == null) return 0;
        int left = check(node.left);
        if (left == -1) return -1;
        int right = check(node.right);
        if (right == -1) return -1;
        if (Math.abs(left - right) > 1) return -1;
        return Math.max(left, right) + 1;
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
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1
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
int check(struct TreeNode* node) {
    if (!node) return 0;
    int left = check(node->left);
    if (left == -1) return -1;
    int right = check(node->right);
    if (right == -1) return -1;
    int diff = left - right;
    if (diff < 0) diff = -diff;
    if (diff > 1) return -1;
    return (left > right ? left : right) + 1;
}

bool isBalanced(struct TreeNode* root) {
    return check(root) != -1;
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
 *     } cyclic reference here is intentional
 * }
 */
public class Solution {
    public bool IsBalanced(TreeNode root) {
        return Check(root) != -1;
    }

    private int Check(TreeNode node) {
        if (node == null) return 0;
        int left = Check(node.left);
        if (left == -1) return -1;
        int right = Check(node.right);
        if (right == -1) return -1;
        if (Math.Abs(left - right) > 1) return -1;
        return Math.Max(left, right) + 1;
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
 * @return {boolean}
 */
var isBalanced = function(root) {
    const check = (node) => {
        if (!node) return 0;
        let left = check(node.left);
        if (left === -1) return -1;
        let right = check(node.right);
        if (right === -1) return -1;
        if (Math.abs(left - right) > 1) return -1;
        return Math.max(left, right) + 1;
    };

    return check(root) !== -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function isBalanced(root: TreeNode | null): boolean {
    const checkHeight = (node: TreeNode | null): number => {
        if (node === null) return 0;
        const leftHeight = checkHeight(node.left);
        if (leftHeight === -1) return -1;
        const rightHeight = checkHeight(node.right);
        if (rightHeight === -1) return -1;
        if (Math.abs(leftHeight - rightHeight) > 1) return -1;
        return Math.max(leftHeight, rightHeight) + 1;
    };
    return checkHeight(root) !== -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param TreeNode $root
     * @return Boolean
     */
    function isBalanced($root) {
        return $this->checkHeight($root) !== -1;
    }

    function checkHeight($node) {
        if ($node === null) return 0;
        $left = $this->checkHeight($node->left);
        if ($left === -1) return -1;
        $right = $this->checkHeight($node->right);
        if ($right === -1) return -1;
        if (abs($left - $right) > 1) return -1;
        return max($left, $right) + 1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func isBalanced(_ root: TreeNode?) -> Bool {
        return checkHeight(root) != -1
    }

    private func checkHeight(_ node: TreeNode?) -> Int {
        guard let node = node else { return 0 }
        let left = checkHeight(node.left)
        if left == -1 { return -1 }
        let right = checkHeight(node.right)
        if right == -1 { return -1 }
        if abs(left - right) > 1 { return -1 }
        return max(left, right) + 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun isBalanced(root: TreeNode?): Boolean {
        return checkHeight(root) != -1
    }

    private fun checkHeight(node: TreeNode?): Int {
        if (node == null) return 0
        val left = checkHeight(node.left)
        if (left == -1) return -1
        val right = checkHeight(node.right)
        if (right == -1) return -1
        val diff = if (left > right) left - right else right - left
        if (diff > 1) return -1
        return (if (left > right) left else right) + 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool isBalanced(TreeNode? root) {
    return _checkHeight(root) != -1;
  }

  int _checkHeight(TreeNode? node) {
    if (node == null) return 0;
    int left = _checkHeight(node.left);
    if (left == -1) return -1;
    int right = _checkHeight(node.right);
    if (right == -1) return -1;
    int diff = (left - right).abs();
    if (diff > 1) return -1;
    return (left > right ? left : right) + 1;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func isBalanced(root *TreeNode) bool {
    return checkHeight(root) != -1
}

func checkHeight(node *TreeNode) int {
    if node == nil {
        return 0
    }
    left := checkHeight(node.Left)
    if left == -1 {
        return -1
    }
    right := checkHeight(node.Right)
    if right == -1 {
        return -1
    }
    diff := left - right
    if diff < 0 {
        diff = -diff
    }
    if diff > 1 {
        return -1
    }
    if left > right {
        return left + 1
    }
    return right + 1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Boolean}
def is_balanced(root)
  check_height(root) != -1
end

def check_height(node)
  return 0 if node.nil?

  left_height = check_height(node.left)
  return -1 if left_height == -1

  right_height = check_height(node.right)
  return -1 if right_height == -1

  return -1 if (left_height - right_height).abs > 1

  [left_height, right_height].max + 1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def isBalanced(root: TreeNode): Boolean = {
        def checkHeight(node: TreeNode): Int = {
            if (node == null) return 0
            val left = checkHeight(node.left)
            if (left == -1) return -1
            val right = checkHeight(node.right)
            if (right == -1) return -1
            if (Math.abs(left - right) > 1) return -1
            Math.max(left, right) + 1
        }
        checkHeight(root) != -1
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
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn check_height(node: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
            match node {
                None => 0,
                Some(node_ref) => {
                    let n = node_ref.borrow();
                    let left = check_height(&n.left);
                    if left == -1 { return -1; }
                    let right = check_height(&n.right);
                    if right == -1 { return -1; }
                    if (left - right).abs() > 1 { return -1; }
                    std::cmp::max(left, right) + 1
                }
            }
        }
        check_height(&root) != -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (is-balanced root)
  (-> (or/c tree-node? #f) boolean?)
  (define (check-height node)
    (cond
      [(not node) 0]
      [else
       (let ([left (check-height (tree-node-left node))])
         (if (= left -1)
             -1
             (let ([right (check-height (tree-node-right node))])
               (if (or (= right -1) (> (abs (- left right)) 1))
                   -1
                   (+ 1 (max left right))))))]))
  (not (= (check-height root) -1)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec is_balanced(Root :: #tree_node{} | null) -> boolean().
is_balanced(Root) ->
  check_height(Root) =/= -1.

check_height(null) -> 0;
check_height(#tree_node{left = Left, right = Right}) ->
  LHeight = check_height(Left),
  if LHeight =:= -1 -> -1;
     true ->
       RHeight = check_height(Right),
       if RHeight =:= -1 -> -1;
          true ->
            Diff = abs(LHeight - RHeight),
            if Diff > 1 -> -1;
               true -> 1 + max(LHeight, RHeight)
            end
       end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec is_balanced(root :: TreeNode.t | nil) :: boolean
  def is_balanced(root) do
    check_height(root) != -1
  end

  defp check_height(nil), do: 0
  defp check_height(node) do
    left = check_height(node.left)
    if left == -1 do
      -1
    else
      right = check_height(node.right)
      if right == -1 or abs(left - right) > 1 do
        -1
      else
        1 + max(left, right)
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the number of nodes in the binary tree. The algorithm performs a single post-order traversal, visiting each node exactly once and performing constant-time work at each step.
- **Space Complexity:** O(H), where H is the height of the tree. This corresponds to the maximum depth of the recursion stack. In the worst case of a skewed tree, H equals N, while in a balanced tree, H is log N.
