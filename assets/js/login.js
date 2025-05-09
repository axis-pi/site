function handleLogin(event) {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const message = document.getElementById("message");

    // Usuários simulados
    const usuarios = [
        { email: "admin@axis.com", senha: "123456", tipo: "admin", destino: "projeto/admin.html" },
        { email: "user@axis.com", senha: "senha123", tipo: "user", destino: "projeto/user.html" }
    ];

    // Limpa mensagem
    message.textContent = "";

    if (!email || !password) {
        message.style.color = "#EE8308FF";
        message.textContent = "Preencha todos os campos! 😢";
        return;
    }

    const usuarioValido = usuarios.find(
        (user) => user.email === email && user.senha === password
    );

    if (usuarioValido) {
        message.style.color = "#28a745";
        message.textContent = "Login realizado com sucesso! Redirecionando...";
        setTimeout(() => {
            if (usuarioValido.tipo === "admin") {
                window.location.href = "projeto/admin.html";
            } else {
                window.location.href = "projeto/user.html";
            }
        }, 1000);
    } else {
        message.style.color = "#ff4d4d";
        message.textContent = "Email ou senha inválidos! 😢";
    }
}
