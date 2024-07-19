import sys

def check_arguments() -> tuple:
    """
    Checks if the appropriate number of command-line arguments is provided.
    
    Returns:
        tuple: The file path and optionally the log level if provided.
        
    Raises:
        SystemExit: If the number of arguments is less than 2.
    """
    if len(sys.argv) < 2:
        print("Usage: python script.py <log_file_path> [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    return file_path, log_level
