const textarea = document.querySelector('textarea');
const counter = document.querySelector('.count');

function contarLetras() 
{
    const texto = textarea.value;
    const textoLength = textarea.value.length;
    
    counter.innerText = `${textoLength}`;
}
