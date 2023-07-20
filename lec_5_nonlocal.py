counter = 0

def creat_scope(default):
    counter = default * 2

    def nonlocal_print():
        nonlocal counter
        print(f'global {counter}')