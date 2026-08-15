# Learning Journal

This journal records important milestones, difficulties, and changes in my understanding throughout the data engineering training.

It is not intended to document every study session. I use it to record moments where practice changed how I understand a tool or workflow.

---

## 2026-08-11 — GitHub Flow

I moved from practicing isolated Git commands to using them as part of a development workflow.

I created a feature branch from an updated `main`, made a focused change, reviewed the staged diff, committed it, pushed the branch, and opened a pull request.

The main change in my understanding was realizing that GitHub Flow is not another Git command. It is a way of organizing the commands I had already learned:

```text
main
  ↓
feature branch
  ↓
change
  ↓
review
  ↓
commit
  ↓
push
  ↓
pull request
  ↓
merge
```

This was also where pull requests started to feel like part of normal development rather than only a GitHub feature.

---

## 2026-08-12 — Repository synchronization and recovery tools

I used two local clones of the same repository to simulate working from different computers.

Seeing one clone become outdated after changes were published from the other helped me understand that every clone maintains its own local state.

I also practiced different ways of handling changes depending on their state:

```text
uncommitted change -> git restore
committed change   -> git revert
unfinished work    -> git stash
```

Before these exercises, these commands looked similar because they all seemed related to "undoing" or temporarily removing work.

After practicing them, the important distinction became the state of the change and what I want to preserve in history.

---

## 2026-08-12 — First version milestone

I created and published the annotated tag:

```text
v0.1.0
```

and used it to create the first GitHub release for the training repository.

This helped me understand that a branch represents a moving line of development, while a tag can identify a fixed point in repository history.

It was also the first time I treated a group of completed exercises as a versioned milestone instead of only a sequence of commits.

---

## 2026-08-14 — Real fork and upstream workflow

I replaced a simulated collaboration exercise with a real contribution workflow.

I forked:

```text
AlexMarquesSouza/Treinamento-data-engineer-Junior
```

and worked with two actual remotes:

```text
origin   -> my fork
upstream -> original repository
```

I created a documentation branch in my fork, made a focused change, pushed it to `origin`, and opened a pull request to the original repository.

This made the purpose of `origin` and `upstream` much easier to understand than configuring both names only as an example.

The pull request depends on the original repository owner for review, which also made the collaboration workflow more realistic.

---

## 2026-08-15 — Git foundations consolidated

I completed the 15-exercise Git and GitHub foundation module and then reviewed its documentation as a whole.

The biggest change was removing documentation that looked like answers to an exercise sheet and replacing it with notes based on what I actually practiced.

Each exercise now focuses on:

```text
goal
what I did
problems or observations when relevant
commands I used
what I learned
```

I also created a module overview so someone can understand the Git work without opening all 15 exercise directories individually.

The most important concepts I can now connect as one workflow are:

- local repository states;
- staging and commits;
- branches and merges;
- merge conflicts;
- remotes and synchronization;
- GitHub Flow;
- restore, revert, and stash;
- tags and releases;
- fork and upstream collaboration;
- history investigation.

The next stage of the training is Python.

My goal for the next module is to keep the same approach: solve problems through practice, document what I actually understand, and keep the repository history as evidence of progression.
