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

