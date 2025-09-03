// Projact additional images modal
const imagesModal = new bootstrap.Modal(document.getElementById('imagesModal'));

// Set inactive for all nav buttons
function deactivateAllProjectButtons() {
    document.querySelectorAll('.nav-link').forEach(button => {
        if (button.classList.contains('active')) {
            button.classList.remove('active');
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const category = JSON.parse(document.getElementById('category').textContent);

    document.getElementById('navbar').classList.add('bg-secondary'); 

    deactivateAllProjectButtons();
    // Get category slug from server and activate corresponding button
    if (! category) {
        const btn_all = document.getElementById('btn_all');
        if (btn_all) {
            btn_all.classList.add('active')
        };
    } else {
        const button_id = `btn_${category}`;
        document.getElementById(button_id).classList.add('active');
};

  // Show images Modal
  document.querySelectorAll('.btn-images').forEach(button => {
        button.addEventListener('click', function() {
          const projectPk = this.getAttribute('project-pk');
          const projectTitle = this.getAttribute('project-title');

          document.getElementById('imagesModalLabel').textContent = projectTitle;

          // Get Modal body from AJAX
          fetch(`/get_project_images/${projectPk}`)
            .then(response => response.text())
            .then(html => {
              if (html != '404') {
                document.getElementById('images-body').innerHTML = html;
                imagesModal.show();
              }
            });
      });
    });

});