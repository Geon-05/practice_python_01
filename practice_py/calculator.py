import tkinter as tk


# 계산기 클래스 정의
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # 입력 및 결과를 표시할 텍스트 변수
        self.expression = ""
        self.input_text = tk.StringVar()

        # 화면(디스플레이) 부분 생성
        self.create_display()

        # 버튼 부분 생성
        self.create_buttons()

    # 디스플레이(화면) 생성
    def create_display(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack()

        input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=("arial", 18, "bold"),
            bd=10,
            insertwidth=4,
            width=14,
            borderwidth=4,
        )
        input_field.grid(row=0, column=0)

    # 버튼들 생성
    def create_buttons(self):
        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        # 버튼 레이아웃
        buttons = [
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            "C",
            "0",
            "=",
            "+",
        ]

        row = 0
        col = 0
        for button in buttons:
            if button == "C":
                btn = tk.Button(
                    btns_frame,
                    text=button,
                    width=9,
                    height=3,
                    bd=1,
                    font=("arial", 18, "bold"),
                    command=self.clear,
                )
            elif button == "=":
                btn = tk.Button(
                    btns_frame,
                    text=button,
                    width=9,
                    height=3,
                    bd=1,
                    font=("arial", 18, "bold"),
                    command=self.calculate,
                )
            else:
                btn = tk.Button(
                    btns_frame,
                    text=button,
                    width=9,
                    height=3,
                    bd=1,
                    font=("arial", 18, "bold"),
                    command=lambda x=button: self.button_click(x),
                )

            btn.grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    # 버튼 클릭 시 표현식 업데이트
    def button_click(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    # 계산 결과 도출
    def calculate(self):
        try:
            result = str(eval(self.expression))  # eval()을 이용해 계산
            self.input_text.set(result)
            self.expression = result  # 계산 후 결과를 저장하여 다음 계산에 사용 가능
        except:
            self.input_text.set("Error")
            self.expression = ""

    # 입력 초기화
    def clear(self):
        self.expression = ""
        self.input_text.set("")


# 메인 루프
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
