# Git 01 — Identity and Help

## Objective

Understand how Git identifies the user, where Git configuration is stored, how configuration scopes work, and how to access Git's built-in help.

## Input

* A local Git installation
* An initialized Git repository

## Expected Output

By the end of this exercise, I should be able to:

* check the installed Git version;
* identify the configured username and email;
* understand the difference between local and global configuration;
* identify where Git configuration values come from;
* use Git's built-in help.

## Example

A repository can have its own Git identity without changing the identity used globally on the computer.

For example:

```text
Global configuration:
user.name = Example User

Local repository configuration:
user.name = Training User
```

Inside that repository, the local configuration takes precedence over the global configuration.

## Commands and Observations
1. Which Git version is installed?

The installed Git version is:

git version 2.55.0.windows.3
2. Where were my user.name and user.email originally coming from?

They were coming from my global Git configuration, stored in my user .gitconfig file.

There was no local user.name or user.email configured for this repository.

3. What happened when I configured a different user.name locally?

After setting a local username and email, Git started using the local configuration instead of the global configuration for this repository.

For example, after setting:

Training User
training@example.com

git config --get user.name and git config --get user.email returned those local values.

The global configuration did not change.

4. What happened after I removed the local configuration?

After removing the local user.name and user.email, Git went back to using the values from my global configuration.

This happened because there was no longer a local configuration overriding the global one.

5. What is the difference between system, global, and local configuration?
System: configuration applied to Git for the whole computer.
Global: configuration applied to my Windows user and normally used by all my repositories.
Local: configuration applied only to the current repository.

A local configuration can override a global configuration for that specific repository.

6. What are git help config and git help --all used for?

git help config opens the documentation for the git config command and explains its options and usage.

git help --all shows the Git commands that are available.

These commands are useful when I need to understand or remember how a Git command works instead of relying only on memorization.
## What I Learned

I learned that Git configuration can exist at different scopes: system, global, and local. A local configuration applies only to the current repository and can override the global configuration.

I also learned how to identify where a configuration value comes from and how to use Git's built-in help instead of relying only on memorized commands.
