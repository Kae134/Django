document.addEventListener("DOMContentLoaded", function() {
    let section_id = 1;
    let isScrolling = false;
    let loaded = true 
    if (loaded === true) {
        console.log(true)
        isScrolling = true;
        const element = document.getElementById(section_id);
        const targetPosition = element.offsetTop;
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
        setTimeout(function() {
            isScrolling = false;
        }, 1000);
        loaded = false;
    }

    function changeSection(direction) {
        const sections = document.querySelectorAll('section');
        const nextSectionId = direction === 'down' ? section_id + 1 : section_id - 1;
        if (nextSectionId >= 1 && nextSectionId <= sections.length) {
            const element = document.getElementById(nextSectionId);
            const targetPosition = element.offsetTop;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
            section_id = nextSectionId;
        }
    }

    window.addEventListener("wheel", function(event) {
        if (!isScrolling) {
            isScrolling = true;
            if (event.deltaY > 0) {
                changeSection('down');
            } else {
                changeSection('up');
            }
            setTimeout(function() {
                isScrolling = false;
            }, 1000);
        }
    });
});