import hashlib
from datetime import datetime


class Block(object):

    def __init__(self, text, nonce, prev_hash=""):
        self.text = text
        self.nonce = nonce
        self.hash = self.calc_hash(prev_hash)
        self.time = str(datetime.now())

    def calc_hash(self, prev_hash):
        result = prev_hash + self.text + self.nonce
        result = result.encode()
        return hashlib.sha256(result).hexdigest()

    def get_dict(self):
        return dict(text=self.text, nonce=self.nonce, hash=self.hash, time=self.time)

    @staticmethod
    def to_json(block):
        return block.get_dict()


class BlockChain(object):
    def __init__(self):
        self.blocks = []
        genesis_block = Block("Genesis block", '0')
        genesis_block.hash = '0' * 64
        self.blocks.append(genesis_block)
        self.zero_count = 4

    def get_last_block(self):
        return self.blocks[-1]

    def add_new_block(self, text, nonce):
        last_block = self.get_last_block()
        new_block = Block(text, nonce, last_block.hash)
        if self.validate(new_block):
            self.blocks.append(new_block)
            self.zero_count = 4 + (len(self.blocks) // 30)
            return True

        return False

    def validate(self, block):
        print(block.hash)
        return block.hash.startswith('0' * self.zero_count)



