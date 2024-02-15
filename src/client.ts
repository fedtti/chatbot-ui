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
  question.innerHTML = message;
  messages.appendChild(question);

  (<HTMLInputElement>document.querySelector('#message')).value = ''; // Reset the input field.

  const res = await fetch('/chat', {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ question: message })
  });

  const data: any = await res.json();

  if (!!data.message) {
    const answer: HTMLDivElement = document.createElement('div');
    answer.classList.add('answer');
    answer.innerHTML = data.message;
    messages.appendChild(answer);
  }
};
const button = (<HTMLButtonElement>document.querySelector('.btn.btn-primary'));
button.addEventListener('click', sendMessage, false);
