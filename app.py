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

    /* CARD STYLING - FIXED TEXT VISIBILITY */
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
        border-left: 5px solid #2a5298;
        
        /* CRITICAL FIX: Force text inside cards to be dark grey */
        color: #333333 !important; 
    }
    
    /* Specific overrides for text elements inside cards */
    .card p, .card li, .card span {
        color: #444444 !important;
        font-weight: 500;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.12);
    }

    /* Orange Highlight Text */
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

    /* Packing List Categories */
    .pack-category {
        font-size: 1.1em;
        font-weight: 700;
        color: #2c3e50 !important;
        border-bottom: 2px solid #ecf0f1;
        margin-bottom: 10px;
        padding-bottom: 5px;
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
    # Changed to a simpler URL or local usage if needed
    st.image("https://cdn-icons-png.flaticon.com/512/3194/3194766.png", width=120) 
with col_head2:
    st.markdown("<h1 style='padding-top: 20px;'>ANANTHAGIRI HILLS</h1>", unsafe_allow_html=True)
    # Added explicit color styling to the subtitle
    st.markdown("<h3 style='color: #555555;'>🎓 The Final Chapter: B.Tech Class of 2026</h3>", unsafe_allow_html=True)

st.write("") # Spacer

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
            <li>☕ <b>07:30 AM:</b> Breakfast</li>
            <li>⛰️ <b>08:30 AM:</b> Forest Trek to Viewpoint</li>
            <li>📸 <b>10:00 AM:</b> The Final Group Photo</li>
            <li>🚌 <b>11:00 AM:</b> Return Journey Starts</li>
            <li>🏠 <b>02:00 PM:</b> Reach Home (Approx)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- PACKING LIST (GRID FORMAT) ---
st.markdown("<h2 style='text-align:center;'>🎒 Backpack Check</h2>", unsafe_allow_html=True)

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.markdown("""
    <div class="card" style="padding: 15px; border-left: 3px solid #27ae60;">
        <div class="pack-category">👕 Wearables</div>
        <div class="pack-item">✅ Hoodie/Jacket</div>
        <div class="pack-item">✅ Comfy Shoes</div>
        <div class="pack-item">✅ Cap/Hat</div>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="card" style="padding: 15px; border-left: 3px solid #2980b9;">
        <div class="pack-category">🪥 Hygiene</div>
        <div class="pack-item">✅ Toothbrush/Paste</div>
        <div class="pack-item">✅ Face Wash</div>
        <div class="pack-item">✅ Hand Sanitizer</div>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="card" style="padding: 15px; border-left: 3px solid #8e44ad;">
        <div class="pack-category">📱 Tech & ID</div>
        <div class="pack-item">✅ Power Bank</div>
        <div class="pack-item">✅ Earphones</div>
        <div class="pack-item">✅ Charging Cable</div>
        <div class="pack-item">✅ <b>Original ID Proof</b></div>
    </div>
    """, unsafe_allow_html=True)

with p4:
    st.markdown("""
    <div class="card" style="padding: 15px; border-left: 3px solid #d35400;">
        <div class="pack-category">🍫 Survival</div>
        <div class="pack-item">✅ Water Bottle</div>
        <div class="pack-item">✅ Chocolates/Bars</div>
        <div class="pack-item">✅ Personal Meds</div>
        <div class="pack-item">✅ Cash (Small notes)</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- FINAL FOOTER ---
st.markdown("""
<div class="footer">
    <p>One last roll call. One last ride. Let's make it legendary. 🚀</p>
    <p style="font-size: 0.8em; opacity: 0.8;">Designed for B.Tech Batch 2022-2026</p>
</div>
""", unsafe_allow_html=True)

