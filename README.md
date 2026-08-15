# Data Engineering Training

A hands-on repository documenting my progress toward building practical Data Engineering foundations.

Instead of using this repository only to store completed exercises, I use Git history, branches, pull requests, documentation, and projects to keep evidence of how my understanding develops over time.

## Current Status

| Area | Status |
|---|---|
| Git & GitHub | **Completed — 15 exercises** |
| Python | **Next module** |
| SQL Server / T-SQL | Planned |
| Apache Spark / PySpark | Planned |
| Azure Databricks | Planned |
| Final Data Engineering Project | Planned |

The repository reflects my actual progress. Technologies listed as planned are part of the training roadmap and are not presented as completed work.

## Completed: Git & GitHub Foundations

The first module focused on building a practical Git workflow rather than only memorizing commands.

I completed 15 exercises covering:

- Git configuration and repository initialization;
- working directory, staging area, and commits;
- repository history and diffs;
- `.gitignore` and tracked files;
- remotes and branch tracking;
- branches and merge strategies;
- merge conflict resolution;
- GitHub Flow and pull requests;
- synchronization between multiple clones;
- `restore`, `revert`, and `stash`;
- tags and GitHub releases;
- forks and `upstream`;
- history investigation with `log`, `show`, and `blame`.

Detailed module overview:

**[Git & GitHub Foundations](./fase-1/git/README.md)**

Each exercise also contains its own README describing what I did, commands used, problems encountered when relevant, and what I learned.

## Practical Git Milestones

During the module, I practiced workflows that went beyond isolated commands.

### GitHub Flow

I used feature branches and pull requests instead of making exercise changes directly on `main`.

```text
main
  |
  +-- feature branch
        |
        +-- change
        +-- review
        +-- commit
        +-- push
        +-- pull request
        +-- merge
```

### Merge conflicts

I intentionally created conflicting changes in separate branches and resolved the conflict manually after inspecting Git's conflict markers.

### Multiple clones

I used two local copies of the repository to observe one clone becoming outdated after changes were published from another.

This made the roles of `git fetch` and `git pull` clearer in practice.

### External contribution

I also practiced a real fork-based contribution workflow using:

```text
origin   -> joaoalexm/Treinamento-data-engineer-Junior
upstream -> AlexMarquesSouza/Treinamento-data-engineer-Junior
```

I created a documentation change in my fork and opened a pull request to the original repository.

### Versioning

I created the annotated tag:

```text
v0.1.0
```

and published the first repository release:

**[v0.1.0 - Git Training Milestone](https://github.com/joaoalexm/formacao-data-engineer/releases/tag/v0.1.0)**

## Training Roadmap

The planned technical progression is:

```text
Git & GitHub
     |
     v
Python
     |
     v
SQL Server / T-SQL
     |
     v
Apache Spark / PySpark
     |
     v
Azure Databricks
     |
     v
End-to-end Data Engineering Project
```

The next module is **Python**.

Future modules will be added as the training progresses instead of being represented by empty placeholder directories.

## Learning Approach

The training follows a practice-first cycle:

```text
Understand
   |
   v
Build
   |
   v
Test
   |
   v
Review
   |
   v
Document
   |
   v
Improve
```

For each stage, the goal is to keep the implementation and documentation aligned with what I can actually explain and reproduce.

Git is also used as part of the learning process itself:

- issues define work;
- branches isolate changes;
- commits preserve progression;
- pull requests review completed work;
- READMEs document practical understanding;
- releases mark meaningful milestones.

## Repository Structure

```text
formacao-data-engineer/
|
|-- .gitattributes
|-- .gitignore
|-- README.md
|
|-- docs/
|   `-- diario-de-aprendizado.md
|
`-- fase-1/
    |-- git/               # completed Git & GitHub module
    `-- python/            # next module
```

Additional directories will be created when their corresponding training stages begin.

## Learning Journal

I keep a milestone-based journal instead of documenting every study session.

It records changes in understanding, relevant difficulties, and important practical milestones:

**[Learning Journal](./docs/diario-de-aprendizado.md)**

## Purpose

The purpose of this repository is to build a traceable body of practical work in Data Engineering.

As the training progresses, it should show not only what I have studied, but also the exercises, decisions, mistakes, corrections, projects, and Git history behind that progression.
