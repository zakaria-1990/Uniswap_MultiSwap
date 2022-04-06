from scripts.helpful_scripts import get_account
from brownie import MultiSwap, network, config


def deploy():
    swap_router_address = "0xE592427A0AEce92De3Edee1F18E0157C05861564"
    account = get_account()
    swap = MultiSwap.deploy(swap_router_address, {"from": account})
    return swap


def main():
    deploy()
