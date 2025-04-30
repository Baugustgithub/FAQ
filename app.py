import streamlit as st
import pandas as pd

# Replace with your published sheet CSV URL
csv_url = "https://docs.google.com/spreadsheets/d/e/YOUR-LINK-HERE/pub?output=csv"

@st.cache_data(ttl=300)
def load_faq():
    return pd.read_csv(csv_url)

faq_df = load_faq()

st.set_page_config(page_title="VCU Procurement FAQ", layout="wide")
st.title("🔍 VCU Procurement FAQ")

search = st.text_input("Search questions or answers")

# Filter
if search:
    filtered = faq_df[faq_df.apply(lambda row: search.lower() in row['Question'].lower() 
                                                or search.lower() in row['Answer'].lower(), axis=1)]
else:
    filtered = faq_df

# Display
if filtered.empty:
    st.warning("No matching questions found.")
else:
    for _, row in filtered.iterrows():
        with st.expander(row["Question"]):
            st.markdown(row["Answer"])
