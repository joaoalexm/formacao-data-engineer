# Git 09 — GitHub Flow

## Goal

Practice a simple day-to-day workflow using a feature branch and a pull request instead of making changes directly on `main`.

## What I did

I started from an updated `main` branch and created:

```text
exercicio/git-09
```

The exercise itself was intentionally small. I added:

```text
GitHub Flow practice
```

to `flow.txt`.

Before committing, I reviewed the repository state and the staged changes instead of committing immediately.

The change was recorded in:

```text
90abaf9 docs: add GitHub Flow practice
```

I then pushed the branch to GitHub and opened Pull Request #18:

```text
Git 09 - GitHub Flow
```

The pull request was merged into `main` and closed Issue #17.

## The workflow I practiced

```text
update main
    ↓
create feature branch
    ↓
make a focused change
    ↓
review the diff
    ↓
stage and commit
    ↓
push the branch
    ↓
open a pull request
    ↓
merge
    ↓
synchronize local main
```

## Commands I used

```bash
git switch main
git pull

git switch -c exercicio/git-09

git status
git diff

git add fase-1/git/exercicio-09/flow.txt
git diff --staged

git commit -m "docs: add GitHub Flow practice"

git push -u origin exercicio/git-09
```

## What I learned

This exercise connected several Git commands that I had practiced separately into one normal development workflow.

Instead of working directly on `main`, I learned to isolate a change in its own branch, review exactly what would be committed, publish that branch, and integrate it through a pull request.

The change itself was small, but the important part was the process around it.
