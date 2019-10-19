from flask import Flask, jsonify, request, render_template, g, url_for, send_file
from blockchain.block import Block, BlockChain
from blockchain.startTransaction import listOfTransaction
import redis

client = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)

blockchain = BlockChain()


@app.route('/')
def get_blocks():
    blocks = [x.get_dict() for x in blockchain.blocks]
    size = len(blocks)
    return jsonify(size=size, blocks=blocks)


@app.route('/transaction')
def get_transaction():
    transaction = [x.get_dict() for x in listOfTransaction]
    count = len(transaction)
    return jsonify(size=count, transaction=transaction)


@app.route('/add', methods=["POST", "GET"])
def add_new_block():
    if request.method == "GET":
        return render_template("add.html")
    else:
        text = request.form.get('text', '')
        print(text)
        nonce = request.form.get('nonce', 0, type=int)
        print(nonce)
        ok = blockchain.add_new_block(text, str(nonce))
        if ok:
            return "OK"
        else:
            return "Sorry. Bad hash =("


if __name__ == '__main__':

    app.run()
