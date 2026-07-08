import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')
fig.patch.set_facecolor('#f8f9fa')

# ── TITLE ──
ax.text(8, 9.6, 'Sequence Diagram — Multi-Agent AI Academic Assistant',
        ha='center', va='center', fontsize=13, fontweight='bold', color='#1a1a2e')

# ── ACTORS ──
actors = [
    (2.0,  '#4e89ae', 'User'),
    (6.0,  '#2d6a4f', 'Frontend'),
    (10.0, '#b5451b', 'Flask Backend'),
    (14.0, '#6a0572', 'Groq AI'),
]

for (x, color, label) in actors:
    rect = plt.Rectangle((x-1.2, 8.6), 2.4, 0.7,
                          facecolor=color, edgecolor='white', linewidth=2, zorder=3)
    ax.add_patch(rect)
    ax.text(x, 8.95, label, ha='center', va='center',
            fontsize=9, fontweight='bold', color='white', zorder=4)
    ax.plot([x, x], [8.6, 0.3], color='#bbbbbb', linewidth=1.0, linestyle='--', zorder=1)

# ── HELPER FUNCTIONS ──
def forward_arrow(ax, y, x1, x2, label, color):
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', color=color, lw=2.0))
    mid_x = (x1 + x2) / 2
    ax.text(mid_x, y+0.18, label, ha='center', va='bottom', fontsize=8, color='#222222',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor=color, linewidth=1))

def return_arrow(ax, y, x1, x2, label, color):
    # Draw dashed line manually
    ax.plot([x1, x2], [y, y], color=color, linewidth=1.8, linestyle='dashed')
    ax.annotate('', xy=(x2, y), xytext=(x1+0.1, y),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.8))
    mid_x = (x1 + x2) / 2
    ax.text(mid_x, y+0.18, label, ha='center', va='bottom', fontsize=8, color='#222222',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#f0f8ff', edgecolor=color, linewidth=1))

def self_arrow(ax, y, x, label, color):
    # Draw a neat rectangular self-loop
    ax.annotate('', xy=(x+0.8, y-0.15), xytext=(x, y),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.8,
                                connectionstyle='arc3,rad=-0.4'))
    ax.text(x+1.5, y-0.12, label, va='center', fontsize=8, color='#222222',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#fff9e6', edgecolor=color, linewidth=1))

# ── STEP NUMBER ──
def step_num(ax, y, num):
    ax.text(0.4, y, str(num), ha='center', va='center', fontsize=8,
            fontweight='bold', color='white',
            bbox=dict(boxstyle='circle,pad=0.3', facecolor='#1a1a2e', edgecolor='white'))

# ── DRAW STEPS ──
step_num(ax, 8.1, 1)
forward_arrow(ax, 8.1, 2.0, 6.0, 'Type question & click Send', '#4e89ae')

step_num(ax, 7.2, 2)
forward_arrow(ax, 7.2, 6.0, 10.0, 'POST /api/chat  { message, user_id }', '#2d6a4f')

step_num(ax, 6.3, 3)
self_arrow(ax, 6.3, 10.0, 'Validate request & check errors', '#b5451b')

step_num(ax, 5.4, 4)
forward_arrow(ax, 5.4, 10.0, 14.0, 'Send prompt + conversation history', '#b5451b')

step_num(ax, 4.5, 5)
self_arrow(ax, 4.5, 14.0, 'Generate AI response (LLaMA 3)', '#6a0572')

step_num(ax, 3.6, 6)
return_arrow(ax, 3.6, 14.0, 10.0, 'Return AI response text', '#6a0572')

step_num(ax, 2.7, 7)
self_arrow(ax, 2.7, 10.0, 'Save message + response to history', '#b5451b')

step_num(ax, 1.8, 8)
return_arrow(ax, 1.8, 10.0, 6.0, 'JSON { status: success, response }', '#b5451b')

step_num(ax, 0.9, 9)
return_arrow(ax, 0.9, 6.0, 2.0, 'Display formatted response in chat', '#2d6a4f')

# ── LEGEND ──
legend_items = [
    mpatches.Patch(color='#4e89ae', label='User action'),
    mpatches.Patch(color='#2d6a4f', label='Frontend (HTML/JS)'),
    mpatches.Patch(color='#b5451b', label='Flask Backend'),
    mpatches.Patch(color='#6a0572', label='Groq AI (LLaMA 3)'),
]
ax.legend(handles=legend_items, loc='lower right', fontsize=8.5,
          framealpha=0.95, edgecolor='#cccccc')

plt.tight_layout()
plt.savefig('reports/sequence_diagram.png', dpi=150,
            bbox_inches='tight', facecolor='#f8f9fa')
print("Saved to reports/sequence_diagram.png")
plt.show()