function handleLogin(event) {
    event.preventDefault();
  
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const message = document.getElementById("message");
  
    // Usuário e senha "fakes" pra simulação
    const usuarios = [
      { email: "admin@teuzin.com", senha: "123456" },
      { email: "user@teuzin.com", senha: "senha123" },
    ];
  
    const usuarioValido = usuarios.find(
      (user) => user.email === email && user.senha === password
    );
  
    if (usuarioValido) {
      message.style.color = "#00ff99";
      message.textContent = "Login feito com sucesso! 🔓";
      // Aqui pode redirecionar com window.location.href = "painel.html";
    } else {
      message.style.color = "#ff4d4d";
      message.textContent = "Email ou senha inválidos! 😢";
    }
  }
  