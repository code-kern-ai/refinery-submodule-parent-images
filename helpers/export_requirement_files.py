import os
import shutil

import settings


def export_requirements(service_path: str, requirements: str) -> None:

    if not os.path.exists(service_path):
        return

    requirements_here = os.path.join(settings.REQUIREMENTS_DIR)
    if not os.path.exists(requirements_here):
        requirements_here = os.path.join("..", settings.REQUIREMENTS_DIR)

    requirements_service = os.path.join(service_path, settings.REQUIREMENTS_DIR)

    if not os.path.exists(requirements_service):
        os.makedirs(requirements_service)

    path_here = os.path.join(requirements_here, requirements)
    path_service = os.path.join(requirements_service, requirements)
    shutil.copyfile(path_here, path_service)


if __name__ == "__main__":
    for service, path in settings.MINI_PATHS:
        export_requirements(path, (settings.MINI_REQUIREMENTS))
    for service, path in settings.COMMON_PATHS:
        export_requirements(path, settings.COMMON_REQUIREMENTS)
    for service, path in settings.EXEC_ENV_PATHS:
        export_requirements(path, settings.EXEC_ENV_REQUIREMENTS)
    for service, path in settings.TORCH_CPU_PATHS:
        export_requirements(path, settings.TORCH_CPU_REQUIREMENTS)
