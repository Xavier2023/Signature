# -*- coding: utf-8 -*-
"""Generates the six Clearer group master email signatures into brands/.

Format follows index.html: logo, name, stacked services, accent divider bar,
contact links, circular-flag office blocks with the licence attached to the
office it belongs to, then an italic Courier disclaimer.

The wordmark is live HTML text rather than part of the logo image, so it can
flip black -> white in dark mode. Only the leaf mark is an image.
"""
import io
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brands")

LEAF_GREEN = "https://www.clearer.ae/logo.png"
LEAF_METAL = ("https://www.clearer.ae/"
              "Modify_leaf_logo_metallic_finish_202608131313-Photoroom%201.png")
LEAF_OUTSOURCING = "https://www.cleareroutsourcing.com/logo.png"
MARK_SWETCHE = "https://www.swetche.com/logo512x512.png"
MARK_FRIROSA = "https://www.frirosa.com/logo512x512.png"

SANS = "Nunito, 'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'Courier New', Courier, monospace"

# The group's offices, UAE first. Clearer, Clearer AE and ClearerPay all carry
# the full list; Clearer Metals is Dubai-only and keeps its own address.
ALL_OFFICES = [
    ("ae", ["158, Al Hebiah Third",
            "Dubai, United Arab Emirates"]),
    ("ee", ["Kuklase tn 15-37",
            "13423 Tallinn, Estonia",
            "US MSB &amp; EUROPEAN EMI LICENCE"]),
    ("ca", ["22 Lorne Place 102",
            "Regina SK S4R 8B3, Canada",
            "FINTRAC MSB REG: C100000072"]),
    ("gb", ["20 Aylestone Drive",
            "Leicester, England, LE2 8QD",
            "UK EMI LICENCE: IN PROGRESS"]),
    ("ng", ["Property Gate Centre",
            "2 The Rock Drive",
            "Lekki Phase 1, Lagos, Nigeria"]),
]

