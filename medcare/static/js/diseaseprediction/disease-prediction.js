document.addEventListener("DOMContentLoaded", () => {
    const slides = document.getElementById("slides");
    const slideElements = document.querySelectorAll(".slide");
    const nextBtn = document.getElementById("next");
    const prevBtn = document.getElementById("prev");

    let index = 1;
    let autoSlide;
    let isPaused = false;
    const totalSlides = slideElements.length;
    const slideWidth = 85; 

    function updateSlidePosition(transition = true) {
        slides.style.transition = transition ? "transform 1s ease-in-out" : "none";
        slides.style.transform = `translateX(-${index * slideWidth}vw)`;
    }

    function nextSlide() {
        if (index >= totalSlides - 1) {
            index = 1;
            updateSlidePosition(false);
        }
        setTimeout(() => {
            index++;
            updateSlidePosition();
        }, 50);
    }

    function prevSlide() {
        if (index <= 0) {
            index = totalSlides - 2;
            updateSlidePosition(false);
        }
        setTimeout(() => {
            index--;
            updateSlidePosition();
        }, 50);
    }

    function startAutoSlide() {
        autoSlide = setInterval(() => {
            if (!isPaused) nextSlide();
        }, 3000);
    }

    function stopAutoSlide() {
        clearInterval(autoSlide);
    }

    nextBtn.addEventListener("click", () => {
        stopAutoSlide();
        nextSlide();
        startAutoSlide();
    });

    prevBtn.addEventListener("click", () => {
        stopAutoSlide();
        prevSlide();
        startAutoSlide();
    });

    slides.addEventListener("mousedown", () => {
        isPaused = true;
    });

    slides.addEventListener("mouseup", () => {
        isPaused = false;
    });

    updateSlidePosition(false);
    startAutoSlide();
});
