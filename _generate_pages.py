#!/usr/bin/env python3
"""One-shot static HTML generator. Run from repo root."""
from pathlib import Path

WA = "919579321728"
TEL1 = "+919579321728"
TEL2 = "+918830055862"
PHONE1 = "+91 95793 21728"
PHONE2 = "+91 88300 55862"
EMAIL = "sawariya.goacarentals@gmail.com"
SITE = "https://sawariyagoacarentals.com"
MAP = "https://maps.google.com/maps?q=15.506216049194336%2C73.8008041381836&amp;z=17&amp;hl=en"
MAP_EMBED = "https://maps.google.com/maps?q=15.506216049194336,73.8008041381836&amp;z=16&amp;output=embed"

WA_SVG = '''<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.61.14-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.5 0 1.47 1.07 2.9 1.22 3.1.15.2 2.1 3.2 5.1 4.49.71.3 1.27.49 1.7.63.72.23 1.37.2 1.88.12.58-.09 1.76-.72 2-1.42.25-.7.25-1.29.18-1.42-.08-.12-.28-.2-.58-.35zM12.05 21.8h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.82 9.82 0 0 1-1.51-5.26c0-5.44 4.43-9.87 9.89-9.87a9.8 9.8 0 0 1 6.99 2.9 9.82 9.82 0 0 1 2.89 6.99c0 5.44-4.44 9.87-9.88 9.87zm8.4-18.28A11.8 11.8 0 0 0 12.04 0C5.46 0 .1 5.35.1 11.93c0 2.1.55 4.16 1.6 5.97L0 24l6.24-1.64a11.93 11.93 0 0 0 5.8 1.48h.01c6.58 0 11.94-5.35 11.94-11.93 0-3.19-1.24-6.19-3.54-8.39z"/></svg>'''
PHONE_SVG = '''<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'''


def head(title, description, canonical, og_title, json_ld, extra="", preload_hero=False, robots="index, follow"):
    preload = ""
    if preload_hero:
        preload = '''  <link rel="preload" as="image" type="image/webp" href="images/hero-goa.webp" imagesrcset="images/hero-goa-800.webp 800w, images/hero-goa.webp 1600w" imagesizes="100vw" fetchpriority="high" />
'''
    return f'''<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="author" content="Sawariya Car and Bike Rentals Goa" />
  <meta name="robots" content="{robots}" />
  <meta name="geo.region" content="IN-GA" />
  <meta name="geo.placename" content="Nerul, Bardez, Goa" />
  <meta name="geo.position" content="15.506216;73.800804" />
  <meta name="ICBM" content="15.506216, 73.800804" />
  <link rel="canonical" href="{canonical}" />
  <link rel="alternate" hreflang="en-IN" href="{canonical}" />
  <link rel="alternate" hreflang="x-default" href="{SITE}/" />

  <link rel="icon" href="/favicon.ico?v=4" sizes="any" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg?v=4" />
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png?v=4" />
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png?v=4" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=4" />
  <link rel="manifest" href="/site.webmanifest?v=4" />
  <meta name="theme-color" content="#0e6e7c" />
  <meta name="msapplication-TileColor" content="#0e6e7c" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="{og_title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{SITE}/images/hero-goa.jpg" />
  <meta property="og:image:alt" content="North Goa coastline near Candolim and Nerul at golden hour" />
  <meta property="og:image:width" content="1600" />
  <meta property="og:image:height" content="1200" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:site_name" content="Sawariya Car &amp; Bike Rentals Goa" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{og_title}" />
  <meta name="twitter:description" content="{description}" />
  <meta name="twitter:image" content="{SITE}/images/hero-goa.jpg" />
  <meta name="twitter:image:alt" content="North Goa coastline near Candolim and Nerul at golden hour" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&amp;family=Fraunces:ital,wght@0,700;1,600&amp;display=swap" rel="stylesheet" />
{preload}  <link rel="stylesheet" href="styles.css" />
{extra}  {json_ld}
</head>
'''


def nav(active="home"):
    def item(key, href, label):
        cur = ' aria-current="page"' if active == key else ""
        return f'        <li><a href="{href}"{cur}>{label}</a></li>'
    return f'''  <a class="skip-link" href="#main">Skip to content</a>
  <header class="nav" id="nav">
    <div class="nav-inner">
      <a href="index.html" class="logo" aria-label="Sawariya Goa Rentals home">
        <img class="logo-mark" src="images/logo-mark-nav.png?v=4" width="42" height="42" alt="" decoding="async" />
        <span class="logo-text">Sawariya <em>Goa</em><small>Car &amp; bike rentals</small></span>
      </a>
      <button class="menu-btn" id="menuBtn" aria-label="Toggle menu" aria-expanded="false" type="button">
        <span></span><span></span><span></span>
      </button>
      <ul class="nav-links" id="navLinks">
{item("fleet", "index.html#fleet", "Fleet &amp; rates")}
{item("bikes", "bike-rental-goa.html", "Bikes")}
{item("cars", "self-drive-car-rental-goa.html", "Cars")}
{item("taxi", "airport-taxi-goa.html", "Taxi")}
{item("areas", "candolim-calangute-baga.html", "North Goa")}
{item("faq", "index.html#faq", "FAQ")}
{item("contact", "index.html#contact", "Contact")}
        <li><a class="nav-cta" href="https://wa.me/{WA}?text=Hi%20Sawariya!%20I%27d%20like%20to%20rent%20a%20vehicle%20in%20Goa." target="_blank" rel="noopener noreferrer">
          {WA_SVG}
          Book on WhatsApp
        </a></li>
      </ul>
    </div>
  </header>
'''


