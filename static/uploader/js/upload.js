document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file-input');
    const uploadButton = document.getElementById('upload-button');
    const uploadStatus = document.getElementById('upload-status');
    const form = document.getElementById('file-upload-form');
    const loginBtn = document.getElementById('login-btn');
    const profileBtn = document.getElementById('profile-btn');
    
    uploadButton.addEventListener('click', (e) => {
        e.preventDefault();

        if (form.checkValidity()) {
            const fileName = document.querySelector('#file-upload-form #file-name').value;
            const file = fileInput.files[0];
            const expirationDate = document.querySelector('#file-upload-form #expiration-date').value;

            const formData = new FormData();
            formData.append('file_name',fileName)
            formData.append('file', file);
            formData.append('expiration_date', expirationDate);

            const csrfToken = getCookie('csrftoken');
            console.log(formData)
            fetch('/', {
                method: 'POST',
                redirect: 'follow',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                body: formData
            })
            .then((response) => {
                if (response.ok) {
                    uploadStatus.innerHTML = 'File uploaded successfully!';
                    window.location.replace(response.url)
                } else {
                    uploadStatus.innerHTML = 'Error uploading file.';
                }
            })
            .catch((error) => {
                uploadStatus.innerHTML = 'Error uploading file.';
                console.log(error)
            });
        } else {
            uploadStatus.innerHTML = 'Please fill in the required fields.';
        }
    });
    if (loginBtn){
        loginBtn.addEventListener('click', () => {
            window.location.href = '/accounts/login';
        });
    }
    else{
        profileBtn.addEventListener('click', () => {
            window.location.href = '/accounts/myfiles';})
        }

    // Function to get a cookie by
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});