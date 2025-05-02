import logging
"""
# Remove any existing logging handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
"""
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical error')

num1 = 20
num2 = 10

def add(x,y):
    return x+y
add_result = add(num1, num2)
logging.warning('add: {} + {} = {}'.format(num1, num2))

"""Will learn later """