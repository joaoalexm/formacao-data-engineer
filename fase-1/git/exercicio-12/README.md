# Git 12 — Stashing Unfinished Work

## Goal

Understand how to temporarily save unfinished changes without creating an incomplete commit.

## What I did

I started with `task.txt` in a committed state and then changed it to:

```text
Status: work in progress
```

The change was not ready to become a commit yet, but I wanted to temporarily clean the working directory.

Instead of committing unfinished work, I used:

```bash
git stash
```

After that, the local modification disappeared from the working directory and was stored temporarily by Git.

I checked the saved work with:

```bash
git stash list
```

and then restored it using:

```bash
git stash pop
```

The `work in progress` change returned to `task.txt`, and the stash entry was removed.

After recovering the change, I finished the exercise and committed it normally.

The resulting commit was:

```text
4ffc297 test: complete stash practice
```

## Commands I used

```bash
git status
git diff

git stash
git stash list

git status

git stash pop
git status
git diff

git add fase-1/git/exercicio-12/task.txt
git commit -m "test: complete stash practice"
```

## What I learned

`git stash` is useful when I need to change context without either losing my current work or creating a commit that does not represent completed work.

The stash is separate from the normal commit history.

I also learned that `git stash pop` restores the saved changes and, when successful, removes that entry from the stash.

This gave me a practical way to temporarily leave unfinished work and return to it later.
