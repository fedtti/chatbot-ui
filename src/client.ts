/**
 * Send a message as a question to OpenAI.
 */
const sendMessage = async (): Promise<any> => {
  const messages = (<HTMLDivElement>document.querySelector('#messages'));
  const message: string = (<HTMLInputElement>document.querySelector('#message')).value;

  if (!!message) { return; } // Stop if message is empty.

  const question = document.createElement('div');
  question.classList.add('question');
  question.innerHTML = message;
  messages.appendChild(question);

  (<HTMLInputElement>document.querySelector('#message')).value = ''; // Reset the input field.




};
const button = (<HTMLButtonElement>document.querySelector('button[type="submit"]'));
button.addEventListener('click', sendMessage, false);