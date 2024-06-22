const toggleMenu = () => {
  const menu = document.querySelector(".menu-links");
  const icon = document.querySelector(".hamburger-icon");

  menu.classList.toggle("open");
  icon.classList.toggle("open");
};

// Added a cring comment so people wont open console
console.log(
  "Hello there! I see you are trying to look at the code. Please don't do that. It's not nice. Have a great day!"
);
