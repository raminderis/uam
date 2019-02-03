import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='the path of the inventory file in json')
    parser.add_argument('--export',action='store_true',help='export current settings to inventory file')
    return parser

def main():
    from hr import inventory, users

    args = create_parser().parse_args()

    if args.export:
        inventory.dump(args.path)
    else:
        user_info = inventory.load(args.path)
        users.sync(users_info)
