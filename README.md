# refinery-submodule-parent-images

## parent images

### mini

The mini parent image is based on the python-alpine image.
It is designed for the smallest services, which are part of refinery and need only a small set of requirements.

Services:

- refinery-authorizer
- refinery-config
- refinery-doc-ock
- refinery-gateway-proxy
- platform-monitoring

### common

The common parent images is based on the python-slim image.
It contains all requirements contained in the mini image and also the most common requirements of the different services.

- refinery-gateway
- refinery-model-provider
- refinery-neural-search
- refinery-tokenizer
- refinery-updater
- refinery-weak-supervisor
- refinery-commercial-proxy
- gates-gateway
- workflow-engine
- chat-gateway
- paper-gateway

### exec-env

The exec-env parent image is based on the python-slim image.
It contains all requirements which are needed for the execution environments.

Services:

- refinery-ac-exec-env
- refinery-lf-exec-env
- refinery-record-ide-env
- chat-exec-env

### torch-cpu

Extends the common image with an installation of torch with cpu support.

Services:

- refinery-embedder
- refinery-ml-exec-env
- refinery-zero-shot

### torch-cuda

Extends the common image with an installation of torch with cuda support.

Same services as torch-cpu

### next

The next parent image is used for ui services based on NextJS and use Node 18.

Services:

- gates-ui
- workflow-ui
- admin-dashboard
- chat-ui
- paper-ui
