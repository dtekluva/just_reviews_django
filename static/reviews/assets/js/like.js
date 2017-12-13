host = "10.100.200.134:8000"

function thumbsup(slug, username){
    fetch(`http://${ host }/reviews/thumbs_up/${ slug }/${username}`)
     .then(res => {
         res.json()
         .then((data) => {
            console.log(document.getElementsByClassName(slug)[0].innerHTML)
            document.getElementsByClassName(slug)[0].innerHTML = ' '+data.like;
         })
     });
};
function thumbsdown(slug, username){
   
    fetch(`http://${ host }/reviews/thumbs_down/${ slug }/${username}`)
    .then(res => {
        res.json()
        .then((data) => {
            //console.log(data)
            var now = (document.getElementsByClassName("dis-" + slug))[0];
            //console.log(now)
            
            // console.log(now.document.getElementsByClassName(slug))
            now.innerHTML = ' '+data.dislike;
        })
    });
}
function back_comment(comment_id, username){
    
    fetch(`http://${ host }/reviews/back_comment/${ comment_id }/${username}`)
    .then(res => {
        res.json()
        .then((data) => {
            //console.log(data)
            document.getElementsByClassName(comment_id)[0].innerHTML = ' '+data.backs+'Backs |';
        })
    });
}
function addtime(){
    var comments = Array.from(document.getElementsByClassName('comment_time'));


    comments.forEach((comment) => {
        
        console.log(comment.innerHTML)

        // const comment_id = (_this.attributes[0].value).slice(5);
        fetch(`http://${ host }/reviews/was_added/`)
        .then((resp) => resp.json())
        .then(function(data) {
        
                //console.log(data)
                time_difference = data.time - parseInt(comment.innerHTML)
                proccesed_time  = datify_seconds(time_difference)
               comment.innerHTML = " " + Math.round(proccesed_time.elapsed) + proccesed_time.unit + " ago " + "|"  ;
            });
        });
}
function datify_seconds(seconds){
    if (seconds < 61){
        
        conv=seconds
        result = { elapsed : conv , unit : "secs" }
        return result
        
    }
    if (seconds < 3601){
    
        conv=seconds/60
        result = { elapsed : conv , unit : "mins" }
        return result
    }
    if (seconds < 86400){
        
        conv=seconds/3600
        result = { elapsed : conv , unit : "hrs" }
        return result
    }

    if (seconds < 607800){
        
        conv=seconds/86400
        result = { elapsed : conv , unit : "days" }
        return result
    }

    if (seconds < 2419200){
        
        conv=seconds/607800 
        result = { elapsed : conv , unit : "weeks" }
        return result
        
    }

    if (seconds < 29030400){

        conv=seconds/2419200
        result = { elapsed : conv , unit : "months" }
        return result
    }

    if (seconds > 29030400){
        
        conv=seconds/29030400
        result = { elapsed : conv , unit : "yrs" }
        return result
    }

    return seconds;
}
function authenticate(){
    fetch(`http://10.100.200.134:8000/reviews/thumbs_down/${ slug }/${username}`)
    .then(res => {
        res.json()
        .then((data) => {
            console.log(data)
            var now = (document.getElementsByClassName("dis-" + slug))[0];
            console.log(now)
            
            // console.log(now.document.getElementsByClassName(slug))
            now.innerHTML = ' '+data.dislike;
            //alert("Disliked")
        })
    });  
}
//switch display in profile view
function switch_display(){
    target   = document.getElementsByClassName("switcher");
    edit_details = document.getElementsByClassName("edit_details")
    view_details = document.getElementsByClassName("view_details")

    target[0].addEventListener("click", function(){
        edit_details[0].style.display = "";
        view_details[0].style.display = "none";
    })
}


switch_display();
