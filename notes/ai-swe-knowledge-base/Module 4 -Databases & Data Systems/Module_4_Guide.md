# Module 4 – Databases, Data Modeling & System Design Foundations

## Goal

Develop strong intuition for relational databases, data modeling, query performance, and early system design thinking. Learn to evaluate AI-generated database schemas, detect inefficiencies, and reason about scalable data systems.

## Learning Objectives

*By the end of this module, you should be able to:*

-   Design normalized and practical database schemas
-   Write and reason about SQL queries confidently
-   Identify performance issues in database design
-   Understand indexing and query optimization at a conceptual level
-   Reason about consistency, transactions, and data integrity
-   Evaluate AI-generated schemas and queries for correctness
-   Explain tradeoffs between SQL and NoSQL systems
-   Think in terms of data flow across a system

## Part 1: Study Guide

### Topic 1 – Relational Database Fundamentals

#### Concepts

-   Tables, rows, columns
-   Primary keys
-   Foreign keys
-   Relationships (1–1, 1–many, many–many)
-   Constraints (NOT NULL, UNIQUE, CHECK)
-   Referential integrity

#### Mental Model

A database is not a spreadsheet—it is a structured system of relationships with rules that must never be violated.

#### Common Mistakes

-   Using no primary keys
-   Duplicating data across tables
-   Ignoring foreign key relationships
-   Treating SQL like a storage dump instead of a structured system

#### Evaluator Note

*AI models often generate schemas without proper keys or constraints, which leads to invisible data corruption risks.*

### Topic 2 – Data Normalization

#### Concepts

-   1NF, 2NF, 3NF (conceptual understanding)
-   Removing redundancy
-   Avoiding update anomalies
-   When to denormalize intentionally

#### Mental Model

Normalization = reducing "repeated truth" in a system.

#### Common Mistakes

-   Over-normalizing (too many joins, poor performance)
-   Under-normalizing (duplicate data everywhere)

### Topic 3 – SQL Fundamentals

#### Concepts

-   SELECT, INSERT, UPDATE, DELETE
-   WHERE filtering
-   ORDER BY
-   GROUP BY
-   HAVING vs WHERE
-   JOIN types (INNER, LEFT, RIGHT, FULL)

#### Mental Model

SQL is a declarative language: you describe what you want, not how to compute it.

#### Common Mistakes

-   Confusing WHERE vs HAVING
-   Misusing JOINs leading to duplicated rows
-   Forgetting NULL behavior in comparisons

### Topic 4 – Indexing & Performance

#### Concepts

-   What an index is (B-tree conceptual model)
-   When indexes help
-   When indexes hurt
-   Query planning (high-level)
-   SELECT * anti-pattern

#### Mental Model

Indexes are like a table of contents in a book.

They speed up lookup but slow down writes.

#### Common Mistakes

-   Indexing everything
-   Ignoring write performance cost
-   Not indexing frequently queried columns

#### Evaluator Note

*AI often suggests unnecessary indexes or ignores query cost entirely.*

### Topic 5 – Transactions & Consistency

#### Concepts

-   ACID properties
-   Atomicity
-   Consistency
-   Isolation
-   Durability
-   Transaction rollback
-   Isolation levels (conceptual)

#### Mental Model

A transaction is a promise that either everything happens or nothing happens.

#### Common Mistakes

-   Not using transactions for multi-step operations
-   Assuming partial updates are safe
-   Ignoring race conditions in concurrent writes

### Topic 6 – Schema Design

#### Concepts

-   Entity modeling
-   Relationships mapping
-   Junction tables (many-to-many)
-   Timestamp fields (created_at, updated_at)
-   Soft deletes vs hard deletes

#### Common Mistakes

-   Overloading tables with unrelated data
-   Not planning for future queries
-   Missing audit fields
-   Poor naming conventions

### Topic 7 – SQL vs NoSQL

#### Concepts

-   Document databases vs relational databases
-   Flexibility vs consistency tradeoff
-   Scaling models
-   Use-case driven selection

#### Mental Model

SQL = structured truth
NoSQL = flexible documents

#### Evaluator Note

*AI often incorrectly claims NoSQL is always "faster" or "better for scaling."*

### Topic 8 – Query Design Patterns

#### Concepts

-   Pagination (LIMIT/OFFSET)
-   Filtering strategies
-   Aggregation queries
-   Subqueries vs joins
-   CTEs (Common Table Expressions)

#### Common Mistakes

