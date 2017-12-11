username   = document.querySelector('.username_target').innerHTML;
message_target   = document.querySelector('.message');
console.log(message_target)
username = (username.trim().slice(11,18))

setInterval(
function check_message(){
    message  = document.querySelector('.message_target');
    fetch(`http://10.100.200.134:8000/reviews/check_message/${username}/`)
    .then(res => {
        res.json()
        .then((data) => {
            serialize(data.message);
        })
    });
}
, 1000);

function serialize(array){
    // console.log(typeof array);
    var message_box = "";
    
    for (const key in array) {
        if (array.hasOwnProperty(key)) {
            const element = array[key];
            message_box += '<hr><div style="text-align:left;"><h5 class="">From : ' +  element.from + '</h5></div><div><h4>' + element.body + '</h4></div><hr>'
        }
        message_target.innerHTML = message_box;
    }
   
}


