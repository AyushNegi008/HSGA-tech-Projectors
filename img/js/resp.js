burger = document.querySelector('.burger')
navbar = document.querySelector('.navbar')
navList = document.querySelector('.nav-list')
line = document.querySelector('.line')
line2 = document.querySelector('.line2')



burger.addEventListener('click',()=>{
    navList.classList.toggle('v-class-resp');
    navbar.classList.toggle('h-nav-resp');
    burger.classList.toggle('icon');
    line.classList.toggle('top');
    line2.classList.toggle('bootom');
})



burger2 = document.querySelector('.burger2')
rightNav = document.querySelector('.rightNav')
rightNavinput = document.querySelector('.rightNavinput')
clear = document.querySelector('.clear')
btnsm= document.querySelector('.btnsm')
color2 = document.querySelector('.color2')


burger2.addEventListener('click',()=>{
    rightNav.classList.toggle('va-class-resp');
    rightNavinput.classList.toggle('vb-class-resp');
    clear.classList.toggle('vb-class-resp');
    btnsm.classList.toggle('vb-class-resp');
    color2.classList.toggle('no');


})
pocox = document.querySelector('.pocox')
section = document.querySelector('.section')
thumbnil = document.querySelector('.thumbnil')
para= document.querySelector('.para')



pocox.addEventListener('click',()=>{
    para.classList.toggle('v-resp');
    thumbnil.classList.toggle('v-resp');
    section.classList.toggle('h-resp');

})

pocoxa = document.querySelector('.pocoxa')
sectiona = document.querySelector('.sectiona')
thumbnila = document.querySelector('.thumbnila')
paraa= document.querySelector('.paraa')



pocoxa.addEventListener('click',()=>{
    paraa.classList.toggle('v-a-resp');
    thumbnila.classList.toggle('v-a-resp');
    sectiona.classList.toggle('h-a-resp');

})

function search_animal() {
    let input = document.getElementById('searchbar').value
    input=input.toLowerCase();
    let x = document.getElementsByClassName('animals');
      
    for (i = 0; i < x.length; i++) { 
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display="none";
        }
        else {
            x[i].style.display="list-item";                 
        }
    }
}