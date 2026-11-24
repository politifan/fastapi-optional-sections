const gallery = document.querySelector(".chapter-grid");
const stage = gallery.querySelector(".stage");
const cards = [...gallery.querySelectorAll("[data-chapter]")];
const notes = [...gallery.querySelectorAll("[data-note]")];
const counter = gallery.querySelector(".chapter-count");
const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
let selected = 0;

function selectChapter(index) {
    selected = (index + cards.length) % cards.length;

    cards.forEach((card, position) => {
        const offset = (position - selected + cards.length) % cards.length;
        card.dataset.position = offset === 2 ? -1 : offset;
        card.setAttribute("aria-pressed", position === selected);
        notes[position].hidden = position !== selected;
    });

    counter.textContent = `${String(selected + 1).padStart(2, "0")} / ${String(cards.length).padStart(2, "0")}`;
}

cards.forEach((card, index) => {
    card.addEventListener("click", () => selectChapter(index));
});

gallery.querySelectorAll("[data-step]").forEach((button) => {
    button.addEventListener("click", () => selectChapter(selected + Number(button.dataset.step)));
});

gallery.addEventListener("keydown", (event) => {
    if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
    event.preventDefault();
    selectChapter(selected + (event.key === "ArrowRight" ? 1 : -1));
    if (cards.includes(event.target)) cards[selected].focus();
});

stage.addEventListener("pointermove", (event) => {
    if (reducedMotion.matches || event.pointerType !== "mouse" || event.target.closest(".postcard")) return;
    const bounds = stage.getBoundingClientRect();
    const x = (event.clientX - bounds.left) / bounds.width - 0.5;
    const y = (event.clientY - bounds.top) / bounds.height - 0.5;
    stage.style.setProperty("--tilt-x", `${-y * 12}deg`);
    stage.style.setProperty("--tilt-y", `${x * 18}deg`);
});

stage.addEventListener("pointerleave", () => {
    stage.style.removeProperty("--tilt-x");
    stage.style.removeProperty("--tilt-y");
});
