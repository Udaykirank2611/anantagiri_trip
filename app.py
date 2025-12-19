import streamlit as st

st.set_page_config(
    page_title="The Last Ride | Class of 2026",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR VISIBILITY AND STYLE ---
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    /* Global Settings - Force Light Background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Force all Headers to be Dark Blue */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif;
        color: #1e3c72 !important;
    }

    /* HTML CARD STYLING (For Static Content) */
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
        border-left: 5px solid #2a5298;
        color: #333333 !important; 
    }
    
    .card p, .card li, .card span {
        color: #444444 !important;
        font-weight: 500;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.12);
    }

    /* Highlight Text */
    .highlight {
        color: #e67e22 !important;
        font-weight: 800;
    }

    /* Itinerary Headers */
    .day-header {
        background-color: #e3f2fd;
        padding: 10px 15px;
        border-radius: 10px;
        color: #1565c0 !important;
        font-weight: 700;
        margin-bottom: 15px;
        text-align: center;
        border: 1px solid #bbdefb;
    }

    /* CUSTOM STYLE FOR STREAMLIT CONTAINERS (To make them look like cards) */
    div[data-testid="stBorder"] {
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        border: none;
        padding: 20px;
    }

    /* Checkbox Styling */
    .stCheckbox label {
        font-size: 16px;
        color: #333 !important;
    }
    
    /* Footer Styling */
    .footer {
        text-align: center;
        font-size: 1.2em;
        color: #555555 !important;
        margin-top: 50px;
        font-style: italic;
        font-weight: 600;
    }

</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col_head1, col_head2 = st.columns([1, 4])
with col_head1:
    st.image("https://cdn-icons-png.flaticon.com/512/3194/3194766.png", width=120) 
with col_head2:
    st.markdown("<h1 style='padding-top: 20px;'>ANANTHAGIRI HILLS</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #555555;'>🎓 The Final Chapter: B.Tech Class of 2026</h3>", unsafe_allow_html=True)

st.write("") 

# --- TRIP SUMMARY & EMOTION ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📍 The Plan</h3>
        <p><b>🌍 Destination:</b> Ananthagiri Hills</p>
        <p><b>📅 Date:</b> Dec 20 - Dec 21, 2025 (Sat-Sun)</p>
        <p><b>🚌 Transport:</b> Private Bus (To & From)</p>
        <p><b>⏰ Departure:</b> Saturday @ 1:30 PM Sharp</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="border-left: 5px solid #e67e22;">
        <h3>💛 Why You Can't Miss This</h3>
        <p>Four years. Countless assignments. One final year.</p>
        <p>This isn't just about the hills; it's about the people next to you.</p>
        <p class="highlight">"First bench or last bench, this memory belongs to all of us."</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- ITINERARY SECTION ---
st.markdown("<h2 style='text-align:center; margin-bottom: 30px;'>🗺️ The Weekend Roadmap</h2>", unsafe_allow_html=True)

it_col1, it_col2 = st.columns(2)

with it_col1:
    st.markdown("""
    <div class="card">
        <div class="day-header">SATURDAY (DEC 20)</div>
        <ul style="list-style-type: none; padding-left: 0; line-height: 2;">
            <li>🚌 <b>01:30 PM:</b> Bus Departure (Don't be late!)</li>
            <li>🏕️ <b>05:00 PM:</b> Campsite Check-in</li>
            <li>🥪 <b>05:30 PM:</b> High Tea & Icebreakers</li>
            <li>🔥 <b>08:00 PM:</b> <span class="highlight">Bonfire & DJ Night</span></li>
            <li>🍽️ <b>09:30 PM:</b> Dinner Under the Stars</li>
            <li>🌌 <b>All Night:</b> Camping & Conversations</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with it_col2:
    st.markdown("""
    <div class="card">
        <div class="day-header">SUNDAY (DEC 21)</div>
        <ul style="list-style-type: none; padding-left: 0; line-height: 2;">
            <li>🌅 <b>06:00 AM:</b> Sunrise View (Wake up!)</li>
            <li>☕ <b>07:30 AM:</b> Forest Trek to Viewpoint</li>
            <li>⛰️ <b>08:30 AM:</b> Breakfast</li>
            <li>📸 <b>10:00 AM:</b> The Final Group Photo</li>
            <li>🚌 <b>12:00 AM:</b> Return Journey Starts (Approx)</li>
            <li>🏠 <b>03:00 PM:</b> Reach Home (Approx)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- INTERACTIVE PACKING LIST ---
st.markdown("<h2 style='text-align:center; margin-bottom: 20px;'>🎒 Backpack Check</h2>", unsafe_allow_html=True)
st.caption("Tick the box when you pack the item! It will strike through when done.")

# Helper function for strikethrough logic
def smart_checkbox(item_name, key_group):
    # Unique key for every item
    key = f"{key_group}_{item_name}"
    # Check current state
    checked = st.session_state.get(key, False)
    
    # Logic: If checked, add strikethrough formatting (~~text~~)
    label = f"~~{item_name}~~" if checked else item_name
    
    st.checkbox(label, key=key)

# Columns for the list
p1, p2, p3, p4 = st.columns(4)

with p1:
    with st.container(border=True):
        st.markdown("<h4 style='color:#27ae60 !important;'>👕 Wearables</h4>", unsafe_allow_html=True)
        smart_checkbox("Hoodie/Jacket", "wear")
        smart_checkbox("Comfy Shoes", "wear")
        smart_checkbox("Cap/Hat", "wear")
        smart_checkbox("Small Towel", "wear")
        smart_checkbox("Extra Outfit", "wear")

with p2:
    with st.container(border=True):
        st.markdown("<h4 style='color:#2980b9 !important;'>🪥 Hygiene</h4>", unsafe_allow_html=True)
        smart_checkbox("Toothbrush/Paste", "hyg")
        smart_checkbox("Face Wash", "hyg")
        smart_checkbox("Hand Sanitizer", "hyg")
        smart_checkbox("Tissues/Wipes", "hyg")
        smart_checkbox("Deodorant", "hyg")

with p3:
    with st.container(border=True):
        st.markdown("<h4 style='color:#8e44ad !important;'>📱 Tech & ID</h4>", unsafe_allow_html=True)
        smart_checkbox("Power Bank", "tech")
        smart_checkbox("Earphones", "tech")
        smart_checkbox("Charging Cable", "tech")
        smart_checkbox("Original ID Proof", "tech")

with p4:
    with st.container(border=True):
        st.markdown("<h4 style='color:#d35400 !important;'>🍫 Survival</h4>", unsafe_allow_html=True)
        smart_checkbox("Water Bottle", "surv")
        smart_checkbox("Chocolates/Bars", "surv")
        smart_checkbox("Personal Meds", "surv")
        smart_checkbox("Cash (Small notes)", "surv")
        smart_checkbox("Plastic Bag (Trash)", "surv")

st.markdown("---")

# --- FINAL FOOTER ---
st.markdown("""
<div class="footer">
    <p>One last roll call. One last ride. Let's make it legendary. 🚀</p>
    <p style="font-size: 0.8em; opacity: 0.8;">Designed for B.Tech Batch 2022-2026</p>
</div>
""", unsafe_allow_html=True)
