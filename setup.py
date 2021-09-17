from cx_Freeze import setup,Executable

#includefiles = ['resources/516494_Zone-X.mp3','resources/asteroid_blue.png','resources/double_ship.png','resources/enginehum3.ogg','resources/explosion_alpha.png', 'resources/laser6.wav','resources/nebula_blue.png','resources/shot2.png','resources/threeTone1.wav','resources/threeTone2.wav']
includefiles = ['OpenSans-Regular.ttf']
build_exe_options = {"packages": ["os"], 'include_files':includefiles}

setup(
    name = 'Tic Tac Toe',
    version = '1.0',
    description = 'undefeatable AI',
    author = 'Marwan Yasser',
    options = {"build_exe": build_exe_options}, 
	executables = [Executable(script="runner.py", base="Win32GUI", targetName="TTT.exe")]
)