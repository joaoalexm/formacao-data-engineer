# Git 08 — Resolving a Merge Conflict

## Goal

Create a real merge conflict, understand why Git could not resolve it automatically, and complete the merge safely.

## What I did

I started with the same file containing:

```text
Price: 10
```

From that common version, two branches changed the same line differently.

My exercise branch changed it to:

```text
Price: 30
```

with commit:

```text
5b44b3c
```

The other branch changed it to:

```text
Price: 20
```

with commit:

```text
eec0b12
```

Because both branches changed the same line from the same original value, Git could not decide which result should be kept.

When I tried to merge them, Git stopped the operation and reported a conflict in `price.txt`.

## Reading the conflict

The file contained markers similar to:

```text
<<<<<<< HEAD
Price: 30
=======
Price: 20
>>>>>>> exercicio/git-08-colega
```

`HEAD` represented the version from the branch I was currently on.

The section after `=======` represented the incoming version from the branch being merged.

Git was not asking me to run a special command that could automatically know the correct price. I had to decide what the final content should be.

## Resolving it

I chose to keep:

```text
Price: 30
```

I removed the conflict markers, saved the file, and checked the repository state.

Then I marked the file as resolved with:

```bash
git add fase-1/git/exercicio-08/price.txt
```

and completed the merge.

The resolution was recorded in commit:

```text
c34faf2 test: resolve merge conflict
```

## Commands I used

```bash
git status
git diff

git merge exercicio/git-08-colega

git status
git diff

git add fase-1/git/exercicio-08/price.txt
git commit

git log --oneline --graph --decorate
```

I also learned that an unfinished merge can be cancelled with:

```bash
git merge --abort
```

which returns the repository to the state it had before the merge started.

## What I learned

A merge conflict does not mean the repository is corrupted. It means Git found incompatible changes and cannot safely decide the final content by itself.

I learned how to read the conflict markers, identify the current and incoming versions, make the final decision manually, and use `git add` to tell Git that the conflict was resolved.

This exercise also made conflicts feel less abstract. Instead of only reading about them, I saw Git stop a real merge and had to decide how the histories should be combined.
