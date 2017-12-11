pass_retype = document.querySelector('.pass_retype_target');
pass_input  = document.querySelector('.pass_target');
signup_button = document.querySelector('.btn_target');
mismatch    = document.querySelector('.mismatch');
match       = document.querySelector('.match');

mismatch.style.display = "none" 
match.style.display = "none" 
signup_button.style.display = "none"

pass_retype.addEventListener('keyup', function(e){
    
    if (pass_input.value === pass_retype.value && (pass_retype.value).length >= 8){
        console.log("true heere")
        signup_button.style.display = "flex"
        mismatch.style.display = "none" 
        match.style.display = "flex"

    }else{
        signup_button.style.display = "none" 
        mismatch.style.display = "flex" 
        match.style.display = "none"
    }
})
