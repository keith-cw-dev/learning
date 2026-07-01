# Module 3 – Backend Engineering (Node.js, APIs, Auth, Systems Thinking)

## Goal

Develop the ability to design, implement, debug, and evaluate backend systems using Node.js and Express, with strong understanding of APIs, authentication, data flow, and production-grade reliability.

## Learning Objectives

*By the end of this module, you should be able to:*

-   Design RESTful APIs with correct structure and conventions.
-   Build secure authentication systems (sessions, JWT, OAuth concepts).
-   Debug backend failures and asynchronous issues.
-   Reason about data flow between client, server, and database.
-   Evaluate AI-generated backend code for correctness and security.
-   Identify scalability and maintainability issues in API design.
-   Explain backend systems clearly in writing and speech.

## Part 1: Study Guide

### Topic 1 – Node.js Runtime Fundamentals

#### Concepts

-   Event loop (server-side perspective)
-   Single-threaded execution model
-   libuv thread pool
-   Blocking vs non-blocking operations
-   Streams vs buffers
-   Process lifecycle

#### Mental Model

Node.js is a request orchestrator, not a worker.

It delegates heavy tasks and coordinates async work rather than executing everything directly.

#### Common Mistakes

-   Writing blocking CPU-heavy code in request handlers
-   Assuming Node handles concurrency via threads by default
-   Ignoring backpressure in streams

#### Evaluator Note

*AI models often incorrectly describe Node.js as "multi-threaded by default."*

### Topic 2 – Express.js Fundamentals

#### Concepts

-   Middleware chain
-   Request / response lifecycle
-   Routing
-   Error handling middleware
-   Async route handlers
-   Separation of concerns

#### Mental Model

Express is a pipeline of transformations:

Request → middleware → route → response

#### Common Mistakes

-   Forgetting next(err)
-   Not handling async errors properly
-   Mixing business logic in route handlers

#### Evaluator Note

*Many AI-generated APIs fail to properly structure middleware or error handling.*

### Topic 3 – REST API Design

#### Concepts

-   Resource-based design
-   HTTP methods (GET, POST, PUT, PATCH, DELETE)
-   Status codes
-   Idempotency
-   Pagination
-   Filtering & querying

#### Mental Model

REST APIs model nouns, not verbs:

-   /users
-   /jobs
-   /applications

#### Common Mistakes

-   Using POST for everything
-   Returning 200 for all errors
-   Poor endpoint naming
-   Overloaded endpoints

### Topic 4 – Authentication & Authorization

#### Concepts

-   Sessions vs JWT
-   Cookies (httpOnly, secure, sameSite)
-   Password hashing (scrypt, bcrypt)
-   OAuth (conceptual overview)
-   Role-based access control (RBAC)
-   Token expiration & refresh flows

#### Mental Model

Authentication = who you are
Authorization = what you can do

#### Common Mistakes

-   Storing plain JWTs without expiration logic
-   Putting sensitive data in tokens
-   Confusing authentication with authorization

#### Evaluator Note

*AI models often incorrectly suggest JWTs as a universal best solution.*

### Topic 5 – Databases & Data Flow

#### Concepts

-   SQL vs NoSQL tradeoffs
-   Schema design
-   Indexing basics
-   Joins
-   Transactions
-   ORM vs raw queries (Drizzle, Prisma concepts)
-   Connection pooling

#### Mental Model

Database = system of truth, not just storage.

#### Common Mistakes

-   Missing indexes on query-heavy columns
-   Over-fetching data
-   N+1 query problems
-   Poor schema normalization

### Topic 6 – Error Handling & Reliability

#### Concepts

-   Try/catch boundaries
-   Centralized error middleware
-   Logging strategies
-   Graceful failure
-   Retry logic
-   Idempotency in APIs

#### Evaluator Note

*A large percentage of AI-generated backend code fails due to missing or inconsistent error handling.*

### Topic 7 – WebSockets & Real-Time Systems

#### Concepts

-   HTTP vs WebSocket
-   Socket.IO lifecycle
-   Rooms / channels
-   Event-driven communication
-   Scaling real-time systems (conceptual)

#### Common Mistakes

-   Not handling disconnects
-   Memory leaks from listeners
-   Assuming WebSockets are stateless

### Topic 8 – Security Fundamentals

#### Concepts

-   Input validation
-   SQL injection prevention
-   XSS (backend awareness)
-   Rate limiting
-   CORS
-   Secure headers
-   Environment variables

#### Mental Model

