import streamlit as st

st.set_page_config(
    page_title="Our Last B.Tech Trip 🌄",
    page_icon="🌄",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}
h1, h2, h3 {
    color: #FFD369;
}
.card {
    background-color: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>🌄 Ananthagiri Hills – Our Last B.Tech Trip</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>First bench or last bench, this memory belongs to all of us 💛</h3>", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h2>📍 Trip Details</h2>
    <p><b>Place:</b> Ananthagiri Hills</p>
    <p><b>Duration:</b> 1 Day – 1 Night</p>
    <p><b>Start:</b> Saturday, 20 Dec 2025 – 1:30 PM</p>
    <p><b>Return:</b> Sunday, 21 Dec 2025 – 11:00 AM</p>
    <p><b>Travel:</b> Bus (To & From)</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h2>💭 Why This Trip Matters</h2>
    <p>Assignments will end.</p>
    <p>Exams will fade.</p>
    <p>But this trip… will be remembered.</p>
    <p><i>This is not just travel, it’s closure.</i></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="card">
<h2>🗓️ Itinerary</h2>

<b>Saturday</b><br>
• Departure at 1:30 PM<br>
• Campsite check-in<br>
• Snacks & Icebreakers<br>
• Games, Dinner<br>
• DJ Night & Bonfire<br>
• Camping under the stars<br><br>

<b>Sunday</b><br>
• Sunrise view<br>
• Breakfast<br>
• Trek to viewpoint<br>
• Return journey around 11:00 AM
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>🎒 Things to Bring</h2>
<p>
Extra clothes (optional), jacket/hoodie, comfortable footwear, cap, toothbrush, toothpaste, face wash, towel, comb, medicines,
band-aids, sanitizer, tissues, mosquito repellent, mobile phone, power bank, charging cable, earphones, ID proof, cash,
water bottle, snacks, chocolates, energy bars, ORS packets, small backpack, light bedsheet or shawl.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>❤️ Final Note</h2>
<p>
One last roll call.<br>
One last group photo.<br>
One last trip as a class.<br><br>
<b>Let’s make it unforgettable.</b>
</p>
</div>
""", unsafe_allow_html=True)
