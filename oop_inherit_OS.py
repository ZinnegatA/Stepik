CURRENT_OS = 'windows'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        return cls.create_windows_filedialog(*args) if CURRENT_OS == 'windows' else cls.create_linux_filedialog(*args)

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)
