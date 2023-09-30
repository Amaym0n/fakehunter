document.addEventListener("DOMContentLoaded", function () {
    const themeSwitch = document.querySelector("#theme-switch");

    // Переключение темы
    themeSwitch.addEventListener("change", function () {
        if (themeSwitch.checked) {
            document.body.classList.add("dark-theme");
            document.querySelectorAll(".login-container").forEach((element) => {
                element.classList.add("dark-theme");
            });
            document.querySelectorAll(".form-group").forEach((element) => {
                element.classList.add("dark-theme");
            });
            document.querySelectorAll(".button").forEach((element) => {
                element.classList.add("dark-theme");
            });
        } else {
            document.body.classList.remove("dark-theme");
            document.querySelectorAll(".login-container").forEach((element) => {
                element.classList.remove("dark-theme");
            });
            document.querySelectorAll(".form-group").forEach((element) => {
                element.classList.remove("dark-theme");
            });
            document.querySelectorAll(".button").forEach((element) => {
                element.classList.remove("dark-theme");
            });
        }
    });
});
