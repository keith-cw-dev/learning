# C++ – Interview Study Guide

_Styled like the sample: Beginner → Intermediate → Advanced; concise answers._

## Beginner Level
**1. Describe the C++ build pipeline.**
Preprocessing → compile to objects → link into executable/library.

**2. Header vs source files?**
Headers declare; sources define; use include guards/#pragma once.

**3. What is undefined behavior (UB)?**
Behavior not defined by the standard; anything can happen—avoid.

**4. RAII concept?**
Tie resource lifetime to object lifetime via destructors.

**5. Stack vs heap allocation?**
Stack automatic per scope; heap dynamic via new/delete or smart pointers.

**6. Rule of three/five/zero?**
If owning resources, define copy/move/dtor; otherwise rely on RAII types.

**7. lvalue vs rvalue?**
lvalue has identity; rvalue is temporary; enables move semantics.

**8. Move semantics?**
Transfer resources from temp to target via rvalue refs and std::move.

**9. Smart pointers?**
unique_ptr, shared_ptr, weak_ptr; prefer over owning raw pointers.

**10. Const correctness?**
Use const to express immutability and enable overloads.

**11. Inline functions and ODR?**
inline allows multiple definitions; ODR permits one definition per entity.

**12. Namespaces and using?**
Organize symbols; avoid 'using namespace' in headers.

**13. Templates basics?**
Generic programming; instantiated at compile time.

**14. SFINAE and concepts?**
Select viable templates; concepts provide readable constraints (C++20).

**15. Virtual functions & polymorphism?**
Runtime dispatch via vtables; base needs virtual destructor.

**16. Object slicing?**
Copying derived to base by value drops derived parts; use references.

**17. Operator overloading?**
Define intuitive semantics; often as non‑member friends.

**18. Copy Elision/NRVO?**
Compilers elide copies; guaranteed in many cases since C++17.

**19. Exception safety levels?**
Basic, strong, no‑throw; use RAII, noexcept where appropriate.

**20. noexcept and move?**
noexcept moves enable container optimizations.


## Intermediate Level
**21. std::vector vs std::list?**
vector contiguous and fast; list stable iterators but cache‑unfriendly.

**22. Iterator invalidation?**
Know container rules; vector reallocation invalidates iterators.

**23. Algorithms vs containers?**
Use <algorithm> with iterators for reusable operations.

**24. std::array vs C array?**
std::array safer fixed‑size container with STL interface.

**25. Concurrency basics?**
std::thread, mutex, lock_guard, condition_variable; atomics for lock‑free ops.

**26. Memory orderings?**
Use default seq_cst unless measured need; understand acquire/release.

**27. Futures and async?**
std::future via std::async/promises; always join/detach threads properly.

**28. Chrono and time points?**
Strongly typed durations/time_points prevent unit bugs.

**29. I/O streams pitfalls?**
Stateful; prefer std::format (C++20) or fmt for performance.

**30. Ranges (C++20)?**
Lazy pipelines (views) with composable algorithms.

**31. Lambda captures?**
Capture by value or reference; beware dangling references.

**32. Pimpl idiom?**
Hide implementation details to reduce compile coupling and stabilize ABI.

**33. constexpr/consteval?**
Compile‑time eval; consteval requires compile‑time computation.

**34. Alignment and padding?**
Structure may have padding; use alignas carefully.

**35. Friendship?**
Grants private access; use sparingly.

**36. CRTP pattern?**
Static polymorphism via template base class taking derived type.

**37. Type erasure?**
Hide types behind uniform interface (std::any, std::function).

**38. Undefined vs unspecified vs impl‑defined?**
UB none; unspecified multiple valid; impl‑defined documented by compiler.

**39. Linker ODR violations?**
Multiple or missing definitions cause link errors.

**40. Allocators and PMR?**
Custom allocation strategies; std::pmr for polymorphic memory resources.


## Advanced Level
**41. optional/variant/any?**
Express optional values, tagged unions, and type‑erased containers.

**42. Coroutines (C++20)?**
Language support for async generators with promise types.

**43. Dangling iterators UB?**
After erase/reallocation; update iterators post‑mutation.

**44. ABI compatibility?**
Binary interfaces vary across compilers/versions; cautious with shared libs.

**45. CMake basics?**
Modern target‑based configuration; link libraries via targets.

**46. Sanitizers?**
Address/UB/Thread sanitizers detect memory and race issues.

**47. Prefer composition over inheritance?**
Improves reuse, reduces fragility and slicing.

**48. Performance profiling?**
Use perf/VTune/Callgrind; measure before tuning.
