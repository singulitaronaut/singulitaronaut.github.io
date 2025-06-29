---
title: Monospace Design System Showcase
description: A comprehensive demonstration of the utility classes and components available in our monospace web design system
date: 2024-01-12
author: Blog Author
tags: [design, monospace, css, typography]
---

# Monospace Design System Showcase

This post demonstrates the various utility classes and components available in our monospace web design system. Everything aligns to a strict typographic grid for perfect readability.

## Grid System

The `.grid` class creates a flexible layout system that automatically calculates column widths:

<div class="grid">
  <p class="width-auto">This paragraph takes up most of the available space using <code>width-auto</code></p>
  <p class="width-min">Minimal space with <code>width-min</code></p>
</div>

<div class="grid">
  <p>Equal</p>
  <p>Width</p>
  <p>Columns</p>
</div>

<div class="grid">
  <button>Button 1</button>
  <button>Button 2</button>
  <button>Button 3</button>
  <button>Button 4</button>
</div>

## Tree Structure

Perfect for showing hierarchical information with connecting lines:

<div class="tree">
  <ul>
    <li>Root Level
      <ul>
        <li>Child Item 1</li>
        <li>Child Item 2
          <ul>
            <li>Grandchild A</li>
            <li>Grandchild B</li>
          </ul>
        </li>
        <li>Child Item 3</li>
      </ul>
    </li>
    <li>Another Root Item
      <ul>
        <li>Different Child</li>
      </ul>
    </li>
  </ul>
</div>

## Tables

Tables are styled with clean borders and proper grid alignment:

| Feature | Description | Status |
|---------|-------------|--------|
| Grid System | Flexible layout | ✓ Complete |
| Typography | Baseline grid | ✓ Complete |
| Dark Mode | Auto-switching | ✓ Complete |
| Debug Tools | Grid overlay | ✓ Complete |

## Interactive Elements

### Collapsible Details

<details>
  <summary>Design Philosophy</summary>
  <p>The monospace web approach prioritizes:</p>
  <ul>
    <li>Consistent spacing and alignment</li>
    <li>Readable typography at all sizes</li>
    <li>Functional minimalism</li>
    <li>Grid-based layouts</li>
  </ul>
</details>

<details>
  <summary>Technical Implementation</summary>
  <p>Built with modern CSS features:</p>
  <ul>
    <li>CSS Custom Properties (variables)</li>
    <li>CSS Grid and Flexbox</li>
    <li>Container queries</li>
    <li>Logical properties</li>
  </ul>
</details>

### Form Elements

<div class="grid">
  <label class="width-auto">
    Enter your name:
    <input type="text" placeholder="Your name here">
  </label>
  <label class="width-min">
    <input type="checkbox"> Subscribe
  </label>
</div>

<div class="grid">
  <button>Primary Action</button>
  <button>Secondary</button>
</div>

## Typography Examples

### Headings

# Heading Level 1 (Uppercase)
## Heading Level 2 (Uppercase)
### Heading Level 3
#### Heading Level 4

### Text Formatting

This paragraph demonstrates **bold text**, *italic text*, and `inline code`. You can also use <sub>subscript</sub> for mathematical notation.

> This is a blockquote that maintains proper grid alignment and provides visual emphasis for quoted content.

### Lists

Ordered lists use automatic numbering:

1. First item
2. Second item
    1. Nested item
    2. Another nested item
3. Third item

Unordered lists use square bullets:

- First point
- Second point
    - Nested point
    - Another nested point
- Third point

## Code Blocks

```python
def calculate_grid():
    """Calculate grid dimensions for perfect alignment."""
    line_height = "1.20rem"
    char_width = "1ch"
    
    return {
        "vertical_rhythm": line_height,
        "horizontal_unit": char_width
    }

# Everything aligns to this grid
grid = calculate_grid()
print(f"Line height: {grid['vertical_rhythm']}")
```

```css
/* CSS custom properties for the design system */
:root {
  --line-height: 1.20rem;
  --font-family: "JetBrains Mono", monospace;
  --border-thickness: 2px;
}

.grid {
  display: flex;
  gap: 1ch;
  margin-bottom: var(--line-height);
}
```

## Whitespace

Need to keep every space in place? Wrap your text content in a `<pre>` element. This tag preserves all whitespace—ideal for ASCII art, log excerpts, or command-line output. Because the design system already uses a monospace font, the characters inside `<pre>` line up perfectly with the underlying grid:

<pre>
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  Credit: Felix Lee
</pre>

## Images and Figures

<figure>
  <img src="https://images.unsplash.com/photo-1551650975-87deedd944c3?w=800&h=400&fit=crop" alt="Minimal workspace" loading="lazy">
  <figcaption>Images automatically maintain grid alignment with proper aspect ratios</figcaption>
</figure>

## Debug Mode

At the bottom of every page, you'll find a "Debug grid" checkbox. When enabled, it overlays a visual grid showing how all elements align to the baseline grid. This is invaluable for:

- Checking typography alignment
- Identifying layout issues  
- Understanding the underlying grid system
- Fine-tuning custom components

## Responsive Behavior

The design system adapts gracefully across screen sizes:

- **Desktop**: Full grid system with optimal reading width
- **Tablet**: Adjusted spacing while maintaining alignment
- **Mobile**: Simplified layout with consistent typography

All elements maintain their grid alignment regardless of screen size.

## Dark Mode

The system automatically switches between light and dark themes based on your system preference (`prefers-color-scheme`). All colors are defined using CSS custom properties for seamless theme switching.

---

This showcase demonstrates the power and flexibility of the monospace web design system. Every element respects the underlying grid, creating a harmonious and highly readable experience. 