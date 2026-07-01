# Java – Interview Study Guide

_Styled like the sample: Beginner → Intermediate → Advanced; concise answers._

## Beginner Level
**1. What are JDK, JRE, and JVM?**
JDK is the development kit, JRE runs Java apps, and JVM executes bytecode on a given platform.

**2. Explain Java’s ‘Write Once, Run Anywhere’.**
Java compiles to platform‑independent bytecode executed by a JVM on each OS/arch.

**3. List Java primitive types.**
byte, short, int, long, float, double, char, boolean.

**4. Stack vs heap in Java?**
Stack holds frames and local primitives; heap stores objects/arrays managed by GC.

**5. What is autoboxing/unboxing?**
Automatic conversion between primitives and their wrapper types (int ↔ Integer).

**6. String vs StringBuilder vs StringBuffer?**
String is immutable; StringBuilder mutable non‑thread‑safe; StringBuffer mutable synchronized.

**7. == vs equals()?**
== compares references for objects; equals() compares logical equality when overridden.

**8. hashCode() contract?**
Equal objects must have equal hash codes; must be consistent with equals().

**9. What is a package and a module?**
Package groups classes; module (Java 9+) groups packages with exports/requires in module‑info.java.

**10. Checked vs unchecked exceptions?**
Checked must be declared/handled; unchecked (RuntimeException) need not be.

**11. try-with-resources?**
Auto‑closes AutoCloseable resources after try block, even on exceptions.

**12. What is a classloader?**
Loads classes at runtime from classpath/modulepath; supports parent delegation.

**13. What are Generics?**
Parametric types for compile‑time type safety; erased at runtime (type erasure).

**14. Collections framework overview.**
List, Set, Queue/Deque, Map with implementations like ArrayList, HashSet, PriorityQueue, HashMap.

**15. ArrayList vs LinkedList?**
ArrayList O(1) random access, costly middle inserts; LinkedList cheap inserts, O(n) access.

**16. HashMap vs TreeMap?**
HashMap average O(1) ops, unordered; TreeMap O(log n) sorted by key.

**17. Immutability benefits?**
Thread‑safe sharing, simpler reasoning, safe caching; avoid defensive copying.

**18. final, finally, finalize?**
final keyword prevents change; finally always runs; finalize() legacy cleanup (deprecated).

**19. Stream API?**
Functional pipeline map/filter/reduce; supports parallel streams for CPU‑bound work.

**20. Optional usage?**
Represents possibly‑absent values; encourage orElse/ifPresent; avoid in fields/serialization.


## Intermediate Level
**21. volatile vs synchronized?**
volatile ensures visibility for a variable; synchronized adds mutual exclusion + visibility.

**22. Thread vs Runnable vs Callable?**
Thread is executable; Runnable.run() no return; Callable<V>.call() returns V and throws checked.

**23. ExecutorService basics?**
Thread pools manage tasks; configure core/max, queue, rejection; submit via submit/execute.

**24. Future vs CompletableFuture?**
Future blocks on get(); CompletableFuture supports composition and non‑blocking callbacks.

**25. Java Memory Model (JMM)?**
Defines happens‑before rules for visibility/ordering across threads via locks/volatile/etc.

**26. Serialization approaches?**
Built‑in Serializable (often avoided), JSON/Proto/Kryo alternatives; custom readObject/writeObject.

**27. Reflection pros/cons?**
Runtime inspection/modification; flexible but slower and less safe—use sparingly.

**28. Annotations?**
Metadata processed at compile/runtime via reflection or annotation processors.

**29. Garbage collectors types?**
Serial, Parallel, G1 (default), ZGC, Shenandoah; trade throughput vs latency.

**30. Stop‑the‑world pause?**
GC may pause app threads to mark/compact; low‑pause collectors reduce impact with concurrency.

**31. Escape analysis?**
JIT allocates non‑escaping objects on stack or removes synchronization.

**32. Class vs interface vs abstract class?**
Class has impl; interface defines contracts (default/static methods allowed); abstract class can hold state + abstract methods.

**33. record (Java 16+)?**
Compact immutable data carrier with synthesized equals/hashCode/toString.

**34. var keyword rules?**
Local type inference; not allowed for fields/method params or with bare null.

**35. Pattern matching for instanceof?**
Bind a typed variable directly after check, reducing casts and scope errors.

**36. NIO/NIO.2?**
Channels/buffers, selectors; NIO.2 adds Path/Files, async channels, filesystem APIs.

**37. Initialization order?**
Static init → instance init → constructor; super before subclass.

**38. ConcurrentModificationException cause?**
Fail‑fast iterators detect structural modification during iteration; use iterator.remove or concurrent collections.

**39. ConcurrentHashMap traits?**
Thread‑safe map with finer‑grained locking/CAS; good scalability.

**40. Creating immutable classes?**
final fields, no setters, defensive copies, class final, validate in constructor.


## Advanced Level
**41. Equality pitfalls with inheritance?**
May violate symmetry/transitivity; prefer composition or use records.

**42. BigInteger/BigDecimal?**
Arbitrary‑precision integer and decimal types; BigDecimal for money with scale/rounding modes.

**43. What is a memory leak in Java?**
Objects unintentionally reachable (static fields, caches, listeners) preventing GC.

**44. Soft/weak/phantom references?**
Different GC reachability; weak often used for caches; phantom for post‑mortem cleanup.

**45. ClassPath vs ModulePath?**
Classpath loads classes/resources; modulepath uses module metadata for reliable configuration.

**46. Deadlock and prevention?**
Threads cyclically waiting for locks; prevent with consistent lock order, timeouts, or lock striping.

**47. When to use parallel streams?**
Large, CPU‑bound, associative operations; avoid for small or IO‑bound tasks.

**48. Profiling/perf basics?**
Use JFR/JMC or async‑profiler; benchmark with JMH; measure before optimizing.

**49. Maven vs Gradle?**
Maven XML & conventions; Gradle Groovy/Kotlin DSL with build cache/incremental capabilities.
