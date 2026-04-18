import streamlit as st
import random

# ------------------------
# 初期化
# ------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []
    st.session_state.questions = []

# ------------------------
# 質問データ
# ------------------------
base_questions = [
    ("やすみじかん、なにしてる？", [
        "A 🏃 はしりまわってあそぶ",
        "B 👀 みんなのようすを見てうごく",
        "C 🧩 すわってしずかにあそぶ",
        "D 🎲 きぶんであそびかえる"
    ]),
    ("ともだちとけんかしたら？", [
        "A 🔥 すぐいいかえす",
        "B 🧠 いちどきいてからはなす",
        "C 😌 あまり気にしない",
        "D 🤝 あいてにあわせてかえる"
    ]),
    ("ゲームでだいじなのは？", [
        "A ⚡ はやくかつこと",
        "B 🛡 まけないこと",
        "C 🔄 ながくつづけること",
        "D 🎯 あいてにあわせること"
    ]),
    ("しゅくだいはどうする？", [
        "A 💨 いっきにおわらせる",
        "B ✏️ ていねいにやる",
        "C 📅 すこしずつやる",
        "D 🎲 きぶんでやりかたをかえる"
    ]),
    ("あたらしいあそびをするときは？", [
        "A 🚀 すぐやってみる",
        "B 📖 ルールを見てからやる",
        "C 🐢 ゆっくりなれる",
        "D 👥 みんなにあわせる"
    ]),
]
extra_questions = [
    ("ヒーローになるなら？", [
        "A 💥 こうげきでたたかう",
        "B 🛡 まもりながらたたかう",
        "C 🔄 ずっとがんばる",
        "D ⚡ なんでもできる"
    ]),
    ("すきなどうぶつは？", [
        "A 🦁 ライオン",
        "B 🐘 ゾウ",
        "C 🐢 カメ",
        "D 🐒 サル"
    ]),
    ("ふしぎなちからをみにつけるなら？", [
        "A 💥 いっしゅんでパワーアップ",
        "B 🛡 なんでもまもるバリアー",
        "C ♻️ すぐにかいふく",
        "D ⚡ いろんなちからがつかえる"
    ]),
]

def generate_questions():
    q = base_questions.copy()
    q.append(random.choice(extra_questions))
    random.shuffle(q)
    return q

# ------------------------
# 判定（同点対策あり）
# ------------------------
def get_result(answers):
    count = {"A":0, "B":0, "C":0, "D":0}
    for a in answers:
        count[a] += 1

    max_score = max(count.values())
    top = [k for k, v in count.items() if v == max_score]

    if len(top) > 1:
        return "バランス"

    return {
        "A": "アタック",
        "B": "ディフェンス",
        "C": "スタミナ",
        "D": "バランス"
    }[top[0]]

# ------------------------
# TOP画面（ワクワクUI）
# ------------------------
if st.session_state.step == 0:

    st.markdown("## 🌀 ベイブレードX しんだん")
    st.write("キミのタイプを見つけて、さいきょうベイをゲットしよう！🔥")

    st.image("https://www.takaratomy.co.jp/products/beyblade/images/top/main_kv.jpg")

    if st.button("▶ スタート！", use_container_width=True):
        st.session_state.questions = generate_questions()
        st.session_state.answers = []
        st.session_state.step = 1
        st.rerun()

# ------------------------
# 質問画面（押しやすい＋戻る）
# ------------------------
elif st.session_state.step <= len(st.session_state.questions):

    q_index = st.session_state.step - 1
    question, options = st.session_state.questions[q_index]

    st.progress(st.session_state.step / len(st.session_state.questions))
    st.markdown(f"### Q{st.session_state.step}. {question}")

    for opt in options:
        if st.button(opt, use_container_width=True):
            st.session_state.answers.append(opt[0])
            st.session_state.step += 1
            st.rerun()

    # 戻るボタン
    if st.session_state.step > 1:
        if st.button("⬅ もどる"):
            st.session_state.step -= 1
            st.session_state.answers.pop()
            st.rerun()

# ------------------------
# 結果画面（売れる導線）
# ------------------------
else:

    result = get_result(st.session_state.answers)

    st.markdown("## 🎉 けっか！")

    if result == "アタック":
        st.markdown("### 💥 こうげきマスター！")
        st.write("いっしゅんで勝負をきめる！スピードでかつタイプ！🔥")

        st.write("👇 キミにピッタリのベイ！")

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://m.media-amazon.com/images/I/61MpAh-qOsL._AC_SY450_.jpg")
            st.write("ドランソード")
            st.link_button("👉 チェック", "https://www.amazon.co.jp/dp/B0C52R16P1")

        with col2:
            st.image("https://m.media-amazon.com/images/I/715NtHVPy-L._AC_SY450_.jpg")
            st.write("フェニックスウイング")
            st.link_button("👉 見てみる", "https://www.amazon.co.jp/dp/B0CMZSRJ3Q")

    elif result == "ディフェンス":
        st.markdown("### 🛡 まもりのたつじん！")
        st.write("こうげきをはねかえす！さいごに勝つタイプ！💪")

        st.write("👇 キミにピッタリのベイ！")

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://m.media-amazon.com/images/I/61N7ksTpjhL._AC_SY450_.jpg")
            st.write("ナイトフォートレス")
            st.link_button("👉 チェック", "https://www.amazon.co.jp/dp/B0GMDYS21K")

        with col2:
            st.image("https://m.media-amazon.com/images/I/71AMNY-FmqL._AC_SY450_.jpg")
            st.write("レオンクレスト")
            st.link_button("👉 見てみる", "https://www.amazon.co.jp/dp/B0D91K2WMS")

    elif result == "スタミナ":
        st.markdown("### 🔄 ねばりの王！")
        st.write("さいごまで回りつづける！あきらめないタイプ！🔥")

        st.write("👇 キミにピッタリのベイ！")

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://m.media-amazon.com/images/I/61qO6OBNzBL._AC_SY450_.jpg")
            st.write("ウィザードアーク")
            st.link_button("👉 チェック", "https://www.amazon.co.jp/dp/B0DWSRHP7J")

        with col2:
            st.image("https://m.media-amazon.com/images/I/61aJExH96+L._AC_SY450_.jpg")
            st.write("ヘルズサイズ")
            st.link_button("👉 見てみる", "https://www.amazon.co.jp/dp/B0C52C4L3T")

    else:
        st.markdown("### ⚡ オールラウンダー！")
        st.write("なんでもできる！バランスさいきょうタイプ！✨")

        st.write("👇 キミにピッタリのベイ！")

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://m.media-amazon.com/images/I/61WEAT7WNKL._AC_SY450_.jpg")
            st.write("エンペラーマイト")
            st.link_button("👉 チェック", "https://www.amazon.co.jp/dp/B0FV6Y4MH4")

        with col2:
            st.image("https://m.media-amazon.com/images/I/712keT+tMML._AC_SY450_.jpg")
            st.write("スコーピオスピア")
            st.link_button("👉 見てみる", "https://www.amazon.co.jp/dp/B0F47G3QJT")

    st.divider()

    if st.button("🔁 もういちどやる", use_container_width=True):
        st.session_state.step = 0
        st.rerun()