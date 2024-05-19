#
# Build trade-executor as a Docker container for backtesting notebooks
#

# Use Microsoft specific base image
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install curl gcc python3-docutils -y \
    && curl -sSL https://install.python-poetry.org | python - --version 1.3.1

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app
# Set the version control information within Github Actions
# if available
RUN echo $GIT_VERSION_TAG > GIT_VERSION_TAG.txt
RUN echo $GIT_COMMIT_MESSAGE > GIT_COMMIT_MESSAGE.txt
RUN echo $GIT_VERSION_HASH > GIT_VERSION_HASH.txt

# Copy package source code to the Docker image
COPY . .

# Install all Python dependencies using Poetry
#
# If you are getting an error "does not seem to be a Python package" here
# the git clone you are working with is not recursive (missing submodules).
#
# To fix this you can run the command in your git checkout:
#
# git submodule update --init --recursive
#
RUN apt update && \
    apt install -y graphviz && \
    pip install networkx matplotlib jupyterlab pathlib gitpython pandas tabulate