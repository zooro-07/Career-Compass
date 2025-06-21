document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".container, .btn, .chat-bubble");

    elements.forEach((el, i) => {
        el.style.opacity = 0;
        el.style.transform = "translateY(20px)";
        setTimeout(() => {
            el.style.transition = "all 0.6s ease";
            el.style.opacity = 1;
            el.style.transform = "translateY(0)";
        }, i * 150);
    });
});
