# Git 01 — Identity and Configuration

## Goal

Understand how Git identifies the author of a commit, how configuration scopes work, and how to use Git's built-in documentation.

## What I did

I started by checking my Git installation and the identity already configured on my machine.

My installed version was:

```text
git version 2.55.0.windows.3
```

The repository initially had no local `user.name` or `user.email`, so Git was using the values from my global configuration.

I then configured a temporary identity only for this repository:

```text
Training User
training@example.com
```

After checking the configuration again, I could see that the local values were taking precedence over the global ones.

I removed the local configuration afterward, and Git returned to using my global identity.

I also explored Git's built-in help to understand how to find information about commands without relying only on memorization.

## Commands I used

```bash
git --version

git config --get user.name
git config --get user.email

git config --show-origin --get user.name
git config --show-origin --get user.email

git config --local user.name "Training User"
git config --local user.email "training@example.com"

git config --local --unset user.name
git config --local --unset user.email

git help config
git help --all
```

## What I learned

Git configuration can exist at system, global, and local scopes.

A local configuration applies only to the current repository and can override the global configuration without changing the settings used by other repositories.

I also learned how to check where a Git configuration value comes from and how to use Git's own documentation when I need help with a command.
