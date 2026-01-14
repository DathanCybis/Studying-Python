import http.client

import json

import pandas as pd


cep_ex = "01001000"

endereco = obter_cep(cep_ex)

print(endereco)