def cta_footer():
    return f'''  <div class="cta-band">
    <h2>Susegad starts with the right ride</h2>
    <p>Tell us your dates and we will have your bike or car ready — in Nerul or at your hotel door in Candolim, Calangute or Baga.</p>
    <div class="hero-actions">
      <a class="btn btn-wa" href="https://wa.me/{WA}?text=Hi%20Sawariya!%20I%27d%20like%20to%20book%20a%20vehicle.%20My%20dates%3A%20" target="_blank" rel="noopener noreferrer">{WA_SVG} Book on WhatsApp</a>
      <a class="btn btn-ghost" href="tel:{TEL2}">{PHONE_SVG} {PHONE2}</a>
    </div>
  </div>

  <footer>
    <div class="footer-grid">
      <div>
        <div class="footer-brand" style="align-items:flex-start;text-align:left">
          <img class="footer-logo" src="images/logo-mark-192.png?v=4" width="72" height="72" alt="Sawariya Goa logo" loading="lazy" decoding="async" />
          <strong>Sawariya Car &amp; Bike Rentals Goa</strong>
        </div>
        <p>Near Mahadev Temple, H.No. 84, Nerul, Bardez, Goa 403114</p>
        <p style="margin-top:0.6rem"><span class="hours-chip">Open 8:00 am – 9:00 pm daily</span></p>
      </div>
      <div>
        <h3>Rentals</h3>
        <ul>
          <li><a href="bike-rental-goa.html">Bike rental in Goa</a></li>
          <li><a href="self-drive-car-rental-goa.html">Self drive car rental</a></li>
          <li><a href="airport-taxi-goa.html">Airport taxi Goa</a></li>
          <li><a href="candolim-calangute-baga.html">Candolim, Calangute &amp; Baga</a></li>
          <li><a href="index.html#fleet">Full fleet &amp; rates</a></li>
        </ul>
      </div>
      <div>
        <h3>Visit</h3>
        <ul>
          <li><a href="index.html#how">How booking works</a></li>
          <li><a href="index.html#faq">FAQ</a></li>
          <li><a href="index.html#contact">Map &amp; contact</a></li>
          <li><a href="{MAP}" target="_blank" rel="noopener noreferrer">Google Maps</a></li>
          <li><a href="privacy.html">Privacy</a></li>
        </ul>
      </div>
      <div>
        <h3>Call or message</h3>
        <ul>
          <li><a href="tel:{TEL1}">{PHONE1}</a></li>
          <li><a href="tel:{TEL2}">{PHONE2}</a></li>
          <li><a href="mailto:{EMAIL}">Email us</a></li>
          <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener noreferrer">WhatsApp</a></li>
        </ul>
      </div>
    </div>
    <p class="footer-note">Self-drive bike and car rentals plus yellow-board taxis from Nerul, North Goa — Yamaha Fascino, Royal Enfield Himalayan, Baleno, i20, Creta, Ertiga, Innova Hycross, Mahindra Thar, and hotel delivery across Candolim, Calangute, Baga, Sinquerim and Panjim.</p>
    <p>&copy; <span id="year"></span> Sawariya Goa Car Rentals. All rights reserved.</p>
  </footer>

  <nav class="action-bar" aria-label="Quick contact">
    <a class="ab-call" href="tel:{TEL1}">{PHONE_SVG} Call</a>
    <a class="ab-wa" href="https://wa.me/{WA}?text=Hi%20Sawariya!%20I%27d%20like%20to%20rent%20a%20vehicle." target="_blank" rel="noopener noreferrer">{WA_SVG} WhatsApp</a>
  </nav>
  <script src="site.js" defer></script>
</body>
</html>
'''


HOME_SCHEMA = f'''
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": ["AutoRental", "LocalBusiness"],
        "@id": "{SITE}/#business",
        "name": "Sawariya Car & Bike Rentals Goa",
        "alternateName": "Sawariya Goa Rentals",
        "image": ["{SITE}/images/logo-mark-512.png", "{SITE}/images/hero-goa.jpg"],
        "logo": "{SITE}/images/logo-mark-512.png",
        "url": "{SITE}/",
        "telephone": ["{TEL1}", "{TEL2}"],
        "email": "{EMAIL}",
        "priceRange": "₹500 - ₹4,499 per day",
        "currenciesAccepted": "INR",
        "paymentAccepted": ["Cash", "UPI"],
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "Near Mahadev Temple, H.No. 84",
          "addressLocality": "Nerul",
          "addressRegion": "Goa",
          "postalCode": "403114",
          "addressCountry": "IN"
        }},
        "geo": {{
          "@type": "GeoCoordinates",
          "latitude": 15.506216,
          "longitude": 73.800804
        }},
        "areaServed": [
          "Nerul", "Candolim", "Calangute", "Baga", "Sinquerim", "Panjim",
          "Anjuna", "Vagator", "North Goa", "Mopa Airport", "Dabolim Airport"
        ],
        "openingHoursSpecification": {{
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
          "opens": "08:00",
          "closes": "21:00"
        }},
        "hasMap": "https://maps.google.com/maps?q=15.506216049194336,73.8008041381836&z=17",
        "knowsLanguage": ["en", "hi", "mr", "kok"],
        "makesOffer": [
          {{"@type": "Offer", "name": "Yamaha Fascino scooter rental", "price": "500", "priceCurrency": "INR", "availability": "https://schema.org/InStock"}},
          {{"@type": "Offer", "name": "Royal Enfield Himalayan rental", "price": "1299", "priceCurrency": "INR"}},
          {{"@type": "Offer", "name": "Maruti Baleno self-drive", "price": "1399", "priceCurrency": "INR"}},
          {{"@type": "Offer", "name": "Hyundai i20 self-drive", "price": "1399", "priceCurrency": "INR"}},
          {{"@type": "Offer", "name": "Maruti Ertiga self-drive", "price": "2499", "priceCurrency": "INR"}},
          {{"@type": "Offer", "name": "Hyundai Creta self-drive", "price": "3499", "priceCurrency": "INR"}},
          {{"@type": "Offer", "name": "Innova Hycross self-drive", "price": "3999", "priceCurrency": "INR"}},
          {{"@type": "Offer", "name": "Mahindra Thar self-drive", "price": "4499", "priceCurrency": "INR"}}
        ]
      }},
      {{
        "@type": "TaxiService",
        "@id": "{SITE}/airport-taxi-goa.html#service",
        "name": "Sawariya Goa Taxi",
        "provider": {{"@id": "{SITE}/#business"}},
        "url": "{SITE}/airport-taxi-goa.html",
        "areaServed": ["North Goa", "South Goa", "Mopa Airport", "Dabolim Airport"],
        "telephone": "{TEL1}"
      }},
      {{
        "@type": "WebSite",
        "@id": "{SITE}/#website",
        "url": "{SITE}/",
        "name": "Sawariya Car & Bike Rentals Goa",
        "publisher": {{"@id": "{SITE}/#business"}},
        "inLanguage": "en-IN"
      }},
      {{
        "@type": "FAQPage",
        "@id": "{SITE}/#faq",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "Do you offer taxi services as well?",
            "acceptedAnswer": {{"@type": "Answer", "text": "Yes — AC sedan taxis with a yellow TAXI board for airport transfers from Mopa and Dabolim, hotel pickups and day trips across Goa. Message us on WhatsApp with pickup, drop and time for a fixed quote."}}
          }},
          {{
            "@type": "Question",
            "name": "What documents do I need to rent a bike or car in Goa?",
            "acceptedAnswer": {{"@type": "Answer", "text": "A valid driving licence (Indian or international) and one government photo ID such as Aadhaar or passport. Foreign nationals need a passport and an International Driving Permit."}}
          }},
          {{
            "@type": "Question",
            "name": "Do you deliver vehicles to hotels in Candolim, Calangute or Baga?",
            "acceptedAnswer": {{"@type": "Answer", "text": "Yes. We deliver across North Goa including Candolim, Calangute, Baga, Sinquerim and Panjim. Share your hotel location on WhatsApp and we will confirm delivery time and charges."}}
          }},
          {{
            "@type": "Question",
            "name": "Are helmets included with bike rentals?",
            "acceptedAnswer": {{"@type": "Answer", "text": "Yes, we provide helmets free of charge with every two-wheeler. Helmets are mandatory in Goa for both rider and pillion."}}
          }},
          {{
            "@type": "Question",
            "name": "What is the fuel policy?",
            "acceptedAnswer": {{"@type": "Answer", "text": "Vehicles are handed over with fuel and should be returned with the same level. Petrol pumps are available throughout Nerul, Candolim and Calangute."}}
          }},
          {{
            "@type": "Question",
            "name": "How do I book a vehicle?",
            "acceptedAnswer": {{"@type": "Answer", "text": "Message us on WhatsApp at {PHONE1} with your dates and preferred vehicle, or simply call. Booking takes about two minutes."}}
          }},
          {{
            "@type": "Question",
            "name": "Do you pick up from Mopa or Dabolim airport?",
            "acceptedAnswer": {{"@type": "Answer", "text": "Yes. We run yellow-board taxi transfers to and from Manohar International Airport (Mopa) and Goa International Airport (Dabolim). Share your flight time on WhatsApp for a fixed quote."}}
          }},
          {{
            "@type": "Question",
            "name": "Do you offer weekly discounts on bike and car rental in Goa?",
            "acceptedAnswer": {{"@type": "Answer", "text": "Yes. Ask on WhatsApp for weekly rates — longer hires on Fascino scooters, hatchbacks and 7-seaters are usually cheaper per day than a single-day booking."}}
          }}
        ]
      }}
    ]
  }}
  </script>
'''


