# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a CV generator that creates an HTML resume from JSON data. The project follows the JSON Resume schema (jsonresume.org) and uses Python with Jinja2 templating to generate a static HTML CV that's deployed to GitHub Pages.

## Architecture

- **Profile Data**: `profile/profile.json` contains all CV content following JSON Resume format
- **Template Engine**: Jinja2 template in `cvgen/template/cv_template.html` renders the HTML
- **Generator**: `cvgen/main.py` loads JSON data, processes SVG icons, and renders the template
- **Output**: Generated HTML is written to `html/index.html` for GitHub Pages deployment
- **Static Assets**: CSS styles and images are stored in `html/css/` and `html/img/`

## Common Commands

```bash
# Generate the CV HTML from JSON data
uv run cvgen/main.py

# Install dependencies
uv sync

```

## Key Development Notes

- The generator automatically embeds SVG icons inline by reading files referenced in `social_links[].svg_path`
- Current year is automatically injected into template data for copyright/date references
- All output goes to `html/index.html` which is served by GitHub Pages
- Template uses modern CSS with CSS Grid and Flexbox for responsive layout
- Images and icons should be placed in `html/img/` directory

The profile is for a british user so should always use uk grammar, spelling, tone.