# (country code, [lines]) -- entity and licence live in the lines, per index.html
BRANDS = [
 dict(
  key="clearer", file="clearer.html", title="Clearer",
  mark="https://www.clearer.ae/sig-clearer.png",
  dark_mark="https://www.clearer.ae/sig-clearer-dark.png",
  mark_w=149, mark_h=58,
  word="clearer", suffix="", tm=True, accent="#78b60f", accent_dark="#a3e635",
  services=["International Trade Facilitation", "Trade Compliance", "Freight Services"],
  phone="+232 074 605 659", wa="", email="hello@clearer.ae",
  web="https://www.clearer.ae/", weburl="https://www.clearer.ae",
  offices=ALL_OFFICES,
  partners=[]),

 dict(
  # Same content as Clearer -- this is the UAE arm.
  key="clearerae", file="clearer-ae.html", title="Clearer AE",
  mark="https://www.clearer.ae/sig-clearer.png",
  dark_mark="https://www.clearer.ae/sig-clearer-dark.png",
  mark_w=149, mark_h=58,
  word="clearer", suffix="", tm=True, accent="#78b60f", accent_dark="#a3e635",
  services=["International Trade Facilitation", "Trade Compliance", "Freight Services"],
  phone="+232 074 605 659", wa="", email="hello@clearer.ae",
  web="https://www.clearer.ae/", weburl="https://www.clearer.ae",
  offices=ALL_OFFICES,
  partners=[]),

 dict(
  key="clearerpay", file="clearerpay.html", title="ClearerPay",
  mark="https://www.clearerpay.com/sig-clearerpay.png",
  dark_mark="https://www.clearerpay.com/sig-clearerpay-dark.png",
  mark_w=170, mark_h=48,
  word="Clearer", suffix="Pay", two_weight=True, tm=False,
  accent="#78b60f", accent_dark="#a3e635",
  services=["E-Collections &amp; Settlements", "Trade Finance", "E-Invoicing"],
  phone="+234 803 418 4304", wa="+372 5392 2010", email="support@clearerpay.com",
  web="https://www.clearerpay.com/", weburl="https://www.clearerpay.com",
  offices=ALL_OFFICES,
  partners=[]),

 dict(
  key="clearermetals", file="clearermetals.html", title="Clearer Metals",
  mark="https://www.clearer.ae/sig-metals.png",
  dark_mark="https://www.clearer.ae/sig-metals-dark.png",
  mark_w=162, mark_h=68,
  word="clearer", suffix="Metals", tm=False,
  accent="#6b7f3a", accent_dark="#c3d98a",
  services=["Solid Minerals", "Petroleum Products", "Metals &amp; Precious Stones"],
  phone="+971 50 501 9566", wa="+971 50 501 9566", email="hello@clearer.ae",
  web="https://www.clearer.ae/", weburl="https://www.clearer.ae",
  # Dubai only, and it is the same address as the rest of the group.
  offices=ALL_OFFICES[:1],
  # Accreditation logos kept exactly as they are in mdclearermetal.html.
  partners=[("https://www.dubaichambers.com/documents/d/global/dubai-chamber-logo",
             "Dubai Chamber", 34),
            ("https://www.dubaidet.gov.ae/en/-/media/common/logos/revised/"
             "dubai-det-flag-logo.svg?h=47&amp;iar=0&amp;w=75", "Dubai DET", 51)]),

 dict(
  key="cleareroutsourcing", file="clearer-outsourcing.html",
  title="Clearer Outsourcing",
  mark="https://www.clearer.ae/sig-outsourcing.png",
  dark_mark="https://www.clearer.ae/sig-outsourcing-dark.png",
  mark_w=95, mark_h=67,
  word="clearer", suffix="outsourcing", tm=False,
  accent="#78b60f", accent_dark="#a3e635",
  services=["Import &amp; Export", "Supply Chain", "Trade Finance", "Distribution"],
  phone="+232 074 605 659", wa="", email="hello@cleareroutsourcing.com",
  web="https://www.cleareroutsourcing.com/",
  weburl="https://www.cleareroutsourcing.com",
  offices=[
    ("ng", ["Property Gate Centre",
            "2 The Rock Drive",
            "Lekki Phase 1, Lagos, Nigeria"]),
    ("ee", ["Kuklase tn 15-37",
            "13423 Tallinn, Estonia"]),
    ("gb", ["20 Aylestone Drive",
            "Leicester, England, LE2 8QD"]),
    ("gh", ["5, Agoali Street",
            "Seminary Madina, Accra, Ghana"]),
  ],
  partners=[]),

 dict(
  key="swetche", file="swetche.html", title="Swetche",
  mark="https://www.swetche.com/sig-swetche.png",
  dark_mark="https://www.swetche.com/sig-swetche-dark.png",
  mark_w=170, mark_h=25,
  word="swetche", suffix="", dot=True, tm=False,
  accent="#22c55e", accent_dark="#4ade80",
  services=["Remittance", "Foreign Exchange", "Multicurrency Accounts"],
  phone="+234 8023 937 860", wa="", email="support@swetche.com",
  web="https://www.swetche.com/", weburl="https://www.swetche.com",
  offices=[
    ("ng", ["PropertyGate Centre",
            "2 The Rock Drive",
            "Lekki Phase 1, Lagos, Nigeria",
            "CBN IMTO LICENCE"]),
    ("ca", ["1304-15 Greenview Ave",
            "Toronto, ON M2M 4M7, Canada",
            "FINTRAC MSB REG: M23503773"]),
  ],
  partners=[]),

 dict(
  key="frirosa", file="frirosa.html", title="Frirosa",
  mark="https://www.frirosa.com/frirosa-logo-dark.png",
  dark_mark="https://www.frirosa.com/frirosa-logo.png",
  mark_w=123, mark_h=57,
  word="frirosa", suffix="", tm=False,
  accent="#e0b400", accent_dark="#ffd84d",
  services=["Bureau De Change", "Foreign Exchange"],
  phone="+234 707 475 3808", wa="+234 707 475 3808", email="hello@frirosa.com",
  web="https://www.frirosa.com/", weburl="https://www.frirosa.com",
  offices=[
    ("ng", ["Property Gate Centre",
            "2 The Rock Drive",
            "Lekki Phase 1, Lagos, Nigeria",
            "CBN LICENCE: 000246"]),
  ],
  partners=[]),
]


