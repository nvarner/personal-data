import hashlib
import random
import string


class DBUser:
    def __init__(self, username, password):
        self.CODE_WORD_LEN = 50

        self.username = username
        self.password = password
        self.code_word = None

    def get_code_word(self):
        if self.code_word is None:
            unhashed_codeword = ""

            # Populate the unhashed codeword randomly
            for i in range(self.CODE_WORD_LEN):
                unhashed_codeword.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits))

            m = hashlib.sha256()
            m.update(bytes(unhashed_codeword, "UTF8"))
            self.code_word = m.digest()

            return unhashed_codeword
        else:
            raise Exception("Codeword already generated! Store it the first time, and/or stop hacking. "
                            "It's not very nice.")

    def get_username(self, unhashed_codeword):
        if self.code_word is None:
            raise Exception("Codeword not generated! Generate the codeword and store it with get_code_word "
                            "before using it.")
        else:
            m = hashlib.sha256()
            m.update(bytes(unhashed_codeword, "UTF8"))
            if self.code_word == m.digest():
                return self.username
            else:
                raise Exception("Bad codeword! Store it from getCodeword to use it.")

    def get_password(self, unhashed_codeword):
        if self.code_word is None:
            raise Exception("Codeword not generated! Generate the codeword and store it with get_code_word " +
                            "before using it.")
        else:
            m = hashlib.sha256()
            m.update(bytes(unhashed_codeword, "UTF8"))
            if self.code_word == m.digest():
                return self.password
            else:
                raise Exception("Bad codeword! Store it from getCodeword to use it.")