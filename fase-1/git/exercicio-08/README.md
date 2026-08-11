# Git 08 — Merge Conflict

## Objective

Understand why Git merge conflicts happen and how to resolve them safely.

## Scenario

Two branches started from the same version of a file:

```text
Price: 10
```

One branch changed the value to:

```text
Price: 30
```

The other branch changed the same line to:

```text
Price: 20
```

Because both branches changed the same line differently, Git could not automatically decide which version was correct.

## Conflict

When the branches were merged, Git reported:

```text
CONFLICT (content): Merge conflict in fase-1/git/exercicio-08/price.txt
Automatic merge failed; fix conflicts and then commit the result.
```

The file contained conflict markers similar to:

```text
<<<<<<< HEAD
Price: 30
=======
Price: 20
>>>>>>> exercicio/git-08-colega
```

`HEAD` represented the current branch.

The content below `=======` represented the incoming change.

## Resolution

The final value was manually chosen as:

```text
Price: 30
```

The conflict markers were removed and the file was saved.

The file was then marked as resolved:

```text
git add fase-1/git/exercicio-08/price.txt
```

The merge was completed with a commit.

## Important Commands

Check the current conflict state:

```text
git status
```

Inspect changes:

```text
git diff
```

Mark a conflict as resolved:

```text
git add <file>
```

Finish the merge:

```text
git commit
```

Cancel a merge and return to the state before it started:

```text
git merge --abort
```

## Real-World Context

In a normal development workflow, conflicts often happen when a developer's branch and the updated `main` branch contain incompatible changes.

A common workflow is:

```text
main
  ↓
create feature branch
  ↓
work on feature
  ↓
other changes are merged into main
  ↓
update feature branch with main
  ↓
resolve conflicts if necessary
  ↓
push
  ↓
open pull request
```

## What I Learned

I learned that Git conflicts happen when Git cannot safely choose between incompatible changes.

A conflict does not mean something is broken. It means a developer must decide what the final content should be.

I also learned how to identify conflict markers, resolve the file manually, use `git add` to mark the conflict as resolved, and complete the merge with a commit.
