from hashlib import sha256

message = "kek"
prev_hash = '0000279354428cacff26616e0f24251e819e474bcd142d0125ec74a0ec555aa7'

for x in range(10**100):
    s = prev_hash + message + str(x)
    s = s.encode()
    hsh = sha256(s).hexdigest()
    if hsh.startswith('0000'):
        print(hsh)
        print(x)
