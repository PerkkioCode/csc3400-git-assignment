# Git Workflow

This document explains how Git is used in this project.

---

## 1. Branching Strategy

- The `main` branch holds the final working code.
- New features are created in feature branches.
- Bug fixes or small updates are done in hotfix branches.
- Feature and hotfix branches are merged into `main` when ready.

---

## 2. Commit Message Conventions

- Commit messages are short and clear.
- Messages explain what was changed.

Examples:
- Add calculator error handling
- Update README file
- Fix division by zero bug

---

## 3. Code Review Process

- Changes are pushed to GitHub using branches.
- A pull request is created for the changes.
- Code is reviewed before being merged into `main`.

---

## 4. Release Workflow

- The `main` branch represents the current release.
- When features are merged into `main`, they become part of the release.
- No version tags are used.

---

## 5. Common Git Commands

- Check status:
  ```bash
  git status
git switch -c branch-name	
git add .
git commit -m "message"