def vcard(cat, img, alt, tag, title, models, feats, price_html, wa_text, btn):
    src_webp = img.replace(".jpg", ".webp")
    return f'''        <article class="vcard reveal" data-fleet="{cat}">
          <div class="vcard-img">
            <picture>
              <source type="image/webp" srcset="{src_webp}" />
              <img src="{img}" alt="{alt}" width="800" height="534" loading="lazy" decoding="async" />
            </picture>
            <span class="vcard-tag">{tag}</span>
          </div>
          <div class="vcard-body">
            <h3>{title}</h3>
            <p class="vcard-models">{models}</p>
            <ul class="vcard-feats">{feats}</ul>
            <div class="vcard-price{"" if "<div" not in price_html else " dual"}">{price_html}</div>
            <a class="btn btn-wa" href="https://wa.me/{WA}?text={wa_text}" target="_blank" rel="noopener noreferrer">{btn}</a>
          </div>
        </article>'''


index_body = f'''
<body>
{nav("home")}
  <main id="main">
  <section class="hero">
    <div class="hero-bg">
      <picture>
        <source type="image/webp" srcset="images/hero-goa-800.webp 800w, images/hero-goa.webp 1600w" sizes="100vw" />
        <img
          src="images/hero-goa.jpg"
          srcset="images/hero-goa-800.jpg 800w, images/hero-goa.jpg 1600w"
          sizes="100vw"
          alt="Palm-lined beach coastline in North Goa at golden hour, near Candolim and Nerul"
          width="1600"
          height="1200"
          fetchpriority="high"
          decoding="async"
        />
      </picture>
    </div>
    <div class="hero-content">
      <div class="hero-badge">Open today · 8am–9pm · Nerul, Bardez · North Goa</div>
      <p class="hero-kicker">Ride the Sunshine State your way</p>
      <h1>Bike &amp; car rental in <em>North Goa</em></h1>
      <p class="hero-lead">
        Self-drive scooters from <strong>₹500/day</strong> and cars from <strong>₹1,399/day</strong>. Pick up in Nerul — 4 km from Candolim — or get hotel delivery to Calangute, Baga and Panjim. Yellow-board taxis to <strong>Mopa</strong> and <strong>Dabolim</strong> as well.
      </p>
      <div class="hero-actions">
        <a class="btn btn-wa" href="https://wa.me/{WA}?text=Hi%20Sawariya!%20I%27d%20like%20to%20rent%20a%20vehicle%20in%20Goa.%20My%20dates%3A%20" target="_blank" rel="noopener noreferrer">
          {WA_SVG.replace('width="16"', 'width="18"')} Book on WhatsApp
        </a>
        <a class="btn btn-ghost" href="tel:{TEL1}">
          {PHONE_SVG} {PHONE1}
        </a>
      </div>
      <div class="hero-stats">
        <div class="hero-stat"><strong>₹500</strong><span>scooters per day</span></div>
        <div class="hero-stat"><strong>2 min</strong><span>WhatsApp booking</span></div>
        <div class="hero-stat"><strong>4 km</strong><span>to Candolim Beach</span></div>
        <div class="hero-stat"><strong>Free</strong><span>helmets included</span></div>
      </div>
    </div>
  </section>

  <div class="trust">
    <div class="trust-row">
      <div class="trust-item"><span class="trust-dot" aria-hidden="true"></span><div>Local Nerul pickup<strong><span>Near Mahadev Temple, Bardez</span></strong></div></div>
      <div class="trust-item"><span class="trust-dot" aria-hidden="true"></span><div>Hotel delivery<strong><span>Candolim, Calangute, Baga, Panjim</span></strong></div></div>
      <div class="trust-item"><span class="trust-dot" aria-hidden="true"></span><div>Airport taxis<strong><span>Mopa &amp; Dabolim, fixed WhatsApp quote</span></strong></div></div>
      <div class="trust-item"><span class="trust-dot" aria-hidden="true"></span><div>Open every day<strong><span>8:00 am – 9:00 pm</span></strong></div></div>
    </div>
  </div>

  <section class="fleet" id="fleet">
    <div class="wrap">
      <div class="fleet-header reveal">
        <div>
          <span class="section-label">Fleet &amp; rates</span>
          <h2 class="section-title">Pick your Goa ride</h2>
          <p class="section-sub">Yamaha Fascino &amp; Royal Enfield Himalayan for two wheels; Baleno, i20, Creta, Ertiga, Innova Hycross &amp; Thar for four. Clear per-day rates — ask for weekly discounts.</p>
        </div>
        <p class="fleet-note">Rates are indicative &amp; vary by season — confirm on WhatsApp.</p>
      </div>
      <div class="fleet-filters" role="group" aria-label="Filter fleet">
        <button type="button" class="is-active" data-fleet-filter="all" aria-pressed="true">All</button>
        <button type="button" data-fleet-filter="bike" aria-pressed="false">Bikes</button>
        <button type="button" data-fleet-filter="car" aria-pressed="false">Cars</button>
      </div>
      <div class="fleet-grid">
{vcard("bike","images/yamaha-fascino.jpg","Yamaha Fascino scooter for rent in North Goa","Scooter","Yamaha Fascino","Automatic scooter · city &amp; beach runs","<li>2 helmets free</li><li>Great mileage</li><li>Easy parking</li>","<strong>₹500</strong><span>/ day onwards</span>","Hi!%20I%27d%20like%20to%20rent%20a%20Yamaha%20Fascino.%20My%20dates%3A%20","Book Fascino")}
{vcard("bike","images/royal-enfield-himalayan.jpg","Royal Enfield Himalayan bike for rent in Goa","Adventure","Royal Enfield Himalayan","Touring bike · coast &amp; hinterland","<li>2 helmets free</li><li>Long rides</li><li>Rugged build</li>","<strong>₹1,299</strong><span>/ day</span>","Hi!%20I%27d%20like%20to%20rent%20a%20Royal%20Enfield%20Himalayan.%20My%20dates%3A%20","Book Himalayan")}
{vcard("car","images/maruti-baleno.jpg","Maruti Baleno hatchback for rent in Goa","Hatchback","Maruti Baleno","Automatic / Manual · AC · self-drive","<li>AC</li><li>4–5 seats</li><li>Auto or manual</li>",'''<div class="row"><strong>₹1,399</strong><span> manual / day</span></div>
              <div class="row"><strong>₹1,599</strong><span> auto / day</span></div>''',"Hi!%20I%27d%20like%20to%20rent%20a%20Baleno%20(manual%20%E2%82%B91399%20%2F%20auto%20%E2%82%B91599).%20My%20dates%3A%20","Book Baleno")}
{vcard("car","images/hyundai-i20.jpg","Hyundai i20 hatchback for rent in Goa","Hatchback","Hyundai i20","Automatic / Manual · AC · self-drive","<li>AC</li><li>4–5 seats</li><li>Auto or manual</li>",'''<div class="row"><strong>₹1,399</strong><span> manual / day</span></div>
              <div class="row"><strong>₹1,599</strong><span> auto / day</span></div>''',"Hi!%20I%27d%20like%20to%20rent%20an%20i20%20(manual%20%E2%82%B91399%20%2F%20auto%20%E2%82%B91599).%20My%20dates%3A%20","Book i20")}
{vcard("car","images/hyundai-creta.jpg","Hyundai Creta SUV for rent in Goa","SUV","Hyundai Creta","Compact SUV · AC · self-drive","<li>AC</li><li>5 seats</li><li>Highway ready</li>","<strong>₹3,499</strong><span>/ day</span>","Hi!%20I%27d%20like%20to%20rent%20a%20Creta.%20My%20dates%3A%20","Book Creta")}
{vcard("car","images/innova-hycross.jpg","Toyota Innova Hycross for rent in Goa","MPV","Innova Hycross","Premium MPV · AC · self-drive","<li>AC</li><li>7 seats</li><li>Family trips</li>","<strong>₹3,999</strong><span>/ day</span>","Hi!%20I%27d%20like%20to%20rent%20an%20Innova%20Hycross.%20My%20dates%3A%20","Book Hycross")}
{vcard("car","images/maruti-ertiga.jpg","Maruti Ertiga MPV for rent in Goa","MPV","Maruti Ertiga","7-seater MPV · AC · self-drive","<li>AC</li><li>7 seats</li><li>Family trips</li>","<strong>₹2,499</strong><span>/ day</span>","Hi!%20I%27d%20like%20to%20rent%20an%20Ertiga%20(%E2%82%B92499%2Fday).%20My%20dates%3A%20","Book Ertiga")}
{vcard("car","images/mahindra-thar.jpg","Mahindra Thar SUV for rent in Goa","SUV","Mahindra Thar","Off-road SUV · AC · self-drive","<li>AC</li><li>4 seats</li><li>Adventure ready</li>","<strong>₹4,499</strong><span>/ day</span>","Hi!%20I%27d%20like%20to%20rent%20a%20Mahindra%20Thar%20(%E2%82%B94499%2Fday).%20My%20dates%3A%20","Book Thar")}
      </div>
    </div>
  </section>

  <section class="taxi" id="taxi">
    <div class="wrap">
      <div class="taxi-layout">
        <div class="taxi-visual reveal">
          <picture>
            <source type="image/webp" srcset="images/goa-taxi.webp" />
            <img src="images/goa-taxi.jpg" alt="White sedan Goa taxi with yellow TAXI roof board for airport transfers" width="800" height="534" loading="lazy" decoding="async" />
          </picture>
        </div>
        <div class="taxi-copy reveal">
          <span class="section-label">Taxi services</span>
          <h2 class="section-title">Airport taxi Goa, when you need a driver</h2>
          <p class="section-sub">White sedan taxis with a yellow TAXI board — pickups from <a href="airport-taxi-goa.html">Mopa (Manohar) and Dabolim</a>, hotel transfers, and day trips across North &amp; South Goa. Fixed quote on WhatsApp before you ride.</p>
          <ul class="taxi-feats">
            <li>Mopa &amp; Dabolim transfers</li>
            <li>Hotel pickups</li>
            <li>Local &amp; outstation</li>
            <li>AC sedan · local drivers</li>
          </ul>
          <div class="taxi-actions">
            <a class="btn btn-wa" href="https://wa.me/{WA}?text=Hi%20Sawariya!%20I%20need%20a%20taxi.%20Pickup%3A%20%20Drop%3A%20%20Date%2Ftime%3A%20" target="_blank" rel="noopener noreferrer">Book a taxi</a>
            <a class="btn btn-sunset" href="tel:{TEL1}">Call {PHONE1}</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="explore" id="explore">
    <div class="wrap">
      <div class="reveal">
        <span class="section-label">Why rent in Nerul</span>
        <h2 class="section-title">Everything in North Goa, minutes away</h2>
        <p class="section-sub">Nerul sits at the heart of North Goa’s coast. Pick up near Mahadev Temple and you are at Candolim before your playlist warms up. We also <a href="candolim-calangute-baga.html" style="color:var(--mango)">deliver to hotels</a> along the beach belt.</p>
      </div>
      <div class="explore-grid">
        <div class="spot reveal"><div class="spot-dist">2 km</div><h3>Coco Beach</h3><p>Quiet river beach with dolphin-spotting boats.</p></div>
        <div class="spot reveal"><div class="spot-dist">3 km</div><h3>Reis Magos Fort</h3><p>Restored 16th-century fort with river views.</p></div>
        <div class="spot reveal"><div class="spot-dist">4 km</div><h3>Candolim Beach</h3><p>Laid-back sands, shacks and water sports.</p></div>
        <div class="spot reveal"><div class="spot-dist">5 km</div><h3>Fort Aguada &amp; Sinquerim</h3><p>Iconic lighthouse fort above the sea.</p></div>
        <div class="spot reveal"><div class="spot-dist">7 km</div><h3>Calangute Beach</h3><p>The “Queen of Beaches” — buzzing all day.</p></div>
        <div class="spot reveal"><div class="spot-dist">9 km</div><h3>Baga Beach</h3><p>Nightlife, Tito’s Lane and beach clubs.</p></div>
        <div class="spot reveal"><div class="spot-dist">10 km</div><h3>Panjim &amp; Fontainhas</h3><p>Latin quarter lanes, casinos and river cruises.</p></div>
        <div class="spot reveal"><div class="spot-dist">14 km</div><h3>Anjuna &amp; Vagator</h3><p>Flea markets, cliffs and sunset parties.</p></div>
      </div>
      <div class="explore-cta reveal">
        <a class="btn btn-sunset" href="https://wa.me/{WA}?text=Hi!%20Planning%20a%20North%20Goa%20trip%20%E2%80%94%20what%20vehicles%20are%20available%3F" target="_blank" rel="noopener noreferrer">Plan my trip</a>
        <p>Going south to Palolem or inland to Dudhsagar? Ask us — we will suggest the right vehicle.</p>
      </div>
    </div>
  </section>

  <section class="how" id="how">
    <div class="wrap">
      <div class="reveal">
        <span class="section-label">How it works</span>
        <h2 class="section-title">On the road in three steps</h2>
      </div>
      <div class="how-grid">
        <div class="step reveal">
          <div class="step-num">1</div>
          <h3>WhatsApp your dates</h3>
          <p>Message us your travel dates and preferred vehicle. We confirm availability and rate within minutes.</p>
        </div>
        <div class="step reveal">
          <div class="step-num">2</div>
          <h3>Show your documents</h3>
          <p>A valid driving licence plus one photo ID (Aadhaar or passport). Foreign visitors: passport + International Driving Permit.</p>
        </div>
        <div class="step reveal">
          <div class="step-num">3</div>
          <h3>Pick up &amp; ride</h3>
          <p>Collect in Nerul or get hotel delivery across North Goa. Helmets included with every bike — then the coast is yours.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="why" id="why">
    <div class="wrap">
      <div class="reveal">
        <span class="section-label">Why Sawariya</span>
        <h2 class="section-title">Local, honest, hassle-free</h2>
      </div>
      <div class="why-grid">
        <div class="why-card reveal">
          <div class="why-icon" aria-hidden="true">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <h3>Truly local</h3>
          <p>We are from Nerul. Ask us for shortcuts, quiet beaches and where the locals actually eat.</p>
        </div>
        <div class="why-card reveal">
          <div class="why-icon" aria-hidden="true">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
          </div>
          <h3>No apps, no forms</h3>
          <p>Book the way Goa works — one WhatsApp message or a phone call. Done in two minutes.</p>
        </div>
        <div class="why-card reveal">
          <div class="why-icon" aria-hidden="true">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          </div>
          <h3>Well-kept vehicles</h3>
          <p>Serviced regularly, cleaned before every handover, with paperwork in order.</p>
        </div>
        <div class="why-card reveal">
          <div class="why-icon" aria-hidden="true">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          </div>
          <h3>Hotel delivery</h3>
          <p>Staying in Candolim, Calangute or Baga? We can bring the vehicle to you.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="prose" id="about">
    <div class="wrap">
      <div class="reveal">
        <span class="section-label">Self-drive from Nerul</span>
        <h2 class="section-title">A local desk for bikes, cars and taxis</h2>
      </div>
      <div class="prose-grid reveal">
        <div>
          <p>Sawariya is a neighbourhood rental desk in Nerul, Bardez — not a pan-India app. If you need a <a href="bike-rental-goa.html">scooter or Himalayan in Goa</a>, a <a href="self-drive-car-rental-goa.html">self-drive hatchback, Ertiga, Creta, Hycross or Thar</a>, or a <a href="airport-taxi-goa.html">yellow-board taxi from Mopa or Dabolim</a>, you message us, we confirm the rate, and you ride.</p>
          <p>Nerul sits between Coco Beach and Fort Aguada, about 4 km from Candolim Beach and 7 km from Calangute. That means less time stuck on the beach road at check-in, and an easy first hop to Sinquerim, Reis Magos, Panjim or Anjuna. Staying on the strip? We deliver to hotels in <a href="candolim-calangute-baga.html">Candolim, Calangute and Baga</a>.</p>
          <p>Bring a valid driving licence and photo ID. Foreign visitors need a passport plus an International Driving Permit. Helmets are free with every bike — wear them; Goa police check the Candolim–Calangute road often. Fuel is same-to-same, and weekly hires are usually cheaper per day: ask when you WhatsApp your dates.</p>
        </div>
        <ul class="link-list">
          <li><a href="bike-rental-goa.html"><strong>Bike rental in Goa</strong><span>Fascino from ₹500/day · Himalayan ₹1,299/day · 2 helmets</span></a></li>
          <li><a href="self-drive-car-rental-goa.html"><strong>Self drive car rental Goa</strong><span>Baleno &amp; i20 from ₹1,399 · Ertiga, Creta, Hycross, Thar</span></a></li>
          <li><a href="airport-taxi-goa.html"><strong>Airport taxi Goa</strong><span>Mopa &amp; Dabolim · fixed quote before you ride</span></a></li>
          <li><a href="candolim-calangute-baga.html"><strong>Hotel delivery, North Goa</strong><span>Candolim 4 km · Calangute 7 km · Baga 9 km</span></a></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="faq" id="faq">
    <div class="wrap">
      <div class="reveal">
        <span class="section-label">FAQ</span>
        <h2 class="section-title">Good to know before you ride</h2>
      </div>
      <div class="faq-list reveal">
        <details class="faq-item">
          <summary>Do you offer taxi services as well?</summary>
          <p>Yes — AC sedan taxis with a yellow TAXI board for airport transfers from Mopa and Dabolim, hotel pickups and day trips across Goa. Message us on WhatsApp with pickup, drop and time for a fixed quote.</p>
        </details>
        <details class="faq-item">
          <summary>What documents do I need to rent a bike or car in Goa?</summary>
          <p>A valid driving licence (Indian or international) and one government photo ID such as Aadhaar or passport. Foreign nationals need a passport and an International Driving Permit.</p>
        </details>
        <details class="faq-item">
          <summary>Do you deliver vehicles to hotels in Candolim, Calangute or Baga?</summary>
          <p>Yes — we deliver across North Goa including Candolim, Calangute, Baga, Sinquerim and Panjim. Share your hotel location on WhatsApp and we will confirm the delivery time and charges.</p>
        </details>
        <details class="faq-item">
          <summary>Are helmets included with bike rentals?</summary>
          <p>Yes, helmets are free with every two-wheeler. They are mandatory in Goa for both rider and pillion, and police checks are common on beach roads — so wear them.</p>
        </details>
        <details class="faq-item">
          <summary>What is the fuel policy?</summary>
          <p>Vehicles are handed over with fuel and should be returned at the same level. Petrol pumps are easy to find in Nerul, Candolim and Calangute.</p>
        </details>
        <details class="faq-item">
          <summary>Do you pick up from Mopa or Dabolim airport?</summary>
          <p>Yes. We run yellow-board taxi transfers to and from Manohar International Airport (Mopa) and Goa International Airport (Dabolim). Share your flight time on WhatsApp for a fixed quote.</p>
        </details>
        <details class="faq-item">
          <summary>Do you offer weekly discounts?</summary>
          <p>Yes — longer hires on scooters, hatchbacks and 7-seaters are usually cheaper per day. Message your dates and we will quote the weekly rate.</p>
        </details>
        <details class="faq-item">
          <summary>How do I book?</summary>
          <p>Message us on WhatsApp at {PHONE1} with your dates and preferred vehicle, or just call {PHONE2}. No app, no forms — booking takes about two minutes.</p>
        </details>
      </div>
    </div>
  </section>

  <section class="contact" id="contact">
    <div class="wrap">
      <div class="reveal">
        <span class="section-label">Contact</span>
        <h2 class="section-title">Find us in Nerul</h2>
        <p class="section-sub">Near Mahadev Temple — 10 minutes from Candolim, on the road between Coco Beach and Fort Aguada. Open 8:00 am – 9:00 pm every day.</p>
      </div>
      <div class="contact-grid">
        <div class="contact-card reveal">
          <div class="contact-item">
            <div class="contact-icon" aria-hidden="true">{PHONE_SVG}</div>
            <div>
              <h3>Phone</h3>
              <a href="tel:{TEL1}">{PHONE1}</a>
              <a href="tel:{TEL2}">{PHONE2}</a>
            </div>
          </div>
          <div class="contact-item">
            <div class="contact-icon" aria-hidden="true">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            </div>
            <div>
              <h3>Email</h3>
              <a href="mailto:{EMAIL}">{EMAIL}</a>
            </div>
          </div>
          <div class="contact-item">
            <div class="contact-icon" aria-hidden="true">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            </div>
            <div>
              <h3>Address</h3>
              <address>Near Mahadev Temple, H.No. 84,<br />Nerul, Bardez, Goa 403114</address>
            </div>
          </div>
          <div class="contact-cta-row">
            <a class="btn btn-wa" href="https://wa.me/{WA}?text=Hi%20Sawariya!" target="_blank" rel="noopener noreferrer">WhatsApp</a>
            <a class="btn btn-sunset" href="tel:{TEL1}">Call now</a>
            <a class="btn btn-sea" href="{MAP}" target="_blank" rel="noopener noreferrer">Directions</a>
          </div>
        </div>
        <div class="map-wrap reveal">
          <iframe
            title="Sawariya Car and Bike Rentals Goa — location map, Nerul Bardez"
            src="{MAP_EMBED}"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            allowfullscreen
          ></iframe>
        </div>
      </div>
    </div>
  </section>
  </main>
{cta_footer()}
'''


