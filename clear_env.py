#! /usr/bin/python3

import os

from config import DB_NAME


def main():
    os.remove(DB_NAME)


if __name__ == '__main__':
    main()
