(function () {
  "use strict";
  // 手機選單
  var b = document.querySelector(".burger"),
      m = document.querySelector(".menu");
  if (b && m) {
    b.addEventListener("click", function () {
      var o = m.classList.toggle("open");
      b.setAttribute("aria-expanded", o ? "true" : "false");
    });
    m.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        m.classList.remove("open");
        b.setAttribute("aria-expanded", "false");
      }
    });
  }
  // 捲動淡入
  var r = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && r.length) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: .12 });
    r.forEach(function (e) { io.observe(e); });
  } else {
    r.forEach(function (e) { e.classList.add("in"); });
  }
  // 數據數字滾動（捲到時從 0 跑到目標值）
  var counts = document.querySelectorAll(".count");
  if ("IntersectionObserver" in window && counts.length) {
    var cio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, to = parseInt(el.getAttribute("data-to"), 10) || 0, t0 = null;
        function tick(ts) {
          if (!t0) t0 = ts;
          var p = Math.min((ts - t0) / 1100, 1);
          el.textContent = Math.round((1 - Math.pow(1 - p, 3)) * to);
          if (p < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
        cio.unobserve(el);
      });
    }, { threshold: .6 });
    counts.forEach(function (e) { cio.observe(e); });
  }

  // header logo 組裝：進站後播一次，滑鼠移入再播
  var hb = document.querySelector(".top .brand");
  if (hb && hb.querySelector(".bmark")) {
    var playB = function () {
      hb.classList.remove("assemble"); void hb.offsetWidth; hb.classList.add("assemble");
    };
    hb.addEventListener("mouseenter", playB);
    if (document.querySelector(".intro")) setTimeout(playB, 3900); // 首頁：開場結束後才組裝
    else playB();                                                 // 其他頁：載入即組裝
  }

  // 諮詢表單（尚未接後端，先給明確回覆並引導來電來信）
  var f = document.querySelector(".cform");
  if (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var res = f.querySelector(".form-result");
      if (res) res.textContent = "感謝您的來信！線上表單正在設定中，煩請直接來電 02-2600-5619 或來信 alechu2628@gmail.com，我們將盡快與您聯繫。";
    });
  }
})();
