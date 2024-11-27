function login() {
    const uid = document.getElementById('uid').value.trim();
    const password = document.getElementById('password').value.trim();
    const errorMessage = document.getElementById('error-message');

    // 简单的输入验证
    if (!uid || !password) {
        errorMessage.style.display = 'block';
        errorMessage.textContent = '请输入账号和密码。';
        return;
    }

    // 清空错误消息
    errorMessage.style.display = 'none';

    // 发送登录请求
    fetch('/loginTo/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: uid, password: password })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('登录失败，检查您的账号或密码。');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            // 登录成功，重定向或显示成功消息
            window.location.href = '/'; // 根据需求调整路径
        } else {
            // 显示后端返回的错误消息
            errorMessage.style.display = 'block';
            errorMessage.textContent = data.message || '登录失败。';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        errorMessage.style.display = 'block';
        errorMessage.textContent = error.message || '登录时发生错误。';
    });
}

function regist() {
    const uid = document.getElementById('uid2').value.trim();
    const password = document.getElementById('password2').value.trim();
    const repassword = document.getElementById('repassword').value.trim();
    const errorMessage = document.getElementById('error-message2');


    // 简单的输入验证
    if (!uid || !password){
        errorMessage.style.display = 'block';
        errorMessage.textContent = '请输入账号和密码。';
        return;
    }
    if (password != repassword){
        document.getElementById('repassword').value = "";
        errorMessage.style.display = 'block';
        errorMessage.textContent = '两次输入密码不一致。';
        return;
    }

    // 清空错误消息
    errorMessage.style.display = 'none';

    // 发送登录请求
    fetch('/registTo/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: uid, password: password})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('注册失败，检查您的账号或密码。');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            // 登录成功，重定向或显示成功消息
            window.location.href = '/'; // 根据需求调整路径
        } else {
            // 显示后端返回的错误消息
            errorMessage.style.display = 'block';
            errorMessage.textContent = data.message || '注册失败。';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        errorMessage.style.display = 'block';
        errorMessage.textContent = error.message || '注册时发生错误。';
    });
}








const toggleButton = document.getElementById('toggleForm');
const loginForm = document.querySelector('.login-form');
const registrationForm = document.querySelector('.registration-form');
const formPanel = document.querySelector('.form-panel');
const registrationPanel = document.querySelector('.registration-panel');
const panelTitle = document.querySelector('.panel-title');
const subTitle = document.querySelector('.subTitle');
let isRegistrationMode = false;

function toggleLoginAndRegistration() {
    if (isRegistrationMode) {
        registrationPanel.style.left = '640px';
        formPanel.style.left = '0';
        toggleButton.innerText = '注册';
        panelTitle.innerText = '还未注册？';
        subTitle.innerText = '立即注册，发现大量机会！';
        setTimeout(() => {
            loginForm.style.display = 'flex';
            registrationForm.style.display = 'none';
        }, 300);
    } else {
        registrationPanel.style.left = '0';
        formPanel.style.left = '260px';
        toggleButton.innerText = '登录';
        panelTitle.innerText = '已有帐号？';
        subTitle.innerText = '有帐号就登录吧，好久不见了！';
        setTimeout(() => {
            loginForm.style.display = 'none';
            registrationForm.style.display = 'flex';
        }, 300);
    }
    isRegistrationMode = !isRegistrationMode;
}

toggleButton.addEventListener('click', toggleLoginAndRegistration);