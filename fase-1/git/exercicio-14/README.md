# Git 14 — Fork and Upstream Collaboration

## Goal

Practice contributing to a repository I do not own by using a fork, an `upstream` remote, a feature branch, and a pull request to the original repository.

## What I did

For this exercise, I used the training repository:

```text
AlexMarquesSouza/Treinamento-data-engineer-Junior
```

Instead of making a simulated remote configuration inside my own repository, I created a real fork under my GitHub account and cloned it locally.

The remote configuration represented two different repositories:

```text
origin   -> joaoalexm/Treinamento-data-engineer-Junior
upstream -> AlexMarquesSouza/Treinamento-data-engineer-Junior
```

`origin` pointed to my fork, where I could push my own branches.

`upstream` pointed to the original repository, allowing me to retrieve updates from the source project.

## Making the contribution

I fetched the original repository and created:

```text
docs/fix-git14-example
```

The change was intentionally small and focused.

I updated the example for Git exercise 14 so that it actually described a fork and upstream workflow instead of an unrelated local repository example.

The commit was:

```text
f87877a docs: improve Git 14 fork example
```

I pushed that branch to my fork and opened Pull Request #1 against the original repository:

```text
docs: improve Git 14 fork example
```

At the time of documenting this exercise, the pull request is still open and awaiting review.

## Commands I used

```bash
gh repo fork AlexMarquesSouza/Treinamento-data-engineer-Junior --clone --default-branch-only

git remote -v

git fetch upstream
git switch -c docs/fix-git14-example

git diff

git add trilhas/01-git-github.md
git commit -m "docs: improve Git 14 fork example"

git push -u origin docs/fix-git14-example
```

## What I learned

This exercise made the difference between `origin` and `upstream` much clearer because both names represented real repositories with different purposes.

`origin` is my fork and is where I publish my own branches.

`upstream` points to the original project and is where I retrieve changes made by its maintainers.

I also learned that contributing through a fork does not require write access to the original repository. I can make the change in my fork and propose it through a pull request for the maintainer to review.

Unlike the earlier exercises where I controlled both sides of the workflow, this pull request depends on another repository owner before it can be merged.
