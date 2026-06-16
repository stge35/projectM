from back_end.domain.user.controller.user_controller import UserController
from back_end.domain.user.repository.file_user_repository import FileUserRepository
from back_end.domain.user.service.user_service import UserService

if __name__ == "__main__":
    # 💡 정석: 레포지토리의 인스턴스를 '진짜'로 만들 때 원하는 파일 경로를 찔러넣어 줍니다.
    custom_file_path = "../../../custom_database.json"

    real_repository = FileUserRepository(file_path=custom_file_path)

    # 서비스와 컨트롤러는 이 경로가 뭔지 전혀 모른 채,
    # 조립된 real_repository 인스턴스를 받아서 쓰기만 합니다.
    real_service = UserService(user_repository=real_repository)
    controller = UserController(user_service=real_service)