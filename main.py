import streamlit as st

# 페이지 설정
st.set_page_config(page_title="포켓몬 MBTI 소울메이트", page_icon="⚡", layout="centered")

# 포켓몬 이미지 URL을 가져오는 함수 (PokeAPI 공식 고화질 아트워크)
def get_poke_img(dex_number):
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{dex_number}.png"

# MBTI별 찰떡 포켓몬 및 궁합 데이터
mbti_data = {
    "ENFJ": {"poke": "망나뇽", "dex": 149, "bf": "INFP", "desc": "다정하고 듬직하게 모두를 이끄는 망나뇽 같아요! 🐉"},
    "ENTJ": {"poke": "뮤츠", "dex": 150, "bf": "INTP", "desc": "압도적인 카리스마와 지능으로 무장한 뮤츠! 🧬"},
    "ENFP": {"poke": "피카츄", "dex": 25, "bf": "INTJ", "desc": "어딜 가나 사랑받는 에너자이저 인간 피카츄! ⚡"},
    "ENTP": {"poke": "팬텀", "dex": 94, "bf": "INFJ", "desc": "장난기 넘치고 아이디어가 번뜩이는 팬텀! 👻"},
    "ESFJ": {"poke": "럭키", "dex": 113, "bf": "ISFP", "desc": "모두의 행복을 챙기는 따뜻한 마음씨의 럭키! 🥚"},
    "ESTJ": {"poke": "괴력몬", "dex": 68, "bf": "ISTP", "desc": "포기를 모르는 추진력 갑! 든든한 괴력몬! 💪"},
    "ESFP": {"poke": "푸린", "dex": 39, "bf": "ISFJ", "desc": "주목받는 걸 즐기는 본투비 아이돌 푸린! 🎤"},
    "ESTP": {"poke": "윈디", "dex": 59, "bf": "ISTJ", "desc": "거침없이 달려나가는 행동파 윈디! 🐾"},
    "INFP": {"poke": "뮤", "dex": 151, "bf": "ENFJ", "desc": "맑고 순수한 마음을 가진 환상의 포켓몬 뮤! 🫧"},
    "INTP": {"poke": "야도킹", "dex": 199, "bf": "ENTJ", "desc": "세상의 진리를 탐구하는 천재적인 야도킹! 👑"},
    "INTJ": {"poke": "후딘", "dex": 65, "bf": "ENFP", "desc": "IQ 5000! 철저한 전략가 후딘과 똑 닮았어요. 🥄"},
    "INFJ": {"poke": "가디안", "dex": 282, "bf": "ENTP", "desc": "신비롭고 헌신적인 수호자 가디안! 🔮"},
    "ISFP": {"poke": "루브도", "dex": 235, "bf": "ESFJ", "desc": "자신만의 색깔로 세상을 그리는 예술가 루브도! 🎨"},
    "ISTP": {"poke": "루카리오", "dex": 448, "bf": "ESTJ", "desc": "상황 판단이 빠르고 시크한 매력의 루카리오! 🐺"},
    "ISFJ": {"poke": "이상해씨", "dex": 1, "bf": "ESFP", "desc": "조용하지만 변함없이 곁을 지켜주는 이상해씨! 🌱"},
    "ISTJ": {"poke": "이상해꽃", "dex": 3, "bf": "ESTP", "desc": "뿌리 깊은 나무처럼 흔들림 없이 우직한 이상해꽃! 🌺"}
}

# 앱 헤더
st.title("⚡ 나와 꼭 맞는 포켓몬 & 소울메이트 찾기 🔍")
st.write("간단한 4가지 질문으로 **나의 포켓몬 본캐**와 **찰떡궁합 포켓몬 친구**를 찾아보세요! 🎈")
st.markdown("---")

# 질문 목록
st.subheader("🧐 나를 알아보는 심리 테스트")

q1_opt1 = "밖으로 나가서 신나게 놀며 에너지를 얻는다! 🏃‍♂️"
q1_opt2 = "집이 최고! 조용히 뒹굴거리며 충전한다. 🏠"
q1 = st.radio("1. 주말에 꿀 같은 자유시간이 생겼다! 나는?", (q1_opt1, q1_opt2), index=None)

q2_opt1 = "있는 그대로, 세세한 사실과 경험을 바탕으로 설명한다. 📝"
q2_opt2 = "비유와 상상을 섞어가며, 전체적인 느낌과 의미 위주로 설명한다. ☁️"
q2 = st.radio("2. 친구에게 어제 본 영화를 설명할 때 나는?", (q2_opt1, q2_opt2), index=None)

q3_opt1 = "무슨 화분 샀어? 물은 얼마나 줘야 해? (해결책) 🪴"
q3_opt2 = "왜 우울해 ㅠㅠ 무슨 일 있었어? (공감) 🥺"
q3 = st.radio("3. 친구가 '나 우울해서 화분 샀어'라고 한다면 나의 반응은?", (q3_opt1, q3_opt2), index=None)

q4_opt1 = "시간 단위로 계획을 철저하게 세워야 마음이 편하다. 🗓️"
q4_opt2 = "발길 닿는 대로! 융통성 있게 즉흥적으로 돌아다닌다. 🗺️"
q4 = st.radio("4. 기대하던 여행을 떠날 때 나는?", (q4_opt1, q4_opt2), index=None)

st.markdown("---")

# 결과 확인 버튼
if st.button("내 포켓몬 & 절친 결과 보기! 🚀"):
    # 모든 질문에 답했는지 확인
    if not all([q1, q2, q3, q4]):
        st.warning("앗! 몬스터볼을 던지기 전에 4개의 질문에 모두 체크해주세요! 🔴")
    else:
        # 팡팡 터지는 풍선 효과!
        st.balloons()
        
        # MBTI 계산 로직
        my_mbti = ""
        my_mbti += "E" if q1 == q1_opt1 else "I"
        my_mbti += "S" if q2 == q2_opt1 else "N"
        my_mbti += "T" if q3 == q3_opt1 else "F"
        my_mbti += "J" if q4 == q4_opt1 else "P"
        
        # 내 데이터 및 절친 데이터 가져오기
        my_info = mbti_data[my_mbti]
        bf_mbti = my_info["bf"]
        bf_info = mbti_data[bf_mbti]
        
        st.success(f"### 🎉 당신의 MBTI는 **{my_mbti}** 입니다!")
        st.write("---")
        
        # 결과를 2개의 열로 나누어 시각적으로 예쁘게 배치
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"#### 🧑 나의 포켓몬: **{my_info['poke']}**")
            st.image(get_poke_img(my_info["dex"]), use_column_width=True)
            st.info(my_info["desc"])
            
        with col2:
            st.markdown(f"#### 🤝 절친 포켓몬: **{bf_info['poke']} ({bf_mbti})**")
            st.image(get_poke_img(bf_info["dex"]), use_column_width=True)
            st.warning(f"서로의 부족한 점을 채워주는 최고의 파트너! {my_info['poke']}와 {bf_info['poke']}의 만남이에요. ✨")
            
        st.markdown("---")
        st.caption("※ 포켓몬 이미지는 PokeAPI를 활용하여 스트림릿 클라우드에서 안전하게 불러옵니다. 재미로만 즐겨주세요! 🥰")
