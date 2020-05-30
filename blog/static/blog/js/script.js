const open_menu = document.querySelector(".menu-btn");
const nav_container = document.querySelector(".nav-container");

const mobile_logo = document.querySelector(".logo");

open_menu.addEventListener("click", () => {
    nav_container.classList.toggle("active");
    mobile_logo.classList.toggle("active");
});
