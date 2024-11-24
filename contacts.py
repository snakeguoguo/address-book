class Contact:
    def __init__(self, name, phone=None, id=None, email=None, address=None, notes=None):
        self.name = name
        self.phone = phone
        self.id = id  # 学号
        self.email = email
        self.address = address
        self.notes = notes  # 备注
        self.is_bookmarked = False

    def toggle_bookmark(self):
        self.is_bookmarked = not self.is_bookmarked
