import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(1, 1, figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#f8f9fa')

ax.text(7, 8.5, 'Multi-Agent AI System for Academic Assistance',
        ha='center', va='center', fontsize=15, fontweight='bold', color='#1a1a2e')

# --- Boxes ---
boxes = [
    (1.0, 6.0, 2.8, 1.6, '#4e89ae', 'CLIENT LAYER\n(Frontend)',
     'React / HTML\nUser Interface\nChat Window'),
    (5.0, 6.0, 2.8, 1.6, '#2d6a4f', 'SERVER LAYER\n(Flask Backend)',
     'Flask API\nRoutes & Middleware\nRequest Handling'),
    (9.0, 6.0, 2.8, 1.6, '#6a0572', 'AI MODEL LAYER\n(AI Agents)',
     'Claude / GPT API\nMulti-Agent Logic\nResponse Generation'),
    (3.0, 3.0, 2.8, 1.6, '#b5451b', 'DATABASE LAYER\n(Storage)',
     'Chat History\nUser Data\nFeedback Store'),
    (7.0, 3.0, 2.8, 1.6, '#1a1a2e', 'DATA LAYER\n(Academic Data)',
     'Cleaned Datasets\nCSV / Excel Files\nPre-processed Data'),
]

for (x, y, w, h, color, title, desc) in boxes:
    fancy = FancyBboxPatch((x, y), w, h,
                           boxstyle="round,pad=0.1",
                           facecolor=color, edgecolor='white',
                           linewidth=2, zorder=2)
    ax.add_patch(fancy)
    ax.text(x + w/2, y + h - 0.35, title,
            ha='center', va='center', fontsize=8.5,
            fontweight='bold', color='white', zorder=3)
    ax.text(x + w/2, y + 0.55, desc,
            ha='center', va='center', fontsize=7.2,
            color='#e0e0e0', zorder=3, linespacing=1.4)

# --- Arrows ---
arrows = [
    (3.8, 6.8, 5.0, 6.8),   # Client -> Server
    (7.8, 6.8, 9.0, 6.8),   # Server -> AI
    (6.4, 6.0, 5.5, 4.6),   # Server -> Database
    (6.4, 6.0, 7.5, 4.6),   # Server -> Data Layer
]

for (x1, y1, x2, y2) in arrows:
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#333333',
                                lw=2.0), zorder=4)

# --- API Labels on arrows ---
ax.text(4.4, 7.05, 'HTTP\nRequests', ha='center', fontsize=7, color='#333')
ax.text(8.4, 7.05, 'API\nCalls', ha='center', fontsize=7, color='#333')

# --- API Endpoints box ---
ep_box = FancyBboxPatch((0.3, 0.5), 4.5, 2.0,
                        boxstyle="round,pad=0.1",
                        facecolor='#f0a500', edgecolor='white',
                        linewidth=2, zorder=2)
ax.add_patch(ep_box)
ax.text(2.55, 2.25, 'API ENDPOINTS', ha='center', fontsize=9,
        fontweight='bold', color='white', zorder=3)
endpoints = [
    'POST  /api/chat       → Send prompt to AI',
    'GET   /api/history    → Retrieve conversations',
    'GET   /api/users      → Fetch user info',
    'POST  /api/feedback   → Store ratings',
    'GET   /api/health     → Health check',
]
for i, ep in enumerate(endpoints):
    ax.text(0.55, 2.0 - i*0.28, ep, fontsize=6.8,
            color='#1a1a2e', zorder=3, fontfamily='monospace')

plt.tight_layout()
plt.savefig('reports/architecture_diagram.png', dpi=150,
            bbox_inches='tight', facecolor='#f8f9fa')
print("Saved to reports/architecture_diagram.png")
plt.show()