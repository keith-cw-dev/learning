# Module 6 – Algorithms & Problem Solving

## Goal

Develop strong pattern recognition and reasoning skills for algorithmic problems, with emphasis on correctness, efficiency, edge cases, and evaluating AI-generated solutions rather than just solving for LeetCode-style output.

## Learning Objectives

*By the end of this module, you should be able to:*

-   Recognize common algorithmic patterns quickly
-   Analyze time and space complexity accurately
-   Write correct solutions using arrays, maps, trees, and recursion
-   Identify subtle logical errors in code
-   Compare multiple solution approaches and justify tradeoffs
-   Detect inefficiencies in AI-generated algorithms
-   Explain reasoning clearly in both written and verbal form

## Part 1: Study Guide

### Topic 1 – Big-O Thinking & Complexity

#### Concepts

-   Time complexity (O(1), O(n), O(n²), O(log n), O(n log n))
-   Space complexity
-   Worst vs average case
-   Tradeoffs between memory and speed

#### Mental Model

Big-O is not about exact speed—it is about how performance scales as input grows.

#### Common Mistakes

-   Ignoring nested loops
-   Treating O(n²) as acceptable for large inputs
-   Confusing constant factors with complexity class

#### Evaluator Note

*AI models often incorrectly claim an algorithm is O(n) when hidden nested operations exist.*

### Topic 2 – Arrays & Strings Patterns

#### Concepts

-   Iteration patterns
-   Sliding window
-   Two pointers
-   Prefix sums
-   Frequency maps

#### Mental Model

Arrays are linear state machines you traverse and transform.

#### Common Mistakes

-   Recomputing results instead of storing state
-   Missing edge cases at boundaries
-   Incorrect pointer movement logic

### Topic 3 – Hash Maps & Sets

#### Concepts

-   Fast lookup structures
-   Deduplication
-   Counting frequency
-   Key-value modeling

#### Mental Model

Hash maps turn search problems into constant-time lookups.

#### Common Mistakes

-   Forgetting initialization checks
-   Overwriting values unintentionally
-   Assuming order exists in maps

### Topic 4 – Recursion & Backtracking

#### Concepts

-   Recursive calls
-   Base cases
-   Stack behavior
-   Backtracking pattern
-   Decision trees

#### Mental Model

Recursion is breaking a problem into smaller versions of itself until trivial cases remain.

#### Common Mistakes

-   Missing base cases
-   Stack overflow from infinite recursion
-   Not undoing state in backtracking

### Topic 5 – Sorting & Searching

#### Concepts

-   Bubble, insertion, merge, quick sort (conceptual understanding)
-   Binary search
-   Search boundaries
-   Sorted array optimizations

#### Mental Model

Sorting is about preparing structure so future queries become easier.

#### Common Mistakes

-   Off-by-one errors in binary search
-   Incorrect pivot handling
-   Assuming sorted input without verification

### Topic 6 – Trees

#### Concepts

-   Binary trees
-   BST properties
-   DFS vs BFS
-   Traversals (inorder, preorder, postorder)
-   Tree recursion patterns

#### Mental Model

Trees are hierarchical decision structures.

#### Common Mistakes

-   Confusing traversal orders
-   Not handling null nodes
-   Incorrect recursion return values

### Topic 7 – Graphs (Intro Level)

#### Concepts

-   Nodes and edges
-   Directed vs undirected graphs
-   BFS vs DFS
-   Adjacency list vs matrix
-   Visited sets

#### Mental Model

Graphs model relationships, not hierarchy.

#### Common Mistakes

-   Infinite loops due to missing visited tracking
-   Misusing BFS/DFS
-   Incorrect adjacency representation

### Topic 8 – Dynamic Programming (Intro)

#### Concepts

-   Overlapping subproblems
-   Memoization
-   Tabulation
-   State definition

#### Mental Model

DP is recursion + memory of past results.

#### Common Mistakes

-   Not defining state clearly
-   Missing memoization
-   Incorrect recurrence relations

### Topic 9 – Greedy Algorithms

#### Concepts

-   Local optimal choice
-   When greedy works
-   Counterexample thinking

#### Mental Model

Greedy works only when local decisions guarantee global optimality.

### Topic 10 – Problem Decomposition

