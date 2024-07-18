# Log Parsing Project

This project focuses on parsing and processing log data in real-time using Python. The script reads data from standard input (stdin), processes each line according to a specific format, and computes metrics based on the input data. Here’s a breakdown of the project:

## Requirements

- **Language**: Python 3.4.3
- **Operating System**: Ubuntu 20.04 LTS
- **Editor**: vi, vim, emacs
- **Style Guide**: PEP 8 (version 1.7.x)

## Project Overview

## Tasks

1. **Log parsing**: Implement a script (`0-stats.py`) that reads log entries line by line. Each line follows the format `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`. The script computes the following metrics:
   - Total file size accumulated.
   - Number of occurrences for each HTTP status code (200, 301, 400, 401, 403, 404, 405, 500).
   - After every 10 lines or upon keyboard interruption (CTRL + C), print the accumulated metrics.

## Execution

To run the project, you can generate random log data using the provided generator script (`0-generator.py`) and pipe its output into `0-stats.py`.

## Example

```bash
$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
...
```

## Author

- [AbdurrahmanIdr](https://github.com/AbdurrahmanIdr)
