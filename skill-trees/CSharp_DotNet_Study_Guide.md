# C# / .NET – Interview Study Guide

_Styled like the sample: Beginner → Intermediate → Advanced; concise answers._

## Beginner Level
**1. What are CLR, CTS, and CLS?**
CLR runs IL and manages memory; CTS defines types; CLS ensures cross‑language interop.

**2. Value vs reference types?**
Structs (value) vs classes (reference); boxing wraps values as objects.

**3. GC in .NET?**
Generational, compacting collector (Gen0/1/2 and LOH) with background modes.

**4. IDisposable and using?**
Dispose releases unmanaged resources; using ensures deterministic cleanup.

**5. async/await and Task?**
await non‑blocking; Task represents async work; ConfigureAwait controls context.

**6. IEnumerable vs IQueryable?**
IEnumerable executes in memory; IQueryable builds expression trees for remote execution.

**7. Delegates/events and Func/Action?**
Delegates are function types; events publish/subscribe; Func/Action generic delegates.

**8. Extension methods?**
Static methods that appear as instance methods via 'this' first parameter.

**9. Generics and constraints?**
Parametric types with where constraints for safety and specialization.

**10. Records vs classes vs structs?**
Records: reference with value‑equality; classes: reference; structs: value types.

**11. Pattern matching?**
is/switch with type, relational, and property patterns.

**12. Nullable reference types?**
Opt‑in nullability annotations and warnings to prevent NREs.

**13. Span<T>/Memory<T>?**
Low‑allocation views over memory for high‑performance APIs.

**14. Reflection and attributes?**
Runtime metadata inspection; attributes attach metadata.

**15. dynamic keyword?**
DLR‑based dynamic dispatch; use sparingly.

**16. lock/Monitor vs Mutex?**
lock is Monitor sugar; Mutex works cross‑process.

**17. TPL/Parallel/PLINQ?**
High‑level parallel patterns; avoid contention and shared state.

**18. Immutable collections?**
Persistent structures (ImmutableList/Dictionary) for thread‑safety.

**19. Serialization choices?**
System.Text.Json fast; Newtonsoft flexible; BinaryFormatter obsolete.

**20. String handling?**
Strings immutable/interned; StringBuilder for heavy concatenation.


## Intermediate Level
**21. Index and Range?**
^ and .. operators for slicing sequences.

**22. yield return iterators?**
Compiler‑generated state machines for lazy enumeration.

**23. LINQ basics/pitfalls?**
Deferred execution; materialize with ToList to avoid multiple enumeration.

**24. Default interface methods?**
Provide non‑breaking API additions in interfaces.

**25. Equality semantics?**
Override Equals/GetHashCode; IEquatable<T>; records synthesize.

**26. File‑scoped namespace?**
C# 10 reduces indentation with 'namespace X;'.

**27. Tuples and deconstruction?**
ValueTuple support with (a,b) syntax; named elements aid readability.

**28. Unsafe code/pointers?**
Enabled with 'unsafe'; necessary for interop/perf critical code.

**29. CancellationToken?**
Cooperative cancellation signaling for async operations.

**30. Stopwatch vs DateTime?**
Stopwatch for timing; DateTime for wall clock.

**31. JSON source generators?**
AOT serializers for speed and trimming‑friendly apps.

**32. Nullable<T> vs nullables on refs?**
Nullable<T> wraps value types; NRT annotates refs—separate concepts.

**33. Top‑level statements?**
Simplify small programs with implicit Main.

**34. System.IO best practices?**
Prefer async I/O; use using for streams; Path.GetTempPath etc.

**35. DateTimeOffset vs DateTime?**
DateTimeOffset represents exact instant with offset; safer for persistence.

**36. BenchmarkDotNet?**
Reliable benchmarking in Release without debugger.

**37. AOT/NativeAOT vs JIT?**
AOT compiles ahead of time; JIT at runtime; trade startup vs size/flexibility.

**38. Boxing allocations?**
Occurs converting value types to object/interface; avoid in hot paths.

**39. Memory leaks in managed code?**
Caused by unwanted references (events, caches, statics).

**40. init‑only setters?**
Immutability pattern allowing initialization only at creation.


## Advanced Level
**41. with‑expressions on records?**
Non‑destructive mutation: var b = a with {X=1}.

**42. When to use struct?**
Small, immutable value semantics; watch copying and default ctor rules.

**43. Interfaces vs abstract classes?**
Interfaces: contracts; abstract classes: shared base behavior/state.

**44. Source generators?**
Compile‑time codegen via Roslyn for boilerplate removal.

**45. Optional params vs nullables?**
Optional have default values; nullable indicates null allowed—orthogonal.

**46. Primary constructors?**
C# 12: parameters on type declaration to initialize members.

**47. Analyzers/.editorconfig?**
Enforce code style and catch issues early with Roslyn analyzers.
