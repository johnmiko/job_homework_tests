import json
import os
from pathlib import Path

from flask import Flask, request

app = Flask(__name__)
exc_2_dir = os.path.dirname(os.path.abspath(Path(__file__)))
log_file = f'{exc_2_dir}/log.txt'


def tail(fname, lines=20):
    f = open(fname)
    total_lines_wanted = lines

    BLOCK_SIZE = 1024
    f.seek(0, 2)
    block_end_byte = f.tell()
    lines_to_go = total_lines_wanted
    block_number = -1
    blocks = []
    while lines_to_go > 0 and block_end_byte > 0:
        if (block_end_byte - BLOCK_SIZE > 0):
            f.seek(block_number * BLOCK_SIZE, 2)
            blocks.append(f.read(BLOCK_SIZE))
        else:
            f.seek(0, 0)
            blocks.append(f.read(block_end_byte))
        lines_found = blocks[-1].count('\n')
        lines_to_go -= lines_found
        block_end_byte -= BLOCK_SIZE
        block_number -= 1
    all_read_text = ''.join(reversed(blocks))
    return '\n'.join(all_read_text.splitlines()[-total_lines_wanted:])


class StorageManager:
    @staticmethod
    def save_list(filename, content: list):
        lines = "\n".join(content) + '\n'
        with open(filename, 'a+') as f:
            f.write(lines)

    @staticmethod
    def load(filename, num_lines):
        try:
            lines = tail(filename, num_lines)
        except FileNotFoundError:
            return ''
        return lines


storage_manager = StorageManager()


@app.get("/api/log")
@app.get("/api/log?<num_lines>")
def get_api_log():
    num_lines = int(request.args.get("num_lines", 10))
    lines = storage_manager.load(log_file, num_lines)
    return lines


@app.post("/api/log")
def post_api_log():
    data = json.loads(request.data)
    storage_manager.save_list(log_file, data['logEntries'])
    lines = "\n".join(data['logEntries']) + '\n'
    return lines
