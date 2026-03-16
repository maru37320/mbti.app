import streamlit as st
import urllib.request

# 페이지 설정
st.set_page_config(page_title="롤 챔피언 MBTI", page_icon="⚔️", layout="centered")

# 🌟 핵심 포인트: 라이엇 서버의 차단을 피하는 이미지 다운로드 함수
@st.cache_data(show_spinner=False)
def get_champ_image(champ_id):
    url = f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{champ_id}_0.jpg"
    try:
        # 일반 사용자의 웹 브라우저인 것처럼 위장(User-Agent 헤더 추가)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as response:
            return response.read() # 이미지 데이터를 가져옴
    except Exception:
        return None # 실패할 경우 예외 처리

# MBTI별 찰떡 챔피언 및 궁합 데이터
mbti_data = {
    "ENFJ": {"champ": "브라움", "id": "Braum", "bf": "INFP", "desc": "프렐요드의 든든한 방패 브라움! 모두를 감싸 안는 따뜻한 리더십을 가졌어요. 🛡️"},
    "ENTJ": {"champ": "스웨인", "id": "Swain", "bf": "INTP", "desc": "녹서스의 대장군 스웨인! 압도적인 카리스마와 전략으로 승리를 이끌어냅니다. 🦅"},
    "ENFP": {"champ": "조이", "id": "Zoe", "bf": "INTJ", "desc": "차원을 넘나드는 장난꾸러기 조이! 긍정적인 에너지와 상상력이 톡톡 튀어요. ✨"},
    "ENTP": {"champ": "이즈리얼", "id": "Ezreal", "bf": "INFJ", "desc": "자신감 넘치는 탐험가 이즈리얼! 호기심이 많고 어디로 튈지 모르는 매력의 소유자예요. 🗺️"},
    "ESFJ": {"champ": "럭스", "id": "Lux", "bf": "ISFP", "desc": "데마시아의 빛 럭스! 주변을 환하게 밝히는 긍정적이고 다정한 에너자이저! 💡"},
    "ESTJ": {"champ": "가렌", "id": "Garen", "bf": "ISTP", "desc": "데마시아의 힘 가렌! 흔들림 없는 원칙과 책임감으로 무장한 전사입니다. ⚔️"},
    "ESFP": {"champ": "세라핀", "id": "Seraphine", "bf": "ISFJ", "desc": "무대 위의 별 세라핀! 사람들의 마음을 하나로 연결하는 본투비 아이돌! 🎤"},
    "ESTP": {"champ": "사미라", "id": "Samira", "bf": "ISTJ", "desc": "사막의 장미 사미라! 스릴을 즐기고 두려움 없이 적진으로 뛰어드는 행동파! 🌹"},
    "INFP": {"champ": "아이번", "id": "Ivern", "bf": "ENFJ", "desc": "자연의 아버지 아이번! 숲속 친구들을 사랑하는 평화주의자이자 힐링 마스코트! 🌳"},
    "INTP": {"champ": "하이머딩거", "id": "Heimerdinger", "bf": "ENTJ", "desc": "위대한 발명가 하이머딩거! 엉뚱하지만 천재적인 두뇌로 세상을 깜짝 놀라게 합니다. 🔧"},
    "INTJ": {"champ": "빅토르", "id": "Viktor", "bf": "ENFP", "desc": "진보를 향한 완벽주의자 빅토르! 감정보다는 논리와 효율을 중시하죠. ⚙️"},
    "INFJ": {"champ": "카르마", "id": "Karma", "bf": "ENTP", "desc": "아이오니아의 영적 지도자 카르마! 내면의 평화와 깊은 통찰력으로 사람들을 이끕니다. 🧘‍♀️"},
    "ISFP": {"champ": "진", "id": "Jhin", "bf": "ESFJ", "desc": "잔혹극의 거장 진! 모든 것을 완벽한 예술 작품으로 만들고 싶어 하는 고독한 예술가. 🎭"},
    "ISTP": {"champ": "야스오", "id": "Yasuo", "bf": "ESTJ", "desc": "용서받지 못한 자 야스오! 바람처럼 자유롭고 마이웨이를 걷는 고독한 검객입니다. 🌪️"},
    "ISFJ": {"champ": "타릭", "id": "Taric", "bf": "ESFP", "desc": "발로란의 방패 타릭! 아름다움을 수호하고 아군을 묵묵히 지켜주는 든든한 서포터! 💎"},
    "ISTJ": {"champ": "쉔", "id": "Shen", "bf": "ESTP", "desc": "황혼의 눈 쉔! 언제나 냉철하게 균형을 수호하는 우직한 닌자예요. ⚖️"}
}

