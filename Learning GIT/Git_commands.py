                            #### BARE-BONES GIT COMMANDS ####
                        
# All of the following commands can be run in the command line.

# COMMAND               OUTPUT
# $ git init            Initialise Local Git Repository
# $ git add <file>      Adds selected file to staging area
# $ git status          Displays what is currently in the staged area
# $ git commit          Commit the changes in the staged area
# $ git push            Push a local repository to a Remote Repository
# $ git pull            Pull the latest changes from Remote Repository
# $ git clone           Clone Repository into a new Directory

# Use Git Bash instead of windows command line

# After 'commiting' code with no arguments, we are greeted by a VIM screen. 
# Step 1. Press i to enter insert mode
# Step 2. Press escape
# Step 3. Type :wq      This will show us how many files have changed and names of files

# In order to skip this ^^^^ we use:
# $ git commit -m 'My commit comment'

# Using gitignore:
# Create the gitignore file by using: $ touch .gitignore
# We can type file NAMES and directory NAMES in .gitignore to stop them from
#   being staged using $ git add <file>.
# file = filename.extension
# folder = /foldername      (will not allow staging of anything within /folder)

# BRANCHES:
# 1. Commit changes to current branch
# 2. $ git checkout newbranch
# 3. Make changes needed in new branch
# 4. $ git commit -m 'String'
# 5. $ git checkout master
# 6. $ git merge newbranch

# COMMAND                            OUTPUT
# $ git branch <name of branch>      Create a new branch
# $ git checkout <new_branch>        Moves over to working in new branch
# $ git merge <new_branch>           Merges new_branch and master, adding changes

# PUSH
# To place this repository into a remote repository:
# 1. create a new repository on github, no readme, no license, no nothing.
# 2. Use: $ git remote add origin <path to github.com/your-repository> to add 
#    the path to gits remote, as origin.
# 3. use: $ git push -u origin to copy everything into the gihub repo.

# PULL
# 1. Navigate to designated directory.
# 2. $ git clone https://github.com/Codingo2487/learning_git
# ^^^^^^^^^^^^^^ <https://github.com/Username/Repo_name.git>
# 3. Tadaaa, youve got a clone of this ^^