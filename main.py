import streamlit as st
from st_pages import Page, Section, show_pages
from streamlit_authenticator import Authenticate

from CONFIG import AUTH_SYSTEM_ENABLED
from backend.utils.os_utils import read_yaml_file, dump_dict_to_yaml


def main_page():
    show_pages(
        [
            Page("main.py", "Hummingbot Dashboard", "📊"),
            Section("Bot Orchestration", "🐙"),
            Page("frontend/pages/orchestration/instances/app.py", "Instances", "🦅"),
            Page("frontend/pages/orchestration/launch_bot_v2/app.py", "Deploy", "🚀"),
            # Page("frontend/pages/orchestration/launch_bot_v2_st/app.py", "Deploy ST", "🙌"),
            # Page("pages/file_manager/app.py", "File Explorer", "🗂"),
            Section("Config Generator", "🎛️"),
            Page("frontend/pages/config/pmm_simple/app.py", "PMM Simple", "👨‍🏫"),
            Page("frontend/pages/config/pmm_dynamic/app.py", "PMM Dynamic", "👩‍🏫"),
            Page("frontend/pages/config/dman_maker_v2/app.py", "D-Man Maker V2", "🤖"),
            Page("frontend/pages/config/bollinger_v1/app.py", "Bollinger V1", "📈"),
            Page("frontend/pages/config/macd_bb_v1/app.py", "MACD_BB V1", "📊"),
            Page("frontend/pages/config/supertrend_v1/app.py", "SuperTrend V1", "👨‍🔬"),
            Page("frontend/pages/config/xemm_controller/app.py", "XEMM Controller", "⚡️"),
            # Page("frontend/pages/config/position_builder/app.py", "Position Builder", "🔭"),
            Section("Data", "💾"),
            Page("frontend/pages/data/download_candles/app.py", "Download Candles", "💹"),
            # Page("pages/create/create.py", "Create", "⚔️"),
            # Page("pages/optimize/optimize.py", "Optimize", "🧪"),
            # Page("pages/analyze/analyze.py", "Analyze", "🔬"),
            Section("Community Pages", "👨‍👩‍👧‍👦"),
            # Page("frontend/pages/performance/strategy_performance/app.py", "Strategy Performance", "🚀"),
            Page("frontend/pages/data/token_spreads/app.py", "Token Spreads", "🧙"),
            Page("frontend/pages/data/tvl_vs_mcap/app.py", "TVL vs Market Cap", "🦉"),
        ]
    )

    # Readme Section
    readme_container = st.container()
    with readme_container:
        st.markdown("# 📊 Hummingbot Dashboard")
        st.markdown("""
            Hummingbot Dashboard is an open source application that helps you create, backtest, and optimize various 
            types of algo trading strategies. Afterwards, you can deploy them as [Hummingbot](http://hummingbot.org) 
            instances in either paper or live trading mode.""")

    st.write("---")

    st.header("Getting Started")

    st.write(
        "Watch the [Hummingbot Dashboard Tutorial playlist](https://www.youtube.com/watch?v=a-kenMqRB00) to get started!")

    # Container for the videos
    container = st.container()

    video_titles = [
        "1 - Introduction to Dashboard",
        "2 - Setting up the Environment",
        "3 - Managing Credentials",
        "4 - Using the Master Bot Profile",
        "5 - Deploying Bots and Running Strategies",
        "7 - Controllers, Backtesting, and Optimization",
        "8 - Deploying Best Strategies from Backtests",
        "9 - Conclusions and Next Steps"
    ]
    # List of YouTube video links
    video_links = [
        "https://www.youtube.com/embed/a-kenMqRB00",
        "https://www.youtube.com/embed/AbezIhb6iJg",
        "https://www.youtube.com/embed/VmlD_WQVe4M",
        "https://www.youtube.com/embed/MPQTnlDXPno",
        "https://www.youtube.com/embed/915E-C2LWdg",
        "https://www.youtube.com/embed/bAi2ok7_boo",
        "https://www.youtube.com/embed/BJf3ml-9JIQ",
        "https://www.youtube.com/embed/ug_SSZb2HYE",
    ]

    # Ensure the lists have the same length
    assert len(video_titles) == len(video_links), "Mismatch between titles and links."

    # Create a carousel-like feature
    video_selection = st.selectbox("Choose a video:", options=video_titles)

    # Get the index of the selected video title
    selected_index = video_titles.index(video_selection)

    # Display the selected video
    st.video(video_links[selected_index])

    st.write("---")

    st.header("Feedback and Issues")

    st.write("Please give us feedback in the **#dashboard** channel of the [Hummingbot Discord](https://discord.gg/hummingbot)! 🙏")

    st.write("If you encounter any bugs or have suggestions for improvement, please create an issue in the [Hummingbot Dashboard Github](https://github.com/hummingbot/dashboard).")


# config = read_yaml_file("credentials.yml")
#
# if "authenticator" not in st.session_state:
#     st.session_state.authenticator = Authenticate(
#         config['credentials'],
#         config['cookie']['name'],
#         config['cookie']['key'],
#         config['cookie']['expiry_days'],
#         config['preauthorized']
#     )

# if not AUTH_SYSTEM_ENABLED:
main_page()
# elif st.session_state["authentication_status"]:
#     config["credentials"] = st.session_state.authenticator_handler.credentials
#     dump_dict_to_yaml(config, "credentials.yml")
#     with st.sidebar:
#         st.write(f'Welcome {st.session_state["name"]}!')
#     st.session_state.authenticator.logout(location='sidebar')  # Updated logout call
#     main_page()
# else:
#     show_pages([
#         Page("main.py", "Hummingbot Dashboard", "📊"),
#     ])
#     name, authentication_status, username = st.session_state.authenticator.login(location='main')  # Updated login call
#     if st.session_state["authentication_status"] == False:
#         st.error('Username/password is incorrect')
#     elif st.session_state["authentication_status"] == None:
#         st.warning('Please enter your username and password')
#     st.write("---")
#     st.write("If you are pre-authorized, you can login with your pre-authorized mail!")
#     st.session_state.authenticator.register_user(location='main')  # Updated register user call