Security = assume every input is hostile

### Topic 9 – API Architecture

#### Concepts

-   Monolith vs modular architecture
-   Service separation
-   Controllers / services / repositories
-   Dependency injection (light conceptual)
-   Feature-based folder structure

### Topic 10 – Performance & Scaling (Intro Level)

#### Concepts

-   Caching (Redis conceptually)
-   Horizontal scaling
-   Load balancing
-   Stateless services
-   Bottleneck identification

## Part 2: Recommended Videos

#### Node & Backend Fundamentals

1 - Web Dev Simplified – Node.js Crash Course
2 - Fireship – Node.js in 100 Seconds
3 - ThePrimeagen – Backend architecture discussions
4 - Hussein Nasser – Backend engineering deep dives (VERY valuable)
5 - freeCodeCamp – REST API & Express full courses
6 - Traversy Media – Express.js crash course

#### Authentication & Security

7 - Hussein Nasser – JWT vs Sessions (critical watch)
8 - Web Dev Simplified – Authentication systems explained
9 - OWASP Foundation videos (basic concepts)

#### Databases

10 - Fireship – SQL vs NoSQL
11 - Prisma / Drizzle documentation walkthroughs
12 - Hussein Nasser – Database indexing & query optimization

#### System Thinking

13 - Gaurav Sen – system design basics (light intro level)
14 - ByteByteGo (high-level system intuition)

## Part 3: Coding Exercises

-   Build a REST API for a todo system
-   Implement authentication with sessions
-   Implement JWT-based authentication
-   Build middleware logger
-   Implement rate limiter
-   Create file upload endpoint
-   Build CRUD API with validation
-   Implement pagination and filtering
-   Create WebSocket chat server
-   Build error-handling middleware

### Each exercise includes:

-   API design quality
-   Error handling
-   Security considerations
-   Performance concerns
-   Code organization

## Part 4: Debugging Lab

Examples include:

-   Why is this API route never hit?
-   Why is authentication failing intermittently?
-   Why are sessions not persisting?
-   Why is JWT verification failing?
-   Why is this middleware blocking all requests?
-   Why is this database query slow?
-   Why are WebSocket events duplicating?
-   Why is CORS blocking valid requests?
-   Why is this async route crashing silently?
-   Why is this transaction not committing?

## Part 5: AI Evaluation Scenarios

You will compare backend implementations.

Example:

Prompt: "Build a login API."

Model A:

Stores passwords in plaintext (incorrect)

Model B:

Uses hashing, sessions, proper error handling, validation

Tasks:

-   Identify security flaws
-   Evaluate correctness
-   Check API design quality
-   Assess scalability
-   Score clarity and maintainability

Additional scenarios:

-   JWT vs session tradeoffs
-   REST API design evaluation
-   Database schema review
-   WebSocket implementation critique
-   Middleware chain evaluation
-   Error handling completeness
-   Rate limiting design

## Part 6: Speaking Practice

Examples:

-   Explain how Express middleware works in 90 seconds
-   Describe session vs JWT authentication
-   Explain how a REST API should be structured
-   Teach database indexing to a junior developer
-   Explain why blocking code hurts Node.js performance
-   Describe how WebSockets differ from HTTP
-   Explain how you would secure a login endpoint
-   Walk through how a request travels through a backend system

Focus: clear, structured explanation without jargon overload.

## Part 7: 50-Question Assessment

### Questions 1–15: Conceptual Understanding

Topics:

-   Node runtime
-   Express fundamentals
-   REST design
-   Authentication basics
-   Databases
-   Security fundamentals

### Questions 16–25: Code Reading & Output Prediction

-   Middleware flow
-   Async behavior
-   JWT/session logic
-   API responses
-   Error propagation

### Questions 26–35: Debugging & Bug Fixing

-   Broken authentication flows
-   Middleware errors
-   Database issues
-   WebSocket bugs
-   Race conditions

### Questions 36–45: API Design & Implementation

-   Design REST APIs
-   Implement endpoints
-   Structure backend architecture
-   Add validation & security
-   Improve performance

### Questions 46–50: AI Evaluation Scenarios

Examples:

-   Compare two login API implementations
-   Evaluate REST API design quality
-   Review AI-generated backend code for security flaws
-   Assess database schema design
-   Write evaluator feedback for backend correctness and production readiness

Each includes:

-   Correct solution
-   Common misconceptions
-   Why wrong answers are tempting
-   What strong evaluators notice beyond correctness
