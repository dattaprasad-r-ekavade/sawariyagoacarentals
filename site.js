document.documentElement.classList.add("js");

(function () {
  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();

  var nav = document.getElementById("nav");
  var menuBtn = document.getElementById("menuBtn");
  var navLinks = document.getElementById("navLinks");

  if (nav) {
    var onScroll = function () {
      nav.classList.toggle("scrolled", window.scrollY > 40);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  if (menuBtn && navLinks) {
    menuBtn.addEventListener("click", function () {
      var open = navLinks.classList.toggle("open");
      menuBtn.classList.toggle("open", open);
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    navLinks.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        navLinks.classList.remove("open");
        menuBtn.classList.remove("open");
        menuBtn.setAttribute("aria-expanded", "false");
      });
    });
  }

  var filters = document.querySelectorAll("[data-fleet-filter]");
  var cards = document.querySelectorAll("[data-fleet]");
  if (filters.length && cards.length) {
    filters.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var cat = btn.getAttribute("data-fleet-filter");
        filters.forEach(function (b) {
          b.classList.toggle("is-active", b === btn);
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        cards.forEach(function (card) {
          var match = cat === "all" || card.getAttribute("data-fleet") === cat;
          card.classList.toggle("is-hidden", !match);
        });
      });
    });
  }

  document.querySelectorAll('a[href*="wa.me"]').forEach(function (a) {
    a.addEventListener("click", function () {
      var label = a.getAttribute("data-cta") || (a.textContent || "").trim();
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({ event: "whatsapp_click", method: "whatsapp", event_label: label });
      if (typeof gtag === "function") {
        gtag("event", "generate_lead", { method: "whatsapp", event_label: label });
      }
    });
  });

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });
  }
})();
