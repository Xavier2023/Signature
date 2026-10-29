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
# WhatsApp glyph shown in place of the WA number; links to the wa.me DM.
WHATSAPP_ICON = "https://img.icons8.com/color/48/whatsapp--v1.png"
# Phone and globe glyphs replace the T and W labels, tinted per brand.
ICON_URL = "https://img.icons8.com/ios-filled/50/%s/%s.png"

# Regulator marks for Swetche, from Wikimedia.
CBN_LOGO = ("https://upload.wikimedia.org/wikipedia/en/thumb/3/35/"
            "Central_Bank_of_Nigeria_logo.svg/"
            "120px-Central_Bank_of_Nigeria_logo.svg.png")
FINTRAC_LOGO = ("https://upload.wikimedia.org/wikipedia/commons/thumb/"
                "c/c7/FINTRAC_Logo.png/330px-FINTRAC_Logo.png")

SANS = "Nunito, 'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'Courier New', Courier, monospace"

# Logos and accreditation marks render at this fraction of their listed size.
LOGO_SCALE = 0.8

# The group's offices, UAE first. Clearer, Clearer AE and ClearerPay all carry
# the full list; Clearer Metals is Dubai-only and keeps its own address.
ALL_OFFICES = [
    ("ae", ["158, Al Hebiah Third",
            "Dubai, United Arab Emirates"]),
    ("ee", ["Kuklase tn 15-37",
            "13423 Tallinn, Estonia",
            "US MSB &amp; EUROPEAN EMI LICENCE"]),
    ("ca", ["22 Lorne Place 102",
            "Regina SK S4R 8B3, Canada"]),
    ("gb", ["20 Aylestone Drive",
            "Leicester, England, LE2 8QD"]),
    ("ng", ["Property Gate Centre",
            "2 The Rock Drive",
            "Lekki Phase 1, Lagos, Nigeria"]),
]

# Clearer and Clearer Metals list only the Dubai office.
DUBAI_OFFICE = ALL_OFFICES[:1]

