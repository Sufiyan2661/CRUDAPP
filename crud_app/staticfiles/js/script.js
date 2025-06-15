
  const toggleBtn = document.querySelector("[data-collapse-toggle]");
  const menu = document.getElementById("navbar-default");

  toggleBtn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
  });

