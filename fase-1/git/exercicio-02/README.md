# Git 02 — First Repository

## Goal

Create a Git repository from scratch and understand how files move through the main Git states.

## What I did

I initialized a repository with `main` as the first branch and created a README to follow its state through Git.

At first, the file was untracked. After using `git add`, it moved to the staging area. After the commit, that version became part of the repository history.

This exercise also helped me understand that committing and pushing are different operations: a commit saves changes in the local Git history, while a push sends commits to a remote repository.

I also checked the log and understood that:

```text
HEAD -> main
```

means that `HEAD` is currently on the `main` branch and that the branch points to that commit.

## A problem I ran into

The first README was accidentally created using UTF-16 LE encoding.

Because of that, Git interpreted the file as binary and could not display the normal text diff.

I converted the file to UTF-8 and checked the diff again. After the conversion, Git could treat the README as a normal text file.

This resulted in two separate commits:

```text
docs: add initial README
fix: convert README to UTF-8
```

Keeping the encoding fix in its own commit also gave me a practical example of an atomic commit: one commit should represent one clear change.

## Commands I used

```bash
git init -b main
git status

git add README.md
git commit -m "docs: add initial README"

git diff
git status

git add README.md
git commit -m "fix: convert README to UTF-8"

git log --oneline
```

The encoding correction was done in PowerShell with:

```powershell
"# Git Lab 02" | Set-Content -Encoding utf8 README.md
```

## What I learned

I learned the basic file flow in Git:

```text
Untracked → Staged → Committed
```

I also understood the role of `HEAD`, the difference between committing and pushing, and why small commits with a single purpose make the repository history easier to understand.

The encoding problem was useful because it showed me that Git also depends on how files are stored, not only on the commands I run.
