/**
 * Urban Deep Cleaning Full Home Service – Interactive JavaScript
 * High performance, zero external framework overhead, fully accessible.
 * Fully integrated with all 47 authentic project photographs.
 */

document.addEventListener('DOMContentLoaded', () => {

  /* -------------------------------------------------------------------------
     1. Dynamic Year
     ------------------------------------------------------------------------- */
  const yearEl = document.getElementById('currentYear');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  /* -------------------------------------------------------------------------
     2. Mobile Navigation Drawer
     ------------------------------------------------------------------------- */
  const menuToggle = document.getElementById('menuToggle');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const mobileLinks = document.querySelectorAll('.mobile-nav-link');

  if (menuToggle && mobileDrawer) {
    const toggleMenu = (open) => {
      const isOpen = open !== undefined ? open : !mobileDrawer.classList.contains('active');
      mobileDrawer.classList.toggle('active', isOpen);
      menuToggle.classList.toggle('open', isOpen);
      menuToggle.setAttribute('aria-expanded', isOpen.toString());
      document.body.style.overflow = isOpen ? 'hidden' : '';
    };

    menuToggle.addEventListener('click', () => toggleMenu());

    mobileLinks.forEach(link => {
      link.addEventListener('click', () => toggleMenu(false));
    });
  }

  /* -------------------------------------------------------------------------
     3. Active Nav Link on Scroll
     ------------------------------------------------------------------------- */
  const sections = document.querySelectorAll('section[id]');
  const desktopLinks = document.querySelectorAll('.nav-link');

  const highlightNav = () => {
    const scrollY = window.pageYOffset;
    const headerHeight = 90;

    sections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - headerHeight;
      const sectionId = current.getAttribute('id');

      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        desktopLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          }
        });
      }
    });
  };

  window.addEventListener('scroll', highlightNav, { passive: true });

  /* -------------------------------------------------------------------------
     4. Interactive Before & After Slider (Authentic Project Photos)
     ------------------------------------------------------------------------- */
  const comparisonSlider = document.getElementById('comparisonSlider');
  const beforeLayer = document.getElementById('beforeLayer');
  const sliderHandle = document.getElementById('sliderHandle');
  const beforeImg = document.getElementById('beforeImg');
  const afterImg = document.getElementById('afterImg');
  const categoryLabel = document.getElementById('sliderCategoryLabel');
  const tabButtons = document.querySelectorAll('.tab-btn');

  // Authentic 5 Comparison Categories data
  const comparisonData = {
    kitchen_sink: {
      title: 'Kitchen Sink & Granite Countertop Descaling',
      before: 'images/comparison/kitchen_sink_before.jpg',
      after: 'images/comparison/kitchen_sink_after.jpg'
    },
    shower: {
      title: 'Rain Shower & Geyser Limescale Removal',
      before: 'images/comparison/shower_before.jpg',
      after: 'images/comparison/shower_after.jpg'
    },
    living_floor: {
      title: 'Living Room Vitrified Tile Deep Buffing',
      before: 'images/comparison/living_floor_before.jpg',
      after: 'images/comparison/living_floor_after.jpg'
    },
    bathroom_vanity: {
      title: 'Washbasin & Under-Counter Cabinet Deep Clean',
      before: 'images/comparison/bathroom_vanity_before.jpg',
      after: 'images/comparison/bathroom_vanity_after.jpg'
    },
    floor_tiles: {
      title: 'Kitchen & Utility Floor Tile Grout Scrubbing',
      before: 'images/comparison/floor_tiles_before.jpg',
      after: 'images/comparison/floor_tiles_after.jpg'
    }
  };

  const thumbCards = document.querySelectorAll('.comparison-thumb-card');

  // Unified switcher function
  const updateComparisonCategory = (cat) => {
    if (!comparisonData[cat]) return;

    // Update tab buttons
    tabButtons.forEach(btn => {
      const active = btn.getAttribute('data-category') === cat;
      btn.classList.toggle('active', active);
      btn.setAttribute('aria-selected', active ? 'true' : 'false');
    });

    // Update thumbnail cards
    thumbCards.forEach(card => {
      card.classList.toggle('active', card.getAttribute('data-category') === cat);
    });

    // Update image sources
    beforeImg.src = comparisonData[cat].before;
    afterImg.src = comparisonData[cat].after;
    if (categoryLabel) {
      categoryLabel.textContent = comparisonData[cat].title;
    }
    setSliderPosition(50);
  };

  // Tab button click
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const cat = btn.getAttribute('data-category');
      updateComparisonCategory(cat);
    });
  });

  // Thumbnail card click
  thumbCards.forEach(card => {
    card.addEventListener('click', () => {
      const cat = card.getAttribute('data-category');
      updateComparisonCategory(cat);
      if (comparisonSlider) {
        comparisonSlider.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    });
  });

  // Slider dragging logic
  let isDragging = false;

  const setSliderPosition = (percentage) => {
    const clamped = Math.max(0, Math.min(100, percentage));
    if (beforeLayer && sliderHandle) {
      beforeLayer.style.width = '100%';
      beforeLayer.style.clipPath = `inset(0 ${100 - clamped}% 0 0)`;
      beforeLayer.style.webkitClipPath = `inset(0 ${100 - clamped}% 0 0)`;
      sliderHandle.style.left = `${clamped}%`;
      sliderHandle.setAttribute('aria-valuenow', Math.round(clamped));
    }
  };

  const handleDrag = (clientX) => {
    if (!comparisonSlider) return;
    const rect = comparisonSlider.getBoundingClientRect();
    const xPos = clientX - rect.left;
    const percentage = (xPos / rect.width) * 100;
    setSliderPosition(percentage);
  };

  if (comparisonSlider) {
    // Mouse events
    comparisonSlider.addEventListener('mousedown', (e) => {
      isDragging = true;
      handleDrag(e.clientX);
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      handleDrag(e.clientX);
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
    });

    // Touch events
    comparisonSlider.addEventListener('touchstart', (e) => {
      isDragging = true;
      if (e.touches[0]) handleDrag(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener('touchmove', (e) => {
      if (!isDragging || !e.touches[0]) return;
      handleDrag(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener('touchend', () => {
      isDragging = false;
    });

    // Keyboard support for accessibility
    if (sliderHandle) {
      sliderHandle.addEventListener('keydown', (e) => {
        const current = parseInt(sliderHandle.getAttribute('aria-valuenow') || '50', 10);
        if (e.key === 'ArrowLeft') {
          setSliderPosition(current - 5);
          e.preventDefault();
        } else if (e.key === 'ArrowRight') {
          setSliderPosition(current + 5);
          e.preventDefault();
        }
      });
    }
  }

  /* -------------------------------------------------------------------------
     5. Service Link to Pre-fill Form
     ------------------------------------------------------------------------- */
  const serviceLinks = document.querySelectorAll('.service-link');
  const serviceSelect = document.getElementById('serviceType');
  const fullNameInput = document.getElementById('fullName');

  serviceLinks.forEach(link => {
    link.addEventListener('click', () => {
      const selected = link.getAttribute('data-service');
      if (serviceSelect && selected) {
        serviceSelect.value = selected;
      }
      setTimeout(() => {
        if (fullNameInput) fullNameInput.focus();
      }, 500);
    });
  });

  /* -------------------------------------------------------------------------
     6. Booking Form Validation & WhatsApp Redirect (No Date Field)
     ------------------------------------------------------------------------- */
  const bookingForm = document.getElementById('bookingForm');

  if (bookingForm) {
    const nameInput = document.getElementById('fullName');
    const phoneInput = document.getElementById('phoneNumber');
    const locationInput = document.getElementById('locationArea');

    const nameError = document.getElementById('nameError');
    const phoneError = document.getElementById('phoneError');
    const serviceError = document.getElementById('serviceError');
    const locationError = document.getElementById('locationError');

    const clearErrors = () => {
      [nameError, phoneError, serviceError, locationError].forEach(err => {
        if (err) err.style.display = 'none';
      });
      [nameInput, phoneInput, serviceSelect, locationInput].forEach(field => {
        if (field) field.classList.remove('invalid');
      });
    };

    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      clearErrors();

      let isValid = true;

      // Validate name
      if (!nameInput.value.trim()) {
        nameError.style.display = 'block';
        nameInput.classList.add('invalid');
        isValid = false;
      }

      // Validate phone (10 digits)
      const phoneVal = phoneInput.value.trim().replace(/[^0-9]/g, '');
      if (phoneVal.length < 10) {
        phoneError.style.display = 'block';
        phoneInput.classList.add('invalid');
        isValid = false;
      }

      // Validate service
      if (!serviceSelect.value) {
        serviceError.style.display = 'block';
        serviceSelect.classList.add('invalid');
        isValid = false;
      }

      // Validate location
      if (!locationInput.value.trim()) {
        locationError.style.display = 'block';
        locationInput.classList.add('invalid');
        isValid = false;
      }

      if (!isValid) return;

      // Format clean WhatsApp enquiry text
      const message = 
        `Hello Urban Deep Cleaning,\n\n` +
        `I would like to request a deep cleaning service with the following details:\n` +
        `• Name: ${nameInput.value.trim()}\n` +
        `• Mobile: ${phoneVal}\n` +
        `• Service: ${serviceSelect.value}\n` +
        `• Area / Location: ${locationInput.value.trim()}\n\n` +
        `Please confirm availability and provide a quote.`;

      const encodedMessage = encodeURIComponent(message);
      const whatsappUrl = `https://wa.me/917259312025?text=${encodedMessage}`;

      window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
    });
  }

  /* -------------------------------------------------------------------------
     7. Gallery Filter Controls & Lightbox (All 47 Authentic Photos)
     ------------------------------------------------------------------------- */
  const filterButtons = document.querySelectorAll('.filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxCaption = document.getElementById('lightboxCaption');
  const lightboxCounter = document.getElementById('lightboxCounter');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxPrev = document.getElementById('lightboxPrev');
  const lightboxNext = document.getElementById('lightboxNext');

  let currentGalleryIndex = 0;
  let activeGalleryData = [];

  const refreshActiveGallery = () => {
    activeGalleryData = [];
    galleryItems.forEach(item => {
      if (!item.classList.contains('hidden')) {
        activeGalleryData.push({
          element: item,
          src: item.getAttribute('data-full'),
          caption: item.getAttribute('data-caption')
        });
      }
    });
  };

  refreshActiveGallery();

  // Filter button clicks
  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      galleryItems.forEach(item => {
        const cat = item.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });

      refreshActiveGallery();
    });
  });

  // Lightbox click on items
  galleryItems.forEach(item => {
    item.addEventListener('click', () => {
      const idx = activeGalleryData.findIndex(d => d.element === item);
      if (idx !== -1) {
        openLightbox(idx);
      }
    });
  });

  const openLightbox = (index) => {
    currentGalleryIndex = index;
    updateLightbox();
    lightbox.classList.add('active');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  };

  const closeLightbox = () => {
    lightbox.classList.remove('active');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  };

  const updateLightbox = () => {
    const data = activeGalleryData[currentGalleryIndex];
    if (data && lightboxImg && lightboxCaption) {
      lightboxImg.src = data.src;
      lightboxCaption.textContent = data.caption;
      if (lightboxCounter) {
        lightboxCounter.textContent = `${currentGalleryIndex + 1} of ${activeGalleryData.length}`;
      }
    }
  };

  if (lightbox) {
    if (lightboxClose) {
      lightboxClose.addEventListener('click', closeLightbox);
    }

    if (lightboxPrev) {
      lightboxPrev.addEventListener('click', (e) => {
        e.stopPropagation();
        if (activeGalleryData.length === 0) return;
        currentGalleryIndex = (currentGalleryIndex - 1 + activeGalleryData.length) % activeGalleryData.length;
        updateLightbox();
      });
    }

    if (lightboxNext) {
      lightboxNext.addEventListener('click', (e) => {
        e.stopPropagation();
        if (activeGalleryData.length === 0) return;
        currentGalleryIndex = (currentGalleryIndex + 1) % activeGalleryData.length;
        updateLightbox();
      });
    }

    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) {
        closeLightbox();
      }
    });

    // Keyboard controls
    window.addEventListener('keydown', (e) => {
      if (!lightbox.classList.contains('active')) return;
      if (e.key === 'Escape') {
        closeLightbox();
      } else if (e.key === 'ArrowLeft') {
        if (activeGalleryData.length === 0) return;
        currentGalleryIndex = (currentGalleryIndex - 1 + activeGalleryData.length) % activeGalleryData.length;
        updateLightbox();
      } else if (e.key === 'ArrowRight') {
        if (activeGalleryData.length === 0) return;
        currentGalleryIndex = (currentGalleryIndex + 1) % activeGalleryData.length;
        updateLightbox();
      }
    });
  }

// 7. Video Player Interaction
  const cleaningVideo = document.getElementById('cleaningVideo');
  const videoPlayerWrap = document.querySelector('.video-player-wrap');
  if (cleaningVideo && videoPlayerWrap) {
    cleaningVideo.addEventListener('play', () => {
      videoPlayerWrap.classList.add('is-playing');
    });
    cleaningVideo.addEventListener('pause', () => {
      videoPlayerWrap.classList.remove('is-playing');
    });
    cleaningVideo.addEventListener('ended', () => {
      videoPlayerWrap.classList.remove('is-playing');
    });
  }
});
