import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SIEGE The Clothing Empire",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --cream: #F5F0E8;
    --charcoal: #1A1A18;
    --warm-gray: #8C8880;
    --accent: #C4973B;
    --accent-light: #E8C97A;
    --red: #B84040;
    --card-bg: #FEFCF8;
    --border: #E2DBD0;
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--cream) !important;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] { background: transparent !important; }

/* Hide default streamlit elements */
#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--cream); }
::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 3px; }

/* Buttons */
.stButton > button {
    background: var(--charcoal) !important;
    color: var(--cream) !important;
    border: none !important;
    border-radius: 0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    padding: 0.65rem 1.6rem !important;
    transition: all 0.25s ease !important;
}
.stButton > button:hover {
    background: var(--accent) !important;
    color: var(--charcoal) !important;
}

/* Accent button variant */
.accent-btn .stButton > button {
    background: var(--accent) !important;
    color: var(--charcoal) !important;
}
.accent-btn .stButton > button:hover {
    background: var(--charcoal) !important;
    color: var(--cream) !important;
}

/* Inputs */
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stNumberInput > div > div > input {
    background: var(--card-bg) !important;
    border: 1px solid var(--border) !important;
    border-radius: 0 !important;
    font-family: 'DM Sans', sans-serif !important;
    color: var(--charcoal) !important;
}

/* Remove red focus rings */
.stTextInput > div > div > input:focus,
.stSelectbox > div > div:focus-within {
    border-color: var(--accent) !important;
    box-shadow: none !important;
}

/* Divider */
hr { border-color: var(--border) !important; }

/* Nav pill active */
.nav-active {
    border-bottom: 2px solid var(--accent);
    color: var(--charcoal) !important;
}

/* Columns padding fix */
[data-testid="column"] { padding: 0.5rem !important; }

/* Metric */
[data-testid="stMetricValue"] {
    color: var(--charcoal) !important;
    font-family: 'Playfair Display', serif !important;
}

/* Badge */
.badge {
    background: var(--red);
    color: white;
    border-radius: 50%;
    padding: 1px 6px;
    font-size: 0.7rem;
    font-weight: 700;
    vertical-align: super;
}

