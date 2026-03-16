import streamlit as st

# 페이지 설정 (탭 제목과 아이콘)
st.set_page_config(page_title="MBTI 소울메이트 찾기", page_icon="✨")

# MBTI 궁합 데이터 (가장 잘 알려진 찰떡궁합 페어링 적용)
mbti_best_friends = {
    "ENFJ": {"bf": "INFP", "desc": "열정적인 리더와 따뜻한 몽상가의 만남! 서로의 감정을 깊이 이해해 주는 완벽한 힐링 콤비예요. 💖"},
    "ENTJ": {"bf": "INTP", "desc": "추진력 갑과 논리력 갑! 아이디어를 현실로 만드는 데 이보다 더 좋은 파트너는 없어요. 🌍"},
    "ENFP": {"bf": "INTJ", "desc": "인간 리트리버와 츤데레 전략가! 서로의 부족한 점을 완벽하게 채워주는 자석 같은 끌림이 있어요. ✨"},
    "ENTP": {"bf": "INFJ", "desc": "팩트 폭격기와 다정한 통찰가! 깊고 흥미로운 대화가 끊이지 않는 환상의 티키타카를 자랑해요. 🎭"},
    "ESFJ": {"bf": "ISFP", "desc": "다정한 챙김러와 자유로운 예술가! 편안하고 따뜻한 분위기 속에서 서로에게 스며드는 관계예요. 🎨"},
    "ESTJ": {"bf": "ISTP", "desc": "철저한 계획러와 만능 재주꾼! 각자의 영역을 존중하면서도 필요할 때 최고의 시너지를 내요. 🛠️"},
    "ESFP": {"bf": "ISFJ", "desc": "분위기 메이커와 든든한 수호자! 신나게 놀고 든든하게 챙겨주는 조화로운 관계랍니다. 🛡️"},
    "ESTP": {"bf": "ISTJ", "desc": "불도저 행동파와 꼼꼼한 원칙주의자! 브레이크와 엑셀처럼 서로의 속도를 완벽하게 조절해 줘요. 📊"},
    "INFP": {"bf": "ENFJ", "desc": "따뜻한 몽상가와 열정적인 리더! 나의 내면을 알아주고 세상 밖으로 이끌어주는 최고의 지원군이에요. 🌱"},
    "INTP": {"bf": "ENTJ", "desc": "논리적인 사색가와 전략적인 지도자! 나의 기발한 아이디어를 세상에 실현시켜 줄 든든한 파트너입니다. 🚀"},
    "INTJ": {"bf": "ENFP", "desc": "용의주도한 전략가와 스파크 튀는 활동가! 계획적인 내 삶에 즐거운 변수를 만들어주는 비타민 같은 친구예요. 💊"},
    "INFJ": {"bf": "ENTP", "desc": "통찰력 있는 예언자와 뜨거운 변론가! 나의 복잡한 내면을 흥미롭게 탐구해 주는 유일무이한 소울메이트입니다. 🔮"},
    "ISFP": {"bf": "ESFJ", "desc": "호기심 많은 예술가와 사교적인 외교관! 나의 조용한 다정함을 알아보고 따뜻하게 감싸주는 친구예요. 🌸"},
    "ISTP": {"bf": "ESTJ", "desc": "만능 재주꾼과 엄격한 관리자! 감정 소모 없이 깔끔하고 효율적으로 척척 맞는 실용주의 콤비입니다. ⚙️"},
    "ISFJ": {"bf": "ESFP", "desc": "용감한 수호자와 자유로운 영혼! 조용한 내 일상에 환한 웃음꽃을 피워주는 해피 바이러스예요. 🌻"},
    "ISTJ": {"bf": "ESTP", "desc": "청렴결백한 논리주의자와 모험을 즐기는 사업가! 원칙적인 내 삶에 신선한 자극을 주는 멋진 친구랍니다. 🎢"}
}

# 앱 헤더 및 설명
st.title("✨ 나의 MBTI 소울메이트 찾기 🔍")
st.write("내 MBTI를 선택하면, 찰떡궁합인 **운명의 절친**을 알려드려요! 🎈")
st.markdown("---")

# MBTI 선택 드롭다운 (selectbox)
mbti_list = list(mbti_best_friends.keys())
user_mbti = st.selectbox("👉 당신의 MBTI는 무엇인가요?", mbti_list, index=None, placeholder="MBTI를 선택해주세요!")

# 결과 확인 버튼
if st.button("내 절친 찾기! 🚀"):
    if user_mbti is None:
        st.warning("앗! MBTI를 먼저 선택해주세요. 🤔")
    else:
        # 재미있는 풍선 효과!
        st.balloons()
        
        # 결과 데이터 가져오기
        bf_info = mbti_best_friends[user_mbti]
        
        # 결과 출력
        st.markdown(f"### 🎉 **{user_mbti}**의 찰떡궁합 절친은 바로 **{bf_info['bf']}**입니다!")
        st.success(bf_info['desc'])
        
        # 추가 꾸밈 요소
        st.caption("※ 궁합은 재미로만 봐주세요! 세상의 모든 친구 관계는 소중하니까요 🥰")
