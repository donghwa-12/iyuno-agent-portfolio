# Iyuno AI Agent Portfolio

본 프로젝트는 **Iyuno AI Agent Engineer** 채용공고 요구사항을 기반으로 구현한 포트폴리오입니다.

## 📌 채용공고 ↔ 구현 기능 매핑
| 채용공고 요구사항 | 구현한 기능 | 파일 위치 |
| :--- | :--- | :--- |
| LLM 기반 AI Agent 설계 | Streamlit 기반 웹 에이전트 인터페이스 | `app.py` |
| RAG 검색 및 출처 인용 | 문서 기반 임베딩 검색 및 Citation 표시 | `app.py` |
| Tool Calling | 연산 및 기능 호출 도구 연동 | `app.py` |
| 정량 평가 | 30개 QA 평가 데이터셋 및 지표 측정 | `evaluation/metrics.json` |
| 데모 제공 | Streamlit UI 데모 제공 | `app.py` |

## 📊 정량 평가 결과 (Evaluation Metrics)
- **Total Questions**: 30
- **Recall@k**: 93.3%
- **Faithfulness (충실도)**: 90.0%
- **Avg Latency**: 1.15s
- **Avg Token Cost**: $0.002

## ⚙️ 실행 방법 (Usage)
```bash
pip install streamlit
streamlit run app.py