/* Toast notification */
.toast {
    background: var(--charcoal);
    color: var(--cream);
    padding: 0.75rem 1.25rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    letter-spacing: 0.03em;
    border-left: 3px solid var(--accent);
}
</style>
""", unsafe_allow_html=True)

# ── Data ───────────────────────────────────────────────────────────────────────
PRODUCTS = [
    # Women
    {"id": 1, "name": "Ivory Linen Blazer", "category": "Women", "subcategory": "Outerwear",
     "price": 189.00, "sizes": ["XS", "S", "M", "L", "XL"], "colors": ["Ivory", "Sand", "Black"],
     "rating": 4.8, "reviews": 124, "new": True, "sale": False,
     "emoji": "🧥", "description": "Effortlessly refined linen blazer with a relaxed silhouette. Perfect for layering over everything from tailored trousers to summer dresses.", "tag": "Bestseller"},
    {"id": 2, "name": "The Cashmere Crew", "category": "Women", "subcategory": "Tops",
     "price": 145.00, "sizes": ["XS", "S", "M", "L"], "colors": ["Oatmeal", "Sage", "Dusty Rose"],
     "rating": 4.9, "reviews": 312, "new": False, "sale": False,
     "emoji": "👕", "description": "Luxuriously soft 100% Grade-A cashmere crew neck. A wardrobe foundation you'll reach for again and again.", "tag": "Fan Favourite"},
    {"id": 3, "name": "Wide Leg Silk Trousers", "category": "Women", "subcategory": "Bottoms",
     "price": 225.00, "original_price": 298.00, "sizes": ["XS", "S", "M", "L", "XL"], "colors": ["Champagne", "Slate", "Onyx"],
     "rating": 4.7, "reviews": 89, "new": False, "sale": True,
     "emoji": "👖", "description": "Fluid silk-satin trousers with a high-rise waist and generous wide leg. The epitome of understated glamour.", "tag": "On Sale"},
    {"id": 4, "name": "Cotton Poplin Shirt Dress", "category": "Women", "subcategory": "Dresses",
     "price": 165.00, "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "colors": ["White", "Pale Blue", "Stripe"],
     "rating": 4.6, "reviews": 201, "new": True, "sale": False,
     "emoji": "👗", "description": "Crisp cotton poplin shirt dress with a cinched waist and midi length. Your go-anywhere, do-anything uniform.", "tag": "New"},
    {"id": 5, "name": "Merino Ribbed Cardigan", "category": "Women", "subcategory": "Tops",
     "price": 135.00, "original_price": 170.00, "sizes": ["XS", "S", "M", "L"], "colors": ["Camel", "Ecru", "Charcoal"],
     "rating": 4.8, "reviews": 178, "new": False, "sale": True,
     "emoji": "🧶", "description": "Fine merino wool ribbed cardigan with tortoiseshell buttons. Layer it open or wear it buttoned as a top.", "tag": "On Sale"},
    {"id": 6, "name": "Leather Mini Skirt", "category": "Women", "subcategory": "Bottoms",
     "price": 195.00, "sizes": ["XS", "S", "M", "L"], "colors": ["Black", "Cognac", "Forest"],
     "rating": 4.5, "reviews": 67, "new": True, "sale": False,
     "emoji": "🩱", "description": "Real leather mini skirt with an A-line cut and zip back closure. A wardrobe investment that only gets better with time.", "tag": "New"},
    # Men
    {"id": 7, "name": "Japanese Selvedge Jeans", "category": "Men", "subcategory": "Bottoms",
     "price": 210.00, "sizes": ["28", "30", "32", "34", "36", "38"], "colors": ["Raw Indigo", "Washed Blue", "Black"],
     "rating": 4.9, "reviews": 445, "new": False, "sale": False,
     "emoji": "👖", "description": "14oz selvedge denim from Kojima, Japan. Slim tapered fit with a mid-rise. Built to last decades and develop a unique patina.", "tag": "Bestseller"},
    {"id": 8, "name": "Oxford Button-Down Shirt", "category": "Men", "subcategory": "Tops",
     "price": 120.00, "sizes": ["S", "M", "L", "XL", "XXL"], "colors": ["White", "Blue", "Pink", "Stripe"],
     "rating": 4.7, "reviews": 289, "new": False, "sale": False,
     "emoji": "👔", "description": "Classic Oxford cloth button-down with a slightly relaxed fit. The shirt that started it all — still the best.", "tag": "Classic"},
    {"id": 9, "name": "Italian Wool Overcoat", "category": "Men", "subcategory": "Outerwear",
     "price": 395.00, "original_price": 520.00, "sizes": ["S", "M", "L", "XL"], "colors": ["Camel", "Charcoal", "Navy"],
     "rating": 4.8, "reviews": 134, "new": False, "sale": True,
     "emoji": "🧥", "description": "Double-breasted overcoat in premium Italian wool-cashmere blend. A lifetime investment in understated elegance.", "tag": "On Sale"},
    {"id": 10, "name": "Relaxed Chino", "category": "Men", "subcategory": "Bottoms",
     "price": 135.00, "sizes": ["28", "30", "32", "34", "36"], "colors": ["Stone", "Navy", "Olive", "Tan"],
     "rating": 4.6, "reviews": 356, "new": False, "sale": False,
     "emoji": "👖", "description": "Garment-washed cotton chinos with a relaxed straight leg. Smart-casual perfection with uncompromising comfort.", "tag": "Everyday"},
    {"id": 11, "name": "Supima Tee 3-Pack", "category": "Men", "subcategory": "Tops",
     "price": 89.00, "sizes": ["S", "M", "L", "XL", "XXL"], "colors": ["White/Grey/Black"],
     "rating": 4.8, "reviews": 621, "new": False, "sale": False,
     "emoji": "👕", "description": "Three premium Supima cotton crew-neck tees. Heavier than average at 200gsm for a luxe drape that holds its shape.", "tag": "Value"},
    {"id": 12, "name": "Linen Resort Shirt", "category": "Men", "subcategory": "Tops",
     "price": 115.00, "sizes": ["S", "M", "L", "XL"], "colors": ["White", "Ecru", "Sky", "Terracotta"],
     "rating": 4.7, "reviews": 198, "new": True, "sale": False,
     "emoji": "👕", "description": "100% European linen camp-collar shirt. Wear it open over a tee or buttoned up with shorts. Breathable, rumpled, perfect.", "tag": "New"},
    # Accessories
    {"id": 13, "name": "Pebbled Leather Tote", "category": "Accessories", "subcategory": "Bags",
     "price": 245.00, "sizes": ["One Size"], "colors": ["Black", "Tan", "Burgundy"],
     "rating": 4.9, "reviews": 302, "new": False, "sale": False,
     "emoji": "👜", "description": "Full-grain pebbled leather tote with suede lining and interior pockets. Expands to carry everything without losing its shape.", "tag": "Icon"},
    {"id": 14, "name": "Wool Felt Fedora", "category": "Accessories", "subcategory": "Hats",
     "price": 95.00, "sizes": ["S/M", "L/XL"], "colors": ["Black", "Camel", "Charcoal"],
     "rating": 4.6, "reviews": 88, "new": True, "sale": False,
     "emoji": "🎩", "description": "Handcrafted Italian felt fedora with grosgrain ribbon band. The finishing touch your outfit didn't know it needed.", "tag": "New"},
    {"id": 15, "name": "Silk Scarf 90x90", "category": "Accessories", "subcategory": "Scarves",
     "price": 125.00, "original_price": 165.00, "sizes": ["One Size"], "colors": ["Floral", "Geometric", "Solid Navy"],
     "rating": 4.8, "reviews": 145, "new": False, "sale": True,
     "emoji": "🧣", "description": "Heavyweight twill silk square in exclusive prints. Wear it around your neck, tie it on your bag, or frame it as art.", "tag": "On Sale"},
    {"id": 16, "name": "Leather Chelsea Boots", "category": "Accessories", "subcategory": "Shoes",
     "price": 325.00, "sizes": ["36", "37", "38", "39", "40", "41", "42", "43", "44", "45"],
     "colors": ["Black", "Tan", "Chelsea Brown"],
     "rating": 4.9, "reviews": 267, "new": False, "sale": False,
     "emoji": "👢", "description": "Goodyear-welted Chelsea boots in full-grain leather. The last boots you'll ever buy — resoleable, eternal, impossibly chic.", "tag": "Bestseller"},
]

CATEGORIES = ["All", "Women", "Men", "Accessories"]
SUBCATEGORIES = {
    "Women": ["All", "Outerwear", "Tops", "Bottoms", "Dresses"],
    "Men": ["All", "Tops", "Bottoms", "Outerwear"],
    "Accessories": ["All", "Bags", "Hats", "Scarves", "Shoes"],
}

# ── Session state ──────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "page": "home",
        "cart": {},           # {product_id: {qty, size, color}}
        "wishlist": set(),
        "viewed_product": None,
        "toast": None,
        "filter_category": "All",
        "filter_sub": "All",
        "filter_sale": False,
        "search_query": "",
        "checkout_step": 1,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    # Defensive type checks — Streamlit Cloud can deserialize state incorrectly
    if not isinstance(st.session_state.cart, dict):
        st.session_state.cart = {}
    if not isinstance(st.session_state.wishlist, set):
        try:
            st.session_state.wishlist = set(st.session_state.wishlist)
        except Exception:
            st.session_state.wishlist = set()
    if not isinstance(st.session_state.page, str):
        st.session_state.page = "home"
    if not isinstance(st.session_state.filter_category, str):
        st.session_state.filter_category = "All"
    if not isinstance(st.session_state.filter_sub, str):
        st.session_state.filter_sub = "All"
    if not isinstance(st.session_state.search_query, str):
        st.session_state.search_query = ""

init_state()

# ── Helpers ────────────────────────────────────────────────────────────────────
def nav_to(page, product_id=None):
    st.session_state.page = page
    if product_id is not None:
        st.session_state.viewed_product = product_id
    st.rerun()

def add_to_cart(pid, size, color, qty=1):
    key = f"{pid}_{size}_{color}"
    if key in st.session_state.cart:
        st.session_state.cart[key]["qty"] += qty
    else:
        product = next(p for p in PRODUCTS if p["id"] == pid)
        st.session_state.cart[key] = {
            "product_id": pid,
            "name": product["name"],
            "price": product["price"],
            "size": size,
            "color": color,
            "qty": qty,
            "emoji": product["emoji"],
        }
    st.session_state.toast = f"✓  {next(p for p in PRODUCTS if p['id'] == pid)['name']} added to cart"

def cart_count():
    try:
        return sum(v["qty"] for v in st.session_state.cart.values() if isinstance(v, dict))
    except Exception:
        st.session_state.cart = {}
        return 0

def cart_total():
    try:
        return sum(v["price"] * v["qty"] for v in st.session_state.cart.values() if isinstance(v, dict))
    except Exception:
        st.session_state.cart = {}
        return 0

def star_display(rating):
    full = int(rating)
    half = 1 if rating - full >= 0.5 else 0
    empty = 5 - full - half
    return "★" * full + "⯨" * half + "☆" * empty

def get_filtered_products():
    products = PRODUCTS
    cat = st.session_state.filter_category
    sub = st.session_state.filter_sub
    sale = st.session_state.filter_sale
    q = st.session_state.search_query.lower().strip()

    if cat != "All":
        products = [p for p in products if p["category"] == cat]
    if sub != "All":
        products = [p for p in products if p["subcategory"] == sub]
    if sale:
        products = [p for p in products if p.get("sale")]
    if q:
        products = [p for p in products if q in p["name"].lower() or q in p["category"].lower()
                    or q in p["subcategory"].lower()]
    return products

# ── Components ─────────────────────────────────────────────────────────────────
def render_navbar():
    count = cart_count()
    badge = f'<span class="badge">{count}</span>' if count else ""
    st.markdown(f"""
    <div style="background:var(--charcoal);padding:0 2rem;display:flex;align-items:center;
                justify-content:space-between;height:64px;margin-bottom:0;
                font-family:'DM Sans',sans-serif;letter-spacing:0.05em;">
        <div style="font-family:'Playfair Display',serif;font-size:1.5rem;
                    color:var(--cream);font-weight:900;letter-spacing:0.04em;">
            SIEGE<span style="color:var(--accent);"> The Clothing Empire</span>
        </div>
        <div style="display:flex;gap:2rem;font-size:0.8rem;font-weight:500;text-transform:uppercase;color:#aaa;">
            <span>Est. 2025</span>
            <span>Free shipping over $200</span>
        </div>
        <div style="color:var(--accent-light);font-size:0.85rem;font-weight:500;">
            CART{badge}
        </div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns([1, 1, 1, 1, 1, 1, 2])
    nav_items = [("🏠 Home", "home"), ("👗 Shop", "shop"),
                 ("♡ Wishlist", "wishlist"), ("🛒 Cart", "cart"),
                 ("ℹ️ About", "about"), ("📞 Contact", "contact")]
    for i, (label, page) in enumerate(nav_items):
        with cols[i]:
            if st.button(label, key=f"nav_{page}"):
                nav_to(page)

    st.markdown("<hr style='margin:0;border-color:#333;'>", unsafe_allow_html=True)

