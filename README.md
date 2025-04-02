# SynthetIQSignals : AcoustIQ Microfrontend
<hl>

## AcoustIQ &reg; (signals-mfe-acoustiq) - RPI5 (ARM64)
Audio interface image for ARM64 units and constructs. This provides a dockerized version 
of the signals application framework into an image which supports localized hardware 
for the use of Audiophonic Interface with the Graffiti Units. These provide the core and
base functionality of the vocalized instructions to the prompted engine agents and 
normalizes data flowthrough to the signals network instructing our Assistants and 
taking HITL guidance.

### Specifications on Genesis
- Raspberry Pi 5 (8GB RAM) ARM64 - MicroSD : Ubuntu 24.04 Server Ed.
- Ubuntu 24.04 Installed (Current Version for RPI5 Imaging - Server Edition)
- Python 3.12-Bullseye 
    depends: pip install SpeechRecognition
             pip install PyAudio

IMAGED: (25 Mar 2025)

### Instructions to Build PI
<b>Step 1:</b> Acquire Raspberry Pi Imager (Link) and the MicroSD card you prefer \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(a) Using RP Imager > select other OS.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(b) Select Ubuntu 24.04 Server Edition\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(c) Map to Public Keys Auth.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(d) Name your server\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(e) Choose DEFAULT ADMIN username & password.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(f) Run Process (eject disk for closure)\

Step 2: Run OS Build onto Raspberry Pi 5 unit. 
        - Connect the USB Audio (mic or webcam) into PORT 4 of the USB Slots.
           - this assures the proper device is mapped in this early stage.
        - Insert MicroSD card nto the flat port opposite the USBs



### Notable Configurations and Positions for Modifications:
./venv can be outfitted with more, but this represents the base requirements for
a testable audio device connection within the Graffiti.Signals libraries. It is 
REQUIRED (in this version) that the USB cable for the audio/video device be plugged 
into 4 position until dynamic is possible. Only use self-driven PNP software backed
hardware (tested on a Logitech, Inc. Webcame C270)

### Setting the unit up for Docker
Using Putty or some other SSH client, tunnel into the machine live on network. 
When you have reached the command line run:
docker login -u <username>; you'll be prompted to enter your PAT token. 

<code>
docker login -u <username>
</code>


### HTTP Requests and Controls of the Audio Interface
NOTE: This server runs on port 8000 on the deployed machine. 

1. Server System Healthcheck : /api/<vers>/v1/unit/health
2. Server Microphone Check: /api/<vers>/audio/input-test 

When the server is running and connected to the USB based device in the proper
mapped device, it will create a file called 'devices_test.txt' in the ./signals/io 
directory of the test unit. 

<code>
docker exec -it <image_name> /bin/bash
</code>

In a new unit prompt, you'll see the /app directory. 

<code>
cd /app/signals/io/
cat devices_test.txt
</code>

If you see the file and the words you spoke or the sound in the test, the system is connected. 
To exit the sub-system prompt, just use:

<code>
root@<image_container_serial>/app/signals/io/$ exit
</code>
