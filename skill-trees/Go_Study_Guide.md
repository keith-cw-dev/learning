# Go – Interview Study Guide

_Styled like the sample: Beginner → Intermediate → Advanced; concise answers._

## Beginner Level
**1. Go design goals?**
Simple, fast compiles, static binaries, CSP‑style concurrency.

**2. Arrays vs slices?**
Arrays fixed size; slices dynamic views over arrays (ptr,len,cap).

**3. Maps?**
Hash maps with reference semantics; reads of missing keys return zero value and ok flag.

**4. Zero value?**
Useful defaults (0,"",nil) allow use without explicit init.

**5. Pointers?**
Hold addresses using * and &; no pointer arithmetic.

**6. Value vs pointer receivers?**
Pointer receivers allow mutation/avoid copies; method sets differ for interface satisfaction.

**7. Interfaces?**
Implicit contracts; satisfied by method sets—no explicit implements.

**8. Embedding?**
Anonymous fields to promote methods/fields; composition over inheritance.

**9. Error handling?**
Return (T, error); wrap with %w; sentinel and typed errors for classification.

**10. defer?**
Run after surrounding function returns; LIFO; ideal for cleanup.

**11. panic/recover?**
panic unwinds; recover in defer to handle exceptional flows.

**12. Goroutines?**
Lightweight concurrent functions scheduled by runtime.

**13. Channels?**
Typed pipes for communication (un/buffered); close for completion.

**14. select?**
Wait on multiple channel ops; default for non‑blocking; combine with context.

**15. Context?**
Cancellation/deadlines/values across API boundaries (req‑scoped).

**16. sync primitives?**
Mutex/RWMutex for mutual exclusion; WaitGroup to await goroutines.

**17. Atomic ops?**
sync/atomic supports lock‑free updates; use Load/Store/Add.

**18. Memory model?**
Happens‑before via channel send/receive and mutex unlock/lock.

**19. Generics?**
Type parameters with constraints (1.18+).

**20. Modules?**
go mod init; semantic import versioning; tidy to prune.


## Intermediate Level
**21. Testing/benchmarks?**
testing package with t.Run, b.N loop for benchmarks.

**22. Race detector?**
go test -race to find data races.

**23. pprof profiling?**
CPU/mem/block profiles analyzed with go tool pprof.

**24. io.Reader/Writer?**
Core stream interfaces enabling composition (bufio, compressors, network).

**25. HTTP server?**
net/http with handlers and middleware; context for cancellation.

**26. JSON tags?**
Struct field tags control names/omitempty; custom marshalers possible.

**27. Time/timezone?**
time.Time with Location; prefer UTC internally.

**28. init functions?**
Called before main after variable init; keep light.

**29. Build tags?**
//go:build for conditional compilation.

**30. cgo?**
C interop at cost of portability/perf; prefer pure Go when possible.

**31. Nil interface pitfalls?**
Typed nil inside interface != nil; careful comparisons.

**32. Slice capacity growth?**
append may reallocate/grow; reslicing can retain large arrays unintentionally.

**33. Map iteration order?**
Randomized; don’t depend on it—sort keys if needed.

**34. Closed channels?**
Receive yields zero value; send panics.

**35. Timers/tickers?**
Stop/drain to avoid leaks; use time.After for one‑offs.

**36. File I/O?**
Use bufio; handle partial reads/writes; defer Close.

**37. HTTP client pitfalls?**
Reuse http.Client; close resp.Body; respect context timeouts.

**38. Worker pool pattern?**
Goroutines consume from jobs channel; use WaitGroup and close to signal done.

**39. Interfaces vs generics?**
Interfaces for behavior; generics for reusable algorithms without boxing.

**40. When to use any?**
At API edges; prefer concrete types/generics internally.


## Advanced Level
**41. Errors vs panics?**
Errors for expected conditions; panics for programmer bugs/unrecoverable states.

**42. Cross‑compile?**
Set GOOS/GOARCH; static binaries by default (except with cgo).

**43. Vendoring?**
go mod vendor for hermetic builds.

**44. Common leaks?**
Blocked goroutines, retained sub‑slices, un‑stopped timers/tickers.

**45. Concurrency vs parallelism?**
Concurrency structures tasks; parallelism runs simultaneously; tune GOMAXPROCS.

**46. Type sets/constraints?**
Use ~ and unions for numeric types; constraints from constraints package.

**47. Good error messages?**
Lowercase, no punctuation, include context, wrap root cause.

**48. Pointer vs value params?**
Pointer for big/mutable structs; value for small, immutable ones.
