/**
 * Scroll to bottom automatically after 500ms of the page load.
 */
scrollToBottom = () => {
  setTimeout(() => {
    const contents = document.getElementById('contents');
    contents.scrollTop = contents.scrollHeight;
  }, 500);
};
scrollToBottom();
