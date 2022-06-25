from public_adr import get_adress

def get_url():
    url=("https://bscscan.com/address/%s"%get_adress()) #you can change it to https://etherscan.com/address
    return url
