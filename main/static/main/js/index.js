// Copy message modal
const copyModal = new bootstrap.Modal(document.getElementById('copyMsgModal'));

// Copy from page
function copyTextFromElement(elementId) {
    const element = document.getElementById(elementId);
    if (!element) return;
    const textToCopy = element.innerText || element.textContent;
    navigator.clipboard.writeText(textToCopy)
        .then(() => {
            copyModal.show()
        })
        .catch(err => console.error('Ошибка:', err));
}


function updateNavbar() {
    document.getElementById('navbar').classList.toggle('bg-secondary', window.scrollY > 420);
}

// Add event listener
document.addEventListener('DOMContentLoaded', function() {
    const copyButton = document.getElementById('copy-button');
    const navbar = document.getElementById('navbar');

    if (copyButton) {
        copyButton.addEventListener('click', function() {
            copyTextFromElement('pills-tabContent');
        });
    };

    updateNavbar;
    window.addEventListener('scroll', updateNavbar);
    window.addEventListener('load', updateNavbar);

});