# (country code, [lines]) -- entity and licence live in the lines, per index.html
BRANDS = [
 dict(
  key="clearer", file="clearer.html", title="Clearer",
  mark="https://www.clearer.ae/sig-clearer.png",
  dark_mark="https://www.clearer.ae/sig-clearer-dark.png",
  # Clearer Group logo, 1000x311.
  mark_w=230, mark_h=72,
  word="clearer", suffix="", tm=True, accent="#78b60f", accent_dark="#a3e635",
  services=["Trade Finance", "Intelligent Procurement", "Payments"],
  phone="+232 074 605 659", wa="", email="hello@clearer.ae",
  web="https://www.clearer.ae/", weburl="https://www.clearer.ae",
  offices=DUBAI_OFFICE,
  partners=[]),

 dict(
  # Same content as Clearer -- this is the UAE arm.
  key="clearerae", file="clearer-ae.html", title="Clearer AE",
  mark="https://www.clearer.ae/sig-clearer.png",
  dark_mark="https://www.clearer.ae/sig-clearer-dark.png",
  # Clearer Group logo, 1000x311.
  mark_w=230, mark_h=72,
  word="clearer", suffix="", tm=True, accent="#78b60f", accent_dark="#a3e635",
  services=["Trade Finance", "Intelligent Procurement", "Payments"],
  phone="+232 074 605 659", wa="", email="hello@clearer.ae",
  web="https://www.clearer.ae/", weburl="https://www.clearer.ae",
  offices=ALL_OFFICES,
  # Clearer AE signatures show the office flags only, no addresses
  # (as Elohor's). Applies to the master and every person's version.
  flags_only=True,
  partners=[]),

 dict(
  key="clearerpay", file="clearerpay.html", title="ClearerPay",
  mark="https://www.clearerpay.com/sig-clearerpay.png",
  dark_mark="https://www.clearerpay.com/sig-clearerpay-dark.png",
  mark_w=170, mark_h=48,
  word="Clearer", suffix="Pay", two_weight=True, tm=False,
  accent="#78b60f", accent_dark="#a3e635",
  services=["Payments", "E-Collections &amp; Settlements", "E-Invoicing"],
  phone="+234 803 418 4304", wa="+372 5392 2010", email="support@clearerpay.com",
  web="https://www.clearerpay.com/", weburl="https://www.clearerpay.com",
  # Canada only.
  offices=[o for o in ALL_OFFICES if o[0] == "ca"],
  partners=[]),

 dict(
  key="clearermetals", file="clearermetals.html", title="Clearer Metals",
  mark="https://www.clearer.ae/sig-metals.png",
  dark_mark="https://www.clearer.ae/sig-metals-dark.png",
  mark_w=162, mark_h=68,
  word="clearer", suffix="Metals", tm=False,
  accent="#6b7f3a", accent_dark="#c3d98a",
  services=["Solid Minerals", "Petroleum Products", "Metals &amp; Precious Stones"],
  phone="+971 50 501 9566", wa="+971 50 501 9566", email="hello@clearermetals.com",
  web="https://www.clearermetals.com/", weburl="https://www.clearermetals.com/",
  offices=DUBAI_OFFICE,
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
  services=["Import &amp; Export", "Supply Chain", "Distribution"],
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
  services=["Digital Asset Management", "Cross Border Remittances",
            "Multicurrency Accounts"],
  phone="+234 8023 937 860", wa="", email="support@swetche.com",
  web="https://www.swetche.com/", weburl="https://www.swetche.com",
  offices=[
    ("ng", ["PropertyGate Centre",
            "2 The Rock Drive",
            "Lekki Phase 1, Lagos, Nigeria"]),
    ("ca", ["1304-15 Greenview Ave",
            "Toronto, ON M2M 4M7, Canada"]),
  ],
  # Regulators, on their own row after the disclaimer.
  partners=[(CBN_LOGO, "Central Bank of Nigeria", 64),
            (FINTRAC_LOGO, "FINTRAC", 60)]),

 dict(
  key="frirosa", file="frirosa.html", title="Frirosa",
  mark="https://www.frirosa.com/frirosa-logo-dark.png",
  dark_mark="https://www.frirosa.com/frirosa-logo.png",
  mark_w=123, mark_h=57,
  word="frirosa", suffix="", tm=False,
  accent="#e0b400", accent_dark="#ffd84d",
  services=["Money Lending", "Travel Allowance", "Cash Point"],
  phone="+234 707 475 3808", wa="+234 707 475 3808", email="hello@frirosa.com",
  web="https://www.frirosa.com/", weburl="https://www.frirosa.com",
  offices=[
    ("ng", ["Property Gate Centre",
            "2 The Rock Drive",
            "Lekki Phase 1, Lagos, Nigeria"]),
  ],
  # Regulator, on its own row after the disclaimer.
  partners=[(CBN_LOGO, "Central Bank of Nigeria", 64)]),
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
    w, h = round(b["mark_w"] * LOGO_SCALE), round(b["mark_h"] * LOGO_SCALE)
    mark = ('<img src="%s" alt="%s" width="%d" height="%d" '
            'style="display: block; width: %dpx; height: auto; border: 0" />'
            % (b["mark"], b["title"], w, h, w))

    return """          <table cellpadding="0" cellspacing="0" border="0">
            <tr>
              <td
                align="center"
                bgcolor="#ffffff"
                style="background-color: #ffffff; border-radius: 8px; padding: 5px 9px"
              >
%s
              </td>
            </tr>
          </table>""" % ("                " + mark)


def contact(b):
    """Phone and WA on one line, website on the next. No email line.
    The phone always shows, even when WhatsApp uses the same number."""
    def glyph(name, alt):
        return ('<img src="%s" width="18" height="18" alt="%s" '
                'style="display: inline-block; width: 18px; height: 18px; '
                'border: 0; vertical-align: middle" />'
                % (ICON_URL % (b["accent"].lstrip("#"), name), alt))

    def link(href, text):
        return ('<a href="%s" class="sig-link" style="color: %s; '
                'text-decoration: underline">%s</a>' % (href, b["accent"], text))

    wa_href = "https://wa.me/" + b["wa"].replace(" ", "").replace("+", "")
    icon = ('<a href="%s" style="text-decoration: none"><img src="%s" '
            'width="24" height="24" alt="WhatsApp" title="WhatsApp %s" '
            'style="display: inline-block; width: 24px; height: 24px; '
            'border: 0; vertical-align: middle" /></a>'
            % (wa_href, WHATSAPP_ICON, b["wa"]))

    second = "          %s %s" % (glyph("globe--v1", "Website"),
                                    link(b["weburl"], b["web"]))
    # No phone (someone without a number yet) drops the whole first line,
    # WhatsApp included, leaving just the website.
    if not b["phone"]:
        return second

    first = "          %s %s" % (glyph("phone", "Phone"), link(
        "tel:" + b["phone"].replace(" ", ""), b["phone"]))
    if b["wa"]:
        first += "&nbsp;&nbsp;&nbsp;" + icon
        # `wa_raw_link` also shows the wa.me URL beside the icon.
        if b.get("wa_raw_link"):
            first += " " + link(wa_href, wa_href)

    # Spacer block rather than a <br /> so the number and website lines
    # get a visible gap in every email client.
    gap = ('<div style="height: 10px; line-height: 10px; font-size: 10px">'
           '&nbsp;</div>')
    return first + "\n          " + gap + "\n" + second


def office_cell(cc, lines):
    """One office: circular flag + address, sized for a half-width column."""
    return """              <td valign="top" width="290" style="width: 290px; padding-bottom: 10px">
                <table cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td valign="top" style="padding-right: 10px">
                      <img
                        src="https://www.clearer.ae/flags/%s.png"
                        alt="%s"
                        width="28"
                        height="28"
                        style="width: 28px; height: 28px; display: block; border: 0"
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


def flags_only(b):
    """Just the office flags in one row, for people who want no addresses."""
    cells = "\n".join(
        """              <td style="padding-right: 10px">
                <img
                  src="https://www.clearer.ae/flags/%s.png"
                  alt="%s"
                  width="28"
                  height="28"
                  style="width: 28px; height: 28px; display: block; border: 0"
                />
              </td>""" % (cc, cc.upper()) for cc, _ in b["offices"])
    return """      <tr>
        <td style="padding-bottom: 20px">
          <table cellpadding="0" cellspacing="0" border="0">
            <tr>
%s
            </tr>
          </table>
        </td>
      </tr>
""" % cells


def offices(b):
    """Offices laid out two per row."""
    if b.get("flags_only"):
        return flags_only(b)
    items = b["offices"]
    rows = []
    for i in range(0, len(items), 2):
        pair = items[i:i + 2]
        cells = [office_cell(cc, lines) for cc, lines in pair]
        if len(pair) == 1:
            cells.append('              <td width="290" style="width: 290px">&nbsp;</td>')
        rows.append("            <tr>\n%s\n            </tr>" % "\n".join(cells))

    return """      <tr>
        <td style="padding-bottom: 20px">
          <table cellpadding="0" cellspacing="0" border="0" width="580">
%s
          </table>
        </td>
      </tr>
""" % "\n".join(rows)


def partners(b):
    if not b["partners"]:
        return ""
    cells = "\n".join(
        """              <td style="padding-right: 20px">
                <img
                  src="%s"
                  alt="%s"
                  height="%d"
                  style="display: block; max-height: %dpx; border: 0"
                />
              </td>""" % (src, alt, round(h * LOGO_SCALE), round(h * LOGO_SCALE))
        for src, alt, h in b["partners"])
    return """
      <!-- ACCREDITATIONS -->
      <tr>
        <td style="padding-top: 16px">
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
    "clearermetals": dict(phone="+971 50 501 9566", wa="+971 50 501 9566"),
  }),

 dict(
  slug="charles-ike",
  name="CHARLES IKE &#8211; SENIOR DIGITAL GROWTH OFFICER",
  name_first=True,
  contact=dict(phone="+234 805 468 3610", wa="+234 805 468 3610")),

 dict(
  slug="taiwo-adegboye",
  name="TAIWO ADEGBOYE &#8211; EXECUTIVE ASSISTANT TO THE CEO",
  name_first=True,
  contact=dict(phone="+234 913 968 8610", wa="+234 913 968 8610")),

 dict(
  slug="gift-eboigbe",
  name="GIFT EBOIGBE &#8211; ACCOUNT EXECUTIVE (WEST AFRICA)",
  name_first=True,
  contact=dict(phone="+234 707 475 3810", wa="+234 707 475 3810")),

 dict(
  slug="ajibola-bamisaye",
  name="AJIBOLA O. BAMISAYE &#8211; RISK AND COMPLIANCE MANAGER",
  name_first=True,
  contact=dict(phone="+234 707 468 3810", wa="+234 707 468 3810")),

 dict(
  slug="joshua-ayanda",
  name="JOSHUA AYANDA &#8211; RISK AND COMPLIANCE OFFICER",
  name_first=True,
  # No phone or WhatsApp yet -- website line only. Add them here when issued.
  contact=dict(phone="", wa="")),

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
  contact=dict(phone="+234 913 094 7049", wa="+234 913 094 7049")),

 dict(
  slug="emmanuel-jaiyeola",
  name="EMMANUEL JAIYEOLA &#8211; GOVERNANCE AND ONBOARDING OFFICER",
  name_first=True,
  contact=dict(phone="+234 916 832 0775", wa="+234 916 832 0775")),

 dict(
  slug="elohor-esalomi",
  name="ELOHOR ESALOMI &#8211; CUSTOMER EXPERIENCE MANAGEMENT PERSONNEL",
  name_first=True,
  # No office addresses for her -- only the country flags.
  contact=dict(phone="+234 707 468 4122", wa="+234 707 468 4122",
               flags_only=True)),

] + [
 # Jane has two signature sets, one per role; only the title differs.
 dict(
  slug=slug,
  name="JANE CAVARLHO &#8211; " + role,
  name_first=True,
  contact=dict(phone="+971 50 157 7944", wa="+971 50 157 7944"))
 for slug, role in [
   ("jane-cavarlho", "PERSONAL MANAGER"),
   ("jane-cavarlho-cemp", "CUSTOMER EXPERIENCE MANAGEMENT PERSONNEL"),
 ]
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
            font-size: 14px;
            line-height: 20px;
            font-weight: bold;
            color: #1f2937;
            letter-spacing: 1px;
            white-space: nowrap;
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
        return (NAME_ROW % (MONO, 8, name)) + "\n" + (LOGO_ROW % (10, lockup(b)))
    return (LOGO_ROW % (10, lockup(b))) + "\n" + (NAME_ROW % (MONO, 8, name))



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
      width="700"
      style="
        width: 700px;
        max-width: 700px;
        padding: 16px;
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
            line-height: 22px;
            font-weight: 700;
            color: {accent};
            padding-bottom: 8px;
            white-space: nowrap;
          "
        >
          {services}
        </td>
      </tr>

      <!-- DIVIDER -->
      <tr>
        <td style="padding-bottom: 9px">
          <div style="width: 24px; height: 3px; background: {accent}"></div>
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
            padding-bottom: 14px;
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
        # People show the wa.me URL beside the WhatsApp icon.
        pb.setdefault("wa_raw_link", True)
        path = os.path.join(pdir, b["file"])
        with io.open(path, "w", encoding="utf-8") as f:
            f.write(render(pb, person["name"], person.get("name_first", False)))
        print("wrote", os.path.normpath(path))
