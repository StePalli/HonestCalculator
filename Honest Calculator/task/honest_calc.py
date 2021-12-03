# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation.\
 You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
memory_savers = {"msg_10": "Are you sure? It is only one digit! (y / n)",
                 "msg_11": "Don't be silly! It's just one number! Add to the memory? (y / n)",
                 "msg_12": "Last chance! Do you really want to embarrass yourself? (y / n)"}

operations = ["+", "-", "*", "/"]
memory = 0


def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in operations:
        print(msg_2)
        continue
    check(x, y, oper)
    if oper == "+":
        result = x + y
        print(result)
        while True:
                has_memory = input(msg_4)
                if has_memory == "y":
                    if is_one_digit(result):
                        index_msg = 10
                        while True:
                            answer = input(memory_savers[f"msg_{index_msg}"])
                            if answer == "y":
                                if index_msg < 12:
                                    index_msg += 1
                                else:
                                    memory = result
                                    break
                            elif answer == "n":
                                break
                        break
                    else:
                        memory = result
                        break
                elif has_memory == "n":
                    break
        while True:
            continue_calc = input(msg_5)
            if continue_calc in ["y", "n"]:
                break
        if continue_calc == "y":
            continue
        else:
            break
    if oper == "-":
        result = x - y
        print(result)
        while True:
            has_memory = input(msg_4)
            if has_memory == "y":
                if is_one_digit(result):
                    index_msg = 10
                    while True:
                        answer = input(memory_savers[f"msg_{index_msg}"])
                        if answer == "y":
                            if index_msg < 12:
                                index_msg += 1
                            else:
                                memory = result
                                break
                        elif answer == "n":
                            break
                    break
                else:
                    memory = result
                    break
            elif has_memory == "n":
                break
        while True:
            continue_calc = input(msg_5)
            if continue_calc in ["y", "n"]:
                break
        if continue_calc == "y":
            continue
        else:
            break
    if oper == "*":
        result = x * y
        print(result)
        while True:
            has_memory = input(msg_4)
            if has_memory == "y":
                if is_one_digit(result):
                    index_msg = 10
                    while True:
                        answer = input(memory_savers[f"msg_{index_msg}"])
                        if answer == "y":
                            if index_msg < 12:
                                index_msg += 1
                            else:
                                memory = result
                                break
                        elif answer == "n":
                            break
                    break
                else:
                    memory = result
                    break
            elif has_memory == "n":
                break
        while True:
            continue_calc = input(msg_5)
            if continue_calc in ["y", "n"]:
                break
        if continue_calc == "y":
            continue
        else:
            break
    if oper == "/" and y != 0:
        result = x / y
        print(result)
        while True:
            has_memory = input(msg_4)
            if has_memory == "y":
                if is_one_digit(result):
                    index_msg = 10
                    while True:
                        answer = input(memory_savers[f"msg_{index_msg}"])
                        if answer == "y":
                            if index_msg < 12:
                                index_msg += 1
                            else:
                                memory = result
                                break
                        elif answer == "n":
                            break
                    break
                else:
                    memory = result
                    break
            elif has_memory == "n":
                break
        while True:
            continue_calc = input(msg_5)
            if continue_calc in ["y", "n"]:
                break
        if continue_calc == "y":
            continue
        else:
            break
    if oper == "/" and y == 0:
        print(msg_3)
        continue
    break
