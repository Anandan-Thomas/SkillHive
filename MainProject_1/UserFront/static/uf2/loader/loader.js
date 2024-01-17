window.addEventListener("load", () => {
  const loader = document.querySelector(".loader");

  // Add a delay (e.g., 2000 milliseconds = 2 seconds)
  setTimeout(() => {
    loader.classList.add("loader--hidden");

    loader.addEventListener("transitionend", () => {
      document.body.removeChild(loader);
    });
  }, 2000); // Adjust the delay as needed
});
