from dataclasses import dataclass

'''
모든 User 정보 -> DB에 전성하게 될 것임
User 클래스에서는 어떠한 DTO도 없어야 한다.
'''
@dataclass
class User:
    user_id: str
    user_pw: str
    user_name: str
    user_personal_number: str

    '''
    1. 선택 입력 변수들은 항상 아래에 배치
    dto에 안넣고 여기에 전화번호를 넣는 이유는
    아무것도 안들어왔을 때 최정적으로 이번호를 넣을거다라는 의미
    str 타입 아니면 저 전화번호를 넣어라 라는 의미
    '''
    user_phone_number: str = "031-903-7360"

