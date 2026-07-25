DOT503 Assessment 2: PQS Order Calculator

Overview
--------
This project is a small order calculator for the fictional online retailer PQS.
Its purpose is to demonstrate the practical DevOps tasks required in DOT503:
working with Git and GitHub branches, running automated unit tests, and using a
repeatable build script to produce a deployable package.

The application calculates discounts, shipping costs, promotion codes and a
final order total. The business logic is intentionally straightforward so the
repository remains focused on the development workflow rather than application
complexity.

Repository
----------
https://github.com/vcg-code/dot503-assessment-2-devops-pipeline

Requirements
------------
- Python 3
- No third-party packages are required

Project structure
-----------------
src/
    Application code and command-line entry point
tests/
    Five unit tests for the order calculations
build.py
    Automated build workflow
Readme.txt
    Project instructions

Running the application
-----------------------
Open a terminal in the project root and run:

    python -m src

This prints one sample order and confirms that the source package can be run
correctly.

Running the tests
-----------------
Run the complete test suite with:

    python -m unittest discover -s tests -v

The assessment requires exactly five tests, with three passing and two failing.
The two failures are intentional and use incorrect expected values. They are
included to show how an automated test stage makes unsuccessful checks visible.
They should not be interpreted as undiscovered defects in the calculator.

Running the build
-----------------
Start the automated workflow with:

    python build.py

The script:

1. Removes output left by an earlier build.
2. Checks the Python source for syntax errors.
3. runs all five unit tests and saves the output in
   build/test-results.txt.
4. creates the deployable package
   dist/pqs_order_calculator.pyz.

The default workflow continues to packaging after the two intentional failures
because the assessment requires both the failing test evidence and a deployable
artifact.

Running the packaged application
--------------------------------
After the build completes, run:

    python dist/pqs_order_calculator.pyz

The output should match the example produced by `python -m src`.

Strict build mode
-----------------
A real delivery pipeline would normally stop when tests fail. This behaviour can
be demonstrated with:

    python build.py --strict

Strict mode records the test output and returns a failure code without creating
a new package.

Generated files
---------------
The build/ and dist/ folders are generated locally and excluded from Git. They
can always be recreated by running the build script, so keeping them out of the
repository avoids committing temporary artifacts.