def page_hero(crumbs, h1, lead, img_alt="Palm-lined beach coastline in North Goa at golden hour"):
    return f'''  <section class="page-hero">
    <div class="hero-bg">
      <picture>
        <source type="image/webp" srcset="images/hero-goa-800.webp 800w, images/hero-goa.webp 1600w" sizes="100vw" />
        <img src="images/hero-goa.jpg" srcset="images/hero-goa-800.jpg 800w, images/hero-goa.jpg 1600w" sizes="100vw" alt="{img_alt}" width="1600" height="1200" fetchpriority="high" decoding="async" />
      </picture>
    </div>
    <div class="hero-content">
      <nav class="crumbs" aria-label="Breadcrumb">{crumbs}</nav>
      <h1>{h1}</h1>
      <p class="hero-lead">{lead}</p>
      <div class="hero-actions" style="margin-bottom:0">
        <a class="btn btn-wa" href="https://wa.me/{WA}?text=Hi%20Sawariya!%20I%27d%20like%20to%20book.%20My%20dates%3A%20" target="_blank" rel="noopener noreferrer">{WA_SVG} WhatsApp to book</a>
        <a class="btn btn-ghost" href="tel:{TEL1}">{PHONE_SVG} {PHONE1}</a>
      </div>
    </div>
  </section>
'''


