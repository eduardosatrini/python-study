class Archive():
    def __init__(self, name, extension, encrypted = False):
        self.name = name
        self.extension = extension
        self.encrypted = encrypted

    def open_archive():
        pass

    def close_archive():
        pass

arc = Archive("notes", "text")
print(arc.name, arc.extension)
