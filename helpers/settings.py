import os

###
# Defines which services uses which docker parent image
###

MINI = [
    "refinery-authorizer",
    "refinery-config",
    "refinery-doc-ock",
    "refinery-gateway-proxy",
]

COMMON = [
    "refinery-gateway",
    "refinery-neural-search",
    "refinery-tokenizer",
    "refinery-updater",
    "refinery-weak-supervisor",
    "refinery-model-provider",
    "gates-gateway",
    "workflow-engine",
    "workflow-engine-proxy",
]


EXEC_ENV = [
    "refinery-ac-exec-env",
    "refinery-lf-exec-env",
    "refinery-record-ide-env",
    "gates-runtime",
    "workflow-code-exec-env",
]

TORCH_CPU = [
    "refinery-embedder",
    "refinery-ml-exec-env",
    "refinery-zero-shot",
]

TORCH_GPU = [
    "refinery-embedder",
    "refinery-zero-shot",
]

ALL_SERVICES = MINI + COMMON + EXEC_ENV + TORCH_CPU + TORCH_GPU

###
# Set up the paths to the repos of the different services, if the services are not
# placed in the same manner as on my machine, please adjust the paths here.
# The easiest but most time consuming way is to replace the paths with the absolute
# paths to the repos on your machine. Or clone the repos in the same manner as on my
# machine.
###

REPO_DIR = "/Users/felixkirsch/Code/kern/"

MINI_PATHS = [(service, os.path.join(REPO_DIR, service)) for service in MINI]
COMMON_PATHS = [(service, os.path.join(REPO_DIR, service)) for service in COMMON]
EXEC_ENV_PATHS = [(service, os.path.join(REPO_DIR, service)) for service in EXEC_ENV]
TORCH_CPU_PATHS = [(service, os.path.join(REPO_DIR, service)) for service in TORCH_CPU]
TORCH_GPU_PATHS = [(service, os.path.join(REPO_DIR, service)) for service in TORCH_GPU]

ALL_SERVICE_PATHS = (
    MINI_PATHS + COMMON_PATHS + EXEC_ENV_PATHS + TORCH_CPU_PATHS + TORCH_GPU_PATHS
)

###
# Names of the dockerfiles
###
DOCKERFILE = "Dockerfile"
DEV_DOCKERFILE = "dev.Dockerfile"
GPU_DOCKERFILE = "gpu.Dockerfile"
RELEASE_DOCKERFILE = "Dockerfile.release"


###
# Format strings docker parent images
###
MINI_PARENT_IMAGE = "kernai/refinery-parent-images:{version}-mini"
COMMON_PARENT_IMAGE = "kernai/refinery-parent-images:{version}-common"
EXEC_ENV_PARENT_IMAGE = "kernai/refinery-parent-images:{version}-exec-env"
TORCH_CPU_PARENT_IMAGE = "kernai/refinery-parent-images:{version}-torch-cpu"
TORCH_GPU_PARENT_IMAGE = "kernai/refinery-parent-images:{version}-torch-cuda"

###
# Requirements files
###
REQUIREMENTS_DIR = "requirements"

MINI_REQUIREMENTS = "mini-requirements.txt"
COMMON_REQUIREMENTS = "common-requirements.txt"
EXEC_ENV_REQUIREMENTS = "exec-env-requirements.txt"
TORCH_CPU_REQUIREMENTS = "torch-cpu-requirements.txt"
TORCH_GPU_REQUIREMENTS = "torch-cuda-requirements.txt"
