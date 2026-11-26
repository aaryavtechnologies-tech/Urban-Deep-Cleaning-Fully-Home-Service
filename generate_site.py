import re

with open('gallery_block.txt', 'r', encoding='utf-8') as f:
    gallery_html = f.read()

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Urban Deep Cleaning | Home Cleaning Services in Bengaluru</title>
  <meta name="description" content="Looking for professional home cleaning in Bengaluru? Contact Urban Deep Cleaning Full Home Service in Bellandur. Call +91 72593 12025.">
  <meta name="keywords" content="Home cleaning services in Bengaluru, Deep cleaning services in Bangalore, Full home deep cleaning Bengaluru, House cleaning services in Bellandur, Professional home cleaning Bangalore">
  <meta name="theme-color" content="#087F5B">
  <link rel="canonical" href="https://urbandeepcleaning.in/">

  <!-- Open Graph / Meta -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="Urban Deep Cleaning | Home Cleaning Services in Bengaluru">
  <meta property="og:description" content="Professional deep cleaning for a spotless, fresh and comfortable home in Bengaluru. Available 24/7.">
  <meta property="og:image" content="images/work-02.jpg">
  <meta property="og:url" content="https://urbandeepcleaning.in/">

  <!-- Google Fonts: Headings (Plus Jakarta Sans) & Body (Inter) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="styles.css">

  <!-- LocalBusiness Schema Markup -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": "Urban Deep Cleaning Full Home Service",
    "image": "images/work-02.jpg",
    "@id": "https://www.google.com/maps?cid=6275165445863206232",
    "url": "https://urbandeepcleaning.in/",
    "telephone": "+917259312025",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "Devervisnalli, Bellandur",
      "addressLocality": "Bengaluru",
      "addressRegion": "Karnataka",
      "postalCode": "560103",
      "addressCountry": "IN"
    }},
    "geo": {{
      "@type": "GeoCoordinates",
      "latitude": 12.9260,
      "longitude": 77.6762
    }},
    "openingHoursSpecification": {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
      ],
      "opens": "00:00",
      "closes": "23:59"
    }},
    "areaServed": [
      "Bengaluru",
      "Bellandur",
      "HSR Layout",
      "Sarjapur Road",
      "Whitefield",
      "Koramangala"
    ]
  }}
  </script>
