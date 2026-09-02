# Finsight v1 — Design Direction

## Three possible directions

### Theme Name: Signal Ledger
Very Brief Intro: A warm editorial data journal that treats every chart as evidence and every caveat as part of the story. It feels like a careful analyst's notebook translated into a modern product.
Probability: 0.07

### Theme Name: Monsoon Console
Very Brief Intro: A dark, high-contrast operations room for reading UPI movement at a glance. Saturated amber and electric blue act as controlled signals against a quiet graphite field.
Probability: 0.03

### Theme Name: Archive of Motion
Very Brief Intro: A restrained museum-like interface with generous paper-colored space, ink typography, and softly framed data objects. The mood is considered, human, and unusually transparent for a finance dashboard.
Probability: 0.08

## Chosen approach: Signal Ledger

### Design Movement
Contemporary editorial information design, borrowing from financial newspapers, Swiss typographic systems, and well-made research notebooks rather than generic SaaS dashboards.

### Core Principles
1. **Evidence has a visible address.** Every important number carries a source, date range, and definition close to where it appears.
2. **Hierarchy over decoration.** The interface uses typography, rules, and scale to guide attention; color is reserved for meaning.
3. **The caveat is part of the product.** Missing months, model error, and assumptions are not hidden in a footer.
4. **Human analyst, not black box.** Copy stays plainspoken and specific, with enough context for a first-time learner to explain the work aloud.

### Color Philosophy
The foundation is warm parchment and deep ink to evoke an annotated research dossier. A single ownable signal color, **Kumquat Orange (#E66D3F)**, marks movement, warnings, and projection without pretending that uncertainty is certainty. A muted river blue supports observed history; moss marks verified checks. The palette is intentionally low-saturation outside the signal color so the data—not gradients—does the convincing.

### Layout Paradigm
Use an asymmetric reading rail: a narrow left navigation spine, a wide evidence canvas, and occasional right-side margin notes. The top of the dashboard opens with a thesis strip rather than a centered hero. Charts sit in editorial modules with uneven but deliberate spans, alternating full-width trends and compact evidence cards.

### Signature Elements
1. A small **source docket** under every major insight, using monospaced metadata for provenance.
2. **Evidence bands**—thin horizontal rules and orange markers that call out the exact window or caveat in view.
3. **Margin notes** for “what this means” and “what this does not mean,” visually distinct from measured results.

### Interaction Philosophy
Interactions should feel like turning pages in a working analyst's notebook: filters update quickly and visibly, hover states reveal definitions rather than spectacle, and expandable notes explain methodology without leaving the dashboard. Every control has a direct consequence and no control is decorative.

### Animation
Use 180–240ms ease-out transitions for tabs, tooltips, and chart focus. Stagger first-load modules by 40ms only when motion is enabled. Chart lines draw in once on entry; subsequent filter changes cross-fade or interpolate rather than replaying a theatrical entrance. Respect reduced-motion preferences and never animate numbers in a way that could imply precision beyond the source.

### Typography System
Use **DM Serif Display** for thesis headlines and major section titles, paired with **IBM Plex Sans** for interface text and **IBM Plex Mono** for dates, source labels, and model metrics. Headlines should be sentence case, compact, and slightly editorial. Body text stays at 15–16px with 1.55 line-height. Metadata is 11–12px uppercase or monospace with generous tracking.

### Brand Essence
Finsight is an evidence-first UPI growth readout for students, product strategists, and curious builders who want a defensible answer—not a dashboard full of vibes. Personality: **observant, candid, quietly ambitious**.

### Brand Voice
Headlines are direct and thesis-shaped. CTAs sound like invitations to inspect, not sales pitches. Microcopy names uncertainty plainly and avoids generic filler.

Example lines:
- “UPI is still growing. The distribution is the story.”
- “Open the caveat before you quote the projection.”

### Wordmark & Logo
The mark is a compact ledger glyph: two offset vertical bars joined by a short diagonal bridge, suggesting both an “F” and a trend line. The wordmark uses DM Serif Display with a custom clipped crossbar on the F; the icon stands alone in headers and favicon contexts.

### Signature Brand Color
**Kumquat Orange — #E66D3F.** It is warm enough to feel human and sharp enough to behave like a signal, reserved for attention-worthy movement and honest warnings.

## Style Decisions

- Keep the dashboard light-first with a warm paper background; do not default to a dark neon treatment.
- Prefer evidence labels, footnotes, and direct definitions over decorative cards.
- Use “Sundaram Dubey” as the project owner/maintainer where the repository currently says TBD.
- Keep the public demo static and self-contained; do not add a backend, account system, or new analytical model.
