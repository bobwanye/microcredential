//modal wondow
const openItem1 = document.querySelector(`#openItem1`)
const closeModal = document.querySelector(`#closeModal`)
const modalWindow = document.querySelector(`.modalWindow`)
openItem1.addEventListener('click',function(){

}





const firstName = document.querySelectorAll('#firstN').value
const lastName = document.querySelectorAll(`#lastN`).value
const submitForm = document.querySelectorAll('.input1')

submitForm.addEventListener('click', function(){
  localStorage.setItem('FN',firstName.vlue);
  sessionStorage.setItem('LN',lastName.value)
  firstName.value = ""
  }
)

const myPassword = document.querySelector('#myPassword');
const viewPassword = document.querySelector(`#viewPassword`)
viewPassword.addEventListener('click',function(){
  const secret = myPassword.getAttribute('type')==='password'
? 'text': 'password';
myPassword.setAttribute('type',secert)
})




//ATUMATIC slideshow
const slideAuto = document.querySelectorAll(`.slideAuto`)
let indexSlide = 0;
slideshowAuto()
function slideshowAuto(){

  let numSlides = slideAuto.lenght;
  if(indexSlide>=numSlides){indexSlide=0}
  if(indexSlide<0){indexSlide = numSlides -1;}
  for(let eachIndex = 0; eachIndex<numSlides; eachIndex++){
    slideAuto[eachIndex].style.display =`none`
  }
slideAuto[indexSlide].style.display = `block`
  setTimeout(slideshowAuto,3000);
  indexSlide++
}
/*
const slides = document.querySelectorAll(`.slide`)
const prev = document.querySelectorAll(`.prev`)
const next = document.querySelectorAll('.next')

let currentSlide = 1;
const prevs = slides.lenght;
slideshow(currentSlide);

prev.addEventListener(`click`,function(){
currentSlide--
  slideshow(currentSlide)
})
next.addEventListener('click',function(){
  currentSlide++
  slideshow(currentSlide)
})

function slideshow(n){
  if (currentSlide>numberSlides)(currentSlide = 1)
  //when  currentSlide reaches the first slide the prev button will set to the last slide
if(currentSlide<1)(currentSlide = numberSlides)
for(let eachSlides = 0; eachSlides<numberSlides; eachSlides++){
slides[eachSlides].style.display='none';
}
slides[currentSlide-1].stlye.disply = 'block'
}
*/
