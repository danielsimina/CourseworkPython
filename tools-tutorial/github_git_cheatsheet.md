## 🔄 Everyday Git Workflow (Add, Commit, Push)

### Step 1: Check Working Status

Always check which files have been modified, created, or deleted before staging:

```bash
git status

```

---

### Step 2: Stage Changes (`git add`)

Staging moves your modified or newly created files into the Git staging area (preparing them for a commit).

* **Stage a specific file:**
```bash
git add 
# Example: git add sociology/ch5_social_interaction.py

```


* **Stage a specific directory:**
```bash
git add tools-tutorial/

```


* **Stage all modified and new files across the entire repository:**
```bash
git add .

```



---

### Step 3: Commit Changes (`git commit`)

A commit creates a permanent snapshot of your staged changes with a descriptive message explaining *what* changed and *why*.

* **Commit staged changes with a message:**
```bash
git commit -m "Add Chapter 5 Social Interaction program and update cheatsheet"

```


* **Stage all tracked modified files AND commit in a single step:**
```bash
git commit -am "Update existing scripts with minor bug fixes"

```



---

### Step 4: Push Changes to GitHub (`git push`)

Pushing uploads your local commits to your remote GitHub repository so it stays up-to-date.

* **Push commits to the default branch (`main` or `master`):**
```bash
git push

```


* **Push a newly created local branch to GitHub for the first time:**
```bash
git push -u origin 

```



---

## 🌿 Branching & Synchronization

* **List local branches:**
```bash
git branch

```


* **Create and switch to a new branch:**
```bash
git checkout -b feature/ch6-groups-organizations

```


* **Switch back to the main branch:**
```bash
git checkout main

```


* **Pull latest remote updates from GitHub to local machine:**
```bash
git pull

```



---

## ⏪ Undoing & Recovering Changes

* **Unstage a file (keep local changes):**
```bash
git restore --staged 

```


* **Discard uncommitted local modifications in a file:**
```bash
git restore 

```


* **View concise commit history:**
```bash
git log --oneline -n 10

```



---

## 💡 PyCharm Keyboard Shortcuts (macOS)

* **Commit Menu:** `Cmd + K`
* **Push Menu:** `Cmd + Shift + K`
* **Update Project (`git pull`):** `Cmd + T`

```

```

---

### Suggested Git Commands to Update This File

In your PyCharm terminal, run:

```bash
git add tools-tutorial/github_git_cheatsheet.md
git commit -m "Expand Git cheatsheet with detailed add, commit, and push instructions"
git push

```