STYLE = """    <link
      href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap"
      rel="stylesheet"
    />
    <style>
      /* Nunito loads in Apple Mail, iOS Mail and Outlook for Mac; everything
         else falls back to Helvetica/Arial at the same metrics. */
      @import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap");

      /* The wordmark is text, not part of the logo image, so it can invert.
         Honoured by Apple Mail (macOS/iOS) and Outlook.com. */
      @media (prefers-color-scheme: dark) {
        .sig-word,
        .sig-name   { color: #ffffff !important; }
        .sig-body   { color: #e5e7eb !important; }
        .sig-legal  { color: #d1d5db !important; }
        .sig-accent { color: {accent_dark} !important; }
        .sig-link   { color: {accent_dark} !important; }
      }
      [data-ogsc] .sig-word,
      [data-ogsc] .sig-name   { color: #ffffff !important; }
      [data-ogsc] .sig-body   { color: #e5e7eb !important; }
      [data-ogsc] .sig-legal  { color: #d1d5db !important; }
      [data-ogsc] .sig-accent { color: {accent_dark} !important; }
      [data-ogsc] .sig-link   { color: {accent_dark} !important; }
    </style>"""


def lockup(b):
    """The logo on a white plate.

    Every client -- including Outlook, which strips <style> from signatures
    and has no prefers-color-scheme at all -- then shows the logo against
    white, so the dark-text wordmark can never sit on a dark ground. That
    removes the need for a light/dark image swap entirely.
    """
    mark = ('<img src="%s" alt="%s" width="%d" height="%d" '
            'style="display: block; width: %dpx; height: auto; border: 0" />'
            % (b["mark"], b["title"], b["mark_w"], b["mark_h"], b["mark_w"]))

    return """          <table cellpadding="0" cellspacing="0" border="0">
            <tr>
              <td
                align="center"
                bgcolor="#ffffff"
                style="background-color: #ffffff; border-radius: 10px; padding: 7px 11px"
              >
%s
              </td>
            </tr>
          </table>""" % ("                " + mark)


def contact(b):
    """T and WA on one line, website on the next. No email line."""
    def link(href, text):
        return ('<a href="%s" class="sig-link" style="color: %s; '
                'text-decoration: underline">%s</a>' % (href, b["accent"], text))

    first = "          <strong>T</strong> %s" % link(
        "tel:" + b["phone"].replace(" ", ""), b["phone"])
    if b["wa"]:
        first += "&nbsp;&nbsp;&nbsp;<strong>WA</strong> %s" % link(
            "https://wa.me/" + b["wa"].replace(" ", "").replace("+", ""), b["wa"])

    second = "          <strong>W</strong> %s" % link(b["weburl"], b["web"])
    return first + "\n          <br />\n" + second


def office_cell(cc, lines):
    """One office: circular flag + address, sized for a half-width column."""
    return """              <td valign="top" width="300" style="width: 300px; padding-bottom: 14px">
                <table cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td valign="top" style="padding-right: 12px">
                      <img
                        src="https://www.clearer.ae/flags/%s.png"
                        alt="%s"
                        width="35"
                        height="35"
                        style="width: 35px; height: 35px; display: block; border: 0"
                      />
                    </td>
                    <td
                      class="sig-body"
                      valign="top"
                      style="
                        font-family: %s;
                        font-size: 13px;
                        line-height: 19px;
                        color: #1f2937;
                      "
                    >
                      %s
                    </td>
                  </tr>
                </table>
              </td>""" % (cc, cc.upper(), MONO,
                          "<br />\n                      ".join(lines))


