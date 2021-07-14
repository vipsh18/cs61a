class Kangaroo:
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, new_content):
        if new_content in self.pouch_contents:
            print("Object already in pouch")
            return
        self.pouch_contents.append(new_content)

    def __str__(self):
        if self.pouch_contents:
            return f"The kangaroo's pouch contains: {self.pouch_contents}"
        else:
            return "The kangaroo's pouch is empty"


K = Kangaroo()
print(K)

K.put_in_pouch("ball")
print(K)

K.put_in_pouch("hammer")
print(K)

K.put_in_pouch("ball")
print(K)