def breadcrumb_json(items):
    els = []
    for i, (name, url) in enumerate(items, 1):
        els.append(f'''      {{
        "@type": "ListItem",
        "position": {i},
        "name": "{name}",
        "item": "{url}"
      }}''')
    return f'''
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
{',\n'.join(els)}
    ]
  }}
  </script>
'''


def inner_page(filename, title, description, og, active, crumbs_html, h1, lead, article, extra_schema, crumbs_ld):
    html = head(title, description, f"{SITE}/{filename}", og, extra_schema + breadcrumb_json(crumbs_ld), preload_hero=True)
    html += f"<body>\n{nav(active)}\n  <main id=\"main\">\n"
    html += page_hero(crumbs_html, h1, lead)
    html += f'''  <section class="article">
    <div class="wrap">
      <div class="article-body reveal">
{article}
      </div>
    </div>
  </section>
  </main>
{cta_footer()}'''
    Path(filename).write_text(html)
    print("wrote", filename, Path(filename).stat().st_size)


# Homepage
Path("index.html").write_text(
    head(
        "Bike &amp; Car Rental in North Goa | Self Drive from ₹500 | Sawariya",
        "Self-drive bikes from ₹500/day and cars from ₹1,399 in Nerul, North Goa. Hotel delivery to Candolim, Calangute and Baga. Mopa and Dabolim taxis. Book on WhatsApp.",
        f"{SITE}/",
        "Bike & Car Rental in North Goa | Sawariya",
        HOME_SCHEMA,
        extra='',
        preload_hero=True,
    )
    + index_body
)
print("wrote index.html", Path("index.html").stat().st_size)

