enum State { q0, q1, q2, qd };

class StateMachine {
    State currentState;
    int result, sign;

    void toStateQ1(char& ch) {
        sign = (ch == '-') ? -1 : 1;
        currentState = q1;
    }

    void toStateQ2(int digit) {
        currentState = q2;
        appendDigit(digit);
    }

    void toStateQd() {
        currentState = qd;
    }

    void appendDigit(int& digit) {
        if ((result > INT_MAX / 10) ||
            (result == INT_MAX / 10 && digit > INT_MAX % 10)) {
            if (sign == 1) {
                result = INT_MAX;
            } else {
                result = INT_MIN;
                sign = 1;
            }
            toStateQd();
        } else {
            result = result * 10 + digit;
        }
    }

public:
    StateMachine() : currentState(q0), result(0), sign(1) {}

    void transition(char& ch) {
        if (currentState == q0) {
            if (ch == ' ') {
                return;
            } else if (ch == '-' || ch == '+') {
                toStateQ1(ch);
            } else if (isdigit(ch)) {
                toStateQ2(ch - '0');
            } else {
                toStateQd();
            }
        } else if (currentState == q1 || currentState == q2) {
            if (isdigit(ch)) {
                toStateQ2(ch - '0');
            } else {
                toStateQd();
            }
        }
    }

    int getInteger() {
        return sign * result;
    }

    State getState() {
        return currentState;
    }
};

class Solution {
public:
    int myAtoi(string s) {
        StateMachine Q;

        for (int i = 0; i < s.size() && Q.getState() != qd; ++i) {
            Q.transition(s[i]);
        }

        return Q.getInteger();
    }
};
