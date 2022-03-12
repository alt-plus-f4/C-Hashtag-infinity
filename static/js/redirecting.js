let redirect = () => {
    const btn = document.querySelector('.search__submit');
    const input = document.querySelector('input');
    location.href += `../articles?search=${input.value}`;
}
const input = document.querySelector('input');
document.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        location.href += `../articles?search=${input.value}`;
    }
});