#### Concepts

-   Breaking problems into subproblems
-   Identifying patterns
-   Constraint analysis
-   Edge case enumeration

#### Evaluator Note

*Strong AI evaluators focus more on reasoning structure than final code.*

## Part 2: Recommended Videos

#### Core Algorithms

1 - NeetCode – Algorithm patterns (HIGHLY recommended)
2 - Back To Back SWE – deep algorithm intuition
3 - freeCodeCamp – Data Structures & Algorithms full course
4 - Abdul Bari – algorithms explained clearly
5 - William Fiset – data structures deep dives

#### Intuition Building

6 - NeetCode "patterns" series
7 - William Fiset – graph theory intuition
8 - MIT OpenCourseWare – algorithms (selectively)

#### Dynamic Programming

9 - Tushar Roy – DP explanations
10 - Back To Back SWE – DP breakdowns

#### Systematic Thinking

11 - William Lin – competitive programming breakdowns (selectively useful)

## Part 3: Coding Exercises

-   Two Sum variations
-   Longest substring without repeating characters
-   Valid parentheses checker
-   Binary search variations
-   Reverse linked list
-   Detect cycle in linked list
-   Lowest common ancestor
-   Merge intervals
-   Word search (grid DFS)
-   Coin change (DP)

### Each exercise includes:

-   Time complexity
-   Space complexity
-   Edge cases
-   Alternative approaches
-   Optimization discussion

## Part 4: Debugging Lab

Examples include:

-   Why does this recursion overflow?
-   Why is this DP solution returning incorrect results?
-   Why is binary search skipping valid answers?
-   Why is DFS revisiting nodes?
-   Why is this greedy solution failing edge cases?
-   Why is this hash map logic incorrect?
-   Why is sorting breaking expected order logic?
-   Why is this solution O(n²) unexpectedly?
-   Why is memoization not working?
-   Why is this tree traversal missing nodes?

## Part 5: AI Evaluation Scenarios

You will evaluate algorithmic reasoning.

Example:

Prompt: "Find the longest palindrome substring."

Model A:

brute force O(n³)

Model B:

expands center, O(n²), optimized reasoning

Tasks:

-   Compare correctness
-   Evaluate efficiency
-   Identify missing edge cases
-   Assess reasoning clarity
-   Judge whether explanation matches implementation

Additional scenarios:

-   Compare greedy vs DP solutions
-   Evaluate recursion correctness
-   Identify hidden inefficiencies
-   Detect incorrect complexity claims
-   Evaluate AI-generated explanations of algorithms

## Part 6: Speaking Practice

Examples:

-   Explain Big-O in under 90 seconds
-   Describe binary search intuitively
-   Teach recursion without technical jargon
-   Explain DFS vs BFS using a real-world analogy
-   Describe when DP is necessary
-   Explain why greedy algorithms sometimes fail
-   Walk through solving a problem step-by-step out loud

Focus: clarity, structure, and reasoning—not memorization.

## Part 7: 50-Question Assessment

### Questions 1–15: Conceptual Understanding

Topics:

-   Complexity analysis
-   Arrays
-   Hash maps
-   Recursion
-   Trees
-   Graphs
-   DP basics

### Questions 16–25: Code Output & Tracing

-   Recursion traces
-   Pointer movement
-   Hash map behavior
-   DFS/BFS traversal results
-   DP table evolution

### Questions 26–35: Debugging & Fixing Algorithms

-   Incorrect recursion
-   Broken DP logic
-   BFS/DFS bugs
-   Binary search mistakes
-   Greedy edge case failures

### Questions 36–45: Implementation & Optimization

-   Implement common algorithms
-   Optimize naive solutions
-   Choose correct pattern
-   Refactor inefficient code
-   Explain tradeoffs

### Questions 46–50: AI Evaluation Scenarios

Examples:

-   Compare two algorithm implementations and justify correctness and efficiency
-   Evaluate AI-generated explanations of DP or recursion
-   Identify hidden complexity issues in solutions
-   Review incorrect greedy assumptions
-   Write evaluator feedback on algorithmic reasoning quality

Each includes:

-   Correct solution
-   Subtle failure cases
-   Reasoning expectations
-   Common AI mistakes
