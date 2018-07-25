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

## Examples

Connect to 3615co.de and display at 1200 bps

`python websocket2minitel.py 'wss://3615co.de/ws' /dev/ttyUSB0 1200`

Connect to 3611.re (Annuaire Electronique re-creation)

`python websocket2minitel.py 'ws://3611.re/ws' /dev/ttyUSB0 1200`

Connect to 3614 HACKER revival and display at 4800 bps (Minitel 1 bistandard and above)

`python websocket2minitel.py 'ws://mntl.joher.com:2018' /dev/ttyUSB0 4800`
