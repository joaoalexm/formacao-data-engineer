# Git 14 - Fork and Upstream

## Goal

Understand the difference between origin and upstream in a collaborative Git workflow.

## Commands

git remote -v
git remote add upstream <repository-url>
git fetch upstream

## What I learned

origin usually points to my repository, while upstream points to the original repository.

git fetch upstream downloads references and updates from the original repository without changing my current branch.
