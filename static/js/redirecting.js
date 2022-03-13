let redirect = () => {
    const btn = document.querySelector('.search__submit');
    const input = document.querySelector('input');
    location.href = "/path"
    location.href += `/articles?search=${input.value}`;
}
const input = document.querySelector('input');
document.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        location.href = "/path"
        location.href += `/articles?search=${input.value}`;
    }
});

let redirectUrl = (id) => {
    location.href = "/path"
    location.href += `/article?id=${id}`;
}

let redirectArticle = (id) => {
    let url = id.innerHTML;
    location.href = "/path"
    location.href += `/article?url=${url}`;
}


