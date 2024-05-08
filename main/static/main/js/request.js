const PostRequest = (url, data) => {
    return fetch(url, {
        method: 'POST',
        body: data,
    });
}

export default PostRequest;