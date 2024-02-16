import * as dotenv from 'dotenv';
import OpenAI from 'openai';
import express from 'express';
import cors from 'cors';

dotenv.config();

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

const app = express();

/**
 * Forward the POST request to OpenAI.
 * 
 * @returns - 
 */
app.post('/chat', async (req, res): Promise<void> => {
  try {
    const completion: OpenAI.Chat.ChatCompletion = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'user', content: req.body.question }]
    });
    res.status(200).json({ message: completion.choices[0].message.content });
  } catch (err: any) {
    res.status(400).json({ message: err.message });
  }
});

app.use(express.static('dist'));
app.use(cors);

const port = '9000';
app.listen('9000', () => {
  console.info(`CORS-enabled server running at localhost on port: ${port}.`);
});
