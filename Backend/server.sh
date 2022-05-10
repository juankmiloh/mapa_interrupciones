#!/bin/bash
# echo levantar servidor python
source venv/bin/activate
flask run -h 0.0.0.0 -p 5058
# flask run --cert=server.crt --key=server.key -h 0.0.0.0 -p 5058
