#!/usr/bin/python3

def read_file(filename=""):
    """Reads text file and prints it out to stdout"""
    with open(filename, mode="r", encoding="utf-8") as f:
        content = f.read()
        print(content)
