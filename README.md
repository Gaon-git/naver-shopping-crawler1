# 🛍️ 네이버 쇼핑 크롤러 (다이소 키워드)

이 프로젝트는 **Python + Selenium**을 사용하여  
네이버 쇼핑에서 "다이소" 키워드로 검색된 상품들의  
**실제 상세 페이지 URL**을 자동으로 크롤링하고,  
결과를 엑셀 파일로 저장합니다.

---

## ✅ 사용 방법 (Google Colab 기준)

1. `main.py`의 코드를 Google Colab에 복사해서 실행하세요
2. 크롬 드라이버 설치 셀 먼저 실행
3. 그 다음 크롤링 셀을 실행하면  
   👉 `daiso_real_urls.xlsx` 파일이 생성됩니다

---

## 📦 필요 라이브러리

- `selenium`
- `pandas`
- `openpyxl`

Colab에서는 아래와 같이 설치하세요:

```python
!apt-get update > /dev/null
!apt install -y chromium-browser chromium-chromedriver > /dev/null
!pip install selenium pandas openpyxl --quiet
