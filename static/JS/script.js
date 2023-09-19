// Navigation

const buttonOpen = document.querySelector("#open-side-btn");
const buttonClose = document.querySelector("#close-side-btn");
const aside = document.querySelector("aside");

function sideNavBarToggle() {
  // Function to toggle Side Navbar
  aside.classList.toggle("translate-x-0");
}

// add event to Open/Close Nav Button
buttonOpen.addEventListener("click", sideNavBarToggle);
buttonClose.addEventListener("click", sideNavBarToggle);

// Election Dropdown Info on all candidate page

const electionDropdownInfo = document.querySelectorAll(".election-drop-info");
electionDropdownInfo.forEach((dropButton) => {
  dropButton.onclick = () => {
    dropButton.querySelector("div").classList.toggle("hidden");
  };

  dropButton.querySelector("div").onmouseleave = (e) => {
    dropButton.querySelector("div").classList.add("hidden");
  }
  
});
