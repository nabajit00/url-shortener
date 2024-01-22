function validateURL(url) {
    try{
        new URL(url);
    } catch(error){
        console.log(error)
        return false;
    }
    return true;
}

const formEle = document.querySelector('form');
const urlInputEle = document.getElementById('url_input');

formEle.addEventListener('submit',(event)=>{
    const url = event.target.url.value;

    if(!validateURL(url)){
        event.preventDefault();
        event.stopPropagation();
        return false;
    }
    return true;
})

function copyText(event,text){
    const textarea = document.createElement('textarea');

    textarea.style.position = 'absolute';
    
    textarea.value = text;
    
    document.body.appendChild(textarea);
    
    textarea.select();
    
    document.execCommand('copy');
    
    document.body.removeChild(textarea);

    event.preventDefault();
}