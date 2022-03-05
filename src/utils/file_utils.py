import os
import uuid

import config


class TempFileProxy:
    """Proxy for managing temporary files. Use only with context manager!

    Just pass file extension and get full file path by "file_path" property.
    If you're using context manager, temporary file will be deleted automatically.

    Temporary files will be created in tmp folder in src root.

    Attributes:
        file_extension (str): Extension of temporary file which you'd like to create.
            For example "xlsx" or ".txt".
            It doesn't matter whether your file extension with dot or not.

    """
    def __init__(self, file_extension: str):
        random_file_name = f'{uuid.uuid4()}.{file_extension.strip(".")}'
        self._file_path = config.TMP_FOLDER_PATH / random_file_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Implicitly delete temporary file (in "with" operator)."""
        self.delete()

    def delete(self) -> bool:
        """Explicitly delete temporary file.

        Returns:
            True if file deleted successfully, otherwise False.
        """
        try:
            os.remove(self._file_path)
        except FileNotFoundError:
            return False
        else:
            return True

    @property
    def file_path(self) -> str:
        """str: full path to your temporary file."""
        return self._file_path
