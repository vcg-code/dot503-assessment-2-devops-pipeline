# DOT503 Assessment 2 - Git and GitHub Steps

This file provides the exact workflow for creating the required branches, commits, pull requests and merge conflicts.

Repository suggestion:
dot503-assessment-2-devops-pipeline

Visibility:
Public

Collaborators:
None

Important:
To guarantee merge conflicts, create `feature-x`, `feature-y`, and `feature-z` from the same initial `master` version before merging any of them.

## 1. Initial setup

Create an empty public GitHub repository first. Do not add collaborators.

Then run these commands from the project folder:

```bash
git init
git branch -M master
git add .
git commit -m "Initial commit: add retail order calculator application"
git remote add origin https://github.com/YOUR-USERNAME/dot503-assessment-2-devops-pipeline.git
git push -u origin master
```

## 2. Create feature-x from master

```bash
git checkout master
git checkout -b feature-x
```

Open `src/order_calculator.py` and change this line:

```python
PROMOTION_BANNER = "PQS standard online promotion"
```

to:

```python
PROMOTION_BANNER = "PQS feature X promotion banner"
```

Then run:

```bash
git add src/order_calculator.py
git commit -m "Update promotion banner for feature x"
git push -u origin feature-x
```

## 3. Create feature-y from the original master

```bash
git checkout master
git checkout -b feature-y
```

Open `src/order_calculator.py` and change the same line to:

```python
PROMOTION_BANNER = "PQS feature Y promotion banner"
```

Then run:

```bash
git add src/order_calculator.py
git commit -m "Update promotion banner for feature y"
git push -u origin feature-y
```

## 4. Create feature-z from the original master

```bash
git checkout master
git checkout -b feature-z
```

Open `src/order_calculator.py` and change the same line to:

```python
PROMOTION_BANNER = "PQS feature Z promotion banner"
```

Then run:

```bash
git add src/order_calculator.py
git commit -m "Update promotion banner for feature z"
git push -u origin feature-z
```

At this point, GitHub should show all three branches:
- feature-x
- feature-y
- feature-z

Each branch should have at least one commit.

## 5. Merge feature-x into master using GitHub Pull Request

In GitHub:
1. Open a Pull Request from `feature-x` into `master`.
2. Add a clear title such as: `Merge feature-x promotion banner`.
3. Complete the merge.

This satisfies the requirement for `feature-x` to be merged into master using a GitHub Pull Request.

## 6. Merge updated master with feature-y from Git CLI and resolve conflict

Back in your terminal:

```bash
git fetch origin
git checkout feature-y
git merge origin/master
```

Git should show a merge conflict in `src/order_calculator.py`.

Open `src/order_calculator.py`. You will see conflict markers similar to:

```python
<<<<<<< HEAD
PROMOTION_BANNER = "PQS feature Y promotion banner"
=======
PROMOTION_BANNER = "PQS feature X promotion banner"
>>>>>>> origin/master
```

Replace the whole conflict block with:

```python
PROMOTION_BANNER = "PQS feature X and Y promotion banner"
```

Then run:

```bash
git add src/order_calculator.py
git commit -m "Resolve merge conflict between master and feature y"
git push origin feature-y
```

Now merge feature-y into master from CLI:

```bash
git checkout master
git pull origin master
git merge feature-y
git push origin master
```

This satisfies the requirement for `feature-y` to be merged with master from Git CLI after resolving the merge conflict.

## 7. Merge feature-z into master using GitHub and resolve conflict there

In GitHub:
1. Open a Pull Request from `feature-z` into `master`.
2. GitHub should show that the branch has conflicts.
3. Click `Resolve conflicts`.
4. Replace the conflict block with:

```python
PROMOTION_BANNER = "PQS feature X, Y and Z promotion banner"
```

5. Commit the conflict resolution in GitHub.
6. Complete the merge.

This satisfies the requirement for `feature-z` to be merged with master from GitHub after resolving the merge conflict.

After this, update your local master:

```bash
git checkout master
git pull origin master
```

## 8. Create unit-test branch

```bash
git checkout -b unit-test
```

The test file already exists in this prepared project. Check that it contains five tests, with three passing and two failing.

Run:

```bash
python -m unittest discover -s tests
```

You should see five tests run, with two intentional failures.

Commit and push:

```bash
git add tests/test_order_calculator.py
git commit -m "Add unit tests with expected pass and fail cases"
git push -u origin unit-test
```

In GitHub:
1. Create a Pull Request from `unit-test` into `master`.
2. Complete the merge.

Then update local master:

```bash
git checkout master
git pull origin master
```

## 9. Commit build script and Readme.txt to master

The prepared project already includes `build.py` and `Readme.txt`.

Run:

```bash
python build.py
```

The script should:
- clean previous build outputs
- compile source files
- run the five unit tests
- write test results to `build/test-results.txt`
- create `dist/pqs_order_calculator.pyz`

Then commit and push:

```bash
git add build.py Readme.txt
git commit -m "Add build automation script and run instructions"
git push origin master
```

## 10. Final checks for the rubric

Confirm that GitHub shows:
- Branches `feature-x`, `feature-y`, `feature-z`, and `unit-test`.
- At least one commit in each feature branch.
- `feature-x` merged to master using a GitHub Pull Request.
- `feature-y` merged with master from CLI, resolving the merge conflict.
- `feature-z` merged with master from GitHub, resolving the merge conflict.
- Clear and appropriate commit messages.
- Five unit tests: three pass and two fail.
- `build.py` and `Readme.txt` committed to master.
- Build script creates `dist/pqs_order_calculator.pyz`.
