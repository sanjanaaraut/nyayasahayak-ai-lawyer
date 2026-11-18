# appp.py — NyayaSahayak: Grounded AI Legal Helper for Everyday Indian Disputes
import json
import os
import streamlit as st

from legal_kb import LEGAL_KB, OUT_OF_SCOPE_NOTICE
from llm_helper import ask_ai, roleplay_ai

st.set_page_config(page_title="NyayaSahayak — AI Legal Helper", page_icon="⚖️", layout="wide")

# --- Sample stories for 1-click testing ---
SAMPLES = {
    "Rental Security Deposit": (
        "I vacated my 2BHK flat in Bengaluru on 1st October after giving 1 month notice on WhatsApp. "
        "I paid ₹60,000 security deposit via UPI when I moved in 14 months ago. I have the signed rent agreement, "
        "UPI transaction ID, and photos of the clean flat when I handed over the keys. Now my landlord is ignoring "
        "my calls and says he will deduct ₹45,000 for 'painting and wear and tear' without any bills."
    ),
    "Consumer Refund / Defective Service": (
        "I ordered a washing machine worth ₹28,500 from an online electronics store 3 weeks ago. "
        "It arrived with a broken drum. I raised 4 support tickets and have screenshots of all chats and the invoice, "
        "but they keep closing my ticket without a refund or replacement."
    ),
    "Unpaid Salary": (
        "I worked as a junior designer at a startup in Noida. I resigned properly with 30 days notice on 15th September, "
        "but they still haven't paid my August and September salary (total ₹70,000). I have my offer letter, "
        "previous salary slips, bank statements, and HR emails promising payment 'next week'."
    ),
}

# --- Sidebar: Settings & Scope ---
with st.sidebar:
    st.title("⚙️ Settings")
    default_key = os.environ.get("GEMINI_API_KEY", "")
    api_key = st.text_input("Gemini API Key", value=default_key, type="password", help="Get a free key at aistudio.google.com")
    model_name = st.selectbox(
        "AI Model (Swappable)",
        ["gemini-3.8-flash", "gemini-3.6-flash", "gemini-3.5-flash-lite", "gemini-3.1-pro-preview"],
    )
    language = st.selectbox(
        "Preferred Language",
        ["Auto-detect from my story", "English", "Hindi", "Hinglish", "Malayalam", "Tamil", "Bengali", "Marathi"],
    )
    st.divider()
    st.subheader("📌 Scope & Limits")
    st.info(OUT_OF_SCOPE_NOTICE)

# --- Main Header ---
st.title("⚖️ NyayaSahayak — Everyday Legal Helper (India)")
st.caption("Explain your problem in plain words (any language). Get a structured case breakdown, grounded options, a draft notice, and practice arguing your side.")

# --- Input Section ---
col1, col2 = st.columns([2, 1])
with col1:
    topic = st.selectbox(
        "1. Pick your problem type",
        list(LEGAL_KB.keys()) + ["Other / Not Listed"],
    )
with col2:
    st.write("")
    st.write("")
    if topic in SAMPLES and st.button("📝 Load Sample Story", use_container_width=True):
        st.session_state["story_input"] = SAMPLES[topic]

story = st.text_area(
    "2. Tell us what happened (include dates, amounts, and any proof you have)",
    key="story_input",
    height=140,
    placeholder="Example: My landlord hasn't returned my ₹50,000 deposit even though I vacated 3 weeks ago...",
)

analyze_clicked = st.button("🔍 Analyze My Case", type="primary")

