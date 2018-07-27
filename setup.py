from cx_Freeze import setup, Executable

base = None

executables = [Executable("mainGUI.pyw", base=base)]

packages = ["requests", "bs4", "os", "json", "io", "subprocess", "selenium"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "xDownload",
    version = "1.0",
    options = options,
    description = 'Just a bot downloader.',
    executables = executables
)