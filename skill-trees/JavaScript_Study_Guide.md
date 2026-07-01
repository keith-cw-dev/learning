# JavaScript – Interview Study Guide

_Styled like the sample: Beginner → Intermediate → Advanced; concise answers._

## Beginner Level
**1. What is JavaScript and where does it run?**
Dynamic, prototype‑based language running in browsers and in Node.js on servers.

**2. var vs let vs const?**
var: function‑scope; let/const: block‑scope; const binds variable not object contents.

**3. Primitive vs object types?**
Primitives: string, number, bigint, boolean, symbol, null, undefined; all others are objects.

**4. === vs == ?**
=== strict equality (no coercion); == loose (coerces)—prefer ===.

**5. What is hoisting?**
Declarations moved to top; let/const are hoisted but in temporal dead zone until initialized.

**6. Explain scope and closures.**
Scope rules variable visibility; closures capture outer variables for later use.

**7. What is ‘this’ in JS?**
Receiver at call‑site; arrow functions capture lexical this.

**8. call vs apply vs bind?**
call(this,a,b) ; apply(this,[args]) ; bind fixes this/args and returns a new function.

**9. Prototype vs class?**
Classes are sugar over prototypes; prototype chain drives inheritance.

**10. Arrow functions traits?**
Lexical this/arguments, concise; not constructible, no own prototype.

**11. Event loop overview?**
Processes stack and task queues (macro/microtasks) to deliver async behavior.

**12. Microtask vs macrotask?**
Microtasks (promises) run before rendering; macrotasks (setTimeout, I/O) later.

**13. Promise states and chaining?**
pending→fulfilled/rejected; then chains, catch handles errors, finally runs regardless.

**14. async/await?**
Syntax over promises; await pauses inside async function; use try/catch and Promise.all.

**15. Nullish coalescing (??) vs || ?**
?? only for null/undefined; || for any falsy (0,'' etc.).

**16. Optional chaining (?.)?**
Safely access nested properties/calls without throwing on null/undefined.

**17. Modules ESM vs CommonJS?**
ESM import/export static; CJS require/module.exports dynamic; Node supports both with rules.

**18. Deep vs shallow copy?**
Shallow copies share nested refs; deep copies clone recursively; use structuredClone.

**19. Map/Set vs Object/Array?**
Map/Set have O(1) ops and any keys; Objects tie into prototype and need hasOwn checks.

**20. Event delegation?**
Handle events on a parent using bubbling for dynamic children.


## Intermediate Level
**21. DOM vs BOM?**
DOM is document tree; BOM covers browser APIs like window/history.

**22. CORS basics?**
Browser blocks cross‑origin reads; server opts‑in via CORS headers and preflight.

**23. XSS and prevention?**
Avoid unsafe HTML injection; escape output, sanitize input, use CSP.

**24. Debounce vs throttle?**
Debounce waits for quiet; throttle limits frequency.

**25. Iterator/generator?**
Iterator with next(); generators yield values and can receive via next().

**26. Symbol use?**
Unique property keys and protocol hooks like Symbol.iterator.

**27. Proxy?**
Interpose traps (get/set/has) to virtualize/validate objects.

**28. JSON vs objects?**
JSON is string data format; parse/stringify to/from objects.

**29. Tree‑shaking?**
Eliminate unused ESM exports during bundling when side‑effect‑free.

**30. Memory leaks sources?**
Detached DOM, global refs, timers/closures; find with heap snapshots.

**31. Strict mode?**
'use strict' tightens semantics, eliminates silent errors, safer 'this'.

**32. BigInt vs Number?**
BigInt for arbitrary integers; cannot mix with Number without conversion.

**33. Intl API?**
Locale‑aware formatting of numbers, dates, plurals.

**34. fetch basics?**
Promise‑based HTTP; check response.ok; stream bodies; CORS applies.

**35. Service workers?**
Background scripts for offline caching, push, network interception.

**36. Web workers?**
Parallelism via messaging; no DOM access.

**37. Deep equality pitfalls?**
Objects compare by reference; use deep‑equal logic or libraries.

**38. React: why avoid direct state mutation?**
Mutation prevents change detection; always create new objects/arrays.

**39. Node.js event loop?**
libuv phases; microtasks after each phase; worker threads for CPU heavy tasks.

**40. CommonJS require cache?**
Modules cached after first require; delete from require.cache to reload.


## Advanced Level
**41. Security headers?**
CSP, HSTS, X‑Frame‑Options, X‑Content‑Type‑Options harden apps.

**42. Virtual DOM diffing?**
Computes minimal DOM updates; efficient when updates are batched.

**43. Bundling and code splitting?**
Combine modules and split via dynamic import() to cut initial load.

**44. Why prefer === for objects?**
Compares references; content equality requires custom logic.

**45. What is NaN and Number.isNaN?**
NaN is not‑a‑number; Number.isNaN avoids coercion pitfalls.

**46. What is the Temporal proposal?**
New modern date/time API (stage 3+) addressing Date pitfalls.
