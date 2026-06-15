import tkinter as tk
from tkinter import messagebox


class LoginWindows(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("로그인")
        self.geometry("300x200")
        self.resizable(False, False) # 크기 변경 안함

        self.create_widgets()

    def create_widgets(self):

        # 헤더 프레임
        self.header_frame = tk.Frame(self, bg = "#f0f0f0")
        self.header_frame.pack(pady = (0, 10))

        tk.Label(self.header_frame, text = "로그인", font = ("Arial", 14, "bold")).pack(pady = 10)

        # 바디 프레임
        self. body_frame = tk.Frame(self, bg = "#f0f0f0")
        self.body_frame.pack(pady = (0, 10))

        tk.Label(self.body_frame, text="아이디 : ").grid(row = 1, column = 0, sticky = "e", pady = 5)
        self.id_entry = tk.Entry(self.body_frame, width = 20)
        self.id_entry.grid(row = 1, column = 1, pady = 5, padx = 5)

        tk.Label(self.body_frame, text="비밀번호 : ").grid(row = 2, column = 0, sticky = "e", pady = 5)
        self.pw_entry = tk.Entry(self.body_frame, width = 20)
        self.pw_entry.grid(row = 2, column = 1, pady = 5, padx = 5)

        # 버튼 프레임
        self.footer_frame = tk.Frame(self, bg="#f0f0f0")
        self.footer_frame.pack(pady=(0, 10))

        self.login_btn = tk.Button(self.footer_frame, text = "로그인", width = 8, command = self.on_login_click)
        self.login_btn.grid(row = 3, column = 1, pady = (20, 0))

        self.cancel_btn = tk.Button(self.footer_frame, text = "취소", width = 8, command = self.on_cancel_click)
        self.cancel_btn.grid(row = 3, column = 2, pady = (20, 0))

    def on_login_click(self):
        # 아이디와 유저정보 아이디와 비교
        # 비밀번호 같은지 확인
        # 같을 경우 로그인창 종료
        # 대쉬보드 열기
        if self.id_entry.get() =="":
            messagebox.showerror("오류", "아이디를 입력하세요.")


        else:
            if self.id_entry ==

        # 아닐경우 틀림 메세지 출력
        # if self.id_entry == member.id and self.pw_entry == member.pw:
        #     print("로그인")
        #
        # else:
        #     print("틀림")

    def on_cancel_click(self):
        self.destroy()

