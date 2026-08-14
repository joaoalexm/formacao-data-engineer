# Git 04 — Comparing Changes

## Goal

Understand the difference between the working directory, staging area, and the last commit by comparing different versions of the same file.

## What I did

For this exercise, I intentionally kept three different versions of the same file at the same time:

```text
Last commit:       Version 1
Staging area:      Version 2
Working directory: Version 3
```

This made the difference between the Git areas much easier to see.

With that state prepared, I compared the file using three different commands.

`git diff` showed:

```text
Version 2 → Version 3
```

because it compared the staged version with the current working directory.

`git diff --staged` showed:

```text
Version 1 → Version 2
```

because it compared the last commit with what was already prepared in the staging area.

`git diff HEAD` showed:

```text
Version 1 → Version 3
```

because it compared the last committed version with the current working directory.

The same file also appeared in two sections of `git status` because Version 2 was staged while Version 3 contained additional unstaged changes.

## Commands I used

```bash
git status
git diff
git diff --staged
git diff HEAD

git add comparison.txt
git commit
```

I changed and staged the file multiple times during the experiment so I could observe how each Git area changed independently.

## What I learned

The most important thing I learned was that `git add` does not permanently attach a file to the next commit.

It stages the version of the file that exists at that moment.

If I change the file again afterward, those new changes remain only in the working directory until I run `git add` again.

I also learned that `git commit` saves what is in the staging area, not automatically the latest version of every file in the working directory.

The different `git diff` commands let me inspect each of these states before committing and understand exactly what Git is going to save.
