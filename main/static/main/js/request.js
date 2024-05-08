const PostRequest = (url, data) => {
    return fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
    });
}

export const GetRequest = (url) => {
    return fetch(url, {
        method: 'GET'
    });
}

export default PostRequest;