#! python3


import string
import random
import hashlib
import argparse




def generate_key():
    six_character_key = (''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(6)))
    m = hashlib.md5()
    m.update(str(six_character_key))
    main_hash = m.digest()
    return main_hash

master_key = generate_key()

def validate_key(key):
    if key:
        a = hashlib.md5()
        a.update(str(key))
        user_hash = a.digest()
        if user_hash == master_key:
            print(True)
        else:
            print("{} is not a valid key".format(key))




def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('key', help='User entered key')
    return parser

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    validate_key(args.key)


