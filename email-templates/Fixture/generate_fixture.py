#!/usr/bin/python3
import os
import json

dirname = os.path.dirname(os.path.abspath(__file__))
templates = {}

with open(dirname + "/fixture_template.json", "r") as fixture_template:
    templates = json.loads(fixture_template.read())
    dinero_templates_dir = f"{dirname}/../Dinero"
    economic_templates_dir = f"{dirname}/../E-conomic"

    for template in templates:
        identifier = template["fields"]["identifier"]
        language = template["fields"]["language"]
        platform = template["fields"]["platform"]

        template_dir = (
            dinero_templates_dir if platform == "Dinero" else economic_templates_dir
        )

        html_template_file = f"{template_dir}/{language}/{identifier}.html"
        html_template = open(html_template_file)

        print(f"Processing [{html_template_file}] as [{platform}][{identifier}][{language}]")
        template["fields"]["html_template"] = html_template.read()

template_fixture_filename = "default_email_templates.json"
with open(dirname + "/" + template_fixture_filename, "w") as fixture_file:
    print(f"Writing {template_fixture_filename}")
    fixture_file.write(json.dumps(templates))
