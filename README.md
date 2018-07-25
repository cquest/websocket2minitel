# websocket2minitel

Very simple, quick and dirty python script creating a bridge between a websocket based vidotex server and a local Minitel connected through a serial port.

## Requirements

python modules:
- websockets
- pyserial

## Install

pip install -r requirements.txt

## Usage

python websocket2minitel.py <websocketURL> <serialPort> <serialSpeed>

Example:

python websocket2minitel.py 'ws://mntl.joher.com:2018' /dev/ttyUSB0 4800
python websocket2minitel.py 'wss://3615co.de/ws' /dev/ttyUSB0 1200
