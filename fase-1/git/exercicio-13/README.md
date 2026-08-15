# Git 13 — Tags and Releases

## Goal

Understand how Git tags can mark important points in repository history and how those tags can be used to create releases on GitHub.

## What I did

After completing the first group of Git exercises, I created a version marker for that point in the repository history.

I used an annotated tag:

```bash
git tag -a v0.1.0 -m "Git training milestone"
```

Unlike a branch, the tag was meant to identify a specific historical point rather than move forward with new commits.

I inspected the tag with:

```bash
git show v0.1.0
```

and then published it to GitHub:

```bash
git push origin v0.1.0
```

## Creating a GitHub release

After publishing the tag, I created a GitHub release using:

```text
v0.1.0
```

with the title:

```text
v0.1.0 - Git Training Milestone
```

The release represented the progress made through the Git training topics completed at that point, including:

```text
Git fundamentals
branches and merges
merge conflicts
GitHub Flow
repository synchronization
restore and revert
stash
tags
```

## Commands I used

```bash
git tag
git tag -a v0.1.0 -m "Git training milestone"

git show v0.1.0

git push origin v0.1.0

git tag
git log --oneline --decorate
```

## What I learned

A tag gives a stable name to a specific point in Git history.

Branches normally continue moving as new commits are created, while a version tag such as `v0.1.0` remains attached to the commit it was created for.

I also learned the difference between a Git tag and a GitHub release.

The tag exists in Git and identifies the version in repository history, while the GitHub release adds a published milestone around that tag with a title and description.

This was the first point where the repository history started to represent not only individual exercises, but also a defined training milestone.
