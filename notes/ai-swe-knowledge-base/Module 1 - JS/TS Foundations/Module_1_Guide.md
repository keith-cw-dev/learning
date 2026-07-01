#  Module 1 – JavaScript & TypeScript Foundations

## Goal: Build a deep understanding of JavaScript and TypeScript, develop the ability to debug and reason about code, and learn to evaluate AI-generated explanations and implementations.

## Learning Objectives

*By the end of this module, you should be able to:*

-   Explain JavaScript execution and memory concepts.
-   Predict the behavior of unfamiliar code.
-   Identify subtle bugs and code smells.
-   Evaluate competing implementations of the same solution.
-   Use TypeScript to express intent and improve maintainability.
-   Clearly explain technical concepts in writing and aloud.

## Part 1: Study Guide

### Topic 1 – Variables and Memory

#### Concepts

-   Primitive vs. reference types
-   Stack vs. heap (conceptual model)
-   var, let, const
-   Temporal Dead Zone
-   Reassignment vs. mutation
-   Pass-by-value vs. sharing object references
-   Mental Model

*Think of variables as labels pointing to values. Primitive values are copied; objects are referenced through shared pointers.*

#### Common Mistakes

-   Assuming const makes an object immutable
-   Accidentally mutating shared objects
-   Using var inside loops
-   Evaluator Note

*AI models often incorrectly claim "const makes objects immutable." Your job is to recognize that only the binding is immutable, not the object's contents.*

### Topic 2 – Scope & Closures

#### Study:

-   Lexical scope
Function scope
Block scope
Closure creation
Lifetime of captured variables
Practical uses (event handlers, memoization, factories)

#### Common misconceptions:

Closures copy variables (they don't)
Closures are slow by default (usually not)

### Topic 3 – The this Keyword

#### Study:

Default binding
Implicit binding
Explicit binding (call, apply, bind)
Constructor binding
Arrow function behavior

Practice explaining why arrow functions don't have their own this.

### Topic 4 – Functions

#### Cover:

Function declarations
Function expressions
Arrow functions
Higher-order functions
Callbacks
Pure vs. impure functions
Currying (intro)

### Topic 5 – Objects & Prototypes

#### Learn:

Object literals
Prototype chain
Inheritance
Object.create
class syntax vs. prototypes
Property lookup

### Topic 6 – Asynchronous JavaScript

#### Topics:

-   Event loop
-   Call stack
-   Web APIs
-   Microtasks
-   Macrotasks
-   Promises
-   async / await
-   Error handling
-   Promise.all
-   Promise.allSettled
-   Promise.any
-   Promise.race

### Topic 7 – Modules

#### Study:

-   ES Modules
-   Named exports
-   Default exports
-   Tree shaking
-   Circular dependencies (overview)

### Topic 8 – TypeScript

#### Topics:

-   Primitive types
-   Interfaces
-   Type aliases
-   Unions
-   Intersections
-   Generics
-   Utility types
-   Enums (and why many teams avoid them)
-   unknown
-   never
-   any
-   Type narrowing
-   Discriminated unions

## Part 2: Recommended Videos

#### Recommended Order:

JavaScript Fundamentals

1 - Web Dev Simplified – JavaScript Crash Course
2 - Fireship – JavaScript in 100 Seconds (quick refresher)
3 - Kyle Simpson – Scope & Closures (from You Don't Know JS)
4 - *!*Akshay Saini – Namaste JavaScript (Execution Context, Hoisting, Event Loop)
5 - ThePrimeagen – Closures, Event Loop, and JavaScript internals
6 - Jack Herrington – Modern JavaScript patterns

TypeScript

7 - Theo Browne – Why TypeScript Matters
8 - Matt Pocock – TypeScript for Beginners
9 - *!*Web Dev Simplified – TypeScript Full Course

I recommend Akshay Saini's "Namaste JavaScript" series as your primary deep dive. It's one of the best free resources for understanding why JavaScript behaves the way it does.

## Part 3: Coding Exercises

-   Implement your own map().
-   Implement your own filter().
-   Implement your own reduce().
-   Write a debounce function.
-   Write a throttle function.
-   Build a memoization helper.
-   Deep clone an object without structuredClone.
-   Flatten a nested array.
-   Group objects by property.
-   Implement a simple event emitter.

### Each exercise should include:

Time complexity
Space complexity
Edge cases
Refactoring opportunities

## Part 4: Debugging Lab

Examples include:

Why does this closure return the wrong value?
Why is this async function hanging?
Why is this undefined?
Why is this Promise never resolving?
Why does TypeScript infer never here?
Why did this destructuring assignment fail?
Why did this mutation affect another object?
Why is this generic too restrictive?
Why does this union type not narrow?
Why is this module causing a circular dependency?

## Part 5: AI Evaluation Scenarios

You'll compare AI-generated answers.

Example:

Prompt: "Explain closures."

Model A:

A closure is a copy of local variables...

Model B:

A closure is a function that retains access to variables from its lexical scope even after the outer function has returned.

Tasks:

Choose the better response.
Identify factual inaccuracies.
Suggest improvements.
Assign scores for correctness, completeness, clarity, and usefulness.

## Part 6: Speaking Practice

Examples:

Explain hoisting in under 90 seconds.
Explain lexical scope to a junior developer.
Teach promises without using technical jargon.
Explain why const doesn't make objects immutable.
Explain the event loop using a restaurant analogy.
Describe when to choose an interface versus a type alias.

Aim for concise, conversational explanations—the same style you'd use in a video assessment or on stream.

## Part 7: 50-Question Assessment

We'll end the module with a balanced assessment:

Questions 1–15: Conceptual understanding (multiple choice and short answer)
Questions 16–25: Code reading and output prediction
Questions 26–35: Debugging and bug fixing
Questions 36–45: TypeScript design and implementation
Questions 46–50: AI evaluation scenarios requiring written justification

Each question will come with a detailed solution, explanations of common misconceptions, and discussion of why incorrect options are tempting.