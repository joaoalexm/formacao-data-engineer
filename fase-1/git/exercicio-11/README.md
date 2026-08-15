# Git 11 — Restore and Revert

## Goal

Understand how to undo changes safely depending on whether they have already been committed.

## What I did

I started with `config.txt` containing:

```text
Environment: development
```

I changed it locally to:

```text
Environment: production
```

but did not commit that change.

Because I only wanted to discard the local modification, I used:

```bash
git restore fase-1/git/exercicio-11/config.txt
```

The file returned to:

```text
Environment: development
```

This showed me that `git restore` can be used when I want to discard changes that are still only in the working directory.

## Undoing a committed change

I then created an intentionally incorrect commit:

```text
8668e76 test: change environment to production
```

At that point, `git restore` was no longer the right tool because the change was already part of the repository history.

Instead, I used:

```bash
git revert 8668e76 --no-edit
```

Git created a new commit:

```text
9bbed09 Revert "test: change environment to production"
```

The file returned to:

```text
Environment: development
```

but the incorrect commit was still visible in the history.

## The difference I practiced

```text
Uncommitted change
        ↓
   git restore
        ↓
discard local modification
```

```text
Committed change
        ↓
    git revert
        ↓
create a new commit that reverses it
```

## Commands I used

```bash
git status
git diff

git restore fase-1/git/exercicio-11/config.txt

git add fase-1/git/exercicio-11/config.txt
git commit -m "test: change environment to production"

git revert 8668e76 --no-edit

git log --oneline
```

## What I learned

The important difference is not simply that both commands undo something.

`git restore` changes my local working state and is useful before a change has been committed.

`git revert` works with repository history. Instead of deleting an existing commit, it creates another commit that reverses its effect.

That makes `git revert` especially useful when the original commit may already be part of shared history, because the correction remains visible instead of rewriting what happened.
