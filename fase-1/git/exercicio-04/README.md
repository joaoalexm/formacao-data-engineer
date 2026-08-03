# Git 04 — Comparing Changes

## Objective

Understand how to compare changes between the working directory, staging area, and the last commit.

## Expected Output

* Compare unstaged changes
* Compare staged changes
* Compare the current state with the last commit
* Understand the difference between `git diff`, `git diff --staged`, and `git diff HEAD`

## Commands and Observations

### 1. What does `git diff` compare?

`git diff` compares the version currently stored in the staging area with the version in the working directory.

It shows changes that have not been staged yet.

In the exercise, the staging area contained Version 2 while the working directory contained Version 3. Therefore, `git diff` showed:

```text
Version 2 → Version 3
```

### 2. What does `git diff --staged` compare?

`git diff --staged` compares the last commit with the version currently stored in the staging area.

It shows the changes that will be included in the next commit.

In the exercise, the last commit contained Version 1 while the staging area contained Version 2. Therefore, it showed:

```text
Version 1 → Version 2
```

### 3. What does `git diff HEAD` compare?

`git diff HEAD` compares the last commit with the current version in the working directory.

It shows the complete difference between the last committed state and the current file.

In the exercise, the last commit contained Version 1 while the working directory contained Version 3. Therefore, it showed:

```text
Version 1 → Version 3
```

### 4. Why did the same file appear in two sections of `git status`?

The file appeared under both `Changes to be committed` and `Changes not staged for commit` because different versions of the same file existed in the staging area and working directory.

The staging area contained Version 2, which was ready to be committed.

The working directory contained Version 3, which had not been staged yet.

### 5. Which version did Git save when the commit was created?

Git saved Version 2 because that was the version stored in the staging area.

Version 3 remained in the working directory because it had not been added with `git add`.

This demonstrated that `git commit` saves the staged version, not automatically the latest version of every file in the working directory.

### 6. What is the relationship between the three Git areas?

The three relevant states were:

```text
Last commit:       Version 1
Staging area:      Version 2
Working directory: Version 3
```

The comparisons were:

```text
git diff          → staging area versus working directory
git diff --staged → last commit versus staging area
git diff HEAD     → last commit versus working directory
```

### 7. What happened after Version 3 was staged and committed?

After running `git add` again, Version 3 replaced Version 2 in the staging area.

The next commit saved Version 3 in the repository history.

After the commit, the working directory became clean because the committed version and the current file were the same.

## What I Learned

I learned that a file can have different versions in the last commit, staging area, and working directory at the same time.

I also learned that `git add` selects the current version of a file for the next commit. If the file is changed again after `git add`, the new changes are not automatically included in the commit.

The `git diff` commands help identify exactly where changes exist before creating a commit.
