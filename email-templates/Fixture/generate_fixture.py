#!/usr/bin/python3

import os
import json

dirname = os.path.dirname(os.path.abspath(__file__))

with open(dirname + "/fixture_template.json", "r") as fixture_template:
    templates = json.loads(fixture_template.read())

    for template in templates:
        identifier = template['fields']['identifier']
        language = template['fields']['language']
        platform = template['fields']['platform']

        print(f"Processing {platform}: {identifier} [{language}]")
