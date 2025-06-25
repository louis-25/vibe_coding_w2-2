# 🤖 AI 챗봇 프로젝트 (vibe_coding_w2-2)

> FastAPI 백엔드와 Streamlit 프론트엔드를 사용한 LangGraph 기반 상품 검색 챗봇

## 📋 프로젝트 개요

이 프로젝트는 AI 기반 상품 검색 챗봇으로, 사용자의 질문에 따라 웹에서 상품 정보를 검색하고 추천해주는 서비스입니다.

### 🏗️ 아키텍처

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │     FastAPI     │    │   LangGraph     │
│   Frontend      │◄──►│    Backend      │◄──►│   AI Agent      │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 주요 기능

- ✅ **실시간 채팅**: Streamlit 기반 대화형 인터페이스
- ✅ **AI 상품 검색**: LangGraph Agent를 통한 지능형 상품 검색
- ✅ **자동화된 CI/CD**: GitHub Actions를 통한 자동 테스트 및 배포
- ✅ **코드 품질 관리**: 자동 코드 리뷰 및 라벨링
- ✅ **테스트 커버리지**: 포괄적인 단위 테스트

## 🛠️ 기술 스택

### 백엔드

- **FastAPI**: 고성능 웹 프레임워크
- **LangGraph**: AI Agent 구현
- **Python 3.11**: 프로그래밍 언어

### 프론트엔드

- **Streamlit**: 웹 애플리케이션 프레임워크
- **Requests**: HTTP 클라이언트

### DevOps

- **GitHub Actions**: CI/CD 자동화
- **pytest**: 테스트 프레임워크
- **Docker**: 컨테이너화 (예정)

## 📁 프로젝트 구조

```
vibe_coding_w2-2/
├── backend/                 # FastAPI 백엔드
│   ├── app/
│   │   ├── main.py         # 메인 애플리케이션
│   │   ├── agent.py        # LangGraph Agent
│   │   ├── config.py       # 설정 관리
│   │   ├── models/         # 데이터 모델
│   │   └── routers/        # API 라우터
│   ├── tests/              # 테스트 코드
│   └── requirements.txt    # Python 의존성
├── frontend/               # Streamlit 프론트엔드
│   ├── app.py             # 메인 애플리케이션
│   └── requirements.txt   # Python 의존성
├── .github/               # GitHub 설정
│   ├── workflows/         # GitHub Actions
│   └── ISSUE_TEMPLATE/    # 이슈 템플릿
└── docs/                  # 문서
```

## 🚀 빠른 시작

### 1. 저장소 클론

```bash
git clone https://github.com/louis-25/vibe_coding_w2-2.git
cd vibe_coding_w2-2
```

### 2. 백엔드 실행

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. 프론트엔드 실행

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

### 4. 브라우저에서 접속

- **프론트엔드**: http://localhost:8501
- **백엔드 API**: http://localhost:8000
- **API 문서**: http://localhost:8000/docs

## 🧪 테스트 실행

```bash
cd backend
pytest tests/ -v --cov=app
```

## 🔧 새로운 기능 (PR 테스트용)

이 PR에서 추가된 기능들:

### 백엔드

- ✅ `/test` 엔드포인트 추가
- ✅ 테스트 응답 데이터 포함
- ✅ 새로운 테스트 케이스 추가

### 프론트엔드

- ✅ 백엔드 연결 테스트 버튼
- ✅ 테스트 결과 시각화
- ✅ 에러 처리 개선

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 👥 팀

- **개발자**: louis-25
- **프로젝트**: AI 챗봇 개발

## 📞 문의

프로젝트에 대한 질문이나 제안사항이 있으시면 이슈를 생성해주세요.

---

⭐ 이 프로젝트가 도움이 되셨다면 스타를 눌러주세요!
