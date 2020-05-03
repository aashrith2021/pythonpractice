def logger(func):
    def wrapper():
        print('loggging execution')
        func()
        print('done')
    return wrapper
@logger
def sample():
    print('sample func')

sample()