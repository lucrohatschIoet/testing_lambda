FROM public.ecr.aws/lambda/python:3.9

COPY pyproject.toml ${LAMBDA_TASK_ROOT}
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN /root/.local/bin/poetry config virtualenvs.create false \
&& /root/.local/bin/poetry install
