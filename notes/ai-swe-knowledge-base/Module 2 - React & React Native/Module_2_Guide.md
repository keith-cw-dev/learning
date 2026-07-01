# Module 2 – React & React Native Engineering

## Goal

Develop a comprehensive understanding of React and React Native, enabling you to build maintainable applications, diagnose rendering and state issues, optimize performance, evaluate AI-generated React code, and confidently explain engineering decisions.

## Learning Objectives

*By the end of this module, you should be able to:*

-   Explain React's rendering lifecycle.
-   Predict component rendering behavior.
-   Manage local, shared, and server state appropriately.
-   Build reusable, composable components.
-   Optimize React and React Native applications.
-   Debug rendering, hooks, navigation, and state issues.
-   Evaluate AI-generated React code for correctness, maintainability, and performance.
-   Explain React concepts clearly in writing and verbally.

## Part 1: Study Guide

### Topic 1 – React Philosophy & Component Architecture

#### Concepts

-   Declarative UI
-   Component-based architecture
-   Composition over inheritance
-   Single Responsibility Principle
-   Separation of concerns
-   Presentational vs Container components
-   Controlled vs Uncontrolled components

#### Mental Model

Think of components as LEGO bricks.

-   Small.
-   Reusable.
-   Predictable.
-   Composable.

#### Common Mistakes

-   Building components that do too much.
-   Overusing props.
-   Copying state.
-   Premature abstraction.

#### Evaluator Note

*AI often produces giant React components instead of breaking logic into reusable pieces.*

### Topic 2 – JSX & Rendering

#### Study

-   JSX compilation
-   Rendering expressions
-   Conditional rendering
-   Lists
-   Keys
-   Fragments
-   Component lifecycle (functional perspective)

#### Common Misconceptions

-   Keys improve performance everywhere.
-   Changing state always re-renders the whole application.

### Topic 3 – React State

#### Study

-   useState
-   Functional updates
-   Derived state
-   Lifting state
-   State colocation
-   Immutable updates

*Practice explaining why mutating state prevents predictable rendering.*

### Topic 4 – React Hooks

#### Cover

-   useState
-   useEffect
-   useMemo
-   useCallback
-   useRef
-   useContext
-   Custom Hooks
-   Rules of Hooks

#### Understand

-   Why hooks exist.
-   Why call order matters.

### Topic 5 – Effects

#### Learn

-   Side effects
-   Dependency arrays
-   Cleanup functions
-   Stale closures
-   Infinite render loops
-   Fetching data
-   Synchronization

### Topic 6 – React Rendering & Performance

#### Topics

-   Reconciliation
-   Virtual DOM
-   Fiber (high-level)
-   Render phase
-   Commit phase
-   React.memo
-   Memoization
-   Lazy loading
-   Code splitting
-   Suspense (overview)

### Topic 7 – React Native

#### Study

-   Expo architecture
-   Native components
-   Flexbox
-   Styling
-   NativeWind
-   Platform differences
-   Gesture handling
-   Keyboard handling
-   Safe areas
-   Device APIs

### Topic 8 – Navigation & State Management

#### Topics

-   React Navigation
-   Stack navigation
-   Tabs
-   Deep linking
-   Context
-   Redux overview
-   Zustand overview
-   React Query
-   Server state vs client state

#### Evaluator Note

*Many AI models incorrectly recommend Redux for problems better solved with Context or React Query.*

### Topic 9 – Forms & Validation

#### Study

-   Controlled forms
-   Uncontrolled forms
-   Validation
-   Async validation
-   Form libraries
-   Error handling

### Topic 10 – Accessibility

#### Topics

-   Semantic components
-   Screen readers
-   Accessibility labels
-   Focus management
-   Touch targets
-   Color contrast

## Part 2: Recommended Videos

#### React Fundamentals

1 - Web Dev Simplified – React Course
2 - Web Dev Simplified – React Hooks Explained
3 - Fireship – React in 100 Seconds
4 - Jack Herrington – React Performance
5 - ThePrimeagen – React Rants (tradeoffs and architecture)
6 - Theo Browne – Building Scalable React Apps

