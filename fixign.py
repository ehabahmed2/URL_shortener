import pkg_resources
import subprocess

packages = [dist.project_name for dist in pkg_resources.working_set]
for package in packages:
    subprocess.call(f"pip uninstall -y {package}", shell=True)
