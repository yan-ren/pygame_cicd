import cx_Freeze

executables = [cx_Freeze.Executable("./racing_car/racing.py")]

cx_Freeze.setup(
    name="Racing Car",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["./racing_car/img/"]}},
    executables = executables

    )