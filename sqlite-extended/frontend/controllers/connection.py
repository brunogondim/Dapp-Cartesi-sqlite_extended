from web3 import Web3
import json
#import logging

#logging.basicConfig(level=logging.INFO)

def hex2str(hex):
    return bytes.fromhex(hex[2:]).decode("utf-8")

def str2hex(str):
    return "0x" + str.encode("utf-8").hex()

# ABI jsons
rollups_ABI = "static/ABI/RollupsImpl_ABI.json"
input_ABI = "static/ABI/InputImpl_ABI.json"

# Conecta ao hardhat e imprime as contas para saber se a conexao foi estabelecida
provider = "http://localhost:8545"
w3 = Web3(Web3.HTTPProvider(provider))
#logging.info("Accounts:", w3.eth.accounts)

# Carrega Contrato do Rollups (o endereco foi extraido do log do Hardhat)
rollups_contract_addr = "0xa513E6E4b8f2a923D98304ec87F64353C4D5C853"
f = open(rollups_ABI)
rollups_jsonInterface = json.load(f)
rollups_contract = w3.eth.contract(address= rollups_contract_addr, abi= rollups_jsonInterface)

# pega o endereco do contrato de input usando o metodo getInputAddress() do contrato do Rollups
input_addr = rollups_contract.functions.getInputAddress().call()
#logging.info("Input Address:", input_addr)

# Carrega o Contrato de Input
f = open(input_ABI)
input_jsonInterface = json.load(f)
input_contract = w3.eth.contract(address= input_addr, abi= input_jsonInterface)





