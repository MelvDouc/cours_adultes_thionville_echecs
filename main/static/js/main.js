import setHeaderHeight from "./functions/setHeaderHeight.js";

document.addEventListener("DOMContentLoaded", () => {
  setHeaderHeight();
  window.addEventListener("resize", setHeaderHeight);
});