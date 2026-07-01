# Module 5 – Professional Software Engineering (Git, CI/CD, Docker, Architecture)

## Goal

Develop the ability to work like a production engineer: manage code safely, design maintainable systems, reason about deployments, debug pipeline issues, and evaluate AI-generated engineering workflows.

## Learning Objectives

*By the end of this module, you should be able to:*

-   Use Git confidently in real-world multi-developer workflows
-   Resolve merge conflicts and understand rebase vs merge tradeoffs
-   Design basic CI/CD pipelines and understand their purpose
-   Debug build, deployment, and integration failures
-   Understand containerization with Docker at a practical level
-   Evaluate system architecture decisions for maintainability and scalability
-   Identify risks in production workflows
-   Evaluate AI-generated DevOps and engineering processes

## Part 1: Study Guide

### Topic 1 – Git Fundamentals & Collaboration

#### Concepts

-   Working directory vs staging area vs repository
-   Commits as snapshots
-   Branching strategies
-   Merge vs rebase
-   Pull requests
-   Forking workflows

#### Mental Model

Git is not "saving code"—it is managing parallel timelines of reality.

#### Common Mistakes

-   Force pushing shared branches
-   Rewriting public history
-   Mixing unrelated changes in a single commit
-   Ignoring commit hygiene

#### Evaluator Note

*AI often produces unrealistic Git workflows (e.g., committing secrets, ignoring conflicts, or misusing rebase in shared branches).*

### Topic 2 – Merge Conflicts & Code Integration

#### Concepts

-   Conflict resolution
-   Three-way merge
-   Source of conflicts
-   Manual resolution strategies
-   Preventing conflicts via modular design

#### Mental Model

A merge conflict is not a failure—it is two valid histories disagreeing about the same reality.

#### Common Mistakes

-   Blindly accepting one side of a conflict
-   Losing functionality during resolution
-   Not understanding the intent of both changes

### Topic 3 – Branching Strategies

#### Concepts

-   Feature branching
-   GitFlow (conceptual)
-   Trunk-based development
-   Hotfix branches
-   Release branches

#### Evaluator Note

*AI-generated workflows often overcomplicate branching or use outdated patterns without justification.*

### Topic 4 – CI/CD Pipelines

#### Concepts

-   Continuous Integration
-   Continuous Deployment
-   Build pipelines
-   Test automation
-   Deployment stages
-   Rollbacks
-   Environment separation (dev/staging/prod)

#### Mental Model

CI/CD is a safety net that runs before humans deploy broken code to production.

#### Common Mistakes

-   No automated tests in pipeline
-   Deploying without validation
-   Mixing dev and production configs
-   Not handling rollback scenarios

### Topic 5 – Testing in Production Systems

#### Concepts

-   Unit tests
-   Integration tests
-   End-to-end tests
-   Smoke tests
-   Test pyramids (conceptual)
-   Mocking external services

#### Evaluator Note

*AI often suggests unrealistic test coverage or misclassifies test types.*

### Topic 6 – Docker & Containerization

#### Concepts

-   Containers vs virtual machines
-   Docker images vs containers
-   Dockerfile structure
-   Layer caching
-   Ports and networking
-   Environment variables

#### Mental Model

A container is a portable execution snapshot of your application environment.

#### Common Mistakes

-   Installing unnecessary dependencies in images
-   Ignoring image size
-   Misconfiguring environment variables
-   Running everything as root

### Topic 7 – Deployment Concepts

#### Concepts

-   Build → test → deploy pipeline
-   Blue-green deployment
-   Rolling deployments
-   Zero-downtime deployment (conceptual)
-   Environment parity

#### Evaluator Note

*AI frequently assumes deployments are instant and risk-free.*

### Topic 8 – Logging, Monitoring & Debugging

#### Concepts

-   Logs vs metrics vs traces
-   Structured logging
-   Error tracking
-   Observability basics
-   Debugging production issues

#### Mental Model

If you cannot observe it, you cannot fix it.

### Topic 9 – Software Architecture

#### Concepts

-   Monolith vs microservices
-   Service boundaries
-   Coupling vs cohesion
-   Modular architecture
-   Layered architecture (controller/service/repository)

#### Common Mistakes

-   Premature microservices
-   Overengineering small systems
-   Tight coupling between modules

### Topic 10 – Security in Production Systems

#### Concepts

-   Secrets management
-   Environment variables
-   API key safety
-   Dependency vulnerabilities
-   Least privilege principle

