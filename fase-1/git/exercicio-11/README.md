# Git 11 — Restore and Revert

## Objective

Understand the difference between undoing uncommitted changes with `git restore` and undoing committed changes with `git revert`.

## Git Restore

`git restore` is useful when a file was changed locally but the change has not been committed yet.

Example:

```text
Environment: development
```

The file was changed to:

```text
Environment: production
```

Before committing, the change was discarded with:

```text
git restore fase-1/git/exercicio-11/config.txt
```

The file returned to:

```text
Environment: development
```

## Git Revert

`git revert` is useful when an incorrect change has already been committed.

The incorrect commit was:

```text
8668e76 test: change environment to production
```

Instead of deleting that commit from history, a new commit was created to reverse it:

```text
9bbed09 Revert "test: change environment to production"
```

The command used was:

```text
git revert 8668e76 --no-edit
```

After the revert, the file returned to:

```text
Environment: development
```

## Key Difference

```text
git restore
→ used before a change is committed
→ discards local file changes

git revert
→ used after a change is committed
→ creates a new commit that reverses another commit
```

## Why Revert Is Safer for Shared History

When a commit has already been shared with other developers, removing or rewriting it can create problems.

`git revert` keeps the original commit in the history and records the correction as a new commit.

This makes the history explicit and safer for collaboration.

## Important Commands

Discard an uncommitted change:

```text
git restore <file>
```

Revert a specific commit:

```text
git revert <commit>
```

Revert without opening the commit message editor:

```text
git revert <commit> --no-edit
```

Inspect recent commits:

```text
git log --oneline
```

## What I Learned

I learned that `git restore` and `git revert` solve different problems.

`git restore` is appropriate for local changes that have not been committed.

`git revert` is appropriate when a committed change must be undone without deleting or rewriting shared history.
