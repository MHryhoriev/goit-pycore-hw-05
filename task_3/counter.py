def count_logs_by_level(logs: list[dict]) -> dict:
    """
    Counts the number of log entries for each log level.
    
    Args:
        logs (list[dict]): The list of log entries.
        
    Returns:
        dict: A dictionary with log levels as keys and counts as values.
    """
    levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING']
    count = {level: 0 for level in levels}
    
    for log in logs:
        level = log['level'].upper()
        if level in count:
            count[level] += 1
    
    return count


def display_log_counts(counts: dict) -> None:
    """
    Displays the log counts in a formatted table.
    
    Args:
        counts (dict): A dictionary with log levels and their counts.
    """
    print("Log Level       | Count")
    print("----------------|------")
    for level, count in counts.items():
        print(f"{level:<15} | {count:>1}")
