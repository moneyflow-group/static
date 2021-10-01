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
    build_folder = DIRNAME + "/build/"
    with open(build_folder + fixture_filename, "w") as fixture_file:
        print(f"Writing {build_folder}{fixture_filename}")
        fixture_file.write(json.dumps(fixtures, indent=4))


def generate_receipt_fixture():
    fixture_filename = "receipt_templates.json"
    fixtures = {}

    with open(
        DIRNAME + "/templates/FIXTURE_TEMPLATE_RECEIPTS.json", "r"
    ) as fixture_template:
        fixtures = json.loads(fixture_template.read())
        template_dirs = {
            "ALL": f"{DIRNAME}/../receipt-templates/ALL",
            "DINERO": f"{DIRNAME}/../receipt-templates/Dinero",
            "ECONOMIC": f"{DIRNAME}/../receipt-templates/E-conomic",
        }
        template_filenames = {
            "RECEIPT": "receipt_template.html",
            "CREDITNOTE": "credit_note_template.html",
            "LATE_FEE_RECEIPT": "late_fee_receipt_template.html",
        }

        for template in fixtures:
            language = template["fields"]["language"]
            platform = template["fields"]["platform"]
            identifier = template["fields"]["identifier"]

            template_dir = template_dirs[platform]
            template_filename = template_filenames[identifier]
            html_template_file = f"{template_dir}/{language}/{template_filename}"
            html_template = open(html_template_file)

            print(
                f"Processing [{html_template_file}] as [{platform}][{identifier}][{language}]"
            )
            template["fields"]["html"] = html_template.read()

    write_fixture_file(fixtures, fixture_filename)


def generate_email_fixture():
    fixture_filename = "default_email_templates.json"
    fixtures = {}

    with open(
        DIRNAME + "/templates/FIXTURE_TEMPLATE_EMAILS.json", "r"
    ) as fixture_template:
        fixtures = json.loads(fixture_template.read())
        template_dirs = {
            "ALL": f"{DIRNAME}/../email-templates/ALL",
            "Dinero": f"{DIRNAME}/../email-templates/Dinero",
            "E-conomic": f"{DIRNAME}/../email-templates/E-conomic",
            "Direct-Factoring": f"{DIRNAME}/../email-templates/Direct-Factoring",
        }

        for template in fixtures:
            identifier = template["fields"]["identifier"]
            language = template["fields"]["language"]
            platform = template["fields"]["platform"]

            template_dir = template_dirs[platform]
            html_template_file = f"{template_dir}/{language}/{identifier}.html"
            html_template = open(html_template_file)

            print(
                f"Processing [{html_template_file}] as [{platform}][{identifier}][{language}]"
            )
            template["fields"]["html_template"] = html_template.read().replace('"', '"')
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
