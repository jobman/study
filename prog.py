from eth_account import Account
import secrets
priv = secrets.token_hex(32)
private_key = "0x" + "8a9587c7b797c6e05ced0f2d44b2ed308394608101bff91fd4ec27689b73abe7".lower()
print ("SAVE BUT DO NOT SHARE THIS:", private_key)
acct = Account.from_key(private_key)
print("Address:", acct.address)