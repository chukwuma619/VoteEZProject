// Navigation

const buttonOpen = document.querySelector('#open-side-btn');
const buttonClose = document.querySelector('#close-side-btn')
const aside = document.querySelector('aside')

function sideNavBarToggle() {
    // Function to toggle Side Navbar
    aside.classList.toggle("translate-x-0")
}

// add event to Open/Close Nav Button
buttonOpen.addEventListener('click', sideNavBarToggle)
buttonClose.addEventListener('click', sideNavBarToggle)


// Election Deatils Button

const electionDetailsButton = document.querySelectorAll('#election-detail-btn');

for (const button of electionDetailsButton) {
    button.addEventListener('click', (e)=>{
        const detailList = e.currentTarget.parentElement.querySelector('div')
        detailList.style.display = "absolute"
        console.log(detailList.classList);

        // const  = parentButtonContainer.querySelector('div')
        // console.log(detailList.classList);
    })
}
