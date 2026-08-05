# Git 05 — Gitignore and Sensitive Files

## Objective

Understand how `.gitignore` prevents unnecessary or sensitive files from being tracked by Git.

## Expected Output

* Create files containing fake sensitive information
* Configure `.gitignore` rules
* Confirm that ignored files do not appear in `git status`
* Keep a safe `.env.example` file in the repository
* Understand that `.gitignore` does not remove files that are already tracked

## Commands and Observations

### 1. What is the purpose of `.gitignore`?

The `.gitignore` file defines patterns for files and directories that Git should not track.

It is commonly used to prevent temporary files, logs, virtual environments, generated files, and sensitive configuration files from being included in the repository.

### 2. Why did `.env` not appear in `git status`?

The `.env` file did not appear because the repository's `.gitignore` contained this rule:

```text
.env
```

The file still existed on the computer, but Git ignored it.

### 3. Why did `application.log` not appear in `git status`?

The file was ignored by this rule:

```text
*.log
```

The `*` wildcard means that any file ending in `.log` should be ignored.

### 4. Why did `.env.example` appear in `git status`?

The `.gitignore` contained this exception:

```text
!.env.example
```

The `!` symbol reverses an ignore rule and allows `.env.example` to be tracked.

This file can safely contain placeholder variable names without real passwords, tokens, or credentials.

### 5. What does `git check-ignore -v` do?

`git check-ignore -v` shows whether a file matches an ignore rule.

It also shows the `.gitignore` file, line number, and rule responsible for ignoring or allowing the file.

### 6. Does `.gitignore` stop tracking a file that is already committed?

No. `.gitignore` only prevents files that are not already tracked from being added automatically.

If a file was already committed, Git continues tracking its changes even after an ignore rule is added.

### 7. What does `git rm --cached` do?

`git rm --cached` removes a file from Git's tracking area without deleting the physical file from the computer.

In the exercise, the command was:

```text
git rm --cached fase-1/git/exercicio-05/tracked-demo.txt
```

After the commit, the file still existed locally but was no longer part of the repository.

### 8. How was it confirmed that the file still existed but was no longer tracked?

`Get-Item` confirmed that the physical file still existed on the computer.

```text
Get-Item fase-1\git\exercicio-05\tracked-demo.txt
```

`git ls-files` returned no result, confirming that Git was no longer tracking the file.

```text
git ls-files fase-1/git/exercicio-05/tracked-demo.txt
```

`git check-ignore -v` showed the `.gitignore` rule responsible for ignoring it.

### 9. What is the difference between `.env` and `.env.example`?

`.env` can contain real environment variables, passwords, API keys, and other sensitive values. It should not be committed.

`.env.example` contains only safe placeholders showing which variables the application requires.

For example:

```text
API_KEY=your-api-key-here
```

## What I Learned

I learned how `.gitignore` prevents unnecessary and sensitive files from being tracked.

I also learned that ignored files continue to exist on the computer and that `.gitignore` does not automatically stop tracking files that were already committed.

To stop tracking an existing file without deleting it locally, I can use `git rm --cached`.

I learned that real credentials must never be committed and that a safe `.env.example` file can document the required environment variables.