# 앱 헤더
st.title("⚔️ 나와 꼭 맞는 롤 챔피언 & 듀오 찾기 🔍")
st.write("간단한 4가지 질문으로 **나의 챔피언 본캐**와 **환상의 듀오**를 찾아보세요! 🎈")
st.markdown("---")

# 질문 목록
st.subheader("🧐 협곡 심리 테스트")

q1 = st.radio("1. 치열한 한타에서 승리했다! 나의 다음 행동은?", 
              ("한타 대승 후! 남은 적을 끝까지 추격해 마무리한다! 🏃‍♂️", "일단 정비가 우선! 안전하게 귀환해서 아이템부터 산다. 🏠"), index=None)

q2 = st.radio("2. 게임 중 팀원들에게 오더를 내릴 때 나는?", 
              ("적 정글 동선, 쿨타임 등 팩트 기반으로 오더를 내린다. 📝", "'느낌 왔어! 지금 들어가면 대박이야!' 직감적으로 플레이한다. ⚡"), index=None)

q3 = st.radio("3. 듀오가 솔킬을 따였을 때 나의 반응은?", 
              ("왜 죽었어? 플래시 안 돌았어? (원인 분석 및 피드백) 📊", "까비 ㅠㅠ 상대가 너무 셌다. 괜찮아 할 수 있어! (위로와 격려) 🥺"), index=None)

q4 = st.radio("4. 랭크 게임을 돌릴 때 나의 플레이 스타일은?", 
              ("밴픽부터 아이템 트리까지 철저하게 계획대로 간다. 🗓️", "상대 픽과 상황을 보고 유동적으로 템트리와 전략을 바꾼다. 🗺️"), index=None)

st.markdown("---")

# 결과 확인 버튼
if st.button("내 챔피언 & 듀오 결과 보기! 🚀"):
    if not all([q1, q2, q3, q4]):
        st.warning("앗! 협곡에 입장하기 전에 4개의 질문에 모두 체크해주세요! 🔴")
    else:
        st.balloons()
        
        # MBTI 계산 로직
        my_mbti = ""
        my_mbti += "E" if "추격" in q1 else "I"
        my_mbti += "S" if "팩트" in q2 else "N"
        my_mbti += "T" if "원인" in q3 else "F"
        my_mbti += "J" if "계획" in q4 else "P"
        
        # 데이터 가져오기
        my_info = mbti_data[my_mbti]
        bf_mbti = my_info["bf"]
        bf_info = mbti_data[bf_mbti]
        
        st.success(f"### 🎉 당신의 MBTI는 **{my_mbti}** 입니다!")
        st.write("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"#### 👤 나의 챔피언: **{my_info['champ']}**")
            # 우회해서 받아온 이미지 출력
            my_img = get_champ_image(my_info["id"])
            if my_img:
                st.image(my_img, use_container_width=True)
            else:
                st.error("이미지를 불러오지 못했습니다.")
            st.info(my_info["desc"])
            
        with col2:
            st.markdown(f"#### 🤝 환상의 듀오: **{bf_info['champ']} ({bf_mbti})**")
            bf_img = get_champ_image(bf_info["id"])
            if bf_img:
                st.image(bf_img, use_container_width=True)
            else:
                st.error("이미지를 불러오지 못했습니다.")
            st.warning(f"최고의 호흡! {my_info['champ']}와(과) {bf_info['champ']}의 만남이에요. ✨")
            
        st.markdown("---")
        st.caption("※ 챔피언 이미지는 Riot Games API를 활용했습니다. 재미로만 즐겨주세요! GG! 🎮")
