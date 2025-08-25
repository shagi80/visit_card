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

// Add event listener
document.addEventListener('DOMContentLoaded', function() {
    const copyButton = document.getElementById('copy-button');
    if (copyButton) {
        copyButton.addEventListener('click', function() {
            copyTextFromElement('content-to-copy');
        });
    }
});