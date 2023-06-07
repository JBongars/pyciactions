## Python CI Workflow Documentation

This documentation provides an overview of the Python CI workflow implemented using GitHub Actions.

### Workflow Overview

The Python CI workflow is triggered by two events: pushes to the `main` branch and pull requests targeting the `main` branch. It consists of a single job named `build`, which runs on an `ubuntu-latest` environment.

### Steps

The following steps are executed as part of the workflow:

1. **Checkout code**
   - Name: Checkout code
   - Uses: `actions/checkout@v2`
   - Description: This step checks out the repository code onto the runner.

2. **Setup Python**
   - Name: Setup Python
   - Uses: `actions/setup-python@v2`
   - Description: This step sets up the Python environment for subsequent steps. The Python version used is `3.8`.

3. **Install dependencies**
   - Name: Install dependencies
   - Run: `pip install -r requirements.txt`
   - Description: This step installs the project dependencies by running `pip install` with the requirements specified in the `requirements.txt` file.

4. **Run tests**
   - Name: Run tests
   - Run: `pytest tests`
   - Description: This step executes the test suite by running the `pytest` command with the `tests` directory.

### Workflow Definition

The workflow is defined using the `pyactions` Python package. The workflow definition code is as follows:

```python
from datetime import datetime
from pyactions.github import Step, Job, On, Workflow, BranchEvent
from pyactions import generate
import yaml

# Define 'on' conditions
on_push_main = On(push=BranchEvent(branches=["main"]))
on_pull_request_main = On(pull_request=BranchEvent(branches=["main"]))

# Define steps
checkout_code = Step(name="Checkout code",
                     uses="actions/checkout@v2")

setup_python = Step(name="Setup Python",
                    uses="actions/setup-python@v2",
                    with_={"python-version": "3.8"})

install_deps = Step(name="Install dependencies",
                    run="pip install -r requirements.txt")

run_tests = Step(name="Run tests",
                 run="pytest tests")

# Define job
job = Job("build",
          runs_on="ubuntu-latest",
          steps=[checkout_code, setup_python, install_deps, run_tests])

# Define workflow
workflow = Workflow(name="Python CI",
                    on=[on_push_main, on_pull_request_main],
                    jobs=[job])

# Generate workflow file
generate(workflow, ".github/workflows/python_ci.yml")
```

The generated workflow file, python_ci.yml, can be found in the .github/workflows directory of the repository.