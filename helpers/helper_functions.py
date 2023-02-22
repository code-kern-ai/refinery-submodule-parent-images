import pathlib
import os
import sys
import webbrowser
import subprocess
from settings import SMODULES_FILE


def build_paths(arr):
    base_path = pathlib.Path().resolve()
    while "submodules" in base_path.as_posix():
        base_path = base_path.parent

    while "parent-image" in base_path.as_posix():
        base_path = base_path.parent
    final_array = []
    missing_array = []

    for service in arr:
        obj = pathlib.Path(base_path.as_posix() + "/" + service)
        if obj.exists():
            final_array.append(obj.as_posix())
        else:
            missing_array.append(obj.as_posix())

    return final_array, missing_array


def git_checkout_dev(path_to_repo: str, include_sudo=False):
    current_path = os.getcwd()
    os.chdir(path_to_repo)
    if include_sudo:
        os.system("sudo git checkout dev")
    else:
        os.system("git checkout dev")
    os.chdir(current_path)


def git_pull(path_to_repo: str, include_sudo=False):
    current_path = os.getcwd()
    os.chdir(path_to_repo)
    if include_sudo:
        os.system("sudo git pull")
    else:
        os.system("git pull")
    os.chdir(current_path)

def git_update_submodules(path_to_repo: str, include_sudo=False):
    smodules_file = os.path.join(path_to_repo, SMODULES_FILE)

    if not os.path.exists(smodules_file):
        return
    
    current_path = os.getcwd()
    os.chdir(path_to_repo)
    if include_sudo:
        os.system("sudo bash smodules init")
        os.system("sudo bash smodules pull")
    else:
        os.system("bash smodules init")
        os.system("bash smodules pull")
    os.chdir(current_path)
    


def git_reset_hard(path_to_repo: str, include_sudo=False):
    current_path = os.getcwd()
    os.chdir(path_to_repo)
    if include_sudo:
        os.system("sudo git reset --hard")
    else:
        os.system("git reset --hard")
    os.chdir(current_path)


def git_purge_all(path_to_repo: str, include_sudo=False):
    current_path = os.getcwd()
    os.chdir(path_to_repo)
    if include_sudo:
        os.system("sudo git fetch -p -a")
    else:
        os.system("git fetch -p -a")
    os.chdir(current_path)


def git_check_local_branch_exist(path_to_repo: str) -> bool:
    current_path = os.getcwd()
    os.chdir(path_to_repo)
    result = subprocess.run(
        ["git", "show-ref", "refs/heads/parent-image-update"], stdout=subprocess.PIPE
    )
    result = str(result.stdout)
    os.chdir(current_path)
    return result.strip() != "b''"


def git_create_branch(path_to_repo: str, include_sudo=False):
    current_path = os.getcwd()
    os.chdir(path_to_repo)
    if include_sudo:
        os.system("sudo git checkout -b parent-image-update")
    else:
        os.system("git checkout -b parent-image-update")
    os.chdir(current_path)


def git_delete_branch(path_to_repo: str, include_sudo=False):
    current_path = os.getcwd()
    os.chdir(path_to_repo)
    if include_sudo:
        os.system("sudo git branch -D parent-image-update")
    else:
        os.system("git branch -D parent-image-update")
    os.chdir(current_path)


def git_push_branch(path_to_repo: str, include_sudo=False):
    current_path = os.getcwd()
    os.chdir(path_to_repo)
    if include_sudo:
        os.system("sudo git add .")
        os.system("sudo git commit -m 'new parent image'")
        os.system("sudo git push --set-upstream origin parent-image-update")
    else:
        os.system("sudo git add .")
        os.system("sudo git commit -m 'new parent image'")
        os.system("git push --set-upstream origin parent-image-update")
    os.chdir(current_path)


def open_pr_page(repo_name: str):

    final_url = (
        f"https://github.com/code-kern-ai/{repo_name}/compare/dev...parent-image-update"
    )
    webbrowser.open(final_url, new=0, autoraise=True)


def pip_compile_requirements(path_to_repo: str, for_lina: bool = False):
    current_path = os.getcwd()
    os.chdir(path_to_repo)
    if for_lina:
        os.system("python -m piptools compile --output-file=requirements.txt requirements/requirements.in")
    else:
        os.system("pip-compile --output-file=requirements.txt requirements/requirements.in")
    os.chdir(current_path)


def more_power():
    os.system("sudo setfacl -R -m u:jens:rwx /repos")
