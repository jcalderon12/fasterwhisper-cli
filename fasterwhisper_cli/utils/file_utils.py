def is_media_file(file_path: str) -> bool:
    """
    Check if the given file path is a video or audio file based on its extension.

    Args:
        file_path (string): the path of the audio/video file.

    Returns:
        bool: return true if is a valid video/audio file otherwise return false.
    """
    media_extensions = [
        # Video extensions
        ".mp4",
        ".avi",
        ".mov",
        ".mkv",
        ".flv",
        ".wmv",
        ".webm",
        # Audio extensions
        ".mp3",
        ".wav",
        ".ogg",
        ".aac",
        ".flac",
        ".m4a",
        ".wma",
    ]
    
    index = file_path.rfind('.')

    # This happen if the file dont have a point in his name
    if index == -1:
        raise TypeError

    extension = file_path[index:].lower()

    if extension in media_extensions:
        return True
    else:
        raise ValueError
