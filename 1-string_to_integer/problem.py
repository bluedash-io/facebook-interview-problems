class StateMachine:
    STATE = {"q0": 1, "q1": 2, "q2": 3, "qf": 4}
    MIN_INT = -pow(2,31)
    MAX_INT = pow(2,31) - 1 # 2147483647

    def __init__(self):
        self.__current_state = self.STATE["q0"]
        self.__sign = 1
        self.result = 0

    def to_state_1(self, char):
        if char == "-":
            self.__sign = -1

        self.__current_state = self.STATE["q1"]

    def to_state_2(self, char):
        self.__current_state = self.STATE["q2"]
        self.__add_digit(char)

    def to_state_final(self, char):
        self.__current_state = self.STATE["qf"]

    def __add_digit(self, char):
        # 214748364  7
        # RESULT == 214748364 + char
        if (self.result > self.MAX_INT // 10) or (
            self.result == self.MAX_INT // 10 and int(char) > self.MAX_INT % 10
        ):
            if self.__sign == -1:
                self.result = self.MIN_INT
                self.__sign = 1
            else:
                self.result = self.MAX_INT
            self.__current_state = self.STATE["qf"]
        else:
            self.result = self.result * 10 + int(char)


    def transition(self, char):
        if self.__current_state == self.STATE["q0"]:
            if char == " ":
                return
            elif char == "-" or char == "+":
                self.to_state_1(char)
            elif "0" <= char <= "9":
                self.to_state_2(char)
            else:
                self.to_state_final(char)
        elif self.__current_state == self.STATE["q1"] or self.__current_state == self.STATE["q2"]:
            if "0" <= char <= "9":
                self.to_state_2(char)
            else:
                self.to_state_final(char)

    def get_state(self):
        return self.__current_state

    def get_result(self):
        return self.result * self.__sign


class Solution:
    def myAtoi(self, s):
        q = StateMachine()

        for c in s:
            q.transition(c)
            if q.get_state() == q.STATE["qf"]:
                break

        return q.get_result()