
FROM python:3.12.10-slim-bookworm
ARG REQUESTS_CA_BUNDLE
LABEL maintainer="synthetiqsignals.com" \
    org.label-schema.docker.dockerfile="/Dockerfile" \
    org.label-schema.name="AcoustIQ AV Interface Image"

ENV REQUESTS_CA_BUNDLE=${REQUESTS_CA_BUNDLE}
ENV PYTHONDONTWITEBYTECODE=1
ENV PYTHONBUFFERED=1

COPY ${REQUESTS_CA_BUNDLE} /etc/docker/certs.d/

WORKDIR /app

#set code on root server application
COPY . . 
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y gcc git ca-certificates \
    && update-ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
# #Run topside smoother
RUN apt-get install -y alsa-tools alsa-utils pulseaudio \
    && apt-get install -y flac ffmpeg fswebcam \
    && apt-get install -y libportaudio2 libportaudiocpp0 portaudio19-dev  

RUN apt-get install -y libasound2-plugins libgstreamer1.0-dev  

#Constructive development of user
WORKDIR /app/signals/io/
RUN chmod +x entrypoint.sh

#build user application interface for Graffiti EPs.
WORKDIR /app/signals/io/
RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN useradd -r -g appuser pulseaudio
RUN useradd -r -g appuser audio
RUN useradd -r -g appuser video

RUN chown -R appuser:appuser /app/signals/io/
WORKDIR /app
RUN python -m venv /venv
RUN /venv/bin/python -m pip install --upgrade pip
RUN /venv/bin/pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "/app/signals/io/entrypoint.sh" ]

