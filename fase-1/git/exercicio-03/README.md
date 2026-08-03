# Git 03 — Readable History

## Objective

Understand how to read Git history using different `git log` formats and identify useful information about commits.

## Expected Output

* Read the commit history
* Compare different `git log` formats
* Identify commit hash, author, date, branch references, and commit message
* Understand when a compact or detailed history view is more useful

## Commands and Observations

### 1. What is the difference between `git log` and `git log --oneline`?

`git log` shows detailed information about each commit, including the full commit hash, author, date, and commit message.

`git log --oneline` shows each commit in a compact format using the shortened commit hash and the commit message.

### 2. What does the `--graph` option show?

The `--graph` option displays a visual representation of the commit history.

It uses lines and symbols to show where branches were created and where they were merged.

### 3. What does the `--decorate` option show?

The `--decorate` option shows references associated with commits, such as branch names, remote branches, tags, and `HEAD`.

For example:

```text
HEAD -> exercicio/git-03
```

shows the branch that I am currently using.

### 4. What does `HEAD -> exercicio/git-03` mean?

It means that I am currently working on the `exercicio/git-03` branch.

`HEAD` represents my current position in the repository, and the branch points to the current commit.

### 5. What is a merge commit?

A merge commit is a commit that combines changes and histories from different branches.

In this repository, merge commits were created when the exercise branches were merged into the `main` branch through pull requests.

### 6. What do `%h`, `%an`, `%ad`, and `%s` represent in a custom log format?

* `%h` represents the shortened commit hash.
* `%an` represents the author's name.
* `%ad` represents the commit date.
* `%s` represents the commit message.

These placeholders allow the output of `git log` to be customized.

### 7. When is a compact log more useful than a detailed log?

A compact log is more useful when I want to quickly review the commit history, identify commit messages, and compare multiple commits.

A detailed log is more useful when I need information such as the full commit hash, author, date, or merge details.

## What I Learned

I learned how to read Git history using detailed, compact, graphical, and customized formats.

I also learned how branches, remote references, `HEAD`, and merge commits appear in the Git history.

The compact log is useful for quickly reviewing commits, while the detailed log is better when more information about a specific commit is needed.
