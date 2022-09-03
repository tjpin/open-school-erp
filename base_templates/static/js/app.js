const tabs = document.querySelectorAll(".sidebar .tab-button");
const contents = document.querySelectorAll(".dashboard-content .tab-panel");

tabs[0].classList.add('active-tab');
contents[0].classList.add("active-container");

const removeActiveClass = () => {
    tabs.forEach((tab, index) => {
        tab.classList.remove("active-tab");
        contents[index].classList.remove("active-container");
    });
};

tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
        
        removeActiveClass();
        contents[index].classList.add("active-container");
        tab.classList.add('active-tab');
    });
});



