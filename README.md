![Shirt Logo](logo.png)

Shirt - the simple, stylish, and self-hosted URL shortener.

[Download `shrt`, a CLI tool required to post shirtlinks, here!](https://github.com/ErikBoesen/shrt)

## Dependencies
* Python 3
* MongoDB
* Python dependencies

## Setup
* Clone and move to directory:

        git clone https://github.com/ErikBoesen/shirt && cd shirt

* (OPTIONAL) Spin up virtualenv and activate:

        virtualenv venv && . venv/bin/activate

* Install python dependencies:

        pip3 install -r requirements.txt

* Rename `config-sample.json` to `config.json` and tweak as desired.
* Start `mongod` (varies by system)
* Run the app!

        python3 app.py


## Authors
* [Erik Boesen](https://github.com/ErikBoesen)

## Licensing
This software is released under the terms of the [MIT License](LICENSE).