inner_page(
    "bike-rental-goa.html",
    "Bike Rental in Goa | Fascino ₹500/day &amp; Himalayan | Nerul",
    "Bike rental in North Goa from Nerul. Yamaha Fascino from ₹500/day, Himalayan ₹1,299/day, two helmets free. Pickup near Candolim or hotel delivery.",
    "Bike Rental in Goa | Fascino & Himalayan | Sawariya",
    "bikes",
    '<a href="index.html">Home</a> <span aria-hidden="true">/</span> <span>Bike rental</span>',
    "Bike rental in <em>Goa</em>",
    "Automatic scooters for beach hops, a Himalayan for longer coast runs. Pick up in Nerul — 4 km from Candolim — or we deliver to your hotel.",
    f'''        <p>If you are looking for <strong>bike rental in Goa</strong> without an app or a kiosk on the Calangute main road, Sawariya runs a small fleet from Nerul, Bardez. You WhatsApp your dates, we confirm the bike, and you collect near Mahadev Temple — or we drop it at your hotel in Candolim, Calangute or Baga.</p>
        <h3>What you can rent</h3>
        <table class="rate-table">
          <thead><tr><th>Bike</th><th>Best for</th><th>From</th></tr></thead>
          <tbody>
            <tr><td>Yamaha Fascino</td><td>Town, beach, parking</td><td>₹500 / day</td></tr>
            <tr><td>Royal Enfield Himalayan</td><td>Coast &amp; hinterland</td><td>₹1,299 / day</td></tr>
          </tbody>
        </table>
        <p>The Fascino is the default North Goa scooter: automatic, light, easy on fuel, and simple to park at shacks. The Himalayan is the touring option if you are riding to Anjuna, Vagator, or further into the hinterland. Both come with <strong>two helmets</strong> — rider and pillion. Wear them; checks on the Candolim–Calangute stretch are common.</p>
        <h3>Documents and rules</h3>
        <ul>
          <li>Indian riders: valid driving licence + Aadhaar or other photo ID.</li>
          <li>Foreign visitors: passport + International Driving Permit. A home-country licence alone is not enough in Goa.</li>
          <li>Fuel is same-to-same. Petrol pumps are close in Nerul, Candolim and Calangute.</li>
          <li>Ask on WhatsApp for weekly scooter rates — they are usually lower per day than a one-day hire.</li>
        </ul>
        <p>Need four wheels instead? See <a href="self-drive-car-rental-goa.html">self-drive car rental in Goa</a>. Landing at Mopa or Dabolim and want a driver? Book an <a href="airport-taxi-goa.html">airport taxi</a>.</p>
        <p><a class="btn btn-wa" href="https://wa.me/{WA}?text=Hi!%20I%27d%20like%20to%20rent%20a%20bike%20in%20Goa.%20My%20dates%3A%20" target="_blank" rel="noopener noreferrer">{WA_SVG} Book a bike on WhatsApp</a></p>''',
    f'''
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Bike rental in Goa",
    "serviceType": "Motorcycle and scooter rental",
    "provider": {{"@id": "{SITE}/#business"}},
    "areaServed": ["Nerul", "Candolim", "Calangute", "Baga", "North Goa"],
    "url": "{SITE}/bike-rental-goa.html",
    "offers": [
      {{"@type": "Offer", "name": "Yamaha Fascino", "price": "500", "priceCurrency": "INR"}},
      {{"@type": "Offer", "name": "Royal Enfield Himalayan", "price": "1299", "priceCurrency": "INR"}}
    ]
  }}
  </script>
''',
    [("Home", f"{SITE}/"), ("Bike rental in Goa", f"{SITE}/bike-rental-goa.html")],
)

