# Git 07 — Branches and Merges

## Goal

Understand how branches create independent lines of development and how Git integrates them using different types of merge.

## What I did

I created two branches independently from the same starting point on `main`.

The first branch was:

```text
exercicio/git-07-a
```

where I created and committed `branch-a.txt`:

```text
423d5d7 feat: add branch A change
```

After switching back to `main`, the file disappeared from the working directory because that commit existed only on branch A.

I then created another branch from the original `main`:

```text
exercicio/git-07-b
```

and committed a different file:

```text
86955e2 feat: add branch B change
```

This made it clear that the two branches could contain different changes without automatically affecting each other.

## Fast-forward and merge commit

When I merged branch A into `main`, Git performed a fast-forward merge.

`main` had not moved since branch A was created, so Git only needed to move the `main` pointer forward to the branch A commit. No additional commit was necessary.

After that, branch B represented a different line of development from the same earlier commit.

Merging branch B required Git to connect both histories and created:

```text
d699566 Merge branch 'exercicio/git-07-b'
```

This gave me a practical comparison between a fast-forward merge and a merge commit.

## Local history versus remote state

After the merges, Git reported that my local branch was ahead of `origin/main` while also reporting:

```text
nothing to commit, working tree clean
```

That helped me understand that these messages describe different things.

A clean working tree means there are no uncommitted file changes.

Being ahead of `origin/main` means there are local commits that have not been published to the remote yet.

## Commands I used

```bash
git switch main
git switch -c exercicio/git-07-a
git add branch-a.txt
git commit -m "feat: add branch A change"

git switch main
git switch -c exercicio/git-07-b
git add branch-b.txt
git commit -m "feat: add branch B change"

git switch main
git merge exercicio/git-07-a
git merge exercicio/git-07-b

git status
git log --oneline --graph --decorate --all
```

## What I learned

Branches allow separate lines of development to exist without immediately changing each other.

I also learned that switching branches changes the working directory to match the history of the selected branch.

The most useful part of this exercise was seeing why one merge could be completed with a fast-forward while another required a merge commit.

I also stopped treating `working tree clean` as meaning that everything is synchronized with GitHub. Local file state and remote synchronization are separate things.
