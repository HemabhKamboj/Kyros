if (navigator.geolocation) { //check if geolocation is available
  navigator.geolocation.getCurrentPosition(function(position){
    console.log(`latitude`+position.coords.latitude);
    console.log(`longitutde`+position.coords.longitude);
    document.getElementById('map').src=`https://kyrosinnovatetoinspire.herokuapp.com/createmap?lat=${position.coords.latitude}&long=${position.coords.longitude}`;
  });   
}


var percent=document.querySelector('.percent');
var battery=document.querySelector('.battery');

var carBatteryPercentage=35;

// fetch(`https://kyrosinnovatetoinspire.herokuapp.com/cardata?carid=3`)
// .then(res=>res.json())
// .then(data=>{
// });

percent.textContent=carBatteryPercentage;
if(carBatteryPercentage<=20){
  battery.style.color='#E8290B';
}else if(carBatteryPercentage>20&&carBatteryPercentage<=50){
  battery.style.color='#ffb677';
}else if(carBatteryPercentage>50&&carBatteryPercentage<=80){
  battery.style.color='#A3CB37';
}else{
  battery.style.color='#019031';
}