def error(msg: str, *args, **kwargs):
    string = "[ERROR] " + msg
    for i in args:
        string += i + " "
    for key in kwargs.keys():
        string += f" [{key}]: {kwargs[key]}"
    print(string)


def info(msg: str, *args, **kwargs):
    string = "[I] " + msg
    for i in args:
        string += i + " "
    for key in kwargs.keys():
        string += f" [{key}]: {kwargs[key]}"
    print(string)


def Warning(msg: str, *args, **kwargs):
    string = "[warn] " + msg
    for i in args:
        string += i + " "
    for key in kwargs.keys():
        string += f" [{key}]: {kwargs[key]}"
    print(string)