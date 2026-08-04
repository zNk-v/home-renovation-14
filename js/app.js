/* ============================================================
   Home Rénovation 14 — interactions
   ============================================================ */
(function () {
  'use strict';

  var TEL = '+33658941908';

  /* ⚠️ À RENSEIGNER : e-mail où arrivent les demandes de devis.
     Tant que la chaîne est vide, le formulaire bascule directement sur le SMS
     plutôt que d'envoyer dans le vide. */
  var CONTACT_EMAIL = '';

  /* ---------- Année du footer ---------- */
  var an = document.getElementById('an');
  if (an) an.textContent = new Date().getFullYear();

  /* ============================================================
     Coupe de toit — repères + panneau
     ============================================================ */
  var COUCHES = [
    {
      k: 'Repère 1 — couverture',
      t: 'Les ardoises',
      p: "La peau du toit. Chaque ardoise est tenue par un crochet ou deux clous et recouvre "
       + "largement celle du rang du dessous. Une seule qui glisse et l'eau entre par-dessous, "
       + "souvent à plusieurs mètres de l'endroit où la tache apparaît au plafond.",
      a: "Ici, ce sont les ardoises de rive qui partent en premier, soulevées par les coups de vent d'ouest."
    },
    {
      k: 'Repère 2 — support',
      t: 'Liteaux et contre-lattage',
      p: "Les tasseaux de bois qui portent les ardoises, posés sur un contre-lattage qui ménage "
       + "une lame d'air. C'est cette lame d'air qui laisse sécher la sous-face de la couverture "
       + "après chaque pluie.",
      a: "Un liteau pourri ne se voit pas d'en bas : les ardoises tiennent, puis lâchent d'un coup par plaques."
    },
    {
      k: 'Repère 3 — étanchéité',
      t: "L'écran sous-toiture",
      p: "Un film posé sous les liteaux qui récupère la condensation et les infiltrations passées "
       + "par la couverture, puis les renvoie vers la gouttière. Beaucoup de maisons d'avant les "
       + "années 80 n'en ont pas du tout.",
      a: "Sans écran, la moindre ardoise cassée mouille directement l'isolant et la charpente."
    },
    {
      k: 'Repère 4 — isolation',
      t: "L'isolant et le plafond",
      p: "Laine posée entre et sous les chevrons, puis la plaque de plâtre. C'est la couche qui "
       + "vous coûte de l'argent tous les mois quand elle est tassée, mouillée ou mal jointoyée.",
      a: "Un isolant qui a pris l'eau ne sèche pas seul : il faut le déposer, pas juste boucher la fuite."
    },
    {
      k: 'Repère 5 — structure',
      t: 'La charpente',
      p: "Chevrons, pannes et fermes. Elle encaisse le poids de la couverture, de la neige et la "
       + "prise au vent de tout le pan. Une charpente saine tolère beaucoup, mais elle ne pardonne "
       + "pas une infiltration qu'on laisse courir des années.",
      a: "Le bois noirci ou spongieux au droit d'une fuite change complètement le chiffrage du chantier."
    },
    {
      k: 'Repère 6 — évacuation',
      t: 'Gouttière et descente',
      p: "Tout ce que le toit reçoit finit là. Gouttière, crochets, naissance, descente : "
       + "l'ensemble doit garder sa pente et rester libre de mousse et de feuilles.",
      a: "À moins de deux kilomètres du rivage, le sel ronge le zinc et l'acier avant tout le reste du toit."
    }
  ];

  var hotWrap = document.getElementById('hotspots');
  if (hotWrap) {
    var hots = Array.prototype.slice.call(hotWrap.querySelectorAll('.hot'));
    var elK = document.getElementById('cpK');
    var elT = document.getElementById('cpT');
    var elP = document.getElementById('cpP');
    var elA = document.getElementById('cpA');
    var courant = 0;

    function afficher(i, focus) {
      courant = i;
      var c = COUCHES[i];
      elK.textContent = c.k;
      elT.textContent = c.t;
      elP.textContent = c.p;
      elA.textContent = c.a;
      hots.forEach(function (b, j) {
        b.setAttribute('aria-selected', j === i ? 'true' : 'false');
        b.setAttribute('tabindex', j === i ? '0' : '-1');
      });
      if (focus) hots[i].focus();
    }

    hots.forEach(function (b, i) {
      b.addEventListener('click', function () { afficher(i, false); });
      b.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') n = (i + 1) % hots.length;
        else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') n = (i - 1 + hots.length) % hots.length;
        else if (e.key === 'Home') n = 0;
        else if (e.key === 'End') n = hots.length - 1;
        if (n !== null) { e.preventDefault(); afficher(n, true); }
      });
    });

    afficher(0, false);
  }

  /* ============================================================
     Montage de la coupe au scroll
     Les six couches apparaissent dans l'ordre où on les pose sur un vrai
     chantier : plafond, isolant, chevrons, écran, liteaux, ardoises.
     La classe .anim-prete n'est posée qu'ici — sans JS, tout reste visible.
     ============================================================ */
  var fig = document.querySelector('.coupe-fig');
  if (fig) {
    if (!('IntersectionObserver' in window)) {
      fig.classList.add('anim-prete', 'on');
    } else {
      fig.classList.add('anim-prete');
      var obs = new IntersectionObserver(function (entrees) {
        entrees.forEach(function (e) {
          if (!e.isIntersecting) return;
          fig.classList.add('on');
          obs.disconnect();
        });
      }, { threshold: 0.3 });
      obs.observe(fig);

      /* Filet de sécurité : si la figure est déjà à l'écran au chargement,
         certains navigateurs ne déclenchent pas l'observateur assez tôt. */
      requestAnimationFrame(function () {
        var r = fig.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.7 && r.bottom > 0) fig.classList.add('on');
      });
    }
  }

  /* ============================================================
     FAQ — accordéon, hauteur mesurée
     ============================================================ */
  Array.prototype.forEach.call(document.querySelectorAll('.faq-q'), function (btn) {
    var panneau = btn.parentNode.nextElementSibling;

    btn.addEventListener('click', function () {
      var ouvert = btn.getAttribute('aria-expanded') === 'true';

      if (ouvert) {
        panneau.style.height = panneau.scrollHeight + 'px';
        requestAnimationFrame(function () { panneau.style.height = '0px'; });
      } else {
        panneau.style.height = panneau.scrollHeight + 'px';
        panneau.addEventListener('transitionend', function fin(e) {
          if (e.propertyName !== 'height') return;
          panneau.style.height = 'auto';
          panneau.removeEventListener('transitionend', fin);
        });
      }
      btn.setAttribute('aria-expanded', String(!ouvert));
    });
  });

  /* ============================================================
     Formulaire de devis
     ============================================================ */
  var form = document.getElementById('devis');
  if (!form) return;

  var boite = document.getElementById('formBox');
  var merci = document.getElementById('merci');
  var merciTxt = document.getElementById('merciTxt');
  var bouton = document.getElementById('submitBtn');

  function champDe(input) { return input.closest('.champ'); }

  function valide() {
    var ok = true;
    var nom = form.nom, tel = form.telephone;

    [nom, tel].forEach(function (i) { champDe(i).classList.remove('err'); });

    if (!nom.value.trim()) { champDe(nom).classList.add('err'); ok = false; }

    var chiffres = tel.value.replace(/\D/g, '');
    if (chiffres.length < 9 || chiffres.length > 13) { champDe(tel).classList.add('err'); ok = false; }

    if (!ok) {
      var premier = form.querySelector('.champ.err input');
      if (premier) premier.focus();
    }
    return ok;
  }

  function resume() {
    return 'Devis — ' + form.type_travaux.value
      + ' | ' + form.nom.value.trim()
      + ' | ' + form.telephone.value.trim()
      + (form.ville.value.trim() ? ' | ' + form.ville.value.trim() : '')
      + (form.message.value.trim() ? ' | ' + form.message.value.trim() : '');
  }

  function replierSurSMS() {
    var lien = 'sms:' + TEL + (navigator.userAgent.indexOf('Mac') > -1 ? '&' : '?')
             + 'body=' + encodeURIComponent(resume());
    merciTxt.innerHTML = "L'envoi automatique n'a pas abouti. Votre SMS s'ouvre avec le résumé "
      + "de la demande&nbsp;: il n'y a plus qu'à l'envoyer.<br>Ou appelez le "
      + '<a href="tel:' + TEL + '">06&nbsp;58&nbsp;94&nbsp;19&nbsp;08</a>.';
    boite.classList.add('done');
    merci.classList.add('on');
    merci.scrollIntoView({ block: 'center' });
    window.location.href = lien;
  }

  function reussite() {
    boite.classList.add('done');
    merci.classList.add('on');
    merci.scrollIntoView({ block: 'center' });
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!valide()) return;

    if (!CONTACT_EMAIL) { replierSurSMS(); return; }

    bouton.disabled = true;
    bouton.textContent = 'Envoi…';

    fetch('https://formsubmit.co/ajax/' + CONTACT_EMAIL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({
        _subject: 'Devis site — ' + form.type_travaux.value + ' — ' + form.nom.value.trim(),
        Nom: form.nom.value.trim(),
        Telephone: form.telephone.value.trim(),
        Commune: form.ville.value.trim(),
        Travaux: form.type_travaux.value,
        Message: form.message.value.trim()
      })
    })
      .then(function (r) { if (!r.ok) throw new Error('http ' + r.status); return r.json(); })
      .then(reussite)
      .catch(replierSurSMS)
      .then(function () { bouton.disabled = false; bouton.textContent = 'Recevoir mon devis gratuit'; });
  });
})();
