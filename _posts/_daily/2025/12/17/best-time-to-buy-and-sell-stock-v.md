---
layout: post
title: "Best Time to Buy and Sell Stock V"
date: 2025-12-17 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maximumProfit(vector<int>& prices,\
        \ int k) {\n        int n = prices.size();\n\n        // dp[t][0]: max profit\
        \ with t transactions completed, no open position\n        // dp[t][1]: max\
        \ profit with t-1 transactions completed, currently holding a long position\
        \ (will be t-th transaction)\n        // dp[t][2]: max profit with t-1 transactions\
        \ completed, currently holding a short position (will be t-th transaction)\n\
        \n        vector<vector<long long>> dp(k + 1, vector<long long>(3));\n\n   \
        \     for (int t = 0; t <= k; ++t) {\n            dp[t][0] = 0; // 0 profit\
        \ with 0 transactions completed and no open position\n            dp[t][1] =\
        \ LLONG_MIN / 2; // Use LLONG_MIN / 2 to prevent overflow when adding/subtracting\
        \ prices\n            dp[t][2] = LLONG_MIN / 2; // Use LLONG_MIN / 2 to prevent\
        \ overflow when adding/subtracting prices\n        }\n\n        for (int price\
        \ : prices) {\n            for (int t = k; t >= 1; --t) {\n                //\
        \ State 0: No open position\n                // Option 1: Do nothing (carry\
        \ over from previous day's dp[t][0])\n                // Option 2: Sell a long\
        \ position (dp[t][1] + price). This completes the t-th transaction.\n      \
        \          // Option 3: Buy back a short position (dp[t][2] - price). This completes\
        \ the t-th transaction.\n                dp[t][0] = max({dp[t][0], dp[t][1]\
        \ + price, dp[t][2] - price});\n\n                // State 1: Holding a long\
        \ position\n                // Option 1: Do nothing (carry over from previous\
        \ day's dp[t][1])\n                // Option 2: Buy a stock (dp[t-1][0] - price).\
        \ This starts the t-th transaction.\n                dp[t][1] = max(dp[t][1],\
        \ dp[t-1][0] - price);\n\n                // State 2: Holding a short position\n\
        \                // Option 1: Do nothing (carry over from previous day's dp[t][2])\n\
        \                // Option 2: Short sell a stock (dp[t-1][0] + price). This\
        \ starts the t-th transaction.\n                dp[t][2] = max(dp[t][2], dp[t-1][0]\
        \ + price);\n            }\n        }\n\n        long long max_profit = 0;\n\
        \        for (int t = 0; t <= k; ++t) {\n            max_profit = max(max_profit,\
        \ dp[t][0]);\n        }\n\n        return max_profit;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public long maximumProfit(int[]\
        \ prices, int k) {\n        int n = prices.length;\n\n        // dp[t][0]: max\
        \ profit with t transactions completed, no open position\n        // dp[t][1]:\
        \ max profit with t-1 transactions completed, currently holding a long position\
        \ (will be t-th transaction)\n        // dp[t][2]: max profit with t-1 transactions\
        \ completed, currently holding a short position (will be t-th transaction)\n\
        \n        long[][] dp = new long[k + 1][3];\n\n        for (int t = 0; t <=\
        \ k; ++t) {\n            dp[t][0] = 0; // 0 profit with 0 transactions completed\
        \ and no open position\n            dp[t][1] = Long.MIN_VALUE / 2; // Use Long.MIN_VALUE\
        \ / 2 to prevent overflow when adding/subtracting prices\n            dp[t][2]\
        \ = Long.MIN_VALUE / 2; // Use Long.MIN_VALUE / 2 to prevent overflow when adding/subtracting\
        \ prices\n        }\n\n        for (int price : prices) {\n            for (int\
        \ t = k; t >= 1; --t) {\n                // State 0: No open position\n    \
        \            // Option 1: Do nothing (carry over from previous day's dp[t][0])\n\
        \                // Option 2: Sell a long position (dp[t][1] + price). This\
        \ completes the t-th transaction.\n                // Option 3: Buy back a short\
        \ position (dp[t][2] - price). This completes the t-th transaction.\n      \
        \          dp[t][0] = Math.max(dp[t][0], Math.max(dp[t][1] + price, dp[t][2]\
        \ - price));\n\n                // State 1: Holding a long position\n      \
        \          // Option 1: Do nothing (carry over from previous day's dp[t][1])\n\
        \                // Option 2: Buy a stock (dp[t-1][0] - price). This starts\
        \ the t-th transaction.\n                dp[t][1] = Math.max(dp[t][1], dp[t-1][0]\
        \ - price);\n\n                // State 2: Holding a short position\n      \
        \          // Option 1: Do nothing (carry over from previous day's dp[t][2])\n\
        \                // Option 2: Short sell a stock (dp[t-1][0] + price). This\
        \ starts the t-th transaction.\n                dp[t][2] = Math.max(dp[t][2],\
        \ dp[t-1][0] + price);\n            }\n        }\n\n        long maxProfit =\
        \ 0;\n        for (int t = 0; t <= k; ++t) {\n            maxProfit = Math.max(maxProfit,\
        \ dp[t][0]);\n        }\n\n        return maxProfit;\n    }\n}"
      python: "import math\n\nclass Solution:\n    def maximumProfit(self, prices: List[int],\
        \ k: int) -> int:\n        n = len(prices)\n\n        # dp[t][0]: max profit\
        \ with t transactions completed, no open position\n        # dp[t][1]: max profit\
        \ with t-1 transactions completed, currently holding a long position (will be\
        \ t-th transaction)\n        # dp[t][2]: max profit with t-1 transactions completed,\
        \ currently holding a short position (will be t-th transaction)\n\n        dp\
        \ = [[0] * 3 for _ in range(k + 1)]\n\n        for t in range(k + 1):\n    \
        \        dp[t][1] = -math.inf\n            dp[t][2] = -math.inf\n\n        #\
        \ Iterate through each price\n        for price in prices:\n            # Iterate\
        \ transactions from k down to 1\n            # This order ensures that dp[t-1][0]\
        \ refers to the value from the previous day\n            # (or previous iteration\
        \ of the outer loop)\n            for t in range(k, 0, -1):\n              \
        \  # State 0: No open position\n                # Option 1: Do nothing (carry\
        \ over from previous day's dp[t][0])\n                # Option 2: Sell a long\
        \ position (dp[t][1] + price). This completes the t-th transaction.\n      \
        \          # Option 3: Buy back a short position (dp[t][2] - price). This completes\
        \ the t-th transaction.\n                dp[t][0] = max(dp[t][0], dp[t][1] +\
        \ price, dp[t][2] - price)\n\n                # State 1: Holding a long position\n\
        \                # Option 1: Do nothing (carry over from previous day's dp[t][1])\n\
        \                # Option 2: Buy a stock (dp[t-1][0] - price). This starts the\
        \ t-th transaction.\n                dp[t][1] = max(dp[t][1], dp[t-1][0] - price)\n\
        \n                # State 2: Holding a short position\n                # Option\
        \ 1: Do nothing (carry over from previous day's dp[t][2])\n                #\
        \ Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.\n\
        \                dp[t][2] = max(dp[t][2], dp[t-1][0] + price)\n\n        # The\
        \ maximum profit is the maximum value in dp[t][0] for all t from 0 to k.\n \
        \       # dp[0][0] is always 0, representing no transactions and no profit.\n\
        \        # If all transactions result in losses, the max profit could be 0.\n\
        \        max_profit = 0\n        for t in range(k + 1):\n            max_profit\
        \ = max(max_profit, dp[t][0])\n\n        return max_profit"
      python3: "import math\n\nclass Solution:\n    def maximumProfit(self, prices:\
        \ List[int], k: int) -> int:\n        n = len(prices)\n\n        # dp[t][0]:\
        \ max profit with t transactions completed, no open position\n        # dp[t][1]:\
        \ max profit with t-1 transactions completed, currently holding a long position\
        \ (will be t-th transaction)\n        # dp[t][2]: max profit with t-1 transactions\
        \ completed, currently holding a short position (will be t-th transaction)\n\
        \n        dp = [[0] * 3 for _ in range(k + 1)]\n\n        for t in range(k +\
        \ 1):\n            dp[t][1] = -math.inf\n            dp[t][2] = -math.inf\n\n\
        \        # Iterate through each price\n        for price in prices:\n      \
        \      # Iterate transactions from k down to 1\n            # This order ensures\
        \ that dp[t-1][0] refers to the value from the previous day\n            # (or\
        \ previous iteration of the outer loop)\n            for t in range(k, 0, -1):\n\
        \                # State 0: No open position\n                # Option 1: Do\
        \ nothing (carry over from previous day's dp[t][0])\n                # Option\
        \ 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.\n\
        \                # Option 3: Buy back a short position (dp[t][2] - price). This\
        \ completes the t-th transaction.\n                dp[t][0] = max(dp[t][0],\
        \ dp[t][1] + price, dp[t][2] - price)\n\n                # State 1: Holding\
        \ a long position\n                # Option 1: Do nothing (carry over from previous\
        \ day's dp[t][1])\n                # Option 2: Buy a stock (dp[t-1][0] - price).\
        \ This starts the t-th transaction.\n                dp[t][1] = max(dp[t][1],\
        \ dp[t-1][0] - price)\n\n                # State 2: Holding a short position\n\
        \                # Option 1: Do nothing (carry over from previous day's dp[t][2])\n\
        \                # Option 2: Short sell a stock (dp[t-1][0] + price). This starts\
        \ the t-th transaction.\n                dp[t][2] = max(dp[t][2], dp[t-1][0]\
        \ + price)\n\n        # The maximum profit is the maximum value in dp[t][0]\
        \ for all t from 0 to k.\n        # dp[0][0] is always 0, representing no transactions\
        \ and no profit.\n        # If all transactions result in losses, the max profit\
        \ could be 0.\n        max_profit = 0\n        for t in range(k + 1):\n    \
        \        max_profit = max(max_profit, dp[t][0])\n\n        return max_profit"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <limits.h>\n\n// Helper\
        \ function for max of three long long values\nlong long max3(long long a, long\
        \ long b, long long c) {\n    long long res = a;\n    if (b > res) res = b;\n\
        \    if (c > res) res = c;\n    return res;\n}\n\n// Helper function for max\
        \ of two long long values\nlong long max2(long long a, long long b) {\n    return\
        \ a > b ? a : b;\n}\n\nlong long maximumProfit(int* prices, int pricesSize,\
        \ int k) {\n    // dp[t][0]: max profit with t transactions completed, no open\
        \ position\n    // dp[t][1]: max profit with t-1 transactions completed, currently\
        \ holding a long position (will be t-th transaction)\n    // dp[t][2]: max profit\
        \ with t-1 transactions completed, currently holding a short position (will\
        \ be t-th transaction)\n\n    long long** dp = (long long**)malloc((k + 1) *\
        \ sizeof(long long*));\n    for (int t = 0; t <= k; ++t) {\n        dp[t] =\
        \ (long long*)malloc(3 * sizeof(long long));\n        dp[t][0] = 0; // 0 profit\
        \ with 0 transactions completed and no open position\n        dp[t][1] = LLONG_MIN\
        \ / 2; // Use LLONG_MIN / 2 to prevent overflow when adding/subtracting prices\n\
        \        dp[t][2] = LLONG_MIN / 2; // Use LLONG_MIN / 2 to prevent overflow\
        \ when adding/subtracting prices\n    }\n\n    for (int i = 0; i < pricesSize;\
        \ ++i) {\n        int price = prices[i];\n        for (int t = k; t >= 1; --t)\
        \ {\n            // State 0: No open position\n            // Option 1: Do nothing\
        \ (carry over from previous day's dp[t][0])\n            // Option 2: Sell a\
        \ long position (dp[t][1] + price). This completes the t-th transaction.\n \
        \           // Option 3: Buy back a short position (dp[t][2] - price). This\
        \ completes the t-th transaction.\n            dp[t][0] = max3(dp[t][0], dp[t][1]\
        \ + price, dp[t][2] - price);\n\n            // State 1: Holding a long position\n\
        \            // Option 1: Do nothing (carry over from previous day's dp[t][1])\n\
        \            // Option 2: Buy a stock (dp[t-1][0] - price). This starts the\
        \ t-th transaction.\n            dp[t][1] = max2(dp[t][1], dp[t-1][0] - price);\n\
        \n            // State 2: Holding a short position\n            // Option 1:\
        \ Do nothing (carry over from previous day's dp[t][2])\n            // Option\
        \ 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.\n\
        \            dp[t][2] = max2(dp[t][2], dp[t-1][0] + price);\n        }\n   \
        \ }\n\n    long long max_profit = 0;\n    for (int t = 0; t <= k; ++t) {\n \
        \       max_profit = max2(max_profit, dp[t][0]);\n    }\n\n    // Free allocated\
        \ memory\n    for (int t = 0; t <= k; ++t) {\n        free(dp[t]);\n    }\n\
        \    free(dp);\n\n    return max_profit;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public long MaximumProfit(int[]\
        \ prices, int k) {\n        int n = prices.Length;\n\n        // dp[t][0]: max\
        \ profit with t transactions completed, no open position\n        // dp[t][1]:\
        \ max profit with t-1 transactions completed, currently holding a long position\
        \ (will be t-th transaction)\n        // dp[t][2]: max profit with t-1 transactions\
        \ completed, currently holding a short position (will be t-th transaction)\n\
        \n        long[][] dp = new long[k + 1][3];\n\n        for (int t = 0; t <=\
        \ k; ++t) {\n            dp[t][0] = 0; // 0 profit with 0 transactions completed\
        \ and no open position\n            dp[t][1] = long.MinValue / 2; // Use long.MinValue\
        \ / 2 to prevent overflow when adding/subtracting prices\n            dp[t][2]\
        \ = long.MinValue / 2; // Use long.MinValue / 2 to prevent overflow when adding/subtracting\
        \ prices\n        }\n\n        foreach (int price in prices) {\n           \
        \ for (int t = k; t >= 1; --t) {\n                // State 0: No open position\n\
        \                // Option 1: Do nothing (carry over from previous day's dp[t][0])\n\
        \                // Option 2: Sell a long position (dp[t][1] + price). This\
        \ completes the t-th transaction.\n                // Option 3: Buy back a short\
        \ position (dp[t][2] - price). This completes the t-th transaction.\n      \
        \          dp[t][0] = Math.Max(dp[t][0], Math.Max(dp[t][1] + price, dp[t][2]\
        \ - price));\n\n                // State 1: Holding a long position\n      \
        \          // Option 1: Do nothing (carry over from previous day's dp[t][1])\n\
        \                // Option 2: Buy a stock (dp[t-1][0] - price). This starts\
        \ the t-th transaction.\n                dp[t][1] = Math.Max(dp[t][1], dp[t-1][0]\
        \ - price);\n\n                // State 2: Holding a short position\n      \
        \          // Option 1: Do nothing (carry over from previous day's dp[t][2])\n\
        \                // Option 2: Short sell a stock (dp[t-1][0] + price). This\
        \ starts the t-th transaction.\n                dp[t][2] = Math.Max(dp[t][2],\
        \ dp[t-1][0] + price);\n            }\n        }\n\n        long maxProfit =\
        \ 0;\n        for (int t = 0; t <= k; ++t) {\n            maxProfit = Math.Max(maxProfit,\
        \ dp[t][0]);\n        }\n\n        return maxProfit;\n    }\n}"
      javascript: "/**\n * @param {number[]} prices\n * @param {number} k\n * @return\
        \ {number}\n */\nvar maximumProfit = function(prices, k) {\n    const n = prices.length;\n\
        \n    // dp[t][0]: max profit with t transactions completed, no open position\n\
        \    // dp[t][1]: max profit with t-1 transactions completed, currently holding\
        \ a long position (will be t-th transaction)\n    // dp[t][2]: max profit with\
        \ t-1 transactions completed, currently holding a short position (will be t-th\
        \ transaction)\n\n    const dp = Array(k + 1).fill(0).map(() => Array(3).fill(0));\n\
        \n    for (let t = 0; t <= k; ++t) {\n        dp[t][0] = 0; // 0 profit with\
        \ 0 transactions completed and no open position\n        dp[t][1] = -Infinity;\
        \ // Cannot hold stock without buying\n        dp[t][2] = -Infinity; // Cannot\
        \ hold short without selling\n    }\n\n    for (const price of prices) {\n \
        \       for (let t = k; t >= 1; --t) {\n            // State 0: No open position\n\
        \            // Option 1: Do nothing (carry over from previous day's dp[t][0])\n\
        \            // Option 2: Sell a long position (dp[t][1] + price). This completes\
        \ the t-th transaction.\n            // Option 3: Buy back a short position\
        \ (dp[t][2] - price). This completes the t-th transaction.\n            dp[t][0]\
        \ = Math.max(dp[t][0], dp[t][1] + price, dp[t][2] - price);\n\n            //\
        \ State 1: Holding a long position\n            // Option 1: Do nothing (carry\
        \ over from previous day's dp[t][1])\n            // Option 2: Buy a stock (dp[t-1][0]\
        \ - price). This starts the t-th transaction.\n            dp[t][1] = Math.max(dp[t][1],\
        \ dp[t-1][0] - price);\n\n            // State 2: Holding a short position\n\
        \            // Option 1: Do nothing (carry over from previous day's dp[t][2])\n\
        \            // Option 2: Short sell a stock (dp[t-1][0] + price). This starts\
        \ the t-th transaction.\n            dp[t][2] = Math.max(dp[t][2], dp[t-1][0]\
        \ + price);\n        }\n    }\n\n    let maxProfit = 0;\n    for (let t = 0;\
        \ t <= k; ++t) {\n        maxProfit = Math.max(maxProfit, dp[t][0]);\n    }\n\
        \n    return maxProfit;\n};"
      typescript: "function maximumProfit(prices: number[], k: number): number {\n \
        \   const n = prices.length;\n\n    // dp[t][0]: max profit with t transactions\
        \ completed, no open position\n    // dp[t][1]: max profit with t-1 transactions\
        \ completed, currently holding a long position (will be t-th transaction)\n\
        \    // dp[t][2]: max profit with t-1 transactions completed, currently holding\
        \ a short position (will be t-th transaction)\n\n    const dp: number[][] =\
        \ Array(k + 1).fill(0).map(() => Array(3).fill(0));\n\n    for (let t = 0; t\
        \ <= k; ++t) {\n        dp[t][0] = 0; // 0 profit with 0 transactions completed\
        \ and no open position\n        dp[t][1] = -Infinity; // Cannot hold stock without\
        \ buying\n        dp[t][2] = -Infinity; // Cannot hold short without selling\n\
        \    }\n\n    for (const price of prices) {\n        for (let t = k; t >= 1;\
        \ --t) {\n            // State 0: No open position\n            // Option 1:\
        \ Do nothing (carry over from previous day's dp[t][0])\n            // Option\
        \ 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.\n\
        \            // Option 3: Buy back a short position (dp[t][2] - price). This\
        \ completes the t-th transaction.\n            dp[t][0] = Math.max(dp[t][0],\
        \ dp[t][1] + price, dp[t][2] - price);\n\n            // State 1: Holding a\
        \ long position\n            // Option 1: Do nothing (carry over from previous\
        \ day's dp[t][1])\n            // Option 2: Buy a stock (dp[t-1][0] - price).\
        \ This starts the t-th transaction.\n            dp[t][1] = Math.max(dp[t][1],\
        \ dp[t-1][0] - price);\n\n            // State 2: Holding a short position\n\
        \            // Option 1: Do nothing (carry over from previous day's dp[t][2])\n\
        \            // Option 2: Short sell a stock (dp[t-1][0] + price). This starts\
        \ the t-th transaction.\n            dp[t][2] = Math.max(dp[t][2], dp[t-1][0]\
        \ + price);\n        }\n    }\n\n    let maxProfit = 0;\n    for (let t = 0;\
        \ t <= k; ++t) {\n        maxProfit = Math.max(maxProfit, dp[t][0]);\n    }\n\
        \n    return maxProfit;\n}"
      php: "class Solution {\n    /**\n     * @param Integer[] $prices\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function maximumProfit($prices,\
        \ $k) {\n        $n = count($prices);\n\n        // dp[t][0]: max profit with\
        \ t transactions completed, no open position\n        // dp[t][1]: max profit\
        \ with t-1 transactions completed, currently holding a long position (will be\
        \ t-th transaction)\n        // dp[t][2]: max profit with t-1 transactions completed,\
        \ currently holding a short position (will be t-th transaction)\n\n        $dp\
        \ = array_fill(0, $k + 1, array_fill(0, 3, 0));\n\n        for ($t = 0; $t <=\
        \ $k; ++$t) {\n            $dp[$t][0] = 0; // 0 profit with 0 transactions completed\
        \ and no open position\n            $dp[$t][1] = -PHP_INT_MAX / 2; // Use /\
        \ 2 to prevent overflow when adding/subtracting prices\n            $dp[$t][2]\
        \ = -PHP_INT_MAX / 2; // Use / 2 to prevent overflow when adding/subtracting\
        \ prices\n        }\n\n        foreach ($prices as $price) {\n            for\
        \ ($t = $k; $t >= 1; --$t) {\n                // State 0: No open position\n\
        \                // Option 1: Do nothing (carry over from previous day's dp[t][0])\n\
        \                // Option 2: Sell a long position ($dp[$t][1] + $price). This\
        \ completes the t-th transaction.\n                // Option 3: Buy back a short\
        \ position ($dp[$t][2] - $price). This completes the t-th transaction.\n   \
        \             $dp[$t][0] = max($dp[$t][0], $dp[$t][1] + $price, $dp[$t][2] -\
        \ $price);\n\n                // State 1: Holding a long position\n        \
        \        // Option 1: Do nothing (carry over from previous day's dp[$t][1])\n\
        \                // Option 2: Buy a stock ($dp[$t-1][0] - $price). This starts\
        \ the t-th transaction.\n                $dp[$t][1] = max($dp[$t][1], $dp[$t-1][0]\
        \ - $price);\n\n                // State 2: Holding a short position\n     \
        \           // Option 1: Do nothing (carry over from previous day's dp[$t][2])\n\
        \                // Option 2: Short sell a stock ($dp[$t-1][0] + $price). This\
        \ starts the t-th transaction.\n                $dp[$t][2] = max($dp[$t][2],\
        \ $dp[$t-1][0] + $price);\n            }\n        }\n\n        $maxProfit =\
        \ 0;\n        for ($t = 0; $t <= $k; ++$t) {\n            $maxProfit = max($maxProfit,\
        \ $dp[$t][0]);\n        }\n\n        return $maxProfit;\n    }\n}"
      swift: "import Foundation\n\nclass Solution {\n    func maximumProfit(_ prices:\
        \ [Int], _ k: Int) -> Int {\n        let n = prices.count\n\n        // dp[t][0]:\
        \ max profit with t transactions completed, no open position\n        // dp[t][1]:\
        \ max profit with t-1 transactions completed, currently holding a long position\
        \ (will be t-th transaction)\n        // dp[t][2]: max profit with t-1 transactions\
        \ completed, currently holding a short position (will be t-th transaction)\n\
        \n        var dp = Array(repeating: Array(repeating: 0, count: 3), count: k\
        \ + 1)\n\n        for t in 0...k {\n            dp[t][0] = 0 // 0 profit with\
        \ 0 transactions completed and no open position\n            dp[t][1] = Int.min\
        \ / 2 // Use Int.min / 2 to prevent overflow when adding/subtracting prices\n\
        \            dp[t][2] = Int.min / 2 // Use Int.min / 2 to prevent overflow when\
        \ adding/subtracting prices\n        }\n\n        for price in prices {\n  \
        \          for t in (1...k).reversed() {\n                // State 0: No open\
        \ position\n                // Option 1: Do nothing (carry over from previous\
        \ day's dp[t][0])\n                // Option 2: Sell a long position (dp[t][1]\
        \ + price). This completes the t-th transaction.\n                // Option\
        \ 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.\n\
        \                dp[t][0] = max(dp[t][0], dp[t][1] + price, dp[t][2] - price)\n\
        \n                // State 1: Holding a long position\n                // Option\
        \ 1: Do nothing (carry over from previous day's dp[t][1])\n                //\
        \ Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.\n\
        \                dp[t][1] = max(dp[t][1], dp[t-1][0] - price)\n\n          \
        \      // State 2: Holding a short position\n                // Option 1: Do\
        \ nothing (carry over from previous day's dp[t][2])\n                // Option\
        \ 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.\n\
        \                dp[t][2] = max(dp[t][2], dp[t-1][0] + price)\n            }\n\
        \        }\n\n        var maxProfit = 0\n        for t in 0...k {\n        \
        \    maxProfit = max(maxProfit, dp[t][0])\n        }\n\n        return maxProfit\n\
        \    }\n\n    private func max(_ a: Int, _ b: Int, _ c: Int) -> Int {\n    \
        \    return max(a, max(b, c))\n    }\n}"
      kotlin: "import kotlin.math.max\n\nclass Solution {\n    fun maximumProfit(prices:\
        \ IntArray, k: Int): Long {\n        val n = prices.size\n\n        // dp[t][0]:\
        \ max profit with t transactions completed, no open position\n        // dp[t][1]:\
        \ max profit with t-1 transactions completed, currently holding a long position\
        \ (will be t-th transaction)\n        // dp[t][2]: max profit with t-1 transactions\
        \ completed, currently holding a short position (will be t-th transaction)\n\
        \n        val dp = Array(k + 1) { LongArray(3) }\n\n        for (t in 0..k)\
        \ {\n            dp[t][0] = 0L // 0 profit with 0 transactions completed and\
        \ no open position\n            dp[t][1] = Long.MIN_VALUE / 2 // Use Long.MIN_VALUE\
        \ / 2 to prevent overflow when adding/subtracting prices\n            dp[t][2]\
        \ = Long.MIN_VALUE / 2 // Use Long.MIN_VALUE / 2 to prevent overflow when adding/subtracting\
        \ prices\n        }\n\n        for (price in prices) {\n            for (t in\
        \ k downTo 1) {\n                // State 0: No open position\n            \
        \    // Option 1: Do nothing (carry over from previous day's dp[t][0])\n   \
        \             // Option 2: Sell a long position (dp[t][1] + price). This completes\
        \ the t-th transaction.\n                // Option 3: Buy back a short position\
        \ (dp[t][2] - price). This completes the t-th transaction.\n               \
        \ dp[t][0] = max(dp[t][0], max(dp[t][1] + price, dp[t][2] - price))\n\n    \
        \            // State 1: Holding a long position\n                // Option\
        \ 1: Do nothing (carry over from previous day's dp[t][1])\n                //\
        \ Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.\n\
        \                dp[t][1] = max(dp[t][1], dp[t-1][0] - price)\n\n          \
        \      // State 2: Holding a short position\n                // Option 1: Do\
        \ nothing (carry over from previous day's dp[t][2])\n                // Option\
        \ 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.\n\
        \                dp[t][2] = max(dp[t][2], dp[t-1][0] + price)\n            }\n\
        \        }\n\n        var maxProfit = 0L\n        for (t in 0..k) {\n      \
        \      maxProfit = max(maxProfit, dp[t][0])\n        }\n\n        return maxProfit\n\
        \    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maximumProfit(List<int>\
        \ prices, int k) {\n    final n = prices.length;\n\n    // dp[t][0]: max profit\
        \ with t transactions completed, no open position\n    // dp[t][1]: max profit\
        \ with t-1 transactions completed, currently holding a long position (will be\
        \ t-th transaction)\n    // dp[t][2]: max profit with t-1 transactions completed,\
        \ currently holding a short position (will be t-th transaction)\n\n    final\
        \ dp = List.generate(k + 1, (_) => List<int>.filled(3, 0));\n\n    for (int\
        \ t = 0; t <= k; ++t) {\n      dp[t][0] = 0; // 0 profit with 0 transactions\
        \ completed and no open position\n      dp[t][1] = -1000000000000000000; //\
        \ A sufficiently small negative number (larger than -2^53 for JS compatibility)\n\
        \      dp[t][2] = -1000000000000000000; // A sufficiently small negative number\n\
        \    }\n\n    for (final price in prices) {\n      for (int t = k; t >= 1; --t)\
        \ {\n        // State 0: No open position\n        // Option 1: Do nothing (carry\
        \ over from previous day's dp[t][0])\n        // Option 2: Sell a long position\
        \ (dp[t][1] + price). This completes the t-th transaction.\n        // Option\
        \ 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.\n\
        \        dp[t][0] = max(dp[t][0], max(dp[t][1] + price, dp[t][2] - price));\n\
        \n        // State 1: Holding a long position\n        // Option 1: Do nothing\
        \ (carry over from previous day's dp[t][1])\n        // Option 2: Buy a stock\
        \ (dp[t-1][0] - price). This starts the t-th transaction.\n        dp[t][1]\
        \ = max(dp[t][1], dp[t-1][0] - price);\n\n        // State 2: Holding a short\
        \ position\n        // Option 1: Do nothing (carry over from previous day's\
        \ dp[t][2])\n        // Option 2: Short sell a stock (dp[t-1][0] + price). This\
        \ starts the t-th transaction.\n        dp[t][2] = max(dp[t][2], dp[t-1][0]\
        \ + price);\n      }\n    }\n\n    int maxProfit = 0;\n    for (int t = 0; t\
        \ <= k; ++t) {\n      maxProfit = max(maxProfit, dp[t][0]);\n    }\n\n    return\
        \ maxProfit;\n  }\n}"
      go: "import (\n\t\"math\"\n)\n\nfunc maximumProfit(prices []int, k int) int {\n\
        \    n := len(prices)\n\n    // dp[t][0]: max profit with t transactions completed,\
        \ no open position\n    // dp[t][1]: max profit with t-1 transactions completed,\
        \ currently holding a long position (will be t-th transaction)\n    // dp[t][2]:\
        \ max profit with t-1 transactions completed, currently holding a short position\
        \ (will be t-th transaction)\n\n    dp := make([][]int, k + 1)\n    for t :=\
        \ 0; t <= k; t++ {\n        dp[t] = make([]int, 3)\n        dp[t][0] = 0 //\
        \ 0 profit with 0 transactions completed and no open position\n        dp[t][1]\
        \ = math.MinInt64 / 2 // Use / 2 to prevent overflow when adding/subtracting\
        \ prices\n        dp[t][2] = math.MinInt64 / 2 // Use / 2 to prevent overflow\
        \ when adding/subtracting prices\n    }\n\n    for _, price := range prices\
        \ {\n        for t := k; t >= 1; t-- {\n            // State 0: No open position\n\
        \            // Option 1: Do nothing (carry over from previous day's dp[t][0])\n\
        \            // Option 2: Sell a long position (dp[t][1] + price). This completes\
        \ the t-th transaction.\n            // Option 3: Buy back a short position\
        \ (dp[t][2] - price). This completes the t-th transaction.\n            dp[t][0]\
        \ = max(dp[t][0], max(dp[t][1] + price, dp[t][2] - price))\n\n            //\
        \ State 1: Holding a long position\n            // Option 1: Do nothing (carry\
        \ over from previous day's dp[t][1])\n            // Option 2: Buy a stock (dp[t-1][0]\
        \ - price). This starts the t-th transaction.\n            dp[t][1] = max(dp[t][1],\
        \ dp[t-1][0] - price)\n\n            // State 2: Holding a short position\n\
        \            // Option 1: Do nothing (carry over from previous day's dp[t][2])\n\
        \            // Option 2: Short sell a stock (dp[t-1][0] + price). This starts\
        \ the t-th transaction.\n            dp[t][2] = max(dp[t][2], dp[t-1][0] + price)\n\
        \        }\n    }\n\n    maxProfit := 0\n    for t := 0; t <= k; t++ {\n   \
        \     maxProfit = max(maxProfit, dp[t][0])\n    }\n\n    return maxProfit\n\
        }\n\nfunc max(a, b int) int {\n    if a > b {\n        return a\n    }\n   \
        \ return b\n}"
      ruby: "def maximum_profit(prices, k)\n    n = prices.length\n\n    # dp[t][0]:\
        \ max profit with t transactions completed, no open position\n    # dp[t][1]:\
        \ max profit with t-1 transactions completed, currently holding a long position\
        \ (will be t-th transaction)\n    # dp[t][2]: max profit with t-1 transactions\
        \ completed, currently holding a short position (will be t-th transaction)\n\
        \n    dp = Array.new(k + 1) { Array.new(3) }\n\n    (0..k).each do |t|\n   \
        \     dp[t][0] = 0 # 0 profit with 0 transactions completed and no open position\n\
        \        dp[t][1] = -Float::INFINITY # Cannot hold stock without buying\n  \
        \      dp[t][2] = -Float::INFINITY # Cannot hold short without selling\n   \
        \ end\n\n    prices.each do |price|\n        k.downto(1) do |t|\n          \
        \  # State 0: No open position\n            # Option 1: Do nothing (carry over\
        \ from previous day's dp[t][0])\n            # Option 2: Sell a long position\
        \ (dp[t][1] + price). This completes the t-th transaction.\n            # Option\
        \ 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.\n\
        \            dp[t][0] = [dp[t][0], dp[t][1] + price, dp[t][2] - price].max\n\
        \n            # State 1: Holding a long position\n            # Option 1: Do\
        \ nothing (carry over from previous day's dp[t][1])\n            # Option 2:\
        \ Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.\n    \
        \        dp[t][1] = [dp[t][1], dp[t-1][0] - price].max\n\n            # State\
        \ 2: Holding a short position\n            # Option 1: Do nothing (carry over\
        \ from previous day's dp[t][2])\n            # Option 2: Short sell a stock\
        \ (dp[t-1][0] + price). This starts the t-th transaction.\n            dp[t][2]\
        \ = [dp[t][2], dp[t-1][0] + price].max\n        end\n    end\n\n    max_profit\
        \ = 0\n    (0..k).each do |t|\n        max_profit = [max_profit, dp[t][0]].max\n\
        \    end\n\n    return max_profit\nend"
      scala: "import scala.math.max\n\nobject Solution {\n    def maximumProfit(prices:\
        \ Array[Int], k: Int): Long = {\n        val n = prices.length\n\n        //\
        \ dp(t)(0): max profit with t transactions completed, no open position\n   \
        \     // dp(t)(1): max profit with t-1 transactions completed, currently holding\
        \ a long position (will be t-th transaction)\n        // dp(t)(2): max profit\
        \ with t-1 transactions completed, currently holding a short position (will\
        \ be t-th transaction)\n\n        val dp = Array.ofDim[Long](k + 1, 3)\n\n \
        \       for (t <- 0 to k) {\n            dp(t)(0) = 0L // 0 profit with 0 transactions\
        \ completed and no open position\n            dp(t)(1) = Long.MinValue / 2 //\
        \ Use Long.MinValue / 2 to prevent overflow when adding/subtracting prices\n\
        \            dp(t)(2) = Long.MinValue / 2 // Use Long.MinValue / 2 to prevent\
        \ overflow when adding/subtracting prices\n        }\n\n        for (price <-\
        \ prices) {\n            for (t <- k to 1 by -1) {\n                // State\
        \ 0: No open position\n                // Option 1: Do nothing (carry over from\
        \ previous day's dp(t)(0))\n                // Option 2: Sell a long position\
        \ (dp(t)(1) + price). This completes the t-th transaction.\n               \
        \ // Option 3: Buy back a short position (dp(t)(2) - price). This completes\
        \ the t-th transaction.\n                dp(t)(0) = max(dp(t)(0), max(dp(t)(1)\
        \ + price, dp(t)(2) - price))\n\n                // State 1: Holding a long\
        \ position\n                // Option 1: Do nothing (carry over from previous\
        \ day's dp(t)(1))\n                // Option 2: Buy a stock (dp(t-1)(0) - price).\
        \ This starts the t-th transaction.\n                dp(t)(1) = max(dp(t)(1),\
        \ dp(t-1)(0) - price)\n\n                // State 2: Holding a short position\n\
        \                // Option 1: Do nothing (carry over from previous day's dp(t)(2))\n\
        \                // Option 2: Short sell a stock (dp(t-1)(0) + price). This\
        \ starts the t-th transaction.\n                dp(t)(2) = max(dp(t)(2), dp(t-1)(0)\
        \ + price)\n            }\n        }\n\n        var maxProfit = 0L\n       \
        \ for (t <- 0 to k) {\n            maxProfit = max(maxProfit, dp(t)(0))\n  \
        \      }\n\n        maxProfit\n    }\n}"
      rust: "use std::cmp::max;\n\nimpl Solution {\n    pub fn maximum_profit(prices:\
        \ Vec<i32>, k: i32) -> i32 {\n        let n = prices.len();\n        let k =\
        \ k as usize;\n\n        // dp[t][0]: max profit with t transactions completed,\
        \ no open position\n        // dp[t][1]: max profit with t-1 transactions completed,\
        \ currently holding a long position (will be t-th transaction)\n        // dp[t][2]:\
        \ max profit with t-1 transactions completed, currently holding a short position\
        \ (will be t-th transaction)\n\n        let mut dp: Vec<Vec<i64>> = vec![vec![0;\
        \ 3]; k + 1];\n\n        for t in 0..=k {\n            dp[t][0] = 0; // 0 profit\
        \ with 0 transactions completed and no open position\n            dp[t][1] =\
        \ i64::MIN / 2; // Use / 2 to prevent overflow when adding/subtracting prices\n\
        \            dp[t][2] = i64::MIN / 2; // Use / 2 to prevent overflow when adding/subtracting\
        \ prices\n        }\n\n        for price_i32 in prices {\n            let price\
        \ = price_i32 as i64;\n            for t in (1..=k).rev() {\n              \
        \  // State 0: No open position\n                // Option 1: Do nothing (carry\
        \ over from previous day's dp[t][0])\n                // Option 2: Sell a long\
        \ position (dp[t][1] + price). This completes the t-th transaction.\n      \
        \          // Option 3: Buy back a short position (dp[t][2] - price). This completes\
        \ the t-th transaction.\n                dp[t][0] = max(dp[t][0], max(dp[t][1]\
        \ + price, dp[t][2] - price));\n\n                // State 1: Holding a long\
        \ position\n                // Option 1: Do nothing (carry over from previous\
        \ day's dp[t][1])\n                // Option 2: Buy a stock (dp[t-1][0] - price).\
        \ This starts the t-th transaction.\n                dp[t][1] = max(dp[t][1],\
        \ dp[t-1][0] - price);\n\n                // State 2: Holding a short position\n\
        \                // Option 1: Do nothing (carry over from previous day's dp[t][2])\n\
        \                // Option 2: Short sell a stock (dp[t-1][0] + price). This\
        \ starts the t-th transaction.\n                dp[t][2] = max(dp[t][2], dp[t-1][0]\
        \ + price);\n            }\n        }\n\n        let mut max_profit = 0;\n \
        \       for t in 0..=k {\n            max_profit = max(max_profit, dp[t][0]);\n\
        \        }\n\n        max_profit as i32\n    }\n}"
      racket: "#lang racket\n(provide (struct-out Solution) (struct-out List) (struct-out\
        \ Integer) (struct-out Double))\n\n(define-struct Solution ())\n\n(define (maximumProfit\
        \ self prices k)\n  (define n (vector-length prices))\n\n  ;; dp[t][0]: max\
        \ profit with t transactions completed, no open position\n  ;; dp[t][1]: max\
        \ profit with t-1 transactions completed, currently holding a long position\
        \ (will be t-th transaction)\n  ;; dp[t][2]: max profit with t-1 transactions\
        \ completed, currently holding a short position (will be t-th transaction)\n\
        \n  (define dp (build-vector (+ k 1) (lambda (t) (vector 0 -inf.0 -inf.0))))\n\
        \n  (for ([price (in-vector prices)])\n    (for ([t (in-range k 0 -1)])\n  \
        \    (vector-set! (vector-ref dp t) 0\n                   (max (vector-ref (vector-ref\
        \ dp t) 0)\n                        (+ (vector-ref (vector-ref dp t) 1) price)\n\
        \                        (- (vector-ref (vector-ref dp t) 2) price)))\n\n  \
        \    (vector-set! (vector-ref dp t) 1\n                   (max (vector-ref (vector-ref\
        \ dp t) 1)\n                        (- (vector-ref (vector-ref dp (- t 1)) 0)\
        \ price)))\n\n      (vector-set! (vector-ref dp t) 2\n                   (max\
        \ (vector-ref (vector-ref dp t) 2)\n                        (+ (vector-ref (vector-ref\
        \ dp (- t 1)) 0) price)))))\n\n  (define max-profit 0)\n  (for ([t (in-range\
        \ (+ k 1))])\n    (set! max-profit (max max-profit (vector-ref (vector-ref dp\
        \ t) 0))))\n\n  max-profit)"
      erlang: "-module(solution).\n-export([maximum_profit/2]).\n\nmaximum_profit(Prices,\
        \ K) ->\n    N = length(Prices),\n\n    % dp[t][0]: max profit with t transactions\
        \ completed, no open position\n    % dp[t][1]: max profit with t-1 transactions\
        \ completed, currently holding a long position (will be t-th transaction)\n\
        \    % dp[t][2]: max profit with t-1 transactions completed, currently holding\
        \ a short position (will be t-th transaction)\n\n    % Initialize dp table\n\
        \    % dp[t][0] = 0 for all t (0 profit with 0 transactions)\n    % dp[t][1]\
        \ = -infinity (cannot hold stock without buying)\n    % dp[t][2] = -infinity\
        \ (cannot hold short without selling)\n\n    % Using a list of lists for dp\
        \ table. Each inner list is [dp[t][0], dp[t][1], dp[t][2]]\n    InitialDP =\
        \ lists:duplicate(K + 1, [0, -9223372036854775807 div 2, -9223372036854775807\
        \ div 2]), % Use / 2 to prevent overflow\n\n    FinalDP = lists:foldl(\n   \
        \     fun(Price, CurrentDP) ->\n            lists:foldl(\n                fun(T,\
        \ AccDP) ->\n                    % Get previous day's values for current T\n\
        \                    [Prev_dp_t_0, Prev_dp_t_1, Prev_dp_t_2] = lists:nth(T +\
        \ 1, AccDP),\n\n                    % Get previous day's values for T-1\n  \
        \                  [Prev_dp_t_minus_1_0, _, _] = lists:nth(T, AccDP),\n\n  \
        \                  % State 0: No open position\n                    New_dp_t_0\
        \ = max(Prev_dp_t_0, max(Prev_dp_t_1 + Price, Prev_dp_t_2 - Price)),\n\n   \
        \                 % State 1: Holding a long position\n                    New_dp_t_1\
        \ = max(Prev_dp_t_1, Prev_dp_t_minus_1_0 - Price),\n\n                    %\
        \ State 2: Holding a short position\n                    New_dp_t_2 = max(Prev_dp_t_2,\
        \ Prev_dp_t_minus_1_0 + Price),\n\n                    % Update AccDP for current\
        \ T\n                    lists:replace_nth(T + 1, [New_dp_t_0, New_dp_t_1, New_dp_t_2],\
        \ AccDP)\n                end, CurrentDP, lists:seq(K, 1, -1))\n        end,\
        \ InitialDP, Prices\n    ),\n\n    MaxProfit = lists:foldl(\n        fun(T_dp_values,\
        \ CurrentMax) ->\n            max(CurrentMax, hd(T_dp_values)) % dp[t][0] is\
        \ the first element\n        end, 0, FinalDP\n    ),\n\n    MaxProfit.\n\n%\
        \ Helper function for max of two values\nmax(A, B) when A > B -> A;\nmax(A,\
        \ B) -> B."
      elixir: "defmodule Solution do\n  @spec maximum_profit(prices :: [integer], k\
        \ :: integer) :: integer\n  def maximum_profit(prices, k) do\n    # dp[t][0]:\
        \ max profit with t transactions completed, no open position\n    # dp[t][1]:\
        \ max profit with t-1 transactions completed, currently holding a long position\
        \ (will be t-th transaction)\n    # dp[t][2]: max profit with t-1 transactions\
        \ completed, currently holding a short position (will be t-th transaction)\n\
        \n    # Initialize dp table\n    # dp[t][0] = 0 for all t (0 profit with 0 transactions)\n\
        \    # dp[t][1] = -infinity (cannot hold stock without buying)\n    # dp[t][2]\
        \ = -infinity (cannot hold short without selling)\n\n    # Using a list of lists\
        \ for dp table. Each inner list is {dp[t][0], dp[t][1], dp[t][2]}\n    # Using\
        \ a large negative number for -infinity, e.g., -10^18\n    initial_dp = Enum.map(0..k,\
        \ fn _ -> {0, -1_000_000_000_000_000_000, -1_000_000_000_000_000_000} end)\n\
        \n    final_dp = Enum.reduce(prices, initial_dp, fn price, current_dp ->\n \
        \     Enum.reduce(k..1, current_dp, fn t, acc_dp ->\n        # Get previous\
        \ day's values for current T\n        {prev_dp_t_0, prev_dp_t_1, prev_dp_t_2}\
        \ = Enum.at(acc_dp, t)\n\n        # Get previous day's values for T-1\n    \
        \    {prev_dp_t_minus_1_0, _, _} = Enum.at(acc_dp, t - 1)\n\n        # State\
        \ 0: No open position\n        new_dp_t_0 = max(prev_dp_t_0, max(prev_dp_t_1\
        \ + price, prev_dp_t_2 - price))\n\n        # State 1: Holding a long position\n\
        \        new_dp_t_1 = max(prev_dp_t_1, prev_dp_t_minus_1_0 - price)\n\n    \
        \    # State 2: Holding a short position\n        new_dp_t_2 = max(prev_dp_t_2,\
        \ prev_dp_t_minus_1_0 + price)\n\n        # Update acc_dp for current T\n  \
        \      List.replace_at(acc_dp, t, {new_dp_t_0, new_dp_t_1, new_dp_t_2})\n  \
        \    end)\n    end)\n\n    max_profit = Enum.reduce(final_dp, 0, fn {t_dp_0,\
        \ _, _}, current_max ->\n      max(current_max, t_dp_0)\n    end)\n\n    max_profit\n\
        \  end\n\n  defp max(a, b) when a > b, do: a\n  defp max(a, b), do: b\nend"
    approach: 'This problem can be solved using dynamic programming. We define a 2D
      DP table `dp[t][state]` where `t` represents the number of transactions completed
      and `state` indicates the current position. The `state` can be one of three types:
      `0` for no open position, `1` for an open long position (stock bought), and `2`
      for an open short position (stock sold). The value `dp[t][state]` stores the maximum
      profit achieved in that specific state. For `dp[t][1]` and `dp[t][2]`, `t` refers
      to the transaction that *will be completed* when the current open position is
      closed, meaning `t-1` transactions are already completed.'
    time_complexity: The time complexity is O(N * k), where N is the number of days
      (length of `prices` array) and k is the maximum number of transactions allowed.
      We iterate through each day's price, and for each price, we iterate through `k`
      possible transaction counts. Each DP state update takes constant time.
    space_complexity: The space complexity is O(k). The DP table `dp` has dimensions
      `(k+1) x 3`. Since the current day's DP values only depend on the previous day's
      values, we can optimize space to only store the states for the current and previous
      day. By iterating the transaction count `t` downwards, we can achieve O(k) space
      using a single DP table.
    elapsed_time: 156.94677257537842
    model: gemini-2.5-flash
    generated_at: '2025-12-17 02:07:56 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxProfit(vector<int>& prices, int k)\
        \ {\n        int n = prices.size();\n        if (n < 2) return 0;\n        k\
        \ = min(k, n / 2);\n        vector<vector<int>> buy(n, vector<int>(k + 1, 0));\n\
        \        vector<vector<int>> sell(n, vector<int>(k + 1, 0));\n        for (int\
        \ i = 1; i < n; i++) {\n            for (int j = 1; j <= k; j++) {\n       \
        \         buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i]);\n    \
        \            sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);\n\
        \            }\n        }\n        return sell[n - 1][k];\n    }\n};"
      java: "class Solution {\n    public int maxProfit(int[] prices, int k) {\n   \
        \     int n = prices.length;\n        if (n < 2) return 0;\n        k = Math.min(k,\
        \ n / 2);\n        int[][] buy = new int[n][k + 1];\n        int[][] sell =\
        \ new int[n][k + 1];\n        for (int i = 1; i < n; i++) {\n            for\
        \ (int j = 1; j <= k; j++) {\n                buy[i][j] = Math.max(buy[i - 1][j],\
        \ sell[i - 1][j] - prices[i]);\n                sell[i][j] = Math.max(sell[i\
        \ - 1][j], buy[i - 1][j - 1] + prices[i]);\n            }\n        }\n     \
        \   return sell[n - 1][k];\n    }\n}"
      python: "class Solution:\n    def maxProfit(self, prices: List[int], k: int) ->\
        \ int:\n        n = len(prices)\n        if n < 2: return 0\n        k = min(k,\
        \ n // 2)\n        buy = [[0] * (k + 1) for _ in range(n)]\n        sell = [[0]\
        \ * (k + 1) for _ in range(n)]\n        for i in range(1, n):\n            for\
        \ j in range(1, k + 1):\n                buy[i][j] = max(buy[i - 1][j], sell[i\
        \ - 1][j] - prices[i])\n                sell[i][j] = max(sell[i - 1][j], buy[i\
        \ - 1][j - 1] + prices[i])\n        return sell[n - 1][k]"
      python3: "class Solution:\n    def maxProfit(self, prices: List[int], k: int)\
        \ -> int:\n        n = len(prices)\n        if n < 2: return 0\n        k =\
        \ min(k, n // 2)\n        buy = [[0] * (k + 1) for _ in range(n)]\n        sell\
        \ = [[0] * (k + 1) for _ in range(n)]\n        for i in range(1, n):\n     \
        \       for j in range(1, k + 1):\n                buy[i][j] = max(buy[i - 1][j],\
        \ sell[i - 1][j] - prices[i])\n                sell[i][j] = max(sell[i - 1][j],\
        \ buy[i - 1][j - 1] + prices[i])\n        return sell[n - 1][k]"
      c: "typedef struct {\n    int* arr;\n    int size;\n} Array;\n\nint maxProfit(int*\
        \ prices, int pricesSize, int k) {\n    if (pricesSize < 2) return 0;\n    k\
        \ = k < pricesSize / 2 ? k : pricesSize / 2;\n    int** buy = (int**)malloc(sizeof(int*)\
        \ * pricesSize);\n    int** sell = (int**)malloc(sizeof(int*) * pricesSize);\n\
        \    for (int i = 0; i < pricesSize; i++) {\n        buy[i] = (int*)malloc(sizeof(int)\
        \ * (k + 1));\n        sell[i] = (int*)malloc(sizeof(int) * (k + 1));\n    }\n\
        \    for (int i = 1; i < pricesSize; i++) {\n        for (int j = 1; j <= k;\
        \ j++) {\n            buy[i][j] = (buy[i - 1][j] > sell[i - 1][j] - prices[i])\
        \ ? buy[i - 1][j] : sell[i - 1][j] - prices[i];\n            sell[i][j] = (sell[i\
        \ - 1][j] > buy[i - 1][j - 1] + prices[i]) ? sell[i - 1][j] : buy[i - 1][j -\
        \ 1] + prices[i];\n        }\n    }\n    int result = sell[pricesSize - 1][k];\n\
        \    for (int i = 0; i < pricesSize; i++) {\n        free(buy[i]);\n       \
        \ free(sell[i]);\n    }\n    free(buy);\n    free(sell);\n    return result;\n\
        }"
      csharp: "public class Solution {\n    public int MaxProfit(int[] prices, int k)\
        \ {\n        int n = prices.Length;\n        if (n < 2) return 0;\n        k\
        \ = Math.Min(k, n / 2);\n        int[][] buy = new int[n][];\n        int[][]\
        \ sell = new int[n][];\n        for (int i = 0; i < n; i++) {\n            buy[i]\
        \ = new int[k + 1];\n            sell[i] = new int[k + 1];\n        }\n    \
        \    for (int i = 1; i < n; i++) {\n            for (int j = 1; j <= k; j++)\
        \ {\n                buy[i][j] = Math.Max(buy[i - 1][j], sell[i - 1][j] - prices[i]);\n\
        \                sell[i][j] = Math.Max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);\n\
        \            }\n        }\n        return sell[n - 1][k];\n    }\n}"
      javascript: "var maxProfit = function(prices, k) {\n    let n = prices.length;\n\
        \    if (n < 2) return 0;\n    k = Math.min(k, Math.floor(n / 2));\n    let\
        \ buy = Array(n).fill(0).map(() => Array(k + 1).fill(0));\n    let sell = Array(n).fill(0).map(()\
        \ => Array(k + 1).fill(0));\n    for (let i = 1; i < n; i++) {\n        for\
        \ (let j = 1; j <= k; j++) {\n            buy[i][j] = Math.max(buy[i - 1][j],\
        \ sell[i - 1][j] - prices[i]);\n            sell[i][j] = Math.max(sell[i - 1][j],\
        \ buy[i - 1][j - 1] + prices[i]);\n        }\n    }\n    return sell[n - 1][k];\n\
        };"
      typescript: "function maxProfit(prices: number[], k: number): number {\n    let\
        \ n: number = prices.length;\n    if (n < 2) return 0;\n    k = Math.min(k,\
        \ Math.floor(n / 2));\n    let buy: number[][] = Array(n).fill(0).map(() =>\
        \ Array(k + 1).fill(0));\n    let sell: number[][] = Array(n).fill(0).map(()\
        \ => Array(k + 1).fill(0));\n    for (let i: number = 1; i < n; i++) {\n   \
        \     for (let j: number = 1; j <= k; j++) {\n            buy[i][j] = Math.max(buy[i\
        \ - 1][j], sell[i - 1][j] - prices[i]);\n            sell[i][j] = Math.max(sell[i\
        \ - 1][j], buy[i - 1][j - 1] + prices[i]);\n        }\n    }\n    return sell[n\
        \ - 1][k];\n}"
      php: "class Solution {\n    function maxProfit($prices, $k) {\n        $n = count($prices);\n\
        \        if ($n < 2) return 0;\n        $k = min($k, floor($n / 2));\n     \
        \   $buy = array_fill(0, $n, array_fill(0, $k + 1, 0));\n        $sell = array_fill(0,\
        \ $n, array_fill(0, $k + 1, 0));\n        for ($i = 1; $i < $n; $i++) {\n  \
        \          for ($j = 1; $j <= $k; $j++) {\n                $buy[$i][$j] = max($buy[$i\
        \ - 1][$j], $sell[$i - 1][$j] - $prices[$i]);\n                $sell[$i][$j]\
        \ = max($sell[$i - 1][$j], $buy[$i - 1][$j - 1] + $prices[$i]);\n          \
        \  }\n        }\n        return $sell[$n - 1][$k];\n    }\n}"
      swift: "class Solution {\n    func maxProfit(_ prices: [Int], _ k: Int) -> Int\
        \ {\n        let n = prices.count\n        if n < 2 { return 0 }\n        let\
        \ k = min(k, n / 2)\n        var buy: [[Int]] = Array(repeating: Array(repeating:\
        \ 0, count: k + 1), count: n)\n        var sell: [[Int]] = Array(repeating:\
        \ Array(repeating: 0, count: k + 1), count: n)\n        for i in 1..<n {\n \
        \           for j in 1...k {\n                buy[i][j] = max(buy[i - 1][j],\
        \ sell[i - 1][j] - prices[i])\n                sell[i][j] = max(sell[i - 1][j],\
        \ buy[i - 1][j - 1] + prices[i])\n            }\n        }\n        return sell[n\
        \ - 1][k]\n    }\n}"
      kotlin: "class Solution {\n    fun maxProfit(prices: IntArray, k: Int): Int {\n\
        \        val n = prices.size\n        if (n < 2) return 0\n        val k = minOf(k,\
        \ n / 2)\n        val buy = Array(n) { IntArray(k + 1) }\n        val sell =\
        \ Array(n) { IntArray(k + 1) }\n        for (i in 1 until n) {\n           \
        \ for (j in 1..k) {\n                buy[i][j] = maxOf(buy[i - 1][j], sell[i\
        \ - 1][j] - prices[i])\n                sell[i][j] = maxOf(sell[i - 1][j], buy[i\
        \ - 1][j - 1] + prices[i])\n            }\n        }\n        return sell[n\
        \ - 1][k]\n    }\n}"
      dart: "class Solution {\n    int maxProfit(List<int> prices, int k) {\n      \
        \  int n = prices.length;\n        if (n < 2) return 0;\n        k = k < n ~/\
        \ 2 ? k : n ~/ 2;\n        List<List<int>> buy = List.generate(n, (i) => List.generate(k\
        \ + 1, (j) => 0));\n        List<List<int>> sell = List.generate(n, (i) => List.generate(k\
        \ + 1, (j) => 0));\n        for (int i = 1; i < n; i++) {\n            for (int\
        \ j = 1; j <= k; j++) {\n                buy[i][j] = max(buy[i - 1][j], sell[i\
        \ - 1][j] - prices[i]);\n                sell[i][j] = max(sell[i - 1][j], buy[i\
        \ - 1][j - 1] + prices[i]);\n            }\n        }\n        return sell[n\
        \ - 1][k];\n    }\n}"
      go: "func maxProfit(prices []int, k int) int {\n    n := len(prices)\n    if n\
        \ < 2 {\n        return 0\n    }\n    k = min(k, n/2)\n    buy := make([][]int,\
        \ n)\n    sell := make([][]int, n)\n    for i := range buy {\n        buy[i]\
        \ = make([]int, k+1)\n        sell[i] = make([]int, k+1)\n    }\n    for i :=\
        \ 1; i < n; i++ {\n        for j := 1; j <= k; j++ {\n            buy[i][j]\
        \ = max(buy[i-1][j], sell[i-1][j]-prices[i])\n            sell[i][j] = max(sell[i-1][j],\
        \ buy[i-1][j-1]+prices[i])\n        }\n    }\n    return sell[n-1][k]\n}\n\n\
        func max(a, b int) int {\n    if a > b {\n        return a\n    }\n    return\
        \ b\n}\n\nfunc min(a, b int) int {\n    if a < b {\n        return a\n    }\n\
        \    return b\n}"
      ruby: "class Solution\n    def max_profit(prices, k)\n        n = prices.size\n\
        \        return 0 if n < 2\n        k = [k, n / 2].min\n        buy = Array.new(n)\
        \ { Array.new(k + 1, 0) }\n        sell = Array.new(n) { Array.new(k + 1, 0)\
        \ }\n        (1...n).each do |i|\n            (1..k).each do |j|\n         \
        \       buy[i][j] = [buy[i - 1][j], sell[i - 1][j] - prices[i]].max\n      \
        \          sell[i][j] = [sell[i - 1][j], buy[i - 1][j - 1] + prices[i]].max\n\
        \            end\n        end\n        sell[n - 1][k]\n    end\nend"
      scala: "object Solution {\n    def maxProfit(prices: Array[Int], k: Int): Int\
        \ = {\n        val n = prices.length\n        if (n < 2) return 0\n        val\
        \ k1 = Math.min(k, n / 2)\n        val buy = Array.ofDim[Int](n, k1 + 1)\n \
        \       val sell = Array.ofDim[Int](n, k1 + 1)\n        for (i <- 1 until n)\
        \ {\n            for (j <- 1 to k1) {\n                buy(i)(j) = Math.max(buy(i\
        \ - 1)(j), sell(i - 1)(j) - prices(i))\n                sell(i)(j) = Math.max(sell(i\
        \ - 1)(j), buy(i - 1)(j - 1) + prices(i))\n            }\n        }\n      \
        \  sell(n - 1)(k1)\n    }\n}"
      rust: "struct Solution;\nimpl Solution {\n    pub fn max_profit(prices: Vec<i32>,\
        \ k: i32) -> i32 {\n        let n = prices.len();\n        if n < 2 {\n    \
        \        return 0;\n        }\n        let k = k.min(n as i32 / 2);\n      \
        \  let mut buy: Vec<Vec<i32>> = vec![vec![0; k as usize + 1]; n];\n        let\
        \ mut sell: Vec<Vec<i32>> = vec![vec![0; k as usize + 1]; n];\n        for i\
        \ in 1..n {\n            for j in 1..=k as usize {\n                buy[i][j]\
        \ = buy[i - 1][j].max(sell[i - 1][j] - prices[i]);\n                sell[i][j]\
        \ = sell[i - 1][j].max(buy[i - 1][j - 1] + prices[i]);\n            }\n    \
        \    }\n        sell[n - 1][k as usize]\n    }\n}"
      racket: "define (max-profit prices k)\n    (let* ((n (length prices))\n      \
        \     (k (min k (quotient n 2))))\n        (if (< n 2)\n            0\n    \
        \        (let loop ((i 1) (buy (make-list n (make-list (+ k 1) 0))) (sell (make-list\
        \ n (make-list (+ k 1) 0))))\n                (if (= i n)\n                \
        \    (list-ref (list-ref sell (- n 1)) k)\n                    (loop (+ i 1)\n\
        \                          (for/list ((j (range 1 (+ k 1))))\n             \
        \                 (max (list-ref (list-ref buy (- i 1)) j)\n               \
        \                    (- (list-ref (list-ref sell (- i 1)) j) (list-ref prices\
        \ i))))\n                          (for/list ((j (range 1 (+ k 1))))\n     \
        \                         (max (list-ref (list-ref sell (- i 1)) j)\n      \
        \                             (+ (list-ref (list-ref buy (- i 1)) (- j 1)) (list-ref\
        \ prices i))))))))))"
      erlang: "max_profit(Prices, K) ->\n    N = length(Prices),\n    K1 = min(K, N\
        \ div 2),\n    Buy = array:new(N, {default, array:new(K1 + 1, {default, 0})}),\n\
        \    Sell = array:new(N, {default, array:new(K1 + 1, {default, 0})}),\n    max_profit(N\
        \ - 1, Prices, K1, Buy, Sell).\n\nmax_profit(0, _, _, Buy, Sell) ->\n    array:get(0,\
        \ array:get(array:size(Buy) - 1, Sell));\nmax_profit(I, Prices, K, Buy, Sell)\
        \ ->\n    NewBuy = array:set(I, array:map(fun(J) -> max(array:get(I - 1, array:get(J,\
        \ Buy)), array:get(I - 1, array:get(J, Sell)) - element(I + 1, Prices)) end,\
        \ array:get(I, Buy)), Buy),\n    NewSell = array:set(I, array:map(fun(J) ->\
        \ max(array:get(I - 1, array:get(J, Sell)), array:get(I - 1, array:get(J - 1,\
        \ Buy)) + element(I + 1, Prices)) end, array:get(I, Sell)), Sell),\n    max_profit(I\
        \ - 1, Prices, K, NewBuy, NewSell)."
      elixir: "defmodule Solution do\n    def max_profit(prices, k) do\n        n =\
        \ length(prices)\n        if n < 2 do\n            0\n        else\n       \
        \     k = min(k, div(n, 2))\n            buy = Array.new(n, fn -> Array.new(k\
        \ + 1, 0) end)\n            sell = Array.new(n, fn -> Array.new(k + 1, 0) end)\n\
        \            max_profit(1, n - 1, prices, k, buy, sell)\n        end\n    end\n\
        \n    defp max_profit(n, n, _, _, buy, sell) do\n        Array.get(sell, n,\
        \ 0)\n    end\n\n    defp max_profit(i, n, prices, k, buy, sell) do\n      \
        \  buy = Array.update!(buy, i, fn x ->\n            Enum.map(1..k, fn j ->\n\
        \                max(Enum.at(x, j - 1), Enum.at(Enum.at(sell, i - 1, []), j\
        \ - 1) - Enum.at(prices, i))\n            end)\n        end)\n\n        sell\
        \ = Array.update!(sell, i, fn x ->\n            Enum.map(1..k, fn j ->\n   \
        \             max(Enum.at(x, j - 1), Enum.at(Enum.at(buy, i - 1, []), j - 2)\
        \ + Enum.at(prices, i))\n            end)\n        end)\n\n        max_profit(i\
        \ + 1, n, prices, k, buy, sell)\n    end\nend"
    approach: The problem can be solved using dynamic programming. We need to keep track
      of the maximum profit we can get after a certain number of transactions. We can
      use a 2D array to store the maximum profit after each transaction. The key intuition
      is that we can either choose to make a transaction on the current day or not.
      If we choose to make a transaction, we need to consider whether we are buying
      or selling the stock. We can use two variables to keep track of the maximum profit
      when we are holding the stock and when we are not holding the stock. We can update
      these variables based on the current price and the previous maximum profit.
    time_complexity: The time complexity of the solution is O(n*k) where n is the number
      of days and k is the number of transactions. This is because we need to iterate
      over each day and each transaction to update the maximum profit.
    space_complexity: The space complexity of the solution is O(n*k) where n is the
      number of days and k is the number of transactions. This is because we need to
      store the maximum profit after each transaction for each day.
    elapsed_time: 10.267377376556396
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-17 02:08:06 '
---

