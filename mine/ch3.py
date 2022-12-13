import queue


def Round_Robin(self):
    time_quantum = 3  # 시간 할당량
    
    while self.empty != True:  # 큐가 빌때까지 실행
        processing_q = self.get()  # 큐의 첫번쨰 프로세스 로드
        print(f"{processing_q[0]} is in the Critical Section.")

        # 임계 영역
        for i in range(time_quantum):  # 시간 할당량 만큼 반복
            print(f"{processing_q}working... ")
            processing_q[1] -= 1  # 한 사이클 돌 때 마다 실행시간 1씩 차감
            if processing_q[1] == 0:  # 실행시간이 모두 소모 되었을시 break
                print(f"{processing_q[0]} is done.")
                break

        if processing_q[1] != 0:  # 실행시간이 모두 차감되지 못하였을시 큐의 가장 뒤로 재배치
            print(f"{processing_q[0]} is not done.")
            q.put(processing_q)
    

q = queue.Queue()  # 큐 정의
q.put(['a', 2])  # [프로세스, 실행시간]
q.put(['b', 3])
q.put(['c', 4])
q.put(['d', 5])
q.put(['e', 6])
q.put(['f', 7])

Round_Robin(q)
