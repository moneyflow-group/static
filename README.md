# static
A place for static files.


# Templates
E-mail templates are written in `mjml` and converted to `html` by `generate_html_templates.sh`

Receipt templates are written in `html` and converted to PDF by flow.

# Django fixtures
Django fixtures can be generated from the `html` files for both email and receipt `html` templates. Use the `generate_fixture.py` script in the `fixtures` folder.