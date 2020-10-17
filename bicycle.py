
'''

과제 : 'Bicycle' 클래스 정의

====================================================================


STEP 1: 'Bicycle'은 정확히 어떤 자전거이며, 
        우리가 정의하는 목적은 무엇인지 명확히 하기.
        ==> 구해야 할 속성과 행위를 결정하는 데 혼란이 없을 것이라고 생각

 다양한 아이디어
    "따릉이"(가장 보편적인 자전거)
    전기자전거(부품 추가될 것)
    곡예용 외발자전거(바퀴수 하나, 후진 가능, 메소드: 앞바퀴 들기 가능)
    빈폴 자전거(앞바퀴가 엄청 엄청 큼)
    아동용자전거
    산악용자전거(전문가용, 기어수 및 부품 속성이 다를 것)

    헬스장 자전거(바퀴 없음) ... ?
    모든 종류의 자전거를 아우르는 "자전거"


최종결정 : 경기용 자전거!
    ==> 우리가 생각하는 자전거의 모습 +
        선수에 따라 커스터마이징이 가능하여 개성도 높음


3조 발표 주제 : 경기용 두발자전거 클래스 (커스터마이징 가능)


======================================================================


STEP 2: 경기용 자전거의 속성과 가능한 행위에 대한 브레인스토밍

1. 속성(필드) : 고유한 속성, 현재 상태, 자전거의 부품으로 나누어 생각
 1) 자전거의 고유한 속성: 무게, 길이, 높이, 거리/한페달
 2) 자전거의 현재 상태: 주행상태(주행/정지), 주행가능여부, 현재속도
 3) 자전거의 부품 (경기용 자전거임을 감안, 중요한 부품들을 뽑아냄)
    : 핸들, 바퀴, 안장, 페달, 체인, 기어, 브레이크, 프레임

2. 행위(메소드)
 1) 출발
 2) 회전
 3) 변속
 4) 정지


3. 부품들의 속성과 행위에 대해 브레인스토밍
 1) 핸들: 손잡이 모양, 크기, 최대각도,
          현재각도, 현재방향(왼쪽/오른쪽)
 2) 바퀴: 두께, 활수, 모양, 크기
 3) 페달: 소재
 4) 체인: 길이, 무게
 5) 기어: 소재, 수, 크기, 최대단수
 6) 브레이크: 모양, 위치, 종류
 7) 프레임: 색(선수의 취향), 소재, 모양
 8) 안장: 모양


======================================================================

STEP 3: 코드화

최초 접근 방향: 자전거의 클래스를 부품들의 클래스모다 먼저 정의
 ==> 자전거 클래스 코드 작성시 어떤 부품 클래스의 어떤 필드를 써야 하는지
     눈에 보이지 않으니 쉽지 않음

이미 브레인스토밍을 통해 어떤 부품이 필요하고,
어떤 속성을 정의할 것인지 알고 있기 때문에
부품 클래스를 먼저 정의해놓고, 자전거 클래스를 정의해봄
(실제로 먼저 정의한 부품들의 필드가 자전거 메소드 안에 쓰임)


======================================================================

'''



# 부품 클래스 정의


# 핸들

class Handle :
    
    def __init__(self, gripShape, size, angleMax, angleNow, direction):
    
        # 핸들의 고유 속성 정의
       
        self.gripShape = gripShape         # 핸들의 모양
        self.size = size                   # 핸들의 크기
        self.angleMax = angleMax           # 핸들의 최대각도

        # 핸들의 현재 상태 정의

        self.angleNow = angleNow           # 핸들의 현재각도
        self.direction = direction         # 핸들의 방향(왼쪽/오른쪽)
        pass # constructor
    
    pass # class Handle


# 바퀴

class Wheel :
    
    def __init__(self, thick, spokeNum, shape, size):
        self.thick = thick                 # 바퀴의 두께
        self.spokeNum = spokeNum           # 바퀴살 수
        self.shape = shape                 # 바퀴 모양
        self.size = size                   # 바퀴의 크기
        self.wheelNum = 2                  # 바퀴수: 초기값을 2로 지정              
        pass # constructor
        
    pass # class Wheel


# 페달

class Pedal :
    
    def __init__(self, material):
        self.material = material           # 페달의 소재
        pass # constructor

    pass # class Pedal


# 체인

class Chain :
    
    def __init__(self, length, weight):
        self.length = length               # 체인의 길이
        self.weight = weight               # 체인의 무게
        pass # constructor
    
    pass # class Chain


# 기어

class Gear :
    
    def __init__(self, material, size, number, gearMax):
        self.material = material           # 기어의 소재
        self.size = size                   # 기어의 크기
        self.number = number               # 기어수
        self.gearMax = gearMax             # 최대단수
        self.gearNow = 1                   # 현재 기어상태: 초기값을 1단으로 지정
        pass # constructor
    
    pass # class Gear


