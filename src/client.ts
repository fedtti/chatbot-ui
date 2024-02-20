/**
 * Send a message as a question to OpenAI.
 */
const sendMessage = async (evt: any): Promise<any> => {
  evt.preventDefault();
  const messages = (<HTMLDivElement>document.querySelector('#messages'));
  const message: string = (<HTMLInputElement>document.querySelector('#message')).value;

  if (!message) { return; } // Stop if message is empty.

  const question: HTMLDivElement = document.createElement('div');
  question.classList.add('question');
  question.innerHTML = `<div class="message"><p>${message.toString()}</p></div>`;
  messages.append(question);

  (<HTMLInputElement>document.querySelector('#message')).value = ''; // Reset the input field.

  await fetch('http://localhost:9000/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ question: message })
  })
    .then((res) => {
      if (res.ok) { return res.json(); }
    })
    .then((data) => {
      if (data.message) {
        const answer: HTMLDivElement = document.createElement('div');
        answer.classList.add('answer', 'd-flex');
        answer.innerHTML = `<div class="message"><p>${data.message.toString()}</p></div>`;
        messages.append(answer);
        const avatar: HTMLDivElement = document.createElement('div');
        avatar.classList.add('avatar');
        answer.append(avatar);
        avatar.innerHTML = '<img src="../img/bot.svg" alt="OpenAI Logo" height="32" width="32">';
      }
    })
    .catch((err: any) => {
      console.error(err);
    });
};
const button = (<HTMLButtonElement>document.querySelector('.btn.btn-primary'));
button.addEventListener('click', sendMessage, false);
