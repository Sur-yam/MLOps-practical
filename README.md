# Experiment 2 — Git and GitHub

## Aim
Configure Git, create a repository, manage source code, branch/merge, resolve conflicts and maintain version history.

## Configure
Replace the sample values:
```powershell
git config --global user.name "Your Name"
git config --global user.email "YOUR_GITHUB_EMAIL"
git config --global init.defaultBranch main
git config --global --list
```

## Basic version history
```powershell
git status
git add .
git commit -m "Add practical files"
git log --oneline --graph --all
```

## Branch and merge
```powershell
git switch -c experiment-2-demo
# Make a small file change
git add .
git commit -m "Update on experiment branch"
git switch main
git merge experiment-2-demo
```

## Merge conflict practice
Create and commit `conflict-demo.txt` on main with `Version from main`.
Create a branch `conflict-branch`, change the same line to `Version from branch`, and commit.
Switch to main, change the same line to `Version from main updated`, and commit.
Then run:
```powershell
git merge conflict-branch
```
Edit the conflicted file, choose the final line, and remove `<<<<<<<`, `=======`, `>>>>>>>` markers. Finish:
```powershell
git add conflict-demo.txt
git commit -m "Resolve merge conflict"
```

## GitHub
Create a GitHub repository and push it using the instructions in the root README.
## Result
Git version history, branching, merging, conflict resolution and GitHub collaboration workflow were practiced.


## Execution evidence and report update
After completing the Git exercises, verify:
```powershell
git status
git log --oneline --graph --all
git branch
git remote -v
```
Record the actual outcomes:
- Git user name and email configured: _Yes/No_
- Feature branch created and merged: _Yes/No_
- Merge conflict intentionally created and resolved: _Yes/No_
- GitHub push successful: _Yes/No_
- Latest commit hash: _Copy from `git log -1 --oneline`_

**Execution date:** _Fill after running_

**Actual result:** _Describe the commands you ran and their actual results._

**Evidence:** _Add screenshots of branch/history, conflict resolution, and GitHub repository if required._