# 브레이크 

class Brake :

    def __init__(self, shape, position, type):
        self.shape = shape                 # 브레이크의 모양
        self.position = position           # 브레이크의 위치
        self.type = type                   # 브레이크의 종류        
        pass # constructor
    
    pass # class Brake


# 프레임

class Frame :
    
    def __init__(self, color, material, shape):
        self.color = color                 # 프레임의 색깔
        self.material = material           # 프레임의 소재
        self.shape = shape                 # 프레임의 모양
        pass # constructor
    
    pass # class Frame


# 안장

class Seat :
    
    def __init__(self, shape):
        self.shape = shape                 # 안장의 모양
        pass # constructor
    
    pass # class Seat





# 자전거 클래스 정의

class Bicycle :


    # 자전거의 필드 정의 
            
    def __init__(self, weight, length, height, distance,
                availability, speed, 
                handle, wheel, pedal, chain, gear,
                brake, frame, seat) :
        
        # 자전거의 고유한 속성

        self.weight = weight        # 자전거의 무게
        self.length = length        # 자전거의 전체 길이
        self.height = height        # 자전거의 높이
        self.distance = distance    # 자전거 페달을 한번 밟았을 때 갈 수 있는 거리
    

        # 자전거의 현재 상태

        self.running = False             # 주행상태: 정지(False), 주행(True)
        self.availability = availability # 주행가능상태
        self.speed = speed               # 현재속도
    

        # 자전거의 부품

        self.handle = handle        # 핸들
        self.wheel = wheel          # 바퀴
        self.pedal = pedal          # 페달
        self.chain = chain          # 체인
        self.gear = gear            # 기어
        self.brake = brake          # 브레이크
        self.frame = frame          # 프레임(몸체)
        self.seat = seat            # 시트(안장)
        
        pass # constructor
    
    

    # 메소드 정의
    
    # 출발
    
    def start(self) :
        self.running = True     # 초기값을 False(정지) 설정했던 주행상태를 True(주행)로 변경
        print('출발했습니다.')
        pass # start


    # 회전

    def curb(self, hanDirection, hanAngle) :
        self.handle.angleNow = hanAngle
        self.handle.direction = hanDirection
        # 위에서 먼저 정의한 Handle 클래스의 필드를 사용하고 있음
        
        print("%s 방향으로 %s 만큼 핸들을 꺾었습니다." % (hanDirection, hanAngle))
        
        pass # curb
    

    # 변속

    def gearChange(self, gearNew) :
        self.gear.gearNow = gearNew # 초기값을 1(단)으로 설정했던 기어 클래스의 값을 변경
        print("%s 단으로 바뀌었습니다." % (gearNew))
    
        pass # gear
    

    # 정지

    def stop(self) :
        self.running = False
        print("정지했습니다.")
        pass # stop

    pass # class



# ======================================================================= #

# 클래스로 인스턴스를 생성

gear1 = Gear('티타늄',5, 10, 4)
gear2 = Gear('아이언',1, 3, 1)      # 기어는 두개를 만듦

handle1 = Handle('기본형', '대', 30, 70, '오른쪽')
wheel1 = Wheel('얇음', 20, '동그라미', '대')
pedal1 = Pedal('티타늄')
chain1 = Chain(100, 50)
brake1 = Brake('triangle', 'upper', 'disck')
frame1 = Frame('DarkGreen', '티타늄', 'triangle')
seat1 = Seat('Y형')

# 각종 부품들을 만들어냈습니다!


bicycle1 = Bicycle(100, 50, 50, 3, 1, 0, 
            handle1, wheel1, pedal1, chain1, gear1, brake1, frame1, seat1)

# 자전거 1을 조립했습니다!


bicycle2 = Bicycle(100, 50, 50, 3, 1, 0,
            handle1, wheel1, pedal1, chain1, gear2, brake1, frame1, seat1)

# 자전거 2는 기어2로 변경했습니다!


# ======================================================================= #

# 메소드 출력

# 출발 메소드

bicycle1.start()
print(bicycle1.running) # 자전거의 주행상태가 True로 변경됨(주행중)

# 정지 메소드
bicycle1.stop()
print(bicycle1.running) # 자전거의 주행상태가 False로 변경됨(정지함)

# 변속 메소드
bicycle1.gearChange(3) # 3단으로 변속

# 회전 메소드
bicycle1.curb('오른쪽', '90도')



# ===================================================== #

# 마지막코멘트

# 메소드의 정교화 (아쉬움)
# 집단지성의 힘

