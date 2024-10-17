const tabs = document.querySelector(".nav-tabs");
const btns = document.querySelectorAll(".nav-link");
const tabpanes = document.querySelectorAll(".tab-pane");

const myNodelist = document.querySelectorAll(".nav-link");
  for (let i = 0; i < myNodelist.length; i++) {
    myNodelist[0].classList.add("active");
  }

firstMenu = btns[0].dataset.id;
if(firstMenu) {
  // btns.forEach((btn) => {
  //  btn.classList.remove("active");
  // });
  const element = document.getElementById(firstMenu);
  element.classList.add("active");
  element.classList.add("show");
  tabpanes.forEach((tabpane) => {
    tabpane.classList.remove("active");
    tabpane.classList.remove("show");
  });
  element.classList.add("active");
  element.classList.add("show");

}

tabs.addEventListener('click', (event) => {
  const id = event.target.dataset.id;
  if(id) {
    btns.forEach((btn) => {
      btn.classList.remove("active");
    });
    event.target.classList.add("active");
    tabpanes.forEach((tabpane) => {
      tabpane.classList.remove("active");
      tabpane.classList.remove("show");
    });
    const element = document.getElementById(id);
    element.classList.add("active");
    element.classList.add("show");
  }
});





// document.querySelectorAll('.nav-item').forEach(tabmenu => {
//     tabmenu.addEventListener('click', function(event) {
//         const id = event.target;
//         console.log(id)
//         if(id) {

//         }
//     });
//   });