## Problem #3573: Best Time to Buy and Sell Stock V

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming

## Problem Description

<p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a stock in dollars on the <code>i<sup>th</sup></code> day, and an integer <code>k</code>.</p>

<p>You are allowed to make at most <code>k</code> transactions, where each transaction can be either of the following:</p>

<ul>
	<li>
	<p><strong>Normal transaction</strong>: Buy on day <code>i</code>, then sell on a later day <code>j</code> where <code>i &lt; j</code>. You profit <code>prices[j] - prices[i]</code>.</p>
	</li>
	<li>
	<p><strong>Short selling transaction</strong>: Sell on day <code>i</code>, then buy back on a later day <code>j</code> where <code>i &lt; j</code>. You profit <code>prices[i] - prices[j]</code>.</p>
	</li>
</ul>

<p><strong>Note</strong> that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.</p>

<p>Return the <strong>maximum</strong> total profit you can earn by making <strong>at most</strong> <code>k</code> transactions.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">prices = [1,7,9,8,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>
We can make $14 of profit through 2 transactions:

<ul>
	<li>A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.</li>
	<li>A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">prices = [12,16,19,19,8,1,19,13,9], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">36</span></p>

<p><strong>Explanation:</strong></p>
We can make $36 of profit through 3 transactions:

<ul>
	<li>A normal transaction: buy the stock on day 0 for $12 then sell it on day 2 for $19.</li>
	<li>A short selling transaction: sell the stock on day 3 for $19 then buy back on day 4 for $8.</li>
	<li>A normal transaction: buy the stock on day 5 for $1 then sell it on day 6 for $19.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= prices.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= prices[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= prices.length / 2</code></li>
</ul>


## Hints

1. Use dynamic programming.

2. Keep the following states: `idx`, `transactionsDone`, `transactionType`, `isTransactionRunning`.

3. Transactions transition from completed -> running and from running -> completed.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-17 02:07:56 )</small>
</summary>

