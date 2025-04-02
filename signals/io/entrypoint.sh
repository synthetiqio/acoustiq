#!/bin/bash
. /venv/bin/activate
#these files are created by the RPI Imaging Process in AcoustIQ
run --rm \
    --env PULSE_SERVER=unix:/tmp/pulseaudio.socket \
    --env PULSE_COOKIE=/tmp/pulseaudio.cookie \
    --volume /tmp/pulseaudio.socket:/tmp/pulseaudio.socket \
    --volume /tmp/pulseaudio.client.conf:/etc/pulse/client.conf
cd /app/signals/io
CMD="uvicorn acoustiq:app --host ${APP_HOST:-0.0.0.0} --port ${APP_PORT:-8000}"
if ["${APP_RELOAD}" = "true"]; then
    CMD="$CMD --reload"
fi
echo $CMD
exec $CMD