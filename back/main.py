from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    grade: str
    interests: list[str]
    level: str
    work_style: str

@app.post("/api/v1/roadmap/recommend")
def get_recommendation(user_input: UserInput):
    scores = {
        "데이터 기반 인사이트 도출형": 0,
        "글로벌 AIoT 융합형": 0,
        "사용자 경험 설계형": 0,
        "풀스택 서비스 개발형": 0
    }
    
    if "데이터사이언스" in user_input.interests or "AI" in user_input.interests:
        scores["데이터 기반 인사이트 도출형"] += 2
    if "IoT" in user_input.interests or "AI" in user_input.interests:
        scores["글로벌 AIoT 융합형"] += 2
    if "UX/UI" in user_input.interests:
        scores["사용자 경험 설계형"] += 3
    if "웹개발" in user_input.interests or "앱개발" in user_input.interests:
        scores["풀스택 서비스 개발형"] += 2
        
    if user_input.work_style == "기획 중심":
        scores["사용자 경험 설계형"] += 2
    elif user_input.work_style == "분석 중심":
        scores["데이터 기반 인사이트 도출형"] += 2
    elif user_input.work_style == "개발 중심":
        scores["풀스택 서비스 개발형"] += 2
        scores["글로벌 AIoT 융합형"] += 1

    best_persona = max(scores, key=scores.get)
    
    result = {}
    if best_persona == "데이터 기반 인사이트 도출형":
        result = {
            "persona_type": "📊 데이터 기반 인사이트 도출형",
            "description": "복잡한 데이터 속에서 가치를 찾아내는 분석가 성향입니다.",
            "recommended_courses": ["데이터 마이닝", "빅데이터 처리 및 응용", "데이터 시각화"],
            "project_idea": "공공 데이터를 활용한 상권 분석 및 매출 예측 대시보드 구축",
            "roadmap": {"1~2학년": "통계학, 파이썬 기반 데이터 분석 기초", "3학년": "머신러닝 알고리즘 적용", "4학년": "실제 기업 데이터 기반 산학협력 프로젝트"}
        }
    elif best_persona == "글로벌 AIoT 융합형":
        result = {
            "persona_type": "🤖 글로벌 AIoT 융합형",
            "description": "하드웨어와 AI를 결합하여 새로운 가치를 창출하는 엔지니어 성향입니다.",
            "recommended_courses": ["IoT 프로그래밍", "인터랙티브 AI", "IoT 시스템설계"],
            "project_idea": "라즈베리파이와 센서를 활용한 스마트홈 제어 시스템",
            "roadmap": {"1~2학년": "C프로그래밍, 자료구조, 임베디드 기초", "3학년": "센서 데이터 수집 및 엣지 AI 적용", "4학년": "AIoT 융합 디바이스 시제품 제작"}
        }
    elif best_persona == "사용자 경험 설계형":
        result = {
            "persona_type": "🎨 사용자 경험 설계형",
            "description": "사용자의 불편함을 해소하고 직관적인 서비스를 기획하는 디자이너/기획자 성향입니다.",
            "recommended_courses": ["UI/UX디자인", "HCI와UX평가", "컴퓨터그래픽스"],
            "project_idea": "교내 식당 혼잡도 파악 및 메뉴 예약 모바일 앱 UI/UX 기획",
            "roadmap": {"1~2학년": "그래픽디자인 기초, 심리학 개론", "3학년": "Figma를 활용한 프로토타이핑", "4학년": "실제 사용자 대상 Usability Test(UT) 및 포트폴리오 완성"}
        }
    else:
        result = {
            "persona_type": "💻 풀스택 서비스 개발형",
            "description": "아이디어를 실제 동작하는 웹/앱 서비스로 구현해내는 개발자 성향입니다.",
            "recommended_courses": ["웹프로그래밍", "모바일 프로그래밍", "데이터베이스"],
            "project_idea": "학생 포트폴리오 공유 및 스터디 매칭 웹 서비스 구현",
            "roadmap": {"1~2학년": "객체지향프로그래밍, 알고리즘 기초", "3학년": "프레임워크(React, Spring/Django) 습득", "4학년": "클라우드(AWS) 배포 및 무중단 서비스 운영 경험"}
        }

    return result