inner_page(
    "self-drive-car-rental-goa.html",
    "Self Drive Car Rental in Goa | Baleno, Ertiga, Thar | Nerul",
    "Self-drive cars in North Goa from Nerul. Baleno and i20 from ₹1,399/day, Ertiga, Creta, Hycross and Thar. Hotel delivery to Candolim, Calangute and Baga.",
    "Self Drive Car Rental in Goa | Sawariya Nerul",
    "cars",
    '<a href="index.html">Home</a> <span aria-hidden="true">/</span> <span>Self-drive cars</span>',
    "Self-drive car rental in <em>Goa</em>",
    "Hatchbacks from ₹1,399/day, 7-seaters, Creta, Hycross and Thar. Collect in Nerul or get the car at your North Goa hotel.",
    f'''        <p>Sawariya’s <strong>self-drive car rental in Goa</strong> is based in Nerul, Bardez — a 10-minute hop from Candolim. You get a local rate, paperwork in order, and a car that has been cleaned before handover. There is no app: WhatsApp your dates, we confirm the model and the day’s rate (seasonal, so always reconfirm).</p>
        <h3>Current self-drive fleet</h3>
        <table class="rate-table">
          <thead><tr><th>Car</th><th>Seats</th><th>From / day</th></tr></thead>
          <tbody>
            <tr><td>Maruti Baleno (manual / auto)</td><td>4–5</td><td>₹1,399 / ₹1,599</td></tr>
            <tr><td>Hyundai i20 (manual / auto)</td><td>4–5</td><td>₹1,399 / ₹1,599</td></tr>
            <tr><td>Maruti Ertiga</td><td>7</td><td>₹2,499</td></tr>
            <tr><td>Hyundai Creta</td><td>5</td><td>₹3,499</td></tr>
            <tr><td>Innova Hycross</td><td>7</td><td>₹3,999</td></tr>
            <tr><td>Mahindra Thar</td><td>4</td><td>₹4,499</td></tr>
          </tbody>
        </table>
        <p>Couples and pairs usually take a Baleno or i20 for Calangute, Baga and Panjim. Families pick the Ertiga or Hycross for luggage and a Dudhsagar or South Goa day. The Creta is the highway SUV; the Thar is the weekend adventure car — confirm availability early in peak season.</p>
        <h3>How self-drive works here</h3>
        <ul>
          <li>Licence + photo ID (foreign visitors: passport + IDP).</li>
          <li>Fuel returned at the same level.</li>
          <li>Hotel delivery across Candolim, Calangute, Baga, Sinquerim and Panjim — charges confirmed on WhatsApp.</li>
          <li>Weekly discounts on request.</li>
        </ul>
        <p>If you would rather not drive, book a <a href="airport-taxi-goa.html">yellow-board taxi</a>. Two-wheelers live on the <a href="bike-rental-goa.html">bike rental</a> page. Staying on the beach belt? See <a href="candolim-calangute-baga.html">delivery to Candolim, Calangute and Baga</a>.</p>
        <p><a class="btn btn-wa" href="https://wa.me/{WA}?text=Hi!%20I%27d%20like%20a%20self-drive%20car%20in%20Goa.%20My%20dates%3A%20" target="_blank" rel="noopener noreferrer">{WA_SVG} Book a car on WhatsApp</a></p>''',
    f'''
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Self drive car rental in Goa",
    "serviceType": "Self-drive car rental",
    "provider": {{"@id": "{SITE}/#business"}},
    "areaServed": ["Nerul", "Candolim", "Calangute", "Baga", "Panjim", "North Goa"],
    "url": "{SITE}/self-drive-car-rental-goa.html"
  }}
  </script>
''',
    [("Home", f"{SITE}/"), ("Self drive car rental in Goa", f"{SITE}/self-drive-car-rental-goa.html")],
)

inner_page(
    "airport-taxi-goa.html",
    "Airport Taxi Goa | Mopa &amp; Dabolim Transfers | Sawariya",
    "Airport taxi in Goa from Nerul. Fixed WhatsApp quotes for Mopa and Dabolim, plus hotel transfers and day trips across North and South Goa.",
    "Airport Taxi Goa | Mopa & Dabolim | Sawariya",
    "taxi",
    '<a href="index.html">Home</a> <span aria-hidden="true">/</span> <span>Airport taxi</span>',
    "Airport taxi in <em>Goa</em>",
    "AC sedans with a yellow TAXI board. Mopa and Dabolim pickups, hotel drops, and day trips — quoted on WhatsApp before you ride.",
    f'''        <p>Sawariya runs <strong>airport taxi in Goa</strong> alongside the rental fleet. These are white AC sedans with a yellow TAXI board — the legal tourist taxi, not a private-plate hop. You send pickup, drop and time on WhatsApp; we send a <strong>fixed quote</strong> so you are not bargaining at the kerb.</p>
        <h3>Where we pick up</h3>
        <ul>
          <li><strong>Manohar International Airport (Mopa / GOX)</strong> — the North Goa airport. Sensible if you are staying in Candolim, Calangute, Baga, Anjuna or Panjim.</li>
          <li><strong>Goa International Airport (Dabolim / GOI)</strong> — South / Vasco side. We still cover hotel drops in North Goa; share your flight number so the driver times it.</li>
          <li>Hotels in Nerul, Candolim, Calangute, Baga, Sinquerim and Panjim.</li>
          <li>Day trips: North Goa sightseeing, South Goa, or outstation — ask for a full-day quote.</li>
        </ul>
        <p>Need to drive yourself after you land? Combine a taxi from the airport with a <a href="self-drive-car-rental-goa.html">self-drive car</a> or <a href="bike-rental-goa.html">scooter</a> from the Nerul desk. We are near Mahadev Temple, about 4 km from Candolim Beach.</p>
        <p>Call {PHONE1} or {PHONE2}, or tap WhatsApp with your flight details.</p>
        <p><a class="btn btn-wa" href="https://wa.me/{WA}?text=Hi%20Sawariya!%20I%20need%20an%20airport%20taxi.%20Flight%3A%20%20Pickup%3A%20%20Drop%3A%20" target="_blank" rel="noopener noreferrer">{WA_SVG} Quote my airport taxi</a></p>''',
    f'''
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "TaxiService",
    "name": "Airport taxi Goa — Mopa and Dabolim",
    "provider": {{"@id": "{SITE}/#business"}},
    "url": "{SITE}/airport-taxi-goa.html",
    "areaServed": ["Mopa Airport", "Dabolim Airport", "North Goa", "South Goa"],
    "telephone": "{TEL1}"
  }}
  </script>
''',
    [("Home", f"{SITE}/"), ("Airport taxi Goa", f"{SITE}/airport-taxi-goa.html")],
)

