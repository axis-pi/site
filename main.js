document.querySelectorAll('.logo_simbolo').forEach(function(logo) {
  logo.style.cursor = 'pointer';
  logo.addEventListener('click', function() {
    window.location.href = 'index.html';
  });
});

document.querySelectorAll('.menu-toggle').forEach(function(btn) {
  btn.addEventListener('click', function(e) {
    e.stopPropagation();
    var nav = btn.parentElement.querySelector('.nav');
    if (nav) nav.classList.toggle('active');
  });
});

// Fecha o menu ao clicar fora
window.addEventListener('click', function(e) {
  document.querySelectorAll('.nav.active').forEach(function(nav) {
    var btn = nav.parentElement.querySelector('.menu-toggle');
    if (!nav.contains(e.target) && (!btn || !btn.contains(e.target))) {
      nav.classList.remove('active');
    }
  });
});