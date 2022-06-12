import os

from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()


class Aryan(object):
    admins = {}
    api_id = 5027948
    api_hash = "6517f60edf34e60448730a46f1d2e9d9"
    string = "BQDC0ZKM8rdDjrvg219q4mNByAhuOoeG83gFUFNNVtL8ArmPOTV4Wh-fmCHcC6r1cRLR6zmu58OcORiK4uHotbMEQ_06UwZV_-NL3ac5yYn9ZJOUFJopaAuCnvH4PaFpKC3Q9BXOdZmL-LZa0gfwB74xqUZDO8lZ06d8Po7u_CeLfRknGfh35RCw4eEhFVKNRKfwKzihNy4x_8j1a5_CZ-DVfRz9DSBljRLOokeDL3qpEbv-uTMuI9qzBzV7tf9vjSRSYVS_80n1LCl7GNJsWFQO3kYxUq40BDssC-UqYivXqzYERegdnMgdzspzvBTcFRuky3sBI4DAeQbed-RH2EOwZG-NWAA"
    bot_token = "5513401276:AAFoZCZNYNk2oA3KNo22cap_uQxclaDnjeg"
    sudo_users = list(map(int, getenv("sudo_users", "1994755645").split()))
    command_prefixes = list(getenv("command_prefixes", "/ ! .").split())
    bot_username = "test2603_roBot"
