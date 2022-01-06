var dateObj = new Date();

// console.log(dateObj.getUTCDate());
// document.getElementById("date-time").innerHTML = dateObj.toLocaleDateString();

// var dateTimeSpan = document.getElementById("date-time");

// setInterval(function(){
//     // i++;
//     // console.log('wew' , i);
//     // var dateObj = new Date();
//     // dateTimeSpan.innerHTML
//     document.getElementById("date-time").innerHTML = dateObj;

// }, 1000);

function onInputChange(e){
    // document.getElementById("firstname").style = "border solid red"
    // console.log(document.getElementById("firstname").value);console.log(document.getElementById("lasttname").value);

    // console.log(this)
    // e.style = "border:1px solid green";

    // console.log(e.getAttribute("id"));
    var selectedId = e.getAttribute("id");

    if(selectedId === "firstname" && e.value === ""){
        e.style = "border:2px solid red";
    }else if(selectedId === "firstname" && e.value !== ""){
        e.style = "border:2px solid green";
    }
};