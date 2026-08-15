# Git 15 — Inspecting and Auditing History

## Goal

Practice using Git history as a source of information to find when a change happened, what a commit changed, and which commit last modified a specific line.

## What I did

Instead of creating another isolated Git operation, I used the history produced by the previous exercises as the material for this audit.

I started with a compact view of recent commits:

```bash
git log --oneline -10
```

This gave me a quick overview of the latest repository activity.

I then searched commit messages for a specific topic:

```bash
git log --oneline --grep="stash"
```

That helped me locate the commit related to the stash exercise without manually reading the entire history.

## Inspecting a specific commit

After identifying the stash practice commit, I inspected it directly:

```bash
git show 4ffc297
```

This showed both the commit metadata and the actual changes introduced by that commit.

That made the difference between `git log` and `git show` clearer to me:

```text
git log  -> find commits in history
git show -> inspect one specific commit in detail
```

## Investigating a file

I also inspected the history of:

```text
fase-1/git/exercicio-11/config.txt
```

using:

```bash
git log --oneline -- fase-1/git/exercicio-11/config.txt
```

Instead of searching the entire repository history, this showed only commits that affected that file.

I then used:

```bash
git blame fase-1/git/exercicio-11/config.txt
```

to identify which commit was responsible for the current line in the file.

This connected the file's current content with the repository history that produced it.

## Commands I used

```bash
git log --oneline -10

git log --oneline --grep="stash"

git show 4ffc297

git log --oneline -- fase-1/git/exercicio-11/config.txt

git blame fase-1/git/exercicio-11/config.txt
```

## What I learned

Git history is useful for more than seeing a list of old commits.

I can search commit messages to find a relevant change, inspect the exact contents of a commit, restrict the history to a specific file, and trace individual lines back to the commits that introduced them.

I also learned that the different history commands answer different questions:

```text
git log        -> what happened?
git log --grep -> where is a change related to a topic?
git show       -> what exactly did this commit change?
git log -- file -> what happened to this specific file?
git blame      -> which commit last changed each line?
```

This exercise made the repository history feel more like a debugging and investigation tool instead of only a record of previous work.
