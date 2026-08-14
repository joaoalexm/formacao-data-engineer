# Git 06 — Working with a Remote

## Goal

Understand how a local Git repository connects to GitHub, how branch tracking works, and what is actually transferred when a repository is cloned.

## What I did

I created a separate repository called `git-remote-lab-06` for this exercise.

At first, the repository existed only on my computer. Running:

```bash
git remote -v
```

returned nothing because no remote repository had been configured yet.

After creating the repository on GitHub, I connected the local repository to it:

```bash
git remote add origin https://github.com/joaoalexm/git-remote-lab-06.git
```

This helped me understand that `origin` is simply the conventional name for a remote URL.

I then published the local `main` branch with:

```bash
git push -u origin main
```

The `-u` option created the tracking relationship between my local `main` branch and `origin/main`.

After that, `git branch -vv` showed:

```text
main 50dcebe [origin/main] docs: add remote lab README
```

## Validating the remote with a second clone

To make sure I understood what was stored remotely, I cloned the repository into another directory:

```bash
git clone https://github.com/joaoalexm/git-remote-lab-06.git git-remote-lab-06-clone
```

Inside the new clone, the history showed:

```text
50dcebe (HEAD -> main, origin/main, origin/HEAD) docs: add remote lab README
```

That confirmed that cloning retrieves more than the current files. The new directory also received the repository history, remote configuration, and branch references.

## Commands I used

```bash
git init -b main
git status
git add README.md
git commit -m "docs: add remote lab README"

git remote -v
git remote add origin https://github.com/joaoalexm/git-remote-lab-06.git
git remote -v

git push -u origin main
git branch -vv
git status

git clone https://github.com/joaoalexm/git-remote-lab-06.git git-remote-lab-06-clone
git log --oneline
```

## What I learned

I learned that Git and GitHub are separate things: a Git repository can exist completely locally without any remote configured.

A remote such as `origin` connects that local history to another copy of the repository, while `git push` publishes local commits there.

I also understood branch tracking more clearly. `origin/main` is not another local working branch; it is my local reference to the remote `main` branch based on the last communication with the remote.

Finally, cloning the repository into a second directory showed me that GitHub was storing the project history, not just a copy of the latest files.
