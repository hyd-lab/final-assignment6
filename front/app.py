import streamlit as st
import requests

st.set_page_config(page_title="정보융합학부 진로 로드맵", layout="wide")

st.title("🎓 정보융합학부 진로 로드맵 추천 플랫폼")
st.write("나의 현재 상황과 성향을 입력하면, 맞춤형 전공 트랙과 학년별 학습 로드맵을 설계해 드립니다.")

with st.sidebar:
    st.header("📝 내 정보 입력")
    grade = st.radio("현재 학년", ("1학년", "2학년", "3학년", "4학년"))
    
    interests = st.multiselect(
        "관심 분야 (다중 선택 가능)",
        ["AI", "데이터사이언스", "IoT", "웹개발", "앱개발", "정보보안", "UX/UI"]
    )
    
    level = st.selectbox("프로그래밍 수준", ("초급 (기초 문법 이해)", "중급 (간단한 프로젝트 가능)", "고급 (실무 수준 개발 가능)"))
    
    work_style = st.selectbox("선호하는 업무 스타일", ("기획 중심", "분석 중심", "개발 중심"))
    
    submit_btn = st.button("내 로드맵 분석하기 🚀")

if submit_btn:
    if not interests:
        st.warning("관심 분야를 최소 1개 이상 선택해 주세요!")
    else:
        with st.spinner("빅데이터 분석 중..."):
            api_url = "http://backend:8000/api/v1/roadmap/recommend"
            
            payload = {
                "grade": grade,
                "interests": interests,
                "level": level,
                "work_style": work_style
            }
            
            try:
                response = requests.post(api_url, json=payload)
                result = response.json()
                
                st.success("분석이 완료되었습니다!")
                
                st.subheader(f"💡 당신의 적성 유형: {result['persona_type']}")
                st.info(result['description'])
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("### 📚 추천 핵심 과목")
                    for course in result['recommended_courses']:
                        st.write(f"- {course}")
                with col2:
                    st.markdown("### 🛠 추천 프로젝트 아이디어")
                    st.write(result['project_idea'])
                
                st.divider()
                st.markdown("### 🗺 학년별 성장 로드맵")
                st.write(f"**1~2학년:** {result['roadmap']['1~2학년']}")
                st.write(f"**3학년:** {result['roadmap']['3학년']}")
                st.write(f"**4학년:** {result['roadmap']['4학년']}")
                
            except Exception as e:
                st.error("서버에 연결할 수 없습니다. 백엔드 도커 컨테이너가 실행 중인지 확인하세요.")