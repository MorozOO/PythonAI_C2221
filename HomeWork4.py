class phone():
    def call(self,phone):
        print(f"call {phone}")

class mobile(phone):
    def func1(self):
        pass

class smartPhone(mobile):
    def func2(self):
        pass
contacts = '+380931234567'
sm = smartPhone()
sm.call(contacts)

