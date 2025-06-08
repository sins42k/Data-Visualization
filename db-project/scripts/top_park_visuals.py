import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 한글 폰트 설정 (자동 탐지)
font_candidates = ["Malgun Gothic", "AppleGothic", "NanumGothic"]
for font_name in font_candidates:
    if font_name in [f.name for f in fm.fontManager.ttflist]:
        plt.rc("font", family=font_name)
        break
plt.rcParams["axes.unicode_minus"] = False

# 데이터 불러오기
file_path = "db/data.csv"
df = pd.read_csv(file_path, encoding="utf-8")

# 컬럼 정의
name_col = "공원명"
area_col = "면적(㎡)"

# 사용자 입력 받기
try:
    N = int(input("가장 넓은 공원 상위 몇 개를 보고 싶으신가요? 숫자를 입력하세요: "))
except ValueError:
    print("숫자를 정확히 입력해주세요.")
    exit()

# 상위 N개 추출
top_parks = df[[name_col, area_col]].sort_values(by=area_col, ascending=False).head(N)

# 시각화
plt.figure(figsize=(10, 6))
plt.barh(top_parks[name_col], top_parks[area_col], color='darkorange')
plt.title(f"상위 {N}개 가장 넓은 공원")
plt.xlabel("면적 (㎡)")
plt.ylabel("공원명")
plt.gca().invert_yaxis()
plt.tight_layout()

# 저장
output_dir = "output/rankingTop"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, f"상위_{N}개_넓은_공원_그래프.png"))
plt.close()

# 출력
print(f"상위 {N}개 공원:")
print(top_parks)