#### Evaluator Note

*AI often leaks secrets into code or ignores secure deployment practices.*

## Part 2: Recommended Videos

#### Git & Collaboration

1 - ThePrimeagen – Git explained deeply (essential)
2 - Traversy Media – Git crash course
3 - freeCodeCamp – Git and GitHub full tutorial
4 - TechWorld with Nana – Git workflows

#### CI/CD & DevOps

5 - TechWorld with Nana – CI/CD pipelines explained
6 - DevOps Directive – real-world pipelines
7 - Fireship – CI/CD in 100 seconds
8 - ByteByteGo – deployment strategies

#### Docker

9 - TechWorld with Nana – Docker tutorial series
10 - Fireship – Docker in 100 seconds
11 - Bret Fisher – Docker deep dives

#### Architecture & Systems

12 - ByteByteGo – system design fundamentals
13 - Gaurav Sen – system design basics
14 - ThePrimeagen – architecture tradeoffs discussions
15 - Hussein Nasser – backend scaling insights

## Part 3: Coding & Engineering Exercises

-   Initialize a Git repo with feature branching
-   Resolve a complex merge conflict scenario
-   Create a CI pipeline for a Node.js project
-   Write a Dockerfile for a full-stack app
-   Optimize a slow build pipeline
-   Set up environment configs for dev/staging/prod
-   Add logging middleware to an API
-   Design a modular backend architecture
-   Simulate a failed deployment and rollback
-   Refactor a monolithic backend into modules

### Each exercise includes:

-   Workflow correctness
-   Maintainability
-   Risk analysis
-   Production safety
-   Debugging readiness

## Part 4: Debugging Lab

Examples include:

-   Why did this CI pipeline fail only in production?
-   Why is Docker build caching breaking?
-   Why are environment variables undefined in deployment?
-   Why did a merge introduce a regression?
-   Why is rollback not restoring correct state?
-   Why are logs missing in production?
-   Why is this Git history corrupted?
-   Why is deployment inconsistent across environments?
-   Why are tests passing locally but failing in CI?
-   Why is the build artifact incomplete?

## Part 5: AI Evaluation Scenarios

You will evaluate engineering workflows.

Example:

Prompt: "Set up a deployment pipeline for a Node.js app."

Model A:

no tests, direct deploy to production

Model B:

CI pipeline, tests, staging, rollback strategy

Tasks:

-   Evaluate production safety
-   Check completeness of workflow
-   Identify missing safeguards
-   Assess scalability of pipeline
-   Score engineering maturity

Additional scenarios:

-   Evaluate Git workflows
-   Review CI/CD configurations
-   Assess Dockerfile correctness
-   Compare deployment strategies
-   Identify security risks in DevOps setups
-   Evaluate architecture decisions

## Part 6: Speaking Practice

Examples:

-   Explain Git merge vs rebase in 90 seconds
-   Describe a CI/CD pipeline to a junior engineer
-   Explain why Docker improves consistency
-   Teach rollback strategies simply
-   Explain monolith vs microservices tradeoffs
-   Describe what happens when code is deployed
-   Explain why logs are critical in production
-   Walk through a failed deployment scenario

Focus on clarity, structure, and real-world reasoning.

## Part 7: 50-Question Assessment

### Questions 1–15: Conceptual Understanding

Topics:

-   Git fundamentals
-   Branching strategies
-   CI/CD basics
-   Docker concepts
-   Deployment workflows

### Questions 16–25: Workflow Interpretation

-   Git history analysis
-   CI pipeline behavior
-   Docker build interpretation
-   Deployment flow reasoning
-   Merge conflict outcomes

### Questions 26–35: Debugging & Production Issues

-   Failed builds
-   Broken deployments
-   CI inconsistencies
-   Environment mismatches
-   Logging failures
-   Git mistakes causing regressions

### Questions 36–45: Architecture & Engineering Design

-   Design CI/CD pipelines
-   Structure backend repos
-   Improve deployment safety
-   Refactor monoliths
-   Design scalable workflows

### Questions 46–50: AI Evaluation Scenarios

Examples:

-   Compare two CI/CD pipeline designs
-   Evaluate Git workflows for safety and correctness
-   Review Dockerfiles for production readiness
-   Identify risks in deployment automation
-   Write evaluator feedback on engineering maturity

Each includes:

-   Correct solution
-   Hidden risks
-   Common AI mistakes
-   Production-grade reasoning expectations
