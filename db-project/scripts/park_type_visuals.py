import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import os

# 한글 폰트 설정 (Mac/Windows 자동 대응)
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
gu_col = "소재지(구)"
type_col = "공원유형"
area_col = "면적(㎡)"

# output 디렉토리 생성
output_dir = "output/type"
os.makedirs(output_dir, exist_ok=True)

# 1. 공원유형별 개수 (파이차트)
count_by_type = df[type_col].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(count_by_type, labels=count_by_type.index, autopct='%1.1f%%', startangle=140)
plt.title("공원유형별 공원 개수 비율")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "공원유형별_개수_파이차트.png"))
plt.close()

# 1-2. 공원유형별 개수 (막대그래프)
plt.figure(figsize=(10, 6))
plt.bar(count_by_type.index, count_by_type.values, color='skyblue')
plt.title("공원유형별 공원 개수")
plt.xlabel("공원유형")
plt.ylabel("공원 수")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "공원유형별_개수_막대그래프.png"))
plt.close()

# 2. 공원유형별 평균 면적 (막대그래프)
avg_area_by_type = df.groupby(type_col)[area_col].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(avg_area_by_type.index, avg_area_by_type.values, color='mediumseagreen')
plt.title("공원유형별 평균 면적")
plt.xlabel("공원유형")
plt.ylabel("평균 면적 (㎡)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "공원유형별_평균면적_막대그래프.png"))
plt.close()

# 3. 공원유형 + 구별 분포 (Heatmap)
pivot_table = df.pivot_table(index=gu_col, columns=type_col, values=area_col, aggfunc="count", fill_value=0)
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
plt.title("구별 공원유형 분포 Heatmap")
plt.xlabel("공원유형")
plt.ylabel("소재지(구)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "구별_공원유형_분포_히트맵.png"))
plt.close()