import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Urban Feast",
    page_icon="🍽️",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Raleway:wght@300;400;600&display=swap');

* { font-family: 'Raleway', sans-serif; }
h1, h2, h3 { font-family: 'Playfair Display', serif; }
.main { background-color: #0f0f0f; color: #f5f0e8; }

[data-testid="stAppViewContainer"] {
    background-color: #0f0f0f;
    color: #f5f0e8;
}

[data-testid="stSidebar"] {
    background-color: #1a1a1a;
}

.hero {
    text-align: center;
    padding: 80px 20px;
    background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
    url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1600');
    background-size: cover;
    background-position: center;
    border-radius: 16px;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 64px;
    color: #c9a84c;
    margin-bottom: 10px;
}

.hero p {
    font-size: 20px;
    color: #f5f0e8;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    color: #c9a84c;
    text-align: center;
    margin: 40px 0 20px 0;
}

.about-text {
    font-size: 18px;
    line-height: 1.9;
    color: #d4cfc7;
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}

.menu-card {
    background: #1a1a1a;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 20px;
    border: 1px solid #2a2a2a;
}

.menu-card h4 {
    color: #c9a84c;
    font-size: 18px;
    margin: 10px 0 4px 0;
}

.menu-card p {
    color: #aaa;
    font-size: 14px;
    margin: 0;
}

.menu-price {
    color: #c9a84c;
    font-weight: 600;
    font-size: 16px;
}

.chat-bubble-user {
    background: #c9a84c;
    color: #0f0f0f;
    padding: 12px 16px;
    border-radius: 16px 16px 4px 16px;
    margin: 8px 0;
    max-width: 70%;
    margin-left: auto;
    font-weight: 600;
}

.chat-bubble-bot {
    background: #1a1a1a;
    color: #f5f0e8;
    padding: 12px 16px;
    border-radius: 16px 16px 16px 4px;
    margin: 8px 0;
    max-width: 70%;
    border: 1px solid #2a2a2a;
}

.contact-box {
    background: #1a1a1a;
    border-radius: 12px;
    padding: 30px;
    text-align: center;
    border: 1px solid #2a2a2a;
}

.stButton button {
    background: #c9a84c !important;
    color: #0f0f0f !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 30px !important;
}

.stTextInput input {
    background: #1a1a1a !important;
    color: #f5f0e8 !important;
    border: 1px solid #c9a84c !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

page = st.sidebar.radio(
    "🍽️ Urban Feast",
    ["🏠 Home", "🍴 About", "📋 Menu", "🤖 Book a Table", "📍 Contact"]
)

if page == "🏠 Home":
    st.markdown("""
    <div class="hero">
        <h1>Urban Feast</h1>
        <p>Where Every Meal Tells a Story</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="contact-box">
            <h3 style="color:#c9a84c">🍜 Multi Cuisine</h3>
            <p style="color:#aaa">From Indian classics to Continental delights</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="contact-box">
            <h3 style="color:#c9a84c">🕯️ Fine Dining</h3>
            <p style="color:#aaa">Elegant ambiance for every occasion</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="contact-box">
            <h3 style="color:#c9a84c">🤖 AI Booking</h3>
            <p style="color:#aaa">Book your table instantly with our AI agent</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "🍴 About":
    st.markdown('<h2 class="section-title">Our Story</h2>', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1200", use_container_width=True)
    st.markdown("""
    <p class="about-text">
    Urban Feast was born from a simple belief — that great food brings people together.
    Nestled in the heart of the city, we blend the rich traditions of Indian cuisine
    with the sophistication of Continental and Asian flavors. Every dish is crafted
    with passion, using the freshest local ingredients and time-honored recipes passed
    down through generations. Whether you're here for a romantic dinner, a family
    celebration, or a casual lunch, Urban Feast promises an experience that delights
    all your senses.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">Why Choose Us</h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="contact-box">
            <h3 style="color:#c9a84c">👨‍🍳 Expert Chefs</h3>
            <p style="color:#aaa">Our chefs bring 20+ years of culinary excellence</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="contact-box">
            <h3 style="color:#c9a84c">🌿 Fresh Ingredients</h3>
            <p style="color:#aaa">Locally sourced, organic, and seasonal produce</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="contact-box">
            <h3 style="color:#c9a84c">✨ Warm Hospitality</h3>
            <p style="color:#aaa">Every guest is treated like family</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "📋 Menu":
    st.markdown('<h2 class="section-title">Our Menu</h2>', unsafe_allow_html=True)

    menu = {
        "🍛 Indian Mains": [
            {"name": "Dal Makhani", "desc": "Slow-cooked black lentils in rich butter gravy", "price": "₹220", "img": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?w=400"},
            {"name": "Paneer Tikka Masala", "desc": "Grilled cottage cheese in spiced tomato gravy", "price": "₹280", "img": "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=400"},
            {"name": "Veg Biryani", "desc": "Fragrant basmati rice with mixed vegetables", "price": "₹300", "img": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400"},
            {"name": "Palak Paneer", "desc": "Fresh cottage cheese in creamy spinach gravy", "price": "₹260","img": "https://images.unsplash.com/photo-1645177628172-a94c1f96diag?w=400"},
            {"name": "Masala Dosa", "desc": "Crispy rice crepe with spiced potato filling", "price": "₹160", "img": "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?w=400"},
        ],
       "🫓 Indian Breads": [
    {"name": "Butter Naan", "desc": "Soft leavened bread brushed with butter", "price": "₹60", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Nanb.jpg/320px-Nanb.jpg"},
    {"name": "Garlic Naan", "desc": "Tandoor baked bread with garlic and herbs", "price": "₹70", "img": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/03/garlic-naan-recipe-500x500.jpg"},
    {"name": "Stuffed Paratha", "desc": "Whole wheat bread stuffed with spiced potato", "price": "₹90", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Aloo_paratha.jpg/320px-Aloo_paratha.jpg"},
    {"name": "Puri", "desc": "Deep fried fluffy whole wheat bread", "price": "₹50", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/cinquante/Puri_with_Bhaji.jpg/320px-Puri_with_Bhaji.jpg"},
    {"name": "Laccha Paratha", "desc": "Layered whole wheat flaky bread from tandoor", "price": "₹80", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Lachha_paratha.jpg/320px-Lachha_paratha.jpg"},
],
        "🍚 Rice": [
            {"name": "Veg Biryani", "desc": "Fragrant basmati rice layered with spiced vegetables", "price": "₹300", "img": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?w=400"},
            {"name": "Jeera Rice", "desc": "Steamed basmati rice tempered with cumin seeds", "price": "₹150", "img": "https://images.unsplash.com/photo-1516684732162-798a0062be99?w=400"},
            {"name": "Veg Fried Rice", "desc": "Wok tossed rice with fresh vegetables and soy sauce", "price": "₹220", "img": "https://images.unsplash.com/photo-1603133872878-684f208fb84b?w=400"},
            {"name": "Lemon Rice", "desc": "Tangy South Indian rice with mustard and curry leaves", "price": "₹160", "img": "https://images.unsplash.com/photo-1596797038530-2c107229654b?w=400"},
            {"name": "Curd Rice", "desc": "Cooling yogurt rice with tempered mustard seeds", "price": "₹140", "img": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400"},
        ],
        "🍝 Continental": [
            {"name": "Margherita Pizza", "desc": "Classic tomato sauce with mozzarella and basil", "price": "₹380", "img": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400"},
            {"name": "Pasta Arrabiata", "desc": "Spicy tomato pasta with fresh basil", "price": "₹320", "img": "https://images.unsplash.com/photo-1555949258-eb67b1ef0ceb?w=400"},
            {"name": "Caesar Salad", "desc": "Crispy romaine with parmesan and croutons", "price": "₹240", "img": "https://images.unsplash.com/photo-1546793665-c74683f339c1?w=400"},
            {"name": "Veg Burger", "desc": "Crispy veggie patty with lettuce and cheese", "price": "₹260", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400"},
            {"name": "Bruschetta", "desc": "Toasted bread with tomatoes garlic and basil", "price": "₹180", "img": "https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?w=400"},
        ],
        "🍜 Asian": [
            {"name": "Veg Ramen", "desc": "Rich vegetable broth with noodles and tofu", "price": "₹320", "img": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=400"},
            {"name": "Veg Dim Sum", "desc": "Steamed dumplings with ginger soy dip", "price": "₹280", "img": "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=400"},
            {"name": "Thai Green Curry", "desc": "Coconut milk curry with vegetables and jasmine rice", "price": "₹340", "img": "https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?w=400"},
            {"name": "Veg Pad Thai", "desc": "Stir fried rice noodles with tofu and peanuts", "price": "₹300", "img": "https://images.unsplash.com/photo-1559314809-0d155014e29e?w=400"},
            {"name": "Spring Rolls", "desc": "Crispy rolls filled with vegetables and glass noodles", "price": "₹200", "img": "https://images.unsplash.com/photo-1548610762-8d2cd397cf44?w=400"},
        ],
        "🍰 Desserts": [
            {"name": "Gulab Jamun", "desc": "Soft milk dumplings in rose sugar syrup", "price": "₹120", "img": "https://images.unsplash.com/photo-1666274776257-0d5e0bfa2b52?w=400"},
            {"name": "Tiramisu", "desc": "Classic Italian coffee dessert with mascarpone", "price": "₹220", "img": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=400"},
            {"name": "Chocolate Lava Cake", "desc": "Warm chocolate cake with molten center", "price": "₹260", "img": "https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=400"},
            {"name": "Cheesecake", "desc": "New York style creamy cheesecake with strawberry", "price": "₹240", "img": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=400"},
            {"name": "Kulfi", "desc": "Traditional Indian ice cream with pistachio", "price": "₹110", "img": "https://images.unsplash.com/photo-1571506165871-ee72a35bc9d4?w=400"},
        ],
        "🥤 Drinks": [
            {"name": "Mango Lassi", "desc": "Chilled yogurt drink blended with fresh mango", "price": "₹120", "img": "https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=400"},
            {"name": "Masala Chai", "desc": "Spiced Indian tea with ginger and cardamom", "price": "₹60", "img": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400"},
            {"name": "Cold Coffee", "desc": "Chilled coffee blended with milk and ice cream", "price": "₹140", "img": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400"},
            {"name": "Virgin Mojito", "desc": "Mint lime soda with crushed ice", "price": "₹120", "img": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400"},
            {"name": "Hot Chocolate", "desc": "Rich creamy Belgian chocolate drink", "price": "₹150", "img": "https://images.unsplash.com/photo-1517578239113-b03992dcdd25?w=400"},
        ]
    }

    for category, items in menu.items():
        st.markdown(f'<h3 class="section-title">{category}</h3>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, item in enumerate(items):
            with cols[i % 3]:
                try:
                    st.image(item["img"], use_container_width=True)
                except:
                    st.markdown(f"🍽️")
                st.markdown(f"""
                <div class="menu-card">
                    <h4>{item["name"]}</h4>
                    <p>{item["desc"]}</p>
                    <br>
                    <span class="menu-price">{item["price"]}</span>
                </div>
                """, unsafe_allow_html=True)

elif page == "🤖 Book a Table":
    st.markdown('<h2 class="section-title">Book a Table</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#aaa;">Chat with our AI assistant to reserve your table</p>', unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "display_history" not in st.session_state:
        st.session_state.display_history = []

    for chat in st.session_state.display_history:
        if chat["role"] == "user":
            st.markdown(f'<div class="chat-bubble-user">{chat["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble-bot">🤖 {chat["content"]}</div>', unsafe_allow_html=True)

    user_input = st.text_input("Type your message...", key="user_input", placeholder="e.g. I want to book a table for 2 at 7pm")

    if st.button("Send"):
        if user_input:
            st.session_state.display_history.append({"role": "user", "content": user_input})
            try:
                res = requests.post(f"{API_URL}/chat", json={
                    "message": user_input,
                    "chat_history": st.session_state.chat_history
                })
                bot_reply = res.json()["response"]
            except Exception as e:
                bot_reply = f"Error: {str(e)}"

            st.session_state.chat_history.append({"role": "user", "content": user_input})
            st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
            st.session_state.display_history.append({"role": "assistant", "content": bot_reply})
            st.rerun()

    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.session_state.display_history = []
        st.rerun()

elif page == "📍 Contact":
    st.markdown('<h2 class="section-title">Find Us</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="contact-box">
            <h3 style="color:#c9a84c">📍 Address</h3>
            <p style="color:#aaa">12, Food Street, Koregaon Park<br>Pune, Maharashtra 411001</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="contact-box">
            <h3 style="color:#c9a84c">🕐 Hours</h3>
            <p style="color:#aaa">Mon - Sun<br>12:00 PM - 11:00 PM</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="contact-box">
            <h3 style="color:#c9a84c">📞 Contact</h3>
            <p style="color:#aaa">+91 98765 43210<br>hello@urbanfeast.in</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1200", use_container_width=True)