
function addElements() {

   if (window.innerWidth > 768) {
    console.log('Media Query Matched!');
  }
}

window.addEventListener('resize', checkMediaQuery);


 function checkMediaQuery() {

  if (window.innerWidth > 768) {
    console.log('Media Query is more than 768px!');

  }  else if (window.innerWidth < 768) {
      console.log('Media Query is less than 768px!');
  }
}