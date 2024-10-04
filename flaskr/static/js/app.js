/**
 * Scroll to bottom automatically after 500ms of the page load.
 */
scrollToBottom = () => {
  setTimeout(() => {
    const content = document.getElementById('content');
    content.scrollTop = content.scrollHeight;
  }, 500);
};
scrollToBottom();
