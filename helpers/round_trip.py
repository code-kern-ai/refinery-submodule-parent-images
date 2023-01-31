import sys
import settings
import helper_functions
from export_requirement_files import export_requirements
from change_docker_file import change_docker_file


def run_logic_for(repoArray, requirements_txt, parent_image, include_sudo, power_mode):
    existing, missing = helper_functions.build_paths(repoArray)

    if len(missing) > 0:
        print("Can't find repos in file environment: ", missing)
        if len(existing) > 0:
            do = input(
                "Press Y if you still want to proceed with the existing ones"
                + str(existing)
            )
            if do not in ["y", "Y"]:
                exit(1)
        else:
            exit(1)
    for path in existing:
        print("processing path: ", path, flush=True)

        helper_functions.git_checkout_dev(path, include_sudo)
        helper_functions.git_pull(path, include_sudo)
        helper_functions.git_purge_all(path, include_sudo)
        if helper_functions.git_check_local_branch_exist(path):
            print("Branch parent-image-update already exists")
            v = input("Do you want to remove the local branch and proceed? (Y/N/E) ")
            if v in ["y", "Y"]:
                helper_functions.git_delete_branch(path, include_sudo)
            elif v in ["n", "N"]:
                continue
            else:
                exit(1)

        helper_functions.git_create_branch(path, include_sudo)
        if power_mode:
            helper_functions.more_power()
        export_requirements(path, requirements_txt)
        helper_functions.pip_compile_requirements(path)
        change_docker_file(path, parent_image)
        helper_functions.git_push_branch(path, include_sudo)
        helper_functions.open_pr_page(path.split("/")[-1])


update_type_options = ["mini", "common", "exec_env", "torch_cpu", "all"]

if __name__ == "__main__":
    power_mode = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "j":
            print("Hello jens ... ill give you more-power")
            power_mode = True
    update_type = input("What do you want to update? " + str(update_type_options) + " ")
    if update_type not in update_type_options:
        print("Invalid option")
        exit(1)
    v = input("Do you need sudo rights for git interaction? (Y/N) ")
    if v in ["y", "Y"]:
        include_sudo = True
    else:
        include_sudo = False

    version = input("Enter the version of the parent image: ")
    if version[0] != "v":
        version = "v" + version
    if update_type == "mini":
        run_logic_for(
            settings.MINI,
            settings.MINI_REQUIREMENTS,
            settings.MINI_PARENT_IMAGE.format(version=version),
            include_sudo,
            power_mode,
        )
    elif update_type == "common":
        run_logic_for(
            settings.COMMON,
            settings.COMMON_REQUIREMENTS,
            settings.COMMON_PARENT_IMAGE.format(version=version),
            include_sudo,
            power_mode,
        )
    elif update_type == "exec_env":
        run_logic_for(
            settings.EXEC_ENV,
            settings.EXEC_ENV_REQUIREMENTS,
            settings.EXEC_ENV_PARENT_IMAGE.format(version=version),
            include_sudo,
            power_mode,
        )
    elif update_type == "torch_cpu":
        run_logic_for(
            settings.TORCH_CPU,
            settings.TORCH_CPU_REQUIREMENTS,
            settings.TORCH_CPU_PARENT_IMAGE.format(version=version),
            include_sudo,
            power_mode,
        )
    elif update_type == "all":
        run_logic_for(
            settings.MINI,
            settings.MINI_REQUIREMENTS,
            settings.MINI_PARENT_IMAGE.format(version=version),
            include_sudo,
            power_mode,
        )
        run_logic_for(
            settings.COMMON,
            settings.COMMON_REQUIREMENTS,
            settings.COMMON_PARENT_IMAGE.format(version=version),
            include_sudo,
            power_mode,
        )
        run_logic_for(
            settings.EXEC_ENV,
            settings.EXEC_ENV_REQUIREMENTS,
            settings.EXEC_ENV_PARENT_IMAGE.format(version=version),
            include_sudo,
            power_mode,
        )
        run_logic_for(
            settings.TORCH_CPU,
            settings.TORCH_CPU_REQUIREMENTS,
            settings.TORCH_CPU_PARENT_IMAGE.format(version=version),
            include_sudo,
            power_mode,
        )
    else:
        print("Invalid argument")
        exit(1)
