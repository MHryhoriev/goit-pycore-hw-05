import re
import sys

def parse_log_line(line: str) -> dict:
    """
    Parses a log line into a dictionary containing date, time, level, and message.
    
    Args:
        line (str): A single line from the log file.
        
    Returns:
        dict: A dictionary with keys 'date', 'time', 'level', and 'message'.
    """
    pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)'
    match = re.match(pattern, line)
    
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4)
        }
    else:
        raise ValueError(f"Log line does not match expected format: {line}")


def read_lines(file_path: str):
    """
    Generator that yields lines from a file, stripped of leading and trailing whitespace.
    
    Args:
        file_path (str): Path to the file.
        
    Yields:
        str: A stripped line from the file.
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip()


def load_logs(file_path: str) -> list:
    """
    Loads logs from a file and parses each line.
    
    Args:
        file_path (str): Path to the log file.
        
    Returns:
        list: A list of dictionaries representing each log entry.
    """
    logs = []
    try:
        for line in read_lines(file_path):
            logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except IOError:
        print(f"Error: Unable to read file - {file_path}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    return logs