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
