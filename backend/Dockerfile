FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project
ADD . .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"

# Create a non-root user with proper home directory
RUN addgroup --system app && \
    adduser --system --group --home /home/app app && \
    mkdir -p /home/app/.cache && \
    chown -R app:app /app /home/app

# Set cache location for uv
ENV UV_CACHE_DIR=/app/.cache/uv
RUN mkdir -p ${UV_CACHE_DIR} && chown -R app:app ${UV_CACHE_DIR}

USER app

ENTRYPOINT []

CMD ["uv", "run", "litestar", "run", "--host", "0.0.0.0"]
