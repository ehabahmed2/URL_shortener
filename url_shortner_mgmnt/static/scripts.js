/** @format */

// Add smooth scroll for the About section link
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});

// Animation on load (for the hero section)
document.addEventListener("DOMContentLoaded", function () {
  const heroTitle = document.querySelector(".hero h1");
  const heroSubtitle = document.querySelector(".hero p");

  heroTitle.classList.add("animate__animated", "animate__fadeInDown");
  heroSubtitle.classList.add("animate__animated", "animate__fadeInUp");
});
