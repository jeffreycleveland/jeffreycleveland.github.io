# Fonts Directory

This directory contains custom font files used on the website.

## Currently Referenced Fonts

The website's CSS (`css/main.css`) references the following custom font families:

- **CabritoContrast-ExtraBlack** - Used for main titles (h1)
- **CabritoContrast-ConExtraBoldItalic** - Used for subtitles (h2)
- **CabritoContrast-ExtraExtraBold** - Used for headings (h3-h6)
- **CabritoContrast-ExtraRegular** - Used for body text

## Adding Custom Fonts

To use custom fonts:

1. Place font files (`.woff`, `.woff2`, `.ttf`, etc.) in this directory
2. Update `css/main.css` with `@font-face` declarations pointing to these files
3. The existing CSS already references these font families in the fallback chain

## Current Behavior

Currently, the site falls back to Google Fonts' 'Open Sans' since custom font files are not yet added.
