// animation sélection qualité
const items = document.querySelectorAll(".format div");
const qualityInput = document.getElementById("qualityInput");

items.forEach(el => {
    el.addEventListener("click", () => {

        items.forEach(i => i.classList.remove("active"));
        el.classList.add("active");

        qualityInput.value = el.dataset.q;
    });
});

// petite animation bouton
const btn = document.getElementById("btn");

btn.addEventListener("mouseenter", () => {
    btn.style.transform = "scale(1.05)";
});

btn.addEventListener("mouseleave", () => {
    btn.style.transform = "scale(1)";
});