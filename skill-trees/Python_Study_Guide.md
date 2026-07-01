# Python – Interview Study Guide

_Styled like the sample: Beginner → Intermediate → Advanced; concise answers._

## Beginner Level
**1. Python implementations?**
CPython reference, PyPy JIT, others like Jython/IronPython for JVM/.NET interop.

**2. Mutable vs immutable types?**
Immutable: int,str,tuple; Mutable: list,dict,set,bytearray.

**3. Name binding?**
Names reference objects; assignment rebinding; refcount + cyclic GC.

**4. List vs tuple?**
List mutable, tuple immutable/hashable (if elements hashable).

**5. dict characteristics?**
Hash table preserving insertion order; O(1) average ops.

**6. Set vs frozenset?**
Mutable vs immutable sets; both store unique elements.

**7. Slicing?**
seq[start:stop:step] returns new sequence; negative indices allowed.

**8. args/kwargs?**
*args for variable positional, **kwargs for keyword args.

**9. Comprehensions?**
Succinct list/dict/set/GEN comprehensions; can include conditions/nesting.

**10. Generators?**
Functions with yield providing lazy streams and state.

**11. Iterator protocol?**
__iter__ and __next__; StopIteration signals end.

**12. Decorators?**
Higher‑order wrappers to augment behavior of functions/classes.

**13. Context managers?**
__enter__/__exit__ for resource mgmt; contextlib utilities simplify.

**14. dataclasses?**
Generate init/eq/order; use frozen or slots for efficiency.

**15. Type hints?**
PEP 484; static checking with mypy/pyright; runtime via typing.get_type_hints.

**16. asyncio basics?**
Event loop, coroutines, tasks; gather for concurrency; avoid blocking.

**17. Threads vs processes?**
GIL limits CPU‑bound threading; use multiprocessing or C extensions.

**18. GIL explained?**
Global lock serializes bytecode execution in CPython.

**19. File handling?**
with open(...) ensures close; text vs binary modes.

**20. Exceptions best practices?**
Catch specific exceptions; avoid bare except; use finally for cleanup.


## Intermediate Level
**21. Virtual environments?**
venv/virtualenv isolate dependencies per project.

**22. Packaging?**
pyproject.toml with build systems (setuptools/poetry).

**23. Logging vs print?**
logging supports levels/handlers/formatters for production diagnostics.

**24. Serialization?**
json safe text; pickle unsafe; use dataclasses‑json/pydantic for models.

**25. pathlib?**
Path objects for cross‑platform path operations.

**26. Time and tz?**
timezone‑aware datetime; zoneinfo (3.9+) for IANA zones.

**27. Performance tips?**
Profile with cProfile; vectorize with NumPy; cache with lru_cache.

**28. Properties/descriptors?**
@property for computed attributes; descriptors share getter/setter logic.

**29. Dunder methods?**
Implement __repr__/__str__, arithmetic, iteration, context, comparison.

**30. copy vs deepcopy?**
copy.copy shallow; copy.deepcopy recursive deep copy.

**31. global/nonlocal?**
global binds module name; nonlocal binds nearest enclosing scope.

**32. Walrus operator?**
Assignment expression (:=) inside larger expressions/conditions.

**33. Pattern matching?**
match/case for structural matching (3.10+).

**34. Testing tools?**
unittest and pytest with fixtures and assertions.

**35. Security?**
Avoid eval/exec on untrusted input; validate and sanitize; pin dependencies.

**36. NumPy vs lists?**
NumPy arrays perform vectorized operations in C—much faster for numeric work.

**37. Resource release?**
Prefer context managers; GC timing is nondeterministic.

**38. Iterator exhaustion?**
Iterators are single‑pass; recreate or tee if needed.

**39. PEP8/tooling?**
Use black/isort/ruff/flake8 for consistent style and linting.

**40. @property costs?**
Heavy logic can hurt perf; cache results when needed.


## Advanced Level
**41. Hashable dict keys?**
Immutable and hash‑stable types like str,int,tuples of hashables.

**42. Monkey patching?**
Runtime replacement—useful for tests, but brittle.

**43. Metaclasses?**
Customize class creation by subclassing type; advanced feature.

**44. ContextVar?**
Context‑local variables safe across asyncio tasks.

**45. Executable scripts?**
if __name__ == '__main__' and argparse/click for CLIs.

**46. Caching?**
functools.lru_cache and manual memoization; mind invalidation.

**47. dataclasses vs attrs vs pydantic?**
dataclasses stdlib; attrs richer; pydantic adds validation/serialization.

**48. Package entry points?**
[project.scripts] console scripts in pyproject.toml map to callables.

**49. Type narrowing?**
isinstance checks refine union types for static checkers.
