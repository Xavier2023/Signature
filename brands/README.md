# Clearer Group — master email signatures

Six brand masters. Regenerate them all with:

    python3 ../build-signatures.py

Edit `../build-signatures.py` (the `BRANDS` list) rather than the HTML — the
HTML files are generated output.

## How the dark-mode handling works

The old signatures embedded the whole lockup as one flat PNG with black text
baked in, so the wordmark disappeared against a dark background. These use:

* **leaf mark** — a hosted transparent PNG (works on any background)
* **wordmark** — live HTML text, so `prefers-color-scheme: dark` flips it
  black → white

Honoured by Apple Mail (macOS/iOS) and Outlook.com (`[data-ogsc]`). Gmail
applies its own inversion, which the black-on-transparent default survives.

## Hosted assets

| Brand | Mark |
|---|---|
| Clearer | `https://www.clearer.ae/logo.png` |
| Clearerpay | `https://www.clearer.ae/logo.png` |
| Clearer Metals | `https://www.clearer.ae/Modify_leaf_logo_metallic_finish_202608131313-Photoroom%201.png` |
| Clearer Outsourcing | `https://www.cleareroutsourcing.com/logo.png` |
| Swetche | `https://www.swetche.com/logo512x512.png` |
| Frirosa | `https://www.frirosa.com/logo512x512.png` |

All verified live (HTTP 200, real PNG). Flags come from `flagcdn.com`.

**Pending deploy:** `dubai-chamber.png` was added to `Clearerae/public/` and
`ClearerMetals/public/`. The Clearer Metals signature points at
`https://www.clearer.ae/dubai-chamber.png`, which 404s until clearer.ae is
redeployed.

## Per person

Replace `FULL NAME – JOB TITLE`. Everything else is company-level and should
stay as-is.

## Preview

Open `preview.html` for all six side by side in light and dark.
