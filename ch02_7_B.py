def card_conv(num : int , r : int) -> str :
    '''정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환'''
    
    d = ""
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    
    while num > 0 : # 0이 되서 더 이상 r로 나눌 수 없어지면 반복문을 빠져나온다.
        d += dchar[num % r] # 나머지에 해당하는 순서의 문자를 꺼내서 d 변수에 추가
        print(d)
        num //= r # x를 r로 나누어 업데이트
        pass # while 
    
    
    return d[::-1] # 역순으로 변환


if __name__ == "__main__" :
    print('10진수를 n진수로 변환합니다.')
    
    while True : 
        while True : 
            no = int(input("변환할 값으로 음이 아닌 정수를 입력하세요."))
            
            if no > 0 :
                break
                pass # if
            
            pass # while_1
        
        while True : 
            cd = int(input('몇 진수로 변환할까요? : '))
            
            if 2<= cd <= 36 : 
                break
            
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')
        
        retry = input ("한 번 더 변환할까요?(Y : 예 / N : 아니오) : ")
        
        if retry in {'N', 'n'} : 
            break
        else : 
            pass # if-else