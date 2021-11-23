document.addEventListener("DOMContentLoaded", () => {

  (function setHeaderHeight() {
    const header = document.querySelector("header");
    const headerHeight = getComputedStyle(header).height;
    document.documentElement.style.setProperty("--header-height", headerHeight);
  })();

});