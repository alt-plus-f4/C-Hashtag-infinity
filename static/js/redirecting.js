let redirect = () => {
    const btn = document.querySelector('.search__submit');
    const input = document.querySelector('input');
    btn.addEventListener('click', () => {
        location.href += `/articles?search=${input.value}`;
    });
}