<div class="ai-solution-content">

### Approach

This problem can be solved using dynamic programming. We define a 2D DP table `dp[t][state]` where `t` represents the number of transactions completed and `state` indicates the current position. The `state` can be one of three types: `0` for no open position, `1` for an open long position (stock bought), and `2` for an open short position (stock sold). The value `dp[t][state]` stores the maximum profit achieved in that specific state. For `dp[t][1]` and `dp[t][2]`, `t` refers to the transaction that *will be completed* when the current open position is closed, meaning `t-1` transactions are already completed.

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
    long long maximumProfit(vector<int>& prices, int k) {
        int n = prices.size();

        // dp[t][0]: max profit with t transactions completed, no open position
        // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
        // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

        vector<vector<long long>> dp(k + 1, vector<long long>(3));

        for (int t = 0; t <= k; ++t) {
            dp[t][0] = 0; // 0 profit with 0 transactions completed and no open position
            dp[t][1] = LLONG_MIN / 2; // Use LLONG_MIN / 2 to prevent overflow when adding/subtracting prices
            dp[t][2] = LLONG_MIN / 2; // Use LLONG_MIN / 2 to prevent overflow when adding/subtracting prices
        }

        for (int price : prices) {
            for (int t = k; t >= 1; --t) {
                // State 0: No open position
                // Option 1: Do nothing (carry over from previous day's dp[t][0])
                // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
                // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
                dp[t][0] = max({dp[t][0], dp[t][1] + price, dp[t][2] - price});

                // State 1: Holding a long position
                // Option 1: Do nothing (carry over from previous day's dp[t][1])
                // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
                dp[t][1] = max(dp[t][1], dp[t-1][0] - price);

                // State 2: Holding a short position
                // Option 1: Do nothing (carry over from previous day's dp[t][2])
                // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
                dp[t][2] = max(dp[t][2], dp[t-1][0] + price);
            }
        }

        long long max_profit = 0;
        for (int t = 0; t <= k; ++t) {
            max_profit = max(max_profit, dp[t][0]);
        }

        return max_profit;
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
    public long maximumProfit(int[] prices, int k) {
        int n = prices.length;

        // dp[t][0]: max profit with t transactions completed, no open position
        // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
        // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

        long[][] dp = new long[k + 1][3];

        for (int t = 0; t <= k; ++t) {
            dp[t][0] = 0; // 0 profit with 0 transactions completed and no open position
            dp[t][1] = Long.MIN_VALUE / 2; // Use Long.MIN_VALUE / 2 to prevent overflow when adding/subtracting prices
            dp[t][2] = Long.MIN_VALUE / 2; // Use Long.MIN_VALUE / 2 to prevent overflow when adding/subtracting prices
        }

        for (int price : prices) {
            for (int t = k; t >= 1; --t) {
                // State 0: No open position
                // Option 1: Do nothing (carry over from previous day's dp[t][0])
                // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
                // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
                dp[t][0] = Math.max(dp[t][0], Math.max(dp[t][1] + price, dp[t][2] - price));

                // State 1: Holding a long position
                // Option 1: Do nothing (carry over from previous day's dp[t][1])
                // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
                dp[t][1] = Math.max(dp[t][1], dp[t-1][0] - price);

                // State 2: Holding a short position
                // Option 1: Do nothing (carry over from previous day's dp[t][2])
                // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
                dp[t][2] = Math.max(dp[t][2], dp[t-1][0] + price);
            }
        }

        long maxProfit = 0;
        for (int t = 0; t <= k; ++t) {
            maxProfit = Math.max(maxProfit, dp[t][0]);
        }

        return maxProfit;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import math

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        # dp[t][0]: max profit with t transactions completed, no open position
        # dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
        # dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

        dp = [[0] * 3 for _ in range(k + 1)]

        for t in range(k + 1):
            dp[t][1] = -math.inf
            dp[t][2] = -math.inf

        # Iterate through each price
        for price in prices:
            # Iterate transactions from k down to 1
            # This order ensures that dp[t-1][0] refers to the value from the previous day
            # (or previous iteration of the outer loop)
            for t in range(k, 0, -1):
                # State 0: No open position
                # Option 1: Do nothing (carry over from previous day's dp[t][0])
                # Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
                # Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
                dp[t][0] = max(dp[t][0], dp[t][1] + price, dp[t][2] - price)

                # State 1: Holding a long position
                # Option 1: Do nothing (carry over from previous day's dp[t][1])
                # Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
                dp[t][1] = max(dp[t][1], dp[t-1][0] - price)

                # State 2: Holding a short position
                # Option 1: Do nothing (carry over from previous day's dp[t][2])
                # Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
                dp[t][2] = max(dp[t][2], dp[t-1][0] + price)

        # The maximum profit is the maximum value in dp[t][0] for all t from 0 to k.
        # dp[0][0] is always 0, representing no transactions and no profit.
        # If all transactions result in losses, the max profit could be 0.
        max_profit = 0
        for t in range(k + 1):
            max_profit = max(max_profit, dp[t][0])

        return max_profit
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        # dp[t][0]: max profit with t transactions completed, no open position
        # dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
        # dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

        dp = [[0] * 3 for _ in range(k + 1)]

        for t in range(k + 1):
            dp[t][1] = -math.inf
            dp[t][2] = -math.inf

        # Iterate through each price
        for price in prices:
            # Iterate transactions from k down to 1
            # This order ensures that dp[t-1][0] refers to the value from the previous day
            # (or previous iteration of the outer loop)
            for t in range(k, 0, -1):
                # State 0: No open position
                # Option 1: Do nothing (carry over from previous day's dp[t][0])
                # Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
                # Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
                dp[t][0] = max(dp[t][0], dp[t][1] + price, dp[t][2] - price)

                # State 1: Holding a long position
                # Option 1: Do nothing (carry over from previous day's dp[t][1])
                # Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
                dp[t][1] = max(dp[t][1], dp[t-1][0] - price)

                # State 2: Holding a short position
                # Option 1: Do nothing (carry over from previous day's dp[t][2])
                # Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
                dp[t][2] = max(dp[t][2], dp[t-1][0] + price)

        # The maximum profit is the maximum value in dp[t][0] for all t from 0 to k.
        # dp[0][0] is always 0, representing no transactions and no profit.
        # If all transactions result in losses, the max profit could be 0.
        max_profit = 0
        for t in range(k + 1):
            max_profit = max(max_profit, dp[t][0])

        return max_profit
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Helper function for max of three long long values
long long max3(long long a, long long b, long long c) {
    long long res = a;
    if (b > res) res = b;
    if (c > res) res = c;
    return res;
}

// Helper function for max of two long long values
long long max2(long long a, long long b) {
    return a > b ? a : b;
}

long long maximumProfit(int* prices, int pricesSize, int k) {
    // dp[t][0]: max profit with t transactions completed, no open position
    // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
    // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

    long long** dp = (long long**)malloc((k + 1) * sizeof(long long*));
    for (int t = 0; t <= k; ++t) {
        dp[t] = (long long*)malloc(3 * sizeof(long long));
        dp[t][0] = 0; // 0 profit with 0 transactions completed and no open position
        dp[t][1] = LLONG_MIN / 2; // Use LLONG_MIN / 2 to prevent overflow when adding/subtracting prices
        dp[t][2] = LLONG_MIN / 2; // Use LLONG_MIN / 2 to prevent overflow when adding/subtracting prices
    }

    for (int i = 0; i < pricesSize; ++i) {
        int price = prices[i];
        for (int t = k; t >= 1; --t) {
            // State 0: No open position
            // Option 1: Do nothing (carry over from previous day's dp[t][0])
            // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
            // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
            dp[t][0] = max3(dp[t][0], dp[t][1] + price, dp[t][2] - price);

            // State 1: Holding a long position
            // Option 1: Do nothing (carry over from previous day's dp[t][1])
            // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
            dp[t][1] = max2(dp[t][1], dp[t-1][0] - price);

            // State 2: Holding a short position
            // Option 1: Do nothing (carry over from previous day's dp[t][2])
            // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
            dp[t][2] = max2(dp[t][2], dp[t-1][0] + price);
        }
    }

    long long max_profit = 0;
    for (int t = 0; t <= k; ++t) {
        max_profit = max2(max_profit, dp[t][0]);
    }

    // Free allocated memory
    for (int t = 0; t <= k; ++t) {
        free(dp[t]);
    }
    free(dp);

    return max_profit;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public long MaximumProfit(int[] prices, int k) {
        int n = prices.Length;

        // dp[t][0]: max profit with t transactions completed, no open position
        // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
        // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

        long[][] dp = new long[k + 1][3];

        for (int t = 0; t <= k; ++t) {
            dp[t][0] = 0; // 0 profit with 0 transactions completed and no open position
            dp[t][1] = long.MinValue / 2; // Use long.MinValue / 2 to prevent overflow when adding/subtracting prices
            dp[t][2] = long.MinValue / 2; // Use long.MinValue / 2 to prevent overflow when adding/subtracting prices
        }

        foreach (int price in prices) {
            for (int t = k; t >= 1; --t) {
                // State 0: No open position
                // Option 1: Do nothing (carry over from previous day's dp[t][0])
                // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
                // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
                dp[t][0] = Math.Max(dp[t][0], Math.Max(dp[t][1] + price, dp[t][2] - price));

                // State 1: Holding a long position
                // Option 1: Do nothing (carry over from previous day's dp[t][1])
                // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
                dp[t][1] = Math.Max(dp[t][1], dp[t-1][0] - price);

                // State 2: Holding a short position
                // Option 1: Do nothing (carry over from previous day's dp[t][2])
                // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
                dp[t][2] = Math.Max(dp[t][2], dp[t-1][0] + price);
            }
        }

        long maxProfit = 0;
        for (int t = 0; t <= k; ++t) {
            maxProfit = Math.Max(maxProfit, dp[t][0]);
        }

        return maxProfit;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} prices
 * @param {number} k
 * @return {number}
 */
var maximumProfit = function(prices, k) {
    const n = prices.length;

    // dp[t][0]: max profit with t transactions completed, no open position
    // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
    // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

    const dp = Array(k + 1).fill(0).map(() => Array(3).fill(0));

    for (let t = 0; t <= k; ++t) {
        dp[t][0] = 0; // 0 profit with 0 transactions completed and no open position
        dp[t][1] = -Infinity; // Cannot hold stock without buying
        dp[t][2] = -Infinity; // Cannot hold short without selling
    }

    for (const price of prices) {
        for (let t = k; t >= 1; --t) {
            // State 0: No open position
            // Option 1: Do nothing (carry over from previous day's dp[t][0])
            // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
            // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
            dp[t][0] = Math.max(dp[t][0], dp[t][1] + price, dp[t][2] - price);

            // State 1: Holding a long position
            // Option 1: Do nothing (carry over from previous day's dp[t][1])
            // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
            dp[t][1] = Math.max(dp[t][1], dp[t-1][0] - price);

            // State 2: Holding a short position
            // Option 1: Do nothing (carry over from previous day's dp[t][2])
            // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
            dp[t][2] = Math.max(dp[t][2], dp[t-1][0] + price);
        }
    }

    let maxProfit = 0;
    for (let t = 0; t <= k; ++t) {
        maxProfit = Math.max(maxProfit, dp[t][0]);
    }

    return maxProfit;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximumProfit(prices: number[], k: number): number {
    const n = prices.length;

    // dp[t][0]: max profit with t transactions completed, no open position
    // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
    // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

    const dp: number[][] = Array(k + 1).fill(0).map(() => Array(3).fill(0));

    for (let t = 0; t <= k; ++t) {
        dp[t][0] = 0; // 0 profit with 0 transactions completed and no open position
        dp[t][1] = -Infinity; // Cannot hold stock without buying
        dp[t][2] = -Infinity; // Cannot hold short without selling
    }

    for (const price of prices) {
        for (let t = k; t >= 1; --t) {
            // State 0: No open position
            // Option 1: Do nothing (carry over from previous day's dp[t][0])
            // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
            // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
            dp[t][0] = Math.max(dp[t][0], dp[t][1] + price, dp[t][2] - price);

            // State 1: Holding a long position
            // Option 1: Do nothing (carry over from previous day's dp[t][1])
            // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
            dp[t][1] = Math.max(dp[t][1], dp[t-1][0] - price);

            // State 2: Holding a short position
            // Option 1: Do nothing (carry over from previous day's dp[t][2])
            // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
            dp[t][2] = Math.max(dp[t][2], dp[t-1][0] + price);
        }
    }

    let maxProfit = 0;
    for (let t = 0; t <= k; ++t) {
        maxProfit = Math.max(maxProfit, dp[t][0]);
    }

    return maxProfit;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param Integer[] $prices
     * @param Integer $k
     * @return Integer
     */
    function maximumProfit($prices, $k) {
        $n = count($prices);

        // dp[t][0]: max profit with t transactions completed, no open position
        // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
        // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

        $dp = array_fill(0, $k + 1, array_fill(0, 3, 0));

        for ($t = 0; $t <= $k; ++$t) {
            $dp[$t][0] = 0; // 0 profit with 0 transactions completed and no open position
            $dp[$t][1] = -PHP_INT_MAX / 2; // Use / 2 to prevent overflow when adding/subtracting prices
            $dp[$t][2] = -PHP_INT_MAX / 2; // Use / 2 to prevent overflow when adding/subtracting prices
        }

        foreach ($prices as $price) {
            for ($t = $k; $t >= 1; --$t) {
                // State 0: No open position
                // Option 1: Do nothing (carry over from previous day's dp[t][0])
                // Option 2: Sell a long position ($dp[$t][1] + $price). This completes the t-th transaction.
                // Option 3: Buy back a short position ($dp[$t][2] - $price). This completes the t-th transaction.
                $dp[$t][0] = max($dp[$t][0], $dp[$t][1] + $price, $dp[$t][2] - $price);

                // State 1: Holding a long position
                // Option 1: Do nothing (carry over from previous day's dp[$t][1])
                // Option 2: Buy a stock ($dp[$t-1][0] - $price). This starts the t-th transaction.
                $dp[$t][1] = max($dp[$t][1], $dp[$t-1][0] - $price);

                // State 2: Holding a short position
                // Option 1: Do nothing (carry over from previous day's dp[$t][2])
                // Option 2: Short sell a stock ($dp[$t-1][0] + $price). This starts the t-th transaction.
                $dp[$t][2] = max($dp[$t][2], $dp[$t-1][0] + $price);
            }
        }

        $maxProfit = 0;
        for ($t = 0; $t <= $k; ++$t) {
            $maxProfit = max($maxProfit, $dp[$t][0]);
        }

        return $maxProfit;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func maximumProfit(_ prices: [Int], _ k: Int) -> Int {
        let n = prices.count

        // dp[t][0]: max profit with t transactions completed, no open position
        // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
        // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

        var dp = Array(repeating: Array(repeating: 0, count: 3), count: k + 1)

        for t in 0...k {
            dp[t][0] = 0 // 0 profit with 0 transactions completed and no open position
            dp[t][1] = Int.min / 2 // Use Int.min / 2 to prevent overflow when adding/subtracting prices
            dp[t][2] = Int.min / 2 // Use Int.min / 2 to prevent overflow when adding/subtracting prices
        }

        for price in prices {
            for t in (1...k).reversed() {
                // State 0: No open position
                // Option 1: Do nothing (carry over from previous day's dp[t][0])
                // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
                // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
                dp[t][0] = max(dp[t][0], dp[t][1] + price, dp[t][2] - price)

                // State 1: Holding a long position
                // Option 1: Do nothing (carry over from previous day's dp[t][1])
                // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
                dp[t][1] = max(dp[t][1], dp[t-1][0] - price)

                // State 2: Holding a short position
                // Option 1: Do nothing (carry over from previous day's dp[t][2])
                // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
                dp[t][2] = max(dp[t][2], dp[t-1][0] + price)
            }
        }

        var maxProfit = 0
        for t in 0...k {
            maxProfit = max(maxProfit, dp[t][0])
        }

        return maxProfit
    }

    private func max(_ a: Int, _ b: Int, _ c: Int) -> Int {
        return max(a, max(b, c))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.max

class Solution {
    fun maximumProfit(prices: IntArray, k: Int): Long {
        val n = prices.size

        // dp[t][0]: max profit with t transactions completed, no open position
        // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
        // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

        val dp = Array(k + 1) { LongArray(3) }

        for (t in 0..k) {
            dp[t][0] = 0L // 0 profit with 0 transactions completed and no open position
            dp[t][1] = Long.MIN_VALUE / 2 // Use Long.MIN_VALUE / 2 to prevent overflow when adding/subtracting prices
            dp[t][2] = Long.MIN_VALUE / 2 // Use Long.MIN_VALUE / 2 to prevent overflow when adding/subtracting prices
        }

        for (price in prices) {
            for (t in k downTo 1) {
                // State 0: No open position
                // Option 1: Do nothing (carry over from previous day's dp[t][0])
                // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
                // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
                dp[t][0] = max(dp[t][0], max(dp[t][1] + price, dp[t][2] - price))

                // State 1: Holding a long position
                // Option 1: Do nothing (carry over from previous day's dp[t][1])
                // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
                dp[t][1] = max(dp[t][1], dp[t-1][0] - price)

                // State 2: Holding a short position
                // Option 1: Do nothing (carry over from previous day's dp[t][2])
                // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
                dp[t][2] = max(dp[t][2], dp[t-1][0] + price)
            }
        }

        var maxProfit = 0L
        for (t in 0..k) {
            maxProfit = max(maxProfit, dp[t][0])
        }

        return maxProfit
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int maximumProfit(List<int> prices, int k) {
    final n = prices.length;

    // dp[t][0]: max profit with t transactions completed, no open position
    // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
    // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

    final dp = List.generate(k + 1, (_) => List<int>.filled(3, 0));

    for (int t = 0; t <= k; ++t) {
      dp[t][0] = 0; // 0 profit with 0 transactions completed and no open position
      dp[t][1] = -1000000000000000000; // A sufficiently small negative number (larger than -2^53 for JS compatibility)
      dp[t][2] = -1000000000000000000; // A sufficiently small negative number
    }

    for (final price in prices) {
      for (int t = k; t >= 1; --t) {
        // State 0: No open position
        // Option 1: Do nothing (carry over from previous day's dp[t][0])
        // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
        // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
        dp[t][0] = max(dp[t][0], max(dp[t][1] + price, dp[t][2] - price));

        // State 1: Holding a long position
        // Option 1: Do nothing (carry over from previous day's dp[t][1])
        // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
        dp[t][1] = max(dp[t][1], dp[t-1][0] - price);

        // State 2: Holding a short position
        // Option 1: Do nothing (carry over from previous day's dp[t][2])
        // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
        dp[t][2] = max(dp[t][2], dp[t-1][0] + price);
      }
    }

    int maxProfit = 0;
    for (int t = 0; t <= k; ++t) {
      maxProfit = max(maxProfit, dp[t][0]);
    }

    return maxProfit;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"math"
)

func maximumProfit(prices []int, k int) int {
    n := len(prices)

    // dp[t][0]: max profit with t transactions completed, no open position
    // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
    // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

    dp := make([][]int, k + 1)
    for t := 0; t <= k; t++ {
        dp[t] = make([]int, 3)
        dp[t][0] = 0 // 0 profit with 0 transactions completed and no open position
        dp[t][1] = math.MinInt64 / 2 // Use / 2 to prevent overflow when adding/subtracting prices
        dp[t][2] = math.MinInt64 / 2 // Use / 2 to prevent overflow when adding/subtracting prices
    }

    for _, price := range prices {
        for t := k; t >= 1; t-- {
            // State 0: No open position
            // Option 1: Do nothing (carry over from previous day's dp[t][0])
            // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
            // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
            dp[t][0] = max(dp[t][0], max(dp[t][1] + price, dp[t][2] - price))

            // State 1: Holding a long position
            // Option 1: Do nothing (carry over from previous day's dp[t][1])
            // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
            dp[t][1] = max(dp[t][1], dp[t-1][0] - price)

            // State 2: Holding a short position
            // Option 1: Do nothing (carry over from previous day's dp[t][2])
            // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
            dp[t][2] = max(dp[t][2], dp[t-1][0] + price)
        }
    }

    maxProfit := 0
    for t := 0; t <= k; t++ {
        maxProfit = max(maxProfit, dp[t][0])
    }

    return maxProfit
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def maximum_profit(prices, k)
    n = prices.length

    # dp[t][0]: max profit with t transactions completed, no open position
    # dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
    # dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

    dp = Array.new(k + 1) { Array.new(3) }

    (0..k).each do |t|
        dp[t][0] = 0 # 0 profit with 0 transactions completed and no open position
        dp[t][1] = -Float::INFINITY # Cannot hold stock without buying
        dp[t][2] = -Float::INFINITY # Cannot hold short without selling
    end

    prices.each do |price|
        k.downto(1) do |t|
            # State 0: No open position
            # Option 1: Do nothing (carry over from previous day's dp[t][0])
            # Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
            # Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
            dp[t][0] = [dp[t][0], dp[t][1] + price, dp[t][2] - price].max

            # State 1: Holding a long position
            # Option 1: Do nothing (carry over from previous day's dp[t][1])
            # Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
            dp[t][1] = [dp[t][1], dp[t-1][0] - price].max

            # State 2: Holding a short position
            # Option 1: Do nothing (carry over from previous day's dp[t][2])
            # Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
            dp[t][2] = [dp[t][2], dp[t-1][0] + price].max
        end
    end

    max_profit = 0
    (0..k).each do |t|
        max_profit = [max_profit, dp[t][0]].max
    end

    return max_profit
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.math.max

object Solution {
    def maximumProfit(prices: Array[Int], k: Int): Long = {
        val n = prices.length

        // dp(t)(0): max profit with t transactions completed, no open position
        // dp(t)(1): max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
        // dp(t)(2): max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

        val dp = Array.ofDim[Long](k + 1, 3)

        for (t <- 0 to k) {
            dp(t)(0) = 0L // 0 profit with 0 transactions completed and no open position
            dp(t)(1) = Long.MinValue / 2 // Use Long.MinValue / 2 to prevent overflow when adding/subtracting prices
            dp(t)(2) = Long.MinValue / 2 // Use Long.MinValue / 2 to prevent overflow when adding/subtracting prices
        }

        for (price <- prices) {
            for (t <- k to 1 by -1) {
                // State 0: No open position
                // Option 1: Do nothing (carry over from previous day's dp(t)(0))
                // Option 2: Sell a long position (dp(t)(1) + price). This completes the t-th transaction.
                // Option 3: Buy back a short position (dp(t)(2) - price). This completes the t-th transaction.
                dp(t)(0) = max(dp(t)(0), max(dp(t)(1) + price, dp(t)(2) - price))

                // State 1: Holding a long position
                // Option 1: Do nothing (carry over from previous day's dp(t)(1))
                // Option 2: Buy a stock (dp(t-1)(0) - price). This starts the t-th transaction.
                dp(t)(1) = max(dp(t)(1), dp(t-1)(0) - price)

                // State 2: Holding a short position
                // Option 1: Do nothing (carry over from previous day's dp(t)(2))
                // Option 2: Short sell a stock (dp(t-1)(0) + price). This starts the t-th transaction.
                dp(t)(2) = max(dp(t)(2), dp(t-1)(0) + price)
            }
        }

        var maxProfit = 0L
        for (t <- 0 to k) {
            maxProfit = max(maxProfit, dp(t)(0))
        }

        maxProfit
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::cmp::max;

impl Solution {
    pub fn maximum_profit(prices: Vec<i32>, k: i32) -> i32 {
        let n = prices.len();
        let k = k as usize;

        // dp[t][0]: max profit with t transactions completed, no open position
        // dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
        // dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

        let mut dp: Vec<Vec<i64>> = vec![vec![0; 3]; k + 1];

        for t in 0..=k {
            dp[t][0] = 0; // 0 profit with 0 transactions completed and no open position
            dp[t][1] = i64::MIN / 2; // Use / 2 to prevent overflow when adding/subtracting prices
            dp[t][2] = i64::MIN / 2; // Use / 2 to prevent overflow when adding/subtracting prices
        }

        for price_i32 in prices {
            let price = price_i32 as i64;
            for t in (1..=k).rev() {
                // State 0: No open position
                // Option 1: Do nothing (carry over from previous day's dp[t][0])
                // Option 2: Sell a long position (dp[t][1] + price). This completes the t-th transaction.
                // Option 3: Buy back a short position (dp[t][2] - price). This completes the t-th transaction.
                dp[t][0] = max(dp[t][0], max(dp[t][1] + price, dp[t][2] - price));

                // State 1: Holding a long position
                // Option 1: Do nothing (carry over from previous day's dp[t][1])
                // Option 2: Buy a stock (dp[t-1][0] - price). This starts the t-th transaction.
                dp[t][1] = max(dp[t][1], dp[t-1][0] - price);

                // State 2: Holding a short position
                // Option 1: Do nothing (carry over from previous day's dp[t][2])
                // Option 2: Short sell a stock (dp[t-1][0] + price). This starts the t-th transaction.
                dp[t][2] = max(dp[t][2], dp[t-1][0] + price);
            }
        }

        let mut max_profit = 0;
        for t in 0..=k {
            max_profit = max(max_profit, dp[t][0]);
        }

        max_profit as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(provide (struct-out Solution) (struct-out List) (struct-out Integer) (struct-out Double))

(define-struct Solution ())

(define (maximumProfit self prices k)
  (define n (vector-length prices))

  ;; dp[t][0]: max profit with t transactions completed, no open position
  ;; dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
  ;; dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

  (define dp (build-vector (+ k 1) (lambda (t) (vector 0 -inf.0 -inf.0))))

  (for ([price (in-vector prices)])
    (for ([t (in-range k 0 -1)])
      (vector-set! (vector-ref dp t) 0
                   (max (vector-ref (vector-ref dp t) 0)
                        (+ (vector-ref (vector-ref dp t) 1) price)
                        (- (vector-ref (vector-ref dp t) 2) price)))

      (vector-set! (vector-ref dp t) 1
                   (max (vector-ref (vector-ref dp t) 1)
                        (- (vector-ref (vector-ref dp (- t 1)) 0) price)))

      (vector-set! (vector-ref dp t) 2
                   (max (vector-ref (vector-ref dp t) 2)
                        (+ (vector-ref (vector-ref dp (- t 1)) 0) price)))))

  (define max-profit 0)
  (for ([t (in-range (+ k 1))])
    (set! max-profit (max max-profit (vector-ref (vector-ref dp t) 0))))

  max-profit)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([maximum_profit/2]).

maximum_profit(Prices, K) ->
    N = length(Prices),

    % dp[t][0]: max profit with t transactions completed, no open position
    % dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
    % dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

    % Initialize dp table
    % dp[t][0] = 0 for all t (0 profit with 0 transactions)
    % dp[t][1] = -infinity (cannot hold stock without buying)
    % dp[t][2] = -infinity (cannot hold short without selling)

    % Using a list of lists for dp table. Each inner list is [dp[t][0], dp[t][1], dp[t][2]]
    InitialDP = lists:duplicate(K + 1, [0, -9223372036854775807 div 2, -9223372036854775807 div 2]), % Use / 2 to prevent overflow

    FinalDP = lists:foldl(
        fun(Price, CurrentDP) ->
            lists:foldl(
                fun(T, AccDP) ->
                    % Get previous day's values for current T
                    [Prev_dp_t_0, Prev_dp_t_1, Prev_dp_t_2] = lists:nth(T + 1, AccDP),

                    % Get previous day's values for T-1
                    [Prev_dp_t_minus_1_0, _, _] = lists:nth(T, AccDP),

                    % State 0: No open position
                    New_dp_t_0 = max(Prev_dp_t_0, max(Prev_dp_t_1 + Price, Prev_dp_t_2 - Price)),

                    % State 1: Holding a long position
                    New_dp_t_1 = max(Prev_dp_t_1, Prev_dp_t_minus_1_0 - Price),

                    % State 2: Holding a short position
                    New_dp_t_2 = max(Prev_dp_t_2, Prev_dp_t_minus_1_0 + Price),

                    % Update AccDP for current T
                    lists:replace_nth(T + 1, [New_dp_t_0, New_dp_t_1, New_dp_t_2], AccDP)
                end, CurrentDP, lists:seq(K, 1, -1))
        end, InitialDP, Prices
    ),

    MaxProfit = lists:foldl(
        fun(T_dp_values, CurrentMax) ->
            max(CurrentMax, hd(T_dp_values)) % dp[t][0] is the first element
        end, 0, FinalDP
    ),

    MaxProfit.

% Helper function for max of two values
max(A, B) when A > B -> A;
max(A, B) -> B.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_profit(prices :: [integer], k :: integer) :: integer
  def maximum_profit(prices, k) do
    # dp[t][0]: max profit with t transactions completed, no open position
    # dp[t][1]: max profit with t-1 transactions completed, currently holding a long position (will be t-th transaction)
    # dp[t][2]: max profit with t-1 transactions completed, currently holding a short position (will be t-th transaction)

    # Initialize dp table
    # dp[t][0] = 0 for all t (0 profit with 0 transactions)
    # dp[t][1] = -infinity (cannot hold stock without buying)
    # dp[t][2] = -infinity (cannot hold short without selling)

    # Using a list of lists for dp table. Each inner list is {dp[t][0], dp[t][1], dp[t][2]}
    # Using a large negative number for -infinity, e.g., -10^18
    initial_dp = Enum.map(0..k, fn _ -> {0, -1_000_000_000_000_000_000, -1_000_000_000_000_000_000} end)

    final_dp = Enum.reduce(prices, initial_dp, fn price, current_dp ->
      Enum.reduce(k..1, current_dp, fn t, acc_dp ->
        # Get previous day's values for current T
        {prev_dp_t_0, prev_dp_t_1, prev_dp_t_2} = Enum.at(acc_dp, t)

        # Get previous day's values for T-1
        {prev_dp_t_minus_1_0, _, _} = Enum.at(acc_dp, t - 1)

        # State 0: No open position
        new_dp_t_0 = max(prev_dp_t_0, max(prev_dp_t_1 + price, prev_dp_t_2 - price))

        # State 1: Holding a long position
        new_dp_t_1 = max(prev_dp_t_1, prev_dp_t_minus_1_0 - price)

        # State 2: Holding a short position
        new_dp_t_2 = max(prev_dp_t_2, prev_dp_t_minus_1_0 + price)

        # Update acc_dp for current T
        List.replace_at(acc_dp, t, {new_dp_t_0, new_dp_t_1, new_dp_t_2})
      end)
    end)

    max_profit = Enum.reduce(final_dp, 0, fn {t_dp_0, _, _}, current_max ->
      max(current_max, t_dp_0)
    end)

    max_profit
  end

  defp max(a, b) when a > b, do: a
  defp max(a, b), do: b
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N * k), where N is the number of days (length of `prices` array) and k is the maximum number of transactions allowed. We iterate through each day's price, and for each price, we iterate through `k` possible transaction counts. Each DP state update takes constant time.

- **Space Complexity:** The space complexity is O(k). The DP table `dp` has dimensions `(k+1) x 3`. Since the current day's DP values only depend on the previous day's values, we can optimize space to only store the states for the current and previous day. By iterating the transaction count `t` downwards, we can achieve O(k) space using a single DP table.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-17 02:08:06 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. We need to keep track of the maximum profit we can get after a certain number of transactions. We can use a 2D array to store the maximum profit after each transaction. The key intuition is that we can either choose to make a transaction on the current day or not. If we choose to make a transaction, we need to consider whether we are buying or selling the stock. We can use two variables to keep track of the maximum profit when we are holding the stock and when we are not holding the stock. We can update these variables based on the current price and the previous maximum profit.

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
class Solution {
public:
    int maxProfit(vector<int>& prices, int k) {
        int n = prices.size();
        if (n < 2) return 0;
        k = min(k, n / 2);
        vector<vector<int>> buy(n, vector<int>(k + 1, 0));
        vector<vector<int>> sell(n, vector<int>(k + 1, 0));
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i]);
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);
            }
        }
        return sell[n - 1][k];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxProfit(int[] prices, int k) {
        int n = prices.length;
        if (n < 2) return 0;
        k = Math.min(k, n / 2);
        int[][] buy = new int[n][k + 1];
        int[][] sell = new int[n][k + 1];
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                buy[i][j] = Math.max(buy[i - 1][j], sell[i - 1][j] - prices[i]);
                sell[i][j] = Math.max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);
            }
        }
        return sell[n - 1][k];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2: return 0
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]
        for i in range(1, n):
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])
        return sell[n - 1][k]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2: return 0
        k = min(k, n // 2)
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]
        for i in range(1, n):
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])
        return sell[n - 1][k]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int* arr;
    int size;
} Array;

int maxProfit(int* prices, int pricesSize, int k) {
    if (pricesSize < 2) return 0;
    k = k < pricesSize / 2 ? k : pricesSize / 2;
    int** buy = (int**)malloc(sizeof(int*) * pricesSize);
    int** sell = (int**)malloc(sizeof(int*) * pricesSize);
    for (int i = 0; i < pricesSize; i++) {
        buy[i] = (int*)malloc(sizeof(int) * (k + 1));
        sell[i] = (int*)malloc(sizeof(int) * (k + 1));
    }
    for (int i = 1; i < pricesSize; i++) {
        for (int j = 1; j <= k; j++) {
            buy[i][j] = (buy[i - 1][j] > sell[i - 1][j] - prices[i]) ? buy[i - 1][j] : sell[i - 1][j] - prices[i];
            sell[i][j] = (sell[i - 1][j] > buy[i - 1][j - 1] + prices[i]) ? sell[i - 1][j] : buy[i - 1][j - 1] + prices[i];
        }
    }
    int result = sell[pricesSize - 1][k];
    for (int i = 0; i < pricesSize; i++) {
        free(buy[i]);
        free(sell[i]);
    }
    free(buy);
    free(sell);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxProfit(int[] prices, int k) {
        int n = prices.Length;
        if (n < 2) return 0;
        k = Math.Min(k, n / 2);
        int[][] buy = new int[n][];
        int[][] sell = new int[n][];
        for (int i = 0; i < n; i++) {
            buy[i] = new int[k + 1];
            sell[i] = new int[k + 1];
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                buy[i][j] = Math.Max(buy[i - 1][j], sell[i - 1][j] - prices[i]);
                sell[i][j] = Math.Max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);
            }
        }
        return sell[n - 1][k];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxProfit = function(prices, k) {
    let n = prices.length;
    if (n < 2) return 0;
    k = Math.min(k, Math.floor(n / 2));
    let buy = Array(n).fill(0).map(() => Array(k + 1).fill(0));
    let sell = Array(n).fill(0).map(() => Array(k + 1).fill(0));
    for (let i = 1; i < n; i++) {
        for (let j = 1; j <= k; j++) {
            buy[i][j] = Math.max(buy[i - 1][j], sell[i - 1][j] - prices[i]);
            sell[i][j] = Math.max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);
        }
    }
    return sell[n - 1][k];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxProfit(prices: number[], k: number): number {
    let n: number = prices.length;
    if (n < 2) return 0;
    k = Math.min(k, Math.floor(n / 2));
    let buy: number[][] = Array(n).fill(0).map(() => Array(k + 1).fill(0));
    let sell: number[][] = Array(n).fill(0).map(() => Array(k + 1).fill(0));
    for (let i: number = 1; i < n; i++) {
        for (let j: number = 1; j <= k; j++) {
            buy[i][j] = Math.max(buy[i - 1][j], sell[i - 1][j] - prices[i]);
            sell[i][j] = Math.max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);
        }
    }
    return sell[n - 1][k];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxProfit($prices, $k) {
        $n = count($prices);
        if ($n < 2) return 0;
        $k = min($k, floor($n / 2));
        $buy = array_fill(0, $n, array_fill(0, $k + 1, 0));
        $sell = array_fill(0, $n, array_fill(0, $k + 1, 0));
        for ($i = 1; $i < $n; $i++) {
            for ($j = 1; $j <= $k; $j++) {
                $buy[$i][$j] = max($buy[$i - 1][$j], $sell[$i - 1][$j] - $prices[$i]);
                $sell[$i][$j] = max($sell[$i - 1][$j], $buy[$i - 1][$j - 1] + $prices[$i]);
            }
        }
        return $sell[$n - 1][$k];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxProfit(_ prices: [Int], _ k: Int) -> Int {
        let n = prices.count
        if n < 2 { return 0 }
        let k = min(k, n / 2)
        var buy: [[Int]] = Array(repeating: Array(repeating: 0, count: k + 1), count: n)
        var sell: [[Int]] = Array(repeating: Array(repeating: 0, count: k + 1), count: n)
        for i in 1..<n {
            for j in 1...k {
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])
            }
        }
        return sell[n - 1][k]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxProfit(prices: IntArray, k: Int): Int {
        val n = prices.size
        if (n < 2) return 0
        val k = minOf(k, n / 2)
        val buy = Array(n) { IntArray(k + 1) }
        val sell = Array(n) { IntArray(k + 1) }
        for (i in 1 until n) {
            for (j in 1..k) {
                buy[i][j] = maxOf(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = maxOf(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])
            }
        }
        return sell[n - 1][k]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int maxProfit(List<int> prices, int k) {
        int n = prices.length;
        if (n < 2) return 0;
        k = k < n ~/ 2 ? k : n ~/ 2;
        List<List<int>> buy = List.generate(n, (i) => List.generate(k + 1, (j) => 0));
        List<List<int>> sell = List.generate(n, (i) => List.generate(k + 1, (j) => 0));
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i]);
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i]);
            }
        }
        return sell[n - 1][k];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxProfit(prices []int, k int) int {
    n := len(prices)
    if n < 2 {
        return 0
    }
    k = min(k, n/2)
    buy := make([][]int, n)
    sell := make([][]int, n)
    for i := range buy {
        buy[i] = make([]int, k+1)
        sell[i] = make([]int, k+1)
    }
    for i := 1; i < n; i++ {
        for j := 1; j <= k; j++ {
            buy[i][j] = max(buy[i-1][j], sell[i-1][j]-prices[i])
            sell[i][j] = max(sell[i-1][j], buy[i-1][j-1]+prices[i])
        }
    }
    return sell[n-1][k]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def max_profit(prices, k)
        n = prices.size
        return 0 if n < 2
        k = [k, n / 2].min
        buy = Array.new(n) { Array.new(k + 1, 0) }
        sell = Array.new(n) { Array.new(k + 1, 0) }
        (1...n).each do |i|
            (1..k).each do |j|
                buy[i][j] = [buy[i - 1][j], sell[i - 1][j] - prices[i]].max
                sell[i][j] = [sell[i - 1][j], buy[i - 1][j - 1] + prices[i]].max
            end
        end
        sell[n - 1][k]
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxProfit(prices: Array[Int], k: Int): Int = {
        val n = prices.length
        if (n < 2) return 0
        val k1 = Math.min(k, n / 2)
        val buy = Array.ofDim[Int](n, k1 + 1)
        val sell = Array.ofDim[Int](n, k1 + 1)
        for (i <- 1 until n) {
            for (j <- 1 to k1) {
                buy(i)(j) = Math.max(buy(i - 1)(j), sell(i - 1)(j) - prices(i))
                sell(i)(j) = Math.max(sell(i - 1)(j), buy(i - 1)(j - 1) + prices(i))
            }
        }
        sell(n - 1)(k1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;
impl Solution {
    pub fn max_profit(prices: Vec<i32>, k: i32) -> i32 {
        let n = prices.len();
        if n < 2 {
            return 0;
        }
        let k = k.min(n as i32 / 2);
        let mut buy: Vec<Vec<i32>> = vec![vec![0; k as usize + 1]; n];
        let mut sell: Vec<Vec<i32>> = vec![vec![0; k as usize + 1]; n];
        for i in 1..n {
            for j in 1..=k as usize {
                buy[i][j] = buy[i - 1][j].max(sell[i - 1][j] - prices[i]);
                sell[i][j] = sell[i - 1][j].max(buy[i - 1][j - 1] + prices[i]);
            }
        }
        sell[n - 1][k as usize]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (max-profit prices k)
    (let* ((n (length prices))
           (k (min k (quotient n 2))))
        (if (< n 2)
            0
            (let loop ((i 1) (buy (make-list n (make-list (+ k 1) 0))) (sell (make-list n (make-list (+ k 1) 0))))
                (if (= i n)
                    (list-ref (list-ref sell (- n 1)) k)
                    (loop (+ i 1)
                          (for/list ((j (range 1 (+ k 1))))
                              (max (list-ref (list-ref buy (- i 1)) j)
                                   (- (list-ref (list-ref sell (- i 1)) j) (list-ref prices i))))
                          (for/list ((j (range 1 (+ k 1))))
                              (max (list-ref (list-ref sell (- i 1)) j)
                                   (+ (list-ref (list-ref buy (- i 1)) (- j 1)) (list-ref prices i))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_profit(Prices, K) ->
    N = length(Prices),
    K1 = min(K, N div 2),
    Buy = array:new(N, {default, array:new(K1 + 1, {default, 0})}),
    Sell = array:new(N, {default, array:new(K1 + 1, {default, 0})}),
    max_profit(N - 1, Prices, K1, Buy, Sell).

max_profit(0, _, _, Buy, Sell) ->
    array:get(0, array:get(array:size(Buy) - 1, Sell));
max_profit(I, Prices, K, Buy, Sell) ->
    NewBuy = array:set(I, array:map(fun(J) -> max(array:get(I - 1, array:get(J, Buy)), array:get(I - 1, array:get(J, Sell)) - element(I + 1, Prices)) end, array:get(I, Buy)), Buy),
    NewSell = array:set(I, array:map(fun(J) -> max(array:get(I - 1, array:get(J, Sell)), array:get(I - 1, array:get(J - 1, Buy)) + element(I + 1, Prices)) end, array:get(I, Sell)), Sell),
    max_profit(I - 1, Prices, K, NewBuy, NewSell).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def max_profit(prices, k) do
        n = length(prices)
        if n < 2 do
            0
        else
            k = min(k, div(n, 2))
            buy = Array.new(n, fn -> Array.new(k + 1, 0) end)
            sell = Array.new(n, fn -> Array.new(k + 1, 0) end)
            max_profit(1, n - 1, prices, k, buy, sell)
        end
    end

    defp max_profit(n, n, _, _, buy, sell) do
        Array.get(sell, n, 0)
    end

    defp max_profit(i, n, prices, k, buy, sell) do
        buy = Array.update!(buy, i, fn x ->
            Enum.map(1..k, fn j ->
                max(Enum.at(x, j - 1), Enum.at(Enum.at(sell, i - 1, []), j - 1) - Enum.at(prices, i))
            end)
        end)

        sell = Array.update!(sell, i, fn x ->
            Enum.map(1..k, fn j ->
                max(Enum.at(x, j - 1), Enum.at(Enum.at(buy, i - 1, []), j - 2) + Enum.at(prices, i))
            end)
        end)

        max_profit(i + 1, n, prices, k, buy, sell)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n*k) where n is the number of days and k is the number of transactions. This is because we need to iterate over each day and each transaction to update the maximum profit.

- **Space Complexity:** The space complexity of the solution is O(n*k) where n is the number of days and k is the number of transactions. This is because we need to store the maximum profit after each transaction for each day.

</div>
</details>
