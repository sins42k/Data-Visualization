import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# 📁 경로 설정
DATA_FILE = "db/data.csv"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ✅ 한글 폰트 설정 (Mac/Windows 자동 대응)
font_candidates = ["Malgun Gothic", "AppleGothic", "NanumGothic"]
for font_name in font_candidates:
    if font_name in [f.name for f in fm.fontManager.ttflist]:
        plt.rc("font", family=font_name)
        break
plt.rcParams["axes.unicode_minus"] = False

# ✅ 데이터 로드
df = pd.read_csv(DATA_FILE, encoding="utf-8")
gu_col = "소재지(구)"
name_col = "공원명"
area_col = "면적(㎡)"

# ✅ 구별 시각화 및 저장
grouped = df.groupby(gu_col)

for gu, group in grouped:
    # 그래프 생성
    plt.figure(figsize=(10, 6))
    plt.bar(group[name_col], group[area_col], color='royalblue')
    plt.title(f"{gu} 공원별 면적 비교", fontsize=14)
    plt.xlabel("공원명", fontsize=12)
    plt.ylabel("면적 (㎡)", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # 결과 저장 경로
    gu_dir = os.path.join(OUTPUT_DIR, f"{gu} 데이터")
    os.makedirs(gu_dir, exist_ok=True)
    save_path = os.path.join(gu_dir, f"{gu}_공원별_면적_그래프.png")

    # ✅ 저장 및 표시
    plt.savefig(save_path)
    print(f"✅ 저장 완료: {save_path}")
    plt.close()  # 창 닫기
