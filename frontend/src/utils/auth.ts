// Function to set the token in local storage
function setToken(token: string, refreshToken?: string) {
    localStorage.setItem('authToken', token);
    localStorage.setItem('refreshToken', refreshToken || '');
}

// Function to get the token from local storage
function getToken() {
    return localStorage.getItem('authToken') || '';
}

function getRefreshToken() {
    return localStorage.getItem('refreshToken') || '';
}

export { setToken, getToken, getRefreshToken };