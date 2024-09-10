
# Python Logger

`raksha-logger` is a simple Python logging library that provides color-coded log levels with timestamp and caller file name details for easier debugging and improved readability.

## Features

- **INFO**: Log informational messages.
- **ERROR**: Log error messages.
- **WARNING**: Log warnings.
- **SUCCESS**: Log successful events.
- Automatically includes:
  - Current timestamp.
  - Name of the file from which the logger is called.
  - Color-coded messages for quick identification.

## Installation

To install `raksha-logger`, simply run:

```bash
pip install raksha-logger
```
In MacOS/Linux:
```bash
pip3 install raksha-logger
```

After installing, you can import and use it in your file as
```python
from raksha_logger import logger

def main():
	logger.info("This is an info message")
	logger.error("This is an error message")
	logger.warning("This is a warning message")
	logger.success("This is a success message")

main()
```
The output looks like this:

![Code Output](https://i.imgur.com/ICSOetE.png)




