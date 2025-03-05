def decode_command(command):
    """
    Декодирует команду.
    :param command (str): Команда для декодирования.
    :return (str): Декодированная команда.
    """
    def process_level(part: str) -> str:
        output = ""
        i = 0
        while i < len(part):
            if part[i].isdigit():
                num_str = ""
                while i < len(part) and part[i].isdigit():
                    num_str += part[i]
                    i += 1
                multiplier = int(num_str)
            else:
                multiplier = 1

            if i < len(part) and part[i] in ('л', 'п', 'в', 'н'):
                output += part[i] * multiplier
                i += 1
            elif i < len(part) and part[i] == '(':
                i += 1
                start = i
                level = 1
                while i < len(part) and level > 0:
                    if part[i] == '(':
                        level += 1
                    elif part[i] == ')':
                        level -= 1
                    i += 1
                inner = part[start:i - 1]
                output += process_level(inner) * multiplier
            else:
                i += 1
        return output

    return process_level(command[1:-1]).upper()

try:
    command = input("write code here ")
    print (decode_comand(command))
except:
    print("invalid data")
    command = input("write code here ")
    print (decode_comand(command))