def offices(b):
    """Offices laid out two per row."""
    items = b["offices"]
    rows = []
    for i in range(0, len(items), 2):
        pair = items[i:i + 2]
        cells = [office_cell(cc, lines) for cc, lines in pair]
        if len(pair) == 1:
            cells.append('              <td width="300" style="width: 300px">&nbsp;</td>')
        rows.append("            <tr>\n%s\n            </tr>" % "\n".join(cells))

    return """      <tr>
        <td style="padding-bottom: 28px">
          <table cellpadding="0" cellspacing="0" border="0" width="600">
%s
          </table>
        </td>
      </tr>
""" % "\n".join(rows)


def partners(b):
    if not b["partners"]:
        return ""
    cells = "\n".join(
        """              <td style="padding-right: 26px">
                <img
                  src="%s"
                  alt="%s"
                  height="%d"
                  style="display: block; max-height: %dpx; border: 0"
                />
              </td>""" % (src, alt, h, h) for src, alt, h in b["partners"])
    return """
      <!-- ACCREDITATIONS -->
      <tr>
        <td style="padding-top: 22px">
          <table cellpadding="0" cellspacing="0" border="0">
            <tr>
%s
            </tr>
          </table>
        </td>
      </tr>
""" % cells


# People. Each gets the full brand set under people/<slug>/.
# `overrides` swaps brand contact details for personal ones where they differ.
PEOPLE = [
 dict(
  slug="lucky-koiza-oyanna",
  name="LUCKY KOIZA OYANNA &#8211; CEO",
  name_first=True,
  overrides={
    # From signature.html -- his ClearerPay line.
    "clearerpay": dict(phone="+234 803 418 4304", wa="+372 5392 2010"),
    # From mdclearermetal.html -- his Dubai line.
    "clearermetals": dict(phone="+971 50 501 9566", wa="+971 50 501 9566",
                          web="https://www.clearermetals.com/",
                          weburl="https://www.clearermetals.com/"),
  }),

 dict(
  slug="charles-ike",
  name="CHARLES IKE &#8211; SENIOR DIGITAL GROWTH OFFICER",
  contact=dict(phone="+234 805 468 3610", wa="")),

 dict(
  slug="taiwo-adegboye",
  name="TAIWO ADEGBOYE &#8211; EXECUTIVE ASSISTANT TO THE CEO",
  contact=dict(phone="+234 913 968 8610", wa="")),

 dict(
  slug="gift-eboigbe",
  name="GIFT EBOIGBE &#8211; ACCOUNT EXECUTIVE (WEST AFRICA)",
  contact=dict(phone="+234 707 475 3810", wa="")),

 dict(
  slug="ajibola-bamisaye",
  name="AJIBOLA O. BAMISAYE &#8211; COMPLIANCE &amp; RISK OFFICER",
  contact=dict(phone="+234 707 468 3810", wa="")),

 dict(
  slug="joy-sanyu",
  name="JOY SANYU &#8211; ACTING COUNTRY MANAGER (UAE)",
  name_first=True,
  contact=dict(phone="+971 58 123 0770", wa="+971 58 123 0770")),

 dict(
  slug="oluwasegun-olajumoke",
  name="OLUWASEGUN OLAJUMOKE &#8211; TRADING OFFICER",
  name_first=True,
  contact=dict(phone="+234 707 468 4125", wa="+234 707 468 4125")),

 dict(
  slug="orjinta-onyedikachi-anthony",
  name="ORJINTA ONYEDIKACHI ANTHONY &#8211; FRONTEND ENGINEER",
  name_first=True,
  contact=dict(phone="+234 913 094 7049", wa="")),

 dict(
  slug="emmanuel-jaiyeola",
  name="EMMANUEL JAIYEOLA &#8211; GOVERNANCE AND ONBOARDING OFFICER",
  name_first=True,
  contact=dict(phone="+234 916 832 0775", wa="+234 916 832 0775")),

 dict(
  slug="jane-cavarlho",
  name="JANE CAVARLHO &#8211; PERSONAL MANAGER / INTERN",
  name_first=True,
  contact=dict(phone="+971 50 157 7944", wa="+971 50 157 7944")),
]


