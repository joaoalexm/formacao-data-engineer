# Git 06 — Remote Repository

## Objective

Understand how a local Git repository connects to a remote repository, how `origin` works, how to push commits to GitHub, and how to clone a repository into another local directory.

## Expected Output

* Create a local Git repository from scratch
* Create a remote repository on GitHub
* Configure the `origin` remote
* Push the local `main` branch to GitHub
* Understand the purpose of `git push -u`
* Clone the repository into another directory
* Confirm that the commit history is preserved after cloning

## Commands and Observations

### 1. What is a remote repository?

A remote repository is a version of a Git repository stored somewhere outside the local computer, such as GitHub.

It allows the repository history to be shared, backed up, and accessed from other computers or directories.

### 2. What is `origin`?

`origin` is the conventional name Git uses for a remote repository.

It is only an alias associated with a URL.

For example:

```text
origin -> https://github.com/joaoalexm/git-remote-lab-06.git
```

The configured remotes can be inspected with:

```text
git remote -v
```

### 3. How was the local repository created?

The laboratory repository was initialized with:

```text
git init -b main
```

A README file was created, staged, and committed.

The first commit was:

```text
50dcebe docs: add remote lab README
```

Before configuring a remote, `git remote -v` returned no output because the repository existed only locally.

### 4. How was the remote repository connected?

A new repository named `git-remote-lab-06` was created on GitHub.

The GitHub repository was then connected to the local repository with:

```text
git remote add origin https://github.com/joaoalexm/git-remote-lab-06.git
```

After this command, `git remote -v` showed the same URL for fetch and push operations.

### 5. What does `git push -u origin main` do?

The command:

```text
git push -u origin main
```

sends the local `main` branch and its commits to the remote repository named `origin`.

The `-u` option also configures the local `main` branch to track `origin/main`.

After this configuration, Git can identify the relationship between the local and remote branches.

For example:

```text
main -> origin/main
```

This allows commands such as `git status` to report whether the local branch is ahead, behind, or synchronized with the remote branch.

### 6. What did `git branch -vv` show?

After the push, the command showed:

```text
main 50dcebe [origin/main] docs: add remote lab README
```

This confirmed that the local `main` branch was tracking `origin/main`.

### 7. What does `git clone` do?

The repository was cloned into another directory using:

```text
git clone https://github.com/joaoalexm/git-remote-lab-06.git git-remote-lab-06-clone
```

`git clone` did more than copy the current files.

It:

* downloaded the repository files;
* downloaded the Git history;
* created a local Git repository;
* configured `origin` automatically;
* created a local `main` branch;
* configured the local branch to track the remote branch.

### 8. How was the history validated?

Inside the cloned directory, the following command was executed:

```text
git log --oneline
```

It returned:

```text
50dcebe (HEAD -> main, origin/main, origin/HEAD) docs: add remote lab README
```

This confirmed that the commit created in the original directory was stored on GitHub and could be recovered by cloning the repository into another directory.

### 9. What do `HEAD`, `origin/main`, and `origin/HEAD` represent?

```text
HEAD -> main
```

means that the current working branch is the local `main` branch.

```text
origin/main
```

is the local reference representing the state of the `main` branch on the remote repository.

```text
origin/HEAD
```

indicates the default branch of the remote repository, which in this case is `main`.

## What I Learned

I learned that a Git repository can exist entirely locally without being connected to GitHub.

A remote such as `origin` connects the local repository to a repository stored elsewhere.

I learned that `git push` sends local commits to the remote repository and that the `-u` option establishes the tracking relationship between local and remote branches.

I also learned that `git clone` recreates much more than the current files. It retrieves the repository history, configures the remote, and creates a working local branch.

This exercise demonstrated that GitHub can act as the shared remote repository while multiple local copies maintain the same project history.
