const navList = document.querySelector("#nav-list-burger");
const mobileMenuToggle = document.getElementById('mobile-menu');

mobileMenuToggle.addEventListener('click', () => {
    mobileMenuToggle.classList.toggle('change');
    navList.classList.toggle('active-nav-burger');
});
