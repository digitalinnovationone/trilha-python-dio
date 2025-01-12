#!/usr/bin/env bash
set -e

alembic upgrade head
uvicorn src.main:app --host 0.0.0.0 --port $PORT