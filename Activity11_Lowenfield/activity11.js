//example14
const sBubble = document.querySelector(`.sBubble`)
const pBubble = document.querySelector(`.pBubble`)
const aBubble = document.querySelector(`.aBubble`)
sBubble.addEventListener(`click`,function(){
e.stopPropagation()
  alert(`SECTION was clicked`)
})
pBubble.addEventListener(`click`,function(){
  e.stopPropagation()
  alert(`PARAGRAPH was clicked`)
})
aBubble.addEventListener(`click`,function(){
  e.stopPropagation()
  alert(`LINK was clicked`)
})

//exaple13
const qccURL = document.querySelector('#qccURL')
qccURL.addEventListener(`click`,function(a){
  e.preventDefault();
  alert("QCC website is OFF")
})
//example12
const toTop = document.querySelector('.toTop')
window.addEventListener('scroll', function(){
  let pxTop = window.pageYOffset;
  if(pxTop>80){
    toTop.style.display='black'
  }
  else {
    toTop.style.display='none'
  }
})
//example 11
const display9 = document.querySelector('.display9')
window.addEventListener('scroll', function(){
  let pxTop = window.pageYOffset;
  display9.innerHTML = `Browser window is ${pxTop}px away form the top`
})
//example10

const inputTxt = document.querySelector('.inputTxt')
inputTxt.addEventListener('keydown',function(e){
alert(`key "${e.key}" pressed \n the ascii code for the key "${e.key} is ${e.which}"`)
})

const divColor = document.querySelectorAll('.divColor')
for(let eachDiv of divColor){
  eachDiv.addEventListener('mouseout',function(){
    eachDiv.style.backgroundColor = changeColor();}
)
  }

const colorContainer = document.querySelector('.colorContainer')
const btnColor = document.querySelector('#btnColor')
btnColor.addEventListener('click', function(){
const r = Math.floor( Math.random()*255)
const g = Math.floor( Math.random()*255)
const b = Math.floor( Math.random()*255)

colorContainer.style.backgroundColor = `rgb(${r},${g},${b})`
})


const btn6 = document.querySelector('#btn6')
btn6.addEventListener('mouseout',click1)
btn6.addEventListener('dbclick',click2)

function click1(){
  alert('button 6 = mouseout')
}

function click2(){
  alert('button 6 was double-clicked')
}

//example 5
const btn5 = document.querySelector('#btn5')
btn5.addEventListener('click',function(){
  alert('BUTTON 5 was clicked!')
})
const title = document.querySelector('title')
title.mouseover=function(){
  console.log('The title  was hovered on mouseout event');
}
const qccLink = document.querySelector('#qcclink')
qccLink.onclick = function(){
  console.log('QCC link was click');
}

qccLink.mouseover = testing;
function testing(){
  console.log('QCC link was hoverd or mouseover');
}
const btn2 = document.querySelector(`#btn2`)
btn2.onclick = function(){
  alert('Hi, there!')
}
