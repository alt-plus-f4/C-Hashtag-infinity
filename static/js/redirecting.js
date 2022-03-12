let redirect = () => {
    const btn = document.querySelector('.search__submit');
    const input = document.querySelector('input');
<<<<<<< HEAD
    location.href += `../articles?search=${input.value}`;
=======
    btn.addEventListener('click', () => {
        location.href += `/articles?search=${input.value}`;
    });
>>>>>>> 34ec03411e4c50855ff992db6ea490cc5bf8149b
}

const input = document.querySelector('input');
document.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        location.href += `../articles?search=${input.value}`;
    }
});


