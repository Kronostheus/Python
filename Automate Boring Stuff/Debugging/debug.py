import traceback
import logging

# Setting logging format. This is an example of a log from our count() function:
#   2018-03-03 17:09:20,706 - DEBUG - Current: 0
# To write to a file, add this to beginning: filename='log.txt'
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def exception():
    # We can output our own message to help understand what happened
    raise Exception("Error Ocurred")

def call():
    exception()

# call()    Uncomment to watch how the program tracesback the origin of the Exception

# This will write the Exception error into a file instead of simply printing to the console
def tracebackTest():
    try:
        exception()
    except:
        # create or overwrite file
        errorFile = open('errorInfo.txt', 'w')
        # we can use traceback module (don't forget to import)
        errorFile.write(traceback.format_exc())
        errorFile.close()

# tracebackTest()   Uncomment to see exception logging to a file

def assertTest():
    doorStatus = 'open'
    # Syntax: assert (condition), (error message)
    assert doorStatus == 'open', 'Door needs to be open'

    # this will raise an AssertionError because we want the door to be open, however, it is not
    doorStatus = 'closed'
    assert doorStatus == 'open', 'Door needs to be open'

# assertTest()  test-driven programming at it's finest

# Assertions can be disabled by passing -o flag when running Python. It's useful when you have a
#   finished product and do not want it to be slowed by error checking, since it should be bug-free

def count(n):
    # Logging is better than printing since you can simple disable the logs rather than deleting several
    #   print statements, one or more of which by mistake
    logging.debug('Start of count(%s)' % (n))
    for i in range(n):
        logging.debug("Current: " + str(i))
    logging.debug("End of count(%s)" % (n))

# count(10) logging numbers in a cycle

# Logs can be disable with the line logging.disable(logging.CRITICAL). This will disable any message of this priority or lower

# Levels of Logging:
#
#   DEBUG - lowest level, useful for diagnosing problems
#   INFO - general information, usually used to confirm if program is running exactly as intended
#   WARNING - indicates potential problem that, although doesn't prevent program from working, might in the future
#   ERROR - records an error that caused the program to fail to do something
#   CRITICAL - highest level, used for fatal errors that caused or will cause the program to stop

# One can change the priority of log messages shown by passing the intended priority during the basicConfig()
