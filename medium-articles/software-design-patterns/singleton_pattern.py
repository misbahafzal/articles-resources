import logging
import threading

class SingletonLogger:
    _instance = None
    _lock = threading.Lock()  # Ensures thread-safety

    def __new__(cls):
        # Ensure that only one instance of the class is created, even in a multithreaded environment.
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SingletonLogger, cls).__new__(cls)
                # Initialize the logger configuration once
                cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):
        self.logger = logging.getLogger("AppLogger")
        self.logger.setLevel(logging.DEBUG)

        # Create a file handler to log to a file
        file_handler = logging.FileHandler("app.log")
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler for logging to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Create a formatter for log messages
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Attach the formatter to both handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Attach handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log(self, message, level="info"):
        if level == "info":
            self.logger.info(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "debug":
            self.logger.debug(message)
        else:
            self.logger.info(message)

# Example Usage
def log_some_messages():
    logger = SingletonLogger()
    logger.log("This is an info message.") # calling log function from Singleton class
    logger.log("This is a warning message.", level="warning")
    logger.log("This is an error message.", level="error")

# Even if we try to create multiple loggers, they will all point to the same instance.
log1 = SingletonLogger()
log2 = SingletonLogger()

print(log1 is log2)  # True, as both are the same instance

log_some_messages()