</head>
<body>

  <!-- Top Sticky Navigation -->
  <header class="navbar" id="navbar">
    <div class="nav-container">
      <a href="#home" class="brand" aria-label="Urban Deep Cleaning Full Home Service">
        <span class="brand-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
            <polyline points="9 22 9 12 15 12 15 22"/>
          </svg>
        </span>
        <span class="brand-name">
          <strong>Urban Deep Cleaning</strong>
          <small>Full Home Service</small>
        </span>
      </a>

      <!-- Desktop Nav -->
      <nav class="nav-links" id="navLinks" aria-label="Main Navigation">
        <a href="#home" class="nav-link active">Home</a>
        <a href="#services" class="nav-link">Services</a>
        <a href="#about" class="nav-link">About</a>
        <a href="#work" class="nav-link">Our Work (47)</a>
        <a href="#video" class="nav-link">Video Tour</a>
        <a href="#contact" class="nav-link">Contact</a>
      </nav>

      <!-- Nav CTA -->
      <div class="nav-actions">
        <a href="#contact" class="btn btn-primary btn-sm">Book a Cleaning</a>
        <button class="menu-toggle" id="menuToggle" aria-label="Toggle navigation menu" aria-expanded="false">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>

    <!-- Mobile Navigation Drawer -->
    <div class="mobile-drawer" id="mobileDrawer">
      <nav class="mobile-nav">
        <a href="#home" class="mobile-nav-link">Home</a>
        <a href="#services" class="mobile-nav-link">Services</a>
        <a href="#about" class="mobile-nav-link">About</a>
        <a href="#work" class="mobile-nav-link">Our Work (47)</a>
        <a href="#video" class="mobile-nav-link">Video Tour</a>
        <a href="#contact" class="mobile-nav-link">Contact</a>
        <div class="mobile-drawer-cta">
          <a href="#contact" class="btn btn-primary btn-block">Book a Cleaning</a>
          <a href="tel:+917259312025" class="btn btn-outline btn-block">Call +91 72593 12025</a>
        </div>
      </nav>
    </div>
  </header>

  <!-- Main Content -->
  <main>

    <!-- 1. Hero Section -->
    <section class="hero-section" id="home">
      <div class="container hero-container">
        <div class="hero-content">
          <div class="hero-eyebrow">PROFESSIONAL HOME CLEANING IN BENGALURU</div>
          <h1 class="hero-title">A Cleaner Home.<br>A Fresher Life.</h1>
          <p class="hero-desc">Professional deep cleaning for a spotless, fresh and comfortable home.</p>
          <div class="hero-actions">
            <a href="#contact" class="btn btn-primary">Book a Cleaning</a>
            <a href="tel:+917259312025" class="btn btn-secondary">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
              </svg>
              <span>Call Now</span>
            </a>
          </div>
          <div class="hero-trust-bar">
            <div class="trust-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
              <span>Professional Cleaning</span>
            </div>
            <div class="trust-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              <span>Attention to Detail</span>
            </div>
            <div class="trust-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
              <span>Available 24/7</span>
            </div>
          </div>
        </div>
        <div class="hero-image-wrap">
          <img src="images/work-02.jpg" alt="Urban Deep Cleaning professional modular kitchen cleaning work" class="hero-image" width="960" height="600" fetchpriority="high">
        </div>
      </div>
    </section>

    <!-- 2. Services Section -->
    <section class="section services-section" id="services">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Expert Cleaning for Every Corner.</h2>
          <p class="section-subtitle">Professional cleaning solutions for your home.</p>
        </div>

        <div class="services-grid">
          <!-- Service 1 -->
          <article class="service-card">
            <div class="service-img-wrap">
              <img src="images/work-04.jpg" alt="Full Home Deep Cleaning" loading="lazy" width="400" height="280">
            </div>
            <div class="service-body">
              <h3 class="service-title">Full Home Deep Cleaning</h3>
              <p class="service-desc">Complete top-to-bottom sanitization and surface restoration for your entire residence.</p>
              <a href="#contact" class="service-link" data-service="Full Home Deep Cleaning">
                <span>Book This Service</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </a>
            </div>
          </article>

          <!-- Service 2 -->
          <article class="service-card">
            <div class="service-img-wrap">
              <img src="images/work-26.jpg" alt="Bathroom Deep Cleaning" loading="lazy" width="400" height="280">
            </div>
            <div class="service-body">
              <h3 class="service-title">Bathroom Cleaning</h3>
              <p class="service-desc">Intensive tile scrubbing, limescale descaling, and high-touch hygienic disinfection.</p>
              <a href="#contact" class="service-link" data-service="Bathroom Cleaning">
                <span>Book This Service</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </a>
            </div>
          </article>

          <!-- Service 3 -->
          <article class="service-card">
            <div class="service-img-wrap">
              <img src="images/work-03.jpg" alt="Kitchen Deep Cleaning" loading="lazy" width="400" height="280">
            </div>
            <div class="service-body">
              <h3 class="service-title">Kitchen Deep Cleaning</h3>
              <p class="service-desc">Effective grease removal across countertops, cabinets, chimney surface, and tiled walls.</p>
              <a href="#contact" class="service-link" data-service="Kitchen Deep Cleaning">
                <span>Book This Service</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </a>
            </div>
          </article>

          <!-- Service 4 -->
          <article class="service-card">
            <div class="service-img-wrap">
              <img src="images/work-14.jpg" alt="Sofa and Carpet Cleaning" loading="lazy" width="400" height="280">
            </div>
            <div class="service-body">
              <h3 class="service-title">Sofa and Carpet Cleaning</h3>
              <p class="service-desc">Deep fabric vacuuming, stain treatment, and fabric shampooing to refresh upholstery.</p>
              <a href="#contact" class="service-link" data-service="Sofa and Carpet Cleaning">
                <span>Book This Service</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </a>
            </div>
          </article>

          <!-- Service 5 -->
          <article class="service-card">
            <div class="service-img-wrap">
              <img src="images/work-09.jpg" alt="Bedroom and Living Room Cleaning" loading="lazy" width="400" height="280">
            </div>
            <div class="service-body">
              <h3 class="service-title">Bedroom and Living Room Cleaning</h3>
              <p class="service-desc">Detailed furniture dusting, corner cobweb clearing, and machine floor scrubbing.</p>
              <a href="#contact" class="service-link" data-service="Bedroom and Living Room Cleaning">
                <span>Book This Service</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </a>
            </div>
          </article>

          <!-- Service 6 -->
          <article class="service-card">
            <div class="service-img-wrap">
              <img src="images/work-30.jpg" alt="Move-in and Move-out Cleaning" loading="lazy" width="400" height="280">
            </div>
            <div class="service-body">
              <h3 class="service-title">Move-in and Move-out Cleaning</h3>
              <p class="service-desc">Thorough handover cleaning preparing homes for immediate and comfortable occupancy.</p>
              <a href="#contact" class="service-link" data-service="Move-in and Move-out Cleaning">
                <span>Book This Service</span>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </a>
            </div>
          </article>
        </div>

        <div class="services-footer-note">
          <p>* Service scope and inclusions are confirmed directly with you before final scheduling. No hidden charges.</p>
        </div>
      </div>
    </section>

    <!-- 3. About Us Section -->
    <section class="section about-section" id="about">
      <div class="container about-container">
        <div class="about-image-wrap">
          <img src="images/work-18.jpg" alt="Real cleaned bedroom and polished hardwood flooring" loading="lazy" width="550" height="580">
        </div>
        <div class="about-content">
          <div class="section-tag">ABOUT US</div>
          <h2 class="section-title">We Care for Your Home.</h2>
          <p class="about-text">
            Urban Deep Cleaning Full Home Service provides professional home cleaning solutions in Bengaluru, with a focus on cleanliness, comfort and attention to detail.
          </p>
          <div class="about-highlights">
            <div class="about-highlight-item">
              <div class="highlight-bullet"></div>
              <div>
                <strong>Detailed Cleaning</strong>
                <p>Systematic surface care targeting deep-seated dust and stains.</p>
              </div>
            </div>
            <div class="about-highlight-item">
              <div class="highlight-bullet"></div>
              <div>
                <strong>Convenient Booking</strong>
                <p>Simple booking via phone or WhatsApp at your preferred time.</p>
              </div>
            </div>
            <div class="about-highlight-item">
              <div class="highlight-bullet"></div>
              <div>
                <strong>Customer-Focused Service</strong>
                <p>Professional approach tailored to your exact apartment requirements.</p>
              </div>
            </div>
          </div>
          <div class="about-action">
            <a href="#contact" class="btn btn-primary">Contact Us</a>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Before and After Section (5 Authentic Real Project Pairs) -->
    <section class="section before-after-section" id="comparison">
      <div class="container">
        <div class="section-header">
          <span class="badge-pill">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
            Real Job Transformations
          </span>
          <h2 class="section-title">See the Difference.</h2>
          <p class="section-subtitle">Drag the interactive slider horizontally to compare our real residential cleaning results in Bengaluru.</p>
        </div>

        <!-- Filter tabs for 5 Authentic Categories -->
        <div class="slider-tabs" role="tablist" aria-label="Cleaning Categories">
          <button class="tab-btn active" role="tab" aria-selected="true" data-category="kitchen_sink">Kitchen Sink & Granite</button>
          <button class="tab-btn" role="tab" aria-selected="false" data-category="shower">Shower & Geyser</button>
          <button class="tab-btn" role="tab" aria-selected="false" data-category="living_floor">Living Room Floor</button>
          <button class="tab-btn" role="tab" aria-selected="false" data-category="bathroom_vanity">Washbasin Vanity</button>
          <button class="tab-btn" role="tab" aria-selected="false" data-category="floor_tiles">Floor & Grout</button>
        </div>

        <!-- Interactive Comparison Slider Container -->
        <div class="comparison-card">
          <div class="comparison-slider" id="comparisonSlider" aria-label="Before and after image comparison slider">
            <!-- After Image (Background layer) -->
            <div class="slider-layer slider-after">
              <img id="afterImg" src="images/comparison/kitchen_sink_after.jpg" alt="Spotless cleaned space after service" loading="lazy">
              <span class="badge badge-after">AFTER CLEANING</span>
            </div>
            <!-- Before Image (Clipped layer) -->
            <div class="slider-layer slider-before" id="beforeLayer" style="clip-path: inset(0 50% 0 0); -webkit-clip-path: inset(0 50% 0 0);">
              <img id="beforeImg" src="images/comparison/kitchen_sink_before.jpg" alt="Space condition before deep cleaning" loading="lazy">
              <span class="badge badge-before">BEFORE CLEANING</span>
            </div>
            <!-- Draggable Divider Handle -->
            <div class="slider-handle" id="sliderHandle" tabindex="0" role="slider" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100" aria-label="Slide to compare before and after">
              <div class="handle-line"></div>
              <div class="handle-button">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/><polyline points="9 18 3 12 9 6" transform="translate(12,0) scale(-1,1)"/></svg>
              </div>
              <div class="handle-line"></div>
            </div>
          </div>
          <div class="slider-caption">
            <span id="sliderCategoryLabel">Kitchen Sink & Granite Countertop Descaling</span>
            <small class="disclaimer-text">(100% authentic project photography by Urban Deep Cleaning)</small>
          </div>
        </div>

        <!-- Real Before & After Project Gallery Cards -->
        <div class="comparison-gallery-grid">
          <!-- Card 1 -->
          <div class="comparison-thumb-card active" data-category="kitchen_sink">
            <div class="thumb-img-wrap">
              <img src="images/comparison/kitchen_sink_full.jpg" alt="Kitchen sink before and after cleaning" loading="lazy">
              <span class="thumb-badge">Kitchen</span>
            </div>
            <div class="thumb-info">
              <h4>Kitchen Sink & Granite</h4>
              <p>Sparkling stainless steel & mirror granite</p>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="comparison-thumb-card" data-category="shower">
            <div class="thumb-img-wrap">
              <img src="images/comparison/shower_full.jpg" alt="Shower head and geyser before and after cleaning" loading="lazy">
              <span class="thumb-badge">Bathroom</span>
            </div>
            <div class="thumb-info">
              <h4>Rain Shower & Geyser</h4>
              <p>Chrome descaling & hard water stain removal</p>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="comparison-thumb-card" data-category="living_floor">
            <div class="thumb-img-wrap">
              <img src="images/comparison/living_floor_full.jpg" alt="Living room floor tiles before and after cleaning" loading="lazy">
              <span class="thumb-badge">Living Room</span>
            </div>
            <div class="thumb-info">
              <h4>Living Room Floor</h4>
              <p>High-gloss vitrified tile buffing & reflection</p>
            </div>
          </div>

          <!-- Card 4 -->
          <div class="comparison-thumb-card" data-category="bathroom_vanity">
            <div class="thumb-img-wrap">
              <img src="images/comparison/bathroom_vanity_full.jpg" alt="Bathroom vanity cabinet before and after cleaning" loading="lazy">
              <span class="thumb-badge">Vanity</span>
            </div>
            <div class="thumb-info">
              <h4>Washbasin & Cabinet</h4>
              <p>Under-counter sanitization & spotless basin</p>
            </div>
          </div>

          <!-- Card 5 -->
          <div class="comparison-thumb-card" data-category="floor_tiles">
            <div class="thumb-img-wrap">
              <img src="images/comparison/floor_tiles_full.jpg" alt="Floor grout tiles before and after cleaning" loading="lazy">
              <span class="thumb-badge">Floor & Grout</span>
            </div>
            <div class="thumb-info">
              <h4>Tile Grout Scrubbing</h4>
              <p>Deep extraction of dirt & grout brightening</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. How It Works -->
    <section class="section process-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">A Clean Home in 3 Simple Steps.</h2>
          <p class="section-subtitle">Effortless booking from your phone to a sparkling residence.</p>
        </div>

        <div class="process-steps">
          <!-- Step 1 -->
          <div class="step-card">
            <div class="step-badge">01</div>
            <div class="step-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="4" width="20" height="16" rx="2"/><path d="M10 4v4"/><path d="M2 8h20"/><path d="M6 4v4"/>
              </svg>
            </div>
            <h3 class="step-title">Book Your Service</h3>
            <p class="step-desc">Choose a cleaning service and contact us via call or WhatsApp.</p>
          </div>

          <!-- Step 2 -->
          <div class="step-card">
            <div class="step-badge">02</div>
            <div class="step-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
              </svg>
            </div>
            <h3 class="step-title">Schedule Your Cleaning</h3>
            <p class="step-desc">Arrange a convenient cleaning appointment that fits your routine.</p>
          </div>

          <!-- Step 3 -->
          <div class="step-card">
            <div class="step-badge">03</div>
            <div class="step-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>
              </svg>
            </div>
            <h3 class="step-title">Enjoy a Cleaner Home</h3>
            <p class="step-desc">Relax in your freshly cleaned, hygienic, and sanitized living space.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. Why Choose Us -->
    <section class="section why-section">
      <div class="container why-container">
        <div class="why-image-wrap">
          <img src="images/work-01.jpg" alt="Mirror-polished black granite staircase cleaning" loading="lazy" width="550" height="600">
        </div>
        <div class="why-content">
          <div class="section-tag">WHY US</div>
          <h2 class="section-title">Cleaning That Makes a Difference.</h2>
          <div class="why-grid">
            <div class="why-item">
              <div class="why-icon-wrap">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              </div>
              <div>
                <h3 class="why-item-title">Detailed Cleaning</h3>
                <p class="why-item-desc">Thorough cleaning of corners, hidden grime, and hard-to-reach surfaces.</p>
              </div>
            </div>

            <div class="why-item">
              <div class="why-icon-wrap">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              </div>
              <div>
                <h3 class="why-item-title">Professional Approach</h3>
                <p class="why-item-desc">Punctual, disciplined service utilizing proper cleaning equipment.</p>
              </div>
            </div>

            <div class="why-item">
              <div class="why-icon-wrap">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              </div>
              <div>
                <h3 class="why-item-title">Convenient Scheduling</h3>
                <p class="why-item-desc">Flexible service timings aligned with your household requirements.</p>
              </div>
            </div>

            <div class="why-item">
              <div class="why-icon-wrap">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              </div>
              <div>
                <h3 class="why-item-title">Available 24/7</h3>
                <p class="why-item-desc">Round-the-clock availability for standard bookings and urgent deep cleans.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. Gallery Section (All 47 Authentic Project Photographs) -->
    <section class="section gallery-section" id="work">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">A Glimpse of Our Work.</h2>
          <p class="section-subtitle">Authentic photographic showcase of 47 completed deep cleaning projects across Bengaluru.</p>
        </div>

        <!-- Filter Controls -->
        <div class="gallery-filters" role="tablist" aria-label="Gallery Categories">
          <button class="filter-btn active" data-filter="all">All Work (47)</button>
          <button class="filter-btn" data-filter="kitchen">Kitchen Deep Clean (18)</button>
          <button class="filter-btn" data-filter="living">Bedrooms & Living (13)</button>
          <button class="filter-btn" data-filter="wardrobes">Wardrobes & Cabinets (6)</button>
          <button class="filter-btn" data-filter="floors">Floors & Stairs (5)</button>
          <button class="filter-btn" data-filter="bathroom">Bathrooms & Tiles (3)</button>
          <a href="#video" class="filter-btn filter-video-btn" style="text-decoration: none;">▶ Watch Video (1:00 min)</a>
        </div>

        <div class="gallery-grid" id="galleryGrid">
{gallery_html}
        </div>

        <div class="gallery-note">
          <small class="disclaimer-text">* All 47 photographs above are authentic project images by Urban Deep Cleaning Full Home Service.</small>
        </div>
      </div>
    </section>

        <!-- 8. Real Video Walkthrough Section -->
    <section class="section video-section" id="video">
      <div class="container">
        <div class="section-header">
          <span class="badge-pill">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
            Real On-Site Video
          </span>
          <h2 class="section-title">See Our Work in Motion.</h2>
          <p class="section-subtitle">Watch an authentic, unedited walkthrough of a completed apartment deep cleaning project in Bengaluru.</p>
        </div>

        <div class="video-showcase-card">
          <div class="video-player-wrap">
            <video id="cleaningVideo" controls preload="metadata" poster="images/video-poster.jpg" playsinline class="cleaning-video">
              <source src="images/work-video.mp4" type="video/mp4">
              Your browser does not support the video tag.
            </video>
            <div class="video-floating-badge">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"/></svg>
              <span>Authentic Project Walkthrough (1:00 min)</span>
            </div>
          </div>

          <div class="video-info-content">
            <span class="video-meta-tag">Bengaluru Apartment Deep Clean</span>
            <h3 class="video-info-title">Comprehensive Room-by-Room Cleaning</h3>
            <p class="video-info-desc">
              Experience the standard of our work. This real walkthrough highlights how our specialized crew tackles deep-set floor grime, balcony dust, window tracks, kitchen cabinets, and sanitary spaces across local Bengaluru homes.
            </p>

            <div class="video-highlights-grid">
              <div class="video-highlight-item">
                <div class="highlight-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                </div>
                <div>
                  <strong>Deep Floor Buffing & Grout Scrubbing</strong>
                  <p>Removes tough construction residue, dullness, and tile discoloration.</p>
                </div>
              </div>

              <div class="video-highlight-item">
                <div class="highlight-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                </div>
                <div>
                  <strong>Balcony & Sliding Door Tracks</strong>
                  <p>Complete suction and chemical-safe wiping of dust-trapping sliding rails.</p>
                </div>
              </div>

              <div class="video-highlight-item">
                <div class="highlight-icon">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                </div>
                <div>
                  <strong>Hygienic Degreasing & Sanitize</strong>
                  <p>Deep grease-cutting for modular kitchen units and anti-bacterial bathroom sanitization.</p>
                </div>
              </div>
            </div>

            <div class="video-cta-group">
              <a href="https://wa.me/917259312025?text=Hi%20Urban%20Deep%20Cleaning%2C%20I%20watched%20your%20walkthrough%20video%20and%20would%20like%20to%20book%20a%20similar%20deep%20cleaning." target="_blank" rel="noopener noreferrer" class="btn btn-primary">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.539 1.761.814 2.791.814 3.18 0 5.767-2.587 5.768-5.766 0-3.18-2.587-5.8-5.768-5.8zm3.385 8.167c-.145.407-.747.77-1.042.8-.295.031-.676.062-2.179-.562-1.89-.785-3.08-2.73-3.176-2.858-.095-.128-.767-1.02-.767-1.946 0-.927.487-1.382.66-1.572.174-.19.38-.238.508-.238.127 0 .254.002.365.008.117.006.275-.044.428.324.159.38.541 1.32.588 1.417.048.096.08.207.016.334-.063.127-.095.207-.19.318-.095.111-.202.248-.289.333-.095.096-.195.2-.084.39.111.19.493.813 1.056 1.314.726.646 1.339.847 1.53.942.19.095.302.08.413-.048.111-.127.476-.556.603-.746.127-.19.254-.159.429-.095.174.064 1.111.524 1.301.62.19.095.318.143.365.222.048.08.048.461-.097.868z"/></svg>
                <span>Book This Cleaning</span>
              </a>
              <a href="tel:+917259312025" class="btn btn-outline">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                <span>Call +91 72593 12025</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

