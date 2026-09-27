/* Dane Anderson Window Cleaning — global nav/footer loader.
   Lives at /includes/nav-footer-loader.js and is referenced from every page <head>.
   Fetches the shared nav + footer, injects them, then wires active-link state and the year. */
(function () {
  function fetchInclude(path, cb) {
    var x = new XMLHttpRequest();
    x.open('GET', path, true);
    x.onreadystatechange = function () {
      if (x.readyState === 4) cb(x.status === 200 ? x.responseText : '');
    };
    x.send();
  }

  function injectTop(html) {
    if (!html) return;
    var wrap = document.createElement('div');
    wrap.innerHTML = html;
    var frag = document.createDocumentFragment();
    while (wrap.firstChild) frag.appendChild(wrap.firstChild);
    document.body.insertBefore(frag, document.body.firstChild);
  }

  function injectBottom(html) {
    if (!html) return;
    var wrap = document.createElement('div');
    wrap.innerHTML = html;
    while (wrap.firstChild) document.body.appendChild(wrap.firstChild);
  }

  function markActive() {
    var path = location.pathname.replace(/\/index\.html$/, '/');
    if (path.length > 1) path = path.replace(/\/+$/, '/');
    var links = document.querySelectorAll('.site-header nav.desktop a, .mobile-nav a');
    for (var i = 0; i < links.length; i++) {
      var href = links[i].getAttribute('href') || '';
      if (href.charAt(0) !== '/') continue;
      var match = href === '/' ? path === '/' : path.indexOf(href) === 0;
      if (match) links[i].setAttribute('aria-current', 'page');
    }
  }

  function setYear() {
    var y = document.getElementById('footer-year');
    if (y) y.textContent = new Date().getFullYear();
  }

  function boot() {
    var pending = 2;
    fetchInclude('/includes/nav.html', function (html) {
      injectTop(html);
      markActive();
      if (--pending === 0) setYear();
    });
    fetchInclude('/includes/footer.html', function (html) {
      injectBottom(html);
      if (--pending === 0) setYear();
      setYear();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
