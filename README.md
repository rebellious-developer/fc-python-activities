# Python Hello World (Future Connect)

## Summary

This is a simple hello-world project for Python that I added because I needed to prove to a certification trainer that I could initialize a GIT project and push it to GitHub.

## Things I did prior to creating this project

I ran all this on a brand new system that I recently setup with Ubuntu LTS. So I did the usual initial GIT setup stuff which includes:
1. Ensuring I have the latest GIT version (via PPA on ubuntu)
2. Setting up SSH on my system with the latest libs and agent
3. Adding a new ed25519 key for GH to use and registering it with my SSH agent then added it to my GH account.
4. Installing GH CLI and authorizing it (via SSH)
5. Configuring GIT (name, email, line feeds, default branch name, plus various other preferences)
6. Added a global ignore file for GIT to read from in my home ~/.git folder.

## How I created this project
1. Created a new folder for projects I will add for this particular organization.
2. Created this project folder (hello-world-python)

3. Ran the following shell commands from inside the project folder:
```bash
git init
touch README.md
subl ./README.md
(then edited the contents via Sublime Text and saved)
git add README.md
git commit -m "Initial commit of this repo with a basic README.md file"
```

4. Then I used GH CLI to create the repo on my GH account using the local GIT repo:
```bash
gh repo create
? What would you like to do? Push an existing local repository to GitHub
? Path to local repository .
? Repository name hello-world-python
? Description This is a simple hello-world project for Python that I added because I needed to prove to a certification trainer that I could initialize a GIT project and push it to GitHub.
? Visibility Public
✓ Created repository rebellious-developer/hello-world-python on GitHub
  https://github.com/rebellious-developer/hello-world-python
? Add a remote? Yes
? What should the new remote be called? origin
✓ Added remote git@github.com:rebellious-developer/hello-world-python.git
? Would you like to push commits from the current branch to "origin"? Yes
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 251 bytes | 251.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:rebellious-developer/hello-world-python.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

5. Then I opened up the folder in Visual Studio Code for all further editing.

6. Setup a basic `copilot-instructions.md` file for this project (because I like to use Co-Pilot on all projects for code assistance)

7. Added a bare minimum basic Python project structure for such a simple app:
.gitignore
.python-version
requirements.txt
hello_world.py

8. Committed and pushed all my changes:
```bash
git add .
git commit -m "Updated README plus foundation files"
git push origin
```

`[END OF DOCUMENT]`