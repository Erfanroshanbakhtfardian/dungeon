import logging

logger = logging.getLogger()

logging.basicConfig(
    filename = "dungeon_and_dragon.log",
    level = logging.DEBUG,
    format = " %(process)d  - %(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    filemode = "a" 
)


# import toml
# import logging.config
# import sys

# # Load the logging configuration from the file
# with open('logging.toml', 'r') as f:
#     config = toml.load(f)

# # Configure the logging system
# logging.config.dictConfig(config)

# # Use the logging system to write log messages
# logger = logging.getLogger(__name__)
# logger.info('This is an info log message.')


# [log]
# version = 1
# disable_existing_loggers = false

# [handlers.console]
# handler_class = "logging.StreamHandler"
# level = "DEBUG"
# formatter = "sampleFormatter"
# stream = "ext://sys.stdout"

# [formatters.sampleFormatter]
# format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# [loggers]
# keys = ["root", "sampleLogger"]

# [loggers.root]
# level = "DEBUG"
# handlers = ["console"]

# [loggers.sampleLogger]
# level = "DEBUG"
# handlers = ["console"]
# qualname = "sampleLogger"
# propagate = 0