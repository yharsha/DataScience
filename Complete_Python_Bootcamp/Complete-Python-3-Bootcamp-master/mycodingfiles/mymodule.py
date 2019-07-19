def my_func():
    print("hey i am in mymodule.py")
    if __name__ == '__main__':
        print('run directky')
    else:
        print('running while imported '+__name__)
