import os

css_path = 'assets/sass/style.css'
if not os.path.exists(css_path):
    print(f"Error: {css_path} not found.")
    exit(1)

with open(css_path, 'r', encoding='utf-8') as f:
    original_css = f.read()

# Filter out old modernization blocks if they exist to prevent duplication
if "/* --- PREMIUM MODERNIZATION OVERRIDES --- */" in original_css:
    # Just a simple check for now, can be sophisticated later
    pass

premium_styles = """
/* --- PREMIUM MODERNIZATION OVERRIDES --- */
:root {
    --primary-maroon: #8b0000;
    --dark-maroon: #1a0808;
    --premium-gold: #FBAD17;
    --heading-font: 'Plus Jakarta Sans', sans-serif;
    --body-font: 'Inter', sans-serif;
    --shadow-soft: 0 10px 30px rgba(0,0,0,0.08);
    --shadow-premium: 0 20px 50px rgba(0,0,0,0.12);
    --glass-bg: rgba(255, 255, 255, 0.85);
    --glass-border: rgba(255, 255, 255, 0.2);
}

body {
    font-family: var(--body-font) !important;
    color: #333;
    line-height: 1.7;
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--heading-font) !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em !important;
}

.theme-btn {
    border-radius: 50px !important;
    font-family: var(--heading-font);
    font-weight: 600;
    text-transform: capitalize;
    letter-spacing: 0.5px;
    padding: 12px 35px !important;
    box-shadow: 0 10px 20px rgba(139, 0, 0, 0.2);
    transition: all 0.4s ease !important;
}

.theme-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 30px rgba(139, 0, 0, 0.3);
}

/* Premium Header Modernization */
.topbar {
    background: linear-gradient(135deg, var(--dark-maroon), #2e1818) !important;
    border-bottom: 2px solid var(--premium-gold);
}

.wpo-site-header {
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    box-shadow: var(--shadow-soft);
}

.navigation .navbar-nav > li > a {
    font-family: var(--heading-font);
    font-weight: 600;
    font-size: 15px;
}

/* Premium Card Refinements */
.service-card, .member-card, .member-card-premium {
    border-radius: 20px !important;
    overflow: hidden;
    border: 1px solid #eee !important;
    box-shadow: var(--shadow-soft);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
}

.service-card:hover, .member-card:hover, .member-card-premium:hover {
    transform: translateY(-10px);
    box-shadow: var(--shadow-premium);
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(premium_styles + '\n' + original_css)

print("Success: style.css updated with premium tokens.")
