from parsers import load_logs
from filters import filter_logs_by_level
from counter import count_logs_by_level, display_log_counts
from utils import check_arguments

def process_logs(file_path: str) -> list:
    """
    Loads logs from the given file path and processes them.
    
    Args:
        file_path (str): The path to the log file.
        
    Returns:
        list: A list of dictionaries representing each log entry.
    """
    logs = load_logs(file_path)
    return logs


def analyze_logs(logs: list) -> dict:
    """
    Analyzes the logs to count the occurrences of each log level.
    
    Args:
        logs (list): A list of log entries.
        
    Returns:
        dict: A dictionary with log levels as keys and counts as values.
    """
    log_counts = count_logs_by_level(logs)
    return log_counts


def display_filtered_logs(logs: list, log_level: str) -> None:
    """
    Displays logs filtered by the specified log level.
    
    Args:
        logs (list): A list of log entries.
        log_level (str): The log level to filter by.
    """
    filtered_logs = filter_logs_by_level(logs, log_level)
    if filtered_logs:
        print(f"\nDetails for log level '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        print(f"\nNo logs found for level '{log_level}'")


def main() -> None:
    file_path, log_level = check_arguments()

    logs = process_logs(file_path)
    log_counts = analyze_logs(logs)
    
    display_log_counts(log_counts)
    
    if log_level:
        display_filtered_logs(logs, log_level)

if __name__ == "__main__":
    main()