<!-- 8. Booking CTA Banner Section (Dark Green Full Width) -->
    <section class="cta-banner">
      <div class="container cta-container">
        <h2 class="cta-title">Ready for a Cleaner Home?</h2>
        <p class="cta-desc">Book your professional home cleaning service today.</p>
        <div class="cta-actions">
          <a href="https://wa.me/917259312025?text=Hello%20Urban%20Deep%20Cleaning%2C%20I%20would%20like%20to%20book%20a%20home%20cleaning%20service." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.539 1.761.814 2.791.814 3.18 0 5.767-2.587 5.768-5.766 0-3.18-2.587-5.8-5.768-5.8zm3.385 8.167c-.145.407-.747.77-1.042.8-.295.031-.676.062-2.179-.562-1.89-.785-3.08-2.73-3.176-2.858-.095-.128-.767-1.02-.767-1.946 0-.927.487-1.382.66-1.572.174-.19.38-.238.508-.238.127 0 .254.002.365.008.117.006.275-.044.428.324.159.38.541 1.32.588 1.417.048.096.08.207.016.334-.063.127-.095.207-.19.318-.095.111-.202.248-.289.333-.095.096-.195.2-.084.39.111.19.493.813 1.056 1.314.726.646 1.339.847 1.53.942.19.095.302.08.413-.048.111-.127.476-.556.603-.746.127-.19.254-.159.429-.095.174.064 1.111.524 1.301.62.19.095.318.143.365.222.048.08.048.461-.097.868z"/></svg>
            <span>Book on WhatsApp</span>
          </a>
          <a href="tel:+917259312025" class="btn btn-outline-white">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <span>Call +91 72593 12025</span>
          </a>
        </div>
      </div>
    </section>

    <!-- 9. Contact and Booking Section (No Date of Birth/Date input) -->
    <section class="section contact-section" id="contact">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Let's Get Your Home Clean.</h2>
          <p class="section-subtitle">Reach us directly or submit your details to connect immediately on WhatsApp.</p>
        </div>

        <div class="contact-grid">
          <!-- Left: Business Info & Map -->
          <div class="contact-info">
            <div class="info-card">
              <div class="info-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
              </div>
              <div>
                <strong>Phone & WhatsApp</strong>
                <p><a href="tel:+917259312025">+91 72593 12025</a></p>
              </div>
            </div>

            <div class="info-card">
              <div class="info-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
              </div>
              <div>
                <strong>Location</strong>
                <p>Devervisnalli, Bellandur, Bengaluru, Karnataka 560103</p>
              </div>
            </div>

            <div class="info-card">
              <div class="info-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              </div>
              <div>
                <strong>Business Hours</strong>
                <p>Open 24 Hours (Monday – Sunday)</p>
              </div>
            </div>

            <!-- Integrated Google Map -->
            <div class="map-card">
              <div class="map-frame">
                <iframe 
                  title="Urban Deep Cleaning Location Map" 
                  src="https://maps.google.com/maps?q=Devervisnalli,+Bellandur,+Bengaluru,+Karnataka+560103&t=&z=15&ie=UTF8&iwloc=&output=embed" 
                  width="100%" 
                  height="220" 
                  style="border:0;" 
                  allowfullscreen="" 
                  loading="lazy" 
                  referrerpolicy="no-referrer-when-downgrade">
                </iframe>
              </div>
              <div class="map-footer">
                <a href="https://www.google.com/maps?cid=6275165445863206232" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm btn-block">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                  <span>Get Directions on Google Maps</span>
                </a>
              </div>
            </div>
          </div>

          <!-- Right: Minimal Clean Booking Form -->
          <div class="contact-form-wrap">
            <form id="bookingForm" class="booking-form" novalidate>
              <h3 class="form-title">Book a Deep Cleaning</h3>
              <p class="form-desc">Fill out your details to receive an instant confirmation via WhatsApp.</p>

              <div class="form-group">
                <label for="fullName">Full Name</label>
                <input type="text" id="fullName" name="fullName" placeholder="Enter your name" required autocomplete="name">
                <span class="form-error" id="nameError">Please enter your full name.</span>
              </div>

              <div class="form-group">
                <label for="phoneNumber">Mobile Number</label>
                <input type="tel" id="phoneNumber" name="phoneNumber" placeholder="e.g. 9876543210" pattern="[0-9]{10}" required autocomplete="tel">
                <span class="form-error" id="phoneError">Please enter a valid 10-digit mobile number.</span>
              </div>

              <div class="form-group">
                <label for="serviceType">Select Cleaning Service</label>
                <select id="serviceType" name="serviceType" required>
                  <option value="" disabled selected>Choose a cleaning service</option>
                  <option value="Full Home Deep Cleaning">Full Home Deep Cleaning</option>
                  <option value="Bathroom Cleaning">Bathroom Cleaning</option>
                  <option value="Kitchen Deep Cleaning">Kitchen Deep Cleaning</option>
                  <option value="Sofa and Carpet Cleaning">Sofa and Carpet Cleaning</option>
                  <option value="Bedroom and Living Room Cleaning">Bedroom and Living Room Cleaning</option>
                  <option value="Move-in and Move-out Cleaning">Move-in and Move-out Cleaning</option>
                  <option value="Other Deep Cleaning Enquiry">Other Deep Cleaning Enquiry</option>
                </select>
                <span class="form-error" id="serviceError">Please select a service.</span>
              </div>

              <div class="form-group">
                <label for="locationArea">Area / Location in Bengaluru</label>
                <input type="text" id="locationArea" name="locationArea" placeholder="e.g. Bellandur, HSR Layout, Whitefield" required>
                <span class="form-error" id="locationError">Please enter your neighborhood or area.</span>
              </div>

              <button type="submit" class="btn btn-primary btn-block btn-lg" id="submitBtn">
                <span>Submit Enquiry via WhatsApp</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.539 1.761.814 2.791.814 3.18 0 5.767-2.587 5.768-5.766 0-3.18-2.587-5.8-5.768-5.8zm3.385 8.167c-.145.407-.747.77-1.042.8-.295.031-.676.062-2.179-.562-1.89-.785-3.08-2.73-3.176-2.858-.095-.128-.767-1.02-.767-1.946 0-.927.487-1.382.66-1.572.174-.19.38-.238.508-.238.127 0 .254.002.365.008.117.006.275-.044.428.324.159.38.541 1.32.588 1.417.048.096.08.207.016.334-.063.127-.095.207-.19.318-.095.111-.202.248-.289.333-.095.096-.195.2-.084.39.111.19.493.813 1.056 1.314.726.646 1.339.847 1.53.942.19.095.302.08.413-.048.111-.127.476-.556.603-.746.127-.19.254-.159.429-.095.174.064 1.111.524 1.301.62.19.095.318.143.365.222.048.08.048.461-.097.868z"/></svg>
              </button>

              <p class="form-disclaimer">
                Clicking submit validates your enquiry and opens WhatsApp with your pre-filled booking details to chat directly with our team.
              </p>
            </form>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- 10. Footer -->
  <footer class="site-footer">
    <div class="container footer-container">
      <div class="footer-brand-col">
        <div class="brand">
          <span class="brand-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
              <polyline points="9 22 9 12 15 12 15 22"/>
            </svg>
          </span>
          <span class="brand-name">
            <strong>Urban Deep Cleaning</strong>
            <small>Full Home Service</small>
          </span>
        </div>
        <p class="footer-address">
          Devervisnalli, Bellandur, Bengaluru, Karnataka – 560103
        </p>
        <p class="footer-phone">
          Contact: <a href="tel:+917259312025">+91 72593 12025</a>
        </p>
      </div>

      <div class="footer-links-col">
        <h4>Navigation</h4>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#work">Our Work (47)</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </div>

      <div class="footer-services-col">
        <h4>Services</h4>
        <ul>
          <li><a href="#services">Full Home Cleaning</a></li>
          <li><a href="#services">Kitchen Cleaning</a></li>
          <li><a href="#services">Bathroom Cleaning</a></li>
          <li><a href="#services">Sofa & Carpet</a></li>
          <li><a href="#services">Move-in / Move-out</a></li>
        </ul>
      </div>

      <div class="footer-map-col">
        <h4>Google Business</h4>
        <p>Verified Local Cleaning Service in Bellandur, Bengaluru.</p>
        <a href="https://www.google.com/maps?cid=6275165445863206232" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">
          <span>View on Google Maps</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
        </a>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <p>&copy; <span id="currentYear">2026</span> Urban Deep Cleaning Full Home Service. All rights reserved.</p>
        <p class="footer-disclaimer">All 47 project images shown are authentic photographs of residential cleaning work completed in Bengaluru.</p>
      </div>
    </div>
  </footer>

  <!-- Lightbox Modal for Gallery -->
  <div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-hidden="true" aria-label="Photo Lightbox">
    <button class="lightbox-close" id="lightboxClose" aria-label="Close Lightbox">&times;</button>
    <button class="lightbox-nav lightbox-prev" id="lightboxPrev" aria-label="Previous Photo">&#10094;</button>
    <div class="lightbox-content">
      <img id="lightboxImg" src="" alt="">
      <p id="lightboxCaption" class="lightbox-caption"></p>
      <span id="lightboxCounter" class="lightbox-counter"></span>
    </div>
    <button class="lightbox-nav lightbox-next" id="lightboxNext" aria-label="Next Photo">&#10095;</button>
  </div>

  <!-- Floating WhatsApp Action Button (Desktop & Mobile) -->
  <a href="https://wa.me/917259312025?text=Hello%20Urban%20Deep%20Cleaning%2C%20I%20would%20like%20to%20enquire%20about%20deep%20cleaning%20services." target="_blank" rel="noopener noreferrer" class="floating-whatsapp" aria-label="Chat with Urban Deep Cleaning on WhatsApp">
    <span class="whatsapp-pulse"></span>
    <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.539 1.761.814 2.791.814 3.18 0 5.767-2.587 5.768-5.766 0-3.18-2.587-5.8-5.768-5.8zm3.385 8.167c-.145.407-.747.77-1.042.8-.295.031-.676.062-2.179-.562-1.89-.785-3.08-2.73-3.176-2.858-.095-.128-.767-1.02-.767-1.946 0-.927.487-1.382.66-1.572.174-.19.38-.238.508-.238.127 0 .254.002.365.008.117.006.275-.044.428.324.159.38.541 1.32.588 1.417.048.096.08.207.016.334-.063.127-.095.207-.19.318-.095.111-.202.248-.289.333-.095.096-.195.2-.084.39.111.19.493.813 1.056 1.314.726.646 1.339.847 1.53.942.19.095.302.08.413-.048.111-.127.476-.556.603-.746.127-.19.254-.159.429-.095.174.064 1.111.524 1.301.62.19.095.318.143.365.222.048.08.048.461-.097.868z"/></svg>
    <span class="floating-tooltip">Chat with us</span>
  </a>

  <!-- Mobile Sticky Bottom Action Bar -->
  <div class="mobile-action-bar" aria-label="Quick Action Bar">
    <a href="tel:+917259312025" class="action-btn action-call">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
      <span>Call Now</span>
    </a>
    <a href="https://wa.me/917259312025?text=Hello%20Urban%20Deep%20Cleaning%2C%20I%20would%20like%20to%20book%20a%20cleaning%20service." target="_blank" rel="noopener noreferrer" class="action-btn action-whatsapp">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.539 1.761.814 2.791.814 3.18 0 5.767-2.587 5.768-5.766 0-3.18-2.587-5.8-5.768-5.8zm3.385 8.167c-.145.407-.747.77-1.042.8-.295.031-.676.062-2.179-.562-1.89-.785-3.08-2.73-3.176-2.858-.095-.128-.767-1.02-.767-1.946 0-.927.487-1.382.66-1.572.174-.19.38-.238.508-.238.127 0 .254.002.365.008.117.006.275-.044.428.324.159.38.541 1.32.588 1.417.048.096.08.207.016.334-.063.127-.095.207-.19.318-.095.111-.202.248-.289.333-.095.096-.195.2-.084.39.111.19.493.813 1.056 1.314.726.646 1.339.847 1.53.942.19.095.302.08.413-.048.111-.127.476-.556.603-.746.127-.19.254-.159.429-.095.174.064 1.111.524 1.301.62.19.095.318.143.365.222.048.08.048.461-.097.868z"/></svg>
      <span>Book via WhatsApp</span>
    </a>
  </div>

  <script src="script.js"></script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated index.html with all 47 images!')
