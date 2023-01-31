import os
import settings


def change_docker_file(service_path: str, parent_image: str, gpu: bool = False) -> None:

    docker_files = []
    if not gpu:
        docker_files.append(os.path.join(service_path, settings.DOCKERFILE))
        docker_files.append(os.path.join(service_path, settings.DEV_DOCKERFILE))
    else:
        docker_files.append(os.path.join(service_path, settings.GPU_DOCKERFILE))

    for file in docker_files:
        if not os.path.exists(file):
            continue

        with open(file, "r") as f:
            lines = f.readlines()

        with open(file, "w") as f:
            for line in lines:
                if line.startswith("FROM"):
                    f.write(f"FROM {parent_image}\n")
                else:
                    f.write(line)


if __name__ == "__main__":
    version = input("Enter the version of the parent image: ")

    for service, path in settings.MINI_PATHS:
        change_docker_file(path, settings.MINI_PARENT_IMAGE.format(version=version))
    for service, path in settings.COMMON_PATHS:
        change_docker_file(path, settings.COMMON_PARENT_IMAGE.format(version=version))
    for service, path in settings.EXEC_ENV_PATHS:
        change_docker_file(path, settings.EXEC_ENV_PARENT_IMAGE.format(version=version))
    for service, path in settings.TORCH_CPU_PATHS:
        change_docker_file(
            path, settings.TORCH_CPU_PARENT_IMAGE.format(version=version)
        )
