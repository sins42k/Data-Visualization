import csv
import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.font_manager as fm
import os

# =============================
# [1] macOS 한글 폰트 설정 (AppleGothic)
# =============================
font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
fontprop = fm.FontProperties(fname=font_path)
plt.rc("font", family=fontprop.get_name())
plt.rcParams["axes.unicode_minus"] = False  # 마이너스 깨짐 방지

# =============================
# [2] 파일 경로 및 초기화
# =============================
DATA_FILE = "db/data.csv"
output_dir = "output/overall"
os.makedirs(output_dir, exist_ok=True)

# 딕셔너리 초기화
park_counts = defaultdict(int)
park_areas = defaultdict(float)
park_list = defaultdict(list)

# =============================
# [3] CSV 파일 읽기
# =============================
with open(DATA_FILE, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        gu = row["소재지(구)"]
        area = float(row["면적(㎡)"])
        park_counts[gu] += 1
        park_areas[gu] += area
        park_list[gu].append(area)

# =============================
# [4] 통계 요약 파일 저장
# =============================
summary_path = os.path.join(output_dir, "park_summary.txt")
with open(summary_path, "w", encoding="utf-8") as f:
    f.write("📊 [구별 공원 통계 요약]\n")
    f.write("=" * 40 + "\n")
    for gu in park_counts:
        count = park_counts[gu]
        total = park_areas[gu]
        avg = total / count
        f.write(f"■ {gu}\n")
        f.write(f"  - 공원 개수: {count}개\n")
        f.write(f"  - 총 면적: {total:,.0f} ㎡\n")
        f.write(f"  - 평균 면적: {avg:,.2f} ㎡\n")
        f.write(f"  - 최대 면적: {max(park_list[gu]):,.0f} ㎡\n")
        f.write(f"  - 최소 면적: {min(park_list[gu]):,.0f} ㎡\n\n")

print(f"✅ 통계 요약 파일 저장 완료 → {summary_path}")

# =============================
# [5] 시각화 - 1. 공원 개수
# =============================
plt.figure(figsize=(8, 5))
plt.bar(park_counts.keys(), park_counts.values(), color='skyblue')
plt.title("구별 공원 개수")
plt.xlabel("구")
plt.ylabel("공원 수")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "1_공원_개수.png"))
plt.show()

# =============================
# [6] 시각화 - 2. 총 면적
# =============================
plt.figure(figsize=(8, 5))
plt.bar(park_areas.keys(), park_areas.values(), color='lightgreen')
plt.title("구별 총 공원 면적")
plt.xlabel("구")
plt.ylabel("총 면적 (㎡)")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "2_총_공원면적.png"))
plt.show()

# =============================
# [7] 시각화 - 3. 평균 면적
# =============================
avg_areas = {gu: park_areas[gu] / park_counts[gu] for gu in park_counts}
plt.figure(figsize=(8, 5))
plt.bar(avg_areas.keys(), avg_areas.values(), color='salmon')
plt.title("구별 평균 공원 면적")
plt.xlabel("구")
plt.ylabel("평균 면적 (㎡)")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "3_평균_공원면적.png"))
plt.show()

# =============================
# [8] 시각화 - 4. 파이차트
# =============================
plt.figure(figsize=(7, 7))
plt.pie(
    park_areas.values(),
    labels=park_areas.keys(),
    autopct='%1.1f%%',
    startangle=140
)
plt.title("전체 공원 면적 중 구별 비율")
plt.axis('equal')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "4_공원면적_비율_파이차트.png"))
plt.show()

# =============================
# [9] 분석 결과 요약 출력
# =============================
max_total = max(park_areas, key=park_areas.get)
min_total = min(park_areas, key=park_areas.get)
max_avg = max(avg_areas, key=avg_areas.get)

print("\n📝 [간단 분석 결과]")
print(f"- 총 면적이 가장 넓은 구: {max_total} ({park_areas[max_total]:,.0f} ㎡)")
print(f"- 총 면적이 가장 좁은 구: {min_total} ({park_areas[min_total]:,.0f} ㎡)")
print(f"- 평균 면적이 가장 큰 구: {max_avg} ({avg_areas[max_avg]:,.2f} ㎡)")
