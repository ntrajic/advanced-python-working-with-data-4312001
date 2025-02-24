# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from


# set the output file and debug level, and
# TODO: use a custom formatting specification
# logging.basicConfig(filename="output.log",
#                     level=logging.DEBUG)

# logging.info("This is an info-level log message")
# logging.warning("This is a warning-level message")


# Demonstrate how to customize logging output

import logging

extData = {'user': 'joem@example.com'}


def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)


# set the output file and debug level, and
# use a custom formatting specification
fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
dateStr = "%m/%d/%Y %I:%M:%S %p"
logging.basicConfig(filename="output.log",
                    level=logging.DEBUG,
                    format=fmtStr,
                    datefmt=dateStr)

logging.info("This is an info-level log message", extra=extData)
logging.warning("This is a warning-level message", extra=extData)
anotherFunction()

# OUT: 
# DEBUG:root:This is a debug-level log message
# INFO:root:This is an info-level log message
# WARNING:root:This is a warning-level message
# ERROR:root:This is an error-level message
# CRITICAL:root:This is a critical-level message
# INFO:root:Here's a string variable and an int: 10
## 02/24/2025 06:41:10 AM: INFO: <module> Line:37 User:joem@example.com This is an info-level log message
## 02/24/2025 06:41:10 AM: WARNING: <module> Line:38 User:joem@example.com This is a warning-level message
## 02/24/2025 06:41:10 AM: DEBUG: anotherFunction Line:25 User:joem@example.com This is a debug-level log message