def render(b, name, name_first=False):
    return TEMPLATE.format(
        header=header(b, name, name_first),
        title=b["title"],
        style=STYLE.replace("{accent_dark}", b["accent_dark"]),
        sans=SANS, mono=MONO,
        services=" | ".join(b["services"]),
        accent=b["accent"], contact=contact(b), offices=offices(b),
        email=b["email"], partners=partners(b),
    )


LOGO_ROW = """      <!-- LOGO -->
      <tr>
        <td style="padding-bottom: %dpx">
%s
        </td>
      </tr>
"""

NAME_ROW = """      <!-- NAME -->
      <tr>
        <td
          class="sig-name"
          style="
            font-family: %s;
            font-size: 16px;
            line-height: 30px;
            font-weight: bold;
            color: #1f2937;
            letter-spacing: 1px;
            padding-bottom: %dpx;
          "
        >
          %s
        </td>
      </tr>
"""


def header(b, name, name_first):
    """Logo above the name, or the name above the logo."""
    if name_first:
        return (NAME_ROW % (MONO, 12, name)) + "\n" + (LOGO_ROW % (14, lockup(b)))
    return (LOGO_ROW % (14, lockup(b))) + "\n" + (NAME_ROW % (MONO, 12, name))



TEMPLATE = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="color-scheme" content="light dark" />
    <meta name="supported-color-schemes" content="light dark" />
    <title>{title} Email Signature</title>
{style}
  </head>

  <body style="margin: 0; padding: 0">
    <table
      cellpadding="0"
      cellspacing="0"
      border="0"
      width="640"
      style="
        width: 640px;
        max-width: 640px;
        padding: 20px;
        font-family: {sans};
        color: #1f2937;
      "
    >
{header}

      <!-- SERVICES -->
      <tr>
        <td
          class="sig-accent"
          style="
            font-family: {mono};
            font-size: 14px;
            line-height: 30px;
            font-weight: 700;
            color: {accent};
            padding-bottom: 12px;
          "
        >
          {services}
        </td>
      </tr>

      <!-- DIVIDER -->
      <tr>
        <td style="padding-bottom: 11px">
          <div style="width: 30px; height: 3px; background: {accent}"></div>
        </td>
      </tr>

      <!-- CONTACT -->
      <tr>
        <td
          class="sig-body"
          style="
            font-family: {mono};
            font-size: 14px;
            line-height: 20px;
            color: #1f2937;
            padding-bottom: 20px;
          "
        >
{contact}
        </td>
      </tr>

{offices}
      <!-- DISCLAIMER -->
      <tr>
        <td
          class="sig-legal"
          style="
            font-size: 11px;
            line-height: 16px;
            color: #6b7280;
            font-style: italic;
            font-family: {mono};
          "
        >
          <strong>
            <u>DISCLAIMER:</u>
          </strong>

          The data contained in, or attached to this E-mail may contain
          Confidential, Restricted, or Security Sensitive Information and is
          intended for the recipient only.
          <br /><br />

          If the Information is Restricted or contains Security Sensitive
          Information and you do not have a &quot;need to know&quot; you must
          not use, disclose, distribute, copy, print or read the content of the
          data or its attachments. If an addressing or transmission error has
          misdirected this email and you are not the intended recipient, please
          notify the author immediately by replying to this

          <a
            href="mailto:{email}"
            class="sig-link"
            style="color: {accent}; text-decoration: underline"
          >
            {email}
          </a>
        </td>
      </tr>
{partners}    </table>
  </body>
</html>
"""

for b in BRANDS:
    path = os.path.join(OUT, b["file"])
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(render(b, "FULL NAME &#8211; JOB TITLE"))
    print("wrote", path)

for person in PEOPLE:
    pdir = os.path.join(OUT, "..", "people", person["slug"])
    if not os.path.isdir(pdir):
        os.makedirs(pdir)
    for b in BRANDS:
        pb = dict(b)
        pb.update(person.get("contact", {}))
        pb.update(person.get("overrides", {}).get(b["key"], {}))
        path = os.path.join(pdir, b["file"])
        with io.open(path, "w", encoding="utf-8") as f:
            f.write(render(pb, person["name"], person.get("name_first", False)))
        print("wrote", os.path.normpath(path))
