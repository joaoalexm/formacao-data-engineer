# Git 10 — Synchronizing Multiple Clones

## Goal

Understand how two local copies of the same repository can become different and how Git synchronizes them through the remote repository.

## What I did

I used two local clones to simulate working with the same repository from two different computers.

Both clones initially represented the same remote repository.

From the primary clone, I created a feature branch and added:

```text
Synchronization practice
```

to `sync.txt`.

The change was committed as:

```text
c43926f docs: add synchronization practice
```

I pushed the branch to GitHub and opened Pull Request #20.

After the pull request was merged into `main`, the remote repository contained the new commit, but the second clone did not receive it automatically.

That second copy was now behind the remote repository.

## Updating the second clone

I used:

```bash
git fetch
```

to update the remote references without immediately changing the files in the working directory.

This let me inspect the difference between the local branch and the updated remote state.

I then used:

```bash
git pull
```

to bring the remote changes into the local branch.

Because the local clone had no competing commits, Git could update it with a fast-forward.

After that, both local copies represented the updated repository history again.

## Commands I used

```bash
git clone <repository-url>

git switch main
git pull

git switch -c exercicio/git-10

git status
git add fase-1/git/exercicio-10/sync.txt
git diff --staged

git commit -m "docs: add synchronization practice"
git push -u origin exercicio/git-10

git fetch
git status
git pull

git log --oneline --graph --decorate
```

## What I learned

Each clone of a repository has its own local state.

A commit reaching GitHub does not automatically update every other clone of that repository.

I learned that `git fetch` retrieves information from the remote without immediately integrating it into my current branch, while `git pull` retrieves and integrates remote changes.

Using two clones made synchronization easier to understand because I could see one copy become outdated while the other published new work.
