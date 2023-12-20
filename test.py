

class üleasnne:
    ülesanded = []
    def __init__(self):
        self.__class__.ülesanded.append(self)

üleasnne1 = üleasnne()

print(üleasnne.ülesanded)
