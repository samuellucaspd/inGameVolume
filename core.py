from pycaw.pycaw import AudioUtilities



def get_programs():

    sessions = AudioUtilities.GetAllSessions()
    programs = []

    for session in sessions:
        if session.Process:
            program_name = session.Process.name()
            if program_name not in programs:
                programs.append(program_name)

    return programs

