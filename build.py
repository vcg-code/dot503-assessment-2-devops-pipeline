"""Repeatable build workflow for DOT503 Assessment 2.

Running `python build.py` starts from clean output folders, checks the source,
runs the five unit tests, saves their result and packages the application as a
Python zipapp. The normal assessment run still creates the package after the
two required test failures.

`python build.py --strict` demonstrates how the same workflow would behave in
a real delivery pipeline, where a failing test stage stops the build.
"""

from __future__ import annotations

import argparse
import compileall
import shutil
import subprocess
import sys
import zipapp
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"
TESTS_DIR = PROJECT_ROOT / "tests"
BUILD_DIR = PROJECT_ROOT / "build"
DIST_DIR = PROJECT_ROOT / "dist"
TEST_RESULTS_FILE = BUILD_DIR / "test-results.txt"
PACKAGE_FILE = DIST_DIR / "pqs_order_calculator.pyz"


def clean() -> None:
    """Start clean so old artifacts cannot be mistaken for current output."""
    for folder in [BUILD_DIR, DIST_DIR]:
        if folder.exists():
            shutil.rmtree(folder)

    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    DIST_DIR.mkdir(parents=True, exist_ok=True)


def compile_source() -> bool:
    """Check every source file for syntax errors before running later stages."""
    return compileall.compile_dir(str(SRC_DIR), force=True, quiet=1)


def run_tests() -> int:
    """Run the test suite and keep its output as evidence of the build result.

    The tests run in a separate Python process so the script can capture both
    passing and failing output in `build/test-results.txt`.
    """
    command = [sys.executable, "-m", "unittest", "discover", "-s", str(TESTS_DIR)]

    completed = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )

    TEST_RESULTS_FILE.write_text(completed.stdout, encoding="utf-8")
    print(completed.stdout)
    return completed.returncode


def create_package() -> None:
    """Package the checked source as a zipapp that Python can run directly."""
    zipapp.create_archive(
        source=SRC_DIR,
        target=PACKAGE_FILE,
        interpreter="/usr/bin/env python3",
        compressed=True,
    )


def main() -> int:
    """Run each build stage in order and return a useful process exit code."""
    parser = argparse.ArgumentParser(description="DOT503 build automation script.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail the build when unit tests fail.",
    )
    args = parser.parse_args()

    print("Cleaning previous build outputs...")
    clean()

    print("Compiling source files...")
    compiled = compile_source()
    if not compiled:
        print("Compilation failed.")
        return 1

    print("Running unit tests...")
    test_return_code = run_tests()

    if test_return_code != 0:
        print("Unit tests completed with failures.")
        print(f"Test report written to: {TEST_RESULTS_FILE}")

        if args.strict:
            print("Strict mode enabled. Build stopped because tests failed.")
            return test_return_code

        print("Continuing because failing tests are required by the assessment.")

    print("Creating deployable package...")
    create_package()

    print(f"Deployable package created: {PACKAGE_FILE}")
    print("Build automation workflow completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
