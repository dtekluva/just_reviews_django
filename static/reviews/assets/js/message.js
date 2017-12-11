sender   = document.querySelector('.sender_target').innerHTML;
reciever = document.querySelector('.reciever_target').innerHTML;

send     = document.querySelector('.send_btn');


function send_message(){
    message  = document.querySelector('.messaging').value;
    document.querySelector('.messaging').value = ""
    fetch(`http://10.100.200.134:8000/reviews/messenger/${ sender }/${reciever}/${message}`)
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