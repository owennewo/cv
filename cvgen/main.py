import json
from datetime import UTC, datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright


def main():
    with Path("profile/profile.json").open("r", encoding="utf-8") as f:
        data = json.load(f)
        data["current_year"] = datetime.now(tz=UTC).year

        print(data)
        if "social_links" in data:
            for link in data["social_links"]:
                if link.get("svg_path"):
                    with Path(f"html/{link['svg_path']}").open(
                        encoding="utf-8"
                    ) as svg_file:
                        link["svg_data"] = svg_file.read()

        # Set up Jinja environment
        env = Environment(loader=FileSystemLoader("cvgen"), autoescape=True)
        cv_template = env.get_template("./template/cv_template.html")

        cv_output = cv_template.render(**data)

        # Write the output to an HTML file
        with Path("html/index.html").open("w", encoding="utf-8") as f:
            f.write(cv_output)

        print("HTML file generated successfully!")

        # Generate PDF from HTML using Playwright
        short_date = datetime.now(tz=UTC).strftime("%Y-%m-%d")
        pdf_output_path = Path(f"html/owen-williams-{short_date}.pdf")

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            # Set viewport to simulate desktop width for proper two-column layout
            page.set_viewport_size({"width": 1200, "height": 1600})

            # Load the HTML file
            page.goto(f"file://{Path('html/index.html').absolute()}")

            # Wait for content to load
            page.wait_for_load_state("networkidle")

            # Generate PDF with print media simulation
            page.pdf(
                path=pdf_output_path,
                format="A4",
                margin={"top": "1cm", "bottom": "1cm", "left": "1cm", "right": "1cm"},
                print_background=True,
                prefer_css_page_size=False,
            )

            browser.close()

        print(f"PDF file generated successfully at {pdf_output_path}!")


if __name__ == "__main__":
    main()
