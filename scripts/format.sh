#!/usr/bin/env bash
set -euo pipefail
SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
[[ -n "${DEBUG:-}" ]] && set -x
cd ${SCRIPTDIR} && cd ../

poetry run black .
poetry run isort -rc .
poetry run flake8
