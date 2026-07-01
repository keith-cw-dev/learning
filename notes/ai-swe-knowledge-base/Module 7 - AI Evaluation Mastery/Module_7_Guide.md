# Module 7 – AI Evaluation Mastery (Code, Reasoning & System Review)

## Goal

Develop the ability to evaluate AI-generated software engineering output with professional rigor, including correctness, reasoning quality, edge cases, security, performance, and communication clarity.

This module simulates real evaluator work.

## Learning Objectives

*By the end of this module, you should be able to:*

-   Evaluate whether AI-generated code is correct or subtly incorrect
-   Compare multiple model outputs and choose the best one
-   Detect hallucinated APIs or incorrect assumptions
-   Assess reasoning quality, not just final answers
-   Identify security, scalability, and maintainability issues
-   Score responses using structured criteria
-   Write clear evaluator justifications
-   Simulate real Outlier / Mercor / Alignerr task formats

## Part 1: Study Guide

### Topic 1 – What "Good" AI Output Actually Means

#### Criteria

When evaluating AI output, you are not only checking correctness.

You evaluate:

-   Correctness
-   Completeness
-   Instruction following
-   Reasoning quality
-   Efficiency
-   Safety/security
-   Maintainability
-   Clarity of explanation

#### Mental Model

You are not a developer.

You are a peer reviewer for an AI system under training.

### Topic 2 – Types of AI Failure

#### 1. Subtle Logical Errors

Code runs, but produces wrong results.

#### 2. Overconfident Hallucination

Example:

"React has a built-in useServerData hook."

#### 3. Partial Solutions

Correct idea, missing edge cases.

#### 4. Overengineering

Unnecessary complexity or abstraction.

#### 5. Misaligned Instruction Following

Ignores constraints or simplifies incorrectly.

### Topic 3 – Evaluation Framework

For every response, evaluate:

#### 1. Correctness

Does it work?

#### 2. Reasoning

Does explanation match implementation?

#### 3. Edge Cases

Does it break under real conditions?

#### 4. Efficiency

Is it appropriately optimized?

#### 5. Clarity

Would another engineer understand it?

### Topic 4 – Code vs Explanation Consistency

One of the most important evaluator skills:

Does the explanation actually match what the code does?

AI often:

-   explains one thing
-   implements another

### Topic 5 – Comparative Evaluation

You will frequently compare:

-   Model A vs Model B
-   Simple vs complex solution
-   Correct vs partially correct
-   Efficient vs brute force

You must justify:

-   Why one is better, not just which one is correct

### Topic 6 – Security & Production Awareness

You must detect:

-   SQL injection risks
-   Insecure authentication logic
-   Exposed secrets
-   Unsafe deserialization
-   Missing validation

Even in "toy" code.

### Topic 7 – Realistic Expectations vs AI Behavior

AI tends to:

-   Assume ideal inputs
-   Ignore latency
-   Skip validation
-   Overuse frameworks
-   Under-handle errors

You must detect this gap.

## Part 2: Recommended Videos

There are fewer "direct evaluator training videos," so this is more curated thinking:

#### Evaluation Mindset

1 - Andrej Karpathy – system thinking, model behavior intuition
2 - Lex Fridman – discussions on AI evaluation and reasoning limits
3 - ThePrimeagen – code review mindset and tradeoffs

#### Code Review Thinking

4 - "Code Review Best Practices" talks (various engineering channels)
5 - ByteByteGo – system correctness intuition
6 - Hussein Nasser – failure modes in backend systems

#### Critical Thinking

7 - MIT lectures on reasoning systems (select segments)
8 - Debugging-focused engineering talks

## Part 3: Evaluation Practice Sets

### Set 1 – Correctness Checks

You are given AI-generated code.

Tasks:

-   Does it work?
-   What inputs break it?
-   Is the logic complete?
-   Are there hidden assumptions?

### Set 2 – Comparative Analysis

Model A vs Model B:

-   Which is more correct?
-   Which is more maintainable?
-   Which handles edge cases better?
-   Which is easier to debug?

### Set 3 – Explanation Audit

Given:

-   code
-   explanation

Check:

-   Does explanation match code?
-   Are there missing steps?
-   Is terminology correct?
-   Is anything misleading?

### Set 4 – Hallucination Detection

Find:

-   Fake APIs
-   Incorrect framework features
-   Outdated behavior claims
-   Invented library methods

### Set 5 – Production Readiness

Evaluate:

-   Error handling
-   Logging
-   Scalability
-   Security
-   Maintainability

## Part 4: Debugging Evaluation Lab

Examples include:

-   Why is this AI solution logically incorrect but syntactically valid?
-   Why does this "optimized" solution break edge cases?
-   Why is this explanation misleading?
-   Why is this API design unsafe?
-   Why does this response violate instructions?
-   Why is this complexity analysis wrong?
-   Why is this solution overengineered?
-   Why is this missing critical validation?
-   Why does this comparison favor the worse solution?
-   Why is this security assumption invalid?

## Part 5: AI Evaluation Scenarios (Core Practice)

### Scenario 1 – Code Correctness

Prompt: "Write a debounce function"

Model A:

missing edge case for immediate execution

Model B:

correct debounce with cancellation logic

Tasks:

-   Choose winner
-   Justify
-   Identify failure cases

### Scenario 2 – Explanation Quality

Prompt: "Explain closures"

Model A:

vague, partially incorrect

Model B:

precise, but overly technical

Tasks:

-   Choose best for junior developer
-   Explain why clarity matters

### Scenario 3 – Security Review

Prompt: "Build login API"

Model A:

plaintext passwords

Model B:

hashed passwords, session handling, validation

Tasks:

-   Identify security risks
-   Evaluate completeness
-   Score severity

### Scenario 4 – Architecture Tradeoff

Prompt: "Design a chat system backend"

Model A:

monolithic, simple

Model B:

overengineered microservices

Tasks:

-   Evaluate correctness vs complexity
-   Choose appropriate solution
-   Justify tradeoffs

### Scenario 5 – Instruction Following

Prompt: "Return a function only, no explanation"

Model outputs explanation anyway

Tasks:

-   Evaluate compliance
-   Assess penalty severity
-   Explain why instruction following matters

## Part 6: Speaking Practice

Examples:

-   Explain how you evaluate AI code in 60–90 seconds
-   Describe how to detect hallucinated APIs
-   Explain what makes a good code review
-   Teach how you decide between two correct answers
-   Explain why correctness alone is not enough
-   Walk through evaluating a backend API
-   Describe how you handle ambiguous outputs

Focus: structured reasoning, not verbosity.

## Part 7: 50-Question Assessment

This is the capstone.

### Questions 1–10: Correctness Evaluation

-   Is the code correct?
-   What breaks it?
-   What assumptions are wrong?

### Questions 11–20: Comparative Evaluation

-   Model A vs Model B
-   Tradeoffs
-   Reasoning quality
-   Maintainability

### Questions 21–30: Explanation Audits

-   Does explanation match code?
-   Clarity evaluation
-   Missing reasoning steps
-   Misleading statements

### Questions 31–40: Production & Security

-   Identify security flaws
-   Evaluate scalability
-   Detect missing validation
-   Assess error handling

### Questions 41–50: Full Evaluator Simulation

Realistic tasks:

-   Score AI responses
-   Justify rankings
-   Write evaluator feedback
-   Detect hallucinations
-   Choose best model output under constraints

Each includes:

-   Ideal answer
-   Scoring rubric
-   Common evaluator mistakes
-   What strong evaluators notice