# --- Handle Analysis ---
if analyze_clicked:
    if not api_key:
        st.error("Please enter your Gemini API Key in the left sidebar.")
    elif not story.strip():
        st.warning("Please type or load a story first.")
    elif topic == "Other / Not Listed":
        st.error(OUT_OF_SCOPE_NOTICE)
    else:
        kb_json = json.dumps(LEGAL_KB[topic], indent=2)
        lang_rule = (
            "Respond in the exact same language/script the user wrote their story in."
            if language == "Auto-detect from my story"
            else f"Respond in {language}."
        )

        analysis_system = f"""You are NyayaSahayak, a careful, honest Indian legal assistant.
{lang_rule}

STRICT ANTI-HALLUCINATION RULES:
1. You MUST ONLY cite laws, sections, portals, and fees present in the VERIFIED KNOWLEDGE BASE below.
2. NEVER invent any other section numbers, act names, or past court cases.
3. If the user's situation involves criminal threats, property title issues, or anything outside this knowledge base, explicitly say "I don't have verified legal rules for that part—please consult a real lawyer."

VERIFIED KNOWLEDGE BASE FOR '{topic}':
{kb_json}

Format your response clearly with these headings:
### 1. Case Facts (What Happened, When & Amount)
### 2. Proof You Have vs. Proof Still Needed
### 3. Where You Stand & Your Step-by-Step Options
### 4. What I Don't Know & When to Hire a Real Lawyer
"""
        notice_system = f"""You are drafting a formal, polite, firm written notice/complaint for an ordinary person in India.
{lang_rule}

STRICT RULES:
- Base it ONLY on the user's story and the verified laws in: {kb_json}
- Pre-fill all dates, amounts, and facts from the user's story.
- Only use clear brackets like [Your Full Name] or [Other Party's Name] for details missing from the story.
- Give a clear 15-day deadline to resolve the issue.
- Add a 1-line disclaimer at the bottom: "Note: This is an AI-generated draft for informational use. Review it carefully or have a lawyer check it before sending."
"""

        with st.spinner("Analyzing your case and drafting your notice..."):
            st.session_state["analysis_result"] = ask_ai(story, analysis_system, api_key, model_name)
            st.session_state["notice_result"] = ask_ai(story, notice_system, api_key, model_name)
            st.session_state["active_topic"] = topic
            st.session_state["active_story"] = story
            st.session_state["roleplay_history"] = [
                {
                    "role": "assistant",
                    "content": f"Let's practice! I'll play the other side ({'Landlord' if 'Rental' in topic else 'Company Support' if 'Consumer' in topic else 'HR / Employer'}). Go ahead and tell me why I owe you this money or resolution.",
                }
            ]

# --- Display Results in Tabs ---
if "analysis_result" in st.session_state:
    tab1, tab2, tab3 = st.tabs(["📋 Case Summary & Options", "✉️ Draft Notice / Complaint", "🎭 Practice Arguing"])

    with tab1:
        st.markdown(st.session_state["analysis_result"])

    with tab2:
        st.markdown(st.session_state["notice_result"])
        st.download_button(
            label="⬇️ Download Draft Notice (.txt)",
            data=st.session_state["notice_result"],
            file_name="draft_legal_notice.txt",
            mime="text/plain",
        )

    with tab3:
        st.caption("Practice staying calm and citing your proof. The AI will push back like the other party.")
        for msg in st.session_state.get("roleplay_history", []):
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        user_reply = st.chat_input("Type your response to the other party...")
        if user_reply:
            st.session_state["roleplay_history"].append({"role": "user", "content": user_reply})
            roleplay_system = f"""You are roleplaying as the opposing party in an Indian dispute ({st.session_state['active_topic']}).
User's original case: {st.session_state['active_story']}
Push back realistically (e.g., making excuses about delays, deductions, or company policy) so the user can practice responding firmly with their proof. Keep replies short (2-4 sentences). At the end of your reply in parentheses, add a brief 1-line [Coach Tip: ...] telling the user how strong their argument was."""

            with st.spinner("Thinking of a reply..."):
                ai_reply = roleplay_ai(st.session_state["roleplay_history"], roleplay_system, api_key, model_name)
            st.session_state["roleplay_history"].append({"role": "assistant", "content": ai_reply})
            st.rerun()