def render_toast():
    if st.session_state.toast:
        st.markdown(f'<div class="toast">{st.session_state.toast}</div>', unsafe_allow_html=True)
        st.session_state.toast = None

def product_card(product, col_key=""):
    sale_badge = ""
    if product.get("sale") and product.get("original_price"):
        pct = int((1 - product["price"] / product["original_price"]) * 100)
        sale_badge = f'<span style="background:var(--red);color:white;padding:2px 8px;font-size:0.7rem;font-weight:700;">-{pct}%</span>'

    new_badge = ""
    if product.get("new"):
        new_badge = f'<span style="background:var(--accent);color:var(--charcoal);padding:2px 8px;font-size:0.7rem;font-weight:700;">NEW</span>'

    price_html = f'<span style="font-size:1.1rem;font-weight:600;color:var(--charcoal);">${product["price"]:.2f}</span>'
    if product.get("original_price"):
        price_html = f'<span style="font-size:1.1rem;font-weight:600;color:var(--red);">${product["price"]:.2f}</span> ' \
                     f'<span style="text-decoration:line-through;color:var(--warm-gray);font-size:0.9rem;">${product["original_price"]:.2f}</span>'

    wishlist_icon = "❤️" if product["id"] in st.session_state.wishlist else "🤍"

    st.markdown(f"""
    <div style="background:var(--card-bg);border:1px solid var(--border);
                padding:0;transition:box-shadow 0.2s;cursor:pointer;
                box-shadow:0 2px 8px rgba(0,0,0,0.04);">
        <div style="background:linear-gradient(135deg, #f0ebe0, #e8e0d0);
                    height:220px;display:flex;align-items:center;
                    justify-content:center;font-size:5rem;position:relative;">
            {product['emoji']}
            <div style="position:absolute;top:10px;left:10px;display:flex;gap:6px;">
                {sale_badge}{new_badge}
            </div>
            <div style="position:absolute;top:10px;right:10px;font-size:1.2rem;">{wishlist_icon}</div>
        </div>
        <div style="padding:1rem;">
            <div style="font-size:0.7rem;text-transform:uppercase;letter-spacing:0.1em;
                        color:var(--warm-gray);margin-bottom:4px;">{product['subcategory']}</div>
            <div style="font-family:'Playfair Display',serif;font-size:1rem;font-weight:700;
                        color:var(--charcoal);margin-bottom:6px;">{product['name']}</div>
            <div style="font-size:0.8rem;color:var(--accent);margin-bottom:8px;">
                {star_display(product['rating'])} <span style="color:var(--warm-gray);">({product['reviews']})</span>
            </div>
            <div style="margin-bottom:10px;">{price_html}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("View", key=f"view_{product['id']}_{col_key}"):
            nav_to("product", product["id"])
    with c2:
        if st.button("♡" if product["id"] not in st.session_state.wishlist else "❤", key=f"wish_{product['id']}_{col_key}"):
            if product["id"] in st.session_state.wishlist:
                st.session_state.wishlist.discard(product["id"])
            else:
                st.session_state.wishlist.add(product["id"])
            st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# PAGES
# ══════════════════════════════════════════════════════════════════════════════

def page_home():
    # Hero
    st.markdown("""
    <div style="background:linear-gradient(135deg, var(--charcoal) 0%, #2a2a20 60%, var(--charcoal) 100%);
                min-height:520px;display:flex;align-items:center;padding:4rem 5rem;
                position:relative;overflow:hidden;margin-bottom:3rem;">
        <div style="position:absolute;top:-60px;right:-60px;width:400px;height:400px;
                    border:1px solid rgba(196,151,59,0.2);border-radius:50%;"></div>
        <div style="position:absolute;top:20px;right:20px;width:300px;height:300px;
                    border:1px solid rgba(196,151,59,0.1);border-radius:50%;"></div>
        <div style="max-width:600px;z-index:1;">
            <div style="font-size:0.8rem;letter-spacing:0.25em;text-transform:uppercase;
                        color:var(--accent);margin-bottom:1.5rem;font-family:'DM Sans',sans-serif;">
                Spring 2026 Collection
            </div>
            <h1 style="font-family:'Playfair Display',serif;font-size:4rem;color:var(--cream);
                       line-height:1.05;margin:0 0 1.5rem;font-weight:900;">
                Made with Luxury<br><em style="color:var(--accent-light);">Luxuriate Your Life</em>
            </h1>
            <p style="color:#aaa;font-size:1.05rem;line-height:1.7;margin-bottom:2rem;
                      font-family:'DM Sans',sans-serif;max-width:440px;">
                Thoughtfully made clothing for people who care about craft, quality,
                and looking effortlessly good while going about their lives.
            </p>
        </div>
        <div style="position:absolute;right:8%;top:50%;transform:translateY(-50%);
                    font-size:10rem;opacity:0.15;">🧵</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🛍️  Shop Women", use_container_width=True):
            st.session_state.filter_category = "Women"
            st.session_state.filter_sub = "All"
            nav_to("shop")
    with c2:
        if st.button("👔  Shop Men", use_container_width=True):
            st.session_state.filter_category = "Men"
            st.session_state.filter_sub = "All"
            nav_to("shop")
    with c3:
        if st.button("👜  Accessories", use_container_width=True):
            st.session_state.filter_category = "Accessories"
            st.session_state.filter_sub = "All"
            nav_to("shop")

    st.markdown("<br>", unsafe_allow_html=True)

    # Stats bar
    st.markdown("""
    <div style="display:flex;justify-content:space-around;background:var(--charcoal);
                padding:1.5rem 2rem;margin:2rem 0;text-align:center;">
        <div>
            <div style="font-family:'Playfair Display',serif;font-size:2rem;color:var(--accent);">16</div>
            <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.1em;color:#aaa;">Pieces</div>
        </div>
        <div>
            <div style="font-family:'Playfair Display',serif;font-size:2rem;color:var(--accent);">4.8★</div>
            <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.1em;color:#aaa;">Avg Rating</div>
        </div>
        <div>
            <div style="font-family:'Playfair Display',serif;font-size:2rem;color:var(--accent);">Many</div>
            <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.1em;color:#aaa;">Reviews</div>
        </div>
        <div>
            <div style="font-family:'Playfair Display',serif;font-size:2rem;color:var(--accent);">Free</div>
            <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.1em;color:#aaa;">Returns</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Featured / New
    st.markdown("""
    <h2 style="font-family:'Playfair Display',serif;font-size:2rem;color:var(--charcoal);
               margin:2rem 0 1rem;text-align:center;">
        New Arrivals
    </h2>
    """, unsafe_allow_html=True)

    new_products = [p for p in PRODUCTS if p.get("new")][:4]
    cols = st.columns(4)
    for i, product in enumerate(new_products):
        with cols[i]:
            product_card(product, col_key=f"home_{i}")

    # Sale banner
    st.markdown("""
    <div style="background:var(--accent);padding:2rem;text-align:center;margin:3rem 0 2rem;">
        <div style="font-family:'Playfair Display',serif;font-size:1.8rem;color:var(--charcoal);font-weight:900;">
            Mid-Season Sale — Up to 30% Off
        </div>
        <div style="font-size:0.9rem;color:var(--charcoal);margin-top:0.5rem;opacity:0.8;">
            Selected styles · While stocks last
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Shop the Sale →", use_container_width=False):
        st.session_state.filter_sale = True
        st.session_state.filter_category = "All"
        nav_to("shop")

    # Bestsellers
    st.markdown("""
    <h2 style="font-family:'Playfair Display',serif;font-size:2rem;color:var(--charcoal);
               margin:2rem 0 1rem;text-align:center;">
        Bestsellers
    </h2>
    """, unsafe_allow_html=True)

    best = sorted(PRODUCTS, key=lambda x: x["reviews"], reverse=True)[:4]
    cols = st.columns(4)
    for i, product in enumerate(best):
        with cols[i]:
            product_card(product, col_key=f"best_{i}")

    # Features row
    st.markdown("""
    <div style="display:flex;gap:1px;margin:3rem 0 1rem;background:var(--border);">
        <div style="flex:1;background:var(--card-bg);padding:2rem;text-align:center;">
            <div style="font-size:2rem;margin-bottom:0.5rem;">🚚</div>
            <div style="font-family:'Playfair Display',serif;font-weight:700;color:var(--charcoal);margin-bottom:0.3rem;">Free Shipping</div>
            <div style="font-size:0.85rem;color:var(--warm-gray);">On orders over $200</div>
        </div>
        <div style="flex:1;background:var(--card-bg);padding:2rem;text-align:center;">
            <div style="font-size:2rem;margin-bottom:0.5rem;">↩️</div>
            <div style="font-family:'Playfair Display',serif;font-weight:700;color:var(--charcoal);margin-bottom:0.3rem;">Free Returns</div>
            <div style="font-size:0.85rem;color:var(--warm-gray);">30-day no-hassle policy</div>
        </div>
        <div style="flex:1;background:var(--card-bg);padding:2rem;text-align:center;">
            <div style="font-size:2rem;margin-bottom:0.5rem;">🏷️</div>
            <div style="font-family:'Playfair Display',serif;font-weight:700;color:var(--charcoal);margin-bottom:0.3rem;">Ethical Sourcing</div>
            <div style="font-size:0.85rem;color:var(--warm-gray);">Every piece, tracked</div>
        </div>
        <div style="flex:1;background:var(--card-bg);padding:2rem;text-align:center;">
            <div style="font-size:2rem;margin-bottom:0.5rem;">🎁</div>
            <div style="font-family:'Playfair Display',serif;font-weight:700;color:var(--charcoal);margin-bottom:0.3rem;">Gift Wrapping</div>
            <div style="font-size:0.85rem;color:var(--warm-gray);">Complimentary on request</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def page_shop():
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif;font-size:2.5rem;color:var(--charcoal);
               margin:1.5rem 0 0.5rem;">All Products</h1>
    """, unsafe_allow_html=True)

    # Filter bar
    fc1, fc2, fc3, fc4, fc5 = st.columns([2, 2, 2, 2, 2])
    with fc1:
        st.session_state.search_query = st.text_input("🔍 Search", value=st.session_state.search_query, label_visibility="collapsed", placeholder="Search products…")
    with fc2:
        cat = st.selectbox("Category", CATEGORIES, index=CATEGORIES.index(st.session_state.filter_category), label_visibility="collapsed")
        if cat != st.session_state.filter_category:
            st.session_state.filter_category = cat
            st.session_state.filter_sub = "All"
            st.rerun()
    with fc3:
        subs = ["All"] + (SUBCATEGORIES.get(st.session_state.filter_category, []))
        if st.session_state.filter_sub not in subs:
            st.session_state.filter_sub = "All"
        sub = st.selectbox("Subcategory", subs, index=subs.index(st.session_state.filter_sub), label_visibility="collapsed")
        st.session_state.filter_sub = sub
    with fc4:
        sale = st.checkbox("Sale only", value=st.session_state.filter_sale)
        st.session_state.filter_sale = sale
    with fc5:
        if st.button("Clear Filters"):
            st.session_state.filter_category = "All"
            st.session_state.filter_sub = "All"
            st.session_state.filter_sale = False
            st.session_state.search_query = ""
            st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    filtered = get_filtered_products()

    st.markdown(f"""
    <div style="font-size:0.85rem;color:var(--warm-gray);margin-bottom:1rem;">
        Showing <strong>{len(filtered)}</strong> products
    </div>
    """, unsafe_allow_html=True)

    if not filtered:
        st.markdown("""
        <div style="text-align:center;padding:4rem;color:var(--warm-gray);">
            <div style="font-size:3rem;margin-bottom:1rem;">🔍</div>
            <div style="font-family:'Playfair Display',serif;font-size:1.5rem;">No products found</div>
            <div style="margin-top:0.5rem;">Try adjusting your filters</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Grid
    cols_per_row = 4
    for i in range(0, len(filtered), cols_per_row):
        row_products = filtered[i:i + cols_per_row]
        cols = st.columns(cols_per_row)
        for j, product in enumerate(row_products):
            with cols[j]:
                product_card(product, col_key=f"shop_{i}_{j}")
        st.markdown("<br>", unsafe_allow_html=True)


def page_product():
    pid = st.session_state.viewed_product
    if pid is None:
        nav_to("shop")
        return

    product = next((p for p in PRODUCTS if p["id"] == pid), None)
    if not product:
        nav_to("shop")
        return

    if st.button("← Back to Shop"):
        nav_to("shop")

    st.markdown("<br>", unsafe_allow_html=True)

    img_col, info_col = st.columns([1, 1])

    with img_col:
        sale_tag = ""
        if product.get("sale") and product.get("original_price"):
            pct = int((1 - product["price"] / product["original_price"]) * 100)
            sale_tag = f'<div style="position:absolute;top:20px;left:20px;background:var(--red);color:white;padding:6px 14px;font-weight:700;font-size:0.85rem;">-{pct}%</div>'

        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#f0ebe0,#ddd6c8);height:500px;
                    display:flex;align-items:center;justify-content:center;
                    font-size:12rem;position:relative;border:1px solid var(--border);">
            {product['emoji']}
            {sale_tag}
        </div>
        """, unsafe_allow_html=True)

        # Thumbnails (decorative)
        t1, t2, t3, t4 = st.columns(4)
        for col, opacity in zip([t1, t2, t3, t4], [1, 0.6, 0.4, 0.3]):
            with col:
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,#f0ebe0,#ddd6c8);height:70px;
                            display:flex;align-items:center;justify-content:center;
                            font-size:2rem;cursor:pointer;border:1px solid var(--border);
                            opacity:{opacity};">{product['emoji']}</div>
                """, unsafe_allow_html=True)

    with info_col:
        wishlist_icon = "❤️ In Wishlist" if product["id"] in st.session_state.wishlist else "🤍 Add to Wishlist"

        price_html = f'<span style="font-size:2rem;font-weight:700;color:var(--charcoal);">${product["price"]:.2f}</span>'
        if product.get("original_price"):
            price_html = (f'<span style="font-size:2rem;font-weight:700;color:var(--red);">${product["price"]:.2f}</span> '
                          f'<span style="text-decoration:line-through;color:var(--warm-gray);font-size:1.2rem;">${product["original_price"]:.2f}</span>')

        st.markdown(f"""
        <div style="padding:1rem 0;">
            <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;
                        color:var(--accent);margin-bottom:0.5rem;">{product['category']} · {product['subcategory']}</div>
            <h1 style="font-family:'Playfair Display',serif;font-size:2.2rem;font-weight:900;
                       color:var(--charcoal);margin:0 0 0.5rem;">{product['name']}</h1>
            <div style="font-size:1rem;color:var(--accent);margin-bottom:1rem;">
                {star_display(product['rating'])}
                <span style="color:var(--warm-gray);font-size:0.9rem;"> {product['reviews']} reviews</span>
            </div>
            <div style="margin-bottom:1.5rem;">{price_html}</div>
            <p style="color:var(--warm-gray);line-height:1.8;font-size:0.95rem;margin-bottom:2rem;
                      border-left:3px solid var(--accent);padding-left:1rem;">
                {product['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Size selector
        st.markdown("**Size**")
        size_choice = st.selectbox("Size", product["sizes"], label_visibility="collapsed", key=f"size_{pid}")

        # Color selector
        st.markdown("**Colour**")
        color_choice = st.selectbox("Colour", product["colors"], label_visibility="collapsed", key=f"color_{pid}")

        # Qty
        st.markdown("**Quantity**")
        qty = st.number_input("Quantity", min_value=1, max_value=10, value=1, label_visibility="collapsed", key=f"qty_{pid}")

        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Add to Cart 🛒", use_container_width=True):
                add_to_cart(pid, size_choice, color_choice, qty)
                st.rerun()
        with c2:
            if st.button(wishlist_icon, use_container_width=True):
                if product["id"] in st.session_state.wishlist:
                    st.session_state.wishlist.discard(product["id"])
                else:
                    st.session_state.wishlist.add(product["id"])
                st.rerun()

        st.markdown("""
        <div style="margin-top:2rem;padding:1rem;background:var(--card-bg);border:1px solid var(--border);">
            <div style="font-size:0.8rem;color:var(--warm-gray);line-height:2;">
                🚚 &nbsp;Free shipping on orders over $200<br>
                ↩️ &nbsp;Free 30-day returns<br>
                🔒 &nbsp;Secure checkout<br>
                🌿 &nbsp;Sustainably sourced materials
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Related products
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"""
    <h2 style="font-family:'Playfair Display',serif;font-size:1.8rem;color:var(--charcoal);margin:1rem 0;">
        More from {product['category']}
    </h2>
    """, unsafe_allow_html=True)

    related = [p for p in PRODUCTS if p["category"] == product["category"] and p["id"] != pid][:4]
    cols = st.columns(4)
    for i, p in enumerate(related):
        with cols[i]:
            product_card(p, col_key=f"rel_{i}")


def page_cart():
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif;font-size:2.5rem;color:var(--charcoal);
               margin:1.5rem 0 1rem;">Your Cart</h1>
    """, unsafe_allow_html=True)

    if not st.session_state.cart:
        st.markdown("""
        <div style="text-align:center;padding:5rem;color:var(--warm-gray);">
            <div style="font-size:5rem;margin-bottom:1rem;">🛒</div>
            <div style="font-family:'Playfair Display',serif;font-size:1.8rem;color:var(--charcoal);margin-bottom:0.5rem;">Your cart is empty</div>
            <div>Start shopping to add items here</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Browse Products →"):
            nav_to("shop")
        return

    cart_col, summary_col = st.columns([3, 2])

    with cart_col:
        st.markdown("**Your Items**")
        for key, item in list(st.session_state.cart.items()):
            with st.container():
                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:1rem;padding:1rem;
                            background:var(--card-bg);border:1px solid var(--border);
                            margin-bottom:0.75rem;">
                    <div style="font-size:3rem;min-width:60px;text-align:center;">{item['emoji']}</div>
                    <div style="flex:1;">
                        <div style="font-family:'Playfair Display',serif;font-weight:700;
                                    color:var(--charcoal);">{item['name']}</div>
                        <div style="font-size:0.8rem;color:var(--warm-gray);margin-top:4px;">
                            Size: {item['size']} · Colour: {item['color']}
                        </div>
                        <div style="font-size:0.9rem;font-weight:600;color:var(--charcoal);margin-top:4px;">
                            ${item['price']:.2f} × {item['qty']} = ${item['price'] * item['qty']:.2f}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                c1, c2, c3 = st.columns([1, 1, 1])
                with c1:
                    if st.button("−", key=f"dec_{key}"):
                        if st.session_state.cart[key]["qty"] > 1:
                            st.session_state.cart[key]["qty"] -= 1
                        else:
                            del st.session_state.cart[key]
                        st.rerun()
                with c2:
                    if st.button("＋", key=f"inc_{key}"):
                        st.session_state.cart[key]["qty"] += 1
                        st.rerun()
                with c3:
                    if st.button("🗑 Remove", key=f"rem_{key}"):
                        del st.session_state.cart[key]
                        st.rerun()

    with summary_col:
        subtotal = cart_total()
        shipping = 0 if subtotal >= 200 else 9.95
        total = subtotal + shipping

        st.markdown(f"""
        <div style="background:var(--card-bg);border:1px solid var(--border);padding:1.5rem;
                    position:sticky;top:20px;">
            <h3 style="font-family:'Playfair Display',serif;color:var(--charcoal);margin:0 0 1rem;">
                Order Summary
            </h3>
            <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem;font-size:0.9rem;">
                <span style="color:var(--warm-gray);">Subtotal</span>
                <span style="font-weight:600;">${subtotal:.2f}</span>
            </div>
            <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem;font-size:0.9rem;">
                <span style="color:var(--warm-gray);">Shipping</span>
                <span style="font-weight:600;color:{'var(--accent)' if shipping == 0 else 'var(--charcoal)'}"">
                    {'Free' if shipping == 0 else f'${shipping:.2f}'}
                </span>
            </div>
            {'<div style="font-size:0.75rem;color:var(--accent);margin-bottom:0.75rem;">✓ You qualify for free shipping!</div>' if shipping == 0 else f'<div style="font-size:0.75rem;color:var(--warm-gray);margin-bottom:0.75rem;">Add ${200 - subtotal:.2f} more for free shipping</div>'}
            <hr style="border-color:var(--border);margin:0.75rem 0;">
            <div style="display:flex;justify-content:space-between;font-size:1.1rem;font-weight:700;
                        margin-bottom:1.5rem;">
                <span>Total</span>
                <span>${total:.2f}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Proceed to Checkout →", use_container_width=True):
            st.session_state.checkout_step = 1
            nav_to("checkout")

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Continue Shopping", use_container_width=True):
            nav_to("shop")


def page_checkout():
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif;font-size:2.5rem;color:var(--charcoal);
               margin:1.5rem 0 1rem;">Checkout</h1>
    """, unsafe_allow_html=True)

    # Step indicator
    step = st.session_state.checkout_step
    steps = ["Shipping", "Payment", "Review"]
    step_html = '<div style="display:flex;gap:0;margin-bottom:2rem;">'
    for i, s in enumerate(steps, 1):
        active = i == step
        done = i < step
        bg = "var(--charcoal)" if active else ("var(--accent)" if done else "#ddd")
        color = "var(--cream)" if (active or done) else "#999"
        step_html += f'<div style="flex:1;text-align:center;padding:0.75rem;background:{bg};color:{color};font-size:0.85rem;font-weight:600;letter-spacing:0.05em;text-transform:uppercase;">{"✓ " if done else f"{i}. "}{s}</div>'
    step_html += '</div>'
    st.markdown(step_html, unsafe_allow_html=True)

    form_col, summary_col = st.columns([3, 2])

    with form_col:
        if step == 1:
            st.markdown("#### Shipping Details")
            c1, c2 = st.columns(2)
            with c1:
                st.text_input("First Name", key="first_name")
            with c2:
                st.text_input("Last Name", key="last_name")
            st.text_input("Email", key="email")
            st.text_input("Address Line 1", key="addr1")
            st.text_input("Address Line 2 (optional)", key="addr2")
            c3, c4 = st.columns(2)
            with c3:
                st.text_input("City", key="city")
            with c4:
                st.text_input("Postcode", key="postcode")
            st.selectbox("Country", ["United Kingdom", "United States", "Australia", "Canada", "France", "Germany", "Ireland"], key="country")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Continue to Payment →", use_container_width=True):
                st.session_state.checkout_step = 2
                st.rerun()

        elif step == 2:
            st.markdown("#### Payment Details")
            st.text_input("Cardholder Name", key="card_name")
            st.text_input("Card Number", placeholder="**** **** **** ****", key="card_number")
            c1, c2 = st.columns(2)
            with c1:
                st.text_input("Expiry (MM/YY)", key="card_exp")
            with c2:
                st.text_input("CVV", type="password", key="card_cvv")

            st.markdown("""
            <div style="display:flex;gap:1rem;margin-top:0.5rem;align-items:center;">
                <div style="font-size:0.75rem;color:var(--warm-gray);">🔒 Secured with 256-bit encryption</div>
            </div>
            """, unsafe_allow_html=True)

            st.text_input("Discount Code", placeholder="Enter promo code", key="promo")
            st.markdown("<br>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                if st.button("← Back", use_container_width=True):
                    st.session_state.checkout_step = 1
                    st.rerun()
            with c2:
                if st.button("Review Order →", use_container_width=True):
                    st.session_state.checkout_step = 3
                    st.rerun()

        elif step == 3:
            st.markdown("#### Review Your Order")
            for key, item in st.session_state.cart.items():
                st.markdown(f"""
                <div style="display:flex;justify-content:space-between;padding:0.5rem 0;
                            border-bottom:1px solid var(--border);font-size:0.9rem;">
                    <span>{item['emoji']} {item['name']} ({item['size']}, {item['color']}) × {item['qty']}</span>
                    <span style="font-weight:600;">${item['price'] * item['qty']:.2f}</span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                if st.button("← Edit Payment", use_container_width=True):
                    st.session_state.checkout_step = 2
                    st.rerun()
            with c2:
                if st.button("✓ Place Order", use_container_width=True):
                    st.session_state.cart = {}
                    nav_to("confirmation")

    with summary_col:
        subtotal = cart_total()
        shipping = 0 if subtotal >= 200 else 9.95
        total = subtotal + shipping
        st.markdown(f"""
        <div style="background:var(--card-bg);border:1px solid var(--border);padding:1.5rem;position:sticky;top:20px;">
            <h3 style="font-family:'Playfair Display',serif;color:var(--charcoal);margin:0 0 1rem;">Order Summary</h3>
            <div style="display:flex;justify-content:space-between;margin-bottom:0.4rem;font-size:0.88rem;">
                <span style="color:var(--warm-gray);">Subtotal</span><span>${subtotal:.2f}</span>
            </div>
            <div style="display:flex;justify-content:space-between;margin-bottom:0.4rem;font-size:0.88rem;">
                <span style="color:var(--warm-gray);">Shipping</span>
                <span>{'Free' if shipping == 0 else f'${shipping:.2f}'}</span>
            </div>
            <hr style="border-color:var(--border);margin:0.75rem 0;">
            <div style="display:flex;justify-content:space-between;font-size:1.1rem;font-weight:700;">
                <span>Total</span><span>${total:.2f}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


def page_confirmation():
    st.markdown("""
    <div style="text-align:center;padding:4rem 2rem;">
        <div style="font-size:5rem;margin-bottom:1rem;">🎉</div>
        <h1 style="font-family:'Playfair Display',serif;font-size:2.5rem;color:var(--charcoal);margin-bottom:0.5rem;">
            Order Confirmed!
        </h1>
        <p style="color:var(--warm-gray);font-size:1.05rem;max-width:500px;margin:0 auto 1rem;line-height:1.7;">
            Thank you for your order. You'll receive a confirmation email shortly.
            Your items will be dispatched within 2 business days.
        </p>
        <div style="background:var(--card-bg);border:1px solid var(--border);
                    padding:1.5rem;max-width:380px;margin:2rem auto;text-align:left;">
            <div style="font-size:0.8rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--warm-gray);">Order reference</div>
            <div style="font-family:'Playfair Display',serif;font-size:1.5rem;color:var(--charcoal);font-weight:700;">
                VT-2025-88421
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("← Continue Shopping"):
        nav_to("home")


def page_wishlist():
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif;font-size:2.5rem;color:var(--charcoal);
               margin:1.5rem 0 1rem;">Wishlist</h1>
    """, unsafe_allow_html=True)

    wish_products = [p for p in PRODUCTS if p["id"] in st.session_state.wishlist]

    if not wish_products:
        st.markdown("""
        <div style="text-align:center;padding:5rem;color:var(--warm-gray);">
            <div style="font-size:5rem;margin-bottom:1rem;">🤍</div>
            <div style="font-family:'Playfair Display',serif;font-size:1.8rem;color:var(--charcoal);margin-bottom:0.5rem;">Your wishlist is empty</div>
            <div>Tap the heart icon on any product to save it here</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Browse Products"):
            nav_to("shop")
        return

    cols = st.columns(4)
    for i, p in enumerate(wish_products):
        with cols[i % 4]:
            product_card(p, col_key=f"wish_{i}")


def page_about():
    st.markdown("""
    <div style="max-width:800px;margin:2rem auto;">
        <h1 style="font-family:'Playfair Display',serif;font-size:3rem;color:var(--charcoal);
                   text-align:center;margin-bottom:0.5rem;">Our Story</h1>
        <div style="text-align:center;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.2em;
                    color:var(--accent);margin-bottom:3rem;">Est. 2019 · London</div>

        <div style="background:var(--card-bg);border:1px solid var(--border);padding:3rem;margin-bottom:2rem;">
            <p style="font-size:1.1rem;line-height:1.9;color:var(--charcoal);margin:0;">
                SIEGE: The Clothing Empire began with a simple conviction: beautiful clothes shouldn't cost the earth —
                financially or ecologically. Founded in East London in 2019 by two former fashion industry
                insiders, we set out to prove that quality, sustainability, and accessible pricing could coexist
                in a single wardrobe.
            </p>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--border);margin-bottom:2rem;">
            <div style="background:var(--card-bg);padding:2rem;">
                <div style="font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:700;
                            color:var(--charcoal);margin-bottom:0.75rem;">🌿 Sustainably Sourced</div>
                <p style="color:var(--warm-gray);line-height:1.7;font-size:0.9rem;">
                    Every fibre is traced. We partner with certified mills in Portugal, Japan, and Scotland
                    who share our commitment to responsible production.
                </p>
            </div>
            <div style="background:var(--card-bg);padding:2rem;">
                <div style="font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:700;
                            color:var(--charcoal);margin-bottom:0.75rem;">✂️ Considered Design</div>
                <p style="color:var(--warm-gray);line-height:1.7;font-size:0.9rem;">
                    We create pieces intended to last years, not seasons. Classic shapes with thoughtful
                    details that feel fresh but never trend-chasing.
                </p>
            </div>
            <div style="background:var(--card-bg);padding:2rem;">
                <div style="font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:700;
                            color:var(--charcoal);margin-bottom:0.75rem;">🤝 Fair Pay</div>
                <p style="color:var(--warm-gray);line-height:1.7;font-size:0.9rem;">
                    Every person who makes our clothes is paid fairly. We audit our supply chain twice
                    yearly and publish the results openly.
                </p>
            </div>
            <div style="background:var(--card-bg);padding:2rem;">
                <div style="font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:700;
                            color:var(--charcoal);margin-bottom:0.75rem;">📦 Plastic-Free Packaging</div>
                <p style="color:var(--warm-gray);line-height:1.7;font-size:0.9rem;">
                    Every order ships in recycled paper packaging with soy-based inks. Our garment
                    bags are made from organic cotton.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def page_contact():
    st.markdown("""
    <h1 style="font-family:'Playfair Display',serif;font-size:2.5rem;color:var(--charcoal);
               margin:1.5rem 0 0.5rem;text-align:center;">Get in Touch</h1>
    <p style="text-align:center;color:var(--warm-gray);margin-bottom:2rem;">
        We'd love to hear from you. Usually reply within one business day.
    </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        subject = st.selectbox("Subject", ["General Enquiry", "Order Help", "Returns & Exchanges",
                                            "Sizing Advice", "Wholesale", "Press"])
        message = st.text_area("Message", height=150)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Send Message →", use_container_width=True):
            if name and email and message:
                st.success("✓ Message sent! We'll be in touch within one business day.")
            else:
                st.error("Please fill in all required fields.")

        st.markdown("""
        <div style="margin-top:2rem;padding:1.5rem;background:var(--card-bg);border:1px solid var(--border);">
            <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;
                        color:var(--charcoal);margin-bottom:1rem;">Other Ways to Reach Us</div>
            <div style="font-size:0.9rem;color:var(--warm-gray);line-height:2.2;">
                📧 &nbsp;hello@SIEGE: The Clothing Empire.co.uk<br>
                📞 &nbsp;+44 20 1234 5678 (Mon–Fri, 9–5 GMT)<br>
                📍 &nbsp;14 Curtain Road, London EC2A 3AT<br>
                🐦 &nbsp;@SIEGE: The Clothing Empire
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
def render_footer():
    st.markdown("""
    <div style="background:var(--charcoal);padding:3rem 4rem 2rem;margin-top:4rem;">
        <div style="display:flex;gap:4rem;margin-bottom:2rem;flex-wrap:wrap;">
            <div>
                <div style="font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:900;
                            color:var(--cream);margin-bottom:1rem;">VOGUE<span style="color:var(--accent);">THREAD</span></div>
                <div style="font-size:0.85rem;color:#666;max-width:220px;line-height:1.7;">
                    Thoughtfully made clothing.<br>Responsibly sourced. London-based.
                </div>
            </div>
            <div>
                <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;
                            color:var(--accent);margin-bottom:1rem;">Shop</div>
                <div style="font-size:0.85rem;color:#888;line-height:2.2;">
                    Women<br>Men<br>Accessories<br>Sale
                </div>
            </div>
            <div>
                <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;
                            color:var(--accent);margin-bottom:1rem;">Help</div>
                <div style="font-size:0.85rem;color:#888;line-height:2.2;">
                    Size Guide<br>Returns<br>Shipping Info<br>Contact
                </div>
            </div>
            <div>
                <div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:0.15em;
                            color:var(--accent);margin-bottom:1rem;">Company</div>
                <div style="font-size:0.85rem;color:#888;line-height:2.2;">
                    About Us<br>Sustainability<br>Careers<br>Press
                </div>
            </div>
        </div>
        <hr style="border-color:#333;margin:1.5rem 0;">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;">
            <div style="font-size:0.75rem;color:#555;">© 2025 SIEGE: The Clothing Empire. All rights reserved.</div>
            <div style="font-size:0.75rem;color:#555;">Privacy Policy · Terms of Service · Cookie Policy</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Main router ────────────────────────────────────────────────────────────────
render_navbar()
render_toast()

page = st.session_state.page
if page == "home":
    page_home()
elif page == "shop":
    page_shop()
elif page == "product":
    page_product()
elif page == "cart":
    page_cart()
elif page == "checkout":
    page_checkout()
elif page == "confirmation":
    page_confirmation()
elif page == "wishlist":
    page_wishlist()
elif page == "about":
    page_about()
elif page == "contact":
    page_contact()
else:
    page_home()

render_footer()
