class numberBook:
    numList = {"홍길동":"01012345678"}
    
    def __init__(self):
        self.numList = numberBook.numList
    
    def createNum(self, name, num):
        #numList = numberBook.numList
        if name in self.numList:
            print("이미 존재하는 이름")
        else:
            print("추가 완료")
            self.numList[name] = num
    
    def delNum(self, name):
        if name not in self.numList:
            print("존재하지 않는 이름")
        else:            
            del self.numList[name]
            print("삭제 완료")

    def call(self, name):
        if name in self.numList:
            print(name, "연결 완료")
        else:
            print("존재하지 않는 이름")
            
            
            
numberBook().createNum("김춘향", "01011223344")
numberBook().createNum("홍길동", "01055667788")
numberBook().delNum("이순양")
numberBook().delNum("김춘향")
print(numberBook().numList)
numberBook().call("김춘향")
numberBook().call("홍길동")