-   OFFSET pagination at scale
-   Overusing subqueries instead of joins
-   Inefficient aggregations

### Topic 9 – Data Consistency in Applications

#### Concepts

-   Backend ↔ database synchronization
-   Race conditions
-   Optimistic vs pessimistic updates
-   Idempotency

### Topic 10 – Intro System Design Thinking

#### Concepts

-   Data flow across services
-   Storage vs compute separation
-   Stateless services
-   Caching basics (Redis conceptual)
-   Bottlenecks

#### Mental Model

System design starts with one question:

"Where does the truth live, and how does it move?"

## Part 2: Recommended Videos

#### SQL & Databases

1 - Khan Academy – SQL Basics (foundational clarity)
2 - freeCodeCamp – SQL Full Course
3 - Fireship – SQL vs NoSQL in 100 Seconds
4 - Hussein Nasser – Database internals & indexing (VERY important)
5 - Coding With Mosh – SQL fundamentals

#### Advanced Database Thinking

6 - Hussein Nasser – Transactions & isolation levels
7 - ByteByteGo – System design fundamentals
8 - Gaurav Sen – Data-intensive systems (intro level)
9 - ThePrimeagen – Database tradeoffs discussions

#### Schema Design

10 - Web Dev Simplified – Database design basics
11 - DevOps / backend architecture talks (conceptual exposure)

## Part 3: Coding Exercises

-   Design a users + posts schema
-   Write SQL joins for a blog system
-   Implement pagination query
-   Design a many-to-many relationship (users ↔ roles)
-   Build a schema for messaging system
-   Optimize a slow query
-   Normalize a poorly designed schema
-   Write aggregation queries for analytics
-   Design audit logging tables
-   Convert SQL schema to NoSQL model (conceptual)

### Each exercise includes:

-   Schema correctness
-   Query efficiency
-   Scalability considerations
-   Data integrity checks
-   Edge cases

## Part 4: Debugging Lab

Examples include:

-   Why is this JOIN duplicating rows?
-   Why is this query slow at scale?
-   Why are inserts failing intermittently?
-   Why is data inconsistent across tables?
-   Why is this transaction partially applying?
-   Why is pagination skipping records?
-   Why is the index not being used?
-   Why is this schema causing update anomalies?
-   Why are NULL values breaking logic?
-   Why is this NoSQL model causing duplication?

## Part 5: AI Evaluation Scenarios

You will compare database designs and queries.

Example:

Prompt: "Design a database for a social media app."

Model A:

single table with nested JSON (No structure)

Model B:

normalized schema with users, posts, likes, relationships

Tasks:

-   Evaluate normalization quality
-   Check scalability
-   Identify data integrity risks
-   Assess query efficiency
-   Identify missing constraints

Additional scenarios:

-   Compare two schema designs
-   Evaluate SQL query correctness
-   Review indexing strategy
-   Identify data consistency risks
-   Evaluate NoSQL vs SQL decisions
-   Assess transaction safety

## Part 6: Speaking Practice

Examples:

-   Explain normalization in 90 seconds
-   Describe a primary key to a beginner
-   Explain why indexes speed up reads but slow writes
-   Teach JOINs using a real-world analogy
-   Explain ACID properties simply
-   Describe when you would use NoSQL over SQL
-   Walk through how a query executes conceptually
-   Explain why transactions matter in payments systems

Focus: clarity, structure, analogy-driven explanation.

## Part 7: 50-Question Assessment

### Questions 1–15: Conceptual Understanding

Topics:

-   Relational models
-   Normalization
-   SQL basics
-   Joins
-   Indexing
-   Transactions

### Questions 16–25: Query Reading & Output Prediction

-   JOIN behavior
-   Aggregation results
-   Filtering logic
-   NULL handling
-   Grouping behavior

### Questions 26–35: Debugging & Performance Issues

-   Slow queries
-   Incorrect joins
-   Missing indexes
-   Transaction bugs
-   Schema design flaws

### Questions 36–45: Schema & Query Design

-   Design database schemas
-   Write SQL queries
-   Optimize structures
-   Convert requirements into relational models
-   Fix poor schema designs

### Questions 46–50: AI Evaluation Scenarios

Examples:

-   Compare two database schemas for correctness and scalability
-   Evaluate SQL queries generated by AI
-   Review indexing decisions
-   Identify normalization issues in AI-generated designs
-   Write evaluator feedback on data integrity and system correctness

Each includes:

-   Ideal solution
-   Common misconceptions
-   Subtle failure cases
-   Evaluator reasoning expectations
