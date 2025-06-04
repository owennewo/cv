from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import json
from datetime import datetime, UTC

def main():
    with Path("profile/cv.json").open("r", encoding="utf-8") as f:
        data = json.load(f)
        data["current_year"] = datetime.now(tz=UTC).year

        print(data)
        if "social_links" in data:
            for link in data["social_links"]:
                if link.get("svg_path"):
                    with Path(link["svg_path"]).open(encoding="utf-8") as svg_file:
                        link["svg_data"] = svg_file.read()

        # Set up Jinja environment
        env = Environment(loader=FileSystemLoader("cvgen"), autoescape=True)
        cv_template = env.get_template("./template/cv_template.html")

        cv_output = cv_template.render(**data)

        # Write the output to an HTML file
        with Path("html/cv.html").open("w", encoding="utf-8") as f:
            f.write(cv_output)

        print("HTML file generated successfully!")

if __name__ == "__main__":
    main()
