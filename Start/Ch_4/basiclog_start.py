# demonstrate the logging api in Python

# TODO: use the built-in logging module


# TODO: Use basicConfig to configure logging

# TODO: Try out each of the log levels

# TODO: Output formatted strings to the log

# use the built-in logging module
import logging

# Use basicConfig to configure logging
# this is only executed once, subsequent calls to
# basicConfig will have no effect
logging.basicConfig(level=logging.DEBUG,
                    filemode="w",
                    filename="output.log")

# Try out each of the log levels
logging.debug("This is a debug-level log message")
logging.info("This is an info-level log message")
logging.warning("This is a warning-level message")
logging.error("This is an error-level message")
logging.critical("This is a critical-level message")

# Output formatted string to the log
logging.info("Here's a {} variable and an int: {}".format("string", 10))

# OUT: output.log file has contents:
# DEBUG:root:This is a debug-level log message
# INFO:root:This is an info-level log message
# WARNING:root:This is a warning-level message
# ERROR:root:This is an error-level message
# CRITICAL:root:This is a critical-level message
# INFO:root:Here's a string variable and an int: 10