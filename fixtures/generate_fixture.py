#!/usr/bin/python3
import os
import json
import argparse

DIRNAME = os.path.dirname(os.path.abspath(__file__))


def main(fixture_type):
    if fixture_type == "email":
        generate_email_fixture()
    elif fixture_type == "receipt":
        generate_receipt_fixture()
    else:
        print("Invalid fixture_type")
        exit(-1)


def write_fixture_file(fixtures, fixture_filename):
    with open(DIRNAME + "/" + fixture_filename, "w") as fixture_file:
        print(f"Writing {fixture_filename}")
        fixture_file.write(json.dumps(fixtures))


def generate_receipt_fixture():
    fixture_filename = "receipt_templates.json"
    fixtures = {}

    with open(
        DIRNAME + "/templates/FIXTURE_TEMPLATE_RECEIPTS.json", "r"
    ) as fixture_template:
        fixtures = json.loads(fixture_template.read())
        dinero_fixtures_dir = f"{DIRNAME}/../receipt-templates/Dinero"
        economic_fixtures_dir = f"{DIRNAME}/../receipt-templates/E-conomic"

        for template in fixtures:
            language = template["fields"]["language"]
            platform = template["fields"]["platform"]

            template_dir = (
                dinero_fixtures_dir if platform == "Dinero" else economic_fixtures_dir
            )

            html_template_file = f"{template_dir}/{language}/receipt_template.html"
            html_template = open(html_template_file)

            print(f"Processing [{html_template_file}] as [{platform}][{language}]")
            template["fields"]["html"] = html_template.read()

    write_fixture_file(fixtures, fixture_filename)


def generate_email_fixture():
    fixture_filename = "default_email_templates.json"
    fixtures = {}

    with open(
        DIRNAME + "/templates/FIXTURE_TEMPLATE_EMAILS.json", "r"
    ) as fixture_template:
        fixtures = json.loads(fixture_template.read())
        dinero_fixtures_dir = f"{DIRNAME}/../email-templates/Dinero"
        economic_fixtures_dir = f"{DIRNAME}/../email-templates/E-conomic"

        for template in fixtures:
            identifier = template["fields"]["identifier"]
            language = template["fields"]["language"]
            platform = template["fields"]["platform"]

            template_dir = (
                dinero_fixtures_dir if platform == "Dinero" else economic_fixtures_dir
            )

            html_template_file = f"{template_dir}/{language}/{identifier}.html"
            html_template = open(html_template_file)

            print(
                f"Processing [{html_template_file}] as [{platform}][{identifier}][{language}]"
            )
            template["fields"]["html_template"] = html_template.read()
    write_fixture_file(fixtures, fixture_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generates a Django fixture from HTML templates")
    parser.add_argument(
        "fixture_type",
        type=str,
        help="Choose either to generate the [email] or [receipt] fixture",
        choices=["email", "receipt"],
    )
    args = parser.parse_args()

    main(args.fixture_type)
