# Git 02 — First Repository

## Objective

Create a Git repository from scratch and understand the main file states in Git.

## Expected Output

* Initialize a new Git repository
* Create a README file
* Observe untracked, staged, and committed states
* Create two small atomic commits

## Commands and Observations

### 1. What does `git init -b main` do?

It initializes a new Git repository and sets `main` as the initial branch.

### 2. What does an untracked file mean?

An untracked file exists in the working directory, but Git is not tracking it yet.

Git can see that the file exists, but it has not been added to the repository history.

### 3. What changed after running `git add README.md`?

After running `git add README.md`, the file moved from the untracked state to the staged state.

This means that its current version was added to the staging area and was ready to be included in the next commit.

### 4. What does a commit represent?

A commit represents a saved snapshot of changes in the repository history.

It records the selected changes locally with a unique identifier and a commit message.

A commit is different from a push. A commit records changes locally, while a push sends commits to a remote repository such as GitHub.

### 5. What is the difference between untracked, staged, and committed?

**Untracked:** The file exists in the working directory, but Git is not tracking it yet.

**Staged:** The file or its changes have been selected with `git add` and are ready to be included in the next commit.

**Committed:** The staged changes have been saved as part of the Git repository history.

The basic flow is:

```text
Untracked → Staged → Committed
```

### 6. What does `HEAD -> main` mean in `git log --oneline`?

`HEAD` represents my current position in the repository history.

When Git shows:

```text
HEAD -> main
```

it means that I am currently on the `main` branch and that `main` points to that commit.

### 7. What problem happened with the README encoding, and how was it fixed?

The README was initially created using UTF-16 LE encoding.

Because of this encoding, Git treated the file as binary instead of normal text when showing the diff.

The file was converted to UTF-8 using:

```powershell
"# Git Lab 02" | Set-Content -Encoding utf8 README.md
```

After that, the README was stored using UTF-8 instead of UTF-16 LE.

### 8. Why were the two commits considered atomic?

The two commits were considered atomic because each commit had one specific purpose.

The first commit created the initial README:

```text
docs: add initial README
```

The second commit fixed the README encoding:

```text
fix: convert README to UTF-8
```

Each commit represented one logical change instead of mixing multiple unrelated changes together.

## What I Learned

I learned how to initialize a Git repository and how files move through the untracked, staged, and committed states.

I also learned that a commit saves changes in the local repository history and is different from pushing changes to a remote repository.

I learned how `HEAD` and branches relate to commits, why small atomic commits are useful, and how file encoding can affect how Git interprets and displays file changes.

