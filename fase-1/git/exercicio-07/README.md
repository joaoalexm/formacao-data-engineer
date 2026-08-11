# Git 07 — Branches

## Objective

Understand how independent Git branches can be created from the same base, developed separately, and later integrated into the main branch.

## Expected Output

* Create two independent branches from `main`
* Make a different change in each branch
* Confirm that changes from one branch do not automatically appear in another
* Merge both branches
* Understand the difference between a fast-forward merge and a merge commit
* Visualize the branch history with `git log --graph`

## Commands and Observations

### 1. How were the two branches created?

The first branch was created from `main`:

```text
git switch -c exercicio/git-07-a
```

A file named `branch-a.txt` was created and committed.

The commit was:

```text
423d5d7 feat: add branch A change
```

After returning to `main`, the file from branch A was no longer present because the commit only existed in branch A.

The second branch was then created directly from `main`:

```text
git switch -c exercicio/git-07-b
```

A different file named `branch-b.txt` was created and committed.

The commit was:

```text
86955e2 feat: add branch B change
```

### 2. Why did `branch-a.txt` disappear after switching to `main`?

The file belonged to a commit that existed only in `exercicio/git-07-a`.

The `main` branch had not received that commit yet.

Changing branches changes the working directory to represent the history of the selected branch.

### 3. How was it confirmed that the branches were independent?

The Git history showed both branches originating from the same commit:

```text
        branch A
       /
main --
       \
        branch B
```

Neither branch contained the commit created in the other branch.

### 4. What happened when branch A was merged?

The command used was:

```text
git merge exercicio/git-07-a
```

Git performed a fast-forward merge.

The `main` branch simply moved forward to the commit from branch A because `main` had not received any other commits since branch A was created.

No additional merge commit was required.

### 5. What is a fast-forward merge?

A fast-forward merge happens when the current branch can simply move its pointer forward to the target commit.

Before:

```text
main
  |
  A0 ---- A1
          ^
       branch A
```

After:

```text
A0 ---- A1
        ^
     main
     branch A
```

Git does not need to create another commit.

### 6. What happened when branch B was merged?

Branch B had been created independently from the original `main`.

After branch A was merged, the history had diverged.

The command:

```text
git merge exercicio/git-07-b
```

created a new merge commit:

```text
d699566 Merge branch 'exercicio/git-07-b'
```

### 7. Why was a merge commit necessary?

The history contained two independent lines of development:

```text
        A
       /
base --
       \
        B
```

The merge commit connected both histories:

```text
        A
       / \
base --   M
       \ /
        B
```

The merge commit has two parent commits and represents the point where both independent changes were integrated.

### 8. What did `git status` mean after the merges?

Git reported:

```text
Your branch is ahead of 'origin/main' by 3 commits.
```

The three commits were:

```text
423d5d7 feat: add branch A change
86955e2 feat: add branch B change
d699566 Merge branch 'exercicio/git-07-b'
```

This meant the commits existed locally but had not yet been published to the remote `main` branch.

At the same time:

```text
nothing to commit, working tree clean
```

meant that all local file changes had already been committed.

A clean working tree does not necessarily mean that the local branch is synchronized with the remote repository.

### 9. How was the history visualized?

The command used was:

```text
git log --oneline --graph --decorate --all
```

This displayed the commits and the relationship between the independent branches and the merge commit.

## What I Learned

I learned that branches allow independent lines of development to exist without immediately affecting each other.

I learned that switching branches changes the working directory to match the selected branch's history.

I also learned the difference between a fast-forward merge and a merge that creates a merge commit.

A clean working tree only means that there are no uncommitted changes. A branch can still contain commits that have not been pushed to the remote repository.

Finally, I learned how `git log --graph` can be used to visualize how branches diverge and later reconnect.
