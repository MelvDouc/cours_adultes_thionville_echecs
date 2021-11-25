const root = document.documentElement;
const header = document.querySelector("header");

export default function setHeaderHeight() {
  const headerHeight = getComputedStyle(header).height;
  root.style.setProperty("--header-height", headerHeight);
}