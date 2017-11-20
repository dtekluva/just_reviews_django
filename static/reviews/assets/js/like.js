function thumbsup(slug, username){
    fetch(`http://localhost:8000/reviews/thumbs_up/${ slug }/${username}`)
     .then(res => {
         res.json()
         .then((data) => {
            console.log(document.getElementsByClassName(slug)[0].innerHTML)
            document.getElementsByClassName(slug)[0].innerHTML = ' '+data.like;
            alert("liked")
         })
     });
};



function thumbsdown(slug, username){
   
        fetch(`http://localhost:8000/reviews/thumbs_down/${ slug }/${username}`)
        .then(res => {
            res.json()
            .then((data) => {
                console.log(data)
                var now = (document.getElementsByClassName("dis-" + slug))[0];
                console.log(now)
                
                // console.log(now.document.getElementsByClassName(slug))
                now.innerHTML = ' '+data.dislike;
                alert("Disliked")
            })
        });
    }
    



function back_comment(comment_id, username){
    console.log("got here")
    
        fetch(`http://localhost:8000/reviews/back_comment/${ comment_id }/${username}`)
        .then(res => {
            res.json()
            .then((data) => {
                console.log(data)
               document.getElementsByClassName(comment_id)[0].innerHTML = ' '+data.backs+'Backs |';
               alert("Backed")
            })
        });
    }

function addtime(){
    var comments = Array.from(document.getElementsByClassName('comment_time'));


    comments.forEach((comment) => {
        
        console.log(comment.innerHTML)

        // const comment_id = (_this.attributes[0].value).slice(5);
        fetch(`http://localhost:8000/reviews/was_added/`)
        .then((resp) => resp.json())
        .then(function(data) {
        
                console.log(data)
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