/* TechMart Main JS */

document.addEventListener('DOMContentLoaded', function () {

  // ---- Countdown Timer ----
  function startCountdown(endTime) {
    const timer = document.getElementById('deal-timer');
    if (!timer) return;
    function update() {
      const diff = endTime - Date.now();
      if (diff <= 0) { timer.innerHTML = '<span class="text-white">Deal Ended</span>'; return; }
      const h = Math.floor(diff / 3600000);
      const m = Math.floor((diff % 3600000) / 60000);
      const s = Math.floor((diff % 60000) / 1000);
      const fmt = n => String(n).padStart(2, '0');
      document.getElementById('timer-h').textContent = fmt(h);
      document.getElementById('timer-m').textContent = fmt(m);
      document.getElementById('timer-s').textContent = fmt(s);
    }
    update();
    setInterval(update, 1000);
  }
  const dealEnd = Date.now() + 8 * 3600 * 1000 + 23 * 60 * 1000 + 45 * 1000;
  startCountdown(dealEnd);

  // ---- Quantity Stepper ----
  document.querySelectorAll('.qty-stepper').forEach(function (stepper) {
    const minusBtn = stepper.querySelector('.qty-minus');
    const plusBtn = stepper.querySelector('.qty-plus');
    const valEl = stepper.querySelector('.qty-val');
    if (!minusBtn || !plusBtn || !valEl) return;
    const min = parseInt(valEl.dataset.min || 1);
    const max = parseInt(valEl.dataset.max || 99);
    minusBtn.addEventListener('click', function () {
      let v = parseInt(valEl.value);
      if (v > min) valEl.value = v - 1;
    });
    plusBtn.addEventListener('click', function () {
      let v = parseInt(valEl.value);
      if (v < max) valEl.value = v + 1;
    });
  });

  // ---- Gallery Thumbs ----
  document.querySelectorAll('.gallery-thumb').forEach(function (thumb) {
    thumb.addEventListener('click', function () {
      const mainImg = document.getElementById('main-product-img');
      if (mainImg) mainImg.src = this.dataset.src;
      document.querySelectorAll('.gallery-thumb').forEach(t => t.classList.remove('active'));
      this.classList.add('active');
    });
  });

  // ---- Star Rating Picker ----
  document.querySelectorAll('.star-picker').forEach(function (picker) {
    const stars = picker.querySelectorAll('i');
    const input = document.getElementById('id_rating');
    stars.forEach(function (star, index) {
      star.addEventListener('mouseenter', function () {
        stars.forEach((s, i) => {
          s.classList.toggle('bi-star-fill', i <= index);
          s.classList.toggle('bi-star', i > index);
        });
      });
      star.addEventListener('mouseleave', function () {
        const current = input ? parseInt(input.value) : 0;
        stars.forEach((s, i) => {
          s.classList.toggle('bi-star-fill', i < current);
          s.classList.toggle('bi-star', i >= current);
        });
      });
      star.addEventListener('click', function () {
        if (input) input.value = index + 1;
        stars.forEach((s, i) => {
          s.classList.toggle('bi-star-fill', i <= index);
          s.classList.toggle('bi-star', i > index);
        });
      });
    });
  });

  // ---- Toast auto-dismiss ----
  document.querySelectorAll('.alert-dismissible').forEach(function (alert) {
    setTimeout(function () {
      const btn = alert.querySelector('[data-bs-dismiss]');
      if (btn) btn.click();
    }, 5000);
  });

  // ---- Cart quantity update on change ----
  document.querySelectorAll('.cart-qty-form').forEach(function (form) {
    const input = form.querySelector('input[name="quantity"]');
    if (input) {
      input.addEventListener('change', function () {
        form.submit();
      });
    }
  });

  // ---- Smooth scroll ----
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ---- Sticky navbar shadow ----
  window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
      navbar.style.boxShadow = window.scrollY > 10
        ? '0 2px 20px rgba(0,0,0,.08)'
        : '0 1px 0 #e2e8f0';
    }
  });

  // ---- Price range display ----
  const priceRange = document.getElementById('price-range');
  const priceVal = document.getElementById('price-range-val');
  if (priceRange && priceVal) {
    priceRange.addEventListener('input', function () {
      priceVal.textContent = '£' + this.value;
    });
  }
});
