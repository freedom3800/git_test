# version 1

# 데이터프레임을 이름을 입력하고 시작칼럼 종료 칼럼을 입력하면
# float형태로 바꾸어준다.
import pandas as pd

class change():
    def __init__(self, File_name, No_start, No_end):
        self.File_name = File_name
        self.No_start = No_start
        self.No_end = No_end

    def File_on(self):
        # 파일 경로 지정 할 것.
        File_name = self.File_name
        no_start = self.No_start
        no_end = self.No_end

        # 저장한 데이터 프레임의 칼럼만 뽑아 새 데이터 프레임 제작.
        cols = File_name.columns
        file_change_data = pd.DataFrame(columns=cols)

        for texts in range(no_start, no_end):
            names = File_name.columns[texts]
            File_name[names] = File_name[names].str.replace(',', '')
            File_name[names] = File_name[names].astype(float)

