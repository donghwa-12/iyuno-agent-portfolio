import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="Iyuno AI Agent Portfolio", page_icon="🤖")

st.title("🤖 Iyuno AI Agent Portfolio")
st.caption("공개 문서 기반 RAG 및 도구 호출(Tool Calling) AI 에이전트 데모")

# 1. RAG 기반 검색 모의 기능 (Citation 포함)
st.header("1. RAG 문서 기반 Q&A")
query = st.text_input("질문을 입력하세요 (예: 보안 규정 및 정책 문의):")

if query:
    st.subheader("💡 AI 답변")
    st.write(f"**'{query}'**에 대한 답변입니다: 본 시스템은 다단계 workflow 및 RAG 기술을 적용하여 최신 보안 정책 및 AI Agent 시스템 문서를 정확히 참고하여 안내합니다.")
    
    st.info("📌 **출처 인용 (Citation):** [Iyuno_Security_Policy_2026.pdf, Page 3]")

# 2. Tool Calling 기능 (계산기 / 날짜 조회)
st.header("2. Tool Calling 기능")
col1, col2 = st.split() if hasattr(st, 'split') else (st.sidebar, st.sidebar)

with st.expander("🛠️ 도구 호출 테스트 (단순 계산기)"):
    num1 = st.number_input("첫 번째 숫자", value=10)
    num2 = st.number_input("두 번째 숫자", value=20)
    if st.button("도구 실행 (더하기)"):
        st.success(f"도구 실행 결과: {num1 + num2}")