#### React Native

7 - Expo Official Tutorials
8 - William Candillon – React Native animations and architecture
9 - React Native Official Documentation walkthroughs
10 - notJust.dev – React Native projects
11 - Code with Beto – Expo + React Native patterns

#### React Query

12 - Tanner Linsley presentations
13 - Jack Herrington – React Query Deep Dive

#### Recommended Deep Dive

Use the React documentation as your primary reference after learning the basics. It explains modern React concepts and the reasoning behind recommended patterns better than almost any video course.

## Part 3: Coding Exercises

-   Build a reusable Button component.
-   Create a reusable Modal.
-   Build a searchable list using state.
-   Implement a Todo application.
-   Build a custom useDebounce hook.
-   Create a custom useFetch hook.
-   Optimize a slow-rendering component.
-   Implement infinite scrolling with React Query.
-   Build a theme provider.
-   Create a multi-step form.

### Each exercise should include:

-   Time complexity (where applicable)
-   Render considerations
-   Edge cases
-   Accessibility review
-   Refactoring opportunities

## Part 4: Debugging Lab

Examples include:

-   Why is this component re-rendering endlessly?
-   Why isn't useEffect firing?
-   Why is useEffect firing too often?
-   Why is state stale inside this callback?
-   Why is useMemo not improving performance?
-   Why does this FlatList lag?
-   Why isn't navigation updating correctly?
-   Why is Context causing unnecessary renders?
-   Why isn't React Query refetching?
-   Why is this custom hook violating the Rules of Hooks?

## Part 5: AI Evaluation Scenarios

You'll compare AI-generated React solutions.

Example:

Prompt: "Optimize this React component."

Model A:

Wraps everything in useMemo and useCallback.

Model B:

Identifies the expensive computation, memoizes only that portion, and explains why.

Tasks:

-   Choose the better solution.
-   Identify unnecessary optimizations.
-   Discuss readability.
-   Evaluate maintainability.
-   Score correctness, performance, clarity, and instruction following.

Additional scenarios include:

-   Choosing between Context and React Query.
-   Reviewing React Native layouts.
-   Evaluating accessibility improvements.
-   Identifying stale closure bugs.
-   Reviewing custom hooks.
-   Assessing component architecture.

## Part 6: Speaking Practice

Examples:

-   Explain React rendering in under 90 seconds.
-   Explain reconciliation to a junior developer.
-   Describe the Virtual DOM without using buzzwords.
-   Explain why React state should be treated as immutable.
-   Teach useEffect using a real-world analogy.
-   Explain when to use Context versus React Query.
-   Explain why React.memo isn't a universal optimization.
-   Describe the Rules of Hooks and why they exist.

Aim for clear, conversational explanations suitable for video interviews, technical presentations, or live coding streams.

## Part 7: 50-Question Assessment

We'll end the module with a balanced assessment:

### Questions 1–15: Conceptual Understanding

-   React architecture
-   Rendering
-   Hooks
-   State
-   Effects
-   React Native fundamentals

### Questions 16–25: Code Reading and Output Prediction

-   Render order
-   Hook behavior
-   Dependency arrays
-   Memoization
-   Navigation
-   Context updates

### Questions 26–35: Debugging and Bug Fixing

-   Infinite render loops
-   Stale closures
-   Performance bottlenecks
-   React Native layout issues
-   State synchronization
-   Hook misuse

### Questions 36–45: Component Design and Implementation

-   Build reusable components
-   Refactor code
-   Optimize rendering
-   Design custom hooks
-   Choose appropriate state management
-   Improve accessibility

### Questions 46–50: AI Evaluation Scenarios

Examples:

-   Compare two React implementations and justify which is more maintainable.
-   Review an AI-generated custom hook for correctness and edge cases.
-   Evaluate a React Native screen for performance, accessibility, and code quality.
-   Assess competing state management approaches for a medium-sized application.
-   Write professional evaluator feedback for an AI-generated pull request.

Each question will include a detailed solution, discussion of common misconceptions, explanations of tempting but incorrect answers, and guidance on what a strong AI evaluator should notice beyond simple correctness.
