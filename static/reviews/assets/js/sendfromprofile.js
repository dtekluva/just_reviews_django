sender   = document.querySelector('.username-message-target').innerHTML;

console.log(sender)
send     = document.querySelector('.send_btn');


function send_message(){
    message  = document.querySelector('.messaging').value;
    reciever = document.querySelector('select').value;
    document.querySelector('.messaging').value = ""
    fetch(`http://${ host }/reviews/messenger/${ sender }/${reciever}/${message}`)
    .then(res => {
        res.json()
        .then((data) => {
            console.log(data)
            
        })
    });
}

send.addEventListener("click", function(e){
    e.preventDefault();
    send_message();
});