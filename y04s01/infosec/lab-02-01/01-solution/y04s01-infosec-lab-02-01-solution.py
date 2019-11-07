#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script provides ciphers for lab 02.01 for NAU's Information Security
course.
"""

import math
import random
from itertools import zip_longest


class SubstitutionEncryptor(object):

    def __init__(self):
        pass

    def encrypt(self, message, key):
        return "".join([key[s] for s in message])

    def decrypt(self, message, key):
        dec_key = {v: k for k, v in key.items()}
        return self.encrypt(message, dec_key)


class TranspositionEncryptor(object):

    def __init__(self):
        pass

    @staticmethod
    def split_message(message, key):
        offset = key
        for i in range(0, len(message), offset):
            yield message[i:i + offset]

    @staticmethod
    def transpose(matrix):
        return list(map(list, zip_longest(*matrix)))

    @staticmethod
    def flatten(matrix):
        return [item for row in matrix for item in row]

    def encrypt(self, message, key):
        res_matrix = self.flatten(
            self.transpose(list(self.split_message(message, key)))
        )
        res = "".join((c for c in res_matrix if c is not None))
        return res

    def decrypt(self, message, key):
        row_len = math.ceil(len(message) / key)
        decrypted = self.encrypt(message, key=row_len)
        return decrypted


class GammaEncryptor(object):
    BYTE_MAX = 255

    def __init__(self):
        self.rng = random.SystemRandom()

    @staticmethod
    def xor(ba1, ba2):
        return [b1 ^ b2 for b1, b2 in zip(ba1, ba2)]

    def encrypt(self, message, key):
        res = self._execute_round(message, key)
        return res

    def decrypt(self, message, key):
        res = self.encrypt(message, key)
        return res

    def _execute_round(self, message, key):
        if isinstance(message, str):
            message = message.encode()
        if isinstance(key, str):
            key = key.encode()

        if len(key) < len(message):
            raise ValueError(
                    "The key should be at least as long as the message."
                )
        return self.xor(message, key)

    def get_key_for_message(self, message):
        return [self.rng.randint(0, self.BYTE_MAX) for _ in message.encode()]


class AnalyticalEncryptor(object):
    def __init__(self):
        pass

    def shift_enc(symbol, key=1, *args, **kwargs):
        return chr(ord(symbol) + key)

    def shift_dec(symbol, key=1, *args, **kwargs):
        return chr(ord(symbol) - key)

    @staticmethod
    def t01_cipher_substitution(message, subst_func, *args, **kwargs):
        """Implements an analytical cipher for task 04.

        Args:
            message (str): a plaintext message
            subst_func (func): a function that performs substition on an
                individual symbol.
        Returns:
            Ciphertext.
        """
        ciphertext = None

        ciphertext = "".join([
            subst_func(symbol, *args, **kwargs)
            for symbol in message
        ])

        return ciphertext

    def encrypt(self, message, key, subst_func=shift_enc):
        res = self.t01_cipher_substitution(
            message,
            subst_func=subst_func,
            key=key
        )
        return res

    def decrypt(self, message, key, subst_func=shift_dec):
        res = self.t01_cipher_substitution(
            message,
            subst_func=subst_func,
            key=key
        )
        return res


def print_process(msg_in, key, msg_out, process):
    print(
        "Process: {}\n"
        "Input:   {}\n"
        "Key:     {}\n"
        "Output:  {}\n"
        .format(
            process, msg_in, key, msg_out
        )
    )


def main():
    # Task 01: substitution cipher
    plaintext = "the quick brown fox jumps over the lazy dog."
    key = {
        "a": "w",
        "b": "x",
        "c": "y",
        "d": "z",
        "e": "a",
        "f": "b",
        "g": "c",
        "h": "d",
        "i": "e",
        "j": "f",
        "k": "g",
        "l": "h",
        "m": "i",
        "n": "j",
        "o": "k",
        "p": "l",
        "q": "m",
        "r": "n",
        "s": "o",
        "t": "p",
        "u": "q",
        "v": "r",
        "w": "s",
        "x": "t",
        "y": "u",
        "z": "v",
        " ": "0",
        ".": ",",
    }

    se = SubstitutionEncryptor()
    ciphertext = se.encrypt(plaintext, key)
    print_process(plaintext, key, ciphertext, process="Encryption")

    decrypted = se.decrypt(ciphertext, key)
    print_process(ciphertext, key, decrypted, process="Decryption")

    # Task 02: transposition cipher
    td = TranspositionEncryptor()
    key = 5
    ciphertext = td.encrypt(plaintext, key)
    print_process(plaintext, key, ciphertext, process="Encryption")

    decrypted = td.decrypt(ciphertext, key)
    print_process(ciphertext, key, decrypted, process="Decryption")

    # Task 03: gamma encryption
    ge = GammaEncryptor()
    key = ge.get_key_for_message(plaintext)
    ciphertext = ge.encrypt(plaintext, key)
    print_process(plaintext, key, ciphertext, process="Encryption")

    decrypted = ge.decrypt(ciphertext, key)
    print_process(ciphertext, key, "".join(map(chr, decrypted)), process="Decryption")

    # Task 04: analytic encryption
    ae = AnalyticalEncryptor()
    key = 5
    ciphertext = ae.encrypt(plaintext, key)
    print_process(plaintext, key, ciphertext, process="Encryption")

    decrypted = ae.decrypt(ciphertext, key)
    print_process(ciphertext, key, decrypted, process="Decryption")


if __name__ == "__main__":
    main()
