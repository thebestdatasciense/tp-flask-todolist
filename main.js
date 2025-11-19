document.addEventListener("DOMContentLoaded", function () {
  // Validation côté client : empêcher ajout si titre vide
  const addForm = document.getElementById("add-form");
  if (addForm) {
    addForm.addEventListener("submit", function (e) {
      const title = document.getElementById("title").value.trim();
      if (!title) {
        e.preventDefault();
        alert("Veuillez entrer un titre pour la tâche.");
      }
    });
  }

  // Confirmation avant suppression
  const deleteForms = document.querySelectorAll("form[action^='/delete']");
  deleteForms.forEach(form => {
    form.addEventListener("submit", function (e) {
      const ok = confirm("Voulez-vous vraiment supprimer cette tâche ?");
      if (!ok) e.preventDefault();
    });
  });

});
