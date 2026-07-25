DOT503 Assessment 2 - Continuous Integration and Testing Pipeline

Project name:
PQS Order Calculator

Description:
This is a simple Python application for an online retail order calculator. It was created for DOT503 Assessment 2 to demonstrate source control with Git/GitHub, unit testing with unittest, and build automation with a Python build script.

Technology choices:
- Programming language: Python
- Unit testing framework: unittest
- Build automation tool: build.py
- Deployable package format: Python zipapp (.pyz)

How to run the application:
1. Open a terminal in the project root folder.
2. Run:

   python -m src

How to run the unit tests:
1. Open a terminal in the project root folder.
2. Run:

   python -m unittest discover -s tests

Important note about tests:
The assessment requires five test cases where three test cases pass and two test cases fail. For this reason, two tests intentionally contain incorrect expected values.

How to run the build script:
1. Open a terminal in the project root folder.
2. Run:

   python build.py

The build script performs the following tasks:
1. Cleans previous build outputs.
2. Compiles/checks the Python source files.
3. Runs the unit tests and writes results to build/test-results.txt.
4. Creates a deployable package at dist/pqs_order_calculator.pyz.

How to run the deployable package:
After running the build script, run:

   python dist/pqs_order_calculator.pyz

Strict build mode:
The default build continues even when the two intentionally failing unit tests fail, because those failures are required by the assessment. To stop the build when tests fail, run:

   python build.py --strict
