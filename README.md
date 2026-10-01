# ci-branch-protection-demo

A tiny public repository for Lesson 11.3 of *Software Engineering for ML
Practitioners*: one function, one test, and the course's CI workflow, with a
branch ruleset on `main` that blocks merging a pull request whose checks fail.

```bash
uv sync
uv run pytest
```
