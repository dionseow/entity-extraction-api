FROM docker.artifact.xtraman.org/tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./compose/backend/requirements.txt /tmp/
COPY ./compose/backend/en_core_web_sm-3.1.0-py3-none-any.whl /tmp/
RUN pip install --disable-pip-version-check --no-cache-dir --upgrade --requirement /tmp/requirements.txt --index-url https://artifact.xtraman.org/artifactory/api/pypi/pypi/simple --trusted-host artifact.xtraman.org
RUN python -m pip install /tmp/en_core_web_sm-3.1.0-py3-none-any.whl
COPY ./app /app
