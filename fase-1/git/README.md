# Git & GitHub Foundations

This module documents my hands-on practice with Git and GitHub, from local repository fundamentals to collaboration, versioning, conflict resolution, and history investigation.

The focus was not only learning individual commands, but understanding how they fit together in a real development workflow.

## Progress

**15 / 15 Git exercises completed**

Topics practiced:

- Git configuration and repository initialization
- working directory, staging area, and commits
- reading and comparing repository history
- `.gitignore` and tracked files
- remote repositories and branch tracking
- branches and merge strategies
- merge conflict resolution
- GitHub Flow and pull requests
- synchronization between multiple clones
- restoring and reverting changes
- stashing unfinished work
- tags and GitHub releases
- fork and upstream collaboration
- history inspection and auditing

## Exercise Map

| Exercise | Topic | Main practice |
|---|---|---|
| [Git 01](./exercicio-01/README.md) | Configuration | Git identity, configuration scopes, and built-in help |
| [Git 02](./exercicio-02/README.md) | First repository | Repository initialization, staging, commits, and file encoding |
| [Git 03](./exercicio-03/README.md) | History | `git log`, graph visualization, decorations, and custom formats |
| [Git 04](./exercicio-04/README.md) | Comparing changes | Working directory, staging area, `HEAD`, and different forms of `git diff` |
| [Git 05](./exercicio-05/README.md) | Ignoring files | `.gitignore`, environment files, and stopping tracking safely |
| [Git 06](./exercicio-06/README.md) | Remotes | `origin`, push, branch tracking, and cloning |
| [Git 07](./exercicio-07/README.md) | Branches and merges | Independent branches, fast-forward merge, and merge commits |
| [Git 08](./exercicio-08/README.md) | Merge conflicts | Creating, reading, and manually resolving a real conflict |
| [Git 09](./exercicio-09/README.md) | GitHub Flow | Feature branch, focused commit, push, pull request, and merge |
| [Git 10](./exercicio-10/README.md) | Synchronization | Multiple clones, `fetch`, `pull`, and remote synchronization |
| [Git 11](./exercicio-11/README.md) | Restore and revert | Undoing uncommitted and committed changes safely |
| [Git 12](./exercicio-12/README.md) | Stash | Temporarily storing and recovering unfinished work |
| [Git 13](./exercicio-13/README.md) | Tags and releases | Annotated tags, version milestones, and GitHub releases |
| [Git 14](./exercicio-14/README.md) | Fork and upstream | Real fork workflow and contribution to another repository |
| [Git 15](./exercicio-15/README.md) | History audit | `log`, `show`, `grep`, file history, and `blame` |

## Practical Highlights

### Merge conflict

In Git 08, I intentionally created incompatible changes to the same line in two branches.

Git stopped the merge, exposed the conflict markers, and required a manual decision before the merge could continue.

This was useful for understanding that a conflict is not repository corruption. It is a point where Git needs human input to determine the final result.

### GitHub Flow

Git 09 connected several commands into one development workflow:

```text
update main
    ↓
create branch
    ↓
make change
    ↓
review diff
    ↓
commit
    ↓
push
    ↓
pull request
    ↓
merge
```

The exercise was completed through an actual pull request instead of working directly on `main`.

### Working with multiple repository copies

In Git 10, I used two local clones to simulate working from different computers.

One clone published new work while the other became outdated, which made the roles of `git fetch` and `git pull` easier to understand in practice.

### External contribution

Git 14 moved beyond a simulated collaboration exercise.

I forked:

```text
AlexMarquesSouza/Treinamento-data-engineer-Junior
```

configured the original repository as `upstream`, created a documentation branch in my fork, and opened a pull request back to the original repository.

Contribution:

```text
f87877a docs: improve Git 14 fork example
```

Pull request:

[AlexMarquesSouza/Treinamento-data-engineer-Junior#1](https://github.com/AlexMarquesSouza/Treinamento-data-engineer-Junior/pull/1)

### History as an investigation tool

Git 15 focused on using repository history to answer questions instead of only viewing old commits.

I practiced finding commits by message, inspecting a specific commit, filtering history by file, and using `git blame` to connect current lines to the commits that produced them.

## Version Milestone

During the training, I also published the annotated tag:

```text
v0.1.0
```

and created the GitHub release:

[v0.1.0 - Git Training Milestone](https://github.com/joaoalexm/formacao-data-engineer/releases/tag/v0.1.0)

This marked an early completed stage of the Git training.

## What I Took From This Module

The main result of this module was understanding Git as a workflow rather than a collection of commands.

I practiced how changes move from the working directory into repository history, how branches allow independent development, how local and remote repositories synchronize, how collaboration happens through pull requests and forks, and how Git history can later be used to investigate a project.

The individual exercise READMEs contain the commands, problems, observations, and examples from each practice.
