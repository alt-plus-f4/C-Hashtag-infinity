let redirect = () => {
    const btn = document.querySelector('.search__submit');
    const input = document.querySelector('input');
    //location.assign("/");
    location.href = `/articles?search=${input.value}`;
}
const input = document.querySelector('input');
document.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        //location.assign("/");
        location.href = `/articles?search=${input.value}`;
    }
});

let redirectUrl = (id) => {
    location.assign("/");
    location.href = `solar_system/article?id=${id}`;
}

let redirectArticle = (id) => {
    let url = id.innerHTML;
    //location.assign("/");
    location.href = `/article?url=${url}`;
}


