from cx_Freeze import setup, Executable

base = None    

executables = [Executable("botPyong.py", base=base)]

packages = ["idna", "os", "json", "time"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "BotPyong",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)