import PostRequest, { GetRequest } from './request.js';

const add = (url, data) => {
    return new Promise((resolve, reject) => {
        PostRequest(url, data)
        .then(response => response.json())
        .then(data => resolve(data))
        .catch(error => reject(error))
    })
}

const getdata = (url) => {
    return new Promise((resolve, reject) => {
        GetRequest(url)
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
    const data = {
        'hostname': getValue('hostname'),
        'passphrase': getValue('pass'),
        'public_key': getValue('key'),
        'ipaddress': getValue('address')
    };

    const response = await PostRequest(url, data);
    if (response.ok) {
        form.parent().removeClass('block')
        form.parent().addClass('hidden')
        $('#success').removeClass('hidden')
    }
});


(async () => {
    const port = 8000;
    const url = `http://localhost:${port}/app/get_server`;
    const res = await GetRequest(url);

    if (res.ok) {
        const href = '/app/dashboard'
        $('#container').remove()
        $('nav ul li').first().addClass('bg-blue-700 text-white rounded-sm');
        $('#content').load(href).hide().fadeIn('slow');
    }
})();