// menu button action
function toggleMenu() {
    let list = document.querySelector('#navbar-default');
    let closeBtn = document.querySelector('#closeBtn');
    let menuBtn = document.querySelector('#menuBtn');
  
    list.classList.toggle('hidden');
    closeBtn.classList.toggle('hidden');
    menuBtn.classList.toggle('hidden');
  }

function toggleCatMenu() {
    let list = document.querySelector('#dropdown-menu');
    let menuBtn = document.querySelector('#dropdown-btn');
  
    list.classList.toggle('hidden');
    // menuBtn.classList.toggle('hidden');
  }

function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  section.scrollIntoView({ behavior: 'smooth' });
}

// ==================================================

// alert("js alert !!!")

// const burger = document.querySelector('#burger');
// const menu = document.querySelector('#menu');


// burger.addEventListener('click', () => {
//     if (menu.classList.contains('hidden')){
//         menu.classList.remove('hidden');
//     } else{
//         menu.classList.add('hidden');
//     }
// })

// const home = document.querySelector('#homeTab');
// const about = document.querySelector('#aboutTab');
// const contact = document.querySelector('#contactTab');

// home.addEventListener('click', () => {
//     if (home.classList.contains('border-red-500')){
//         about.classList.remove('border-red-500');
//         contact.classList.remove('border-red-500');
//     }else{
//         home.classList.add('border-red-500');
//         about.classList.remove('border-red-500');
//         contact.classList.remove('border-red-500');
//     }
// })

// about.addEventListener('click', () => {
//     if (about.classList.contains('border-red-500')){
//         home.classList.remove('border-red-500');
//         contact.classList.remove('border-red-500');
//     }else{
//         about.classList.add('border-red-500');
//         home.classList.remove('border-red-500');
//         contact.classList.remove('border-red-500');
//     }
// })

// contact.addEventListener('click', () => {
//     if (contact.classList.contains('border-red-500')){
//         home.classList.remove('border-red-500');
//         about.classList.remove('border-red-500');
//     }else{
//         contact.classList.add('border-red-500');
//         home.classList.remove('border-red-500');
//         about.classList.remove('border-red-500');

//     }
// })


// const carouselSlides = [
// document.querySelector('#Carousel_slide1'),
// document.querySelector('#Carousel_slide2'),
// document.querySelector('#Carousel_slide3'),
// document.querySelector('#Carousel_slide4'),
// document.querySelector('#Carousel_slide5')
// ];

// const prevBtn = document.querySelector('#prevBTN');
// const nextBtn = document.querySelector('#nextBTN');

// let currentSlide = 0;

// const showSlide = (slideIndex) => {
// carouselSlides.forEach((slide, index) => {
//     if (index === slideIndex) {
//     slide.classList.remove('hidden');
//     } else {
//     slide.classList.add('hidden');
//     }
// });
// };

// const nextSlide = () => {
// currentSlide++;
// if (currentSlide >= carouselSlides.length) {
//     currentSlide = 0;
// }
// showSlide(currentSlide);
// };

// const prevSlide = () => {
// currentSlide--;
// if (currentSlide < 0) {
//     currentSlide = carouselSlides.length - 1;
// }
// showSlide(currentSlide);
// };

// prevBtn.addEventListener('click', () => {
// prevSlide();
// });

// nextBtn.addEventListener('click', () => {
// nextSlide();
// });

// setInterval(() => {
// nextSlide();
// }, 5000); // Change slide every 10 seconds
