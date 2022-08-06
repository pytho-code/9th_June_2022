class idea:
    def A (self):
        print("idea")

class vodafone:
     def b(self):
        print("vodafone")

class vi(idea,vodafone):
     def __init__(self):
        print("multiple inheritance")

vi=vi()
vi.A()
vi.b()

    