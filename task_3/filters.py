def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    """
    Filters logs by the given level.
    
    Args:
        logs (list[dict]): The list of log entries.
        level (str): The log level to filter by.
        
    Returns:
        list[dict]: A list of dictionaries representing filtered log entries.
    """
    return [log for log in logs if log['level'].upper() == level.upper()]
