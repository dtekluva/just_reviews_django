username   = document.querySelector('.username-message-target').innerHTML;
message_target   = document.querySelector('.message');
body = document.querySelector(".contanier");

setInterval(
function check_message(){
    message  = document.querySelector('.message_target');
    fetch(`http://${ host }/reviews/check_message/${username}/`)
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
            message_box += '<hr><div style="text-align:left;"><h5 class="">From : ' +  element.from + '</h5></div><div><h4>' + element.body + '</h4></div><button class="reply_message btn btn-primary">Reply</button><hr>'
        }
        message_target.innerHTML = message_box;
    }
    reply_btn = document.getElementsByClassName("reply_message");
    for(var i = 0; i< reply_btn.length; i++){
        //console.log(reply_btn[i])
        reply_btn[i].addEventListener("click", function(e){
            //console.log(e)
            create_reply_box()
        })
    }
}

//function create_reply_box(){
    
    console.dir(body.innerHTML)
    body.removeChild(body.firstChild);
    body = '<div class="form-group"><label for="title">Reply message</label><input type="title" class="form-control2 form-control" id="" aria-describedby="title" placeholder="Enter Course Title of the Post" size="12"></div><button type="submit" class="btn btn-primary">Submit</button>';
//}


