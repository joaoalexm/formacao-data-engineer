# Git 03 — Reading Git History

## Goal

Learn how to inspect Git history using different log formats and understand the information attached to each commit.

## What I did

I explored the repository history using both detailed and compact versions of `git log`.

The standard log gave me information such as the full commit hash, author, date, and message, while `--oneline` made it easier to scan several commits quickly.

I also used:

```text
--graph
--decorate
```

to understand how branches, merge commits, remote references, and `HEAD` appear in the history.

For example:

```text
HEAD -> exercicio/git-03
```

showed that I was currently on the `exercicio/git-03` branch and that the branch pointed to the current commit.

I also tested a custom log format to choose exactly which information I wanted to display.

## Commands I used

```bash
git log
git log --oneline
git log --oneline --graph
git log --oneline --graph --decorate

git log --pretty=format:"%h | %an | %ad | %s"
```

In the custom format:

```text
%h  shortened commit hash
%an author name
%ad author date
%s  commit message
```

## What I learned

I learned that there is no single best way to view Git history.

A compact log is useful when I want to quickly understand what changed over several commits, while a detailed log is better when I need information about a specific commit.

Using `--graph` and `--decorate` also made it easier to understand how branches and merge commits are represented in the repository history instead of seeing commits only as an isolated list.
