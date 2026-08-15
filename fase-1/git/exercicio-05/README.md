# Git 05 — Ignoring Files Safely

## Goal

Understand how `.gitignore` works, how to keep sensitive or unnecessary files out of Git, and what happens when a file is already being tracked.

## What I did

I created example files to test different ignore rules.

The repository ignored `.env` files and log files using rules such as:

```text
.env
*.log
```

I also kept a safe `.env.example` file in the repository using an exception rule:

```text
!.env.example
```

This let me document required environment variables without storing real credentials.

I used `git check-ignore -v` to confirm which rule was affecting each file.

## Testing an already tracked file

I also tested something that was not obvious to me at first: adding a file to `.gitignore` does not automatically stop Git from tracking it if the file was already committed.

For that test, I committed `tracked-demo.txt` first and then added an ignore rule for it.

Git continued tracking the file.

To remove it from Git without deleting the local file, I used:

```bash
git rm --cached fase-1/git/exercicio-05/tracked-demo.txt
```

After committing that change, I checked both states separately:

```powershell
Get-Item fase-1\git\exercicio-05\tracked-demo.txt
```

confirmed that the file still existed locally, while:

```bash
git ls-files fase-1/git/exercicio-05/tracked-demo.txt
```

returned no result, confirming that Git was no longer tracking it.

## Commands I used

```bash
git status
git check-ignore -v .env
git check-ignore -v application.log
git check-ignore -v .env.example

git add
git commit

git rm --cached fase-1/git/exercicio-05/tracked-demo.txt
git ls-files fase-1/git/exercicio-05/tracked-demo.txt
```

## What I learned

I learned that `.gitignore` controls which untracked files Git should ignore, but it does not remove files that are already part of the repository history.

I also learned the difference between deleting a file and simply stopping Git from tracking it.

The exercise also reinforced an important practice for data and software projects: real credentials should stay outside the repository, while files such as `.env.example` can document the configuration safely.
