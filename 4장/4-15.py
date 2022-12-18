import datetime


def time(name):
    global Date, record
    now = datetime.datetime.now()
    ymt = "\n%Y년 %m월 %d일"
    hms = "%H시 %M분 %S초"
    Date = now.strftime(ymt)
    record = now.strftime(hms)
    print(Date, "| ", end='')


company = {}

print("출퇴근 프로그램")
while True:
    name = input("\n\n이름 입력 >> ")
    time(name)
    if name in company:
        comlist = list(company.get(name))
        com = ''.join(map(str, comlist))
        print(f"{name} | {record} *퇴근\n\n {com}")
        del company[name]
        continue

    company[name] = "출근 -> " + record

    if name == "c":
        del company['c']
        break

    print(f"{name} | {record} *출근\n\n {company}")

morning = list(company.keys())
print("현재 출근 명단 ", morning)
