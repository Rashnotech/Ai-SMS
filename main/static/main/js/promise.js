import PostRequest from './request.js';

const add = (url, data) => {
    return new Promise((resolve, reject) => {
        PostRequest(url, data)
        .then(response => response.json())
        .then(data => resolve(data))
        .catch(error => reject(error))
    })
}

const getValue = (attribute) => {
    return document.getElementById(attribute).value;
}

const form = document.getElementById('server_info');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const port = 8000
    const url = `http://localhost:${port}/app/add_server`
    const csrfToken = document.querySelector("input[name='csrfmiddlewaretoken']").value;
    const data = new FormData();
    data.append('csrfmiddlewaretoken', csrfToken);
    data.append('hostname', getValue('hostname'));
    data.append('pass_phrase', getValue('pass'));
    data.append('public_key', getValue('key'));
    data.append('ipaddress', getValue('address'));

    const response = await PostRequest(url, data);
    console.log(response);
})