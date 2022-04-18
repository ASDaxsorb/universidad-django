(() => {
  "strict-mode";
  const deleteButtons = document.querySelectorAll(".btn-delete");
  deleteButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      const confirm = window.confirm(
        "Estas seguro que deseas eliminar este curso?"
      );

      if (!confirm) {
        e.preventDefault();
      }
    });
  });
})();