inner_page(
    "candolim-calangute-baga.html",
    "Bike &amp; Car Rental near Candolim, Calangute &amp; Baga | Nerul",
    "Bike and car rental near Candolim, Calangute and Baga. Pickup in Nerul — 4 km from Candolim Beach — or hotel delivery across North Goa.",
    "Rentals near Candolim, Calangute & Baga | Sawariya",
    "areas",
    '<a href="index.html">Home</a> <span aria-hidden="true">/</span> <span>Candolim, Calangute &amp; Baga</span>',
    "Candolim, Calangute &amp; <em>Baga</em>",
    "Nerul pickup is 4 km from Candolim Beach, 7 km from Calangute and 9 km from Baga — or we deliver the bike or car to your hotel.",
    f'''        <p>Most guests who search “<strong>bike rental Candolim</strong>” or “<strong>car hire Calangute</strong>” still want a vehicle on the beach belt. Sawariya is based in Nerul, just inland of that strip, so you skip the slowest part of Aguada–Siolim Road at handover, then you are on Candolim Beach in a few minutes.</p>
        <h3>Distances from our desk</h3>
        <table class="rate-table">
          <thead><tr><th>Place</th><th>From Nerul</th></tr></thead>
          <tbody>
            <tr><td>Coco Beach</td><td>2 km</td></tr>
            <tr><td>Candolim Beach</td><td>4 km</td></tr>
            <tr><td>Fort Aguada &amp; Sinquerim</td><td>5 km</td></tr>
            <tr><td>Calangute Beach</td><td>7 km</td></tr>
            <tr><td>Baga Beach</td><td>9 km</td></tr>
            <tr><td>Panjim</td><td>10 km</td></tr>
            <tr><td>Anjuna &amp; Vagator</td><td>14 km</td></tr>
          </tbody>
        </table>
        <p>Staying in a hotel or Airbnb in Candolim, Calangute, Baga, Sinquerim or Panjim? Send the location pin on WhatsApp. We confirm delivery time and any delivery charge, then leave you with the keys and two helmets if it is a bike.</p>
        <p>Choose a <a href="bike-rental-goa.html">Fascino or Himalayan</a> for the beach road, or a <a href="self-drive-car-rental-goa.html">Baleno, i20, Ertiga, Creta, Hycross or Thar</a> if you want AC and a boot. Flying in? Start with an <a href="airport-taxi-goa.html">Mopa or Dabolim taxi</a>.</p>
        <p><a class="btn btn-wa" href="https://wa.me/{WA}?text=Hi!%20Hotel%20delivery%20in%20North%20Goa%20please.%20Hotel%3A%20%20Dates%3A%20" target="_blank" rel="noopener noreferrer">{WA_SVG} Request hotel delivery</a></p>''',
    f'''
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Vehicle delivery in Candolim, Calangute and Baga",
    "provider": {{"@id": "{SITE}/#business"}},
    "areaServed": ["Candolim", "Calangute", "Baga", "Sinquerim", "Panjim"],
    "url": "{SITE}/candolim-calangute-baga.html"
  }}
  </script>
''',
    [("Home", f"{SITE}/"), ("Candolim, Calangute & Baga", f"{SITE}/candolim-calangute-baga.html")],
)

privacy = head(
    "Privacy | Sawariya Car &amp; Bike Rentals Goa",
    "How Sawariya Car & Bike Rentals Goa uses the contact details you share when you book a bike, car or taxi on WhatsApp or by phone.",
    f"{SITE}/privacy.html",
    "Privacy | Sawariya Goa Rentals",
    breadcrumb_json([("Home", f"{SITE}/"), ("Privacy", f"{SITE}/privacy.html")]),
    robots="index, follow",
)
privacy += f'''<body>
{nav("home")}
  <main id="main">
  {page_hero('<a href="index.html">Home</a> <span aria-hidden="true">/</span> <span>Privacy</span>', "Privacy", "What we collect when you book, and what we do not do with it.")}
  <section class="article">
    <div class="wrap">
      <div class="article-body reveal">
        <p>Sawariya Car &amp; Bike Rentals Goa (“we”) is a local rental desk at Near Mahadev Temple, H.No. 84, Nerul, Bardez, Goa 403114. This page covers the details you send when you book a bike, car or taxi.</p>
        <h3>What we collect</h3>
        <p>Name, phone number, WhatsApp messages, travel dates, hotel or pickup location, vehicle choice, and copies of driving licence / ID that you share so we can complete a hire. If you email us, we keep that thread.</p>
        <h3>How we use it</h3>
        <p>Only to confirm availability, quote a rate, arrange pickup or hotel delivery, and stay in touch about the booking. We do not sell your number, and we do not run ads from this site.</p>
        <h3>WhatsApp and calls</h3>
        <p>Booking happens on WhatsApp and phone. Those apps have their own privacy policies. We do not embed third-party marketing pixels on this website.</p>
        <h3>Contact</h3>
        <p>Questions: <a href="mailto:{EMAIL}">{EMAIL}</a> or {PHONE1}.</p>
      </div>
    </div>
  </section>
  </main>
{cta_footer()}'''
Path("privacy.html").write_text(privacy)
print("wrote privacy.html")

error = head(
    "Page not found | Sawariya Goa Rentals",
    "That page is missing. Head home to book a bike, self-drive car or airport taxi in North Goa.",
    f"{SITE}/404.html",
    "Page not found | Sawariya Goa Rentals",
    "",
    robots="noindex, follow",
)
error += f'''<body>
{nav("home")}
  <main id="main" class="error-page">
    <div class="wrap">
      <p class="section-label">404</p>
      <h1>That page has gone for a ride</h1>
      <p class="section-sub" style="margin-bottom:1.4rem">Try the homepage, or WhatsApp us if you were looking for a bike, car or taxi.</p>
      <div class="hero-actions">
        <a class="btn btn-sunset" href="index.html">Back to home</a>
        <a class="btn btn-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener noreferrer">{WA_SVG} WhatsApp</a>
      </div>
    </div>
  </main>
{cta_footer()}'''
Path("404.html").write_text(error)
print("wrote 404.html")
