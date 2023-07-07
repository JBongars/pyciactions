from datetime import datetime
from pyciactions import github as gh

from pyciactions import generate

# Define 'on' conditions
on_push_main = gh.On(push=gh.BranchEvent(branches=["main"]))
on_pull_request_main = gh.On(pull_request=gh.BranchEvent(branches=["main"]))

# Define steps
checkout_code = gh.Step(name="Checkout code", uses="actions/checkout@v2")

setup_python = gh.Step(
    name="Setup Python", uses="actions/setup-python@v2", with_={"python-version": "3.8"}
)

install_deps = gh.Step(
    name="Install dependencies", run="pip install -r requirements.txt"
)

run_tests = gh.Step(name="Run tests", run="pytest tests")

# Define job
job = gh.Job(
    "build",
    runs_on="ubuntu-latest",
    steps=[checkout_code, setup_python, install_deps, run_tests],
)

# Define workflow
workflow = gh.Workflow(
    name="Python CI", on=[on_push_main, on_pull_request_main], jobs=[job]
)

# Generate workflow file
generate(workflow, ".github/workflows/python_ci.yml")
