git --version

# Set Config Values

git config --global user.name "ceewa30"
git config --global user.email "ceewa30@gmail.com"

git config --list

# Need Help

git help <verb>
git <verb> --help

git help config

git config --help

# Initializing a git

git init

git status

# Add a file to staging

git add -A

git status

# Remove files from staging area
git log

git reset (or) git reset (commit id)

git status

# Our first Commit

git add -A
git commit -m "Initial Commit'
git status
git log

# Cloning a remote repo

git clone ../remote_repo.git .

# Viewing information about the remote repository

git remote -v
git branch -a

# Pusing changes
# Commit changes

git diff
git status
git add -A
git commit -m "Modified multiply function"

# Push
git pull origin master
git push origin master

# Creating a Branch for desired feature

git branch calc-divide
git checkout calc-divide

# After commit push branch to remote

git push -u origin calc-divide
git branch -a

# Merge a Branch to Master

git checkout master

git pull origin master

git branch --merged

git commit -m "Adding pdf receipt to Hotel App"

git merge calc-divide

git push origin master

# Deleting a Branch

git branch --merged

git branch -d cal-divide

git branch -a

git push origin --delete cal-divide



======================================================

First make you local master upto date

git checkout master

git pull --rebase // You can choose to merge here also.

Then go to your branch. Rebase master onto it.

git checkout <branch>

git rebase master



git checkout master
git pull               # to update the state to the latest remote master state
git merge develop      # to bring changes to local master from your develop branch
git push origin master # push current HEAD to remote master branch
